## BluetoothServices

> `/System/Library/PrivateFrameworks/BluetoothServices.framework/Versions/A/BluetoothServices`

```diff

-23.1.0.0.0
-  __TEXT.__text: 0x136d8
+24.26.0.0.0
+  __TEXT.__text: 0x14618
   __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x13c4
+  __TEXT.__objc_methlist: 0x191c
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x68c
-  __TEXT.__cstring: 0x39d2
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__cstring: 0x39e1
+  __TEXT.__unwind_info: 0x600
   __TEXT.__objc_classname: 0x22c
   __TEXT.__objc_methname: 0x356d
   __TEXT.__objc_methtype: 0xc59

   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf8
+  __DATA_CONST.__objc_selrefs: 0xc50
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x2b0
-  __AUTH_CONST.__const: 0x3f0
+  __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__cfstring: 0x380
-  __AUTH_CONST.__objc_const: 0x3460
+  __AUTH_CONST.__objc_const: 0x2a48
   __AUTH.__objc_data: 0x460
   __AUTH.__data: 0x8
   __DATA.__objc_ivar: 0x284

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 06F5F358-1CB1-3EEB-9D99-729EB9723ECD
-  Functions: 546
-  Symbols:   1282
+  UUID: 0912813B-B2E9-3B45-B3A3-2BF84B5C9B1B
+  Functions: 675
+  Symbols:   1419
   CStrings:  1166
 
Symbols:
+ -[BTAirPodsControlServiceClient _completeRequest:error:].cold.1
+ -[BTAirPodsControlServiceClient _completeRequest:error:].cold.2
+ -[BTAirPodsControlServiceClient _invalidate].cold.1
+ -[BTAirPodsControlServiceClient _reportError:].cold.1
+ -[BTAirPodsControlServiceClient _runConnectStart].cold.1
+ -[BTAirPodsControlServiceClient _runConnectStart].cold.2
+ -[BTAirPodsControlServiceClient _runConnectStart].cold.3
+ -[BTAirPodsControlServiceClient _runConnectStart].cold.4
+ -[BTAirPodsControlServiceClient _runConnectStart].cold.5
+ -[BTAirPodsControlServiceClient _runConnectStart].cold.6
+ -[BTAirPodsControlServiceClient _runDiscoverCharacteristicsStart].cold.1
+ -[BTAirPodsControlServiceClient _runDiscoverCharacteristicsStart].cold.2
+ -[BTAirPodsControlServiceClient _runDiscoverCharacteristicsStart].cold.3
+ -[BTAirPodsControlServiceClient _runDiscoverCharacteristicsStart].cold.4
+ -[BTAirPodsControlServiceClient _runDiscoverServicesStart].cold.1
+ -[BTAirPodsControlServiceClient _runDiscoverServicesStart].cold.2
+ -[BTAirPodsControlServiceClient _runDiscoverServicesStart].cold.3
+ -[BTAirPodsControlServiceClient _runProcessRequest:].cold.1
+ -[BTAirPodsControlServiceClient _runProcessRequest:].cold.2
+ -[BTAirPodsControlServiceClient _runProcessRequest:].cold.3
+ -[BTAirPodsControlServiceClient _runProcessRequest:].cold.4
+ -[BTAirPodsControlServiceClient _run].cold.1
+ -[BTAirPodsControlServiceClient centralManager:didConnectPeripheral:].cold.1
+ -[BTAirPodsControlServiceClient centralManager:didConnectPeripheral:].cold.2
+ -[BTAirPodsControlServiceClient centralManager:didFailToConnectPeripheral:error:].cold.1
+ -[BTAirPodsControlServiceClient centralManager:didFailToConnectPeripheral:error:].cold.2
+ -[BTAirPodsControlServiceClient centralManager:didUpdateFindMyPeripherals:].cold.1
+ -[BTAirPodsControlServiceClient centralManagerDidUpdateState:].cold.1
+ -[BTAirPodsControlServiceClient peripheral:didDiscoverCharacteristicsForService:error:].cold.1
+ -[BTAirPodsControlServiceClient peripheral:didDiscoverCharacteristicsForService:error:].cold.2
+ -[BTAirPodsControlServiceClient peripheral:didDiscoverCharacteristicsForService:error:].cold.3
+ -[BTAirPodsControlServiceClient peripheral:didDiscoverServices:].cold.1
+ -[BTAirPodsControlServiceClient peripheral:didDiscoverServices:].cold.2
+ -[BTAirPodsControlServiceClient peripheral:didDiscoverServices:].cold.3
+ -[BTAirPodsControlServiceClient peripheral:didUpdateNotificationStateForCharacteristic:error:].cold.1
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.1
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.10
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.2
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.3
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.4
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.5
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.6
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.7
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.8
+ -[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:].cold.9
+ -[BTAirPodsControlServiceClient peripheral:didWriteValueForCharacteristic:error:].cold.1
+ -[BTAirPodsControlServiceClient peripheral:didWriteValueForCharacteristic:error:].cold.2
+ -[BTAudioRoutingRequest _activate].cold.1
+ -[BTAudioRoutingRequest _ensureXPCStarted].cold.1
+ -[BTAudioRoutingRequest _interrupted].cold.1
+ -[BTAudioRoutingRequest _invalidated].cold.1
+ -[BTAudioRoutingRequest _invalidated].cold.2
+ -[BTAudioRoutingRequest _reportError:].cold.1
+ -[BTAudioRoutingRequest isSystemContext].cold.1
+ -[BTAudioSession _ensureXPCStarted].cold.1
+ -[BTAudioSession _interrupted].cold.1
+ -[BTAudioSession _invalidated].cold.1
+ -[BTAudioSession _invalidated].cold.2
+ -[BTAudioSession _reportError:].cold.1
+ -[BTAudioSession isSystemContext].cold.1
+ -[BTBannerUISession _xpcCompleted:].cold.1
+ -[BTBannerUISession _xpcCompleted:].cold.2
+ -[BTBannerUISession _xpcCompleted:].cold.3
+ -[BTBannerUISession _xpcConnectionMessage:].cold.1
+ -[BTBannerUISession _xpcConnectionMessage:].cold.2
+ -[BTBannerUISession _xpcConnectionMessage:].cold.3
+ -[BTBannerUISession _xpcConnectionMessage:].cold.4
+ -[BTBannerUISession _xpcConnectionMessage:].cold.5
+ -[BTBannerUISession _xpcEvent:].cold.1
+ -[BTBannerUISession _xpcEvent:].cold.2
+ -[BTBannerUISession _xpcSendMessage].cold.1
+ -[BTBannerUISession _xpcSendReplyError:request:].cold.1
+ -[BTBannerUISession _xpcSendReplyError:request:].cold.2
+ -[BTBluetoothPairingSession _activate].cold.1
+ -[BTBluetoothPairingSession dealloc].cold.1
+ -[BTCloudDevice initWithCoder:].cold.1
+ -[BTCloudDeviceSupportInformation initWithCoder:].cold.1
+ -[BTCloudServicesClient _ensureXPCStarted].cold.1
+ -[BTCloudServicesClient _interrupted].cold.1
+ -[BTCloudServicesClient _invalidated].cold.1
+ -[BTCloudServicesClient _invalidated].cold.2
+ -[BTCloudServicesClient currentConsoleUserID].cold.1
+ -[BTCloudServicesClient isSystemContext].cold.1
+ -[BTMagicPairingSettings initWithCoder:].cold.1
+ -[BTServicesClient _ensureXPCStarted].cold.1
+ -[BTServicesClient _interrupted].cold.1
+ -[BTServicesClient _invalidated].cold.1
+ -[BTServicesClient _invalidated].cold.2
+ -[BTServicesClient isSystemContext].cold.1
+ BTXPCGetNextClientID.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __28-[BTAudioSession invalidate]_block_invoke.cold.1
+ __29-[BTBannerUISession activate]_block_invoke.cold.1
+ __30-[BTServicesClient invalidate]_block_invoke.cold.1
+ __34-[BTAudioRoutingRequest _activate]_block_invoke.33.cold.1
+ __34-[BTAudioRoutingRequest _activate]_block_invoke.33.cold.2
+ __34-[BTAudioRoutingRequest _activate]_block_invoke.cold.1
+ __35-[BTAudioRoutingRequest invalidate]_block_invoke.cold.1
+ __35-[BTCloudServicesClient invalidate]_block_invoke.cold.1
+ __38-[BTAudioRoutingRequest _activateSync]_block_invoke.cold.1
+ __38-[BTAudioRoutingRequest _activateSync]_block_invoke_2.cold.1
+ __38-[BTAudioRoutingRequest _activateSync]_block_invoke_2.cold.2
+ __41-[BTAudioSession activateWithCompletion:]_block_invoke.cold.1
+ __42-[BTAudioRoutingRequest _handleServerDied]_block_invoke.cold.1
+ __43-[BTAirPodsControlServiceClient invalidate]_block_invoke.cold.1
+ __44-[BTCloudServicesClient listenForUserChange]_block_invoke.cold.1
+ __48-[BTAirPodsControlServiceClient isFindmyManaged]_block_invoke.cold.1
+ __49-[BTAirPodsControlServiceClient _runConnectStart]_block_invoke.cold.1
+ __52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke.cold.1
+ __52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke.cold.2
+ __52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke.cold.3
+ __52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke_2.cold.1
+ __65-[BTAirPodsControlServiceClient setSilentMode:completionHandler:]_block_invoke.cold.1
+ __65-[BTAirPodsControlServiceClient setSilentMode:completionHandler:]_block_invoke.cold.2
+ __68-[BTAirPodsControlServiceClient getSilentModeWithCompletionHandler:]_block_invoke.cold.1
+ __68-[BTAirPodsControlServiceClient getSilentModeWithCompletionHandler:]_block_invoke.cold.2
+ ___52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke_2
+ ___block_descriptor_52_e8_32s40s_e5_v8?0l
+ dynamicStoreCallback.cold.1
+ initWPClient.cold.1
CStrings:
+ "-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke_2"
+ "BTMagicPairingSettings[%@]: Name(%lu), PID: %@, VID: %@"
+ "BTMagicPairingSettings[%@]: Name(%lu): %@, PID: %@, VID: %@, MainKey: %@, AccKey: %@, MainHint: %@, AccHint: %@, IRK: %@, Enc: %@, V: %@, C: %@, R: %@, BM: %@, DID1: %@, DID2: %@, LS: %@, LSv2: %@, S: %@, SS: %@, OBC: %@-%@"
- "-[BTAudioRoutingRequest updateAudioState:withState:]"
- "BTMagicPairingSettings[%@]: Name(%ld), PID: %@, VID: %@"
- "BTMagicPairingSettings[%@]: Name(%ld): %@, PID: %@, VID: %@, MainKey: %@, AccKey: %@, MainHint: %@, AccHint: %@, IRK: %@, Enc: %@, V: %@, C: %@, R: %@, BM: %@, DID1: %@, DID2: %@, LS: %@, LSv2: %@, S: %@, SS: %@, OBC: %@-%@"

```
