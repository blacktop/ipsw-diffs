## AppleMediaServicesUI

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI`

```diff

-5.1.8.2.2
-  __TEXT.__text: 0x1180b8
-  __TEXT.__auth_stubs: 0x2310
-  __TEXT.__objc_methlist: 0xc450
-  __TEXT.__const: 0x3d04
-  __TEXT.__cstring: 0x9414
-  __TEXT.__oslogstring: 0x888c
-  __TEXT.__gcc_except_tab: 0x10f4
+5.2.13.2.1
+  __TEXT.__text: 0x11a3bc
+  __TEXT.__auth_stubs: 0x2320
+  __TEXT.__objc_methlist: 0xc628
+  __TEXT.__const: 0x3d54
+  __TEXT.__cstring: 0x9724
+  __TEXT.__oslogstring: 0x8a67
+  __TEXT.__gcc_except_tab: 0x10d4
   __TEXT.__dlopen_cstrs: 0xbb6
-  __TEXT.__swift5_typeref: 0x3cc2
-  __TEXT.__swift5_reflstr: 0x10a8
+  __TEXT.__swift5_typeref: 0x3d36
+  __TEXT.__swift5_reflstr: 0x10b8
   __TEXT.__swift5_assocty: 0x930
-  __TEXT.__constg_swiftt: 0x1dfc
-  __TEXT.__swift5_fieldmd: 0xf58
+  __TEXT.__constg_swiftt: 0x1e84
+  __TEXT.__swift5_fieldmd: 0xf90
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_capture: 0x66c
+  __TEXT.__swift5_capture: 0x67c
   __TEXT.__swift5_proto: 0x1d0
-  __TEXT.__swift5_types: 0x15c
+  __TEXT.__swift5_types: 0x164
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4f34
+  __TEXT.__unwind_info: 0x4fc4
   __TEXT.__eh_frame: 0x1138
-  __TEXT.__objc_classname: 0x2149
-  __TEXT.__objc_methname: 0x21224
-  __TEXT.__objc_methtype: 0x6b7d
-  __TEXT.__objc_stubs: 0x18120
+  __TEXT.__objc_classname: 0x216e
+  __TEXT.__objc_methname: 0x216bc
+  __TEXT.__objc_methtype: 0x6bb8
+  __TEXT.__objc_stubs: 0x18500
   __DATA_CONST.__got: 0x848
   __DATA_CONST.__const: 0x3478
-  __DATA_CONST.__objc_classlist: 0x818
+  __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18378
-  __DATA_CONST.__objc_selrefs: 0x7380
+  __DATA_CONST.__objc_const: 0x18588
+  __DATA_CONST.__objc_selrefs: 0x74a8
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__objc_const: 0x54f8
-  __AUTH_CONST.__cfstring: 0x9be0
-  __AUTH_CONST.__const: 0x4d88
-  __AUTH_CONST.__objc_intobj: 0x2b8
+  __AUTH_CONST.__objc_const: 0x5588
+  __AUTH_CONST.__cfstring: 0x9dc0
+  __AUTH_CONST.__const: 0x4de8
+  __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_ptr: 0x108
-  __AUTH_CONST.__auth_got: 0x1198
-  __AUTH.__objc_data: 0x47c8
-  __AUTH.__data: 0x2b00
+  __AUTH_CONST.__auth_ptr: 0x110
+  __AUTH_CONST.__auth_got: 0x11a0
+  __AUTH.__objc_data: 0x49b0
+  __AUTH.__data: 0x2b50
   __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0xe00
+  __DATA.__objc_classrefs: 0xe18
   __DATA.__objc_superrefs: 0x630
-  __DATA.__objc_ivar: 0xed0
+  __DATA.__objc_ivar: 0xee8
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x3098
+  __DATA.__data: 0x30d8
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x3ef0
   __DATA.__common: 0x60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8659
-  Symbols:   18610
-  CStrings:  8572
+  Functions: 8721
+  Symbols:   18735
+  CStrings:  8653
 
