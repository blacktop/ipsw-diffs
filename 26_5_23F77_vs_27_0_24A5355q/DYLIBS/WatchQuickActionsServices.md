## WatchQuickActionsServices

> `/System/Library/PrivateFrameworks/WatchQuickActionsServices.framework/WatchQuickActionsServices`

```diff

-183.11.0.0.0
-  __TEXT.__text: 0xb670
-  __TEXT.__auth_stubs: 0x590
+191.0.0.0.0
+  __TEXT.__text: 0xad8c
   __TEXT.__objc_methlist: 0xa6c
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x4ee
+  __TEXT.__cstring: 0x4fd
   __TEXT.__oslogstring: 0xb90
-  __TEXT.__gcc_except_tab: 0x230
+  __TEXT.__gcc_except_tab: 0x250
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__objc_classname: 0x216
-  __TEXT.__objc_methname: 0x255b
-  __TEXT.__objc_methtype: 0x8c3
-  __TEXT.__objc_stubs: 0x1cc0
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x530
+  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x558
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_selrefs: 0x980
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0x180
   __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x5a0
   __AUTH_CONST.__objc_const: 0xe40
   __AUTH_CONST.__objc_doubleobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x480

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE8EE298-D486-3D77-8231-0C3CF720899B
-  Functions: 269
+  UUID: D122F0A6-CFB1-31DC-B6D4-9D798D110072
+  Functions: 266
   Symbols:   1162
-  CStrings:  673
+  CStrings:  183
 
Symbols:
+ GCC_except_table2
+ ___58-[WQAOverlayCoordinator _mainQueue_showUIForQuickActions:]_block_invoke.417
+ ___66-[WatchQuickActionsServices _handleAppDidBecomeActiveNotification]_block_invoke.508
+ ___66-[WatchQuickActionsServices registerQuickActions:startupCallback:]_block_invoke.513
+ ___69-[WatchQuickActionsServices _handleAppDidEnterBackgroundNotification]_block_invoke.510
+ ___70-[WQAOverlayCoordinator animateConfirmationForQuickAction:completion:]_block_invoke.396
+ ___70-[WQAOverlayCoordinator animateConfirmationForQuickAction:completion:]_block_invoke_2.397
+ ___70-[WQAOverlayCoordinator animateConfirmationForQuickAction:completion:]_block_invoke_3.398
+ ___80-[WQAOverlayCoordinator _mainQueue_showHintsWithPrimaryQuickActions:completion:]_block_invoke.431
+ ___80-[WQAOverlayCoordinator _mainQueue_showHintsWithPrimaryQuickActions:completion:]_block_invoke_2.435
+ ___95-[WatchQuickActionsServices userInterfaceClient:processMessageFromServer:withIdentifier:error:]_block_invoke.518
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.480
+ ___block_literal_global.501
+ ___block_literal_global.512
+ ___block_literal_global.516
+ ___block_literal_global.606
+ ___block_literal_global.608
+ ___block_literal_global.610
+ ___block_literal_global.620
+ ___block_literal_global.622
+ ___block_literal_global.627
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x9
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___58-[WQAOverlayCoordinator _mainQueue_showUIForQuickActions:]_block_invoke.354
- ___66-[WatchQuickActionsServices _handleAppDidBecomeActiveNotification]_block_invoke.445
- ___66-[WatchQuickActionsServices registerQuickActions:startupCallback:]_block_invoke.450
- ___69-[WatchQuickActionsServices _handleAppDidEnterBackgroundNotification]_block_invoke.447
- ___70-[WQAOverlayCoordinator animateConfirmationForQuickAction:completion:]_block_invoke.333
- ___70-[WQAOverlayCoordinator animateConfirmationForQuickAction:completion:]_block_invoke_2.334
- ___70-[WQAOverlayCoordinator animateConfirmationForQuickAction:completion:]_block_invoke_3.335
- ___80-[WQAOverlayCoordinator _mainQueue_showHintsWithPrimaryQuickActions:completion:]_block_invoke.368
- ___80-[WQAOverlayCoordinator _mainQueue_showHintsWithPrimaryQuickActions:completion:]_block_invoke_2.372
- ___95-[WatchQuickActionsServices userInterfaceClient:processMessageFromServer:withIdentifier:error:]_block_invoke.455
- ___block_literal_global.417
- ___block_literal_global.438
- ___block_literal_global.449
- ___block_literal_global.453
- ___block_literal_global.544
- ___block_literal_global.546
- ___block_literal_global.548
- ___block_literal_global.558
- ___block_literal_global.560
- ___block_literal_global.565
- _objc_msgSend$decodeObjectForKey:
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AXUIService>\""
- "@\"<WQAHostLifecycleObserver>\""
- "@\"<WQAOverlayDataSource>\""
- "@\"<WatchQuickActionAnimationHandler>\""
- "@\"<WatchQuickActionHostObserver>\""
- "@\"AXAccessQueue\"24@0:8Q16"
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXUIClient\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"WQAOverlayCoordinator\"16"
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSDictionary\"48@0:8@\"NSDictionary\"16Q24@\"NSString\"32^@40"
- "@\"NSDictionary\"52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40^@44"
- "@\"NSHashTable\""
- "@\"NSMutableArray\""
- "@\"NSSet\"24@0:8Q16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8Q16"
- "@\"UIBezierPath\""
- "@\"UIColor\""
- "@\"UIView\""
- "@\"WQAOverlayCoordinator\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16Q24^@32"
- "@48@0:8@16@24@32@?40"
- "@48@0:8@16@24Q32^@40"
- "@48@0:8@16Q24@32^@40"
- "@52@0:8@16Q24@32i40^@44"
- "@?"
- "@?16@0:8"
- "AXUIClientDelegate"
- "AXUIService"
- "Archiving"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16Q24"
- "BLSBacklightStateObserving"
- "Banner"
- "CGColor"
- "CGPath"
- "DigitalCrown"
- "Feedback"
- "HostLifecycle"
- "Internal"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "Scrolling"
- "T#,R"
- "T@\"<AXUIService>\",R,N,V_localService"
- "T@\"<WQAHostLifecycleObserver>\",W,N,V_hostLifecycleObserver"
- "T@\"<WQAOverlayDataSource>\",W,N,V_dataSource"
- "T@\"<WatchQuickActionAnimationHandler>\",W,N,V_animationHandler"
- "T@\"<WatchQuickActionHostObserver>\",W,N,V_hostObserver"
- "T@\"AXUIClient\",R,N,V_serverClient"
- "T@\"NSArray\",&,N,V_currentShapeLayersForHint"
- "T@\"NSMutableArray\",&,N,V_quickActionShapeLayers"
- "T@\"NSString\",&,N,V_quickActionIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_localizedTitle"
- "T@\"UIBezierPath\",&,N,V_path"
- "T@\"UIColor\",&,N,V_overlayTintColor"
- "T@\"UIView\",W,N,V_hostingView"
- "T@\"UIView\",W,N,V_viewToOverlay"
- "T@\"WQAOverlayCoordinator\",R,N,V_overlayCoordinator"
- "T@?,R,C,N,V_activationCallback"
- "TB,N,V_allowsResizingAnimations"
- "TB,N,V_hasNoActivationGesture"
- "TB,N,V_inputSourcesRequireFocusRing"
- "TB,N,V_receivedActivationGesture"
- "TB,N,V_started"
- "TB,R"
- "TQ,R"
- "Td,N,V_overlayCornerRadius"
- "Tq,N,V_internalQuickActionType"
- "Tq,N,V_quickActionVisualsToken"
- "Tq,N,V_visualsToken"
- "T{CGPoint=dd},N,V_overlayInset"
- "UUID"
- "UUIDString"
- "VisualsPriv"
- "Vv16@0:8"
- "WQAHostLifecycleObserver"
- "WQAOverlayCoordinator"
- "WQAOverlayDataSource"
- "WQAShapeLayer"
- "WatchControlSettingsObserver"
- "WatchCrownPressQuickAction"
- "WatchQuickAction"
- "WatchQuickActionHost"
- "WatchQuickActionHostCategory"
- "WatchQuickActionHostObserver"
- "WatchQuickActionPrivate"
- "WatchQuickActionsServices"
- "^{_NSZone=}16@0:8"
- "_UIViewBoundingPathChangeObserver"
- "_WQA_HostDeallocNotifier"
- "_activationCallback"
- "_addBoundingPathChangeObserver:"
- "_allowsResizingAnimations"
- "_animateUsingDefaultDampedSpringWithDelay:initialSpringVelocity:options:animations:completion:"
- "_animationHandler"
- "_applyOverlayFromView:withHostingView:"
- "_astFocusRingIsVisible"
- "_astHasDoubleTapActivationGesture"
- "_bezierPathWithPillRect:cornerRadius:"
- "_boundingPathMayHaveChangedForView:relativeToBoundsOriginOnly:"
- "_commonInitLocalizedTitle:quickActionType:targetView:hostingView:withQuickActivationCallback:withQuickActivationEndCallback:"
- "_createNonAnimatingShapeLayerFromPath:"
- "_currentShapeLayersForHint"
- "_dataSource"
- "_handleAppDidBecomeActiveNotification"
- "_handleAppDidEnterBackgroundNotification"
- "_handleFocusRingVisibilityChanged"
- "_handleWatchQuickActionsEnabledDidChangeNotification"
- "_hasNoActivationGesture"
- "_hostLifecycleObserver"
- "_hostObserver"
- "_hostingView"
- "_identifier"
- "_init"
- "_inputSourcesRequireFocusRing"
- "_internalQuickActionType"
- "_localService"
- "_local_removeQuickActionsWithIdentifiers:"
- "_localizedBannerInstructionText"
- "_localizedTitle"
- "_lock_quickActionHolders"
- "_mainQueue_addAnimatedShapeLayerForQuickAction:"
- "_mainQueue_backlightDidTurnOff"
- "_mainQueue_backlightDidTurnOn"
- "_mainQueue_cleanupHintViews"
- "_mainQueue_cleanupShapeLayers"
- "_mainQueue_removeShapeLayer:"
- "_mainQueue_showHintsWithPrimaryQuickActions:completion:"
- "_mainQueue_showUIForQuickActions:"
- "_overlayCoordinator"
- "_overlayCornerRadius"
- "_overlayInset"
- "_overlayTintColor"
- "_path"
- "_performBlockAccessingQuickActionHolders:"
- "_quickActionHolderLock"
- "_quickActionIdentifier"
- "_quickActionShapeLayers"
- "_quickActionVisualsToken"
- "_receivedActivationGesture"
- "_removeBoundingPathChangeObserver:"
- "_retrieveQuickActionForIdentifier:"
- "_sendAsyncMessageToServer:withIdentifier:completion:"
- "_sendMessageToServer:withIdentifier:"
- "_sendMessageToServer:withIdentifier:error:"
- "_serverClient"
- "_shouldObserveBacklightServicesForAppStateChange"
- "_shouldShowHintsForQuickActions:"
- "_started"
- "_tearDownServiceIfActive"
- "_updateGestureSettings"
- "_updateOverlaysIfNecessary"
- "_viewToOverlay"
- "_visualsToken"
- "_wqa_actuallyClearAndUnregisterQuickAction:"
- "_wqa_registerQuickActionForBoundingPathChanges:"
- "_wqa_unregisterExistingQuickActionForBoundingPathChanges"
- "accessQueueForProcessingMessageWithIdentifier:"
- "activationCallback"
- "addAnimation:forKey:"
- "addIndex:"
- "addObject:"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addSettingsObserver:"
- "addSublayer:"
- "addSubview:"
- "allObjects"
- "allValues"
- "allowsResizingAnimations"
- "animateConfirmationForQuickAction:completion:"
- "animateInstructionalBannerWithScaleFactor:interstepDuration:"
- "animateWithDuration:animations:completion:"
- "animationHandler"
- "animationWithKeyPath:"
- "applicationState"
- "applyBezierPath:withHostingView:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "ax_filteredArrayUsingBlock:"
- "ax_mappedArrayUsingBlock:"
- "backlight:activatingWithEvent:"
- "backlight:deactivatingWithEvent:"
- "backlight:didChangeAlwaysOnEnabled:"
- "backlight:didCompleteUpdateToState:forEvent:"
- "backlight:didCompleteUpdateToState:forEvents:abortedEvents:"
- "backlight:performingEvent:"
- "backlightState"
- "bezierPathWithRoundedRect:cornerRadius:"
- "boolValue"
- "bounds"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleWithPath:"
- "callStackSymbols"
- "canShowOverlays"
- "cancel"
- "class"
- "clearColor"
- "clearQuickActions"
- "clearQuickActionsWithCompletion:"
- "colorWithRed:green:blue:alpha:"
- "conformsToProtocol:"
- "connectionWillBeInterruptedForClientWithIdentifier:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "containsObject:"
- "convertRect:toCoordinateSpace:"
- "coordinateSpace"
- "cornerCurve"
- "cornerRadius"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentShapeLayersForHint"
- "currentVisualsToken"
- "d"
- "d16@0:8"
- "dataSource"
- "dealloc"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "defaultCenter"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "focusItemContainer"
- "frame"
- "functionWithName:"
- "greyActivationGesture"
- "hasNoActivationGesture"
- "hash"
- "hideInstructionalBanner"
- "hostLifecycleObserver"
- "hostObserver"
- "hostingView"
- "i24@0:8@\"NSString\"16"
- "i24@0:8@16"
- "indexSet"
- "init"
- "initWithCoder:"
- "initWithDataSource:"
- "initWithFrame:"
- "initWithIdentifier:serviceBundleName:"
- "initWithLocalizedTitle:activationCallback:"
- "initWithLocalizedTitle:completionHandler:"
- "initWithLocalizedTitle:targetView:activationCallback:"
- "initWithLocalizedTitle:targetView:hostingView:activationCallback:"
- "inputSourcesRequireFocusRing"
- "internalQuickActionType"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isLoaded"
- "isMemberOfClass:"
- "isProxy"
- "isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
- "layer"
- "length"
- "loadAndReturnError:"
- "localService"
- "localizedStringForKey:value:table:"
- "mainAccessQueue"
- "mainBundle"
- "mainQueue"
- "messageWithIdentifierRequiresWritingBlock:"
- "messageWithIdentifierShouldBeProcessedAsynchronously:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "overlayCoordinator"
- "overlayCornerRadius"
- "overlayInset"
- "overlayTintColor"
- "parentFocusEnvironment"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "possibleRequiredEntitlementsForProcessingMessageWithIdentifier:"
- "previousState"
- "principalClass"
- "processInfo"
- "processInitializationMessage:"
- "processMessage:withIdentifier:fromClientWithIdentifier:error:"
- "processMessage:withIdentifier:fromClientWithIdentifier:pid:error:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:completion:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:"
- "processName"
- "q"
- "q16@0:8"
- "quickActionDidBecomeInactive:"
- "quickActionFromSerializedData:error:"
- "quickActionHostDidInvalidate"
- "quickActionHostInvalidated:"
- "quickActionHostingView"
- "quickActionIdentifier"
- "quickActionPath"
- "quickActionPrimaryView"
- "quickActionShapeLayers"
- "quickActionVisualsToken"
- "quickActionWillActivate:"
- "quickActionWillHint:"
- "quickActionWillPulse:"
- "quickActionsForOverlayCoordinator:"
- "receivedActivationGesture"
- "refreshOverlaysIfNecessary"
- "registerQuickActions:"
- "registerQuickActions:startupCallback:"
- "release"
- "removeAllObjects"
- "removeFromSuperlayer"
- "removeFromSuperview"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsAtIndexes:"
- "removeObserver:"
- "requestCrownPress"
- "requestCrownPressWithCompletionHandler:"
- "requestFeedbackForQuickActionType:"
- "requestStartScrollWithDirection:"
- "requestStopScroll"
- "requiredEntitlementForProcessingMessageWithIdentifier:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "sendSynchronousMessage:withIdentifier:error:"
- "serializedDataFromQuickAction:error:"
- "serverClient"
- "serviceTypeForClientWithIdentifier:"
- "serviceWasFullyInitialized"
- "setAffineTransform:"
- "setAllowsResizingAnimations:"
- "setAlpha:"
- "setAnimationHandler:"
- "setAutoreverses:"
- "setBackgroundColor:"
- "setBounds:"
- "setCurrentShapeLayersForHint:"
- "setDataSource:"
- "setDelegate:"
- "setDuration:"
- "setFillColor:"
- "setFillMode:"
- "setFillRule:"
- "setFrame:"
- "setFromValue:"
- "setHasNoActivationGesture:"
- "setHostLifecycleObserver:"
- "setHostObserver:"
- "setHostingView:"
- "setInputSourcesRequireFocusRing:"
- "setInternalQuickActionType:"
- "setLineWidth:"
- "setMask:"
- "setObject:forKeyedSubscript:"
- "setOpacity:"
- "setOverlayCornerRadius:"
- "setOverlayInset:"
- "setOverlayTintColor:"
- "setPath:"
- "setPosition:"
- "setQuickActionHostObserver:"
- "setQuickActionIdentifier:"
- "setQuickActionShapeLayers:"
- "setQuickActionVisualsToken:"
- "setReceivedActivationGesture:"
- "setRemovedOnCompletion:"
- "setRepeatCount:"
- "setStarted:"
- "setStrokeColor:"
- "setTimingFunction:"
- "setToValue:"
- "setTransform:"
- "setViewToOverlay:"
- "setVisualsToken:"
- "setWithArray:"
- "sharedApplication"
- "sharedBacklight"
- "sharedInstance"
- "shouldUseLocalServiceBundle"
- "showInstructionalBannerWithTitle:subtitle:"
- "startWithCallback:"
- "state"
- "stopCurrentOverlays"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "superclass"
- "superlayer"
- "supportsSecureCoding"
- "unarchivedObjectOfClasses:fromData:error:"
- "unregisterQuickActionIdentifiers:startupCallback:"
- "unregisterQuickActions:"
- "unregisterQuickActions:startupCallback:"
- "updateLocalizedTitle:"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<WatchQuickActionHostObserver>\"16"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"WatchControlSettings\"16"
- "v24@0:8@\"WatchQuickAction\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"<BLSBacklightStateObservable>\"16B24"
- "v28@0:8@\"UIView\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"<BLSBacklightStateObservable>\"16@\"BLSBacklightChangeEvent\"24"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8{CGPoint=dd}16"
- "v40@0:8@\"<BLSBacklightStateObservable>\"16q24@\"BLSBacklightChangeEvent\"32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8{CGPoint=dd}16d32"
- "v48@0:8@\"<BLSBacklightStateObservable>\"16q24@\"NSArray\"32@\"NSArray\"40"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSDictionary\"16Q24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8@16q24@32@40"
- "v52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8@16Q24@32i40@?44"
- "v64@0:8@16q24@32@40@?48@?56"
- "viewToOverlay"
- "visualsToken"
- "watchControlSettingsDidChange:"
- "weakObjectsHashTable"
- "wqa_setHostLifecycleObserver:"
- "zone"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
