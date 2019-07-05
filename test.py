import fdb

connect = fdb.connect(
    database=r"C:\Program Files\Firebird\Firebird_3_0\examples\empbuild\EMPLOYEE.FDB",
    user='sysdba',
    password='masterkey',
    fb_library_name=r"C:\Program Files\Firebird\Firebird_3_0\fbclient.dll",
)

# -----------------------------------------
# print(connect.db_info(fdb.isc_info_user_names))

# -----------------------------------------
cursor = connect.cursor()
SELECT = "SELECT * FROM employee"
cursor.execute(SELECT)

print([name[0] for name in cursor.description])
# print(cursor.fetchall())

# -----------------------------------------
# for name in cursor.itermap():
#     print(name)

# -----------------------------------------
# connect.begin()
# info = connect.trans_info([fdb.isc_info_tra_id, fdb.isc_info_tra_oldest_interesting,
#                        fdb.isc_info_tra_oldest_snapshot, fdb.isc_info_tra_oldest_active,
#                        fdb.isc_info_tra_isolation, fdb.isc_info_tra_access,
#                        fdb.isc_info_tra_lock_timeout])
# for inf in info:
#     print(info[inf])
