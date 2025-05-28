## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-755.3.1.0.0
-  __TEXT.__text: 0x80e54
-  __TEXT.__auth_stubs: 0x2b30
-  __TEXT.__objc_methlist: 0x7a4
-  __TEXT.__cstring: 0x24ea8
-  __TEXT.__const: 0x204
-  __TEXT.__gcc_except_tab: 0x2dc
+760.20.1.0.0
+  __TEXT.__text: 0x842c4
+  __TEXT.__auth_stubs: 0x2c80
+  __TEXT.__objc_methlist: 0x7c4
+  __TEXT.__cstring: 0x25933
+  __TEXT.__const: 0x214
+  __TEXT.__gcc_except_tab: 0x304
   __TEXT.__oslogstring: 0x16e
-  __TEXT.__unwind_info: 0x142c
-  __TEXT.__objc_classname: 0xfa
-  __TEXT.__objc_methname: 0x2c0b
-  __TEXT.__objc_methtype: 0xab2
-  __TEXT.__objc_stubs: 0x2ce0
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x2b48
+  __TEXT.__unwind_info: 0x148c
+  __TEXT.__objc_classname: 0xfb
+  __TEXT.__objc_methname: 0x2d79
+  __TEXT.__objc_methtype: 0xac2
+  __TEXT.__objc_stubs: 0x2de0
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x2d90
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12a8
-  __DATA_CONST.__objc_selrefs: 0xbf0
+  __DATA_CONST.__objc_const: 0x1348
+  __DATA_CONST.__objc_selrefs: 0xc30
+  __DATA_CONST.__objc_classrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__const: 0x29d8
-  __AUTH_CONST.__cfstring: 0x5040
+  __AUTH_CONST.__const: 0x2978
+  __AUTH_CONST.__cfstring: 0x51e0
   __AUTH_CONST.__objc_const: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x15a8
+  __AUTH_CONST.__auth_got: 0x1650
   __AUTH.__data: 0xb8
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x178
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0xe0
-  __DATA.__data: 0x1470
-  __DATA.__bss: 0x1dc
+  __DATA.__objc_ivar: 0xf4
+  __DATA.__data: 0x1400
+  __DATA.__bss: 0x1cc
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0x4d8
-  __DATA_DIRTY.__bss: 0x128
+  __DATA_DIRTY.__data: 0x548
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1676
-  Symbols:   5297
-  CStrings:  4194
+  Functions: 1708
+  Symbols:   5406
+  CStrings:  4272
 
