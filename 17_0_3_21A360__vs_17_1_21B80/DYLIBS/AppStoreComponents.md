## AppStoreComponents

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents`

```diff

-6.0.44.0.0
-  __TEXT.__text: 0x7f794
+6.1.6.0.0
+  __TEXT.__text: 0x82a38
   __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_methlist: 0x5e44
-  __TEXT.__const: 0x1284
+  __TEXT.__objc_methlist: 0x60e0
+  __TEXT.__const: 0x12a4
   __TEXT.__gcc_except_tab: 0x608
-  __TEXT.__cstring: 0x2ff2
+  __TEXT.__cstring: 0x3172
   __TEXT.__dlopen_cstrs: 0x14f
-  __TEXT.__oslogstring: 0x26cb
-  __TEXT.__constg_swiftt: 0x658
-  __TEXT.__swift5_typeref: 0x3fe
+  __TEXT.__oslogstring: 0x27c7
+  __TEXT.__constg_swiftt: 0x684
+  __TEXT.__swift5_typeref: 0x404
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0xc10
-  __TEXT.__swift5_fieldmd: 0xb04
+  __TEXT.__swift5_reflstr: 0xc40
+  __TEXT.__swift5_fieldmd: 0xb38
   __TEXT.__swift5_assocty: 0x1b0
   __TEXT.__swift5_capture: 0x190
   __TEXT.__swift5_proto: 0xf4
-  __TEXT.__swift5_types: 0x9c
+  __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2060
-  __TEXT.__objc_classname: 0xc56
-  __TEXT.__objc_methname: 0xd491
-  __TEXT.__objc_methtype: 0x20c5
-  __TEXT.__objc_stubs: 0xa260
+  __TEXT.__unwind_info: 0x20e4
+  __TEXT.__objc_classname: 0xc8d
+  __TEXT.__objc_methname: 0xdcda
+  __TEXT.__objc_methtype: 0x2174
+  __TEXT.__objc_stubs: 0xa560
   __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x1408
-  __DATA_CONST.__objc_classlist: 0x378
+  __DATA_CONST.__const: 0x1438
+  __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8970
-  __DATA_CONST.__objc_selrefs: 0x2ed0
+  __DATA_CONST.__objc_const: 0x8ee0
+  __DATA_CONST.__objc_selrefs: 0x2fc0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x3920
+  __AUTH_CONST.__objc_const: 0x120
+  __AUTH_CONST.__cfstring: 0x3aa0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__const: 0x980
   __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH.__objc_data: 0x0
-  __AUTH.__data: 0x98
+  __AUTH.__objc_data: 0x150
+  __AUTH.__data: 0xc0
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x5a8
-  __DATA.__objc_superrefs: 0x330
-  __DATA.__objc_ivar: 0x5e8
-  __DATA.__data: 0x1990
+  __DATA.__objc_classrefs: 0x5b8
+  __DATA.__objc_superrefs: 0x340
+  __DATA.__objc_ivar: 0x644
+  __DATA.__data: 0x19b0
   __DATA.__bss: 0x19d0
   __DATA.__common: 0x150
   __DATA_DIRTY.__const: 0x1698
   __DATA_DIRTY.__objc_const: 0x34a0
   __DATA_DIRTY.__objc_data: 0x2190
-  __DATA_DIRTY.__data: 0x880
+  __DATA_DIRTY.__data: 0x888
   __DATA_DIRTY.__bss: 0x778
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 51E86E2D-2026-35BC-9B36-1DD253BF12D3
-  Functions: 3073
-  Symbols:   8360
-  CStrings:  3932
+  UUID: 4052A2E3-B2F4-3FC6-958F-7082F1DB2F4C
+  Functions: 3139
+  Symbols:   8540
+  CStrings:  4030
 
