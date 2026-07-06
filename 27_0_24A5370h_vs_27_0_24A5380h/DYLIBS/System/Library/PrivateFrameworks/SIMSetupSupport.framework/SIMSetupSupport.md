## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-  __TEXT.__text: 0xdf23c
-  __TEXT.__objc_methlist: 0xc1f4
-  __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x2068
-  __TEXT.__cstring: 0x16c4a
-  __TEXT.__oslogstring: 0x87f4
+  __TEXT.__text: 0xe0d58
+  __TEXT.__objc_methlist: 0xc284
+  __TEXT.__const: 0x1f0
+  __TEXT.__gcc_except_tab: 0x20e8
+  __TEXT.__cstring: 0x172cc
+  __TEXT.__oslogstring: 0x8a8d
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2ed8
+  __TEXT.__unwind_info: 0x2f40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x20d8
+  __DATA_CONST.__const: 0x20e8
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d40
+  __DATA_CONST.__objc_selrefs: 0x5d98
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x228
   __DATA_CONST.__got: 0xbe0
-  __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__cfstring: 0xa640
-  __AUTH_CONST.__objc_const: 0x4d368
+  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__cfstring: 0xa8c0
+  __AUTH_CONST.__objc_const: 0x4d458
   __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x35c0
-  __DATA.__objc_ivar: 0x12c4
+  __DATA.__objc_ivar: 0x12dc
   __DATA.__data: 0xc70
   __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4818
