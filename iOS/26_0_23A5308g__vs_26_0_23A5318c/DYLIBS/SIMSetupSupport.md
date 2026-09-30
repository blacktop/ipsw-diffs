## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-867.0.0.0.0
-  __TEXT.__text: 0xacbd8
+871.2.0.0.0
+  __TEXT.__text: 0xb3b14
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x9a14
-  __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x1c4c
-  __TEXT.__cstring: 0xf5a8
-  __TEXT.__oslogstring: 0x6331
+  __TEXT.__objc_methlist: 0xa00c
+  __TEXT.__const: 0x1b8
+  __TEXT.__gcc_except_tab: 0x1ca0
+  __TEXT.__cstring: 0xfb3e
+  __TEXT.__oslogstring: 0x65f6
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2440
-  __TEXT.__objc_classname: 0x1502
-  __TEXT.__objc_methname: 0x156a3
-  __TEXT.__objc_methtype: 0x3510
-  __TEXT.__objc_stubs: 0xdb40
-  __DATA_CONST.__got: 0xa40
-  __DATA_CONST.__const: 0x1d18
-  __DATA_CONST.__objc_classlist: 0x460
-  __DATA_CONST.__objc_catlist: 0x50
+  __TEXT.__unwind_info: 0x2530
+  __TEXT.__objc_classname: 0x158c
+  __TEXT.__objc_methname: 0x16622
+  __TEXT.__objc_methtype: 0x354f
+  __TEXT.__objc_stubs: 0xe1a0
+  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__const: 0x1d50
+  __DATA_CONST.__objc_classlist: 0x480
+  __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e38
+  __DATA_CONST.__objc_selrefs: 0x50e8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x400
-  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0x7220
-  __AUTH_CONST.__objc_const: 0x3b678
-  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0x74c0
+  __AUTH_CONST.__objc_const: 0x3d2a8
+  __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x2b70
-  __DATA.__objc_ivar: 0xe1c
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH.__objc_data: 0x2cb0
+  __DATA.__objc_ivar: 0xec0
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BF8CEC45-D4CA-354C-BC01-FF8D4950EFE6
-  Functions: 3728
-  Symbols:   13574
-  CStrings:  7160
+  UUID: F5436B68-F928-3922-A988-CFC0F28717FE
+  Functions: 3874
+  Symbols:   14035
+  CStrings:  7374
 
