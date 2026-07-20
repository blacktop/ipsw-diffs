## InternetSharing

> `/usr/libexec/InternetSharing`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-398.0.0.0.0
-  __TEXT.__text: 0x1be48
+399.0.0.0.0
+  __TEXT.__text: 0x1bf58
   __TEXT.__auth_stubs: 0x10c0
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x7fe6
+  __TEXT.__cstring: 0x8044
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0x3f0
   __DATA_CONST.__const: 0x510
-  __DATA_CONST.__cfstring: 0x880
+  __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0x2e0
   __DATA.__data: 0x1fc
   __DATA.__bss: 0x151
-  __DATA.__common: 0x9e
+  __DATA.__common: 0x9f
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libmrc.dylib
   Functions: 341
   Symbols:   364
-  CStrings:  1134
+  CStrings:  1138
 
Functions:
~ sub_1000173e4 : 2312 -> 2464
~ sub_10001b090 -> sub_10001b128 : 852 -> 972
CStrings:
+ "DisableHostModeAllSubnetsLocal %s"
+ "HostModeAllSubnetsLocal"
+ "all_subnets_local"
+ "use_server_config"
```
