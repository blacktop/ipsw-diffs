## ClockAppIntents

> `/System/Library/ExtensionKit/Extensions/ClockAppIntents.appex/ClockAppIntents`

```diff

-268.2.1.0.0
+268.2.2.0.0
   __TEXT.__text: 0x1bc
   __TEXT.__auth_stubs: 0x70
   __TEXT.__const: 0xaa

   __DATA_CONST.__auth_got: 0x38
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x10
   __DATA.__bss: 0x100

   - /System/Library/PrivateFrameworks/ClockAppIntentsSupport.framework/ClockAppIntentsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 52895F0F-A054-3C12-AE69-0C623C5A04DB
+  UUID: 586BF487-DCB5-3134-95F9-F0944FD92B80
   Functions: 9
-  Symbols:   28
+  Symbols:   30
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
