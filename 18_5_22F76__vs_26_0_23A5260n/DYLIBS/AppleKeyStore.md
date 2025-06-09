## AppleKeyStore

> `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`

```diff

-1827.120.2.0.0
-  __TEXT.__text: 0x47e74
-  __TEXT.__auth_stubs: 0x1480
-  __TEXT.__cstring: 0x3283
-  __TEXT.__const: 0x4541
-  __TEXT.__oslogstring: 0xd3
-  __TEXT.__constg_swiftt: 0x4fc
-  __TEXT.__swift5_typeref: 0x2c4
-  __TEXT.__swift5_reflstr: 0x739
-  __TEXT.__swift5_fieldmd: 0x8b4
-  __TEXT.__swift5_types: 0x54
+2155.0.5.502.2
+  __TEXT.__text: 0x571e8
+  __TEXT.__auth_stubs: 0x16b0
+  __TEXT.__const: 0xa4f0
+  __TEXT.__cstring: 0x2f43
+  __TEXT.__oslogstring: 0xf71
+  __TEXT.__dlopen_cstrs: 0x56
+  __TEXT.__constg_swiftt: 0x730
+  __TEXT.__swift5_typeref: 0x6b8
+  __TEXT.__swift5_reflstr: 0x83d
+  __TEXT.__swift5_fieldmd: 0xdb0
+  __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x100
+  __TEXT.__swift5_proto: 0x2ec
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__swift5_assocty: 0x168
-  __TEXT.__unwind_info: 0xf60
-  __TEXT.__eh_frame: 0x1390
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x3bd0
+  __TEXT.__swift5_assocty: 0x3d8
+  __TEXT.__unwind_info: 0x1500
+  __TEXT.__eh_frame: 0x18e8
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x5c10
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0xa40
-  __AUTH_CONST.__const: 0xaa8
-  __AUTH_CONST.__cfstring: 0x500
+  __AUTH_CONST.__auth_got: 0xb58
+  __AUTH_CONST.__const: 0x1cc8
+  __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x268
   __AUTH.__data: 0x480
-  __DATA.__data: 0xeb0
-  __DATA.__bss: 0x1d70
-  __DATA.__common: 0x7e0
+  __DATA.__data: 0x1358
+  __DATA.__common: 0x8a0
+  __DATA.__bss: 0x5b10
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SwiftASN1Internal.framework/SwiftASN1Internal
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: ABFC7BD0-A855-3669-86E4-ED8A86FC6107
-  Functions: 1747
-  Symbols:   2955
-  CStrings:  649
+  UUID: DC3E21F7-C424-3923-BE9A-671EA4FE3F16
+  Functions: 2520
+  Symbols:   3664
+  CStrings:  723
 
Symbols:
+ _ACRTRoot_public_key
+ _AKSIdentityAdd
+ _AKSIdentityAddPersonaWithACM
+ _AKSIdentityAuthenticate
+ _AKSIdentityAuthenticateOnVolume
+ _AKSIdentityChangePasscodeForUuid
+ _AKSIdentityChangePasscodeWithACM
+ _AKSIdentityCreateFirstWithACM
+ _AKSIdentityCreateRecovery
+ _AKSIdentityCreateWithACM
+ _AKSIdentityDeleteRecovery
+ _AKSIdentityExists
+ _AKSIdentityExistsOnVolume
+ _AKSIdentityListForVolume
+ _AKSIdentityListRecoveryUsers
+ _AKSIdentityListRecoveryUsersForVolume
+ _AKSIdentityLoginWithACMCred
+ _AKSIdentityLoginWithACMCredOnVolume
+ _AKSIdentityNew
+ _AKSIdentityPolicyStatus
+ _AKSIdentityRecover
+ _AKSIdentityRecoverOnVolume
+ _AKSIdentityResetAllOnVolume
+ _AKSIdentityResetOnVolume
+ _AKSIdentitySetPrimaryWithACM
+ _AKSIdentityTransferOwnership
+ _AKSIdentityTransferPrimaryWithACM
+ _AKSIdentityUnlockInternal.cold.2
+ _AKSIdentityUnlockInternal.cold.3
+ _AKSIdentityUnlockInternal.cold.4
+ _AKSIdentityUnlockInternal.cold.5
+ _AKSIdentityUnlockSessionWithACMCred
+ _AKSIdentityUnlockWithACMCred
+ _AKSIdentityVerifyPasscode
+ _AKSIdentityVerifyPasscodeOnVolume
+ _AKSIdentityVolumeOwnership
+ _ApplePlatformBackportECCRootCAG1
+ _ApplePlatformBackportECCRootCAG1PublicKey
+ _ApplePlatformBackportECCRootCAG1SKID
+ _ApplePlatformBackportECCRootCAG1SPKI
+ _ApplePlatformBackportECCRootCAG1_public_key
+ _ApplePlatformBackportECCRootCAG1_skid
+ _ApplePlatformBackportECCRootCAG1_spki
+ _ApplePlatformBackportRSARootCAG1
+ _ApplePlatformBackportRSARootCAG1PublicKey
+ _ApplePlatformBackportRSARootCAG1SKID
+ _ApplePlatformBackportRSARootCAG1SPKI
+ _ApplePlatformBackportRSARootCAG1_public_key
+ _ApplePlatformBackportRSARootCAG1_skid
+ _ApplePlatformBackportRSARootCAG1_spki
+ _ApplePlatformBootstrapECCRootCAG1
+ _ApplePlatformBootstrapECCRootCAG1PublicKey
+ _ApplePlatformBootstrapECCRootCAG1SKID
+ _ApplePlatformBootstrapECCRootCAG1SPKI
+ _ApplePlatformBootstrapECCRootCAG1_public_key
+ _ApplePlatformBootstrapECCRootCAG1_skid
+ _ApplePlatformBootstrapECCRootCAG1_spki
+ _ApplePlatformCodeSigningECCRootCAG1
+ _ApplePlatformCodeSigningECCRootCAG1PublicKey
+ _ApplePlatformCodeSigningECCRootCAG1SKID
+ _ApplePlatformCodeSigningECCRootCAG1SPKI
+ _ApplePlatformCodeSigningECCRootCAG1_public_key
+ _ApplePlatformCodeSigningECCRootCAG1_skid
+ _ApplePlatformCodeSigningECCRootCAG1_spki
+ _ApplePlatformCodeSigningRSARootCAG1
+ _ApplePlatformCodeSigningRSARootCAG1PublicKey
+ _ApplePlatformCodeSigningRSARootCAG1SKID
+ _ApplePlatformCodeSigningRSARootCAG1SPKI
+ _ApplePlatformCodeSigningRSARootCAG1_public_key
+ _ApplePlatformCodeSigningRSARootCAG1_skid
+ _ApplePlatformCodeSigningRSARootCAG1_spki
+ _ApplePlatformDeveloperECCRootCAG1
+ _ApplePlatformDeveloperECCRootCAG1PublicKey
+ _ApplePlatformDeveloperECCRootCAG1SKID
+ _ApplePlatformDeveloperECCRootCAG1SPKI
+ _ApplePlatformDeveloperECCRootCAG1_public_key
+ _ApplePlatformDeveloperECCRootCAG1_skid
+ _ApplePlatformDeveloperECCRootCAG1_spki
+ _ApplePlatformDeveloperRSARootCAG1
+ _ApplePlatformDeveloperRSARootCAG1PublicKey
+ _ApplePlatformDeveloperRSARootCAG1SKID
+ _ApplePlatformDeveloperRSARootCAG1SPKI
+ _ApplePlatformDeveloperRSARootCAG1_public_key
+ _ApplePlatformDeveloperRSARootCAG1_skid
+ _ApplePlatformDeveloperRSARootCAG1_spki
+ _ApplePlatformECCRootCAG1
+ _ApplePlatformECCRootCAG1PublicKey
+ _ApplePlatformECCRootCAG1SKID
+ _ApplePlatformECCRootCAG1SPKI
+ _ApplePlatformECCRootCAG1_public_key
+ _ApplePlatformECCRootCAG1_skid
+ _ApplePlatformECCRootCAG1_spki
+ _ApplePlatformMultipurposeECCRootCAG1
+ _ApplePlatformMultipurposeECCRootCAG1PublicKey
+ _ApplePlatformMultipurposeECCRootCAG1SKID
+ _ApplePlatformMultipurposeECCRootCAG1SPKI
+ _ApplePlatformMultipurposeECCRootCAG1_public_key
+ _ApplePlatformMultipurposeECCRootCAG1_skid
+ _ApplePlatformMultipurposeECCRootCAG1_spki
+ _ApplePlatformMultipurposeRSARootCAG1
+ _ApplePlatformMultipurposeRSARootCAG1PublicKey
+ _ApplePlatformMultipurposeRSARootCAG1SKID
+ _ApplePlatformMultipurposeRSARootCAG1SPKI
+ _ApplePlatformMultipurposeRSARootCAG1_public_key
+ _ApplePlatformMultipurposeRSARootCAG1_skid
+ _ApplePlatformMultipurposeRSARootCAG1_spki
+ _ApplePlatformRSARootCAG1
+ _ApplePlatformRSARootCAG1PublicKey
+ _ApplePlatformRSARootCAG1SKID
+ _ApplePlatformRSARootCAG1SPKI
+ _ApplePlatformRSARootCAG1_public_key
+ _ApplePlatformRSARootCAG1_skid
+ _ApplePlatformRSARootCAG1_spki
+ _ApplePlatformTLSECCRootCAG1
+ _ApplePlatformTLSECCRootCAG1PublicKey
+ _ApplePlatformTLSECCRootCAG1SKID
+ _ApplePlatformTLSECCRootCAG1SPKI
+ _ApplePlatformTLSECCRootCAG1_public_key
+ _ApplePlatformTLSECCRootCAG1_skid
+ _ApplePlatformTLSECCRootCAG1_spki
+ _ApplePlatformTLSRSARootCAG1
+ _ApplePlatformTLSRSARootCAG1PublicKey
+ _ApplePlatformTLSRSARootCAG1SKID
+ _ApplePlatformTLSRSARootCAG1SPKI
+ _ApplePlatformTLSRSARootCAG1_public_key
+ _ApplePlatformTLSRSARootCAG1_skid
+ _ApplePlatformTLSRSARootCAG1_spki
+ _AppleRootCAG2SPKI
+ _AppleRootCAG2_skid
+ _AppleRootCAG2_spki
+ _AppleRootCAG3SPKI
+ _AppleRootCAG3_skid
+ _AppleRootCAG3_spki
+ _AppleRootCA_skid
+ _AppleRootCA_spki
+ _AppleRootFlags
+ _AppleRootSPKIs
+ _BASepAppRoot_public_key
+ _BASepAppRoot_skid
+ _BASepAppRoot_spki
+ _BASystemRoot_public_key
+ _BASystemRoot_skid
+ _BASystemRoot_spki
+ _BAUserRoot_public_key
+ _BAUserRoot_skid
+ _BAUserRoot_spki
+ _BlockedYonkers_spki
+ _CFDictionaryGetTypeID
+ _CFEqual
+ _CFStringGetLength
+ _CTEvaluateICDPFederation
+ _CTGetICDPFederationType
+ _DevICDPFederationRoot152PublicKey
+ _DevICDPFederationRoot152SKID
+ _DevICDPFederationRoot152_public_key
+ _DevICDPFederationRoot152_skid
+ _DevICDPFederationRoot4PublicKey
+ _DevICDPFederationRoot4SKID
+ _DevICDPFederationRoot4_public_key
+ _DevICDPFederationRoot4_skid
+ _ICDPFederationRoot101PublicKey
+ _ICDPFederationRoot101SKID
+ _ICDPFederationRoot101_public_key
+ _ICDPFederationRoot101_skid
+ _ICDPFederationRoot102PublicKey
+ _ICDPFederationRoot102SKID
+ _ICDPFederationRoot102_public_key
+ _ICDPFederationRoot102_skid
+ _ICDPFederationRoot103PublicKey
+ _ICDPFederationRoot103SKID
+ _ICDPFederationRoot103_public_key
+ _ICDPFederationRoot103_skid
+ _ICDPFederationRoot310PublicKey
+ _ICDPFederationRoot310SKID
+ _ICDPFederationRoot310_public_key
+ _ICDPFederationRoot310_skid
+ _ICDPFederationRoot500PublicKey
+ _ICDPFederationRoot500SKID
+ _ICDPFederationRoot500_public_key
+ _ICDPFederationRoot500_skid
+ _IORegistryEntryGetParentEntry
+ _MFi4RootSPKI
+ _MFi4Root_public_key
+ _MFi4Root_skid
+ _MFi4Root_spki
+ _MobileKeyBagLibrary
+ _MobileKeyBagLibraryCore
+ _MobileKeyBagLibraryCore.frameworkLibrary
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_106
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ _OUTLINED_FUNCTION_110
+ _OUTLINED_FUNCTION_111
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _OUTLINED_FUNCTION_114
+ _OUTLINED_FUNCTION_115
+ _OUTLINED_FUNCTION_116
+ _OUTLINED_FUNCTION_117
+ _OUTLINED_FUNCTION_118
+ _OUTLINED_FUNCTION_119
+ _OUTLINED_FUNCTION_120
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ _REQUIRE_func.cold.1
+ _SEKProdRoot_public_key
+ _SEKProdRoot_skid
+ _SEKTestRoot_public_key
+ _SEKTestRoot_skid
+ _TestApplePlatformBackportECCRootCAG1
+ _TestApplePlatformBackportECCRootCAG1PublicKey
+ _TestApplePlatformBackportECCRootCAG1SKID
+ _TestApplePlatformBackportECCRootCAG1SPKI
+ _TestApplePlatformBackportECCRootCAG1_public_key
+ _TestApplePlatformBackportECCRootCAG1_skid
+ _TestApplePlatformBackportECCRootCAG1_spki
+ _TestApplePlatformBackportRSARootCAG1
+ _TestApplePlatformBackportRSARootCAG1PublicKey
+ _TestApplePlatformBackportRSARootCAG1SKID
+ _TestApplePlatformBackportRSARootCAG1SPKI
+ _TestApplePlatformBackportRSARootCAG1_public_key
+ _TestApplePlatformBackportRSARootCAG1_skid
+ _TestApplePlatformBackportRSARootCAG1_spki
+ _TestApplePlatformBootstrapECCRootCAG1
+ _TestApplePlatformBootstrapECCRootCAG1PublicKey
+ _TestApplePlatformBootstrapECCRootCAG1SKID
+ _TestApplePlatformBootstrapECCRootCAG1SPKI
+ _TestApplePlatformBootstrapECCRootCAG1_public_key
+ _TestApplePlatformBootstrapECCRootCAG1_skid
+ _TestApplePlatformBootstrapECCRootCAG1_spki
+ _TestApplePlatformCodeSigningECCRootCAG1
+ _TestApplePlatformCodeSigningECCRootCAG1PublicKey
+ _TestApplePlatformCodeSigningECCRootCAG1SKID
+ _TestApplePlatformCodeSigningECCRootCAG1SPKI
+ _TestApplePlatformCodeSigningECCRootCAG1_public_key
+ _TestApplePlatformCodeSigningECCRootCAG1_skid
+ _TestApplePlatformCodeSigningECCRootCAG1_spki
+ _TestApplePlatformCodeSigningRSARootCAG1
+ _TestApplePlatformCodeSigningRSARootCAG1PublicKey
+ _TestApplePlatformCodeSigningRSARootCAG1SKID
+ _TestApplePlatformCodeSigningRSARootCAG1SPKI
+ _TestApplePlatformCodeSigningRSARootCAG1_public_key
+ _TestApplePlatformCodeSigningRSARootCAG1_skid
+ _TestApplePlatformCodeSigningRSARootCAG1_spki
+ _TestApplePlatformDeveloperECCRootCAG1
+ _TestApplePlatformDeveloperECCRootCAG1PublicKey
+ _TestApplePlatformDeveloperECCRootCAG1SKID
+ _TestApplePlatformDeveloperECCRootCAG1SPKI
+ _TestApplePlatformDeveloperECCRootCAG1_public_key
+ _TestApplePlatformDeveloperECCRootCAG1_skid
+ _TestApplePlatformDeveloperECCRootCAG1_spki
+ _TestApplePlatformDeveloperRSARootCAG1
+ _TestApplePlatformDeveloperRSARootCAG1PublicKey
+ _TestApplePlatformDeveloperRSARootCAG1SKID
+ _TestApplePlatformDeveloperRSARootCAG1SPKI
+ _TestApplePlatformDeveloperRSARootCAG1_public_key
+ _TestApplePlatformDeveloperRSARootCAG1_skid
+ _TestApplePlatformDeveloperRSARootCAG1_spki
+ _TestApplePlatformECCRootCAG1
+ _TestApplePlatformECCRootCAG1PublicKey
+ _TestApplePlatformECCRootCAG1SKID
+ _TestApplePlatformECCRootCAG1SPKI
+ _TestApplePlatformECCRootCAG1_public_key
+ _TestApplePlatformECCRootCAG1_skid
+ _TestApplePlatformECCRootCAG1_spki
+ _TestApplePlatformMultipurposeECCRootCAG1
+ _TestApplePlatformMultipurposeECCRootCAG1PublicKey
+ _TestApplePlatformMultipurposeECCRootCAG1SKID
+ _TestApplePlatformMultipurposeECCRootCAG1SPKI
+ _TestApplePlatformMultipurposeECCRootCAG1_public_key
+ _TestApplePlatformMultipurposeECCRootCAG1_skid
+ _TestApplePlatformMultipurposeECCRootCAG1_spki
+ _TestApplePlatformMultipurposeRSARootCAG1
+ _TestApplePlatformMultipurposeRSARootCAG1PublicKey
+ _TestApplePlatformMultipurposeRSARootCAG1SKID
+ _TestApplePlatformMultipurposeRSARootCAG1SPKI
+ _TestApplePlatformMultipurposeRSARootCAG1_public_key
+ _TestApplePlatformMultipurposeRSARootCAG1_skid
+ _TestApplePlatformMultipurposeRSARootCAG1_spki
+ _TestApplePlatformRSARootCAG1
+ _TestApplePlatformRSARootCAG1PublicKey
+ _TestApplePlatformRSARootCAG1SKID
+ _TestApplePlatformRSARootCAG1SPKI
+ _TestApplePlatformRSARootCAG1_public_key
+ _TestApplePlatformRSARootCAG1_skid
+ _TestApplePlatformRSARootCAG1_spki
+ _TestApplePlatformTLSECCRootCAG1
+ _TestApplePlatformTLSECCRootCAG1PublicKey
+ _TestApplePlatformTLSECCRootCAG1SKID
+ _TestApplePlatformTLSECCRootCAG1SPKI
+ _TestApplePlatformTLSECCRootCAG1_public_key
+ _TestApplePlatformTLSECCRootCAG1_skid
+ _TestApplePlatformTLSECCRootCAG1_spki
+ _TestApplePlatformTLSRSARootCAG1
+ _TestApplePlatformTLSRSARootCAG1PublicKey
+ _TestApplePlatformTLSRSARootCAG1SKID
+ _TestApplePlatformTLSRSARootCAG1SPKI
+ _TestApplePlatformTLSRSARootCAG1_public_key
+ _TestApplePlatformTLSRSARootCAG1_skid
+ _TestApplePlatformTLSRSARootCAG1_spki
+ _TestAppleRootCAG2
+ _TestAppleRootCAG2SPKI
+ _TestAppleRootCAG2_skid
+ _TestAppleRootCAG2_spki
+ _TestAppleRootCAG3
+ _TestAppleRootCAG3SPKI
+ _TestAppleRootCAG3_skid
+ _TestAppleRootCAG3_spki
+ _TestAppleRootCA_skid
+ _TestAppleRootCA_spki
+ _TestAppleRootECC_skid
+ _TestAppleRootECC_spki
+ _UcrtRootSPKI
+ _UcrtRoot_public_key
+ _UcrtRoot_spki
+ _X509PolicyICDPFederation
+ __AKSIdentityAddPersonaWithACM
+ __AKSIdentityChangePasscode
+ __AKSIdentityChangePasscode.cold.1
+ __AKSIdentitySetPrimary
+ __AKSIdentityTransferPrimary
+ __Block_object_assign
+ __Block_object_dispose
+ ___MobileKeyBagLibraryCore_block_invoke
+ ___block_descriptor_tmp.10
+ ___block_descriptor_tmp.126
+ ___block_descriptor_tmp.137
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.15
+ ___block_descriptor_tmp.151
+ ___block_descriptor_tmp.167
+ ___block_descriptor_tmp.50
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.8
+ ___block_literal_global.150
+ ___block_literal_global.153
+ ___block_literal_global.169
+ ___cf_set_lock_state_block_invoke
+ ___copy_helper_block_8_32r
+ ___der_key_label
+ ___der_key_memento_expiry_bucket_0m_20m
+ ___der_key_memento_expiry_bucket_0m_2m
+ ___der_key_memento_expiry_bucket_10m_inf
+ ___der_key_memento_expiry_bucket_20m_60m
+ ___der_key_memento_expiry_bucket_24h_48h
+ ___der_key_memento_expiry_bucket_2m_4m
+ ___der_key_memento_expiry_bucket_48h_72h
+ ___der_key_memento_expiry_bucket_4m_6m
+ ___der_key_memento_expiry_bucket_60m_24h
+ ___der_key_memento_expiry_bucket_6m_8m
+ ___der_key_memento_expiry_bucket_72h_inf
+ ___der_key_memento_expiry_bucket_8m_10m
+ ___der_key_memento_expiry_counter
+ ___der_key_memento_expiry_state
+ ___der_key_primary_group_uuid
+ ___der_key_primary_user_uuid
+ ___der_key_sw_tag
+ ___der_key_timestamp
+ ___der_key_username
+ ___der_key_wkukey_kcv
+ ___destroy_helper_block_8_32r
+ ___getMKBUnlockDeviceSymbolLoc_block_invoke
+ ___getMKBUnlockDeviceWithACMSymbolLoc_block_invoke
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy240_8
+ ___swift_memcpy41_8
+ ___swift_memcpy82_8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___swift_project_boxed_opaque_existential_1
+ ___xpc_set_fv_policy_status_block_invoke
+ ___xpc_set_lock_state_block_invoke
+ __aks_backup_enable_volume
+ __aks_change_secret_epilogue
+ __aks_change_secret_epilogue.cold.1
+ __aks_recover_with_escrow_bag
+ __aks_recover_with_escrow_bag.cold.1
+ __aks_se_get_reset_token_for_memento_secret
+ __aks_set_configuration
+ __aks_set_system_with_passcode
+ __aks_set_system_with_passcode.cold.1
+ __aks_unlock_bag
+ __aks_unlock_bag.cold.1
+ __aks_unlock_with_sync_bag
+ __akslog_context
+ __current_pid
+ __merge_dict_cb.cold.2
+ __sl_dlopen
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AppleKeyStore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AppleKeyStore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AppleKeyStore
+ _abort_report_np
+ _aks_apfs_container_disk_for_path
+ _aks_apfs_container_disk_for_path.cold.1
+ _aks_apfs_container_disk_for_path.cold.2
+ _aks_apfs_container_disk_for_path.cold.3
+ _aks_apfs_container_disk_for_path.cold.4
+ _aks_apfs_container_disk_for_path.cold.5
+ _aks_apfs_container_disk_for_path.cold.6
+ _aks_apfs_container_disk_for_path.cold.7
+ _aks_apfs_container_disk_for_path.cold.8
+ _aks_apfs_container_disk_for_path.cold.9
+ _aks_apfs_copy_volume_uuid_for_disk
+ _aks_apfs_get_disk_portability
+ _aks_apfs_get_disk_portability.cold.1
+ _aks_apfs_get_disk_portability.cold.2
+ _aks_apfs_get_disk_portability.cold.3
+ _aks_apfs_mountpoint_for_disk
+ _aks_backup_enable_volume_with_acm
+ _aks_change_secret_epilogue_with_acm
+ _aks_change_secret_epilogue_with_opts
+ _aks_change_secret_with_kek
+ _aks_change_secret_with_kek.cold.1
+ _aks_create_bag_with_acm
+ _aks_create_escrow_bag_with_acm
+ _aks_create_sync_bag_with_acm
+ _aks_enable_cache_flow
+ _aks_enable_cache_flow.cold.1
+ _aks_get_icsc_srp
+ _aks_recover_with_escrow_bag_with_acm
+ _aks_reset_iteration_count
+ _aks_reset_iteration_count.cold.1
+ _aks_se_get_passcode_derivation
+ _aks_se_get_reset_token_for_memento_secret_with_acm
+ _aks_se_get_reset_token_for_memento_secret_with_opts
+ _aks_se_memento_secret_drop
+ _aks_se_memento_secret_drop.cold.1
+ _aks_se_recover_with_acm
+ _aks_se_recover_with_acm.cold.1
+ _aks_se_recover_with_opts
+ _aks_set_configuration_with_acm
+ _aks_set_configuration_with_opts
+ _aks_set_system_with_acm
+ _aks_set_system_with_opts
+ _aks_unlock_bag_with_acm
+ _aks_unlock_device_with_acm
+ _aks_unlock_device_with_acm.cold.1
+ _aks_unlock_device_with_opts
+ _aks_unlock_with_sync_bag_with_acm
+ _aks_verify_password_memento_with_acm
+ _aks_verify_password_with_acm
+ _aks_verify_password_with_opts
+ _asprintf
+ _associated conformance 13AppleKeyStore09AKSSystemB10GenerationOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 13AppleKeyStore09AKSSystemB4TypeOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04LockE0O10CodingKeysOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04LockE0O10CodingKeysOs0gB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04LockE0O10CodingKeysOs0gB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04LockE0O17SwiftASN1Internal21DERImplicitlyTaggableAaH12DERParseable
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04LockE0O17SwiftASN1Internal21DERImplicitlyTaggableAaH15DERSerializable
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04LockE0OSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V10CodingKeysOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V10CodingKeysOs0gB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V10CodingKeysOs0gB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V17SwiftASN1Internal21DERImplicitlyTaggableAaH12DERParseable
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V17SwiftASN1Internal21DERImplicitlyTaggableAaH15DERSerializable
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0Vs10SetAlgebraAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0Vs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0Vs9OptionSetAASY
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV04MoreE0Vs9OptionSetAAs0H7Algebra
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOs0fB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOs0fB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADV10CodingKeysOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADV10CodingKeysOs0fB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADV10CodingKeysOs0fB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADV17SwiftASN1Internal21DERImplicitlyTaggableAaG12DERParseable
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADV17SwiftASN1Internal21DERImplicitlyTaggableAaG15DERSerializable
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADVs10SetAlgebraAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADVs9OptionSetAASY
+ _associated conformance 13AppleKeyStore11AKSIdentityV5StateVADVs9OptionSetAAs0G7Algebra
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOs0fB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOs0fB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOs0hB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOs0hB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateV10CodingKeysOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateV10CodingKeysOs0iB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateV10CodingKeysOs0iB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateVs10SetAlgebraAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateVs9OptionSetAASY
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateVs9OptionSetAAs0J7Algebra
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV7OptionsV10CodingKeysOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV7OptionsV10CodingKeysOs0gB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV6ConfigV7OptionsV10CodingKeysOs0gB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOs0fB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLOs0fB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateV10CodingKeysOSHAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateV10CodingKeysOs0gB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateV10CodingKeysOs0gB0AAs28CustomDebugStringConvertible
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateV17SwiftASN1Internal21DERImplicitlyTaggableAaH12DERParseable
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateV17SwiftASN1Internal21DERImplicitlyTaggableAaH15DERSerializable
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateVs10SetAlgebraAASQ
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateVs9OptionSetAASY
+ _associated conformance 13AppleKeyStore11AKSIdentityV7MementoV5StateVs9OptionSetAAs0H7Algebra
+ _associated conformance 13AppleKeyStore9AKSHandleV10CodingKeysOSHAASQ
+ _associated conformance 13AppleKeyStore9AKSHandleV10CodingKeysOs0eB0AAs23CustomStringConvertible
+ _associated conformance 13AppleKeyStore9AKSHandleV10CodingKeysOs0eB0AAs28CustomDebugStringConvertible
+ _audit_stringMobileKeyBag
+ _ccder_sizeof_implicit_raw_octet_string
+ _cf_set_dict_value
+ _cf_set_lock_state
+ _copy_raw_secret
+ _decode_icsc_params_internal
+ _der_key_label
+ _der_key_memento_expiry_bucket_0m_20m
+ _der_key_memento_expiry_bucket_0m_2m
+ _der_key_memento_expiry_bucket_10m_inf
+ _der_key_memento_expiry_bucket_20m_60m
+ _der_key_memento_expiry_bucket_24h_48h
+ _der_key_memento_expiry_bucket_2m_4m
+ _der_key_memento_expiry_bucket_48h_72h
+ _der_key_memento_expiry_bucket_4m_6m
+ _der_key_memento_expiry_bucket_60m_24h
+ _der_key_memento_expiry_bucket_6m_8m
+ _der_key_memento_expiry_bucket_72h_inf
+ _der_key_memento_expiry_bucket_8m_10m
+ _der_key_memento_expiry_counter
+ _der_key_memento_expiry_state
+ _der_key_primary_group_uuid
+ _der_key_primary_user_uuid
+ _der_key_sw_tag
+ _der_key_timestamp
+ _der_key_username
+ _der_key_wkukey_kcv
+ _dlerror
+ _dlsym
+ _encode_icsc_params_internal
+ _getMKBUnlockDeviceSymbolLoc
+ _getMKBUnlockDeviceSymbolLoc.ptr
+ _getMKBUnlockDeviceWithACMSymbolLoc
+ _getMKBUnlockDeviceWithACMSymbolLoc.ptr
+ _get_akslog_context
+ _get_akslog_pid
+ _getmntinfo
+ _icdpFederationAnchors
+ _keypath_getTm
+ _numICDPRoots
+ _process_lock_state_for_handle
+ _ref_key_create_request_to_class
+ _se_derivation_request_deserialize
+ _se_derivation_request_serialization_len
+ _se_derivation_request_serialize
+ _set_akslog_context
+ _set_akslog_pid
+ _strcmp
+ _strdup
+ _swift_makeBoxUnique
+ _swift_unknownObjectRelease_n
+ _swift_willThrowTypedImpl
+ _symbolic $ss12CaseIterableP
+ _symbolic SS
+ _symbolic SaySSG
+ _symbolic Say_____G 13AppleKeyStore09AKSSystemB10GenerationO
+ _symbolic Say_____G 13AppleKeyStore09AKSSystemB4TypeO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV5StateV
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV5StateV04LockE0O
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV5StateV04LockE0O10CodingKeysO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V10CodingKeysO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV5StateV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV5StateVADV
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV5StateVADV10CodingKeysO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV6ConfigV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateV
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateV10CodingKeysO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV6ConfigV7OptionsV10CodingKeysO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV7MementoV
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV7MementoV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLO
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV7MementoV5StateV
+ _symbolic _____ 13AppleKeyStore11AKSIdentityV7MementoV5StateV10CodingKeysO
+ _symbolic _____ 13AppleKeyStore9AKSHandleV10CodingKeysO
+ _symbolic _____ s6UInt32V
+ _symbolic _____Sg 13AppleKeyStore11AKSIdentityV5StateV04LockE0O
+ _symbolic _____Sg 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V
+ _symbolic _____Sg 13AppleKeyStore11AKSIdentityV5StateVADV
+ _symbolic _____Sg 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV
+ _symbolic _____Sg 13AppleKeyStore11AKSIdentityV7MementoV5StateV
+ _symbolic _____Sg s6UInt32V
+ _symbolic _____Sg s6UInt64V
+ _symbolic ______SSt 13AppleKeyStore11AKSIdentityV5StateV04MoreE0V
+ _symbolic ______SSt 13AppleKeyStore11AKSIdentityV5StateVADV
+ _symbolic ______SSt 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateV
+ _symbolic ______SSt 13AppleKeyStore11AKSIdentityV6ConfigV7OptionsV
+ _symbolic ______SSt 13AppleKeyStore11AKSIdentityV7MementoV5StateV
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV5StateV04LockH0O10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV5StateV04MoreH0V10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV5StateV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV5StateVAFV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV6ConfigV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV6ConfigV7OptionsV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV7MementoV10CodingKeys33_F7C24E31B02C6EB54CF5863DB581FA0ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore11AKSIdentityV7MementoV5StateV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 13AppleKeyStore9AKSHandleV10CodingKeysO
+ _symbolic _____y______SStG s23_ContiguousArrayStorageC 13AppleKeyStore11AKSIdentityV5StateV04MoreH0V
+ _symbolic _____y______SStG s23_ContiguousArrayStorageC 13AppleKeyStore11AKSIdentityV5StateVAFV
+ _symbolic _____y______SStG s23_ContiguousArrayStorageC 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV5StateV
+ _symbolic _____y______SStG s23_ContiguousArrayStorageC 13AppleKeyStore11AKSIdentityV6ConfigV7OptionsV
+ _symbolic _____y______SStG s23_ContiguousArrayStorageC 13AppleKeyStore11AKSIdentityV7MementoV5StateV
+ _type_layout_string 13AppleKeyStore11AKSIdentityV5StateV
+ _type_layout_string 13AppleKeyStore11AKSIdentityV6ConfigV12RecoveryBlobV
+ _type_layout_string 13AppleKeyStore11AKSIdentityV7MementoV
+ _type_layout_string 13AppleKeyStore11AKSIdentityV7MementoV5StateV
+ _uid_from_handle
+ _vsnprintf
+ _xpc_set_dict_value
+ _xpc_set_fv_policy_status
+ _xpc_set_lock_state
- _AKSIdentityChangePasscode.cold.1
- _AKSIdentityMigrate
- _ApplePlatformBackportECCRootG1
- _ApplePlatformBackportECCRootG1PublicKey
- _ApplePlatformBackportECCRootG1SKID
- _ApplePlatformBackportECCRootG1SPKI
- _ApplePlatformBackportRSARootG1
- _ApplePlatformBackportRSARootG1PublicKey
- _ApplePlatformBackportRSARootG1SKID
- _ApplePlatformBackportRSARootG1SPKI
- _AppleRootCAPublicKey
- _AppleRootCASKID
- _AppleRootG2PublicKey
- _AppleRootG2SKID
- _AppleRootG2SPKI
- _AppleRootG3PublicKey
- _AppleRootG3SKID
- _AppleRootG3SPKI
- _BlockedYonkersPublicKey
- _MFi4RootSpki
- _SEKProdRoot
- _SEKProdRootSPKI
- _SEKTestRoot
- _SEKTestRootSPKI
- _TestApplePlatformBackportECCRootG1
- _TestApplePlatformBackportECCRootG1PublicKey
- _TestApplePlatformBackportECCRootG1SKID
- _TestApplePlatformBackportECCRootG1SPKI
- _TestApplePlatformBackportRSARootG1
- _TestApplePlatformBackportRSARootG1PublicKey
- _TestApplePlatformBackportRSARootG1SKID
- _TestApplePlatformBackportRSARootG1SPKI
- _TestAppleRootCAPublicKey
- _TestAppleRootCASKID
- _TestAppleRootECCPublicKey
- _TestAppleRootECCSKID
- _TestAppleRootG2
- _TestAppleRootG2PublicKey
- _TestAppleRootG2SKID
- _TestAppleRootG2SPKI
- _TestAppleRootG3
- _TestAppleRootG3PublicKey
- _TestAppleRootG3SKID
- _TestAppleRootG3SPKI
- _UcrtRootSpki
- ____service_get_connection_block_invoke
- ____service_get_connection_block_invoke_2
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.17
- ___block_descriptor_tmp.171
- ___block_literal_global.152
- ___block_literal_global.157
- ___block_literal_global.173
- ___block_literal_global.19
- ___swift_memcpy232_8
- __acrt_root_public_key
- __applekeystored_client_send_secret
- __applekeystored_client_send_uid
- __baa_sep_app_root_public_key
- __baa_sep_app_root_skid
- __baa_sep_app_root_spki
- __baa_system_root_public_key
- __baa_system_root_skid
- __baa_system_root_spki
- __baa_user_root_public_key
- __baa_user_root_skid
- __baa_user_root_spki
- __mfi4_root_pub_key
- __mfi4_root_skid
- __mfi4_root_spki
- __sek_prod_root_public_key
- __sek_prod_root_skid
- __sek_prod_root_spki
- __sek_test_root_public_key
- __sek_test_root_skid
- __sek_test_root_spki
- __service_send_msg
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_AppleKeyStore
- __ucrt_root_pub_key
- __ucrt_root_spki
- __xpc_error_connection_invalid
- __xpc_type_error
- _aks_change_secret_epilogue.cold.1
- _aks_change_secret_opts.cold.1
- _aks_recover_with_escrow_bag.cold.1
- _aks_set_system_with_passcode.cold.1
- _aks_unlock_bag.cold.1
- _applekeystored_client_identity_change_passcode
- _applekeystored_client_identity_create
- _applekeystored_client_identity_delete
- _applekeystored_client_identity_load
- _applekeystored_client_identity_migrate
- _applekeystored_client_kb_change_secret
- _applekeystored_client_kb_create
- _applekeystored_client_kb_is_locked
- _applekeystored_client_kb_load
- _applekeystored_client_kb_load_uid
- _applekeystored_client_kb_reset
- _applekeystored_client_kb_save
- _applekeystored_client_kb_unload
- _applekeystored_client_kb_unlock
- _applekeystored_client_stash_create
- _applekeystored_client_stash_load
- _der_key_validate
- _der_key_validate.cold.1
- _der_key_validate.cold.2
- _get_aks_log_pid
- _getenv
- _set_info_key
- _set_lock_state
- _swift_bridgeObjectRelease_n
- _type_layout_string 13AppleKeyStore11AKSIdentityV6ConfigV7OptionsV
- _xpc_connection_create_mach_service
- _xpc_connection_resume
- _xpc_connection_send_message_with_reply_sync
- _xpc_connection_set_event_handler
- _xpc_copy_description
- _xpc_dictionary_create
- _xpc_dictionary_get_bool
- _xpc_dictionary_get_int64
- _xpc_dictionary_set_data
- _xpc_get_type
- _xpc_release
CStrings:
+ "%s"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %swarning parsing an unverified attestation%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s APFSVolumeGetUnlockRecord: %s\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s APFSVolumeListUUIDsOfUnlockRecords failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s APFSVolumeRemoveUnlockRecord: %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s APFSVolumeSetUnlockRecord: %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Bad input %d %zd %d %zd%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Container bsd name: %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Controller supports encryption: not portable%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not create container dev path%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get C string for container%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get Container Scheme for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get Container for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get IOService for disk %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get container bsd name%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get snapshot parent volume for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Device is connected internally: not portable%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Escrow blob is too big %zd/%llu%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get parent IO object for %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get volume UUID for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOObject %{public}s is not AppleAPFSVolume%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOServiceGetMatchingService failed to find %{public}s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s MKBUnlockDevice()->%d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s MKBUnlockDeviceWithACM()->%d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Not a Volume Object for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unexpected IO property type%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unwrapped DER backup bag%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s context not initialized%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s dumping attestation info:%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s error: CTEvaluateBAA returned %x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s error: incorrect key type%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s error: invalid namespace, expected ssca%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s error: not attestion only key%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s escrow blob parse error %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s extension error %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fstatfs error: %s\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s incorrect attestation data%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid type%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid uuid size%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s no apfs fwk%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s no kek%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s self has no sig%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s skipping: not apfs%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s statfs error: %s\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s string fail%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mis-match during load%s\n"
+ "AppleAPFSSnapshot"
+ "BSD Name"
+ "CacheFlowEnabled"
+ "Controller Characteristics"
+ "DeviceHandle"
+ "Encryption Type"
+ "IOService"
+ "Internal"
+ "MKBUnlockDevice"
+ "MKBUnlockDeviceWithACM"
+ "Physical Interconnect Location"
+ "Protocol Characteristics"
+ "_aks_backup_enable_volume"
+ "_aks_change_secret_epilogue"
+ "_aks_recover_with_escrow_bag"
+ "_aks_se_get_reset_token_for_memento_secret"
+ "_aks_set_configuration"
+ "_aks_set_system_with_passcode"
+ "_aks_unlock_bag"
+ "_aks_unlock_with_sync_bag"
+ "aks.fw"
+ "aks_apfs_container_disk_for_path"
+ "aks_apfs_get_disk_portability"
+ "aks_change_secret_with_kek"
+ "aks_enable_cache_flow"
+ "aks_get_icsc_srp"
+ "aks_reset_iteration_count"
+ "aks_se_get_passcode_derivation"
+ "aks_se_memento_secret_drop"
+ "aks_se_recover_with_acm"
+ "aks_unlock_device_with_acm"
+ "auxiliary-unlocked"
+ "beenPasscodeUnlocked"
+ "description"
+ "escrowPasscodePeriod"
+ "escrowTokenPeriod"
+ "escrowUnwrapRequired"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "hasFilevaultRecovery"
+ "hasLastKnownGoodPasswordRecovery"
+ "i28@?0^{__CFString=}8Q16i24"
+ "inactivityRebootEnabled"
+ "inactivityRebootSet"
+ "maxUnlockAttempts"
+ "mementoBlobExists"
+ "mementoPasscodeGeneration"
+ "mementoSupported"
+ "onenessAutomaticMode"
+ "passcodeGeneration"
+ "passcodeServiceEntangled"
+ "passcodeServiceProtected"
+ "passcodeTreshold"
+ "peerRecordsDirty"
+ "peerRecordsFlush"
+ "rawValue"
+ "recoveryBlobState"
+ "recoveryCountdown"
+ "recoveryIterations"
+ "recoveryPasscodeServiceFailedUnlockedAttemptsCached"
+ "recoveryRequired"
+ "recoveryTargetIterations"
+ "remoteSessionUnlocked"
+ "sb"
+ "seRecoveryRequired"
+ "ses"
+ "sfa"
+ "sgs"
+ "sls"
+ "sms"
+ "softlink:o:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
+ "srcd"
+ "ss"
+ "unlockedWithEscrow"
+ "waffleChefProtected"
+ "xartUnlockPolicy"
+ "xartUnlockPolicyCached"
+ "xartUnlockPolicyDirty"
+ "xartUnlockPolicyEnforced"
- "%s%s:%s%s%s%s%u:%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %sdump %s (len = %zd)%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %swarning parsing an unverified attestation%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s APFSVolumeGetUnlockRecord: %s\n%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s APFSVolumeListUUIDsOfUnlockRecords failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s APFSVolumeRemoveUnlockRecord: %s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s APFSVolumeSetUnlockRecord: %s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Bad input %d %zd %d %zd%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Escrow blob is too big %zd/%llu%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to get volume UUID for %s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Unwrapped DER backup bag%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s context not initialized%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s dumping attestation info:%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s error: CTEvaluateBAA returned %x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s error: incorrect key type%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s error: invalid namespace, expected ssca%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s error: not attestion only key%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s escrow blob parse error %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s extension error %s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s incorrect attestation data%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s invalid type%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s invalid uuid size%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s ioreg: %d, boot_arg: %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s no apfs fwk%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s no kek%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s overflow%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s self has no sig%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s skipping: not apfs%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s statfs error: %s\n%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s string fail%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s version mis-match during load%s\n"
- "USE_APPLEKEYSTORED_TEST"
- "Using applekeystored-test variant"
- "_context"
- "_destroy"
- "_key"
- "_locked"
- "_no_pin"
- "_rc"
- "_request"
- "_secret"
- "_secret_new"
- "_uid"
- "_user_uuid"
- "aks"
- "aks_backup_enable_volume"
- "aks_change_secret_epilogue"
- "aks_change_secret_opts"
- "aks_recover_with_escrow_bag"
- "aks_se_get_reset_token_for_memento_secret"
- "aks_set_configuration"
- "aks_set_system_with_passcode"
- "aks_unlock_bag"
- "aks_unlock_with_sync_bag"
- "applekeystored not available"
- "applekeystored should never get messages on this connection: %s"
- "com.apple.applekeystored"
- "com.apple.applekeystored-test"
- "der_key_validate"
- "failed to open connection to %s\n"
- "v16@?0^v8"

```
