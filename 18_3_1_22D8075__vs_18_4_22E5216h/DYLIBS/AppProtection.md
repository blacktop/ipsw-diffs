## AppProtection

> `/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`

```diff

-35.2.5.0.0
-  __TEXT.__text: 0xa16c8
-  __TEXT.__auth_stubs: 0x1f20
+35.2.7.0.0
+  __TEXT.__text: 0x9d57c
+  __TEXT.__auth_stubs: 0x1ee0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0xf98
-  __TEXT.__const: 0x3930
+  __TEXT.__objc_methlist: 0x132c
+  __TEXT.__const: 0x4220
   __TEXT.__oslogstring: 0x3518
-  __TEXT.__cstring: 0x5004
+  __TEXT.__cstring: 0x4c24
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__swift5_typeref: 0x29bc
+  __TEXT.__swift5_typeref: 0x2984
   __TEXT.__swift5_fieldmd: 0x1b10
   __TEXT.__constg_swiftt: 0x317c
-  __TEXT.__swift5_reflstr: 0x175f
+  __TEXT.__swift5_reflstr: 0x174f
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x408
   __TEXT.__swift5_capture: 0x1514

   __TEXT.__swift5_proto: 0x2b0
   __TEXT.__swift5_types: 0x240
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x2328
-  __TEXT.__eh_frame: 0x2aa0
+  __TEXT.__unwind_info: 0x1f60
+  __TEXT.__eh_frame: 0x29c8
   __TEXT.__objc_classname: 0x273
   __TEXT.__objc_methname: 0x2201
   __TEXT.__objc_methtype: 0x6cf
   __TEXT.__objc_stubs: 0x580
-  __DATA_CONST.__got: 0x578
+  __DATA_CONST.__got: 0x580
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x990
+  __DATA_CONST.__objc_selrefs: 0xa08
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xfa0
-  __AUTH_CONST.__auth_ptr: 0x940
+  __AUTH_CONST.__auth_got: 0xf80
+  __AUTH_CONST.__auth_ptr: 0x950
   __AUTH_CONST.__const: 0x6698
   __AUTH_CONST.__cfstring: 0x5e0
-  __AUTH_CONST.__objc_const: 0x45b8
+  __AUTH_CONST.__objc_const: 0x3f90
   __AUTH.__objc_data: 0x1ad8
   __AUTH.__data: 0x1f20
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x2090
-  __DATA.__bss: 0x3dc0
-  __DATA.__common: 0xf0
+  __DATA.__data: 0x20a0
+  __DATA.__bss: 0x3dd0
+  __DATA.__common: 0xf8
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__data: 0x828
+  __DATA_DIRTY.__data: 0x7e8
   __DATA_DIRTY.__bss: 0x2f0
-  __DATA_DIRTY.__common: 0x58
+  __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3391
-  Symbols:   876
-  CStrings:  1299
+  Functions: 3186
+  Symbols:   910
+  CStrings:  1277
 
Symbols:
+ _APRErrorDomain
+ __APRErrorCodeDescription
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_getExistentialTypeMetadata
- _APErrorDomain
- __APErrorCodeDescription
- _objc_release_x10
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
- _swift_unknownObjectWeakCopyAssign
- _swift_unknownObjectWeakCopyInit
- _swift_unknownObjectWeakTakeAssign
- _swift_unknownObjectWeakTakeInit
CStrings:
+ "APRErrorDomain"
- "APErrorDomain"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Library/store.sqlite3"
- "Negative value is not representable"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
