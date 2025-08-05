## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2881.0.15.0.0
-  __TEXT.__text: 0x105c90
+2881.0.25.0.0
+  __TEXT.__text: 0x10631c
   __TEXT.__auth_stubs: 0x2f00
-  __TEXT.__objc_stubs: 0x1ba0
-  __TEXT.__objc_methlist: 0x63c
+  __TEXT.__objc_stubs: 0x1d00
+  __TEXT.__objc_methlist: 0x664
   __TEXT.__const: 0x1168
-  __TEXT.__cstring: 0x17599
+  __TEXT.__cstring: 0x175c7
   __TEXT.__gcc_except_tab: 0x334
-  __TEXT.__oslogstring: 0x1ec77
+  __TEXT.__oslogstring: 0x1ecde
   __TEXT.__objc_classname: 0x649
-  __TEXT.__objc_methname: 0x1a25
+  __TEXT.__objc_methname: 0x1b39
   __TEXT.__objc_methtype: 0x62a
-  __TEXT.__unwind_info: 0x1648
+  __TEXT.__unwind_info: 0x1650
   __TEXT.__eh_frame: 0x74
   __DATA_CONST.__auth_got: 0x1790
-  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__auth_ptr: 0x78
   __DATA_CONST.__const: 0x6478
   __DATA_CONST.__cfstring: 0x1160

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x4108
-  __DATA.__objc_selrefs: 0x890
-  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_const: 0x4138
+  __DATA.__objc_selrefs: 0x8f0
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x1270
   __DATA.__data: 0x4328
   __DATA.__bss: 0x16de0

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 09F922ED-4855-3A24-9CAA-46D6847D9127
-  Functions: 1833
-  Symbols:   4559
-  CStrings:  4835
+  UUID: 92428C17-65A6-3B14-B490-50DEBE2AD272
+  Functions: 1836
+  Symbols:   4575
+  CStrings:  4852
 