-  Symbols:   17296
-  CStrings:  4372
+  Functions: 4843
+  Symbols:   17370
+  CStrings:  4433
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[NSArray(CTDisplayPlan) filteredPlansSuppressingNotSupportedMatchingALSCarriers:]
+ -[SSInstallPlanInformation maybeUpdatePendingProfileReleaseStatus]
+ -[SSQuickSwitchPreActivationFailureViewController .cxx_destruct]
+ -[SSQuickSwitchPreActivationFailureViewController _doneButtonTapped]
+ -[SSQuickSwitchPreActivationFailureViewController delegate]
+ -[SSQuickSwitchPreActivationFailureViewController initWithDelegate:result:otherDeviceName:]
+ -[SSQuickSwitchPreActivationFailureViewController prepare:]
+ -[SSQuickSwitchPreActivationFailureViewController setDelegate:]
+ -[SSQuickSwitchPreActivationFailureViewController viewDidLoad]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _continueFirstViewController:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow enrollmentResult]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setEnrollmentResult:]
+ -[TSActivationFlowWithSimSetupFlow intermediateDefaultsToQuickSwitch]
+ -[TSActivationFlowWithSimSetupFlow presetQuickSwitchFlowType]
+ -[TSActivationFlowWithSimSetupFlow setIntermediateDefaultsToQuickSwitch:]
+ -[TSActivationFlowWithSimSetupFlow setPresetQuickSwitchFlowType:]
+ -[TSCellularPlanActivatingFlow _handleQuickSwitchPendingProfileRelease]
+ -[TSCellularSetupTimeoutFailureViewController initWithTimeoutReason:isEmbeddedInResultView:plans:quickSwitchFlowType:]
+ -[TSCoreTelephonyClientCache clearReconnectionCredentialsWithCompletion:]
+ -[TSCoreTelephonyClientCache hasQuickSwitchEnrolledLineWithCompletion:]
+ -[TSMultiPlanIntermediateViewController defaultSection]
+ -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:defaultSection:]
+ -[TSSIMSetupPublicApiInstallFlow initWithAppName:requireSetup:skipGeneralInstallConsent:hasProvisioningServiceImpact:skipShowSettings:]
+ -[TSTransferCloudFlow _continueFirstViewController:]
+ -[TSWebsheetSignupFlow initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:planIdentifier:secondaryEid:]
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table136
+ GCC_except_table141
+ GCC_except_table150
+ GCC_except_table157
+ GCC_except_table165
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table214
+ GCC_except_table29
+ GCC_except_table61
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table92
+ _CTPlanTransferStatusTimeoutPendingProfileRelease
+ _OBJC_CLASS_$_SSQuickSwitchPreActivationFailureViewController
+ _OBJC_IVAR_$_SSQuickSwitchPreActivationFailureViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._enrollmentResult
+ _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._intermediateDefaultsToQuickSwitch
+ _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._presetQuickSwitchFlowType
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._defaultSection
+ _OBJC_IVAR_$_TSSIMSetupPublicApiInstallFlow._skipShowSettings
+ _OBJC_IVAR_$_TSWebsheetSignupFlow._planIdentifier
+ _OBJC_IVAR_$_TSWebsheetSignupFlow._secondaryEid
+ _OBJC_METACLASS_$_SSQuickSwitchPreActivationFailureViewController
+ _TSUserInfoIntermediateDefaultsToQuickSwitchKey
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchPreActivationFailureViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchPreActivationFailureViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchPreActivationFailureViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchPreActivationFailureViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchPreActivationFailureViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchPreActivationFailureViewController
+ ___38-[TSTransferFlow firstViewController:]_block_invoke
+ ___43-[TSPostMigrationFlow firstViewController:]_block_invoke_2
+ ___45-[TSWebsheetSignupFlow accountPendingRelease]_block_invoke
+ ___52-[TSTransferCloudFlow _continueFirstViewController:]_block_invoke
+ ___69-[SSQuickSwitchSecondaryEnrollmentFlow _continueFirstViewController:]_block_invoke
+ ___71-[TSCoreTelephonyClientCache hasQuickSwitchEnrolledLineWithCompletion:]_block_invoke
+ ___73-[TSCoreTelephonyClientCache clearReconnectionCredentialsWithCompletion:]_block_invoke
+ ___82-[NSArray(CTDisplayPlan) filteredPlansSuppressingNotSupportedMatchingALSCarriers:]_block_invoke
+ ___83-[TSWebsheetSignupFlow didPurchasePlanSuccessfullyWithCarrier:mnc:gid1:gid2:state:]_block_invoke
+ _objc_msgSend$_continueFirstViewController:
+ _objc_msgSend$_handleQuickSwitchPendingProfileRelease
+ _objc_msgSend$clearReconnectionCredentials:
+ _objc_msgSend$clearReconnectionCredentialsWithCompletion:
+ _objc_msgSend$didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:planIdentifier:completion:
+ _objc_msgSend$filteredPlansSuppressingNotSupportedMatchingALSCarriers:
+ _objc_msgSend$hasQuickSwitchEnrolledLineWithCompletion:
+ _objc_msgSend$initWithAppName:requireSetup:skipGeneralInstallConsent:hasProvisioningServiceImpact:skipShowSettings:
+ _objc_msgSend$initWithDelegate:result:otherDeviceName:
+ _objc_msgSend$initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:defaultSection:
+ _objc_msgSend$initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:planIdentifier:secondaryEid:
+ _objc_msgSend$initWithTimeoutReason:isEmbeddedInResultView:plans:quickSwitchFlowType:
+ _objc_msgSend$maybeUpdatePendingProfileReleaseStatus
+ _objc_msgSend$numberOfSectionsInTableView:
+ _objc_msgSend$setIntermediateDefaultsToQuickSwitch:
+ _objc_msgSend$setPresetQuickSwitchFlowType:
- -[SSQuickSwitchNoWiFiViewController .cxx_destruct]
- -[SSQuickSwitchNoWiFiViewController _doneButtonTapped]
- -[SSQuickSwitchNoWiFiViewController delegate]
- -[SSQuickSwitchNoWiFiViewController initWithDelegate:otherDeviceName:]
- -[SSQuickSwitchNoWiFiViewController prepare:]
- -[SSQuickSwitchNoWiFiViewController setDelegate:]
- -[SSQuickSwitchNoWiFiViewController viewDidLoad]
- -[SSQuickSwitchSecondaryEnrollmentFlow noWiFiOnOldDevice]
- -[SSQuickSwitchSecondaryEnrollmentFlow setNoWiFiOnOldDevice:]
- -[TSCellularSetupTimeoutFailureViewController initWithTimeoutReason:isEmbeddedInResultView:plans:]
- -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:]
- -[TSWebsheetSignupFlow initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:]
- GCC_except_table129
- GCC_except_table131
- GCC_except_table135
- GCC_except_table140
- GCC_except_table148
- GCC_except_table156
- GCC_except_table164
- GCC_except_table198
- GCC_except_table201
- GCC_except_table209
- GCC_except_table211
- GCC_except_table213
- GCC_except_table88
- GCC_except_table90
- _OBJC_CLASS_$_SSQuickSwitchNoWiFiViewController
- _OBJC_IVAR_$_SSQuickSwitchNoWiFiViewController._delegate
- _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._noWiFiOnOldDevice
- _OBJC_METACLASS_$_SSQuickSwitchNoWiFiViewController
- __OBJC_$_INSTANCE_METHODS_SSQuickSwitchNoWiFiViewController
- __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchNoWiFiViewController
- __OBJC_$_PROP_LIST_SSQuickSwitchNoWiFiViewController
- __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchNoWiFiViewController
- __OBJC_CLASS_RO_$_SSQuickSwitchNoWiFiViewController
- __OBJC_METACLASS_RO_$_SSQuickSwitchNoWiFiViewController
- _objc_msgSend$didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:completion:
- _objc_msgSend$initWithAppName:requireSetup:skipGeneralInstallConsent:hasProvisioningServiceImpact:
- _objc_msgSend$initWithDelegate:otherDeviceName:
- _objc_msgSend$initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:
- _objc_msgSend$initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:
- _objc_msgSend$initWithTimeoutReason:isEmbeddedInResultView:plans:
CStrings:
+ "-[NSArray(CTDisplayPlan) filteredPlansSuppressingNotSupportedMatchingALSCarriers:]_block_invoke"
+ "-[SSInstallPlanInformation maybeUpdatePendingProfileReleaseStatus]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _continueFirstViewController:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _continueFirstViewController:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow _handleQuickSwitchPendingProfileRelease]"
+ "-[TSCoreTelephonyClientCache clearReconnectionCredentialsWithCompletion:]_block_invoke"
+ "-[TSCoreTelephonyClientCache hasQuickSwitchEnrolledLineWithCompletion:]_block_invoke"
+ "-[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:defaultSection:]"
+ "-[TSPostMigrationFlow firstViewController:]_block_invoke"
+ "-[TSTransferCloudFlow _continueFirstViewController:]"
+ "-[TSTransferCloudFlow firstViewController:]_block_invoke"
+ "-[TSTransferFlow firstViewController:]_block_invoke"
+ "-[TSWebsheetSignupFlow initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:planIdentifier:secondaryEid:]"
+ "CTPlanTransferStatusTimeoutPendingProfileRelease"
+ "Cleared reconnection credentials @%s"
+ "ERROR_QS_PENDING_PROFILE_RELEASE_TIMEOUT_MESSAGE"
+ "ERROR_QS_PENDING_PROFILE_RELEASE_TIMEOUT_MESSAGE_BUDDY"
+ "ERROR_QS_PENDING_PROFILE_RELEASE_TIMEOUT_MESSAGE_SLIDING_BUDDY"
+ "ERROR_QS_PENDING_PROFILE_RELEASE_TIMEOUT_SLIDING_MESSAGE"
+ "IntermediateDefaultsToQuickSwitch"
+ "QS enrolled line in buddy, suppressing SSQuickSwitchSecondaryEnrollmentFlow @%s"
+ "QS enrolled line in buddy, suppressing TSTransferCloudFlow @%s"
+ "QS enrolled line in buddy, suppressing TSTransferFlow @%s"
+ "QS enrolled line, clearing reconnection credentials and skipping post-migration @%s"
+ "QS_ENROLL_CONSENT_PRIMARY_ESIM_DETAILS"
+ "QS_NO_WLAN_DETAILS_BUDDY_%@"
+ "QS_NO_WLAN_DETAILS_BUDDY_NO_NAME"
+ "QS_NO_WLAN_TITLE_POSTBUDDY"
+ "QS_TRANSPORT_FAILURE_DETAILS_BUDDY_%@"
+ "QS_TRANSPORT_FAILURE_DETAILS_BUDDY_NO_NAME"
+ "QS_TRANSPORT_FAILURE_DETAILS_POSTBUDDY_%@"
+ "QS_TRANSPORT_FAILURE_DETAILS_POSTBUDDY_NO_NAME"
+ "QS_TRANSPORT_FAILURE_TITLE_POSTBUDDY"
+ "QS_TRANSPORT_FAILURE_WLAN_DETAILS_BUDDY_%@"
+ "QS_TRANSPORT_FAILURE_WLAN_DETAILS_BUDDY_NO_NAME"
+ "QS_TRANSPORT_FAILURE_WLAN_DETAILS_POSTBUDDY_%@"
+ "QS_TRANSPORT_FAILURE_WLAN_DETAILS_POSTBUDDY_NO_NAME"
+ "QUICK_SWITCH_OLD_DEVICE_PENDING_PROFILE_RELEASE_DETAIL"
+ "QUICK_SWITCH_OLD_DEVICE_PENDING_PROFILE_RELEASE_SLIDING_DETAIL"
+ "SkipOpenSettings"
+ "Suppressing NotSupported magnolia plan (%@) matching ALS carrier @%s"
+ "[E]Failed to clear reconnection credentials: %@ @%s"
+ "[E]Failed to query accountsSupportingQuickSwitchFromThisDevice: %@ @%s"
+ "enrollment result before subflow handoff: %lu @%s"
+ "handle pending profile release @%s"
+ "hasQuickSwitchEnrolledLine: %@ (accounts=%lu) @%s"
+ "pending profile release, update %@ status to TimeoutPendingProfileRelease @%s"
+ "primary-iccid: %@, use case: %@, planIdentifier: %@, secondaryEid: %@ @%s"
+ "secondary-device-active"
+ "transport ready @%s"
+ "transport-ready"
- "-[SSQuickSwitchSecondaryEnrollmentFlow firstViewController:]"
- "-[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:]"
- "-[TSTransferCloudFlow firstViewController:]"
- "-[TSWebsheetSignupFlow initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:]"
- "QS_NO_WIFI_TITLE_BUDDY"
- "WiFi check result from old device: available=%d @%s"
- "available"
- "enrollment failed: Wi-Fi unavailable on old device [result=%lu] @%s"
- "primary-iccid: %@, use case: %@ @%s"
- "quick-switch-wifi-check"

```
