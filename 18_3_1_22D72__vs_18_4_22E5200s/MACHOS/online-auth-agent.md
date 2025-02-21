## online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

-436.40.5.0.0
-  __TEXT.__text: 0x3b120
-  __TEXT.__auth_stubs: 0x1d00
+436.100.18.0.0
+  __TEXT.__text: 0x33dbc
+  __TEXT.__auth_stubs: 0x1ca0
   __TEXT.__objc_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x258
-  __TEXT.__const: 0x1b1c
+  __TEXT.__objc_methlist: 0x38c
+  __TEXT.__const: 0x1ebc
   __TEXT.__gcc_except_tab: 0x3ec
-  __TEXT.__cstring: 0x34fe
+  __TEXT.__cstring: 0x3278
   __TEXT.__objc_methname: 0x1163
-  __TEXT.__oslogstring: 0x1fce
+  __TEXT.__oslogstring: 0x1fee
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methtype: 0x212
   __TEXT.__dlopen_cstrs: 0x12c
   __TEXT.__constg_swiftt: 0xb7c
-  __TEXT.__swift5_typeref: 0x7ff
+  __TEXT.__swift5_typeref: 0x7f7
   __TEXT.__swift5_reflstr: 0x6f5
   __TEXT.__swift5_fieldmd: 0x984
   __TEXT.__swift5_types: 0xe8

   __TEXT.__swift5_proto: 0x148
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__unwind_info: 0xf90
-  __TEXT.__eh_frame: 0x1268
-  __DATA_CONST.__auth_got: 0xe90
-  __DATA_CONST.__got: 0x4b0
+  __TEXT.__unwind_info: 0xdf0
+  __TEXT.__eh_frame: 0x1310
+  __DATA_CONST.__auth_got: 0xe60
+  __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x470
-  __DATA_CONST.__const: 0x22b0
+  __DATA_CONST.__const: 0x22c0
   __DATA_CONST.__cfstring: 0xc80
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0xf98
-  __DATA.__objc_selrefs: 0x5f8
+  __DATA.__objc_const: 0xd58
+  __DATA.__objc_selrefs: 0x698
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x1610
-  __DATA.__bss: 0x2650
-  __DATA.__common: 0xc0
+  __DATA.__data: 0x1618
+  __DATA.__bss: 0x2660
+  __DATA.__common: 0xf8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1280
-  Symbols:   423
-  CStrings:  866
+  Functions: 1147
+  Symbols:   431
+  CStrings:  853
 
Symbols:
+ _CFStringCreateWithCString
+ _os_parse_boot_arg_string
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- _objc_retain_x9
- _swift_arrayDestroy
- _swift_getEnumCaseMultiPayload
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "4a20c45a-2a99-4ad8-bdd2-c7ab4b0c1a8d"
+ "Using emulated device UDID: %@\n"
+ "amfi_emulate_device_udid"
+ "bee84af7-d2ca-44e9-992b-54db447d20fc"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
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
