## dyld

> `/usr/lib/dyld`

```diff

-1376.6.0.0.0
-  __TEXT.__text: 0x9146c
+1376.7.0.0.0
+  __TEXT.__text: 0x914cc
   __TEXT.__const: 0x2038
   __TEXT.__cstring: 0xffdd
   __TEXT.__unwind_info: 0x4f0

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  UUID: 34F54DC6-1319-3C1B-B798-A7F2CB95415E
+  UUID: E6DECFD2-EFE3-3F28-B2EF-C8D7042F9330
   Functions: 2990
-  Symbols:   4132
+  Symbols:   4134
   CStrings:  2000
 
Symbols:
+ _ZN3lsl9Allocator4freeEPv.cold.1
+ _ZN3lsl9Allocator7reallocEPvy.cold.1
Functions:
~ __ZN3lsl9Allocator7reallocEPvy : 264 -> 308
~ __ZN3lsl9Allocator4freeEPv : 52 -> 156
~ __ZN3lsl9Allocator10freeObjectEPv : 108 -> 80
~ _dyld_parse_boot_arg_int : 456 -> 432
CStrings:
+ "1376.7"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Mar  5 23:12:42 PST 2026; root:libignition-58~36921/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Thu Mar  5 23:12:42 PST 2026; root:libignition-58~36921/libignition_core/RELEASE_ARM64E"
- "1376.6"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Feb 26 23:05:24 PST 2026; root:libignition-58~36759/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Thu Feb 26 23:05:24 PST 2026; root:libignition-58~36759/libignition_core/RELEASE_ARM64E"

```
