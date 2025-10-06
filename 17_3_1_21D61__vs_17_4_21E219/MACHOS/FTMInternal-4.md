## FTMInternal-4

> `/Applications/FTMInternal-4.app/FTMInternal-4`

```diff

-34.2.0.0.0
-  __TEXT.__text: 0x1fe0e4
-  __TEXT.__auth_stubs: 0x2de0
+34.3.0.0.0
+  __TEXT.__text: 0x1ff008
+  __TEXT.__auth_stubs: 0x2e10
   __TEXT.__objc_stubs: 0x5be0
   __TEXT.__objc_methlist: 0x1a4a0
-  __TEXT.__cstring: 0x1024d
-  __TEXT.__objc_methname: 0x1e19d
+  __TEXT.__cstring: 0x1064d
+  __TEXT.__objc_methname: 0x1e1b3
   __TEXT.__objc_classname: 0xff1
   __TEXT.__objc_methtype: 0x783f
   __TEXT.__gcc_except_tab: 0x398
-  __TEXT.__const: 0x5254
+  __TEXT.__const: 0x5204
   __TEXT.__oslogstring: 0x527
   __TEXT.__constg_swiftt: 0x2cd4
-  __TEXT.__swift5_typeref: 0x92e4
+  __TEXT.__swift5_typeref: 0x8fb8
   __TEXT.__swift5_reflstr: 0x1dba
   __TEXT.__swift5_fieldmd: 0x1f2c
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x5be0
+  __TEXT.__unwind_info: 0x5bf8
   __TEXT.__eh_frame: 0xe08
-  __DATA_CONST.__auth_got: 0x1700
-  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__auth_got: 0x1718
+  __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__auth_ptr: 0x150
-  __DATA_CONST.__const: 0x8be0
+  __DATA_CONST.__const: 0x8bf8
   __DATA_CONST.__cfstring: 0xf320
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_classrefs: 0x4c0
+  __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_intobj: 0x6f0
   __DATA.__objc_const: 0x2e848
   __DATA.__objc_selrefs: 0x8f78
-  __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x4c0
-  __DATA.__objc_superrefs: 0x518
   __DATA.__objc_ivar: 0x1b68
   __DATA.__objc_data: 0x5bf0
-  __DATA.__data: 0x6b18
+  __DATA.__data: 0x6bf8
   __DATA.__bss: 0x6600
   __DATA.__common: 0x1c0
   - /AppleInternal/Library/Frameworks/CellularLogging.framework/CellularLogging

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C5BF38A8-2B14-3972-AD3E-318BC2FA9933
-  Functions: 12616
-  Symbols:   1293
-  CStrings:  11898
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 79DF8CF0-2F5E-3AFF-86BC-32AFC2841DF4
+  Functions: 12647
+  Symbols:   1298
+  CStrings:  11920
 
Symbols:
+ _$sSw10copyMemory4fromySW_tF
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyXl_Ts5
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
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
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIWindow\",?,&,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"
- "T@\"UIWindow\",&,N"

```
