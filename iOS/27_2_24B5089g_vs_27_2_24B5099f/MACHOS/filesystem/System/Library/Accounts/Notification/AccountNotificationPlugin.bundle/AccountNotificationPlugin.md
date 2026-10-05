## AccountNotificationPlugin

> `/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/AccountNotificationPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-291.125.4.0.0
-  __TEXT.__text: 0x7f4
+291.125.7.0.0
+  __TEXT.__text: 0x824
   __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_stubs: 0x280
+  __TEXT.__objc_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x1a4
   __TEXT.__const: 0x20
   __TEXT.__oslogstring: 0x1ce
   __TEXT.__cstring: 0xf5
   __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x424
+  __TEXT.__objc_methname: 0x471
   __TEXT.__objc_methtype: 0x214
   __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0xe8

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0xc8
-  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__got: 0x48
   __DATA.__objc_const: 0x230
-  __DATA.__objc_selrefs: 0x180
+  __DATA.__objc_selrefs: 0x188
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 12
-  Symbols:   39
-  CStrings:  99
+  Symbols:   41
+  CStrings:  100
 
Symbols:
+ _OBJC_CLASS_$_FARestrictionsManagementSettings
+ ___kCFBooleanTrue
Functions:
~ sub_eb4 -> sub_f14 : 192 -> 240
CStrings:
+ "restrictionsManagementSettingsWithIsManaged:hasStrictPolicy:"
+ "setRestrictions:managementSettings:completion:"
- "setRestrictionsWithCompletion:"
```
