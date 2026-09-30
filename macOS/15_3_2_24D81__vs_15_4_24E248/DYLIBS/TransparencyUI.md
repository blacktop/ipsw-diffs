## TransparencyUI

> `/System/Library/PrivateFrameworks/TransparencyUI.framework/Versions/A/TransparencyUI`

```diff

-1218.80.18.0.0
-  __TEXT.__text: 0x3fc60
+1218.100.244.0.0
+  __TEXT.__text: 0x405e8
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x234c
+  __TEXT.__objc_methlist: 0x2bf4
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x500c
   __TEXT.__oslogstring: 0x2573
-  __TEXT.__gcc_except_tab: 0x568
+  __TEXT.__gcc_except_tab: 0x578
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0xea0
+  __TEXT.__unwind_info: 0x1518
   __TEXT.__objc_classname: 0x595
-  __TEXT.__objc_methname: 0x7bcc
+  __TEXT.__objc_methname: 0x7bd0
   __TEXT.__objc_methtype: 0x1924
-  __TEXT.__objc_stubs: 0x5200
+  __TEXT.__objc_stubs: 0x51e0
   __DATA_CONST.__got: 0x500
   __DATA_CONST.__const: 0x220
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c50
+  __DATA_CONST.__objc_selrefs: 0x1fa0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0x39e0
   __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x8350
+  __AUTH_CONST.__objc_const: 0x7350
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A589DEE4-8D8B-380D-9AAC-363612A5FC05
-  Functions: 1521
-  Symbols:   3650
-  CStrings:  2471
+  UUID: C818166F-81D8-316C-83ED-C70B0B5B1DB2
+  Functions: 1906
+  Symbols:   4027
+  CStrings:  2470
 
Symbols:
+ +[TUIUtils isHSA2].cold.2
+ +[TUIUtils isMismatchedAccountError:].cold.2
+ +[TUIUtils isNetworkError:].cold.2
+ +[TUIUtils isTransparencyFeatureEnabled:].cold.3
+ +[TUIUtils isTransparencyFeatureEnabled:].cold.4
+ -[TUIAIDPPOptInSpecifierProvider dealloc].cold.2
+ -[TUIAIDPPOptInSpecifierProvider initWithAccountManager:].cold.2
+ -[TUIAIDPPOptInSpecifierProvider initWithAccountManager:].cold.3
+ -[TUIAIDPPOptInSpecifierProvider specifiers].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _accountKeyUIFeatureEnabled].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _beginObservingTransparencyStatusChangedNotification].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _checkKTStatus:].cold.1
+ -[TUIAIDPPOptInSpecifierViewController _deviceList].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupStackView].cold.3
+ -[TUIAIDPPOptInSpecifierViewController _setupStackView].cold.4
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateCDPError].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateCDPWaiting].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateDeviceError].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateIDSDisabled].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateNoError].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateNoIDSAppleID].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateOptInPendingCDPError].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateOptInPendingCDPWaiting].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateOtherError].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateTemporaryError].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _setupUIStateTreeReset].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _stopObservingTransparencyStatusChangedNotification].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _systemFailureUIFeatureEnabled].cold.2
+ -[TUIAIDPPOptInSpecifierViewController _transparencyStatusChangedNotificationHandler:].cold.1
+ -[TUIAIDPPOptInSpecifierViewController dealloc].cold.2
+ -[TUIAIDPPOptInSpecifierViewController deviceListModified:].cold.2
+ -[TUIAIDPPOptInSpecifierViewController deviceListModified:].cold.3
+ -[TUIAIDPPOptInSpecifierViewController deviceListModified:].cold.4
+ -[TUIAIDPPOptInSpecifierViewController initWithAccountManager:].cold.3
+ -[TUIAIDPPOptInSpecifierViewController initWithAccountManager:].cold.4
+ -[TUIAIDPPOptInSpecifierViewController loadView].cold.2
+ -[TUIAIDPPOptInSpecifierViewController optInFlowResultWithStateUpdate].cold.1
+ -[TUIAIDPPOptInSpecifierViewController refreshDevices].cold.2
+ -[TUIAIDPPOptInSpecifierViewController viewDidAppear].cold.2
+ -[TUIAIDPPOptInSpecifierViewController viewDidDisappear].cold.2
+ -[TUIAIDPPOptInSpecifierViewController viewDidLoad].cold.2
+ -[TUIAppleAccountManager initWithAccountStore:].cold.2
+ -[TUIAppleAccountManager silentRenewAppleAccountWithCompletionHandler:].cold.2
+ -[TUIDeviceDetailsViewController _deviceList].cold.2
+ -[TUIDeviceDetailsViewController _updateDevicesWithIssuesList:].cold.1
+ -[TUIDeviceDetailsViewController _updateDevicesWithIssuesList:].cold.2
+ -[TUIDeviceDetailsViewController _updateDevicesWithIssuesList:].cold.3
+ -[TUIDeviceDetailsViewController _updateDevicesWithIssuesList:].cold.4
+ -[TUIDeviceDetailsViewController deviceListModified:].cold.2
+ -[TUIDeviceDetailsViewController initWithAccountManager:devicesWithIssuesIdentifiers:].cold.1
+ -[TUIDeviceDetailsViewController viewDidLoad].cold.2
+ -[TUIIDMSDeviceSource mapDeviceWithMissing:aaDevices:].cold.2
+ -[TUIKTAppIntentsData init].cold.2
+ -[TUIKTAppIntentsData publicVerificationCodeWithCompletion:].cold.2
+ -[TUIKTAppIntentsData statusWithCompletion:].cold.2
+ -[TUIKTAppIntentsData statusWithCompletion:].cold.3
+ -[TUIKTConversationPaneController _otherPartyAccountKeyFieldClicked:].cold.2
+ -[TUIKTConversationPaneController _selfAccountKeyFieldClicked:].cold.2
+ -[TUIKTConversationPaneController codeNoMatchButtonClicked:].cold.2
+ -[TUIKTConversationPaneController copySelfKeyClicked:].cold.2
+ -[TUIKTConversationPaneController displayAll].cold.2
+ -[TUIKTConversationPaneController displayAll].cold.3
+ -[TUIKTConversationPaneController displayCode:].cold.2
+ -[TUIKTConversationPaneController doneClicked:].cold.2
+ -[TUIKTConversationPaneController initForMembers:options:].cold.2
+ -[TUIKTConversationPaneController initForMembers:options:].cold.3
+ -[TUIKTConversationPaneController initWithPeer:peerTransparencyUuid:peerAddress:].cold.1
+ -[TUIKTConversationPaneController loadView].cold.2
+ -[TUIKTConversationPaneController markAsVerifiedClicked:].cold.2
+ -[TUIKTConversationPaneController reportToAppleFeatureEnabled].cold.2
+ -[TUIKTConversationPaneController showHideKeyBoxes:].cold.2
+ -[TUIKTConversationPaneController showInfoAlert:].cold.2
+ -[TUIKTConversationPaneController showKeysLinkClicked:].cold.2
+ -[TUIKTConversationPaneController showNoMatchAlert].cold.2
+ -[TUIKTConversationPaneController textView:clickedOnLink:atIndex:].cold.2
+ -[TUIKTConversationPaneController updateUI].cold.2
+ -[TUIKTConversationPaneController verifyContact:peerPublicAccountIdentity:].cold.1
+ -[TUIKTConversationPaneController verifyContact:peerPublicAccountIdentity:].cold.2
+ -[TUIKTConversationPaneController verifyContact:peerPublicAccountIdentity:].cold.3
+ -[TUIKTConversationPaneController viewDidAppear].cold.2
+ -[TUIKTConversationPaneController viewDidDisappear].cold.3
+ -[TUIKTConversationPaneController viewDidDisappear].cold.4
+ -[TUIKTConversationPaneController viewDidLoad].cold.2
+ -[TUIKTConversationPaneController viewWillAppear].cold.2
+ -[TUIKTConversationPaneController viewWillDisappear].cold.2
+ -[TUIKTConversationPaneController windowDidBecomeKey:].cold.2
+ -[TUIKTConversationPaneController windowDidResignKey:].cold.2
+ -[TUIKTConversationViewController displayCodeSheet].cold.2
+ -[TUIKTConversationViewController initWithPeer:transparencyUuid:peerAddress:options:].cold.1
+ -[TUIKTConversationViewController loadView].cold.2
+ -[TUIKTConversationViewController sheetEnded].cold.2
+ -[TUIKTConversationViewController updateLinkText].cold.2
+ -[TUIKTConversationViewController verifyConversationClicked:].cold.2
+ -[TUIKTConversationViewController viewDidAppear].cold.2
+ -[TUIKTConversationViewController viewDidDisappear].cold.3
+ -[TUIKTConversationViewController viewDidDisappear].cold.4
+ -[TUIKTConversationViewController viewDidLoad].cold.2
+ -[TUIKTDeviceErrorViewController endWebView:].cold.2
+ -[TUIKTDeviceErrorViewController initWithAccountManager:devicesWithErrors:].cold.1
+ -[TUIKTDeviceErrorViewController loadFailed:].cold.2
+ -[TUIKTDeviceErrorViewController removeDevicesClicked:].cold.1
+ -[TUIKTDeviceErrorViewController resizeModalSheet:].cold.2
+ -[TUIKTDeviceErrorViewController shouldHideCancelButton].cold.2
+ -[TUIKTDeviceErrorViewController sizeChangedFrom:toSize:webViewName:callback:].cold.2
+ -[TUIKTDeviceErrorViewController skipAndContinueSignIn].cold.2
+ -[TUIKTDeviceErrorViewController viewDetailsPressed:].cold.1
+ -[TUIKTDeviceErrorViewController viewDetailsPressed:].cold.2
+ -[TUIKTDeviceErrorViewController viewDetailsPressed:].cold.3
+ -[TUIKTFooterViewController learnMoreButtonPressed:].cold.2
+ -[TUIKTFooterViewController loadView].cold.2
+ -[TUIKTLearnMorePresenter dealloc].cold.2
+ -[TUIKTLearnMorePresenter init].cold.2
+ -[TUIKTLearnMorePresenter presentWithPresentingWindow:].cold.3
+ -[TUIKTLearnMorePresenter presentWithPresentingWindow:].cold.4
+ -[TUIKTLearnMoreRemoteViewControllerHost dealloc].cold.2
+ -[TUIKTLearnMoreRemoteViewControllerHost loadView].cold.2
+ -[TUIKTLearnMoreRemoteViewControllerHost privacySheetDidDismissWithError:reply:].cold.3
+ -[TUIKTLearnMoreRemoteViewControllerHost privacySheetDidDismissWithError:reply:].cold.4
+ -[TUIKTLearnMoreRemoteViewControllerHost viewServiceDidTerminateWithError:].cold.2
+ -[TUIKTLearnMoreViewController _connectToRemoteServiceWithCompletion:].cold.2
+ -[TUIKTLearnMoreViewController _showRemoteServicePrivacySheet].cold.2
+ -[TUIKTLearnMoreViewController closeRemoteServiceConnection].cold.2
+ -[TUIKTLearnMoreViewController dealloc].cold.2
+ -[TUIKTLearnMoreViewController loadView].cold.2
+ -[TUIKTLearnMoreViewController presentWithPresentingWindow:].cold.2
+ -[TUIKTLearnMoreViewController viewDidAppear].cold.2
+ -[TUIKTOptInStatusViewController _changeOptInState:].cold.2
+ -[TUIKTOptInStatusViewController _messagesSettingsButtonPressed].cold.2
+ -[TUIKTOptInStatusViewController _optInSwitchToggled].cold.1
+ -[TUIKTOptInStatusViewController _reportToAppleButtonPressed].cold.2
+ -[TUIKTOptInStatusViewController _resetButtonPressed].cold.2
+ -[TUIKTOptInStatusViewController _showMessagesSettings].cold.2
+ -[TUIKTOptInStatusViewController _showOptOutConfirmationAlertWithCompletion:].cold.2
+ -[TUIKTOptInStatusViewController _showResetConfirmationAlertWithCompletion:].cold.2
+ -[TUIKTOptInStatusViewController _turnOffButtonPressed].cold.2
+ -[TUIKTOptInStatusViewController _updateAppleIDButtonPressed].cold.2
+ -[TUIKTOptInStatusViewController _updateAppleID].cold.2
+ -[TUIKTOptInStatusViewController activeConnectionChanged].cold.2
+ -[TUIKTOptInStatusViewController configureStatusViewForErrorState].cold.2
+ -[TUIKTOptInStatusViewController configureStatusViewForHappyState].cold.2
+ -[TUIKTOptInStatusViewController configureStatusViewForWaitingState].cold.2
+ -[TUIKTOptInStatusViewController dealloc].cold.2
+ -[TUIKTOptInStatusViewController dismissPendingPopupUI].cold.2
+ -[TUIKTOptInStatusViewController initWithAccountManager:stateManager:].cold.3
+ -[TUIKTOptInStatusViewController initWithAccountManager:stateManager:].cold.4
+ -[TUIKTOptInStatusViewController loadView].cold.2
+ -[TUIKTOptInStatusViewController optInFlowResultWithStateUpdate].cold.1
+ -[TUIKTOptInStatusViewController processOptInStateChange].cold.2
+ -[TUIKTOptInStatusViewController viewDidAppear].cold.2
+ -[TUIKTOptInStatusViewController viewDidAppear].cold.3
+ -[TUIKTOptInStatusViewController viewDidDisappear].cold.2
+ -[TUIKTOptInStatusViewController viewDidLoad].cold.2
+ -[TUIKTReportToAppleViewController _updateReportManager].cold.2
+ -[TUIKTReportToAppleViewController cancelButtonClicked:].cold.2
+ -[TUIKTReportToAppleViewController initWithContext:staticIdentityManager:].cold.1
+ -[TUIKTReportToAppleViewController loadView].cold.2
+ -[TUIKTReportToAppleViewController sendButtonClicked:].cold.2
+ -[TUIKTReportToAppleViewController showDetailsClicked:].cold.2
+ -[TUIKTReportToAppleViewController textView:clickedOnLink:atIndex:].cold.2
+ -[TUIKTReportToAppleViewController viewDidAppear].cold.2
+ -[TUIKTReportToAppleViewController viewDidLoad].cold.2
+ -[TUIKTSingleAccountViewController _accountKeyValueClicked:].cold.2
+ -[TUIKTSingleAccountViewController _beginObservingTransparencyStatusChangedNotification].cold.2
+ -[TUIKTSingleAccountViewController _showInfoAlert:].cold.2
+ -[TUIKTSingleAccountViewController _stopObservingTransparencyStatusChangedNotification].cold.2
+ -[TUIKTSingleAccountViewController _transparencyStatusChangedNotificationHandler:].cold.1
+ -[TUIKTSingleAccountViewController copyAccountKeyLinkClicked:].cold.1
+ -[TUIKTSingleAccountViewController initWithOptions:].cold.2
+ -[TUIKTSingleAccountViewController init].cold.2
+ -[TUIKTSingleAccountViewController loadView].cold.2
+ -[TUIKTSingleAccountViewController refreshKey].cold.2
+ -[TUIKTSingleAccountViewController updateUI].cold.2
+ -[TUIKTStateManager init].cold.2
+ -[TUIKTStateManager isManateeAvailableWithCompletion:].cold.2
+ -[TUIKTStateManager setExpectedResolutionDays:].cold.2
+ -[TUIKTStateManager stateLabel].cold.2
+ -[TUIKTStateManager updateStateWithKTStatusResult:].cold.1
+ -[TUIKTStateManager updateStateWithKTStatusResult:].cold.2
+ -[TUIMarkAsVerifiedButton layout].cold.2
+ -[TUINetworkMonitor _setNetworkMonitorUpdateHandlerWithPath:completion:].cold.2
+ -[TUINetworkMonitor dealloc].cold.2
+ -[TUINetworkMonitor init].cold.2
+ -[TUINetworkMonitor setUpNetworkPathMonitor].cold.2
+ -[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:].cold.2
+ -[TUIOptInFlowControllerImpl _beginIneligibleDevicesRemoteUIRequestWithCompletion:].cold.2
+ -[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:].cold.2
+ -[TUIOptInFlowControllerImpl _dimissWithOptInState:completion:].cold.2
+ -[TUIOptInFlowControllerImpl _dismissIneligibleDevicesRemoteUI].cold.2
+ -[TUIOptInFlowControllerImpl _dismissOptInFlow].cold.2
+ -[TUIOptInFlowControllerImpl _dismissOptOutFlow].cold.2
+ -[TUIOptInFlowControllerImpl _dismissWelcomeScreen].cold.2
+ -[TUIOptInFlowControllerImpl _iCloudAccountMatchesiMessageAccount].cold.2
+ -[TUIOptInFlowControllerImpl _iCloudAccountMatchesiMessageAccount].cold.3
+ -[TUIOptInFlowControllerImpl _iCloudAccountMatchesiMessageAccount].cold.4
+ -[TUIOptInFlowControllerImpl _iCloudAccountMatchesiMessageAccount].cold.5
+ -[TUIOptInFlowControllerImpl _ineligibleDevicesRemoteUIFeatureEnabled].cold.2
+ -[TUIOptInFlowControllerImpl _initOBContainterViewWithModel:].cold.2
+ -[TUIOptInFlowControllerImpl _learnMorePressed].cold.2
+ -[TUIOptInFlowControllerImpl _showAppleIdPrefpaneOptInFlow].cold.2
+ -[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingWindow:].cold.2
+ -[TUIOptInFlowControllerImpl _showMessagesSettingsOptInFlow].cold.2
+ -[TUIOptInFlowControllerImpl _showMessagesSettingsOptOutFlow].cold.2
+ -[TUIOptInFlowControllerImpl _showOBSheetWithModel:].cold.2
+ -[TUIOptInFlowControllerImpl _showOptInResultError:error:].cold.2
+ -[TUIOptInFlowControllerImpl _startFlowPressed].cold.2
+ -[TUIOptInFlowControllerImpl _verifyMessages:].cold.4
+ -[TUIOptInFlowControllerImpl _verifyMessages:].cold.5
+ -[TUIOptInFlowControllerImpl _verifyMessages:].cold.6
+ -[TUIOptInFlowControllerImpl authenticationFailed:].cold.2
+ -[TUIOptInFlowControllerImpl beginOptInFlow].cold.2
+ -[TUIOptInFlowControllerImpl beginOptOutFlow].cold.2
+ -[TUIOptInFlowControllerImpl clientInfo].cold.2
+ -[TUIOptInFlowControllerImpl dismissPendingPopupUI].cold.2
+ -[TUIOptInFlowControllerImpl endWebView:].cold.5
+ -[TUIOptInFlowControllerImpl endWebView:].cold.6
+ -[TUIOptInFlowControllerImpl endWebView:].cold.7
+ -[TUIOptInFlowControllerImpl endWebView:].cold.8
+ -[TUIOptInFlowControllerImpl endWebView:].cold.9
+ -[TUIOptInFlowControllerImpl icaSetButtonBar:webViewName:].cold.2
+ -[TUIOptInFlowControllerImpl initWithKeyWindow:accountManager:stateManager:].cold.2
+ -[TUIOptInFlowControllerImpl loadFailed:].cold.2
+ -[TUIOptInFlowControllerImpl performAccountChecksForFlow:].cold.2
+ -[TUIOptInFlowControllerImpl shouldHideCancelButton].cold.2
+ -[TUIOptInFlowControllerImpl showPurchaseSharingForAltDSID:callback:].cold.2
+ -[TUIOptInFlowControllerImpl sizeChangedFrom:toSize:webViewName:callback:].cold.1
+ -[TUIOptInFlowControllerImpl skipAndContinueSignIn].cold.2
+ -[TUIOptInFlowControllerImpl webViewDidFinishLoading:].cold.2
+ -[TUIReportManager fetchDataWithUUID:].cold.1
+ -[TUIReportManager sendReport:].cold.1
+ -[TUIStaticIdentityManager _sessionStateWithStateString:].cold.1
+ -[TUIStaticIdentityManager deleteKTSession].cold.1
+ -[TUIStaticIdentityManager initWithConversationMembers:options:].cold.1
+ -[TUIStaticIdentityManager localizedPeerAccountNameMessage:].cold.1
+ -[TUIStaticIdentityManager localizedPeerAccountNameMessage:].cold.2
+ -[TUIStaticIdentityManager peerCNContact:].cold.1
+ -[TUIStaticIdentityManager postNotificationName:object:userInfo:deliverImmediately:].cold.1
+ -[TUIStaticIdentityManager requestConversationVerificationState:completionHandler:].cold.1
+ -[TUIStaticIdentityManager requestNewSasCodeWithDelay].cold.2
+ -[TUIStaticIdentityManager requestNewSasCode].cold.2
+ -[TUIStaticIdentityManager requestSelfAccountKey].cold.2
+ -[TUIStaticIdentityManager sessionExpired:].cold.1
+ -[TUIStaticIdentityManager verifyConversation].cold.1
+ -[TUIStaticIdentityManager verifyConversation].cold.2
+ GCC_except_table168
+ GCC_except_table184
+ GCC_except_table187
+ GCC_except_table271
+ GCC_except_table277
+ GCC_except_table49
+ TUIKTLearnMoreRemoteViewControllerHostInterface.cold.1
+ TUIKTLearnMoreRemoteViewControllerServiceInterface.cold.1
+ __31-[TUIReportManager sendReport:]_block_invoke.3.cold.1
+ __38-[TUIReportManager fetchDataWithUUID:]_block_invoke.11.cold.1
+ __41-[TUIOptInFlowControllerImpl endWebView:]_block_invoke.376.cold.1
+ __43-[TUIKTConversationPaneController updateUI]_block_invoke.189.cold.1
+ __43-[TUIStaticIdentityManager _setupKTSession]_block_invoke.111.cold.1
+ __43-[TUIStaticIdentityManager _setupKTSession]_block_invoke.111.cold.2
+ __43-[TUIStaticIdentityManager _setupKTSession]_block_invoke.cold.1
+ __43-[TUIStaticIdentityManager _setupKTSession]_block_invoke.cold.2
+ __44-[TUIKTAppIntentsData statusWithCompletion:]_block_invoke.9.cold.1
+ __44-[TUIKTAppIntentsData statusWithCompletion:]_block_invoke.9.cold.2
+ __44-[TUIKTSingleAccountViewController updateUI]_block_invoke.64.cold.1
+ __44-[TUIKTSingleAccountViewController updateUI]_block_invoke.64.cold.2
+ __44-[TUINetworkMonitor setUpNetworkPathMonitor]_block_invoke.10.cold.1
+ __44-[TUINetworkMonitor setUpNetworkPathMonitor]_block_invoke.13.cold.1
+ __46-[TUIOptInFlowControllerImpl _verifyMessages:]_block_invoke.356.cold.3
+ __46-[TUIOptInFlowControllerImpl _verifyMessages:]_block_invoke.356.cold.4
+ __47-[TUIKTReportToAppleViewController viewDidLoad]_block_invoke.75.cold.1
+ __48-[TUIKTOptInStatusViewController _updateAppleID]_block_invoke.192.cold.1
+ __48-[TUIKTOptInStatusViewController _updateAppleID]_block_invoke.192.cold.2
+ __48-[TUIKTOptInStatusViewController _updateAppleID]_block_invoke.198.cold.1
+ __49-[TUIKTConversationPaneController showInfoAlert:]_block_invoke.212.cold.1
+ __49-[TUIKTConversationViewController updateLinkText]_block_invoke.47.cold.1
+ __49-[TUIStaticIdentityManager requestSelfAccountKey]_block_invoke.17.cold.2
+ __49-[TUIStaticIdentityManager requestSelfAccountKey]_block_invoke.17.cold.3
+ __49-[TUIStaticIdentityManager requestSelfAccountKey]_block_invoke.24.cold.3
+ __49-[TUIStaticIdentityManager requestSelfAccountKey]_block_invoke.24.cold.4
+ __49-[TUIStaticIdentityManager requestSelfAccountKey]_block_invoke.24.cold.5
+ __50-[TUIOptInFlowControllerImpl _showAppleIdPrefpane]_block_invoke.290.cold.1
+ __50-[TUIOptInFlowControllerImpl _showAppleIdPrefpane]_block_invoke.cold.2
+ __50-[TUIOptInFlowControllerImpl _showAppleIdPrefpane]_block_invoke.cold.3
+ __51-[TUIKTConversationPaneController showNoMatchAlert]_block_invoke.221.cold.1
+ __51-[TUIKTConversationPaneController showNoMatchAlert]_block_invoke.221.cold.2
+ __51-[TUIKTConversationPaneController showNoMatchAlert]_block_invoke.228.cold.1
+ __51-[TUIKTConversationPaneController showNoMatchAlert]_block_invoke.241.cold.2
+ __51-[TUIKTConversationPaneController showNoMatchAlert]_block_invoke.247.cold.1
+ __51-[TUIKTConversationViewController displayCodeSheet]_block_invoke.59.cold.2
+ __51-[TUIKTConversationViewController displayCodeSheet]_block_invoke.59.cold.3
+ __51-[TUIKTSingleAccountViewController _showInfoAlert:]_block_invoke.72.cold.1
+ __51-[TUIOptInFlowControllerImpl _showMessagesSettings]_block_invoke.cold.3
+ __51-[TUIOptInFlowControllerImpl _showMessagesSettings]_block_invoke.cold.4
+ __51-[TUIOptInFlowControllerImpl _showMessagesSettings]_block_invoke.cold.5
+ __51-[TUIOptInFlowControllerImpl dismissPendingPopupUI]_block_invoke.99.cold.1
+ __52-[TUIKTOptInStatusViewController _changeOptInState:]_block_invoke.233.cold.1
+ __52-[TUIKTOptInStatusViewController _changeOptInState:]_block_invoke.233.cold.2
+ __52-[TUIOptInFlowControllerImpl _showOBSheetWithModel:]_block_invoke.114.cold.1
+ __52-[TUIOptInFlowControllerImpl _showOBSheetWithModel:]_block_invoke.117.cold.3
+ __52-[TUIOptInFlowControllerImpl _showOBSheetWithModel:]_block_invoke.117.cold.4
+ __53-[TUIDeviceDetailsViewController deviceListModified:]_block_invoke.69.cold.1
+ __53-[TUIKTDeviceErrorViewController viewDetailsPressed:]_block_invoke.100.cold.2
+ __53-[TUIKTDeviceErrorViewController viewDetailsPressed:]_block_invoke.100.cold.3
+ __53-[TUIKTDeviceErrorViewController viewDetailsPressed:]_block_invoke.92.cold.1
+ __53-[TUIKTDeviceErrorViewController viewDetailsPressed:]_block_invoke.92.cold.2
+ __53-[TUIKTOptInStatusViewController _optInSwitchToggled]_block_invoke.133.cold.1
+ __53-[TUIKTOptInStatusViewController _optInSwitchToggled]_block_invoke.136.cold.1
+ __53-[TUIKTOptInStatusViewController _resetButtonPressed]_block_invoke.227.cold.1
+ __54-[TUIKTOptInStatusViewController _dismissPendingAlert]_block_invoke.cold.2
+ __54-[TUIKTOptInStatusViewController _dismissPendingAlert]_block_invoke.cold.3
+ __54-[TUIKTReportToAppleViewController sendButtonClicked:]_block_invoke.143.cold.1
+ __54-[TUIKTReportToAppleViewController sendButtonClicked:]_block_invoke.146.cold.1
+ __54-[TUIKTReportToAppleViewController sendButtonClicked:]_block_invoke.150.cold.1
+ __54-[TUIKTReportToAppleViewController sendButtonClicked:]_block_invoke.150.cold.2
+ __54-[TUIKTStateManager isManateeAvailableWithCompletion:]_block_invoke.26.cold.2
+ __54-[TUIKTStateManager isManateeAvailableWithCompletion:]_block_invoke.26.cold.3
+ __54-[TUIStaticIdentityManager requestNewSasCodeWithDelay]_block_invoke.46.cold.1
+ __55-[TUIAIDPPOptInSpecifierViewController _checkKTStatus:]_block_invoke.87.cold.1
+ __55-[TUIAIDPPOptInSpecifierViewController _checkKTStatus:]_block_invoke.87.cold.2
+ __55-[TUIAIDPPOptInSpecifierViewController _checkKTStatus:]_block_invoke.93.cold.1
+ __55-[TUIAIDPPOptInSpecifierViewController _checkKTStatus:]_block_invoke.93.cold.2
+ __55-[TUIKTOptInStatusViewController _showMessagesSettings]_block_invoke.208.cold.3
+ __55-[TUIKTOptInStatusViewController _showMessagesSettings]_block_invoke.208.cold.4
+ __55-[TUIKTOptInStatusViewController _showMessagesSettings]_block_invoke.208.cold.5
+ __55-[TUIKTOptInStatusViewController _turnOffButtonPressed]_block_invoke.180.cold.1
+ __55-[TUIKTReportToAppleViewController showDetailsClicked:]_block_invoke.122.cold.1
+ __55-[TUIKTReportToAppleViewController showDetailsClicked:]_block_invoke.125.cold.1
+ __55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.159.cold.1
+ __55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.cold.1
+ __55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.cold.2
+ __57-[TUIKTOptInStatusViewController processOptInStateChange]_block_invoke.123.cold.1
+ __58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.167.cold.3
+ __58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.167.cold.4
+ __58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.167.cold.5
+ __58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.177.cold.1
+ __58-[TUIOptInFlowControllerImpl performAccountChecksForFlow:]_block_invoke.66.cold.3
+ __58-[TUIOptInFlowControllerImpl performAccountChecksForFlow:]_block_invoke.66.cold.4
+ __58-[TUIOptInFlowControllerImpl performAccountChecksForFlow:]_block_invoke.69.cold.4
+ __58-[TUIOptInFlowControllerImpl performAccountChecksForFlow:]_block_invoke.69.cold.5
+ __58-[TUIOptInFlowControllerImpl performAccountChecksForFlow:]_block_invoke.69.cold.6
+ __58-[TUIOptInFlowControllerImpl performAccountChecksForFlow:]_block_invoke.69.cold.7
+ __58-[TUIOptInFlowControllerImpl performAccountChecksForFlow:]_block_invoke.73.cold.1
+ __58-[TUIOptInFlowControllerImpl performAccountChecksForFlow:]_block_invoke.81.cold.1
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.128.cold.1
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.128.cold.2
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.128.cold.3
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.128.cold.4
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.128.cold.5
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.145.cold.5
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.145.cold.6
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.145.cold.7
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.145.cold.8
+ __59-[TUIAIDPPOptInSpecifierViewController deviceListModified:]_block_invoke.145.cold.9
+ __60-[TUIKTAppIntentsData publicVerificationCodeWithCompletion:]_block_invoke.35.cold.1
+ __60-[TUIKTAppIntentsData publicVerificationCodeWithCompletion:]_block_invoke.35.cold.2
+ __60-[TUIKTLearnMoreViewController presentWithPresentingWindow:]_block_invoke.12.cold.2
+ __60-[TUIKTLearnMoreViewController presentWithPresentingWindow:]_block_invoke.18.cold.2
+ __60-[TUIKTLearnMoreViewController presentWithPresentingWindow:]_block_invoke.18.cold.3
+ __60-[TUIKTLearnMoreViewController presentWithPresentingWindow:]_block_invoke_2.cold.2
+ __60-[TUIKTLearnMoreViewController presentWithPresentingWindow:]_block_invoke_2.cold.3
+ __62-[TUIKTLearnMoreViewController _showRemoteServicePrivacySheet]_block_invoke.54.cold.2
+ __62-[TUIKTLearnMoreViewController _showRemoteServicePrivacySheet]_block_invoke.58.cold.1
+ __63-[TUIDeviceDetailsViewController _updateDevicesWithIssuesList:]_block_invoke.60.cold.1
+ __63-[TUIOptInFlowControllerImpl _dimissWithOptInState:completion:]_block_invoke.300.cold.1
+ __63-[TUIOptInFlowControllerImpl _dimissWithOptInState:completion:]_block_invoke.300.cold.2
+ __64-[TUIKTOptInStatusViewController optInFlowResultWithStateUpdate]_block_invoke.295.cold.1
+ __64-[TUIKTOptInStatusViewController optInFlowResultWithStateUpdate]_block_invoke.295.cold.2
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.185.cold.3
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.185.cold.4
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.185.cold.5
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.185.cold.6
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.185.cold.7
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.185.cold.8
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.185.cold.9
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.203.cold.1
+ __66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.216.cold.1
+ __67-[TUIKTReportToAppleViewController textView:clickedOnLink:atIndex:]_block_invoke.180.cold.1
+ __70-[TUIKTLearnMoreViewController _connectToRemoteServiceWithCompletion:]_block_invoke.39.cold.2
+ __70-[TUIKTLearnMoreViewController _connectToRemoteServiceWithCompletion:]_block_invoke.39.cold.3
+ __70-[TUIKTLearnMoreViewController _connectToRemoteServiceWithCompletion:]_block_invoke.39.cold.4
+ __71-[TUIAppleAccountManager silentRenewAppleAccountWithCompletionHandler:]_block_invoke.5.cold.1
+ __71-[TUIAppleAccountManager silentRenewAppleAccountWithCompletionHandler:]_block_invoke.5.cold.2
+ __72-[TUINetworkMonitor _setNetworkMonitorUpdateHandlerWithPath:completion:]_block_invoke.22.cold.2
+ __72-[TUINetworkMonitor _setNetworkMonitorUpdateHandlerWithPath:completion:]_block_invoke.22.cold.3
+ __72-[TUINetworkMonitor _setNetworkMonitorUpdateHandlerWithPath:completion:]_block_invoke.22.cold.4
+ __72-[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingWindow:]_block_invoke.313.cold.1
+ __74-[TUIOptInFlowControllerImpl sizeChangedFrom:toSize:webViewName:callback:]_block_invoke.398.cold.1
+ __75-[TUIKTConversationPaneController verifyContact:peerPublicAccountIdentity:]_block_invoke.202.cold.1
+ __83-[TUIOptInFlowControllerImpl _beginIneligibleDevicesRemoteUIRequestWithCompletion:]_block_invoke.230.cold.1
+ __83-[TUIOptInFlowControllerImpl _beginIneligibleDevicesRemoteUIRequestWithCompletion:]_block_invoke.230.cold.2
+ __83-[TUIOptInFlowControllerImpl _beginIneligibleDevicesRemoteUIRequestWithCompletion:]_block_invoke.239.cold.1
+ __83-[TUIOptInFlowControllerImpl _beginIneligibleDevicesRemoteUIRequestWithCompletion:]_block_invoke.244.cold.2
+ __83-[TUIStaticIdentityManager requestConversationVerificationState:completionHandler:]_block_invoke_2.cold.1
+ __84-[TUIStaticIdentityManager postNotificationName:object:userInfo:deliverImmediately:]_block_invoke.122.cold.1
+ _objc_msgSend$setPreventsApplicationTerminationWhenModal:
- GCC_except_table138
- GCC_except_table154
- GCC_except_table155
- GCC_except_table236
- GCC_except_table238
- GCC_except_table39
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _objc_msgSend$disableUpdateMask
- _objc_msgSend$setDisableUpdateMask:
CStrings:
+ "setPreventsApplicationTerminationWhenModal:"
- "disableUpdateMask"
- "setDisableUpdateMask:"

```
