## AMPCoreUI

> `/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI`

```diff

-1452.4.2.0.0
-  __TEXT.__text: 0x93d8
-  __TEXT.__auth_stubs: 0x420
+1453.0.4.0.0
+  __TEXT.__text: 0x87b8
   __TEXT.__objc_methlist: 0xaf4
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__cstring: 0x240
+  __TEXT.__gcc_except_tab: 0x234
+  __TEXT.__cstring: 0x256
   __TEXT.__dlopen_cstrs: 0x206
   __TEXT.__oslogstring: 0x3a8
-  __TEXT.__unwind_info: 0x360
-  __TEXT.__objc_classname: 0x22b
-  __TEXT.__objc_methname: 0x2634
-  __TEXT.__objc_methtype: 0x85e
-  __TEXT.__objc_stubs: 0x1c20
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa50
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x1460
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0xa8

   - /System/Library/PrivateFrameworks/StoreServices.framework/StoreServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7284E74-B2DF-309B-87FA-7AE5A201FE3B
+  UUID: 12FE8685-2226-3335-8616-F8FDB9C03C5A
   Functions: 214
-  Symbols:   1004
-  CStrings:  577
+  Symbols:   1011
+  CStrings:  57
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[AMPTintedBackgroundButton updateBackgroundColor] : 156 -> 148
~ -[AMPOnboardingFeature initWithImage:titleText:descriptionText:] : 180 -> 196
~ -[AMPOnboardingViewController initWithHeaderImage:titleText:descriptionText:primaryButtonText:privacyLinkController:] : 468 -> 484
~ _getAMSUIOnboardingViewControllerClass : 220 -> 224
~ ___117-[AMPOnboardingViewController initWithHeaderImage:titleText:descriptionText:primaryButtonText:privacyLinkController:]_block_invoke : 132 -> 124
~ -[AMPOnboardingViewController initWithTitleText:features:primaryButtonText:privacyLinkController:] : 1012 -> 984
~ ___98-[AMPOnboardingViewController initWithTitleText:features:primaryButtonText:privacyLinkController:]_block_invoke : 132 -> 124
~ -[AMPOnboardingViewController viewDidLoad] : 312 -> 280
~ -[AMPOnboardingViewController viewWillAppear:] : 148 -> 140
~ -[AMPOnboardingViewController viewDidLayoutSubviews] : 200 -> 188
~ -[AMPOnboardingViewController traitCollectionDidChange:] : 104 -> 100
~ -[AMPOnboardingViewController supportedInterfaceOrientations] : 72 -> 68
~ -[AMPOnboardingViewController cappedTraitCollection] : 420 -> 388
~ ___52-[AMPOnboardingViewController cappedTraitCollection]_block_invoke : 160 -> 156
~ -[AMPOnboardingViewController childTraitCollectionForViewController:] : 296 -> 288
~ -[AMPOnboardingViewController updateOverrideTraits] : 292 -> 288
~ -[AMPOnboardingViewController didTapPrimaryButton:] : 136 -> 128
~ -[AMPOnboardingViewController isPresentedInFormSheet] : 140 -> 132
~ -[AMPOnboardingViewController setTitleText:] : 80 -> 20
~ -[AMPOnboardingViewController setDescriptionText:] : 80 -> 20
~ -[AMPOnboardingViewController setPrimaryButtonText:] : 80 -> 20
~ -[AMPOnboardingViewController privacyLinkController] : 16 -> 20
~ -[AMPOnboardingViewController primaryButtonCallback] : 16 -> 20
~ -[AMPOnboardingViewController onboardingController] : 16 -> 20
~ -[AMPOnboardingViewController setOnboardingController:] : 80 -> 20
~ -[AMPOnboardingViewController image] : 16 -> 20
~ -[AMPOnboardingViewController setImage:] : 80 -> 20
~ -[AMPOnboardingViewController statusBarVisualEffectView] : 16 -> 20
~ -[AMPOnboardingViewController setStatusBarVisualEffectView:] : 80 -> 20
~ -[AMPOnboardingViewController backdropView] : 16 -> 20
~ -[AMPOnboardingViewController setBackdropView:] : 80 -> 20
~ -[AMPOnboardingViewController metricsQueue] : 16 -> 20
~ -[AMPOnboardingViewController setMetricsQueue:] : 80 -> 20
~ -[AMPOnboardingViewController viewHasAppeared] : 16 -> 20
~ -[AMPOnboardingViewController setViewHasAppeared:] : 16 -> 20
~ -[AMPUserNotificationContentViewController initWithNotification:delegate:] : 2052 -> 1916
~ ___74-[AMPUserNotificationContentViewController initWithNotification:delegate:]_block_invoke : 312 -> 300
~ ___74-[AMPUserNotificationContentViewController initWithNotification:delegate:]_block_invoke_2 : 452 -> 400
~ -[AMPUserNotificationContentViewController loadView] : 720 -> 636
~ -[AMPUserNotificationContentViewController setPreferredContentSize:] : 124 -> 120
~ -[AMPUserNotificationContentViewController expectedContentSize] : 504 -> 460
~ -[AMPUserNotificationContentViewController viewWillAppear:] : 192 -> 180
~ -[AMPUserNotificationContentViewController viewWillLayoutSubviews] : 1040 -> 940
~ -[AMPUserNotificationContentViewController imageViewTapped:] : 68 -> 64
~ -[AMPUserNotificationContentViewController mediaPause] : 184 -> 168
~ _getAVAudioSessionClass : 220 -> 224
~ -[AMPUserNotificationContentViewController observeValueForKeyPath:ofObject:change:context:] : 1508 -> 1344
~ -[AMPUserNotificationContentViewController userNotification] : 16 -> 20
~ -[AMPUserNotificationContentViewController audioSessionCategory] : 16 -> 20
~ -[AMPUserNotificationContentViewController setAudioSessionCategory:] : 80 -> 20
~ -[AMPUserNotificationContentViewController audioSessionCategoryOptions] : 16 -> 20
~ -[AMPUserNotificationContentViewController setAudioSessionCategoryOptions:] : 16 -> 20
~ -[AMPUserNotificationContentViewController hasAppeared] : 16 -> 20
~ -[AMPUserNotificationContentViewController setHasAppeared:] : 16 -> 20
~ -[AMPUserNotificationContentViewController hasPlayedVideo] : 16 -> 20
~ -[AMPUserNotificationContentViewController setHasPlayedVideo:] : 16 -> 20
~ -[AMPUserNotificationContentViewController imageView] : 16 -> 20
~ -[AMPUserNotificationContentViewController metrics] : 16 -> 20
~ -[AMPUserNotificationContentViewController setMetrics:] : 80 -> 20
~ -[AMPUserNotificationContentViewController textLabel] : 16 -> 20
~ -[AMPUserNotificationContentViewController titleLabel] : 16 -> 20
~ -[AMPUserNotificationContentViewController videoPlayerController] : 16 -> 20
~ -[AMPOnboardingHeaderView initWithFrame:] : 320 -> 332
~ -[AMPOnboardingHeaderView layoutSubviews] : 956 -> 896
~ -[AMPOnboardingHeaderView traitCollectionDidChange:] : 392 -> 364
~ -[AMPOnboardingHeaderView updateContentSize] : 656 -> 616
~ -[AMPOnboardingHeaderView setContainerHeight:] : 96 -> 100
~ -[AMPOnboardingHeaderView setIsPresentedInFormSheet:] : 84 -> 88
~ -[AMPOnboardingHeaderView imageView] : 16 -> 20
~ -[AMPOnboardingHeaderView setImageView:] : 80 -> 20
~ -[AMPOnboardingHeaderView titleLabel] : 16 -> 20
~ -[AMPOnboardingHeaderView setTitleLabel:] : 80 -> 20
~ -[AMPOnboardingHeaderView descriptionLabel] : 16 -> 20
~ -[AMPOnboardingHeaderView setDescriptionLabel:] : 80 -> 20
~ -[AMPOnboardingHeaderView containerHeight] : 16 -> 20
~ -[AMPOnboardingHeaderView isPresentedInFormSheet] : 16 -> 20
~ -[AMPButton initWithFrame:] : 200 -> 188
~ -[AMPButton tintColorDidChange] : 104 -> 100
~ -[AMPOnboardingFeatureView layoutSubviews] : 556 -> 532
~ -[AMPOnboardingFeatureView sizeThatFits:] : 184 -> 176
~ -[AMPOnboardingFeatureView traitCollectionDidChange:] : 304 -> 280
~ -[AMPOnboardingFeatureView baselineOffsetFromBottom] : 68 -> 64
~ -[AMPOnboardingFeatureView imageView] : 16 -> 20
~ -[AMPOnboardingFeatureView setImageView:] : 80 -> 20
~ -[AMPOnboardingFeatureView titleLabel] : 16 -> 20
~ -[AMPOnboardingFeatureView setTitleLabel:] : 80 -> 20
~ -[AMPOnboardingFeatureView descriptionLabel] : 16 -> 20
~ -[AMPOnboardingFeatureView setDescriptionLabel:] : 80 -> 20
~ -[AMPOnboardingMultiFeatureHeaderView initWithFeatures:] : 520 -> 532
~ -[AMPOnboardingMultiFeatureHeaderView layoutSubviews] : 1092 -> 1052
~ -[AMPOnboardingMultiFeatureHeaderView traitCollectionDidChange:] : 280 -> 264
~ -[AMPOnboardingMultiFeatureHeaderView setContainerHeight:] : 96 -> 100
~ -[AMPOnboardingMultiFeatureHeaderView setIsPresentedInFormSheet:] : 84 -> 88
~ -[AMPOnboardingMultiFeatureHeaderView updateContentSize] : 944 -> 888
~ -[AMPOnboardingMultiFeatureHeaderView titleLabel] : 16 -> 20
~ -[AMPOnboardingMultiFeatureHeaderView setTitleLabel:] : 80 -> 20
~ -[AMPOnboardingMultiFeatureHeaderView containerHeight] : 16 -> 20
~ -[AMPOnboardingMultiFeatureHeaderView isPresentedInFormSheet] : 16 -> 20
~ -[AMPOnboardingMultiFeatureHeaderView featureViews] : 16 -> 20
~ -[AMPOnboardingMultiFeatureHeaderView setFeatureViews:] : 80 -> 20
~ +[AMPCardMetadataRegistration metadataForPassTypeIdentifier:serialNumber:size:] : 800 -> 768
~ ___79+[AMPCardMetadataRegistration metadataForPassTypeIdentifier:serialNumber:size:]_block_invoke : 2452 -> 2272
~ ___79+[AMPCardMetadataRegistration metadataForPassTypeIdentifier:serialNumber:size:]_block_invoke.20 : 88 -> 84
~ +[AMPCardMetadataRegistration _cardArtworkForPaymentPass:width:] : 540 -> 472
~ +[AMPCardMetadataRegistration _passesForPassTypeIdentifier:serialNumber:] : 1188 -> 1136
~ _PKPaymentPassFunction : 60 -> 12
~ _PKPassLibraryFunction : 60 -> 12
~ +[AMPAppleCardArtwork cardIcon] : 976 -> 876
~ +[AMPAppleCardArtwork cardIconString] : 544 -> 468
~ -[AMPPrivacyAnimatedTransitioning _presentedViewControllerForContext:] : 168 -> 144
~ -[AMPPrivacyAnimatedTransitioning _animateTransition:completionBlock:] : 692 -> 684
~ -[AMPPrivacyAnimatedTransitioning setViewController:] : 64 -> 12
~ -[AMPUserNotificationViewController viewWillLayoutSubviews] : 228 -> 212
~ -[AMPUserNotificationViewController viewWillDisappear:] : 96 -> 92
~ -[AMPUserNotificationViewController openNotification] : 68 -> 64
~ -[AMPUserNotificationViewController renderUserNotification:] : 668 -> 576
~ ___60-[AMPUserNotificationViewController renderUserNotification:]_block_invoke : 140 -> 128
~ -[AMPUserNotificationViewController didReceiveNotification:] : 556 -> 480
~ -[AMPUserNotificationViewController bagContract] : 16 -> 20
~ -[AMPUserNotificationViewController setBagContract:] : 80 -> 20
~ -[AMPUserNotificationViewController contentViewController] : 16 -> 20
~ -[AMPUserNotificationViewController setContentViewController:] : 80 -> 20
~ -[AMPPrivacyPresentationController containerViewWillLayoutSubviews] : 380 -> 364
~ -[AMPPrivacyPresentationController containerViewDidLayoutSubviews] : 200 -> 188
~ -[AMPPrivacyPresentationController _prepareDimmingViewIfNecessary] : 304 -> 284
~ -[AMPPrivacyPresentationController presentationTransitionWillBegin] : 120 -> 112
~ -[AMPPrivacyPresentationController dimmingView] : 16 -> 20
~ -[AMPPrivacyPresentationController setDimmingView:] : 80 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AMPUserNotificationContentDelegate>\""
- "@\"<AMSURLBagContract>\""
- "@\"<UIViewImplicitlyAnimating>\"24@0:8@\"<UIViewControllerContextTransitioning>\"16"
- "@\"AMPUserNotificationContentViewController\""
- "@\"AMSMetrics\""
- "@\"AMSUIOnboardingViewController\""
- "@\"AMSUserNotification\""
- "@\"AVPlayerViewController\""
- "@\"NSArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"OBPrivacyLinkController\""
- "@\"UIColor\"16@0:8"
- "@\"UIImage\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIViewController\""
- "@\"UIViewController\"32@0:8@\"UIPresentationController\"16q24"
- "@\"UIVisualEffectView\""
- "@\"_UIBackdropView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@56@0:8@16@24@32@40@48"
- "@?"
- "@?16@0:8"
- "AMPAppleCardArtwork"
- "AMPButton"
- "AMPCardMetadataRegistration"
- "AMPOnboardingFeature"
- "AMPOnboardingFeatureView"
- "AMPOnboardingHeaderView"
- "AMPOnboardingMultiFeatureHeaderView"
- "AMPOnboardingViewController"
- "AMPPrivacyAnimatedTransitioning"
- "AMPPrivacyPresentationController"
- "AMPTintedBackgroundButton"
- "AMPUserNotificationContentDelegate"
- "AMPUserNotificationContentViewController"
- "AMPUserNotificationViewController"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIPresentationController\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@16"
- "NSObject"
- "OSLogObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<AMPUserNotificationContentDelegate>\",W,N,V_delegate"
- "T@\"<AMSURLBagContract>\",&,N,V_bagContract"
- "T@\"AMPUserNotificationContentViewController\",&,N,V_contentViewController"
- "T@\"AMSMetrics\",&,N,V_metrics"
- "T@\"AMSUIOnboardingViewController\",&,N,V_onboardingController"
- "T@\"AMSUserNotification\",R,N,V_userNotification"
- "T@\"AVPlayerViewController\",R,N,V_videoPlayerController"
- "T@\"NSArray\",&,N,V_featureViews"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_metricsQueue"
- "T@\"NSString\",&,N,V_audioSessionCategory"
- "T@\"NSString\",&,N,V_descriptionText"
- "T@\"NSString\",&,N,V_primaryButtonText"
- "T@\"NSString\",&,N,V_titleText"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_descriptionText"
- "T@\"NSString\",R,N,V_titleText"
- "T@\"OBPrivacyLinkController\",R,N,V_privacyLinkController"
- "T@\"UIColor\",?,R,C,N"
- "T@\"UIImage\",&,N,V_image"
- "T@\"UIImage\",R,N"
- "T@\"UIImage\",R,N,V_image"
- "T@\"UIImageView\",&,N,V_imageView"
- "T@\"UIImageView\",R,N,V_imageView"
- "T@\"UILabel\",&,N,V_descriptionLabel"
- "T@\"UILabel\",&,N,V_titleLabel"
- "T@\"UILabel\",R,N,V_textLabel"
- "T@\"UILabel\",R,N,V_titleLabel"
- "T@\"UITraitCollection\",R,N"
- "T@\"UIView\",&,N,V_dimmingView"
- "T@\"UIViewController\",&,N,V_viewController"
- "T@\"UIVisualEffectView\",&,N,V_statusBarVisualEffectView"
- "T@\"_UIBackdropView\",&,N,V_backdropView"
- "T@?,C,N,V_primaryButtonCallback"
- "TB,GisPresentation,V_presentation"
- "TB,N,V_hasAppeared"
- "TB,N,V_hasPlayedVideo"
- "TB,N,V_isPresentedInFormSheet"
- "TB,N,V_viewHasAppeared"
- "TB,R,N"
- "TQ,?,R,N"
- "TQ,N,V_audioSessionCategoryOptions"
- "TQ,R"
- "Td,N,V_containerHeight"
- "Td,R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N"
- "T{CGSize=dd},R,N"
- "UIAdaptivePresentationControllerDelegate"
- "UIScrollViewDelegate"
- "UIViewControllerAnimatedTransitioning"
- "UNNotificationContentExtension"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activePresentationController"
- "_animateTransition:completionBlock:"
- "_audioSessionCategory"
- "_audioSessionCategoryOptions"
- "_backdropView"
- "_bagContract"
- "_baselineOffsetFromBottom"
- "_cardArtworkForPaymentPass:width:"
- "_containerHeight"
- "_contentViewController"
- "_delegate"
- "_descriptionLabel"
- "_descriptionText"
- "_dimmingView"
- "_featureViews"
- "_firstBaselineOffsetFromTop"
- "_frameForTransitionViewInPresentationSuperview:"
- "_hasAppeared"
- "_hasPlayedVideo"
- "_image"
- "_imageView"
- "_isPresentedInFormSheet"
- "_metrics"
- "_metricsQueue"
- "_onboardingController"
- "_passesForPassTypeIdentifier:serialNumber:"
- "_prepareDimmingViewIfNecessary"
- "_presentation"
- "_presentedViewControllerForContext:"
- "_primaryButtonCallback"
- "_primaryButtonText"
- "_privacyLinkController"
- "_setContinuousCornerRadius:"
- "_statusBarVisualEffectView"
- "_textLabel"
- "_titleLabel"
- "_titleText"
- "_userNotification"
- "_videoPlayerController"
- "_viewController"
- "_viewHasAppeared"
- "adaptivePresentationStyle"
- "adaptivePresentationStyleForPresentationController:"
- "adaptivePresentationStyleForPresentationController:traitCollection:"
- "addChildViewController:"
- "addGestureRecognizer:"
- "addObject:"
- "addObserver:forKeyPath:options:context:"
- "addSubview:"
- "adjustedContentInsetDidChange"
- "animateTransition:"
- "animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:"
- "animationEnded:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "artworkUrl"
- "associatedAccountServiceAccountIdentifier"
- "audioSessionCategory"
- "audioSessionCategoryOptions"
- "autorelease"
- "backdropView"
- "bagContract"
- "bagForProfile:profileVersion:"
- "bagKeySet"
- "bagSubProfile"
- "bagSubProfileVersion"
- "base64EncodedStringWithOptions:"
- "baselineOffsetFromBottom"
- "bounds"
- "cappedTraitCollection"
- "cardIcon"
- "cardIconString"
- "cardImageWithDimensions:"
- "category"
- "categoryOptions"
- "childTraitCollectionForViewController:"
- "childViewControllers"
- "class"
- "clearColor"
- "colorWithAlphaComponent:"
- "colorWithWhite:alpha:"
- "completeTransition:"
- "conformsToProtocol:"
- "containerHeight"
- "containerView"
- "containerViewDidLayoutSubviews"
- "containerViewWillLayoutSubviews"
- "containsObject:"
- "contentOverlayView"
- "contentViewController"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createUNNotificationActions"
- "d"
- "d16@0:8"
- "d24@0:8@\"<UIViewControllerContextTransitioning>\"16"
- "d24@0:8@16"
- "dataWithContentsOfURL:"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "description"
- "descriptionLabel"
- "descriptionText"
- "devicePrimaryInAppPaymentApplication"
- "didMoveToParentViewController:"
- "didReceiveNotification:"
- "didReceiveNotificationResponse:completionHandler:"
- "didTapPrimaryButton:"
- "dimmingView"
- "enqueueEvent:"
- "enumerateObjectsUsingBlock:"
- "eventForContentEngagementWithNotification:"
- "eventForVideoPlaybackForNotification:"
- "expectedContentSize"
- "extensionContext"
- "featureViews"
- "floatValue"
- "fontDescriptorWithSymbolicTraits:"
- "fontWithDescriptor:size:"
- "frame"
- "hasAppeared"
- "hasAssociatedPeerPaymentAccount"
- "hasPlayedVideo"
- "hash"
- "headerImage"
- "image"
- "imageView"
- "imageViewTapped:"
- "imageWithData:scale:"
- "informativeText"
- "init"
- "initWithContainerID:bag:"
- "initWithFeature:"
- "initWithFeatures:"
- "initWithFrame:"
- "initWithHeaderImage:titleText:descriptionText:primaryButtonText:privacyLinkController:"
- "initWithImage:titleText:descriptionText:"
- "initWithNibName:bundle:"
- "initWithNotification:delegate:"
- "initWithPresentedViewController:presentingViewController:"
- "initWithTarget:action:"
- "initWithTitleText:features:primaryButtonText:privacyLinkController:"
- "initWithUNNotification:"
- "insertSubview:atIndex:"
- "interruptibleAnimatorForTransition:"
- "isEqual:"
- "isEqualToString:"
- "isHighlighted"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isModalInPresentation"
- "isPresentation"
- "isPresentedInFormSheet"
- "isProxy"
- "isRunningUnitTests"
- "layer"
- "layoutIfNeeded"
- "layoutSubviews"
- "loadView"
- "localizedDescription"
- "logKey"
- "mainScreen"
- "mediaPause"
- "mediaPlay"
- "mediaPlayPauseButtonFrame"
- "mediaPlayPauseButtonTintColor"
- "mediaPlayPauseButtonType"
- "metadataForPassTypeIdentifier:serialNumber:size:"
- "metrics"
- "metricsForTextStyle:"
- "metricsQueue"
- "navigationController"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "onboardingController"
- "openNotification"
- "passWithPassTypeIdentifier:serialNumber:"
- "passesOfType:"
- "pause"
- "paymentNetworkIdentifier"
- "paymentPass"
- "performNotificationDefaultAction"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "player"
- "playerItemWithURL:"
- "playerWithPlayerItem:"
- "postNotificationName:object:userInfo:"
- "preferredContentSize"
- "preferredContentSizeCategory"
- "preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
- "preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:"
- "preferredFontForTextStyle:"
- "preferredFontForTextStyle:compatibleWithTraitCollection:"
- "presentViewController:animated:completion:"
- "presentation"
- "presentationController"
- "presentationController:prepareAdaptivePresentationController:"
- "presentationController:viewControllerForAdaptivePresentationStyle:"
- "presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:"
- "presentationControllerDidAttemptToDismiss:"
- "presentationControllerDidDismiss:"
- "presentationControllerShouldDismiss:"
- "presentationControllerWillDismiss:"
- "presentationStyle"
- "presentationTransitionWillBegin"
- "presentedView"
- "presentedViewController"
- "presentingViewController"
- "primaryAccountNumberSuffix"
- "primaryButtonCallback"
- "primaryButtonText"
- "privacyLinkController"
- "q16@0:8"
- "q24@0:8@\"UIPresentationController\"16"
- "q24@0:8@16"
- "q32@0:8@\"UIPresentationController\"16@\"UITraitCollection\"24"
- "q32@0:8@16@24"
- "registerBagKeySet:forProfile:profileVersion:"
- "release"
- "removeFromSuperview"
- "renderUserNotification:"
- "replaceCurrentItemWithPlayerItem:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safeAreaInsets"
- "scale"
- "scaledValueForValue:compatibleWithTraitCollection:"
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
- "self"
- "semanticContentAttribute"
- "sendSubviewToBack:"
- "serialNumber"
- "setAllowsEnteringFullScreen:"
- "setAllowsExternalPlayback:"
- "setAlpha:"
- "setAudioSessionCategory:"
- "setAudioSessionCategoryOptions:"
- "setBackdropView:"
- "setBackgroundColor:"
- "setBagContract:"
- "setCardArtwork:"
- "setCardType:"
- "setCategory:withOptions:error:"
- "setClipsToBounds:"
- "setContainerHeight:"
- "setContentMode:"
- "setContentSize:"
- "setContentViewController:"
- "setCornerRadius:"
- "setDelegate:"
- "setDescriptionLabel:"
- "setDescriptionShort:"
- "setDescriptionText:"
- "setDimmingView:"
- "setFeatureViews:"
- "setFont:"
- "setFrame:"
- "setHasAppeared:"
- "setHasPlayedVideo:"
- "setHighlighted:"
- "setImage:"
- "setImageView:"
- "setIsPresentedInFormSheet:"
- "setLineBreakMode:"
- "setMetrics:"
- "setMetricsQueue:"
- "setModalInPresentation:"
- "setModalPresentationStyle:"
- "setMuted:"
- "setNavigationBarHidden:animated:"
- "setNeedsLayout"
- "setNotificationActions:"
- "setNumberOfLines:"
- "setOnboardingController:"
- "setOverrideTraitCollection:forChildViewController:"
- "setPaymentNetwork:"
- "setPlayer:"
- "setPreferredContentSize:"
- "setPresentation:"
- "setPrimaryButtonCallback:"
- "setPrimaryButtonText:"
- "setSerialNumber:"
- "setShowsHorizontalScrollIndicator:"
- "setShowsVerticalScrollIndicator:"
- "setStatusBarVisualEffectView:"
- "setSuffix:"
- "setText:"
- "setTextAlignment:"
- "setTitleColor:forState:"
- "setTitleLabel:"
- "setTitleText:"
- "setTransform:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUpdatesNowPlayingInfoCenter:"
- "setUserInteractionEnabled:"
- "setViewController:"
- "setViewHasAppeared:"
- "sharedConfig"
- "sharedInstance"
- "sharedUserNotificationConfig"
- "sharediTunesStoreConfig"
- "shouldLog"
- "shouldLogToDisk"
- "shouldRemovePresentersView"
- "size"
- "sizeThatFits:"
- "startAccessingSecurityScopedResource"
- "statusBarVisualEffectView"
- "stopAccessingSecurityScopedResource"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "superclass"
- "supportedInterfaceOrientations"
- "systemBackgroundColor"
- "textLabel"
- "tintColor"
- "tintColorDidChange"
- "title"
- "titleLabel"
- "titleText"
- "traitCollection"
- "traitCollectionDidChange:"
- "traitCollectionWithPreferredContentSizeCategory:"
- "traitCollectionWithTraitsFromCollections:"
- "transitionDuration:"
- "updateBackgroundColor"
- "updateContentSize"
- "updateOverrideTraits"
- "userInterfaceIdiom"
- "userInterfaceLayoutDirectionForSemanticContentAttribute:"
- "userNotification"
- "userNotificationFromNotification:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<UIViewControllerContextTransitioning>\"16"
- "v24@0:8@\"UIPresentationController\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UNNotification\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"UIPresentationController\"16@\"UIPresentationController\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UNNotificationResponse\"16@?<v@?Q>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8{CGSize=dd}16"
- "v40@0:8@\"UIPresentationController\"16q24@\"<UIViewControllerTransitionCoordinator>\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UIViewController\"16{CGSize=dd}24"
- "v40@0:8@16@24d32"
- "v40@0:8@16q24@32"
- "v40@0:8@16{CGSize=dd}24"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "videoBounds"
- "videoPlayerController"
- "videoUrl"
- "view"
- "viewController"
- "viewController:didUpdatePreferredContentSize:"
- "viewControllerForKey:"
- "viewDidAppear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "viewHasAppeared"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillLayoutSubviews"
- "whiteColor"
- "zone"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}32@0:8{CGSize=dd}16"

```
