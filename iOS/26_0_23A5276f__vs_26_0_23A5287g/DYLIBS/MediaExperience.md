## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-270.64.3.0.0
-  __TEXT.__text: 0x2a5ee0
-  __TEXT.__auth_stubs: 0x1ff0
+270.66.2.11.1
+  __TEXT.__text: 0x2a6d8c
+  __TEXT.__auth_stubs: 0x2000
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x5ca4
-  __TEXT.__cstring: 0x4110c
+  __TEXT.__objc_methlist: 0x5d5c
+  __TEXT.__cstring: 0x4128e
   __TEXT.__const: 0x1b58
-  __TEXT.__gcc_except_tab: 0x2cf8
-  __TEXT.__oslogstring: 0x63ddd
+  __TEXT.__gcc_except_tab: 0x2ce0
+  __TEXT.__oslogstring: 0x63f20
   __TEXT.__dlopen_cstrs: 0x5bd
-  __TEXT.__unwind_info: 0x4b00
-  __TEXT.__objc_classname: 0x760
-  __TEXT.__objc_methname: 0x15293
-  __TEXT.__objc_methtype: 0x208e
-  __TEXT.__objc_stubs: 0xd1a0
-  __DATA_CONST.__got: 0xa78
+  __TEXT.__unwind_info: 0x4c58
+  __TEXT.__objc_classname: 0x774
+  __TEXT.__objc_methname: 0x15568
+  __TEXT.__objc_methtype: 0x20b7
+  __TEXT.__objc_stubs: 0xd2c0
+  __DATA_CONST.__got: 0xa80
   __DATA_CONST.__const: 0x6640
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3aa0
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_selrefs: 0x3ae0
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x1010
-  __AUTH_CONST.__const: 0x3e00
-  __AUTH_CONST.__cfstring: 0x18b80
-  __AUTH_CONST.__objc_const: 0x8828
+  __AUTH_CONST.__auth_got: 0x1018
+  __AUTH_CONST.__const: 0x3e20
+  __AUTH_CONST.__cfstring: 0x18ba0
+  __AUTH_CONST.__objc_const: 0x8a68
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xa00
+  __AUTH.__objc_data: 0xa50
   __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x82c
+  __DATA.__objc_ivar: 0x854
   __DATA.__data: 0xfe0
-  __DATA.__bss: 0x18a9
+  __DATA.__bss: 0x18b9
   __DATA.__common: 0x558
   __DATA_DIRTY.__objc_data: 0x960
-  __DATA_DIRTY.__bss: 0x420
+  __DATA_DIRTY.__bss: 0x430
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A9B9F35-6A37-3934-A94A-B9C6C821CB3F
-  Functions: 7389
-  Symbols:   23131
-  CStrings:  18340
+  UUID: 44D0E946-F074-340E-B0C4-FDE15E64194F
+  Functions: 7411
+  Symbols:   23207
+  CStrings:  18375
 
