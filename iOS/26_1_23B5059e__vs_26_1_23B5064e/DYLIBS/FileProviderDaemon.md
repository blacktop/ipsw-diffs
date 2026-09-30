## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-3882.40.119.0.0
-  __TEXT.__text: 0x9eeccc
-  __TEXT.__auth_stubs: 0x5cc0
-  __TEXT.__objc_methlist: 0x9c24
-  __TEXT.__const: 0x25da0
-  __TEXT.__cstring: 0x4344d
-  __TEXT.__oslogstring: 0x1e4b2
-  __TEXT.__gcc_except_tab: 0xe788
+3882.40.131.0.0
+  __TEXT.__text: 0x9f1ee4
+  __TEXT.__auth_stubs: 0x5cd0
+  __TEXT.__objc_methlist: 0x9cc4
+  __TEXT.__const: 0x25e10
+  __TEXT.__cstring: 0x436dd
+  __TEXT.__oslogstring: 0x1e682
+  __TEXT.__gcc_except_tab: 0xe8e8
   __TEXT.__ustring: 0x176e
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__constg_swiftt: 0x12c84
-  __TEXT.__swift5_typeref: 0x122b0
+  __TEXT.__constg_swiftt: 0x12cf4
+  __TEXT.__swift5_typeref: 0x122f0
   __TEXT.__swift5_builtin: 0x898
   __TEXT.__swift5_mpenum: 0x134
-  __TEXT.__swift5_reflstr: 0xc3ed
-  __TEXT.__swift5_fieldmd: 0xafcc
+  __TEXT.__swift5_reflstr: 0xc44d
+  __TEXT.__swift5_fieldmd: 0xb024
   __TEXT.__swift5_assocty: 0x23f8
-  __TEXT.__swift5_capture: 0x184ec
+  __TEXT.__swift5_capture: 0x18414
   __TEXT.__swift5_proto: 0x1974
-  __TEXT.__swift5_types: 0xae4
+  __TEXT.__swift5_types: 0xae8
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_protos: 0xa0
   __TEXT.__swift_as_entry: 0xa8
   __TEXT.__swift_as_ret: 0xa4
-  __TEXT.__unwind_info: 0x14bc8
-  __TEXT.__eh_frame: 0x2705c
-  __TEXT.__objc_classname: 0xefa
-  __TEXT.__objc_methname: 0x1daf8
-  __TEXT.__objc_methtype: 0x6b4e
-  __TEXT.__objc_stubs: 0xff80
+  __TEXT.__unwind_info: 0x14c38
+  __TEXT.__eh_frame: 0x27104
+  __TEXT.__objc_classname: 0xefd
+  __TEXT.__objc_methname: 0x1dcc7
+  __TEXT.__objc_methtype: 0x6b6e
+  __TEXT.__objc_stubs: 0x10080
   __DATA_CONST.__got: 0x1828
-  __DATA_CONST.__const: 0x4e70
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__const: 0x4eb8
+  __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x61a8
+  __DATA_CONST.__objc_selrefs: 0x61f8
   __DATA_CONST.__objc_protorefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x2e70
-  __AUTH_CONST.__const: 0x45920
-  __AUTH_CONST.__cfstring: 0x6f60
-  __AUTH_CONST.__objc_const: 0x2c2e8
+  __DATA_CONST.__objc_arraydata: 0x100
+  __AUTH_CONST.__auth_got: 0x2e78
+  __AUTH_CONST.__const: 0x45748
+  __AUTH_CONST.__cfstring: 0x7060
+  __AUTH_CONST.__objc_const: 0x2c3c8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x20c8
-  __AUTH.__data: 0x25a8
-  __DATA.__objc_ivar: 0xb3c
-  __DATA.__data: 0x8738
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH.__objc_data: 0x21b8
+  __AUTH.__data: 0x25c8
+  __DATA.__objc_ivar: 0xb44
+  __DATA.__data: 0x86f8
   __DATA.__bss: 0x261d0
-  __DATA.__common: 0x2d0
+  __DATA.__common: 0x2e0
   __DATA_DIRTY.__objc_data: 0x3868
-  __DATA_DIRTY.__data: 0xe328
+  __DATA_DIRTY.__data: 0xe368
   __DATA_DIRTY.__bss: 0xb770
   __DATA_DIRTY.__common: 0x8e8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5C20A54D-8964-3086-AF9F-D04B334CDA6D
