## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2881.120.11.0.0
-  __TEXT.__text: 0x107760
-  __TEXT.__auth_stubs: 0x2f00
-  __TEXT.__objc_stubs: 0x2020
+3066.0.0.502.1
+  __TEXT.__text: 0x108410
+  __TEXT.__auth_stubs: 0x2fa0
+  __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x694
-  __TEXT.__const: 0x1170
-  __TEXT.__cstring: 0x179bd
-  __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__oslogstring: 0x1f627
-  __TEXT.__objc_classname: 0x649
-  __TEXT.__objc_methname: 0x1db6
+  __TEXT.__cstring: 0x17912
+  __TEXT.__const: 0x14bc
+  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__oslogstring: 0x20d66
+  __TEXT.__objc_classname: 0x646
+  __TEXT.__objc_methname: 0x1e32
   __TEXT.__objc_methtype: 0x64d
-  __TEXT.__unwind_info: 0x16a0
-  __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x1790
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x6440
-  __DATA_CONST.__cfstring: 0x11a0
+  __TEXT.__unwind_info: 0x16d0
+  __TEXT.__eh_frame: 0x7c
+  __DATA_CONST.__const: 0x62c8
+  __DATA_CONST.__cfstring: 0x1200
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__auth_got: 0x17e0
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__auth_ptr: 0x78
   __DATA.__objc_const: 0x4188
-  __DATA.__objc_selrefs: 0x9c0
+  __DATA.__objc_selrefs: 0x9e8
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x1270
-  __DATA.__data: 0x4328
-  __DATA.__bss: 0x16df8
+  __DATA.__data: 0x4330
+  __DATA.__bss: 0x16e50
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/DeviceToDeviceManager
+  - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/StatusKit.framework/StatusKit
   - /System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter
+  - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: E2392592-ADE6-339F-B9B3-0CD9B6E773F8
-  Functions: 1845
-  Symbols:   4611
-  CStrings:  4914
+  UUID: C498466C-E8C0-3846-98BA-CD68A923A72C
+  Functions: 1869
+  Symbols:   4641
+  CStrings:  4910
 
