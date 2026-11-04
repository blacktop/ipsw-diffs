## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

```diff

-89.0.0.0.0
-  __TEXT.__text: 0x49bcc
-  __TEXT.__objc_methlist: 0x4a3c
+93.0.0.0.0
+  __TEXT.__text: 0x4ab54
+  __TEXT.__objc_methlist: 0x4b04
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x1413
-  __TEXT.__oslogstring: 0x5f5f
-  __TEXT.__gcc_except_tab: 0x1bac
-  __TEXT.__unwind_info: 0x1660
+  __TEXT.__cstring: 0x1480
+  __TEXT.__oslogstring: 0x6019
+  __TEXT.__gcc_except_tab: 0x1c50
+  __TEXT.__unwind_info: 0x16d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa58
+  __DATA_CONST.__const: 0xaa0
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dc8
+  __DATA_CONST.__objc_selrefs: 0x1e80
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x288
   __DATA_CONST.__got: 0x480
-  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x1a80
-  __AUTH_CONST.__objc_const: 0x6c98
+  __AUTH_CONST.__objc_const: 0x6d58
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1450
-  __DATA.__objc_ivar: 0x3b8
+  __DATA.__objc_ivar: 0x3c8
   __DATA.__data: 0x600
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1726
-  Symbols:   2775
-  CStrings:  629
+  Functions: 1745
+  Symbols:   2809
+  CStrings:  637
 
Symbols:
+ +[MTRPluginClientXPCProxy _connectionQueueBusy]
+ +[MTRPluginClientXPCProxy connectionQueueBusyBegin]
+ +[MTRPluginClientXPCProxy connectionQueueBusyEnd]
+ -[MTRPluginClientConnection _deliverMessagePayloadToPrimaryResident:timeout:responseHandler:completion:]
+ -[MTRPluginClientXPCProxy _hasSendWindowLocked]
+ -[MTRPluginClientXPCProxy _sendBarrierCompleted]
+ -[MTRPluginClientXPCProxy _sendIssued]
+ -[MTRPluginClientXPCProxy _sendLocked:]
+ -[MTRPluginClientXPCProxy callsQueuedSinceSendBarrierCount]
+ -[MTRPluginClientXPCProxy disconnected]
+ -[MTRPluginClientXPCProxy inFlightSendCount]
+ -[MTRPluginClientXPCProxy pendingCalls]
+ -[MTRPluginClientXPCProxy queuedSendCount]
+ -[MTRPluginClientXPCProxy setCallsQueuedSinceSendBarrierCount:]
+ -[MTRPluginClientXPCProxy setDisconnected:]
+ -[MTRPluginClientXPCProxy setInFlightSendCount:]
+ -[MTRPluginClientXPCProxy setQueuedSendCount:]
+ -[MTRPluginProtobufOverModernTransport _sendMessageToPrimaryHomeHub:throughConnections:timeout:metric:]
+ -[MTRPluginRemoteClient _sendControllerConfiguration:controller:completion:]
+ -[MTRPluginRemoteClient registrationAwaitingClear]
+ -[MTRPluginRemoteClient residentMayHoldUnclearedRegistration]
+ -[MTRPluginRemoteClient setRegistrationAwaitingClear:]
+ -[MTRPluginRemoteClient setResidentMayHoldUnclearedRegistration:]
+ -[MTRPluginRemoteSessionManager _acceptsRelayedReportForNodeID:homeUUID:]
+ GCC_except_table23
+ GCC_except_table32
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table48
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table6
+ GCC_except_table7
+ _OBJC_IVAR_$_MTRPluginClientXPCProxy._callsQueuedSinceSendBarrierCount
+ _OBJC_IVAR_$_MTRPluginClientXPCProxy._disconnected
+ _OBJC_IVAR_$_MTRPluginClientXPCProxy._inFlightSendCount
+ _OBJC_IVAR_$_MTRPluginClientXPCProxy._pendingCalls
+ _OBJC_IVAR_$_MTRPluginClientXPCProxy._queuedSendCount
+ _OBJC_IVAR_$_MTRPluginRemoteClient._registrationAwaitingClear
+ _OBJC_IVAR_$_MTRPluginRemoteClient._residentMayHoldUnclearedRegistration
+ __OBJC_$_CLASS_METHODS_MTRPluginClientXPCProxy
+ ___103-[MTRPluginProtobufOverModernTransport _sendMessageToPrimaryHomeHub:throughConnections:timeout:metric:]_block_invoke
+ ___103-[MTRPluginProtobufOverModernTransport _sendMessageToPrimaryHomeHub:throughConnections:timeout:metric:]_block_invoke_2
+ ___104-[MTRPluginClientConnection _deliverMessagePayloadToPrimaryResident:timeout:responseHandler:completion:]_block_invoke
+ ___39-[MTRPluginClientXPCProxy _sendLocked:]_block_invoke
+ ___76-[MTRPluginRemoteClient _sendControllerConfiguration:controller:completion:]_block_invoke
+ ___block_descriptor_32_e65_q24?0"MTRPluginClientConnection"8"MTRPluginClientConnection"16l
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e8_v16?08ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e8_v12?0B8ls32l8s40l8s48l8s56l8s64l8
+ ___clientConnectionsForMessage_block_invoke
+ _clientConnectionsForMessage
+ _objc_setProperty_nonatomic_copy
+ _sConnectionQueueBusyDepth
- -[MTRPluginClientConnection _deliverMessagePayloadToPrimaryResident:timeout:responseHandler:]
- -[MTRPluginClientXPCProxy callRemoteProxyObject:applyBackpressureCap:]
- -[MTRPluginClientXPCProxy inFlightPossiblyCappedSendCount]
- -[MTRPluginClientXPCProxy lastDropLogNSec]
- -[MTRPluginClientXPCProxy setInFlightPossiblyCappedSendCount:]
- -[MTRPluginClientXPCProxy setLastDropLogNSec:]
- -[MTRPluginClientXPCProxy setSuppressedDropCount:]
- -[MTRPluginClientXPCProxy suppressedDropCount]
- GCC_except_table36
- GCC_except_table50
- _OBJC_IVAR_$_MTRPluginClientXPCProxy._inFlightPossiblyCappedSendCount
- _OBJC_IVAR_$_MTRPluginClientXPCProxy._lastDropLogNSec
- _OBJC_IVAR_$_MTRPluginClientXPCProxy._suppressedDropCount
- ___70-[MTRPluginClientXPCProxy callRemoteProxyObject:applyBackpressureCap:]_block_invoke
- ___77-[MTRPluginProtobufOverModernTransport _sendMessageToPrimaryHomeHub:timeout:]_block_invoke
- ___93-[MTRPluginClientConnection _deliverMessagePayloadToPrimaryResident:timeout:responseHandler:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e8_v16?08ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40bs48w_e5_v8?0ls32l8s40l8w48l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- _clientConnectionForMessage
- _clock_gettime_nsec_np
CStrings:
+ "!"
+ "%@ Clearing resident registration for controller %@ before registering %@"
+ "%@ Connection %@ refused _deliverMessagePayloadToPrimaryResident"
+ "%@ Deferring registration %@ for controller %@ until the resident answers the clear"
+ "%@ No connection accepted _deliverMessagePayloadToPrimaryResident for message: %@"
+ "%@ disconnecting client, %s: %lu sends in flight, %lu calls queued since the last send barrier, %lu calls queued - dropping them"
+ "Q"
+ "halted"
+ "past the 4096-call cap"
+ "q24@?0@\"MTRPluginClientConnection\"8@\"MTRPluginClientConnection\"16"
+ "v12@?0B8"
- "%@ Failed to _deliverMessagePayloadToPrimaryResident for connection: %@"
- "%@ No connection\u00a0found to _deliverMessagePayloadToPrimaryResident for message: %@"
- "%@ dropping XPC send to client - in-flight count %lu >= cap %lu (%lu drop(s) since last log)"
```
