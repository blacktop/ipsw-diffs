## managedcorespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/managedcorespotlightd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x4100
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0xc00
+2459.405.0.0.0
+  __TEXT.__text: 0x4148
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0xc20
   __TEXT.__objc_methlist: 0x704
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__objc_methname: 0xf2d
+  __TEXT.__objc_methname: 0xf43
   __TEXT.__cstring: 0x4b3
   __TEXT.__oslogstring: 0x51d
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methtype: 0x3f5
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__unwind_info: 0x1b0
   __DATA_CONST.__const: 0x300
   __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0x118
   __DATA.__objc_const: 0xd80
-  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_selrefs: 0x4e0
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180

   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
+  - /System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework
   - /System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon
   - /System/Library/PrivateFrameworks/SpotlightIndex.framework/Versions/A/SpotlightIndex
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 145
-  Symbols:   134
-  CStrings:  331
+  Symbols:   138
+  CStrings:  332
 
Symbols:
+ _OBJC_CLASS_$_SAUserSetupState
+ _getuid
+ _objc_opt_class
+ _xpc_dictionary_get_int64
Functions:
~ sub_1000015d8 -> sub_100001660 : 8 -> 80
CStrings:
+ "getSetupStateForUser:"
```
