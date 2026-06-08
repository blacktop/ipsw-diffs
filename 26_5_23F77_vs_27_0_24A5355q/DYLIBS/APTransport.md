## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0xa60f0
-  __TEXT.__auth_stubs: 0x3260
-  __TEXT.__objc_methlist: 0x13f4
-  __TEXT.__cstring: 0x2c4ad
-  __TEXT.__const: 0x3e0
-  __TEXT.__gcc_except_tab: 0x71c
-  __TEXT.__oslogstring: 0x16e
+980.58.1.11.1
+  __TEXT.__text: 0xb3810
+  __TEXT.__objc_methlist: 0x1cf4
+  __TEXT.__const: 0x418
+  __TEXT.__gcc_except_tab: 0x9d8
+  __TEXT.__cstring: 0x2f773
   __TEXT.__dlopen_cstrs: 0x1f3
-  __TEXT.__unwind_info: 0x2878
-  __TEXT.__objc_classname: 0x1f5
-  __TEXT.__objc_methname: 0x4c39
-  __TEXT.__objc_methtype: 0x101f
-  __TEXT.__objc_stubs: 0x43e0
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x36a8
-  __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x50
+  __TEXT.__oslogstring: 0x31c
+  __TEXT.__unwind_info: 0x2c60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3cc0
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e0
-  __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x1940
-  __AUTH_CONST.__const: 0x2b68
-  __AUTH_CONST.__cfstring: 0x5ea0
-  __AUTH_CONST.__objc_const: 0x1ce0
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0x278
-  __DATA.__objc_ivar: 0x170
-  __DATA.__data: 0x1350
-  __DATA.__bss: 0x138
-  __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__data: 0xaf0
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_CONST.__objc_selrefs: 0x1b38
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__got: 0x438
+  __AUTH_CONST.__const: 0x2d38
+  __AUTH_CONST.__cfstring: 0x63a0
+  __AUTH_CONST.__objc_const: 0x2498
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x1e0
+  __AUTH.__data: 0x2c0
+  __DATA.__objc_ivar: 0x18c
+  __DATA.__data: 0x1580
+  __DATA.__bss: 0x148
+  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__data: 0xbd0
+  __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
-  - /System/Library/PrivateFrameworks/IO80211.framework/IO80211
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
-  - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F15B8E8-8447-3D9E-AA71-AAB8B9839174
-  Functions: 4933
-  Symbols:   12657
-  CStrings:  5953
+  UUID: A4CCF876-2982-360B-9717-F6B8FA9A5145
+  Functions: 5278
+  Symbols:   13570
+  CStrings:  5282
 
