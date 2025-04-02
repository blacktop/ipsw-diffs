## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote`

```diff

-4024.540.1.0.0
-  __TEXT.__text: 0x2dc578
+4024.600.5.0.0
+  __TEXT.__text: 0x2dd7a4
   __TEXT.__auth_stubs: 0x13a0
-  __TEXT.__objc_methlist: 0x28424
+  __TEXT.__objc_methlist: 0x2848c
   __TEXT.__const: 0x4f8
-  __TEXT.__cstring: 0x2923b
-  __TEXT.__oslogstring: 0xbb14
-  __TEXT.__gcc_except_tab: 0x5900
+  __TEXT.__cstring: 0x292ea
+  __TEXT.__oslogstring: 0xbc11
+  __TEXT.__gcc_except_tab: 0x5964
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0xa600
-  __TEXT.__objc_classname: 0x4884
-  __TEXT.__objc_methname: 0x468b2
-  __TEXT.__objc_methtype: 0x85f3
-  __TEXT.__objc_stubs: 0x24660
-  __DATA_CONST.__got: 0x1228
-  __DATA_CONST.__const: 0x41b8
+  __TEXT.__unwind_info: 0xa650
+  __TEXT.__objc_classname: 0x4878
+  __TEXT.__objc_methname: 0x46a8a
+  __TEXT.__objc_methtype: 0x864e
+  __TEXT.__objc_stubs: 0x246a0
+  __DATA_CONST.__got: 0x1220
+  __DATA_CONST.__const: 0x41c0
   __DATA_CONST.__objc_classlist: 0x10c8
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x200
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdb98
+  __DATA_CONST.__objc_selrefs: 0xdbb8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xf18
   __DATA_CONST.__objc_arraydata: 0x228
   __AUTH_CONST.__auth_got: 0x9e0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x9410
-  __AUTH_CONST.__cfstring: 0x1fb20
-  __AUTH_CONST.__objc_const: 0x41770
+  __AUTH_CONST.__const: 0x9470
+  __AUTH_CONST.__cfstring: 0x1fc20
+  __AUTH_CONST.__objc_const: 0x41938
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x41a0
-  __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x2f2c
-  __DATA.__data: 0x1850
-  __DATA.__bss: 0xa20
+  __AUTH.__data: 0xe0
+  __DATA.__objc_ivar: 0x2f48
+  __DATA.__data: 0x18b0
+  __DATA.__bss: 0xa30
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x6630
-  __DATA_DIRTY.__data: 0x158
+  __DATA_DIRTY.__data: 0x160
   __DATA_DIRTY.__bss: 0x388
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 19044
-  Symbols:   34740
-  CStrings:  18452
+  Functions: 19065
+  Symbols:   34787
+  CStrings:  18479
 
Symbols:
+ -[MRAVConcreteOutputContext clusterController:clusterTypeDidChange:]
+ -[MRAVConcreteOutputDevice _loadLocalOverridesWithOutputContext:outputDevice:]
+ -[MRAVConcreteOutputDevice initWithAVOutputDevice:outputContext:]
+ -[MRAVConcreteOutputDevice initWithAVOutputDevice:outputContext:].cold.1
+ -[MRAVConcreteOutputDevice initWithAVOutputDevice:sourceInfo:outputContext:]
+ -[MRAVConcreteOutputDevice outputContext]
+ -[MRAVConcreteOutputDevice setOutputContext:]
+ -[MRAVConcreteRoutingDiscoverySession clusterController:clusterTypeDidChange:]
+ -[MRDeviceInfo deviceSubtype]
+ -[MRNowPlayingOriginClientManager clearActiveSystemEndpointsWithReason:]
+ -[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]
+ -[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:].cold.1
+ -[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:].cold.2
+ -[MRNowPlayingOriginClientManager updateActiveSystemEndpointOutputDeviceUID:forType:reason:]
+ -[NSError(MRAdditions) initWithMRError:description:underlyingError:]
+ GCC_except_table45
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._groupContainsGroupLeaderOverride
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._isAirPlayActiveOverride
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._isGroupLeaderOverride
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._isProxyGroupPlayerOverride
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._outputContext
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._parentGroupContainsGroupLeaderOverride
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._parentGroupUIDOverride
+ _AVOutputContextTypeAudioFunction
+ _MRComputeGroupID
+ _MRComputeGroupIDWithDeviceInfo
+ __111-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]_block_invoke.53
+ __111-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]_block_invoke.56
+ __111-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]_block_invoke.cold.1
+ __131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.109
+ __131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.88
+ __131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.88.cold.1
+ __61+[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:]_block_invoke.64
+ __61-[MRAVConcreteRoutingDiscoverySession availableOutputDevices]_block_invoke.13
+ __63-[MRMediaRemoteServiceClient addPlayerPathInvalidationHandler:]_block_invoke.97
+ __65+[MRAVConcreteOutputContext _initializeAVFNotificationForwarding]_block_invoke.129
+ __65+[MRAVConcreteOutputContext _initializeAVFNotificationForwarding]_block_invoke_2.130
+ __96-[MRNowPlayingOriginClientManager resolveActiveSystemEndpointWithType:timeout:queue:completion:]_block_invoke.73
+ __96-[MRNowPlayingOriginClientManager resolveActiveSystemEndpointWithType:timeout:queue:completion:]_block_invoke.75
+ __MRDictionaryCalculateDeltas_block_invoke.511
+ __MRMediaRemoteRequestDeviceUID_block_invoke.425
+ __MRMediaRemoteRequestIsGroupLeader_block_invoke.441
+ __OBJC_$_INSTANCE_METHODS_MRDeviceInfo(MRActiveRoutesObserverAdditions)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MRAVClusterObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MRAVClusterObserver
+ __OBJC_$_PROTOCOL_REFS_MRAVClusterObserver
+ __OBJC_CLASS_PROTOCOLS_$_MRAVConcreteOutputContext
+ __OBJC_CLASS_PROTOCOLS_$_MRAVConcreteRoutingDiscoverySession
+ __OBJC_LABEL_PROTOCOL_$_MRAVClusterObserver
+ __OBJC_PROTOCOL_$_MRAVClusterObserver
+ ___111-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]_block_invoke
+ ___58-[MRAVConcreteOutputContext initWithAVOutputContext:type:]_block_invoke
+ ___61+[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:]_block_invoke_2
+ ___78-[MRAVConcreteOutputDevice _loadLocalOverridesWithOutputContext:outputDevice:]_block_invoke
+ ___78-[MRAVConcreteOutputDevice _loadLocalOverridesWithOutputContext:outputDevice:]_block_invoke_2
+ ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.433
+ ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.433.cold.1
+ ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.434
+ ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8l
+ ___block_descriptor_48_e8_32s40s_e5_B8?0l
+ __block_literal_global.227
+ __block_literal_global.259
+ __block_literal_global.428
+ __block_literal_global.504
+ __block_literal_global.507
+ __block_literal_global.555
+ __block_literal_global.558
+ __block_literal_global.99
+ _constantValAVOutputContextTypeAudio
+ _getAVOutputContextTypeAudio
+ _initValAVOutputContextTypeAudio
+ _objc_msgSend$clearActiveSystemEndpointsWithReason:
+ _objc_msgSend$initWithAVOutputDevice:outputContext:
+ _objc_msgSend$initWithMRError:description:underlyingError:
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$updateActiveSystemEndpointOutputDeviceUID:forType:reason:
+ initValAVOutputContextTypeAudio.cold.1
- -[MRAVConcreteOutputDevice _loadLocalOverrides]
- -[MRAVConcreteOutputDevice initWithAVOutputDevice:sourceInfo:].cold.1
- -[MRDeviceInfo(MRDeviceInfoOutputDeviceAdditions) deviceSubtype]
- -[MRNowPlayingOriginClientManager clearActiveSystemEndpoints]
- -[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:queue:completion:].cold.1
- -[MRNowPlayingOriginClientManager updateActiveSystemEndpointOutputDeviceUID:forType:]
- __101-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:queue:completion:]_block_invoke.51
- __101-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:queue:completion:]_block_invoke.54
- __101-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:queue:completion:]_block_invoke.cold.1
- __131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.101
- __131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.80
- __131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.80.cold.1
- __47-[MRAVConcreteOutputDevice _loadLocalOverrides]_block_invoke.15
- __61-[MRAVConcreteRoutingDiscoverySession availableOutputDevices]_block_invoke.11
- __63-[MRMediaRemoteServiceClient addPlayerPathInvalidationHandler:]_block_invoke.94
- __65+[MRAVConcreteOutputContext _initializeAVFNotificationForwarding]_block_invoke.126
- __65+[MRAVConcreteOutputContext _initializeAVFNotificationForwarding]_block_invoke_2.127
- __96-[MRNowPlayingOriginClientManager resolveActiveSystemEndpointWithType:timeout:queue:completion:]_block_invoke.65
- __96-[MRNowPlayingOriginClientManager resolveActiveSystemEndpointWithType:timeout:queue:completion:]_block_invoke.67
- __MRDictionaryCalculateDeltas_block_invoke.507
- __MRMediaRemoteRequestDeviceUID_block_invoke.422
- __MRMediaRemoteRequestIsGroupLeader_block_invoke.437
- __OBJC_$_INSTANCE_METHODS_MRDeviceInfo(MRActiveRoutesObserverAdditions|MRDeviceInfoOutputDeviceAdditions)
- ___101-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:queue:completion:]_block_invoke
- ___47-[MRAVConcreteOutputDevice _loadLocalOverrides]_block_invoke
- ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.427
- ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.430.cold.1
- ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.431
- __block_literal_global.210
- __block_literal_global.425
- __block_literal_global.500
- __block_literal_global.503
- __block_literal_global.545
- __block_literal_global.548
- _objc_msgSend$clearActiveSystemEndpoints
- _objc_msgSend$setHasIsLocalDevice:
- _objc_msgSend$updateActiveSystemEndpointOutputDeviceUID:forType:
CStrings:
+ "%@+%@"
+ "%@+%@+%@"
+ "AVOutputContextTypeAudio"
+ "MRAVClusterObserver"
+ "MissingNativeGroup"
+ "T@\"AVOutputContext\",W,N,V_outputContext"
+ "[MRAVConcreteOutputDevice] GroupID mismatch: %@ -> %@"
+ "[MRNowPlayingOriginClientManager] %{public}@SystemEndpoint changed from %{public}@ to %{public}@ because %{public}@"
+ "[MRNowPlayingOriginClientManager] Clearing system endpoint UIDs because %{public}@"
+ "_groupContainsGroupLeaderOverride"
+ "_isAirPlayActiveOverride"
+ "_isGroupLeaderOverride"
+ "_isProxyGroupPlayerOverride"
+ "_loadLocalOverridesWithOutputContext:outputDevice:"
+ "_parentGroupContainsGroupLeaderOverride"
+ "_parentGroupUIDOverride"
+ "clearActiveSystemEndpointsWithReason:"
+ "fetching data from server"
+ "handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:"
+ "initWithAVOutputDevice:outputContext:"
+ "initWithAVOutputDevice:sourceInfo:outputContext:"
+ "initWithMRError:description:underlyingError:"
+ "initializing"
+ "received update from server (restoring: %@)"
+ "restore connection"
+ "updateActiveSystemEndpointOutputDeviceUID:forType:reason:"
+ "v28@0:8@\"MRAVClusterController\"16I24"
+ "v32@0:8@\"MRAVClusterController\"16Q24"
+ "v40@0:8@16q24@32"
+ "\xa1"
- "MRDeviceInfoOutputDeviceAdditions"
- "_loadLocalOverrides"
- "clearActiveSystemEndpoints"
- "updateActiveSystemEndpointOutputDeviceUID:forType:"

```
