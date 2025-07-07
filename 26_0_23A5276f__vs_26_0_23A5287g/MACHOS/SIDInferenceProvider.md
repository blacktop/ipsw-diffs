## SIDInferenceProvider

> `/System/Library/ExtensionKit/Extensions/SIDInferenceProvider.appex/SIDInferenceProvider`

```diff

-1.20.0.0.0
+1.22.0.0.0
   __TEXT.__text: 0xacb0
   __TEXT.__auth_stubs: 0xe40
   __TEXT.__objc_stubs: 0x2c0

   __DATA_CONST.__auth_got: 0x730
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6ABB287D-8AA8-376B-AFB3-0A2B2ED7F747
+  UUID: 1764E6F0-DB0B-3BF7-AA1A-EB0D9157D50D
   Functions: 161
-  Symbols:   184
+  Symbols:   187
   CStrings:  125
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftIntents

```
