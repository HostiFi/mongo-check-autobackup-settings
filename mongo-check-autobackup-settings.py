import pymongo

needs_to_be_fixed = 0

client = pymongo.MongoClient("mongodb://127.0.0.1:27117/ace")
mdb = client.ace
super_mgmt_settings = mdb.setting.find_one({'key':'super_mgmt'})

if super_mgmt_settings['autobackup_max_files'] != 14:
    needs_to_be_fixed = 1

if super_mgmt_settings['autobackup_cron_expr'] != '0 2 * * *':
    needs_to_be_fixed = 1

if super_mgmt_settings['autobackup_timezone'] != 'America/New_York':
    needs_to_be_fixed = 1

if super_mgmt_settings['autobackup_days'] != 0:
    needs_to_be_fixed = 1

if super_mgmt_settings['autobackup_enabled'] != True:
    needs_to_be_fixed = 1

print needs_to_be_fixed
