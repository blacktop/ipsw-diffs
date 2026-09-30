## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-30.59.1.9.0
-  __TEXT.__text: 0x1f5704
-  __TEXT.__auth_stubs: 0x2ad0
-  __TEXT.__objc_stubs: 0x18160
-  __TEXT.__objc_methlist: 0xbafc
+31.5.2.1.2
+  __TEXT.__text: 0x1f7dbc
+  __TEXT.__auth_stubs: 0x2ae0
+  __TEXT.__objc_stubs: 0x18520
+  __TEXT.__objc_methlist: 0xbd14
   __TEXT.__const: 0x39e0
-  __TEXT.__gcc_except_tab: 0x4e18
-  __TEXT.__cstring: 0x426c3
-  __TEXT.__objc_classname: 0xa26
-  __TEXT.__objc_methname: 0x24089
-  __TEXT.__objc_methtype: 0x327c
+  __TEXT.__gcc_except_tab: 0x4dc0
+  __TEXT.__cstring: 0x431b3
+  __TEXT.__objc_classname: 0xa46
+  __TEXT.__objc_methname: 0x246dd
+  __TEXT.__objc_methtype: 0x32a0
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca
   __TEXT.__ustring: 0x10

   __TEXT.__swift5_capture: 0x193c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x5748
+  __TEXT.__unwind_info: 0x57d0
   __TEXT.__eh_frame: 0x2070
-  __DATA_CONST.__auth_got: 0x1578
+  __DATA_CONST.__auth_got: 0x1580
   __DATA_CONST.__got: 0xc98
   __DATA_CONST.__auth_ptr: 0x570
-  __DATA_CONST.__const: 0xaab8
-  __DATA_CONST.__cfstring: 0x9a60
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __DATA_CONST.__const: 0xab10
+  __DATA_CONST.__cfstring: 0x9ba0
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_intobj: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1a1f0
-  __DATA.__objc_selrefs: 0x7a70
-  __DATA.__objc_ivar: 0x1498
-  __DATA.__objc_data: 0x2a68
-  __DATA.__data: 0x4218
-  __DATA.__bss: 0x6ad0
+  __DATA.__objc_const: 0x1a4c0
+  __DATA.__objc_selrefs: 0x7bb0
+  __DATA.__objc_ivar: 0x14cc
+  __DATA.__objc_data: 0x2ab8
+  __DATA.__data: 0x4288
+  __DATA.__bss: 0x6ae0
   __DATA.__common: 0x398
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6279CE43-94DC-3CC7-87D1-11E5D3DB59E7
-  Functions: 9285
-  Symbols:   1237
-  CStrings:  14596
+  UUID: 1E8E3E4F-D6E9-3FD6-92FC-7A5D21CB43F4
+  Functions: 9363
+  Symbols:   1238
+  CStrings:  14733
 
