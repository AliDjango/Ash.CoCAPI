from collections import namedtuple

import requests

base_key = 'v1'
base_url = 'https://api.clashofclans.com/{base_key}/'.format(base_key=base_key)
from urllib.parse import quote


def fetch(url, params=None):
    result = requests.get(base_url + url, headers=headers, params=params)
    if result.status_code != 200:
        return [result.status_code, result.json()]
    return result.json()


def get_results(rclass, fetched):
    if isinstance(fetched, list):
        return Error.from_result(fetched)
    else:
        return globals()[rclass].from_result(fetched)


_error_base = namedtuple('error', ['message', 'reason', 'code'])


class Error(_error_base):
    @staticmethod
    def from_result(result):
        if result is None or result == []:
            return None
        return Error(
            message=result[1].get('message'),
            reason=result[1].get('reason'),
            code=result[0]
        )


_clans_badgeuls_base = namedtuple('badgeurl', ['large', 'medium', 'small'])


class Clans_badgeuls(_clans_badgeuls_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Clans_badgeuls(
            large=result.get('large'),
            medium=result.get('medium'),
            small=result.get('small')
        )


_search_clan_base = namedtuple('clan', ['items', 'paging'])


class Search_clan(_search_clan_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        results = result
        return Search_clan(
            items=[Search_clan_items.from_result(result) for result in results['items']],
            paging=Search_clan_paging.from_result(result.get('paging'))
        )


_search_clan_items_base = namedtuple('items', ['clanPoints', 'requiredTrophies', 'warFrequency', 'clanLevel', 'type',
                                               'name', 'tag', 'location', 'warWins', 'members', 'badgeUrls'])


class Search_clan_items(_search_clan_items_base):
    @staticmethod
    def from_result(result):
        if result is None or result is True:
            return None

        return Search_clan_items(
            clanPoints=result.get('clanPoints'),
            requiredTrophies=result.get('requiredTrophies'),
            warFrequency=result.get('warFrequency'),
            clanLevel=result.get('clanLevel'),
            type=result.get('type'),
            name=result.get('name'),
            tag=result.get('tag'),
            location=result.get('location'),
            warWins=result.get('warWins'),
            members=result.get('members'),
            badgeUrls=Clans_badgeuls.from_result(result.get('badgeUrls')),
        )


_search_clan_paging_base = namedtuple('paging', ['cursors'])


class Search_clan_paging(_search_clan_paging_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return Search_clan_paging(
            cursors=Search_clan_paging_cursors.from_result(result.get('cursors'))
        )


_search_clan_paging_cursor_base = namedtuple('cursors', ['after'])


class Search_clan_paging_cursors(_search_clan_paging_cursor_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Search_clan_paging_cursors(
            after=result.get('after')
        )


_clantag_base = namedtuple('clan',
                           ['warFrequency', 'requiredTrophies', 'memberList', 'clanPoints', 'name', 'location',
                            'warWins', 'members', 'clanLevel', 'badgeUrls', 'description', 'tag', 'type'])


class Clantag(_clantag_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Clantag(
            warFrequency=result.get('warFrequency'),
            requiredTrophies=result.get('requiredTrophies'),
            memberList=result.get('memberList'),
            clanPoints=result.get('clanPoints'),
            name=result.get('name'),
            location=result.get('location'),
            warWins=result.get('warWins'),
            members=result.get('members'),
            clanLevel=result.get('clanLevel'),
            badgeUrls=result.get('badgeUrls'),
            description=result.get('description'),
            tag=result.get('tag'),
            type=result.get('type'),
        )


_clan_members_base = namedtuple('clan', ['items'])


class Clan_members(_clan_members_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        results = result
        return Clan_members(
            items=[Clan_members_items.from_result(result) for result in results['items']],
        )


_clan_members_items_base = namedtuple('items', ['donations', 'previousClanRank', 'name', 'role', 'league',
                                                'expLevel', 'donationsReceived', 'clanRank', 'trophies'])


class Clan_members_items(_clan_members_items_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Clan_members_items(
            donations=result.get('donations'),
            previousClanRank=result.get('previousClanRank'),
            name=result.get('name'),
            role=result.get('role'),
            league=result.get('league'),
            expLevel=result.get('expLevel'),
            donationsReceived=result.get('donationsReceived'),
            clanRank=result.get('clanRank'),
            trophies=result.get('trophies'),
        )


_locations_base = namedtuple('location', ['items'])


class Locations(_locations_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        results = result
        return Locations(
            items=[Locations_items.from_result(result) for result in results['items']],
        )


_location_items_base = namedtuple('items', ['name', 'id', 'isCountry', 'countryCode'])


class Locations_items(_location_items_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Locations_items(
            name=result.get('name'),
            id=result.get('id'),
            isCountry=result.get('isCountry'),
            countryCode=result.get('countryCode'),
        )


_location_ranking_base = namedtuple('location', ['items'])


class Location_ranking(_location_ranking_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        results = result
        try:
            items = [Location_ranking_players.from_result(result) for result in results['items']]
        except TypeError:
            print(results['items'][0])
            items = [Location_ranking_clans.from_result(result) for result in results['items']]
        return Location_ranking(
            items=items
        )


_location_ranking_clan_base = namedtuple('clan', ['rank', 'badgeUrls', 'name', 'tag', 'members',
                                                  'previousRank', 'clanLevel', 'location', 'clanPoints'])


class Location_ranking_clans(_location_ranking_clan_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Location_ranking_clans(
            rank=result.get('rank'),
            badgeUrls=Clans_badgeuls.from_result(result.get('badgeUrls')),
            name=result.get('name'),
            tag=result.get('tag'),
            members=result.get('members'),
            previousRank=result.get('previousRank'),
            clanLevel=result.get('clanLevel'),
            location=result.get('location'),
            clanPoints=result.get('clanPoints')
        )


_location_ranking_player_base = namedtuple('player', ['trophies', 'rank', 'clan', 'name', 'defenseWins',
                                                      'previousRank', 'expLevel', 'league', 'attackWins'])


class Location_ranking_players(_location_ranking_player_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Location_ranking_players(
            trophies=result.get('trophies'),
            rank=result.get('rank'),
            clan=result.get('clan'),
            name=result.get('name'),
            defenseWins=result.get('defenseWins'),
            previousRank=result.get('previousRank'),
            expLevel=result.get('expLevel'),
            league=result.get('league'),
            attackWins=result.get('attackWins'),
        )


_leagues_base = namedtuple('leagues', ['items'])


class Leagues(_leagues_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        results = result
        return Leagues(
            items=[Leagues_items.from_result(result) for result in results['items']],
        )


_leagues_items_base = namedtuple('items', ['iconUrls', 'id', 'name'])


class Leagues_items(_leagues_items_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Leagues_items(
            iconUrls=Leagues_iconurl.from_result(result.get('iconUrls')),
            id=result.get('id'),
            name=result.get('name'),
        )


_leagues_iconurl_base = namedtuple('iconurl', ['large', 'medium', 'small'])


class Leagues_iconurl(_leagues_iconurl_base):
    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Leagues_iconurl(
            large=result.get('large'),
            medium=result.get('medium'),
            small=result.get('small'),
        )


# class result()
#######################clans#######################


def _search_clan(name=None, warfrequency=None, locationid=None, minmembers=None, maxmembers=None,
                 minclanpoints=None, minclanlevel=None, limit=10, after=None, before=None, **kwargs):
    """
    Search all clans by name and/or filtering the results using various criteria.
    At least one filtering criteria must be defined and if name is used as part
    of search, it is required to be at least three characters long.
    For the time being, there is no pagination of the results and the amount of
    clans returned as part of search has a fixed maximum amount. Also, it is not
    possible to specify ordering for results so clients should not rely on any
    specific ordering as that may change in the future releases of the API.

    :param name:Search clans by name. If name is used as part of search query,it needs to be
    at least three characters long.Name search parameter is interpreted as wild card search,
    so it may appear anywhere in the clan name.
    :param warfrequency:Filter by clan war frequency
    :param locationid:Filter by clan location identifier. For list of available locations,
    refer to getLocations operation.
    :param minmembers:Filter by minimum amount of clan members.
    :param maxmembers:Filter by maximum amount of clan members.
    :param minclanpoints:Filter by minimum amount of clan points.
    :param minclanlevel:Filter by minimum clan level.
    :param limit:Limit the number of items returned in the response.
    :param after:Return only items that occur after this marker. After marker can be found from
    clan search response, inside the 'paging' property. Note that only after or before can be
    specified for a request, not both.
    :param before:Return only items that occur before this marker. Before marker can be found from
    clan search response, inside the 'paging' property. Note that only after or before can be
    specified for a request, not both.

    :type name:string
    :type warfrequency:string
    :type minmembers:integer
    :type maxmembers:integer
    :type minclanpoints:integer
    :type minclanlevel:integer
    :type limit:integer
    :type after:integer
    :type before:integer
    :return:
    ..note::
            you don't have to call this function directly.you can call the related function in cocapi.
    """
    params = dict(name=name,
                  warfrequency=warfrequency,
                  minmembers=minmembers,
                  maxmembers=maxmembers,
                  minclanpoints=minclanpoints,
                  minclanlevel=minclanlevel,
                  limit=limit,
                  after=after,
                  before=before)
    return get_results('Search_clan', fetch('clans', params=params))


def _get_clan(clantag):
    """
    Get information about a single clan by clan tag. Clan tags can be found using clan search operation.
    Note that clan tags start with hash character '#'.

    :param clantag:Tag of the clan to retrieve.
    :type clantag:string
    :return:
    """
    return get_results('Clantag', fetch('clans/{clantag}'.format(clantag=quote(clantag))))


def _get_clan_members(clantag):
    """
    List clan members

    :param clantag:Tag of the clan to retrieve.
    :type clantag:string
    :return:
    """
    return get_results('Clan_members', fetch('clans/{clantag}/members'.format(clantag=quote(clantag))))


#######################locations#######################

def _get_locations():
    """
    List all available locations
    :return:
    """
    return get_results('Locations', fetch('locations'))


def _get_locationid(locationid):
    """
    Get information about specific location
    :param locationid:Identifier of the location to retrieve.
    :type locationid:string
    :return:
    """
    return get_results('Locations_items', fetch('locations/{locationid}'.format(locationid=locationid)))


def _get_location_ranking(locationid, rankingid):
    """
    Get rankings for a specific location
    :param locationid:Identifier of the location to retrieve.
    :param rankingid:Identifier of the ranking list to retrieve.
    :type locationid:string
    :type rankingid:string
    :return:
    """
    return get_results('Location_ranking',
                       fetch('locations/{locationid}/rankings/{rankingid}'.format(locationid=locationid,
                                                                                  rankingid=rankingid)))


#######################leagues#######################
def _get_leagues():
    """
    Get list of leagues
    :return:
    """
    return get_results('Leagues', fetch('leagues'))


#######################classes#######################
class cocapi:
    def __init__(self, token):
        global headers
        self.token = token
        self.headers = {'authorization': 'Bearer %s' % self.token, 'Accept': 'application/json'}
        headers = self.headers
        self.request_args = dict(token=self.token)

    def _merge_overrides(self, **kwargs):
        ra = self.request_args.copy()
        ra.update(kwargs)
        return ra

    def search_clan(self, *args, **kwargs):
        return _search_clan(*args, **kwargs)

    def get_clantag(self, *args, **kwargs):
        return _get_clan(*args, **kwargs)

    def get_clan_members(self, *args, **kwargs):
        return _get_clan_members(*args, **kwargs)

    def get_locations(self, *args, **kwargs):
        return _get_locations(*args, **kwargs)

    def get_locationid(self, *args, **kwargs):
        return _get_locationid(*args, **kwargs)

    def get_location_ranking(self, *args, **kwargs):
        return _get_location_ranking(*args, **kwargs)

    def get_leagues(self, *args, **kwargs):
        return _get_leagues(*args, **kwargs)
