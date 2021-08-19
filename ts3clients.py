#!/usr/bin/env python3

import os
import sys

import ts3

def print_config():
    """Print plugin configuration"""
    print("graph_title TeamSpeak clients online")
    print("graph_vlabel number of clients")
    print("graph_category teamspeak")
    print("graph_info Number of TeamSpeak clients online")
    print("graph_printf %3.0lf")
    print("graph_args --base 1000 --lower-limit 0")
    print("graph_scale no")
    print("clients.label clients")

def fetch_clients():
    """Fetch and print number of clients online"""
    query_host = os.getenv("query_host", "127.0.0.1")
    query_ssh_port = os.getenv("query_ssh_port", 10022)
    query_user = os.getenv("query_user")
    query_password = os.getenv("query_password")

    if not query_user or not query_password:
        print("Environment variables 'query_user' and 'query_password' are required")
        sys.exit(1)

    uri = f"ssh://{query_user}:{query_password}@{query_host}:{query_ssh_port}"
    with ts3.query.TS3ServerConnection(uri) as ts3conn:
        ts3conn.exec_("use", sid=1)
        serverinfo = ts3conn.exec_("serverinfo")
        clients = int(serverinfo[0]["virtualserver_clientsonline"])
        queryclients = int(serverinfo[0]["virtualserver_queryclientsonline"])

        print(f"clients.value {clients - queryclients}")

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "config":
            print_config()
        elif sys.argv[1] == "autoconf":
            print("no")
        else:
            print(f"Unknown argument '{sys.argv[1]}'")
            sys.exit(1)
    else:
        fetch_clients()

if __name__ == "__main__":
    main()
