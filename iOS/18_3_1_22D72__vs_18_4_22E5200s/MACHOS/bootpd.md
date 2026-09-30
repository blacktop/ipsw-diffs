## bootpd

> `/usr/libexec/bootpd`

```diff

-494.80.2.0.0
-  __TEXT.__text: 0x10200
-  __TEXT.__auth_stubs: 0x8e0
+494.100.3.0.0
+  __TEXT.__text: 0x100f8
+  __TEXT.__auth_stubs: 0x8f0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x1ead
+  __TEXT.__cstring: 0x1eb3
   __TEXT.__oslogstring: 0x114f
-  __TEXT.__unwind_info: 0x2e8
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x2c8
+  __DATA_CONST.__auth_got: 0x478
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x1300
   __DATA_CONST.__cfstring: 0xbe0
   __DATA.__data: 0xa8
-  __DATA.__common: 0x119
+  __DATA.__common: 0x311
   __DATA.__bss: 0x1350
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 199
+  Functions: 193
   Symbols:   185
-  CStrings:  645
+  CStrings:  646
 
Symbols:
+ ___res_9_state
- __res
CStrings:
+ "local"

```
