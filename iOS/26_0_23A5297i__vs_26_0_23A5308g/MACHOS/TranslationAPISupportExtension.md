## TranslationAPISupportExtension

> `/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension`

```diff

-345.0.0.0.0
+348.1.0.0.0
   __TEXT.__text: 0x1a8e0
   __TEXT.__auth_stubs: 0x11f0
   __TEXT.__objc_methlist: 0x1b4

   __DATA_CONST.__auth_got: 0x8f8
   __DATA_CONST.__got: 0x318
   __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA_CONST.__const: 0x778
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DC87C53E-794B-3963-B3B8-CEF136B10F82
+  UUID: 34F9AB58-C319-3285-BC81-B7F685A3EDF3
   Functions: 561
-  Symbols:   178
+  Symbols:   179
   CStrings:  149
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
