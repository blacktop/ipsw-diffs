## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-55.80.4.0.0
-  __TEXT.__text: 0x2a340
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x1acc
-  __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x3f11
-  __TEXT.__cstring: 0x24b8
-  __TEXT.__gcc_except_tab: 0x9ec
+59.100.16.0.0
+  __TEXT.__text: 0x2d9f0
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0x1c34
+  __TEXT.__const: 0xf8
+  __TEXT.__oslogstring: 0x4282
+  __TEXT.__cstring: 0x25e6
+  __TEXT.__gcc_except_tab: 0xa5c
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x8e8
-  __TEXT.__objc_classname: 0x21b
-  __TEXT.__objc_methname: 0x872a
-  __TEXT.__objc_methtype: 0x9ae
-  __TEXT.__objc_stubs: 0x63a0
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x1320
+  __TEXT.__unwind_info: 0xad0
+  __TEXT.__objc_classname: 0x21c
+  __TEXT.__objc_methname: 0x8c95
+  __TEXT.__objc_methtype: 0x9f5
+  __TEXT.__objc_stubs: 0x6780
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b30
+  __DATA_CONST.__objc_selrefs: 0x1c48
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x480
-  __AUTH_CONST.__auth_got: 0x2e0
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x17c0
-  __AUTH_CONST.__objc_const: 0x1dc0
-  __AUTH_CONST.__objc_intobj: 0x9c0
-  __AUTH_CONST.__objc_arrayobj: 0x450
+  __DATA_CONST.__objc_arraydata: 0x508
+  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x1840
+  __AUTH_CONST.__objc_const: 0x1fa0
+  __AUTH_CONST.__objc_intobj: 0xab0
+  __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x170
+  __DATA.__objc_ivar: 0x198
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D49C5EE9-7B31-332B-8EF3-E6307848F642
-  Functions: 784
-  Symbols:   3040
-  CStrings:  1942
+  UUID: DF21A149-5A43-30FA-9AF3-F104FB035344
+  Functions: 822
+  Symbols:   3154
+  CStrings:  2027
 
