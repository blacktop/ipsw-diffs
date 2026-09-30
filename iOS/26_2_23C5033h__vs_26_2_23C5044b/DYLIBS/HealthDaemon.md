## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6200.3.8.0.0
-  __TEXT.__text: 0x792ad0
+6200.3.10.2.1
+  __TEXT.__text: 0x793514
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x43b64
+  __TEXT.__objc_methlist: 0x43bd4
   __TEXT.__const: 0x1df6c
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x7d138
+  __TEXT.__cstring: 0x7d1b5
   __TEXT.__constg_swiftt: 0x14dc
   __TEXT.__swift5_typeref: 0xd9d
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x5c4
-  __TEXT.__oslogstring: 0x41df2
+  __TEXT.__oslogstring: 0x41ed3
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__gcc_except_tab: 0x383b4
+  __TEXT.__gcc_except_tab: 0x383e4
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1cd38
+  __TEXT.__unwind_info: 0x1cd68
   __TEXT.__eh_frame: 0x2310
-  __TEXT.__objc_classname: 0xc5c3
-  __TEXT.__objc_methname: 0x8ed6c
-  __TEXT.__objc_methtype: 0x16c36
-  __TEXT.__objc_stubs: 0x505c0
-  __DATA_CONST.__got: 0x5668
-  __DATA_CONST.__const: 0x1d2a0
+  __TEXT.__objc_classname: 0xc5ea
+  __TEXT.__objc_methname: 0x8ef81
+  __TEXT.__objc_methtype: 0x16c43
+  __TEXT.__objc_stubs: 0x50700
+  __DATA_CONST.__got: 0x5678
+  __DATA_CONST.__const: 0x1d310
   __DATA_CONST.__objc_classlist: 0x29d8
   __DATA_CONST.__objc_catlist: 0x4c0
-  __DATA_CONST.__objc_protolist: 0x9b0
+  __DATA_CONST.__objc_protolist: 0x9b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19f18
+  __DATA_CONST.__objc_selrefs: 0x19f78
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d88
   __DATA_CONST.__objc_arraydata: 0x84a0
   __AUTH_CONST.__auth_got: 0x2428
-  __AUTH_CONST.__const: 0x10018
-  __AUTH_CONST.__cfstring: 0x3d5e0
-  __AUTH_CONST.__objc_const: 0x7d9b8
+  __AUTH_CONST.__const: 0x10038
+  __AUTH_CONST.__cfstring: 0x3d5c0
+  __AUTH_CONST.__objc_const: 0x7da48
   __AUTH_CONST.__objc_arrayobj: 0x1ed8
-  __AUTH_CONST.__objc_intobj: 0x3e58
+  __AUTH_CONST.__objc_intobj: 0x3e70
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0xd120
   __AUTH.__data: 0x760
-  __DATA.__objc_ivar: 0x43b8
-  __DATA.__data: 0x81c8
+  __DATA.__objc_ivar: 0x43bc
+  __DATA.__data: 0x8228
   __DATA.__common: 0x64
   __DATA.__bss: 0x18c0
-  __DATA_DIRTY.__objc_ivar: 0xe88
+  __DATA_DIRTY.__objc_ivar: 0xe90
   __DATA_DIRTY.__objc_data: 0xe2e0
   __DATA_DIRTY.__data: 0x210
   __DATA_DIRTY.__bss: 0x3d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 98FCFE56-E763-30F1-8A8B-82C9FA7834CB
-  Functions: 34769
-  Symbols:   103917
-  CStrings:  44281
+  UUID: 222C398C-2A4A-3D70-8042-613A04E1EE6E
+  Functions: 34782
+  Symbols:   103966
+  CStrings:  44304
 
