## libsystemstats.dylib

> `/usr/lib/libsystemstats.dylib`

```diff

-510.0.0.0.0
-  __TEXT.__text: 0x78e0
+510.120.2.0.0
+  __TEXT.__text: 0x7e88
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x6ad
+  __TEXT.__cstring: 0x6cb
   __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__oslogstring: 0xb9f
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__oslogstring: 0xd35
+  __TEXT.__unwind_info: 0x268
   __TEXT.__objc_methname: 0x185
   __TEXT.__objc_stubs: 0x240
   __DATA_CONST.__got: 0x60

   __DATA_CONST.__objc_selrefs: 0x98
   __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__cfstring: 0x180
   __DATA.__bss: 0x18
   __DATA_DIRTY.__data: 0x540
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 631CF64C-EB20-3A51-87B1-EE199360E639
-  Functions: 179
-  Symbols:   204
-  CStrings:  173
+  UUID: 7A68A33C-C2BE-3B24-931A-9CAC004BC2C8
+  Functions: 190
+  Symbols:   206
+  CStrings:  182
 
Symbols:
+ _systemstats_get_microstackshot_cycle_interval_xlog_tasking
+ _systemstats_set_microstackshot_cycle_interval_xlog_tasking
CStrings:
+ "Invalid microstackshot cycle xlog tasking: %llu < min %llu"
+ "Invalid microstackshot cycle xlog tasking: %llu > max %llu"
+ "Invalid number for microstackshot cycle interval xlog tasking: %lld"
+ "Microstackshot PMI cycle interval xlog tasked to %llu"
+ "Microstackshot PMI cycle interval xlog tasked to disabled"
+ "Must be root to get microstackshot cycle xlog tasking"
+ "Must be root to set microstackshot cycle xlog tasking"
+ "xlog_tasking.PMICycleInterval"

```
