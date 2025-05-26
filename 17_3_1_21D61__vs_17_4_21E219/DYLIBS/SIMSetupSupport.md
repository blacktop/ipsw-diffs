## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-579.1.0.0.0
-  __TEXT.__text: 0x67a14
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x520c
+609.0.0.0.0
+  __TEXT.__text: 0x6cd94
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x5834
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x871e
-  __TEXT.__gcc_except_tab: 0xcd4
-  __TEXT.__oslogstring: 0x3b5c
+  __TEXT.__cstring: 0x8de2
+  __TEXT.__oslogstring: 0x3dd9
+  __TEXT.__gcc_except_tab: 0xd50
   __TEXT.__dlopen_cstrs: 0x1b6
-  __TEXT.__unwind_info: 0x172c
-  __TEXT.__objc_classname: 0xd75
-  __TEXT.__objc_methname: 0xeda5
-  __TEXT.__objc_methtype: 0x2dc2
-  __TEXT.__objc_stubs: 0x9d80
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x11d0
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __TEXT.__unwind_info: 0x1810
+  __TEXT.__objc_classname: 0xdcf
+  __TEXT.__objc_methname: 0xf805
+  __TEXT.__objc_methtype: 0x2da9
+  __TEXT.__objc_stubs: 0xa380
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x12a0
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1f618
-  __DATA_CONST.__objc_selrefs: 0x3280
+  __DATA_CONST.__objc_const: 0x216d8
+  __DATA_CONST.__objc_selrefs: 0x34e0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x658
+  __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x3880
-  __AUTH_CONST.__objc_const: 0x2018
-  __AUTH_CONST.__const: 0x500
+  __AUTH_CONST.__cfstring: 0x3e60
+  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__objc_const: 0x20f0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x318
-  __AUTH_CONST.__auth_got: 0x3e8
-  __AUTH.__objc_data: 0x1b80
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x630
-  __DATA.__objc_superrefs: 0x290
-  __DATA.__objc_ivar: 0x858
-  __DATA.__data: 0xaf0
+  __AUTH_CONST.__objc_intobj: 0x3d8
+  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH.__objc_data: 0x1cc0
+  __DATA.__objc_ivar: 0x900
+  __DATA.__data: 0xa90
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SafariServices.framework/SafariServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2319
-  Symbols:   8563
-  CStrings:  4164
+  Functions: 2474
+  Symbols:   9042
+  CStrings:  4358
 
