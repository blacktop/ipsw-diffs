## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x4c230
+46.0.0.0.0
+  __TEXT.__text: 0x4c3d8
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x7030
+  __TEXT.__objc_methlist: 0x7058
   __TEXT.__const: 0x2c4
-  __TEXT.__oslogstring: 0x1dd1
-  __TEXT.__cstring: 0x2c05
-  __TEXT.__gcc_except_tab: 0x7c0
+  __TEXT.__oslogstring: 0x1e21
+  __TEXT.__cstring: 0x2c15
+  __TEXT.__gcc_except_tab: 0x7a0
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0xa8
   __TEXT.__swift5_typeref: 0x120

   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x14f0
+  __TEXT.__unwind_info: 0x14e0
   __TEXT.__eh_frame: 0x458
   __TEXT.__objc_classname: 0x114e
-  __TEXT.__objc_methname: 0x1419d
-  __TEXT.__objc_methtype: 0x49bc
-  __TEXT.__objc_stubs: 0xd020
-  __DATA_CONST.__got: 0xe70
-  __DATA_CONST.__const: 0x1000
+  __TEXT.__objc_methname: 0x14295
+  __TEXT.__objc_methtype: 0x4955
+  __TEXT.__objc_stubs: 0xd120
+  __DATA_CONST.__got: 0xe68
+  __DATA_CONST.__const: 0xfd8
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4858
+  __DATA_CONST.__objc_selrefs: 0x4888
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0xc0
+  __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x6e0
-  __AUTH_CONST.__const: 0x338
-  __AUTH_CONST.__cfstring: 0x2ea0
-  __AUTH_CONST.__objc_const: 0x112f0
+  __AUTH_CONST.__const: 0x378
+  __AUTH_CONST.__cfstring: 0x2ec0
+  __AUTH_CONST.__objc_const: 0x11340
   __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1bf0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x5dc
+  __DATA.__objc_ivar: 0x5e0
   __DATA.__data: 0x1358
   __DATA.__bss: 0x60
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0DF4E41C-4092-3E98-AA89-F73E46472565
-  Functions: 2112
-  Symbols:   8113
-  CStrings:  4588
+  UUID: 94FF6048-1ED1-3577-B5F4-B8677B32AC41
+  Functions: 2116
+  Symbols:   8122
+  CStrings:  4596
 
