## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2775.0.0.0.0
-  __TEXT.__text: 0x49def8
+2777.1.0.0.0
+  __TEXT.__text: 0x49e428
   __TEXT.__init_offsets: 0x1a8
   __TEXT.__objc_methlist: 0x74c
   __TEXT.__const: 0x1f9ec
-  __TEXT.__gcc_except_tab: 0x41f08
-  __TEXT.__cstring: 0x14101
-  __TEXT.__oslogstring: 0x4ccb8
-  __TEXT.__unwind_info: 0x19900
+  __TEXT.__gcc_except_tab: 0x41f6c
+  __TEXT.__cstring: 0x1413f
+  __TEXT.__oslogstring: 0x4ccfb
+  __TEXT.__unwind_info: 0x19918
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d78
+  __DATA_CONST.__const: 0x3da0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__objc_const: 0xb80
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0x16b0
+  __AUTH_CONST.__auth_got: 0x16c0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x2c8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 16439
-  Symbols:   24907
-  CStrings:  8706
+  Functions: 16441
+  Symbols:   24912
+  CStrings:  8709
 
Symbols:
+ __ZN22IMSSecurityAssociation15createTemporaryEb
+ __ZNSt3__19to_stringEx
+ ___block_descriptor_72_ea8_32s40s48s56r_e22_v16?0"NSDictionary"8lr56l8s32l8s40l8s48l8
+ _kSymptomDiagnosticErrorRandomizedSuppression
+ _objc_retain_x25
Functions:
~ __ZN16SipLazuliManager4sendERK16LazuliSendParamsRK6SipUri : 3596 -> 3620
~ ____ZN24AttestationServiceHelper4signEPKhmRKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS2_10shared_ptrI8SipStackEENS2_8functionIFvS8_jEEE_block_invoke : 1272 -> 1732
+ __ZN22IMSSecurityAssociation15createTemporaryEb
~ __ZN26IMSSecurityAssociationPair15createTemporaryERKNSt3__110shared_ptrI9IpAddressEES5_RKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEj : 1572 -> 516
~ __ZN26IMSSecurityAssociationPair6updateERKNSt3__110shared_ptrI9IpAddressEES5_PK29SipIPSec3gppSecurityMechanismPA16_KhSB_j : 3288 -> 3396
~ __ZN10SipSession28handleInviteOrUpdateResponseENSt3__110shared_ptrIK11SipResponseEENS1_I20SipClientTransactionEE : 11524 -> 11536
~ __ZN21SipRegistrationClient27captureAbcRcsPushRegFailureEv : 1064 -> 1080
~ __ZN3abc8snapshotERKNS_6ParamsE : 1124 -> 1216
~ ____ZN3abc8snapshotERKNS_6ParamsE_block_invoke : 440 -> 688
+ ____ZN3abc8snapshotERKNS_6ParamsE_block_invoke.6
~ __ZN15SipStackManager22createNewLazuliSessionENSt3__110shared_ptrI8SipStackEERK6SipUri20LazuliSessionOptionsP9ImsResult : 1508 -> 1524
CStrings:
+ "#E %{private, mask.hash}sMessage size %llu exceeds MessageMaxSize %llu (compressed=%{BOOL}d)"
+ "AttestationServiceSigningFailure"
+ "error="
+ "retry abc to defeat randomized suppression"
- "#E %{private, mask.hash}sMessage size %llu exceeds MessageMaxSize %u"
```
