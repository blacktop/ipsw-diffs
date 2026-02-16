## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-883.9.0.0.0
-  __TEXT.__text: 0xba4fc
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0xa3fc
-  __TEXT.__const: 0x1d0
-  __TEXT.__gcc_except_tab: 0x1dcc
-  __TEXT.__cstring: 0x10a02
-  __TEXT.__oslogstring: 0x6d7b
+892.0.0.0.0
+  __TEXT.__text: 0xc0654
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0xa4ac
+  __TEXT.__const: 0x1d8
+  __TEXT.__gcc_except_tab: 0x1d80
+  __TEXT.__cstring: 0x10bc6
+  __TEXT.__oslogstring: 0x6e32
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2658
+  __TEXT.__unwind_info: 0x2868
   __TEXT.__objc_classname: 0x15de
-  __TEXT.__objc_methname: 0x16fb0
-  __TEXT.__objc_methtype: 0x35f7
-  __TEXT.__objc_stubs: 0xe6e0
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x1db0
+  __TEXT.__objc_methname: 0x1747f
+  __TEXT.__objc_methtype: 0x36fd
+  __TEXT.__objc_stubs: 0xe900
+  __DATA_CONST.__got: 0xa88
+  __DATA_CONST.__const: 0x1db8
   __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52e8
+  __DATA_CONST.__objc_selrefs: 0x5390
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x1a8
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x900
-  __AUTH_CONST.__cfstring: 0x7ac0
-  __AUTH_CONST.__objc_const: 0x3e008
+  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__const: 0x8e0
+  __AUTH_CONST.__cfstring: 0x7bc0
+  __AUTH_CONST.__objc_const: 0x3e140
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x2d00
-  __DATA.__objc_ivar: 0xf08
+  __DATA.__objc_ivar: 0xf28
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 53294ED0-8638-38E3-87BB-F133E849DFA9
-  Functions: 3982
-  Symbols:   14357
-  CStrings:  7613
+  UUID: F9F6DFEB-B21F-3472-84F6-7088B3FAA5B9
+  Functions: 4026
+  Symbols:   14665
+  CStrings:  7671
 
