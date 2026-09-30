## netstat

> `/usr/sbin/netstat`

```diff

-741.0.0.0.0
-  __TEXT.__text: 0x17770
+741.100.2.0.0
+  __TEXT.__text: 0x17a54
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__cstring: 0xb100
+  __TEXT.__cstring: 0xb1d4
   __TEXT.__const: 0x398
-  __TEXT.__unwind_info: 0x190
+  __TEXT.__unwind_info: 0x198
   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
-  __DATA.__data: 0xa0c
-  __DATA.__bss: 0xabb8
+  __DATA.__data: 0xa3c
+  __DATA.__bss: 0xabc8
   __DATA.__common: 0x6b0
   - /usr/lib/libSystem.B.dylib
-  UUID: BE654CE0-5065-37DA-973C-B674B46CAE4A
-  Functions: 98
-  Symbols:   270
-  CStrings:  1804
+  UUID: 61A37FEA-4AF7-39C2-8EF3-9090C6AE28F4
+  Functions: 99
+  Symbols:   271
+  CStrings:  1812
 
Symbols:
+ _print_if_lpw_stats
Functions:
~ _print_if_ports_used_stats : 3292 -> 3432
+ _print_if_lpw_stats
CStrings:
+ "\t%llu magic packet%s checked\n"
+ "\t%llu magic packet%s found\n"
+ "\t%llu packet%s received in LPW mode\n"
+ "\t%llu packet%s sent in LPW mode\n"
+ "\t%llu packet%s transmitted in LPW mode\n"
+ "LPW stats on %s\n"
+ "lpw"
+ "sysctl IFDATA_LPWSTATS"

```
