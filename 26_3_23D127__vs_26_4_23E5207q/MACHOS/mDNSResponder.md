## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2881.80.4.0.1
-  __TEXT.__text: 0x106c14
-  __TEXT.__auth_stubs: 0x2f00
-  __TEXT.__objc_stubs: 0x1d00
-  __TEXT.__objc_methlist: 0x664
-  __TEXT.__const: 0x1180
-  __TEXT.__cstring: 0x17588
-  __TEXT.__gcc_except_tab: 0x334
-  __TEXT.__oslogstring: 0x1ef61
+2881.100.53.0.0
+  __TEXT.__text: 0x107458
+  __TEXT.__auth_stubs: 0x2ef0
+  __TEXT.__objc_stubs: 0x2020
+  __TEXT.__objc_methlist: 0x694
+  __TEXT.__const: 0x1170
+  __TEXT.__cstring: 0x178ff
+  __TEXT.__gcc_except_tab: 0x338
+  __TEXT.__oslogstring: 0x1f627
   __TEXT.__objc_classname: 0x649
-  __TEXT.__objc_methname: 0x1b39
-  __TEXT.__objc_methtype: 0x62a
-  __TEXT.__unwind_info: 0x1658
+  __TEXT.__objc_methname: 0x1db6
+  __TEXT.__objc_methtype: 0x64d
+  __TEXT.__unwind_info: 0x16a0
   __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x1790
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__auth_got: 0x1788
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x6478
-  __DATA_CONST.__cfstring: 0x1160
+  __DATA_CONST.__const: 0x6400
+  __DATA_CONST.__cfstring: 0x11a0
   __DATA_CONST.__objc_classlist: 0x1d8
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x4138
-  __DATA.__objc_selrefs: 0x8f0
+  __DATA.__objc_const: 0x4188
+  __DATA.__objc_selrefs: 0x9c0
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x1270
   __DATA.__data: 0x4328
-  __DATA.__bss: 0x16de0
+  __DATA.__bss: 0x16df8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 08A24F14-F1AD-3A76-A11B-0D2AF14D60F5
-  Functions: 1838
-  Symbols:   4577
-  CStrings:  4854
+  UUID: D1CD2E05-8D0F-3817-A2FC-668BBBB8B694
+  Functions: 1844
+  Symbols:   4607
+  CStrings:  4911
 