Symbols:
+ +[MXRadiosPreferences sharedInstance]
+ +[MXRadiosPreferences sharedInstance].cold.1
+ -[MXCoreSession(Utilities) getIsPlayingVideoOutput]
+ -[MXRadiosPreferences dealloc]
+ -[MXRadiosPreferences init]
+ -[MXRadiosPreferences isAirplaneModeEnabled]
+ -[MXRoutingContextModificationMetrics currentRouteDescriptors]
+ -[MXRoutingContextModificationMetrics previousRouteDescriptors]
+ -[MXRoutingContextModificationMetrics setCurrentRouteDescriptors:]
+ -[MXRoutingContextModificationMetrics setPreviousRouteDescriptors:]
+ -[MXRoutingContextModificationResult currentRouteDescriptors]
+ -[MXRoutingContextModificationResult initWithRouteConfigUpdatedReason:modificationMetrics:previousRouteDescriptors:currentRouteDescriptors:]
+ -[MXRoutingContextModificationResult previousRouteDescriptors]
+ -[MXSessionManager resumeNowPlayingAppForCarPlay]
+ -[MXSessionManager setShouldResumeNowPlayingAppOnDelayedCarPlayPortPublication:]
+ -[MXSessionManager shouldResumeNowPlayingAppOnDelayedCarPlayPortPublication]
+ -[MXSessionManager updateNowPlayingAppShouldResumeForCarPlay:]
+ _CFAutorelease
+ _FigEndpointDescriptorUtility_AreRouteDescriptorsOfTypeAirPlay
+ _FigEndpointDescriptorUtility_AreRouteIDsTheSame
+ _OBJC_CLASS_$_MXRadiosPreferences
+ _OBJC_CLASS_$_RadiosPreferences
+ _OBJC_IVAR_$_MXRadiosPreferences.mRadiosPreferences
+ _OBJC_IVAR_$_MXRadiosPreferences.mSerialQueue
+ _OBJC_IVAR_$_MXRoutingContextCallbackHelper.mCurrentRouteDescriptors
+ _OBJC_IVAR_$_MXRoutingContextCallbackHelper.mFigRoutingContext
+ _OBJC_IVAR_$_MXRoutingContextCallbackHelper.mPreviousRouteDescriptors
+ _OBJC_IVAR_$_MXRoutingContextModificationMetrics._currentRouteDescriptors
+ _OBJC_IVAR_$_MXRoutingContextModificationMetrics._previousRouteDescriptors
+ _OBJC_IVAR_$_MXRoutingContextModificationResult._currentRouteDescriptors
+ _OBJC_IVAR_$_MXRoutingContextModificationResult._previousRouteDescriptors
+ _OBJC_IVAR_$_MXSessionManager._shouldResumeNowPlayingAppOnDelayedCarPlayPortPublication
+ _OBJC_METACLASS_$_MXRadiosPreferences
+ __OBJC_$_CLASS_METHODS_MXRadiosPreferences
+ __OBJC_$_INSTANCE_METHODS_MXRadiosPreferences
+ __OBJC_$_INSTANCE_VARIABLES_MXRadiosPreferences
+ __OBJC_$_PROP_LIST_MXRadiosPreferences
+ __OBJC_CLASS_RO_$_MXRadiosPreferences
+ __OBJC_METACLASS_RO_$_MXRadiosPreferences
+ ___37+[MXRadiosPreferences sharedInstance]_block_invoke
+ ___44-[MXRadiosPreferences isAirplaneModeEnabled]_block_invoke
+ ___62-[MX_BannerManager promptUserResponseForRoute:connectHandler:]_block_invoke.101
+ ___FigRouteDiscoveryManagerStoreDiscoverer_block_invoke
+ ___FigRouteDiscoveryManagerStoreDiscoverer_block_invoke_2
+ ___block_literal_global.127
+ ___block_literal_global.181
+ ___block_literal_global.68
+ ___block_literal_global.77
+ ___block_literal_global.82
+ ___discoverer_SetProperty_block_invoke_2.56
+ _discoveryManager_getSharedSerializationQueue.sharedSerializationQueue
+ _figRouteDiscovererRemoteXPC_EnsureClientEstablished.clientCallbacks
+ _figRouteDiscovererRemoteXPC_EnsureClientEstablished.lock
+ _objc_msgSend$airplaneMode
+ _objc_msgSend$currentRouteDescriptors
+ _objc_msgSend$initWithRouteConfigUpdatedReason:modificationMetrics:previousRouteDescriptors:currentRouteDescriptors:
+ _objc_msgSend$isAirplaneModeEnabled
+ _objc_msgSend$previousRouteDescriptors
+ _objc_msgSend$resumeNowPlayingAppForCarPlay
+ _objc_msgSend$setCurrentRouteDescriptors:
+ _objc_msgSend$setPreviousRouteDescriptors:
+ _objc_msgSend$setShouldResumeNowPlayingAppOnDelayedCarPlayPortPublication:
+ _objc_msgSend$shouldResumeNowPlayingAppOnDelayedCarPlayPortPublication
+ _objc_msgSend$updateNowPlayingAppShouldResumeForCarPlay:
+ _vaeTakeOwnershipForSelectedPortIfRequired
+ _vaemIsPortPresentInConnectedInputPorts
- -[MXRoutingContextModificationResult initWithRouteConfigUpdatedReason:modificationMetrics:]
- -[MXSessionManager nowPlayingAppShouldResumeForCarPlay:]
- GCC_except_table55
- ___62-[MX_BannerManager promptUserResponseForRoute:connectHandler:]_block_invoke.100
- ___78-[MX_DeviceManagementPolicyDidChangeObserver deviceManagementPolicyDidChange:]_block_invoke_2
- ___FigRouteDiscovererCreate_block_invoke
- ___block_literal_global.115
- ___block_literal_global.129
- ___block_literal_global.185
- ___discoverer_SetProperty_block_invoke_2.57
- ___routingContext_CopyPredictedSelectedRouteDescriptor_block_invoke
- ___routingContext_CopyPredictedSelectedRouteDescriptor_block_invoke.45
- _kFigRouteDiscovererNotification_ServerConnectionDied_block_invoke.clientCallbacks
- _objc_msgSend$initWithRouteConfigUpdatedReason:modificationMetrics:
- _objc_msgSend$nowPlayingAppShouldResumeForCarPlay:
CStrings:
+ "-CMVAEndpoint- %s: Failed to make ports %{public}@ routable for port %u, userPickedRoute=%{BOOL}u, routingContextUUID=%{public}@"
+ "-CMVAEndpoint- %s: Failed to take ownership for port %u, userPickedRoute=%{BOOL}u, routingContextUUID=%{public}@"
+ "-CMVAEndpoint- %s: Not requesting ownership for port %d for reason=%{public}@ because port is not present in connected input or output ports."
+ "-CMVAEndpoint- %s: Took ownership for %{public}@ ports for port %u, userPickedRoute=%{BOOL}u, routingContextUUID=%{public}@"
+ "-CMVAEndptUtl- %s: Not resuming Now Playing app because carIsOnPhoneCall = %{BOOL}u, carIsDoingSpeech = %{BOOL}u "
+ "-CMVAEndptUtl- %s: shouldAutoRoute = false for port %u due to portType equal to %u"
+ "-MXCoreSessionUtilities- %s: IsPortManaged: %{BOOL}u, port = %u"
+ "-MXCoreSessionUtilities- %s: Port %u is not in-ear, not routing."
+ "-MXRoutingContextReportingService- %s: Skip reporting because currentRouteAirPlay: %{BOOL}u, routeDescriptorsTheSame: %{BOOL}u"
+ "-[MXCoreSession(Utilities) userPreferredInputPortIsBluetoothManagedAndHighQuality]"
+ "-[MXRadiosPreferences isAirplaneModeEnabled]"
+ "-[MXRoutingContextReportingService initWithModificationMetrics:useMockService:]"
+ "-[MXSessionManager resumeNowPlayingAppForCarPlay]"
+ "-[MXSessionManager updateNowPlayingAppShouldResumeForCarPlay:]"
+ "21:16:35"
+ "@\"RadiosPreferences\""
+ "@48@0:8@16@24@32@40"
+ "CurrentRouteDescriptors"
+ "FigRouteDiscoveryManagerStoreDiscoverer"
+ "FigRouteDiscoveryManagerStoreDiscoverer_block_invoke"
+ "FigRouteDiscoveryManagerStoreDiscoverer_block_invoke_2"
+ "HistoricalAudio"
+ "Jul  1 2025"
+ "MXRadiosPreferences"
+ "MX_RadiosPreferences.m"
+ "Route Discoverer Remote Client creation failed."
+ "T@\"NSArray\",&,V_currentRouteDescriptors"
+ "T@\"NSArray\",&,V_previousRouteDescriptors"
+ "T@\"NSArray\",R,&,N,V_currentRouteDescriptors"
+ "T@\"NSArray\",R,&,N,V_previousRouteDescriptors"
+ "TB,N,V_shouldResumeNowPlayingAppOnDelayedCarPlayPortPublication"
+ "_currentRouteDescriptors"
+ "_shouldResumeNowPlayingAppOnDelayedCarPlayPortPublication"
+ "airplaneMode"
+ "com.apple.mediaexperience.RadiosPreferences"
+ "currentRouteDescriptors"
+ "figRouteDiscovererRemoteXPC_EnsureClientEstablished"
+ "initWithRouteConfigUpdatedReason:modificationMetrics:previousRouteDescriptors:currentRouteDescriptors:"
+ "isAirplaneModeEnabled"
+ "mCurrentRouteDescriptors"
+ "mFigRoutingContext"
+ "mPreviousRouteDescriptors"
+ "mRadiosPreferences"
+ "resumeNowPlayingAppForCarPlay"
+ "setCurrentRouteDescriptors:"
+ "setPreviousRouteDescriptors:"
+ "setShouldResumeNowPlayingAppOnDelayedCarPlayPortPublication:"
+ "shouldResumeNowPlayingAppOnDelayedCarPlayPortPublication"
+ "updateNowPlayingAppShouldResumeForCarPlay:"
+ "vaeTakeOwnershipForSelectedPortIfRequired"
- "-CMSMDevState- %s: Airplane mode enabled: %{public}s"
- "-CMVAEndpoint- %s: Not requesting ownership for port %d for reason=%{public}@ because port is not present in connected output ports."
- "-CMVAEndptUtl- %s: shouldAutoRoute = false for port %u due to portType equal to %d"
- "-FigRouteDiscovererXPCRemote- %s:  Endpoint Discoverer Remote Client created %d"
- "-MXCoreSessionUtilities- %s: Port %u for session %{public}@ is Smart-Routing capable, allowing SR to proceed normally and returning nil."
- "-MXCoreSessionUtilities- %s: User preferred input port %u for %{public}@ is Bluetooth microphone, isWirelessConnection=%{BOOL}u, isPortManaged=%{BOOL}u"
- "-[MXSessionManager nowPlayingAppShouldResumeForCarPlay:]"
- "-[MX_DeviceManagementPolicyDidChangeObserver deviceManagementPolicyDidChange:]_block_invoke_2"
- "00:10:36"
- "AirplaneMode"
- "CMSMDeviceState_IsAirplaneModeEnabled"
- "Jun 14 2025"
- "figRouteDiscovererRemoteXPC_EnsureClientEstablished_block_invoke"
- "initWithRouteConfigUpdatedReason:modificationMetrics:"
- "nowPlayingAppShouldResumeForCarPlay:"
- "routingContext_CopyPredictedSelectedRouteDescriptor_block_invoke"

```
