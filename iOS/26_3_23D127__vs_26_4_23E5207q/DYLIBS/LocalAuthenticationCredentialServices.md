## LocalAuthenticationCredentialServices

> `/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x2360
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x428
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x117
-  __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__oslogstring: 0x97
+2005.100.174.0.0
+  __TEXT.__text: 0x18260
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x63c
+  __TEXT.__const: 0x290
+  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__cstring: 0x217a
+  __TEXT.__oslogstring: 0x3e0
   __TEXT.__dlopen_cstrs: 0x5d
-  __TEXT.__unwind_info: 0x170
-  __TEXT.__objc_classname: 0xa9
-  __TEXT.__objc_methname: 0x43e
-  __TEXT.__objc_methtype: 0x144
-  __TEXT.__objc_stubs: 0x3e0
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x158
-  __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__swift5_typeref: 0x52
+  __TEXT.__constg_swiftt: 0xd8
+  __TEXT.__swift5_reflstr: 0x10
+  __TEXT.__swift5_fieldmd: 0x48
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__unwind_info: 0x5a8
+  __TEXT.__eh_frame: 0x4b8
+  __TEXT.__objc_classname: 0x1b3
+  __TEXT.__objc_methname: 0x807
+  __TEXT.__objc_methtype: 0x37c
+  __TEXT.__objc_stubs: 0x520
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x150
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xb78
-  __DATA.__objc_ivar: 0x28
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0xf0
+  __AUTH_CONST.__cfstring: 0x140
+  __AUTH_CONST.__objc_const: 0x1700
+  __AUTH.__objc_data: 0x240
+  __DATA.__objc_ivar: 0x10
+  __DATA.__data: 0x222
+  __DATA.__bss: 0x98
+  __DATA_DIRTY.__objc_data: 0x308
+  __DATA_DIRTY.__data: 0x150
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C8B59F7D-71B2-38BE-9570-221A5BEC26E2
-  Functions: 96
-  Symbols:   425
-  CStrings:  104
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: F41A89BE-DFD8-363A-AA74-B560E4C5ABB0
+  Functions: 648
+  Symbols:   1136
+  CStrings:  422
 
Symbols:
+ -[LACSUnmanagedContext .cxx_destruct]
+ -[LACSUnmanagedContext _decryptData:seed:externalizedContext:error:]
+ -[LACSUnmanagedContext _encryptData:seed:externalizedContext:error:]
+ -[LACSUnmanagedContext _encryptionSeedForContext:error:]
+ -[LACSUnmanagedContext _withContext:error:]
+ -[LACSUnmanagedContext _withContext:error:].cold.1
+ -[LACSUnmanagedContext contextRef]
+ -[LACSUnmanagedContext dealloc]
+ -[LACSUnmanagedContext externalize]
+ -[LACSUnmanagedContext fetchCredentialData:]
+ -[LACSUnmanagedContext init:]
+ -[LACSUnmanagedContext init:].cold.1
+ -[LACSUnmanagedContext initWithACMContextRef:ownsContextRef:]
+ -[LACSUnmanagedContext initWithContextRef:error:]
+ -[LACSUnmanagedContext initWithContextRef:error:].cold.1
+ -[LACSUnmanagedContext storeCredentialData:securely:error:]
+ GCC_except_table14
+ GCC_except_table8
+ _ACMContextAddCredential
+ _ACMContextAddCredentialWithScope
+ _ACMContextContainsCredentialType
+ _ACMContextContainsCredentialTypeEx
+ _ACMContextContainsPassphraseCredentialWithPurpose
+ _ACMContextCopyData
+ _ACMContextCreate
+ _ACMContextCreateWithExternalForm
+ _ACMContextCreateWithFlags
+ _ACMContextCredentialGetProperty
+ _ACMContextCredentialGetPropertyEx
+ _ACMContextDelete
+ _ACMContextGetData
+ _ACMContextGetDataEx
+ _ACMContextGetDataProperty
+ _ACMContextGetExternalForm
+ _ACMContextGetExternalForm.cold.1
+ _ACMContextGetInfo
+ _ACMContextGetTrackingNumber
+ _ACMContextRemoveCredentialsByType
+ _ACMContextRemoveCredentialsByTypeAndScope
+ _ACMContextRemoveCredentialsByValue
+ _ACMContextRemoveCredentialsByValueAndScope
+ _ACMContextRemovePassphraseCredentialsByPurposeAndScope
+ _ACMContextReplacePassphraseCredentialsWithScope
+ _ACMContextSetData
+ _ACMContextSetDataEx
+ _ACMContextVerifyAclConstraint
+ _ACMContextVerifyAclConstraintForOperation
+ _ACMContextVerifyPolicy
+ _ACMContextVerifyPolicyEx
+ _ACMContextVerifyPolicyWithPreflight
+ _ACMCredentialCreate
+ _ACMCredentialDelete
+ _ACMCredentialGetProperty
+ _ACMCredentialGetPropertyData
+ _ACMCredentialGetType
+ _ACMCredentialSetProperty
+ _ACMDecryptData
+ _ACMDecryptDataEx
+ _ACMEncryptData
+ _ACMEncryptDataEx
+ _ACMGetAclAuthMethod
+ _ACMGetEnvironmentVariable
+ _ACMGlobalContextAddCredential
+ _ACMGlobalContextCredentialGetProperty
+ _ACMGlobalContextRemoveCredentialsByType
+ _ACMGlobalContextVerifyPolicy
+ _ACMKernelControl
+ _ACMParseAclAndCopyConstraintCharacteristics
+ _ACMPing
+ _ACMRequirementGetPriority
+ _ACMRequirementGetProperties
+ _ACMRequirementGetProperty
+ _ACMRequirementGetPropertyData
+ _ACMRequirementGetState
+ _ACMRequirementGetSubrequirements
+ _ACMRequirementGetType
+ _ACMSEPControl
+ _ACMSEPControlEx
+ _ACMSetEnvironmentVariable
+ _ACMSetEnvironmentVariableWithAccessPolicy
+ _CompareCredentials
+ _CopyCredential
+ _DeallocCredentialList
+ _DeserializeAddCredential
+ _DeserializeAddCredentialType
+ _DeserializeCredential
+ _DeserializeCredentialList
+ _DeserializeGetContextProperty
+ _DeserializeProcessAcl
+ _DeserializeRemoveCredential
+ _DeserializeReplacePassphraseCredential
+ _DeserializeRequirement
+ _DeserializeVerifyAclConstraint
+ _DeserializeVerifyPolicy
+ _GetSerializedAddCredentialSize
+ _GetSerializedCredentialSize
+ _GetSerializedGetContextPropertySize
+ _GetSerializedProcessAclSize
+ _GetSerializedRemoveCredentialSize
+ _GetSerializedReplacePassphraseCredentialSize
+ _GetSerializedRequirementSize
+ _GetSerializedVerifyAclConstraintSize
+ _GetSerializedVerifyPolicySize
+ _IOConnectCallScalarMethod
+ _IOConnectCallStructMethod
+ _IOObjectRelease
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _IOServiceOpen
+ _LACSLogPassword
+ _LACSLogPassword.__logObj
+ _LACSLogPassword.cold.1
+ _LACSLogPassword.onceToken
+ _LibCall_ACMContexAddCredentialWithScope
+ _LibCall_ACMContexRemoveCredentialsByTypeAndScope
+ _LibCall_ACMContextContainsCredentialTypeEx
+ _LibCall_ACMContextCopyData
+ _LibCall_ACMContextCreate
+ _LibCall_ACMContextCreateWithExternalForm
+ _LibCall_ACMContextCredentialGetProperty
+ _LibCall_ACMContextDelete
+ _LibCall_ACMContextGetData
+ _LibCall_ACMContextGetInfo
+ _LibCall_ACMContextLoadFromImage
+ _LibCall_ACMContextRemoveCredentialsByValueAndScope
+ _LibCall_ACMContextSetData
+ _LibCall_ACMContextUnloadToImage
+ _LibCall_ACMContextUnloadToImage_Block
+ _LibCall_ACMContextVerifyAclConstraint
+ _LibCall_ACMContextVerifyAclConstraintForOperation
+ _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx
+ _LibCall_ACMContextVerifyPolicyEx
+ _LibCall_ACMContextVerifyPolicyEx_Block
+ _LibCall_ACMContextVerifyPolicyWithPreflight_Block
+ _LibCall_ACMContextVerifyPolicy_Block
+ _LibCall_ACMCredentialCreate
+ _LibCall_ACMCredentialDelete
+ _LibCall_ACMCredentialGetPropertyData
+ _LibCall_ACMCredentialGetType
+ _LibCall_ACMCredentialSetProperty
+ _LibCall_ACMGetAclAuthMethod_Block
+ _LibCall_ACMGetEnvironmentVariable
+ _LibCall_ACMGetEnvironmentVariable_Block
+ _LibCall_ACMGlobalContextCredentialGetProperty
+ _LibCall_ACMGlobalContextCredentialGetProperty_Block
+ _LibCall_ACMGlobalContextVerifyPolicyEx
+ _LibCall_ACMGlobalContextVerifyPolicy_Block
+ _LibCall_ACMKernDoubleClickNotify
+ _LibCall_ACMKernelControl
+ _LibCall_ACMKernelControl.cold.1
+ _LibCall_ACMKernelControl_Block
+ _LibCall_ACMPing
+ _LibCall_ACMPublishTrustedAccessories
+ _LibCall_ACMRequirementDelete
+ _LibCall_ACMRequirementGetPriority
+ _LibCall_ACMRequirementGetPropertyData
+ _LibCall_ACMRequirementGetState
+ _LibCall_ACMRequirementGetType
+ _LibCall_ACMSEPControl
+ _LibCall_ACMSEPControl_Block
+ _LibCall_ACMSecContextCopyCredentialsArrayEx
+ _LibCall_ACMSecContextGetUnlockSecret
+ _LibCall_ACMSecContextProcessAcl
+ _LibCall_ACMSecContextProcessAclAndCopyAuthMethod
+ _LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement
+ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
+ _LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser
+ _LibCall_ACMSecCredentialsArrayDelete
+ _LibCall_ACMSecSetBiometryAvailability
+ _LibCall_ACMSecSetBuiltinBiometry
+ _LibCall_ACMSetEnvironmentVariable
+ _LibCall_ACMTRMLoadState
+ _LibCall_ACMTRMLoadState_Block
+ _LibCall_ACMTRMSaveState
+ _LibCall_BuildCommand
+ _LibSer_ACMDeserializeEnvironmentVariableType
+ _LibSer_ACMDeserializeSEPControlCode
+ _LibSer_ContextCredentialGetPropertyEx_Deserialize
+ _LibSer_ContextCredentialGetPropertyEx_GetSize
+ _LibSer_ContextCredentialGetPropertyEx_Serialize
+ _LibSer_ContextCredentialGetProperty_Deserialize
+ _LibSer_ContextCredentialGetProperty_GetSize
+ _LibSer_ContextCredentialGetProperty_Serialize
+ _LibSer_DeleteContext_Deserialize
+ _LibSer_DeleteContext_GetSize
+ _LibSer_DeleteContext_Serialize
+ _LibSer_GetAclAuthMethod_Deserialize
+ _LibSer_GetAclAuthMethod_GetSize
+ _LibSer_GetAclAuthMethod_Serialize
+ _LibSer_GetSerializedContainsCredential_GetSize
+ _LibSer_GetSerializedContainsCredential_Serialize
+ _LibSer_GetUnlockSecretResponse_Deserialize
+ _LibSer_GetUnlockSecretResponse_GetSize
+ _LibSer_GetUnlockSecretResponse_Serialize
+ _LibSer_GetUnlockSecret_Deserialize
+ _LibSer_GetUnlockSecret_GetSize
+ _LibSer_GetUnlockSecret_Serialize
+ _LibSer_GlobalContextCredentialGetProperty_Deserialize
+ _LibSer_GlobalContextCredentialGetProperty_GetSize
+ _LibSer_GlobalContextCredentialGetProperty_Serialize
+ _LibSer_RemoveCredentialByType_Deserialize
+ _LibSer_RemoveCredentialByType_GetSize
+ _LibSer_RemoveCredentialByType_Serialize
+ _LibSer_SEPControlResponse_Deserialize
+ _LibSer_SEPControlResponse_GetSize
+ _LibSer_SEPControlResponse_Serialize
+ _LibSer_SEPControl_Deserialize
+ _LibSer_SEPControl_GetSize
+ _LibSer_SEPControl_Serialize
+ _LibSer_StorageAnyCmd_DeserializeCommonFields
+ _LibSer_StorageGetData_Deserialize
+ _LibSer_StorageGetData_GetSize
+ _LibSer_StorageGetData_Serialize
+ _LibSer_StorageSetData_Deserialize
+ _LibSer_StorageSetData_GetSize
+ _LibSer_StorageSetData_Serialize
+ _OBJC_CLASS_$_LACSUnmanagedContext
+ _OBJC_CLASS_$_LACSUnmanagedExtractablePassword
+ _OBJC_CLASS_$_LACSUnmanagedSecurePassword
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ _OBJC_CLASS_$__TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
+ _OBJC_IVAR_$_LACSUnmanagedContext._contextRef
+ _OBJC_IVAR_$_LACSUnmanagedContext._externalizedContextRef
+ _OBJC_IVAR_$_LACSUnmanagedContext._ownsContextRef
+ _OBJC_METACLASS_$_LACSUnmanagedContext
+ _OBJC_METACLASS_$_LACSUnmanagedExtractablePassword
+ _OBJC_METACLASS_$_LACSUnmanagedSecurePassword
+ _OBJC_METACLASS_$__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ _OBJC_METACLASS_$__TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SerializeAddCredential
+ _SerializeCredential
+ _SerializeCredentialList
+ _SerializeGetContextProperty
+ _SerializeProcessAcl
+ _SerializeRemoveCredential
+ _SerializeReplacePassphraseCredential
+ _SerializeRequirement
+ _SerializeVerifyAclConstraint
+ _SerializeVerifyPolicy
+ _Util_AllocCredential
+ _Util_AllocRequirement
+ _Util_CreateRequirement
+ _Util_DeallocCredential
+ _Util_DeallocRequirement
+ _Util_GetBitCount
+ _Util_KeybagLockStateToEnvVar
+ _Util_ReadFromBuffer
+ _Util_SafeDeallocParameters
+ _Util_WriteToBuffer
+ _Util_hexDumpToStrHelper
+ _Util_hexDumpToStrHelper.cold.1
+ _Util_hexDumpToStrHelper.cold.2
+ _Util_isNonNullEqualMemory
+ _Util_isNullOrZeroMemory
+ __CLASS_METHODS_LACSExtractableCredential
+ __CLASS_METHODS_LACSExtractablePassword
+ __CLASS_METHODS_LACSSecureCredential
+ __CLASS_METHODS_LACSSecurePassword
+ __CLASS_METHODS__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ __CLASS_PROPERTIES_LACSExtractableCredential
+ __CLASS_PROPERTIES_LACSExtractablePassword
+ __CLASS_PROPERTIES_LACSSecureCredential
+ __CLASS_PROPERTIES_LACSSecurePassword
+ __CLASS_PROPERTIES__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ __DATA_LACSExtractableCredential
+ __DATA_LACSExtractablePassword
+ __DATA_LACSSecureCredential
+ __DATA_LACSSecurePassword
+ __DATA_LACSUnmanagedExtractablePassword
+ __DATA_LACSUnmanagedSecurePassword
+ __DATA__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ __DATA__TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
+ __INSTANCE_METHODS_LACSExtractableCredential
+ __INSTANCE_METHODS_LACSExtractablePassword
+ __INSTANCE_METHODS_LACSSecureCredential
+ __INSTANCE_METHODS_LACSSecurePassword
+ __INSTANCE_METHODS_LACSUnmanagedExtractablePassword
+ __INSTANCE_METHODS_LACSUnmanagedSecurePassword
+ __INSTANCE_METHODS__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ __INSTANCE_METHODS__TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
+ __IVARS_LACSExtractableCredential
+ __IVARS_LACSExtractablePassword
+ __IVARS_LACSSecureCredential
+ __IVARS_LACSSecurePassword
+ __IVARS_LACSUnmanagedExtractablePassword
+ __IVARS_LACSUnmanagedSecurePassword
+ __IVARS__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ __IVARS__TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
+ __METACLASS_DATA_LACSExtractableCredential
+ __METACLASS_DATA_LACSExtractablePassword
+ __METACLASS_DATA_LACSSecureCredential
+ __METACLASS_DATA_LACSSecurePassword
+ __METACLASS_DATA_LACSUnmanagedExtractablePassword
+ __METACLASS_DATA_LACSUnmanagedSecurePassword
+ __METACLASS_DATA__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ __METACLASS_DATA__TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS_LACSUnmanagedContext
+ __OBJC_$_INSTANCE_VARIABLES_LACSUnmanagedContext
+ __OBJC_$_PROP_LIST_LACSUnmanagedContext
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACSContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACSContext
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_LACSContext
+ __OBJC_CLASS_PROTOCOLS_$_LACSContext
+ __OBJC_CLASS_PROTOCOLS_$_LACSUnmanagedContext
+ __OBJC_CLASS_RO_$_LACSUnmanagedContext
+ __OBJC_LABEL_PROTOCOL_$_LACSContext
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_LACSUnmanagedContext
+ __OBJC_PROTOCOL_$_LACSContext
+ __OBJC_PROTOCOL_$_NSObject
+ __PROPERTIES_LACSExtractableCredential
+ __PROPERTIES_LACSExtractablePassword
+ __PROPERTIES_LACSSecureCredential
+ __PROPERTIES_LACSSecurePassword
+ __PROPERTIES_LACSUnmanagedExtractablePassword
+ __PROPERTIES_LACSUnmanagedSecurePassword
+ __PROPERTIES__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ __PROPERTIES__TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
+ __PROTOCOLS_LACSExtractableCredential
+ __PROTOCOLS_LACSExtractableCredential.2
+ __PROTOCOLS_LACSExtractablePassword
+ __PROTOCOLS_LACSExtractablePassword.2
+ __PROTOCOLS_LACSSecureCredential
+ __PROTOCOLS_LACSSecureCredential.2
+ __PROTOCOLS_LACSSecurePassword
+ __PROTOCOLS_LACSSecurePassword.2
+ __PROTOCOLS__TtC37LocalAuthenticationCredentialServices12LACSPassword
+ __PROTOCOLS__TtC37LocalAuthenticationCredentialServices12LACSPassword.2
+ ___34-[LACSUnmanagedContext contextRef]_block_invoke
+ ___44-[LACSUnmanagedContext fetchCredentialData:]_block_invoke
+ ___44-[LACSUnmanagedContext fetchCredentialData:]_block_invoke_2
+ ___56-[LACSUnmanagedContext _encryptionSeedForContext:error:]_block_invoke
+ ___59-[LACSUnmanagedContext storeCredentialData:securely:error:]_block_invoke
+ ___LACSLogPassword_block_invoke
+ ___assert_rtn
+ ___block_descriptor_40_e8_32r_e13_v24?0r^v8Q16lr32l8
+ ___block_descriptor_48_e8_32s40r_e26_B24?0^{__ACMHandle=}8^16ls32l8r40l8
+ ___block_descriptor_49_e8_32s40s_e26_B24?0^{__ACMHandle=}8^16ls32l8s40l8
+ ___block_literal_global.7
+ ___chkstk_darwin
+ ___memcpy_chk
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy0_1
+ ___swift_noop_void_return
+ ___swift_reflection_version
+ __allocatedMem.0
+ __allocatedMem.2
+ __allocatedMem.3
+ __logLevel
+ __os_log_default
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_LocalAuthenticationCredentialServices
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_LocalAuthenticationCredentialServices
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_LocalAuthenticationCredentialServices
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_LocalAuthenticationCredentialServices
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_LocalAuthenticationCredentialServices
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_LocalAuthenticationCredentialServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_LocalAuthenticationCredentialServices
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_reportUnimplementedInitializer
+ _aclRequiresPasscodeInternal
+ _acm_explicit_bzero
+ _acm_get_mem
+ _acm_mem_alloc_data
+ _acm_mem_alloc_info
+ _acm_mem_alloc_typed
+ _acm_mem_free
+ _acm_mem_free_data
+ _acm_mem_free_info
+ _bzero
+ _cc_clear
+ _cc_cmp_safe
+ _ccaes_gcm_decrypt_mode
+ _ccaes_gcm_encrypt_mode
+ _ccgcm_context_size
+ _ccgcm_finalize
+ _ccgcm_init
+ _ccgcm_set_iv
+ _ccgcm_update
+ _cchkdf
+ _ccrng
+ _ccsha256_di
+ _checkCCError
+ _checkParameter
+ _crypto_decryptText
+ _crypto_decryptText_version1
+ _crypto_decryptText_version2
+ _crypto_deriveKeyAndDecryptData
+ _crypto_deriveKeyAndEncryptData
+ _crypto_encryptText
+ _crypto_encryptText_version1
+ _crypto_encryptText_version2
+ _crypto_encryptedTextLength
+ _crypto_generateKey
+ _crypto_generateKeyFromSharedInfo
+ _crypto_generateRandomSaltLazily
+ _crypto_plainTextLength
+ _deserializeParameters
+ _flat unique So11LACSContext_p
+ _gACMLoggingLevel
+ _generateRandom
+ _getLengthOfParameters
+ _getRequirementDataSizeForVersion
+ _getRequirementDataSizeForVersion.cold.1
+ _getRequirementDataSizeForVersion.cold.2
+ _init
+ _ioKitTransport
+ _kIOMasterPortDefault
+ _mach_task_self_
+ _malloc_type_calloc
+ _memcmp
+ _memcpy
+ _memset_s
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_msgSend$_decryptData:seed:externalizedContext:error:
+ _objc_msgSend$_encryptData:seed:externalizedContext:error:
+ _objc_msgSend$_encryptionSeedForContext:error:
+ _objc_msgSend$_withContext:error:
+ _objc_msgSend$bytes
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$errorWithCode:debugDescription:
+ _objc_msgSend$init
+ _objc_msgSend$init:
+ _objc_msgSend$initWithACMContextRef:ownsContextRef:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithContextRef:error:
+ _objc_msgSend$initWithData:contextRef:error:
+ _objc_msgSend$length
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$stringWithFormat:
+ _objc_opt_self
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x28
+ _performCommand
+ _platform_rng.state
+ _printf
+ _processAclCommandInternal
+ _putchar
+ _serializeParameters
+ _strlen
+ _strnlen
+ _swift_bridgeObjectRelease
+ _swift_deallocPartialClassInstance
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isaMask
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 37LocalAuthenticationCredentialServices12LACSPasswordC
+ _symbolic _____ 37LocalAuthenticationCredentialServices21LACSUnmanagedPasswordC
+ _symbolic _____ 37LocalAuthenticationCredentialServices7LACSLogO
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic ______p So11LACSContextP
+ _updateLogLevelFromKext
+ _updateLogLevelFromKext.cold.1
+ _verifyAclConstraintForOperationCommandInternal
+ _verifyAclConstraintInternal
- +[LACSCredential supportsSecureCoding]
- +[LACSExtractableCredential supportsSecureCoding]
- +[LACSExtractablePassword supportsSecureCoding]
- +[LACSPassword supportsSecureCoding]
- +[LACSSecureCredential supportsSecureCoding]
- +[LACSSecurePassword supportsSecureCoding]
- -[LACSContext fetchCredentialUUID:]
- -[LACSContext fetchCredentialUUID:].cold.1
- -[LACSContext storeCredentialUUID:error:]
- -[LACSContext storeCredentialUUID:error:].cold.1
- -[LACSCredential .cxx_destruct]
- -[LACSCredential contextRef]
- -[LACSCredential encodeWithCoder:]
- -[LACSCredential initWithCoder:]
- -[LACSCredential initWithUUID:password:]
- -[LACSCredential password]
- -[LACSCredential uuid]
- -[LACSExtractableCredential .cxx_destruct]
- -[LACSExtractableCredential contextRef]
- -[LACSExtractableCredential credential]
- -[LACSExtractableCredential encodeWithCoder:]
- -[LACSExtractableCredential initWithCoder:]
- -[LACSExtractableCredential initWithCredential:]
- -[LACSExtractableCredential initWithCredential:password:]
- -[LACSExtractableCredential initWithUUID:password:error:]
- -[LACSExtractableCredential password]
- -[LACSExtractableCredential secureCopy]
- -[LACSExtractableCredential uuid]
- -[LACSExtractablePassword .cxx_destruct]
- -[LACSExtractablePassword contextRef]
- -[LACSExtractablePassword data:]
- -[LACSExtractablePassword data]
- -[LACSExtractablePassword encodeWithCoder:]
- -[LACSExtractablePassword initWithCoder:]
- -[LACSExtractablePassword initWithData:error:]
- -[LACSExtractablePassword initWithPassword:]
- -[LACSExtractablePassword password]
- -[LACSExtractablePassword secureCopy]
- -[LACSPassword .cxx_destruct]
- -[LACSPassword contextRef]
- -[LACSPassword context]
- -[LACSPassword data:]
- -[LACSPassword encodeWithCoder:]
- -[LACSPassword initWithCoder:]
- -[LACSPassword initWithContext:]
- -[LACSSecureCredential .cxx_destruct]
- -[LACSSecureCredential contextRef]
- -[LACSSecureCredential credential]
- -[LACSSecureCredential encodeWithCoder:]
- -[LACSSecureCredential initWithCoder:]
- -[LACSSecureCredential initWithCredential:]
- -[LACSSecureCredential initWithCredential:password:]
- -[LACSSecureCredential initWithUUID:password:error:]
- -[LACSSecureCredential password]
- -[LACSSecureCredential uuid]
- -[LACSSecurePassword .cxx_destruct]
- -[LACSSecurePassword contextRef]
- -[LACSSecurePassword encodeWithCoder:]
- -[LACSSecurePassword initWithCoder:]
- -[LACSSecurePassword initWithData:error:]
- -[LACSSecurePassword initWithPassword:]
- -[LACSSecurePassword password]
- GCC_except_table11
- _OBJC_CLASS_$_LACSCredential
- _OBJC_CLASS_$_LACSPassword
- _OBJC_IVAR_$_LACSCredential._password
- _OBJC_IVAR_$_LACSCredential._uuid
- _OBJC_IVAR_$_LACSExtractableCredential._credential
- _OBJC_IVAR_$_LACSExtractableCredential._password
- _OBJC_IVAR_$_LACSExtractablePassword._password
- _OBJC_IVAR_$_LACSPassword._context
- _OBJC_IVAR_$_LACSSecureCredential._credential
- _OBJC_IVAR_$_LACSSecureCredential._password
- _OBJC_IVAR_$_LACSSecurePassword._password
- _OBJC_METACLASS_$_LACSCredential
- _OBJC_METACLASS_$_LACSPassword
- __OBJC_$_CLASS_METHODS_LACSCredential
- __OBJC_$_CLASS_METHODS_LACSExtractableCredential
- __OBJC_$_CLASS_METHODS_LACSExtractablePassword
- __OBJC_$_CLASS_METHODS_LACSPassword
- __OBJC_$_CLASS_METHODS_LACSSecureCredential
- __OBJC_$_CLASS_METHODS_LACSSecurePassword
- __OBJC_$_CLASS_PROP_LIST_LACSCredential
- __OBJC_$_CLASS_PROP_LIST_LACSExtractableCredential
- __OBJC_$_CLASS_PROP_LIST_LACSExtractablePassword
- __OBJC_$_CLASS_PROP_LIST_LACSPassword
- __OBJC_$_CLASS_PROP_LIST_LACSSecureCredential
- __OBJC_$_CLASS_PROP_LIST_LACSSecurePassword
- __OBJC_$_INSTANCE_METHODS_LACSCredential
- __OBJC_$_INSTANCE_METHODS_LACSExtractableCredential
- __OBJC_$_INSTANCE_METHODS_LACSExtractablePassword
- __OBJC_$_INSTANCE_METHODS_LACSPassword
- __OBJC_$_INSTANCE_METHODS_LACSSecureCredential
- __OBJC_$_INSTANCE_METHODS_LACSSecurePassword
- __OBJC_$_INSTANCE_VARIABLES_LACSCredential
- __OBJC_$_INSTANCE_VARIABLES_LACSExtractableCredential
- __OBJC_$_INSTANCE_VARIABLES_LACSExtractablePassword
- __OBJC_$_INSTANCE_VARIABLES_LACSPassword
- __OBJC_$_INSTANCE_VARIABLES_LACSSecureCredential
- __OBJC_$_INSTANCE_VARIABLES_LACSSecurePassword
- __OBJC_$_PROP_LIST_LACSCredential
- __OBJC_$_PROP_LIST_LACSExtractableCredential
- __OBJC_$_PROP_LIST_LACSExtractablePassword
- __OBJC_$_PROP_LIST_LACSPassword
- __OBJC_$_PROP_LIST_LACSSecureCredential
- __OBJC_$_PROP_LIST_LACSSecurePassword
- __OBJC_CLASS_PROTOCOLS_$_LACSCredential
- __OBJC_CLASS_PROTOCOLS_$_LACSExtractableCredential
- __OBJC_CLASS_PROTOCOLS_$_LACSExtractablePassword
- __OBJC_CLASS_PROTOCOLS_$_LACSPassword
- __OBJC_CLASS_PROTOCOLS_$_LACSSecureCredential
- __OBJC_CLASS_PROTOCOLS_$_LACSSecurePassword
- __OBJC_CLASS_RO_$_LACSCredential
- __OBJC_CLASS_RO_$_LACSExtractableCredential
- __OBJC_CLASS_RO_$_LACSExtractablePassword
- __OBJC_CLASS_RO_$_LACSPassword
- __OBJC_CLASS_RO_$_LACSSecureCredential
- __OBJC_CLASS_RO_$_LACSSecurePassword
- __OBJC_METACLASS_RO_$_LACSCredential
- __OBJC_METACLASS_RO_$_LACSExtractableCredential
- __OBJC_METACLASS_RO_$_LACSExtractablePassword
- __OBJC_METACLASS_RO_$_LACSPassword
- __OBJC_METACLASS_RO_$_LACSSecureCredential
- __OBJC_METACLASS_RO_$_LACSSecurePassword
- ___30-[LACSPassword initWithCoder:]_block_invoke
- ___35-[LACSContext fetchCredentialUUID:]_block_invoke
- ___36-[LACSSecurePassword initWithCoder:]_block_invoke
- ___41-[LACSContext storeCredentialUUID:error:]_block_invoke
- ___41-[LACSExtractablePassword initWithCoder:]_block_invoke
- ___43-[LACSExtractableCredential initWithCoder:]_block_invoke
- ___block_descriptor_40_e8_32s_e18_"LACSContext"8?0ls32l8
- ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e28_v24?0"NSUUID"8"NSError"16lr32l8r40l8
- _objc_alloc_init
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$context
- _objc_msgSend$credentialsUUIDWithReply:
- _objc_msgSend$decodeObjectOfClass:forKey:
- _objc_msgSend$initWithCredential:
- _objc_msgSend$initWithCredential:password:
- _objc_msgSend$initWithUUID:password:
- _objc_msgSend$setCredentialsUUID:reply:
- _objc_msgSend$storeCredentialUUID:error:
- _objc_opt_class
- _objc_retain_x1
- _objc_retain_x3
CStrings:
+ "#16@0:8"
+ "%02x "
+ "%@"
+ "%s: %s (len=%u): acl:"
+ "%s: %s (len=%u): operation:"
+ "%s: %s: CS[%u] acquired.\n"
+ "%s: %s: CS[%u] created (flags=0x%x).\n"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n"
+ "%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n"
+ "%s: %s: acl = %p, aclLength = %zu.\n"
+ "%s: %s: called.\n"
+ "%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n"
+ "%s: %s: cmd(%u) on CS[%u] -> ok.\n"
+ "%s: %s: command = %u.\n"
+ "%s: %s: constraintState = %p.\n"
+ "%s: %s: context = %p.\n"
+ "%s: %s: log level set to %d.\n"
+ "%s: %s: maxGlobalCredentialAge = %u.\n"
+ "%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n"
+ "%s: %s: operation = %p, operationLength = %zu.\n"
+ "%s: %s: parameters = %p, parameterCount = %u.\n"
+ "%s: %s: requirePasscode = %p.\n"
+ "%s: %s: returning, -> ctx = %p.\n"
+ "%s: %s: returning, err = %ld, code=%u.\n"
+ "%s: %s: returning, err = %ld, var=%u.\n"
+ "%s: %s: returning, err = %ld.\n"
+ "%s: %s: returning.\n"
+ "%{public}@"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "0123456789abcdef"
+ "<data>"
+ "@\"<LACSContext>\""
+ "@\"NSData\""
+ "@\"NSData\"16@0:8"
+ "@\"NSData\"24@0:8^@16"
+ "@\"NSString\"16@0:8"
+ "@\"_TtC37LocalAuthenticationCredentialServices12LACSPassword\""
+ "@\"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword\""
+ "@24@0:8:16"
+ "@28@0:8^{__ACMHandle=}16B24"
+ "@32@0:8:16@24"
+ "@32@0:8^{__ACMHandle=}16^@24"
+ "@40@0:8:16@24@32"
+ "@48@0:8@16@24@32^@40"
+ "ACM"
+ "ACMContextAddCredential"
+ "ACMContextAddCredentialWithScope"
+ "ACMContextContainsCredentialType"
+ "ACMContextContainsCredentialTypeEx"
+ "ACMContextContainsPassphraseCredentialWithPurpose"
+ "ACMContextCopyData"
+ "ACMContextCreateWithExternalForm"
+ "ACMContextCreateWithFlags"
+ "ACMContextCredentialGetPropertyEx"
+ "ACMContextDelete"
+ "ACMContextGetData"
+ "ACMContextGetDataEx"
+ "ACMContextGetDataProperty"
+ "ACMContextGetExternalForm"
+ "ACMContextGetInfo"
+ "ACMContextRemoveCredentialsByType"
+ "ACMContextRemoveCredentialsByTypeAndScope"
+ "ACMContextRemoveCredentialsByValue"
+ "ACMContextRemoveCredentialsByValueAndScope"
+ "ACMContextRemovePassphraseCredentialsByPurposeAndScope"
+ "ACMContextReplacePassphraseCredentialsWithScope"
+ "ACMContextSetData"
+ "ACMContextSetDataEx"
+ "ACMContextVerifyPolicy"
+ "ACMContextVerifyPolicyEx"
+ "ACMContextVerifyPolicyWithPreflight"
+ "ACMCredential"
+ "ACMCredential - ACMCredentialDataAP"
+ "ACMCredential - ACMCredentialDataBiometryMatchAttempted"
+ "ACMCredential - ACMCredentialDataBiometryMatched"
+ "ACMCredential - ACMCredentialDataContinuityUnlock"
+ "ACMCredential - ACMCredentialDataKextDenyList"
+ "ACMCredential - ACMCredentialDataPasscodeValidated"
+ "ACMCredential - ACMCredentialDataPasscodeValidated2"
+ "ACMCredential - ACMCredentialDataPassphraseEntered"
+ "ACMCredential - ACMCredentialDataPassphraseExtractable"
+ "ACMCredential - ACMCredentialDataSecureIntent"
+ "ACMCredential - ACMCredentialDataSignature"
+ "ACMCredential - ACMCredentialDataUserOutputDisplayed"
+ "ACMCredentialGetProperty"
+ "ACMGetAclAuthMethod"
+ "ACMGetEnvironmentVariable"
+ "ACMGlobalContextAddCredential"
+ "ACMGlobalContextCredentialGetProperty"
+ "ACMGlobalContextRemoveCredentialsByType"
+ "ACMGlobalContextVerifyPolicy"
+ "ACMHandleWithPayload"
+ "ACMKernelControl"
+ "ACMLib"
+ "ACMParseAclAndCopyConstraintCharacteristics"
+ "ACMRequirement"
+ "ACMRequirement - ACMRequirementDataAP"
+ "ACMRequirement - ACMRequirementDataAccessGroups"
+ "ACMRequirement - ACMRequirementDataAnd"
+ "ACMRequirement - ACMRequirementDataBiometryMatchAttempted"
+ "ACMRequirement - ACMRequirementDataBiometryMatched"
+ "ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes"
+ "ACMRequirement - ACMRequirementDataKeyRef"
+ "ACMRequirement - ACMRequirementDataKofN"
+ "ACMRequirement - ACMRequirementDataKofNWithAttributes"
+ "ACMRequirement - ACMRequirementDataOr"
+ "ACMRequirement - ACMRequirementDataPasscodeValidated"
+ "ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes"
+ "ACMRequirement - ACMRequirementDataPassphraseEntered"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "ACMRequirement - ACMRequirementDataPushButtonWithAttributes"
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "ACMRequirement - ACMRequirementDataSecureIntent"
+ "ACMRequirement - ACMRequirementDataSecureStateWithAttributes"
+ "ACMRequirement - ACMRequirementDataUserOutputDisplayed"
+ "ACMRequirementGetProperties"
+ "ACMRequirementGetProperty"
+ "ACMRequirementGetSubrequirements"
+ "ACMSetEnvironmentVariable"
+ "ACMSetEnvironmentVariableWithAccessPolicy"
+ "AppleCredentialManager"
+ "B"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B24@?0^{__ACMHandle=}8^@16"
+ "B32@0:8@?16^@24"
+ "B36@0:8@\"NSData\"16B24^@28"
+ "CommonUtil.c"
+ "CredentialServices.Password"
+ "DeallocCredentialList"
+ "DeserializeCredentialList"
+ "DeserializeProcessAcl"
+ "DeserializeVerifyAclConstraint"
+ "DeserializeVerifyPolicy"
+ "Failed to create ACM context"
+ "Failed to create ACM context from context ref"
+ "Failed to create ACM context, status: %d"
+ "Failed to create LACSExtractablePassword: %{public}@"
+ "Failed to create LACSSecurePassword: %{public}@"
+ "Failed to create LACSUnmanagedExtractablePassword with contextRef: %{public}@"
+ "Failed to create LACSUnmanagedExtractablePassword: %{public}@"
+ "Failed to create LACSUnmanagedSecurePassword with contextRef: %{public}@"
+ "Failed to create LACSUnmanagedSecurePassword: %{public}@"
+ "Failed to decrypt data, status: %d"
+ "Failed to encrypt data, status: %d"
+ "Failed to extract data %{public}@"
+ "Failed to get data from ACM context, status: %d"
+ "Failed to get encryption seed, status: %d"
+ "Failed to obtain encryption size, status: %d"
+ "Failed to obtain plain data size, status: %d"
+ "Failed to store data in ACM context, status: %d"
+ "LACSUnmanagedContext"
+ "LACSUnmanagedExtractablePassword"
+ "LACSUnmanagedSecurePassword"
+ "LibCall.c"
+ "LibCall_ACMContexAddCredentialWithScope"
+ "LibCall_ACMContexRemoveCredentialsByTypeAndScope"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMContextCreate"
+ "LibCall_ACMContextCreateWithExternalForm"
+ "LibCall_ACMContextCredentialGetProperty"
+ "LibCall_ACMContextDelete"
+ "LibCall_ACMContextGetData"
+ "LibCall_ACMContextGetInfo"
+ "LibCall_ACMContextLoadFromImage"
+ "LibCall_ACMContextRemoveCredentialsByValueAndScope"
+ "LibCall_ACMContextSetData"
+ "LibCall_ACMContextUnloadToImage"
+ "LibCall_ACMContextUnloadToImage_Block"
+ "LibCall_ACMContextVerifyPolicyAndCopyRequirementEx"
+ "LibCall_ACMContextVerifyPolicyEx"
+ "LibCall_ACMContextVerifyPolicyEx_Block"
+ "LibCall_ACMContextVerifyPolicyWithPreflight_Block"
+ "LibCall_ACMGetAclAuthMethod_Block"
+ "LibCall_ACMGetEnvironmentVariable"
+ "LibCall_ACMGetEnvironmentVariable_Block"
+ "LibCall_ACMGlobalContextCredentialGetProperty"
+ "LibCall_ACMGlobalContextCredentialGetProperty_Block"
+ "LibCall_ACMGlobalContextVerifyPolicyEx"
+ "LibCall_ACMGlobalContextVerifyPolicy_Block"
+ "LibCall_ACMKernDoubleClickNotify"
+ "LibCall_ACMKernelControl"
+ "LibCall_ACMKernelControl_Block"
+ "LibCall_ACMPing"
+ "LibCall_ACMPublishTrustedAccessories"
+ "LibCall_ACMRequirementDelete"
+ "LibCall_ACMSEPControl"
+ "LibCall_ACMSEPControl_Block"
+ "LibCall_ACMSecContextCopyCredentialsArrayEx"
+ "LibCall_ACMSecContextGetUnlockSecret"
+ "LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser"
+ "LibCall_ACMSecSetBiometryAvailability"
+ "LibCall_ACMSecSetBuiltinBiometry"
+ "LibCall_ACMSetEnvironmentVariable"
+ "LibCall_ACMTRMLoadState"
+ "LibCall_ACMTRMLoadState_Block"
+ "LibCall_ACMTRMSaveState"
+ "LibCall_BuildCommand"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "LibSerialization.c"
+ "LocalAuthenticationCredentialServices.LACSExtractableCredential"
+ "LocalAuthenticationCredentialServices.LACSExtractablePassword"
+ "LocalAuthenticationCredentialServices.LACSPassword"
+ "LocalAuthenticationCredentialServices.LACSSecureCredential"
+ "LocalAuthenticationCredentialServices.LACSSecurePassword"
+ "LocalAuthenticationCredentialServices.LACSUnmanagedExtractablePassword"
+ "LocalAuthenticationCredentialServices.LACSUnmanagedPassword"
+ "LocalAuthenticationCredentialServices.LACSUnmanagedSecurePassword"
+ "NO"
+ "NSObject"
+ "NULL"
+ "Q16@0:8"
+ "T#,R"
+ "T@\"<LACSContext>\",N,R,Vcontext"
+ "T@\"LACSExtractablePassword\",N,R,Vpassword"
+ "T@\"LACSSecurePassword\",N,R,Vpassword"
+ "T@\"NSData\",R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSUUID\",N,R"
+ "T@\"_TtC37LocalAuthenticationCredentialServices12LACSPassword\",N,R,Vpassword"
+ "T@\"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword\",N,R,Vpassword"
+ "TB,N,R"
+ "TQ,R"
+ "Util_AllocCredential"
+ "Util_AllocRequirement"
+ "Util_CreateRequirement"
+ "Util_DeallocCredential"
+ "Util_DeallocRequirement"
+ "Util_ReadFromBuffer"
+ "Util_SafeDeallocParameters"
+ "Util_WriteToBuffer"
+ "Util_hexDumpToStrHelper"
+ "Vv16@0:8"
+ "YES"
+ "^{_NSZone=}16@0:8"
+ "^{__ACMHandle=}"
+ "_TtC37LocalAuthenticationCredentialServices12LACSPassword"
+ "_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword"
+ "_contextRef"
+ "_decryptData:seed:externalizedContext:error:"
+ "_encryptData:seed:externalizedContext:error:"
+ "_encryptionSeedForContext:error:"
+ "_externalizedContextRef"
+ "_ownsContextRef"
+ "_withContext:error:"
+ "aclRequiresPasscodeInternal"
+ "acm_mem_alloc_info"
+ "acm_mem_free_info"
+ "acm_transport"
+ "array of ACMCredentialRef"
+ "array of ACMParameter"
+ "autorelease"
+ "bytes"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "checkCCError"
+ "class"
+ "commandCursor == commandBuffer + sizeof(commandBuffer)"
+ "conformsToProtocol:"
+ "crypto_decryptText"
+ "crypto_decryptText_version1"
+ "crypto_decryptText_version2"
+ "crypto_deriveKeyAndDecryptData"
+ "crypto_deriveKeyAndEncryptData"
+ "crypto_encryptText"
+ "crypto_encryptText_version1"
+ "crypto_encryptText_version2"
+ "crypto_generateKey"
+ "crypto_generateKeyFromSharedInfo"
+ "crypto_generateKeyFromSharedInfo_version1"
+ "crypto_generateKeyFromSharedInfo_version2"
+ "crypto_generateRandomSaltLazily"
+ "dataWithBytes:length:"
+ "dataWithLength:"
+ "dealloc"
+ "debugDescription"
+ "description"
+ "deserializeParameters"
+ "dst || !dstCapacity"
+ "false"
+ "generateRandom"
+ "getLengthOfParameters"
+ "getRequirementDataSizeForVersion"
+ "hash"
+ "init()"
+ "init:"
+ "initWithACMContextRef:ownsContextRef:"
+ "initWithBytes:length:"
+ "initWithContextRef:error:"
+ "initWithData:contextRef:error:"
+ "ioKitTransport"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "length"
+ "mutableBytes"
+ "performCommand"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "platform_rng"
+ "processAclCommandInternal"
+ "processAclInternal"
+ "release"
+ "requirement"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "serializeParameters"
+ "src || !srcLen"
+ "stringWithFormat:"
+ "superclass"
+ "updateLogLevelFromKext"
+ "uuidBytes"
+ "v24@?0r^v8Q16"
+ "verifyAclConstraintForOperationCommandInternal"
+ "verifyAclConstraintInternal"
+ "zone"
- "@\"LACSContext\""
- "@\"LACSContext\"8@?0"
- "@\"LACSCredential\""
- "@\"LACSPassword\""
- "@\"NSUUID\""
- "@32@0:8@16@24"
- "B32@0:8@16^@24"
- "Credential UUID fetch failed (err:%@)"
- "Credential UUID storage failed (err:%@)"
- "LACSCredential"
- "LACSPassword"
- "T@\"LACSContext\",R,N,V_context"
- "T@\"LACSCredential\",R,N,V_credential"
- "T@\"LACSExtractablePassword\",R,N,V_password"
- "T@\"LACSPassword\",R,N,V_password"
- "T@\"LACSSecurePassword\",R,N,V_password"
- "T@\"NSUUID\",R,N"
- "T@\"NSUUID\",R,N,V_uuid"
- "_credential"
- "_password"
- "_uuid"
- "credential"
- "credentialsUUIDWithReply:"
- "decodeObjectOfClass:forKey:"
- "fetchCredentialUUID:"
- "initWithCredential:"
- "initWithCredential:password:"
- "initWithUUID:password:"
- "setCredentialsUUID:reply:"
- "storeCredentialUUID:error:"
- "v20@?0B8@\"NSError\"12"
- "v24@?0@\"NSUUID\"8@\"NSError\"16"

```
