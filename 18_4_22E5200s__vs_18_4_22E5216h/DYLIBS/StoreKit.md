## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-814.4.17.0.0
-  __TEXT.__text: 0x154f68
+814.4.21.0.0
+  __TEXT.__text: 0x15a3b0
   __TEXT.__auth_stubs: 0x2df0
-  __TEXT.__objc_methlist: 0x5a3c
+  __TEXT.__objc_methlist: 0x5a0c
   __TEXT.__gcc_except_tab: 0xfec
-  __TEXT.__const: 0xb9f4
-  __TEXT.__oslogstring: 0x3340
-  __TEXT.__cstring: 0x6f27
+  __TEXT.__const: 0xbd64
+  __TEXT.__oslogstring: 0x32d0
+  __TEXT.__cstring: 0x6f07
   __TEXT.__dlopen_cstrs: 0x43f
-  __TEXT.__constg_swiftt: 0x27f8
-  __TEXT.__swift5_typeref: 0x3698
+  __TEXT.__constg_swiftt: 0x2820
+  __TEXT.__swift5_typeref: 0x36ce
   __TEXT.__swift5_reflstr: 0x2504
-  __TEXT.__swift5_fieldmd: 0x3400
-  __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_assocty: 0x800
-  __TEXT.__swift5_proto: 0xb08
-  __TEXT.__swift5_types: 0x3d8
-  __TEXT.__swift5_capture: 0x197c
+  __TEXT.__swift5_fieldmd: 0x3440
+  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__swift5_assocty: 0x848
+  __TEXT.__swift5_proto: 0xb38
+  __TEXT.__swift5_types: 0x3e0
+  __TEXT.__swift5_capture: 0x1938
   __TEXT.__swift_as_entry: 0x3cc
-  __TEXT.__swift_as_ret: 0x3c4
-  __TEXT.__swift5_mpenum: 0x38
+  __TEXT.__swift_as_ret: 0x3b4
+  __TEXT.__swift5_mpenum: 0x40
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0x66a8
-  __TEXT.__eh_frame: 0xa0c0
+  __TEXT.__unwind_info: 0x6710
+  __TEXT.__eh_frame: 0xa400
   __TEXT.__objc_classname: 0x12ef
   __TEXT.__objc_methname: 0xc92e
   __TEXT.__objc_methtype: 0x2d6b
   __TEXT.__objc_stubs: 0x7de0
   __DATA_CONST.__got: 0xb18
   __DATA_CONST.__const: 0x1820
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x1708
-  __AUTH_CONST.__auth_ptr: 0xcf8
-  __AUTH_CONST.__const: 0xc650
-  __AUTH_CONST.__cfstring: 0x3780
-  __AUTH_CONST.__objc_const: 0x13768
+  __AUTH_CONST.__auth_ptr: 0xd60
+  __AUTH_CONST.__const: 0xc710
+  __AUTH_CONST.__cfstring: 0x37a0
+  __AUTH_CONST.__objc_const: 0x133c0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x22f8
-  __AUTH.__data: 0x1cd8
+  __AUTH.__objc_data: 0x2238
+  __AUTH.__data: 0x1cb0
   __DATA.__objc_ivar: 0x5c0
-  __DATA.__data: 0x5498
-  __DATA.__bss: 0x14560
+  __DATA.__data: 0x54c8
+  __DATA.__bss: 0x14b60
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x738

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10213
-  Symbols:   5380
-  CStrings:  3820
+  Functions: 10310
+  Symbols:   5456
+  CStrings:  3817
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initEnumMetadataSinglePayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "21:26:56"
+ "Failed to get XPC remote object to enumerate statuses for %{public}s"
+ "Feb 21 2025"
+ "IterationType.groupID("
+ "IterationType.transactionID("
- "12:32:03"
- "Failed in XPC to get status for %{public}llu: %{public}@"
- "Failed to get XPC remote object to get status for %{public}llu"
- "Failed to get XPC remote object to get status for %{public}s"
- "Feb 16 2025"
- "StoreKit.LocalStatusReceiver"
- "_TtC8StoreKit19LocalStatusReceiver"
- "closure"

```
