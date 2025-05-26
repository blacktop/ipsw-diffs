## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2200.80.16.0.0
-  __TEXT.__text: 0xf9618
-  __TEXT.__auth_stubs: 0x2d70
-  __TEXT.__objc_stubs: 0x1140
+2200.100.94.0.2
+  __TEXT.__text: 0xfb654
+  __TEXT.__auth_stubs: 0x2d30
+  __TEXT.__objc_stubs: 0x1200
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__cstring: 0x19400
+  __TEXT.__cstring: 0x1969c
   __TEXT.__const: 0xdd0
-  __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__oslogstring: 0x1a1dc
-  __TEXT.__objc_classname: 0x588
-  __TEXT.__objc_methname: 0x101b
-  __TEXT.__objc_methtype: 0x5ec
-  __TEXT.__unwind_info: 0x1644
+  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__oslogstring: 0x1a3e7
+  __TEXT.__objc_classname: 0x5b1
+  __TEXT.__objc_methname: 0x10c9
+  __TEXT.__objc_methtype: 0x52d
+  __TEXT.__unwind_info: 0x1668
   __TEXT.__eh_frame: 0x7c
-  __DATA_CONST.__auth_got: 0x16c8
+  __DATA_CONST.__auth_got: 0x16a8
   __DATA_CONST.__got: 0x300
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x5890
-  __DATA_CONST.__cfstring: 0x1060
-  __DATA_CONST.__objc_classlist: 0x1a8
-  __DATA_CONST.__objc_protolist: 0x1c8
+  __DATA_CONST.__const: 0x5a40
+  __DATA_CONST.__cfstring: 0x10c0
+  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x3b00
-  __DATA.__objc_selrefs: 0x488
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0x3c08
+  __DATA.__objc_selrefs: 0x4b8
   __DATA.__objc_classrefs: 0x130
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_data: 0x1090
-  __DATA.__data: 0x4150
-  __DATA.__bss: 0x16828
+  __DATA.__objc_data: 0x10e0
+  __DATA.__data: 0x41b0
+  __DATA.__bss: 0x16848
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/DeviceToDeviceManager
-  - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1737
-  Symbols:   4100
-  CStrings:  4533
+  Functions: 1758
+  Symbols:   4140
+  CStrings:  4582
 
