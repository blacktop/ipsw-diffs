## MCUIAppIntents

> `/System/Library/ExtensionKit/Extensions/MCUIAppIntents.appex/MCUIAppIntents`

```diff

-55.60.5.0.0
+55.60.7.0.0
   __TEXT.__text: 0x2efc
   __TEXT.__auth_stubs: 0x4e0
   __TEXT.__cstring: 0x2ba

   __DATA_CONST.__auth_got: 0x270
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x3a0
-  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x190
   __DATA.__bss: 0xc08

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8A62A8E6-9782-380C-AACB-B4EBA5A3F127
+  UUID: 405022D7-D727-3A6F-8B4E-EA295561FA04
   Functions: 122
-  Symbols:   44
+  Symbols:   49
   CStrings:  15
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia

```
