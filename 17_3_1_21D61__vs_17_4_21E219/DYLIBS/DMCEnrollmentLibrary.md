## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-3.26.4.1.0
-  __TEXT.__text: 0x1409c
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0xd14
+3.26.5.12.0
+  __TEXT.__text: 0x16c48
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0xeec
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x14df
-  __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__oslogstring: 0x1e50
-  __TEXT.__dlopen_cstrs: 0x10b
-  __TEXT.__unwind_info: 0x450
-  __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methname: 0x491a
-  __TEXT.__objc_methtype: 0x4b6
-  __TEXT.__objc_stubs: 0x3820
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__cstring: 0x1760
+  __TEXT.__gcc_except_tab: 0x3e0
+  __TEXT.__oslogstring: 0x2197
+  __TEXT.__dlopen_cstrs: 0xae
+  __TEXT.__unwind_info: 0x4bc
+  __TEXT.__objc_classname: 0xe5
+  __TEXT.__objc_methname: 0x552c
+  __TEXT.__objc_methtype: 0x553
+  __TEXT.__objc_stubs: 0x4160
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0xb00
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb88
-  __DATA_CONST.__objc_selrefs: 0xef0
-  __DATA_CONST.__objc_arraydata: 0x4d0
-  __AUTH_CONST.__cfstring: 0xd80
-  __AUTH_CONST.__objc_const: 0x48
+  __DATA_CONST.__objc_const: 0xd20
+  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_classrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_arraydata: 0x598
+  __AUTH_CONST.__cfstring: 0xee0
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__objc_intobj: 0x5d0
+  __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__objc_intobj: 0x4f8
-  __AUTH_CONST.__objc_arrayobj: 0x288
-  __AUTH_CONST.__auth_got: 0x280
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x140
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0xcc
+  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xe8
   __DATA.__bss: 0x78
   __DATA_DIRTY.__const: 0x60
   __DATA_DIRTY.__objc_const: 0x1b0

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 375
-  Symbols:   1585
-  CStrings:  951
+  Functions: 434
+  Symbols:   1823
+  CStrings:  1086
 
