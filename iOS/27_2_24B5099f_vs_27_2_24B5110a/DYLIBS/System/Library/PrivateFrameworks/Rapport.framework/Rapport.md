## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-751.200.74.0.0
-  __TEXT.__text: 0xdad58
-  __TEXT.__objc_methlist: 0xa1a8
-  __TEXT.__cstring: 0x14eac
-  __TEXT.__const: 0x41a8
-  __TEXT.__gcc_except_tab: 0x1518
-  __TEXT.__oslogstring: 0x26bd
-  __TEXT.__swift5_typeref: 0xc4f
-  __TEXT.__swift5_capture: 0x950
-  __TEXT.__swift5_fieldmd: 0xb34
-  __TEXT.__constg_swiftt: 0xdbc
-  __TEXT.__swift5_reflstr: 0x93c
-  __TEXT.__swift5_proto: 0x144
-  __TEXT.__swift5_types: 0xb0
+751.200.92.0.0
+  __TEXT.__text: 0xe0d38
+  __TEXT.__objc_methlist: 0xa2d0
+  __TEXT.__cstring: 0x14fec
+  __TEXT.__const: 0x4458
+  __TEXT.__gcc_except_tab: 0x1530
+  __TEXT.__oslogstring: 0x289d
+  __TEXT.__swift5_typeref: 0xccd
+  __TEXT.__swift5_capture: 0x958
+  __TEXT.__swift5_fieldmd: 0xc14
+  __TEXT.__constg_swiftt: 0xf08
+  __TEXT.__swift5_reflstr: 0xabc
+  __TEXT.__swift5_proto: 0x164
+  __TEXT.__swift5_types: 0xb8
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x1c
-  __TEXT.__swift5_assocty: 0x88
-  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_assocty: 0x100
+  __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3c00
+  __TEXT.__unwind_info: 0x3d08
   __TEXT.__eh_frame: 0x960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x28d8
+  __DATA_CONST.__const: 0x2960
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4610
+  __DATA_CONST.__objc_selrefs: 0x46d0
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x4e8
-  __AUTH_CONST.__const: 0x27c0
-  __AUTH_CONST.__cfstring: 0x5f40
-  __AUTH_CONST.__objc_const: 0x11678
+  __DATA_CONST.__got: 0x4f0
+  __AUTH_CONST.__const: 0x2940
+  __AUTH_CONST.__cfstring: 0x5fc0
+  __AUTH_CONST.__objc_const: 0x11808
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1190
+  __AUTH_CONST.__auth_got: 0x11b0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x111c
-  __DATA.__data: 0x678
+  __DATA.__objc_ivar: 0x1124
+  __DATA.__data: 0x6e8
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x2618
+  __DATA_DIRTY.__objc_data: 0x2768
   __DATA_DIRTY.__data: 0x2660
   __DATA_DIRTY.__bss: 0xd8
   __DATA_DIRTY.__common: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5843
-  Symbols:   6872
-  CStrings:  3073
+  Functions: 5948
+  Symbols:   6913
+  CStrings:  3093
 
Symbols:
+ -[RPCompanionLinkDevice updateMultiUserDeviceWithPeer:]
+ -[RPConnection _accountOwnerCheckEnabled]
+ -[RPConnection _isAccountCheckedWithPeerModel:]
+ -[RPConnection _localDeviceClass]
+ -[RPConnection _multiUserDeviceWithIdentifier:]
+ -[RPConnection _peerUpdatedAfterTrustChange:]
+ -[RPConnection _sourceVersionFromString:]
+ -[RPConnection accountOwnerCheckApplies]
+ -[RPConnection localAccountUpdated]
+ -[RPConnection multiUserDevices]
+ -[RPConnection setMultiUserDevices:]
+ -[RPConnection verifyIdentityProof:accountAltDSID:]
+ -[RPConnection verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:]
+ -[RPSiriSession setTriggeredPhrase:]
+ -[RPSiriSession triggeredPhrase]
+ GCC_except_table291
+ GCC_except_table72
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table95
+ _OBJC_IVAR_$_RPConnection._multiUserDevices
+ _OBJC_IVAR_$_RPSiriSession._triggeredPhrase
+ _RPLinkIsAccountChecked
+ _RPOptionMultiUserDeviceID
+ _TextToSourceVersion
+ ___82-[RPConnection verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:]_block_invoke
+ ___82-[RPConnection verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:]_block_invoke_2
+ ___block_descriptor_65_e8_32s40s48bs56r_e25_v20?0B8"CUPairedPeer"12ls32l8s40l8r56l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e23_v20?0B8"RPIdentity"12ls32l8s40l8s48l8s56l8s64l8r80l8s72l8
+ ___swift_closure_destructor.115Tm
+ ___swift_closure_destructor.144Tm
+ ___swift_closure_destructor.156Tm
+ ___swift_closure_destructor.188Tm
+ ___swift_closure_destructor.255Tm
+ __sepBackedIdentityEnabled.enabled
+ _associated conformance 7Rapport16RPConnectionCoreC17AccountOwnerCheckOSHAASQ
+ _associated conformance So21RPAccountOwnerSourcesVs10SetAlgebraSCSQ
+ _associated conformance So21RPAccountOwnerSourcesVs10SetAlgebraSCs25ExpressibleByArrayLiteral
+ _associated conformance So21RPAccountOwnerSourcesVs9OptionSetSCSY
+ _associated conformance So21RPAccountOwnerSourcesVs9OptionSetSCs0E7Algebra
+ _swift_bridgeObjectRetain_n
+ _symbolic $ss10SetAlgebraP
+ _symbolic $ss25ExpressibleByArrayLiteralP
+ _symbolic $ss9OptionSetP
+ _symbolic _____ 7Rapport16RPConnectionCoreC17AccountOwnerCheckO
+ _symbolic _____ So21RPAccountOwnerSourcesV
+ _symbolic _____Sg 7Rapport16RPConnectionCoreC17AccountOwnerCheckO
+ _type_layout_string So21RPAccountOwnerSourcesV
- GCC_except_table73
- GCC_except_table92
- ___swift_closure_destructor.113Tm
- ___swift_closure_destructor.142Tm
- ___swift_closure_destructor.154Tm
- ___swift_closure_destructor.186Tm
- ___swift_closure_destructor.253Tm
CStrings:
+ "### Account owner removed: peer reports another account, ours %{private,mask.hash}s, peer %{private,mask.hash}s, sources 0x%{public}s, model %{public}s, %{public}s"
+ "### Failed to obtain local account for multi-user HK verify\n"
+ "-[RPConnection verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:]"
+ "Account owner kept: %{public}s, sources 0x%{public}s, model %{public}s, %{public}s"
+ "Account owner not checked: disabled, %{public}s"
+ "Account owner withheld: %{public}s, ours %{private,mask.hash}s, sources 0x%{public}s, model %{public}s, %{public}s"
+ "AccountOwnerCheck"
+ "SEPBackedIdentity"
+ "Send AltDSID update: %{public}s"
+ "_vtPhrase"
+ "disabled"
+ "exemptLink"
+ "iCrowd"
+ "legacyPeer"
+ "localUnknown"
+ "match"
+ "mismatch"
+ "missingFlag.MultiUser"
+ "multiUserDevID"
+ "peerUnknown"
```
