## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience`

```diff

-360.75.1.0.0
-  __TEXT.__text: 0x98c74
+385.10.5.1.0
+  __TEXT.__text: 0x9b140
   __TEXT.__delay_helper: 0xdc
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0x1e3c
+  __TEXT.__objc_methlist: 0x1e54
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x11f96
-  __TEXT.__oslogstring: 0xfacb
-  __TEXT.__gcc_except_tab: 0x1068
-  __TEXT.__dlopen_cstrs: 0x1bc
-  __TEXT.__unwind_info: 0x1b30
+  __TEXT.__cstring: 0x1220b
+  __TEXT.__oslogstring: 0x10564
+  __TEXT.__gcc_except_tab: 0x10c4
+  __TEXT.__dlopen_cstrs: 0x16e
+  __TEXT.__unwind_info: 0x1b70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2750
+  __DATA_CONST.__const: 0x2738
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13c8
+  __DATA_CONST.__objc_selrefs: 0x1400
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x7f0
-  __AUTH_CONST.__const: 0x2410
-  __AUTH_CONST.__cfstring: 0xade0
-  __AUTH_CONST.__objc_const: 0x3348
+  __DATA_CONST.__got: 0x818
+  __AUTH_CONST.__const: 0x2460
+  __AUTH_CONST.__cfstring: 0xae00
+  __AUTH_CONST.__objc_const: 0x3378
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x488
-  __DATA.__objc_ivar: 0x2bc
+  __AUTH.__objc_data: 0x438
+  __DATA.__objc_ivar: 0x2c0
   __DATA.__data: 0x3b4
-  __DATA.__bss: 0x420
+  __DATA.__bss: 0x408
   __DATA.__common: 0x1d0
-  __DATA_DIRTY.__objc_data: 0x528
+  __DATA_DIRTY.__objc_data: 0x578
   __DATA_DIRTY.__bss: 0x6fc
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/Versions/A/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/TimeSync.framework/Versions/A/TimeSync
   - /System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2776
-  Symbols:   5273
-  CStrings:  2931
+  Functions: 2801
+  Symbols:   5296
+  CStrings:  2973
 
Symbols:
+ -[MXCoreSessionBase preferredOutputSampleRate]
+ -[MXCoreSessionBase setPreferredOutputSampleRate:]
+ FigRoutingManagerContextUtilities_ClearPersistedNANRouteInfo
+ FigRoutingManagerContextUtilities_CopyPersistedNANRouteInfo
+ FigRoutingManagerContextUtilities_SetPersistedNANRouteInfo
+ GCC_except_table226
+ GCC_except_table31
+ MX_FeatureFlags_AreMacNANRouteEnhancementsEnabled
+ MX_FeatureFlags_AreMacNANRouteEnhancementsEnabled.areMacNANRouteEnhancementsEnabled
+ MX_FeatureFlags_AreMacNANRouteEnhancementsEnabled.onceToken
+ OBJC_IVAR_$_MXCoreSessionBase._preferredOutputSampleRate
+ _CFStringCompare
+ _FigRoutingManagerContextUtilities_ClearPersistedNANRouteInfo
+ _FigRoutingManagerContextUtilities_CopyPersistedNANRouteInfo
+ _FigRoutingManagerContextUtilities_SetPersistedNANRouteInfo
+ _FigRoutingManagerCopyNANEndpointFromPickedEndpoints
+ _FigRoutingManagerIsNANEndpointPresentInPickedEndpoints
+ _MX_FeatureFlags_AreMacNANRouteEnhancementsEnabled
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_SLSDisplaySyncSessionClient
+ _OUTLINED_FUNCTION_56
+ ___FigRoutingManagerContextUtilities_ClearPersistedNANRouteInfo_block_invoke
+ ___FigRoutingManagerContextUtilities_CopyPersistedNANRouteInfo_block_invoke
+ ___FigRoutingManagerContextUtilities_SetPersistedNANRouteInfo_block_invoke
+ ___MX_FeatureFlags_AreMacNANRouteEnhancementsEnabled_block_invoke
+ ___block_descriptor_64_e8_32o40r_e24_v16?0"NSNotification"8l
+ ___routingManager_waitForRouteDiscovery_block_invoke
+ __routingManager_endpointUIAgentEventCallback_block_invoke
+ _kSLSDisplaySyncSessionNotificationInitialized
+ _kSLSDisplaySyncSessionNotificationStarted
+ _kSLSDisplaySyncSessionUUID
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$setMaxConcurrentOperationCount:
+ _objc_msgSend$setName:
+ _objc_msgSend$signal
+ _objc_msgSend$unregisterNotification
+ _objc_msgSend$waitUntilDate:
+ _routingContextUtilities_clearPersistedNANRouteUID
+ _routingContextUtilities_copyEndpointID
+ _routingContextUtilities_copyEndpointName
+ _routingManager_saveNANRouteIfApplicable
- GCC_except_table39
- GCC_except_table61
- SkyLightLibraryCore.frameworkLibrary
- _SkyLightLibrary
- _SkyLightLibraryCore
- __47-[MXSessionManager initializeDisplaySyncClient]_block_invoke
- ___SkyLightLibraryCore_block_invoke
- ___getSLSDisplaySyncSessionClientClass_block_invoke
- ___getkSLSDisplaySyncSessionNotificationInitializedSymbolLoc_block_invoke
- ___getkSLSDisplaySyncSessionNotificationStartedSymbolLoc_block_invoke
- ___getkSLSDisplaySyncSessionUUIDSymbolLoc_block_invoke
- __getSLSDisplaySyncSessionClientClass_block_invoke
- _audit_stringSkyLight
- _objc_msgSend$unregisterNotificationBlocks
- getSLSDisplaySyncSessionClientClass.softClass
- getkSLSDisplaySyncSessionNotificationInitializedSymbolLoc.ptr
- getkSLSDisplaySyncSessionNotificationStartedSymbolLoc.ptr
- getkSLSDisplaySyncSessionUUIDSymbolLoc.ptr
CStrings:
+ "-FigEndpointUIAgentHelper- %s: Setting new endpointUIAgent, current cached (%p) "
+ "-FigRoutingManager- %s: Adding a DISSOCIATED endpoint to the aggregate — activation is expected to fail with kFigEndpointError_Dissociated: routeUID=%{public}@, name=%{public}@, endpoint=[%p], routingContextUUID=%{public}@"
+ "-FigRoutingManager- %s: Adding endpoint to the aggregate: routeUID=%{public}@, name=%{public}@, endpoint=[%p], isDissociated=NO, routingContextUUID=%{public}@"
+ "-FigRoutingManagerContextUtilities- %s: Clearing persisted NAN route"
+ "-FigRoutingManagerContextUtilities- %s: Clearing persisted NAN route - UID=%{private}@, Name=%{public}@"
+ "-FigRoutingManagerContextUtilities- %s: Persisting NAN route - UID=%{private}@, Name=%{public}@"
+ "-FigRoutingManager_macOS- %s: Attempting to find Route %{public}@ in discovery"
+ "-FigRoutingManager_macOS- %s: Attempting to restore NAN route - UID=%{private}@, Name=%{public}@"
+ "-FigRoutingManager_macOS- %s: Attempting to restore persisted NAN route - UID=%{private}@, Name=%{public}@"
+ "-FigRoutingManager_macOS- %s: Endpoint with UID %{private}@ (Name: %{public}@) not available from discovery, cannot restore"
+ "-FigRoutingManager_macOS- %s: Endpoint with UID %{public}@ not found in discovery"
+ "-FigRoutingManager_macOS- %s: Expanded subendpoints: IDs=%{private}@, Names=%{public}@"
+ "-FigRoutingManager_macOS- %s: Failed to allocate endpointIDs array"
+ "-FigRoutingManager_macOS- %s: Failed to allocate endpointNames array"
+ "-FigRoutingManager_macOS- %s: Failed to create route discoverer, err=%d"
+ "-FigRoutingManager_macOS- %s: Failed to get system audio context UUID"
+ "-FigRoutingManager_macOS- %s: Found endpoint connected over NAN at index %ld"
+ "-FigRoutingManager_macOS- %s: No NAN endpoint found in picked endpoints"
+ "-FigRoutingManager_macOS- %s: No NAN endpoint to persist"
+ "-FigRoutingManager_macOS- %s: No endpoint connected over NAN found in array of %ld endpoints"
+ "-FigRoutingManager_macOS- %s: No persisted NAN route UID to restore"
+ "-FigRoutingManager_macOS- %s: No picked endpoints to check for NAN"
+ "-FigRoutingManager_macOS- %s: No subendpoints found (subEndpoints = NULL)"
+ "-FigRoutingManager_macOS- %s: Picked endpoints: IDs=%{private}@, Names=%{public}@"
+ "-FigRoutingManager_macOS- %s: Saving NAN route for sleep/wake recovery - UID=%{private}@, Name=%{public}@"
+ "-FigRoutingManager_macOS- %s: Selecting restored NAN route: %{public}@"
+ "-FigRoutingManager_macOS- %s: Successfully discovered endpoint - UID=%{public}@, Name=%{public}@"
+ "-FigRoutingManager_macOS- %s: Timeout occurred when discovering route with UID: %{public}@"
+ "-FigRoutingManager_macOS- %s: endpoints array is empty"
+ "-FigRoutingManager_macOS- %s: endpoints parameter is NULL"
+ "-FigRoutingManager_macOS- %s: routeUID is NULL"
+ "-MX_FeatureFlags- %s: MediaExperience/MacNANRouteEnhancements feature is %{public}s"
+ "00:35:37"
+ "FigRoutingManagerAddEndpointToAggregate"
+ "FigRoutingManagerContextUtilities_ClearPersistedNANRouteInfo"
+ "FigRoutingManagerContextUtilities_ClearPersistedNANRouteInfo_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyPersistedNANRouteInfo"
+ "FigRoutingManagerContextUtilities_SetPersistedNANRouteInfo"
+ "FigRoutingManagerContextUtilities_SetPersistedNANRouteInfo_block_invoke"
+ "FigRoutingManagerCopyNANEndpointFromPickedEndpoints"
+ "MX_FeatureFlags_AreMacNANRouteEnhancementsEnabled_block_invoke"
+ "MacNANRouteEnhancements"
+ "Oct 10 2026"
+ "com.apple.coremedia.macosrouting.discovery"
+ "routingContextUtilities_copyEndpointConnectedOverNAN"
+ "routingContextUtilities_copyEndpointIDs"
+ "routingContextUtilities_copyEndpointNames"
+ "routingManager_discoverAndCopyEndpointWithUID"
+ "routingManager_restoreNANRouteIfApplicable"
+ "routingManager_saveNANRouteIfApplicable"
+ "routingManager_waitForRouteDiscovery"
- "-FigEndpointUIAgentHelper- %s: Setting new endpointUIAgent (%p) old (%p) "
- "/System/Library/PrivateFrameworks/SkyLight.framework/Contents/MacOS/SkyLight"
- "15:46:10"
- "Aug  8 2026"
- "SLSDisplaySyncSessionClient"
- "kSLSDisplaySyncSessionNotificationInitialized"
- "kSLSDisplaySyncSessionNotificationStarted"
- "kSLSDisplaySyncSessionUUID"
- "softlink:o:path:/System/Library/PrivateFrameworks/SkyLight.framework/SkyLight"
```
