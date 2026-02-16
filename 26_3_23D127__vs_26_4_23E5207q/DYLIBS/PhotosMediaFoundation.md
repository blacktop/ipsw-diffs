## PhotosMediaFoundation

> `/System/Library/PrivateFrameworks/PhotosMediaFoundation.framework/PhotosMediaFoundation`

```diff

-832.0.107.0.0
-  __TEXT.__text: 0x1ffc
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x414
+840.1.220.0.0
+  __TEXT.__text: 0x22f8
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x42c
   __TEXT.__swift5_typeref: 0x2b
   __TEXT.__const: 0xb8
   __TEXT.__swift5_reflstr: 0x9

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xb0
-  __TEXT.__cstring: 0x2a7
+  __TEXT.__gcc_except_tab: 0xbc
+  __TEXT.__cstring: 0x2d3
   __TEXT.__oslogstring: 0x1a2
-  __TEXT.__unwind_info: 0x170
+  __TEXT.__unwind_info: 0x168
   __TEXT.__objc_classname: 0x174
-  __TEXT.__objc_methname: 0x991
+  __TEXT.__objc_methname: 0xa18
   __TEXT.__objc_methtype: 0x386
-  __TEXT.__objc_stubs: 0x600
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x1e0
+  __TEXT.__objc_stubs: 0x680
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x270
+  __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__auth_got: 0x1f0
   __AUTH_CONST.__const: 0xd8
   __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x860
+  __AUTH_CONST.__objc_const: 0x8a0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x258

   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 1C543EEA-A685-3A67-87E9-B541161F3131
-  Functions: 70
-  Symbols:   394
-  CStrings:  211
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 5C8FB192-BE18-3996-A9A7-F72FF0CD5D3B
+  Functions: 72
+  Symbols:   421
+  CStrings:  217
 
Symbols:
+ -[AVPlayerItem(PhotosMediaFoundation) queryHasCaptionsWithCompletion:]
+ _AVMediaCharacteristicLegible
+ _OBJC_CLASS_$_AVPlayerItem
+ __OBJC_$_CATEGORY_AVPlayerItem_$_PhotosMediaFoundation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_AVPlayerItem_$_PhotosMediaFoundation
+ ___70-[AVPlayerItem(PhotosMediaFoundation) queryHasCaptionsWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e43_v24?0"AVMediaSelectionGroup"8"NSError"16ls32l8
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_PhotosMediaFoundation
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_PhotosMediaFoundation
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_PhotosMediaFoundation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_PhotosMediaFoundation
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_PhotosMediaFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_PhotosMediaFoundation
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_PhotosMediaFoundation
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_PhotosMediaFoundation
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_PhotosMediaFoundation
+ _objc_msgSend$asset
+ _objc_msgSend$hasMediaCharacteristic:
+ _objc_msgSend$loadMediaSelectionGroupForMediaCharacteristic:completionHandler:
+ _objc_msgSend$options
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "asset"
+ "hasMediaCharacteristic:"
+ "loadMediaSelectionGroupForMediaCharacteristic:completionHandler:"
+ "options"
+ "queryHasCaptionsWithCompletion:"
+ "v24@?0@\"AVMediaSelectionGroup\"8@\"NSError\"16"

```
