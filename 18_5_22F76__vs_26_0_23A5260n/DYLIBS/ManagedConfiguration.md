## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2400.5.2.0.0
-  __TEXT.__text: 0xe0508
-  __TEXT.__auth_stubs: 0x1690
-  __TEXT.__objc_methlist: 0xaca4
-  __TEXT.__const: 0x1124
-  __TEXT.__cstring: 0x16011
-  __TEXT.__oslogstring: 0x8582
-  __TEXT.__gcc_except_tab: 0xf6c
+2420.1.1.0.0
+  __TEXT.__text: 0xf7d6c
+  __TEXT.__auth_stubs: 0x1750
+  __TEXT.__objc_methlist: 0xb14c
+  __TEXT.__const: 0x1394
+  __TEXT.__cstring: 0x17bf7
+  __TEXT.__oslogstring: 0x8c67
+  __TEXT.__gcc_except_tab: 0x109c
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x2d00
-  __TEXT.__objc_classname: 0xc51
-  __TEXT.__objc_methname: 0x1cc68
-  __TEXT.__objc_methtype: 0x2149
-  __TEXT.__objc_stubs: 0xd400
-  __DATA_CONST.__got: 0xa48
-  __DATA_CONST.__const: 0x4c78
-  __DATA_CONST.__objc_classlist: 0x3c0
+  __TEXT.__unwind_info: 0x3070
+  __TEXT.__objc_classname: 0xc99
+  __TEXT.__objc_methname: 0x1df92
+  __TEXT.__objc_methtype: 0x2360
+  __TEXT.__objc_stubs: 0xdb80
+  __DATA_CONST.__got: 0xa88
+  __DATA_CONST.__const: 0x4cf0
+  __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x59c8
+  __DATA_CONST.__objc_selrefs: 0x5c90
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0xb58
-  __AUTH_CONST.__const: 0x2250
-  __AUTH_CONST.__cfstring: 0x191c0
-  __AUTH_CONST.__objc_const: 0xd400
+  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH_CONST.__const: 0x2070
+  __AUTH_CONST.__cfstring: 0x19200
+  __AUTH_CONST.__objc_const: 0xd6a8
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x968
-  __DATA.__data: 0xb68
-  __DATA.__bss: 0xc99
+  __AUTH.__objc_data: 0x1220
+  __DATA.__objc_ivar: 0x980
+  __DATA.__data: 0xc20
+  __DATA.__bss: 0xc49
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1400
-  __DATA_DIRTY.__bss: 0x218
+  __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
+  - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9501F43-F86C-3821-9AA1-4225953BA7CE
-  Functions: 5118
-  Symbols:   16428
-  CStrings:  11813
+  UUID: D9D774D2-5E57-3686-B896-D2985D7C532C
+  Functions: 5618
+  Symbols:   17321
+  CStrings:  12187
 
