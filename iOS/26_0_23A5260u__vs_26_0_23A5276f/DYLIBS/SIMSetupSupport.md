## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-849.1.0.0.0
-  __TEXT.__text: 0xa8970
-  __TEXT.__auth_stubs: 0x820
+855.0.0.0.0
+  __TEXT.__text: 0xa9664
+  __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0x9704
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x1c14
-  __TEXT.__cstring: 0xec28
-  __TEXT.__oslogstring: 0x5fa7
+  __TEXT.__gcc_except_tab: 0x1b98
+  __TEXT.__cstring: 0xee66
+  __TEXT.__oslogstring: 0x619c
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x23a8
-  __TEXT.__objc_classname: 0x14bb
-  __TEXT.__objc_methname: 0x14c98
-  __TEXT.__objc_methtype: 0x32cf
-  __TEXT.__objc_stubs: 0xd500
-  __DATA_CONST.__got: 0xa20
-  __DATA_CONST.__const: 0x1c70
-  __DATA_CONST.__objc_classlist: 0x458
+  __TEXT.__unwind_info: 0x23e0
+  __TEXT.__objc_classname: 0x14c1
+  __TEXT.__objc_methname: 0x14fdd
+  __TEXT.__objc_methtype: 0x3324
+  __TEXT.__objc_stubs: 0xd880
+  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__const: 0x1ca8
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c30
+  __DATA_CONST.__objc_selrefs: 0x4d10
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x408
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x420
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0x6ba0
-  __AUTH_CONST.__objc_const: 0x3b3a8
+  __DATA_CONST.__objc_superrefs: 0x400
+  __DATA_CONST.__objc_arraydata: 0x38
+  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0x6d40
+  __AUTH_CONST.__objc_const: 0x3ac60
   __AUTH_CONST.__objc_intobj: 0x4e0
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x2b20
-  __DATA.__objc_ivar: 0xdcc
+  __AUTH.__objc_data: 0x2ad0
+  __DATA.__objc_ivar: 0xdc8
   __DATA.__data: 0xb50
   __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE2571EF-97C0-33BC-8068-B3AED64D81D9
-  Functions: 3648
-  Symbols:   13319
-  CStrings:  6911
+  UUID: 4DBA40ED-7E88-358D-991D-B8959BF134FA
+  Functions: 3661
+  Symbols:   13356
+  CStrings:  6988
 
