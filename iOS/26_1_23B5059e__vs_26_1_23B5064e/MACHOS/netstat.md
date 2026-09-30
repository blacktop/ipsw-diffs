## netstat

> `/usr/sbin/netstat`

```diff

-728.0.0.0.0
-  __TEXT.__text: 0x175ec
+728.40.1.0.0
+  __TEXT.__text: 0x176ec
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__cstring: 0xaece
+  __TEXT.__cstring: 0xafbc
   __TEXT.__const: 0xd8
   __TEXT.__unwind_info: 0x168
   __DATA_CONST.__auth_got: 0x258

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
   __DATA.__data: 0x884
-  __DATA.__bss: 0xab88
+  __DATA.__bss: 0xabb8
   __DATA.__common: 0x730
   - /usr/lib/libSystem.B.dylib
-  UUID: E8D315CC-ADAD-30D1-ACBD-CE79E611EAD9
+  UUID: F58A49B6-0685-3842-9535-C31A9B1C937F
   Functions: 91
   Symbols:   294
-  CStrings:  1784
+  CStrings:  1788
 
Functions:
~ _tcp_stats : 10300 -> 10428
~ _udp_stats : 1740 -> 1868
CStrings:
+ "\t%llu ICMP packet%s for port unreachable not suppressed\n"
+ "\t%llu RST packet%s for port unreachable not suppressed\n"
+ "\t%llu duplicate ICMP packet%s for port unreachable suppressed\n"
+ "\t%llu duplicate RST packet%s for port unreachable suppressed\n"

```
