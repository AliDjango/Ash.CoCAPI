**Functions**
=============

Note : before using These Functions,You must make an instance of cocapi Class with your token:
```
from ash.cocapi import cocapi
"""
You can directly use library file,copy cocapi.py file to your directory then change the import statement in this way:
from cocapi import cocapi
"""
token = "your token here as str"
api = cocapi(token)
```


----------


Search_clan()
-------------

With this function,you can search for a clan by:

 - name
 - warfrequency: 
 - locationid
 - minmembers
 - maxmembers
 - minclanpoints
 - minclanlevel
 
You should use Atleast one of them.

`search_clan(name=None, warfrequency=None, locationid=None, minmembers=None, maxmembers=None,
                 minclanpoints=None, minclanlevel=None, limit=10, after=None, before=None)`
                 
here are some Examples of this function:

search for clan by name:

```
result = api.search_clan(name='Clash of Clans')
for result in results:
	print("clan tag : {} , clan name : {}".format(result.tag, result.name))
```

search for clan by minimum number of members:

```
result = api.search_clan(minmembers=10)
for result in results:
	print("clan tag : {} , clan name : {}".format(result.tag, result.name))
```

search for a clan by the name and war frequency:

```
result = api.search_clan(name='Clash of Clans', warfrequency="always")
for result in results:
	print("clan tag : {} , clan name : {}".format(result.tag, result.name))
```


----------


get_clantag()
-------------
If you already have a clan tag, you may get the clan information using clan tag.

the only argument is clantag,starting with #:

`get_clantag(clantag)`

example:

`api.get_clantag("#8J2VQJYL")`


----------


get_clan_members()
------------------
If you already have a clan tag, you may get the clan members using clan tag.

the only argument is clantag starting with #:

`get_clan_members(clantag)`

example:

`api.get_clan_members("#8J2VQJYL")`


----------

get_locations()
---------------
If you need to work with locations,you may find all location IDs with their information with this function.

`get_locations()`

There is no argument for this command.

example:

`api.get_locations()`


----------

get_locationid()
----------------

If you have a locationID , you may get it's information using `get_locationid(locationid)`.

The only argument for this function is the locationID.

example:
`api.get_locationid(32000115)`


----------

get_location_ranking()
----------------------
Need to get Player/clan Rankings?

Want to see the rankings for a special location?!

if so,use `get_location_ranking()` to achieve this!

arguments for this function is : `LocationID, Mode`

Mode can be "players" or "clans.

example:

`api.get_location_ranking(32000115,'players')`
`api.get_location_ranking(32000115,'clans')`

----------

get_leagues()
-------------
With this function, you can get informations about leagues.

`get_leagues()`

example:

`api.get_leagues()`
