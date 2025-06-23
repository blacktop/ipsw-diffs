## SOSSettings

> `/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings`

```diff

-651.100.2.0.0
-  __TEXT.__text: 0x113f4
-  __TEXT.__auth_stubs: 0xd60
+652.100.2.0.0
+  __TEXT.__text: 0x10d1c
+  __TEXT.__auth_stubs: 0xcf0
   __TEXT.__objc_stubs: 0x20e0
   __TEXT.__objc_methlist: 0xae0
-  __TEXT.__cstring: 0x1100
+  __TEXT.__cstring: 0x1190
   __TEXT.__objc_classname: 0x1cc
   __TEXT.__objc_methname: 0x2d6a
   __TEXT.__objc_methtype: 0x7ce
-  __TEXT.__oslogstring: 0x795
+  __TEXT.__oslogstring: 0x70c
   __TEXT.__const: 0x364
-  __TEXT.__swift5_typeref: 0xabc
+  __TEXT.__swift5_typeref: 0xaae
   __TEXT.__swift5_capture: 0x130
   __TEXT.__constg_swiftt: 0x3c8
   __TEXT.__swift5_reflstr: 0xbd

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x518
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__eh_frame: 0x414
-  __DATA_CONST.__auth_got: 0x6b8
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__auth_got: 0x680
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_ptr: 0x1a8
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x68

   __DATA.__objc_selrefs: 0xc48
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x670
-  __DATA.__data: 0x920
+  __DATA.__data: 0x918
   __DATA.__bss: 0x178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

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
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7AF55123-A629-3048-A6EE-6D7AD67D41DE
-  Functions: 361
-  Symbols:   274
+  UUID: 352A41BC-29A1-3943-9330-22ACCEBD4727
+  Functions: 351
+  Symbols:   266
   CStrings:  772
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
- __swiftImmortalRefCount
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _malloc_size
- _memmove
- _swift_isUniquelyReferenced_nonNull_native
- _swift_slowAlloc
- _swift_slowDealloc
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."

```