Symbols:
+ +[DNSHeuristics clearNetworkAsFiltered:]
+ +[DNSHeuristics setNetworkAsFiltered:]
+ +[DNSHeuristics setNetworkAsFiltered:filtered:]
+ +[DNSHeuristics setNetworkSettings:value:]
+ FreeARElemCallback.2844
+ GCC_except_table1063
+ GCC_except_table108
+ GCC_except_table112
+ GCC_except_table1255
+ GCC_except_table1449
+ _OBJC_CLASS_$_OS_mrcs_dns_service_registration_request
+ _OBJC_METACLASS_$_OS_mrcs_dns_service_registration_request
+ _Querier_RegisterNativeDNSService
+ __Block_byref_object_copy_.898
+ __Block_byref_object_dispose_.899
+ __OBJC_$_PROP_LIST_OS_mrcs_dns_service_registration_request
+ __OBJC_$_PROTOCOL_REFS_OS_mrcs_dns_service_registration_request
+ __OBJC_CLASS_PROTOCOLS_$_OS_mrcs_dns_service_registration_request
+ __OBJC_CLASS_RO_$_OS_mrcs_dns_service_registration_request
+ __OBJC_LABEL_PROTOCOL_$_OS_mrcs_dns_service_registration_request
+ __OBJC_METACLASS_RO_$_OS_mrcs_dns_service_registration_request
+ __OBJC_PROTOCOL_$_OS_mrcs_dns_service_registration_request
+ __Querier_DNSServiceRegistrationStartHandler
+ __Querier_DNSServiceRegistrationStopHandler
+ ___dnssd_server_init_block_invoke_3
+ ___getHeuristicsQueue_block_invoke
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6176
+ ___mdns_server_log_block_invoke.4454
+ ___mrcs_server_activate_block_invoke
+ ___mrcs_server_set_dns_proxy_handlers_block_invoke
+ ___mrcs_server_set_dns_service_registration_handlers_block_invoke
+ __block_descriptor_tmp.1.6141
+ __block_descriptor_tmp.10.4661
+ __block_descriptor_tmp.10.6171
+ __block_descriptor_tmp.10.7171
+ __block_descriptor_tmp.11.4453
+ __block_descriptor_tmp.11.5994
+ __block_descriptor_tmp.11.6509
+ __block_descriptor_tmp.113
+ __block_descriptor_tmp.12.1035
+ __block_descriptor_tmp.12.247
+ __block_descriptor_tmp.12.5996
+ __block_descriptor_tmp.12.6506
+ __block_descriptor_tmp.12.858
+ __block_descriptor_tmp.13.6756
+ __block_descriptor_tmp.13.860
+ __block_descriptor_tmp.14.3470
+ __block_descriptor_tmp.14.4669
+ __block_descriptor_tmp.14.5969
+ __block_descriptor_tmp.14.882
+ __block_descriptor_tmp.144.3799
+ __block_descriptor_tmp.15.5977
+ __block_descriptor_tmp.15.6168
+ __block_descriptor_tmp.15.6757
+ __block_descriptor_tmp.15.965
+ __block_descriptor_tmp.159.4861
+ __block_descriptor_tmp.16.4397
+ __block_descriptor_tmp.16.4437
+ __block_descriptor_tmp.1672
+ __block_descriptor_tmp.17.3473
+ __block_descriptor_tmp.17.4280
+ __block_descriptor_tmp.17.6499
+ __block_descriptor_tmp.17.6759
+ __block_descriptor_tmp.1731
+ __block_descriptor_tmp.18.4673
+ __block_descriptor_tmp.18.6513
+ __block_descriptor_tmp.18.6760
+ __block_descriptor_tmp.184.2857
+ __block_descriptor_tmp.19.4400
+ __block_descriptor_tmp.19.5970
+ __block_descriptor_tmp.19.6761
+ __block_descriptor_tmp.19.937
+ __block_descriptor_tmp.2.4342
+ __block_descriptor_tmp.2.6174
+ __block_descriptor_tmp.20.1032
+ __block_descriptor_tmp.20.4449
+ __block_descriptor_tmp.20.5974
+ __block_descriptor_tmp.20.6765
+ __block_descriptor_tmp.209.5706
+ __block_descriptor_tmp.21.3475
+ __block_descriptor_tmp.21.5967
+ __block_descriptor_tmp.213.5801
+ __block_descriptor_tmp.22.1741
+ __block_descriptor_tmp.22.4667
+ __block_descriptor_tmp.228.5708
+ __block_descriptor_tmp.23.1748
+ __block_descriptor_tmp.233
+ __block_descriptor_tmp.238
+ __block_descriptor_tmp.24.1749
+ __block_descriptor_tmp.24.3512
+ __block_descriptor_tmp.247
+ __block_descriptor_tmp.25.3430
+ __block_descriptor_tmp.25.5989
+ __block_descriptor_tmp.25.6753
+ __block_descriptor_tmp.251
+ __block_descriptor_tmp.255
+ __block_descriptor_tmp.2556
+ __block_descriptor_tmp.26.1750
+ __block_descriptor_tmp.261
+ __block_descriptor_tmp.265
+ __block_descriptor_tmp.27.1751
+ __block_descriptor_tmp.27.3431
+ __block_descriptor_tmp.27.4665
+ __block_descriptor_tmp.2702
+ __block_descriptor_tmp.28.940
+ __block_descriptor_tmp.280
+ __block_descriptor_tmp.284
+ __block_descriptor_tmp.2858
+ __block_descriptor_tmp.29.1753
+ __block_descriptor_tmp.29.5987
+ __block_descriptor_tmp.3.1735
+ __block_descriptor_tmp.3.2706
+ __block_descriptor_tmp.3.4321
+ __block_descriptor_tmp.3.6003
+ __block_descriptor_tmp.3.6144
+ __block_descriptor_tmp.3.6501
+ __block_descriptor_tmp.3.7291
+ __block_descriptor_tmp.3.971
+ __block_descriptor_tmp.30.5986
+ __block_descriptor_tmp.306
+ __block_descriptor_tmp.31.3427
+ __block_descriptor_tmp.31.5985
+ __block_descriptor_tmp.310
+ __block_descriptor_tmp.312
+ __block_descriptor_tmp.316
+ __block_descriptor_tmp.32.5965
+ __block_descriptor_tmp.33.1014
+ __block_descriptor_tmp.33.1756
+ __block_descriptor_tmp.33.5983
+ __block_descriptor_tmp.34.1022
+ __block_descriptor_tmp.34.1764
+ __block_descriptor_tmp.3401
+ __block_descriptor_tmp.341
+ __block_descriptor_tmp.35.1763
+ __block_descriptor_tmp.36.3408
+ __block_descriptor_tmp.3649
+ __block_descriptor_tmp.37.1760
+ __block_descriptor_tmp.37.3423
+ __block_descriptor_tmp.37.4678
+ __block_descriptor_tmp.3722
+ __block_descriptor_tmp.39.4675
+ __block_descriptor_tmp.4.4439
+ __block_descriptor_tmp.4.4880
+ __block_descriptor_tmp.4.6004
+ __block_descriptor_tmp.4.6148
+ __block_descriptor_tmp.40.3420
+ __block_descriptor_tmp.41.1758
+ __block_descriptor_tmp.41.4660
+ __block_descriptor_tmp.4282
+ __block_descriptor_tmp.4312
+ __block_descriptor_tmp.4339
+ __block_descriptor_tmp.44.4646
+ __block_descriptor_tmp.4435
+ __block_descriptor_tmp.45.1755
+ __block_descriptor_tmp.4561
+ __block_descriptor_tmp.46.1021
+ __block_descriptor_tmp.46.4642
+ __block_descriptor_tmp.46.7211
+ __block_descriptor_tmp.47.3478
+ __block_descriptor_tmp.47.5404
+ __block_descriptor_tmp.4718
+ __block_descriptor_tmp.49.1012
+ __block_descriptor_tmp.49.4881
+ __block_descriptor_tmp.5.4442
+ __block_descriptor_tmp.5.4886
+ __block_descriptor_tmp.5.6005
+ __block_descriptor_tmp.50.1019
+ __block_descriptor_tmp.50.4748
+ __block_descriptor_tmp.50.7204
+ __block_descriptor_tmp.51.4747
+ __block_descriptor_tmp.5170
+ __block_descriptor_tmp.52.4655
+ __block_descriptor_tmp.524
+ __block_descriptor_tmp.53
+ __block_descriptor_tmp.5392
+ __block_descriptor_tmp.55.1009
+ __block_descriptor_tmp.56
+ __block_descriptor_tmp.58.979
+ __block_descriptor_tmp.5804
+ __block_descriptor_tmp.6.1769
+ __block_descriptor_tmp.6.6152
+ __block_descriptor_tmp.6.6179
+ __block_descriptor_tmp.6.7161
+ __block_descriptor_tmp.6.968
+ __block_descriptor_tmp.604.4188
+ __block_descriptor_tmp.6137
+ __block_descriptor_tmp.6162
+ __block_descriptor_tmp.6217
+ __block_descriptor_tmp.63
+ __block_descriptor_tmp.64.984
+ __block_descriptor_tmp.6492
+ __block_descriptor_tmp.67.4721
+ __block_descriptor_tmp.6718
+ __block_descriptor_tmp.6771
+ __block_descriptor_tmp.6813
+ __block_descriptor_tmp.683
+ __block_descriptor_tmp.69.4722
+ __block_descriptor_tmp.6958
+ __block_descriptor_tmp.7.4310
+ __block_descriptor_tmp.7.4910
+ __block_descriptor_tmp.7.6155
+ __block_descriptor_tmp.7.832
+ __block_descriptor_tmp.70.4758
+ __block_descriptor_tmp.71.4754
+ __block_descriptor_tmp.7155
+ __block_descriptor_tmp.72.4752
+ __block_descriptor_tmp.7287
+ __block_descriptor_tmp.7523
+ __block_descriptor_tmp.7538
+ __block_descriptor_tmp.8.4308
+ __block_descriptor_tmp.8.4446
+ __block_descriptor_tmp.8.6494
+ __block_descriptor_tmp.8.841
+ __block_descriptor_tmp.826
+ __block_descriptor_tmp.9.1034
+ __block_descriptor_tmp.9.4315
+ __block_descriptor_tmp.9.5993
+ __block_descriptor_tmp.92.4827
+ __block_descriptor_tmp.961
+ __block_descriptor_tmp.97.4799
+ __block_literal_global.10
+ __block_literal_global.104.765
+ __block_literal_global.11.2424
+ __block_literal_global.12.6164
+ __block_literal_global.12.7167
+ __block_literal_global.13
+ __block_literal_global.14.6493
+ __block_literal_global.141
+ __block_literal_global.146
+ __block_literal_global.15.7409
+ __block_literal_global.1631
+ __block_literal_global.17.6166
+ __block_literal_global.1726
+ __block_literal_global.18
+ __block_literal_global.20.4671
+ __block_literal_global.22.6762
+ __block_literal_global.240
+ __block_literal_global.2412
+ __block_literal_global.249
+ __block_literal_global.2550
+ __block_literal_global.263
+ __block_literal_global.2700
+ __block_literal_global.282
+ __block_literal_global.29.4663
+ __block_literal_global.308
+ __block_literal_global.314
+ __block_literal_global.3207
+ __block_literal_global.339
+ __block_literal_global.3398
+ __block_literal_global.3647
+ __block_literal_global.376
+ __block_literal_global.3763
+ __block_literal_global.39.3419
+ __block_literal_global.4.7402
+ __block_literal_global.43.6439
+ __block_literal_global.4440
+ __block_literal_global.4558
+ __block_literal_global.47
+ __block_literal_global.4884
+ __block_literal_global.5.6496
+ __block_literal_global.5391
+ __block_literal_global.5634
+ __block_literal_global.5972
+ __block_literal_global.599.4187
+ __block_literal_global.6031
+ __block_literal_global.6160
+ __block_literal_global.6213
+ __block_literal_global.6453
+ __block_literal_global.6716
+ __block_literal_global.6755
+ __block_literal_global.679
+ __block_literal_global.6955
+ __block_literal_global.7153
+ __block_literal_global.7285
+ __block_literal_global.7398
+ __block_literal_global.7521
+ __block_literal_global.7535
+ __block_literal_global.8.1740
+ __block_literal_global.8.2406
+ __block_literal_global.8.6177
+ __block_literal_global.8.7159
+ __block_literal_global.824
+ __block_literal_global.9.6038
+ __block_literal_global.959
+ __dx_gai_request_report_powerlog_progress
+ __handle_queryrecord_request_start
+ __mdns_dispatch_create_monotonic_timer
+ __mdns_label_is_protocol_label
+ __mdns_powerlog_event_dictionary_set_int64
+ __mdns_powerlog_event_with_record_type_and_duration
+ __mdns_powerlog_get_monotonic_time_ns
+ __mdns_querier_clear_delegation
+ __mrcs_dns_service_registration_request_copy_description
+ __mrcs_dns_service_registration_request_finalize
+ __mrcs_dns_service_registration_request_kind
+ __mrcs_server_activate_block_invoke.6
+ _clock_gettime_nsec_np
+ _g_activated
+ _g_dns_proxy_handlers
+ _g_dns_service_registration_handlers
+ _getHeuristicsQueue
+ _kMRCSServerDNSProxyHandlers
+ _kMRCSServerDNSServiceRegistrationHandlers
+ _mDNSPlatformValidQuestionForInterface
+ _mdns_address_create_from_ip_address_string
+ _mdns_dns_service_definition_create_from_xpc_dictionary
+ _mdns_powerlog_getaddrinfo_progress
+ _mdns_powerlog_getaddrinfo_stop
+ _mdns_powerlog_register_record_stop
+ _mdns_querier_set_delegator_audit_token
+ _mdns_querier_set_delegator_uuid
+ _mdns_server_log.s_log.4444
+ _mdns_server_log.s_once.4443
+ _mrc_xpc_dns_proxy_params_get_force_aaaa_synthesis
+ _mrc_xpc_dns_proxy_params_get_nat64_prefix
+ _mrc_xpc_dns_proxy_params_get_output_interface
+ _mrcs_dns_service_registration_request_kind_block_invoke.s_listener
+ _nw_parameters_set_prefer_no_proxy
+ _nw_parameters_set_source_application
+ _objc_msgSend$DNSHeuristicsFailureStateInfo
+ _objc_msgSend$clearNetworkAsFiltered:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isDNSHeuristicsFilteredNetwork
+ _objc_msgSend$setDNSHeuristicsFailureStateInfo:
+ _objc_msgSend$setDNSHeuristicsFilteredNetwork:
+ _objc_msgSend$setNetworkAsFiltered:
+ _objc_msgSend$setNetworkAsFiltered:filtered:
+ _objc_msgSend$setNetworkSettings:value:
+ _objc_msgSend$shortSSID
+ _objc_msgSend$updateKnownNetworkProfile:properties:error:
+ _xpc_array_get_string
+ dnssd_server_init.s_powerlog_progress_timer
+ g_session_list.4448
+ getHeuristicsQueue.onceToken
+ getHeuristicsQueue.queue
+ util_managed_network_change_handler.s_interface
+ util_managed_network_change_handler.s_last_blue_atlas_id
- +[DNSHeuristics clearNetworkAsFiltered:network:]
- +[DNSHeuristics setNetworkAsFiltered:network:]
- +[DNSHeuristics setNetworkAsFiltered:network:filtered:]
- +[DNSHeuristics setNetworkSettings:network:value:]
- FreeARElemCallback.2807
- GCC_except_table1047
- GCC_except_table105
- GCC_except_table109
- GCC_except_table1231
- GCC_except_table1419
- GCC_except_table1424
- GCC_except_table1428
- GCC_except_table1430
- _CFDictionaryAddValue
- _WiFiDeviceClientCopyCurrentNetwork
- _WiFiDeviceClientGetInterfaceRoleIndex
- _WiFiManagerClientCopyCurrentSessionBasedNetwork
- _WiFiManagerClientCopyInterfaces
- _WiFiManagerClientCreate
- _WiFiManagerClientSetNetworkProperty
- _WiFiNetworkGetProperty
- __Block_byref_object_copy_.896
- __Block_byref_object_dispose_.897
- ____util_cwf_queue_block_invoke
- ___block_descriptor_48_e8_32r40w_e5_v8?0lr32l8w40l8
- ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
- ___copyHeuristicsQueue_block_invoke
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6097
- ___mrcs_server_init_block_invoke
- ___util_is_car_play_block_invoke
- ___util_is_managed_network_block_invoke
- ___util_managed_network_change_handler_block_invoke_4
- ___util_managed_network_change_handler_block_invoke_5
- __block_descriptor_tmp.1.6064
- __block_descriptor_tmp.10.4583
- __block_descriptor_tmp.10.6092
- __block_descriptor_tmp.10.7082
- __block_descriptor_tmp.11.5916
- __block_descriptor_tmp.11.6423
- __block_descriptor_tmp.110
- __block_descriptor_tmp.12.1029
- __block_descriptor_tmp.12.244
- __block_descriptor_tmp.12.5918
- __block_descriptor_tmp.12.6420
- __block_descriptor_tmp.12.856
- __block_descriptor_tmp.13.4346
- __block_descriptor_tmp.13.6669
- __block_descriptor_tmp.13.858
- __block_descriptor_tmp.14.3424
- __block_descriptor_tmp.14.4591
- __block_descriptor_tmp.14.5890
- __block_descriptor_tmp.14.880
- __block_descriptor_tmp.141
- __block_descriptor_tmp.15.5898
- __block_descriptor_tmp.15.6089
- __block_descriptor_tmp.15.6670
- __block_descriptor_tmp.159
- __block_descriptor_tmp.1641
- __block_descriptor_tmp.1692
- __block_descriptor_tmp.17.3427
- __block_descriptor_tmp.17.4226
- __block_descriptor_tmp.17.6413
- __block_descriptor_tmp.17.6672
- __block_descriptor_tmp.18.4595
- __block_descriptor_tmp.18.6427
- __block_descriptor_tmp.18.6673
- __block_descriptor_tmp.189.2820
- __block_descriptor_tmp.19.5891
- __block_descriptor_tmp.19.6674
- __block_descriptor_tmp.19.935
- __block_descriptor_tmp.2.4288
- __block_descriptor_tmp.2.6095
- __block_descriptor_tmp.20.5895
- __block_descriptor_tmp.20.6676
- __block_descriptor_tmp.209.5623
- __block_descriptor_tmp.21.3429
- __block_descriptor_tmp.21.5887
- __block_descriptor_tmp.21.965
- __block_descriptor_tmp.213.5721
- __block_descriptor_tmp.22.1702
- __block_descriptor_tmp.22.4589
- __block_descriptor_tmp.228.5625
- __block_descriptor_tmp.23.1709
- __block_descriptor_tmp.239
- __block_descriptor_tmp.24.1710
- __block_descriptor_tmp.24.3466
- __block_descriptor_tmp.241
- __block_descriptor_tmp.25.1011
- __block_descriptor_tmp.25.3385
- __block_descriptor_tmp.25.5911
- __block_descriptor_tmp.25.6666
- __block_descriptor_tmp.250.5704
- __block_descriptor_tmp.2516
- __block_descriptor_tmp.252
- __block_descriptor_tmp.254
- __block_descriptor_tmp.26.1019
- __block_descriptor_tmp.26.1711
- __block_descriptor_tmp.264
- __block_descriptor_tmp.2662
- __block_descriptor_tmp.268
- __block_descriptor_tmp.27.1712
- __block_descriptor_tmp.27.3386
- __block_descriptor_tmp.27.4587
- __block_descriptor_tmp.28.1015
- __block_descriptor_tmp.28.939
- __block_descriptor_tmp.2821
- __block_descriptor_tmp.283
- __block_descriptor_tmp.287
- __block_descriptor_tmp.29.5909
- __block_descriptor_tmp.3.1696
- __block_descriptor_tmp.3.2666
- __block_descriptor_tmp.3.4267
- __block_descriptor_tmp.3.5925
- __block_descriptor_tmp.3.6067
- __block_descriptor_tmp.3.6415
- __block_descriptor_tmp.3.7202
- __block_descriptor_tmp.3.963
- __block_descriptor_tmp.30.5908
- __block_descriptor_tmp.309
- __block_descriptor_tmp.31.3382
- __block_descriptor_tmp.31.5907
- __block_descriptor_tmp.313
- __block_descriptor_tmp.315
- __block_descriptor_tmp.319
- __block_descriptor_tmp.32.5885
- __block_descriptor_tmp.33.1716
- __block_descriptor_tmp.33.5904
- __block_descriptor_tmp.3357
- __block_descriptor_tmp.338
- __block_descriptor_tmp.34.1724
- __block_descriptor_tmp.35.1723
- __block_descriptor_tmp.3603
- __block_descriptor_tmp.3676
- __block_descriptor_tmp.37.1001
- __block_descriptor_tmp.37.1720
- __block_descriptor_tmp.37.3378
- __block_descriptor_tmp.37.4600
- __block_descriptor_tmp.38.5888
- __block_descriptor_tmp.39.4597
- __block_descriptor_tmp.4.4379
- __block_descriptor_tmp.4.4799
- __block_descriptor_tmp.4.5926
- __block_descriptor_tmp.4.6071
- __block_descriptor_tmp.40.3375
- __block_descriptor_tmp.41.1009
- __block_descriptor_tmp.41.1718
- __block_descriptor_tmp.41.4582
- __block_descriptor_tmp.42
- __block_descriptor_tmp.4228
- __block_descriptor_tmp.4258
- __block_descriptor_tmp.4285
- __block_descriptor_tmp.43.5905
- __block_descriptor_tmp.4343
- __block_descriptor_tmp.4374
- __block_descriptor_tmp.44.1017
- __block_descriptor_tmp.44.4569
- __block_descriptor_tmp.4484
- __block_descriptor_tmp.45.1715
- __block_descriptor_tmp.46.4565
- __block_descriptor_tmp.46.7122
- __block_descriptor_tmp.4640
- __block_descriptor_tmp.47.1006
- __block_descriptor_tmp.47.3432
- __block_descriptor_tmp.47.5321
- __block_descriptor_tmp.49.4800
- __block_descriptor_tmp.5.4805
- __block_descriptor_tmp.5.5927
- __block_descriptor_tmp.50.4669
- __block_descriptor_tmp.50.7115
- __block_descriptor_tmp.50.974
- __block_descriptor_tmp.5087
- __block_descriptor_tmp.522
- __block_descriptor_tmp.5309
- __block_descriptor_tmp.55.979
- __block_descriptor_tmp.56.841
- __block_descriptor_tmp.56.980
- __block_descriptor_tmp.57
- __block_descriptor_tmp.5724
- __block_descriptor_tmp.6.1031
- __block_descriptor_tmp.6.1729
- __block_descriptor_tmp.6.6075
- __block_descriptor_tmp.6.6100
- __block_descriptor_tmp.6.7072
- __block_descriptor_tmp.602
- __block_descriptor_tmp.6060
- __block_descriptor_tmp.6085
- __block_descriptor_tmp.6138
- __block_descriptor_tmp.6406
- __block_descriptor_tmp.6631
- __block_descriptor_tmp.6682
- __block_descriptor_tmp.67.4643
- __block_descriptor_tmp.6724
- __block_descriptor_tmp.681
- __block_descriptor_tmp.6869
- __block_descriptor_tmp.69.4644
- __block_descriptor_tmp.7.4256
- __block_descriptor_tmp.7.4827
- __block_descriptor_tmp.7.6078
- __block_descriptor_tmp.7.829
- __block_descriptor_tmp.70.4679
- __block_descriptor_tmp.7066
- __block_descriptor_tmp.71.4675
- __block_descriptor_tmp.7198
- __block_descriptor_tmp.72.4673
- __block_descriptor_tmp.7435
- __block_descriptor_tmp.7450
- __block_descriptor_tmp.8.4254
- __block_descriptor_tmp.8.4377
- __block_descriptor_tmp.8.6408
- __block_descriptor_tmp.8.838
- __block_descriptor_tmp.823
- __block_descriptor_tmp.9.1032
- __block_descriptor_tmp.9.4261
- __block_descriptor_tmp.9.5915
- __block_descriptor_tmp.92.4748
- __block_descriptor_tmp.960
- __block_descriptor_tmp.97.4720
- __block_literal_global.101.937
- __block_literal_global.11.2384
- __block_literal_global.11.5977
- __block_literal_global.12.6087
- __block_literal_global.12.7078
- __block_literal_global.138
- __block_literal_global.14.6407
- __block_literal_global.145
- __block_literal_global.15.7319
- __block_literal_global.1628
- __block_literal_global.1687
- __block_literal_global.20.4593
- __block_literal_global.2372
- __block_literal_global.243
- __block_literal_global.2510
- __block_literal_global.252.5701
- __block_literal_global.266
- __block_literal_global.2660
- __block_literal_global.285
- __block_literal_global.29.4585
- __block_literal_global.311
- __block_literal_global.317
- __block_literal_global.3170
- __block_literal_global.3354
- __block_literal_global.336
- __block_literal_global.3601
- __block_literal_global.3717
- __block_literal_global.373
- __block_literal_global.39.3374
- __block_literal_global.4.7312
- __block_literal_global.40.6355
- __block_literal_global.4372
- __block_literal_global.44
- __block_literal_global.4481
- __block_literal_global.4803
- __block_literal_global.5.6410
- __block_literal_global.5308
- __block_literal_global.5551
- __block_literal_global.5893
- __block_literal_global.59
- __block_literal_global.5954
- __block_literal_global.597
- __block_literal_global.6
- __block_literal_global.6083
- __block_literal_global.6134
- __block_literal_global.6368
- __block_literal_global.6629
- __block_literal_global.6668
- __block_literal_global.677
- __block_literal_global.6866
- __block_literal_global.7064
- __block_literal_global.7196
- __block_literal_global.7308
- __block_literal_global.7433
- __block_literal_global.7447
- __block_literal_global.8.1701
- __block_literal_global.8.2366
- __block_literal_global.8.5961
- __block_literal_global.8.6098
- __block_literal_global.8.7070
- __block_literal_global.821
- __block_literal_global.958
- __mdns_powerlog_bonjour_event
- __util_cwf_interface
- __util_cwf_queue
- _copyHeuristicsQueue
- _mdns_dispatch_create_oneshot_monotonic_timer
- _objc_msgSend$clearNetworkAsFiltered:network:
- _objc_msgSend$copy
- _objc_msgSend$setNetworkAsFiltered:network:
- _objc_msgSend$setNetworkAsFiltered:network:filtered:
- _objc_msgSend$setNetworkSettings:network:value:
- _util_cwf_interface.s_interface
- _util_cwf_queue.s_once
- _util_cwf_queue.s_queue
- copyHeuristicsQueue.onceToken
- copyHeuristicsQueue.queue
- g_session_list.4376
- getNetworkManager.manager
- mrcs_server_init.s_listener
CStrings:
+ "@24@0:8@16"
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "B32@0:8@16@24"
+ "DNS service registration start handler"
+ "DNS service registration stop handler"
+ "DNSHeuristicsFailureStateInfo"
+ "Failed to create XPC listener for %{public}s"
+ "Failed to create periodic powerlog report timer"
+ "OS_mrcs_dns_service_registration_request"
+ "PowerLog event -- id: %ld, name: %@, subtype: %{public}s, exclude: %{mdns:yesno}d, dictionary: %@"
+ "Registered for known network privacy risk changes"
+ "SetupSocket: Attributing mDNS traffic to com.apple.datausage.dns.multicast failed: %{public}s"
+ "T@\"NSString\",?,R,C"
+ "Un-registering for known network privacy risk changes"
+ "Updating privacy risk status %d"
+ "[R%u] DNSServiceQueryRecord(%X, %d, %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), %{mdns:rrtype}d) STOP PID[%d](%{public}s)"
+ "addresses"
+ "bonjourOperation"
+ "browse progress"
+ "browse start"
+ "browse stop"
+ "clearNetworkAsFiltered:"
+ "clock_gettime_nsec_np() returned 0: %{mdns:err}d"
+ "com.apple.mDNSResponder.dns-service-registration"
+ "definition"
+ "dns_heuristics_report_resolution_failure %@ %d"
+ "dns_heuristics_report_resolution_success"
+ "dns_service_registration.start"
+ "dns_service_registration.stop"
+ "dnssd_server: report client request progress to powerlog"
+ "domains"
+ "durationMs"
+ "getaddrinfo progress"
+ "getaddrinfo start"
+ "getaddrinfo stop"
+ "ifindex"
+ "invalidate"
+ "isDNSHeuristicsFilteredNetwork"
+ "mDNSResponder-2200.100.94.0.2"
+ "mrcs_dns_service_registration_request"
+ "mrcs_server"
+ "periodic powerlog report timer fired"
+ "q"
+ "query record progress"
+ "query record start"
+ "query record stop"
+ "register record progress"
+ "register record start"
+ "register record stop"
+ "requestID"
+ "resolve progress"
+ "resolve start"
+ "resolve stop"
+ "scoped"
+ "service register progress"
+ "service register start"
+ "service register stop"
+ "setDNSHeuristicsFailureStateInfo:"
+ "setDNSHeuristicsFilteredNetwork:"
+ "setNetworkAsFiltered:"
+ "setNetworkAsFiltered:filtered:"
+ "setNetworkSettings:value:"
+ "shortSSID"
+ "subtype"
+ "updateKnownNetworkProfile:properties:error:"
+ "usesAWDL"
- "@24@0:8^{__WiFiNetwork=}16"
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"
- "B24@0:8^{__WiFiNetwork=}16"
- "B32@0:8^{__WiFiManagerClient=}16^{__WiFiNetwork=}24"
- "B36@0:8^{__WiFiManagerClient=}16^{__WiFiNetwork=}24B32"
- "B40@0:8^{__WiFiManagerClient=}16^{__WiFiNetwork=}24@32"
- "DNSFailures"
- "FilteredNetwork"
- "PowerLog event -- id: %ld, name: %@, exclude: %{mdns:yesno}d, dictionary: %@"
- "[R%u] DNSServiceQueryRecord(%X, %d, %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%x), %{public}s) STOP PID[%d](%{public}s)"
- "clearNetworkAsFiltered:network:"
- "com.apple.mDNSResponder.util.wifi_cwf_queue"
- "copy"
- "mDNSResponder-2200.80.16"
- "setNetworkAsFiltered:network:"
- "setNetworkAsFiltered:network:filtered:"
- "setNetworkSettings:network:value:"

```
