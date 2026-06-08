## libAONConnection.dylib

> `/usr/lib/libAONConnection.dylib`

```diff

-142.100.19.0.0
-  __TEXT.__text: 0x7fb4
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x1a7a
-  __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__oslogstring: 0x8de
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x8c
-  __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x270
+236.0.0.0.1
+  __TEXT.__text: 0xa7e8
+  __TEXT.__const: 0x180
+  __TEXT.__cstring: 0x1f1d
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__oslogstring: 0xd38
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x388
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0xa0
-  __DATA.__data: 0x40
-  __DATA.__bss: 0x40
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x238
+  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__weak_auth_got: 0x38
+  __AUTH_CONST.__auth_got: 0x340
+  __DATA.__data: 0x50
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 411A75CF-DF57-3044-BA90-AA484BAFB141
-  Functions: 122
-  Symbols:   386
-  CStrings:  187
+  UUID: 0FEAE6AC-E868-3CD0-BB84-84439812498D
+  Functions: 201
+  Symbols:   489
+  CStrings:  224
 
Symbols:
+ GCC_except_table142
+ _IOConnectUnmapMemory64
+ __Block_copy
+ __ZL34aon_net_status_to_libnetcore_error12AONNetStatus
+ __ZL8fileName.90
+ __ZN22AONNetConnectionClient13onPSKReceivedEj18aon_net_tls_cipheryjPKhmS2_m
+ __ZN22AONNetConnectionClient15onFlowConnectedERKNSt3__15arrayIhLm16EEEjjRK23aon_net_flow_metadata_s
+ __ZN22AONNetConnectionClient18onFlowDisconnectedERKNSt3__15arrayIhLm16EEEj12AONNetStatus
+ __ZN22AONNetConnectionClient21onRxBuffersSubmissionEjPtjt
+ __ZN22AONNetConnectionClient21onTxBuffersCompletionEPtj
+ __ZN4ULPN15TBClientAdaptor10purgeFlowsEN6AONNet14DisconnectModeEb
+ __ZN4ULPN15TBClientAdaptor11connectFlowEyRKNSt3__15arrayIhLm16EEEjjRK17aon_net_if_configRK21aon_net_flow_config_stPKc
+ __ZN4ULPN15TBClientAdaptor12toTBIPConfigERK19aon_net_ip_config_sR22aonnetworking_ipflow_s
+ __ZN4ULPN15TBClientAdaptor13toTLSMetadataERK27aonnetworking_tlsmetadata_sR22aon_net_tls_metadata_s
+ __ZN4ULPN15TBClientAdaptor13updatePathMTUEjt
+ __ZN4ULPN15TBClientAdaptor14disconnectFlowEjN6AONNet14DisconnectModeE
+ __ZN4ULPN15TBClientAdaptor15submitTxBuffersEjPKtj
+ __ZN4ULPN15TBClientAdaptor15toTBALPNStringsERA3_A33_KcmR28aonnetworking_alpnstring_v_s
+ __ZN4ULPN15TBClientAdaptor17completeRxBuffersEPKtj
+ __ZN4ULPN15TBClientAdaptor21registerUseCaseClientERN6AONNet14IUseCaseClientE
+ __ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb
+ __ZNK4ULPN15TBClientAdaptor12getUseCaseIdEv
+ __ZTI22AONNetConnectionClient
+ __ZTIN4ULPN15TBClientAdaptorE
+ __ZTIN6AONNet14IUseCaseClientE
+ __ZTIN6AONNet8IUseCaseE
+ __ZTS22AONNetConnectionClient
+ __ZTSN4ULPN15TBClientAdaptorE
+ __ZTSN6AONNet14IUseCaseClientE
+ __ZTSN6AONNet8IUseCaseE
+ __ZTV22AONNetConnectionClient
+ __ZTVN4ULPN15TBClientAdaptorE
+ __ZnwmSt19__type_descriptor_t
+ ____ZN4ULPN15TBClientAdaptor11connectFlowEyRKNSt3__15arrayIhLm16EEEjjRK17aon_net_if_configRK21aon_net_flow_config_stPKc_block_invoke
+ ____ZN4ULPN15TBClientAdaptor13toTLSMetadataERK27aonnetworking_tlsmetadata_sR22aon_net_tls_metadata_s_block_invoke
+ ____ZN4ULPN15TBClientAdaptor13updatePathMTUEjt_block_invoke
+ ____ZN4ULPN15TBClientAdaptor14disconnectFlowEjN6AONNet14DisconnectModeE_block_invoke
+ ____ZN4ULPN15TBClientAdaptor15toTBALPNStringsERA3_A33_KcmR28aonnetworking_alpnstring_v_s_block_invoke
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke.3
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke_2
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke_2.6
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke_3
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke_3.10
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke_4
+ ___block_descriptor_tmp.12
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.135.150
+ ___block_descriptor_tmp.136
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.14
+ ___block_descriptor_tmp.16.146
+ ___block_descriptor_tmp.17
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.2
+ ___block_descriptor_tmp.20.156
+ ___block_descriptor_tmp.21
+ ___block_descriptor_tmp.5
+ ___block_descriptor_tmp.7
+ ___block_descriptor_tmp.9
+ ___block_literal_global.26
+ ___block_literal_global.34
+ _aon_flow_config_copy
+ _aon_flow_config_create_quic
+ _aon_flow_config_create_tls
+ _aon_flow_config_get_flow_type
+ _aon_flow_config_get_ip_config
+ _aon_flow_config_get_quic_config
+ _aon_flow_config_get_tcp_config
+ _aon_flow_config_get_tls_handshake_config
+ _aon_flow_config_get_udp_config
+ _aon_flow_config_init
+ _aon_flow_config_is_valid
+ _aon_if_config_get_interface_mtu
+ _aon_if_config_get_interface_name
+ _aon_if_config_get_interface_type
+ _aon_if_config_get_local_mac
+ _aon_if_config_get_remote_mac
+ _aon_if_config_is_valid
+ _aon_if_config_set_interface_mtu
+ _aon_if_config_set_interface_name
+ _aon_if_config_set_interface_type
+ _aon_if_config_set_local_mac
+ _aon_if_config_set_remote_mac
+ _aon_ip_config_get_type
+ _aon_ip_config_is_valid
+ _aon_ip_config_set_ipv4_addresses
+ _aon_ip_config_set_ipv6_addresses
+ _aon_ip_config_set_path_mtu
+ _aon_net_connect_flow_with_ring_id
+ _aon_quic_config_get_idle_timeout
+ _aon_quic_config_get_ignore_path_errors
+ _aon_quic_config_get_probe_simultaneously
+ _aon_quic_config_get_source_connection_id_length
+ _aon_quic_config_set_idle_timeout
+ _aon_quic_config_set_ignore_path_errors
+ _aon_quic_config_set_probe_simultaneously
+ _aon_quic_config_set_source_connection_id_length
+ _aon_tcp_config_get_ports
+ _aon_tcp_config_set_ports
+ _aon_tls_handshake_config_add_alpn
+ _aon_tls_handshake_config_clear_alpns
+ _aon_tls_handshake_config_get_alpn_at_index
+ _aon_tls_handshake_config_get_alpn_count
+ _aon_tls_handshake_config_psk_set_psk
+ _aon_tls_handshake_config_rpk_get_local_private_key
+ _aon_tls_handshake_config_rpk_get_local_private_key_len
+ _aon_tls_handshake_config_rpk_get_local_public_key
+ _aon_tls_handshake_config_rpk_get_local_public_key_len
+ _aon_tls_handshake_config_rpk_get_peer_authentication
+ _aon_tls_handshake_config_rpk_get_remote_public_key
+ _aon_tls_handshake_config_rpk_get_remote_public_key_len
+ _aon_tls_handshake_config_rpk_set_identity
+ _aon_tls_handshake_config_rpk_set_peer_authentication
+ _aon_tls_handshake_config_rpk_set_remote_public_key
+ _aon_udp_config_get_ports
+ _aon_udp_config_set_ports
+ _aonnetworking_alpnstring__v_visit
+ _aonnetworking_ipflow__raw_encode
+ _aonnetworking_networkingerrorcode__decode
+ _aonnetworking_tlshandshakeconfig__raw_encode
+ _ncprivkey8__v_count
+ _ncpubkey8__v_count
+ _ncpubkey8__v_raw_encode
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _shmem_close
+ _shmem_map_memory
+ _shmem_open
+ _shmem_unmap_memory
+ _tb_message_raw_decode_u8
+ _tb_message_raw_encode_bool
- GCC_except_table29
- GCC_except_table37
- GCC_except_table40
- GCC_except_table45
- GCC_except_table47
- GCC_except_table49
- GCC_except_table56
- GCC_except_table58
- _OBJC_CLASS_$_SDRDiagnosticReporter
- __ZZL27trigger_abc_for_buffer_lossvE27symptom_diagnostic_reporter
- __ZZZ20aon_net_service_initEUb_E49debug_detected_buffer_leak_in_previous_completion
- ____ZL27trigger_abc_for_buffer_lossv_block_invoke
- ___aon_net_connect_flow_with_telemetry_slot_block_invoke
- ___aon_net_disconnect_flow_block_invoke
- ___aon_net_path_update_block_invoke
- ___aon_net_remove_flow_block_invoke
- ___aon_net_service_init_block_invoke.18
- ___aon_net_service_init_block_invoke.19
- ___aon_net_service_init_block_invoke.20
- ___aon_net_service_init_block_invoke.5
- ___aon_net_service_init_block_invoke_2
- ___aon_net_service_init_block_invoke_3
- ___aon_net_service_init_block_invoke_4
- ___aon_net_service_init_block_invoke_5
- ___block_descriptor_32_e22_v16?0"NSDictionary"8l
- ___block_descriptor_40_e11_v16?0I8i12l
- ___block_descriptor_40_e11_v20?0Q8C16l
- ___block_descriptor_40_e212_v20?0I8r^{aonnetworking_pskconfig_s=S{ncpsk8_v_s=C(?={?=*Q?}{?=*QQ}{?=^{tb_message_s}QQQ})}{ncpskid8_v_s=C(?={?=*Q?}{?=*QQ}{?=^{tb_message_s}QQQ})}{aonnetworking_seconds_s=I}{aonnetworking_milliseconds_s=I}}12l
- ___block_descriptor_40_e297_v20?0I8r^{aonnetworking_flowmetadata_s=Q(?={?={aonnetworking_tcpmetadata_s={aonnetworking_milliseconds_s=I}}{aonnetworking_tlsmetadata_s={aonnetworking_alpnstring__opt_s=B{aonnetworking_alpnstring_s={ncalpn8_v_s=C(?={?=*Q?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}s{aonnetworking_milliseconds_s=I}}})}12l
- ___block_descriptor_40_ea8_32r_e8_v12?0i8lr32l8
- ___block_descriptor_48_e15_v20?0[64S]8I16l
- ___block_descriptor_48_e21_v28?0I8[64S]12I20S24l
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.126
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.128
- ___block_descriptor_tmp.130
- ___block_literal_global.23
- ___block_literal_global.44
- ___block_literal_global.49
- _aonnetworking_networkingservice__init
- _aonnetworking_networkingservice_connectflow
- _aonnetworking_networkingservice_disconnectflow
- _aonnetworking_networkingservicecallback__server_start_owned
- _memset
- _objc_alloc
- _objc_autoreleaseReturnValue
- _objc_msgSend
- _objc_msgSend$initWithQueue:
- _objc_msgSend$signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:
- _objc_msgSend$snapshotWithSignature:duration:event:payload:reply:
- _objc_release_x22
- _objc_release_x23
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retainBlock
- _objc_retain_x19
CStrings:
+ "%s: ALPN string too long"
+ "%s: IP configuration not set"
+ "%s: MTU must not be 0"
+ "%s: Set remote MAC address for WiFi interface"
+ "%s: TLS handshake type not set"
+ "%s: flow_config is NULL"
+ "%s: interface name too long"
+ "%s: interface type not set"
+ "%s: invalid IPv4 addresses"
+ "%s: invalid IPv6 addresses"
+ "%s: invalid interface type %llu"
+ "%s: invalid parameters"
+ "%s: invalid port (local=%u, remote=%u)"
+ "%s: invalid quic_config"
+ "%s: invalid rpk_config"
+ "%s: invalid tcp_config"
+ "%s: invalid tls_handshake_config"
+ "%s: invalid udp_config"
+ "%s: local MAC address only supported for WiFi interfaces"
+ "%s: maximum ALPN count reached"
+ "%s: remote MAC address only supported for WiFi interfaces"
+ "%s: source connection ID length %u exceeds maximum (%u)"
+ "%s:%d TBClientAdaptor dir %d ret %d"
+ "%s:%d disconnect() Invalid mode=%u flowId=0x%x"
+ "%s:%d init() Invalid lengths, pskLen %zu pskIdLen %zu"
+ "%s:%d toFlowMetadata() Invalid tag=%llu"
+ "%s:%d toTBALPNStrings() Invalid ALPN at index=%zu len=%zu"
+ "%s:%d toTBALPNStrings() Invalid ALPN, count=%zu"
+ "%s:%d toTBFlowConfig() Invalid flow type, type %llu"
+ "%s:%d toTBIPConfig() Invalid ipType=%llu"
+ "%s:%d toTBIfConfig() Invalid ifType=%llu"
+ "%s:%d toTBPSKHandshakeConfig() Invalid length, pskLen=%zu pskIdLen=%zu"
+ "%s:%d toTBQUICFlowConfig() QUIC flows only support RPK handshake type, type %llu"
+ "%s:%d toTBRPKHandshakeConfig() Invalid length, localPublicKeyLen=%zu localPrivateKeyLen=%zu remotePublicKeyLen=%zu"
+ "%s:%d toTBTLSFlowConfig() Invalid TLS handshake type, type %llu"
+ "%s:%d toTLSMetadata() Invalid ALPN"
+ "%s:%d toTLSMetadata() Invalid ALPN len=%zu"
+ "AFKSharedMemoryRegionBase"
+ "TBClientAdaptor client init failed[%u] for client[%s]<->server[%s]"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCPRIVKEY8 (aka. UInt8)]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCPRIVKEY8 (aka. UInt8)]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCPUBKEY8 (aka. UInt8)]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[AONNetworking.NCPUBKEY8 (aka. UInt8)]` metadata: 0x%x (%s:%d)\n"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "aon net rx completion doorbell failed with status %d"
+ "aon net tx submission doorbell failed with status %d"
+ "aon_flow_config_copy"
+ "aon_flow_config_init"
+ "aon_if_config_get_local_mac"
+ "aon_if_config_get_remote_mac"
+ "aon_if_config_set_interface_mtu"
+ "aon_if_config_set_interface_name"
+ "aon_if_config_set_interface_type"
+ "aon_if_config_set_local_mac"
+ "aon_if_config_set_remote_mac"
+ "aon_ip_config_set_ipv4_addresses"
+ "aon_ip_config_set_ipv6_addresses"
+ "aon_ip_config_set_path_mtu"
+ "aon_net_connect_flow_with_ring_id"
+ "aon_net_submit_buffers"
+ "aon_quic_config_set_idle_timeout"
+ "aon_quic_config_set_ignore_path_errors"
+ "aon_quic_config_set_probe_simultaneously"
+ "aon_quic_config_set_source_connection_id_length"
+ "aon_tcp_config_set_ports"
+ "aon_tls_handshake_config_add_alpn"
+ "aon_tls_handshake_config_clear_alpns"
+ "aon_tls_handshake_config_psk_set_psk"
+ "aon_tls_handshake_config_rpk_set_identity"
+ "aon_tls_handshake_config_rpk_set_peer_authentication"
+ "aon_tls_handshake_config_rpk_set_remote_public_key"
+ "aon_udp_config_set_ports"
+ "client->tb_client_adaptor"
+ "invalid callbacks"
+ "invalid psk"
+ "invalid psk id"
+ "rx shared memory buffer size is invalid"
+ "rx shared memory name is invalid"
+ "rx shared memory ring count is invalid"
+ "tightbeam setup via TBClientAdaptor %s<->%s completed"
+ "tx shared memory buffer size is invalid"
+ "tx shared memory name is invalid"
+ "tx shared memory ring count is invalid"
+ "v24@?0[16C]8I16i20"
+ "v32@?0[16C]8I16I20r^{aonnetworking_flowmetadata_s=Q(?={?={aonnetworking_tcpmetadata_s={aonnetworking_milliseconds_s=I}}{aonnetworking_tlsmetadata_s={aonnetworking_alpnstring__opt_s=B{aonnetworking_alpnstring_s={ncalpn8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}s{aonnetworking_milliseconds_s=I}}}{?={aonnetworking_quicmetadata_s={aonnetworking_milliseconds_s=I}}{aonnetworking_tlsmetadata_s={aonnetworking_alpnstring__opt_s=B{aonnetworking_alpnstring_s={ncalpn8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}s{aonnetworking_milliseconds_s=I}}})}24"
- "AFKSharedMemoryRegion"
- "Channel"
- "Failed to allocate memory for PSK"
- "Failed to allocate memory for PSK ID"
- "Failed to send snapshot to Symptoms"
- "Invalid ALPN at index %zu"
- "Invalid PSK ID size: %zu"
- "Invalid PSK size: %zu"
- "Invalid psk id info"
- "Invalid psk info"
- "Leak"
- "Successfully sent snapshot to Symptoms"
- "ULPN"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[64c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "aon net disconnect flow failed with error %d"
- "aon net networking path update failed with error %d"
- "aon net remove flow failed with error %d"
- "aon net rx completion doorbell failed with error %d"
- "aon net tx submission doorbell failed with error %d"
- "aon networking service initialization failed[%u] for client[%s]<->server[%s]"
- "aon_net_connect_flow_with_telemetry_slot"
- "aon_net_service_init_block_invoke"
- "apsd"
- "connect flow failed with error %d"
- "failed to setup security layer"
- "flow_config->values.tls_config.tls_handshake_config.values.psk.alpn_count <= AON_NET_MAX_ALPNS"
- "got response from diagnosticReporter %@"
- "initWithQueue:"
- "invalid TLS handshake type %llu"
- "invalid flow type %llu"
- "invalid if type %llu"
- "invalid ip family %llu"
- "rx_attr"
- "shared memory buffer size is invalid"
- "shared memory name is invalid"
- "shared memory ring count is invalid"
- "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
- "snapshotWithSignature:duration:event:payload:reply:"
- "tb_flow_metadata && tb_flow_metadata->tag == AONNETWORKING_FLOWMETADATA__TLS"
- "tightbeam setup %s<->%s completed"
- "tx_attr"
- "v16@?0@\"NSDictionary\"8"
- "v16@?0I8i12"
- "v20@?0I8r^{aonnetworking_flowmetadata_s=Q(?={?={aonnetworking_tcpmetadata_s={aonnetworking_milliseconds_s=I}}{aonnetworking_tlsmetadata_s={aonnetworking_alpnstring__opt_s=B{aonnetworking_alpnstring_s={ncalpn8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}s{aonnetworking_milliseconds_s=I}}})}12"

```
