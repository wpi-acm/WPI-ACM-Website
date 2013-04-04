# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


ACMOfficers = [
    {
        'year' : '2013-2014',
        'members': [{
            'name': "Alexander Karp",
            'position': "President",
            'photo': "2013/alex.png"
        },{
            'name': "Taymon Beal",
            'position': "Vice President",
            'photo': "2013/taymon.png"
        },{
            'name': "Merrielle Ondreicka",
            'position': "Secretary",
            'photo': "2013/merrielle.png"
        },{
            'name': "Ian Naval",
            'position': "System Administrator",
            'photo': "2013/ian.png"
        },{
            'name': "Henrique Polido",
            'position': "Events Coordinator",
            'photo': "2013/henrique.png"
        }]
    },
    {
        'year' :'2012-2013',
        'members': [{
            'name': "Henrique Polido",
            'position': "President",
            'photo': "2011/henrique.png"
        },{
            'name': "Alex Karp",
            'position': "Vice-President",
            'photo': "2011/alex.png"
        },{
            'name': "Marc Green",
            'position': "Treasure",
            'photo': "2011/marc.png"
        },{
            'name': "Taymon Beal",
            'position': "Lab Manager",
            'photo': "2011/taymon.png"
        },{
            'name': "Thinh Nguyen",
            'position': "Secretary",
            'photo': "2011/thinh.png"
        },{
            'name': "Michael Checca",
            'position': "Events Coordinator",
            'photo': "2011/michael.png"
        },{
            'name': "Ian Naval",
            'position': "Sys. Admin",
            'photo': "2011/ian.png"
        }]
    },
    {
        'year' :'2011-2012',
        'members': [{
            'name': "Nate Thorn",
            'position': "President",
            'photo': "2010/nate.png"
        }]
    }
]



def members(request):
    return render_to_response('core/members.html', {'officers': ACMOfficers}, context_instance=RequestContext(request))
