#Challenge -

#1. Using python, CREATE a sqlite table to store the switch configuration in. Create (at least) the following columns:
#			- hostname
#			- ip
#			- startup_config
#			- running_config
#			- valid_config
			

import sqlite3
from napalm import get_network_driver

def first_run():
    conn = sqlite3.connect("fancy_switches.db")
    try: 
        conn.execute("CREATE TABLE switches (hostname CHAR, ip CHAR, startup_config CHAR, running_config CHAR, valid_config BOOL)")
        
        #2. Using python, INSERT known information into the sqlite table (hostname and ip)
        conn.execute("INSERT INTO switches (hostname,ip) VALUES ('sw-1','10.7.76.189')")
        conn.execute("INSERT INTO switches (hostname,ip) VALUES ('sw-2','10.5.17.14')")
        conn.commit()
    except sqlite3.OperationalError as err:
        print(err)
    finally:
        conn.close()

#3. Using your previous python scripts, retrieve the startup_config and running_config for each switch and update the database (columns startup_config and running_config) with this information.
def retrv_conf(sw):
    driver = get_network_driver('eos')
    device = driver(sw, 'admin', 'alta3')
    device.open()
    sw_conf = device.get_config()
    return sw_conf


def update_sw_conf(sw):
    conn = sqlite3.connect("fancy_switches.db")
    sw_conf = retrv_conf(sw)
    run_conf = sw_conf['running']
    start_conf = sw_conf['startup']
    conn.execute(f"UPDATE switches SET running_config = '{run_conf}' where hostname = '{sw}'")
    conn.execute(f"UPDATE switches SET startup_config = '{start_conf}' where hostname = '{sw}'")
    valid = comply(sw)
    conn.execute(f"UPDATE switches SET valid_config = '{valid}' where hostname = '{sw}'")
    conn.commit()


#4. Using your previous python scripts, run the configuration validation check for each switch and update the database (column valid_config [True|False]) with this information.

def comply(sw):
    driver = get_network_driver('eos')
    device = driver(sw, 'admin', 'alta3')
    device.open()
    complies = device.compliance_report(f"/home/student/pyna/{sw}_validate.yml")
    device.close()
    if complies['complies']:
        compliant = True
    else:
        compliant = False
    return compliant


update_sw_conf('sw-2')