Symbols:
+ +[APHomeManagerInterface shared]
+ +[APHomeManagerInterface shared].cold.1
+ -[APBonjourCacheHomeKit setCachingMetrics:]
+ -[APBrowserBTLEManager createBTLEAdvertiserWithAdvertiseRate:]
+ -[APBrowserBTLEManager createBTLEAdvertiserWithAdvertiseRate:].cold.1
+ -[APBrowserBTLEManager createBTLEAdvertiserWithAdvertiseRate:].cold.2
+ -[APBrowserBTLEManager createBTLEAdvertiserWithAdvertiseRate:].cold.3
+ -[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB:reason:]
+ -[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:host:reason:]
+ -[APCarSessionRequestHandler startAdvertisingCarPlayControlForUSBWithHost:]
+ -[APCarSessionRequestHandler startAdvertisingCarPlayControlForWiFiUUID:host:]
+ -[APCarSessionRequestHandler updateBonjourHost:completion:]
+ -[APCarSessionRequestHandler updateBonjourHost:completion:].cold.1
+ -[APCarSessionRequestHandler updateBonjourHost:completion:].cold.2
+ -[APCarSessionRequestHandler updateBonjourHost:completion:].cold.3
+ -[APCarSessionRequestHandler updateBonjourHost:completion:].cold.4
+ -[APEndpointCachingMetrics _incrementMetric:]
+ -[APEndpointCachingMetrics init]
+ -[APEndpointCachingMetrics reportCacheEviction]
+ -[APEndpointCachingMetrics reportCacheHit]
+ -[APEndpointCachingMetrics reportCacheMiss]
+ -[APEndpointCachingMetrics reportCacheReport]
+ -[APEndpointCachingMetrics reportEppActivation]
+ -[APEndpointCachingMetrics reportEppCachedActivationFailure]
+ -[APEndpointCachingMetrics reportEppCachedActivation]
+ -[APEndpointCachingMetrics reset]
+ -[APEndpointCachingMetrics send]
+ -[APEndpointCachingMetrics send].cold.1
+ -[APEndpointCachingMetrics snapshot]
+ -[APHomeKitDeviceMonitor fullRefresh:]
+ -[APHomeKitDeviceMonitor homeAccessoriesDidChangeHandler]
+ -[APHomeKitDeviceMonitor setHomeAccessoriesDidChangeHandler:]
+ -[APHomeKitDeviceMonitor terminusCapableDeviceIDsByHomeUUID]
+ -[APHomeManagerInterface _checkState]
+ -[APHomeManagerInterface _dispatch:respondingTo:perform:]
+ -[APHomeManagerInterface _dispatchAccessoryDelegatesRespondingTo:performing:]
+ -[APHomeManagerInterface _dispatchHomeDelegatesRespondingTo:performing:]
+ -[APHomeManagerInterface _dispatchManagerDelegatesRespondingTo:performing:]
+ -[APHomeManagerInterface _ensureStarted]
+ -[APHomeManagerInterface _ensureStopped]
+ -[APHomeManagerInterface _hasAnyDelegates]
+ -[APHomeManagerInterface _updateAccessoryDelegateTree:]
+ -[APHomeManagerInterface _updateHomeDelegateTree:]
+ -[APHomeManagerInterface _updateManagerDelegateTree:]
+ -[APHomeManagerInterface _updateState]
+ -[APHomeManagerInterface accessories]
+ -[APHomeManagerInterface accessoryDidUpdateName:]
+ -[APHomeManagerInterface addDelegate:]
+ -[APHomeManagerInterface dealloc]
+ -[APHomeManagerInterface dealloc].cold.1
+ -[APHomeManagerInterface home:didAddAccessory:]
+ -[APHomeManagerInterface home:didRemoveAccessory:]
+ -[APHomeManagerInterface homeManager:didAddHome:]
+ -[APHomeManagerInterface homeManager:didRemoveHome:]
+ -[APHomeManagerInterface homeManager:didUpdateMultiUserStatus:reason:]
+ -[APHomeManagerInterface homeManager:didUpdateStatus:]
+ -[APHomeManagerInterface homeManagerDidUpdateCurrentHome:]
+ -[APHomeManagerInterface homeManagerDidUpdateHomes:]
+ -[APHomeManagerInterface homes]
+ -[APHomeManagerInterface init]
+ -[APHomeManagerInterface isReady]
+ -[APHomeManagerInterface removeDelegate:]
+ -[APHomeManagerInterface setIsReady:]
+ -[CUNANEndpoint(APTNANDataSession) wfaDiscoveryResult]
+ GCC_except_table109
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table83
+ GCC_except_table91
+ GCC_except_table95
+ _APAdvertiserInfoCopyAirPlayDataWithNANServiceType.cold.42
+ _APAdvertiserInfoCopyClusterCompatibleAirPlayData.cold.31
+ _APBrowserCarBonjourInjectConnectCmd
+ _APBrowserCarSessionInjectConnectCmd
+ _APBrowserCreate.cold.27
+ _APBrowserCreate.cold.28
+ _APBrowserDeregisterDeviceDiscoveryObserver
+ _APBrowserRegisterDeviceDiscoveryObserver
+ _APConnectivityHelperGetQualityAssessmentString
+ _APGetSignpostsLogHandle
+ _APSCopyP2PNetworkLLWInfo
+ _APSGetOpenNANServiceType
+ _APSIsMemberOfPersistentGroup
+ _APSIsResponsiveAudioSenderEnabled
+ _APSNetworkAddressIsMulticast
+ _APSNetworkInterfaceNameToInterfaceIndex
+ _APTNANDataSessionAttemptToAbortActivation
+ _APTNANDataSessionCopyPeerAddresses
+ _APTNANDataSessionCopyPeerAddresses.cold.1
+ _APTNANDataSessionCopyPeerAddresses.cold.2
+ _APTNANDataSessionCopyPeerAddresses.cold.3
+ _APTNANDataSessionCopyPeerAddresses.cold.4
+ _APTNANDataSessionCreate.cold.9
+ _APTNANDataSessionCreateStatisticsReport.cold.4
+ _APTNANDataSessionGetRSSI
+ _APTNANDataSessionGetRSSI.cold.1
+ _APTNANDataSessionGetV5PairingStatus
+ _APTNANDataSessionIsActivatable.cold.2
+ _APTTerminusPeerCoordinatorAddPeer
+ _APTTerminusPeerCoordinatorAddPeer.cold.1
+ _APTTerminusPeerCoordinatorAddPeer.cold.2
+ _APTTerminusPeerCoordinatorCopyMulticastGroupAddress
+ _APTTerminusPeerCoordinatorCopyMulticastGroupAddress.cold.1
+ _APTTerminusPeerCoordinatorCreate
+ _APTTerminusPeerCoordinatorCreate.cold.1
+ _APTTerminusPeerCoordinatorCreate.cold.2
+ _APTTerminusPeerCoordinatorCreate.cold.3
+ _APTTerminusPeerCoordinatorCreate.cold.4
+ _APTTerminusPeerCoordinatorCreate.cold.5
+ _APTTerminusPeerCoordinatorCreate.cold.6
+ _APTTerminusPeerCoordinatorCreate.cold.7
+ _APTTerminusPeerCoordinatorCreate.cold.8
+ _APTTerminusPeerCoordinatorGetTypeID
+ _APTTerminusPeerCoordinatorGetTypeID.cold.1
+ _APTTerminusPeerCoordinatorInvalidate
+ _APTTerminusPeerCoordinatorInvalidate.cold.1
+ _APTTerminusPeerCoordinatorInvalidate.cold.2
+ _APTTerminusPeerCoordinatorRemovePeer
+ _APTTerminusPeerCoordinatorRemovePeer.cold.1
+ _APTTerminusPeerCoordinatorRemovePeer.cold.2
+ _APTTerminusPeerCoordinatorSetPreWarmTimeoutSecsForTesting
+ _APTTerminusPeerCoordinatorWarmPeer
+ _APTTerminusPeerCoordinatorWarmPeer.cold.1
+ _APTTerminusPeerCoordinatorWarmPeer.cold.2
+ _APTransportConnectionUDPNWReceiveLoopContextInvalidate
+ _APTransportConnectionUnbufferedNWCreate.cold.16
+ _APTransportConnectionUnbufferedNWCreate.cold.17
+ _APTransportDeviceGetNANv5PairingStatus
+ _APTransportDeviceWaitForReachability
+ _APTransportSessionCreate.cold.12
+ _APTransportTrafficCaptureCloseTCPStream
+ _APTransportTrafficCaptureCreate
+ _APTransportTrafficCaptureCreate.cold.1
+ _APTransportTrafficCaptureCreate.cold.2
+ _APTransportTrafficCaptureCreate.cold.3
+ _APTransportTrafficCaptureGetTypeID
+ _APTransportTrafficCaptureGetTypeID.cold.1
+ _APTransportTrafficCaptureOpenTCPStream
+ _APTransportTrafficCaptureStartSession
+ _APTransportTrafficCaptureStopSession
+ _APTransportTrafficCaptureStopSession.cold.1
+ _APTransportTrafficCaptureWriteMulticastMessage
+ _APTransportTrafficCaptureWriteTCPMessage
+ _APTransportTrafficCaptureWriteTCPMessage.cold.1
+ _APTransportTrafficCaptureWriteTCPMessage.cold.2
+ _APTransportTrafficCaptureWriteTCPMessage.cold.3
+ _CFDataCreateWithBytesNoCopy
+ _CMGetAttachment
+ _FigCFArrayGetFirstValue
+ _FigCFDictionaryGetInt64IfPresent
+ _FigCFDictionaryRemoveAllValues
+ _FigCFDictionarySetUInt64
+ _HTTPClientSetDebugDelegate
+ _HTTPMessageSetPriority
+ _OBJC_CLASS_$_APEndpointCachingMetrics
+ _OBJC_CLASS_$_APHomeManagerInterface
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._metrics
+ _OBJC_IVAR_$_APEndpointCachingMetrics._metrics
+ _OBJC_IVAR_$_APHomeKitDeviceMonitor._homeAccessoriesDidChangeHandler
+ _OBJC_IVAR_$_APHomeManagerInterface._accessoryDelegates
+ _OBJC_IVAR_$_APHomeManagerInterface._homeDelegates
+ _OBJC_IVAR_$_APHomeManagerInterface._homeManager
+ _OBJC_IVAR_$_APHomeManagerInterface._homeManagerDelegates
+ _OBJC_IVAR_$_APHomeManagerInterface._isReady
+ _OBJC_IVAR_$_APHomeManagerInterface._isStarted
+ _OBJC_METACLASS_$_APEndpointCachingMetrics
+ _OBJC_METACLASS_$_APHomeManagerInterface
+ _OUTLINED_FUNCTION_61
+ _SocketTransportRead
+ _SocketTransportWriteV
+ __APConnectivityHelperEnsureAWDLSoloSupportListenerStarted
+ __APConnectivityHelperStartLinkQualityAssessmentListener
+ __APConnectivityHelperStopLinkQualityAssessmentListener
+ __APConnectivityHelperStopLinkQualityAssessmentListener.cold.1
+ __APConnectivityHelperStopLinkQualityAssessmentListener.cold.2
+ __APConnectivityHelperStopListeningToEvent.cold.14
+ __APTTerminusPeerCoordinatorFinalize
+ __APTTerminusPeerCoordinatorGetTypeID
+ __APTransportTrafficCaptureFinalize
+ __APTransportTrafficCaptureFinalize.cold.1
+ __APTransportTrafficCaptureGetTypeID
+ __OBJC_$_CATEGORY_CUNANEndpoint_$_APTNANDataSession
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CUNANEndpoint_$_APTNANDataSession
+ __OBJC_$_CLASS_METHODS_APHomeManagerInterface
+ __OBJC_$_INSTANCE_METHODS_APEndpointCachingMetrics
+ __OBJC_$_INSTANCE_METHODS_APHomeManagerInterface
+ __OBJC_$_INSTANCE_VARIABLES_APEndpointCachingMetrics
+ __OBJC_$_INSTANCE_VARIABLES_APHomeManagerInterface
+ __OBJC_$_PROP_LIST_APHomeManagerInterface
+ __OBJC_$_PROP_LIST_CUNANEndpoint_$_APTNANDataSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMAccessoryDelegatePrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeDelegatePrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeManagerDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMAccessoryDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeManagerDelegatePrivate
+ __OBJC_$_PROTOCOL_REFS_HMAccessoryDelegatePrivate
+ __OBJC_$_PROTOCOL_REFS_HMHomeDelegatePrivate
+ __OBJC_$_PROTOCOL_REFS_HMHomeManagerDelegatePrivate
+ __OBJC_CLASS_PROTOCOLS_$_APHomeManagerInterface
+ __OBJC_CLASS_RO_$_APEndpointCachingMetrics
+ __OBJC_CLASS_RO_$_APHomeManagerInterface
+ __OBJC_LABEL_PROTOCOL_$_HMAccessoryDelegatePrivate
+ __OBJC_LABEL_PROTOCOL_$_HMHomeDelegatePrivate
+ __OBJC_LABEL_PROTOCOL_$_HMHomeManagerDelegatePrivate
+ __OBJC_METACLASS_RO_$_APEndpointCachingMetrics
+ __OBJC_METACLASS_RO_$_APHomeManagerInterface
+ __OBJC_PROTOCOL_$_HMAccessoryDelegatePrivate
+ __OBJC_PROTOCOL_$_HMHomeDelegatePrivate
+ __OBJC_PROTOCOL_$_HMHomeManagerDelegatePrivate
+ __OBJC_PROTOCOL_REFERENCE_$_HMAccessoryDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_HMHomeDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_HMHomeManagerDelegate
+ ___32+[APHomeManagerInterface shared]_block_invoke
+ ___32+[APHomeManagerInterface shared]_block_invoke.cold.1
+ ___43-[APBonjourCacheHomeKit setCachingMetrics:]_block_invoke
+ ___47-[APHomeManagerInterface home:didAddAccessory:]_block_invoke
+ ___48-[APBrowserBTLEManager ensureAdvertisingStarted]_block_invoke.cold.3
+ ___48-[APBrowserBTLEManager ensureAdvertisingStarted]_block_invoke_2
+ ___48-[APBrowserBTLEManager ensureAdvertisingStarted]_block_invoke_2.cold.1
+ ___49-[APHomeManagerInterface accessoryDidUpdateName:]_block_invoke
+ ___49-[APHomeManagerInterface homeManager:didAddHome:]_block_invoke
+ ___50-[APHomeManagerInterface home:didRemoveAccessory:]_block_invoke
+ ___52-[APHomeManagerInterface homeManager:didRemoveHome:]_block_invoke
+ ___52-[APHomeManagerInterface homeManagerDidUpdateHomes:]_block_invoke
+ ___54-[APHomeManagerInterface homeManager:didUpdateStatus:]_block_invoke
+ ___58-[APHomeManagerInterface homeManagerDidUpdateCurrentHome:]_block_invoke
+ ___59-[APCarSessionRequestHandler updateBonjourHost:completion:]_block_invoke
+ ___59-[APCarSessionRequestHandler updateBonjourHost:completion:]_block_invoke_2
+ ___59-[APCarSessionRequestHandler updateBonjourHost:completion:]_block_invoke_3
+ ___60-[APHomeKitDeviceMonitor terminusCapableDeviceIDsByHomeUUID]_block_invoke
+ ___60-[APHomeKitDeviceMonitor terminusCapableDeviceIDsByHomeUUID]_block_invoke.cold.1
+ ___60-[APHomeKitDeviceMonitor terminusCapableDeviceIDsByHomeUUID]_block_invoke.cold.2
+ ___70-[APHomeManagerInterface homeManager:didUpdateMultiUserStatus:reason:]_block_invoke
+ ___75-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB:reason:]_block_invoke
+ ___75-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB:reason:]_block_invoke_2
+ ___75-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB:reason:]_block_invoke_2.cold.1
+ ___75-[APCarSessionRequestHandler startAdvertisingCarPlayControlForUSBWithHost:]_block_invoke
+ ___77-[APCarSessionRequestHandler startAdvertisingCarPlayControlForWiFiUUID:host:]_block_invoke
+ ___85-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:host:reason:]_block_invoke
+ ___85-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:host:reason:]_block_invoke_2
+ ___85-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:host:reason:]_block_invoke_2.cold.1
+ ___85-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:host:reason:]_block_invoke_2.cold.2
+ ___APBrowserCarBonjourInjectConnectCmd_block_invoke
+ ___APBrowserCarBonjourInjectConnectCmd_block_invoke.cold.1
+ ___APBrowserCarBonjourInjectConnectCmd_block_invoke.cold.2
+ ___APBrowserCarSessionInjectConnectCmd_block_invoke
+ ___APBrowserCarSessionInjectConnectCmd_block_invoke.cold.1
+ ___APBrowserDeregisterDeviceDiscoveryObserver_block_invoke
+ ___APBrowserDeregisterDeviceDiscoveryObserver_block_invoke_2
+ ___APBrowserRegisterDeviceDiscoveryObserver_block_invoke
+ ___APTNANDataSessionRetainActivation_block_invoke_6
+ ___APTNANDataSessionRetainActivation_block_invoke_7
+ ___APTNANDataSessionRetainActivation_block_invoke_7.cold.1
+ ___APTNANDataSessionRetainActivation_block_invoke_7.cold.2
+ ___APTTerminusPeerCoordinatorAddPeer_block_invoke
+ ___APTTerminusPeerCoordinatorInvalidate_block_invoke
+ ___APTTerminusPeerCoordinatorRemovePeer_block_invoke
+ ___APTTerminusPeerCoordinatorRemovePeer_block_invoke.cold.1
+ ___APTTerminusPeerCoordinatorRemovePeer_block_invoke.cold.2
+ ___APTTerminusPeerCoordinatorRemovePeer_block_invoke.cold.3
+ ___APTTerminusPeerCoordinatorRemovePeer_block_invoke.cold.4
+ ___APTTerminusPeerCoordinatorWarmPeer_block_invoke
+ ___APTransportDeviceWaitForReachability_block_invoke
+ ___APTransportTrafficCaptureCloseTCPStream_block_invoke
+ ___APTransportTrafficCaptureOpenTCPStream_block_invoke
+ ___APTransportTrafficCaptureOpenTCPStream_block_invoke.cold.1
+ ___APTransportTrafficCaptureOpenTCPStream_block_invoke.cold.2
+ ___APTransportTrafficCaptureOpenTCPStream_block_invoke.cold.3
+ ___APTransportTrafficCaptureOpenTCPStream_block_invoke.cold.4
+ ___APTransportTrafficCaptureOpenTCPStream_block_invoke.cold.5
+ ___APTransportTrafficCaptureStartSession_block_invoke
+ ___APTransportTrafficCaptureStartSession_block_invoke.cold.1
+ ___APTransportTrafficCaptureStartSession_block_invoke.cold.2
+ ___APTransportTrafficCaptureStartSession_block_invoke.cold.3
+ ___APTransportTrafficCaptureStopSession_block_invoke
+ ___APTransportTrafficCaptureStopSession_block_invoke.cold.1
+ ___APTransportTrafficCaptureStopSession_block_invoke.cold.2
+ ___APTransportTrafficCaptureWriteMulticastMessage_block_invoke
+ ___APTransportTrafficCaptureWriteMulticastMessage_block_invoke.cold.1
+ ___APTransportTrafficCaptureWriteMulticastMessage_block_invoke.cold.2
+ ___APTransportTrafficCaptureWriteMulticastMessage_block_invoke.cold.3
+ ___APTransportTrafficCaptureWriteTCPMessage_block_invoke
+ ___APTransportTrafficCaptureWriteTCPMessage_block_invoke.cold.1
+ ___APTransportTrafficCaptureWriteTCPMessage_block_invoke.cold.2
+ ___APTransportTrafficCaptureWriteTCPMessage_block_invoke.cold.3
+ ____APConnectivityHelperStartLinkQualityAssessmentListener_block_invoke
+ ____APConnectivityHelperStopLinkQualityAssessmentListener_block_invoke
+ ___aptTrafficMetrics_getTargetQueue_block_invoke
+ ___block_descriptor_40_e8_32o_e8_v16?08ls32l8
+ ___block_descriptor_44_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_48_e30_v16?0?<v?"CUNANEndpoint">8l
+ ___block_descriptor_48_e8_32o40o_e8_v16?08ls32l8s40l8
+ ___block_descriptor_48_e8_32o_e8_v16?08ls32l8
+ ___block_descriptor_56_e8_32o40o48o_e10_v16?0r^v8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32o40o_e8_v16?08ls32l8s40l8
+ ___block_descriptor_64_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_72_e8_32b40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_72_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32o40r48r_e21_v16?0^{__CFNumber=}8lr40l8s32l8r48l8
+ ___block_descriptor_72_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_89_e8_32o40r48r56r_e21_v16?0^{__CFNumber=}8lr40l8r48l8s32l8r56l8
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.117
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.136
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.149
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.160
+ ___block_descriptor_tmp.161
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.171
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.184
+ ___block_descriptor_tmp.187
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.195
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.204
+ ___block_descriptor_tmp.209
+ ___block_descriptor_tmp.213
+ ___block_descriptor_tmp.249
+ ___block_descriptor_tmp.253
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.43
+ ___block_descriptor_tmp.50
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.7
+ ___block_descriptor_tmp.73
+ ___block_descriptor_tmp.83
+ ___block_descriptor_tmp.90
+ ___block_descriptor_tmp.96
+ ___block_descriptor_tmp.99
+ ___block_literal_global.104
+ ___block_literal_global.131
+ ___block_literal_global.157
+ ___block_literal_global.160
+ ___block_literal_global.177
+ ___block_literal_global.179
+ ___block_literal_global.19
+ ___block_literal_global.25
+ ___block_literal_global.251
+ ___block_literal_global.255
+ ___block_literal_global.363
+ ___block_literal_global.50
+ ___block_literal_global.79
+ ___browser_Invalidate_block_invoke
+ ___browser_dispatchDiscoveryObserverNotification_block_invoke
+ ___browser_notifyAllDiscoveryObservers_block_invoke
+ ___browser_notifyDiscoveryObservers_block_invoke
+ ___carPlayHelperSession_registerForConnectivityEventWithRetry_block_invoke
+ ___httpConnection_setupHTTPClient_block_invoke
+ ___httpConnection_setupHTTPServer_block_invoke
+ ___httpconnection_DumpHierarchy_block_invoke
+ ___httpconnection_configureEncryptionInternal_block_invoke
+ ___httpconnection_configureEncryptionInternal_block_invoke_2
+ ___session_DumpHierarchy_block_invoke
+ ___streamAggregate_SetReadyToSendBatchCallback_block_invoke
+ ___streamAggregate_readyToSendBatchCallback_block_invoke
+ ___streamAggregate_updateReadyToSendBatchCallbackForConnection_block_invoke
+ ___stream_CopyProperty_block_invoke.cold.2
+ ___stream_DumpHierarchy_block_invoke
+ ___tcpconnection_DumpHierarchy_block_invoke
+ ___tcpunbuf_DumpHierarchy_block_invoke
+ ___terminusPeerCoordinator_createAndStartIdleTimer_block_invoke
+ ___terminusPeerCoordinator_createAndStartIdleTimer_block_invoke_2
+ ___udpconnection_DumpHierarchy_block_invoke
+ ___unbufnwGuts_connectionSendPackages_block_invoke_3
+ _browser_addDeviceDiscoveryObserver.sNextTokenCount
+ _browser_deviceAddOrUpdateOSSignpost
+ _browser_dispatchDiscoveryObserverNotification
+ _browser_getCorrelationIDForDeviceInfo
+ _browser_getResolvedDeviceIDLinks
+ _browser_notifyDiscoveryObservers
+ _browser_updateEventInfoForDevice.cold.12
+ _browser_updateEventInfoForDevice.cold.13
+ _carPlayHelperSession_addDisplayConfigurationToDictionary
+ _carPlayHelperSession_registerForConnectivityEventWithRetry
+ _datagramPackage_GetArrivalDeadlineTicks
+ _datagramPackage_GetPacketID
+ _datagramPackage_SetArrivalDeadlineTicks
+ _datagramPackage_SetPacketID
+ _dispatch_after
+ _dispatch_queue_create_with_target$V2
+ _fclose
+ _fopen
+ _fwrite
+ _gAPTTerminusPeerCoordinatorInitOnce
+ _gAPTTerminusPeerCoordinatorTypeID
+ _gAPTransportTrafficCaptureInitOnce
+ _gAPTransportTrafficCaptureTypeID
+ _gLogCategory_APEndpointCachingMetrics
+ _gLogCategory_APHomeManagerInterface
+ _gLogCategory_APTTerminusPeerCoordinator
+ _gLogCategory_APTransportTrafficCapture
+ _gRTCKeyMap
+ _getHMHomeManagerClass
+ _getHMMutableHomeManagerConfigurationClass
+ _httpConnectionCapture_setCapturingDelegateIfNeeded
+ _httpConnectionCapture_setEncryptionDelegate
+ _httpconnection_invalidateInternal.cold.1
+ _httpconnection_netTransportFinalize
+ _httpconnection_netTransportInitialize
+ _httpconnection_netTransportRead
+ _httpconnection_netTransportWrite
+ _httpconnection_netTransportWrite.cold.1
+ _httpconnection_netTransportWrite.cold.2
+ _httpconnection_netTransportWrite.cold.3
+ _httpconnection_netTransportWrite.cold.4
+ _httpconnection_sendPackageHTTPClientCallback
+ _kAPAdvertiserInfoProperty_ClusterMemberVariant
+ _kAPCarPlayHelperDisplayConfigurationKey_ScaleMode
+ _kAPCarPlayHelperDisplayConfigurationKey_ZoomFactorByDisplayIndex
+ _kAPCarPlayHelperEventInfoKey_DisplayConfiguration
+ _kAPCarPlayHelperNotification_DisplayConfigurationChanged
+ _kAPConnectivityHelperEventInfoKey_WiFiNetworkEstimatedMaxThroughputMbps
+ _kAPConnectivityHelperEventInfoKey_WiFiNetworkQualityAssessment
+ _kAPConnectivityHelperEventInfoKey_WiFiNetworkQualityAssessmentUpdatedAt
+ _kAPConnectivityHelperEventInfoKey_WiFiNetworkRSSI
+ _kAPConnectivityHelperQualityAssessment_Fair
+ _kAPConnectivityHelperQualityAssessment_Good
+ _kAPConnectivityHelperQualityAssessment_Poor
+ _kAPConnectivityHelperQualityAssessment_Unknown
+ _kAPConnectivityHelperQualityAssessment_Unusable
+ _kAPSTransportMessageAttachmentKey_ArrivalDeadlineTicks
+ _kAPSTransportMessageAttachmentKey_PacketID
+ _kAPTTerminusMonitorDeviceInfoKey_ApplicationID
+ _kAPTTerminusMonitorDeviceInfoKey_InterfaceIndex
+ _kAPTTerminusMonitorDeviceInfoKey_InterfaceName
+ _kAPTTerminusMonitorDeviceInfoKey_IsPrimaryAssistCapable
+ _kAPTTerminusMonitorDeviceInfoKey_IsSelectedAsPrimaryAssist
+ _kAPTTerminusPeerCoordinatorClass
+ _kAPTransportConnectionOption_MaxPackageExpiryMs
+ _kAPTransportConnectionOption_PackageExpiryOffsetMs
+ _kAPTransportConnectionOption_TransportTrafficCapture
+ _kAPTransportConnectionTimingInformationKey_LastValidMessageReceivedTimeTicks
+ _kAPTransportConnectionUnbufNW_aggregateProtocol
+ _kAPTransportConnectionUnbufNW_aggregateProtocolVTable
+ _kAPTransportConnectionUnbufNW_aggregateProtocol_baseProtocol
+ _kAPTransportDeviceIsReachableOption_MinNANRSSI
+ _kAPTransportSessionStreamOption_NWContextType
+ _kAPTransportSessionStreamOption_UseLLWInterface
+ _kAPTransportStreamProperty_PackageType
+ _kAPTransportTrafficCaptureClass
+ _kFigDispatchQueueCFDictionaryValueCallbacks
+ _nw_parameters_copy
+ _nw_parameters_set_listen_for_multicast_only
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_checkState
+ _objc_msgSend$_dispatch:respondingTo:perform:
+ _objc_msgSend$_dispatchAccessoryDelegatesRespondingTo:performing:
+ _objc_msgSend$_dispatchHomeDelegatesRespondingTo:performing:
+ _objc_msgSend$_dispatchManagerDelegatesRespondingTo:performing:
+ _objc_msgSend$_ensureStarted
+ _objc_msgSend$_ensureStopped
+ _objc_msgSend$_hasAnyDelegates
+ _objc_msgSend$_incrementMetric:
+ _objc_msgSend$_startAdvertisingCarPlayControlForUSB:reason:
+ _objc_msgSend$_startAdvertisingCarPlayControlForWiFiUUID:host:reason:
+ _objc_msgSend$_updateAccessoryDelegateTree:
+ _objc_msgSend$_updateHomeDelegateTree:
+ _objc_msgSend$_updateManagerDelegateTree:
+ _objc_msgSend$_updateState
+ _objc_msgSend$accessoryDidUpdateName:
+ _objc_msgSend$addDelegate:
+ _objc_msgSend$autoPairable
+ _objc_msgSend$boolValue
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$copy
+ _objc_msgSend$createBTLEAdvertiserWithAdvertiseRate:
+ _objc_msgSend$datapathID
+ _objc_msgSend$delegate
+ _objc_msgSend$device
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$displayScaleMode
+ _objc_msgSend$estimatedMaxThroughputMbps
+ _objc_msgSend$fullRefresh:
+ _objc_msgSend$home:didAddAccessory:
+ _objc_msgSend$home:didRemoveAccessory:
+ _objc_msgSend$homeAccessoriesDidChangeHandler
+ _objc_msgSend$homeManager:didAddHome:
+ _objc_msgSend$homeManager:didRemoveHome:
+ _objc_msgSend$homeManager:didUpdateMultiUserStatus:reason:
+ _objc_msgSend$homeManager:didUpdateStatus:
+ _objc_msgSend$homeManagerDidUpdateCurrentHome:
+ _objc_msgSend$homeManagerDidUpdateHomes:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$majorVersion
+ _objc_msgSend$modelIdentifier
+ _objc_msgSend$multiUserStatus
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$pairedUUID
+ _objc_msgSend$pairingConfiguration
+ _objc_msgSend$peerMACAddressData
+ _objc_msgSend$productInfo
+ _objc_msgSend$productPlatform
+ _objc_msgSend$qualityAssessment
+ _objc_msgSend$removeDelegate:
+ _objc_msgSend$reportCacheMiss
+ _objc_msgSend$reportCacheReport
+ _objc_msgSend$rssi
+ _objc_msgSend$setAdvertiseRate:
+ _objc_msgSend$setHomeAccessoriesDidChangeHandler:
+ _objc_msgSend$setIsReady:
+ _objc_msgSend$setPairedResultWaitHandler:
+ _objc_msgSend$setPairingBundleID:
+ _objc_msgSend$setPairingClient:
+ _objc_msgSend$shared
+ _objc_msgSend$snapshot
+ _objc_msgSend$softwareVersion
+ _objc_msgSend$status
+ _objc_msgSend$supportedPairSetupMethods
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$updatedAt
+ _objc_msgSend$wantsCarPlayControlAdvertisingForUSBWithHost:
+ _objc_msgSend$wantsCarPlayControlAdvertisingForWiFiUUID:host:
+ _objc_msgSend$weakObjectsHashTable
+ _objc_msgSend$wfaDiscoveryResult
+ _objc_msgSend$zoomFactorByDisplayIndex
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_signpost_id_generate
+ _sIdleTimeoutSecs
+ _session_activateNANDS.cold.2
+ _session_activateNANDS.cold.3
+ _session_createConnection.cold.6
+ _session_createConnection.cold.7
+ _session_createConnection.cold.8
+ _session_createConnection.cold.9
+ _session_shouldAbort
+ _shared.onceToken
+ _shared.sShared
+ _streamAggregate_SetReadyToSendBatchCallback
+ _streamAggregate_SetReadyToSendBatchCallback.cold.1
+ _streamAggregate_SetReadyToSendBatchCallback.cold.2
+ _streamAggregate_SignalDataAvailable
+ _streamAggregate_SignalDataAvailable.cold.1
+ _streamAggregate_SignalDataAvailable.cold.2
+ _streamAggregate_readyToSendBatchCallback
+ _streamAggregate_updateReadyToSendBatchCallbackForConnection
+ _terminusPeerCoordinator_cancelIdleTimer
+ _terminusPeerCoordinator_createAndStartIdleTimer
+ _terminusPeerCoordinator_createMeshConfiguratorIfNecessary
+ _terminusPeerCoordinator_destroyMeshConfiguratorIfNecessary
+ _terminusPeerCoordinator_destroyMeshConfiguratorIfNecessary.cold.1
+ _terminusPeerCoordinator_resetIdleTimer
+ _trafficCapture_buildAndWritePcapPacket
+ _trafficCapture_buildAndWritePcapPacket.cold.1
+ _trafficCapture_buildAndWritePcapPacket.cold.2
+ _trafficCapture_buildAndWritePcapPacket.cold.3
+ _trafficCapture_buildAndWritePcapPacket.cold.4
+ _trafficCapture_buildAndWritePcapPacket.cold.5
+ _trafficCapture_createStreamContext
+ _trafficCapture_createStreamContext.cold.1
+ _trafficCapture_createStreamContext.cold.2
+ _trafficCapture_createStreamContext.cold.3
+ _trafficCapture_createStreamContext.cold.4
+ _trafficCapture_writePcapTCPPacket
+ _trafficCapture_writePcapTCPPacket.cold.1
+ _trafficCapture_writePcapTCPPacket.cold.2
+ _trafficCapture_writeTCPPacketSplittingIfNeeded
+ _trafficCapture_writeTCPPacketSplittingIfNeeded.cold.1
+ _unbufnwAggregate_AddSubConnection
+ _unbufnwAggregate_Clone
+ _unbufnwAggregate_Clone.cold.1
+ _unbufnwAggregate_Clone.cold.2
+ _unbufnwAggregate_Clone.cold.3
+ _unbufnwAggregate_Clone.cold.4
+ _unbufnwAggregate_Clone.cold.5
+ _unbufnwAggregate_Clone.cold.6
+ _unbufnwAggregate_CopyDebugDescription
+ _unbufnwAggregate_RemoveSubConnection
+ _unbufnwAggregate_updateSubConnection
+ _unbufnwAggregate_updateSubConnection.cold.1
+ _unbufnwAggregate_updateSubConnection.cold.2
+ _unbufnwAggregate_updateSubConnection.cold.3
+ _unbufnwAggregate_updateSubConnection.cold.4
+ _unbufnwAggregate_updateSubConnection.cold.5
+ _unbufnwAggregate_updateSubConnection.cold.6
+ _unbufnwGuts_handleSignal
+ _unbufnwGuts_handleSignal.cold.1
+ _unbufnw_SetProperty.cold.1
+ _unbufnw_SetProperty.cold.10
+ _unbufnw_SetProperty.cold.11
+ _unbufnw_SetProperty.cold.12
+ _unbufnw_SetProperty.cold.13
+ _unbufnw_SetProperty.cold.14
+ _unbufnw_SetProperty.cold.15
+ _unbufnw_SetProperty.cold.16
+ _unbufnw_SetProperty.cold.17
+ _unbufnw_SetProperty.cold.18
+ _unbufnw_SetProperty.cold.19
+ _unbufnw_SetProperty.cold.2
+ _unbufnw_SetProperty.cold.20
+ _unbufnw_SetProperty.cold.21
+ _unbufnw_SetProperty.cold.22
+ _unbufnw_SetProperty.cold.23
+ _unbufnw_SetProperty.cold.24
+ _unbufnw_SetProperty.cold.25
+ _unbufnw_SetProperty.cold.26
+ _unbufnw_SetProperty.cold.27
+ _unbufnw_SetProperty.cold.28
+ _unbufnw_SetProperty.cold.29
+ _unbufnw_SetProperty.cold.3
+ _unbufnw_SetProperty.cold.30
+ _unbufnw_SetProperty.cold.31
+ _unbufnw_SetProperty.cold.32
+ _unbufnw_SetProperty.cold.33
+ _unbufnw_SetProperty.cold.34
+ _unbufnw_SetProperty.cold.35
+ _unbufnw_SetProperty.cold.4
+ _unbufnw_SetProperty.cold.5
+ _unbufnw_SetProperty.cold.6
+ _unbufnw_SetProperty.cold.7
+ _unbufnw_SetProperty.cold.8
+ _unbufnw_SetProperty.cold.9
+ _unbufnw_createOutgoingConnection
+ _unbufnw_createOutgoingConnection.cold.1
+ _unbufnw_createOutgoingConnection.cold.2
+ _unbufnw_createOutgoingConnection.cold.3
+ _unbufnw_createOutgoingConnection.cold.4
+ _unbufnw_createRemoteEndpoint
+ _unbufnw_createRemoteEndpoint.cold.1
+ _unbufnw_createRemoteEndpoint.cold.2
+ _unbufnw_createRemoteEndpoint.cold.3
- -[APBrowserBTLEManager createBTLEAdvertiser]
- -[APBrowserBTLEManager createBTLEAdvertiser].cold.1
- -[APBrowserBTLEManager createBTLEAdvertiser].cold.2
- -[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB]
- -[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB].cold.1
- -[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:]
- -[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:].cold.1
- -[APCarSessionRequestHandler startAdvertisingCarPlayControlForUSB]
- -[APCarSessionRequestHandler startAdvertisingCarPlayControlForWiFiUUID:]
- -[APHomeKitDeviceMonitor activateWithCompletionInternal:].cold.3
- -[APHomeKitDeviceMonitor activateWithCompletionInternal:].cold.4
- -[APHomeKitDeviceMonitor fullRefresh]
- -[APHomeKitDeviceMonitor homeConfigurationDidChangeHandler]
- -[APHomeKitDeviceMonitor homeManager]
- -[APHomeKitDeviceMonitor setHomeConfigurationDidChangeHandler:]
- -[APHomeKitDeviceMonitor setHomeManager:]
- GCC_except_table107
- GCC_except_table32
- GCC_except_table35
- GCC_except_table36
- GCC_except_table45
- GCC_except_table48
- GCC_except_table49
- GCC_except_table51
- GCC_except_table54
- GCC_except_table55
- GCC_except_table59
- GCC_except_table70
- GCC_except_table76
- GCC_except_table86
- GCC_except_table90
- _APTNANDataSessionCopyPeerAddress
- _APTNANDataSessionCopyPeerAddress.cold.1
- _APTNANDataSessionCopyPeerAddress.cold.2
- _APTNANDataSessionCopyPeerAddress.cold.3
- _APTNANDataSessionCopyPeerAddress.cold.4
- _NSSelectorFromString
- _OBJC_IVAR_$_APHomeKitDeviceMonitor._homeConfigurationDidChangeHandler
- _OBJC_IVAR_$_APHomeKitDeviceMonitor._homeManager
- __APBonjourBrowserStopBrowsingOpenNAN.cold.1
- ___66-[APCarSessionRequestHandler startAdvertisingCarPlayControlForUSB]_block_invoke
- ___67-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB]_block_invoke
- ___67-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB]_block_invoke_2
- ___67-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB]_block_invoke_2.cold.1
- ___72-[APCarSessionRequestHandler startAdvertisingCarPlayControlForWiFiUUID:]_block_invoke
- ___73-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:]_block_invoke
- ___73-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:]_block_invoke_2
- ___73-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:]_block_invoke_2.cold.1
- ___73-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:]_block_invoke_2.cold.2
- ___APTNANDataSessionRetainActivation_block_invoke_5.cold.1
- ___APTNANDataSessionRetainActivation_block_invoke_5.cold.2
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.135
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.158
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.166
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.173
- ___block_descriptor_tmp.182
- ___block_descriptor_tmp.185
- ___block_descriptor_tmp.186
- ___block_descriptor_tmp.188
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.196
- ___block_descriptor_tmp.197
- ___block_descriptor_tmp.198
- ___block_descriptor_tmp.207
- ___block_descriptor_tmp.237
- ___block_descriptor_tmp.241
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.33
- ___block_descriptor_tmp.40
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.53
- ___block_descriptor_tmp.61
- ___block_descriptor_tmp.72
- ___block_descriptor_tmp.74
- ___block_descriptor_tmp.76
- ___block_descriptor_tmp.79
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.95
- ___block_literal_global.151
- ___block_literal_global.153
- ___block_literal_global.16
- ___block_literal_global.170
- ___block_literal_global.172
- ___block_literal_global.22
- ___block_literal_global.239
- ___block_literal_global.243
- ___block_literal_global.361
- ___block_literal_global.38
- ___block_literal_global.46
- ___block_literal_global.58
- ___block_literal_global.61
- ___block_literal_global.85
- ___udpconnection_setupListenerNW_block_invoke.cold.1
- ___unbufnw_SetProperty_block_invoke
- ___unbufnw_SignalDataAvailable_block_invoke
- _objc_msgSend$_startAdvertisingCarPlayControlForUSB
- _objc_msgSend$_startAdvertisingCarPlayControlForWiFiUUID:
- _objc_msgSend$createBTLEAdvertiser
- _objc_msgSend$currentHome
- _objc_msgSend$fullRefresh
- _objc_msgSend$homeConfigurationDidChangeHandler
- _objc_msgSend$homeManager
- _objc_msgSend$setHomeConfigurationDidChangeHandler:
- _objc_msgSend$setHomeManager:
- _objc_msgSend$wantsCarPlayControlAdvertisingForUSB
- _objc_msgSend$wantsCarPlayControlAdvertisingForWiFiUUID:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x27
- _stream_DumpHierarchy.cold.1
- _stream_DumpHierarchy.cold.2
- _stream_DumpHierarchy.cold.3
- _stream_DumpHierarchy.cold.4
- _stream_dumpConnectionInfo
- _udpconnection_DumpHierarchy.cold.4
CStrings:
+ " (LLW)"
+ " AWDL"
+ " BTLE"
+ " Direct"
+ " Enet"
+ " NAN"
+ " USB"
+ " WiFi"
+ " [INVALIDATED]"
+ "+[APHomeManagerInterface shared]_block_invoke"
+ "-[APBrowserBTLEManager createBTLEAdvertiserWithAdvertiseRate:]"
+ "-[APBrowserBTLEManager ensureAdvertisingStarted]_block_invoke_2"
+ "-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB:reason:]_block_invoke_2"
+ "-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:host:reason:]"
+ "-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:host:reason:]_block_invoke_2"
+ "-[APCarSessionRequestHandler updateBonjourHost:completion:]"
+ "-[APEndpointCachingMetrics send]"
+ "-[APHomeKitDeviceMonitor fullRefresh:]"
+ "-[APHomeKitDeviceMonitor terminusCapableDeviceIDsByHomeUUID]_block_invoke"
+ "-[APHomeManagerInterface _ensureStarted]"
+ "-[APHomeManagerInterface _ensureStopped]"
+ "-[APHomeManagerInterface _updateState]"
+ "-[APHomeManagerInterface accessoryDidUpdateName:]"
+ "-[APHomeManagerInterface addDelegate:]"
+ "-[APHomeManagerInterface dealloc]"
+ "-[APHomeManagerInterface home:didAddAccessory:]"
+ "-[APHomeManagerInterface home:didRemoveAccessory:]"
+ "-[APHomeManagerInterface homeManager:didAddHome:]"
+ "-[APHomeManagerInterface homeManager:didRemoveHome:]"
+ "-[APHomeManagerInterface homeManager:didUpdateMultiUserStatus:reason:]"
+ "-[APHomeManagerInterface homeManager:didUpdateStatus:]"
+ "-[APHomeManagerInterface homeManagerDidUpdateCurrentHome:]"
+ "-[APHomeManagerInterface homeManagerDidUpdateHomes:]"
+ "-[APHomeManagerInterface removeDelegate:]"
+ "-[APHomeManagerInterface setIsReady:]"
+ "980.58.1.11.1"
+ "AP Setup Msg Send Delay"
+ "APBrowserCarBonjourInjectConnectCmd_block_invoke"
+ "APEndpointCachingMetrics"
+ "APHomeManagerInterface"
+ "APHomeManagerInterface.m"
+ "APTNANDataSessionCopyPeerAddresses"
+ "APTNANDataSessionGetRSSI"
+ "APTNANDataSessionRef transportDevice_getNANDataSession(APTransportDeviceRef, APSNANServiceType, Boolean, Boolean, OSStatus *)"
+ "APTNANDataSessionRetainActivation_block_invoke_5"
+ "APTTerminusPeerCoordinator"
+ "APTTerminusPeerCoordinator.%{ptr}.state"
+ "APTTerminusPeerCoordinatorAddPeer"
+ "APTTerminusPeerCoordinatorAddPeer_block_invoke"
+ "APTTerminusPeerCoordinatorCopyMulticastGroupAddress"
+ "APTTerminusPeerCoordinatorCreate"
+ "APTTerminusPeerCoordinatorInvalidate"
+ "APTTerminusPeerCoordinatorRemovePeer"
+ "APTTerminusPeerCoordinatorRemovePeer_block_invoke"
+ "APTTerminusPeerCoordinatorWarmPeer"
+ "APTTerminusPeerCoordinatorWarmPeer_block_invoke"
+ "APTUnbufNW"
+ "APTransportConnectionUnbufferedNW <APTransportConnectionAggregateProtocol> on <%p>"
+ "APTransportDeviceWaitForReachability"
+ "APTransportStreamAggregate.%{ptr}.data"
+ "APTransportTrafficCapture"
+ "APTransportTrafficCaptureCloseTCPStream"
+ "APTransportTrafficCaptureCreate"
+ "APTransportTrafficCaptureOpenTCPStream"
+ "APTransportTrafficCaptureOpenTCPStream_block_invoke"
+ "APTransportTrafficCaptureStartSession_block_invoke"
+ "APTransportTrafficCaptureStopSession_block_invoke"
+ "APTransportTrafficCaptureWriteMulticastMessage"
+ "APTransportTrafficCaptureWriteMulticastMessage_block_invoke"
+ "APTransportTrafficCaptureWriteTCPMessage"
+ "ApplicationID"
+ "AudioAccessory5,1"
+ "BTLE advertiser activation complete. Started AirPlaySource advertising with rate=%s.\n"
+ "BTLE advertiser rate reset to default.\n"
+ "BTLE advertiser rate will reset to default in %d second(s).\n"
+ "Background"
+ "BackgroundLow"
+ "BonjourHost updated by CarKit (host: %{ptr})"
+ "Boolean APTransportDeviceIsReachable(APTransportDeviceRef, APTransportDeviceAddressType, CFDictionaryRef _Nullable, Boolean * _Nullable)"
+ "Boolean APTransportDeviceWaitForReachability(APTransportDeviceRef, APTransportDeviceAddressType, int64_t, dispatch_semaphore_t _Nullable, CFDictionaryRef _Nullable)"
+ "Boolean APTransportDeviceWaitForReachability(APTransportDeviceRef, APTransportDeviceAddressType, int64_t, dispatch_semaphore_t _Nullable, CFDictionaryRef _Nullable)_block_invoke"
+ "BoostedBTLEAirPlaySourceAdvertiseRate"
+ "Browser BTLE Device Discovered"
+ "Browser Device Discovered"
+ "Browser Device Re-discovered"
+ "Browser Start Detailed Discovery"
+ "Browser Start DetailedNonP2P Discovery"
+ "Browser Start None Discovery"
+ "Browser Start Presence Discovery"
+ "Connection:[%{ptr}]%s (HTTP) %''@ (Not Connected) Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (HTTP) %''@ Ports:%##a -> %##a CID:0x%08X Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (TCP) %''@ (Not Connected) Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (TCP) %''@ Ports:%##a -> %##a%?s%?lu Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (TCPUnbuffered) %''@ (Not Connected) Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (TCPUnbuffered) %''@ Ports:%##a -> %##a%?s%?lu Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (UDP) %''@ (Not Connected) Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (UDP) %''@ Remote:%##a%?s%?lu Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (UDPNW) %''@ (Not Connected) Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (UDPNW) %''@ Remote:%##a%?s%?lu Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (UnbufferedNW:%C) %''@ (Not Connected) Parent:[%{ptr}]\n"
+ "Connection:[%{ptr}]%s (UnbufferedNW:%C) %''@ Ports:%##a -> %##a Parent:[%{ptr}]\n"
+ "Default"
+ "DeviceID: %{public}@"
+ "DeviceID: %{public}@ ServiceType: %s NewTransportTypes:%s%s%s%s%s%s%s"
+ "DeviceID: %{public}@ ServiceType: %s OldTransports:%s%s%s%s%s%s%s NewTransports:%s%s%s%s%s%s%s"
+ "Fair"
+ "FlexibleNAN_AutoPair"
+ "FlexibleNAN_InfraRelayAvoidance"
+ "Forwarding update for ephemeral device %@ to stable device %@"
+ "Good"
+ "High"
+ "Ignoring WiFi link quality assessment monitoring on VirtualMachine\n"
+ "Info for ephemeral device %@ will be applied to stable device %@"
+ "Injecting 'connect' command \n"
+ "Injecting connect command\n"
+ "InterfaceIndex"
+ "InterfaceName"
+ "IsPrimaryAssistCapable"
+ "IsSelectedAsPrimaryAssist"
+ "LastValidMessageReceivedTimeTicks"
+ "Link Quality Assessment"
+ "Link Quality Assessment Listening Stopped"
+ "LinkQualityAssessment"
+ "Low"
+ "LowLatencyNAN (Secure)"
+ "Max"
+ "MaxPackageExpiryMs"
+ "Medium"
+ "MediumHigh"
+ "MediumMid"
+ "MinNANRSSI"
+ "Missing SendBackingProvider"
+ "NANDS [%{ptr}] Aborting in-progress activation"
+ "NANDS [%{ptr}] Discovery result: %@"
+ "NANDS [%{ptr}] Paired result %s available"
+ "NANDS [%{ptr}] Paired result not yet available. Waiting up to %lldms"
+ "NANDS [%{ptr}] failed to obtain NANEndpoint for GetRSSI with error: %#m"
+ "NANDS [%{ptr}] failed to obtain NANEndpoint for GetV5PairingStatus with error: %#m"
+ "NANDS [%{ptr}] not activatable, AutoPair required, but peer is not AutoPairable"
+ "OSStatus APBrowserCarBonjourInjectConnectCmd(APBrowserRef, uint64_t)_block_invoke"
+ "OSStatus APBrowserCarSessionInjectConnectCmd(APBrowserRef, uint64_t)_block_invoke"
+ "OSStatus APTNANDataSessionGetRSSI(APTNANDataSessionRef, int64_t *)"
+ "OSStatus APTNANDataSessionRetainActivation(APTNANDataSessionRef)_block_invoke_6"
+ "OSStatus APTNANDataSessionRetainActivation(APTNANDataSessionRef)_block_invoke_7"
+ "OSStatus APTTerminusPeerCoordinatorAddPeer(APTTerminusPeerCoordinatorRef, CFStringRef)_block_invoke"
+ "OSStatus APTTerminusPeerCoordinatorCreate(APSNetworkAddressRef, APTTerminusPeerCoordinatorRef *)"
+ "OSStatus APTTerminusPeerCoordinatorRemovePeer(APTTerminusPeerCoordinatorRef, CFStringRef, Boolean)_block_invoke"
+ "OSStatus APTTerminusPeerCoordinatorWarmPeer(APTTerminusPeerCoordinatorRef, CFStringRef)_block_invoke"
+ "OSStatus APTransportTrafficCaptureCreate(CFDictionaryRef, APTransportTrafficCaptureRef *)"
+ "OSStatus APTransportTrafficCaptureStartSession(APTransportTrafficCaptureRef, const char *, CFDictionaryRef)_block_invoke"
+ "OSStatus APTransportTrafficCaptureStopSession(APTransportTrafficCaptureRef)"
+ "OSStatus APTransportTrafficCaptureStopSession(APTransportTrafficCaptureRef)_block_invoke"
+ "OSStatus APTransportTrafficCaptureWriteMulticastMessage(APTransportTrafficCaptureRef, sockaddr_ip *, sockaddr_ip *, CFDataRef, APTransportTrafficCaptureMessageDirection)_block_invoke"
+ "OSStatus APTransportTrafficCaptureWriteTCPMessage(APTransportTrafficCaptureRef, void *, CFTypeRef, APTransportTrafficCaptureMessageDirection)_block_invoke"
+ "OSStatus _APConnectivityHelperHandleLinkQualityAssessmentInternal(APConnectivityHelperRef, NSDictionary *)"
+ "OSStatus _APConnectivityHelperStartLinkQualityAssessmentListener(APConnectivityHelperRef)"
+ "OSStatus _APConnectivityHelperStopLinkQualityAssessmentListener(APConnectivityHelperRef)"
+ "OSStatus browser_getResolvedDeviceIDLinks(APBrowserRef, CFNumberRef, CFNumberRef *, CFNumberRef *, CFNumberRef *)"
+ "OSStatus session_createConnectionForStream(FigTransportSessionRef, FigTransportStreamID, CFStringRef, FigThreadPriority, CFDictionaryRef, APTransportConnectionRef *)"
+ "OSStatus terminusPeerCoordinator_createMeshConfiguratorIfNecessary(APTTerminusPeerCoordinatorRef)"
+ "OSStatus trafficCapture_buildAndWritePcapPacket(APTransportTrafficCaptureRef, APTransportTrafficCaptureStream *, sockaddr_ip *, sockaddr_ip *, void *, uint32_t, void *, size_t)"
+ "OSStatus trafficCapture_writeTCPPacketsFromBlockBuffer(APTransportTrafficCaptureRef, APTransportTrafficCaptureStream *, CMBlockBufferRef, APTransportTrafficCaptureMessageDirection)"
+ "OSStatus trafficCapture_writeTCPPacketsFromData(APTransportTrafficCaptureRef, APTransportTrafficCaptureStream *, CFDataRef, APTransportTrafficCaptureMessageDirection)"
+ "OSStatus unbufnwAggregate_Clone(APTransportConnectionAggregateRef, CFStringRef, APTransportConnectionAggregateRef *)"
+ "OSStatus unbufnwAggregate_updateSubConnection(APTransportConnectionAggregateRef, APTransportConnectionRef, Boolean)"
+ "OSStatus unbufnw_createOutgoingConnection(APTransportConnectionRef, nw_parameters_t, nw_endpoint_t)"
+ "PackageExpiryOffsetMs"
+ "Periodic"
+ "PeriodicHigh"
+ "Poor"
+ "Removing"
+ "Skip resetting BTLE advertiser rate to default, as the original advertiser has stopped.\n"
+ "StartBonjourForWiFi: %@, reason: %@\n"
+ "Stream:[%{ptr}]%s (Buffered) %''@ Parent:[%{ptr}]\n"
+ "Stream:[%{ptr}]%s (Unbuffered) %''@ Parent:[%{ptr}]\n"
+ "TransportSession:[%{ptr}]%s %''@ Parent:[%{ptr}]\n"
+ "TransportTrafficCapture"
+ "Unable to create shared interface: HomeKit unavailable"
+ "Unusable"
+ "UseLLWInterface"
+ "Using advertiseRate: %s"
+ "[%{ptr}] %s %s reachable%?{end}. Wait %s"
+ "[%{ptr}] %s Home [%{ptr}]: %@"
+ "[%{ptr}] %s Not able to get display configuration, aborting discovery (bonjourHost: %@)"
+ "[%{ptr}] %s Not able to get display configuration, aborting discovery (sessionHost: %@)"
+ "[%{ptr}] %s StartBonjourForUSB, reason: %@, host: %{ptr}\n"
+ "[%{ptr}] %s StartBonjourForWiFi: %@, reason: %@, host: %@\n"
+ "[%{ptr}] %s SubConnection [%{ptr}]"
+ "[%{ptr}] %s [%{ptr}]"
+ "[%{ptr}] %s [%{ptr}] [%{ptr}]"
+ "[%{ptr}] %s [%{ptr}] status=%lld reason=%@"
+ "[%{ptr}] %s [%{ptr}] status=%llu"
+ "[%{ptr}] %s not yet reachable. Waiting up to %lldms"
+ "[%{ptr}] APTTerminusPeerCoordinator Created with MulticastAddress: %@\n"
+ "[%{ptr}] Abort NANDS [%{ptr}] activation"
+ "[%{ptr}] Add delegate [%{ptr}]"
+ "[%{ptr}] Added Traffic Registration [%{ptr}]%?{end} for group: %@"
+ "[%{ptr}] Added peer [%{ptr}]\n"
+ "[%{ptr}] Added pre-warmed peer [%{ptr}]\n"
+ "[%{ptr}] All peers are removed, release meshConfigurator [%{ptr}]\n"
+ "[%{ptr}] Capturing message from CFData (len: %lu, direction: %d)"
+ "[%{ptr}] Capturing message from CMBlockBuffer (len: %lu, direction: %d)"
+ "[%{ptr}] Capturing multicast message (len: %lu, direction: %d)"
+ "[%{ptr}] Cloned to [%{ptr}]"
+ "[%{ptr}] Cloning..."
+ "[%{ptr}] Create connection to %##a"
+ "[%{ptr}] Create new meshConfigurator [%{ptr}]\n"
+ "[%{ptr}] Created shared interface"
+ "[%{ptr}] Dropping expired package [%{ptr}], <1ms remaining"
+ "[%{ptr}] Dropping expired package [%{ptr}], deadline passed by %llums"
+ "[%{ptr}] Failed to add Traffic Registration%?s%?@ err=%#m"
+ "[%{ptr}] Failed to capture message (err: %#m)\n"
+ "[%{ptr}] Failed to close traffic capture stream: %#m\n"
+ "[%{ptr}] Failed to handle Link Quality Assessment event.\n"
+ "[%{ptr}] Failed to open traffic capture stream: %#m\n"
+ "[%{ptr}] Failed to record received traffic: %#m\n"
+ "[%{ptr}] Failed to record sent traffic: %#m\n"
+ "[%{ptr}] Failed to register for event %d (err: %#m), retrying in 1s (attempt %d/%d)\n"
+ "[%{ptr}] Failed to register for event %d after %d retries: %#m\n"
+ "[%{ptr}] Failed to set up listener for LinkQualityAssessment, error: %#m"
+ "[%{ptr}] Finalizing\n"
+ "[%{ptr}] Found linked devices stable:%@ ephemeral:%@"
+ "[%{ptr}] Idle timeout for peer [%{ptr}] — removing peer\n"
+ "[%{ptr}] Initiating session stop\n"
+ "[%{ptr}] Keep peer [%{ptr}] warm and start %d secs idle timer... \n"
+ "[%{ptr}] Link quality assessment info: %@"
+ "[%{ptr}] NAN reachable, but RSSI %lld is below the threshold %lld; reporting as non-reachable"
+ "[%{ptr}] Not ready: Home Manager status 0x%llx"
+ "[%{ptr}] Ready: Home Manager multi user status ready"
+ "[%{ptr}] Remove delegate [%{ptr}]"
+ "[%{ptr}] Removed peer [%{ptr}]\n"
+ "[%{ptr}] Removing Traffic Registration [%{ptr}]"
+ "[%{ptr}] Resuming%?s..."
+ "[%{ptr}] Reverse connection failed"
+ "[%{ptr}] Sending package [%{ptr}] with expiryMs=%llu"
+ "[%{ptr}] Sent endpoint caching metrics %?{end} %@"
+ "[%{ptr}] Session stop completed\n"
+ "[%{ptr}] Skipping Infra Transaction"
+ "[%{ptr}] Start session for %s %s (err: %#m)\n"
+ "[%{ptr}] Starting Home Manager [%{ptr}]"
+ "[%{ptr}] Starting WiFi LinkQualityAssessment listener.\n"
+ "[%{ptr}] Stopping Home Manager [%{ptr}]"
+ "[%{ptr}] Stopping WiFi LinkQualityAssessment listener.\n"
+ "[%{ptr}] Unsupported address family: %d\n"
+ "[%{ptr}] Warm peer [%{ptr}] and start %d secs idle timer... \n"
+ "[%{ptr}] dealloc"
+ "[%{ptr}] isReady %s -> %s"
+ "[%{ptr}] listener started on %##a"
+ "[%{ptr}] maxPackageExpiryMs=%llu packageExpiryOffsetMs=%llu"
+ "[%{ptr}] overridePackageExpiryMs=%lld"
+ "_APConnectivityHelperEnsureLinkQualityAssessmentListenerStarted"
+ "_APConnectivityHelperEnsureLinkQualityAssessmentListenerStopped"
+ "_APConnectivityHelperHandleLinkQualityAssessmentInternal"
+ "_APConnectivityHelperStartLinkQualityAssessmentListener"
+ "_APConnectivityHelperStopLinkQualityAssessmentListener"
+ "allowOpenNANNoSecurity"
+ "browser_addDeviceDiscoveryObserver"
+ "browser_getResolvedDeviceIDLinks"
+ "browser_removeDeviceDiscoveryObserver"
+ "carPlayHelperSession_addDisplayConfigurationToDictionary"
+ "carPlayHelperSession_registerForConnectivityEventWithRetry"
+ "clusterMemberVariant"
+ "cmv"
+ "com.apple.APTransportTrafficCapture"
+ "discoveryResult"
+ "displayConfiguration"
+ "displayConfigurationChanged"
+ "enableSetupMsgSignposting"
+ "eppActivations"
+ "eppCacheEvictions"
+ "eppCacheHits"
+ "eppCacheMisses"
+ "eppCacheReports"
+ "eppCachedActivationFailures"
+ "eppCachedActivations"
+ "httpconnectionCapture_captureOutgoingMessageData"
+ "httpconnection_netTransportRead"
+ "initiated by AirPlay after checking with CarKit"
+ "initiated by CarKit"
+ "is now"
+ "llMaxPackageExpiryMs"
+ "llPackageExpiryOffsetMs"
+ "q"
+ "scaleMode"
+ "senderBTLEAdvertiseRate"
+ "senderBTLEAdvertiseRateResetDelaySecs"
+ "still not"
+ "streamAggregate_SetReadyToSendBatchCallback"
+ "streamAggregate_SignalDataAvailable"
+ "streamAggregate_readyToSendBatchCallback"
+ "streamAggregate_updateReadyToSendBatchCallbackForConnection"
+ "stream_DumpHierarchy_block_invoke"
+ "terminusPeerCoordinator_createAndStartIdleTimer"
+ "timed out"
+ "trafficCapture_PCAPWriteFileHeader"
+ "trafficCapture_buildAndWritePcapPacket"
+ "trafficCapture_buildPacketBuffer"
+ "trafficCapture_createStreamContext"
+ "trafficCapture_emulateTCPHandshake"
+ "trafficCapture_updateIPv4Header"
+ "trafficCapture_updateIPv6Header"
+ "trafficCapture_writePcapPacketRecordToFile"
+ "trafficCapture_writePcapTCPPacket"
+ "trafficCapture_writePcapUDPPacket"
+ "trafficCapture_writeTCPPacketSplittingIfNeeded"
+ "trafficCapture_writeTCPPacketsFromBlockBuffer"
+ "unbufferedNWOverridePackageExpiryMs"
+ "unbufnwAggregate_Clone"
+ "unbufnwAggregate_CopyDebugDescription"
+ "unbufnwAggregate_updateSubConnection"
+ "unbufnw_createOutgoingConnection"
+ "unbufnw_createRemoteEndpoint"
+ "v16@?0@8"
+ "v16@?0@?<v@?@\"CUNANEndpoint\">8"
+ "v16@?0^{?=^v^?^?^?^?}8"
+ "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*i}8"
+ "v16@?0^{__CFNumber=}8"
+ "void APTNANDataSessionAttemptToAbortActivation(APTNANDataSessionRef)"
+ "void APTNANDataSessionGetV5PairingStatus(APTNANDataSessionRef, Boolean * _Nullable, Boolean * _Nullable)"
+ "void _APTransportTrafficCaptureFinalize(CFTypeRef)"
+ "void carPlayHelperSession_registerForConnectivityEventWithRetry(APConnectivityHelperRef, APCarPlayHelperRef, APConnectivityHelperEventType, dispatch_queue_t, int)"
+ "void tcpconnection_cleanUp(APTransportConnectionRef)"
+ "void tcpconnection_receivedData(void *)"
+ "void terminusPeerCoordinator_createAndStartIdleTimer(APTTerminusPeerCoordinatorRef, CFStringRef)_block_invoke"
+ "void terminusPeerCoordinator_destroyMeshConfiguratorIfNecessary(APTTerminusPeerCoordinatorRef)"
+ "void unbufnwGuts_handleSignal(void *)"
+ "wb"
+ "wifiNetworkEstimatedMaxThroughputMbps"
+ "wifiNetworkQualityAssessment"
+ "wifiNetworkQualityAssessmentUpdatedAt"
+ "wifiNetworkRSSI"
+ "zoomFactorByDisplayIndex"
- " (Current)"
- "#16@0:8"
- "-[APBrowserBTLEManager createBTLEAdvertiser]"
- "-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB]"
- "-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForUSB]_block_invoke_2"
- "-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:]"
- "-[APCarSessionRequestHandler _startAdvertisingCarPlayControlForWiFiUUID:]_block_invoke_2"
- "-[APHomeKitDeviceMonitor fullRefresh]"
- ".cxx_destruct"
- "950.7.1"
- "@\"APHomeKitDeviceMonitor\""
- "@\"CARSessionRequestAgent\""
- "@\"CBAdvertiser\""
- "@\"CBDiscovery\""
- "@\"CUCoalescer\""
- "@\"CUSystemMonitor\""
- "@\"CWFInterface\""
- "@\"HMHomeManager\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8S16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^v16"
- "@24@0:8^{OpaqueAPBrowser=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8B16^@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@?16^{__CFString=}24"
- "@32@0:8^v16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "APBonjourCacheEvictionPolicy"
- "APBonjourCacheEvictionTTL"
- "APBonjourCacheHomeKitItem"
- "APBonjourCacheManager"
- "APBrokerHTTPUtilsTaskDelegate"
- "APCarSessionRequestHandler"
- "APHomeKitDeviceMonitor.m"
- "APTNANDataSessionCopyPeerAddress"
- "APTNANDataSessionRef transportDevice_getNANDataSession(APTransportDeviceRef, APSNANServiceType, Boolean, OSStatus *)"
- "APTNANPairingDelegate"
- "APTransportStreamAggregate requires a SendBackingProvider!"
- "AWDLPeerContextWithMACAddress:interfaceName:"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSDictionary\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16B24B28"
- "B32@0:8@16^@24"
- "BTLE advertiser activation complete. Started AirPlaySource advertising.\n"
- "BrowserNIDelegate"
- "C"
- "C16@0:8"
- "CARSessionRequestHandling"
- "Connection:[%{ptr}] (HTTP) %''@ (Not Connected) Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (HTTP) %''@ Ports:%##a -> %##a CID:0x%08X Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (TCP) %''@ (Not Connected) Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (TCP) %''@ Ports:%##a -> %##a%?s%?lu Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (TCPUnbuffered) %''@ (Not Connected) Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (TCPUnbuffered) %''@ Ports:%##a -> %##a%?s%?lu Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (UDP) %''@ (Not Connected) Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (UDP) %''@ Remote:%##a%?s%?lu Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (UDPNW) %''@ (Not Connected) Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (UDPNW) %''@ Remote:%##a%?s%?lu Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (UnbufferedNW:%C) %''@ (Not Connected) Parent:[%{ptr}]\n"
- "Connection:[%{ptr}] (UnbufferedNW:%C) %''@ Ports:%##a -> %##a Parent:[%{ptr}]\n"
- "HMAccessoryDelegate"
- "HMHomeDelegate"
- "HMHomeManagerDelegate"
- "Infra Transaction"
- "Introspector"
- "JSONObjectWithData:options:error:"
- "NISessionDelegate"
- "NSObject"
- "NSURLSessionDelegate"
- "NSURLSessionTaskDelegate"
- "OSStatus session_createConnectionForStream(FigTransportSessionRef, FigTransportStreamID, CFStringRef, APTransportSessionInterfaceType, APTransportSessionInterfaceFlags, FigThreadPriority, CFDictionaryRef, APTransportConnectionRef *)"
- "OSStatus unbufnw_SignalDataAvailable(APTransportConnectionRef)_block_invoke"
- "Q16@0:8"
- "Q24@0:8@16"
- "RSSI"
- "StartBonjourForUSB\n"
- "StartBonjourForWiFi: %@\n"
- "Stream:[%{ptr}] (Buffered) %''@ Parent:[%{ptr}]\n"
- "Stream:[%{ptr}] (Unbuffered) %''@ Parent:[%{ptr}]\n"
- "T#,R"
- "T@\"APHomeKitDeviceMonitor\",N,V_homeKitDeviceMonitor"
- "T@\"CBAdvertiser\",&,N,V_btleAdvertiser"
- "T@\"CBDiscovery\",&,N,V_btleDiscoverer"
- "T@\"CUCoalescer\",N,V_diskWriteCoalescer"
- "T@\"CUSystemMonitor\",N,V_systemMonitor"
- "T@\"HMHomeManager\",N,V_homeManager"
- "T@\"NSArray\",&,N,V_evictionPolicies"
- "T@\"NSArray\",R,N"
- "T@\"NSDictionary\",&,N,V_deviceInfo"
- "T@\"NSDictionary\",&,N,V_userInfo"
- "T@\"NSDictionary\",R,N"
- "T@\"NSMutableDictionary\",&,N,V_btleDevices"
- "T@\"NSMutableDictionary\",&,N,V_cache"
- "T@\"NSMutableDictionary\",&,N,V_presentRealDevices"
- "T@\"NSMutableSet\",&,N,V_deviceIdentifiers"
- "T@\"NSMutableSet\",&,N,V_expectedDeviceIDs"
- "T@\"NSMutableSet\",&,N,V_reportedCachedDeviceIDs"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@\"NSObject<OS_dispatch_queue>\",N,V_dispatchQueue"
- "T@\"NSObject<OS_dispatch_queue>\",N,V_internalBrowserQueue"
- "T@\"NSObject<OS_dispatch_queue>\",N,V_internalQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_eventQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSObject<OS_dispatch_source>\",N,V_timeoutTimer"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",&,N,V_currentNetworkSignature"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_label"
- "T@\"NSString\",C,N,V_serviceType"
- "T@\"NSString\",N,V_bonjourProtocol"
- "T@\"NSString\",N,V_bonjourServiceName"
- "T@\"NSString\",N,V_instanceName"
- "T@\"NSString\",R,C"
- "T@?,C,N,V_cachedDeviceFoundHandler"
- "T@?,C,N,V_cachedDeviceLostHandler"
- "T@?,C,N,V_homeConfigurationDidChangeHandler"
- "T@?,C,N,V_invalidationHandler"
- "T@?,C,N,V_reportDeviceFoundHandler"
- "T@?,C,N,V_reportDeviceLostHandler"
- "T@?,N,V_deviceFoundHandlerBlock"
- "TB,N,V_activatedPresentDeviceStashing"
- "TB,N,V_browseForAltReceiver"
- "TB,N,V_invalidated"
- "TB,N,V_isAdvertising"
- "TB,N,V_isBrowsing"
- "TB,N,V_isEnabled"
- "TB,N,V_isInvalidated"
- "TB,N,V_isScanning"
- "TB,N,V_isSoloBeaconDisabled"
- "TB,N,V_preferencesUpdated"
- "TB,N,V_requireDeviceNetworkSignature"
- "TB,N,V_usePresentDeviceStashing"
- "TC,N,V_handledPairingRequest"
- "TC,V_authPromptWasDismissed"
- "TQ,R"
- "T^?,N,V_eventHandlerFunc"
- "T^v,N,V_eventHandlerContext"
- "T^{BonjourBrowser=},N,V_bonjourBrowser"
- "Td,N,V_timeToLiveSeconds"
- "Ti,N,V_btleAdvertiserSeed"
- "Ti,N,V_btleDiscovererSeed"
- "Tr^v,N,V_btleDiscoveryManagerToken"
- "Traffic Registration"
- "TransportSession:[%{ptr}] %''@ Parent:[%{ptr}]\n"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByDeletingLastPathComponent"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didCreateTask:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSession:task:didCompleteWithError:"
- "URLSession:task:didFinishCollectingMetrics:"
- "URLSession:task:didReceiveChallenge:completionHandler:"
- "URLSession:task:didReceiveInformationalResponse:"
- "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
- "URLSession:task:needNewBodyStream:"
- "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
- "URLSession:task:willBeginDelayedRequest:completionHandler:"
- "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
- "URLSession:taskIsWaitingForConnectivity:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "WiFiAwareDataSessionPairingDelegate"
- "[%{ptr}] %s Home [%{ptr}]: %@%?s"
- "[%{ptr}] %s StartBonjourForUSB\n"
- "[%{ptr}] %s StartBonjourForWiFi: %@\n"
- "[%{ptr}] Added %s [%{ptr}]%?{end} for group: %@"
- "[%{ptr}] Failed to add %s%?s%?@ err=%#m"
- "[%{ptr}] Removing %s [%{ptr}]"
- "[%{ptr}] Resuming..."
- "[%{ptr}] listener started on port %u"
- "^?"
- "^?16@0:8"
- "^v"
- "^v16@0:8"
- "^{BonjourBrowser=}"
- "^{BonjourBrowser=}16@0:8"
- "^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}}"
- "^{OpaqueFigCFWeakReferenceHolder=}"
- "^{_NSZone=}16@0:8"
- "^{__CFSet=}"
- "^{__CFString=}"
- "_APBonjourBrowserEnqueueOperation"
- "_activateWithCompletion:"
- "_activatedPresentDeviceStashing"
- "_addDeviceToCache:pairedPeerInfo:event:"
- "_agent"
- "_auditCaches"
- "_auditCachesIfNecessary:event:"
- "_authPromptWasDismissed"
- "_bonjourBrowser"
- "_bonjourProtocol"
- "_bonjourServiceName"
- "_browseForAltReceiver"
- "_browserWeak"
- "_btleAdvertiser"
- "_btleAdvertiserSeed"
- "_btleDevices"
- "_btleDiscoverer"
- "_btleDiscovererSeed"
- "_btleDiscoveryManagerToken"
- "_btleMode"
- "_cache"
- "_cacheChanged"
- "_cachedDeviceFoundHandler"
- "_cachedDeviceLostHandler"
- "_cachedItems"
- "_cancelRetryGetPairedPeers"
- "_carPlayHelpers"
- "_coreWiFiInterface"
- "_coreWiFiQueue"
- "_currentNetworkSignature"
- "_deviceFound:altPairedInfo:recheck:event:"
- "_deviceFoundHandlerBlock"
- "_deviceIdentifiers"
- "_deviceInfo"
- "_deviceMap"
- "_diskWriteCoalescer"
- "_dispatchQueue"
- "_ensureKnownNetworkProfileMonitoringStarted"
- "_eventContext"
- "_eventHandlerContext"
- "_eventHandlerFunc"
- "_eventQueue"
- "_evictionPolicies"
- "_expectedDeviceIDs"
- "_flushCachedItems"
- "_getCacheDirectoryURLCreateIfNecessary:error:"
- "_getCacheFileURLCreateIfNecessary:error:"
- "_handleAuthorizationRequestBlock"
- "_handleKnownNetworkProfileUpdate:"
- "_handledPairingRequest"
- "_homeConfigurationDidChangeHandler"
- "_homeKitDeviceMonitor"
- "_homeManager"
- "_instanceName"
- "_internalBrowserQueue"
- "_internalQueue"
- "_invalidate"
- "_invalidateCalled"
- "_invalidateDone"
- "_invalidated"
- "_invalidationHandler"
- "_isAdvertising"
- "_isBrowsing"
- "_isEnabled"
- "_isInvalidated"
- "_isMonitoringKnownNetworkProfile"
- "_isPublicAirPlayNetwork"
- "_isScanning"
- "_isSoloBeaconDisabled"
- "_label"
- "_logContext"
- "_migrateCacheDirectoryIfNecessary"
- "_networkSignature"
- "_networkSignatureChanged"
- "_networkSignatureWasValidAt"
- "_p2pDeviceMap"
- "_p2pSoloSupported"
- "_p2pSoloSupportedIsSet"
- "_pairedPeersChanged"
- "_pairedPeersChangedToken"
- "_pairedPeersGetting"
- "_pairedPeersMap"
- "_preferencesUpdated"
- "_presentRealDevices"
- "_queue"
- "_readCachedItems"
- "_recheckDevices:"
- "_refreshCachedItems"
- "_refreshOrRemoveCachedItem:"
- "_removeIfDuplicatesFoundOrIfNoLongerCacheable:identifier:serialNumber:manufacturer:isCacheable:"
- "_replaceIfnameFromDNSString:"
- "_reportCachedItemLost:event:"
- "_reportCachedItemsFound:"
- "_reportCachedItemsLost:"
- "_reportDeviceFoundHandler"
- "_reportDeviceLostHandler"
- "_reportedCachedDeviceIDs"
- "_requireDeviceNetworkSignature"
- "_retryTimer"
- "_sanitizeDNSStrings:"
- "_serviceType"
- "_sslCertificateHostName"
- "_startAdvertisingCarPlayControlForUSB"
- "_startAdvertisingCarPlayControlForWiFiUUID:"
- "_startRetryGetPairedPeersTimer"
- "_systemMonitor"
- "_timeToLiveSeconds"
- "_timeoutTimer"
- "_ucat"
- "_updateCachedDeviceInfoWhenRealDeviceIsFound:event:"
- "_updateDeviceMap:deviceIdentifier:deviceAdded:"
- "_updateLastSeenTimestamp:"
- "_usePresentDeviceStashing"
- "_userInfo"
- "_writeCachedItems:"
- "_writeCoaleser"
- "accessories"
- "accessory:didAddProfile:"
- "accessory:didRemoveProfile:"
- "accessory:didUpdateAssociatedServiceTypeForService:"
- "accessory:didUpdateFirmwareVersion:"
- "accessory:didUpdateNameForService:"
- "accessory:service:didUpdateValueForCharacteristic:"
- "accessoryDidUpdateName:"
- "accessoryDidUpdateReachability:"
- "accessoryDidUpdateServices:"
- "activate"
- "activateOverlaySessionOnEndpoint:figEndpoint:"
- "activateWithCompletion:"
- "activateWithCompletionInternal:"
- "activatedPresentDeviceStashing"
- "activeDevices"
- "activityWithType:reason:"
- "addCarPlayHelper:"
- "addEntriesFromDictionary:"
- "addExpectedDeviceID:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserverForName:object:queue:usingBlock:"
- "addOrUpdateOrReAddItem:flags:logCategory:logLabel:error:"
- "airplaySourceFlags"
- "airplayTargetConfigSeed"
- "airplayTargetFlags"
- "airplayTargetIPv4"
- "airplayTargetIPv6"
- "airplayTargetPort"
- "allKeys"
- "allObjects"
- "allValues"
- "allowAllOpenNANNoSecurity"
- "appendFormat:"
- "appendString:"
- "applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithObjects:count:"
- "authPromptWasDismissed"
- "authenticationMethod"
- "autorelease"
- "availableCachedDevices"
- "bandwidth"
- "beginActivity:error:"
- "beginMonitoring"
- "binEnd"
- "binStart"
- "bleRSSI"
- "bluetoothState"
- "bonjourBrowser"
- "bonjourProtocol"
- "bonjourServiceName"
- "btleAdvertiser"
- "btleAdvertiserSeed"
- "btleDevices"
- "btleDiscoverer"
- "btleDiscovererSeed"
- "btleDiscoveryManagerToken"
- "btleManagerState"
- "bytes"
- "cStringUsingEncoding:"
- "cache"
- "cacheDevice:"
- "cacheHKPeerIfNeeded:pairedPeerInfo:"
- "cachedDeviceFoundHandler"
- "cachedDeviceLostHandler"
- "cachedDevices"
- "callDeviceFoundHandlerOnce:error:"
- "canCacheDevice:"
- "cancel"
- "cancelRequests"
- "carplayUUID"
- "carplayWiFiUUID"
- "caseInsensitiveCompare:"
- "channel"
- "channelNumber"
- "channelSequence"
- "channelSequenceMismatchOn2GCount"
- "channelSequenceMismatchOn5GCount"
- "checkAndEvictCachedDevicesIfNecessary"
- "checkCarPlayControlAdvertisingForUSB"
- "checkCarPlayControlAdvertisingForWiFiUUID:"
- "class"
- "code"
- "compare:"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "containsObject:"
- "containsString:"
- "contentsOfDirectoryAtPath:error:"
- "controlFlags"
- "copyDescription"
- "copyDescriptionInternal"
- "copyItemMatchingItem:flags:error:"
- "copyItemsMatchingItem:flags:error:"
- "copyShowInfo:verbose:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "createBTLEAdvertiser"
- "createBTLEDiscoverer"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createEventInfoDictionary:withDeviceID:IPAddress:port:supportsSolo:rssi:"
- "credentialForTrust:"
- "csaCount"
- "currentHandler"
- "currentHome"
- "currentKnownNetworkProfile"
- "currentNetworkSignature"
- "currentState"
- "customData"
- "d16@0:8"
- "data"
- "dataTaskWithRequest:completionHandler:"
- "dataWithBytes:length:"
- "dataWithJSONObject:options:error:"
- "dataWithPropertyList:format:options:error:"
- "datapathID"
- "date"
- "dateModified"
- "dateWithTimeIntervalSinceReferenceDate:"
- "deactivateOverlaySessionOnEndpoint:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultManager"
- "deriveSharedSecretForProtocolName:context:derivationMethod:completion:"
- "describeBonjourInfo:"
- "description"
- "deviceFound:"
- "deviceFoundHandlerBlock"
- "deviceIdentifier"
- "deviceIdentifiers"
- "deviceLost:"
- "dfsChannelsCount"
- "dictionary"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "discoveryFlags"
- "discoveryToken"
- "diskWriteCoalescer"
- "dispatchEvent:withEventInfo:"
- "dispatchQueue"
- "displayName"
- "distance"
- "doubleValue"
- "effectiveIdentifier"
- "endActivity:"
- "endMonitoring"
- "ensureAdvertisingStarted"
- "ensureAdvertisingStopped"
- "ensureAdvertisingStoppedWithSeed:"
- "ensurePreferencesUpdatedWithShouldForce:"
- "ensureScanningStarted"
- "ensureScanningStopped"
- "ensureScanningStoppedWithSeed:"
- "enumerateKeysAndObjectsUsingBlock:"
- "ephemeralSessionConfiguration"
- "errorWithDomain:code:userInfo:"
- "eventHandlerContext"
- "eventHandlerFunc"
- "eventQueue"
- "evictCachedDeviceWithID:"
- "evictCachedDeviceWithIDInternal:"
- "evictionPolicies"
- "execOnQueueAsync:"
- "expectedDeviceIDs"
- "extensionChannelAbove"
- "fauxObjectWithDiscoveryToken:name:deviceIdentifier:"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "filterUsingPredicate:"
- "finishTasksAndInvalidate"
- "firstObject"
- "forceReportCachedDevices"
- "forceReportCachedDevicesFound"
- "forceReportCachedDevicesLost"
- "fullRefresh"
- "generateDiversifiedPINWithCompletionHandler:"
- "generateStatisticsReportWithCompletionHandler:"
- "getBTLEMode:"
- "getBytes:length:"
- "getCString:maxLength:encoding:"
- "getCacheDirectoryURLWithParentDirectory:creatingIfNecessary:"
- "getCacheFileURLCreatingParentDirectoriesIfNecessary:"
- "getDeviceID:"
- "getExpectedBonjourService"
- "getExpectedServiceInstanceName"
- "getPairedPeersWithOptions:completion:"
- "getReportableCachedDevices"
- "getRestrictedModeAuthorizationsForCertificateSerial:"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFoundDevice:"
- "handleHomeKitAccessoriesDidChange"
- "handleHomeKitDeviceConfigurationChanged:"
- "handleLostDevice:"
- "handleNetworkSignatureChanged:"
- "handlePairingRequestOfType:withInputCompletionHandler:"
- "handleRealDeviceFoundForCachedDevice:"
- "handleRealDeviceLostForCachedDevice:"
- "handledPairingRequest"
- "hasPrefix:"
- "hash"
- "home"
- "home:didAddAccessory:"
- "home:didAddActionSet:"
- "home:didAddRoom:"
- "home:didAddRoom:toZone:"
- "home:didAddService:toServiceGroup:"
- "home:didAddServiceGroup:"
- "home:didAddTrigger:"
- "home:didAddUser:"
- "home:didAddZone:"
- "home:didEncounterError:forAccessory:"
- "home:didRemoveAccessory:"
- "home:didRemoveActionSet:"
- "home:didRemoveRoom:"
- "home:didRemoveRoom:fromZone:"
- "home:didRemoveService:fromServiceGroup:"
- "home:didRemoveServiceGroup:"
- "home:didRemoveTrigger:"
- "home:didRemoveUser:"
- "home:didRemoveZone:"
- "home:didUnblockAccessory:"
- "home:didUpdateActionsForActionSet:"
- "home:didUpdateHomeHubState:"
- "home:didUpdateNameForActionSet:"
- "home:didUpdateNameForRoom:"
- "home:didUpdateNameForServiceGroup:"
- "home:didUpdateNameForTrigger:"
- "home:didUpdateNameForZone:"
- "home:didUpdateRoom:forAccessory:"
- "home:didUpdateTrigger:"
- "homeConfigurationDidChangeHandler"
- "homeDidUpdateAccessControlForCurrentUser:"
- "homeDidUpdateName:"
- "homeDidUpdateSupportedFeatures:"
- "homeKitDeviceIDs"
- "homeKitDeviceMonitor"
- "homeManager"
- "homeManager:didAddHome:"
- "homeManager:didReceiveAddAccessoryRequest:"
- "homeManager:didRemoveHome:"
- "homeManager:didUpdateAuthorizationStatus:"
- "homeManagerDidUpdateCurrentHome:"
- "homeManagerDidUpdateHomes:"
- "homeManagerDidUpdatePrimaryHome:"
- "homes"
- "i16@0:8"
- "i20@0:8B16"
- "i20@0:8S16"
- "i20@0:8i16"
- "i24@0:8@16"
- "i24@0:8^S16"
- "i24@0:8d16"
- "i28@0:8I16@20"
- "i28@0:8^@16B24"
- "i40@0:8^?16^v24^{OpaqueAPBrowserBTLEManager={__CFRuntimeBase=QAQ}@}32"
- "i64@0:8^@16@24@32@40@48@56"
- "identifier"
- "idsDeviceIdentifier"
- "info"
- "infraAssocCount"
- "infraDisassocCount"
- "infraRelayOperationStatus"
- "infraRelayRequestersCount"
- "infraScanCount"
- "infrastructureChannel"
- "init"
- "initWithAddress:"
- "initWithBrowser:"
- "initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:"
- "initWithBytes:"
- "initWithCapacity:"
- "initWithConfiguration:"
- "initWithDatapathID:role:peerMacAddress:"
- "initWithEventContext:"
- "initWithHandleAuthorizationRequestBlock:logContext:"
- "initWithLogContext:sslCertificateHostName:"
- "initWithObjects:"
- "initWithOptions:cachePolicy:"
- "initWithRequestHandler:"
- "initWithServiceType:"
- "initWithSet:"
- "instanceName"
- "intValue"
- "internalBrowserQueue"
- "internalQueue"
- "internetSharingPolicy"
- "invalidate"
- "invalidateInternal"
- "invalidated"
- "invalidationHandler"
- "is2GHz"
- "is5GHz"
- "is6GHz"
- "is6GHzPSC"
- "isAdvertising"
- "isBrowsing"
- "isCarPlay"
- "isDeviceCacheable:"
- "isEnabled"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToSet:"
- "isEqualToString:"
- "isInvalidated"
- "isKindOfClass:"
- "isLinkDownDebounceInProgress"
- "isMemberOfClass:"
- "isProxy"
- "isPublicAirPlayNetwork"
- "isRemoteDeviceConnected"
- "isScanning"
- "isSoloBeaconDisabled"
- "isValidNetworkSignature:"
- "isWiredCarPlaySimulator"
- "itemWithDeviceInfo:userInfo:"
- "label"
- "lastPathComponent"
- "length"
- "loadCache"
- "localDataAddress"
- "localizedDescription"
- "localizedFailureReason"
- "lowercaseString"
- "mediaRouteIdentifier"
- "metadata"
- "moveItemAtPath:toPath:error:"
- "mutableCopy"
- "nearbySoloDevicesCount"
- "networkName"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedShort:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "overrideDistance:"
- "packetsHOFOn2GCount"
- "packetsNAVOn2GCount"
- "packetsOn2GCount"
- "packetsOn5GCount"
- "packetsOverridenOn5GCount"
- "pairingRequestCompletedForDataSession:pairingKeyStoreID:deviceID:"
- "pairingRequestStartedForDataSession:nfcTagScannedCompletionHandler:"
- "pairingRequestStartedForDataSession:passphraseInputCompletionHandler:"
- "pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:"
- "pairingRequestStartedForDataSession:qrCodeScannedCompletionHandler:"
- "path"
- "peerAddress"
- "peerMACAddressData"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "powerOn"
- "predicateWithBlock:"
- "preferencesUpdated"
- "preferred2GChannelsCount"
- "preferred5GChannelsCount"
- "prepareDeviceInfo:"
- "prepareForRemovingWiFiUUID:completion:"
- "presentRealDevices"
- "primaryNetworkSignature"
- "protectionSpace"
- "q16@0:8"
- "queue"
- "quietIECount"
- "r^v"
- "r^v16@0:8"
- "rangeOfString:"
- "realDeviceFound:"
- "realDeviceFound:userInfo:"
- "realDeviceFoundInternal:"
- "realDeviceLost:"
- "realDeviceLostInternal:"
- "refreshWithAccessory:isAddOrUpdate:notifyOnAccessoryChange:"
- "refreshWithHome:isAddOrUpdate:notifyOnAccessoriesChanged:"
- "registerAPOOverlaysServerMachService"
- "registerSessionRequestHandlerMachService"
- "release"
- "removeAllExpectedDeviceIDs"
- "removeAllObjects"
- "removeCarPlayHelper:"
- "removeExpectedDeviceID:"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeItemMatchingItem:error:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "replaceObjectAtIndex:withObject:"
- "reportCachedDevice:found:withHandler:"
- "reportDeviceFoundHandler"
- "reportDeviceLostHandler"
- "reportIssue:"
- "reportedCachedDeviceIDs"
- "requestParameters"
- "requestWithURL:cachePolicy:timeoutInterval:"
- "requireDeviceNetworkSignature"
- "respondsToSelector:"
- "restrictedModeAuthorizationsForCertificateSerial:"
- "resume"
- "retain"
- "retainCount"
- "runWithConfiguration:"
- "rxFWDelayHistogram"
- "rxIPCDelayHistogram"
- "rxRSSIHistogram"
- "self"
- "sendRequestID:request:options:responseHandler:"
- "serverTrust"
- "serviceTypes"
- "session:didGenerateShareableConfigurationData:forObject:"
- "session:didInvalidateWithError:"
- "session:didRemoveNearbyObjects:withReason:"
- "session:didUpdateAlgorithmConvergence:forObject:"
- "session:didUpdateDLTDOAMeasurements:"
- "session:didUpdateNearbyObjects:"
- "sessionDidStartRunning:"
- "sessionSuspensionEnded:"
- "sessionWasSuspended:"
- "sessionWithConfiguration:"
- "set"
- "setAWDLPeerTrafficRegistration:error:"
- "setAccessGroup:"
- "setAccessibleType:"
- "setActionHandler:"
- "setActivatedPresentDeviceStashing:"
- "setActive:"
- "setAirplaySourceFlags:"
- "setAllowsCellularAccess:"
- "setAuthPromptWasDismissed:"
- "setBTLEMode:"
- "setBonjourBrowser:"
- "setBonjourProtocol:"
- "setBonjourServiceName:"
- "setBrowseForAltReceiver:"
- "setBtleAdvertiser:"
- "setBtleAdvertiserSeed:"
- "setBtleDevices:"
- "setBtleDiscoverer:"
- "setBtleDiscovererSeed:"
- "setBtleDiscoveryManagerToken:"
- "setCache:"
- "setCachedDeviceFoundHandler:"
- "setCachedDeviceLostHandler:"
- "setControlFlags:"
- "setCurrentNetworkSignature:"
- "setDelegate:"
- "setDelegateQueue:"
- "setDestinationDevice:"
- "setDeviceFoundHandler:"
- "setDeviceFoundHandlerBlock:"
- "setDeviceIdentifiers:"
- "setDeviceInfo:"
- "setDeviceLostHandler:"
- "setDiscoveryFlags:"
- "setDiskWriteCoalescer:"
- "setDispatchQueue:"
- "setEventHandler:"
- "setEventHandler:context:managerRef:"
- "setEventHandlerContext:"
- "setEventHandlerFunc:"
- "setEvictionPolicies:"
- "setExpectedDeviceIDs:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHandledPairingRequest:"
- "setHomeConfigurationDidChangeHandler:"
- "setHomeKitDeviceMonitor:"
- "setHomeManager:"
- "setIdentifier:"
- "setInactiveUpdatingLevel:"
- "setInstanceName:"
- "setInternalBrowserQueue:"
- "setInternalQueue:"
- "setInterruptionHandler:"
- "setInvalidated:"
- "setInvalidationHandler:"
- "setIsAdvertising:"
- "setIsBrowsing:"
- "setIsEnabled:"
- "setIsInvalidated:"
- "setIsScanning:"
- "setIsSoloBeaconDisabled:"
- "setLabel:"
- "setLeeway:"
- "setMaxDelay:"
- "setMetadata:"
- "setMinDelay:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPeerContextList:"
- "setPeerEndpoint:"
- "setPreferencesUpdated:"
- "setPresentRealDevices:"
- "setPrimaryNetworkChangedHandler:"
- "setReportDeviceFoundHandler:"
- "setReportDeviceLostHandler:"
- "setReportedCachedDeviceIDs:"
- "setRequireDeviceNetworkSignature:"
- "setRtpSequenceNumber:"
- "setRtpStartTime:"
- "setServiceName:"
- "setServiceType:"
- "setSessionFlags:"
- "setStateUpdatedHandler:"
- "setSupportsSolo:"
- "setSystemMonitor:"
- "setTerminationHandler:"
- "setTimeToLiveSeconds:"
- "setTimeoutIntervalForResource:"
- "setTimeoutTimer:"
- "setTrafficFlags:"
- "setType:"
- "setUsePresentDeviceStashing:"
- "setUserInfo:"
- "setValue:forHTTPHeaderField:"
- "setWaitsForConnectivity:"
- "setWfaConnectionMode:"
- "setWfaPairSetupServiceSpecificInfo:"
- "setWfaPairingCacheEnabled:"
- "setWfaPairingDelegate:"
- "setWfaPairingMetadata:"
- "setWfaPairingMethod:"
- "setWithSet:"
- "setupBonjourBrowser"
- "setupDiskWriteCoalescer"
- "setupEvictionPolicies"
- "setupIntrospector"
- "sharedInstance"
- "shouldAdvertiseSourcePresence"
- "shouldEvict:"
- "shouldEvictDevice:policy:"
- "shouldProcessDeviceForCache:"
- "sortedArrayUsingComparator:"
- "sourceVersion"
- "standardizedURL"
- "startAdvertisingCarPlayControlForUSB"
- "startAdvertisingCarPlayControlForUSBWithHost:"
- "startAdvertisingCarPlayControlForWiFiUUID:"
- "startAdvertisingCarPlayControlForWiFiUUID:host:"
- "startBonjourBrowser"
- "startBrowsingFor:withTimeout:deviceFoundHandler:"
- "startMode:"
- "startMonitoringEventType:error:"
- "startSessionWithHost:completion:"
- "startSessionWithHost:requestIdentifier:completion:"
- "startTimerWithTimeout:"
- "statusCode"
- "statusFlags"
- "stop"
- "stopBrowsing"
- "stopBrowsingWithError:"
- "stopMonitoringEventType:"
- "stoppedSessionForHostIdentifier:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringForBTLEMode:"
- "stringForBTLEState:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "substringToIndex:"
- "superclass"
- "supportsMutualAuthentication"
- "supportsSoloMode"
- "systemMonitor"
- "textInfo"
- "timeIntervalSinceReferenceDate"
- "timeToLiveSeconds"
- "timeoutTimer"
- "trigger"
- "txCCAHistogram"
- "txChipModeErrorCount"
- "txConsecutiveErrorsHistogram"
- "txDroppedCount"
- "txErrorCount"
- "txExpiredCount"
- "txFailedCount"
- "txFirmwareFreePacketCount"
- "txForceLifetimeExpiredCount"
- "txIOErrorCount"
- "txInternalErrorCount"
- "txMaxRetriesCount"
- "txMemoryErrorCount"
- "txNoACKCount"
- "txNoRemotePeerCount"
- "txNoResourcesCount"
- "txPacketExpiryHistogram"
- "uncacheDevice:"
- "unsignedIntValue"
- "updateExpectedDeviceIDsAdding:removing:"
- "updateLinkStatus:"
- "updatePairedPeersWithGroupID:groupInfo:options:completion:"
- "usePresentDeviceStashing"
- "userInfo"
- "v16@0:8"
- "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8i16"
- "v24@0:8@\"CARSessionRequestBonjourHost\"16"
- "v24@0:8@\"HMAccessory\"16"
- "v24@0:8@\"HMHome\"16"
- "v24@0:8@\"HMHomeManager\"16"
- "v24@0:8@\"NISession\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8^?16"
- "v24@0:8^v16"
- "v24@0:8^{BonjourBrowser=}16"
- "v24@0:8^{OpaqueAPCarPlayHelperHelper=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v24@0:8r^v16"
- "v32@0:8@\"CARSessionRequestHost\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"HMAccessory\"16@\"HMAccessoryProfile\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMService\"24"
- "v32@0:8@\"HMAccessory\"16@\"NSString\"24"
- "v32@0:8@\"HMHome\"16@\"HMAccessory\"24"
- "v32@0:8@\"HMHome\"16@\"HMActionSet\"24"
- "v32@0:8@\"HMHome\"16@\"HMRoom\"24"
- "v32@0:8@\"HMHome\"16@\"HMServiceGroup\"24"
- "v32@0:8@\"HMHome\"16@\"HMTrigger\"24"
- "v32@0:8@\"HMHome\"16@\"HMUser\"24"
- "v32@0:8@\"HMHome\"16@\"HMZone\"24"
- "v32@0:8@\"HMHome\"16Q24"
- "v32@0:8@\"HMHomeManager\"16@\"HMAddAccessoryRequest\"24"
- "v32@0:8@\"HMHomeManager\"16@\"HMHome\"24"
- "v32@0:8@\"HMHomeManager\"16Q24"
- "v32@0:8@\"NISession\"16@\"NSArray\"24"
- "v32@0:8@\"NISession\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@\"CARSessionRequestBonjourHost\"24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
- "v32@0:8@\"WiFiAwareDataSession\"16@?<v@?@\"NSData\">24"
- "v32@0:8@\"WiFiAwareDataSession\"16@?<v@?@\"NSString\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8Q16@\"NSData\"24"
- "v32@0:8Q16@24"
- "v32@0:8^{__CFString=}16@?24"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"CARSessionRequestHost\"16@\"NSUUID\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"HMAccessory\"16@\"HMService\"24@\"HMCharacteristic\"32"
- "v40@0:8@\"HMHome\"16@\"HMRoom\"24@\"HMAccessory\"32"
- "v40@0:8@\"HMHome\"16@\"HMRoom\"24@\"HMZone\"32"
- "v40@0:8@\"HMHome\"16@\"HMService\"24@\"HMServiceGroup\"32"
- "v40@0:8@\"HMHome\"16@\"NSError\"24@\"HMAccessory\"32"
- "v40@0:8@\"NISession\"16@\"NIAlgorithmConvergence\"24@\"NINearbyObject\"32"
- "v40@0:8@\"NISession\"16@\"NSArray\"24q32"
- "v40@0:8@\"NISession\"16@\"NSData\"24@\"NINearbyObject\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
- "v40@0:8@\"WiFiAwareDataSession\"16@\"NSUUID\"24Q32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "v40@0:8@16@24q32"
- "v40@0:8@16d24@?32"
- "v44@0:8@16@24B32q36"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v52@0:8Q16@24@32@40B48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24q32q40q48"
- "value"
- "valueForKey:"
- "wantsCarPlayControlAdvertisingForUSB"
- "wantsCarPlayControlAdvertisingForWiFiUUID:"
- "wfaDataSessionClient"
- "wiredIPv6Addresses"
- "wirelessIPv6Addresses"
- "writeCache"
- "writeToURL:atomically:"
- "writeToURL:options:error:"
- "zone"

```
