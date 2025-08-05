## mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

-4025.100.108.0.0
-  __TEXT.__text: 0x396c08
-  __TEXT.__auth_stubs: 0x6020
-  __TEXT.__objc_stubs: 0x23a80
-  __TEXT.__objc_methlist: 0x141fc
-  __TEXT.__objc_methname: 0x389ec
-  __TEXT.__cstring: 0x1ccab
-  __TEXT.__objc_classname: 0x2caa
-  __TEXT.__objc_methtype: 0x6bca
+4025.100.115.1.0
+  __TEXT.__text: 0x398f7c
+  __TEXT.__auth_stubs: 0x6040
+  __TEXT.__objc_stubs: 0x23bc0
+  __TEXT.__objc_methlist: 0x14244
+  __TEXT.__objc_methname: 0x38c17
+  __TEXT.__cstring: 0x1cf7b
+  __TEXT.__objc_classname: 0x2cab
+  __TEXT.__objc_methtype: 0x6bfe
   __TEXT.__const: 0xc474
-  __TEXT.__gcc_except_tab: 0x6374
-  __TEXT.__oslogstring: 0x22029
+  __TEXT.__gcc_except_tab: 0x6384
+  __TEXT.__oslogstring: 0x22049
   __TEXT.__dlopen_cstrs: 0x224
   __TEXT.__swift5_typeref: 0x4b6d
   __TEXT.__swift5_capture: 0x4d14

   __TEXT.__swift5_proto: 0x838
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x58
-  __TEXT.__unwind_info: 0xb3c8
+  __TEXT.__unwind_info: 0xb3d8
   __TEXT.__eh_frame: 0x6024
-  __DATA_CONST.__auth_got: 0x3020
-  __DATA_CONST.__got: 0x2ba0
+  __DATA_CONST.__auth_got: 0x3030
+  __DATA_CONST.__got: 0x2ba8
   __DATA_CONST.__auth_ptr: 0xc38
-  __DATA_CONST.__const: 0x1a4a8
-  __DATA_CONST.__cfstring: 0xd4c0
+  __DATA_CONST.__const: 0x1a510
+  __DATA_CONST.__cfstring: 0xd720
   __DATA_CONST.__objc_classlist: 0x9f8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x5a8

   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0x24de8
-  __DATA.__objc_selrefs: 0xb558
-  __DATA.__objc_ivar: 0x1604
+  __DATA.__objc_const: 0x24e48
+  __DATA.__objc_selrefs: 0xb5b8
+  __DATA.__objc_ivar: 0x160c
   __DATA.__objc_data: 0x8b18
   __DATA.__data: 0xa990
   __DATA.__bss: 0xea30

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 287F449E-8C5B-3E21-8FDB-BC4DE38F0E03
-  Functions: 15911
-  Symbols:   3222
-  CStrings:  16096
+  UUID: 91223ADB-979C-3AA4-9F75-B43C363D5B37
+  Functions: 15929
+  Symbols:   3226
+  CStrings:  16159
 
