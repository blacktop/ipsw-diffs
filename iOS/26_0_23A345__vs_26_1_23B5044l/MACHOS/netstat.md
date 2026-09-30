## netstat

> `/usr/sbin/netstat`

```diff

-726.0.0.0.0
-  __TEXT.__text: 0x173bc
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__cstring: 0xaf2b
+728.0.0.0.0
+  __TEXT.__text: 0x175ec
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__cstring: 0xaece
   __TEXT.__const: 0xd8
-  __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__auth_got: 0x250
+  __TEXT.__unwind_info: 0x168
+  __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
   __DATA.__data: 0x884
-  __DATA.__bss: 0xab90
-  __DATA.__common: 0x728
+  __DATA.__bss: 0xab88
+  __DATA.__common: 0x730
   - /usr/lib/libSystem.B.dylib
-  UUID: A09FE526-9F3E-3360-A33B-AA8F3FD402B5
-  Functions: 89
-  Symbols:   292
-  CStrings:  1785
+  UUID: E8D315CC-ADAD-30D1-ACBD-CE79E611EAD9
+  Functions: 91
+  Symbols:   294
+  CStrings:  1784
 
Symbols:
+ _print_intpr_header
+ _printprotoifstats
+ _rem_nstat_src
+ _strncpy
- print_if_link_heuristics_stats.cold.1
- rxpollstatpr.cold.1
Functions:
~ _intpr : 7728 -> 7156
+ _print_intpr_header
~ _aqstatpr : 1808 -> 1900
~ _rxpollstatpr : 996 -> 1224
~ _print_link_status : 3544 -> 3372
+ _rem_nstat_src
~ _ip6_ifstats : 1564 -> 1588
~ _icmp6_ifstats : 1996 -> 2020
~ _main : 2252 -> 2136
~ _printproto : 368 -> 288
+ _printprotoifstats
~ _print_if_link_heuristics_stats : 1476 -> 1528
CStrings:
+ "NONE"
+ "create_control_socket"
+ "getifaddrs"
+ "ioctl(SIOCGIFEFLAGS"
- "%s statistics option requires interface name\n"
- "%s: no per-interface stats routine\n"
- "Polling"
- "Queue"
- "additional link status option requires interface name\n"

```
