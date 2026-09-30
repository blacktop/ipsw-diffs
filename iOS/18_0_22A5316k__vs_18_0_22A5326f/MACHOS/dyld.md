## dyld

> `/usr/lib/dyld`

```diff

-1230.3.0.0.0
-  __TEXT.__text: 0x71d7c
+1231.1.0.0.0
+  __TEXT.__text: 0x7223c
   __TEXT.__const: 0x1c30
   __TEXT.__cstring: 0xdead
   __TEXT.__info_plist: 0x4ee

   __DATA_DIRTY.__bss: 0x1bc0
   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__allocator: 0x44000
-  Functions: 2359
-  Symbols:   3252
+  Functions: 2360
+  Symbols:   3253
   CStrings:  1773
 
Symbols:
+ __ZN3lsl14readPVLEUInt64ERNSt3__14spanISt4byteLm18446744073709551615EEERy
+ __ZN5dyld45Atlas5ImageD1Ev
- __ZN3lsl14readPVLEUInt64ERNSt3__14spanISt4byteLm18446744073709551615EEE
CStrings:
+ "1231.1"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Jul 30 20:37:53 PDT 2024; root:libignition-56~37036/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Tue Jul 30 20:37:53 PDT 2024; root:libignition-56~37036/libignition_core/RELEASE_ARM64E"
- "1230.3"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Jul 15 21:20:53 PDT 2024; root:libignition-56~33984/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Mon Jul 15 21:20:53 PDT 2024; root:libignition-56~33984/libignition_core/RELEASE_ARM64E"

```
