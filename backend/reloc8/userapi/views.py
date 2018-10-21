from django.shortcuts import render
from userapi.models import Client
from cityapi.models import City
from userapi.serializers import *
from rest_framework import status, generics, filters
from rest_framework.response import Response
from django.db import IntegrityError
from datetime import datetime, timedelta
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import requests
import json
from statistics import mean
import os
import datetime
from django.contrib.gis.measure import Distance

# Create your views here.


class CalcSuite(generics.ListCreateAPIView):
    queryset = City.objects.all()
    sales_tax = .15
    def tax_get(self, salary, city):
        state = city[-2:]
        headers = {'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUElfS0VZX01BTkFHRVIiLCJ"
                                     "odHRwOi8vdGF4ZWUuaW8vdXNlcl9pZCI6IjViY2JjNWE2NTRiOTIxNDdkYjI0ZmRhZCIsImh0dHA6Ly90"
                                     "YXhlZS5pby9zY29wZXMiOlsiYXBpIl0sImlhdCI6MTU0MDA4MjA3M30.QheSNYfM3hY_COVn-S2LW4Ska"
                                     "2NQiDxeMQKy6KwclyM",
                   'Cache-Control': "no-cache"
        }
        url = "https://taxee.io/api/v2/calculate/2018"
        payload = "filing_status=single&pay_rate=" + salary + "&state=" + state
        response = requests.request("POST", url, data=payload, headers=headers)
        tax = response.json()
        mx = response.text
        #['single']['FederalStatistics']['income_tax_brackets']['IncomeTaxBracket']['amount']
        #salary_tru = salary - tax
        return tax

    def get_housing(self, request, city):
        if "1_bed" in request.data['housing']:
            if request.POST.get('h_type','') == "modest":
                return city.lo_bed_price1
            elif request.POST.get('h_type','') == "average":
                return city.lo_bed_price2
            elif request.POST.get('h_type','') == "trendy":
                return city.lo_bed_price3

        elif "2_bed" in request.data['housing']:
            if request.POST.get('h_type','')=="modest":
                return city.mid_bed_price1
            elif request.POST.get('h_type','')=="average":
                return city.mid_bed_price2
            elif request.POST.get('h_type','') == "trendy":
                return city.mid_bed_price3

        elif "3_bed" in request.data['housing']:
            if request.POST.get('h_type','') == "modest":
                return city.hi_bed_price1
            elif request.POST.get('h_type','') == "average":
                return city.hi_bed_price2
            elif request.POST.get('h_type','') == "trendy":
                return city.hi_bed_price3

        elif "studio" == request.data['housing']:
            if request.POST.get('h_type','') == "modest":
                return city.stud_bed_price1
            elif request.POST.get('h_type','') == "average":
                return city.stud_bed_price2
            elif request.POST.get('h_type','') == "trendy":
                return city.stud_bed_price3


    def getDriver(self, request, curr_city):
        retval = 0
        if(request.data['vehicle']):
            retval = (curr_city.gas_gallon + curr_city.auto_maintenance_price) * (curr_city.miles_driven + curr_city.parking_price
                                                                         + curr_city.auto_insurance +curr_city.auto_tax)
        else:
            retval = curr_city.bus_pass
        return retval

    def getEntertainment(self, request, city):
        retval = 0
        if(request.data['ent_val'] == 0):
            retval = 0
        else:
            if(request.data['ent_val'] == 1):
                retval = ((4*city.drink_price)+(city.movie_price)+(.5*city.sports_leisure_price))*(1+self.sales_tax)
            elif (request.data['ent_val'] == 2):
                retval = ((8 * city.drink_price) + (5*city.movie_price) + (
                            1 * city.sports_leisure_price)) * (1+self.sales_tax)
            elif (request.data['ent_val'] == 3):
                retval = ((28 * city.drink_price) + (10*city.movie_price) + (
                            2 * city.sports_leisure_price)) * (1+self.sales_tax)
        return retval


    def getEatOut(self, flag, request, city, gotten_val):
        retval = 0
        if flag==0:
            retval = float(mean([city.low_dineout,city.mid_dineout,city.fast_food]))*(1+self.sales_tax)
        if flag==1:
            retval = gotten_val * float(request.data['din_out'])*4
        return retval

    def getGroceryMeal(self, city):
        retval = (mean([city.chicken_breast_lb, city.beef_lb])/2) + (mean([city.tomato_lb, city.potato_lb, city.onion_lb,
                 city.lettuce_lb])/4) + (mean([city.apples_lb, city.banana_lb]) / 4) +\
                  (mean([city.milk_gallon, city.bread_loaf, city.eggs_dozen])/6)

        return retval

    def getGrocery(self, request, per_meal):
        retval = (21 - int(request.data['din_out']))*per_meal*4
        return retval


    def startCalc(self, req):
        city = req.data['city_new']
        tax_data = self.tax_get(req.data['salary'], city)
        salary_after_tax = float(req.data['salary']) - (float(tax_data['annual']['fica']['amount']) + float(tax_data['annual']['state']['amount']) +\
                                                 float(tax_data['annual']['federal']['amount']))

        curr_city = City.objects.filter(city_name=city).first()
        print(curr_city.lo_bed_price1)

        housing_cost = self.get_housing(req, curr_city)
        utility_cost = curr_city.utility_price
        internet_cost = curr_city.internet_price
        driving_cost = self.getDriver(req, curr_city)
        pub_transp_sav = driving_cost - curr_city.bus_pass
        entertainment = self.getEntertainment(req, curr_city)

        eat_out_per_meal = self.getEatOut(0, req,curr_city, 0)
        eatout_cost = self.getEatOut(1, req, curr_city, eat_out_per_meal)

        grocery_per_meal = self.getGroceryMeal(curr_city)
        grocery_cost = self.getGrocery(req, grocery_per_meal)
        grocery_save = eat_out_per_meal - float(grocery_per_meal)

        tax_cost = float(req.data['salary']) - salary_after_tax
        food_cost = eatout_cost + float(grocery_cost)

        disposable_income = salary_after_tax - (float(housing_cost) + float(utility_cost) + float(internet_cost) + \
                                                float(driving_cost) + float(entertainment) + float(eatout_cost) + float(grocery_cost))


        #advice = getAdvice(housing_cost, salary_after_tax)
        final_set = {'housing_cost': float(housing_cost),'utility_cost': float(utility_cost),'internet_cost': float(internet_cost),
                     'driving_cost': float(driving_cost), 'entertainment_cost': float(entertainment),'tax_cost': float(tax_cost),
                     'disposable_income': float(disposable_income)}
        final_set =json.dumps(final_set)
        return final_set





class ClientActions(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        """
        Author: Daniel Boaitey
        Creates a new client object with all necessary information. Validation occurs in this method.
        """
        calculator = CalcSuite()
        try:
            #request.POST._mutable = True
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except IntegrityError:
            response_data = {
                "success": "False",
                "message": ""
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            raise e

        headers = self.get_success_headers(serializer.data)
        id_val = request.data["id"]
        response_data = {
            "success": "True",
            "message": Client.objects.count(),
            "performance": serializer.data,
        }
        valz = calculator.startCalc(request)

        return Response({valz}, status=status.HTTP_201_CREATED, headers=headers)
