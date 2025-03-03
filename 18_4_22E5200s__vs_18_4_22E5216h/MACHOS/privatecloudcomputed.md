## privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

```diff

-2250.18.1.0.0
-  __TEXT.__text: 0x183438
-  __TEXT.__auth_stubs: 0x37b0
-  __TEXT.__objc_methlist: 0x394
-  __TEXT.__cstring: 0x530a
-  __TEXT.__swift5_typeref: 0x3de0
-  __TEXT.__const: 0xab9e
+2250.21.0.0.0
+  __TEXT.__text: 0x188500
+  __TEXT.__auth_stubs: 0x37d0
+  __TEXT.__objc_methlist: 0x3a8
+  __TEXT.__cstring: 0x53da
+  __TEXT.__swift5_typeref: 0x3e16
+  __TEXT.__const: 0xabbe
   __TEXT.__constg_swiftt: 0x3500
-  __TEXT.__swift5_reflstr: 0x390f
-  __TEXT.__swift5_fieldmd: 0x3944
+  __TEXT.__swift5_reflstr: 0x391f
+  __TEXT.__swift5_fieldmd: 0x3950
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_types: 0x35c
   __TEXT.__swift5_assocty: 0x4f8
   __TEXT.__swift5_proto: 0x86c
-  __TEXT.__swift_as_entry: 0x3e4
-  __TEXT.__swift_as_ret: 0x478
-  __TEXT.__objc_methname: 0xa76
+  __TEXT.__swift_as_entry: 0x3e8
+  __TEXT.__swift_as_ret: 0x47c
+  __TEXT.__objc_methname: 0xa9c
   __TEXT.__oslogstring: 0x4528
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0x54
-  __TEXT.__swift5_capture: 0xb68
+  __TEXT.__swift5_capture: 0xb78
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0xe9
-  __TEXT.__unwind_info: 0x5558
-  __TEXT.__eh_frame: 0xcd98
-  __DATA_CONST.__auth_got: 0x1bd8
-  __DATA_CONST.__got: 0xd68
-  __DATA_CONST.__auth_ptr: 0xe80
+  __TEXT.__unwind_info: 0x54d0
+  __TEXT.__eh_frame: 0xcb30
+  __DATA_CONST.__auth_got: 0x1be8
+  __DATA_CONST.__got: 0xd88
+  __DATA_CONST.__auth_ptr: 0xe70
   __DATA_CONST.__const: 0x6758
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x26d0
-  __DATA.__objc_selrefs: 0x2e0
+  __DATA.__objc_const: 0x26f8
+  __DATA.__objc_selrefs: 0x2f0
   __DATA.__objc_data: 0x588
   __DATA.__data: 0x86a0
   __DATA.__bss: 0x10540

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5953
-  Symbols:   240
-  CStrings:  1116
+  Functions: 5925
+  Symbols:   243
+  CStrings:  1127
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSingleCaseWithLayoutString
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
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
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
- _swift_initEnumMetadataSingleCaseWithLayoutString
- _swift_initEnumMetadataSinglePayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "%s received headers\n%s"
+ "%s received no trailers"
+ "%s received trailers\n%s"
+ "%s request task cancelled"
+ "%s response head received: %s"
+ "%s sending headers\n%s"
+ "%s xpc.cancel received"
+ "%s xpc.close received (no-op)"
+ "%s xpc.next received callID=%ld"
+ "%s xpc.next responding callID=%ld count=%ld"
+ "%s xpc.next responding callID=%ld error=%@"
+ "%s xpc.send received data.count=%ld isComplete=%{bool}d"
+ "_attestationsUnavailable"
+ "_maxRequestLifetimeReached"
+ "_nodesOverUtilized"
+ "_requestChunkTimeout"
+ "_workloadNotFound"
+ "closeWithCompletion:"
+ "requestProxies"
+ "startTrustedRequest.Task"
+ "underlyingErrors"
- "%s Cancellation received. Cancelling task!"
- "%s Next call (callID: %ld received"
- "%s Next call (callID: %ld) failed. Error: %@"
- "%s Next call (callID: %ld) returned. Bytes: %ld"
- "%s Ropes response header: %s: %s"
- "%s Ropes response trailer: %s: %s"
- "%s headers: %s"
- "%s response head received: %s; headers: %s"
- "%s response trailers received: %s"
- "%s sending headers: %s"

```