Symbols:
+ +[DMCEnrollmentFlowController(Utilities) _createEnrollmentNotAllowedDuringSDPError]
+ +[DMCEnrollmentFlowController(Utilities) _createEnterpriseApplicationExistsErrorWithAppName:]
+ +[DMCEnrollmentFlowController(Utilities) _createEnterpriseApplicationMissingEntitlementsError]
+ +[DMCEnrollmentFlowController(Utilities) _createGeneralError]
+ +[DMCEnrollmentFlowController(Utilities) _createGeneralSignInError]
+ +[DMCEnrollmentFlowController(Utilities) _createInvalidCloudConfigError]
+ +[DMCEnrollmentFlowController(Utilities) _createMissingAppleAccountForUserEnrollmentError]
+ +[DMCEnrollmentFlowController(Utilities) _createMissingEnterpriseApplicationBundleIDError]
+ +[DMCEnrollmentFlowController(Utilities) _createMissingEnterpriseApplicationError]
+ +[DMCEnrollmentFlowController(Utilities) _createMissingRMAccountError]
+ +[DMCEnrollmentFlowController(Utilities) _createUnsupportedFeatureError]
+ +[DMCReturnToServiceHelper preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:error:]
+ -[DMCEnrollmentFlowController _analyzeCloudConfig:enrollmentType:isReturnToService:obliterationShelter:]
+ -[DMCEnrollmentFlowController _askForMDMUsernameAndCredential]
+ -[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]
+ -[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]
+ -[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]
+ -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:]
+ -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:username:password:machineInfo:anchorCertificateRefs:]
+ -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:]
+ -[DMCEnrollmentFlowController _handleNeedCredentialsError:]
+ -[DMCEnrollmentFlowController _handleSoftwareUpdateRequiredError:]
+ -[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]
+ -[DMCEnrollmentFlowController _promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:]
+ -[DMCEnrollmentFlowController _restoreSetAsideProfiles]
+ -[DMCEnrollmentFlowController _storeCloudConfig:]
+ -[DMCEnrollmentFlowController _waitForDeviceConfiguration]
+ -[DMCEnrollmentFlowController cloudConfig]
+ -[DMCEnrollmentFlowController continueMacBuddyORGOEnrollmentFlowWithAuthenticationResults:serviceURL:bearerToken:profileData:completionHandler:]
+ -[DMCEnrollmentFlowController expectedBuildVersion]
+ -[DMCEnrollmentFlowController expectedOSVersion]
+ -[DMCEnrollmentFlowController isReturnToService]
+ -[DMCEnrollmentFlowController obliterationShelter]
+ -[DMCEnrollmentFlowController password]
+ -[DMCEnrollmentFlowController setCloudConfig:]
+ -[DMCEnrollmentFlowController setExpectedBuildVersion:]
+ -[DMCEnrollmentFlowController setExpectedOSVersion:]
+ -[DMCEnrollmentFlowController setIsReturnToService:]
+ -[DMCEnrollmentFlowController setObliterationShelter:]
+ -[DMCEnrollmentFlowController setPassword:]
+ -[DMCEnrollmentFlowController setWifiProfileIdentifier:]
+ -[DMCEnrollmentFlowController startInBuddyEnrollmentFlowRestartIfFail:completionHandler:]
+ -[DMCEnrollmentFlowController wifiProfileIdentifier]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_RTS_commonSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_commonSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_deviceEnrollment_legacy_additionalNativeAuth_steps]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_deviceEnrollment_legacy_steps]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_deviceEnrollment_softwareUpdate_steps]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_deviceEnrollment_webURL_steps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_MAID_firstPartSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_MAID_secondPartSteps_default]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_MAID_secondPartSteps_orgToken]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_commonSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_reauthSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_ESSO_firstPartSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_ESSO_secondPartSteps_default]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_ESSO_secondPartSteps_orgToken]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_firstPartSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_secondPartSteps_default]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_secondPartSteps_orgToken]
+ -[DMCEnrollmentFlowController(Sequence) _MDM_SharediPad_commonSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ORGO_MACBuddy_commonSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ORGO_MACBuddy_firstPartSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ORGO_MACBuddy_secondPartSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ORGO_MAIDEnrollmentSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ORGO_commonSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ORGO_deviceEnrollmentSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ORGO_pre_enrollment_steps]
+ -[DMCEnrollmentFlowController(Sequence) _PDUE_UserEnrollment_commonSteps]
+ -[DMCEnrollmentFlowController(Sequence) _Watch_deviceEnrollmentSteps]
+ -[DMCEnrollmentFlowController(Sequence) _commonStepsForEnrollmentType:isReturnToService:]
+ -[DMCEnrollmentFlowController(Sequence) _nameForStep:]
+ -[DMCEnrollmentFlowController(Sequence) _postEnrollmentSteps]
+ -[DMCEnrollmentFlowController(Sequence) _stepsWithUI]
+ -[DMCEnrollmentFlowController(Utilities) _addNotification]
+ -[DMCEnrollmentFlowController(Utilities) _appNameWithBundleID:]
+ -[DMCEnrollmentFlowController(Utilities) _appWithBundleIDExists:]
+ -[DMCEnrollmentFlowController(Utilities) _blockAppInstallsIfNecessary]
+ -[DMCEnrollmentFlowController(Utilities) _blockAppInstalls]
+ -[DMCEnrollmentFlowController(Utilities) _bundleIDsFromAppIDs:]
+ -[DMCEnrollmentFlowController(Utilities) _convertErrorToHumanReadableError:]
+ -[DMCEnrollmentFlowController(Utilities) _errorTranslation]
+ -[DMCEnrollmentFlowController(Utilities) _extractAndVerifyPropertiesFromProfileData:enrollmentMethod:isESSO:essoAppITunesStoreID:error:]
+ -[DMCEnrollmentFlowController(Utilities) _fetchAppAttributesWithITunesItemID:error:]
+ -[DMCEnrollmentFlowController(Utilities) _fetchAppAttributesWithITunesItemID:error:].cold.1
+ -[DMCEnrollmentFlowController(Utilities) _fetchAppAttributesWithITunesItemID:error:].cold.2
+ -[DMCEnrollmentFlowController(Utilities) _guardAgainstConflictingAccountsWithUsername:]
+ -[DMCEnrollmentFlowController(Utilities) _isBYODEnrollment:]
+ -[DMCEnrollmentFlowController(Utilities) _isORGOEnrollment:]
+ -[DMCEnrollmentFlowController(Utilities) _readDirtyStateFromDisk]
+ -[DMCEnrollmentFlowController(Utilities) _receivedApplicationWillTerminateNotification:]
+ -[DMCEnrollmentFlowController(Utilities) _shouldDoReturnToService]
+ -[DMCEnrollmentFlowController(Utilities) _translatedErrorStringForError:]
+ -[DMCEnrollmentFlowController(Utilities) _trustedErrors]
+ -[DMCEnrollmentFlowController(Utilities) _unblockAppInstallsIfNecessaryWithCaller:]
+ -[DMCEnrollmentFlowController(Utilities) _unblockAppInstallsWithCaller:]
+ -[DMCEnrollmentFlowController(Utilities) _updateCredentialForAccount:authTokens:]
+ -[DMCEnrollmentFlowController(Utilities) _validEnrollmentMode:enrollmentMethod:]
+ -[DMCEnrollmentFlowController(Utilities) _writeDirtyStateToDisk:]
+ -[DMCServiceDiscoveryHelper fetchEnrollmentProfileWithServiceURL:username:password:authTokens:enrollmentMethod:machineInfo:anchorCertificateRefs:completionHandler:]
+ GCC_except_table130
+ GCC_except_table135
+ GCC_except_table18
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table73
+ GCC_except_table89
+ GCC_except_table92
+ GCC_except_table98
+ _OBJC_CLASS_$_DMCObliterationShelter
+ _OBJC_CLASS_$_DMCRatchet
+ _OBJC_CLASS_$_DMCReturnToServiceHelper
+ _OBJC_CLASS_$_MDMCloudConfiguration
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._cloudConfig
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._expectedBuildVersion
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._expectedOSVersion
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._isReturnToService
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._obliterationShelter
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._password
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._wifiProfileIdentifier
+ _OBJC_METACLASS_$_DMCReturnToServiceHelper
+ __OBJC_$_CLASS_METHODS_DMCEnrollmentFlowController(Utilities|Sequence)
+ __OBJC_$_CLASS_METHODS_DMCReturnToServiceHelper
+ __OBJC_$_INSTANCE_METHODS_DMCEnrollmentFlowController(Utilities|Sequence)
+ __OBJC_CLASS_RO_$_DMCReturnToServiceHelper
+ __OBJC_METACLASS_RO_$_DMCReturnToServiceHelper
+ ___110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke
+ ___110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke.66
+ ___110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke_2
+ ___110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke_2.67
+ ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.62
+ ___121-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:username:password:machineInfo:anchorCertificateRefs:]_block_invoke
+ ___121-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:username:password:machineInfo:anchorCertificateRefs:]_block_invoke_2
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.80
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.81
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.82
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.83
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.85
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.84
+ ___144-[DMCEnrollmentFlowController continueMacBuddyORGOEnrollmentFlowWithAuthenticationResults:serviceURL:bearerToken:profileData:completionHandler:]_block_invoke
+ ___164-[DMCServiceDiscoveryHelper fetchEnrollmentProfileWithServiceURL:username:password:authTokens:enrollmentMethod:machineInfo:anchorCertificateRefs:completionHandler:]_block_invoke
+ ___164-[DMCServiceDiscoveryHelper fetchEnrollmentProfileWithServiceURL:username:password:authTokens:enrollmentMethod:machineInfo:anchorCertificateRefs:completionHandler:]_block_invoke_2
+ ___192-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:]_block_invoke
+ ___192-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:]_block_invoke_2
+ ___210-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke
+ ___210-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2
+ ___49-[DMCEnrollmentFlowController _storeCloudConfig:]_block_invoke
+ ___53-[DMCEnrollmentFlowController(Sequence) _stepsWithUI]_block_invoke
+ ___55-[DMCEnrollmentFlowController _restoreSetAsideProfiles]_block_invoke
+ ___56-[DMCEnrollmentFlowController(Utilities) _trustedErrors]_block_invoke
+ ___56-[DMCEnrollmentFlowController(Utilities) _trustedErrors]_block_invoke.cold.1
+ ___58-[DMCEnrollmentFlowController _waitForDeviceConfiguration]_block_invoke
+ ___58-[DMCEnrollmentFlowController _waitForDeviceConfiguration]_block_invoke_2
+ ___59-[DMCEnrollmentFlowController(Utilities) _blockAppInstalls]_block_invoke
+ ___59-[DMCEnrollmentFlowController(Utilities) _errorTranslation]_block_invoke
+ ___61-[DMCEnrollmentFlowController(Sequence) _postEnrollmentSteps]_block_invoke
+ ___62-[DMCEnrollmentFlowController _askForMDMUsernameAndCredential]_block_invoke
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.120
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.121
+ ___72-[DMCEnrollmentFlowController(Utilities) _unblockAppInstallsWithCaller:]_block_invoke
+ ___84-[DMCEnrollmentFlowController(Utilities) _fetchAppAttributesWithITunesItemID:error:]_block_invoke
+ ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke
+ ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.110
+ ___98-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:]_block_invoke
+ ___99-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e31_v28?0"NSData"8B16"NSError"20ls32l8
+ ___block_descriptor_40_e8_32s_e34_v28?0"NSString"8"NSString"16B24ls32l8
+ ___block_descriptor_40_e8_32w_e28_v24?0"NSData"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_41_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_literal_global.132
+ ___block_literal_global.165
+ ___block_literal_global.79
+ ___getAMSMediaTaskPlatformiPadSymbolLoc_block_invoke
+ ___getAMSMediaTaskPlatformiPhoneSymbolLoc_block_invoke
+ ___kCFBooleanFalse
+ __unnamed_array_storage.102
+ __unnamed_array_storage.109
+ __unnamed_array_storage.118
+ __unnamed_array_storage.123
+ __unnamed_array_storage.128
+ __unnamed_array_storage.135
+ __unnamed_array_storage.140
+ __unnamed_array_storage.145
+ __unnamed_array_storage.150
+ __unnamed_array_storage.155
+ __unnamed_array_storage.158
+ __unnamed_array_storage.162
+ __unnamed_array_storage.167
+ __unnamed_array_storage.26
+ __unnamed_array_storage.32
+ __unnamed_array_storage.37
+ __unnamed_array_storage.44
+ __unnamed_array_storage.53
+ __unnamed_array_storage.58
+ __unnamed_array_storage.65
+ __unnamed_array_storage.69
+ __unnamed_array_storage.72
+ __unnamed_array_storage.76
+ __unnamed_array_storage.77
+ __unnamed_array_storage.82
+ __unnamed_array_storage.85
+ __unnamed_array_storage.9
+ __unnamed_array_storage.99
+ _dispatch_after
+ _dispatch_get_global_queue
+ _dispatch_time
+ _getAMSMediaTaskPlatformiPadSymbolLoc.ptr
+ _getAMSMediaTaskPlatformiPhoneSymbolLoc.ptr
+ _kCCAnchorCertificatesKey
+ _kCCCloudConfigurationUICompleteKey
+ _kCCCloudConfigurationWasAppliedKey
+ _kCCConfigurationURLKey
+ _kCCConfigurationWebURLKey
+ _kCCEnrollmentAnchorCertificatesKey
+ _kCCEnrollmentServerKey
+ _kCCEnrollmentURLKey
+ _kCCIsSupervisedKey
+ _kDMCErrorDetailsBuildVersionKey
+ _kDMCErrorDetailsOSVersionKey
+ _kDMCProfileInstallationSourceReturnToService
+ _objc_alloc_init
+ _objc_msgSend$_ADE_commonSteps
+ _objc_msgSend$_ADE_deviceEnrollment_legacy_additionalNativeAuth_steps
+ _objc_msgSend$_ADE_deviceEnrollment_legacy_steps
+ _objc_msgSend$_ADE_deviceEnrollment_softwareUpdate_steps
+ _objc_msgSend$_ADE_deviceEnrollment_webURL_steps
+ _objc_msgSend$_ORGO_pre_enrollment_steps
+ _objc_msgSend$_PDUE_UserEnrollment_commonSteps
+ _objc_msgSend$_analyzeCloudConfig:enrollmentType:isReturnToService:obliterationShelter:
+ _objc_msgSend$_askForMDMUsernameAndCredential
+ _objc_msgSend$_askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:
+ _objc_msgSend$_commonStepsForEnrollmentType:isReturnToService:
+ _objc_msgSend$_createInvalidCloudConfigError
+ _objc_msgSend$_ensureWiFiConnectionWithWiFiProfile:
+ _objc_msgSend$_fetchCloudConfigWithEnrollmentType:isReturnToService:
+ _objc_msgSend$_fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:
+ _objc_msgSend$_fetchEnrollmentProfileFromServiceURL:username:password:machineInfo:anchorCertificateRefs:
+ _objc_msgSend$_fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:
+ _objc_msgSend$_handleNeedCredentialsError:
+ _objc_msgSend$_handleSoftwareUpdateRequiredError:
+ _objc_msgSend$_installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:
+ _objc_msgSend$_promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:
+ _objc_msgSend$_restoreSetAsideProfiles
+ _objc_msgSend$_shouldDoReturnToService
+ _objc_msgSend$_storeCloudConfig:
+ _objc_msgSend$_waitForDeviceConfiguration
+ _objc_msgSend$awaitDeviceConfiguredWithCompletionHandler:
+ _objc_msgSend$clear
+ _objc_msgSend$cloudConfig
+ _objc_msgSend$cloudConfigurationDetails
+ _objc_msgSend$continueMacBuddyORGOEnrollmentFlowWithAuthenticationResults:serviceURL:bearerToken:profileData:completionHandler:
+ _objc_msgSend$currentLocale
+ _objc_msgSend$details
+ _objc_msgSend$ensureNetworkConnectionWithCompletionHandler:
+ _objc_msgSend$expectedBuildVersion
+ _objc_msgSend$expectedOSVersion
+ _objc_msgSend$fetchCloudConfigWithCompletionHandler:
+ _objc_msgSend$fetchEnrollmentProfileWithServiceURL:username:password:authTokens:enrollmentMethod:machineInfo:anchorCertificateRefs:completionHandler:
+ _objc_msgSend$fetchEnrollmentProfileWithWebAuthURL:machineInfo:anchorCertificateRefs:completionHandler:
+ _objc_msgSend$hasConfigFile
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$indexSetWithIndexesInRange:
+ _objc_msgSend$insertObjects:atIndexes:
+ _objc_msgSend$isAuthorizedForOperation:
+ _objc_msgSend$isDeviceConfigured
+ _objc_msgSend$isReturnToService
+ _objc_msgSend$isSupervised
+ _objc_msgSend$isTeslaEnrolled
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$markCloudConfigurationAsUICompleted
+ _objc_msgSend$mdmProfileData
+ _objc_msgSend$obliterationShelter
+ _objc_msgSend$password
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$preserveWithError:
+ _objc_msgSend$requestMDMUsernameAndPasswordWithCompletionHandler:
+ _objc_msgSend$requestSoftwareUpdateWithOSVersion:buildVersion:completionHandler:
+ _objc_msgSend$requestUserConsentWithCloudConfig:completionHandler:
+ _objc_msgSend$restoreSetAsideCloudConfigAndProfilesWithCompletionHandler:
+ _objc_msgSend$retrieveWithError:
+ _objc_msgSend$setAdditionalPlatforms:
+ _objc_msgSend$setCloudConfig:
+ _objc_msgSend$setCloudConfigurationDetails:
+ _objc_msgSend$setExpectedBuildVersion:
+ _objc_msgSend$setExpectedOSVersion:
+ _objc_msgSend$setIsReturnToService:
+ _objc_msgSend$setIsSupervised:
+ _objc_msgSend$setLanguageStrings:
+ _objc_msgSend$setLocaleString:
+ _objc_msgSend$setMdmProfileData:
+ _objc_msgSend$setObliterationShelter:
+ _objc_msgSend$setPassword:
+ _objc_msgSend$setWifiProfileData:
+ _objc_msgSend$setWifiProfileIdentifier:
+ _objc_msgSend$shouldSimulateDEPCommunication
+ _objc_msgSend$showAwaitingDeviceConfigurationScene
+ _objc_msgSend$showFetchingCloudConfigurationScene
+ _objc_msgSend$simulatedCloudConfigProfile
+ _objc_msgSend$simulatedMDMEnrollmentProfile
+ _objc_msgSend$storeCloudConfig:completionHandler:
+ _objc_msgSend$userInfo
+ _objc_msgSend$wifiProfileData
+ _objc_msgSend$wifiProfileIdentifier
- +[DMCEnrollmentFlowController _createEnrollmentNotAllowedDuringSDPError]
- +[DMCEnrollmentFlowController _createEnterpriseApplicationExistsErrorWithAppName:]
- +[DMCEnrollmentFlowController _createEnterpriseApplicationMissingEntitlementsError]
- +[DMCEnrollmentFlowController _createGeneralError]
- +[DMCEnrollmentFlowController _createGeneralSignInError]
- +[DMCEnrollmentFlowController _createMissingAppleAccountForUserEnrollmentError]
- +[DMCEnrollmentFlowController _createMissingEnterpriseApplicationBundleIDError]
- +[DMCEnrollmentFlowController _createMissingEnterpriseApplicationError]
- +[DMCEnrollmentFlowController _createMissingRMAccountError]
- +[DMCEnrollmentFlowController _createUnsupportedFeatureError]
- -[DMCEnrollmentFlowController _ADxE_MAID_firstPartSteps]
- -[DMCEnrollmentFlowController _ADxE_MAID_secondPartSteps_default]
- -[DMCEnrollmentFlowController _ADxE_MAID_secondPartSteps_orgToken]
- -[DMCEnrollmentFlowController _ADxE_commonSteps]
- -[DMCEnrollmentFlowController _ADxE_reauthSteps]
- -[DMCEnrollmentFlowController _ADxE_thirdParty_ESSO_firstPartSteps]
- -[DMCEnrollmentFlowController _ADxE_thirdParty_ESSO_secondPartSteps_default]
- -[DMCEnrollmentFlowController _ADxE_thirdParty_ESSO_secondPartSteps_orgToken]
- -[DMCEnrollmentFlowController _ADxE_thirdParty_firstPartSteps]
- -[DMCEnrollmentFlowController _ADxE_thirdParty_secondPartSteps_default]
- -[DMCEnrollmentFlowController _ADxE_thirdParty_secondPartSteps_orgToken]
- -[DMCEnrollmentFlowController _MDM_SharediPad_commonSteps]
- -[DMCEnrollmentFlowController _MDM_UserEnrollment_commonSteps]
- -[DMCEnrollmentFlowController _ORGO_MACBuddy_commonSteps]
- -[DMCEnrollmentFlowController _ORGO_MACBuddy_firstPartSteps]
- -[DMCEnrollmentFlowController _ORGO_MACBuddy_secondPartSteps]
- -[DMCEnrollmentFlowController _ORGO_MAIDEnrollmentSteps]
- -[DMCEnrollmentFlowController _ORGO_commonSteps]
- -[DMCEnrollmentFlowController _ORGO_deviceEnrollmentSteps]
- -[DMCEnrollmentFlowController _Watch_deviceEnrollmentSteps]
- -[DMCEnrollmentFlowController _addNotification]
- -[DMCEnrollmentFlowController _appNameWithBundleID:]
- -[DMCEnrollmentFlowController _appWithBundleIDExists:]
- -[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:]
- -[DMCEnrollmentFlowController _blockAppInstallsIfNecessary]
- -[DMCEnrollmentFlowController _blockAppInstalls]
- -[DMCEnrollmentFlowController _bundleIDsFromAppIDs:]
- -[DMCEnrollmentFlowController _commonStepsForEnrollmentType:]
- -[DMCEnrollmentFlowController _convertErrorToHumanReadableError:]
- -[DMCEnrollmentFlowController _errorTranslation]
- -[DMCEnrollmentFlowController _extractAndVerifyPropertiesFromProfileData:enrollmentMethod:isESSO:essoAppITunesStoreID:error:]
- -[DMCEnrollmentFlowController _fetchAppAttributesWithITunesItemID:error:]
- -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:]
- -[DMCEnrollmentFlowController _guardAgainstConflictingAccountsWithUsername:]
- -[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:enrollmentType:]
- -[DMCEnrollmentFlowController _isBYODEnrollment:]
- -[DMCEnrollmentFlowController _isORGOEnrollment:]
- -[DMCEnrollmentFlowController _nameForStep:]
- -[DMCEnrollmentFlowController _postEnrollmentSteps]
- -[DMCEnrollmentFlowController _readDirtyStateFromDisk]
- -[DMCEnrollmentFlowController _receivedApplicationWillTerminateNotification:]
- -[DMCEnrollmentFlowController _stepsWithUI]
- -[DMCEnrollmentFlowController _translatedErrorStringForError:]
- -[DMCEnrollmentFlowController _trustedErrors]
- -[DMCEnrollmentFlowController _unblockAppInstallsIfNecessaryWithCaller:]
- -[DMCEnrollmentFlowController _unblockAppInstallsWithCaller:]
- -[DMCEnrollmentFlowController _updateCredentialForAccount:authTokens:]
- -[DMCEnrollmentFlowController _validEnrollmentMode:enrollmentMethod:]
- -[DMCEnrollmentFlowController _writeDirtyStateToDisk:]
- GCC_except_table104
- GCC_except_table109
- GCC_except_table112
- GCC_except_table118
- GCC_except_table139
- GCC_except_table159
- GCC_except_table181
- GCC_except_table58
- GCC_except_table61
- GCC_except_table66
- GCC_except_table69
- GCC_except_table72
- GCC_except_table82
- GCC_except_table87
- GCC_except_table90
- GCC_except_table93
- GCC_except_table96
- GCC_except_table99
- _LocalAuthenticationLibraryCore.frameworkLibrary
- __OBJC_$_CLASS_METHODS_DMCEnrollmentFlowController
- __OBJC_$_INSTANCE_METHODS_DMCEnrollmentFlowController
- ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.188
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.204
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.205
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.206
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.207
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.209
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.208
- ___144-[DMCEnrollmentFlowController continueMacBuddyORGOEnrollmentFlowWithAuthentiactionResults:serviceURL:bearerToken:profileData:completionHandler:]_block_invoke
- ___146-[DMCServiceDiscoveryHelper fetchEnrollmentProfileWithServiceURL:authTokens:enrollmentMethod:machineInfo:anchorCertificateRefs:completionHandler:]_block_invoke
- ___170-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:enrollmentType:]_block_invoke
- ___170-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:enrollmentType:]_block_invoke_2
- ___174-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:]_block_invoke
- ___174-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:]_block_invoke_2
- ___43-[DMCEnrollmentFlowController _stepsWithUI]_block_invoke
- ___45-[DMCEnrollmentFlowController _trustedErrors]_block_invoke
- ___45-[DMCEnrollmentFlowController _trustedErrors]_block_invoke.cold.1
- ___48-[DMCEnrollmentFlowController _blockAppInstalls]_block_invoke
- ___48-[DMCEnrollmentFlowController _errorTranslation]_block_invoke
- ___51-[DMCEnrollmentFlowController _postEnrollmentSteps]_block_invoke
- ___61-[DMCEnrollmentFlowController _unblockAppInstallsWithCaller:]_block_invoke
- ___73-[DMCEnrollmentFlowController _fetchAppAttributesWithITunesItemID:error:]_block_invoke
- ___80-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:]_block_invoke
- ___80-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:]_block_invoke_2
- ___LocalAuthenticationLibraryCore_block_invoke
- ___block_literal_global.144
- ___block_literal_global.362
- ___block_literal_global.402
- ___block_literal_global.451
- ___getLARatchetManagerClass_block_invoke
- ___getLARatchetManagerClass_block_invoke.cold.1
- __unnamed_array_storage.100
- __unnamed_array_storage.107
- __unnamed_array_storage.114
- __unnamed_array_storage.117
- __unnamed_array_storage.124
- __unnamed_array_storage.129
- __unnamed_array_storage.134
- __unnamed_array_storage.137
- __unnamed_array_storage.141
- __unnamed_array_storage.146
- __unnamed_array_storage.364
- __unnamed_array_storage.388
- __unnamed_array_storage.399
- __unnamed_array_storage.46
- __unnamed_array_storage.49
- __unnamed_array_storage.52
- __unnamed_array_storage.57
- __unnamed_array_storage.66
- __unnamed_array_storage.71
- __unnamed_array_storage.84
- __unnamed_array_storage.87
- __unnamed_array_storage.97
- _audit_stringLocalAuthentication
- _getLARatchetManagerClass
- _getLARatchetManagerClass.softClass
- _kESSOApplicationEntitlement
- _objc_msgSend$_MDM_UserEnrollment_commonSteps
- _objc_msgSend$_askForUserConsentWithProfileData:managedAppleID:
- _objc_msgSend$_commonStepsForEnrollmentType:
- _objc_msgSend$_fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:
- _objc_msgSend$_installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:enrollmentType:
- _objc_msgSend$isFeatureEnabled
- _objc_msgSend$sharedInstance
- _objc_msgSend$simulatedMDMAccountDrivenEnrollmentProfile
CStrings:
+ "\x15\x12\x12\x13\x1f\a"
+ "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:username:password:machineInfo:anchorCertificateRefs:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _waitForDeviceConfiguration]_block_invoke_2"
+ "@\"DMCObliterationShelter\""
+ "@28@0:8Q16B24"
+ "@40@0:8@16@24^@32"
+ "AMSMediaTaskPlatformiPad"
+ "AMSMediaTaskPlatformiPhone"
+ "AnalyzeCloudConfig"
+ "AnalyzeServerInformation"
+ "AwaitDeviceConfiguration"
+ "Cloud config doesn't require an enrollment."
+ "Cloud config has Web URL"
+ "Cloud config has no configuration URL. But we are doing Return to Service!"
+ "Cloud config has traditional configuration URL."
+ "DMCReturnToServiceHelper"
+ "DMC_INVALID_CLOUD_CONFIG"
+ "Device has local Cloud Config profile from Return to Service, restoring..."
+ "Doing RRTS on non-ADE enrolled device, need to preserve the cloud config"
+ "Enrollment type ADE is not supported!"
+ "EnsureWiFiConnection"
+ "Failed to install WiFi profile: %{public}@"
+ "Failed to restore set aside profiles with error: %{public}@"
+ "Failed to store cloud config. Error: %{public}@"
+ "Failed to trigger software update due to error: %{public}@"
+ "FetchCloudConfig"
+ "FetchEnrollmentProfileWithCredential"
+ "FetchEnrollmentProfileWithWebURL"
+ "No cloud config to store. Skipping..."
+ "No need to ask for consent during Return to Service"
+ "Nothing to restore, continue..."
+ "PromptForMDMUsernameAndCredential"
+ "PromptForSoftwareUpdate"
+ "RestoreSetAsideProfiles"
+ "Return to Service: Does not support webURL!"
+ "Return to Service: Has local MDM profile."
+ "Sequence"
+ "Starting Return to Service Enrollment..."
+ "Starting in Buddy Enrollment..."
+ "StoreCloudConfig"
+ "Supervision state has changed, continue as non-RTS flow."
+ "T@\"DMCObliterationShelter\",&,N,V_obliterationShelter"
+ "T@\"NSDictionary\",&,N,V_cloudConfig"
+ "T@\"NSString\",&,N,V_expectedBuildVersion"
+ "T@\"NSString\",&,N,V_expectedOSVersion"
+ "T@\"NSString\",&,N,V_password"
+ "T@\"NSString\",&,N,V_wifiProfileIdentifier"
+ "TB,N,V_isReturnToService"
+ "Utilities"
+ "WiFi profile installation canceled"
+ "WiFi profile installed"
+ "_ADE_RTS_commonSteps"
+ "_ADE_commonSteps"
+ "_ADE_deviceEnrollment_legacy_additionalNativeAuth_steps"
+ "_ADE_deviceEnrollment_legacy_steps"
+ "_ADE_deviceEnrollment_softwareUpdate_steps"
+ "_ADE_deviceEnrollment_webURL_steps"
+ "_ORGO_pre_enrollment_steps"
+ "_PDUE_UserEnrollment_commonSteps"
+ "_analyzeCloudConfig:enrollmentType:isReturnToService:obliterationShelter:"
+ "_askForMDMUsernameAndCredential"
+ "_askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:"
+ "_cloudConfig"
+ "_commonStepsForEnrollmentType:isReturnToService:"
+ "_createInvalidCloudConfigError"
+ "_ensureWiFiConnectionWithWiFiProfile:"
+ "_expectedBuildVersion"
+ "_expectedOSVersion"
+ "_fetchCloudConfigWithEnrollmentType:isReturnToService:"
+ "_fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:"
+ "_fetchEnrollmentProfileFromServiceURL:username:password:machineInfo:anchorCertificateRefs:"
+ "_fetchEnrollmentProfileFromWebURL:machineInfo:anchorCertificateRefs:"
+ "_handleNeedCredentialsError:"
+ "_handleSoftwareUpdateRequiredError:"
+ "_installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:"
+ "_isReturnToService"
+ "_obliterationShelter"
+ "_password"
+ "_promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:"
+ "_restoreSetAsideProfiles"
+ "_shouldDoReturnToService"
+ "_storeCloudConfig:"
+ "_waitForDeviceConfiguration"
+ "_wifiProfileIdentifier"
+ "awaitDeviceConfiguredWithCompletionHandler:"
+ "clear"
+ "cloudConfig"
+ "cloudConfigurationDetails"
+ "continueMacBuddyORGOEnrollmentFlowWithAuthenticationResults:serviceURL:bearerToken:profileData:completionHandler:"
+ "currentLocale"
+ "details"
+ "ensureNetworkConnectionWithCompletionHandler:"
+ "expectedBuildVersion"
+ "expectedOSVersion"
+ "fetchCloudConfigWithCompletionHandler:"
+ "fetchEnrollmentProfileWithServiceURL:username:password:authTokens:enrollmentMethod:machineInfo:anchorCertificateRefs:completionHandler:"
+ "fetchEnrollmentProfileWithWebAuthURL:machineInfo:anchorCertificateRefs:completionHandler:"
+ "hasConfigFile"
+ "indexOfObject:"
+ "indexSetWithIndexesInRange:"
+ "insertObjects:atIndexes:"
+ "isAuthorizedForOperation:"
+ "isDeviceConfigured"
+ "isReturnToService"
+ "isSupervised"
+ "isTeslaEnrolled"
+ "localeIdentifier"
+ "markCloudConfigurationAsUICompleted"
+ "mdmProfileData"
+ "obliterationShelter"
+ "password"
+ "preferredLanguages"
+ "preserveWithError:"
+ "preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:error:"
+ "requestMDMUsernameAndPasswordWithCompletionHandler:"
+ "requestSoftwareUpdateWithOSVersion:buildVersion:completionHandler:"
+ "requestUserConsentWithCloudConfig:completionHandler:"
+ "restoreSetAsideCloudConfigAndProfilesWithCompletionHandler:"
+ "retrieveWithError:"
+ "setAdditionalPlatforms:"
+ "setCloudConfig:"
+ "setCloudConfigurationDetails:"
+ "setExpectedBuildVersion:"
+ "setExpectedOSVersion:"
+ "setIsReturnToService:"
+ "setIsSupervised:"
+ "setLanguageStrings:"
+ "setLocaleString:"
+ "setMdmProfileData:"
+ "setObliterationShelter:"
+ "setPassword:"
+ "setWifiProfileData:"
+ "setWifiProfileIdentifier:"
+ "shouldSimulateDEPCommunication"
+ "showAwaitingDeviceConfigurationScene"
+ "showFetchingCloudConfigurationScene"
+ "simulatedCloudConfigProfile"
+ "simulatedMDMEnrollmentProfile"
+ "startInBuddyEnrollmentFlowRestartIfFail:completionHandler:"
+ "storeCloudConfig:completionHandler:"
+ "userInfo"
+ "v28@0:8Q16B24"
+ "v28@?0@\"NSData\"8B16@\"NSError\"20"
+ "v28@?0@\"NSString\"8@\"NSString\"16B24"
+ "v44@0:8@16Q24B32@36"
+ "v56@0:8@16@24@32@40@48"
+ "v80@0:8@16@24@32@40Q48@56@64@?72"
+ "v80@0:8@16@24@32@40Q48Q56B64@68B76"
+ "v88@0:8@16@24@32@40B48@52@60@68Q76B84"
+ "wifiProfileData"
+ "wifiProfileIdentifier"
- "\x15\x12\x12\x13\x1f\x01"
- "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:]_block_invoke_2"
- "-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:]_block_invoke_2"
- "ChooseEnrollmentType"
- "Enrollment type is Unknown! returning an empty array for the commonSteps for this enrollment type!"
- "LARatchetManager"
- "Unable to check SDP with LocalAuthentication!"
- "_MDM_UserEnrollment_commonSteps"
- "_askForUserConsentWithProfileData:managedAppleID:"
- "_commonStepsForEnrollmentType:"
- "_fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:"
- "_installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:enrollmentType:"
- "isFeatureEnabled"
- "sharedInstance"
- "simulatedMDMAccountDrivenEnrollmentProfile"
- "softlink:r:path:/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication"
- "v76@0:8@16@24@32@40B48@52@60Q68"
- "v76@0:8@16@24@32@40Q48Q56B64@68"

```
