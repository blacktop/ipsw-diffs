## mDNSResponderHelper

> `/usr/sbin/mDNSResponderHelper`

```diff

-2600.120.12.0.0
+2862.0.0.0.1
   __TEXT.__text: 0x2ef8
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__const: 0x154
+  __TEXT.__const: 0x151
   __TEXT.__cstring: 0x2e0
   __TEXT.__oslogstring: 0xce7
   __TEXT.__unwind_info: 0xa0

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: EAF2F766-BC40-384B-B991-8F80581A7CE1
+  - /usr/lib/libobjc.A.dylib
+  UUID: AEED0137-0634-3179-9ED3-A561C1BB50CC
   Functions: 16
   Symbols:   130
   CStrings:  98
Symbols:
+ _mh_command_copy_app_trust_info
- _mh_command_copy_app_service_types

```
