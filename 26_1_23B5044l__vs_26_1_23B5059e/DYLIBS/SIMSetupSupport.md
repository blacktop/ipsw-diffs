## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-874.1.0.0.0
-  __TEXT.__text: 0xb7594
+879.0.0.0.0
+  __TEXT.__text: 0xb8f38
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0xa2b4
-  __TEXT.__const: 0x1d8
+  __TEXT.__objc_methlist: 0xa38c
+  __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x1db8
-  __TEXT.__cstring: 0x10092
-  __TEXT.__oslogstring: 0x6acb
+  __TEXT.__cstring: 0x1074d
+  __TEXT.__oslogstring: 0x6aa3
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2600
-  __TEXT.__objc_classname: 0x15cf
-  __TEXT.__objc_methname: 0x16c24
-  __TEXT.__objc_methtype: 0x355e
-  __TEXT.__objc_stubs: 0xe500
+  __TEXT.__unwind_info: 0x2638
+  __TEXT.__objc_classname: 0x15e4
+  __TEXT.__objc_methname: 0x16e64
+  __TEXT.__objc_methtype: 0x356e
+  __TEXT.__objc_stubs: 0xe600
   __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x1db0
   __DATA_CONST.__objc_classlist: 0x488
-  __DATA_CONST.__objc_catlist: 0x68
+  __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5238
+  __DATA_CONST.__objc_selrefs: 0x52a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x430
-  __DATA_CONST.__objc_arraydata: 0x140
+  __DATA_CONST.__objc_arraydata: 0x1a8
   __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x7640
-  __AUTH_CONST.__objc_const: 0x3dea0
-  __AUTH_CONST.__objc_intobj: 0x690
+  __AUTH_CONST.__const: 0x8e0
+  __AUTH_CONST.__cfstring: 0x7980
+  __AUTH_CONST.__objc_const: 0x3df90
+  __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x2d00
-  __DATA.__objc_ivar: 0xee8
+  __DATA.__objc_ivar: 0xefc
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D07AE94-3C1D-35ED-830A-8AF185F3E3C6
-  Functions: 3948
-  Symbols:   14268
-  CStrings:  7492
+  UUID: 6F720217-6060-3856-BABC-DDBE5B7964D7
+  Functions: 3969
+  Symbols:   14323
+  CStrings:  7562
 