Symbols:
+ _$s12MediaControl14RoutingSessionV8HostInfoV010isPersonalE0Sbvg
+ _$s12MediaControl14RoutingSessionV8HostInfoV4name10symbolName07productI0015isVisibleSilentE00k8PersonalE0AESS_S2SSgS2btcfC
+ _$s12MediaControl14RoutingSessionV8HostInfoV4name10symbolName07productI0015isVisibleSilentE00k8PersonalE0AESS_S2SSgS2btcfcfA3_
+ _$s12MediaControl22RoutingSessionSnapshotV14activeSessions08inactiveG00fD0ACSayAA0cD0VG_AiHSgtcfC
+ _MRMediaRemoteEndpointFeaturesDescription
+ _OBJC_CLASS_$_MRRollingWindowActivityTracker
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
- _$s12MediaControl14RoutingSessionV8HostInfoV4name10symbolName07productI0015isVisibleSilentE0AESS_S2SSgSbtcfC
- _$s12MediaControl22RoutingSessionSnapshotV8sessions06activeD0ACSayAA0cD0VG_AGSgtcfC
- _MRProcessIsMediaServerDaemon
CStrings:
+ "  discoveryTracker=%@\n"
+ "%@ %p {\n    effective discovery mode = %@, %@\n    desired discovery mode = %@, %@\n    xpc connection = %@\n    pid = %d\n    bundle id = %@\n    isProcessSuspended = %u\n    discoveryTracker = %@\n    connection monitor = %@\n}"
+ "%@ : %@"
+ "@\"<MRActivityTracker>\""
+ "@\"<MRDGroupSessionListenerDelegate>\""
+ "@\"MRDFastSyncGroupSessionParticipant\""
+ "@\"MRIRRouteRecommendationCandidate\""
+ "@\"NSString\"24@?0@\"NSString\"8@\"MRAVConcreteOutputContext\"16"
+ "AirPlay -> UGLEndpoint"
+ "Builtin + Remove -> UGLEndpoint"
+ "C"
+ "Direct.%@"
+ "Duplicate %@"
+ "Hosted.%@"
+ "Not AirPlay -> LocalEndpoint"
+ "OutputContextManager"
+ "T@\"<MRActivityTracker>\",&,N,V_discoveryTracker"
+ "[%s] Item: %{public}s, selected in local session, is .remoteControllable, has handoff content, existing containing session -> .handoff"
+ "[%s] Item: %{public}s, selected in local session, is .remoteControllable, has handoff content, existing containing session, push disabled -> .set"
+ "[%s] Item: %{public}s, selected in local session, is .remoteControllable, has handoff content, no existing containing session -> .handoff"
+ "[%s] Item: %{public}s, selected in local session, is .remoteControllable, has no handoff content -> .set"
+ "[%s] Item: %{public}s, selected in local session, is .remoteControllable, publisher does not support handoff -> .set"
+ "[%s] reloadSnapshot - reload for: %{public}s"
+ "[%s] reloadSnapshot - skip update snapshot for: %{public}s because of filter rules"
+ "[%s] reloadSnapshot - update snapshot for: %{public}s"
+ "[%s] setExpandedSessionIdentifiers - no internal client found matching client: %{public}s"
+ "[%s] setUIPresented - no internal client found matching client: %{public}s"
+ "[%s] updatePendingItemIdentifiers - items: %{public}s for client: %{public}s"
+ "[MRDAVOutputContextManager] Duplicate AVOutputContext instance in %@ and allSharedAudioOutputContexts after mediaserverd death: %@ vs %@"
+ "[MRDAVOutputContextManager] OutputContext appears in both active and inactive lists: %@"
+ "[MRDAVOutputContextManager] OutputContext appears in both active and reserved lists: %@"
+ "[MRDAVOutputContextManager] OutputContext appears in both inactive and reserved lists: %@"
+ "[MRDAVOutputContextManager] Processed outputContext - Actions: %@"
+ "[MRDAVOutputContextManager] Re-building output context state in response to mediaserverd death in <%lf seconds> with outputContexts %@"
+ "[MRDAVOutputContextManager] Reloading outputContexts on serialQueue..."
+ "_discoveryTracker"
+ "_handleMediaServerDeath:"
+ "_onSerialQueue_processOutputContext:"
+ "_onSerialQueue_reloadOutputContexts:"
+ "_processOutputContext:"
+ "_reloadOutputContexts"
+ "activeOutputContext"
+ "cannot host a group session"
+ "discoveryTracker"
+ "feature not enabled"
+ "inactiveOutputContext"
+ "initWithActivityName:maxAllowedTime:windowDuration:handler:"
+ "isEligibleForHostingGroupSession"
+ "isPersonalDevice"
+ "joined another group session"
+ "logAndVerifyActiveSnapshot:inactiveSnapshot:reservedSnapshot:outputContext:currentActiveContexts:currentInactiveContexts:currentReservedContexts:"
+ "moved to active (%@)"
+ "moved to inactive (%@)"
+ "moved to reserved (%@)"
+ "persistantDiscoveryModeDetectionDuration"
+ "persistantDiscoveryModeDetectionWindowDuration"
+ "removed from active (%@)"
+ "removed from inactive (%@)"
+ "removed from reserved (%@)"
+ "setDiscoveryTracker:"
+ "startActivityTracking"
+ "stopActivityTracking"
+ "v24@?0@\"NSArray\"8@\"NSString\"16"
+ "v72@0:8@16@24@32@40@48@56@64"
+ "verboseOutputContextManagerLogging"
- "%@ %p {\n    effective discovery mode = %@, %@\n    desired discovery mode = %@, %@\n    xpc connection = %@\n    pid = %d\n    bundle id = %@\n    isProcessSuspended = %u\n    connection monitor = %@\n}"
- "Persistent RemoteControl Discovery"
- "[%s] Item: %{public}s, selected in local session, is .remoteControllable, has no nowPlayingInfo content -> .set"
- "[%s] Item: %{public}s, selected in local session, is .remoteControllable, has nowPlayingInfo content, existing containing session -> .handoff"
- "[%s] Item: %{public}s, selected in local session, is .remoteControllable, has nowPlayingInfo content, existing containing session, push disabled -> .set"
- "[%s] Item: %{public}s, selected in local session, is .remoteControllable, has nowPlayingInfo content, no existing containing session -> .handoff"
- "[%s] reloadSnapshot - Reload for: %{public}s"
- "[%s] reloadSnapshot - Update snapshot for: %{public}s"
- "[%s] reloadSnapshot - Updated filtered snapshot for: %{public}s"
- "[%s] setExpandedSessionIdentifiers - No internal client found matching client: %{public}s"
- "[%s] setUIPresented - No internal client found matching client: %{public}s"
- "[MRDAVOutputContextManager] OutputContext already reserved. Not adding to inactive list %@"
- "[MRDAVOutputContextManager] OutputContext became active %@ with local: %@"
- "[MRDAVOutputContextManager] OutputContext became active %@ with: %@"
- "[MRDAVOutputContextManager] OutputContext became inactive %@"
- "[MRDAVOutputContextManager] OutputContext deactiviating %@"
- "[MRDAVOutputContextManager] Re-building output context state in response to mediaserverd death"
- "[MRDAVOutputContextManager] Reserving outputContext %{public}@ for: %{public}@"
- "[MRDAVOutputContextManager] Returning active outputContext %@ with devices: %@ for: %@"
- "[MRDAVOutputContextManager] Returning reserved outputContext %@ for: %@"
- "[MRDAVOutputContextManager] Reusing inactive outputContext %{public}@ for: %{public}@ (%{public}@)"
- "[RemoteControlDiscoverySession] Discovery still on after %lf seconds. ABC..."
- "_discoveryTimer"
- "_handleMediaServerDeath"
- "persistentDiscoveryABCDuration"
- "processOutputContext:"
- "reloadOutputContexts"
- "sendPlaybackSession<%@>"

```
