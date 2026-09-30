## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-215.13.2.0.0
-  __TEXT.__text: 0x275188
-  __TEXT.__auth_stubs: 0x1f30
-  __TEXT.__objc_methlist: 0x4874
-  __TEXT.__cstring: 0x3c3bc
+215.16.1.0.0
+  __TEXT.__text: 0x2770c0
+  __TEXT.__auth_stubs: 0x1f50
+  __TEXT.__objc_methlist: 0x491c
+  __TEXT.__cstring: 0x3c636
   __TEXT.__const: 0x1ad8
-  __TEXT.__gcc_except_tab: 0x2310
-  __TEXT.__oslogstring: 0x5b1a7
+  __TEXT.__gcc_except_tab: 0x23b8
+  __TEXT.__oslogstring: 0x5b4f2
   __TEXT.__dlopen_cstrs: 0x5bd
   __TEXT.__unwind_info: 0x43e0
-  __TEXT.__objc_classname: 0x506
-  __TEXT.__objc_methname: 0x12a88
-  __TEXT.__objc_methtype: 0x1c5d
-  __TEXT.__objc_stubs: 0xb760
-  __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__const: 0x64c0
-  __DATA_CONST.__objc_classlist: 0x168
+  __TEXT.__objc_classname: 0x51c
+  __TEXT.__objc_methname: 0x12ce7
+  __TEXT.__objc_methtype: 0x1cdc
+  __TEXT.__objc_stubs: 0xb900
+  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__const: 0x6510
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3160
-  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_selrefs: 0x31c8
+  __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xfb0
+  __AUTH_CONST.__auth_got: 0xfc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3b18
-  __AUTH_CONST.__cfstring: 0x17a40
-  __AUTH_CONST.__objc_const: 0x7e90
+  __AUTH_CONST.__const: 0x3b38
+  __AUTH_CONST.__cfstring: 0x17aa0
+  __AUTH_CONST.__objc_const: 0x8020
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x500
+  __AUTH.__objc_data: 0x550
   __AUTH.__data: 0x510
-  __DATA.__objc_ivar: 0x758
+  __DATA.__objc_ivar: 0x76c
   __DATA.__data: 0xf0c
   __DATA.__bss: 0x1918
-  __DATA.__common: 0x5c8
+  __DATA.__common: 0x598
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x1a8
-  __DATA_DIRTY.__common: 0x60
+  __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5401
-  Symbols:   7929
-  CStrings:  14014
+  Functions: 5422
+  Symbols:   7953
+  CStrings:  14065
 
Symbols:
+ _FigCFNumberGetUInt32
+ _OBJC_CLASS_$_NSPredicate
+ _kFigRoutingContextProperty_IsContextPrewarmed
+ _objc_setProperty_atomic_copy
CStrings:
+ "+[MXSystemController(InternalUse) isAppAllowedToInitiatePlayback:]"
+ "-FigRoutingContext- %!s(MISSING): Setting prewarming state: %!{(MISSING)BOOL}u"
+ "-MXPrewarmedChannel- %!s(MISSING): (%!p(MISSING)) Called routingContextUUID %!{(MISSING)public}@"
+ "-MXPrewarmedChannel- %!s(MISSING): Called (%!p(MISSING))"
+ "-MXRoutingContextController- %!s(MISSING): Called"
+ "-MXRoutingContextController- %!s(MISSING): Called with result %!{(MISSING)public}@"
+ "-MXRoutingContextController- %!s(MISSING): Called. Need to deactivate the prewarmed channel."
+ "-MXRoutingContextController- %!s(MISSING): Called. routeUUIDs: %!{(MISSING)public}@."
+ "-MXRoutingContextController- %!s(MISSING): Failed to find all route descriptors"
+ "-MXRoutingContextController- %!s(MISSING): Persisting prewarming to the system."
+ "-MXRoutingContextController- %!s(MISSING): Prewarm failed! Didn't find all the route descriptors."
+ "-MXRoutingContextController- %!s(MISSING): Time out occured when discovering route descriptors"
+ "-MXSystemController- %!s(MISSING): '%!@(MISSING)' '%!s(MISSING)' allowed to initiate Playback"
+ "-MXSystemController- %!s(MISSING): appBundleID cannot be nil!"
+ "-[MXRoutingContextController discoverRouteDescriptorsWithRouteUUIDS:forDiscoverer:]"
+ "-[MXRoutingContextController prewarmRoutesWithUUIDs:completionHandler:]"
+ "-[MXRoutingContextController selectRouteDescriptors:]"
+ "-[MXRoutingPrewarmingChannel dealloc]"
+ "-[MXRoutingPrewarmingChannel initWithRoutingContextUUID:endpoint:previousRouteDescriptors:]"
+ "22:32:56"
+ "@32@0:8@16^{OpaqueFigRouteDiscoverer=}24"
+ "@40@0:8@16^{OpaqueFigEndpoint=}24@32"
+ "@?16@0:8"
+ "B24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "BackgroundRunning"
+ "BackgroundTaskSuspended"
+ "CompletionHandler"
+ "ForegroundRunning"
+ "MXRoutingContextController"
+ "MXRoutingContextControllerModificationCallback"
+ "MXRoutingContextControllerModificationCallback_block_invoke"
+ "MXRoutingPrewarmingChannel"
+ "Oct 23 2024"
+ "PreviousRouteDescriptors"
+ "ReceiverDeviceIsPlaying"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,N,V_previousRouteDescriptors"
+ "T@\"NSString\",R,N,V_routingContextUUID"
+ "T@?,C,V_closeChannelBlock"
+ "T@?,C,V_persistPrewarmingBlock"
+ "TB,N,GisContextPrewarmed"
+ "T^{OpaqueFigEndpoint=},R,N,V_endpoint"
+ "^{OpaqueFigRoutingContext=}"
+ "_closeChannelBlock"
+ "_persistPrewarmingBlock"
+ "_previousRouteDescriptors"
+ "closeChannel"
+ "closeChannelBlock"
+ "contextPrewarmed"
+ "currentRoutes"
+ "discoverRouteDescriptorsWithRouteUUIDS:forDiscoverer:"
+ "filteredArrayUsingPredicate:"
+ "initWithRoutingContextUUID:"
+ "initWithRoutingContextUUID:endpoint:previousRouteDescriptors:"
+ "isContextPrewarmed"
+ "mDiscovererType"
+ "mRoutingContext"
+ "persistChannel"
+ "persistPrewarmingBlock"
+ "predicateWithBlock:"
+ "previousRouteDescriptors"
+ "prewarmRoutesWithUUIDs:completionHandler:"
+ "routeDescriptorsWithRouteIDs:discoverer:"
+ "selectRouteDescriptors:"
+ "setCloseChannelBlock:"
+ "setContextPrewarmed:"
+ "setPersistPrewarmingBlock:"
+ "signal"
+ "v24@0:8@?16"
- "(really) Unknown"
- "13:34:40"
- "Background Running"
- "Background Suspended"
- "Foreground Running"
- "MXPredictedRoutesForSystemMusic"
- "Oct 16 2024"
- "T@\"NSMutableArray\",&,V_routeUUIDs"
- "T@\"NSString\",&,V_userInitiatedAppBundleID"
- "Tq,V_origin"
- "Unknown (daemon)"
- "_origin"
- "_routeUUIDs"
- "_userInitiatedAppBundleID"
- "origin"
- "routeUUIDs"
- "setOrigin:"
- "setRouteUUIDs:"
- "setUserInitiatedAppBundleID:"
- "userInitiatedAppBundleID"

```
