## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-107.0.0.0.0
-  __TEXT.__text: 0x646f0
+108.1.0.0.0
+  __TEXT.__text: 0x6517c
   __TEXT.__auth_stubs: 0x1580
   __TEXT.__objc_methlist: 0x654
   __TEXT.__const: 0x2cd0
   __TEXT.__cstring: 0x56d8
-  __TEXT.__oslogstring: 0x335a
-  __TEXT.__gcc_except_tab: 0x694
+  __TEXT.__oslogstring: 0x33ba
+  __TEXT.__gcc_except_tab: 0x730
   __TEXT.__swift5_typeref: 0x9de
   __TEXT.__swift5_reflstr: 0xdf3
   __TEXT.__swift5_assocty: 0x1b0

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x23c
-  __TEXT.__unwind_info: 0xe68
+  __TEXT.__unwind_info: 0xe78
   __TEXT.__eh_frame: 0xba0
   __TEXT.__objc_classname: 0xd0
   __TEXT.__objc_methname: 0x11dc

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0xad0
-  __AUTH_CONST.__auth_ptr: 0x4a8
+  __AUTH_CONST.__auth_ptr: 0x4b0
   __AUTH_CONST.__const: 0x23a0
   __AUTH_CONST.__cfstring: 0x19a0
   __AUTH_CONST.__objc_const: 0x1668

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1279
-  Symbols:   754
-  CStrings:  1058
+  Functions: 1281
+  Symbols:   760
+  CStrings:  1060
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "%25s:%-5d Invalid blob to sign. { blob=%@ }"
+ "%25s:%-5d Signed data blob. { keyId=%@ }"
+ "AppAttest (%@-108.1) - %@"
+ "Failed to sign data. { error=%@ }"
+ "Sign"
- "AppAttest (%@-107) - %@"
- "AppAttest_AppAttestation_Sign"
- "Not supported."

```
