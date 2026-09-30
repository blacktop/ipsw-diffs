## MXUIService

> `/System/Library/PrivateFrameworks/MXUIService.framework/MXUIService`

```diff

-315.6.1.0.0
-  __TEXT.__text: 0x8994
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x84c
-  __TEXT.__const: 0x100
+320.18.1.0.0
+  __TEXT.__text: 0xe008
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0xb7c
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0xa0e
+  __TEXT.__oslogstring: 0x951
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__cstring: 0x5a5
-  __TEXT.__oslogstring: 0x523
-  __TEXT.__unwind_info: 0x178
-  __TEXT.__objc_classname: 0x12d
-  __TEXT.__objc_methname: 0x2013
-  __TEXT.__objc_methtype: 0x605
-  __TEXT.__objc_stubs: 0x1340
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_classname: 0x177
+  __TEXT.__objc_methname: 0x2931
+  __TEXT.__objc_methtype: 0x6d4
+  __TEXT.__objc_stubs: 0x1a80
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x820
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x1680
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xec
+  __DATA_CONST.__objc_selrefs: 0xa60
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x440
+  __AUTH_CONST.__objc_const: 0x1a08
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x300
-  __DATA.__common: 0x48
+  __DATA.__common: 0x90
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BannerKit.framework/BannerKit
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/MXUIServiceClient.framework/MXUIServiceClient
   - /System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5A2AFE98-34B9-3D52-9FD3-3FA9A0FAA409
-  Functions: 97
-  Symbols:   613
-  CStrings:  553
+  UUID: 18EC1A3D-FB18-3F0E-9F5C-459F5332FDA1
+  Functions: 170
+  Symbols:   858
+  CStrings:  704
 
Symbols:
+ +[MXUIServicePillManager sharedInstance]
+ +[MXUIServicePillManager sharedInstance].cold.1
+ -[MXUIServiceBanner actionHandler]
+ -[MXUIServiceBanner bannerActive]
+ -[MXUIServiceBanner bannerTimeoutInSeconds]
+ -[MXUIServiceBanner centerContentItems]
+ -[MXUIServiceBanner constraintsForLayoutMode]
+ -[MXUIServiceBanner createConstraintsForAskOrReverseBanner]
+ -[MXUIServiceBanner headSetString]
+ -[MXUIServiceBanner isAskOrReverseBanner]
+ -[MXUIServiceBanner leadingAccessoryView]
+ -[MXUIServiceBanner leadingViewWritable]
+ -[MXUIServiceBanner pillView]
+ -[MXUIServiceBanner setActionHandler:]
+ -[MXUIServiceBanner setBannerActive:]
+ -[MXUIServiceBanner setBannerTimeoutInSeconds:]
+ -[MXUIServiceBanner setCenterContentItems:]
+ -[MXUIServiceBanner setConstraintsForLayoutMode:]
+ -[MXUIServiceBanner setHeadSetString:]
+ -[MXUIServiceBanner setIsAskOrReverseBanner:]
+ -[MXUIServiceBanner setLeadingAccessoryView:]
+ -[MXUIServiceBanner setLeadingViewWritable:]
+ -[MXUIServiceBanner setPillView:]
+ -[MXUIServiceBanner setTimerRequired:]
+ -[MXUIServiceBanner setTrailingAccessoryView:]
+ -[MXUIServiceBanner setTrailingViewWritable:]
+ -[MXUIServiceBanner setUseJindoPath:]
+ -[MXUIServiceBanner setUuid:]
+ -[MXUIServiceBanner timerRequired]
+ -[MXUIServiceBanner trailingAccessoryView]
+ -[MXUIServiceBanner trailingViewWritable]
+ -[MXUIServiceBanner useJindoPath]
+ -[MXUIServiceBanner uuid]
+ -[MXUIServiceBanner viewComposeWithConstraints]
+ -[MXUIServiceBanner viewDidAppear:]
+ -[MXUIServiceBannerCarPlayVideo .cxx_destruct]
+ -[MXUIServiceBannerCarPlayVideo _addDismissalHandlerForView:]
+ -[MXUIServiceBannerCarPlayVideo _createActionButtonForCarPlayVideo:]
+ -[MXUIServiceBannerCarPlayVideo _createBannerTapViewForCarPlayVideo]
+ -[MXUIServiceBannerCarPlayVideo _createConnectBannerTextLabelForCarPlayVideo:bottomLabel:]
+ -[MXUIServiceBannerCarPlayVideo configureBannerViewsForCarPlayVideo]
+ -[MXUIServiceBannerCarPlayVideo configureCarPlayVideoBanner:]
+ -[MXUIServiceBannerCarPlayVideo createConstraintsForAskOrReverseBanner]
+ -[MXUIServiceBannerCarPlayVideo handleTapOnButton:]
+ -[MXUIServiceBannerCarPlayVideo handleTapToDismissBanner:]
+ -[MXUIServiceBannerCarPlayVideo init]
+ -[MXUIServiceBannerCarPlayVideo preferredContentSizeWithPresentationSize:containerSize:]
+ -[MXUIServiceBannerCarPlayVideo viewDidDisappear:]
+ -[MXUIServiceBannerCarPlayVideo viewWillLayoutSubviews]
+ -[MXUIServicePill .cxx_destruct]
+ -[MXUIServicePill activityIdentifier]
+ -[MXUIServicePill backgroundActivityAttribution]
+ -[MXUIServicePill description]
+ -[MXUIServicePill dismiss]
+ -[MXUIServicePill initWithBackgroundActivity:]
+ -[MXUIServicePill showWithTapHandler:]
+ -[MXUIServicePill tapHandler]
+ -[MXUIServicePill updateAttribution]
+ -[MXUIServicePillManager .cxx_destruct]
+ -[MXUIServicePillManager activePills]
+ -[MXUIServicePillManager dismiss:]
+ -[MXUIServicePillManager init]
+ -[MXUIServicePillManager publisher]
+ -[MXUIServicePillManager show:]
+ -[MXUIService_BannerUIDelegate showCarPlayVideoBanner:completionHandler:]
+ -[MXUIService_BannerUIDelegate updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:]
+ _MXUIService_CommonButtonParam_RouteToCar
+ _NSLog
+ _OBJC_CLASS_$_BSAuditToken
+ _OBJC_CLASS_$_MXUIServiceBannerCarPlayVideo
+ _OBJC_CLASS_$_MXUIServicePill
+ _OBJC_CLASS_$_MXUIServicePillManager
+ _OBJC_CLASS_$_STActivityAttribution
+ _OBJC_CLASS_$_STBackgroundActivitiesStatusDomainBackgroundActivityAttribution
+ _OBJC_CLASS_$_STBackgroundActivitiesStatusDomainPublisher
+ _OBJC_IVAR_$_MXUIServiceBanner._leadingViewWritable
+ _OBJC_IVAR_$_MXUIServiceBanner._timerRequired
+ _OBJC_IVAR_$_MXUIServiceBanner._trailingViewWritable
+ _OBJC_IVAR_$_MXUIServiceBanner._trailingViewWritableHeight
+ _OBJC_IVAR_$_MXUIServiceBanner._trailingViewWritableWidth
+ _OBJC_IVAR_$_MXUIServiceBanner._useheadSetString
+ _OBJC_IVAR_$_MXUIServiceBannerCarPlayVideo._actionButton
+ _OBJC_IVAR_$_MXUIServicePill._activityIdentifier
+ _OBJC_IVAR_$_MXUIServicePill._backgroundActivityAttribution
+ _OBJC_IVAR_$_MXUIServicePill._tapHandler
+ _OBJC_IVAR_$_MXUIServicePillManager._activePills
+ _OBJC_IVAR_$_MXUIServicePillManager._publisher
+ _OBJC_METACLASS_$_MXUIServiceBannerCarPlayVideo
+ _OBJC_METACLASS_$_MXUIServicePill
+ _OBJC_METACLASS_$_MXUIServicePillManager
+ __OBJC_$_CLASS_METHODS_MXUIServicePillManager
+ __OBJC_$_INSTANCE_METHODS_MXUIServiceBannerCarPlayVideo
+ __OBJC_$_INSTANCE_METHODS_MXUIServicePill
+ __OBJC_$_INSTANCE_METHODS_MXUIServicePillManager
+ __OBJC_$_INSTANCE_VARIABLES_MXUIServiceBannerCarPlayVideo
+ __OBJC_$_INSTANCE_VARIABLES_MXUIServicePill
+ __OBJC_$_INSTANCE_VARIABLES_MXUIServicePillManager
+ __OBJC_$_PROP_LIST_MXUIServicePill
+ __OBJC_$_PROP_LIST_MXUIServicePillManager
+ __OBJC_CLASS_RO_$_MXUIServiceBannerCarPlayVideo
+ __OBJC_CLASS_RO_$_MXUIServicePill
+ __OBJC_CLASS_RO_$_MXUIServicePillManager
+ __OBJC_METACLASS_RO_$_MXUIServiceBannerCarPlayVideo
+ __OBJC_METACLASS_RO_$_MXUIServicePill
+ __OBJC_METACLASS_RO_$_MXUIServicePillManager
+ ___102-[MXUIService_BannerUIDelegate updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:]_block_invoke
+ ___30-[MXUIServicePillManager init]_block_invoke
+ ___30-[MXUIServicePillManager init]_block_invoke_2
+ ___31-[MXUIServicePillManager show:]_block_invoke
+ ___31-[MXUIServicePillManager show:]_block_invoke.43
+ ___34-[MXUIServicePillManager dismiss:]_block_invoke
+ ___34-[MXUIServicePillManager dismiss:]_block_invoke.44
+ ___40+[MXUIServicePillManager sharedInstance]_block_invoke
+ ___73-[MXUIService_BannerUIDelegate showCarPlayVideoBanner:completionHandler:]_block_invoke
+ ___block_descriptor_32_e59_v16?0"STBackgroundActivitiesStatusDomainUserInteraction"8l
+ ___block_descriptor_48_e8_32s40s_e118_v24?0"STMutableBackgroundActivitiesStatusDomainData"8"STMutableBackgroundActivitiesStatusDomainDataChangeContext"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.38
+ _gMXUIServiceBannerCarPlayVideo
+ _gMXUIServicePillTrace
+ _objc_enumerationMutation
+ _objc_getProperty
+ _objc_msgSend$_addDismissalHandlerForView:
+ _objc_msgSend$_createActionButtonForCarPlayVideo:
+ _objc_msgSend$_createBannerTapViewForCarPlayVideo
+ _objc_msgSend$_createConnectBannerTextLabelForCarPlayVideo:bottomLabel:
+ _objc_msgSend$actionHandler
+ _objc_msgSend$activeBackgroundActivities
+ _objc_msgSend$activePills
+ _objc_msgSend$activityIdentifier
+ _objc_msgSend$addAttribution:
+ _objc_msgSend$attributionWithAuditToken:
+ _objc_msgSend$backgroundActivityAttribution
+ _objc_msgSend$bannerActive
+ _objc_msgSend$boolValue
+ _objc_msgSend$configureBannerViewsForCarPlayVideo
+ _objc_msgSend$configureCarPlayVideoBanner:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:constant:
+ _objc_msgSend$constraintsForLayoutMode
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copy
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createConstraintsForAskOrReverseBanner
+ _objc_msgSend$dismiss
+ _objc_msgSend$dismiss:
+ _objc_msgSend$handleUserInteractionsWithBlock:
+ _objc_msgSend$initWithBackgroundActivity:
+ _objc_msgSend$initWithBackgroundActivityIdentifier:activityAttribution:showsWhenForeground:
+ _objc_msgSend$layer
+ _objc_msgSend$leadingAccessoryView
+ _objc_msgSend$leadingViewWritable
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$publisher
+ _objc_msgSend$realToken
+ _objc_msgSend$removeAttribution:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setActionHandler:
+ _objc_msgSend$setBannerActive:
+ _objc_msgSend$setBannerTimeoutInSeconds:
+ _objc_msgSend$setBaseForegroundColor:
+ _objc_msgSend$setConstraintsForLayoutMode:
+ _objc_msgSend$setIsAskOrReverseBanner:
+ _objc_msgSend$setLeadingAccessoryView:
+ _objc_msgSend$setLeadingViewWritable:
+ _objc_msgSend$setTimerRequired:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setTrailingAccessoryView:
+ _objc_msgSend$setTrailingViewWritable:
+ _objc_msgSend$setUseJindoPath:
+ _objc_msgSend$setUuid:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$show:
+ _objc_msgSend$showWithTapHandler:
+ _objc_msgSend$systemDarkGreenColor
+ _objc_msgSend$systemGreenColor
+ _objc_msgSend$tapHandler
+ _objc_msgSend$tokenForCurrentProcess
+ _objc_msgSend$trailingAccessoryView
+ _objc_msgSend$trailingViewWritable
+ _objc_msgSend$updateAttribution
+ _objc_msgSend$updateVolatileData:completion:
+ _objc_msgSend$uuid
+ _objc_msgSend$viewComposeWithConstraints
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_setProperty_nonatomic_copy
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
- -[MXUIServiceBanner _createConstraintsForConnectBannerIfNeeded]
- -[MXUIServiceBanner viewIsAppearing:]
- _OBJC_IVAR_$_MXUIServiceBanner._headSetString
- _OBJC_IVAR_$_MXUIServiceBanner._leadingAccessorySymbol
- _OBJC_IVAR_$_MXUIServiceBanner._leadingAccessorySymbolSize
- _OBJC_IVAR_$_MXUIServiceBanner._leadingAccessorySymbolSizeJindo
- _OBJC_IVAR_$_MXUIServiceBanner._leadingAccessorySymbolSizeNonJindo
- _OBJC_IVAR_$_MXUIServiceBanner._leadingView
- _OBJC_IVAR_$_MXUIServiceBanner._trailingView
- _OBJC_IVAR_$_MXUIServiceBanner._trailingViewHeight
- _OBJC_IVAR_$_MXUIServiceBanner._trailingViewWidth
- _gCurrentBanners
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_createConstraintsForConnectBannerIfNeeded
- _objc_msgSend$leadingView
- _objc_msgSend$removeObject:
- _objc_msgSend$trailingView
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "-MXUIService- %s: Showing STBackgroundActivityStatus pill (activityIdentifier='%{public}@', yesToShow='%d')"
+ "-MXUIServiceBanner- %s: ActiveLayoutMode set to %ld\n"
+ "-MXUIServiceBannerCarPlayVideo- %s: %@ didDisappear"
+ "-MXUIServiceBannerCarPlayVideo- %s: %@ view configure is not done yet"
+ "-MXUIServiceBannerCarPlayVideo- %s: Calling button tap callback\n"
+ "-MXUIServiceBannerCarPlayVideo- %s: Got UUID %@"
+ "-MXUIServiceBannerCarPlayVideo- %s: Handling CarPlay video button tap\n"
+ "-MXUIServiceBannerCarPlayVideo- %s: Handling tap for dismissal\n"
+ "-MXUIServicePill- %s: Added attribution for activity: %{public}@"
+ "-MXUIServicePill- %s: Dismissing %{public}@"
+ "-MXUIServicePill- %s: Removed attribution for activity: %{public}@"
+ "-MXUIServicePill- %s: STBackgroundActivitiesStatusDomainPublisher updateVolatileData completed for activity: %{public}@"
+ "-MXUIServicePill- %s: Showing %{public}@"
+ "-MXUIServicePill- %s: SystemStatus pill touch for %{public}@"
+ "-MXUIServicePill- %s: SystemStatus pill touch for %{public}@ but no tap handler"
+ "-MXUIServicePill- %s: Tap handler seeing activity %{public}@"
+ "-[MXUIServiceBanner setActiveLayoutMode:]"
+ "-[MXUIServiceBannerCarPlayVideo configureCarPlayVideoBanner:]"
+ "-[MXUIServiceBannerCarPlayVideo handleTapOnButton:]"
+ "-[MXUIServiceBannerCarPlayVideo handleTapToDismissBanner:]"
+ "-[MXUIServiceBannerCarPlayVideo viewDidDisappear:]"
+ "-[MXUIServiceBannerCarPlayVideo viewWillLayoutSubviews]"
+ "-[MXUIServicePill dismiss]"
+ "-[MXUIServicePill showWithTapHandler:]"
+ "-[MXUIServicePillManager dismiss:]_block_invoke"
+ "-[MXUIServicePillManager init]_block_invoke"
+ "-[MXUIServicePillManager init]_block_invoke_2"
+ "-[MXUIServicePillManager show:]_block_invoke"
+ "-[MXUIService_BannerUIDelegate updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:]"
+ "<MXUIServicePill: activityIdentifier=%@; attribution=%@; tapHandler=%p>"
+ "@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\""
+ "@\"STBackgroundActivitiesStatusDomainPublisher\""
+ "@20@0:8B16"
+ "@?16@0:8"
+ "Constraints already created\n"
+ "MXUIServiceBannerCarPlayVideo"
+ "MXUIServicePill"
+ "MXUIServicePillManager"
+ "T@\"NSMutableArray\",&,N,V_centerContentItems"
+ "T@\"NSMutableDictionary\",&,N,V_constraintsForLayoutMode"
+ "T@\"NSMutableDictionary\",R,V_activePills"
+ "T@\"NSString\",&,N,V_useheadSetString"
+ "T@\"NSString\",R,C,N,V_activityIdentifier"
+ "T@\"NSUUID\",&,N,V_uuid"
+ "T@\"PLPillView\",&,N,V_pillView"
+ "T@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\",R,C,N,V_backgroundActivityAttribution"
+ "T@\"STBackgroundActivitiesStatusDomainPublisher\",R,V_publisher"
+ "T@\"UIView\",&,N,V_leadingAccessoryView"
+ "T@\"UIView\",&,N,V_trailingAccessoryView"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",&,N,V_leadingViewWritable"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",&,N,V_trailingViewWritable"
+ "T@?,C,N,V_actionHandler"
+ "T@?,R,C,N,V_tapHandler"
+ "TB,N,V_isAskOrReverseBanner"
+ "TB,N,V_timerRequired"
+ "TB,N,V_useJindoPath"
+ "TB,V_bannerActive"
+ "Td,N,V_bannerTimeoutInSeconds"
+ "VIDEO_SHOW_IN_CAR"
+ "VIDEO_SHOW_ON_PHONE"
+ "VIDEO_WILL_PLAY_IN_CAR"
+ "VIDEO_WILL_PLAY_ON_PHONE"
+ "_actionButton"
+ "_activePills"
+ "_activityIdentifier"
+ "_addDismissalHandlerForView:"
+ "_backgroundActivityAttribution"
+ "_createActionButtonForCarPlayVideo:"
+ "_createBannerTapViewForCarPlayVideo"
+ "_createConnectBannerTextLabelForCarPlayVideo:bottomLabel:"
+ "_leadingViewWritable"
+ "_publisher"
+ "_tapHandler"
+ "_timerRequired"
+ "_trailingViewWritable"
+ "_trailingViewWritableHeight"
+ "_trailingViewWritableWidth"
+ "_useheadSetString"
+ "actionHandler"
+ "activeBackgroundActivities"
+ "activePills"
+ "activityIdentifier"
+ "addAttribution:"
+ "attributionWithAuditToken:"
+ "backgroundActivityAttribution"
+ "bannerActive"
+ "bannerTimeoutInSeconds"
+ "boolValue"
+ "centerContentItems"
+ "configureBannerViewsForCarPlayVideo"
+ "configureCarPlayVideoBanner:"
+ "constraintLessThanOrEqualToAnchor:constant:"
+ "constraintsForLayoutMode"
+ "containsObject:"
+ "copy"
+ "countByEnumeratingWithState:objects:count:"
+ "createConstraintsForAskOrReverseBanner"
+ "dismiss"
+ "dismiss:"
+ "handleTapOnButton:"
+ "handleTapToDismissBanner:"
+ "handleUserInteractionsWithBlock:"
+ "headSetString"
+ "initWithBackgroundActivity:"
+ "initWithBackgroundActivityIdentifier:activityAttribution:showsWhenForeground:"
+ "isAskOrReverseBanner"
+ "layer"
+ "leadingAccessoryView"
+ "leadingViewWritable"
+ "mxuiservice_trace"
+ "mxuiservicebannercarplayvideo_trace"
+ "mxuiservicepill_trace"
+ "objectForKey:"
+ "pillView"
+ "play.tv.fill"
+ "publisher"
+ "realToken"
+ "removeAttribution:"
+ "removeObjectForKey:"
+ "setActionHandler:"
+ "setBannerActive:"
+ "setBannerTimeoutInSeconds:"
+ "setBaseForegroundColor:"
+ "setConstraintsForLayoutMode:"
+ "setHeadSetString:"
+ "setIsAskOrReverseBanner:"
+ "setLeadingAccessoryView:"
+ "setLeadingViewWritable:"
+ "setPillView:"
+ "setTimerRequired:"
+ "setTitle:"
+ "setTrailingAccessoryView:"
+ "setTrailingViewWritable:"
+ "setUseJindoPath:"
+ "setUuid:"
+ "setValue:forKey:"
+ "sharedInstance"
+ "show:"
+ "showCarPlayVideoBanner:completionHandler:"
+ "showWithTapHandler:"
+ "systemDarkGreenColor"
+ "systemGreenColor"
+ "tapHandler"
+ "timerRequired"
+ "tokenForCurrentProcess"
+ "trailingAccessoryView"
+ "trailingViewWritable"
+ "updateAttribution"
+ "updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:"
+ "updateVolatileData:completion:"
+ "useJindoPath"
+ "uuid"
+ "v16@?0@\"STBackgroundActivitiesStatusDomainUserInteraction\"8"
+ "v24@0:8d16"
+ "v24@?0@\"STMutableBackgroundActivitiesStatusDomainData\"8@\"STMutableBackgroundActivitiesStatusDomainDataChangeContext\"16"
+ "v36@0:8@\"NSString\"16C24@?<v@?i@\"NSError\">28"
+ "v36@0:8@16C24@?28"
+ "viewComposeWithConstraints"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N,V_leadingView"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N,V_trailingView"
- "_createConstraintsForConnectBannerIfNeeded"
- "_headSetString"
- "_leadingAccessorySymbol"
- "_leadingAccessorySymbolSize"
- "_leadingAccessorySymbolSizeJindo"
- "_leadingAccessorySymbolSizeNonJindo"
- "_leadingView"
- "_trailingView"
- "_trailingViewHeight"
- "_trailingViewWidth"
- "removeObject:"
- "viewIsAppearing:"

```
