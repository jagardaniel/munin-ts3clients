# munin-ts3clients

ts3clients - A Munin plugin to monitor the number of active clients on a TeamSpeak 3 server.

---

### Requirements

- Python >3.6
- ts3 python module (ts3>=2.0.0b2)
- TeamSpeak 3 server with SSH query support (>3.3.0)

### Configuration

Example configuration

`/etc/munin/plugin-conf.d/ts3clients`

```
[ts3clients]
env.query_host 127.0.0.1
env.query_ssh_port 10022
env.query_user serveradmin
env.query_password secretpassword
```

Copy the script (ts3clients.py) to `/usr/local/munin/lib/plugins/ts3clients` and create a symlink to it in the `/etc/munin/plugins` directory. Use the command `munin-run ts3clients` to make sure that the script works as it should and then restart munin-node to activate it.