## terminusd

> `/usr/libexec/terminusd`

```diff

-578.120.3.0.0
-  __TEXT.__text: 0x16ec78
-  __TEXT.__auth_stubs: 0x2820
-  __TEXT.__objc_stubs: 0x8080
-  __TEXT.__objc_methlist: 0x5210
-  __TEXT.__const: 0x25c
-  __TEXT.__gcc_except_tab: 0x3ba4
-  __TEXT.__objc_methname: 0x10e9d
-  __TEXT.__cstring: 0x3ee9a
-  __TEXT.__oslogstring: 0x237b
-  __TEXT.__objc_classname: 0xe3b
-  __TEXT.__objc_methtype: 0x3505
-  __TEXT.__unwind_info: 0x2230
-  __DATA_CONST.__auth_got: 0x1420
-  __DATA_CONST.__got: 0x9e0
+658.0.0.0.2
+  __TEXT.__text: 0x17e728
+  __TEXT.__auth_stubs: 0x2b60
+  __TEXT.__objc_stubs: 0x8680
+  __TEXT.__objc_methlist: 0x5388
+  __TEXT.__const: 0x24c
+  __TEXT.__gcc_except_tab: 0x4244
+  __TEXT.__objc_methname: 0x118f0
+  __TEXT.__cstring: 0x40af5
+  __TEXT.__oslogstring: 0x247e
+  __TEXT.__objc_classname: 0xe87
+  __TEXT.__objc_methtype: 0x382c
+  __TEXT.__unwind_info: 0x23e0
+  __DATA_CONST.__auth_got: 0x15c0
+  __DATA_CONST.__got: 0xa08
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x31f0
-  __DATA_CONST.__cfstring: 0xb9a0
-  __DATA_CONST.__objc_classlist: 0x410
+  __DATA_CONST.__const: 0x3330
+  __DATA_CONST.__cfstring: 0xbd80
+  __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__objc_intobj: 0x5a0
+  __DATA_CONST.__objc_intobj: 0x5e8
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x14828
-  __DATA.__objc_selrefs: 0x2b80
-  __DATA.__objc_ivar: 0x1984
-  __DATA.__objc_data: 0x28a0
+  __DATA.__objc_const: 0x15068
+  __DATA.__objc_selrefs: 0x2d30
+  __DATA.__objc_ivar: 0x1a44
+  __DATA.__objc_data: 0x2990
   __DATA.__data: 0xce8
-  __DATA.__bss: 0x6a0
+  __DATA.__bss: 0x6b0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
-  - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libmrc.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 989E8D8C-F312-3761-B9CF-D357CE45C88C
-  Functions: 2988
-  Symbols:   973
-  CStrings:  11227
+  UUID: 2DEC5460-2A4A-39EB-878D-1C17CF2455EE
+  Functions: 3079
+  Symbols:   1030
+  CStrings:  11526
 
Symbols:
+ _CFStringCompare
+ _CFStringCreateCopy
+ _CFUUIDCreateString
+ _NEVirtualInterfaceCopyNexusInstances
+ _NEVirtualInterfaceEnableFlowswitch
+ _NEVirtualInterfaceRemoveAddress
+ _NRConvertMachTimeToMicroseconds
+ _NRCreateLocalIdentity
+ _NRDiffMachTimeInSeconds
+ _NRDiffMicroTimeInSeconds
+ _OBJC_CLASS_$_NRDeviceInfo
+ _OBJC_CLASS_$_NRDeviceProxyInfo
+ _OBJC_CLASS_$_SecExternalPreSharedKey
+ _SCNetworkInterfaceCopyAll
+ _SCNetworkInterfaceGetBSDName
+ _SCNetworkInterfaceGetInterfaceType
+ _SecCreateSharedWebCredentialPassword
+ __SCNetworkInterfaceCreateWithBSDName
+ __SCNetworkInterfaceIsCarPlay
+ _kSCNetworkInterfaceTypeEthernet
+ _nrXPCKeyDeviceInfo
+ _nrXPCKeySimulateSlicingEnabled
+ _nrXPCKeyTestCompanionAPL
+ _nrXPCKeyUseASQUIC
+ _nr_absolute_time
+ _nr_continuous_time
+ _nw_agent_create_with_quic_migration_info
+ _nw_agent_set_assert_handlers
+ _nw_agent_set_resolve_flags
+ _nw_connection_copy_connected_remote_endpoint
+ _nw_endpoint_copy_port_string
+ _nw_endpoint_get_device_id
+ _nw_http_field_name_proxy_authenticate
+ _nw_http_field_name_proxy_authorization
+ _nw_http_fields_append
+ _nw_http_messaging_create_options
+ _nw_http_proxy_server_cancel
+ _nw_http_proxy_server_create
+ _nw_http_proxy_server_get_port
+ _nw_http_proxy_server_set_outbound_connection_handler
+ _nw_http_proxy_server_set_state_changed_handler
+ _nw_http_proxy_server_start
+ _nw_http_response_create_well_known
+ _nw_http_response_set_status_code
+ _nw_parameters_add_protocol_stack_member
+ _nw_parameters_copy
+ _nw_parameters_create_application_service_quic
+ _nw_parameters_get_parent_id
+ _nw_parameters_set_attach_protocol_listener
+ _nw_parameters_set_local_endpoint
+ _nw_parameters_set_multipath_service
+ _nw_parameters_set_server_mode
+ _nw_path_copy_endpoint
+ _nw_path_copy_path_for_client
+ _nw_protocol_copy_swift_tls_record_definition
+ _nw_protocol_create_options
+ _nw_protocol_stack_prepend_application_protocol
+ _nw_proxy_config_set_prohibit_direct
+ _nw_quic_migration_info_copy_data
+ _nw_quic_migration_info_create
+ _nw_quic_migration_info_set_interface
+ _nw_quic_migration_info_set_remote_endpoint
+ _nw_service_connector_create_with_endpoint
+ _nw_tcp_create_options
+ _sec_protocol_options_set_external_pre_shared_key_selection_block
+ _sec_protocol_options_set_use_raw_external_pre_shared_keys
+ _uuid_generate
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _NEVirtualInterfaceEnableChannelAndGetNexusInstance
- _OBJC_CLASS_$_CBPeripheral
- _SecGenerateSelfSignedCertificate
- _SecIdentityCreate
- _nw_parameters_copy_avoided_netagent_types
- _sec_identity_create_with_certificates
CStrings:
+ "\nCompanion APL allowed: %s"
+ "%@ (c: %@, p: %@)"
+ "%@: Expected to receive only %u nexus instances: %@"
+ "%@://%@:%u"
+ "%@://[%@]:%u"
+ "%s called with null (configure_tcp != (_nw_parameters_configure_protocol_disable))"
+ "%s called with null advertisedEndpoint"
+ "%s called with null configure_tcp"
+ "%s called with null configure_tls"
+ "%s called with null self.virtualInterface"
+ "%s called with null virtualInterface"
+ "%s%.30s:%-4d %@ Updating usesTLS %d to %d"
+ "%s%.30s:%-4d %@ failed to add policy %@ to session %@"
+ "%s%.30s:%-4d %@ removing policies"
+ "%s%.30s:%-4d %@: Active: Device RSSI %d Target RSSI %d"
+ "%s%.30s:%-4d %@: Both sides support APL"
+ "%s%.30s:%-4d %@: Both sides use APL"
+ "%s%.30s:%-4d %@: Created UTUN nexus instances: %@"
+ "%s%.30s:%-4d %@: Failed to enable channel for UTUN"
+ "%s%.30s:%-4d %@: Ignoring device with invalid timestamp: %@"
+ "%s%.30s:%-4d %@: Ignoring device with no Watch setup data: %@"
+ "%s%.30s:%-4d %@: Ignoring device with too short Watch setup data (%zu < %zu): %@"
+ "%s%.30s:%-4d %@: Ignoring device with unrecognized header version %u: %@"
+ "%s%.30s:%-4d %@: Ignoring stale advertisement last seen %fs ago: %@"
+ "%s%.30s:%-4d %@: Inactive: Device RSSI %d Target RSSI %d"
+ "%s%.30s:%-4d %@: Local doesn't support APL, but remote does"
+ "%s%.30s:%-4d %@: Local doesn't use APL, but remote does"
+ "%s%.30s:%-4d %@: Not setting allow multicast flag on a link with no interface"
+ "%s%.30s:%-4d %@: Pairing completion timer expired while pairing %@"
+ "%s%.30s:%-4d %@: Remote doesn't support APL, but local does"
+ "%s%.30s:%-4d %@: Remote doesn't use APL, but local does"
+ "%s%.30s:%-4d %@: Setting packetNexus.availability: %lu -> %lu"
+ "%s%.30s:%-4d %@: added addresses to virtual interface %@ : %@"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (httpProxyServerEndpoint) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (self.httpConnectProxyServer) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: lrbIOVecLen > 0; tlvLen=%u filledInLinkReadBufferBytes=%u handledLinkReadBufferBytes=%u"
+ "%s%.30s:%-4d Authenticated using Basic authentication"
+ "%s%.30s:%-4d Bad format for username/password: %@"
+ "%s%.30s:%-4d Client %@ trying to set companion APL to %d"
+ "%s%.30s:%-4d Client %@ trying to set simulate slicing enabled to %d"
+ "%s%.30s:%-4d Connection for service %@ entered state %s with error %@"
+ "%s%.30s:%-4d Deferring creating link for %@ as link suspension is in effect for non-nearby links"
+ "%s%.30s:%-4d Did not find Proxy-Authorization header"
+ "%s%.30s:%-4d Failed to create http connect proxy server"
+ "%s%.30s:%-4d Failed to get exec UUID for %d"
+ "%s%.30s:%-4d Incorrect Proxy-Authorization for user: %@"
+ "%s%.30s:%-4d Invalid Proxy-Authorization header: %s"
+ "%s%.30s:%-4d Proxy Authorization failed"
+ "%s%.30s:%-4d Received new connection endpoint:%@ request:%@"
+ "%s%.30s:%-4d Setting Companion APL allowed to %@"
+ "%s%.30s:%-4d Setting Simulate slicing enabled to %d"
+ "%s%.30s:%-4d advertise stopped for %@ : %@"
+ "%s%.30s:%-4d advertising services %@"
+ "%s%.30s:%-4d asName %@ requires classC connection"
+ "%s%.30s:%-4d completed writing data %u/%zu bytes"
+ "%s%.30s:%-4d http connect proxy server cancelled"
+ "%s%.30s:%-4d http connect proxy server is already running"
+ "%s%.30s:%-4d http connect proxy server started %u port:%u"
+ "%s%.30s:%-4d ignoring in-progress resolve request for %@"
+ "%s%.30s:%-4d ignoring inactive interface: %@"
+ "%s%.30s:%-4d ignoring resolve request for %@ as they are complete"
+ "%s%.30s:%-4d l2CAP channel read error %@"
+ "%s%.30s:%-4d l2CAP channel write error %@"
+ "%s%.30s:%-4d not resolving asName %@ as classC is not connected"
+ "%s%.30s:%-4d not starting QR link for %@"
+ "%s%.30s:%-4d not starting link due to pending companion APL enablement"
+ "%s%.30s:%-4d overriding device ID to companion link"
+ "%s%.30s:%-4d parser failed to handle full packet"
+ "%s%.30s:%-4d received %lu datagrams"
+ "%s%.30s:%-4d received flow assert for %@ (%p) from %@ (%@)"
+ "%s%.30s:%-4d received flow assert without an appsvc name"
+ "%s%.30s:%-4d received flow unassert for %@ (%p) from %@ (%@)"
+ "%s%.30s:%-4d received flow unassert without an appsvc name"
+ "%s%.30s:%-4d received start advertise request for %@ (%p) from %@ (%@, %@)"
+ "%s%.30s:%-4d received start browse request for %@ (%p) from %@ (%@)"
+ "%s%.30s:%-4d received start resolve request for %@ (%p) from %@ (%@)"
+ "%s%.30s:%-4d received unexpected flow assert for %@"
+ "%s%.30s:%-4d received unexpected flow unassert for %@"
+ "%s%.30s:%-4d removing endpoint for asName %@ %@"
+ "%s%.30s:%-4d removing endpoints %@"
+ "%s%.30s:%-4d scanning services %@"
+ "%s%.30s:%-4d simulating cellular slicing enabled as per settings"
+ "%s%.30s:%-4d start http connect proxy server : %@"
+ "%s%.30s:%-4d starting BT scans for services %@"
+ "%s%.30s:%-4d stopping BT scans"
+ "%s%.30s:%-4d successfully marked interface %@ as companion link interface"
+ "%s%.30s:%-4d token matched for asName %@ sent %@ received %@"
+ "%s%.30s:%-4d token mismatched for asName %@ sent %@ received %@"
+ "%s%.30s:%-4d unpublishing published PSMs %@"
+ "%{public}s Assertion Failed: (httpProxyServerEndpoint) != ((void*)0)"
+ "%{public}s Assertion Failed: (self.httpConnectProxyServer) != ((void*)0)"
+ "%{public}s Assertion Failed: lrbIOVecLen > 0; tlvLen=%u filledInLinkReadBufferBytes=%u handledLinkReadBufferBytes=%u"
+ "+[NRDDeviceConductor createDeviceMonitorDictWithNRUUID:isNearby:isConnected:isCloudConnected:isAsleep:isClassCConnected:hasUnpairedBluetooth:linkType:linkSubtype:proxySvcIntfName:thermalPressure:pluggedIn:deviceInfo:replyDict:]"
+ "+[NRDLocalDevice resumeNonNearbyLinksForNRUUID:]"
+ "+[NRDLocalDevice suspendNonNearbyLinksForNRUUID:]"
+ "+[NRDLocalDevice updateReceivedProxyNotifyPayloadInner:nrUUID:saveToDisk:]"
+ "+[NRDLocalDevice updateRemoteDeviceFlagsInner:nrUUID:saveToDisk:]"
+ "+[NRDLocalDevice updateUsesTLS:nrUUID:]"
+ "-[NRASMRequest dealloc]"
+ "-[NRASMResolveRequest deviceIdentifier]"
+ "-[NRApplicationServiceManager canSkipQRAssert:]"
+ "-[NRApplicationServiceManager removeEndpointForASName:endpoint:]"
+ "-[NRApplicationServiceManager setupResolverAgent]_block_invoke_8"
+ "-[NRApplicationServiceManager setupResolverAgent]_block_invoke_9"
+ "-[NRApplicationServiceManager shouldResolveASNameAfterClassCUnlock:]"
+ "-[NRCompanionProxyAgent registerAgentForLink:]"
+ "-[NRDDeviceConductor addCompanionScopingAgentToInterface:]"
+ "-[NRDDeviceConductor addIPTunnelPolicyForLinkInner:policyOrder:]"
+ "-[NRDDeviceConductor createCatchAllInterfaceIfNeeded]"
+ "-[NRDDeviceConductor createTokenAgentForToken:]_block_invoke"
+ "-[NRDDeviceConductor createTokenAgentForToken:]_block_invoke_2"
+ "-[NRDDeviceConductor didStopAdvertiseRequestForASName:endpoint:asClient:]"
+ "-[NRDTestServer setupTestServer]_block_invoke"
+ "-[NRDTestServer setupTestServer]_block_invoke_2"
+ "-[NRDevicePairingManagerContext handlePairingCompletionTimerExpiry]"
+ "-[NRLinkBluetooth configureVirtualInterfaceAddresses]"
+ "-[NRLinkBluetooth readPacketsFromL2CAPChannel]_block_invoke"
+ "-[NRLinkDirector cancelHTTPConnectProxyServer]"
+ "-[NRLinkDirector handleHTTPConnectProxyAuthorization:]"
+ "-[NRLinkDirector handleHTTPConnectProxyAuthorization:]_block_invoke"
+ "-[NRLinkDirector startHTTPConnectProxyServerIfNeeded]"
+ "-[NRLinkDirector startHTTPConnectProxyServerIfNeeded]_block_invoke"
+ "-[NRLinkDirector startHTTPConnectProxyServerIfNeeded]_block_invoke_3"
+ "-[NRLinkDirector updateCompanionAPLEnabled:nrUUID:]"
+ "-[NRLinkDirector updateDeviceMonitorConnectionsForNRUUID:]"
+ "-[NRLinkManagerBluetooth advertiseServiceUUIDs:identifier:]"
+ "-[NRLinkManagerBluetooth centralManager:didDiscoverPeripheral:advertisementData:RSSI:]"
+ "-[NRLinkManagerBluetooth invalidatePeripheralManager]"
+ "-[NRLinkManagerBluetooth monitorL2CAPChannelConnectionsForPSM:serviceUUID:bluetoothRole:updateBlock:]"
+ "-[NRLinkManagerBluetooth scanForServiceUUIDs:identifier:]"
+ "-[NRLinkManagerBluetooth startScanningIfNeeded]"
+ "-[NRLinkManagerBluetooth stopScanningIfNeeded]"
+ "-[NRLinkManagerWiFi createIRLinkForNRUUIDs:]"
+ "-[NRLinkQuickRelay setupUTUN]"
+ "-[NRLinkWiFi getOrSendIDSDeviceID]_block_invoke"
+ "-[NRLinkWiFi getOrSendIDSDeviceID]_block_invoke_2"
+ "-[NRLinkWiFi sendNotifyPayload]_block_invoke"
+ "-[NRLinkWired getOrSendIDSDeviceID]_block_invoke"
+ "-[NRLinkWired getOrSendIDSDeviceID]_block_invoke_2"
+ "-[NRLinkWired sendNotifyPayload]_block_invoke"
+ "."
+ "0.0.0.0"
+ "04:25:30"
+ "658.0.0.0.2"
+ ":"
+ "<%@>"
+ "@\"NRASMRequestMetadata\""
+ "@\"NSObject<OS_nw_endpoint>\""
+ "@\"NSObject<OS_nw_http_proxy_server>\""
+ "@20@0:8C16"
+ "@28@0:8B16^B20"
+ "Basic"
+ "Basic realm=\"Access to internal site\""
+ "Companion"
+ "CompanionAPL"
+ "CompanionLinkMLKEM"
+ "DC_Dealloc"
+ "DTC Fallback"
+ "DTCFallbackAgent"
+ "Device is not eligible for migration or graduation!"
+ "DirectToCloudAgent-%@"
+ "Failed to add policy"
+ "Failed to add policy %@ to session %@"
+ "Failed to serialize deviceInfo"
+ "Failed to setup nexus instance"
+ "May 23 2025"
+ "Migration info"
+ "NRASMRequestMetadata"
+ "NRBluetoothAdvertiseRequest"
+ "NRBluetoothAdvertiseRequest[services: %@]"
+ "NRBluetoothScanRequest"
+ "NRBluetoothScanRequest[services: %@]"
+ "NRCopyExecUUIDFromProcessPID"
+ "NRCopyNexusInstancesForInterface"
+ "NRLinkCopyTransportChildSAConfigForInitiator"
+ "NRLinkCopyTunnelChildSAConfigForInitiator"
+ "NRLinkParserWriteOutputCallback_block_invoke"
+ "T@\"NSObject<OS_nw_agent>\",&,N,V_migrationInfoAgent"
+ "T@\"NSObject<OS_nw_endpoint>\",&,N"
+ "T@\"NSObject<OS_nw_endpoint>\",R,N,V_proxyEndpoint"
+ "T@\"NWNetworkAgentRegistration\",&,N,V_shoesProxyAgentRegistration"
+ "TB,N,V_isSendingLocalClassCUnlockNotify"
+ "TB,N,V_needsToSendLocalClassCUnlockNotify"
+ "UUIDWithNSUUID:"
+ "_advertiseRequests"
+ "_asQUICServiceConnector"
+ "_attachedToInterface"
+ "_companionScopingAgent"
+ "_deviceIdentifier"
+ "_discoveredPeripherals"
+ "_discoveryRSSIThreshold"
+ "_dtcFallbackAgent"
+ "_dtcFallbackAgentUUID"
+ "_externalLinkInterfaceNames"
+ "_flow"
+ "_hasPendingClassCASNameResolveRequest"
+ "_hasPendingCompanionAPLEnablement"
+ "_hasPolicies"
+ "_httpConnectProxyServer"
+ "_incomingResolveASNameToToken"
+ "_ipHeaderOffset"
+ "_isClassC"
+ "_isSendingLocalClassCUnlockNotify"
+ "_metadata"
+ "_migrationInfoAgent"
+ "_needsTemporaryCentralManager"
+ "_needsToSendLocalClassCUnlockNotify"
+ "_outgoingResolveASNameToToken"
+ "_pairingCompletionTimer"
+ "_parentIdentifier"
+ "_pid"
+ "_proxyEndpoint"
+ "_proxyPassword"
+ "_proxyUserName"
+ "_psk"
+ "_pskIdentity"
+ "_removeEndpoints"
+ "_resolveCompleted"
+ "_resolverHasCompleteOnConnect"
+ "_scanRequests"
+ "_serviceUUIDs"
+ "_setError"
+ "_shoesProxyAgentRegistration"
+ "_skipQRAssert"
+ "_suspendNonNearbyLinks"
+ "allowsApplicationServiceConnections"
+ "bleAdvertisementTimestampMachContinuous"
+ "c"
+ "classC"
+ "clientFlags:"
+ "com.apple.networkrelay.encoded"
+ "com.apple.networkrelay.test-server"
+ "companionAPLAllowed"
+ "context"
+ "copyLocalOuterEndpoint:"
+ "copyNotifyPayloadsToSendWithProxy:sendingClassC:"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "didStopAdvertiseRequestForASName:endpoint:asClient:"
+ "external_identity"
+ "extraSupportedSignatureHashes"
+ "failed to configure addresses"
+ "getOrSendIDSDeviceID"
+ "handleSetCompanionAPLForTesting"
+ "handleSimulateSlicingEnabled"
+ "hasError"
+ "https"
+ "initWithAdvisoryAgentDomain:agentType:advisoryMode:"
+ "initWithBase64EncodedData:options:"
+ "initWithExternalIdentity:::"
+ "initWithUnsignedShort:"
+ "invalid endpoint %@"
+ "ioctl SIOCGIFTYPE failed: [%d] %s"
+ "ioctl SIOCSIFISCOMPANIONLINK failed: [%d] %s"
+ "ip-header-offset"
+ "isPacketBased"
+ "isSendingLocalClassCUnlockNotify"
+ "kCBMsgArgAddressString"
+ "kCBMsgArgLocalIRK"
+ "l"
+ "link suspension in effect for non-nearby links"
+ "migrationInfoAgent"
+ "needsToSendLocalClassCUnlockNotify"
+ "nr_parameters_create_secure_tcp"
+ "nw_tcp_create_options failed"
+ "nw_tls_create_options failed"
+ "openPacketL2CAPChannel:withIncomingMTU:options:"
+ "outOfBandKey was nil and !wasInitiallySetupUsingIDSPairing and !isModernPairing and !isExternalPairing"
+ "outOfBandKey was nil and !wasInitiallySetupUsingIDSPairing and !isModernPairing and !isExternalPairing for NRUUID %@"
+ "peripheral:didCompleteChannelSoundingProcedure:error:"
+ "position"
+ "proxyEndpoint"
+ "proxyInfo"
+ "proxyProviderAuthMode"
+ "proxyProviderType"
+ "publishPacketL2CAPChannel:requiresEncryption:withIncomingMTU:options:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "readPacketsWithCompletionHandler:"
+ "remoteEndpoint"
+ "removeEndpoint"
+ "sendData:withCompletion:"
+ "sendNotifyPayload"
+ "serviceUUID"
+ "setByAddingObject:"
+ "setConnectedInterfaceName:"
+ "setConnectedLinkSubtype:"
+ "setConnectedLinkType:"
+ "setHttpConnectPSK:"
+ "setHttpConnectPSKIdentity:"
+ "setHttpConnectPassword:"
+ "setHttpConnectURLs:"
+ "setHttpConnectUserName:"
+ "setIsSendingLocalClassCUnlockNotify:"
+ "setMigrationInfoAgent:"
+ "setNeedsToSendLocalClassCUnlockNotify:"
+ "setPosition:"
+ "setProxyEndpoint:"
+ "setProxyInfo:"
+ "setProxyProviderType:"
+ "setShoesProxyAgentRegistration:"
+ "shoesProxyAgentRegistration"
+ "shouldSendIDSDeviceID"
+ "simulateSlicingEnabled"
+ "skipQRAssert"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringValue"
+ "stringWithCString:encoding:"
+ "suspendNonNearbyLinks"
+ "terminusd.SystemConfiguration"
+ "terminusdSettingsSetCompanionAPLAllowed"
+ "terminusdSettingsSetSimulateSlicingEnabled"
+ "unregisterAllEndpoints"
+ "v24@?0@\"NSObject<OS_nw_agent_client>\"8@?<v@?ii@\"NSObject<OS_dispatch_data>\">16"
+ "v28@?0@\"NSError\"8S16@\"NSDictionary\"20"
+ "v32@?0@\"NSObject<OS_sec_protocol_metadata>\"8@\"NSArray\"16@?<v@?@\"SecExternalPreSharedKey\">24"
+ "v40@0:8@\"CBPeripheral\"16@\"NSDictionary\"24@\"NSError\"32"
+ "v40@0:8@\"NSString\"16@\"NSObject<OS_nw_endpoint>\"24@\"NRApplicationServiceClient\"32"
+ "v40@?0@\"NSObject<OS_nw_endpoint>\"8@\"NSObject<OS_nw_parameters>\"16@\"NSObject<OS_nw_http_request>\"24@?<v@?@\"NSObject<OS_nw_endpoint>\"@\"NSObject<OS_nw_parameters>\"@\"NSObject<OS_nw_http_response>\"@\"NSObject<OS_dispatch_data>\">32"
+ "v48@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40"
+ "v52@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44"
+ "v52@0:8@16@24I32@36@44"
+ "v56@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40Q48"
+ "v56@0:8@16@24@32@40Q48"
+ "v60@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44Q52"
+ "v60@0:8@16@24I32@36@44Q52"
+ "\xc1"
- "\v"
- "%@: Attempting to set allow multicast flag on a link with no interface"
- "%@: Expected to receive only %d nexus instances: %@"
- "%@: os_channel_attr_get(MONITOR) returned %d"
- "%s called with null childSAConfiguration"
- "%s called with null ikeSAConfiguration"
- "%s called with null privateKey"
- "%s called with null publicKey"
- "%s%.30s:%-4d %@: Active: RSSI %d Target RSSI %d"
- "%s%.30s:%-4d %@: Inactive: RSSI %d Target RSSI %d"
- "%s%.30s:%-4d %@: Link Channel MONITOR = %llu"
- "%s%.30s:%-4d %@: Nexus Channel MONITOR = %llu"
- "%s%.30s:%-4d %@: Sending IKEv2 data of length %llu"
- "%s%.30s:%-4d %@: deferring further candidate processing until next advertisement"
- "%s%.30s:%-4d %@: handling uIKE packet of %llu bytes"
- "%s%.30s:%-4d %@: updated interface \"%@\" with addresses %@ (classC)"
- "%s%.30s:%-4d %@: updated interface \"%@\" with addresses %@ (classD)"
- "%s%.30s:%-4d Connection for service %@ entered state %swith error %@"
- "%s%.30s:%-4d MASQUEProxyServer feature disabled"
- "%s%.30s:%-4d SecGenerateSelfSignedCertificate() failed"
- "%s%.30s:%-4d SecIdentityCreate() failed"
- "%s%.30s:%-4d already paired with peripheral %@"
- "%s%.30s:%-4d received start advertise request for %@ (%p) from %@"
- "%s%.30s:%-4d received start browse request for %@ (%p) from %@"
- "%s%.30s:%-4d received start resolve request for %@ (%p) from %@"
- "%s%.30s:%-4d using existing central manager"
- "%s%.30s:%-4d using existing peripheral manager"
- "+[NRDDeviceConductor createDeviceMonitorDictWithNRUUID:isNearby:isConnected:isCloudConnected:isAsleep:isClassCConnected:hasUnpairedBluetooth:linkType:linkSubtype:proxySvcIntfName:thermalPressure:pluggedIn:replyDict:]"
- "+[NRDLocalDevice updateRemoteDeviceFlags:nrUUID:]"
- ", local"
- "-[NRCompanionProxyAgent registerAgent]"
- "-[NRDDeviceConductor createCatchAllInterface]"
- "-[NRDDeviceConductor updateProxyCriteriaPoliciesIfNeeded]_block_invoke_2"
- "-[NRDDeviceConductor updateProxyCriteriaPoliciesIfNeeded]_block_invoke_3"
- "-[NRLinkManagerBluetooth monitorL2CAPChannelConnectionsForPSM:updateBlock:]"
- "-[NRLinkManagerBluetooth updatePairingInfoForPeripheral:]"
- "-[NRLinkManagerBluetooth updatePairingInfoForPeripheral:]_block_invoke"
- "02:14:10"
- "578.120.3"
- "@20@0:8B16"
- "Apr 19 2025"
- "EncryptedIdentity"
- "MASQUEProxyServer"
- "NRCreateLocalIdentity"
- "NRLinkChildSAConfigurationSetInitiatorLifetime"
- "NRLinkIKESAConfigurationSetInitiatorLifetime"
- "O\r*"
- "T@\"NWNetworkAgentRegistration\",&,N,V_proxyAgentRegistration"
- "_completed"
- "_proxyAgentRegistration"
- "copyNotifyPayloadsToSendWithProxy:"
- "openL2CAPChannel:"
- "outOfBandKey was nil and !wasInitiallySetupUsingIDSPairing and !isModernPairing"
- "outOfBandKey was nil and !wasInitiallySetupUsingIDSPairing and !isModernPairing for NRUUID %@"
- "outgoingInterfaceName"
- "proxyAgentRegistration"
- "publishL2CAPChannel:requiresEncryption:"
- "removeNetworkAgentFromInterfaceNamed:"
- "setProxyAgentRegistration:"
- "\xb1"

```
