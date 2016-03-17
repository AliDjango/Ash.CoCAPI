**AsH.CoCAPI** is a module for calling the official Clash of Clans Api in Python.
It supports all available methods that The Api supports
In order to use this module,you have to get a Token from https://developer.clashofclans.com
as a quick view on the functions you can use this code.
**Please See the Docs branch for a complete documentation and examples**

    from ash.cocapi import *
    
    api = cocapi('token')
    #searching Clan
    results = api.search_clan(name='Clan Name Here')
    """
    you can use these to make and advanced search
    name-warfrequency-locationid-minmembers-maxmembers--minclanpoints-minclanlevel-limit-after-before"""
    tag=results.items[0].tag#to use other functions with this example
    for result in results.items:
        print(i.name,i.tag,i.members)
    
    #getting a specific clan using Clantag
    result = api.get_clantag(tag)
    print(result.name,result.stag)
    
    #getting clan members using clantag
    results = api.get_clan_members(tag)
    for result in results.items:
        print(result.name, result.role)
    
    #getting all locations
    results = api.get_locations()
    for result in result.sitems:
        print(result.id, result.name)
    
    #getting a locationid information
    result = api.get_locationid(32000115)
    print(result.name)
    
    #getting ranking for a specific location,you can get 'players' or 'clans'
    results = api.get_location_ranking(32000115, 'players')
    for result in results.items:
        print(result.name)
    
    #getting all leagues
    results = api.get_leagues()
    for result in result.sitems:
        print(result.name)


