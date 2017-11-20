#-*- coding: utf-8 -*-
import psycopg2
import time
import sys
sys.path.append(r"C:\Work\XenTools\VM_Require_Tools\VM_Info_Sync")
import VM_Info_Sync
sys.dont_write_bytecode = True


class DBTool:

    def __init__(self):
        db = VM_Info_Sync.DBTools()
        Test_Case_ID=db.Get_MAC_Address()
        self.testCase_ID = Test_Case_ID

        PostgresSQL_IP = "192.168.3.47"
        DBName = "mdx_xen_case_db"
        user = "postgres"
        password = "moldex3d!"
        conn_string = "host={} dbname={} user={} password={}".format(
            PostgresSQL_IP, DBName, user, password)
        connection = psycopg2.connect(conn_string)
        self.cursor = connection.cursor()

    def Get_GroupID(self):
        sqlf = """SELECT "ixTestGroup_id"
                  FROM "Xen_VM_Instance_App_vm_ins_for_test"
                  WHERE "id" = '{}'
               """
        sql = sqlf.format(self.testCase_ID)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print rows
        self.GroupID = rows[0][0]

    def Wait_All_TestCase_Complete(self):
        sqlf = """SELECT "sStatus"
                  FROM "Xen_VM_Instance_App_vm_ins_for_test"
                  WHERE "ixTestGroup_id" = '{}'
                  AND "id" <> '{}'
               """
        sql = sqlf.format(self.GroupID, self.testCase_ID)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for i in range(len(rows)):
            isComplete = "Complete/Shutdown" not in rows[i][0] and "Test_Complete" not in rows[i][0]
            if isComplete:
                return False
        return True


if __name__ == "__main__":
    db=DBTool()
    db.Get_GroupID()
    while not db.Wait_All_TestCase_Complete():
        time.sleep(10)
    print "Done!"