Symbols:
+ -[NSDictionary(ua_extension) mutableCopyDeep]
+ -[UAPresenceManager reloadFromPresence:]
+ FreeARElemCallback.2649
+ GCC_except_table1220
+ GCC_except_table1226
+ GCC_except_table1394
+ GCC_except_table1591
+ GCC_except_table1811
+ _CFPropertyListIsValid
+ _CFReadStreamRead
+ _CFWriteStreamWrite
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSInputStream
+ _OBJC_CLASS_$_NSOutputStream
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _UAStreamTag_addr
+ _UAStreamTag_interface
+ _UAStreamTag_qhash
+ _UAStreamTag_version
+ _UAStream_version
+ __36-[UAPresenceManager assertPresence:]_block_invoke.93
+ __41-[UAPresenceManager releaseSubscriptions]_block_invoke.57
+ __44-[UAPresenceManager updateCacheFromPresence]_block_invoke.119
+ __44-[UAPresenceManager updateCacheFromPresence]_block_invoke_2.120
+ __Block_byref_object_copy_.923
+ __Block_byref_object_dispose_.924
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_ua_extension
+ __OBJC_$_CATEGORY_NSDictionary_$_ua_extension
+ ____mdns_dns_service_manager_update_config_snapshots_block_invoke
+ ____task_log_block_invoke
+ ___background_task_repeating_daily_register_block_invoke
+ ___block_descriptor_40_e8_32bs_e22_v16?0"BGSystemTask"8ls32l8
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6346
+ ___mdns_dns_service_manager_probe_discovered_service_block_invoke.235
+ ___mdns_dns_service_manager_probe_discovered_service_block_invoke_2.236
+ ___mdns_server_log_block_invoke.4358
+ ___unicast_assist_hash_for_interface_block_invoke.337
+ __block_descriptor_tmp.1.6314
+ __block_descriptor_tmp.10.4341
+ __block_descriptor_tmp.10.6144
+ __block_descriptor_tmp.11.6340
+ __block_descriptor_tmp.11.6704
+ __block_descriptor_tmp.11.862
+ __block_descriptor_tmp.12.6151
+ __block_descriptor_tmp.12.6701
+ __block_descriptor_tmp.12.863
+ __block_descriptor_tmp.120.4850
+ __block_descriptor_tmp.121.4843
+ __block_descriptor_tmp.122.4867
+ __block_descriptor_tmp.129
+ __block_descriptor_tmp.13.4357
+ __block_descriptor_tmp.13.4743
+ __block_descriptor_tmp.13.6152
+ __block_descriptor_tmp.130.4797
+ __block_descriptor_tmp.131
+ __block_descriptor_tmp.133.3661
+ __block_descriptor_tmp.14.1068
+ __block_descriptor_tmp.14.3276
+ __block_descriptor_tmp.14.876
+ __block_descriptor_tmp.140.4821
+ __block_descriptor_tmp.1455
+ __block_descriptor_tmp.148.948
+ __block_descriptor_tmp.149
+ __block_descriptor_tmp.15.6106
+ __block_descriptor_tmp.150
+ __block_descriptor_tmp.1540
+ __block_descriptor_tmp.16.6351
+ __block_descriptor_tmp.17.1069
+ __block_descriptor_tmp.17.4141
+ __block_descriptor_tmp.17.4747
+ __block_descriptor_tmp.17.6107
+ __block_descriptor_tmp.17.6695
+ __block_descriptor_tmp.17.903
+ __block_descriptor_tmp.173
+ __block_descriptor_tmp.179
+ __block_descriptor_tmp.18.3284
+ __block_descriptor_tmp.18.4281
+ __block_descriptor_tmp.18.4329
+ __block_descriptor_tmp.18.6113
+ __block_descriptor_tmp.18.6708
+ __block_descriptor_tmp.18.905
+ __block_descriptor_tmp.19.6101
+ __block_descriptor_tmp.19.906
+ __block_descriptor_tmp.2.4215
+ __block_descriptor_tmp.2.7018
+ __block_descriptor_tmp.20.6146
+ __block_descriptor_tmp.20.6989
+ __block_descriptor_tmp.20.907
+ __block_descriptor_tmp.20.996
+ __block_descriptor_tmp.208
+ __block_descriptor_tmp.21.4284
+ __block_descriptor_tmp.21.4740
+ __block_descriptor_tmp.21.7004
+ __block_descriptor_tmp.22.1550
+ __block_descriptor_tmp.22.3286
+ __block_descriptor_tmp.22.4344
+ __block_descriptor_tmp.22.6147
+ __block_descriptor_tmp.225
+ __block_descriptor_tmp.227
+ __block_descriptor_tmp.23.1557
+ __block_descriptor_tmp.23.6990
+ __block_descriptor_tmp.2308
+ __block_descriptor_tmp.232
+ __block_descriptor_tmp.233.5789
+ __block_descriptor_tmp.238.2994
+ __block_descriptor_tmp.24.1558
+ __block_descriptor_tmp.24.3315
+ __block_descriptor_tmp.24.6142
+ __block_descriptor_tmp.2411
+ __block_descriptor_tmp.248
+ __block_descriptor_tmp.249.2791
+ __block_descriptor_tmp.25.1066
+ __block_descriptor_tmp.25.3339
+ __block_descriptor_tmp.25.6991
+ __block_descriptor_tmp.250
+ __block_descriptor_tmp.251.5872
+ __block_descriptor_tmp.255.5869
+ __block_descriptor_tmp.26.1559
+ __block_descriptor_tmp.26.4737
+ __block_descriptor_tmp.26.6139
+ __block_descriptor_tmp.2662
+ __block_descriptor_tmp.27.1560
+ __block_descriptor_tmp.27.6136
+ __block_descriptor_tmp.27.6996
+ __block_descriptor_tmp.27.963
+ __block_descriptor_tmp.28.6134
+ __block_descriptor_tmp.28.6997
+ __block_descriptor_tmp.29.1562
+ __block_descriptor_tmp.29.3344
+ __block_descriptor_tmp.29.6097
+ __block_descriptor_tmp.29.6998
+ __block_descriptor_tmp.3.1002
+ __block_descriptor_tmp.3.1544
+ __block_descriptor_tmp.3.2309
+ __block_descriptor_tmp.3.4218
+ __block_descriptor_tmp.3.6160
+ __block_descriptor_tmp.3.6317
+ __block_descriptor_tmp.3.6344
+ __block_descriptor_tmp.3.6697
+ __block_descriptor_tmp.3.7406
+ __block_descriptor_tmp.3.7566
+ __block_descriptor_tmp.30.6125
+ __block_descriptor_tmp.30.6982
+ __block_descriptor_tmp.31.3356
+ __block_descriptor_tmp.32.4345
+ __block_descriptor_tmp.32.6127
+ __block_descriptor_tmp.3204
+ __block_descriptor_tmp.33.1564
+ __block_descriptor_tmp.33.6988
+ __block_descriptor_tmp.34.1573
+ __block_descriptor_tmp.34.3227
+ __block_descriptor_tmp.34.6976
+ __block_descriptor_tmp.35.1572
+ __block_descriptor_tmp.35.7005
+ __block_descriptor_tmp.3515
+ __block_descriptor_tmp.3594
+ __block_descriptor_tmp.36.4752
+ __block_descriptor_tmp.38.1048
+ __block_descriptor_tmp.38.3228
+ __block_descriptor_tmp.38.4749
+ __block_descriptor_tmp.388.2595
+ __block_descriptor_tmp.39.1056
+ __block_descriptor_tmp.39.6076
+ __block_descriptor_tmp.4.4219
+ __block_descriptor_tmp.4.4331
+ __block_descriptor_tmp.4.4952
+ __block_descriptor_tmp.4.6161
+ __block_descriptor_tmp.4.6321
+ __block_descriptor_tmp.40.1566
+ __block_descriptor_tmp.40.4732
+ __block_descriptor_tmp.41.1052
+ __block_descriptor_tmp.41.1567
+ __block_descriptor_tmp.4143
+ __block_descriptor_tmp.4179
+ __block_descriptor_tmp.42.3225
+ __block_descriptor_tmp.4210
+ __block_descriptor_tmp.43.4716
+ __block_descriptor_tmp.4326
+ __block_descriptor_tmp.45.4711
+ __block_descriptor_tmp.47.3211
+ __block_descriptor_tmp.47.5477
+ __block_descriptor_tmp.4792
+ __block_descriptor_tmp.48.3277
+ __block_descriptor_tmp.48.4953
+ __block_descriptor_tmp.5.2320
+ __block_descriptor_tmp.5.4220
+ __block_descriptor_tmp.5.4332
+ __block_descriptor_tmp.5.4958
+ __block_descriptor_tmp.5.6162
+ __block_descriptor_tmp.50.4819
+ __block_descriptor_tmp.51.1038
+ __block_descriptor_tmp.51.3221
+ __block_descriptor_tmp.51.4727
+ __block_descriptor_tmp.5230
+ __block_descriptor_tmp.534
+ __block_descriptor_tmp.5465
+ __block_descriptor_tmp.55.1046
+ __block_descriptor_tmp.56.7466
+ __block_descriptor_tmp.58.1054
+ __block_descriptor_tmp.5897
+ __block_descriptor_tmp.59.3345
+ __block_descriptor_tmp.6.1578
+ __block_descriptor_tmp.6.4192
+ __block_descriptor_tmp.6.4333
+ __block_descriptor_tmp.6.6325
+ __block_descriptor_tmp.6.999
+ __block_descriptor_tmp.60.3348
+ __block_descriptor_tmp.60.7459
+ __block_descriptor_tmp.61.1043
+ __block_descriptor_tmp.61.3346
+ __block_descriptor_tmp.611
+ __block_descriptor_tmp.62.3359
+ __block_descriptor_tmp.62.6121
+ __block_descriptor_tmp.63.4698
+ __block_descriptor_tmp.6310
+ __block_descriptor_tmp.6336
+ __block_descriptor_tmp.6396
+ __block_descriptor_tmp.64.1010
+ __block_descriptor_tmp.6583
+ __block_descriptor_tmp.6689
+ __block_descriptor_tmp.69.1015
+ __block_descriptor_tmp.69.4830
+ __block_descriptor_tmp.6925
+ __block_descriptor_tmp.7.4177
+ __block_descriptor_tmp.7.4336
+ __block_descriptor_tmp.7.6164
+ __block_descriptor_tmp.7.6328
+ __block_descriptor_tmp.7.6349
+ __block_descriptor_tmp.7.6954
+ __block_descriptor_tmp.7.850
+ __block_descriptor_tmp.70.1016
+ __block_descriptor_tmp.70.4826
+ __block_descriptor_tmp.7019
+ __block_descriptor_tmp.702
+ __block_descriptor_tmp.7053
+ __block_descriptor_tmp.7205
+ __block_descriptor_tmp.7400
+ __block_descriptor_tmp.7562
+ __block_descriptor_tmp.76.4930
+ __block_descriptor_tmp.76.7409
+ __block_descriptor_tmp.7768
+ __block_descriptor_tmp.78.7438
+ __block_descriptor_tmp.8.157
+ __block_descriptor_tmp.8.4175
+ __block_descriptor_tmp.8.6690
+ __block_descriptor_tmp.8.857
+ __block_descriptor_tmp.80.4928
+ __block_descriptor_tmp.81.846
+ __block_descriptor_tmp.84
+ __block_descriptor_tmp.9.4182
+ __block_descriptor_tmp.9.4735
+ __block_descriptor_tmp.91.4902
+ __block_descriptor_tmp.93.4900
+ __block_descriptor_tmp.992
+ __block_literal_global.103
+ __block_literal_global.11.4733
+ __block_literal_global.118
+ __block_literal_global.135
+ __block_literal_global.139.847
+ __block_literal_global.1442
+ __block_literal_global.145
+ __block_literal_global.15.4338
+ __block_literal_global.15.4739
+ __block_literal_global.15.7684
+ __block_literal_global.1535
+ __block_literal_global.176
+ __block_literal_global.19.4745
+ __block_literal_global.20.4325
+ __block_literal_global.2236
+ __block_literal_global.2307
+ __block_literal_global.2405
+ __block_literal_global.253.5798
+ __block_literal_global.257.5801
+ __block_literal_global.276
+ __block_literal_global.279
+ __block_literal_global.3001
+ __block_literal_global.306.4517
+ __block_literal_global.324
+ __block_literal_global.3337
+ __block_literal_global.334
+ __block_literal_global.336
+ __block_literal_global.340
+ __block_literal_global.3513
+ __block_literal_global.3625
+ __block_literal_global.386
+ __block_literal_global.422
+ __block_literal_global.43.6637
+ __block_literal_global.4334
+ __block_literal_global.4585
+ __block_literal_global.4956
+ __block_literal_global.5.6339
+ __block_literal_global.5.6692
+ __block_literal_global.5.7404
+ __block_literal_global.53.4719
+ __block_literal_global.5464
+ __block_literal_global.5715
+ __block_literal_global.59
+ __block_literal_global.607
+ __block_literal_global.6099
+ __block_literal_global.6203
+ __block_literal_global.6334
+ __block_literal_global.6392
+ __block_literal_global.643
+ __block_literal_global.6576
+ __block_literal_global.6651
+ __block_literal_global.6923
+ __block_literal_global.6978
+ __block_literal_global.698
+ __block_literal_global.7202
+ __block_literal_global.7398
+ __block_literal_global.7560
+ __block_literal_global.7675
+ __block_literal_global.7766
+ __block_literal_global.8.1549
+ __block_literal_global.8.2230
+ __block_literal_global.80
+ __block_literal_global.86
+ __block_literal_global.9.6347
+ __block_literal_global.95
+ __block_literal_global.990
+ __mdns_dns_service_set_config_and_snapshot
+ __mdns_odoh_config_hash
+ __task_log
+ __unicast_assist_persistance_cache_read_tag
+ __unicast_assist_persistance_create_url
+ _dns_record_type_value_to_string
+ _mdns_server_log.s_log.4339
+ _mdns_server_log.s_once.4337
+ _nw_resolver_config_copy_dictionary
+ _objc_msgSend$URLsForDirectory:inDomains:
+ _objc_msgSend$close
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$hasBytesAvailable
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$inputStreamWithURL:
+ _objc_msgSend$isFileURL
+ _objc_msgSend$lastObject
+ _objc_msgSend$mutableCopyDeep
+ _objc_msgSend$open
+ _objc_msgSend$outputStreamWithURL:append:
+ _objc_msgSend$read:maxLength:
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$reloadFromPresence:
+ _objc_msgSend$setInterval:
+ _objc_msgSend$setSkUpdates:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$taskRequestForIdentifier:
+ _objc_msgSend$write:maxLength:
+ _objc_msgSend$writePropertyList:toStream:format:options:error:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _task_log.s_log
+ _task_log.s_once
+ _unicast_assist_cache_purge
+ _unicast_assist_persistance_presence_load_from_store.s_loaded
+ g_nwi_state.4567
+ g_session_list.4343
- -[UAPresenceManager updateInvalidFromPresence]
- FreeARElemCallback.2638
- GCC_except_table1221
- GCC_except_table1227
- GCC_except_table1391
- GCC_except_table1586
- GCC_except_table1809
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_INTERVAL_5_MIN
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _XPC_ACTIVITY_REPEATING
- __36-[UAPresenceManager assertPresence:]_block_invoke.92
- __41-[UAPresenceManager releaseSubscriptions]_block_invoke.56
- __44-[UAPresenceManager updateCacheFromPresence]_block_invoke.116
- __44-[UAPresenceManager updateCacheFromPresence]_block_invoke_2.117
- __Block_byref_object_copy_.915
- __Block_byref_object_dispose_.916
- ____mdns_dns_service_manager_finalize_block_invoke
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6323
- ___mdns_dns_service_manager_create_block_invoke
- ___mdns_dns_service_manager_probe_discovered_service_block_invoke.231
- ___mdns_dns_service_manager_probe_discovered_service_block_invoke_2.232
- ___mdns_server_log_block_invoke.4347
- ___unicast_assist_hash_for_interface_block_invoke.319
- __block_descriptor_tmp.1.6291
- __block_descriptor_tmp.10.4330
- __block_descriptor_tmp.10.6113
- __block_descriptor_tmp.11.6317
- __block_descriptor_tmp.11.6681
- __block_descriptor_tmp.11.854
- __block_descriptor_tmp.115.4837
- __block_descriptor_tmp.117
- __block_descriptor_tmp.119.4817
- __block_descriptor_tmp.12.6120
- __block_descriptor_tmp.12.6678
- __block_descriptor_tmp.12.855
- __block_descriptor_tmp.120.4819
- __block_descriptor_tmp.121.4811
- __block_descriptor_tmp.122.4836
- __block_descriptor_tmp.13.4346
- __block_descriptor_tmp.13.4711
- __block_descriptor_tmp.13.6121
- __block_descriptor_tmp.130.4765
- __block_descriptor_tmp.134
- __block_descriptor_tmp.14.1059
- __block_descriptor_tmp.14.3265
- __block_descriptor_tmp.14.867
- __block_descriptor_tmp.140.4789
- __block_descriptor_tmp.144
- __block_descriptor_tmp.1444
- __block_descriptor_tmp.145.939
- __block_descriptor_tmp.15.6075
- __block_descriptor_tmp.1529
- __block_descriptor_tmp.16.6328
- __block_descriptor_tmp.17.1060
- __block_descriptor_tmp.17.4130
- __block_descriptor_tmp.17.4715
- __block_descriptor_tmp.17.6076
- __block_descriptor_tmp.17.6672
- __block_descriptor_tmp.17.895
- __block_descriptor_tmp.170
- __block_descriptor_tmp.18.3273
- __block_descriptor_tmp.18.4270
- __block_descriptor_tmp.18.4318
- __block_descriptor_tmp.18.6082
- __block_descriptor_tmp.18.6685
- __block_descriptor_tmp.18.897
- __block_descriptor_tmp.183
- __block_descriptor_tmp.19.6070
- __block_descriptor_tmp.19.898
- __block_descriptor_tmp.2.4204
- __block_descriptor_tmp.2.6995
- __block_descriptor_tmp.20.6115
- __block_descriptor_tmp.20.6966
- __block_descriptor_tmp.20.899
- __block_descriptor_tmp.20.988
- __block_descriptor_tmp.204
- __block_descriptor_tmp.21.4273
- __block_descriptor_tmp.21.4708
- __block_descriptor_tmp.21.6981
- __block_descriptor_tmp.213
- __block_descriptor_tmp.22.1539
- __block_descriptor_tmp.22.3275
- __block_descriptor_tmp.22.4333
- __block_descriptor_tmp.22.6116
- __block_descriptor_tmp.220
- __block_descriptor_tmp.223
- __block_descriptor_tmp.226
- __block_descriptor_tmp.2297
- __block_descriptor_tmp.23.1546
- __block_descriptor_tmp.23.6967
- __block_descriptor_tmp.233.5761
- __block_descriptor_tmp.236.2990
- __block_descriptor_tmp.24.1547
- __block_descriptor_tmp.24.3304
- __block_descriptor_tmp.24.6111
- __block_descriptor_tmp.2400
- __block_descriptor_tmp.242
- __block_descriptor_tmp.243
- __block_descriptor_tmp.245.2984
- __block_descriptor_tmp.25.1057
- __block_descriptor_tmp.25.3328
- __block_descriptor_tmp.25.6968
- __block_descriptor_tmp.251.5841
- __block_descriptor_tmp.26.1548
- __block_descriptor_tmp.26.4705
- __block_descriptor_tmp.26.6108
- __block_descriptor_tmp.2651
- __block_descriptor_tmp.27.1549
- __block_descriptor_tmp.27.6105
- __block_descriptor_tmp.27.6973
- __block_descriptor_tmp.27.954
- __block_descriptor_tmp.28.6103
- __block_descriptor_tmp.28.6974
- __block_descriptor_tmp.29.1551
- __block_descriptor_tmp.29.3333
- __block_descriptor_tmp.29.6066
- __block_descriptor_tmp.29.6975
- __block_descriptor_tmp.3.1533
- __block_descriptor_tmp.3.2298
- __block_descriptor_tmp.3.4207
- __block_descriptor_tmp.3.6129
- __block_descriptor_tmp.3.6294
- __block_descriptor_tmp.3.6321
- __block_descriptor_tmp.3.6674
- __block_descriptor_tmp.3.7550
- __block_descriptor_tmp.3.994
- __block_descriptor_tmp.30.6094
- __block_descriptor_tmp.30.6959
- __block_descriptor_tmp.31.3345
- __block_descriptor_tmp.3193
- __block_descriptor_tmp.32.4334
- __block_descriptor_tmp.32.6096
- __block_descriptor_tmp.33.1553
- __block_descriptor_tmp.33.6965
- __block_descriptor_tmp.34.1562
- __block_descriptor_tmp.34.3216
- __block_descriptor_tmp.34.6953
- __block_descriptor_tmp.35.1561
- __block_descriptor_tmp.35.6982
- __block_descriptor_tmp.3504
- __block_descriptor_tmp.3583
- __block_descriptor_tmp.36.4720
- __block_descriptor_tmp.38.1039
- __block_descriptor_tmp.38.3217
- __block_descriptor_tmp.38.4717
- __block_descriptor_tmp.39.1047
- __block_descriptor_tmp.39.6045
- __block_descriptor_tmp.392
- __block_descriptor_tmp.4.4208
- __block_descriptor_tmp.4.4320
- __block_descriptor_tmp.4.4920
- __block_descriptor_tmp.4.6130
- __block_descriptor_tmp.4.6298
- __block_descriptor_tmp.4.7381
- __block_descriptor_tmp.40.1555
- __block_descriptor_tmp.40.4700
- __block_descriptor_tmp.41.1043
- __block_descriptor_tmp.41.1556
- __block_descriptor_tmp.4132
- __block_descriptor_tmp.4168
- __block_descriptor_tmp.4199
- __block_descriptor_tmp.42.3214
- __block_descriptor_tmp.43.4684
- __block_descriptor_tmp.4315
- __block_descriptor_tmp.45.4679
- __block_descriptor_tmp.47.3200
- __block_descriptor_tmp.47.5449
- __block_descriptor_tmp.4760
- __block_descriptor_tmp.48.3266
- __block_descriptor_tmp.48.4921
- __block_descriptor_tmp.5.2309
- __block_descriptor_tmp.5.4209
- __block_descriptor_tmp.5.4321
- __block_descriptor_tmp.5.4926
- __block_descriptor_tmp.5.6131
- __block_descriptor_tmp.50.4787
- __block_descriptor_tmp.51.1030
- __block_descriptor_tmp.51.3210
- __block_descriptor_tmp.51.4695
- __block_descriptor_tmp.5198
- __block_descriptor_tmp.536
- __block_descriptor_tmp.5437
- __block_descriptor_tmp.55.1038
- __block_descriptor_tmp.58.1045
- __block_descriptor_tmp.5866
- __block_descriptor_tmp.59.3334
- __block_descriptor_tmp.6.1567
- __block_descriptor_tmp.6.4181
- __block_descriptor_tmp.6.4322
- __block_descriptor_tmp.6.6302
- __block_descriptor_tmp.6.991
- __block_descriptor_tmp.60.3337
- __block_descriptor_tmp.60.7450
- __block_descriptor_tmp.61.1035
- __block_descriptor_tmp.61.3335
- __block_descriptor_tmp.614
- __block_descriptor_tmp.62.3348
- __block_descriptor_tmp.62.6090
- __block_descriptor_tmp.6287
- __block_descriptor_tmp.63.4666
- __block_descriptor_tmp.6313
- __block_descriptor_tmp.6373
- __block_descriptor_tmp.64.1002
- __block_descriptor_tmp.64.7443
- __block_descriptor_tmp.6560
- __block_descriptor_tmp.6666
- __block_descriptor_tmp.69.1007
- __block_descriptor_tmp.69.4798
- __block_descriptor_tmp.6902
- __block_descriptor_tmp.693
- __block_descriptor_tmp.6996
- __block_descriptor_tmp.7.4166
- __block_descriptor_tmp.7.4325
- __block_descriptor_tmp.7.6133
- __block_descriptor_tmp.7.6305
- __block_descriptor_tmp.7.6326
- __block_descriptor_tmp.7.6931
- __block_descriptor_tmp.7.841
- __block_descriptor_tmp.70.1008
- __block_descriptor_tmp.70.4794
- __block_descriptor_tmp.7030
- __block_descriptor_tmp.7182
- __block_descriptor_tmp.7377
- __block_descriptor_tmp.7546
- __block_descriptor_tmp.76.4898
- __block_descriptor_tmp.7756
- __block_descriptor_tmp.8.161
- __block_descriptor_tmp.8.4164
- __block_descriptor_tmp.8.6667
- __block_descriptor_tmp.8.7391
- __block_descriptor_tmp.8.849
- __block_descriptor_tmp.80.4896
- __block_descriptor_tmp.80.7394
- __block_descriptor_tmp.81
- __block_descriptor_tmp.82
- __block_descriptor_tmp.835
- __block_descriptor_tmp.88
- __block_descriptor_tmp.9.4171
- __block_descriptor_tmp.9.4703
- __block_descriptor_tmp.91.4870
- __block_descriptor_tmp.93.4868
- __block_descriptor_tmp.984
- __block_literal_global.10.7387
- __block_literal_global.11.4701
- __block_literal_global.115
- __block_literal_global.132
- __block_literal_global.136
- __block_literal_global.142.959
- __block_literal_global.1431
- __block_literal_global.15.4327
- __block_literal_global.15.4707
- __block_literal_global.15.7670
- __block_literal_global.1524
- __block_literal_global.180
- __block_literal_global.19.4713
- __block_literal_global.20.4314
- __block_literal_global.2225
- __block_literal_global.2296
- __block_literal_global.2394
- __block_literal_global.249
- __block_literal_global.253.5770
- __block_literal_global.267
- __block_literal_global.270
- __block_literal_global.28.6181
- __block_literal_global.2989
- __block_literal_global.299
- __block_literal_global.312.4558
- __block_literal_global.316
- __block_literal_global.318
- __block_literal_global.322
- __block_literal_global.3326
- __block_literal_global.3502
- __block_literal_global.3614
- __block_literal_global.390.2584
- __block_literal_global.426
- __block_literal_global.43.6614
- __block_literal_global.4323
- __block_literal_global.4575
- __block_literal_global.4924
- __block_literal_global.5.6316
- __block_literal_global.5.6669
- __block_literal_global.53.4687
- __block_literal_global.5436
- __block_literal_global.5687
- __block_literal_global.58
- __block_literal_global.6
- __block_literal_global.6068
- __block_literal_global.610
- __block_literal_global.6174
- __block_literal_global.6311
- __block_literal_global.6369
- __block_literal_global.6553
- __block_literal_global.6628
- __block_literal_global.689
- __block_literal_global.6900
- __block_literal_global.6955
- __block_literal_global.7179
- __block_literal_global.7375
- __block_literal_global.7544
- __block_literal_global.7661
- __block_literal_global.7754
- __block_literal_global.8.1538
- __block_literal_global.8.2219
- __block_literal_global.833
- __block_literal_global.84
- __block_literal_global.9.6324
- __block_literal_global.90
- __block_literal_global.94
- __block_literal_global.982
- __dnssd_analytics_init_block_invoke.7
- __mdns_dns_service_get_provider_name_cstr
- __mdns_dns_service_manager_enumerate_all_service_array_pointers
- __mdns_dns_service_update_nw_config_data
- _dnssd_svcb_service_name_is_empty
- _dnssec_obj_rrset_get_time_received
- _mDNSInterface_BLE
- _mDNSInterface_P2P
- _mdns_dso_message_is_unidirectional
- _mdns_server_log.s_log.4328
- _mdns_server_log.s_once.4326
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$updateInvalidFromPresence
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _xpc_activity_register
- _xpc_activity_set_state
- _xpc_activity_should_defer
- g_nwi_state.4554
- g_session_list.4332
CStrings:
+ ", odoh config hash: 0x%08x"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dns_push/dns_push_discovery.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssd_server.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_mdns_core.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_denial_of_existence.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_domain_name.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_resource_record_member.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_dnskey.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_nsec3.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rrset.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_validation_manager.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/domain_name_labels.c"
+ "/Library/Caches/com.apple.xbs/98D5A3F1-A89D-4184-8CC1-625E766DF519/TemporaryDirectory.LfTf47/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/rdata_parser.c"
+ "B16@?0r^{mdns_dns_service_s={mdns_obj_s=^vii^{mdns_kind_s}}Q{_discovered_detail_s=QQ^{nw_endpoint}B[7c]}^{mdns_resolver_s}^{mdns_push_server_s}^{__CFArray}^{_domain_item_s}^{nw_resolver_config}^{nw_resolver_config}*^v^?^{__CFArray}^{mdns_dns_service_s}^{__CFArray}^{__CFArray}*^{mdns_querier_s}^{__CFArray}^{dispatch_source_s}^{nw_array}^{mdns_domain_name_s}^{dispatch_source_s}^{__CFArray}^{dispatch_queue_s}@?IIiIISSCCcBBBBBB[7c]}8"
+ "Failed to copy config dictionary: %@"
+ "Failed to create config snapshot from dictionary: %@"
+ "ODoH decryption failed with HTTP status %d, config hash: 0x%08x"
+ "ODoH query failed with HTTP status %u, config hash: 0x%08x"
+ "URLsForDirectory:inDomains:"
+ "background_task"
+ "background_task_repeating_daily_register - No Analytics for %{public}s"
+ "background_task_repeating_daily_register - No BGSystemTaskScheduler class"
+ "background_task_repeating_daily_register - register for task failed"
+ "background_task_repeating_daily_register - task already exists %{public}@"
+ "background_task_repeating_daily_register - task submit error %{public}@"
+ "close"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "defaultManager"
+ "dictionaryWithContentsOfURL:error:"
+ "dnssd_analytics_init_block_invoke_2"
+ "dnssd_analytics_update_dns_query_info cell %d qtype %s queries %u latency %u pos %d"
+ "fileURLWithPath:isDirectory:"
+ "hasBytesAvailable"
+ "initWithIdentifier:"
+ "inputStreamWithURL:"
+ "isFileURL"
+ "lastObject"
+ "mDNSResponder-2881.100.53"
+ "mutableCopyDeep"
+ "open"
+ "outputStreamWithURL:append:"
+ "presence:persistentDevicesChanged:"
+ "presence:presentDevicesChanged:"
+ "read:maxLength:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "reloadFromPresence:"
+ "setInterval:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "stringByAppendingPathComponent:"
+ "submitTaskRequest:error:"
+ "taskRequestForIdentifier:"
+ "unicast assist persistance cache failed to create input stream %{public}@"
+ "unicast assist persistance cache failed to create output stream %{public}@"
+ "unicast assist persistance cache read error bytes left at tag %d"
+ "unicast assist persistance cache read failed (next addr) ifhash %x ifid %2.2u"
+ "unicast assist persistance cache read failed (next interface)"
+ "unicast assist persistance cache read failed (next qhash) addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P ifhash %x ifid %2.2u"
+ "unicast assist persistance cache read failed (version val)"
+ "unicast assist persistance cache read from %{public}@"
+ "unicast assist persistance cache read zero bytes available"
+ "unicast assist persistance cache save failed (version tag)"
+ "unicast assist persistance cache save failed (version val)"
+ "unicast assist persistance cache save failed addr %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P ifhash %x ifid %2.2u"
+ "unicast assist persistance cache save failed ifhash %x ifid %2.2u"
+ "unicast assist persistance cache save failed qhash %x %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P ifhash %x ifid %2.2u"
+ "unicast assist persistance cache saved to %{public}@"
+ "unicast assist persistance cache wrong tag %d expected %d"
+ "unicast assist persistance cache wrong version %d expected %d"
+ "unicast assist persistance caches directory create %{public}@ error %{public}@"
+ "unicast assist persistance presence failed to create output stream %{public}@"
+ "unicast assist persistance presence failed to read cache %{public}@"
+ "unicast assist persistance presence failed to write cache %{public}@"
+ "unicast assist persistance presence reloaded from %{public}@"
+ "unicast assist persistance presence saved to %{public}@"
+ "unicast assist reloadFromPresence(%s): next (auth) count %lu from %@ time %@"
+ "unicast_assist_cache.bin"
+ "unicast_assist_presence.plist"
+ "v16@?0@\"BGSystemTask\"8"
+ "v32@0:8@\"SKPresence\"16@\"NSArray\"24"
+ "write:maxLength:"
+ "writePropertyList:toStream:format:options:error:"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dns_push/dns_push_discovery.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssd_server.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_mdns_core.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_denial_of_existence.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_domain_name.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_resource_record_member.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_dnskey.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_nsec3.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rrset.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_validation_manager.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/domain_name_labels.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/rdata_parser.c"
- "<INVALID STATE>"
- "B16@?0r^{mdns_dns_service_s={mdns_obj_s=^vii^{mdns_kind_s}}Q{_discovered_detail_s=QQ^{nw_endpoint}B[7c]}^{mdns_resolver_s}^{mdns_push_server_s}^{__CFArray}^{_domain_item_s}^{nw_resolver_config}*^v^?^{__CFArray}^{mdns_dns_service_s}^{__CFArray}^{__CFArray}^{mdns_xpc_string_s}**^{mdns_querier_s}^{__CFArray}^{dispatch_source_s}^{nw_array}^{mdns_domain_name_s}^{dispatch_source_s}^{__CFArray}^{dispatch_queue_s}@?IIiIISSCCcBBBBB[0c]}8"
- "Config is NULL"
- "[R%u] DNSServiceRegister STOP -- , duration: %{mdns:time_duration}u"
- "[R%u] DNSServiceRegister STOP -- SRV name: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P (%x), port: %u, flags: 0x%X, interface index: %d, client pid: %d (%{public}s), , duration: %{mdns:time_duration}u"
- "com.apple.mDNSResponder.analytics.daily: Analytics XPC_ACTIVITY_STATE_DONE failed"
- "com.apple.mDNSResponder.analytics.daily: Asked to defer"
- "com.apple.mDNSResponder.analytics.daily: Asked to defer but failed to set state"
- "dnssd_analytics_update_dns_query_info cell %d qtype %d queries %u latency %u pos %d"
- "mDNSMacOSXCreateEtcHostsEntry: ERROR!! name NULL"
- "mDNSResponder-2881.80.4.0.1"
- "uDNS_ReceiveMsg: TCP DNS response had TC bit set: ignoring"
- "unicast assist updateInvalidFromPresence: next (auth) count %lu from %@ time %@"
- "updateInvalidFromPresence"
- "v16@?0^{_xpc_activity_s=}8"

```
