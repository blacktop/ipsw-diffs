## CloudAttestation

> `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`

```diff

-199.100.10.0.4
-  __TEXT.__text: 0xf8cd8
-  __TEXT.__auth_stubs: 0x2590
+199.100.24.0.1
+  __TEXT.__text: 0x10ac40
+  __TEXT.__auth_stubs: 0x25a0
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0xb91e
-  __TEXT.__cstring: 0x2554
-  __TEXT.__constg_swiftt: 0x2894
-  __TEXT.__swift5_typeref: 0x25dc
-  __TEXT.__swift5_fieldmd: 0x3174
-  __TEXT.__swift5_proto: 0x9c8
-  __TEXT.__swift5_types: 0x3bc
-  __TEXT.__oslogstring: 0x2288
-  __TEXT.__swift5_reflstr: 0x28a3
-  __TEXT.__swift_as_entry: 0x224
-  __TEXT.__swift_as_ret: 0x1e0
-  __TEXT.__swift5_capture: 0x158
-  __TEXT.__swift5_assocty: 0x508
-  __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_mpenum: 0x94
+  __TEXT.__const: 0xbd4e
+  __TEXT.__cstring: 0x25b4
+  __TEXT.__constg_swiftt: 0x2960
+  __TEXT.__swift5_typeref: 0x25fe
+  __TEXT.__swift5_fieldmd: 0x327c
+  __TEXT.__swift5_proto: 0xa04
+  __TEXT.__swift5_types: 0x3d4
+  __TEXT.__oslogstring: 0x2468
+  __TEXT.__swift5_reflstr: 0x2993
+  __TEXT.__swift_as_entry: 0x270
+  __TEXT.__swift_as_ret: 0x22c
+  __TEXT.__swift5_capture: 0x16c
+  __TEXT.__swift5_assocty: 0x558
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_mpenum: 0xa4
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x42e0
-  __TEXT.__eh_frame: 0x81d8
+  __TEXT.__unwind_info: 0x44f0
+  __TEXT.__eh_frame: 0x8aa8
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methname: 0x3b5
   __TEXT.__objc_methtype: 0x16c
-  __DATA_CONST.__got: 0x5b0
-  __DATA_CONST.__const: 0x430
+  __DATA_CONST.__got: 0x6d8
+  __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0x12c8
-  __AUTH_CONST.__auth_ptr: 0xc28
-  __AUTH_CONST.__const: 0x5a30
+  __AUTH_CONST.__auth_got: 0x12d0
+  __AUTH_CONST.__auth_ptr: 0xa80
+  __AUTH_CONST.__const: 0x5e00
   __AUTH_CONST.__objc_const: 0x658
   __AUTH.__objc_data: 0x1b0
-  __AUTH.__data: 0x1de8
-  __DATA.__data: 0x29d8
-  __DATA.__bss: 0xff80
-  __DATA.__common: 0x208
+  __AUTH.__data: 0x1db8
+  __DATA.__data: 0x2b08
+  __DATA.__bss: 0x10700
+  __DATA.__common: 0x220
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x1ea8
+  __DATA_DIRTY.__data: 0x1eb0
   __DATA_DIRTY.__common: 0x158
   __DATA_DIRTY.__bss: 0x2400
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5543
+  Functions: 5678
   Symbols:   350
-  CStrings:  531
+  CStrings:  541
 
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
- _objc_release_x9
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
+ "%s is covered by proxy node attestation"
+ "AttestationBundle passed ProxiedReleaseTransparencyPolicy: All proxied releases are included in transparency log"
+ "Bundle AppData failed integrity check: (digest:%{public}s != nonce:%{public}s"
+ "Bundle AppData is non-empty, but attestation contains no nonce"
+ "Empty proxied releases, production clients will reject this proxy node attestation"
+ "Nonce %s does not match %s"
+ "Proxy is not providing proxied releases"
+ "Release %{public}s has expired in transparency log"
+ "Software %{public}s has expired in transparency log"
+ "app data integrity check failed: (nonce:%{public}s != digest:%{public}s"
+ "com.apple.CloudAttestation.AutoValidator"
+ "com.apple.CloudAttestaton.MuxValidator"
+ "missing nonce from validated attestation"
+ "missing validated attestation"
- "%s is covered by proxy attestation"
- "AttestationBundle passed ProxiedReleaseTransparencyPolicy: All proxied releases are included in the transparency log"
- "Release %{public}s has expired in the transparency log"
- "Software %{public}s has expired in the transparency log"

```
