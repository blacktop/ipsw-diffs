## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2600.120.12.0.0
-  __TEXT.__text: 0xfe83c
-  __TEXT.__auth_stubs: 0x2df0
-  __TEXT.__objc_stubs: 0x1220
-  __TEXT.__objc_methlist: 0x334
-  __TEXT.__const: 0x1128
-  __TEXT.__cstring: 0x16fb1
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__oslogstring: 0x1dc06
-  __TEXT.__objc_classname: 0x5f9
-  __TEXT.__objc_methname: 0x106c
-  __TEXT.__objc_methtype: 0x52d
-  __TEXT.__unwind_info: 0x1580
-  __DATA_CONST.__auth_got: 0x1708
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x6100
-  __DATA_CONST.__cfstring: 0x1060
-  __DATA_CONST.__objc_classlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0x1e0
+2862.0.0.0.1
+  __TEXT.__text: 0x1058f4
+  __TEXT.__auth_stubs: 0x2ee0
+  __TEXT.__objc_stubs: 0x1b80
+  __TEXT.__objc_methlist: 0x63c
+  __TEXT.__const: 0x1168
+  __TEXT.__cstring: 0x174d7
+  __TEXT.__gcc_except_tab: 0x360
+  __TEXT.__oslogstring: 0x1ec41
+  __TEXT.__objc_classname: 0x649
+  __TEXT.__objc_methname: 0x1a02
+  __TEXT.__objc_methtype: 0x62a
+  __TEXT.__unwind_info: 0x1650
+  __TEXT.__eh_frame: 0x74
+  __DATA_CONST.__auth_got: 0x1780
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__auth_ptr: 0x78
+  __DATA_CONST.__const: 0x6478
+  __DATA_CONST.__cfstring: 0x1280
+  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x3aa8
-  __DATA.__objc_selrefs: 0x5b0
-  __DATA.__objc_classrefs: 0x130
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_data: 0x1180
-  __DATA.__data: 0x4250
-  __DATA.__bss: 0x16d80
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA.__objc_const: 0x4108
+  __DATA.__objc_selrefs: 0x888
+  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_data: 0x1270
+  __DATA.__data: 0x4328
+  __DATA.__bss: 0x16de0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 33FC5664-2544-3691-9155-C0C402D9E1CB
-  Functions: 1739
-  Symbols:   4284
-  CStrings:  4560
+  UUID: AFA84D0B-F26F-3B69-A097-493D4FBF2591
+  Functions: 1833
+  Symbols:   4558
+  CStrings:  4851
 
