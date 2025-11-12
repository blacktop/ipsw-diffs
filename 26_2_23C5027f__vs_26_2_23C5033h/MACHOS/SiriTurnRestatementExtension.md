## SiriTurnRestatementExtension

> `/System/Library/ExtensionKit/Extensions/SiriTurnRestatementExtension.appex/SiriTurnRestatementExtension`

```diff

-3510.3.1.0.0
+3510.3.2.0.0
   __TEXT.__text: 0x43c8
   __TEXT.__auth_stubs: 0x610
   __TEXT.__const: 0x2b6

   __DATA_CONST.__auth_got: 0x308
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x158
-  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0xd0
   __DATA.__bss: 0x390

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CB5CA1DC-7C8E-3E85-8C3D-F7B4B3ADFE86
+  UUID: 109A7368-D5F8-365F-8E54-77EA9E21FA17
   Functions: 86
-  Symbols:   80
+  Symbols:   81
   CStrings:  15
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression

```
