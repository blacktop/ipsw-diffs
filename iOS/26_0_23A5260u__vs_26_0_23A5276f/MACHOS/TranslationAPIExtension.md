## TranslationAPIExtension

> `/System/Library/ExtensionKit/Extensions/TranslationAPIExtension.appex/TranslationAPIExtension`

```diff

-336.4.0.0.0
-  __TEXT.__text: 0x1a4d0
-  __TEXT.__auth_stubs: 0x11a0
+341.0.0.0.0
+  __TEXT.__text: 0x1a440
+  __TEXT.__auth_stubs: 0x11b0
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0xc92
+  __TEXT.__const: 0xc82
   __TEXT.__swift5_typeref: 0x12b5
-  __TEXT.__cstring: 0x707
+  __TEXT.__cstring: 0x797
   __TEXT.__objc_methname: 0x43e
   __TEXT.__constg_swiftt: 0x72c
   __TEXT.__swift5_reflstr: 0x22f
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_fieldmd: 0x254
   __TEXT.__swift5_capture: 0x1bc
-  __TEXT.__oslogstring: 0x49d
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x34
+  __TEXT.__oslogstring: 0x40d
   __TEXT.__swift5_protos: 0x8
   __TEXT.__objc_classname: 0x25
   __TEXT.__objc_methtype: 0x152

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x748
   __TEXT.__eh_frame: 0x6f4
-  __DATA_CONST.__auth_got: 0x8d0
+  __DATA_CONST.__auth_got: 0x8d8
   __DATA_CONST.__got: 0x310
   __DATA_CONST.__auth_ptr: 0x3b0
-  __DATA_CONST.__const: 0x760
+  __DATA_CONST.__const: 0x750
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 506A068D-A1E9-3047-A379-4B1F321DA0A1
+  UUID: D45425CF-D75D-3BCC-82AB-622DC2627089
   Functions: 560
-  Symbols:   180
+  Symbols:   178
   CStrings:  149
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."

```
