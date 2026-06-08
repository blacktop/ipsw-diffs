## CommunicationSafetySettings

> `/System/Library/PreferenceBundles/CommunicationSafetySettings.bundle/CommunicationSafetySettings`

```diff

-34.4.1.0.0
+37.0.0.0.0
   __TEXT.__text: 0x76c
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_stubs: 0x160

   __TEXT.__objc_classname: 0x1c
   __TEXT.__objc_methtype: 0x21
   __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48
   __DATA.__objc_selrefs: 0x60
   __DATA.__objc_data: 0x70

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2951B8EA-D6F7-3BAE-86F0-90B2462D61DF
+  UUID: C783782F-0385-3AC5-98BF-8302575A9D59
   Functions: 14
-  Symbols:   54
+  Symbols:   53
   CStrings:  17
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftVideoToolbox

```