Symbols:
+ +[UAQhash qhash:withTime:]
+ -[NSArray(ua_extension) describeQHashes]
+ -[NSArray(ua_extension) describeUAQHashes]
+ -[NSArray(ua_extension) filterObjectsUsingBlock:]
+ -[NSData(ua_extension) describeAddr]
+ -[UAPresenceManager .cxx_destruct]
+ -[UAPresenceManager _addRecordsFromPresence:]
+ -[UAPresenceManager addQhash:forInterface:]
+ -[UAPresenceManager assertPresence:]
+ -[UAPresenceManager authCheckTime]
+ -[UAPresenceManager authRecords]
+ -[UAPresenceManager authUpdateTime]
+ -[UAPresenceManager dealloc]
+ -[UAPresenceManager handleAuthCheck:]
+ -[UAPresenceManager handleNetworkUpdate:]
+ -[UAPresenceManager idlePresence:]
+ -[UAPresenceManager init]
+ -[UAPresenceManager initialCloudKitImportReceived:]
+ -[UAPresenceManager lastAuthUpdate]
+ -[UAPresenceManager lastUnsubscribeTime]
+ -[UAPresenceManager networkAddrs]
+ -[UAPresenceManager networkUpdateTime]
+ -[UAPresenceManager presenceAsserted]
+ -[UAPresenceManager presenceReady]
+ -[UAPresenceManager presenceSubscribed]
+ -[UAPresenceManager presenceUpdateTime]
+ -[UAPresenceManager presence]
+ -[UAPresenceManager presentDevicesChangedForPresence:]
+ -[UAPresenceManager releaseSubscriptions]
+ -[UAPresenceManager removeQhash:forInterface:]
+ -[UAPresenceManager retainSubscription]
+ -[UAPresenceManager setAuthCheckTime:]
+ -[UAPresenceManager setAuthRecords:]
+ -[UAPresenceManager setAuthUpdateTime:]
+ -[UAPresenceManager setLastAuthUpdate:]
+ -[UAPresenceManager setLastUnsubscribeTime:]
+ -[UAPresenceManager setNetworkAddrs:]
+ -[UAPresenceManager setNetworkUpdateTime:]
+ -[UAPresenceManager setPresence:]
+ -[UAPresenceManager setPresenceAsserted:]
+ -[UAPresenceManager setPresenceReady:]
+ -[UAPresenceManager setPresenceSubscribed:]
+ -[UAPresenceManager setPresenceUpdateTime:]
+ -[UAPresenceManager setSkUpdates:]
+ -[UAPresenceManager skUpdates]
+ -[UAPresenceManager updateCacheFromPresence]
+ -[UAPresenceManager updateInvalidFromPresence]
+ -[UAQhash initQhash:withTime:]
+ -[UAQhash qhash]
+ -[UAQhash removed]
+ -[UAQhash setQhash:]
+ -[UAQhash setRemoved:]
+ -[UAQhash setTime:]
+ -[UAQhash time]
+ FreeARElemCallback.2635
+ GCC_except_table1216
+ GCC_except_table1222
+ GCC_except_table1385
+ GCC_except_table1580
+ GCC_except_table1803
+ OBJC_IVAR_$_UAPresenceManager._authCheckTime
+ OBJC_IVAR_$_UAPresenceManager._authRecords
+ OBJC_IVAR_$_UAPresenceManager._authUpdateTime
+ OBJC_IVAR_$_UAPresenceManager._lastAuthUpdate
+ OBJC_IVAR_$_UAPresenceManager._lastUnsubscribeTime
+ OBJC_IVAR_$_UAPresenceManager._networkAddrs
+ OBJC_IVAR_$_UAPresenceManager._networkUpdateTime
+ OBJC_IVAR_$_UAPresenceManager._presence
+ OBJC_IVAR_$_UAPresenceManager._presenceAsserted
+ OBJC_IVAR_$_UAPresenceManager._presenceReady
+ OBJC_IVAR_$_UAPresenceManager._presenceSubscribed
+ OBJC_IVAR_$_UAPresenceManager._presenceUpdateTime
+ OBJC_IVAR_$_UAPresenceManager._skUpdates
+ OBJC_IVAR_$_UAQhash._qhash
+ OBJC_IVAR_$_UAQhash._removed
+ OBJC_IVAR_$_UAQhash._time
+ _CFDictionaryCreateCopy
+ _CFReadStreamClose
+ _CFWriteStreamCreateWithFile
+ _CacheGroupHasAddressOnInterface
+ _EnableSocketReadEvent
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_OS_mdns_trust_state
+ _OBJC_CLASS_$_SKPresence
+ _OBJC_CLASS_$_SKPresenceAssertionOptions
+ _OBJC_CLASS_$_SKPresenceOptions
+ _OBJC_CLASS_$_SKPresencePayload
+ _OBJC_CLASS_$_UAPresenceManager
+ _OBJC_CLASS_$_UAQhash
+ _OBJC_METACLASS_$_OS_mdns_trust_state
+ _OBJC_METACLASS_$_UAPresenceManager
+ _OBJC_METACLASS_$_UAQhash
+ _OUTLINED_FUNCTION_0
+ _SameNameCacheRecordsMatchInSourceTypeClass
+ __36-[UAPresenceManager assertPresence:]_block_invoke.89
+ __41-[UAPresenceManager releaseSubscriptions]_block_invoke.56
+ __44-[UAPresenceManager updateCacheFromPresence]_block_invoke.113
+ __44-[UAPresenceManager updateCacheFromPresence]_block_invoke_2.114
+ __AppendEscapedASCIIString
+ __MergedGlobals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_ua_extension
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_ua_extension
+ __OBJC_$_CATEGORY_NSArray_$_ua_extension
+ __OBJC_$_CATEGORY_NSData_$_ua_extension
+ __OBJC_$_CLASS_METHODS_UAQhash
+ __OBJC_$_INSTANCE_METHODS_UAPresenceManager
+ __OBJC_$_INSTANCE_METHODS_UAQhash
+ __OBJC_$_INSTANCE_VARIABLES_UAPresenceManager
+ __OBJC_$_INSTANCE_VARIABLES_UAQhash
+ __OBJC_$_PROP_LIST_OS_mdns_trust_state
+ __OBJC_$_PROP_LIST_UAPresenceManager
+ __OBJC_$_PROP_LIST_UAQhash
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SKPresenceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SKPresenceDelegate
+ __OBJC_$_PROTOCOL_REFS_OS_mdns_trust_state
+ __OBJC_$_PROTOCOL_REFS_SKPresenceDelegate
+ __OBJC_CLASS_PROTOCOLS_$_OS_mdns_trust_state
+ __OBJC_CLASS_PROTOCOLS_$_UAPresenceManager
+ __OBJC_CLASS_RO_$_OS_mdns_trust_state
+ __OBJC_CLASS_RO_$_UAPresenceManager
+ __OBJC_CLASS_RO_$_UAQhash
+ __OBJC_LABEL_PROTOCOL_$_OS_mdns_trust_state
+ __OBJC_LABEL_PROTOCOL_$_SKPresenceDelegate
+ __OBJC_METACLASS_RO_$_OS_mdns_trust_state
+ __OBJC_METACLASS_RO_$_UAPresenceManager
+ __OBJC_METACLASS_RO_$_UAQhash
+ __OBJC_PROTOCOL_$_OS_mdns_trust_state
+ __OBJC_PROTOCOL_$_SKPresenceDelegate
+ ___25-[UAPresenceManager init]_block_invoke
+ ___36-[UAPresenceManager assertPresence:]_block_invoke
+ ___36-[UAPresenceManager assertPresence:]_block_invoke_2
+ ___36-[UAPresenceManager assertPresence:]_block_invoke_3
+ ___37-[UAPresenceManager handleAuthCheck:]_block_invoke
+ ___39-[UAPresenceManager retainSubscription]_block_invoke
+ ___41-[UAPresenceManager releaseSubscriptions]_block_invoke
+ ___43-[UAPresenceManager addQhash:forInterface:]_block_invoke
+ ___44-[UAPresenceManager updateCacheFromPresence]_block_invoke
+ ___44-[UAPresenceManager updateCacheFromPresence]_block_invoke_2
+ ___44-[UAPresenceManager updateCacheFromPresence]_block_invoke_3
+ ___44-[UAPresenceManager updateCacheFromPresence]_block_invoke_4
+ ___46-[UAPresenceManager removeQhash:forInterface:]_block_invoke
+ ___49-[NSArray(ua_extension) filterObjectsUsingBlock:]_block_invoke
+ ____mdns_dns_push_service_definition_copy_description_block_invoke_2
+ ____mrcs_prefs_log_block_invoke
+ ____unicast_assist_should_activate_presence_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e25_B16?0"SKPresentDevice"8l
+ ___block_descriptor_36_e24_B32?0"UAQhash"8Q16^B24l
+ ___block_descriptor_40_e22_B16?0"NSDictionary"8l
+ ___block_descriptor_40_e8_32bs_e15_B32?08Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSNumber"8ls32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e22_B16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e24_v32?0"UAQhash"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e29_B32?0"NSDictionary"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e32_B32?0"SKPresentDevice"8Q16^B24ls32l8
+ ___destructor_8_s32_s48_s56_s64
+ ___isPlatformVersionAtLeast
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6321
+ ___mdns_dns_service_manager_probe_discovered_service_block_invoke.231
+ ___mdns_dns_service_manager_probe_discovered_service_block_invoke_2.232
+ ___mdns_server_log_block_invoke.4343
+ ___mdns_url_session_send_block_invoke.102
+ ___mdns_url_session_send_block_invoke.104
+ ___mdns_url_session_send_block_invoke.110
+ ___unicast_assist_hash_for_interface_block_invoke.310
+ ___unicast_assist_init_block_invoke
+ ___unicast_assist_init_block_invoke_2
+ __availability_version_check
+ __block_descriptor_tmp.1.6289
+ __block_descriptor_tmp.10.4326
+ __block_descriptor_tmp.10.6111
+ __block_descriptor_tmp.107
+ __block_descriptor_tmp.109
+ __block_descriptor_tmp.11.6315
+ __block_descriptor_tmp.11.6679
+ __block_descriptor_tmp.11.851
+ __block_descriptor_tmp.112
+ __block_descriptor_tmp.115.4837
+ __block_descriptor_tmp.119.4818
+ __block_descriptor_tmp.12.6118
+ __block_descriptor_tmp.12.6676
+ __block_descriptor_tmp.12.852
+ __block_descriptor_tmp.120.4820
+ __block_descriptor_tmp.121.4812
+ __block_descriptor_tmp.122.4836
+ __block_descriptor_tmp.127
+ __block_descriptor_tmp.128
+ __block_descriptor_tmp.13.4342
+ __block_descriptor_tmp.13.4711
+ __block_descriptor_tmp.13.6119
+ __block_descriptor_tmp.130.4766
+ __block_descriptor_tmp.134
+ __block_descriptor_tmp.14.1054
+ __block_descriptor_tmp.14.3261
+ __block_descriptor_tmp.140.4790
+ __block_descriptor_tmp.142
+ __block_descriptor_tmp.1439
+ __block_descriptor_tmp.144
+ __block_descriptor_tmp.145.936
+ __block_descriptor_tmp.15.6073
+ __block_descriptor_tmp.1524
+ __block_descriptor_tmp.16.6326
+ __block_descriptor_tmp.17.1055
+ __block_descriptor_tmp.17.4126
+ __block_descriptor_tmp.17.4715
+ __block_descriptor_tmp.17.6074
+ __block_descriptor_tmp.17.6670
+ __block_descriptor_tmp.17.892
+ __block_descriptor_tmp.170
+ __block_descriptor_tmp.18.3269
+ __block_descriptor_tmp.18.4266
+ __block_descriptor_tmp.18.4314
+ __block_descriptor_tmp.18.6080
+ __block_descriptor_tmp.18.6683
+ __block_descriptor_tmp.18.894
+ __block_descriptor_tmp.182
+ __block_descriptor_tmp.19.6068
+ __block_descriptor_tmp.2.4200
+ __block_descriptor_tmp.2.6992
+ __block_descriptor_tmp.20.6113
+ __block_descriptor_tmp.20.6963
+ __block_descriptor_tmp.20.984
+ __block_descriptor_tmp.204
+ __block_descriptor_tmp.21.4269
+ __block_descriptor_tmp.21.4708
+ __block_descriptor_tmp.21.6978
+ __block_descriptor_tmp.217
+ __block_descriptor_tmp.218
+ __block_descriptor_tmp.22.1534
+ __block_descriptor_tmp.22.3271
+ __block_descriptor_tmp.22.4329
+ __block_descriptor_tmp.22.6114
+ __block_descriptor_tmp.221
+ __block_descriptor_tmp.222
+ __block_descriptor_tmp.2292
+ __block_descriptor_tmp.23.1541
+ __block_descriptor_tmp.23.6964
+ __block_descriptor_tmp.230
+ __block_descriptor_tmp.233.5759
+ __block_descriptor_tmp.234
+ __block_descriptor_tmp.236.2986
+ __block_descriptor_tmp.2395
+ __block_descriptor_tmp.24.1542
+ __block_descriptor_tmp.24.3301
+ __block_descriptor_tmp.24.6109
+ __block_descriptor_tmp.240
+ __block_descriptor_tmp.241
+ __block_descriptor_tmp.244
+ __block_descriptor_tmp.246.2981
+ __block_descriptor_tmp.25.1052
+ __block_descriptor_tmp.25.3325
+ __block_descriptor_tmp.25.6965
+ __block_descriptor_tmp.251.5839
+ __block_descriptor_tmp.255
+ __block_descriptor_tmp.26.1543
+ __block_descriptor_tmp.26.4705
+ __block_descriptor_tmp.26.6106
+ __block_descriptor_tmp.262
+ __block_descriptor_tmp.2648
+ __block_descriptor_tmp.27.1544
+ __block_descriptor_tmp.27.6103
+ __block_descriptor_tmp.27.6970
+ __block_descriptor_tmp.27.951
+ __block_descriptor_tmp.28.6101
+ __block_descriptor_tmp.28.6971
+ __block_descriptor_tmp.29.1546
+ __block_descriptor_tmp.29.3330
+ __block_descriptor_tmp.29.6064
+ __block_descriptor_tmp.29.6972
+ __block_descriptor_tmp.3.1528
+ __block_descriptor_tmp.3.2293
+ __block_descriptor_tmp.3.4203
+ __block_descriptor_tmp.3.6127
+ __block_descriptor_tmp.3.6292
+ __block_descriptor_tmp.3.6319
+ __block_descriptor_tmp.3.6672
+ __block_descriptor_tmp.3.7545
+ __block_descriptor_tmp.3.990
+ __block_descriptor_tmp.30.6092
+ __block_descriptor_tmp.30.6956
+ __block_descriptor_tmp.31.3341
+ __block_descriptor_tmp.3188
+ __block_descriptor_tmp.32.4330
+ __block_descriptor_tmp.32.6094
+ __block_descriptor_tmp.33.1548
+ __block_descriptor_tmp.33.6962
+ __block_descriptor_tmp.34.1557
+ __block_descriptor_tmp.34.3212
+ __block_descriptor_tmp.34.6950
+ __block_descriptor_tmp.35.1556
+ __block_descriptor_tmp.35.6979
+ __block_descriptor_tmp.3500
+ __block_descriptor_tmp.3579
+ __block_descriptor_tmp.36.4720
+ __block_descriptor_tmp.38.1032
+ __block_descriptor_tmp.38.3213
+ __block_descriptor_tmp.38.4717
+ __block_descriptor_tmp.39.1042
+ __block_descriptor_tmp.39.6043
+ __block_descriptor_tmp.391
+ __block_descriptor_tmp.4.4204
+ __block_descriptor_tmp.4.4316
+ __block_descriptor_tmp.4.4920
+ __block_descriptor_tmp.4.6128
+ __block_descriptor_tmp.4.6296
+ __block_descriptor_tmp.4.7378
+ __block_descriptor_tmp.40.1550
+ __block_descriptor_tmp.40.4700
+ __block_descriptor_tmp.41.1037
+ __block_descriptor_tmp.41.1551
+ __block_descriptor_tmp.4128
+ __block_descriptor_tmp.4195
+ __block_descriptor_tmp.42.3210
+ __block_descriptor_tmp.43.4684
+ __block_descriptor_tmp.4311
+ __block_descriptor_tmp.45.4679
+ __block_descriptor_tmp.47.3195
+ __block_descriptor_tmp.47.5447
+ __block_descriptor_tmp.4760
+ __block_descriptor_tmp.48.3262
+ __block_descriptor_tmp.48.4921
+ __block_descriptor_tmp.5.2304
+ __block_descriptor_tmp.5.4205
+ __block_descriptor_tmp.5.4317
+ __block_descriptor_tmp.5.4926
+ __block_descriptor_tmp.5.6129
+ __block_descriptor_tmp.50.3280
+ __block_descriptor_tmp.50.4788
+ __block_descriptor_tmp.51.1041
+ __block_descriptor_tmp.51.3206
+ __block_descriptor_tmp.51.4695
+ __block_descriptor_tmp.5198
+ __block_descriptor_tmp.538
+ __block_descriptor_tmp.54.3204
+ __block_descriptor_tmp.5435
+ __block_descriptor_tmp.55.1039
+ __block_descriptor_tmp.58.1035
+ __block_descriptor_tmp.5864
+ __block_descriptor_tmp.6.1562
+ __block_descriptor_tmp.6.4177
+ __block_descriptor_tmp.6.4318
+ __block_descriptor_tmp.6.6300
+ __block_descriptor_tmp.6.987
+ __block_descriptor_tmp.60.1028
+ __block_descriptor_tmp.60.3333
+ __block_descriptor_tmp.60.7445
+ __block_descriptor_tmp.61.3331
+ __block_descriptor_tmp.62.3344
+ __block_descriptor_tmp.62.6088
+ __block_descriptor_tmp.6285
+ __block_descriptor_tmp.63.4666
+ __block_descriptor_tmp.63.998
+ __block_descriptor_tmp.6311
+ __block_descriptor_tmp.6371
+ __block_descriptor_tmp.64.7438
+ __block_descriptor_tmp.6558
+ __block_descriptor_tmp.6664
+ __block_descriptor_tmp.68.4763
+ __block_descriptor_tmp.6899
+ __block_descriptor_tmp.69.1003
+ __block_descriptor_tmp.69.4799
+ __block_descriptor_tmp.6993
+ __block_descriptor_tmp.7.4321
+ __block_descriptor_tmp.7.6131
+ __block_descriptor_tmp.7.6303
+ __block_descriptor_tmp.7.6324
+ __block_descriptor_tmp.7.6928
+ __block_descriptor_tmp.7.838
+ __block_descriptor_tmp.70.4795
+ __block_descriptor_tmp.7027
+ __block_descriptor_tmp.7179
+ __block_descriptor_tmp.7374
+ __block_descriptor_tmp.7541
+ __block_descriptor_tmp.76.4898
+ __block_descriptor_tmp.7769
+ __block_descriptor_tmp.78
+ __block_descriptor_tmp.8.160
+ __block_descriptor_tmp.8.6665
+ __block_descriptor_tmp.8.7388
+ __block_descriptor_tmp.8.846
+ __block_descriptor_tmp.80.4896
+ __block_descriptor_tmp.80.7391
+ __block_descriptor_tmp.832
+ __block_descriptor_tmp.9.4703
+ __block_descriptor_tmp.91.4870
+ __block_descriptor_tmp.93.4868
+ __block_descriptor_tmp.97
+ __block_descriptor_tmp.980
+ __block_literal_global.10.7384
+ __block_literal_global.11.4701
+ __block_literal_global.112
+ __block_literal_global.132
+ __block_literal_global.141
+ __block_literal_global.1426
+ __block_literal_global.144
+ __block_literal_global.15.4323
+ __block_literal_global.15.4707
+ __block_literal_global.15.7661
+ __block_literal_global.1519
+ __block_literal_global.179
+ __block_literal_global.19.4713
+ __block_literal_global.20.4310
+ __block_literal_global.220
+ __block_literal_global.2220
+ __block_literal_global.224
+ __block_literal_global.2291
+ __block_literal_global.235
+ __block_literal_global.2389
+ __block_literal_global.239
+ __block_literal_global.243
+ __block_literal_global.249
+ __block_literal_global.253.5768
+ __block_literal_global.257
+ __block_literal_global.258
+ __block_literal_global.261
+ __block_literal_global.264
+ __block_literal_global.28.6179
+ __block_literal_global.290
+ __block_literal_global.2985
+ __block_literal_global.303
+ __block_literal_global.307.4549
+ __block_literal_global.309
+ __block_literal_global.313.4628
+ __block_literal_global.3323
+ __block_literal_global.3498
+ __block_literal_global.3610
+ __block_literal_global.389
+ __block_literal_global.425
+ __block_literal_global.43.6612
+ __block_literal_global.4319
+ __block_literal_global.4569
+ __block_literal_global.4924
+ __block_literal_global.5.6314
+ __block_literal_global.5.6667
+ __block_literal_global.53.4687
+ __block_literal_global.5434
+ __block_literal_global.5685
+ __block_literal_global.58
+ __block_literal_global.6066
+ __block_literal_global.6172
+ __block_literal_global.6309
+ __block_literal_global.6367
+ __block_literal_global.6551
+ __block_literal_global.6626
+ __block_literal_global.6897
+ __block_literal_global.6952
+ __block_literal_global.7176
+ __block_literal_global.7372
+ __block_literal_global.7539
+ __block_literal_global.7652
+ __block_literal_global.7767
+ __block_literal_global.8.1533
+ __block_literal_global.8.2214
+ __block_literal_global.830
+ __block_literal_global.9.6322
+ __block_literal_global.91
+ __block_literal_global.978
+ __initializeAvailabilityCheck
+ __isPlatformVersionAtLeast.cold.1
+ __isPlatformVersionAtLeast.cold.2
+ __mdns_dns_service_manager_deregister_service_by_config
+ __mdns_trust_state_copy_description
+ __mdns_trust_state_finalize
+ __mdns_trust_state_kind
+ __mrcs_prefs_create_plist_file_path
+ __mrcs_prefs_get_plist
+ __set_user_dir_suffix
+ __unicast_assist_data_to_addr
+ __unicast_assist_internal_queue
+ __unicast_assist_network_ready_for_presence
+ __unicast_assist_presence_update_shared_cache_enable
+ __unicast_assist_records_for_interface
+ _compatibilityInitializeAvailabilityCheck
+ _confstr
+ _dispatch_once_f
+ _fread
+ _fseek
+ _ftell
+ _g_public_lock
+ _initializeAvailabilityCheck
+ _kCFBooleanFalse
+ _mDNSCoreRestartQuestion
+ _malloc
+ _mdns_address_create_from_ip_address_string_and_port
+ _mdns_server_log.s_log.4324
+ _mdns_server_log.s_once.4322
+ _mdns_socket_forget
+ _mrcs_prefs_get_plist.s_plist
+ _mrcs_prefs_log.s_log
+ _mrcs_prefs_log.s_once
+ _mrcs_prefs_set_shared_assist_cache_enable
+ _notify_post
+ _nw_resolver_config_get_port
+ _objc_msgSend$_addRecordsFromPresence:
+ _objc_msgSend$addDelegate:queue:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$array
+ _objc_msgSend$assertPresenceWithPresencePayload:assertionOptions:completion:
+ _objc_msgSend$assertionTime
+ _objc_msgSend$authRecords
+ _objc_msgSend$authUpdateTime
+ _objc_msgSend$boolValue
+ _objc_msgSend$bytes
+ _objc_msgSend$compare:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$describeAddr
+ _objc_msgSend$describeQHashes
+ _objc_msgSend$describeUAQHashes
+ _objc_msgSend$deviceIdentifier
+ _objc_msgSend$effectiveBundleIdentifier
+ _objc_msgSend$filterObjectsUsingBlock:
+ _objc_msgSend$handleNetworkUpdate:
+ _objc_msgSend$hasInitialCloudKitImportOccurredWithCompletion:
+ _objc_msgSend$idlePresence:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$initQhash:withTime:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithPresenceIdentifier:options:
+ _objc_msgSend$initWithPriority:
+ _objc_msgSend$initWithServiceIdentifier:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isSelfDevice
+ _objc_msgSend$lastAuthUpdate
+ _objc_msgSend$lastUnsubscribeTime
+ _objc_msgSend$networkAddrs
+ _objc_msgSend$networkUpdateTime
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$payloadDictionary
+ _objc_msgSend$presence
+ _objc_msgSend$presenceAsserted
+ _objc_msgSend$presencePayload
+ _objc_msgSend$presenceReady
+ _objc_msgSend$presenceSubscribed
+ _objc_msgSend$presenceUpdateTime
+ _objc_msgSend$presentDevices
+ _objc_msgSend$qhash
+ _objc_msgSend$qhash:withTime:
+ _objc_msgSend$releasePresenceWithCompletion:
+ _objc_msgSend$releaseSubscriptions
+ _objc_msgSend$releaseTransientSubscriptionAssertionWithCompletion:
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$removed
+ _objc_msgSend$retainSubscription
+ _objc_msgSend$retainTransientSubscriptionAssertionWithCompletion:
+ _objc_msgSend$setAuthUpdateTime:
+ _objc_msgSend$setIsDaemonIdleExitEnabled:
+ _objc_msgSend$setIsPersonal:
+ _objc_msgSend$setLastAuthUpdate:
+ _objc_msgSend$setLastUnsubscribeTime:
+ _objc_msgSend$setNetworkAddrs:
+ _objc_msgSend$setNetworkUpdateTime:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setPresenceAsserted:
+ _objc_msgSend$setPresenceReady:
+ _objc_msgSend$setPresenceSubscribed:
+ _objc_msgSend$setPresenceUpdateTime:
+ _objc_msgSend$setRemoved:
+ _objc_msgSend$setTime:
+ _objc_msgSend$skUpdates
+ _objc_msgSend$string
+ _objc_msgSend$time
+ _objc_msgSend$updateCacheFromPresence
+ _objc_msgSend$updateInvalidFromPresence
+ _objc_retain_x24
+ _rewind
+ _s_presence
+ _s_shared_cache_enabled
+ _unicast_assist_addr_refresh
+ _unicast_assist_presence_idle.last_idle
+ _unicast_assist_should_activate_presence.s_once
+ _unicast_assist_should_activate_presence.should_activate
+ g_nwi_state.4551
+ g_session_list.4328
+ unicast_assist_init.s_once
- FreeARElemCallback.2644
- GCC_except_table1169
- GCC_except_table1176
- GCC_except_table1306
- GCC_except_table1500
- _CheckTSRForAuthRecord
- _PacketRecordMatches
- _SetupLocalHostRecords
- _ShouldSuppressKnownAnswer
- ____mdns_dns_service_manager_update_nw_config_data_block_invoke
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6181
- ___mdns_dns_service_manager_probe_discovered_service_block_invoke.234
- ___mdns_dns_service_manager_probe_discovered_service_block_invoke_2.235
- ___mdns_server_log_block_invoke.4339
- ___mdns_url_session_send_block_invoke.101
- ___mdns_url_session_send_block_invoke.103
- ___mdns_url_session_send_block_invoke.109
- ___unicast_assist_hash_for_interface_block_invoke.34
- __block_descriptor_tmp.1.6150
- __block_descriptor_tmp.10.4322
- __block_descriptor_tmp.10.5993
- __block_descriptor_tmp.106
- __block_descriptor_tmp.108.4747
- __block_descriptor_tmp.11.6175
- __block_descriptor_tmp.11.6512
- __block_descriptor_tmp.11.852
- __block_descriptor_tmp.111
- __block_descriptor_tmp.113
- __block_descriptor_tmp.118.4717
- __block_descriptor_tmp.119.4719
- __block_descriptor_tmp.12.6000
- __block_descriptor_tmp.12.6509
- __block_descriptor_tmp.12.853
- __block_descriptor_tmp.120.4711
- __block_descriptor_tmp.121.4733
- __block_descriptor_tmp.129
- __block_descriptor_tmp.129.4666
- __block_descriptor_tmp.13.4338
- __block_descriptor_tmp.13.4611
- __block_descriptor_tmp.13.6001
- __block_descriptor_tmp.131
- __block_descriptor_tmp.133.3655
- __block_descriptor_tmp.139
- __block_descriptor_tmp.14.1053
- __block_descriptor_tmp.14.3272
- __block_descriptor_tmp.140.4802
- __block_descriptor_tmp.1446
- __block_descriptor_tmp.145.542
- __block_descriptor_tmp.149
- __block_descriptor_tmp.15.5956
- __block_descriptor_tmp.151
- __block_descriptor_tmp.1531
- __block_descriptor_tmp.16.6186
- __block_descriptor_tmp.17.1054
- __block_descriptor_tmp.17.4132
- __block_descriptor_tmp.17.4615
- __block_descriptor_tmp.17.5957
- __block_descriptor_tmp.17.6503
- __block_descriptor_tmp.17.893
- __block_descriptor_tmp.173
- __block_descriptor_tmp.177
- __block_descriptor_tmp.18.3280
- __block_descriptor_tmp.18.4262
- __block_descriptor_tmp.18.4310
- __block_descriptor_tmp.18.5963
- __block_descriptor_tmp.18.6516
- __block_descriptor_tmp.19.5951
- __block_descriptor_tmp.2.4196
- __block_descriptor_tmp.2.6814
- __block_descriptor_tmp.20.5995
- __block_descriptor_tmp.20.6785
- __block_descriptor_tmp.20.983
- __block_descriptor_tmp.207
- __block_descriptor_tmp.209
- __block_descriptor_tmp.21.4265
- __block_descriptor_tmp.21.4608
- __block_descriptor_tmp.21.6800
- __block_descriptor_tmp.216
- __block_descriptor_tmp.22.1541
- __block_descriptor_tmp.22.3282
- __block_descriptor_tmp.22.4325
- __block_descriptor_tmp.22.5996
- __block_descriptor_tmp.224.5651
- __block_descriptor_tmp.227
- __block_descriptor_tmp.229
- __block_descriptor_tmp.23.1548
- __block_descriptor_tmp.23.6786
- __block_descriptor_tmp.2303
- __block_descriptor_tmp.231
- __block_descriptor_tmp.232
- __block_descriptor_tmp.233.3002
- __block_descriptor_tmp.239
- __block_descriptor_tmp.24.1549
- __block_descriptor_tmp.24.3308
- __block_descriptor_tmp.24.5991
- __block_descriptor_tmp.24.950
- __block_descriptor_tmp.2406
- __block_descriptor_tmp.246.2993
- __block_descriptor_tmp.246.5722
- __block_descriptor_tmp.248
- __block_descriptor_tmp.249
- __block_descriptor_tmp.25.1051
- __block_descriptor_tmp.25.3332
- __block_descriptor_tmp.25.6787
- __block_descriptor_tmp.250.2788
- __block_descriptor_tmp.254
- __block_descriptor_tmp.26.1550
- __block_descriptor_tmp.26.4605
- __block_descriptor_tmp.26.5988
- __block_descriptor_tmp.2657
- __block_descriptor_tmp.27.1551
- __block_descriptor_tmp.27.5985
- __block_descriptor_tmp.27.6792
- __block_descriptor_tmp.28.5983
- __block_descriptor_tmp.28.6793
- __block_descriptor_tmp.29.1553
- __block_descriptor_tmp.29.3337
- __block_descriptor_tmp.29.4326
- __block_descriptor_tmp.29.5947
- __block_descriptor_tmp.29.6794
- __block_descriptor_tmp.3.1535
- __block_descriptor_tmp.3.2304
- __block_descriptor_tmp.3.4199
- __block_descriptor_tmp.3.6009
- __block_descriptor_tmp.3.6153
- __block_descriptor_tmp.3.6179
- __block_descriptor_tmp.3.6505
- __block_descriptor_tmp.3.7367
- __block_descriptor_tmp.3.989
- __block_descriptor_tmp.30.6778
- __block_descriptor_tmp.31.3348
- __block_descriptor_tmp.31.4327
- __block_descriptor_tmp.3199
- __block_descriptor_tmp.32.5976
- __block_descriptor_tmp.33.1555
- __block_descriptor_tmp.33.6784
- __block_descriptor_tmp.34.1564
- __block_descriptor_tmp.34.3223
- __block_descriptor_tmp.34.6772
- __block_descriptor_tmp.35.1563
- __block_descriptor_tmp.35.6801
- __block_descriptor_tmp.3507
- __block_descriptor_tmp.3586
- __block_descriptor_tmp.36.4620
- __block_descriptor_tmp.38.1031
- __block_descriptor_tmp.38.3224
- __block_descriptor_tmp.38.4617
- __block_descriptor_tmp.383
- __block_descriptor_tmp.39.1041
- __block_descriptor_tmp.39.5926
- __block_descriptor_tmp.4.4200
- __block_descriptor_tmp.4.4312
- __block_descriptor_tmp.4.4818
- __block_descriptor_tmp.4.6010
- __block_descriptor_tmp.4.6157
- __block_descriptor_tmp.4.7200
- __block_descriptor_tmp.40.1557
- __block_descriptor_tmp.40.4600
- __block_descriptor_tmp.41.1036
- __block_descriptor_tmp.41.1558
- __block_descriptor_tmp.4134
- __block_descriptor_tmp.4191
- __block_descriptor_tmp.42.3221
- __block_descriptor_tmp.43.4584
- __block_descriptor_tmp.4307
- __block_descriptor_tmp.45.4579
- __block_descriptor_tmp.4660
- __block_descriptor_tmp.47.3206
- __block_descriptor_tmp.47.5345
- __block_descriptor_tmp.48.3273
- __block_descriptor_tmp.48.4819
- __block_descriptor_tmp.5.2315
- __block_descriptor_tmp.5.4201
- __block_descriptor_tmp.5.4313
- __block_descriptor_tmp.5.4824
- __block_descriptor_tmp.5.6011
- __block_descriptor_tmp.50.3291
- __block_descriptor_tmp.50.4688
- __block_descriptor_tmp.51.1040
- __block_descriptor_tmp.51.3217
- __block_descriptor_tmp.51.4595
- __block_descriptor_tmp.5106
- __block_descriptor_tmp.532
- __block_descriptor_tmp.5333
- __block_descriptor_tmp.54.3215
- __block_descriptor_tmp.55.1038
- __block_descriptor_tmp.5747
- __block_descriptor_tmp.58.1034
- __block_descriptor_tmp.6.1569
- __block_descriptor_tmp.6.4173
- __block_descriptor_tmp.6.4314
- __block_descriptor_tmp.6.6161
- __block_descriptor_tmp.6.986
- __block_descriptor_tmp.60.1027
- __block_descriptor_tmp.60.3340
- __block_descriptor_tmp.60.7267
- __block_descriptor_tmp.61.3338
- __block_descriptor_tmp.6146
- __block_descriptor_tmp.6171
- __block_descriptor_tmp.62.3351
- __block_descriptor_tmp.62.5971
- __block_descriptor_tmp.6231
- __block_descriptor_tmp.63.4566
- __block_descriptor_tmp.63.997
- __block_descriptor_tmp.64.7260
- __block_descriptor_tmp.6497
- __block_descriptor_tmp.6721
- __block_descriptor_tmp.68.4663
- __block_descriptor_tmp.6815
- __block_descriptor_tmp.6849
- __block_descriptor_tmp.69.1002
- __block_descriptor_tmp.69.4698
- __block_descriptor_tmp.7.4317
- __block_descriptor_tmp.7.6013
- __block_descriptor_tmp.7.6164
- __block_descriptor_tmp.7.6184
- __block_descriptor_tmp.7.6750
- __block_descriptor_tmp.7.839
- __block_descriptor_tmp.70.4694
- __block_descriptor_tmp.7001
- __block_descriptor_tmp.7196
- __block_descriptor_tmp.7363
- __block_descriptor_tmp.75.4794
- __block_descriptor_tmp.7596
- __block_descriptor_tmp.77.4795
- __block_descriptor_tmp.79.4792
- __block_descriptor_tmp.8.155
- __block_descriptor_tmp.8.6498
- __block_descriptor_tmp.8.7210
- __block_descriptor_tmp.8.847
- __block_descriptor_tmp.80.7213
- __block_descriptor_tmp.834
- __block_descriptor_tmp.9.4603
- __block_descriptor_tmp.90
- __block_descriptor_tmp.91.4766
- __block_descriptor_tmp.96
- __block_descriptor_tmp.979
- __block_literal_global.10.7206
- __block_literal_global.11.4601
- __block_literal_global.128
- __block_literal_global.135
- __block_literal_global.143
- __block_literal_global.1433
- __block_literal_global.145
- __block_literal_global.15.4319
- __block_literal_global.15.4607
- __block_literal_global.15.7483
- __block_literal_global.1526
- __block_literal_global.174
- __block_literal_global.19.4613
- __block_literal_global.20.4306
- __block_literal_global.211
- __block_literal_global.215
- __block_literal_global.2231
- __block_literal_global.226
- __block_literal_global.230
- __block_literal_global.2302
- __block_literal_global.234
- __block_literal_global.2400
- __block_literal_global.244
- __block_literal_global.248.5662
- __block_literal_global.252
- __block_literal_global.256
- __block_literal_global.2997
- __block_literal_global.33.4504
- __block_literal_global.3330
- __block_literal_global.3505
- __block_literal_global.36.4503
- __block_literal_global.3619
- __block_literal_global.381
- __block_literal_global.39.4494
- __block_literal_global.417
- __block_literal_global.43.6444
- __block_literal_global.4315
- __block_literal_global.4499
- __block_literal_global.4822
- __block_literal_global.5.6174
- __block_literal_global.5.6500
- __block_literal_global.53.4587
- __block_literal_global.5332
- __block_literal_global.5577
- __block_literal_global.5949
- __block_literal_global.6040
- __block_literal_global.6169
- __block_literal_global.6227
- __block_literal_global.6458
- __block_literal_global.6719
- __block_literal_global.6774
- __block_literal_global.6998
- __block_literal_global.7194
- __block_literal_global.7361
- __block_literal_global.7474
- __block_literal_global.7594
- __block_literal_global.8.1540
- __block_literal_global.8.2225
- __block_literal_global.832
- __block_literal_global.9.6047
- __block_literal_global.9.6182
- __block_literal_global.977
- __mdns_dns_service_manager_enumerate_all_services
- _initializeD2DPlugins
- _mDNSCoreInitComplete
- _mDNSMacOSXUpdateEtcHosts
- _mdns_address_create_from_ip_address_string
- _mdns_server_log.s_log.4320
- _mdns_server_log.s_once.4318
- _util_managed_network_change_handler
- g_nwi_state.4501
- g_session_list.4324
CStrings:
+ " \""
+ "\","
+ "%d.%d.%d"
+ "%s%u"
+ "%slocal-purview"
+ "%smdns-alternative"
+ "%x"
+ "%{public}sReceived %{mdns:acceptable}d %zu-byte response from %@ over %{mdns:protocol}d via %{public}s -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX, %{sensitive}@"
+ "%{public}sReceived %{mdns:acceptable}d %zu-byte response from %@ over %{mdns:protocol}d via %{public}s -- %{public,mdns:dnshdr}.*P, %{sensitive}@"
+ "%{public}sSent %zu-byte query #%u to %@ over %{mdns:protocol}d via %{public}s -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX, %{sensitive}@"
+ "%{public}sSent %zu-byte query #%u to %@ over %{mdns:protocol}d via %{public}s -- %{public,mdns:dnshdr}.*P, %{sensitive}@"
+ "%{public}sSent %zu-byte test query #%u to %@ over %{mdns:protocol}d via %{public}s -- %{public,mdns:dnshdr}.*P, %{sensitive}@"
+ "%{public}sWithholding unresponsive server symptom: Lack of response is for local. IN SOA query"
+ "-[UAPresenceManager updateCacheFromPresence]"
+ ".cxx_destruct"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "5"
+ "<INVALID REQUEST>"
+ "<INVALID RESULT>"
+ "<INVALID STATE>"
+ "@\"NSArray\""
+ "@\"NSMutableDictionary\""
+ "@\"SKPresence\""
+ "@24@0:8@?16"
+ "@24@0:8I16i20"
+ "Asynchronous trust evaluation failed: %@"
+ "B"
+ "B16@?0@\"NSDictionary\"8"
+ "B16@?0@\"NSNumber\"8"
+ "B16@?0@\"NSString\"8"
+ "B16@?0@\"SKPresentDevice\"8"
+ "B32@?0@\"NSDictionary\"8Q16^B24"
+ "B32@?0@\"SKPresentDevice\"8Q16^B24"
+ "B32@?0@\"UAQhash\"8Q16^B24"
+ "B32@?0@8Q16^B24"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "CLA"
+ "Creating DNS service from resolver config -- %@"
+ "DSYNC"
+ "Enabled read kevent for socket -- socket: %d"
+ "Failed to allocate empty dictionary for plist"
+ "Failed to copy value -- key: %{public}@, error: %{mdns:err}ld"
+ "Failed to create plist from file -- path: %{public}@, error: %{public}@"
+ "Failed to create read stream -- path: %{public}@"
+ "Failed to create write stream -- path: %{public}@"
+ "Failed to disable read kevent for mDNS socket -- socket: %d, error: %{mdns:err}ld"
+ "Failed to enable read kevent for socket -- socket: %d, error: %{mdns:err}ld"
+ "Failed to get temp directory -- error %{mdns:err}ld"
+ "Failed to open read stream -- path: %{public}@"
+ "Failed to open write stream -- path: %{public}@"
+ "Failed to post notification -- name: %{public}s, status: %u"
+ "Failed to start asynchronous trust evaluation -- provider name: %s, error: %{mdns:err}ld"
+ "Failed to write plist to file -- path: %{public}@, error: %{public}@"
+ "I16@0:8"
+ "IPN"
+ "NXNAME"
+ "OS_mdns_trust_state"
+ "ProductVersion"
+ "RESINFO"
+ "Removing record(s) -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d, rdata: %{sensitive, mask.hash, mdns:rdata}.*P, collectively: %{mdns:yesno}d"
+ "SKPresenceDelegate"
+ "SetupSocket: setting SO_TIMESTAMP_CONTINUOUS failed: %{public}s"
+ "T@\"NSArray\",&,N,V_lastAuthUpdate"
+ "T@\"NSArray\",&,N,V_networkAddrs"
+ "T@\"NSMutableDictionary\",&,N,V_authRecords"
+ "T@\"NSMutableDictionary\",&,N,V_skUpdates"
+ "T@\"SKPresence\",&,N,V_presence"
+ "TB,N,V_presenceAsserted"
+ "TB,N,V_presenceReady"
+ "TB,N,V_presenceSubscribed"
+ "TB,N,V_removed"
+ "TI,N,V_qhash"
+ "Temp directory path is empty"
+ "Temporarily disabled read kevent for mDNS socket -- socket: %d"
+ "Ti,N,V_authCheckTime"
+ "Ti,N,V_authUpdateTime"
+ "Ti,N,V_lastUnsubscribeTime"
+ "Ti,N,V_networkUpdateTime"
+ "Ti,N,V_presenceUpdateTime"
+ "Ti,N,V_time"
+ "UAPresence updateCacheFromPresence"
+ "UAPresenceManager"
+ "UAQhash"
+ "WALLET"
+ "WARNING: Processed %d messages from IPv%d mDNS socket in %d ms"
+ "WARNING: Processed %d messages from socket %d in %d ms"
+ "[Q%u] Handling concluded querier: %{sensitive}@"
+ "[R%u->Q%u] getaddrinfo result -- event: %{mdns:addrmv}d, ifindex: %d, name: %{sensitive}@, type: %{mdns:rrtype}d, rdata: %{sensitive}@, expired: %{mdns:yesno}d"
+ "[R%u->Q%u] getaddrinfo result -- event: %{mdns:addrmv}d, ifindex: %d, name: %{sensitive}@, type: %{mdns:rrtype}d, rdata: <none>, reason: %{mdns:nreason}d"
+ "[Sub%llu] Collectively removing record(s) -- name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %{mdns:rrtype}d"
+ "_addRecordsFromPresence:"
+ "_authCheckTime"
+ "_authRecords"
+ "_authUpdateTime"
+ "_lastAuthUpdate"
+ "_lastUnsubscribeTime"
+ "_mdns_trust_load_trust_info util_copy_trust_info err %d info %@\n"
+ "_networkAddrs"
+ "_networkUpdateTime"
+ "_presence"
+ "_presenceAsserted"
+ "_presenceReady"
+ "_presenceSubscribed"
+ "_presenceUpdateTime"
+ "_qhash"
+ "_removed"
+ "_skUpdates"
+ "_time"
+ "addDelegate:queue:"
+ "addQhash:forInterface:"
+ "addr"
+ "appendFormat:"
+ "appendString:"
+ "array"
+ "assertPresence:"
+ "assertPresenceWithPresencePayload:assertionOptions:completion:"
+ "assertionTime"
+ "authCheckTime"
+ "authRecords"
+ "authUpdateTime"
+ "auth_records"
+ "background"
+ "bonjour_services_array"
+ "boolValue"
+ "bytes"
+ "com.apple.mDNSResponder.unicast_assist.SKPresence"
+ "com.apple.mrcs.prefs-changed.ahared-assist-cache"
+ "com.apple.private.mDNSResponder.shared-assist-cache"
+ "compare:"
+ "dataWithBytes:length:"
+ "describeAddr"
+ "describeQHashes"
+ "describeUAQHashes"
+ "deviceIdentifier"
+ "effectiveBundleIdentifier"
+ "effective_bundle_id"
+ "effective_bundle_id %s status \"%s\" flags 0x%x"
+ "enable"
+ "executable_path"
+ "filterObjectsUsingBlock:"
+ "had_invalid_addr"
+ "handleAuthCheck:"
+ "handleNetworkUpdate:"
+ "hasInitialCloudKitImportOccurredWithCompletion:"
+ "i"
+ "i16@0:8"
+ "idlePresence:"
+ "ifhash"
+ "ifid"
+ "indexOfObjectPassingTest:"
+ "indexesOfObjectsPassingTest:"
+ "init"
+ "initQhash:withTime:"
+ "initWithDictionary:"
+ "initWithPresenceIdentifier:options:"
+ "initWithPriority:"
+ "initWithServiceIdentifier:"
+ "initialCloudKitImportReceived:"
+ "interactive"
+ "invitedHandlesChangedForPresence:"
+ "isEqualToArray:"
+ "isEqualToNumber:"
+ "isSelfDevice"
+ "is_apple_internal"
+ "kCFAllocatorNull"
+ "known"
+ "lastAuthUpdate"
+ "lastUnsubscribeTime"
+ "mDNSPlatformInitDNSProxySkts: Failed to create listening sockets"
+ "mDNSResponder-2862.0.0.0.1"
+ "mdns_trust_state"
+ "mrcs_prefs"
+ "mrcs_prefs.plist"
+ "networkAddrs"
+ "networkUpdateTime"
+ "no_entitlement"
+ "objectAtIndex:"
+ "objectsAtIndexes:"
+ "payloadDictionary"
+ "plist read from file is not a dictionary -- path: %{public}@"
+ "presence"
+ "presence only"
+ "presenceAsserted"
+ "presenceAssertionForPresence:completedSuccessfully:error:"
+ "presenceDaemonDisconnected:"
+ "presencePayload"
+ "presenceReady"
+ "presenceSubscribed"
+ "presenceUpdateTime"
+ "presentDevices"
+ "presentDevicesChangedForPresence:"
+ "qhash"
+ "qhash:withTime:"
+ "realtime"
+ "releasePresenceWithCompletion:"
+ "releaseSubscriptions"
+ "releaseTransientSubscriptionAssertionWithCompletion:"
+ "removeObjectsAtIndexes:"
+ "removeQhash:forInterface:"
+ "retainSubscription"
+ "retainTransientSubscriptionAssertionWithCompletion:"
+ "sdk_build_version"
+ "setAuthCheckTime:"
+ "setAuthRecords:"
+ "setAuthUpdateTime:"
+ "setIsDaemonIdleExitEnabled:"
+ "setIsPersonal:"
+ "setLastAuthUpdate:"
+ "setLastUnsubscribeTime:"
+ "setNetworkAddrs:"
+ "setNetworkUpdateTime:"
+ "setObject:forKey:"
+ "setPresence:"
+ "setPresenceAsserted:"
+ "setPresenceReady:"
+ "setPresenceSubscribed:"
+ "setPresenceUpdateTime:"
+ "setQhash:"
+ "setRemoved:"
+ "setSkUpdates:"
+ "setTime:"
+ "shared-assist-cache.enable"
+ "shared_assist_cache.enablement"
+ "skUpdates"
+ "sla"
+ "sla%u"
+ "ua_extension"
+ "unicast assist (restart) - no active question for qnamehash %x"
+ "unicast assist SKPresence assertPresenceWithCompletion: %{public}@"
+ "unicast assist SKPresence dealloc:"
+ "unicast assist SKPresence hasInitialCloudKitImportOccurredWithCompletion: %d"
+ "unicast assist SKPresence hasInitialCloudKitImportOccurredWithCompletion: %{public}@"
+ "unicast assist SKPresence init: _presence %{public}@"
+ "unicast assist SKPresence initialCloudKitImportReceived called"
+ "unicast assist SKPresence releasePresenceWithCompletion: %{public}@"
+ "unicast assist SKPresence releaseSubscriptions: %{public}@"
+ "unicast assist SKPresence releaseTransientSubscriptionAssertionWithCompletion: %{public}@"
+ "unicast assist SKPresence retainSubscription"
+ "unicast assist SKPresence retainTransientSubscriptionAssertionWithCompletion: %{public}@"
+ "unicast assist _addRecordsFromPresence: (error) qhash %x addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P err %d"
+ "unicast assist _addRecordsFromPresence: add qhashes %@ addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P ifhash %x"
+ "unicast assist _addRecordsFromPresence: no subnet for addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
+ "unicast assist _addRecordsFromPresence: restarted (%s) qhash %x addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P"
+ "unicast assist _unicate_assist_data_to_addr bad addr size %lu"
+ "unicast assist assertPresence (auth) qhashes %@ addr %{sensitive, mask.hash}@ ifid %2.2u ifhash %x"
+ "unicast assist handleAuthCheck aged out %@ qhashes ifid %2.2u"
+ "unicast assist handleNetworkUpdate (changed) was %lu now %lu"
+ "unicast assist mrcs_prefs_monitor_shared_assist_cache_changes s_shared_cache_enabled (%{bool}d) -> (%{bool}d)"
+ "unicast assist updateCacheFromPresence: (removed) FAILED qhash %x addr %{sensitive, mask.hash}@ err %d"
+ "unicast assist updateCacheFromPresence: next (auth) count %lu from %@ time %@"
+ "unicast assist updateCacheFromPresence: remove diffed (auth) count %lu from %@"
+ "unicast assist updateCacheFromPresence: remove missing device (auth) count %lu from %@"
+ "unicast assist updateCacheFromPresence: remove qhashes %@ addr %{sensitive, mask.hash}@ ifhash %x"
+ "unicast assist updateCacheFromPresence: skipping stale update from %@ time %@"
+ "unicast assist updateCacheFromPresence: skipping version %@ from %@ expected %@"
+ "unicast assist updateInvalidFromPresence: next (auth) count %lu from %@ time %@"
+ "updateCacheFromPresence"
+ "updateInvalidFromPresence"
+ "util_copy_trust_info bundleRecordForAuditToken %{public}@\n"
+ "v16@?0@\"NSError\"8"
+ "v20@0:8B16"
+ "v20@0:8I16"
+ "v20@0:8i16"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"SKPresence\"16"
+ "v28@0:8I16^{mDNSInterfaceID_dummystruct=^v}20"
+ "v32@?0@\"UAQhash\"8Q16^B24"
+ "v36@0:8@\"SKPresence\"16B24@\"NSError\"28"
+ "v36@0:8@16B24@28"
+ "version"
- "%{public}sReceived %{mdns:acceptable}d %zu-byte response from %@ over %{mdns:protocol}d via %{public}s -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX, %{public}s"
- "%{public}sReceived %{mdns:acceptable}d %zu-byte response from %@ over %{mdns:protocol}d via %{public}s -- %{public,mdns:dnshdr}.*P, %{public}s"
- "%{public}sSent %zu-byte query #%u to %@ over %{mdns:protocol}d via %{public}s -- %{mdns:dns.idflags}08lX, counts: %{mdns:dns.counts}016llX, %{public}s"
- "%{public}sSent %zu-byte query #%u to %@ over %{mdns:protocol}d via %{public}s -- %{public,mdns:dnshdr}.*P, %{public}s"
- "%{public}sSent %zu-byte test query #%u to %@ over %{mdns:protocol}d via %{public}s -- %{public,mdns:dnshdr}.*P, %{public}s"
- "[Q%u] Handling concluded querier: %{public}s"
- "[R%u->Q%u] getaddrinfo result -- event: %{mdns:addrmv}d, ifindex: %d, name: %{public}s, type: %{mdns:rrtype}d, rdata: %{public}s, expired: %{mdns:yesno}d"
- "[R%u->Q%u] getaddrinfo result -- event: %{mdns:addrmv}d, ifindex: %d, name: %{public}s, type: %{mdns:rrtype}d, rdata: <none>, reason: %{mdns:nreason}d"
- "_mdns_trust_checks_bundle_record_for_app bundleRecordForAuditToken %{public}@\n"
- "mDNSResponder-2600.120.12"

```
