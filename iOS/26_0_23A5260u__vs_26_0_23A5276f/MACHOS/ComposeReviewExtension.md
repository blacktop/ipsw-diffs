## ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension`

```diff

-7.0.43.2.1
-  __TEXT.__text: 0x26e4
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__const: 0x2d2
+7.0.48.0.0
+  __TEXT.__text: 0x1fc0
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__const: 0x2c2
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x94
-  __TEXT.__swift5_typeref: 0x43d
+  __TEXT.__swift5_typeref: 0x42f
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_assocty: 0x48
+  __TEXT.__cstring: 0x81
   __TEXT.__objc_methname: 0x8
-  __TEXT.__oslogstring: 0x85
-  __TEXT.__cstring: 0x17
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x180
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__auth_ptr: 0x1a0
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x100
+  __DATA.__data: 0xf8
   __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DA694330-99B3-3D5D-A896-2672CAAAC421
-  Functions: 82
-  Symbols:   78
-  CStrings:  3
+  UUID: 8CD2914D-5826-36D0-BB8C-7CDA4DBB056B
+  Functions: 71
+  Symbols:   60
+  CStrings:  2
 
Symbols:
+ _objc_release_x23
- __os_log_impl
- __swiftImmortalRefCount
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _malloc_size
- _memcpy
- _memmove
- _objc_release_x21
- _os_log_type_enabled
- _swift_allocObject
- _swift_bridgeObjectRelease
- _swift_bridgeObjectRetain
- _swift_getObjectType
- _swift_isUniquelyReferenced_nonNull_native
- _swift_slowAlloc
- _swift_slowDealloc
- _swift_unknownObjectRetain
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "ReviewExtensionService"

```