Symbols:
+ +[ASCEligibility isITunesStoreClient:]
+ +[ASCOfferAlertOffer supportsSecureCoding]
+ -[ASCCustomLockupContentProvider .cxx_destruct]
+ -[ASCCustomLockupContentProvider badgeView]
+ -[ASCCustomLockupContentProvider initWithLockupView:]
+ -[ASCCustomLockupContentProvider lockupView]
+ -[ASCLockupContentView badgeView]
+ -[ASCLockupContentView setBadge:]
+ -[ASCLockupContentView setBadgeView:]
+ -[ASCLockupContentView shouldHideBadge]
+ -[ASCLockupPresenter customContentProvider]
+ -[ASCLockupPresenter initWithView:customContentProvider:offerPresenter:metricsPresenter:]
+ -[ASCLockupPresenter initWithView:customContentProvider:offerPresenter:metricsPresenter:context:]
+ -[ASCLockupView presentingSceneBundleIdentifier]
+ -[ASCLockupView presentingSceneIdentifier]
+ -[ASCLockupView setPresentingSceneBundleIdentifier:]
+ -[ASCLockupView setPresentingSceneIdentifier:]
+ -[ASCOfferAlertOffer .cxx_destruct]
+ -[ASCOfferAlertOffer ageRating]
+ -[ASCOfferAlertOffer alertFooterMessage]
+ -[ASCOfferAlertOffer alertMessage]
+ -[ASCOfferAlertOffer alertTitle]
+ -[ASCOfferAlertOffer checkRestrictionsForContentRating]
+ -[ASCOfferAlertOffer completionOffer]
+ -[ASCOfferAlertOffer copyWithZone:]
+ -[ASCOfferAlertOffer description]
+ -[ASCOfferAlertOffer encodeWithCoder:]
+ -[ASCOfferAlertOffer flags]
+ -[ASCOfferAlertOffer hash]
+ -[ASCOfferAlertOffer id]
+ -[ASCOfferAlertOffer initWithCoder:]
+ -[ASCOfferAlertOffer initWithCoder:].cold.1
+ -[ASCOfferAlertOffer initWithCoder:].cold.2
+ -[ASCOfferAlertOffer initWithCoder:].cold.3
+ -[ASCOfferAlertOffer initWithCoder:].cold.4
+ -[ASCOfferAlertOffer initWithID:titles:subtitles:flags:ageRating:metrics:alertTitle:alertMessage:alertFooterMessage:isCancelable:checkRestrictionsForContentRating:shouldCheckForAvailableDiskSpace:remoteControllerRequirement:shouldIncludeActiveAccountInFooterMessage:shouldPromptForConfirmation:completionOffer:]
+ -[ASCOfferAlertOffer isCancelable]
+ -[ASCOfferAlertOffer isEqual:]
+ -[ASCOfferAlertOffer metrics]
+ -[ASCOfferAlertOffer offerWithMetrics:]
+ -[ASCOfferAlertOffer remoteControllerRequirement]
+ -[ASCOfferAlertOffer shouldCheckForAvailableDiskSpace]
+ -[ASCOfferAlertOffer shouldIncludeActiveAccountInFooterMessage]
+ -[ASCOfferAlertOffer shouldPromptForConfirmation]
+ -[ASCOfferAlertOffer subtitles]
+ -[ASCOfferAlertOffer titles]
+ -[ASCOfferButton updateVisualEffects]
+ -[ASCOfferContext .cxx_destruct]
+ -[ASCOfferContext initWithFlags:presentingSceneIdentifier:presentingSceneBundleIdentifier:]
+ -[ASCOfferContext offerContextByAddingFlags:]
+ -[ASCOfferContext offerContextWithPresentingSceneIdentifier:presentingSceneBundleIdentifier:]
+ -[ASCOfferContext presentingSceneBundleIdentifier]
+ -[ASCOfferContext presentingSceneIdentifier]
+ GCC_except_table20
+ GCC_except_table26
+ GCC_except_table57
+ _ASCLocalizedStringFromBundle
+ _ASCLockupContextTVAppOpenIn
+ _OBJC_CLASS_$_ASCCustomLockupContentProvider
+ _OBJC_CLASS_$_ASCOfferAlertOffer
+ _OBJC_CLASS_$__TtC18AppStoreComponents3PPM
+ _OBJC_IVAR_$_ASCCustomLockupContentProvider._lockupView
+ _OBJC_IVAR_$_ASCLockupContentView._badgeView
+ _OBJC_IVAR_$_ASCLockupPresenter._customContentProvider
+ _OBJC_IVAR_$_ASCLockupView._presentingSceneBundleIdentifier
+ _OBJC_IVAR_$_ASCLockupView._presentingSceneIdentifier
+ _OBJC_IVAR_$_ASCOfferAlertOffer._ageRating
+ _OBJC_IVAR_$_ASCOfferAlertOffer._alertFooterMessage
+ _OBJC_IVAR_$_ASCOfferAlertOffer._alertMessage
+ _OBJC_IVAR_$_ASCOfferAlertOffer._alertTitle
+ _OBJC_IVAR_$_ASCOfferAlertOffer._checkRestrictionsForContentRating
+ _OBJC_IVAR_$_ASCOfferAlertOffer._completionOffer
+ _OBJC_IVAR_$_ASCOfferAlertOffer._flags
+ _OBJC_IVAR_$_ASCOfferAlertOffer._id
+ _OBJC_IVAR_$_ASCOfferAlertOffer._isCancelable
+ _OBJC_IVAR_$_ASCOfferAlertOffer._metrics
+ _OBJC_IVAR_$_ASCOfferAlertOffer._remoteControllerRequirement
+ _OBJC_IVAR_$_ASCOfferAlertOffer._shouldCheckForAvailableDiskSpace
+ _OBJC_IVAR_$_ASCOfferAlertOffer._shouldIncludeActiveAccountInFooterMessage
+ _OBJC_IVAR_$_ASCOfferAlertOffer._shouldPromptForConfirmation
+ _OBJC_IVAR_$_ASCOfferAlertOffer._subtitles
+ _OBJC_IVAR_$_ASCOfferAlertOffer._titles
+ _OBJC_IVAR_$_ASCOfferContext._presentingSceneBundleIdentifier
+ _OBJC_IVAR_$_ASCOfferContext._presentingSceneIdentifier
+ _OBJC_METACLASS_$_ASCCustomLockupContentProvider
+ _OBJC_METACLASS_$_ASCOfferAlertOffer
+ _OBJC_METACLASS_$__TtC18AppStoreComponents3PPM
+ __DATA__TtC18AppStoreComponents3PPM
+ __METACLASS_DATA__TtC18AppStoreComponents3PPM
+ __OBJC_$_CLASS_METHODS_ASCOfferAlertOffer
+ __OBJC_$_CLASS_METHODS__TtC18AppStoreComponents3PPM
+ __OBJC_$_CLASS_PROP_LIST_ASCOfferAlertOffer
+ __OBJC_$_INSTANCE_METHODS_ASCCustomLockupContentProvider
+ __OBJC_$_INSTANCE_METHODS_ASCOfferAlertOffer
+ __OBJC_$_INSTANCE_METHODS__TtC18AppStoreComponents3PPM
+ __OBJC_$_INSTANCE_VARIABLES_ASCCustomLockupContentProvider
+ __OBJC_$_INSTANCE_VARIABLES_ASCOfferAlertOffer
+ __OBJC_$_PROP_LIST_ASCCustomLockupContentProvider
+ __OBJC_$_PROP_LIST_ASCOfferAlertOffer
+ __OBJC_CLASS_PROTOCOLS_$_ASCOfferAlertOffer
+ __OBJC_CLASS_RO_$_ASCCustomLockupContentProvider
+ __OBJC_CLASS_RO_$_ASCOfferAlertOffer
+ __OBJC_METACLASS_RO_$_ASCCustomLockupContentProvider
+ __OBJC_METACLASS_RO_$_ASCOfferAlertOffer
+ ___73-[ASCLockupProductDetails presentFromViewController:animated:completion:]_block_invoke_2
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ _objc_msgSend$_sceneIdentifier
+ _objc_msgSend$alertFooterMessage
+ _objc_msgSend$badgeView
+ _objc_msgSend$checkRestrictionsForContentRating
+ _objc_msgSend$completionOffer
+ _objc_msgSend$customContentProvider
+ _objc_msgSend$initWithFlags:presentingSceneIdentifier:presentingSceneBundleIdentifier:
+ _objc_msgSend$initWithID:titles:subtitles:flags:ageRating:metrics:alertTitle:alertMessage:alertFooterMessage:isCancelable:checkRestrictionsForContentRating:shouldCheckForAvailableDiskSpace:remoteControllerRequirement:shouldIncludeActiveAccountInFooterMessage:shouldPromptForConfirmation:completionOffer:
+ _objc_msgSend$initWithLockupView:
+ _objc_msgSend$initWithView:customContentProvider:offerPresenter:metricsPresenter:
+ _objc_msgSend$initWithView:customContentProvider:offerPresenter:metricsPresenter:context:
+ _objc_msgSend$isCancelable
+ _objc_msgSend$isITunesStoreClient:
+ _objc_msgSend$lockupLayoutOfSize:traitCollection:artworkView:headingText:titleText:subtitleText:offerText:offerButton:badge:
+ _objc_msgSend$offerContextByAddingFlags:
+ _objc_msgSend$offerContextWithPresentingSceneIdentifier:presentingSceneBundleIdentifier:
+ _objc_msgSend$presentingSceneBundleIdentifier
+ _objc_msgSend$presentingSceneIdentifier
+ _objc_msgSend$remoteControllerRequirement
+ _objc_msgSend$setBadge:
+ _objc_msgSend$setBadgeView:
+ _objc_msgSend$shouldCheckForAvailableDiskSpace
+ _objc_msgSend$shouldHideBadge
+ _objc_msgSend$shouldIncludeActiveAccountInFooterMessage
+ _objc_msgSend$shouldPromptForConfirmation
+ _objc_msgSend$updateVisualEffects
+ _objc_msgSend$windowScene
+ _symbolic _____ 18AppStoreComponents3PPMC
- -[ASCLockupPresenter initWithView:offerPresenter:metricsPresenter:context:]
- -[ASCOfferButton updateFocusState]
- GCC_except_table16
- GCC_except_table25
- GCC_except_table54
- _objc_msgSend$initWithView:offerPresenter:metricsPresenter:context:
- _objc_msgSend$lockupLayoutOfSize:traitCollection:artworkView:headingText:titleText:subtitleText:offerText:offerButton:
- _objc_msgSend$updateFocusState
CStrings:
+ "\v"
+ "\x13\x18"
+ "$\x16"
+ "("
+ "@\"ASCCustomLockupContentProvider\""
+ "@\"ASCLockupView\""
+ "@128@0:8@16@24@32q40@48@56@64@72@80B88@92B100@104B112B116@120"
+ "@40@0:8q16@24@32"
+ "ASCCustomLockupContentProvider"
+ "ASCOfferAlertOffer"
+ "Could not decode ASCOfferAlertOffer because id was missing"
+ "Could not decode ASCOfferAlertOffer because metrics was missing"
+ "Could not decode ASCOfferAlertOffer because subtitles was missing"
+ "Could not decode ASCOfferAlertOffer because titles was missing"
+ "T@\"<ASCOffer>\",R,C,N,V_completionOffer"
+ "T@\"ASCCustomLockupContentProvider\",R,N,V_customContentProvider"
+ "T@\"ASCLockupView\",R,W,N,V_lockupView"
+ "T@\"NSNumber\",R,C,N,V_checkRestrictionsForContentRating"
+ "T@\"NSString\",&,N,V_presentingSceneBundleIdentifier"
+ "T@\"NSString\",&,N,V_presentingSceneIdentifier"
+ "T@\"NSString\",R,C,N,V_alertFooterMessage"
+ "T@\"NSString\",R,C,N,V_presentingSceneBundleIdentifier"
+ "T@\"NSString\",R,C,N,V_presentingSceneIdentifier"
+ "T@\"NSString\",R,C,N,V_remoteControllerRequirement"
+ "T@\"UIView\",&,N,V_badgeView"
+ "TB,R,N,V_isCancelable"
+ "TB,R,N,V_shouldCheckForAvailableDiskSpace"
+ "TB,R,N,V_shouldIncludeActiveAccountInFooterMessage"
+ "TB,R,N,V_shouldPromptForConfirmation"
+ "_TtC18AppStoreComponents3PPM"
+ "_alertFooterMessage"
+ "_badgeView"
+ "_checkRestrictionsForContentRating"
+ "_completionOffer"
+ "_customContentProvider"
+ "_isCancelable"
+ "_lockupView"
+ "_presentingSceneBundleIdentifier"
+ "_presentingSceneIdentifier"
+ "_remoteControllerRequirement"
+ "_sceneIdentifier"
+ "_shouldCheckForAvailableDiskSpace"
+ "_shouldIncludeActiveAccountInFooterMessage"
+ "_shouldPromptForConfirmation"
+ "alertFooterMessage"
+ "badgeView"
+ "badgeViewForLockupView:"
+ "checkRestrictionsForContentRating"
+ "com.apple.MobileStore"
+ "completionOffer"
+ "customContentProvider"
+ "d24@0:8d16"
+ "d32@0:8d16d24"
+ "initWithFlags:presentingSceneIdentifier:presentingSceneBundleIdentifier:"
+ "initWithID:titles:subtitles:flags:ageRating:metrics:alertTitle:alertMessage:alertFooterMessage:isCancelable:checkRestrictionsForContentRating:shouldCheckForAvailableDiskSpace:remoteControllerRequirement:shouldIncludeActiveAccountInFooterMessage:shouldPromptForConfirmation:completionOffer:"
+ "initWithLockupView:"
+ "initWithView:customContentProvider:offerPresenter:metricsPresenter:"
+ "initWithView:customContentProvider:offerPresenter:metricsPresenter:context:"
+ "isCancelable"
+ "isITunesStoreClient:"
+ "lockupLayoutOfSize:traitCollection:artworkView:headingText:titleText:subtitleText:offerText:offerButton:badge:"
+ "lockupView"
+ "offerContextByAddingFlags:"
+ "offerContextWithPresentingSceneIdentifier:presentingSceneBundleIdentifier:"
+ "presentingSceneBundleIdentifier"
+ "presentingSceneIdentifier"
+ "remoteControllerRequirement"
+ "scaledValueWithOriginal:updated:"
+ "setBadge:"
+ "setBadgeView:"
+ "setPresentingSceneBundleIdentifier:"
+ "setPresentingSceneIdentifier:"
+ "shouldCheckForAvailableDiskSpace"
+ "shouldHideBadge"
+ "shouldIncludeActiveAccountInFooterMessage"
+ "shouldPromptForConfirmation"
+ "tvAppOpenIn"
+ "unverifiedScaledValue:"
+ "updateVisualEffects"
+ "v24@0:8@\"UIView\"16"
+ "windowScene"
+ "{?=\"lockupViewDidBeginRequest\"b1\"lockupViewDidFinishRequest\"b1\"lockupViewDidFailRequestWithError\"b1\"lockupViewAppStateDidChange\"b1\"metricsActivityForAdLockupViewToPerformActionOfOfferInState\"b1\"lockupViewDidInvalidateIntrinsicContentSize\"b1\"lockupViewShouldSupportDSIDLessInstalls\"b1\"productDetailsPresentationContextForLockupView\"b1\"lockupViewPreprocessOfferInStateCompletionBlock\"b1\"badgeViewForLockupView\"b1}"
- "$\x15"
- "&"
- "initWithView:offerPresenter:metricsPresenter:context:"
- "lockupLayoutOfSize:traitCollection:artworkView:headingText:titleText:subtitleText:offerText:offerButton:"
- "updateFocusState"
- "{?=\"lockupViewDidBeginRequest\"b1\"lockupViewDidFinishRequest\"b1\"lockupViewDidFailRequestWithError\"b1\"lockupViewAppStateDidChange\"b1\"metricsActivityForAdLockupViewToPerformActionOfOfferInState\"b1\"lockupViewDidInvalidateIntrinsicContentSize\"b1\"lockupViewShouldSupportDSIDLessInstalls\"b1\"productDetailsPresentationContextForLockupView\"b1\"lockupViewPreprocessOfferInStateCompletionBlock\"b1}"

```