Symbols:
+ _CUXPCEncodeNSError
+ _xpc_copy
- _xpc_connection_copy_invalidation_reason
CStrings:
+ "### Register controller failed: %@"
+ "### Registration with manager failed: CID 0x%X, %@"
+ "### Shared XPC connection interrupted"
+ "### Shared XPC connection invalidated"
+ "### Shared connection activation failed: %@"
+ "-[AAController _registerWithSharedManager:]"
+ "-[AAController _registerWithSharedManager:]_block_invoke"
+ "-[AAController activateWithCompletion:]"
+ "-[AAControllerSharedXPCManager _activateSharedConnection]"
+ "-[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:]"
+ "-[AAControllerSharedXPCManager _handleActivationReply:]"
+ "-[AAControllerSharedXPCManager _handleConnectionInterruption]"
+ "-[AAControllerSharedXPCManager _handleXPCEvent:]"
+ "-[AAControllerSharedXPCManager _processPendingMessages]"
+ "-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]"
+ "-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke_2"
+ "-[AAControllerSharedXPCManager init]"
+ "-[AAControllerSharedXPCManager invalidate]_block_invoke"
+ "-[AAControllerSharedXPCManager registerController:completion:]_block_invoke"
+ "-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke"
+ "-[AAControllerSharedXPCManager unregisterController:]_block_invoke"
+ "-[AADeviceManagerDaemon updateFarFieldSessionOnGoing:forBluetoothAddress:]_block_invoke"
+ "-[AAGestureControl _handleFarFieldStatusChanged:]"
+ "-[BTSmartRoutingDaemon _queryLocalAudioCategory]"
+ "-[BTSmartRoutingDaemon _tipiHealingCompleteCheckTimerForDevice:]"
+ "-[BTSmartRoutingDaemon _tipiHealingHijackTimerReset]"
+ "-[SRConnectionManager _isHeadphoneEligibleForTipiV2:result:]_block_invoke"
+ "-[SRConnectionManager _isHeadphonePrerequisiteMet:]_block_invoke"
+ "-[SRConnectionManager bluetoothStateChanged:]"
+ "-[SRConnectionManager pairedDeviceCountChanged:]"
+ "-[SRDiscoveredDevice _updateUnifiedInEarState]"
+ "-[SRDiscoveredDevice setAacpInEarState:]"
+ "-[SRDiscoveredDevice setNearbyInEar:]"
+ "-[SRDiscoveredDevice setPrevFailedTipiConnectType:]"
+ "2ndSourceConnecting"
+ "2ndSourceHigherActivityLevel"
+ "AAControllerSharedXPCManager"
+ "AAControllerSharedXPCManager initialized"
+ "Activating shared XPC connection"
+ "Already registered with manager: CID 0x%X"
+ "Attempting to reestablish connection after interruption"
+ "AudioStateSnapshot: BtState %s Route %@ App %@, Score %@, Remote %@ NumofApp %@"
+ "B32@0:8@16^I24"
+ "BT not PowerOn"
+ "BluetoothStateChanged %s -> %s"
+ "ConnectedSourceDiffiCloud"
+ "Controller not registered"
+ "Device shouldnt route"
+ "Device tipi healing was completed for %@ with tipi healing timer, but no routing request found for device"
+ "Eligible for DR from nearby ATV isAllowedFromPairedDevice %s"
+ "Establishing shared XPC connection"
+ "EvaluateNearbyDevicesForConnection paired %d connectedWx %d nearbyWx %d srDisDeviceCount %d nearbySource %d btState %s audioRoute %s tipiScore %s sourceSRcapable %s audioCategory %d callStarted %s OD %s"
+ "Evaluator: connect start: %@ type %s"
+ "Far field session ongoing btAddress: %@ changed: %s -> %s"
+ "Far field session ongoing state changed notified device with address %s"
+ "FirstConnectAfterSREnabled"
+ "FwNotEligible"
+ "Invalidating AAControllerSharedXPCManager"
+ "Manager invalidated"
+ "MissingFwVersion"
+ "No XPC connection"
+ "No more registered controllers, keeping connection alive for reuse"
+ "Not phase3 and we made it DontRoute"
+ "Processing %lu pending messages"
+ "QueryLocalAudioCategory %@"
+ "Queued message for controller %@, pending count: %lu"
+ "Received XPC reply for controller %@: %@"
+ "Registered controller %@, total: %lu"
+ "Registered with manager: CID 0x%X"
+ "Registering with shared manager: CID 0x%X"
+ "Sending XPC message for controller %@: %@"
+ "Setting Bluetooth state after activation %s -> %s"
+ "Setting RoutingAction %s isTiPiDevice %s isStreamingFromOtherSource %s isBudswap %s manual %s isTriangleRecoveryInitiatedAddress %s localAudio %@"
+ "Setting aacpInEarState %@ %s -> %s"
+ "Setting connected banner tick %llu"
+ "Setting inEarStateUnified %@ %s -> %s"
+ "Setting prevFailedTipiConnectType %@ %s -> %s"
+ "Shared XPC connection activated successfully"
+ "T@\"NSMutableArray\",&,N,V_pendingMessages"
+ "T@\"NSMutableSet\",&,N,V_registeredControllers"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_managerQueue"
+ "T@\"NSString\",&,N,V_farFieldDeviceAddress"
+ "TB,N,V_connectionActive"
+ "TB,N,V_invalidateCalled"
+ "Tc,N,V_farFieldSessionOnGoing"
+ "Ti,N,V_aacpInEarState"
+ "Ti,N,V_nearbyInEar"
+ "Ti,N,V_prevFailedTipiConnectType"
+ "Ti,R,N,V_inEarStateUnified"
+ "Tipi Healing timer(for address: %@) does not match device tipi healing was completed for: %@"
+ "Tipi healing already ongoing, dropping old request!"
+ "Tipi healing complete when hijack timer was running, service pending MX routing request"
+ "Tipi healing timer: forget"
+ "TipiScore1Unknown"
+ "TipiScore2Unknown"
+ "TipiTableEvent: Tipi healing complete now but device FW does not support HijackV2, service pending MX request if needed"
+ "Trying LE pipe reason %@"
+ "Unregistered controller %@, remaining: %lu"
+ "_aacpInEarState"
+ "_activateSharedConnection"
+ "_connectionActive"
+ "_connectionEstablished"
+ "_distributeDeviceInfoArray:"
+ "_distributeXPCMessage:"
+ "_ensureSharedConnectionWithCompletion:"
+ "_farFieldDeviceAddress"
+ "_farFieldSessionOnGoing"
+ "_farFieldStatusMonitoringEnsureStarted"
+ "_farFieldStatusMonitoringEnsureStopped"
+ "_getInEarStateFromCbDevice:"
+ "_handleActivationReply:"
+ "_handleConnectionInterruption"
+ "_handleConnectionInvalidation"
+ "_handleDualBudLongPressGesture called translation not installed"
+ "_handleFarFieldStatusChanged:"
+ "_handleXPCEvent:"
+ "_inEarStateUnified"
+ "_invalidateConnection"
+ "_isHeadphoneEligibleForTipiV2:result:"
+ "_isHeadphonePrerequisiteMet:"
+ "_managerQueue"
+ "_pairedDeviceCount"
+ "_pendingActivations"
+ "_pendingMessages"
+ "_prevFailedTipiConnectType"
+ "_processPendingMessages"
+ "_queryLocalAudioCategory"
+ "_registerWithSharedManager:"
+ "_registeredControllers"
+ "_registeredWithManager"
+ "_sendMessage:controller:queue:replyHandler:"
+ "_sharedXPCConnection"
+ "_shouldTryLEPipe:"
+ "_tipiHealingCompleteCheckTimerForDevice:"
+ "_tipiHealingHijackTimerAddress"
+ "_tipiHealingHijackTimerReset"
+ "_updateUnifiedInEarState"
+ "aacpInEarState"
+ "applicationIsInstalled:"
+ "btAddress %@ nbNm %@ isNb %s ts1 %s ts2 %s fw %@ isCp %s sc %d nbInEar %s nbLh %@ fd %s nbSt %s prevFailConnect %s"
+ "com.apple.AAControllerSharedXPCManager"
+ "com.apple.Translate"
+ "com.apple.bluetooth.FarFieldBluetoothRouteEnable"
+ "connectionActive"
+ "controller"
+ "errC"
+ "errD"
+ "errM"
+ "errO"
+ "farFieldDeviceAddress"
+ "farFieldSessionOnGoing"
+ "inEarStateUnified"
+ "invalidateCalled"
+ "pairedDeviceCountChanged %d -> %d"
+ "pairedDeviceCountChanged:"
+ "pendingMessages"
+ "playing success sound as _farFieldSessionOnGoing == %i"
+ "prevFailedTipiConnectType"
+ "registerController:completion:"
+ "registeredControllers"
+ "replyHandler"
+ "sendMessage:controller:queue:replyHandler:"
+ "setAacpInEarState:"
+ "setConnectionActive:"
+ "setFarFieldDeviceAddress:"
+ "setFarFieldSessionOnGoing:"
+ "setInvalidateCalled:"
+ "setManagerQueue:"
+ "setNearbyInEar:"
+ "setPendingMessages:"
+ "setPrevFailedTipiConnectType:"
+ "setRegisteredControllers:"
+ "sharedManager"
+ "skipping playing success sound as _farFieldSessionOnGoing == true"
+ "unregisterController:"
+ "updateFarFieldSessionOnGoing:forBluetoothAddress:"
+ "v48@0:8@16@24@32@?40"
+ "value"
- "### Activate failed: CID 0x%X, %@"
- "### Invalidated unexpectedly for reason %s"
- "-[AAController _activateXPC:]"
- "-[AAController _activateXPCCompleted:]"
- "-[AAController _activate]"
- "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
- "-[BTServicesDaemon openRadarforAudioQuality]"
- "-[SRConnectionManager _findHeadphoneForOnDemandEvent:]_block_invoke"
- "-[SRConnectionManager _findHeadphoneForOnDemandEvent:]_block_invoke_2"
- "-[SRConnectionManager _findHeadphoneForOnDemandEventStart]_block_invoke"
- "-[SRConnectionManager _isHeadphoneEligibleForTipiV2:]_block_invoke"
- "-[SRConnectionManager _isHeadphonePrerequisiteMet:connectType:]_block_invoke"
- "-[SRConnectionManager _isOnDemandConnectEligible:result:]"
- "-[SRDiscoveredDevice _setNearbyInEar:]"
- "1551854"
- "2nd source activity level higher"
- "815886"
- "Activate: CID 0x%X"
- "Activated: CID 0x%X"
- "AudioStateSnapshot: Route:%@ App %@, Score %@, Remote %@NumofApp %@"
- "Backoff LE Pipe for >=2 high activity nearby sources"
- "Bluetooth Audio Quality Feedback"
- "CoreBluetooth - HFP Audio | iOS"
- "Eligible for DR from nearby ATV isAllowedFromNearbyDevice %s isAllowedFromPairedDevice %s"
- "EvaluateNearbyDevicesForConnection connectedWx %d nearbyWx %d srDisDeviceCount %d nearbySource %d btState %s audioRoute %s tipiScore %s sourceSRcapable %s audioCategory %d callStarted %s OD %s"
- "Evaluator: connect start: %@"
- "FindHeadphoneForOnDemandEvent: Skip, reason %@"
- "FindHeadphoneForOnDemandEventWithResult: Skip, reason %@"
- "Keywords"
- "Performance"
- "Re-activate: CID 0x%X"
- "Received audio score and tipi healing hijack timer is running, service pending MX request"
- "Setting connected banner tick %u"
- "TI,N,V_coreBluetoothInternalFlag"
- "Ti,R,N,V_nearbyInEar"
- "TipiTableEvent: Tipi healing complete now but device FW does not support HijackV2, service pending MX request"
- "_activateXPC:"
- "_activateXPCCompleted:"
- "_coreBluetoothInternalFlag"
- "_findHeadphoneForOnDemandEvent:"
- "_findHeadphoneForOnDemandEventStart"
- "_isHeadphoneEligibleForTipiV2:"
- "_isHeadphonePrerequisiteMet:connectType:"
- "_isThisDeviceAHomePod"
- "_setNearbyInEar:"
- "audioQuality - File Radar"
- "audioQuality banner timeout"
- "audioQuality user click, openradar"
- "audioQuality user dismiss"
- "audioQuality: banner action: %s, %{error}"
- "audioQuality: banner error for device %@"
- "btAddress %@ nbNm %@ isNb %s ts1 %s ts2 %s fw %@ isCp %s sc %d nbInEar %s nbLh %@ fd %s nbSt %s"
- "coreBluetoothInternalFlag"
- "nothing is connected"
- "setCoreBluetoothInternalFlag:"

```
