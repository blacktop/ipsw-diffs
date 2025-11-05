## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/Versions/A/AudioAccessoryServices`

```diff

-23.1.0.0.0
-  __TEXT.__text: 0x25a9c
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x2ab4
+24.26.0.0.0
+  __TEXT.__text: 0x29250
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x3234
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0xb08
-  __TEXT.__cstring: 0x6cf4
-  __TEXT.__unwind_info: 0x938
-  __TEXT.__objc_classname: 0x341
-  __TEXT.__objc_methname: 0x6f5d
-  __TEXT.__objc_methtype: 0xecf
-  __TEXT.__objc_stubs: 0x28a0
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x550
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__gcc_except_tab: 0xb04
+  __TEXT.__cstring: 0x6e39
+  __TEXT.__unwind_info: 0xb58
+  __TEXT.__objc_classname: 0x363
+  __TEXT.__objc_methname: 0x6da4
+  __TEXT.__objc_methtype: 0xf98
+  __TEXT.__objc_stubs: 0x2b60
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x460
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1530
+  __DATA_CONST.__objc_selrefs: 0x15e8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x350
-  __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0x12e0
-  __AUTH_CONST.__objc_const: 0x60d0
-  __AUTH.__objc_data: 0x780
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__cfstring: 0x1300
+  __AUTH_CONST.__objc_const: 0x56f0
+  __AUTH.__objc_data: 0x7d0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x594
-  __DATA.__data: 0xa50
-  __DATA.__bss: 0xb8
+  __DATA.__objc_ivar: 0x5a8
+  __DATA.__data: 0xac0
+  __DATA.__bss: 0xd8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C2E9BDB-C61A-37AD-89AF-9D6DAF57F42A
-  Functions: 1116
-  Symbols:   2337
-  CStrings:  2450
+  UUID: B7120F2E-7AB2-3EEC-8A67-ED0FD57BFF17
+  Functions: 1427
+  Symbols:   2724
+  CStrings:  2418
 
Symbols:
+ +[AASystemStateMonitor supportsSecureCoding]
+ +[AAUSBSupportedDeviceManager supportsSecureCoding]
+ -[AAAudioRoutingControl _activateDirect:].cold.1
+ -[AAAudioRoutingControl _activateXPC:].cold.1
+ -[AAAudioRoutingControl _activate].cold.1
+ -[AAAudioRoutingControl _activate].cold.2
+ -[AAAudioRoutingControl _ensureXPCStarted].cold.1
+ -[AAAudioRoutingControl _interrupted].cold.1
+ -[AAAudioRoutingControl _invalidated].cold.1
+ -[AAAudioRoutingControl _invalidated].cold.2
+ -[AAAudioRoutingControl _reportError:].cold.1
+ -[AAAudioRoutingControl isSystemContext].cold.1
+ -[AAAudioRoutingControl setArbitrationBlockingModeWithCompletion:completion:].cold.1
+ -[AAAudioRoutingControl setArbitrationBlockingModeWithCompletion:completion:].cold.2
+ -[AAAudioRoutingControl setArbitrationBlockingModeWithCompletion:completion:].cold.3
+ -[AAAudioSessionControl _activate:].cold.1
+ -[AAAudioSessionControl _activateDirect:].cold.1
+ -[AAAudioSessionControl _activateXPC:reactivate:].cold.1
+ -[AAAudioSessionControl _activateXPC:reactivate:].cold.2
+ -[AAAudioSessionControl _ensureXPCStarted].cold.1
+ -[AAAudioSessionControl _interrupted].cold.1
+ -[AAAudioSessionControl _invalidated].cold.1
+ -[AAAudioSessionControl _invalidated].cold.2
+ -[AAAudioSessionControl _reportError:].cold.1
+ -[AAAudioSessionControl isSystemContext].cold.1
+ -[AAAudioSessionControl setMuteAction:auditToken:bundleIdentifier:].cold.1
+ -[AACloudServicesClient _ensureXPCStarted].cold.1
+ -[AACloudServicesClient _ensureXPCStarted].cold.2
+ -[AACloudServicesClient _interrupted].cold.1
+ -[AACloudServicesClient _invalidated].cold.1
+ -[AACloudServicesClient _invalidated].cold.2
+ -[AACloudServicesClient _reportError:].cold.1
+ -[AACloudServicesClient hmDeviceCloudRecordInfosUpdated:].cold.1
+ -[AACloudServicesClient hmDeviceCloudRecordInfosUpdated:].cold.2
+ -[AACloudServicesClient isSystemContext].cold.1
+ -[AAController _activateXPC:].cold.1
+ -[AAController _activateXPCCompleted:].cold.1
+ -[AAController _activateXPCCompleted:].cold.2
+ -[AAController _interrupted].cold.1
+ -[AAController _invalidated].cold.1
+ -[AAController _sendAccessoryEventMessage:eventType:destinationIdentifier:completionHandler:].cold.1
+ -[AAController _sendAccessoryEventMessage:eventType:destinationIdentifier:completionHandler:].cold.2
+ -[AAController _sendDeviceConfig:destinationIdentifier:completionHandler:].cold.1
+ -[AAController _sendDeviceConfig:destinationIdentifier:completionHandler:].cold.2
+ -[AAController _xpcReceivedMessage:].cold.1
+ -[AAController _xpcReceivedMessage:].cold.2
+ -[AAController xpcReceivedMessage:].cold.1
+ -[AAController xpcReceivedMessage:].cold.2
+ -[AAController xpcReceivedMessage:].cold.3
+ -[AADeviceManager _activate:].cold.1
+ -[AADeviceManager _ensureXPCStarted].cold.1
+ -[AADeviceManager _interrupted].cold.1
+ -[AADeviceManager _invalidated].cold.1
+ -[AADeviceManager _invalidated].cold.2
+ -[AADeviceManager _reportError:].cold.1
+ -[AADeviceManager _reset].cold.1
+ -[AADeviceManager aaServicesRequireReset].cold.1
+ -[AADeviceManager deviceHeadGestureDetected:].cold.1
+ -[AADeviceManager deviceManagerFoundDevice:].cold.1
+ -[AADeviceManager isSystemContext].cold.1
+ -[AAProxCardsInfo setUsbAudioVersion:]
+ -[AAProxCardsInfo usbAudioVersion]
+ -[AASystemStateMonitor .cxx_destruct]
+ -[AASystemStateMonitor HRMCapableDeviceChangedHandler]
+ -[AASystemStateMonitor _activate:]
+ -[AASystemStateMonitor _activate:].cold.1
+ -[AASystemStateMonitor _activateDirect:]
+ -[AASystemStateMonitor _activateDirect:].cold.1
+ -[AASystemStateMonitor _activateXPC:reactivate:]
+ -[AASystemStateMonitor _activateXPC:reactivate:].cold.1
+ -[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]
+ -[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted].cold.1
+ -[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStopped]
+ -[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStopped].cold.1
+ -[AASystemStateMonitor _connectedDeviceFound:]
+ -[AASystemStateMonitor _connectedDeviceLost:]
+ -[AASystemStateMonitor _ensureXPCStarted]
+ -[AASystemStateMonitor _ensureXPCStarted].cold.1
+ -[AASystemStateMonitor _interrupted]
+ -[AASystemStateMonitor _interrupted].cold.1
+ -[AASystemStateMonitor _invalidateDirect]
+ -[AASystemStateMonitor _invalidated]
+ -[AASystemStateMonitor _invalidated].cold.1
+ -[AASystemStateMonitor _invalidated].cold.2
+ -[AASystemStateMonitor _reportError:]
+ -[AASystemStateMonitor _reportError:].cold.1
+ -[AASystemStateMonitor aaDeviceConnectionChanged:withAADevice:]
+ -[AASystemStateMonitor aaDeviceConnectionChanged:withAADevice:].cold.1
+ -[AASystemStateMonitor aaDeviceConnectionChangedHandler]
+ -[AASystemStateMonitor aaDeviceRouteChanged:withAADevice:]
+ -[AASystemStateMonitor aaDeviceRouteChanged:withAADevice:].cold.1
+ -[AASystemStateMonitor aaDeviceRouteChanged:withAADevice:].cold.2
+ -[AASystemStateMonitor aaDeviceRouteChangedHandler]
+ -[AASystemStateMonitor activateWithCompletion:]
+ -[AASystemStateMonitor clientID]
+ -[AASystemStateMonitor connectedDiscovery]
+ -[AASystemStateMonitor description]
+ -[AASystemStateMonitor devicesMap]
+ -[AASystemStateMonitor direct]
+ -[AASystemStateMonitor dispatchQueue]
+ -[AASystemStateMonitor encodeWithCoder:]
+ -[AASystemStateMonitor initWithCoder:]
+ -[AASystemStateMonitor init]
+ -[AASystemStateMonitor internalServicesDaemon]
+ -[AASystemStateMonitor interruptionHandler]
+ -[AASystemStateMonitor invalidate]
+ -[AASystemStateMonitor invalidationHandler]
+ -[AASystemStateMonitor isHRMCapableDevicePresent]
+ -[AASystemStateMonitor isSystemContext]
+ -[AASystemStateMonitor isSystemContext].cold.1
+ -[AASystemStateMonitor setAaDeviceConnectionChangedHandler:]
+ -[AASystemStateMonitor setAaDeviceRouteChangedHandler:]
+ -[AASystemStateMonitor setClientID:]
+ -[AASystemStateMonitor setConnectedDiscovery:]
+ -[AASystemStateMonitor setDevicesMap:]
+ -[AASystemStateMonitor setDispatchQueue:]
+ -[AASystemStateMonitor setHRMCapableDeviceChangedHandler:]
+ -[AASystemStateMonitor setInternalServicesDaemon:]
+ -[AASystemStateMonitor setInterruptionHandler:]
+ -[AASystemStateMonitor setInvalidationHandler:]
+ -[AASystemStateMonitor setTestListenerEndpoint:]
+ -[AASystemStateMonitor testListenerEndpoint]
+ -[AAUSBSupportedDeviceManager .cxx_destruct]
+ -[AAUSBSupportedDeviceManager _ensureXPCStarted]
+ -[AAUSBSupportedDeviceManager _ensureXPCStarted].cold.1
+ -[AAUSBSupportedDeviceManager _handleServerDied]
+ -[AAUSBSupportedDeviceManager _interrupted]
+ -[AAUSBSupportedDeviceManager _interrupted].cold.1
+ -[AAUSBSupportedDeviceManager _invalidated]
+ -[AAUSBSupportedDeviceManager _invalidated].cold.1
+ -[AAUSBSupportedDeviceManager _invalidated].cold.2
+ -[AAUSBSupportedDeviceManager _reportError:]
+ -[AAUSBSupportedDeviceManager _reportError:].cold.1
+ -[AAUSBSupportedDeviceManager clientID]
+ -[AAUSBSupportedDeviceManager description]
+ -[AAUSBSupportedDeviceManager dispatchQueue]
+ -[AAUSBSupportedDeviceManager encodeWithCoder:]
+ -[AAUSBSupportedDeviceManager initWithCoder:]
+ -[AAUSBSupportedDeviceManager init]
+ -[AAUSBSupportedDeviceManager invalidate]
+ -[AAUSBSupportedDeviceManager isSystemContext]
+ -[AAUSBSupportedDeviceManager isSystemContext].cold.1
+ -[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]
+ -[AAUSBSupportedDeviceManager setClientID:]
+ -[AAUSBSupportedDeviceManager setDispatchQueue:]
+ -[AudioAccessoryDevice routed]
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
+ AAXPCGetNextClientID.cold.1
+ BTXPCGetNextClientID.cold.1
+ OBJC_IVAR_$_AAProxCardsInfo._usbAudioVersion
+ OBJC_IVAR_$_AASystemStateMonitor._HRMCapableDeviceChangedHandler
+ OBJC_IVAR_$_AASystemStateMonitor._aaDeviceConnectionChangedHandler
+ OBJC_IVAR_$_AASystemStateMonitor._aaDeviceRouteChangedHandler
+ OBJC_IVAR_$_AASystemStateMonitor._activateCalled
+ OBJC_IVAR_$_AASystemStateMonitor._activateCompletion
+ OBJC_IVAR_$_AASystemStateMonitor._clientID
+ OBJC_IVAR_$_AASystemStateMonitor._connectedDiscovery
+ OBJC_IVAR_$_AASystemStateMonitor._devicesMap
+ OBJC_IVAR_$_AASystemStateMonitor._dispatchQueue
+ OBJC_IVAR_$_AASystemStateMonitor._internalServicesDaemon
+ OBJC_IVAR_$_AASystemStateMonitor._interruptionHandler
+ OBJC_IVAR_$_AASystemStateMonitor._invalidateCalled
+ OBJC_IVAR_$_AASystemStateMonitor._invalidateDone
+ OBJC_IVAR_$_AASystemStateMonitor._invalidationHandler
+ OBJC_IVAR_$_AASystemStateMonitor._isHRMCapableDevicePresent
+ OBJC_IVAR_$_AASystemStateMonitor._resetOngoing
+ OBJC_IVAR_$_AASystemStateMonitor._testListenerEndpoint
+ OBJC_IVAR_$_AASystemStateMonitor._xpcCnx
+ OBJC_IVAR_$_AAUSBSupportedDeviceManager._activateCompletion
+ OBJC_IVAR_$_AAUSBSupportedDeviceManager._clientID
+ OBJC_IVAR_$_AAUSBSupportedDeviceManager._dispatchQueue
+ OBJC_IVAR_$_AAUSBSupportedDeviceManager._invalidateCalled
+ OBJC_IVAR_$_AAUSBSupportedDeviceManager._invalidateDone
+ OBJC_IVAR_$_AAUSBSupportedDeviceManager._xpcCnx
+ _OBJC_CLASS_$_AASystemStateMonitor
+ _OBJC_CLASS_$_AAUSBSupportedDeviceManager
+ _OBJC_METACLASS_$_AASystemStateMonitor
+ _OBJC_METACLASS_$_AAUSBSupportedDeviceManager
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
+ __25-[AADeviceManager _reset]_block_invoke_2.cold.1
+ __26-[AAController invalidate]_block_invoke.cold.1
+ __28-[BTAudioSession invalidate]_block_invoke.cold.1
+ __29-[AADeviceManager _activate:]_block_invoke.22.cold.1
+ __29-[AADeviceManager _activate:]_block_invoke.22.cold.2
+ __29-[AADeviceManager _activate:]_block_invoke.cold.1
+ __29-[AADeviceManager _activate:]_block_invoke.cold.2
+ __29-[AADeviceManager invalidate]_block_invoke.cold.1
+ __29-[BTBannerUISession activate]_block_invoke.cold.1
+ __30-[BTServicesClient invalidate]_block_invoke.cold.1
+ __34-[AAAudioRoutingControl _activate]_block_invoke.cold.1
+ __34-[AACloudServicesClient _activate]_block_invoke.14.cold.1
+ __34-[AACloudServicesClient _activate]_block_invoke.17.cold.1
+ __34-[AACloudServicesClient _activate]_block_invoke.17.cold.2
+ __34-[AASystemStateMonitor _activate:]_block_invoke.cold.1
+ __34-[AASystemStateMonitor _activate:]_block_invoke.cold.2
+ __34-[AASystemStateMonitor invalidate]_block_invoke.cold.1
+ __34-[BTAudioRoutingRequest _activate]_block_invoke.33.cold.1
+ __34-[BTAudioRoutingRequest _activate]_block_invoke.33.cold.2
+ __34-[BTAudioRoutingRequest _activate]_block_invoke.cold.1
+ __35-[AAAudioRoutingControl invalidate]_block_invoke.cold.1
+ __35-[AAAudioSessionControl _activate:]_block_invoke.cold.1
+ __35-[AAAudioSessionControl _activate:]_block_invoke.cold.2
+ __35-[AAAudioSessionControl invalidate]_block_invoke.cold.1
+ __35-[AACloudServicesClient invalidate]_block_invoke.cold.1
+ __35-[BTAudioRoutingRequest invalidate]_block_invoke.cold.1
+ __35-[BTCloudServicesClient invalidate]_block_invoke.cold.1
+ __38-[AAAudioRoutingControl _activateXPC:]_block_invoke.cold.1
+ __38-[BTAudioRoutingRequest _activateSync]_block_invoke.cold.1
+ __38-[BTAudioRoutingRequest _activateSync]_block_invoke_2.cold.1
+ __38-[BTAudioRoutingRequest _activateSync]_block_invoke_2.cold.2
+ __41-[AASystemStateMonitor _ensureXPCStarted]_block_invoke.30
+ __41-[AAUSBSupportedDeviceManager invalidate]_block_invoke.cold.1
+ __41-[BTAudioSession activateWithCompletion:]_block_invoke.cold.1
+ __42-[AAAudioRoutingControl _handleServerDied]_block_invoke.cold.1
+ __42-[AADeviceManager activateWithCompletion:]_block_invoke.cold.1
+ __42-[BTAudioRoutingRequest _handleServerDied]_block_invoke.cold.1
+ __43-[BTAirPodsControlServiceClient invalidate]_block_invoke.cold.1
+ __44-[BTCloudServicesClient listenForUserChange]_block_invoke.cold.1
+ __45-[AADeviceManager setHeadGestureUpdateFlags:]_block_invoke.6.cold.1
+ __45-[AADeviceManager setHeadGestureUpdateFlags:]_block_invoke.6.cold.2
+ __47-[AASystemStateMonitor activateWithCompletion:]_block_invoke.cold.1
+ __48-[AAAudioRoutingControl activateWithCompletion:]_block_invoke.cold.1
+ __48-[AAAudioSessionControl activateWithCompletion:]_block_invoke.cold.1
+ __48-[AACloudServicesClient activateWithCompletion:]_block_invoke.cold.1
+ __48-[AASystemStateMonitor _activateXPC:reactivate:]_block_invoke.15
+ __48-[AASystemStateMonitor _activateXPC:reactivate:]_block_invoke.cold.1
+ __48-[AASystemStateMonitor _activateXPC:reactivate:]_block_invoke.cold.2
+ __48-[AAUSBSupportedDeviceManager _ensureXPCStarted]_block_invoke.19
+ __48-[AAUSBSupportedDeviceManager _handleServerDied]_block_invoke.cold.1
+ __48-[BTAirPodsControlServiceClient isFindmyManaged]_block_invoke.cold.1
+ __49-[AAAudioSessionControl _activateXPC:reactivate:]_block_invoke.cold.1
+ __49-[AAAudioSessionControl _activateXPC:reactivate:]_block_invoke.cold.2
+ __49-[BTAirPodsControlServiceClient _runConnectStart]_block_invoke.cold.1
+ __52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke.cold.1
+ __52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke.cold.2
+ __52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke.cold.3
+ __52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke_2.cold.1
+ __58-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke.84
+ __58-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke.84.cold.1
+ __58-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke_2.cold.1
+ __59-[AAAudioRoutingControl hrmSessionStateChanged:completion:]_block_invoke.cold.1
+ __59-[AAAudioRoutingControl hrmSessionStateChanged:completion:]_block_invoke.cold.2
+ __62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke.80
+ __62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke.cold.1
+ __62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_2.81
+ __62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_2.81.cold.1
+ __62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_2.81.cold.2
+ __62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_2.cold.1
+ __65-[BTAirPodsControlServiceClient setSilentMode:completionHandler:]_block_invoke.cold.1
+ __65-[BTAirPodsControlServiceClient setSilentMode:completionHandler:]_block_invoke.cold.2
+ __67-[AAAudioSessionControl setMuteAction:auditToken:bundleIdentifier:]_block_invoke.cold.1
+ __67-[AAAudioSessionControl setMuteAction:auditToken:bundleIdentifier:]_block_invoke.cold.2
+ __68-[BTAirPodsControlServiceClient getSilentModeWithCompletionHandler:]_block_invoke.cold.1
+ __68-[BTAirPodsControlServiceClient getSilentModeWithCompletionHandler:]_block_invoke.cold.2
+ __73-[AAController sendDeviceConfig:destinationIdentifier:completionHandler:]_block_invoke.cold.1
+ __74-[AAController sendPMEConfigData:destinationIdentifier:completionHandler:]_block_invoke.cold.1
+ __77-[AAAudioRoutingControl setArbitrationBlockingModeWithCompletion:completion:]_block_invoke.cold.1
+ __81-[AAController sendGetTipiTableMessageToDestinationIdentifier:completionHandler:]_block_invoke.cold.1
+ __83-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke.cold.1
+ __83-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke.cold.2
+ __83-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke.cold.3
+ __83-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke_2.cold.1
+ __85-[AAController sendMultimodalContextMessage:destinationIdentifier:completionHandler:]_block_invoke.cold.1
+ __86-[AAController sendConversationDetectMessage:destinationIdentifier:completionHandler:]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_AASystemStateMonitor
+ __OBJC_$_CLASS_METHODS_AAUSBSupportedDeviceManager
+ __OBJC_$_CLASS_PROP_LIST_AASystemStateMonitor
+ __OBJC_$_CLASS_PROP_LIST_AAUSBSupportedDeviceManager
+ __OBJC_$_INSTANCE_METHODS_AASystemStateMonitor
+ __OBJC_$_INSTANCE_METHODS_AAUSBSupportedDeviceManager
+ __OBJC_$_INSTANCE_VARIABLES_AASystemStateMonitor
+ __OBJC_$_INSTANCE_VARIABLES_AAUSBSupportedDeviceManager
+ __OBJC_$_PROP_LIST_AASystemStateMonitor
+ __OBJC_$_PROP_LIST_AAUSBSupportedDeviceManager
+ __OBJC_CLASS_PROTOCOLS_$_AASystemStateMonitor
+ __OBJC_CLASS_PROTOCOLS_$_AAUSBSupportedDeviceManager
+ __OBJC_CLASS_RO_$_AASystemStateMonitor
+ __OBJC_CLASS_RO_$_AAUSBSupportedDeviceManager
+ __OBJC_METACLASS_RO_$_AASystemStateMonitor
+ __OBJC_METACLASS_RO_$_AAUSBSupportedDeviceManager
+ ___34-[AASystemStateMonitor _activate:]_block_invoke
+ ___34-[AASystemStateMonitor invalidate]_block_invoke
+ ___39-[AASystemStateMonitor isSystemContext]_block_invoke
+ ___41-[AASystemStateMonitor _ensureXPCStarted]_block_invoke
+ ___41-[AAUSBSupportedDeviceManager invalidate]_block_invoke
+ ___46-[AAUSBSupportedDeviceManager isSystemContext]_block_invoke
+ ___47-[AASystemStateMonitor activateWithCompletion:]_block_invoke
+ ___48-[AASystemStateMonitor _activateXPC:reactivate:]_block_invoke
+ ___48-[AAUSBSupportedDeviceManager _ensureXPCStarted]_block_invoke
+ ___48-[AAUSBSupportedDeviceManager _handleServerDied]_block_invoke
+ ___52-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke_2
+ ___62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke
+ ___62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_2
+ ___62-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_3
+ ___83-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke
+ ___83-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e30_v16?0"AudioAccessoryDevice"8l
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_52_e8_32s40s_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0l
+ __block_literal_global.57
+ __block_literal_global.72
+ __block_literal_global.75
+ _gLogCategory_AASystemStateMonitor
+ _gLogCategory_AAUSBSupportedDeviceManager
+ _objc_getProperty
+ _objc_msgSend$_connectedDeviceDiscoveryEnsureStarted
+ _objc_msgSend$_connectedDeviceDiscoveryEnsureStopped
+ _objc_msgSend$_connectedDeviceFound:
+ _objc_msgSend$_connectedDeviceLost:
+ _objc_msgSend$aaDeviceConnectionChanged:withAADevice:
+ _objc_msgSend$aaDeviceRouteChanged:withAADevice:
+ _objc_msgSend$activateSystemStateMonitorDirect:completion:
+ _objc_msgSend$activateWithCompletion:
+ _objc_msgSend$connectedDiscovery
+ _objc_msgSend$devicesMap
+ _objc_msgSend$direct
+ _objc_msgSend$internalServicesDaemon
+ _objc_msgSend$invalidateSystemStateMonitorDirect:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$proxCardUserActionOnHeadphone:btAddress:withAction:completion:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$routed
+ _objc_msgSend$setConnectedDiscovery:
+ _objc_msgSend$setDeviceFoundHandler:
+ _objc_msgSend$setDeviceLostHandler:
+ _objc_msgSend$setDevicesMap:
+ _objc_msgSend$setDispatchQueue:
+ _objc_msgSend$smartRoutingStateFlags
+ _objc_msgSend$systemStateMonitorActivate:completion:
+ _objc_setProperty_atomic_copy
+ dynamicStoreCallback.cold.1
+ initWPClient.cold.1
- -[SRDiscoveredDevice .cxx_destruct]
- -[SRDiscoveredDevice _setBtAddress:]
- -[SRDiscoveredDevice _setConnectionState:]
- -[SRDiscoveredDevice _setInUseBannerBackoffReason:]
- -[SRDiscoveredDevice _setInUseBannerBackoffTick:]
- -[SRDiscoveredDevice _setInUseBannerShown:]
- -[SRDiscoveredDevice _setIsNearby:]
- -[SRDiscoveredDevice _setMutedSpeakerForRemotePhoneCall:]
- -[SRDiscoveredDevice _setNearbyConnectedSourceCount:]
- -[SRDiscoveredDevice _setNearbyInEar:]
- -[SRDiscoveredDevice _setNearbyLastRouteHost:]
- -[SRDiscoveredDevice _setNearbyName:]
- -[SRDiscoveredDevice _setNearbyOutOfCaseTime:]
- -[SRDiscoveredDevice _setNearbyPaired:]
- -[SRDiscoveredDevice _setNearbyPrevInEar:]
- -[SRDiscoveredDevice _setNearbyProductID:]
- -[SRDiscoveredDevice _setNearbyStreamState:]
- -[SRDiscoveredDevice _setNearbyWxDevice:]
- -[SRDiscoveredDevice _setNearbyiCloudSignIn:]
- -[SRDiscoveredDevice _setRouteToWxAfterUnhide:]
- -[SRDiscoveredDevice _setUserConnectedState:]
- -[SRDiscoveredDevice btAddress]
- -[SRDiscoveredDevice connectionState]
- -[SRDiscoveredDevice inUseBannerBackoffReason]
- -[SRDiscoveredDevice inUseBannerBackoffTick]
- -[SRDiscoveredDevice inUseBannerShown]
- -[SRDiscoveredDevice isNearby]
- -[SRDiscoveredDevice mutedSpeakerForRemotePhoneCall]
- -[SRDiscoveredDevice nearbyConnectedSourceCount]
- -[SRDiscoveredDevice nearbyInEar]
- -[SRDiscoveredDevice nearbyLastRouteHost]
- -[SRDiscoveredDevice nearbyName]
- -[SRDiscoveredDevice nearbyOutOfCaseTime]
- -[SRDiscoveredDevice nearbyPaired]
- -[SRDiscoveredDevice nearbyPrevInEar]
- -[SRDiscoveredDevice nearbyProductID]
- -[SRDiscoveredDevice nearbyStreamState]
- -[SRDiscoveredDevice nearbyWxDevice]
- -[SRDiscoveredDevice nearbyiCloudSignIn]
- -[SRDiscoveredDevice routeToWxAfterUnhide]
- -[SRDiscoveredDevice userConnectedState]
- OBJC_IVAR_$_SRDiscoveredDevice._btAddress
- OBJC_IVAR_$_SRDiscoveredDevice._connectionState
- OBJC_IVAR_$_SRDiscoveredDevice._inUseBannerBackoffReason
- OBJC_IVAR_$_SRDiscoveredDevice._inUseBannerBackoffTick
- OBJC_IVAR_$_SRDiscoveredDevice._inUseBannerShown
- OBJC_IVAR_$_SRDiscoveredDevice._isNearby
- OBJC_IVAR_$_SRDiscoveredDevice._mutedSpeakerForRemotePhoneCall
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyConnectedSourceCount
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyInEar
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyLastRouteHost
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyName
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyOutOfCaseTime
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyPaired
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyPrevInEar
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyProductID
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyStreamState
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyWxDevice
- OBJC_IVAR_$_SRDiscoveredDevice._nearbyiCloudSignIn
- OBJC_IVAR_$_SRDiscoveredDevice._routeToWxAfterUnhide
- OBJC_IVAR_$_SRDiscoveredDevice._userConnectedState
- _OBJC_CLASS_$_SRDiscoveredDevice
- _OBJC_METACLASS_$_SRDiscoveredDevice
- __58-[AADeviceManager sendDeviceConfig:identifier:completion:]_block_invoke.79
- __OBJC_$_INSTANCE_METHODS_SRDiscoveredDevice
- __OBJC_$_INSTANCE_VARIABLES_SRDiscoveredDevice
- __OBJC_$_PROP_LIST_SRDiscoveredDevice
- __OBJC_CLASS_RO_$_SRDiscoveredDevice
- __OBJC_METACLASS_RO_$_SRDiscoveredDevice
- _gLogCategory_SRDiscoveredDevice
- _objc_msgSend$isEqualToData:
- _objc_msgSend$isEqualToString:
CStrings:
+ "### Activate failed: %{error}\n"
+ "### proxCardUserActionOnHeadphone failed to start XPC"
+ "### proxCardUserActionOnHeadphone no XPC"
+ ", USB Ad %llu"
+ "-[AASystemStateMonitor _activate:]"
+ "-[AASystemStateMonitor _activate:]_block_invoke"
+ "-[AASystemStateMonitor _activateDirect:]"
+ "-[AASystemStateMonitor _activateXPC:reactivate:]"
+ "-[AASystemStateMonitor _activateXPC:reactivate:]_block_invoke"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_2"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStopped]"
+ "-[AASystemStateMonitor _ensureXPCStarted]"
+ "-[AASystemStateMonitor _interrupted]"
+ "-[AASystemStateMonitor _invalidated]"
+ "-[AASystemStateMonitor _reportError:]"
+ "-[AASystemStateMonitor aaDeviceConnectionChanged:withAADevice:]"
+ "-[AASystemStateMonitor aaDeviceRouteChanged:withAADevice:]"
+ "-[AASystemStateMonitor activateWithCompletion:]_block_invoke"
+ "-[AASystemStateMonitor invalidate]_block_invoke"
+ "-[AAUSBSupportedDeviceManager _ensureXPCStarted]"
+ "-[AAUSBSupportedDeviceManager _handleServerDied]_block_invoke"
+ "-[AAUSBSupportedDeviceManager _interrupted]"
+ "-[AAUSBSupportedDeviceManager _invalidated]"
+ "-[AAUSBSupportedDeviceManager _reportError:]"
+ "-[AAUSBSupportedDeviceManager invalidate]_block_invoke"
+ "-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke"
+ "-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke_2"
+ "-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke_2"
+ "@\"AADeviceManager\""
+ "@\"AAServicesDaemon\""
+ "AASystemStateMonitor"
+ "AASystemStateMonitor, CID 0x%X"
+ "AAUSBSupportedDeviceManager"
+ "AAUSBSupportedDeviceManager, CID 0x%X"
+ "BTMagicPairingSettings[%@]: Name(%lu), PID: %@, VID: %@"
+ "BTMagicPairingSettings[%@]: Name(%lu): %@, PID: %@, VID: %@, MainKey: %@, AccKey: %@, MainHint: %@, AccHint: %@, IRK: %@, Enc: %@, V: %@, C: %@, R: %@, BM: %@, DID1: %@, DID2: %@, LS: %@, LSv2: %@, S: %@, SS: %@, OBC: %@-%@"
+ "Calling connection changed handler with device %@, CID 0x%X"
+ "Calling route changed handler with device %@"
+ "Connected discovery start"
+ "Connected discovery stop"
+ "DeviceManager interrupted"
+ "DeviceManager invalidated"
+ "HRMCapableDeviceChangedHandler"
+ "T@\"AADeviceManager\",&,N,V_connectedDiscovery"
+ "T@\"AAServicesDaemon\",&,N,V_internalServicesDaemon"
+ "T@\"NSMutableDictionary\",&,N,V_devicesMap"
+ "T@?,C,V_HRMCapableDeviceChangedHandler"
+ "T@?,C,V_aaDeviceConnectionChangedHandler"
+ "T@?,C,V_aaDeviceRouteChangedHandler"
+ "TB,R,N"
+ "TB,R,V_isHRMCapableDevicePresent"
+ "TQ,V_usbAudioVersion"
+ "_HRMCapableDeviceChangedHandler"
+ "_aaDeviceConnectionChangedHandler"
+ "_aaDeviceRouteChangedHandler"
+ "_connectedDeviceDiscoveryEnsureStarted"
+ "_connectedDeviceDiscoveryEnsureStopped"
+ "_connectedDeviceFound:"
+ "_connectedDeviceLost:"
+ "_connectedDiscovery"
+ "_devicesMap"
+ "_internalServicesDaemon"
+ "_isHRMCapableDevicePresent"
+ "_usbAudioVersion"
+ "aaDeviceConnectionChanged:withAADevice:"
+ "aaDeviceConnectionChangedHandler"
+ "aaDeviceRouteChanged:withAADevice:"
+ "aaDeviceRouteChangedHandler"
+ "activateSystemStateMonitorDirect:completion:"
+ "connectedDiscovery"
+ "devicesMap"
+ "direct"
+ "internalServicesDaemon"
+ "invalidateSystemStateMonitorDirect:"
+ "isHRMCapableDevicePresent"
+ "objectForKeyedSubscript:"
+ "proxCardUserActionOnHeadphone CID 0x%X device %@"
+ "proxCardUserActionOnHeadphone:btAddress:withAction:completion:"
+ "proxCardUserActionOnHeadphone:withAction:completion:"
+ "removeObjectForKey:"
+ "routed"
+ "setAaDeviceConnectionChangedHandler:"
+ "setAaDeviceRouteChangedHandler:"
+ "setConnectedDiscovery:"
+ "setDevicesMap:"
+ "setHRMCapableDeviceChangedHandler:"
+ "setInternalServicesDaemon:"
+ "setUsbAudioVersion:"
+ "systemStateMonitorActivate:completion:"
+ "usbA"
+ "usbAudioVersion"
+ "v16@?0@\"AudioAccessoryDevice\"8"
+ "v28@0:8B16@20"
+ "v32@0:8@\"AASystemStateMonitor\"16@?<v@?@\"NSError\">24"
+ "v36@0:8@16C24@?28"
+ "v44@0:8@\"AAUSBSupportedDeviceManager\"16@\"NSString\"24C32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8@16@24C32@?36"
- "-[BTAudioRoutingRequest updateAudioState:withState:]"
- "-[SRDiscoveredDevice _setBtAddress:]"
- "-[SRDiscoveredDevice _setConnectionState:]"
- "-[SRDiscoveredDevice _setInUseBannerBackoffReason:]"
- "-[SRDiscoveredDevice _setInUseBannerBackoffTick:]"
- "-[SRDiscoveredDevice _setInUseBannerShown:]"
- "-[SRDiscoveredDevice _setIsNearby:]"
- "-[SRDiscoveredDevice _setMutedSpeakerForRemotePhoneCall:]"
- "-[SRDiscoveredDevice _setNearbyConnectedSourceCount:]"
- "-[SRDiscoveredDevice _setNearbyInEar:]"
- "-[SRDiscoveredDevice _setNearbyLastRouteHost:]"
- "-[SRDiscoveredDevice _setNearbyName:]"
- "-[SRDiscoveredDevice _setNearbyOutOfCaseTime:]"
- "-[SRDiscoveredDevice _setNearbyPaired:]"
- "-[SRDiscoveredDevice _setNearbyPrevInEar:]"
- "-[SRDiscoveredDevice _setNearbyProductID:]"
- "-[SRDiscoveredDevice _setNearbyStreamState:]"
- "-[SRDiscoveredDevice _setNearbyiCloudSignIn:]"
- "-[SRDiscoveredDevice _setRouteToWxAfterUnhide:]"
- "-[SRDiscoveredDevice _setUserConnectedState:]"
- "@\"SFDevice\""
- "BTMagicPairingSettings[%@]: Name(%ld), PID: %@, VID: %@"
- "BTMagicPairingSettings[%@]: Name(%ld): %@, PID: %@, VID: %@, MainKey: %@, AccKey: %@, MainHint: %@, AccHint: %@, IRK: %@, Enc: %@, V: %@, C: %@, R: %@, BM: %@, DID1: %@, DID2: %@, LS: %@, LSv2: %@, S: %@, SS: %@, OBC: %@-%@"
- "Disconnected"
- "Disconnecting"
- "HFP Call"
- "HFP Other"
- "SRDiscoveredDevice"
- "Setting btaddress %@ -> %@"
- "Setting connectionState %s -> %s"
- "Setting inUseBannerBackoff %@ %@ -> %@"
- "Setting inUseBannerBackoffTick %@ %u -> %u"
- "Setting inUseBannerShown %@ %s -> %s"
- "Setting isNearby %@ %s -> %s"
- "Setting muted speaker for remote phone call %s -> %s"
- "Setting nearbyConnectedSourceCount %@ %d -> %d"
- "Setting nearbyInEar %@ %s -> %s"
- "Setting nearbyLastRouteHost %@ %@ -> %@"
- "Setting nearbyName %@ %@ -> %@"
- "Setting nearbyPaired %@ %s -> %s"
- "Setting nearbyPrevInEar %@ %s -> %s"
- "Setting nearbyProductID %@ %u -> %u"
- "Setting nearbyStreamState %@ %s -> %s"
- "Setting nearbyiCloudSignIn %@ %s -> %s"
- "Setting outOfCaseTime %@ %d -> %d"
- "Setting routeToWxAfterUnhide %@ %s -> %s"
- "Setting userConnectedState %s -> %s"
- "T@\"NSData\",R,N,V_nearbyLastRouteHost"
- "T@\"NSString\",R,C,N,V_btAddress"
- "T@\"NSString\",R,C,N,V_nearbyName"
- "T@\"NSString\",R,N,V_inUseBannerBackoffReason"
- "T@\"SFDevice\",R,C,N,V_nearbyWxDevice"
- "TB,R,N,V_inUseBannerShown"
- "TB,R,N,V_isNearby"
- "TB,R,N,V_mutedSpeakerForRemotePhoneCall"
- "TB,R,N,V_nearbyPaired"
- "TB,R,N,V_nearbyiCloudSignIn"
- "TB,R,N,V_routeToWxAfterUnhide"
- "TB,R,N,V_userConnectedState"
- "TC,R,N,V_connectionState"
- "TC,R,N,V_nearbyConnectedSourceCount"
- "TC,R,N,V_nearbyOutOfCaseTime"
- "TI,R,N,V_nearbyProductID"
- "TQ,R,N,V_inUseBannerBackoffTick"
- "Ti,R,N,V_nearbyInEar"
- "Ti,R,N,V_nearbyPrevInEar"
- "Tq,R,N,V_nearbyStreamState"
- "Unspecified"
- "_btAddress"
- "_connectionState"
- "_inUseBannerBackoffReason"
- "_inUseBannerBackoffTick"
- "_inUseBannerShown"
- "_isNearby"
- "_mutedSpeakerForRemotePhoneCall"
- "_nearbyConnectedSourceCount"
- "_nearbyInEar"
- "_nearbyLastRouteHost"
- "_nearbyName"
- "_nearbyOutOfCaseTime"
- "_nearbyPaired"
- "_nearbyPrevInEar"
- "_nearbyProductID"
- "_nearbyStreamState"
- "_nearbyWxDevice"
- "_nearbyiCloudSignIn"
- "_routeToWxAfterUnhide"
- "_setBtAddress:"
- "_setConnectionState:"
- "_setInUseBannerBackoffReason:"
- "_setInUseBannerBackoffTick:"
- "_setInUseBannerShown:"
- "_setIsNearby:"
- "_setMutedSpeakerForRemotePhoneCall:"
- "_setNearbyConnectedSourceCount:"
- "_setNearbyInEar:"
- "_setNearbyLastRouteHost:"
- "_setNearbyName:"
- "_setNearbyOutOfCaseTime:"
- "_setNearbyPaired:"
- "_setNearbyPrevInEar:"
- "_setNearbyProductID:"
- "_setNearbyStreamState:"
- "_setNearbyWxDevice:"
- "_setNearbyiCloudSignIn:"
- "_setRouteToWxAfterUnhide:"
- "_setUserConnectedState:"
- "_userConnectedState"
- "btAddress"
- "connectionState"
- "inUseBannerBackoffReason"
- "inUseBannerBackoffTick"
- "inUseBannerShown"
- "isEqualToData:"
- "isEqualToString:"
- "isNearby"
- "mutedSpeakerForRemotePhoneCall"
- "nearbyConnectedSourceCount"
- "nearbyInEar"
- "nearbyLastRouteHost"
- "nearbyName"
- "nearbyOutOfCaseTime"
- "nearbyPaired"
- "nearbyPrevInEar"
- "nearbyProductID"
- "nearbyStreamState"
- "nearbyWxDevice"
- "nearbyiCloudSignIn"
- "q"
- "q16@0:8"
- "routeToWxAfterUnhide"
- "userConnectedState"
- "v24@0:8q16"

```