Symbols:
+ FreeARElemCallback.2688
+ GCC_except_table123
+ GCC_except_table1250
+ GCC_except_table1256
+ GCC_except_table127
+ GCC_except_table1418
+ GCC_except_table1601
+ GCC_except_table1832
+ GCC_except_table488
+ _AWDLTimeoutNotificationHandler
+ _DNSRecordDataToStringEx2.kBase32ExtendedHex
+ _DecrementAutoTargetServices
+ _DowngradeAuthRecordAWDLInclusion
+ _OBJC_CLASS_$_AWDLServiceDiscoveryManager
+ _OBJC_CLASS_$_LockdownModeManager
+ _TimingDefenseEnabled
+ __36-[UAPresenceManager assertPresence:]_block_invoke.92
+ __44-[UAPresenceManager updateCacheFromPresence]_block_invoke.118
+ __44-[UAPresenceManager updateCacheFromPresence]_block_invoke_2.119
+ __AppendHexString
+ __Block_byref_object_copy_.957
+ __Block_byref_object_dispose_.958
+ __DNSRecordDataToStringEx2
+ ____dx_gai_request_commit_result_block_invoke
+ ____dx_schedule_delayed_results_timer_block_invoke
+ ____mdns_awdl_log_block_invoke
+ ____mdns_awdl_manager_block_invoke
+ ____mdns_clock_log_block_invoke
+ ____mdns_siphash_get_per_process_key_block_invoke
+ ___block_descriptor_60_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___dnssd_svcb_has_ohttp_block_invoke
+ ___http_task_fetch_ohttp_config_block_invoke
+ ___http_task_fetch_ohttp_config_block_invoke_2
+ ___mdns_dispatch_data_memcpy_block_invoke
+ ___mdns_dns_service_manager_probe_discovered_service_block_invoke.238
+ ___mdns_dns_service_manager_probe_discovered_service_block_invoke_2.239
+ ___mdns_dns_service_manager_process_ddr_response_block_invoke.227
+ ___mdns_ne_dns_proxy_state_watch_fetch_manager_status_block_invoke.28
+ ___mdns_resolver_set_up_server_path_evaluator_block_invoke.47
+ ___mdns_server_log_block_invoke.4439
+ ___mdns_tls_resolver_create_stream_params_block_invoke.14
+ ___mdns_url_session_send_block_invoke.82
+ ___mdns_url_session_send_block_invoke.84
+ ___mdns_url_session_send_block_invoke.90
+ ___unicast_assist_hash_for_interface_block_invoke.335
+ __block_descriptor_tmp.1.6363
+ __block_descriptor_tmp.10.4422
+ __block_descriptor_tmp.10.6189
+ __block_descriptor_tmp.100
+ __block_descriptor_tmp.101.4921
+ __block_descriptor_tmp.102.4944
+ __block_descriptor_tmp.1027
+ __block_descriptor_tmp.104.1001
+ __block_descriptor_tmp.11.6393
+ __block_descriptor_tmp.11.6759
+ __block_descriptor_tmp.11.894
+ __block_descriptor_tmp.110
+ __block_descriptor_tmp.12.6196
+ __block_descriptor_tmp.12.6756
+ __block_descriptor_tmp.12.895
+ __block_descriptor_tmp.120.5012
+ __block_descriptor_tmp.121.4807
+ __block_descriptor_tmp.13.4438
+ __block_descriptor_tmp.13.6197
+ __block_descriptor_tmp.133.3728
+ __block_descriptor_tmp.14.1105
+ __block_descriptor_tmp.14.3325
+ __block_descriptor_tmp.14.908
+ __block_descriptor_tmp.1492
+ __block_descriptor_tmp.15.6151
+ __block_descriptor_tmp.1577
+ __block_descriptor_tmp.16.4826
+ __block_descriptor_tmp.16.6402
+ __block_descriptor_tmp.16.914
+ __block_descriptor_tmp.17.1106
+ __block_descriptor_tmp.17.4222
+ __block_descriptor_tmp.17.6152
+ __block_descriptor_tmp.17.6750
+ __block_descriptor_tmp.171
+ __block_descriptor_tmp.18.3333
+ __block_descriptor_tmp.18.4362
+ __block_descriptor_tmp.18.4410
+ __block_descriptor_tmp.18.4823
+ __block_descriptor_tmp.18.6158
+ __block_descriptor_tmp.18.6763
+ __block_descriptor_tmp.18.937
+ __block_descriptor_tmp.184
+ __block_descriptor_tmp.19.6146
+ __block_descriptor_tmp.19.938
+ __block_descriptor_tmp.2.4296
+ __block_descriptor_tmp.2.7071
+ __block_descriptor_tmp.2.7494
+ __block_descriptor_tmp.20
+ __block_descriptor_tmp.20.1032
+ __block_descriptor_tmp.20.4822
+ __block_descriptor_tmp.20.6191
+ __block_descriptor_tmp.20.7042
+ __block_descriptor_tmp.201
+ __block_descriptor_tmp.207
+ __block_descriptor_tmp.21.4365
+ __block_descriptor_tmp.21.7057
+ __block_descriptor_tmp.216.945
+ __block_descriptor_tmp.22.1587
+ __block_descriptor_tmp.22.3335
+ __block_descriptor_tmp.22.4425
+ __block_descriptor_tmp.22.6192
+ __block_descriptor_tmp.220
+ __block_descriptor_tmp.220.5931
+ __block_descriptor_tmp.224.5928
+ __block_descriptor_tmp.226
+ __block_descriptor_tmp.23.1594
+ __block_descriptor_tmp.23.4805
+ __block_descriptor_tmp.23.7043
+ __block_descriptor_tmp.231
+ __block_descriptor_tmp.231.3052
+ __block_descriptor_tmp.2343
+ __block_descriptor_tmp.235
+ __block_descriptor_tmp.24.1595
+ __block_descriptor_tmp.24.3366
+ __block_descriptor_tmp.24.6187
+ __block_descriptor_tmp.242
+ __block_descriptor_tmp.243
+ __block_descriptor_tmp.2450
+ __block_descriptor_tmp.25.1103
+ __block_descriptor_tmp.25.3390
+ __block_descriptor_tmp.25.4800
+ __block_descriptor_tmp.25.7044
+ __block_descriptor_tmp.252
+ __block_descriptor_tmp.253
+ __block_descriptor_tmp.254
+ __block_descriptor_tmp.254.3039
+ __block_descriptor_tmp.258
+ __block_descriptor_tmp.258.3034
+ __block_descriptor_tmp.26.1596
+ __block_descriptor_tmp.26.6184
+ __block_descriptor_tmp.27.1597
+ __block_descriptor_tmp.27.6181
+ __block_descriptor_tmp.27.7049
+ __block_descriptor_tmp.27.997
+ __block_descriptor_tmp.2701
+ __block_descriptor_tmp.273
+ __block_descriptor_tmp.277
+ __block_descriptor_tmp.28.5029
+ __block_descriptor_tmp.28.6179
+ __block_descriptor_tmp.28.7050
+ __block_descriptor_tmp.29.1599
+ __block_descriptor_tmp.29.3395
+ __block_descriptor_tmp.29.4898
+ __block_descriptor_tmp.29.6142
+ __block_descriptor_tmp.29.7051
+ __block_descriptor_tmp.299
+ __block_descriptor_tmp.3.1039
+ __block_descriptor_tmp.3.1581
+ __block_descriptor_tmp.3.2344
+ __block_descriptor_tmp.3.4299
+ __block_descriptor_tmp.3.6205
+ __block_descriptor_tmp.3.6366
+ __block_descriptor_tmp.3.6396
+ __block_descriptor_tmp.3.6752
+ __block_descriptor_tmp.3.7659
+ __block_descriptor_tmp.30.4897
+ __block_descriptor_tmp.30.6170
+ __block_descriptor_tmp.30.7035
+ __block_descriptor_tmp.303
+ __block_descriptor_tmp.305
+ __block_descriptor_tmp.309
+ __block_descriptor_tmp.31.3407
+ __block_descriptor_tmp.31.4817
+ __block_descriptor_tmp.32.4426
+ __block_descriptor_tmp.32.6172
+ __block_descriptor_tmp.3252
+ __block_descriptor_tmp.33.1601
+ __block_descriptor_tmp.33.7041
+ __block_descriptor_tmp.34.1041
+ __block_descriptor_tmp.34.1610
+ __block_descriptor_tmp.34.3276
+ __block_descriptor_tmp.34.7029
+ __block_descriptor_tmp.35.1609
+ __block_descriptor_tmp.35.7058
+ __block_descriptor_tmp.3578
+ __block_descriptor_tmp.3661
+ __block_descriptor_tmp.38.1085
+ __block_descriptor_tmp.38.3277
+ __block_descriptor_tmp.384
+ __block_descriptor_tmp.39.1092
+ __block_descriptor_tmp.39.6121
+ __block_descriptor_tmp.4.4300
+ __block_descriptor_tmp.4.4412
+ __block_descriptor_tmp.4.5028
+ __block_descriptor_tmp.4.6206
+ __block_descriptor_tmp.4.6370
+ __block_descriptor_tmp.40.1098
+ __block_descriptor_tmp.40.1603
+ __block_descriptor_tmp.41.1604
+ __block_descriptor_tmp.419
+ __block_descriptor_tmp.42.3274
+ __block_descriptor_tmp.4224
+ __block_descriptor_tmp.4260
+ __block_descriptor_tmp.4291
+ __block_descriptor_tmp.43.4788
+ __block_descriptor_tmp.44.1089
+ __block_descriptor_tmp.4407
+ __block_descriptor_tmp.46.4871
+ __block_descriptor_tmp.47.3259
+ __block_descriptor_tmp.47.5558
+ __block_descriptor_tmp.48.3326
+ __block_descriptor_tmp.48.4872
+ __block_descriptor_tmp.486
+ __block_descriptor_tmp.4868
+ __block_descriptor_tmp.493
+ __block_descriptor_tmp.497
+ __block_descriptor_tmp.5.2355
+ __block_descriptor_tmp.5.4301
+ __block_descriptor_tmp.5.4413
+ __block_descriptor_tmp.5.5034
+ __block_descriptor_tmp.5.6207
+ __block_descriptor_tmp.50.4905
+ __block_descriptor_tmp.502
+ __block_descriptor_tmp.506
+ __block_descriptor_tmp.51.3270
+ __block_descriptor_tmp.51.4900
+ __block_descriptor_tmp.510
+ __block_descriptor_tmp.5306
+ __block_descriptor_tmp.54.3268
+ __block_descriptor_tmp.55.1091
+ __block_descriptor_tmp.5546
+ __block_descriptor_tmp.566
+ __block_descriptor_tmp.58.1083
+ __block_descriptor_tmp.58.5005
+ __block_descriptor_tmp.59.3396
+ __block_descriptor_tmp.59.7559
+ __block_descriptor_tmp.5934
+ __block_descriptor_tmp.6.1036
+ __block_descriptor_tmp.6.1615
+ __block_descriptor_tmp.6.4273
+ __block_descriptor_tmp.6.4414
+ __block_descriptor_tmp.6.6374
+ __block_descriptor_tmp.6.7498
+ __block_descriptor_tmp.6.880
+ __block_descriptor_tmp.60.3399
+ __block_descriptor_tmp.60.5003
+ __block_descriptor_tmp.61.1080
+ __block_descriptor_tmp.61.3397
+ __block_descriptor_tmp.62.3410
+ __block_descriptor_tmp.62.6166
+ __block_descriptor_tmp.63.7552
+ __block_descriptor_tmp.6359
+ __block_descriptor_tmp.6389
+ __block_descriptor_tmp.64.1048
+ __block_descriptor_tmp.6451
+ __block_descriptor_tmp.646
+ __block_descriptor_tmp.6638
+ __block_descriptor_tmp.6744
+ __block_descriptor_tmp.69.1053
+ __block_descriptor_tmp.6978
+ __block_descriptor_tmp.7.4258
+ __block_descriptor_tmp.7.4417
+ __block_descriptor_tmp.7.6209
+ __block_descriptor_tmp.7.6377
+ __block_descriptor_tmp.7.6400
+ __block_descriptor_tmp.7.7007
+ __block_descriptor_tmp.7.882
+ __block_descriptor_tmp.70.1054
+ __block_descriptor_tmp.701
+ __block_descriptor_tmp.7072
+ __block_descriptor_tmp.7106
+ __block_descriptor_tmp.72
+ __block_descriptor_tmp.7279
+ __block_descriptor_tmp.73.4973
+ __block_descriptor_tmp.740
+ __block_descriptor_tmp.7441
+ __block_descriptor_tmp.7491
+ __block_descriptor_tmp.7655
+ __block_descriptor_tmp.77.4954
+ __block_descriptor_tmp.7840
+ __block_descriptor_tmp.7875
+ __block_descriptor_tmp.79.7501
+ __block_descriptor_tmp.8.4256
+ __block_descriptor_tmp.8.6380
+ __block_descriptor_tmp.8.6745
+ __block_descriptor_tmp.8.889
+ __block_descriptor_tmp.81
+ __block_descriptor_tmp.81.7531
+ __block_descriptor_tmp.87.7514
+ __block_descriptor_tmp.89
+ __block_descriptor_tmp.9.4263
+ __block_descriptor_tmp.94.4876
+ __block_descriptor_tmp.95
+ __block_descriptor_tmp.99
+ __block_literal_global.1025
+ __block_literal_global.117
+ __block_literal_global.123
+ __block_literal_global.1479
+ __block_literal_global.15.4419
+ __block_literal_global.15.7779
+ __block_literal_global.152
+ __block_literal_global.1572
+ __block_literal_global.162
+ __block_literal_global.198
+ __block_literal_global.20.4406
+ __block_literal_global.222
+ __block_literal_global.226
+ __block_literal_global.2271
+ __block_literal_global.2342
+ __block_literal_global.238
+ __block_literal_global.244
+ __block_literal_global.2444
+ __block_literal_global.256
+ __block_literal_global.256.3033
+ __block_literal_global.260
+ __block_literal_global.275
+ __block_literal_global.275.4715
+ __block_literal_global.278
+ __block_literal_global.3.3580
+ __block_literal_global.30
+ __block_literal_global.301
+ __block_literal_global.3047
+ __block_literal_global.305
+ __block_literal_global.307
+ __block_literal_global.322
+ __block_literal_global.33.4809
+ __block_literal_global.332
+ __block_literal_global.338
+ __block_literal_global.3388
+ __block_literal_global.3576
+ __block_literal_global.3692
+ __block_literal_global.4.7772
+ __block_literal_global.417
+ __block_literal_global.42
+ __block_literal_global.43.6692
+ __block_literal_global.4415
+ __block_literal_global.454
+ __block_literal_global.4670
+ __block_literal_global.488
+ __block_literal_global.495
+ __block_literal_global.499
+ __block_literal_global.5.6392
+ __block_literal_global.5.6747
+ __block_literal_global.5032
+ __block_literal_global.504
+ __block_literal_global.508
+ __block_literal_global.5545
+ __block_literal_global.5859
+ __block_literal_global.6144
+ __block_literal_global.6250
+ __block_literal_global.6387
+ __block_literal_global.642
+ __block_literal_global.6447
+ __block_literal_global.6631
+ __block_literal_global.6706
+ __block_literal_global.679
+ __block_literal_global.6976
+ __block_literal_global.7031
+ __block_literal_global.7276
+ __block_literal_global.736
+ __block_literal_global.7438
+ __block_literal_global.7489
+ __block_literal_global.7653
+ __block_literal_global.7768
+ __block_literal_global.7838
+ __block_literal_global.7873
+ __block_literal_global.8.1030
+ __block_literal_global.8.1586
+ __block_literal_global.8.2265
+ __block_literal_global.8.7496
+ __block_literal_global.9.6398
+ __block_literal_global.94
+ __dx_gai_request_commit_result
+ __dx_gai_request_process_answer
+ __dx_gai_request_triage_result
+ __dx_gai_request_update_failover_state
+ __dx_server_check_sessions
+ __mdns_awdl_create_service_name_string
+ __mdns_awdl_log
+ __mdns_awdl_manager
+ __mdns_dns_service_manager_register_discovered_service
+ __mdns_https_resolver_set_h3_support
+ __mdns_signed_append_domain_name_string_to_sb
+ __mdns_siphash_with_key_ex
+ __mdns_string_builder_append_ipv4_sockaddr
+ __mdns_string_builder_append_ipv6_sockaddr
+ __mdns_string_builder_append_private_string
+ __return_browse_request_error
+ __return_regservice_request_error
+ __return_resolve_request_error
+ _append_regrecord_entry_reply
+ _append_reply_with_timing_defense
+ _arc4random_buf
+ _deregister_record_entry
+ _dx_schedule_delayed_results_timer.s_scheduled_fire_time_ns
+ _dx_schedule_delayed_results_timer.s_timer
+ _external_start_advertising_helper
+ _external_stop_resolving_service
+ _g_awdl_service_discovery_manager_lock
+ _mDNSCoreReceiveNoUnicastAnswers
+ _mDNS_Init
+ _mdns_awdl_add_client
+ _mdns_awdl_log.s_log
+ _mdns_awdl_log.s_once
+ _mdns_awdl_manager.once
+ _mdns_awdl_manager.s_manager
+ _mdns_awdl_remove_client
+ _mdns_base64_encode_u32_unpadded
+ _mdns_clock_log.s_log
+ _mdns_clock_log.s_once
+ _mdns_clock_uptime_ns
+ _mdns_fd_set_nonblocking
+ _mdns_nw_create_dns_over_bytestream_protocol_options
+ _mdns_nw_parameters_add_dns_over_bytestream_framer
+ _mdns_parse_printable_ascii_run
+ _mdns_privacy_obfuscate_domain_name_str
+ _mdns_privacy_obfuscate_ipv4_address
+ _mdns_privacy_obfuscate_ipv6_address
+ _mdns_privacy_obfuscate_string
+ _mdns_server_log.s_log.4420
+ _mdns_server_log.s_once.4418
+ _mdns_siphash_domain_label_u32
+ _mdns_siphash_domain_name_str_u32
+ _mdns_siphash_domain_name_u32
+ _mdns_siphash_get_per_process_key.s_siphash_key
+ _mdns_siphash_get_per_process_key.s_siphash_key_once
+ _mdns_siphash_u32
+ _mdns_string_builder_append_escaped_ascii_string
+ _mdns_string_builder_append_sockaddr
+ _mdns_timing_defense_pick_delay_bucket
+ _notify_cancel
+ _notify_register_file_descriptor
+ _nw_ip_options_set_dscp_value
+ _nw_parameters_set_service_class
+ _nw_protocol_stack_copy_internet_protocol
+ _nw_resolver_config_get_h3_support
+ _nw_resolver_config_set_h3_support
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addAWDLDiscoveryClient:forService:error:
+ _objc_msgSend$enabled
+ _objc_msgSend$removeAWDLDiscoveryClient:forService:error:
+ _objc_msgSend$setAssumesHTTP3Capable:
+ _objc_msgSend$shared
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x10
+ _objc_retain_x4
+ _os_variant_allows_internal_security_policies
+ _unicast_assist_addr_update
+ g_nwi_state.4652
+ g_session_list.4424
+ mdns_base64_encode_u32_unpadded.base64_charset
+ mdns_timing_defense_pick_delay_bucket.bucket_history
+ mdns_timing_defense_pick_delay_bucket.bucket_history_count
+ mdns_timing_defense_pick_delay_bucket.bucket_history_next
- DNSRecordDataToStringEx.kBase32ExtendedHex
- FreeARElemCallback.2650
- GCC_except_table110
- GCC_except_table114
- GCC_except_table1220
- GCC_except_table1226
- GCC_except_table1394
- GCC_except_table1591
- GCC_except_table1812
- _DNSMessagePrintObfuscatedString
- _DNSMessageToString
- _DNSRecordDataToStringEx
- _DomainNameHashValue
- _GetCUSymAddr_DataBuffer_Append.sAddr
- _GetCUSymAddr_DataBuffer_Append.sOnce
- _GetCUSymAddr_DataBuffer_AppendF.sAddr
- _GetCUSymAddr_DataBuffer_AppendF.sOnce
- _GetCUSymAddr_DataBuffer_Detach.sAddr
- _GetCUSymAddr_DataBuffer_Detach.sOnce
- _GetCUSymAddr_DataBuffer_Free.sAddr
- _GetCUSymAddr_DataBuffer_Free.sOnce
- _GetCUSymAddr_DataBuffer_Init.sAddr
- _GetCUSymAddr_DataBuffer_Init.sOnce
- _GetCUSymAddr_SNPrintF.sAddr
- _GetCUSymAddr_SNPrintF.sOnce
- _OUTLINED_FUNCTION_0
- __36-[UAPresenceManager assertPresence:]_block_invoke.93
- __44-[UAPresenceManager updateCacheFromPresence]_block_invoke.119
- __44-[UAPresenceManager updateCacheFromPresence]_block_invoke_2.120
- __AppendDomainNameStringEx
- __AppendEscapedASCIIString
- __AppendIPAddress
- __AppendIPv4Address
- __AppendIPv6Address
- __Block_byref_object_copy_.923
- __Block_byref_object_dispose_.924
- __DNSMessagePrintObfuscatedIPAddress
- __NameIsPrivate
- ____GetCUSymAddr_DataBuffer_AppendF_block_invoke
- ____GetCUSymAddr_DataBuffer_Append_block_invoke
- ____GetCUSymAddr_DataBuffer_Detach_block_invoke
- ____GetCUSymAddr_DataBuffer_Free_block_invoke
- ____GetCUSymAddr_DataBuffer_Init_block_invoke
- ____GetCUSymAddr_SNPrintF_block_invoke
- ____dx_gai_request_append_cname_block_invoke
- ____dx_gai_request_append_result_block_invoke
- ____dx_gai_request_check_for_failover_restart_block_invoke
- ____dx_gai_request_copy_cname_update_block_invoke
- ____mdns_copy_dns_over_bytestream_framer_block_invoke
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6355
- ___mdns_dns_service_manager_probe_discovered_service_block_invoke.235
- ___mdns_dns_service_manager_probe_discovered_service_block_invoke_2.236
- ___mdns_ne_dns_proxy_state_watch_fetch_manager_status_block_invoke.29
- ___mdns_resolver_set_up_server_path_evaluator_block_invoke.67
- ___mdns_server_log_block_invoke.4367
- ___mdns_tls_resolver_create_stream_params_block_invoke.34
- ___mdns_url_session_send_block_invoke.102
- ___mdns_url_session_send_block_invoke.104
- ___mdns_url_session_send_block_invoke.110
- ___unicast_assist_hash_for_interface_block_invoke.337
- __block_descriptor_tmp.1.6323
- __block_descriptor_tmp.10.4350
- __block_descriptor_tmp.10.6153
- __block_descriptor_tmp.104
- __block_descriptor_tmp.107
- __block_descriptor_tmp.109
- __block_descriptor_tmp.11.6349
- __block_descriptor_tmp.11.6713
- __block_descriptor_tmp.11.862
- __block_descriptor_tmp.112
- __block_descriptor_tmp.114
- __block_descriptor_tmp.115
- __block_descriptor_tmp.12.6160
- __block_descriptor_tmp.12.6710
- __block_descriptor_tmp.12.863
- __block_descriptor_tmp.120.4859
- __block_descriptor_tmp.121.4852
- __block_descriptor_tmp.122.4876
- __block_descriptor_tmp.13.4366
- __block_descriptor_tmp.13.4752
- __block_descriptor_tmp.13.6161
- __block_descriptor_tmp.130.4806
- __block_descriptor_tmp.133.3670
- __block_descriptor_tmp.14.1068
- __block_descriptor_tmp.14.3277
- __block_descriptor_tmp.14.876
- __block_descriptor_tmp.140.4830
- __block_descriptor_tmp.141
- __block_descriptor_tmp.142
- __block_descriptor_tmp.1455
- __block_descriptor_tmp.148.948
- __block_descriptor_tmp.15.6115
- __block_descriptor_tmp.1540
- __block_descriptor_tmp.16.6360
- __block_descriptor_tmp.17.1069
- __block_descriptor_tmp.17.4150
- __block_descriptor_tmp.17.4756
- __block_descriptor_tmp.17.6116
- __block_descriptor_tmp.17.6704
- __block_descriptor_tmp.17.903
- __block_descriptor_tmp.179
- __block_descriptor_tmp.18.3285
- __block_descriptor_tmp.18.4290
- __block_descriptor_tmp.18.4338
- __block_descriptor_tmp.18.6122
- __block_descriptor_tmp.18.6717
- __block_descriptor_tmp.18.905
- __block_descriptor_tmp.188
- __block_descriptor_tmp.19.6110
- __block_descriptor_tmp.19.906
- __block_descriptor_tmp.2.4224
- __block_descriptor_tmp.2.7027
- __block_descriptor_tmp.2.7420
- __block_descriptor_tmp.20.6155
- __block_descriptor_tmp.20.6998
- __block_descriptor_tmp.20.907
- __block_descriptor_tmp.20.996
- __block_descriptor_tmp.208
- __block_descriptor_tmp.21.4293
- __block_descriptor_tmp.21.4749
- __block_descriptor_tmp.21.7013
- __block_descriptor_tmp.217
- __block_descriptor_tmp.218
- __block_descriptor_tmp.22.1550
- __block_descriptor_tmp.22.3287
- __block_descriptor_tmp.22.4353
- __block_descriptor_tmp.22.6156
- __block_descriptor_tmp.221
- __block_descriptor_tmp.222
- __block_descriptor_tmp.225
- __block_descriptor_tmp.227
- __block_descriptor_tmp.23.1557
- __block_descriptor_tmp.23.6999
- __block_descriptor_tmp.2308
- __block_descriptor_tmp.232
- __block_descriptor_tmp.233.5798
- __block_descriptor_tmp.238
- __block_descriptor_tmp.238.2995
- __block_descriptor_tmp.24.1558
- __block_descriptor_tmp.24.3316
- __block_descriptor_tmp.24.6151
- __block_descriptor_tmp.240
- __block_descriptor_tmp.2411
- __block_descriptor_tmp.244
- __block_descriptor_tmp.245
- __block_descriptor_tmp.248
- __block_descriptor_tmp.249.2792
- __block_descriptor_tmp.25.1066
- __block_descriptor_tmp.25.3340
- __block_descriptor_tmp.25.7000
- __block_descriptor_tmp.251.5881
- __block_descriptor_tmp.255
- __block_descriptor_tmp.255.5878
- __block_descriptor_tmp.259
- __block_descriptor_tmp.26.1559
- __block_descriptor_tmp.26.4746
- __block_descriptor_tmp.26.6148
- __block_descriptor_tmp.262
- __block_descriptor_tmp.263
- __block_descriptor_tmp.2663
- __block_descriptor_tmp.27.1560
- __block_descriptor_tmp.27.6145
- __block_descriptor_tmp.27.7005
- __block_descriptor_tmp.27.963
- __block_descriptor_tmp.278
- __block_descriptor_tmp.28.6143
- __block_descriptor_tmp.28.7006
- __block_descriptor_tmp.282
- __block_descriptor_tmp.29.1562
- __block_descriptor_tmp.29.3345
- __block_descriptor_tmp.29.6106
- __block_descriptor_tmp.29.7007
- __block_descriptor_tmp.3.1002
- __block_descriptor_tmp.3.1544
- __block_descriptor_tmp.3.2309
- __block_descriptor_tmp.3.4227
- __block_descriptor_tmp.3.6169
- __block_descriptor_tmp.3.6326
- __block_descriptor_tmp.3.6353
- __block_descriptor_tmp.3.6706
- __block_descriptor_tmp.3.7584
- __block_descriptor_tmp.30.6134
- __block_descriptor_tmp.30.6991
- __block_descriptor_tmp.304
- __block_descriptor_tmp.308
- __block_descriptor_tmp.31.3357
- __block_descriptor_tmp.310
- __block_descriptor_tmp.314
- __block_descriptor_tmp.32.4354
- __block_descriptor_tmp.32.6136
- __block_descriptor_tmp.3205
- __block_descriptor_tmp.33.1564
- __block_descriptor_tmp.33.6997
- __block_descriptor_tmp.34
- __block_descriptor_tmp.34.1573
- __block_descriptor_tmp.34.3228
- __block_descriptor_tmp.34.6985
- __block_descriptor_tmp.35.1572
- __block_descriptor_tmp.35.7014
- __block_descriptor_tmp.3524
- __block_descriptor_tmp.36.4761
- __block_descriptor_tmp.3603
- __block_descriptor_tmp.38.1048
- __block_descriptor_tmp.38.3229
- __block_descriptor_tmp.38.4758
- __block_descriptor_tmp.388
- __block_descriptor_tmp.388.2596
- __block_descriptor_tmp.39.1056
- __block_descriptor_tmp.39.6085
- __block_descriptor_tmp.4.4228
- __block_descriptor_tmp.4.4340
- __block_descriptor_tmp.4.4961
- __block_descriptor_tmp.4.6170
- __block_descriptor_tmp.4.6330
- __block_descriptor_tmp.40.1566
- __block_descriptor_tmp.40.4741
- __block_descriptor_tmp.41.1052
- __block_descriptor_tmp.41.1567
- __block_descriptor_tmp.4152
- __block_descriptor_tmp.4188
- __block_descriptor_tmp.42.3226
- __block_descriptor_tmp.4219
- __block_descriptor_tmp.43.4725
- __block_descriptor_tmp.4335
- __block_descriptor_tmp.45.4720
- __block_descriptor_tmp.47.3212
- __block_descriptor_tmp.47.5486
- __block_descriptor_tmp.48.3278
- __block_descriptor_tmp.48.4962
- __block_descriptor_tmp.4801
- __block_descriptor_tmp.484
- __block_descriptor_tmp.491
- __block_descriptor_tmp.495
- __block_descriptor_tmp.498
- __block_descriptor_tmp.5.2320
- __block_descriptor_tmp.5.4229
- __block_descriptor_tmp.5.4341
- __block_descriptor_tmp.5.4967
- __block_descriptor_tmp.5.6171
- __block_descriptor_tmp.50.4828
- __block_descriptor_tmp.504
- __block_descriptor_tmp.508
- __block_descriptor_tmp.51.1038
- __block_descriptor_tmp.51.3222
- __block_descriptor_tmp.51.4736
- __block_descriptor_tmp.52
- __block_descriptor_tmp.5239
- __block_descriptor_tmp.534
- __block_descriptor_tmp.5474
- __block_descriptor_tmp.55.1046
- __block_descriptor_tmp.57
- __block_descriptor_tmp.58.1054
- __block_descriptor_tmp.59.3346
- __block_descriptor_tmp.59.7484
- __block_descriptor_tmp.5906
- __block_descriptor_tmp.6.1578
- __block_descriptor_tmp.6.4201
- __block_descriptor_tmp.6.4342
- __block_descriptor_tmp.6.6334
- __block_descriptor_tmp.6.7424
- __block_descriptor_tmp.6.999
- __block_descriptor_tmp.60.3349
- __block_descriptor_tmp.61.1043
- __block_descriptor_tmp.61.3347
- __block_descriptor_tmp.611
- __block_descriptor_tmp.62.3360
- __block_descriptor_tmp.62.6130
- __block_descriptor_tmp.63.4707
- __block_descriptor_tmp.63.7477
- __block_descriptor_tmp.6319
- __block_descriptor_tmp.6345
- __block_descriptor_tmp.64.1010
- __block_descriptor_tmp.6405
- __block_descriptor_tmp.6592
- __block_descriptor_tmp.66
- __block_descriptor_tmp.6698
- __block_descriptor_tmp.68
- __block_descriptor_tmp.69.1015
- __block_descriptor_tmp.69.4839
- __block_descriptor_tmp.6934
- __block_descriptor_tmp.7.4186
- __block_descriptor_tmp.7.4345
- __block_descriptor_tmp.7.6173
- __block_descriptor_tmp.7.6337
- __block_descriptor_tmp.7.6358
- __block_descriptor_tmp.7.6963
- __block_descriptor_tmp.7.850
- __block_descriptor_tmp.70.1016
- __block_descriptor_tmp.70.4835
- __block_descriptor_tmp.702
- __block_descriptor_tmp.7028
- __block_descriptor_tmp.7062
- __block_descriptor_tmp.7214
- __block_descriptor_tmp.7417
- __block_descriptor_tmp.7580
- __block_descriptor_tmp.76.4939
- __block_descriptor_tmp.7788
- __block_descriptor_tmp.78
- __block_descriptor_tmp.79.7427
- __block_descriptor_tmp.8.157
- __block_descriptor_tmp.8.4184
- __block_descriptor_tmp.8.6699
- __block_descriptor_tmp.8.857
- __block_descriptor_tmp.80.4937
- __block_descriptor_tmp.81.7456
- __block_descriptor_tmp.81.846
- __block_descriptor_tmp.9.4191
- __block_descriptor_tmp.9.4744
- __block_descriptor_tmp.91.4911
- __block_descriptor_tmp.93.4909
- __block_descriptor_tmp.97
- __block_descriptor_tmp.992
- __block_literal_global.10
- __block_literal_global.11.4742
- __block_literal_global.118
- __block_literal_global.139.847
- __block_literal_global.144
- __block_literal_global.1442
- __block_literal_global.146
- __block_literal_global.15.4347
- __block_literal_global.15.4748
- __block_literal_global.15.7704
- __block_literal_global.1535
- __block_literal_global.176
- __block_literal_global.19.4754
- __block_literal_global.20.4334
- __block_literal_global.220
- __block_literal_global.2236
- __block_literal_global.224
- __block_literal_global.23
- __block_literal_global.2307
- __block_literal_global.235
- __block_literal_global.239
- __block_literal_global.240
- __block_literal_global.2405
- __block_literal_global.243
- __block_literal_global.247
- __block_literal_global.253
- __block_literal_global.253.5807
- __block_literal_global.257
- __block_literal_global.257.5810
- __block_literal_global.261
- __block_literal_global.264
- __block_literal_global.276
- __block_literal_global.279
- __block_literal_global.28
- __block_literal_global.280
- __block_literal_global.3002
- __block_literal_global.306
- __block_literal_global.306.4526
- __block_literal_global.312
- __block_literal_global.324
- __block_literal_global.3338
- __block_literal_global.336
- __block_literal_global.340
- __block_literal_global.3522
- __block_literal_global.3634
- __block_literal_global.390
- __block_literal_global.4.7697
- __block_literal_global.422
- __block_literal_global.43.6646
- __block_literal_global.4343
- __block_literal_global.4594
- __block_literal_global.486
- __block_literal_global.493
- __block_literal_global.4965
- __block_literal_global.497
- __block_literal_global.5.6348
- __block_literal_global.5.6701
- __block_literal_global.502
- __block_literal_global.506
- __block_literal_global.53.4728
- __block_literal_global.5473
- __block_literal_global.5724
- __block_literal_global.607
- __block_literal_global.6108
- __block_literal_global.6212
- __block_literal_global.6343
- __block_literal_global.6401
- __block_literal_global.643
- __block_literal_global.6585
- __block_literal_global.6660
- __block_literal_global.6932
- __block_literal_global.698
- __block_literal_global.6987
- __block_literal_global.7211
- __block_literal_global.7415
- __block_literal_global.7578
- __block_literal_global.7693
- __block_literal_global.7786
- __block_literal_global.8.1549
- __block_literal_global.8.2230
- __block_literal_global.8.7422
- __block_literal_global.9.6356
- __block_literal_global.95
- __block_literal_global.990
- __dx_gai_request_append_result
- __dx_gai_request_check_for_failover_restart
- __dx_gai_request_enqueue_result
- __isPlatformVersionAtLeast.cold.1
- __isPlatformVersionAtLeast.cold.2
- __mdns_add_dns_over_bytestream_framer
- __mdns_normal_resolver_kind_block_invoke
- __mdns_normal_resolver_kind_block_invoke_2
- __mdns_normal_resolver_kind_block_invoke_3
- __mdns_string_builder_append_domain_name_string
- _mdns_copy_dns_over_bytestream_framer.s_framer_def
- _mdns_copy_dns_over_bytestream_framer.s_once
- _mdns_powerlog_register_record_stop
- _mdns_server_log.s_log.4348
- _mdns_server_log.s_once.4346
- _mdns_string_builder_append_sockaddr_description
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _strtol
- _unicast_assist_addr_add
- _unicast_assist_addr_refresh
- g_nwi_state.4576
- g_session_list.4352
CStrings:
+ " %d%02d%02d%02d%02d%02d"
+ " %s%s"
+ " '"
+ "%*s"
+ "%s %s"
+ "%{public}s Conflicting mDNS -- waking %{sensitive, mdnsresponder:mac_addr}.6P %{mdns:mac_hash}u %{sensitive}s %{mdns:s_hash}u"
+ "%{public}s: LHS: (%d bytes) %{sensitive, mdnsresponder:hex_sequence}.*P %{mdns:hex_hash}u"
+ "%{public}s: RHS: (%d bytes) %{sensitive, mdnsresponder:hex_sequence}.*P %{mdns:hex_hash}u"
+ "'"
+ "*** Network Configuration Change ***  IPv6 address %{sensitive, network:in6_addr}.16P %{mdns:ipv6_hash}u TENTATIVE, will retry"
+ "<dn:%s>"
+ "<ipv4:%s>"
+ "<ipv6:%s>"
+ "<s:%s>"
+ "=\""
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
+ "AWDL Timeout"
+ "AWDLTimeoutNotificationHandler: Downgrading kDNSServiceFlagsIncludeAWDL questions and AuthRecords"
+ "AWDLTimeoutNotificationHandler: Handling AWDL client requests"
+ "AWDLTimeoutNotificationHandler: read() failed: %{mdns:err}ld"
+ "AWDLTimeoutNotificationInit: Failed to create notification file descriptor: %u"
+ "AWDLTimeoutNotificationInit: KQueueSet() failed: %{mdns:err}ld"
+ "AWDLTimeoutNotificationInit: Making socket non-blocking failed: %{mdns:err}ld"
+ "AddOrUpdateTSRForCacheGroup: %s TSR %{sensitive}s %{mdns:s_hash}u"
+ "AddOrUpdateTSRForCacheGroup: No cache record for new TSR %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "AddOrUpdateTSRForCacheGroup: tsrTimestamp[%d] out of range (%d) on TSR for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "AddTSRRDataToMessage: TSR can't be written -- name %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u hashkey %x"
+ "Added AWDL discovery client -- client: %{public}@, service name: %{public}@"
+ "Another representative of InterfaceID exists - ifid: %d, ifname: %{public}s, ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "Answer set counter not found for the cached record - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rrtype: %{mdns:rrtype}d."
+ "AnswerAllLocalQuestionsWithLocalAuthRecord ERROR m->CurrentQuestion already set: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{mdns:rrtype}d)"
+ "AnswerLocalQuestionWithLocalAuthRecord: *NOT* delivering %{public}s event for local record type %X %{sensitive}s %{mdns:s_hash}u"
+ "Attempt to put kDNSRecordTypeUnregistered %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "Attempt to register record with invalid name: %{sensitive}s %{mdns:s_hash}u"
+ "Attempt to register record with invalid rdata: %{sensitive}s %{mdns:s_hash}u"
+ "Automatic browsing domain changes - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, event: %{public}s, interface ID: %p%{public}s"
+ "Automatic browsing domain discovered via network - change: %{public}s, interface name: %{public}s, browsing domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "Automatic browsing domain is added - domain name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, uid: %u"
+ "Automatic browsing domain is removed - domain name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, uid: %u"
+ "B36@?0r^{?=i(?=(?=[16C][8S][4I])(?=[4C]I))}8^{mDNSInterfaceID_dummystruct=^v}16B24B28i32"
+ "B40@?0r^{dispatch_data_s=}8Q16r^v24Q32"
+ "Bad service type in %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u.%{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u%{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u Application protocol name must be underscore plus 1-15 characters. See <http://www.dns-sd.org/ServiceTypes.html>"
+ "Can't put more names into current message, will possibly put it into the next message - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s), remaining space: %ld"
+ "Can't put more rdata into current message, will possibly put it into the next message - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s), remaining space: %ld"
+ "CancelGetZoneData: Question %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s) ThisQInterval %d not -1"
+ "Cannot exit yet; Resource Record still exists: %{sensitive}s %{mdns:s_hash}u"
+ "Changed RRSet for %{sensitive}s %{mdns:s_hash}u"
+ "ClearInactiveInterfaces: Deleting %{public}s(%u) %{sensitive, mdnsresponder:mac_addr}.6P %{mdns:mac_hash}u InterfaceID %p(%p) %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u/%d Age %d -- primary: %{mdns:yesno}d"
+ "ClearInactiveInterfaces: Deregistering %{public}s(%u) %{sensitive, mdnsresponder:mac_addr}.6P %{mdns:mac_hash}u InterfaceID %p(%p), primary %p, %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u/%d -- flashing: %{mdns:yesno}d, occulting: %{mdns:yesno}d, primary: %{mdns:yesno}d"
+ "ClearInactiveInterfaces: Holding %{public}s(%u) %{sensitive, mdnsresponder:mac_addr}.6P %{mdns:mac_hash}u InterfaceID %p(%p) %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u/%d Age %d -- primary: %{mdns:yesno}d"
+ "CompleteDeregistration: called for Resource record %{sensitive}s %{mdns:s_hash}u"
+ "ConfigResolvers -- scope type: %{public, mdnsresponder:dns_scope_type}u, resolver[%d]: {domain: %{sensitive}s %{mdns:dn_hash}u, name server count: %d}"
+ "ConfigSearchDomains -- search domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "ConstructServiceName: %{public}s: %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u.%{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u%{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "ConstructServiceName: Service type with non-leading underscore %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "Correcting TTL from %4u to %4u from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%u for records %{sensitive}s %{mdns:s_hash}u"
+ "D2DBrowseListRelease - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, ref count: %u"
+ "D2DBrowseListRelease item not found in the list - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d"
+ "D2DBrowseListRetain - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, ref count: %u"
+ "DecrementAutoTargetServices: AutoTargetAWDLIncludedCount %u Record %{sensitive}s %{mdns:s_hash}u"
+ "DecrementAutoTargetServices: AutoTargetAWDLOnlyCount %u Record %{sensitive}s %{mdns:s_hash}u"
+ "DecrementAutoTargetServices: AutoTargetServices %u Record %{sensitive}s %{mdns:s_hash}u"
+ "DecrementAutoTargetServices: NumAllInterfaceRecords %u NumAllInterfaceQuestions %u %{sensitive}s %{mdns:s_hash}u"
+ "DecrementAutoTargetServices: called for RRLocalOnly() record: %{sensitive}s %{mdns:s_hash}u"
+ "Denial of existence record changes, purging the old negative record - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{public}s"
+ "Denial of existence record does not change, rescuing the old negative record - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{public}s"
+ "DeregLoop: %{public}s deregistration for %p %02X %{sensitive}s %{mdns:s_hash}u"
+ "Deregistering orphaned TSR - %{sensitive}s %{mdns:s_hash}u"
+ "DiscardDeregistrations ERROR m->CurrentRecord already set %{sensitive}s %{mdns:s_hash}u"
+ "Discovered local resolver configuration updated - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, result: %d"
+ "ERROR: deregister_record_entry, mDNS_Deregister: %d"
+ "Error: regrecord_callback: successful registration of orphaned record %{sensitive}s %{mdns:s_hash}u"
+ "Excessive name conflicts (%u) for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s); rate limiting in effect"
+ "Failed to add AWDL discovery client -- client: %{public}@, service: %{public}@, error: %{public}@"
+ "Failed to allocate and init AWDLServiceDiscoveryManager"
+ "Failed to create UTF-8 string from client name: %{public}s"
+ "Failed to create UTF-8 string from service type: %{public}s"
+ "Failed to extract service type from record name"
+ "Failed to find out a provable denial of existence NSEC set - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %u, NSEC count: %u, error: %{public}s"
+ "Failed to find out a provable denial of existence NSEC3 set - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %u, NSEC3 count: %u, error: %{public}s"
+ "Failed to remove AWDL discovery client -- client: %{public}@, service: %{public}@, error: %{public}@"
+ "Failed to set computer name -- name: %{sensitive}s %{mdns:dn_hash}u, error: %ld"
+ "Failed to set local hostname -- name: %{sensitive}s %{mdns:dn_hash}u, error: %ld"
+ "Fast flushing AWDL cache record -- age: %d ticks, expire: %d ticks, record: %{sensitive}s %{mdns:s_hash}u"
+ "FlushAddressCacheRecords: Purging Resourcerecord - record description: %{sensitive}s %{mdns:s_hash}u."
+ "FlushAllCacheRecords: Purging Resourcerecord - record description: %{sensitive}s %{mdns:s_hash}u."
+ "Found a matching entry in the CacheFlushRecords - new rrtype: %{mdns:rrtype}d, matched name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, description: %{sensitive}s %{mdns:s_hash}u"
+ "FreeARElemCallback: Have to cut %{sensitive}s %{mdns:s_hash}u"
+ "FreeD2DARElemCallback: Could not find in D2DRecords: %{sensitive}s %{mdns:s_hash}u"
+ "FreeD2DARElemCallback: Found in D2DRecords: %{sensitive}s %{mdns:s_hash}u"
+ "FreeEtcHosts: %{sensitive}s %{mdns:s_hash}u"
+ "GetAuthGroup: Already have AuthGroup for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "GetAuthGroup: Failed to allocate memory for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "GetAuthGroup: Not finding AuthGroup for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "GetAuthInfoForName_internal deleting expired key %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "GetLargeResourceRecord: SetRData failed for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "Ignoring attempt to re-add interface (%{public}s, %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u) already marked as existing"
+ "Ignoring conflict on interface %d with recently deregistered hostname record: %{sensitive}s %{mdns:s_hash}u"
+ "IncrementAutoTargetServices: AutoTargetAWDLIncludedCount %u Record %{sensitive}s %{mdns:s_hash}u"
+ "IncrementAutoTargetServices: AutoTargetAWDLOnlyCount %u Record %{sensitive}s %{mdns:s_hash}u"
+ "IncrementAutoTargetServices: AutoTargetServices %u Record %{sensitive}s %{mdns:s_hash}u"
+ "IncrementAutoTargetServices: NumAllInterfaceRecords %u NumAllInterfaceQuestions %u %{sensitive}s %{mdns:s_hash}u"
+ "IncrementAutoTargetServices: called for RRLocalOnly() record: %{sensitive}s %{mdns:s_hash}u"
+ "Initialized RRSet for %{sensitive}s %{mdns:s_hash}u"
+ "Interface already represented in list - ifid: %d, ifname: %{public}s, ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "Interface not represented in list; marking active and retriggering queries - ifid: %d, ifname: %{public}s, ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "Interface probe will be delayed - ifname: %{public}s, ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u, probe delay: %d"
+ "Invalid expiration time for the current DNSSEC validated record - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rr_type: %{mdns:rrtype}d"
+ "Invalid mDNSAddrType - domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, interface index: %u, mDNSAddrType: v%d."
+ "LNT MakeTCPConnection: bad address/port %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d"
+ "Last representative of InterfaceID deregistered; marking questions etc. dormant - ifid: %d, ifname: %{public}s, ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "Make validated RR expire soon - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rr_type: %{mdns:rrtype}d"
+ "MakeTCPConnection: connecting to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d"
+ "Making record answered by the current response as expired if it is not refreshed in the response - Q interface ID: %p, qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, RR interface ID: %p, RR description: %{sensitive}s %{mdns:s_hash}u."
+ "Marking resolver HTTP/3 support to: %{bool}d"
+ "NetWakeInterface: interface -- ifname: %{public}s, address: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u, supports Wake-On-Lan: %{mdns:yesno}d"
+ "No existing TSR for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "No target count to update for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "Planning to stop the %{public}s enumeration - domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, grace period: %ds."
+ "Pointer to message is NULL while filling resource record %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "ProbeRRMatchAndTSRCheck: Conflict with our ar %p rrtype: %{mdns:rrtype}d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u%{sensitive}s %{mdns:s_hash}u"
+ "ProbeRRMatchAndTSRCheck: pkt ar on interface  %p rrtype: %{mdns:rrtype}d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u%{sensitive}s %{mdns:s_hash}u"
+ "ProcessQuery - deregistering %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u type %{public}s on interface id: %p due to TSR conflict"
+ "ProcessQuery: Preparing unicast assist query (max unanswered) - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{mdns:rrtype}d qhash %{sensitive}x"
+ "Purging cached TSR record that matches orphaned TSR -- %{sensitive}s %{mdns:s_hash}u"
+ "Question not found in the active list - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{public}s."
+ "Received Goodbye packet for cached record -- name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, last time received: %{public, timeval}.*P, interface index: %u, source address: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u, name hash if PTR: %{public, mdns:dn_hash}u"
+ "Received positive DNSKEY or DS RRSet without RRSIG, malformed - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d."
+ "ReconfirmAntecedents: Reconfirming (depth=%d, InterfaceID=%p, name_hash=%{public, mdns:dn_hash}u, target_name_hash=%{public, mdns:dn_hash}u) %{sensitive}s %{mdns:s_hash}u"
+ "ReleaseCacheRecord: ERROR!! cg NULL for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "RemoveAuthRecord: ERROR!! AuthGroup not found for %{sensitive}s %{mdns:s_hash}u"
+ "RemoveAuthRecord: removing auth record %{sensitive}s %{mdns:s_hash}u from table"
+ "Removed AWDL discovery client -- client: %{public}@, service name: %{public}@"
+ "Removing cached peer record -- peer address: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d"
+ "Removing record(s) -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u, collectively: %{mdns:yesno}d"
+ "Rescuing DNSSEC validated record - name: %{public, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, old original ttl: %u, new original ttl: %u, new actual ttl: %u"
+ "ResolveSimultaneousProbe - deregistering %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u type %{public}s on interface id: %p due to TSR conflict"
+ "Resuming the %{public}s enumeration - active client count: %u, domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u."
+ "SKIPPED unicast assist query - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u %d %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{mdns:rrtype}d qhash %{sensitive}x"
+ "SPS Callback %d %{sensitive}s %{mdns:s_hash}u"
+ "SendResponses: No active interface %d to send: %d %02X %{sensitive}s %{mdns:s_hash}u"
+ "ServiceCallback: All records %{public}sregistered for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "SetNextAnnounceProbeTime: ProbeCount %d Next in %d %{sensitive}s %{mdns:s_hash}u"
+ "SetPrefsBrowseDomains is adding/removing domain for Browsing and Automatic Browsing domains - domain name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, uid: %u, result: %{public}s"
+ "SetTargetToHostName: Don't know how to set the target of rrtype %{mdns:rrtype}d"
+ "SetUnicastTargetToHostName No target for %{sensitive}s %{mdns:s_hash}u"
+ "SetUnicastTargetToHostName target %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u for resource record %{public}s"
+ "SetupActiveInterfaces: Registered %{public}s (%u) BSSID %{sensitive, mdnsresponder:mac_addr}.6P %{mdns:mac_hash}u Struct addr %p, primary %p, %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u/%d%{public}s%{public}s%{public}s"
+ "Starting the %{public}s enumeration - domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u."
+ "State Dump: filename is too long to be put into the buffer, ignoring the current file - file name to be copied: %{sensitive}s, length: %u, buffer length: %u"
+ "Stopping the %{public}s enumeration - domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u."
+ "Stopping the resolver discovery -- domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "TSR timestamp - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, new: %d  old: %d"
+ "The AWDLServiceDiscoveryManager class isn't available"
+ "The mDNS message does not have enough space for the NSEC record, will add it to the next message (This is not an error message) -- remaining space: %ld, NSEC name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "TimingDefenseForceEnable"
+ "Tried to register a NetworkInterfaceInfo that's already in the list - ifname: %{public}s, ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "Tried to register a NetworkInterfaceInfo with invalid mask - ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u, ifmask: %{public, mdnsresponder:ip_addr}.20P"
+ "Tried to register a NetworkInterfaceInfo with zero InterfaceID - ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "Unable to start OHTTP config fetch"
+ "Unicast assist answered -- new POOF threshold %u for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{mdns:rrtype}d"
+ "UpdateDeviceInfoRecord Deregister %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "UpdateDeviceInfoRecord Register %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "UpdateQuestionDuplicates transferred LLQ state for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "UpdateQuestionDuplicates transferred nta pointer for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "Using fast activation for DirectLink interface - ifname: %{public}s, ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "[A(%x, %x)] Received %u-byte IPv4 mDNS query from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[A(%x, %x)] Received %u-byte IPv4 mDNS query from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[A(%x, %x)] Received %u-byte IPv6 mDNS query from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[A(%x, %x)] Received %u-byte IPv6 mDNS query from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[A(%x, %x)] Received a previous IPv4 mDNS query from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over multicast via %{public}s/%u"
+ "[A(%x, %x)] Received a previous IPv4 mDNS query from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u"
+ "[A(%x, %x)] Received a previous IPv6 mDNS query from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over multicast via %{public}s/%u"
+ "[A(%x, %x)] Received a previous IPv6 mDNS query from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u"
+ "[A(%x, %x)] Sent %u-byte IPv4 mDNS response over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[A(%x, %x)] Sent %u-byte IPv4 mDNS response to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[A(%x, %x)] Sent %u-byte IPv6 mDNS response over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[A(%x, %x)] Sent %u-byte IPv6 mDNS response to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[A(%x, %x)] Sent a previous IPv4 mDNS response to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u"
+ "[A(%x, %x)] Sent a previous IPv6 mDNS response to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u"
+ "[Q%d] AnswerQuestionByFollowingCNAME: Resolving a .local CNAME -- CNAME: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[Q%u->SubQ%u] DS denial lookup record changes - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, %{mdns:pos/neg}d, %{mdns:addrmv}d, interface index: %d, mortality: %{mdns:mortality}d, ttl: %u"
+ "[Q%u->SubQ%u] Insecure validation complete, scheduling cache update - insecure zone: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, ttl: %u"
+ "[Q%u->SubQ%u] Possible DS denial found, starting secure DS denial query - DS name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[Q%u->SubQ%u] Searching for DS denial - q_name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[Q%u->SubQ%u] Start insecure validation - unsigned domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[Q%u->SubQ%u] Start to query validated key records to validate the RRSet - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d"
+ "[Q%u->SubQ%u] Stop DS denial look up question - DS denial lookup name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[Q%u] %{public}s %{public}s DNS Message %lu bytes from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d via %{public}s (%p)"
+ "[Q%u] AnswerQuestionByFollowingCNAME: Not following CNAME referral -- CNAME: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, referral count: %u, self referential: %{mdns:yesno}d"
+ "[Q%u] AnswerQuestionByFollowingCNAME: following CNAME referral -- CNAME: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, referral count: %u"
+ "[Q%u] CacheRecordRmvEventsForCurrentQuestion: Calling AnswerCurrentQuestionWithResourceRecord (RMV) for question - rr name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rr type: %{mdns:rrtype}d, local answers: %u"
+ "[Q%u] CacheRecordRmvEventsForCurrentQuestion: Suppressing RMV events for question - rr name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rr type: %{mdns:rrtype}d, current active question: Q%d, current answers: %u"
+ "[Q%u] Create the denial of existence record set - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, denial type: %{public}s"
+ "[Q%u] Current DNSSEC validation manager contains record(s) that are to be removed soon, wait for the coming update before updating the cache - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[Q%u] DNS %{public}s%{public}s (%lu) (flags %02X%02X) RCODE: %{public}s (%d)%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s:%{sensitive}s %{mdns:s_hash}u %u/%u/%u %{sensitive}s %{mdns:s_hash}u"
+ "[Q%u] DNS push discovery finished, using service with SRV name _dns-push-tls._tcp.%{public, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u -- service id: %llu, re registered: %{mdns:yesno}d"
+ "[Q%u] DNSSEC record changes - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, rrtype: %{mdns:rrtype}d, %{mdns:pos/neg}d, contains denial: %{mdns:yesno}d, %{mdns:addrmv}d, interface index: %d, motality: %{mdns:mortality}d, original ttl: %u, actual ttl: %u, validated: %{mdns:yesno}d."
+ "[Q%u] DNSSEC secure record changes - %{mdns:pos/neg}d, %{mdns:addrmv}d, qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, rd_len: %u."
+ "[Q%u] DetermineUnicastQuerySuppression: Query suppressed for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{public}s%{public}s"
+ "[Q%u] Failed to register push service -- id: %lluauthoritative zone: %{public, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, interface index: %u, error: %{mdns:err}ld"
+ "[Q%u] Generating RMV events because the question will be stopped - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{public}s."
+ "[Q%u] InitDNSConfig: Setting StopTime on the uDNS question %p %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[Q%u] Insecure validation failed - state: %{public, mdns:dnssec_inval_state}u, DS denial lookup name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, DS denial lookup q: Q%d, secure DS denial q: Q%d"
+ "[Q%u] New validation key requestor replaces the old one - new name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, old name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d"
+ "[Q%u] Sending unicast assist query (refresh %{mdns:yesno}d) - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{mdns:rrtype}d qhash %{sensitive}x"
+ "[Q%u] Sending unicast assist query - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u %d %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{mdns:rrtype}d qhash %{sensitive}x"
+ "[Q%u] Stopping Primary DNSSEC question - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d"
+ "[Q%u] The discovered possible denial of existence for DS record points back to the current question itself, insecure delegation validation fails due to possible missing RRSIG of the original response - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[Q%u] The existing validation key requestor can still be reused - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d"
+ "[Q%u] Unable to continue the trust chain validation since DS is self-signed - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[Q%u] Unable to create the denial of existence record set - error: %{public}s, qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, soaRRSIGCount: %u, nsecCount: %u, nsec3Count: %u, rrsigCount: %u."
+ "[Q%u] Unable to start DNS push server discovery for the single-label name (TLD) -- qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d"
+ "[Q%u] Update cache for DNSSEC question - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, rr_type: %{mdns:rrtype}d, new original ttl: %u, actual ttl: %u, %{mdns:pos/neg}d, DNSSEC result: %{public, mdns:dnssec_result}u, rescued: %zu, added: %zu, total: %zu, purged: %zu."
+ "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s), PID[%d], EUID[%u], ServiceID[%d] evaluator is NULL"
+ "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s), PID[%d], EUID[%u], ServiceID[%d] host is NULL"
+ "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s), PID[%d], EUID[%u], ServiceID[%d] parameters is NULL"
+ "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s), PID[%d], EUID[%u], ServiceID[%d] path is NULL"
+ "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u service ID is set ->service_ID:[%d] "
+ "[Q%u] mDNSPlatformSendUDP -> sendto(%d) failed to send packet on InterfaceID %p %{public}s/%d to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d skt %d error %ld errno %d (%{public}s) %u"
+ "[Q%u] mDNSPlatformSendUDP sendto(%d) failed to send packet on InterfaceID %p %{public}s/%d to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d skt %d error %ld errno %d (%{public}s) %u"
+ "[Q%u] mDNSPlatformSendUDP: sendto(%d) failed to send packet on InterfaceID %p %{public}s/%d to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d skt %d error %ld errno %d (%{public}s) %u MessageCount is %d"
+ "[Q%u] mDNS_StartQuery_internal START -- qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d"
+ "[Q%u] mDNS_StopQuery_internal STOP -- name hash: %{public, mdns:dn_hash}u"
+ "[Q%u] setsockopt - IP_MULTICAST_IF error %{sensitive, network:in_addr}.4P %{mdns:ipv4_hash}u %d errno %d (%{public}s)"
+ "[Q(%x, %x)] Received %u-byte IPv4 mDNS response from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[Q(%x, %x)] Received %u-byte IPv4 mDNS response from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[Q(%x, %x)] Received %u-byte IPv6 mDNS response from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[Q(%x, %x)] Received %u-byte IPv6 mDNS response from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[Q(%x, %x)] Received a previous IPv4 mDNS response from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over multicast via %{public}s/%u"
+ "[Q(%x, %x)] Received a previous IPv4 mDNS response from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u"
+ "[Q(%x, %x)] Received a previous IPv6 mDNS response from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over multicast via %{public}s/%u"
+ "[Q(%x, %x)] Received a previous IPv6 mDNS response from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u"
+ "[Q(%x, %x)] Sent %u-byte IPv4 mDNS query over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[Q(%x, %x)] Sent %u-byte IPv4 mDNS query to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[Q(%x, %x)] Sent %u-byte IPv6 mDNS query over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[Q(%x, %x)] Sent %u-byte IPv6 mDNS query to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mdnsresponder:mdns_name_hash_type_bytes}.*P"
+ "[Q(%x, %x)] Sent a previous IPv4 mDNS query to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u"
+ "[Q(%x, %x)] Sent a previous IPv6 mDNS query to %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u over unicast via %{public}s/%u"
+ "[R%u->(Q%u, Q%u)] DNSServiceResolve NoSuchRecord -- instance: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, split AWDL query: %{mdns:yesno}d"
+ "[R%u->(Q%u, Q%u)] DNSServiceResolve RESULT -- instance: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, ifindex: %u, target host: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u), port: %u, negative txt: %{mdns:yesno}d, txt rdlength: %u, split AWDL query: %{mdns:yesno}d"
+ "[R%u->DupQ%d->Q%d] UpdateQuestionDuplicates: question %p %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s) duplicate of %p %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u->DupQ%u->Q%u] Duplicate question %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u->Q%d] AnswerNewQuestion ERROR m->CurrentQuestion already set: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u->Q%d] DNSServiceEnumerateDomains(%{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u) RESULT %{mdns:addrmv_upper}d: %{sensitive}s %{mdns:dn_hash}u"
+ "[R%u->Q%u->subQ%u] Stop getting the zone data - zone qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, zone qtype: %{public}s."
+ "[R%u->Q%u] Cleared resolver UUID for question: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Q%u] InitDNSConfig: Setting StopTime on the uDNS question %p %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u->Q%u] Not starting long-lived query polling since the question has been stopped - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{public}s, LLQ_State: %{public}s."
+ "[R%u->Q%u] Question for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s%{public}s) assigned DNS service -- %@"
+ "[R%u->Q%u] Restarting question that got expired CNAMEs -- current name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, original name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d"
+ "[R%u->Q%u] Retrying path evaluation -- qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{public}s, reason: %{public}s"
+ "[R%u->Q%u] Starting long-lived query polling - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{public}s, LLQ_State: %{public}s."
+ "[R%u->Q%u] mDNSCoreReceiveNoUnicastAnswers: Generate negative response for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u->Q%u] mDNSCoreReceiveNoUnicastAnswers: Renewing negative TTL from %u to %u %{sensitive}s %{mdns:s_hash}u"
+ "[R%u->Q%u] mDNSCoreReceiveNoUnicastAnswers: Skipping check and not creating a negative cache entry for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u->Q%u] mDNS_StopQuery_internal: Question %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s) not found in active list."
+ "[R%u->Q%u] queryrecord_result_reply add tracker %{sensitive}s %{mdns:dn_hash}u"
+ "[R%u->Rec%u] DNSServiceRegisterRecord Result -- event: %{public, mdnsresponder:reg_result}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Rec%u] DNSServiceRegisterRecord Result -- event: %{public, mdnsresponder:reg_result}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Rec%u] DNSServiceRegisterRecord Result -- event: %{public, mdnsresponder:reg_result}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Rec%u] DNSServiceRegisterRecord Result -- event: %{public, mdnsresponder:reg_result}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Rec%u] DNSServiceRegisterRecord START -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, "
+ "[R%u->Rec%u] DNSServiceRegisterRecord START -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), "
+ "[R%u->Rec%u] DNSServiceRegisterRecord START -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u->Rec%u] DNSServiceRegisterRecord START -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, name hash: %{public, mdns:dn_hash}u"
+ "[R%u->Rec%u] DNSServiceRegisterRecord STOP -- name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u->Rec%u] DNSServiceRegisterRecord STOP -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, index: %d, client: %{public}s(pid: %d), duration: %{mdns:time_duration}utype: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Rec%u] DNSServiceRegisterRecord STOP -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, index: %d, client: %{public}s(pid: %d), duration: %{mdns:time_duration}utype: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Rec%u] DNSServiceRemoveRecord -- ifindex: %d, client pid: %d (%{public}s), duration: %{mdns:time_duration}u, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->Rec%u] DNSServiceRemoveRecord -- ifindex: %d, client pid: %d (%{public}s), duration: %{mdns:time_duration}u, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->Rec%u] DNSServiceRemoveRecord -- name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceRegisterRecord Result -- record %u, event: ERROR, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceRegisterRecord Result -- record %u, event: ERROR, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceRegisterRecord Result -- record %u, event: ERROR, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceRegisterRecord Result -- record %u, event: ERROR, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %{public, mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "[R%u] DNSServiceAddRecord(%X, %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, %{public}s, %d) PID[%d](%{public}s)"
+ "[R%u] DNSServiceBrowse -> SubBrowser START -- qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[R%u] DNSServiceBrowse Cancel domain enumeration for WAB and mDNS -- , flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceBrowse Cancel domain enumeration for WAB and mDNS -- name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceBrowse START -- name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceBrowse START -- service type: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, domain: %{sensitive}s %{mdns:dn_hash}u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceBrowse STOP -- name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceBrowse STOP -- service name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceGetAddrInfo START -- hostname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, protocols: %u, DNSSEC enabled, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceGetAddrInfo START -- hostname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, protocols: %u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceGetAddrInfo START -- name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceGetAddrInfo STOP -- hostname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceGetAddrInfo STOP -- name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceGetAddrInfo: Signed result does not cover hostname: %{sensitive}s %{mdns:dn_hash}u, ifindex: %u."
+ "[R%u] DNSServiceNATPortMappingCreate(%X, %u, %u, %u) RESULT %{sensitive, network:in_addr}.4P %{mdns:ipv4_hash}u:%u TTL %u"
+ "[R%u] DNSServiceQueryRecord START -- name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceQueryRecord START -- qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, DNSSEC enabled, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceQueryRecord START -- qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceQueryRecord STOP -- name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceQueryRecord STOP -- qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceReconfirmRecord FAILED -- name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceReconfirmRecord FAILED -- rr name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rr type: %{mdns:rrtype}d, error: %d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), "
+ "[R%u] DNSServiceReconfirmRecord FAILED -- rr name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rr type: %{mdns:rrtype}d, error: %d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceReconfirmRecord START -- name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceReconfirmRecord START -- rr name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rr type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), "
+ "[R%u] DNSServiceReconfirmRecord START -- rr name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rr type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceRegister START -- name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceRegister START -- service type: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, port: %u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceRegister STOP -- SRV name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, port: %u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceRegister STOP -- name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceRegister result -- event: ADDED, SRV name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, port: %u, PTR name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceRegister(%{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, %u) %s"
+ "[R%u] DNSServiceRemoveRecord(%{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, %{public}s) PID[%d](%{public}s): %d"
+ "[R%u] DNSServiceResolve START -- SRV name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, split AWDL query: %{mdns:yesno}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceResolve START -- name hash: %{public, mdns:dn_hash}u"
+ "[R%u] DNSServiceResolve STOP -- SRV name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, split AWDL query: %{mdns:yesno}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceResolve STOP -- name hash: %{public, mdns:dn_hash}u, duration: %{mdns:time_duration}u"
+ "[R%u] DNSServiceResolve: Signed result does not cover service: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, ifindex: %u."
+ "[R%u] DNSServiceUpdateRecord(%{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, %{mdns:rrtype}d) UPDATE PID[%d](%s)"
+ "[R%u] DNSServiceUpdateRecord(%{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, %{public}s%{public}s) PID[%d](%{public}s)"
+ "[R%u] ERROR: QueryRecordOpStartQuestion mDNS_StartQuery for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{public}s failed with error %d"
+ "[R%u] ERROR: bad domain name '%{sensitive}s %{mdns:dn_hash}u'"
+ "[R%u] ERROR: bad hostname '%{sensitive}s %{mdns:dn_hash}u'"
+ "[R%u] PeerConnectionRelease(%X %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u) START PID[%d](%{public}s)"
+ "[R%u] QueryRecordOpCallback: Question %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s) answering local with negative unicast response"
+ "[R%u] QueryRecordOpCallback: Question %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s) timing out, InterfaceID %p"
+ "[R%u] QueryRecordOpCallback: Suppressed question %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u] QueryRecordOpStart: starting parallel unicast query for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{public}s"
+ "[R%u] Restarting question for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s) due to DNS service failover"
+ "[R%u] Restarting question for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u AAAA record as question for A record (RCODE %d)"
+ "[R%u] Signed resolve result does not cover request -- hostname: %{sensitive}s %{mdns:dn_hash}u, ifindex: %u"
+ "[R%u] getaddrinfo error -- hostname: %{private}s %{mdns:dn_hash}u, error: %{mdns:err}ld, client pid: %lld (%{public}s)"
+ "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{private}s %{mdns:dn_hash}u, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s)"
+ "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{private}s %{mdns:dn_hash}u, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s), delegator pid: %lld (%{public}s)"
+ "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{private}s %{mdns:dn_hash}u, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s), delegator uuid: %{public,uuid_t}.16P"
+ "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{sensitive}s %{mdns:dn_hash}u, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s)"
+ "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{sensitive}s %{mdns:dn_hash}u, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s), delegator pid: %lld (%{public}s)"
+ "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{sensitive}s %{mdns:dn_hash}u, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s), delegator uuid: %{public,uuid_t}.16P"
+ "[R%u] getaddrinfo stop (forced) -- hostname: %{private}s %{mdns:dn_hash}u, client pid: %lld (%{public}s)"
+ "[R%u] getaddrinfo stop (forced) -- hostname: %{sensitive}s %{mdns:dn_hash}u, client pid: %lld (%{public}s)"
+ "[R%u] getaddrinfo stop -- hostname: %{private}s %{mdns:dn_hash}u, client pid: %lld (%{public}s)"
+ "[R%u] getaddrinfo stop -- hostname: %{sensitive}s %{mdns:dn_hash}u, client pid: %lld (%{public}s)"
+ "[R%u] handle_regrecord_request: TSR fail, removing %{sensitive}s %{mdns:s_hash}u (%p), InterfaceID %p"
+ "[R%u] mDNS_StartBrowse returned error (UNICAST_DISCOVERY) -- error: %d, type: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "[R%u] read_rr_from_ipc_msg: SetRData failed for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[R%u] regRecordAddTSRRecord(0x%X, %d, %{sensitive}s %{mdns:s_hash}u) START PID[%d](%{public}s)"
+ "[R%u] regRecordAddTSRRecord(0x%X, %d,%{sensitive}s %{mdns:s_hash}u) ERROR (%d)"
+ "[R%u] regservice_callback: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u is not valid DNS-SD SRV name"
+ "[R%u] update_record: SetRData failed for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "[Sub%llu] Collectively removing record(s) -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d"
+ "[Sub%llu] DNS Push server returned unrelated record -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d"
+ "[Sub%llu] Removing record from the cache due to subscriber invalidation -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, TTL: %us"
+ "addAWDLDiscoveryClient:forService:error:"
+ "application/ohttp-keys"
+ "awdl"
+ "clock"
+ "clock_gettime_nsec_np(CLOCK_UPTIME_RAW) error: %{mdns:err}d"
+ "com.apple.private.restrict-post.wifip2p.awdl.AWDLDiscoveryTimeout"
+ "conflictWithAuthRecordsOrFlush - Conflict with %{sensitive}s %{mdns:s_hash}u (%p), InterfaceID %p"
+ "conflictWithAuthRecordsOrFlush - deregistering %{sensitive}s %{mdns:s_hash}u InterfaceID %p"
+ "conflictWithCacheRecordsOrFlush - new TSR, flushing interface %d %{sensitive}s %{mdns:s_hash}u"
+ "external_start_resolving_service - fqdn: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "external_stop_resolving_service - fqdn: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "handle_regrecord_request: Name conflict %{sensitive}s %{mdns:s_hash}u InterfaceID %p"
+ "handle_regrecord_request: TSR Stale Data, record cache is newer %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u InterfaceID %p"
+ "handle_regrecord_request: TSR Stale data, auth cache is newer %{sensitive}s %{mdns:s_hash}u InterfaceID %p"
+ "https://%s/.well-known/ohttp-gateway"
+ "internal_start_advertising_service - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rrtype: %{mdns:rrtype}d"
+ "internal_start_browsing_for_service: starting browse - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d"
+ "internal_stop_advertising_service: %{sensitive}s %{mdns:s_hash}u"
+ "internal_stop_browsing_for_service: stopping browse - qname: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, qtype: %{mdns:rrtype}d"
+ "intf->InterfaceActive already set for interface - ifname: %{public}s, ifaddr: %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "mDNSCoreDowngradeAWDLInclusion"
+ "mDNSCoreMachineSleep: %{sensitive}s %{mdns:s_hash}u: Adjusted the remain ttl %d by %d seconds"
+ "mDNSCoreMachineSleep: %{sensitive}s %{mdns:s_hash}u: Purging after adjusting the remaining TTL %d by %d seconds"
+ "mDNSCoreMachineSleep: %{sensitive}s %{mdns:s_hash}u: Purging cache entry SleptTime %d, Remaining TTL %d"
+ "mDNSCoreReceiveCacheCheck: Discarding (%{public}s) %{sensitive}s %{mdns:s_hash}u rrtype change from (%{mdns:rrtype}d%{public}s) to (%{mdns:rrtype}d%{public}s)"
+ "mDNSCoreReceiveCacheCheck: Discarding due to domainname case change new: %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveCacheCheck: Discarding due to domainname case change old: %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveCacheCheck: Keeping Standard TTL for %{sensitive}s %{mdns:s_hash}u %p"
+ "mDNSCoreReceiveCacheCheck: rescuing RR with new TTL %u: %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveNoUnicastAnswers: Removing expired record %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse - deregistering %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u type %{public}s on interface %d due to TSR conflict"
+ "mDNSCoreReceiveResponse - flushed interface %d %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse - flushing cache group %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u type %{public}s on interface %d due to TSR conflict"
+ "mDNSCoreReceiveResponse: Already reset to Probing: %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse: Dep Record: %08X %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse: Ignoring response received before we even began probing: %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse: Our Record: %08X %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse: Pkt Record: %08X %{sensitive}s %{mdns:s_hash}u (interface %d)"
+ "mDNSCoreReceiveResponse: ProbeCount %u; restarting probing after %d-tick pause due to possibly spurious multicast conflict (%d/%d) via interface %d for %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse: ProbeCount %u; will deregister %{sensitive}s %{mdns:s_hash}u due to %{public}scast conflict via interface %d"
+ "mDNSCoreReceiveResponse: Received from %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse: Resetting to Probing: %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse: Unexpected conflict discarding %{sensitive}s %{mdns:s_hash}u"
+ "mDNSCoreReceiveResponse: Unexpected record type %X %{sensitive}s %{mdns:s_hash}u"
+ "mDNSPlatformValidRecordForInterface: Filtering privacy risk -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, ifname: %{public}s, ifid: %d"
+ "mDNSPreferencesSetNames: changing computer name -- last change: %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u -> %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u, current change: %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u -> %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u"
+ "mDNSPreferencesSetNames: changing local host name -- last change: %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u -> %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u, current change: %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u -> %{sensitive, mdnsresponder:domain_label}.*P %{mdns:dl_hash}u"
+ "mDNSResponder-3066.0.0.502.1"
+ "mDNS_AddMcastResolver: Adding %{public, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, InterfaceID %p, timeout %u"
+ "mDNS_AddSearchDomain: domain already in list -- search domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "mDNS_AddSearchDomain: new search domain added -- search domain: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, InterfaceID %p"
+ "mDNS_Deregister_internal: %{sensitive}s %{mdns:s_hash}u already marked kDNSRecordTypeDeregistering"
+ "mDNS_Deregister_internal: %{sensitive}s %{mdns:s_hash}u already marked kDNSRecordTypeUnregistered"
+ "mDNS_Deregister_internal: ERROR!! cannot insert %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_Deregister_internal: Purging cached record that matches deregistered AuthRecord -- interface: %{public}s/%u, record: %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_Deregister_internal: Record %p not found in list %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_Deregister_internal: callback with mStatus_MemFree for %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_FinalExit failed to send goodbye for: %p %02X %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_PurgeBeforeResolve: Flushing %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_Register_internal: Diverting record to local-only %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_Register_internal: ERROR! %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s): rr->DependentOn && RecordType != kDNSRecordTypeUnique or kDNSRecordTypeKnownUnique"
+ "mDNS_Register_internal: ERROR! %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s): rr->DependentOn->RecordType bad type %X"
+ "mDNS_Register_internal: ERROR!! Tried to register AuthRecord %p %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{mdns:rrtype}d) that's already in the Duplicate list"
+ "mDNS_Register_internal: ERROR!! Tried to register AuthRecord %p %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{mdns:rrtype}d) that's already in the list"
+ "mDNS_Register_internal: ERROR!! Tried to register LocalOnly AuthRecord %p %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{mdns:rrtype}d) that's already in the list"
+ "mDNS_Register_internal: Name conflict %{sensitive}s %{mdns:s_hash}u (%p), InterfaceID %p"
+ "mDNS_Register_internal: RecordType must be non-zero %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_Register_internal: Shutting down, can't register %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_Register_internal: TTL %X should be 1 - 0x7FFFFFFF %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_Register_internal: adding to active record list -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "mDNS_Register_internal: adding to active record list -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "mDNS_Register_internal: adding to duplicate list -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mdns:rdata}.*P %{mdns:rd_hash}u"
+ "mDNS_Register_internal: adding to duplicate list -- name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, rdata: <none>"
+ "mDNS_Register_internal: record %{sensitive}s %{mdns:s_hash}u in NoTarget state"
+ "mDNS_RemoveDynDNSHostName %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "mDNS_RemoveDynDNSHostName removing v4 %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "mDNS_RemoveDynDNSHostName removing v6 %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "mDNS_RemoveDynDNSHostName: no such domainname %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "mDNS_StartExit: ERROR m->CurrentRecord already set %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_StartExit: Should not still have Duplicate Records remaining: %02X %{sensitive}s %{mdns:s_hash}u"
+ "mDNS_StartQuery_internal: Error! Tried to add a question %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s) %p that's already in the active list"
+ "mDNS_StopQuery_internal: Just deleted the current restart question: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{public}s)"
+ "ohttp"
+ "register_service_instance: TSR Stale Data, record cache is newer %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u InterfaceID %p"
+ "register_service_instance: TSR Stale data, auth cache is newer %{sensitive}s %{mdns:s_hash}u InterfaceID %p"
+ "removeAWDLDiscoveryClient:forService:error:"
+ "setAssumesHTTP3Capable:"
+ "shared"
+ "tcpConnectionCallback: DeviceDescription SOAP address %{sensitive}s %{mdns:s_hash}u SOAP path %{sensitive}s %{mdns:s_hash}u"
+ "tcpConnectionCallback: tcpInfo->Address:Port [%{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u:%d] tcpInfo->op[%u] tcpInfo->retries[%d] tcpInfo->Request[%{sensitive}s %{mdns:s_hash}u] tcpInfo->Reply[%{sensitive}s %{mdns:s_hash}u]"
+ "tls-supported-groups"
+ "tsrTimestamp[%u] out of range (%d) on TSR for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "uDNSDeregisterRecord: Cannot find the anchor Resource Record for %{sensitive}s %{mdns:s_hash}u, not an error"
+ "uDNS_DeregisterRecord: ERROR!! QueuedRData same as rdata for %{sensitive}s %{mdns:s_hash}u"
+ "uDNS_DeregisterRecord: ERROR: Another anchorRR %{sensitive}s %{mdns:s_hash}u found"
+ "uDNS_DeregisterRecord: Found Anchor RR %{sensitive}s %{mdns:s_hash}u terminated"
+ "uDNS_DeregisterRecord: Freeing InFlightRData for %{sensitive}s %{mdns:s_hash}u"
+ "uDNS_DeregisterRecord: Freeing QueuedRData for %{sensitive}s %{mdns:s_hash}u"
+ "uDNS_DeregisterRecord: InFlightRData same as rdata for %{sensitive}s %{mdns:s_hash}u"
+ "uDNS_DeregisterRecord: Resource Record %{sensitive}s %{mdns:s_hash}u, state %u"
+ "uDNS_DeregisterRecord: State %u for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u type %{public}s"
+ "uDNS_SetupWABQueries -- action: 0x%x, flags: 0x%x, ifid: %p, domain: %{public, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: DELETE Browse for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: DELETE Deregistering PTR -- record: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u PTR %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: DELETE Legacy Browse for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: DELETE Registration for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: Deleting Browse for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: Deleting Legacy Browse for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: Deleting Registration for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowse) returned error -- name hash: %{public, mdns:dn_hash}u, error: %d"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowseAutomatic) returned error -- name hash: %{public, mdns:dn_hash}u, error: %d"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowseDefault) returned error -- name hash: %{public, mdns:dn_hash}u, error: %d"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeRegistration) returned error -- name hash: %{public, mdns:dn_hash}u, error: %d"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeRegistrationDefault) returned error -- name hash: %{public, mdns:dn_hash}u, error: %d"
+ "uDNS_SetupWABQueries: Starting Browse for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: Starting Default Browse for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: Starting Default Registration for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: Starting Legacy Browse for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_SetupWABQueries: Starting Registration for domain -- name hash: %{public, mdns:dn_hash}u"
+ "uDNS_Tasks ERROR m->CurrentQuestion already set: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u (%{mdns:rrtype}d)"
+ "unicast assist (restart) - no active question for qnamehash %{sensitive}x"
+ "unicast assist _addRecordsFromPresence: (error) qhash %x addr %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u err %d"
+ "unicast assist _addRecordsFromPresence: add qhashes %@ addr %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u ifhash %x"
+ "unicast assist _addRecordsFromPresence: no subnet for addr %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "unicast assist _addRecordsFromPresence: restarted (%s) qhash %x addr %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u"
+ "unicast assist persistance cache read failed (next qhash) addr %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u ifhash %x ifid %2.2u"
+ "unicast assist persistance cache save failed addr %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u ifhash %x ifid %2.2u"
+ "unicast assist persistance cache save failed qhash %x %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u ifhash %x ifid %2.2u"
+ "unicast assist qhash (%s) keeping presence - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u qhash %x"
+ "unicast assist qhash flushed (%s) - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u qhash %x"
+ "unicast assist qhash flushed (overflow) - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u qhash %x"
+ "unicast assist record %s %s%s - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u %2.2u %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{public}s qhash %x rectype 0x%X%s"
+ "unicast assist record flushed (0 qhashes) - %{sensitive, mdnsresponder:ip_addr}.20P %{mdns:ip_hash}u %2.2u ifhash %x"
+ "v28@?0^{dispatch_data_s=}8i16^{__CFError=}20"
+ "xD2DAddToCache: mDNS_Register failed - error: %d, name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, auth record: %{sensitive}s %{mdns:s_hash}u"
+ "xD2DAddToCache: mDNS_Register succeeded - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, Interface ID: %p, auth record: %{sensitive}s %{mdns:s_hash}u"
+ "xD2DClearCache: Clearing and deregistering cache record - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rrtype: %{mdns:rrtype}d, auth record: %{sensitive}s %{mdns:s_hash}u"
+ "xD2DFindInList: Could not find in D2DRecords - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, auth record: %{sensitive}s %{mdns:s_hash}u"
+ "xD2DParse got record - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, rrtype: %{mdns:rrtype}d, rdata: %{sensitive}s %{mdns:s_hash}u"
+ "xD2DParseCompressedPacket: Our Bytes - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, TTL: %u, rdata length: %u"
+ "xD2DRemoveFromCache: removing record from cache - name: %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u, type: %{mdns:rrtype}d, auth record: %{sensitive}s %{mdns:s_hash}u"
- "\n"
- "\nADDITIONAL SECTION\n"
- "\nANSWER SECTION\n"
- "\nAUTHORITY SECTION\n"
- "\nQUESTION SECTION\n"
- "\n]"
- " %#H"
- " %-5s"
- " %-5s\n"
- " %.4H"
- " %2s"
- " %6u %2s"
- " %s=\""
- " %u%02u%02u%02u%02u%02u"
- " '%H'"
- " CF"
- " TYPE%u\n"
- "%#.4a"
- "%#H"
- "%#{txt}"
- "%-30s"
- "%-42s"
- "%.4H"
- "%s OPT %u"
- "%s%.*a"
- "%s%~s"
- "%{public}s Conflicting mDNS -- waking %{sensitive, mask.hash, mdnsresponder:mac_addr}.6P %{sensitive, mask.hash}s"
- "%{public}s: LHS: (%d bytes) %{sensitive, mask.hash, mdnsresponder:hex_sequence}.*P"
- "%{public}s: RHS: (%d bytes) %{sensitive, mask.hash, mdnsresponder:hex_sequence}.*P"
- "%~-30s"
- "%~-42s"
- "%~s"
- "%~s "
- "'%H'"
- "*** Network Configuration Change ***  IPv6 address %{sensitive, mask.hash, network:in6_addr}.16P TENTATIVE, will retry"
- "<IPv4:%s>"
- "<IPv6:%s>"
- "AddOrUpdateTSRForCacheGroup: %s TSR %{sensitive, mask.hash}s"
- "AddOrUpdateTSRForCacheGroup: No cache record for new TSR %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "AddOrUpdateTSRForCacheGroup: tsrTimestamp[%d] out of range (%d) on TSR for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "AddTSRRDataToMessage: TSR can't be written -- name %{sensitive, mask.hash, mdnsresponder:domain_name}.*P hashkey %x"
- "Additional count: %u\n"
- "Another representative of InterfaceID exists - ifid: %d, ifname: %{public}s, ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "Answer count:     %u\n"
- "Answer set counter not found for the cached record - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rrtype: %{sensitive, mask.hash}s."
- "AnswerAllLocalQuestionsWithLocalAuthRecord ERROR m->CurrentQuestion already set: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "AnswerLocalQuestionWithLocalAuthRecord: *NOT* delivering %{public}s event for local record type %X %{sensitive, mask.hash}s"
- "Attempt to put kDNSRecordTypeUnregistered %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "Attempt to register record with invalid name: %{sensitive, mask.hash}s"
- "Attempt to register record with invalid rdata: %{sensitive, mask.hash}s"
- "Authority count:  %u\n"
- "Automatic browsing domain changes - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, event: %{public}s, interface ID: %p%{public}s"
- "Automatic browsing domain discovered via network - change: %{public}s, interface name: %{public}s, browsing domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "Automatic browsing domain is added - domain name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, uid: %u"
- "Automatic browsing domain is removed - domain name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, uid: %u"
- "B28@?0r^{?=i(?=(?=[16C][8S][4I])(?=[4C]I))}8^{mDNSInterfaceID_dummystruct=^v}16B24"
- "Bad service type in %{sensitive, mask.hash, mdnsresponder:domain_label}.*P.%{sensitive, mask.hash, mdnsresponder:domain_name}.*P%{sensitive, mask.hash, mdnsresponder:domain_name}.*P Application protocol name must be underscore plus 1-15 characters. See <http://www.dns-sd.org/ServiceTypes.html>"
- "Binding IPv6 socket to random port failed -- error: %{mdns:err}ld, tries: %d"
- "Binding IPv6 socket to random port succeeded -- port: %u, tries: %d"
- "CF"
- "CF "
- "Can't put more names into current message, will possibly put it into the next message - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s), remaining space: %ld"
- "Can't put more rdata into current message, will possibly put it into the next message - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s), remaining space: %ld"
- "CancelGetZoneData: Question %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) ThisQInterval %d not -1"
- "Cannot exit yet; Resource Record still exists: %{sensitive, mask.hash}s"
- "Changed RRSet for %{sensitive, mask.hash}s"
- "ClearInactiveInterfaces: Deleting %{public}s(%u) %{sensitive, mask.hash, mdnsresponder:mac_addr}.6P InterfaceID %p(%p) %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P/%d Age %d -- primary: %{mdns:yesno}d"
- "ClearInactiveInterfaces: Deregistering %{public}s(%u) %{sensitive, mask.hash, mdnsresponder:mac_addr}.6P InterfaceID %p(%p), primary %p, %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P/%d -- flashing: %{mdns:yesno}d, occulting: %{mdns:yesno}d, primary: %{mdns:yesno}d"
- "ClearInactiveInterfaces: Holding %{public}s(%u) %{sensitive, mask.hash, mdnsresponder:mac_addr}.6P InterfaceID %p(%p) %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P/%d Age %d -- primary: %{mdns:yesno}d"
- "CompleteDeregistration: called for Resource record %{sensitive, mask.hash}s"
- "ConfigResolvers -- scope type: %{public, mdnsresponder:dns_scope_type}u, resolver[%d]: {domain: %{sensitive, mask.hash}s, name server count: %d}"
- "ConfigSearchDomains -- search domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "ConstructServiceName: %{public}s: %{sensitive, mask.hash, mdnsresponder:domain_label}.*P.%{sensitive, mask.hash, mdnsresponder:domain_name}.*P%{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "ConstructServiceName: Service type with non-leading underscore %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "Correcting TTL from %4u to %4u from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%u for records %{sensitive, mask.hash}s"
- "D2DBrowseListRelease - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, ref count: %u"
- "D2DBrowseListRelease item not found in the list - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d"
- "D2DBrowseListRetain - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, ref count: %u"
- "DNS over byte-stream"
- "DataBuffer_Append"
- "DataBuffer_AppendF"
- "DataBuffer_Detach"
- "DataBuffer_Free"
- "DataBuffer_Init"
- "DecrementAutoTargetServices: AutoTargetAWDLIncludedCount %u Record %{sensitive, mask.hash}s"
- "DecrementAutoTargetServices: AutoTargetAWDLOnlyCount %u Record %{sensitive, mask.hash}s"
- "DecrementAutoTargetServices: AutoTargetServices %u Record %{sensitive, mask.hash}s"
- "DecrementAutoTargetServices: NumAllInterfaceRecords %u NumAllInterfaceQuestions %u %{sensitive, mask.hash}s"
- "DecrementAutoTargetServices: called for RRLocalOnly() record: %{public}s"
- "Denial of existence record changes, purging the old negative record - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{public}s"
- "Denial of existence record does not change, rescuing the old negative record - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{public}s"
- "DeregLoop: %{public}s deregistration for %p %02X %{sensitive, mask.hash}s"
- "Deregistering orphaned TSR - %{sensitive, mask.hash}s"
- "DiscardDeregistrations ERROR m->CurrentRecord already set %{sensitive, mask.hash}s"
- "Discovered local resolver configuration updated - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, result: %d"
- "ERROR: remove_record, mDNS_Deregister: %d"
- "Error: regrecord_callback: successful registration of orphaned record %{sensitive, mask.hash}s"
- "Excessive name conflicts (%u) for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s); rate limiting in effect"
- "Failed to find out a provable denial of existence NSEC set - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %u, NSEC count: %u, error: %{public}s"
- "Failed to find out a provable denial of existence NSEC3 set - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %u, NSEC3 count: %u, error: %{public}s"
- "Failed to set computer name -- name: %{sensitive, mask.hash}s, error: %ld"
- "Failed to set local hostname -- name: %{sensitive, mask.hash}s, error: %ld"
- "Fast flushing AWDL cache record -- age: %d ticks, expire: %d ticks, record: %{sensitive, mask.hash}s"
- "Flags:            0x%04X %c/"
- "FlushAddressCacheRecords: Purging Resourcerecord - record description: %{sensitive, mask.hash}s."
- "FlushAllCacheRecords: Purging Resourcerecord - record description: %{sensitive, mask.hash}s."
- "Found a matching entry in the CacheFlushRecords - new rrtype: %{sensitive, mask.hash}s, matched name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, description: %{sensitive, mask.hash}s"
- "FreeARElemCallback: Have to cut %{sensitive, mask.hash}s"
- "FreeD2DARElemCallback: Could not find in D2DRecords: %{sensitive, mask.hash}s"
- "FreeD2DARElemCallback: Found in D2DRecords: %{sensitive, mask.hash}s"
- "FreeEtcHosts: %{sensitive, mask.hash}s"
- "GetAuthGroup: Already have AuthGroup for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "GetAuthGroup: Failed to allocate memory for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "GetAuthGroup: Not finding AuthGroup for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "GetAuthInfoForName_internal deleting expired key %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "GetLargeResourceRecord: SetRData failed for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "ID:               0x%04X (%u)\n"
- "Ignoring attempt to re-add interface (%{public}s, %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P) already marked as existing"
- "Ignoring conflict on interface %d with recently deregistered hostname record: %{sensitive, mask.hash}s"
- "IncrementAutoTargetServices: AutoTargetAWDLIncludedCount %u Record %{sensitive, mask.hash}s"
- "IncrementAutoTargetServices: AutoTargetAWDLOnlyCount %u Record %{sensitive, mask.hash}s"
- "IncrementAutoTargetServices: AutoTargetServices %u Record %{sensitive, mask.hash}s"
- "IncrementAutoTargetServices: NumAllInterfaceRecords %u NumAllInterfaceQuestions %u %{sensitive, mask.hash}s"
- "IncrementAutoTargetServices: called for RRLocalOnly() record: %{sensitive, mask.hash}s"
- "Initialized RRSet for %{sensitive, mask.hash}s"
- "Interface already represented in list - ifid: %d, ifname: %{public}s, ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "Interface not represented in list; marking active and retriggering queries - ifid: %d, ifname: %{public}s, ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "Interface probe will be delayed - ifname: %{public}s, ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P, probe delay: %d"
- "Invalid expiration time for the current DNSSEC validated record - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr_type: %{mdns:rrtype}d"
- "Invalid mDNSAddrType - domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, interface index: %u, mDNSAddrType: v%d."
- "LNT MakeTCPConnection: bad address/port %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d"
- "Last representative of InterfaceID deregistered; marking questions etc. dormant - ifid: %d, ifname: %{public}s, ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "Make validated RR expire soon - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr_type: %{mdns:rrtype}d"
- "MakeTCPConnection: connecting to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d"
- "Making record answered by the current response as expired if it is not refreshed in the response - Q interface ID: %p, qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{sensitive, mask.hash}s, RR interface ID: %p, RR description: %{sensitive, mask.hash}s."
- "NetWakeInterface: interface -- ifname: %{public}s, address: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P, supports Wake-On-Lan: %{mdns:yesno}d"
- "No existing TSR for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "No target count to update for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "Planning to stop the %{public}s enumeration - domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, grace period: %ds."
- "Pointer to message is NULL while filling resource record %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "ProbeRRMatchAndTSRCheck: Conflict with our ar %p rrtype: %{sensitive, mask.hash}s, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P%{sensitive, mask.hash}s"
- "ProbeRRMatchAndTSRCheck: pkt ar on interface  %p rrtype: %{sensitive, mask.hash}s, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P%{sensitive, mask.hash}s"
- "ProcessQuery - deregistering %{sensitive, mask.hash, mdnsresponder:domain_name}.*P type %{public}s on interface id: %p due to TSR conflict"
- "ProcessQuery: Preparing unicast assist query (max unanswered) - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{mdns:rrtype}d qhash %x"
- "Purging cached TSR record that matches orphaned TSR -- %{sensitive, mask.hash}s"
- "QM"
- "QU"
- "Question count:   %u\n"
- "Question not found in the active list - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{public}s."
- "Received Goodbye packet for cached record -- name hash: %x, type: %{mdns:rrtype}d, last time received: %{public, timeval}.*P, interface index: %u, source address: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P, name hash if PTR: %x"
- "Received positive DNSKEY or DS RRSet without RRSIG, malformed - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d."
- "ReconfirmAntecedents: Reconfirming (depth=%d, InterfaceID=%p, name_hash=%x, target_name_hash=%x) %{sensitive, mask.hash}s"
- "ReleaseCacheRecord: ERROR!! cg NULL for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "RemoveAuthRecord: ERROR!! AuthGroup not found for %{sensitive, mask.hash}s"
- "RemoveAuthRecord: removing auth record %{sensitive, mask.hash}s from table"
- "Removing cached peer record -- peer address: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d"
- "Removing record(s) -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P, collectively: %{mdns:yesno}d"
- "Rescuing DNSSEC validated record - name: %{public, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, old original ttl: %u, new original ttl: %u, new actual ttl: %u"
- "ResolveSimultaneousProbe - deregistering %{sensitive, mask.hash, mdnsresponder:domain_name}.*P type %{public}s on interface id: %p due to TSR conflict"
- "Resuming the %{public}s enumeration - active client count: %u, domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P."
- "SKIPPED unicast assist query - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %d %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{mdns:rrtype}d qhash %x"
- "SNPrintF"
- "SPS Callback %d %{sensitive, mask.hash}s"
- "SendResponses: No active interface %d to send: %d %02X %{sensitive, mask.hash}s"
- "ServiceCallback: All records %{public}sregistered for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "SetNextAnnounceProbeTime: ProbeCount %d Next in %d %{sensitive, mask.hash}s"
- "SetPrefsBrowseDomains is adding/removing domain for Browsing and Automatic Browsing domains - domain name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, uid: %u, result: %{public}s"
- "SetTargetToHostName: Don't know how to set the target of rrtype %{public}s"
- "SetUnicastTargetToHostName No target for %{sensitive, mask.hash}s"
- "SetUnicastTargetToHostName target %{sensitive, mask.hash, mdnsresponder:domain_name}.*P for resource record %{public}s"
- "SetupActiveInterfaces: Registered %{public}s (%u) BSSID %{sensitive, mask.hash, mdnsresponder:mac_addr}.6P Struct addr %p, primary %p, %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P/%d%{public}s%{public}s%{public}s"
- "Starting the %{public}s enumeration - domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P."
- "State Dump: filename is too long to be put into the buffer, ignoring the current file - file name to be copied: %{sensitive, mask.hash}s, length: %u, buffer length: %u"
- "Stopping the %{public}s enumeration - domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P."
- "Stopping the resolver discovery -- domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "TSR timestamp - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, new: %d  old: %d"
- "The mDNS message does not have enough space for the NSEC record, will add it to the next message (This is not an error message) -- remaining space: %ld, NSEC name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "Tried to register a NetworkInterfaceInfo that's already in the list - ifname: %{public}s, ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "Tried to register a NetworkInterfaceInfo with invalid mask - ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P, ifmask: %{public, mdnsresponder:ip_addr}.20P"
- "Tried to register a NetworkInterfaceInfo with zero InterfaceID - ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "UpdateDeviceInfoRecord Deregister %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "UpdateDeviceInfoRecord Register %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "UpdateQuestionDuplicates transferred LLQ state for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "UpdateQuestionDuplicates transferred nta pointer for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "Using fast activation for DirectLink interface - ifname: %{public}s, ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "[A(%x, %x)] Received %u-byte IPv4 mDNS query from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[A(%x, %x)] Received %u-byte IPv4 mDNS query from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[A(%x, %x)] Received %u-byte IPv6 mDNS query from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[A(%x, %x)] Received %u-byte IPv6 mDNS query from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[A(%x, %x)] Received a previous IPv4 mDNS query from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over multicast via %{public}s/%u"
- "[A(%x, %x)] Received a previous IPv4 mDNS query from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u"
- "[A(%x, %x)] Received a previous IPv6 mDNS query from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over multicast via %{public}s/%u"
- "[A(%x, %x)] Received a previous IPv6 mDNS query from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u"
- "[A(%x, %x)] Sent %u-byte IPv4 mDNS response over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[A(%x, %x)] Sent %u-byte IPv4 mDNS response to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[A(%x, %x)] Sent %u-byte IPv6 mDNS response over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[A(%x, %x)] Sent %u-byte IPv6 mDNS response to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[A(%x, %x)] Sent a previous IPv4 mDNS response to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u"
- "[A(%x, %x)] Sent a previous IPv6 mDNS response to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u"
- "[Q%d] AnswerQuestionByFollowingCNAME: Resolving a .local CNAME -- CNAME: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[Q%u->SubQ%u] DS denial lookup record changes - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, %{mdns:pos/neg}d, %{mdns:addrmv}d, interface index: %d, mortality: %{mdns:mortality}d, ttl: %u"
- "[Q%u->SubQ%u] Insecure validation complete, scheduling cache update - insecure zone: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, ttl: %u"
- "[Q%u->SubQ%u] Possible DS denial found, starting secure DS denial query - DS name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[Q%u->SubQ%u] Searching for DS denial - q_name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[Q%u->SubQ%u] Start insecure validation - unsigned domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[Q%u->SubQ%u] Start to query validated key records to validate the RRSet - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d"
- "[Q%u->SubQ%u] Stop DS denial look up question - DS denial lookup name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[Q%u] %{public}s %{public}s DNS Message %lu bytes from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d via %{public}s (%p)"
- "[Q%u] AnswerQuestionByFollowingCNAME: Not following CNAME referral -- CNAME: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, referral count: %u, self referential: %{mdns:yesno}d"
- "[Q%u] AnswerQuestionByFollowingCNAME: following CNAME referral -- CNAME: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, referral count: %u"
- "[Q%u] CacheRecordRmvEventsForCurrentQuestion: Calling AnswerCurrentQuestionWithResourceRecord (RMV) for question - rr name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %{mdns:rrtype}d, local answers: %u"
- "[Q%u] CacheRecordRmvEventsForCurrentQuestion: Suppressing RMV events for question - rr name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %{mdns:rrtype}d, current active question: Q%d, current answers: %u"
- "[Q%u] Create the denial of existence record set - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{sensitive, mask.hash}s, denial type: %{public}s"
- "[Q%u] Current DNSSEC validation manager contains record(s) that are to be removed soon, wait for the coming update before updating the cache - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[Q%u] DNS %{public}s%{public}s (%lu) (flags %02X%02X) RCODE: %{public}s (%d)%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s:%{sensitive, mask.hash}s %u/%u/%u %{sensitive, mask.hash}s"
- "[Q%u] DNS push discovery finished, using service with SRV name _dns-push-tls._tcp.%{public, mdnsresponder:domain_name}.*P -- service id: %llu, re registered: %{mdns:yesno}d"
- "[Q%u] DNSSEC record changes - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d, rrtype: %{mdns:rrtype}d, %{mdns:pos/neg}d, contains denial: %{mdns:yesno}d, %{mdns:addrmv}d, interface index: %d, motality: %{mdns:mortality}d, original ttl: %u, actual ttl: %u, validated: %{mdns:yesno}d."
- "[Q%u] DNSSEC secure record changes - %{mdns:pos/neg}d, %{mdns:addrmv}d, qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d, rd_len: %u."
- "[Q%u] DetermineUnicastQuerySuppression: Query suppressed for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{public}s%{public}s"
- "[Q%u] Failed to register push service -- id: %lluauthoritative zone: %{public, mdnsresponder:domain_name}.*P, interface index: %u, error: %{mdns:err}ld"
- "[Q%u] Generating RMV events because the question will be stopped - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{public}s."
- "[Q%u] InitDNSConfig: Setting StopTime on the uDNS question %p %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[Q%u] Insecure validation failed - state: %{public, mdns:dnssec_inval_state}u, DS denial lookup name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, DS denial lookup q: Q%d, secure DS denial q: Q%d"
- "[Q%u] New validation key requestor replaces the old one - new name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, old name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d"
- "[Q%u] Sending unicast assist query (refresh %{mdns:yesno}d) - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{mdns:rrtype}d qhash %x"
- "[Q%u] Sending unicast assist query - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %d %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{mdns:rrtype}d qhash %x"
- "[Q%u] Stopping Primary DNSSEC question - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{sensitive, mask.hash}s"
- "[Q%u] The discovered possible denial of existence for DS record points back to the current question itself, insecure delegation validation fails due to possible missing RRSIG of the original response - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[Q%u] The existing validation key requestor can still be reused - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d"
- "[Q%u] Unable to continue the trust chain validation since DS is self-signed - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[Q%u] Unable to create the denial of existence record set - error: %{public}s, qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{sensitive, mask.hash}s, soaRRSIGCount: %u, nsecCount: %u, nsec3Count: %u, rrsigCount: %u."
- "[Q%u] Unable to start DNS push server discovery for the single-label name (TLD) -- qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d"
- "[Q%u] Update cache for DNSSEC question - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d, rr_type: %{mdns:rrtype}d, new original ttl: %u, actual ttl: %u, %{mdns:pos/neg}d, DNSSEC result: %{public, mdns:dnssec_result}u, rescued: %zu, added: %zu, total: %zu, purged: %zu."
- "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s), PID[%d], EUID[%u], ServiceID[%d] evaluator is NULL"
- "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s), PID[%d], EUID[%u], ServiceID[%d] host is NULL"
- "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s), PID[%d], EUID[%u], ServiceID[%d] parameters is NULL"
- "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s), PID[%d], EUID[%u], ServiceID[%d] path is NULL"
- "[Q%u] mDNSPlatformGetDNSRoutePolicy: Query for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P service ID is set ->service_ID:[%d] "
- "[Q%u] mDNSPlatformSendUDP -> sendto(%d) failed to send packet on InterfaceID %p %{public}s/%d to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d skt %d error %ld errno %d (%{public}s) %u"
- "[Q%u] mDNSPlatformSendUDP sendto(%d) failed to send packet on InterfaceID %p %{public}s/%d to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d skt %d error %ld errno %d (%{public}s) %u"
- "[Q%u] mDNSPlatformSendUDP: sendto(%d) failed to send packet on InterfaceID %p %{public}s/%d to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d skt %d error %ld errno %d (%{public}s) %u MessageCount is %d"
- "[Q%u] mDNS_StartQuery_internal START -- qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), qtype: %{mdns:rrtype}d"
- "[Q%u] mDNS_StopQuery_internal STOP -- name hash: %x"
- "[Q%u] setsockopt - IP_MULTICAST_IF error %{sensitive, mask.hash, network:in_addr}.4P %d errno %d (%{public}s)"
- "[Q(%x, %x)] Received %u-byte IPv4 mDNS response from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[Q(%x, %x)] Received %u-byte IPv4 mDNS response from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[Q(%x, %x)] Received %u-byte IPv6 mDNS response from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[Q(%x, %x)] Received %u-byte IPv6 mDNS response from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[Q(%x, %x)] Received a previous IPv4 mDNS response from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over multicast via %{public}s/%u"
- "[Q(%x, %x)] Received a previous IPv4 mDNS response from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u"
- "[Q(%x, %x)] Received a previous IPv6 mDNS response from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over multicast via %{public}s/%u"
- "[Q(%x, %x)] Received a previous IPv6 mDNS response from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u"
- "[Q(%x, %x)] Sent %u-byte IPv4 mDNS query over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[Q(%x, %x)] Sent %u-byte IPv4 mDNS query to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[Q(%x, %x)] Sent %u-byte IPv6 mDNS query over multicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[Q(%x, %x)] Sent %u-byte IPv6 mDNS query to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX %{sensitive, mask.hash, mdnsresponder:mdns_name_hash_type_bytes}.*P"
- "[Q(%x, %x)] Sent a previous IPv4 mDNS query to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u"
- "[Q(%x, %x)] Sent a previous IPv6 mDNS query to %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P over unicast via %{public}s/%u"
- "[R%u->(Q%u, Q%u)] DNSServiceResolve NoSuchRecord -- instance: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%{sensitive}x), split AWDL query: %{mdns:yesno}d"
- "[R%u->(Q%u, Q%u)] DNSServiceResolve RESULT -- instance: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%{sensitive}x), ifindex: %u, target host: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%{sensitive}x), port: %u, negative txt: %{mdns:yesno}d, txt rdlength: %u, split AWDL query: %{mdns:yesno}d"
- "[R%u->DupQ%d->Q%d] UpdateQuestionDuplicates: question %p %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) duplicate of %p %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u->DupQ%u->Q%u] Duplicate question %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u->Q%d] AnswerNewQuestion ERROR m->CurrentQuestion already set: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u->Q%d] DNSServiceEnumerateDomains(%{sensitive, mask.hash, mdnsresponder:domain_label}.*P) RESULT %{mdns:addrmv_upper}d: %{sensitive, mask.hash}s"
- "[R%u->Q%u->subQ%u] Stop getting the zone data - zone qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, zone qtype: %{public}s."
- "[R%u->Q%u] Cleared resolver UUID for question: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Q%u] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Q%u] InitDNSConfig: Setting StopTime on the uDNS question %p %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u->Q%u] Not starting long-lived query polling since the question has been stopped - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{public}s, LLQ_State: %{public}s."
- "[R%u->Q%u] Question for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s%{public}s) assigned DNS service -- %@"
- "[R%u->Q%u] Restarting question that got expired CNAMEs -- current name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, original name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d"
- "[R%u->Q%u] Retrying path evaluation -- qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{public}s, reason: %{public}s"
- "[R%u->Q%u] Starting long-lived query polling - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{public}s, LLQ_State: %{public}s."
- "[R%u->Q%u] mDNSCoreReceiveNoUnicastAnswers: Generate negative response for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u->Q%u] mDNSCoreReceiveNoUnicastAnswers: Renewing negative TTL from %u to %u %{sensitive, mask.hash}s"
- "[R%u->Q%u] mDNSCoreReceiveNoUnicastAnswers: Skipping check and not creating a negative cache entry for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u->Q%u] mDNS_StopQuery_internal: Question %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) not found in active list."
- "[R%u->Q%u] queryrecord_result_reply add tracker %{sensitive, mask.hash}s"
- "[R%u->Rec%u] DNSServiceRegisterRecord Result -- event: %{public, mdnsresponder:reg_result}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Rec%u] DNSServiceRegisterRecord Result -- event: %{public, mdnsresponder:reg_result}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Rec%u] DNSServiceRegisterRecord Result -- event: %{public, mdnsresponder:reg_result}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Rec%u] DNSServiceRegisterRecord Result -- event: %{public, mdnsresponder:reg_result}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Rec%u] DNSServiceRegisterRecord START -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, "
- "[R%u->Rec%u] DNSServiceRegisterRecord START -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), "
- "[R%u->Rec%u] DNSServiceRegisterRecord START -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u->Rec%u] DNSServiceRegisterRecord START -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, name hash: %x"
- "[R%u->Rec%u] DNSServiceRegisterRecord STOP -- name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u->Rec%u] DNSServiceRegisterRecord STOP -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), index: %d, client: %{public}s(pid: %d), duration: %{mdns:time_duration}utype: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Rec%u] DNSServiceRegisterRecord STOP -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), index: %d, client: %{public}s(pid: %d), duration: %{mdns:time_duration}utype: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Rec%u] DNSServiceRemoveRecord -- ifindex: %d, client pid: %d (%{public}s), duration: %{mdns:time_duration}u, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->Rec%u] DNSServiceRemoveRecord -- ifindex: %d, client pid: %d (%{public}s), duration: %{mdns:time_duration}u, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->Rec%u] DNSServiceRemoveRecord -- name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceBrowse result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceGetAddrInfo result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceQueryRecord result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceRegisterRecord Result -- record %u, event: ERROR, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceRegisterRecord Result -- record %u, event: ERROR, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceRegisterRecord Result -- record %u, event: ERROR, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceRegisterRecord Result -- record %u, event: ERROR, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name hash: %x, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), dnssec: %{public, mdns:dnssec_result}u, type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "[R%u->mDNS] DNSServiceResolve result -- event: %{mdns:addrmv}d, expired: %{mdns:yesno}d, ifindex: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "[R%u] DNSServiceAddRecord(%X, %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, %{public}s, %d) PID[%d](%{public}s)"
- "[R%u] DNSServiceBrowse -> SubBrowser START -- qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x)"
- "[R%u] DNSServiceBrowse Cancel domain enumeration for WAB and mDNS -- , duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceBrowse Cancel domain enumeration for WAB and mDNS -- , flags: 0x%X, interface index: %d, client pid: %d (%{public}s), , duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceBrowse START -- "
- "[R%u] DNSServiceBrowse START -- service type: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, domain: %{sensitive, mask.hash}s, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), "
- "[R%u] DNSServiceBrowse STOP -- name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceBrowse STOP -- service name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceGetAddrInfo START -- hostname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, protocols: %u, DNSSEC enabled, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u] DNSServiceGetAddrInfo START -- hostname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, protocols: %u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u] DNSServiceGetAddrInfo START -- name hash: %x"
- "[R%u] DNSServiceGetAddrInfo STOP -- hostname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceGetAddrInfo STOP -- name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceGetAddrInfo: Signed result does not cover hostname: %{sensitive, mask.hash}s, ifindex: %u."
- "[R%u] DNSServiceNATPortMappingCreate(%X, %u, %u, %u) RESULT %{sensitive, mask.hash, network:in_addr}.4P:%u TTL %u"
- "[R%u] DNSServiceQueryRecord START -- name hash: %x"
- "[R%u] DNSServiceQueryRecord START -- qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d, DNSSEC enabled, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u] DNSServiceQueryRecord START -- qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u] DNSServiceQueryRecord STOP -- name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceQueryRecord STOP -- qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceReconfirmRecord FAILED -- name hash: %x"
- "[R%u] DNSServiceReconfirmRecord FAILED -- rr name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %{mdns:rrtype}d, error: %d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), "
- "[R%u] DNSServiceReconfirmRecord FAILED -- rr name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %{mdns:rrtype}d, error: %d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u] DNSServiceReconfirmRecord START -- name hash: %x"
- "[R%u] DNSServiceReconfirmRecord START -- rr name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), "
- "[R%u] DNSServiceReconfirmRecord START -- rr name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %{mdns:rrtype}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u] DNSServiceRegister START -- name hash: %x"
- "[R%u] DNSServiceRegister START -- service type: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, port: %u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u] DNSServiceRegister STOP -- SRV name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), port: %u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceRegister STOP -- name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceRegister result -- event: ADDED, SRV name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), port: %u, PTR name hash: %x"
- "[R%u] DNSServiceRegister(%{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), %u) %s"
- "[R%u] DNSServiceRemoveRecord(%{sensitive, mask.hash, mdnsresponder:domain_name}.*P, %{public}s) PID[%d](%{public}s): %d"
- "[R%u] DNSServiceResolve START -- SRV name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, split AWDL query: %{mdns:yesno}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x"
- "[R%u] DNSServiceResolve START -- name hash: %x"
- "[R%u] DNSServiceResolve STOP -- SRV name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, split AWDL query: %{mdns:yesno}d, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceResolve STOP -- name hash: %x, duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceResolve: Signed result does not cover service: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, ifindex: %u."
- "[R%u] DNSServiceUpdateRecord(%{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), %{mdns:rrtype}d) UPDATE PID[%d](%s)"
- "[R%u] DNSServiceUpdateRecord(%{sensitive, mask.hash, mdnsresponder:domain_name}.*P, %{public}s%{public}s) PID[%d](%{public}s)"
- "[R%u] ERROR: QueryRecordOpStartQuestion mDNS_StartQuery for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{public}s failed with error %d"
- "[R%u] ERROR: bad domain name '%{sensitive, mask.hash}s'"
- "[R%u] ERROR: bad hostname '%{sensitive, mask.hash}s'"
- "[R%u] PeerConnectionRelease(%X %{sensitive, mask.hash, mdnsresponder:domain_name}.*P) START PID[%d](%{public}s)"
- "[R%u] QueryRecordOpCallback: Question %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) answering local with negative unicast response"
- "[R%u] QueryRecordOpCallback: Question %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) timing out, InterfaceID %p"
- "[R%u] QueryRecordOpCallback: Suppressed question %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u] QueryRecordOpStart: starting parallel unicast query for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{public}s"
- "[R%u] Restarting question for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) due to DNS service failover"
- "[R%u] Restarting question for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P AAAA record as question for A record (RCODE %d)"
- "[R%u] Signed resolve result does not cover request -- hostname: %{private,mask.hash}s, ifindex: %u"
- "[R%u] getaddrinfo error -- hostname: %{private,mask.hash}s, error: %{mdns:err}ld, client pid: %lld (%{public}s)"
- "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{private,mask.hash}s, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s)"
- "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{private,mask.hash}s, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s), delegator pid: %lld (%{public}s)"
- "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{private,mask.hash}s, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s), delegator uuid: %{public,uuid_t}.16P"
- "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{sensitive,mask.hash}s, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s)"
- "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{sensitive,mask.hash}s, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s), delegator pid: %lld (%{public}s)"
- "[R%u] getaddrinfo start -- flags: 0x%X, ifindex: %d, protocols: %u, hostname: %{sensitive,mask.hash}s, options: %{mdns:gaiopts}X, client pid: %lld (%{public}s), delegator uuid: %{public,uuid_t}.16P"
- "[R%u] getaddrinfo stop (forced) -- hostname: %{private,mask.hash}s, client pid: %lld (%{public}s)"
- "[R%u] getaddrinfo stop (forced) -- hostname: %{sensitive,mask.hash}s, client pid: %lld (%{public}s)"
- "[R%u] getaddrinfo stop -- hostname: %{private,mask.hash}s, client pid: %lld (%{public}s)"
- "[R%u] getaddrinfo stop -- hostname: %{sensitive,mask.hash}s, client pid: %lld (%{public}s)"
- "[R%u] handle_regrecord_request: TSR fail, removing %{sensitive, mask.hash}s (%p), InterfaceID %p"
- "[R%u] mDNS_StartBrowse returned error (UNICAST_DISCOVERY) -- error: %d, type: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "[R%u] read_rr_from_ipc_msg: SetRData failed for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[R%u] regRecordAddTSRRecord(0x%X, %d, %{sensitive, mask.hash}s) START PID[%d](%{public}s)"
- "[R%u] regRecordAddTSRRecord(0x%X, %d,%{sensitive, mask.hash}s) ERROR (%d)"
- "[R%u] regservice_callback: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P is not valid DNS-SD SRV name"
- "[R%u] update_record: SetRData failed for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "[Sub%llu] Collectively removing record(s) -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d"
- "[Sub%llu] Removing record from the cache due to subscriber invalidation -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, TTL: %us"
- "conflictWithAuthRecordsOrFlush - Conflict with %{sensitive, mask.hash}s (%p), InterfaceID %p"
- "conflictWithAuthRecordsOrFlush - deregistering %{sensitive, mask.hash}s InterfaceID %p"
- "conflictWithCacheRecordsOrFlush - new TSR, flushing interface %d %{sensitive, mask.hash}s"
- "external_start_resolving_service - fqdn: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "external_stop_resolving_service - fqdn: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "handle_regrecord_request: Name conflict %{sensitive, mask.hash}s InterfaceID %p"
- "handle_regrecord_request: TSR Stale Data, record cache is newer %{sensitive, mask.hash, mdnsresponder:domain_name}.*P InterfaceID %p"
- "handle_regrecord_request: TSR Stale data, auth cache is newer %{sensitive, mask.hash}s InterfaceID %p"
- "i16@?0^{nw_framer=}8"
- "internal_start_advertising_service - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rrtype: %{mdns:rrtype}d"
- "internal_start_browsing_for_service: starting browse - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d"
- "internal_stop_advertising_service: %{sensitive, mask.hash}s"
- "internal_stop_browsing_for_service: stopping browse - qname: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %{mdns:rrtype}d"
- "intf->InterfaceActive already set for interface - ifname: %{public}s, ifaddr: %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "mDNSCoreMachineSleep: %{sensitive, mask.hash}s: Adjusted the remain ttl %d by %d seconds"
- "mDNSCoreMachineSleep: %{sensitive, mask.hash}s: Purging after adjusting the remaining TTL %d by %d seconds"
- "mDNSCoreMachineSleep: %{sensitive, mask.hash}s: Purging cache entry SleptTime %d, Remaining TTL %d"
- "mDNSCoreReceiveCacheCheck: Discarding (%{public}s) %{sensitive, mask.hash}s rrtype change from (%{public}s%{public}s) to (%{public}s%{public}s)"
- "mDNSCoreReceiveCacheCheck: Discarding due to domainname case change new: %{sensitive, mask.hash}s"
- "mDNSCoreReceiveCacheCheck: Discarding due to domainname case change old: %{sensitive, mask.hash}s"
- "mDNSCoreReceiveCacheCheck: Keeping Standard TTL for %{sensitive, mask.hash}s %p"
- "mDNSCoreReceiveCacheCheck: rescuing RR with new TTL %u: %{sensitive, mask.hash}s"
- "mDNSCoreReceiveNoUnicastAnswers: Removing expired record%{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse - deregistering %{sensitive, mask.hash, mdnsresponder:domain_name}.*P type %{public}s on interface %d due to TSR conflict"
- "mDNSCoreReceiveResponse - flushed interface %d %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse - flushing cache group %{sensitive, mask.hash, mdnsresponder:domain_name}.*P type %{public}s on interface %d due to TSR conflict"
- "mDNSCoreReceiveResponse: Already reset to Probing: %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse: Dep Record: %08X %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse: Ignoring response received before we even began probing: %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse: Our Record: %08X %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse: Pkt Record: %08X %{sensitive, mask.hash}s (interface %d)"
- "mDNSCoreReceiveResponse: ProbeCount %u; restarting probing after %d-tick pause due to possibly spurious multicast conflict (%d/%d) via interface %d for %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse: ProbeCount %u; will deregister %{sensitive, mask.hash}s due to %{public}scast conflict via interface %d"
- "mDNSCoreReceiveResponse: Received from %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse: Resetting to Probing: %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse: Unexpected conflict discarding %{sensitive, mask.hash}s"
- "mDNSCoreReceiveResponse: Unexpected record type %X %{sensitive, mask.hash}s"
- "mDNSPlatformValidRecordForInterface: Filtering privacy risk -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, ifname: %{public}s, ifid: %d"
- "mDNSPreferencesSetNames: changing computer name -- last change: %{sensitive, mask.hash, mdnsresponder:domain_label}.*P -> %{sensitive, mask.hash, mdnsresponder:domain_label}.*P, current change: %{sensitive, mask.hash, mdnsresponder:domain_label}.*P -> %{sensitive, mask.hash, mdnsresponder:domain_label}.*P"
- "mDNSPreferencesSetNames: changing local host name -- last change: %{sensitive, mask.hash, mdnsresponder:domain_label}.*P -> %{sensitive, mask.hash, mdnsresponder:domain_label}.*P, current change: %{sensitive, mask.hash, mdnsresponder:domain_label}.*P -> %{sensitive, mask.hash, mdnsresponder:domain_label}.*P"
- "mDNSResponder-2881.120.11"
- "mDNS_AddMcastResolver: Adding %{public, mdnsresponder:domain_name}.*P, InterfaceID %p, timeout %u"
- "mDNS_AddSearchDomain: domain already in list -- search domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "mDNS_AddSearchDomain: new search domain added -- search domain: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, InterfaceID %p"
- "mDNS_Deregister_internal: %{sensitive, mask.hash}s already marked kDNSRecordTypeDeregistering"
- "mDNS_Deregister_internal: %{sensitive, mask.hash}s already marked kDNSRecordTypeUnregistered"
- "mDNS_Deregister_internal: ERROR!! cannot insert %{sensitive, mask.hash}s"
- "mDNS_Deregister_internal: Purging cached record that matches deregistered AuthRecord -- interface: %{public}s/%u, record: %{sensitive, mask.hash}s"
- "mDNS_Deregister_internal: Record %p not found in list %{sensitive, mask.hash}s"
- "mDNS_Deregister_internal: callback with mStatus_MemFree for %{sensitive, mask.hash}s"
- "mDNS_FinalExit failed to send goodbye for: %p %02X %{sensitive, mask.hash}s"
- "mDNS_PurgeBeforeResolve: Flushing %{sensitive, mask.hash}s"
- "mDNS_Register_internal: Diverting record to local-only %{sensitive, mask.hash}s"
- "mDNS_Register_internal: ERROR! %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s): rr->DependentOn && RecordType != kDNSRecordTypeUnique or kDNSRecordTypeKnownUnique"
- "mDNS_Register_internal: ERROR! %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s): rr->DependentOn->RecordType bad type %X"
- "mDNS_Register_internal: ERROR!! Tried to register AuthRecord %p %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) that's already in the Duplicate list"
- "mDNS_Register_internal: ERROR!! Tried to register AuthRecord %p %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) that's already in the list"
- "mDNS_Register_internal: ERROR!! Tried to register LocalOnly AuthRecord %p %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) that's already in the list"
- "mDNS_Register_internal: Name conflict %{sensitive, mask.hash}s (%p), InterfaceID %p"
- "mDNS_Register_internal: RecordType must be non-zero %{sensitive, mask.hash}s"
- "mDNS_Register_internal: Shutting down, can't register %{sensitive, mask.hash}s"
- "mDNS_Register_internal: TTL %X should be 1 - 0x7FFFFFFF %{sensitive, mask.hash}s"
- "mDNS_Register_internal: adding to active record list -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "mDNS_Register_internal: adding to active record list -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "mDNS_Register_internal: adding to duplicate list -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P"
- "mDNS_Register_internal: adding to duplicate list -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), type: %{mdns:rrtype}d, rdata: <none>"
- "mDNS_Register_internal: record %{public}s in NoTarget state"
- "mDNS_RemoveDynDNSHostName %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "mDNS_RemoveDynDNSHostName removing v4 %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "mDNS_RemoveDynDNSHostName removing v6 %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "mDNS_RemoveDynDNSHostName: no such domainname %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "mDNS_StartExit: ERROR m->CurrentRecord already set %{sensitive, mask.hash}s"
- "mDNS_StartExit: Should not still have Duplicate Records remaining: %02X %{sensitive, mask.hash}s"
- "mDNS_StartQuery_internal: Error! Tried to add a question %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s) %p that's already in the active list"
- "mDNS_StopQuery_internal: Just deleted the current restart question: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{public}s)"
- "refresh"
- "register_service_instance: TSR Stale Data, record cache is newer %{sensitive, mask.hash, mdnsresponder:domain_name}.*P InterfaceID %p"
- "register_service_instance: TSR Stale data, auth cache is newer %{sensitive, mask.hash}s InterfaceID %p"
- "tcpConnectionCallback: DeviceDescription SOAP address %{sensitive, mask.hash}s SOAP path %{sensitive, mask.hash}s"
- "tcpConnectionCallback: tcpInfo->Address:Port [%{sensitive, mask.hash, mdnsresponder:ip_addr}.20P:%d] tcpInfo->op[%u] tcpInfo->retries[%d] tcpInfo->Request[%{sensitive, mask.hash}s] tcpInfo->Reply[%{sensitive, mask.hash}s]"
- "tsrTimestamp[%u] out of range (%d) on TSR for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "uDNSDeregisterRecord: Cannot find the anchor Resource Record for %{sensitive, mask.hash}s, not an error"
- "uDNS_DeregisterRecord: ERROR!! QueuedRData same as rdata for %{sensitive, mask.hash}s"
- "uDNS_DeregisterRecord: ERROR: Another anchorRR %{sensitive, mask.hash}s found"
- "uDNS_DeregisterRecord: Found Anchor RR %{sensitive, mask.hash}s terminated"
- "uDNS_DeregisterRecord: Freeing InFlightRData for %{sensitive, mask.hash}s"
- "uDNS_DeregisterRecord: Freeing QueuedRData for %{sensitive, mask.hash}s"
- "uDNS_DeregisterRecord: InFlightRData same as rdata for %{sensitive, mask.hash}s"
- "uDNS_DeregisterRecord: Resource Record %{sensitive, mask.hash}s, state %u"
- "uDNS_DeregisterRecord: State %u for %{sensitive, mask.hash, mdnsresponder:domain_name}.*P type %{public}s"
- "uDNS_SetupWABQueries -- action: 0x%x, flags: 0x%x, ifid: %p, domain: %{public, mdnsresponder:domain_name}.*P (%x)"
- "uDNS_SetupWABQueries: DELETE Browse for domain -- name hash: %x"
- "uDNS_SetupWABQueries: DELETE Deregistering PTR -- record: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P PTR %{sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "uDNS_SetupWABQueries: DELETE Legacy Browse for domain -- name hash: %x"
- "uDNS_SetupWABQueries: DELETE Registration for domain -- name hash: %x"
- "uDNS_SetupWABQueries: Deleting Browse for domain -- name hash: %x"
- "uDNS_SetupWABQueries: Deleting Legacy Browse for domain -- name hash: %x"
- "uDNS_SetupWABQueries: Deleting Registration for domain -- name hash: %x"
- "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowse) returned error -- name hash: %x, error: %d"
- "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowseAutomatic) returned error -- name hash: %x, error: %d"
- "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowseDefault) returned error -- name hash: %x, error: %d"
- "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeRegistration) returned error -- name hash: %x, error: %d"
- "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeRegistrationDefault) returned error -- name hash: %x, error: %d"
- "uDNS_SetupWABQueries: Starting Browse for domain -- name hash: %x"
- "uDNS_SetupWABQueries: Starting Default Browse for domain -- name hash: %x"
- "uDNS_SetupWABQueries: Starting Default Registration for domain -- name hash: %x"
- "uDNS_SetupWABQueries: Starting Legacy Browse for domain -- name hash: %x"
- "uDNS_SetupWABQueries: Starting Registration for domain -- name hash: %x"
- "uDNS_Tasks ERROR m->CurrentQuestion already set: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%{sensitive, mask.hash}s)"
- "unicast assist (restart) - no active question for qnamehash %x"
- "unicast assist _addRecordsFromPresence: (error) qhash %x addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P err %d"
- "unicast assist _addRecordsFromPresence: add qhashes %@ addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P ifhash %x"
- "unicast assist _addRecordsFromPresence: no subnet for addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "unicast assist _addRecordsFromPresence: restarted (%s) qhash %x addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
- "unicast assist persistance cache read failed (next qhash) addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P ifhash %x ifid %2.2u"
- "unicast assist persistance cache save failed addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P ifhash %x ifid %2.2u"
- "unicast assist persistance cache save failed qhash %x %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P ifhash %x ifid %2.2u"
- "unicast assist qhash (%s) keeping presence - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P qhash %x"
- "unicast assist qhash flushed (%s) - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P qhash %x"
- "unicast assist qhash flushed (overflow) - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P qhash %x"
- "unicast assist record %s %s%s - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %2.2u %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{public}s qhash %x rectype 0x%X%s"
- "unicast assist record flushed (0 qhashes) - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %2.2u ifhash %x"
- "v36@?0^{nw_framer=}8^{nw_protocol_metadata=}16Q24B32"
- "xD2DAddToCache: mDNS_Register failed - error: %d, name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, auth record: %{sensitive, mask.hash}s"
- "xD2DAddToCache: mDNS_Register succeeded - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, Interface ID: %p, auth record: %{sensitive, mask.hash}s"
- "xD2DClearCache: Clearing and deregistering cache record - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rrtype: %{mdns:rrtype}d, auth record: %{sensitive, mask.hash}s"
- "xD2DFindInList: Could not find in D2DRecords - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, auth record: %{sensitive, mask.hash}s"
- "xD2DParse got record - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, rrtype: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash}s"
- "xD2DParseCompressedPacket: Our Bytes - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, TTL: %u, rdata length: %u"
- "xD2DRemoveFromCache: removing record from cache - name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, auth record: %{sensitive, mask.hash}s"
- "«REDACTED HOSTNAME»"

```
