## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-52.0.0.0.0
-  __TEXT.__text: 0x4e5b4
-  __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x70e4
-  __TEXT.__const: 0x4c4
-  __TEXT.__oslogstring: 0x211f
-  __TEXT.__cstring: 0x2d45
-  __TEXT.__gcc_except_tab: 0x7a0
+54.0.0.0.0
+  __TEXT.__text: 0x4cd3c
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x6e34
+  __TEXT.__const: 0x4b4
+  __TEXT.__oslogstring: 0x219f
+  __TEXT.__cstring: 0x2d65
+  __TEXT.__gcc_except_tab: 0x750
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0xa8
   __TEXT.__swift5_typeref: 0x1b6

   __TEXT.__swift5_fieldmd: 0x54
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1568
+  __TEXT.__unwind_info: 0x14f0
   __TEXT.__eh_frame: 0x480
-  __TEXT.__objc_classname: 0x117b
-  __TEXT.__objc_methname: 0x14452
-  __TEXT.__objc_methtype: 0x4932
-  __TEXT.__objc_stubs: 0xd280
-  __DATA_CONST.__got: 0xec0
-  __DATA_CONST.__const: 0x1038
-  __DATA_CONST.__objc_classlist: 0x310
+  __TEXT.__objc_classname: 0x113b
+  __TEXT.__objc_methname: 0x13f95
+  __TEXT.__objc_methtype: 0x46bf
+  __TEXT.__objc_stubs: 0xcf60
+  __DATA_CONST.__got: 0xea8
+  __DATA_CONST.__const: 0x10f8
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48d0
+  __DATA_CONST.__objc_selrefs: 0x47d8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x2f60
-  __AUTH_CONST.__objc_const: 0x11430
+  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x2ea0
+  __AUTH_CONST.__objc_const: 0x10820
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0x1bf0
+  __AUTH.__objc_data: 0x1b00
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x5ec
+  __DATA.__objc_ivar: 0x5c0
   __DATA.__data: 0x13f8
   __DATA.__bss: 0x260
   __DATA.__common: 0x18

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
+  - /System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI
   - /System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A822DAFB-DDCF-382E-8A65-710E5E2211F0
-  Functions: 2183
-  Symbols:   8209
-  CStrings:  4634
+  UUID: 183B50A7-A09D-3B78-8C6D-A01A404D75D2
+  Functions: 2134
+  Symbols:   8042
+  CStrings:  4564
 
