## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-752.0.0.0.0
-  __TEXT.__text: 0x7c0a8
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x73dc
-  __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0xa245
-  __TEXT.__oslogstring: 0x4539
-  __TEXT.__gcc_except_tab: 0x1398
-  __TEXT.__dlopen_cstrs: 0x206
-  __TEXT.__unwind_info: 0x1ad8
-  __TEXT.__objc_classname: 0x102c
-  __TEXT.__objc_methname: 0x10a45
-  __TEXT.__objc_methtype: 0x2f58
-  __TEXT.__objc_stubs: 0xac60
-  __DATA_CONST.__got: 0x8b0
-  __DATA_CONST.__const: 0x14b0
-  __DATA_CONST.__objc_classlist: 0x360
-  __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0xe8
+849.1.0.0.0
+  __TEXT.__text: 0xa8970
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x9704
+  __TEXT.__const: 0x1b0
+  __TEXT.__gcc_except_tab: 0x1c14
+  __TEXT.__cstring: 0xec28
+  __TEXT.__oslogstring: 0x5fa7
+  __TEXT.__dlopen_cstrs: 0x2be
+  __TEXT.__ustring: 0xa
+  __TEXT.__unwind_info: 0x23a8
+  __TEXT.__objc_classname: 0x14bb
+  __TEXT.__objc_methname: 0x14c98
+  __TEXT.__objc_methtype: 0x32cf
+  __TEXT.__objc_stubs: 0xd500
+  __DATA_CONST.__got: 0xa20
+  __DATA_CONST.__const: 0x1c70
+  __DATA_CONST.__objc_classlist: 0x458
+  __DATA_CONST.__objc_catlist: 0x50
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3de8
+  __DATA_CONST.__objc_selrefs: 0x4c30
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x310
-  __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x410
-  __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x4960
-  __AUTH_CONST.__objc_const: 0x29e18
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_intobj: 0x480
-  __AUTH.__objc_data: 0x2170
-  __DATA.__objc_ivar: 0xa50
-  __DATA.__data: 0xaf0
-  __DATA.__bss: 0x140
+  __DATA_CONST.__objc_superrefs: 0x408
+  __DATA_CONST.__objc_arraydata: 0x48
+  __AUTH_CONST.__auth_got: 0x420
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__cfstring: 0x6ba0
+  __AUTH_CONST.__objc_const: 0x3b3a8
+  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH.__objc_data: 0x2b20
+  __DATA.__objc_ivar: 0xdcc
+  __DATA.__data: 0xb50
+  __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/StoreKit.framework/StoreKit
+  - /System/Library/Frameworks/Symbols.framework/Symbols
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents

   - /System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
+  - /System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D052AD71-5509-363E-A48B-A1B418DC34F0
-  Functions: 2750
-  Symbols:   10245
-  CStrings:  5313
+  UUID: AE2571EF-97C0-33BC-8068-B3AED64D81D9
+  Functions: 3648
+  Symbols:   13319
+  CStrings:  6911
 
