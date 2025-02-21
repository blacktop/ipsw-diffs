## nptocompaniond

> `/usr/libexec/nptocompaniond`

```diff

-2022.400.1.0.0
-  __TEXT.__text: 0x6bf3c
-  __TEXT.__auth_stubs: 0x1c60
+2022.500.2.0.0
+  __TEXT.__text: 0x64e00
+  __TEXT.__auth_stubs: 0x1c30
   __TEXT.__objc_stubs: 0x40a0
-  __TEXT.__objc_methlist: 0x215c
-  __TEXT.__const: 0x1d80
+  __TEXT.__objc_methlist: 0x25a4
+  __TEXT.__const: 0x1ea0
   __TEXT.__objc_methname: 0x51cf
-  __TEXT.__cstring: 0x309e
-  __TEXT.__swift5_typeref: 0xd4a
+  __TEXT.__cstring: 0x2dbe
+  __TEXT.__swift5_typeref: 0xd9a
   __TEXT.__constg_swiftt: 0xcac
   __TEXT.__swift5_reflstr: 0xa90
   __TEXT.__swift5_fieldmd: 0xa24

   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_proto: 0x178
   __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift_as_entry: 0x108
+  __TEXT.__swift_as_ret: 0x130
   __TEXT.__swift5_assocty: 0xf8
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x298
-  __TEXT.__unwind_info: 0x1ae0
-  __TEXT.__eh_frame: 0x2548
-  __DATA_CONST.__auth_got: 0xe40
-  __DATA_CONST.__got: 0x660
-  __DATA_CONST.__auth_ptr: 0x3e8
-  __DATA_CONST.__const: 0x2220
+  __TEXT.__unwind_info: 0x1a00
+  __TEXT.__eh_frame: 0x2610
+  __DATA_CONST.__auth_got: 0xe28
+  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__auth_ptr: 0x3e0
+  __DATA_CONST.__const: 0x2248
   __DATA_CONST.__cfstring: 0x1240
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x60

   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x5908
-  __DATA.__objc_selrefs: 0x1440
+  __DATA.__objc_const: 0x5158
+  __DATA.__objc_selrefs: 0x1578
   __DATA.__objc_ivar: 0x304
   __DATA.__objc_data: 0x17e0
-  __DATA.__data: 0x1c90
+  __DATA.__data: 0x1cf0
   __DATA.__bss: 0x2a40
   __DATA.__common: 0x188
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2256
-  Symbols:   785
-  CStrings:  1752
+  Functions: 2168
+  Symbols:   790
+  CStrings:  1736
 
Symbols:
+ _$sSaMa
+ _$ss5Int32VN
+ _$ss5Int64VN
+ __swift_FORCE_LOAD_$_swiftCompression
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_initStructMetadataWithLayoutString
- _$sBbWV
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