Symbols:
+ -[DMCBYODEnrollmentFlowUIPresenter ensureNetworkConnectionWithCompletionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter requestDevicePasscodeDataWithCompletionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter(Test) receivedProfile:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper isExtractableContext]
+ -[DMCEnrollmentFlowManagedConfigurationHelper setIsExtractableContext:]
+ -[DMCEnrollmentFlowUIPresenterBase passcodeContext]
+ -[DMCEnrollmentFlowUIPresenterBase setPasscodeContext:]
+ -[DMCUnenrollmentFlowUIPresenter requestDevicePasscodeDataWithCompletionHandler:]
+ GCC_except_table17
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table51
+ GCC_except_table72
+ _LAPasscodeServiceErrorDomain
+ _OBJC_CLASS_$_DMCNetworkMonitor
+ _OBJC_CLASS_$_LAPasscodeVerificationService
+ _OBJC_CLASS_$_LAPasscodeVerificationServiceOptions
+ _OBJC_IVAR_$_DMCEnrollmentFlowManagedConfigurationHelper._isExtractableContext
+ _OBJC_IVAR_$_DMCEnrollmentFlowUIPresenterBase._passcodeContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_DMCEnrollmentFlowPasscodeRequestPresenter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCEnrollmentFlowPasscodeRequestPresenter
+ __OBJC_$_PROTOCOL_REFS_DMCEnrollmentFlowPasscodeRequestPresenter
+ __OBJC_LABEL_PROTOCOL_$_DMCEnrollmentFlowPasscodeRequestPresenter
+ __OBJC_PROTOCOL_$_DMCEnrollmentFlowPasscodeRequestPresenter
+ ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.48
+ ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.49
+ ___118-[DMCBYODEnrollmentFlowUIPresenter requestWebAuthenticationWithWebAuthURL:authenticator:authParams:completionHandler:]_block_invoke.67
+ ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke.71
+ ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_2.72
+ ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_3.75
+ ___202-[DMCEnrollmentFlowManagedConfigurationHelper manageApplicationWithBundleID:iTunesItemID:organization:personaID:associatedDomains:associatedDomainsEnableDirectDownloads:configuration:completionHandler:]_block_invoke.43
+ ___81-[DMCUnenrollmentFlowUIPresenter requestDevicePasscodeDataWithCompletionHandler:]_block_invoke
+ ___83-[DMCBYODEnrollmentFlowUIPresenter requestDevicePasscodeDataWithCompletionHandler:]_block_invoke
+ ___84-[DMCEnrollmentFlowManagedConfigurationHelper _mdmV1AppsInstallationStateDidChange:]_block_invoke.69
+ ___90-[DMCEnrollmentFlowManagedConfigurationHelper awaitDeviceConfiguredWithCompletionHandler:]_block_invoke.109
+ ___93-[DMCEnrollmentFlowManagedConfigurationHelper _systemAppDeletableInstallationStateDidChange:]_block_invoke.100
+ ___94-[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequestNeedsExtractablePasscode:]_block_invoke_4
+ ___95-[DMCEnrollmentFlowUIPresenterBase requestDevicePasscodeWithDescriptionText:completionHandler:]_block_invoke.6
+ ___95-[DMCEnrollmentFlowUIPresenterBase requestDevicePasscodeWithDescriptionText:completionHandler:]_block_invoke_2
+ ___block_descriptor_32_e22_v24?0"NSData"8B16B20l
+ ___block_descriptor_40_e8_32bs_e19_v20?0"NSData"8B16ls32l8
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e31_v24?0"LAContext"8"NSError"16lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.108
+ ___block_literal_global.111
+ _objc_msgSend$credentialOfType:reply:
+ _objc_msgSend$deviceMightHaveNetworkStrict:
+ _objc_msgSend$installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:
+ _objc_msgSend$receivedProfile:
+ _objc_msgSend$requestDevicePasscodeContextNeedsExtractable:completionHandler:
+ _objc_msgSend$setIsExtractableContext:
+ _objc_msgSend$setPasscodeSubPrompt:
+ _objc_msgSend$startInParentVC:options:completion:
- -[DMCBYODEnrollmentFlowUIPresenter requestDevicePasscodeWithCompletionHandler:]
- -[DMCBYODEnrollmentFlowUIPresenter(Test) ensureNetworkConnectionWithCompletionHandler:]
- -[DMCBYODEnrollmentFlowUIPresenter(Test) recievedProfile:]
- -[DMCDevicePINPane .cxx_destruct]
- -[DMCDevicePINPane _textFont]
- -[DMCDevicePINPane descriptionLabel]
- -[DMCDevicePINPane initWithFrame:]
- -[DMCDevicePINPane passcodeField]
- -[DMCDevicePINPane setStyle:]
- -[DMCDevicePINPane setTitle:]
- -[DMCDevicePINPane setTitleText:]
- -[DMCDevicePINPane style]
- -[DMCDevicePINPane titleText]
- -[DMCEnrollmentFlowManagedConfigurationHelper installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:]
- -[DMCEnrollmentFlowUIPresenterBase didAcceptEnteredPIN:]
- -[DMCEnrollmentFlowUIPresenterBase didCancelEnteringPIN]
- -[DMCEnrollmentFlowUIPresenterBase passcodeCompletionHandler]
- -[DMCEnrollmentFlowUIPresenterBase pinEntryViewController]
- -[DMCEnrollmentFlowUIPresenterBase setPasscodeCompletionHandler:]
- -[DMCEnrollmentFlowUIPresenterBase setPinEntryViewController:]
- -[DMCPINEntryViewController .cxx_destruct]
- -[DMCPINEntryViewController _titleFont]
- -[DMCPINEntryViewController _updateStyle]
- -[DMCPINEntryViewController delegate]
- -[DMCPINEntryViewController descriptionText]
- -[DMCPINEntryViewController dmc_viewControllerHasBeenDismissed]
- -[DMCPINEntryViewController inProgress]
- -[DMCPINEntryViewController initWithStyle:]
- -[DMCPINEntryViewController leftBarButtonTapped:]
- -[DMCPINEntryViewController loadView]
- -[DMCPINEntryViewController presentationControllerDidAttemptToDismiss:]
- -[DMCPINEntryViewController rightBarButtonItem]
- -[DMCPINEntryViewController setDelegate:]
- -[DMCPINEntryViewController setDescriptionText:]
- -[DMCPINEntryViewController setInProgress:]
- -[DMCPINEntryViewController setRightBarButtonItem:]
- -[DMCPINEntryViewController setSubviewLayoutFrame:]
- -[DMCPINEntryViewController setTitleLabel:]
- -[DMCPINEntryViewController stringsBundle]
- -[DMCPINEntryViewController style]
- -[DMCPINEntryViewController subviewLayoutFrame]
- -[DMCPINEntryViewController titleLabel]
- -[DMCPINEntryViewController viewWillAppear:]
- -[DMCPINEntryViewController viewWillLayoutSubviews]
- -[DMCTestNetworkMonitor .cxx_destruct]
- -[DMCTestNetworkMonitor availableHanlder]
- -[DMCTestNetworkMonitor initWithNetworkAvailableHandler:]
- -[DMCTestNetworkMonitor isNetworkAvailableWithFlags:]
- -[DMCTestNetworkMonitor reachability]
- -[DMCTestNetworkMonitor setAvailableHanlder:]
- -[DMCTestNetworkMonitor setReachability:]
- -[DMCTestNetworkMonitor startMonitoring]
- -[DMCTestNetworkMonitor verifyNetworkFlags:]
- -[DMCUnenrollmentFlowUIPresenter requestDevicePasscodeWithCompletionHandler:]
- GCC_except_table15
- GCC_except_table24
- GCC_except_table25
- GCC_except_table50
- GCC_except_table70
- OBJC_IVAR_$_DevicePINController._mode
- OBJC_IVAR_$_DevicePINPane._pinView
- _CFRunLoopGetMain
- _OBJC_CLASS_$_DMCDevicePINPane
- _OBJC_CLASS_$_DMCPINEntryViewController
- _OBJC_CLASS_$_DMCTestNetworkMonitor
- _OBJC_CLASS_$_DevicePINController
- _OBJC_CLASS_$_DevicePINPane
- _OBJC_IVAR_$_DMCDevicePINPane._style
- _OBJC_IVAR_$_DMCDevicePINPane._titleText
- _OBJC_IVAR_$_DMCEnrollmentFlowUIPresenterBase._passcodeCompletionHandler
- _OBJC_IVAR_$_DMCEnrollmentFlowUIPresenterBase._pinEntryViewController
- _OBJC_IVAR_$_DMCPINEntryViewController._delegate
- _OBJC_IVAR_$_DMCPINEntryViewController._descriptionText
- _OBJC_IVAR_$_DMCPINEntryViewController._inProgress
- _OBJC_IVAR_$_DMCPINEntryViewController._rightBarButtonItem
- _OBJC_IVAR_$_DMCPINEntryViewController._style
- _OBJC_IVAR_$_DMCPINEntryViewController._subviewLayoutFrame
- _OBJC_IVAR_$_DMCPINEntryViewController._titleLabel
- _OBJC_IVAR_$_DMCTestNetworkMonitor._availableHanlder
- _OBJC_IVAR_$_DMCTestNetworkMonitor._reachability
- _OBJC_METACLASS_$_DMCDevicePINPane
- _OBJC_METACLASS_$_DMCPINEntryViewController
- _OBJC_METACLASS_$_DMCTestNetworkMonitor
- _OBJC_METACLASS_$_DevicePINController
- _OBJC_METACLASS_$_DevicePINPane
- _SCNetworkReachabilityCreateWithOptions
- _SCNetworkReachabilityGetFlags
- _SCNetworkReachabilityScheduleWithRunLoop
- _SCNetworkReachabilitySetCallback
- _SCNetworkReachabilityUnscheduleFromRunLoop
- __OBJC_$_INSTANCE_METHODS_DMCDevicePINPane
- __OBJC_$_INSTANCE_METHODS_DMCPINEntryViewController
- __OBJC_$_INSTANCE_METHODS_DMCTestNetworkMonitor
- __OBJC_$_INSTANCE_VARIABLES_DMCDevicePINPane
- __OBJC_$_INSTANCE_VARIABLES_DMCPINEntryViewController
- __OBJC_$_INSTANCE_VARIABLES_DMCTestNetworkMonitor
- __OBJC_$_PROP_LIST_DMCDevicePINPane
- __OBJC_$_PROP_LIST_DMCPINEntryViewController
- __OBJC_$_PROP_LIST_DMCTestNetworkMonitor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIAdaptivePresentationControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIAdaptivePresentationControllerDelegate
- __OBJC_$_PROTOCOL_REFS_UIAdaptivePresentationControllerDelegate
- __OBJC_CLASS_PROTOCOLS_$_DMCEnrollmentFlowUIPresenterBase
- __OBJC_CLASS_PROTOCOLS_$_DMCPINEntryViewController
- __OBJC_CLASS_RO_$_DMCDevicePINPane
- __OBJC_CLASS_RO_$_DMCPINEntryViewController
- __OBJC_CLASS_RO_$_DMCTestNetworkMonitor
- __OBJC_LABEL_PROTOCOL_$_UIAdaptivePresentationControllerDelegate
- __OBJC_METACLASS_RO_$_DMCDevicePINPane
- __OBJC_METACLASS_RO_$_DMCPINEntryViewController
- __OBJC_METACLASS_RO_$_DMCTestNetworkMonitor
- __OBJC_PROTOCOL_$_UIAdaptivePresentationControllerDelegate
- ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.45
- ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.46
- ___118-[DMCBYODEnrollmentFlowUIPresenter requestWebAuthenticationWithWebAuthURL:authenticator:authParams:completionHandler:]_block_invoke.60
- ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke.65
- ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_2.66
- ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_3.69
- ___202-[DMCEnrollmentFlowManagedConfigurationHelper manageApplicationWithBundleID:iTunesItemID:organization:personaID:associatedDomains:associatedDomainsEnableDirectDownloads:configuration:completionHandler:]_block_invoke.40
- ___34-[DMCDevicePINPane initWithFrame:]_block_invoke
- ___43-[DMCPINEntryViewController initWithStyle:]_block_invoke
- ___56-[DMCEnrollmentFlowUIPresenterBase didAcceptEnteredPIN:]_block_invoke
- ___56-[DMCEnrollmentFlowUIPresenterBase didAcceptEnteredPIN:]_block_invoke_2
- ___56-[DMCEnrollmentFlowUIPresenterBase didCancelEnteringPIN]_block_invoke
- ___57-[DMCTestNetworkMonitor initWithNetworkAvailableHandler:]_block_invoke
- ___84-[DMCEnrollmentFlowManagedConfigurationHelper _mdmV1AppsInstallationStateDidChange:]_block_invoke.66
- ___87-[DMCBYODEnrollmentFlowUIPresenter(Test) ensureNetworkConnectionWithCompletionHandler:]_block_invoke
- ___87-[DMCBYODEnrollmentFlowUIPresenter(Test) ensureNetworkConnectionWithCompletionHandler:]_block_invoke_2
- ___90-[DMCEnrollmentFlowManagedConfigurationHelper awaitDeviceConfiguredWithCompletionHandler:]_block_invoke.104
- ___93-[DMCEnrollmentFlowManagedConfigurationHelper _systemAppDeletableInstallationStateDidChange:]_block_invoke.97
- ___block_literal_global.106
- __networkReachabilityCallback
- _kCFRunLoopCommonModes
- _kDevicePINControllerDelegate
- _objc_msgSend$_updateStyle
- _objc_msgSend$availableHanlder
- _objc_msgSend$bringSubviewToFront:
- _objc_msgSend$descriptionLabel
- _objc_msgSend$descriptionText
- _objc_msgSend$didCancelEnteringPIN
- _objc_msgSend$initWithNetworkAvailableHandler:
- _objc_msgSend$installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:
- _objc_msgSend$isNetworkAvailableWithFlags:
- _objc_msgSend$numberWithInt:
- _objc_msgSend$pane
- _objc_msgSend$passcodeCompletionHandler
- _objc_msgSend$passcodeField
- _objc_msgSend$pinEntryViewController
- _objc_msgSend$recievedProfile:
- _objc_msgSend$setAdjustsFontSizeToFitWidth:
- _objc_msgSend$setAvailableHanlder:
- _objc_msgSend$setDescriptionText:
- _objc_msgSend$setHidesNavigationButtons:
- _objc_msgSend$setMinimumScaleFactor:
- _objc_msgSend$setNavigationBarHidden:animated:
- _objc_msgSend$setPane:
- _objc_msgSend$setPasscodeCompletionHandler:
- _objc_msgSend$setPinEntryViewController:
- _objc_msgSend$setSubviewLayoutFrame:
- _objc_msgSend$setTitle:font:
- _objc_msgSend$setTitleLabel:
- _objc_msgSend$simplePIN
- _objc_msgSend$startMonitoring
- _objc_msgSend$style
- _objc_msgSend$titleText
- _objc_msgSend$valueForKeyPath:
- _objc_msgSend$verifyNetworkFlags:
CStrings:
+ "@\"LAContext\""
+ "BYCloudConfigRetrieveProfileFromWebErrorDomain"
+ "DMCEnrollmentFlowPasscodeRequestPresenter"
+ "DMC_ENROLLMENT_NO_NETWORK"
+ "Failed to get extractable password: %{public}@"
+ "LAPasscodeVerificationService canceled by user"
+ "LAPasscodeVerificationService failed: %{public}@"
+ "T@\"LAContext\",&,N,V_passcodeContext"
+ "TB,N,V_isExtractableContext"
+ "_isExtractableContext"
+ "_passcodeContext"
+ "credentialOfType:reply:"
+ "deviceMightHaveNetworkStrict:"
+ "did not receive download response!"
+ "installEnrollmentProfile:devicePasscode:devicePasscodeContext:passcodeContextExtractable:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
+ "isExtractableContext"
+ "passcodeContext"
+ "received 403 response from website!"
+ "received 404 response from website!"
+ "receivedProfile:"
+ "requestDevicePasscodeContextNeedsExtractable:completionHandler:"
+ "requestMDMUsernameAndPasswordWithErrorMessage:completionHandler:"
+ "setIsExtractableContext:"
+ "setPasscodeContext:"
+ "setPasscodeSubPrompt:"
+ "startInParentVC:options:completion:"
+ "v20@?0@\"NSData\"8B16"
+ "v24@?0@\"LAContext\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8B16B20"
+ "v28@0:8B16@?<v@?@\"NSData\"BB>20"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSString\"B>24"
+ "v96@0:8@\"NSData\"16@\"NSString\"24@\"NSData\"32B40@\"NSString\"44@\"NSString\"52B60@\"NSNumber\"64@\"NSArray\"72@\"NSString\"80@?<v@?@\"NSString\"B@\"NSError\">88"
+ "v96@0:8@16@24@32B40@44@52B60@64@72@80@?88"
- "@\"<DevicePINControllerDelegate>\""
- "@\"DMCPINEntryViewController\""
- "@\"UIBarButtonItem\""
- "@\"UIViewController\"32@0:8@\"UIPresentationController\"16q24"
- "@24@0:8@?16"
- "B20@0:8I16"
- "B24@0:8@\"UIPresentationController\"16"
- "BYCloudConfigRetreiveProfileFromWebErrorDomain"
- "DMCDevicePINPane"
- "DMCPINEntryViewController"
- "DMCTestNetworkMonitor"
- "Network is available."
- "ResolverBypass"
- "T@\"<DevicePINControllerDelegate>\",W,N,V_delegate"
- "T@\"DMCPINEntryViewController\",&,N,V_pinEntryViewController"
- "T@\"NSString\",C,N,V_descriptionText"
- "T@\"UIBarButtonItem\",&,N,V_rightBarButtonItem"
- "T@\"UILabel\",&,N,V_titleLabel"
- "T@\"UIView\",R,N"
- "T@?,C,N,V_availableHanlder"
- "T@?,C,N,V_passcodeCompletionHandler"
- "TQ,R,N,V_style"
- "T^{__SCNetworkReachability=},N,V_reachability"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_subviewLayoutFrame"
- "UIAdaptivePresentationControllerDelegate"
- "UI_ENTER_PASSCODE"
- "^{__SCNetworkReachability=}"
- "^{__SCNetworkReachability=}16@0:8"
- "_availableHanlder"
- "_descriptionText"
- "_passcodeCompletionHandler"
- "_pinEntryViewController"
- "_pinView._passcodeField"
- "_pinView._titleLabel"
- "_reachability"
- "_rightBarButtonItem"
- "_subviewLayoutFrame"
- "_titleLabel"
- "_updateStyle"
- "adaptivePresentationStyleForPresentationController:"
- "adaptivePresentationStyleForPresentationController:traitCollection:"
- "availableHanlder"
- "bringSubviewToFront:"
- "descriptionLabel"
- "descriptionText"
- "did not recieve download response!"
- "initWithNetworkAvailableHandler:"
- "installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
- "isNetworkAvailableWithFlags:"
- "nodename"
- "numberWithInt:"
- "pane"
- "passcodeCompletionHandler"
- "passcodeField"
- "pinEntryViewController"
- "presentationController:prepareAdaptivePresentationController:"
- "presentationController:viewControllerForAdaptivePresentationStyle:"
- "presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:"
- "presentationControllerDidAttemptToDismiss:"
- "presentationControllerDidDismiss:"
- "presentationControllerShouldDismiss:"
- "presentationControllerWillDismiss:"
- "q24@0:8@\"UIPresentationController\"16"
- "q32@0:8@\"UIPresentationController\"16@\"UITraitCollection\"24"
- "reachability"
- "recieved 403 response from website!"
- "recieved 404 response from website!"
- "recievedProfile:"
- "setAdjustsFontSizeToFitWidth:"
- "setAvailableHanlder:"
- "setDescriptionText:"
- "setHidesNavigationButtons:"
- "setMinimumScaleFactor:"
- "setNavigationBarHidden:animated:"
- "setPane:"
- "setPasscodeCompletionHandler:"
- "setPinEntryViewController:"
- "setReachability:"
- "setSubviewLayoutFrame:"
- "setTitle:font:"
- "setTitleLabel:"
- "simplePIN"
- "startMonitoring"
- "stringsBundle"
- "subviewLayoutFrame"
- "v24@0:8@\"UIPresentationController\"16"
- "v24@0:8^{__SCNetworkReachability=}16"
- "v32@0:8@\"UIPresentationController\"16@\"UIPresentationController\"24"
- "v40@0:8@\"UIPresentationController\"16q24@\"<UIViewControllerTransitionCoordinator>\"32"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v92@0:8@\"NSData\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48B56@\"NSNumber\"60@\"NSArray\"68@\"NSString\"76@?<v@?@\"NSString\"B@\"NSError\">84"
- "v92@0:8@16@24@32@40@48B56@60@68@76@?84"
- "valueForKeyPath:"
- "verifyNetworkFlags:"
- "www.apple.com"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
