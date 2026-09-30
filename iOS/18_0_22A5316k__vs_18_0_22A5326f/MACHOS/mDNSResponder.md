## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2559.0.31.0.0
-  __TEXT.__text: 0xf2ac0
-  __TEXT.__auth_stubs: 0x2e00
+2559.0.51.0.0
+  __TEXT.__text: 0xfecc8
+  __TEXT.__auth_stubs: 0x2df0
   __TEXT.__objc_stubs: 0x15a0
   __TEXT.__objc_methlist: 0x21c
-  __TEXT.__const: 0x10d0
+  __TEXT.__const: 0x1110
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__cstring: 0x17ec1
-  __TEXT.__oslogstring: 0x17a40
+  __TEXT.__cstring: 0x16e3a
+  __TEXT.__oslogstring: 0x1cf9c
   __TEXT.__objc_classname: 0x63a
   __TEXT.__objc_methname: 0x13ed
   __TEXT.__objc_methtype: 0x5da
-  __TEXT.__unwind_info: 0x1630
-  __DATA_CONST.__auth_got: 0x1710
+  __TEXT.__unwind_info: 0x1650
+  __DATA_CONST.__auth_got: 0x1708
   __DATA_CONST.__got: 0x330
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x60b0
+  __DATA_CONST.__const: 0x6068
   __DATA_CONST.__cfstring: 0x1140
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x10

   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x11d0
   __DATA.__data: 0x42b8
-  __DATA.__bss: 0x16b20
+  __DATA.__bss: 0x16d20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1792
-  Symbols:   4315
-  CStrings:  4446
+  Functions: 1799
+  Symbols:   4325
+  CStrings:  4480
 
