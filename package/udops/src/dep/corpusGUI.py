# commit
from udops.src.dep.UIHandler.uiauthentication import authentication
from udops.src.dep.UIHandler.uihandler import uihandler
import re

try:

    def loc(team):
        auth = authentication()
        team = auth.get_user_team(team)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@22")
        print(f"team---->{team}")
        return team[1]

    class GUI:

        def create_corpus(self, data):
            try:
                auth = authentication()
                user_id = auth.authenticate_user(data['username'])
                print(f"user_is --> {user_id}")
                if user_id == 0:
                    return 0
                else:
                    team = auth.get_user_team(data['teamname'])
                    team_id = team[0]
                    location = team[1]

                    if team_id == 0:
                        return 3
                    else:
                        corpus_details = {
                            "corpus_name": data['corpus_name'],
                            "corpus_type": data['corpus_type'],
                            "language": data['language'],
                            "source_type": data['source_type'],
                            "vendor": data['vendor'],
                            "domain": data['domain'],
                            "description": data['description'],
                            "lang_code": data['lang_code'],
                            "acquisition_date": data['acquisition_date'],
                            "migration_date": data['migration_date'],
                            "flag":data['flag']
                        }
                        uih = uihandler()
                        create_corpus = uih.init(corpus_details, data['source'],location)
                        if create_corpus == 1:
                            corpus_id = auth.corpus_id(data['corpus_name'])
                            auth.default_acess(corpus_id, user_id)
                            auth.Corpus_team_map(team_id, corpus_id)
                            return 1
                        elif create_corpus == 2:
                            return 2
                        else:
                            return create_corpus

            except Exception as e:
                return e

        def add(self, data):
            uih = uihandler()
            location = loc(data["teamname"])
            return uih.add(data["target"],location)

        def remote(self,teamname:str, name: str, data: str, gita: str):
            uih = uihandler()
            if re.sub(r'^.*/(.*?)(\.git)?$', r'\1', gita) == name:
                location = loc(teamname)
                return uih.remote(name, data, gita, location)

        def commit(self, teamname,message: str):
            uih = uihandler()
            location = loc(teamname)
            return uih.commit(message,location)

        def push(self, data):
            try:
                uih = uihandler()
                auth = authentication()
                user_id = auth.authenticate_user(data['username'])
                print(f"user_id---> {user_id}")
                if user_id == 0:
                    return 0
                else:
                    corpus_id = auth.corpus_id(data['corpus_name'])
                    print(f"corpus_id -->{corpus_id}")
                    access_type = "write"
                    access = auth.authorize_user(user_id, corpus_id, access_type)
                    location = loc(data['teamname'])

                    if access == 0:
                        return 2
                    else:
                        if uih.push(location) == 1:
                            return 1
                        else:
                            return uih.push(location)

            except Exception as e:
                return e

        def clone(self, data):
            try:
                uih = uihandler()
                auth = authentication()
                user_id = auth.authenticate_user(data['username'])
                if user_id == 0:
                    return 0
                else:
                    corpus_id = auth.corpus_id(data['corpus_name'])
                    print(f"corpus_id-->{corpus_id}")
                    access = auth.authorize_user_clone(user_id, corpus_id)
                    location = loc(data["teamname"])
                    print(f"location-->{location}")
                    if access == 0:
                        return 2
                    else:
                        if uih.clone(data['corpus_name'],data['gita'],location) == 1:
                            return 1
                        else:
                            return uih.clone(data['corpus_name'],data['gita'],location)
            except Exception as a:
                return a

        def pull(self, data):
            try:
                uih = uihandler()
                auth = authentication()
                user_id = auth.authenticate_user(data['username'])
                if user_id == 0:
                    return 0
                else:
                    corpus_id = auth.corpus_id(data['corpus_name'])
                    location = loc(data["teamname"])
                    if auth.authorize_user_clone(user_id, corpus_id) == 1:
                        return uih.pull(data['folder'],location)
                    else:
                        return uih.pull(data['folder'],location)
            except Exception as e:
                return e

except Exception as e:
    raise e