Symbols:
+ +[TSSIMSetupFlow _flowWithOptions:]
+ +[TSSIMSetupFlow _flowWithOptions:].cold.1
+ +[TSSIMSetupFlow _flowWithOptions:].cold.2
+ +[TSUtilities openPrefsURL:]
+ -[SSOBLinkTrayButton .cxx_destruct]
+ -[SSOBLinkTrayButton _centerActivityIndicatorInButton]
+ -[SSOBLinkTrayButton _hideLoading]
+ -[SSOBLinkTrayButton _showLoading]
+ -[SSOBLinkTrayButton hideSpinner]
+ -[SSOBLinkTrayButton normalStateTitle]
+ -[SSOBLinkTrayButton setNormalStateTitle:]
+ -[SSOBLinkTrayButton setSpinner:]
+ -[SSOBLinkTrayButton showSpinner]
+ -[SSOBLinkTrayButton spinner]
+ -[SSUserConsentViewController .cxx_destruct]
+ -[SSUserConsentViewController _cancelButtonTapped]
+ -[SSUserConsentViewController _continueButtonTapped]
+ -[SSUserConsentViewController _setNavigationItems]
+ -[SSUserConsentViewController animating]
+ -[SSUserConsentViewController cachedButtons]
+ -[SSUserConsentViewController customizeSpinner]
+ -[SSUserConsentViewController delegate]
+ -[SSUserConsentViewController init]
+ -[SSUserConsentViewController setAnimating:]
+ -[SSUserConsentViewController setCachedButtons:]
+ -[SSUserConsentViewController setDelegate:]
+ -[SSUserConsentViewController setSpinner:]
+ -[SSUserConsentViewController setSpinnerContainer:]
+ -[SSUserConsentViewController spinnerContainer]
+ -[SSUserConsentViewController spinner]
+ -[SSUserConsentViewController viewDidAppear:]
+ -[SSUserConsentViewController viewDidLoad]
+ -[TSActivationFlowWithSimSetupFlow _showPendingInstallItems]
+ -[TSBuddyMLController type]
+ -[TSCarrierSignupFlow _getSFSafariViewControllerWithURL:]
+ -[TSCarrierSignupFlow setSubFlow:]
+ -[TSCarrierSignupFlow startTimer:]
+ -[TSCarrierSignupFlow subFlow]
+ -[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]
+ -[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:].cold.1
+ -[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]
+ -[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:].cold.1
+ -[TSCellularPlanActivatingFlow _handleOtpStatusUpdate:]
+ -[TSCellularPlanActivatingFlow _stopTimerWithBackgroundTaskState:]
+ -[TSCellularPlanActivatingFlow _stopTimerWithBackgroundTaskState:].cold.1
+ -[TSCellularPlanActivatingFlow initWithSkipActivatingPane:timerType:transferBackPlan:setupType:]
+ -[TSCellularPlanActivatingFlow oneTimeCodeViewController]
+ -[TSCellularPlanActivatingFlow oneTimePasscodePaneShown]
+ -[TSCellularPlanActivatingFlow setOneTimeCodeViewController:]
+ -[TSCellularPlanActivatingFlow setOneTimePasscodePaneShown:]
+ -[TSCellularPlanActivatingFlow setSourceIccid:]
+ -[TSCellularPlanActivatingFlow setTermsAndConditionsShown:]
+ -[TSCellularPlanActivatingFlow setTermsAndConditionsViewController:]
+ -[TSCellularPlanActivatingFlow sourceIccid]
+ -[TSCellularPlanActivatingFlow startTimer:]
+ -[TSCellularPlanActivatingFlow termsAndConditionsShown]
+ -[TSCellularPlanActivatingFlow termsAndConditionsViewController]
+ -[TSCellularPlanActivatingFlow userDidTapCancel]
+ -[TSCellularPlanIntroViewController _hideQRCodeOption]
+ -[TSPRXSIMTransferringViewController initWithTitle:subtitle:otpDetectorNeeded:]
+ -[TSPRXSIMTransferringViewController otpDetectorNeeded]
+ -[TSPRXSIMTransferringViewController setOtpDetectorNeeded:]
+ -[TSProximitySourceTransferFlow initForResumption]
+ -[TSProximitySourceTransferFlow isHiding]
+ -[TSProximitySourceTransferFlow isResumingAfterPause]
+ -[TSProximitySourceTransferFlow setIsHiding:]
+ -[TSProximitySourceTransferFlow setIsResumingAfterPause:]
+ -[TSProximitySourceTransferFlow transferEventUpdate:].cold.1
+ -[TSSIMSetupFlow endFlowGracefully:]
+ -[TSSIMSetupFlow flowType]
+ -[TSSIMSetupFlow getRootFlow]
+ -[TSSIMSetupFlow getRootFlow].cold.1
+ -[TSSIMSetupFlow setFlowType:]
+ -[TSSIMSetupFlow showLoadFailureAlert:error:]
+ -[TSSIMSetupFlow startTimer:]
+ -[TSSIMSetupPublicApiInstallFlow _alertConsentWithCompletion:]
+ -[TSSIMSetupPublicApiInstallFlow _displayUserConsentAlert:]
+ -[TSSIMSetupPublicApiInstallFlow _firstViewController]
+ -[TSSIMSetupPublicApiInstallFlow userDidTapCancel]
+ -[TSSubFlowViewController initWithFlow:navigationController:]
+ -[TSTermsAndConditionsViewController .cxx_destruct]
+ -[TSTermsAndConditionsViewController _acceptClicked:]
+ -[TSTermsAndConditionsViewController _cancelTransfer:]
+ -[TSTermsAndConditionsViewController acceptButton]
+ -[TSTermsAndConditionsViewController client]
+ -[TSTermsAndConditionsViewController declineButton]
+ -[TSTermsAndConditionsViewController delegate]
+ -[TSTermsAndConditionsViewController initWithSourceIccid:mainText:]
+ -[TSTermsAndConditionsViewController loadView]
+ -[TSTermsAndConditionsViewController mainText]
+ -[TSTermsAndConditionsViewController setAcceptButton:]
+ -[TSTermsAndConditionsViewController setClient:]
+ -[TSTermsAndConditionsViewController setDeclineButton:]
+ -[TSTermsAndConditionsViewController setDelegate:]
+ -[TSTermsAndConditionsViewController setMainText:]
+ -[TSTermsAndConditionsViewController setSourceIccid:]
+ -[TSTermsAndConditionsViewController setSpinner:]
+ -[TSTermsAndConditionsViewController setTextView:]
+ -[TSTermsAndConditionsViewController setTitleLabel:]
+ -[TSTermsAndConditionsViewController sourceIccid]
+ -[TSTermsAndConditionsViewController spinner]
+ -[TSTermsAndConditionsViewController textView]
+ -[TSTermsAndConditionsViewController titleLabel]
+ -[TSTermsAndConditionsViewController viewDidLoad]
+ -[TSTransferFlow _updateSourceProxCardState:]
+ -[TSTransferFlow ctClient]
+ -[TSTransferFlow isSourceProxCardVisible]
+ -[TSTransferFlow setCtClient:]
+ -[TSTransferFlow setIsSourceProxCardVisible:]
+ -[TSTransferFlow transferEventUpdate:]
+ -[TSTransferFlow userDidTapCancel]
+ -[TSTransferOneTimeCodeViewController .cxx_destruct]
+ -[TSTransferOneTimeCodeViewController _cancelButtonTapped:]
+ -[TSTransferOneTimeCodeViewController _changeOtpTextFieldState:]
+ -[TSTransferOneTimeCodeViewController _continueButtonTapped:]
+ -[TSTransferOneTimeCodeViewController _handleKeyboardPresentation:]
+ -[TSTransferOneTimeCodeViewController _hideKeyboard]
+ -[TSTransferOneTimeCodeViewController _keyboardWillHide:]
+ -[TSTransferOneTimeCodeViewController _resendOTP]
+ -[TSTransferOneTimeCodeViewController _setupLayoutConstraint]
+ -[TSTransferOneTimeCodeViewController _textFieldDidChange]
+ -[TSTransferOneTimeCodeViewController animating]
+ -[TSTransferOneTimeCodeViewController cachedButtons]
+ -[TSTransferOneTimeCodeViewController cancelButton]
+ -[TSTransferOneTimeCodeViewController client]
+ -[TSTransferOneTimeCodeViewController continueButton]
+ -[TSTransferOneTimeCodeViewController delegate]
+ -[TSTransferOneTimeCodeViewController details]
+ -[TSTransferOneTimeCodeViewController disableButtonsAndHideSpinnerText]
+ -[TSTransferOneTimeCodeViewController initWithSourceIccid:phoneNumber:carrierName:usePin:]
+ -[TSTransferOneTimeCodeViewController otpEditor]
+ -[TSTransferOneTimeCodeViewController resendOTPButton]
+ -[TSTransferOneTimeCodeViewController setAnimating:]
+ -[TSTransferOneTimeCodeViewController setCachedButtons:]
+ -[TSTransferOneTimeCodeViewController setCancelButton:]
+ -[TSTransferOneTimeCodeViewController setClient:]
+ -[TSTransferOneTimeCodeViewController setContinueButton:]
+ -[TSTransferOneTimeCodeViewController setDelegate:]
+ -[TSTransferOneTimeCodeViewController setDetails:]
+ -[TSTransferOneTimeCodeViewController setOtpEditor:]
+ -[TSTransferOneTimeCodeViewController setResendOTPButton:]
+ -[TSTransferOneTimeCodeViewController setSkipButton:]
+ -[TSTransferOneTimeCodeViewController setSourceIccid:]
+ -[TSTransferOneTimeCodeViewController setSpinner:]
+ -[TSTransferOneTimeCodeViewController setSpinnerContainer:]
+ -[TSTransferOneTimeCodeViewController setUsePin:]
+ -[TSTransferOneTimeCodeViewController skipButton]
+ -[TSTransferOneTimeCodeViewController sourceIccid]
+ -[TSTransferOneTimeCodeViewController spinnerContainer]
+ -[TSTransferOneTimeCodeViewController spinner]
+ -[TSTransferOneTimeCodeViewController textFieldShouldReturn:]
+ -[TSTransferOneTimeCodeViewController updateOtpState:]
+ -[TSTransferOneTimeCodeViewController usePin]
+ -[TSTransferOneTimeCodeViewController viewDidLoad]
+ -[TSUserInPurchaseFlowAssertion assertUserInPurchaseFlowStartOver:caller:]
+ -[TSUserInPurchaseFlowAssertion deassertUserInPurchaseFlowWithForce:caller:]
+ -[TSWebsheetViewController initForRemotePlan:carrierName:skipUIDismissal:]
+ GCC_except_table21
+ GCC_except_table28
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table44
+ _CFUserNotificationDisplayAlert
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_SSOBLinkTrayButton
+ _OBJC_CLASS_$_SSUserConsentViewController
+ _OBJC_CLASS_$_TSTermsAndConditionsViewController
+ _OBJC_CLASS_$_TSTransferOneTimeCodeViewController
+ _OBJC_CLASS_$_UINavigationBarAppearance
+ _OBJC_CLASS_$_UITapGestureRecognizer
+ _OBJC_CLASS_$_UITextView
+ _OBJC_CLASS_$_UIToolbar
+ _OBJC_IVAR_$_SSOBLinkTrayButton._normalStateTitle
+ _OBJC_IVAR_$_SSOBLinkTrayButton._spinner
+ _OBJC_IVAR_$_SSUserConsentViewController._animating
+ _OBJC_IVAR_$_SSUserConsentViewController._cachedButtons
+ _OBJC_IVAR_$_SSUserConsentViewController._delegate
+ _OBJC_IVAR_$_SSUserConsentViewController._spinner
+ _OBJC_IVAR_$_SSUserConsentViewController._spinnerContainer
+ _OBJC_IVAR_$_TSBuddyMLController._type
+ _OBJC_IVAR_$_TSBuddyMLViewController._isBootstrapAsserted
+ _OBJC_IVAR_$_TSCarrierSignupFlow._subFlow
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._oneTimeCodeViewController
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._oneTimePasscodePaneShown
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._sourceIccid
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._termsAndConditionsShown
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._termsAndConditionsViewController
+ _OBJC_IVAR_$_TSPRXSIMTransferringViewController._otpDetectorNeeded
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._isHiding
+ _OBJC_IVAR_$_TSProximitySourceTransferFlow._isResumingAfterPause
+ _OBJC_IVAR_$_TSSIMSetupFlow._flowType
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._acceptButton
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._client
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._declineButton
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._delegate
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._mainText
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._sourceIccid
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._spinner
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._textView
+ _OBJC_IVAR_$_TSTermsAndConditionsViewController._titleLabel
+ _OBJC_IVAR_$_TSTransferFlow._ctClient
+ _OBJC_IVAR_$_TSTransferFlow._isSourceProxCardVisible
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._animating
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._cachedButtons
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._cancelButton
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._client
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._continueButton
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._delegate
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._details
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._otpEditor
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._resendOTPButton
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._skipButton
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._sourceIccid
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._spinner
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._spinnerContainer
+ _OBJC_IVAR_$_TSTransferOneTimeCodeViewController._usePin
+ _OBJC_IVAR_$_TSWebsheetViewController._skipUIDismissal
+ _OBJC_METACLASS_$_OBLinkTrayButton
+ _OBJC_METACLASS_$_SSOBLinkTrayButton
+ _OBJC_METACLASS_$_SSUserConsentViewController
+ _OBJC_METACLASS_$_TSTermsAndConditionsViewController
+ _OBJC_METACLASS_$_TSTransferOneTimeCodeViewController
+ _TSUserInfoCarrierName
+ _TSUserInfoOtpStateKey
+ _TSUserInfoResumeTransferProxCardKey
+ _TSUserInfoTCMainTextKey
+ _TSUserInfoTCStateKey
+ _TSUserInfoUsePinKey
+ _UITextContentTypeOneTimeCode
+ __OBJC_$_INSTANCE_METHODS_SSOBLinkTrayButton
+ __OBJC_$_INSTANCE_METHODS_SSUserConsentViewController
+ __OBJC_$_INSTANCE_METHODS_TSTermsAndConditionsViewController
+ __OBJC_$_INSTANCE_METHODS_TSTransferOneTimeCodeViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSOBLinkTrayButton
+ __OBJC_$_INSTANCE_VARIABLES_SSUserConsentViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTermsAndConditionsViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTransferOneTimeCodeViewController
+ __OBJC_$_PROP_LIST_SSOBLinkTrayButton
+ __OBJC_$_PROP_LIST_SSUserConsentViewController
+ __OBJC_$_PROP_LIST_TSTermsAndConditionsViewController
+ __OBJC_$_PROP_LIST_TSTransferOneTimeCodeViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSUserConsentViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTermsAndConditionsViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTransferOneTimeCodeViewController
+ __OBJC_CLASS_RO_$_SSOBLinkTrayButton
+ __OBJC_CLASS_RO_$_SSUserConsentViewController
+ __OBJC_CLASS_RO_$_TSTermsAndConditionsViewController
+ __OBJC_CLASS_RO_$_TSTransferOneTimeCodeViewController
+ __OBJC_METACLASS_RO_$_SSOBLinkTrayButton
+ __OBJC_METACLASS_RO_$_SSUserConsentViewController
+ __OBJC_METACLASS_RO_$_TSTermsAndConditionsViewController
+ __OBJC_METACLASS_RO_$_TSTransferOneTimeCodeViewController
+ ___34-[SSOBLinkTrayButton _hideLoading]_block_invoke
+ ___44-[TSTransferFlowModel requestCarrierSetups:]_block_invoke.39
+ ___45-[TSSIMSetupFlow showLoadFailureAlert:error:]_block_invoke
+ ___45-[TSSIMSetupFlow showLoadFailureAlert:error:]_block_invoke_2
+ ___49-[TSTransferCloudFlowModel requestCarrierSetups:]_block_invoke.34
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.29
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.29.cold.1
+ ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.29.cold.2
+ ___49-[TSTransferOneTimeCodeViewController _resendOTP]_block_invoke
+ ___49-[TSTransferOneTimeCodeViewController _resendOTP]_block_invoke.cold.1
+ ___50-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke.23
+ ___51-[TSProximitySourceTransferFlow _bootstrapTransfer]_block_invoke.118
+ ___53-[TSProximitySourceTransferFlow transferEventUpdate:]_block_invoke
+ ___53-[TSTermsAndConditionsViewController _acceptClicked:]_block_invoke
+ ___53-[TSTermsAndConditionsViewController _acceptClicked:]_block_invoke.cold.1
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.199
+ ___54-[TSSIMSetupPublicApiInstallFlow firstViewController:]_block_invoke
+ ___54-[TSTermsAndConditionsViewController _cancelTransfer:]_block_invoke
+ ___54-[TSTermsAndConditionsViewController _cancelTransfer:]_block_invoke.cold.1
+ ___54-[TSTransferOneTimeCodeViewController updateOtpState:]_block_invoke
+ ___54-[TSTransferOneTimeCodeViewController updateOtpState:]_block_invoke_2
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.24
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.24.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.25
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.25.cold.1
+ ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.26
+ ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.34
+ ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.34.cold.1
+ ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke.69
+ ___61-[TSTransferOneTimeCodeViewController _continueButtonTapped:]_block_invoke
+ ___61-[TSTransferOneTimeCodeViewController _continueButtonTapped:]_block_invoke.cold.1
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.143
+ ___62-[TSSIMSetupPublicApiInstallFlow _alertConsentWithCompletion:]_block_invoke
+ ___62-[TSSIMSetupPublicApiInstallFlow _alertConsentWithCompletion:]_block_invoke_2
+ ___62-[TSSIMSetupPublicApiInstallFlow _alertConsentWithCompletion:]_block_invoke_2.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.91
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.91.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.92
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.92.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.93
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.93.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.94
+ ___64-[TSPRXSIMTransferringViewController _setupOneTimeCodeDetection]_block_invoke.56
+ ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke.185
+ ___70-[TSCellularSetupLoadingViewController safariViewControllerDidFinish:]_block_invoke.135
+ ___71-[TSTransferOneTimeCodeViewController disableButtonsAndHideSpinnerText]_block_invoke
+ ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.102
+ ___73-[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]_block_invoke
+ ___73-[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]_block_invoke.cold.1
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.96
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.96.cold.1
+ ___76-[TSCarrierSignupFlow showFirstViewControllerWithHostController:completion:]_block_invoke_7
+ ___76-[TSCarrierSignupFlow showFirstViewControllerWithHostController:completion:]_block_invoke_8
+ ___76-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.152
+ ___76-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.156
+ ___77-[TSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke.72
+ ___79-[TSCellularSetupLoadingViewController setupCoreTelephonyClientForRemoteSignup]_block_invoke.95
+ ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.276
+ ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.280
+ ___85-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]_block_invoke
+ ___85-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]_block_invoke.112
+ ___85-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]_block_invoke.cold.1
+ ___86-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke.41
+ ___block_descriptor_48_e8_32bs40w_e8_v12?0B8ls32l8w40l8
+ ___block_descriptor_52_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48w_e43_v16?0"UIViewController<TSSetupFlowItem>"8lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e60_v40?0"NSString"8"NSDictionary"16"NSString"24"NSError"32lw56l8s48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.118
+ ___block_literal_global.125
+ ___block_literal_global.201
+ ___block_literal_global.251
+ ___block_literal_global.282
+ ___block_literal_global.289
+ ___block_literal_global.29
+ ___block_literal_global.31
+ ___block_literal_global.36
+ ___block_literal_global.40
+ ___block_literal_global.42
+ ___block_literal_global.422
+ ___block_literal_global.44
+ ___block_literal_global.475
+ ___block_literal_global.96
+ _objc_msgSend$_alertConsentWithCompletion:
+ _objc_msgSend$_changeOtpTextFieldState:
+ _objc_msgSend$_displayOneTimeCodeViewController:carrierName:usePin:
+ _objc_msgSend$_displayTermsAndConditionsViewController:
+ _objc_msgSend$_displayUserConsentAlert:
+ _objc_msgSend$_flowWithOptions:
+ _objc_msgSend$_getSFSafariViewControllerWithURL:
+ _objc_msgSend$_handleOtpStatusUpdate:
+ _objc_msgSend$_hideKeyboard
+ _objc_msgSend$_hideQRCodeOption
+ _objc_msgSend$_setupLayoutConstraint
+ _objc_msgSend$_showPendingInstallItems
+ _objc_msgSend$_stopTimerWithBackgroundTaskState:
+ _objc_msgSend$_updateSourceProxCardState:
+ _objc_msgSend$addGestureRecognizer:
+ _objc_msgSend$assertUserInPurchaseFlowStartOver:caller:
+ _objc_msgSend$configureWithDefaultBackground
+ _objc_msgSend$constraintGreaterThanOrEqualToAnchor:constant:
+ _objc_msgSend$currentActivatingState
+ _objc_msgSend$deassertUserInPurchaseFlowWithForce:caller:
+ _objc_msgSend$disableButtonsAndHideSpinnerText
+ _objc_msgSend$endFlowGracefully:
+ _objc_msgSend$getRootFlow
+ _objc_msgSend$handleTermsAndConditionsCompleted:consented:completion:
+ _objc_msgSend$handleUserEnteredOtp:otp:completion:
+ _objc_msgSend$hideSpinner
+ _objc_msgSend$initForRemotePlan:carrierName:skipUIDismissal:
+ _objc_msgSend$initForResumption
+ _objc_msgSend$initWithFlow:navigationController:
+ _objc_msgSend$initWithSkipActivatingPane:timerType:transferBackPlan:setupType:
+ _objc_msgSend$initWithSourceIccid:mainText:
+ _objc_msgSend$initWithSourceIccid:phoneNumber:carrierName:usePin:
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$initWithTarget:action:
+ _objc_msgSend$initWithTitle:subtitle:otpDetectorNeeded:
+ _objc_msgSend$isFirstResponder
+ _objc_msgSend$oneTimeCodeViewController
+ _objc_msgSend$openPrefsURL:
+ _objc_msgSend$openSensitiveURL:withOptions:error:
+ _objc_msgSend$renewOneTimePassword:completion:
+ _objc_msgSend$setBorderStyle:
+ _objc_msgSend$setDismissButtonStyle:
+ _objc_msgSend$setEditable:
+ _objc_msgSend$setInputAccessoryView:
+ _objc_msgSend$setItems:
+ _objc_msgSend$setNavigationBarHidden:animated:
+ _objc_msgSend$setOneTimeCodeViewController:
+ _objc_msgSend$setOneTimePasscodePaneShown:
+ _objc_msgSend$setRole:
+ _objc_msgSend$setScrollEdgeAppearance:
+ _objc_msgSend$setSecureTextEntry:
+ _objc_msgSend$setStandardAppearance:
+ _objc_msgSend$setTermsAndConditionsShown:
+ _objc_msgSend$setTermsAndConditionsViewController:
+ _objc_msgSend$setTextContentType:
+ _objc_msgSend$setToolbarHidden:animated:
+ _objc_msgSend$setToolbarItems:
+ _objc_msgSend$set_isBeingUsedForCellularServiceBootstrap:
+ _objc_msgSend$showLoadFailureAlert:error:
+ _objc_msgSend$showSpinner
+ _objc_msgSend$sizeToFit
+ _objc_msgSend$sourceIccid
+ _objc_msgSend$startTimer:
+ _objc_msgSend$termsAndConditionsViewController
+ _objc_msgSend$updateOtpState:
+ _objc_msgSend$updateSourceProxCardState:
- +[SSOBBoldTrayButton boldButton]
- +[TSSIMSetupFlow bootstrapTransferFlowWithSession:transferablePlanOnSource:]
- +[TSSIMSetupFlow flowWithOptions:].cold.1
- +[TSSIMSetupFlow flowWithOptions:].cold.2
- +[TSSIMSetupFlow initWithAppName:requireSetup:]
- +[TSSIMSetupFlow initWithAppName:requireSetup:skipGeneralInstallConsent:]
- +[TSURLRequestFactory requestWithType:URL:postdata:].cold.7
- -[TSCellularPlanActivatingFlow _startTimer:]
- -[TSCellularPlanActivatingFlow _stopTimer]
- -[TSCellularPlanScanViewController _decodeQR:]
- -[TSCellularPlanScanViewController btOpenPhoto]
- -[TSCellularPlanScanViewController imagePickerController:didFinishPickingMediaWithInfo:]
- -[TSCellularPlanScanViewController imagePickerControllerDidCancel:]
- -[TSCellularPlanScanViewController imagePicker]
- -[TSCellularPlanScanViewController imageView]
- -[TSCellularPlanScanViewController imageWithImage:scaledToFillSize:]
- -[TSCellularPlanScanViewController openPhotoTapped:]
- -[TSCellularPlanScanViewController setBtOpenPhoto:]
- -[TSCellularPlanScanViewController setImagePicker:]
- -[TSCellularPlanScanViewController setImageView:]
- -[TSPRXSIMTransferringViewController initWithTitle:subtitle:]
- -[TSSIMSetupFlow showLoadFailureAlert:]
- -[TSTransferFlow _userDidTapCancel]
- -[TSUserInPurchaseFlowAssertion assertUserInPurchaseFlowStartOver:]
- -[TSUserInPurchaseFlowAssertion deassertUserInPurchaseFlowWithForce:]
- -[TSWebsheetViewController initForRemotePlan:carrierName:]
- GCC_except_table30
- _CIDetectorAccuracy
- _CIDetectorAccuracyHigh
- _CIDetectorImageOrientation
- _CIDetectorTypeQRCode
- _OBJC_CLASS_$_CIContext
- _OBJC_CLASS_$_CIDetector
- _OBJC_CLASS_$_CIImage
- _OBJC_CLASS_$_UIImagePickerController
- _OBJC_IVAR_$_TSCellularPlanScanViewController._btOpenPhoto
- _OBJC_IVAR_$_TSCellularPlanScanViewController._imagePicker
- _OBJC_IVAR_$_TSCellularPlanScanViewController._imageView
- _UIImagePickerControllerOriginalImage
- __OBJC_$_CLASS_METHODS_SSOBBoldTrayButton
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIImagePickerControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIImagePickerControllerDelegate
- __OBJC_$_PROTOCOL_REFS_UIImagePickerControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_UIImagePickerControllerDelegate
- __OBJC_PROTOCOL_$_UIImagePickerControllerDelegate
- ___34-[SSOBBoldTrayButton _hideLoading]_block_invoke
- ___39-[TSSIMSetupFlow showLoadFailureAlert:]_block_invoke
- ___39-[TSSIMSetupFlow showLoadFailureAlert:]_block_invoke_2
- ___44-[TSTransferFlowModel requestCarrierSetups:]_block_invoke.36
- ___49-[TSTransferCloudFlowModel requestCarrierSetups:]_block_invoke.31
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.26
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.26.cold.1
- ___49-[TSTransferCloudFlowModel requestTransferPlans:]_block_invoke.26.cold.2
- ___50-[TSManagedDeviceInstallFlow firstViewController:]_block_invoke.20
- ___51-[TSProximitySourceTransferFlow _bootstrapTransfer]_block_invoke.109
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.196
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.21
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.21.cold.1
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.22
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.22.cold.1
- ___55-[TSTransferCloudFlowModel requestPlansWithCompletion:]_block_invoke.23
- ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.31
- ___56-[TSActivationFlowWithSimSetupFlow firstViewController:]_block_invoke.31.cold.1
- ___58-[TSSecureIntentGestureViewController _doubleClickGesture]_block_invoke.66
- ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.140
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.83
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.83.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.84
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.84.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.85
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.85.cold.1
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.86
- ___64-[TSPRXSIMTransferringViewController _setupOneTimeCodeDetection]_block_invoke.53
- ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke.182
- ___70-[TSCellularSetupLoadingViewController safariViewControllerDidFinish:]_block_invoke.132
- ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.94
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.88
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.88.cold.1
- ___76+[TSSIMSetupFlow bootstrapTransferFlowWithSession:transferablePlanOnSource:]_block_invoke
- ___76-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.149
- ___76-[TSTransferListViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.153
- ___77-[TSCellularPlanScanViewController _addNewPlanWithCardData:confirmationCode:]_block_invoke.78
- ___79-[TSCellularSetupLoadingViewController setupCoreTelephonyClientForRemoteSignup]_block_invoke.92
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.273
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.277
- ___86-[TSTransferFlowModel requestPlans:transferablePlanOnSource:bootstrapOnly:completion:]_block_invoke.38
- ___block_descriptor_48_e8_32s40w_e43_v16?0"UIViewController<TSSetupFlowItem>"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e60_v40?0"NSString"8"NSDictionary"16"NSString"24"NSError"32lw48l8s40l8s32l8
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.122
- ___block_literal_global.198
- ___block_literal_global.248
- ___block_literal_global.26
- ___block_literal_global.279
- ___block_literal_global.28
- ___block_literal_global.286
- ___block_literal_global.30
- ___block_literal_global.35
- ___block_literal_global.37
- ___block_literal_global.377
- ___block_literal_global.39
- ___block_literal_global.429
- ___block_literal_global.91
- _kCGImagePropertyOrientation
- _objc_msgSend$_decodeQR:
- _objc_msgSend$_startTimer:
- _objc_msgSend$_stopTimer
- _objc_msgSend$assertUserInPurchaseFlowStartOver:
- _objc_msgSend$btOpenPhoto
- _objc_msgSend$context
- _objc_msgSend$deassertUserInPurchaseFlowWithForce:
- _objc_msgSend$detectorOfType:context:options:
- _objc_msgSend$featuresInImage:options:
- _objc_msgSend$imageWithCGImage:
- _objc_msgSend$imageWithImage:scaledToFillSize:
- _objc_msgSend$initForRemotePlan:carrierName:
- _objc_msgSend$initWithSkipActivatingPane:delayStartTimer:transferBackPlan:setupType:
- _objc_msgSend$messageString
- _objc_msgSend$properties
- _objc_msgSend$readableContentGuide
- _objc_msgSend$setSourceType:
- _objc_msgSend$showLoadFailureAlert:
CStrings:
+ "\x01\x15\x15"
+ "\x11\x12\x1d\x112"
+ "\x12\x12"
+ "\x13\x18"
+ "\x131"
+ "\x18"
+ "%@ prox card on source device @%s"
+ "%@%@"
+ "****"
+ "+[TSSIMSetupFlow _flowWithOptions:]"
+ "+[TSUtilities openPrefsURL:]"
+ "-[TSCarrierSignupFlow startTimer:]"
+ "-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]"
+ "-[TSCellularPlanActivatingFlow _displayOneTimeCodeViewController:carrierName:usePin:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]"
+ "-[TSCellularPlanActivatingFlow _displayTermsAndConditionsViewController:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow _handleOtpStatusUpdate:]"
+ "-[TSCellularPlanActivatingFlow _stopTimerWithBackgroundTaskState:]"
+ "-[TSCellularPlanActivatingFlow startTimer:]"
+ "-[TSSIMSetupFlow getRootFlow]"
+ "-[TSSIMSetupPublicApiInstallFlow _alertConsentWithCompletion:]_block_invoke"
+ "-[TSSIMSetupPublicApiInstallFlow _alertConsentWithCompletion:]_block_invoke_2"
+ "-[TSSIMSetupPublicApiInstallFlow _firstViewController]"
+ "-[TSTermsAndConditionsViewController _acceptClicked:]_block_invoke"
+ "-[TSTermsAndConditionsViewController _cancelTransfer:]_block_invoke"
+ "-[TSTransferFlow _updateSourceProxCardState:]"
+ "-[TSTransferFlow transferEventUpdate:]"
+ "-[TSTransferOneTimeCodeViewController _cancelButtonTapped:]"
+ "-[TSTransferOneTimeCodeViewController _continueButtonTapped:]_block_invoke"
+ "-[TSTransferOneTimeCodeViewController _resendOTP]"
+ "-[TSTransferOneTimeCodeViewController _resendOTP]_block_invoke"
+ "-[TSTransferOneTimeCodeViewController updateOtpState:]"
+ "-[TSUserInPurchaseFlowAssertion assertUserInPurchaseFlowStartOver:caller:]"
+ "-[TSUserInPurchaseFlowAssertion deassertUserInPurchaseFlowWithForce:caller:]"
+ "@\"SSOBLinkTrayButton\""
+ "@\"TSTermsAndConditionsViewController\""
+ "@\"TSTransferOneTimeCodeViewController\""
+ "@\"UITextView\""
+ "@32@0:8B16@20B28"
+ "@44@0:8B16q20@28Q36"
+ "ACTIVATE_NEW_ESIM_ALERT_DETAIL"
+ "ACTIVATE_NEW_ESIM_ALERT_TITLE"
+ "AGREE"
+ "ALLOW"
+ "Already activated and return @%s"
+ "CAMERA"
+ "CELLULAR_PLAN_INTRO_DETAIL_NO_QR_CODE"
+ "CONNECTING"
+ "DISAGREE"
+ "ENTER_ACCOUNT_PIN"
+ "ENTER_ONE_TIME_PASSCODE"
+ "ENTER_PIN_DETAILS_%@"
+ "ENTER_PIN_DETAILS_NO_CARRIER"
+ "ERROR_TRANSFER_ITEM_XPC_CONNECTION_BROKEN_MESSAGE"
+ "ERROR_TRANSFER_ITEM_XPC_CONNECTION_BROKEN_TITLE"
+ "ESIM_NOT_SUPPORT_TITLE_ADD_PLAN_%@"
+ "INCORRECT_ONE_TIME_PASSCODE"
+ "INCORRECT_ONE_TIME_PASSCODE_MESSAGE"
+ "INCORRECT_PIN"
+ "INCORRECT_PIN_MESSAGE"
+ "INSTALL_ESIM_CONSENT_DETAIL"
+ "Lite"
+ "NOT_ALLOW"
+ "NOT_CONNECTED_TO_WIFI"
+ "ONE_TIME_PASSCODE_DETAILS_%@_%@"
+ "ONE_TIME_PASSCODE_DETAILS_NO_CARRIER_%@"
+ "ONE_TIME_PASSCODE_DETAILS_NO_CARRIER_NO_PHONE_NUMBER"
+ "ONE_TIME_PASSCODE_DETAILS_NO_PHONE_NUMBER_%@"
+ "OneTimeCodeViewController nil @%s"
+ "OneTimeViewController active. Updating OTP state. @%s"
+ "OtpStateKey"
+ "Q&"
+ "RENEW_ONE_TIME_PASSCODE"
+ "ResumeTransferProxCardKey"
+ "SSOBLinkTrayButton"
+ "SSUserConsentViewController"
+ "SettingsCellular"
+ "T@\"NSString\",&,V_details"
+ "T@\"NSString\",&,V_mainText"
+ "T@\"NSString\",&,V_sourceIccid"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,V_type"
+ "T@\"OBLinkTrayButton\",&,V_skipButton"
+ "T@\"SSOBBoldTrayButton\",&,V_continueButton"
+ "T@\"SSOBLinkTrayButton\",&,V_resendOTPButton"
+ "T@\"TSTermsAndConditionsViewController\",W,V_termsAndConditionsViewController"
+ "T@\"TSTransferOneTimeCodeViewController\",W,V_oneTimeCodeViewController"
+ "T@\"UIButton\",&,V_acceptButton"
+ "T@\"UIButton\",&,V_declineButton"
+ "T@\"UITextField\",&,V_otpEditor"
+ "T@\"UITextView\",&,V_textView"
+ "TB,V_isHiding"
+ "TB,V_isResumingAfterPause"
+ "TB,V_isSourceProxCardVisible"
+ "TB,V_oneTimePasscodePaneShown"
+ "TB,V_otpDetectorNeeded"
+ "TB,V_termsAndConditionsShown"
+ "TB,V_usePin"
+ "TCMainTextKey"
+ "TCStateKey"
+ "TQ,V_flowType"
+ "TRANSFER_ACTION"
+ "TRANSFER_ERROR_MAX_OTP_ATTEMPTS_EXHAUSTED_DETAIL_%@"
+ "TRANSFER_ERROR_MAX_OTP_ATTEMPTS_EXHAUSTED_DETAIL_NO_CARRIER"
+ "TRANSFER_ERROR_MAX_PIN_ATTEMPTS_EXHAUSTED_DETAIL_%@"
+ "TRANSFER_ERROR_MAX_PIN_ATTEMPTS_EXHAUSTED_DETAIL_NO_CARRIER"
+ "TSProximitySourceTransferFlow hidden @%s"
+ "TSTermsAndConditionsViewController"
+ "TSTransferOneTimeCodeViewController"
+ "TURN_ON_WIFI_TO_PURCHASE_PLAN"
+ "UpdateProxCardVisibility"
+ "UsePinKey"
+ "[Db] Root flow : %@ @%s"
+ "[Db] stop timer @%s"
+ "[E]Unexpected transferEventUpdate for resuming prox card @%s"
+ "[E]handleTermsAndConditionsCompleted failed : %@ @%s"
+ "[E]handleUserEnteredOtp failed : %@ @%s"
+ "[E]invalid navigationController @%s"
+ "[E]present notification failed:%d @%s"
+ "[E]renewOneTimePassword failed : %@ @%s"
+ "[I] No postdata for: %@ @%s"
+ "_acceptClicked:"
+ "_alertConsentWithCompletion:"
+ "_assertionCounter: %d, caller:%@ @%s"
+ "_cancelButtonTapped:"
+ "_cancelTransfer:"
+ "_changeOtpTextFieldState:"
+ "_continueButtonTapped:"
+ "_declineButton"
+ "_details"
+ "_displayOneTimeCodeViewController:carrierName:usePin:"
+ "_displayTermsAndConditionsViewController:"
+ "_displayUserConsentAlert:"
+ "_flowWithOptions:"
+ "_getSFSafariViewControllerWithURL:"
+ "_handleKeyboardPresentation:"
+ "_handleOtpStatusUpdate:"
+ "_hideKeyboard"
+ "_hideQRCodeOption"
+ "_isBootstrapAsserted"
+ "_isHiding"
+ "_isResumingAfterPause"
+ "_isSourceProxCardVisible"
+ "_keyboardWillHide:"
+ "_mainText"
+ "_oneTimeCodeViewController"
+ "_oneTimePasscodePaneShown"
+ "_otpDetectorNeeded"
+ "_otpEditor"
+ "_resendOTP"
+ "_resendOTPButton"
+ "_setupLayoutConstraint"
+ "_showPendingInstallItems"
+ "_skipButton"
+ "_skipUIDismissal"
+ "_sourceIccid"
+ "_stopTimerWithBackgroundTaskState:"
+ "_termsAndConditionsShown"
+ "_termsAndConditionsViewController"
+ "_textFieldDidChange"
+ "_textView"
+ "_type"
+ "_updateSourceProxCardState:"
+ "_usePin"
+ "addGestureRecognizer:"
+ "assertUserInPurchaseFlowStartOver:caller:"
+ "cancel event already handled @%s"
+ "cancelled otp verification @%s"
+ "configureWithDefaultBackground"
+ "constraintGreaterThanOrEqualToAnchor:constant:"
+ "continueButton"
+ "deassertUserInPurchaseFlowWithForce:caller:"
+ "declineButton"
+ "disableButtonsAndHideSpinnerText"
+ "endFlowGracefully:"
+ "getRootFlow"
+ "handleTermsAndConditionsCompleted:consented:completion:"
+ "handleUserEnteredOtp:otp:completion:"
+ "hideSpinner"
+ "hiding"
+ "iPadUIPolish"
+ "initForRemotePlan:carrierName:skipUIDismissal:"
+ "initForResumption"
+ "initWithFlow:navigationController:"
+ "initWithSkipActivatingPane:timerType:transferBackPlan:setupType:"
+ "initWithSourceIccid:mainText:"
+ "initWithSourceIccid:phoneNumber:carrierName:usePin:"
+ "initWithString:attributes:"
+ "initWithTarget:action:"
+ "initWithTitle:subtitle:otpDetectorNeeded:"
+ "isFirstResponder"
+ "isHiding"
+ "isResumingAfterPause"
+ "isSourceProxCardVisible"
+ "kTransferInformationSent"
+ "mainText"
+ "oneTimeCodeViewController"
+ "oneTimePasscodePaneShown"
+ "openPrefsURL:"
+ "openSensitiveURL:withOptions:error:"
+ "openURL failed with error: %s, isOpened:%d\n @%s"
+ "otpDetectorNeeded"
+ "otpEditor"
+ "plansDidUpdate:"
+ "prefs:root=MOBILE_DATA_SETTINGS_ID&path=CELLULAR"
+ "push : %@ on : %@ @%s"
+ "renewOneTimePassword:completion:"
+ "requested new OTP @%s"
+ "resendOTPButton"
+ "response flags = %lu @%s"
+ "setBorderStyle:"
+ "setContinueButton:"
+ "setDeclineButton:"
+ "setDetails:"
+ "setDismissButtonStyle:"
+ "setEditable:"
+ "setInputAccessoryView:"
+ "setIsHiding:"
+ "setIsResumingAfterPause:"
+ "setIsSourceProxCardVisible:"
+ "setItems:"
+ "setMainText:"
+ "setNavigationBarHidden:animated:"
+ "setOneTimeCodeViewController:"
+ "setOneTimePasscodePaneShown:"
+ "setOtpDetectorNeeded:"
+ "setOtpEditor:"
+ "setResendOTPButton:"
+ "setRole:"
+ "setScrollEdgeAppearance:"
+ "setSecureTextEntry:"
+ "setSkipButton:"
+ "setSourceIccid:"
+ "setStandardAppearance:"
+ "setTermsAndConditionsShown:"
+ "setTermsAndConditionsViewController:"
+ "setTextContentType:"
+ "setTextView:"
+ "setToolbarHidden:animated:"
+ "setToolbarItems:"
+ "setUsePin:"
+ "set_isBeingUsedForCellularServiceBootstrap:"
+ "showLoadFailureAlert:error:"
+ "showSpinner"
+ "showing"
+ "sizeToFit"
+ "skipButton"
+ "start timer on subflow %@ @%s"
+ "start timer: %f @%s"
+ "startTimer:"
+ "termsAndConditionsShown"
+ "termsAndConditionsViewController"
+ "textView"
+ "transfer option is %s @%s"
+ "transfer state : %ld @%s"
+ "updateOtpState:"
+ "updateSourceProxCardState:"
+ "updating otpState to %ld @%s"
+ "usePin"
+ "v24@0:8@\"CTDisplayPlanList\"16"
+ "\xf0c"
- "\x01\x15\x14"
- "\x11\x12\x1d\x11\x11"
- "\x12\x11"
- "\x131r"
- "+[TSSIMSetupFlow bootstrapTransferFlowWithSession:transferablePlanOnSource:]_block_invoke"
- "+[TSSIMSetupFlow flowWithOptions:]"
- "+[TSSIMSetupFlow initWithAppName:requireSetup:]"
- "+[TSSIMSetupFlow initWithAppName:requireSetup:skipGeneralInstallConsent:]"
- "-[TSActivationFlowWithSimSetupFlow dealloc]"
- "-[TSActivationFlowWithSimSetupFlow initRequireSetup:transferBackPlan:]"
- "-[TSBuddyMLViewController _setUserInPurchaseFlow]"
- "-[TSBuddyMLViewController dealloc]"
- "-[TSQRCodeScanFlow dealloc]"
- "-[TSQRCodeScanFlow initWithBackButton:]"
- "-[TSSIMSetupPublicApiInstallFlow dealloc]"
- "-[TSSIMSetupPublicApiInstallFlow initWithAppName:requireSetup:skipGeneralInstallConsent:]"
- "-[TSTransferCloudFlow dealloc]"
- "-[TSTransferCloudFlow initWithProximitySetupState:]"
- "-[TSTransferFlow dealloc]"
- "-[TSTransferFlow initWithSession:hasTransferablePlan:isStandaloneProximityTransfer:transferBackPlan:]"
- "-[TSTransferFlow init]"
- "-[TSUserInPurchaseFlowAssertion assertUserInPurchaseFlowStartOver:]"
- "-[TSUserInPurchaseFlowAssertion deassertUserInPurchaseFlowWithForce:]"
- "@\"UIImagePickerController\""
- "@40@0:8@16{CGSize=dd}24"
- "Q'"
- "SIMSetupSupport/MagnoliaOverProximity iPadESIMProvisioningParity is %s @%s"
- "T@\"UIButton\",W,N,V_btOpenPhoto"
- "T@\"UIImagePickerController\",&,V_imagePicker"
- "T@\"UIImageView\",&,V_imageView"
- "UIImagePickerControllerDelegate"
- "[E]Missing / empty postdata for signup info: %@ @%s"
- "_assertionCounter: %d @%s"
- "_btOpenPhoto"
- "_decodeQR:"
- "_imagePicker"
- "_imageView"
- "_startTimer:"
- "_stopTimer"
- "assert in purchase flow @%s"
- "assertUserInPurchaseFlowStartOver:"
- "bootstrap completed. show = %d @%s"
- "bootstrapTransferFlowWithSession:transferablePlanOnSource:"
- "btOpenPhoto"
- "context"
- "de-assert in purchase flow @%s"
- "deassertUserInPurchaseFlowWithForce:"
- "detectorOfType:context:options:"
- "featuresInImage:options:"
- "imagePicker"
- "imagePickerController:didFinishPickingImage:editingInfo:"
- "imagePickerController:didFinishPickingMediaWithInfo:"
- "imagePickerControllerDidCancel:"
- "imageWithCGImage:"
- "imageWithImage:scaledToFillSize:"
- "initForRemotePlan:carrierName:"
- "initWithAppName:requireSetup:"
- "messageString"
- "openPhotoTapped:"
- "properties"
- "readableContentGuide"
- "setBtOpenPhoto:"
- "setImagePicker:"
- "setImageView:"
- "setSourceType:"
- "showLoadFailureAlert:"
- "v24@0:8@\"UIImagePickerController\"16"
- "v32@0:8@\"UIImagePickerController\"16@\"NSDictionary\"24"
- "v40@0:8@\"UIImagePickerController\"16@\"UIImage\"24@\"NSDictionary\"32"
- "\xf0a"

```
