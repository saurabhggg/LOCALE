# LOCALE
Here is CRUD API database .
There are four end points.
First one is add(http://127.0.0.1:5000/add   METHOD='POST'). Enter the json data and the data will be stored in the database.Id and user_id should not be empty as it will be used to search the data.
Second one is datas(http://127.0.0.1:5000/datas   METHOD='GET'). This can be used to view your table.
Third one is update(http://127.0.0.1:5000/update   METHOD='POST'). This is used to update the existing data. If data is not there then it will notify you that "DATA TO BE UPDATED DOES NOT EXISTS"
Or if the data exists then it will notify you that "DATA IS UPDATED".
Fourth one is delete(http://127.0.0.1:5000/delete/<ids>   METHOD='GET'). This is used to delete the existing data. If data is not there then it will notify you that "DATA DOES NOT EXISTS". Else the data will be deleted and it will notify you that "DATA IS DELETED".