Symbols:
+ -[APBonjourCacheManager _auditCachesIfNecessary:event:]
+ -[APBonjourCacheManager _ensureKnownNetworkProfileMonitoringStarted]
+ -[APBonjourCacheManager _handleKnownNetworkProfileUpdate:]
+ -[APCarSessionRequestHandler startSessionWithHost:requestIdentifier:completion:]
+ GCC_except_table12
+ _APSFlatQueueCreate
+ _APSFlatQueueDequeueWhileB
+ _APSFlatQueueEnqueue
+ _APSFlatQueueIsEmpty
+ _APSSettingsIsFeatureEnabled
+ _APTPackageRTPBufferedCreateWithBBuf
+ _APTPackageRTPBufferedGetHeaderSize
+ _APTPackageRTPBufferedGetPayloadSize
+ _APTransportConnectionGetStatusString
+ _APTransportPackageBufferedAPAPCreateWithBBuf
+ _APTransportPackageBufferedAPAPGetHeaderSize
+ _APTransportPackageBufferedAPAPGetPayloadSize
+ _APTransportStreamSendData
+ _APTransportStreamSendDataCreatingReplyData
+ _CFAllocatorGetTypeID
+ _CFArrayEnsureCreatedAndAppend
+ _CMBlockBufferCreateEmpty
+ _CMBlockBufferIsEmpty
+ _FigCFArrayGetValueAtIndex
+ _OBJC_IVAR_$_APBonjourCacheManager._auditCaches
+ _OBJC_IVAR_$_APBonjourCacheManager._coreWiFiInterface
+ _OBJC_IVAR_$_APBonjourCacheManager._coreWiFiQueue
+ _OBJC_IVAR_$_APBonjourCacheManager._isMonitoringKnownNetworkProfile
+ _OBJC_IVAR_$_APBonjourCacheManager._isPublicAirPlayNetwork
+ ___68-[APBonjourCacheManager _ensureKnownNetworkProfileMonitoringStarted]_block_invoke
+ ___68-[APBonjourCacheManager _ensureKnownNetworkProfileMonitoringStarted]_block_invoke_2
+ ___68-[APBonjourCacheManager _ensureKnownNetworkProfileMonitoringStarted]_block_invoke_3
+ ___68-[APBonjourCacheManager _ensureKnownNetworkProfileMonitoringStarted]_block_invoke_4
+ ___80-[APCarSessionRequestHandler startSessionWithHost:requestIdentifier:completion:]_block_invoke
+ ___80-[APCarSessionRequestHandler startSessionWithHost:requestIdentifier:completion:]_block_invoke_2
+ ___80-[APCarSessionRequestHandler startSessionWithHost:requestIdentifier:completion:]_block_invoke_3
+ ___block_descriptor_40_e8_32w_e18_v16?0"CWFEvent"8lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32o40o_e10_v16?0r^v8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.146
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.55
+ ___block_literal_global.118
+ ___block_literal_global.120
+ ___block_literal_global.150
+ ___block_literal_global.153
+ ___block_literal_global.200
+ ___block_literal_global.204
+ ___tcpunbufnwGuts_connectionHandlePackageHeader_block_invoke
+ ___tcpunbufnwGuts_connectionHandlePackagePayload_block_invoke
+ ___tcpunbufnwGuts_connectionReceivePackages_block_invoke
+ ___tcpunbufnwGuts_connectionSendPackages_block_invoke
+ ___tcpunbufnwGuts_connectionStateChangedHandler_block_invoke
+ ___tcpunbufnwGuts_drainEventQueueAsyncOnCallbackQueue_block_invoke
+ ___tcpunbufnwGuts_drainEventQueueAsyncOnCallbackQueue_block_invoke_2
+ ___tcpunbufnwGuts_handleNewConnectionInternal_block_invoke
+ ___tcpunbufnwGuts_updatePackageTrackingInternal_block_invoke
+ ___tcpunbufnw_Resume_block_invoke_2
+ ___tcpunbufnw_SetProperty_block_invoke
+ __dispatch_data_empty
+ _dispatch_data_get_size
+ _kAPCarPlayHelperSessionHostInfoKey_AuthenticationCertificateSerial
+ _kAPCarPlayHelperSessionHostInfoKey_PairedVehicleIdentifier
+ _kAPCarPlayHelperSessionHostInfoKey_RequestIdentifier
+ _kAPTransportConnectionOption_IsPackageDeliveryTrackingEnabled
+ _kAPTransportConnectionProperty_BBufBackingAllocator
+ _kAPTransportConnectionProperty_LastDeliveredPackage
+ _kAPTransportConnectionProperty_ShouldReceivePackages
+ _kAPTransportStreamProperty_LastDeliveredMessage
+ _nw_connection_copy_endpoint
+ _nw_connection_fillout_tcp_connection_info
+ _nw_connection_force_cancel
+ _nw_endpoint_copy_interface
+ _nw_listener_set_new_connection_limit
+ _nw_parameters_copy_required_interface
+ _nw_parameters_set_no_delay
+ _nw_path_copy_effective_remote_endpoint
+ _objc_loadWeakRetained
+ _objc_msgSend$_auditCachesIfNecessary:event:
+ _objc_msgSend$_ensureKnownNetworkProfileMonitoringStarted
+ _objc_msgSend$_handleKnownNetworkProfileUpdate:
+ _objc_msgSend$authenticationCertificateSerial
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$pairedVehicleIdentifier
+ _objc_msgSend$supportsMutualAuthentication
+ _objc_retain_x26
+ _objc_retain_x28
+ _tcpunbufnwGuts_connectionHandlePackagePayload
+ _tcpunbufnwGuts_connectionHandlePotentialDisconnect
+ _tcpunbufnwGuts_connectionReceivePackages
+ _tcpunbufnwGuts_connectionSendPackages
+ _tcpunbufnwGuts_drainEventQueueAsyncOnCallbackQueue
+ _tcpunbufnwGuts_handleNewConnectionInternal
+ _tcpunbufnwGuts_invalidateInternal
+ _tcpunbufnwGuts_setEventCallback
+ _tcpunbufnwGuts_updatePackageTrackingInternal
+ _tcpunbufnwGuts_updateStatus
+ _tcpunbufnwGuts_updateStatusInternal
+ _tcpunbufnwTrackingWindowItem_Copy
+ _tcpunbufnwTrackingWindowItem_Free
- -[APCarSessionRequestHandler startSessionWithHost:completion:]
- _FigCFNumberCreateSInt32
- ___62-[APCarSessionRequestHandler startSessionWithHost:completion:]_block_invoke
- ___62-[APCarSessionRequestHandler startSessionWithHost:completion:]_block_invoke_2
- ___62-[APCarSessionRequestHandler startSessionWithHost:completion:]_block_invoke_3
- ___block_descriptor_tmp.143
- ___block_descriptor_tmp.144
- ___block_descriptor_tmp.177
- ___block_descriptor_tmp.181
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.149
- ___block_literal_global.152
- ___block_literal_global.179
- ___block_literal_global.183
- ___block_literal_global.35
- ___tcpunbufnwGuts_callEventCallbackInternal_block_invoke
- ___tcpunbufnwGuts_invalidate_block_invoke
- ___tcpunbufnwGuts_receiveSinkInternal_block_invoke
- ___tcpunbufnwGuts_sendPackagesInternal_block_invoke
- ___tcpunbufnwGuts_stateChangedHandler_block_invoke
- ___tcpunbufnw_AddEventCallback_block_invoke
- ___tcpunbufnw_RemoveEventCallback_block_invoke
- _tcpunbufnwGuts_receiveSinkInternal
- _tcpunbufnwGuts_sendPackagesInternal
CStrings:
+ "\x13\x12\x11\x12\x12\x16"
+ "%@ already migrated"
+ "%s monitoring known network profile%?{end}: %@"
+ "%{ptr}"
+ "-[APBonjourCacheManager _auditCachesIfNecessary:event:]"
+ "-[APBonjourCacheManager _ensureKnownNetworkProfileMonitoringStarted]_block_invoke_4"
+ "-[APBonjourCacheManager _handleKnownNetworkProfileUpdate:]"
+ "-[APBonjourCacheManager _reportCachedItemsFound:]"
+ "-[APBonjourCacheManager init]"
+ "-[APCarSessionRequestHandler startSessionWithHost:requestIdentifier:completion:]_block_invoke"
+ "0x%hx"
+ "760.20.1"
+ "@\"CWFInterface\""
+ "APBonjourCache.corewifi.%{ptr}"
+ "APTPackageRTPBufferedCreateWithBBuf"
+ "APTPackageRTPBufferedGetHeaderSize"
+ "APTPackageRTPBufferedGetPayloadSize"
+ "APTransportPackageBufferedAPAPGetHeaderSize"
+ "APTransportPackageBufferedAPAPGetPayloadSize"
+ "APTransportStreamSendData"
+ "APTransportStreamSendDataCreatingReplyData"
+ "AirPlayPerf_BufferedDeliveryTracking"
+ "Auditing caches for event: %s device info: %s"
+ "BBufBackingAllocator"
+ "Boolean tcpunbufnwGuts_connectionHandlePotentialDisconnect(APTransportConnectionTCPUnbufferedNWGutsRef, nw_content_context_t, _Bool, nw_error_t)"
+ "BufferedNW"
+ "C16@?0r^v8"
+ "Current"
+ "Detected network profile updated, isPublicAirPlayNetwork: %s -> %s"
+ "Device: %llu exists across %u other network signature%s"
+ "FailedToConnect"
+ "Found existing cache entry for device: %llu cachedLastSeen: %.3fs ago deviceLastSeen: %.3fs ago networkSignature: %@ (%s)"
+ "Ignoring device found on public AirPlay network: %llu, '%@'"
+ "Ignoring request to report cached devices while on public AirPlay network"
+ "IsPackageDeliveryTrackingEnabled"
+ "KnownNetworkProfileChanged"
+ "LastDeliveredMessage"
+ "LastDeliveredPackage"
+ "OSStatus APTPackageRTPBufferedCreateWithBBuf(CFAllocatorRef, CMBlockBufferRef, APTransportPackageRef *)"
+ "OSStatus apapPackage_create(CFAllocatorRef, Boolean, CMBlockBufferRef, APTransportPackageRef *)"
+ "OSStatus tcpunbufnwGuts_handleNewConnectionInternal(APTransportConnectionTCPUnbufferedNWGutsRef, nw_connection_t, Boolean)"
+ "OSStatus tcpunbufnwGuts_updateStatusInternal(APTransportConnectionTCPUnbufferedNWGutsRef, APTransportConnectionStatus, OSStatus)"
+ "Other"
+ "ShouldReceivePackages"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found cache file %'@ for current network signature %'@ which is a public AirPlay network"
+ "[%{ptr}] %s '%##a' (using '%s' interface)..."
+ "[%{ptr}] %s Mutual Authentication requested, sessionHostInfo: %@\n"
+ "[%{ptr}] %s Setting pairedVehicleIdentifier, sessionHostInfo: %@\n"
+ "[%{ptr}] %s Setting requestIdentifier: %@\n"
+ "[%{ptr}] %s StartSessionHost: requestID=%@, host=%@\n"
+ "[%{ptr}] %s to '%##a' err=%#m"
+ "[%{ptr}] APTransportConnectionHTTP with name %'@ created. QoS: %d Priority: %u\n"
+ "[%{ptr}] Resume failed err=%#m"
+ "[%{ptr}] Resuming..."
+ "[%{ptr}] connection state '%s'%?{end} err=%#m"
+ "[%{ptr}] listener started on port %u"
+ "[%{ptr}] listener state '%s'%?{end} err=%#m"
+ "[%{ptr}] received ERROR '%@', disconnecting..."
+ "[%{ptr}] received FIN, disconnecting..."
+ "[%{ptr}] status '%@' -> '%@'%?{end} err=%#m"
+ "[%{ptr}] updatePackageTracking() lastSendSeq=%u unsentByteCount=%u lastDeliveredSeq=%u"
+ "_auditCaches"
+ "_auditCachesIfNecessary:event:"
+ "_coreWiFiInterface"
+ "_coreWiFiQueue"
+ "_ensureKnownNetworkProfileMonitoringStarted"
+ "_handleKnownNetworkProfileUpdate:"
+ "_isMonitoringKnownNetworkProfile"
+ "_isPublicAirPlayNetwork"
+ "accepting connection from"
+ "auditBonjourCache"
+ "authenticationCertificateSerial"
+ "cancelled"
+ "connecting to"
+ "dictionaryWithContentsOfFile:"
+ "disconnected from"
+ "failed to connect to"
+ "fileExistsAtPath:"
+ "invalid"
+ "pairedVehicleIdentifier"
+ "ready"
+ "requestIdentifier"
+ "s"
+ "supportsMutualAuthentication"
+ "tcpunbufnwGuts_callEventCallbackInternal"
+ "tcpunbufnwGuts_connectionHandlePackageHeader"
+ "tcpunbufnwGuts_connectionHandlePackagePayload"
+ "tcpunbufnwGuts_connectionSendPackages"
+ "tcpunbufnwGuts_handleNewConnectionInternal"
+ "tcpunbufnwGuts_updatePackageTrackingInternal"
+ "tcpunbufnwGuts_updateStatusInternal"
+ "tcpunbufnw_getPackageCallbacksForPackageType"
+ "void tcpunbufnwGuts_connectionSendPackages(APTransportConnectionTCPUnbufferedNWGutsRef)"
+ "void tcpunbufnwGuts_connectionSendPackages(APTransportConnectionTCPUnbufferedNWGutsRef)_block_invoke"
+ "void tcpunbufnwGuts_connectionStateChangedHandler(APTransportConnectionTCPUnbufferedNWGutsRef, nw_connection_state_t, nw_error_t)"
+ "void tcpunbufnwGuts_invalidateInternal(APTransportConnectionTCPUnbufferedNWGutsRef)"
+ "void tcpunbufnwGuts_listenerStateChangedHandler(APTransportConnectionTCPUnbufferedNWListenerContext *, nw_listener_state_t, nw_error_t)"
+ "void tcpunbufnwGuts_updatePackageTrackingInternal(APTransportConnectionTCPUnbufferedNWGutsRef, APTransportPackageRef, size_t)"
+ "waiting"
- "\x13\x12\x11\x12\x16"
- "-[APCarSessionRequestHandler startSessionWithHost:completion:]_block_invoke"
- "755.3.1"
- "APTPackageRTPBufferedCreate"
- "OSStatus APTPackageRTPBufferedCreate(CFAllocatorRef, APTransportPackageRef *)"
- "OSStatus apapPackage_create(CFAllocatorRef, Boolean, APTransportPackageRef *)"
- "[%{ptr}] %s StartSessionHost: %@\n"
- "[%{ptr}] APTransportConnectionHTTP with name %'@ created. Connection QoS: %d\n"
- "[%{ptr}] FIN received, disconnecting..."
- "[%{ptr}] Send %s after %.2fms, %.2fms into the interval, %.2fms into the connection lifetime. %zu bytes sent with send status: %#m\n"
- "[%{ptr}] Send would block so partial data sent.\n"
- "[%{ptr}] connecting to '%##a' (using '%s' interface)..."
- "[%{ptr}] disconnected from '%##a' err=%#m"
- "[%{ptr}] failed to connect to '%##a' err=%#m"
- "[%{ptr}] state '%s'%?{end} err=%#m"
- "finished"
- "tcpunbufnwGuts_sendPackagesInternal"
- "transportBufferedAudioUseNW"
- "void APTTrafficMetricsSendFinished(APTTrafficMetricsRef, OSStatus, size_t)"
- "void tcpunbufnwGuts_invalidate(APTransportConnectionTCPUnbufferedNWGutsRef)"
- "void tcpunbufnwGuts_receiveSinkInternal(APTransportConnectionTCPUnbufferedNWGutsRef)_block_invoke"
- "void tcpunbufnwGuts_sendPackagesInternal(APTransportConnectionTCPUnbufferedNWGutsRef)"
- "void tcpunbufnwGuts_sendPackagesInternal(APTransportConnectionTCPUnbufferedNWGutsRef)_block_invoke"
- "void tcpunbufnwGuts_stateChangedHandler(APTransportConnectionTCPUnbufferedNWGutsRef, nw_connection_state_t, nw_error_t)"

```
