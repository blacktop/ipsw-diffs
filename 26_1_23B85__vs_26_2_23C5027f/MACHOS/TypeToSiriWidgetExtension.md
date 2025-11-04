## TypeToSiriWidgetExtension

> `/Applications/Siri.app/PlugIns/TypeToSiriWidgetExtension.appex/TypeToSiriWidgetExtension`

```diff

-3505.22.1.11.1
+3510.4.2.0.0
   __TEXT.__text: 0x3ee4
   __TEXT.__auth_stubs: 0x400
   __TEXT.__cstring: 0x1d9

   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x1c0
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x1c8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9AC65CA8-99B7-30B2-BC14-FA5E6880A6EF
+  UUID: 03C5D5EE-55DE-3896-8BD0-83F55457DC0A
   Functions: 105
-  Symbols:   53
+  Symbols:   59
   CStrings:  19
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftVideoToolbox

```
