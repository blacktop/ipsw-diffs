## ViewBridge

> `/System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge`

```diff

-767.5.0.0.0
-  __TEXT.__text: 0xb48a0
-  __TEXT.__auth_stubs: 0x1750
+769.1.0.0.0
+  __TEXT.__text: 0xc46a8
+  __TEXT.__auth_stubs: 0x1730
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x6a80
+  __TEXT.__objc_methlist: 0x7b1c
   __TEXT.__const: 0x229
-  __TEXT.__gcc_except_tab: 0x621c
-  __TEXT.__cstring: 0x22095
+  __TEXT.__gcc_except_tab: 0x629c
+  __TEXT.__cstring: 0x22081
   __TEXT.__oslogstring: 0xdfb9
-  __TEXT.__unwind_info: 0x3520
+  __TEXT.__unwind_info: 0x39f8
   __TEXT.__objc_classname: 0x11a0
-  __TEXT.__objc_methname: 0x129b0
+  __TEXT.__objc_methname: 0x129dd
   __TEXT.__objc_methtype: 0x42f8
-  __TEXT.__objc_stubs: 0xf180
+  __TEXT.__objc_stubs: 0xf1a0
   __DATA_CONST.__got: 0x628
   __DATA_CONST.__const: 0x650
   __DATA_CONST.__objc_classlist: 0x3a8

   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4580
+  __DATA_CONST.__objc_selrefs: 0x47e0
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH_CONST.__auth_got: 0xbb0
   __AUTH_CONST.__const: 0x3b38
   __AUTH_CONST.__cfstring: 0xfd40
-  __AUTH_CONST.__objc_const: 0xc9c8
+  __AUTH_CONST.__objc_const: 0xaaf8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x8
   __DATA.__objc_ivar: 0x758
-  __DATA.__data: 0x13c8
+  __DATA.__data: 0x13d0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x668
   __DATA.__common: 0x14

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1042C2A9-B2D5-3CED-A402-0082B75874CE
-  Functions: 3193
-  Symbols:   8401
-  CStrings:  10291
+  UUID: B7F99B43-DE6A-3A12-AA44-045CFF5ED789
+  Functions: 4830
+  Symbols:   10057
+  CStrings:  10288
 
Symbols:
+ +[NSAccessoryViewWindow windowWithContentRect:atopRemoteView:withColorization:].cold.1
+ +[NSCFRunLoopSemaphore _observe:whilePerforming:].cold.1
+ +[NSCFRunLoopSemaphore _observe:whilePerforming:].cold.2
+ +[NSCFRunLoopSemaphore _observe:whilePerforming:].cold.3
+ +[NSCFRunLoopSemaphore currentRunLoopMode].cold.1
+ +[NSCFRunLoopSemaphore initialize].cold.1
+ +[NSCFRunLoopSemaphore mode].cold.1
+ +[NSPreviewHostView allocWithZone:].cold.1
+ +[NSPreviewHostViewController forgetKeyboardFocusTheft:].cold.1
+ +[NSPreviewHostViewController launchTargetApp:options:error:].cold.1
+ +[NSPreviewHostViewController nsxpcInterface].cold.1
+ +[NSPreviewHostViewController rememberKeyboardFocusTheft:perpetratedByApp:].cold.1
+ +[NSPreviewHostViewController rememberKeyboardFocusTheft:perpetratedByApp:].cold.2
+ +[NSPreviewHostViewController rememberKeyboardFocusTheft:perpetratedByApp:].cold.3
+ +[NSPreviewHostViewController targetAppEnvironmentVariables].cold.1
+ +[NSPreviewHostViewController targetAppEnvironmentVariables].cold.2
+ +[NSPreviewHostViewController targetAppEnvironmentVariables].cold.3
+ +[NSPreviewHostViewController targetAppEnvironmentVariables].cold.4
+ +[NSPreviewHostViewController targetAppEnvironmentVariables].cold.5
+ +[NSPreviewHostViewController targetAppLaunchOptions].cold.1
+ +[NSPreviewStarter applicationDidFinishLaunching:].cold.1
+ +[NSPreviewStarter load].cold.1
+ +[NSPreviewStarter load].cold.2
+ +[NSPreviewStarter load].cold.3
+ +[NSPreviewTargetController _nsxpcListenerEndpoint].cold.1
+ +[NSPreviewTargetController _windowMayOrder:].cold.1
+ +[NSPreviewTargetController _windowMayOrder:].cold.2
+ +[NSPreviewTargetController _windowMayOrder:].cold.3
+ +[NSPreviewTargetController bootstrap:hostControllerProxy:reply:].cold.1
+ +[NSPreviewTargetController initialize].cold.1
+ +[NSPreviewTargetController listener:shouldAcceptNewConnection:].cold.1
+ +[NSPreviewTargetController listener:shouldAcceptNewConnection:].cold.2
+ +[NSPreviewTargetController listener:shouldAcceptNewConnection:].cold.3
+ +[NSPreviewTargetController nsxpcInterface].cold.1
+ +[NSPreviewTargetController nsxpcInterface].cold.2
+ +[NSPreviewTargetController preflight:reply:].cold.1
+ +[NSPreviewTargetController targetControllerClassForName:].cold.2
+ +[NSRemoteView _remoteViewForIdentifier:].cold.1
+ +[NSRemoteView _remoteViewForIdentifier:].cold.2
+ +[NSRemoteView anyRemoteViewAttachedToWindow:].cold.1
+ +[NSRemoteView endAppModalSession:].cold.1
+ +[NSRemoteView ensureAuxServiceAwareOfHostApp:].cold.1
+ +[NSRemoteView initAll].cold.1
+ +[NSRemoteView observeValueForKeyPath:ofObject:change:context:].cold.1
+ +[NSRemoteView observeValueForKeyPath:ofObject:change:context:].cold.2
+ +[NSRemoteView remoteViewsAttachedToWindow:].cold.1
+ +[NSRemoteView remoteViewsAttachedToWindow:].cold.2
+ +[NSRemoteView remoteViewsAttachedToWindow:].cold.3
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.1
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.10
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.11
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.12
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.13
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.2
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.3
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.4
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.5
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.6
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.7
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.8
+ +[NSRemoteView rendezvousWindow:kind:spawnedBy:styleMask:contentRect:identifier:listenerEndpoint:completion:].cold.9
+ +[NSRemoteView shouldEnsureAuxServiceAwareOfHostAppDueToInitialize].cold.1
+ +[NSRemoteViewController _onAppKitThreadRequestViewController:withBlock:].cold.1
+ +[NSRemoteViewController _onAppKitThreadRequestViewController:withBlock:].cold.2
+ +[NSRemoteViewController _onAppKitThreadRequestViewController:withBlock:].cold.3
+ +[NSRemoteViewController _onAppKitThreadRequestViewController:withBlock:].cold.4
+ +[NSRemoteViewController _requestViewController:withBlock:].cold.1
+ +[NSRemoteViewController requestViewController:connectionHandler:].cold.1
+ +[NSRemoteViewController requestViewController:fromServiceListenerEndpoint:connectionHandler:].cold.1
+ +[NSRemoteViewController requestViewController:fromServiceListenerEndpoint:connectionHandler:].cold.2
+ +[NSRemoteViewController requestViewController:fromServiceWithBundleIdentifier:connectionHandler:].cold.1
+ +[NSRemoteViewController requestViewController:fromServiceWithBundleIdentifier:connectionHandler:].cold.2
+ +[NSRemoteViewController requestViewController:withServiceViewControllerIdentifier:forRemoteView:connectionHandler:].cold.1
+ +[NSRemoteViewController requestViewControllerForExtensionWithIdentifier:fromServiceWithBundleIdentifier:serviceInstanceIdentifier:connectionHandler:].cold.1
+ +[NSRemoteViewController requestViewControllerForExtensionWithIdentifier:fromServiceWithBundleIdentifier:serviceInstanceIdentifier:connectionHandler:].cold.2
+ +[NSRemoteViewControllerForTouchBarItem copyConstraintIdentifier:].cold.1
+ +[NSRemoteViewMarshal nsxpcInterface:].cold.1
+ +[NSRemoteViewMarshal nsxpcInterface:].cold.2
+ +[NSRemoteViewMarshal nsxpcInterface:].cold.3
+ +[NSRemoteViewSemaphore semaphoreWithActivity:].cold.1
+ +[NSRendezvousWindowController bridgeKeysForSemiAutonomousWindowBase:].cold.1
+ +[NSRendezvousWindowController bridgeKeys].cold.1
+ +[NSServiceViewController allocWithZone:].cold.1
+ +[NSServiceViewController controllerForIdentifier:].cold.1
+ +[NSServiceViewController currentAppIsViewService].cold.1
+ +[NSServiceViewController exportedInterface].cold.1
+ +[NSServiceViewController filterStyleMask:].cold.1
+ +[NSServiceViewController filterStyleMask:].cold.2
+ +[NSServiceViewController overrideHostAppMinimal].cold.1
+ +[NSServiceViewController overrideHostApp].cold.1
+ +[NSServiceViewController remoteViewControllerInterface].cold.1
+ +[NSServiceViewController serviceBundle].cold.1
+ +[NSServiceViewController serviceBundle].cold.2
+ +[NSServiceViewController serviceViewControllerForWindow:].cold.1
+ +[NSServiceViewController setAccessibilityParent:forWindow:].cold.1
+ +[NSServiceViewController setAccessibilityParent:forWindow:].cold.2
+ +[NSServiceViewController withHostAppAuditToken:invoke:].cold.1
+ +[NSServiceViewController withHostProcessIdentifier:invoke:].cold.1
+ +[NSServiceViewController withHostProcessIdentifier:invoke:].cold.2
+ +[NSServiceViewController withHostProcessIdentifier:invoke:].cold.3
+ +[NSServiceViewController(CompatibilityDylibs) addCompatibilityDylib:].cold.1
+ +[NSServiceViewController(Introspector) _windowForContextID:fromViewService:error:].cold.1
+ +[NSServiceViewController(Introspector) _windowForContextID:fromViewService:error:].cold.2
+ +[NSServiceViewControllerForTouchBarItem controllerWithTouchBarItem:andAppearance:].cold.1
+ +[NSServiceViewControllerForTouchBarItem controllerWithTouchBarItem:andAppearance:].cold.2
+ +[NSServiceViewControllerForTouchBarItem controllerWithTouchBarItem:andAppearance:].cold.3
+ +[NSServiceViewControllerForTouchBarItem describeTouchBars:].cold.1
+ +[NSServiceViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.1
+ +[NSServiceViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.2
+ +[NSServiceViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.3
+ +[NSServiceViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.4
+ +[NSServiceViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.5
+ +[NSServiceViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.6
+ +[NSServiceViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.7
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.1
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.10
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.2
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.3
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.4
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.5
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.6
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.7
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.8
+ +[NSServiceViewControllerForTouchBarItem showOverlayTouchBar:withOptions:].cold.9
+ +[NSServiceViewControllerForTouchBarItem touchBarProviders:inWindow:includingWindowItself:].cold.1
+ +[NSServiceViewControllerForTouchBarItem touchBarProvidersForWindow:includingWindowItself:].cold.1
+ +[NSServiceViewControllerForTouchBarItem touchBarsForProviders:].cold.1
+ +[NSServiceViewControllerForTouchBarItem viewServiceTouchBarControllerIdentifier:].cold.1
+ +[NSServiceViewControllerForTouchBarItem viewServiceTouchBarControllerIdentifier:].cold.2
+ +[NSTouchBar(ViewBridge) touchBarForIdentifier:].cold.1
+ +[NSTouchBarItem(ViewBridge) touchBarItemForIdentifier:].cold.1
+ +[NSTouchBarItemOverlay(ViewBridge) overlayForIdentifier:].cold.1
+ +[NSVBKeyboardEventSpecification event:matchesAnySpecification:].cold.1
+ +[NSVBKeyboardEventSpecification event:matchesAnySpecification:].cold.2
+ +[NSVBKeyboardEventSpecification event:matchesAnySpecification:].cold.3
+ +[NSVBNamedFault _invokeIfShouldFault:format:arguments:block:].cold.1
+ +[NSVBNamedFault _invokeIfShouldFault:format:arguments:block:].cold.2
+ +[NSVBNamedFault _invokeIfShouldFault:format:arguments:block:].cold.3
+ +[NSVBNamedFault fault:withProbability:wasTaken:].cold.1
+ +[NSVBNamedFault idle:ifShouldFault:].cold.1
+ +[NSVBNamedFault idle:ifShouldFault:].cold.2
+ +[NSVBNamedFault shouldFault:].cold.1
+ +[NSVBNamedFault sleep:ifShouldFault:].cold.1
+ +[NSVBNamedFault sleep:ifShouldFault:].cold.2
+ +[NSVBObjectDeallocationCanary _logDeallocation:withCallStackSymbols:].cold.1
+ +[NSVBObjectDeallocationCanary attachCanaryToObject:].cold.1
+ +[NSVB_AnimationFencingSupport _animateWithAttributes:animations:].cold.1
+ +[NSVB_AnimationFencingSupport _animateWithAttributes:animations:].cold.2
+ +[NSVB_AnimationFencingSupport _animateWithAttributes:animations:].cold.3
+ +[NSVB_AnimationFencingSupport _currentAnimationAttributes:].cold.1
+ +[NSVB_AnimationFencingSupport _currentAnimationAttributes:].cold.2
+ +[NSVB_AnimationFencingSupport _currentAnimationAttributes:].cold.3
+ +[NSVB_QueueingProxy proxyWithTarget:connectionClient:shouldSuspendInvocationBlock:].cold.1
+ +[NSVB_ViewServiceBehaviorProxy proxyWrappingExportedObject:forCommunicationAtScope:withServiceMarshal:exportedProtocol:].cold.1
+ +[NSVB_ViewServiceImplicitAnimationDecodingProxy proxyDecodingAnimationsForTarget:withServiceMarshal:].cold.1
+ +[NSVB_ViewServiceImplicitAnimationDecodingProxy proxyDecodingAnimationsForTarget:withServiceMarshal:].cold.2
+ +[NSVB_ViewServiceImplicitAnimationEncodingProxy proxyEncodingAnimationsForTarget:controlMessageTarget:animationAttributes:sentAnimationAttributes:].cold.1
+ +[NSVB_ViewServiceXPCMachSendRight wrapSendRight:].cold.1
+ +[NSViewServiceApplication addHostPID:].cold.1
+ +[NSViewServiceApplication addHostPID:].cold.2
+ +[NSViewServiceApplication allocWithZone:].cold.1
+ +[NSViewServiceApplication bootstrapKind].cold.1
+ +[NSViewServiceApplication bootstrapSharedServiceListener].cold.1
+ +[NSViewServiceApplication bootstrapSharedServiceListener].cold.2
+ +[NSViewServiceApplication bootstrapSharedServiceListener].cold.3
+ +[NSViewServiceApplication bootstrapSharedServiceListener].cold.4
+ +[NSViewServiceApplication bundleForClass].cold.1
+ +[NSViewServiceApplication cacheFakeEvent:].cold.1
+ +[NSViewServiceApplication cacheMainBundleAsServiceBundle].cold.1
+ +[NSViewServiceApplication doctorServiceBundleInfoDictionary:].cold.1
+ +[NSViewServiceApplication doctorServiceBundleInfoDictionary:].cold.2
+ +[NSViewServiceApplication doctorServiceBundleInfoDictionary:].cold.3
+ +[NSViewServiceApplication doctorServiceBundleInfoDictionary:].cold.4
+ +[NSViewServiceApplication ensureNSApp].cold.1
+ +[NSViewServiceApplication ensureNSApp].cold.2
+ +[NSViewServiceApplication firstHostPID].cold.1
+ +[NSViewServiceApplication hasBootstrapKind:].cold.1
+ +[NSViewServiceApplication hasBootstrapKind:].cold.2
+ +[NSViewServiceApplication isFakeEvent:].cold.1
+ +[NSViewServiceApplication mungeStandardUserDefaults].cold.1
+ +[NSViewServiceApplication mungeStandardUserDefaults].cold.2
+ +[NSViewServiceApplication mungeStandardUserDefaults].cold.3
+ +[NSViewServiceApplication mungeStandardUserDefaults].cold.4
+ +[NSViewServiceApplication mungeStandardUserDefaults].cold.5
+ +[NSViewServiceApplication mungeStandardUserDefaults].cold.6
+ +[NSViewServiceApplication mungeStandardUserDefaults].cold.7
+ +[NSViewServiceApplication requiresFixedHost].cold.1
+ +[NSViewServiceApplication validateXpcBundleInfoDictionary:].cold.1
+ +[NSViewServiceApplication validateXpcBundleInfoDictionary:].cold.2
+ +[NSViewServiceApplication validateXpcBundleInfoDictionary:].cold.3
+ +[NSViewServiceApplication validateXpcBundleInfoDictionary:].cold.4
+ +[NSViewServiceApplication validateXpcBundleInfoDictionary:].cold.5
+ +[NSViewServiceApplication validateXpcBundleInfoDictionary:].cold.6
+ +[NSViewServiceApplication(Extension) bootstrapForExtensionKitWithDelegate:error:].cold.1
+ +[NSViewServiceApplication(Extension) commonBootstrapForExtensionWithError:].cold.1
+ +[NSViewServiceMarshal beginFreeWindowRendezvous:].cold.1
+ +[NSViewServiceMarshal beginFreeWindowRendezvous:].cold.2
+ +[NSViewServiceMarshal beginFreeWindowRendezvous:].cold.3
+ +[NSViewServiceMarshal beginFreeWindowRendezvous:].cold.4
+ +[NSViewServiceMarshal considerWindowForRendezvous:].cold.1
+ +[NSViewServiceMarshal considerWindowForRendezvous:].cold.2
+ +[NSViewServiceMarshal hostApp].cold.1
+ +[NSViewServiceMarshal hostApp].cold.2
+ +[NSViewServiceMarshal informHostsOfConnectionToService:].cold.1
+ +[NSViewServiceMarshal logIfFirstRepsonderOf:isNot:].cold.1
+ +[NSViewServiceMarshal logIfFirstRepsonderOf:isNot:].cold.2
+ +[NSViewServiceMarshal patchNSCursor].cold.1
+ +[NSViewServiceMarshal patchNSMenu].cold.1
+ +[NSViewServiceMarshal patchNSView].cold.1
+ +[NSViewServiceMarshal patchNSWindow].cold.1
+ +[NSViewServiceMarshal patchNSWindow].cold.2
+ +[NSViewServiceMarshal requestUserInteractionWithPatience:options:sender:].cold.1
+ +[NSViewServiceMarshal serviceMarshalForHostWindow:].cold.1
+ +[NSViewServiceMarshal serviceMarshals].cold.1
+ +[NSViewServiceMarshal serviceWindowWouldActivate:].cold.1
+ +[NSViewServiceMarshal viewBridgeAuxiliaryProxyForConnection:withErrorHandler:].cold.1
+ +[NSViewServiceMarshal viewBridgeAuxiliaryProxyForConnection:withErrorHandler:].cold.2
+ +[NSViewServiceMarshal whenWindow:isAssociatedWithRemoteViewPerform:].cold.1
+ +[NSViewServiceMarshal whenWindow:isAssociatedWithRemoteViewPerform:].cold.2
+ +[NSViewServiceMarshal windowDidOrderOnScreenAndFinishAnimating:].cold.1
+ +[NSViewServiceMarshal windowWillOrderOnScreen:].cold.1
+ +[NSViewService_PKSubsystem _initForPlugInKit].cold.1
+ +[NSWindow(PreviewAllocator) subClassWindowClass:].cold.1
+ +[NSWindow(PreviewAllocator) subClassWindowClass:].cold.2
+ +[NSWindow(PreviewAllocator) subClassWindowClass:].cold.3
+ +[NSWindow(PreviewAllocator) swizzledAllocWithZone:].cold.1
+ +[NSWindow(PreviewAllocator) swizzledAllocWithZone:].cold.2
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.1
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.10
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.11
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.2
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.3
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.4
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.5
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.6
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.7
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.8
+ +[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:].cold.9
+ +[NSXPCSharedListener cacheFutureEndpointsForServiceNamed:].cold.1
+ +[NSXPCSharedListener connectToService:instanceIdentifier:listener:queue:completion:].cold.1
+ +[NSXPCSharedListener connectionForListenerNamed:fromServiceNamed:instanceIdentifier:].cold.1
+ +[NSXPCSharedListener connectionForListenerNamed:fromServiceNamed:instanceIdentifier:].cold.2
+ +[NSXPCSharedListener connectionForListenerNamed:fromServiceNamed:instanceIdentifier:].cold.3
+ +[NSXPCSharedListener connectionForListenerNamed:fromServiceNamed:instanceIdentifier:].cold.4
+ +[NSXPCSharedListener endpointForReply:withListenerName:replyErrorCode:].cold.1
+ +[NSXPCSharedListener getSDKVersionOfServiceNamed:reply:].cold.1
+ +[NSXPCSharedListener listenerEndpointForService:instanceIdentifier:listener:queue:completion:].cold.1
+ +[NSXPCSharedListener listenerEndpointForService:instanceIdentifier:listener:queue:completion:].cold.2
+ +[NSXPCSharedListener listenerEndpointForService:instanceIdentifier:listener:queue:completion:].cold.3
+ +[NSXPCSharedListener listenerEndpointForService:instanceIdentifier:listener:queue:completion:].cold.4
+ +[NSXPCSharedListener service:builtForPlatform:againstMinimumSDK:reply:].cold.1
+ +[UINSServiceViewController initialize].cold.1
+ +[ViewBridgeUtilities appearanceWithData:].cold.1
+ +[ViewBridgeUtilities appearanceWithData:].cold.2
+ +[ViewBridgeUtilities concreteColorWithColorFromCurrentAppearance:].cold.1
+ +[ViewBridgeUtilities concreteColorWithColorFromCurrentAppearance:].cold.2
+ +[ViewBridgeUtilities createIdentifier].cold.1
+ +[ViewBridgeUtilities createIdentifier].cold.2
+ +[ViewBridgeUtilities dataWithAppearance:].cold.1
+ +[ViewBridgeUtilities dataWithAppearance:].cold.2
+ +[ViewBridgeUtilities decodeIdentifier:].cold.1
+ +[ViewBridgeUtilities decodeIdentifier:].cold.2
+ +[ViewBridgeUtilities decodeIdentifier:].cold.3
+ +[ViewBridgeUtilities describeAuditToken:].cold.1
+ +[ViewBridgeUtilities describeEventMask:].cold.1
+ +[ViewBridgeUtilities hostAppClientParametersClasses].cold.1
+ +[ViewBridgeUtilities hostAppIsActive:].cold.1
+ +[ViewBridgeUtilities informationStringForKey:forApplication:].cold.1
+ +[ViewBridgeUtilities informationStringForKey:forApplication:].cold.2
+ +[ViewBridgeUtilities informationStringForKey:forProcess:].cold.1
+ +[ViewBridgeUtilities minMaxFrameSizeFromConstraintsOfWindow:].cold.1
+ +[ViewBridgeUtilities pushAbortModalSessionEvent].cold.1
+ +[ViewBridgeUtilities removeResponder:fromChainOf:].cold.1
+ +[ViewBridgeUtilities removeResponder:fromChainOf:].cold.2
+ +[ViewBridgeUtilities setApplication:value:forKey:].cold.1
+ +[ViewBridgeUtilities setCurrentApplicationValue:forKey:].cold.1
+ +[ViewBridgeUtilities withThreadName:performActions:].cold.1
+ +[ViewBridgeUtilities withThreadName:performActions:].cold.2
+ +[ViewBridgeUtilities withThreadName:performActions:].cold.3
+ +[ViewBridgeUtilities withThreadName:performActions:].cold.4
+ +[ViewBridgeUtilities withThreadName:performActions:].cold.5
+ +[ViewHost ultimateAncestorOfWindow:inDictionaryOfHostsAndServices:consideringEachViewHost:].cold.1
+ +[ViewHost ultimateAncestorOfWindow:inDictionaryOfHostsAndServices:consideringEachViewHost:].cold.2
+ -[CalledByClient forApp:retrievePreviewEndpoint:].cold.1
+ -[CalledByClient forApp:retrievePreviewEndpoint:].cold.2
+ -[CalledByClient hostAppConnectionForListenerEndpoint:].cold.1
+ -[CalledByClient hostAppConnectionForListenerEndpoint:].cold.2
+ -[ControlListenerDelegate listener:shouldAcceptNewConnection:].cold.1
+ -[ControlListenerDelegate listener:shouldAcceptNewConnection:].cold.2
+ -[ControlListenerDelegate listener:shouldAcceptNewConnection:].cold.3
+ -[FenceGroup fenceGroupID].cold.1
+ -[FenceGroup init].cold.1
+ -[FenceGroupListenerDelegate listener:shouldAcceptNewConnection:].cold.1
+ -[FenceGroupListenerDelegate listener:shouldAcceptNewConnection:].cold.2
+ -[FenceGroupMember acquireActiveRole:completion:].cold.2
+ -[FenceGroupMember acquireActiveRole:completion:].cold.3
+ -[FenceGroupMember create:].cold.1
+ -[FenceGroupMember create:].cold.2
+ -[FenceGroupMember join:completion:].cold.1
+ -[HostAndService dealloc].cold.1
+ -[HostAndService event:isCloseEnoughTo:].cold.1
+ -[HostAndService event:isCloseEnoughTo:].cold.2
+ -[HostAndService stealKeyFocus:wantsAggressiveKeyboardFocusTheftCancellation:].cold.1
+ -[HostAndService stealKeyFocus:wantsAggressiveKeyboardFocusTheftCancellation:].cold.2
+ -[HostAndService stealKeyFocus:wantsAggressiveKeyboardFocusTheftCancellation:].cold.3
+ -[HostListenerDelegate listener:shouldAcceptNewConnection:].cold.1
+ -[HostListenerDelegate listener:shouldAcceptNewConnection:].cold.2
+ -[HostListenerDelegate listener:shouldAcceptNewConnection:].cold.3
+ -[HostOrService applicationSerialNumber].cold.1
+ -[HostOrService forEvent:invokeWithFlatEvent:].cold.1
+ -[HostOrService initWithConnection:].cold.1
+ -[HostOrService initWithConnection:].cold.2
+ -[HostOrService joinPair:reply:configure:].cold.1
+ -[HostOrService owningProcess:forWindow:].cold.1
+ -[HostOrService owningProcess:forWindow:].cold.2
+ -[ListenerDelegate listener:shouldAcceptNewConnection:].cold.1
+ -[ListenerDelegate listener:shouldAcceptNewConnection:].cold.2
+ -[ListenerDelegate listener:shouldAcceptNewConnection:].cold.3
+ -[ListenerDelegate listener:shouldAcceptNewConnection:].cold.4
+ -[NSAccessoryViewWindow _orderedDrawerAndWindowKeyLoopGroupingViews].cold.1
+ -[NSAccessoryViewWindow _orderedDrawerAndWindowKeyLoopGroupingViews].cold.2
+ -[NSAccessoryViewWindow forwardingTargetForSelector:].cold.1
+ -[NSAccessoryViewWindow updateAccessoryViewAccessibility].cold.1
+ -[NSAccessoryViewWindow updateAccessoryViewAccessibility].cold.2
+ -[NSCFRunLoopObserver dealloc].cold.1
+ -[NSCFRunLoopObserver dealloc].cold.2
+ -[NSCFRunLoopObserver dealloc].cold.3
+ -[NSCFRunLoopObserver dealloc].cold.4
+ -[NSCFRunLoopObserver initWithActivities:].cold.1
+ -[NSCFRunLoopObserver observeMode:withBlock:].cold.1
+ -[NSCFRunLoopObserver observeMode:withBlock:].cold.2
+ -[NSCFRunLoopObserver observeMode:withBlock:].cold.3
+ -[NSCFRunLoopSemaphore initWithMode:].cold.1
+ -[NSCFRunLoopSemaphore signal].cold.1
+ -[NSCFRunLoopSemaphore wait:].cold.1
+ -[NSCFRunLoopSemaphore wait].cold.1
+ -[NSChildWindowQueueElement initWithIdentifier:parameters:listenerEndpoint:reply:].cold.1
+ -[NSChildWindowQueueElement initWithIdentifier:parameters:listenerEndpoint:reply:].cold.2
+ -[NSChildWindowQueueElement initWithIdentifier:parameters:listenerEndpoint:reply:].cold.3
+ -[NSChildWindowQueueElement initWithIdentifier:parameters:listenerEndpoint:reply:].cold.4
+ -[NSCustomTouchBarItemForRemoteView dealloc].cold.1
+ -[NSDeferredSheet initWithChildIdentifier:parentIdentifier:windowBase:size:isCritical:listenerEndpoint:withReply:].cold.1
+ -[NSEventLoopSemaphore invokeLoopInModeForDuration:withBlock:].cold.1
+ -[NSEventQueue dequeueTimestamp:].cold.1
+ -[NSEventQueue dequeueTimestamp:].cold.2
+ -[NSEventQueue dequeueTimestamp:].cold.3
+ -[NSEventQueue enqueue:].cold.1
+ -[NSEventQueue initWithCapacity:].cold.1
+ -[NSEventQueue initWithCapacity:].cold.2
+ -[NSEventQueue initWithCapacity:].cold.3
+ -[NSEventQueue init].cold.1
+ -[NSEventQueue nextEventEqualToEvent:dequeue:].cold.1
+ -[NSEventQueue nextEventEqualToEvent:dequeue:].cold.2
+ -[NSFakeServiceResponder forwardInvocation:].cold.1
+ -[NSFakeServiceResponder forwardInvocation:].cold.2
+ -[NSFakeServiceResponder initWithView:action:validateMenuItem:validateUserInterfaceItem:targetIdentifier:].cold.1
+ -[NSGroupTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.1
+ -[NSGroupTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.2
+ -[NSGroupTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.3
+ -[NSGroupTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.4
+ -[NSGroupTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.5
+ -[NSGroupTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.6
+ -[NSObtainingEndpointState addError:description:forListenerNamed:fromServiceNamed:].cold.1
+ -[NSObtainingEndpointState addError:description:forListenerNamed:fromServiceNamed:].cold.2
+ -[NSObtainingEndpointState addError:description:forListenerNamed:fromServiceNamed:].cold.3
+ -[NSPanelForServiceViewControllerForTouchBarItem initWithContentRect:styleMask:backing:defer:].cold.1
+ -[NSPreviewHostView previewHostViewController].cold.1
+ -[NSPreviewHostViewController handleKeyEquivalent:eventOwner:reply:].cold.1
+ -[NSPreviewHostViewController isValid].cold.1
+ -[NSPreviewHostViewController loadView].cold.1
+ -[NSPreviewHostViewController observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[NSPreviewHostViewController observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[NSPreviewHostViewController observeValueForKeyPath:ofObject:change:context:].cold.3
+ -[NSPreviewHostViewController observeValueForKeyPath:ofObject:change:context:].cold.4
+ -[NSPreviewHostViewController requestConnectionToTargetApp:completionHandler:].cold.1
+ -[NSPreviewHostViewController requestConnectionToTargetApp:completionHandler:].cold.2
+ -[NSPreviewHostViewController requestFrame:reply:].cold.1
+ -[NSPreviewHostViewController setCursor:].cold.1
+ -[NSPreviewHostViewController setEventMask:].cold.1
+ -[NSPreviewHostViewController setView:].cold.1
+ -[NSPreviewHostViewController targetControllerProxyWithErrorHandler:].cold.1
+ -[NSPreviewHostViewController targetWindowStateChanged:].cold.1
+ -[NSPreviewHostViewController view:didMoveToWindow:].cold.1
+ -[NSPreviewHostViewController view:willMoveToWindow:].cold.1
+ -[NSPreviewTargetController _maintainLevelOfWindow:].cold.1
+ -[NSPreviewTargetController _realizeRequestedStateOfWindow:].cold.1
+ -[NSPreviewTargetController _realizeRequestedStateOfWindow:].cold.2
+ -[NSPreviewTargetController _realizeRequestedStateOfWindow:].cold.3
+ -[NSPreviewTargetController _realizeRequestedStateOfWindow:].cold.4
+ -[NSPreviewTargetController _realizeRequestedStateOfWindow:].cold.5
+ -[NSPreviewTargetController _realizeRequestedWindow:stateWithIdentifier:].cold.1
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.1
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.10
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.11
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.12
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.13
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.2
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.3
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.4
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.5
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.6
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.7
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.8
+ -[NSPreviewTargetController bootstrap:hostAppClientParameters:hostControllerProxy:brp:].cold.9
+ -[NSPreviewTargetController dealloc].cold.1
+ -[NSPreviewTargetController guaranteeSignal:after:].cold.1
+ -[NSPreviewTargetController handleKeyEquivalent:].cold.1
+ -[NSPreviewTargetController hostAppConnection:].cold.1
+ -[NSPreviewTargetController hostControllerProxyWithErrorHandler:].cold.1
+ -[NSPreviewTargetController isValid].cold.1
+ -[NSPreviewTargetController stealKeyboardFocus].cold.1
+ -[NSPreviewTargetController stealKeyboardFocus].cold.2
+ -[NSPreviewTargetController stealKeyboardFocus].cold.3
+ -[NSPreviewTargetWindow addChildWindow:ordered:].cold.2
+ -[NSPreviewTargetWindow downgradeFromLogicalKeyToAppearance].cold.1
+ -[NSPreviewTargetWindow downgradeFromLogicalKeyToAppearance].cold.2
+ -[NSPreviewTargetWindow orderWindow:relativeTo:].cold.1
+ -[NSPreviewTargetWindow removeChildWindow:].cold.1
+ -[NSPreviewTargetWindow removeChildWindow:].cold.2
+ -[NSPreviewTargetWindow superSetFrameCommon:display:stashSize:aux:force:].cold.1
+ -[NSRemoteView _accessibilityChildren:].cold.1
+ -[NSRemoteView _accessibilityParentToken:].cold.1
+ -[NSRemoteView _addPotentialKeyFocusThief:].cold.1
+ -[NSRemoteView _adjustToServiceWindowStyleMask].cold.1
+ -[NSRemoteView _adjustWindowBackgroundColor:].cold.1
+ -[NSRemoteView _advanceToConfigPhase:].cold.1
+ -[NSRemoteView _advanceToConfigPhase:].cold.2
+ -[NSRemoteView _advanceToConfigPhaseLegacy].cold.1
+ -[NSRemoteView _advanceToRunPhase:].cold.1
+ -[NSRemoteView _associateMouseAndMouseCursorPosition:].cold.1
+ -[NSRemoteView _associate].cold.1
+ -[NSRemoteView _associate].cold.2
+ -[NSRemoteView _associate].cold.3
+ -[NSRemoteView _awaitInvalidation].cold.1
+ -[NSRemoteView _beginAppModalSession:parameters:listenerEndpoint:completion:].cold.1
+ -[NSRemoteView _beginAppModalSession:parameters:listenerEndpoint:completion:].cold.2
+ -[NSRemoteView _beginSheet:modalForWindow:windowBase:size:isCritical:listenerEndpoint:withReply:].cold.1
+ -[NSRemoteView _beginSheet:windowBase:modalForWindow:size:isCritical:listenerEndpoint:completion:].cold.1
+ -[NSRemoteView _bridge].cold.1
+ -[NSRemoteView _bridge].cold.2
+ -[NSRemoteView _bridge].cold.3
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.1
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.10
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.11
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.12
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.2
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.3
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.4
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.5
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.6
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.7
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.8
+ -[NSRemoteView _configureAndRetainServiceMarshalConnection:].cold.9
+ -[NSRemoteView _copyViewServiceMarshalReply:withClientExportedObjectWithClientInterface:withClientExportedObjectWithAnimationSyncInterface:].cold.1
+ -[NSRemoteView _copyViewServiceMarshalReply:withClientExportedObjectWithClientInterface:withClientExportedObjectWithAnimationSyncInterface:].cold.2
+ -[NSRemoteView _disassociate].cold.1
+ -[NSRemoteView _disengageFromAllWindows].cold.1
+ -[NSRemoteView _effectiveAppearanceAsData].cold.1
+ -[NSRemoteView _effectiveAppearanceAsData].cold.2
+ -[NSRemoteView _elementsForTokens:].cold.1
+ -[NSRemoteView _elementsForTokens:].cold.2
+ -[NSRemoteView _elementsForTokens:].cold.3
+ -[NSRemoteView _endFence].cold.1
+ -[NSRemoteView _endFence].cold.2
+ -[NSRemoteView _endTrackingLoop:reply:].cold.1
+ -[NSRemoteView _ensureBridgeObserversForRendezvousWindow].cold.1
+ -[NSRemoteView _ensureBridgeObserversForRendezvousWindow].cold.2
+ -[NSRemoteView _ensureClientExportedInterface].cold.1
+ -[NSRemoteView _ensureClientExportedObject].cold.1
+ -[NSRemoteView _ensureViewServiceIsResponsive].cold.1
+ -[NSRemoteView _filterStyleMask:forWindowBase:].cold.1
+ -[NSRemoteView _frameOfServiceWindowDidChange:windowBackgroundColor:reply:].cold.1
+ -[NSRemoteView _hostWindowLevelDidChange:].cold.1
+ -[NSRemoteView _invalidateWithError:].cold.1
+ -[NSRemoteView _invalidateWithError:].cold.2
+ -[NSRemoteView _postSuperInit].cold.1
+ -[NSRemoteView _preSuperInit].cold.1
+ -[NSRemoteView _preSuperInit].cold.2
+ -[NSRemoteView _regionForOpaqueDescendants:forMove:forUnderTitlebar:].cold.1
+ -[NSRemoteView _regionForOpaqueDescendants:forMove:forUnderTitlebar:].cold.2
+ -[NSRemoteView _remoteViewBecameFirstResponder:withIPC:].cold.1
+ -[NSRemoteView _remoteViewBecameFirstResponder:withIPC:].cold.2
+ -[NSRemoteView _sendWindowFakeClick:why:].cold.1
+ -[NSRemoteView _sendWindowFakeClick:why:].cold.2
+ -[NSRemoteView _serviceProcessIdentifier].cold.1
+ -[NSRemoteView _serviceRequestsFrame:serviceWindowBackgroundColor:animate:async:transaction:completion:].cold.1
+ -[NSRemoteView _serviceValidatesAction:menuItem:userInterfaceItem:targetIdentifier:sender:].cold.1
+ -[NSRemoteView _serviceValidatesAction:menuItem:userInterfaceItem:targetIdentifier:sender:].cold.2
+ -[NSRemoteView _serviceValidatesAction:menuItem:userInterfaceItem:targetIdentifier:sender:].cold.3
+ -[NSRemoteView _serviceWindowHasDragRegion:].cold.1
+ -[NSRemoteView _serviceWindowReceivedScrollWheel:eventOwner:].cold.1
+ -[NSRemoteView _serviceWindowReceivedScrollWheel:eventOwner:].cold.2
+ -[NSRemoteView _setCursor:].cold.1
+ -[NSRemoteView _shouldAdjustToServiceStyleMask].cold.1
+ -[NSRemoteView _shouldImposeVibrancySupport:].cold.1
+ -[NSRemoteView _shouldImposeVibrancySupport:].cold.2
+ -[NSRemoteView _snapshot:].cold.1
+ -[NSRemoteView _updateAccessibilityConnection:legend:withReply:].cold.1
+ -[NSRemoteView _viewServiceMarshalProxy:withErrorHandler:].cold.1
+ -[NSRemoteView _viewServiceMarshalProxy:withErrorHandler:].cold.2
+ -[NSRemoteView _waitOnSemaphore:withPatience:].cold.1
+ -[NSRemoteView _withoutCatchSupplementalTargetForAction:sender:].cold.1
+ -[NSRemoteView _withoutCatchSupplementalTargetForAction:sender:].cold.2
+ -[NSRemoteView advanceToRunPhaseIfNeeded].cold.1
+ -[NSRemoteView auxiliaryListenerEndpointForProtocol:].cold.1
+ -[NSRemoteView auxiliaryListenerEndpointForProtocol:].cold.2
+ -[NSRemoteView beginAppModalSessionForWindow].cold.1
+ -[NSRemoteView beginAppModalSessionForWindow].cold.2
+ -[NSRemoteView beginAppModalSessionForWindow].cold.3
+ -[NSRemoteView beginAppModalSessionForWindow].cold.4
+ -[NSRemoteView cacheDisplayInRect:toBitmapImageRep:].cold.1
+ -[NSRemoteView enqueueChildWindow:parameters:listenerEndpoint:reply:].cold.1
+ -[NSRemoteView ensureDeferredSheets].cold.1
+ -[NSRemoteView forwardKeyboardEvent:withSemaphore:].cold.1
+ -[NSRemoteView invalidate].cold.1
+ -[NSRemoteView maintainAppWideNotifications:].cold.1
+ -[NSRemoteView maintainAppWideNotifications:].cold.2
+ -[NSRemoteView maintainContainingWindowNotifications:].cold.1
+ -[NSRemoteView maintainContainingWindowNotifications:].cold.2
+ -[NSRemoteView maintainContainingWindowNotifications:].cold.3
+ -[NSRemoteView maintainKeyTestWindowNotifications:].cold.1
+ -[NSRemoteView maintainKeyTestWindowNotifications:].cold.2
+ -[NSRemoteView maintainKeyTestWindowNotifications:].cold.3
+ -[NSRemoteView maintainProcessNotificationEventMonitor:].cold.1
+ -[NSRemoteView maintainProcessNotificationEventMonitor:].cold.2
+ -[NSRemoteView maintainScrollViewSeparatorTrackingAdapterForWindow:].cold.1
+ -[NSRemoteView maintainScrollViewSeparatorTrackingAdapterForWindow:].cold.2
+ -[NSRemoteView maintainWindowEventMonitor:].cold.1
+ -[NSRemoteView remoteViewControllerParametersForService].cold.1
+ -[NSRemoteView retreatToConfigPhase].cold.1
+ -[NSRemoteView serviceViewControllerProxy:].cold.1
+ -[NSRemoteView serviceViewControllerProxyWithErrorHandler:].cold.1
+ -[NSRemoteView serviceViewControllerProxyWithErrorHandler:].cold.2
+ -[NSRemoteView serviceViewSize].cold.1
+ -[NSRemoteView setDelegate:].cold.1
+ -[NSRemoteView setExtensionIdentifier:].cold.1
+ -[NSRemoteView setExtensionIdentifier:].cold.2
+ -[NSRemoteView setRemoteAccessibilityChildrenTokens:].cold.1
+ -[NSRemoteView setRemoteViewControllerParametersForService:].cold.1
+ -[NSRemoteView setRemoteViewControllerParametersForService:].cold.2
+ -[NSRemoteView setRendezvousWindowIdentifier:].cold.1
+ -[NSRemoteView setRendezvousWindowIdentifier:].cold.2
+ -[NSRemoteView setRendezvousWindowIdentifier:].cold.3
+ -[NSRemoteView setRendezvousWindowIdentifier:].cold.4
+ -[NSRemoteView setServiceListenerEndpoint:].cold.1
+ -[NSRemoteView setServiceListenerEndpoint:].cold.2
+ -[NSRemoteView setServiceName:].cold.1
+ -[NSRemoteView setServiceName:].cold.2
+ -[NSRemoteView setServiceName:].cold.3
+ -[NSRemoteView setServiceObject:forKey:].cold.1
+ -[NSRemoteView setServiceSubclassName:].cold.1
+ -[NSRemoteView setServiceSubclassName:].cold.2
+ -[NSRemoteView setTrustsServiceKeyEvents:].cold.1
+ -[NSRemoteView setTrustsServiceKeyEvents:].cold.2
+ -[NSRemoteView setTrustsServiceKeyEvents:].cold.3
+ -[NSRemoteView sheetCompleted:].cold.1
+ -[NSRemoteView sheetCompleted:].cold.2
+ -[NSRemoteView stolenKeyFocusEventFilter:].cold.1
+ -[NSRemoteView synchronizeAnimationsInActions:].cold.1
+ -[NSRemoteView synchronizeAnimationsInActions:].cold.2
+ -[NSRemoteView synchronizeAnimationsInActions:].cold.3
+ -[NSRemoteView wrapProxyForAnimationFencing:withAnimationAttributesFor:].cold.1
+ -[NSRemoteView wrapProxyForAnimationFencing:withAnimationAttributesFor:].cold.2
+ -[NSRemoteView wrapProxyForAnimationFencing:withAnimationAttributesFor:].cold.3
+ -[NSRemoteView(AccessoryView) serviceAccessoryViewFrameChanged:].cold.1
+ -[NSRemoteView(AccessoryView) setAccessoryView:].cold.1
+ -[NSRemoteView(AccessoryView) setAccessoryView:].cold.2
+ -[NSRemoteView(AccessoryView) setAccessoryView:].cold.3
+ -[NSRemoteView(NSTouchBarInternal) _assertObjectsOf:areKindOfClass:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _assertObjectsOf:areKindOfClass:].cold.2
+ -[NSRemoteView(NSTouchBarInternal) _configureTouchBar:perDescription:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _configureTouchBar:perDescription:].cold.2
+ -[NSRemoteView(NSTouchBarInternal) _decodeBoolean:inDescription:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _hideTouchBarPopover:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _ifNecessaryReplaceTouchBar:escapeKeyReplacementItem:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _ifNecessaryReplaceTouchBars].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _ifNecessaryReplaceTouchBars].cold.2
+ -[NSRemoteView(NSTouchBarInternal) _ifNecessaryReplaceTouchBars].cold.3
+ -[NSRemoteView(NSTouchBarInternal) _ifNecessaryReplaceTouchBars].cold.4
+ -[NSRemoteView(NSTouchBarInternal) _ifNecessaryReplaceTouchBars].cold.5
+ -[NSRemoteView(NSTouchBarInternal) _mapPerProcessIdentifiers:of:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _mapPerProcessIdentifiers:of:].cold.2
+ -[NSRemoteView(NSTouchBarInternal) _mapPerProcessIdentifiers:of:].cold.3
+ -[NSRemoteView(NSTouchBarInternal) _serviceHasTouchBars:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _setTouchBar:description:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _setTouchBar:escapeKeyReplacementItem:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _setTouchBarItem:itemPosition:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _showTouchBarPopover:fromItem:withOverlayIdentifier:withCloseButton:withControlStrip:withOptions:].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _showTouchBarPopover:fromItem:withOverlayIdentifier:withCloseButton:withControlStrip:withOptions:].cold.2
+ -[NSRemoteView(NSTouchBarInternal) _showTouchBarPopover:fromItem:withOverlayIdentifier:withCloseButton:withControlStrip:withOptions:].cold.3
+ -[NSRemoteView(NSTouchBarInternal) _showTouchBarPopover:fromItem:withOverlayIdentifier:withCloseButton:withControlStrip:withOptions:].cold.4
+ -[NSRemoteView(NSTouchBarInternal) _showTouchBarPopover:fromItem:withOverlayIdentifier:withCloseButton:withControlStrip:withOptions:].cold.5
+ -[NSRemoteView(NSTouchBarInternal) _showTouchBarPopover:fromItem:withOverlayIdentifier:withCloseButton:withControlStrip:withOptions:].cold.6
+ -[NSRemoteView(NSTouchBarInternal) _showTouchBarPopover:fromItem:withOverlayIdentifier:withCloseButton:withControlStrip:withOptions:].cold.7
+ -[NSRemoteView(NSTouchBarInternal) _showTouchBarPopover:fromItem:withOverlayIdentifier:withCloseButton:withControlStrip:withOptions:].cold.8
+ -[NSRemoteView(NSTouchBarInternal) _touchBarsDescription].cold.1
+ -[NSRemoteView(NSTouchBarInternal) _touchBarsDescription].cold.2
+ -[NSRemoteView(NSTouchBarInternal) _touchBarsDescription].cold.3
+ -[NSRemoteViewController _postServiceViewReceivedLeftMouseDownNotification:].cold.1
+ -[NSRemoteViewController _postServiceViewReceivedLeftMouseDownNotification:].cold.2
+ -[NSRemoteViewController serviceAuditToken].cold.1
+ -[NSRemoteViewController serviceProcessIdentifier].cold.1
+ -[NSRemoteViewController serviceViewControllerProxyWithErrorHandler:].cold.1
+ -[NSRemoteViewController setServiceBundleIdentifier:].cold.1
+ -[NSRemoteViewController setServiceBundleIdentifier:].cold.2
+ -[NSRemoteViewController setServiceListenerEndpoint:].cold.1
+ -[NSRemoteViewController setServiceViewControllerClassName:].cold.1
+ -[NSRemoteViewController setServiceViewControllerClassName:].cold.2
+ -[NSRemoteViewController setView:].cold.1
+ -[NSRemoteViewController setView:].cold.2
+ -[NSRemoteViewController setView:].cold.3
+ -[NSRemoteViewController setView:].cold.4
+ -[NSRemoteViewController setView:].cold.5
+ -[NSRemoteViewController setView:].cold.6
+ -[NSRemoteViewController setView:].cold.7
+ -[NSRemoteViewControllerAuxiliary _viewWithoutLoad].cold.1
+ -[NSRemoteViewControllerAuxiliary dealloc].cold.1
+ -[NSRemoteViewControllerAuxiliary view:encounteredError:].cold.1
+ -[NSRemoteViewControllerAuxiliary view:encounteredError:].cold.2
+ -[NSRemoteViewControllerAuxiliary view:encounteredError:].cold.3
+ -[NSRemoteViewControllerAuxiliary viewDidInvalidate:].cold.3
+ -[NSRemoteViewControllerAuxiliary viewDidInvalidate:].cold.4
+ -[NSRemoteViewControllerAuxiliary viewShouldDragOldestAncestorWindow:].cold.1
+ -[NSRemoteViewControllerForTouchBarItem boolForBridgeKey:].cold.1
+ -[NSRemoteViewControllerForTouchBarItem boolForBridgeKey:].cold.2
+ -[NSRemoteViewControllerForTouchBarItem boolForBridgeKey:].cold.3
+ -[NSRemoteViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[NSRemoteViewControllerForTouchBarItem observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[NSRemoteViewControllerForTouchBarItem sizeForBridgeKey:].cold.1
+ -[NSRemoteViewControllerForTouchBarItem sizeForBridgeKey:].cold.2
+ -[NSRemoteViewControllerForTouchBarItem sizeForBridgeKey:].cold.3
+ -[NSRemoteViewControllerParametersForService copyWithZone:].cold.1
+ -[NSRemoteViewControllerParametersForServiceBase initWithCoder:].cold.1
+ -[NSRemoteViewControllerParametersForServiceBase initWithCoder:].cold.2
+ -[NSRemoteViewControllerParametersForServiceBase initWithCoder:].cold.3
+ -[NSRemoteViewControllerParametersForServiceBase initWithCoder:].cold.4
+ -[NSRemoteViewControllerParametersForServiceBase initWithCoder:].cold.5
+ -[NSRemoteViewControllerParametersForServiceBase initWithCoder:].cold.6
+ -[NSRemoteViewHostAppListenerDelegate listener:shouldAcceptNewConnection:].cold.1
+ -[NSRemoteViewHostAppListenerDelegate listener:shouldAcceptNewConnection:].cold.2
+ -[NSRemoteViewHostAppListenerDelegate listener:shouldAcceptNewConnection:].cold.3
+ -[NSRemoteViewMarshal _topmostAppModalSessionHasRendezvousWindowIdentifier:].cold.1
+ -[NSRemoteViewMarshal _topmostAppModalSessionHasRendezvousWindowIdentifier:].cold.2
+ -[NSRemoteViewMarshal dealloc].cold.1
+ -[NSRemoteViewMarshal initWithView:].cold.1
+ -[NSRemoteViewMarshal matchBootstrapFrameOfWindow:].cold.1
+ -[NSRemoteViewMarshal matchBootstrapFrameOfWindow:].cold.2
+ -[NSRemoteViewMarshal matchBootstrapFrameOfWindow:].cold.3
+ -[NSRemoteViewMarshal registerBridgeKeys:].cold.3
+ -[NSRemoteViewMarshal window:isUltimatelySpawnedFrom:].cold.1
+ -[NSRemoteViewSemaphore initWithActivity:].cold.1
+ -[NSRemoteViewSemaphore initWithActivity:].cold.2
+ -[NSRendezvousChildWindowController invalidateWithError:].cold.1
+ -[NSRendezvousChildWindowDelegate initWithWindow:andParent:].cold.1
+ -[NSRendezvousChildWindowDelegate originRelevantToParent:].cold.1
+ -[NSRendezvousPopoverController popoverAccessibilityParent].cold.1
+ -[NSRendezvousPopoverDelegate _setValue:forKey:context:].cold.1
+ -[NSRendezvousSheetController invalidate].cold.1
+ -[NSRendezvousWindowController awakeFromRemoteView].cold.1
+ -[NSRendezvousWindowController awakeFromRemoteView].cold.2
+ -[NSRendezvousWindowController dealloc].cold.1
+ -[NSRendezvousWindowController initWithWindow:].cold.1
+ -[NSRendezvousWindowController initWithWindow:].cold.2
+ -[NSRendezvousWindowController invalidate].cold.1
+ -[NSRendezvousWindowController invalidate].cold.2
+ -[NSRendezvousWindowController invalidate].cold.3
+ -[NSRendezvousWindowController objectToObserveForKey:withWindow:].cold.1
+ -[NSRendezvousWindowController objectToObserveForKey:withWindow:].cold.2
+ -[NSRendezvousWindowController tokenForElement:].cold.1
+ -[NSRendezvousWindowRemoteViewDelegate _setAccessibilityElement:forKey:context:].cold.1
+ -[NSRendezvousWindowRemoteViewDelegate _setAccessibilityElement:forKey:context:].cold.2
+ -[NSRendezvousWindowRemoteViewDelegate disengageFromWindow].cold.1
+ -[NSRendezvousWindowRemoteViewDelegate initWithWindow:].cold.1
+ -[NSRendezvousWindowRemoteViewDelegate observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[NSRendezvousWindowRemoteViewDelegate observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[NSRendezvousWindowRemoteViewDelegate observeValueForKeyPath:ofObject:change:context:].cold.3
+ -[NSRendezvousWindowRemoteViewDelegate observeValueForKeyPath:ofObject:change:context:].cold.4
+ -[NSRendezvousWindowRemoteViewDelegate observeValueForKeyPath:ofObject:change:context:].cold.5
+ -[NSSelfDestructingRemoteViewDelegate viewDidInvalidate:].cold.1
+ -[NSSemiAutonomousRendezvousWindowController awakeFromRemoteView].cold.1
+ -[NSSemiAutonomousRendezvousWindowController awakeFromRemoteView].cold.2
+ -[NSServiceViewController _installViewIntoWindow:].cold.1
+ -[NSServiceViewController _requestFrame:async:hostShouldAnimate:animation:completion:].cold.1
+ -[NSServiceViewController _respondsToAction:forTarget:].cold.1
+ -[NSServiceViewController _respondsToAction:forTarget:].cold.2
+ -[NSServiceViewController _retainMarshal].cold.1
+ -[NSServiceViewController _validateTarget:forAction:].cold.1
+ -[NSServiceViewController _validateTarget:forAction:].cold.2
+ -[NSServiceViewController adjustLayout:animation:completion:].cold.1
+ -[NSServiceViewController adjustLayout:animation:completion:].cold.2
+ -[NSServiceViewController advanceToRunPhase].cold.1
+ -[NSServiceViewController awakeFromRemoteView].cold.1
+ -[NSServiceViewController bridge].cold.1
+ -[NSServiceViewController bridge].cold.2
+ -[NSServiceViewController childWindowDidInvalidate:dueToError:].cold.1
+ -[NSServiceViewController childWindowDidInvalidate:dueToError:].cold.2
+ -[NSServiceViewController description].cold.1
+ -[NSServiceViewController exportedObject].cold.1
+ -[NSServiceViewController hostWindowReceivedEventType:].cold.1
+ -[NSServiceViewController initWithNibName:bundle:].cold.1
+ -[NSServiceViewController initWithNibName:bundle:].cold.2
+ -[NSServiceViewController initWithWindow:].cold.1
+ -[NSServiceViewController invalid].cold.1
+ -[NSServiceViewController invalidate].cold.1
+ -[NSServiceViewController isValid].cold.1
+ -[NSServiceViewController loadView].cold.1
+ -[NSServiceViewController nibBundle].cold.1
+ -[NSServiceViewController nibName].cold.1
+ -[NSServiceViewController remoteViewControllerProxy:withProxyErrorHandler:].cold.1
+ -[NSServiceViewController remoteViewControllerProxyWithErrorHandler:].cold.1
+ -[NSServiceViewController remoteViewControllerProxyWithErrorHandler:].cold.2
+ -[NSServiceViewController remoteViewControllerProxyWithErrorHandler:].cold.3
+ -[NSServiceViewController remoteViewControllerProxyWithErrorHandler:].cold.4
+ -[NSServiceViewController remoteViewIdentifier].cold.1
+ -[NSServiceViewController remoteViewSizeChanged:transaction:].cold.1
+ -[NSServiceViewController requestFrame:animation:completion:].cold.1
+ -[NSServiceViewController requestFrame:animation:completion:].cold.2
+ -[NSServiceViewController requestResize:animation:completion:].cold.1
+ -[NSServiceViewController requestResize:animation:completion:].cold.2
+ -[NSServiceViewController retreatToConfigPhase].cold.1
+ -[NSServiceViewController scrollWheel:].cold.1
+ -[NSServiceViewController serviceViewControllerIdentifierCreating:].cold.1
+ -[NSServiceViewController serviceViewControllerIdentifierCreating:].cold.2
+ -[NSServiceViewController setRemoteViewSafeAreaInsets:].cold.1
+ -[NSServiceViewController setRemoteViewSafeAreaInsets:].cold.2
+ -[NSServiceViewController setView:].cold.1
+ -[NSServiceViewController setView:].cold.2
+ -[NSServiceViewController setView:].cold.3
+ -[NSServiceViewController sizeHint].cold.1
+ -[NSServiceViewController valid].cold.1
+ -[NSServiceViewController wantsForwardedScrollEventsForAxis:].cold.1
+ -[NSServiceViewController whileMouseIsDisassociatedFromMouseCursorPosition:].cold.1
+ -[NSServiceViewControllerForTouchBarItem awakeFromRemoteView].cold.1
+ -[NSServiceViewControllerForTouchBarItem awakeFromRemoteView].cold.2
+ -[NSServiceViewControllerForTouchBarItem awakeFromRemoteView].cold.3
+ -[NSServiceViewControllerForTouchBarItem awakeFromRemoteView].cold.4
+ -[NSServiceViewControllerForTouchBarItem awakeFromRemoteView].cold.5
+ -[NSServiceViewControllerForTouchBarItem awakeFromRemoteView].cold.6
+ -[NSServiceViewControllerForTouchBarItem awakeFromRemoteView].cold.7
+ -[NSServiceViewControllerForTouchBarItem informRemoteViewOfNewSizes].cold.1
+ -[NSServiceViewControllerForTouchBarItem informRemoteViewOfNewSizes].cold.2
+ -[NSServiceViewControllerForTouchBarItem informRemoteViewOfNewSizes].cold.3
+ -[NSServiceViewControllerForTouchBarItem initWithAppearance:].cold.1
+ -[NSServiceViewControllerForTouchBarItem initWithAppearance:].cold.2
+ -[NSServiceViewControllerForTouchBarItem initWithAppearance:].cold.3
+ -[NSServiceViewControllerForTouchBarItem loadView].cold.1
+ -[NSServiceViewControllerForTouchBarItem loadView].cold.2
+ -[NSServiceViewControllerForTouchBarItem loadView].cold.3
+ -[NSServiceViewControllerForTouchBarItem loadView].cold.4
+ -[NSServiceViewControllerForTouchBarItem loadView].cold.5
+ -[NSServiceViewControllerForTouchBarItem loadView].cold.6
+ -[NSServiceViewControllerForTouchBarItem loadView].cold.7
+ -[NSServiceViewControllerForTouchBarItem loadView].cold.8
+ -[NSServiceViewControllerForTouchBarItem prepareItemsOfBar:].cold.1
+ -[NSServiceViewControllerForTouchBarItem remoteViewSizeChanged:transaction:].cold.1
+ -[NSServiceViewControllerForTouchBarItem remoteViewSizeChanged:transaction:].cold.2
+ -[NSServiceViewControllerForTouchBarItem remoteViewSizeChanged:transaction:].cold.3
+ -[NSServiceViewControllerUnifyingProxy initWithClientProxy:andAnimationSyncProxy:withErrorHandler:].cold.1
+ -[NSServiceViewControllerUnifyingProxy initWithClientProxy:andAnimationSyncProxy:withErrorHandler:].cold.2
+ -[NSServiceViewControllerUnifyingProxy initWithClientProxy:andAnimationSyncProxy:withErrorHandler:].cold.3
+ -[NSServiceViewControllerUnifyingProxy initWithClientProxy:andAnimationSyncProxy:withErrorHandler:].cold.4
+ -[NSServiceViewControllerUnifyingProxy initWithClientProxy:andAnimationSyncProxy:withErrorHandler:].cold.5
+ -[NSServiceViewControllerWindow initWithContentRect:withViewController:].cold.1
+ -[NSSpaceTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.1
+ -[NSSpaceTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.2
+ -[NSSpaceTouchBarItemForRemoteView initWithIdentifier:andDescription:].cold.1
+ -[NSSpaceTouchBarItemForRemoteView initWithIdentifier:andDescription:].cold.2
+ -[NSTouchBar(ViewBridge) _annotateWithDescriptionOfProvider:].cold.1
+ -[NSTouchBar(ViewBridge) _annotateWithDescriptionOfProvider:].cold.2
+ -[NSTouchBar(ViewBridge) viewServiceTouchBarControllerDescription].cold.1
+ -[NSTouchBar(ViewBridge) viewServiceTouchBarControllerDescription].cold.2
+ -[NSTouchBar(ViewBridge) viewServiceTouchBarControllerDescription].cold.3
+ -[NSTouchBar(ViewBridge) viewServiceTouchBarControllerDescription].cold.4
+ -[NSTouchBar(ViewBridge) viewServiceTouchBarControllerDescription].cold.5
+ -[NSTouchBar(ViewBridge) viewServiceTouchBarControllerDescription].cold.6
+ -[NSTouchBarForRemoteView initWithServiceBarIdentifier:remoteView:].cold.1
+ -[NSTouchBarForRemoteView initWithServiceBarIdentifier:remoteView:].cold.2
+ -[NSTouchBarItem(ViewBridge) _hostHidPopoverBar:forItem:sender:].cold.1
+ -[NSTouchBarItem(ViewBridge) _hostShowedPopoverBar:forItem:sender:].cold.1
+ -[NSTouchBarItem(ViewBridge) _viewServiceTouchBarControllerIdentifier].cold.1
+ -[NSTouchBarItem(ViewBridge) _viewServiceTouchBarControllerIdentifier].cold.2
+ -[NSTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.1
+ -[NSTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.2
+ -[NSTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.3
+ -[NSTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.4
+ -[NSTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.5
+ -[NSTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.6
+ -[NSTouchBarItem(ViewBridge) viewServiceTouchBarControllerDescription].cold.7
+ -[NSTouchBarItemContainerView(ViewBridge) setFrameSize:].cold.1
+ -[NSTouchBarItemOverlayForRemoteView didChangePopoverBarState:].cold.1
+ -[NSTouchBarItemOverlayForRemoteView didChangePopoverBarState:].cold.2
+ -[NSTouchBarItemOverlayForRemoteView didChangePopoverBarState:].cold.3
+ -[NSVBAuditToken tokenAsData].cold.1
+ -[NSVBKeyboardEventSpecification encodeWithCoder:].cold.1
+ -[NSVBKeyboardEventSpecification initWithCharactersIgnoringModifiers:modifierFlags:modifierFlagsCriterion:].cold.1
+ -[NSVBKeyboardEventSpecification initWithCharactersIgnoringModifiers:modifierFlags:modifierFlagsCriterion:].cold.2
+ -[NSVBKeyboardEventSpecification initWithCharactersIgnoringModifiers:modifierFlags:modifierFlagsCriterion:].cold.3
+ -[NSVBKeyboardEventSpecification initWithCharactersIgnoringModifiers:modifierFlags:modifierFlagsCriterion:].cold.4
+ -[NSVBKeyboardEventSpecification initWithCoder:].cold.1
+ -[NSVBKeyboardEventSpecification initWithCoder:].cold.2
+ -[NSVBKeyboardEventSpecification initWithKeyCode:modifierFlags:modifierFlagsCriterion:].cold.1
+ -[NSVBKeyboardEventSpecification initWithKeyCode:modifierFlags:modifierFlagsCriterion:].cold.2
+ -[NSVBObjectDeallocationCanary _dealloc:].cold.1
+ -[NSVBObjectDeallocationCanary _initForObject:].cold.1
+ -[NSVBObjectDeallocationCanary _initForObject:].cold.2
+ -[NSVBObjectDeallocationCanary _logDeallocation:withCallStackSymbols:].cold.1
+ -[NSVB_QueueingProxy isValid].cold.1
+ -[NSVB_ViewAnimationAttributes initWithCoder:].cold.1
+ -[NSVB_ViewAnimationAttributes initWithCoder:].cold.2
+ -[NSVB_ViewAnimationAttributes initWithCoder:].cold.3
+ -[NSVB_ViewAnimationAttributes initWithCoder:].cold.4
+ -[NSVB_ViewServiceFencingController fencingControlProxy:didBeginFencingWithSendRight:].cold.1
+ -[NSVB_ViewServiceFencingController fencingControlProxy:didEndFencingWithSendRight:].cold.1
+ -[NSVB_ViewServiceFencingController forgetFencingMessagesForFencingControlProxy:].cold.1
+ -[NSVB_ViewServiceFencingController forgetFencingMessagesForFencingControlProxy:].cold.2
+ -[NSVB_ViewServiceImplicitAnimationDecodingProxy shouldApplyAnimationAttributes:].cold.1
+ -[NSView(NSServiceViewController) respondsToAction:fromTask:].cold.1
+ -[NSView(NSServiceViewController) respondsToAction:fromTask:].cold.2
+ -[NSViewBridge allKeys].cold.1
+ -[NSViewBridge hasKey:].cold.1
+ -[NSViewBridge hasObject:forKey:].cold.1
+ -[NSViewBridge hasObject:forKey:].cold.2
+ -[NSViewBridge hasObjectForKey:].cold.1
+ -[NSViewBridge keyIsRelevantToBuddy:].cold.1
+ -[NSViewBridge objectForKey:].cold.1
+ -[NSViewBridge objectForKey:].cold.2
+ -[NSViewBridge ownerForKey:].cold.1
+ -[NSViewBridge ownerForKey:].cold.2
+ -[NSViewBridge registerKey:defaultObject:owner:].cold.1
+ -[NSViewBridge registerKey:defaultObject:owner:].cold.2
+ -[NSViewBridge registerKey:defaultObject:owner:].cold.3
+ -[NSViewBridge setObject:forKey:withKVO:local:].cold.1
+ -[NSViewBridge setObject:forKey:withKVO:local:].cold.2
+ -[NSViewBridge setObject:forKey:withKVO:local:].cold.3
+ -[NSViewBridge setSnapshot:].cold.1
+ -[NSViewBridge setSnapshot:].cold.2
+ -[NSViewBridge setSnapshot:].cold.3
+ -[NSViewBridge setSnapshot:].cold.4
+ -[NSViewBridge setSnapshot:].cold.5
+ -[NSViewBridge setSnapshot:].cold.6
+ -[NSViewBridge setSnapshot:].cold.7
+ -[NSViewBridge setValue:forKey:].cold.1
+ -[NSViewBridge setValue:forKey:].cold.2
+ -[NSViewBridge snapshot].cold.1
+ -[NSViewBridge snapshot].cold.2
+ -[NSViewBridge snapshot].cold.3
+ -[NSViewBridge validClasses].cold.1
+ -[NSViewBridge valueForKey:].cold.1
+ -[NSViewBridge valueForKey:].cold.2
+ -[NSViewBridgeObject setObject:].cold.1
+ -[NSViewRemoteBridge auditToken].cold.1
+ -[NSViewRemoteBridge observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[NSViewRemoteBridge observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[NSViewRemoteBridge observeValueForKeyPath:ofObject:change:context:].cold.3
+ -[NSViewRemoteBridge observeValueForKeyPath:ofObject:change:context:].cold.4
+ -[NSViewRemoteBridge processIdentifier].cold.1
+ -[NSViewServiceAccessoryView _updateAccessoryViewAccessibility:].cold.1
+ -[NSViewServiceAccessoryView _updateAccessoryViewAccessibility:].cold.2
+ -[NSViewServiceAccessoryView _updateAccessoryViewAccessibility:].cold.3
+ -[NSViewServiceAccessoryView accessibilityChildren:].cold.1
+ -[NSViewServiceAccessoryView connectContext:withServiceMarshal:].cold.1
+ -[NSViewServiceAccessoryView initWithFrame:].cold.1
+ -[NSViewServiceAccessoryView updateAccessoryViewAccessibility:].cold.1
+ -[NSViewServiceAccessoryView updateAccessoryViewAccessibility:].cold.2
+ -[NSViewServiceApplication _eventIsToxic:].cold.1
+ -[NSViewServiceApplication _handleSymbolicHotKey:].cold.1
+ -[NSViewServiceApplication _modalSession:sendEvent:].cold.1
+ -[NSViewServiceApplication _modalSession:sendEvent:].cold.2
+ -[NSViewServiceApplication _modalSession:sendEvent:].cold.3
+ -[NSViewServiceApplication _shouldFakeMainWindow].cold.1
+ -[NSViewServiceApplication _shouldFakeMainWindow].cold.2
+ -[NSViewServiceApplication _withToxicEventMonitorPerform:].cold.1
+ -[NSViewServiceApplication appModalSessionInProgressForAnyHostOtherThan:].cold.1
+ -[NSViewServiceApplication beginHostAppModalSession:forWindow:withSize:withReply:].cold.1
+ -[NSViewServiceApplication beginHostAppModalSession:forWindow:withSize:withReply:].cold.2
+ -[NSViewServiceApplication beginHostAppModalSession:forWindow:withSize:withReply:].cold.3
+ -[NSViewServiceApplication beginHostAppModalSessionForWindow:withLocalSession:].cold.1
+ -[NSViewServiceApplication beginHostAppModalSessionForWindow:withLocalSession:].cold.2
+ -[NSViewServiceApplication beginHostAppModalSessionForWindow:withLocalSession:].cold.3
+ -[NSViewServiceApplication beginHostAppModalSessionForWindow:withLocalSession:relativeToWindow:].cold.1
+ -[NSViewServiceApplication beginHostAppModalSessionForWindow:withLocalSession:relativeToWindow:].cold.2
+ -[NSViewServiceApplication beginModalSessionForWindow:relativeToWindow:].cold.1
+ -[NSViewServiceApplication beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:].cold.2
+ -[NSViewServiceApplication endHostAppModalSession:withWindow:].cold.1
+ -[NSViewServiceApplication endHostAppModalSession:withWindow:].cold.2
+ -[NSViewServiceApplication endHostAppModalSession:withWindow:].cold.3
+ -[NSViewServiceApplication endModalSession:].cold.1
+ -[NSViewServiceApplication endServiceAppModalSession:withWindow:].cold.1
+ -[NSViewServiceApplication enqueueException:].cold.1
+ -[NSViewServiceApplication finishLaunching].cold.2
+ -[NSViewServiceApplication mainWindow].cold.1
+ -[NSViewServiceApplication raiseIfDeferredException:].cold.1
+ -[NSViewServiceApplication respondsToAction:fromTask:].cold.1
+ -[NSViewServiceApplication sendEvent:withForwarding:].cold.1
+ -[NSViewServiceApplication sendEventWithoutCatch:withForwarding:].cold.1
+ -[NSViewServiceBridge observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[NSViewServiceBridge observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[NSViewServiceBridge observeValueForKeyPath:ofObject:change:context:].cold.3
+ -[NSViewServiceBridge observeValueForKeyPath:ofObject:change:context:].cold.4
+ -[NSViewServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.1
+ -[NSViewServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.2
+ -[NSViewServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.3
+ -[NSViewServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.4
+ -[NSViewServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.5
+ -[NSViewServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.6
+ -[NSViewServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.7
+ -[NSViewServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.8
+ -[NSViewServiceMarshal _addChildWindow:ordered:].cold.1
+ -[NSViewServiceMarshal _addChildWindow:ordered:].cold.2
+ -[NSViewServiceMarshal _addChildWindow:ordered:].cold.3
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.1
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.10
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.11
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.12
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.13
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.14
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.15
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.16
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.17
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.18
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.2
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.3
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.4
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.5
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.6
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.7
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.8
+ -[NSViewServiceMarshal _bootstrap:replyData:completion:].cold.9
+ -[NSViewServiceMarshal _runCommandEquivalentEventLoop].cold.1
+ -[NSViewServiceMarshal _serviceWindowDidBecomeKey:].cold.1
+ -[NSViewServiceMarshal _serviceWindowDidResignKey:].cold.1
+ -[NSViewServiceMarshal _serviceWindowDidResize:].cold.1
+ -[NSViewServiceMarshal abortTrackingLoop:].cold.1
+ -[NSViewServiceMarshal acquireKeyAppearanceBecause:].cold.1
+ -[NSViewServiceMarshal addChildWindow:ordered:].cold.2
+ -[NSViewServiceMarshal adjustWindowContext].cold.1
+ -[NSViewServiceMarshal adjustWindowContext].cold.2
+ -[NSViewServiceMarshal advanceToRunPhase:].cold.1
+ -[NSViewServiceMarshal allowAppNap:].cold.1
+ -[NSViewServiceMarshal allowAppNap:].cold.2
+ -[NSViewServiceMarshal animateWindow:frame:].cold.1
+ -[NSViewServiceMarshal backingScaleFactor:].cold.1
+ -[NSViewServiceMarshal becomeKeyBecause:].cold.1
+ -[NSViewServiceMarshal becomeKeyWindow:].cold.1
+ -[NSViewServiceMarshal beginHostSheet:isCritical:completion:].cold.1
+ -[NSViewServiceMarshal beginHostSheet:isCritical:completion:].cold.2
+ -[NSViewServiceMarshal beginHostSheet:isCritical:completion:].cold.3
+ -[NSViewServiceMarshal beginHostSheet:isCritical:completion:].cold.4
+ -[NSViewServiceMarshal bootstrap:withReply:].cold.1
+ -[NSViewServiceMarshal cacheHostAccessibilityParentUsingToken:].cold.1
+ -[NSViewServiceMarshal cancelActionHitRemoteView].cold.1
+ -[NSViewServiceMarshal concretizedWindowBackgroundColor].cold.1
+ -[NSViewServiceMarshal concretizedWindowBackgroundColor].cold.2
+ -[NSViewServiceMarshal concretizedWindowBackgroundColor].cold.3
+ -[NSViewServiceMarshal concretizedWindowBackgroundColor].cold.4
+ -[NSViewServiceMarshal connectToAuxiliaryServiceWithWindow:].cold.1
+ -[NSViewServiceMarshal connectToAuxiliaryServiceWithWindow:].cold.2
+ -[NSViewServiceMarshal considerChildWindowsOfWindow:].cold.1
+ -[NSViewServiceMarshal constrainContentViewSize:ofWindow:].cold.1
+ -[NSViewServiceMarshal constrainContentViewSize:ofWindow:].cold.2
+ -[NSViewServiceMarshal constrainContentViewSize:ofWindow:].cold.3
+ -[NSViewServiceMarshal constrainContentViewSize:ofWindow:].cold.4
+ -[NSViewServiceMarshal constrainContentViewSize:ofWindow:].cold.5
+ -[NSViewServiceMarshal constrainContentViewSize:ofWindow:].cold.6
+ -[NSViewServiceMarshal description].cold.1
+ -[NSViewServiceMarshal didSetView].cold.1
+ -[NSViewServiceMarshal didSetView].cold.2
+ -[NSViewServiceMarshal didSetView].cold.3
+ -[NSViewServiceMarshal didSetView].cold.4
+ -[NSViewServiceMarshal didSetView].cold.5
+ -[NSViewServiceMarshal disengageFromAllWindows].cold.1
+ -[NSViewServiceMarshal electScrollViewSeparatorTrackingAdapterForWindow:].cold.1
+ -[NSViewServiceMarshal ensureClientExportedInterface].cold.1
+ -[NSViewServiceMarshal ensureClientExportedInterface].cold.2
+ -[NSViewServiceMarshal ensureClientExportedObject].cold.1
+ -[NSViewServiceMarshal ensureClientExportedObject].cold.2
+ -[NSViewServiceMarshal ensureWindow:hasCorrectOrigin:].cold.1
+ -[NSViewServiceMarshal exchangeAccessibilityTokens:enhancedUserInterface:withReply:].cold.1
+ -[NSViewServiceMarshal fakeMenuItemForTarget:withAction:].cold.1
+ -[NSViewServiceMarshal findTargetAndAction:].cold.1
+ -[NSViewServiceMarshal findTargetAndAction:].cold.2
+ -[NSViewServiceMarshal forgetConstraints].cold.1
+ -[NSViewServiceMarshal forgetConstraints].cold.2
+ -[NSViewServiceMarshal forgetViewController:].cold.1
+ -[NSViewServiceMarshal forwardActionUpHostResponderChain:].cold.1
+ -[NSViewServiceMarshal forwardActionUpHostResponderChain:].cold.2
+ -[NSViewServiceMarshal hasTouchBars:].cold.1
+ -[NSViewServiceMarshal hasTouchBars:].cold.2
+ -[NSViewServiceMarshal hostWindowBecameKey:inActiveApp:firstResponderState:isContentView:].cold.1
+ -[NSViewServiceMarshal hostWindowChangedKeyness:].cold.1
+ -[NSViewServiceMarshal hostWindowIsKey:].cold.1
+ -[NSViewServiceMarshal hostWindowLevelDidChange:].cold.1
+ -[NSViewServiceMarshal hostWindowModalSessionStatus:].cold.1
+ -[NSViewServiceMarshal hostWindowResignedKey:].cold.1
+ -[NSViewServiceMarshal hostWindowResignedKey:focusOnly:inActiveApp:isContentView:].cold.1
+ -[NSViewServiceMarshal informHostOfContentMinSize:contentMaxSize:].cold.1
+ -[NSViewServiceMarshal initWithConnection:].cold.1
+ -[NSViewServiceMarshal invalidate].cold.1
+ -[NSViewServiceMarshal maintainNotificationsForWindow:].cold.1
+ -[NSViewServiceMarshal maintainNotificationsForWindow:].cold.2
+ -[NSViewServiceMarshal maintainNotificationsForWindow:].cold.3
+ -[NSViewServiceMarshal maintainNotificationsForWindow:].cold.4
+ -[NSViewServiceMarshal observeValueForContentMinSize:].cold.1
+ -[NSViewServiceMarshal observeValueForContentMinSize:].cold.2
+ -[NSViewServiceMarshal observeValueForContentView:].cold.1
+ -[NSViewServiceMarshal observeValueForContentView:].cold.2
+ -[NSViewServiceMarshal observeValueForContentView:].cold.3
+ -[NSViewServiceMarshal observeValueForContentView:].cold.4
+ -[NSViewServiceMarshal observeValueForContentView:].cold.5
+ -[NSViewServiceMarshal observeValueForFirstResponder:].cold.1
+ -[NSViewServiceMarshal observeValueForFirstResponder:].cold.2
+ -[NSViewServiceMarshal observeValueForHasScrolledContentsUnderTitlebar:ofScrollViewSeparatorTrackingAdapter:].cold.1
+ -[NSViewServiceMarshal observeValueForHasScrolledContentsUnderTitlebar:ofScrollViewSeparatorTrackingAdapter:].cold.2
+ -[NSViewServiceMarshal observeValueForScrollViewFrame:ofScrollViewSeparatorTrackingAdapter:].cold.1
+ -[NSViewServiceMarshal observeValueForScrollViewFrame:ofScrollViewSeparatorTrackingAdapter:].cold.2
+ -[NSViewServiceMarshal observeValueForWindow:ofObject:change:context:].cold.1
+ -[NSViewServiceMarshal orderWindow:options:].cold.1
+ -[NSViewServiceMarshal orderWindow:options:].cold.2
+ -[NSViewServiceMarshal orderedDrawerAndWindowKeyLoopGroupingViews:].cold.1
+ -[NSViewServiceMarshal performAction:forTarget:].cold.1
+ -[NSViewServiceMarshal prepareWindow:].cold.1
+ -[NSViewServiceMarshal registerBridgeKey:defaultObject:owner:].cold.1
+ -[NSViewServiceMarshal remoteViewBecameFirstResponder:forWindowsWithKeyness:inVisibleWindow:].cold.1
+ -[NSViewServiceMarshal remoteViewChangedFirstResponder:].cold.1
+ -[NSViewServiceMarshal remoteViewControllerProxy:].cold.1
+ -[NSViewServiceMarshal remoteViewControllerProxy:].cold.2
+ -[NSViewServiceMarshal remoteViewControllerProxy:].cold.3
+ -[NSViewServiceMarshal remoteViewMarshal:withErrorHandler:].cold.1
+ -[NSViewServiceMarshal remoteViewReceivedLeftMouseDown:].cold.1
+ -[NSViewServiceMarshal requestFrame:transaction:animate:async:completion:].cold.1
+ -[NSViewServiceMarshal requestFrame:transaction:animate:async:completion:].cold.2
+ -[NSViewServiceMarshal requestFrame:transaction:animate:async:completion:].cold.3
+ -[NSViewServiceMarshal requestFrame:transaction:animate:async:completion:].cold.4
+ -[NSViewServiceMarshal resignFirstResponderIfNecessary].cold.1
+ -[NSViewServiceMarshal resignKeyWindow:].cold.1
+ -[NSViewServiceMarshal retreatToConfigPhase].cold.1
+ -[NSViewServiceMarshal retreatToConfigPhase].cold.2
+ -[NSViewServiceMarshal scrollViewSeparatorTrackingAdapter:qualifiesForWindow:].cold.1
+ -[NSViewServiceMarshal scrollViewSeparatorTrackingAdapter:qualifiesForWindow:].cold.2
+ -[NSViewServiceMarshal semaphoreForViewBridgePrivateMode].cold.1
+ -[NSViewServiceMarshal setAppearanceOfWindow:].cold.1
+ -[NSViewServiceMarshal setEventMaskBasedOnWindow:].cold.1
+ -[NSViewServiceMarshal setFirstResponderForRemoteView:].cold.1
+ -[NSViewServiceMarshal setFirstResponderForRemoteView:].cold.2
+ -[NSViewServiceMarshal setFirstResponderForRemoteView:].cold.3
+ -[NSViewServiceMarshal setHostObject:forKey:].cold.1
+ -[NSViewServiceMarshal setHostObject:forKey:].cold.2
+ -[NSViewServiceMarshal unregisterScrollViewSeparatorTrackingAdapter:forWindow:].cold.1
+ -[NSViewServiceMarshal unregisterScrollViewSeparatorTrackingAdapter:forWindow:].cold.2
+ -[NSViewServiceMarshal updateWindow:frameAnimationStatusAfterActions:].cold.1
+ -[NSViewServiceMarshal validateTargetAndAction:validateMenuItem:validateUserInterfaceItem:].cold.1
+ -[NSViewServiceMarshal visualizeConstraints].cold.1
+ -[NSViewServiceMarshal visualizeConstraints].cold.2
+ -[NSViewServiceMarshal visualizeConstraints].cold.3
+ -[NSViewServiceMarshal whileContainedRemoteViewSetsCursorPerform:].cold.1
+ -[NSViewServiceMarshal whileFilteringResponderChain:].cold.1
+ -[NSViewServiceMarshal whileOrderingSheetFront:withParent:performActions:].cold.1
+ -[NSViewServiceMarshal whileOrderingWindow:perform:].cold.1
+ -[NSViewServiceMarshal window:hasRegionForOpaqueViews:blockingDraggableFrame:].cold.1
+ -[NSViewServiceMarshal windowForContextID:reply:].cold.1
+ -[NSViewServiceMarshal windowReceivedLeftMouseDown:].cold.1
+ -[NSViewServiceMarshal windowReceivedLeftMouseDown:].cold.2
+ -[NSViewServiceMarshal windowReceivedLeftMouseDown:].cold.3
+ -[NSViewServiceMarshalSemaphore wait:].cold.1
+ -[NSViewService_PKSubsystem _beginUsing:withBundle:].cold.1
+ -[NSWindow(NSPreviewTarget) previewSwizzledAddChildWindow:ordered:].cold.1
+ -[NSWindow(NSPreviewTarget) previewSwizzledAddChildWindow:ordered:].cold.2
+ -[NSWindow(NSPreviewTarget) previewSwizzledSetLevel:].cold.1
+ -[NSWindow(NSPreviewTarget) previewSwizzledStyleMask].cold.1
+ -[NSWindow(ViewBridgeService) _isPopoverWindow].cold.1
+ -[NSWindow(ViewBridgeService) _lastDragRegionDataDescription].cold.1
+ -[NSWindow(ViewBridgeService) _lastDragRegionDataDescription].cold.2
+ -[NSWindow(ViewBridgeService) _lastDragRegionDataDescription].cold.3
+ -[NSWindow(ViewBridgeService) _lastDragRegionDataDescription].cold.4
+ -[NSWindow(ViewBridgeService) _lastDragRegionDataDescription].cold.5
+ -[NSWindow(ViewBridgeService) _lastDragRegionDataDescription].cold.6
+ -[NSWindow(ViewBridgeService) _lastDragRegionDataDescription].cold.7
+ -[NSWindow(ViewBridgeSwizzle) _addViewServiceNameToTitleOfColorPanel:].cold.1
+ -[NSWindow(ViewBridgeSwizzle) _addViewServiceNameToTitleOfColorPanel:].cold.2
+ -[NSWindow(ViewBridgeSwizzle) _addViewServiceNameToTitleOfColorPanel:].cold.3
+ -[NSWindow(ViewBridgeSwizzle) _beginSheet:isCritical:completionHandler:].cold.1
+ -[NSWindow(ViewBridgeSwizzle) _beginSheet:isCritical:completionHandler:].cold.2
+ -[NSWindow(ViewBridgeSwizzle) _localizedInfoDictionaryObjectForKey:ifAvailableFromBundle:].cold.1
+ -[NSWindow(ViewBridgeSwizzle) _localizedInfoDictionaryObjectForKey:ifAvailableFromBundle:].cold.2
+ -[NSWindow(ViewBridgeSwizzle) _localizedInfoDictionaryObjectForKey:ifAvailableFromBundle:].cold.3
+ -[NSWindow(ViewBridgeSwizzle) _vbEndSheet:returnCode:].cold.1
+ -[NSWindow(ViewBridgeSwizzle) beginServiceSheet:completionHandler:isCritical:].cold.1
+ -[NSWindow(ViewBridgeSwizzle) swizzledAddChildWindow:ordered:].cold.2
+ -[NSWindow(ViewBridgeSwizzle) swizzledDoOrderWindow:].cold.1
+ -[NSXPCSharedListener addListener:withName:].cold.1
+ -[NSXPCSharedListener addListener:withName:].cold.2
+ -[NSXPCSharedListener listenerEndpointWithName:].cold.1
+ -[NSXPCSharedListener resumeAdditionalService:].cold.1
+ -[NSXPCSharedListener resumeSubService:].cold.1
+ -[NSXPCSharedListenerManagerDelegate listener:shouldAcceptNewConnection:].cold.1
+ -[NSXPCSharedListenerManagerDelegate listener:shouldAcceptNewConnection:].cold.2
+ -[NSXPCSharedListenerManagerDelegate listener:shouldAcceptNewConnection:].cold.3
+ -[ServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.1
+ -[ServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.2
+ -[ServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.3
+ -[ServiceListenerDelegate listener:shouldAcceptNewConnection:].cold.4
+ -[UINSServiceViewController _redirectTarget:forSelector:].cold.1
+ -[UINSServiceViewController _respondsToAction:forTarget:].cold.1
+ -[UINSServiceViewController _respondsToAction:forTarget:].cold.2
+ -[UINSServiceViewController _respondsToAction:forTarget:].cold.3
+ -[UINSServiceViewController _validateTarget:forAction:].cold.1
+ -[UINSServiceViewController _validateTarget:forAction:].cold.2
+ -[UINSServiceViewController _validateTarget:forAction:].cold.3
+ -[UINSServiceViewController _validateTarget:forAction:].cold.4
+ -[UINSServiceViewController loadView].cold.1
+ -[UINSServiceViewController loadView].cold.2
+ -[UINSServiceViewController loadView].cold.3
+ -[UINSServiceViewController loadView].cold.4
+ -[UINSServiceViewController loadView].cold.5
+ -[VBUnretainedMap description].cold.1
+ -[VBUnretainedMap objectForKey:].cold.1
+ -[VBUnretainedMap removeObjectForKey:].cold.1
+ -[VBXPCConnection initWithListenerEndpoint:andReplyPatience:].cold.1
+ -[VBXPCConnection initWithUnderlyingConnection:andReplyPatience:].cold.1
+ -[VBXPCConnection initWithUnderlyingConnection:andReplyPatience:].cold.2
+ -[VBXPCConnectionFenced acquireActiveRole].cold.1
+ -[VBXPCConnectionFenced addIncomingFence:].cold.1
+ -[VBXPCConnectionFenced addIncomingFence:].cold.2
+ -[VBXPCConnectionFenced addPostCommitHandlerIfNecessary].cold.1
+ -[VBXPCConnectionFenced description].cold.1
+ -[VBXPCConnectionFenced incrementActiveRoleDurability].cold.1
+ -[VBXPCConnectionFenced mutateOutgoingMessage:withReplyIdentifier:].cold.1
+ -[VBXPCConnectionFenced mutateOutgoingMessage:withReplyIdentifier:].cold.2
+ -[VBXPCConnectionFenced startFenceForMessage:withContext:].cold.1
+ -[VBXPCConnectionFenced startFenceForMessage:withContext:].cold.2
+ -[VBXPCConnectionTransport completeReply:].cold.1
+ -[VBXPCConnectionTransport initWithConnection:].cold.1
+ -[VBXPCConnectionTransport setErrorHandler:].cold.1
+ -[VBXPCConnectionTransport setMessageHandler:].cold.1
+ -[ViewHost invalidate:].cold.1
+ -[ViewHost potentialCommandEquivalentHitServiceApp:from:fullDispatch:reply:].cold.1
+ -[ViewService eventResemblesCommandEquivalent:].cold.1
+ -[ViewService invalidate:].cold.1
+ -[ViewService keyboardEventHitRemoteView:from:reply:].cold.1
+ -[ViewService keyboardEventHitRemoteView:from:reply:].cold.2
+ -[ViewService requestFrame:serviceWindowBackgroundColor:animate:async:transaction:completion:].cold.1
+ -[ViewService windowForContextID:reply:].cold.1
+ GCC_except_table247
+ NSRemoteViewControllerParametersForServiceAssertCoherence.cold.1
+ NSViewServiceMain.cold.1
+ NSViewServiceMain.cold.10
+ NSViewServiceMain.cold.11
+ NSViewServiceMain.cold.12
+ NSViewServiceMain.cold.13
+ NSViewServiceMain.cold.14
+ NSViewServiceMain.cold.15
+ NSViewServiceMain.cold.16
+ NSViewServiceMain.cold.17
+ NSViewServiceMain.cold.2
+ NSViewServiceMain.cold.3
+ NSViewServiceMain.cold.4
+ NSViewServiceMain.cold.5
+ NSViewServiceMain.cold.6
+ NSViewServiceMain.cold.7
+ NSViewServiceMain.cold.8
+ NSViewServiceMain.cold.9
+ VBMutableDictionaryAddValue.cold.1
+ VBMutableDictionaryAddValue.cold.2
+ VBMutableDictionaryAddValue.cold.3
+ VBMutableDictionaryCount.cold.1
+ VBMutableDictionaryCreate.cold.1
+ VBMutableDictionaryCreate.cold.2
+ VBMutableDictionaryGetValue.cold.1
+ VBMutableDictionaryGetValue.cold.2
+ VBMutableDictionaryRemoveValue.cold.1
+ VBMutableDictionaryRemoveValue.cold.2
+ VBShouldLogFirst.cold.1
+ ViewBridgeAuxiliaryMain.cold.1
+ _NSRendezvousWindowApplicationTerminationBehaviorWhenModal
+ _NSViewServiceGetDelegate.cold.1
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
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ZL31methodNotSupportedWithQualifierP13objc_selectorP10objc_classPKc.cold.1
+ _ZL31methodNotSupportedWithQualifierP13objc_selectorP10objc_classPKc.cold.2
+ _ZL31methodNotSupportedWithQualifierP13objc_selectorP10objc_classPKc.cold.3
+ _ZL32synchronizedWithHostsAndServicesU13block_pointerFvP19NSMutableDictionaryIP8NSStringP14HostAndServiceEE.cold.1
+ _ZL33NSPreviewHostKeyFocusThiefMonitor_block_invoke_2.cold.1
+ _ZL33NSPreviewHostKeyFocusThiefMonitor_block_invoke_2.cold.2
+ _ZL33NSPreviewHostKeyFocusThiefMonitor_block_invoke_2.cold.3
+ _ZL33NSPreviewHostKeyFocusThiefMonitor_block_invoke_2.cold.4
+ _ZL33NSPreviewHostKeyFocusThiefMonitor_block_invoke_2.cold.5
+ _ZL33NSPreviewHostKeyFocusThiefMonitor_block_invoke_2.cold.6
+ _ZL33NSPreviewHostKeyFocusThiefMonitor_block_invoke_2.cold.7
+ _ZL35synchronizedWithHostAppDescriptionsU13block_pointerFvP19NSMutableDictionaryIP14NSVBAuditTokenP12NSDictionaryEE.cold.1
+ _ZL40notifyPresentationAgainstWindowSupressedP8NSWindow41NSPreviewTargetSuppressedPresentationKind.cold.1
+ _ZL40notifyPresentationAgainstWindowSupressedP8NSWindow41NSPreviewTargetSuppressedPresentationKind.cold.2
+ _ZL40synchronizedWithHostAppListenerEndpointsU13block_pointerFvP19NSMutableDictionaryIP14NSVBAuditTokenP21NSXPCListenerEndpointEE.cold.1
+ _ZL43CoreApplicationServicesNotificationFunction18LSNotificationCodedPKvPK7__LSASNS1_11LSSessionIDS1_.cold.1
+ _ZL43CoreApplicationServicesNotificationFunction18LSNotificationCodedPKvPK7__LSASNS1_11LSSessionIDS1_.cold.2
+ _ZL43CoreApplicationServicesNotificationFunction18LSNotificationCodedPKvPK7__LSASNS1_11LSSessionIDS1_.cold.3
+ _ZL43CoreApplicationServicesNotificationFunction18LSNotificationCodedPKvPK7__LSASNS1_11LSSessionIDS1_.cold.4
+ _ZN6EventsC2EPKcj.cold.1
+ __102+[NSVB_ViewServiceImplicitAnimationDecodingProxy proxyDecodingAnimationsForTarget:withServiceMarshal:]_block_invoke.45.cold.1
+ __102+[NSVB_ViewServiceImplicitAnimationDecodingProxy proxyDecodingAnimationsForTarget:withServiceMarshal:]_block_invoke_2.cold.1
+ __102+[NSVB_ViewServiceImplicitAnimationDecodingProxy proxyDecodingAnimationsForTarget:withServiceMarshal:]_block_invoke_3.cold.1
+ __106+[NSMenu(ViewBridgeSwizzle) swizzledMenuItemWithKeyEquivalentMatchingEvent:inMenu:includingDisabledItems:]_block_invoke.cold.1
+ __106+[NSMenu(ViewBridgeSwizzle) swizzledMenuItemWithKeyEquivalentMatchingEvent:inMenu:includingDisabledItems:]_block_invoke.cold.2
+ __108+[NSXPCSharedListener _endpointForListenerNamed:fromServiceNamed:instanceIdentifier:queue:async:completion:]_block_invoke_2.cold.1
+ __109-[ViewHost joinPair:serviceViewControllerIdentifier:frameInScreenCoords:hostWindowKind:hostWindowBase:reply:]_block_invoke.cold.1
+ __116+[NSRemoteViewController requestViewController:withServiceViewControllerIdentifier:forRemoteView:connectionHandler:]_block_invoke.cold.1
+ __116+[NSRemoteViewController requestViewController:withServiceViewControllerIdentifier:forRemoteView:connectionHandler:]_block_invoke.cold.2
+ __116+[NSRemoteViewController requestViewController:withServiceViewControllerIdentifier:forRemoteView:connectionHandler:]_block_invoke.cold.3
+ __150+[NSRemoteViewController requestViewControllerForExtensionWithIdentifier:fromServiceWithBundleIdentifier:serviceInstanceIdentifier:connectionHandler:]_block_invoke.cold.1
+ __150+[NSRemoteViewController requestViewControllerForExtensionWithIdentifier:fromServiceWithBundleIdentifier:serviceInstanceIdentifier:connectionHandler:]_block_invoke.cold.2
+ __150+[NSRemoteViewController requestViewControllerForExtensionWithIdentifier:fromServiceWithBundleIdentifier:serviceInstanceIdentifier:connectionHandler:]_block_invoke.cold.3
+ __21-[FenceGroup dealloc]_block_invoke.cold.1
+ __23+[NSRemoteView initAll]_block_invoke_3.cold.1
+ __28+[NSViewBridge validClasses]_block_invoke.cold.1
+ __29-[NSCFRunLoopSemaphore wait:]_block_invoke.cold.1
+ __35+[NSCFRunLoopSemaphore invocations]_block_invoke.cold.1
+ __35-[NSXPCSharedListener addDelegate:]_block_invoke.cold.1
+ __35-[NSXPCSharedListener addDelegate:]_block_invoke.cold.2
+ __36+[NSXPCSharedListener endpointCache]_block_invoke.cold.1
+ __36-[FenceGroupMember join:completion:]_block_invoke.cold.1
+ __36-[FenceGroupMember join:completion:]_block_invoke.cold.2
+ __37+[FenceGroup withFenceGroupsPerform:]_block_invoke.cold.1
+ __37-[CalledByClient endpointForHostApp:]_block_invoke.cold.1
+ __37-[UINSServiceViewController loadView]_block_invoke.cold.1
+ __37-[ViewService joinPair:window:reply:]_block_invoke.cold.1
+ __38+[NSRemoteView rendezvousWindowClass:]_block_invoke_2.cold.1
+ __38+[NSRemoteView rendezvousWindowClass:]_block_invoke_3.cold.1
+ __38+[NSRemoteView rendezvousWindowClass:]_block_invoke_3.cold.2
+ __38-[NSRemoteView _advanceToConfigPhase:]_block_invoke.cold.1
+ __38-[NSRemoteView _advanceToConfigPhase:]_block_invoke.cold.2
+ __39+[ViewBridgeUtilities createIdentifier]_block_invoke.cold.1
+ __39-[HostOrService applicationDisplayName]_block_invoke.cold.1
+ __39-[HostOrService applicationDisplayName]_block_invoke.cold.2
+ __41-[NSRemoteView _beginTrackingLoop:reply:]_block_invoke.cold.1
+ __42-[HostOrService joinPair:reply:configure:]_block_invoke.cold.1
+ __42-[VBXPCConnectionFenced acquireActiveRole]_block_invoke.18.cold.1
+ __42-[VBXPCConnectionFenced acquireActiveRole]_block_invoke.cold.1
+ __44+[HostAndService determineKeyFocus:because:]_block_invoke.132.cold.1
+ __44+[HostAndService determineKeyFocus:because:]_block_invoke.159.cold.1
+ __44+[HostAndService determineKeyFocus:because:]_block_invoke.159.cold.2
+ __44+[HostAndService determineKeyFocus:because:]_block_invoke.159.cold.3
+ __44+[HostAndService determineKeyFocus:because:]_block_invoke.cold.1
+ __44+[HostAndService determineKeyFocus:because:]_block_invoke_2.cold.1
+ __44+[HostAndService determineKeyFocus:because:]_block_invoke_2.cold.2
+ __44+[HostAndService determineKeyFocus:because:]_block_invoke_2.cold.3
+ __44+[NSRemoteView remoteViewsAttachedToWindow:]_block_invoke.cold.1
+ __44+[NSXPCSharedListener sharedServiceListener]_block_invoke.cold.1
+ __44+[NSXPCSharedListener sharedServiceListener]_block_invoke.cold.2
+ __44+[NSXPCSharedListener sharedServiceListener]_block_invoke.cold.3
+ __44+[NSXPCSharedListener sharedServiceListener]_block_invoke.cold.4
+ __44-[NSViewServiceMarshal allowKeyboardEvents:]_block_invoke.cold.1
+ __44-[NSXPCSharedListener addListener:withName:]_block_invoke.cold.1
+ __44-[NSXPCSharedListener addListener:withName:]_block_invoke.cold.2
+ __45+[NSTouchBar(ViewBridge) _activeBarsAndItems]_block_invoke.cold.1
+ __45+[NSTouchBar(ViewBridge) _activeBarsAndItems]_block_invoke.cold.2
+ __45+[ViewBridgeUtilities copyDeferredBlockQueue]_block_invoke.cold.1
+ __46+[NSRemoteView anyRemoteViewAttachedToWindow:]_block_invoke.cold.1
+ __46-[NSRemoteView setRendezvousWindowIdentifier:]_block_invoke.cold.1
+ __46-[ViewService declineKeyboardEventsOtherThan:]_block_invoke.cold.1
+ __47-[NSPreviewTargetWindow startLocalEventMonitor]_block_invoke.cold.1
+ __47-[NSRemoteView _remoteViewBecameFirstResponder]_block_invoke.cold.1
+ __47-[VBXPCConnectionFenced fenceGroupMemberProxy:]_block_invoke.cold.1
+ __47-[VBXPCConnectionFenced fenceGroupMemberProxy:]_block_invoke.cold.2
+ __47-[VBXPCConnectionTransport detectReplyTimeout:]_block_invoke.cold.1
+ __48+[NSViewServiceApplication serviceConfiguration]_block_invoke.cold.1
+ __48+[NSViewServiceMarshal auxiliaryProxyFor:async:]_block_invoke.cold.1
+ __48-[NSRemoteViewControllerForTouchBarItem kvoKeys]_block_invoke.cold.1
+ __49+[NSCFRunLoopSemaphore _observe:whilePerforming:]_block_invoke.cold.1
+ __49+[NSCFRunLoopSemaphore _observe:whilePerforming:]_block_invoke.cold.2
+ __49+[NSCFRunLoopSemaphore _observe:whilePerforming:]_block_invoke_2.cold.1
+ __49+[NSCFRunLoopSemaphore _observe:whilePerforming:]_block_invoke_2.cold.2
+ __49+[NSVBNamedFault fault:withProbability:wasTaken:]_block_invoke.cold.1
+ __49+[NSVBNamedFault fault:withProbability:wasTaken:]_block_invoke.cold.2
+ __49-[CalledByClient forApp:retrievePreviewEndpoint:]_block_invoke.765.cold.1
+ __49-[FenceGroupMember acquireActiveRole:completion:]_block_invoke.cold.1
+ __49-[FenceGroupMember acquireActiveRole:completion:]_block_invoke.cold.2
+ __49-[FenceGroupMember acquireActiveRole:completion:]_block_invoke.cold.3
+ __51+[NSPreviewTargetController _nsxpcListenerEndpoint]_block_invoke.cold.1
+ __52-[NSRemoteView _maintainFirstResponder:inDirection:]_block_invoke.1477.cold.1
+ __52-[NSRemoteView _maintainFirstResponder:inDirection:]_block_invoke.cold.1
+ __53+[NSAutolayoutJailWindow frameViewClassForStyleMask:]_block_invoke_2.cold.1
+ __53+[NSAutolayoutJailWindow frameViewClassForStyleMask:]_block_invoke_2.cold.2
+ __53+[ViewBridgeUtilities hostAppClientParametersClasses]_block_invoke.cold.1
+ __53-[NSServiceViewController remoteViewControllerProxy:]_block_invoke.cold.1
+ __54-[NSViewServiceMarshal remoteViewCaresAboutTouchBars:]_block_invoke.cold.1
+ __55+[NSXPCSharedListener warmUpClassNamed:inServiceNamed:]_block_invoke.cold.1
+ __55+[NSXPCSharedListener warmUpClassNamed:inServiceNamed:]_block_invoke.cold.2
+ __56-[NSViewServiceMarshal _bootstrap:replyData:completion:]_block_invoke.cold.1
+ __56-[NSViewServiceMarshal _bootstrap:replyData:completion:]_block_invoke.cold.2
+ __56-[NSViewServiceMarshal _bootstrap:replyData:completion:]_block_invoke.cold.3
+ __56-[NSViewServiceMarshal _bootstrap:replyData:completion:]_block_invoke.cold.4
+ __57+[NSViewServiceMarshal informHostsOfConnectionToService:]_block_invoke.cold.1
+ __57+[NSXPCSharedListener getSDKVersionOfServiceNamed:reply:]_block_invoke.cold.1
+ __57+[NSXPCSharedListener getSDKVersionOfServiceNamed:reply:]_block_invoke.cold.2
+ __57-[NSAccessoryViewWindow updateAccessoryViewAccessibility]_block_invoke.cold.1
+ __59-[NSViewServiceMarshal remoteViewMarshal:withErrorHandler:]_block_invoke.cold.1
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.1
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.2
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.3
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.4
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.5
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.6
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.7
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.8
+ __60-[NSRemoteViewControllerParametersForService initWithCoder:]_block_invoke.cold.9
+ __60-[NSViewServiceMarshal connectToAuxiliaryServiceWithWindow:]_block_invoke.cold.1
+ __60-[NSViewServiceMarshal frameOfServiceWindowDidChange:reply:]_block_invoke.1570.cold.1
+ __61+[NSPreviewHostViewController launchTargetApp:options:error:]_block_invoke.cold.1
+ __62-[NSEventLoopSemaphore invokeLoopInModeForDuration:withBlock:]_block_invoke.cold.1
+ __65+[NSPreviewTargetController bootstrap:hostControllerProxy:reply:]_block_invoke.cold.1
+ __65+[NSPreviewTargetController commandEquivalentsToWithholdFromHost]_block_invoke.cold.1
+ __65+[NSXPCSharedListener listenerEndpointForService:listener:error:]_block_invoke.cold.1
+ __65+[NSXPCSharedListener listenerEndpointForService:listener:error:]_block_invoke.cold.2
+ __65-[ViewService _addChildWindow:identifier:listenerEndpoint:reply:]_block_invoke.cold.1
+ __66+[NSVB_AnimationFencingSupport _animateWithAttributes:animations:]_block_invoke.cold.1
+ __67-[CalledByClient _addFreeWindow:identifier:listenerEndpoint:reply:]_block_invoke.cold.1
+ __67-[CalledByClient _addFreeWindow:identifier:listenerEndpoint:reply:]_block_invoke.cold.2
+ __67-[CalledByClient _addFreeWindow:identifier:listenerEndpoint:reply:]_block_invoke_2.cold.1
+ __67-[VBXPCConnectionFenced mutateOutgoingMessage:withReplyIdentifier:]_block_invoke.cold.1
+ __69+[NSPreviewTargetController setCommandEquivalentsToWithholdFromHost:]_block_invoke.cold.1
+ __69-[NSPreviewHostViewController targetControllerProxyWithErrorHandler:]_block_invoke.cold.1
+ __70+[NSRendezvousWindowController bridgeKeysForSemiAutonomousWindowBase:]_block_invoke.cold.1
+ __70+[NSRendezvousWindowController bridgeKeysForSemiAutonomousWindowBase:]_block_invoke.cold.2
+ __70+[NSRendezvousWindowController bridgeKeysForSemiAutonomousWindowBase:]_block_invoke.cold.3
+ __70+[NSRendezvousWindowController bridgeKeysForSemiAutonomousWindowBase:]_block_invoke.cold.4
+ __70-[NSViewServiceMarshal updateWindow:frameAnimationStatusAfterActions:]_block_invoke.665.cold.1
+ __72+[NSRemoteViewMarshal _addFreeWindow:parameters:listenerEndpoint:reply:]_block_invoke.cold.1
+ __72+[NSRemoteViewMarshal _addFreeWindow:parameters:listenerEndpoint:reply:]_block_invoke.cold.2
+ __72+[NSRemoteViewMarshal _addFreeWindow:parameters:listenerEndpoint:reply:]_block_invoke_2.cold.1
+ __72+[NSXPCSharedListener service:builtForPlatform:againstMinimumSDK:reply:]_block_invoke.cold.1
+ __72+[NSXPCSharedListener service:builtForPlatform:againstMinimumSDK:reply:]_block_invoke.cold.2
+ __72-[NSRemoteView wrapProxyForAnimationFencing:withAnimationAttributesFor:]_block_invoke.cold.1
+ __74+[NSXPCSharedListener connectToService:instanceIdentifier:listener:error:]_block_invoke.cold.1
+ __74+[NSXPCSharedListener connectToService:instanceIdentifier:listener:error:]_block_invoke.cold.2
+ __74-[NSViewServiceMarshal requestFrame:transaction:animate:async:completion:]_block_invoke.1493.cold.1
+ __74-[ViewService _frameOfServiceWindowDidChange:windowBackgroundColor:reply:]_block_invoke.cold.1
+ __75-[CalledByClient _requestUserInteractionWithPatience:options:sender:reply:]_block_invoke.cold.1
+ __75-[CalledByClient _requestUserInteractionWithPatience:options:sender:reply:]_block_invoke.cold.2
+ __75-[NSServiceViewController remoteViewControllerProxy:withProxyErrorHandler:]_block_invoke.cold.1
+ __75-[NSServiceViewController remoteViewControllerProxy:withProxyErrorHandler:]_block_invoke.cold.2
+ __75-[NSServiceViewController remoteViewControllerProxy:withProxyErrorHandler:]_block_invoke_2.cold.1
+ __77-[NSRemoteView _beginAppModalSession:parameters:listenerEndpoint:completion:]_block_invoke_2.cold.1
+ __77-[NSRemoteView _beginAppModalSession:parameters:listenerEndpoint:completion:]_block_invoke_2.cold.2
+ __79+[NSAccessoryViewWindow windowWithContentRect:atopRemoteView:withColorization:]_block_invoke.cold.1
+ __79+[NSAccessoryViewWindow windowWithContentRect:atopRemoteView:withColorization:]_block_invoke.cold.2
+ __80-[NSSemiAutonomousRendezvousWindowController remoteViewSizeChanged:transaction:]_block_invoke.cold.1
+ __82-[NSRemoteViewMarshal beginAppModalSession:parameters:listenerEndpoint:withReply:]_block_invoke.cold.1
+ __84-[NSVB_ViewServiceFencingController fencingControlProxy:didEndFencingWithSendRight:]_block_invoke.51.cold.1
+ __84-[ViewService _requestFrame:windowBackgroundColor:duringFunc:withProxyOrErrorBlock:]_block_invoke.cold.1
+ __84-[ViewService _requestFrame:windowBackgroundColor:duringFunc:withProxyOrErrorBlock:]_block_invoke.cold.2
+ __84-[ViewService _requestFrame:windowBackgroundColor:duringFunc:withProxyOrErrorBlock:]_block_invoke_2.cold.1
+ __86-[NSVB_ViewServiceFencingController fencingControlProxy:didBeginFencingWithSendRight:]_block_invoke.cold.1
+ __86-[NSVB_ViewServiceFencingController fencingControlProxy:didBeginFencingWithSendRight:]_block_invoke.cold.2
+ __88+[ViewBridgeUtilities allowSettingMousePointerImageInBackground:whilePerformingActions:]_block_invoke.cold.2
+ __91+[NSServiceViewControllerForTouchBarItem touchBarProviders:inWindow:includingWindowItself:]_block_invoke.269.cold.1
+ __91+[NSServiceViewControllerForTouchBarItem touchBarProviders:inWindow:includingWindowItself:]_block_invoke.cold.1
+ __94-[NSRemoteViewHostAppExportedObject _requestUserInteractionWithPatience:options:sender:reply:]_block_invoke.cold.1
+ __95+[NSXPCSharedListener listenerEndpointForService:instanceIdentifier:listener:queue:completion:]_block_invoke_2.cold.1
+ __95-[ViewService _requestFrame:serviceWindowBackgroundColor:animate:async:transaction:completion:]_block_invoke.cold.1
+ __98-[NSRemoteView _beginSheet:windowBase:modalForWindow:size:isCritical:listenerEndpoint:completion:]_block_invoke.cold.1
+ __98-[NSRemoteView _beginSheet:windowBase:modalForWindow:size:isCritical:listenerEndpoint:completion:]_block_invoke.cold.2
+ __98-[NSRemoteView _beginSheet:windowBase:modalForWindow:size:isCritical:listenerEndpoint:completion:]_block_invoke.cold.3
+ __98-[NSRemoteView _beginSheet:windowBase:modalForWindow:size:isCritical:listenerEndpoint:completion:]_block_invoke.cold.4
+ __98-[NSRemoteView _beginSheet:windowBase:modalForWindow:size:isCritical:listenerEndpoint:completion:]_block_invoke.cold.5
+ __MergedGlobals
+ __ZNKSt3__16vectorIPU18objcproto8NSObject11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU18objcproto8NSObject11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__13mapIP10objc_classS2_NS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S2_EEEEED1B8ne190102Ev
+ __ZNSt3__13setIP10objc_classNS_4lessIS2_EENS_9allocatorIS2_EEED1B8ne190102Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___ZL12swizzleAllocv_block_invoke.cold.1
+ ___ZL20signalHandlerSIGUSR1Pv_block_invoke.cold.1
+ ___ZL20signalHandlerSIGUSR1Pv_block_invoke_2.cold.1
+ ___ZL32synchronizedWithHostsAndServicesU13block_pointerFvP19NSMutableDictionaryIP8NSStringP14HostAndServiceEE_block_invoke.cold.1
+ ___ZL35synchronizedWithHostAppDescriptionsU13block_pointerFvP19NSMutableDictionaryIP14NSVBAuditTokenP12NSDictionaryEE_block_invoke.cold.1
+ ___ZL40synchronizedWithHostAppListenerEndpointsU13block_pointerFvP19NSMutableDictionaryIP14NSVBAuditTokenP21NSXPCListenerEndpointEE_block_invoke.cold.1
+ ___ZL9bootstrapP27NSPreviewHostViewControllerP21NSXPCListenerEndpointP37NSPreviewHostViewControllerParametersU13block_pointerFvPU8__kindofS_P7NSErrorE_block_invoke_3.cold.1
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.1
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.10
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.11
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.12
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.13
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.14
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.15
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.16
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.17
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.18
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.2
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.3
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.4
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.5
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.6
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.7
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.8
+ ___ensureAuxServiceAwareOfHostApp_block_invoke.cold.9
+ ___ensureAuxServiceAwareOfHostApp_block_invoke_2.2668.cold.1
+ __aeInteractWithUserCallback_block_invoke.cold.1
+ __aeInteractWithUserCallback_block_invoke.cold.2
+ __aeInteractWithUserCallback_block_invoke.cold.3
+ __aeInteractWithUserCallback_block_invoke.cold.4
+ __aeInteractWithUserCallback_block_invoke.cold.5
+ __aeInteractWithUserCallback_block_invoke.cold.6
+ __asynchronouslyBootstrapRemoteViewControllerForTouchBarItem_block_invoke.cold.1
+ __asynchronouslyBootstrapRemoteViewControllerForTouchBarItem_block_invoke.cold.2
+ __auxiliaryProxyFor_block_invoke.cold.1
+ __auxiliaryProxyFor_block_invoke.cold.2
+ __auxiliaryProxyFor_block_invoke.cold.3
+ __auxiliaryProxyFor_block_invoke.cold.4
+ __auxiliaryProxyFor_block_invoke.cold.5
+ __auxiliaryProxyFor_block_invoke.cold.6
+ __auxiliaryProxyFor_block_invoke.cold.7
+ __deferBlockOntoMainThread_block_invoke.cold.1
+ __deferBlockOntoMainThread_block_invoke.cold.2
+ __deferBlockOntoMainThread_block_invoke.cold.3
+ __deferBlockOntoMainThread_block_invoke.cold.4
+ __deferBlockOntoMainThread_block_invoke_3.cold.1
+ __deferNSXPCInvocationOntoMainThread_block_invoke.cold.1
+ __fakeEventQueue_block_invoke.cold.1
+ __frameworkBundle_block_invoke.cold.1
+ __hostAppListener_block_invoke.cold.1
+ __hostAppListener_block_invoke.cold.2
+ __hostAppListener_block_invoke.cold.3
+ __hostWindowClassFromWindowBase_block_invoke.cold.1
+ __hostWindowClassFromWindowBase_block_invoke.cold.2
+ __hostWindowClassFromWindowBase_block_invoke.cold.3
+ __ignoreSubclass_block_invoke.cold.1
+ __inputMethodKitUsesXPC_block_invoke.cold.1
+ __inputMethodKitUsesXPC_block_invoke.cold.2
+ __remoteViewForServiceViewControllerIdentifier_block_invoke.cold.1
+ __runLoopModes_block_invoke.cold.1
+ __runLoopModes_block_invoke.cold.2
+ __sendEventToApplicationBypassingSubclasses_block_invoke.cold.1
+ __sendEventToApplicationBypassingSubclasses_block_invoke.cold.2
+ __vbAfterClientError_block_invoke.cold.1
+ __wakeUpMainRunLoop_block_invoke.cold.1
+ __wakeUpMainRunLoop_block_invoke.cold.2
+ __wakeUpMainRunLoop_block_invoke.cold.3
+ __wakeUpMainRunLoop_block_invoke.cold.4
+ __withEndpointCache_block_invoke.cold.1
+ __withServicesToCache_block_invoke.cold.1
+ __xpc_event_handler_no_catch_block_invoke.cold.1
+ __xpc_event_handler_no_catch_block_invoke.cold.2
+ _auxiliaryProxyForAttempting.cold.1
+ _ensureAuxServiceAwareOfHostApp.cold.1
+ _objc_msgSend$_setApplicationTerminationBehaviorWhenModal:
+ accessibilityChildTokens.cold.1
+ accessibilityChildTokens.cold.2
+ accessibilityChildTokens.cold.3
+ associateMouseAndMouseCursorPosition.cold.1
+ associateMouseAndMouseCursorPosition.cold.2
+ auxiliaryProxyFor.cold.1
+ auxiliaryProxyFor.cold.2
+ bundleInfoIsInputMethod.cold.1
+ callStackSymbolsWithoutAddresses.cold.1
+ callStackSymbolsWithoutAddresses.cold.2
+ callStackSymbolsWithoutAddresses.cold.3
+ callStackSymbolsWithoutAddresses.cold.4
+ changeActuallyHasNewValue.cold.1
+ changeActuallyHasNewValue.cold.2
+ changeActuallyHasNewValue.cold.3
+ classIsKindOfClass.cold.1
+ classIsKindOfClass.cold.2
+ controllerForWindow.cold.1
+ copyValueForEntitlement.cold.1
+ createError.cold.1
+ createError.cold.2
+ createError.cold.3
+ createErrorWithDebugDescription.cold.1
+ createErrorWithDebugDescription.cold.2
+ createErrorWithDebugDescription.cold.3
+ createErrorWithDebugDescription.cold.4
+ createErrorWithServiceAndListener.cold.1
+ createErrorWithServiceAndListener.cold.2
+ createErrorWithServiceAndListener.cold.3
+ createErrorWithServiceAndListener.cold.4
+ deferBlockOntoMainThread.cold.1
+ deferNSXPCInvocationOntoMainThread.cold.1
+ describeCGError.cold.1
+ describeException.cold.1
+ describeException.cold.2
+ describeException.cold.3
+ describeException.cold.4
+ endChildSheets.cold.1
+ endpointCacheKey.cold.1
+ ensureTargetIdentifier.cold.1
+ eventsCloseEnough.cold.1
+ eventsCloseEnough.cold.2
+ extractIdentifiersFromDescriptions.cold.1
+ extractIdentifiersFromDescriptions.cold.2
+ extractIdentifiersFromDescriptions.cold.3
+ fakeMouseEvent.cold.1
+ fakeMouseEvent.cold.2
+ fakeMouseEvent.cold.3
+ fakeMouseEvent.cold.4
+ fakeMouseEvent.cold.5
+ flattenEvent.cold.1
+ flattenEvent.cold.2
+ frameworkBundle.cold.1
+ getWindowID.cold.2
+ getWindowID.cold.3
+ hasSecCodeSigningIdentifier.cold.1
+ hostWindowClassFromWindowBase.cold.1
+ hostWindowClassFromWindowBase.cold.2
+ ignoreWindow.cold.1
+ ignoreWindow.cold.2
+ invalidatedDuringBootstrap.cold.1
+ invalidatedDuringBootstrap.cold.2
+ invokeRunLoopInModeForDuration.cold.1
+ invokeRunLoopInModeForDuration.cold.2
+ isCurrentApp.cold.1
+ isCurrentApp.cold.2
+ itemForDescription.cold.1
+ itemForDescription.cold.10
+ itemForDescription.cold.11
+ itemForDescription.cold.12
+ itemForDescription.cold.13
+ itemForDescription.cold.14
+ itemForDescription.cold.15
+ itemForDescription.cold.16
+ itemForDescription.cold.17
+ itemForDescription.cold.2
+ itemForDescription.cold.3
+ itemForDescription.cold.4
+ itemForDescription.cold.5
+ itemForDescription.cold.6
+ itemForDescription.cold.7
+ itemForDescription.cold.8
+ itemForDescription.cold.9
+ lusmFunc.cold.1
+ minimalViewServiceTouchBarControllerIdentifier.cold.1
+ overrideMethod.cold.1
+ overrideMethod.cold.10
+ overrideMethod.cold.2
+ overrideMethod.cold.3
+ overrideMethod.cold.4
+ overrideMethod.cold.5
+ overrideMethod.cold.6
+ overrideMethod.cold.7
+ overrideMethod.cold.8
+ overrideMethod.cold.9
+ postExceptionEventOnAppKitThread.cold.1
+ privateRunLoopMode.cold.1
+ raiseFatalError.cold.1
+ raiseFatalError.cold.2
+ raiseFatalError.cold.3
+ raiseIfNull.cold.1
+ registerAsApplication.cold.1
+ registerAsApplication.cold.10
+ registerAsApplication.cold.11
+ registerAsApplication.cold.2
+ registerAsApplication.cold.3
+ registerAsApplication.cold.4
+ registerAsApplication.cold.5
+ registerAsApplication.cold.6
+ registerAsApplication.cold.7
+ registerAsApplication.cold.8
+ registerAsApplication.cold.9
+ remoteViewForRendezvousWindow.cold.1
+ replyWithError.cold.1
+ responderToPreserve.cold.1
+ restoreKeyboardEventFidelity.cold.1
+ restoreKeyboardEventFidelity.cold.2
+ restoreKeyboardEventFidelity.cold.3
+ runAnimationGroup.cold.1
+ runLoopModes.cold.1
+ runLoopTypeIsAppKit.cold.1
+ runLoopTypeIsAppKit.cold.2
+ runLoopTypeIsAppKit.cold.3
+ runLoopTypeIsAppKit.cold.4
+ runLoopTypeIsAppKit.cold.5
+ runLoopTypeIsAppKit.cold.6
+ runLoopTypeIsAppKit.cold.7
+ runningOnAppKitThread.cold.1
+ secCodeCopyGuestAttributeAuditToken.cold.1
+ secCodeCopyGuestAttributeAuditToken.cold.2
+ sendEventToApplicationBypassingSubclasses.cold.1
+ setWindowStyleMask.cold.1
+ sheetForIdentifier.cold.1
+ sheetForIdentifier.cold.2
+ simulateAppSendEvent.cold.1
+ simulateAppSendEvent.cold.2
+ snapshotWindow.cold.1
+ snapshotWindow.cold.2
+ snapshotWindow.cold.3
+ standardSpaces.cold.1
+ stringResemblesAction.cold.1
+ subclassAndConfigure.cold.1
+ subclassAndConfigure.cold.2
+ subclassAndConfigure.cold.3
+ subclassAndConfigure.cold.4
+ subclassAndConfigure.cold.5
+ subclassAndConfigure.cold.6
+ subclassAndConfigure.cold.7
+ subclassAndConfigure.cold.8
+ swizzle.cold.1
+ swizzle.cold.2
+ templateItemsForDescriptions.cold.1
+ templateItemsForDescriptions.cold.2
+ templateItemsForDescriptions.cold.3
+ unflattenEvent.cold.1
+ unflattenEvent.cold.2
+ vbAfterClientError.cold.1
+ vbBool.cold.1
+ wakeUpMainRunLoop.cold.1
+ wakeUpMainRunLoop.cold.2
+ windowBaseFromServiceWindow.cold.1
+ windowBaseFromServiceWindow.cold.2
+ windowFrameAnimationInProgress.cold.1
+ windowFrameAnimationInProgress.cold.2
+ withHintInProgress.cold.1
+ withHintInProgress.cold.2
+ withImplicitAnimation.cold.1
- __ZGVZ45+[NSPreviewTargetController _windowMayOrder:]E14allowedClasses
- __ZGVZ45+[NSPreviewTargetController _windowMayOrder:]E17disallowedClasses
- __ZGVZ58+[NSPreviewTargetController targetControllerClassForName:]E21sAcceptableClassCache
- __ZGVZL29ViewBridgeAuxiliaryInitializeiPPKcE9sigSource
- __ZNKSt3__16vectorIPU18objcproto8NSObject11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU18objcproto8NSObject11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__13mapIP10objc_classS2_NS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S2_EEEEED1B8ne180100Ev
- __ZNSt3__13setIP10objc_classNS_4lessIS2_EENS_9allocatorIS2_EEED1B8ne180100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZ45+[NSPreviewTargetController _windowMayOrder:]E14allowedClasses
- __ZZ45+[NSPreviewTargetController _windowMayOrder:]E17disallowedClasses
- __ZZ58+[NSPreviewTargetController targetControllerClassForName:]E21sAcceptableClassCache
- __ZZL29ViewBridgeAuxiliaryInitializeiPPKcE9sigSource
- _strcmp
- _strncmp
- inputMethodKitUsesXPC.once
- inputMethodKitUsesXPC.result
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_AnimationFencingSupport.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_QueueingProxy.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_ViewServiceImplicitAnimationCoding.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_ViewServiceUIBehaviorProxy.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_ViewServiceXPCMachSendRight.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSCFRunLoopSemaphore.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSPreviewHostViewController.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSPreviewTargetController.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSRemoteView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSRemoteViewController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSRendezvousWindowController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSServiceViewController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSServiceViewController.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSVBKeyboardEventSpecification.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSVBNamedFault.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSViewBridge.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSViewServiceApplication.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSViewServiceMarshal.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSViewServiceMarshal.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/UINSServiceViewController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/VBXPCConnection.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/VBXPCConnectionFenced.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeAccessoryViewSupport.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeAuxiliary/ViewBridgeAuxiliary.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeIllegalSubclass.i"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeLogging.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeTouchBars.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeUtilities.m"
+ "_applicationTerminationBehaviorWhenModal"
+ "_setApplicationTerminationBehaviorWhenModal:"
- "(bogus value)"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_AnimationFencingSupport.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_QueueingProxy.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_ViewServiceImplicitAnimationCoding.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_ViewServiceUIBehaviorProxy.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/AnimationFencing/NSVB_ViewServiceXPCMachSendRight.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSCFRunLoopSemaphore.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSPreviewHostViewController.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSPreviewTargetController.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSRemoteView.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSRemoteViewController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSRendezvousWindowController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSServiceViewController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSServiceViewController.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSVBKeyboardEventSpecification.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSVBNamedFault.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSViewBridge.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSViewServiceApplication.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSViewServiceMarshal.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/NSViewServiceMarshal.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/UINSServiceViewController.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/VBXPCConnection.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/VBXPCConnectionFenced.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeAccessoryViewSupport.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeAuxiliary/ViewBridgeAuxiliary.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeIllegalSubclass.i"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeLogging.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeTouchBars.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ViewBridge/ViewBridgeUtilities.m"
- "preventsApplicationTerminationWhenModal"
- "v"

```
