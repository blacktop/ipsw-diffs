## netstat

> `/usr/sbin/netstat`

```diff

-728.60.2.0.0
-  __TEXT.__text: 0x176ec
+730.80.3.0.0
+  __TEXT.__text: 0x16de0
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__cstring: 0xafbc
-  __TEXT.__const: 0xd8
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__cstring: 0xb015
+  __TEXT.__const: 0x388
+  __TEXT.__unwind_info: 0x180
   __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
-  __DATA.__data: 0x884
+  __DATA.__data: 0x9a4
   __DATA.__bss: 0xabb8
-  __DATA.__common: 0x730
+  __DATA.__common: 0x6b0
   - /usr/lib/libSystem.B.dylib
-  UUID: 5F328525-D3C5-3315-B3FD-FB1B8F5676D9
-  Functions: 91
-  Symbols:   294
-  CStrings:  1788
+  UUID: D0C73C18-7B9C-3306-8B45-7C126042DAFE
+  Functions: 93
+  Symbols:   264
+  CStrings:  1792
 
Symbols:
+ _getprogname
+ _mptcp_reinit
+ _name2protox
+ _netstat_params_initializer
+ _netstat_parse_parameters
+ _netstat_print_banner
+ _netstat_run
+ _optopt
+ _reinitalize_protocols
+ _tcp_reinit
+ _udp_reinit
+ _usage
- _Aflag
- _Bflag
- _Fflag
- _Lflag
- _Qflag
- _Rflag
- _Sflag
- _Wflag
- _af
- _aflag
- _bflag
- _cflag
- _cq
- _dflag
- _errx
- _gflag
- _iflag
- _interface
- _interval
- _lflag
- _mflag
- _nflag
- _pflag
- _prioflag
- _qflag
- _rflag
- _sflag
- _tflag
- _unit
- _vflag
- _xflag
- _zflag
- bpf_stats.cold.1
- bpf_stats.cold.2
- bpf_stats.cold.3
- ifmalist_dump.cold.1
- intpr.cold.12
- routepr.cold.1
- routepr.cold.2
- routepr.cold.3
- tcp_ifstats.cold.1
- udp_ifstats.cold.1
CStrings:
+ "\t%llu duplicate IMCP packet%s for port unreachable suppressed\n"
+ "#\n# %s %s\n#\n"
+ "# option -I requires an interface name"
+ "-%c "
+ "AaBbc:dFf:gI:ikLlmnP:p:qQrRsStuvWw:xz%:"
+ "interface name is not valid: %s"
+ "unexpected: '%c' (optind: %d)\n"
- "\t%llu duplicate ICMP packet%s for port unreachable suppressed\n"
- "AaBbc:dFf:gI:ikLlmnP:p:qQrRsStuvWw:xz"
- "interface name is not valid: %s\n"

```
