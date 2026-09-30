## MessagesCloudSync

> `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-1402.500.128.2.2
-  __TEXT.__text: 0xe048c
-  __TEXT.__auth_stubs: 0x1ef0
-  __TEXT.__objc_methlist: 0xb28
-  __TEXT.__const: 0x82d0
-  __TEXT.__cstring: 0x46e1
+1402.500.164.2.1
+  __TEXT.__text: 0xf2558
+  __TEXT.__auth_stubs: 0x1f10
+  __TEXT.__objc_methlist: 0xb40
+  __TEXT.__const: 0x82c0
+  __TEXT.__cstring: 0x4741
   __TEXT.__constg_swiftt: 0x2b28
   __TEXT.__swift5_typeref: 0x2680
   __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0x2b0a
-  __TEXT.__swift5_fieldmd: 0x3138
+  __TEXT.__swift5_reflstr: 0x2b3a
+  __TEXT.__swift5_fieldmd: 0x3144
   __TEXT.__swift5_assocty: 0x5a0
-  __TEXT.__oslogstring: 0x4a94
+  __TEXT.__oslogstring: 0x4b94
   __TEXT.__swift5_proto: 0x724
   __TEXT.__swift5_types: 0x2d0
-  __TEXT.__swift5_capture: 0xe10
+  __TEXT.__swift5_capture: 0xe20
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0x8c
-  __TEXT.__swift_as_entry: 0x3f8
-  __TEXT.__swift_as_ret: 0x478
-  __TEXT.__unwind_info: 0x34b0
-  __TEXT.__eh_frame: 0x935c
+  __TEXT.__swift_as_entry: 0x404
+  __TEXT.__swift_as_ret: 0x484
+  __TEXT.__unwind_info: 0x3628
+  __TEXT.__eh_frame: 0x9d0c
   __TEXT.__objc_classname: 0x195
-  __TEXT.__objc_methname: 0x2876
-  __TEXT.__objc_methtype: 0x55f
+  __TEXT.__objc_methname: 0x28a8
+  __TEXT.__objc_methtype: 0x58a
   __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x790
+  __DATA_CONST.__got: 0x798
   __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe20
+  __DATA_CONST.__objc_selrefs: 0xe30
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf80
-  __AUTH_CONST.__auth_ptr: 0xad0
-  __AUTH_CONST.__const: 0x86b0
+  __AUTH_CONST.__auth_got: 0xf90
+  __AUTH_CONST.__auth_ptr: 0xb48
+  __AUTH_CONST.__const: 0x86d8
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x24c8
+  __AUTH_CONST.__objc_const: 0x2510
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x578
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x1920
+  __DATA.__data: 0x1950
   __DATA.__bss: 0x90f0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x588
-  __DATA_DIRTY.__data: 0x25f0
+  __DATA_DIRTY.__objc_data: 0x590
+  __DATA_DIRTY.__data: 0x25c0
   __DATA_DIRTY.__bss: 0x3680
   __DATA_DIRTY.__common: 0x268
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3667
+  Functions: 3725
   Symbols:   414
-  CStrings:  1492
+  CStrings:  1501
 
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
+ "@\"NSDate\"24@0:8@\"NSString\"16"
+ "Account status update, attempting to resume after bad account status."
+ "Error restarting sync backfillSync due to no completed sync, processing error: "
+ "Failed to restart sync phase backfillSync due to no completed sync, error: %@"
+ "Identity status update, attempting to resume after bad identity status."
+ "No last full sync date, starting backfill sync"
+ "Scheduling periodic sync with %s, lastSyncDate %s"
+ "Tried to resume syncing, but we're already syncing"
+ "initWithDelegate:syncStateManager:"
+ "lastFullSyncDate"
+ "syncDateForKey:"
- "Account status update, and we stopped syncing due to bad account status."
- "Identity status update, and we stopped syncing due to bad identity status."
- "initWithDelegate:"

```
