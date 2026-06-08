## ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension`

```diff

-7.5.10.2.1
-  __TEXT.__text: 0x2078
-  __TEXT.__auth_stubs: 0x4c0
+8.0.35.2.1
+  __TEXT.__text: 0x22a0
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x358
+  __TEXT.__const: 0x350
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x94
-  __TEXT.__swift5_typeref: 0x42f
+  __TEXT.__swift5_typeref: 0x3cf
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__cstring: 0x81
+  __TEXT.__oslogstring: 0x85
+  __TEXT.__cstring: 0x17
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_methname: 0x8
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x130
+  __TEXT.__unwind_info: 0x100
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x1b8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0xf8
+  __DATA.__data: 0xb8
   __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit

   - /System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6CF7CF7C-7F33-3627-8E86-D02FD696F87B
-  Functions: 79
-  Symbols:   59
-  CStrings:  2
+  UUID: 31B25EA7-2297-3AFC-A45B-4275C5F51F55
+  Functions: 80
+  Symbols:   83
+  CStrings:  3
 
Symbols:
+ __os_log_impl
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_release_x25
+ _os_log_type_enabled
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x28
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x28
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_release
- _objc_release_x21
- _objc_release_x24
- _objc_retain_x21
- _swift_errorRelease
CStrings:
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "ReviewExtensionService"
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."

```
