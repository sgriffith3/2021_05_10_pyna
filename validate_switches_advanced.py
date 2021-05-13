from napalm import get_network_driver
import pprint as pp
import yaml


def run_compliance(net_os, net_host, uname, passw, comp_file):
    driver = get_network_driver(net_os)
    device = driver(net_host, uname, passw)
    device.open()
    compliant = device.compliance_report(comp_file)
    pp.pprint(compliant)
    device.close()
    return compliant


if __name__ == "__main__":
    #run_compliance('eos', 'sw-1', 'admin', 'alta3', '/home/student/pyna/sw1_validate.yml')
    #with open("switches.csv") as f:
    #    txt = f.readlines()
    #    for line in txt:
    #        switch_data = line.split(',')
    #        print(switch_data)
    #        run_compliance(switch_data[3], switch_data[0], switch_data[1], switch_data[2], switch_data[4].strip())
    failed = []
    with open("switches.yml") as yf:
        myaml = yaml.load(yf, Loader=yaml.SafeLoader)
        print(myaml)
        print(type(myaml))
        for sw in myaml:
            for compf in sw['comp_files']:
                print(f"Running validation test {compf} against {sw['name']}")
                passfail = run_compliance(sw['os'], sw['name'], sw['user'], sw['passw'], compf)
                if not passfail['complies']:
                    failed.append(passfail)
    print(failed)
                    
