## VoiceShortcutsUICardKitProviderSupport

> `/System/Library/PrivateFrameworks/VoiceShortcutsUICardKitProviderSupport.framework/VoiceShortcutsUICardKitProviderSupport`

```diff

-3525.5.11.11.1
-  __TEXT.__text: 0x393c
-  __TEXT.__auth_stubs: 0x280
+3600.49.31.1.6
+  __TEXT.__text: 0x3344
   __TEXT.__objc_methlist: 0x5dc
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x109
+  __TEXT.__cstring: 0x114
   __TEXT.__oslogstring: 0x9e
   __TEXT.__ustring: 0x40
-  __TEXT.__unwind_info: 0x150
-  __TEXT.__objc_classname: 0x1cd
-  __TEXT.__objc_methname: 0x1355
-  __TEXT.__objc_methtype: 0x62c
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5a0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0xbc8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28587F75-566E-3540-B888-0C4423DBF6AB
+  UUID: E2B1852A-D695-3250-902B-DFBCC893CF20
   Functions: 80
-  Symbols:   497
-  CStrings:  314
+  Symbols:   500
+  CStrings:  14
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x25
Functions:
~ -[VSUIProgressCardViewController _setUpViews] : 1776 -> 1556
~ -[VSUIProgressCardViewController _setUpHelpers] : 220 -> 204
~ -[VSUIProgressCardViewController _updateDelegateOnBoundsDidChange] : 84 -> 80
~ -[VSUIProgressCardViewController _progressStateMachine] : 108 -> 96
~ -[VSUIProgressCardViewController _progressIndicatorViewController] : 132 -> 128
~ -[VSUIProgressCardViewController _hairlineView] : 192 -> 184
~ -[VSUIProgressCardViewController _statusView] : 144 -> 140
~ -[VSUIProgressCardViewController _loadingIndicatorView] : 148 -> 144
~ -[VSUIProgressCardViewController actionStatusView:didAddViewFromProgressViewController:] : 160 -> 152
~ -[VSUIProgressCardViewController progressStateMachine:didTransitionToState:fromState:forEvent:] : 268 -> 272
~ ___95-[VSUIProgressCardViewController progressStateMachine:didTransitionToState:fromState:forEvent:]_block_invoke : 388 -> 376
~ -[VSUIProgressCardViewController _initWithCard:delegate:loadProvidersImmediately:] : 204 -> 216
~ -[VSUIProgressCardViewController cardSectionViewWillAppearForCardSection:withAppearanceFeedback:] : 300 -> 284
~ -[VSUIProgressCardViewController cardSectionViewDidAppearForCardSection:withAppearanceFeedback:] : 268 -> 264
~ -[VSUIProgressCardViewController contentHeightForWidth:] : 248 -> 244
~ -[VSUIProgressCardViewController handleCardCommand:reply:] : 264 -> 276
~ -[VSUIProgressCardViewController shouldAnimateTransitionToState:fromState:forProgressIndicatorViewController:] : 16 -> 20
~ -[VSUIProgressCardViewController progress] : 64 -> 20
~ -[VSUIProgressCardViewController _setStatusView:] : 80 -> 20
~ -[VSUIProgressCardViewController _setLoadingIndicatorView:] : 80 -> 20
~ -[VSUIProgressCardViewController _setProgressIndicatorViewController:] : 80 -> 20
~ -[VSUIProgressCardViewController _setHairlineView:] : 80 -> 20
~ -[VSUIProgressCardViewController _setProgressStateMachine:] : 80 -> 20
~ -[VSUIVoiceShortcutCard _configureWithCard:] : 776 -> 724
~ -[VSUIVoiceShortcutCard cardIdentifier] : 64 -> 20
~ -[VSUIVoiceShortcutCard loadCardWithCompletion:] : 248 -> 240
~ -[VSUIVoiceShortcutCard loadCardWithContent:completion:] : 268 -> 276
~ ___56-[VSUIVoiceShortcutCard loadCardWithContent:completion:]_block_invoke : 224 -> 212
~ -[VSUIVoiceShortcutCard shortcutIdentifier] : 16 -> 20
~ -[VSUIVoiceShortcutCard intent] : 16 -> 20
~ -[VSUIVoiceShortcutCard intentResponse] : 16 -> 20
~ -[VSUIVoiceShortcutCard sectionCommands] : 16 -> 20
~ -[VSUIAsyncLoadingCard loadCardWithCompletion:] : 28 -> 32
~ -[VSUICKPEntryPoint displayPriorityForCard:] : 84 -> 76
~ -[VSUICKPEntryPoint cardViewControllerForCard:] : 528 -> 484
~ -[VSUIActionStatusView resetState] : 116 -> 108
~ -[VSUIActionStatusView sizeThatFits:] : 188 -> 180
~ -[VSUIActionStatusView progressStateMachine:didTransitionToState:fromState:forEvent:] : 336 -> 324
~ -[VSUIActionStatusView _setUpViews] : 1028 -> 928
~ -[VSUIActionStatusView _updateAcitivityViewSubviewWithDelegateProvidedView] : 624 -> 564
~ -[VSUIActionStatusView activityView] : 16 -> 20
~ -[VSUIActionStatusView setActivityView:] : 80 -> 20
~ -[VSUIActionStatusView errorView] : 16 -> 20
~ -[VSUIActionStatusView setErrorView:] : 80 -> 20
~ -[_VSUIActionStatusErrorView sizeThatFits:] : 112 -> 108
~ -[_VSUIActionStatusErrorView _setUpViews] : 2004 -> 1816
~ -[_VSUIActionStatusErrorView errorLabel] : 16 -> 20
~ -[_VSUIActionStatusErrorView setErrorLabel:] : 80 -> 20
~ -[_VSUIActionStatusErrorView errorIconView] : 16 -> 20
~ -[_VSUIActionStatusErrorView setErrorIconView:] : 80 -> 20
~ -[_VSUIActionStatusErrorView errorIconBackgroundView] : 16 -> 20
~ -[_VSUIActionStatusErrorView setErrorIconBackgroundView:] : 80 -> 20
~ -[VSUIVoiceShortcutCard loadCardWithCompletion:].cold.1 : 204 -> 152
~ -[VSUIActionStatusView progressStateMachine:ignoredEvent:].cold.1 : 192 -> 144
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<CRCard>\""
- "@\"<VSUIActionStatusViewDelegate>\""
- "@\"INIntent\""
- "@\"INIntentResponse\""
- "@\"NSArray\""
- "@\"NSLayoutConstraint\""
- "@\"NSProgress\""
- "@\"NSProgress\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"SUICProgressIndicatorViewController\""
- "@\"SUICProgressStateMachine\""
- "@\"SUICProgressStateMachine\"24@0:8@\"SUICProgressIndicatorViewController\"16"
- "@\"UIActivityIndicatorView\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIView\""
- "@\"UIViewController\"16@0:8"
- "@\"UIViewController<CRKCardViewControlling>\"24@0:8@\"<CRCard>\"16"
- "@\"VSUIActionStatusView\""
- "@\"_VSUIActionStatusErrorView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B40@0:8q16q24@\"SUICProgressIndicatorViewController\"32"
- "B40@0:8q16q24@32"
- "CRKCardViewControllerProviding"
- "CRKIdentifiedProviding"
- "CRKProviderIdentifying"
- "CRKProviding"
- "NSObject"
- "NSProgressReporting"
- "Q16@0:8"
- "Q24@0:8@\"<CRCard>\"16"
- "Q24@0:8@16"
- "SUICProgressIndicatorViewControllerDataSource"
- "SUICProgressStateMachineObserving"
- "T#,R"
- "T@\"<VSUIActionStatusViewDelegate>\",W,N,V_delegate"
- "T@\"INIntent\",R,N,V_intent"
- "T@\"INIntentResponse\",R,N,V_intentResponse"
- "T@\"NSArray\",R,N,V_sectionCommands"
- "T@\"NSProgress\",R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N,V_shortcutIdentifier"
- "T@\"SUICProgressIndicatorViewController\",&,N,G_progressIndicatorViewController,S_setProgressIndicatorViewController:,V_progressIndicatorViewController"
- "T@\"SUICProgressStateMachine\",&,N,G_progressStateMachine,S_setProgressStateMachine:,V_progressStateMachine"
- "T@\"UIActivityIndicatorView\",&,N,G_loadingIndicatorView,S_setLoadingIndicatorView:,V_loadingIndicatorView"
- "T@\"UIImageView\",&,N,V_errorIconView"
- "T@\"UILabel\",&,N,V_errorLabel"
- "T@\"UIView\",&,N,G_hairlineView,S_setHairlineView:,V_hairlineView"
- "T@\"UIView\",&,N,V_activityView"
- "T@\"UIView\",&,N,V_errorIconBackgroundView"
- "T@\"VSUIActionStatusView\",&,N,G_statusView,S_setStatusView:,V_statusView"
- "T@\"_VSUIActionStatusErrorView\",&,N,V_errorView"
- "TQ,R"
- "VSUIActionStatusView"
- "VSUIActionStatusViewDelegate"
- "VSUIActionStatusViewProgressViewControllerProviding"
- "VSUIAsyncLoadingCard"
- "VSUICKPEntryPoint"
- "VSUIPerformActionCardProvider"
- "VSUIProgressCardViewController"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_VSUIActionStatusErrorView"
- "_activityView"
- "_animatesStateTransitions"
- "_canShowWhileLocked"
- "_configureWithCard:"
- "_delegate"
- "_errorIconBackgroundView"
- "_errorIconView"
- "_errorLabel"
- "_errorView"
- "_flatImageWithColor:"
- "_hairlineView"
- "_hasAsynchronousCard"
- "_initWithCard:delegate:loadProvidersImmediately:"
- "_intent"
- "_intentCategory"
- "_intentResponse"
- "_loadingIndicatorView"
- "_metadata"
- "_progress"
- "_progressIndicatorViewController"
- "_progressStateMachine"
- "_sectionCommands"
- "_setHairlineView:"
- "_setLoadingIndicatorView:"
- "_setMetadata:"
- "_setProgressIndicatorViewController:"
- "_setProgressStateMachine:"
- "_setStatusView:"
- "_setUpHelpers"
- "_setUpViews"
- "_shortcutIdentifier"
- "_statusView"
- "_statusViewFailureHeightConstraint"
- "_statusViewSuccessHeightConstraint"
- "_storedCard"
- "_updateAcitivityViewSubviewWithDelegateProvidedView"
- "_updateDelegateOnBoundsDidChange"
- "actionStatusView:didAddViewFromProgressViewController:"
- "activateConstraints:"
- "activityView"
- "addChildViewController:"
- "addObservers:"
- "addSubview:"
- "animateWithDuration:animations:"
- "animatesProgress"
- "anyObject"
- "arrayWithObjects:count:"
- "asynchronous"
- "autorelease"
- "blackColor"
- "bottomAnchor"
- "bounds"
- "bundleForClass:"
- "card"
- "cardIdentifier"
- "cardSectionView"
- "cardSectionViewDidAppearForCardSection:withAppearanceFeedback:"
- "cardSectionViewSource"
- "cardSectionViewWillAppearForCardSection:withAppearanceFeedback:"
- "cardSections"
- "cardViewControllerBoundsDidChange:"
- "cardViewControllerDelegate"
- "cardViewControllerForCard:"
- "centerXAnchor"
- "centerYAnchor"
- "class"
- "colorWithAlphaComponent:"
- "commands"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "constraintGreaterThanOrEqualToAnchor:"
- "constraintLessThanOrEqualToAnchor:"
- "constraintLessThanOrEqualToConstant:"
- "contentHeightForWidth:"
- "d24@0:8d16"
- "debugDescription"
- "delegate"
- "description"
- "didMoveToParentViewController:"
- "displayPriorityForCard:"
- "errorIconBackgroundView"
- "errorIconView"
- "errorLabel"
- "errorView"
- "event"
- "executionContext"
- "firstObject"
- "hairlineView"
- "handleCardCommand:reply:"
- "handleEvent:"
- "hasExecutionContext"
- "hash"
- "heightAnchor"
- "imageNamed:inBundle:"
- "init"
- "initWithActivityIndicatorStyle:"
- "initWithCard:"
- "initWithCardViewConfig:"
- "initWithCoder:"
- "initWithFrame:"
- "initWithImage:"
- "initWithIntent:response:"
- "intent"
- "intentResponse"
- "interactions"
- "isActive"
- "isEqual:"
- "isHidden"
- "isKindOfClass:"
- "isLoading"
- "isMemberOfClass:"
- "isProxy"
- "layer"
- "leadingAnchor"
- "leftAnchor"
- "loadCardWithCompletion:"
- "loadCardWithContent:completion:"
- "loadingIndicatorView"
- "localizedStringForKey:value:table:"
- "messageData"
- "numberWithInteger:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferredContentSize"
- "preferredFontForTextStyle:"
- "presentation:didApplyCardSectionViewSource:toCardViewController:"
- "progress"
- "progressIndicatorViewController"
- "progressStateMachine"
- "progressStateMachine:didTransitionToState:fromState:forEvent:"
- "progressStateMachine:ignoredEvent:"
- "progressViewController"
- "providerIdentifier"
- "release"
- "removeFromSuperview"
- "requestCardSectionViewProviderForCard:delegate:reply:"
- "requestIdentifiedCardSectionViewProviderForCard:delegate:reply:"
- "resetState"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rightAnchor"
- "secondaryLabelColor"
- "sectionCommands"
- "self"
- "setActive:"
- "setActivityView:"
- "setAlpha:"
- "setBackgroundColor:"
- "setCommands:"
- "setContent:"
- "setContentMode:"
- "setCornerRadius:"
- "setDataSource:"
- "setDelegate:"
- "setErrorIconBackgroundView:"
- "setErrorIconView:"
- "setErrorLabel:"
- "setErrorView:"
- "setExecutionContext:"
- "setFont:"
- "setFormat:"
- "setFrame:"
- "setHidden:"
- "setHidesWhenStopped:"
- "setLineBreakMode:"
- "setMasksToBounds:"
- "setNumberOfLines:"
- "setShowThumbnailImage:"
- "setStyle:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "shortcutIdentifier"
- "shouldAnimateTransitionToState:fromState:forProgressIndicatorViewController:"
- "sizeThatFits:"
- "startAnimating"
- "startWithReply:"
- "stateMachineForProgressIndicatorViewController:"
- "statusView"
- "stopAnimating"
- "superclass"
- "systemGray3Color"
- "systemGray5Color"
- "systemGrayColor"
- "topAnchor"
- "trailingAnchor"
- "typeName"
- "underlyingIntent"
- "underlyingIntentResponse"
- "unregisterCardViewController:"
- "v16@0:8"
- "v24@0:8@\"UIViewController<CRKCardViewControlling>\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"SUICProgressStateMachine\"16q24"
- "v32@0:8@\"VSUIActionStatusView\"16@\"UIViewController\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v40@0:8@\"<CRCard>\"16@\"<CRKCardSectionViewProviderDelegate>\"24@?<v@?@\"NSError\"@\"<CRKCardSectionViewProviding>\">32"
- "v40@0:8@\"<CRCard>\"16@\"<CRKCardSectionViewProviderDelegate>\"24@?<v@?@\"NSError\"@\"<CRKIdentifiedCardSectionViewProviding>\">32"
- "v40@0:8@\"<CRKCardPresenting>\"16@\"<CRKCardSectionViewSourcing>\"24@\"UIViewController<CRKCardViewControlling>\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"SUICProgressStateMachine\"16q24q32q40"
- "v48@0:8@16q24q32q40"
- "view"
- "viewConfigurationForCardSection:"
- "vocabularyIdentifier"
- "voiceCommand"
- "widthAnchor"
- "zone"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}32@0:8{CGSize=dd}16"

```
