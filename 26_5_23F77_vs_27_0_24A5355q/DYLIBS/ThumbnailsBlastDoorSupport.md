## ThumbnailsBlastDoorSupport

> `/System/Library/PrivateFrameworks/ThumbnailsBlastDoorSupport.framework/ThumbnailsBlastDoorSupport`

```diff

-295.600.21.0.0
-  __TEXT.__text: 0x20fc
-  __TEXT.__auth_stubs: 0x4d0
+322.100.2.2.1
+  __TEXT.__text: 0x2740
   __TEXT.__objc_methlist: 0xa4
-  __TEXT.__const: 0xda
-  __TEXT.__cstring: 0x118
-  __TEXT.__swift5_typeref: 0x96
+  __TEXT.__const: 0xc2
+  __TEXT.__cstring: 0xe8
+  __TEXT.__swift5_typeref: 0x93
+  __TEXT.__oslogstring: 0x36
   __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_reflstr: 0x11
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__unwind_info: 0x118
   __TEXT.__eh_frame: 0x90
-  __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methname: 0x17d
-  __TEXT.__objc_methtype: 0xba
-  __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x270
-  __AUTH_CONST.__const: 0x50
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x78
   __AUTH_CONST.__objc_const: 0x160
+  __AUTH_CONST.__auth_got: 0x308
   __AUTH.__objc_data: 0x128
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x70
+  __DATA.__data: 0x60
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6B49730F-5BAC-3B5C-AA78-CB3A6912D407
-  Functions: 37
-  Symbols:   140
-  CStrings:  27
+  UUID: D1226B58-D70D-3336-AD33-20C78B09D2C2
+  Functions: 44
+  Symbols:   159
+  CStrings:  6
 
Symbols:
+ ___swift_closure_destructor
+ ___swift_closure_destructor.4
+ ___swift_destroy_boxed_opaque_existential_0
+ __os_log_impl
+ __swiftImmortalRefCount
+ __swift_stdlib_malloc_size
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_retain_x2
+ _objc_retain_x3
+ _os_log_type_enabled
+ _swift_arrayDestroy
+ _swift_bridgeObjectRetain
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x22
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x28
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- _OBJC_CLASS_$_OS_os_log
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_ThumbnailsBlastDoorSupport
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- __swift_FORCE_LOAD_$_swiftVideoToolbox_$_ThumbnailsBlastDoorSupport
- _objc_release_x25
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _swift_errorRetain
- _swift_retain
- _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
CStrings:
+ "Generating thumbnail with maxPixelDim %s and scale %s"
- ".cxx_destruct"
- "@\"ThumbnailsBlastDoorInterfaceInternal\""
- "@16@0:8"
- "@40@0:8@16f24f28^@32"
- "@48@0:8@16f24f28q32^@40"
- "Generating thumbnail with maxPixelDim %@ and scale %@"
- "T@\"ThumbnailsBlastDoorInterfaceInternal\",&,N,V_interface"
- "ThumbnailsBlastDoorInterface"
- "ThumbnailsBlastDoorInterfaceInternal"
- "_interface"
- "bd"
- "dealloc"
- "generateImageThumbnailForFileURL:maxPixelDimension:scale:error:"
- "generateImageThumbnailForFileURL:maxPixelDimension:scale:frameNumber:error:"
- "generateMovieThumbnailForAttachmentWithFileURL:maxPixelDimension:minThumbnailPxSize:scale:resultHandler:"
- "init"
- "interface"
- "maxFrameCount"
- "setInterface:"
- "v16@0:8"
- "v24@0:8@16"
- "v56@0:8@16f24{CGSize=dd}28f44@?48"

```
