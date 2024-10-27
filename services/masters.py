from core.db_utils import DbManager


MASTER_DATA ='masterdata'
class Masterservice:

    async def get_countries(self):
        countries = DbManager().db[MASTER_DATA].find().to_list()
        for country in countries:
            country.pop('_id')
            if not country:
                countries = 'others'
        return countries