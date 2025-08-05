## netstat

> `/usr/sbin/netstat`

```diff

 726.0.0.0.0
-  __TEXT.__text: 0x17290
+  __TEXT.__text: 0x173bc
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__cstring: 0xae4c
+  __TEXT.__cstring: 0xaf2b
   __TEXT.__const: 0xd8
   __TEXT.__unwind_info: 0x158
   __DATA_CONST.__auth_got: 0x250

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
   __DATA.__data: 0x884
-  __DATA.__bss: 0xab68
+  __DATA.__bss: 0xab90
   __DATA.__common: 0x728
   - /usr/lib/libSystem.B.dylib
-  UUID: 98671020-CED4-3BCC-966E-1D05E1E0ACD7
+  UUID: A09FE526-9F3E-3360-A33B-AA8F3FD402B5
   Functions: 89
   Symbols:   292
-  CStrings:  1780
+  CStrings:  1785
 
Functions:
~ _print_if_ports_used_stats : 2736 -> 3036
CStrings:
+ "\t%llu delayed wake packet%s\n"
+ "\t%llu ignored delayed attributed event%s\n"
+ "\t%llu ignored delayed unattributed event%s\n"
+ "\t%llu ignored wake packet%s in same wake cycle\n"
+ "\t%llu spurious no wake from sleep packet event%s\n"
+ "\t%llu wake pkt event notifications%s in vain\n"
- "\t%llu spurious wake packet event%s\n"

```
