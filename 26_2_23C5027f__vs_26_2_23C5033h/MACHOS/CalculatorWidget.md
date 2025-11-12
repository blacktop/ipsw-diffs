## CalculatorWidget

> `/private/var/staged_system_apps/Calculator.app/PlugIns/CalculatorWidget.appex/CalculatorWidget`

```diff

-122.2.3.0.0
+122.2.4.0.0
   __TEXT.__text: 0x31c4
   __TEXT.__auth_stubs: 0x410
   __TEXT.__cstring: 0x130

   __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x378
-  __DATA_CONST.__const: 0x288
+  __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x120

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 72FD70A1-1058-3BDE-95E3-5D6D9DCA60EB
+  UUID: 45DEDEA7-E929-3202-8ED1-E13C9D4E19E5
   Functions: 119
-  Symbols:   51
+  Symbols:   53
   CStrings:  7
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
