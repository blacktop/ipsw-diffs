## mDNSResponderHelper

> `/usr/sbin/mDNSResponderHelper`

```diff

-2559.80.8.0.0
-  __TEXT.__text: 0x2f20
+2600.100.146.0.0
+  __TEXT.__text: 0x2ef8
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__const: 0x13d
+  __TEXT.__const: 0x154
   __TEXT.__cstring: 0x2e0
   __TEXT.__oslogstring: 0xce7
-  __TEXT.__unwind_info: 0xa8
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0xa0

   __DATA.__data: 0x18
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  Functions: 17
-  Symbols:   129
+  Functions: 16
+  Symbols:   130
   CStrings:  98
 
Symbols:
+ _mh_command_copy_app_service_types

```