Symbols:
+ +[SSManualEntryCell rowHeight]
+ +[TSDeviceInfoViewController _isSecureForRemoteViewService]
+ +[TSIdentityShareFlow showAlert]
+ +[TSIdentityShareViewController _isSecureForRemoteViewService]
+ +[TSPRXIdentityShareViewController _isSecureForRemoteViewService]
+ +[TSSIMSetupFlow _flowWithOptions:].cold.5
+ +[TSSinglePlanTransferViewController getTitleAndDetailsForPlanType:transferCapability:isShowingFilteredPlans:carrier:]
+ +[TSSinglePlanTransferViewController getTitleAndDetailsForPlanType:transferCapability:isShowingFilteredPlans:carrier:].cold.1
+ +[TSUtilities alsPlanCarriers:]
+ +[TSUtilities appendLeftToRightMark:]
+ +[TSUtilities areAnyPlansOnDevice]
+ +[TSUtilities compareProductVersion:toProductVersion:]
+ +[TSUtilities concatenateDescriptors:]
+ +[TSUtilities formatLocAndConcatenateDescriptors:]
+ +[TSUtilities getCellularPlanItem:withIccid:]
+ +[TSUtilities getErrorDescription:]
+ +[TSUtilities getPlanByID:fromPlans:]
+ +[TSUtilities getWordRepresentationForInt:]
+ +[TSUtilities isIccidForPhySlot:]
+ +[TSUtilities isLanguageRightToLeft]
+ +[TSUtilities isNFCEnable]
+ +[TSUtilities isPhone]
+ +[TSUtilities isRegRestLocationUnavailable:]
+ +[TSUtilities numActivePlansOnDevice]
+ +[TSUtilities odaPlanCarriers:]
+ +[TSUtilities planItemText:]
+ +[TSUtilities productVersion]
+ +[TSUtilities skEventFromDictionary:]
+ +[TSUtilities sourceDevicesCount:]
+ +[TSUtilities transferablePlanCarriers:]
+ -[CTDisplayPlan(SimSetup) identifier]
+ -[CTDisplayPlan(SimSetup) isRegulatoryRestrictedPlan]
+ -[CTDisplayPlan(UITableViewCell) imageName]
+ -[CTDisplayPlan(UITableViewCell) text]
+ -[CrossPlatformManualDetailsViewController .cxx_destruct]
+ -[CrossPlatformManualDetailsViewController _constructDCTUrl:withPasscode:]
+ -[CrossPlatformManualDetailsViewController _doneButtonTapped]
+ -[CrossPlatformManualDetailsViewController _doneButtonTapped].cold.1
+ -[CrossPlatformManualDetailsViewController animating]
+ -[CrossPlatformManualDetailsViewController cachedButtons]
+ -[CrossPlatformManualDetailsViewController canBeShownFromSuspendedState]
+ -[CrossPlatformManualDetailsViewController continueButton]
+ -[CrossPlatformManualDetailsViewController dctDelegate]
+ -[CrossPlatformManualDetailsViewController delegate]
+ -[CrossPlatformManualDetailsViewController init]
+ -[CrossPlatformManualDetailsViewController keyboardWasShown:]
+ -[CrossPlatformManualDetailsViewController keyboardWillBeHidden:]
+ -[CrossPlatformManualDetailsViewController numberOfSectionsInTableView:]
+ -[CrossPlatformManualDetailsViewController resetFirstResponder]
+ -[CrossPlatformManualDetailsViewController setAnimating:]
+ -[CrossPlatformManualDetailsViewController setCachedButtons:]
+ -[CrossPlatformManualDetailsViewController setContinueButton:]
+ -[CrossPlatformManualDetailsViewController setDctDelegate:]
+ -[CrossPlatformManualDetailsViewController setDelegate:]
+ -[CrossPlatformManualDetailsViewController setSpinner:]
+ -[CrossPlatformManualDetailsViewController setSpinnerContainer:]
+ -[CrossPlatformManualDetailsViewController spinnerContainer]
+ -[CrossPlatformManualDetailsViewController spinner]
+ -[CrossPlatformManualDetailsViewController tableView:cellForRowAtIndexPath:]
+ -[CrossPlatformManualDetailsViewController tableView:numberOfRowsInSection:]
+ -[CrossPlatformManualDetailsViewController textFieldDidBeginEditing:]
+ -[CrossPlatformManualDetailsViewController textFieldDidEndEditing:]
+ -[CrossPlatformManualDetailsViewController textFieldShouldReturn:]
+ -[CrossPlatformManualDetailsViewController viewDidAppear:]
+ -[CrossPlatformManualDetailsViewController viewDidLayoutSubviews]
+ -[CrossPlatformManualDetailsViewController viewDidLoad]
+ -[CrossPlatformManualDetailsViewController viewWillAppear:]
+ -[CrossPlatformManualDetailsViewController viewWillDisappear:]
+ -[CrossPlatformShowManualDetailsViewController .cxx_destruct]
+ -[CrossPlatformShowManualDetailsViewController canBeShownFromSuspendedState]
+ -[CrossPlatformShowManualDetailsViewController dctInfo]
+ -[CrossPlatformShowManualDetailsViewController delegate]
+ -[CrossPlatformShowManualDetailsViewController initWithAuthCode:]
+ -[CrossPlatformShowManualDetailsViewController numberOfSectionsInTableView:]
+ -[CrossPlatformShowManualDetailsViewController queryParamToTitle]
+ -[CrossPlatformShowManualDetailsViewController setDctInfo:]
+ -[CrossPlatformShowManualDetailsViewController setDelegate:]
+ -[CrossPlatformShowManualDetailsViewController setQueryParamToTitle:]
+ -[CrossPlatformShowManualDetailsViewController tableView:cellForRowAtIndexPath:]
+ -[CrossPlatformShowManualDetailsViewController tableView:numberOfRowsInSection:]
+ -[CrossPlatformShowManualDetailsViewController viewDidAppear:]
+ -[CrossPlatformShowManualDetailsViewController viewDidLayoutSubviews]
+ -[CrossPlatformShowManualDetailsViewController viewDidLoad]
+ -[CrossPlatformShowManualDetailsViewController viewWillAppear:]
+ -[CrossPlatformTransferAuthQRCodeViewController _cancelButtonTapped]
+ -[CrossPlatformTransferAuthQRCodeViewController _otherButtonTapped]
+ -[CrossPlatformTransferAuthQRCodeViewController isCancelButtonTapped]
+ -[CrossPlatformTransferAuthQRCodeViewController isOtherButtonTapped]
+ -[CrossPlatformTransferAuthQRCodeViewController isStartOverRequiredOnBackButtonTapped]
+ -[CrossPlatformTransferAuthQRCodeViewController otherOptionsButton]
+ -[CrossPlatformTransferAuthQRCodeViewController setIsCancelButtonTapped:]
+ -[CrossPlatformTransferAuthQRCodeViewController setIsOtherButtonTapped:]
+ -[CrossPlatformTransferAuthQRCodeViewController setOtherOptionsButton:]
+ -[CrossPlatformTransferAuthQRCodeViewController viewWillAppear:]
+ -[CrossPlatformTransferIntroViewController .cxx_destruct]
+ -[CrossPlatformTransferIntroViewController _cancelButtonTapped]
+ -[CrossPlatformTransferIntroViewController _doneButtonTapped]
+ -[CrossPlatformTransferIntroViewController delegate]
+ -[CrossPlatformTransferIntroViewController init]
+ -[CrossPlatformTransferIntroViewController setDelegate:]
+ -[CrossPlatformTransferIntroViewController viewDidLoad]
+ -[CrossPlatformTransferSourceSelectionWarningViewController _handleNotificationESIMInstallStateChanged:]
+ -[CrossPlatformTransferSourceSelectionWarningViewController init]
+ -[CrossPlatformTransferSourceSelectionWarningViewController viewDidLoad]
+ -[ExitBuddyIconView initWithFrame:]
+ -[NSString(PhoneNumber) formattedPhoneNumber]
+ -[NSString(QRCode) parseQueryParamsWithTitleDictionary:]
+ -[NSString(SHA256) sha256]
+ -[SSCardManualEntryViewController .cxx_destruct]
+ -[SSCardManualEntryViewController _heightAnchorConstant]
+ -[SSCardManualEntryViewController addNewPlanWithUserInfo]
+ -[SSCardManualEntryViewController backOption]
+ -[SSCardManualEntryViewController canBeShownFromSuspendedState]
+ -[SSCardManualEntryViewController delegate]
+ -[SSCardManualEntryViewController heightAnchor]
+ -[SSCardManualEntryViewController init]
+ -[SSCardManualEntryViewController keyboardDidHide:]
+ -[SSCardManualEntryViewController keyboardWasShown:]
+ -[SSCardManualEntryViewController numberOfSectionsInTableView:]
+ -[SSCardManualEntryViewController onError]
+ -[SSCardManualEntryViewController resetFirstResponder]
+ -[SSCardManualEntryViewController setDelegate:]
+ -[SSCardManualEntryViewController setHeightAnchor:]
+ -[SSCardManualEntryViewController tableView:cellForRowAtIndexPath:]
+ -[SSCardManualEntryViewController tableView:cellForRowAtIndexPath:].cold.1
+ -[SSCardManualEntryViewController tableView:numberOfRowsInSection:]
+ -[SSCardManualEntryViewController textField:shouldChangeCharactersInRange:replacementString:]
+ -[SSCardManualEntryViewController textFieldDidBeginEditing:]
+ -[SSCardManualEntryViewController textFieldDidEndEditing:]
+ -[SSCardManualEntryViewController textFieldShouldReturn:]
+ -[SSCardManualEntryViewController updateTableHeightAnchor]
+ -[SSCardManualEntryViewController viewDidAppear:]
+ -[SSCardManualEntryViewController viewDidLayoutSubviews]
+ -[SSCardManualEntryViewController viewDidLoad]
+ -[SSCardManualEntryViewController viewWillAppear:]
+ -[SSCardManualEntryViewController viewWillDisappear:]
+ -[SSCellularPlanScanViewController .cxx_destruct]
+ -[SSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]
+ -[SSCellularPlanScanViewController _learnMoreTapped]
+ -[SSCellularPlanScanViewController confirmationCodeRequired]
+ -[SSCellularPlanScanViewController entryPoint]
+ -[SSCellularPlanScanViewController fauxCardData]
+ -[SSCellularPlanScanViewController initWithBackButton:]
+ -[SSCellularPlanScanViewController onCodeDetected:completion:]
+ -[SSCellularPlanScanViewController onCodeDetected:completion:].cold.1
+ -[SSCellularPlanScanViewController setEntryPoint:]
+ -[SSCellularPlanScanViewController transferViaQRCode]
+ -[SSCellularPlanScanViewController viewDidLoad]
+ -[SSCellularPlanScanViewController viewWillAppear:]
+ -[SSCellularSetupMultiSIMActivatingViewController .cxx_destruct]
+ -[SSCellularSetupMultiSIMActivatingViewController _statusDescription:info:]
+ -[SSCellularSetupMultiSIMActivatingViewController accessoryViewForStatus:]
+ -[SSCellularSetupMultiSIMActivatingViewController delegate]
+ -[SSCellularSetupMultiSIMActivatingViewController initWithPlanInfos:]
+ -[SSCellularSetupMultiSIMActivatingViewController initWithPlanInfos:].cold.1
+ -[SSCellularSetupMultiSIMActivatingViewController isPlanInstalledAndNotEnabled:item:]
+ -[SSCellularSetupMultiSIMActivatingViewController plans]
+ -[SSCellularSetupMultiSIMActivatingViewController setDelegate:]
+ -[SSCellularSetupMultiSIMActivatingViewController setPlans:]
+ -[SSCellularSetupMultiSIMActivatingViewController updateInstallationStatus:forPlanID:]
+ -[SSCellularSetupMultiSIMActivatingViewController updateInstallationStatus:forPlanID:].cold.1
+ -[SSCellularSetupMultiSIMActivatingViewController(TSSetupFlowItem) prepare:]
+ -[SSCellularSetupMultiSIMActivatingViewController(UITableViewDataSource) tableView:cellForRowAtIndexPath:]
+ -[SSCellularSetupMultiSIMActivatingViewController(UITableViewDataSource) tableView:cellForRowAtIndexPath:].cold.1
+ -[SSCellularSetupMultiSIMActivatingViewController(UITableViewDataSource) tableView:numberOfRowsInSection:]
+ -[SSCellularSetupMultiSIMActivatingViewController(ViewLifeCycle) _setupTableView]
+ -[SSCellularSetupMultiSIMActivatingViewController(ViewLifeCycle) viewDidLoad]
+ -[SSCellularSetupMultiSIMConnectingViewController initWithPlanInfos:userEnablePlans:skip:]
+ -[SSCellularSetupMultiSIMConnectingViewController setSkip:]
+ -[SSCellularSetupMultiSIMConnectingViewController skip]
+ -[SSCellularSetupMultiSIMConnectingViewController(TSSetupFlowItem) _areAllPlansInTerminalState]
+ -[SSCellularSetupMultiSIMConnectingViewController(TSSetupFlowItem) accessoryViewForStatus:]
+ -[SSCellularSetupMultiSIMConnectingViewController(TSSetupFlowItem) prepare:]
+ -[SSConfirmationCodeViewController .cxx_destruct]
+ -[SSConfirmationCodeViewController _hideKeyboard]
+ -[SSConfirmationCodeViewController _setupLayoutConstraint]
+ -[SSConfirmationCodeViewController _textFieldDidChange]
+ -[SSConfirmationCodeViewController canBeShownFromSuspendedState]
+ -[SSConfirmationCodeViewController codeTextField]
+ -[SSConfirmationCodeViewController confirm:]
+ -[SSConfirmationCodeViewController confirmationCode]
+ -[SSConfirmationCodeViewController continueButton]
+ -[SSConfirmationCodeViewController delegate]
+ -[SSConfirmationCodeViewController initAsMidOperationWithCarrierName:]
+ -[SSConfirmationCodeViewController initAsMidOperationWithCarrierName:requireGeneralConsent:]
+ -[SSConfirmationCodeViewController initWithCardData:]
+ -[SSConfirmationCodeViewController setCodeTextField:]
+ -[SSConfirmationCodeViewController setContinueButton:]
+ -[SSConfirmationCodeViewController setDelegate:]
+ -[SSConfirmationCodeViewController textField:shouldChangeCharactersInRange:replacementString:]
+ -[SSConfirmationCodeViewController textFieldShouldBeginEditing:]
+ -[SSConfirmationCodeViewController textFieldShouldReturn:]
+ -[SSConfirmationCodeViewController userDidTapCancel]
+ -[SSConfirmationCodeViewController viewDidAppear:]
+ -[SSConfirmationCodeViewController viewDidLoad]
+ -[SSConfirmationCodeViewController viewWillDisappear:]
+ -[SSCrossPlatformScanViewController init]
+ -[SSCrossPlatformTransferSourceSelectionViewController _cancelButtonTapped]
+ -[SSCrossPlatformTransferSourceSelectionViewController _laterButtonTapped]
+ -[SSCrossPlatformTransferSourceSelectionViewController _preselectPlanIfNeeded]
+ -[SSCrossPlatformTransferSourceSelectionViewController initWithPlans:planItems:fromDataTransferSession:]
+ -[SSCrossPlatformTransferSourceSelectionViewController viewDidAppear:]
+ -[SSInstallPlanInformation .cxx_destruct]
+ -[SSInstallPlanInformation activatingState]
+ -[SSInstallPlanInformation carrierErrorCode]
+ -[SSInstallPlanInformation carrierName]
+ -[SSInstallPlanInformation confirmationCodeViewController]
+ -[SSInstallPlanInformation description]
+ -[SSInstallPlanInformation displayPlan]
+ -[SSInstallPlanInformation eSIMTravelState]
+ -[SSInstallPlanInformation identifier]
+ -[SSInstallPlanInformation imageName]
+ -[SSInstallPlanInformation initWithItem:]
+ -[SSInstallPlanInformation initWithPlan:]
+ -[SSInstallPlanInformation installError]
+ -[SSInstallPlanInformation installationEndTime]
+ -[SSInstallPlanInformation installationStartTime]
+ -[SSInstallPlanInformation isDataOnly]
+ -[SSInstallPlanInformation isDisabled]
+ -[SSInstallPlanInformation isPreInstalled]
+ -[SSInstallPlanInformation isUserInHomeCountry]
+ -[SSInstallPlanInformation maybeUpdateTimeoutStatus:]
+ -[SSInstallPlanInformation phoneNumber]
+ -[SSInstallPlanInformation planItem]
+ -[SSInstallPlanInformation planName]
+ -[SSInstallPlanInformation postdata]
+ -[SSInstallPlanInformation setCarrierErrorCode:]
+ -[SSInstallPlanInformation setConfirmationCodeViewController:]
+ -[SSInstallPlanInformation setDisplayPlan:]
+ -[SSInstallPlanInformation setESIMTravelState:]
+ -[SSInstallPlanInformation setInstallError:]
+ -[SSInstallPlanInformation setInstallationEndTime:]
+ -[SSInstallPlanInformation setInstallationStartTime:]
+ -[SSInstallPlanInformation setIsDataOnly:]
+ -[SSInstallPlanInformation setIsDisabled:]
+ -[SSInstallPlanInformation setIsPreInstalled:]
+ -[SSInstallPlanInformation setIsUserInHomeCountry:]
+ -[SSInstallPlanInformation setPhoneNumber:]
+ -[SSInstallPlanInformation setPlanItem:]
+ -[SSInstallPlanInformation setPlanName:]
+ -[SSInstallPlanInformation setPostdata:]
+ -[SSInstallPlanInformation setStatus:]
+ -[SSInstallPlanInformation setTargetIccid:]
+ -[SSInstallPlanInformation setTargetIccidHash:]
+ -[SSInstallPlanInformation setUseTravelOnly:]
+ -[SSInstallPlanInformation setWaitForPhoneNumber:]
+ -[SSInstallPlanInformation setWebsheetUrl:]
+ -[SSInstallPlanInformation status]
+ -[SSInstallPlanInformation targetIccidHash]
+ -[SSInstallPlanInformation targetIccid]
+ -[SSInstallPlanInformation text]
+ -[SSInstallPlanInformation updateTargetIccidInfo:]
+ -[SSInstallPlanInformation useTravelOnly]
+ -[SSInstallPlanInformation waitForPhoneNumber]
+ -[SSInstallPlanInformation websheetUrl]
+ -[SSLabelPickerViewController .cxx_destruct]
+ -[SSLabelPickerViewController _doneButtonTapped]
+ -[SSLabelPickerViewController associatedPlanItem]
+ -[SSLabelPickerViewController chosenLabelIndexPath]
+ -[SSLabelPickerViewController chosenLabel]
+ -[SSLabelPickerViewController customLabelIndexPath]
+ -[SSLabelPickerViewController customLabelRowValue]
+ -[SSLabelPickerViewController customLabel]
+ -[SSLabelPickerViewController dealloc]
+ -[SSLabelPickerViewController initWithAssociatedPlanItem:initialLabel:predefinedUserLabels:]
+ -[SSLabelPickerViewController initialLabel]
+ -[SSLabelPickerViewController numberOfSectionsInTableView:]
+ -[SSLabelPickerViewController predefinedUserLabels]
+ -[SSLabelPickerViewController setAssociatedPlanItem:]
+ -[SSLabelPickerViewController setChosenLabelIndexPath:]
+ -[SSLabelPickerViewController setCustomLabel:]
+ -[SSLabelPickerViewController setInitialLabel:]
+ -[SSLabelPickerViewController setPredefinedUserLabels:]
+ -[SSLabelPickerViewController tableView:cellForRowAtIndexPath:]
+ -[SSLabelPickerViewController tableView:didSelectRowAtIndexPath:]
+ -[SSLabelPickerViewController tableView:numberOfRowsInSection:]
+ -[SSLabelPickerViewController tableView:titleForHeaderInSection:]
+ -[SSLabelPickerViewController textFieldDidEndEditing:]
+ -[SSLabelPickerViewController viewDidLayoutSubviews]
+ -[SSLabelPickerViewController viewDidLoad]
+ -[SSLimitedSelectableTableView .cxx_destruct]
+ -[SSLimitedSelectableTableView _refreshTableView]
+ -[SSLimitedSelectableTableView initWithFrame:style:limit:]
+ -[SSLimitedSelectableTableView limit]
+ -[SSLimitedSelectableTableView selectRowAtIndexPath:animated:scrollPosition:]
+ -[SSLimitedSelectableTableView setDelegate:]
+ -[SSLimitedSelectableTableView setLimit:]
+ -[SSLimitedSelectableTableView setViewDelegate:]
+ -[SSLimitedSelectableTableView tableView:didDeselectRowAtIndexPath:]
+ -[SSLimitedSelectableTableView tableView:didSelectRowAtIndexPath:]
+ -[SSLimitedSelectableTableView viewDelegate]
+ -[SSManualEntryCell .cxx_destruct]
+ -[SSManualEntryCell disablePredicativeTextForTextField:]
+ -[SSManualEntryCell editableTextField]
+ -[SSManualEntryCell prepareForReuse]
+ -[SSManualEntryCell setEditableTextField:]
+ -[SSManualEntryCell setupConstraints]
+ -[SSManualEntryCell setupViewsWithTag:delegate:]
+ -[SSManualEntryCell setupWithDelegate:indexPath:]
+ -[SSMultiSIMResultViewController .cxx_destruct]
+ -[SSMultiSIMResultViewController _continueButtonTapped]
+ -[SSMultiSIMResultViewController backOption]
+ -[SSMultiSIMResultViewController delegate]
+ -[SSMultiSIMResultViewController heightAnchor]
+ -[SSMultiSIMResultViewController initWithPlanInfos:]
+ -[SSMultiSIMResultViewController numberOfSectionsInTableView:]
+ -[SSMultiSIMResultViewController pushTimeoutFailureViewControllerWithStatus:forPlan:]
+ -[SSMultiSIMResultViewController pushToDetailViewControllerWithError:forPlan:]
+ -[SSMultiSIMResultViewController pushToDetailViewControllerWithError:forPlan:].cold.1
+ -[SSMultiSIMResultViewController setDelegate:]
+ -[SSMultiSIMResultViewController setHeightAnchor:]
+ -[SSMultiSIMResultViewController tableView:cellForRowAtIndexPath:]
+ -[SSMultiSIMResultViewController tableView:cellForRowAtIndexPath:].cold.1
+ -[SSMultiSIMResultViewController tableView:didSelectRowAtIndexPath:]
+ -[SSMultiSIMResultViewController tableView:didSelectRowAtIndexPath:].cold.1
+ -[SSMultiSIMResultViewController tableView:numberOfRowsInSection:]
+ -[SSMultiSIMResultViewController viewDidLoad]
+ -[SSMultiSIMResultViewController(TSSetupFlowItem) prepare:]
+ -[SSPRXD2DMigrationDoneViewController .cxx_destruct]
+ -[SSPRXD2DMigrationDoneViewController _launchDisembarkUI:]
+ -[SSPRXD2DMigrationDoneViewController delegate]
+ -[SSPRXD2DMigrationDoneViewController init]
+ -[SSPRXD2DMigrationDoneViewController setDelegate:]
+ -[SSProximityDevice activateUsingPreSharedKey:completion:]
+ -[SSScanViewController _otherButtonTapped]
+ -[SSScanViewController initWithTitle:detail:]
+ -[SSScanViewController isEnterManuallyTapped]
+ -[SSScanViewController setIsEnterManuallyTapped:]
+ -[TSActivationFlowWithSimSetupFlow isFlexPolicyOn]
+ -[TSActivationFlowWithSimSetupFlow setIsFlexPolicyOn:]
+ -[TSActivationPolicyMismatchFlow _firstViewController]
+ -[TSActivationPolicyMismatchFlow firstViewController].cold.1
+ -[TSAuthFlow descriptors]
+ -[TSAuthFlow initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:]
+ -[TSAuthFlow isDtoEvaluationRequired]
+ -[TSAuthFlow isSecureIntentRequired]
+ -[TSAuthFlow setDescriptors:]
+ -[TSAuthFlow setIsDtoEvaluationRequired:]
+ -[TSAuthFlow setIsSecureIntentRequired:]
+ -[TSBootstrapCrossPlatformTransferFlow .cxx_destruct]
+ -[TSBootstrapCrossPlatformTransferFlow dctPrewarmSucceded]
+ -[TSBootstrapCrossPlatformTransferFlow firstViewController:]
+ -[TSBootstrapCrossPlatformTransferFlow firstViewController:].cold.1
+ -[TSBootstrapCrossPlatformTransferFlow firstViewController]
+ -[TSBootstrapCrossPlatformTransferFlow firstViewController].cold.1
+ -[TSBootstrapCrossPlatformTransferFlow initWithRetainedObject:isSource:]
+ -[TSBootstrapCrossPlatformTransferFlow isSource]
+ -[TSBootstrapCrossPlatformTransferFlow nextViewControllerFrom:]
+ -[TSBootstrapCrossPlatformTransferFlow setDctPrewarmSucceded:]
+ -[TSBootstrapCrossPlatformTransferFlow setIsSource:]
+ -[TSCellularPlanActivatingFlow _cancelTransferringPlan:]
+ -[TSCellularPlanActivatingFlow _findPlanInfoWithPlanID:]
+ -[TSCellularPlanActivatingFlow _findPlanInfoWithPlanStatus:]
+ -[TSCellularPlanActivatingFlow _findPlanInfoWithTargetIccid:]
+ -[TSCellularPlanActivatingFlow _findPlanInfoWithTargetIccidHash:]
+ -[TSCellularPlanActivatingFlow _firstViewController].cold.1
+ -[TSCellularPlanActivatingFlow _maybeDisplaySourceDeviceConsentAlert:]
+ -[TSCellularPlanActivatingFlow _maybeMoveToNextItem]
+ -[TSCellularPlanActivatingFlow _maybePresentFirstViewController:]
+ -[TSCellularPlanActivatingFlow _maybePresentFirstViewController:].cold.1
+ -[TSCellularPlanActivatingFlow _maybeReplyFirstViewControllerCallbackWithViewController:]
+ -[TSCellularPlanActivatingFlow _maybeReplyFirstViewControllerCallbackWithViewController:].cold.1
+ -[TSCellularPlanActivatingFlow _maybeSendTransferResults]
+ -[TSCellularPlanActivatingFlow _maybeSendTransferUICapability:]
+ -[TSCellularPlanActivatingFlow _maybeStartTimerForNewlyInstalledPlan:newStatus:]
+ -[TSCellularPlanActivatingFlow _onInstallError:]
+ -[TSCellularPlanActivatingFlow _requireSyncUpTransferResultsWithSource]
+ -[TSCellularPlanActivatingFlow allPlansActivated]
+ -[TSCellularPlanActivatingFlow buddyMLViewController]
+ -[TSCellularPlanActivatingFlow cancelledDeviceIDs]
+ -[TSCellularPlanActivatingFlow carrierSetupPlan]
+ -[TSCellularPlanActivatingFlow confirmCellularPlanTransfer]
+ -[TSCellularPlanActivatingFlow defaultVoiceIccid]
+ -[TSCellularPlanActivatingFlow displayedDeviceIDs]
+ -[TSCellularPlanActivatingFlow iccidToEnable]
+ -[TSCellularPlanActivatingFlow initWithEnablingPlanIccid:]
+ -[TSCellularPlanActivatingFlow initWithSelectedPlans:confirmCellularPlanTransfer:isForCrossPlatformTransfer:session:sourceOsVersion:]
+ -[TSCellularPlanActivatingFlow initWithSelectedPlans:confirmCellularPlanTransfer:isForCrossPlatformTransfer:session:sourceOsVersion:].cold.1
+ -[TSCellularPlanActivatingFlow initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:]
+ -[TSCellularPlanActivatingFlow installingPlanInfos]
+ -[TSCellularPlanActivatingFlow isForCrossPlatformTransfer]
+ -[TSCellularPlanActivatingFlow messageSession]
+ -[TSCellularPlanActivatingFlow pendingInteractiveViewControllers]
+ -[TSCellularPlanActivatingFlow planEnablementState]
+ -[TSCellularPlanActivatingFlow presentedViewController]
+ -[TSCellularPlanActivatingFlow setAllPlansActivated:]
+ -[TSCellularPlanActivatingFlow setBuddyMLViewController:]
+ -[TSCellularPlanActivatingFlow setCancelledDeviceIDs:]
+ -[TSCellularPlanActivatingFlow setCarrierSetupPlan:]
+ -[TSCellularPlanActivatingFlow setConfirmCellularPlanTransfer:]
+ -[TSCellularPlanActivatingFlow setDefaultVoiceIccid:]
+ -[TSCellularPlanActivatingFlow setDisplayedDeviceIDs:]
+ -[TSCellularPlanActivatingFlow setIccidToEnable:]
+ -[TSCellularPlanActivatingFlow setInstallingPlanInfos:]
+ -[TSCellularPlanActivatingFlow setIsForCrossPlatformTransfer:]
+ -[TSCellularPlanActivatingFlow setMessageSession:]
+ -[TSCellularPlanActivatingFlow setPendingInteractiveViewControllers:]
+ -[TSCellularPlanActivatingFlow setPlanEnablementState:]
+ -[TSCellularPlanActivatingFlow setPresentedViewController:]
+ -[TSCellularPlanActivatingFlow setSourceOsVersion:]
+ -[TSCellularPlanActivatingFlow setUserEnabledPlanInfos:]
+ -[TSCellularPlanActivatingFlow sourceOsVersion]
+ -[TSCellularPlanActivatingFlow userEnabledPlanInfos]
+ -[TSCellularPlanActivatingFlow(Consolidated) _areAllPlansInPostInstallOrTerminalState]
+ -[TSCellularPlanActivatingFlow(Consolidated) _areAllPlansInTerminalState]
+ -[TSCellularPlanActivatingFlow(Consolidated) _collectAllPhoneNumbersForDevice:]
+ -[TSCellularPlanActivatingFlow(Consolidated) _hasAnyDisabledInstallPlan]
+ -[TSCellularPlanActivatingFlow(Consolidated) _hasAnyPlanSuccessfullyInstalledOrPostInstalled]
+ -[TSCellularPlanActivatingFlow(Consolidated) _hasAnyPlanSuccessfullyInstalled]
+ -[TSCellularPlanActivatingFlow(Consolidated) consolidatedActivatingState]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _handleMultiSIMInstallationStatusUpdateEvent:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _handleOtpStatusUpdate:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _isAppInBackground]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _offerFallbackOption]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _redirectToBTFlow]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _shouldOfferFallbackOptionOnError:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _startedByFollowup]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) launchWebsheet:completion:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) launchWebsheet:completion:].cold.1
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) transferEventUpdate:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) updateProvisioningError:targetIccidHash:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _dequeueInteractiveUI]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _displayCarrierSetupViewController:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _displayConfirmationCodeViewController:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _displayOneTimeCodeViewController:phoneNumber:carrierName:usePin:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _displayTermsAndConditionsViewController:mainText:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _displayWebsheetViewController:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _enqueueInteractiveUI:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _getWebsheetInfo:completion:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _maybeDisplayInteractiveUI:]
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _maybeDisplayInteractiveUI:].cold.1
+ -[TSCellularPlanActivatingFlow(InteractiveUI) _maybeDisplayNextIntermediateViewController]
+ -[TSCellularPlanActivatingFlow(Override) firstViewController:]
+ -[TSCellularPlanActivatingFlow(Override) firstViewController]
+ -[TSCellularPlanActivatingFlow(Override) firstViewController].cold.1
+ -[TSCellularPlanActivatingFlow(Override) nextViewControllerFrom:]
+ -[TSCellularPlanActivatingFlow(Override) setTopViewController:]
+ -[TSCellularPlanActivatingFlow(Single) carrierErrorCode]
+ -[TSCellularPlanActivatingFlow(Single) carrierName]
+ -[TSCellularPlanActivatingFlow(Single) phoneNumber]
+ -[TSCellularPlanActivatingFlow(Single) planError]
+ -[TSCellularPlanActivatingFlow(Single) planName]
+ -[TSCellularPlanActivatingFlow(Single) targetIccid]
+ -[TSCellularPlanActivatingFlow(Single) updatePlanItem]
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handleActivatedItemUpdate:]
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handlePostInstallItemUpdate:]
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handlePostInstallItemUpdate:].cold.1
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handleProvisioningItemUpdate:]
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeDeleteTransferBackItem:]
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeHandleConfirmationCodeError:]
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeHandleConfirmationCodeError:].cold.1
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeHandleProvisioningError:items:]
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeHandleProvisioningError:items:].cold.1
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _shouldWaitUntilPhoneNumberBeReady:completion:]
+ -[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) planItemsUpdated:planListError:]
+ -[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]
+ -[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) navigateToNextPaneFrom:navigationController:]
+ -[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) setDefaultNavigationItems:]
+ -[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) userDidTapCancel]
+ -[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]
+ -[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:].cold.1
+ -[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:].cold.2
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _maybeUpdatePhysicalSIMStatus:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _maybeUpdatePhysicalSIMStatus:].cold.1
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _maybeUpdatePlanNameForTargetIccid:planName:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _maybeUpdatePlanNameWithoutPlanID:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _maybeUpdateUserEnabledPlans:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateCarrierErrorCode:withPlanID:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateCarrierErrorCode:withPlanID:].cold.1
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:].cold.1
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withTargetIccidHash:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withTargetIccidHash:].cold.1
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:forPlanInfo:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:withPlanID:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:withPlanID:].cold.1
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:withTargetIccid:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateTargetIccid:withPlanID:]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateTargetIccid:withPlanID:].cold.1
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateTargetIccidWithoutPlanID:]
+ -[TSCellularPlanItemCell isPhysical]
+ -[TSCellularPlanItemCell setEnable:]
+ -[TSCellularPlanItemCell setIsPhysical:]
+ -[TSCellularPlanLabelsViewController setPendingLabel:forPlanItem:].cold.1
+ -[TSCellularPlanProximityTransferController launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:]
+ -[TSCellularSetupActivatingViewController animating]
+ -[TSCellularSetupActivatingViewController cachedButtons]
+ -[TSCellularSetupActivatingViewController initWithPlans:skip:]
+ -[TSCellularSetupActivatingViewController initWithTitle:details:symbolName:plans:skip:]
+ -[TSCellularSetupActivatingViewController initWithTransferOutPlan:]
+ -[TSCellularSetupActivatingViewController setAnimating:]
+ -[TSCellularSetupActivatingViewController setCachedButtons:]
+ -[TSCellularSetupActivatingViewController setSpinnerContainer:]
+ -[TSCellularSetupActivatingViewController spinnerContainer]
+ -[TSCellularSetupActivatingViewController(TSSetupFlowItem) prepare:]
+ -[TSCellularSetupCompleteViewController _continueButtonTapped].cold.1
+ -[TSCellularSetupCompleteViewController initWithPlanIdentifer:]
+ -[TSCellularSetupCompleteViewController initWithPlans:skip:isForCrossPlatformTransfer:]
+ -[TSCellularSetupCompleteViewController planItem]
+ -[TSCellularSetupCompleteViewController setPlanItem:]
+ -[TSCellularSetupCompleteViewController(TSSetupFlowItem) prepare:]
+ -[TSCellularSetupTimeoutFailureViewController initWithTimeoutReason:isEmbeddedInResultView:plans:]
+ -[TSCellularSetupTimeoutFailureViewController(TSSetupFlowItem) prepare:]
+ -[TSCoreTelephonyClientCache bootstrapPlanTransferUsingMessageSession:flowType:completion:]
+ -[TSCoreTelephonyClientCache submitAutoReconnectionDetails:]
+ -[TSCoreTelephonyClientCache updateSecureIntentData:isDTOEvaluationFailed:]
+ -[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]
+ -[TSCrossPlatformSourceAuthFlow _showCancelAlert:withMessage:]
+ -[TSCrossPlatformSourceAuthFlow didProcessDCTCode]
+ -[TSCrossPlatformSourceAuthFlow initWithCode:]
+ -[TSCrossPlatformSourceAuthFlow setDidProcessDCTCode:]
+ -[TSCrossPlatformSourceAuthFlow viewControllerDidComplete:]
+ -[TSCrossPlatformSourceTransferFlow _prepareDisplayItems:withPlanItems:]
+ -[TSCrossPlatformSourceTransferFlow init:]
+ -[TSCrossPlatformSourceTransferFlow isFromDataTransferSession]
+ -[TSCrossPlatformSourceTransferFlow setIsFromDataTransferSession:]
+ -[TSCrossPlatformTargetAuthFlow backButtonClicked:]
+ -[TSCrossPlatformTargetAuthFlow deactiveCrossPlatformTransport]
+ -[TSCrossPlatformTargetAuthFlow init]
+ -[TSCrossPlatformTargetAuthFlow userDidTapCancel]
+ -[TSCrossPlatformTargetTransferFlow _showCancelAlert:withMessage:]
+ -[TSCrossPlatformTargetTransferFlow handleCrossplatformSessionResponse:completion:]
+ -[TSCrossPlatformTargetTransferFlow init]
+ -[TSCrossPlatformTargetTransferFlow selectedPlans]
+ -[TSCrossPlatformTargetTransferFlow setSelectedPlans:]
+ -[TSCrossPlatformTargetTransferFlow transferEventUpdate:]
+ -[TSDeviceInfoCell initWithStyle:reuseIdentifier:]
+ -[TSDeviceInfoCell layoutSubviews]
+ -[TSDeviceInfoViewController .cxx_destruct]
+ -[TSDeviceInfoViewController _canShowWhileLocked]
+ -[TSDeviceInfoViewController _cancelButtonTapped]
+ -[TSDeviceInfoViewController _doneButtonTapped]
+ -[TSDeviceInfoViewController _shareIdentityTapped]
+ -[TSDeviceInfoViewController delegate]
+ -[TSDeviceInfoViewController heightAnchor]
+ -[TSDeviceInfoViewController initWithOptions:]
+ -[TSDeviceInfoViewController numberOfSectionsInTableView:]
+ -[TSDeviceInfoViewController setDelegate:]
+ -[TSDeviceInfoViewController setHeightAnchor:]
+ -[TSDeviceInfoViewController tableView:cellForRowAtIndexPath:]
+ -[TSDeviceInfoViewController tableView:cellForRowAtIndexPath:].cold.1
+ -[TSDeviceInfoViewController tableView:heightForRowAtIndexPath:]
+ -[TSDeviceInfoViewController tableView:numberOfRowsInSection:]
+ -[TSDeviceInfoViewController tableView:viewForHeaderInSection:]
+ -[TSDeviceInfoViewController viewDidLayoutSubviews]
+ -[TSDeviceInfoViewController viewDidLoad]
+ -[TSEnableTableViewController .cxx_destruct]
+ -[TSEnableTableViewController _areAllInstallingPlansBeEnabled]
+ -[TSEnableTableViewController _doneButtonTapped]
+ -[TSEnableTableViewController _getTraveleSIMStateWithCompletion:]
+ -[TSEnableTableViewController _maybeDismissSelf]
+ -[TSEnableTableViewController _prepareForEnablingItem:]
+ -[TSEnableTableViewController _prepareForEnablingItem:].cold.1
+ -[TSEnableTableViewController _prepareForEnablingItem:].cold.2
+ -[TSEnableTableViewController _prepareForInstallingItems:]
+ -[TSEnableTableViewController _refreshContinueButton]
+ -[TSEnableTableViewController _refreshTableView]
+ -[TSEnableTableViewController _skipButtonTapped]
+ -[TSEnableTableViewController _updateEnablePlanItems]
+ -[TSEnableTableViewController allPlans]
+ -[TSEnableTableViewController animating]
+ -[TSEnableTableViewController cachedButtons]
+ -[TSEnableTableViewController canBeShownFromSuspendedState]
+ -[TSEnableTableViewController customizeSpinner]
+ -[TSEnableTableViewController delegate]
+ -[TSEnableTableViewController enablingIccid]
+ -[TSEnableTableViewController initWithEnablingPlanInfo:]
+ -[TSEnableTableViewController initWithInfos:]
+ -[TSEnableTableViewController installInfos]
+ -[TSEnableTableViewController needShow]
+ -[TSEnableTableViewController originalEnabledPlans]
+ -[TSEnableTableViewController prepare:]
+ -[TSEnableTableViewController selectedItems]
+ -[TSEnableTableViewController setAllPlans:]
+ -[TSEnableTableViewController setAnimating:]
+ -[TSEnableTableViewController setCachedButtons:]
+ -[TSEnableTableViewController setDelegate:]
+ -[TSEnableTableViewController setEnablingIccid:]
+ -[TSEnableTableViewController setInstallInfos:]
+ -[TSEnableTableViewController setNeedShow:]
+ -[TSEnableTableViewController setOriginalEnabledPlans:]
+ -[TSEnableTableViewController setSelectedItems:]
+ -[TSEnableTableViewController setSpinner:]
+ -[TSEnableTableViewController setSpinnerContainer:]
+ -[TSEnableTableViewController spinnerContainer]
+ -[TSEnableTableViewController spinner]
+ -[TSEnableTableViewController viewDidLayoutSubviews]
+ -[TSEnableTableViewController viewDidLoad]
+ -[TSEnableTableViewController viewWillAppear:]
+ -[TSEnableTableViewController(UITableViewDataSource) numberOfSectionsInTableView:]
+ -[TSEnableTableViewController(UITableViewDataSource) selectRowAtIndexPath:animated:scrollPosition:]
+ -[TSEnableTableViewController(UITableViewDataSource) tableView:cellForRowAtIndexPath:]
+ -[TSEnableTableViewController(UITableViewDataSource) tableView:numberOfRowsInSection:]
+ -[TSEnableTableViewController(UITableViewDelegate) tableView:didDeselectRowAtIndexPath:]
+ -[TSEnableTableViewController(UITableViewDelegate) tableView:didSelectRowAtIndexPath:]
+ -[TSIDSTransferFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:]
+ -[TSIDSTransferFlow selectedTransferPlansCount]
+ -[TSIDSTransferFlow setSelectedTransferPlansCount:]
+ -[TSIdentityShareFlow .cxx_destruct]
+ -[TSIdentityShareFlow cancelButton]
+ -[TSIdentityShareFlow firstViewController:]
+ -[TSIdentityShareFlow firstViewController]
+ -[TSIdentityShareFlow initWithOptions:]
+ -[TSIdentityShareFlow init]
+ -[TSIdentityShareFlow isDeviceInfo]
+ -[TSIdentityShareFlow nextViewControllerFrom:]
+ -[TSIdentityShareFlow options]
+ -[TSIdentityShareFlow setCancelButton:]
+ -[TSIdentityShareFlow setIsDeviceInfo:]
+ -[TSIdentityShareFlow setOptions:]
+ -[TSIdentityShareViewController .cxx_destruct]
+ -[TSIdentityShareViewController _canShowWhileLocked]
+ -[TSIdentityShareViewController _doneButtonTapped]
+ -[TSIdentityShareViewController _userDidTapCancel]
+ -[TSIdentityShareViewController delegate]
+ -[TSIdentityShareViewController details]
+ -[TSIdentityShareViewController detailtitle]
+ -[TSIdentityShareViewController init]
+ -[TSIdentityShareViewController setDelegate:]
+ -[TSIdentityShareViewController setDetails:]
+ -[TSIdentityShareViewController setDetailtitle:]
+ -[TSIdentityShareViewController viewDidLoad]
+ -[TSLowDataModeConfigViewController .cxx_destruct]
+ -[TSLowDataModeConfigViewController _cancelButtonTapped]
+ -[TSLowDataModeConfigViewController _continueButtonTapped]
+ -[TSLowDataModeConfigViewController _continueButtonTapped].cold.1
+ -[TSLowDataModeConfigViewController _learnMoreButtonTapped]
+ -[TSLowDataModeConfigViewController _sendTravelEventMetricForPlan:useLDM:]
+ -[TSLowDataModeConfigViewController _sendTravelEventMetricForPlan:useLDM:].cold.1
+ -[TSLowDataModeConfigViewController _setUpButtons]
+ -[TSLowDataModeConfigViewController _setUpLearnMoreLink]
+ -[TSLowDataModeConfigViewController delegate]
+ -[TSLowDataModeConfigViewController initWithPlans:]
+ -[TSLowDataModeConfigViewController init]
+ -[TSLowDataModeConfigViewController isShown]
+ -[TSLowDataModeConfigViewController prepare:]
+ -[TSLowDataModeConfigViewController setDelegate:]
+ -[TSLowDataModeConfigViewController setIsShown:]
+ -[TSLowDataModeConfigViewController viewDidLoad]
+ -[TSManagedDeviceInstallFlow ctClient]
+ -[TSManagedDeviceInstallFlow setCtClient:]
+ -[TSMidOperationFailureViewController initShowErrorOnSourceWithPlanIdentifier:]
+ -[TSMidOperationFailureViewController initWithPlanItemError:updatePlanItem:withBackButton:forCarrier:withCarrierErrorCode:isEmbeddedInResultView:]
+ -[TSMidOperationFailureViewController initWithPlans:]
+ -[TSMidOperationFailureViewController(TSSetupFlowItem) prepare:]
+ -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:]
+ -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:].cold.1
+ -[TSNavigationBarSpinnerManager stopSpinnerInNavigationItem:withIdentifier:].cold.1
+ -[TSNoPlanForTransferViewController _otherButtonTapped]
+ -[TSNoPlanForTransferViewController _turnOnLocationServicesTapped]
+ -[TSNoPlanForTransferViewController initWithPlans:]
+ -[TSNoPlanForTransferViewController plans]
+ -[TSNoPlanForTransferViewController setPlans:]
+ -[TSNoPlanForTransferViewController(UITableViewDataSource) _isAnyPlanRequireLocationService]
+ -[TSNoPlanForTransferViewController(UITableViewDataSource) _isAnyPlanWithMismatchedActivationPolicy]
+ -[TSNoPlanForTransferViewController(UITableViewDataSource) tableView:cellForRowAtIndexPath:]
+ -[TSNoPlanForTransferViewController(UITableViewDataSource) tableView:numberOfRowsInSection:]
+ -[TSNoPlanForTransferViewController(UITableViewDataSource) tableView:viewForFooterInSection:]
+ -[TSPRXIdentityShareViewController .cxx_destruct]
+ -[TSPRXIdentityShareViewController NFCTransferStatus]
+ -[TSPRXIdentityShareViewController _canShowWhileLocked]
+ -[TSPRXIdentityShareViewController _createPKGlyphView]
+ -[TSPRXIdentityShareViewController _failIdentityShare]
+ -[TSPRXIdentityShareViewController _maybeFlowCompleted:]
+ -[TSPRXIdentityShareViewController _maybeFlowCompleted:].cold.1
+ -[TSPRXIdentityShareViewController _reloadScreen]
+ -[TSPRXIdentityShareViewController _startNFCIdentityShare]
+ -[TSPRXIdentityShareViewController _startNFCIdentityShare].cold.1
+ -[TSPRXIdentityShareViewController _startSystemMonitor]
+ -[TSPRXIdentityShareViewController _stopNFCIdentityShare]
+ -[TSPRXIdentityShareViewController _stopNFCIdentityShare].cold.1
+ -[TSPRXIdentityShareViewController _stopSystemMonitor]
+ -[TSPRXIdentityShareViewController _successIdentityShare]
+ -[TSPRXIdentityShareViewController _unlockScreen]
+ -[TSPRXIdentityShareViewController _unlockScreen].cold.1
+ -[TSPRXIdentityShareViewController _unregisterLockState]
+ -[TSPRXIdentityShareViewController cancelAction]
+ -[TSPRXIdentityShareViewController ctClient]
+ -[TSPRXIdentityShareViewController dealloc]
+ -[TSPRXIdentityShareViewController delegate]
+ -[TSPRXIdentityShareViewController init]
+ -[TSPRXIdentityShareViewController isNFCDataSuccessTransfer]
+ -[TSPRXIdentityShareViewController nfcAnimationView]
+ -[TSPRXIdentityShareViewController retryAction]
+ -[TSPRXIdentityShareViewController setCancelAction:]
+ -[TSPRXIdentityShareViewController setCtClient:]
+ -[TSPRXIdentityShareViewController setDelegate:]
+ -[TSPRXIdentityShareViewController setIsNFCDataSuccessTransfer:]
+ -[TSPRXIdentityShareViewController setNFCTransferStatus:]
+ -[TSPRXIdentityShareViewController setNfcAnimationView:]
+ -[TSPRXIdentityShareViewController setRetryAction:]
+ -[TSPRXIdentityShareViewController setSystemMonitor:]
+ -[TSPRXIdentityShareViewController setUnlockAction:]
+ -[TSPRXIdentityShareViewController systemMonitor]
+ -[TSPRXIdentityShareViewController unlockAction]
+ -[TSPRXIdentityShareViewController viewDidAppear:]
+ -[TSPRXIdentityShareViewController viewDidLoad]
+ -[TSPRXReconnectWaitingViewController initWithTitle:subtitle:]
+ -[TSPRXSIMTransferCompleteViewController _createPKGlyphView]
+ -[TSPRXSIMTransferCompleteViewController _getSubtitleWhenSyncWithTarget:selectedPlansCount:selectedPlansFailedTransferCount:]
+ -[TSPRXSIMTransferCompleteViewController _getTitleWhenSyncWithTarget:selectedPlansCount:selectedPlansFailedTransferCount:]
+ -[TSPRXSIMTransferCompleteViewController _updateLayoutConstraint]
+ -[TSPRXSIMTransferCompleteViewController doneAction]
+ -[TSPRXSIMTransferCompleteViewController glyphView]
+ -[TSPRXSIMTransferCompleteViewController initWithSelectedPlansCount:selectedPlansFailedTransferCount:isDisembarkUIRequired:]
+ -[TSPRXSIMTransferCompleteViewController initWithoutTargetSyncAndSelectedPlansCount:]
+ -[TSPRXSIMTransferCompleteViewController isDisembarkUIRequired]
+ -[TSPRXSIMTransferCompleteViewController isSyncWithTargetResults]
+ -[TSPRXSIMTransferCompleteViewController selectedPlansCount]
+ -[TSPRXSIMTransferCompleteViewController selectedPlansFailedTransferCount]
+ -[TSPRXSIMTransferCompleteViewController setDoneAction:]
+ -[TSPRXSIMTransferCompleteViewController setGlyphView:]
+ -[TSPRXSIMTransferCompleteViewController setIsDisembarkUIRequired:]
+ -[TSPRXSIMTransferCompleteViewController setIsSyncWithTargetResults:]
+ -[TSPRXSIMTransferCompleteViewController setSelectedPlansCount:]
+ -[TSPRXSIMTransferCompleteViewController setSelectedPlansFailedTransferCount:]
+ -[TSPRXSIMTransferCompleteViewController setTriangleImageView:]
+ -[TSPRXSIMTransferCompleteViewController triangleImageView]
+ -[TSPRXSIMTransferCompleteViewController viewDidLoad]
+ -[TSPostMigrationFlow .cxx_destruct]
+ -[TSPostMigrationFlow _createTargetProxFlowVC]
+ -[TSPostMigrationFlow _createTransferCloudFlowVC]
+ -[TSPostMigrationFlow _createTransferFlowVC]
+ -[TSPostMigrationFlow _subFlowVcWithReconnectionCredentials:]
+ -[TSPostMigrationFlow ctClient]
+ -[TSPostMigrationFlow firstViewController:]
+ -[TSPostMigrationFlow initWithSession:sourceOSVersion:proximitySetupState:transferablePlanOnSource:]
+ -[TSPostMigrationFlow isProxFlowShown]
+ -[TSPostMigrationFlow nextViewControllerFrom:]
+ -[TSPostMigrationFlow prepareViewController:completion:]
+ -[TSPostMigrationFlow proximitySetupState]
+ -[TSPostMigrationFlow session]
+ -[TSPostMigrationFlow setCtClient:]
+ -[TSPostMigrationFlow setIsProxFlowShown:]
+ -[TSPostMigrationFlow setProximitySetupState:]
+ -[TSPostMigrationFlow setSession:]
+ -[TSPostMigrationFlow setSourceOSVersion:]
+ -[TSPostMigrationFlow setTransferablePlanOnSource:]
+ -[TSPostMigrationFlow sourceOSVersion]
+ -[TSPostMigrationFlow transferablePlanOnSource]
+ -[TSProximitySourceTransferFlow _decodeTransferStatus:]
+ -[TSProximitySourceTransferFlow _handleTransferResults:]
+ -[TSProximitySourceTransferFlow _handleTransferUICapability:]
+ -[TSProximitySourceTransferFlow _registerMessages]
+ -[TSProximitySourceTransferFlow _registerMessages].cold.1
+ -[TSProximitySourceTransferFlow _timerFired]
+ -[TSProximitySourceTransferFlow _timerFired].cold.1
+ -[TSProximitySourceTransferFlow _updateTransferStatus:]
+ -[TSProximitySourceTransferFlow areAllPlansTransferedOut]
+ -[TSProximitySourceTransferFlow isDeviceIdentifierPresent]
+ -[TSProximitySourceTransferFlow isPreSharedKeyPresent]
+ -[TSProximitySourceTransferFlow numSelectedPlansNotTransferredOut]
+ -[TSProximitySourceTransferFlow peerDeviceInfo]
+ -[TSProximitySourceTransferFlow selectedTransferPlansCount]
+ -[TSProximitySourceTransferFlow session]
+ -[TSProximitySourceTransferFlow setAreAllPlansTransferedOut:]
+ -[TSProximitySourceTransferFlow setIsDeviceIdentifierPresent:]
+ -[TSProximitySourceTransferFlow setIsPreSharedKeyPresent:]
+ -[TSProximitySourceTransferFlow setNumSelectedPlansNotTransferredOut:]
+ -[TSProximitySourceTransferFlow setPeerDeviceInfo:]
+ -[TSProximitySourceTransferFlow setSelectedTransferPlansCount:]
+ -[TSProximitySourceTransferFlow setSession:]
+ -[TSProximitySourceTransferFlow setSupportsSyncTransferResults:]
+ -[TSProximitySourceTransferFlow setTimer:]
+ -[TSProximitySourceTransferFlow supportsSyncTransferResults]
+ -[TSProximitySourceTransferFlow timer]
+ -[TSProximityTargetTransferFlow _createTransferSubFlowVcWithSession:isPostmigrationFlow:]
+ -[TSProximityTargetTransferFlow _createTransferSubFlowVcWithSession:isPostmigrationFlow:].cold.1
+ -[TSProximityTargetTransferFlow _maybeSubmitAutoReconnectionDetails]
+ -[TSProximityTargetTransferFlow initWithTransferBackPlan:isPostMigrationFlow:]
+ -[TSProximityTargetTransferFlow isAuthenticationCompleted]
+ -[TSProximityTargetTransferFlow isPostMigrationFlow]
+ -[TSProximityTargetTransferFlow setIsAuthenticationCompleted:]
+ -[TSProximityTargetTransferFlow setIsPostMigrationFlow:]
+ -[TSProximityTargetTransferFlow setWaitingStartTime:]
+ -[TSProximityTargetTransferFlow waitingStartTime]
+ -[TSRoamingEducationViewController .cxx_destruct]
+ -[TSRoamingEducationViewController _cancelButtonTapped]
+ -[TSRoamingEducationViewController _continueButtonTapped]
+ -[TSRoamingEducationViewController _learnMoreButtonTapped]
+ -[TSRoamingEducationViewController _sendTravelEventMetricForRoaming:]
+ -[TSRoamingEducationViewController _sendTravelEventMetricForRoaming:].cold.1
+ -[TSRoamingEducationViewController _setUpButtons]
+ -[TSRoamingEducationViewController _setUpLearnMoreLink]
+ -[TSRoamingEducationViewController delegate]
+ -[TSRoamingEducationViewController init]
+ -[TSRoamingEducationViewController setDelegate:]
+ -[TSRoamingEducationViewController setTappedLearnMore:]
+ -[TSRoamingEducationViewController tappedLearnMore]
+ -[TSRoamingEducationViewController viewDidLoad]
+ -[TSSIMSetupFlow _maybeClearSubFlowViewController:]
+ -[TSSIMSetupFlow _maybeSetNavigationController:]
+ -[TSSIMSetupFlow addSubFlowViewController:]
+ -[TSSIMSetupFlow firstViewControllerForDisplay]
+ -[TSSIMSetupFlow handleStartOverWithEntryPoint:navigationController:completion:]
+ -[TSSIMSetupFlow maybePrepareNextDisplayViewController:completion:]
+ -[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:].cold.1
+ -[TSSIMSetupFlow rootFlow]
+ -[TSSIMSetupFlow rootFlow].cold.1
+ -[TSSIMSetupFlow rootViewController].cold.1
+ -[TSSIMSetupFlow setSubFlowViewControllers:]
+ -[TSSIMSetupFlow subFlowViewControllers]
+ -[TSSIMSetupPublicApiInstallFlow _isFollowUpInstall]
+ -[TSSIMSetupPublicApiInstallFlow _validCarrierName]
+ -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:isDTOEvaluationFailed:]
+ -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:isDTOEvaluationFailed:].cold.1
+ -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:isDTOEvaluationFailed:].cold.2
+ -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:isDTOEvaluationFailed:].cold.3
+ -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:isDTOEvaluationFailed:].cold.4
+ -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:isDTOEvaluationFailed:].cold.5
+ -[TSSecureIntentGestureViewController _updateAuthenticationStatus:isDTOEvaluationFailed:]
+ -[TSSecureIntentGestureViewController descriptors]
+ -[TSSecureIntentGestureViewController evaluateDtoPolicy:]
+ -[TSSecureIntentGestureViewController formatedDescriptor]
+ -[TSSecureIntentGestureViewController initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:]
+ -[TSSecureIntentGestureViewController isDtoEvaluationRequired]
+ -[TSSecureIntentGestureViewController isDtoEvaluationSucceeded]
+ -[TSSecureIntentGestureViewController isSecureIntentRequired]
+ -[TSSecureIntentGestureViewController isSecureIntentSucceeded]
+ -[TSSecureIntentGestureViewController prepare:]
+ -[TSSecureIntentGestureViewController setDescriptors:]
+ -[TSSecureIntentGestureViewController setFormatedDescriptor:]
+ -[TSSecureIntentGestureViewController setIsDtoEvaluationRequired:]
+ -[TSSecureIntentGestureViewController setIsDtoEvaluationSucceeded:]
+ -[TSSecureIntentGestureViewController setIsSecureIntentRequired:]
+ -[TSSecureIntentGestureViewController setIsSecureIntentSucceeded:]
+ -[TSSinglePlanTransferViewController _maybeAutoInstallPendingPlan]
+ -[TSSinglePlanTransferViewController ctClient]
+ -[TSSinglePlanTransferViewController initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isShowingFilteredPlans:]
+ -[TSSinglePlanTransferViewController initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isStandaloneProximityFlow:transferBackPhoneNumber:isShowingFilteredPlans:]
+ -[TSSinglePlanTransferViewController isSkipButtonTapped]
+ -[TSSinglePlanTransferViewController selectedPlan]
+ -[TSSinglePlanTransferViewController setCtClient:]
+ -[TSSinglePlanTransferViewController setIsSkipButtonTapped:]
+ -[TSSinglePlanTransferViewController viewWillAppear:]
+ -[TSSourceAutoReconnectTransferFlow .cxx_destruct]
+ -[TSSourceAutoReconnectTransferFlow ctClient]
+ -[TSSourceAutoReconnectTransferFlow firstViewController:]
+ -[TSSourceAutoReconnectTransferFlow init]
+ -[TSSourceAutoReconnectTransferFlow isTransferCompleted]
+ -[TSSourceAutoReconnectTransferFlow nextViewControllerFrom:]
+ -[TSSourceAutoReconnectTransferFlow proxSetupAuthEventUpdate:]
+ -[TSSourceAutoReconnectTransferFlow setCtClient:]
+ -[TSSourceAutoReconnectTransferFlow setIsTransferCompleted:]
+ -[TSSourceAutoReconnectTransferFlow transferEventUpdate:]
+ -[TSSourceAutoReconnectTransferredViewController .cxx_destruct]
+ -[TSSourceAutoReconnectTransferredViewController _continueButtonTapped]
+ -[TSSourceAutoReconnectTransferredViewController delegate]
+ -[TSSourceAutoReconnectTransferredViewController init]
+ -[TSSourceAutoReconnectTransferredViewController setDelegate:]
+ -[TSSourceAutoReconnectTransferredViewController viewDidLoad]
+ -[TSSourceAutoReconnectWaitingViewController .cxx_destruct]
+ -[TSSourceAutoReconnectWaitingViewController _skipButtonTapped:]
+ -[TSSourceAutoReconnectWaitingViewController delegate]
+ -[TSSourceAutoReconnectWaitingViewController init]
+ -[TSSourceAutoReconnectWaitingViewController setDelegate:]
+ -[TSSourceAutoReconnectWaitingViewController setSkipButton:]
+ -[TSSourceAutoReconnectWaitingViewController skipButton]
+ -[TSSourceAutoReconnectWaitingViewController viewDidLoad]
+ -[TSSubFlowViewController initWithFlow:navigationController:delegate:]
+ -[TSSubFlowViewController initWithOptions:navigationController:delegate:]
+ -[TSSubFlowViewController setDelegate:].cold.1
+ -[TSSubFlowViewController simSetupFlowCompleted:].cold.2
+ -[TSSubFlowViewController viewDidAppear:]
+ -[TSTargetReconnectWaitingViewController .cxx_destruct]
+ -[TSTargetReconnectWaitingViewController _skipButtonTapped:]
+ -[TSTargetReconnectWaitingViewController connectionStarted]
+ -[TSTargetReconnectWaitingViewController delegate]
+ -[TSTargetReconnectWaitingViewController init]
+ -[TSTargetReconnectWaitingViewController isStartOverRequiredOnBackButtonTapped]
+ -[TSTargetReconnectWaitingViewController setDelegate:]
+ -[TSTargetReconnectWaitingViewController setSkipButton:]
+ -[TSTargetReconnectWaitingViewController setWaitingStartTime:]
+ -[TSTargetReconnectWaitingViewController skipButton]
+ -[TSTargetReconnectWaitingViewController submitAutoReconnectionDetails]
+ -[TSTargetReconnectWaitingViewController viewDidLoad]
+ -[TSTargetReconnectWaitingViewController waitingStartTime]
+ -[TSTransferCloudFlow _firstViewController]
+ -[TSTransferCloudFlow firstViewController].cold.1
+ -[TSTransferCloudFlow initWithProximitySetupState:proxPlansFiltered:]
+ -[TSTransferCloudFlowModel isFlexPolicyOn]
+ -[TSTransferCloudFlowModel setIsFlexPolicyOn:]
+ -[TSTransferFlow _maybeClearFirstViewControllerCallback]
+ -[TSTransferFlow firstViewController].cold.1
+ -[TSTransferFlow initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:]
+ -[TSTransferFlow isPostMigrationFlow]
+ -[TSTransferFlow isUsingPreSharedKey]
+ -[TSTransferFlow setIsPostMigrationFlow:]
+ -[TSTransferFlow setIsUsingPreSharedKey:]
+ -[TSTransferFlow setSourceOSVersion:]
+ -[TSTransferFlow sourceOSVersion]
+ -[TSTransferFlowModel arePlansAvailable:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]
+ -[TSTransferFlowModel bootstrap:isUsingPreSharedKey:completion:]
+ -[TSTransferFlowModel establishReconnectionCredentials:completion:]
+ -[TSTransferFlowModel isFlexPolicyOn]
+ -[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]
+ -[TSTransferFlowModel setIsFlexPolicyOn:]
+ -[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:]
+ -[TSTransferListViewController _installMultipleSelectedPlans]
+ -[TSTransferListViewController _installMultipleSelectedPlans].cold.1
+ -[TSTransferListViewController _installMultipleSelectedPlans].cold.2
+ -[TSTransferListViewController _isAnyPlanRequireLocationService]
+ -[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:].cold.1
+ -[TSTransferListViewController _startInstallMultiplePlans:transferPlans:andCarrierSetupItems:]
+ -[TSTransferListViewController _viewWillAppear]
+ -[TSTransferListViewController allPlansInstallComplete]
+ -[TSTransferListViewController ctClient]
+ -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:allowsMultiSelection:]
+ -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:]
+ -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:allowsMultiSelection:]
+ -[TSTransferListViewController planError]
+ -[TSTransferListViewController planList]
+ -[TSTransferListViewController selectedPlans]
+ -[TSTransferListViewController setCtClient:]
+ -[TSTransferListViewController setPlanError:]
+ -[TSTransferListViewController setPlanList:]
+ -[TSTransferListViewController setSelectedPlans:]
+ -[TSTransferOneTimeCodeViewController _installStateChanged:]
+ -[TSTransferOneTimeCodeViewController _startObserver]
+ -[TSTravelBuddyViewController .cxx_destruct]
+ -[TSTravelBuddyViewController _continueButtonTapped:]
+ -[TSTravelBuddyViewController _continueButtonTapped:].cold.1
+ -[TSTravelBuddyViewController _continueButtonTapped:].cold.2
+ -[TSTravelBuddyViewController _dismissViewController]
+ -[TSTravelBuddyViewController _getDetailsTextWithIccid:]
+ -[TSTravelBuddyViewController _getDetailsTextWithIccid:].cold.1
+ -[TSTravelBuddyViewController _getPlanItemsToLimitService:]
+ -[TSTravelBuddyViewController _getTraveleSIMStateWithCompletion:]
+ -[TSTravelBuddyViewController _heightAnchorConstant]
+ -[TSTravelBuddyViewController _laterButtonTapped:]
+ -[TSTravelBuddyViewController _maybeUpdateHomeIccid:homeIccid:]
+ -[TSTravelBuddyViewController _refreshTableView]
+ -[TSTravelBuddyViewController _setTravelIccidInfo:]
+ -[TSTravelBuddyViewController _shouldPlanBeRegisteredForIMessage:]
+ -[TSTravelBuddyViewController _shouldPlanBeRegisteredForIMessage:].cold.1
+ -[TSTravelBuddyViewController _shouldPlanBeRegisteredForIMessage:].cold.2
+ -[TSTravelBuddyViewController animating]
+ -[TSTravelBuddyViewController backToCurrentTopPane]
+ -[TSTravelBuddyViewController cachedButtons]
+ -[TSTravelBuddyViewController customizeSpinner]
+ -[TSTravelBuddyViewController delegate]
+ -[TSTravelBuddyViewController didUserClickContinue]
+ -[TSTravelBuddyViewController initWithIccids:homeIccid:voiceIccid:postArrivalInstallation:]
+ -[TSTravelBuddyViewController initWithPlans:homeIccid:]
+ -[TSTravelBuddyViewController isShown]
+ -[TSTravelBuddyViewController numberOfSectionsInTableView:]
+ -[TSTravelBuddyViewController planItems]
+ -[TSTravelBuddyViewController prepare:]
+ -[TSTravelBuddyViewController setAnimating:]
+ -[TSTravelBuddyViewController setCachedButtons:]
+ -[TSTravelBuddyViewController setDelegate:]
+ -[TSTravelBuddyViewController setDidUserClickContinue:]
+ -[TSTravelBuddyViewController setIsShown:]
+ -[TSTravelBuddyViewController setPlanItems:]
+ -[TSTravelBuddyViewController setSpinner:]
+ -[TSTravelBuddyViewController setSpinnerContainer:]
+ -[TSTravelBuddyViewController setTravelOnlySelected:]
+ -[TSTravelBuddyViewController spinnerContainer]
+ -[TSTravelBuddyViewController spinner]
+ -[TSTravelBuddyViewController subscriptionInfoDidChange]
+ -[TSTravelBuddyViewController tableView:cellForRowAtIndexPath:]
+ -[TSTravelBuddyViewController tableView:didSelectRowAtIndexPath:]
+ -[TSTravelBuddyViewController tableView:heightForFooterInSection:]
+ -[TSTravelBuddyViewController tableView:heightForHeaderInSection:]
+ -[TSTravelBuddyViewController tableView:numberOfRowsInSection:]
+ -[TSTravelBuddyViewController tableView:viewForHeaderInSection:]
+ -[TSTravelBuddyViewController travelOnlySelected]
+ -[TSTravelBuddyViewController viewDidLoad]
+ -[TSTravelEducationFlow _getSFSafariViewControllerWithURL:]
+ -[TSTravelEducationIntroViewController _decodeBase64EncodedString:]
+ -[TSTravelEducationIntroViewController roamingInfo]
+ -[TSTravelEducationIntroViewController setRoamingInfo:]
+ -[TSTravelModeFlow .cxx_destruct]
+ -[TSTravelModeFlow _getCellularPlanItemForTravelSIM]
+ -[TSTravelModeFlow firstViewController:]
+ -[TSTravelModeFlow firstViewController]
+ -[TSTravelModeFlow firstViewController].cold.1
+ -[TSTravelModeFlow initWithOptions:]
+ -[TSTravelModeFlow nextViewControllerFrom:]
+ -[TSTravelModeFlow nextViewControllerFrom:].cold.1
+ -[TSTravelModeFlow options]
+ -[TSTravelModeFlow setOptions:]
+ -[TSTravelModeFlow setTravelSIM:]
+ -[TSTravelModeFlow travelSIM]
+ -[TSTravelModeIntroViewController .cxx_destruct]
+ -[TSTravelModeIntroViewController _cancelButtonTapped]
+ -[TSTravelModeIntroViewController _continueButtonTapped]
+ -[TSTravelModeIntroViewController _continueButtonTapped].cold.1
+ -[TSTravelModeIntroViewController _getCarrierNameForDefaultDataSub]
+ -[TSTravelModeIntroViewController _learnMoreButtonTapped]
+ -[TSTravelModeIntroViewController _setUpButtons]
+ -[TSTravelModeIntroViewController _setUpLearnMoreLink]
+ -[TSTravelModeIntroViewController _setUpTableView]
+ -[TSTravelModeIntroViewController delegate]
+ -[TSTravelModeIntroViewController footer]
+ -[TSTravelModeIntroViewController heightAnchor]
+ -[TSTravelModeIntroViewController initWithOptions:extractionSource:]
+ -[TSTravelModeIntroViewController numberOfSectionsInTableView:]
+ -[TSTravelModeIntroViewController setDelegate:]
+ -[TSTravelModeIntroViewController setFooter:]
+ -[TSTravelModeIntroViewController setHeightAnchor:]
+ -[TSTravelModeIntroViewController tableView:cellForRowAtIndexPath:]
+ -[TSTravelModeIntroViewController tableView:numberOfRowsInSection:]
+ -[TSTravelModeIntroViewController tableView:willDisplayHeaderView:forSection:]
+ -[TSTravelModeIntroViewController viewDidLoad]
+ -[TSTravelSimCapabilitySelectionViewController .cxx_destruct]
+ -[TSTravelSimCapabilitySelectionViewController _continueButtonTapped:]
+ -[TSTravelSimCapabilitySelectionViewController _heightAnchorConstant]
+ -[TSTravelSimCapabilitySelectionViewController _refreshTableView]
+ -[TSTravelSimCapabilitySelectionViewController delegate]
+ -[TSTravelSimCapabilitySelectionViewController initWithPlans:isSelectedAsTravelSIM:]
+ -[TSTravelSimCapabilitySelectionViewController isDataOnlySelected]
+ -[TSTravelSimCapabilitySelectionViewController numberOfSectionsInTableView:]
+ -[TSTravelSimCapabilitySelectionViewController prepare:]
+ -[TSTravelSimCapabilitySelectionViewController setDelegate:]
+ -[TSTravelSimCapabilitySelectionViewController setIsDataOnlySelected:]
+ -[TSTravelSimCapabilitySelectionViewController tableView:cellForRowAtIndexPath:]
+ -[TSTravelSimCapabilitySelectionViewController tableView:didSelectRowAtIndexPath:]
+ -[TSTravelSimCapabilitySelectionViewController tableView:heightForFooterInSection:]
+ -[TSTravelSimCapabilitySelectionViewController tableView:heightForHeaderInSection:]
+ -[TSTravelSimCapabilitySelectionViewController tableView:numberOfRowsInSection:]
+ -[TSTravelSimCapabilitySelectionViewController tableView:viewForHeaderInSection:]
+ -[TSTravelSimCapabilitySelectionViewController viewDidLoad]
+ -[TSTravelSimTypeSelectionViewController .cxx_destruct]
+ -[TSTravelSimTypeSelectionViewController _continueButtonTapped:]
+ -[TSTravelSimTypeSelectionViewController _heightAnchorConstant]
+ -[TSTravelSimTypeSelectionViewController _refreshTableView]
+ -[TSTravelSimTypeSelectionViewController delegate]
+ -[TSTravelSimTypeSelectionViewController initWithPlans:]
+ -[TSTravelSimTypeSelectionViewController isSelectedAsTravelSIM]
+ -[TSTravelSimTypeSelectionViewController isShown]
+ -[TSTravelSimTypeSelectionViewController numberOfSectionsInTableView:]
+ -[TSTravelSimTypeSelectionViewController prepare:]
+ -[TSTravelSimTypeSelectionViewController setDelegate:]
+ -[TSTravelSimTypeSelectionViewController setIsSelectedAsTravelSIM:]
+ -[TSTravelSimTypeSelectionViewController setIsShown:]
+ -[TSTravelSimTypeSelectionViewController tableView:cellForRowAtIndexPath:]
+ -[TSTravelSimTypeSelectionViewController tableView:didSelectRowAtIndexPath:]
+ -[TSTravelSimTypeSelectionViewController tableView:heightForFooterInSection:]
+ -[TSTravelSimTypeSelectionViewController tableView:heightForHeaderInSection:]
+ -[TSTravelSimTypeSelectionViewController tableView:numberOfRowsInSection:]
+ -[TSTravelSimTypeSelectionViewController tableView:viewForHeaderInSection:]
+ -[TSTravelSimTypeSelectionViewController viewDidLoad]
+ -[TSWebsheetViewController _cancelButtonTapped]
+ -[TSWebsheetViewController _dismissDueToLoadFailure]
+ -[TSWebsheetViewController _showFailureAlert]
+ -[TSWebsheetViewController initWithURL:postdata:]
+ -[TSWebsheetViewController prepare:]
+ -[UITableViewCell(SS) defaultConfig]
+ -[UIViewController(Flow) flow]
+ -[UIViewController(SubFlow) subFlowType]
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table129
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table149
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table21
+ GCC_except_table222
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table47
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table66
+ GCC_except_table74
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table82
+ _AudioServicesPlaySystemSoundWithCompletion
+ _CC_SHA256
+ _CTPlanTransferCapabilityAsString
+ _CTPlanTransferStatusActivatedNoPhoneNumber
+ _CTPlanTransferStatusAsString
+ _CTPlanTransferStatusTimeoutInstallOngoing
+ _CTPlanTransferStatusTimeoutInstalledNoService
+ _CTPlanTransferStatusTimeoutNotConsented
+ _DisembarkUILibraryCore.frameworkLibrary
+ _FBSOpenApplicationOptionKeyUnlockDevice
+ _MGGetStringAnswer
+ _OBJC_CLASS_$_CTAutoReconnectionDetails
+ _OBJC_CLASS_$_CTCellularPlanProperties
+ _OBJC_CLASS_$_CTODAPlan
+ _OBJC_CLASS_$_CTPendingPlan
+ _OBJC_CLASS_$_CTServiceDescriptor
+ _OBJC_CLASS_$_CUMessageSession
+ _OBJC_CLASS_$_CrossPlatformManualDetailsViewController
+ _OBJC_CLASS_$_CrossPlatformShowManualDetailsViewController
+ _OBJC_CLASS_$_CrossPlatformTransferIntroViewController
+ _OBJC_CLASS_$_ExitBuddyIconView
+ _OBJC_CLASS_$_FBSOpenApplicationOptions
+ _OBJC_CLASS_$_FBSOpenApplicationService
+ _OBJC_CLASS_$_IDSService
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSNotification
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSSymbolDrawOnEffect
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_OBSetupAssistantSpinnerController
+ _OBJC_CLASS_$_PKGlyphView
+ _OBJC_CLASS_$_SSCardManualEntryViewController
+ _OBJC_CLASS_$_SSCellularPlanScanViewController
+ _OBJC_CLASS_$_SSCellularSetupMultiSIMActivatingViewController
+ _OBJC_CLASS_$_SSCellularSetupMultiSIMConnectingViewController
+ _OBJC_CLASS_$_SSConfirmationCodeViewController
+ _OBJC_CLASS_$_SSCrossPlatformScanViewController
+ _OBJC_CLASS_$_SSInstallPlanInformation
+ _OBJC_CLASS_$_SSLabelPickerViewController
+ _OBJC_CLASS_$_SSLimitedSelectableTableView
+ _OBJC_CLASS_$_SSManualEntryCell
+ _OBJC_CLASS_$_SSMultiSIMResultViewController
+ _OBJC_CLASS_$_SSPRXD2DMigrationDoneViewController
+ _OBJC_CLASS_$_TSBootstrapCrossPlatformTransferFlow
+ _OBJC_CLASS_$_TSDeviceInfoCell
+ _OBJC_CLASS_$_TSDeviceInfoViewController
+ _OBJC_CLASS_$_TSEnableTableViewController
+ _OBJC_CLASS_$_TSIdentityShareFlow
+ _OBJC_CLASS_$_TSIdentityShareViewController
+ _OBJC_CLASS_$_TSLowDataModeConfigViewController
+ _OBJC_CLASS_$_TSPRXIdentityShareViewController
+ _OBJC_CLASS_$_TSPRXReconnectWaitingViewController
+ _OBJC_CLASS_$_TSPostMigrationFlow
+ _OBJC_CLASS_$_TSRoamingEducationViewController
+ _OBJC_CLASS_$_TSSourceAutoReconnectTransferFlow
+ _OBJC_CLASS_$_TSSourceAutoReconnectTransferredViewController
+ _OBJC_CLASS_$_TSSourceAutoReconnectWaitingViewController
+ _OBJC_CLASS_$_TSTargetReconnectWaitingViewController
+ _OBJC_CLASS_$_TSTravelBuddyViewController
+ _OBJC_CLASS_$_TSTravelModeFlow
+ _OBJC_CLASS_$_TSTravelModeIntroViewController
+ _OBJC_CLASS_$_TSTravelSimCapabilitySelectionViewController
+ _OBJC_CLASS_$_TSTravelSimTypeSelectionViewController
+ _OBJC_CLASS_$_UIListContentConfiguration
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._activeTextField
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._animating
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._cachedButtons
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._continueButton
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._dctDelegate
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._delegate
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._keyboardSize
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._spinner
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._spinnerContainer
+ _OBJC_IVAR_$_CrossPlatformManualDetailsViewController._values
+ _OBJC_IVAR_$_CrossPlatformShowManualDetailsViewController._dctInfo
+ _OBJC_IVAR_$_CrossPlatformShowManualDetailsViewController._delegate
+ _OBJC_IVAR_$_CrossPlatformShowManualDetailsViewController._queryParamToTitle
+ _OBJC_IVAR_$_CrossPlatformTransferAuthQRCodeViewController._isCancelButtonTapped
+ _OBJC_IVAR_$_CrossPlatformTransferAuthQRCodeViewController._isOtherButtonTapped
+ _OBJC_IVAR_$_CrossPlatformTransferAuthQRCodeViewController._otherOptionsButton
+ _OBJC_IVAR_$_CrossPlatformTransferIntroViewController._delegate
+ _OBJC_IVAR_$_SSCardManualEntryViewController._delegate
+ _OBJC_IVAR_$_SSCardManualEntryViewController._heightAnchor
+ _OBJC_IVAR_$_SSCardManualEntryViewController._keyboardSize
+ _OBJC_IVAR_$_SSCardManualEntryViewController._nextButton
+ _OBJC_IVAR_$_SSCardManualEntryViewController._tableHeightAnchor
+ _OBJC_IVAR_$_SSCardManualEntryViewController._values
+ _OBJC_IVAR_$_SSCellularPlanScanViewController._confirmationCodeRequired
+ _OBJC_IVAR_$_SSCellularPlanScanViewController._entryPoint
+ _OBJC_IVAR_$_SSCellularPlanScanViewController._fauxCardData
+ _OBJC_IVAR_$_SSCellularPlanScanViewController._transferViaQRCode
+ _OBJC_IVAR_$_SSCellularPlanScanViewController._withBackButton
+ _OBJC_IVAR_$_SSCellularSetupMultiSIMActivatingViewController._delegate
+ _OBJC_IVAR_$_SSCellularSetupMultiSIMActivatingViewController._planStatusDescriptions
+ _OBJC_IVAR_$_SSCellularSetupMultiSIMActivatingViewController._plans
+ _OBJC_IVAR_$_SSCellularSetupMultiSIMConnectingViewController._skip
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._cancelButton
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._carrierName
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._codeTextField
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._confirmationCode
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._continueButton
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._delegate
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._fauxCardData
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._isMidOperation
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._nextButton
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._requireGeneralConsent
+ _OBJC_IVAR_$_SSConfirmationCodeViewController._userConsentResponse
+ _OBJC_IVAR_$_SSCrossPlatformTransferSourceSelectionViewController._fromDataTransferSession
+ _OBJC_IVAR_$_SSCrossPlatformTransferSourceSelectionViewController._laterButton
+ _OBJC_IVAR_$_SSInstallPlanInformation._carrierErrorCode
+ _OBJC_IVAR_$_SSInstallPlanInformation._confirmationCodeViewController
+ _OBJC_IVAR_$_SSInstallPlanInformation._displayPlan
+ _OBJC_IVAR_$_SSInstallPlanInformation._eSIMTravelState
+ _OBJC_IVAR_$_SSInstallPlanInformation._installError
+ _OBJC_IVAR_$_SSInstallPlanInformation._installationEndTime
+ _OBJC_IVAR_$_SSInstallPlanInformation._installationStartTime
+ _OBJC_IVAR_$_SSInstallPlanInformation._isDataOnly
+ _OBJC_IVAR_$_SSInstallPlanInformation._isDisabled
+ _OBJC_IVAR_$_SSInstallPlanInformation._isPreInstalled
+ _OBJC_IVAR_$_SSInstallPlanInformation._isUserInHomeCountry
+ _OBJC_IVAR_$_SSInstallPlanInformation._phoneNumber
+ _OBJC_IVAR_$_SSInstallPlanInformation._planItem
+ _OBJC_IVAR_$_SSInstallPlanInformation._planName
+ _OBJC_IVAR_$_SSInstallPlanInformation._postdata
+ _OBJC_IVAR_$_SSInstallPlanInformation._status
+ _OBJC_IVAR_$_SSInstallPlanInformation._targetIccid
+ _OBJC_IVAR_$_SSInstallPlanInformation._targetIccidHash
+ _OBJC_IVAR_$_SSInstallPlanInformation._useTravelOnly
+ _OBJC_IVAR_$_SSInstallPlanInformation._waitForPhoneNumber
+ _OBJC_IVAR_$_SSInstallPlanInformation._websheetUrl
+ _OBJC_IVAR_$_SSLabelPickerViewController._associatedPlanItem
+ _OBJC_IVAR_$_SSLabelPickerViewController._chosenLabelIndexPath
+ _OBJC_IVAR_$_SSLabelPickerViewController._customLabel
+ _OBJC_IVAR_$_SSLabelPickerViewController._initialLabel
+ _OBJC_IVAR_$_SSLabelPickerViewController._predefinedUserLabels
+ _OBJC_IVAR_$_SSLimitedSelectableTableView._limit
+ _OBJC_IVAR_$_SSLimitedSelectableTableView._viewDelegate
+ _OBJC_IVAR_$_SSManualEntryCell._editableTextField
+ _OBJC_IVAR_$_SSMultiSIMResultViewController._delegate
+ _OBJC_IVAR_$_SSMultiSIMResultViewController._heightAnchor
+ _OBJC_IVAR_$_SSMultiSIMResultViewController._infos
+ _OBJC_IVAR_$_SSPRXD2DMigrationDoneViewController._delegate
+ _OBJC_IVAR_$_SSScanViewController._isEnterManuallyTapped
+ _OBJC_IVAR_$_SSScanViewController._scannedCode
+ _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._isFlexPolicyOn
+ _OBJC_IVAR_$_TSAuthFlow._descriptors
+ _OBJC_IVAR_$_TSAuthFlow._isDtoEvaluationRequired
+ _OBJC_IVAR_$_TSAuthFlow._isSecureIntentRequired
+ _OBJC_IVAR_$_TSBootstrapCrossPlatformTransferFlow._client
+ _OBJC_IVAR_$_TSBootstrapCrossPlatformTransferFlow._dctPrewarmSucceded
+ _OBJC_IVAR_$_TSBootstrapCrossPlatformTransferFlow._firstViewControllerCallback
+ _OBJC_IVAR_$_TSBootstrapCrossPlatformTransferFlow._isSource
+ _OBJC_IVAR_$_TSBootstrapCrossPlatformTransferFlow._preWarmOngoing
+ _OBJC_IVAR_$_TSBootstrapCrossPlatformTransferFlow._retainedObject
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._allPlansActivated
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._buddyMLViewController
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._cancelledDeviceIDs
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._carrierSetupPlan
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._carrierSetupPostData
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._carrierSetupUrl
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._confirmCellularPlanTransfer
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._defaultVoiceIccid
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._displayedDeviceIDs
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._iccidToEnable
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._installingPlanInfos
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._isForCrossPlatformTransfer
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._messageSession
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._pendingInteractiveViewControllers
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._planEnablementState
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._presentedViewController
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._sourceOsVersion
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._userEnabledPlanInfos
+ _OBJC_IVAR_$_TSCellularPlanItemCell._isPhysical
+ _OBJC_IVAR_$_TSCellularSetupActivatingViewController._animating
+ _OBJC_IVAR_$_TSCellularSetupActivatingViewController._cachedButtons
+ _OBJC_IVAR_$_TSCellularSetupActivatingViewController._needShow
+ _OBJC_IVAR_$_TSCellularSetupActivatingViewController._spinnerContainer
+ _OBJC_IVAR_$_TSCellularSetupCompleteViewController._client
+ _OBJC_IVAR_$_TSCellularSetupCompleteViewController._isTravelFlow
+ _OBJC_IVAR_$_TSCellularSetupCompleteViewController._isUserInHomeCountry
+ _OBJC_IVAR_$_TSCellularSetupCompleteViewController._needShow
+ _OBJC_IVAR_$_TSCellularSetupCompleteViewController._planInfo
+ _OBJC_IVAR_$_TSCellularSetupCompleteViewController._planItem
+ _OBJC_IVAR_$_TSCellularSetupTimeoutFailureViewController._isEmbeddedInResultView
+ _OBJC_IVAR_$_TSCellularSetupTimeoutFailureViewController._plans
+ _OBJC_IVAR_$_TSCrossPlatformSourceAuthFlow._didProcessDCTCode
+ _OBJC_IVAR_$_TSCrossPlatformSourceAuthFlow.dctCode
+ _OBJC_IVAR_$_TSCrossPlatformSourceTransferFlow._isFromDataTransferSession
+ _OBJC_IVAR_$_TSCrossPlatformTargetAuthFlow._dctCode
+ _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._selectedPlans
+ _OBJC_IVAR_$_TSDeviceInfoViewController._delegate
+ _OBJC_IVAR_$_TSDeviceInfoViewController._doneButton
+ _OBJC_IVAR_$_TSDeviceInfoViewController._heightAnchor
+ _OBJC_IVAR_$_TSDeviceInfoViewController._shareIdentityButton
+ _OBJC_IVAR_$_TSDeviceInfoViewController._singleItemFlow
+ _OBJC_IVAR_$_TSDeviceInfoViewController._sortedInfo
+ _OBJC_IVAR_$_TSEnableTableViewController._allPlans
+ _OBJC_IVAR_$_TSEnableTableViewController._animating
+ _OBJC_IVAR_$_TSEnableTableViewController._cachedButtons
+ _OBJC_IVAR_$_TSEnableTableViewController._continueButton
+ _OBJC_IVAR_$_TSEnableTableViewController._delegate
+ _OBJC_IVAR_$_TSEnableTableViewController._enablingIccid
+ _OBJC_IVAR_$_TSEnableTableViewController._installInfos
+ _OBJC_IVAR_$_TSEnableTableViewController._maxAllowedeSIMCount
+ _OBJC_IVAR_$_TSEnableTableViewController._needShow
+ _OBJC_IVAR_$_TSEnableTableViewController._originalEnabledPlans
+ _OBJC_IVAR_$_TSEnableTableViewController._selectedItems
+ _OBJC_IVAR_$_TSEnableTableViewController._skipButton
+ _OBJC_IVAR_$_TSEnableTableViewController._spinner
+ _OBJC_IVAR_$_TSEnableTableViewController._spinnerContainer
+ _OBJC_IVAR_$_TSIDSTransferFlow._selectedTransferPlansCount
+ _OBJC_IVAR_$_TSIdentityShareFlow._cancelButton
+ _OBJC_IVAR_$_TSIdentityShareFlow._isDeviceInfo
+ _OBJC_IVAR_$_TSIdentityShareFlow._options
+ _OBJC_IVAR_$_TSIdentityShareViewController._cancelButton
+ _OBJC_IVAR_$_TSIdentityShareViewController._delegate
+ _OBJC_IVAR_$_TSIdentityShareViewController._details
+ _OBJC_IVAR_$_TSIdentityShareViewController._detailtitle
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._client
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._continueButton
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._defaultDataContext
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._delegate
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._isShown
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._options
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._plans
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._skipButton
+ _OBJC_IVAR_$_TSLowDataModeConfigViewController._tableHeightAnchor
+ _OBJC_IVAR_$_TSManagedDeviceInstallFlow._ctClient
+ _OBJC_IVAR_$_TSMidOperationFailureViewController._isEmbeddedInResultView
+ _OBJC_IVAR_$_TSMidOperationFailureViewController._isSourceSideError
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._isShowingFilteredPlans
+ _OBJC_IVAR_$_TSNoPlanForTransferViewController._plans
+ _OBJC_IVAR_$_TSNoPlanForTransferViewController._showTurnOnLocationServices
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._NFCTransferStatus
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._cancelAction
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._ctClient
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._delegate
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._isNFCDataSuccessTransfer
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._nfcAnimationView
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._retryAction
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._systemMonitor
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController._unlockAction
+ _OBJC_IVAR_$_TSPRXIdentityShareViewController.springBoardLockStateNotifyToken
+ _OBJC_IVAR_$_TSPRXPasscodeEntryViewController.delegate
+ _OBJC_IVAR_$_TSPRXSIMTransferCompleteViewController._doneAction
+ _OBJC_IVAR_$_TSPRXSIMTransferCompleteViewController._glyphView
+ _OBJC_IVAR_$_TSPRXSIMTransferCompleteViewController._isDisembarkUIRequired
+ _OBJC_IVAR_$_TSPRXSIMTransferCompleteViewController._isSyncWithTargetResults
+ _OBJC_IVAR_$_TSPRXSIMTransferCompleteViewController._selectedPlansCount
+ _OBJC_IVAR_$_TSPRXSIMTransferCompleteViewController._selectedPlansFailedTransferCount
+ _OBJC_IVAR_$_TSPRXSIMTransferCompleteViewController._triangleImageView
+ _OBJC_IVAR_$_TSPostMigrationFlow._ctClient
+ _OBJC_IVAR_$_TSPostMigrationFlow._isProxFlowShown
+ _OBJC_IVAR_$_TSPostMigrationFlow._proximitySetupState
+ _OBJC_IVAR_$_TSPostMigrationFlow._session
+ _OBJC_IVAR_$_TSPostMigrationFlow._sourceOSVersion
+ _OBJC_IVAR_$_TSPostMigrationFlow._transferablePlanOnSource
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._areAllPlansTransferedOut
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._isDeviceIdentifierPresent
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._isPreSharedKeyPresent
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._numSelectedPlansNotTransferredOut
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._peerDeviceInfo
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._selectedTransferPlansCount
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._session
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._supportsSyncTransferResults
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._timer
+ _OBJC_IVAR_$_TSProximityTargetTransferFlow._isAuthenticationCompleted
+ _OBJC_IVAR_$_TSProximityTargetTransferFlow._isPostMigrationFlow
+ _OBJC_IVAR_$_TSProximityTargetTransferFlow._waitingStartTime
+ _OBJC_IVAR_$_TSRoamingEducationViewController._client
+ _OBJC_IVAR_$_TSRoamingEducationViewController._continueButton
+ _OBJC_IVAR_$_TSRoamingEducationViewController._delegate
+ _OBJC_IVAR_$_TSRoamingEducationViewController._skipButton
+ _OBJC_IVAR_$_TSRoamingEducationViewController._tappedLearnMore
+ _OBJC_IVAR_$_TSSIMSetupFlow._subFlowViewControllers
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._descriptors
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._formatedDescriptor
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._isDtoEvaluationRequired
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._isDtoEvaluationSucceeded
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._isSecureIntentRequired
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._isSecureIntentSucceeded
+ _OBJC_IVAR_$_TSSinglePlanTransferViewController._carrierName
+ _OBJC_IVAR_$_TSSinglePlanTransferViewController._ctClient
+ _OBJC_IVAR_$_TSSinglePlanTransferViewController._isSkipButtonTapped
+ _OBJC_IVAR_$_TSSinglePlanTransferViewController._needAutoInstallPendingPlan
+ _OBJC_IVAR_$_TSSinglePlanTransferViewController._selectedPlan
+ _OBJC_IVAR_$_TSSourceAutoReconnectTransferFlow._cancelButton
+ _OBJC_IVAR_$_TSSourceAutoReconnectTransferFlow._ctClient
+ _OBJC_IVAR_$_TSSourceAutoReconnectTransferFlow._isTransferCompleted
+ _OBJC_IVAR_$_TSSourceAutoReconnectTransferredViewController._continueButton
+ _OBJC_IVAR_$_TSSourceAutoReconnectTransferredViewController._delegate
+ _OBJC_IVAR_$_TSSourceAutoReconnectWaitingViewController._delegate
+ _OBJC_IVAR_$_TSSourceAutoReconnectWaitingViewController._skipButton
+ _OBJC_IVAR_$_TSTargetReconnectWaitingViewController._delegate
+ _OBJC_IVAR_$_TSTargetReconnectWaitingViewController._skipButton
+ _OBJC_IVAR_$_TSTargetReconnectWaitingViewController._waitingStartTime
+ _OBJC_IVAR_$_TSTransferCloudFlow._proxPlansFiltered
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._isFlexPolicyOn
+ _OBJC_IVAR_$_TSTransferFlow._isPostMigrationFlow
+ _OBJC_IVAR_$_TSTransferFlow._isUsingPreSharedKey
+ _OBJC_IVAR_$_TSTransferFlow._sourceOSVersion
+ _OBJC_IVAR_$_TSTransferFlowModel._isFlexPolicyOn
+ _OBJC_IVAR_$_TSTransferListViewController._allPlansInstallComplete
+ _OBJC_IVAR_$_TSTransferListViewController._allowMultiPlanSelection
+ _OBJC_IVAR_$_TSTransferListViewController._ctClient
+ _OBJC_IVAR_$_TSTransferListViewController._planError
+ _OBJC_IVAR_$_TSTransferListViewController._planList
+ _OBJC_IVAR_$_TSTransferListViewController._selectedPlans
+ _OBJC_IVAR_$_TSTravelBuddyViewController._animating
+ _OBJC_IVAR_$_TSTravelBuddyViewController._client
+ _OBJC_IVAR_$_TSTravelBuddyViewController._continueButton
+ _OBJC_IVAR_$_TSTravelBuddyViewController._delegate
+ _OBJC_IVAR_$_TSTravelBuddyViewController._didUserClickContinue
+ _OBJC_IVAR_$_TSTravelBuddyViewController._homeIccid
+ _OBJC_IVAR_$_TSTravelBuddyViewController._homeIccidPhoneNumber
+ _OBJC_IVAR_$_TSTravelBuddyViewController._isHomeSIMOnPhySlot
+ _OBJC_IVAR_$_TSTravelBuddyViewController._isShown
+ _OBJC_IVAR_$_TSTravelBuddyViewController._isTravelSIMDataOnly
+ _OBJC_IVAR_$_TSTravelBuddyViewController._isTravelSIMOnPhySlot
+ _OBJC_IVAR_$_TSTravelBuddyViewController._laterButton
+ _OBJC_IVAR_$_TSTravelBuddyViewController._planItems
+ _OBJC_IVAR_$_TSTravelBuddyViewController._plans
+ _OBJC_IVAR_$_TSTravelBuddyViewController._postArrivalInstallation
+ _OBJC_IVAR_$_TSTravelBuddyViewController._spinner
+ _OBJC_IVAR_$_TSTravelBuddyViewController._tableHeightAnchor
+ _OBJC_IVAR_$_TSTravelBuddyViewController._travelIccid
+ _OBJC_IVAR_$_TSTravelBuddyViewController._travelIccidInfo
+ _OBJC_IVAR_$_TSTravelBuddyViewController._travelOnlySelected
+ _OBJC_IVAR_$_TSTravelBuddyViewController._voiceIccid
+ _OBJC_IVAR_$_TSTravelBuddyViewController.cachedButtons
+ _OBJC_IVAR_$_TSTravelBuddyViewController.spinnerContainer
+ _OBJC_IVAR_$_TSTravelEducationIntroViewController._roamingInfo
+ _OBJC_IVAR_$_TSTravelModeFlow._options
+ _OBJC_IVAR_$_TSTravelModeFlow._travelSIM
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._client
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._continueButton
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._dataSubCarrierName
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._dataSubscriptionContext
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._delegate
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._footer
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._heightAnchor
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._isUserAbroad
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._options
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._roamingSwitchEnabled
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._skipButton
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._tableHeightAnchor
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._tappedLearnMore
+ _OBJC_IVAR_$_TSTravelSimCapabilitySelectionViewController._client
+ _OBJC_IVAR_$_TSTravelSimCapabilitySelectionViewController._continueButton
+ _OBJC_IVAR_$_TSTravelSimCapabilitySelectionViewController._delegate
+ _OBJC_IVAR_$_TSTravelSimCapabilitySelectionViewController._iccid
+ _OBJC_IVAR_$_TSTravelSimCapabilitySelectionViewController._installPlans
+ _OBJC_IVAR_$_TSTravelSimCapabilitySelectionViewController._isDataOnlySelected
+ _OBJC_IVAR_$_TSTravelSimCapabilitySelectionViewController._tableHeightAnchor
+ _OBJC_IVAR_$_TSTravelSimCapabilitySelectionViewController._userSelectAsTravelSIM
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._client
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._continueButton
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._delegate
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._iccid
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._installPlans
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._isSIMOnPhySlot
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._isSelectedAsTravelSIM
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._isShown
+ _OBJC_IVAR_$_TSTravelSimTypeSelectionViewController._tableHeightAnchor
+ _OBJC_IVAR_$_TSWebsheetViewController._postdata
+ _OBJC_IVAR_$_TSWebsheetViewController._url
+ _OBJC_METACLASS_$_CrossPlatformManualDetailsViewController
+ _OBJC_METACLASS_$_CrossPlatformShowManualDetailsViewController
+ _OBJC_METACLASS_$_CrossPlatformTransferIntroViewController
+ _OBJC_METACLASS_$_ExitBuddyIconView
+ _OBJC_METACLASS_$_OBSetupAssistantSpinnerController
+ _OBJC_METACLASS_$_SSCardManualEntryViewController
+ _OBJC_METACLASS_$_SSCellularPlanScanViewController
+ _OBJC_METACLASS_$_SSCellularSetupMultiSIMActivatingViewController
+ _OBJC_METACLASS_$_SSCellularSetupMultiSIMConnectingViewController
+ _OBJC_METACLASS_$_SSConfirmationCodeViewController
+ _OBJC_METACLASS_$_SSCrossPlatformScanViewController
+ _OBJC_METACLASS_$_SSInstallPlanInformation
+ _OBJC_METACLASS_$_SSLabelPickerViewController
+ _OBJC_METACLASS_$_SSLimitedSelectableTableView
+ _OBJC_METACLASS_$_SSManualEntryCell
+ _OBJC_METACLASS_$_SSMultiSIMResultViewController
+ _OBJC_METACLASS_$_SSPRXD2DMigrationDoneViewController
+ _OBJC_METACLASS_$_TSBootstrapCrossPlatformTransferFlow
+ _OBJC_METACLASS_$_TSDeviceInfoCell
+ _OBJC_METACLASS_$_TSDeviceInfoViewController
+ _OBJC_METACLASS_$_TSEnableTableViewController
+ _OBJC_METACLASS_$_TSIdentityShareFlow
+ _OBJC_METACLASS_$_TSIdentityShareViewController
+ _OBJC_METACLASS_$_TSLowDataModeConfigViewController
+ _OBJC_METACLASS_$_TSPRXIdentityShareViewController
+ _OBJC_METACLASS_$_TSPRXReconnectWaitingViewController
+ _OBJC_METACLASS_$_TSPostMigrationFlow
+ _OBJC_METACLASS_$_TSRoamingEducationViewController
+ _OBJC_METACLASS_$_TSSourceAutoReconnectTransferFlow
+ _OBJC_METACLASS_$_TSSourceAutoReconnectTransferredViewController
+ _OBJC_METACLASS_$_TSSourceAutoReconnectWaitingViewController
+ _OBJC_METACLASS_$_TSTargetReconnectWaitingViewController
+ _OBJC_METACLASS_$_TSTravelBuddyViewController
+ _OBJC_METACLASS_$_TSTravelModeFlow
+ _OBJC_METACLASS_$_TSTravelModeIntroViewController
+ _OBJC_METACLASS_$_TSTravelSimCapabilitySelectionViewController
+ _OBJC_METACLASS_$_TSTravelSimTypeSelectionViewController
+ _OBJC_METACLASS_$_UITableView
+ _PKNearFieldRadioIsEnabled
+ _SSPlanTransferStatusAsString
+ _TSMigrationAuthCodeKey
+ _TSNotificationCrossPlatformTransfer
+ _TSNotificationInstallFailed
+ _TSTravelActionPostArrivalBuddyLDMOff
+ _TSTravelActionPostArrivalBuddyLDMOn
+ _TSTravelActionPostArrivalBuddyUseTravelAndHomeSIM
+ _TSTravelActionPostArrivalBuddyUseTravelSIM
+ _TSTravelActionPostArrivalInstallLDMOff
+ _TSTravelActionPostArrivalInstallLDMOn
+ _TSTravelActionPostArrivalInstallUseTravelAndHomeSIM
+ _TSTravelActionPostArrivalInstallUseTravelSIM
+ _TSTravelActionRoamingEducationRoamingOff
+ _TSTravelActionRoamingEducationRoamingOn
+ _TSTravelActionTappedLearnMore
+ _TSTravelActionTravelIntroRoamingOff
+ _TSTravelActionTravelIntroRoamingOn
+ _TSTravelEventDetailsFinalAction
+ _TSTravelEventDetailsFinalActionSubtype
+ _TSTravelEventDetailsIccid
+ _TSTravelEventDetailsNotificationType
+ _TSTravelEventNotificationPostArrivalBuddy
+ _TSTravelEventNotificationPostArrivalBuddyRoaming
+ _TSTravelEventNotificationPostArrivalInstall
+ _TSTravelEventNotificationPreDepartureInstall
+ _TSTravelEventNotificationRoamingEducation
+ _TSTravelEventNotificationTravelIntro
+ _TSTravelExtractionSource
+ _TSTravelHomeSIMIccid
+ _TSTravelModeOptions
+ _TSTravelPurchasedSIMIccid
+ _TSTravelRoamingURL
+ _TSTravelShowLocalPlanOption
+ _TSTravelShowPurchaseOption
+ _TSTravelShowRoamingOption
+ _TSTravelUserLocation
+ _TSTravelVoiceSIMIccid
+ _TSUserInfoConfirmCellularPlanTransferKey
+ _TSUserInfoForCrossPlatformTransferKey
+ _TSUserInfoFromDataTransferSessionKey
+ _TSUserInfoHasLocalPlanKey
+ _TSUserInfoHostViewControllerKey
+ _TSUserInfoIccidToEnableKey
+ _TSUserInfoIsD2DMigrationSucceedKey
+ _TSUserInfoIsDtoEvaluationRequiredKey
+ _TSUserInfoIsPostMigrationFlowKey
+ _TSUserInfoIsSecureIntentRequiredKey
+ _TSUserInfoIsSourceKey
+ _TSUserInfoIsUsingPreSharedKeyKey
+ _TSUserInfoMigrationAuthCodeKey
+ _TSUserInfoNavigationControllerKey
+ _TSUserInfoPlanIdKey
+ _TSUserInfoPlansKey
+ _TSUserInfoProxPlansFilteredKey
+ _TSUserInfoRetainReference
+ _TSUserInfoSourceOSVersionKey
+ _TSUserInfoWebsheetInfoKey
+ _UIKeyboardDidHideNotification
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UITableViewCell_$_SS
+ __OBJC_$_CATEGORY_NSString_$_SHA256
+ __OBJC_$_CATEGORY_UITableViewCell_$_SS
+ __OBJC_$_CATEGORY_UIViewController_$_Flow
+ __OBJC_$_CLASS_METHODS_SSManualEntryCell
+ __OBJC_$_CLASS_METHODS_TSDeviceInfoViewController
+ __OBJC_$_CLASS_METHODS_TSIdentityShareFlow
+ __OBJC_$_CLASS_METHODS_TSIdentityShareViewController
+ __OBJC_$_CLASS_METHODS_TSPRXIdentityShareViewController
+ __OBJC_$_INSTANCE_METHODS_CTDisplayPlan(SimSetup|UITableViewCell)
+ __OBJC_$_INSTANCE_METHODS_CrossPlatformManualDetailsViewController
+ __OBJC_$_INSTANCE_METHODS_CrossPlatformShowManualDetailsViewController
+ __OBJC_$_INSTANCE_METHODS_CrossPlatformTransferIntroViewController
+ __OBJC_$_INSTANCE_METHODS_ExitBuddyIconView
+ __OBJC_$_INSTANCE_METHODS_NSString(SHA256|QRCode|PhoneNumber)
+ __OBJC_$_INSTANCE_METHODS_OBHeaderView(SSHelper|SSHelper)
+ __OBJC_$_INSTANCE_METHODS_SSCardManualEntryViewController
+ __OBJC_$_INSTANCE_METHODS_SSCellularPlanScanViewController
+ __OBJC_$_INSTANCE_METHODS_SSCellularSetupMultiSIMActivatingViewController(ViewLifeCycle|UITableViewDataSource|TSSetupFlowItem)
+ __OBJC_$_INSTANCE_METHODS_SSCellularSetupMultiSIMConnectingViewController(TSSetupFlowItem)
+ __OBJC_$_INSTANCE_METHODS_SSConfirmationCodeViewController
+ __OBJC_$_INSTANCE_METHODS_SSCrossPlatformScanViewController
+ __OBJC_$_INSTANCE_METHODS_SSInstallPlanInformation
+ __OBJC_$_INSTANCE_METHODS_SSLabelPickerViewController
+ __OBJC_$_INSTANCE_METHODS_SSLimitedSelectableTableView
+ __OBJC_$_INSTANCE_METHODS_SSManualEntryCell
+ __OBJC_$_INSTANCE_METHODS_SSMultiSIMResultViewController(TSSetupFlowItem)
+ __OBJC_$_INSTANCE_METHODS_SSPRXD2DMigrationDoneViewController
+ __OBJC_$_INSTANCE_METHODS_TSBootstrapCrossPlatformTransferFlow
+ __OBJC_$_INSTANCE_METHODS_TSCellularPlanActivatingFlow(Override|TSCellularPlanManagerCacheDelegate|CoreTelephonyClientCellularPlanManagementDelegate|TSSIMSetupDelegate|TSSIMSetupFlowDelegate|Single|Consolidated|UpdatePlanInfo|InteractiveUI)
+ __OBJC_$_INSTANCE_METHODS_TSCellularSetupActivatingViewController(TSSetupFlowItem)
+ __OBJC_$_INSTANCE_METHODS_TSCellularSetupCompleteViewController(TSSetupFlowItem)
+ __OBJC_$_INSTANCE_METHODS_TSCellularSetupTimeoutFailureViewController(TSSetupFlowItem)
+ __OBJC_$_INSTANCE_METHODS_TSDeviceInfoCell
+ __OBJC_$_INSTANCE_METHODS_TSDeviceInfoViewController
+ __OBJC_$_INSTANCE_METHODS_TSEnableTableViewController(UITableViewDelegate|UITableViewDataSource)
+ __OBJC_$_INSTANCE_METHODS_TSIdentityShareFlow
+ __OBJC_$_INSTANCE_METHODS_TSIdentityShareViewController
+ __OBJC_$_INSTANCE_METHODS_TSLowDataModeConfigViewController
+ __OBJC_$_INSTANCE_METHODS_TSMidOperationFailureViewController(TSSetupFlowItem)
+ __OBJC_$_INSTANCE_METHODS_TSNoPlanForTransferViewController(UITableViewDataSource)
+ __OBJC_$_INSTANCE_METHODS_TSPRXIdentityShareViewController
+ __OBJC_$_INSTANCE_METHODS_TSPRXReconnectWaitingViewController
+ __OBJC_$_INSTANCE_METHODS_TSPostMigrationFlow
+ __OBJC_$_INSTANCE_METHODS_TSRoamingEducationViewController
+ __OBJC_$_INSTANCE_METHODS_TSSourceAutoReconnectTransferFlow
+ __OBJC_$_INSTANCE_METHODS_TSSourceAutoReconnectTransferredViewController
+ __OBJC_$_INSTANCE_METHODS_TSSourceAutoReconnectWaitingViewController
+ __OBJC_$_INSTANCE_METHODS_TSTargetReconnectWaitingViewController
+ __OBJC_$_INSTANCE_METHODS_TSTravelBuddyViewController
+ __OBJC_$_INSTANCE_METHODS_TSTravelModeFlow
+ __OBJC_$_INSTANCE_METHODS_TSTravelModeIntroViewController
+ __OBJC_$_INSTANCE_METHODS_TSTravelSimCapabilitySelectionViewController
+ __OBJC_$_INSTANCE_METHODS_TSTravelSimTypeSelectionViewController
+ __OBJC_$_INSTANCE_METHODS_UILabel(RangeBold|RangeBold|RangeBold)
+ __OBJC_$_INSTANCE_METHODS_UIViewController(Flow|InModalPresentation|SubFlow)
+ __OBJC_$_INSTANCE_VARIABLES_CrossPlatformManualDetailsViewController
+ __OBJC_$_INSTANCE_VARIABLES_CrossPlatformShowManualDetailsViewController
+ __OBJC_$_INSTANCE_VARIABLES_CrossPlatformTransferIntroViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSCardManualEntryViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSCellularPlanScanViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSCellularSetupMultiSIMActivatingViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSCellularSetupMultiSIMConnectingViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSConfirmationCodeViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSInstallPlanInformation
+ __OBJC_$_INSTANCE_VARIABLES_SSLabelPickerViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSLimitedSelectableTableView
+ __OBJC_$_INSTANCE_VARIABLES_SSManualEntryCell
+ __OBJC_$_INSTANCE_VARIABLES_SSMultiSIMResultViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSPRXD2DMigrationDoneViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSBootstrapCrossPlatformTransferFlow
+ __OBJC_$_INSTANCE_VARIABLES_TSDeviceInfoViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSEnableTableViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSIdentityShareFlow
+ __OBJC_$_INSTANCE_VARIABLES_TSIdentityShareViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSLowDataModeConfigViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSPRXIdentityShareViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSPostMigrationFlow
+ __OBJC_$_INSTANCE_VARIABLES_TSRoamingEducationViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSSourceAutoReconnectTransferFlow
+ __OBJC_$_INSTANCE_VARIABLES_TSSourceAutoReconnectTransferredViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSSourceAutoReconnectWaitingViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTargetReconnectWaitingViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelBuddyViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelModeFlow
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelModeIntroViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelSimCapabilitySelectionViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelSimTypeSelectionViewController
+ __OBJC_$_PROP_LIST_CrossPlatformManualDetailsViewController
+ __OBJC_$_PROP_LIST_CrossPlatformShowManualDetailsViewController
+ __OBJC_$_PROP_LIST_CrossPlatformTransferIntroViewController
+ __OBJC_$_PROP_LIST_SSCardManualEntryViewController
+ __OBJC_$_PROP_LIST_SSCellularPlanScanViewController
+ __OBJC_$_PROP_LIST_SSCellularSetupMultiSIMConnectingViewController
+ __OBJC_$_PROP_LIST_SSConfirmationCodeViewController
+ __OBJC_$_PROP_LIST_SSInstallPlanInformation
+ __OBJC_$_PROP_LIST_SSLabelPickerViewController
+ __OBJC_$_PROP_LIST_SSLimitedSelectableTableView
+ __OBJC_$_PROP_LIST_SSManualEntryCell
+ __OBJC_$_PROP_LIST_SSMultiSIMResultViewController
+ __OBJC_$_PROP_LIST_SSPRXD2DMigrationDoneViewController
+ __OBJC_$_PROP_LIST_TSBootstrapCrossPlatformTransferFlow
+ __OBJC_$_PROP_LIST_TSDeviceInfoViewController
+ __OBJC_$_PROP_LIST_TSIdentityShareFlow
+ __OBJC_$_PROP_LIST_TSIdentityShareViewController
+ __OBJC_$_PROP_LIST_TSLowDataModeConfigViewController
+ __OBJC_$_PROP_LIST_TSPRXIdentityShareViewController
+ __OBJC_$_PROP_LIST_TSPostMigrationFlow
+ __OBJC_$_PROP_LIST_TSRoamingEducationViewController
+ __OBJC_$_PROP_LIST_TSSetupFlowItem
+ __OBJC_$_PROP_LIST_TSSourceAutoReconnectTransferFlow
+ __OBJC_$_PROP_LIST_TSSourceAutoReconnectTransferredViewController
+ __OBJC_$_PROP_LIST_TSSourceAutoReconnectWaitingViewController
+ __OBJC_$_PROP_LIST_TSTargetReconnectWaitingViewController
+ __OBJC_$_PROP_LIST_TSTravelBuddyViewController
+ __OBJC_$_PROP_LIST_TSTravelModeFlow
+ __OBJC_$_PROP_LIST_TSTravelModeIntroViewController
+ __OBJC_$_PROP_LIST_TSTravelSimCapabilitySelectionViewController
+ __OBJC_$_PROP_LIST_TSTravelSimTypeSelectionViewController
+ __OBJC_$_PROP_LIST_UIViewController_$_Flow
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DCTCodeDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PRXFlowDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DCTCodeDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRXFlowDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientDelegate
+ __OBJC_$_PROTOCOL_REFS_DCTCodeDelegate
+ __OBJC_$_PROTOCOL_REFS_PRXFlowDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CrossPlatformManualDetailsViewController
+ __OBJC_CLASS_PROTOCOLS_$_CrossPlatformShowManualDetailsViewController
+ __OBJC_CLASS_PROTOCOLS_$_CrossPlatformTransferIntroViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSCardManualEntryViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSCellularPlanScanViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSCellularSetupMultiSIMActivatingViewController(ViewLifeCycle|UITableViewDataSource|TSSetupFlowItem)
+ __OBJC_CLASS_PROTOCOLS_$_SSConfirmationCodeViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSLabelPickerViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSLimitedSelectableTableView
+ __OBJC_CLASS_PROTOCOLS_$_SSMultiSIMResultViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSPRXD2DMigrationDoneViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSCellularPlanActivatingFlow(Override|TSCellularPlanManagerCacheDelegate|CoreTelephonyClientCellularPlanManagementDelegate|TSSIMSetupDelegate|TSSIMSetupFlowDelegate|Single|Consolidated|UpdatePlanInfo|InteractiveUI)
+ __OBJC_CLASS_PROTOCOLS_$_TSDeviceInfoViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSEnableTableViewController(UITableViewDelegate|UITableViewDataSource)
+ __OBJC_CLASS_PROTOCOLS_$_TSIdentityShareFlow
+ __OBJC_CLASS_PROTOCOLS_$_TSIdentityShareViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSLowDataModeConfigViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSNoPlanForTransferViewController(UITableViewDataSource)
+ __OBJC_CLASS_PROTOCOLS_$_TSPRXIdentityShareViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSPostMigrationFlow
+ __OBJC_CLASS_PROTOCOLS_$_TSRoamingEducationViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSSourceAutoReconnectTransferFlow
+ __OBJC_CLASS_PROTOCOLS_$_TSSourceAutoReconnectTransferredViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSSourceAutoReconnectWaitingViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTargetReconnectWaitingViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelBuddyViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelModeFlow
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelModeIntroViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelSimCapabilitySelectionViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelSimTypeSelectionViewController
+ __OBJC_CLASS_RO_$_CrossPlatformManualDetailsViewController
+ __OBJC_CLASS_RO_$_CrossPlatformShowManualDetailsViewController
+ __OBJC_CLASS_RO_$_CrossPlatformTransferIntroViewController
+ __OBJC_CLASS_RO_$_ExitBuddyIconView
+ __OBJC_CLASS_RO_$_SSCardManualEntryViewController
+ __OBJC_CLASS_RO_$_SSCellularPlanScanViewController
+ __OBJC_CLASS_RO_$_SSCellularSetupMultiSIMActivatingViewController
+ __OBJC_CLASS_RO_$_SSCellularSetupMultiSIMConnectingViewController
+ __OBJC_CLASS_RO_$_SSConfirmationCodeViewController
+ __OBJC_CLASS_RO_$_SSCrossPlatformScanViewController
+ __OBJC_CLASS_RO_$_SSInstallPlanInformation
+ __OBJC_CLASS_RO_$_SSLabelPickerViewController
+ __OBJC_CLASS_RO_$_SSLimitedSelectableTableView
+ __OBJC_CLASS_RO_$_SSManualEntryCell
+ __OBJC_CLASS_RO_$_SSMultiSIMResultViewController
+ __OBJC_CLASS_RO_$_SSPRXD2DMigrationDoneViewController
+ __OBJC_CLASS_RO_$_TSBootstrapCrossPlatformTransferFlow
+ __OBJC_CLASS_RO_$_TSDeviceInfoCell
+ __OBJC_CLASS_RO_$_TSDeviceInfoViewController
+ __OBJC_CLASS_RO_$_TSEnableTableViewController
+ __OBJC_CLASS_RO_$_TSIdentityShareFlow
+ __OBJC_CLASS_RO_$_TSIdentityShareViewController
+ __OBJC_CLASS_RO_$_TSLowDataModeConfigViewController
+ __OBJC_CLASS_RO_$_TSPRXIdentityShareViewController
+ __OBJC_CLASS_RO_$_TSPRXReconnectWaitingViewController
+ __OBJC_CLASS_RO_$_TSPostMigrationFlow
+ __OBJC_CLASS_RO_$_TSRoamingEducationViewController
+ __OBJC_CLASS_RO_$_TSSourceAutoReconnectTransferFlow
+ __OBJC_CLASS_RO_$_TSSourceAutoReconnectTransferredViewController
+ __OBJC_CLASS_RO_$_TSSourceAutoReconnectWaitingViewController
+ __OBJC_CLASS_RO_$_TSTargetReconnectWaitingViewController
+ __OBJC_CLASS_RO_$_TSTravelBuddyViewController
+ __OBJC_CLASS_RO_$_TSTravelModeFlow
+ __OBJC_CLASS_RO_$_TSTravelModeIntroViewController
+ __OBJC_CLASS_RO_$_TSTravelSimCapabilitySelectionViewController
+ __OBJC_CLASS_RO_$_TSTravelSimTypeSelectionViewController
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientDelegate
+ __OBJC_LABEL_PROTOCOL_$_DCTCodeDelegate
+ __OBJC_LABEL_PROTOCOL_$_PRXFlowDelegate
+ __OBJC_METACLASS_RO_$_CrossPlatformManualDetailsViewController
+ __OBJC_METACLASS_RO_$_CrossPlatformShowManualDetailsViewController
+ __OBJC_METACLASS_RO_$_CrossPlatformTransferIntroViewController
+ __OBJC_METACLASS_RO_$_ExitBuddyIconView
+ __OBJC_METACLASS_RO_$_SSCardManualEntryViewController
+ __OBJC_METACLASS_RO_$_SSCellularPlanScanViewController
+ __OBJC_METACLASS_RO_$_SSCellularSetupMultiSIMActivatingViewController
+ __OBJC_METACLASS_RO_$_SSCellularSetupMultiSIMConnectingViewController
+ __OBJC_METACLASS_RO_$_SSConfirmationCodeViewController
+ __OBJC_METACLASS_RO_$_SSCrossPlatformScanViewController
+ __OBJC_METACLASS_RO_$_SSInstallPlanInformation
+ __OBJC_METACLASS_RO_$_SSLabelPickerViewController
+ __OBJC_METACLASS_RO_$_SSLimitedSelectableTableView
+ __OBJC_METACLASS_RO_$_SSManualEntryCell
+ __OBJC_METACLASS_RO_$_SSMultiSIMResultViewController
+ __OBJC_METACLASS_RO_$_SSPRXD2DMigrationDoneViewController
+ __OBJC_METACLASS_RO_$_TSBootstrapCrossPlatformTransferFlow
+ __OBJC_METACLASS_RO_$_TSDeviceInfoCell
+ __OBJC_METACLASS_RO_$_TSDeviceInfoViewController
+ __OBJC_METACLASS_RO_$_TSEnableTableViewController
+ __OBJC_METACLASS_RO_$_TSIdentityShareFlow
+ __OBJC_METACLASS_RO_$_TSIdentityShareViewController
+ __OBJC_METACLASS_RO_$_TSLowDataModeConfigViewController
+ __OBJC_METACLASS_RO_$_TSPRXIdentityShareViewController
+ __OBJC_METACLASS_RO_$_TSPRXReconnectWaitingViewController
+ __OBJC_METACLASS_RO_$_TSPostMigrationFlow
+ __OBJC_METACLASS_RO_$_TSRoamingEducationViewController
+ __OBJC_METACLASS_RO_$_TSSourceAutoReconnectTransferFlow
+ __OBJC_METACLASS_RO_$_TSSourceAutoReconnectTransferredViewController
+ __OBJC_METACLASS_RO_$_TSSourceAutoReconnectWaitingViewController
+ __OBJC_METACLASS_RO_$_TSTargetReconnectWaitingViewController
+ __OBJC_METACLASS_RO_$_TSTravelBuddyViewController
+ __OBJC_METACLASS_RO_$_TSTravelModeFlow
+ __OBJC_METACLASS_RO_$_TSTravelModeIntroViewController
+ __OBJC_METACLASS_RO_$_TSTravelSimCapabilitySelectionViewController
+ __OBJC_METACLASS_RO_$_TSTravelSimTypeSelectionViewController
+ __OBJC_PROTOCOL_$_CoreTelephonyClientDelegate
+ __OBJC_PROTOCOL_$_DCTCodeDelegate
+ __OBJC_PROTOCOL_$_PRXFlowDelegate
+ ___103-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _offerFallbackOption]_block_invoke
+ ___103-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _offerFallbackOption]_block_invoke_2
+ ___103-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _offerFallbackOption]_block_invoke_3
+ ___103-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _offerFallbackOption]_block_invoke_4
+ ___109-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) launchWebsheet:completion:]_block_invoke
+ ___114-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _shouldWaitUntilPhoneNumberBeReady:completion:]_block_invoke
+ ___114-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _shouldWaitUntilPhoneNumberBeReady:completion:]_block_invoke.cold.1
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.484
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke_2
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke_3
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke_4
+ ___131-[TSIDSTransferFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:]_block_invoke
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke.50
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke_2
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke_3
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke_4
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke_5
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke_6
+ ___147-[TSTransferFlowModel arePlansAvailable:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke
+ ___147-[TSTransferFlowModel arePlansAvailable:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke.cold.1
+ ___155-[TSCellularPlanProximityTransferController launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:]_block_invoke
+ ___157-[TSTransferFlow initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:]_block_invoke
+ ___29-[TSSIMSetupFlow _startOver:]_block_invoke_3.cold.1
+ ___32+[TSIdentityShareFlow showAlert]_block_invoke
+ ___32+[TSIdentityShareFlow showAlert]_block_invoke_2
+ ___32+[TSIdentityShareFlow showAlert]_block_invoke_2.cold.1
+ ___34-[TSAuthFlow firstViewController:]_block_invoke
+ ___36-[TSWebsheetViewController prepare:]_block_invoke
+ ___39-[SSScanViewController decodeMetadata:]_block_invoke.51
+ ___39-[TSSIMSetupFlow setIdleTimerDisabled:]_block_invoke
+ ___39-[TSTransferFlow _firstViewController:]_block_invoke.184
+ ___39-[TSTransferFlow _firstViewController:]_block_invoke.cold.1
+ ___39-[TSTravelBuddyViewController prepare:]_block_invoke
+ ___39-[TSTravelBuddyViewController prepare:]_block_invoke.48
+ ___43-[SSPRXD2DMigrationDoneViewController init]_block_invoke
+ ___43-[TSPostMigrationFlow firstViewController:]_block_invoke
+ ___43-[TSSIMSetupFlow addSubFlowViewController:]_block_invoke
+ ___44-[SSConfirmationCodeViewController confirm:]_block_invoke
+ ___44-[TSTransferFlowModel requestCarrierSetups:]_block_invoke.45
+ ___45-[TSLowDataModeConfigViewController prepare:]_block_invoke
+ ___45-[TSLowDataModeConfigViewController prepare:]_block_invoke.cold.1
+ ___45-[TSWebsheetViewController _showFailureAlert]_block_invoke
+ ___46-[TSRemotePlanSignUpFlow firstViewController:]_block_invoke
+ ___47-[TSPRXIdentityShareViewController viewDidLoad]_block_invoke
+ ___47-[TSPRXIdentityShareViewController viewDidLoad]_block_invoke_2
+ ___47-[TSPRXIdentityShareViewController viewDidLoad]_block_invoke_3
+ ___47-[TSSecureIntentGestureViewController prepare:]_block_invoke
+ ___47-[TSSecureIntentGestureViewController prepare:]_block_invoke_2
+ ___48-[TSPRXDeviceUnlockViewController _unlockScreen]_block_invoke.58
+ ___48-[TSPRXDeviceUnlockViewController _unlockScreen]_block_invoke.58.cold.1
+ ___49-[TSPRXIdentityShareViewController _unlockScreen]_block_invoke
+ ___49-[TSPRXIdentityShareViewController _unlockScreen]_block_invoke.cold.1
+ ___49-[TSTransferCloudFlowModel requestCarrierSetups:]_block_invoke.40
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.35
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.35.cold.1
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.35.cold.2
+ ___50-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke.31
+ ___50-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke.37
+ ___50-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke_2.38
+ ___50-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke_2.38.cold.1
+ ___50-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke_3.39
+ ___50-[TSProximitySourceTransferFlow _registerMessages]_block_invoke
+ ___50-[TSProximitySourceTransferFlow _registerMessages]_block_invoke_2
+ ___50-[TSTravelSimTypeSelectionViewController prepare:]_block_invoke
+ ___51-[TSProximitySourceTransferFlow _bootstrapTransfer]_block_invoke.144
+ ___51-[TSSIMSetupFlow _maybeClearSubFlowViewController:]_block_invoke
+ ___52-[SSConfirmationCodeViewController userDidTapCancel]_block_invoke
+ ___52-[SSConfirmationCodeViewController userDidTapCancel]_block_invoke_2
+ ___52-[TSCellularPlanActivatingFlow _maybeMoveToNextItem]_block_invoke
+ ___52-[TSCellularPlanActivatingFlow _maybeMoveToNextItem]_block_invoke_2
+ ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke
+ ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke.79
+ ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke.cold.1
+ ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke_2
+ ___52-[TSSetupAssistantSIMSetupFlow firstViewController:]_block_invoke
+ ___52-[TSSetupAssistantSIMSetupFlow firstViewController:]_block_invoke_2
+ ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.22
+ ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.22.cold.1
+ ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.22.cold.2
+ ___53-[TSPRXSIMTransferCompleteViewController viewDidLoad]_block_invoke
+ ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke.112
+ ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke.112.cold.1
+ ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke.113
+ ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke.113.cold.1
+ ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke.113.cold.2
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.212
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.214
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.213
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_3
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_3.cold.1
+ ___53-[TSTravelBuddyViewController _continueButtonTapped:]_block_invoke
+ ___54-[TSActivationPolicyMismatchFlow firstViewController:]_block_invoke
+ ___55-[TSEnableTableViewController _prepareForEnablingItem:]_block_invoke
+ ___55-[TSPRXIdentityShareViewController _startSystemMonitor]_block_invoke
+ ___55-[TSPRXIdentityShareViewController _startSystemMonitor]_block_invoke_2
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.31
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.31.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.32
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.32.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.33
+ ___56-[NSString(QRCode) parseQueryParamsWithTitleDictionary:]_block_invoke
+ ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.40
+ ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.40.cold.1
+ ___56-[TSCellularPlanActivatingFlow _cancelTransferringPlan:]_block_invoke
+ ___56-[TSCellularPlanActivatingFlow _cancelTransferringPlan:]_block_invoke.cold.1
+ ___56-[TSPostMigrationFlow prepareViewController:completion:]_block_invoke
+ ___56-[TSTransferFlow _maybeClearFirstViewControllerCallback]_block_invoke
+ ___56-[TSTravelSimCapabilitySelectionViewController prepare:]_block_invoke
+ ___57-[SSCardManualEntryViewController addNewPlanWithUserInfo]_block_invoke
+ ___57-[SSCardManualEntryViewController textFieldShouldReturn:]_block_invoke
+ ___57-[TSCellularPlanActivatingFlow _maybeSendTransferResults]_block_invoke
+ ___57-[TSCrossPlatformSourceTransferFlow firstViewController:]_block_invoke
+ ___57-[TSCrossPlatformTargetTransferFlow firstViewController:]_block_invoke.23
+ ___57-[TSPRXIdentityShareViewController _successIdentityShare]_block_invoke
+ ___57-[TSPRXIdentityShareViewController _successIdentityShare]_block_invoke_2
+ ___57-[TSSecureIntentGestureViewController evaluateDtoPolicy:]_block_invoke
+ ___57-[TSSinglePlanTransferViewController _startPlanTransfer:]_block_invoke_4
+ ___57-[TSSinglePlanTransferViewController _startPlanTransfer:]_block_invoke_5
+ ___57-[TSSourceAutoReconnectTransferFlow firstViewController:]_block_invoke
+ ___57-[TSSourceAutoReconnectTransferFlow firstViewController:]_block_invoke.cold.1
+ ___57-[TSSourceAutoReconnectWaitingViewController viewDidLoad]_block_invoke
+ ___58-[SSProximityDevice activateUsingPreSharedKey:completion:]_block_invoke
+ ___58-[SSProximityDevice activateUsingPreSharedKey:completion:]_block_invoke.25
+ ___58-[SSProximityDevice activateUsingPreSharedKey:completion:]_block_invoke.25.cold.1
+ ___58-[SSProximityDevice activateUsingPreSharedKey:completion:]_block_invoke.cold.1
+ ___58-[TSEnableTableViewController _prepareForInstallingItems:]_block_invoke
+ ___58-[TSPRXIdentityShareViewController _startNFCIdentityShare]_block_invoke
+ ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke.80
+ ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke_2
+ ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke_3
+ ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke_4
+ ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.68
+ ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.68.cold.1
+ ___59-[TSCrossPlatformSourceAuthFlow viewControllerDidComplete:]_block_invoke
+ ___59-[TSCrossPlatformSourceAuthFlow viewControllerDidComplete:]_block_invoke.cold.1
+ ___59-[TSSinglePlanTransferViewController _startPendingInstall:]_block_invoke_3
+ ___59-[TSSinglePlanTransferViewController _startPendingInstall:]_block_invoke_4
+ ___59-[TSTransferOneTimeCodeViewController _cancelButtonTapped:]_block_invoke
+ ___60-[TSBootstrapCrossPlatformTransferFlow firstViewController:]_block_invoke
+ ___60-[TSBootstrapCrossPlatformTransferFlow firstViewController:]_block_invoke.27
+ ___60-[TSCoreTelephonyClientCache submitAutoReconnectionDetails:]_block_invoke
+ ___60-[TSCoreTelephonyClientCache submitAutoReconnectionDetails:]_block_invoke.cold.1
+ ___61-[CrossPlatformManualDetailsViewController _doneButtonTapped]_block_invoke
+ ___61-[CrossPlatformManualDetailsViewController _doneButtonTapped]_block_invoke.cold.1
+ ___61-[CrossPlatformManualDetailsViewController _doneButtonTapped]_block_invoke.cold.2
+ ___61-[TSPostMigrationFlow _subFlowVcWithReconnectionCredentials:]_block_invoke
+ ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke
+ ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.160
+ ___62-[TSCellularSetupCompleteViewController _continueButtonTapped]_block_invoke
+ ___62-[TSCellularSetupCompleteViewController _continueButtonTapped]_block_invoke.cold.1
+ ___62-[TSCrossPlatformSourceAuthFlow _showCancelAlert:withMessage:]_block_invoke
+ ___62-[TSCrossPlatformSourceAuthFlow _showCancelAlert:withMessage:]_block_invoke_2
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.184
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.186
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke_2
+ ___63-[TSCellularPlanActivatingFlow _maybeSendTransferUICapability:]_block_invoke
+ ___63-[TSCrossPlatformTargetAuthFlow deactiveCrossPlatformTransport]_block_invoke
+ ___63-[TSCrossPlatformTargetAuthFlow deactiveCrossPlatformTransport]_block_invoke.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.100
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.97
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.97.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.98
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.98.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.99
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.99.cold.1
+ ___64-[TSPRXSIMTransferringViewController _setupOneTimeCodeDetection]_block_invoke.65
+ ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke.197
+ ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke_4
+ ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke_5
+ ___65-[TSCellularPlanActivatingFlow _maybePresentFirstViewController:]_block_invoke
+ ___65-[TSCellularPlanActivatingFlow _maybePresentFirstViewController:]_block_invoke.53
+ ___65-[TSCellularPlanActivatingFlow _maybePresentFirstViewController:]_block_invoke.cold.1
+ ___65-[TSEnableTableViewController _getTraveleSIMStateWithCompletion:]_block_invoke
+ ___65-[TSTravelBuddyViewController _getTraveleSIMStateWithCompletion:]_block_invoke
+ ___66-[CrossPlatformManualDetailsViewController textFieldShouldReturn:]_block_invoke
+ ___66-[TSCrossPlatformTargetTransferFlow _showCancelAlert:withMessage:]_block_invoke
+ ___66-[TSCrossPlatformTargetTransferFlow _showCancelAlert:withMessage:]_block_invoke_2
+ ___66-[TSRecommendedCarrierAppsFlow _requestCarrierAppsWithCompletion:]_block_invoke_3
+ ___66-[TSRecommendedCarrierAppsFlow _requestCarrierAppsWithCompletion:]_block_invoke_3.cold.1
+ ___66-[TSRecommendedCarrierAppsFlow _requestCarrierAppsWithCompletion:]_block_invoke_3.cold.2
+ ___67-[TSSIMSetupFlow maybePrepareNextDisplayViewController:completion:]_block_invoke
+ ___67-[TSSIMSetupFlow maybePrepareNextDisplayViewController:completion:]_block_invoke_2
+ ___70-[TSCellularPlanActivatingFlow _maybeDisplaySourceDeviceConsentAlert:]_block_invoke
+ ___70-[TSCellularPlanActivatingFlow _maybeDisplaySourceDeviceConsentAlert:]_block_invoke_2
+ ___70-[TSCellularPlanActivatingFlow _maybeDisplaySourceDeviceConsentAlert:]_block_invoke_3
+ ___70-[TSCellularSetupLoadingViewController safariViewControllerDidFinish:]_block_invoke.94
+ ___70-[TSTravelSimCapabilitySelectionViewController _continueButtonTapped:]_block_invoke
+ ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.108
+ ___72-[TSBootstrapCrossPlatformTransferFlow initWithRetainedObject:isSource:]_block_invoke
+ ___72-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) userDidTapCancel]_block_invoke
+ ___72-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) userDidTapCancel]_block_invoke.cold.1
+ ___72-[TSCrossPlatformSourceTransferFlow _prepareDisplayItems:withPlanItems:]_block_invoke
+ ___74-[TSCellularPlanActivatingFlow(InteractiveUI) _maybeDisplayInteractiveUI:]_block_invoke
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.530
+ ___75-[SSCrossPlatformTransferSourceSelectionViewController _cancelButtonTapped]_block_invoke
+ ___75-[SSCrossPlatformTransferSourceSelectionViewController _cancelButtonTapped]_block_invoke.cold.1
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.102
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.102.cold.1
+ ___75-[TSCellularPlanActivatingFlow(InteractiveUI) _getWebsheetInfo:completion:]_block_invoke
+ ___75-[TSCellularPlanActivatingFlow(InteractiveUI) _getWebsheetInfo:completion:]_block_invoke.cold.1
+ ___77-[SSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke
+ ___77-[SSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke.62
+ ___77-[SSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke_2
+ ___77-[SSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke_2.cold.1
+ ___77-[SSLimitedSelectableTableView selectRowAtIndexPath:animated:scrollPosition:]_block_invoke
+ ___78-[SSCrossPlatformTransferSourceSelectionViewController _preselectPlanIfNeeded]_block_invoke
+ ___79-[TSCellularSetupLoadingViewController setupCoreTelephonyClientForRemoteSignup]_block_invoke.61
+ ___80-[TSCellularPlanActivatingFlow _maybeStartTimerForNewlyInstalledPlan:newStatus:]_block_invoke
+ ___80-[TSSIMSetupFlow handleStartOverWithEntryPoint:navigationController:completion:]_block_invoke
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayCarrierSetupViewController:]_block_invoke
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayCarrierSetupViewController:]_block_invoke.cold.1
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.595
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.cold.1
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.542
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.542.cold.1
+ ___83-[TSCrossPlatformTargetTransferFlow handleCrossplatformSessionResponse:completion:]_block_invoke
+ ___83-[TSCrossPlatformTargetTransferFlow handleCrossplatformSessionResponse:completion:]_block_invoke_2
+ ___83-[TSCrossPlatformTargetTransferFlow handleCrossplatformSessionResponse:completion:]_block_invoke_2.cold.1
+ ___86-[TSCellularPlanActivatingFlow(InteractiveUI) _displayConfirmationCodeViewController:]_block_invoke
+ ___87-[TSCrossPlatformSourceTransferFlow launchSimSetupForTransferPlanSelection:completion:]_block_invoke.31
+ ___87-[TSCrossPlatformSourceTransferFlow launchSimSetupForTransferPlanSelection:completion:]_block_invoke.cold.2
+ ___89-[TSSecureIntentGestureViewController _updateAuthenticationStatus:isDTOEvaluationFailed:]_block_invoke
+ ___89-[TSSecureIntentGestureViewController _updateAuthenticationStatus:isDTOEvaluationFailed:]_block_invoke_2
+ ___94-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:]_block_invoke
+ ___94-[TSTransferListViewController _startInstallMultiplePlans:transferPlans:andCarrierSetupItems:]_block_invoke
+ ___94-[TSTransferListViewController _startInstallMultiplePlans:transferPlans:andCarrierSetupItems:]_block_invoke_2
+ ___95-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handleActivatedItemUpdate:]_block_invoke
+ ___95-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handleActivatedItemUpdate:]_block_invoke.cold.1
+ ___97-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeDeleteTransferBackItem:]_block_invoke
+ ___99-[TSEnableTableViewController(UITableViewDataSource) selectRowAtIndexPath:animated:scrollPosition:]_block_invoke
+ ___DisembarkUILibraryCore_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e35_B32?0"CTCellularPlanItem"8Q16^B24l
+ ___block_descriptor_32_e37_q24?0"NSIndexPath"8"NSIndexPath"16l
+ ___block_descriptor_32_e37_v24?0"BSProcessHandle"8"NSError"16l
+ ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_32_e42_v28?0i8"NSDictionary"12"NSDictionary"20l
+ ___block_descriptor_32_e51_q24?0"CTCellularPlanItem"8"CTCellularPlanItem"16l
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e41_v24?0"CTPlanTravelDetails"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_40_e8_32w_e26_v16?0"UIViewController"8lw32l8
+ ___block_descriptor_40_e8_32w_e79_v32?0"NSDictionary"8"NSDictionary"16?<v?i"NSDictionary""NSDictionary">24lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0C8lw32l8
+ ___block_descriptor_44_e5_v8?0l
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e41_v24?0"CTPlanTravelDetails"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e46_v32?0"CTRemoteDeviceList"8B16B20"NSError"24lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e41_v24?0"CTPlanTravelDetails"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e23_v16?0"UIAlertAction"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e8_v12?0B8ls32l8w40l8
+ ___block_descriptor_49_e8_32bs40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_49_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_49_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e26_v16?0"UIViewController"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e35_v24?0"NSString"8"NSDictionary"16lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e41_v24?0"CTPlanTravelDetails"8"NSError"16lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e50_v24?0"CTXPCServiceSubscriptionInfo"8"NSError"16lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v16?0q8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e8_v12?0B8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSArray"8lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e26_v16?0"UIViewController"8lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e8_v12?0B8ls48l8s32l8s40l8w56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8w56l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0ls48l8s32l8s40l8w56l8
+ ___block_descriptor_66_e8_32s40s48bs56w_e8_v12?0B8lw56l8s48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e8_v12?0B8lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.105
+ ___block_literal_global.117
+ ___block_literal_global.118
+ ___block_literal_global.120
+ ___block_literal_global.137
+ ___block_literal_global.216
+ ___block_literal_global.285
+ ___block_literal_global.301
+ ___block_literal_global.35
+ ___block_literal_global.37
+ ___block_literal_global.39
+ ___block_literal_global.393
+ ___block_literal_global.46
+ ___block_literal_global.48
+ ___block_literal_global.483
+ ___block_literal_global.486
+ ___block_literal_global.49
+ ___block_literal_global.50
+ ___block_literal_global.53
+ ___block_literal_global.544
+ ___block_literal_global.648
+ ___block_literal_global.67
+ ___block_literal_global.678
+ ___block_literal_global.71
+ ___block_literal_global.738
+ ___block_literal_global.80
+ ___block_literal_global.82
+ ___block_literal_global.85
+ ___block_literal_global.86
+ ___getDKPresenterClass_block_invoke
+ ___getDKPresenterClass_block_invoke.cold.1
+ _audit_stringDisembarkUI
+ _dispatch_assert_queue$V2
+ _findPlanInfoWithPlanID
+ _findPlanInfoWithPlanStatus
+ _findPlanInfoWithTargetIccid
+ _findPlanInfoWithTargetIccidHash
+ _findPlanInfoWithoutTargetIccid
+ _getDKPresenterClass.softClass
+ _isFailedState
+ _isPostInstallingOrTerminalState
+ _isProvisioningOngoingState
+ _isSuccessState
+ _isTerminalState
+ _kCAFilterNearest
+ _kScreenLockIconKey
+ _kXMarkIconKey
+ _objc_msgSend$NFCTransferStatus
+ _objc_msgSend$SIMIdentifier
+ _objc_msgSend$UUID
+ _objc_msgSend$_areAllInstallingPlansBeEnabled
+ _objc_msgSend$_areAllPlansInPostInstallOrTerminalState
+ _objc_msgSend$_areAllPlansInTerminalState
+ _objc_msgSend$_cancelTransferringPlan:
+ _objc_msgSend$_collectAllPhoneNumbersForDevice:
+ _objc_msgSend$_constructDCTUrl:withPasscode:
+ _objc_msgSend$_createTargetProxFlowVC
+ _objc_msgSend$_createTransferCloudFlowVC
+ _objc_msgSend$_createTransferFlowVC
+ _objc_msgSend$_createTransferSubFlowVcWithSession:isPostmigrationFlow:
+ _objc_msgSend$_decodeBase64EncodedString:
+ _objc_msgSend$_decodeTransferStatus:
+ _objc_msgSend$_dequeueInteractiveUI
+ _objc_msgSend$_dismissDueToLoadFailure
+ _objc_msgSend$_dismissViewController
+ _objc_msgSend$_displayCarrierSetupViewController:
+ _objc_msgSend$_displayConfirmationCodeViewController:
+ _objc_msgSend$_displayIntermediateViewController:
+ _objc_msgSend$_displayOneTimeCodeViewController:phoneNumber:carrierName:usePin:
+ _objc_msgSend$_displayTermsAndConditionsViewController:mainText:
+ _objc_msgSend$_displayWebsheetViewController:
+ _objc_msgSend$_enqueueInteractiveUI:
+ _objc_msgSend$_failIdentityShare
+ _objc_msgSend$_findEligiblePlans:
+ _objc_msgSend$_findPlanInfoWithPlanID:
+ _objc_msgSend$_findPlanInfoWithPlanStatus:
+ _objc_msgSend$_findPlanInfoWithTargetIccid:
+ _objc_msgSend$_findPlanInfoWithTargetIccidHash:
+ _objc_msgSend$_getCarrierNameForDefaultDataSub
+ _objc_msgSend$_getCellularPlanItemForTravelSIM
+ _objc_msgSend$_getDetailsTextWithIccid:
+ _objc_msgSend$_getSubtitleWhenSyncWithTarget:selectedPlansCount:selectedPlansFailedTransferCount:
+ _objc_msgSend$_getTitleWhenSyncWithTarget:selectedPlansCount:selectedPlansFailedTransferCount:
+ _objc_msgSend$_getTraveleSIMStateWithCompletion:
+ _objc_msgSend$_getWebsheetInfo:completion:
+ _objc_msgSend$_handleActivatedItemUpdate:
+ _objc_msgSend$_handleMultiSIMInstallationStatusUpdateEvent:
+ _objc_msgSend$_handlePostInstallItemUpdate:
+ _objc_msgSend$_handleProvisioningItemUpdate:
+ _objc_msgSend$_handleTransferResults:
+ _objc_msgSend$_handleTransferUICapability:
+ _objc_msgSend$_hasAnyPlanSuccessfullyInstalled
+ _objc_msgSend$_installMultipleSelectedPlans
+ _objc_msgSend$_isAnyPlanRequireLocationService
+ _objc_msgSend$_isAnyPlanWithMismatchedActivationPolicy
+ _objc_msgSend$_isFollowUpInstall
+ _objc_msgSend$_launchDisembarkUI:
+ _objc_msgSend$_maybeAutoInstallPendingPlan
+ _objc_msgSend$_maybeClearFirstViewControllerCallback
+ _objc_msgSend$_maybeClearSubFlowViewController:
+ _objc_msgSend$_maybeDismissSelf
+ _objc_msgSend$_maybeDisplayInteractiveUI:
+ _objc_msgSend$_maybeDisplayNextIntermediateViewController
+ _objc_msgSend$_maybeDisplaySourceDeviceConsentAlert:
+ _objc_msgSend$_maybeFlowCompleted:
+ _objc_msgSend$_maybeHandleConfirmationCodeError:
+ _objc_msgSend$_maybeHandleProvisioningError:items:
+ _objc_msgSend$_maybeMoveToNextItem
+ _objc_msgSend$_maybePresentFirstViewController:
+ _objc_msgSend$_maybeReplyFirstViewControllerCallbackWithViewController:
+ _objc_msgSend$_maybeSendExternalizedContext:isDTOEvaluationFailed:
+ _objc_msgSend$_maybeSendTransferResults
+ _objc_msgSend$_maybeSendTransferUICapability:
+ _objc_msgSend$_maybeSetNavigationController:
+ _objc_msgSend$_maybeStartTimerForNewlyInstalledPlan:newStatus:
+ _objc_msgSend$_maybeSubmitAutoReconnectionDetails
+ _objc_msgSend$_maybeUpdateHomeIccid:homeIccid:
+ _objc_msgSend$_maybeUpdatePhysicalSIMStatus:
+ _objc_msgSend$_maybeUpdatePlanNameForTargetIccid:planName:
+ _objc_msgSend$_maybeUpdatePlanNameWithoutPlanID:
+ _objc_msgSend$_maybeUpdateUserEnabledPlans:
+ _objc_msgSend$_offerFallbackOption
+ _objc_msgSend$_prepareDisplayItems:withPlanItems:
+ _objc_msgSend$_prepareForEnablingItem:
+ _objc_msgSend$_prepareForInstallingItems:
+ _objc_msgSend$_preselectPlanIfNeeded
+ _objc_msgSend$_redirectToBTFlow
+ _objc_msgSend$_refreshContinueButton
+ _objc_msgSend$_refreshTableView
+ _objc_msgSend$_registerMessages
+ _objc_msgSend$_reloadScreen
+ _objc_msgSend$_requireSyncUpTransferResultsWithSource
+ _objc_msgSend$_sendTravelEventMetricForPlan:useLDM:
+ _objc_msgSend$_sendTravelEventMetricForRoaming:
+ _objc_msgSend$_setTravelIccidInfo:
+ _objc_msgSend$_setUpButtons
+ _objc_msgSend$_setUpLearnMoreLink
+ _objc_msgSend$_setUpTableView
+ _objc_msgSend$_setupTableView
+ _objc_msgSend$_shouldOfferFallbackOptionOnError:
+ _objc_msgSend$_shouldWaitUntilPhoneNumberBeReady:completion:
+ _objc_msgSend$_showCancelAlert:withMessage:
+ _objc_msgSend$_showFailureAlert
+ _objc_msgSend$_startInstallMultiplePlans:transferPlans:andCarrierSetupItems:
+ _objc_msgSend$_startNFCIdentityShare
+ _objc_msgSend$_startObserver
+ _objc_msgSend$_statusDescription:info:
+ _objc_msgSend$_stopNFCIdentityShare
+ _objc_msgSend$_subFlowVcWithReconnectionCredentials:
+ _objc_msgSend$_successIdentityShare
+ _objc_msgSend$_updateAuthenticationStatus:isDTOEvaluationFailed:
+ _objc_msgSend$_updateCarrierErrorCode:withPlanID:
+ _objc_msgSend$_updateEnablePlanItems
+ _objc_msgSend$_updateInstallError:withPlanID:webUrl:postData:
+ _objc_msgSend$_updateInstallError:withTargetIccidHash:
+ _objc_msgSend$_updatePlanStatus:forPlanInfo:
+ _objc_msgSend$_updatePlanStatus:withPlanID:
+ _objc_msgSend$_updatePlanStatus:withTargetIccid:
+ _objc_msgSend$_updateTargetIccid:withPlanID:
+ _objc_msgSend$_updateTargetIccidWithoutPlanID:
+ _objc_msgSend$_updateTransferStatus:
+ _objc_msgSend$_updateTrayButtonText:
+ _objc_msgSend$_validCarrierName
+ _objc_msgSend$accessoryViewForStatus:
+ _objc_msgSend$accounts
+ _objc_msgSend$activate
+ _objc_msgSend$activateUsingPreSharedKey:completion:
+ _objc_msgSend$activatingState
+ _objc_msgSend$addSubFlowViewController:
+ _objc_msgSend$addSymbolEffect:
+ _objc_msgSend$allObjects
+ _objc_msgSend$alsPlanCarriers:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendLeftToRightMark:
+ _objc_msgSend$appendString:
+ _objc_msgSend$areAnyPlansOnDevice
+ _objc_msgSend$arePlansAvailable:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$backButtonClicked:
+ _objc_msgSend$backToCurrentTopPane
+ _objc_msgSend$bootstrap:isUsingPreSharedKey:completion:
+ _objc_msgSend$bootstrapPlanTransferUsingMessageSession:flowType:completion:
+ _objc_msgSend$buddyMLViewController
+ _objc_msgSend$bytes
+ _objc_msgSend$cachedPhoneNumber
+ _objc_msgSend$cancelPlanInstallation:completion:
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$carrierErrorCode
+ _objc_msgSend$center
+ _objc_msgSend$clearReconnectionCredentials:
+ _objc_msgSend$compareProductVersion:toProductVersion:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$componentsWithString:
+ _objc_msgSend$configurationWithPointSize:
+ _objc_msgSend$confirmationCodeViewController
+ _objc_msgSend$connectionStarted
+ _objc_msgSend$consolidatedActivatingState
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:
+ _objc_msgSend$continueTransferWithoutWifi:
+ _objc_msgSend$ctClient
+ _objc_msgSend$deactivateCrossPlatformTransport:completion:
+ _objc_msgSend$deactiveCrossPlatformTransport
+ _objc_msgSend$defaultConfig
+ _objc_msgSend$defaultContentConfiguration
+ _objc_msgSend$dequeueReusableCellWithIdentifier:forIndexPath:
+ _objc_msgSend$descriptorWithSubscriptionContext:
+ _objc_msgSend$dictionary
+ _objc_msgSend$disablePredicativeTextForTextField:
+ _objc_msgSend$displayPlan
+ _objc_msgSend$doneAction
+ _objc_msgSend$eSIMTravelState
+ _objc_msgSend$effect
+ _objc_msgSend$establishReconnectionCredentials:completion:
+ _objc_msgSend$establishReconnectionCredentialsUsingMessageSession:completion:
+ _objc_msgSend$evaluateDtoPolicy:
+ _objc_msgSend$externalizedContext
+ _objc_msgSend$firstViewControllerForDisplay
+ _objc_msgSend$flow
+ _objc_msgSend$footerConfiguration
+ _objc_msgSend$formatLocAndConcatenateDescriptors:
+ _objc_msgSend$formattedPhoneNumber
+ _objc_msgSend$fragment
+ _objc_msgSend$getCellularPlanItem:withIccid:
+ _objc_msgSend$getCurrentDataSubscriptionContextSync:
+ _objc_msgSend$getErrorDescription:
+ _objc_msgSend$getProximityTransportSession:remoteDeviceInfo:usePreSharedKey:completion:
+ _objc_msgSend$getTitleAndDetailsForPlanType:transferCapability:isShowingFilteredPlans:carrier:
+ _objc_msgSend$getTravelInfoForIccid:completion:
+ _objc_msgSend$getWordRepresentationForInt:
+ _objc_msgSend$handleStartOverWithEntryPoint:navigationController:completion:
+ _objc_msgSend$handleWaitingOnWifiStatusUpdate:
+ _objc_msgSend$iccidHash
+ _objc_msgSend$identifier
+ _objc_msgSend$imageByApplyingSymbolConfiguration:
+ _objc_msgSend$imageName
+ _objc_msgSend$imageWithCIImage:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$init:
+ _objc_msgSend$initAsMidOperationWithCarrierName:requireGeneralConsent:
+ _objc_msgSend$initShowErrorOnSourceWithPlanIdentifier:
+ _objc_msgSend$initWithAssociatedPlanItem:initialLabel:predefinedUserLabels:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithCode:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithEnablingPlanIccid:
+ _objc_msgSend$initWithEnablingPlanInfo:
+ _objc_msgSend$initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:
+ _objc_msgSend$initWithFlow:navigationController:delegate:
+ _objc_msgSend$initWithIccids:homeIccid:voiceIccid:postArrivalInstallation:
+ _objc_msgSend$initWithInBuddy:transferablePlans:selectedTransferablePlans:alsPlans:selectedAlsPlans:odaPlans:transferPlanCarriers:selectedTransferPlanCarriers:alsPlanCarriers:selectedAlsPlanCarriers:odaPlanCarriers:selectedOdaPlanCarriers:sourceDevicesCount:selectedSourceDevicesCount:
+ _objc_msgSend$initWithInfos:
+ _objc_msgSend$initWithItem:
+ _objc_msgSend$initWithOptions:extractionSource:
+ _objc_msgSend$initWithOptions:navigationController:delegate:
+ _objc_msgSend$initWithPlanIdentifer:
+ _objc_msgSend$initWithPlanInfos:
+ _objc_msgSend$initWithPlanInfos:userEnablePlans:skip:
+ _objc_msgSend$initWithPlanItemError:updatePlanItem:withBackButton:forCarrier:withCarrierErrorCode:isEmbeddedInResultView:
+ _objc_msgSend$initWithPlans:homeIccid:
+ _objc_msgSend$initWithPlans:isSelectedAsTravelSIM:
+ _objc_msgSend$initWithPlans:planItems:fromDataTransferSession:
+ _objc_msgSend$initWithPlans:skip:
+ _objc_msgSend$initWithPlans:skip:isForCrossPlatformTransfer:
+ _objc_msgSend$initWithProximitySetupState:proxPlansFiltered:
+ _objc_msgSend$initWithRetainedObject:isSource:
+ _objc_msgSend$initWithSelectedPlans:confirmCellularPlanTransfer:isForCrossPlatformTransfer:session:sourceOsVersion:
+ _objc_msgSend$initWithSelectedPlansCount:selectedPlansFailedTransferCount:isDisembarkUIRequired:
+ _objc_msgSend$initWithService:
+ _objc_msgSend$initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:
+ _objc_msgSend$initWithSession:sourceOSVersion:proximitySetupState:transferablePlanOnSource:
+ _objc_msgSend$initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:
+ _objc_msgSend$initWithSuccess:skipped:duration:
+ _objc_msgSend$initWithTemplate:
+ _objc_msgSend$initWithTimeoutReason:isEmbeddedInResultView:plans:
+ _objc_msgSend$initWithTitle:details:symbolName:plans:skip:
+ _objc_msgSend$initWithTransferBackPlan:isPostMigrationFlow:
+ _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:allowsMultiSelection:
+ _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:
+ _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:allowsMultiSelection:
+ _objc_msgSend$initWithTransferItems:showOtherOptions:isShowingFilteredPlans:
+ _objc_msgSend$initWithTransferOutPlan:
+ _objc_msgSend$initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isShowingFilteredPlans:
+ _objc_msgSend$initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isStandaloneProximityFlow:transferBackPhoneNumber:isShowingFilteredPlans:
+ _objc_msgSend$initWithURL:postdata:
+ _objc_msgSend$initWithoutTargetSyncAndSelectedPlansCount:
+ _objc_msgSend$installError
+ _objc_msgSend$installMultiplePlans:completionHandler:
+ _objc_msgSend$installationEndTime
+ _objc_msgSend$installationStartTime
+ _objc_msgSend$isActiveDataPlan
+ _objc_msgSend$isDataActive
+ _objc_msgSend$isDataOnly
+ _objc_msgSend$isDisabled
+ _objc_msgSend$isDtoEvaluationRequired
+ _objc_msgSend$isEnterManuallyTapped
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isFlexPolicyOn
+ _objc_msgSend$isGlobalMVNO
+ _objc_msgSend$isIccidForPhySlot:
+ _objc_msgSend$isLanguageRightToLeft
+ _objc_msgSend$isNFCEnable
+ _objc_msgSend$isPhone
+ _objc_msgSend$isPlanInstalledAndNotEnabled:item:
+ _objc_msgSend$isPostMigrationFlow
+ _objc_msgSend$isPreInstalled
+ _objc_msgSend$isPreSharedKeyForReconnectionPresent:completion:
+ _objc_msgSend$isPreSharedKeyPresent
+ _objc_msgSend$isRegRestLocationUnavailable:
+ _objc_msgSend$isRegulatoryRestrictedPlan
+ _objc_msgSend$isSelectable
+ _objc_msgSend$isSelectedAsTravelSIM
+ _objc_msgSend$isSharingIdentitySupportedWithError:
+ _objc_msgSend$isShown
+ _objc_msgSend$isSkipButtonTapped
+ _objc_msgSend$isSource
+ _objc_msgSend$isTraveleSIM
+ _objc_msgSend$isUserInHomeCountry
+ _objc_msgSend$isUserTraveling
+ _objc_msgSend$isUsingPreSharedKey
+ _objc_msgSend$isVinylCapable
+ _objc_msgSend$lightGrayColor
+ _objc_msgSend$limit
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$matchingSim
+ _objc_msgSend$maybePrepareNextDisplayViewController:completion:
+ _objc_msgSend$maybeUpdateTimeoutStatus:
+ _objc_msgSend$nearbyActionExtraData
+ _objc_msgSend$needShow
+ _objc_msgSend$needsToRun:
+ _objc_msgSend$notificationWithName:object:userInfo:
+ _objc_msgSend$numActivePlansOnDevice
+ _objc_msgSend$odaPlanCarriers:
+ _objc_msgSend$openApplication:withOptions:completion:
+ _objc_msgSend$optionsWithDictionary:
+ _objc_msgSend$parseQueryParamsWithTitleDictionary:
+ _objc_msgSend$percentEncodedQuery
+ _objc_msgSend$planError
+ _objc_msgSend$planItem
+ _objc_msgSend$planItemText:
+ _objc_msgSend$planList
+ _objc_msgSend$planName
+ _objc_msgSend$prepareViewController:completion:
+ _objc_msgSend$presentInSettings
+ _objc_msgSend$presentProxCardFlowWithDelegate:initialViewController:
+ _objc_msgSend$pushTimeoutFailureViewControllerWithStatus:forPlan:
+ _objc_msgSend$pushToDetailViewControllerWithError:forPlan:
+ _objc_msgSend$queryItems
+ _objc_msgSend$queryStartSessionRequest:
+ _objc_msgSend$registerRequestID:options:handler:
+ _objc_msgSend$reloadInputViews
+ _objc_msgSend$removeAction:
+ _objc_msgSend$requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:
+ _objc_msgSend$rightAnchor
+ _objc_msgSend$roamingInfo
+ _objc_msgSend$rootFlow
+ _objc_msgSend$safeAreaLayoutGuide
+ _objc_msgSend$saveCellularSettingsForReturnToHome:
+ _objc_msgSend$secondaryText
+ _objc_msgSend$secondaryTextProperties
+ _objc_msgSend$selectedItems
+ _objc_msgSend$selectedPlan
+ _objc_msgSend$sendRequestID:options:request:responseHandler:
+ _objc_msgSend$sendTravelBuddyCAEvent:error:
+ _objc_msgSend$set
+ _objc_msgSend$setActivityIndicatorHidden:
+ _objc_msgSend$setAllowsInlineMediaPlayback:
+ _objc_msgSend$setAssociatedIccid:
+ _objc_msgSend$setBorderColor:
+ _objc_msgSend$setBorderWidth:
+ _objc_msgSend$setBuddyMLViewController:
+ _objc_msgSend$setCarrierErrorCode:
+ _objc_msgSend$setCenter:
+ _objc_msgSend$setConfirmationCodeViewController:
+ _objc_msgSend$setContentConfiguration:
+ _objc_msgSend$setContentMode:
+ _objc_msgSend$setCornerRadius:
+ _objc_msgSend$setDctDelegate:
+ _objc_msgSend$setDefaults
+ _objc_msgSend$setDidProcessDCTCode:
+ _objc_msgSend$setDoneAction:
+ _objc_msgSend$setESIMTravelState:
+ _objc_msgSend$setEditing:
+ _objc_msgSend$setEnable:
+ _objc_msgSend$setFragment:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setInstallError:
+ _objc_msgSend$setInstallationEndTime:
+ _objc_msgSend$setInstallationStartTime:
+ _objc_msgSend$setIsDataOnly:
+ _objc_msgSend$setIsDisabled:
+ _objc_msgSend$setIsDtoEvaluationSucceeded:
+ _objc_msgSend$setIsFlexPolicyOn:
+ _objc_msgSend$setIsPreSharedKeyPresent:
+ _objc_msgSend$setIsSecureIntentSucceeded:
+ _objc_msgSend$setIsSkipButtonTapped:
+ _objc_msgSend$setIsUserInHomeCountry:
+ _objc_msgSend$setLowDataMode:enable:
+ _objc_msgSend$setMagnificationFilter:
+ _objc_msgSend$setMasksToBounds:
+ _objc_msgSend$setModalTransitionStyle:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$setPhoneNumber:
+ _objc_msgSend$setPlanItem:
+ _objc_msgSend$setPlanName:
+ _objc_msgSend$setQuery:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$setSecondaryText:
+ _objc_msgSend$setSectionFooterHeight:
+ _objc_msgSend$setSectionHeaderHeight:
+ _objc_msgSend$setSeparatorColor:
+ _objc_msgSend$setSeparatorStyle:
+ _objc_msgSend$setShouldAdjustButtonTrayForKeyboard:
+ _objc_msgSend$setSimCapability:
+ _objc_msgSend$setSmartDashesType:
+ _objc_msgSend$setSmartInsertDeleteType:
+ _objc_msgSend$setSmartQuotesType:
+ _objc_msgSend$setSpellCheckingType:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setSubFlowViewControllers:
+ _objc_msgSend$setSupportedRegionCodes:
+ _objc_msgSend$setTitleColor:forState:
+ _objc_msgSend$setUseTravelOnly:
+ _objc_msgSend$setViewDelegate:
+ _objc_msgSend$setWaitForPhoneNumber:
+ _objc_msgSend$setWebsheetUrl:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$setupConstraints
+ _objc_msgSend$setupViewsWithTag:delegate:
+ _objc_msgSend$setupWithDelegate:indexPath:
+ _objc_msgSend$sha256
+ _objc_msgSend$shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:
+ _objc_msgSend$showAlert
+ _objc_msgSend$skipButton
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$sourceDevicesCount:
+ _objc_msgSend$sourceOSVersion
+ _objc_msgSend$startSharingIdentity:
+ _objc_msgSend$stopSharingIdentity
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringFromNumber:
+ _objc_msgSend$subFlowViewControllers
+ _objc_msgSend$submitAutoReconnectionDetails
+ _objc_msgSend$submitAutoReconnectionDetails:
+ _objc_msgSend$submitAutoReconnectionDetails:completion:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$systemGray6Color
+ _objc_msgSend$systemLightGrayColor
+ _objc_msgSend$tableView:didSelectRowAtIndexPath:
+ _objc_msgSend$targetIccid
+ _objc_msgSend$targetIccidHash
+ _objc_msgSend$textProperties
+ _objc_msgSend$timerWithTimeInterval:target:selector:userInfo:repeats:
+ _objc_msgSend$transferablePlanCarriers:
+ _objc_msgSend$travelOnlySelected
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateCellularPlanProperties:appName:appType:completionHandler:
+ _objc_msgSend$updateInstallationStatus:forPlanID:
+ _objc_msgSend$updateRasterizationScale:
+ _objc_msgSend$updateSecureIntentData:isDTOEvaluationFailed:
+ _objc_msgSend$updateSecureIntentData:isDTOEvaluationFailed:error:
+ _objc_msgSend$updateTableHeightAnchor
+ _objc_msgSend$updateTargetIccidInfo:
+ _objc_msgSend$useTravelOnly
+ _objc_msgSend$value
+ _objc_msgSend$viewDelegate
+ _objc_msgSend$waitForPhoneNumber
- +[TSFlowHelper handleStartOverAgainstNoPlan:navigationController:completion:]
- +[TSSIMSetupFlow initActivationCodeRequireSetup:]
- +[TSSIMSetupFlow initWithActivationCodeOnlyFlow]
- +[TSSIMSetupFlow initWithSetupFlowWithIccid:showAddPlan:]
- +[TSSIMSetupFlow initWithSetupFlowWithIccid:showAddPlan:forceDualSIMSetup:]
- +[TSSinglePlanTransferViewController getTitleAndDetailsForPlanType:transferCapability:]
- +[TSSinglePlanTransferViewController getTitleAndDetailsForPlanType:transferCapability:].cold.1
- -[CrossPlatformTransferOngoingViewController .cxx_destruct]
- -[CrossPlatformTransferOngoingViewController _promptWithDeviceName:phoneNumber:]
- -[CrossPlatformTransferOngoingViewController _setUpLabel]
- -[CrossPlatformTransferOngoingViewController _setUpSpinner]
- -[CrossPlatformTransferOngoingViewController _spinnerStartAnimating]
- -[CrossPlatformTransferOngoingViewController _spinnerStopAnimating]
- -[CrossPlatformTransferOngoingViewController delegate]
- -[CrossPlatformTransferOngoingViewController initWithPhoneNumber:]
- -[CrossPlatformTransferOngoingViewController label]
- -[CrossPlatformTransferOngoingViewController maybeDismissAlert]
- -[CrossPlatformTransferOngoingViewController maybeDismissAlert].cold.1
- -[CrossPlatformTransferOngoingViewController maybeDismissAlert].cold.2
- -[CrossPlatformTransferOngoingViewController phoneNumber]
- -[CrossPlatformTransferOngoingViewController setDelegate:]
- -[CrossPlatformTransferOngoingViewController setLabel:]
- -[CrossPlatformTransferOngoingViewController setPhoneNumber:]
- -[CrossPlatformTransferOngoingViewController setShowAlert:]
- -[CrossPlatformTransferOngoingViewController setSpinner:]
- -[CrossPlatformTransferOngoingViewController showAlert]
- -[CrossPlatformTransferOngoingViewController spinner]
- -[CrossPlatformTransferOngoingViewController viewDidAppear:]
- -[CrossPlatformTransferOngoingViewController viewDidDisappear:]
- -[CrossPlatformTransferOngoingViewController viewDidLoad]
- -[CrossPlatformTransferSourceSelectionWarningViewController initWithPeerDeviceName:]
- -[SSCrossPlatformTransferSourceSelectionViewController _continueButtonTapped:].cold.1
- -[SSCrossPlatformTransferSourceSelectionViewController initWithPlans:planItems:device:]
- -[SSProximityDevice activate:]
- -[SSProximityDevice skEventFromDictionary:]
- -[SSScanViewController detailLabel]
- -[SSScanViewController setDetailLabel:]
- -[SSScanViewController setTitleLabel:]
- -[SSScanViewController titleLabel]
- -[TSAuthFlow descriptor]
- -[TSAuthFlow firstViewController]
- -[TSAuthFlow initWithExternalizedContext:descriptor:isLocalConvertFlow:]
- -[TSAuthFlow setDescriptor:]
- -[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]
- -[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:].cold.1
- -[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]
- -[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:].cold.1
- -[TSCellularPlanActivatingFlow _handleOtpStatusUpdate:]
- -[TSCellularPlanActivatingFlow _isAppInBackground]
- -[TSCellularPlanActivatingFlow _maybeDeleteTransferBackItem:]
- -[TSCellularPlanActivatingFlow _maybeMoveToNextViewController]
- -[TSCellularPlanActivatingFlow _onTransferError:]
- -[TSCellularPlanActivatingFlow _shouldWaitUntilPhoneNumberBeReady:]
- -[TSCellularPlanActivatingFlow _startedByFollowup]
- -[TSCellularPlanActivatingFlow carrierErrorCode]
- -[TSCellularPlanActivatingFlow carrierName]
- -[TSCellularPlanActivatingFlow currentActivatingState]
- -[TSCellularPlanActivatingFlow failureWebsheetError]
- -[TSCellularPlanActivatingFlow firstViewController:]
- -[TSCellularPlanActivatingFlow firstViewController]
- -[TSCellularPlanActivatingFlow firstViewController].cold.1
- -[TSCellularPlanActivatingFlow initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:delayStartActivatingTimer:]
- -[TSCellularPlanActivatingFlow installingPlanIdentifier]
- -[TSCellularPlanActivatingFlow launchWebsheet:completion:]
- -[TSCellularPlanActivatingFlow launchWebsheet:completion:].cold.1
- -[TSCellularPlanActivatingFlow nextViewControllerFrom:]
- -[TSCellularPlanActivatingFlow offerFallbackOption]
- -[TSCellularPlanActivatingFlow phoneNumber]
- -[TSCellularPlanActivatingFlow planActiveOnSource]
- -[TSCellularPlanActivatingFlow planInstallError]
- -[TSCellularPlanActivatingFlow planItemsUpdated:planListError:]
- -[TSCellularPlanActivatingFlow planItemsUpdated:planListError:].cold.1
- -[TSCellularPlanActivatingFlow planItemsUpdated:planListError:].cold.2
- -[TSCellularPlanActivatingFlow planItemsUpdated:planListError:].cold.3
- -[TSCellularPlanActivatingFlow planItemsUpdated:planListError:].cold.4
- -[TSCellularPlanActivatingFlow planName]
- -[TSCellularPlanActivatingFlow redirectToBTFlow]
- -[TSCellularPlanActivatingFlow setCarrierErrorCode:]
- -[TSCellularPlanActivatingFlow setCarrierName:]
- -[TSCellularPlanActivatingFlow setCurrentActivatingState:]
- -[TSCellularPlanActivatingFlow setDefaultNavigationItems:]
- -[TSCellularPlanActivatingFlow setFailureWebsheetError:]
- -[TSCellularPlanActivatingFlow setInstallingPlanIdentifier:]
- -[TSCellularPlanActivatingFlow setPhoneNumber:]
- -[TSCellularPlanActivatingFlow setPlanActiveOnSource:]
- -[TSCellularPlanActivatingFlow setPlanInstallError:]
- -[TSCellularPlanActivatingFlow setPlanName:]
- -[TSCellularPlanActivatingFlow setShouldShowCompletePaneOnTimeout:]
- -[TSCellularPlanActivatingFlow setShowConfirmationCodePane:]
- -[TSCellularPlanActivatingFlow setSourceIccid:]
- -[TSCellularPlanActivatingFlow setStartTime:]
- -[TSCellularPlanActivatingFlow setSubscriptionContextUUID:]
- -[TSCellularPlanActivatingFlow setTopViewController:]
- -[TSCellularPlanActivatingFlow setTransferError:]
- -[TSCellularPlanActivatingFlow setTransferState:]
- -[TSCellularPlanActivatingFlow setUpdatePlanItem:]
- -[TSCellularPlanActivatingFlow setWaitForPhoneNumber:]
- -[TSCellularPlanActivatingFlow shouldOfferFallbackOptionOnError:]
- -[TSCellularPlanActivatingFlow shouldShowCompletePaneOnTimeout]
- -[TSCellularPlanActivatingFlow showConfirmationCodePane]
- -[TSCellularPlanActivatingFlow simSetupFlowCompleted:]
- -[TSCellularPlanActivatingFlow sourceIccid]
- -[TSCellularPlanActivatingFlow startTime]
- -[TSCellularPlanActivatingFlow subscriptionContextUUID]
- -[TSCellularPlanActivatingFlow transferError]
- -[TSCellularPlanActivatingFlow transferEventUpdate:]
- -[TSCellularPlanActivatingFlow transferState]
- -[TSCellularPlanActivatingFlow updatePlanItem]
- -[TSCellularPlanActivatingFlow userDidTapCancel]
- -[TSCellularPlanActivatingFlow waitForPhoneNumber]
- -[TSCellularPlanCardInfoViewController .cxx_destruct]
- -[TSCellularPlanCardInfoViewController addNewPlanWithUserInfo:]
- -[TSCellularPlanCardInfoViewController canBeShownFromSuspendedState]
- -[TSCellularPlanCardInfoViewController configureCell:atIndexPath:]
- -[TSCellularPlanCardInfoViewController delegate]
- -[TSCellularPlanCardInfoViewController enterActivationLabel]
- -[TSCellularPlanCardInfoViewController infoTableViewHeightConstraint]
- -[TSCellularPlanCardInfoViewController infoTableView]
- -[TSCellularPlanCardInfoViewController init]
- -[TSCellularPlanCardInfoViewController keyboardWasShown:]
- -[TSCellularPlanCardInfoViewController keyboardWillBeHidden:]
- -[TSCellularPlanCardInfoViewController onError]
- -[TSCellularPlanCardInfoViewController resetFirstResponder]
- -[TSCellularPlanCardInfoViewController scrollViewForKeyboardIfNecessary]
- -[TSCellularPlanCardInfoViewController scrollView]
- -[TSCellularPlanCardInfoViewController setDelegate:]
- -[TSCellularPlanCardInfoViewController setEnterActivationLabel:]
- -[TSCellularPlanCardInfoViewController setInfoTableView:]
- -[TSCellularPlanCardInfoViewController setInfoTableViewHeightConstraint:]
- -[TSCellularPlanCardInfoViewController setScrollView:]
- -[TSCellularPlanCardInfoViewController tableView:cellForRowAtIndexPath:]
- -[TSCellularPlanCardInfoViewController tableView:heightForRowAtIndexPath:]
- -[TSCellularPlanCardInfoViewController tableView:numberOfRowsInSection:]
- -[TSCellularPlanCardInfoViewController textField:shouldChangeCharactersInRange:replacementString:]
- -[TSCellularPlanCardInfoViewController textFieldDidBeginEditing:]
- -[TSCellularPlanCardInfoViewController textFieldDidEndEditing:]
- -[TSCellularPlanCardInfoViewController textFieldShouldReturn:]
- -[TSCellularPlanCardInfoViewController viewDidAppear:]
- -[TSCellularPlanCardInfoViewController viewDidLayoutSubviews]
- -[TSCellularPlanCardInfoViewController viewDidLoad]
- -[TSCellularPlanCardInfoViewController viewWillAppear:]
- -[TSCellularPlanCardInfoViewController viewWillDisappear:]
- -[TSCellularPlanConfirmationCodeViewController .cxx_destruct]
- -[TSCellularPlanConfirmationCodeViewController canBeShownFromSuspendedState]
- -[TSCellularPlanConfirmationCodeViewController codeTextField]
- -[TSCellularPlanConfirmationCodeViewController confirm:]
- -[TSCellularPlanConfirmationCodeViewController confirmationCodeMessageLabel]
- -[TSCellularPlanConfirmationCodeViewController confirmationCodeTitleLabel]
- -[TSCellularPlanConfirmationCodeViewController confirmationCode]
- -[TSCellularPlanConfirmationCodeViewController delegate]
- -[TSCellularPlanConfirmationCodeViewController initAsMidOperationWithCarrierName:]
- -[TSCellularPlanConfirmationCodeViewController initWithCardData:]
- -[TSCellularPlanConfirmationCodeViewController setCodeTextField:]
- -[TSCellularPlanConfirmationCodeViewController setConfirmationCodeMessageLabel:]
- -[TSCellularPlanConfirmationCodeViewController setConfirmationCodeTitleLabel:]
- -[TSCellularPlanConfirmationCodeViewController setDelegate:]
- -[TSCellularPlanConfirmationCodeViewController textField:shouldChangeCharactersInRange:replacementString:]
- -[TSCellularPlanConfirmationCodeViewController textFieldShouldBeginEditing:]
- -[TSCellularPlanConfirmationCodeViewController textFieldShouldReturn:]
- -[TSCellularPlanConfirmationCodeViewController userDidTapCancel]
- -[TSCellularPlanConfirmationCodeViewController viewDidAppear:]
- -[TSCellularPlanConfirmationCodeViewController viewDidLoad]
- -[TSCellularPlanConfirmationCodeViewController viewWillDisappear:]
- -[TSCellularPlanLabelPickerTableViewController .cxx_destruct]
- -[TSCellularPlanLabelPickerTableViewController _doneButtonTapped]
- -[TSCellularPlanLabelPickerTableViewController associatedPlanItem]
- -[TSCellularPlanLabelPickerTableViewController chosenLabelIndexPath]
- -[TSCellularPlanLabelPickerTableViewController chosenLabel]
- -[TSCellularPlanLabelPickerTableViewController customLabelIndexPath]
- -[TSCellularPlanLabelPickerTableViewController customLabelRowValue]
- -[TSCellularPlanLabelPickerTableViewController customLabel]
- -[TSCellularPlanLabelPickerTableViewController init]
- -[TSCellularPlanLabelPickerTableViewController initialLabel]
- -[TSCellularPlanLabelPickerTableViewController numberOfSectionsInTableView:]
- -[TSCellularPlanLabelPickerTableViewController predefinedUserLabels]
- -[TSCellularPlanLabelPickerTableViewController setAssociatedPlanItem:]
- -[TSCellularPlanLabelPickerTableViewController setChosenLabelIndexPath:]
- -[TSCellularPlanLabelPickerTableViewController setCustomLabel:]
- -[TSCellularPlanLabelPickerTableViewController setInitialLabel:]
- -[TSCellularPlanLabelPickerTableViewController setPredefinedUserLabels:]
- -[TSCellularPlanLabelPickerTableViewController tableView:cellForRowAtIndexPath:]
- -[TSCellularPlanLabelPickerTableViewController tableView:didSelectRowAtIndexPath:]
- -[TSCellularPlanLabelPickerTableViewController tableView:numberOfRowsInSection:]
- -[TSCellularPlanLabelPickerTableViewController tableView:titleForHeaderInSection:]
- -[TSCellularPlanLabelPickerTableViewController textFieldDidEndEditing:]
- -[TSCellularPlanLabelPickerTableViewController viewWillAppear:]
- -[TSCellularPlanLabelsViewController heightAnchor]
- -[TSCellularPlanLabelsViewController setHeightAnchor:]
- -[TSCellularPlanProximityTransferController launchSecureIntentUI:descriptor:isLocalConvertFlow:completion:]
- -[TSCellularPlanScanViewController .cxx_destruct]
- -[TSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]
- -[TSCellularPlanScanViewController btLearnMore]
- -[TSCellularPlanScanViewController canBeShownFromSuspendedState]
- -[TSCellularPlanScanViewController captureOutput:didOutputMetadataObjects:fromConnection:]
- -[TSCellularPlanScanViewController confirmationCodeRequired]
- -[TSCellularPlanScanViewController cutoutView]
- -[TSCellularPlanScanViewController delegate]
- -[TSCellularPlanScanViewController didChangeValueForKey:]
- -[TSCellularPlanScanViewController drawQRBox:]
- -[TSCellularPlanScanViewController enterDetailsManuallyButton]
- -[TSCellularPlanScanViewController enterFauxCardDataManually:]
- -[TSCellularPlanScanViewController entryPoint]
- -[TSCellularPlanScanViewController fauxCardData]
- -[TSCellularPlanScanViewController initWithBackButton:]
- -[TSCellularPlanScanViewController learnMoreTapped:]
- -[TSCellularPlanScanViewController makeCGPoint:]
- -[TSCellularPlanScanViewController manualCardInfoEntry]
- -[TSCellularPlanScanViewController positionQRCodeLabel]
- -[TSCellularPlanScanViewController presentViewController:animated:completion:]
- -[TSCellularPlanScanViewController scanQRCodeLabel]
- -[TSCellularPlanScanViewController scanView]
- -[TSCellularPlanScanViewController scannerView]
- -[TSCellularPlanScanViewController setBtLearnMore:]
- -[TSCellularPlanScanViewController setCutoutView:]
- -[TSCellularPlanScanViewController setDelegate:]
- -[TSCellularPlanScanViewController setEnterDetailsManuallyButton:]
- -[TSCellularPlanScanViewController setEntryPoint:]
- -[TSCellularPlanScanViewController setPositionQRCodeLabel:]
- -[TSCellularPlanScanViewController setScanQRCodeLabel:]
- -[TSCellularPlanScanViewController setScanView:]
- -[TSCellularPlanScanViewController setScannerView:]
- -[TSCellularPlanScanViewController startScanning]
- -[TSCellularPlanScanViewController transferViaQRCode]
- -[TSCellularPlanScanViewController viewDidDisappear:]
- -[TSCellularPlanScanViewController viewDidLayoutSubviews]
- -[TSCellularPlanScanViewController viewDidLoad]
- -[TSCellularPlanScanViewController viewWillAppear:]
- -[TSCellularPlanScanViewController viewWillTransitionToSize:withTransitionCoordinator:]
- -[TSCellularSetupActivatingViewController _setUpLabel]
- -[TSCellularSetupActivatingViewController _setUpSpinner]
- -[TSCellularSetupActivatingViewController _setupLabelContraint]
- -[TSCellularSetupActivatingViewController _spinnerStartAnimating]
- -[TSCellularSetupActivatingViewController _spinnerStopAnimating]
- -[TSCellularSetupActivatingViewController details]
- -[TSCellularSetupActivatingViewController initWithTitle:details:symbolName:]
- -[TSCellularSetupActivatingViewController initWithTransferOutPlan:toDevice:]
- -[TSCellularSetupActivatingViewController init]
- -[TSCellularSetupActivatingViewController setDetails:]
- -[TSCellularSetupActivatingViewController viewDidDisappear:]
- -[TSCellularSetupCompleteViewController initWithPhoneNumber:planName:planActiveOnSource:]
- -[TSCellularSetupCompleteViewController initWithPlanIdentifer:deviceName:]
- -[TSCellularSetupLoadingViewController loadingView]
- -[TSCellularSetupLoadingViewController setLoadingView:]
- -[TSCellularSetupTimeoutFailureViewController initWithTimeoutReason:]
- -[TSCoreTelephonyClientCache bootstrapPlanTransferUsingMessageSession:completion:]
- -[TSCoreTelephonyClientCache updateSecureIntentData:]
- -[TSCrossPlatformSourceAuthFlow _connectToDevice:completion:].cold.1
- -[TSCrossPlatformSourceAuthFlow _showAlert]
- -[TSCrossPlatformSourceAuthFlow init]
- -[TSCrossPlatformSourceTransferFlow init]
- -[TSCrossPlatformTargetAuthFlow initWithDeviceName:]
- -[TSCrossPlatformTargetTransferFlow deviceName]
- -[TSCrossPlatformTargetTransferFlow initWithDeviceName:]
- -[TSCrossPlatformTargetTransferFlow phoneNumber]
- -[TSCrossPlatformTargetTransferFlow setDeviceName:]
- -[TSCrossPlatformTargetTransferFlow setPhoneNumber:]
- -[TSIDSTransferFlow isWebsheetFlow]
- -[TSIDSTransferFlow launchSecureIntentUI:descriptor:isLocalConvertFlow:completion:]
- -[TSIDSTransferFlow setIsWebsheetFlow:]
- -[TSMidOperationFailureViewController initWithPlanItemError:updatePlanItem:withBackButton:forCarrier:withCarrierErrorCode:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:]
- -[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:].cold.1
- -[TSNoPlanForTransferViewController _scanButtonTapped]
- -[TSPRXSIMTransferCompleteViewController init]
- -[TSProximityTargetTransferFlow initWithTransferBackPlan:]
- -[TSProximityTargetTransferFlow nextViewControllerFrom:].cold.1
- -[TSQRCodeScanFlow viewControllerDidComplete:]
- -[TSSIMSetupFlow getRootFlow]
- -[TSSIMSetupFlow getRootFlow].cold.1
- -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:]
- -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:].cold.1
- -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:].cold.2
- -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:].cold.3
- -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:].cold.4
- -[TSSecureIntentGestureViewController _maybeSendExternalizedContext:].cold.5
- -[TSSecureIntentGestureViewController _updateAuthenticationStatus:]
- -[TSSecureIntentGestureViewController descriptor]
- -[TSSecureIntentGestureViewController initWithExternalizedContext:descriptor:isLocalConvertFlow:]
- -[TSSecureIntentGestureViewController setDescriptor:]
- -[TSSecureIntentGestureViewController setIsSecureIntentFailed:]
- -[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]
- -[TSSinglePlanTransferViewController initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:]
- -[TSSinglePlanTransferViewController initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isStandaloneProximityFlow:transferBackPhoneNumber:]
- -[TSSubFlowViewController initWithFlow:navigationController:]
- -[TSSubFlowViewController initWithOptions:navigationController:]
- -[TSTransferCloudFlow initWithProximitySetupState:]
- -[TSTransferFlow initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:]
- -[TSTransferFlowModel arePlansAvailable:transferablePlanOnSource:bootstrapOnly:completion:]
- -[TSTransferFlowModel bootstrap:completion:]
- -[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]
- -[TSTransferListViewController _heightAnchorConstant]
- -[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]
- -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:]
- -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:]
- -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:]
- -[TSTransferListViewController tableView:willSelectRowAtIndexPath:]
- -[TSWebsheetSignupFlow _showFailureAlert:completion:]
- -[TSWebsheetSignupFlow viewControllerDidComplete:]
- -[TSWebsheetViewController sendRequest:]
- GCC_except_table22
- GCC_except_table29
- GCC_except_table60
- GCC_except_table72
- GCC_except_table73
- _CGRectContainsRect
- _CGRectIntersectsRect
- _OBJC_CLASS_$_CrossPlatformTransferOngoingViewController
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_TSCellularPlanCardInfoViewController
- _OBJC_CLASS_$_TSCellularPlanConfirmationCodeViewController
- _OBJC_CLASS_$_TSCellularPlanLabelPickerTableViewController
- _OBJC_CLASS_$_TSCellularPlanScanViewController
- _OBJC_CLASS_$_UIFontDescriptor
- _OBJC_IVAR_$_CrossPlatformTransferOngoingViewController._delegate
- _OBJC_IVAR_$_CrossPlatformTransferOngoingViewController._label
- _OBJC_IVAR_$_CrossPlatformTransferOngoingViewController._phoneNumber
- _OBJC_IVAR_$_CrossPlatformTransferOngoingViewController._showAlert
- _OBJC_IVAR_$_CrossPlatformTransferOngoingViewController._spinner
- _OBJC_IVAR_$_SSScanViewController._detailLabel
- _OBJC_IVAR_$_SSScanViewController._titleLabel
- _OBJC_IVAR_$_TSAuthFlow._descriptor
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._carrierErrorCode
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._carrierName
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._currentActivatingState
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._failureWebsheetError
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._installingPlanIdentifier
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._phoneNumber
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._planActiveOnSource
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._planInstallError
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._planName
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._shouldShowCompletePaneOnTimeout
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._showConfirmationCodePane
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._sourceIccid
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._startTime
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._subscriptionContextUUID
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._transferError
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._transferState
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._updatePlanItem
- _OBJC_IVAR_$_TSCellularPlanActivatingFlow._waitForPhoneNumber
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._activeTextField
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._delegate
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._enterActivationLabel
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._fauxCardData
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._infoTableView
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._infoTableViewHeightConstraint
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._keyboardSize
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._nextButton
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._scrollView
- _OBJC_IVAR_$_TSCellularPlanCardInfoViewController._tableData
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._cancelButton
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._carrierName
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._codeTextField
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._confirmationCode
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._confirmationCodeMessageLabel
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._confirmationCodeTitleLabel
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._delegate
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._fauxCardData
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._isMidOperation
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._nextButton
- _OBJC_IVAR_$_TSCellularPlanConfirmationCodeViewController._userConsentResponse
- _OBJC_IVAR_$_TSCellularPlanLabelPickerTableViewController._associatedPlanItem
- _OBJC_IVAR_$_TSCellularPlanLabelPickerTableViewController._chosenLabelIndexPath
- _OBJC_IVAR_$_TSCellularPlanLabelPickerTableViewController._customLabel
- _OBJC_IVAR_$_TSCellularPlanLabelPickerTableViewController._initialLabel
- _OBJC_IVAR_$_TSCellularPlanLabelPickerTableViewController._predefinedUserLabels
- _OBJC_IVAR_$_TSCellularPlanLabelsViewController._heightAnchor
- _OBJC_IVAR_$_TSCellularPlanScanViewController._btLearnMore
- _OBJC_IVAR_$_TSCellularPlanScanViewController._confirmationCodeRequired
- _OBJC_IVAR_$_TSCellularPlanScanViewController._cutoutView
- _OBJC_IVAR_$_TSCellularPlanScanViewController._delegate
- _OBJC_IVAR_$_TSCellularPlanScanViewController._enterDetailsManuallyButton
- _OBJC_IVAR_$_TSCellularPlanScanViewController._entryPoint
- _OBJC_IVAR_$_TSCellularPlanScanViewController._fauxCardData
- _OBJC_IVAR_$_TSCellularPlanScanViewController._holeOutlineLayer
- _OBJC_IVAR_$_TSCellularPlanScanViewController._manualCardInfoEntry
- _OBJC_IVAR_$_TSCellularPlanScanViewController._nextTimeToAcceptScan
- _OBJC_IVAR_$_TSCellularPlanScanViewController._positionQRCodeLabel
- _OBJC_IVAR_$_TSCellularPlanScanViewController._scanQRCodeLabel
- _OBJC_IVAR_$_TSCellularPlanScanViewController._scanView
- _OBJC_IVAR_$_TSCellularPlanScanViewController._scannerView
- _OBJC_IVAR_$_TSCellularPlanScanViewController._transferViaQRCode
- _OBJC_IVAR_$_TSCellularPlanScanViewController._withBackButton
- _OBJC_IVAR_$_TSCellularSetupActivatingViewController._details
- _OBJC_IVAR_$_TSCellularSetupLoadingViewController._loadingView
- _OBJC_IVAR_$_TSCrossPlatformTargetAuthFlow._deviceName
- _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._deviceName
- _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._phoneNumber
- _OBJC_IVAR_$_TSIDSTransferFlow._isWebsheetFlow
- _OBJC_IVAR_$_TSPRXPasscodeEntryViewController._delegate
- _OBJC_IVAR_$_TSSecureIntentGestureViewController._descriptor
- _OBJC_IVAR_$_TSSecureIntentGestureViewController._isSecureIntentFailed
- _OBJC_IVAR_$_TSTransferListViewController._tableHeightAnchor
- _OBJC_METACLASS_$_CrossPlatformTransferOngoingViewController
- _OBJC_METACLASS_$_TSCellularPlanCardInfoViewController
- _OBJC_METACLASS_$_TSCellularPlanConfirmationCodeViewController
- _OBJC_METACLASS_$_TSCellularPlanLabelPickerTableViewController
- _OBJC_METACLASS_$_TSCellularPlanScanViewController
- _TSDelayStartActivatingTimerKey
- _TSHasLocalPlanKey
- _TSHostViewControllerKey
- _TSIsLocalConvertKey
- _TSUserInfoCarrierName
- _UIEdgeInsetsZero
- _UIFontTextStyleTitle0
- _UIFontTextStyleTitle1
- __OBJC_$_CATEGORY_INSTANCE_METHODS_CTDisplayPlan_$_SimSetup
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UIViewController_$_InModalPresentation
- __OBJC_$_CATEGORY_NSString_$_QRCode
- __OBJC_$_CATEGORY_UIViewController_$_InModalPresentation
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
- __OBJC_$_CLASS_PROP_LIST_TSCellularPlanScanViewController
- __OBJC_$_INSTANCE_METHODS_CrossPlatformTransferOngoingViewController
- __OBJC_$_INSTANCE_METHODS_NSString(QRCode|PhoneNumber)
- __OBJC_$_INSTANCE_METHODS_OBHeaderView(SSHelper|SSHelper|SSHelper)
- __OBJC_$_INSTANCE_METHODS_TSCellularPlanActivatingFlow
- __OBJC_$_INSTANCE_METHODS_TSCellularPlanCardInfoViewController
- __OBJC_$_INSTANCE_METHODS_TSCellularPlanConfirmationCodeViewController
- __OBJC_$_INSTANCE_METHODS_TSCellularPlanLabelPickerTableViewController
- __OBJC_$_INSTANCE_METHODS_TSCellularPlanScanViewController
- __OBJC_$_INSTANCE_METHODS_TSCellularSetupActivatingViewController
- __OBJC_$_INSTANCE_METHODS_TSCellularSetupCompleteViewController
- __OBJC_$_INSTANCE_METHODS_TSCellularSetupTimeoutFailureViewController
- __OBJC_$_INSTANCE_METHODS_TSMidOperationFailureViewController
- __OBJC_$_INSTANCE_METHODS_TSNoPlanForTransferViewController
- __OBJC_$_INSTANCE_METHODS_UILabel(RangeBold|RangeBold|RangeBold|RangeBold)
- __OBJC_$_INSTANCE_VARIABLES_CrossPlatformTransferOngoingViewController
- __OBJC_$_INSTANCE_VARIABLES_TSCellularPlanCardInfoViewController
- __OBJC_$_INSTANCE_VARIABLES_TSCellularPlanConfirmationCodeViewController
- __OBJC_$_INSTANCE_VARIABLES_TSCellularPlanLabelPickerTableViewController
- __OBJC_$_INSTANCE_VARIABLES_TSCellularPlanScanViewController
- __OBJC_$_PROP_LIST_CrossPlatformTransferOngoingViewController
- __OBJC_$_PROP_LIST_TSCellularPlanActivatingFlow
- __OBJC_$_PROP_LIST_TSCellularPlanCardInfoViewController
- __OBJC_$_PROP_LIST_TSCellularPlanConfirmationCodeViewController
- __OBJC_$_PROP_LIST_TSCellularPlanLabelPickerTableViewController
- __OBJC_$_PROP_LIST_TSCellularPlanScanViewController
- __OBJC_$_PROP_LIST_TSNoPlanForTransferViewController
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding
- __OBJC_CLASS_PROTOCOLS_$_CrossPlatformTransferOngoingViewController
- __OBJC_CLASS_PROTOCOLS_$_TSCellularPlanActivatingFlow
- __OBJC_CLASS_PROTOCOLS_$_TSCellularPlanCardInfoViewController
- __OBJC_CLASS_PROTOCOLS_$_TSCellularPlanConfirmationCodeViewController
- __OBJC_CLASS_PROTOCOLS_$_TSCellularPlanLabelPickerTableViewController
- __OBJC_CLASS_PROTOCOLS_$_TSCellularPlanScanViewController
- __OBJC_CLASS_PROTOCOLS_$_TSNoPlanForTransferViewController
- __OBJC_CLASS_RO_$_CrossPlatformTransferOngoingViewController
- __OBJC_CLASS_RO_$_TSCellularPlanCardInfoViewController
- __OBJC_CLASS_RO_$_TSCellularPlanConfirmationCodeViewController
- __OBJC_CLASS_RO_$_TSCellularPlanLabelPickerTableViewController
- __OBJC_CLASS_RO_$_TSCellularPlanScanViewController
- __OBJC_LABEL_PROTOCOL_$_NSCoding
- __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
- __OBJC_METACLASS_RO_$_CrossPlatformTransferOngoingViewController
- __OBJC_METACLASS_RO_$_TSCellularPlanCardInfoViewController
- __OBJC_METACLASS_RO_$_TSCellularPlanConfirmationCodeViewController
- __OBJC_METACLASS_RO_$_TSCellularPlanLabelPickerTableViewController
- __OBJC_METACLASS_RO_$_TSCellularPlanScanViewController
- __OBJC_PROTOCOL_$_NSCoding
- __OBJC_PROTOCOL_$_NSSecureCoding
- ___101-[TSTransferFlow initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:]_block_invoke
- ___30-[SSProximityDevice activate:]_block_invoke
- ___30-[SSProximityDevice activate:]_block_invoke.1
- ___30-[SSProximityDevice activate:]_block_invoke.1.cold.1
- ___30-[SSProximityDevice activate:]_block_invoke.cold.1
- ___39-[SSScanViewController decodeMetadata:]_block_invoke.47
- ___43-[TSCrossPlatformSourceAuthFlow _showAlert]_block_invoke
- ___43-[TSCrossPlatformSourceAuthFlow _showAlert]_block_invoke_2
- ___44-[TSTransferFlowModel requestCarrierSetups:]_block_invoke.39
- ___46-[TSPRXSIMTransferCompleteViewController init]_block_invoke
- ___49-[TSTransferCloudFlowModel requestCarrierSetups:]_block_invoke.34
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.29
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.29.cold.1
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.29.cold.2
- ___50-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke.23
- ___50-[TSWebsheetSignupFlow viewControllerDidComplete:]_block_invoke
- ___51-[TSCellularPlanActivatingFlow offerFallbackOption]_block_invoke
- ___51-[TSCellularPlanActivatingFlow offerFallbackOption]_block_invoke_2
- ___51-[TSCellularPlanActivatingFlow offerFallbackOption]_block_invoke_3
- ___51-[TSCellularPlanActivatingFlow offerFallbackOption]_block_invoke_4
- ___51-[TSProximitySourceTransferFlow _bootstrapTransfer]_block_invoke.118
- ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.16
- ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.16.cold.1
- ___53-[TSCrossPlatformTargetAuthFlow firstViewController:]_block_invoke.16.cold.2
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.198
- ___53-[TSWebsheetSignupFlow _showFailureAlert:completion:]_block_invoke
- ___54-[TSCellularPlanActivatingFlow simSetupFlowCompleted:]_block_invoke
- ___54-[TSCellularPlanActivatingFlow simSetupFlowCompleted:]_block_invoke.73
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.24
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.24.cold.1
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.25
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.25.cold.1
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.26
- ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.34
- ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.34.cold.1
- ___56-[TSCellularPlanConfirmationCodeViewController confirm:]_block_invoke
- ___57-[TSCrossPlatformTargetTransferFlow firstViewController:]_block_invoke.17
- ___58-[TSCellularPlanActivatingFlow launchWebsheet:completion:]_block_invoke
- ___58-[TSCellularPlanActivatingFlow launchWebsheet:completion:]_block_invoke_2
- ___58-[TSCellularPlanActivatingFlow launchWebsheet:completion:]_block_invoke_2.cold.1
- ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke.73
- ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.cold.1
- ___61-[TSCellularPlanActivatingFlow _maybeDeleteTransferBackItem:]_block_invoke
- ___62-[TSCellularPlanActivatingFlow _maybeMoveToNextViewController]_block_invoke
- ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.160
- ___63-[TSCellularPlanActivatingFlow planItemsUpdated:planListError:]_block_invoke
- ___63-[TSCellularPlanActivatingFlow planItemsUpdated:planListError:]_block_invoke.cold.1
- ___63-[TSCellularPlanCardInfoViewController addNewPlanWithUserInfo:]_block_invoke
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.93
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.93.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.94
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.94.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.95
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.95.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.96
- ___64-[TSCellularPlanConfirmationCodeViewController userDidTapCancel]_block_invoke
- ___64-[TSCellularPlanConfirmationCodeViewController userDidTapCancel]_block_invoke_2
- ___64-[TSPRXSIMTransferringViewController _setupOneTimeCodeDetection]_block_invoke.56
- ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke.187
- ___66-[TSRecommendedCarrierAppsFlow _requestCarrierAppsWithCompletion:]_block_invoke_2.cold.1
- ___66-[TSRecommendedCarrierAppsFlow _requestCarrierAppsWithCompletion:]_block_invoke_2.cold.2
- ___67-[TSCellularPlanActivatingFlow _shouldWaitUntilPhoneNumberBeReady:]_block_invoke
- ___67-[TSCellularPlanActivatingFlow _shouldWaitUntilPhoneNumberBeReady:]_block_invoke.cold.1
- ___67-[TSSecureIntentGestureViewController _updateAuthenticationStatus:]_block_invoke
- ___67-[TSSecureIntentGestureViewController _updateAuthenticationStatus:]_block_invoke_2
- ___70-[TSCellularSetupLoadingViewController safariViewControllerDidFinish:]_block_invoke.86
- ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.104
- ___73-[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]_block_invoke
- ___73-[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]_block_invoke.cold.1
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.98
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.98.cold.1
- ___76-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke
- ___76-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.154
- ___76-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.158
- ___76-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke_2
- ___77+[TSFlowHelper handleStartOverAgainstNoPlan:navigationController:completion:]_block_invoke
- ___77-[TSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke
- ___77-[TSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke.76
- ___77-[TSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke_2
- ___77-[TSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke_2.cold.1
- ___79-[TSCellularSetupLoadingViewController setupCoreTelephonyClientForRemoteSignup]_block_invoke.46
- ___80-[CrossPlatformTransferOngoingViewController _promptWithDeviceName:phoneNumber:]_block_invoke
- ___80-[CrossPlatformTransferOngoingViewController _promptWithDeviceName:phoneNumber:]_block_invoke_2
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.280
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.284
- ___85-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]_block_invoke
- ___85-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]_block_invoke.119
- ___85-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]_block_invoke.cold.1
- ___86-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke
- ___86-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke.41
- ___86-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke_2
- ___86-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke_3
- ___86-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke_4
- ___86-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke_5
- ___87-[TSCellularPlanScanViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
- ___90-[TSCellularPlanScanViewController captureOutput:didOutputMetadataObjects:fromConnection:]_block_invoke
- ___90-[TSCellularPlanScanViewController captureOutput:didOutputMetadataObjects:fromConnection:]_block_invoke.48
- ___90-[TSCellularPlanScanViewController captureOutput:didOutputMetadataObjects:fromConnection:]_block_invoke_2
- ___90-[TSCellularPlanScanViewController captureOutput:didOutputMetadataObjects:fromConnection:]_block_invoke_3
- ___91-[TSTransferFlowModel arePlansAvailable:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke
- ___91-[TSTransferFlowModel arePlansAvailable:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke.cold.1
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8w48l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e26_v16?0"UIViewController"8lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e43_v28?0"CTRemoteDeviceList"8B16"NSError"20lw48l8s40l8s32l8
- ___block_descriptor_57_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSArray"8lw56l8s32l8s40l8s48l8
- ___block_literal_global.115
- ___block_literal_global.127
- ___block_literal_global.200
- ___block_literal_global.255
- ___block_literal_global.286
- ___block_literal_global.29
- ___block_literal_global.293
- ___block_literal_global.31
- ___block_literal_global.33
- ___block_literal_global.36
- ___block_literal_global.38
- ___block_literal_global.40
- ___block_literal_global.41
- ___block_literal_global.433
- ___block_literal_global.460
- ___block_literal_global.47
- ___block_literal_global.513
- ___block_literal_global.68
- ___block_literal_global.96
- _dispatch_get_current_queue
- _objc_msgSend$_cancelTransferringPlan
- _objc_msgSend$_displayOneTimeCodeViewController:carrierName:usePin:
- _objc_msgSend$_displayTermsAndConditionsViewController:
- _objc_msgSend$_maybeDisplayConsent:phoneNumber:completion:
- _objc_msgSend$_maybeMoveToNextViewController
- _objc_msgSend$_maybeSendExternalizedContext:
- _objc_msgSend$_otherButtonTapped
- _objc_msgSend$_promptWithDeviceName:phoneNumber:
- _objc_msgSend$_setUpLabel
- _objc_msgSend$_setUpSpinner
- _objc_msgSend$_setupLabelContraint
- _objc_msgSend$_shouldWaitUntilPhoneNumberBeReady:
- _objc_msgSend$_showAlert
- _objc_msgSend$_spinnerStartAnimating
- _objc_msgSend$_spinnerStopAnimating
- _objc_msgSend$_updateAuthenticationStatus:
- _objc_msgSend$activate:
- _objc_msgSend$addNewPlanWithUserInfo:
- _objc_msgSend$arePlansAvailable:transferablePlanOnSource:bootstrapOnly:completion:
- _objc_msgSend$bootstrap:completion:
- _objc_msgSend$bootstrapPlanTransferForEndpoint:usingMessageSession:completion:
- _objc_msgSend$bootstrapPlanTransferUsingMessageSession:completion:
- _objc_msgSend$btLearnMore
- _objc_msgSend$configureCell:atIndexPath:
- _objc_msgSend$convertRect:toView:
- _objc_msgSend$currentActivatingState
- _objc_msgSend$date
- _objc_msgSend$dateWithTimeIntervalSinceNow:
- _objc_msgSend$enterDetailsManuallyButton
- _objc_msgSend$getProximityTransportSession:remoteDeviceInfo:completion:
- _objc_msgSend$getRootFlow
- _objc_msgSend$getTitleAndDetailsForPlanType:transferCapability:
- _objc_msgSend$handleStartOverAgainstNoPlan:navigationController:completion:
- _objc_msgSend$indexPathWithIndex:
- _objc_msgSend$initWithAllowDismiss:
- _objc_msgSend$initWithDeviceName:
- _objc_msgSend$initWithExternalizedContext:descriptor:isLocalConvertFlow:
- _objc_msgSend$initWithFlow:navigationController:
- _objc_msgSend$initWithInBuddy:transferablePlans:selectedTransferablePlans:alsPlans:selectedAlsPlans:odaPlans:
- _objc_msgSend$initWithOptions:navigationController:
- _objc_msgSend$initWithPeerDeviceName:
- _objc_msgSend$initWithPhoneNumber:planName:planActiveOnSource:
- _objc_msgSend$initWithPlanIdentifer:deviceName:
- _objc_msgSend$initWithPlanItemError:updatePlanItem:withBackButton:forCarrier:withCarrierErrorCode:
- _objc_msgSend$initWithPlans:planItems:device:
- _objc_msgSend$initWithProximitySetupState:
- _objc_msgSend$initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:
- _objc_msgSend$initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:delayStartActivatingTimer:
- _objc_msgSend$initWithTag:delegate:
- _objc_msgSend$initWithTimeoutReason:
- _objc_msgSend$initWithTitle:details:symbolName:
- _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:
- _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:
- _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:
- _objc_msgSend$initWithTransferItems:showOtherOptions:
- _objc_msgSend$initWithTransferOutPlan:toDevice:
- _objc_msgSend$initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:
- _objc_msgSend$initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isStandaloneProximityFlow:transferBackPhoneNumber:
- _objc_msgSend$isContinueByUser
- _objc_msgSend$isWebsheetFlow
- _objc_msgSend$lastBaselineAnchor
- _objc_msgSend$loadingView
- _objc_msgSend$manualCardInfoEntry
- _objc_msgSend$offerFallbackOption
- _objc_msgSend$oneTimeCodeViewController
- _objc_msgSend$origin
- _objc_msgSend$positionQRCodeLabel
- _objc_msgSend$preferredFontDescriptorWithTextStyle:
- _objc_msgSend$redirectToBTFlow
- _objc_msgSend$requestPlans:transferablePlanOnSource:bootstrapOnly:completion:
- _objc_msgSend$requireSetup
- _objc_msgSend$rowHeight
- _objc_msgSend$scrollRectToVisible:animated:
- _objc_msgSend$scrollViewForKeyboardIfNecessary
- _objc_msgSend$sendRequest:
- _objc_msgSend$setAssociatedPlanItem:
- _objc_msgSend$setContentInset:
- _objc_msgSend$setInitialLabel:
- _objc_msgSend$setIsWebsheetFlow:
- _objc_msgSend$setLoadingView:
- _objc_msgSend$setOneTimeCodeViewController:
- _objc_msgSend$setOneTimePasscodePaneShown:
- _objc_msgSend$setPredefinedUserLabels:
- _objc_msgSend$setScrollIndicatorInsets:
- _objc_msgSend$setTableHeaderView:
- _objc_msgSend$setTermsAndConditionsShown:
- _objc_msgSend$setTermsAndConditionsViewController:
- _objc_msgSend$shouldOfferFallbackOptionOnError:
- _objc_msgSend$sourceIccid
- _objc_msgSend$spinnerStopAnimating
- _objc_msgSend$superview
- _objc_msgSend$tableView:heightForRowAtIndexPath:
- _objc_msgSend$takeScreenShot:
- _objc_msgSend$termsAndConditionsViewController
- _objc_msgSend$updateSecureIntentData:
- _printf
- _puts
- _sIsSuccessState
- _sIsTerminateState
CStrings:
+ "\t%@ @%s"
+ " id=%@"
+ " status=%s"
+ "$"
+ "%02x"
+ "%@"
+ "%@ %@"
+ "%@ Wait until phone number to be ready: %{bool}d @%s"
+ "%@ failed : %@ @%s"
+ "%@ in present. enqueue : %@ @%s"
+ "%@ not required @%s"
+ "%@ transfer status %s @%s"
+ "%@_"
+ "%sselect plan : %@ @%s"
+ "&"
+ "*"
+ "* %"
+ "+[TSIdentityShareFlow showAlert]_block_invoke_2"
+ "+[TSSinglePlanTransferViewController getTitleAndDetailsForPlanType:transferCapability:isShowingFilteredPlans:carrier:]"
+ "+[TSUtilities numActivePlansOnDevice]"
+ "-[CrossPlatformManualDetailsViewController _doneButtonTapped]"
+ "-[CrossPlatformManualDetailsViewController _doneButtonTapped]_block_invoke"
+ "-[CrossPlatformManualDetailsViewController tableView:cellForRowAtIndexPath:]"
+ "-[CrossPlatformManualDetailsViewController textFieldShouldReturn:]_block_invoke"
+ "-[SSCardManualEntryViewController addNewPlanWithUserInfo]"
+ "-[SSCardManualEntryViewController tableView:cellForRowAtIndexPath:]"
+ "-[SSCardManualEntryViewController textFieldShouldReturn:]_block_invoke"
+ "-[SSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke_2"
+ "-[SSCellularPlanScanViewController onCodeDetected:completion:]"
+ "-[SSCellularSetupMultiSIMActivatingViewController initWithPlanInfos:]"
+ "-[SSCellularSetupMultiSIMActivatingViewController updateInstallationStatus:forPlanID:]"
+ "-[SSCellularSetupMultiSIMActivatingViewController(TSSetupFlowItem) prepare:]"
+ "-[SSCellularSetupMultiSIMActivatingViewController(UITableViewDataSource) tableView:cellForRowAtIndexPath:]"
+ "-[SSCellularSetupMultiSIMConnectingViewController(TSSetupFlowItem) _areAllPlansInTerminalState]"
+ "-[SSCellularSetupMultiSIMConnectingViewController(TSSetupFlowItem) prepare:]"
+ "-[SSConfirmationCodeViewController confirm:]"
+ "-[SSCrossPlatformTransferSourceSelectionViewController _cancelButtonTapped]"
+ "-[SSCrossPlatformTransferSourceSelectionViewController _cancelButtonTapped]_block_invoke"
+ "-[SSInstallPlanInformation maybeUpdateTimeoutStatus:]"
+ "-[SSMultiSIMResultViewController pushTimeoutFailureViewControllerWithStatus:forPlan:]"
+ "-[SSMultiSIMResultViewController pushToDetailViewControllerWithError:forPlan:]"
+ "-[SSMultiSIMResultViewController tableView:cellForRowAtIndexPath:]"
+ "-[SSMultiSIMResultViewController tableView:didSelectRowAtIndexPath:]"
+ "-[TSActivationPolicyMismatchFlow firstViewController]"
+ "-[TSAuthFlow firstViewController:]"
+ "-[TSBootstrapCrossPlatformTransferFlow firstViewController:]"
+ "-[TSBootstrapCrossPlatformTransferFlow firstViewController:]_block_invoke"
+ "-[TSBootstrapCrossPlatformTransferFlow firstViewController]"
+ "-[TSBootstrapCrossPlatformTransferFlow initWithRetainedObject:isSource:]_block_invoke"
+ "-[TSBootstrapCrossPlatformTransferFlow nextViewControllerFrom:]"
+ "-[TSCellularPlanActivatingFlow _cancelTransferringPlan:]"
+ "-[TSCellularPlanActivatingFlow _cancelTransferringPlan:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow _maybeDisplaySourceDeviceConsentAlert:]"
+ "-[TSCellularPlanActivatingFlow _maybeMoveToNextItem]"
+ "-[TSCellularPlanActivatingFlow _maybePresentFirstViewController:]"
+ "-[TSCellularPlanActivatingFlow _maybePresentFirstViewController:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow _maybeReplyFirstViewControllerCallbackWithViewController:]"
+ "-[TSCellularPlanActivatingFlow _maybeSendTransferUICapability:]"
+ "-[TSCellularPlanActivatingFlow _maybeSendTransferUICapability:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow _maybeStartTimerForNewlyInstalledPlan:newStatus:]"
+ "-[TSCellularPlanActivatingFlow _onInstallError:]"
+ "-[TSCellularPlanActivatingFlow _requireSyncUpTransferResultsWithSource]"
+ "-[TSCellularPlanActivatingFlow initWithSelectedPlans:confirmCellularPlanTransfer:isForCrossPlatformTransfer:session:sourceOsVersion:]"
+ "-[TSCellularPlanActivatingFlow(Consolidated) _areAllPlansInPostInstallOrTerminalState]"
+ "-[TSCellularPlanActivatingFlow(Consolidated) _areAllPlansInTerminalState]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _handleOtpStatusUpdate:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) _offerFallbackOption]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) launchWebsheet:completion:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) transferEventUpdate:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) updateProvisioningError:targetIccidHash:]"
+ "-[TSCellularPlanActivatingFlow(InteractiveUI) _displayCarrierSetupViewController:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(InteractiveUI) _getWebsheetInfo:completion:]"
+ "-[TSCellularPlanActivatingFlow(InteractiveUI) _getWebsheetInfo:completion:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(InteractiveUI) _maybeDisplayInteractiveUI:]"
+ "-[TSCellularPlanActivatingFlow(Override) firstViewController:]"
+ "-[TSCellularPlanActivatingFlow(Override) firstViewController]"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handleActivatedItemUpdate:]"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handleActivatedItemUpdate:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handlePostInstallItemUpdate:]"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _handleProvisioningItemUpdate:]"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeDeleteTransferBackItem:]"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeDeleteTransferBackItem:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeHandleConfirmationCodeError:]"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _maybeHandleProvisioningError:items:]"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) _shouldWaitUntilPhoneNumberBeReady:completion:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(TSCellularPlanManagerCacheDelegate) planItemsUpdated:planListError:]"
+ "-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]"
+ "-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) navigateToNextPaneFrom:navigationController:]"
+ "-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) userDidTapCancel]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]"
+ "-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _maybeUpdatePhysicalSIMStatus:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _maybeUpdatePlanNameForTargetIccid:planName:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _maybeUpdatePlanNameWithoutPlanID:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateCarrierErrorCode:withPlanID:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withTargetIccidHash:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:forPlanInfo:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:withPlanID:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:withTargetIccid:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateTargetIccid:withPlanID:]"
+ "-[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateTargetIccidWithoutPlanID:]"
+ "-[TSCellularPlanLabelsViewController setPendingLabel:forPlanItem:]"
+ "-[TSCellularPlanProximityTransferController launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:]"
+ "-[TSCellularPlanProximityTransferController launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:]_block_invoke"
+ "-[TSCellularSetupActivatingViewController initWithTitle:details:symbolName:plans:skip:]"
+ "-[TSCellularSetupCompleteViewController _continueButtonTapped]"
+ "-[TSCellularSetupCompleteViewController _continueButtonTapped]_block_invoke"
+ "-[TSCoreTelephonyClientCache submitAutoReconnectionDetails:]_block_invoke"
+ "-[TSCoreTelephonyClientCache updateSecureIntentData:isDTOEvaluationFailed:]"
+ "-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke"
+ "-[TSCrossPlatformSourceAuthFlow viewControllerDidComplete:]_block_invoke"
+ "-[TSCrossPlatformSourceTransferFlow firstViewController:]_block_invoke"
+ "-[TSCrossPlatformSourceTransferFlow launchSimSetupForTransferPlanSelection:completion:]_block_invoke_2"
+ "-[TSCrossPlatformTargetAuthFlow deactiveCrossPlatformTransport]_block_invoke"
+ "-[TSCrossPlatformTargetTransferFlow handleCrossplatformSessionResponse:completion:]"
+ "-[TSCrossPlatformTargetTransferFlow handleCrossplatformSessionResponse:completion:]_block_invoke_2"
+ "-[TSCrossPlatformTargetTransferFlow transferEventUpdate:]"
+ "-[TSDeviceInfoViewController tableView:cellForRowAtIndexPath:]"
+ "-[TSEnableTableViewController _areAllInstallingPlansBeEnabled]"
+ "-[TSEnableTableViewController _getTraveleSIMStateWithCompletion:]_block_invoke"
+ "-[TSEnableTableViewController _prepareForEnablingItem:]"
+ "-[TSEnableTableViewController _prepareForInstallingItems:]_block_invoke"
+ "-[TSEnableTableViewController _updateEnablePlanItems]"
+ "-[TSIDSTransferFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:]"
+ "-[TSIdentityShareFlow firstViewController]"
+ "-[TSLowDataModeConfigViewController _continueButtonTapped]"
+ "-[TSLowDataModeConfigViewController _sendTravelEventMetricForPlan:useLDM:]"
+ "-[TSLowDataModeConfigViewController prepare:]"
+ "-[TSLowDataModeConfigViewController prepare:]_block_invoke"
+ "-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke_2"
+ "-[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:isShowingFilteredPlans:]"
+ "-[TSNavigationBarSpinnerManager stopSpinnerInNavigationItem:withIdentifier:]"
+ "-[TSPRXIdentityShareViewController _maybeFlowCompleted:]"
+ "-[TSPRXIdentityShareViewController _startNFCIdentityShare]"
+ "-[TSPRXIdentityShareViewController _startSystemMonitor]_block_invoke_2"
+ "-[TSPRXIdentityShareViewController _stopNFCIdentityShare]"
+ "-[TSPRXIdentityShareViewController _stopSystemMonitor]"
+ "-[TSPRXIdentityShareViewController _unlockScreen]"
+ "-[TSPRXIdentityShareViewController _unlockScreen]_block_invoke"
+ "-[TSPostMigrationFlow _subFlowVcWithReconnectionCredentials:]"
+ "-[TSPostMigrationFlow nextViewControllerFrom:]"
+ "-[TSProximitySourceTransferFlow _handleTransferResults:]"
+ "-[TSProximitySourceTransferFlow _handleTransferUICapability:]"
+ "-[TSProximitySourceTransferFlow _registerMessages]"
+ "-[TSProximitySourceTransferFlow _timerFired]"
+ "-[TSProximitySourceTransferFlow _updateTransferStatus:]"
+ "-[TSProximitySourceTransferFlow firstViewController:]_block_invoke"
+ "-[TSProximitySourceTransferFlow nextViewControllerFrom:]"
+ "-[TSProximityTargetTransferFlow _createTransferSubFlowVcWithSession:isPostmigrationFlow:]"
+ "-[TSRecommendedCarrierAppsFlow _requestCarrierAppsWithCompletion:]_block_invoke_3"
+ "-[TSRoamingEducationViewController _sendTravelEventMetricForRoaming:]"
+ "-[TSSIMSetupFlow _maybeClearSubFlowViewController:]"
+ "-[TSSIMSetupFlow _maybeClearSubFlowViewController:]_block_invoke"
+ "-[TSSIMSetupFlow firstViewControllerForDisplay]"
+ "-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]"
+ "-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke_2"
+ "-[TSSIMSetupFlow rootFlow]"
+ "-[TSSecureIntentGestureViewController _maybeSendExternalizedContext:isDTOEvaluationFailed:]"
+ "-[TSSecureIntentGestureViewController _updateAuthenticationStatus:isDTOEvaluationFailed:]_block_invoke_2"
+ "-[TSSecureIntentGestureViewController evaluateDtoPolicy:]"
+ "-[TSSecureIntentGestureViewController initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:]"
+ "-[TSSourceAutoReconnectTransferFlow firstViewController:]_block_invoke"
+ "-[TSSourceAutoReconnectTransferFlow transferEventUpdate:]"
+ "-[TSSubFlowViewController setDelegate:]"
+ "-[TSTargetReconnectWaitingViewController _skipButtonTapped:]"
+ "-[TSTransferCloudFlow _firstViewController]"
+ "-[TSTransferFlow _firstViewController:]_block_invoke"
+ "-[TSTransferFlow _maybeClearFirstViewControllerCallback]_block_invoke"
+ "-[TSTransferFlow firstViewController]"
+ "-[TSTransferFlowModel arePlansAvailable:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke"
+ "-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]"
+ "-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:]"
+ "-[TSTransferListViewController _installMultipleSelectedPlans]"
+ "-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke"
+ "-[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:]"
+ "-[TSTransferListViewController _startInstallMultiplePlans:transferPlans:andCarrierSetupItems:]"
+ "-[TSTransferListViewController _startPendingInstall:]_block_invoke_3"
+ "-[TSTransferOneTimeCodeViewController _cancelButtonTapped:]_block_invoke"
+ "-[TSTravelBuddyViewController _continueButtonTapped:]"
+ "-[TSTravelBuddyViewController _getDetailsTextWithIccid:]"
+ "-[TSTravelBuddyViewController _getTraveleSIMStateWithCompletion:]"
+ "-[TSTravelBuddyViewController _getTraveleSIMStateWithCompletion:]_block_invoke"
+ "-[TSTravelBuddyViewController _maybeUpdateHomeIccid:homeIccid:]"
+ "-[TSTravelBuddyViewController _setTravelIccidInfo:]"
+ "-[TSTravelBuddyViewController _shouldPlanBeRegisteredForIMessage:]"
+ "-[TSTravelBuddyViewController backToCurrentTopPane]"
+ "-[TSTravelBuddyViewController initWithIccids:homeIccid:voiceIccid:postArrivalInstallation:]"
+ "-[TSTravelBuddyViewController initWithPlans:homeIccid:]"
+ "-[TSTravelBuddyViewController prepare:]"
+ "-[TSTravelBuddyViewController prepare:]_block_invoke"
+ "-[TSTravelBuddyViewController subscriptionInfoDidChange]"
+ "-[TSTravelBuddyViewController tableView:didSelectRowAtIndexPath:]"
+ "-[TSTravelEducationIntroViewController _decodeBase64EncodedString:]"
+ "-[TSTravelModeFlow firstViewController:]"
+ "-[TSTravelModeFlow firstViewController]"
+ "-[TSTravelModeFlow nextViewControllerFrom:]"
+ "-[TSTravelModeIntroViewController _continueButtonTapped]"
+ "-[TSTravelSimCapabilitySelectionViewController _continueButtonTapped:]"
+ "-[TSTravelSimCapabilitySelectionViewController _continueButtonTapped:]_block_invoke"
+ "-[TSTravelSimCapabilitySelectionViewController prepare:]"
+ "-[TSTravelSimCapabilitySelectionViewController prepare:]_block_invoke"
+ "-[TSTravelSimTypeSelectionViewController _continueButtonTapped:]"
+ "."
+ "/"
+ "1/e"
+ "19.0"
+ "3"
+ "6"
+ "8"
+ "<%@ %p"
+ ">"
+ "@\"<DCTCodeDelegate>\""
+ "@\"<TSSIMSetupFlowDelegate>\"16@0:8"
+ "@\"<UITableViewDelegate>\""
+ "@\"CTPlanList\""
+ "@\"NSMutableSet\""
+ "@\"NSSet\""
+ "@\"SSConfirmationCodeViewController\""
+ "@\"SSInstallPlanInformation\""
+ "@\"SSLabelPickerViewController\""
+ "@\"TSBuddyMLViewController\""
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@20@0:8i16"
+ "@28@0:8B16i20i24"
+ "@28@0:8i16i20B24"
+ "@36@0:8q16B24@28"
+ "@44@0:8@16@24B32B36B40"
+ "@44@0:8@16@24Q32B40"
+ "@44@0:8Q16Q24B32@36"
+ "@48@0:8@16B24B28@32@40"
+ "@48@0:8@16B24B28B32B36B40B44"
+ "@52@0:8@16@24@32@40B48"
+ "@56@0:8@16@24B32@36@44B52"
+ "@56@0:8@16B24B28@32@40B48B52"
+ "@60@0:8@16B24B28B32B36B40B44@48B56"
+ "@64@0:8@16B24B28B32@36@44B52B56B60"
+ "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48Q56"
+ "@84@0:8B16q20@28Q36@44B52@56B64@68@76"
+ "ACTIVATE_NEW_ESIM_ALERT_TITLE_WITH_CARRIER_%@"
+ "ACTIVATING"
+ "AND"
+ "AUTO_RECONNECT_COMPLETED_TRANSFER_DETAIL"
+ "AUTO_RECONNECT_COMPLETED_TRANSFER_TITLE"
+ "AUTO_RECONNECT_WAITING_TRANSFER_DETAIL"
+ "AUTO_RECONNECT_WAITING_TRANSFER_TITLE"
+ "AVAILABLE"
+ "Ab"
+ "B32@0:8Q16@24"
+ "B32@?0@\"CTCellularPlanItem\"8Q16^B24"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "BuddyPostMigrationFlow"
+ "BuddyPostMigrationFlow feature disabled @%s"
+ "BuddyPostMigrationFlow feature disabled. Creating TSTransferCloudFlow @%s"
+ "CANCELED"
+ "CARRIER_TRANSFER_ERROR_CODE_MAINTENANCE_FAILURE_%@"
+ "CARRIER_TRANSFER_ERROR_CODE_MAINTENANCE_FAILURE_BUDDY_%@"
+ "CARRIER_TRANSFER_ERROR_CODE_MAINTENANCE_FAILURE_BUDDY_NO_NAME"
+ "CARRIER_TRANSFER_ERROR_CODE_MAINTENANCE_FAILURE_NO_NAME"
+ "CELLULAR_PLAN_ENABLEMENT_SELECTION_FOR_TURN_ON_A_SIM_DETAIL"
+ "CELLULAR_PLAN_ENABLEMENT_SELECTION_FOR_TURN_ON_A_SIM_DETAIL_%@"
+ "CELLULAR_PLAN_ENABLEMENT_SELECTION_FOR_TURN_ON_A_SIM_DETAIL_WITH_PHONE_NUMBER_%@"
+ "CELLULAR_PLAN_ENABLEMENT_SELECTION_FOR_TURN_ON_A_SIM_TITLE"
+ "CELLULAR_PLAN_ENABLEMENT_SELECTION_NO_CHANGE"
+ "CELLULAR_PLAN_ENABLE_MULTI_PLAN_DETAIL"
+ "CELLULAR_PLAN_ENABLE_MULTI_PLAN_TITLE"
+ "CELLULAR_PLAN_ENABLE_ONE_PLAN_DETAIL"
+ "CELLULAR_PLAN_ENABLE_ONE_PLAN_TITLE"
+ "CICode128BarcodeGenerator"
+ "COMMA"
+ "CONFIRMATION_CODE_TITLE"
+ "CONNECTING_TO_NETWORK"
+ "CONTINUE_WITHOUT_WIFI_ALERT_BUTTON_%@"
+ "CONTINUE_WITHOUT_WIFI_ALERT_MESSAGE_%@"
+ "CONTINUE_WITHOUT_WIFI_ALERT_TITLE_%@"
+ "CROSSPLATFORM_INELIGIBLE_DEVICE_MESSAGE"
+ "CROSSPLATFORM_INELIGIBLE_DEVICE_TITLE"
+ "CROSSPLATFORM_NATIVE_CAMERA_DETAIL_WIFI"
+ "CROSSPLATFORM_NATIVE_CAMERA_DETAIL_WLAN"
+ "CROSSPLATFORM_NATIVE_CAMERA_TITLE"
+ "CROSSPLATFORM_TRANSFER_FAIL_ON_SOURCE_NUMBER_CROSSPLATFORM_MODEL"
+ "CROSSPLATFORM_TRANSFER_FAIL_TITLE"
+ "CROSSTRANSFER_CONN_FAIL_GENERAL"
+ "CROSSTRANSFER_CONN_FAIL_GENERAL_MSG"
+ "CROSSTRANSFER_TIMEOUT_DETAIL_WIFI"
+ "CROSSTRANSFER_TIMEOUT_DETAIL_WLAN"
+ "CTCELLULARPLANERROR_AUTHENTICATION_FAILED_MESSAGE"
+ "CTCELLULARPLANERROR_AUTHENTICATION_FAILED_TITLE"
+ "CTCELLULARPLANERROR_TRANSFER_CANCEL_MESSAGE"
+ "CTCELLULARPLANERROR_TRANSFER_CANCEL_TITLE"
+ "CTPlanTransferStatusActivatedNoPhoneNumber"
+ "CTPlanTransferStatusTimeoutInstallOngoing"
+ "CTPlanTransferStatusTimeoutInstalledNoService"
+ "CTPlanTransferStatusTimeoutNotConsented"
+ "CTPlanTravelDetails (%@) @%s"
+ "CTPlanTravelDetails for %@: %@ @%s"
+ "Cancel"
+ "Cancel transfer plan(s) on device id: %@ @%s"
+ "Cannot go back from postInstall to Installing state. @%s"
+ "Cannot query transfer plans and carrier setup items on bootstrap @%s"
+ "CardManualEntry"
+ "CellID"
+ "Cellular plan item %@ is currently registered for iMessage @%s"
+ "ConfirmCellularPlanTransfer"
+ "Consolidated"
+ "CoreTelephonyClientDelegate"
+ "CrossPlatformManualDetailsViewController"
+ "CrossPlatformShowManualDetailsViewController"
+ "CrossPlatformTransferBuddy"
+ "CrossPlatformTransferIntroViewController"
+ "CrossPlatformTransferKey"
+ "DCTCodeDelegate"
+ "DEVICE_INFO_TITLE"
+ "DKPresenter"
+ "DONOT_SHARE"
+ "DOUBLE_CLICK_SIDE_BUTTON_MULTI_PLAN_%@"
+ "DOUBLE_CLICK_SIDE_BUTTON_SINGLE_PLAN_%@"
+ "DTO Evaluation failed @%s"
+ "Default voice iccid is not set. @%s"
+ "Device is already cancelled transfer @%s"
+ "DtoEvaluationRequired"
+ "EID"
+ "ENTER_ACTIVATION_CODE"
+ "ENTER_ACTIVATION_CODE_MESSAGE"
+ "ESIM_AVAILABLE_TO_INSTALL"
+ "ESIM_CAPABILITY_VOICE_DATA_HEADER"
+ "ESIM_IN_STORE_SIGNUP_BUTTON"
+ "ESIM_IN_STORE_SIGNUP_DETAIL"
+ "ESIM_IN_STORE_SIGNUP_TITLE"
+ "ESIM_TYPE_HOME_SIM_OPTION_TEXT"
+ "ESIM_TYPE_HOME_SIM_OPTION_TITLE"
+ "ESIM_TYPE_SELECTION_DETAILS"
+ "ESIM_TYPE_SELECTION_HEADER"
+ "ESIM_TYPE_TRAVEL_SIM_OPTION_TEXT"
+ "ESIM_TYPE_TRAVEL_SIM_OPTION_TITLE"
+ "Enable travel eSIM %@ - error:%@ @%s"
+ "Error no defined cell for index: %@ @%s"
+ "Establishing reconnection credentials @%s"
+ "ExitBuddyIconView"
+ "F"
+ "Flow"
+ "Found a matching cellular plan item %@ @%s"
+ "GSMA_SCAN_DETAIL"
+ "GSMA_SCAN_TITLE"
+ "Home ICCID needs to be updated to %@ @%s"
+ "IMEI"
+ "IMEI2"
+ "IccidToEnable"
+ "InteractiveUI"
+ "IsD2DMigrationSucceedKey"
+ "IsFromDataTransferSession"
+ "IsPostMigrationFlowKey"
+ "IsSourceKey"
+ "IsUsingPreSharedKey"
+ "MAYBE"
+ "MEID"
+ "MIGRATION_COMPLETE_DETAILS"
+ "MIGRATION_COMPLETE_TITLE"
+ "MULTISIM_RESULT_ALL_FAILURE_DETAIL"
+ "MULTISIM_RESULT_ALL_FAILURE_TITLE"
+ "MULTISIM_RESULT_DETAIL"
+ "MULTISIM_RESULT_PENDING"
+ "MULTISIM_RESULT_SOME_FAILURE_DETAIL"
+ "MULTISIM_RESULT_SOME_PENDING_DETAIL"
+ "MULTISIM_RESULT_TITLE"
+ "MULTI_ESIM_TRANSFER_DETAIL"
+ "MULTI_ESIM_TRANSFER_FILTERED_DETAIL"
+ "MULTI_ESIM_TRANSFER_FILTERED_TITLE"
+ "MigrationAuthCode"
+ "MultiplePlanInstallation"
+ "NEW_CELLULAR_PLAN_DETAIL"
+ "NFCTransferStatus"
+ "NFC_RADIO_DISABLED_GOTO_SETTINGS"
+ "NFC_RADIO_DISABLED_OK"
+ "NFC_RADIO_DISABLED_TITLE"
+ "NO_ELIGIBLE_SIMS_MESSAGE"
+ "NO_ELIGIBLE_SIMS_TITLE"
+ "NavigationController"
+ "Next field is first responder: %@ @%s"
+ "No SIM selected @%s"
+ "No matching SODA plan in the plans @%s"
+ "No reconnection credentials @%s"
+ "No remote plans in selection @%s"
+ "Not a single SIM installation. @%s"
+ "Not showing confirmation alert for non vinyl source device @%s"
+ "Otp cancelled : %@ @%s"
+ "Otp cancelled, reset OTC view controller @%s"
+ "Otp valid, reset OTC view controller @%s"
+ "Override"
+ "PASSCODE_CELL_TITLE"
+ "PLAN_TRANSFERRED_DETAIL_%@"
+ "PRXCARD_IN_STORE_ESIM_FAIL_BUTTON"
+ "PRXCARD_IN_STORE_ESIM_FAIL_SUBTITLE"
+ "PRXCARD_IN_STORE_ESIM_FAIL_TITLE"
+ "PRXCARD_IN_STORE_ESIM_LOCKED_SUBTITLE"
+ "PRXCARD_IN_STORE_ESIM_LOCKED_TITLE"
+ "PRXCARD_IN_STORE_ESIM_SUBTITLE"
+ "PRXCARD_IN_STORE_ESIM_SUCCESS_SUBTITLE"
+ "PRXCARD_IN_STORE_ESIM_SUCCESS_TITLE"
+ "PRXCARD_IN_STORE_ESIM_TITLE"
+ "PRXCARD_RECONNECTING_SUBTITLE"
+ "PRXCARD_RECONNECTING_TITLE"
+ "PRXCARD_SOURCE_COMPLETE_MULTIPLE_TITLE"
+ "PRXCARD_SOURCE_COMPLETE_SINGLE_TITLE"
+ "PRXCARD_TARGET_TRANSFER_ALL_FAILED_DETAIL"
+ "PRXCARD_TARGET_TRANSFER_COMPLETE_MULTIPLE_DETAIL"
+ "PRXCARD_TARGET_TRANSFER_COMPLETE_SINGLE_DETAIL"
+ "PRXCARD_TARGET_TRANSFER_COMPLETE_TITLE"
+ "PRXCARD_TARGET_TRANSFER_FAILED_DETAIL_%@"
+ "PRXCARD_TARGET_TRANSFER_FAILED_TITLE"
+ "PRXCARD_TARGET_TRANSFER_SINGLE_FAILED_DETAIL"
+ "PRXFlowDelegate"
+ "PSIM_CAPABILITY_VOICE_DATA_HEADER"
+ "PSIM_TYPE_HOME_SIM_OPTION_TEXT"
+ "PSIM_TYPE_SELECTION_DETAILS"
+ "PSIM_TYPE_SELECTION_HEADER"
+ "PSIM_TYPE_TRAVEL_SIM_OPTION_TEXT"
+ "PlanId"
+ "PlanInstallStatus"
+ "PlanStatus"
+ "Plans"
+ "Plans info does not exist. @%s"
+ "PreSharedKey present: %d @%s"
+ "ProductVersion"
+ "ProxPlansFilteredKey"
+ "READY"
+ "RECONNECT_PRX_TRANSFER_DETAIL"
+ "RECONNECT_PRX_TRANSFER_TITLE"
+ "Resetting didUserClickContinue @%s"
+ "Results"
+ "SESSION_ID_CELL_TITLE"
+ "SETUP_FAILED"
+ "SETUP_LOADING_MESSAGE"
+ "SHA256"
+ "SHARE"
+ "SIM %@ is not enabled - plan status to not enabled @%s"
+ "SIMIdentifier"
+ "SIM_CAPABILITY_DATA_ONLY_TEXT"
+ "SIM_CAPABILITY_DATA_ONLY_TITLE"
+ "SIM_CAPABILITY_VOICE_DATA_OPTION_TEXT"
+ "SIM_CAPABILITY_VOICE_DATA_OPTION_TITLE"
+ "SIM_CAPABILITY_VOICE_DATA_TITLE"
+ "SINGLE_ESIM_TRANSFER_FILTERED_DETAIL"
+ "SINGLE_ESIM_TRANSFER_FILTERED_TITLE"
+ "SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_INELIGIBLE_DETAIL_%@"
+ "SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_MISSING_CERTIFICATE"
+ "SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_MISSING_CERTIFICATE_%@"
+ "SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_REGULATORY_RESTRICTED"
+ "SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_UNKNOWN_LOCATION"
+ "SOURCE_MANUAL_ENTRY_DETAILS"
+ "SOURCE_MANUAL_ENTRY_SPINNER_TEXT"
+ "SOURCE_MANUAL_ENTRY_TITLE"
+ "SS"
+ "SSCardManualEntryViewController"
+ "SSCellularPlanScanViewController"
+ "SSCellularSetupMultiSIMActivatingViewController"
+ "SSCellularSetupMultiSIMConnectingViewController"
+ "SSConfirmationCodeViewController"
+ "SSCrossPlatformScanViewController"
+ "SSInstallPlanInformation"
+ "SSLabelPickerViewController"
+ "SSLimitedSelectableTableView"
+ "SSManualEntryCell"
+ "SSMultiSIMResultViewController"
+ "SSPRXD2DMigrationDoneViewController"
+ "SecureIntentRequired"
+ "Setting travel iccid info for %@ @%s"
+ "Showing travel buddy pane from post arrival notification @%s"
+ "Single"
+ "Skip for CTRemotePlan @%s"
+ "Skip showing enablement pane for travel eSIM @%s"
+ "Skip showing travel buddy pane @%s"
+ "Skip waiting for phone number to be ready for iccid %@ @%s"
+ "Skipping reconnection @%s"
+ "Solarium"
+ "SourceOSVersion"
+ "SubFlow"
+ "SupportsSyncTransferResults"
+ "SwiftUI"
+ "T@\"<DCTCodeDelegate>\",W,V_dctDelegate"
+ "T@\"<TSSIMSetupFlowDelegate>\",W"
+ "T@\"<TSSIMSetupFlowDelegate>\",W,Vdelegate"
+ "T@\"<UITableViewDelegate>\",W,N,V_viewDelegate"
+ "T@\"CTCellularPlanItem\",&,V_planItem"
+ "T@\"CTDisplayPlan\",&,V_displayPlan"
+ "T@\"CTDisplayPlan\",R,V_selectedPlan"
+ "T@\"CTPlan\",&,V_carrierSetupPlan"
+ "T@\"CTPlanList\",&,V_planList"
+ "T@\"CUMessageSession\",&,V_messageSession"
+ "T@\"CoreTelephonyClient\",&,N,V_ctClient"
+ "T@\"NSArray\",&,N,V_descriptors"
+ "T@\"NSArray\",&,V_allPlans"
+ "T@\"NSArray\",&,V_dctInfo"
+ "T@\"NSArray\",&,V_descriptors"
+ "T@\"NSArray\",&,V_installInfos"
+ "T@\"NSArray\",&,V_planItems"
+ "T@\"NSArray\",&,V_plans"
+ "T@\"NSArray\",&,V_selectedItems"
+ "T@\"NSArray\",&,VcachedButtons"
+ "T@\"NSDictionary\",&,N,V_options"
+ "T@\"NSDictionary\",&,V_peerDeviceInfo"
+ "T@\"NSDictionary\",&,V_queryParamToTitle"
+ "T@\"NSError\",&,V_installError"
+ "T@\"NSError\",&,V_planError"
+ "T@\"NSMutableArray\",&,V_installingPlanInfos"
+ "T@\"NSMutableArray\",&,V_pendingInteractiveViewControllers"
+ "T@\"NSMutableArray\",&,V_subFlowViewControllers"
+ "T@\"NSMutableArray\",&,V_userEnabledPlanInfos"
+ "T@\"NSMutableSet\",&,V_cancelledDeviceIDs"
+ "T@\"NSMutableSet\",&,V_displayedDeviceIDs"
+ "T@\"NSNumber\",&,V_eSIMTravelState"
+ "T@\"NSSet\",&,V_originalEnabledPlans"
+ "T@\"NSString\",&,N,V_details"
+ "T@\"NSString\",&,N,V_detailtitle"
+ "T@\"NSString\",&,N,V_formatedDescriptor"
+ "T@\"NSString\",&,V_defaultVoiceIccid"
+ "T@\"NSString\",&,V_enablingIccid"
+ "T@\"NSString\",&,V_iccidToEnable"
+ "T@\"NSString\",&,V_sourceOSVersion"
+ "T@\"NSString\",&,V_sourceOsVersion"
+ "T@\"NSString\",&,V_targetIccid"
+ "T@\"NSString\",&,V_targetIccidHash"
+ "T@\"NSString\",&,V_travelSIM"
+ "T@\"NSString\",&,V_websheetUrl"
+ "T@\"NSString\",R"
+ "T@\"NSTimer\",&,V_timer"
+ "T@\"NSURL\",&,V_roamingInfo"
+ "T@\"OBLinkTrayButton\",&,V_otherOptionsButton"
+ "T@\"PKGlyphView\",&,V_nfcAnimationView"
+ "T@\"PRXAction\",&,N,V_doneAction"
+ "T@\"PRXAction\",&,V_cancelAction"
+ "T@\"PRXAction\",&,V_retryAction"
+ "T@\"PRXAction\",&,V_unlockAction"
+ "T@\"SSConfirmationCodeViewController\",W,V_confirmationCodeViewController"
+ "T@\"SSLabelPickerViewController\",&,V_labelPickerViewController"
+ "T@\"TSBuddyMLViewController\",W,V_buddyMLViewController"
+ "T@\"TSSIMSetupFlow\",R"
+ "T@\"UIImageView\",&,N,V_triangleImageView"
+ "T@\"UITableViewHeaderFooterView\",&,N,V_footer"
+ "T@\"UITextField\",&,V_codeTextField"
+ "T@\"UIView\",&,VspinnerContainer"
+ "T@\"UIViewController\",W,V_presentedViewController"
+ "T@\"UIViewController<TSSetupFlowItem>\",&,V_firstViewController"
+ "TARGET_MANUAL_DETAILS_DETAIL"
+ "TARGET_MANUAL_DETAILS_TITLE"
+ "TB,N,V_isFlexPolicyOn"
+ "TB,R,V_allPlansInstallComplete"
+ "TB,V_allPlansActivated"
+ "TB,V_areAllPlansTransferedOut"
+ "TB,V_confirmCellularPlanTransfer"
+ "TB,V_dctPrewarmSucceded"
+ "TB,V_didProcessDCTCode"
+ "TB,V_didUserClickContinue"
+ "TB,V_isCancelButtonTapped"
+ "TB,V_isDataOnly"
+ "TB,V_isDataOnlySelected"
+ "TB,V_isDeviceIdentifierPresent"
+ "TB,V_isDeviceInfo"
+ "TB,V_isDisabled"
+ "TB,V_isDisembarkUIRequired"
+ "TB,V_isDtoEvaluationRequired"
+ "TB,V_isDtoEvaluationSucceeded"
+ "TB,V_isEnterManuallyTapped"
+ "TB,V_isFlexPolicyOn"
+ "TB,V_isForCrossPlatformTransfer"
+ "TB,V_isFromDataTransferSession"
+ "TB,V_isNFCDataSuccessTransfer"
+ "TB,V_isPhysical"
+ "TB,V_isPostMigrationFlow"
+ "TB,V_isPreInstalled"
+ "TB,V_isPreSharedKeyPresent"
+ "TB,V_isProxFlowShown"
+ "TB,V_isSecureIntentRequired"
+ "TB,V_isSecureIntentSucceeded"
+ "TB,V_isSelectedAsTravelSIM"
+ "TB,V_isShown"
+ "TB,V_isSkipButtonTapped"
+ "TB,V_isSource"
+ "TB,V_isSyncWithTargetResults"
+ "TB,V_isUserInHomeCountry"
+ "TB,V_isUsingPreSharedKey"
+ "TB,V_needShow"
+ "TB,V_skip"
+ "TB,V_supportsSyncTransferResults"
+ "TB,V_tappedLearnMore"
+ "TB,V_transferablePlanOnSource"
+ "TB,V_travelOnlySelected"
+ "TB,V_useTravelOnly"
+ "TQ,N,V_limit"
+ "TQ,V_NFCTransferStatus"
+ "TQ,V_planEnablementState"
+ "TQ,V_proximitySetupState"
+ "TQ,V_status"
+ "TRANSFER"
+ "TRANSFER_ESIMS_DETAIL_%@"
+ "TRANSFER_FAILED"
+ "TRANSFER_INELIGIBLE_PLANS"
+ "TRANSFER_INELIGIBLE_PLANS_DETAIL"
+ "TRANSFER_PLAN_ITEM_DETAIL_REGULATORY_RESTRICTED"
+ "TRANSFER_PLAN_LABELS_SECTION_FOOTER_UNKNOWN_LOCATION"
+ "TRANSFER_SPEED_BUMP_TITLE_%lu"
+ "TRANSFER_TARGET_TITLE_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_AND_HOME_ESIM_TITLE"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_AND_HOME_PSIM_TITLE"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_TITLE"
+ "TRAVEL_BUDDY_TRAVEL_PSIM_AND_HOME_ESIM_TITLE"
+ "TRAVEL_BUDDY_TRAVEL_PSIM_AND_HOME_PSIM_TITLE"
+ "TRAVEL_BUDDY_TRAVEL_PSIM_ONLY_TITLE"
+ "TRAVEL_ESIM_SETUP_COMPLETE_ABROAD_DETAILS"
+ "TRAVEL_ESIM_SETUP_COMPLETE_ABROAD_DETAILS_DATA_NO_INFO"
+ "TRAVEL_ESIM_SETUP_COMPLETE_ABROAD_DETAILS_NO_INFO"
+ "TRAVEL_ESIM_SETUP_COMPLETE_ABROAD_TITLE"
+ "TRAVEL_ESIM_SETUP_COMPLETE_DETAILS_%@"
+ "TRAVEL_ESIM_SETUP_COMPLETE_TITLE"
+ "TRAVEL_LEARN_MORE"
+ "TRAVEL_MODE_DATA_ROAMING_DESCRIPTION"
+ "TRAVEL_MODE_DATA_ROAMING_LABEL"
+ "TRAVEL_MODE_DATA_ROAMING_LABEL_%@"
+ "TRAVEL_MODE_DATA_ROAMING_ON"
+ "TRAVEL_MODE_LDM_BODY"
+ "TRAVEL_MODE_LDM_BUTTON"
+ "TRAVEL_MODE_LDM_TITLE"
+ "TRAVEL_MODE_PRE_DEPARTURE_BODY_%@"
+ "TRAVEL_MODE_PRE_DEPARTURE_BODY_ABROAD"
+ "TRAVEL_MODE_PRE_DEPARTURE_TITLE"
+ "TRAVEL_MODE_PURCHASE_ESIM_DESCRIPTION"
+ "TRAVEL_MODE_PURCHASE_ESIM_LABEL"
+ "TRAVEL_MODE_PURCHASE_PSIM_DESCRIPTION"
+ "TRAVEL_MODE_PURCHASE_PSIM_LABEL"
+ "TRAVEL_MODE_ROAMING_EDUCATION_BODY"
+ "TRAVEL_MODE_ROAMING_EDUCATION_TITLE"
+ "TRAVEL_MODE_ROAMING_ON_WARNING_LEARN_MORE"
+ "TRAVEL_PSIM_SETUP_COMPLETE_ABROAD_DETAILS_DATA_NO_INFO"
+ "TRAVEL_PSIM_SETUP_COMPLETE_ABROAD_DETAILS_NO_INFO"
+ "TRAVEL_PSIM_SETUP_COMPLETE_ABROAD_TITLE"
+ "TSBootstrapCrossPlatformTransferFlow"
+ "TSDeviceInfoCell"
+ "TSDeviceInfoViewController"
+ "TSEnableTableViewController"
+ "TSIdentityShareFlow"
+ "TSIdentityShareViewController"
+ "TSLowDataModeConfigViewController"
+ "TSPRXIdentityShareViewController"
+ "TSPRXReconnectWaitingViewController"
+ "TSPostMigrationFlow"
+ "TSRoamingEducationViewController"
+ "TSSourceAutoReconnectTransferFlow"
+ "TSSourceAutoReconnectTransferredViewController"
+ "TSSourceAutoReconnectWaitingViewController"
+ "TSTargetReconnectWaitingViewController"
+ "TSTravelBuddyViewController"
+ "TSTravelModeFlow"
+ "TSTravelModeIntroViewController"
+ "TSTravelSimCapabilitySelectionViewController"
+ "TSTravelSimTypeSelectionViewController"
+ "TSUserInfoRetainReference"
+ "Td,V_installationEndTime"
+ "Td,V_installationStartTime"
+ "Td,V_waitingStartTime"
+ "Ti,V_numSelectedPlansNotTransferredOut"
+ "Ti,V_selectedPlansCount"
+ "Ti,V_selectedPlansFailedTransferCount"
+ "Ti,V_selectedTransferPlansCount"
+ "Time to complete activating for plan type %tu with result %tu, duration: %f  @%s"
+ "TransferResults"
+ "TransferUICapability"
+ "Travel eSIM is installed while abroad and it's the only SIM @%s"
+ "Try finding from installing plans info @%s"
+ "UITableViewCell"
+ "UNABLE_TO_TRANSFER"
+ "UUID"
+ "Unknown"
+ "UpdatePlanInfo"
+ "Updating SIM property failed with [%@] @%s"
+ "User chose to keep travel & home SIMs. @%s"
+ "User chose to keep travel SIM only. @%s"
+ "User has chosen this SIM to be %@ @%s"
+ "Using bootstrap @%s"
+ "Using bootstrap: %d, on wifi:%d @%s"
+ "ViewLifeCycle"
+ "WAITING"
+ "WLAN"
+ "Wait for launchSimSetupForTransferPlanSelection call from CT @%s"
+ "Wait until user makes a decision @%s"
+ "WaitingOnWifiStatus"
+ "WebsheetInfoKey"
+ "WiFi"
+ "[Db] %s with completionType:%ld @%s"
+ "[Db] After sort : %@ @%s"
+ "[Db] Before sort : %@ @%s"
+ "[Db] Start NFC @%s"
+ "[Db] Stop NFC @%s"
+ "[Db] register cu.message @%s"
+ "[Db] requesting unlock @%s"
+ "[Db] set label:%@ for item:%@, uuid:%@ @%s"
+ "[Db] something weird happend. unexpected top vc:%@ @%s"
+ "[Db] unlock canceled @%s"
+ "[E]%@ has no mdn, carrier, label @%s"
+ "[E]%@-%@ provisioning error: %@ @%s"
+ "[E]Barcode length > view width! @%s"
+ "[E]Could not find matching cellular plan item for travel SIM @%s"
+ "[E]Enabling plans: %@, error: %@ @%s"
+ "[E]Fail to fetch CurrentDataSubscription: %@ @%s"
+ "[E]Fail to set international data access status @%s"
+ "[E]Faile to save cellular settings: %@ @%s"
+ "[E]Failed to cancel plan installation for:%@ error:%@ @%s"
+ "[E]Failed to find a plan item for home iccid @%s"
+ "[E]Failed to find info @%s"
+ "[E]Failed to get iMessageService. @%s"
+ "[E]Failed to send travel metric for post arrival install [%@] @%s"
+ "[E]Failed to send travel metric for predeparture install [%@] @%s"
+ "[E]Failed to send travel metric for roaming education [%@] @%s"
+ "[E]Failed to send travel metric for travel intro [%@] @%s"
+ "[E]Invalid DCT Code! @%s"
+ "[E]Invalid indexPath: %@ @%s"
+ "[E]Invalid uuid for item: %@. @%s"
+ "[E]No defined cell for index: %@ @%s"
+ "[E]No plan found with plan status CTPlanTransferStatusLaunchWebsheet @%s"
+ "[E]No selected items! @%s"
+ "[E]auto reconnection details submission failure. error:%@ @%s"
+ "[E]cannot find install plan info for plan ID : %@ @%s"
+ "[E]cannot find install plan info for target iccid hash : %@ @%s"
+ "[E]cannot find matching info for iccid: %@ @%s"
+ "[E]dactivate transport failed : %@ @%s"
+ "[E]don't have eligible plan to transfer @%s"
+ "[E]failed to move to home screen: %@ @%s"
+ "[E]failed to verify dct code @%s"
+ "[E]iPad should not supports MultiSIM transfer @%s"
+ "[E]incorrect enabling item count : %lu @%s"
+ "[E]installMultiplePlans error=%@ @%s"
+ "[E]installMultiplePlans failed with error: %@ @%s"
+ "[E]invalid %s @%s"
+ "[E]invalid DCTCodeDelegate delegate @%s"
+ "[E]invalid TSProximitySourceTransferFlow @%s"
+ "[E]no error for %@, showing generic error message. @%s"
+ "[E]no plan selected @%s"
+ "[E]nothing to present!!! @%s"
+ "[E]plan %@ has no item @%s"
+ "[E]plan or deviceId is nil @%s"
+ "[E]root vc not find. flow - %@, root - %@ @%s"
+ "[E]strong self gone @%s"
+ "[E]subflow %@ has no first view @%s"
+ "[E]unexpected bar item : %@ @%s"
+ "[E]unexpected transfer capability : %lu(%s) @%s"
+ "[F](%@) stop untracked navigation item: %@, expect:%@ @%s"
+ "[F]No need launch enable plan flow for non-hydra device @%s"
+ "[F]No need to launch enable plan flow when there is only 1 plan enabled @%s"
+ "[F]cannot find plan id : %@ @%s"
+ "[F]delegate is wrong. expected: %@, actual: %@ @%s"
+ "[F]first vc callback is already cleared. topVC:%@, vc:%@ @%s"
+ "[F]invalid plan identifier @%s"
+ "[F]missing navigation controller, UI transition will not work @%s"
+ "[F]out of bound index @%s"
+ "[F]unexpect change of delegate: %@ @%s"
+ "[F]unimplemented, please use async version @%s"
+ "[I] active plan is not the provisioning plan. ignore:%@ @%s"
+ "[I] enablement in presentation @%s"
+ "[I] not all plan in terminal state, we should wait here @%s"
+ "[I] websheet in presentation @%s"
+ "_"
+ "_NFCTransferStatus"
+ "_allPlans"
+ "_allPlansActivated"
+ "_allPlansInstallComplete"
+ "_allowMultiPlanSelection"
+ "_areAllInstallingPlansBeEnabled"
+ "_areAllPlansInPostInstallOrTerminalState"
+ "_areAllPlansInTerminalState"
+ "_areAllPlansTransferedOut"
+ "_buddyMLViewController"
+ "_cancelAction"
+ "_cancelTransferringPlan:"
+ "_cancelledDeviceIDs"
+ "_carrierSetupPlan"
+ "_collectAllPhoneNumbersForDevice:"
+ "_confirmationCodeViewController"
+ "_constructDCTUrl:withPasscode:"
+ "_createTargetProxFlowVC"
+ "_createTransferCloudFlowVC"
+ "_createTransferFlowVC"
+ "_createTransferSubFlowVcWithSession:isPostmigrationFlow:"
+ "_dataSubCarrierName"
+ "_dataSubscriptionContext"
+ "_dctDelegate"
+ "_dctInfo"
+ "_dctPrewarmSucceded"
+ "_decodeBase64EncodedString:"
+ "_decodeBase64EncodedString: ret %@ @%s"
+ "_decodeTransferStatus:"
+ "_defaultDataContext"
+ "_defaultVoiceIccid"
+ "_dequeueInteractiveUI"
+ "_descriptors"
+ "_detailtitle"
+ "_didProcessDCTCode"
+ "_didUserClickContinue"
+ "_dismissDueToLoadFailure"
+ "_dismissViewController"
+ "_displayCarrierSetupViewController:"
+ "_displayConfirmationCodeViewController:"
+ "_displayIntermediateViewController:"
+ "_displayOneTimeCodeViewController:phoneNumber:carrierName:usePin:"
+ "_displayPlan"
+ "_displayTermsAndConditionsViewController:mainText:"
+ "_displayWebsheetViewController:"
+ "_displayedDeviceIDs"
+ "_doneAction"
+ "_eSIMTravelState"
+ "_enablingIccid"
+ "_enqueueInteractiveUI:"
+ "_failIdentityShare"
+ "_findEligiblePlans:"
+ "_findPlanInfoWithPlanID:"
+ "_findPlanInfoWithPlanStatus:"
+ "_findPlanInfoWithTargetIccid:"
+ "_findPlanInfoWithTargetIccidHash:"
+ "_formatedDescriptor"
+ "_fromDataTransferSession"
+ "_getCarrierNameForDefaultDataSub"
+ "_getCellularPlanItemForTravelSIM"
+ "_getDetailsTextWithIccid:"
+ "_getPlanItemsToLimitService:"
+ "_getSubtitleWhenSyncWithTarget:selectedPlansCount:selectedPlansFailedTransferCount:"
+ "_getTitleWhenSyncWithTarget:selectedPlansCount:selectedPlansFailedTransferCount:"
+ "_getTraveleSIMStateWithCompletion:"
+ "_getWebsheetInfo:completion:"
+ "_handleActivatedItemUpdate:"
+ "_handleMultiSIMInstallationStatusUpdateEvent:"
+ "_handleNotificationESIMInstallStateChanged:"
+ "_handlePostInstallItemUpdate:"
+ "_handleProvisioningItemUpdate:"
+ "_handleTransferResults:"
+ "_handleTransferUICapability:"
+ "_hasAnyDisabledInstallPlan"
+ "_hasAnyPlanSuccessfullyInstalled"
+ "_hasAnyPlanSuccessfullyInstalledOrPostInstalled"
+ "_homeIccid"
+ "_homeIccidPhoneNumber"
+ "_iccidToEnable"
+ "_infos"
+ "_installError"
+ "_installInfos"
+ "_installMultipleSelectedPlans"
+ "_installPlans"
+ "_installStateChanged:"
+ "_installationEndTime"
+ "_installationStartTime"
+ "_installingPlanInfos"
+ "_isAnyPlanRequireLocationService"
+ "_isAnyPlanWithMismatchedActivationPolicy"
+ "_isCancelButtonTapped"
+ "_isDataOnly"
+ "_isDataOnlySelected"
+ "_isDeviceIdentifierPresent"
+ "_isDeviceInfo"
+ "_isDisabled"
+ "_isDisembarkUIRequired"
+ "_isDtoEvaluationRequired"
+ "_isDtoEvaluationSucceeded"
+ "_isEmbeddedInResultView"
+ "_isEnterManuallyTapped"
+ "_isFlexPolicyOn"
+ "_isFollowUpInstall"
+ "_isForCrossPlatformTransfer"
+ "_isFromDataTransferSession"
+ "_isHomeSIMOnPhySlot"
+ "_isNFCDataSuccessTransfer"
+ "_isPhysical"
+ "_isPostMigrationFlow"
+ "_isPreInstalled"
+ "_isPreSharedKeyPresent"
+ "_isProxFlowShown"
+ "_isSIMOnPhySlot"
+ "_isSecureIntentRequired"
+ "_isSecureIntentSucceeded"
+ "_isSelectedAsTravelSIM"
+ "_isShowingFilteredPlans"
+ "_isShown"
+ "_isSkipButtonTapped"
+ "_isSource"
+ "_isSourceSideError"
+ "_isSyncWithTargetResults"
+ "_isTravelFlow"
+ "_isTravelSIMDataOnly"
+ "_isTravelSIMOnPhySlot"
+ "_isUserAbroad"
+ "_isUserInHomeCountry"
+ "_isUsingPreSharedKey"
+ "_laterButtonTapped:"
+ "_launchDisembarkUI:"
+ "_learnMoreTapped"
+ "_limit"
+ "_maxAllowedeSIMCount"
+ "_maybeAutoInstallPendingPlan"
+ "_maybeClearFirstViewControllerCallback"
+ "_maybeClearSubFlowViewController:"
+ "_maybeDismissSelf"
+ "_maybeDisplayInteractiveUI:"
+ "_maybeDisplayNextIntermediateViewController"
+ "_maybeDisplaySourceDeviceConsentAlert:"
+ "_maybeFlowCompleted:"
+ "_maybeHandleConfirmationCodeError:"
+ "_maybeHandleProvisioningError:items:"
+ "_maybeMoveToNextItem"
+ "_maybePresentFirstViewController:"
+ "_maybeReplyFirstViewControllerCallbackWithViewController:"
+ "_maybeSendExternalizedContext:isDTOEvaluationFailed:"
+ "_maybeSendTransferResults"
+ "_maybeSendTransferUICapability:"
+ "_maybeSetNavigationController:"
+ "_maybeStartTimerForNewlyInstalledPlan:newStatus:"
+ "_maybeSubmitAutoReconnectionDetails"
+ "_maybeUpdateHomeIccid:homeIccid:"
+ "_maybeUpdatePhysicalSIMStatus:"
+ "_maybeUpdatePlanNameForTargetIccid:planName:"
+ "_maybeUpdatePlanNameWithoutPlanID:"
+ "_maybeUpdateUserEnabledPlans:"
+ "_messageSession"
+ "_needAutoInstallPendingPlan"
+ "_needShow"
+ "_nfcAnimationView"
+ "_numSelectedPlansNotTransferredOut"
+ "_offerFallbackOption"
+ "_onInstallError:"
+ "_originalEnabledPlans"
+ "_otherOptionsButton"
+ "_peerDeviceInfo"
+ "_pendingInteractiveViewControllers"
+ "_planEnablementState"
+ "_planError"
+ "_planList"
+ "_planStatusDescriptions"
+ "_postArrivalInstallation"
+ "_preWarmOngoing"
+ "_prepareDisplayItems:withPlanItems:"
+ "_prepareForEnablingItem:"
+ "_prepareForInstallingItems:"
+ "_preselectPlanIfNeeded"
+ "_presentedViewController"
+ "_proxPlansFiltered"
+ "_queryParamToTitle"
+ "_redirectToBTFlow"
+ "_refreshContinueButton"
+ "_refreshTableView"
+ "_registerMessages"
+ "_reloadScreen"
+ "_requireGeneralConsent"
+ "_requireSyncUpTransferResultsWithSource"
+ "_retainedObject"
+ "_retryAction"
+ "_roamingInfo"
+ "_roamingSwitchEnabled"
+ "_scannedCode"
+ "_selectedItems"
+ "_selectedPlan"
+ "_selectedPlansCount"
+ "_selectedPlansFailedTransferCount"
+ "_selectedTransferPlansCount"
+ "_sendTravelEventMetricForPlan:useLDM:"
+ "_sendTravelEventMetricForRoaming:"
+ "_setTravelIccidInfo:"
+ "_setUpButtons"
+ "_setUpLearnMoreLink"
+ "_setUpTableView"
+ "_setupTableView"
+ "_shareIdentityButton"
+ "_shareIdentityTapped"
+ "_shouldOfferFallbackOptionOnError:"
+ "_shouldPlanBeRegisteredForIMessage:"
+ "_shouldWaitUntilPhoneNumberBeReady:completion:"
+ "_showCancelAlert:withMessage:"
+ "_showFailureAlert"
+ "_showTurnOnLocationServices"
+ "_singleItemFlow"
+ "_skip"
+ "_skipButtonTapped:"
+ "_sortedInfo"
+ "_sourceOSVersion"
+ "_sourceOsVersion"
+ "_startInstallMultiplePlans:transferPlans:andCarrierSetupItems:"
+ "_startNFCIdentityShare"
+ "_startObserver"
+ "_status"
+ "_statusDescription:info:"
+ "_stopNFCIdentityShare"
+ "_subFlowVcWithReconnectionCredentials:"
+ "_subFlowViewControllers"
+ "_successIdentityShare"
+ "_supportsSyncTransferResults"
+ "_tappedLearnMore"
+ "_targetIccid"
+ "_targetIccidHash"
+ "_timer"
+ "_timerFired"
+ "_transferablePlanOnSource"
+ "_travelIccid"
+ "_travelIccidInfo"
+ "_travelOnlySelected"
+ "_travelSIM"
+ "_triangleImageView"
+ "_turnOnLocationServicesTapped"
+ "_unlockAction"
+ "_updateAuthenticationStatus:isDTOEvaluationFailed:"
+ "_updateCarrierErrorCode:withPlanID:"
+ "_updateEnablePlanItems"
+ "_updateInstallError:withPlanID:webUrl:postData:"
+ "_updateInstallError:withTargetIccidHash:"
+ "_updatePlanStatus:forPlanInfo:"
+ "_updatePlanStatus:withPlanID:"
+ "_updatePlanStatus:withTargetIccid:"
+ "_updateTargetIccid:withPlanID:"
+ "_updateTargetIccidWithoutPlanID:"
+ "_updateTransferStatus:"
+ "_useTravelOnly"
+ "_userEnabledPlanInfos"
+ "_userSelectAsTravelSIM"
+ "_validCarrierName"
+ "_values"
+ "_viewDelegate"
+ "_voiceIccid"
+ "_waitingStartTime"
+ "_webView:focusRequiresStrongPasswordAssistance:completionHandler:"
+ "accessoryViewForStatus:"
+ "accounts"
+ "activate"
+ "activateUsingPreSharedKey:completion:"
+ "activatingState"
+ "activeSubscriptionsDidChange"
+ "addNewPlanWithUserInfo"
+ "addSubFlowViewController:"
+ "addSymbolEffect:"
+ "addressField:%@, activationCode:%@, confirmationCode:%@ @%s"
+ "all done ? %{bool}d @%s"
+ "all transfered : %{bool}d, has transfer failure : %d @%s"
+ "allObjects"
+ "allPlans"
+ "allPlansActivated"
+ "allPlansInstallComplete"
+ "already scanned the code. Ignoring this @%s"
+ "alsPlanCarriers:"
+ "appendFormat:"
+ "appendLeftToRightMark:"
+ "appendString:"
+ "areAllPlansTransferedOut"
+ "areAnyPlansOnDevice"
+ "arePlansAvailable:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:"
+ "arrayByAddingObjectsFromArray:"
+ "arrow.3.trianglepath"
+ "backButtonClicked:"
+ "backToCurrentTopPane"
+ "bootstrap:isUsingPreSharedKey:completion:"
+ "bootstrapPlanTransferUsingMessageSession:flowType:completion:"
+ "bootstrapping CT failed with: %@ @%s"
+ "buddyMLViewController"
+ "bytes"
+ "cachedPhoneNumber"
+ "cancel button tapped, cancel the flow, send empty selection @%s"
+ "cancelAction"
+ "cancelPlanInstallation:completion:"
+ "cancelledDeviceIDs"
+ "cannot find install or user enable plan info for targetIccid : %@ @%s"
+ "cannot find install plan info for target iccid : %@ @%s"
+ "cannot go back from terminal state to PostInstalling @%s"
+ "capitalizedString"
+ "carrierSetupPlan"
+ "center"
+ "checkmark.circle.fill"
+ "chevron.forward"
+ "circle"
+ "clear subflow vc : %@ @%s"
+ "clearReconnectionCredentials:"
+ "com.apple.madrid"
+ "com.apple.springboard"
+ "compareProductVersion:toProductVersion:"
+ "componentsSeparatedByString:"
+ "componentsWithString:"
+ "concatenateDescriptors:"
+ "configurationWithPointSize:"
+ "confirmCellularPlanTransfer"
+ "confirmation code is already handled @%s"
+ "confirmationCodeViewController"
+ "connectionStarted"
+ "consent timeout, update %@ status to TimeoutNotConsented @%s"
+ "consolidatedActivatingState"
+ "constraintLessThanOrEqualToAnchor:"
+ "continueTransferWithoutWifi:"
+ "cross platform transfer case, dont show Source Device Consent Alert @%s"
+ "cross.platform.transfer"
+ "cur : %@, next: %@ @%s"
+ "current view:%@, current sub flow type: %lu, next view:%@ @%s"
+ "data only"
+ "dctDelegate"
+ "dctInfo"
+ "dctPrewarmSucceded"
+ "deactivateCrossPlatformTransport:completion:"
+ "deactiveCrossPlatformTransport"
+ "defaultConfig"
+ "defaultContentConfiguration"
+ "defaultVoiceIccid"
+ "dequeueReusableCellWithIdentifier:forIndexPath:"
+ "descriptorWithSubscriptionContext:"
+ "descriptors"
+ "detailtitle"
+ "device has no capable cross platform transfer plans @%s"
+ "dictionary"
+ "didProcessDCTCode"
+ "didUserClickContinue"
+ "disablePredicativeTextForTextField:"
+ "dismissAutoFillInternalFeedbackActivityForFormAutoFillController:immediately:"
+ "displayPlan"
+ "displayedDeviceIDs"
+ "doneAction"
+ "dualSimCapabilityDidChange"
+ "eSIMTravelExperience"
+ "eSIMTravelState"
+ "effect"
+ "enablingIccid"
+ "error already set, ignore @%s"
+ "establishReconnectionCredentials:completion:"
+ "establishReconnectionCredentialsUsingMessageSession:completion:"
+ "evaluateDtoPolicy:"
+ "evaluating dto policy @%s"
+ "exclamationmark.triangle"
+ "exclamationmark.triangle.fill"
+ "externalized context = %@ isSecureIntentRequired: %d, isDtoEvaluationRequired:%d @%s"
+ "extractionSource"
+ "finalAction"
+ "finalActionSubtype"
+ "findPlanInfoWithoutTargetIccid"
+ "first view controller %@ for root flow %@ @%s"
+ "firstViewControllerForDisplay"
+ "flow"
+ "flow is moved out. let's clean it : %@ @%s"
+ "footerConfiguration"
+ "formatLocAndConcatenateDescriptors:"
+ "formatedDescriptor"
+ "formattedPhoneNumber"
+ "fragment"
+ "getCellularPlanItem:withIccid:"
+ "getCurrentDataSubscriptionContextSync:"
+ "getErrorDescription:"
+ "getPlanByID:fromPlans:"
+ "getProximityTransportSession:remoteDeviceInfo:usePreSharedKey:completion:"
+ "getTitleAndDetailsForPlanType:transferCapability:isShowingFilteredPlans:carrier:"
+ "getTravelInfoForIccid:completion:"
+ "getWordRepresentationForInt:"
+ "gift"
+ "handleCrossplatformSessionResponse:completion:"
+ "handleStartOverWithEntryPoint:navigationController:completion:"
+ "handleWaitingOnWifiStatusUpdate:"
+ "header.textLable"
+ "home eSIM iccid (%@) post arrival installation (%@) @%s"
+ "home sim"
+ "homeSIMIccid"
+ "https"
+ "https://support.apple.com/102433"
+ "https://support.apple.com/109037"
+ "https://support.apple.com/118227"
+ "iccidHash"
+ "iccidToEnable"
+ "identifier"
+ "ignore physical SIM : %@ @%s"
+ "imageByApplyingSymbolConfiguration:"
+ "imageName"
+ "imageWithCIImage:"
+ "indexOfObjectPassingTest:"
+ "indexesOfObjectsPassingTest:"
+ "init:"
+ "initAsMidOperationWithCarrierName:requireGeneralConsent:"
+ "initShowErrorOnSourceWithPlanIdentifier:"
+ "initWithAssociatedPlanItem:initialLabel:predefinedUserLabels:"
+ "initWithBase64EncodedString:options:"
+ "initWithCode:"
+ "initWithData:encoding:"
+ "initWithEnablingPlanIccid:"
+ "initWithEnablingPlanInfo:"
+ "initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:"
+ "initWithFlow:navigationController:delegate:"
+ "initWithFrame:style:limit:"
+ "initWithIccids:homeIccid:voiceIccid:postArrivalInstallation:"
+ "initWithInBuddy:transferablePlans:selectedTransferablePlans:alsPlans:selectedAlsPlans:odaPlans:transferPlanCarriers:selectedTransferPlanCarriers:alsPlanCarriers:selectedAlsPlanCarriers:odaPlanCarriers:selectedOdaPlanCarriers:sourceDevicesCount:selectedSourceDevicesCount:"
+ "initWithInfos:"
+ "initWithItem:"
+ "initWithOptions:extractionSource:"
+ "initWithOptions:navigationController:delegate:"
+ "initWithPlanIdentifer:"
+ "initWithPlanInfos:"
+ "initWithPlanInfos:userEnablePlans:skip:"
+ "initWithPlanItemError:updatePlanItem:withBackButton:forCarrier:withCarrierErrorCode:isEmbeddedInResultView:"
+ "initWithPlans:homeIccid:"
+ "initWithPlans:isSelectedAsTravelSIM:"
+ "initWithPlans:planItems:fromDataTransferSession:"
+ "initWithPlans:skip:"
+ "initWithPlans:skip:isForCrossPlatformTransfer:"
+ "initWithProximitySetupState:proxPlansFiltered:"
+ "initWithRetainedObject:isSource:"
+ "initWithSelectedPlans:confirmCellularPlanTransfer:isForCrossPlatformTransfer:session:sourceOsVersion:"
+ "initWithSelectedPlansCount:selectedPlansFailedTransferCount:isDisembarkUIRequired:"
+ "initWithService:"
+ "initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:"
+ "initWithSession:sourceOSVersion:proximitySetupState:transferablePlanOnSource:"
+ "initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:"
+ "initWithSpinnerText:"
+ "initWithSuccess:skipped:duration:"
+ "initWithTemplate:"
+ "initWithTimeoutReason:isEmbeddedInResultView:plans:"
+ "initWithTitle:detail:"
+ "initWithTitle:detailText:symbolName:contentLayout:"
+ "initWithTitle:details:symbolName:plans:skip:"
+ "initWithTransferBackPlan:isPostMigrationFlow:"
+ "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:allowsMultiSelection:"
+ "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:"
+ "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:allowsMultiSelection:"
+ "initWithTransferItems:showOtherOptions:isShowingFilteredPlans:"
+ "initWithTransferOutPlan:"
+ "initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isShowingFilteredPlans:"
+ "initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isStandaloneProximityFlow:transferBackPhoneNumber:isShowingFilteredPlans:"
+ "initWithURL:postdata:"
+ "initWithoutTargetSyncAndSelectedPlansCount:"
+ "inject back button action for : %@, handler: %@ @%s"
+ "install.failed"
+ "installError"
+ "installInfos"
+ "installMultiplePlans:completionHandler:"
+ "installationEndTime"
+ "installationStartTime"
+ "installingPlanInfos"
+ "invalid TSCrossPlatformSourceTransferFlow @%s"
+ "isActiveDataPlan"
+ "isCancelButtonTapped"
+ "isDataActive"
+ "isDataOnly"
+ "isDataOnlySelected"
+ "isDeviceIdentifierPresent"
+ "isDeviceInfo"
+ "isDisabled"
+ "isDisembarkUIRequired"
+ "isDtoEvaluationRequired"
+ "isDtoEvaluationSucceeded"
+ "isEnterManuallyTapped"
+ "isEqualToSet:"
+ "isFlexPolicyOn"
+ "isForCrossPlatformTransfer"
+ "isFromDataTransferSession"
+ "isGlobalMVNO"
+ "isIccidForPhySlot:"
+ "isLanguageRightToLeft"
+ "isNFCDataSuccessTransfer"
+ "isNFCEnable"
+ "isPhone"
+ "isPlanInstalledAndNotEnabled:item:"
+ "isPostMigrationFlow"
+ "isPreInstalled"
+ "isPreSharedKeyForReconnectionPresent:completion:"
+ "isPreSharedKeyPresent"
+ "isProxFlowShown"
+ "isRegRestLocationUnavailable:"
+ "isRegulatoryRestrictedPlan"
+ "isSecureIntentRequired"
+ "isSecureIntentSucceeded"
+ "isSelectable"
+ "isSelectedAsTravelSIM"
+ "isSharingIdentitySupportedWithError:"
+ "isShown"
+ "isSkipButtonTapped"
+ "isSource"
+ "isSyncWithTargetResults"
+ "isTraveleSIM"
+ "isUserAbroad"
+ "isUserInHomeCountry"
+ "isUserTraveling"
+ "isUsingPreSharedKey"
+ "isVinylCapable"
+ "kCrossTransferConnectFailReason"
+ "kCrossTransferSessionError"
+ "kSelectedTransferPlansCount"
+ "key"
+ "keyboardDidHide:"
+ "launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:"
+ "lightGrayColor"
+ "limit"
+ "lock.iphone"
+ "lowercaseString"
+ "mapping %@ -> %@ @%s"
+ "matchingSim"
+ "maybePrepareNextDisplayViewController:completion:"
+ "maybeUpdateTimeoutStatus:"
+ "messageSession"
+ "migrate.google.com"
+ "mm ongoing after enable the plan. %@ state: %s, mdn:%@ @%s"
+ "navigation controller"
+ "nearbyActionExtraData"
+ "needShow"
+ "nfcAnimationView"
+ "no change @%s"
+ "not all plans with a completed state. %@ state: %s, mdn:%@ @%s"
+ "not all plans with post install state. %@ state - %s @%s"
+ "notificationType"
+ "notificationWithName:object:userInfo:"
+ "numActivePlansOnDevice"
+ "numActivePlansOnDevice: %ld @%s"
+ "numSelectedPlansNotTransferredOut"
+ "odaPlanCarriers:"
+ "openApplication:withOptions:completion:"
+ "options: %lu @%s"
+ "optionsWithDictionary:"
+ "originalEnabledPlans"
+ "otherOptionsButton"
+ "p"
+ "parseQueryParamsWithTitleDictionary:"
+ "pausing transfer timer for wi-fi selection @%s"
+ "peerDeviceInfo"
+ "pendingInteractiveViewControllers"
+ "percentEncodedQuery"
+ "phone number is not ready. set as CTPlanTransferStatusActivatedNoPhoneNumber @%s"
+ "plan%ld"
+ "planEnablementState"
+ "planError"
+ "planItemText:"
+ "planList"
+ "postarrival_buddy"
+ "postarrival_buddy_ldm_off"
+ "postarrival_buddy_ldm_on"
+ "postarrival_buddy_roaming"
+ "postarrival_buddy_use_travel"
+ "postarrival_buddy_use_travel_and_home"
+ "postarrival_install"
+ "postarrival_install_ldm_off"
+ "postarrival_install_ldm_on"
+ "postarrival_install_use_travel"
+ "postarrival_install_use_travel_and_home"
+ "predeparture_install"
+ "prepareViewController:completion:"
+ "present first view : %@ @%s"
+ "presentAutoFillInternalFeedbackToastForFormAutoFillController:diagnosticsDataWithoutPageContents:"
+ "presentInSettings"
+ "presentProxCardFlowWithDelegate:initialViewController:"
+ "presenting %@, enqueue %@ @%s"
+ "productVersion"
+ "proxCardFlowDidDismiss"
+ "proxCardFlowWillPresent"
+ "proximitySetupState"
+ "push %@ for %@ with status : %s @%s"
+ "pushTimeoutFailureViewControllerWithStatus:forPlan:"
+ "pushToDetailViewControllerWithError:forPlan:"
+ "q24@?0@\"CTCellularPlanItem\"8@\"CTCellularPlanItem\"16"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "q24@?0@\"NSIndexPath\"8@\"NSIndexPath\"16"
+ "queryItems"
+ "queryParamToTitle"
+ "queryStartSessionRequest:"
+ "receive status update for %@ : %lu(%s) @%s"
+ "received error already : %@, new error: %@ for %@ @%s"
+ "recv provisioning error : %@ for target iccid hash : %@ @%s"
+ "registerRequestID:options:handler:"
+ "release retaind mk object @%s"
+ "reloadInputViews"
+ "removeAction:"
+ "requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:"
+ "resetPendingAutoFillInternalFeedbackToastDismissalTimer"
+ "results:%@ @%s"
+ "resuming transfer timer for wi-fi selection @%s"
+ "retryAction"
+ "return vc %p to MK in firstViewController call @%s"
+ "rightAnchor"
+ "roamingInfo"
+ "roaming_education"
+ "roaming_education_roaming_off"
+ "roaming_education_roaming_on"
+ "root flow delegate: %@ @%s"
+ "rootFlow"
+ "s"
+ "safeAreaLayoutGuide"
+ "saveCellularSettingsForReturnToHome:"
+ "secondaryText"
+ "secondaryTextProperties"
+ "selectedItems"
+ "selectedItems %@ @%s"
+ "selectedPlan"
+ "selectedPlansCount"
+ "selectedPlansFailedTransferCount"
+ "selectedTransferPlansCount"
+ "send transfer ui capability : %@ @%s"
+ "sendRequestID:options:request:responseHandler:"
+ "sendTravelBuddyCAEvent:error:"
+ "set"
+ "set phone number %@ for plan: %@ @%s"
+ "set plan name %@ for plan %@ @%s"
+ "set plan name - %@ @%s"
+ "setActivityIndicatorHidden:"
+ "setAllPlans:"
+ "setAllPlansActivated:"
+ "setAllowsInlineMediaPlayback:"
+ "setAreAllPlansTransferedOut:"
+ "setAssociatedIccid:"
+ "setBorderColor:"
+ "setBorderWidth:"
+ "setBuddyMLViewController:"
+ "setCancelAction:"
+ "setCancelledDeviceIDs:"
+ "setCarrierSetupPlan:"
+ "setCenter:"
+ "setConfirmCellularPlanTransfer:"
+ "setConfirmationCodeViewController:"
+ "setContentConfiguration:"
+ "setContentMode:"
+ "setCornerRadius:"
+ "setDctDelegate:"
+ "setDctInfo:"
+ "setDctPrewarmSucceded:"
+ "setDefaultVoiceIccid:"
+ "setDefaults"
+ "setDescriptors:"
+ "setDetailtitle:"
+ "setDidProcessDCTCode:"
+ "setDidUserClickContinue:"
+ "setDisplayPlan:"
+ "setDisplayedDeviceIDs:"
+ "setDoneAction:"
+ "setESIMTravelState:"
+ "setEditing:"
+ "setEnable:"
+ "setEnablingIccid:"
+ "setFormatedDescriptor:"
+ "setFragment:"
+ "setHost:"
+ "setIccidToEnable:"
+ "setInstallError:"
+ "setInstallInfos:"
+ "setInstallationEndTime:"
+ "setInstallationStartTime:"
+ "setInstallingPlanInfos:"
+ "setIsCancelButtonTapped:"
+ "setIsDataOnly:"
+ "setIsDataOnlySelected:"
+ "setIsDeviceIdentifierPresent:"
+ "setIsDeviceInfo:"
+ "setIsDisabled:"
+ "setIsDisembarkUIRequired:"
+ "setIsDtoEvaluationRequired:"
+ "setIsDtoEvaluationSucceeded:"
+ "setIsEnterManuallyTapped:"
+ "setIsFlexPolicyOn:"
+ "setIsForCrossPlatformTransfer:"
+ "setIsFromDataTransferSession:"
+ "setIsNFCDataSuccessTransfer:"
+ "setIsPhysical:"
+ "setIsPostMigrationFlow:"
+ "setIsPreInstalled:"
+ "setIsPreSharedKeyPresent:"
+ "setIsProxFlowShown:"
+ "setIsSecureIntentRequired:"
+ "setIsSecureIntentSucceeded:"
+ "setIsSelectedAsTravelSIM:"
+ "setIsShown:"
+ "setIsSkipButtonTapped:"
+ "setIsSource:"
+ "setIsSyncWithTargetResults:"
+ "setIsUserInHomeCountry:"
+ "setIsUsingPreSharedKey:"
+ "setLimit:"
+ "setLowDataMode:enable:"
+ "setMagnificationFilter:"
+ "setMasksToBounds:"
+ "setMessageSession:"
+ "setModalTransitionStyle:"
+ "setNFCTransferStatus:"
+ "setNeedShow:"
+ "setNfcAnimationView:"
+ "setNumSelectedPlansNotTransferredOut:"
+ "setNumberStyle:"
+ "setOriginalEnabledPlans:"
+ "setOtherOptionsButton:"
+ "setPeerDeviceInfo:"
+ "setPendingInteractiveViewControllers:"
+ "setPlanEnablementState:"
+ "setPlanError:"
+ "setPlanItem:"
+ "setPlanItems:"
+ "setPlanList:"
+ "setPlans:"
+ "setPresentedViewController:"
+ "setProximitySetupState:"
+ "setQuery:"
+ "setQueryParamToTitle:"
+ "setRetryAction:"
+ "setRoamingInfo:"
+ "setScheme:"
+ "setSecondaryText:"
+ "setSectionFooterHeight:"
+ "setSectionHeaderHeight:"
+ "setSelectedItems:"
+ "setSelectedPlansCount:"
+ "setSelectedPlansFailedTransferCount:"
+ "setSelectedTransferPlansCount:"
+ "setSeparatorColor:"
+ "setSeparatorStyle:"
+ "setShouldAdjustButtonTrayForKeyboard:"
+ "setSimCapability:"
+ "setSkip:"
+ "setSmartDashesType:"
+ "setSmartInsertDeleteType:"
+ "setSmartQuotesType:"
+ "setSourceOSVersion:"
+ "setSourceOsVersion:"
+ "setSpellCheckingType:"
+ "setStatus:"
+ "setSubFlowViewControllers:"
+ "setSupportedRegionCodes:"
+ "setSupportsSyncTransferResults:"
+ "setTappedLearnMore:"
+ "setTargetIccid:"
+ "setTargetIccidHash:"
+ "setTimer:"
+ "setTitleColor:forState:"
+ "setTransferablePlanOnSource:"
+ "setTravelOnlySelected:"
+ "setTravelSIM:"
+ "setTriangleImageView:"
+ "setUnlockAction:"
+ "setUseTravelOnly:"
+ "setUserEnabledPlanInfos:"
+ "setViewDelegate:"
+ "setWaitingStartTime:"
+ "setWithArray:"
+ "settings-navigation://com.apple.Settings.General/NFC_LINK"
+ "settings-navigation://com.apple.Settings.PrivacyAndSecurity/LOCATION"
+ "setupConstraints"
+ "setupViewsWithTag:delegate:"
+ "setupWithDelegate:indexPath:"
+ "sha256"
+ "shippingbox"
+ "shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:completion:"
+ "show : %{bool}d, skip : %{bool} d, count : %lu @%s"
+ "simLessSubscriptionsDidChange"
+ "skip"
+ "skip - count : %lu @%s"
+ "skip. count : %lu @%s"
+ "smartphone"
+ "softlink:r:path:/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI"
+ "sortedArrayUsingComparator:"
+ "source ui capability : %@ @%s"
+ "sourceDevicesCount:"
+ "sourceOSVersion"
+ "sourceOsVersion"
+ "src.ver:%@ @%s"
+ "startSharingIdentity:"
+ "stopSharingIdentity"
+ "stringByAppendingString:"
+ "stringFromNumber:"
+ "sub flow doesnot follow 1st VC paradigm : %lu @%s"
+ "subFlowViewControllers"
+ "submitAutoReconnectionDetails"
+ "submitAutoReconnectionDetails:"
+ "submitAutoReconnectionDetails:completion:"
+ "subscriptionInfoDidChange"
+ "substringToIndex:"
+ "supports hydra: %@, selectable plans: %lu, enabled plans: %lu @%s"
+ "supportsSyncTransferResults"
+ "systemGray6Color"
+ "systemLightGrayColor"
+ "tappedLearnMore"
+ "tapped_learn_more"
+ "target supported UI capability:%@ @%s"
+ "targetIccid"
+ "targetIccidHash"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "textProperties"
+ "timeout, update %@ status to TimeoutInstallOngoing @%s"
+ "timer"
+ "timerWithTimeInterval:target:selector:userInfo:repeats:"
+ "top view controller"
+ "transfer abort, require to launch websheet : %@, websheetUrl: %@, postdata: %@ @%s"
+ "transfer back, enable the item %@. error:%@ @%s"
+ "transfer education"
+ "transferablePlanCarriers:"
+ "transferablePlanOnSource"
+ "travel eSIM iccid (%@) home eSIM iccid (%@) default voice iccid (%@) @%s"
+ "travel sim"
+ "travelIccid"
+ "travelIccid (%@) voiceIccid (%@) @%s"
+ "travelOnlySelected"
+ "travelSIM"
+ "travelSIMIccid"
+ "travel_intro"
+ "travel_intro_roaming_off"
+ "travel_intro_roaming_on"
+ "triangleImageView"
+ "un"
+ "unable to get strong self @%s"
+ "unable to query start session request: %@ @%s"
+ "unimplemented plan type : %@"
+ "unlockAction"
+ "unsignedIntValue"
+ "update target iccid %@ without plan ID @%s"
+ "updateCellularPlanProperties:appName:appType:completionHandler:"
+ "updateInstallationStatus:forPlanID:"
+ "updateProvisioningError:targetIccidHash:"
+ "updateRasterizationScale:"
+ "updateSIMTransferStatus:"
+ "updateSecureIntentData:isDTOEvaluationFailed:"
+ "updateSecureIntentData:isDTOEvaluationFailed:error:"
+ "updateTableHeightAnchor"
+ "updateTargetIccidInfo:"
+ "useTravelOnly"
+ "user select [%lu] plans @%s"
+ "user tap back to cancel with top visible view controller: %@ @%s"
+ "userEnabledPlanInfos"
+ "v16@?0q8"
+ "v24@?0@\"BSProcessHandle\"8@\"NSError\"16"
+ "v24@?0@\"CTPlanTravelDetails\"8@\"NSError\"16"
+ "v28@0:8@\"_SFFormAutoFillController\"16B24"
+ "v28@0:8B16@?20"
+ "v28@?0i8@\"NSDictionary\"12@\"NSDictionary\"20"
+ "v32@0:8@\"NSArray\"16@?<v@?BB>24"
+ "v32@0:8@\"NSError\"16@\"NSString\"24"
+ "v32@0:8@\"WKWebView\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"_SFFormAutoFillController\"16@\"WBSAutoFillInternalFeedbackDiagnosticsData\"24"
+ "v32@?0@\"CTRemoteDeviceList\"8B16B20@\"NSError\"24"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@?<v@?i@\"NSDictionary\"@\"NSDictionary\">24"
+ "v36@0:8@16B24q28"
+ "v40@0:8@\"WKWebView\"16@\"<_WKFocusedElementInfo>\"24@?<v@?B>32"
+ "v40@0:8@16Q24@?32"
+ "v44@0:8@16@24@32B40"
+ "v52@0:8@\"NSData\"16@\"NSArray\"24B32B36B40@?<v@?B>44"
+ "v52@0:8@16@24B32B36B40@?44"
+ "v56@0:8@16B24B28@32B40B44@?48"
+ "value"
+ "view controller : %@ @%s"
+ "viewDelegate"
+ "voice capable"
+ "voiceSIMIccid"
+ "waitingStartTime"
+ "webView:insertInputSuggestion:"
+ "without target iccid, matching to %@ @%s"
+ "xmark"
+ "\x82"
+ "\xb1"
+ "\xb4\xd1"
+ "\xe1"
+ "\xf0!"
+ "\xf1"
- "%"
- "%@ plan installed. @%s"
- "%s showAddPlan: %d forceDualSIMSetup: %d @%s"
- "+[TSSIMSetupFlow initActivationCodeRequireSetup:]"
- "+[TSSIMSetupFlow initWithActivationCodeOnlyFlow]"
- "+[TSSIMSetupFlow initWithSetupFlowWithIccid:showAddPlan:]"
- "+[TSSIMSetupFlow initWithSetupFlowWithIccid:showAddPlan:forceDualSIMSetup:]"
- "+[TSSinglePlanTransferViewController getTitleAndDetailsForPlanType:transferCapability:]"
- "-[CrossPlatformTransferOngoingViewController maybeDismissAlert]"
- "-[CrossPlatformTransferOngoingViewController viewDidDisappear:]"
- "-[SSCrossPlatformTransferSourceSelectionViewController _continueButtonTapped:]"
- "-[TSAuthFlow firstViewController]"
- "-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]"
- "-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]_block_invoke"
- "-[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]"
- "-[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]_block_invoke"
- "-[TSCellularPlanActivatingFlow _handleOtpStatusUpdate:]"
- "-[TSCellularPlanActivatingFlow _maybeDeleteTransferBackItem:]"
- "-[TSCellularPlanActivatingFlow _maybeDeleteTransferBackItem:]_block_invoke"
- "-[TSCellularPlanActivatingFlow _onTransferError:]"
- "-[TSCellularPlanActivatingFlow _shouldWaitUntilPhoneNumberBeReady:]_block_invoke"
- "-[TSCellularPlanActivatingFlow firstViewController:]"
- "-[TSCellularPlanActivatingFlow firstViewController]"
- "-[TSCellularPlanActivatingFlow launchWebsheet:completion:]"
- "-[TSCellularPlanActivatingFlow launchWebsheet:completion:]_block_invoke"
- "-[TSCellularPlanActivatingFlow launchWebsheet:completion:]_block_invoke_2"
- "-[TSCellularPlanActivatingFlow nextViewControllerFrom:]"
- "-[TSCellularPlanActivatingFlow offerFallbackOption]_block_invoke"
- "-[TSCellularPlanActivatingFlow planItemsUpdated:planListError:]"
- "-[TSCellularPlanActivatingFlow planItemsUpdated:planListError:]_block_invoke"
- "-[TSCellularPlanActivatingFlow simSetupFlowCompleted:]"
- "-[TSCellularPlanActivatingFlow simSetupFlowCompleted:]_block_invoke"
- "-[TSCellularPlanActivatingFlow transferEventUpdate:]"
- "-[TSCellularPlanCardInfoViewController addNewPlanWithUserInfo:]"
- "-[TSCellularPlanConfirmationCodeViewController confirm:]"
- "-[TSCellularPlanProximityTransferController launchSecureIntentUI:descriptor:isLocalConvertFlow:completion:]"
- "-[TSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke_2"
- "-[TSCellularPlanScanViewController captureOutput:didOutputMetadataObjects:fromConnection:]"
- "-[TSCellularPlanScanViewController captureOutput:didOutputMetadataObjects:fromConnection:]_block_invoke"
- "-[TSCellularSetupActivatingViewController viewDidDisappear:]"
- "-[TSCoreTelephonyClientCache updateSecureIntentData:]"
- "-[TSCrossPlatformSourceAuthFlow _connectToDevice:completion:]"
- "-[TSIDSTransferFlow launchSecureIntentUI:descriptor:isLocalConvertFlow:completion:]"
- "-[TSMultiPlanIntermediateViewController initWithTransferItems:showOtherOptions:]"
- "-[TSProximityTargetTransferFlow nextViewControllerFrom:]"
- "-[TSRecommendedCarrierAppsFlow _requestCarrierAppsWithCompletion:]_block_invoke_2"
- "-[TSSIMSetupFlow getRootFlow]"
- "-[TSSecureIntentGestureViewController _maybeSendExternalizedContext:]"
- "-[TSSecureIntentGestureViewController _updateAuthenticationStatus:]_block_invoke_2"
- "-[TSSecureIntentGestureViewController initWithExternalizedContext:descriptor:isLocalConvertFlow:]"
- "-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke"
- "-[TSTransferFlowModel arePlansAvailable:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke"
- "-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]"
- "-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke"
- "1!"
- "2"
- "@\"TSCellularPlanLabelPickerTableViewController\""
- "@\"UIScrollView\""
- "@\"UITableView\""
- "@24@0:8@\"NSCoder\"16"
- "@32@0:8Q16Q24"
- "@40@0:8@16B24B28@32"
- "@40@0:8@16B24B28B32B36"
- "@52@0:8@16@24B32@36@44"
- "@56@0:8@16B24B28B32@36@44B52"
- "@56@0:8@16B24B28B32B36B40B44@48"
- "@60@0:8B16q20@28Q36@44B52B56"
- "AB"
- "ALLOW"
- "ANDROID"
- "Alert is not currently presented. @%s"
- "Alert is still presented, dismissing it now. @%s"
- "Already activated and return @%s"
- "Android"
- "CONTINUE_BUTTON_STATE_POST_INSTALLING"
- "CROSSPLATFORM_TRANSFER_CONFIRM_DETAIL_%@"
- "CROSSPLATFORM_TRANSFER_CONFIRM_TITLE_%@"
- "CROSSTRANSFER_TIMEOUT_DETAIL"
- "CarrierName"
- "CrossPlatformTransferOngoingViewController"
- "DOUBLE_CLICK_SIDE_BUTTON_%@"
- "DelayStartActivatingTimerKey"
- "Don't have other device, maybe show intro @%s"
- "ERROR: invalid delegate for transfer plan. invoke TSCellularPlanManagerCache directly @%s"
- "ESIM"
- "NOT_ALLOW"
- "NPHCELLULAR_CARD_INFO_CONFIRMATION_CODE_PLACEHOLDER"
- "NSCoding"
- "NSSecureCoding"
- "Not launching websheet in buddy @%s"
- "PLACEHOLDER_KEY"
- "PLAN_TRANSFERRED_DETAIL_%@_%@"
- "PLAN_TRANSFERRED_DETAIL_NO_DEVICE_NAME_%@"
- "PLAN_TRANSFERRED_DETAIL_NO_PHONENUMBER_%@"
- "PRXCARD_SOURCE_COMPLETE_TITLE"
- "Phone number is already available @%s"
- "SIM is not enabled - early return @%s"
- "SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_INELIGIBLE_DETAIL"
- "Skip waiting for phone number to be ready @%s"
- "T@\"<TSSIMSetupFlowDelegate>\",W,N,V_delegate"
- "T@\"CTCellularPlanItem\",&,V_updatePlanItem"
- "T@\"NSError\",&,V_transferError"
- "T@\"NSLayoutConstraint\",W,N,V_infoTableViewHeightConstraint"
- "T@\"NSString\",&,N,V_descriptor"
- "T@\"NSString\",&,V_descriptor"
- "T@\"NSString\",&,V_deviceName"
- "T@\"NSString\",&,V_installingPlanIdentifier"
- "T@\"NSString\",&,V_subscriptionContextUUID"
- "T@\"NSString\",W,V_phoneNumber"
- "T@\"TSCellularPlanLabelPickerTableViewController\",&,V_labelPickerViewController"
- "T@\"TSCellularSetupLoadingView\",&,N,V_loadingView"
- "T@\"UIButton\",W,N,V_btLearnMore"
- "T@\"UIButton\",W,N,V_enterDetailsManuallyButton"
- "T@\"UILabel\",&,V_detailLabel"
- "T@\"UILabel\",W,N,V_confirmationCodeMessageLabel"
- "T@\"UILabel\",W,N,V_confirmationCodeTitleLabel"
- "T@\"UILabel\",W,N,V_enterActivationLabel"
- "T@\"UILabel\",W,N,V_positionQRCodeLabel"
- "T@\"UILabel\",W,N,V_scanQRCodeLabel"
- "T@\"UIScrollView\",W,N,V_scrollView"
- "T@\"UITableView\",W,N,V_infoTableView"
- "T@\"UITextField\",W,N,V_codeTextField"
- "T@\"UIView\",W,N,V_cutoutView"
- "T@\"UIView\",W,N,V_scanView"
- "T@\"UIViewController\",&,V_firstViewController"
- "TABLE_CELL_KEY"
- "TB,R,V_manualCardInfoEntry"
- "TB,V_isSecureIntentFailed"
- "TB,V_isWebsheetFlow"
- "TB,V_planActiveOnSource"
- "TB,V_shouldShowCompletePaneOnTimeout"
- "TB,V_showAlert"
- "TB,V_showConfirmationCodePane"
- "TITLE_KEY"
- "TQ,V_currentActivatingState"
- "TSCellularPlanCardInfoView"
- "TSCellularPlanCardInfoViewController"
- "TSCellularPlanConfirmationCodeView"
- "TSCellularPlanConfirmationCodeViewController"
- "TSCellularPlanLabelPickerTableViewController"
- "TSCellularPlanScanView"
- "TSCellularPlanScanViewController"
- "Td,V_startTime"
- "Time to complete activating for plan type %tu with result %tu : %f  @%s"
- "VALUE_KEY"
- "Wait until phone number to be ready: %@ @%s"
- "WiFi is required to query transfer plans and carrier setup items @%s"
- "[Db] %s - addressField:%@, activationCode:%@, confirmationCode:%@ @%s"
- "[Db] active plan is not the provisioning plan. expect:%@, actual:%@ @%s"
- "[E]empty plan items @%s"
- "[E]invalid navigationController @%s"
- "[E]invalid topview controller @%s"
- "[E]missing CT implementation - rdar://137927148 @%s"
- "[E]provisioning error:%@ @%s"
- "[E]unexpected transfer capability : %lu @%s"
- "[E]unimplemented selector - selectTransferPlans:completion: @%s"
- "_btLearnMore"
- "_confirmationCodeMessageLabel"
- "_confirmationCodeTitleLabel"
- "_currentActivatingState"
- "_descriptor"
- "_detailLabel"
- "_displayOneTimeCodeViewController:carrierName:usePin:"
- "_displayTermsAndConditionsViewController:"
- "_enterActivationLabel"
- "_infoTableView"
- "_infoTableViewHeightConstraint"
- "_installingPlanIdentifier"
- "_isSecureIntentFailed"
- "_isWebsheetFlow"
- "_manualCardInfoEntry"
- "_maybeDisplayConsent:phoneNumber:completion:"
- "_maybeMoveToNextViewController"
- "_maybeSendExternalizedContext:"
- "_onTransferError:"
- "_planActiveOnSource"
- "_positionQRCodeLabel"
- "_promptWithDeviceName:phoneNumber:"
- "_scanButtonTapped"
- "_scanQRCodeLabel"
- "_scrollView"
- "_setUpLabel"
- "_setUpSpinner"
- "_setupLabelContraint"
- "_shouldShowCompletePaneOnTimeout"
- "_shouldWaitUntilPhoneNumberBeReady:"
- "_showAlert"
- "_showConfirmationCodePane"
- "_spinnerStartAnimating"
- "_spinnerStopAnimating"
- "_startTime"
- "_subscriptionContextUUID"
- "_tableData"
- "_transferError"
- "_updateAuthenticationStatus:"
- "activate:"
- "activation complete @%s"
- "activation timed out @%s"
- "addNewPlanWithUserInfo:"
- "already launch failure url, ignore @%s"
- "arePlansAvailable:transferablePlanOnSource:bootstrapOnly:completion:"
- "arrow.turn.up.forward.iphone"
- "bootstrap:completion:"
- "bootstrapPlanTransferForEndpoint:usingMessageSession:completion:"
- "bootstrapPlanTransferUsingMessageSession:completion:"
- "btLearnMore"
- "cancel transfer. start over @%s"
- "checkmark.circle"
- "configureCell:atIndexPath:"
- "confirmationCode:%@ @%s"
- "confirmationCodeMessageLabel"
- "confirmationCodeTitleLabel"
- "convertRect:toView:"
- "currentActivatingState"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "descriptor"
- "detailLabel"
- "e"
- "encodeWithCoder:"
- "enterActivationLabel"
- "enterFauxCardDataManually:"
- "externalized context = %@ @%s"
- "getProximityTransportSession:remoteDeviceInfo:completion:"
- "getRootFlow"
- "getTitleAndDetailsForPlanType:transferCapability:"
- "handleStartOverAgainstNoPlan:navigationController:completion:"
- "ignore the error, launch error Websheet instead @%s"
- "in viewDidLoad secure intent"
- "indexPathWithIndex:"
- "infoTableView"
- "infoTableViewHeightConstraint"
- "initActivationCodeRequireSetup:"
- "initWithActivationCodeOnlyFlow"
- "initWithCoder:"
- "initWithDeviceName:"
- "initWithExternalizedContext:descriptor:isLocalConvertFlow:"
- "initWithFlow:navigationController:"
- "initWithInBuddy:transferablePlans:selectedTransferablePlans:alsPlans:selectedAlsPlans:odaPlans:"
- "initWithOptions:navigationController:"
- "initWithPeerDeviceName:"
- "initWithPhoneNumber:"
- "initWithPhoneNumber:planName:planActiveOnSource:"
- "initWithPlanIdentifer:deviceName:"
- "initWithPlanItemError:updatePlanItem:withBackButton:forCarrier:withCarrierErrorCode:"
- "initWithPlans:planItems:device:"
- "initWithProximitySetupState:"
- "initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:"
- "initWithSetupFlowWithIccid:showAddPlan:"
- "initWithSetupFlowWithIccid:showAddPlan:forceDualSIMSetup:"
- "initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:delayStartActivatingTimer:"
- "initWithTimeoutReason:"
- "initWithTitle:details:symbolName:"
- "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:"
- "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:"
- "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:"
- "initWithTransferItems:showOtherOptions:"
- "initWithTransferOutPlan:toDevice:"
- "initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:"
- "initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isStandaloneProximityFlow:transferBackPhoneNumber:"
- "inject back button action for : %@ @%s"
- "installingPlanIdentifier"
- "isLocalConvertFlow: %d\n"
- "isWebsheetFlow"
- "kTransferWebsheet"
- "lastBaselineAnchor"
- "launchSecureIntentUI:descriptor:isLocalConvertFlow:completion:"
- "learnMoreTapped:"
- "loadingView"
- "manualCardInfoEntry"
- "maybeDismissAlert"
- "offerFallbackOption"
- "origin"
- "planActiveOnSource"
- "positionQRCodeLabel"
- "preferredFontDescriptorWithTextStyle:"
- "push : %@ on : %@ @%s"
- "r"
- "received error already : %@, new error: %@ @%s"
- "redirectToBTFlow"
- "requestPlans:transferablePlanOnSource:bootstrapOnly:completion:"
- "scanQRCodeLabel"
- "scrollRectToVisible:animated:"
- "scrollViewForKeyboardIfNecessary"
- "sendRequest:"
- "setBtLearnMore:"
- "setConfirmationCodeMessageLabel:"
- "setConfirmationCodeTitleLabel:"
- "setContentInset:"
- "setCurrentActivatingState:"
- "setDescriptor:"
- "setDetailLabel:"
- "setDeviceName:"
- "setEnterActivationLabel:"
- "setInfoTableView:"
- "setInfoTableViewHeightConstraint:"
- "setInstallingPlanIdentifier:"
- "setIsSecureIntentFailed:"
- "setIsWebsheetFlow:"
- "setLoadingView:"
- "setPlanActiveOnSource:"
- "setPositionQRCodeLabel:"
- "setScanQRCodeLabel:"
- "setScrollIndicatorInsets:"
- "setScrollView:"
- "setShouldShowCompletePaneOnTimeout:"
- "setShowAlert:"
- "setShowConfirmationCodePane:"
- "setStartTime:"
- "setSubscriptionContextUUID:"
- "setTableHeaderView:"
- "setTransferError:"
- "setUpdatePlanItem:"
- "shouldOfferFallbackOptionOnError:"
- "shouldShowCompletePaneOnTimeout"
- "showConfirmationCodePane"
- "startTime"
- "subscriptionContextUUID"
- "superview"
- "supportsSecureCoding"
- "t"
- "transfer abort, require to launch websheet : %@ @%s"
- "transfer back, enable the item. error:%@ @%s"
- "transfer error already set, ignore @%s"
- "transfer failed : %@ @%s"
- "transferError"
- "updateSecureIntentData:"
- "user tap back to cancel @%s"
- "v24@0:8@\"NSCoder\"16"
- "v40@0:8@16B24B28@?32"
- "v44@0:8@\"NSData\"16@\"NSString\"24B32@?<v@?B>36"
- "\xc1"
- "\xf0c"

```
