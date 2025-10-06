## DepthCore

> `/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore`

```diff

 159.6.0.0.0
-  __TEXT.__text: 0x24814
-  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__text: 0x24f78
+  __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0x70
-  __TEXT.__const: 0x29c6
+  __TEXT.__const: 0x2ab6
   __TEXT.__swift5_typeref: 0xb12
   __TEXT.__constg_swiftt: 0x9b4
   __TEXT.__swift5_reflstr: 0x866

   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x27c
   __TEXT.__swift5_types: 0xf4
-  __TEXT.__cstring: 0xee6
+  __TEXT.__cstring: 0x1206
   __TEXT.__swift5_capture: 0x148
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x1adc
-  __TEXT.__eh_frame: 0xd38
+  __TEXT.__unwind_info: 0x1ad0
+  __TEXT.__eh_frame: 0xd48
   __TEXT.__objc_methname: 0x465
   __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5d0
   __DATA_CONST.__objc_selrefs: 0x1e8
+  __DATA_CONST.__objc_classrefs: 0xb8
   __AUTH_CONST.__const: 0x23b0
-  __AUTH_CONST.__auth_got: 0x710
-  __AUTH.__data: 0x310
-  __AUTH.__objc_data: 0x2f8
-  __DATA.__objc_classrefs: 0xb8
-  __DATA.__data: 0x880
+  __AUTH_CONST.__auth_got: 0x728
+  __AUTH.__objc_data: 0x100
+  __AUTH.__data: 0x2e8
+  __DATA.__data: 0x930
   __DATA.__bss: 0x4fa0
-  __DATA.__common: 0xb8
+  __DATA.__common: 0x98
+  __DATA_DIRTY.__objc_data: 0x1f8
+  __DATA_DIRTY.__data: 0x48
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C67A46DB-C686-39F4-B5FE-E02EDB1FC005
-  Functions: 1512
-  Symbols:   525
-  CStrings:  160
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 64EF0A84-B8E7-3083-9C83-F6A400AA164B
+  Functions: 1532
+  Symbols:   529
+  CStrings:  176
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_DepthCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_DepthCore
+ _block_copy_helper.30
+ _block_copy_helper.59
+ _block_copy_helper.71
+ _block_descriptor.32
+ _block_descriptor.61
+ _block_descriptor.73
+ _block_destroy_helper.31
+ _block_destroy_helper.60
+ _block_destroy_helper.72
+ _objc_retain_x26
- _block_copy_helper.25
- _block_copy_helper.60
- _block_copy_helper.72
- _block_descriptor.27
- _block_descriptor.62
- _block_descriptor.74
- _block_destroy_helper.26
- _block_destroy_helper.61
- _block_destroy_helper.73
- _swift_setDeallocating
CStrings:
+ "Can't construct Array with count < 0"
+ "Insufficient space allocated to copy string contents"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```
