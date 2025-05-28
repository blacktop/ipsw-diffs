## PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

-525.60.9.0.0
-  __TEXT.__text: 0x64c
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0x160
+525.100.35.0.0
+  __TEXT.__text: 0x6d8
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_stubs: 0x1c0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x18c
+  __TEXT.__cstring: 0x1e2
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__objc_methname: 0xf7
+  __TEXT.__objc_methname: 0x133
   __TEXT.__unwind_info: 0x64
-  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x58
-  __DATA.__objc_classrefs: 0x48
-  __DATA.__bss: 0x40
+  __DATA_CONST.__objc_classrefs: 0x48
+  __DATA.__objc_selrefs: 0x70
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 6
-  Symbols:   50
-  CStrings:  28
+  Symbols:   52
+  CStrings:  34
 
Symbols:
+ _MGGetBoolAnswer
+ ___CFConstantStringClassReference
CStrings:
+ "DeviceSupports80ChargeLimit"
+ "allowMCLOverride"
+ "boolValue"
+ "com.apple.smartcharging.topoffprotection"
+ "isInternalBuild"
+ "numberForPreferenceKey:inDomain:"

```
