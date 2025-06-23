## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x28b7c
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x19ec
+46.0.0.0.0
+  __TEXT.__text: 0x29434
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x1a9c
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x3b58
-  __TEXT.__cstring: 0x21a2
-  __TEXT.__gcc_except_tab: 0x8c0
+  __TEXT.__oslogstring: 0x3cdd
+  __TEXT.__cstring: 0x2301
+  __TEXT.__gcc_except_tab: 0x938
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x8b0
-  __TEXT.__objc_classname: 0x210
-  __TEXT.__objc_methname: 0x8228
-  __TEXT.__objc_methtype: 0x936
-  __TEXT.__objc_stubs: 0x6040
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0x1188
+  __TEXT.__unwind_info: 0x8c8
+  __TEXT.__objc_classname: 0x21c
+  __TEXT.__objc_methname: 0x8508
+  __TEXT.__objc_methtype: 0x95d
+  __TEXT.__objc_stubs: 0x6260
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__const: 0x1250
   __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a48
+  __DATA_CONST.__objc_selrefs: 0x1ad8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x3e0
-  __AUTH_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x450
+  __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1600
-  __AUTH_CONST.__objc_const: 0x1d20
-  __AUTH_CONST.__objc_intobj: 0x960
-  __AUTH_CONST.__objc_arrayobj: 0x3c0
+  __AUTH_CONST.__cfstring: 0x1740
+  __AUTH_CONST.__objc_const: 0x1dc0
+  __AUTH_CONST.__objc_intobj: 0x978
+  __AUTH_CONST.__objc_arrayobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x168
-  __DATA.__data: 0x1f0
+  __DATA.__objc_ivar: 0x170
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x1f8
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D71B6E51-6ECC-3FD8-B060-CC5DC698795A
-  Functions: 756
-  Symbols:   2929
-  CStrings:  1852
+  UUID: 852CBF06-FDEF-3E40-A497-83D46A406F36
+  Functions: 772
+  Symbols:   2997
+  CStrings:  1905
 
