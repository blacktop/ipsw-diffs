## AppStoreOverlays

> `/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays`

```diff

-8.5.1.0.0
-  __TEXT.__text: 0x658c
-  __TEXT.__auth_stubs: 0x3a0
+27.0.33.0.0
+  __TEXT.__text: 0x5db4
   __TEXT.__objc_methlist: 0xb8c
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x641
+  __TEXT.__cstring: 0x650
   __TEXT.__oslogstring: 0x942
-  __TEXT.__gcc_except_tab: 0x70
+  __TEXT.__gcc_except_tab: 0x50
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x2a0
-  __TEXT.__objc_classname: 0x212
-  __TEXT.__objc_methname: 0x1a15
-  __TEXT.__objc_methtype: 0x62d
-  __TEXT.__objc_stubs: 0x1500
-  __DATA_CONST.__got: 0x108
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x300
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x798
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x1348
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0x3c0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77BB47FB-DD27-35B7-AE95-7D0B685E0AE2
+  UUID: A1FC3B32-74CF-3C38-A083-9DD09F034F3F
   Functions: 213
-  Symbols:   945
-  CStrings:  525
+  Symbols:   951
+  CStrings:  126
 
Symbols:
+ ___53-[ASOOverlayViewController _loadViewServiceIfNeeded:]_block_invoke.56
+ ___54-[ASOOverlayViewController _loadRemoteViewController:]_block_invoke.63
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x9
- ___53-[ASOOverlayViewController _loadViewServiceIfNeeded:]_block_invoke.14
- ___54-[ASOOverlayViewController _loadRemoteViewController:]_block_invoke.21
- _objc_autorelease
Functions:
~ -[ASOOverlayAppClipConfiguration initWithStorage:] : 108 -> 116
~ -[ASOOverlayAppClipConfiguration initWithCoder:] : 320 -> 308
~ -[ASOOverlayAppClipConfiguration copyWithZone:] : 116 -> 112
~ -[ASOOverlayAppClipConfiguration setPosition:] : 108 -> 104
~ -[ASOOverlayAppClipConfiguration position] : 88 -> 84
~ -[ASOOverlayAppClipConfiguration additionalValueForKey:serviceContext:] : 172 -> 168
~ -[ASOOverlayAppClipConfiguration encodeWithCoder:] : 116 -> 112
~ -[ASOOverlayAppClipConfiguration description] : 196 -> 180
~ -[ASOOverlayAppConfiguration initWithStorage:] : 108 -> 116
~ -[ASOOverlayAppConfiguration initWithCoder:] : 320 -> 308
~ -[ASOOverlayAppConfiguration copyWithZone:] : 116 -> 112
~ -[ASOOverlayAppConfiguration setPosition:] : 108 -> 104
~ -[ASOOverlayAppConfiguration position] : 88 -> 84
~ -[ASOOverlayAppConfiguration setUserDismissible:] : 108 -> 104
~ -[ASOOverlayAppConfiguration userDismissible] : 88 -> 84
~ -[ASOOverlayAppConfiguration additionalValueForKey:] : 116 -> 108
~ -[ASOOverlayAppConfiguration encodeWithCoder:] : 116 -> 112
~ -[ASOOverlayAppConfiguration description] : 196 -> 180
~ -[ASOOverlayManager initWithScene:] : 264 -> 268
~ -[ASOOverlayManager presentOverlay:] : 356 -> 304
~ ___36-[ASOOverlayManager presentOverlay:]_block_invoke : 296 -> 268
~ ___35-[ASOOverlayManager dismissOverlay]_block_invoke : 128 -> 120
~ -[ASOOverlayManager willStartPresentingOverlay] : 268 -> 244
~ ___47-[ASOOverlayManager didFinishDismissingOverlay]_block_invoke : 192 -> 180
~ -[ASOOverlayManager makeViewControllerIfNeeded] : 248 -> 228
~ -[ASOOverlayManager setViewController:] : 64 -> 12
~ -[UIWindowScene(AppOverlayManager) _aso_appOverlayManager] : 316 -> 304
~ -[ASOOverlayTransitionContext initWithCoder:] : 240 -> 232
~ -[ASOOverlayTransitionContext addAnimationBlock:] : 120 -> 116
~ -[ASOOverlayTransitionContext encodeWithCoder:] : 220 -> 212
~ -[ASOOverlayTransitionContext setAnimationBlocks:] : 64 -> 12
~ _getASCSignpostSpanClass : 220 -> 224
~ _ASOViewRenderOverlayRequested : 276 -> 272
~ -[ASODismissRemoteOverlayOperation cancel] : 208 -> 164
~ -[ASODismissRemoteOverlayOperation finishExecuting] : 256 -> 212
~ -[ASODismissRemoteOverlayOperation start] : 376 -> 324
~ -[ASODismissRemoteOverlayOperation isExecuting] : 20 -> 24
~ -[ASODismissRemoteOverlayOperation setIsExecuting:] : 16 -> 20
~ -[ASODismissRemoteOverlayOperation isFinished] : 20 -> 24
~ -[ASODismissRemoteOverlayOperation setIsFinished:] : 16 -> 20
~ -[ASOPresentRemoteOverlayOperation cancel] : 208 -> 164
~ -[ASOPresentRemoteOverlayOperation finishExecuting] : 256 -> 212
~ -[ASOPresentRemoteOverlayOperation start] : 464 -> 400
~ ___41-[ASOPresentRemoteOverlayOperation start]_block_invoke : 112 -> 108
~ -[ASOPresentRemoteOverlayOperation remoteOverlay] : 16 -> 20
~ -[ASOPresentRemoteOverlayOperation setRemoteOverlay:] : 80 -> 20
~ -[ASOPresentRemoteOverlayOperation isExecuting] : 20 -> 24
~ -[ASOPresentRemoteOverlayOperation setIsExecuting:] : 16 -> 20
~ -[ASOPresentRemoteOverlayOperation isFinished] : 20 -> 24
~ -[ASOPresentRemoteOverlayOperation setIsFinished:] : 16 -> 20
~ +[ASORemoteOverlay log] : 84 -> 68
~ -[ASORemoteOverlay initWithOverlay:contextProvider:hostSpan:] : 176 -> 188
~ -[ASORemoteOverlay finishWithError:] : 312 -> 304
~ -[ASORemoteOverlay context] : 84 -> 76
~ -[ASORemoteOverlay overlayConfiguration] : 252 -> 232
~ -[ASORemoteOverlay remoteStoreOverlayDidFailToLoadWithError:] : 308 -> 264
~ ___61-[ASORemoteOverlay remoteStoreOverlayDidFailToLoadWithError:]_block_invoke : 360 -> 332
~ -[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:] : 212 -> 224
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:]_block_invoke : 604 -> 560
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:]_block_invoke.14 : 248 -> 244
~ -[ASORemoteOverlay remoteStoreOverlayDidFinishPresentation:] : 164 -> 168
~ ___60-[ASORemoteOverlay remoteStoreOverlayDidFinishPresentation:]_block_invoke : 360 -> 332
~ -[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:] : 188 -> 196
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke : 600 -> 560
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke.21 : 248 -> 244
~ ___57-[ASORemoteOverlay remoteStoreOverlayDidFinishDismissal:]_block_invoke : 360 -> 332
~ -[ASORemoteOverlay setOverlay:] : 64 -> 12
~ -[ASORemoteOverlay setPresentationTransitionContext:] : 64 -> 12
~ -[ASOOverlayViewController initWithNibName:bundle:] : 216 -> 224
~ -[ASOOverlayViewController viewDidLoad] : 352 -> 332
~ -[ASOOverlayViewController viewDidLayoutSubviews] : 252 -> 236
~ -[ASOOverlayViewController presentOverlay:] : 388 -> 324
~ -[ASOOverlayViewController dismissOverlay] : 260 -> 204
~ -[ASOOverlayViewController failAllQueuedOverlaysWithError:] : 600 -> 576
~ -[ASOOverlayViewController loadViewServiceIfNeeded] : 140 -> 136
~ ___51-[ASOOverlayViewController loadViewServiceIfNeeded]_block_invoke : 188 -> 192
~ -[ASOOverlayViewController _loadViewServiceIfNeeded:] : 452 -> 400
~ ___53-[ASOOverlayViewController _loadViewServiceIfNeeded:]_block_invoke : 872 -> 792
~ ___53-[ASOOverlayViewController _loadViewServiceIfNeeded:]_block_invoke.14 -> ___53-[ASOOverlayViewController _loadViewServiceIfNeeded:]_block_invoke.56 : 232 -> 224
~ ___54-[ASOOverlayViewController _loadRemoteViewController:]_block_invoke : 496 -> 444
~ ___54-[ASOOverlayViewController _loadRemoteViewController:]_block_invoke.21 -> ___54-[ASOOverlayViewController _loadRemoteViewController:]_block_invoke.63 : 196 -> 188
~ ___54-[ASOOverlayViewController _loadRemoteViewController:]_block_invoke_2 : 616 -> 572
~ -[ASOOverlayViewController willStartPresentingOverlay:transitionContext:] : 212 -> 164
~ -[ASOOverlayViewController didFinishDismissingOverlay:] : 204 -> 156
~ -[ASOOverlayViewController viewServiceDidTerminateWithError:] : 368 -> 332
~ -[ASOOverlayViewController shutdownViewServiceIfOverlayOffScreen] : 216 -> 208
~ -[ASOOverlayViewController remoteViewController] : 16 -> 20
~ -[ASOOverlayViewController setRemoteViewController:] : 80 -> 20
~ -[ASOOverlayViewController currentOverlay] : 16 -> 20
~ -[ASOOverlayViewController setCurrentOverlay:] : 80 -> 20
~ -[ASOOverlayViewController viewServiceQueue] : 16 -> 20
~ -[ASOOverlayViewController setViewServiceQueue:] : 80 -> 20
~ -[ASOOverlayViewController isViewServiceLoading] : 16 -> 20
~ -[ASOOverlayViewController setIsViewServiceLoading:] : 16 -> 20
~ -[ASOOverlayViewController presentationQueue] : 16 -> 20
~ -[ASOOverlayViewController setPresentationQueue:] : 80 -> 20
~ +[ASOHostContext _extensionAuxiliaryHostProtocol] : 84 -> 68
~ ___49+[ASOHostContext _extensionAuxiliaryHostProtocol]_block_invoke : 76 -> 72
~ +[ASOHostContext _extensionAuxiliaryVendorProtocol] : 84 -> 68
~ ___51+[ASOHostContext _extensionAuxiliaryVendorProtocol]_block_invoke : 344 -> 328
~ -[ASOHostContext serviceContext] : 84 -> 76
~ -[ASOHostContext presentOverlayWithConfiguration:delegate:reply:] : 140 -> 144
~ -[ASOHostContext dismissOverlayWithReply:] : 100 -> 96
~ -[ASORemoteViewController viewServiceDidTerminateWithError:] : 348 -> 288
~ -[ASODismissRemoteOverlayOperation start].cold.1 : 128 -> 84
~ -[ASOPresentRemoteOverlayOperation start].cold.1 : 128 -> 84
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ASOOverlay>\""
- "@\"<ASORemoteOverlayHost>\""
- "@\"<ASORemoteViewControllerDelegate>\""
- "@\"ASCSignpostSpan\""
- "@\"ASOHostContext\""
- "@\"ASOHostContext\"16@0:8"
- "@\"ASOOverlayManager\""
- "@\"ASOOverlayTransitionContext\""
- "@\"ASOOverlayViewController\""
- "@\"ASOOverlayWindow\""
- "@\"ASORemoteOverlay\""
- "@\"ASORemoteViewController\""
- "@\"NSArray\"24@0:8@\"UIScene\"16"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSOperationQueue\""
- "@\"NSString\"16@0:8"
- "@\"UIScene\""
- "@\"UIScene\"16@0:8"
- "@\"_UIRemoteViewController\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@\"UIScene\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8{CGPoint=dd}16@32"
- "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
- "ASODismissRemoteOverlayOperation"
- "ASOHostContext"
- "ASOHostProtocol"
- "ASOOverlayAnimator"
- "ASOOverlayAppClipConfiguration"
- "ASOOverlayAppConfiguration"
- "ASOOverlayConfiguration"
- "ASOOverlayManager"
- "ASOOverlayTransitionContext"
- "ASOOverlayViewController"
- "ASOOverlayWindow"
- "ASOPresentRemoteOverlayOperation"
- "ASORemoteAppOverlayDelegate"
- "ASORemoteOverlayHost"
- "ASORemoteViewController"
- "ASORemoteViewControllerDelegate"
- "ASOServiceProtocol"
- "AppOverlayManager"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CGRectValue"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<ASOOverlay>\",&,N,V_overlay"
- "T@\"<ASOOverlayConfiguration>\",R,C,N"
- "T@\"<ASORemoteOverlayHost>\",W,N,V_contextProvider"
- "T@\"<ASORemoteViewControllerDelegate>\",W,N,V_delegate"
- "T@\"ASCSignpostSpan\",R,&,N,V_hostSpan"
- "T@\"ASOHostContext\",W,N,V_context"
- "T@\"ASOOverlayManager\",R,N"
- "T@\"ASOOverlayManager\",W,N,V_overlayManager"
- "T@\"ASOOverlayTransitionContext\",&,N,V_presentationTransitionContext"
- "T@\"ASOOverlayViewController\",&,N,V_viewController"
- "T@\"ASOOverlayWindow\",R,&,N,V_window"
- "T@\"ASORemoteOverlay\",&,N,V_currentOverlay"
- "T@\"ASORemoteOverlay\",&,N,V_remoteOverlay"
- "T@\"ASORemoteViewController\",&,N,V_remoteViewController"
- "T@\"NSMutableArray\",&,N,V_animationBlocks"
- "T@\"NSMutableDictionary\",R,&,N,V_storage"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_viewServiceQueue"
- "T@\"NSObject<OS_os_log>\",R"
- "T@\"NSOperationQueue\",&,N,V_presentationQueue"
- "T@\"NSString\",&,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",R,C"
- "T@\"UIScene\",W,N,G_scene,S_setScene:"
- "T@\"UIScene\",W,N,G_scene,S_setScene:,V_scene"
- "TB,N"
- "TB,N,V_isActive"
- "TB,N,V_isLoaded"
- "TB,N,V_isViewServiceLoading"
- "TB,R"
- "TB,V_isExecuting"
- "TB,V_isFinished"
- "TQ,R"
- "Tq,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_endFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_startFrame"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_UISceneComponentProviding"
- "_actionHandlersForScene:"
- "_actionRespondersForScene:"
- "_animationBlocks"
- "_aso_appOverlayManager"
- "_auxiliaryConnection"
- "_canAffectStatusBarAppearance"
- "_context"
- "_contextProvider"
- "_currentOverlay"
- "_delegate"
- "_endFrame"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_extensionContextForUUID:"
- "_hostSpan"
- "_isActive"
- "_isExecuting"
- "_isFinished"
- "_isLoaded"
- "_isSystemWindow"
- "_isViewServiceLoading"
- "_loadRemoteViewController:"
- "_loadViewServiceIfNeeded:"
- "_overlay"
- "_overlayManager"
- "_presentationQueue"
- "_presentationTransitionContext"
- "_registerSceneComponent:forKey:"
- "_remoteOverlay"
- "_remoteViewController"
- "_scene"
- "_scene:didTransitionFromActivationState:withReasonsMask:"
- "_scene:willTransitionToActivationState:withReasonsMask:"
- "_sceneComponentForKey:"
- "_sceneIdentifier"
- "_sceneWillInvalidate:"
- "_setScene:"
- "_settingsDiffActionsForScene:"
- "_startFrame"
- "_storage"
- "_viewController"
- "_viewServiceQueue"
- "_window"
- "activationState"
- "addAnimationBlock:"
- "addAnimationBlockInternal:"
- "addChildViewController:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addOperation:"
- "addSubview:"
- "additionalValueForKey:"
- "additionalValueForKey:serviceContext:"
- "allocWithZone:"
- "animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:"
- "animationBlocks"
- "appIdentifier"
- "arrayWithObjects:count:"
- "autorelease"
- "beginEmitting"
- "boolValue"
- "bounds"
- "bundleIdentifier"
- "campaignToken"
- "cancel"
- "class"
- "conformsToProtocol:"
- "connectedScenes"
- "containsObject:"
- "context"
- "contextProvider"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentDevice"
- "currentOverlay"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "delegate"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didChangeValueForKey:"
- "didEnterBackground"
- "didFinishDismissingOverlay"
- "didFinishDismissingOverlay:"
- "didMoveToParentViewController:"
- "didReceiveMemoryWarning"
- "disconnect"
- "dismissOverlay"
- "dismissOverlayOperationWithContextProvider:"
- "dismissOverlayWithReply:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endEmitting"
- "endFrame"
- "endFrameInternal"
- "errorWithDomain:code:userInfo:"
- "extensionsWithMatchingAttributes:completion:"
- "failAllQueuedOverlaysWithError:"
- "finishExecuting"
- "finishWithError:"
- "firstObject"
- "hasPrefix:"
- "hasPrivateEntitlement"
- "hash"
- "hitTest:withEvent:"
- "hostContextForOverlayViewService"
- "hostSpan"
- "init"
- "initWithAppIdentifier:position:"
- "initWithCoder:"
- "initWithContextProvider:"
- "initWithNibName:bundle:"
- "initWithOverlay:contextProvider:hostSpan:"
- "initWithPosition:"
- "initWithRemoteOverlay:"
- "initWithScene:"
- "initWithStartFrame:endFrame:"
- "initWithStorage:"
- "initWithWindowScene:"
- "instantiateViewControllerWithInputItems:connectionHandler:"
- "integerValue"
- "interfaceWithProtocol:"
- "isActive"
- "isCancelled"
- "isEqual:"
- "isInternalWindow"
- "isKindOfClass:"
- "isLoaded"
- "isMemberOfClass:"
- "isProxy"
- "isViewServiceLoading"
- "latestReleaseID"
- "layoutMargins"
- "loadViewIfNeeded"
- "loadViewServiceIfNeeded"
- "localizedDescription"
- "log"
- "mainBundle"
- "makeViewControllerIfNeeded"
- "mutableCopy"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKey:"
- "operationCount"
- "operations"
- "overlay"
- "overlayConfiguration"
- "overlayDelegate"
- "overlayManager"
- "overlayRequestedWithTag:"
- "performAnimations:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "position"
- "presentOverlay:"
- "presentOverlayOperation"
- "presentOverlayWithConfiguration:delegate:reply:"
- "presentationQueue"
- "presentationTransitionContext"
- "primaryTag"
- "productVariantID"
- "providerToken"
- "q16@0:8"
- "release"
- "remoteObjectProxy"
- "remoteOverlay"
- "remoteStoreOverlayDidFailToLoadWithError:"
- "remoteStoreOverlayDidFinishDismissal:"
- "remoteStoreOverlayDidFinishPresentation:"
- "remoteStoreOverlayWillStartDismissing:executeBlock:"
- "remoteStoreOverlayWillStartPresenting:executeBlock:"
- "remoteViewController"
- "remoteViewControllerForOverlayViewService"
- "removeFromParentViewController"
- "removeFromSuperview"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rootViewController"
- "self"
- "serviceContext"
- "setAdditionalValue:forKey:"
- "setAnimationBlocks:"
- "setAppIdentifier:"
- "setCampaignToken:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setContext:"
- "setContextProvider:"
- "setCurrentOverlay:"
- "setDelegate:"
- "setEndFrame:"
- "setEndFrameInternal:"
- "setFrame:"
- "setHidden:"
- "setInsetsLayoutMarginsFromSafeArea:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInvalidationHandler:"
- "setIsActive:"
- "setIsExecuting:"
- "setIsFinished:"
- "setIsLoaded:"
- "setIsViewServiceLoading:"
- "setLatestReleaseID:"
- "setLayoutMargins:"
- "setLevel:"
- "setMaxConcurrentOperationCount:"
- "setNeedsLayout"
- "setOverlay:"
- "setOverlayManager:"
- "setPosition:"
- "setPresentationQueue:"
- "setPresentationTransitionContext:"
- "setProductVariantID:"
- "setProviderToken:"
- "setRemoteOverlay:"
- "setRemoteViewController:"
- "setRootViewController:"
- "setStartFrame:"
- "setStartFrameInternal:"
- "setSuspended:"
- "setUserDismissable:"
- "setUserDismissible:"
- "setUserInteractionEnabled:"
- "setValue:forKey:"
- "setViewController:"
- "setViewRespectsSystemMinimumLayoutMargins:"
- "setViewServiceQueue:"
- "setWithArray:"
- "sharedApplication"
- "shutdownViewServiceIfOverlayOffScreen"
- "start"
- "startFrame"
- "startFrameInternal"
- "storage"
- "storeOverlay:didFailToLoadWithError:"
- "storeOverlay:didFinishDismissal:"
- "storeOverlay:didFinishPresentation:"
- "storeOverlay:willStartDismissal:"
- "storeOverlay:willStartPresentation:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synchronizeAnimationsInActions:"
- "userDismissable"
- "userDismissible"
- "userInterfaceIdiom"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"ASOOverlayTransitionContext\"16"
- "v24@0:8@\"ASORemoteOverlay\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"UIScene\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8q16"
- "v32@0:8@\"ASOOverlayTransitionContext\"16@?<v@?>24"
- "v32@0:8@\"ASORemoteOverlay\"16@\"ASOOverlayTransitionContext\"24"
- "v32@0:8@16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@?24"
- "v40@0:8@\"<ASOOverlayConfiguration>\"16@\"<ASORemoteAppOverlayDelegate>\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"UIScene\"16q24Q32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16q24Q32"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "valueWithCGRect:"
- "view"
- "viewController"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewServiceDidTerminateWithError:"
- "viewServiceQueue"
- "willChangeValueForKey:"
- "willMoveToParentViewController:"
- "willStartPresentingOverlay"
- "willStartPresentingOverlay:transitionContext:"
- "window"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
