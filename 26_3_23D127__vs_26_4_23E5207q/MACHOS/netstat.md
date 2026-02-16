## netstat

> `/usr/sbin/netstat`

```diff

-730.80.3.0.0
-  __TEXT.__text: 0x16de0
+741.0.0.0.0
+  __TEXT.__text: 0x17770
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__cstring: 0xb015
-  __TEXT.__const: 0x388
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__cstring: 0xb100
+  __TEXT.__const: 0x398
+  __TEXT.__unwind_info: 0x190
   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
-  __DATA.__data: 0x9a4
+  __DATA.__data: 0xa0c
   __DATA.__bss: 0xabb8
   __DATA.__common: 0x6b0
   - /usr/lib/libSystem.B.dylib
-  UUID: D02CDBFD-C39E-37E8-A4AA-4CA6F28C4B5C
-  Functions: 93
-  Symbols:   264
-  CStrings:  1792
+  UUID: BE654CE0-5065-37DA-973C-B674B46CAE4A
+  Functions: 98
+  Symbols:   270
+  CStrings:  1804
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _in6_addr_print
+ _in_addr_print
+ _keysockpr
+ _routeprotox
+ _rtsock_pcblist
CStrings:
+ "\t%lld IP filter%s currently attached by OS\n"
+ "\t%u enqueue source update message failure%s\n"
+ "%-18.18s "
+ "%-40.40s "
+ "%-40.40s %-40.40s "
+ "%-6.6s %-6.6s %-6.6s "
+ "%-6.6s %6u %6u "
+ "%-6s %6u %6u "
+ "Active pfkey sockets"
+ "Active routing sockets"
+ "net.route.pcblist"
+ "route"
+ "sysctl: %s for buf len %zd"
+ "sysctl: %s for len"
- "\t%u enqueue source udpate message failure%s\n"
- "got %d twice\n"

```