Symbols:
+ +[TSCellularPlanUserConsentViewController calculateTitleAndDetailsWithName:consentType:trialPlanType:trialExpirationDate:title:details:hasProvisioningServiceImpact:]
+ +[TSCellularPlanUserConsentViewController calculateTitleAndDetailsWithName:consentType:trialPlanType:trialExpirationDate:title:details:hasProvisioningServiceImpact:].cold.1
+ -[CTDisplayPlan(SimSetup) requiresSoftwareUpdate]
+ -[NSArray(CTDisplayPlan) filteredPlansForUnknownLocationBucket]
+ -[TSCellularPlanUserConsentViewController initWithConfirmationCode:consentType:requireAdditionalConsent:confirmationCode:acceptButtonTapped:hasProvisioningServiceImpact:]
+ -[TSCellularPlanUserConsentViewController initWithName:consentType:requireAdditionalConsent:hasProvisioningServiceImpact:]
+ -[TSCellularPlanUserConsentViewController initWithName:consentType:requireAdditionalConsent:trialPlanType:trialExpirationDate:hasProvisioningServiceImpact:]
+ -[TSCoreTelephonyClientCache hasProvisioningServiceImpact:]
+ -[TSCoreTelephonyClientCache hasProvisioningServiceImpact:].cold.1
+ -[TSCoreTelephonyClientCache hasProvisioningServiceImpact:].cold.2
+ -[TSCoreTelephonyClientCache hasProvisioningServiceImpactMap]
+ -[TSCoreTelephonyClientCache setHasProvisioningServiceImpactMap:]
+ -[TSCrossPlatformTargetTransferFlow cachedIneligibleViewController]
+ -[TSCrossPlatformTargetTransferFlow setCachedIneligibleViewController:]
+ -[TSOnDeviceConversionFlow initWithPhoneNumber:carrierName:iccid:]
+ -[TSQRCodeScanFlow hasProvisioningServiceImpact]
+ -[TSQRCodeScanFlow setHasProvisioningServiceImpact:]
+ -[TSSIMSetupPublicApiInstallFlow _getTrialPlanDate:]
+ -[TSSIMSetupPublicApiInstallFlow _getTrialPlanTypeAndDateOfInstallingIccid:]
+ -[TSSIMSetupPublicApiInstallFlow _isTrialPlanExpiringInThreeDays:]
+ -[TSSIMSetupPublicApiInstallFlow initWithAppName:requireSetup:skipGeneralInstallConsent:hasProvisioningServiceImpact:]
+ -[TSSinglePlanTransferViewController initWithLocalPhysical:carrierName:hasProvisioningServiceImpact:]
+ -[TSSinglePlanTransferViewController initWithLocalPhysical:carrierName:hasProvisioningServiceImpact:].cold.1
+ _CFCalendarComposeAbsoluteTime
+ _CFCalendarCopyCurrent
+ _CFCalendarDecomposeAbsoluteTime
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._hasProvisioningServiceImpact
+ _OBJC_IVAR_$_TSCoreTelephonyClientCache._hasProvisioningServiceImpactMap
+ _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._cachedIneligibleViewController
+ _OBJC_IVAR_$_TSOnDeviceConversionFlow._iccid
+ _OBJC_IVAR_$_TSQRCodeScanFlow._hasProvisioningServiceImpact
+ _OBJC_IVAR_$_TSSIMSetupPublicApiInstallFlow._hasProvisioningServiceImpact
+ _OBJC_IVAR_$_TSSIMSetupPublicApiInstallFlow._installingIccid
+ _OBJC_IVAR_$_TSSinglePlanTransferViewController._hasProvisioningServiceImpact
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _TSUserInfoHasProvisioningServiceImpactKey
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.106.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.107
+ ___block_literal_global.306
+ ___block_literal_global.322
+ ___block_literal_global.58
+ ___block_literal_global.687
+ ___block_literal_global.716
+ ___block_literal_global.776
+ _objc_msgSend$_getTrialPlanDate:
+ _objc_msgSend$_getTrialPlanTypeAndDateOfInstallingIccid:
+ _objc_msgSend$_isTrialPlanExpiringInThreeDays:
+ _objc_msgSend$cachedIneligibleViewController
+ _objc_msgSend$calculateTitleAndDetailsWithName:consentType:trialPlanType:trialExpirationDate:title:details:hasProvisioningServiceImpact:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$filteredPlansForUnknownLocationBucket
+ _objc_msgSend$filteredPlansWithTransferCapability:
+ _objc_msgSend$hasProvisioningServiceImpact:
+ _objc_msgSend$hasProvisioningServiceImpact:error:
+ _objc_msgSend$initWithAppName:requireSetup:skipGeneralInstallConsent:hasProvisioningServiceImpact:
+ _objc_msgSend$initWithConfirmationCode:consentType:requireAdditionalConsent:confirmationCode:acceptButtonTapped:hasProvisioningServiceImpact:
+ _objc_msgSend$initWithLocalPhysical:carrierName:hasProvisioningServiceImpact:
+ _objc_msgSend$initWithName:consentType:requireAdditionalConsent:hasProvisioningServiceImpact:
+ _objc_msgSend$initWithName:consentType:requireAdditionalConsent:trialPlanType:trialExpirationDate:hasProvisioningServiceImpact:
+ _objc_msgSend$initWithPhoneNumber:carrierName:iccid:
+ _objc_msgSend$requiresSoftwareUpdate
+ _objc_msgSend$setCachedIneligibleViewController:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$trialExpirationDate
- +[TSCellularPlanUserConsentViewController calculateTitleAndDetailsWithName:consentType:title:details:]
- +[TSCellularPlanUserConsentViewController calculateTitleAndDetailsWithName:consentType:title:details:].cold.1
- -[TSCellularPlanUserConsentViewController initWithConfirmationCode:consentType:requireAdditionalConsent:confirmationCode:acceptButtonTapped:]
- -[TSCellularPlanUserConsentViewController initWithName:consentType:requireAdditionalConsent:]
- -[TSOnDeviceConversionFlow initWithPhoneNumber:carrierName:]
- -[TSSIMSetupPublicApiInstallFlow initWithAppName:requireSetup:skipGeneralInstallConsent:]
- -[TSSinglePlanTransferViewController initWithLocalPhysical:carrierName:]
- -[TSSinglePlanTransferViewController initWithLocalPhysical:carrierName:].cold.1
- ___61-[TSPostMigrationFlow _subFlowVcWithReconnectionCredentials:]_block_invoke
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.103
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.103.cold.1
- ___block_literal_global.300
- ___block_literal_global.316
- ___block_literal_global.52
- ___block_literal_global.54
- ___block_literal_global.57
- ___block_literal_global.681
- ___block_literal_global.710
- ___block_literal_global.770
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$clearReconnectionCredentials:
- _objc_msgSend$initWithAppName:requireSetup:skipGeneralInstallConsent:
- _objc_msgSend$initWithConfirmationCode:consentType:requireAdditionalConsent:confirmationCode:acceptButtonTapped:
- _objc_msgSend$initWithLocalPhysical:carrierName:
- _objc_msgSend$initWithName:consentType:requireAdditionalConsent:
- _objc_msgSend$initWithPhoneNumber:carrierName:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "+[TSCellularPlanUserConsentViewController calculateTitleAndDetailsWithName:consentType:trialPlanType:trialExpirationDate:title:details:hasProvisioningServiceImpact:]"
+ "-[TSCoreTelephonyClientCache hasProvisioningServiceImpact:]"
+ "-[TSSinglePlanTransferViewController initWithLocalPhysical:carrierName:hasProvisioningServiceImpact:]"
+ "@24@0:8d16"
+ "@40@0:8@16Q24B32B36"
+ "@52@0:8@16Q24B32@36B44B48"
+ "@56@0:8@16Q24B32Q36@44B52"
+ "APP_USER_CONSENT_DETAIL_FOR_TRIAL_OVER_72_%@_%@"
+ "APP_USER_CONSENT_DETAIL_FOR_TRIAL_UNDER_72_%@_%@"
+ "B24@0:8d16"
+ "GENERAL_USER_CONSENT_COMMON_DETAIL_FOR_TRIAL_OVER_72_%@_%@"
+ "GENERAL_USER_CONSENT_COMMON_DETAIL_FOR_TRIAL_UNDER_72_%@_%@"
+ "HasProvisioningServiceImpactKey"
+ "Q24@0:8^@16"
+ "SERVICE_IMPACT_MESSAGE"
+ "T@\"NSMutableDictionary\",&,V_hasProvisioningServiceImpactMap"
+ "T@\"UIViewController\",&,N,V_cachedIneligibleViewController"
+ "TB,V_hasProvisioningServiceImpact"
+ "[E]Invalid iccid for has provisioning service impact @%s"
+ "[E]hasProvisioningServiceImpact failed with error: %@ @%s"
+ "_cachedIneligibleViewController"
+ "_getTrialPlanDate:"
+ "_getTrialPlanTypeAndDateOfInstallingIccid:"
+ "_hasProvisioningServiceImpact"
+ "_hasProvisioningServiceImpactMap"
+ "_installingIccid"
+ "_isTrialPlanExpiringInThreeDays:"
+ "_webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:requestURL:method:submissionHandler:"
+ "cachedIneligibleViewController"
+ "calculateTitleAndDetailsWithName:consentType:trialPlanType:trialExpirationDate:title:details:hasProvisioningServiceImpact:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "does not have"
+ "doubleValue"
+ "filteredPlansForUnknownLocationBucket"
+ "has"
+ "hasProvisioningServiceImpact"
+ "hasProvisioningServiceImpact:"
+ "hasProvisioningServiceImpact:error:"
+ "hasProvisioningServiceImpactMap"
+ "iccid: %@ %@ service impact @%s"
+ "initWithAppName:requireSetup:skipGeneralInstallConsent:hasProvisioningServiceImpact:"
+ "initWithConfirmationCode:consentType:requireAdditionalConsent:confirmationCode:acceptButtonTapped:hasProvisioningServiceImpact:"
+ "initWithLocalPhysical:carrierName:hasProvisioningServiceImpact:"
+ "initWithName:consentType:requireAdditionalConsent:hasProvisioningServiceImpact:"
+ "initWithName:consentType:requireAdditionalConsent:trialPlanType:trialExpirationDate:hasProvisioningServiceImpact:"
+ "initWithPhoneNumber:carrierName:iccid:"
+ "installing iccid [%@] from [%@] @%s"
+ "requiresSoftwareUpdate"
+ "setCachedIneligibleViewController:"
+ "setDateStyle:"
+ "setHasProvisioningServiceImpact:"
+ "setHasProvisioningServiceImpactMap:"
+ "setTimeStyle:"
+ "stringFromDate:"
+ "trialExpirationDate"
+ "v68@0:8@16Q24Q32@40^@48^@56B64"
+ "v80@0:8@\"WKWebView\"16@\"NSDictionary\"24@\"WKFrameInfo\"32@\"WKFrameInfo\"40@\"NSObject<NSSecureCoding>\"48@\"NSURL\"56@\"NSString\"64@?<v@?>72"
+ "v80@0:8@16@24@32@40@48@56@64@?72"
+ "yMd"
+ "yMdHms"
+ "\xf01"
- "+[TSCellularPlanUserConsentViewController calculateTitleAndDetailsWithName:consentType:title:details:]"
- "-[TSSinglePlanTransferViewController initWithLocalPhysical:carrierName:]"
- "@36@0:8@16Q24B32"
- "@48@0:8@16Q24B32@36B44"
- "clearReconnectionCredentials:"
- "initWithAppName:requireSetup:skipGeneralInstallConsent:"
- "initWithConfirmationCode:consentType:requireAdditionalConsent:confirmationCode:acceptButtonTapped:"
- "initWithLocalPhysical:carrierName:"
- "initWithName:consentType:requireAdditionalConsent:"
- "initWithPhoneNumber:carrierName:"
- "\xf0!"

```