-  Functions: 29659
-  Symbols:   25532
-  CStrings:  13702
+  UUID: A29D64DF-E5BC-3368-A16D-5165C4BC4E34
+  Functions: 29687
+  Symbols:   25583
+  CStrings:  13743
 
Symbols:
+ -[FPDConfigurationStore partialReimportHierarchyLimit]
+ -[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:skipSysdiagnose:]
+ -[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:skipSysdiagnose:].cold.1
+ -[FPDTapToRadarManager requestTapToRadarWithTitle:description:keywords:attachments:displayReason:providerID:skipSysdiagnose:]
+ -[FPDVolume _isDiskSpaceMonitorRunning]
+ -[FPDVolume isDiskSpaceMonitorRunning]
+ -[FPDVolume maxTimerIterations]
+ -[FPDVolume monitorLowDiskSpaceRecoveryForConcreteError:].cold.4
+ -[FPDVolume monitorLowDiskSpaceRecovery].cold.1
+ -[FPDVolume monitorLowDiskSpaceRecovery].cold.2
+ -[FPDVolume shouldSkipDiskSpaceMonitor]
+ -[FPDVolume timerDelay]
+ -[FPDXPCServicer _test_isDiskSpaceMonitorRunningForDomain:completionHandler:]
+ -[FPDXPCServicer _test_isDiskSpaceMonitorRunningForDomain:completionHandler:].cold.1
+ GCC_except_table367
+ GCC_except_table370
+ GCC_except_table374
+ GCC_except_table383
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table406
+ GCC_except_table409
+ GCC_except_table412
+ GCC_except_table419
+ GCC_except_table420
+ GCC_except_table424
+ GCC_except_table429
+ GCC_except_table434
+ GCC_except_table435
+ GCC_except_table441
+ GCC_except_table442
+ GCC_except_table450
+ GCC_except_table453
+ GCC_except_table457
+ GCC_except_table458
+ GCC_except_table463
+ GCC_except_table472
+ GCC_except_table484
+ GCC_except_table487
+ GCC_except_table488
+ GCC_except_table551
+ _OBJC_CLASS_$__TtC18FileProviderDaemon21FPDynamicErrorDecider
+ _OBJC_IVAR_$_FPDConfigurationStore._partialReimportHierarchyLimit
+ _OBJC_IVAR_$_FPDVolume._diskSpaceRecoveryTimerCurrentIteration
+ _OBJC_METACLASS_$__TtC18FileProviderDaemon21FPDynamicErrorDecider
+ __CLASS_METHODS__TtC18FileProviderDaemon21FPDynamicErrorDecider
+ __DATA__TtC18FileProviderDaemon21FPDynamicErrorDecider
+ __INSTANCE_METHODS__TtC18FileProviderDaemon21FPDynamicErrorDecider
+ __METACLASS_DATA__TtC18FileProviderDaemon21FPDynamicErrorDecider
+ __PROTOCOLS__TtC18FileProviderDaemon17FPCKReportSection.26
+ ___168-[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:skipSysdiagnose:]_block_invoke
+ ___168-[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:skipSysdiagnose:]_block_invoke.33
+ ___168-[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:skipSysdiagnose:]_block_invoke.33.cold.1
+ ___168-[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:skipSysdiagnose:]_block_invoke.cold.1
+ ___77-[FPDXPCServicer _test_isDiskSpaceMonitorRunningForDomain:completionHandler:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.238
+ _block_copy_helper.1290
+ _block_copy_helper.1297
+ _block_copy_helper.1301
+ _block_copy_helper.1305
+ _block_copy_helper.1309
+ _block_copy_helper.1318
+ _block_copy_helper.1325
+ _block_copy_helper.1345
+ _block_copy_helper.1355
+ _block_copy_helper.1365
+ _block_copy_helper.1376
+ _block_copy_helper.1483
+ _block_copy_helper.1542
+ _block_copy_helper.1545
+ _block_copy_helper.1548
+ _block_copy_helper.1555
+ _block_copy_helper.1606
+ _block_copy_helper.1609
+ _block_copy_helper.1612
+ _block_copy_helper.1615
+ _block_copy_helper.1620
+ _block_copy_helper.1625
+ _block_copy_helper.1630
+ _block_copy_helper.1635
+ _block_copy_helper.1640
+ _block_copy_helper.1645
+ _block_copy_helper.4718
+ _block_copy_helper.4730
+ _block_copy_helper.4740
+ _block_copy_helper.4752
+ _block_copy_helper.4764
+ _block_copy_helper.4776
+ _block_copy_helper.4842
+ _block_copy_helper.4858
+ _block_copy_helper.4865
+ _block_copy_helper.4910
+ _block_copy_helper.5017
+ _block_copy_helper.5020
+ _block_copy_helper.5068
+ _block_copy_helper.5134
+ _block_copy_helper.5137
+ _block_copy_helper.5206
+ _block_copy_helper.5209
+ _block_copy_helper.5218
+ _block_copy_helper.5230
+ _block_copy_helper.5236
+ _block_copy_helper.5248
+ _block_copy_helper.5260
+ _block_copy_helper.5272
+ _block_copy_helper.5278
+ _block_copy_helper.5290
+ _block_copy_helper.5317
+ _block_copy_helper.5320
+ _block_copy_helper.5407
+ _block_copy_helper.5439
+ _block_copy_helper.5442
+ _block_copy_helper.5452
+ _block_copy_helper.5455
+ _block_copy_helper.5461
+ _block_copy_helper.5475
+ _block_copy_helper.5481
+ _block_copy_helper.5493
+ _block_copy_helper.5504
+ _block_copy_helper.5516
+ _block_copy_helper.5525
+ _block_copy_helper.5536
+ _block_copy_helper.5542
+ _block_copy_helper.5554
+ _block_copy_helper.5649
+ _block_copy_helper.5652
+ _block_copy_helper.5791
+ _block_copy_helper.5794
+ _block_copy_helper.5834
+ _block_copy_helper.5837
+ _block_copy_helper.5863
+ _block_copy_helper.5873
+ _block_copy_helper.5902
+ _block_copy_helper.5905
+ _block_copy_helper.5916
+ _block_copy_helper.5968
+ _block_copy_helper.5971
+ _block_copy_helper.5977
+ _block_copy_helper.5980
+ _block_copy_helper.5997
+ _block_copy_helper.6004
+ _block_copy_helper.6022
+ _block_copy_helper.6034
+ _block_copy_helper.6052
+ _block_copy_helper.6064
+ _block_copy_helper.6082
+ _block_copy_helper.6092
+ _block_copy_helper.6124
+ _block_copy_helper.6127
+ _block_copy_helper.6136
+ _block_copy_helper.6170
+ _block_copy_helper.6173
+ _block_copy_helper.6191
+ _block_copy_helper.6198
+ _block_descriptor.1292
+ _block_descriptor.1299
+ _block_descriptor.1303
+ _block_descriptor.1307
+ _block_descriptor.1311
+ _block_descriptor.1320
+ _block_descriptor.1327
+ _block_descriptor.1347
+ _block_descriptor.1357
+ _block_descriptor.1367
+ _block_descriptor.1378
+ _block_descriptor.1485
+ _block_descriptor.1544
+ _block_descriptor.1547
+ _block_descriptor.1550
+ _block_descriptor.1557
+ _block_descriptor.1608
+ _block_descriptor.1611
+ _block_descriptor.1614
+ _block_descriptor.1617
+ _block_descriptor.1622
+ _block_descriptor.1627
+ _block_descriptor.1632
+ _block_descriptor.1637
+ _block_descriptor.1642
+ _block_descriptor.1647
+ _block_descriptor.4720
+ _block_descriptor.4732
+ _block_descriptor.4742
+ _block_descriptor.4754
+ _block_descriptor.4766
+ _block_descriptor.4778
+ _block_descriptor.4844
+ _block_descriptor.4860
+ _block_descriptor.4867
+ _block_descriptor.4912
+ _block_descriptor.5019
+ _block_descriptor.5022
+ _block_descriptor.5070
+ _block_descriptor.5136
+ _block_descriptor.5139
+ _block_descriptor.5208
+ _block_descriptor.5211
+ _block_descriptor.5220
+ _block_descriptor.5232
+ _block_descriptor.5238
+ _block_descriptor.5250
+ _block_descriptor.5262
+ _block_descriptor.5274
+ _block_descriptor.5280
+ _block_descriptor.5292
+ _block_descriptor.5319
+ _block_descriptor.5322
+ _block_descriptor.5409
+ _block_descriptor.5441
+ _block_descriptor.5444
+ _block_descriptor.5454
+ _block_descriptor.5457
+ _block_descriptor.5463
+ _block_descriptor.5477
+ _block_descriptor.5483
+ _block_descriptor.5495
+ _block_descriptor.5506
+ _block_descriptor.5518
+ _block_descriptor.5527
+ _block_descriptor.5538
+ _block_descriptor.5544
+ _block_descriptor.5556
+ _block_descriptor.5651
+ _block_descriptor.5654
+ _block_descriptor.5793
+ _block_descriptor.5796
+ _block_descriptor.5836
+ _block_descriptor.5839
+ _block_descriptor.5865
+ _block_descriptor.5875
+ _block_descriptor.5904
+ _block_descriptor.5907
+ _block_descriptor.5918
+ _block_descriptor.5970
+ _block_descriptor.5973
+ _block_descriptor.5979
+ _block_descriptor.5982
+ _block_descriptor.5999
+ _block_descriptor.6006
+ _block_descriptor.6024
+ _block_descriptor.6036
+ _block_descriptor.6054
+ _block_descriptor.6066
+ _block_descriptor.6084
+ _block_descriptor.6094
+ _block_descriptor.6126
+ _block_descriptor.6129
+ _block_descriptor.6138
+ _block_descriptor.6172
+ _block_descriptor.6175
+ _block_descriptor.6193
+ _block_descriptor.6200
+ _block_destroy_helper.1291
+ _block_destroy_helper.1298
+ _block_destroy_helper.1302
+ _block_destroy_helper.1306
+ _block_destroy_helper.1310
+ _block_destroy_helper.1319
+ _block_destroy_helper.1326
+ _block_destroy_helper.1346
+ _block_destroy_helper.1356
+ _block_destroy_helper.1366
+ _block_destroy_helper.1377
+ _block_destroy_helper.1484
+ _block_destroy_helper.1543
+ _block_destroy_helper.1546
+ _block_destroy_helper.1549
+ _block_destroy_helper.1556
+ _block_destroy_helper.1607
+ _block_destroy_helper.1610
+ _block_destroy_helper.1613
+ _block_destroy_helper.1616
+ _block_destroy_helper.1621
+ _block_destroy_helper.1626
+ _block_destroy_helper.1631
+ _block_destroy_helper.1636
+ _block_destroy_helper.1641
+ _block_destroy_helper.1646
+ _block_destroy_helper.4719
+ _block_destroy_helper.4731
+ _block_destroy_helper.4741
+ _block_destroy_helper.4753
+ _block_destroy_helper.4765
+ _block_destroy_helper.4777
+ _block_destroy_helper.4843
+ _block_destroy_helper.4859
+ _block_destroy_helper.4866
+ _block_destroy_helper.4911
+ _block_destroy_helper.5018
+ _block_destroy_helper.5021
+ _block_destroy_helper.5069
+ _block_destroy_helper.5135
+ _block_destroy_helper.5138
+ _block_destroy_helper.5207
+ _block_destroy_helper.5210
+ _block_destroy_helper.5219
+ _block_destroy_helper.5231
+ _block_destroy_helper.5237
+ _block_destroy_helper.5249
+ _block_destroy_helper.5261
+ _block_destroy_helper.5273
+ _block_destroy_helper.5279
+ _block_destroy_helper.5291
+ _block_destroy_helper.5318
+ _block_destroy_helper.5321
+ _block_destroy_helper.5408
+ _block_destroy_helper.5440
+ _block_destroy_helper.5443
+ _block_destroy_helper.5453
+ _block_destroy_helper.5456
+ _block_destroy_helper.5462
+ _block_destroy_helper.5476
+ _block_destroy_helper.5482
+ _block_destroy_helper.5494
+ _block_destroy_helper.5505
+ _block_destroy_helper.5517
+ _block_destroy_helper.5526
+ _block_destroy_helper.5537
+ _block_destroy_helper.5543
+ _block_destroy_helper.5555
+ _block_destroy_helper.5650
+ _block_destroy_helper.5653
+ _block_destroy_helper.5792
+ _block_destroy_helper.5795
+ _block_destroy_helper.5835
+ _block_destroy_helper.5838
+ _block_destroy_helper.5864
+ _block_destroy_helper.5874
+ _block_destroy_helper.5903
+ _block_destroy_helper.5906
+ _block_destroy_helper.5917
+ _block_destroy_helper.5969
+ _block_destroy_helper.5972
+ _block_destroy_helper.5978
+ _block_destroy_helper.5981
+ _block_destroy_helper.5998
+ _block_destroy_helper.6005
+ _block_destroy_helper.6023
+ _block_destroy_helper.6035
+ _block_destroy_helper.6053
+ _block_destroy_helper.6065
+ _block_destroy_helper.6083
+ _block_destroy_helper.6093
+ _block_destroy_helper.6125
+ _block_destroy_helper.6128
+ _block_destroy_helper.6137
+ _block_destroy_helper.6171
+ _block_destroy_helper.6174
+ _block_destroy_helper.6192
+ _block_destroy_helper.6199
+ _keypath_get.13Tm
+ _keypath_get.17Tm
+ _keypath_get.3Tm
+ _keypath_get.9Tm
+ _keypath_set.4Tm
+ _objc_msgSend$_isDiskSpaceMonitorRunning
+ _objc_msgSend$isDiskSpaceMonitorRunning
+ _objc_msgSend$maxTimerIterations
+ _objc_msgSend$requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:skipSysdiagnose:
+ _objc_msgSend$requestTapToRadarWithTitle:description:keywords:attachments:displayReason:providerID:skipSysdiagnose:
+ _objc_msgSend$setAutoDiagnostics:
+ _objc_msgSend$shouldSendFor:
+ _objc_msgSend$shouldSkipDiskSpaceMonitor
+ _objc_msgSend$timerDelay
+ _objectdestroy.101Tm
+ _objectdestroy.1230Tm
+ _objectdestroy.1390Tm
+ _objectdestroy.1411Tm
+ _objectdestroy.146Tm
+ _objectdestroy.1487Tm
+ _objectdestroy.1490Tm
+ _objectdestroy.156Tm
+ _objectdestroy.1585Tm
+ _objectdestroy.337Tm
+ _objectdestroy.4702Tm
+ _objectdestroy.4786Tm
+ _objectdestroy.4994Tm
+ _objectdestroy.5037Tm
+ _objectdestroy.5656Tm
+ _objectdestroy.5687Tm
+ _objectdestroy.5742Tm
+ _objectdestroy.5861Tm
+ _objectdestroy.92Tm
+ _objectdestroy.98Tm
+ _symbolic _____ 18FileProviderDaemon21FPDynamicErrorDeciderC
+ _symbolic ___________y2ID_____QzAcDQy_G______pSgt 18FileProviderDaemon7JobCodeO AA16ReconciliationIDO AA0A4ItemP s5ErrorP
- -[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:]
- -[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:].cold.1
- GCC_except_table369
- GCC_except_table372
- GCC_except_table376
- GCC_except_table385
- GCC_except_table404
- GCC_except_table405
- GCC_except_table408
- GCC_except_table411
- GCC_except_table418
- GCC_except_table422
- GCC_except_table423
- GCC_except_table428
- GCC_except_table433
- GCC_except_table437
- GCC_except_table438
- GCC_except_table446
- GCC_except_table449
- GCC_except_table455
- GCC_except_table456
- GCC_except_table461
- GCC_except_table470
- GCC_except_table474
- GCC_except_table483
- GCC_except_table486
- GCC_except_table548
- __PROTOCOLS__TtC18FileProviderDaemon17FPCKReportSection.21
- ___152-[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:]_block_invoke
- ___152-[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:]_block_invoke.33
- ___152-[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:]_block_invoke.33.cold.1
- ___152-[FPDTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:]_block_invoke.cold.1
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.221
- _block_copy_helper.1328
- _block_copy_helper.1335
- _block_copy_helper.1339
- _block_copy_helper.1343
- _block_copy_helper.1356
- _block_copy_helper.1363
- _block_copy_helper.1383
- _block_copy_helper.1393
- _block_copy_helper.1403
- _block_copy_helper.1414
- _block_copy_helper.1518
- _block_copy_helper.1580
- _block_copy_helper.1583
- _block_copy_helper.1586
- _block_copy_helper.1593
- _block_copy_helper.1644
- _block_copy_helper.1647
- _block_copy_helper.1650
- _block_copy_helper.1653
- _block_copy_helper.1658
- _block_copy_helper.1663
- _block_copy_helper.1668
- _block_copy_helper.1673
- _block_copy_helper.1678
- _block_copy_helper.1683
- _block_copy_helper.4714
- _block_copy_helper.4726
- _block_copy_helper.4738
- _block_copy_helper.4750
- _block_copy_helper.4756
- _block_copy_helper.4768
- _block_copy_helper.4834
- _block_copy_helper.4850
- _block_copy_helper.4857
- _block_copy_helper.4902
- _block_copy_helper.5009
- _block_copy_helper.5012
- _block_copy_helper.5060
- _block_copy_helper.5126
- _block_copy_helper.5129
- _block_copy_helper.5198
- _block_copy_helper.5201
- _block_copy_helper.5210
- _block_copy_helper.5222
- _block_copy_helper.5228
- _block_copy_helper.5240
- _block_copy_helper.5252
- _block_copy_helper.5264
- _block_copy_helper.5270
- _block_copy_helper.5282
- _block_copy_helper.5309
- _block_copy_helper.5312
- _block_copy_helper.5399
- _block_copy_helper.5431
- _block_copy_helper.5434
- _block_copy_helper.5444
- _block_copy_helper.5447
- _block_copy_helper.5453
- _block_copy_helper.5467
- _block_copy_helper.5473
- _block_copy_helper.5485
- _block_copy_helper.5496
- _block_copy_helper.5508
- _block_copy_helper.5517
- _block_copy_helper.5528
- _block_copy_helper.5534
- _block_copy_helper.5546
- _block_copy_helper.5641
- _block_copy_helper.5644
- _block_copy_helper.5783
- _block_copy_helper.5786
- _block_copy_helper.5826
- _block_copy_helper.5829
- _block_copy_helper.5855
- _block_copy_helper.5865
- _block_copy_helper.5894
- _block_copy_helper.5897
- _block_copy_helper.5908
- _block_copy_helper.5960
- _block_copy_helper.5963
- _block_copy_helper.5969
- _block_copy_helper.5972
- _block_copy_helper.5989
- _block_copy_helper.5996
- _block_copy_helper.6014
- _block_copy_helper.6026
- _block_copy_helper.6044
- _block_copy_helper.6056
- _block_copy_helper.6074
- _block_copy_helper.6084
- _block_copy_helper.6116
- _block_copy_helper.6119
- _block_copy_helper.6128
- _block_copy_helper.6162
- _block_copy_helper.6165
- _block_copy_helper.6183
- _block_copy_helper.6190
- _block_descriptor.1330
- _block_descriptor.1337
- _block_descriptor.1341
- _block_descriptor.1345
- _block_descriptor.1358
- _block_descriptor.1365
- _block_descriptor.1385
- _block_descriptor.1395
- _block_descriptor.1405
- _block_descriptor.1416
- _block_descriptor.1520
- _block_descriptor.1582
- _block_descriptor.1585
- _block_descriptor.1588
- _block_descriptor.1595
- _block_descriptor.1646
- _block_descriptor.1649
- _block_descriptor.1652
- _block_descriptor.1655
- _block_descriptor.1660
- _block_descriptor.1665
- _block_descriptor.1670
- _block_descriptor.1675
- _block_descriptor.1680
- _block_descriptor.1685
- _block_descriptor.4716
- _block_descriptor.4728
- _block_descriptor.4740
- _block_descriptor.4752
- _block_descriptor.4758
- _block_descriptor.4770
- _block_descriptor.4836
- _block_descriptor.4852
- _block_descriptor.4859
- _block_descriptor.4904
- _block_descriptor.5011
- _block_descriptor.5014
- _block_descriptor.5062
- _block_descriptor.5128
- _block_descriptor.5131
- _block_descriptor.5200
- _block_descriptor.5203
- _block_descriptor.5212
- _block_descriptor.5224
- _block_descriptor.5230
- _block_descriptor.5242
- _block_descriptor.5254
- _block_descriptor.5266
- _block_descriptor.5272
- _block_descriptor.5284
- _block_descriptor.5311
- _block_descriptor.5314
- _block_descriptor.5401
- _block_descriptor.5433
- _block_descriptor.5436
- _block_descriptor.5446
- _block_descriptor.5449
- _block_descriptor.5455
- _block_descriptor.5469
- _block_descriptor.5475
- _block_descriptor.5487
- _block_descriptor.5498
- _block_descriptor.5510
- _block_descriptor.5519
- _block_descriptor.5530
- _block_descriptor.5536
- _block_descriptor.5548
- _block_descriptor.5643
- _block_descriptor.5646
- _block_descriptor.5785
- _block_descriptor.5788
- _block_descriptor.5828
- _block_descriptor.5831
- _block_descriptor.5857
- _block_descriptor.5867
- _block_descriptor.5896
- _block_descriptor.5899
- _block_descriptor.5910
- _block_descriptor.5962
- _block_descriptor.5965
- _block_descriptor.5971
- _block_descriptor.5974
- _block_descriptor.5991
- _block_descriptor.5998
- _block_descriptor.6016
- _block_descriptor.6028
- _block_descriptor.6046
- _block_descriptor.6058
- _block_descriptor.6076
- _block_descriptor.6086
- _block_descriptor.6118
- _block_descriptor.6121
- _block_descriptor.6130
- _block_descriptor.6164
- _block_descriptor.6167
- _block_descriptor.6185
- _block_descriptor.6192
- _block_destroy_helper.1329
- _block_destroy_helper.1336
- _block_destroy_helper.1340
- _block_destroy_helper.1344
- _block_destroy_helper.1357
- _block_destroy_helper.1364
- _block_destroy_helper.1384
- _block_destroy_helper.1394
- _block_destroy_helper.1404
- _block_destroy_helper.1415
- _block_destroy_helper.1519
- _block_destroy_helper.1581
- _block_destroy_helper.1584
- _block_destroy_helper.1587
- _block_destroy_helper.1594
- _block_destroy_helper.1645
- _block_destroy_helper.1648
- _block_destroy_helper.1651
- _block_destroy_helper.1654
- _block_destroy_helper.1659
- _block_destroy_helper.1664
- _block_destroy_helper.1669
- _block_destroy_helper.1674
- _block_destroy_helper.1679
- _block_destroy_helper.1684
- _block_destroy_helper.4715
- _block_destroy_helper.4727
- _block_destroy_helper.4739
- _block_destroy_helper.4751
- _block_destroy_helper.4757
- _block_destroy_helper.4769
- _block_destroy_helper.4835
- _block_destroy_helper.4851
- _block_destroy_helper.4858
- _block_destroy_helper.4903
- _block_destroy_helper.5010
- _block_destroy_helper.5013
- _block_destroy_helper.5061
- _block_destroy_helper.5127
- _block_destroy_helper.5130
- _block_destroy_helper.5199
- _block_destroy_helper.5202
- _block_destroy_helper.5211
- _block_destroy_helper.5223
- _block_destroy_helper.5229
- _block_destroy_helper.5241
- _block_destroy_helper.5253
- _block_destroy_helper.5265
- _block_destroy_helper.5271
- _block_destroy_helper.5283
- _block_destroy_helper.5310
- _block_destroy_helper.5313
- _block_destroy_helper.5400
- _block_destroy_helper.5432
- _block_destroy_helper.5435
- _block_destroy_helper.5445
- _block_destroy_helper.5448
- _block_destroy_helper.5454
- _block_destroy_helper.5468
- _block_destroy_helper.5474
- _block_destroy_helper.5486
- _block_destroy_helper.5497
- _block_destroy_helper.5509
- _block_destroy_helper.5518
- _block_destroy_helper.5529
- _block_destroy_helper.5535
- _block_destroy_helper.5547
- _block_destroy_helper.5642
- _block_destroy_helper.5645
- _block_destroy_helper.5784
- _block_destroy_helper.5787
- _block_destroy_helper.5827
- _block_destroy_helper.5830
- _block_destroy_helper.5856
- _block_destroy_helper.5866
- _block_destroy_helper.5895
- _block_destroy_helper.5898
- _block_destroy_helper.5909
- _block_destroy_helper.5961
- _block_destroy_helper.5964
- _block_destroy_helper.5970
- _block_destroy_helper.5973
- _block_destroy_helper.5990
- _block_destroy_helper.5997
- _block_destroy_helper.6015
- _block_destroy_helper.6027
- _block_destroy_helper.6045
- _block_destroy_helper.6057
- _block_destroy_helper.6075
- _block_destroy_helper.6085
- _block_destroy_helper.6117
- _block_destroy_helper.6120
- _block_destroy_helper.6129
- _block_destroy_helper.6163
- _block_destroy_helper.6166
- _block_destroy_helper.6184
- _block_destroy_helper.6191
- _keypath_get.12Tm
- _keypath_get.4Tm
- _keypath_get.8Tm
- _objc_msgSend$requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:
- _objectdestroy.1249Tm
- _objectdestroy.1428Tm
- _objectdestroy.1449Tm
- _objectdestroy.1525Tm
- _objectdestroy.1528Tm
- _objectdestroy.1623Tm
- _objectdestroy.175Tm
- _objectdestroy.185Tm
- _objectdestroy.198Tm
- _objectdestroy.228Tm
- _objectdestroy.356Tm
- _objectdestroy.4778Tm
- _objectdestroy.4986Tm
- _objectdestroy.5029Tm
- _objectdestroy.5648Tm
- _objectdestroy.5679Tm
- _objectdestroy.5734Tm
- _objectdestroy.5853Tm
- _symbolic ___________y2ID_____QzAcDQy_Gt 18FileProviderDaemon7JobCodeO AA16ReconciliationIDO AA0A4ItemP
CStrings:
+ "-[FPDXPCServicer _test_isDiskSpaceMonitorRunningForDomain:completionHandler:]"
+ "-[FPDXPCServicer _test_isDiskSpaceMonitorRunningForDomain:completionHandler:]_block_invoke"
+ "Disk space monitor not running for low disk domain"
+ "Domain was disconnected due to low disk space, but the disk space monitor wasn't triggered for the volume\n\ndomain: %@\nvolume: %@\n"
+ "SELECT id, scheduling_state, scheduling_state_continuation, reason\n  FROM "
+ "SQLDB: Check hierarchy size"
+ "Ti,R,N,V_partialReimportHierarchyLimit"
+ "[DEBUG] [diskspace] Found error %@, but low disk space monitor already running"
+ "[DEBUG] [diskspace] Low disk space monitor already running"
+ "[DEBUG] [diskspace] Skipping disk space monitor due to user defaults"
+ "[INFO] [diskspace] (%@) In low disk space: %lld bytes (< %lld)"
+ "[NOTICE] [diskspace] Disk space monitor reached max iterations (%lu), restarting fileproviderd"
+ "[NOTICE] [diskspace] Setting up to monitor low disk space recovery (delay %lu s, max iterations %lu)"
+ "[NOTICE] [diskspace] [%lu/%lu] Trying to recover from disconnect due to low disk space on timed check."
+ "_TtC18FileProviderDaemon21FPDynamicErrorDecider"
+ "_diskSpaceRecoveryTimerCurrentIteration"
+ "_isDiskSpaceMonitorRunning"
+ "_partialReimportHierarchyLimit"
+ "_test_isDiskSpaceMonitorRunningForDomain:completionHandler:"
+ "disconnecting a domain found an issue"
+ "disk-space-monitor-delay"
+ "disk-space-monitor-max-iterations"
+ "disk-space-monitor-skip"
+ "ignored item %{public}s materialization failed asynchronously: %@"
+ "init-deadend-backend"
+ "isDiskSpaceMonitorRunning"
+ "maxTimerIterations"
+ "partialReimportFallBackFullReimport"
+ "partialReimportHierarchyLimit"
+ "requestCompleted(isIgnored:db:error:)"
+ "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:skipSysdiagnose:"
+ "requestTapToRadarWithTitle:description:keywords:attachments:displayReason:providerID:skipSysdiagnose:"
+ "setAutoDiagnostics:"
+ "shouldSendFor:"
+ "shouldSkipDiskSpaceMonitor"
+ "timerDelay"
+ "v68@0:8@16@24@32@40@48@56B64"
+ "v92@0:8@16@24@32@40q48@56@64@72@80B88"
+ "\x81"
+ "🚚  hierarchy of %s is too big, falling back on reimporting the root item"
- "Mark reconciliation as needs delete because %s"
- "SELECT id, scheduling_state, scheduling_state_continuation\n  FROM "
- "[INFO] [diskspace] (%@) In low disk space: %lld bytes"
- "[NOTICE] [diskspace] Setting up to monitor low disk space recovery."
- "[NOTICE] [diskspace] Trying to recover from disconnect due to low disk space on timed check."
- "requestCompleted(isIgnored:db:)"
- "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:providerID:"
- "v88@0:8@16@24@32@40q48@56@64@72@80"

```
