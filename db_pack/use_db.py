__author__ = "Manouchehr Rasouli"
__date__ = "2/Aug/2017, 3/Aug/2017, 5/Aug/2017"

import json


class use_exception_db:
    def __init__(self, connection):
        self.db = connection.check_point_database
        self.collection = self.db.exception_collection

    def insert_error(self, error):
        Error = {"Error" : str(error)}
        self.collection.insert(Error)
        return None

    def delete_all_exceptions(self):
        self.collection.remove({})
        return None

    def get_all_exceptions_as_list(self):
        exception_list = []
        cursor = self.collection.find({})
        for dock in cursor:
            exception_list.append(dock["Error"])
        return exception_list


class use_url_db:
    def __init__(self, connection):
        self.db = connection.check_point_database
        self.collection = self.db.url_collection

    def insert_url(self, urls):
        url = []
        url_dic = json.loads(urls)
        urls_value = url_dic.values()
        url_list = self.get_urls_as_list()
        for item in urls_value:
            if item in url_list:
                print("the url " + str(item) + " exist !")
            else:
                url.append({"url" : str(item)})
        if len(url) > 0:
            self.collection.insert_many(url)
        else:
            print("Thers no any url !")
        return None

    def get_urls_as_list(self):
        url_list = []
        cursor = self.collection.find({})
        for dock in cursor:
            url_list.append(dock["url"])
        return url_list

    def delete_all_urls(self):
        #also we can return some result for this behavior of database
        self.collection.remove({})
        return None

    def delete_urls(self, urls):
        url_dic = json.loads(urls)
        urls_value = url_dic.values()
        for url in urls_value:
            self.collection.remove({"url" : url})
        return None


class use_result_db:
    def __init__(self,connection):
        self.db = connection.check_point_database
        self.collection = self.db.result_collection

    def inser_results_as_list(self, result_list):
        self.collection.insert_many(result_list)
        return None

    def get_results(self):
        result_list = []
        cursor = self.collection.find({})
        for dock in cursor:
            result_list.append(dock["Result"])
        return result_list

    def get_result_as_list_after(self, date):
        url_list = []
        cursor = self.collection.find({"Result.date" : {"$gt" : date}})
        for dock in cursor:
            url_list.append(dock["Result"])
        return url_list

    def get_results_for_url(self, url):
        result_list = []
        cursor = self.collection.find({"url" : url})
        for dock in cursor:
            result_list.append(dock["Result"])
        return result_list

    def delete_all_results(self):
        self.collection.remove({})
        return None

    def delete_results_for_url(self, url):
        self.collection.remove({"url" : url})
        return None