Symbols:
+ +[DMCEnrollmentInterface mdmMigrationAlert]
+ -[DMCEnrollmentFlowManagedConfigurationHelper _analyzeAppFetchingResult:terminationStates:checkManagementState:checkInstallationState:appType:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequest]
+ -[DMCEnrollmentFlowManagedConfigurationHelper devicePasscodeContext]
+ -[DMCEnrollmentFlowManagedConfigurationHelper generateAndSyncBootstrapTokenWithPasscode:passcodeContext:completionHandler:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper isMDMProfileADEProfile]
+ -[DMCEnrollmentFlowManagedConfigurationHelper profileConnectionDidRequestCurrentPasscodeContext:needsExtractablePasscode:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper setDevicePasscodeContext:]
+ -[DMCEnrollmentInterface _presentMDMMigrationAlert]
+ GCC_except_table48
+ _OBJC_IVAR_$_DMCEnrollmentFlowManagedConfigurationHelper._devicePasscodeContext
+ ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.43
+ ___202-[DMCEnrollmentFlowManagedConfigurationHelper manageApplicationWithBundleID:iTunesItemID:organization:personaID:associatedDomains:associatedDomainsEnableDirectDownloads:configuration:completionHandler:]_block_invoke.37
+ ___43+[DMCEnrollmentInterface mdmMigrationAlert]_block_invoke
+ ___43+[DMCEnrollmentInterface mdmMigrationAlert]_block_invoke_2
+ ___69-[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequest]_block_invoke
+ ___69-[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequest]_block_invoke_2
+ ___84-[DMCEnrollmentFlowManagedConfigurationHelper _mdmV1AppsInstallationStateDidChange:]_block_invoke.61
+ ___90-[DMCEnrollmentFlowManagedConfigurationHelper awaitDeviceConfiguredWithCompletionHandler:]_block_invoke.99
+ ___93-[DMCEnrollmentFlowManagedConfigurationHelper _systemAppDeletableInstallationStateDidChange:]_block_invoke.92
+ ___block_descriptor_32_e23_v16?0"UIAlertAction"8l
+ ___block_descriptor_40_e8_32s_e21_v20?0"NSString"8B16ls32l8
+ ___block_literal_global.101
+ ___block_literal_global.118
+ _objc_msgSend$_analyzeAppFetchingResult:terminationStates:checkManagementState:checkInstallationState:appType:
+ _objc_msgSend$_handlePasscodeRequest
+ _objc_msgSend$devicePasscodeContext
+ _objc_msgSend$generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:
+ _objc_msgSend$generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:
+ _objc_msgSend$installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:
+ _objc_msgSend$installationState
+ _objc_msgSend$isADEProfile
+ _objc_msgSend$isMigrationMandatoryWithPendingCloudConfig:
+ _objc_msgSend$launchMigrationApplicationWithError:
+ _objc_msgSend$mdmMigrationAlert
+ _objc_msgSend$requestDevicePasscodeWithCompletionHandler:
+ _objc_msgSend$respondToCurrentPasscodeRequestContinue:passcodeContext:
+ _objc_msgSend$setDevicePasscodeContext:
+ _objc_msgSend$simulatedMDMAccountDrivenEnrollmentAuthenticationResults
- -[DMCEnrollmentFlowManagedConfigurationHelper _analyzeAppFetchingResult:terminationStates:appType:]
- -[DMCEnrollmentFlowManagedConfigurationHelper createBootstrapTokenIfNeededWithPasscode:completionHandler:]
- -[DMCEnrollmentFlowManagedConfigurationHelper deleteBootstrapTokenWithBootstrapToken:passcode:completionHandler:]
- -[DMCEnrollmentFlowManagedConfigurationHelper installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:completionHandler:]
- -[DMCEnrollmentFlowManagedConfigurationHelper installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:]
- -[DMCEnrollmentFlowManagedConfigurationHelper syncBootstrapToken:completionHandler:]
- -[DMCEnrollmentInterface setBeginMigrationButtonEnabled:]
- -[DMCEnrollmentInterface showMigrationAlert]
- GCC_except_table16
- GCC_except_table44
- _MDMBootstrapTokenErrorDomain
- ___106-[DMCEnrollmentFlowManagedConfigurationHelper createBootstrapTokenIfNeededWithPasscode:completionHandler:]_block_invoke
- ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.41
- ___202-[DMCEnrollmentFlowManagedConfigurationHelper manageApplicationWithBundleID:iTunesItemID:organization:personaID:associatedDomains:associatedDomainsEnableDirectDownloads:configuration:completionHandler:]_block_invoke.36
- ___44-[DMCEnrollmentInterface showMigrationAlert]_block_invoke
- ___84-[DMCEnrollmentFlowManagedConfigurationHelper _mdmV1AppsInstallationStateDidChange:]_block_invoke.58
- ___90-[DMCEnrollmentFlowManagedConfigurationHelper awaitDeviceConfiguredWithCompletionHandler:]_block_invoke.96
- ___93-[DMCEnrollmentFlowManagedConfigurationHelper _systemAppDeletableInstallationStateDidChange:]_block_invoke.89
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32w_e23_v16?0"UIAlertAction"8lw32l8
- ___block_literal_global.98
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_DMCEnrollmentProvider
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DMCEnrollmentProvider
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DMCEnrollmentProvider
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DMCEnrollmentProvider
- _objc_msgSend$_analyzeAppFetchingResult:terminationStates:appType:
- _objc_msgSend$deleteBootstrapTokenWithToken:devicePasscode:completionHandler:
- _objc_msgSend$generateBootstrapTokenWithDevicePasscode:completionHandler:
- _objc_msgSend$installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:
- _objc_msgSend$simluatedMDMAccountDrivenEnrollmentAuthenticationResults
- _objc_msgSend$startInBuddyMigrationEnrollment
- _objc_msgSend$syncBootstrapTokenToMDMWithToken:completionHandler:
CStrings:
+ "Adding Cancel button to reboot alert because deadline has not passed."
+ "Awaiting %lu of %lu %{public}@ apps to be installed: %{public}@"
+ "B48@0:8@16@24B32B36@40"
+ "MDM_MIGRATION_BUTTON_START"
+ "MDM_MIGRATION_OPTION_NOTNOW"
+ "MDM_MIGRATION_OPTION_RESTART"
+ "MDM_MIGRATION_RESTART_WARNING_TEXT"
+ "MDM_MIGRATION_RESTART_WARNING_TITLE"
+ "Not adding Cancel button to reboot alert because deadline has passed!"
+ "T@\"NSData\",&,N,V_devicePasscodeContext"
+ "Will ask for passcode"
+ "_analyzeAppFetchingResult:terminationStates:checkManagementState:checkInstallationState:appType:"
+ "_devicePasscodeContext"
+ "_handlePasscodeRequest"
+ "_presentMDMMigrationAlert"
+ "devicePasscodeContext"
+ "generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:"
+ "generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:"
+ "generateAndSyncBootstrapTokenWithPasscode:passcodeContext:completionHandler:"
+ "installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
+ "isADEProfile"
+ "isMDMProfileADEProfile"
+ "isMigrationMandatoryWithPendingCloudConfig:"
+ "launchMigrationApplicationWithError:"
+ "mdmMigrationAlert"
+ "profileConnectionDidRequestCurrentPasscodeContext:needsExtractablePasscode:"
+ "respondToCurrentPasscodeRequestContinue:passcodeContext:"
+ "setDevicePasscodeContext:"
+ "simulatedMDMAccountDrivenEnrollmentAuthenticationResults"
+ "v28@0:8@\"MCProfileConnection\"16B24"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?B@\"NSError\">32"
+ "v92@0:8@\"NSData\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48B56@\"NSNumber\"60@\"NSArray\"68@\"NSString\"76@?<v@?@\"NSString\"B@\"NSError\">84"
+ "v92@0:8@16@24@32@40@48B56@60@68@76@?84"
- "Begin Migration button tapped!"
- "Beginning this flow will reboot your device."
- "Bootstrap token created."
- "Bootstrap token creation failed with error: %{public}@"
- "Bootstrap user exists already."
- "DMC_MDM_MIGRATION_BEGIN"
- "Management Migration"
- "Migrate Now"
- "_analyzeAppFetchingResult:terminationStates:appType:"
- "createBootstrapTokenIfNeededWithPasscode:completionHandler:"
- "deleteBootstrapTokenWithBootstrapToken:passcode:completionHandler:"
- "deleteBootstrapTokenWithToken:devicePasscode:completionHandler:"
- "generateBootstrapTokenWithDevicePasscode:completionHandler:"
- "installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:completionHandler:"
- "installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
- "setBeginMigrationButtonEnabled:"
- "showMigrationAlert"
- "simluatedMDMAccountDrivenEnrollmentAuthenticationResults"
- "syncBootstrapToken:completionHandler:"
- "syncBootstrapTokenToMDMWithToken:completionHandler:"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSString\"B@\"NSError\">48"
- "v84@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48@\"NSNumber\"52@\"NSArray\"60@\"NSString\"68@?<v@?@\"NSString\"B@\"NSError\">76"
- "v84@0:8@16@24@32@40B48@52@60@68@?76"

```