Symbols:
+ +[SSQRCodeIntroViewController getDetail:]
+ +[SSTransferIntroViewController getDetails:]
+ +[TSCellularPlanIntroViewController getDetailsWithTransferOption:showQRCodeOption:showCrossTransferOption:transferIneligiblePlans:]
+ +[TSUtilities FormattedCarrierListFromSet:]
+ +[TSUtilities _isAnyRequireStoreVisitPlan:]
+ +[TSUtilities _isAnySourceNeedsSoftwareUpdatePlan:]
+ +[TSUtilities allPlansRequireSoftwareUpdate:]
+ +[TSUtilities getStoreVisitStatusForPlan:cache:]
+ +[TSUtilities getStoreVisitStatusForPlan:cache:].cold.1
+ -[CTDisplayPlan(SimSetup) deviceName]
+ -[CTDisplayPlan(SimSetup) isPlanHiddenRequiredForCloudFlow]
+ -[CTDisplayPlan(SimSetup) requireVisitStoreOnce]
+ -[CrossPlatformTargetQRCodeWarningViewController .cxx_destruct]
+ -[CrossPlatformTargetQRCodeWarningViewController _cancelButtonTapped]
+ -[CrossPlatformTargetQRCodeWarningViewController _doneButtonTapped]
+ -[CrossPlatformTargetQRCodeWarningViewController _learnMoreTapped]
+ -[CrossPlatformTargetQRCodeWarningViewController _setupLaterButtonTapped]
+ -[CrossPlatformTargetQRCodeWarningViewController delegate]
+ -[CrossPlatformTargetQRCodeWarningViewController init]
+ -[CrossPlatformTargetQRCodeWarningViewController setDelegate:]
+ -[CrossPlatformTargetQRCodeWarningViewController viewDidLoad]
+ -[DCTCodeManager hasCode]
+ -[NSArray(SimSetup) filteredPlansRequiresScanOption]
+ -[NSArray(SimSetup) filteredPlansWithTransferCapabilities:]
+ -[NSArray(SimSetup) filteredPlansWithTransferCapability:]
+ -[SSQRCodeIntroViewController .cxx_destruct]
+ -[SSQRCodeIntroViewController _laterButtonTapped:]
+ -[SSQRCodeIntroViewController _scanButtonTapped:]
+ -[SSQRCodeIntroViewController delegate]
+ -[SSQRCodeIntroViewController initWithPlans:]
+ -[SSQRCodeIntroViewController isScanButtonTapped]
+ -[SSQRCodeIntroViewController setDelegate:]
+ -[SSQRCodeIntroViewController setIsScanButtonTapped:]
+ -[SSQRCodeIntroViewController viewDidLoad]
+ -[SSTransferIntroViewController .cxx_destruct]
+ -[SSTransferIntroViewController _laterButtonTapped:]
+ -[SSTransferIntroViewController _transferButtonTapped:]
+ -[SSTransferIntroViewController delegate]
+ -[SSTransferIntroViewController initWithItems:]
+ -[SSTransferIntroViewController isTransferButtonTapped]
+ -[SSTransferIntroViewController setDelegate:]
+ -[SSTransferIntroViewController setIsTransferButtonTapped:]
+ -[SSTransferIntroViewController viewDidLoad]
+ -[SSVisitStoreViewController .cxx_destruct]
+ -[SSVisitStoreViewController _continueButtonTapped:]
+ -[SSVisitStoreViewController _laterButtonTapped:]
+ -[SSVisitStoreViewController delegate]
+ -[SSVisitStoreViewController initWithPlans:]
+ -[SSVisitStoreViewController setDelegate:]
+ -[SSVisitStoreViewController viewDidLoad]
+ -[TSActivationFlowWithSimSetupFlow _maybePresentFirstViewController:firstViewControllerCallback:]
+ -[TSActivationFlowWithSimSetupFlow _maybePresentFirstViewController:firstViewControllerCallback:].cold.1
+ -[TSActivationFlowWithSimSetupFlow setTransferIneligibleViaCloudItems:]
+ -[TSActivationFlowWithSimSetupFlow setTransferItems:]
+ -[TSActivationFlowWithSimSetupFlow transferIneligibleViaCloudItems]
+ -[TSActivationFlowWithSimSetupFlow transferItems]
+ -[TSCellularPlanIntroViewController _isStandaloneQRCodeView]
+ -[TSCellularPlanIntroViewController _loadIcons]
+ -[TSCellularPlanIntroViewController _scanButtonTapped:]
+ -[TSCellularPlanIntroViewController _shouldShowTravelEducation]
+ -[TSCellularPlanIntroViewController _shouldShowTravelEducation].cold.1
+ -[TSCellularPlanIntroViewController initWithShowTransferOption:requireDelayBluetoothConnection:showQrCodeOption:transferIneligiblePlans:]
+ -[TSCellularPlanIntroViewController initWithShowTransferOption:requireDelayBluetoothConnection:showQrCodeOption:transferIneligiblePlans:].cold.1
+ -[TSCellularPlanIntroViewController isTravelEduButtonTapped]
+ -[TSCellularPlanIntroViewController needShowTransferIntroPane]
+ -[TSCellularPlanIntroViewController prepare:]
+ -[TSCellularPlanIntroViewController setIsTravelEduButtonTapped:]
+ -[TSCellularPlanIntroViewController setNeedShowTransferIntroPane:]
+ -[TSCellularPlanIntroViewController setShowCrossTransferOption:]
+ -[TSCellularPlanIntroViewController setShowQRCodeOption:]
+ -[TSCellularPlanIntroViewController setShowTransferOption:]
+ -[TSCellularPlanIntroViewController setShowTravelEduOption:]
+ -[TSCellularPlanIntroViewController setTransferIneligiblePlans:]
+ -[TSCellularPlanIntroViewController showCrossTransferOption]
+ -[TSCellularPlanIntroViewController showQRCodeOption]
+ -[TSCellularPlanIntroViewController showTransferOption]
+ -[TSCellularPlanIntroViewController showTravelEduOption]
+ -[TSCellularPlanIntroViewController transferIneligiblePlans]
+ -[TSCoreTelephonyClientCache getStoreVisitStatusForCarrier:]
+ -[TSCoreTelephonyClientCache getStoreVisitStatusForCarrier:].cold.1
+ -[TSCoreTelephonyClientCache getStoreVisitStatusForCarrier:].cold.2
+ -[TSCoreTelephonyClientCache loadSimSetupInfo:]
+ -[TSCoreTelephonyClientCache loadSimSetupInfo:].cold.1
+ -[TSCoreTelephonyClientCache loadSimSetupInfo:].cold.2
+ -[TSCoreTelephonyClientCache saveSimSetupInfo:info:]
+ -[TSCoreTelephonyClientCache saveSimSetupInfo:info:].cold.1
+ -[TSCoreTelephonyClientCache saveStoreVisitStatusForCarrier:visited:]
+ -[TSCrossPlatformTargetAuthFlow showQRCodePane:]
+ -[TSCrossPlatformTargetAuthFlow viewControllerDidComplete:]
+ -[TSMultiPlanIntermediateViewController hiddenInCloudFlowPlans]
+ -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:]
+ -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:].cold.1
+ -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:showQrCodeOption:transferIneligiblePlans:hiddenInCloudFlowPlans:]
+ -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:]
+ -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:]
+ -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:].cold.1
+ -[TSMultiPlanIntermediateViewController isScanButtonTapped]
+ -[TSMultiPlanIntermediateViewController plansWithScanOption]
+ -[TSMultiPlanIntermediateViewController setHiddenInCloudFlowPlans:]
+ -[TSMultiPlanIntermediateViewController setIsScanButtonTapped:]
+ -[TSMultiPlanIntermediateViewController setPlansWithScanOption:]
+ -[TSMultiPlanIntermediateViewController setSwUpdatePlans:]
+ -[TSMultiPlanIntermediateViewController swUpdatePlans]
+ -[TSPRXIdentityShareViewController _updateCurrentAction:]
+ -[TSPRXIdentityShareViewController primaryAction]
+ -[TSPRXIdentityShareViewController setPrimaryAction:]
+ -[TSQRCodeScanFlow initWithBackButton:plans:]
+ -[TSQRCodeScanFlow plans]
+ -[TSQRCodeScanFlow setPlans:]
+ -[TSTargetReconnectWaitingViewController connectionEstablished]
+ -[TSTransferCloudFlow _createIntroViewController:showQrCodeOption:]
+ -[TSTransferCloudFlow _maybePresentFirstViewController:firstViewControllerCallback:]
+ -[TSTransferCloudFlow _maybePresentFirstViewController:firstViewControllerCallback:].cold.1
+ -[TSTransferCloudFlowModel filterTransferPlans:].cold.3
+ -[TSTransferCloudFlowModel init]
+ -[TSTransferCloudFlowModel isD2dDone]
+ -[TSTransferCloudFlowModel loadSimSetupInfo]
+ -[TSTransferCloudFlowModel needOfferProximityTransferOption]
+ -[TSTransferCloudFlowModel needOfferQRCodeOption]
+ -[TSTransferCloudFlowModel requireStoreVisitItems]
+ -[TSTransferCloudFlowModel setIsD2dDone:]
+ -[TSTransferCloudFlowModel setNeedOfferProximityTransferOption:]
+ -[TSTransferCloudFlowModel setNeedOfferQRCodeOption:]
+ -[TSTransferCloudFlowModel setRequireStoreVisitItems:]
+ -[TSTransferCloudFlowModel setStoreVisitedMap:]
+ -[TSTransferCloudFlowModel setTransferIneligibleItems:]
+ -[TSTransferCloudFlowModel setTransferableHiddenInCloudFlowItems:]
+ -[TSTransferCloudFlowModel storeVisitedMap]
+ -[TSTransferCloudFlowModel transferIneligibleItems]
+ -[TSTransferCloudFlowModel transferableHiddenInCloudFlowItems]
+ -[TSTransferFlow _createIntroViewControllerWithIneligiblePlans:]
+ -[TSTransferFlow _maybePresentFirstViewController:firstViewControllerCallback:]
+ -[TSTransferFlow _maybePresentFirstViewController:firstViewControllerCallback:].cold.1
+ -[TSTransferFlow _saveSimsetupD2dInfo:]
+ -[TSTransferFlowModel init]
+ -[TSTransferFlowModel isProximityFlow]
+ -[TSTransferFlowModel needOfferQRCodeOption]
+ -[TSTransferFlowModel requireStoreVisitItems]
+ -[TSTransferFlowModel setIsProximityFlow:]
+ -[TSTransferFlowModel setNeedOfferQRCodeOption:]
+ -[TSTransferFlowModel setRequireStoreVisitItems:]
+ -[TSTransferFlowModel setSimsetupD2dInfo:]
+ -[TSTransferFlowModel setStoreVisitedMap:]
+ -[TSTransferFlowModel setTransferIneligibleItems:]
+ -[TSTransferFlowModel simsetupD2dInfo]
+ -[TSTransferFlowModel storeVisitedMap]
+ -[TSTransferFlowModel transferIneligibleItems]
+ -[TSTransferListViewController tableView:titleForFooterInSection:]
+ -[TSTransferListViewController tableView:willDisplayFooterView:forSection:]
+ -[TSTravelBuddyViewController _shouldDisplayPhoneNumber:]
+ -[TSTravelModeIntroViewController _skipButtonTapped:].cold.1
+ -[TSTravelModeIntroViewController init]
+ GCC_except_table23
+ GCC_except_table39
+ GCC_except_table47
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table80
+ GCC_except_table87
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table96
+ _OBJC_CLASS_$_CrossPlatformTargetQRCodeWarningViewController
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_SSQRCodeIntroViewController
+ _OBJC_CLASS_$_SSTransferIntroViewController
+ _OBJC_CLASS_$_SSVisitStoreViewController
+ _OBJC_IVAR_$_CrossPlatformTargetQRCodeWarningViewController._delegate
+ _OBJC_IVAR_$_SSQRCodeIntroViewController._delegate
+ _OBJC_IVAR_$_SSQRCodeIntroViewController._isScanButtonTapped
+ _OBJC_IVAR_$_SSTransferIntroViewController._delegate
+ _OBJC_IVAR_$_SSTransferIntroViewController._isTransferButtonTapped
+ _OBJC_IVAR_$_SSVisitStoreViewController._carrier
+ _OBJC_IVAR_$_SSVisitStoreViewController._continueButton
+ _OBJC_IVAR_$_SSVisitStoreViewController._delegate
+ _OBJC_IVAR_$_SSVisitStoreViewController._laterButton
+ _OBJC_IVAR_$_SSVisitStoreViewController._plan
+ _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._transferIneligibleViaCloudItems
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._bluetoothChecker
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._client
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._crossTransferIcon
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._isTravelEduButtonTapped
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._maxIconHeight
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._maxIconWidth
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._needShowTransferIntroPane
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._qrIcon
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._scanButton
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._showTravelEduOption
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._transferIcon
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._transferIneligiblePlans
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController._travelEduIcon
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._hiddenInCloudFlowPlans
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._isScanButtonTapped
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._laterButton
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._plansWithScanOption
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._showQrCodeOption
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._swUpdatePlans
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._primaryAction
+ _OBJC_IVAR_$_TSQRCodeScanFlow._plans
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._isD2dDone
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._needOfferProximityTransferOption
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._needOfferQRCodeOption
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._requireStoreVisitItems
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._storeVisitedMap
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._transferIneligibleItems
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._transferableHiddenInCloudFlowItems
+ _OBJC_IVAR_$_TSTransferFlowModel._needOfferQRCodeOption
+ _OBJC_IVAR_$_TSTransferFlowModel._requireStoreVisitItems
+ _OBJC_IVAR_$_TSTransferFlowModel._simsetupD2dInfo
+ _OBJC_IVAR_$_TSTransferFlowModel._storeVisitedMap
+ _OBJC_IVAR_$_TSTransferFlowModel._transferIneligibleItems
+ _OBJC_IVAR_$_TSTravelBuddyViewController._homeIccidCarrierName
+ _OBJC_IVAR_$_TSTravelBuddyViewController._secondHomeIccidCarrierName
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._showBackButton
+ _OBJC_METACLASS_$_CrossPlatformTargetQRCodeWarningViewController
+ _OBJC_METACLASS_$_SSQRCodeIntroViewController
+ _OBJC_METACLASS_$_SSTransferIntroViewController
+ _OBJC_METACLASS_$_SSVisitStoreViewController
+ _OUTLINED_FUNCTION_4
+ _TSSIMSetupInfoD2DDone
+ _TSSIMSetupInfoD2DInfo
+ _TSTravelActionPostArrivalLDMOff
+ _TSTravelActionPostArrivalLDMOn
+ _TSTravelActionPostArrivalUseTravelAndHomeSIM
+ _TSTravelActionPostArrivalUseTravelSIM
+ _TSTravelActionTappedNotNow
+ _TSTravelActionTappedNotNowReducedEducation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_SimSetup
+ __OBJC_$_CATEGORY_NSArray_$_SimSetup
+ __OBJC_$_CLASS_METHODS_SSQRCodeIntroViewController
+ __OBJC_$_CLASS_METHODS_SSTransferIntroViewController
+ __OBJC_$_CLASS_METHODS_TSCellularPlanIntroViewController
+ __OBJC_$_INSTANCE_METHODS_CrossPlatformTargetQRCodeWarningViewController
+ __OBJC_$_INSTANCE_METHODS_SSQRCodeIntroViewController
+ __OBJC_$_INSTANCE_METHODS_SSTransferIntroViewController
+ __OBJC_$_INSTANCE_METHODS_SSVisitStoreViewController
+ __OBJC_$_INSTANCE_VARIABLES_CrossPlatformTargetQRCodeWarningViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQRCodeIntroViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSTransferIntroViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSVisitStoreViewController
+ __OBJC_$_PROP_LIST_CrossPlatformTargetQRCodeWarningViewController
+ __OBJC_$_PROP_LIST_SSQRCodeIntroViewController
+ __OBJC_$_PROP_LIST_SSTransferIntroViewController
+ __OBJC_$_PROP_LIST_SSVisitStoreViewController
+ __OBJC_CLASS_PROTOCOLS_$_CrossPlatformTargetQRCodeWarningViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQRCodeIntroViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSTransferIntroViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSVisitStoreViewController
+ __OBJC_CLASS_RO_$_CrossPlatformTargetQRCodeWarningViewController
+ __OBJC_CLASS_RO_$_SSQRCodeIntroViewController
+ __OBJC_CLASS_RO_$_SSTransferIntroViewController
+ __OBJC_CLASS_RO_$_SSVisitStoreViewController
+ __OBJC_METACLASS_RO_$_CrossPlatformTargetQRCodeWarningViewController
+ __OBJC_METACLASS_RO_$_SSQRCodeIntroViewController
+ __OBJC_METACLASS_RO_$_SSTransferIntroViewController
+ __OBJC_METACLASS_RO_$_SSVisitStoreViewController
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke.51
+ ___39-[TSTransferFlow _firstViewController:]_block_invoke.217
+ ___44-[TSTransferFlowModel requestCarrierSetups:]_block_invoke.46
+ ___48-[TSCrossPlatformTargetAuthFlow showQRCodePane:]_block_invoke
+ ___48-[TSCrossPlatformTargetAuthFlow showQRCodePane:]_block_invoke.23
+ ___48-[TSCrossPlatformTargetAuthFlow showQRCodePane:]_block_invoke.23.cold.1
+ ___48-[TSCrossPlatformTargetAuthFlow showQRCodePane:]_block_invoke.23.cold.2
+ ___48-[TSCrossPlatformTargetAuthFlow showQRCodePane:]_block_invoke.cold.1
+ ___49-[TSTransferCloudFlowModel requestCarrierSetups:]_block_invoke.44
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.38
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.38.cold.1
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.38.cold.2
+ ___52-[TSCoreTelephonyClientCache saveSimSetupInfo:info:]_block_invoke
+ ___52-[TSCoreTelephonyClientCache saveSimSetupInfo:info:]_block_invoke.cold.1
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.211
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.213
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.212
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.35
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.35.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.36
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.36.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.37
+ ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.41
+ ___57-[NSArray(SimSetup) filteredPlansWithTransferCapability:]_block_invoke
+ ___59-[NSArray(SimSetup) filteredPlansWithTransferCapabilities:]_block_invoke
+ ___59-[TSCrossPlatformTargetAuthFlow viewControllerDidComplete:]_block_invoke
+ ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.165
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.100
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.100.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.101
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.101.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.102
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.102.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.103
+ ___69-[TSCoreTelephonyClientCache saveStoreVisitStatusForCarrier:visited:]_block_invoke
+ ___69-[TSCoreTelephonyClientCache saveStoreVisitStatusForCarrier:visited:]_block_invoke.cold.1
+ ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.111
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.105
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.105.cold.1
+ ___79-[TSTransferFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke
+ ___79-[TSTransferFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke.cold.1
+ ___84-[TSTransferCloudFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke
+ ___84-[TSTransferCloudFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke.cold.1
+ ___97-[TSActivationFlowWithSimSetupFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke
+ ___97-[TSActivationFlowWithSimSetupFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke.cold.1
+ ___block_descriptor_40_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_40_e8_32s_e25_B24?08"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e43_v16?0"UIViewController<TSSetupFlowItem>"8lw48l8s40l8s32l8
+ ___block_literal_global.215
+ ___block_literal_global.297
+ ___block_literal_global.313
+ ___block_literal_global.52
+ ___block_literal_global.54
+ ___block_literal_global.57
+ ___block_literal_global.672
+ ___block_literal_global.702
+ ___block_literal_global.762
+ _objc_msgSend$FormattedCarrierListFromSet:
+ _objc_msgSend$_createIntroViewController:showQrCodeOption:
+ _objc_msgSend$_createIntroViewControllerWithIneligiblePlans:
+ _objc_msgSend$_isAnyRequireStoreVisitPlan:
+ _objc_msgSend$_isAnySourceNeedsSoftwareUpdatePlan:
+ _objc_msgSend$_isStandaloneQRCodeView
+ _objc_msgSend$_loadIcons
+ _objc_msgSend$_maybePresentFirstViewController:firstViewControllerCallback:
+ _objc_msgSend$_saveSimsetupD2dInfo:
+ _objc_msgSend$_shouldDisplayPhoneNumber:
+ _objc_msgSend$_shouldShowTravelEducation
+ _objc_msgSend$_updateCurrentAction:
+ _objc_msgSend$allPlansRequireSoftwareUpdate:
+ _objc_msgSend$connectionEstablished
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$filteredPlansRequiresScanOption
+ _objc_msgSend$filteredPlansWithTransferCapabilities:
+ _objc_msgSend$getDetail:
+ _objc_msgSend$getDetails:
+ _objc_msgSend$getDetailsWithTransferOption:showQRCodeOption:showCrossTransferOption:transferIneligiblePlans:
+ _objc_msgSend$getStoreVisitStatusForCarrier:
+ _objc_msgSend$getStoreVisitStatusForPlan:cache:
+ _objc_msgSend$hasCode
+ _objc_msgSend$initWithBackButton:plans:
+ _objc_msgSend$initWithItems:
+ _objc_msgSend$initWithShowTransferOption:requireDelayBluetoothConnection:showQrCodeOption:transferIneligiblePlans:
+ _objc_msgSend$initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:
+ _objc_msgSend$initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:
+ _objc_msgSend$initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:
+ _objc_msgSend$isD2dDone
+ _objc_msgSend$isPlanHiddenRequiredForCloudFlow
+ _objc_msgSend$isProximityFlow
+ _objc_msgSend$isTransferButtonTapped
+ _objc_msgSend$isTravelEduButtonTapped
+ _objc_msgSend$loadCarrierStoreVisitStatusForCarrier:error:
+ _objc_msgSend$loadSimSetupInfo
+ _objc_msgSend$loadSimSetupInfo:
+ _objc_msgSend$loadSimSetupInfo:error:
+ _objc_msgSend$needHideForCloudFlow
+ _objc_msgSend$needOfferProximityTransferOption
+ _objc_msgSend$needOfferQRCodeOption
+ _objc_msgSend$needShowTransferIntroPane
+ _objc_msgSend$needVisitStoreForTransfer
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$replaceAction:withNewAction:
+ _objc_msgSend$requireStoreVisitItems
+ _objc_msgSend$requireVisitStoreOnce
+ _objc_msgSend$saveCarrierStoreVisitStatus:visited:completion:
+ _objc_msgSend$saveSimSetupInfo:info:
+ _objc_msgSend$saveSimSetupInfo:info:completion:
+ _objc_msgSend$saveStoreVisitStatusForCarrier:visited:
+ _objc_msgSend$setNeedOfferProximityTransferOption:
+ _objc_msgSend$setNeedOfferQRCodeOption:
+ _objc_msgSend$shouldShowTravelEducation:
+ _objc_msgSend$showQRCodePane:
+ _objc_msgSend$simsetupD2dInfo
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$transferIneligibleItems
+ _objc_msgSend$transferIneligibleViaCloudItems
+ _objc_msgSend$transferableHiddenInCloudFlowItems
- -[TSCellularPlanIntroViewController _hideQRCodeOption]
- -[TSCellularPlanIntroViewController initWithShowTransferOption:requireDelayBluetoothConnection:]
- -[TSCrossPlatformTargetAuthFlow init]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:].cold.1
- -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:].cold.1
- -[TSQRCodeScanFlow initWithBackButton:]
- -[TSTargetReconnectWaitingViewController connectionStarted]
- -[TSTransferCloudFlow _createIntroViewController:]
- -[TSTransferFlow _createIntroViewController]
- -[TSTransferListViewController heightAnchor]
- -[TSTransferListViewController setHeightAnchor:]
- -[TSTransferListViewController tableView:heightForFooterInSection:]
- -[TSTransferListViewController tableView:viewForFooterInSection:]
- -[TSTransferListViewController updateFooterView]
- -[TSTravelModeIntroViewController _learnMoreButtonTapped]
- -[TSTravelModeIntroViewController _setUpLearnMoreLink]
- GCC_except_table26
- GCC_except_table31
- GCC_except_table36
- GCC_except_table38
- GCC_except_table42
- GCC_except_table48
- GCC_except_table67
- GCC_except_table74
- GCC_except_table79
- GCC_except_table81
- GCC_except_table82
- _OBJC_IVAR_$_TSCellularPlanIntroViewController.bluetoothChecker
- _OBJC_IVAR_$_TSCellularPlanIntroViewController.viewController
- _OBJC_IVAR_$_TSCrossPlatformTargetAuthFlow._dctCode
- _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._inBuddy
- _OBJC_IVAR_$_TSTransferListViewController._heightAnchor
- _OBJC_IVAR_$_TSTravelModeIntroViewController._dataSubscriptionContext
- _TSTravelActionPostArrivalBuddyLDMOff
- _TSTravelActionPostArrivalBuddyLDMOn
- _TSTravelActionPostArrivalBuddyUseTravelAndHomeSIM
- _TSTravelActionPostArrivalBuddyUseTravelSIM
- _TSTravelActionPostArrivalInstallLDMOff
- _TSTravelActionPostArrivalInstallLDMOn
- _TSTravelActionPostArrivalInstallUseTravelAndHomeSIM
- _TSTravelActionPostArrivalInstallUseTravelSIM
- _TSTravelActionTravelIntroRoamingOff
- _TSTravelActionTravelIntroRoamingOn
- ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke.50
- ___39-[TSTransferFlow _firstViewController:]_block_invoke.184
- ___44-[TSTransferFlowModel requestCarrierSetups:]_block_invoke.45
- ___49-[TSTransferCloudFlowModel requestCarrierSetups:]_block_invoke.40
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.35
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.35.cold.1
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.35.cold.2
- ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke
- ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.22
- ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.22.cold.1
- ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.22.cold.2
- ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.cold.1
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.215
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.217
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.216
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.31
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.31.cold.1
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.32
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.32.cold.1
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.33
- ___56-[TSTransferFlow _maybeClearFirstViewControllerCallback]_block_invoke
- ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.166
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.96
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.96.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.97
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.97.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.98
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.98.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.99
- ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.107
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.101
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.101.cold.1
- ___block_descriptor_40_e8_32w_e26_v16?0"UIViewController"8lw32l8
- ___block_descriptor_64_e8_32s40bs48r56w_e30_v24?0"NSString"8"NSError"16lw56l8s40l8r48l8s32l8
- ___block_literal_global.219
- ___block_literal_global.294
- ___block_literal_global.310
- ___block_literal_global.44
- ___block_literal_global.49
- ___block_literal_global.678
- ___block_literal_global.708
- ___block_literal_global.768
- _objc_msgSend$_createIntroViewController
- _objc_msgSend$_createIntroViewController:
- _objc_msgSend$_hideQRCodeOption
- _objc_msgSend$connectionStarted
- _objc_msgSend$getCurrentDataSubscriptionContextSync:
- _objc_msgSend$initWithShowTransferOption:requireDelayBluetoothConnection:
- _objc_msgSend$initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:
- _objc_msgSend$initWithTransferItems:showOtherOptions:isShowingFilteredPlans:
- _objc_msgSend$removeAction:
CStrings:
+ "\tR"
+ "%@ %@ %@"
+ "%@%@%@ %@"
+ "+"
+ "+[TSUtilities getStoreVisitStatusForPlan:cache:]"
+ "-[TSActivationFlowWithSimSetupFlow _maybePresentFirstViewController:firstViewControllerCallback:]"
+ "-[TSActivationFlowWithSimSetupFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke"
+ "-[TSCellularPlanIntroViewController _isStandaloneQRCodeView]"
+ "-[TSCellularPlanIntroViewController _shouldShowTravelEducation]"
+ "-[TSCellularPlanIntroViewController initWithShowTransferOption:requireDelayBluetoothConnection:showQrCodeOption:transferIneligiblePlans:]"
+ "-[TSCoreTelephonyClientCache getStoreVisitStatusForCarrier:]"
+ "-[TSCoreTelephonyClientCache loadSimSetupInfo:]"
+ "-[TSCoreTelephonyClientCache saveSimSetupInfo:info:]"
+ "-[TSCoreTelephonyClientCache saveSimSetupInfo:info:]_block_invoke"
+ "-[TSCoreTelephonyClientCache saveStoreVisitStatusForCarrier:visited:]_block_invoke"
+ "-[TSCrossPlatformTargetAuthFlow showQRCodePane:]_block_invoke"
+ "-[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:]"
+ "-[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:]"
+ "-[TSTransferCloudFlow _maybePresentFirstViewController:firstViewControllerCallback:]"
+ "-[TSTransferCloudFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke"
+ "-[TSTransferFlow _maybePresentFirstViewController:firstViewControllerCallback:]"
+ "-[TSTransferFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke"
+ "-[TSTravelModeIntroViewController _skipButtonTapped:]"
+ "7"
+ "@\"UIImage\""
+ "@36@0:8B16B20B24@28"
+ "@56@0:8@16B24B28@32@40@48"
+ "@64@0:8@16@24@32B40B44@48@56"
+ "B24@?0@8@\"NSDictionary\"16"
+ "CARRIER"
+ "CELLULAR_PLAN_INTRO_QRCODE_%@"
+ "CELLULAR_PLAN_INTRO_QRCODE_NO_CARRIER"
+ "CELLULAR_PLAN_TRANSFER_INTRO_DETAIL"
+ "CELLULAR_PLAN_TRANSFER_INTRO_DETAIL_%@"
+ "CONTINUE_WITHOUT_CELLULAR"
+ "CROSSPLATFORM_TARGET_QRCODE_WARNING_DETAIL"
+ "CROSSPLATFORM_TARGET_QRCODE_WARNING_TITLE"
+ "CrossPlatformTargetQRCodeWarningViewController"
+ "FormattedCarrierListFromSet:"
+ "INTERMEDIATE_TRANSFER_PLAN_ITEM_SUBTITLE"
+ "INTERMEDIATE_TRANSFER_PLAN_ITEM_SUBTITLE_@"
+ "LEARN_MORE_NO_ELLIPSIS"
+ "MULTI_ESIM_TRANSFER_FILTERED_QR_CODE_DETAIL"
+ "MULTI_ESIM_TRANSFER_QR_CODE_DETAIL"
+ "Not Show"
+ "OR"
+ "SCAN_QR_CODE"
+ "SCAN_QR_CODE_SUBTEXT"
+ "SCAN_QR_CODE_SUBTEXT_@"
+ "SET_UP_LATER"
+ "SSQRCodeIntroViewController"
+ "SSTransferIntroViewController"
+ "SSVisitStoreViewController"
+ "Show"
+ "Show travel education result: %@ @%s"
+ "StandaloneQRCodeView: YES @%s"
+ "T@\"NSArray\",&,V_hiddenInCloudFlowPlans"
+ "T@\"NSArray\",&,V_plansWithScanOption"
+ "T@\"NSArray\",&,V_swUpdatePlans"
+ "T@\"NSArray\",&,V_transferIneligiblePlans"
+ "T@\"NSMutableArray\",&,N,V_requireStoreVisitItems"
+ "T@\"NSMutableArray\",&,N,V_transferIneligibleItems"
+ "T@\"NSMutableArray\",&,N,V_transferableHiddenInCloudFlowItems"
+ "T@\"NSMutableArray\",&,V_transferIneligibleViaCloudItems"
+ "T@\"NSMutableArray\",&,V_transferItems"
+ "T@\"NSMutableDictionary\",&,V_simsetupD2dInfo"
+ "T@\"NSMutableDictionary\",&,V_storeVisitedMap"
+ "T@\"PRXAction\",&,V_primaryAction"
+ "TB,N,V_isD2dDone"
+ "TB,N,V_isProximityFlow"
+ "TB,N,V_needOfferProximityTransferOption"
+ "TB,N,V_needOfferQRCodeOption"
+ "TB,V_isTransferButtonTapped"
+ "TB,V_isTravelEduButtonTapped"
+ "TB,V_needShowTransferIntroPane"
+ "TB,V_showCrossTransferOption"
+ "TB,V_showQRCodeOption"
+ "TB,V_showTransferOption"
+ "TB,V_showTravelEduOption"
+ "TRAVEL_EDUCATION_BUTTON"
+ "TRAVEL_MODE_EDU_FROM_ADD_ESIM_BODY"
+ "VERIFICATION_COMPLETE"
+ "VISIT_STORE_DETAIL_%@"
+ "VISIT_STORE_TITLE"
+ "Your carrier"
+ "[Db] incompatible CT @%s"
+ "[Db] ineligible plan: %@, offer qrcode @%s"
+ "[Db] transferable plan cannot proceed via cloud flow @%s"
+ "[Db] visit store plan : %@ @%s"
+ "[E]Error checking: %@ @%s"
+ "[E]invalid carrier for plan : %@ @%s"
+ "[E]load simsetup info failed. key: %@, error:%@ @%s"
+ "[E]load visit store failed : %@ @%s"
+ "[E]nothing to present @%s"
+ "[E]save simsetup info failed. key:%@, error: %@ @%s"
+ "[E]save store visited status (%{bool}d) for %@ failed - %@ @%s"
+ "[F]no option need to show @%s"
+ "_bluetoothChecker"
+ "_carrier"
+ "_createIntroViewController:showQrCodeOption:"
+ "_createIntroViewControllerWithIneligiblePlans:"
+ "_crossTransferIcon"
+ "_hiddenInCloudFlowPlans"
+ "_homeIccidCarrierName"
+ "_isAnyRequireStoreVisitPlan:"
+ "_isAnySourceNeedsSoftwareUpdatePlan:"
+ "_isD2dDone"
+ "_isStandaloneQRCodeView"
+ "_isTransferButtonTapped"
+ "_isTravelEduButtonTapped"
+ "_loadIcons"
+ "_maxIconHeight"
+ "_maxIconWidth"
+ "_maybePresentFirstViewController:firstViewControllerCallback:"
+ "_needOfferProximityTransferOption"
+ "_needOfferQRCodeOption"
+ "_needShowTransferIntroPane"
+ "_plansWithScanOption"
+ "_primaryAction"
+ "_qrIcon"
+ "_requireStoreVisitItems"
+ "_saveSimsetupD2dInfo:"
+ "_scanButton"
+ "_scanButtonTapped:"
+ "_secondHomeIccidCarrierName"
+ "_setupLaterButtonTapped"
+ "_shouldDisplayPhoneNumber:"
+ "_shouldShowTravelEducation"
+ "_showBackButton"
+ "_showQrCodeOption"
+ "_showTravelEduOption"
+ "_simsetupD2dInfo"
+ "_storeVisitedMap"
+ "_swUpdatePlans"
+ "_transferButtonTapped:"
+ "_transferIcon"
+ "_transferIneligibleItems"
+ "_transferIneligiblePlans"
+ "_transferIneligibleViaCloudItems"
+ "_transferableHiddenInCloudFlowItems"
+ "_travelEduIcon"
+ "_updateCurrentAction:"
+ "airplane"
+ "allPlansRequireSoftwareUpdate:"
+ "connectionEstablished"
+ "cur : %@(%p), next: %@(%p) @%s"
+ "d2dDone"
+ "filteredArrayUsingPredicate:"
+ "filteredPlansRequiresScanOption"
+ "filteredPlansWithTransferCapabilities:"
+ "filteredPlansWithTransferCapability:"
+ "getDetail:"
+ "getDetails:"
+ "getDetailsWithTransferOption:showQRCodeOption:showCrossTransferOption:transferIneligiblePlans:"
+ "getStoreVisitStatusForCarrier:"
+ "getStoreVisitStatusForPlan:cache:"
+ "hasCode"
+ "hiddenInCloudFlowPlans"
+ "https://support.apple.com/123878"
+ "initWithBackButton:plans:"
+ "initWithItems:"
+ "initWithShowTransferOption:requireDelayBluetoothConnection:showQrCodeOption:transferIneligiblePlans:"
+ "initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:transferIneligiblePlans:hiddenInCloudFlowPlans:"
+ "initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:showQrCodeOption:transferIneligiblePlans:hiddenInCloudFlowPlans:"
+ "initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:"
+ "initWithTransferItems:showOtherOptions:isShowingFilteredPlans:transferIneligiblePlans:hiddenInCloudFlowPlans:swUpdatePlans:"
+ "isD2dDone"
+ "isPlanHiddenRequiredForCloudFlow"
+ "isProximityFlow"
+ "isTransferButtonTapped"
+ "isTravelEduButtonTapped"
+ "loadCarrierStoreVisitStatusForCarrier:error:"
+ "loadSimSetupInfo"
+ "loadSimSetupInfo:"
+ "loadSimSetupInfo:error:"
+ "localizedCaseInsensitiveCompare:"
+ "needHideForCloudFlow"
+ "needOfferProximityTransferOption"
+ "needOfferQRCodeOption"
+ "needShowTransferIntroPane"
+ "needVisitStoreForTransfer"
+ "next vc mismatch. expect:%@(%p), real:%@(%p) @%s"
+ "plansWithScanOption"
+ "postarrival_ldm_off"
+ "postarrival_ldm_on"
+ "postarrival_use_travel"
+ "postarrival_use_travel_and_home"
+ "predicateWithBlock:"
+ "present first view : %@(%p) @%s"
+ "primaryAction"
+ "push %@(%p) onto %@(%p) @%s"
+ "replaceAction:withNewAction:"
+ "requireStoreVisitItems"
+ "requireVisitStoreOnce"
+ "saveCarrierStoreVisitStatus:visited:completion:"
+ "saveSimSetupInfo:info:"
+ "saveSimSetupInfo:info:completion:"
+ "saveStoreVisitStatusForCarrier:visited:"
+ "saving simsetup info. key: %@, info: %@ @%s"
+ "setHiddenInCloudFlowPlans:"
+ "setIsD2dDone:"
+ "setIsProximityFlow:"
+ "setIsTransferButtonTapped:"
+ "setIsTravelEduButtonTapped:"
+ "setNeedOfferProximityTransferOption:"
+ "setNeedOfferQRCodeOption:"
+ "setNeedShowTransferIntroPane:"
+ "setPlansWithScanOption:"
+ "setPrimaryAction:"
+ "setRequireStoreVisitItems:"
+ "setShowCrossTransferOption:"
+ "setShowQRCodeOption:"
+ "setShowTransferOption:"
+ "setShowTravelEduOption:"
+ "setSimsetupD2dInfo:"
+ "setStoreVisitedMap:"
+ "setSwUpdatePlans:"
+ "setTransferIneligibleItems:"
+ "setTransferIneligiblePlans:"
+ "setTransferIneligibleViaCloudItems:"
+ "setTransferableHiddenInCloudFlowItems:"
+ "shouldShowTravelEducation:"
+ "showQRCodePane:"
+ "showTravelEduOption"
+ "showTravelEducationOption"
+ "simsetup info key: %@, value: %@ @%s"
+ "simsetupD2dInfo"
+ "storeVisitedMap"
+ "subarrayWithRange:"
+ "swUpdatePlans"
+ "tapped_not_now"
+ "tapped_not_now_reduced_education"
+ "transfer plans: %lu, store visit:%lu, hidden: %lu, ineligible: %lu @%s"
+ "transfer plans: %lu, store visit:%lu, ineligible: %lu @%s"
+ "transferIneligibleItems"
+ "transferIneligiblePlans"
+ "transferIneligibleViaCloudItems"
+ "transferableHiddenInCloudFlowItems"
+ "user explicitly mentioned he/she has not visited store, plan (%@) is not able to transfer for now. @%s"
+ "user explicitly notify having not visited store, plan (%@) is not able to transfer for now. @%s"
+ "\xd1"
+ "\xf01"
- "'"
- "-[TSActivationFlowWithSimSetupFlow _createFirstViewController:]"
- "-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke"
- "-[TSMultiPlanIntermediateViewController initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:]"
- "-[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:]"
- "-[TSTransferCloudFlow _createIntroViewController:]"
- "-[TSTransferFlow _createIntroViewController]"
- "-[TSTransferFlow _maybeClearFirstViewControllerCallback]_block_invoke"
- "6"
- "@48@0:8@16@24@32B40B44"
- "IPAD_MULTI_TRANSFER_SUBTEXT_%lu"
- "MULTI_TRANSFER_SUBTEXT_%lu"
- "Received kCrossTransferDCTCode, but firstViewControllerCallback is not set @%s"
- "SET_UP_LATER_IN_SETTINGS_SUB"
- "SIMSetupSupport/MagnoliaOverProximity or iPadESIMProvisioningParity is %s @%s"
- "TRANSFER_PLAN_ITEM_TITLE_NO_CARRIER_NAME"
- "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DATAONLY_%@"
- "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DATAONLY_DUALSIM_%@_%@"
- "TRAVEL_MODE_REDUCED_EDU_PRE_DEPARTURE_BODY_ABROAD"
- "_createIntroViewController"
- "_createIntroViewController:"
- "_dataSubscriptionContext"
- "_dctCode"
- "_hideQRCodeOption"
- "a"
- "bluetoothChecker"
- "connectionStarted"
- "cur : %@, next: %@ @%s"
- "disabled"
- "enabled"
- "getCurrentDataSubscriptionContextSync:"
- "https://support.apple.com/119606"
- "initWithShowTransferOption:requireDelayBluetoothConnection:"
- "initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:"
- "initWithTransferItems:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:"
- "initWithTransferItems:showOtherOptions:isShowingFilteredPlans:"
- "kCrossTransferDCTCode code is nil or code is empty, end flow @%s"
- "next vc mismatch. expect:%@, real:%@ @%s"
- "postarrival_buddy_ldm_off"
- "postarrival_buddy_ldm_on"
- "postarrival_buddy_use_travel"
- "postarrival_buddy_use_travel_and_home"
- "postarrival_install_ldm_off"
- "postarrival_install_ldm_on"
- "postarrival_install_use_travel"
- "postarrival_install_use_travel_and_home"
- "present first view : %@ @%s"
- "push %@ onto %@ @%s"
- "removeAction:"
- "transfer option is %s @%s"
- "travel_intro_roaming_off"
- "travel_intro_roaming_on"
- "view controller : %@ @%s"

```
