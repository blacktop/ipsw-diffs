## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent`

```diff

-140.0.0.0.0
-  __TEXT.__text: 0x6bc74
+150.0.0.0.0
+  __TEXT.__text: 0x6f504
   __TEXT.__auth_stubs: 0x1f80
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x1e0
   __TEXT.__const: 0x127c
   __TEXT.__objc_classname: 0x113
-  __TEXT.__objc_methname: 0xd48
+  __TEXT.__objc_methname: 0xd8b
   __TEXT.__objc_methtype: 0x194
-  __TEXT.__cstring: 0x3595
+  __TEXT.__cstring: 0x3905
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0xbe4
-  __TEXT.__swift5_typeref: 0x10f9
+  __TEXT.__swift5_typeref: 0x10e1
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x7ad
   __TEXT.__swift5_fieldmd: 0x754

   __TEXT.__swift5_types: 0x84
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_capture: 0x34c
-  __TEXT.__unwind_info: 0x1a58
-  __TEXT.__eh_frame: 0x1cd0
+  __TEXT.__unwind_info: 0x1ac8
+  __TEXT.__eh_frame: 0x1ce0
   __DATA_CONST.__auth_got: 0xfc8
-  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__got: 0x598
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x2150
+  __DATA_CONST.__const: 0x21c8
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0xd8
   __DATA.__objc_const: 0x1870
-  __DATA.__objc_selrefs: 0x2c0
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0xd8
+  __DATA.__objc_selrefs: 0x2d0
   __DATA.__objc_data: 0x528
-  __DATA.__data: 0x1840
+  __DATA.__data: 0x1830
   __DATA.__bss: 0x1990
-  __DATA.__common: 0x49
+  __DATA.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1234
-  Symbols:   807
-  CStrings:  414
+  Functions: 1254
+  Symbols:   806
+  CStrings:  436
 
Symbols:
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ _swift_unknownObjectRetain_n
- _$s15ManagedSettings14XPCConnectableP19interruptionHandleryycSgvsTj
- _$s15ManagedSettings14XPCConnectableP19invalidationHandleryycSgvsTj
- _$sSD4KeysVMn
- _$ss4Int8VN
- _objc_retain_x10
- _objc_retain_x11
CStrings:
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
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
+ "invalid Collection: less than 'count' elements in collection"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"

```
