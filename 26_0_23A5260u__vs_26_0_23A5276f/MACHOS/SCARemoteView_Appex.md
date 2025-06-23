## SCARemoteView Appex

> `/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/SCARemoteView Appex`

```diff

-114.1.1.0.0
-  __TEXT.__text: 0x2bc4
-  __TEXT.__auth_stubs: 0x530
+117.0.0.0.0
+  __TEXT.__text: 0x24a0
+  __TEXT.__auth_stubs: 0x470
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x450
-  __TEXT.__swift5_typeref: 0x383
+  __TEXT.__const: 0x440
+  __TEXT.__swift5_typeref: 0x375
   __TEXT.__swift5_capture: 0x58
   __TEXT.__objc_methname: 0x1b
   __TEXT.__swift5_reflstr: 0x52

   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x14
-  __TEXT.__cstring: 0x4a
+  __TEXT.__cstring: 0xd1
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x85
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x360
+  __TEXT.__unwind_info: 0x160
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__auth_ptr: 0x198
+  __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x28
   __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x298
   __DATA.__bss: 0x408
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1D758384-4975-3652-B0ED-C0E0892AECA1
-  Functions: 97
-  Symbols:   91
+  UUID: 540FD4A9-0DF9-31A2-98C8-504A10BDF393
+  Functions: 86
+  Symbols:   76
   CStrings:  9
 
Symbols:
+ _objc_release_x27
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
- _objc_retain
- _os_log_type_enabled
- _swift_isUniquelyReferenced_nonNull_native
- _swift_slowAlloc
- _swift_slowDealloc
- _swift_unknownObjectRetain
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."

```