Symbols:
+ -[HDMirroredWorkoutSessionServer _cancelDisconnectTimerIfNeeded]
+ -[HDMirroredWorkoutSessionServer _cancelNearbyDeviceTimeoutTimerIfNeeded]
+ -[HDMirroredWorkoutSessionServer _scheduleNearbyDeviceTimeoutTimerIfNeeded]
+ -[HDMirroredWorkoutSessionServer _scheduleNearbyDeviceTimeoutTimer]
+ -[HDMirroredWorkoutSessionServer initWithProfile:configuration:sessionUUID:globalState:clientBundleIdentifier:connectedDeviceIDSIdentifier:]
+ -[HDMirroredWorkoutSessionServer nearbyDeviceTimeoutInterval]
+ -[HDMirroredWorkoutSessionServer rapportMessengerNearbyDeviceFoundWithIdentifier:]
+ -[HDMirroredWorkoutSessionServer rapportMessengerNearbyDeviceLostWithIdentifier:]
+ -[HDMirroredWorkoutSessionServer unit_test_setConnectedDeviceIDSIdentifier:]
+ -[HDRapportMessenger _handleIncomingRequest:idsIdentifier:responseHandler:]
+ -[HDRapportMessenger addNearbyDeviceObserver:]
+ -[HDRapportMessenger currentlyConnectedDeviceIDSIdentifiers]
+ -[HDRapportMessenger nearbyDeviceFoundWithIdentifier:]
+ -[HDRapportMessenger nearbyDeviceLostWithIdentifier:]
+ -[HDRapportMessenger removeNearbyDeviceObserver:]
+ -[HDRapportMessenger searchForNearbyDevices]
+ -[HDWorkoutMirroringManager _createServerWithData:idsIdentifier:completion:]
+ -[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:idsIdentifier:data:responseHandler:]
+ -[HDWorkoutSessionRapportSyncController rapportMessenger:didReceiveRequest:idsIdentifier:data:responseHandler:]
+ _OBJC_IVAR_$_HDRapportMessenger._deviceObservers
+ _OBJC_IVAR_$_HDRapportMessenger._lock_isNearbyDeviceSearchActive
+ _RPOptionSenderIDSDeviceID
+ _RPOptionTimeoutSeconds
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDRapportMessengerNearbyDeviceObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDRapportMessengerNearbyDeviceObserver
+ __OBJC_$_PROTOCOL_REFS_HDRapportMessengerNearbyDeviceObserver
+ __OBJC_LABEL_PROTOCOL_$_HDRapportMessengerNearbyDeviceObserver
+ __OBJC_PROTOCOL_$_HDRapportMessengerNearbyDeviceObserver
+ ___111-[HDWorkoutSessionRapportSyncController rapportMessenger:didReceiveRequest:idsIdentifier:data:responseHandler:]_block_invoke
+ ___44-[HDRapportMessenger searchForNearbyDevices]_block_invoke
+ ___44-[HDRapportMessenger searchForNearbyDevices]_block_invoke.335
+ ___44-[HDRapportMessenger searchForNearbyDevices]_block_invoke.336
+ ___53-[HDRapportMessenger nearbyDeviceLostWithIdentifier:]_block_invoke
+ ___54-[HDRapportMessenger nearbyDeviceFoundWithIdentifier:]_block_invoke
+ ___60-[HDRapportMessenger currentlyConnectedDeviceIDSIdentifiers]_block_invoke
+ ___65-[HDWorkoutSessionRapportSyncController _sendPendingTransactions]_block_invoke.368
+ ___67-[HDMirroredWorkoutSessionServer _scheduleNearbyDeviceTimeoutTimer]_block_invoke
+ ___75-[HDRapportMessenger _handleIncomingRequest:idsIdentifier:responseHandler:]_block_invoke
+ ___75-[HDRapportMessenger _handleIncomingRequest:idsIdentifier:responseHandler:]_block_invoke_2
+ ___81-[HDWorkoutSessionRapportSyncController sendRequest:transaction:responseHandler:]_block_invoke.360
+ ___99-[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:idsIdentifier:data:responseHandler:]_block_invoke
+ ___99-[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:idsIdentifier:data:responseHandler:]_block_invoke.323
+ ___block_descriptor_32_e31_16?0"RPCompanionLinkDevice"8l
+ ___block_descriptor_40_e8_32s_e50_v16?0"<HDRapportMessengerNearbyDeviceObserver>"8ls32l8
+ ___block_descriptor_40_e8_32w_e31_v16?0"RPCompanionLinkDevice"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e41_v32?0"NSData"8"NSString"16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e40_v16?0"HDMirroredWorkoutSessionServer"8ls32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e41_v32?0"NSData"8"NSString"16"NSError"24ls32l8s56l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e38_v16?0"<HDRapportMessengerObserver>"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e44_v24?0"HDWorkoutSessionServer"8"NSError"16ls80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.362
+ _objc_msgSend$_cancelDisconnectTimerIfNeeded
+ _objc_msgSend$_cancelNearbyDeviceTimeoutTimerIfNeeded
+ _objc_msgSend$_createServerWithData:idsIdentifier:completion:
+ _objc_msgSend$_handleIncomingRequest:idsIdentifier:responseHandler:
+ _objc_msgSend$_scheduleNearbyDeviceTimeoutTimer
+ _objc_msgSend$_scheduleNearbyDeviceTimeoutTimerIfNeeded
+ _objc_msgSend$activeDevices
+ _objc_msgSend$addNearbyDeviceObserver:
+ _objc_msgSend$currentlyConnectedDeviceIDSIdentifiers
+ _objc_msgSend$idsDeviceIdentifier
+ _objc_msgSend$initWithProfile:configuration:sessionUUID:globalState:clientBundleIdentifier:connectedDeviceIDSIdentifier:
+ _objc_msgSend$nearbyDeviceFoundWithIdentifier:
+ _objc_msgSend$nearbyDeviceLostWithIdentifier:
+ _objc_msgSend$nearbyDeviceTimeoutInterval
+ _objc_msgSend$rapportMessenger:didReceiveRequest:idsIdentifier:data:responseHandler:
+ _objc_msgSend$rapportMessengerNearbyDeviceFoundWithIdentifier:
+ _objc_msgSend$rapportMessengerNearbyDeviceLostWithIdentifier:
+ _objc_msgSend$searchForNearbyDevices
+ _objc_msgSend$setControlFlags:
+ _objc_msgSend$setDeviceFoundHandler:
+ _objc_msgSend$setDeviceLostHandler:
- -[HDMirroredWorkoutSessionServer cancelDisconnectTimerIfNeeded]
- -[HDMirroredWorkoutSessionServer initWithProfile:configuration:sessionUUID:globalState:clientBundleIdentifier:]
- -[HDRapportMessenger _handleIncomingRequest:responseHandler:]
- -[HDWorkoutMirroringManager _createServerWithData:completion:]
- -[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:data:responseHandler:]
- -[HDWorkoutSessionRapportSyncController _cancelReceiveHeartbeatTimeout]
- -[HDWorkoutSessionRapportSyncController _lock_cancelReceiveHeartbeatTimeout]
- -[HDWorkoutSessionRapportSyncController _receiveHeartbeatDidTimeout]
- -[HDWorkoutSessionRapportSyncController _scheduleReceiveHeartbeatTimeout]
- -[HDWorkoutSessionRapportSyncController heartbeatReceiveTimeout]
- -[HDWorkoutSessionRapportSyncController rapportMessenger:didReceiveRequest:data:responseHandler:]
- -[HDWorkoutSessionRapportSyncController receivedHeartbeatWithCompletion:]
- _OBJC_IVAR_$_HDWorkoutSessionRapportSyncController._receiveHeartbeatTimeoutSource
- ___61-[HDRapportMessenger _handleIncomingRequest:responseHandler:]_block_invoke
- ___61-[HDRapportMessenger _handleIncomingRequest:responseHandler:]_block_invoke_2
- ___65-[HDWorkoutSessionRapportSyncController _sendPendingTransactions]_block_invoke.371
- ___73-[HDWorkoutSessionRapportSyncController _scheduleReceiveHeartbeatTimeout]_block_invoke
- ___81-[HDWorkoutSessionRapportSyncController sendRequest:transaction:responseHandler:]_block_invoke.363
- ___85-[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:data:responseHandler:]_block_invoke
- ___85-[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:data:responseHandler:]_block_invoke.323
- ___97-[HDWorkoutSessionRapportSyncController rapportMessenger:didReceiveRequest:data:responseHandler:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e40_v16?0"HDMirroredWorkoutSessionServer"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e38_v16?0"<HDRapportMessengerObserver>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e44_v24?0"HDWorkoutSessionServer"8"NSError"16ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.354
- _objc_msgSend$_cancelReceiveHeartbeatTimeout
- _objc_msgSend$_createServerWithData:completion:
- _objc_msgSend$_handleIncomingRequest:responseHandler:
- _objc_msgSend$_lock_cancelReceiveHeartbeatTimeout
- _objc_msgSend$_receiveHeartbeatDidTimeout
- _objc_msgSend$_scheduleReceiveHeartbeatTimeout
- _objc_msgSend$cancelDisconnectTimerIfNeeded
- _objc_msgSend$heartbeatReceiveTimeout
- _objc_msgSend$initWithProfile:configuration:sessionUUID:globalState:clientBundleIdentifier:
- _objc_msgSend$rapportMessenger:didReceiveRequest:data:responseHandler:
- _objc_msgSend$receivedHeartbeatWithCompletion:
CStrings:
+ "%{public}@: Cancelling nearby device timer."
+ "%{public}@: Scheduling nearby device timer."
+ "@16@?0@\"RPCompanionLinkDevice\"8"
+ "HDRapportMessengerNearbyDeviceObserver"
+ "[mirroring] %{public}@: Error received monitoring nearby devices %{public}@"
+ "[mirroring] %{public}@: Initializing MirroredSessionServer with IDS identifier %{public}@."
+ "[mirroring]: Device found %{public}@"
+ "[mirroring]: Device lost %{public}@"
+ "_cancelDisconnectTimerIfNeeded"
+ "_cancelNearbyDeviceTimeoutTimerIfNeeded"
+ "_connectedDeviceIDSIdentifier"
+ "_createServerWithData:idsIdentifier:completion:"
+ "_deviceObservers"
+ "_handleIncomingRequest:idsIdentifier:responseHandler:"
+ "_lock_isNearbyDeviceSearchActive"
+ "_nearbyDeviceOutOfRangeTimeoutSource"
+ "_scheduleNearbyDeviceTimeoutTimer"
+ "_scheduleNearbyDeviceTimeoutTimerIfNeeded"
+ "activeDevices"
+ "addNearbyDeviceObserver:"
+ "currentlyConnectedDeviceIDSIdentifiers"
+ "idsDeviceIdentifier"
+ "initWithProfile:configuration:sessionUUID:globalState:clientBundleIdentifier:connectedDeviceIDSIdentifier:"
+ "nearbyDeviceFoundWithIdentifier:"
+ "nearbyDeviceLostWithIdentifier:"
+ "nearbyDeviceTimeoutInterval"
+ "rapportMessenger:didReceiveRequest:idsIdentifier:data:responseHandler:"
+ "rapportMessengerNearbyDeviceFoundWithIdentifier:"
+ "rapportMessengerNearbyDeviceLostWithIdentifier:"
+ "removeNearbyDeviceObserver:"
+ "searchForNearbyDevices"
+ "setControlFlags:"
+ "setDeviceFoundHandler:"
+ "setDeviceLostHandler:"
+ "unit_test_setConnectedDeviceIDSIdentifier:"
+ "v16@?0@\"<HDRapportMessengerNearbyDeviceObserver>\"8"
+ "v16@?0@\"RPCompanionLinkDevice\"8"
+ "v32@?0@\"NSData\"8@\"NSString\"16@\"NSError\"24"
+ "v56@0:8@\"HDRapportMessenger\"16@\"HDRapportRequestIdentifier\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
- "Primary session is unreachable."
- "[mirroring] %{public}@: No heartbeat received in the last %f seconds, marking session as disconnected."
- "_cancelReceiveHeartbeatTimeout"
- "_createServerWithData:completion:"
- "_handleIncomingRequest:responseHandler:"
- "_lock_cancelReceiveHeartbeatTimeout"
- "_receiveHeartbeatDidTimeout"
- "_receiveHeartbeatTimeoutSource"
- "_scheduleReceiveHeartbeatTimeout"
- "cancelDisconnectTimerIfNeeded"
- "heartbeatReceiveTimeout"
- "initWithProfile:configuration:sessionUUID:globalState:clientBundleIdentifier:"
- "rapportMessenger:didReceiveRequest:data:responseHandler:"
- "receivedHeartbeatWithCompletion:"
- "v48@0:8@\"HDRapportMessenger\"16@\"HDRapportRequestIdentifier\"24@\"NSData\"32@?<v@?@\"NSData\"@\"NSError\">40"

```
