import unittest
import sqlite3 as sql

class testing_cricketPlayerDb(unittest.TestCase):
    def setUp(self):
        self.Name1="vk"
       # self.Name2="pant"
        self.Number="18"
        self.connection=sql.connect("Cricketer.db")

    def tearDown(self):
        self.Name=" "
        self.Number=" "
        self.connection.close()

    def test_verify_player_name(self):
        result=self.connection.execute("select Player_Name from Player where Player_Num="+self.Number)
        for i in result:
            fetchedplayerName=i[0]

        self.assertEqual(self.Name,fetchedplayerName)

  #  def test_verify_player_name_2(self):
   #     result=self.connection.execute("select Player_Name from Player where Player_Num="+self.Number)
    #    for i in result:
     #       fetchedplayername=i[0]
      #  self.assertEqual(self.Name1,fetchedplayername)

if __name__=="__main__":
    unittest.main()