Symbols:
+ +[DMCEnrollmentFlowController(Utilities) _createPasscodeRequiredError]
+ +[DMCMigrationHelper currentEnrollmentStateSupportsMigration]
+ +[DMCMigrationHelper hasPendingEnrollmentWithExistingCloudConfig:]
+ +[DMCMigrationHelper isDeviceEligibleForMigrationWithExistingCloudConfig:outReason:]
+ +[DMCMigrationHelper isMigrationSupportedWithExistingCloudConfig:outReason:]
+ +[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:success:completionHandler:]
+ -[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]
+ -[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithDevicePasscode:devicePasscodeContext:]
+ -[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:]
+ -[DMCEnrollmentFlowController _installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:personaID:]
+ -[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]
+ -[DMCEnrollmentFlowController devicePasscodeContext]
+ -[DMCEnrollmentFlowController loggingSupport]
+ -[DMCEnrollmentFlowController setLoggingSupport:]
+ -[DMCEnrollmentFlowController(Utilities) devicePasscodeContext]
+ -[DMCLoggingSupport(Enrollments) _appRelatedSubsystems]
+ -[DMCLoggingSupport(Enrollments) _bundleIDsForAppRelatedProcesses]
+ -[DMCLoggingSupport(Enrollments) _bundleIDsForDeviceManagementProcesses]
+ -[DMCLoggingSupport(Enrollments) _bundleIDsForEnrollmentHostingApps]
+ -[DMCLoggingSupport(Enrollments) _deviceManagementSubsystems]
+ -[DMCLoggingSupport(Enrollments) enableDebugLoggingForAppPreservation]
+ -[DMCLoggingSupport(Enrollments) enableDebugLoggingForEnrollment]
+ -[DMCMigrationFlowController _enrollmentTypeNotSupportedError]
+ GCC_except_table104
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table118
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table13
+ GCC_except_table131
+ GCC_except_table139
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table19
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table59
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table79
+ GCC_except_table8
+ GCC_except_table93
+ GCC_except_table96
+ GCC_except_table99
+ _DMCMigrationEligibilityDescriptionABE
+ _DMCMigrationEligibilityDescriptionEligible
+ _DMCMigrationEligibilityDescriptionRRTS
+ _DMCMigrationEligibilityDescriptionSharedIPad
+ _DMCMigrationEligibilityDescriptionUnsupervised
+ _DMCMigrationEligibilityDescriptionUnsupportedEnrollment
+ _DMCMigrationHasIncompleteMigrationKey
+ _DMCMigrationUserInitiatedMigrationKey
+ _OBJC_CLASS_$_DMCLoggingSupport
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._devicePasscodeContext
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._loggingSupport
+ __OBJC_$_CATEGORY_DMCLoggingSupport_$_Enrollments
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_DMCLoggingSupport_$_Enrollments
+ ___100-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithDevicePasscode:devicePasscodeContext:]_block_invoke
+ ___100-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithDevicePasscode:devicePasscodeContext:]_block_invoke_2
+ ___111-[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:]_block_invoke
+ ___111-[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:]_block_invoke_2
+ ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.87
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.107
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.96
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.99
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.100
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.108
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.97
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_3.101
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.123
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.124
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.125
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.126
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.128
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.127
+ ___232-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke
+ ___232-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2
+ ___56-[DMCUnenrollmentFlowController _askForPasscodeIfNeeded]_block_invoke.11
+ ___56-[DMCUnenrollmentFlowController _askForPasscodeIfNeeded]_block_invoke_2.15
+ ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke.35
+ ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke_2.36
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.160
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.161
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.162
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke.65
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2
+ ___73-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2.69
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.10
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.6
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.11
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.8
+ ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.146
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.135
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.138
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.136
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.139
+ ___95+[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:success:completionHandler:]_block_invoke
+ ___95+[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:success:completionHandler:]_block_invoke.15
+ ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.174
+ ___block_descriptor_40_e8_32bs_e21_v20?0"NSString"8B16ls32l8
+ ___block_descriptor_40_e8_32bs_e22_v28?0"NSData"8Q16B24ls32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40w_e35_v36?0"NSData"8Q16"NSString"24B32ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e8_v12?0B8ls32l8w40l8
+ ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8lw48l8s40l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_65_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_literal_global.156
+ ___block_literal_global.185
+ ___block_literal_global.91
+ _objc_getProperty
+ _objc_msgSend$_appRelatedSubsystems
+ _objc_msgSend$_askForPasscodeIfNeededWithEnrollmentType:
+ _objc_msgSend$_bundleIDsForAppRelatedProcesses
+ _objc_msgSend$_bundleIDsForDeviceManagementProcesses
+ _objc_msgSend$_bundleIDsForEnrollmentHostingApps
+ _objc_msgSend$_createAndSyncBootstrapTokenWithDevicePasscode:devicePasscodeContext:
+ _objc_msgSend$_deviceManagementSubsystems
+ _objc_msgSend$_enrollmentTypeNotSupportedError
+ _objc_msgSend$_installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:
+ _objc_msgSend$_installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:personaID:
+ _objc_msgSend$_installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:
+ _objc_msgSend$currentEnrollmentStateSupportsMigration
+ _objc_msgSend$devicePasscodeContext
+ _objc_msgSend$enableDebugLoggingForAppPreservation
+ _objc_msgSend$enableDebugLoggingForEnrollment
+ _objc_msgSend$enableDebugLoggingForProcesses:
+ _objc_msgSend$enableDebugLoggingForSubsystems:
+ _objc_msgSend$generateAndSyncBootstrapTokenWithPasscode:passcodeContext:completionHandler:
+ _objc_msgSend$hasPendingEnrollmentWithExistingCloudConfig:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:
+ _objc_msgSend$isADEProfile
+ _objc_msgSend$isMDMProfileADEProfile
+ _objc_msgSend$isMigrationSupportedWithExistingCloudConfig:outReason:
+ _objc_msgSend$loggingSupport
+ _objc_msgSend$makeEndMigrationRequestIfNeededWithCloudConfig:success:completionHandler:
+ _objc_msgSend$queueBlock:afterDelay:
+ _objc_msgSend$requestDevicePasscodeDataWithCompletionHandler:
+ _objc_msgSend$setDevicePasscodeDataType:
+ _objc_msgSend$setLoggingSupport:
- +[DMCMigrationHelper isMigrationSupportedWithExistingCloudConfig:]
- +[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:]
- -[DMCEnrollmentFlowController _askForPasscodeIfNeeded]
- -[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]
- -[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:personaID:]
- -[DMCEnrollmentFlowController _installESSOConfigurationWithProfileData:declarations:devicePasscode:personaID:]
- -[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]
- -[DMCMigrationFlowController _createEnrollmentTypeNotSupportedError]
- -[DMCMigrationFlowController _createUnenrollmentFailedError]
- GCC_except_table100
- GCC_except_table105
- GCC_except_table108
- GCC_except_table114
- GCC_except_table121
- GCC_except_table124
- GCC_except_table127
- GCC_except_table135
- GCC_except_table172
- GCC_except_table175
- GCC_except_table178
- GCC_except_table18
- GCC_except_table187
- GCC_except_table192
- GCC_except_table195
- GCC_except_table198
- GCC_except_table62
- GCC_except_table65
- GCC_except_table68
- GCC_except_table7
- GCC_except_table73
- GCC_except_table77
- GCC_except_table89
- GCC_except_table92
- GCC_except_table95
- ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.77
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.86
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.94
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.88
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.95
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_7
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.112
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.113
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.114
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.115
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.117
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.116
- ___210-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke
- ___210-[DMCEnrollmentFlowController _installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:]_block_invoke_2
- ___54-[DMCEnrollmentFlowController _askForPasscodeIfNeeded]_block_invoke
- ___54-[DMCEnrollmentFlowController _askForPasscodeIfNeeded]_block_invoke_2
- ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke.33
- ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke_2.34
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.149
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.150
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.151
- ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke
- ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke.171
- ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke.173
- ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke_2
- ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke_2.172
- ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke_2.174
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.4
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.8
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.6
- ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.9
- ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.135
- ___87+[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:]_block_invoke
- ___87+[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:]_block_invoke.16
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.124
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.127
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.125
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.128
- ___89-[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:personaID:]_block_invoke
- ___89-[DMCEnrollmentFlowController _installESSOConfigurationProfile:devicePasscode:personaID:]_block_invoke_2
- ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.163
- ___block_descriptor_48_e8_32s40s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e8_v12?0B8lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_literal_global.151
- ___block_literal_global.180
- ___block_literal_global.89
- _kMDMMigrationHasIncompleteMigrationKey
- _kMDMMigrationUserInitiatedMigrationKey
- _objc_msgSend$_createAndSyncBootstrapTokenWithPasscode:
- _objc_msgSend$_createEnrollmentTypeNotSupportedError
- _objc_msgSend$_createUnenrollmentFailedError
- _objc_msgSend$_installESSOConfigurationProfile:devicePasscode:personaID:
- _objc_msgSend$_installESSOConfigurationWithProfileData:declarations:devicePasscode:personaID:
- _objc_msgSend$_installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:
- _objc_msgSend$createBootstrapTokenIfNeededWithPasscode:completionHandler:
- _objc_msgSend$deleteBootstrapTokenWithBootstrapToken:passcode:completionHandler:
- _objc_msgSend$installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:completionHandler:
- _objc_msgSend$installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:
- _objc_msgSend$isMigrationSupportedWithExistingCloudConfig:
- _objc_msgSend$makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:
- _objc_msgSend$syncBootstrapToken:completionHandler:
CStrings:
+ "-[DMCEnrollmentFlowController _askForPasscodeIfNeededWithEnrollmentType:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_6"
+ "@\"DMCLoggingSupport\""
+ "B32@0:8@16^@24"
+ "Bootstrap token exists already."
+ "DMCMigrationHelper: Device has incomplete MDM enrollment!"
+ "DMCMigrationHelper: Device has incomplete migration!"
+ "DMCMigrationHelper: Device has pending enrollment, consider it as eligible for migration."
+ "DMCMigrationHelper: Device is data separated."
+ "DMCMigrationHelper: Device is not ADE enrolled."
+ "DMCMigrationHelper: Device is not MDM enrolled."
+ "DMCMigrationHelper: Migration from non DEP enrolled device is not supported"
+ "DMC_ENROLLMENT_PASSCODE_REQUIRED"
+ "Device is not enrolled with the original MDM server. Do not presrve apps."
+ "Enrollments"
+ "Evaluation returned with migration scheduled: %d, error: %{public}@"
+ "Generate and sync bootstrap token failed with error: %{public}@. Token created: %ld"
+ "Generate and sync bootstrap token succeeded."
+ "MDM_MIGRATION_ERROR_FAILED"
+ "MDM_MIGRATION_ERROR_NOT_SUPPORTED"
+ "Preserving managed apps..."
+ "Sending EndMDMMigration request with serverUID %{public}@, success: %d"
+ "T@\"DMCLoggingSupport\",&,N,V_loggingSupport"
+ "T@\"NSData\",R,V_devicePasscodeContext"
+ "_appRelatedSubsystems"
+ "_askForPasscodeIfNeededWithEnrollmentType:"
+ "_bundleIDsForAppRelatedProcesses"
+ "_bundleIDsForDeviceManagementProcesses"
+ "_bundleIDsForEnrollmentHostingApps"
+ "_createAndSyncBootstrapTokenWithDevicePasscode:devicePasscodeContext:"
+ "_createPasscodeRequiredError"
+ "_deviceManagementSubsystems"
+ "_devicePasscodeContext"
+ "_enrollmentTypeNotSupportedError"
+ "_installESSOConfigurationProfile:devicePasscode:devicePasscodeContext:personaID:"
+ "_installESSOConfigurationWithProfileData:declarations:devicePasscode:devicePasscodeContext:personaID:"
+ "_installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:"
+ "_loggingSupport"
+ "com.apple.Preferences"
+ "com.apple.devicemanagementclient.cloudconfigd"
+ "com.apple.devicemanagementclient.managedappsd"
+ "com.apple.devicemanagementclient.mdmd"
+ "com.apple.dmcapps"
+ "com.apple.dmd"
+ "com.apple.managedappdistributiond"
+ "com.apple.managedconfiguration.profiled"
+ "com.apple.purplebuddy"
+ "com.apple.remotemanagement.ManagedAppsSubscriber"
+ "com.apple.remotemanagementd"
+ "currentEnrollmentStateSupportsMigration"
+ "devicePasscodeContext"
+ "enableDebugLoggingForAppPreservation"
+ "enableDebugLoggingForEnrollment"
+ "enableDebugLoggingForProcesses:"
+ "enableDebugLoggingForSubsystems:"
+ "fail"
+ "generateAndSyncBootstrapTokenWithPasscode:passcodeContext:completionHandler:"
+ "hasPendingEnrollmentWithExistingCloudConfig:"
+ "initWithData:encoding:"
+ "installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
+ "isADEProfile"
+ "isDeviceEligibleForMigrationWithExistingCloudConfig:outReason:"
+ "isMDMProfileADEProfile"
+ "isMigrationSupportedWithExistingCloudConfig:outReason:"
+ "loggingSupport"
+ "makeEndMigrationRequestIfNeededWithCloudConfig:success:completionHandler:"
+ "queueBlock:afterDelay:"
+ "requestDevicePasscodeDataWithCompletionHandler:"
+ "setLoggingSupport:"
+ "v28@?0@\"NSData\"8Q16B24"
+ "v36@?0@\"NSData\"8Q16@\"NSString\"24B32"
+ "v96@0:8@16@24@32@40@48B56@60@68@76Q84B92"
- "+[DMCMigrationHelper hasIncompleteMigration]"
- "-[DMCEnrollmentFlowController _askForPasscodeIfNeeded]_block_invoke_2"
- "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_7"
- "DMC_MDM_MIGRATION_FAILED"
- "Evaluation returned with migration needed: %d, error: %{public}@"
- "Failed to create bootstrap token with error: %{public}@"
- "Failed to delete bootstrap token with error: %{public}@"
- "Failed to retrieve HasIncompleteMigration info with error: %{public}@"
- "Failed to sync bootstrap token with error: %{public}@"
- "HasIncompleteMigration"
- "MDM_ERROR_MIGRATION_NOT_SUPPORTED"
- "MDM_MIGRATION_FAILED_TO_UNENROLL"
- "No bootstrap token was created. Continue..."
- "No cloud config or the cloud config does not have the deadline key for MDM migration."
- "UserInitiatedMigration"
- "_createAndSyncBootstrapTokenWithPasscode:"
- "_createEnrollmentTypeNotSupportedError"
- "_createUnenrollmentFailedError"
- "_installESSOConfigurationProfile:devicePasscode:personaID:"
- "_installESSOConfigurationWithProfileData:declarations:devicePasscode:personaID:"
- "_installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:essoConfigurationProfile:wifiProfileIdentifier:enrollmentType:isReturnToService:"
- "createBootstrapTokenIfNeededWithPasscode:completionHandler:"
- "deleteBootstrapTokenWithBootstrapToken:passcode:completionHandler:"
- "installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:completionHandler:"
- "installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
- "isMigrationSupportedWithExistingCloudConfig:"
- "makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:"
- "syncBootstrapToken:completionHandler:"
- "v88@0:8@16@24@32@40B48@52@60@68Q76B84"

```
