## netstat

> `/usr/sbin/netstat`

```diff

-705.100.5.0.0
-  __TEXT.__text: 0x1633c
+725.0.0.0.0
+  __TEXT.__text: 0x170e8
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0xa93d
-  __TEXT.__unwind_info: 0x158
+  __TEXT.__cstring: 0xadfd
+  __TEXT.__unwind_info: 0x150
   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
-  __DATA.__data: 0x85c
-  __DATA.__bss: 0xac08
+  __DATA.__data: 0x884
+  __DATA.__bss: 0xab68
   __DATA.__common: 0x728
   - /usr/lib/libSystem.B.dylib
-  UUID: 69F7EC91-E123-3BF6-83A6-BE1B75F9DF1C
+  UUID: 8104F819-38D8-3E8A-8E3D-40356F3C2301
   Functions: 88
-  Symbols:   292
-  CStrings:  1749
+  Symbols:   291
+  CStrings:  1776
 
Symbols:
- _njcl
Functions:
~ _intpr : 7724 -> 7728
~ _aqstatpr : 1768 -> 1808
~ _tcp_stats : 9320 -> 10300
~ _mptcp_stats : 1516 -> 2984
~ _udp_stats : 1704 -> 1740
~ _ip_stats : 2844 -> 2972
~ _igmp_stats : 1316 -> 1320
~ _ip6_stats : 5436 -> 5640
~ _ip6_ifstats : 1524 -> 1564
~ _icmp6_stats : 1932 -> 1948
~ _icmp6_ifstats : 1920 -> 1996
~ _ipsec_stats : 1596 -> 1604
~ _pfkey_stats : 1764 -> 1788
~ _vsockpr : 932 -> 984
~ _vsockstats : 136 -> 240
~ _mbpr : 3432 -> 3252
~ _print_nstat_stats : 1184 -> 1188
~ _print_net_api_stats : 3024 -> 3156
~ _print_if_ports_used_stats : 2412 -> 2736
~ _print_if_link_heuristics_stats : 1440 -> 1476
CStrings:
+ "\t\t%u time%s CE received in ACE field\n"
+ "\t\t%u time%s received AccECN SYN packet with CE\n"
+ "\t\t%u time%s received AccECN SYN packet with ECT0\n"
+ "\t\t%u time%s received AccECN SYN packet with ECT1\n"
+ "\t\t%u time%s received AccECN SYN packet with Not-ECT\n"
+ "\t%llu LPW connection idle wake%s\n"
+ "\t%llu LPW not idle connection wake%s\n"
+ "\t%llu LPW to full wake transition%s\n"
+ "\t%llu byte%s sent in aggregate\n"
+ "\t%llu byte%s sent in handover\n"
+ "\t%llu byte%s sent on cellular in aggregate mode\n"
+ "\t%llu byte%s sent on cellular in handover mode\n"
+ "\t%llu byte%s sent on cellular in handover-mode\n"
+ "\t%llu connection idle wake%s\n"
+ "\t%u MPTCP attempt%s using aggregate mode\n"
+ "\t%u MPTCP attempt%s using handover mode\n"
+ "\t%u MPTCP duplicate-only packet%s received\n"
+ "\t%u MPTCP packet%s dropped for lack of memory\n"
+ "\t%u MPTCP packet%s with data after window\n"
+ "\t%u SYN cookie%s received\n"
+ "\t%u SYN cookie%s sent\n"
+ "\t%u aggregate mode connection%s that negotiated MPTCP\n"
+ "\t%u connection%s that moved traffic away from cellular when starting on cellular\n"
+ "\t%u new subflow%s that fell back to regular TCP on Wi-Fi\n"
+ "\t%u new subflow%s that fell back to regular TCP on cellular\n"
+ "\t%u number of join ack retransmits%s\n"
+ "\t%u open %s socket%s\n"
+ "\t%u successful extraction of entr%s\n"
+ "\t%u successfull handover mode connection%s that started on Wi-Fi\n"
+ "\t%u successfull handover mode connection%s that started on cellular\n"
+ "\t%u syncache entr%s aborted\n"
+ "\t%u time%s an MPTCP connection triggered cellular\n"
+ "\t%u time%s could not reply to packet\n"
+ "     [ congestion feedback: %llu\t congestion drops: %llu ]\n"
+ "%-6.6s %-6.6s %-6.6s %-6.6s %-18.18s %-18.18s %-11.11s"
+ "%-6.6s %-6.6s %6u %6u %-18s %-18s %-11s"
+ "NEW FQ_CODEL"
+ "net.%s.pcbcount"
+ "net.%s.pcblist"
+ "vsock_private"
+ "vsockp"
- "\t\t%u connection%s fell back due to RST after SYN\n"
- "\t\t%u retransmission%s not needed \n"
- "\t\t%u time%s DSACK was disabled on a connection\n"
- "\t%u connection%s had stretch ack algorithm disabled\n"
- "\t%u open vsock socket%s\n"
- "\t%u subflow switch%s due to advisory\n"
- "\t%u subflow switch%s due to peer\n"
- "%-5.5s %-6.6s %-6.6s %-6.6s %-18.18s %-18.18s %-11.11s"
- "%-5.5s %-6.6s %6u %6u %-18s %-18s %-11s"
- "kern.ipc.njcl"
- "net.vsock.pcbcount"
- "net.vsock.pcblist"
- "sysctl: net.vsock.pcbcount"
- "vsock:"

```
