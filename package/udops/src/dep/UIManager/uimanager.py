from udops.src.dep.UIManager.RepoManager.repo import repomanager
from udops.src.dep.config.Connection import *
from udops.src.dep.InputProperties import *
prop = properties()
connection = Connection()
conn = connection.get_connection()


class uimanager:

    def create_corpus(self, json_loader, target, location):
        try:
            repo = repomanager()
            in_it = repo.init(location)
            if in_it == 1:
                url_get = repo.get_url(target, location)
                if url_get == 1:
                    corpus_create = repo.create_corpus(json_loader, conn)
                    if corpus_create == 1:
                        return 1
                    elif corpus_create == 2:
                        return 2
                    else:
                        return corpus_create
                else:
                    return url_get
            else:
                return in_it
        except Exception as e:
            return e

    def add(self, target,location):
        try:
            repo = repomanager()
            return repo.add_(target,location)
        except Exception as e:
            return e

    def remote(self,name,data,gita,location):
        try:
            repo = repomanager()
            return repo.remote(name,data,gita, location)
        except Exception as e:
            return e

    def commit(self,message,location):
        try:
            repo = repomanager()
            return repo.commit(message,location)
        except Exception as e:
            return e

    def push(self,location):
        try:
            repo = repomanager()
            return repo.push(location)
        except Exception as e:
            return e

    def clone(self,corpus_name,arg,location):
        try:
            repo = repomanager()
            return repo.clone(corpus_name,arg,location,conn)
        except Exception as e:
            return e

    def pull(self,file,location):
        try:
            repo = repomanager()
            repo.pull(file,location)
            return 1
        except Exception as e:
            return e

    