Symbols:
+ +[AMSUIParentalVerificationApplePayTask _walletHasValidSetup:paymentRequest:]
+ -[AMSUIAuthenticateTaskCoordinator _authenticateTaskForItem:]
+ -[AMSUIAuthenticateTaskCoordinator _authenticateTaskForItem:authenticationResults:]
+ -[AMSUIAuthenticateTaskCoordinator handleRequest:presentingViewController:]
+ -[AMSUIBaseMessageViewController _debugInfoIsNotEmpty]
+ -[AMSUIBaseMessageViewController _presentDebugMenu]
+ -[AMSUIBaseMessageViewController _setupDebugMenu]
+ -[AMSUIMessageView debugButton]
+ -[AMSUIMessageView setDebugButton:]
+ -[AMSUIMessageView setupDebugButtonWithTarget:action:]
+ -[AMSUIMessageViewLayoutContext _calculateFooterButtonSizes]
+ -[AMSUIMessageViewLayoutContext _maxFooterButtonWidth]
+ -[AMSUIMessageViewLayoutContext _maxTextContainerWidth]
+ -[AMSUIMessageViewLayoutContext debugButtonFrame]
+ -[AMSUIMessageViewLayoutContext debugButtonSize]
+ -[AMSUIMessageViewLayoutContext setDebugButtonFrame:]
+ -[AMSUIMessageViewLayoutContext setDebugButtonSize:]
+ -[AMSUIWebBagAction account]
+ -[AMSUIWebBagAction setAccount:]
+ -[AMSUIWebCameraReaderPageModel prefersSessionTeardown]
+ -[AMSUIWebCameraReaderPageModel setPrefersSessionTeardown:]
+ -[AMSUIWebCameraReaderViewController _setupCameraReader]
+ -[AMSUIWebCameraReaderViewController viewDidDisappear:]
+ -[AMSUIWebClientContext reducedMemoryMode]
+ -[AMSUIWebClientContext setReducedMemoryMode:]
+ -[AMSUIWebPlaceholderViewController removeSnapshot]
+ -[AMSUIWebSnapshotView removeSnapshot]
+ -[AMSUIWebViewController reducedMemoryMode]
+ -[AMSUIWebViewController setReducedMemoryMode:]
+ GCC_except_table101
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table30
+ GCC_except_table53
+ GCC_except_table80
+ GCC_except_table85
+ GCC_except_table88
+ GCC_except_table95
+ _OBJC_CLASS_$_AMSAuthenticateTaskCoordinator
+ _OBJC_CLASS_$_AMSUIAuthenticateTaskCoordinator
+ _OBJC_CLASS_$_AMSUIDebugMenu
+ _OBJC_CLASS_$__TtC20AppleMediaServicesUI22DebugMenuBarButtonItem
+ _OBJC_IVAR_$_AMSUIMessageView._debugButton
+ _OBJC_IVAR_$_AMSUIMessageViewLayoutContext._debugButtonFrame
+ _OBJC_IVAR_$_AMSUIMessageViewLayoutContext._debugButtonSize
+ _OBJC_IVAR_$_AMSUIWebBagAction._account
+ _OBJC_IVAR_$_AMSUIWebCameraReaderPageModel._prefersSessionTeardown
+ _OBJC_IVAR_$_AMSUIWebClientContext._reducedMemoryMode
+ _OBJC_METACLASS_$_AMSAuthenticateTaskCoordinator
+ _OBJC_METACLASS_$_AMSUIAuthenticateTaskCoordinator
+ _OBJC_METACLASS_$_AMSUIDebugMenu
+ _OBJC_METACLASS_$_UIBarButtonItem
+ _OBJC_METACLASS_$__TtC20AppleMediaServicesUI22DebugMenuBarButtonItem
+ __DATA_AMSUIDebugMenu
+ __DATA__TtC20AppleMediaServicesUI22DebugMenuBarButtonItem
+ __IVARS__TtC20AppleMediaServicesUI22DebugMenuBarButtonItem
+ __METACLASS_DATA_AMSUIDebugMenu
+ __METACLASS_DATA__TtC20AppleMediaServicesUI22DebugMenuBarButtonItem
+ __OBJC_$_CLASS_METHODS_AMSUIDebugMenu
+ __OBJC_$_INSTANCE_METHODS_AMSUIAuthenticateTaskCoordinator
+ __OBJC_$_INSTANCE_METHODS_AMSUIDebugMenu
+ __OBJC_$_INSTANCE_METHODS__TtC20AppleMediaServicesUI22DebugMenuBarButtonItem
+ __OBJC_CLASS_RO_$_AMSUIAuthenticateTaskCoordinator
+ __OBJC_METACLASS_RO_$_AMSUIAuthenticateTaskCoordinator
+ ___39-[AMSUIWebSafariViewController _share:]_block_invoke.78
+ ___39-[AMSUIWebSafariViewController _share:]_block_invoke_2.82
+ ___51-[AMSUIBaseMessageViewController _setImageWithURL:]_block_invoke.55
+ ___51-[AMSUIBaseMessageViewController _setImageWithURL:]_block_invoke.57
+ ___56-[AMSUIBaseMessageViewController _loadIconAssetWithURL:]_block_invoke.48
+ ___59-[AMSUIBaseMessageViewController _setMICAIconAssetWithURL:]_block_invoke.50
+ ___59-[AMSUIBaseMessageViewController _setMICAIconAssetWithURL:]_block_invoke.52
+ ___60-[AMSUIMessageViewLayoutContext _calculateFooterButtonSizes]_block_invoke
+ ___60-[AMSUIPaymentVerificationTokenFetchTask performWebFlowTask]_block_invoke.63
+ ___77-[AMSUIPaymentVerificationTokenFetchTask performApplePayTaskWithFeatureFlag:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e43_v24?0"AMSAuthenticateResult"8"NSError"16ls32l8s40l8
+ ___block_literal_global.127
+ _objc_msgSend$_calculateFooterButtonSizes
+ _objc_msgSend$_debugInfoIsNotEmpty
+ _objc_msgSend$_maxFooterButtonWidth
+ _objc_msgSend$_maxTextContainerWidth
+ _objc_msgSend$_setupCameraReader
+ _objc_msgSend$_setupDebugMenu
+ _objc_msgSend$_walletHasValidSetup:paymentRequest:
+ _objc_msgSend$accesssControlRef
+ _objc_msgSend$configurationWithPointSize:
+ _objc_msgSend$debugButton
+ _objc_msgSend$debugButtonFrame
+ _objc_msgSend$debugButtonSize
+ _objc_msgSend$debugLogsEnabled
+ _objc_msgSend$evaluationMechanismsForAccessControl:operation:error:
+ _objc_msgSend$handleRequest:presentingViewController:
+ _objc_msgSend$handleRequestDictionary:
+ _objc_msgSend$initWithAuthenticationResults:presentingViewController:options:
+ _objc_msgSend$lightGrayColor
+ _objc_msgSend$prefersSessionTeardown
+ _objc_msgSend$presentDebugMenuWithPresentingVC:debugInfo:
+ _objc_msgSend$reducedMemoryMode
+ _objc_msgSend$removeSnapshot
+ _objc_msgSend$setDebugButtonFrame:
+ _objc_msgSend$setDebugButtonSize:
+ _objc_msgSend$setEndPoint:
+ _objc_msgSend$setImage:forState:
+ _objc_msgSend$setLocalizedErrorMessage:
+ _objc_msgSend$setReducedMemoryMode:
+ _objc_msgSend$setupDebugButtonWithTarget:action:
+ _objc_msgSend$systemClearColor
+ _objc_msgSend$systemImageNamed:withConfiguration:
+ _objc_msgSend$targetFrame
+ _symbolic SDy_____ypG s11AnyHashableV
+ _symbolic SaySDy_____ypGG s11AnyHashableV
+ _symbolic So15UIBarButtonItemC
+ _symbolic So16UIViewControllerCSgXw
+ _symbolic _____ 20AppleMediaServicesUI22DebugMenuBarButtonItemC
+ _symbolic _____ 20AppleMediaServicesUI9DebugMenuC
+ _symbolic _____XMT 20AppleMediaServicesUI9DebugMenuC
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC s11AnyHashableV
- -[AMSUIMessageViewLayoutContext _calculateFooterButtonFrames]
- GCC_except_table17
- GCC_except_table32
- GCC_except_table51
- GCC_except_table63
- GCC_except_table76
- GCC_except_table77
- GCC_except_table86
- GCC_except_table93
- GCC_except_table99
- ___39-[AMSUIWebSafariViewController _share:]_block_invoke.77
- ___39-[AMSUIWebSafariViewController _share:]_block_invoke_2.81
- ___51-[AMSUIBaseMessageViewController _setImageWithURL:]_block_invoke.48
- ___51-[AMSUIBaseMessageViewController _setImageWithURL:]_block_invoke.50
- ___54-[AMSUIMessageView _recordNewsDebugEventWithCategory:]_block_invoke
- ___56-[AMSUIBaseMessageViewController _loadIconAssetWithURL:]_block_invoke.41
- ___59-[AMSUIBaseMessageViewController _setMICAIconAssetWithURL:]_block_invoke.43
- ___59-[AMSUIBaseMessageViewController _setMICAIconAssetWithURL:]_block_invoke.45
- ___60-[AMSUIPaymentVerificationTokenFetchTask performWebFlowTask]_block_invoke.57
- ___61-[AMSUIMessageViewLayoutContext _calculateFooterButtonFrames]_block_invoke
- ___block_descriptor_48_e8_32s40w_e43_v24?0"AMSAuthenticateResult"8"NSError"16lw40l8s32l8
- ___block_literal_global.121
- _objc_msgSend$_calculateFooterButtonFrames
CStrings:
+ "\x13\x11"
+ "\x1f\x01\x14"
+ "%{public}@ Missing a required parameter, unable to process the authenticate request. request = %{public}@ presentingViewController = %{public}@"
+ "%{public}@: AMS can respond to action with deeplink %{public}@"
+ "%{public}@: Action invoked (identifier: %{public}@)"
+ "%{public}@: Enqueueing Engagement Impression MetricsEvent"
+ "%{public}@: Enqueueing metrics fields"
+ "%{public}@: [%{public}@] Reduce memory mode enabled, cleaning up snapshot"
+ "%{public}@: [%{public}@] cancelling camera session"
+ "%{public}@: [%{public}@] starting camera session"
+ "%{public}@: evaluating camera session teardown"
+ "%{public}@: setting up camera session"
+ "-apple-system-clear"
+ "@\"AMSUICommonButton\""
+ "@\"AMSUIWebSnapshotView\""
+ "AMSAuthenticateTaskCoordinatorItemKeyPresentingViewController"
+ "AMSAuthenticateTaskCoordinatorItemKeyRequest"
+ "AMSUIAuthenticateTaskCoordinator"
+ "AMSUIDebugMenu"
+ "AppleMediaServicesUI.DebugMenuBarButtonItem"
+ "AppleMediaServicesUI/DebugMenu.swift"
+ "AppleNews"
+ "Missing required parameter"
+ "PARENTAL_VERIFICATION_APPLE_PAY_CLASSIC_SHEET_ERROR_TITLE"
+ "PVK APC feature not enabled"
+ "Presenting debug menu failed with error: "
+ "T@\"AMSUICommonButton\",&,N,V_debugButton"
+ "T@\"AMSUIWebSnapshotView\",&,N,V_snapshotView"
+ "TB,N,V_prefersSessionTeardown"
+ "TB,N,V_reducedMemoryMode"
+ "The required authenticate request or view controller was missing."
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_debugButtonFrame"
+ "T{CGSize=dd},N,V_debugButtonSize"
+ "User closed payment sheet"
+ "_TtC20AppleMediaServicesUI22DebugMenuBarButtonItem"
+ "_authenticateTaskForItem:"
+ "_authenticateTaskForItem:authenticationResults:"
+ "_calculateFooterButtonSizes"
+ "_debugButton"
+ "_debugButtonFrame"
+ "_debugButtonSize"
+ "_debugInfoIsNotEmpty"
+ "_maxFooterButtonWidth"
+ "_maxTextContainerWidth"
+ "_prefersSessionTeardown"
+ "_presentDebugMenu"
+ "_reducedMemoryMode"
+ "_setupCameraReader"
+ "_setupDebugMenu"
+ "_walletHasValidSetup:paymentRequest:"
+ "accesssControlRef"
+ "amsui.onboarding"
+ "amsui.onboarding.primaryButton"
+ "amsui.onboarding.secondaryButton"
+ "ant.fill"
+ "configurationWithPointSize:"
+ "configurationWithPointSize:weight:"
+ "debugButton"
+ "debugButtonFrame"
+ "debugButtonSize"
+ "debugInfo"
+ "debugLogsEnabled"
+ "evaluationMechanismsForAccessControl:operation:error:"
+ "handleRequest:presentingViewController:"
+ "handleRequestDictionary:"
+ "https://amsui.apple.com/dynamic/marketing#route=debugMenu"
+ "lightGrayColor"
+ "prefersSessionTeardown"
+ "presentDebugMenu"
+ "presentDebugMenuWithPresentingVC:debugInfo:"
+ "presentingVC"
+ "pvk_apc_disabled"
+ "reducedMemoryMode"
+ "removeSnapshot"
+ "setDebugButton:"
+ "setDebugButtonFrame:"
+ "setDebugButtonSize:"
+ "setEndPoint:"
+ "setImage:forState:"
+ "setLocalizedErrorMessage:"
+ "setPrefersSessionTeardown:"
+ "setReducedMemoryMode:"
+ "setTarget:"
+ "setupDebugButtonWithTarget:action:"
+ "systemImageNamed:withConfiguration:"
+ "targetFrame"
+ "v32@0:8@16:24"
- "\x1b("
- "%{public}@: AMS can respond to action with identifier %{public}@"
- "%{public}@: Action invoked"
- "%{public}@: Enqueueing Engagement MetricsEvent"
- "News"
- "T@\"UIView\",&,N,V_snapshotView"
- "_calculateFooterButtonFrames"

```
