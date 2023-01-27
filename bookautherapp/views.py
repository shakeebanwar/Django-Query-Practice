from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.db.models import F, Q, Value as V, When, Case
from decimal import Decimal
from django.db.models.functions import Concat, Coalesce,ExtractYear
import datetime
from django.db.models import Avg, Max, Min, Count


class books(APIView):
    def get(self,request):

        #Filter
        # bookes = Book.objects.filter(title="History").values()
        # bookes = Book.objects.filter(title__startswith="Rom").values()
        
        #-----------------------------------------------------------------------------------------------------
        # Books published in 2013
        # bookes = Book.objects.filter(published__year=2013).values()

        #------------------------------------------------------------------------------------------------------
        # Books published in the year 2000 or after
        # bookes = Book.objects.filter(published__year__gte=2000).values('published__year')

        #------------------------------------------------------------------------------------------------------
        # # Books published before the year 2000
        # bookes = Book.objects.filter(published__year__lt=2016).values('published__year')


        #-------------------------------------------------------------------------------------------------------
        # Between Dates
        # start_date = datetime.date(2012, 1, 1)
        # end_date = datetime.date(2014, 1, 3)
        # bookes = Book.objects.filter(published__range=(start_date, end_date)).values()

        #-------------------------------------------------------------------------------------------------------
        # Q and F Functions
        # bookes = Book.objects.filter(Q(published__year=2013) | Q(published__year=2016)).values('title')
        
        # Query books published by authors under 30 years old (this is not exactly true because years vary in length)
        
        # bookes = Book.objects.filter(published__lte=F("author__birth_date") + datetime.timedelta(days=365*30)).values()


        #----------------------------------------------------------------------------------------------------
        # for updation of models...
        # OLD CODE
            # reporter = Reporters.objects.get(name='Tintin')
            # reporter.stories_filed = F('stories_filed') + 1
            # reporter.save()

        # bookes = Book.objects.filter(title="Romance")
        # bookes.update(rating=F("rating") + 1)



        #------------------------------------------------------------------------------------------------------
        #Annotaion with respect to F function
        # bookes = Author.objects.annotate(full_name=Concat(F("firstname"), V(" "), F("lastname"))).values("full_name")
        # bookes = Author.objects.annotate(known_as=Coalesce(F("nickname"), F("firstname"))).values("known_as")



        #--------------------------------------------------------------------------------------------------------
        # # Add a new field with the rating multiplied by 100
        # bookes = Book.objects.annotate(rating_multiplied=F("rating") * 100).values("rating_multiplied")

        #---------------------------------------------------------------------------------------------------

        # Aggregate Avg, min, Max, Count
        # {'price__avg': Decimal('13.50')}
        # bookes = Book.objects.aggregate(Avg("price"))
        
        # # {'price__max: Decimal('13.50')}
        # bookes = Book.objects.aggregate(Max("price"))
        
        # {'published__min': datetime.date(1866, 7, 25)}
        # bookes = Book.objects.aggregate(Min("published"))
        
        # Count Books
        # bookes = Author.objects.annotate(num_books=Count("books")).values("num_books")

        #--------------------------------------------------------------------------------------------------------
       
       
        # Case...When

        

    #     bookes = Book.objects.annotate(discounted_price=Case(
    #     When(category="Romance", then=  F("price") - 10 * F("price") /100 ),
    #     When(category="Historical fiction", then=  F("price") - 5 * F("price") /100 ),
    #     default=None
    # )).values('category','price', 'discounted_price')



        
        
        #Add  a new field with the authors age at the time of publishing the book
        
        
        #bookes = Book.objects.annotate(author_age=ExtractYear(F("published")) - ExtractYear(F("author__birth_date"))).values("author_age")
        
        
      
        return Response({'status': True, 'data': bookes})