Symbols:
+ +[DMCReturnToServiceHelper preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:shouldRetryEnrollment:error:]
+ -[DMCEnrollmentFlowController _ensureNetworkConnection]
+ -[DMCEnrollmentFlowController _installWiFiProfile:]
+ -[DMCEnrollmentFlowController _prepareForReturnToService]
+ -[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateError:]
+ -[DMCEnrollmentFlowController _restartFlow]
+ -[DMCEnrollmentFlowController _workerQueue_cleanupCachedValuesWillRestart:]
+ -[DMCEnrollmentFlowController dynamicRestartInterval]
+ -[DMCEnrollmentFlowController enrollmentFlowMonitorStarted]
+ -[DMCEnrollmentFlowController enrollmentFlowUUID]
+ -[DMCEnrollmentFlowController minimumRestartInterval]
+ -[DMCEnrollmentFlowController restartEnrollmentFlowImmediately]
+ -[DMCEnrollmentFlowController restartInterval]
+ -[DMCEnrollmentFlowController restartScheduled]
+ -[DMCEnrollmentFlowController setDynamicRestartInterval:]
+ -[DMCEnrollmentFlowController setEnrollmentFlowMonitorStarted:]
+ -[DMCEnrollmentFlowController setEnrollmentFlowUUID:]
+ -[DMCEnrollmentFlowController setMinimumRestartInterval:]
+ -[DMCEnrollmentFlowController setRestartInterval:]
+ -[DMCEnrollmentFlowController setRestartScheduled:]
+ -[DMCEnrollmentFlowController setSoftwareUpdateError:]
+ -[DMCEnrollmentFlowController softwareUpdateError]
+ -[DMCEnrollmentFlowController(Sequence) _oneTimeSteps]
+ -[DMCEnrollmentFlowController(Sequence) _oneTimeSteps].cold.1
+ -[DMCEnrollmentFlowController(Utilities) _bottomLevelErrorFromError:]
+ -[DMCEnrollmentFlowController(Utilities) _removeAllNotification]
+ -[DMCEnrollmentFlowControllerBase _workerQueue_cleanupCachedValuesWillRestart:]
+ -[DMCEnrollmentFlowControllerBase executedSteps]
+ -[DMCEnrollmentFlowControllerBase setExecutedSteps:]
+ -[DMCRapidReturnToServiceFlowController _triggerRRTSWithCompletionHandler:]
+ -[DMCRapidReturnToServiceFlowController networkMonitor]
+ -[DMCRapidReturnToServiceFlowController preserveDataPlan]
+ -[DMCRapidReturnToServiceFlowController setNetworkMonitor:]
+ -[DMCRapidReturnToServiceFlowController setPreserveDataPlan:]
+ -[DMCRapidReturnToServiceFlowController setShouldRetryEnrollment:]
+ -[DMCRapidReturnToServiceFlowController shouldRetryEnrollment]
+ -[DMCReturnToServiceHelper shouldRetryEnrollment]
+ GCC_except_table104
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table137
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table149
+ GCC_except_table151
+ GCC_except_table188
+ GCC_except_table19
+ GCC_except_table191
+ GCC_except_table205
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table244
+ GCC_except_table33
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table8
+ GCC_except_table84
+ _DMCMCInstallationErrorDomain
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_DMCNetworkMonitor
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._dynamicRestartInterval
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._enrollmentFlowMonitorStarted
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._enrollmentFlowUUID
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._minimumRestartInterval
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._restartInterval
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._restartScheduled
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._softwareUpdateError
+ _OBJC_IVAR_$_DMCEnrollmentFlowControllerBase._executedSteps
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._networkMonitor
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._preserveDataPlan
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._shouldRetryEnrollment
+ _OUTLINED_FUNCTION_0
+ ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.98
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.112
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.123
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.113
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.124
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_3.117
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.155
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.156
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.157
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.158
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.160
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.159
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke.134
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke.149
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2.140
+ ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2.150
+ ___51-[DMCEnrollmentFlowController _installWiFiProfile:]_block_invoke
+ ___51-[DMCEnrollmentFlowController _installWiFiProfile:]_block_invoke_2
+ ___54-[DMCEnrollmentFlowController(Sequence) _oneTimeSteps]_block_invoke
+ ___55-[DMCEnrollmentFlowController _ensureNetworkConnection]_block_invoke
+ ___55-[DMCEnrollmentFlowController _ensureNetworkConnection]_block_invoke_2
+ ___56-[DMCUnenrollmentFlowController _askForPasscodeIfNeeded]_block_invoke.12
+ ___56-[DMCUnenrollmentFlowController _askForPasscodeIfNeeded]_block_invoke_2.16
+ ___57-[DMCEnrollmentFlowController _prepareForReturnToService]_block_invoke
+ ___57-[DMCEnrollmentFlowController _prepareForReturnToService]_block_invoke_2
+ ___63-[DMCEnrollmentFlowController restartEnrollmentFlowImmediately]_block_invoke
+ ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke.38
+ ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke_2.39
+ ___65-[DMCEnrollmentFlowController _flowTerminatedWithError:canceled:]_block_invoke.37
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke.72
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2.76
+ ___75-[DMCRapidReturnToServiceFlowController _triggerRRTSWithCompletionHandler:]_block_invoke
+ ___75-[DMCRapidReturnToServiceFlowController _triggerRRTSWithCompletionHandler:]_block_invoke.10
+ ___75-[DMCRapidReturnToServiceFlowController _triggerRRTSWithCompletionHandler:]_block_invoke.6
+ ___75-[DMCRapidReturnToServiceFlowController _triggerRRTSWithCompletionHandler:]_block_invoke_2
+ ___75-[DMCRapidReturnToServiceFlowController _triggerRRTSWithCompletionHandler:]_block_invoke_2.11
+ ___75-[DMCRapidReturnToServiceFlowController _triggerRRTSWithCompletionHandler:]_block_invoke_2.8
+ ___79-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateError:]_block_invoke
+ ___79-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateError:]_block_invoke_2
+ ___79-[DMCMigrationFlowController _sendStartMigrationRequestWithPendingCloudConfig:]_block_invoke.28
+ ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.176
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.167
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.170
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.168
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.171
+ ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.205
+ ___block_descriptor_56_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e56_v48?0"NSData"8"NSData"16"NSData"24B32B36"NSError"40ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e29_v24?0"NSArray"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e17_v16?0"NSError"8lw72l8s32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_90_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_literal_global.112
+ ___block_literal_global.180
+ ___block_literal_global.205
+ ___block_literal_global.209
+ ___block_literal_global.210
+ __oneTimeSteps.onceToken
+ __oneTimeSteps.steps
+ _objc_msgSend$_bottomLevelErrorFromError:
+ _objc_msgSend$_ensureNetworkConnection
+ _objc_msgSend$_installWiFiProfile:
+ _objc_msgSend$_oneTimeSteps
+ _objc_msgSend$_prepareForReturnToService
+ _objc_msgSend$_promptForSoftwareUpdateWithSoftwareUpdateError:
+ _objc_msgSend$_removeAllNotification
+ _objc_msgSend$_restartFlow
+ _objc_msgSend$_triggerRRTSWithCompletionHandler:
+ _objc_msgSend$_workerQueue_cleanupCachedValuesWillRestart:
+ _objc_msgSend$deviceMightHaveNetworkStrict:
+ _objc_msgSend$dynamicRestartInterval
+ _objc_msgSend$enrollmentFlowMonitorStarted
+ _objc_msgSend$enrollmentFlowUUID
+ _objc_msgSend$executedSteps
+ _objc_msgSend$installWiFiProfileIfNeeded:completionHandler:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$minimumRestartInterval
+ _objc_msgSend$networkMonitor
+ _objc_msgSend$prepareForReturnToServiceWithCompletionHandler:
+ _objc_msgSend$preserveDataPlan
+ _objc_msgSend$preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:shouldRetryEnrollment:error:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:
+ _objc_msgSend$restartInterval
+ _objc_msgSend$restartScheduled
+ _objc_msgSend$setEnrollmentFlowMonitorStarted:
+ _objc_msgSend$setEnrollmentFlowUUID:
+ _objc_msgSend$setPreserveDataPlan:
+ _objc_msgSend$setRestartInterval:
+ _objc_msgSend$setRestartScheduled:
+ _objc_msgSend$setShouldRetryEnrollment:
+ _objc_msgSend$setSoftwareUpdateError:
+ _objc_msgSend$shouldRetryEnrollment
+ _objc_msgSend$softwareUpdateError
+ _objc_msgSend$trackEndTime
+ _objc_msgSend$underlyingErrors
+ _objc_retainAutoreleasedReturnValue
- +[DMCReturnToServiceHelper preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:]
- -[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]
- -[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]
- -[DMCEnrollmentFlowController _workerQueue_cleanupCachedValues]
- -[DMCEnrollmentFlowController setSoftwareUpdateInfo:]
- -[DMCEnrollmentFlowController softwareUpdateInfo]
- GCC_except_table107
- GCC_except_table112
- GCC_except_table117
- GCC_except_table120
- GCC_except_table126
- GCC_except_table133
- GCC_except_table136
- GCC_except_table139
- GCC_except_table18
- GCC_except_table184
- GCC_except_table187
- GCC_except_table190
- GCC_except_table199
- GCC_except_table204
- GCC_except_table207
- GCC_except_table210
- GCC_except_table31
- GCC_except_table44
- GCC_except_table47
- GCC_except_table52
- GCC_except_table55
- GCC_except_table58
- GCC_except_table65
- GCC_except_table68
- GCC_except_table7
- GCC_except_table71
- GCC_except_table73
- GCC_except_table76
- GCC_except_table96
- _OBJC_IVAR_$_DMCEnrollmentFlowController._softwareUpdateInfo
- ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.90
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.104
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.99
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.100
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.105
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_3.109
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.147
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.148
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.149
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.150
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.152
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.151
- ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke.126
- ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke.141
- ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2.132
- ___259-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2.142
- ___56-[DMCUnenrollmentFlowController _askForPasscodeIfNeeded]_block_invoke.11
- ___56-[DMCUnenrollmentFlowController _askForPasscodeIfNeeded]_block_invoke_2.15
- ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke.35
- ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke_2.36
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.186
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.187
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.188
- ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke.64
- ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2.68
- ___78-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]_block_invoke
- ___78-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]_block_invoke_2
- ___79-[DMCMigrationFlowController _sendStartMigrationRequestWithPendingCloudConfig:]_block_invoke.25
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.10
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.2
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.6
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.11
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.3
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.8
- ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.170
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.159
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.162
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.160
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.163
- ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.200
- ___block_descriptor_48_e8_32bs40w_e33_v28?0"NSString"8B16"NSError"20lw40l8s32l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_descriptor_56_e8_32s40bs_e50_v40?0"NSData"8"NSData"16"NSData"24"NSError"32ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s72l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8
- ___block_literal_global.161
- ___block_literal_global.190
- ___block_literal_global.201
- ___block_literal_global.93
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_ensureWiFiConnectionWithWiFiProfile:
- _objc_msgSend$_promptForSoftwareUpdateWithSoftwareUpdateInfo:
- _objc_msgSend$preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:
- _objc_msgSend$requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:
- _objc_msgSend$setSoftwareUpdateInfo:
- _objc_msgSend$softwareUpdateInfo
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "%s shouldRestart: %d self.hasExecutedUIStep %d self.restartIfFail %d"
+ "("
+ "+[DMCReturnToServiceHelper preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:shouldRetryEnrollment:error:]"
+ "-[DMCEnrollmentFlowController _ensureNetworkConnection]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _flowTerminatedWithError:canceled:]_block_invoke"
+ "-[DMCEnrollmentFlowController _installWiFiProfile:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _prepareForReturnToService]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateError:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController initWithPresenter:managedConfigurationHelper:rmStoreHelper:]"
+ "-[DMCEnrollmentFlowControllerBase _workerQueue_performFlowStep:]"
+ "@\"DMCNetworkMonitor\""
+ "@\"NSMutableSet\""
+ "@\"NSUUID\""
+ "@52@0:8@16@24@32B40^@44"
+ "Cleaning up dirty state... %{public}@"
+ "Enrollment flow UUID has changed. (old: %{public}@, new: %{public}@)"
+ "EnsureNetworkConnection"
+ "Failed to switch to persona %{public}@ for Apple account update: %{public}@"
+ "Failed to switch to persona %{public}@ for RM account enrollment update: %{public}@"
+ "Failed to switch to persona %{public}@ for RM account reauth update: %{public}@"
+ "Failed to switch to persona %{public}@ for RM account update: %{public}@"
+ "Failed to switch to persona %{public}@ for account verification: %{public}@"
+ "Failed to switch to persona %{public}@ for iCloud account update: %{public}@"
+ "Failed to switch to persona %{public}@ for iTunes account update: %{public}@"
+ "InstallWiFiProfile"
+ "MobileAssetAssetAudience"
+ "PrepareForReturnToService"
+ "Restart was handled elsewhere."
+ "Restarting enrollment flow immediately"
+ "Step %{public}@ has been executed. Skipping..."
+ "T@\"DMCNetworkMonitor\",&,N,V_networkMonitor"
+ "T@\"NSError\",&,N,V_softwareUpdateError"
+ "T@\"NSMutableSet\",&,N,V_executedSteps"
+ "T@\"NSUUID\",&,N,V_enrollmentFlowUUID"
+ "TB,N,V_dynamicRestartInterval"
+ "TB,N,V_enrollmentFlowMonitorStarted"
+ "TB,N,V_preserveDataPlan"
+ "TB,N,V_restartScheduled"
+ "TB,N,V_shouldRetryEnrollment"
+ "Td,N,V_minimumRestartInterval"
+ "Td,N,V_restartInterval"
+ "_bottomLevelErrorFromError:"
+ "_dynamicRestartInterval"
+ "_enrollmentFlowMonitorStarted"
+ "_enrollmentFlowUUID"
+ "_ensureNetworkConnection"
+ "_executedSteps"
+ "_installWiFiProfile:"
+ "_minimumRestartInterval"
+ "_networkMonitor"
+ "_oneTimeSteps"
+ "_prepareForReturnToService"
+ "_preserveDataPlan"
+ "_promptForSoftwareUpdateWithSoftwareUpdateError:"
+ "_removeAllNotification"
+ "_restartFlow"
+ "_restartInterval"
+ "_restartScheduled"
+ "_shouldRetryEnrollment"
+ "_softwareUpdateError"
+ "_triggerRRTSWithCompletionHandler:"
+ "_workerQueue_cleanupCachedValuesWillRestart:"
+ "com.apple.MobileAsset"
+ "d"
+ "d16@0:8"
+ "deviceMightHaveNetworkStrict:"
+ "dynamicRestartInterval"
+ "enrollmentFlowMonitorStarted"
+ "enrollmentFlowUUID"
+ "executedSteps"
+ "hasExecutedUIStep = YES"
+ "installWiFiProfileIfNeeded:completionHandler:"
+ "minimumRestartInterval"
+ "networkMonitor"
+ "prepareForReturnToServiceWithCompletionHandler:"
+ "preserveDataPlan"
+ "preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:shouldRetryEnrollment:error:"
+ "profiled is not monitoring current enrollment. Try cleanup within Settings app"
+ "removeObserver:"
+ "requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:"
+ "restartEnrollmentFlowImmediately"
+ "restartInterval"
+ "restartScheduled"
+ "setDynamicRestartInterval:"
+ "setEnrollmentFlowMonitorStarted:"
+ "setEnrollmentFlowUUID:"
+ "setExecutedSteps:"
+ "setMinimumRestartInterval:"
+ "setNetworkMonitor:"
+ "setPreserveDataPlan:"
+ "setRestartInterval:"
+ "setRestartScheduled:"
+ "setShouldRetryEnrollment:"
+ "setSoftwareUpdateError:"
+ "shouldRetryEnrollment"
+ "softwareUpdateError"
+ "trackEndTime"
+ "underlyingErrors"
+ "v24@0:8d16"
+ "v48@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24B32B36@\"NSError\"40"
- "+[DMCReturnToServiceHelper preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:]"
- "-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2"
- "-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]_block_invoke_2"
- "-[DMCEnrollmentFlowController _workerQueue_performFlowStep:]"
- "-[DMCMigrationFlowController _workerQueue_performFlowStep:]"
- "-[DMCUnenrollmentFlowController _workerQueue_performFlowStep:]"
- "@48@0:8@16@24@32^@40"
- "Cleaning up dirty state..."
- "EnsureWiFiConnection"
- "T@\"NSDictionary\",&,N,V_softwareUpdateInfo"
- "WiFi profile is not available."
- "_ensureWiFiConnectionWithWiFiProfile:"
- "_promptForSoftwareUpdateWithSoftwareUpdateInfo:"
- "_softwareUpdateInfo"
- "preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:"
- "requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:"
- "setSoftwareUpdateInfo:"
- "softwareUpdateInfo"
- "v40@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24@\"NSError\"32"

```