Symbols:
+ -[UAPresenceManager localNetworkHashes]
+ -[UAPresenceManager newSharableAddresses:]
+ -[UAPresenceManager setLocalNetworkHashes:]
+ FreeARElemCallback.2637
+ GCC_except_table1219
+ GCC_except_table1225
+ GCC_except_table1389
+ GCC_except_table1584
+ GCC_except_table1807
+ OBJC_IVAR_$_UAPresenceManager._localNetworkHashes
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ __36-[UAPresenceManager assertPresence:]_block_invoke.92
+ __44-[UAPresenceManager updateCacheFromPresence]_block_invoke.116
+ __44-[UAPresenceManager updateCacheFromPresence]_block_invoke_2.117
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6323
+ ___mdns_server_log_block_invoke.4350
+ ___unicast_assist_hash_for_interface_block_invoke.319
+ __block_descriptor_tmp.1.6291
+ __block_descriptor_tmp.10.4333
+ __block_descriptor_tmp.10.6113
+ __block_descriptor_tmp.11.6317
+ __block_descriptor_tmp.11.6681
+ __block_descriptor_tmp.115.4837
+ __block_descriptor_tmp.119.4818
+ __block_descriptor_tmp.12.6120
+ __block_descriptor_tmp.12.6678
+ __block_descriptor_tmp.120.4820
+ __block_descriptor_tmp.121.4812
+ __block_descriptor_tmp.122.4836
+ __block_descriptor_tmp.13.4349
+ __block_descriptor_tmp.13.4712
+ __block_descriptor_tmp.13.6121
+ __block_descriptor_tmp.130.4766
+ __block_descriptor_tmp.140.4790
+ __block_descriptor_tmp.15.6075
+ __block_descriptor_tmp.16.6328
+ __block_descriptor_tmp.17.4133
+ __block_descriptor_tmp.17.4716
+ __block_descriptor_tmp.17.6076
+ __block_descriptor_tmp.17.6672
+ __block_descriptor_tmp.18.4273
+ __block_descriptor_tmp.18.4321
+ __block_descriptor_tmp.18.6082
+ __block_descriptor_tmp.18.6685
+ __block_descriptor_tmp.19.6070
+ __block_descriptor_tmp.2.4207
+ __block_descriptor_tmp.2.6995
+ __block_descriptor_tmp.20.6115
+ __block_descriptor_tmp.20.6966
+ __block_descriptor_tmp.21.4276
+ __block_descriptor_tmp.21.4709
+ __block_descriptor_tmp.21.6981
+ __block_descriptor_tmp.22.4336
+ __block_descriptor_tmp.22.6116
+ __block_descriptor_tmp.23.6967
+ __block_descriptor_tmp.233.5761
+ __block_descriptor_tmp.24.6111
+ __block_descriptor_tmp.25.6968
+ __block_descriptor_tmp.251.5841
+ __block_descriptor_tmp.26.4706
+ __block_descriptor_tmp.26.6108
+ __block_descriptor_tmp.2650
+ __block_descriptor_tmp.27.6105
+ __block_descriptor_tmp.27.6973
+ __block_descriptor_tmp.28.6103
+ __block_descriptor_tmp.28.6974
+ __block_descriptor_tmp.29.6066
+ __block_descriptor_tmp.29.6975
+ __block_descriptor_tmp.3.4210
+ __block_descriptor_tmp.3.6129
+ __block_descriptor_tmp.3.6294
+ __block_descriptor_tmp.3.6321
+ __block_descriptor_tmp.3.6674
+ __block_descriptor_tmp.3.7550
+ __block_descriptor_tmp.30.6094
+ __block_descriptor_tmp.30.6959
+ __block_descriptor_tmp.32.4337
+ __block_descriptor_tmp.32.6096
+ __block_descriptor_tmp.33.6965
+ __block_descriptor_tmp.34.6953
+ __block_descriptor_tmp.35.6982
+ __block_descriptor_tmp.36.4721
+ __block_descriptor_tmp.38.4718
+ __block_descriptor_tmp.39.6045
+ __block_descriptor_tmp.4.4211
+ __block_descriptor_tmp.4.4323
+ __block_descriptor_tmp.4.4920
+ __block_descriptor_tmp.4.6130
+ __block_descriptor_tmp.4.6298
+ __block_descriptor_tmp.4.7381
+ __block_descriptor_tmp.40.4701
+ __block_descriptor_tmp.4135
+ __block_descriptor_tmp.4171
+ __block_descriptor_tmp.4202
+ __block_descriptor_tmp.43.4685
+ __block_descriptor_tmp.4318
+ __block_descriptor_tmp.45.4680
+ __block_descriptor_tmp.47.5449
+ __block_descriptor_tmp.4761
+ __block_descriptor_tmp.48.4921
+ __block_descriptor_tmp.5.4212
+ __block_descriptor_tmp.5.4324
+ __block_descriptor_tmp.5.4926
+ __block_descriptor_tmp.5.6131
+ __block_descriptor_tmp.50.4788
+ __block_descriptor_tmp.51.4696
+ __block_descriptor_tmp.5198
+ __block_descriptor_tmp.5437
+ __block_descriptor_tmp.5866
+ __block_descriptor_tmp.6.4184
+ __block_descriptor_tmp.6.4325
+ __block_descriptor_tmp.6.6302
+ __block_descriptor_tmp.60.7450
+ __block_descriptor_tmp.62.6090
+ __block_descriptor_tmp.6287
+ __block_descriptor_tmp.63.4667
+ __block_descriptor_tmp.6313
+ __block_descriptor_tmp.6373
+ __block_descriptor_tmp.64.7443
+ __block_descriptor_tmp.6560
+ __block_descriptor_tmp.6666
+ __block_descriptor_tmp.69.4799
+ __block_descriptor_tmp.6902
+ __block_descriptor_tmp.6996
+ __block_descriptor_tmp.7.4169
+ __block_descriptor_tmp.7.4328
+ __block_descriptor_tmp.7.6133
+ __block_descriptor_tmp.7.6305
+ __block_descriptor_tmp.7.6326
+ __block_descriptor_tmp.7.6931
+ __block_descriptor_tmp.70.4795
+ __block_descriptor_tmp.7030
+ __block_descriptor_tmp.7182
+ __block_descriptor_tmp.7377
+ __block_descriptor_tmp.7546
+ __block_descriptor_tmp.76.4898
+ __block_descriptor_tmp.7756
+ __block_descriptor_tmp.8.4167
+ __block_descriptor_tmp.8.6667
+ __block_descriptor_tmp.8.7391
+ __block_descriptor_tmp.80.4896
+ __block_descriptor_tmp.80.7394
+ __block_descriptor_tmp.9.4174
+ __block_descriptor_tmp.9.4704
+ __block_descriptor_tmp.91.4870
+ __block_descriptor_tmp.93.4868
+ __block_literal_global.10.7387
+ __block_literal_global.11.4702
+ __block_literal_global.115
+ __block_literal_global.15.4330
+ __block_literal_global.15.4708
+ __block_literal_global.15.7670
+ __block_literal_global.19.4714
+ __block_literal_global.20.4317
+ __block_literal_global.253.5770
+ __block_literal_global.267
+ __block_literal_global.270
+ __block_literal_global.28.6181
+ __block_literal_global.299
+ __block_literal_global.312
+ __block_literal_global.316
+ __block_literal_global.318
+ __block_literal_global.322
+ __block_literal_global.43.6614
+ __block_literal_global.4326
+ __block_literal_global.4576
+ __block_literal_global.4924
+ __block_literal_global.5.6316
+ __block_literal_global.5.6669
+ __block_literal_global.53.4688
+ __block_literal_global.5436
+ __block_literal_global.5687
+ __block_literal_global.6068
+ __block_literal_global.6174
+ __block_literal_global.6311
+ __block_literal_global.6369
+ __block_literal_global.6553
+ __block_literal_global.6628
+ __block_literal_global.6900
+ __block_literal_global.6955
+ __block_literal_global.7179
+ __block_literal_global.7375
+ __block_literal_global.7544
+ __block_literal_global.7661
+ __block_literal_global.7754
+ __block_literal_global.9.6324
+ __block_literal_global.94
+ _mdns_server_log.s_log.4331
+ _mdns_server_log.s_once.4329
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allObjects
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$localNetworkHashes
+ _objc_msgSend$minusSet:
+ _objc_msgSend$newSharableAddresses:
+ _objc_msgSend$orderedSet
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$setWithArray:
+ g_nwi_state.4557
+ g_session_list.4335
- FreeARElemCallback.2638
- GCC_except_table1217
- GCC_except_table1223
- GCC_except_table1386
- GCC_except_table1581
- GCC_except_table1804
- __36-[UAPresenceManager assertPresence:]_block_invoke.89
- __44-[UAPresenceManager updateCacheFromPresence]_block_invoke.113
- __44-[UAPresenceManager updateCacheFromPresence]_block_invoke_2.114
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6325
- ___mdns_server_log_block_invoke.4348
- ___unicast_assist_hash_for_interface_block_invoke.310
- __block_descriptor_tmp.1.6293
- __block_descriptor_tmp.10.4331
- __block_descriptor_tmp.10.6115
- __block_descriptor_tmp.11.6319
- __block_descriptor_tmp.11.6683
- __block_descriptor_tmp.115.4841
- __block_descriptor_tmp.119.4822
- __block_descriptor_tmp.12.6122
- __block_descriptor_tmp.12.6680
- __block_descriptor_tmp.120.4824
- __block_descriptor_tmp.121.4816
- __block_descriptor_tmp.122.4840
- __block_descriptor_tmp.13.4347
- __block_descriptor_tmp.13.4716
- __block_descriptor_tmp.13.6123
- __block_descriptor_tmp.130.4770
- __block_descriptor_tmp.140.4794
- __block_descriptor_tmp.15.6077
- __block_descriptor_tmp.16.6330
- __block_descriptor_tmp.17.4131
- __block_descriptor_tmp.17.4720
- __block_descriptor_tmp.17.6078
- __block_descriptor_tmp.17.6674
- __block_descriptor_tmp.18.4271
- __block_descriptor_tmp.18.4319
- __block_descriptor_tmp.18.6084
- __block_descriptor_tmp.18.6687
- __block_descriptor_tmp.19.6072
- __block_descriptor_tmp.2.4205
- __block_descriptor_tmp.2.6996
- __block_descriptor_tmp.20.6117
- __block_descriptor_tmp.20.6967
- __block_descriptor_tmp.21.4274
- __block_descriptor_tmp.21.4713
- __block_descriptor_tmp.21.6982
- __block_descriptor_tmp.22.4334
- __block_descriptor_tmp.22.6118
- __block_descriptor_tmp.23.6968
- __block_descriptor_tmp.233.5763
- __block_descriptor_tmp.24.6113
- __block_descriptor_tmp.25.6969
- __block_descriptor_tmp.251.5843
- __block_descriptor_tmp.26.4710
- __block_descriptor_tmp.26.6110
- __block_descriptor_tmp.2651
- __block_descriptor_tmp.27.6107
- __block_descriptor_tmp.27.6974
- __block_descriptor_tmp.28.6105
- __block_descriptor_tmp.28.6975
- __block_descriptor_tmp.29.6068
- __block_descriptor_tmp.29.6976
- __block_descriptor_tmp.3.4208
- __block_descriptor_tmp.3.6131
- __block_descriptor_tmp.3.6296
- __block_descriptor_tmp.3.6323
- __block_descriptor_tmp.3.6676
- __block_descriptor_tmp.3.7549
- __block_descriptor_tmp.30.6096
- __block_descriptor_tmp.30.6960
- __block_descriptor_tmp.32.4335
- __block_descriptor_tmp.32.6098
- __block_descriptor_tmp.33.6966
- __block_descriptor_tmp.34.6954
- __block_descriptor_tmp.35.6983
- __block_descriptor_tmp.36.4725
- __block_descriptor_tmp.38.4722
- __block_descriptor_tmp.39.6047
- __block_descriptor_tmp.4.4209
- __block_descriptor_tmp.4.4321
- __block_descriptor_tmp.4.4924
- __block_descriptor_tmp.4.6132
- __block_descriptor_tmp.4.6300
- __block_descriptor_tmp.4.7382
- __block_descriptor_tmp.40.4705
- __block_descriptor_tmp.4133
- __block_descriptor_tmp.4169
- __block_descriptor_tmp.4200
- __block_descriptor_tmp.43.4689
- __block_descriptor_tmp.4316
- __block_descriptor_tmp.45.4684
- __block_descriptor_tmp.47.5451
- __block_descriptor_tmp.4765
- __block_descriptor_tmp.48.4925
- __block_descriptor_tmp.5.4210
- __block_descriptor_tmp.5.4322
- __block_descriptor_tmp.5.4930
- __block_descriptor_tmp.5.6133
- __block_descriptor_tmp.50.4792
- __block_descriptor_tmp.51.4700
- __block_descriptor_tmp.5202
- __block_descriptor_tmp.5439
- __block_descriptor_tmp.5868
- __block_descriptor_tmp.6.4182
- __block_descriptor_tmp.6.4323
- __block_descriptor_tmp.6.6304
- __block_descriptor_tmp.60.7449
- __block_descriptor_tmp.62.6092
- __block_descriptor_tmp.6289
- __block_descriptor_tmp.63.4671
- __block_descriptor_tmp.6315
- __block_descriptor_tmp.6375
- __block_descriptor_tmp.64.7442
- __block_descriptor_tmp.6562
- __block_descriptor_tmp.6668
- __block_descriptor_tmp.69.4803
- __block_descriptor_tmp.6903
- __block_descriptor_tmp.6997
- __block_descriptor_tmp.7.4167
- __block_descriptor_tmp.7.4326
- __block_descriptor_tmp.7.6135
- __block_descriptor_tmp.7.6307
- __block_descriptor_tmp.7.6328
- __block_descriptor_tmp.7.6932
- __block_descriptor_tmp.70.4799
- __block_descriptor_tmp.7031
- __block_descriptor_tmp.7183
- __block_descriptor_tmp.7378
- __block_descriptor_tmp.7545
- __block_descriptor_tmp.76.4902
- __block_descriptor_tmp.7755
- __block_descriptor_tmp.8.4165
- __block_descriptor_tmp.8.6669
- __block_descriptor_tmp.8.7392
- __block_descriptor_tmp.80.4900
- __block_descriptor_tmp.80.7395
- __block_descriptor_tmp.9.4172
- __block_descriptor_tmp.9.4708
- __block_descriptor_tmp.91.4874
- __block_descriptor_tmp.93.4872
- __block_literal_global.10.7388
- __block_literal_global.11.4706
- __block_literal_global.112
- __block_literal_global.15.4328
- __block_literal_global.15.4712
- __block_literal_global.15.7669
- __block_literal_global.19.4718
- __block_literal_global.20.4315
- __block_literal_global.253.5772
- __block_literal_global.258
- __block_literal_global.261
- __block_literal_global.28.6183
- __block_literal_global.290
- __block_literal_global.303
- __block_literal_global.307.4554
- __block_literal_global.309
- __block_literal_global.313.4633
- __block_literal_global.43.6616
- __block_literal_global.4324
- __block_literal_global.4574
- __block_literal_global.4928
- __block_literal_global.5.6318
- __block_literal_global.5.6671
- __block_literal_global.53.4692
- __block_literal_global.5438
- __block_literal_global.5689
- __block_literal_global.6070
- __block_literal_global.6176
- __block_literal_global.6313
- __block_literal_global.6371
- __block_literal_global.6555
- __block_literal_global.6630
- __block_literal_global.6901
- __block_literal_global.6956
- __block_literal_global.7180
- __block_literal_global.7376
- __block_literal_global.7543
- __block_literal_global.7660
- __block_literal_global.7753
- __block_literal_global.9.6326
- __block_literal_global.91
- _mdns_server_log.s_log.4329
- _mdns_server_log.s_once.4327
- g_nwi_state.4556
- g_session_list.4333
Functions:
~ _PacketRRConflict : 688 -> 1124
~ -[UAPresenceManager .cxx_destruct] : 104 -> 116
+ -[UAPresenceManager setAuthRecords:]
+ -[UAPresenceManager presenceReady]
~ ___44-[UAPresenceManager updateCacheFromPresence]_block_invoke : 1048 -> 1060
~ -[UAPresenceManager handleNetworkUpdate:] : 776 -> 756
+ -[UAPresenceManager newSharableAddresses:]
~ -[UAPresenceManager init] : 544 -> 568
~ ____post_unicast_assist_presence_block_invoke : 400 -> 408
CStrings:
+ "6"
+ "Ignoring conflict on interface %d with recently deregistered hostname record: %{sensitive, mask.hash}s"
+ "T@\"NSMutableDictionary\",&,N,V_localNetworkHashes"
+ "_localNetworkHashes"
+ "addObjectsFromArray:"
+ "allObjects"
+ "intersectsSet:"
+ "localNetworkHashes"
+ "mDNSResponder-2881.0.25"
+ "minusSet:"
+ "newSharableAddresses:"
+ "orderedSet"
+ "removeAllObjects"
+ "removeObjectsForKeys:"
+ "removeObjectsInRange:"
+ "setLocalNetworkHashes:"
+ "setWithArray:"
+ "update_devices_invalid"
+ "update_devices_missing"
- "5"
- "mDNSResponder-2881.0.15"

```
