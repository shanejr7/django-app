from django.shortcuts import render
from store.models import Store, User, Auction, Stakeholder
from django.db.models import F
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from django.utils.html import strip_tags
import datetime


# Create your views here.

def store_detail(request):

    user_store_obj1 = Store.objects.filter(pk__in=[1, 2, 3,4]).values('user__id','user__username','user__email','user__license','user__timestamp',
        'id','product','title','body','price','quantity','auction','product_type', 'contract_type','service_type',
        'data_type','season','views','img_url','address', 'duration_timestamp','timestamp')

    user_store_obj2 = Store.objects.filter(id=5).values('user__id','user__username','user__email','user__license','user__timestamp',
        'id','product','title','body','price','quantity','auction','product_type', 'contract_type','service_type',
        'data_type','season','views','img_url','address', 'duration_timestamp','timestamp')

    user_store_obj3 = Store.objects.filter(pk__in=[6, 7, 8,9]).values('user__id','user__username','user__email','user__license','user__timestamp',
        'id','product','title','body','price','quantity','auction','product_type', 'contract_type','service_type',
        'data_type','season','views','img_url','address', 'duration_timestamp','timestamp')
    user_store_obj4 = Store.objects.filter(id=10).values('user__id','user__username','user__email','user__license','user__timestamp',
        'id','product','title','body','price','quantity','auction','product_type', 'contract_type','service_type',
        'data_type','season','views','img_url','address', 'duration_timestamp','timestamp')

    user_store_obj5 = Store.objects.filter(pk__in=[11, 12, 13,14]).values('user__id','user__username','user__email','user__license','user__timestamp',
        'id','product','title','body','price','quantity','auction','product_type', 'contract_type','service_type',
        'data_type','season','views','img_url','address', 'duration_timestamp','timestamp')

    user_store_top_quality_rank_obj = User.objects.filter(quality_rank__gte=80)[:8].values('id','username','img_url','email','license','quality_rank','timestamp')

    context = {

        "user_store_objs1": user_store_obj1,
        "user_store_objs2": user_store_obj2,
        "user_store_objs3": user_store_obj3,
        "user_store_objs4": user_store_obj4,
        "user_store_objs5": user_store_obj5,
        "user_store_quality_rank_objs": user_store_top_quality_rank_obj,

    }

    return render(request, "store_detail.html", context)

def user_store_detail(request, uid,sid):

    owner_obj = []
    store_obj = []
    store_auction_obj = []
    store_auction_history_obj = []
    error = []

    uid = strip_tags(uid)
    sid = strip_tags(sid)


    if int(uid) and int(sid):
        owner_obj = User.objects.get(pk=uid)

        store_obj = Store.objects.filter(user_id=owner_obj.id,id=sid)

        Store.objects.filter(user_id=owner_obj.id,id=sid).update(views=F('views')+1)

        store_auction_obj = Auction.objects.filter(store_id=sid).values('store__id','store__auction','store__quantity','user__username','user__img_url','user_id','highest_bid',
            'accepted_bid','application','price','quantity','timestamp').order_by('-price')

        store_auction_history_obj = Auction.objects.filter(store_id=sid).values('store__id','store__auction','store__quantity','user__username','user__img_url','user_id','highest_bid',
            'accepted_bid','application','price','quantity','timestamp').order_by('timestamp')
 
    else:
        error = "This page is empty. Please come back soon."

    context = {

        "products": store_obj,
        "users": owner_obj,
        "auction_users": store_auction_obj,
        "auction_history": store_auction_history_obj, 
        "error": error,

    }

    return render(request, "user_store_detail.html", context)

@requires_csrf_token
def create_auction(request):

    error = []

    store_id = strip_tags(request.POST.get('storeID'))
    owner_id = strip_tags(request.POST.get('ownerID'))
    user_auction_id = strip_tags(request.POST.get('userAuctionID'))
    bid_amount = strip_tags(request.POST.get('bidAmount'))

    owner_obj = User.objects.get(pk=owner_id)

    store_obj = Store.objects.filter(user_id=owner_obj.id,id=store_id)
    store_auction_obj = Auction.objects.filter(store_id=store_id).values('store__id','store__auction','store__quantity','user__username','user__img_url','user_id','highest_bid',
            'accepted_bid','application','price','quantity','timestamp').order_by('-price')

    store_auction_history_obj = Auction.objects.filter(store_id=store_id).values('store__id','store__auction','store__quantity','user__username','user__img_url','user_id','highest_bid',
            'accepted_bid','application','price','quantity','timestamp').order_by('timestamp') 

    if  int(store_id) and  int(owner_id) and  int(user_auction_id) and float(bid_amount):
        date = datetime.datetime.now()
        time_stamp = date.strftime('%m-%d-%Y %H:%M')
        create_user_auction = Auction(store_id=store_id ,user_id=user_auction_id,accepted_bid=False,application=False,price=bid_amount, timestamp=time_stamp)
        create_user_auction.save()

    else:
        error = "Bid was not processed."

    context = {

        "products": store_obj,
        "users": owner_obj,
        "error": error,

    }

    return render(request, "user_store_detail.html", context)