Symbols:
+ +[NSMutableDictionary(CategorizedPlans) dictionaryWithPlansByGroupByTransferCapability:]
+ -[NSArray(CTDisplayPlan) getCombinedFooterForNonTransferablePlans]
+ -[NSArray(CTDisplayPlan) getCombinedTitleAndDetailsForNonTransferablePlans:details:]
+ -[NSArray(CTDisplayPlan) getCombinedTitleAndDetailsForTransferCapability:title:detail:]
+ -[NSArray(CTDisplayPlan) getCombinedTitleAndDetailsForTransferCapability:title:detail:].cold.1
+ -[NSMutableDictionary(CategorizedPlans) mergeByTransferCapabilities:]
+ -[SSConfirmationCodeViewController _textFieldDidBegin]
+ -[SSConfirmationCodeViewController _textFieldDidEnd]
+ -[SSQRCodeIntroViewController _configureNavigationItem]
+ -[SSQRCodeIntroViewController viewWillAppear:]
+ -[SSVisitStoreViewController _otherButtonTapped:]
+ -[SSVisitStoreViewController initWithPlans:showOtherOption:]
+ -[SSVisitStoreViewController isOtherButtonTapped]
+ -[SSVisitStoreViewController setIsOtherButtonTapped:]
+ -[SSVisitStoreViewController viewWillAppear:]
+ -[TSCrossPlatformSourceTransferFlow isSecureIntentRejected]
+ -[TSCrossPlatformSourceTransferFlow setIsSecureIntentRejected:]
+ -[TSCrossPlatformTargetTransferFlow setCancelNavigationBarItems:]
+ -[TSMidOperationFailureViewController initShowErrorOnSourceWithDelayedDownloadECSWithPlanIdentifier:]
+ -[TSMidOperationFailureViewController initWithPlans:isCrossPlatformTransfer:]
+ -[TSMidOperationFailureViewController initWithSecureIntentRejected]
+ -[TSNoPlanForTransferViewController initShowNoSIMForCrossPlatformTransfer]
+ -[TSTransferCloudFlow nextViewControllerFrom:].cold.1
+ GCC_except_table26
+ GCC_except_table42
+ GCC_except_table48
+ _CTPlanTransferCapabilityRequireVisitStoreOnce
+ _OBJC_IVAR_$_SSVisitStoreViewController._isOtherButtonTapped
+ _OBJC_IVAR_$_SSVisitStoreViewController._showOtherOption
+ _OBJC_IVAR_$_TSCrossPlatformSourceTransferFlow._isSecureIntentRejected
+ _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._cancelButton
+ _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._noSIMOrNoEligibleSIMOnSource
+ _OBJC_IVAR_$_TSMidOperationFailureViewController._isForCrossPlatform
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSMutableDictionary_$_CategorizedPlans
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableDictionary_$_CategorizedPlans
+ __OBJC_$_CATEGORY_NSMutableDictionary_$_CategorizedPlans
+ ___236-[TSTransferListViewController initWithTransferPlans:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:]_block_invoke
+ ___57-[TSCrossPlatformTargetTransferFlow firstViewController:]_block_invoke.26
+ ___block_literal_global.170
+ ___block_literal_global.83
+ _objc_msgSend$_configureNavigationItem
+ _objc_msgSend$dictionaryWithPlansByGroupByTransferCapability:
+ _objc_msgSend$getCombinedFooterForNonTransferablePlans
+ _objc_msgSend$getCombinedTitleAndDetailsForNonTransferablePlans:details:
+ _objc_msgSend$getCombinedTitleAndDetailsForTransferCapability:title:detail:
+ _objc_msgSend$initShowErrorOnSourceWithDelayedDownloadECSWithPlanIdentifier:
+ _objc_msgSend$initShowNoSIMForCrossPlatformTransfer
+ _objc_msgSend$initWithPlans:isCrossPlatformTransfer:
+ _objc_msgSend$initWithPlans:showOtherOption:
+ _objc_msgSend$initWithSecureIntentRejected
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$mergeByTransferCapabilities:
+ _sFormattedCarrierListFromSet
- -[CTDisplayPlan(SimSetup) detailsForViewController]
- -[SSConfirmationCodeViewController _textFieldDidChange]
- -[SSVisitStoreViewController initWithPlans:]
- -[TSTransferListViewController sectionFooter]
- -[TSTransferListViewController setSectionFooter:]
- GCC_except_table23
- GCC_except_table47
- _CTCellularPlanErroreSIMLimitReachedDueToRegulatory_COMPAT
- _CTPlanTransferCapabilityNotSupportedReachedRegulatoryeSIMLimit_COMPAT
- _OBJC_IVAR_$_TSTransferListViewController._sectionFooter
- ___57-[TSCrossPlatformTargetTransferFlow firstViewController:]_block_invoke.23
- ___block_literal_global.80
- ___block_literal_global.86
- _objc_msgSend$_isAnyRequireStoreVisitPlan:
- _objc_msgSend$_isAnySourceNeedsSoftwareUpdatePlan:
- _objc_msgSend$detailsForViewController
- _objc_msgSend$initWithCarrier:phoneNumber:transferCapability:showOtherOptions:entryPoint:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:
CStrings:
+ "%@%@ %@ %@"
+ "-[NSArray(CTDisplayPlan) getCombinedTitleAndDetailsForTransferCapability:title:detail:]"
+ "-[TSTransferCloudFlow nextViewControllerFrom:]"
+ "COMBINED_MULTI_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_INELIGIBLE_DETAIL_%@_%@"
+ "COMBINED_SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_INELIGIBLE_DETAIL_%@_%@"
+ "COMBINED_SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_INELIGIBLE_DETAIL_ACTIVATION_POLICY_MISMATCH_CARRIER_UNLOCK_%@"
+ "COMBINED_SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_MISSING_CERTIFICATE_%@"
+ "COMBINED_SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_REGULATORY_RESTRICTED_%@"
+ "COMBINED_SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_UNREGULATORY_RESTRICTED_%@"
+ "COMBINED_TRANSFER_INELIGIBLE_FOR_NOW_PLAN_DETAIL_%@_%@"
+ "COMBINED_TRANSFER_SOURCE_UPDATE_REQUIRED_DETAIL_%@"
+ "COMBINED_TRANSFER_TARGET_UPDATE_REQUIRED_DETAIL_%@"
+ "CROSSPLATFORM_TRANSFER_FAIL_ON_SOURCE_NUMBER_CROSSPLATFORM_MODEL_BUDDY"
+ "CROSSPLATFORM_TRANSFER_FAIL_ON_SOURCE_NUMBER_CROSSPLATFORM_MODEL_DELAYED_%@"
+ "CROSSPLATFORM_TRANSFER_FAIL_ON_SOURCE_NUMBER_CROSSPLATFORM_MODEL_SECURENT_INTENT_REJECTED"
+ "CROSSPLATFORM_TRANSFER_FAIL_TITLE_BUDDY"
+ "CROSSPLATFORM_TRANSFER_FAIL_TITLE_DELAYED"
+ "CROSSPLATFORM_TRANSFER_FAIL_TITLE_SECURENT_INTENT_REJECTED"
+ "CROSSPLATFORM_TRANSFER_NO_SIM_FOR_TRANSFER"
+ "CROSSPLATFORM_TRANSFER_NO_SIM_FOR_TRANSFER_DETAIL"
+ "CategorizedPlans"
+ "MULTISIM_INELIGIBLE_TRANSFER_PLANS_TITLE"
+ "MULTI_TRANSFER_PLAN_LABELS_SECTION_FOOTER_VISIT_STORE_%@"
+ "SINGLE_TRANSFER_PLAN_LABELS_SECTION_FOOTER_VISIT_STORE_%@"
+ "TB,V_isSecureIntentRejected"
+ "TRANSFER_PLAN_LABELS_SECTION_FOOTER_CARRIER_UNLOCK_%@"
+ "TRANSFER_PLAN_LABELS_SECTION_FOOTER_MISSING_CERTIFICATE_%@"
+ "TRANSFER_PLAN_LABELS_SECTION_FOOTER_REQUIRE_SOURCE_SOFTWARE_UPDATE_%@"
+ "TRANSFER_PLAN_LABELS_SECTION_FOOTER_REQUIRE_TARGET_SOFTWARE_UPDATE_%@"
+ "TRANSFER_PLAN_LABELS_SECTION_FOOTER_USE_TRANSFER_FROM_NEARBY_%@_BUDDY"
+ "VISIT_STORE_FOR_TRANSFER_DETAIL_%@"
+ "VISIT_STORE_FOR_WARNING_DETAIL_%@"
+ "_configureNavigationItem"
+ "_isForCrossPlatform"
+ "_isSecureIntentRejected"
+ "_noSIMOrNoEligibleSIMOnSource"
+ "_showOtherOption"
+ "_textFieldDidBegin"
+ "_textFieldDidEnd"
+ "dictionaryWithPlansByGroupByTransferCapability:"
+ "getCombinedFooterForNonTransferablePlans"
+ "getCombinedTitleAndDetailsForNonTransferablePlans:details:"
+ "getCombinedTitleAndDetailsForTransferCapability:title:detail:"
+ "initShowErrorOnSourceWithDelayedDownloadECSWithPlanIdentifier:"
+ "initShowNoSIMForCrossPlatformTransfer"
+ "initWithPlans:isCrossPlatformTransfer:"
+ "initWithPlans:showOtherOption:"
+ "initWithSecureIntentRejected"
+ "isEqualToNumber:"
+ "isSecureIntentRejected"
+ "kCrossTransferSecureIntentRejected"
+ "mergeByTransferCapabilities:"
+ "setIsSecureIntentRejected:"
+ "v32@0:8^@16^@24"
+ "v40@0:8Q16^@24^@32"
- "-[CTDisplayPlan(SimSetup) detailsForViewController]"
- "@\"UITableViewCell\""
- "T@\"UITableViewCell\",&,V_sectionFooter"
- "TRANSFER_INELIGIBLE_PLAN_DETAIL_%@"
- "VERIFICATION_COMPLETE"
- "VISIT_STORE_DETAIL_%@"
- "_sectionFooter"
- "detailsForViewController"
- "sectionFooter"
- "setSectionFooter:"
- "unexpected transfer capability : %s @%s"

```
