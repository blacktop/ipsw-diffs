## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-871.3.0.0.0
-  __TEXT.__text: 0xb3bc0
+874.1.0.0.0
+  __TEXT.__text: 0xb7594
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0xa00c
-  __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x1ca0
-  __TEXT.__cstring: 0xfb5d
-  __TEXT.__oslogstring: 0x65f6
+  __TEXT.__objc_methlist: 0xa2b4
+  __TEXT.__const: 0x1d8
+  __TEXT.__gcc_except_tab: 0x1db8
+  __TEXT.__cstring: 0x10092
+  __TEXT.__oslogstring: 0x6acb
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2530
-  __TEXT.__objc_classname: 0x158c
-  __TEXT.__objc_methname: 0x16622
-  __TEXT.__objc_methtype: 0x354f
-  __TEXT.__objc_stubs: 0xe1a0
-  __DATA_CONST.__got: 0xa70
-  __DATA_CONST.__const: 0x1d50
-  __DATA_CONST.__objc_classlist: 0x480
-  __DATA_CONST.__objc_catlist: 0x58
+  __TEXT.__unwind_info: 0x2600
+  __TEXT.__objc_classname: 0x15cf
+  __TEXT.__objc_methname: 0x16c24
+  __TEXT.__objc_methtype: 0x355e
+  __TEXT.__objc_stubs: 0xe500
+  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__const: 0x1db0
+  __DATA_CONST.__objc_classlist: 0x488
+  __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50e8
+  __DATA_CONST.__objc_selrefs: 0x5238
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x428
-  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_superrefs: 0x430
+  __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0x74e0
-  __AUTH_CONST.__objc_const: 0x3d2a8
-  __AUTH_CONST.__objc_intobj: 0x570
+  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__cfstring: 0x7640
+  __AUTH_CONST.__objc_const: 0x3dea0
+  __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x2cb0
-  __DATA.__objc_ivar: 0xec0
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH.__objc_data: 0x2d00
+  __DATA.__objc_ivar: 0xee8
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0C456A9-6B2D-300B-955A-CA5C4DFF4FCD
-  Functions: 3874
-  Symbols:   14035
-  CStrings:  7376
+  UUID: 3D07AE94-3C1D-35ED-830A-8AF185F3E3C6
+  Functions: 3948
+  Symbols:   14268
+  CStrings:  7492
 
