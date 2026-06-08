## SCARemoteView Appex

> `/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/SCARemoteView Appex`

```diff

-130.4.1.0.0
-  __TEXT.__text: 0x5ed8
-  __TEXT.__auth_stubs: 0x830
+145.0.0.0.0
+  __TEXT.__text: 0x5f30
+  __TEXT.__auth_stubs: 0x980
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x5b8
-  __TEXT.__constg_swiftt: 0x34c
-  __TEXT.__swift5_typeref: 0x7f5
+  __TEXT.__const: 0x548
+  __TEXT.__constg_swiftt: 0x358
+  __TEXT.__swift5_typeref: 0x7a9
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_fieldmd: 0xe4
-  __TEXT.__swift5_reflstr: 0x76
+  __TEXT.__swift5_reflstr: 0x77
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_capture: 0x84
-  __TEXT.__cstring: 0x20f
+  __TEXT.__cstring: 0x17f
+  __TEXT.__oslogstring: 0x85
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
+  __TEXT.__swift_as_cont: 0x1c
   __TEXT.__objc_methname: 0x28
   __TEXT.__objc_methtype: 0x11
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__unwind_info: 0x248
   __TEXT.__eh_frame: 0x2b4
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__auth_ptr: 0x200
-  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x220
   __DATA.__objc_const: 0x28
   __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x380
+  __DATA.__data: 0x418
   __DATA.__bss: 0x438
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit

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
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 20F2C776-9367-32F5-94C6-DB8C5B68C3E1
-  Functions: 127
-  Symbols:   103
+  UUID: 381A672A-F3E9-32A4-9AAB-07DA55CFB3D9
+  Functions: 136
+  Symbols:   120
   CStrings:  24
 
Symbols:
+ __os_log_impl
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCompression
+ _memcpy
+ _memmove
+ _objc_release_x23
+ _os_log_type_enabled
+ _swift_beginAccess
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_endAccess
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x23
+ _swift_release_x8
+ _swift_retain_x25
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRetain
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- _objc_release_x24
- _objc_release_x28
- _objc_retain_x8
CStrings:
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."

```
