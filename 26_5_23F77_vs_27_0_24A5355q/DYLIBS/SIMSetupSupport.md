## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-894.6.0.0.0
-  __TEXT.__text: 0xc14d8
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0xa4cc
-  __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x1d80
-  __TEXT.__cstring: 0x10cf9
-  __TEXT.__oslogstring: 0x6f19
+953.0.0.0.0
+  __TEXT.__text: 0xdb198
+  __TEXT.__objc_methlist: 0xbef4
+  __TEXT.__const: 0x1e8
+  __TEXT.__gcc_except_tab: 0x1f88
+  __TEXT.__cstring: 0x15704
+  __TEXT.__oslogstring: 0x860f
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2870
-  __TEXT.__objc_classname: 0x15de
-  __TEXT.__objc_methname: 0x174ed
-  __TEXT.__objc_methtype: 0x3700
-  __TEXT.__objc_stubs: 0xe960
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x1db8
-  __DATA_CONST.__objc_classlist: 0x488
+  __TEXT.__unwind_info: 0x2e58
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2090
+  __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x53a0
+  __DATA_CONST.__objc_selrefs: 0x5b88
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x430
-  __DATA_CONST.__objc_arraydata: 0x1a8
-  __AUTH_CONST.__auth_got: 0x418
-  __AUTH_CONST.__const: 0x920
-  __AUTH_CONST.__cfstring: 0x7c00
-  __AUTH_CONST.__objc_const: 0x3e140
-  __AUTH_CONST.__objc_intobj: 0x6c0
+  __DATA_CONST.__objc_superrefs: 0x508
+  __DATA_CONST.__objc_arraydata: 0x208
+  __DATA_CONST.__got: 0xbd8
+  __AUTH_CONST.__const: 0xb40
+  __AUTH_CONST.__cfstring: 0x9de0
+  __AUTH_CONST.__objc_const: 0x4dab8
+  __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH.__objc_data: 0x2d00
-  __DATA.__objc_ivar: 0xf28
-  __DATA.__data: 0xbb0
-  __DATA.__bss: 0x170
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x3570
+  __DATA.__objc_ivar: 0x1268
+  __DATA.__data: 0xc70
+  __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E621969-5D11-3711-8504-303B6A297048
-  Functions: 4031
-  Symbols:   14680
-  CStrings:  7686
+  UUID: 9C7C5014-6AAF-3123-8175-5DC1B6C05499
+  Functions: 4740
+  Symbols:   17086
+  CStrings:  4219
 
Symbols:
+ +[SSQuickSwitchBlockerViewController getTitleDetailAndSymbolForAccounts:selfAppleAccountDsids:quickSwitchToTransferPlanMap:]
+ +[TSSIMSetupFlow _maybeCreateSIMConfigFlowAsPreFlow:options:]
+ +[TSUtilities filterQSAccountsWithoutTransferPlan:quickSwitchToTransferPlanMap:]
+ +[TSUtilities filterTransferPlansAlreadyInQuickSwitch:]
+ +[TSUtilities findQuickSwitchAccountInfo:fromAccounts:]
+ +[TSUtilities getMarketingModelName]
+ +[TSUtilities getQuickSwitchErrorTitleDetail:forCarrier:]
+ +[TSUtilities groupHasOrphanPrimary:]
+ +[TSUtilities groupQSAccountsByNonSecondaryIccid:]
+ +[TSUtilities groupQSAccountsByNonSecondaryIccid:].cold.1
+ +[TSUtilities isQSAccountCapable:]
+ +[TSUtilities isSecondaryTwinnedNoTransferWithoutCompanion:inAccounts:quickSwitchToTransferPlanMap:]
+ +[TSUtilities matchTransferPlans:toQSAccounts:]
+ +[TSUtilities shouldOfferQSAccount:serialNumber:]
+ +[TSUtilities shouldOfferQSAccountFromDisplayPlan:serialNumber:]
+ +[TSUtilities shouldShowDevicePicker:]
+ +[TSUtilities transferFlowTypeForAccount:quickSwitchToTransferPlanMap:]
+ -[CTDisplayPlan(SimSetup) deviceID]
+ -[CTDisplayPlan(SimSetup) modelName]
+ -[OBWelcomeController(Spinner) _prepareSpinner].cold.1
+ -[OBWelcomeController(Spinner) _showButtonTraySpinnerWithBusyText:animating:]
+ -[OBWelcomeController(Spinner) _showButtonTraySpinnerWithBusyText:animating:].cold.1
+ -[SSInstallPlanInformation isQuickSwitchSwap]
+ -[SSInstallPlanInformation quickSwitchAccount]
+ -[SSInstallPlanInformation setIsQuickSwitchSwap:]
+ -[SSInstallPlanInformation setQuickSwitchAccount:]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController .cxx_destruct]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController _addIconView]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController _animateIcon]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController _completeFlow]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController action]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController delegate]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController iconView]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController initWithPhoneNumber:result:]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController phoneNumber]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController result]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController setAction:]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController setDelegate:]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController setIconView:]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController setPhoneNumber:]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController setResult:]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController viewDidAppear:]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController viewDidLayoutSubviews]
+ -[SSPRXQuickSwitchPrimaryCompleteViewController viewDidLoad]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController .cxx_destruct]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController _handleDismiss]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController _startEnrollment]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController account]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController action]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController coreTelephonyClient]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController delegate]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController flowType]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController initWithAccount:secondary:flowType:]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController phoneNumber]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController secondary]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController setAccount:]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController setAction:]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController setCoreTelephonyClient:]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController setDelegate:]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController setFlowType:]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController setPhoneNumber:]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController setSecondary:]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController viewDidLayoutSubviews]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController viewDidLoad]
+ -[SSPRXQuickSwitchPrimaryEnrollConsentViewController viewWillAppear:]
+ -[SSPRXQuickSwitchPrimarySettingUpViewController .cxx_destruct]
+ -[SSPRXQuickSwitchPrimarySettingUpViewController delegate]
+ -[SSPRXQuickSwitchPrimarySettingUpViewController setDelegate:]
+ -[SSPRXQuickSwitchPrimarySettingUpViewController viewDidLayoutSubviews]
+ -[SSPRXQuickSwitchPrimarySettingUpViewController viewDidLoad]
+ -[SSPRXQuickSwitchPrimarySettingUpViewController viewWillAppear:]
+ -[SSPRXQuickSwitchPrimarySharingViewController .cxx_destruct]
+ -[SSPRXQuickSwitchPrimarySharingViewController delegate]
+ -[SSPRXQuickSwitchPrimarySharingViewController initWithPhoneNumber:]
+ -[SSPRXQuickSwitchPrimarySharingViewController phoneNumber]
+ -[SSPRXQuickSwitchPrimarySharingViewController setDelegate:]
+ -[SSPRXQuickSwitchPrimarySharingViewController setPhoneNumber:]
+ -[SSPRXQuickSwitchPrimarySharingViewController sharingDidComplete]
+ -[SSPRXQuickSwitchPrimarySharingViewController viewDidLayoutSubviews]
+ -[SSPRXQuickSwitchPrimarySharingViewController viewDidLoad]
+ -[SSPRXQuickSwitchPrimarySharingViewController viewWillAppear:]
+ -[SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController .cxx_destruct]
+ -[SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController delegate]
+ -[SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController setDelegate:]
+ -[SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController viewDidLayoutSubviews]
+ -[SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController viewDidLoad]
+ -[SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController viewWillAppear:]
+ -[SSQuickSwitchActivatingViewController .cxx_destruct]
+ -[SSQuickSwitchActivatingViewController animating]
+ -[SSQuickSwitchActivatingViewController cachedButtons]
+ -[SSQuickSwitchActivatingViewController delegate]
+ -[SSQuickSwitchActivatingViewController initWithPlanInfos:isQuickSwitchSlidingOngoing:]
+ -[SSQuickSwitchActivatingViewController prepare:]
+ -[SSQuickSwitchActivatingViewController setAnimating:]
+ -[SSQuickSwitchActivatingViewController setCachedButtons:]
+ -[SSQuickSwitchActivatingViewController setDelegate:]
+ -[SSQuickSwitchActivatingViewController setSpinner:]
+ -[SSQuickSwitchActivatingViewController setSpinnerContainer:]
+ -[SSQuickSwitchActivatingViewController spinnerContainer]
+ -[SSQuickSwitchActivatingViewController spinner]
+ -[SSQuickSwitchActivatingViewController viewDidLoad]
+ -[SSQuickSwitchActivatingViewController viewWillAppear:]
+ -[SSQuickSwitchAlertViewController .cxx_destruct]
+ -[SSQuickSwitchAlertViewController _transferQuickSwitchAccount]
+ -[SSQuickSwitchAlertViewController delegate]
+ -[SSQuickSwitchAlertViewController initWithNavigationController:account:messageSession:quickSwitchToTransferPlanMap:]
+ -[SSQuickSwitchAlertViewController prepare:]
+ -[SSQuickSwitchAlertViewController setDelegate:]
+ -[SSQuickSwitchAlertViewController userDidConfirm]
+ -[SSQuickSwitchBlockerViewController .cxx_destruct]
+ -[SSQuickSwitchBlockerViewController _continueButtonTapped]
+ -[SSQuickSwitchBlockerViewController _learnMoreButtonTapped]
+ -[SSQuickSwitchBlockerViewController _otherOptionsTapped]
+ -[SSQuickSwitchBlockerViewController delegate]
+ -[SSQuickSwitchBlockerViewController initWithAccounts:selfAppleAccountDsids:quickSwitchToTransferPlanMap:isFirstView:delegate:]
+ -[SSQuickSwitchBlockerViewController isOtherOptionsTapped]
+ -[SSQuickSwitchBlockerViewController prepare:]
+ -[SSQuickSwitchBlockerViewController setDelegate:]
+ -[SSQuickSwitchBlockerViewController viewDidLoad]
+ -[SSQuickSwitchBlockerViewController viewWillAppear:]
+ -[SSQuickSwitchDevicePickerViewController .cxx_destruct]
+ -[SSQuickSwitchDevicePickerViewController _continueButtonTapped:]
+ -[SSQuickSwitchDevicePickerViewController _heightAnchorConstant]
+ -[SSQuickSwitchDevicePickerViewController _otherOptionsTapped]
+ -[SSQuickSwitchDevicePickerViewController _primaryDeviceNameExcluding:]
+ -[SSQuickSwitchDevicePickerViewController _refreshTableView]
+ -[SSQuickSwitchDevicePickerViewController _setupLaterButtonTapped:]
+ -[SSQuickSwitchDevicePickerViewController _showTransferConfirmationAlert]
+ -[SSQuickSwitchDevicePickerViewController continueButton]
+ -[SSQuickSwitchDevicePickerViewController delegate]
+ -[SSQuickSwitchDevicePickerViewController flowType]
+ -[SSQuickSwitchDevicePickerViewController initWithAccounts:messageSession:quickSwitchToTransferPlanMap:isFirstView:delegate:]
+ -[SSQuickSwitchDevicePickerViewController isOtherOptionsTapped]
+ -[SSQuickSwitchDevicePickerViewController numberOfSectionsInTableView:]
+ -[SSQuickSwitchDevicePickerViewController prepare:]
+ -[SSQuickSwitchDevicePickerViewController selectedAccount]
+ -[SSQuickSwitchDevicePickerViewController selectedIndexPath]
+ -[SSQuickSwitchDevicePickerViewController selectedNewLine]
+ -[SSQuickSwitchDevicePickerViewController setContinueButton:]
+ -[SSQuickSwitchDevicePickerViewController setDelegate:]
+ -[SSQuickSwitchDevicePickerViewController setFlowType:]
+ -[SSQuickSwitchDevicePickerViewController setSelectedAccount:]
+ -[SSQuickSwitchDevicePickerViewController setSelectedIndexPath:]
+ -[SSQuickSwitchDevicePickerViewController tableView:cellForRowAtIndexPath:]
+ -[SSQuickSwitchDevicePickerViewController tableView:didSelectRowAtIndexPath:]
+ -[SSQuickSwitchDevicePickerViewController tableView:heightForFooterInSection:]
+ -[SSQuickSwitchDevicePickerViewController tableView:heightForHeaderInSection:]
+ -[SSQuickSwitchDevicePickerViewController tableView:numberOfRowsInSection:]
+ -[SSQuickSwitchDevicePickerViewController tableView:viewForHeaderInSection:]
+ -[SSQuickSwitchDevicePickerViewController viewDidLoad]
+ -[SSQuickSwitchDevicePickerViewController viewWillAppear:]
+ -[SSQuickSwitchEACSSignOutViewController .cxx_destruct]
+ -[SSQuickSwitchEACSSignOutViewController _buildDetailTextWithInfos:flowType:isDeleteESIM:selfSerialNumber:]
+ -[SSQuickSwitchEACSSignOutViewController _cancelButtonTapped]
+ -[SSQuickSwitchEACSSignOutViewController _carrierNameForInfos:]
+ -[SSQuickSwitchEACSSignOutViewController _continueButtonTapped]
+ -[SSQuickSwitchEACSSignOutViewController _deviceNameForInfo:selfSerialNumber:]
+ -[SSQuickSwitchEACSSignOutViewController _groupInfosByRoleAndDevice:selfSerialNumber:]
+ -[SSQuickSwitchEACSSignOutViewController _isCarrierNameFallback:]
+ -[SSQuickSwitchEACSSignOutViewController _isDeviceNameFallback:selfSerialNumber:]
+ -[SSQuickSwitchEACSSignOutViewController _joinPhonesWithOr:]
+ -[SSQuickSwitchEACSSignOutViewController _learnMoreButtonTapped]
+ -[SSQuickSwitchEACSSignOutViewController _numberKeyForPrimary:flowType:isDeleteESIM:plural:deviceIsFallback:]
+ -[SSQuickSwitchEACSSignOutViewController _phoneNumberForInfo:]
+ -[SSQuickSwitchEACSSignOutViewController _preambleForFlowType:]
+ -[SSQuickSwitchEACSSignOutViewController _scanInfos:hasPrimary:hasSecondary:primaryDeviceName:primaryDeviceIsFallback:primaryPhoneNumber:secondaryPhoneNumbers:secondaryDeviceName:secondaryDeviceIsFallback:]
+ -[SSQuickSwitchEACSSignOutViewController _shouldShowConfirmAlertWithInfos:flowType:needsConfirmation:isDeleteESIM:]
+ -[SSQuickSwitchEACSSignOutViewController delegate]
+ -[SSQuickSwitchEACSSignOutViewController initWithNumberSharingInfos:flowType:isDeleteESIM:needsConfirmation:selfSerialNumber:]
+ -[SSQuickSwitchEACSSignOutViewController prepare:]
+ -[SSQuickSwitchEACSSignOutViewController setDelegate:]
+ -[SSQuickSwitchEACSSignOutViewController viewDidLoad]
+ -[SSQuickSwitchEnrollmentConsentViewController .cxx_destruct]
+ -[SSQuickSwitchEnrollmentConsentViewController _continueButtonTapped]
+ -[SSQuickSwitchEnrollmentConsentViewController _continueButtonTapped].cold.1
+ -[SSQuickSwitchEnrollmentConsentViewController delegate]
+ -[SSQuickSwitchEnrollmentConsentViewController flowType]
+ -[SSQuickSwitchEnrollmentConsentViewController initWithAccount:flowType:session:delegate:]
+ -[SSQuickSwitchEnrollmentConsentViewController numberOfSectionsInTableView:]
+ -[SSQuickSwitchEnrollmentConsentViewController prepare:]
+ -[SSQuickSwitchEnrollmentConsentViewController setDelegate:]
+ -[SSQuickSwitchEnrollmentConsentViewController setFlowType:]
+ -[SSQuickSwitchEnrollmentConsentViewController tableView:cellForRowAtIndexPath:]
+ -[SSQuickSwitchEnrollmentConsentViewController tableView:numberOfRowsInSection:]
+ -[SSQuickSwitchEnrollmentConsentViewController viewDidLoad]
+ -[SSQuickSwitchEnrollmentFollowUpFlow .cxx_destruct]
+ -[SSQuickSwitchEnrollmentFollowUpFlow firstViewController:]
+ -[SSQuickSwitchEnrollmentFollowUpFlow firstViewController]
+ -[SSQuickSwitchEnrollmentFollowUpFlow initWithPhoneNumber:]
+ -[SSQuickSwitchEnrollmentFollowUpFlow isBootstrapAssertionRequired]
+ -[SSQuickSwitchFollowUpOnOtherPhoneViewController .cxx_destruct]
+ -[SSQuickSwitchFollowUpOnOtherPhoneViewController _doneButtonTapped]
+ -[SSQuickSwitchFollowUpOnOtherPhoneViewController delegate]
+ -[SSQuickSwitchFollowUpOnOtherPhoneViewController initWithPhoneNumber:]
+ -[SSQuickSwitchFollowUpOnOtherPhoneViewController setDelegate:]
+ -[SSQuickSwitchFollowUpOnOtherPhoneViewController viewDidLoad]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController .cxx_destruct]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController _continueButtonTapped]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController _setUpLaterButtonTapped]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController decisionDelegate]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController delegate]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController initWithPlans:skip:]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController isShown]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController prepare:]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController setDecisionDelegate:]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController setDelegate:]
+ -[SSQuickSwitchIncompleteWebsheetDecisionViewController viewDidLoad]
+ -[SSQuickSwitchLifeCycleChangeFlow .cxx_destruct]
+ -[SSQuickSwitchLifeCycleChangeFlow _currentDeviceSerialNumber]
+ -[SSQuickSwitchLifeCycleChangeFlow client]
+ -[SSQuickSwitchLifeCycleChangeFlow deviceIdentifier]
+ -[SSQuickSwitchLifeCycleChangeFlow firstViewController:]
+ -[SSQuickSwitchLifeCycleChangeFlow firstViewController:].cold.1
+ -[SSQuickSwitchLifeCycleChangeFlow firstViewController:].cold.2
+ -[SSQuickSwitchLifeCycleChangeFlow firstViewController]
+ -[SSQuickSwitchLifeCycleChangeFlow firstViewController].cold.1
+ -[SSQuickSwitchLifeCycleChangeFlow initWithQSLifeCycleChangeFlowType:isDeleteESIM:]
+ -[SSQuickSwitchLifeCycleChangeFlow initWithQSLifeCycleChangeFlowType:isDeleteESIM:deviceIdentifier:needsConfirmation:]
+ -[SSQuickSwitchLifeCycleChangeFlow isDeleteESIM]
+ -[SSQuickSwitchLifeCycleChangeFlow lifeCycleChangeFlowType]
+ -[SSQuickSwitchLifeCycleChangeFlow needsConfirmation]
+ -[SSQuickSwitchLifeCycleChangeFlow setClient:]
+ -[SSQuickSwitchLifeCycleChangeFlow setDeviceIdentifier:]
+ -[SSQuickSwitchLifeCycleChangeFlow setIsDeleteESIM:]
+ -[SSQuickSwitchLifeCycleChangeFlow setLifeCycleChangeFlowType:]
+ -[SSQuickSwitchLifeCycleChangeFlow setNeedsConfirmation:]
+ -[SSQuickSwitchLifeCycleChangeFlow userDidTapCancel]
+ -[SSQuickSwitchListViewController .cxx_destruct]
+ -[SSQuickSwitchListViewController _continueButtonTapped:]
+ -[SSQuickSwitchListViewController _heightAnchorConstant]
+ -[SSQuickSwitchListViewController _otherOptionsTapped]
+ -[SSQuickSwitchListViewController _refreshTableView]
+ -[SSQuickSwitchListViewController _setupLaterButtonTapped:]
+ -[SSQuickSwitchListViewController _showTransferConfirmationAlert]
+ -[SSQuickSwitchListViewController continueButton]
+ -[SSQuickSwitchListViewController delegate]
+ -[SSQuickSwitchListViewController flowType]
+ -[SSQuickSwitchListViewController initWithGroupedAccounts:messageSession:quickSwitchToTransferPlanMap:isFirstView:delegate:]
+ -[SSQuickSwitchListViewController isOtherOptionsTapped]
+ -[SSQuickSwitchListViewController numberOfSectionsInTableView:]
+ -[SSQuickSwitchListViewController prepare:]
+ -[SSQuickSwitchListViewController selectedAccounts]
+ -[SSQuickSwitchListViewController selectedGroupKey]
+ -[SSQuickSwitchListViewController selectedIndexPath]
+ -[SSQuickSwitchListViewController setContinueButton:]
+ -[SSQuickSwitchListViewController setDelegate:]
+ -[SSQuickSwitchListViewController setFlowType:]
+ -[SSQuickSwitchListViewController setSelectedAccounts:]
+ -[SSQuickSwitchListViewController setSelectedGroupKey:]
+ -[SSQuickSwitchListViewController setSelectedIndexPath:]
+ -[SSQuickSwitchListViewController tableView:cellForRowAtIndexPath:]
+ -[SSQuickSwitchListViewController tableView:didSelectRowAtIndexPath:]
+ -[SSQuickSwitchListViewController tableView:heightForFooterInSection:]
+ -[SSQuickSwitchListViewController tableView:heightForHeaderInSection:]
+ -[SSQuickSwitchListViewController tableView:numberOfRowsInSection:]
+ -[SSQuickSwitchListViewController tableView:viewForHeaderInSection:]
+ -[SSQuickSwitchListViewController viewDidLoad]
+ -[SSQuickSwitchListViewController viewWillAppear:]
+ -[SSQuickSwitchNoWiFiViewController .cxx_destruct]
+ -[SSQuickSwitchNoWiFiViewController _doneButtonTapped]
+ -[SSQuickSwitchNoWiFiViewController delegate]
+ -[SSQuickSwitchNoWiFiViewController initWithDelegate:]
+ -[SSQuickSwitchNoWiFiViewController prepare:]
+ -[SSQuickSwitchNoWiFiViewController setDelegate:]
+ -[SSQuickSwitchNoWiFiViewController viewDidLoad]
+ -[SSQuickSwitchPrimaryEnrollmentFlow .cxx_destruct]
+ -[SSQuickSwitchPrimaryEnrollmentFlow _notifyFlowCompletion:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow _notifyQuickSwitchEnrollmentFailure:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow _notifyQuickSwitchEnrollmentFailure:].cold.1
+ -[SSQuickSwitchPrimaryEnrollmentFlow _proxCardFlowDidDismiss]
+ -[SSQuickSwitchPrimaryEnrollmentFlow _startBackgroundTask]
+ -[SSQuickSwitchPrimaryEnrollmentFlow _stopBackgroundTask]
+ -[SSQuickSwitchPrimaryEnrollmentFlow account]
+ -[SSQuickSwitchPrimaryEnrollmentFlow backgroundTask]
+ -[SSQuickSwitchPrimaryEnrollmentFlow client]
+ -[SSQuickSwitchPrimaryEnrollmentFlow didCompleteSecureIntent]
+ -[SSQuickSwitchPrimaryEnrollmentFlow didCompleteSecureIntent].cold.1
+ -[SSQuickSwitchPrimaryEnrollmentFlow didRequestPresentationForProxCard:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow enrollmentResult]
+ -[SSQuickSwitchPrimaryEnrollmentFlow evaluateNextStepFromViewController:completion:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow evaluateNextStepFromViewController:completion:].cold.1
+ -[SSQuickSwitchPrimaryEnrollmentFlow externalizedContext]
+ -[SSQuickSwitchPrimaryEnrollmentFlow firstViewController:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow firstViewController:].cold.1
+ -[SSQuickSwitchPrimaryEnrollmentFlow firstViewController]
+ -[SSQuickSwitchPrimaryEnrollmentFlow firstViewController].cold.1
+ -[SSQuickSwitchPrimaryEnrollmentFlow hasReceivedEnrollmentResult]
+ -[SSQuickSwitchPrimaryEnrollmentFlow initWithAccount:secondary:flowType:messageSession:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow initWithAccount:secondary:flowType:messageSession:].cold.1
+ -[SSQuickSwitchPrimaryEnrollmentFlow isFlowCompleted]
+ -[SSQuickSwitchPrimaryEnrollmentFlow isSecureIntentPending]
+ -[SSQuickSwitchPrimaryEnrollmentFlow isSlidingWebsheetIncomplete]
+ -[SSQuickSwitchPrimaryEnrollmentFlow isWaitingForEnrollmentResult]
+ -[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:].cold.1
+ -[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:].cold.2
+ -[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:].cold.3
+ -[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:completion:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:completion:].cold.1
+ -[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:isQuickSwitchFlow:completion:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow messageSession]
+ -[SSQuickSwitchPrimaryEnrollmentFlow nextViewControllerFrom:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow notifyQuickSwitchEnrollmentResult:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow planDescriptors]
+ -[SSQuickSwitchPrimaryEnrollmentFlow primaryIccid]
+ -[SSQuickSwitchPrimaryEnrollmentFlow quickSwitchFlowType]
+ -[SSQuickSwitchPrimaryEnrollmentFlow secondary]
+ -[SSQuickSwitchPrimaryEnrollmentFlow secureIntentProxCard]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setAccount:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setBackgroundTask:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setClient:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setEnrollmentResult:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setExternalizedContext:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setHasReceivedEnrollmentResult:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setIsFlowCompleted:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setIsSecureIntentPending:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setIsSlidingWebsheetIncomplete:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setIsWaitingForEnrollmentResult:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setMessageSession:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setPlanDescriptors:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setPrimaryIccid:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setQuickSwitchFlowType:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setSecondary:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setSecureIntentProxCard:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setUserIntentContext:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setWebsheetFlow:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow setWebsheetPurchaseCompleted:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow simSetupFlowCompleted:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow updateQuickSwitchEnrollmentStatus:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow userIntentContext]
+ -[SSQuickSwitchPrimaryEnrollmentFlow viewControllerDidComplete:]
+ -[SSQuickSwitchPrimaryEnrollmentFlow websheetFlow]
+ -[SSQuickSwitchPrimaryEnrollmentFlow websheetPurchaseCompleted]
+ -[SSQuickSwitchPublicAPIConsentFlow .cxx_destruct]
+ -[SSQuickSwitchPublicAPIConsentFlow firstViewController:]
+ -[SSQuickSwitchPublicAPIConsentFlow firstViewController]
+ -[SSQuickSwitchPublicAPIConsentFlow initWithIccid:numberSuffix:phoneNumber:secondaryIccid:secondaryPhoneNumber:appName:]
+ -[SSQuickSwitchPublicAPIConsentViewController .cxx_destruct]
+ -[SSQuickSwitchPublicAPIConsentViewController _bodyTextWithPlain:boldSubstring:]
+ -[SSQuickSwitchPublicAPIConsentViewController _buildPhoneNumberTableViewWithPrimary:secondary:]
+ -[SSQuickSwitchPublicAPIConsentViewController _cancelTapped]
+ -[SSQuickSwitchPublicAPIConsentViewController _goToSettingsTapped]
+ -[SSQuickSwitchPublicAPIConsentViewController _verifyAndShareTapped]
+ -[SSQuickSwitchPublicAPIConsentViewController delegate]
+ -[SSQuickSwitchPublicAPIConsentViewController initWithAppName:numberSuffix:]
+ -[SSQuickSwitchPublicAPIConsentViewController initWithAppName:numberSuffix:phoneNumber:iccid:secondaryPhoneNumber:secondaryIccid:]
+ -[SSQuickSwitchPublicAPIConsentViewController initWithAppName:phoneNumber:iccid:]
+ -[SSQuickSwitchPublicAPIConsentViewController prepare:]
+ -[SSQuickSwitchPublicAPIConsentViewController prepare:].cold.1
+ -[SSQuickSwitchPublicAPIConsentViewController setDelegate:]
+ -[SSQuickSwitchPublicAPIConsentViewController tableView:cellForRowAtIndexPath:]
+ -[SSQuickSwitchPublicAPIConsentViewController tableView:didSelectRowAtIndexPath:]
+ -[SSQuickSwitchPublicAPIConsentViewController tableView:numberOfRowsInSection:]
+ -[SSQuickSwitchPublicAPIConsentViewController viewDidLayoutSubviews]
+ -[SSQuickSwitchPublicAPIConsentViewController viewDidLoad]
+ -[SSQuickSwitchSecondaryEnrollmentFlow .cxx_destruct]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _capableAccounts]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _consentViewControllerForAccount:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _createQuickSwitchEnrollmentSubflow:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _createQuickSwitchEnrollmentSubflow:].cold.1
+ -[SSQuickSwitchSecondaryEnrollmentFlow _filterOnDeviceTransferredPlan:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _firstViewController]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _getCarrierSetupWithCompletion:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _getQSAccountsWithMessageSession:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _maybePresentFirstViewController:firstViewControllerCallback:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _maybePresentFirstViewController:firstViewControllerCallback:].cold.1
+ -[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:].cold.1
+ -[SSQuickSwitchSecondaryEnrollmentFlow accounts]
+ -[SSQuickSwitchSecondaryEnrollmentFlow cancelButton]
+ -[SSQuickSwitchSecondaryEnrollmentFlow carrierSetupItems]
+ -[SSQuickSwitchSecondaryEnrollmentFlow firstViewController:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow firstViewController]
+ -[SSQuickSwitchSecondaryEnrollmentFlow firstViewController].cold.1
+ -[SSQuickSwitchSecondaryEnrollmentFlow groupedAccounts]
+ -[SSQuickSwitchSecondaryEnrollmentFlow hadOnDeviceTransferredPlan]
+ -[SSQuickSwitchSecondaryEnrollmentFlow initWithMessageSession:accounts:primarySerialNumber:carrierSetupItems:sourceOSVersion:sourceDeviceClass:isFirstView:quickSwitchToTransferPlanMap:quickSwitchFlowType:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow messageSession]
+ -[SSQuickSwitchSecondaryEnrollmentFlow nextViewControllerFrom:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow noWiFiOnOldDevice]
+ -[SSQuickSwitchSecondaryEnrollmentFlow notifyQuickSwitchEnrollmentResult:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow primarySerialNumber]
+ -[SSQuickSwitchSecondaryEnrollmentFlow quickSwitchFlowType]
+ -[SSQuickSwitchSecondaryEnrollmentFlow quickSwitchToTransferPlanMap]
+ -[SSQuickSwitchSecondaryEnrollmentFlow selectedAccount]
+ -[SSQuickSwitchSecondaryEnrollmentFlow selfAppleAccountDsids]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setAccounts:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setCancelButton:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setCancelNavigationBarItems:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setCarrierSetupItems:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setGroupedAccounts:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setHadOnDeviceTransferredPlan:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setMessageSession:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setNoWiFiOnOldDevice:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setPrimarySerialNumber:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setQuickSwitchFlowType:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setQuickSwitchToTransferPlanMap:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setSelectedAccount:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setSelfAppleAccountDsids:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setSourceDeviceClass:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setSourceOSVersion:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow setTransferPlans:]
+ -[SSQuickSwitchSecondaryEnrollmentFlow sourceDeviceClass]
+ -[SSQuickSwitchSecondaryEnrollmentFlow sourceOSVersion]
+ -[SSQuickSwitchSecondaryEnrollmentFlow transferPlans]
+ -[SSQuickSwitchSecondaryEnrollmentFlow updateQuickSwitchEnrollmentStatus:]
+ -[SSQuickSwitchSecondarySharingViewController .cxx_destruct]
+ -[SSQuickSwitchSecondarySharingViewController _continueButtonTapped:]
+ -[SSQuickSwitchSecondarySharingViewController _heightAnchorConstant]
+ -[SSQuickSwitchSecondarySharingViewController _otherButtonTapped]
+ -[SSQuickSwitchSecondarySharingViewController _refreshTableView]
+ -[SSQuickSwitchSecondarySharingViewController _setupLaterButtonTapped:]
+ -[SSQuickSwitchSecondarySharingViewController _shareOptionSubtext]
+ -[SSQuickSwitchSecondarySharingViewController _showTransferConfirmationAlert]
+ -[SSQuickSwitchSecondarySharingViewController _transferQuickSwitchAccount:]
+ -[SSQuickSwitchSecondarySharingViewController accounts]
+ -[SSQuickSwitchSecondarySharingViewController continueButton]
+ -[SSQuickSwitchSecondarySharingViewController delegate]
+ -[SSQuickSwitchSecondarySharingViewController flowType]
+ -[SSQuickSwitchSecondarySharingViewController initWithAccounts:hasTransferPlans:blockerViewNeeded:showConfirmationAlert:messageSession:quickSwitchToTransferPlanMap:delegate:]
+ -[SSQuickSwitchSecondarySharingViewController isOtherButtonTapped]
+ -[SSQuickSwitchSecondarySharingViewController isShown]
+ -[SSQuickSwitchSecondarySharingViewController numberOfSectionsInTableView:]
+ -[SSQuickSwitchSecondarySharingViewController prepare:]
+ -[SSQuickSwitchSecondarySharingViewController selectedIndexPath]
+ -[SSQuickSwitchSecondarySharingViewController selectedOption]
+ -[SSQuickSwitchSecondarySharingViewController setAccounts:]
+ -[SSQuickSwitchSecondarySharingViewController setContinueButton:]
+ -[SSQuickSwitchSecondarySharingViewController setDelegate:]
+ -[SSQuickSwitchSecondarySharingViewController setFlowType:]
+ -[SSQuickSwitchSecondarySharingViewController setIsOtherButtonTapped:]
+ -[SSQuickSwitchSecondarySharingViewController setIsShown:]
+ -[SSQuickSwitchSecondarySharingViewController setSelectedIndexPath:]
+ -[SSQuickSwitchSecondarySharingViewController setSelectedOption:]
+ -[SSQuickSwitchSecondarySharingViewController tableView:cellForRowAtIndexPath:]
+ -[SSQuickSwitchSecondarySharingViewController tableView:didSelectRowAtIndexPath:]
+ -[SSQuickSwitchSecondarySharingViewController tableView:heightForFooterInSection:]
+ -[SSQuickSwitchSecondarySharingViewController tableView:heightForHeaderInSection:]
+ -[SSQuickSwitchSecondarySharingViewController tableView:numberOfRowsInSection:]
+ -[SSQuickSwitchSecondarySharingViewController tableView:viewForHeaderInSection:]
+ -[SSQuickSwitchSecondarySharingViewController viewDidLoad]
+ -[SSQuickSwitchSecondarySharingViewController viewWillAppear:]
+ -[SSQuickSwitchSlidingChoiceViewController .cxx_destruct]
+ -[SSQuickSwitchSlidingChoiceViewController _continueButtonTapped:]
+ -[SSQuickSwitchSlidingChoiceViewController _refreshTableView]
+ -[SSQuickSwitchSlidingChoiceViewController continueButton]
+ -[SSQuickSwitchSlidingChoiceViewController delegate]
+ -[SSQuickSwitchSlidingChoiceViewController flowType]
+ -[SSQuickSwitchSlidingChoiceViewController initWithAccount:session:delegate:]
+ -[SSQuickSwitchSlidingChoiceViewController numberOfSectionsInTableView:]
+ -[SSQuickSwitchSlidingChoiceViewController selectedIndexPath]
+ -[SSQuickSwitchSlidingChoiceViewController setContinueButton:]
+ -[SSQuickSwitchSlidingChoiceViewController setDelegate:]
+ -[SSQuickSwitchSlidingChoiceViewController setSelectedIndexPath:]
+ -[SSQuickSwitchSlidingChoiceViewController tableView:cellForRowAtIndexPath:]
+ -[SSQuickSwitchSlidingChoiceViewController tableView:didSelectRowAtIndexPath:]
+ -[SSQuickSwitchSlidingChoiceViewController tableView:heightForFooterInSection:]
+ -[SSQuickSwitchSlidingChoiceViewController tableView:heightForHeaderInSection:]
+ -[SSQuickSwitchSlidingChoiceViewController tableView:numberOfRowsInSection:]
+ -[SSQuickSwitchSlidingChoiceViewController tableView:viewForHeaderInSection:]
+ -[SSQuickSwitchSlidingChoiceViewController viewDidLoad]
+ -[SSQuickSwitchSwapConsentViewController .cxx_destruct]
+ -[SSQuickSwitchSwapConsentViewController _cancelButtonTapped]
+ -[SSQuickSwitchSwapConsentViewController _continueButtonTapped]
+ -[SSQuickSwitchSwapConsentViewController _initiateSwapTransfer]
+ -[SSQuickSwitchSwapConsentViewController _setNavigationItems]
+ -[SSQuickSwitchSwapConsentViewController animating]
+ -[SSQuickSwitchSwapConsentViewController cachedButtons]
+ -[SSQuickSwitchSwapConsentViewController client]
+ -[SSQuickSwitchSwapConsentViewController delegate]
+ -[SSQuickSwitchSwapConsentViewController initWithPrimaryAccount:delegate:]
+ -[SSQuickSwitchSwapConsentViewController prepare:]
+ -[SSQuickSwitchSwapConsentViewController primaryAccount]
+ -[SSQuickSwitchSwapConsentViewController setAnimating:]
+ -[SSQuickSwitchSwapConsentViewController setCachedButtons:]
+ -[SSQuickSwitchSwapConsentViewController setClient:]
+ -[SSQuickSwitchSwapConsentViewController setDelegate:]
+ -[SSQuickSwitchSwapConsentViewController setPrimaryAccount:]
+ -[SSQuickSwitchSwapConsentViewController setSpinner:]
+ -[SSQuickSwitchSwapConsentViewController setSpinnerContainer:]
+ -[SSQuickSwitchSwapConsentViewController spinnerContainer]
+ -[SSQuickSwitchSwapConsentViewController spinner]
+ -[SSQuickSwitchSwapConsentViewController viewDidAppear:]
+ -[SSQuickSwitchSwapConsentViewController viewDidLoad]
+ -[SSQuickSwitchSwapFlow .cxx_destruct]
+ -[SSQuickSwitchSwapFlow _createActivatingSubflow]
+ -[SSQuickSwitchSwapFlow _createActivatingSubflow].cold.1
+ -[SSQuickSwitchSwapFlow client]
+ -[SSQuickSwitchSwapFlow firstViewController:]
+ -[SSQuickSwitchSwapFlow firstViewController:].cold.1
+ -[SSQuickSwitchSwapFlow firstViewController:].cold.2
+ -[SSQuickSwitchSwapFlow firstViewController]
+ -[SSQuickSwitchSwapFlow firstViewController].cold.1
+ -[SSQuickSwitchSwapFlow iccid]
+ -[SSQuickSwitchSwapFlow initWithIccid:]
+ -[SSQuickSwitchSwapFlow nextViewControllerFrom:]
+ -[SSQuickSwitchSwapFlow primaryAccount]
+ -[SSQuickSwitchSwapFlow setClient:]
+ -[SSQuickSwitchSwapFlow setIccid:]
+ -[SSQuickSwitchSwapFlow setPrimaryAccount:]
+ -[SSQuickSwitchWaitOnWebsheetViewController .cxx_destruct]
+ -[SSQuickSwitchWaitOnWebsheetViewController delegate]
+ -[SSQuickSwitchWaitOnWebsheetViewController initWithPlanInfos:isQuickSwitchSlidingOngoing:]
+ -[SSQuickSwitchWaitOnWebsheetViewController prepare:]
+ -[SSQuickSwitchWaitOnWebsheetViewController setDelegate:]
+ -[SSQuickSwitchWaitOnWebsheetViewController viewDidLoad]
+ -[SSQuickSwitchWaitSourceConsentViewController .cxx_destruct]
+ -[SSQuickSwitchWaitSourceConsentViewController delegate]
+ -[SSQuickSwitchWaitSourceConsentViewController initWithPlanInfos:]
+ -[SSQuickSwitchWaitSourceConsentViewController prepare:]
+ -[SSQuickSwitchWaitSourceConsentViewController setDelegate:]
+ -[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]
+ -[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:].cold.1
+ -[TSActivationFlowWithSimSetupFlow didPurchasePlanSuccessfullyWithEid:imei:meid:iccid:alternateSDMP:matchingId:state:]
+ -[TSActivationFlowWithSimSetupFlow didPurchasePlanSuccessfullyWithEid:imei:meid:iccid:alternateSDMP:matchingId:state:].cold.1
+ -[TSActivationFlowWithSimSetupFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:matchingId:state:]
+ -[TSActivationFlowWithSimSetupFlow quickSwitchPlans]
+ -[TSActivationFlowWithSimSetupFlow quickSwitchToTransferPlanMap]
+ -[TSActivationFlowWithSimSetupFlow setQuickSwitchPlans:]
+ -[TSActivationFlowWithSimSetupFlow setQuickSwitchToTransferPlanMap:]
+ -[TSAuthFlow _firstViewControllerForLegacyFlow:]
+ -[TSAuthFlow _firstViewControllerWithUserIntentContext:]
+ -[TSAuthFlow evaluateNextStepFromViewController:completion:]
+ -[TSAuthFlow evaluateNextStepFromViewController:completion:].cold.1
+ -[TSAuthFlow initWithExternalizedContext:descriptors:userIntentContext:]
+ -[TSAuthFlow setUserIntentContext:]
+ -[TSAuthFlow userIntentContext]
+ -[TSCarrierSignupFlow _showLoadFailureAlert:error:]
+ -[TSCellularPlanActivatingFlow initWithQuickSwitchAccount:isSwap:iccid:quickSwitchFlowType:]
+ -[TSCellularPlanActivatingFlow isQuickSwitchOngoing]
+ -[TSCellularPlanActivatingFlow quickSwitchFlowType]
+ -[TSCellularPlanActivatingFlow setIsQuickSwitchOngoing:]
+ -[TSCellularPlanActivatingFlow setQuickSwitchFlowType:]
+ -[TSCellularPlanActivatingFlow setSharedPhoneNumber:]
+ -[TSCellularPlanActivatingFlow sharedPhoneNumber]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) launchQuickSwitchSetup:completion:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) notifyQuickSwitchEnrollmentResult:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) notifyQuickSwitchEnrollmentResult:].cold.1
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) updateQuickSwitchEnrollmentStatus:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) updateQuickSwitchEnrollmentStatus:].cold.1
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) updateQuickSwitchEnrollmentStatus:].cold.2
+ -[TSCellularPlanActivatingFlow(SSQuickSwitchIncompleteWebsheetDecision) resolveIncompleteWebsheetWithFollowup:]
+ -[TSCellularPlanActivatingFlow(SSQuickSwitchIncompleteWebsheetDecision) resolveIncompleteWebsheetWithFollowup:].cold.1
+ -[TSCellularPlanActivatingFlow(SecureIntent) evaluateNextStepFromViewController:completion:]
+ -[TSCellularPlanActivatingFlow(SecureIntent) evaluateNextStepFromViewController:completion:].cold.1
+ -[TSCellularPlanActivatingFlow(SecureIntent) proxCardFlowDidDismiss]
+ -[TSCellularPlanActivatingFlow(SecureIntent) proxCardFlowDidDismiss].cold.1
+ -[TSCellularPlanManagerCache didTransferPlanForEid:iccid:srcIccid:smdpURL:matchingId:state:]
+ -[TSCellularSetupActivatingViewController _maybeShowQuickSwitchAlert]
+ -[TSCellularSetupActivatingViewController initWithQuickSwitchPlan:]
+ -[TSCellularSetupActivatingViewController plan]
+ -[TSCellularSetupActivatingViewController setPlan:]
+ -[TSCellularSetupActivatingViewController setShouldShowSharingText:]
+ -[TSCellularSetupActivatingViewController shouldShowSharingText]
+ -[TSCellularSetupActivatingViewController viewDidAppear:]
+ -[TSCellularSetupCompleteViewController _getTitleAndDetailText:selectedItems:isForCrossPlatformTransfer:]
+ -[TSCellularSetupCompleteViewController initWithPlans:selectedItems:skip:isForCrossPlatformTransfer:quickSwitchFlowType:]
+ -[TSCellularSetupCompleteViewController quickSwitchFlowType]
+ -[TSCellularSetupCompleteViewController setQuickSwitchFlowType:]
+ -[TSCoreTelephonyClientCache getAppleAccountDsids]
+ -[TSCoreTelephonyClientCache isESIMUnavailable]
+ -[TSCoreTelephonyClientCache loadSimSetupInfo:].cold.3
+ -[TSCoreTelephonyClientCache saveSimSetupInfo:info:].cold.2
+ -[TSCoreTelephonyClientCache setSupportsDynamicSIMConfigurationCache:]
+ -[TSCoreTelephonyClientCache supportsDynamicSIMConfigurationCache]
+ -[TSCoreTelephonyClientCache supportsDynamicSIMConfiguration]
+ -[TSCoreTelephonyClientCache supportsDynamicSIMConfiguration].cold.1
+ -[TSCoreTelephonyClientCache updateQuickSwitchConsentResult:iccid:]
+ -[TSCoreTelephonyClientCache updateQuickSwitchConsentResult:iccid:].cold.1
+ -[TSMultiPlanIntermediateViewController _continueButtonTapped:]
+ -[TSMultiPlanIntermediateViewController _isSingleOption]
+ -[TSMultiPlanIntermediateViewController _refreshTableView]
+ -[TSMultiPlanIntermediateViewController _sectionTypeForSection:]
+ -[TSMultiPlanIntermediateViewController continueButton]
+ -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:]
+ -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:].cold.1
+ -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:].cold.2
+ -[TSMultiPlanIntermediateViewController isQuickSwitchCellTapped]
+ -[TSMultiPlanIntermediateViewController selectedIndexPath]
+ -[TSMultiPlanIntermediateViewController setContinueButton:]
+ -[TSMultiPlanIntermediateViewController setIsQuickSwitchCellTapped:]
+ -[TSMultiPlanIntermediateViewController setSelectedIndexPath:]
+ -[TSPRXSIMTransferringViewController otpDetectionStartTime]
+ -[TSPRXSIMTransferringViewController setOtpDetectionStartTime:]
+ -[TSPostMigrationFlow loadSimSetupInfo]
+ -[TSPostMigrationFlow setUserSelectedQSOption:]
+ -[TSPostMigrationFlow userSelectedQSOption]
+ -[TSRemotePlanSignUpFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:matchingId:state:]
+ -[TSSIMSetupFlow dealloc]
+ -[TSSecureIntentGestureViewController _evaluateNextStepFromSelf:]
+ -[TSSecureIntentGestureViewController _evaluateNextStepFromSelf:].cold.1
+ -[TSSecureIntentGestureViewController _handleEvaluateAccessControlResponse:]
+ -[TSSecureIntentGestureViewController _isQuickSwitch]
+ -[TSSecureIntentGestureViewController _updateAuthenticationStatus:]
+ -[TSSecureIntentGestureViewController initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:quickSwitchFlowType:]
+ -[TSSecureIntentGestureViewController initWithExternalizedContext:descriptors:userIntentContext:viewDelegate:]
+ -[TSSecureIntentGestureViewController initWithExternalizedContext:descriptors:userIntentContext:viewDelegate:quickSwitchFlowType:]
+ -[TSSecureIntentGestureViewController quickSwitchFlowType]
+ -[TSSecureIntentGestureViewController setQuickSwitchFlowType:]
+ -[TSSecureIntentGestureViewController setUserIntentContext:]
+ -[TSSecureIntentGestureViewController setViewDelegate:]
+ -[TSSecureIntentGestureViewController userIntentContext]
+ -[TSSecureIntentGestureViewController viewDelegate]
+ -[TSTransferCloudFlowModel cachedD2DTransferPlans]
+ -[TSTransferCloudFlowModel isD2dDeferView]
+ -[TSTransferCloudFlowModel setCachedD2DTransferPlans:]
+ -[TSTransferCloudFlowModel setIsD2dDeferView:]
+ -[TSTransferFlow _saveSimsetupD2dInfo:shouldDeferView:]
+ -[TSTransferFlowModel bootstrap:isPostMigrationFlow:isUsingPreSharedKey:completion:]
+ -[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferPlans:completion:]
+ -[TSTravelBuddyViewController _getSubTextForSectionWithoutLazuli:]
+ -[TSTravelBuddyViewController _isPlanRegisteredForLazuli:]
+ -[TSTravelBuddyViewController _isPlanRegisteredForLazuli:].cold.1
+ -[TSTravelBuddyViewController _isPlanRegisteredForLazuli:].cold.2
+ -[TSTravelBuddyViewController _isPlanRegisteredForLazuli:].cold.3
+ -[TSTravelSimCapabilitySelectionViewController installPlans]
+ -[TSTravelSimCapabilitySelectionViewController setInstallPlans:]
+ -[TSUserInPurchaseFlowAssertion .cxx_destruct]
+ -[TSUserInPurchaseFlowAssertion deassertUserInPurchaseFlowWithForce:caller:].cold.1
+ -[TSWebsheetSignupFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:matchingId:state:]
+ -[TSWebsheetSignupFlow initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:]
+ -[TSWebsheetSignupFlow setUseCase:]
+ -[TSWebsheetSignupFlow useCase]
+ GCC_except_table131
+ GCC_except_table137
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table158
+ GCC_except_table166
+ GCC_except_table203
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table29
+ GCC_except_table40
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table75
+ GCC_except_table82
+ GCC_except_table90
+ GCC_except_table91
+ _CGAffineTransformIdentity
+ _CTPlanTransferStatusTimeoutAfterQSTransferDone
+ _CTQuickSwitchFlowTypeAsString
+ _CTQuickSwitchLifecycleStateAsString
+ _CTQuickSwitchRoleAsString
+ _NSParagraphStyleAttributeName
+ _OBJC_CLASS_$_CTDisplayPlanList
+ _OBJC_CLASS_$_CTQuickSwitchAccountInfo
+ _OBJC_CLASS_$_CTQuickSwitchDeviceInfo
+ _OBJC_CLASS_$_CTUserIntentContext
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMutableParagraphStyle
+ _OBJC_CLASS_$_NSTextAttachment
+ _OBJC_CLASS_$_SSPRXQuickSwitchPrimaryCompleteViewController
+ _OBJC_CLASS_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController
+ _OBJC_CLASS_$_SSPRXQuickSwitchPrimarySettingUpViewController
+ _OBJC_CLASS_$_SSPRXQuickSwitchPrimarySharingViewController
+ _OBJC_CLASS_$_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController
+ _OBJC_CLASS_$_SSQuickSwitchActivatingViewController
+ _OBJC_CLASS_$_SSQuickSwitchAlertViewController
+ _OBJC_CLASS_$_SSQuickSwitchBlockerViewController
+ _OBJC_CLASS_$_SSQuickSwitchDevicePickerViewController
+ _OBJC_CLASS_$_SSQuickSwitchEACSSignOutViewController
+ _OBJC_CLASS_$_SSQuickSwitchEnrollmentConsentViewController
+ _OBJC_CLASS_$_SSQuickSwitchEnrollmentFollowUpFlow
+ _OBJC_CLASS_$_SSQuickSwitchFollowUpOnOtherPhoneViewController
+ _OBJC_CLASS_$_SSQuickSwitchIncompleteWebsheetDecisionViewController
+ _OBJC_CLASS_$_SSQuickSwitchLifeCycleChangeFlow
+ _OBJC_CLASS_$_SSQuickSwitchListViewController
+ _OBJC_CLASS_$_SSQuickSwitchNoWiFiViewController
+ _OBJC_CLASS_$_SSQuickSwitchPrimaryEnrollmentFlow
+ _OBJC_CLASS_$_SSQuickSwitchPublicAPIConsentFlow
+ _OBJC_CLASS_$_SSQuickSwitchPublicAPIConsentViewController
+ _OBJC_CLASS_$_SSQuickSwitchSecondaryEnrollmentFlow
+ _OBJC_CLASS_$_SSQuickSwitchSecondarySharingViewController
+ _OBJC_CLASS_$_SSQuickSwitchSlidingChoiceViewController
+ _OBJC_CLASS_$_SSQuickSwitchSwapConsentViewController
+ _OBJC_CLASS_$_SSQuickSwitchSwapFlow
+ _OBJC_CLASS_$_SSQuickSwitchWaitOnWebsheetViewController
+ _OBJC_CLASS_$_SSQuickSwitchWaitSourceConsentViewController
+ _OBJC_CLASS_$_UIFontDescriptor
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ _OBJC_CLASS_$_UIGraphicsImageRendererFormat
+ _OBJC_CLASS_$_UIListContentConfiguration
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_SSInstallPlanInformation._isQuickSwitchSwap
+ _OBJC_IVAR_$_SSInstallPlanInformation._quickSwitchAccount
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryCompleteViewController._action
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryCompleteViewController._delegate
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryCompleteViewController._iconView
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryCompleteViewController._phoneNumber
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryCompleteViewController._result
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController._account
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController._action
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController._coreTelephonyClient
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController._delegate
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController._flowType
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController._phoneNumber
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController._secondary
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimarySettingUpViewController._delegate
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimarySharingViewController._delegate
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimarySharingViewController._phoneNumber
+ _OBJC_IVAR_$_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchActivatingViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchActivatingViewController._isQuickSwitchSlidingOngoing
+ _OBJC_IVAR_$_SSQuickSwitchActivatingViewController._planInfos
+ _OBJC_IVAR_$_SSQuickSwitchActivatingViewController.animating
+ _OBJC_IVAR_$_SSQuickSwitchActivatingViewController.cachedButtons
+ _OBJC_IVAR_$_SSQuickSwitchActivatingViewController.spinner
+ _OBJC_IVAR_$_SSQuickSwitchActivatingViewController.spinnerContainer
+ _OBJC_IVAR_$_SSQuickSwitchAlertViewController._account
+ _OBJC_IVAR_$_SSQuickSwitchAlertViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchAlertViewController._messageSession
+ _OBJC_IVAR_$_SSQuickSwitchAlertViewController._navigationController
+ _OBJC_IVAR_$_SSQuickSwitchAlertViewController._quickSwitchToTransferPlanMap
+ _OBJC_IVAR_$_SSQuickSwitchAlertViewController._userDidConfirm
+ _OBJC_IVAR_$_SSQuickSwitchBlockerViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchBlockerViewController._isFirstView
+ _OBJC_IVAR_$_SSQuickSwitchBlockerViewController._isOtherOptionsTapped
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._accounts
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._client
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._continueButton
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._flowType
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._hasOrphanPrimary
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._isFirstView
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._isOtherOptionsTapped
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._messageSession
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._newLineSectionIndex
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._quickSwitchToTransferPlanMap
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._selectedAccount
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._selectedIndexPath
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._selectedNewLine
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._setupLaterButton
+ _OBJC_IVAR_$_SSQuickSwitchDevicePickerViewController._tableHeightAnchor
+ _OBJC_IVAR_$_SSQuickSwitchEACSSignOutViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchEACSSignOutViewController._flowType
+ _OBJC_IVAR_$_SSQuickSwitchEACSSignOutViewController._infos
+ _OBJC_IVAR_$_SSQuickSwitchEACSSignOutViewController._isDeleteESIM
+ _OBJC_IVAR_$_SSQuickSwitchEACSSignOutViewController._needsConfirmation
+ _OBJC_IVAR_$_SSQuickSwitchEACSSignOutViewController._selfSerialNumber
+ _OBJC_IVAR_$_SSQuickSwitchEACSSignOutViewController._showsConfirmAlert
+ _OBJC_IVAR_$_SSQuickSwitchEnrollmentConsentViewController._account
+ _OBJC_IVAR_$_SSQuickSwitchEnrollmentConsentViewController._client
+ _OBJC_IVAR_$_SSQuickSwitchEnrollmentConsentViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchEnrollmentConsentViewController._flowType
+ _OBJC_IVAR_$_SSQuickSwitchEnrollmentConsentViewController._session
+ _OBJC_IVAR_$_SSQuickSwitchEnrollmentFollowUpFlow._phoneNumber
+ _OBJC_IVAR_$_SSQuickSwitchFollowUpOnOtherPhoneViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchIncompleteWebsheetDecisionViewController._decisionDelegate
+ _OBJC_IVAR_$_SSQuickSwitchIncompleteWebsheetDecisionViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchIncompleteWebsheetDecisionViewController._installPlans
+ _OBJC_IVAR_$_SSQuickSwitchIncompleteWebsheetDecisionViewController._isShown
+ _OBJC_IVAR_$_SSQuickSwitchIncompleteWebsheetDecisionViewController._skip
+ _OBJC_IVAR_$_SSQuickSwitchLifeCycleChangeFlow._client
+ _OBJC_IVAR_$_SSQuickSwitchLifeCycleChangeFlow._deviceIdentifier
+ _OBJC_IVAR_$_SSQuickSwitchLifeCycleChangeFlow._isDeleteESIM
+ _OBJC_IVAR_$_SSQuickSwitchLifeCycleChangeFlow._lifeCycleChangeFlowType
+ _OBJC_IVAR_$_SSQuickSwitchLifeCycleChangeFlow._needsConfirmation
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._allAccounts
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._client
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._continueButton
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._flowType
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._groupedAccounts
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._isFirstView
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._isOtherOptionsTapped
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._messageSession
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._quickSwitchToTransferPlanMap
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._selectedAccounts
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._selectedGroupKey
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._selectedIndexPath
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._setupLaterButton
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._sortedKeys
+ _OBJC_IVAR_$_SSQuickSwitchListViewController._tableHeightAnchor
+ _OBJC_IVAR_$_SSQuickSwitchNoWiFiViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._account
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._backgroundTask
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._client
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._enrollmentResult
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._externalizedContext
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._hasReceivedEnrollmentResult
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._isFlowCompleted
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._isSecureIntentPending
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._isSlidingWebsheetIncomplete
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._isWaitingForEnrollmentResult
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._messageSession
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._planDescriptors
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._primaryIccid
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._quickSwitchFlowType
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._secondary
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._secureIntentProxCard
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._userIntentContext
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._websheetFlow
+ _OBJC_IVAR_$_SSQuickSwitchPrimaryEnrollmentFlow._websheetPurchaseCompleted
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentFlow._appName
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentFlow._iccid
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentFlow._numberSuffix
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentFlow._phoneNumber
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentFlow._secondaryIccid
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentFlow._secondaryPhoneNumber
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._appName
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._bodyLabel
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._consentCase
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._iccid
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._numberSuffix
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._phoneNumber
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._phoneNumberLabels
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._phoneNumberTableView
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._secondaryIccid
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._secondaryPhoneNumber
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._selectedIndex
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._tableViewHeightConstraint
+ _OBJC_IVAR_$_SSQuickSwitchPublicAPIConsentViewController._verifyAction
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._accounts
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._cancelButton
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._carrierSetupItems
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._client
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._groupedAccounts
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._hadOnDeviceTransferredPlan
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._isFirstView
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._messageSession
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._noWiFiOnOldDevice
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._primarySerialNumber
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._queryGroup
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._quickSwitchFlowType
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._quickSwitchToTransferPlanMap
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._selectedAccount
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._selfAppleAccountDsids
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._simsetupQSInfo
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._sourceDeviceClass
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._sourceOSVersion
+ _OBJC_IVAR_$_SSQuickSwitchSecondaryEnrollmentFlow._transferPlans
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._accounts
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._blockerViewNeeded
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._client
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._continueButton
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._flowType
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._hasTransferPlans
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._isOtherButtonTapped
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._isShown
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._isSingleOption
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._messageSession
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._quickSwitchToTransferPlanMap
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._selectedAccount
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._selectedIndexPath
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._selectedOption
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._setupLaterButton
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._showConfirmationAlert
+ _OBJC_IVAR_$_SSQuickSwitchSecondarySharingViewController._tableHeightAnchor
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._account
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._client
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._continueButton
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._deviceName
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._flowType
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._selectedIndexPath
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._session
+ _OBJC_IVAR_$_SSQuickSwitchSlidingChoiceViewController._tableHeightAnchor
+ _OBJC_IVAR_$_SSQuickSwitchSwapConsentViewController._animating
+ _OBJC_IVAR_$_SSQuickSwitchSwapConsentViewController._cachedButtons
+ _OBJC_IVAR_$_SSQuickSwitchSwapConsentViewController._client
+ _OBJC_IVAR_$_SSQuickSwitchSwapConsentViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchSwapConsentViewController._primaryAccount
+ _OBJC_IVAR_$_SSQuickSwitchSwapConsentViewController._spinner
+ _OBJC_IVAR_$_SSQuickSwitchSwapConsentViewController._spinnerContainer
+ _OBJC_IVAR_$_SSQuickSwitchSwapFlow._client
+ _OBJC_IVAR_$_SSQuickSwitchSwapFlow._iccid
+ _OBJC_IVAR_$_SSQuickSwitchSwapFlow._primaryAccount
+ _OBJC_IVAR_$_SSQuickSwitchWaitOnWebsheetViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchWaitOnWebsheetViewController._isQuickSwitchSlidingOngoing
+ _OBJC_IVAR_$_SSQuickSwitchWaitSourceConsentViewController._delegate
+ _OBJC_IVAR_$_SSQuickSwitchWaitSourceConsentViewController._planInfos
+ _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._quickSwitchPlans
+ _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._quickSwitchToTransferPlanMap
+ _OBJC_IVAR_$_TSAuthFlow._userIntentContext
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._isQuickSwitchOngoing
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._isSecureIntentPending
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._isWebsheetIncomplete
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._quickSwitchFlowType
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._secureIntentDescriptors
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._secureIntentExternalizedContext
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._secureIntentUserIntentContext
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._sharedPhoneNumber
+ _OBJC_IVAR_$_TSCellularSetupActivatingViewController._plan
+ _OBJC_IVAR_$_TSCellularSetupActivatingViewController._shouldShowSharingText
+ _OBJC_IVAR_$_TSCellularSetupCompleteViewController._quickSwitchFlowType
+ _OBJC_IVAR_$_TSCoreTelephonyClientCache._supportsDynamicSIMConfigurationCache
+ _OBJC_IVAR_$_TSMidOperationFailureViewController._isQuickSwitch
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._continueButton
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._isQuickSwitchCellTapped
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._selectedIndexPath
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._showQuickSwitchOption
+ _OBJC_IVAR_$_TSMultiPlanIntermediateViewController._showTransferOption
+ _OBJC_IVAR_$_TSPRXSIMTransferringViewController._otpDetectionStartTime
+ _OBJC_IVAR_$_TSPostMigrationFlow._userSelectedQSOption
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._quickSwitchFlowType
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._userIntentContext
+ _OBJC_IVAR_$_TSSecureIntentGestureViewController._viewDelegate
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._cachedD2DTransferPlans
+ _OBJC_IVAR_$_TSTransferCloudFlowModel._isD2dDeferView
+ _OBJC_IVAR_$_TSUserInPurchaseFlowAssertion._client
+ _OBJC_IVAR_$_TSWebsheetSignupFlow._useCase
+ _OBJC_METACLASS_$_SSPRXQuickSwitchPrimaryCompleteViewController
+ _OBJC_METACLASS_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController
+ _OBJC_METACLASS_$_SSPRXQuickSwitchPrimarySettingUpViewController
+ _OBJC_METACLASS_$_SSPRXQuickSwitchPrimarySharingViewController
+ _OBJC_METACLASS_$_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController
+ _OBJC_METACLASS_$_SSQuickSwitchActivatingViewController
+ _OBJC_METACLASS_$_SSQuickSwitchAlertViewController
+ _OBJC_METACLASS_$_SSQuickSwitchBlockerViewController
+ _OBJC_METACLASS_$_SSQuickSwitchDevicePickerViewController
+ _OBJC_METACLASS_$_SSQuickSwitchEACSSignOutViewController
+ _OBJC_METACLASS_$_SSQuickSwitchEnrollmentConsentViewController
+ _OBJC_METACLASS_$_SSQuickSwitchEnrollmentFollowUpFlow
+ _OBJC_METACLASS_$_SSQuickSwitchFollowUpOnOtherPhoneViewController
+ _OBJC_METACLASS_$_SSQuickSwitchIncompleteWebsheetDecisionViewController
+ _OBJC_METACLASS_$_SSQuickSwitchLifeCycleChangeFlow
+ _OBJC_METACLASS_$_SSQuickSwitchListViewController
+ _OBJC_METACLASS_$_SSQuickSwitchNoWiFiViewController
+ _OBJC_METACLASS_$_SSQuickSwitchPrimaryEnrollmentFlow
+ _OBJC_METACLASS_$_SSQuickSwitchPublicAPIConsentFlow
+ _OBJC_METACLASS_$_SSQuickSwitchPublicAPIConsentViewController
+ _OBJC_METACLASS_$_SSQuickSwitchSecondaryEnrollmentFlow
+ _OBJC_METACLASS_$_SSQuickSwitchSecondarySharingViewController
+ _OBJC_METACLASS_$_SSQuickSwitchSlidingChoiceViewController
+ _OBJC_METACLASS_$_SSQuickSwitchSwapConsentViewController
+ _OBJC_METACLASS_$_SSQuickSwitchSwapFlow
+ _OBJC_METACLASS_$_SSQuickSwitchWaitOnWebsheetViewController
+ _OBJC_METACLASS_$_SSQuickSwitchWaitSourceConsentViewController
+ _TSSIMSetupInfoCachedTransferPlans
+ _TSSIMSetupInfoDeferView
+ _TSSIMSetupInfoDualeSimCapabilityLoss
+ _TSSIMSetupInfoFlexPolicyOn
+ _TSSIMSetupInfoQSInfo
+ _TSSIMSetupInfoUserSelectedQSOption
+ _TSUserInfoCarrierSetupItemsKey
+ _TSUserInfoDeviceIdentifierKey
+ _TSUserInfoIsDeleteESIMKey
+ _TSUserInfoIsSecondaryKey
+ _TSUserInfoIsSwapKey
+ _TSUserInfoNeedsConfirmationKey
+ _TSUserInfoQSLifeCycleChangeFlowTypeKey
+ _TSUserInfoQuickSwitchAccount
+ _TSUserInfoQuickSwitchAccountKey
+ _TSUserInfoQuickSwitchAccountsKey
+ _TSUserInfoQuickSwitchConsentAppNameKey
+ _TSUserInfoQuickSwitchConsentIccidKey
+ _TSUserInfoQuickSwitchConsentNumberSuffixKey
+ _TSUserInfoQuickSwitchConsentPhoneNumberKey
+ _TSUserInfoQuickSwitchConsentSecondaryIccidKey
+ _TSUserInfoQuickSwitchConsentSecondaryPhoneNumberKey
+ _TSUserInfoQuickSwitchDeviceKey
+ _TSUserInfoQuickSwitchEnrollmentFlowTypeKey
+ _TSUserInfoQuickSwitchFlowTypeKey
+ _TSUserInfoQuickSwitchFollowUpPhoneNumberKey
+ _TSUserInfoQuickSwitchTransferPlanMapKey
+ _TSUserInfoSourceDeviceClassKey
+ _TSUserInfoSourceSerialNumberKey
+ _TSUserInfoUseCase
+ _TSUserInfoUserIntentContextKey
+ _UIFontTextStyleTitle2
+ _UILayoutFittingCompressedSize
+ __OBJC_$_CLASS_METHODS_SSQuickSwitchBlockerViewController
+ __OBJC_$_INSTANCE_METHODS_SSPRXQuickSwitchPrimaryCompleteViewController
+ __OBJC_$_INSTANCE_METHODS_SSPRXQuickSwitchPrimaryEnrollConsentViewController
+ __OBJC_$_INSTANCE_METHODS_SSPRXQuickSwitchPrimarySettingUpViewController
+ __OBJC_$_INSTANCE_METHODS_SSPRXQuickSwitchPrimarySharingViewController
+ __OBJC_$_INSTANCE_METHODS_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchActivatingViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchAlertViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchBlockerViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchDevicePickerViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchEACSSignOutViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchEnrollmentConsentViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchEnrollmentFollowUpFlow
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchFollowUpOnOtherPhoneViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchIncompleteWebsheetDecisionViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchLifeCycleChangeFlow
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchListViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchNoWiFiViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchPrimaryEnrollmentFlow
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchPublicAPIConsentFlow
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchPublicAPIConsentViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchSecondaryEnrollmentFlow
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchSecondarySharingViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchSlidingChoiceViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchSwapConsentViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchSwapFlow
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchWaitOnWebsheetViewController
+ __OBJC_$_INSTANCE_METHODS_SSQuickSwitchWaitSourceConsentViewController
+ __OBJC_$_INSTANCE_METHODS_TSCellularPlanActivatingFlow(Override|SSQuickSwitchIncompleteWebsheetDecision|TSCellularPlanManagerCacheDelegate|CoreTelephonyClientCellularPlanManagementDelegate|CoreTelephonyClientQuickSwitchEnrollmentDelegate|TSSIMSetupDelegate|TSSIMSetupFlowDelegate|Single|Consolidated|UpdatePlanInfo|InteractiveUI|SecureIntent)
+ __OBJC_$_INSTANCE_VARIABLES_SSPRXQuickSwitchPrimaryCompleteViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSPRXQuickSwitchPrimaryEnrollConsentViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSPRXQuickSwitchPrimarySettingUpViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSPRXQuickSwitchPrimarySharingViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchActivatingViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchAlertViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchBlockerViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchDevicePickerViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchEACSSignOutViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchEnrollmentConsentViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchEnrollmentFollowUpFlow
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchFollowUpOnOtherPhoneViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchIncompleteWebsheetDecisionViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchLifeCycleChangeFlow
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchListViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchNoWiFiViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchPrimaryEnrollmentFlow
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchPublicAPIConsentFlow
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchPublicAPIConsentViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchSecondaryEnrollmentFlow
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchSecondarySharingViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchSlidingChoiceViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchSwapConsentViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchSwapFlow
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchWaitOnWebsheetViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSQuickSwitchWaitSourceConsentViewController
+ __OBJC_$_PROP_LIST_SSPRXQuickSwitchPrimaryCompleteViewController
+ __OBJC_$_PROP_LIST_SSPRXQuickSwitchPrimaryEnrollConsentViewController
+ __OBJC_$_PROP_LIST_SSPRXQuickSwitchPrimarySettingUpViewController
+ __OBJC_$_PROP_LIST_SSPRXQuickSwitchPrimarySharingViewController
+ __OBJC_$_PROP_LIST_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchActivatingViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchAlertViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchBlockerViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchDevicePickerViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchEACSSignOutViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchEnrollmentConsentViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchFollowUpOnOtherPhoneViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchIncompleteWebsheetDecisionViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchLifeCycleChangeFlow
+ __OBJC_$_PROP_LIST_SSQuickSwitchListViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchNoWiFiViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchPrimaryEnrollmentFlow
+ __OBJC_$_PROP_LIST_SSQuickSwitchPublicAPIConsentViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchSecondaryEnrollmentFlow
+ __OBJC_$_PROP_LIST_SSQuickSwitchSecondarySharingViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchSlidingChoiceViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchSwapConsentViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchSwapFlow
+ __OBJC_$_PROP_LIST_SSQuickSwitchWaitOnWebsheetViewController
+ __OBJC_$_PROP_LIST_SSQuickSwitchWaitSourceConsentViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientQuickSwitchEnrollmentDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSQuickSwitchIncompleteWebsheetDecisionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TSSecureIntentGestureViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientQuickSwitchEnrollmentDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSQuickSwitchIncompleteWebsheetDecisionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TSSecureIntentGestureViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientQuickSwitchEnrollmentDelegate
+ __OBJC_$_PROTOCOL_REFS_SSQuickSwitchIncompleteWebsheetDecisionDelegate
+ __OBJC_$_PROTOCOL_REFS_TSSecureIntentGestureViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SSPRXQuickSwitchPrimaryCompleteViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSPRXQuickSwitchPrimarySettingUpViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSPRXQuickSwitchPrimarySharingViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchActivatingViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchAlertViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchBlockerViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchDevicePickerViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchEACSSignOutViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchEnrollmentConsentViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchFollowUpOnOtherPhoneViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchIncompleteWebsheetDecisionViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchLifeCycleChangeFlow
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchListViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchNoWiFiViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchPrimaryEnrollmentFlow
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchPublicAPIConsentViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchSecondaryEnrollmentFlow
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchSecondarySharingViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchSlidingChoiceViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchSwapConsentViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchSwapFlow
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchWaitOnWebsheetViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSQuickSwitchWaitSourceConsentViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSCellularPlanActivatingFlow(Override|SSQuickSwitchIncompleteWebsheetDecision|TSCellularPlanManagerCacheDelegate|CoreTelephonyClientCellularPlanManagementDelegate|CoreTelephonyClientQuickSwitchEnrollmentDelegate|TSSIMSetupDelegate|TSSIMSetupFlowDelegate|Single|Consolidated|UpdatePlanInfo|InteractiveUI|SecureIntent)
+ __OBJC_CLASS_RO_$_SSPRXQuickSwitchPrimaryCompleteViewController
+ __OBJC_CLASS_RO_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController
+ __OBJC_CLASS_RO_$_SSPRXQuickSwitchPrimarySettingUpViewController
+ __OBJC_CLASS_RO_$_SSPRXQuickSwitchPrimarySharingViewController
+ __OBJC_CLASS_RO_$_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchActivatingViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchAlertViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchBlockerViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchDevicePickerViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchEACSSignOutViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchEnrollmentConsentViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchEnrollmentFollowUpFlow
+ __OBJC_CLASS_RO_$_SSQuickSwitchFollowUpOnOtherPhoneViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchIncompleteWebsheetDecisionViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchLifeCycleChangeFlow
+ __OBJC_CLASS_RO_$_SSQuickSwitchListViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchNoWiFiViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchPrimaryEnrollmentFlow
+ __OBJC_CLASS_RO_$_SSQuickSwitchPublicAPIConsentFlow
+ __OBJC_CLASS_RO_$_SSQuickSwitchPublicAPIConsentViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchSecondaryEnrollmentFlow
+ __OBJC_CLASS_RO_$_SSQuickSwitchSecondarySharingViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchSlidingChoiceViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchSwapConsentViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchSwapFlow
+ __OBJC_CLASS_RO_$_SSQuickSwitchWaitOnWebsheetViewController
+ __OBJC_CLASS_RO_$_SSQuickSwitchWaitSourceConsentViewController
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientQuickSwitchEnrollmentDelegate
+ __OBJC_LABEL_PROTOCOL_$_SSQuickSwitchIncompleteWebsheetDecisionDelegate
+ __OBJC_LABEL_PROTOCOL_$_TSSecureIntentGestureViewControllerDelegate
+ __OBJC_METACLASS_RO_$_SSPRXQuickSwitchPrimaryCompleteViewController
+ __OBJC_METACLASS_RO_$_SSPRXQuickSwitchPrimaryEnrollConsentViewController
+ __OBJC_METACLASS_RO_$_SSPRXQuickSwitchPrimarySettingUpViewController
+ __OBJC_METACLASS_RO_$_SSPRXQuickSwitchPrimarySharingViewController
+ __OBJC_METACLASS_RO_$_SSPRXQuickSwitchPrimaryWebsheetIncompleteViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchActivatingViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchAlertViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchBlockerViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchDevicePickerViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchEACSSignOutViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchEnrollmentConsentViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchEnrollmentFollowUpFlow
+ __OBJC_METACLASS_RO_$_SSQuickSwitchFollowUpOnOtherPhoneViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchIncompleteWebsheetDecisionViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchLifeCycleChangeFlow
+ __OBJC_METACLASS_RO_$_SSQuickSwitchListViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchNoWiFiViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchPrimaryEnrollmentFlow
+ __OBJC_METACLASS_RO_$_SSQuickSwitchPublicAPIConsentFlow
+ __OBJC_METACLASS_RO_$_SSQuickSwitchPublicAPIConsentViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchSecondaryEnrollmentFlow
+ __OBJC_METACLASS_RO_$_SSQuickSwitchSecondarySharingViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchSlidingChoiceViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchSwapConsentViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchSwapFlow
+ __OBJC_METACLASS_RO_$_SSQuickSwitchWaitOnWebsheetViewController
+ __OBJC_METACLASS_RO_$_SSQuickSwitchWaitSourceConsentViewController
+ __OBJC_PROTOCOL_$_CoreTelephonyClientQuickSwitchEnrollmentDelegate
+ __OBJC_PROTOCOL_$_SSQuickSwitchIncompleteWebsheetDecisionDelegate
+ __OBJC_PROTOCOL_$_TSSecureIntentGestureViewControllerDelegate
+ ___101-[SSQuickSwitchSecondaryEnrollmentFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke
+ ___101-[SSQuickSwitchSecondaryEnrollmentFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke.cold.1
+ ___108-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferPlans:completion:]_block_invoke
+ ___111-[TSCellularPlanActivatingFlow(SSQuickSwitchIncompleteWebsheetDecision) resolveIncompleteWebsheetWithFollowup:]_block_invoke
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.534
+ ___116-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) launchQuickSwitchSetup:completion:]_block_invoke
+ ___116-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) launchQuickSwitchSetup:completion:]_block_invoke.cold.1
+ ___117-[TSRemotePlanSignUpFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:matchingId:state:]_block_invoke
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke.42
+ ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke.44
+ ___166-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:isQuickSwitchFlow:completion:]_block_invoke
+ ___166-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:isQuickSwitchFlow:completion:]_block_invoke_2
+ ___166-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:isQuickSwitchFlow:completion:]_block_invoke_2.cold.1
+ ___39-[TSTransferFlow _firstViewController:]_block_invoke.196
+ ___44-[SSQuickSwitchAlertViewController prepare:]_block_invoke
+ ___44-[SSQuickSwitchAlertViewController prepare:]_block_invoke.45
+ ___44-[SSQuickSwitchAlertViewController prepare:]_block_invoke.45.cold.1
+ ___44-[SSQuickSwitchAlertViewController prepare:]_block_invoke.cold.1
+ ___44-[TSTransferFlowModel requestCarrierSetups:]_block_invoke.38
+ ___44-[TSWebsheetSignupFlow firstViewController:]_block_invoke
+ ___45-[SSQuickSwitchSwapFlow firstViewController:]_block_invoke
+ ___45-[SSQuickSwitchSwapFlow firstViewController:]_block_invoke.cold.1
+ ___45-[SSQuickSwitchSwapFlow firstViewController:]_block_invoke.cold.2
+ ___45-[SSQuickSwitchSwapFlow firstViewController:]_block_invoke.cold.3
+ ___47-[TSSecureIntentGestureViewController prepare:]_block_invoke.106
+ ___47-[TSSecureIntentGestureViewController prepare:]_block_invoke_3
+ ___48-[TSAuthFlow _firstViewControllerForLegacyFlow:]_block_invoke
+ ___49-[TSCellularPlanQRCodeScannerView layoutSubviews]_block_invoke
+ ___49-[TSTransferCloudFlowModel requestCarrierSetups:]_block_invoke.40
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.34
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.34.cold.1
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.34.cold.2
+ ___50-[SSQRCodeIntroViewController _laterButtonTapped:]_block_invoke
+ ___50-[SSQRCodeIntroViewController _laterButtonTapped:]_block_invoke_2
+ ___50-[TSTravelSimTypeSelectionViewController prepare:]_block_invoke.cold.1
+ ___51-[TSCarrierSignupFlow _showLoadFailureAlert:error:]_block_invoke
+ ___51-[TSCarrierSignupFlow _showLoadFailureAlert:error:]_block_invoke_2
+ ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke.80
+ ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke_3
+ ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke_2
+ ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke_2.cold.1
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.225
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.227
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.226
+ ___53-[TSTravelBuddyViewController _continueButtonTapped:]_block_invoke.124
+ ___55+[TSUtilities filterTransferPlansAlreadyInQuickSwitch:]_block_invoke
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.29
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.29.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.31
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.31.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.32
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.32.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.33
+ ___56-[SSQuickSwitchLifeCycleChangeFlow firstViewController:]_block_invoke
+ ___56-[SSQuickSwitchLifeCycleChangeFlow firstViewController:]_block_invoke.25
+ ___56-[SSQuickSwitchLifeCycleChangeFlow firstViewController:]_block_invoke.25.cold.1
+ ___56-[SSQuickSwitchLifeCycleChangeFlow firstViewController:]_block_invoke.25.cold.2
+ ___56-[SSQuickSwitchLifeCycleChangeFlow firstViewController:]_block_invoke.cold.1
+ ___56-[SSQuickSwitchLifeCycleChangeFlow firstViewController:]_block_invoke.cold.2
+ ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.34
+ ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.34.cold.1
+ ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.35
+ ___56-[TSAuthFlow _firstViewControllerWithUserIntentContext:]_block_invoke
+ ___56-[TSPRXIdentityShareViewController _maybeFlowCompleted:]_block_invoke
+ ___57-[SSQuickSwitchPublicAPIConsentFlow firstViewController:]_block_invoke
+ ___58-[SSQuickSwitchPrimaryEnrollmentFlow _startBackgroundTask]_block_invoke
+ ___58-[SSQuickSwitchPublicAPIConsentViewController viewDidLoad]_block_invoke
+ ___58-[SSQuickSwitchPublicAPIConsentViewController viewDidLoad]_block_invoke_2
+ ___58-[SSQuickSwitchPublicAPIConsentViewController viewDidLoad]_block_invoke_3
+ ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke.89
+ ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke_2
+ ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke_2.cold.1
+ ___60-[SSPRXQuickSwitchPrimaryCompleteViewController viewDidLoad]_block_invoke
+ ___60-[SSQuickSwitchPrimaryEnrollmentFlow simSetupFlowCompleted:]_block_invoke
+ ___60-[SSQuickSwitchPrimaryEnrollmentFlow simSetupFlowCompleted:]_block_invoke.67
+ ___60-[SSQuickSwitchSecondaryEnrollmentFlow firstViewController:]_block_invoke
+ ___60-[SSQuickSwitchSecondaryEnrollmentFlow firstViewController:]_block_invoke.43
+ ___60-[SSQuickSwitchSecondaryEnrollmentFlow firstViewController:]_block_invoke.43.cold.1
+ ___60-[SSQuickSwitchSecondaryEnrollmentFlow firstViewController:]_block_invoke.cold.1
+ ___60-[TSAuthFlow evaluateNextStepFromViewController:completion:]_block_invoke
+ ___60-[TSAuthFlow evaluateNextStepFromViewController:completion:]_block_invoke.26
+ ___61-[SSPRXQuickSwitchPrimaryCompleteViewController _animateIcon]_block_invoke
+ ___61-[SSPRXQuickSwitchPrimaryCompleteViewController _animateIcon]_block_invoke_2
+ ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.166
+ ___62-[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:]_block_invoke
+ ___62-[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:]_block_invoke.70
+ ___62-[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:]_block_invoke.70.cold.1
+ ___62-[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:]_block_invoke.70.cold.2
+ ___62-[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:]_block_invoke.cold.1
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.187
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.190
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke_2.cold.1
+ ___63-[SSQuickSwitchAlertViewController _transferQuickSwitchAccount]_block_invoke
+ ___63-[SSQuickSwitchAlertViewController _transferQuickSwitchAccount]_block_invoke.cold.1
+ ___63-[SSQuickSwitchEACSSignOutViewController _continueButtonTapped]_block_invoke
+ ___63-[SSQuickSwitchEACSSignOutViewController _continueButtonTapped]_block_invoke_2
+ ___63-[SSQuickSwitchSwapConsentViewController _initiateSwapTransfer]_block_invoke
+ ___63-[SSQuickSwitchSwapConsentViewController _initiateSwapTransfer]_block_invoke.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.101
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.101.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.102
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.102.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.103
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.103.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.107.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.107.cold.2
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.109
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.114
+ ___64-[TSPRXSIMTransferringViewController _setupOneTimeCodeDetection]_block_invoke.66
+ ___64-[TSPRXSIMTransferringViewController _setupOneTimeCodeDetection]_block_invoke.cold.2
+ ___65-[SSPRXQuickSwitchPrimaryEnrollConsentViewController viewDidLoad]_block_invoke
+ ___65-[SSPRXQuickSwitchPrimaryEnrollConsentViewController viewDidLoad]_block_invoke_2
+ ___65-[SSQuickSwitchListViewController _showTransferConfirmationAlert]_block_invoke
+ ___65-[SSQuickSwitchListViewController _showTransferConfirmationAlert]_block_invoke.104
+ ___65-[SSQuickSwitchListViewController _showTransferConfirmationAlert]_block_invoke.104.cold.1
+ ___65-[SSQuickSwitchListViewController _showTransferConfirmationAlert]_block_invoke.98
+ ___65-[SSQuickSwitchListViewController _showTransferConfirmationAlert]_block_invoke.98.cold.1
+ ___65-[SSQuickSwitchListViewController _showTransferConfirmationAlert]_block_invoke.cold.1
+ ___66-[SSQuickSwitchSlidingChoiceViewController _continueButtonTapped:]_block_invoke
+ ___66-[SSQuickSwitchSlidingChoiceViewController _continueButtonTapped:]_block_invoke.cold.1
+ ___67-[TSSecureIntentGestureViewController _updateAuthenticationStatus:]_block_invoke
+ ___67-[TSSecureIntentGestureViewController _updateAuthenticationStatus:]_block_invoke_2
+ ___68-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]_block_invoke
+ ___68-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]_block_invoke.59
+ ___68-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]_block_invoke.59.cold.1
+ ___68-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]_block_invoke.60
+ ___68-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]_block_invoke.60.cold.1
+ ___68-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]_block_invoke.61
+ ___68-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]_block_invoke.cold.1
+ ___69-[SSQuickSwitchEnrollmentConsentViewController _continueButtonTapped]_block_invoke
+ ___69-[SSQuickSwitchEnrollmentConsentViewController _continueButtonTapped]_block_invoke.cold.1
+ ___69-[TSCellularPlanIntroViewController tableView:cellForRowAtIndexPath:]_block_invoke
+ ___70-[SSPRXQuickSwitchPrimaryEnrollConsentViewController _startEnrollment]_block_invoke
+ ___70-[SSPRXQuickSwitchPrimaryEnrollConsentViewController _startEnrollment]_block_invoke.cold.1
+ ___70-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:completion:]_block_invoke
+ ___70-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:completion:]_block_invoke.cold.1
+ ___70-[TSCellularSetupLoadingViewController safariViewControllerDidFinish:]_block_invoke.133
+ ___71-[SSQuickSwitchSecondaryEnrollmentFlow _getCarrierSetupWithCompletion:]_block_invoke
+ ___71-[SSQuickSwitchSecondaryEnrollmentFlow _getCarrierSetupWithCompletion:]_block_invoke.cold.1
+ ___72-[SSQuickSwitchPrimaryEnrollmentFlow didRequestPresentationForProxCard:]_block_invoke
+ ___72-[SSQuickSwitchPrimaryEnrollmentFlow didRequestPresentationForProxCard:]_block_invoke.cold.1
+ ___72-[SSQuickSwitchPrimaryEnrollmentFlow didRequestPresentationForProxCard:]_block_invoke.cold.2
+ ___72-[SSQuickSwitchPrimaryEnrollmentFlow notifyQuickSwitchEnrollmentResult:]_block_invoke
+ ___72-[SSQuickSwitchPrimaryEnrollmentFlow notifyQuickSwitchEnrollmentResult:]_block_invoke.56
+ ___72-[SSQuickSwitchPrimaryEnrollmentFlow updateQuickSwitchEnrollmentStatus:]_block_invoke
+ ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.125
+ ___73-[SSQuickSwitchDevicePickerViewController _showTransferConfirmationAlert]_block_invoke
+ ___73-[SSQuickSwitchDevicePickerViewController _showTransferConfirmationAlert]_block_invoke.93
+ ___73-[SSQuickSwitchDevicePickerViewController _showTransferConfirmationAlert]_block_invoke.93.cold.1
+ ___73-[SSQuickSwitchDevicePickerViewController _showTransferConfirmationAlert]_block_invoke.99
+ ___73-[SSQuickSwitchDevicePickerViewController _showTransferConfirmationAlert]_block_invoke.99.cold.1
+ ___73-[SSQuickSwitchDevicePickerViewController _showTransferConfirmationAlert]_block_invoke.cold.1
+ ___73-[SSQuickSwitchSecondaryEnrollmentFlow _getQSAccountsWithMessageSession:]_block_invoke
+ ___73-[SSQuickSwitchSecondaryEnrollmentFlow _getQSAccountsWithMessageSession:]_block_invoke.64
+ ___73-[SSQuickSwitchSecondaryEnrollmentFlow _getQSAccountsWithMessageSession:]_block_invoke.cold.1
+ ___73-[SSQuickSwitchSecondaryEnrollmentFlow _getQSAccountsWithMessageSession:]_block_invoke.cold.2
+ ___74-[SSQuickSwitchPrimaryEnrollmentFlow _notifyQuickSwitchEnrollmentFailure:]_block_invoke
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.623
+ ___74-[TSUserInPurchaseFlowAssertion assertUserInPurchaseFlowStartOver:caller:]_block_invoke
+ ___74-[TSUserInPurchaseFlowAssertion assertUserInPurchaseFlowStartOver:caller:]_block_invoke.cold.1
+ ___75-[SSQuickSwitchSecondarySharingViewController _transferQuickSwitchAccount:]_block_invoke
+ ___75-[SSQuickSwitchSecondarySharingViewController _transferQuickSwitchAccount:]_block_invoke.cold.1
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.119
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.119.cold.1
+ ___76-[TSSecureIntentGestureViewController _handleEvaluateAccessControlResponse:]_block_invoke
+ ___76-[TSSecureIntentGestureViewController _handleEvaluateAccessControlResponse:]_block_invoke_2
+ ___77-[SSQuickSwitchSecondarySharingViewController _showTransferConfirmationAlert]_block_invoke
+ ___77-[SSQuickSwitchSecondarySharingViewController _showTransferConfirmationAlert]_block_invoke.112
+ ___77-[SSQuickSwitchSecondarySharingViewController _showTransferConfirmationAlert]_block_invoke.112.cold.1
+ ___77-[SSQuickSwitchSecondarySharingViewController _showTransferConfirmationAlert]_block_invoke.cold.1
+ ___79-[TSCellularSetupLoadingViewController setupCoreTelephonyClientForRemoteSignup]_block_invoke.100
+ ___80+[TSUtilities filterQSAccountsWithoutTransferPlan:quickSwitchToTransferPlanMap:]_block_invoke
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.685
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.634
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.634.cold.1
+ ___84-[SSQuickSwitchPrimaryEnrollmentFlow evaluateNextStepFromViewController:completion:]_block_invoke
+ ___84-[SSQuickSwitchPrimaryEnrollmentFlow evaluateNextStepFromViewController:completion:]_block_invoke_2
+ ___85-[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:]_block_invoke
+ ___85-[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:]_block_invoke.54
+ ___85-[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:]_block_invoke.cold.1
+ ___85-[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:]_block_invoke_2
+ ___90-[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke
+ ___90-[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke.115
+ ___90-[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke.cold.1
+ ___90-[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke.cold.2
+ ___92-[TSCellularPlanActivatingFlow(SecureIntent) evaluateNextStepFromViewController:completion:]_block_invoke
+ ___92-[TSCellularPlanActivatingFlow(SecureIntent) evaluateNextStepFromViewController:completion:]_block_invoke_2
+ ___94-[SSQuickSwitchSecondaryEnrollmentFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke
+ ___94-[SSQuickSwitchSecondaryEnrollmentFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke.68
+ ___94-[SSQuickSwitchSecondaryEnrollmentFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke.cold.1
+ ___94-[SSQuickSwitchSecondaryEnrollmentFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke.cold.2
+ ___95-[TSWebsheetSignupFlow didPurchasePlanSuccessfullyWithEid:imei:meid:iccid:alternateSDMP:state:]_block_invoke
+ ___block_descriptor_32_e40_B24?0"CTDisplayPlan"8"NSDictionary"16l
+ ___block_descriptor_32_e51_B24?0"CTQuickSwitchAccountInfo"8"NSDictionary"16l
+ ___block_descriptor_33_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8
+ ___block_descriptor_40_e8_32s_e51_B24?0"CTQuickSwitchAccountInfo"8"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32w_e20_v20?0B8"NSError"12lw32l8
+ ___block_descriptor_40_e8_32w_e29_v24?0"NSArray"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32bs40w_e46_v24?0"CTQuickSwitchAccountInfo"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32w40w_e8_v16?0Q8lw32l8w40l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12ls40l8w48l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e23_v16?0"UIAlertAction"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8ls40l8w48l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40r48w_e34_v24?0"NSDictionary"8"NSError"16lr40l8w48l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56w_e8_v12?0B8lw56l8r48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48r56w_e61_v32?0"NSArray"8"CTDisplayPlanList"16"CTDisplayPlanList"24lr48l8w56l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_literal_global.108
+ ___block_literal_global.112
+ ___block_literal_global.117
+ ___block_literal_global.124
+ ___block_literal_global.126
+ ___block_literal_global.140
+ ___block_literal_global.164
+ ___block_literal_global.229
+ ___block_literal_global.26
+ ___block_literal_global.300
+ ___block_literal_global.316
+ ___block_literal_global.480
+ ___block_literal_global.533
+ ___block_literal_global.536
+ ___block_literal_global.62
+ ___block_literal_global.636
+ ___block_literal_global.64
+ ___block_literal_global.70
+ ___block_literal_global.823
+ ___block_literal_global.853
+ ___block_literal_global.86
+ ___block_literal_global.913
+ ___block_literal_global.991
+ ___getIMOneTimeCodeTimeStampKeySymbolLoc_block_invoke
+ _getIMOneTimeCodeTimeStampKeySymbolLoc.ptr
+ _isTimeoutState
+ _objc_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_end_catch
+ _objc_msgSend$_addIconView
+ _objc_msgSend$_animateIcon
+ _objc_msgSend$_bodyTextWithPlain:boldSubstring:
+ _objc_msgSend$_buildDetailTextWithInfos:flowType:isDeleteESIM:selfSerialNumber:
+ _objc_msgSend$_buildPhoneNumberTableViewWithPrimary:secondary:
+ _objc_msgSend$_cancelTapped
+ _objc_msgSend$_capableAccounts
+ _objc_msgSend$_carrierNameForInfos:
+ _objc_msgSend$_completeFlow
+ _objc_msgSend$_consentViewControllerForAccount:
+ _objc_msgSend$_continueButtonTapped:
+ _objc_msgSend$_createActivatingSubflow
+ _objc_msgSend$_createQuickSwitchEnrollmentSubflow:
+ _objc_msgSend$_currentDeviceSerialNumber
+ _objc_msgSend$_deviceNameForInfo:selfSerialNumber:
+ _objc_msgSend$_evaluateNextStepFromSelf:
+ _objc_msgSend$_filterOnDeviceTransferredPlan:
+ _objc_msgSend$_firstViewControllerForLegacyFlow:
+ _objc_msgSend$_firstViewControllerWithUserIntentContext:
+ _objc_msgSend$_getCarrierSetupWithCompletion:
+ _objc_msgSend$_getQSAccountsWithMessageSession:
+ _objc_msgSend$_getQuickSwitchAccountsFromDisplayPlansWithCompletion:
+ _objc_msgSend$_getSubTextForSectionWithoutLazuli:
+ _objc_msgSend$_getTitleAndDetailText:selectedItems:isForCrossPlatformTransfer:
+ _objc_msgSend$_goToSettingsTapped
+ _objc_msgSend$_groupInfosByRoleAndDevice:selfSerialNumber:
+ _objc_msgSend$_handleActivatingExpiry
+ _objc_msgSend$_handleDismiss
+ _objc_msgSend$_handleEvaluateAccessControlResponse:
+ _objc_msgSend$_initiateSwapTransfer
+ _objc_msgSend$_isCarrierNameFallback:
+ _objc_msgSend$_isDeviceNameFallback:selfSerialNumber:
+ _objc_msgSend$_isPlanRegisteredForLazuli:
+ _objc_msgSend$_isQuickSwitch
+ _objc_msgSend$_isSingleOption
+ _objc_msgSend$_joinPhonesWithOr:
+ _objc_msgSend$_maybeCreateSIMConfigFlowAsPreFlow:options:
+ _objc_msgSend$_maybeShowQuickSwitchAlert
+ _objc_msgSend$_notifyQuickSwitchEnrollmentFailure:
+ _objc_msgSend$_numberKeyForPrimary:flowType:isDeleteESIM:plural:deviceIsFallback:
+ _objc_msgSend$_phoneNumberForInfo:
+ _objc_msgSend$_preambleForFlowType:
+ _objc_msgSend$_primaryDeviceNameExcluding:
+ _objc_msgSend$_requestTransferPlans:
+ _objc_msgSend$_saveSimsetupD2dInfo:shouldDeferView:
+ _objc_msgSend$_scanInfos:hasPrimary:hasSecondary:primaryDeviceName:primaryDeviceIsFallback:primaryPhoneNumber:secondaryPhoneNumbers:secondaryDeviceName:secondaryDeviceIsFallback:
+ _objc_msgSend$_sectionTypeForSection:
+ _objc_msgSend$_shareOptionSubtext
+ _objc_msgSend$_shouldShowConfirmAlertWithInfos:flowType:needsConfirmation:isDeleteESIM:
+ _objc_msgSend$_showButtonTraySpinnerWithBusyText:animating:
+ _objc_msgSend$_showLoadFailureAlert:error:
+ _objc_msgSend$_showTransferConfirmationAlert
+ _objc_msgSend$_startEnrollment
+ _objc_msgSend$_transferQuickSwitchAccount
+ _objc_msgSend$_transferQuickSwitchAccount:
+ _objc_msgSend$_updateAuthenticationStatus:
+ _objc_msgSend$_verifyAndShareTapped
+ _objc_msgSend$accountInfoFromDictionary:
+ _objc_msgSend$action
+ _objc_msgSend$allValues
+ _objc_msgSend$animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:
+ _objc_msgSend$appendAttributedString:
+ _objc_msgSend$appleAccountDsids
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$attributedStringWithAttachment:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$bootstrap:isPostMigrationFlow:isUsingPreSharedKey:completion:
+ _objc_msgSend$bootstrapQuickSwitchEnrollmentFlowAsSecondary:
+ _objc_msgSend$bootstrapQuickSwitchEnrollmentFlowAsSecondary:completion:
+ _objc_msgSend$bottomTray
+ _objc_msgSend$companionInfos
+ _objc_msgSend$concatenateDescriptors:
+ _objc_msgSend$configurationWithFont:
+ _objc_msgSend$configurationWithWeight:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:constant:
+ _objc_msgSend$contextFromDictionary:
+ _objc_msgSend$date
+ _objc_msgSend$deploymentType
+ _objc_msgSend$deviceIdentifier
+ _objc_msgSend$deviceInfoFromDictionary:
+ _objc_msgSend$didCompleteSecureIntent
+ _objc_msgSend$didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:completion:
+ _objc_msgSend$didSignUpQuickSwitchPlanCanceled:error:completion:
+ _objc_msgSend$didTransferPlanForCsn:iccid:srcIccid:profileServer:matchingId:state:
+ _objc_msgSend$didTransferPlanForEid:iccid:srcIccid:smdpURL:matchingId:state:
+ _objc_msgSend$didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:matchingId:state:
+ _objc_msgSend$displayName
+ _objc_msgSend$doDsidsMatch
+ _objc_msgSend$drawAtPoint:
+ _objc_msgSend$enrollQuickSwitch:secondaryDevice:flowType:session:completion:
+ _objc_msgSend$evaluateDtoPolicy:completion:
+ _objc_msgSend$evaluateNextStepFromViewController:completion:
+ _objc_msgSend$featureSupported
+ _objc_msgSend$filterQSAccountsWithoutTransferPlan:quickSwitchToTransferPlanMap:
+ _objc_msgSend$filterTransferPlansAlreadyInQuickSwitch:
+ _objc_msgSend$getAppleAccountDsids
+ _objc_msgSend$getMarketingModelName
+ _objc_msgSend$getNumberSharingInfoForAllSIMsWithCompletion:
+ _objc_msgSend$getNumberSharingInfoForSerialNumber:completion:
+ _objc_msgSend$getQuickSwitchAccountsForDisplayPlans:completion:
+ _objc_msgSend$getQuickSwitchErrorTitleDetail:forCarrier:
+ _objc_msgSend$getQuickSwitchPrimaryAccount:completion:
+ _objc_msgSend$getQuickSwitchSpecificDSIDsForThisDevice:
+ _objc_msgSend$getSystemConfiguration:withError:
+ _objc_msgSend$getTitleDetailAndSymbolForAccounts:selfAppleAccountDsids:quickSwitchToTransferPlanMap:
+ _objc_msgSend$groupHasOrphanPrimary:
+ _objc_msgSend$groupQSAccountsByNonSecondaryIccid:
+ _objc_msgSend$iconView
+ _objc_msgSend$imageWithActions:
+ _objc_msgSend$imageWithTintColor:renderingMode:
+ _objc_msgSend$initWithAccount:flowType:session:delegate:
+ _objc_msgSend$initWithAccount:secondary:flowType:
+ _objc_msgSend$initWithAccount:secondary:flowType:messageSession:
+ _objc_msgSend$initWithAccount:session:delegate:
+ _objc_msgSend$initWithAccounts:hasTransferPlans:blockerViewNeeded:showConfirmationAlert:messageSession:quickSwitchToTransferPlanMap:delegate:
+ _objc_msgSend$initWithAccounts:messageSession:quickSwitchToTransferPlanMap:isFirstView:delegate:
+ _objc_msgSend$initWithAccounts:selfAppleAccountDsids:quickSwitchToTransferPlanMap:isFirstView:delegate:
+ _objc_msgSend$initWithAppName:numberSuffix:
+ _objc_msgSend$initWithAppName:numberSuffix:phoneNumber:iccid:secondaryPhoneNumber:secondaryIccid:
+ _objc_msgSend$initWithAppName:phoneNumber:iccid:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithDisplayPlans:
+ _objc_msgSend$initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:quickSwitchFlowType:
+ _objc_msgSend$initWithExternalizedContext:descriptors:userIntentContext:
+ _objc_msgSend$initWithExternalizedContext:descriptors:userIntentContext:viewDelegate:
+ _objc_msgSend$initWithExternalizedContext:descriptors:userIntentContext:viewDelegate:quickSwitchFlowType:
+ _objc_msgSend$initWithGroupedAccounts:messageSession:quickSwitchToTransferPlanMap:isFirstView:delegate:
+ _objc_msgSend$initWithIccid:numberSuffix:phoneNumber:secondaryIccid:secondaryPhoneNumber:appName:
+ _objc_msgSend$initWithMessageSession:accounts:primarySerialNumber:carrierSetupItems:sourceOSVersion:sourceDeviceClass:isFirstView:quickSwitchToTransferPlanMap:quickSwitchFlowType:
+ _objc_msgSend$initWithNavigationController:account:messageSession:quickSwitchToTransferPlanMap:
+ _objc_msgSend$initWithNumberSharingInfos:flowType:isDeleteESIM:needsConfirmation:selfSerialNumber:
+ _objc_msgSend$initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:
+ _objc_msgSend$initWithPhoneNumber:
+ _objc_msgSend$initWithPhoneNumber:result:
+ _objc_msgSend$initWithPlanInfos:isQuickSwitchSlidingOngoing:
+ _objc_msgSend$initWithPlans:selectedItems:skip:isForCrossPlatformTransfer:quickSwitchFlowType:
+ _objc_msgSend$initWithPrimaryAccount:delegate:
+ _objc_msgSend$initWithQSLifeCycleChangeFlowType:isDeleteESIM:deviceIdentifier:needsConfirmation:
+ _objc_msgSend$initWithQuickSwitchAccount:isSwap:iccid:quickSwitchFlowType:
+ _objc_msgSend$initWithQuickSwitchPlan:
+ _objc_msgSend$initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:
+ _objc_msgSend$initWithSize:format:
+ _objc_msgSend$isD2dDeferView
+ _objc_msgSend$isDTOEvaluationRequired:completion:
+ _objc_msgSend$isDeleteESIM
+ _objc_msgSend$isESIMUnavailable
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isEnrolled
+ _objc_msgSend$isOtherOptionsTapped
+ _objc_msgSend$isQSAccountCapable:
+ _objc_msgSend$isQuickSwitchCellTapped
+ _objc_msgSend$isQuickSwitchSupported
+ _objc_msgSend$isQuickSwitchSwap
+ _objc_msgSend$isSecondaryTwinnedNoTransferWithoutCompanion:inAccounts:quickSwitchToTransferPlanMap:
+ _objc_msgSend$isSecureIntentRequired:completion:
+ _objc_msgSend$lifeCycleChangeFlowType
+ _objc_msgSend$lifecycleState
+ _objc_msgSend$lowDataMode:error:
+ _objc_msgSend$matchTransferPlans:toQSAccounts:
+ _objc_msgSend$needsConfirmation
+ _objc_msgSend$notifyQuickSwitchEnrollmentResult:
+ _objc_msgSend$operationStatus
+ _objc_msgSend$otpDetectionStartTime
+ _objc_msgSend$pairedDeviceName
+ _objc_msgSend$pairedDeviceSerialNumber
+ _objc_msgSend$preferredFontDescriptorWithTextStyle:
+ _objc_msgSend$preferredFormat
+ _objc_msgSend$primarySerialNumber
+ _objc_msgSend$qsLifecycleState
+ _objc_msgSend$qsRole
+ _objc_msgSend$quickSwitchAccount
+ _objc_msgSend$quickSwitchFlowType
+ _objc_msgSend$quickSwitchPlans
+ _objc_msgSend$reason
+ _objc_msgSend$registrationState
+ _objc_msgSend$releaseBootstrapService:
+ _objc_msgSend$reloadRowsAtIndexPaths:withRowAnimation:
+ _objc_msgSend$requestBootstrapService:completion:
+ _objc_msgSend$resolveIncompleteWebsheetWithFollowup:
+ _objc_msgSend$resolveQuickSwitchWebsheetIncomplete:followup:completion:
+ _objc_msgSend$role
+ _objc_msgSend$secondarySystemGroupedBackgroundColor
+ _objc_msgSend$selectedAccount
+ _objc_msgSend$selectedAccounts
+ _objc_msgSend$selectedNewLine
+ _objc_msgSend$selectedOption
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setAccounts:
+ _objc_msgSend$setContentMode:
+ _objc_msgSend$setDecisionDelegate:
+ _objc_msgSend$setExclusionPaths:
+ _objc_msgSend$setIsQuickSwitchSwap:
+ _objc_msgSend$setIsSlidingWebsheetIncomplete:
+ _objc_msgSend$setPreferredContentSize:
+ _objc_msgSend$setPrimaryAccount:
+ _objc_msgSend$setQuickSwitchAccount:
+ _objc_msgSend$setQuickSwitchFlowType:
+ _objc_msgSend$setQuickSwitchPlans:
+ _objc_msgSend$setScale:
+ _objc_msgSend$setSupportsDynamicSIMConfigurationCache:
+ _objc_msgSend$setTextToSecondaryTextVerticalPadding:
+ _objc_msgSend$setTimeoutIntervalForResource:
+ _objc_msgSend$setTransferPlans:
+ _objc_msgSend$setWaitsForConnectivity:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$shouldOfferQSAccount:serialNumber:
+ _objc_msgSend$shouldOfferQSAccountFromDisplayPlan:serialNumber:
+ _objc_msgSend$shouldShowDevicePicker:
+ _objc_msgSend$shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferPlans:completion:
+ _objc_msgSend$staticFeatureProperties
+ _objc_msgSend$subtitleCellConfiguration
+ _objc_msgSend$supportsDynamicSIMConfigurationCache
+ _objc_msgSend$supportsDynamicSIMConfigurationWithError:
+ _objc_msgSend$supportsNoChargeForOnboarding
+ _objc_msgSend$switchState
+ _objc_msgSend$symbolicTraits
+ _objc_msgSend$systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:
+ _objc_msgSend$tertiaryLabelColor
+ _objc_msgSend$textContainer
+ _objc_msgSend$titleTextView
+ _objc_msgSend$transferFlowTypeForAccount:quickSwitchToTransferPlanMap:
+ _objc_msgSend$transferQuickSwitch:targetDevice:flowType:session:completion:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$updateQuickSwitchConsentResult:iccid:
+ _objc_msgSend$updateQuickSwitchConsentResult:iccid:error:
+ _objc_msgSend$updateSecureIntentResult:data:error:completion:
+ _objc_msgSend$userDidConfirm
+ _objc_msgSend$userIntentContext
+ _objc_msgSend$userProvideEnrollmentConsent:consent:completion:
+ _objc_msgSend$viewWithTag:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x9
- +[TSFlowHelper getAccountMemberTransferablePlanWithSameCarrierName:transferablePlans:]
- +[TSFlowHelper hasTransferablePlanWithSameCarrierName:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:]
- +[TSFlowHelper sortIndexesInDescending:]
- +[TSUtilities displayPlanFromObject:]
- +[TSUtilities getStoreVisitStatusForPlan:cache:]
- +[TSUtilities getStoreVisitStatusForPlan:cache:].cold.1
- +[TSUtilities odaPlans:]
- -[TSActivationFlowWithSimSetupFlow didPurchasePlanSuccessfullyWithEid:imei:meid:iccid:alternateSDMP:state:]
- -[TSActivationFlowWithSimSetupFlow didPurchasePlanSuccessfullyWithEid:imei:meid:iccid:alternateSDMP:state:].cold.1
- -[TSActivationFlowWithSimSetupFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:state:]
- -[TSActivationFlowWithSimSetupFlow setTransferIneligibleViaCloudItems:]
- -[TSActivationFlowWithSimSetupFlow setTransferItems:]
- -[TSActivationFlowWithSimSetupFlow transferIneligibleViaCloudItems]
- -[TSActivationFlowWithSimSetupFlow transferItems]
- -[TSCellularPlanManagerCache didTransferPlanForEid:iccid:srcIccid:smdpURL:state:]
- -[TSCellularSetupCompleteViewController initWithPlans:selectedItems:skip:isForCrossPlatformTransfer:]
- -[TSCellularSetupLoadingView secondLabel]
- -[TSCellularSetupLoadingView setSecondLabel:]
- -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:]
- -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:].cold.1
- -[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:].cold.2
- -[TSProximitySourceTransferFlow firstViewController:].cold.1
- -[TSRemotePlanSignUpFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:state:]
- -[TSSIMSetupFlow showLoadFailureAlert:error:]
- -[TSTransferCloudFlowModel filterTransferPlans:].cold.3
- -[TSTransferCloudFlowModel requireStoreVisitItems]
- -[TSTransferCloudFlowModel setRequireStoreVisitItems:]
- -[TSTransferCloudFlowModel setTransferIneligibleItems:]
- -[TSTransferCloudFlowModel setTransferItems:]
- -[TSTransferCloudFlowModel setTransferableHiddenInCloudFlowItems:]
- -[TSTransferCloudFlowModel transferIneligibleItems]
- -[TSTransferCloudFlowModel transferItems]
- -[TSTransferCloudFlowModel transferableHiddenInCloudFlowItems]
- -[TSTransferFlow _saveSimsetupD2dInfo:]
- -[TSTransferFlowModel bootstrap:isUsingPreSharedKey:completion:]
- -[TSTransferFlowModel filterTransferPlans:].cold.2
- -[TSTransferFlowModel requireStoreVisitItems]
- -[TSTransferFlowModel setRequireStoreVisitItems:]
- -[TSTransferFlowModel setTransferIneligibleItems:]
- -[TSTransferFlowModel setTransferItems:]
- -[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:]
- -[TSTransferFlowModel transferIneligibleItems]
- -[TSTransferFlowModel transferItems]
- -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:allowsMultiSelection:]
- -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:]
- -[TSTransferListViewController initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:allowsMultiSelection:]
- -[TSWebsheetSignupFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:state:]
- -[TSWebsheetViewController _webView:accessoryViewCustomButtonTappedInFormInputSession:]
- -[TSWebsheetViewController _webView:insertTextSuggestion:inInputSession:]
- -[TSWebsheetViewController _webView:willStartInputSession:]
- -[TSWebsheetViewController _webView:willSubmitFormValues:userObject:submissionHandler:]
- -[TSWebsheetViewController formAutoFillControllerCanPrefillForm:]
- -[TSWebsheetViewController formAutoFillControllerShouldDisableAutoFill:]
- -[TSWebsheetViewController formAutoFillControllerURLForFormAutoFill:]
- GCC_except_table122
- GCC_except_table124
- GCC_except_table128
- GCC_except_table141
- GCC_except_table153
- GCC_except_table187
- GCC_except_table190
- GCC_except_table198
- GCC_except_table227
- GCC_except_table24
- GCC_except_table43
- GCC_except_table48
- GCC_except_table60
- GCC_except_table62
- GCC_except_table81
- GCC_except_table94
- GCC_except_table96
- GCC_except_table97
- _OBJC_CLASS_$__SFFormAutoFillController
- _OBJC_CLASS_$__SFWebView
- _OBJC_CLASS_$__WKProcessPoolConfiguration
- _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._transferIneligibleViaCloudItems
- _OBJC_IVAR_$_TSActivationFlowWithSimSetupFlow._transferItems
- _OBJC_IVAR_$_TSCellularSetupLoadingView._secondLabel
- _OBJC_IVAR_$_TSTransferCloudFlowModel._requireStoreVisitItems
- _OBJC_IVAR_$_TSTransferCloudFlowModel._transferIneligibleItems
- _OBJC_IVAR_$_TSTransferCloudFlowModel._transferItems
- _OBJC_IVAR_$_TSTransferCloudFlowModel._transferableHiddenInCloudFlowItems
- _OBJC_IVAR_$_TSTransferFlow._transferItems
- _OBJC_IVAR_$_TSTransferFlowModel._requireStoreVisitItems
- _OBJC_IVAR_$_TSTransferFlowModel._transferIneligibleItems
- _OBJC_IVAR_$_TSTransferFlowModel._transferItems
- _OBJC_IVAR_$_TSWebsheetViewController._autoFillController
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __OBJC_$_INSTANCE_METHODS_TSCellularPlanActivatingFlow(Override|TSCellularPlanManagerCacheDelegate|CoreTelephonyClientCellularPlanManagementDelegate|TSSIMSetupDelegate|TSSIMSetupFlowDelegate|Single|Consolidated|UpdatePlanInfo|InteractiveUI)
- __OBJC_$_PROP_LIST_SFFormAutoFillControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFFormAutoFillControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFFormAutoFillControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SFFormAutoFillControllerDelegate
- __OBJC_$_PROTOCOL_REFS_SFFormAutoFillControllerDelegate
- __OBJC_CLASS_PROTOCOLS_$_TSCellularPlanActivatingFlow(Override|TSCellularPlanManagerCacheDelegate|CoreTelephonyClientCellularPlanManagementDelegate|TSSIMSetupDelegate|TSSIMSetupFlowDelegate|Single|Consolidated|UpdatePlanInfo|InteractiveUI)
- __OBJC_LABEL_PROTOCOL_$_SFFormAutoFillControllerDelegate
- __OBJC_PROTOCOL_$_SFFormAutoFillControllerDelegate
- ___106-[TSRemotePlanSignUpFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:state:]_block_invoke
- ___108-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:]_block_invoke
- ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.503
- ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke.51
- ___142-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke_6
- ___34-[TSAuthFlow firstViewController:]_block_invoke
- ___39-[TSTransferFlow _firstViewController:]_block_invoke.218
- ___40+[TSFlowHelper sortIndexesInDescending:]_block_invoke
- ___44-[TSTransferFlowModel requestCarrierSetups:]_block_invoke.46
- ___45-[TSSIMSetupFlow showLoadFailureAlert:error:]_block_invoke
- ___45-[TSSIMSetupFlow showLoadFailureAlert:error:]_block_invoke_2
- ___49-[TSTransferCloudFlowModel requestCarrierSetups:]_block_invoke.44
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.38
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.38.cold.1
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.38.cold.2
- ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke.81
- ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke.112
- ___53-[TSProximitySourceTransferFlow firstViewController:]_block_invoke.112.cold.1
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.231
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.233
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.232
- ___53-[TSTravelBuddyViewController _continueButtonTapped:]_block_invoke.116
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.35
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.35.cold.1
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.36
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.36.cold.1
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.37
- ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.40
- ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.40.cold.1
- ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.41
- ___57-[TSSinglePlanTransferViewController _startPlanTransfer:]_block_invoke_4
- ___57-[TSSinglePlanTransferViewController _startPlanTransfer:]_block_invoke_5
- ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke.80
- ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.71
- ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.71.cold.1
- ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.172
- ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.177
- ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.180
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.104
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.104.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.105
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.105.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.106
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.106.cold.1
- ___64-[TSPRXSIMTransferringViewController _setupOneTimeCodeDetection]_block_invoke.65
- ___70-[TSCellularSetupLoadingViewController safariViewControllerDidFinish:]_block_invoke.91
- ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.114
- ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.549
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.108
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.108.cold.1
- ___79-[TSCellularSetupLoadingViewController setupCoreTelephonyClientForRemoteSignup]_block_invoke.58
- ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.611
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.560
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.560.cold.1
- ___block_descriptor_32_e11_q24?0816l
- ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_48_e8_32r40w_e34_v24?0"NSDictionary"8"NSError"16lr32l8w40l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_v16?0Q8ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e8_v12?0B8lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64w_e8_v12?0B8lw64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56r64w_e61_v32?0"NSArray"8"CTDisplayPlanList"16"CTDisplayPlanList"24lr56l8s32l8w64l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.104
- ___block_literal_global.120
- ___block_literal_global.170
- ___block_literal_global.235
- ___block_literal_global.306
- ___block_literal_global.322
- ___block_literal_global.410
- ___block_literal_global.502
- ___block_literal_global.505
- ___block_literal_global.55
- ___block_literal_global.562
- ___block_literal_global.58
- ___block_literal_global.687
- ___block_literal_global.716
- ___block_literal_global.776
- ___block_literal_global.84
- _objc_msgSend$URLByAppendingPathComponent:
- _objc_msgSend$_saveSimsetupD2dInfo:
- _objc_msgSend$autoFill
- _objc_msgSend$bootstrap:isUsingPreSharedKey:completion:
- _objc_msgSend$builtInPlugInsURL
- _objc_msgSend$constraintLessThanOrEqualToAnchor:multiplier:
- _objc_msgSend$constraintLessThanOrEqualToAnchor:multiplier:constant:
- _objc_msgSend$didTransferPlanForCsn:iccid:srcIccid:profileServer:state:
- _objc_msgSend$didTransferPlanForEid:iccid:srcIccid:smdpURL:state:
- _objc_msgSend$didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:state:
- _objc_msgSend$displayPlanFromObject:
- _objc_msgSend$fieldFocusedWithInputSession:
- _objc_msgSend$getAccountMemberTransferablePlanWithSameCarrierName:transferablePlans:
- _objc_msgSend$getStoreVisitStatusForCarrier:
- _objc_msgSend$getStoreVisitStatusForPlan:cache:
- _objc_msgSend$hasTransferablePlanWithSameCarrierName:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:
- _objc_msgSend$initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:
- _objc_msgSend$initWithPlans:selectedItems:skip:isForCrossPlatformTransfer:
- _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:allowsMultiSelection:
- _objc_msgSend$initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:
- _objc_msgSend$initWithWebView:delegate:
- _objc_msgSend$insertTextSuggestion:
- _objc_msgSend$odaPlans:
- _objc_msgSend$prefillFormsSoonIfNeeded
- _objc_msgSend$requireStoreVisitItems
- _objc_msgSend$secondLabel
- _objc_msgSend$setInjectedBundleURL:
- _objc_msgSend$setSecondLabel:
- _objc_msgSend$shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:
- _objc_msgSend$showLoadFailureAlert:error:
- _objc_msgSend$sortIndexesInDescending:
- _objc_msgSend$sortUsingComparator:
- _objc_msgSend$transferIneligibleItems
- _objc_msgSend$transferIneligibleViaCloudItems
- _objc_msgSend$transferItems
- _objc_msgSend$transferPlanWithIdentifier:fromDevice:completionHandler:
- _objc_msgSend$transferableHiddenInCloudFlowItems
- _objc_msgSend$willSubmitFormValues:userObject:submissionHandler:
- _objc_release_x10
CStrings:
+ "\n"
+ "\n\n%@"
+ "  "
+ " %@ "
+ "%"
+ "%ld_%@"
+ "%lu transfer plans @%s"
+ "("
+ "(no transfer plan)"
+ ")"
+ "+[TSUtilities groupQSAccountsByNonSecondaryIccid:]"
+ ", "
+ "-[OBWelcomeController(Spinner) _prepareSpinner]"
+ "-[OBWelcomeController(Spinner) _showButtonTraySpinnerWithBusyText:animating:]"
+ "-[SSPRXQuickSwitchPrimaryCompleteViewController _completeFlow]"
+ "-[SSPRXQuickSwitchPrimaryEnrollConsentViewController _startEnrollment]_block_invoke"
+ "-[SSQuickSwitchAlertViewController _transferQuickSwitchAccount]_block_invoke"
+ "-[SSQuickSwitchAlertViewController prepare:]_block_invoke"
+ "-[SSQuickSwitchDevicePickerViewController _continueButtonTapped:]"
+ "-[SSQuickSwitchDevicePickerViewController _showTransferConfirmationAlert]_block_invoke"
+ "-[SSQuickSwitchDevicePickerViewController initWithAccounts:messageSession:quickSwitchToTransferPlanMap:isFirstView:delegate:]"
+ "-[SSQuickSwitchDevicePickerViewController tableView:didSelectRowAtIndexPath:]"
+ "-[SSQuickSwitchEnrollmentConsentViewController _continueButtonTapped]"
+ "-[SSQuickSwitchEnrollmentConsentViewController _continueButtonTapped]_block_invoke"
+ "-[SSQuickSwitchLifeCycleChangeFlow firstViewController:]"
+ "-[SSQuickSwitchLifeCycleChangeFlow firstViewController:]_block_invoke"
+ "-[SSQuickSwitchLifeCycleChangeFlow firstViewController]"
+ "-[SSQuickSwitchListViewController _continueButtonTapped:]"
+ "-[SSQuickSwitchListViewController _showTransferConfirmationAlert]_block_invoke"
+ "-[SSQuickSwitchListViewController tableView:didSelectRowAtIndexPath:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow _notifyQuickSwitchEnrollmentFailure:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow _notifyQuickSwitchEnrollmentFailure:]_block_invoke"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow _proxCardFlowDidDismiss]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow _startBackgroundTask]_block_invoke"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow didCompleteSecureIntent]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow didRequestPresentationForProxCard:]_block_invoke"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow evaluateNextStepFromViewController:completion:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow evaluateNextStepFromViewController:completion:]_block_invoke_2"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow firstViewController:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow firstViewController]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow initWithAccount:secondary:flowType:messageSession:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:]_block_invoke"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow launchQuickSwitchEnrollmentWebsheet:completion:]_block_invoke_2"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:completion:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:completion:]_block_invoke"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:isQuickSwitchFlow:completion:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:isQuickSwitchFlow:completion:]_block_invoke"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:isQuickSwitchFlow:completion:]_block_invoke_2"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow notifyQuickSwitchEnrollmentResult:]_block_invoke"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow notifyQuickSwitchEnrollmentResult:]_block_invoke_2"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow simSetupFlowCompleted:]_block_invoke"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow updateQuickSwitchEnrollmentStatus:]"
+ "-[SSQuickSwitchPrimaryEnrollmentFlow viewControllerDidComplete:]"
+ "-[SSQuickSwitchPublicAPIConsentViewController prepare:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _createQuickSwitchEnrollmentSubflow:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _filterOnDeviceTransferredPlan:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _firstViewController]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _getCarrierSetupWithCompletion:]_block_invoke"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _getQSAccountsWithMessageSession:]_block_invoke"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _getQSAccountsWithMessageSession:]_block_invoke_2"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke_2"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _maybePresentFirstViewController:firstViewControllerCallback:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _maybePresentFirstViewController:firstViewControllerCallback:]_block_invoke"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _requestPlansWithCompletion:]_block_invoke"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow _requestTransferPlans:]_block_invoke"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow firstViewController:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow firstViewController:]_block_invoke"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow firstViewController]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow notifyQuickSwitchEnrollmentResult:]"
+ "-[SSQuickSwitchSecondaryEnrollmentFlow updateQuickSwitchEnrollmentStatus:]"
+ "-[SSQuickSwitchSecondarySharingViewController _continueButtonTapped:]"
+ "-[SSQuickSwitchSecondarySharingViewController _showTransferConfirmationAlert]_block_invoke"
+ "-[SSQuickSwitchSecondarySharingViewController _transferQuickSwitchAccount:]_block_invoke"
+ "-[SSQuickSwitchSecondarySharingViewController tableView:didSelectRowAtIndexPath:]"
+ "-[SSQuickSwitchSlidingChoiceViewController _continueButtonTapped:]"
+ "-[SSQuickSwitchSlidingChoiceViewController _continueButtonTapped:]_block_invoke"
+ "-[SSQuickSwitchSlidingChoiceViewController tableView:didSelectRowAtIndexPath:]"
+ "-[SSQuickSwitchSwapConsentViewController _initiateSwapTransfer]_block_invoke"
+ "-[SSQuickSwitchSwapFlow _createActivatingSubflow]"
+ "-[SSQuickSwitchSwapFlow firstViewController:]"
+ "-[SSQuickSwitchSwapFlow firstViewController:]_block_invoke"
+ "-[SSQuickSwitchSwapFlow firstViewController]"
+ "-[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]"
+ "-[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke"
+ "-[TSActivationFlowWithSimSetupFlow _getQuickSwitchAccountsFromDisplayPlansWithCompletion:]_block_invoke_2"
+ "-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke_2"
+ "-[TSActivationFlowWithSimSetupFlow didPurchasePlanSuccessfullyWithEid:imei:meid:iccid:alternateSDMP:matchingId:state:]"
+ "-[TSAuthFlow evaluateNextStepFromViewController:completion:]"
+ "-[TSAuthFlow evaluateNextStepFromViewController:completion:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow initWithQuickSwitchAccount:isSwap:iccid:quickSwitchFlowType:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) launchQuickSwitchSetup:completion:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) launchQuickSwitchSetup:completion:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) notifyQuickSwitchEnrollmentResult:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) updateQuickSwitchEnrollmentStatus:]"
+ "-[TSCellularPlanActivatingFlow(SSQuickSwitchIncompleteWebsheetDecision) resolveIncompleteWebsheetWithFollowup:]"
+ "-[TSCellularPlanActivatingFlow(SSQuickSwitchIncompleteWebsheetDecision) resolveIncompleteWebsheetWithFollowup:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(SecureIntent) evaluateNextStepFromViewController:completion:]"
+ "-[TSCellularPlanActivatingFlow(SecureIntent) evaluateNextStepFromViewController:completion:]_block_invoke_2"
+ "-[TSCellularPlanActivatingFlow(SecureIntent) proxCardFlowDidDismiss]"
+ "-[TSCellularSetupActivatingViewController _maybeShowQuickSwitchAlert]"
+ "-[TSCellularSetupCompleteViewController _getTitleAndDetailText:selectedItems:isForCrossPlatformTransfer:]"
+ "-[TSCoreTelephonyClientCache getAppleAccountDsids]"
+ "-[TSCoreTelephonyClientCache supportsDynamicSIMConfiguration]"
+ "-[TSCoreTelephonyClientCache updateQuickSwitchConsentResult:iccid:]"
+ "-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke_2"
+ "-[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:quickSwitchPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:]"
+ "-[TSPostMigrationFlow firstViewController:]"
+ "-[TSProximitySourceTransferFlow firstViewController:]_block_invoke_2"
+ "-[TSRemotePlanSignUpFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:matchingId:state:]_block_invoke"
+ "-[TSSecureIntentGestureViewController _evaluateNextStepFromSelf:]"
+ "-[TSSecureIntentGestureViewController _updateAuthenticationStatus:]_block_invoke_2"
+ "-[TSSecureIntentGestureViewController initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:quickSwitchFlowType:]"
+ "-[TSSecureIntentGestureViewController prepare:]_block_invoke"
+ "-[TSTransferFlow _saveSimsetupD2dInfo:shouldDeferView:]"
+ "-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:]_block_invoke"
+ "-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferPlans:completion:]"
+ "-[TSTravelBuddyViewController _isPlanRegisteredForLazuli:]"
+ "-[TSUserInPurchaseFlowAssertion assertUserInPurchaseFlowStartOver:caller:]_block_invoke"
+ "-[TSWebsheetSignupFlow initWithRequestType:websheetURL:postdata:useCase:pirmaryIccid:]"
+ "1R"
+ "27.0"
+ "???"
+ "AUTOMATIC_NUMBER_SWITCHING"
+ "Activating"
+ "ActivationCode"
+ "ActivationPolicyMismatch"
+ "After filtering accounts without transfer plans: %lu @%s"
+ "After filtering enrolled transfer plans: %lu @%s"
+ "B24@?0@\"CTDisplayPlan\"8@\"NSDictionary\"16"
+ "B24@?0@\"CTQuickSwitchAccountInfo\"8@\"NSDictionary\"16"
+ "CTPlanTransferStatusTimeoutAfterQSTransferDone"
+ "Carrier setup: %@ @%s"
+ "CarrierSetupItems"
+ "CarrierSignup"
+ "Continue tapped but no group selected @%s"
+ "CoreTelephony"
+ "Creating QuickSwitch enrollment subflow for phone number: %@ @%s"
+ "Creating activating subflow for QuickSwitch swap @%s"
+ "Creating websheet flow with URL: %@, requestType: %lu, primaryIccid: %@ @%s"
+ "CrossPlatformAuth"
+ "CrossPlatformTransfer"
+ "Deferring D2D view @%s"
+ "Device had a ODA tether during buddy @%s"
+ "Device has a pending SODA tether @%s"
+ "DeviceIdentifierKey"
+ "DeviceInfo"
+ "Enrollment result %ld received on WebsheetIncompleteVC, completing flow @%s"
+ "Enrollment result %ld received while on SharingVC, dismissing websheet @%s"
+ "Enrollment result %ld received while topVC is %@, no-op @%s"
+ "Enrollment result received on SettingUpVC, progressing to CompleteVC with result: %ld @%s"
+ "FALLBACK_CARRIER_NAME"
+ "FALLBACK_DEVICE_NAME"
+ "FALLBACK_PHONE_NUMBER"
+ "Fetched dsids: %@, error: %@ @%s"
+ "FindMyWipe: no Secondary SIMs on this device for serial %@ @%s"
+ "FindMyWipe: no number sharing infos for serial %@ @%s"
+ "Followup"
+ "Found %lu quickswitch plans @%s"
+ "Getting quickswitch plans from display plans @%s"
+ "IDSTransfer"
+ "IMOneTimeCodeTimeStampKey"
+ "IdentityShare"
+ "Ignoring old OTP code: %@ (timestamp: %@) @%s"
+ "Installing a GMVNO SIM while traveling @%s"
+ "IsDeleteESIMKey"
+ "IsSecondaryKey"
+ "IsSwapKey"
+ "LDM is enabled already for %@ @%s"
+ "ManageAccount"
+ "ManagedDeviceInstall"
+ "NeedsConfirmationKey"
+ "No EACS accounts found, ending flow @%s"
+ "No decoded data @%s"
+ "No twinned SIMs found, ending flow @%s"
+ "Nothing found @%s"
+ "ON_%@"
+ "Offering %lu quickswitch plans @%s"
+ "Offering %lu quickswitch plans from display plans @%s"
+ "On bootstrap @%s"
+ "OnDeviceConversion"
+ "PASSCODE"
+ "PIN"
+ "PhoneNumberCell"
+ "PostMigrationTransfer"
+ "ProximityTransfer"
+ "PublicInstall"
+ "QS acct:%@ @%s"
+ "QS already attempted in buddy, skipping @%s"
+ "QS enrollment timeout after transfer done, update %@ status to TimeoutAfterQSTransferDone @%s"
+ "QS sliding timeout, update %@ status to Failed @%s"
+ "QSLifeCycleChangeFlowTypeKey"
+ "QS_ACTIVATING_DETAILS"
+ "QS_ACTIVATING_TITLE"
+ "QS_BLOCKER_AA_MISMATCH_DETAIL_OTHER_BUDDY_%@"
+ "QS_BLOCKER_AA_MISMATCH_DETAIL_OTHER_POSTBUDDY_%@"
+ "QS_BLOCKER_AA_MISMATCH_DETAIL_SELF_BUDDY"
+ "QS_BLOCKER_AA_MISMATCH_DETAIL_SELF_POSTBUDDY"
+ "QS_BLOCKER_AA_MISMATCH_TITLE_OTHER"
+ "QS_BLOCKER_AA_MISMATCH_TITLE_SELF"
+ "QS_BLOCKER_SECONDARY_TWINNED_NO_TRANSFER_%@"
+ "QS_BLOCKER_SOFTWARE_UPDATE_DETAIL"
+ "QS_BLOCKER_SOFTWARE_UPDATE_TITLE"
+ "QS_COMPANION_DEVICE_NEEDED_%@"
+ "QS_CONFIRM_TRANSFER_ALERT_%@_%@"
+ "QS_CONSENT_BODY_MULTI"
+ "QS_CONSENT_BODY_NO_MATCH"
+ "QS_CONSENT_BODY_SINGLE"
+ "QS_CONSENT_CLOSE"
+ "QS_CONSENT_PRIVACY_NOTE"
+ "QS_CONSENT_TITLE"
+ "QS_CONSENT_VERIFY_SHARE"
+ "QS_DEVICE_PICKER_DETAILS"
+ "QS_DEVICE_PICKER_KEEP_NEARBY_%@"
+ "QS_DEVICE_PICKER_REPLACE_%@"
+ "QS_DEVICE_PICKER_SET_UP_NEW_LINE"
+ "QS_EACS_CARRIER_NOTICE"
+ "QS_EACS_CARRIER_NOTICE_%@"
+ "QS_EACS_CONFIRM_BUTTON_DELETE_ESIM"
+ "QS_EACS_CONFIRM_BUTTON_ERASE"
+ "QS_EACS_CONFIRM_BUTTON_SIGNOUT"
+ "QS_EACS_CONFIRM_TITLE_DELETE_ESIM"
+ "QS_EACS_CONFIRM_TITLE_ERASE"
+ "QS_EACS_CONFIRM_TITLE_SIGNOUT"
+ "QS_EACS_PRIMARY_DELETE_ESIM_CONFIRM_%@"
+ "QS_EACS_PRIMARY_DELETE_ESIM_CONFIRM_%@_%@"
+ "QS_EACS_PRIMARY_DELETE_ESIM_CONFIRM_FALLBACK_DEVICE"
+ "QS_EACS_PRIMARY_DELETE_ESIM_CONFIRM_FALLBACK_DEVICE_%@"
+ "QS_EACS_PRIMARY_DELETE_ESIM_NUMBERS_%@_%@"
+ "QS_EACS_PRIMARY_DELETE_ESIM_NUMBERS_FALLBACK_DEVICE_%@"
+ "QS_EACS_PRIMARY_DELETE_ESIM_NUMBER_%@_%@"
+ "QS_EACS_PRIMARY_DELETE_ESIM_NUMBER_FALLBACK_DEVICE_%@"
+ "QS_EACS_PRIMARY_KEEP_ESIM_ADVICE_%@_%@"
+ "QS_EACS_PRIMARY_KEEP_ESIM_ADVICE_FALLBACK_DEVICE"
+ "QS_EACS_PRIMARY_KEEP_ESIM_CONFIRM_%@"
+ "QS_EACS_PRIMARY_KEEP_ESIM_CONFIRM_FALLBACK_DEVICE"
+ "QS_EACS_PRIMARY_KEEP_ESIM_NUMBERS_%@_%@"
+ "QS_EACS_PRIMARY_KEEP_ESIM_NUMBERS_FALLBACK_DEVICE_%@"
+ "QS_EACS_PRIMARY_KEEP_ESIM_NUMBER_%@_%@"
+ "QS_EACS_PRIMARY_KEEP_ESIM_NUMBER_FALLBACK_DEVICE_%@"
+ "QS_EACS_PRIMARY_SIGNOUT_CONFIRM_%@_%@"
+ "QS_EACS_PRIMARY_SIGNOUT_CONFIRM_FALLBACK_DEVICE_%@"
+ "QS_EACS_PRIMARY_SIGNOUT_NUMBERS_%@_%@"
+ "QS_EACS_PRIMARY_SIGNOUT_NUMBERS_FALLBACK_DEVICE_%@"
+ "QS_EACS_PRIMARY_SIGNOUT_NUMBER_%@_%@"
+ "QS_EACS_PRIMARY_SIGNOUT_NUMBER_FALLBACK_DEVICE_%@"
+ "QS_EACS_SECONDARY_DELETE_ESIM_NUMBERS_%@_%@"
+ "QS_EACS_SECONDARY_DELETE_ESIM_NUMBERS_FALLBACK_DEVICE_%@"
+ "QS_EACS_SECONDARY_DELETE_ESIM_NUMBER_%@_%@"
+ "QS_EACS_SECONDARY_DELETE_ESIM_NUMBER_FALLBACK_DEVICE_%@"
+ "QS_EACS_SECONDARY_KEEP_ESIM_ADVICE"
+ "QS_EACS_SECONDARY_KEEP_ESIM_ADVICE_NUMBERS_%@"
+ "QS_EACS_SECONDARY_KEEP_ESIM_NUMBERS_%@_%@"
+ "QS_EACS_SECONDARY_KEEP_ESIM_NUMBERS_FALLBACK_DEVICE_%@"
+ "QS_EACS_SECONDARY_KEEP_ESIM_NUMBER_%@_%@"
+ "QS_EACS_SECONDARY_KEEP_ESIM_NUMBER_FALLBACK_DEVICE_%@"
+ "QS_EACS_SECONDARY_SIGNOUT_CONFIRM"
+ "QS_EACS_SECONDARY_SIGNOUT_NUMBERS_%@_%@"
+ "QS_EACS_SECONDARY_SIGNOUT_NUMBERS_FALLBACK_DEVICE_%@"
+ "QS_EACS_SECONDARY_SIGNOUT_NUMBER_%@_%@"
+ "QS_EACS_SECONDARY_SIGNOUT_NUMBER_FALLBACK_DEVICE_%@"
+ "QS_ENROLL_CONSENT_CHARGE_DETAILS"
+ "QS_ENROLL_CONSENT_CHARGE_TITLE"
+ "QS_ENROLL_CONSENT_DETAILS"
+ "QS_ENROLL_CONSENT_LOCATION_DETAILS"
+ "QS_ENROLL_CONSENT_LOCATION_TITLE"
+ "QS_ENROLL_CONSENT_PRIMARY_ESIM_DETAILS_SLIDING"
+ "QS_FINDMY_WIPE_CONFIRM_BUTTON"
+ "QS_FINDMY_WIPE_CONFIRM_NUMBERS_%@"
+ "QS_FINDMY_WIPE_CONFIRM_NUMBER_%@"
+ "QS_FINDMY_WIPE_NUMBERS_%@_%@"
+ "QS_FINDMY_WIPE_NUMBER_%@_%@"
+ "QS_FINDMY_WIPE_PREAMBLE"
+ "QS_FLOW_TYPE_CHOICE_DETAILS"
+ "QS_FLOW_TYPE_CHOICE_OPTION_ENROLL_ONLY"
+ "QS_FLOW_TYPE_CHOICE_OPTION_ENROLL_ONLY_SUBTITLE_%@"
+ "QS_FLOW_TYPE_CHOICE_OPTION_SLIDING"
+ "QS_FLOW_TYPE_CHOICE_OPTION_SLIDING_SUBTITLE"
+ "QS_FLOW_TYPE_CHOICE_TITLE"
+ "QS_FOLLOWUP_OTHER_PHONE_DETAIL"
+ "QS_FOLLOWUP_OTHER_PHONE_DETAIL_%@"
+ "QS_FOLLOWUP_OTHER_PHONE_TITLE"
+ "QS_IN_PROGRESS"
+ "QS_LOCAL_SIGNOUT_CONFIRM_BUTTON_CANCEL"
+ "QS_LOCAL_SIGNOUT_CONFIRM_BUTTON_CONTINUE"
+ "QS_LOCAL_SIGNOUT_CONFIRM_MESSAGE"
+ "QS_LOCAL_SIGNOUT_CONFIRM_TITLE_%@"
+ "QS_NOT_AVAILABLE"
+ "QS_NO_WIFI_DETAILS"
+ "QS_NO_WIFI_TITLE"
+ "QS_PRIMARY_SETTING_UP_TITLE"
+ "QS_SETTING_UP_DETAILS"
+ "QS_SETTING_UP_TITLE"
+ "QS_SHARE_COMPLETE_DETAIL"
+ "QS_SHARE_COMPLETE_DETAIL_%@"
+ "QS_SHARE_COMPLETE_DETAIL_%@_%@"
+ "QS_SHARE_COMPLETE_DETAIL_DEVICE_%@"
+ "QS_SHARE_ESIM_DETAILS"
+ "QS_SHARE_ESIM_SET_UP_CARRIER_%@"
+ "QS_SHARE_ESIM_SET_UP_DEVICE_NAMES_%@"
+ "QS_SHARE_ESIM_SET_UP_PHONE_%@"
+ "QS_SHARE_ESIM_TITLE"
+ "QS_SHARE_PHONE_NUMBER_DETAILS"
+ "QS_SHARE_PHONE_NUMBER_LIST_DETAILS"
+ "QS_SHARE_PHONE_NUMBER_NO_TRANSFER_DETAILS"
+ "QS_SLIDING_CONTINUE_ON_OTHER_PHONE_DETAILS"
+ "QS_SLIDING_CONTINUE_ON_OTHER_PHONE_TITLE"
+ "QS_SLIDING_TRANSFER_TIMEOUT_DESCRIPTION"
+ "QS_SLIDING_TRANSFER_TIMEOUT_DESCRIPTION_BUDDY"
+ "QS_SLIDING_TRANSFER_TIMEOUT_TITLE"
+ "QS_SWAP_CONSENT_DETAIL"
+ "QS_SWAP_CONSENT_TITLE"
+ "QS_SWAP_ESIM_DETAILS"
+ "QS_SWAP_ESIM_TITLE"
+ "QS_SWAP_PRIMARY_ACTION_MESSAGE"
+ "QS_SWAP_PRIMARY_ACTION_TITLE_%@"
+ "QS_TRANSFER_ESIM_DETAILS"
+ "QS_WAIT_SOURCE_CONSENT_DETAILS"
+ "QS_WAIT_SOURCE_CONSENT_TITLE"
+ "QUICK_SWITCH_CONFIRM_TITLE"
+ "QUICK_SWITCH_DOUBLE_CLICK_SIDE_BUTTON"
+ "QUICK_SWITCH_PRIMARY_COMPLETE_FAILURE_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_COMPLETE_FAILURE_TITLE"
+ "QUICK_SWITCH_PRIMARY_COMPLETE_IN_PROGRESS_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_COMPLETE_SUCCESS_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_COMPLETE_SUCCESS_TITLE"
+ "QUICK_SWITCH_PRIMARY_COMPLETE_TIMEOUT_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_COMPLETE_TIMEOUT_TITLE"
+ "QUICK_SWITCH_PRIMARY_REVERSE_PROVISIONING_SKIPPED_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_REVERSE_PROVISIONING_SKIPPED_TITLE"
+ "QUICK_SWITCH_PRIMARY_SHARING_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_SHARING_TITLE"
+ "QUICK_SWITCH_PRIMARY_SLIDING_START_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_SLIDING_START_TITLE"
+ "QUICK_SWITCH_PRIMARY_START_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_START_TITLE"
+ "QUICK_SWITCH_PRIMARY_TRANSFER_START_SUBTITLE"
+ "QUICK_SWITCH_PRIMARY_WEBSHEET_INCOMPLETE_DETAIL"
+ "QUICK_SWITCH_PRIMARY_WEBSHEET_INCOMPLETE_TITLE"
+ "QUICK_SWITCH_SHARING_IN_PROGRESS"
+ "QUICK_SWITCH_SLIDING_CONFIRM_TITLE"
+ "QUICK_SWITCH_WEBSHEET_INCOMPLETE_DECISION_DETAIL"
+ "QUICK_SWITCH_WEBSHEET_INCOMPLETE_DECISION_TITLE"
+ "QUICK_SWITCH_WEBSHEET_INCOMPLETE_SET_UP_LATER"
+ "Quick Switch primary enrollment complete - result: %ld @%s"
+ "QuickSwitch"
+ "QuickSwitchAccount"
+ "QuickSwitchAccounts"
+ "QuickSwitchConsent"
+ "QuickSwitchConsentAppName"
+ "QuickSwitchConsentIccid"
+ "QuickSwitchConsentNumberSuffix"
+ "QuickSwitchConsentPhoneNumber"
+ "QuickSwitchConsentSecondaryIccid"
+ "QuickSwitchConsentSecondaryPhoneNumber"
+ "QuickSwitchDevice"
+ "QuickSwitchEnrollmentFlowType"
+ "QuickSwitchFlowType"
+ "QuickSwitchFollowUpPhoneNumber"
+ "QuickSwitchIcon"
+ "QuickSwitchLifeCycleChange"
+ "QuickSwitchOnboarding"
+ "QuickSwitchTransferPlanMap"
+ "RCSOnPartiallyActiveSim"
+ "RecommendedCarrierApps"
+ "RemoteSignup"
+ "SIMSetupAssistant"
+ "Secure intent gesture completed, advancing to sharing pane @%s"
+ "SecureIntent"
+ "SerialNumber"
+ "Share eSIM"
+ "Showing QuickSwitch swap alert for device: %@ @%s"
+ "Skipping SODA query, carrier setup items already provided @%s"
+ "Skipping because user selected QS option @%s"
+ "Source OS version %@ is below %@ - skipping Quick Switch @%s"
+ "Source device class is %@, not iPhone - skipping Quick Switch @%s"
+ "SourceAutoReconnect"
+ "SourceDeviceClass"
+ "SourceSerialNumber"
+ "THIS_IPHONE"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATAONLY_NO_RCS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATAONLY_RCS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATAONLY_RCS_NOT_REGISTERED_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATA_VOICE_NO_RCS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATA_VOICE_RCS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_DATA_VOICE_RCS_NOT_REGISTERED_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_RCS_DATAONLY_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_RCS_DATAONLY_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_RCS_DATA_VOICE_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_ESIM_DETAILS_RCS_DATA_VOICE_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_DATAONLY_NO_RCS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_DATAONLY_RCS_REGISTERED_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_DATA_VOICE_NO_RCS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_DATA_VOICE_RCS_NOT_REGISTERED_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_DATA_VOICE_RCS_REGISTERED_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_RCS_DATAONLY_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_RCS_DATAONLY_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_RCS_DATAONLY_NOT_REGISTERED_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_RCS_DATA_VOICE_%@"
+ "TRAVEL_BUDDY_TRAVEL_AND_HOME_PSIM_DETAILS_RCS_DATA_VOICE_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_IMESSAGE_ON_BOTH_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_IMESSAGE_ON_HOME_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_IMESSAGE_ON_HOME_NO_IMESSAGE_NO_RCS_ON_ONE_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_IMESSAGE_ON_HOME_RCS_ON_ONE_%@_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_NO_IMESSAGE_NO_RCS_ON_ONE_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_NO_IMESSAGE_ON_ONE_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_NO_RCS_ON_ONE_%@_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_RCS_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_RCS_NO_IMSG_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_RCS_ON_BOTH_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_RCS_ON_HOME_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_RCS_ON_HOME_IMESSAGE_ON_ONE_%@_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_DUALSIM_RCS_ON_HOME_NO_IMESSAGE_NO_RCS_ON_ONE_%@_%@_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_DETAILS_RCS_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_IMESSAGE_DETAILS_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_NO_IMSG_NO_RCS_DETAILS_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_ONLY_RCS_DETAILS_%@"
+ "TRAVEL_BUDDY_TRAVEL_ESIM_RCS_FOOTER"
+ "TRAVEL_BUDDY_TRAVEL_PSIM_RCS_FOOTER"
+ "TRAVEL_ESIM_SETUP_COMPLETE_DETAILS_DATA_ONLY_%@"
+ "TSCellularPlanActivatingFlow initialized with QuickSwitch account. isSwap: %d, primary:%@, secondary-iccid: %@ @%s"
+ "Transfer"
+ "Transfer eSIM"
+ "TransferCloudPlansInstall"
+ "TransferQRCode"
+ "TravelEducation"
+ "TravelMode"
+ "Triggering transition from %@ to secure intent @%s"
+ "Triggering transition from %@ to secure intent for flowType %lu @%s"
+ "Type: %s (%lu) @%s"
+ "UseCase"
+ "User confirmed device selection: %@ (role: %d, newLine: %d) @%s"
+ "User confirmed flow type choice: %d @%s"
+ "User confirmed selection of group: %@ @%s"
+ "User confirmed selection: %@ @%s"
+ "User consented to Quick Switch enrollment @%s"
+ "User selected device: %@ (role: %d) @%s"
+ "User selected group key: %@ with %lu accounts @%s"
+ "User selected option: Share eSIM (Quick Switch) @%s"
+ "User selected option: Transfer eSIM @%s"
+ "User selected: Keep Primary on %@ (enroll only) @%s"
+ "User selected: Set up Primary eSIM on this iPhone (sliding) @%s"
+ "User selected: Set up new line on this iPhone @%s"
+ "UserIntentContext"
+ "UserResponse"
+ "Using cached D2D transfer plans @%s"
+ "Websheet flow presented successfully @%s"
+ "WebsheetSignup"
+ "WiFi check result from old device: available=%d @%s"
+ "[E]Expected consent or sharing view controller but found: %@ @%s"
+ "[E]Failed to archive simsetup D2D info: %@ @%s"
+ "[E]Failed to bootstrap QuickSwitch secondary flow: %@ @%s"
+ "[E]Failed to create bottom constraint: %@ @%s"
+ "[E]Failed to create spinner constraints: %@ @%s"
+ "[E]Failed to decode simsetupD2DInfo: %@ @%s"
+ "[E]Failed to get QuickSwitch primary account: %@ @%s"
+ "[E]Failed to get carrier setup items: %@ @%s"
+ "[E]Failed to get context info for,  %@ @%s"
+ "[E]Failed to get lazuli system configuration,  %@ @%s"
+ "[E]Failed to get number sharing info for all SIMs: %@ @%s"
+ "[E]Failed to query supportsDynamicSIMConfiguration: %@ @%s"
+ "[E]Failed to release bootstrap: %@ @%s"
+ "[E]Failed to request bootstrap: %@ @%s"
+ "[E]Failed to transfer QuickSwitch: %@ @%s"
+ "[E]FindMyWipe: failed to get number sharing info for serial %@: %@ @%s"
+ "[E]FindMyWipe: missing device identifier @%s"
+ "[E]Invalid TSTravelSimTypeSelectionViewController @%s"
+ "[E]Missing primary ICCID, cannot notify CT about failure @%s"
+ "[E]Missing primary iccid in options @%s"
+ "[E]Missing websheet URL in options @%s"
+ "[E]No QuickSwitch account selected! @%s"
+ "[E]No primary account available for activating subflow @%s"
+ "[E]No primary account found for iccid: %@ @%s"
+ "[E]QS account has no valid iccid for grouping, skipping @%s"
+ "[E]Received unhandled enrollment result: %lu @%s"
+ "[E]Unexpected type for UserIntentContext: %@ @%s"
+ "[E]completion is nil @%s"
+ "[E]e:%@ @%s"
+ "[E]enroll qs failed: %@ @%s"
+ "[E]enrollment consent not handled properly in CT : %@ @%s"
+ "[E]firstViewController called without completion handler - async bootstrap required @%s"
+ "[E]getQuickSwitchAccountsForDisplayPlans failed: %@ @%s"
+ "[E]iccid is nil @%s"
+ "[E]invalid SSQuickSwitchAlertViewController @%s"
+ "[E]invalid SSQuickSwitchDevicePickerViewController @%s"
+ "[E]invalid SSQuickSwitchListViewController @%s"
+ "[E]invalid SSQuickSwitchSecondarySharingViewController @%s"
+ "[E]missing user intent context @%s"
+ "[E]missing view delegate @%s"
+ "[E]no plan info to resolve websheet incomplete @%s"
+ "[E]query quick switch failed : %@ @%s"
+ "[E]query quick switch for display plans failed : %@ @%s"
+ "[E]secure intent dismissed without completion @%s"
+ "[E]secure intent failed, cancel the flow @%s"
+ "[E]transferQuickSwitch failed: %@ @%s"
+ "[E]unexpected qs flow type @%s"
+ "[E]unhandled update : %@ @%s"
+ "[E]updateQuickSwitchConsentResult failed: %@ @%s"
+ "[E]websheet flow returned nil view controller @%s"
+ "[E]websheet incomplete with invalid top VC. expect WaitOnWebsheet VC. @%s"
+ "[F]BLOCKED: nav.topVC has presentedVC:%@, push will fail! @%s"
+ "[F]Missing required fields for case %ld @%s"
+ "[F]unexpected flow type @%s"
+ "[I] Updating plan info: CTPlanTransferStatusTimeoutInstallOngoing. Current VC: %@ @%s"
+ "a"
+ "app in background, deassert bootstrap @%s"
+ "app in foreground, assert bootstrap @%s"
+ "arrow.triangle.swap"
+ "available"
+ "cachedTransferPlans"
+ "checkmark.circle"
+ "choice%ld"
+ "completed"
+ "consentCell%ld"
+ "deferView"
+ "detail"
+ "device%ld"
+ "dollarsign"
+ "dto reply:%@ @%s"
+ "enroll result : %@ @%s"
+ "enrollment failed: Wi-Fi unavailable on old device [result=%lu] @%s"
+ "enrollment phase started @%s"
+ "enrollment-started"
+ "externalized context = %@ isSecureIntentRequired: %d, isDtoEvaluationRequired:%d, quickSwitchFlowType:%lu @%s"
+ "failed"
+ "first view controller : %@(%p) @%s"
+ "first view controller: %@(%p) @%s"
+ "flow dismiss. flow.complete:%d, waiting for result:%d @%s"
+ "getting quick switch plans from display plans @%s"
+ "group%ld"
+ "https://support.apple.com/en-us/118669?cid=mc-ols-esim-article_ht212780-ios_ui-07192022"
+ "iPhone"
+ "iccid: %@, capability:%s account:<role: %s, state: %s> @%s"
+ "incomplete"
+ "iphone.and.arrow.forward.inward"
+ "iphone.on.iphone"
+ "isActivationPolicyMismatch: %d @%s"
+ "isDualeSIMCapabilityLoss"
+ "launched"
+ "location"
+ "marketing-name"
+ "matchingId"
+ "message.and.video"
+ "notified CT about Quick Switch enrollment cancellation with error: %@ @%s"
+ "phase"
+ "phone"
+ "phone.badge.checkmark"
+ "primary : %@, secondary : %@, qs flow: %s @%s"
+ "primary-iccid"
+ "primary-iccid: %@, use case: %@ @%s"
+ "quick-switch"
+ "quick-switch-enrollment-phase"
+ "quick-switch-provisioning-info"
+ "quick-switch-websheet-status"
+ "quick-switch-wifi-check"
+ "required : %{BOOL}d, e:%@ @%s"
+ "resolved websheet incomplete with followup:%{bool}d, error:%@ @%s"
+ "secondary-iccid"
+ "secure intent PRXCard dismissed, isSecureIntentPending:%d @%s"
+ "simsetupQSInfo"
+ "sliding flow, auto consent enrollment for %@ @%s"
+ "source class : %@, os ver : %@ @%s"
+ "symbol"
+ "transfer plans: %lu, store visit:%lu @%s"
+ "transfer plans: %lu, store visit:%lu, hidden: %lu @%s"
+ "transferQuickSwitch succeeded @%s"
+ "updateQuickSwitchEnrollmentStatus websheet status:%@ @%s"
+ "updateQuickSwitchEnrollmentStatus: primaryIccid:%@, secondaryIccid:%@ @%s"
+ "userSelectedQSOption"
+ "v16@?0@\"UIGraphicsImageRendererContext\"8"
+ "v24@?0@\"CTQuickSwitchAccountInfo\"8@\"NSError\"16"
+ "websheet FAILED on primary! current VC: %@ @%s"
+ "websheet flow already dismissed. @%s"
+ "websheet incomplete on primary device! current VC: %@ @%s"
+ "websheet launched on primary device, advance to WaitOnWebsheet pane @%s"
+ "websheet: [%@] %@ @%s"
+ "xmark.circle"
+ "\xf04\xe1"
- "#16@0:8"
- "&"
- "+[TSFlowHelper getAccountMemberTransferablePlanWithSameCarrierName:transferablePlans:]"
- "+[TSFlowHelper hasTransferablePlanWithSameCarrierName:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:]"
- "+[TSUtilities getStoreVisitStatusForPlan:cache:]"
- ","
- "-[TSActivationFlowWithSimSetupFlow _filterCarrierSetupItems:]"
- "-[TSActivationFlowWithSimSetupFlow didPurchasePlanSuccessfullyWithEid:imei:meid:iccid:alternateSDMP:state:]"
- "-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke"
- "-[TSMultiPlanIntermediateViewController initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:]"
- "-[TSProximitySourceTransferFlow firstViewController:]"
- "-[TSRemotePlanSignUpFlow didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:state:]_block_invoke"
- "-[TSSecureIntentGestureViewController initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:]"
- "-[TSTransferCloudFlowModel filterCarrierSetupItems:]"
- "-[TSTransferFlowModel filterCarrierSetupItems:]"
- "-[TSTransferFlowModel shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:]"
- ".cxx_destruct"
- "@"
- "@\"<AVCaptureMetadataOutputObjectsDelegate>\""
- "@\"<DCTCodeDelegate>\""
- "@\"<ESIMProxTransferControllerDelegate>\""
- "@\"<SSScanViewControllerDelegate>\""
- "@\"<TSCellularPlanManagerCacheDelegate>\""
- "@\"<TSEntitlementJSHandlerDelegate>\""
- "@\"<TSSIMSetupDelegate>\""
- "@\"<TSSIMSetupFlowDelegate>\""
- "@\"<TSSIMSetupFlowDelegate>\"16@0:8"
- "@\"<UITableViewDelegate>\""
- "@\"<UIViewControllerAnimatedTransitioning>\"48@0:8@\"UINavigationController\"16q24@\"UIViewController\"32@\"UIViewController\"40"
- "@\"<UIViewControllerInteractiveTransitioning>\"32@0:8@\"UINavigationController\"16@\"<UIViewControllerAnimatedTransitioning>\"24"
- "@\"ASCLockupRequest\""
- "@\"ASCLockupView\""
- "@\"ASCMetricsActivity\"32@0:8@\"ASCLockupView\"16@\"<ASCOffer>\"24"
- "@\"AVCaptureDeviceInput\""
- "@\"AVCaptureSession\""
- "@\"AVCaptureVideoPreviewLayer\""
- "@\"BluetoothChecker\""
- "@\"CAShapeLayer\""
- "@\"CBCentralManager\""
- "@\"CNGeminiBadge\""
- "@\"CTCellularPlanCarrierItem\""
- "@\"CTCellularPlanItem\""
- "@\"CTDanglingPlanItem\""
- "@\"CTDeviceIdentifier\""
- "@\"CTDisplayPlan\""
- "@\"CTDisplayPlanList\""
- "@\"CTPlan\""
- "@\"CTPlanList\""
- "@\"CTRemotePlan\""
- "@\"CTUserLabel\""
- "@\"CTXPCServiceSubscriptionContext\""
- "@\"CUMessageSession\""
- "@\"CUSystemMonitor\""
- "@\"CoreTelephonyClient\""
- "@\"IMOneTimeCodeAccelerator\""
- "@\"LAUIPhysicalButtonView\""
- "@\"NFAssertion\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"UITableView\"16"
- "@\"NSArray\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSArray\"40@0:8@\"SFSafariViewController\"16@\"NSURL\"24@\"NSString\"32"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"24@0:8@\"WKWebView\"16"
- "@\"NSError\""
- "@\"NSIndexPath\""
- "@\"NSIndexPath\"24@0:8@\"UITableView\"16"
- "@\"NSIndexPath\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSLayoutConstraint\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSString\"32@0:8@\"UITableView\"16q24"
- "@\"NSTimer\""
- "@\"NSURL\""
- "@\"NSURL\"24@0:8@\"_SFFormAutoFillController\"16"
- "@\"NSUUID\"16@0:8"
- "@\"OBBoldTrayButton\""
- "@\"OBLinkTrayButton\""
- "@\"OBTrayButton\""
- "@\"OBTrayButton\"16@0:8"
- "@\"PKGlyphView\""
- "@\"PRXAction\""
- "@\"RUIPage\"40@0:8@\"RemoteUIController\"16@\"NSString\"24@\"NSDictionary\"32"
- "@\"RemoteUIController\""
- "@\"SSConfirmationCodeViewController\""
- "@\"SSInstallPlanInformation\""
- "@\"SSLabelPickerViewController\""
- "@\"SSNFCAssertion\""
- "@\"SSOBBoldTrayButton\""
- "@\"SSOBLinkTrayButton\""
- "@\"SSProximityDevice\""
- "@\"SSSpinner\""
- "@\"SSSpinner\"16@0:8"
- "@\"TSBuddyMLController\""
- "@\"TSBuddyMLViewController\""
- "@\"TSCellularPlanProximityTransferController\""
- "@\"TSCellularPlanQRCodeScannerView\""
- "@\"TSCellularSetupLoadingView\""
- "@\"TSRemotePlanWebsheetContext\""
- "@\"TSSIMSetupFlow\""
- "@\"TSTermsAndConditionsViewController\""
- "@\"TSTransferCloudFlowModel\""
- "@\"TSTransferFlowModel\""
- "@\"TSTransferOneTimeCodeViewController\""
- "@\"UIActivityIndicatorView\""
- "@\"UIBarButtonItem\""
- "@\"UIButton\""
- "@\"UIContextMenuConfiguration\"48@0:8@\"UITableView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UIImage\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
- "@\"UIMenu\"48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSArray\"40"
- "@\"UINavigationController\""
- "@\"UIStackView\""
- "@\"UISwipeActionsConfiguration\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UISwitch\""
- "@\"UITableViewCell\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITableViewHeaderFooterView\""
- "@\"UITargetedPreview\"32@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UITextField\""
- "@\"UITextView\""
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"UITableView\"16q24"
- "@\"UIView\"32@0:8@\"WKWebView\"16@\"<_WKFormInputSession>\"24"
- "@\"UIViewController\""
- "@\"UIViewController\"24@0:8@\"ASCLockupView\"16"
- "@\"UIViewController\"32@0:8@\"UIPresentationController\"16q24"
- "@\"UIViewController\"40@0:8@\"WKWebView\"16@\"WKPreviewElementInfo\"24@\"NSArray\"32"
- "@\"UIViewController<PRXCardContentProviding>\""
- "@\"UIViewController<TSSetupFlowItem>\""
- "@\"WBSSavedAccountContext\"24@0:8@\"_SFFormAutoFillController\"16"
- "@\"WKUserContentController\""
- "@\"WKWebView\""
- "@\"WKWebView\"48@0:8@\"WKWebView\"16@\"WKWebViewConfiguration\"24@\"WKNavigationAction\"32@\"WKWindowFeatures\"40"
- "@\"_SFFormAutoFillController\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8B16B20"
- "@24@0:8Q16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8@16i24"
- "@28@0:8B16@20"
- "@28@0:8B16B20B24"
- "@28@0:8B16i20i24"
- "@28@0:8Q16B24"
- "@28@0:8i16B20B24"
- "@28@0:8i16i20B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16B24B28"
- "@32@0:8@16q24"
- "@32@0:8B16@20B28"
- "@32@0:8B16B20@24"
- "@32@0:8Q16@24"
- "@32@0:8q16@24"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24@28"
- "@36@0:8@16B24B28B32"
- "@36@0:8@16d24f32"
- "@36@0:8B16@20@28"
- "@36@0:8B16@20B28B32"
- "@36@0:8B16B20B24@28"
- "@36@0:8q16B24@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24B32B36"
- "@40@0:8@16Q24@32"
- "@40@0:8@16Q24B32B36"
- "@40@0:8Q16@24@32"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16@24B32B36B40"
- "@44@0:8@16@24Q32B40"
- "@44@0:8@16B24B28B32B36B40"
- "@44@0:8Q16B24@28@36"
- "@44@0:8Q16Q24B32@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@48@0:8@16B24B28@32@40"
- "@48@0:8@16B24B28B32B36B40B44"
- "@48@0:8@16q24@32@40"
- "@48@0:8@16{_NSRange=QQ}24@40"
- "@48@0:8Q16@24Q32@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@52@0:8@16@24@32@40B48"
- "@52@0:8@16Q24B32@36B44B48"
- "@56@0:8@16@24B32@36@44B52"
- "@56@0:8@16B24B28@32@40B48B52"
- "@56@0:8@16Q24B32Q36@44B52"
- "@60@0:8@16@24@32B40B44B48B52B56"
- "@60@0:8@16B24B28B32@36@44B52B56"
- "@60@0:8@16B24B28B32B36B40B44@48B56"
- "@60@0:8@16{UIEdgeInsets=dddd}24f56"
- "@60@0:8Q16@24@32@40B48B52B56"
- "@64@0:8@16B24B28B32@36@44B52B56B60"
- "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48Q56"
- "@68@0:8@16@24Q32B40Q44@52B60B64"
- "@72@0:8@16@24Q32B40Q44@52B60B64B68"
- "@88@0:8B16q20@28Q36@44B52@56B64@68@76B84"
- "@?"
- "@?16@0:8"
- "AR"
- "ASCLockupViewDelegate"
- "AVCaptureMetadataOutputObjectsDelegate"
- "Account member has a transferrable plan with a SODA tether @%s"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIPresentationController\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@\"UITextField\"16"
- "B24@0:8@\"_SFFormAutoFillController\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8d16"
- "B32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24"
- "B32@0:8@\"WKWebView\"16@\"<_WKFocusedElementInfo>\"24"
- "B32@0:8@\"WKWebView\"16@\"<_WKFormInputSession>\"24"
- "B32@0:8@\"WKWebView\"16@\"WKPreviewElementInfo\"24"
- "B32@0:8@16@24"
- "B32@0:8Q16@24"
- "B40@0:8@\"RemoteUIController\"16@\"NSMutableURLRequest\"24@\"NSURLResponse\"32"
- "B40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "B44@0:8@16@24B32@36"
- "B48@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24@\"RUIElement\"32@\"RUIPage\"40"
- "B48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSString\"40"
- "B48@0:8@16:24@32@40"
- "B48@0:8@16@24@32@40"
- "B48@0:8@16{_NSRange=QQ}24@40"
- "BluetoothChecker"
- "BuddyPinAutoLayout"
- "C"
- "C16@0:8"
- "CBCentralManagerDelegate"
- "CGColor"
- "CGImage"
- "CGPath"
- "CGRectValue"
- "CSN"
- "CTDisplayPlan"
- "CategorizedPlans"
- "Consolidated"
- "CoreTelephonyClientCellularPlanManagementDelegate"
- "CoreTelephonyClientDelegate"
- "CrossPlatformManualDetailsViewController"
- "CrossPlatformShowManualDetailsViewController"
- "CrossPlatformTargetQRCodeWarningViewController"
- "CrossPlatformTransferAuthQRCodeViewController"
- "CrossPlatformTransferIntroViewController"
- "CrossPlatformTransferSourceSelectionWarningViewController"
- "DCTCodeDelegate"
- "DCTCodeManager"
- "ESIMProxTransferControllerDelegate"
- "ExitBuddyIconView"
- "FormattedCarrierListFromSet:"
- "FormattedCarrierListFromSet:conjunction:"
- "HTTPBody"
- "InModalPresentation"
- "InteractiveUI"
- "LAUIDelegate"
- "MapsEdgeConstraints"
- "NFCTransferStatus"
- "NSObject"
- "NSString"
- "NavigationBar"
- "One click transferrable plan exists with same carrier name [%@] @%s"
- "Override"
- "PRXFlowDelegate"
- "PhoneNumber"
- "Plan %@ will be removed from transfer list @%s"
- "Q16@0:8"
- "Q24@0:8@\"UINavigationController\"16"
- "Q24@0:8@16"
- "Q24@0:8^@16"
- "RangeBold"
- "RemoteUIControllerDelegate"
- "SFFormAutoFillControllerDelegate"
- "SFSafariViewControllerDelegate"
- "SHA256"
- "SIMIdentifier"
- "SS"
- "SSCardManualEntryViewController"
- "SSCellularPlanCarrierAppsViewController"
- "SSCellularPlanScanViewController"
- "SSCellularSetupMultiSIMActivatingViewController"
- "SSCellularSetupMultiSIMConnectingViewController"
- "SSConfirmationCodeViewController"
- "SSCrossPlatformScanViewController"
- "SSCrossPlatformTransferSourceSelectionViewController"
- "SSHelper"
- "SSInstallPlanInformation"
- "SSLabelPickerViewController"
- "SSLimitedSelectableTableView"
- "SSMultiSIMResultViewController"
- "SSNFCAssertion"
- "SSOBBoldTrayButton"
- "SSOBLinkTrayButton"
- "SSPRXD2DMigrationDoneViewController"
- "SSProximityDevice"
- "SSQRCodeIntroViewController"
- "SSRecommendedCarrierAppCell"
- "SSRemoteAlertFlowDelegate"
- "SSScanViewController"
- "SSScanViewControllerDelegate"
- "SSSpinner"
- "SSSpinnerProtocol"
- "SSTransferIntroViewController"
- "SSUITableViewController"
- "SSUIViewController"
- "SSUserConsentViewController"
- "SSVisitStoreViewController"
- "SSeSIMCountRestrictionWarningViewController"
- "SafariServices.wkbundle"
- "Single"
- "Spinner"
- "SubFlow"
- "T#,R"
- "T@\"<AVCaptureMetadataOutputObjectsDelegate>\",N,V_delegate"
- "T@\"<DCTCodeDelegate>\",W,V_dctDelegate"
- "T@\"<ESIMProxTransferControllerDelegate>\",W,N,V_delegate"
- "T@\"<SSScanViewControllerDelegate>\",W,V_qrcodeDelegate"
- "T@\"<TSCellularPlanManagerCacheDelegate>\",W,N,Vdelegate"
- "T@\"<TSEntitlementJSHandlerDelegate>\",W,V_callbackDelegate"
- "T@\"<TSSIMSetupDelegate>\",W,V_delegate"
- "T@\"<TSSIMSetupFlowDelegate>\",W"
- "T@\"<TSSIMSetupFlowDelegate>\",W,V_delegate"
- "T@\"<TSSIMSetupFlowDelegate>\",W,Vdelegate"
- "T@\"<UITableViewDelegate>\",W,N,V_viewDelegate"
- "T@\"ASCLockupView\",&,N,V_lockupView"
- "T@\"AVCaptureVideoPreviewLayer\",R,N,V_previewLayer"
- "T@\"CNGeminiBadge\",&,V_badge"
- "T@\"CTCellularPlanCarrierItem\",&,N,V_selectedCarrierItem"
- "T@\"CTCellularPlanItem\",&,V_associatedPlanItem"
- "T@\"CTCellularPlanItem\",&,V_defaultVoiceItem"
- "T@\"CTCellularPlanItem\",&,V_planItem"
- "T@\"CTDanglingPlanItem\",&,V_danglingPlanItem"
- "T@\"CTDeviceIdentifier\",&,V_transferPlanDeviceID"
- "T@\"CTDisplayPlan\",&,V_displayPlan"
- "T@\"CTDisplayPlan\",&,V_selectedTransferPlan"
- "T@\"CTDisplayPlan\",R,V_selectedPlan"
- "T@\"CTDisplayPlanList\",&,N,V_carrierSetupItems"
- "T@\"CTDisplayPlanList\",&,N,V_crossPlatformTransferItems"
- "T@\"CTDisplayPlanList\",&,N,V_pendingInstallItems"
- "T@\"CTPlan\",&,V_carrierSetupPlan"
- "T@\"CTPlan\",&,V_plan"
- "T@\"CTPlanList\",&,V_planList"
- "T@\"CTRemotePlan\",&,V_transferPlan"
- "T@\"CTUserLabel\",&,V_customLabel"
- "T@\"CTUserLabel\",&,V_initialLabel"
- "T@\"CTUserLabel\",R"
- "T@\"CTXPCServiceSubscriptionContext\",N,V_subscriptionContext"
- "T@\"CUMessageSession\",&,V_messageSession"
- "T@\"CUMessageSession\",&,V_session"
- "T@\"CUSystemMonitor\",&,V_systemMonitor"
- "T@\"CoreTelephonyClient\",&,N,V_client"
- "T@\"CoreTelephonyClient\",&,N,V_ctClient"
- "T@\"CoreTelephonyClient\",&,V_client"
- "T@\"CoreTelephonyClient\",&,V_ctClient"
- "T@\"IMOneTimeCodeAccelerator\",&,V_oneTimeCodeAccelerator"
- "T@\"LAUIPhysicalButtonView\",&,N,V_physicalButtonView"
- "T@\"NFAssertion\",&,V_preventConnectionHandoverAssertion"
- "T@\"NSArray\",&"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",&,N,V_carrierItems"
- "T@\"NSArray\",&,N,V_descriptors"
- "T@\"NSArray\",&,V_allPlans"
- "T@\"NSArray\",&,V_cachedButtons"
- "T@\"NSArray\",&,V_cachedPlanItems"
- "T@\"NSArray\",&,V_danglingPlanItems"
- "T@\"NSArray\",&,V_dctInfo"
- "T@\"NSArray\",&,V_descriptors"
- "T@\"NSArray\",&,V_installInfos"
- "T@\"NSArray\",&,V_leftBarButtonItems"
- "T@\"NSArray\",&,V_planItemBadges"
- "T@\"NSArray\",&,V_planItems"
- "T@\"NSArray\",&,V_plans"
- "T@\"NSArray\",&,V_predefinedUserLabels"
- "T@\"NSArray\",&,V_selectedItems"
- "T@\"NSArray\",&,V_selectedPlanItems"
- "T@\"NSArray\",&,V_selectedPlans"
- "T@\"NSArray\",&,V_transferIneligiblePlans"
- "T@\"NSArray\",&,V_transferPlans"
- "T@\"NSArray\",&,VcachedButtons"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,N"
- "T@\"NSData\",&,N,V_externalizedContext"
- "T@\"NSData\",&,V_externalizedContext"
- "T@\"NSDictionary\",&,N,V_options"
- "T@\"NSDictionary\",&,N,V_postdata"
- "T@\"NSDictionary\",&,V_options"
- "T@\"NSDictionary\",&,V_peerDeviceInfo"
- "T@\"NSDictionary\",&,V_postdata"
- "T@\"NSDictionary\",&,V_queryParamToTitle"
- "T@\"NSDictionary\",&,V_remoteInfo"
- "T@\"NSDictionary\",&,V_text"
- "T@\"NSDictionary\",&,V_websheetOptions"
- "T@\"NSError\",&,V_failureWebsheetError"
- "T@\"NSError\",&,V_installError"
- "T@\"NSError\",&,V_lastError"
- "T@\"NSError\",&,V_planError"
- "T@\"NSError\",&,V_planInstallError"
- "T@\"NSIndexPath\",&,V_chosenLabelIndexPath"
- "T@\"NSIndexPath\",&,V_chosenTargetCellularPlanItem"
- "T@\"NSIndexPath\",&,V_chosenUseIndexPath"
- "T@\"NSLayoutConstraint\",&,N,V_bottomConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_heightAnchor"
- "T@\"NSLayoutConstraint\",&,N,V_leadingConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_leftConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_rightConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_topConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_trailingConstraint"
- "T@\"NSMutableArray\",&,N"
- "T@\"NSMutableArray\",&,N,V_requireStoreVisitItems"
- "T@\"NSMutableArray\",&,N,V_transferIneligibleItems"
- "T@\"NSMutableArray\",&,N,V_transferItems"
- "T@\"NSMutableArray\",&,N,V_transferPlans"
- "T@\"NSMutableArray\",&,N,V_transferableHiddenInCloudFlowItems"
- "T@\"NSMutableArray\",&,V_chosenUseIndexPaths"
- "T@\"NSMutableArray\",&,V_currentItemsForIMessage"
- "T@\"NSMutableArray\",&,V_installingPlanInfos"
- "T@\"NSMutableArray\",&,V_pendingInteractiveViewControllers"
- "T@\"NSMutableArray\",&,V_sortedPlanItemsWithPendingLabels"
- "T@\"NSMutableArray\",&,V_subFlowViewControllers"
- "T@\"NSMutableArray\",&,V_transferIneligibleViaCloudItems"
- "T@\"NSMutableArray\",&,V_transferItems"
- "T@\"NSMutableArray\",&,V_transferPlans"
- "T@\"NSMutableArray\",&,V_userEnabledPlanInfos"
- "T@\"NSMutableDictionary\",&,V_backOptions"
- "T@\"NSMutableDictionary\",&,V_hasProvisioningServiceImpactMap"
- "T@\"NSMutableDictionary\",&,V_navigationItems"
- "T@\"NSMutableDictionary\",&,V_previousLeftBarButtonItems"
- "T@\"NSMutableDictionary\",&,V_previousRightBarButtonItems"
- "T@\"NSMutableDictionary\",&,V_simsetupD2dInfo"
- "T@\"NSMutableDictionary\",&,V_storeVisitedMap"
- "T@\"NSMutableSet\",&,V_cancelledDeviceIDs"
- "T@\"NSMutableSet\",&,V_displayedDeviceIDs"
- "T@\"NSNumber\",&,V_eSIMTravelState"
- "T@\"NSNumber\",&,V_waitForPhoneNumber"
- "T@\"NSSet\",&,V_originalEnabledPlans"
- "T@\"NSString\",&,N,V_code"
- "T@\"NSString\",&,N,V_formatedDescriptor"
- "T@\"NSString\",&,N,V_websheetUrl"
- "T@\"NSString\",&,V_buddyMLURL"
- "T@\"NSString\",&,V_carrierErrorCode"
- "T@\"NSString\",&,V_carrierName"
- "T@\"NSString\",&,V_carrierNameForSelectedItem"
- "T@\"NSString\",&,V_currentTitle"
- "T@\"NSString\",&,V_defaultVoiceIccid"
- "T@\"NSString\",&,V_detailText"
- "T@\"NSString\",&,V_details"
- "T@\"NSString\",&,V_enablingIccid"
- "T@\"NSString\",&,V_iccid"
- "T@\"NSString\",&,V_iccidToEnable"
- "T@\"NSString\",&,V_installBucketSubtitle"
- "T@\"NSString\",&,V_installBucketTitle"
- "T@\"NSString\",&,V_mainText"
- "T@\"NSString\",&,V_name"
- "T@\"NSString\",&,V_normalStateTitle"
- "T@\"NSString\",&,V_phoneNumber"
- "T@\"NSString\",&,V_pin"
- "T@\"NSString\",&,V_planName"
- "T@\"NSString\",&,V_qrcodeBucketSubtitle"
- "T@\"NSString\",&,V_qrcodeBucketTitle"
- "T@\"NSString\",&,V_secondaryButtonDetail"
- "T@\"NSString\",&,V_sourceIccid"
- "T@\"NSString\",&,V_sourceOSVersion"
- "T@\"NSString\",&,V_sourceOsVersion"
- "T@\"NSString\",&,V_targetIccid"
- "T@\"NSString\",&,V_targetIccidHash"
- "T@\"NSString\",&,V_transferBackPlanPhoneNumber"
- "T@\"NSString\",&,V_travelSIM"
- "T@\"NSString\",&,V_url"
- "T@\"NSString\",&,V_websheetUrl"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_confirmationCode"
- "T@\"NSString\",R,V_fauxCardData"
- "T@\"NSString\",R,V_iccid"
- "T@\"NSString\",R,V_type"
- "T@\"NSTimer\",&,V_activatingTimer"
- "T@\"NSTimer\",&,V_timer"
- "T@\"NSURL\",&,N,V_carrierURL"
- "T@\"NSURL\",&,V_roamingInfo"
- "T@\"NSURL\",R,V_url"
- "T@\"NSUUID\",?,R,N"
- "T@\"OBLinkTrayButton\",&,V_otherOptionsButton"
- "T@\"OBLinkTrayButton\",&,V_skipButton"
- "T@\"OBTrayButton\",&"
- "T@\"OBTrayButton\",&,V_spinnerContainer"
- "T@\"OBTrayButton\",&,VspinnerContainer"
- "T@\"PKGlyphView\",&,N,V_glyphView"
- "T@\"PKGlyphView\",&,V_nfcAnimationView"
- "T@\"PRXAction\",&,N,V_confirmTextView"
- "T@\"PRXAction\",&,N,V_doneAction"
- "T@\"PRXAction\",&,V_action"
- "T@\"PRXAction\",&,V_cancelAction"
- "T@\"PRXAction\",&,V_continueAction"
- "T@\"PRXAction\",&,V_primaryAction"
- "T@\"PRXAction\",&,V_retryAction"
- "T@\"PRXAction\",&,V_unlockAction"
- "T@\"RemoteUIController\",&,V_remoteUIController"
- "T@\"SSConfirmationCodeViewController\",W,V_confirmationCodeViewController"
- "T@\"SSLabelPickerViewController\",&,V_labelPickerViewController"
- "T@\"SSNFCAssertion\",&,V_nfcAssertion"
- "T@\"SSOBBoldTrayButton\",&,V_acceptButton"
- "T@\"SSOBBoldTrayButton\",&,V_continueButton"
- "T@\"SSOBBoldTrayButton\",&,V_doneButton"
- "T@\"SSOBLinkTrayButton\",&,V_enterDetailsManuallyButton"
- "T@\"SSOBLinkTrayButton\",&,V_resendOTPButton"
- "T@\"SSOBLinkTrayButton\",&,V_skipButton"
- "T@\"SSProximityDevice\",&,V_btClient"
- "T@\"SSProximityDevice\",&,V_btDevice"
- "T@\"SSProximityDevice\",&,V_btServer"
- "T@\"SSProximityDevice\",&,V_client"
- "T@\"SSProximityDevice\",W,V_btServer"
- "T@\"SSSpinner\",&"
- "T@\"SSSpinner\",&,N,V_spinner"
- "T@\"SSSpinner\",&,V_spinner"
- "T@\"TSBuddyMLViewController\",W,V_buddyMLViewController"
- "T@\"TSCellularPlanProximityTransferController\",&,V_proxTransferController"
- "T@\"TSCellularPlanQRCodeScannerView\",&,V_scannerView"
- "T@\"TSRemotePlanWebsheetContext\",&,V_remotePlanWebsheetContext"
- "T@\"TSSIMSetupFlow\",&,V_subFlow"
- "T@\"TSSIMSetupFlow\",&,V_websheetFlow"
- "T@\"TSSIMSetupFlow\",R"
- "T@\"TSSIMSetupFlow\",W,V_parentFlow"
- "T@\"TSTermsAndConditionsViewController\",W,V_termsAndConditionsViewController"
- "T@\"TSTransferCloudFlowModel\",&,V_model"
- "T@\"TSTransferFlowModel\",&,V_model"
- "T@\"TSTransferOneTimeCodeViewController\",W,V_oneTimeCodeViewController"
- "T@\"UIActivityIndicatorView\",&,N,V_spinner"
- "T@\"UIActivityIndicatorView\",&,V_activityIndicator"
- "T@\"UIActivityIndicatorView\",&,V_indicatorView"
- "T@\"UIBarButtonItem\",&,V_cancelButton"
- "T@\"UIButton\",&,V_acceptButton"
- "T@\"UIButton\",&,V_declineButton"
- "T@\"UIImageView\",&,N,V_imgView"
- "T@\"UIImageView\",&,N,V_triangleImageView"
- "T@\"UIImageView\",&,V_radioImageView"
- "T@\"UILabel\",&,N"
- "T@\"UILabel\",&,N,V_firstLabel"
- "T@\"UILabel\",&,N,V_label"
- "T@\"UILabel\",&,N,V_pinCodeLabel"
- "T@\"UILabel\",&,N,V_secondLabel"
- "T@\"UILabel\",&,V_descriptionLabel"
- "T@\"UILabel\",&,V_label"
- "T@\"UILabel\",&,V_planInfo"
- "T@\"UILabel\",&,V_title"
- "T@\"UILabel\",&,V_titleLabel"
- "T@\"UILabel\",C,N,V_placeHolderLabel"
- "T@\"UINavigationController\",W,V_navigationController"
- "T@\"UINavigationController\",W,V_websheetRootViewController"
- "T@\"UIStackView\",&,V_stackView"
- "T@\"UISwitch\",R,N,V_switchControl"
- "T@\"UITableViewHeaderFooterView\",&,N,V_footer"
- "T@\"UITableViewHeaderFooterView\",&,V_footer"
- "T@\"UITextField\",&,N,V_editableTextField"
- "T@\"UITextField\",&,V_codeTextField"
- "T@\"UITextField\",&,V_otpEditor"
- "T@\"UITextView\",&,V_textView"
- "T@\"UIView\",&,V_cutoutView"
- "T@\"UIView\",&,V_scanView"
- "T@\"UIView\",&,V_snapshot"
- "T@\"UIView\",&,V_spinnerContainer"
- "T@\"UIViewController\",&,N,V_cachedIneligibleViewController"
- "T@\"UIViewController\",&,V_firstViewControllerInstance"
- "T@\"UIViewController\",W,V_dismissingViewController"
- "T@\"UIViewController\",W,V_presentedViewController"
- "T@\"UIViewController\",W,V_prevViewController"
- "T@\"UIViewController<PRXCardContentProviding>\",&,V_secureIntentProxCard"
- "T@\"UIViewController<TSSetupFlowItem>\",&,V_firstViewController"
- "T@\"UIViewController<TSSetupFlowItem>\",W,V_nextViewController"
- "T@\"UIViewController<TSSetupFlowItem>\",W,V_topViewController"
- "T@,&,V_transferBackOldItem"
- "T@,&,V_transferBackPlan"
- "T@?,C,N,V_eventHandler"
- "T@?,C,V_firstViewControllerCallback"
- "T@?,C,V_requestCompletion"
- "TB"
- "TB,N,V_areTransferPlansReady"
- "TB,N,V_isActivationPolicyMismatch"
- "TB,N,V_isD2dDone"
- "TB,N,V_isDualeSIMCapablityLoss"
- "TB,N,V_isExternalizedContextSent"
- "TB,N,V_isFlexPolicyOn"
- "TB,N,V_isProcessCanceled"
- "TB,N,V_isProximityFlow"
- "TB,N,V_isRemotePlan"
- "TB,N,V_isStandaloneProximityTransfer"
- "TB,N,V_isTransferNotSupportedFromiPhone"
- "TB,N,V_needOfferProximityTransferOption"
- "TB,N,V_needOfferQRCodeOption"
- "TB,N,V_showTransferredPane"
- "TB,R"
- "TB,R,N,GisAnimating"
- "TB,R,N,V_canUseCamera"
- "TB,R,V_allPlansInstallComplete"
- "TB,R,V_confirmationCodeRequired"
- "TB,R,V_isContinueByUser"
- "TB,R,V_transferViaQRCode"
- "TB,R,V_useLiveID"
- "TB,V_allPlansActivated"
- "TB,V_allowDismiss"
- "TB,V_animating"
- "TB,V_areAllPlansTransferedOut"
- "TB,V_confirmCellularPlanTransfer"
- "TB,V_confirmationCodeRequired"
- "TB,V_crossPlatformTransferPlanSelected"
- "TB,V_dctPrewarmSucceded"
- "TB,V_didProcessDCTCode"
- "TB,V_didUserClickContinue"
- "TB,V_eSIMInstallFromWebsheetFlowStarted"
- "TB,V_followDirections"
- "TB,V_forceDualSIMSetup"
- "TB,V_hasBackButton"
- "TB,V_hasContinueButton"
- "TB,V_hasDoneButton"
- "TB,V_hasProvisioningServiceImpact"
- "TB,V_hasTransferablePlan"
- "TB,V_hidesBackButton"
- "TB,V_inBuddy"
- "TB,V_installingTransferPlan"
- "TB,V_isAuthenticationCompleted"
- "TB,V_isAvailableOptionsQueryCompleted"
- "TB,V_isCancelButtonTapped"
- "TB,V_isCancelTapped"
- "TB,V_isCarrierDirectAuthItemSelected"
- "TB,V_isCarrierSetupItemSelected"
- "TB,V_isCrossPlatformButtonTapped"
- "TB,V_isDataOnly"
- "TB,V_isDataOnlySelected"
- "TB,V_isDeviceIdentifierPresent"
- "TB,V_isDisabled"
- "TB,V_isDisembarkUIRequired"
- "TB,V_isDtoEvaluationRequired"
- "TB,V_isDtoEvaluationSucceeded"
- "TB,V_isDualSIMConfig"
- "TB,V_isEOnly"
- "TB,V_isEnterManuallyTapped"
- "TB,V_isExistingPlanTapped"
- "TB,V_isFlexPolicyOn"
- "TB,V_isFlowCompleted"
- "TB,V_isFlowFinished"
- "TB,V_isForCrossPlatformTransfer"
- "TB,V_isFromDataTransferSession"
- "TB,V_isHiding"
- "TB,V_isIdleTimerDisabled"
- "TB,V_isLocalConvert"
- "TB,V_isLocalConvertFlow"
- "TB,V_isNFCDataSuccessTransfer"
- "TB,V_isOfferFallbackFlow"
- "TB,V_isOtherButtonTapped"
- "TB,V_isPhysical"
- "TB,V_isPostMigrationFlow"
- "TB,V_isPreInstalled"
- "TB,V_isPreSharedKeyPresent"
- "TB,V_isPreinstallingViewControllerActive"
- "TB,V_isProxFlowShown"
- "TB,V_isProximityTransferButtonTapped"
- "TB,V_isPurchaseLocalPlanTapped"
- "TB,V_isRemotePeerClosed"
- "TB,V_isResumingAfterPause"
- "TB,V_isRoamingTapped"
- "TB,V_isSIMTypeSelectionShown"
- "TB,V_isScanButtonTapped"
- "TB,V_isSecureIntentRejected"
- "TB,V_isSecureIntentRequired"
- "TB,V_isSecureIntentSucceeded"
- "TB,V_isSelectedAsTravelSIM"
- "TB,V_isShown"
- "TB,V_isSkipButtonTapped"
- "TB,V_isSource"
- "TB,V_isSourceProxCardVisible"
- "TB,V_isStandaloneProximityFlow"
- "TB,V_isStandaloneProximityTransfer"
- "TB,V_isStartOverNeeded"
- "TB,V_isSyncWithTargetResults"
- "TB,V_isTransferButtonTapped"
- "TB,V_isTransferCompleted"
- "TB,V_isTransferListCellTapped"
- "TB,V_isTravelEduButtonTapped"
- "TB,V_isUserInHomeCountry"
- "TB,V_isUsingPreSharedKey"
- "TB,V_isViewControllerPresented"
- "TB,V_isViewControllerPresenting"
- "TB,V_maybeShowConfirmationCodePane"
- "TB,V_needShow"
- "TB,V_needShowTransferIntroPane"
- "TB,V_oneTimePasscodePaneShown"
- "TB,V_otpDetectorNeeded"
- "TB,V_prevTravelOnlySelection"
- "TB,V_requireDelayBluetoothConnection"
- "TB,V_requireSetup"
- "TB,V_returnHome"
- "TB,V_showCrossTransferOption"
- "TB,V_showDupLabelsFooter"
- "TB,V_showQRCodeOption"
- "TB,V_showSIMSetup"
- "TB,V_showTransferOption"
- "TB,V_showTravelEduOption"
- "TB,V_skip"
- "TB,V_skipActivatingPane"
- "TB,V_supportsSyncTransferResults"
- "TB,V_tappedLearnMore"
- "TB,V_termsAndConditionsShown"
- "TB,V_transferablePlanOnSource"
- "TB,V_travelOnlySelected"
- "TB,V_useGMVNOAsTravelSIM"
- "TB,V_useLiveID"
- "TB,V_usePin"
- "TB,V_useTravelOnly"
- "TB,V_usingFirstViewControllerParadigm"
- "TB,V_withBackButton"
- "TC,V_remoteDeviceClass"
- "TQ,N,V_limit"
- "TQ,N,V_userConsentResponse"
- "TQ,R"
- "TQ,R,N,V_consentType"
- "TQ,R,N,V_usesType"
- "TQ,V_NFCTransferStatus"
- "TQ,V_backgroundTask"
- "TQ,V_endpoint"
- "TQ,V_entryPoint"
- "TQ,V_flowType"
- "TQ,V_nonMagnoliaCount"
- "TQ,V_planEnablementState"
- "TQ,V_planSetupType"
- "TQ,V_proximitySetupState"
- "TQ,V_selectedPlanTransferStatus"
- "TQ,V_status"
- "TQ,V_subFlowType"
- "TQ,V_userConsentType"
- "TRANSFER_WEBSHEET_LOADING_MESSAGE_%@"
- "TSActivationFlowWithSimSetupFlow"
- "TSActivationPolicyMismatchFlow"
- "TSAddCellularPlanViewController"
- "TSAuthFlow"
- "TSBootstrapCrossPlatformTransferFlow"
- "TSBuddyMLController"
- "TSBuddyMLViewController"
- "TSCarrierItemListViewController"
- "TSCarrierSignupFlow"
- "TSCellularPlanActivatingFlow"
- "TSCellularPlanIntroViewController"
- "TSCellularPlanItemCell"
- "TSCellularPlanLabelTableViewCell"
- "TSCellularPlanLabelsViewController"
- "TSCellularPlanManagerCache"
- "TSCellularPlanManagerCacheDelegate"
- "TSCellularPlanProximityTransferController"
- "TSCellularPlanQRCodeScannerView"
- "TSCellularPlanRemapTableViewCell"
- "TSCellularPlanRemapViewController"
- "TSCellularPlanTableViewCell"
- "TSCellularPlanUserConsentViewController"
- "TSCellularPlanUsesDataSwitchCell"
- "TSCellularPlanUsesTableViewCell"
- "TSCellularPlanUsesViewController"
- "TSCellularSetupActivatingViewController"
- "TSCellularSetupCompleteViewController"
- "TSCellularSetupLoadingView"
- "TSCellularSetupLoadingViewController"
- "TSCellularSetupTimeoutFailureViewController"
- "TSCoreTelephonyClientCache"
- "TSCrossPlatformSourceAuthFlow"
- "TSCrossPlatformSourceTransferFlow"
- "TSCrossPlatformTargetAuthFlow"
- "TSCrossPlatformTargetTransferFlow"
- "TSDeviceInfoCell"
- "TSDeviceInfoViewController"
- "TSEnableTableViewController"
- "TSEntitlementJSHandlerDelegate"
- "TSFlowHelper"
- "TSIDSSimTransferringViewController"
- "TSIDSSubscriptionSelector"
- "TSIDSTransferFlow"
- "TSIdentityShareFlow"
- "TSLowDataModeConfigViewController"
- "TSManagedDeviceInstallFlow"
- "TSMidOperationFailureViewController"
- "TSMultiPlanIntermediateViewController"
- "TSNavigationBarSpinnerManager"
- "TSNoPlanForTransferViewController"
- "TSOBTableWelcomeController"
- "TSOBWelcomeController"
- "TSOnDeviceConversionFlow"
- "TSPRXDeviceUnlockViewController"
- "TSPRXIdentityShareViewController"
- "TSPRXPasscodeEntryViewController"
- "TSPRXReconnectWaitingViewController"
- "TSPRXSIMTransferCompleteViewController"
- "TSPRXSIMTransferringViewController"
- "TSPRXStartViewController"
- "TSPostMigrationFlow"
- "TSProximityPINCodeViewController"
- "TSProximitySourceTransferFlow"
- "TSProximityTargetTransferFlow"
- "TSProximityWaitingViewController"
- "TSQRCodeScanFlow"
- "TSRecommendedCarrierAppsFlow"
- "TSRemotePlanSignUpFlow"
- "TSRemotePlanWebsheetContext"
- "TSRemoteUIStyle"
- "TSRoamingEducationViewController"
- "TSSIMSetupDelegate"
- "TSSIMSetupFlow"
- "TSSIMSetupFlowDelegate"
- "TSSIMSetupPublicApiInstallFlow"
- "TSSecureIntentGestureViewController"
- "TSSetupAssistantSIMSetupFlow"
- "TSSetupFlowItem"
- "TSSinglePlanTransferViewController"
- "TSSourceAutoReconnectTransferFlow"
- "TSSourceAutoReconnectTransferredViewController"
- "TSSourceAutoReconnectWaitingViewController"
- "TSSpinnerNavigationBarItem"
- "TSSubFlowViewController"
- "TSTargetReconnectWaitingViewController"
- "TSTermsAndConditionsViewController"
- "TSTransferCloudFlow"
- "TSTransferCloudFlowModel"
- "TSTransferFlow"
- "TSTransferFlowModel"
- "TSTransferListViewController"
- "TSTransferOneTimeCodeViewController"
- "TSTransferQRCodeFlow"
- "TSTransferQRCodeViewController"
- "TSTransferredViewController"
- "TSTravelBuddyViewController"
- "TSTravelEducationExistingPlanViewController"
- "TSTravelEducationFlow"
- "TSTravelEducationIntroViewController"
- "TSTravelEducationRoamingViewController"
- "TSTravelModeFlow"
- "TSTravelModeIntroViewController"
- "TSTravelSimCapabilitySelectionViewController"
- "TSTravelSimTypeSelectionViewController"
- "TSURLRequestFactory"
- "TSUserConsentViewController"
- "TSUserInPurchaseFlowAssertion"
- "TSUserResponseFlow"
- "TSUtilities"
- "TSWebsheetSignupFlow"
- "TSWebsheetViewController"
- "Td,V_installationEndTime"
- "Td,V_installationStartTime"
- "Td,V_waitingStartTime"
- "This should only take a few seconds to complete."
- "Ti,V_flowType"
- "Ti,V_numSelectedPlansNotTransferredOut"
- "Ti,V_passcodeType"
- "Ti,V_selectedPlansCount"
- "Ti,V_selectedPlansFailedTransferCount"
- "Ti,V_selectedTransferPlansCount"
- "Tq,N,V_dismissCause"
- "Tq,V_backToSelfOption"
- "Tq,V_signupUserConsentResponse"
- "Tq,V_timeoutReason"
- "Tq,V_transferState"
- "Transferrable plan %@ will be removed from the list @%s"
- "UIAdaptivePresentationControllerDelegate"
- "UIKitExtras"
- "UINavigationControllerDelegate"
- "UIScrollViewDelegate"
- "UITableViewCell"
- "UITableViewDataSource"
- "UITableViewDelegate"
- "UITextFieldDelegate"
- "URL"
- "URLByAppendingPathComponent:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "UpdatePlanInfo"
- "Using bootstrap: %d, on wifi:%d @%s"
- "ViewControllerBackOption"
- "ViewLifeCycle"
- "Vv16@0:8"
- "WKNavigationDelegate"
- "WKScriptMessageHandler"
- "WKUIDelegate"
- "Websheet transferrable plan exists with same carrier name [%@] %@ @%s"
- "[Db] no eligible plan to transfer in buddy @%s"
- "[Db] visit store plan : %@ @%s"
- "[E]invalid carrier for plan : %@ @%s"
- "[F]delegate not conforms to protocol : %@ @%s"
- "[I] app in background, deassert bootstrap @%s"
- "[I] app in foreground, assert bootstrap @%s"
- "^{_NSZone=}16@0:8"
- "_LearnMoreButton"
- "_LearnMoreButtonTapped"
- "_NFCTransferStatus"
- "_WKInputDelegate"
- "_acceptButton"
- "_acceptButtonTapped"
- "_acceptClicked:"
- "_action"
- "_activatingTimer"
- "_activeTextField"
- "_activityIndicator"
- "_addNewPlanWithCardData:confirmationCode:"
- "_alertConsentWithCompletion:"
- "_allPlans"
- "_allPlansActivated"
- "_allPlansInstallComplete"
- "_allowDismiss"
- "_allowMultiPlanSelection"
- "_animating"
- "_areAllInstallingPlansBeEnabled"
- "_areAllPlansInPostInstallOrTerminalState"
- "_areAllPlansInTerminalState"
- "_areAllPlansTransferedOut"
- "_areTransferPlansReady"
- "_assert"
- "_assertNFC"
- "_assertionCounter"
- "_associatedPlanItem"
- "_autoFillController"
- "_backFromNextPane"
- "_backOptions"
- "_backToSelfOption"
- "_backgroundTask"
- "_badge"
- "_beginAdvertising:"
- "_bluetoothChecker"
- "_bootstrapPlanTransfer"
- "_bootstrapTransfer"
- "_bottomConstraint"
- "_btClient"
- "_btDevice"
- "_btServer"
- "_buddyMLController"
- "_buddyMLURL"
- "_buddyMLViewController"
- "_button"
- "_buttonAction"
- "_buttons"
- "_cacheLockupsWithCollectionRequest:withCompletionBlock:"
- "_cachedButtons"
- "_cachedIneligibleViewController"
- "_cachedPlanItems"
- "_calculatePlanSelection"
- "_callbackDelegate"
- "_canShowWhileLocked"
- "_canUseCamera"
- "_cancelAction"
- "_cancelButton"
- "_cancelButtonTapped"
- "_cancelButtonTapped:"
- "_cancelTransfer:"
- "_cancelTransferringPlan"
- "_cancelTransferringPlan:"
- "_cancelledDeviceIDs"
- "_captureSession"
- "_carrier"
- "_carrierApps"
- "_carrierErrorCode"
- "_carrierItems"
- "_carrierName"
- "_carrierNameForSelectedItem"
- "_carrierSetupItems"
- "_carrierSetupPlan"
- "_carrierSetupPostData"
- "_carrierSetupUrl"
- "_carrierURL"
- "_centerActivityIndicatorInButton"
- "_changeCameraConfiguration"
- "_changeOtpTextFieldState:"
- "_chosenLabelIndexPath"
- "_chosenTargetCellularPlanItem"
- "_chosenUseIndexPath"
- "_chosenUseIndexPaths"
- "_client"
- "_code"
- "_codeTextField"
- "_collectAllPhoneNumbersForDevice:"
- "_completion"
- "_configureNavigationItem"
- "_configureRUIController"
- "_confirmCellularPlanTransfer"
- "_confirmTextView"
- "_confirmationCode"
- "_confirmationCodeRequired"
- "_confirmationCodeViewController"
- "_connectToDevice:completion:"
- "_consentType"
- "_constructDCTUrl:withPasscode:"
- "_containsButton:"
- "_containsSSOBBoldTrayButton"
- "_continueAction"
- "_continueButton"
- "_continueButtonTapped"
- "_continueButtonTapped:"
- "_continueButtonTappedOnce"
- "_coreTelephonyClient"
- "_createFirstViewController"
- "_createFirstViewController:"
- "_createIntroViewController:showQrCodeOption:"
- "_createIntroViewControllerWithIneligiblePlans:"
- "_createPKGlyphView"
- "_createTargetProxFlowVC"
- "_createTransferCloudFlowVC"
- "_createTransferFlowVC"
- "_createTransferSubFlowVcWithSession:isPostmigrationFlow:"
- "_createURLRequest:"
- "_crossPlatformTransferItems"
- "_crossPlatformTransferPlan"
- "_crossPlatformTransferPlanSelected"
- "_crossTransferIcon"
- "_ctClient"
- "_currentItemsForIMessage"
- "_currentLanguageIsRTL"
- "_currentTitle"
- "_customLabel"
- "_cutoutView"
- "_danglingPlanItem"
- "_danglingPlanItems"
- "_dataSubCarrierName"
- "_dataSwitchEnabled"
- "_dctDelegate"
- "_dctInfo"
- "_dctPrewarmSucceded"
- "_deassert"
- "_deassertNFC"
- "_declineButton"
- "_declineButtonTapped"
- "_decodeBase64EncodedString:"
- "_decodeTransferStatus:"
- "_defaultDataContext"
- "_defaultVoiceIccid"
- "_defaultVoiceItem"
- "_delegate"
- "_dequeueInteractiveUI"
- "_descriptionLabel"
- "_descriptors"
- "_detailFont"
- "_detailText"
- "_details"
- "_deviceInput"
- "_deviceName"
- "_didFinishDocumentLoad"
- "_didFirstLayout"
- "_didInstallationFail"
- "_didProcessDCTCode"
- "_didReceivePurchaseCallback"
- "_didReceiveResponse"
- "_didUserClickContinue"
- "_didViewAppear"
- "_disableMismatchedPlan"
- "_dismissCause"
- "_dismissDueToLoadFailure"
- "_dismissSelf"
- "_dismissViewController"
- "_dismissingViewController"
- "_displayCarrierSetupViewController:"
- "_displayConfirmationCodeViewController:"
- "_displayIntermediateViewController:"
- "_displayOneTimeCodeViewController:phoneNumber:carrierName:usePin:"
- "_displayPlan"
- "_displayTermsAndConditionsViewController:mainText:"
- "_displayUserConsentAlert:"
- "_displayWebsheetViewController:"
- "_displayedDeviceIDs"
- "_doneAction"
- "_doneButton"
- "_doneButtonTapped"
- "_doubleClickGesture"
- "_dummyArtwork"
- "_dummyLockup"
- "_eSIMInstallFromWebsheetFlowStarted"
- "_eSIMTravelState"
- "_editableTextField"
- "_enablingIccid"
- "_endAdvertising"
- "_endPinningInputViews"
- "_endpoint"
- "_enqueueInteractiveUI:"
- "_enterDetailsManuallyButton"
- "_entryPoint"
- "_errorHeaderDetail"
- "_eventHandler"
- "_externalizedContext"
- "_failIdentityShare"
- "_failureWebsheetError"
- "_fallbackToActivationCode"
- "_fauxCardData"
- "_fetchCarrierListWithCompletion:"
- "_filterCarrierSetupItems:"
- "_findEligiblePlans:"
- "_findPPRItem:"
- "_findPlanInfoWithPlanID:"
- "_findPlanInfoWithPlanStatus:"
- "_findPlanInfoWithTargetIccid:"
- "_findPlanInfoWithTargetIccidHash:"
- "_firstLabel"
- "_firstViewCompletion"
- "_firstViewController"
- "_firstViewController:"
- "_firstViewControllerCallback"
- "_firstViewControllerInstance"
- "_flatImageWithColor:"
- "_flowType"
- "_flowWithOptions:"
- "_followDirections"
- "_footer"
- "_forceDualSIMSetup"
- "_formatedDescriptor"
- "_fromDataTransferSession"
- "_getCarrierNameForDefaultDataSub"
- "_getCellularPlanItemForTravelSIM"
- "_getCurrentDeviceOrientation"
- "_getDetailsTextWithIccid:"
- "_getPlanItemsToLimitService:"
- "_getSFSafariViewControllerWithURL:"
- "_getSubTextForSection:"
- "_getSubTextToDisplay:carrierName:"
- "_getSubtitleWhenSyncWithTarget:selectedPlansCount:selectedPlansFailedTransferCount:"
- "_getTitleWhenSyncWithTarget:selectedPlansCount:selectedPlansFailedTransferCount:"
- "_getTraveleSIMStateWithCompletion:"
- "_getTrialPlanDate:"
- "_getTrialPlanTypeAndDateOfInstallingIccid:"
- "_getValidatedPlanItemFor:"
- "_getValueFromCountryBunbleByKey:"
- "_getWebsheetInfo:completion:"
- "_gid1"
- "_gid2"
- "_glyphView"
- "_handleActivatedItemUpdate:"
- "_handleActivatingExpiry"
- "_handleCarrierInfoWithUrl:postdata:type:error:"
- "_handleKeyboardPresentation:"
- "_handleLockState:"
- "_handleMultiSIMInstallationStatusUpdateEvent:"
- "_handleNotificationESIMInstallStateChanged:"
- "_handleOtpStatusUpdate:"
- "_handlePINCodeUpdate:"
- "_handlePlanAddition:"
- "_handlePlanPurchaseWithMessageBody:"
- "_handlePostInstallItemUpdate:"
- "_handleProvisioningItemUpdate:"
- "_handleRuntimeError:"
- "_handleSKEvent:"
- "_handleTransferResults:"
- "_handleTransferUICapability:"
- "_handleTransferWithMessageBody:"
- "_handleUserCancelNotification:"
- "_hasAnyDisabledInstallPlan"
- "_hasAnyPlanSuccessfullyInstalled"
- "_hasAnyPlanSuccessfullyInstalledOrPostInstalled"
- "_hasBackButton"
- "_hasCarrierSetupItemsQueried"
- "_hasContinueButton"
- "_hasDoneButton"
- "_hasPendingInstallPlansQueried"
- "_hasProvisioningServiceImpact"
- "_hasProvisioningServiceImpactMap"
- "_hasTransferablePlan"
- "_heightAnchor"
- "_heightAnchorConstant"
- "_heightConstraint"
- "_hide"
- "_hideButtonTraySpinner"
- "_hideKeyboard"
- "_hideLoading"
- "_hidesBackButton"
- "_holeOutlineLayer"
- "_homeIccid"
- "_homeIccidCarrierName"
- "_homeIccidPhoneNumber"
- "_homeIccidPlanItem"
- "_hostViewController"
- "_iccid"
- "_iccidToEnable"
- "_idNeedsEncryption"
- "_ignoreTransport"
- "_imgView"
- "_inBuddy"
- "_inPrivateNetworkMode"
- "_indicatorView"
- "_infos"
- "_initWithConfiguration:"
- "_initialLabel"
- "_initialRequest"
- "_initializePlanItems"
- "_installBucketSubtitle"
- "_installBucketTitle"
- "_installError"
- "_installInfos"
- "_installMultipleSelectedPlans"
- "_installName"
- "_installPlans"
- "_installSelectedPlans"
- "_installStateChanged:"
- "_installationEndTime"
- "_installationStartTime"
- "_installingALSPlan"
- "_installingIccid"
- "_installingPlanInfos"
- "_installingTransferPlan"
- "_isActionDismissToCancelFlow:"
- "_isActivationPolicyMismatch"
- "_isAnyPlanRequireLocationService"
- "_isAnyPlanWithMismatchedActivationPolicy"
- "_isAnyRequireStoreVisitPlan:"
- "_isAnySourceNeedsSoftwareUpdatePlan:"
- "_isAnyTransferPlanWithDirectAuth"
- "_isAppInBackground"
- "_isAuthenticationCompleted"
- "_isAvailableOptionsQueryCompleted"
- "_isBootstrapAsserted"
- "_isBootstrapComplete"
- "_isBootstrapTriggerred"
- "_isCancelButtonTapped"
- "_isCancelTapped"
- "_isCarrierDirectAuthItemSelected"
- "_isCarrierSetupItemSelected"
- "_isCarrierSetupItemSelected:"
- "_isCloudTransfer"
- "_isContinueByUser"
- "_isCrossPlatformButtonTapped"
- "_isD2dDone"
- "_isDataOnly"
- "_isDataOnlySelected"
- "_isDeviceIdentifierPresent"
- "_isDisabled"
- "_isDisembarkUIRequired"
- "_isDtoEvaluationRequired"
- "_isDtoEvaluationSucceeded"
- "_isDualSIMConfig"
- "_isDualeSIMCapabilityLoss"
- "_isDualeSIMCapablityLoss"
- "_isEOnly"
- "_isEmbeddedInResultView"
- "_isEnterManuallyTapped"
- "_isExistingPlanTapped"
- "_isExternalizedContextSent"
- "_isFlexPolicyOn"
- "_isFlowCompleted"
- "_isFlowFinished"
- "_isFollowUpInstall"
- "_isForCrossPlatform"
- "_isForCrossPlatformTransfer"
- "_isFromDataTransferSession"
- "_isHexadecimalString:"
- "_isHiding"
- "_isHomeSIMOnPhySlot"
- "_isIdleTimerDisabled"
- "_isLocalConvert"
- "_isLocalConvertFlow"
- "_isMidOperation"
- "_isNFCDataSuccessTransfer"
- "_isOfferFallbackFlow"
- "_isOtherButtonTapped"
- "_isPhysical"
- "_isPlanRegisteredForIMessage:"
- "_isPlanSelected:selectedItems:"
- "_isPostMigrationFlow"
- "_isPreInstalled"
- "_isPreSharedKeyPresent"
- "_isPreinstallingViewControllerActive"
- "_isProcessCanceled"
- "_isProfilePendingRelease:"
- "_isProxFlowShown"
- "_isProximityFlow"
- "_isProximityTransferButtonTapped"
- "_isPurchaseLocalPlanTapped"
- "_isQueriableFirstViewController"
- "_isRemotePeerClosed"
- "_isRemotePlan"
- "_isResumingAfterPause"
- "_isRoamingTapped"
- "_isSIMOnPhySlot"
- "_isSIMTypeSelectionShown"
- "_isScanButtonTapped"
- "_isSecureForRemoteViewService"
- "_isSecureIntentRejected"
- "_isSecureIntentRequired"
- "_isSecureIntentSucceeded"
- "_isSelectedAsTravelSIM"
- "_isSharingIdentitySupported"
- "_isShowingFilteredPlans"
- "_isShown"
- "_isSinglePhysicalSIMTransfer"
- "_isSkipButtonTapped"
- "_isSource"
- "_isSourceProxCardVisible"
- "_isSourceSideError"
- "_isSourceThirdParty"
- "_isStandaloneProximityFlow"
- "_isStandaloneProximityTransfer"
- "_isStandaloneQRCodeView"
- "_isStartOverNeeded"
- "_isSubTextSelected"
- "_isSubscriptionReadyForTravel4FF:"
- "_isSyncWithTargetResults"
- "_isTransferButtonTapped"
- "_isTransferCapable"
- "_isTransferCompleted"
- "_isTransferListCellTapped"
- "_isTransferNotSupportedFromiPhone"
- "_isTravelEduButtonTapped"
- "_isTravelFlow"
- "_isTravelSIMDataOnly"
- "_isTravelSIMOnPhySlot"
- "_isTrialPlanExpiringInThreeDays:"
- "_isUserAbroad"
- "_isUserInHomeCountry"
- "_isUsingPreSharedKey"
- "_isViewControllerPresented"
- "_isViewControllerPresenting"
- "_jsonBodyWithPostdata:"
- "_keyboardSize"
- "_keyboardWillHide:"
- "_label"
- "_labelPickerViewController"
- "_labelToDetailPadding"
- "_lastError"
- "_laterButton"
- "_laterButtonTapped"
- "_laterButtonTapped:"
- "_launchDirectAuthFlow:"
- "_launchDisembarkUI:"
- "_leadingConstraint"
- "_learnMoreButtonTapped"
- "_learnMoreTapped"
- "_leftBarButtonItems"
- "_leftConstraint"
- "_limit"
- "_loadIcons"
- "_loadingView"
- "_locationServiceButtonAction"
- "_lockupView"
- "_mainText"
- "_manager"
- "_maps_constraintsEqualToEdgesOfView:insets:priority:"
- "_maxAllowedeSIMCount"
- "_maxIconHeight"
- "_maxIconWidth"
- "_maybeAutoInstallPendingPlan"
- "_maybeClearFirstViewControllerCallback"
- "_maybeClearSubFlow"
- "_maybeClearSubFlowViewController:"
- "_maybeDeleteTransferBackItem:"
- "_maybeDismissAlert:"
- "_maybeDismissSelf"
- "_maybeDisplayInteractiveUI:"
- "_maybeDisplayNextIntermediateViewController"
- "_maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:"
- "_maybeDisplaySourceDeviceConsentAlert:"
- "_maybeEnableDoneButton"
- "_maybeEnableOneTimeCodeCheck"
- "_maybeFlowCompleted:"
- "_maybeHandleConfirmationCodeError:"
- "_maybeHandleProvisioningError:items:"
- "_maybeLaunchURLForCarrierDirectAuth:"
- "_maybeMoveToNextItem"
- "_maybePresentFirstViewController:"
- "_maybePresentFirstViewController:firstViewControllerCallback:"
- "_maybeReplyFirstViewControllerCallbackWithViewController:"
- "_maybeSendExternalizedContext:isDTOEvaluationFailed:"
- "_maybeSendTransferResults"
- "_maybeSendTransferUICapability:"
- "_maybeSetNavigationController:"
- "_maybeShowConfirmationCodePane"
- "_maybeShowPreinstallConsentOnViewController:"
- "_maybeShowPreinstallConsentOnViewController:planItems:"
- "_maybeStartTimerForNewlyInstalledPlan:newStatus:"
- "_maybeSubmitAutoReconnectionDetails"
- "_maybeUpdateHomeIccid:homeIccid:"
- "_maybeUpdatePhysicalSIMStatus:"
- "_maybeUpdatePlanNameForTargetIccid:planName:"
- "_maybeUpdatePlanNameWithoutPlanID:"
- "_maybeUpdateTableView"
- "_maybeUpdateUserEnabledPlans:"
- "_mcc"
- "_messageSession"
- "_metadataQueue"
- "_mnc"
- "_model"
- "_name"
- "_navigationController"
- "_navigationItems"
- "_needAutoInstallPendingPlan"
- "_needCustomizeBackAction:"
- "_needOfferOtherOptions"
- "_needOfferProximityTransferOption"
- "_needOfferQRCodeOption"
- "_needShow"
- "_needShowTransferIntroPane"
- "_nextButton"
- "_nextTimeToAcceptScan"
- "_nextViewController"
- "_nfcAnimationView"
- "_nfcAssertion"
- "_nonMagnoliaCount"
- "_normalStateTitle"
- "_notifyFlowCompletion:"
- "_numNonRemotePlanItems"
- "_numSelectedPlansNotTransferredOut"
- "_objectModels"
- "_offerFallbackOption"
- "_onESIMInstallFromWebSheetFlowStart"
- "_onInstallError:"
- "_oneTimeCodeAccelerator"
- "_oneTimeCodeViewController"
- "_oneTimePasscodePaneShown"
- "_openRoamingSettings"
- "_options"
- "_originalEnabledPlans"
- "_otherButtonTapped"
- "_otherButtonTapped:"
- "_otherOptionsButton"
- "_otpDetectorNeeded"
- "_otpEditor"
- "_parentFlow"
- "_passcodeType"
- "_peerDeviceInfo"
- "_pendingInstallItems"
- "_pendingInstallPlan"
- "_pendingInstallPlans"
- "_pendingInteractiveViewControllers"
- "_phoneNumber"
- "_physicalButtonView"
- "_pin"
- "_pinCodeLabel"
- "_placeHolderLabel"
- "_plan"
- "_planEnablementState"
- "_planError"
- "_planInfo"
- "_planInstallError"
- "_planItem"
- "_planItemBadges"
- "_planItemError"
- "_planItems"
- "_planList"
- "_planName"
- "_planSetupType"
- "_planStatusDescriptions"
- "_planType"
- "_plans"
- "_popAllSIMSetupFlowViewControllers:"
- "_postArrivalInstallation"
- "_postdata"
- "_preWarmOngoing"
- "_predefinedUserLabels"
- "_prepareCellInformationWithPendingInstallPlans:transferPlans:carrierSetupPlans:isHiddenPlanSelectable:"
- "_prepareDisplayItems:withPlanItems:"
- "_prepareForEnablingItem:"
- "_prepareForInstallingItems:"
- "_prepareSpinner"
- "_preselectPlanIfNeeded"
- "_presentFirstViewController"
- "_presentedViewController"
- "_prevTravelOnlySelection"
- "_prevViewController"
- "_preventConnectionHandoverAssertion"
- "_previewLayer"
- "_previousLeftBarButtonItems"
- "_previousRightBarButtonItems"
- "_primaryAction"
- "_processPool"
- "_provisioningWatchDogTimer"
- "_proxCardFlowDidDismiss"
- "_proxPlansFiltered"
- "_proxTransferController"
- "_proximitySetupState"
- "_pushStartOverViewController:from:"
- "_qrIcon"
- "_qrcodeBucketSubtitle"
- "_qrcodeBucketTitle"
- "_qrcodeDelegate"
- "_queryGroup"
- "_queryParamToTitle"
- "_radioImageView"
- "_receivedPendingInstallItems"
- "_receivedTransferItems"
- "_redirectToBTFlow"
- "_reduceEducation"
- "_refreshTableView"
- "_registerLockState"
- "_reloadScreen"
- "_remoteDeviceClass"
- "_remoteInfo"
- "_remotePlanWebsheetContext"
- "_remoteUIController"
- "_remoteViewControllerProxy"
- "_request"
- "_requestCarrierAppsWithCompletion:"
- "_requestCarrierSetupsWithCompletion:"
- "_requestCipherText:completion:"
- "_requestCompletion"
- "_requestCrossPlatformTransferPlanListWithCompletion:"
- "_requestLoadedCompletion"
- "_requestPendingInstallItemsWithCompletion:"
- "_requestPlansWithCompletion:"
- "_requestTransferPlanListWithCompletion:"
- "_requestType"
- "_requireAdditionalConsent"
- "_requireDelayBluetoothConnection"
- "_requireGeneralConsent"
- "_requireSetup"
- "_requireStoreVisitItems"
- "_requireSyncUpTransferResultsWithSource"
- "_resendOTP"
- "_resendOTPButton"
- "_resetExtension:"
- "_retainedObject"
- "_retryAction"
- "_returnHome"
- "_rightConstraint"
- "_roamingInfo"
- "_saveSimsetupD2dInfo:"
- "_scanButton"
- "_scanButtonTapped:"
- "_scanView"
- "_scannedCode"
- "_scannerView"
- "_screenStateChanged"
- "_secondHomeIccidCarrierName"
- "_secondHomeIccidPhoneNumber"
- "_secondHomeIccidPlanItem"
- "_secondLabel"
- "_secondaryButtonDetail"
- "_secureIntentProxCard"
- "_selectedCarrierItem"
- "_selectedItems"
- "_selectedPlan"
- "_selectedPlanItems"
- "_selectedPlanTransferStatus"
- "_selectedPlans"
- "_selectedPlansCount"
- "_selectedPlansFailedTransferCount"
- "_selectedTransferPlan"
- "_selectedTransferPlansCount"
- "_sendSIMSetupReadyNotification"
- "_sendTravelEventMetricForPlan:useLDM:"
- "_sendTravelEventMetricForRoaming:"
- "_serviceImpact"
- "_session"
- "_setApplePayEnabled:"
- "_setCookieAcceptPolicy:completionHandler:"
- "_setEphemeral:"
- "_setInputDelegate:"
- "_setNavigationItem"
- "_setNavigationItems"
- "_setNonAppInitiated:"
- "_setShowingLinkPreview:"
- "_setShowingLinkPreviewWithMinimalUI:"
- "_setTravelIccidInfo:"
- "_setUpButtons"
- "_setUpLearnMoreLink"
- "_setUpTableView"
- "_setUseCustomBackButtonAction:"
- "_setUserInPurchaseFlow"
- "_setupActivityIndicator"
- "_setupClient:"
- "_setupLabels"
- "_setupLaterButtonTapped"
- "_setupLayoutConstraint"
- "_setupOneTimeCodeDetection"
- "_setupTableView"
- "_shareIdentityButton"
- "_shareIdentityTapped"
- "_shouldDisplayPhoneNumber:"
- "_shouldIgnoreWebviewError:"
- "_shouldOfferFallbackOptionOnError:"
- "_shouldShowTravelEducation"
- "_shouldWaitUntilPhoneNumberBeReady:completion:"
- "_show:"
- "_showAddPlan"
- "_showAlert:"
- "_showBackButton"
- "_showButtonTraySpinnerWithBusyText:"
- "_showCancelAlert:withMessage:"
- "_showCancelButton:"
- "_showCrossTransferOption"
- "_showDupLabelsFooter"
- "_showFailureAlert"
- "_showFailureAlert:completion:"
- "_showLoading"
- "_showOptions"
- "_showOtherOption"
- "_showOtherOptions"
- "_showPendingInstallItems"
- "_showQRCodeOption"
- "_showQrCodeOption"
- "_showSIMSetup"
- "_showSpinning"
- "_showTransferOption"
- "_showTransferredPane"
- "_showTravelEduOption"
- "_showTurnOnLocationServices"
- "_showVerifyingIndicator:"
- "_signUpViewController"
- "_signupConsentResponse"
- "_signupUserConsentResponse"
- "_simsetupD2dInfo"
- "_singleItemFlow"
- "_skip"
- "_skipActivatingPane"
- "_skipButton"
- "_skipButtonTapped"
- "_skipButtonTapped:"
- "_skipGeneralInstallConsent"
- "_skipIntroPaneForWebsheetFlow"
- "_skipUIDismissal"
- "_slotForPlanItem:"
- "_snapshot"
- "_sortedInfo"
- "_sortedPlanItemsWithPendingLabels"
- "_sourceIccid"
- "_sourceOSVersion"
- "_sourceOsVersion"
- "_speedBumper"
- "_spinner"
- "_spinnerContainer"
- "_stackView"
- "_startBackgroundTask"
- "_startClientFlow"
- "_startInstallMultiplePlans:transferPlans:andCarrierSetupItems:"
- "_startLocalPlanConversion"
- "_startMonitoringConnection"
- "_startNFCIdentityShare"
- "_startObserver"
- "_startOver:"
- "_startPendingInstall:"
- "_startPlanTransfer:"
- "_startPlanTransfer:withDeviceID:"
- "_startSystemMonitor"
- "_startedByFollowup"
- "_status"
- "_statusDescription:info:"
- "_stopBackgroundTask"
- "_stopNFCIdentityShare"
- "_stopScanning"
- "_stopSystemMonitor"
- "_stopTimerWithBackgroundTaskState:"
- "_storeVisitedMap"
- "_subFlow"
- "_subFlowType"
- "_subFlowVcWithReconnectionCredentials:"
- "_subFlowViewControllers"
- "_submitCellularPlanSetupDetails"
- "_subscriptionContext"
- "_successIdentityShare"
- "_supportsSyncTransferResults"
- "_switchControl"
- "_systemMonitor"
- "_tableHeightAnchor"
- "_tappedLearnMore"
- "_targetIccid"
- "_targetIccidHash"
- "_termsAndConditionsShown"
- "_termsAndConditionsViewController"
- "_text"
- "_textFieldDidBegin"
- "_textFieldDidChange"
- "_textFieldDidEnd"
- "_textView"
- "_timeoutReason"
- "_timer"
- "_timerFired"
- "_title"
- "_titleForItem:"
- "_titleLabel"
- "_topConstraint"
- "_topViewController"
- "_trailingConstraint"
- "_transferBackOldItem"
- "_transferBackPhoneNumber"
- "_transferBackPlan"
- "_transferBackPlanPhoneNumber"
- "_transferButtonTapped:"
- "_transferConsentOnSource"
- "_transferCredentials"
- "_transferESimInstallationStarted"
- "_transferIcon"
- "_transferIneligibleItems"
- "_transferIneligiblePlans"
- "_transferIneligibleViaCloudItems"
- "_transferItems"
- "_transferPlan"
- "_transferPlanDeviceID"
- "_transferPlans"
- "_transferState"
- "_transferViaQRCode"
- "_transferableHiddenInCloudFlowItems"
- "_transferablePlanOnSource"
- "_transferringWatchDogTimer"
- "_translateRequestType:"
- "_travelEduIcon"
- "_travelIccid"
- "_travelIccidInfo"
- "_travelIccidPlanItem"
- "_travelOnlySelected"
- "_travelSIM"
- "_triangleImageView"
- "_turnOnLocationServicesTapped"
- "_type"
- "_unlockAction"
- "_unlockScreen"
- "_unregisterLockState"
- "_updateAuthenticationStatus:isDTOEvaluationFailed:"
- "_updateBusyText:"
- "_updateButtonStatus"
- "_updateCachedPlanItems"
- "_updateCarrierErrorCode:withPlanID:"
- "_updateCurrentAction:"
- "_updateEnablePlanItems"
- "_updateInstallError:withPlanID:webUrl:postData:"
- "_updateInstallError:withTargetIccidHash:"
- "_updateLayoutConstraint"
- "_updateLocalCachedPlanItems:"
- "_updatePlanItem"
- "_updatePlanStatus:forPlanInfo:"
- "_updatePlanStatus:withPlanID:"
- "_updatePlanStatus:withTargetIccid:"
- "_updateSourceProxCardState:"
- "_updateTargetIccid:withPlanID:"
- "_updateTargetIccidWithoutPlanID:"
- "_updateTransferStatus:"
- "_updateTrayButtonText:"
- "_url"
- "_urlEncodedBodyWithCarrierPostRawData:"
- "_urlEncodedBodyWithPostdata:"
- "_useCustomBackButtonAction"
- "_useGMVNOAsTravelSIM"
- "_useLiveID"
- "_usePin"
- "_useTravelOnly"
- "_userConsentResponse"
- "_userConsentType"
- "_userDidTapCancel"
- "_userDisagreedTermsAndConditions"
- "_userEnabledPlanInfos"
- "_userSelectAsTravelSIM"
- "_usesType"
- "_usingFirstViewControllerParadigm"
- "_validCarrierName"
- "_values"
- "_viewController"
- "_viewDelegate"
- "_viewWillAppear"
- "_voiceIccid"
- "_waitForPhoneNumber"
- "_waitForService"
- "_waitingStartTime"
- "_webView"
- "_webView:accessoryViewCustomButtonTappedInFormInputSession:"
- "_webView:decidePolicyForFocusedElement:"
- "_webView:didStartInputSession:"
- "_webView:focusRequiresStrongPasswordAssistance:"
- "_webView:focusRequiresStrongPasswordAssistance:completionHandler:"
- "_webView:focusShouldStartInputSession:"
- "_webView:focusedElementContextViewForInputSession:"
- "_webView:focusedElementContextViewHeightForFittingSize:inputSession:"
- "_webView:insertTextSuggestion:inInputSession:"
- "_webView:navigationDidFinishDocumentLoad:"
- "_webView:renderingProgressDidChange:"
- "_webView:shouldRevealFocusOverlayForInputSession:"
- "_webView:willStartInputSession:"
- "_webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:requestURL:method:submissionHandler:"
- "_webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:"
- "_webView:willSubmitFormValues:userObject:submissionHandler:"
- "_webViewAdditionalContextForStrongPasswordAssistance:"
- "_webViewConfigurationWithProcessPool:"
- "_web_errorIsInDomain:"
- "_websheetFlow"
- "_websheetOptions"
- "_websheetRootViewController"
- "_websheetURL"
- "_websheetUrl"
- "_withBackButton"
- "_wkUserContentController"
- "aa_primaryAppleAccount"
- "absoluteString"
- "acceptButton"
- "accessoryButton"
- "accessoryType"
- "accessoryViewForStatus:"
- "accountCancelled"
- "accountPendingRelease"
- "accounts"
- "action"
- "actionWithTitle:style:handler:"
- "activate"
- "activateConstraints:"
- "activateCrossPlatformTransport:completion:"
- "activateProximityTransfer:completion:"
- "activateUsingPreSharedKey:completion:"
- "activateWithCompletion:"
- "activatingState"
- "activatingTimer"
- "activeIMessageSlots"
- "activeSubscriptionsDidChange"
- "activityIndicator"
- "adaptivePresentationStyleForPresentationController:"
- "adaptivePresentationStyleForPresentationController:traitCollection:"
- "addAccessoryButton:"
- "addAction:"
- "addArcWithCenter:radius:startAngle:endAngle:clockwise:"
- "addArrangedSubview:"
- "addAttribute:value:range:"
- "addButton:"
- "addConstraint:"
- "addConstraints:"
- "addDetailLabel:withErrorCodeSubstr:"
- "addDetailLabel:withPhoneNumber:"
- "addGestureRecognizer:"
- "addInput:"
- "addLineToPoint:"
- "addNewPlanWithAddress:matchingId:confirmationCode:userConsent:completion:"
- "addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:"
- "addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:"
- "addNewPlanWithCardData:confirmationCode:userConsentResponse:completion:"
- "addNewPlanWithUserInfo"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:"
- "addObserver:selector:name:object:"
- "addOutput:"
- "addPlanWith:completionHandler:"
- "addScriptMessageHandler:name:"
- "addSubFlowViewController:"
- "addSublayer:"
- "addSubview:"
- "addSymbolEffect:"
- "addTarget:action:forControlEvents:"
- "addUserScript:"
- "alertControllerWithTitle:message:preferredStyle:"
- "alignmentRectInsets"
- "allButtons"
- "allConstraints"
- "allHTTPHeaderFields"
- "allKeys"
- "allObjects"
- "allPages"
- "allPlans"
- "allPlansActivated"
- "allPlansInstallComplete"
- "allPlansRequireSoftwareUpdate:"
- "allowDismiss"
- "alsPlanCarriers:"
- "animateAlongsideTransition:completion:"
- "animateWithDuration:animations:completion:"
- "animating"
- "appBackgrounded"
- "appForegrounded"
- "appendBytes:length:"
- "appendFormat:"
- "appendLeftToRightMark:"
- "appendString:"
- "applicationState"
- "applyToObjectModel:"
- "areAllPlansTransferedOut"
- "areAnyPlansOnDevice"
- "arePlansAvailable:"
- "arePlansAvailable:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:"
- "arePlansRequested"
- "areTransferPlansReady"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "assertUserInPurchaseFlowStartOver:caller:"
- "associatedPlanItem"
- "attemptFailed"
- "attributedText"
- "attributes"
- "autoFill"
- "autorelease"
- "backButtonClicked:"
- "backOption"
- "backOptions"
- "backToCurrentTopPane"
- "backToSelfOption"
- "backgroundColorForRemotePlan:"
- "backgroundTask"
- "badge"
- "badgeForText:"
- "becomeFirstResponder"
- "begin"
- "beginBackgroundTaskWithExpirationHandler:"
- "beginConfiguration"
- "bezierPath"
- "blackColor"
- "body"
- "boldButton"
- "boldSystemFontOfSize:"
- "boolValue"
- "bootstrap:isUsingPreSharedKey:completion:"
- "bootstrapPlanTransferForEndpoint:flowType:usingMessageSession:completion:"
- "bootstrapPlanTransferUsingMessageSession:flowType:completion:"
- "bottomAnchor"
- "bottomConstraint"
- "bottomPadding"
- "bounds"
- "bringSubviewToFront:"
- "btClient"
- "btDevice"
- "btServer"
- "buddyMLURL"
- "buddyMLViewController"
- "builtInPlugInsURL"
- "bundleForClass:"
- "buttonTray"
- "buttonWithType:"
- "buttons"
- "bytes"
- "cachedButtons"
- "cachedIneligibleViewController"
- "cachedPhoneNumber"
- "cachedPlanItems"
- "calculateInstallConsentTextTypeFor:"
- "calculateTitleAndDetailsWithName:consentType:title:details:"
- "calculateTitleAndDetailsWithName:consentType:trialPlanType:trialExpirationDate:title:details:hasProvisioningServiceImpact:"
- "callbackDelegate"
- "canBeShownFromSuspendedState"
- "canOpenURL:"
- "canSetSessionPreset:"
- "canUseCamera"
- "cancelAction"
- "cancelButton"
- "cancelButtonTapped"
- "cancelCellularPlanTransfer:fromDevice:completionHandler:"
- "cancelFlow"
- "cancelNextPane"
- "cancelPlanInstallation:completion:"
- "cancelTransferPlan:fromDevice:completionHandler:"
- "cancelledDeviceIDs"
- "capitalizedString"
- "captureOutput:didOutputMetadataObjects:fromConnection:"
- "carrierErrorCode"
- "carrierItems"
- "carrierItemsShouldUpdate:completion:"
- "carrierName"
- "carrierNameForSelectedItem"
- "carrierNames"
- "carrierSetupItems"
- "carrierSetupPlan"
- "carrierURL"
- "caseInsensitiveCompare:"
- "cellForRowAtIndexPath:"
- "centerXAnchor"
- "centerYAnchor"
- "centralManager:connectionEventDidOccur:forPeripheral:"
- "centralManager:didConnectPeripheral:"
- "centralManager:didDisconnectPeripheral:error:"
- "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
- "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
- "centralManager:didFailToConnectPeripheral:error:"
- "centralManager:didUpdateANCSAuthorizationForPeripheral:"
- "centralManager:willRestoreState:"
- "centralManagerDidUpdateState:"
- "characterDirectionForLanguage:"
- "characterSetWithCharactersInString:"
- "chosenLabel"
- "chosenLabelIndexPath"
- "chosenTargetCellularPlanItem"
- "chosenUseIndexPath"
- "chosenUseIndexPaths"
- "class"
- "clearCache"
- "clearCarrierSetupItemsCache"
- "clearColor"
- "client"
- "clientInfo"
- "code"
- "codeDidChange"
- "codeTextField"
- "colorWithWhite:alpha:"
- "commit"
- "commitConfiguration"
- "compare:"
- "compareProductVersion:toProductVersion:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "componentsSeparatedByString:"
- "componentsWithString:"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "concatenateDescriptors:"
- "configurationWithPointSize:"
- "configurationWithPointSize:weight:"
- "configurationWithPointSize:weight:scale:"
- "configureNavigationItem"
- "configureWithDefaultBackground"
- "confirm:"
- "confirmCellularPlanTransfer"
- "confirmTextView"
- "confirmationCode"
- "confirmationCodeRequired"
- "confirmationCodeViewController"
- "conformsToProtocol:"
- "connectCrossPlatformTransportWithCode:completion:"
- "connection"
- "connectionEstablished"
- "consentType"
- "consolidatedActivatingState"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToAnchor:constant:priority:"
- "constraintEqualToConstant:"
- "constraintGreaterThanOrEqualToAnchor:"
- "constraintGreaterThanOrEqualToAnchor:constant:"
- "constraintGreaterThanOrEqualToConstant:"
- "constraintLessThanOrEqualToAnchor:"
- "constraintLessThanOrEqualToAnchor:multiplier:"
- "constraintLessThanOrEqualToAnchor:multiplier:constant:"
- "constraintLessThanOrEqualToConstant:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "containsObject:"
- "containsStringCaseInsensitive:"
- "contentHuggingPriorityForAxis:"
- "contentOffset"
- "contentSize"
- "contentView"
- "continueAction"
- "continueButton"
- "continueTransferWithoutWifi:"
- "convertPhysicalSIMToeSIMWithCompletion:"
- "convertPhysicalToeSIMWithCompletionHandler:"
- "convertRect:fromView:"
- "copy"
- "copyCarrierBundleValue:key:bundleType:error:"
- "copyCarrierBundleValue:keyHierarchy:bundleType:error:"
- "corners"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createTSRemotePlanWebsheetContext:"
- "crossPlatformTransferItems"
- "crossPlatformTransferPlanSelected"
- "ctClient"
- "currentDevice"
- "currentItemsForIMessage"
- "currentLocale"
- "currentSavedAccountContextForFormAutoFillController:"
- "currentTitle"
- "customLabel"
- "customLabelIndexPath"
- "customLabelRowValue"
- "customizeSpinner"
- "cutoutView"
- "d"
- "d16@0:8"
- "d32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "d32@0:8@\"UITableView\"16q24"
- "d32@0:8@16@24"
- "d32@0:8@16q24"
- "d48@0:8@\"WKWebView\"16{CGSize=dd}24@\"<_WKFormInputSession>\"40"
- "d48@0:8@16{CGSize=dd}24@40"
- "danglingPlanItem"
- "danglingPlanItems"
- "danglingPlanItemsShouldUpdate:"
- "darkQRCode"
- "dataSwitchChanged:"
- "dataUsingEncoding:"
- "dataWithCapacity:"
- "dataWithJSONObject:options:error:"
- "dataWithPropertyList:format:options:error:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dctCode"
- "dctDelegate"
- "dctInfo"
- "dctPrewarmSucceded"
- "deactivate"
- "deactivateConstraints:"
- "deactivateCrossPlatformTransport:completion:"
- "deactiveCrossPlatformTransport"
- "dealloc"
- "deassertUserInPurchaseFlowWithForce:caller:"
- "debugDescription"
- "declineButton"
- "declineCrossPlatformTransfer:"
- "decodeMetadata:"
- "defaultCenter"
- "defaultConfig"
- "defaultContentConfiguration"
- "defaultDeviceWithMediaType:"
- "defaultMetrics"
- "defaultStore"
- "defaultVoiceIccid"
- "defaultVoiceItem"
- "defaultWebpagePreferences"
- "defaultWorkspace"
- "delegate"
- "dequeueReusableCellWithIdentifier:"
- "dequeueReusableCellWithIdentifier:forIndexPath:"
- "description"
- "descriptionLabel"
- "descriptorWithSubscriptionContext:"
- "descriptors"
- "deselectRowAtIndexPath:animated:"
- "detailLabelConstraints"
- "detailText"
- "detailTextLabel"
- "device has no capable cross platform transfer plans @%s"
- "deviceID"
- "deviceName"
- "deviceSupportsHydra"
- "devices"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithPlansByGroupByTransferCapability:"
- "didCancelRemotePlan"
- "didChangeValueForKey:"
- "didComplete"
- "didDeletePlanItem:completion:"
- "didEnablePlanItems:"
- "didEnablePlanItemsForTravel:"
- "didProcessDCTCode"
- "didPurchasePlanForCarrier:mnc:gid1:gid2:state:"
- "didPurchasePlanForCsn:iccid:profileServer:state:"
- "didPurchasePlanForEid:iccid:smdpURL:state:"
- "didPurchasePlanSuccessfullyWithCarrier:mnc:gid1:gid2:state:"
- "didPurchasePlanSuccessfullyWithEid:imei:meid:iccid:alternateSDMP:state:"
- "didPurchasePlanWithIccid:downloadProfile:"
- "didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:"
- "didRequestPresentationForProxCard:"
- "didSelectPlanForData:completion:"
- "didSelectPlanForDefaultVoice:completion:"
- "didSelectPlanItem:isEnable:"
- "didSelectPlansForIMessage:completion:"
- "didTransferPlanForCsn:iccid:srcIccid:profileServer:state:"
- "didTransferPlanForEid:iccid:srcIccid:smdpURL:state:"
- "didTransferPlanSuccessfullyWithEid:imei:meid:iccid:srcIccid:alternateSDMP:state:"
- "didUserClickContinue"
- "disableButtonsAndHideSpinnerText"
- "disablePredicativeTextForTextField:"
- "dismiss"
- "dismissAutoFillInternalFeedbackActivityForFormAutoFillController:immediately:"
- "dismissCause"
- "dismissSimSetupFlowFromViewController"
- "dismissViewControllerAnimated:completion:"
- "dismissViewControllerWithTransition:completion:"
- "dismissingViewController"
- "displayPlan"
- "displayPlanFromObject:"
- "displayedDeviceIDs"
- "displayedPages"
- "doRegistrationForIMessage:"
- "domain"
- "doneAction"
- "doneButton"
- "doubleValue"
- "drawInRect:"
- "drawQRBox:"
- "dualSimCapabilityDidChange"
- "durationForTransition:"
- "eSIMInstallFromWebsheetFlowStarted"
- "eSIMTravelState"
- "edgeConstraintsWithTop:leading:bottom:trailing:"
- "editableTextField"
- "effect"
- "enablingIccid"
- "encryptDataWithCarrierIdentifiers:mnc:gid1:gid2:data:completion:"
- "endBackgroundTask:"
- "endEditing:"
- "endFlowGracefully:"
- "endpoint"
- "enterDetailsManuallyButton"
- "entryPoint"
- "enumerateKeysAndObjectsUsingBlock:"
- "ephemeralSessionConfiguration"
- "errorForCode:"
- "errorWithDomain:code:userInfo:"
- "establishReconnectionCredentials:completion:"
- "establishReconnectionCredentialsUsingMessageSession:completion:"
- "evaluateAccessControl:operation:options:error:"
- "evaluateAccessControl:operation:options:reply:"
- "evaluateDtoPolicy:"
- "event:params:reply:"
- "eventHandler"
- "extent"
- "externalized context = %@ isSecureIntentRequired: %d, isDtoEvaluationRequired:%d @%s"
- "externalizedContext"
- "extractPhoneInfoFromOptions:"
- "failureWebsheetError"
- "fauxCardData"
- "fieldFocusedWithInputSession:"
- "filterCarrierSetupItems:"
- "filterTransferPlans:"
- "filterUsingPredicate:"
- "filterWithName:"
- "filteredArrayUsingPredicate:"
- "filteredPlansForHiddenInCloudBucket:"
- "filteredPlansForNonInstallableBucket"
- "filteredPlansForNonQRCodeBucket"
- "filteredPlansForQRCodeBucket"
- "filteredPlansForSoftwareUpdateBucket"
- "filteredPlansForTransferableBucket"
- "filteredPlansForUnknownLocationBucket"
- "filteredPlansForVisitStoreBucket"
- "filteredPlansWithTransferCapabilities:restrictionAllowed:"
- "filteredPlansWithTransferCapability:"
- "filteredPlansWithoutSODATether:"
- "findFirstResponderInView:"
- "findSubscriptionContextForCellularPlanItem:fromSubscriptionContexts:"
- "firstBaselineAnchor"
- "firstLabel"
- "firstObject"
- "firstViewController"
- "firstViewController:"
- "firstViewControllerCallback"
- "firstViewControllerForDisplay"
- "firstViewControllerInstance"
- "floatValue"
- "flow"
- "flowCompleted:"
- "flowWithOptions:"
- "followDirections"
- "font"
- "fontDescriptor"
- "fontDescriptorWithSymbolicTraits:"
- "fontWithDescriptor:size:"
- "footer"
- "forceDualSIMSetup"
- "forceRecheckTransferableAndPendingInstallPlans"
- "formAutoFillControllerCanPrefillForm:"
- "formAutoFillControllerDidFocusSensitiveFormField:"
- "formAutoFillControllerDidUserDeclineAutomaticStrongPasswordForCurrentDomain:"
- "formAutoFillControllerGetAuthenticationForAutoFill:completion:"
- "formAutoFillControllerShouldDisableAutoFill:"
- "formAutoFillControllerShouldDisableStreamlinedLogin:"
- "formAutoFillControllerURLForFormAutoFill:"
- "formAutoFillControllerUserChoseToUseGeneratedPassword:"
- "formatLocAndConcatenateDescriptors:"
- "formatedDescriptor"
- "formattedPhoneNumber"
- "formattedPhoneNumber:withCountryCode:"
- "fragment"
- "frame"
- "getAVCaptureMetadataOutput"
- "getAccountMemberTransferablePlanWithSameCarrierName:transferablePlans:"
- "getByteRepresentationOf:"
- "getCarrierSetupWithCompletion:"
- "getCellTextAt:"
- "getCellularPlanItem:withIccid:"
- "getCombinedFooterForNonTransferablePlans"
- "getCombinedTitleAndDetailsForNonTransferablePlans:details:"
- "getCombinedTitleAndDetailsForTransferCapability:title:detail:"
- "getCoreTelephonyClient"
- "getCrossPlatformTransportSession:completion:"
- "getDCTCode:"
- "getDanglingPlanItems"
- "getDetail:"
- "getDetails:"
- "getDetailsWithTransferOption:showQRCodeOption:showCrossTransferOption:transferIneligiblePlans:"
- "getDisplayOptions"
- "getErrorDescription:"
- "getErrorTitleDetail:forCarrier:"
- "getHardwareModelName"
- "getLocalizedStringIf:then:otherwise:"
- "getMobileEquipmentInfo:"
- "getPendingLabelAtIndex:"
- "getPhoneInfoFromCT"
- "getPlanByID:fromPlans:"
- "getPlanItemByIndex:"
- "getPlanTransferCredentials:completion:"
- "getPredefinedLabels"
- "getPredefinedUserLabels"
- "getProximityTransportSession:remoteDeviceInfo:usePreSharedKey:completion:"
- "getRemoteDeviceDisplayName:"
- "getRemotePlanManageAccountInfoFor:completion:"
- "getShortLabelsForLabels:"
- "getSpinnerBusyText"
- "getStoreVisitStatusForCarrier:"
- "getStoreVisitStatusForPlan:cache:"
- "getStringWithFirstCharacterUppercase:"
- "getSubscriptionContextUUIDforPlan:"
- "getSubscriptionInfo:"
- "getSubscriptionInfoWithError:"
- "getSupportedFlowTypes"
- "getSupportedFlowTypes:"
- "getTitleAndDetailsForPlanType:transferCapability:isShowingFilteredPlans:carrier:"
- "getTitleAndDetailsForTransferCapability:carrier:phoneNumber:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isVisitStoreRequired:"
- "getTransferCapability:"
- "getTransferPlansWithCompletion:"
- "getTravelInfoForIccid:completion:"
- "getWebsheetInfo:completion:"
- "getWebsheetInfoForPlan:inBuddy:completion:"
- "getWebsheetViewController"
- "getWordRepresentationForInt:"
- "glyphView"
- "grayColor"
- "handleCrossplatformSessionResponse:completion:"
- "handleError:"
- "handleProvisioningWatchdogExpiry"
- "handleStartOverWithEntryPoint:navigationController:completion:"
- "handleTermsAndConditionsCompleted:consented:completion:"
- "handleTransferringWatchdogExpiry"
- "handleUserEnteredOtp:otp:completion:"
- "handleWaitingOnWifiStatusUpdate:"
- "hasBackButton"
- "hasCellularBaseband"
- "hasCellularConnection:"
- "hasCode"
- "hasContinueButton"
- "hasDoneButton"
- "hasInstallingPlanOrUserPlan:"
- "hasPrefix:"
- "hasProvisioningServiceImpact"
- "hasProvisioningServiceImpact:"
- "hasProvisioningServiceImpact:error:"
- "hasProvisioningServiceImpactMap"
- "hasTransferablePlan"
- "hasTransferablePlanWithSameCarrierName:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:"
- "hash"
- "headerLabel"
- "headerLabelToDetailAndSubtitleLabelPadding"
- "headerLabelToDetailLabelPadding"
- "headerView"
- "heightAnchor"
- "hideSpinner"
- "hideTransferPlan:fromDevice:completion:"
- "hidesBackButton"
- "hidesBusyIndicator"
- "hostViewController"
- "httpCookieStore"
- "i16@0:8"
- "iccidHash"
- "iccidToEnable"
- "imageByApplyingSymbolConfiguration:"
- "imageByApplyingTransform:"
- "imageBySamplingNearest"
- "imageName"
- "imageNamed:inBundle:withConfiguration:"
- "imageView"
- "imageWithCIImage:"
- "imageWithRenderingMode:"
- "imageWithTintColor:"
- "imgView"
- "in buddy"
- "inBuddy"
- "indexInPredefinedLabels:"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "indexPathForPreferredFocusedViewInTableView:"
- "indexPathForRow:inSection:"
- "indexPathsForSelectedRows"
- "indexesOfObjectsPassingTest:"
- "indicatorView"
- "infoDictionary"
- "init"
- "init:"
- "initAsMidOperationWithCarrierName:"
- "initAsMidOperationWithCarrierName:requireGeneralConsent:"
- "initForRemotePlan:carrierName:skipUIDismissal:"
- "initForRemotePlan:carrierName:skipUIDismissal:showCarrierWarning:"
- "initForRemotePlan:carrierName:viewController:"
- "initForResumptionWithSelectedTransferPlans:targetUICapability:isPreSharedKeyPresent:"
- "initNonPersistentConfiguration"
- "initRequireSetup:transferBackPlan:"
- "initShowCarrierNotSupportCrossPlatformTransfer"
- "initShowErrorOnSourceWithDelayedDownloadECSWithPlanIdentifier:"
- "initShowErrorOnSourceWithPlanIdentifier:"
- "initShowNoSIMForCrossPlatformTransfer"
- "initWith:fallbackToActivationCode:ignoreTransport:"
- "initWithActivityIndicatorStyle:"
- "initWithAllowDismiss:"
- "initWithAppName:requireSetup:skipGeneralInstallConsent:hasProvisioningServiceImpact:"
- "initWithArrangedSubviews:"
- "initWithArray:"
- "initWithAssociatedPlanItem:initialLabel:predefinedUserLabels:"
- "initWithBTServer:transferBackPhoneNumber:"
- "initWithBackButton:"
- "initWithBackButton:continueButton:danglingPlanItem:"
- "initWithBackButton:plans:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithBase64EncodedString:options:"
- "initWithBlockForUpdates:"
- "initWithBtDevice:"
- "initWithBtDevice:passcodeType:"
- "initWithBundleType:"
- "initWithButton:"
- "initWithCIImage:"
- "initWithCTPlan:inBuddy:"
- "initWithCTPlan:websheetURL:postdata:"
- "initWithCardData:"
- "initWithCarrier:phoneNumber:transferCapability:showOtherOptions:entryPoint:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:"
- "initWithCarrier:phoneNumber:transferCapability:showOtherOptions:entryPoint:sourceDeviceName:isTransferNotSupportedFromiPhone:isTransferBackPlan:isStartOverNeeded:"
- "initWithCarrierApps:country:"
- "initWithCarrierName:"
- "initWithCode:"
- "initWithConfirmationCode:consentType:requireAdditionalConsent:confirmationCode:acceptButtonTapped:hasProvisioningServiceImpact:"
- "initWithConfirmationCodeRequired:"
- "initWithConsentType:name:"
- "initWithCrossPlatformTransferPlan:"
- "initWithData:encoding:"
- "initWithDelegate:"
- "initWithDelegate:queue:options:"
- "initWithDetails:installIccid:sourceIccid:unusableIccid:phoneNumber:mcc:mnc:gid1:gid2:smdp:useDS:esim:flowType:"
- "initWithDevice:error:"
- "initWithDictionary:error:"
- "initWithDomain:code:userInfo:"
- "initWithESIMDelegate:"
- "initWithEnablingPlanIccid:"
- "initWithEnablingPlanInfo:"
- "initWithEventType:"
- "initWithEventType:error:"
- "initWithExternalizedContext:"
- "initWithExternalizedContext:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:"
- "initWithFlow:navigationController:delegate:"
- "initWithFrame:"
- "initWithFrame:configuration:"
- "initWithFrame:style:"
- "initWithFrame:style:limit:"
- "initWithHostController:"
- "initWithID:kind:context:limit:"
- "initWithID:kind:metrics:icon:heading:title:subtitle:ageRating:offer:"
- "initWithIccid:"
- "initWithIccid:forceDualSIMSetup:allowDismiss:"
- "initWithIccid:showAddPlan:forceDualSIMSetup:allowDismiss:"
- "initWithIccids:homeIccid:voiceIccid:postArrivalInstallation:"
- "initWithImage:"
- "initWithInBuddy:carrierName:setupType:setupResult:duration:"
- "initWithInBuddy:transferablePlans:selectedTransferablePlans:alsPlans:selectedAlsPlans:odaPlans:transferPlanCarriers:selectedTransferPlanCarriers:alsPlanCarriers:selectedAlsPlanCarriers:odaPlanCarriers:selectedOdaPlanCarriers:sourceDevicesCount:selectedSourceDevicesCount:"
- "initWithInfos:"
- "initWithInt64:"
- "initWithIsStandaloneProximityTransfer:transferBackPlan:"
- "initWithItem:"
- "initWithItems:"
- "initWithLabel:"
- "initWithLocalPhysical:carrierName:hasProvisioningServiceImpact:"
- "initWithName:"
- "initWithName:consentType:requireAdditionalConsent:hasProvisioningServiceImpact:"
- "initWithName:consentType:requireAdditionalConsent:trialPlanType:trialExpirationDate:hasProvisioningServiceImpact:"
- "initWithName:value:"
- "initWithNibName:bundle:"
- "initWithObjects:"
- "initWithOptions:"
- "initWithOptions:extractionSource:reduceEducation:arrivalCountry:"
- "initWithOptions:navigationController:delegate:"
- "initWithPIN:"
- "initWithPassword:"
- "initWithPasswordType:pairingFlags:throttleSeconds:"
- "initWithPasswordType:password:"
- "initWithPeerDevice:"
- "initWithPendingInstallItems:"
- "initWithPendingInstallPlan:"
- "initWithPendingInstallPlans:transferPlans:carrierSetupPlans:showQRCodeOption:showOtherOptions:isShowingFilteredPlans:isStandaloneProximityFlow:isHiddenPlanSelectable:"
- "initWithPhoneNumber:carrierName:iccid:"
- "initWithPlan:"
- "initWithPlan:queriableFirstViewController:hostViewController:"
- "initWithPlanIdentifer:"
- "initWithPlanIdentifiers:"
- "initWithPlanInfos:"
- "initWithPlanInfos:userEnablePlans:skip:"
- "initWithPlanItemError:"
- "initWithPlanItemError:updatePlanItem:withBackButton:forCarrier:withCarrierErrorCode:isEmbeddedInResultView:"
- "initWithPlans:"
- "initWithPlans:homeIccid:"
- "initWithPlans:isCrossPlatformTransfer:"
- "initWithPlans:isSelectedAsTravelSIM:"
- "initWithPlans:planItems:fromDataTransferSession:"
- "initWithPlans:selectedItems:skip:isForCrossPlatformTransfer:"
- "initWithPlans:showOtherOption:"
- "initWithPlans:showOtherOptions:"
- "initWithPlans:showOtherOptions:isStartOverNeeded:"
- "initWithPlans:skip:"
- "initWithPlans:withBackButton:"
- "initWithProximitySetupState:proxPlansFiltered:"
- "initWithQueue:"
- "initWithQueue:endpoint:remoteInfo:"
- "initWithRemotePlanWebsheetContext:"
- "initWithRemotePlanWebsheetContext:isRemotePlan:"
- "initWithRequestType:skipIntroPaneForWebsheetFlow:websheetURL:postdata:"
- "initWithRetainedObject:isSource:"
- "initWithRootViewController:"
- "initWithSecureIntentRejected"
- "initWithSelectedPlans:confirmCellularPlanTransfer:isForCrossPlatformTransfer:session:sourceOsVersion:"
- "initWithSelectedPlansCount:selectedPlansFailedTransferCount:isDisembarkUIRequired:"
- "initWithService:"
- "initWithSession:"
- "initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:"
- "initWithSession:sourceOSVersion:proximitySetupState:transferablePlanOnSource:"
- "initWithShowTransferOption:requireDelayBluetoothConnection:showQrCodeOption:transferIneligiblePlans:"
- "initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:isLocalConvert:"
- "initWithSource:injectionTime:forMainFrameOnly:"
- "initWithSourceIccid:mainText:"
- "initWithSourceIccid:phoneNumber:carrierName:usePin:"
- "initWithSpinnerText:"
- "initWithString:"
- "initWithString:attributes:"
- "initWithStyle:"
- "initWithStyle:reuseIdentifier:"
- "initWithSuccess:skipped:duration:"
- "initWithTag:delegate:"
- "initWithTarget:action:"
- "initWithTemplate:"
- "initWithText:"
- "initWithTimeoutReason:isEmbeddedInResultView:plans:"
- "initWithTitle:detail:"
- "initWithTitle:detailText:icon:"
- "initWithTitle:detailText:icon:adoptTableViewScrollView:"
- "initWithTitle:detailText:icon:contentLayout:"
- "initWithTitle:detailText:symbolName:"
- "initWithTitle:detailText:symbolName:adoptTableViewScrollView:"
- "initWithTitle:detailText:symbolName:contentLayout:"
- "initWithTitle:details:symbolName:plans:skip:"
- "initWithTitle:style:target:action:"
- "initWithTitle:subtitle:"
- "initWithTitle:subtitle:otpDetectorNeeded:"
- "initWithTransferBackPlan:"
- "initWithTransferBackPlan:isPostMigrationFlow:"
- "initWithTransferCredentials:carrierName:"
- "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:allowsMultiSelection:"
- "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:"
- "initWithTransferItems:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:showOtherOptions:allowsMultiSelection:"
- "initWithTransferOutPlan:"
- "initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isShowingFilteredPlans:"
- "initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isStandaloneProximityFlow:transferBackPhoneNumber:isShowingFilteredPlans:"
- "initWithTransferPlans:confirmCellularPlanTransfer:isActivationPolicyMismatch:isDualeSIMCapabilityLoss:pendingInstallItems:carrierSetupItems:showOtherOptions:isStandaloneProximityFlow:allowsMultiSelection:"
- "initWithTransferredPlan:"
- "initWithType:allowDismiss:"
- "initWithType:withDoneButton:"
- "initWithURL:configuration:"
- "initWithURL:postdata:carrierName:"
- "initWithURLTemplate:width:height:decoration:preferredCrop:preferredFormat:"
- "initWithWebView:delegate:"
- "initWithoutTargetSyncAndSelectedPlansCount:"
- "initialLabel"
- "insertObject:atIndex:"
- "insertSublayer:atIndex:"
- "insertTextSuggestion:"
- "installBucketSubtitle"
- "installBucketTitle"
- "installError"
- "installInfos"
- "installMultiplePlans:completionHandler:"
- "installPendingPlan:completion:"
- "installPendingPlanList:completion:"
- "installRestriction"
- "installationEndTime"
- "installationStartTime"
- "installingPlanInfos"
- "installingTransferPlan"
- "intValue"
- "integerValue"
- "invalidate"
- "invalidate:"
- "invalidateProximityTransfer:force:completion:"
- "invertedSet"
- "invokeCompletionWithPlanInstallResult:"
- "iphone.and.arrow.forward"
- "isAccountMemberTransferablePlan"
- "isActivationPolicyMismatch"
- "isActivationPolicyMismatch: %d, transfer plans: %@ @%s"
- "isActiveDataPlan"
- "isAnimating"
- "isAnyPlanOfTransferCapability:availableForThisDeviceWithCompletion:"
- "isAnyPlanOfTransferCapability:withCompletion:"
- "isAnyPlanTransferableFromThisDeviceForFlow:OrError:"
- "isAuthenticationCompleted"
- "isAutoFocusRangeRestrictionSupported"
- "isAvailableOptionsQueryCompleted"
- "isBackAllowed:"
- "isBluetoothOff:"
- "isBootstrapAssertionRequired"
- "isCancelButtonTapped"
- "isCancelTapped"
- "isCarrierDirectAuthItemSelected"
- "isCarrierSetupItemSelected"
- "isCaseInsensitiveEqual:withString:"
- "isCloudFlow"
- "isContinueByUser"
- "isCrossPlatformButtonTapped"
- "isD2dDone"
- "isDataActive"
- "isDataOnly"
- "isDataOnlySelected"
- "isDefaultVoice"
- "isDeleteNotAllowed"
- "isDeviceIdentifierPresent"
- "isDeviceLocked"
- "isDisableNotAllowed"
- "isDisabled"
- "isDisembarkUIRequired"
- "isDtoEvaluationRequired"
- "isDtoEvaluationSucceeded"
- "isDualSIMConfig"
- "isDualeSIMCapablityLoss"
- "isEOnly"
- "isEmbeddedSIMOnlyConfig"
- "isEmbeddedSIMOnlyConfig:"
- "isEnterManuallyTapped"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToPhoneNumber:"
- "isEqualToSet:"
- "isEqualToString:"
- "isExistingPlanTapped"
- "isExposureModeSupported:"
- "isExternalizedContextSent"
- "isFirstResponder"
- "isFlowCompleted"
- "isFlowFinished"
- "isFocusModeSupported:"
- "isForCrossPlatformTransfer"
- "isFromDataTransferSession"
- "isGlobalMVNO"
- "isGreenTeaCapable"
- "isHiding"
- "isIccidForPhySlot:"
- "isIdleTimerDisabled"
- "isInModalPresentation"
- "isInstalling"
- "isKindOfClass:"
- "isLanguageRightToLeft"
- "isLocalConvert"
- "isLocalConvertFlow"
- "isMemberOfClass:"
- "isMovingFromParentViewController"
- "isMovingToParentViewController"
- "isMultiESimEnabled"
- "isNFCDataSuccessTransfer"
- "isNFCEnable"
- "isNotEligibleActivationPolicyMismatchPlan"
- "isOfferFallbackFlow"
- "isOn"
- "isOnBootstrap"
- "isOnDeviceTransferredPlan"
- "isOneClickTransferablePlan"
- "isOtherButtonTapped"
- "isPad"
- "isPhone"
- "isPhysical"
- "isPlanHiddenRequiredForCloudFlow"
- "isPlanInstalledAndNotEnabled:item:"
- "isPlanWithIccid:"
- "isPostMigrationFlow"
- "isPreInstalled"
- "isPreSharedKeyForReconnectionPresent:completion:"
- "isPreSharedKeyPresent"
- "isPreinstallingViewControllerActive"
- "isProcessCanceled"
- "isProxFlowShown"
- "isProximityFlow"
- "isProximityTransferButtonTapped"
- "isProxy"
- "isPurchaseLocalPlanTapped"
- "isRegRestActiveLocationAuthorizedOff:"
- "isRegRestActiveLocationServiceOff:"
- "isRegRestLocationUnavailable:"
- "isRegulatoryRestrictedForCurrentLocationPlan"
- "isRegulatoryRestrictedPlan"
- "isRegulatoryRestrictionActive:"
- "isRemotePeerClosed"
- "isRemotePlan"
- "isResumingAfterPause"
- "isRoamingTapped"
- "isSIMTypeSelectionShown"
- "isScanButtonTapped"
- "isSecureIntentFailed"
- "isSecureIntentRejected"
- "isSecureIntentRequired"
- "isSecureIntentSucceeded"
- "isSecureIntentUIRequired:"
- "isSecuredFlow"
- "isSelectable"
- "isSelected"
- "isSelectedAsTravelSIM"
- "isSharingIdentitySupportedWithError:"
- "isShown"
- "isSimDataOnly"
- "isSkipButtonTapped"
- "isSolariumEnabled"
- "isSource"
- "isSourceProxCardVisible"
- "isStandaloneProximityFlow"
- "isStandaloneProximityTransfer"
- "isStartOverNeeded"
- "isStartOverRequiredOnBackButtonTapped"
- "isSyncWithTargetResults"
- "isTransferButtonTapped"
- "isTransferCompleted"
- "isTransferIneligiblePlan"
- "isTransferListCellTapped"
- "isTransferNotSupportedFromiPhone"
- "isTransferablePlan"
- "isTravelEduButtonTapped"
- "isTraveleSIM"
- "isUserInHomeCountry"
- "isUserInteractionEnabled"
- "isUserTraveling"
- "isUsingPreSharedKey"
- "isVideoOrientationSupported"
- "isViewControllerPresented"
- "isViewControllerPresenting"
- "isVinylCapable"
- "isWebsheetTransferablePlan"
- "isWhiteBalanceModeSupported:"
- "isWiFi:%d, hasPlans:%d, usingBootstrap:%d @%s"
- "isWifiAvailable"
- "keyboardDidHide:"
- "keyboardWasShown:"
- "keyboardWillBeHidden:"
- "labelColor"
- "labelId"
- "labelPickerViewController"
- "lastError"
- "lastObject"
- "launchSecureIntentUI:descriptors:isLocalConvertFlow:isSecureIntentRequired:isDtoEvaluationRequired:completion:"
- "launchSimSetupForTransferPlanSelection:completion:"
- "launchURL:"
- "launchWebsheet:completion:"
- "layer"
- "layoutIfNeeded"
- "layoutMarginsGuide"
- "layoutSubviews"
- "leadingAnchor"
- "leadingConstraint"
- "leftAnchor"
- "leftBarButtonItems"
- "leftConstraint"
- "length"
- "lightGrayColor"
- "lightQRCode"
- "limit"
- "linkButton"
- "listCellConfiguration"
- "loadCarrierStoreVisitStatusForCarrier:error:"
- "loadRequest:"
- "loadRequest:completion:"
- "loadSimSetupInfo"
- "loadSimSetupInfo:"
- "loadSimSetupInfo:error:"
- "loadView"
- "localizedCaseInsensitiveCompare:"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "lockForConfiguration:"
- "lockupView"
- "lockupView:appStateDidChange:"
- "lockupView:didFailRequestWithError:"
- "lockupViewDidBeginRequest:"
- "lockupViewDidFinishRequest:"
- "lockupViewDidInvalidateIntrinsicContentSize:"
- "lowercaseString"
- "mainBundle"
- "mainContentGuide"
- "mainScreen"
- "mainText"
- "makeCGPoint:"
- "matchingSim"
- "maybePrepareNextDisplayViewController:completion:"
- "maybeRegisterDismissHandler:"
- "maybeShowConfirmationCodePane"
- "maybeUpdateTimeoutStatus"
- "meInfoList"
- "mergeByTransferCapabilities:"
- "messageSession"
- "metadataOutputRectOfInterestForRect:"
- "metricsActivityForLockupView:toPerformActionOfOffer:"
- "model"
- "modelName"
- "moveToPoint:"
- "mutableCopy"
- "name"
- "navBarTitle"
- "navigateToNextPaneFrom:navigationController:"
- "navigationController"
- "navigationController:animationControllerForOperation:fromViewController:toViewController:"
- "navigationController:didShowViewController:animated:"
- "navigationController:interactionControllerForAnimationController:"
- "navigationController:willShowViewController:animated:"
- "navigationControllerPreferredInterfaceOrientationForPresentation:"
- "navigationControllerSupportedInterfaceOrientations:"
- "navigationItem"
- "navigationItems"
- "nearbyActionDeviceClass"
- "nearbyActionExtraData"
- "needHideForCloudFlow"
- "needOfferProximityTransferOption"
- "needOfferQRCodeOption"
- "needShow"
- "needShowTransferIntroPane"
- "needVisitStoreForTransfer"
- "needsCustomMemoryError"
- "needsToRun:"
- "needsToRunUsingMessageSession:completion:"
- "needsToRunUsingMessageSession:transferablePlanOnSource:completion:"
- "nextViewController"
- "nextViewControllerFrom:"
- "nfcAnimationView"
- "nfcAssertion"
- "nonMagnoliaCount"
- "normalStateTitle"
- "notificationWithName:object:userInfo:"
- "null"
- "numActivePlansOnDeviceExcept:"
- "numSelectedPlansNotTransferredOut"
- "numberOfRowsInSection:"
- "numberOfSections"
- "numberOfSectionsInTableView:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "odaPlanCarriers:"
- "odaPlans:"
- "onCodeDetected:completion:"
- "onError"
- "oneTimeCodeAccelerator"
- "oneTimeCodeViewController"
- "oneTimePasscodePaneShown"
- "openApplication:withOptions:completion:"
- "openPrefsURL:"
- "openSensitiveURL:withOptions:"
- "openSensitiveURL:withOptions:error:"
- "openURL:options:completionHandler:"
- "optionsWithDictionary:"
- "orientation"
- "originalEnabledPlans"
- "otherOptionsButton"
- "otpDetectorNeeded"
- "otpEditor"
- "outputImage"
- "outputs"
- "parentFlow"
- "parentViewController"
- "parseQueryParamsWithTitleDictionary:"
- "passcodeEntryView"
- "passcodeType"
- "path"
- "pathForResource:ofType:"
- "peerDeviceInfo"
- "pendingInstallItems"
- "pendingInstallItemsWithCompletion:"
- "pendingInteractiveViewControllers"
- "pendingReleaseRemotePlan"
- "percentEncodedQuery"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phoneSubscriptionWithSubscriptionSlot:"
- "physicalButtonView"
- "pin"
- "pinCodeLabel"
- "pinToEdges:"
- "pinToHorizontalEdges:"
- "pinToVerticalEdges:"
- "placeHolderLabel"
- "planEnablementState"
- "planError"
- "planID"
- "planInfo"
- "planInstallError"
- "planItemBadges"
- "planItemText:"
- "planItems"
- "planItemsShouldUpdate:"
- "planItemsUpdated:planListError:"
- "planItemsWithCompletion:"
- "planList"
- "planName"
- "planSetupType"
- "plans"
- "plansDidUpdate:"
- "plansPendingCrossPlatformTransferWithCompletion:"
- "plansPendingInstallWithCompletion:"
- "pointForCaptureDevicePointOfInterest:"
- "pointSize"
- "popToViewController:animated:"
- "popViewControllerAnimated:"
- "populatePostbackDictionary:"
- "position"
- "post buddy"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "postdata"
- "predefinedUserLabels"
- "predicateWithBlock:"
- "preferredContentSize"
- "preferredFontForTextStyle:"
- "preferredLanguages"
- "prefillFormsSoonIfNeeded"
- "preinstallPPRAlertControllerWithItems:completion:"
- "prepare:"
- "prepareForReuse"
- "prepareLabels:"
- "prepareViewController:completion:"
- "presentAutoFillInternalFeedbackToastForFormAutoFillController:diagnosticsDataWithoutPageContents:"
- "presentInSettings"
- "presentProxCardFlowWithDelegate:initialViewController:"
- "presentViewController:animated:completion:"
- "presentationController"
- "presentationController:prepareAdaptivePresentationController:"
- "presentationController:viewControllerForAdaptivePresentationStyle:"
- "presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:"
- "presentationControllerDidAttemptToDismiss:"
- "presentationControllerDidDismiss:"
- "presentationControllerShouldDismiss:"
- "presentationControllerWillDismiss:"
- "presentedViewController"
- "presentingViewController"
- "presentingViewControllerForLockupView:"
- "prevTravelOnlySelection"
- "prevViewController"
- "preventConnectionHandoverAssertion"
- "previewLayer"
- "previousLeftBarButtonItems"
- "previousRightBarButtonItems"
- "primaryAccount"
- "primaryAction"
- "primaryColor"
- "productClass"
- "productVersion"
- "provideUserResponse:confirmationCode:"
- "proxCardFlowDidDismiss"
- "proxCardFlowWillPresent"
- "proxSetupAuthEventUpdate:"
- "proxTransferController"
- "proximitySetupState"
- "pushTimeoutFailureViewControllerWithStatus:forPlan:"
- "pushToDetailViewControllerWithError:forPlan:"
- "pushViewController:animated:"
- "q16@0:8"
- "q24@0:8@\"UINavigationController\"16"
- "q24@0:8@\"UIPresentationController\"16"
- "q24@0:8@\"UITableView\"16"
- "q24@0:8@16"
- "q24@?0@8@16"
- "q32@0:8@\"UIPresentationController\"16@\"UITraitCollection\"24"
- "q32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "q32@0:8@\"UITableView\"16q24"
- "q32@0:8@\"WKWebView\"16@\"<_WKFocusedElementInfo>\"24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q40@0:8@\"UITableView\"16@\"NSString\"24q32"
- "q40@0:8@16@24q32"
- "qrCode"
- "qrcodeBucketSubtitle"
- "qrcodeBucketTitle"
- "qrcodeDelegate"
- "query"
- "queryItemWithName:value:"
- "queryItems"
- "queryParamToTitle"
- "queryStartSessionRequest:"
- "radioImageView"
- "rangeOfCharacterFromSet:"
- "rangeOfComposedCharacterSequencesForRange:"
- "rangeOfString:"
- "rangeOfString:options:"
- "receivedResponse"
- "receivedResponseWithVC:"
- "registerClass:forCellReuseIdentifier:"
- "registerIMessageWithPlanItems:"
- "registerSlotsForIMessage:"
- "release"
- "releaseAssertion:"
- "reloadData"
- "reloadInputViews"
- "remapDanglingItem:"
- "remapSimLabel:to:"
- "remoteDeviceClass"
- "remoteDisplayPlans"
- "remoteInfo"
- "remotePlan"
- "remotePlanSignupInfoFor:userConsent:completion:"
- "remotePlanWebsheetContext"
- "remoteUIController"
- "remoteUIController:createPageWithName:attributes:"
- "remoteUIController:didDismissModalNavigationWithObjectModels:"
- "remoteUIController:didFinishLoadWithError:"
- "remoteUIController:didFinishLoadWithError:forRequest:"
- "remoteUIController:didPresentObjectModel:modally:"
- "remoteUIController:didReceiveChallenge:completionHandler:"
- "remoteUIController:didReceiveHTTPResponse:"
- "remoteUIController:didReceiveHTTPResponse:forRequest:"
- "remoteUIController:didReceiveObjectModel:actionSignal:"
- "remoteUIController:didRefreshObjectModel:"
- "remoteUIController:didRemoveObjectModel:"
- "remoteUIController:loadResourcesForObjectModel:completion:"
- "remoteUIController:objectModel:shouldDisplayNamedElement:page:"
- "remoteUIController:shouldLoadRequest:redirectResponse:"
- "remoteUIController:shouldLoadRequest:redirectResponse:withCompletionHandler:"
- "remoteUIController:willLoadRequest:"
- "remoteUIController:willPresentModalNavigationController:"
- "remoteUIController:willPresentObjectModel:modally:"
- "remoteUIControllerDidDismiss:"
- "removeAllButtons"
- "removeAllObjects"
- "removeAllScriptMessageHandlers"
- "removeButton:"
- "removeFromSuperlayer"
- "removeFromSuperview"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeObserver:name:object:"
- "renewOneTimePassword:completion:"
- "replaceAction:withNewAction:"
- "replaceObjectAtIndex:withObject:"
- "request"
- "requestAssertion:error:"
- "requestCarrierSetups:"
- "requestCompletion"
- "requestCrossPlatformTransferPlanListWithCompletion:"
- "requestPendingInstallPlans:"
- "requestPlans:transferablePlanOnSource:bootstrapOnly:sourceOSVersion:isPostMigrationFlow:isUsingPreSharedKey:completion:"
- "requestPlansWithCompletion:"
- "requestTransferPlans:"
- "requestWithType:URL:postdata:"
- "requestWithURL:"
- "requireDelayBluetoothConnection"
- "requireSetup"
- "requireStoreVisitItems"
- "requireVisitStoreOnce"
- "requiresSoftwareUpdate"
- "resendOTPButton"
- "resetDelegate:"
- "resetFirstResponder"
- "resetPendingAutoFillInternalFeedbackToastDismissalTimer"
- "resetProximityTransportExtension:"
- "resignFirstResponder"
- "resolvedColorWithTraitCollection:"
- "respondsToSelector:"
- "restartWith:"
- "resumeCrossPlatformTransferSession:"
- "resumePlanProvisioning:userConsent:"
- "resumePlanProvisioning:userConsent:completion:"
- "retain"
- "retainCount"
- "retry"
- "retryAction"
- "returnHome"
- "rightAnchor"
- "rightBarButtonItems"
- "rightConstraint"
- "rootFlow"
- "rootViewController"
- "row"
- "rowHeight"
- "rows"
- "sGetSelectedPlanItems"
- "sInPrivateNetworkMode:"
- "sInPrivateNetworkModeForItem:"
- "safariViewController:activityItemsForURL:title:"
- "safariViewController:didCompleteInitialLoad:"
- "safariViewController:excludedActivityTypesForURL:title:"
- "safariViewController:initialLoadDidRedirectToURL:"
- "safariViewController:url:postdata:completion:"
- "safariViewControllerDidFinish:"
- "safariViewControllerWillOpenInBrowser:"
- "saveCarrierStoreVisitStatus:visited:completion:"
- "saveDefaultUse:"
- "savePlanLabels:"
- "saveSimSetupInfo:info:"
- "saveSimSetupInfo:info:completion:"
- "saveStoreVisitStatusForCarrier:visited:"
- "scale"
- "scaledValueForValue:"
- "scanView"
- "scannerView"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "scheme"
- "screenOn"
- "scrollRectToVisible:animated:"
- "scrollView"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "secondLabel"
- "secondaryButtonDetail"
- "secondaryLabelColor"
- "secondarySystemBackgroundColor"
- "secondaryText"
- "secondaryTextProperties"
- "section"
- "sectionIndexTitlesForTableView:"
- "sections"
- "secureIntentAccessControlItem"
- "secureIntentProxCard"
- "selectPlanForData:"
- "selectPlanForVoice:"
- "selectPlansForIMessage:"
- "selectRowAtIndexPath:animated:scrollPosition:"
- "selectTransferPlans:completion:"
- "selectedCarrierItem"
- "selectedItems"
- "selectedPlan"
- "selectedPlanItems"
- "selectedPlanTransferStatus"
- "selectedPlans"
- "selectedPlansCount"
- "selectedPlansFailedTransferCount"
- "selectedSubscriptionsWithError:"
- "selectedTransferPlan"
- "selectedTransferPlansCount"
- "self"
- "sendRequestID:options:request:responseHandler:"
- "sendTravelBuddyCAEvent:carrierName:error:"
- "sendTravelBuddyCAEvent:error:"
- "sendUserResponse:confirmationCode:"
- "session"
- "set"
- "setAcceptButton:"
- "setAccessibilityLabel:"
- "setAccessoryType:"
- "setAccessoryView:"
- "setAction:"
- "setActivatingTimer:"
- "setActive:"
- "setActivityIndicator:"
- "setActivityIndicatorHidden:"
- "setAdjustsFontSizeToFitWidth:"
- "setAlignment:"
- "setAllPlans:"
- "setAllPlansActivated:"
- "setAllowDismiss:"
- "setAllowsInlineMediaPlayback:"
- "setAllowsMultipleSelection:"
- "setAllowsSelection:"
- "setAllowsSelectionDuringEditing:"
- "setAlpha:"
- "setAnimating:"
- "setAnimationStyle:"
- "setAreAllPlansTransferedOut:"
- "setAreTransferPlansReady:"
- "setAssociatedIccid:"
- "setAssociatedPlanItem:"
- "setAttributedText:"
- "setAutoFocusRangeRestriction:"
- "setAutocapitalizationType:"
- "setAutocorrectionType:"
- "setAutomaticallyPresentsProductDetails:"
- "setAutoresizesSubviews:"
- "setAutoresizingMask:"
- "setAxis:"
- "setBackBarButtonItem:"
- "setBackOptions:"
- "setBackToSelfOption:"
- "setBackgroundColor:"
- "setBackgroundColorTransformer:"
- "setBackgroundConfiguration:"
- "setBackgroundTask:"
- "setBackgroundView:"
- "setBadge:"
- "setBoldSubString:"
- "setBorderColor:"
- "setBorderStyle:"
- "setBorderWidth:"
- "setBottomConstraint:"
- "setBtClient:"
- "setBtDevice:"
- "setBtServer:"
- "setBuddyMLURL:"
- "setBuddyMLViewController:"
- "setCachedButtons:"
- "setCachedIneligibleViewController:"
- "setCachedPlanItems:"
- "setCallbackDelegate:"
- "setCancelAction:"
- "setCancelButton:"
- "setCancelNavigationBarItems:"
- "setCancelledDeviceIDs:"
- "setCarrierErrorCode:"
- "setCarrierItems:"
- "setCarrierName:"
- "setCarrierNameForSelectedItem:"
- "setCarrierSetupItems:"
- "setCarrierSetupPlan:"
- "setCarrierURL:"
- "setChosenLabelIndexPath:"
- "setChosenTargetCellularPlanItem:"
- "setChosenUseIndexPath:"
- "setChosenUseIndexPaths:"
- "setClearButtonMode:"
- "setClient:"
- "setClipsToBounds:"
- "setCode:"
- "setCodeTextField:"
- "setColor:"
- "setColor:toSubstring:"
- "setColorMode:animated:"
- "setConfirmCellularPlanTransfer:"
- "setConfirmTextView:"
- "setConfirmationCodeRequired:"
- "setConfirmationCodeViewController:"
- "setConstant:"
- "setContentConfiguration:"
- "setContentHuggingPriority:forAxis:"
- "setContentInset:"
- "setContentOffset:"
- "setContinueAction:"
- "setContinueButton:"
- "setCornerRadius:"
- "setCrossPlatformTransferItems:"
- "setCrossPlatformTransferPlanSelected:"
- "setCtClient:"
- "setCurrentItemsForIMessage:"
- "setCurrentTitle:"
- "setCustomImage:withAlignmentEdgeInsets:"
- "setCustomLabel:"
- "setCustomView:"
- "setCutoutView:"
- "setDanglingPlanItem:"
- "setDanglingPlanItems:"
- "setDataDetectorTypes:"
- "setDataFallbackEnabled:forIccid:"
- "setDataSource:"
- "setDateStyle:"
- "setDctDelegate:"
- "setDctInfo:"
- "setDctPrewarmSucceded:"
- "setDeclineButton:"
- "setDefaultNavigationItems:"
- "setDefaultVoiceIccid:"
- "setDefaultVoiceItem:"
- "setDefaults"
- "setDelegate:"
- "setDescriptionLabel:"
- "setDescriptors:"
- "setDetailLabelConstraints:"
- "setDetailText:"
- "setDetails:"
- "setDidProcessDCTCode:"
- "setDidUserClickContinue:"
- "setDirectionalLayoutMargins:"
- "setDisable"
- "setDisableActions:"
- "setDismissButtonAction:"
- "setDismissButtonStyle:"
- "setDismissCause:"
- "setDismissalType:"
- "setDismissingViewController:"
- "setDispatchQueue:"
- "setDisplayPlan:"
- "setDisplayedDeviceIDs:"
- "setDoneAction:"
- "setDoneButton:"
- "setESIMInstallFromWebsheetFlowStarted:"
- "setESIMTravelState:"
- "setEditable:"
- "setEditableTextField:"
- "setEditing:"
- "setEnable:"
- "setEnabled:"
- "setEnablesReturnKeyAutomatically:"
- "setEnablingIccid:"
- "setEndpoint:"
- "setEnterDetailsManuallyButton:"
- "setEntersReaderIfAvailable:"
- "setEntryPoint:"
- "setEstimatedRowHeight:"
- "setEventHandler:"
- "setExposureMode:"
- "setExposurePointOfInterest:"
- "setExternalizedContext:"
- "setFailureWebsheetError:"
- "setFillColor:"
- "setFirstLabel:"
- "setFirstViewController:"
- "setFirstViewControllerCallback:"
- "setFirstViewControllerInstance:"
- "setFlowType:"
- "setFocusMode:"
- "setFocusPointOfInterest:"
- "setFollowDirections:"
- "setFont:"
- "setFooter:"
- "setForceDualSIMSetup:"
- "setFormatedDescriptor:"
- "setFragment:"
- "setFrame:"
- "setGlyphView:"
- "setGroup:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHandlerForButtonName:handler:"
- "setHandlerForElementName:handler:"
- "setHasBackButton:"
- "setHasContinueButton:"
- "setHasDoneButton:"
- "setHasProvisioningServiceImpact:"
- "setHasProvisioningServiceImpactMap:"
- "setHasTransferablePlan:"
- "setHeightAnchor:"
- "setHidden:"
- "setHidesBackButton:"
- "setHidesBackButton:animated:"
- "setHidesWhenStopped:"
- "setHost:"
- "setHostViewController:"
- "setIccid:"
- "setIccidToEnable:"
- "setIcon:"
- "setIdleTimerDisabled:"
- "setImage:"
- "setImgView:"
- "setInBuddy:"
- "setIndicatorView:"
- "setInitialLabel:"
- "setInjectedBundleURL:"
- "setInputAccessoryView:"
- "setInstallBucketSubtitle:"
- "setInstallBucketTitle:"
- "setInstallError:"
- "setInstallInfos:"
- "setInstallationEndTime:"
- "setInstallationStartTime:"
- "setInstallingPlanInfos:"
- "setInstallingTransferPlan:"
- "setInstruction:"
- "setIsAccessibilityElement:"
- "setIsActivationPolicyMismatch:"
- "setIsAuthenticationCompleted:"
- "setIsAvailableOptionsQueryCompleted:"
- "setIsCancelButtonTapped:"
- "setIsCancelTapped:"
- "setIsCarrierDirectAuthItemSelected:"
- "setIsCarrierSetupItemSelected:"
- "setIsCrossPlatformButtonTapped:"
- "setIsD2dDone:"
- "setIsDataOnly:"
- "setIsDataOnlySelected:"
- "setIsDeviceIdentifierPresent:"
- "setIsDisabled:"
- "setIsDisembarkUIRequired:"
- "setIsDtoEvaluationRequired:"
- "setIsDtoEvaluationSucceeded:"
- "setIsDualSIMConfig:"
- "setIsDualeSIMCapablityLoss:"
- "setIsEOnly:"
- "setIsEnterManuallyTapped:"
- "setIsExistingPlanTapped:"
- "setIsExternalizedContextSent:"
- "setIsFlexPolicyOn:"
- "setIsFlowCompleted:"
- "setIsFlowFinished:"
- "setIsForCrossPlatformTransfer:"
- "setIsFromDataTransferSession:"
- "setIsHiding:"
- "setIsIdleTimerDisabled:"
- "setIsLocalConvert:"
- "setIsLocalConvertFlow:"
- "setIsNFCDataSuccessTransfer:"
- "setIsOfferFallbackFlow:"
- "setIsOtherButtonTapped:"
- "setIsPhysical:"
- "setIsPostMigrationFlow:"
- "setIsPreInstalled:"
- "setIsPreSharedKeyPresent:"
- "setIsPreinstallingViewControllerActive:"
- "setIsProcessCanceled:"
- "setIsProxFlowShown:"
- "setIsProximityFlow:"
- "setIsProximityTransferButtonTapped:"
- "setIsPurchaseLocalPlanTapped:"
- "setIsRemotePeerClosed:"
- "setIsRemotePlan:"
- "setIsResumingAfterPause:"
- "setIsRoamingTapped:"
- "setIsSIMTypeSelectionShown:"
- "setIsScanButtonTapped:"
- "setIsSecureIntentRejected:"
- "setIsSecureIntentRequired:"
- "setIsSecureIntentSucceeded:"
- "setIsSelectedAsTravelSIM:"
- "setIsShown:"
- "setIsSkipButtonTapped:"
- "setIsSource:"
- "setIsSourceProxCardVisible:"
- "setIsStandaloneProximityFlow:"
- "setIsStandaloneProximityTransfer:"
- "setIsStartOverNeeded:"
- "setIsSyncWithTargetResults:"
- "setIsTransferButtonTapped:"
- "setIsTransferCompleted:"
- "setIsTransferListCellTapped:"
- "setIsTransferNotSupportedFromiPhone:"
- "setIsTravelEduButtonTapped:"
- "setIsUserInHomeCountry:"
- "setIsUsingPreSharedKey:"
- "setIsViewControllerPresented:"
- "setIsViewControllerPresenting:"
- "setItems:"
- "setKeyboardType:"
- "setLabel:"
- "setLabel:badge:"
- "setLabel:description:badge:"
- "setLabelForPlan:label:"
- "setLabelPickerViewController:"
- "setLabelWithNoBadge:"
- "setLastError:"
- "setLayoutMargins:"
- "setLeadingConstraint:"
- "setLeftBarButtonItem:"
- "setLeftBarButtonItem:animated:"
- "setLeftBarButtonItems:"
- "setLeftBarButtonItems:animated:"
- "setLeftConstraint:"
- "setLimit:"
- "setLineBreakMode:"
- "setLineWidth:"
- "setLockup:"
- "setLockupRequest:withDelegate:"
- "setLockupView:"
- "setLowDataMode:enable:"
- "setMagnificationFilter:"
- "setMainText:"
- "setMasksToBounds:"
- "setMaybeShowConfirmationCodePane:"
- "setMessageSession:"
- "setMetadataObjectTypes:"
- "setMetadataObjectsDelegate:queue:"
- "setMinimumFontSize:"
- "setModalInPresentation:"
- "setModalPresentationStyle:"
- "setModalTransitionStyle:"
- "setModel:"
- "setNFCTransferStatus:"
- "setName:"
- "setNavigationBarColor"
- "setNavigationBarHidden:animated:"
- "setNavigationController:"
- "setNavigationDelegate:"
- "setNavigationItems:"
- "setNeedOfferProximityTransferOption:"
- "setNeedOfferQRCodeOption:"
- "setNeedShow:"
- "setNeedShowTransferIntroPane:"
- "setNeedsLayout"
- "setNextViewController:"
- "setNfcAnimationView:"
- "setNfcAssertion:"
- "setNonMagnoliaCount:"
- "setNormalStateTitle:"
- "setNumSelectedPlansNotTransferredOut:"
- "setNumberOfDigits:"
- "setNumberOfLines:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOn:"
- "setOneTimeCodeAccelerator:"
- "setOneTimeCodeViewController:"
- "setOneTimePasscodePaneShown:"
- "setOptions:"
- "setOrientation:"
- "setOriginalEnabledPlans:"
- "setOtherOptionsButton:"
- "setOtpDetectorNeeded:"
- "setOtpEditor:"
- "setParentFlow:"
- "setPasscodeType:"
- "setPath:"
- "setPeerDeviceInfo:"
- "setPendingInstallItems:"
- "setPendingInteractiveViewControllers:"
- "setPendingLabel:forPlanItem:"
- "setPhoneNumber:"
- "setPhysicalButtonView:"
- "setPin:"
- "setPinCodeLabel:"
- "setPlaceHolderLabel:"
- "setPlaceholder:"
- "setPlan:"
- "setPlanEnablementState:"
- "setPlanError:"
- "setPlanInfo:"
- "setPlanInstallError:"
- "setPlanItem:"
- "setPlanItemBadges:"
- "setPlanItems:"
- "setPlanList:"
- "setPlanName:"
- "setPlanSetupType:"
- "setPlans:"
- "setPostdata:"
- "setPredefinedUserLabels:"
- "setPreferredAction:"
- "setPreferredContentMode:"
- "setPresentedViewController:"
- "setPrevTravelOnlySelection:"
- "setPrevViewController:"
- "setPreventConnectionHandoverAssertion:"
- "setPreviousLeftBarButtonItems:"
- "setPreviousRightBarButtonItems:"
- "setPrimaryAction:"
- "setPriority:"
- "setProcessPool:"
- "setProxTransferController:"
- "setProximitySetupState:"
- "setQrcodeBucketSubtitle:"
- "setQrcodeBucketTitle:"
- "setQrcodeDelegate:"
- "setQuery:"
- "setQueryItems:"
- "setQueryParamToTitle:"
- "setRadioImageView:"
- "setRectOfInterest:"
- "setRemoteDeviceClass:"
- "setRemoteInfo:"
- "setRemotePlanWebsheetContext:"
- "setRemoteUIController:"
- "setRequest:"
- "setRequestCompletion:"
- "setRequireDelayBluetoothConnection:"
- "setRequireSetup:"
- "setRequireStoreVisitItems:"
- "setResendOTPButton:"
- "setRetryAction:"
- "setReturnHome:"
- "setReturnKeyType:"
- "setRightBarButtonItem:"
- "setRightBarButtonItem:animated:"
- "setRightBarButtonItems:animated:"
- "setRightConstraint:"
- "setRoamingInfo:"
- "setRole:"
- "setRowHeight:"
- "setScanView:"
- "setScannerView:"
- "setScheme:"
- "setScreenOnChangedHandler:"
- "setScrollEdgeAppearance:"
- "setScrollEnabled:"
- "setScrollIndicatorInsets:"
- "setSecondLabel:"
- "setSecondaryButtonDetail:"
- "setSecondaryText:"
- "setSectionFooterHeight:"
- "setSectionHeaderHeight:"
- "setSecureIntentProxCard:"
- "setSecureTextEntry:"
- "setSelected:animated:"
- "setSelectedBackgroundView:"
- "setSelectedCarrierItem:"
- "setSelectedItems:"
- "setSelectedPlanItems:"
- "setSelectedPlanTransferStatus:"
- "setSelectedPlans:"
- "setSelectedPlansCount:"
- "setSelectedPlansFailedTransferCount:"
- "setSelectedSubscriptions:withCompletion:"
- "setSelectedTransferPlan:"
- "setSelectedTransferPlansCount:"
- "setSelectionStyle:"
- "setSeparatorColor:"
- "setSeparatorInset:"
- "setSeparatorStyle:"
- "setSession:"
- "setSessionConfiguration:"
- "setSessionPreset:"
- "setShadowColor:"
- "setShouldAdjustButtonTrayForKeyboard:"
- "setShouldAdjustScrollViewInsetForKeyboard:"
- "setShowCrossTransferOption:"
- "setShowDupLabelsFooter:"
- "setShowQRCodeOption:"
- "setShowSIMSetup:"
- "setShowTransferOption:"
- "setShowTransferredPane:"
- "setShowTravelEduOption:"
- "setShowsVerticalScrollIndicator:"
- "setSignupUserConsentResponse:"
- "setSimCapability:"
- "setSimsetupD2dInfo:"
- "setSkip:"
- "setSkipActivatingPane:"
- "setSkipButton:"
- "setSmartDashesType:"
- "setSmartInsertDeleteType:"
- "setSmartQuotesType:"
- "setSnapshot:"
- "setSortedPlanItemsWithPendingLabels:"
- "setSourceApplicationSecondaryIdentifier:"
- "setSourceIccid:"
- "setSourceOSVersion:"
- "setSourceOsVersion:"
- "setSpacing:"
- "setSpellCheckingType:"
- "setSpinner:"
- "setSpinnerContainer:"
- "setStackView:"
- "setStandardAppearance:"
- "setState:"
- "setState:animated:completionHandler:"
- "setStatus:"
- "setStoreVisitedMap:"
- "setStrokeColor:"
- "setStyle:"
- "setSubFlow:"
- "setSubFlowType:"
- "setSubFlowViewControllers:"
- "setSubscriptionContext:"
- "setSubtitle:"
- "setSupportDynamicDataSimSwitch:forIccid:completion:"
- "setSupportedRegionCodes:"
- "setSupportsSyncTransferResults:"
- "setSuppressesConnectionTerminationOnSystemChange:"
- "setSystemMonitor:"
- "setTableView:"
- "setTag:"
- "setTappedLearnMore:"
- "setTargetIccid:"
- "setTargetIccidHash:"
- "setTermsAndConditionsShown:"
- "setTermsAndConditionsViewController:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTextContentType:"
- "setTextEntryCompletionHandler:"
- "setTextFieldOffset:"
- "setTextView:"
- "setTimeStyle:"
- "setTimeoutInterval:"
- "setTimeoutReason:"
- "setTimer:"
- "setTintColor:"
- "setTitle:"
- "setTitle:forState:"
- "setTitleLabel:"
- "setToolbarHidden:animated:"
- "setToolbarItems:"
- "setTopConstraint:"
- "setTopViewController:"
- "setTrailingConstraint:"
- "setTransferBackOldItem:"
- "setTransferBackPlan:"
- "setTransferBackPlanPhoneNumber:"
- "setTransferIneligibleItems:"
- "setTransferIneligiblePlans:"
- "setTransferIneligibleViaCloudItems:"
- "setTransferItems:"
- "setTransferPlan:"
- "setTransferPlanDeviceID:"
- "setTransferPlans:"
- "setTransferStarted"
- "setTransferState:"
- "setTransferableHiddenInCloudFlowItems:"
- "setTransferablePlanOnSource:"
- "setTransform:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setTravelOnlySelected:"
- "setTravelSIM:"
- "setTriangleImageView:"
- "setUIDelegate:"
- "setUiDelegate:"
- "setUnlockAction:"
- "setUpeSIMLaunched:"
- "setUrl:"
- "setUseGMVNOAsTravelSIM:"
- "setUseLiveID:"
- "setUsePin:"
- "setUseTravelOnly:"
- "setUserConsentResponse:"
- "setUserConsentType:"
- "setUserContentController:"
- "setUserEnabledPlanInfos:"
- "setUserInPurchaseFlow:"
- "setUserInteractionEnabled:"
- "setUsingFirstViewControllerParadigm:"
- "setValue:forHTTPHeaderField:"
- "setValue:forKey:"
- "setVideoGravity:"
- "setVideoOrientation:"
- "setView:"
- "setViewAttributes:"
- "setViewControllers:animated:"
- "setViewDelegate:"
- "setViewDisappearHandler:"
- "setWaitForPhoneNumber:"
- "setWaitingStartTime:"
- "setWebsheetFlow:"
- "setWebsheetOptions:"
- "setWebsheetRootViewController:"
- "setWebsheetUrl:"
- "setWebsiteDataStore:"
- "setWhiteBalanceMode:"
- "setWithArray:"
- "setWithBackButton:"
- "set_isBeingUsedForCellularServiceBootstrap:"
- "set_sourceApplicationSecondaryIdentifier:"
- "settingsMode"
- "setupAssistantStyle"
- "setupCameraSession"
- "setupConstraints"
- "setupCoreTelephonyClientForRemoteSignup"
- "setupNavigationBarItems"
- "setupViewsWithTag:delegate:"
- "setupWithDelegate:indexPath:"
- "sha256"
- "shared"
- "sharedApplication"
- "sharedDefaultEvaluator"
- "sharedHardwareManagerWithNoUI"
- "sharedInstance"
- "sharedLockupViewGroup"
- "sharedManager"
- "shouldShowCarrierSetupPane"
- "shouldShowPlanSetup:"
- "shouldShowPlanSetupWithCompletion:"
- "shouldShowTransferPlans:sourceOSVersion:isPostMigrationFlow:transferItems:completion:"
- "shouldShowTransferredPane"
- "shouldShowTravelEducation:"
- "showActivityIndicatorWithStatus:"
- "showAlert"
- "showBluetoothOffAlertForCrossPlatformTransfer:withCloseHandler:"
- "showButtonsAvailable"
- "showButtonsBusy"
- "showDupLabelsFooter"
- "showFirstViewControllerWithHostController:completion:"
- "showLoadFailureAlert:error:"
- "showQRCodePane:"
- "showSIMSetup"
- "showSpinner"
- "showTransferredPane"
- "showTravelEduOption"
- "showsBusyIndicator"
- "signupUserConsentResponse"
- "simLessSubscriptionsDidChange"
- "simSetupFlowCompleted"
- "simSetupFlowCompleted:"
- "size"
- "sizeThatFits:"
- "sizeToFit"
- "sizeWithFont:constrainedToSize:lineBreakMode:"
- "skEventFromDictionary:"
- "skip"
- "skipActivatingPane"
- "skipButton"
- "snapshot"
- "snapshotViewAfterScreenUpdates:"
- "sortIndexesInDescending:"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "sortedPlanItemsWithPendingLabels"
- "sourceDevicesCount:"
- "sourceOSVersion"
- "sourceOsVersion"
- "spinner"
- "spinnerContainer"
- "spinnerStartAnimating"
- "spinnerStopAnimating"
- "springBoardLockStateNotifyToken"
- "stackView"
- "startAnimating"
- "startOverWithFirstViewController:"
- "startRunning"
- "startScanning"
- "startSharingIdentity:"
- "startSpinnerInNavigationItem:withIdentifier:"
- "startTimer:"
- "stopAnimating"
- "stopRunning"
- "stopSharingIdentity"
- "stopSpinnerForIdentifier:"
- "stopSpinnerInNavigationItem:withIdentifier:"
- "storeVisitedMap"
- "string"
- "stringByAppendingString:"
- "stringByReplacingCharactersInRange:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringFromDate:"
- "stringFromNumber:"
- "stringValue"
- "stringWithContentsOfFile:encoding:error:"
- "stringWithFormat:"
- "stringWithString:"
- "subFlow"
- "subFlowType"
- "subFlowViewControllers"
- "subarrayWithRange:"
- "submitAutoReconnectionDetails"
- "submitAutoReconnectionDetails:"
- "submitAutoReconnectionDetails:completion:"
- "submitPlanSetupDetails:"
- "submitPlanSetupDetails:completion:"
- "submitSimSetupUsage:"
- "submitSimSetupUsage:completion:"
- "subscriptionContext"
- "subscriptionInfoDidChange"
- "subscriptionSlot"
- "subscriptions"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "subviews"
- "superclass"
- "superlayer"
- "supportedTransferOption"
- "supportsAVCaptureSessionPreset:"
- "supportsHydraWithError:"
- "supportsSyncTransferResults"
- "switchControl"
- "systemBackgroundColor"
- "systemBlueColor"
- "systemFontOfSize:"
- "systemGray6Color"
- "systemGrayColor"
- "systemGroupedBackgroundColor"
- "systemImageNamed:"
- "systemImageNamed:withConfiguration:"
- "systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:"
- "systemLightGrayColor"
- "systemMonitor"
- "systemYellowColor"
- "tabIDForAutoFill"
- "tableView"
- "tableView:accessoryButtonTappedForRowWithIndexPath:"
- "tableView:accessoryTypeForRowWithIndexPath:"
- "tableView:canEditRowAtIndexPath:"
- "tableView:canFocusRowAtIndexPath:"
- "tableView:canMoveRowAtIndexPath:"
- "tableView:canPerformAction:forRowAtIndexPath:withSender:"
- "tableView:canPerformPrimaryActionForRowAtIndexPath:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:commitEditingStyle:forRowAtIndexPath:"
- "tableView:contextMenuConfigurationForRowAtIndexPath:point:"
- "tableView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:didDeselectRowAtIndexPath:"
- "tableView:didEndDisplayingCell:forRowAtIndexPath:"
- "tableView:didEndDisplayingFooterView:forSection:"
- "tableView:didEndDisplayingHeaderView:forSection:"
- "tableView:didEndEditingRowAtIndexPath:"
- "tableView:didHighlightRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:didUnhighlightRowAtIndexPath:"
- "tableView:didUpdateFocusInContext:withAnimationCoordinator:"
- "tableView:editActionsForRowAtIndexPath:"
- "tableView:editingStyleForRowAtIndexPath:"
- "tableView:estimatedHeightForFooterInSection:"
- "tableView:estimatedHeightForHeaderInSection:"
- "tableView:estimatedHeightForRowAtIndexPath:"
- "tableView:heightForFooterInSection:"
- "tableView:heightForHeaderInSection:"
- "tableView:heightForRowAtIndexPath:"
- "tableView:indentationLevelForRowAtIndexPath:"
- "tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:moveRowAtIndexPath:toIndexPath:"
- "tableView:numberOfRowsInSection:"
- "tableView:performAction:forRowAtIndexPath:withSender:"
- "tableView:performPrimaryActionForRowAtIndexPath:"
- "tableView:previewForDismissingContextMenuWithConfiguration:"
- "tableView:previewForHighlightingContextMenuWithConfiguration:"
- "tableView:sectionForSectionIndexTitle:atIndex:"
- "tableView:selectionFollowsFocusForRowAtIndexPath:"
- "tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:shouldHighlightRowAtIndexPath:"
- "tableView:shouldIndentWhileEditingRowAtIndexPath:"
- "tableView:shouldShowMenuForRowAtIndexPath:"
- "tableView:shouldSpringLoadRowAtIndexPath:withContext:"
- "tableView:shouldUpdateFocusInContext:"
- "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
- "tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:"
- "tableView:titleForFooterInSection:"
- "tableView:titleForHeaderInSection:"
- "tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:viewForFooterInSection:"
- "tableView:viewForHeaderInSection:"
- "tableView:willBeginEditingRowAtIndexPath:"
- "tableView:willDeselectRowAtIndexPath:"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "tableView:willDisplayContextMenuWithConfiguration:animator:"
- "tableView:willDisplayFooterView:forSection:"
- "tableView:willDisplayHeaderView:forSection:"
- "tableView:willEndContextMenuInteractionWithConfiguration:animator:"
- "tableView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "tableView:willSelectRowAtIndexPath:"
- "tableViewDidEndMultipleSelectionInteraction:"
- "tableViewOM"
- "tag"
- "takeScreenShot:"
- "tappedLearnMore"
- "target"
- "targetIccid"
- "targetIccidHash"
- "templateSession"
- "termsAndConditionsShown"
- "termsAndConditionsViewController"
- "text"
- "textColorForRemotePlan:"
- "textField:editMenuForCharactersInRange:suggestedActions:"
- "textField:editMenuForCharactersInRanges:suggestedActions:"
- "textField:insertInputSuggestion:"
- "textField:shouldChangeCharactersInRange:replacementString:"
- "textField:shouldChangeCharactersInRanges:replacementString:"
- "textField:willDismissEditMenuWithAnimator:"
- "textField:willPresentEditMenuWithAnimator:"
- "textFieldDidBeginEditing:"
- "textFieldDidChangeSelection:"
- "textFieldDidEndEditing:"
- "textFieldDidEndEditing:reason:"
- "textFieldShouldBeginEditing:"
- "textFieldShouldClear:"
- "textFieldShouldEndEditing:"
- "textFieldShouldReturn:"
- "textLabel"
- "textProperties"
- "textView"
- "timer"
- "timerWithTimeInterval:target:selector:userInfo:repeats:"
- "titleLabel"
- "topAnchor"
- "topConstraint"
- "topViewController"
- "trailingAnchor"
- "trailingConstraint"
- "traitCollection"
- "traitCollectionWithUserInterfaceStyle:"
- "transfer plans [%lu] : %@ @%s"
- "transfer plans: %lu, store visit:%lu, hidden: %lu, ineligible: %lu @%s"
- "transfer plans: %lu, store visit:%lu, ineligible: %lu @%s"
- "transferAttributes"
- "transferBackOldItem"
- "transferBackPlan"
- "transferBackPlanPhoneNumber"
- "transferCapability"
- "transferCapabilityForMessage"
- "transferEndpoint"
- "transferEventUpdate:"
- "transferIneligibleItems"
- "transferIneligiblePlans"
- "transferIneligibleViaCloudItems"
- "transferItems"
- "transferOptions"
- "transferPlan"
- "transferPlan:fromDevice:completionHandler:"
- "transferPlanDeviceID"
- "transferPlanListWithCompletion:"
- "transferPlanWithIdentifier:fromDevice:completionHandler:"
- "transferPlans"
- "transferPlans:fromDevice:completionHandler:"
- "transferPlansWithIdentifier:fromDevice:completionHandler:"
- "transferState"
- "transferViaQRCode"
- "transferableHiddenInCloudFlowItems"
- "transferablePlanCarriers:"
- "transferablePlanOnSource"
- "transferablePlans:"
- "transferredStatus"
- "travelOnlySelected"
- "travelSIM"
- "trialExpirationDate"
- "triangleImageView"
- "unformattedPhoneNumber"
- "unlockAction"
- "unlockForConfiguration"
- "unregisteredSelectedPlanItems:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updateBusyText:"
- "updateCellularPlanProperties:appName:appType:completionHandler:"
- "updateFooterView"
- "updateImage"
- "updateInstallationStatus:forPlanID:"
- "updateOtpState:"
- "updatePIN:"
- "updatePlanItem"
- "updateProvisioningError:targetIccidHash:"
- "updateRasterizationScale:"
- "updateRectOfInterest"
- "updateSIMTransferStatus:"
- "updateSecureIntentData:isDTOEvaluationFailed:"
- "updateSecureIntentData:isDTOEvaluationFailed:error:"
- "updateSourceProxCardState:"
- "updateTableHeightAnchor"
- "updateTargetIccidInfo:"
- "updateText"
- "updateText:"
- "updateViewConstraints"
- "uppercaseString"
- "uppercaseStringWithLocale:"
- "useGMVNOAsTravelSIM"
- "useLiveID"
- "usePin"
- "useTravelOnly"
- "user explicitly mentioned he/she has not visited store, plan (%@) is not able to transfer for now. @%s"
- "user explicitly notify having not visited store, plan (%@) is not able to transfer for now. @%s"
- "userConsentResponse"
- "userConsentType"
- "userContentController:didReceiveScriptMessage:"
- "userDidExitWebsheetFlowForPlan:"
- "userDidProvideResponse:confirmationCode:forPlan:isRemote:completion:"
- "userDidTapCancel"
- "userEnabledPlanInfos"
- "userInfo"
- "userInteractionEnabled"
- "userInterfaceIdiom"
- "userInterfaceStyle"
- "userLabel"
- "userSignupInitiatedOrFailed"
- "usesInterfaceType:"
- "usesType"
- "usingBootstrapDataService"
- "usingBootstrapDataService:"
- "usingFirstViewControllerParadigm"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8i16"
- "v24@0:8@\"<PRXCardContentProviding>\"16"
- "v24@0:8@\"<TSSIMSetupFlowDelegate>\"16"
- "v24@0:8@\"ASCLockupView\"16"
- "v24@0:8@\"CBCentralManager\"16"
- "v24@0:8@\"CTDisplayPlanList\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"OBTrayButton\"16"
- "v24@0:8@\"RemoteUIController\"16"
- "v24@0:8@\"SFSafariViewController\"16"
- "v24@0:8@\"SSSpinner\"16"
- "v24@0:8@\"UIPresentationController\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITableView\"16"
- "v24@0:8@\"UITextField\"16"
- "v24@0:8@\"UIViewController\"16"
- "v24@0:8@\"WKWebView\"16"
- "v24@0:8@\"_SFFormAutoFillController\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"SFSafariViewController\"16B24"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@\"_SFFormAutoFillController\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16q20"
- "v32@0:8@\"ASCLockupView\"16@\"NSError\"24"
- "v32@0:8@\"ASCLockupView\"16@\"NSString\"24"
- "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
- "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSArray\"16@\"NSError\"24"
- "v32@0:8@\"NSArray\"16@?<v@?BB>24"
- "v32@0:8@\"NSArray\"16@?<v@?BBi>24"
- "v32@0:8@\"NSDictionary\"16@?<v@?B>24"
- "v32@0:8@\"NSError\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"RemoteUIController\"16@\"NSArray\"24"
- "v32@0:8@\"RemoteUIController\"16@\"NSError\"24"
- "v32@0:8@\"RemoteUIController\"16@\"NSHTTPURLResponse\"24"
- "v32@0:8@\"RemoteUIController\"16@\"NSMutableURLRequest\"24"
- "v32@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24"
- "v32@0:8@\"RemoteUIController\"16@\"UINavigationController\"24"
- "v32@0:8@\"SFSafariViewController\"16@\"NSURL\"24"
- "v32@0:8@\"UIPresentationController\"16@\"UIPresentationController\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"UITextField\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"UITextField\"16q24"
- "v32@0:8@\"WKUserContentController\"16@\"WKScriptMessage\"24"
- "v32@0:8@\"WKWebView\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"WKWebView\"16@\"<_WKFormInputSession>\"24"
- "v32@0:8@\"WKWebView\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"WKWebView\"16@\"UIViewController\"24"
- "v32@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24"
- "v32@0:8@\"WKWebView\"16@\"WKNavigation\"24"
- "v32@0:8@\"_SFFormAutoFillController\"16@\"WBSAutoFillInternalFeedbackDiagnosticsData\"24"
- "v32@0:8@\"_SFFormAutoFillController\"16@?<v@?B@\"LAContext\">24"
- "v32@0:8@16:24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8Q16@24"
- "v32@0:8Q16@?24"
- "v32@0:8^@16^@24"
- "v32@0:8q16@24"
- "v36@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24B32"
- "v36@0:8@\"UINavigationController\"16@\"UIViewController\"24B32"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@?28"
- "v36@0:8@16B24q28"
- "v40@0:8@\"AVCaptureOutput\"16@\"NSArray\"24@\"AVCaptureConnection\"32"
- "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
- "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
- "v40@0:8@\"RemoteUIController\"16@\"NSError\"24@\"NSURLRequest\"32"
- "v40@0:8@\"RemoteUIController\"16@\"NSHTTPURLResponse\"24@\"NSURLRequest\"32"
- "v40@0:8@\"RemoteUIController\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"RemoteUIController\"16@\"RUIObjectModel\"24^Q32"
- "v40@0:8@\"UIPresentationController\"16q24@\"<UIViewControllerTransitionCoordinator>\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UITableView\"16@\"UIView\"24q32"
- "v40@0:8@\"UITableView\"16q24@\"NSIndexPath\"32"
- "v40@0:8@\"WKWebView\"16@\"<_WKFocusedElementInfo>\"24@?<v@?B>32"
- "v40@0:8@\"WKWebView\"16@\"NSString\"24@?<v@?q>32"
- "v40@0:8@\"WKWebView\"16@\"NSURLAuthenticationChallenge\"24@?<v@?B>32"
- "v40@0:8@\"WKWebView\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"WKWebView\"16@\"UITextSuggestion\"24@\"<_WKFormInputSession>\"32"
- "v40@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24@?<v@?@\"UIContextMenuConfiguration\">32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigation\"24@\"NSError\"32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@\"WKDownload\"32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@?<v@?q>32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigationResponse\"24@\"WKDownload\"32"
- "v40@0:8@\"WKWebView\"16@\"WKNavigationResponse\"24@?<v@?q>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24^Q32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8B16B20@24@?32"
- "v40@0:8Q16^@24^@32"
- "v40@0:8q16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8q16@24@?32"
- "v40@0:8{CGSize=dd}16@32"
- "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
- "v48@0:8@\"RemoteUIController\"16@\"NSMutableURLRequest\"24@\"NSURLResponse\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@\"WKWebView\"16@\"NSDictionary\"24@\"NSObject<NSSecureCoding>\"32@?<v@?>40"
- "v48@0:8@\"WKWebView\"16@\"NSString\"24@\"WKFrameInfo\"32@?<v@?>40"
- "v48@0:8@\"WKWebView\"16@\"NSString\"24@\"WKFrameInfo\"32@?<v@?B>40"
- "v48@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@\"WKWebpagePreferences\"32@?<v@?q@\"WKWebpagePreferences\">40"
- "v48@0:8@\"WKWebView\"16@\"WKOpenPanelParameters\"24@\"WKFrameInfo\"32@?<v@?@\"NSArray\">40"
- "v48@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24@\"WKFrameInfo\"32@?<v@?q>40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24q32@?40"
- "v48@0:8@16Q24^@32^@40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
- "v52@0:8@\"NSData\"16@\"NSArray\"24B32B36B40@?<v@?B>44"
- "v52@0:8@16@24B32@36@?44"
- "v52@0:8@16@24B32B36B40@?44"
- "v52@0:8@16@24d32B40@44"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@\"WKWebView\"16@\"NSString\"24@\"NSString\"32@\"WKFrameInfo\"40@?<v@?@\"NSString\">48"
- "v56@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24@\"WKFrameInfo\"32q40@?<v@?q>48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32q40@?48"
- "v56@0:8@16B24B28@32B40B44@?48"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56"
- "v64@0:8@\"WKWebView\"16@\"NSDictionary\"24@\"WKFrameInfo\"32@\"WKFrameInfo\"40@\"NSObject<NSSecureCoding>\"48@?<v@?>56"
- "v64@0:8@16@24@32@40@48@56"
- "v64@0:8@16@24@32@40@48@?56"
- "v68@0:8@16Q24Q32@40^@48^@56B64"
- "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64"
- "v72@0:8@16@24@32@40@48@56@64"
- "v80@0:8@\"WKWebView\"16@\"NSDictionary\"24@\"WKFrameInfo\"32@\"WKFrameInfo\"40@\"NSObject<NSSecureCoding>\"48@\"NSURL\"56@\"NSString\"64@?<v@?>72"
- "v80@0:8@16@24@32@40@48@56@64@?72"
- "validateProximityTransfer:pin:completion:"
- "valueForKey:"
- "verifyPIN:"
- "view"
- "viewController"
- "viewControllerDidComplete:"
- "viewControllers"
- "viewDelegate"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "visibleCells"
- "visibleViewController"
- "waitForPhoneNumber"
- "waitForResponse:"
- "waitingStartTime"
- "webView:authenticationChallenge:shouldAllowDeprecatedTLS:"
- "webView:commitPreviewingViewController:"
- "webView:contextMenuConfigurationForElement:completionHandler:"
- "webView:contextMenuDidEndForElement:"
- "webView:contextMenuForElement:willCommitWithAnimator:"
- "webView:contextMenuWillPresentForElement:"
- "webView:createWebViewWithConfiguration:forNavigationAction:windowFeatures:"
- "webView:decidePolicyForNavigationAction:decisionHandler:"
- "webView:decidePolicyForNavigationAction:preferences:decisionHandler:"
- "webView:decidePolicyForNavigationResponse:decisionHandler:"
- "webView:didCommitNavigation:"
- "webView:didFailNavigation:withError:"
- "webView:didFailProvisionalNavigation:withError:"
- "webView:didFinishNavigation:"
- "webView:didReceiveAuthenticationChallenge:completionHandler:"
- "webView:didReceiveServerRedirectForProvisionalNavigation:"
- "webView:didStartProvisionalNavigation:"
- "webView:insertInputSuggestion:"
- "webView:navigationAction:didBecomeDownload:"
- "webView:navigationResponse:didBecomeDownload:"
- "webView:previewingViewControllerForElement:defaultActions:"
- "webView:requestDeviceOrientationAndMotionPermissionForOrigin:initiatedByFrame:decisionHandler:"
- "webView:requestMediaCapturePermissionForOrigin:initiatedByFrame:type:decisionHandler:"
- "webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:completionHandler:"
- "webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:completionHandler:"
- "webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:completionHandler:"
- "webView:runOpenPanelWithParameters:initiatedByFrame:completionHandler:"
- "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "webView:shouldPreviewElement:"
- "webView:showLockdownModeFirstUseMessage:completionHandler:"
- "webView:willDismissEditMenuWithAnimator:"
- "webView:willPresentEditMenuWithAnimator:"
- "webViewDidClose:"
- "webViewWebContentProcessDidTerminate:"
- "websheetFlow"
- "websheetInfoForIccid:completion:"
- "websheetInfoForPlan:completion:"
- "websheetInfoForPlan:inBuddy:completion:"
- "websheetOptions"
- "websheetRootViewController"
- "websheetUrl"
- "whiteColor"
- "whitespaceCharacterSet"
- "widthAnchor"
- "willSubmitFormValues:userObject:submissionHandler:"
- "window"
- "withBackButton"
- "zone"
- "{CGPoint=dd}24@0:8@16"
- "{CGPoint=dd}32@0:8{CGPoint=dd}16"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}40@0:8{CGSize=dd}16f32f36"
- "\xd4\xd1"

```