Symbols:
+ +[MCACMContextWrapper contextWrapperForData:ofType:outError:]
+ +[MCACMContextWrapper externalizedContextForSecretData:dataType:outExternalizedContext:outContextRef:]
+ +[MCCrypto copyLeafCertificateFromTrust:]
+ +[MCExtractablePasscodeContextWrapper contextWrapperForExtractablePasscode:outError:]
+ +[MCExtractablePasscodeContextWrapper contextWrapperFromExternalizedContext:outError:]
+ +[MCPasscodeManager characteristicsDictionaryFromPasscodeContext:]
+ +[MCPasscodeManager hashForPasscodeContext:usingMethod:salt:customIterations:]
+ +[MCPasscodeManager passcodeContext:compliesWithPolicyFromRestrictions:checkHistory:outError:]
+ +[MCPasscodeUtilities unlockScreenTypeForPasscodeContext:outSimplePasscodeType:]
+ +[MCSecurePasscodeContextWrapper contextWrapperForSecureSecretData:outError:]
+ +[MCSecurePasscodeContextWrapper credentialSetForPasscode:outError:]
+ -[MCACMContextWrapper .cxx_destruct]
+ -[MCACMContextWrapper contextRef]
+ -[MCACMContextWrapper dealloc]
+ -[MCACMContextWrapper externalizedContext]
+ -[MCACMContextWrapper initWithExternalizedContext:contextRef:shouldDestroyContentsOnDealloc:]
+ -[MCACMContextWrapper shouldDestroyContentsOnDealloc]
+ -[MCDNSSettingsPayload allowFailover]
+ -[MCExtractablePasscodeContextWrapper passcodeExists]
+ -[MCExtractablePasscodeContextWrapper passcodeIsEqualToString:]
+ -[MCExtractablePasscodeContextWrapper passcodeLength]
+ -[MCExtractablePasscodeContextWrapper passcode]
+ -[MCHacks _deviceRegionCode]
+ -[MCPasscodeManager _checkPasscodeContext:againstHistoryWithRestrictions:outError:]
+ -[MCPasscodeManager _publicPasscodeDictSharedDataVolume:]
+ -[MCPasscodeManager passcodeContext:compliesWithPolicyCheckHistory:outError:]
+ -[MCPasscodeManager unlockDeviceWithPasscodeContext:outError:]
+ -[MCPasscodeManager unlockScreenTypeForSharedDataVolume:]
+ -[MCPasscodeManager unlockSimplePasscodeTypeForSharedDataVolume:]
+ -[MCProfileConnection(CloudConfiguration) shouldShowMDMMigrationUI]
+ -[MCProfileConnection(Misc) appsRatingExemptedBundleIDs]
+ -[MCProfileConnection(Misc) createMDMUnlockTokenIfNeededWithPasscodeContext:completionBlock:]
+ -[MCProfileConnection(Misc) deniedICCIDsForImessageFaceTime]
+ -[MCProfileConnection(Misc) deniedICCIDsForRCS]
+ -[MCProfileConnection(Misc) isAccessibilityTypingFeedbackAllowed]
+ -[MCProfileConnection(Misc) isAccountModificationAllowed]
+ -[MCProfileConnection(Misc) isActivationLockAllowedWhileSupervised]
+ -[MCProfileConnection(Misc) setAutoCorrectionAllowed:completion:]
+ -[MCProfileConnection(Misc) setContinuousPathKeyboardAllowed:completion:]
+ -[MCProfileConnection(Misc) setKeyboardShortcutsAllowed:completion:]
+ -[MCProfileConnection(Misc) setPredictiveKeyboardAllowed:completion:]
+ -[MCProfileConnection(Misc) setSmartPunctuationAllowed:completion:]
+ -[MCProfileConnection(Misc) setSpellCheckAllowed:completion:]
+ -[MCProfileConnection(Passcode) changePasscodeWithOldPasscodeContext:newPasscodeContext:outError:]
+ -[MCProfileConnection(Passcode) changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:]
+ -[MCProfileConnection(Passcode) changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:outError:]
+ -[MCProfileConnection(Passcode) changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:skipRecovery:outError:]
+ -[MCProfileConnection(Passcode) clearPasscodeWithEscrowKeybagData:secretContext:outError:]
+ -[MCProfileConnection(Passcode) passcodeContext:meetsCurrentConstraintsOutError:]
+ -[MCProfileConnection(Passcode) unlockDeviceWithPasscodeContext:outError:]
+ -[MCProfileConnection(Passcode) unlockScreenTypeForPasscodeContext:outSimplePasscodeType:]
+ -[MCProfileConnection(Passcode) unlockScreenTypeForSharedDataVolume:OutSimplePasscodeType:]
+ -[MCProfileConnection(Private) _debug_scheduleBackgroundTask:interval:tolerance:completion:]
+ -[MCProfileConnection(Profiles) _setTrustedCodeSigningIdentities:]
+ -[MCProfileConnection(Profiles) addTrustedCodeSigningIdentities:]
+ -[MCProfileConnection(Profiles) removeTrustedCodeSigningIdentities:]
+ -[MCProfileConnection(Profiles) setTrustedCodeSigningIdentities:]
+ -[MCProfileConnection(Profiles) signerIdentityForBundleID:]
+ -[MCProfileConnection(Profiles) syncTrustedCodeSigningIdentitiesWithOutError:]
+ -[MCProfileConnection(Profiles) trustedCodeSigningIdentities]
+ -[MCProfileConnection(Profiles) verifiedTrustedCodeSigningIdentities]
+ -[MCProfileConnection(Restrictions) applyRestrictionDictionary:toSystem:clientType:clientUUID:outError:]
+ -[MCProfileConnection(Restrictions) applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]
+ -[MCProfileConnection(Settings) setAsk:forBoolSetting:configurationUUID:toSystem:user:credentialSet:]
+ -[MCProfileConnection(Settings) setAsk:forBoolSetting:configurationUUID:toSystem:user:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setAsk:forBoolSetting:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:]
+ -[MCProfileConnection(Settings) setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:]
+ -[MCProfileConnection(Settings) setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:]
+ -[MCProfileConnection(Settings) setBoolValue:ask:forSetting:credentialSet:]
+ -[MCProfileConnection(Settings) setBoolValue:ask:forSetting:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setBoolValue:ask:forSetting:toSystem:user:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setBoolValue:forSetting:completion:]
+ -[MCProfileConnection(Settings) setBoolValue:forSetting:credentialSet:]
+ -[MCProfileConnection(Settings) setBoolValue:forSetting:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setBoolValue:forSetting:toSystem:user:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:]
+ -[MCProfileConnection(Settings) setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:errorCompletionBlock:]
+ -[MCProfileConnection(Settings) setParametersForSettingsByType:credentialSet:]
+ -[MCProfileConnection(Settings) setParametersForSettingsByType:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setParametersForSettingsByType:toSystem:user:credentialSet:]
+ -[MCProfileConnection(Settings) setParametersForSettingsByType:toSystem:user:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setValue:forSetting:completion:]
+ -[MCProfileConnection(Settings) setValue:forSetting:credentialSet:]
+ -[MCProfileConnection(Settings) setValue:forSetting:credentialSet:completion:]
+ -[MCProfileConnection(Settings) setValue:forSetting:toSystem:user:credentialSet:]
+ -[MCProfileConnection(Settings) setValues:forIntersectionSetting:completion:]
+ -[MCProfileConnection(Settings) setValues:forIntersectionSetting:toSystem:user:waitUntilCompleted:completion:]
+ -[MCProfileConnection(Settings) setValues:forUnionSetting:completion:]
+ -[MCProfileConnection(Settings) setValues:forUnionSetting:toSystem:user:waitUntilCompleted:completion:]
+ -[MCRelayPayload allowDNSFailover]
+ -[MCRestrictionsPayload _verifyIntersectionMaxCount:forFeature:error:]
+ -[MCRestrictionsPayload _verifyMaxCount:forItems:forFeature:error:]
+ -[MCRestrictionsPayload _verifyUnionMaxCount:forFeature:error:]
+ -[MCSingleAppModeConfiguration allowAccessibilityTypingFeedback]
+ -[MCSingleAppModeConfiguration setAllowAccessibilityTypingFeedback:]
+ -[MCTVRemotePayload _allowedRemotesDescription]
+ -[MCTVRemotePayload _allowedRemotesTitle]
+ -[MCTVRemotePayload _allowedTVsDescription]
+ -[MCTVRemotePayload _allowedTVsTitle]
+ -[MCWiFiPayload allowJoinBeforeFirstUnlock]
+ -[MCWiFiPayload setAllowJoinBeforeFirstUnlock:]
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table280
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table89
+ GCC_except_table99
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
+ _LibCall_ACMSecContextGetUnlockSecret
+ _LibCall_ACMSecContextProcessAcl
+ _LibCall_ACMSecContextProcessAclAndCopyAuthMethod
+ _LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement
+ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
+ _LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser
+ _LibCall_ACMSecSetBiometryAvailability
+ _LibCall_ACMSecSetBuiltinBiometry
+ _LibCall_ACMSetEnvironmentVariable
+ _LibCall_ACMTRMLoadState
+ _LibCall_ACMTRMLoadState_Block
+ _LibCall_ACMTRMSaveState
+ _LibCall_BuildCommand
+ _LibSer_ACMDeserializeEnvironmentVariableType
+ _LibSer_ACMDeserializeSEPControlCode
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
+ _MCConfigurationProfilesSystemGroupContainerNF
+ _MCFeatureAccessibilityTypingFeedbackAllowed
+ _MCFeatureAppsRatingExemptedBundleIDs
+ _MCFeatureDeniedICCIDsForImessageFaceTime
+ _MCFeatureDeniedICCIDsForRCS
+ _MCKeybagCopyEscrowWithContext
+ _MCKeybagCreateMDMEscrowWithPasscodeContext
+ _MCKeybagCreateSupervisionEscrowWithPasscodeContext
+ _MCPostSetupAutoInstallProfilePathNF
+ _MCPostSetupAutoInstallProfilePathNF.cold.1
+ _MCPostSetupAutoInstallProfilePathNF.once
+ _MCPostSetupAutoInstallProfilePathNF.str
+ _MCRapidReturnToServiceNotification
+ _MCSystemProfileLibraryDirectoryNF
+ _MCSystemProfileLibraryDirectoryNF.cold.1
+ _MCSystemProfileLibraryDirectoryNF.once
+ _MCSystemProfileLibraryDirectoryNF.str
+ _MCSystemProfileStorageDirectoryNF
+ _MCSystemProfileStorageDirectoryNF.cold.1
+ _MCSystemProfileStorageDirectoryNF.once
+ _MCSystemProfileStorageDirectoryNF.str
+ _MDMSkipKeyChangedNotification
+ _MKBDeviceSetGracePeriodWithACM
+ _MKBKeyBagCreateEscrowWithACM
+ _MKBSetDeviceConfigurationsWithACM
+ _MKBUnlockDeviceWithACM
+ _OBJC_CLASS_$_DMCMigrationFlowController
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_MCACMContextWrapper
+ _OBJC_CLASS_$_MCExtractablePasscodeContextWrapper
+ _OBJC_CLASS_$_MCSecurePasscodeContextWrapper
+ _OBJC_CLASS_$_MDMOptionsUtilities
+ _OBJC_CLASS_$_UMLManager
+ _OBJC_IVAR_$_MCACMContextWrapper._contextRef
+ _OBJC_IVAR_$_MCACMContextWrapper._externalizedContext
+ _OBJC_IVAR_$_MCACMContextWrapper._shouldDestroyContentsOnDealloc
+ _OBJC_IVAR_$_MCDNSSettingsPayload._allowFailover
+ _OBJC_IVAR_$_MCRelayPayload._allowDNSFailover
+ _OBJC_IVAR_$_MCSingleAppModeConfiguration._allowAccessibilityTypingFeedback
+ _OBJC_IVAR_$_MCWiFiPayload._allowJoinBeforeFirstUnlock
+ _OBJC_METACLASS_$_MCACMContextWrapper
+ _OBJC_METACLASS_$_MCExtractablePasscodeContextWrapper
+ _OBJC_METACLASS_$_MCSecurePasscodeContextWrapper
+ _SecKeyCopyPublicKey
+ _SecKeyCreateRandomKey
+ _SecTrustCopyCertificateChain
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
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_MCACMContextWrapper
+ __OBJC_$_CLASS_METHODS_MCExtractablePasscodeContextWrapper
+ __OBJC_$_CLASS_METHODS_MCSecurePasscodeContextWrapper
+ __OBJC_$_INSTANCE_METHODS_MCACMContextWrapper
+ __OBJC_$_INSTANCE_METHODS_MCExtractablePasscodeContextWrapper
+ __OBJC_$_INSTANCE_VARIABLES_MCACMContextWrapper
+ __OBJC_$_PROP_LIST_MCACMContextWrapper
+ __OBJC_$_PROP_LIST_MCExtractablePasscodeContextWrapper
+ __OBJC_CLASS_RO_$_MCACMContextWrapper
+ __OBJC_CLASS_RO_$_MCExtractablePasscodeContextWrapper
+ __OBJC_CLASS_RO_$_MCSecurePasscodeContextWrapper
+ __OBJC_METACLASS_RO_$_MCACMContextWrapper
+ __OBJC_METACLASS_RO_$_MCExtractablePasscodeContextWrapper
+ __OBJC_METACLASS_RO_$_MCSecurePasscodeContextWrapper
+ ___100-[MCProfileConnection(Misc) defaultAppBundleIDForCommunicationServiceType:forAccountWithIdentifier:]_block_invoke.62
+ ___102+[MCACMContextWrapper externalizedContextForSecretData:dataType:outExternalizedContext:outContextRef:]_block_invoke
+ ___111-[MCProfileConnection(Passcode) changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:]_block_invoke
+ ___111-[MCProfileConnection(Passcode) changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:]_block_invoke.9
+ ___116-[MCProfileConnection(Passcode) changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:skipRecovery:outError:]_block_invoke
+ ___116-[MCProfileConnection(Passcode) changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:skipRecovery:outError:]_block_invoke.11
+ ___140-[MCProfileConnection(Settings) setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:]_block_invoke
+ ___241-[MCProfileConnection(Restrictions) applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]_block_invoke
+ ___241-[MCProfileConnection(Restrictions) applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]_block_invoke.2
+ ___27-[MCProfileConnection init]_block_invoke.35
+ ___47-[MCExtractablePasscodeContextWrapper passcode]_block_invoke
+ ___59-[MCProfileConnection(Profiles) signerIdentityForBundleID:]_block_invoke
+ ___59-[MCProfileConnection(Profiles) signerIdentityForBundleID:]_block_invoke.86
+ ___61-[MCProfileConnection(Misc) setSpellCheckAllowed:completion:]_block_invoke
+ ___65-[MCProfileConnection(Misc) setAutoCorrectionAllowed:completion:]_block_invoke
+ ___67-[MCProfileConnection(Misc) setSmartPunctuationAllowed:completion:]_block_invoke
+ ___68-[MCProfileConnection(Misc) setKeyboardShortcutsAllowed:completion:]_block_invoke
+ ___69-[MCProfileConnection(Misc) setPredictiveKeyboardAllowed:completion:]_block_invoke
+ ___69-[MCProfileConnection(Profiles) verifiedTrustedCodeSigningIdentities]_block_invoke
+ ___69-[MCProfileConnection(Profiles) verifiedTrustedCodeSigningIdentities]_block_invoke.81
+ ___73-[MCProfileConnection(Misc) setContinuousPathKeyboardAllowed:completion:]_block_invoke
+ ___73-[MCProfileConnection(Profiles) provisiongProfileUUIDsForSignerIdentity:]_block_invoke.85
+ ___74-[MCProfileConnection(CloudConfiguration) managingOrganizationInformation]_block_invoke.68
+ ___75-[MCProfileConnection(CloudConfiguration) storedProfileDataWithCompletion:]_block_invoke.49
+ ___75-[MCProfileConnection(Profiles) getAreBundlesBlocked:bundlePaths:outError:]_block_invoke.89
+ ___78-[MCProfileConnection(Profiles) syncTrustedCodeSigningIdentitiesWithOutError:]_block_invoke
+ ___78-[MCProfileConnection(Profiles) syncTrustedCodeSigningIdentitiesWithOutError:]_block_invoke.84
+ ___80-[MCProfileConnection(Profiles) installProfileData:options:interactionDelegate:]_block_invoke.95
+ ___81-[MCProfileConnection(CloudConfiguration) setupAssistantDidFinishWithCompletion:]_block_invoke.61
+ ___81-[MCProfileConnection(CloudConfiguration) setupAssistantDidFinishWithCompletion:]_block_invoke.64
+ ___81-[MCProfileConnection(Profiles) updateProfileWithIdentifier:interactionDelegate:]_block_invoke.96
+ ___90-[MCProfileConnection(Passcode) clearPasscodeWithEscrowKeybagData:secretContext:outError:]_block_invoke
+ ___92-[MCProfileConnection(Profiles) getIsBundleBlocked:bundlePath:outHash:outHashType:outError:]_block_invoke.87
+ ___93-[MCProfileConnection(Misc) createMDMUnlockTokenIfNeededWithPasscodeContext:completionBlock:]_block_invoke
+ ___93-[MCProfileConnection(Passcode) changePasscodeWithRecoveryPasscode:to:skipRecovery:outError:]_block_invoke.10
+ ___MCPostSetupAutoInstallProfilePathNF_block_invoke
+ ___MCSystemProfileLibraryDirectoryNF_block_invoke
+ ___MCSystemProfileStorageDirectoryNF_block_invoke
+ ___assert_rtn
+ ___block_descriptor_40_e8_32r_e13_v24?0r^v8Q16lr32l8
+ ___block_descriptor_40_e8_32r_e27_v24?0"NSSet"8"NSError"16lr32l8
+ ___block_descriptor_48_e8_32s40r_e13_v24?0r^v8Q16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e30_v24?0"NSString"8"NSError"16ls32l8r40l8
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.169
+ ___block_literal_global.103
+ ___block_literal_global.107
+ ___block_literal_global.112
+ ___block_literal_global.117
+ ___block_literal_global.118
+ ___block_literal_global.129
+ ___block_literal_global.134
+ ___block_literal_global.1345
+ ___block_literal_global.1354
+ ___block_literal_global.1356
+ ___block_literal_global.1358
+ ___block_literal_global.139
+ ___block_literal_global.143
+ ___block_literal_global.144
+ ___block_literal_global.148
+ ___block_literal_global.154
+ ___block_literal_global.155
+ ___block_literal_global.159
+ ___block_literal_global.164
+ ___block_literal_global.169
+ ___block_literal_global.171
+ ___block_literal_global.174
+ ___block_literal_global.179
+ ___block_literal_global.191
+ ___block_literal_global.193
+ ___block_literal_global.196
+ ___block_literal_global.201
+ ___block_literal_global.204
+ ___block_literal_global.209
+ ___block_literal_global.214
+ ___block_literal_global.219
+ ___block_literal_global.224
+ ___block_literal_global.228
+ ___block_literal_global.234
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.255
+ ___block_literal_global.256
+ ___block_literal_global.260
+ ___block_literal_global.264
+ ___block_literal_global.265
+ ___block_literal_global.270
+ ___block_literal_global.559
+ ___block_literal_global.57
+ ___block_literal_global.60
+ ___block_literal_global.63
+ ___block_literal_global.64
+ ___block_literal_global.654
+ ___block_literal_global.67
+ ___block_literal_global.671
+ ___block_literal_global.69
+ ___block_literal_global.691
+ ___block_literal_global.73
+ ___block_literal_global.740
+ ___block_literal_global.775
+ ___block_literal_global.78
+ ___block_literal_global.780
+ ___block_literal_global.785
+ ___block_literal_global.790
+ ___block_literal_global.795
+ ___block_literal_global.80
+ ___block_literal_global.88
+ ___block_literal_global.89
+ ___block_literal_global.94
+ ___block_literal_global.99
+ ___credentialSetFromPasscode_block_invoke
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
+ __allocatedMem.0
+ __allocatedMem.2
+ __allocatedMem.3
+ __current_pid
+ __logLevel
+ __merge_dict_cb.cold.2
+ __os_log_default
+ _aclRequiresPasscodeInternal
+ _acm_explicit_bzero
+ _acm_get_mem
+ _acm_mem_alloc_data
+ _acm_mem_alloc_info
+ _acm_mem_alloc_typed
+ _acm_mem_free
+ _acm_mem_free_data
+ _acm_mem_free_info
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
+ _ccaes_gcm_decrypt_mode
+ _ccaes_gcm_encrypt_mode
+ _ccder_sizeof_implicit_raw_octet_string
+ _ccgcm_context_size
+ _ccgcm_finalize
+ _ccgcm_init
+ _ccgcm_set_iv
+ _ccgcm_update
+ _checkCCError
+ _checkParameter
+ _copy_raw_secret
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
+ _deserializeParameters
+ _encode_icsc_params_internal
+ _gACMLoggingLevel
+ _generateRandom
+ _getLengthOfParameters
+ _getRequirementDataSizeForVersion
+ _getRequirementDataSizeForVersion.cold.1
+ _getRequirementDataSizeForVersion.cold.2
+ _get_akslog_context
+ _get_akslog_pid
+ _init
+ _ioKitTransport
+ _kIOMainPortDefault
+ _kMCMDMProfileIdentifierToWiFiRecoveryNetworkPayloadUUIDDependencyKey
+ _kMDMOptionsKey
+ _objc_exception_rethrow
+ _objc_msgSend$_allowedRemotesDescription
+ _objc_msgSend$_allowedRemotesTitle
+ _objc_msgSend$_allowedTVsDescription
+ _objc_msgSend$_allowedTVsTitle
+ _objc_msgSend$_checkPasscodeContext:againstHistoryWithRestrictions:outError:
+ _objc_msgSend$_debug_scheduleBackgroundTask:interval:tolerance:completion:
+ _objc_msgSend$_deviceRegionCode
+ _objc_msgSend$_newZStringWithString:
+ _objc_msgSend$_publicPasscodeDictSharedDataVolume:
+ _objc_msgSend$_setTrustedCodeSigningIdentities:
+ _objc_msgSend$_verifyIntersectionMaxCount:forFeature:error:
+ _objc_msgSend$_verifyMaxCount:forItems:forFeature:error:
+ _objc_msgSend$_verifyUnionMaxCount:forFeature:error:
+ _objc_msgSend$allowAccessibilityTypingFeedback
+ _objc_msgSend$allowDNSFailover
+ _objc_msgSend$allowFailover
+ _objc_msgSend$allowJoinBeforeFirstUnlock
+ _objc_msgSend$applicationState
+ _objc_msgSend$applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:
+ _objc_msgSend$applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:
+ _objc_msgSend$changePasscodeWithOldPasscodeContext:newPasscodeContext:isRecovery:skipRecovery:completion:
+ _objc_msgSend$changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:
+ _objc_msgSend$changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:skipRecovery:outError:
+ _objc_msgSend$characteristicsDictionaryFromPasscodeContext:
+ _objc_msgSend$clearPasscodeWithEscrowKeybagData:secretContext:completion:
+ _objc_msgSend$compatibilityObject
+ _objc_msgSend$contextWrapperForData:ofType:outError:
+ _objc_msgSend$contextWrapperForSecureSecretData:outError:
+ _objc_msgSend$contextWrapperFromExternalizedContext:outError:
+ _objc_msgSend$copyLeafCertificateFromTrust:
+ _objc_msgSend$counterpartIdentifiers
+ _objc_msgSend$createMDMUnlockTokenIfNeededWithPasscodeContext:completion:
+ _objc_msgSend$defaultMDMOptions
+ _objc_msgSend$externalizedContext
+ _objc_msgSend$externalizedContextForSecretData:dataType:outExternalizedContext:outContextRef:
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithExternalizedContext:contextRef:shouldDestroyContentsOnDealloc:
+ _objc_msgSend$initWithValue:localizedKey:
+ _objc_msgSend$keybagOpaqueDataOnSharedDataVolumePath:withError:
+ _objc_msgSend$passcode
+ _objc_msgSend$passcodeContext:compliesWithPolicyCheckHistory:outError:
+ _objc_msgSend$passcodeContext:compliesWithPolicyFromRestrictions:checkHistory:outError:
+ _objc_msgSend$passcodeExists
+ _objc_msgSend$setAsk:forBoolSetting:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:
+ _objc_msgSend$setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:
+ _objc_msgSend$setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:completion:
+ _objc_msgSend$setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:
+ _objc_msgSend$setBoolValue:ask:forSetting:credentialSet:
+ _objc_msgSend$setBoolValue:ask:forSetting:credentialSet:completion:
+ _objc_msgSend$setBoolValue:ask:forSetting:toSystem:user:credentialSet:completion:
+ _objc_msgSend$setBoolValue:forSetting:credentialSet:
+ _objc_msgSend$setBoolValue:forSetting:credentialSet:completion:
+ _objc_msgSend$setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:completion:
+ _objc_msgSend$setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:
+ _objc_msgSend$setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:errorCompletionBlock:
+ _objc_msgSend$setParametersForSettingsByType:credentialSet:
+ _objc_msgSend$setParametersForSettingsByType:toSystem:user:credentialSet:
+ _objc_msgSend$setParametersForSettingsByType:toSystem:user:credentialSet:completion:
+ _objc_msgSend$setValue:forSetting:credentialSet:
+ _objc_msgSend$setValue:forSetting:credentialSet:completion:
+ _objc_msgSend$setValue:forSetting:toSystem:user:credentialSet:
+ _objc_msgSend$setValues:forIntersectionSetting:toSystem:user:waitUntilCompleted:completion:
+ _objc_msgSend$setValues:forUnionSetting:toSystem:user:waitUntilCompleted:completion:
+ _objc_msgSend$shouldShowMDMMigrationUI
+ _objc_msgSend$shouldShowMigrationUI
+ _objc_msgSend$signerIdentityForBundleID:completion:
+ _objc_msgSend$syncTrustedCodeSigningIdentitiesWithCompletion:
+ _objc_msgSend$trustedCodeSigningIdentities
+ _objc_msgSend$trustedCodeSigningIdentitiesWithCompletion:
+ _objc_msgSend$unlockDeviceWithPasscodeContext:outError:
+ _objc_msgSend$unlockScreenTypeForPasscodeContext:outSimplePasscodeType:
+ _objc_msgSend$unlockScreenTypeForSharedDataVolume:
+ _objc_msgSend$unlockSimplePasscodeTypeForSharedDataVolume:
+ _objc_terminate
+ _performCommand
+ _platform_rng.state
+ _processAclCommandInternal
+ _ref_key_create_request_to_class
+ _se_derivation_request_deserialize
+ _se_derivation_request_serialization_len
+ _se_derivation_request_serialize
+ _serializeParameters
+ _set_akslog_context
+ _set_akslog_pid
+ _strnlen
+ _updateLogLevelFromKext
+ _updateLogLevelFromKext.cold.1
+ _verifyAclConstraintForOperationCommandInternal
+ _verifyAclConstraintInternal
+ _vsnprintf
- +[MCLazyInitializationUtilities initAppleIDSSOAuthentication]
- +[MCLazyInitializationUtilities initAuthKit]
- +[MCLazyInitializationUtilities initUserManagement]
- +[MCPasscodeManager defaultNewPasscodeEntrySimplePasscodeType]
- -[MCHacks isGreenTea].cold.1
- -[MCHacks isJapanSKU].cold.1
- -[MCProfileConnection(Misc) setTrustedCodeSigningIdentities:]
- -[MCProfileConnection(Misc) trustedCodeSigningIdentities]
- -[MCProfileConnection(Private) debugRescheduleBackgroundActivity:startDate:gracePeriod:repeatingInterval:]
- -[MCProfileConnection(Profiles) addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:outError:]
- -[MCTimerContext disable]
- -[MCTimerContext enabled]
- -[MCTimerContext init]
- -[MCTimerContext setEnabled:]
- GCC_except_table105
- GCC_except_table108
- GCC_except_table265
- GCC_except_table34
- GCC_except_table50
- GCC_except_table84
- GCC_except_table88
- GCC_except_table91
- GCC_except_table95
- _AppleIDSSOAuthenticationBundle
- _AppleIDSSOAuthenticationBundle.cold.1
- _AppleIDSSOAuthenticationBundle.onceToken
- _AppleIDSSOAuthenticationBundle.retval
- _AppleMediaServicesBundle.onceToken
- _AppleMediaServicesBundle.retval
- _AppleMediaServicesUIBundle.onceToken
- _AppleMediaServicesUIBundle.retval
- _AuthKitBundle.onceToken
- _AuthKitBundle.retval
- _CFDataGetBytes
- _CPGetDeviceRegionCode
- _IOMasterPort
- _IORegistryEntrySearchCFProperty
- _IOServiceNameMatching
- _MCAIDAMutableServiceContextClass
- _MCAIDAServiceOwnersManagerClass
- _MCAIDAServiceTypeCloud
- _MCAKAnisetteProvisioningControllerClass
- _MCAKAnisetteProvisioningControllerClass.cold.1
- _MCAKAuthenticationAlternateDSIDKey
- _MCAKAuthenticationPasswordKey
- _MCAKAuthenticationUsernameKey
- _MCAMSAuthenticateOptionsClass
- _MCAMSAuthenticateOptionsClass.cold.1
- _MCAMSUIAuthenticateTaskClass
- _MCAMSUIAuthenticateTaskClass.cold.1
- _MCIOBluetoothMAC
- _MCIOModelString
- _MCKeybagCopyEscrowWithAuth
- _MCKeybagCreateMDMEscrowWithPasscode
- _MCKeybagCreateSupervisionEscrowWithPasscode
- _MCPostSetupAutoInstallProfilePath
- _MCPostSetupAutoInstallProfilePath.cold.1
- _MCPostSetupAutoInstallProfilePath.once
- _MCPostSetupAutoInstallProfilePath.str
- _MCUMEducationUserSizeKey
- _MCUMUserManagerClass
- _MCUMUserManagerClass.cold.1
- _MCUMUserManagerClass.onceToken
- _MCUMUserManagerClass.theClass
- _MCUMUserManagerErrorDomain
- _MCUMUserSessionProvisionTypeEducation
- _MCUMUserSessionProvisionTypeKey
- _MCUMUserSwitchBlockingTaskClass
- _MCUMUserSwitchBlockingTaskClass.cold.1
- _MCUMUserSwitchBlockingTaskClass.onceToken
- _MCUMUserSwitchBlockingTaskClass.theClass
- _MKBDeviceSetGracePeriod
- _MKBKeyBagCreateEscrowWithAuth
- _MKBSetDeviceConfigurations
- _OBJC_CLASS_$_LSApplicationProxy
- _OBJC_CLASS_$_MCTimerContext
- _OBJC_CLASS_$_MDMClient
- _OBJC_IVAR_$_MCTimerContext._enabled
- _OBJC_METACLASS_$_MCTimerContext
- _OUTLINED_FUNCTION_75
- _SecKeyGeneratePair
- _SecTrustGetCertificateAtIndex
- _UserManagementBundle
- _UserManagementBundle.cold.1
- _UserManagementBundle.onceToken
- _UserManagementBundle.retval
- __AIDAServiceTypeCloud
- __AKAuthenticationAlternateDSIDKey
- __AKAuthenticationPasswordKey
- __AKAuthenticationUsernameKey
- __OBJC_$_INSTANCE_METHODS_MCTimerContext
- __OBJC_$_INSTANCE_VARIABLES_MCTimerContext
- __OBJC_$_PROP_LIST_MCTimerContext
- __OBJC_CLASS_RO_$_MCTimerContext
- __OBJC_METACLASS_RO_$_MCTimerContext
- __UMUserManagerErrorDomain
- ___100-[MCProfileConnection(Misc) defaultAppBundleIDForCommunicationServiceType:forAccountWithIdentifier:]_block_invoke.60
- ___100-[MCProfileConnection(Profiles) addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:outError:]_block_invoke
- ___100-[MCProfileConnection(Profiles) addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:outError:]_block_invoke.78
- ___106-[MCProfileConnection(Private) debugRescheduleBackgroundActivity:startDate:gracePeriod:repeatingInterval:]_block_invoke
- ___232-[MCProfileConnection(Restrictions) applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]_block_invoke
- ___232-[MCProfileConnection(Restrictions) applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]_block_invoke.2
- ___44+[MCLazyInitializationUtilities initAuthKit]_block_invoke
- ___44+[MCLazyInitializationUtilities initAuthKit]_block_invoke_2
- ___51+[MCLazyInitializationUtilities initUserManagement]_block_invoke
- ___51+[MCLazyInitializationUtilities initUserManagement]_block_invoke_2
- ___61+[MCLazyInitializationUtilities initAppleIDSSOAuthentication]_block_invoke
- ___61+[MCLazyInitializationUtilities initAppleIDSSOAuthentication]_block_invoke_2
- ___73-[MCProfileConnection(Profiles) provisiongProfileUUIDsForSignerIdentity:]_block_invoke.79
- ___74-[MCProfileConnection(CloudConfiguration) managingOrganizationInformation]_block_invoke.67
- ___75-[MCProfileConnection(CloudConfiguration) storedProfileDataWithCompletion:]_block_invoke.47
- ___75-[MCProfileConnection(Profiles) getAreBundlesBlocked:bundlePaths:outError:]_block_invoke.83
- ___80-[MCProfileConnection(Profiles) installProfileData:options:interactionDelegate:]_block_invoke.89
- ___81-[MCProfileConnection(CloudConfiguration) setupAssistantDidFinishWithCompletion:]_block_invoke.60
- ___81-[MCProfileConnection(CloudConfiguration) setupAssistantDidFinishWithCompletion:]_block_invoke.63
- ___81-[MCProfileConnection(Profiles) updateProfileWithIdentifier:interactionDelegate:]_block_invoke.90
- ___92-[MCProfileConnection(Profiles) getIsBundleBlocked:bundlePath:outHash:outHashType:outError:]_block_invoke.81
- ___93-[MCProfileConnection(Passcode) changePasscodeWithRecoveryPasscode:to:skipRecovery:outError:]_block_invoke.9
- ___AppleIDSSOAuthenticationBundle_block_invoke
- ___AppleIDSSOAuthenticationBundle_block_invoke_2
- ___AppleMediaServicesBundle_block_invoke
- ___AppleMediaServicesBundle_block_invoke_2
- ___AppleMediaServicesUIBundle_block_invoke
- ___AppleMediaServicesUIBundle_block_invoke_2
- ___AuthKitBundle_block_invoke
- ___AuthKitBundle_block_invoke_2
- ___MCPostSetupAutoInstallProfilePath_block_invoke
- ___MCUMUserManagerClass_block_invoke
- ___MCUMUserSwitchBlockingTaskClass_block_invoke
- ___UserManagementBundle_block_invoke
- ___UserManagementBundle_block_invoke_2
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12ls32l8r40l8r48l8
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.171
- ___block_literal_global.100
- ___block_literal_global.104
- ___block_literal_global.109
- ___block_literal_global.113
- ___block_literal_global.114
- ___block_literal_global.115
- ___block_literal_global.120
- ___block_literal_global.125
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.1339
- ___block_literal_global.1342
- ___block_literal_global.1344
- ___block_literal_global.1346
- ___block_literal_global.137
- ___block_literal_global.142
- ___block_literal_global.157
- ___block_literal_global.158
- ___block_literal_global.162
- ___block_literal_global.163
- ___block_literal_global.167
- ___block_literal_global.172
- ___block_literal_global.173
- ___block_literal_global.177
- ___block_literal_global.182
- ___block_literal_global.192
- ___block_literal_global.194
- ___block_literal_global.207
- ___block_literal_global.211
- ___block_literal_global.212
- ___block_literal_global.217
- ___block_literal_global.222
- ___block_literal_global.227
- ___block_literal_global.231
- ___block_literal_global.237
- ___block_literal_global.239
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.263
- ___block_literal_global.267
- ___block_literal_global.272
- ___block_literal_global.286
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.301
- ___block_literal_global.321
- ___block_literal_global.327
- ___block_literal_global.329
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.335
- ___block_literal_global.337
- ___block_literal_global.339
- ___block_literal_global.341
- ___block_literal_global.343
- ___block_literal_global.345
- ___block_literal_global.347
- ___block_literal_global.349
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.355
- ___block_literal_global.357
- ___block_literal_global.45
- ___block_literal_global.553
- ___block_literal_global.62
- ___block_literal_global.648
- ___block_literal_global.66
- ___block_literal_global.665
- ___block_literal_global.679
- ___block_literal_global.71
- ___block_literal_global.728
- ___block_literal_global.758
- ___block_literal_global.76
- ___block_literal_global.763
- ___block_literal_global.768
- ___block_literal_global.773
- ___block_literal_global.778
- ___block_literal_global.79
- ___block_literal_global.81
- ___block_literal_global.86
- ___block_literal_global.91
- ___block_literal_global.96
- __kUMEducationUserSizeKey
- __kUMUserSessionProvisionTypeEducation
- __kUMUserSessionProvisionTypeKey
- _aks_change_secret_epilogue.cold.1
- _aks_change_secret_opts.cold.1
- _aks_recover_with_escrow_bag.cold.1
- _aks_set_system_with_passcode.cold.1
- _aks_unlock_bag.cold.1
- _der_key_validate
- _der_key_validate.cold.1
- _der_key_validate.cold.2
- _get_aks_log_pid
- _initAppleIDSSOAuthentication.onceToken
- _initAuthKit.onceToken
- _initUserManagement.onceToken
- _kMCCPDeviceIDKey
- _objc_msgSend$addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:completion:
- _objc_msgSend$appState
- _objc_msgSend$applicationProxyForCompanionIdentifier:
- _objc_msgSend$applicationProxyForIdentifier:
- _objc_msgSend$applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:
- _objc_msgSend$debugRescheduleBackgroundActivity:startDate:gracePeriod:repeatingInterval:completion:
- _objc_msgSend$defaultNewPasscodeEntrySimplePasscodeType
- _objc_msgSend$initAppleIDSSOAuthentication
- _objc_msgSend$initAuthKit
- _objc_msgSend$initUserManagement
- _objc_msgSend$memberQueueManagingProfileIdentifier
- _objc_msgSend$setBoolValue:forSetting:toSystem:user:
- _objc_msgSend$setParametersForSettingsByType:passcode:
- _objc_msgSend$setParametersForSettingsByType:toSystem:user:
CStrings:
+ "%02x "
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
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unwrapped DER backup bag%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n"
+ "/.nofollow"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "<data>"
+ "@36@0:8@16I24^@28"
+ "@36@0:8@16^{__ACMHandle=}24B32"
+ "ACM"
+ "ACMContextAddCredential"
+ "ACMContextAddCredentialWithScope"
+ "ACMContextContainsCredentialType"
+ "ACMContextContainsCredentialTypeEx"
+ "ACMContextContainsPassphraseCredentialWithPurpose"
+ "ACMContextCopyData"
+ "ACMContextCreateWithExternalForm"
+ "ACMContextCreateWithFlags"
+ "ACMContextCredentialGetProperty"
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
+ "ALLOW_DNS_FAILOVER"
+ "Allow Failover: %@\n"
+ "AllowDNSFailover"
+ "AllowFailover"
+ "AllowJoinBeforeFirstUnlock"
+ "Allowed"
+ "AppleCredentialManager"
+ "Attempting clearing passcode with escrow keybag context"
+ "Attempting to set grace period to %lu seconds. Passcode context present: %{public}@"
+ "Attempting to set maximum failed passcode attempts to %lu. Passcode context present: %{public}@"
+ "B40@0:8Q16@24^@32"
+ "B48@0:8Q16@24@32^@40"
+ "B52@0:8@16B24@28@36^@44"
+ "B96@0:8@16B24B28@32@40@48@56@64^B72^B80^@88"
+ "Cannot read public passcode metadata for shared data volume: %{public}@"
+ "Change passcode with context error. Error: %{public}@"
+ "Change passcode with recovery passcode context error. Error: %{public}@"
+ "Clear passcode with escrow keybag context error. Error: %{public}@"
+ "Cloud config indicates that the MDM profile is not mandatory"
+ "CommonUtil.c"
+ "Could not generate public/private key pair for CSR: %{public}@"
+ "Couldn't create auth context: ACM err %d"
+ "Couldn't create auth context: ACM error %d"
+ "Couldn't create wrapper context for externalized context"
+ "Couldn't get passcode in auth context: ACM err %d"
+ "Couldn't set secret data for type %d in auth context: ACM err %d"
+ "Couldn't verify input passcode: AKS error %d"
+ "DNS Failover: %@\n"
+ "DNS_SETTINGS_ALLOW_FAILOVER"
+ "DeallocCredentialList"
+ "Deleting ACMContextRef. Should destroy contents: %@"
+ "DeserializeCredentialList"
+ "DeserializeProcessAcl"
+ "DeserializeVerifyAclConstraint"
+ "DeserializeVerifyPolicy"
+ "FEATURE_IMESSAGE_ICCIDS"
+ "FEATURE_RCS_ICCIDS"
+ "FEATURE_SAFARI_HISTORY_CLEARING"
+ "FEATURE_SAFARI_PRIVATE_BROWSING"
+ "Failed to create MDM unlock token with context. Error: %{public}@"
+ "FilterURLs"
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
+ "MCACMContextWrapper"
+ "MCExtractablePasscodeContextWrapper"
+ "MCPasscodeManager failed to unlock device with empty credential set"
+ "MCPasscodeManager successfully unlocked device with credential set."
+ "MCPasscodeManager unlocking device with credential set..."
+ "MCProfileConnection+Profiles XPC failed to get signer identity for bundle ID '%{public}@' with error: %{public}@"
+ "MCProfileConnection+Profiles XPC failed to get trusted code signing identities with error: %{public}@"
+ "MCProfileConnection+Profiles XPC failed to sync trusted code signing identities with error: %{public}@"
+ "MCProfileConnection+Profiles failed to get signer identity for bundle ID '%{public}@' with error: %{public}@"
+ "MCProfileConnection+Profiles failed to get trusted code signing identities with error: %{public}@"
+ "MCProfileConnection+Profiles failed to sync trusted code signing identities with error: %{public}@"
+ "MCSecurePasscodeContextWrapper"
+ "NULL"
+ "Not Allowed"
+ "PASSCODE_ERROR_CANNOT_CREATE_PASSCODE_CONTEXT_WRAPPER"
+ "PASSCODE_ERROR_CANNOT_CREATE_PASSCODE_CONTEXT_WRAPPER_P_CODE"
+ "ProfileIdentifierToRecoveryWiFiPayloadUUID"
+ "Received skip key changed notification"
+ "RegionCode"
+ "T@\"NSData\",R,N,V_externalizedContext"
+ "TB,N,V_allowAccessibilityTypingFeedback"
+ "TB,N,V_allowJoinBeforeFirstUnlock"
+ "TB,R,N,V_allowDNSFailover"
+ "TB,R,N,V_allowFailover"
+ "TB,R,N,V_shouldDestroyContentsOnDealloc"
+ "TQ,R,N"
+ "T^{__ACMHandle=},R,N,V_contextRef"
+ "URLFilterParameters"
+ "Unable to create has for passcode. Error: %@"
+ "Unable to retrieve passcode characteristics. Error: %@"
+ "Util_AllocCredential"
+ "Util_AllocRequirement"
+ "Util_CreateRequirement"
+ "Util_DeallocCredential"
+ "Util_DeallocRequirement"
+ "Util_ReadFromBuffer"
+ "Util_SafeDeallocParameters"
+ "Util_WriteToBuffer"
+ "Util_hexDumpToStrHelper"
+ "WIFI_JOIN_BEFORE_FIRST_UNLOCK"
+ "^{__ACMHandle=}"
+ "^{__ACMHandle=}16@0:8"
+ "^{__SecCertificate=}24@0:8^{__SecTrust=}16"
+ "_aks_backup_enable_volume"
+ "_aks_change_secret_epilogue"
+ "_aks_recover_with_escrow_bag"
+ "_aks_se_get_reset_token_for_memento_secret"
+ "_aks_set_configuration"
+ "_aks_set_system_with_passcode"
+ "_aks_unlock_bag"
+ "_aks_unlock_with_sync_bag"
+ "_allowAccessibilityTypingFeedback"
+ "_allowDNSFailover"
+ "_allowFailover"
+ "_allowJoinBeforeFirstUnlock"
+ "_allowedRemotesDescription"
+ "_allowedRemotesTitle"
+ "_allowedTVsDescription"
+ "_allowedTVsTitle"
+ "_checkPasscodeContext:againstHistoryWithRestrictions:outError:"
+ "_contextRef"
+ "_debug_scheduleBackgroundTask:interval:tolerance:completion:"
+ "_deviceRegionCode"
+ "_externalizedContext"
+ "_newZStringWithString:"
+ "_publicPasscodeDictSharedDataVolume:"
+ "_setTrustedCodeSigningIdentities:"
+ "_shouldDestroyContentsOnDealloc"
+ "_verifyIntersectionMaxCount:forFeature:error:"
+ "_verifyMaxCount:forItems:forFeature:error:"
+ "_verifyUnionMaxCount:forFeature:error:"
+ "aclRequiresPasscodeInternal"
+ "acm_mem_alloc_info"
+ "acm_mem_free_info"
+ "acm_transport"
+ "addTrustedCodeSigningIdentities:"
+ "aks_change_secret_with_kek"
+ "aks_enable_cache_flow"
+ "aks_get_icsc_srp"
+ "aks_reset_iteration_count"
+ "aks_se_get_passcode_derivation"
+ "aks_se_memento_secret_drop"
+ "aks_se_recover_with_acm"
+ "aks_unlock_device_with_acm"
+ "allowAccessibilityTypingFeedback"
+ "allowDNSFailover"
+ "allowFailover"
+ "allowJoinBeforeFirstUnlock"
+ "applicationState"
+ "applyRestrictionDictionary:toSystem:clientType:clientUUID:outError:"
+ "applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:"
+ "applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
+ "appsRatingExemptedBundleIDs"
+ "array of ACMCredentialRef"
+ "array of ACMParameter"
+ "cc_cmp_safe"
+ "ccgcm_finalize"
+ "ccgcm_init"
+ "ccgcm_set_iv"
+ "ccgcm_update"
+ "cchkdf"
+ "ccrng"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:isRecovery:skipRecovery:completion:"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:outError:"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:"
+ "changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:outError:"
+ "changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:skipRecovery:outError:"
+ "characteristicsDictionaryFromPasscodeContext:"
+ "checkCCError"
+ "clearPasscodeWithEscrowKeybagData:secretContext:completion:"
+ "clearPasscodeWithEscrowKeybagData:secretContext:outError:"
+ "com.apple.managedconfiguration.rrts"
+ "commandCursor == commandBuffer + sizeof(commandBuffer)"
+ "compatibilityObject"
+ "contextRef"
+ "contextWrapperForData:ofType:outError:"
+ "contextWrapperForExtractablePasscode:outError:"
+ "contextWrapperForSecureSecretData:outError:"
+ "contextWrapperFromExternalizedContext:outError:"
+ "copyLeafCertificateFromTrust:"
+ "counterpartIdentifiers"
+ "createMDMUnlockTokenIfNeededWithPasscodeContext:completion:"
+ "createMDMUnlockTokenIfNeededWithPasscodeContext:completionBlock:"
+ "credentialSetForPasscode:outError:"
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
+ "deniedICCIDsForImessageFaceTime"
+ "deniedICCIDsForRCS"
+ "deniedICCIDsForiMessageFaceTime"
+ "deserializeParameters"
+ "dst || !dstCapacity"
+ "externalizedContext"
+ "externalizedContextForSecretData:dataType:outExternalizedContext:outContextRef:"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "false"
+ "generateRandom"
+ "getLengthOfParameters"
+ "getRequirementDataSizeForVersion"
+ "hashForPasscodeContext:usingMethod:salt:customIterations:"
+ "i44@0:8@16I24^@28^^{__ACMHandle}36"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithBytes:length:encoding:"
+ "initWithExternalizedContext:contextRef:shouldDestroyContentsOnDealloc:"
+ "ioKitTransport"
+ "isAccessibilityTypingFeedbackAllowed"
+ "isAccountModificationAllowed"
+ "keybagOpaqueDataOnSharedDataVolumePath:withError:"
+ "passcodeContext:compliesWithPolicyCheckHistory:outError:"
+ "passcodeContext:compliesWithPolicyFromRestrictions:checkHistory:outError:"
+ "passcodeContext:meetsCurrentConstraintsOutError:"
+ "passcodeExists"
+ "passcodeIsEqualToString:"
+ "passcodeLength"
+ "performCommand"
+ "platform_rng"
+ "processAclCommandInternal"
+ "processAclInternal"
+ "removeTrustedCodeSigningIdentities:"
+ "requirement"
+ "serializeParameters"
+ "setAllowAccessibilityTypingFeedback:"
+ "setAllowJoinBeforeFirstUnlock:"
+ "setAsk:forBoolSetting:configurationUUID:toSystem:user:credentialSet:"
+ "setAsk:forBoolSetting:configurationUUID:toSystem:user:credentialSet:completion:"
+ "setAsk:forBoolSetting:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:"
+ "setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:"
+ "setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:completion:"
+ "setBoolValue:ask:forSetting:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:"
+ "setBoolValue:ask:forSetting:credentialSet:"
+ "setBoolValue:ask:forSetting:credentialSet:completion:"
+ "setBoolValue:ask:forSetting:toSystem:user:credentialSet:completion:"
+ "setBoolValue:forSetting:completion:"
+ "setBoolValue:forSetting:credentialSet:"
+ "setBoolValue:forSetting:credentialSet:completion:"
+ "setBoolValue:forSetting:toSystem:user:credentialSet:completion:"
+ "setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:completion:"
+ "setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:completion:"
+ "setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:waitUntilCompleted:errorCompletionBlock:"
+ "setParametersForSettingsByType:credentialSet:"
+ "setParametersForSettingsByType:credentialSet:completion:"
+ "setParametersForSettingsByType:toSystem:user:credentialSet:"
+ "setParametersForSettingsByType:toSystem:user:credentialSet:completion:"
+ "setValue:forSetting:completion:"
+ "setValue:forSetting:credentialSet:"
+ "setValue:forSetting:credentialSet:completion:"
+ "setValue:forSetting:toSystem:user:credentialSet:"
+ "setValues:forIntersectionSetting:completion:"
+ "setValues:forIntersectionSetting:toSystem:user:waitUntilCompleted:completion:"
+ "setValues:forUnionSetting:completion:"
+ "setValues:forUnionSetting:toSystem:user:waitUntilCompleted:completion:"
+ "shouldDestroyContentsOnDealloc"
+ "shouldShowMDMMigrationUI"
+ "shouldShowMigrationUI"
+ "signerIdentityForBundleID:"
+ "signerIdentityForBundleID:completion:"
+ "src || !srcLen"
+ "syncTrustedCodeSigningIdentitiesWithCompletion:"
+ "syncTrustedCodeSigningIdentitiesWithOutError:"
+ "trustedCodeSigningIdentitiesWithCompletion:"
+ "unlockDeviceWithPasscodeContext:outError:"
+ "unlockScreenTypeForPasscodeContext:outSimplePasscodeType:"
+ "unlockScreenTypeForSharedDataVolume:"
+ "unlockScreenTypeForSharedDataVolume:OutSimplePasscodeType:"
+ "unlockSimplePasscodeTypeForSharedDataVolume:"
+ "updateLogLevelFromKext"
+ "v24@?0r^v8Q16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v48@0:8@\"NSData\"16@\"NSData\"24B32B36@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSString\"16d24d32@?<v@?@\"NSError\">40"
+ "v48@0:8@16d24d32@?40"
+ "v52@0:8@16@24B32B36B40@?44"
+ "v56@0:8@\"NSDictionary\"16@\"NSString\"24B32B36@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24B32B36@40@?48"
+ "v60@0:8@16@24B32B36@40B48@?52"
+ "v68@0:8B16B20@24@32B40B44@48B56@?60"
+ "v80@0:8@\"NSDictionary\"16B24B28@\"NSArray\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@?<v@?BB@\"NSError\">72"
+ "v80@0:8@16B24B28@32@40@48@56@64@?72"
+ "verifiedTrustedCodeSigningIdentities"
+ "verifyAclConstraintForOperationCommandInternal"
+ "verifyAclConstraintInternal"
- "%02x:%02x:%02x:%02x:%02x:%02x"
- "%@%@"
- "%s%s:%s%s%s%s%u:%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %sdump %s (len = %zd)%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Unwrapped DER backup bag%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s ioreg: %d, boot_arg: %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s overflow%s\n"
- "/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework"
- "/System/Library/PrivateFrameworks/AppleMediaServices.framework"
- "/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework"
- "/System/Library/PrivateFrameworks/AuthKit.framework"
- "/System/Library/PrivateFrameworks/UserManagement.framework"
- "AIDAMutableServiceContext"
- "AIDAServiceOwnersManager"
- "AIDAServiceTypeCloud"
- "AKAnisetteProvisioningController"
- "AKAuthenticationAlternateDSIDKey"
- "AKAuthenticationPasswordKey"
- "AKAuthenticationUsernameKey"
- "AMSAuthenticateOptions"
- "AMSUIAuthenticateTask"
- "Attempting to set grace period to %lu seconds. Passcode present: %{public}@"
- "Attempting to set maximum failed passcode attempts to %lu. Passcode present: %{public}@"
- "Cloud config indicates that the MDM profile is not mandatory or is removable."
- "Could not generate public/private key pair for CSR."
- "IODeviceTree"
- "MCProfileConnection+Profiles XPC failed to add trusted code signing identities for provisioning profile uuid '%{public}@' with error: %{public}@"
- "MCProfileConnection+Profiles failed to add trusted code signing identities for provisioning profile uuid '%{public}@' with error: %{public}@"
- "MCTimerContext"
- "Reschedule background activity error. Error: %{public}@"
- "TB,N,V_enabled"
- "UMUserManager"
- "UMUserManagerErrorDomain"
- "UMUserSwitchBlockingTask"
- "_enabled"
- "addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:completion:"
- "addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:outError:"
- "aks_backup_enable_volume"
- "aks_change_secret_epilogue"
- "aks_change_secret_opts"
- "aks_recover_with_escrow_bag"
- "aks_se_get_reset_token_for_memento_secret"
- "aks_set_configuration"
- "aks_set_system_with_passcode"
- "aks_unlock_bag"
- "aks_unlock_with_sync_bag"
- "appState"
- "applicationProxyForCompanionIdentifier:"
- "applicationProxyForIdentifier:"
- "applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:"
- "bluetooth"
- "debugRescheduleBackgroundActivity:startDate:gracePeriod:repeatingInterval:"
- "debugRescheduleBackgroundActivity:startDate:gracePeriod:repeatingInterval:completion:"
- "defaultNewPasscodeEntrySimplePasscodeType"
- "der_key_validate"
- "disable"
- "enabled"
- "failed to open connection to %s\n"
- "initAppleIDSSOAuthentication"
- "initAuthKit"
- "initUserManagement"
- "kUMEducationUserSizeKey"
- "kUMUserSessionProvisionTypeEducation"
- "kUMUserSessionProvisionTypeKey"
- "local-mac-address"
- "memberQueueManagingProfileIdentifier"
- "model-number"
- "setEnabled:"
- "v48@0:8q16@24@32@40"
- "v56@0:8q16@\"NSDate\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSError\">48"
- "v56@0:8q16@24@32@40@?48"
- "v76@0:8@\"NSDictionary\"16B24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSString\"60@?<v@?BB@\"NSError\">68"
- "v76@0:8@16B24@28@36@44@52@60@?68"

```