Symbols:
+ +[TSUtilities isSolariumEnabled]
+ +[TSUtilities numActivePlansOnDeviceExcept:]
+ -[CrossPlatformManualDetailsViewController textField:shouldChangeCharactersInRange:replacementString:]
+ -[CrossPlatformTransferIntroViewController _LearnMoreButtonTapped]
+ -[SSCardManualEntryViewController findFirstResponderInView:]
+ -[SSScanViewController startScanning]
+ -[TSCellularPlanActivatingFlow selectedItems]
+ -[TSCellularPlanActivatingFlow setSelectedItems:]
+ -[TSCellularPlanQRCodeScannerView setupCameraSession].cold.5
+ -[TSCellularPlanUsesViewController _maybeEnableDoneButton]
+ -[TSCellularPlanUsesViewController doneButton]
+ -[TSCellularPlanUsesViewController setDoneButton:]
+ -[TSCellularPlanUsesViewController viewWillAppear:]
+ -[TSCellularSetupCompleteViewController _isPlanSelected:selectedItems:]
+ -[TSCellularSetupCompleteViewController detailText]
+ -[TSCellularSetupCompleteViewController initWithPlans:selectedItems:skip:isForCrossPlatformTransfer:]
+ -[TSCellularSetupCompleteViewController setDetailText:]
+ -[TSCellularSetupLoadingView initWithCarrierName:]
+ -[TSDeviceInfoViewController extractPhoneInfoFromOptions:]
+ -[TSDeviceInfoViewController getPhoneInfoFromCT]
+ -[TSDeviceInfoViewController getPhoneInfoFromCT].cold.1
+ -[TSDeviceInfoViewController getPhoneInfoFromCT].cold.2
+ -[TSDeviceInfoViewController getPhoneInfoFromCT].cold.3
+ -[TSDeviceInfoViewController initWithOptions:].cold.1
+ -[TSDeviceInfoViewController tableView:cellForRowAtIndexPath:].cold.2
+ -[TSEnableTableViewController(UITableViewDataSource) scrollViewDidEndDecelerating:]
+ -[TSIdentityShareFlow appBackgrounded]
+ -[TSIdentityShareFlow appBackgrounded].cold.1
+ -[TSNoPlanForTransferViewController(UITableViewDataSource) tableView:titleForFooterInSection:]
+ -[TSNoPlanForTransferViewController(UITableViewDataSource) tableView:willDisplayFooterView:forSection:]
+ -[TSPRXIdentityShareViewController _registerLockState]
+ -[TSPRXIdentityShareViewController _registerLockState].cold.1
+ -[TSPRXIdentityShareViewController dealloc].cold.1
+ -[TSPRXIdentityShareViewController viewWillDisappear:]
+ -[TSPRXIdentityShareViewController viewWillDisappear:].cold.1
+ -[TSProximitySourceTransferFlow initForResumptionWithSelectedTransferPlans:targetUICapability:isPreSharedKeyPresent:]
+ -[TSSIMSetupFlow restartWith:].cold.2
+ -[TSSIMSetupFlow restartWith:].cold.3
+ -[TSWebsheetViewController initForRemotePlan:carrierName:skipUIDismissal:showCarrierWarning:]
+ -[TSWebsheetViewController initWithURL:postdata:carrierName:]
+ -[UIView(BuddyPinAutoLayout) pinToEdges:]
+ -[UIView(BuddyPinAutoLayout) pinToHorizontalEdges:]
+ -[UIView(BuddyPinAutoLayout) pinToVerticalEdges:]
+ -[UIViewController(NavigationBar) setNavigationBarColor]
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table131
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table151
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table198
+ GCC_except_table224
+ GCC_except_table46
+ _OBJC_CLASS_$_OBTrayButton
+ _OBJC_CLASS_$_UIBackgroundConfiguration
+ _OBJC_IVAR_$_CrossPlatformTransferIntroViewController._LearnMoreButton
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._selectedItems
+ _OBJC_IVAR_$_TSCellularSetupCompleteViewController._detailText
+ _OBJC_IVAR_$_TSCellularSetupLoadingView._carrierName
+ _OBJC_IVAR_$_TSTravelBuddyViewController._isSubTextSelected
+ _TSUserInfoIsPreSharedKeyPresentKey
+ _TSUserInfoSupportsSyncTransferResultsKey
+ _TSUserInfokSelectedTransferPlansCountKey
+ _UIEdgeInsetsZero
+ __OBJC_$_CATEGORY_UIView_$_BuddyPinAutoLayout
+ __OBJC_$_INSTANCE_METHODS_UIView(BuddyPinAutoLayout|UIKitExtras)
+ __OBJC_$_INSTANCE_METHODS_UIViewController(Flow|InModalPresentation|SubFlow|NavigationBar)
+ __UISolariumEnabled
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.492
+ ___39-[SSScanViewController decodeMetadata:]_block_invoke.49
+ ___51-[TSProximitySourceTransferFlow _bootstrapTransfer]_block_invoke.151
+ ___54-[TSPRXIdentityShareViewController _registerLockState]_block_invoke
+ ___54-[TSPRXIdentityShareViewController _registerLockState]_block_invoke.cold.1
+ ___63-[TSTravelBuddyViewController tableView:cellForRowAtIndexPath:]_block_invoke
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.96
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.96.cold.1
+ ___70-[TSCellularSetupLoadingViewController safariViewControllerDidFinish:]_block_invoke.91
+ ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.107
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.538
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.101
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.101.cold.1
+ ___79-[TSCellularSetupLoadingViewController setupCoreTelephonyClientForRemoteSignup]_block_invoke.58
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.601
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.550
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.550.cold.1
+ ___83-[TSEnableTableViewController(UITableViewDataSource) scrollViewDidEndDecelerating:]_block_invoke
+ ___block_descriptor_32_e26_"UIColor"16?0"UIColor"8l
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8w56l8s40l8s48l8
+ ___block_literal_global.104
+ ___block_literal_global.119
+ ___block_literal_global.122
+ ___block_literal_global.401
+ ___block_literal_global.491
+ ___block_literal_global.494
+ ___block_literal_global.552
+ ___block_literal_global.660
+ ___block_literal_global.690
+ ___block_literal_global.750
+ _objc_msgSend$CSN
+ _objc_msgSend$IMEI
+ _objc_msgSend$_isPlanSelected:selectedItems:
+ _objc_msgSend$_maybeEnableDoneButton
+ _objc_msgSend$allButtons
+ _objc_msgSend$buttonWithType:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:multiplier:constant:
+ _objc_msgSend$convertRect:fromView:
+ _objc_msgSend$extractPhoneInfoFromOptions:
+ _objc_msgSend$findFirstResponderInView:
+ _objc_msgSend$getMobileEquipmentInfo:
+ _objc_msgSend$getPhoneInfoFromCT
+ _objc_msgSend$host
+ _objc_msgSend$imageBySamplingNearest
+ _objc_msgSend$initForRemotePlan:carrierName:skipUIDismissal:showCarrierWarning:
+ _objc_msgSend$initForResumptionWithSelectedTransferPlans:targetUICapability:isPreSharedKeyPresent:
+ _objc_msgSend$initWithCarrierName:
+ _objc_msgSend$initWithPlans:selectedItems:skip:isForCrossPlatformTransfer:
+ _objc_msgSend$initWithURL:postdata:carrierName:
+ _objc_msgSend$installingPlanInfos
+ _objc_msgSend$isSolariumEnabled
+ _objc_msgSend$listCellConfiguration
+ _objc_msgSend$meInfoList
+ _objc_msgSend$numActivePlansOnDeviceExcept:
+ _objc_msgSend$pinToEdges:
+ _objc_msgSend$pinToHorizontalEdges:
+ _objc_msgSend$pinToVerticalEdges:
+ _objc_msgSend$scrollRectToVisible:animated:
+ _objc_msgSend$setBackgroundColorTransformer:
+ _objc_msgSend$setBackgroundConfiguration:
+ _objc_msgSend$setClient:
+ _objc_msgSend$setContentInset:
+ _objc_msgSend$setEnablesReturnKeyAutomatically:
+ _objc_msgSend$setMinimumFontSize:
+ _objc_msgSend$setNavigationBarColor
+ _objc_msgSend$setScrollIndicatorInsets:
+ _objc_msgSend$setShouldAdjustScrollViewInsetForKeyboard:
+ _objc_msgSend$subviews
+ _objc_msgSend$supportsAVCaptureSessionPreset:
+ _objc_msgSend$target
+ _objc_msgSend$whiteColor
- +[TSIdentityShareViewController _isSecureForRemoteViewService]
- +[TSUtilities numActivePlansOnDevice]
- -[SSScanViewController _startScanning]
- -[TSCellularSetupCompleteViewController initWithPlans:skip:isForCrossPlatformTransfer:]
- -[TSCellularSetupLoadingViewController viewWillAppear:]
- -[TSIdentityShareFlow init]
- -[TSIdentityShareFlow isDeviceInfo]
- -[TSIdentityShareFlow setIsDeviceInfo:]
- -[TSIdentityShareViewController .cxx_destruct]
- -[TSIdentityShareViewController _canShowWhileLocked]
- -[TSIdentityShareViewController _doneButtonTapped]
- -[TSIdentityShareViewController _userDidTapCancel]
- -[TSIdentityShareViewController delegate]
- -[TSIdentityShareViewController details]
- -[TSIdentityShareViewController detailtitle]
- -[TSIdentityShareViewController init]
- -[TSIdentityShareViewController setDelegate:]
- -[TSIdentityShareViewController setDetails:]
- -[TSIdentityShareViewController setDetailtitle:]
- -[TSIdentityShareViewController viewDidLoad]
- -[TSNoPlanForTransferViewController(UITableViewDataSource) tableView:viewForFooterInSection:]
- -[TSPRXIdentityShareViewController _startSystemMonitor]
- -[TSPRXIdentityShareViewController _stopSystemMonitor]
- -[TSPRXIdentityShareViewController setSystemMonitor:]
- -[TSPRXIdentityShareViewController systemMonitor]
- -[TSProximitySourceTransferFlow _registerMessages]
- -[TSProximitySourceTransferFlow _registerMessages].cold.1
- -[TSProximitySourceTransferFlow initForResumption]
- -[TSTravelBuddyViewController tableView:heightForFooterInSection:]
- -[TSWebsheetViewController initWithURL:postdata:]
- GCC_except_table118
- GCC_except_table124
- GCC_except_table129
- GCC_except_table137
- GCC_except_table138
- GCC_except_table149
- GCC_except_table183
- GCC_except_table186
- GCC_except_table194
- GCC_except_table222
- GCC_except_table42
- _OBJC_CLASS_$_TSIdentityShareViewController
- _OBJC_CLASS_$_UIListContentConfiguration
- _OBJC_IVAR_$_TSIdentityShareFlow._isDeviceInfo
- _OBJC_IVAR_$_TSIdentityShareViewController._cancelButton
- _OBJC_IVAR_$_TSIdentityShareViewController._delegate
- _OBJC_IVAR_$_TSIdentityShareViewController._details
- _OBJC_IVAR_$_TSIdentityShareViewController._detailtitle
- _OBJC_IVAR_$_TSPRXIdentityShareViewController._systemMonitor
- _OBJC_METACLASS_$_TSIdentityShareViewController
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UIView_$_UIKitExtras
- __OBJC_$_CATEGORY_UIView_$_UIKitExtras
- __OBJC_$_CLASS_METHODS_TSIdentityShareViewController
- __OBJC_$_INSTANCE_METHODS_TSIdentityShareViewController
- __OBJC_$_INSTANCE_METHODS_UIViewController(Flow|InModalPresentation|SubFlow)
- __OBJC_$_INSTANCE_VARIABLES_TSIdentityShareViewController
- __OBJC_$_PROP_LIST_TSIdentityShareViewController
- __OBJC_CLASS_PROTOCOLS_$_TSIdentityShareViewController
- __OBJC_CLASS_RO_$_TSIdentityShareViewController
- __OBJC_METACLASS_RO_$_TSIdentityShareViewController
- ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.484
- ___39-[SSScanViewController decodeMetadata:]_block_invoke.51
- ___50-[TSProximitySourceTransferFlow _registerMessages]_block_invoke
- ___50-[TSProximitySourceTransferFlow _registerMessages]_block_invoke_2
- ___51-[TSProximitySourceTransferFlow _bootstrapTransfer]_block_invoke.144
- ___55-[TSPRXIdentityShareViewController _startSystemMonitor]_block_invoke
- ___55-[TSPRXIdentityShareViewController _startSystemMonitor]_block_invoke_2
- ___59-[TSSinglePlanTransferViewController _startPendingInstall:]_block_invoke_4
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.100
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.99.cold.1
- ___70-[TSCellularSetupLoadingViewController safariViewControllerDidFinish:]_block_invoke.94
- ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.108
- ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.530
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.102
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.102.cold.1
- ___79-[TSCellularSetupLoadingViewController setupCoreTelephonyClientForRemoteSignup]_block_invoke.61
- ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.595
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.542
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.542.cold.1
- ___block_descriptor_40_e8_32w_e79_v32?0"NSDictionary"8"NSDictionary"16?<v?i"NSDictionary""NSDictionary">24lw32l8
- ___block_literal_global.105
- ___block_literal_global.117
- ___block_literal_global.137
- ___block_literal_global.393
- ___block_literal_global.483
- ___block_literal_global.486
- ___block_literal_global.544
- ___block_literal_global.648
- ___block_literal_global.678
- ___block_literal_global.71
- ___block_literal_global.738
- _objc_msgSend$_registerMessages
- _objc_msgSend$_startScanning
- _objc_msgSend$_validCarrierName
- _objc_msgSend$center
- _objc_msgSend$footerConfiguration
- _objc_msgSend$initForResumption
- _objc_msgSend$initWithPlans:skip:isForCrossPlatformTransfer:
- _objc_msgSend$initWithURL:postdata:
- _objc_msgSend$navigationBar
- _objc_msgSend$numActivePlansOnDevice
- _objc_msgSend$registerRequestID:options:handler:
- _objc_msgSend$setCenter:
- _objc_msgSend$setContentMode:
CStrings:
+ " error=%@"
+ " targetIccidHash=%@"
+ "+ %"
+ "+[TSUtilities numActivePlansOnDeviceExcept:]"
+ "-[TSDeviceInfoViewController getPhoneInfoFromCT]"
+ "-[TSDeviceInfoViewController initWithOptions:]"
+ "-[TSIdentityShareFlow appBackgrounded]"
+ "-[TSPRXIdentityShareViewController _registerLockState]"
+ "-[TSPRXIdentityShareViewController _registerLockState]_block_invoke"
+ "-[TSPRXIdentityShareViewController dealloc]"
+ "-[TSPRXIdentityShareViewController viewWillDisappear:]"
+ "-[TSTermsAndConditionsViewController _cancelTransfer:]"
+ "5"
+ "@\"OBTrayButton\""
+ "@\"OBTrayButton\"16@0:8"
+ "@\"UIColor\"16@?0@\"UIColor\"8"
+ "@28@0:8i16B20B24"
+ "@36@0:8B16@20B28B32"
+ "@40@0:8@16@24B32B36"
+ "ACTIVATE"
+ "BuddyPinAutoLayout"
+ "CELLULAR_PLAN_COMPLETE_DETAIL_FOR_UNSELECTED_ESIM_%@"
+ "CROSSPLATFORM_TRANSFER_LEARN_MORE"
+ "CSN"
+ "CTCELLULARPLANERROR_TRANSFER_CANCEL_ON_TARGET_MESSAGE"
+ "False"
+ "IPAD_PRXCARD_TARGET_TRANSFER_FAILED_DETAIL_%@_%d"
+ "IsPreSharedKeyPresent"
+ "MULTISIM_RESULT_ALL_PENDING_DETAIL"
+ "MULTISIM_RESULT_DETAIL_ALL_SUCCESS"
+ "MULTISIM_RESULT_PENDING_TITLE"
+ "MULTISIM_RESULT_SOME_FAILURE_SOME_PENDING_DETAIL"
+ "NavigationBar"
+ "PRXCARD_TARGET_TRANSFER_FAILED_DETAIL_%@_%d"
+ "T&C cancelled @%s"
+ "T@\"NSString\",&,V_detailText"
+ "T@\"OBTrayButton\",&"
+ "T@\"OBTrayButton\",&,V_spinnerContainer"
+ "T@\"OBTrayButton\",&,VspinnerContainer"
+ "T@\"SSOBBoldTrayButton\",&,V_doneButton"
+ "TRANSFER_WEBSHEET_LOADING_MESSAGE_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_FOOTER"
+ "TRAVEL_BUDDY_TRAVEL_PSIM_FOOTER"
+ "TRAVEL_MODE_ESIM_LDM_BODY"
+ "TRAVEL_MODE_PSIM_LDM_BODY"
+ "True"
+ "[Db] Stop NFC in dealloc @%s"
+ "[Db] Stop NFC in device lock handler @%s"
+ "[Db] Stop NFC in viewWillDisappear @%s"
+ "[Db] TSIdentityShareFlow appBackgrounded @%s"
+ "[Db] sender = %@ @%s"
+ "[Db] vc:%@ @%s"
+ "[E]Barcode generation failed. @%s"
+ "[E]Could not create CoreTelephonyClient! @%s"
+ "[E]Could not get any phoneInfo from input options or CoreTelephonyClient! @%s"
+ "[E]getMobileEquipmentInfo: failed: %{public}@ @%s"
+ "[E]mobileEquipmentInfoList.meInfoList was unexpectedly nil @%s"
+ "[E]unable to register @%s"
+ "_LearnMoreButton"
+ "_LearnMoreButtonTapped"
+ "_detailText"
+ "_isPlanSelected:selectedItems:"
+ "_isSubTextSelected"
+ "_maybeEnableDoneButton"
+ "allButtons"
+ "buttonWithType:"
+ "constraintLessThanOrEqualToAnchor:multiplier:constant:"
+ "convertRect:fromView:"
+ "detailText"
+ "doneButton"
+ "extractPhoneInfoFromOptions:"
+ "findFirstResponderInView:"
+ "getMobileEquipmentInfo:"
+ "getPhoneInfoFromCT"
+ "handle multi plan install status : %@ isEndSession %@ @%s"
+ "host"
+ "https://support.apple.com/119606"
+ "imageBySamplingNearest"
+ "initForRemotePlan:carrierName:skipUIDismissal:showCarrierWarning:"
+ "initForResumptionWithSelectedTransferPlans:targetUICapability:isPreSharedKeyPresent:"
+ "initWithCarrierName:"
+ "initWithPlans:selectedItems:skip:isForCrossPlatformTransfer:"
+ "initWithURL:postdata:carrierName:"
+ "isSolariumEnabled"
+ "kCrossTransferEndSession"
+ "listCellConfiguration"
+ "meInfoList"
+ "migrate.google"
+ "numActivePlansOnDeviceExcept(%@): %ld @%s"
+ "numActivePlansOnDeviceExcept:"
+ "pinToEdges:"
+ "pinToHorizontalEdges:"
+ "pinToVerticalEdges:"
+ "scrollRectToVisible:animated:"
+ "setBackgroundColorTransformer:"
+ "setBackgroundConfiguration:"
+ "setContentInset:"
+ "setDetailText:"
+ "setDoneButton:"
+ "setEnablesReturnKeyAutomatically:"
+ "setMinimumFontSize:"
+ "setNavigationBarColor"
+ "setScrollIndicatorInsets:"
+ "setShouldAdjustScrollViewInsetForKeyboard:"
+ "subviews"
+ "supportsAVCaptureSessionPreset:"
+ "target"
+ "v24@0:8@\"OBTrayButton\"16"
+ "whiteColor"
+ "\xc4\xd1"
- "* %"
- "+[TSUtilities numActivePlansOnDevice]"
- "-[TSPRXIdentityShareViewController _startSystemMonitor]_block_invoke_2"
- "-[TSPRXIdentityShareViewController _stopSystemMonitor]"
- "-[TSProximitySourceTransferFlow _registerMessages]"
- "6"
- "@\"UIView\"16@0:8"
- "ACTIVATE_NEW_ESIM_ALERT_TITLE_WITH_CARRIER_%@"
- "DEVICE_INFO_TITLE"
- "DONOT_SHARE"
- "MULTISIM_RESULT_DETAIL"
- "PRXCARD_TARGET_TRANSFER_FAILED_DETAIL_%@"
- "SHARE"
- "T@\"NSString\",&,N,V_details"
- "T@\"NSString\",&,N,V_detailtitle"
- "T@\"UIView\",&"
- "T@\"UIView\",&,VspinnerContainer"
- "TB,V_isDeviceInfo"
- "TRAVEL_ESIM_SETUP_COMPLETE_ABROAD_DETAILS_DATA_NO_INFO"
- "TRAVEL_MODE_LDM_BODY"
- "TRAVEL_PSIM_SETUP_COMPLETE_ABROAD_DETAILS_DATA_NO_INFO"
- "TSIdentityShareViewController"
- "[Db] register cu.message @%s"
- "_detailtitle"
- "_isDeviceInfo"
- "_registerMessages"
- "_startScanning"
- "center"
- "detailtitle"
- "footerConfiguration"
- "handle multi plan install status : %@ @%s"
- "initForResumption"
- "initWithPlans:skip:isForCrossPlatformTransfer:"
- "initWithURL:postdata:"
- "isDeviceInfo"
- "migrate.google.com"
- "navigationBar"
- "numActivePlansOnDevice"
- "numActivePlansOnDevice: %ld @%s"
- "registerRequestID:options:handler:"
- "setCenter:"
- "setContentMode:"
- "setDetailtitle:"
- "setIsDeviceInfo:"
- "v24@0:8@\"UIView\"16"
- "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@?<v@?i@\"NSDictionary\"@\"NSDictionary\">24"
- "\xb4\xd1"

```
