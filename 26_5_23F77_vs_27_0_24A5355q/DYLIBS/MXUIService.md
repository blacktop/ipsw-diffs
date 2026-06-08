## MXUIService

> `/System/Library/PrivateFrameworks/MXUIService.framework/MXUIService`

```diff

-330.6.1.0.0
-  __TEXT.__text: 0xe008
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0xb7c
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0xa0e
-  __TEXT.__oslogstring: 0x951
+360.58.1.0.0
+  __TEXT.__text: 0x9dd0
+  __TEXT.__objc_methlist: 0xb9c
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x9e8
+  __TEXT.__oslogstring: 0x97b
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__unwind_info: 0x260
-  __TEXT.__objc_classname: 0x177
-  __TEXT.__objc_methname: 0x2931
-  __TEXT.__objc_methtype: 0x6d4
-  __TEXT.__objc_stubs: 0x1a80
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x1a0
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa60
+  __DATA_CONST.__objc_selrefs: 0xa58
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x440
-  __AUTH_CONST.__objc_const: 0x1a08
+  __AUTH_CONST.__cfstring: 0x4a0
+  __AUTH_CONST.__objc_const: 0x1820
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xf8
+  __DATA.__objc_ivar: 0xb8
   __DATA.__data: 0x300
   __DATA.__common: 0x90
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AB8BBDD-D60B-30AB-8198-3A784DD1352F
-  Functions: 170
-  Symbols:   858
-  CStrings:  704
+  UUID: A54F2764-71F3-3F5C-8731-904F5880F5A1
+  Functions: 227
+  Symbols:   975
+  CStrings:  152
 
Symbols:
+ -[MXUIServiceBanner _createButtonForStyle:]
+ -[MXUIServiceBanner _createTextLabelsForStyle:topText:bottomText:]
+ -[MXUIServiceBanner configureAudioMovedBanner:]
+ -[MXUIServiceBanner configureBannerWithStyle:configuration:]
+ -[MXUIServiceBanner createConstraintsForBannerLayout]
+ -[MXUIServiceBanner primaryText]
+ -[MXUIServiceBanner requestsAlertingAssertion]
+ -[MXUIServiceBanner setPrimaryText:]
+ -[MXUIServiceBanner setRequestsAlertingAssertion:]
+ -[MXUIServiceBanner setUsesExpandedLayout:]
+ -[MXUIServiceBanner usesExpandedLayout]
+ -[MXUIServiceBannerCarPlayVideo createConstraintsForBannerLayout]
+ -[MXUIService_BannerUIDelegate _showBannerWithStyle:parameters:completionHandler:]
+ -[MXUIService_BannerUIDelegate showAudioMovedBanner:completionHandler:]
+ GCC_except_table34
+ _MXUIService_CommonUIParam_ConnectionType
+ _MXUIService_CommonUIParam_HeadsetString
+ _MXUIService_CommonUIParam_RouteToCar
+ _MXUIService_CommonUIParam_SourceAppName
+ _MXUIService_CommonUIParam_UUID
+ _OBJC_IVAR_$_MXUIServiceBanner._primaryText
+ _OBJC_IVAR_$_MXUIServiceBanner._requestsAlertingAssertion
+ _OBJC_IVAR_$_MXUIServiceBanner._usesExpandedLayout
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _UIFontWeightSemibold
+ ___31-[MXUIServicePillManager show:]_block_invoke.84
+ ___34-[MXUIServicePillManager dismiss:]_block_invoke.85
+ ___82-[MXUIService_BannerUIDelegate _showBannerWithStyle:parameters:completionHandler:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.79
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_createButtonForStyle:
+ _objc_msgSend$_createTextLabelsForStyle:topText:bottomText:
+ _objc_msgSend$_showBannerWithStyle:parameters:completionHandler:
+ _objc_msgSend$configureBannerWithStyle:configuration:
+ _objc_msgSend$createConstraintsForBannerLayout
+ _objc_msgSend$setRequestsAlertingAssertion:
+ _objc_msgSend$setUsesExpandedLayout:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- -[MXUIServiceBanner _createConnectBannerTextLabel:bottomLabel:]
- -[MXUIServiceBanner _createConstraintsForDisconnectedBannerIfNeeded]
- -[MXUIServiceBanner _createConstraintsForUndoBannerIfNeeded]
- -[MXUIServiceBanner _createDisconnectedBannerTextLabel:bottomLabel:]
- -[MXUIServiceBanner _createUndoBannerTextLabel:bottomLabel:]
- -[MXUIServiceBanner createConstraintsForAskOrReverseBanner]
- -[MXUIServiceBanner getAppIcon:]
- -[MXUIServiceBanner headSetString]
- -[MXUIServiceBanner isAskOrReverseBanner]
- -[MXUIServiceBanner setHeadSetString:]
- -[MXUIServiceBanner setIsAskOrReverseBanner:]
- -[MXUIServiceBannerCarPlayVideo createConstraintsForAskOrReverseBanner]
- GCC_except_table32
- _MXUIService_CommonButtonParam_ConnectionType
- _MXUIService_CommonButtonParam_HeadsetString
- _MXUIService_CommonButtonParam_RouteToCar
- _MXUIService_CommonButtonParam_UUID
- _OBJC_CLASS_$_UIScreen
- _OBJC_IVAR_$_MXUIServiceBanner._backgroundColor
- _OBJC_IVAR_$_MXUIServiceBanner._ccItemsIcon
- _OBJC_IVAR_$_MXUIServiceBanner._ccItemsText
- _OBJC_IVAR_$_MXUIServiceBanner._ccText
- _OBJC_IVAR_$_MXUIServiceBanner._centerContentText
- _OBJC_IVAR_$_MXUIServiceBanner._collapseButton
- _OBJC_IVAR_$_MXUIServiceBanner._connectedBanner
- _OBJC_IVAR_$_MXUIServiceBanner._contentView
- _OBJC_IVAR_$_MXUIServiceBanner._customItems
- _OBJC_IVAR_$_MXUIServiceBanner._customView
- _OBJC_IVAR_$_MXUIServiceBanner._isAskOrReverseBanner
- _OBJC_IVAR_$_MXUIServiceBanner._isFirstInstance
- _OBJC_IVAR_$_MXUIServiceBanner._leadingAccessoryIconPath
- _OBJC_IVAR_$_MXUIServiceBanner._trailingAccessoryIconName
- _OBJC_IVAR_$_MXUIServiceBanner._trailingAccessoryIconPath
- _OBJC_IVAR_$_MXUIServiceBanner._trailingAccessoryText
- _OBJC_IVAR_$_MXUIServiceBanner._trailingViewWritableHeight
- _OBJC_IVAR_$_MXUIServiceBanner._trailingViewWritableWidth
- _OBJC_IVAR_$_MXUIServiceBanner._useheadSetString
- ___31-[MXUIServicePillManager show:]_block_invoke.43
- ___34-[MXUIServicePillManager dismiss:]_block_invoke.44
- ___65-[MXUIService_BannerUIDelegate showUndoButton:completionHandler:]_block_invoke
- ___68-[MXUIService_BannerUIDelegate showConnectButton:completionHandler:]_block_invoke
- ___73-[MXUIService_BannerUIDelegate showDisconnectedButton:completionHandler:]_block_invoke
- ___block_literal_global.38
- _objc_msgSend$_applicationIconImageForBundleIdentifier:format:scale:
- _objc_msgSend$_createBannerTapViewForCarPlayVideo
- _objc_msgSend$_createConnectBannerTextLabel:bottomLabel:
- _objc_msgSend$_createDisconnectedBannerTextLabel:bottomLabel:
- _objc_msgSend$_createUndoBannerTextLabel:bottomLabel:
- _objc_msgSend$configureConnectBanner:
- _objc_msgSend$configureDisconnectedBanner:
- _objc_msgSend$configureUndoBanner:
- _objc_msgSend$createConstraintsForAskOrReverseBanner
- _objc_msgSend$createDisconnectedButton
- _objc_msgSend$createInUseConnectButton
- _objc_msgSend$createReverseButton
- _objc_msgSend$mainScreen
- _objc_msgSend$scale
- _objc_msgSend$setIsAskOrReverseBanner:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ "-MXUIServiceBanner- %s: MXBannerStyleAudioMoved requires Jindo path — skipping non-Jindo layout"
+ "-[MXUIServiceBanner configureBannerWithStyle:configuration:]"
+ "AUDIO_MOVED_TO_SPEAKER"
+ "_MXUISScheduledTap"
+ "speaker.wave.3"
- "#16@0:8"
- "-MXUIServiceBanner- %s: Getting app icon for %{public}@"
- "-[MXUIServiceBanner configureConnectBanner:]"
- "-[MXUIServiceBanner configureDisconnectedBanner:]"
- "-[MXUIServiceBanner configureUndoBanner:]"
- "-[MXUIServiceBanner getAppIcon:]"
- ".cxx_destruct"
- "@\"<BNPresentableContext>\"16@0:8"
- "@\"<SBUISystemApertureElement>\"16@0:8"
- "@\"BNBannerSource\""
- "@\"BSAction\"16@0:8"
- "@\"MXUIServiceBanner\""
- "@\"NSArray\""
- "@\"NSLayoutConstraint\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\"16@0:8"
- "@\"NSUUID\""
- "@\"PLPillContentItem\""
- "@\"PLPillView\""
- "@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\""
- "@\"STBackgroundActivitiesStatusDomainPublisher\""
- "@\"UIButton\""
- "@\"UIColor\"16@0:8"
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIStackView\""
- "@\"UIView\""
- "@\"UIView<SBUISystemApertureAccessoryView>\""
- "@\"UIView<SBUISystemApertureAccessoryView>\"16@0:8"
- "@\"UIViewController\""
- "@\"UIViewController\"16@0:8"
- "@\"UIViewController<SBUISystemApertureElement>\"16@0:8"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "BNPresentable"
- "BNPresentableIdentifying"
- "BNPresentableObserving"
- "MXUIServiceBanner"
- "MXUIServiceBannerCarPlayVideo"
- "MXUIServiceDelegateProtocol"
- "MXUIServicePill"
- "MXUIServicePillManager"
- "MXUIService_BannerUIDelegate"
- "NSObject"
- "Q16@0:8"
- "SBUISA_standardInteritemPadding"
- "SBUISA_systemApertureLegibleContentLayoutMarginsGuide"
- "SBUISA_systemApertureObstructedAreaLayoutGuide"
- "SBUISA_systemApertureTrailingConcentricContentLayoutGuide"
- "SBUISystemApertureAccessoryView"
- "SBUISystemApertureElement"
- "SBUISystemApertureElementProviding"
- "SRHostedJindoPresentableAccessoryView"
- "T#,R"
- "T@\"<BNPresentableContext>\",?,W,N"
- "T@\"<SBUISystemApertureElement>\",?,R,W,N"
- "T@\"BSAction\",?,R,N"
- "T@\"NSMutableArray\",&,N,V_centerContentItems"
- "T@\"NSMutableDictionary\",&,N,V_constraintsForLayoutMode"
- "T@\"NSMutableDictionary\",R,V_activePills"
- "T@\"NSSet\",?,R,C,N"
- "T@\"NSString\",&,N,V_useheadSetString"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_activityIdentifier"
- "T@\"NSString\",R,C,N,V_associatedScenePersistenceIdentifier"
- "T@\"NSString\",R,C,N,V_requestIdentifier"
- "T@\"NSURL\",?,R,C,N"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"PLPillView\",&,N,V_pillView"
- "T@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\",R,C,N,V_backgroundActivityAttribution"
- "T@\"STBackgroundActivitiesStatusDomainPublisher\",R,V_publisher"
- "T@\"UIColor\",?,R,C,N"
- "T@\"UILabel\",&,N,V_ccBottomViewLabel"
- "T@\"UILabel\",&,N,V_ccTopViewLabel"
- "T@\"UIStackView\",&,N,V_verticalTrailingStackView"
- "T@\"UIView\",&,N,V_leadingAccessoryView"
- "T@\"UIView\",&,N,V_trailingAccessoryView"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",&,N,V_leadingViewWritable"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",&,N,V_trailingViewWritable"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N"
- "T@\"UIViewController\",?,R,N"
- "T@\"UIViewController<SBUISystemApertureElement>\",R,N"
- "T@?,C,N,V_actionHandler"
- "T@?,R,C,N,V_tapHandler"
- "TB,?,N"
- "TB,?,N,V_canRequestAlertingAssertion"
- "TB,?,R,N"
- "TB,?,R,N,GisDraggingDismissalEnabled"
- "TB,?,R,N,GisDraggingInteractionEnabled"
- "TB,?,R,N,GisTouchOutsideDismissalEnabled"
- "TB,N,V_isAskOrReverseBanner"
- "TB,N,V_timerRequired"
- "TB,N,V_useJindoPath"
- "TB,V_bannerActive"
- "TQ,?,N"
- "TQ,?,R,N"
- "TQ,R"
- "Td,?,R,N"
- "Td,N,V_bannerTimeoutInSeconds"
- "Ti,N,V_pid"
- "Tq,?,R,N"
- "Tq,N"
- "Tq,N,V_activeLayoutMode"
- "Tq,R,N"
- "T{CGSize=dd},?,R,N"
- "T{CGSize=dd},N,V_compactSize"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_actionButton"
- "_actionHandler"
- "_activeConstraints"
- "_activeLayoutMode"
- "_activePills"
- "_activityIdentifier"
- "_addDismissalHandlerForView:"
- "_applicationIconImageForBundleIdentifier:format:scale:"
- "_associatedScenePersistenceIdentifier"
- "_backgroundActivityAttribution"
- "_backgroundColor"
- "_bannerActive"
- "_bannerAssetTransaction"
- "_bannerSource"
- "_bannerTimeoutInSeconds"
- "_bannerTimer"
- "_bannerTransaction"
- "_banners"
- "_bundleID"
- "_canRequestAlertingAssertion"
- "_canShowWhileLocked"
- "_ccBottomViewLabel"
- "_ccItemsIcon"
- "_ccItemsText"
- "_ccText"
- "_ccTopViewLabel"
- "_centerContentItems"
- "_centerContentText"
- "_collapseButton"
- "_compactSize"
- "_connectedBanner"
- "_constraintsForLayoutMode"
- "_contentView"
- "_createActionButtonForCarPlayVideo:"
- "_createBannerTapView"
- "_createBannerTapViewForCarPlayVideo"
- "_createConnectBannerTextLabel:bottomLabel:"
- "_createConnectBannerTextLabelForCarPlayVideo:bottomLabel:"
- "_createConstraintsForDisconnectedBannerIfNeeded"
- "_createConstraintsForUndoBannerIfNeeded"
- "_createDeviceReplacementBannerTextLabel:"
- "_createDisconnectedBannerTextLabel:bottomLabel:"
- "_createUndoBannerTextLabel:bottomLabel:"
- "_customItems"
- "_customView"
- "_dispatchQueue"
- "_identifier"
- "_imageView"
- "_isAskOrReverseBanner"
- "_isFirstInstance"
- "_isInvalidated"
- "_leadingAccessoryIconName"
- "_leadingAccessoryIconPath"
- "_leadingAccessoryView"
- "_leadingViewWritable"
- "_mainQueue"
- "_minimalAccessoryView"
- "_pid"
- "_pillView"
- "_presentBanner"
- "_publisher"
- "_requestIdentifier"
- "_systemApertureLeadingAccessoryView"
- "_systemApertureTrailingAccessoryView"
- "_systemImageNamed:withConfiguration:"
- "_tapHandler"
- "_tightBoundingBoxLayoutGuide"
- "_timerRequired"
- "_trailingAccessoryIconName"
- "_trailingAccessoryIconPath"
- "_trailingAccessoryText"
- "_trailingAccessoryView"
- "_trailingViewWritable"
- "_trailingViewWritableHeight"
- "_trailingViewWritableWidth"
- "_useJindoPath"
- "_useheadSetString"
- "_uuid"
- "_vc"
- "_verticalTrailingStackView"
- "actionHandler"
- "activateConstraints:"
- "activateWithActionHandler:"
- "activeBackgroundActivities"
- "activeLayoutMode"
- "activePills"
- "activityIdentifier"
- "addAttribution:"
- "addGestureRecognizer:"
- "addObject:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "animateAlongsideTransition:completion:"
- "application:didFinishLaunchingWithOptions:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "associatedAppBundleIdentifier"
- "associatedScenePersistenceIdentifier"
- "attachedMinimalViewRequiresZeroPadding"
- "attributionWithAuditToken:"
- "autorelease"
- "background"
- "backgroundActivitiesToSuppress"
- "backgroundActivityAttribution"
- "bannerActive"
- "bannerContentOutsets"
- "bannerDidDismiss:"
- "bannerSourceForDestination:forRequesterIdentifier:"
- "bannerTimeoutInSeconds"
- "blackColor"
- "boolValue"
- "bottomAnchor"
- "bounds"
- "bundleForClass:"
- "bundleIdentifier"
- "buttonWithConfiguration:primaryAction:"
- "canRequestAlertingAssertion"
- "ccBottomViewLabel"
- "ccTopViewLabel"
- "centerContentItems"
- "centerXAnchor"
- "centerYAnchor"
- "checkifVideoAssetExists"
- "class"
- "clearColor"
- "colorWithAlphaComponent:"
- "colorWithRed:green:blue:alpha:"
- "compactSize"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "configurationWithPointSize:weight:"
- "configureBannerViews"
- "configureBannerViewsForCarPlayVideo"
- "configureCarPlayVideoBanner:"
- "configureConnectBanner:"
- "configureDisconnectedBanner:"
- "configureInputDeviceReplacementPillForConnectedDevice:replacedDevice:"
- "configureUndoBanner:"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "constraintGreaterThanOrEqualToAnchor:"
- "constraintGreaterThanOrEqualToConstant:"
- "constraintLessThanOrEqualToAnchor:"
- "constraintLessThanOrEqualToAnchor:constant:"
- "constraintsForLayoutMode"
- "containerSize"
- "containsObject:"
- "containsString:"
- "contentRole"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createConstraintsForAskOrReverseBanner"
- "createCustomStaticImageView:withIcon:"
- "createCustomView:WithCustomIconName:"
- "createDisconnectedButton"
- "createInUseConnectButton"
- "createReverseButton"
- "currentThread"
- "d"
- "d16@0:8"
- "deactivateConstraints:"
- "debugDescription"
- "description"
- "detachedMinimalView"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dismiss"
- "dismiss:"
- "dismissBanner:"
- "dismissBannerWithUUID:withResponse:"
- "dismissIfMatchesUUID:withResponse:"
- "draggingDidBeginWithGestureProxy:"
- "draggingDismissalEnabled"
- "draggingInteractionEnabled"
- "elementIdentifier"
- "fetchUIImageForClientConfig:"
- "firstBaselineAnchor"
- "getAppIcon:"
- "handleTap:"
- "handleTapOnButton:"
- "handleTapToDismissBanner:"
- "handleUserInteractionsWithBlock:"
- "hash"
- "headSetString"
- "heightAnchor"
- "i"
- "i16@0:8"
- "imageNamed:"
- "imageWithRenderingMode:"
- "init"
- "init:"
- "initWithBackgroundActivity:"
- "initWithBackgroundActivityIdentifier:activityAttribution:showsWhenForeground:"
- "initWithFrame:"
- "initWithImage:"
- "initWithLeadingAccessoryView:"
- "initWithLeadingAccessoryView:trailingAccessoryView:"
- "initWithNibName:bundle:"
- "initWithTarget:action:"
- "initWithText:"
- "initWithText:style:"
- "initWithUUIDString:"
- "intValue"
- "intrinsicContentSize"
- "invalidate"
- "invalidateWithReason:"
- "isAskOrReverseBanner"
- "isDraggingDismissalEnabled"
- "isDraggingInteractionEnabled"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isTouchOutsideDismissalEnabled"
- "keyColor"
- "lastObject"
- "launchAction"
- "launchURL"
- "layer"
- "layoutDescriptionWithError:"
- "leadingAccessoryView"
- "leadingAnchor"
- "leadingView"
- "leadingViewWritable"
- "length"
- "loadViewIfNeeded"
- "localizedStringForKey:value:table:"
- "mainBundle"
- "mainScreen"
- "maximumLayoutMode"
- "minimalView"
- "minimalViewLayoutAxis"
- "minimumLayoutMode"
- "numberWithInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pid"
- "pillView"
- "postPresentable:options:userInfo:error:"
- "preferredBackgroundActivitiesToSuppress"
- "preferredContentSizeWithPresentationSize:containerSize:"
- "preferredCustomAspectRatio"
- "preferredCustomLayout"
- "preferredHeightForBottomSafeArea"
- "preferredLayoutMode"
- "prefersFixedPortraitOrientation"
- "presentableBehavior"
- "presentableContext"
- "presentableDescription"
- "presentableDidAppearAsBanner:"
- "presentableDidDisappearAsBanner:withReason:"
- "presentableType"
- "presentableWillAppearAsBanner:"
- "presentableWillDisappearAsBanner:withReason:"
- "presentableWillNotAppearAsBanner:withReason:"
- "presentationBehaviors"
- "presentationSize"
- "preventsAutomaticDismissal"
- "preventsInteractiveDismissal"
- "providesHostedContent"
- "publisher"
- "q16@0:8"
- "realToken"
- "release"
- "removeAttribution:"
- "removeLastObject"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removedAccessoryColorCode:"
- "requestAlertingAssertion"
- "requestIdentifier"
- "requesterIdentifier"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "revokePresentableWithRequestIdentifier:reason:animated:userInfo:error:"
- "scale"
- "self"
- "setActionHandler:"
- "setActive:"
- "setActiveLayoutMode:"
- "setAlpha:"
- "setAutomaticallyInvalidatable:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setBannerActive:"
- "setBannerTimeoutInSeconds:"
- "setBannerTimer"
- "setBaseForegroundColor:"
- "setCanRequestAlertingAssertion:"
- "setCcBottomViewLabel:"
- "setCcTopViewLabel:"
- "setCenterContentItems:"
- "setCompactSize:"
- "setConfiguration:"
- "setConstraintsForLayoutMode:"
- "setContentMode:"
- "setCornerRadius:"
- "setFont:"
- "setFrame:"
- "setHeadSetString:"
- "setHidden:"
- "setImage:"
- "setIsAskOrReverseBanner:"
- "setLeadingAccessoryView:"
- "setLeadingViewWritable:"
- "setMarqueeEnabled:"
- "setMarqueeRunning:"
- "setMinimalViewLayoutAxis:"
- "setNumberOfTapsRequired:"
- "setNumberOfTouchesRequired:"
- "setObject:forKeyedSubscript:"
- "setPid:"
- "setPillView:"
- "setPreferredContentSize:"
- "setPreferredSymbolConfigurationForImage:"
- "setPresentableContext:"
- "setText:"
- "setTextColor:"
- "setTimerRequired:"
- "setTintColor:"
- "setTitle:"
- "setTrailingAccessoryView:"
- "setTrailingViewWritable:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUseJindoPath:"
- "setUserInteractionEnabled:"
- "setUuid:"
- "setValue:forKey:"
- "setVerticalTrailingStackView:"
- "shadowOutsets"
- "sharedInstance"
- "show:"
- "showBannerWithTimeout"
- "showCarPlayVideoBanner:completionHandler:"
- "showConnectButton:completionHandler:"
- "showDisconnectedButton:completionHandler:"
- "showInputDeviceReplacementPillForConnectedDevice:replacedDevice:"
- "showUndoButton:completionHandler:"
- "showWithTapHandler:"
- "sizeThatFits:forLayoutMode:"
- "statusBarStyleOverridesToSuppress"
- "stringWithFormat:"
- "superclass"
- "systemApertureElement"
- "systemApertureElementContext"
- "systemApertureElementProvider"
- "systemApertureElementViewController"
- "systemBlueColor"
- "systemDarkGreenColor"
- "systemFontOfSize:weight:"
- "systemGreenColor"
- "systemImageNamed:"
- "systemWhiteColor"
- "tapHandler"
- "timerRequired"
- "tintedButtonConfiguration"
- "tokenForCurrentProcess"
- "topAnchor"
- "touchOutsideDismissalEnabled"
- "trailingAccessoryView"
- "trailingAnchor"
- "trailingView"
- "trailingViewWritable"
- "updateAttribution"
- "updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:"
- "updateVolatileData:completion:"
- "useJindoPath"
- "userInfoForPosting"
- "userInteractionDidEndForBannerForPresentable:"
- "userInteractionWillBeginForBannerForPresentable:"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<BNPanGestureProxy>\"16"
- "v24@0:8@\"<BNPresentable>\"16"
- "v24@0:8@\"<BNPresentableContext>\"16"
- "v24@0:8@\"<UIViewControllerTransitionCoordinator>\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16i24"
- "v32@0:8@\"<BNPresentable>\"16@\"NSString\"24"
- "v32@0:8@\"NSDictionary\"16@?<v@?i@\"NSError\">24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSUUID\"16@\"NSNumber\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8@\"NSString\"16C24@?<v@?i@\"NSError\">28"
- "v36@0:8@16C24@?28"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "valueForKey:"
- "verticalTrailingStackView"
- "view"
- "viewComposeWithConstraints"
- "viewController"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillLayoutSubviews"
- "viewWillLayoutSubviewsWithTransitionCoordinator:"
- "widthAnchor"
- "window"
- "zone"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}40@0:8{CGSize=dd}16q32"
- "{CGSize=dd}48@0:8{CGSize=dd}16{CGSize=dd}32"
- "{UIEdgeInsets=dddd}16@0:8"

```