Symbols:
+ +[TSNoPlanForTransferViewController getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isVisitStoreRequired:]
+ +[TSNoPlanForTransferViewController getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isVisitStoreRequired:].cold.1
+ +[TSUtilities displayPlanFromObject:]
+ -[CTDisplayPlan(SimSetup) detailsForViewController]
+ -[CTDisplayPlan(SimSetup) installRestriction]
+ -[NSArray(CTDisplayPlan) carrierNames]
+ -[NSArray(CTDisplayPlan) filteredPlansForHiddenInCloudBucket:]
+ -[NSArray(CTDisplayPlan) filteredPlansForNonInstallableBucket]
+ -[NSArray(CTDisplayPlan) filteredPlansForNonQRCodeBucket]
+ -[NSArray(CTDisplayPlan) filteredPlansForQRCodeBucket]
+ -[NSArray(CTDisplayPlan) filteredPlansForSoftwareUpdateBucket]
+ -[NSArray(CTDisplayPlan) filteredPlansForTransferableBucket]
+ -[NSArray(CTDisplayPlan) filteredPlansForVisitStoreBucket]
+ -[NSArray(CTDisplayPlan) filteredPlansWithTransferCapabilities:restrictionAllowed:]
+ -[NSArray(CTDisplayPlan) filteredPlansWithTransferCapability:]
+ -[NSMutableArray(CTDisplayPlan) filteredPlansWithoutSODATether:]
+ -[NSSet(NSString) containsStringCaseInsensitive:]
+ -[SSCrossPlatformTransferSourceSelectionViewController _skipButtonTapped]
+ -[SSQRCodeIntroViewController _otherButtonTapped:]
+ -[SSQRCodeIntroViewController entryPoint]
+ -[SSQRCodeIntroViewController initWithPlans:withBackButton:]
+ -[SSQRCodeIntroViewController isOtherButtonTapped]
+ -[SSQRCodeIntroViewController isStartOverRequiredOnBackButtonTapped]
+ -[SSQRCodeIntroViewController setEntryPoint:]
+ -[SSQRCodeIntroViewController setIsOtherButtonTapped:]
+ -[SSQRCodeIntroViewController setWithBackButton:]
+ -[SSQRCodeIntroViewController withBackButton]
+ -[SSeSIMCountRestrictionWarningViewController .cxx_destruct]
+ -[SSeSIMCountRestrictionWarningViewController _continueButtonTapped]
+ -[SSeSIMCountRestrictionWarningViewController delegate]
+ -[SSeSIMCountRestrictionWarningViewController init]
+ -[SSeSIMCountRestrictionWarningViewController setDelegate:]
+ -[SSeSIMCountRestrictionWarningViewController viewDidLoad]
+ -[TSActivationFlowWithSimSetupFlow nextViewControllerFrom:].cold.1
+ -[TSActivationFlowWithSimSetupFlow setCancelNavigationBarItems:]
+ -[TSActivationFlowWithSimSetupFlow setTransferPlans:]
+ -[TSActivationFlowWithSimSetupFlow transferPlans]
+ -[TSBootstrapCrossPlatformTransferFlow flowCompleted:]
+ -[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) setCancelNavigationBarItems:]
+ -[TSCrossPlatformTargetTransferFlow session]
+ -[TSCrossPlatformTargetTransferFlow setSession:]
+ -[TSMultiPlanIntermediateViewController _prepareCellInformationWithPendingInstallPlans:transferPlans:carrierSetupPlans:isHiddenPlanSelectable:]
+ -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:]
+ -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:].cold.1
+ -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:].cold.2
+ -[TSMultiPlanIntermediateViewController installBucketSubtitle]
+ -[TSMultiPlanIntermediateViewController installBucketTitle]
+ -[TSMultiPlanIntermediateViewController nonMagnoliaCount]
+ -[TSMultiPlanIntermediateViewController qrcodeBucketSubtitle]
+ -[TSMultiPlanIntermediateViewController qrcodeBucketTitle]
+ -[TSMultiPlanIntermediateViewController setInstallBucketSubtitle:]
+ -[TSMultiPlanIntermediateViewController setInstallBucketTitle:]
+ -[TSMultiPlanIntermediateViewController setNonMagnoliaCount:]
+ -[TSMultiPlanIntermediateViewController setQrcodeBucketSubtitle:]
+ -[TSMultiPlanIntermediateViewController setQrcodeBucketTitle:]
+ -[TSNoPlanForTransferViewController initWithCarrier:phoneNumber:transferCapability:showOtherOptions:entryPoint:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isStartOverNeeded:]
+ -[TSNoPlanForTransferViewController initWithPlans:showOtherOptions:]
+ -[TSNoPlanForTransferViewController initWithPlans:showOtherOptions:isStartOverNeeded:]
+ -[TSNoPlanForTransferViewController isStartOverNeeded]
+ -[TSNoPlanForTransferViewController setIsStartOverNeeded:]
+ -[TSOnDeviceConversionFlow setCancelNavigationBarItems:]
+ -[TSPostMigrationFlow startOverWithFirstViewController:]
+ -[TSProximityPINCodeViewController backOption]
+ -[TSProximityTargetTransferFlow setCancelNavigationBarItems:]
+ -[TSQRCodeScanFlow setCancelNavigationBarItems:]
+ -[TSSIMSetupFlow flowCompleted:]
+ -[TSSIMSetupPublicApiInstallFlow setCancelNavigationBarItems:]
+ -[TSSetupAssistantSIMSetupFlow setCancelNavigationBarItems:]
+ -[TSTargetReconnectWaitingViewController backOption]
+ -[TSTransferCloudFlow setCancelNavigationBarItems:]
+ -[TSTransferCloudFlowModel setTransferPlans:]
+ -[TSTransferCloudFlowModel transferPlans]
+ -[TSTransferFlow setCancelNavigationBarItems:]
+ -[TSTransferFlowModel setTransferPlans:]
+ -[TSTransferFlowModel transferPlans]
+ -[TSTransferListViewController initWithTransferPlans:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:]
+ -[TSTransferListViewController setTransferPlans:]
+ -[TSTransferListViewController transferPlans]
+ -[TSTravelBuddyViewController _getSubTextForSection:]
+ -[TSTravelBuddyViewController _getSubTextToDisplay:carrierName:]
+ -[TSTravelBuddyViewController _isPlanRegisteredForIMessage:]
+ -[TSTravelBuddyViewController _isPlanRegisteredForIMessage:].cold.1
+ -[TSTravelBuddyViewController _isSubscriptionReadyForTravel4FF:]
+ -[TSTravelBuddyViewController _isSubscriptionReadyForTravel4FF:].cold.1
+ -[TSTravelBuddyViewController isDualSIMConfig]
+ -[TSTravelBuddyViewController prevTravelOnlySelection]
+ -[TSTravelBuddyViewController setIsDualSIMConfig:]
+ -[TSTravelBuddyViewController setPrevTravelOnlySelection:]
+ -[TSUserResponseFlow setCancelNavigationBarItems:]
+ -[TSWebsheetSignupFlow setCancelNavigationBarItems:]
+ -[UIViewController(SimSetup) configureNavigationItem]
+ -[UIViewController(SimSetup) configureNavigationItem].cold.1
+ -[UIViewController(SimSetup) dismissSimSetupFlowFromViewController]
+ -[UIViewController(SimSetup) dismissSimSetupFlowFromViewController].cold.1
+ -[UIViewController(SimSetup) isCloudFlow]
+ -[UIViewController(SimSetup) isCloudFlow].cold.1
+ -[UIViewController(SimSetup) isCloudFlow].cold.2
+ -[UIViewController(SimSetup) userDidTapCancel]
+ -[UIViewController(SimSetup) userDidTapCancel].cold.1
+ GCC_except_table36
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table94
+ GCC_except_table97
+ _CTCellularPlanErroreSIMLimitReachedDueToRegulatory_COMPAT
+ _CTPlanTransferCapabilityNotSupportedReachedRegulatoryeSIMLimit_COMPAT
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_SSeSIMCountRestrictionWarningViewController
+ _OBJC_IVAR_$_SSQRCodeIntroViewController._entryPoint
+ _OBJC_IVAR_$_SSQRCodeIntroViewController._isOtherButtonTapped
+ _OBJC_IVAR_$_SSQRCodeIntroViewController._withBackButton
+ _OBJC_IVAR_$_SSeSIMCountRestrictionWarningViewController._delegate
+ _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._transferPlans
+ _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._session
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._installBucketSubtitle
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._installBucketTitle
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._nonMagnoliaCount
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._qrcodeBucketSubtitle
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._qrcodeBucketTitle
+ _OBJC_IVAR_$_TSNoPlanForTransferViewController._isStartOverNeeded
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._transferPlans
+ _OBJC_IVAR_$_TSTransferFlowModel._transferPlans
+ _OBJC_IVAR_$_TSTransferListViewController._transferPlans
+ _OBJC_IVAR_$_TSTravelBuddyViewController._homeIccidPlanItem
+ _OBJC_IVAR_$_TSTravelBuddyViewController._secondHomeIccidPlanItem
+ _OBJC_IVAR_$_TSTravelBuddyViewController._travelIccidPlanItem
+ _OBJC_METACLASS_$_SSeSIMCountRestrictionWarningViewController
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_CTDisplayPlan
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableArray_$_CTDisplayPlan
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSSet_$_NSString
+ __OBJC_$_CATEGORY_NSArray_$_CTDisplayPlan
+ __OBJC_$_CATEGORY_NSMutableArray_$_CTDisplayPlan
+ __OBJC_$_CATEGORY_NSSet_$_NSString
+ __OBJC_$_INSTANCE_METHODS_SSeSIMCountRestrictionWarningViewController
+ __OBJC_$_INSTANCE_METHODS_UIViewController(Flow|InModalPresentation|SubFlow|SimSetup|NavigationBar)
+ __OBJC_$_INSTANCE_VARIABLES_SSeSIMCountRestrictionWarningViewController
+ __OBJC_$_PROP_LIST_SSeSIMCountRestrictionWarningViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSeSIMCountRestrictionWarningViewController
+ __OBJC_CLASS_RO_$_SSeSIMCountRestrictionWarningViewController
+ __OBJC_METACLASS_RO_$_SSeSIMCountRestrictionWarningViewController
+ ___32-[TSQRCodeScanFlow handleError:]_block_invoke_6
+ ___32-[TSQRCodeScanFlow handleError:]_block_invoke_7
+ ___39-[TSTransferFlow _firstViewController:]_block_invoke.218
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.218
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.220
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.219
+ ___53-[TSTravelBuddyViewController _continueButtonTapped:]_block_invoke.116
+ ___53-[TSTravelBuddyViewController _continueButtonTapped:]_block_invoke.cold.1
+ ___57-[TSCrossPlatformTargetTransferFlow firstViewController:]_block_invoke.cold.1
+ ___57-[TSCrossPlatformTargetTransferFlow firstViewController:]_block_invoke.cold.2
+ ___58-[NSArray(CTDisplayPlan) filteredPlansForVisitStoreBucket]_block_invoke
+ ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.172
+ ___62-[NSArray(CTDisplayPlan) filteredPlansForHiddenInCloudBucket:]_block_invoke
+ ___62-[NSArray(CTDisplayPlan) filteredPlansWithTransferCapability:]_block_invoke
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.181
+ ___64-[NSMutableArray(CTDisplayPlan) filteredPlansWithoutSODATether:]_block_invoke
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.103.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.104
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.104.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.105
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.105.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.106
+ ___64-[TSTravelBuddyViewController _isSubscriptionReadyForTravel4FF:]_block_invoke
+ ___64-[TSTravelBuddyViewController _isSubscriptionReadyForTravel4FF:]_block_invoke.cold.1
+ ___67-[UIViewController(SimSetup) dismissSimSetupFlowFromViewController]_block_invoke
+ ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.114
+ ___73-[SSCrossPlatformTransferSourceSelectionViewController _skipButtonTapped]_block_invoke
+ ___73-[SSCrossPlatformTransferSourceSelectionViewController _skipButtonTapped]_block_invoke.cold.1
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.108
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.108.cold.1
+ ___83-[NSArray(CTDisplayPlan) filteredPlansWithTransferCapabilities:restrictionAllowed:]_block_invoke
+ ___86-[TSNoPlanForTransferViewController initWithPlans:showOtherOptions:isStartOverNeeded:]_block_invoke
+ ___block_descriptor_32_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_32_e41_q24?0"CTDisplayPlan"8"CTDisplayPlan"16l
+ ___block_descriptor_33_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_41_e8_32s_e25_B24?08"NSDictionary"16ls32l8
+ ___block_descriptor_73_e8_32s40s48s56r64w_e61_v32?0"NSArray"8"CTDisplayPlanList"16"CTDisplayPlanList"24lr56l8s32l8w64l8s40l8s48l8
+ ___block_literal_global.222
+ ___block_literal_global.680
+ ___block_literal_global.709
+ ___block_literal_global.769
+ ___block_literal_global.87
+ ___block_literal_global.90
+ _objc_msgSend$_getSubTextForSection:
+ _objc_msgSend$_getSubTextToDisplay:carrierName:
+ _objc_msgSend$_isPlanRegisteredForIMessage:
+ _objc_msgSend$_isSubscriptionReadyForTravel4FF:
+ _objc_msgSend$_prepareCellInformationWithPendingInstallPlans:transferPlans:carrierSetupPlans:isHiddenPlanSelectable:
+ _objc_msgSend$carrierNames
+ _objc_msgSend$configureNavigationItem
+ _objc_msgSend$containsStringCaseInsensitive:
+ _objc_msgSend$currentLocale
+ _objc_msgSend$detailsForViewController
+ _objc_msgSend$dismissSimSetupFlowFromViewController
+ _objc_msgSend$displayPlanFromObject:
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$filteredPlansForHiddenInCloudBucket:
+ _objc_msgSend$filteredPlansForNonInstallableBucket
+ _objc_msgSend$filteredPlansForNonQRCodeBucket
+ _objc_msgSend$filteredPlansForQRCodeBucket
+ _objc_msgSend$filteredPlansForSoftwareUpdateBucket
+ _objc_msgSend$filteredPlansForTransferableBucket
+ _objc_msgSend$filteredPlansForVisitStoreBucket
+ _objc_msgSend$filteredPlansWithTransferCapabilities:restrictionAllowed:
+ _objc_msgSend$filteredPlansWithoutSODATether:
+ _objc_msgSend$flowCompleted:
+ _objc_msgSend$getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isVisitStoreRequired:
+ _objc_msgSend$initWithCarrier:phoneNumber:transferCapability:showOtherOptions:entryPoint:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isStartOverNeeded:
+ _objc_msgSend$initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:
+ _objc_msgSend$initWithPlans:showOtherOptions:
+ _objc_msgSend$initWithPlans:showOtherOptions:isStartOverNeeded:
+ _objc_msgSend$initWithPlans:withBackButton:
+ _objc_msgSend$initWithTransferPlans:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:
+ _objc_msgSend$installRestriction
+ _objc_msgSend$isCloudFlow
+ _objc_msgSend$labelId
+ _objc_msgSend$setCancelNavigationBarItems:
+ _objc_msgSend$string
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$transferPlans
+ _objc_msgSend$uppercaseStringWithLocale:
- +[TSNoPlanForTransferViewController getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:]
- +[TSNoPlanForTransferViewController getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:].cold.1
- -[NSArray(SimSetup) filteredPlansRequiresScanOption]
- -[NSArray(SimSetup) filteredPlansWithTransferCapabilities:]
- -[NSArray(SimSetup) filteredPlansWithTransferCapability:]
- -[SSQRCodeIntroViewController initWithPlans:]
- -[TSActivationFlowWithSimSetupFlow setDefaultNavigationItems:]
- -[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) setDefaultNavigationItems:]
- -[TSMultiPlanIntermediateViewController _heightAnchorConstant]
- -[TSMultiPlanIntermediateViewController hiddenInCloudFlowPlans]
- -[TSMultiPlanIntermediateViewController initWithPendingInstallItems:]
- -[TSMultiPlanIntermediateViewController initWithPendingInstallItems:].cold.1
- -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:].cold.1
- -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:showQrCodeOption:transferIneligiblePlans:hiddenInCloudFlowPlans:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:].cold.1
- -[TSMultiPlanIntermediateViewController plansWithScanOption]
- -[TSMultiPlanIntermediateViewController setHiddenInCloudFlowPlans:]
- -[TSMultiPlanIntermediateViewController setPlansWithScanOption:]
- -[TSMultiPlanIntermediateViewController setSwUpdatePlans:]
- -[TSMultiPlanIntermediateViewController swUpdatePlans]
- -[TSNoPlanForTransferViewController initWithPlans:]
- -[TSOnDeviceConversionFlow setDefaultNavigationItems:]
- -[TSProximityTargetTransferFlow setDefaultNavigationItems:]
- -[TSQRCodeScanFlow setDefaultNavigationItems:]
- -[TSSIMSetupPublicApiInstallFlow setDefaultNavigationItems:]
- -[TSSetupAssistantSIMSetupFlow setDefaultNavigationItems:]
- -[TSTransferCloudFlow setDefaultNavigationItems:]
- -[TSTransferFlow setDefaultNavigationItems:]
- -[TSTransferListViewController getRemoteDeviceDisplayName:]
- -[TSTransferListViewController setTransferItems:]
- -[TSTransferListViewController transferItems]
- -[TSTravelBuddyViewController _shouldPlanBeRegisteredForIMessage:]
- -[TSTravelBuddyViewController _shouldPlanBeRegisteredForIMessage:].cold.1
- -[TSTravelBuddyViewController _shouldPlanBeRegisteredForIMessage:].cold.2
- -[TSUserResponseFlow setDefaultNavigationItems:]
- -[TSWebsheetSignupFlow setDefaultNavigationItems:]
- GCC_except_table45
- GCC_except_table52
- GCC_except_table58
- GCC_except_table80
- GCC_except_table87
- GCC_except_table93
- GCC_except_table95
- _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._carrierSetupItems
- _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._hiddenInCloudFlowPlans
- _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._pendingInstallItems
- _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._plansWithScanOption
- _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._swUpdatePlans
- _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._tableHeightAnchor
- _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._transferItems
- _OBJC_IVAR_$_TSTransferListViewController._transferItems
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_SimSetup
- __OBJC_$_CATEGORY_NSArray_$_SimSetup
- __OBJC_$_INSTANCE_METHODS_UIViewController(Flow|InModalPresentation|SubFlow|NavigationBar)
- ___39-[TSTransferFlow _firstViewController:]_block_invoke.217
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.211
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.213
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.212
- ___57-[NSArray(SimSetup) filteredPlansWithTransferCapability:]_block_invoke
- ___59-[NSArray(SimSetup) filteredPlansWithTransferCapabilities:]_block_invoke
- ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.165
- ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.186
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.100
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.100.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.101
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.101.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.102
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.102.cold.1
- ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.111
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.105
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.105.cold.1
- ___80-[TSSIMSetupFlow handleStartOverWithEntryPoint:navigationController:completion:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e38_v24?0"CUMessageSession"8"NSError"16ls40l8s32l8
- ___block_descriptor_65_e8_32s40s48r56w_e61_v32?0"NSArray"8"CTDisplayPlanList"16"CTDisplayPlanList"24lr48l8w56l8s32l8s40l8
- ___block_literal_global.215
- ___block_literal_global.672
- ___block_literal_global.702
- ___block_literal_global.762
- ___block_literal_global.88
- _objc_msgSend$_shouldDisplayPhoneNumber:
- _objc_msgSend$allPlansRequireSoftwareUpdate:
- _objc_msgSend$filteredPlansRequiresScanOption
- _objc_msgSend$filteredPlansWithTransferCapabilities:
- _objc_msgSend$getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:
- _objc_msgSend$initWithPendingInstallItems:
- _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:allowsMultiSelection:
- _objc_msgSend$initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:
- _objc_msgSend$initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:
- _objc_msgSend$initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:
- _objc_msgSend$isTransferNotSupportedFromiPhone
- _sIsAnyPlanTransferable
CStrings:
+ "\n\n"
+ "+[TSNoPlanForTransferViewController getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isVisitStoreRequired:]"
+ ","
+ "-[CTDisplayPlan(SimSetup) detailsForViewController]"
+ "-[NSMutableArray(CTDisplayPlan) filteredPlansWithoutSODATether:]_block_invoke"
+ "-[SSCrossPlatformTransferSourceSelectionViewController _skipButtonTapped]"
+ "-[SSCrossPlatformTransferSourceSelectionViewController _skipButtonTapped]_block_invoke"
+ "-[TSActivationFlowWithSimSetupFlow _createFirstViewController:]"
+ "-[TSBootstrapCrossPlatformTransferFlow flowCompleted:]"
+ "-[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:]"
+ "-[TSTravelBuddyViewController _continueButtonTapped:]_block_invoke"
+ "-[TSTravelBuddyViewController _isPlanRegisteredForIMessage:]"
+ "-[TSTravelBuddyViewController _isSubscriptionReadyForTravel4FF:]"
+ "-[TSTravelBuddyViewController _isSubscriptionReadyForTravel4FF:]_block_invoke"
+ "-[UIViewController(SimSetup) configureNavigationItem]"
+ "-[UIViewController(SimSetup) dismissSimSetupFlowFromViewController]"
+ "-[UIViewController(SimSetup) dismissSimSetupFlowFromViewController]_block_invoke"
+ "-[UIViewController(SimSetup) isCloudFlow]"
+ "-[UIViewController(SimSetup) userDidTapCancel]"
+ "@60@0:8@16@24@32B40B44B48B52B56"
+ "@60@0:8Q16@24@32@40B48B52B56"
+ "@72@0:8@16@24Q32B40Q44@52B60B64B68"
+ "Account member plan (%@) with a SODA tether @%s"
+ "CTDisplayPlan"
+ "Data+eSIM case,topview is SSCrossPlatformTransferSourceSelectionViewController and source received end session(skip or carrier lock on target case), exit flow @%s"
+ "Dismissing modal presentation from root: %@ @%s"
+ "ESIM_COUNT_RESTRICTION_WARNING_DETAIL"
+ "ESIM_COUNT_RESTRICTION_WARNING_TITLE"
+ "FlowCompleted: %lu release retained mk object @%s"
+ "Modal presentation dismissed successfully @%s"
+ "NSString"
+ "No modal presentation to dismiss @%s"
+ "SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_UNKNOWN_LOCATION_BUDDY"
+ "SSeSIMCountRestrictionWarningViewController"
+ "Setting _travelIccidPlanItem (%@) @%s"
+ "Subscription context UUID is not ready for travel plan item @%s"
+ "Subscription context for travel 4FF (%@) is ready. @%s"
+ "Subscription is not ready for travel 4FF (%@) @%s"
+ "T@\"NSArray\",&,V_transferPlans"
+ "T@\"NSMutableArray\",&,N,V_transferPlans"
+ "T@\"NSMutableArray\",&,V_transferPlans"
+ "T@\"NSString\",&,V_installBucketSubtitle"
+ "T@\"NSString\",&,V_installBucketTitle"
+ "T@\"NSString\",&,V_qrcodeBucketSubtitle"
+ "T@\"NSString\",&,V_qrcodeBucketTitle"
+ "TB,V_isDualSIMConfig"
+ "TB,V_isStartOverNeeded"
+ "TB,V_prevTravelOnlySelection"
+ "TQ,V_nonMagnoliaCount"
+ "TRANSFER_INELIGIBLE_PLAN_DETAIL_%@"
+ "TRANSFER_PLAN_LABELS_SECTION_FOOTER_USE_TRANSFER_FROM_NEARBY_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATAONLY_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATAONLY_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_DATAONLY_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_DATAONLY_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_NO_IMSG_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_NO_IMSG_ON_ONE_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_NO_IMSG_DETAILS_%@"
+ "Websheet-inbuddy plan (%@) with a SODA tether @%s"
+ "[E]%@ doesnot conform to TSSetuFlowItem @%s"
+ "[E]%@(%p) doesnot have a delegate @%s"
+ "[E]Failed to find plan item for travel 4FF @%s"
+ "[E]delegate not set @%s"
+ "[E]invalid message session @%s"
+ "[E]no installable plans. showing intermediate pane is unexpected @%s"
+ "[E]unexpected @%s"
+ "_getSubTextForSection:"
+ "_getSubTextToDisplay:carrierName:"
+ "_homeIccidPlanItem"
+ "_installBucketSubtitle"
+ "_installBucketTitle"
+ "_isPlanRegisteredForIMessage:"
+ "_isStartOverNeeded"
+ "_isSubscriptionReadyForTravel4FF:"
+ "_nonMagnoliaCount"
+ "_otherButtonTapped:"
+ "_prepareCellInformationWithPendingInstallPlans:transferPlans:carrierSetupPlans:isHiddenPlanSelectable:"
+ "_qrcodeBucketSubtitle"
+ "_qrcodeBucketTitle"
+ "_secondHomeIccidPlanItem"
+ "_transferPlans"
+ "_travelIccidPlanItem"
+ "als:%lu, soda:%{bool}d @%s"
+ "carrierNames"
+ "configureNavigationItem"
+ "containsStringCaseInsensitive:"
+ "currentLocale"
+ "detailsForViewController"
+ "dismissSimSetupFlowFromViewController"
+ "displayPlanFromObject:"
+ "filterUsingPredicate:"
+ "filteredPlansForHiddenInCloudBucket:"
+ "filteredPlansForNonInstallableBucket"
+ "filteredPlansForNonQRCodeBucket"
+ "filteredPlansForQRCodeBucket"
+ "filteredPlansForSoftwareUpdateBucket"
+ "filteredPlansForTransferableBucket"
+ "filteredPlansForVisitStoreBucket"
+ "filteredPlansWithTransferCapabilities:restrictionAllowed:"
+ "filteredPlansWithoutSODATether:"
+ "flowCompleted:"
+ "getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isVisitStoreRequired:"
+ "initWithCarrier:phoneNumber:transferCapability:showOtherOptions:entryPoint:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isStartOverNeeded:"
+ "initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:"
+ "initWithPlans:showOtherOptions:"
+ "initWithPlans:showOtherOptions:isStartOverNeeded:"
+ "initWithPlans:withBackButton:"
+ "initWithTransferPlans:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:"
+ "installBucketSubtitle"
+ "installBucketTitle"
+ "installRestriction"
+ "isCloudFlow"
+ "isDualSIMConfig"
+ "isStartOverNeeded"
+ "labelId"
+ "nonMagnoliaCount"
+ "prevTravelOnlySelection"
+ "q24@?0@\"CTDisplayPlan\"8@\"CTDisplayPlan\"16"
+ "qrcodeBucketSubtitle"
+ "qrcodeBucketTitle"
+ "setCancelNavigationBarItems:"
+ "setInstallBucketSubtitle:"
+ "setInstallBucketTitle:"
+ "setIsDualSIMConfig:"
+ "setIsStartOverNeeded:"
+ "setNonMagnoliaCount:"
+ "setPrevTravelOnlySelection:"
+ "setQrcodeBucketSubtitle:"
+ "setQrcodeBucketTitle:"
+ "setTransferPlans:"
+ "skip button tapped, cancel the flow, send empty selection @%s"
+ "soda : %{bool}d @%s"
+ "string"
+ "substringFromIndex:"
+ "transferPlans"
+ "transferable:%lu (store:%lu), software update:%lu (store:%lu), qrcode:%lu, non install:%lu @%s"
+ "transferable:%lu (store:%lu, hidden:%lu), software update:%lu (store:%lu), qrcode:%lu, non install:%lu @%s"
+ "unexpected transfer capability : %s @%s"
+ "uppercaseStringWithLocale:"
+ "\xf0a"
- "+"
- "+[TSNoPlanForTransferViewController getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:]"
- "-[TSBootstrapCrossPlatformTransferFlow nextViewControllerFrom:]"
- "-[TSMultiPlanIntermediateViewController initWithPendingInstallItems:]"
- "-[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:]"
- "-[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:]"
- "-[TSTravelBuddyViewController _shouldPlanBeRegisteredForIMessage:]"
- "@56@0:8@16B24B28@32@40@48"
- "@56@0:8Q16@24@32@40B48B52"
- "@64@0:8@16@24@32B40B44@48@56"
- "MULTI_ALS_SUBTEXT_WITH_COUNT_%lu"
- "MULTI_ESIM_TRANSFER_FILTERED_DETAIL"
- "MULTI_ESIM_TRANSFER_FILTERED_QR_CODE_DETAIL"
- "MULTI_ESIM_TRANSFER_FILTERED_TITLE"
- "T@\"NSArray\",&,V_hiddenInCloudFlowPlans"
- "T@\"NSArray\",&,V_plansWithScanOption"
- "T@\"NSArray\",&,V_swUpdatePlans"
- "T@\"NSArray\",&,V_transferItems"
- "TRANSFER_INELIGIBLE_PLANS"
- "TRANSFER_INELIGIBLE_PLANS_DETAIL"
- "[E]Invalid uuid for item: %@. @%s"
- "_hiddenInCloudFlowPlans"
- "_plansWithScanOption"
- "_shouldPlanBeRegisteredForIMessage:"
- "_swUpdatePlans"
- "filteredPlansRequiresScanOption"
- "filteredPlansWithTransferCapabilities:"
- "getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:"
- "hiddenInCloudFlowPlans"
- "initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:"
- "initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:showQrCodeOption:transferIneligiblePlans:hiddenInCloudFlowPlans:"
- "initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:"
- "initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:"
- "plansWithScanOption"
- "setHiddenInCloudFlowPlans:"
- "setPlansWithScanOption:"
- "setSwUpdatePlans:"
- "swUpdatePlans"
- "\xf01"

```