@requires_csrf_token
def purchase(request):

    error = []

    store_id = strip_tags(request.POST.get('storeID'))
    owner_id = strip_tags(request.POST.get('ownerID'))
    user_auction_id = strip_tags(request.POST.get('userAuctionID'))
    bid_amount = strip_tags(request.POST.get('bidAmount'))

    owner_obj = User.objects.get(pk=owner_id)

    store_obj = Store.objects.filter(user_id=owner_obj.id,id=store_id)
    Store.objects.filter(user_id=owner_obj.id,id=store_id).update(quantity=F('quantity')-1)
    store_auction_obj = Auction.objects.filter(store_id=store_id).values('store__id','store__auction','store__quantity','user__username','user__img_url','user_id','highest_bid',
            'accepted_bid','application','price','quantity','timestamp').order_by('-price')

    store_auction_history_obj = Auction.objects.filter(store_id=store_id).values('store__id','store__auction','store__quantity','user__username','user__img_url','user_id','highest_bid',
            'accepted_bid','application','price','quantity','timestamp').order_by('timestamp') 

    if  int(store_id) and  int(owner_id) and  int(user_auction_id) and (float(bid_amount)):
        date = datetime.datetime.now()
        time_stamp = date.strftime('%m-%d-%Y %H:%M')
        create_user_auction = Auction(store_id=store_id ,user_id=user_auction_id,accepted_bid=False,application=False,price=bid_amount, timestamp=time_stamp)
        create_user_auction.save()

    else:
        error = "Purchase was not processed."

    context = {

        "products": store_obj,
        "users": owner_obj,
        "error": error,

    }

    return render(request, "user_store_detail.html", context)

@requires_csrf_token
def apply(request):

    error = []

    store_id = strip_tags(request.POST.get('storeID'))
    owner_id = strip_tags(request.POST.get('ownerID'))
    user_auction_id = strip_tags(request.POST.get('userAuctionID'))

    owner_obj = User.objects.get(pk=owner_id)

    store_obj = Store.objects.filter(user_id=owner_obj.id,id=store_id)
    store_auction_obj = Auction.objects.filter(store_id=store_id).values('store__id','store__auction','store__quantity','user__username','user__img_url','user_id','highest_bid',
            'accepted_bid','application','price','quantity','timestamp').order_by('-price')

    store_auction_history_obj = Auction.objects.filter(store_id=store_id).values('store__id','store__auction','store__quantity','user__username','user__img_url','user_id','highest_bid',
            'accepted_bid','application','price','quantity','timestamp').order_by('timestamp') 

    if  int(store_id) and  int(owner_id) and  int(user_auction_id):
        date = datetime.datetime.now()
        time_stamp = date.strftime('%m-%d-%Y %H:%M')
        create_user_auction = Auction(store_id=store_id ,user_id=user_auction_id,accepted_bid=False,application=True,price=0.00, timestamp=time_stamp)
        create_user_auction.save()

    else:
        error = "Application was not processed."

    context = {

        "products": store_obj,
        "users": owner_obj,
        "error": error,

    }

    return render(request, "user_store_detail.html", context)

def activity(request):

    store_obj = []
    error = []

    store_obj = Store.objects.values('user__id','user__username','user__email','user__license','user__timestamp',
        'id','product','title','body','price','quantity','auction','product_type', 'contract_type','service_type',
        'data_type','season','views','img_url','address', 'duration_timestamp','timestamp').order_by('user__timestamp') 

  

    context = {

        "store": store_obj,  #// new store post
        "error": error,

    }
    
    return render(request, "activity.html",context)

      # query by timestamp
    # sort different table queries by timestamp -> merge into activity array list

        # select Store table and join with associated User

        # select User from Follow table and join with associated following User

        # select User from Like table and join with associated like Store 

        # select Auction table and associated Store , User

        # List<Activity> activ = new ArrayList<Activity>();

        # activ.add(store_obj) .. .get(0).setObjectTypeName("store") 
        # activ.add(follow_obj) .get(1).setObjectTypeName("follow") 
        # activ.add(like_obj)   .get(2).setObjectTypeName("like") 
        # activ.add(auction_obj)  .get(3).setObjectTypeName("auction") 
        
        # sort different table with different cloumns by timestamps with activ object
        # print correct html activity template based on obj types

        #loop activ object
        # if objType == type1:
            # this template
        # if objType == type2:
            # this template
        #......... etc
    #       context = {

    #     "store": store_obj,  #// new store post
    #     "follow": follow_obj, #// user just followed another user
    #     "like": like_obj,  #// user just liked a store
    #     "auction": auction_obj, #// user just made a auction submission
    #     "error": error,

    # }


def rankings(request):

    # query rankings of all users desc
    user_store_top_quality_rank_obj = []
    error = []

    user_store_top_quality_rank_obj = User.objects.values('id','username','img_url','email','license','quality_rank','timestamp')


    context = {

        "users":  user_store_top_quality_rank_obj,
        "error": error,

    }
    
    return render(request, "rankings.html",context)



