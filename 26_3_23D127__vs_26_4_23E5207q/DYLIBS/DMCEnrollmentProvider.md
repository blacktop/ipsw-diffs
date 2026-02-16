## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-55.80.4.0.0
-  __TEXT.__text: 0x4c750
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0x6e2c
+59.100.16.0.0
+  __TEXT.__text: 0x526dc
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x6e84
   __TEXT.__const: 0x504
-  __TEXT.__oslogstring: 0x223f
-  __TEXT.__cstring: 0x2d65
-  __TEXT.__gcc_except_tab: 0x710
+  __TEXT.__oslogstring: 0x23bf
+  __TEXT.__cstring: 0x2d18
+  __TEXT.__gcc_except_tab: 0x774
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0xa8
   __TEXT.__swift5_typeref: 0x1b6

   __TEXT.__swift5_fieldmd: 0x54
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x14d8
-  __TEXT.__eh_frame: 0x480
-  __TEXT.__objc_classname: 0x113b
-  __TEXT.__objc_methname: 0x13fa9
-  __TEXT.__objc_methtype: 0x46c1
-  __TEXT.__objc_stubs: 0xcea0
+  __TEXT.__unwind_info: 0x1928
+  __TEXT.__eh_frame: 0x430
+  __TEXT.__objc_classname: 0x11a5
+  __TEXT.__objc_methname: 0x140c3
+  __TEXT.__objc_methtype: 0x4772
+  __TEXT.__objc_stubs: 0xd040
   __DATA_CONST.__got: 0xe98
-  __DATA_CONST.__const: 0x10f8
+  __DATA_CONST.__const: 0x1120
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4798
+  __DATA_CONST.__objc_selrefs: 0x47c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x240
-  __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x7c8
+  __DATA_CONST.__objc_arraydata: 0x90
+  __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x2ea0
-  __AUTH_CONST.__objc_const: 0x107c8
+  __AUTH_CONST.__cfstring: 0x2f00
+  __AUTH_CONST.__objc_const: 0x10840
+  __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1b00
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x5b8
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__data: 0x13f8
   __DATA.__bss: 0x260
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 19C0213E-1671-3317-BA37-4A4D89E0CA81
-  Functions: 2129
-  Symbols:   8017
-  CStrings:  4557
+  UUID: C90D1A3C-325D-363E-8330-E3664D35699F
+  Functions: 2137
+  Symbols:   8048
+  CStrings:  4576
 
