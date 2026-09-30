## install_monitor

> `System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/Resources/install_monitor`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1491.160.2.700.1
-  __TEXT.__text: 0xd4c
-  __TEXT.__auth_stubs: 0x210
+1491.160.2.701.2
+  __TEXT.__text: 0xda8
+  __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__const: 0x60
-  __TEXT.__objc_methname: 0x2b5
-  __TEXT.__cstring: 0x274
+  __TEXT.__objc_methname: 0x2c8
+  __TEXT.__cstring: 0x2ab
   __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methtype: 0x97
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x8

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 16
-  Symbols:   53
-  CStrings:  76
+  Symbols:   55
+  CStrings:  77
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _PKSIPWriteDataSafely
Functions:
~ sub_100000ce8 -> sub_100000d58 : 568 -> 660
CStrings:
+ "PackageKit: Could not write exclusion state to %s (%s)"
+ "dataWithPropertyList:format:options:error:"
- "writeToFile:atomically:"
```
