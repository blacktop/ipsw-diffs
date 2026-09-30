## MeasureSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/MeasureSettingsAppIntentsExtension.appex/MeasureSettingsAppIntentsExtension`

```diff

-181.40.1.0.0
+181.60.2.0.0
   __TEXT.__text: 0x3fb0
   __TEXT.__auth_stubs: 0x540
   __TEXT.__const: 0x7b8

   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x188
   __DATA.__bss: 0xc10

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
-  UUID: 20DB6552-EEAD-3F0C-A77B-8BC672DF451F
+  UUID: 9D1C7700-CD3A-3B63-A470-4BE58E47D3C9
   Functions: 128
-  Symbols:   45
+  Symbols:   50
   CStrings:  23
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia

```