Symbols:
+ -[DMCEnrollmentFlowManagedConfigurationHelper _enableSystemAppsPeriodicCheckTimer]
+ -[DMCEnrollmentFlowManagedConfigurationHelper installWiFiProfileIfNeeded:completionHandler:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper isMDMEnrollmentAllowed]
+ -[DMCEnrollmentFlowManagedConfigurationHelper setSystemAppPeriodicCheckTimer:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper systemAppPeriodicCheckTimer]
+ -[DMCEnrollmentFlowUIPresenterBase presentActivityPageWithTitle:text:showBottomView:]
+ -[DMCEnrollmentInterface _presentSignInUnavailableMDMEnrollmentRestricted]
+ GCC_except_table55
+ GCC_except_table80
+ _OBJC_IVAR_$_DMCEnrollmentFlowManagedConfigurationHelper._systemAppPeriodicCheckTimer
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ ___100-[DMCReturnToServiceController _fetchAndInstallMDMProfileIfNeededWithCloudConfig:completionHandler:]_block_invoke.10
+ ___100-[DMCReturnToServiceController _fetchAndInstallMDMProfileIfNeededWithCloudConfig:completionHandler:]_block_invoke.13
+ ___100-[DMCReturnToServiceController _fetchAndInstallMDMProfileIfNeededWithCloudConfig:completionHandler:]_block_invoke.6
+ ___138-[DMCBYODEnrollmentFlowUIPresenter requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke.86
+ ___138-[DMCBYODEnrollmentFlowUIPresenter requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke_2.87
+ ___82-[DMCEnrollmentFlowManagedConfigurationHelper _enableSystemAppsPeriodicCheckTimer]_block_invoke
+ ___92-[DMCEnrollmentFlowManagedConfigurationHelper installWiFiProfileIfNeeded:completionHandler:]_block_invoke
+ ___93-[DMCEnrollmentFlowManagedConfigurationHelper _systemAppDeletableInstallationStateDidChange:]_block_invoke_2
+ ___94-[DMCReturnToServiceController _fetchAndStoreCloudConfigurationIfNeededWithCompletionHandler:]_block_invoke.5
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ ___block_literal_global.127
+ _objc_msgSend$DMCIsSpinner
+ _objc_msgSend$_enableSystemAppsPeriodicCheckTimer
+ _objc_msgSend$declarationIdentifier
+ _objc_msgSend$declarationsWithTypes:completionHandler:
+ _objc_msgSend$enrollmentURL
+ _objc_msgSend$isKindOfClass:
+ _objc_msgSend$isMDMEnrollmentAllowed
+ _objc_msgSend$presentActivityPageWithTitle:text:showBottomView:
+ _objc_msgSend$registeredIdentifier
+ _objc_msgSend$setSystemAppPeriodicCheckTimer:
+ _objc_msgSend$storesWithScope:completionHandler:
+ _objc_msgSend$systemAppPeriodicCheckTimer
+ _objc_msgSend$trackEndTime
+ _objc_msgSend$waitForProcessingOfDeclarations:timeout:completionHandler:
- -[DMCEnrollmentFlowUIPresenterBase presentActivityPageWithTitle:text:showButtomView:]
- GCC_except_table52
- ___100-[DMCReturnToServiceController _fetchAndInstallMDMProfileIfNeededWithCloudConfig:completionHandler:]_block_invoke.12
- ___100-[DMCReturnToServiceController _fetchAndInstallMDMProfileIfNeededWithCloudConfig:completionHandler:]_block_invoke.5
- ___100-[DMCReturnToServiceController _fetchAndInstallMDMProfileIfNeededWithCloudConfig:completionHandler:]_block_invoke.9
- ___138-[DMCBYODEnrollmentFlowUIPresenter requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke_4
- ___138-[DMCBYODEnrollmentFlowUIPresenter requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke_5
- ___94-[DMCReturnToServiceController _fetchAndStoreCloudConfigurationIfNeededWithCompletionHandler:]_block_invoke.4
- ___block_literal_global.123
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$presentActivityPageWithTitle:text:showButtomView:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "/Library/Caches/com.apple.xbs/8034402B-B4E4-48BD-9085-738E874DF78C/TemporaryDirectory.cSTShA/Sources/DeviceManagementClientTools/DeviceManagementClientTools/DMC Enrollment Provider/DMC UI Utilities/Views/Functional Views/DMCEnrollmentConfirmationView.m"
+ "ACCOUNTS_SIGN_IN_UNAVAILABLE_MDM_ENROLLMENT_RESTRICTED"
+ "Failed to parse WiFi profile data with error: %{public}@"
+ "Failed to restore original persona %{public}@ after MAID auth: %{public}@"
+ "Failed to restore original persona %{public}@ after simulated auth: %{public}@"
+ "Failed to switch to persona %{public}@ for BYOD authentication: %{public}@"
+ "No-op Managed Sign In button MDM enrollment is restricted"
+ "T@\"NSTimer\",&,N,V_systemAppPeriodicCheckTimer"
+ "WiFi profile exists on the device."
+ "_enableSystemAppsPeriodicCheckTimer"
+ "_presentSignInUnavailableMDMEnrollmentRestricted"
+ "_systemAppPeriodicCheckTimer"
+ "com.apple.FakeApp1"
+ "com.apple.FakeApp2"
+ "installWiFiProfileIfNeeded:completionHandler:"
+ "isMDMEnrollmentAllowed"
+ "prepareForReturnToServiceWithCompletionHandler:"
+ "presentActivityPageWithTitle:text:showBottomView:"
+ "setSystemAppPeriodicCheckTimer:"
+ "systemAppPeriodicCheckTimer"
+ "trackEndTime"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSString\"B@\"NSError\">24"
- "/Library/Caches/com.apple.xbs/Sources/DeviceManagementClientTools/DeviceManagementClientTools/DMC Enrollment Provider/DMC UI Utilities/Views/Functional Views/DMCEnrollmentConfirmationView.m"
- "manager:didFailVerificationWithError:"
- "managerDidFinishVerification:"
- "presentActivityPageWithTitle:text:showButtomView:"

```