Symbols:
+ FreeARElemCallback.2609
+ GCC_except_table1070
+ GCC_except_table1151
+ GCC_except_table1157
+ GCC_except_table1301
+ GCC_except_table1502
+ _Querier_RegisterCustomPushDNSServiceWithConnectionErrorHandler
+ _ResourceRecordGetRDataBytesPointer
+ __Block_byref_object_copy_.894
+ __Block_byref_object_dispose_.895
+ ____mdns_dns_service_make_defunct_block_invoke
+ ____mdns_dso_client_session_handle_error_block_invoke
+ ____mrcs_session_handle_dns_service_registration_start_block_invoke
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6229
+ ___mdns_dns_service_manager_probe_discovered_service_block_invoke.233
+ ___mdns_dns_service_manager_probe_discovered_service_block_invoke_2.234
+ ___mdns_push_server_invalidate_block_invoke
+ ___mdns_server_log_block_invoke.4307
+ __block_descriptor_tmp.1.6196
+ __block_descriptor_tmp.10.4290
+ __block_descriptor_tmp.10.4640
+ __block_descriptor_tmp.10.6034
+ __block_descriptor_tmp.10.7261
+ __block_descriptor_tmp.11.6223
+ __block_descriptor_tmp.11.6560
+ __block_descriptor_tmp.11.835
+ __block_descriptor_tmp.115.4771
+ __block_descriptor_tmp.119.4754
+ __block_descriptor_tmp.12.6041
+ __block_descriptor_tmp.12.6557
+ __block_descriptor_tmp.12.836
+ __block_descriptor_tmp.120.4756
+ __block_descriptor_tmp.121.4748
+ __block_descriptor_tmp.122.4839
+ __block_descriptor_tmp.123.4770
+ __block_descriptor_tmp.13.4306
+ __block_descriptor_tmp.13.6042
+ __block_descriptor_tmp.13.841
+ __block_descriptor_tmp.131.4704
+ __block_descriptor_tmp.133
+ __block_descriptor_tmp.133.3627
+ __block_descriptor_tmp.137
+ __block_descriptor_tmp.14.1038
+ __block_descriptor_tmp.14.3255
+ __block_descriptor_tmp.14.4648
+ __block_descriptor_tmp.14.849
+ __block_descriptor_tmp.140
+ __block_descriptor_tmp.1429
+ __block_descriptor_tmp.143.4622
+ __block_descriptor_tmp.143.939
+ __block_descriptor_tmp.15.5997
+ __block_descriptor_tmp.1507
+ __block_descriptor_tmp.151
+ __block_descriptor_tmp.16.6221
+ __block_descriptor_tmp.163
+ __block_descriptor_tmp.17.1039
+ __block_descriptor_tmp.17.3260
+ __block_descriptor_tmp.17.4104
+ __block_descriptor_tmp.17.5998
+ __block_descriptor_tmp.17.6551
+ __block_descriptor_tmp.173
+ __block_descriptor_tmp.18.4278
+ __block_descriptor_tmp.18.4652
+ __block_descriptor_tmp.18.6004
+ __block_descriptor_tmp.18.6564
+ __block_descriptor_tmp.188
+ __block_descriptor_tmp.19.4227
+ __block_descriptor_tmp.19.5993
+ __block_descriptor_tmp.19.6834
+ __block_descriptor_tmp.19.878
+ __block_descriptor_tmp.2.4166
+ __block_descriptor_tmp.20.6036
+ __block_descriptor_tmp.20.968
+ __block_descriptor_tmp.206
+ __block_descriptor_tmp.21.3262
+ __block_descriptor_tmp.21.6835
+ __block_descriptor_tmp.215
+ __block_descriptor_tmp.219
+ __block_descriptor_tmp.22.1517
+ __block_descriptor_tmp.22.4230
+ __block_descriptor_tmp.22.4293
+ __block_descriptor_tmp.22.4645
+ __block_descriptor_tmp.22.6037
+ __block_descriptor_tmp.222
+ __block_descriptor_tmp.225
+ __block_descriptor_tmp.2279
+ __block_descriptor_tmp.228.5690
+ __block_descriptor_tmp.23.1524
+ __block_descriptor_tmp.23.3283
+ __block_descriptor_tmp.23.6836
+ __block_descriptor_tmp.232.5686
+ __block_descriptor_tmp.233
+ __block_descriptor_tmp.236.2980
+ __block_descriptor_tmp.238
+ __block_descriptor_tmp.238.2875
+ __block_descriptor_tmp.2380
+ __block_descriptor_tmp.24.1525
+ __block_descriptor_tmp.24.3305
+ __block_descriptor_tmp.24.6032
+ __block_descriptor_tmp.24.933
+ __block_descriptor_tmp.242.5764
+ __block_descriptor_tmp.246.2975
+ __block_descriptor_tmp.246.5762
+ __block_descriptor_tmp.249
+ __block_descriptor_tmp.25.1036
+ __block_descriptor_tmp.25.6841
+ __block_descriptor_tmp.250.5770
+ __block_descriptor_tmp.253
+ __block_descriptor_tmp.26.1526
+ __block_descriptor_tmp.26.6030
+ __block_descriptor_tmp.26.6842
+ __block_descriptor_tmp.260
+ __block_descriptor_tmp.2622
+ __block_descriptor_tmp.264
+ __block_descriptor_tmp.27.1527
+ __block_descriptor_tmp.27.4642
+ __block_descriptor_tmp.27.6027
+ __block_descriptor_tmp.27.6843
+ __block_descriptor_tmp.279
+ __block_descriptor_tmp.28.3310
+ __block_descriptor_tmp.28.6025
+ __block_descriptor_tmp.28.6831
+ __block_descriptor_tmp.283
+ __block_descriptor_tmp.29.1529
+ __block_descriptor_tmp.29.4294
+ __block_descriptor_tmp.29.5989
+ __block_descriptor_tmp.3.1511
+ __block_descriptor_tmp.3.2280
+ __block_descriptor_tmp.3.4145
+ __block_descriptor_tmp.3.6050
+ __block_descriptor_tmp.3.6199
+ __block_descriptor_tmp.3.6227
+ __block_descriptor_tmp.3.6553
+ __block_descriptor_tmp.3.7387
+ __block_descriptor_tmp.3.974
+ __block_descriptor_tmp.30.6016
+ __block_descriptor_tmp.305
+ __block_descriptor_tmp.309
+ __block_descriptor_tmp.31.4295
+ __block_descriptor_tmp.31.6828
+ __block_descriptor_tmp.315
+ __block_descriptor_tmp.3180
+ __block_descriptor_tmp.32.6018
+ __block_descriptor_tmp.32.6849
+ __block_descriptor_tmp.33.1531
+ __block_descriptor_tmp.33.3204
+ __block_descriptor_tmp.33.6015
+ __block_descriptor_tmp.34.1540
+ __block_descriptor_tmp.3479
+ __block_descriptor_tmp.35.1539
+ __block_descriptor_tmp.3558
+ __block_descriptor_tmp.37.3207
+ __block_descriptor_tmp.37.4657
+ __block_descriptor_tmp.370
+ __block_descriptor_tmp.38.1016
+ __block_descriptor_tmp.39.1026
+ __block_descriptor_tmp.39.4654
+ __block_descriptor_tmp.391
+ __block_descriptor_tmp.4.4280
+ __block_descriptor_tmp.4.4855
+ __block_descriptor_tmp.4.6051
+ __block_descriptor_tmp.4.6203
+ __block_descriptor_tmp.40.1533
+ __block_descriptor_tmp.40.5968
+ __block_descriptor_tmp.41.1021
+ __block_descriptor_tmp.41.1534
+ __block_descriptor_tmp.41.3201
+ __block_descriptor_tmp.41.4637
+ __block_descriptor_tmp.4106
+ __block_descriptor_tmp.4136
+ __block_descriptor_tmp.414
+ __block_descriptor_tmp.4163
+ __block_descriptor_tmp.4275
+ __block_descriptor_tmp.44.4619
+ __block_descriptor_tmp.46.3187
+ __block_descriptor_tmp.46.4613
+ __block_descriptor_tmp.46.7303
+ __block_descriptor_tmp.4697
+ __block_descriptor_tmp.47.5384
+ __block_descriptor_tmp.48.3267
+ __block_descriptor_tmp.484
+ __block_descriptor_tmp.49.4856
+ __block_descriptor_tmp.491
+ __block_descriptor_tmp.495
+ __block_descriptor_tmp.498
+ __block_descriptor_tmp.5.2291
+ __block_descriptor_tmp.5.4281
+ __block_descriptor_tmp.5.4861
+ __block_descriptor_tmp.5.6052
+ __block_descriptor_tmp.50.4727
+ __block_descriptor_tmp.50.7296
+ __block_descriptor_tmp.500
+ __block_descriptor_tmp.504
+ __block_descriptor_tmp.508
+ __block_descriptor_tmp.51.1025
+ __block_descriptor_tmp.51.4726
+ __block_descriptor_tmp.5144
+ __block_descriptor_tmp.518
+ __block_descriptor_tmp.52.4632
+ __block_descriptor_tmp.5372
+ __block_descriptor_tmp.55.1023
+ __block_descriptor_tmp.57.3311
+ __block_descriptor_tmp.5789
+ __block_descriptor_tmp.58.1019
+ __block_descriptor_tmp.58.3313
+ __block_descriptor_tmp.598
+ __block_descriptor_tmp.6.1545
+ __block_descriptor_tmp.6.4282
+ __block_descriptor_tmp.6.6207
+ __block_descriptor_tmp.6.6802
+ __block_descriptor_tmp.6.7251
+ __block_descriptor_tmp.6.971
+ __block_descriptor_tmp.60.1012
+ __block_descriptor_tmp.60.3323
+ __block_descriptor_tmp.6192
+ __block_descriptor_tmp.6217
+ __block_descriptor_tmp.6277
+ __block_descriptor_tmp.63.6011
+ __block_descriptor_tmp.63.982
+ __block_descriptor_tmp.64.4600
+ __block_descriptor_tmp.6545
+ __block_descriptor_tmp.66.7264
+ __block_descriptor_tmp.675
+ __block_descriptor_tmp.6775
+ __block_descriptor_tmp.68.7274
+ __block_descriptor_tmp.6862
+ __block_descriptor_tmp.6896
+ __block_descriptor_tmp.69.4700
+ __block_descriptor_tmp.69.987
+ __block_descriptor_tmp.7.4134
+ __block_descriptor_tmp.7.4285
+ __block_descriptor_tmp.7.4885
+ __block_descriptor_tmp.7.6054
+ __block_descriptor_tmp.7.6210
+ __block_descriptor_tmp.7.6232
+ __block_descriptor_tmp.7.822
+ __block_descriptor_tmp.70.4735
+ __block_descriptor_tmp.7048
+ __block_descriptor_tmp.72
+ __block_descriptor_tmp.7245
+ __block_descriptor_tmp.7383
+ __block_descriptor_tmp.76.4832
+ __block_descriptor_tmp.7623
+ __block_descriptor_tmp.8.4132
+ __block_descriptor_tmp.8.6546
+ __block_descriptor_tmp.8.830
+ __block_descriptor_tmp.80.4830
+ __block_descriptor_tmp.817
+ __block_descriptor_tmp.9.4139
+ __block_descriptor_tmp.91.4804
+ __block_descriptor_tmp.93.4802
+ __block_descriptor_tmp.964
+ __block_literal_global.12.4638
+ __block_literal_global.12.6093
+ __block_literal_global.12.7257
+ __block_literal_global.123
+ __block_literal_global.135
+ __block_literal_global.139
+ __block_literal_global.1416
+ __block_literal_global.142
+ __block_literal_global.145.4618
+ __block_literal_global.15.4287
+ __block_literal_global.15.7503
+ __block_literal_global.1502
+ __block_literal_global.16.4644
+ __block_literal_global.160.4492
+ __block_literal_global.20.4274
+ __block_literal_global.20.4650
+ __block_literal_global.2207
+ __block_literal_global.2278
+ __block_literal_global.2374
+ __block_literal_global.240
+ __block_literal_global.248.5702
+ __block_literal_global.251
+ __block_literal_global.255
+ __block_literal_global.262
+ __block_literal_global.281
+ __block_literal_global.2979
+ __block_literal_global.3.6081
+ __block_literal_global.307
+ __block_literal_global.313
+ __block_literal_global.3303
+ __block_literal_global.34
+ __block_literal_global.3477
+ __block_literal_global.35.3176
+ __block_literal_global.3591
+ __block_literal_global.368
+ __block_literal_global.39.3205
+ __block_literal_global.393
+ __block_literal_global.404
+ __block_literal_global.4283
+ __block_literal_global.43.3177
+ __block_literal_global.43.4514
+ __block_literal_global.43.6492
+ __block_literal_global.4513
+ __block_literal_global.4859
+ __block_literal_global.486
+ __block_literal_global.493
+ __block_literal_global.497
+ __block_literal_global.5.6219
+ __block_literal_global.5.6548
+ __block_literal_global.502
+ __block_literal_global.506
+ __block_literal_global.5371
+ __block_literal_global.54.4624
+ __block_literal_global.5616
+ __block_literal_global.593
+ __block_literal_global.5991
+ __block_literal_global.6079
+ __block_literal_global.6273
+ __block_literal_global.6506
+ __block_literal_global.671
+ __block_literal_global.6773
+ __block_literal_global.68
+ __block_literal_global.6824
+ __block_literal_global.7045
+ __block_literal_global.7243
+ __block_literal_global.7381
+ __block_literal_global.7494
+ __block_literal_global.7621
+ __block_literal_global.8.1516
+ __block_literal_global.8.2201
+ __block_literal_global.8.7249
+ __block_literal_global.815
+ __block_literal_global.9.6230
+ __block_literal_global.962
+ __mdns_dso_client_session_handle_error
+ _conflictWithCacheRecordsOrFlush
+ _mDNS_DomainNameFNV1aHash
+ _mdns_push_server_invalidate
+ _mdns_server_log.s_log.4288
+ _mdns_server_log.s_once.4286
+ _requestShouldLogFullRequestInfo
+ g_nwi_state.4494
+ g_session_list.4292
+ mDNSCoreReceiveUpdate.msgs.262
- FreeARElemCallback.2590
- GCC_except_table1067
- GCC_except_table1147
- GCC_except_table1153
- GCC_except_table1297
- GCC_except_table1497
- _FatalError
- _Querier_RegisterCustomPushDNSService
- __Block_byref_object_copy_.898
- __Block_byref_object_dispose_.899
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6171
- ___mdns_dns_service_manager_probe_discovered_service_block_invoke.231
- ___mdns_dns_service_manager_probe_discovered_service_block_invoke_2.232
- ___mdns_server_log_block_invoke.4249
- __block_descriptor_tmp.1.6138
- __block_descriptor_tmp.10.4234
- __block_descriptor_tmp.10.4579
- __block_descriptor_tmp.10.5976
- __block_descriptor_tmp.10.7202
- __block_descriptor_tmp.11.6165
- __block_descriptor_tmp.11.6502
- __block_descriptor_tmp.11.839
- __block_descriptor_tmp.115.4710
- __block_descriptor_tmp.119.4693
- __block_descriptor_tmp.12.5983
- __block_descriptor_tmp.12.6499
- __block_descriptor_tmp.12.840
- __block_descriptor_tmp.120.4695
- __block_descriptor_tmp.121.4687
- __block_descriptor_tmp.122.4778
- __block_descriptor_tmp.123.4709
- __block_descriptor_tmp.13.4248
- __block_descriptor_tmp.13.5984
- __block_descriptor_tmp.13.845
- __block_descriptor_tmp.138
- __block_descriptor_tmp.139
- __block_descriptor_tmp.14.1040
- __block_descriptor_tmp.14.3204
- __block_descriptor_tmp.14.4587
- __block_descriptor_tmp.14.853
- __block_descriptor_tmp.142.4780
- __block_descriptor_tmp.1428
- __block_descriptor_tmp.143.4561
- __block_descriptor_tmp.144
- __block_descriptor_tmp.145
- __block_descriptor_tmp.147.3546
- __block_descriptor_tmp.15.5941
- __block_descriptor_tmp.1506
- __block_descriptor_tmp.16.6163
- __block_descriptor_tmp.169
- __block_descriptor_tmp.17.1041
- __block_descriptor_tmp.17.3209
- __block_descriptor_tmp.17.4048
- __block_descriptor_tmp.17.5942
- __block_descriptor_tmp.17.6493
- __block_descriptor_tmp.172
- __block_descriptor_tmp.18.4222
- __block_descriptor_tmp.18.4591
- __block_descriptor_tmp.18.5947
- __block_descriptor_tmp.18.6506
- __block_descriptor_tmp.18.6791
- __block_descriptor_tmp.189
- __block_descriptor_tmp.19.4171
- __block_descriptor_tmp.19.5935
- __block_descriptor_tmp.19.882
- __block_descriptor_tmp.2.4110
- __block_descriptor_tmp.20.5978
- __block_descriptor_tmp.20.6774
- __block_descriptor_tmp.20.970
- __block_descriptor_tmp.204
- __block_descriptor_tmp.21.3211
- __block_descriptor_tmp.213.5728
- __block_descriptor_tmp.217
- __block_descriptor_tmp.22.1516
- __block_descriptor_tmp.22.4174
- __block_descriptor_tmp.22.4237
- __block_descriptor_tmp.22.4584
- __block_descriptor_tmp.22.5979
- __block_descriptor_tmp.22.6776
- __block_descriptor_tmp.220
- __block_descriptor_tmp.221
- __block_descriptor_tmp.224.5634
- __block_descriptor_tmp.2272
- __block_descriptor_tmp.228.5632
- __block_descriptor_tmp.23.1523
- __block_descriptor_tmp.23.3232
- __block_descriptor_tmp.234
- __block_descriptor_tmp.234.2960
- __block_descriptor_tmp.237
- __block_descriptor_tmp.2373
- __block_descriptor_tmp.239
- __block_descriptor_tmp.24.1524
- __block_descriptor_tmp.24.3254
- __block_descriptor_tmp.24.5974
- __block_descriptor_tmp.24.6777
- __block_descriptor_tmp.24.937
- __block_descriptor_tmp.240
- __block_descriptor_tmp.242.5706
- __block_descriptor_tmp.243
- __block_descriptor_tmp.246.5704
- __block_descriptor_tmp.25.1038
- __block_descriptor_tmp.251
- __block_descriptor_tmp.252
- __block_descriptor_tmp.26.1525
- __block_descriptor_tmp.26.5972
- __block_descriptor_tmp.26.6782
- __block_descriptor_tmp.2603
- __block_descriptor_tmp.262
- __block_descriptor_tmp.266
- __block_descriptor_tmp.27.1526
- __block_descriptor_tmp.27.4581
- __block_descriptor_tmp.27.5969
- __block_descriptor_tmp.27.6783
- __block_descriptor_tmp.28.3259
- __block_descriptor_tmp.28.5967
- __block_descriptor_tmp.28.6784
- __block_descriptor_tmp.281
- __block_descriptor_tmp.285
- __block_descriptor_tmp.29.1528
- __block_descriptor_tmp.29.4238
- __block_descriptor_tmp.29.5930
- __block_descriptor_tmp.29.6771
- __block_descriptor_tmp.3.1510
- __block_descriptor_tmp.3.2273
- __block_descriptor_tmp.3.4089
- __block_descriptor_tmp.3.5992
- __block_descriptor_tmp.3.6141
- __block_descriptor_tmp.3.6169
- __block_descriptor_tmp.3.6495
- __block_descriptor_tmp.3.7327
- __block_descriptor_tmp.3.976
- __block_descriptor_tmp.30.5958
- __block_descriptor_tmp.307
- __block_descriptor_tmp.3129
- __block_descriptor_tmp.313
- __block_descriptor_tmp.317
- __block_descriptor_tmp.32.5960
- __block_descriptor_tmp.33.1530
- __block_descriptor_tmp.33.3153
- __block_descriptor_tmp.34.1539
- __block_descriptor_tmp.34.6768
- __block_descriptor_tmp.3428
- __block_descriptor_tmp.35.1538
- __block_descriptor_tmp.3507
- __block_descriptor_tmp.37.3156
- __block_descriptor_tmp.37.4596
- __block_descriptor_tmp.375
- __block_descriptor_tmp.38.1018
- __block_descriptor_tmp.39.1028
- __block_descriptor_tmp.39.4593
- __block_descriptor_tmp.39.5910
- __block_descriptor_tmp.393
- __block_descriptor_tmp.4.4224
- __block_descriptor_tmp.4.4795
- __block_descriptor_tmp.4.5993
- __block_descriptor_tmp.4.6145
- __block_descriptor_tmp.40.1532
- __block_descriptor_tmp.4050
- __block_descriptor_tmp.4080
- __block_descriptor_tmp.41.1023
- __block_descriptor_tmp.41.1533
- __block_descriptor_tmp.41.3150
- __block_descriptor_tmp.41.4576
- __block_descriptor_tmp.4107
- __block_descriptor_tmp.4219
- __block_descriptor_tmp.44.4559
- __block_descriptor_tmp.443
- __block_descriptor_tmp.46.3136
- __block_descriptor_tmp.46.4554
- __block_descriptor_tmp.46.7243
- __block_descriptor_tmp.4636
- __block_descriptor_tmp.47.5327
- __block_descriptor_tmp.48.3216
- __block_descriptor_tmp.49.4796
- __block_descriptor_tmp.5.2284
- __block_descriptor_tmp.5.4225
- __block_descriptor_tmp.5.4801
- __block_descriptor_tmp.5.5994
- __block_descriptor_tmp.50.4665
- __block_descriptor_tmp.50.7236
- __block_descriptor_tmp.5084
- __block_descriptor_tmp.51.1027
- __block_descriptor_tmp.51.4664
- __block_descriptor_tmp.52.4571
- __block_descriptor_tmp.526
- __block_descriptor_tmp.5315
- __block_descriptor_tmp.55.1025
- __block_descriptor_tmp.553
- __block_descriptor_tmp.560
- __block_descriptor_tmp.564
- __block_descriptor_tmp.567
- __block_descriptor_tmp.569
- __block_descriptor_tmp.57.3260
- __block_descriptor_tmp.573
- __block_descriptor_tmp.5731
- __block_descriptor_tmp.577
- __block_descriptor_tmp.58.1021
- __block_descriptor_tmp.58.3262
- __block_descriptor_tmp.6.1544
- __block_descriptor_tmp.6.4226
- __block_descriptor_tmp.6.6149
- __block_descriptor_tmp.6.7192
- __block_descriptor_tmp.6.973
- __block_descriptor_tmp.60.1014
- __block_descriptor_tmp.60.3272
- __block_descriptor_tmp.602
- __block_descriptor_tmp.61.5955
- __block_descriptor_tmp.6134
- __block_descriptor_tmp.6159
- __block_descriptor_tmp.6219
- __block_descriptor_tmp.63.984
- __block_descriptor_tmp.64.4541
- __block_descriptor_tmp.64.5939
- __block_descriptor_tmp.6487
- __block_descriptor_tmp.6717
- __block_descriptor_tmp.6744
- __block_descriptor_tmp.679
- __block_descriptor_tmp.68.7214
- __block_descriptor_tmp.6837
- __block_descriptor_tmp.69.4639
- __block_descriptor_tmp.69.989
- __block_descriptor_tmp.6989
- __block_descriptor_tmp.7.4078
- __block_descriptor_tmp.7.4229
- __block_descriptor_tmp.7.4825
- __block_descriptor_tmp.7.5996
- __block_descriptor_tmp.7.6152
- __block_descriptor_tmp.7.6174
- __block_descriptor_tmp.7.826
- __block_descriptor_tmp.70.4674
- __block_descriptor_tmp.7186
- __block_descriptor_tmp.72.4669
- __block_descriptor_tmp.7323
- __block_descriptor_tmp.7563
- __block_descriptor_tmp.76.4771
- __block_descriptor_tmp.8.4076
- __block_descriptor_tmp.8.6488
- __block_descriptor_tmp.8.834
- __block_descriptor_tmp.80.4769
- __block_descriptor_tmp.820
- __block_descriptor_tmp.9.4083
- __block_descriptor_tmp.91.4743
- __block_descriptor_tmp.93.4741
- __block_descriptor_tmp.966
- __block_literal_global.12.4577
- __block_literal_global.12.6035
- __block_literal_global.12.7198
- __block_literal_global.129
- __block_literal_global.134
- __block_literal_global.141
- __block_literal_global.1415
- __block_literal_global.144
- __block_literal_global.149
- __block_literal_global.15.4231
- __block_literal_global.15.7443
- __block_literal_global.1501
- __block_literal_global.16.4583
- __block_literal_global.166.4436
- __block_literal_global.20.4218
- __block_literal_global.20.4589
- __block_literal_global.2200
- __block_literal_global.2271
- __block_literal_global.2367
- __block_literal_global.241
- __block_literal_global.249
- __block_literal_global.250
- __block_literal_global.253
- __block_literal_global.264
- __block_literal_global.283
- __block_literal_global.2955
- __block_literal_global.3.6023
- __block_literal_global.309
- __block_literal_global.31.6764
- __block_literal_global.315
- __block_literal_global.3252
- __block_literal_global.3426
- __block_literal_global.35.3125
- __block_literal_global.3543
- __block_literal_global.373
- __block_literal_global.39.3154
- __block_literal_global.395
- __block_literal_global.409
- __block_literal_global.4227
- __block_literal_global.43.3126
- __block_literal_global.43.4455
- __block_literal_global.43.6434
- __block_literal_global.4454
- __block_literal_global.4799
- __block_literal_global.5.6161
- __block_literal_global.5.6490
- __block_literal_global.5314
- __block_literal_global.54.4563
- __block_literal_global.555
- __block_literal_global.5559
- __block_literal_global.562
- __block_literal_global.566
- __block_literal_global.571
- __block_literal_global.575
- __block_literal_global.5932
- __block_literal_global.597
- __block_literal_global.6021
- __block_literal_global.6157
- __block_literal_global.6448
- __block_literal_global.66.5934
- __block_literal_global.6715
- __block_literal_global.675
- __block_literal_global.6775
- __block_literal_global.6986
- __block_literal_global.7184
- __block_literal_global.7321
- __block_literal_global.7434
- __block_literal_global.7561
- __block_literal_global.8.1515
- __block_literal_global.8.2194
- __block_literal_global.8.7190
- __block_literal_global.818
- __block_literal_global.9.6172
- __block_literal_global.964
- _abort
- _getLocalTimestampFromPlatformTime
- _mDNSPreferencesSetName
- _mdns_server_log.s_log.4232
- _mdns_server_log.s_once.4230
- g_nwi_state.4435
- g_session_list.4236
- mDNSCoreReceiveUpdate.msgs.264
CStrings:
+ "%!s(MISSING)reports-push-connection-error"
+ "*** Network Configuration Change *** -- change count: %!l(MISSING)d, delay: %!d(MISSING), flags: %!{(MISSING)public, mdnsresponder:net_change_flags}d"
+ "*** Network Configuration Change *** -- network changed: %!{(MISSING)mdns:yesno}d, delay: %!d(MISSING) ticks"
+ ", reports connection error"
+ "B16@?0r^{mdns_dns_service_s={mdns_obj_s=^vii^{mdns_kind_s}}Q{_discovered_detail_s=QQ^{nw_endpoint}B[7c]}^{mdns_resolver_s}^{mdns_push_server_s}^{__CFArray}^{_domain_item_s}^{nw_resolver_config}*^v^?^{__CFArray}^{mdns_dns_service_s}^{__CFArray}^{__CFArray}^{mdns_xpc_string_s}**^{mdns_querier_s}^{__CFArray}^{dispatch_source_s}^{nw_array}^{mdns_domain_name_s}^{dispatch_source_s}^{__CFArray}^{dispatch_queue_s}@?IIiIISSCCcBBBBB[0c]}8"
+ "ConfigResolvers -- scope type: %!{(MISSING)public, mdnsresponder:dns_scope_type}d, resolver[%!d(MISSING)]: {domain: %!{(MISSING)sensitive, mask.hash}s, name server count: %!d(MISSING)}"
+ "ConfigSearchDomains -- search domain: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P"
+ "ConfigSearchDomains: An invalid search domain was detected -- index: %!d(MISSING), name server count: %!d(MISSING)"
+ "ConfigSearchDomains: Ignoring search domains for interface -- scope type: %!{(MISSING)public, mdnsresponder:dns_scope_type}d"
+ "ConfigSearchDomains: Ignoring search domains for interface -- scope type: %!{(MISSING)public, mdnsresponder:dns_scope_type}d, ifname: %!{(MISSING)public}s"
+ "ConfigSearchDomains: configuring search domains -- count: %!d(MISSING), scope type: %!{(MISSING)public, mdnsresponder:dns_scope_type}d, generation: %!l(MISSING)lu"
+ "ConfigSearchDomains: configuring search domains -- count: %!d(MISSING), scope type: %!{(MISSING)public, mdnsresponder:dns_scope_type}d, generation: %!l(MISSING)lu, ifname: %!{(MISSING)public}s"
+ "NetWakeInterface: SIOCGIFWAKEFLAGS failed -- ifname: %!{(MISSING)public}s, error: %!{(MISSING)darwin.errno}d"
+ "NetWakeInterface: interface -- ifname: %!{(MISSING)public}s, address: %!{(MISSING)sensitive, mask.hash, mdnsresponder:ip_addr}.20P, supports Wake-On-Lan: %!{(MISSING)mdns:yesno}d"
+ "NetWakeInterface: interface supports TCP Keepalive -- ifname: %!{(MISSING)public}s"
+ "NetWakeInterface: socket failed -- socket: %!d(MISSING), ifname: %!{(MISSING)public}s, error: %!{(MISSING)darwin.errno}d"
+ "Received Goodbye packet for cached record -- name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, last time received: %!{(MISSING)public, timeval}.*P, interface index: %!d(MISSING), source address: %!{(MISSING)sensitive, mask.hash, mdnsresponder:ip_addr}.20P, name hash if PTR: %!x(MISSING)"
+ "SysEventCallBack -- event: %!{(MISSING)public, mdnsresponder:kev_dl_event}d"
+ "SysEventCallBack error -- error: %!{(MISSING)mdns:err}ld"
+ "[DSO%!l(MISSING)lu] DSO session is forcibly aborted by the other side -- error: %!{(MISSING)mdns:err}ld"
+ "[DSO%!l(MISSING)lu] Reporting connection error to the client -- error: %!{(MISSING)mdns:err}ld"
+ "[Q%!d(MISSING)] AnswerQuestionByFollowingCNAME: Resolving a .local CNAME -- CNAME: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P"
+ "[Q%!d(MISSING)] GenerateNegativeResponse: Generating negative response for question"
+ "[Q%!u(MISSING)] AnswerQuestionByFollowingCNAME: Not following CNAME referral -- CNAME: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, referral count: %!u(MISSING), self referential: %!{(MISSING)mdns:yesno}d"
+ "[Q%!u(MISSING)] AnswerQuestionByFollowingCNAME: following CNAME referral -- CNAME: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, referral count: %!u(MISSING)"
+ "[Q%!u(MISSING)] mDNS_StartQuery_internal START -- qname: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), qtype: %!{(MISSING)mdns:rrtype}d"
+ "[Q%!u(MISSING)] mDNS_StartQuery_internal: Purging records before resolving"
+ "[Q%!u(MISSING)] mDNS_StopQuery_internal STOP -- name hash: %!x(MISSING)"
+ "[R%!d(MISSING)->Q%!d(MISSING)] DNSServiceResolve(%!{(MISSING)sensitive, mask.hash}s (%!x(MISSING))) NoSuchRecord"
+ "[R%!d(MISSING)->Q%!d(MISSING)] DNSServiceResolve(%!{(MISSING)sensitive, mask.hash}s (%!x(MISSING))) RESULT   %!{(MISSING)sensitive, mask.hash}s (%!x(MISSING)):%!d(MISSING)"
+ "[R%!d(MISSING)] DNSServiceRegister(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), %!u(MISSING)) STOP PID[%!d(MISSING)](%!{(MISSING)public}s) -- duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Q%!u(MISSING)] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Q%!u(MISSING)] Question assigned DNS service %!l(MISSING)lu"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceBrowse result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceGetAddrInfo result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceQueryRecord result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name hash: %!x(MISSING), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), dnssec: %!{(MISSING)public, mdns:dnssec_result}d, type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->mDNSQ] DNSServiceResolve result -- event: %!{(MISSING)mdns:addrmv}d, expired: %!{(MISSING)mdns:yesno}d, ifindex: %!d(MISSING), name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)] DNSServiceBrowse -> SubBrowser START -- qname: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING))"
+ "[R%!u(MISSING)] DNSServiceBrowse Cancel domain enumeration for WAB and mDNS -- , duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceBrowse Cancel domain enumeration for WAB and mDNS -- , flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), , duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceBrowse START -- "
+ "[R%!u(MISSING)] DNSServiceBrowse START -- service type: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, domain: %!{(MISSING)sensitive, mask.hash}s, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), "
+ "[R%!u(MISSING)] DNSServiceBrowse STOP -- name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceBrowse STOP -- service name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceGetAddrInfo START -- hostname: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, protocols: %!u(MISSING), DNSSEC enabled, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceGetAddrInfo START -- hostname: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, protocols: %!u(MISSING), flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceGetAddrInfo START -- name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceGetAddrInfo STOP -- hostname: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceGetAddrInfo STOP -- name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceQueryRecord START -- name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceQueryRecord START -- qname: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %!{(MISSING)mdns:rrtype}d, DNSSEC enabled, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceQueryRecord START -- qname: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %!{(MISSING)mdns:rrtype}d, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceQueryRecord STOP -- name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceQueryRecord STOP -- qname: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, qtype: %!{(MISSING)mdns:rrtype}d, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceReconfirmRecord FAILED -- "
+ "[R%!u(MISSING)] DNSServiceReconfirmRecord FAILED -- name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceReconfirmRecord FAILED -- rr name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %!{(MISSING)mdns:rrtype}d, error: %!d(MISSING), flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), "
+ "[R%!u(MISSING)] DNSServiceReconfirmRecord FAILED -- rr name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %!{(MISSING)mdns:rrtype}d, error: %!d(MISSING), flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceReconfirmRecord START -- "
+ "[R%!u(MISSING)] DNSServiceReconfirmRecord START -- name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceReconfirmRecord START -- rr name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %!{(MISSING)mdns:rrtype}d, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), "
+ "[R%!u(MISSING)] DNSServiceReconfirmRecord START -- rr name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, rr type: %!{(MISSING)mdns:rrtype}d, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceRegister START -- name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceRegister START -- service type: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, domain: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, port: %!u(MISSING), flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceRegister STOP -- , duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceRegister STOP -- SRV name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), port: %!u(MISSING), flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), , duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceRegister STOP -- SRV name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), port: %!u(MISSING), flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceRegister STOP -- name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceRegister result -- event: ADDED, SRV name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), port: %!u(MISSING), PTR name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceRegister(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), %!u(MISSING)) %!s(MISSING)"
+ "[R%!u(MISSING)] DNSServiceRegisterRecord START -- "
+ "[R%!u(MISSING)] DNSServiceRegisterRecord START -- name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceRegisterRecord START -- name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %!{(MISSING)mdns:rrtype}d, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), "
+ "[R%!u(MISSING)] DNSServiceRegisterRecord START -- name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, type: %!{(MISSING)mdns:rrtype}d, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceResolve START -- SRV name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceResolve START -- name hash: %!x(MISSING)"
+ "[R%!u(MISSING)] DNSServiceResolve STOP -- SRV name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, flags: 0x%!X(MISSING), interface index: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceResolve STOP -- name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "[R%!u(MISSING)] DNSServiceUpdateRecord(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), %!{(MISSING)mdns:rrtype}d) UPDATE PID[%!d(MISSING)](%!s(MISSING))"
+ "body"
+ "conflictWithCacheRecordsOrFlush - new TSR, flushing interface %!d(MISSING) %!{(MISSING)sensitive, mask.hash}s"
+ "connection_error"
+ "handle_regrecord_request: TSR Stale Data, record cache is newer %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P InterfaceID %!p(MISSING)"
+ "isExcludedInterface: SIOCGIFFUNCTIONALTYPE failed -- error: %!{(MISSING)darwin.errno}d"
+ "isExcludedInterface: excluding %!{(MISSING)public}s"
+ "isExcludedInterface: excluding coprocessor interface %!{(MISSING)public}s"
+ "mDNSPlatformSetDNSConfig -- config->n_resolver: %!d(MISSING), this config generagtion: %!l(MISSING)lu, last config generation: %!l(MISSING)lu, changed: %!{(MISSING)mdns:yesno}d"
+ "mDNSPlatformSetDNSConfig Error: dns_configuration_copy returned NULL"
+ "mDNSPlatformSetDNSConfig new updates -- setservers: %!{(MISSING)mdns:yesno}d, setsearch: %!{(MISSING)mdns:yesno}d, fqdn: %!{(MISSING)mdns:yesno}d, RegDomains: %!{(MISSING)mdns:yesno}d, BrowseDomains: %!{(MISSING)mdns:yesno}d"
+ "mDNSPlatformSetDNSConfig: acking configuration"
+ "mDNSPreferencesSetNames: changing computer name -- last change: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_label}.*P -> %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_label}.*P, current change: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_label}.*P -> %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_label}.*P"
+ "mDNSPreferencesSetNames: changing local host name -- last change: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_label}.*P -> %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_label}.*P, current change: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_label}.*P -> %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_label}.*P"
+ "mDNSResponder-2559.0.51"
+ "mDNS_AddSearchDomain: domain already in list -- search domain: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P"
+ "mDNS_AddSearchDomain: new search domain added -- search domain: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, InterfaceID %!p(MISSING)"
+ "mDNS_Register_internal: adding to active record list -- name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "mDNS_Register_internal: adding to active record list -- name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "mDNS_Register_internal: adding to duplicate list -- name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "mDNS_Register_internal: adding to duplicate list -- name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "register_service_instance: TSR Stale Data, record cache is newer %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P InterfaceID %!p(MISSING)"
+ "reports_connection_errors"
+ "uDNS_SetupWABQueries -- action: 0x%!x(MISSING), flags: 0x%!x(MISSING), ifid: %!p(MISSING), domain: %!{(MISSING)public, mdnsresponder:domain_name}.*P (%!x(MISSING))"
+ "uDNS_SetupWABQueries: DELETE Browse for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: DELETE Deregistering PTR -- record: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P PTR %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P"
+ "uDNS_SetupWABQueries: DELETE Legacy Browse for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: DELETE Registration for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: Deleting Browse for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: Deleting Legacy Browse for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: Deleting Registration for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowse) returned error -- name hash: %!x(MISSING), error: %!d(MISSING)"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowseAutomatic) returned error -- name hash: %!x(MISSING), error: %!d(MISSING)"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeBrowseDefault) returned error -- name hash: %!x(MISSING), error: %!d(MISSING)"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeRegistration) returned error -- name hash: %!x(MISSING), error: %!d(MISSING)"
+ "uDNS_SetupWABQueries: GetDomains(mDNS_DomainTypeRegistrationDefault) returned error -- name hash: %!x(MISSING), error: %!d(MISSING)"
+ "uDNS_SetupWABQueries: Starting Browse for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: Starting Default Browse for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: Starting Default Registration for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: Starting Legacy Browse for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: Starting Registration for domain -- name hash: %!x(MISSING)"
+ "uDNS_SetupWABQueries: mDNS_Deregister returned error -- error: %!d(MISSING)"
+ "xD2DServiceCallback -- event: %!{(MISSING)public, mdnsresponder:d2d_service_event}d"
- " (Self-Referential)"
- " (no scheduled configuration change)"
- " + SetKeyChainTimer"
- " BrowseDomains"
- " RegDomains"
- " fqdn"
- " setsearch"
- " setservers"
- "%!s(MISSING): %!s(MISSING)"
- "(Computer Name) "
- "(DNS) "
- "(DynamicDNS) "
- "(Local Hostname) "
- "(P2P/IFEF_DIRECTLINK/IFEF_AWDL/IsCarPlaySSID) "
- "(kSCValNetIPv4ConfigMethodLinkLocal) "
- "*** Network Configuration Change ***  %!d(MISSING) ticks late%!{(MISSING)public}s"
- "*** Network Configuration Change *** %!l(MISSING)d change%!{(MISSING)public}s %!{(MISSING)public}s%!{(MISSING)public}s%!{(MISSING)public}s%!{(MISSING)public}s%!{(MISSING)public}s%!{(MISSING)public}sdelay %!d(MISSING)%!{(MISSING)public}s"
- "B16@?0r^{mdns_dns_service_s={mdns_obj_s=^vii^{mdns_kind_s}}Q{_discovered_detail_s=QQ^{nw_endpoint}B[7c]}^{mdns_resolver_s}^{mdns_push_server_s}^{__CFArray}^{_domain_item_s}^{nw_resolver_config}*^v^?^{__CFArray}^{mdns_dns_service_s}^{__CFArray}^{__CFArray}^{mdns_xpc_string_s}**^{mdns_querier_s}^{__CFArray}^{dispatch_source_s}^{nw_array}^{mdns_domain_name_s}^{dispatch_source_s}^{__CFArray}IIiIISSCCcBBBBB[0c]}8"
- "ChangedKeysHaveIPv4LL: Empty dictionary"
- "ChangedKeysHaveIPv4LL: No dictionary"
- "ChangedKeysHaveIPv4LL: configmethod %!s(MISSING)"
- "ChangedKeysHaveIPv4LL: found serviceid %!s(MISSING)"
- "ChangedKeysHaveIPv4LL: potential ifname %!s(MISSING)"
- "CheckInterfaceSupport: No %!{(MISSING)public}s for interface %!{(MISSING)public}s/%!{(MISSING)public}s kr 0x%!X(MISSING)"
- "CheckInterfaceSupport: No service for interface %!{(MISSING)public}s"
- "ConfigResolvers: %!s(MISSING) resolver[%!d(MISSING)] domain %!s(MISSING) n_nameserver %!d(MISSING)"
- "ConfigSearchDomains: (%!s(MISSING)) Ignoring search domain for interface %!s(MISSING)"
- "ConfigSearchDomains: (%!s(MISSING)) configuring search domain %!s(MISSING) %!s(MISSING) (generation= %!l(MISSING)lu)"
- "ConfigSearchDomains: An invalid search domain was detected for %!s(MISSING) domain %!s(MISSING) n_nameserver %!d(MISSING), (generation= %!l(MISSING)lu)"
- "D2DServiceFound"
- "D2DServiceLost"
- "D2DServicePeerLost"
- "D2DServiceReleased"
- "D2DServiceResolved"
- "D2DServiceRetained"
- "ERROR: malloc"
- "FinalizeSearchDomains: The hash is different"
- "FinalizeSearchDomains: The hash is same"
- "InitCommonState: setting RequestUnicast = %!d(MISSING) for %!s(MISSING) (%!s(MISSING))"
- "InterfaceScoped"
- "KEV_DL_ADDMULTI"
- "KEV_DL_DELMULTI"
- "KEV_DL_IFCAP_CHANGED"
- "KEV_DL_IF_ATTACHED"
- "KEV_DL_IF_DETACHED"
- "KEV_DL_IF_DETACHING"
- "KEV_DL_IF_IDLE_ROUTE_REFCNT"
- "KEV_DL_LINK_ADDRESS_CHANGED"
- "KEV_DL_LINK_OFF"
- "KEV_DL_LINK_ON"
- "KEV_DL_LINK_QUALITY_METRIC_CHANGED"
- "KEV_DL_PROTO_ATTACHED"
- "KEV_DL_PROTO_DETACHED"
- "KEV_DL_SIFFLAGS"
- "KEV_DL_SIFGENERIC"
- "KEV_DL_SIFMEDIA"
- "KEV_DL_SIFMETRICS"
- "KEV_DL_SIFMTU"
- "KEV_DL_SIFPHYS"
- "KEV_DL_SUBCLASS"
- "KEV_DL_WAKEFLAGS_CHANGED"
- "KEV_NETWORK_CLASS"
- "KEV_VENDOR_APPLE"
- "NetWakeInterface SIOCGIFWAKEFLAGS %!s(MISSING) errno %!d(MISSING) (%!s(MISSING))"
- "NetWakeInterface socket failed %!s(MISSING) error %!d(MISSING) errno %!d(MISSING) (%!s(MISSING))"
- "NetWakeInterface: %!s(MISSING) supports TCP Keepalive returning true"
- "NetWakeInterface: %!{(MISSING)public}s %!{(MISSING)sensitive, mask.hash, mdnsresponder:ip_addr}.20P %!{(MISSING)public}s WOMP"
- "NetworkChanged: interface %!s(MISSING) qualifies for reduced change handling delay"
- "Received Goodbye packet for cached record - name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), type: %!{(MISSING)public}s, last time received: %!{(MISSING)public}s, interface: %!{(MISSING)public}s, source address: %!{(MISSING)sensitive, mask.hash, mdnsresponder:ip_addr}.20P, RDATA domain if PTR: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P, name hash if PTR: %!x(MISSING)"
- "ServiceScoped"
- "SysEventCallBack got %!l(MISSING)d bytes size %!u(MISSING) %!X(MISSING) %!s(MISSING) %!X(MISSING) %!s(MISSING) %!X(MISSING) %!s(MISSING) id %!d(MISSING) code %!d(MISSING) %!s(MISSING)"
- "SysEventCallBack: recv error %!l(MISSING)d errno %!d(MISSING) (%!s(MISSING))"
- "Unscoped"
- "[DSO%!l(MISSING)lu] DSO session is forcibly aborted by the other side."
- "[R%!d(MISSING)->Q%!d(MISSING)] AnswerQuestionByFollowingCNAME: %!p(MISSING) %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!{(MISSING)public}s)  NOT following CNAME referral %!d(MISSING)%!{(MISSING)public}s for %!{(MISSING)sensitive, mask.hash}s"
- "[R%!d(MISSING)->Q%!d(MISSING)] AnswerQuestionByFollowingCNAME: %!p(MISSING) %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!{(MISSING)public}s) following CNAME referral %!d(MISSING) for %!{(MISSING)sensitive, mask.hash}s"
- "[R%!d(MISSING)->Q%!d(MISSING)] AnswerQuestionByFollowingCNAME: Resolving a .local CNAME %!p(MISSING) %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!{(MISSING)public}s) Record %!{(MISSING)sensitive, mask.hash}s"
- "[R%!d(MISSING)->Q%!d(MISSING)] DNSServiceBrowse(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!{(MISSING)public}s) RESULT %!{(MISSING)mdns:addrmv_upper}d interface %!d(MISSING): %!{(MISSING)sensitive, mask.hash}s"
- "[R%!d(MISSING)->Q%!d(MISSING)] DNSServiceResolve(%!{(MISSING)sensitive, mask.hash}s(%!x(MISSING))) NoSuchRecord"
- "[R%!d(MISSING)->Q%!d(MISSING)] DNSServiceResolve(%!{(MISSING)sensitive, mask.hash}s(%!x(MISSING))) RESULT   %!{(MISSING)sensitive, mask.hash}s(%!x(MISSING)):%!d(MISSING)"
- "[R%!d(MISSING)->Q%!d(MISSING)] GenerateNegativeResponse: Generating negative response for question %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!{(MISSING)public}s)"
- "[R%!d(MISSING)] DNSServiceBrowse(%!X(MISSING), %!d(MISSING), \"%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P\"(%!x(MISSING))) STOP PID[%!d(MISSING)](%!{(MISSING)public}s) -- duration: %!{(MISSING)mdns:time_duration}u"
- "[R%!d(MISSING)] DNSServiceBrowse(%!X(MISSING), %!d(MISSING), \"%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P\", \"%!{(MISSING)sensitive, mask.hash}s\") START PID[%!d(MISSING)](%!{(MISSING)public}s)"
- "[R%!d(MISSING)] DNSServiceQueryRecord(%!X(MISSING), %!d(MISSING), %!{(MISSING)sensitive, mask.hash}s(%!x(MISSING)), %!{(MISSING)mdns:rrtype}d%!{(MISSING)public}s) START PID[%!d(MISSING)](%!{(MISSING)public}s)"
- "[R%!d(MISSING)] DNSServiceReconfirmRecord(%!X(MISSING), %!d(MISSING), %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!{(MISSING)mdns:rrtype}d) FAILED PID[%!d(MISSING)](%!{(MISSING)public}s) -- status: %!d(MISSING)"
- "[R%!d(MISSING)] DNSServiceReconfirmRecord(%!X(MISSING), %!d(MISSING), %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!{(MISSING)mdns:rrtype}d) START PID[%!d(MISSING)](%!{(MISSING)public}s)"
- "[R%!d(MISSING)] DNSServiceRegister(%!X(MISSING), %!d(MISSING), \"%!{(MISSING)sensitive, mask.hash}s\", \"%!{(MISSING)sensitive, mask.hash}s\", \"%!{(MISSING)sensitive, mask.hash}s\", %!x(MISSING), \"%!{(MISSING)sensitive, mask.hash}s\", %!u(MISSING)) START PID[%!d(MISSING)](%!{(MISSING)public}s)"
- "[R%!d(MISSING)] DNSServiceRegister(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!u(MISSING)) STOP PID[%!d(MISSING)](%!{(MISSING)public}s) -- duration: %!{(MISSING)mdns:time_duration}u"
- "[R%!d(MISSING)] DNSServiceRegisterRecord(0x%!X(MISSING), %!d(MISSING), %!{(MISSING)sensitive, mask.hash}s) START PID[%!d(MISSING)](%!{(MISSING)public}s)"
- "[R%!d(MISSING)] DNSServiceResolve(%!X(MISSING), %!d(MISSING), \"%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P\"(%!x(MISSING))) START PID[%!d(MISSING)](%!{(MISSING)public}s)"
- "[R%!d(MISSING)] DNSServiceResolve(%!X(MISSING), %!d(MISSING), \"%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P\"(%!x(MISSING))) STOP PID[%!d(MISSING)](%!{(MISSING)public}s) -- duration: %!{(MISSING)mdns:time_duration}u"
- "[R%!u(MISSING)->Q%!u(MISSING)] DNSService%!{(MISSING)public}s(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!{(MISSING)mdns:rrtype}d) RESULT %!{(MISSING)mdns:addrmv_upper}d interface %!d(MISSING): (%!{(MISSING)mdns:mortality}d, %!{(MISSING)public, mdns:dnssec_result}d)%!{(MISSING)sensitive, mask.hash}s"
- "[R%!u(MISSING)->Q%!u(MISSING)] Question for %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!{(MISSING)public}s%!{(MISSING)public}s) assigned DNS service %!l(MISSING)lu"
- "[R%!u(MISSING)] DNSServiceBrowse - SubBrowser(\"%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P\"(%!x(MISSING))) START"
- "[R%!u(MISSING)] DNSServiceBrowse Cancel domain enumeration for WAB and mDNS PID[%!d(MISSING)](%!{(MISSING)public}s)"
- "[R%!u(MISSING)] DNSServiceGetAddrInfo(%!X(MISSING), %!d(MISSING), %!u(MISSING), %!{(MISSING)sensitive, mask.hash}s%!{(MISSING)public}s) START PID[%!d(MISSING)](%!{(MISSING)public}s)"
- "[R%!u(MISSING)] DNSServiceGetAddrInfo(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P) STOP PID[%!d(MISSING)](%!{(MISSING)public}s) -- duration: %!{(MISSING)mdns:time_duration}u"
- "[R%!u(MISSING)] DNSServiceQueryRecord(%!X(MISSING), %!d(MISSING), %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!{(MISSING)mdns:rrtype}d) STOP PID[%!d(MISSING)](%!{(MISSING)public}s) -- duration: %!{(MISSING)mdns:time_duration}u"
- "[R%!u(MISSING)] DNSServiceRegister(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!u(MISSING)) %!s(MISSING)"
- "[R%!u(MISSING)] DNSServiceRegister(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!u(MISSING)) ADDED -- PTR name hash: %!x(MISSING)"
- "[R%!u(MISSING)] DNSServiceResolve(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING))) %!{(MISSING)mdns:addrmv_upper}d interface %!u(MISSING): %!{(MISSING)sensitive, mask.hash}s"
- "[R%!u(MISSING)] DNSServiceUpdateRecord(%!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), %!{(MISSING)mdns:rrtype}d) UPDATE PID[%!d(MISSING)](%!s(MISSING))"
- "browse_termination_callback: calling external_stop_browsing_for_service()"
- "for interface %!s(MISSING)"
- "isExcludedInterface: SIOCGIFFUNCTIONALTYPE failed, errno = %!d(MISSING) (%!s(MISSING))"
- "isExcludedInterface: excluding %!s(MISSING)"
- "isExcludedInterface: excluding coprocessor interface %!s(MISSING)"
- "mDNSPlatformSetDNSConfig(setservers): generation number %!l(MISSING)lu same, not processing"
- "mDNSPlatformSetDNSConfig: Acking configuration setservers %!d(MISSING), setsearch %!d(MISSING)"
- "mDNSPlatformSetDNSConfig: Error: dns_configuration_copy returned NULL"
- "mDNSPlatformSetDNSConfig: config->n_resolver = %!d(MISSING), generation %!l(MISSING)lu, last %!l(MISSING)lu"
- "mDNSPlatformSetDNSConfig:%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)"
- "mDNSPreferencesSetNames not invoking helper %!s(MISSING) %!s(MISSING), %!s(MISSING) %!s(MISSING), old %!s(MISSING), new %!s(MISSING)"
- "mDNSResponder-2559.0.31"
- "mDNS_AddSearchDomain already in list %!s(MISSING)"
- "mDNS_AddSearchDomain created new %!s(MISSING), InterfaceID %!p(MISSING)"
- "mDNS_Register_internal: Adding to active record list -- name hash: %!x(MISSING) %!{(MISSING)sensitive, mask.hash}s"
- "mDNS_Register_internal: Adding to duplicate list  name hash: %!x(MISSING) %!{(MISSING)sensitive, mask.hash}s"
- "mDNS_StartQuery_internal: NumAllInterfaceRecords %!u(MISSING) NumAllInterfaceQuestions %!u(MISSING) %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!{(MISSING)public}s)"
- "mDNS_StartQuery_internal: Purging for %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P"
- "mDNS_StopQuery_internal: NumAllInterfaceRecords %!u(MISSING) NumAllInterfaceQuestions %!u(MISSING) %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P (%!{(MISSING)public}s)"
- "prevnewhostlabel"
- "prevnewnicelabel"
- "prevoldhostlabel"
- "prevoldnicelabel"
- "supports"
- "uDNS_SetupWABQueries: DELETE  Browse for domain  %!s(MISSING)"
- "uDNS_SetupWABQueries: DELETE  Legacy Browse for domain  %!s(MISSING)"
- "uDNS_SetupWABQueries: DELETE  Registration for domain  %!s(MISSING)"
- "uDNS_SetupWABQueries: DELETE Deregistering PTR %!s(MISSING) -> %!s(MISSING)"
- "uDNS_SetupWABQueries: Deleting Browse for domain  %!s(MISSING)"
- "uDNS_SetupWABQueries: Deleting Legacy Browse for domain  %!s(MISSING)"
- "uDNS_SetupWABQueries: Deleting Registration for domain  %!s(MISSING)"
- "uDNS_SetupWABQueries: GetDomains for domain %!s(MISSING) returned error(s):\n%!d(MISSING) (mDNS_DomainTypeBrowse)\n"
- "uDNS_SetupWABQueries: GetDomains for domain %!s(MISSING) returned error(s):\n%!d(MISSING) (mDNS_DomainTypeBrowseAutomatic)\n"
- "uDNS_SetupWABQueries: GetDomains for domain %!s(MISSING) returned error(s):\n%!d(MISSING) (mDNS_DomainTypeBrowseDefault)\n"
- "uDNS_SetupWABQueries: GetDomains for domain %!s(MISSING) returned error(s):\n%!d(MISSING) (mDNS_DomainTypeRegistration)\n"
- "uDNS_SetupWABQueries: GetDomains for domain %!s(MISSING) returned error(s):\n%!d(MISSING) (mDNS_DomainTypeRegistrationDefault)"
- "uDNS_SetupWABQueries: Starting Browse for domain %!s(MISSING)"
- "uDNS_SetupWABQueries: Starting Default Browse for domain %!s(MISSING)"
- "uDNS_SetupWABQueries: Starting Default Registration for domain %!s(MISSING)"
- "uDNS_SetupWABQueries: Starting Legacy Browse for domain %!s(MISSING)"
- "uDNS_SetupWABQueries: Starting Registration for domain %!s(MISSING)"
- "uDNS_SetupWABQueries:: ERROR!! mDNS_Deregister returned %!d(MISSING)"
- "uDNS_SetupWABQueries:action 0x%!x(MISSING): Flags 0x%!x(MISSING),  AuthRecs %!p(MISSING), InterfaceID %!p(MISSING) %!s(MISSING)"
- "xD2DServiceCallback - event: %!{(MISSING)public}s, result: %!d(MISSING), instanceHandle: %!p(MISSING), transportType: %!u(MISSING), LHS: %!p(MISSING) (%!z(MISSING)u), RHS: %!p(MISSING) (%!z(MISSING)u), userData: %!p(MISSING)"

```
