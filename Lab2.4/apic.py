import requests, json, pprint
from flask import Flask
from flask import render_template, jsonify


# controller = "devnetapi.cisco.com/sandbox/apic_em"
controller = "sandboxapicem.cisco.com"

def ticket():
    url = 'https://' + controller + '/api/v1/ticket'
    payload = {"username": "devnetuser",
               "password": "Cisco123!"
              }
    header = {"content-type": "application/json"}

    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return response.json()['response']['serviceTicket']


def hosts(ticket):
    url = "https://" + controller + "/api/v1/host"

    header = {"content-type": "application/json",
              "X-Auth-Token":ticket
             }

    response = requests.get(url, headers=header, verify=False)
    return response.json()


def devices(ticket):
    url = "https://" + controller + "/api/v1/network-device"

    header = {"content-type": "application/json",
              "X-Auth-Token": ticket
              }

    response = requests.get(url, headers=header, verify=False)
    return response.json()

def topolog(ticket):
    url = "https://" + controller + "/api/v1/topology/physical-topology"

    header = {"content-type": "application/json",
              "X-Auth-Token": ticket
              }

    response = requests.get(url, headers=header, verify=False)
    return response.json()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("topology.html")

@app.route("/api/topology")
def topology():
    ticket = ticket()
    return jsonify(topolog(ticket)['response'])

if __name__ == '__main__':

    ticket = ticket()

    print("Hosts = ")
    pprint.pprint(hosts(ticket))
    print("Devices = ")
    pprint.pprint(devices(ticket))
    print("Topology = ")
    pprint.pprint(topolog(ticket))

    app.run(debug=True)

