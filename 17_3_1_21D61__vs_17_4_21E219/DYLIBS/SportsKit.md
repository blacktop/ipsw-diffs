## SportsKit

> `/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit`

```diff

-159.20.11.0.0
-  __TEXT.__text: 0xc06e4
-  __TEXT.__auth_stubs: 0x1ef0
+159.40.26.0.0
+  __TEXT.__text: 0xc0fd8
+  __TEXT.__auth_stubs: 0x1f80
   __TEXT.__objc_methlist: 0x688
-  __TEXT.__const: 0xbe98
+  __TEXT.__const: 0xbe78
+  __TEXT.__cstring: 0x494c
   __TEXT.__swift5_typeref: 0x31ac
   __TEXT.__swift5_capture: 0x5e0
-  __TEXT.__cstring: 0x453c
   __TEXT.__swift5_reflstr: 0x1f93
   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__constg_swiftt: 0x3850

   __TEXT.__swift5_types: 0x3e0
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x55c8
-  __TEXT.__eh_frame: 0x5b2c
+  __TEXT.__unwind_info: 0x5420
+  __TEXT.__eh_frame: 0x5afc
   __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0xa25
+  __TEXT.__objc_methname: 0xa38
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x7b0
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x7c0
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3c78
   __DATA_CONST.__objc_selrefs: 0x2c0
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x98
   __AUTH_CONST.__const: 0x8170
   __AUTH_CONST.__objc_const: 0x40
-  __AUTH_CONST.__auth_got: 0xf78
-  __AUTH.__data: 0xd20
+  __AUTH_CONST.__auth_got: 0xfc0
+  __AUTH.__data: 0xd18
   __AUTH.__objc_data: 0x12f8
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x98
   __DATA.__objc_data: 0x1a8
-  __DATA.__data: 0x2db0
-  __DATA.__bss: 0x134b0
-  __DATA.__common: 0x78
+  __DATA.__data: 0x2db8
+  __DATA.__bss: 0x13430
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x17c0
-  __DATA_DIRTY.__data: 0x2ec0
-  __DATA_DIRTY.__bss: 0x4d00
-  __DATA_DIRTY.__common: 0xf0
+  __DATA_DIRTY.__data: 0x2f08
+  __DATA_DIRTY.__bss: 0x4d80
+  __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 44BF32FE-B3CD-386E-91DC-9DB4F5BD7F86
-  Functions: 8472
-  Symbols:   3979
-  CStrings:  716
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 6E9AD947-2016-3ED0-98D2-AE67BC45AAB3
+  Functions: 8487
+  Symbols:   3987
+  CStrings:  739
 
Symbols:
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_SportsKit
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_SportsKit
+ _block_copy_helper.19
+ _block_copy_helper.28
+ _block_copy_helper.34
+ _block_descriptor.21
+ _block_descriptor.30
+ _block_descriptor.36
+ _block_destroy_helper.20
+ _block_destroy_helper.29
+ _block_destroy_helper.35
+ _objc_release_x9
+ _objc_retain_x1
+ _objc_retain_x2
+ _swift_unknownObjectRetain_n
- _OUTLINED_FUNCTION_224
- _OUTLINED_FUNCTION_225
- _OUTLINED_FUNCTION_226
- _block_copy_helper.20
- _block_copy_helper.29
- _block_copy_helper.35
- _block_descriptor.22
- _block_descriptor.31
- _block_descriptor.37
- _block_destroy_helper.21
- _block_destroy_helper.30
- _block_destroy_helper.36
CStrings:
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Negative value is not representable"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "invalid Collection: less than 'count' elements in collection"

```
