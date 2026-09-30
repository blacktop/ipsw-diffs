## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-62460.2.3.0.0
-  __TEXT.__text: 0x17d01c
+62460.40.49.502.1
+  __TEXT.__text: 0x17d2b0
   __TEXT.__lazy_helpers: 0x54
   __TEXT.__objc_methlist: 0x67bc
-  __TEXT.__const: 0x1b9d0
+  __TEXT.__const: 0x1b9b8
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__cstring: 0x19482
-  __TEXT.__gcc_except_tab: 0x7d8c
-  __TEXT.__oslogstring: 0xf8d9
+  __TEXT.__cstring: 0x194d2
+  __TEXT.__gcc_except_tab: 0x7db4
+  __TEXT.__oslogstring: 0xf8f9
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1f2c
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x72d0
+  __TEXT.__unwind_info: 0x72e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15360
+  __DATA_CONST.__const: 0x15380
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x34c8
+  __DATA_CONST.__objc_selrefs: 0x34d0
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__got: 0x770
   __AUTH_CONST.__const: 0x3f80
-  __AUTH_CONST.__cfstring: 0x17800
+  __AUTH_CONST.__cfstring: 0x178c0
   __AUTH_CONST.__objc_const: 0xa5f8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7134
-  Symbols:   14858
-  CStrings:  5755
+  Functions: 7137
+  Symbols:   14866
+  CStrings:  5762
 
Symbols:
+ +[TPMIDStableTrustedDeviceID supportsSecureCoding]
+ -[TPMIDStableTrustedDeviceID .cxx_destruct]
+ -[TPMIDStableTrustedDeviceID compare:]
+ -[TPMIDStableTrustedDeviceID description]
+ -[TPMIDStableTrustedDeviceID encodeWithCoder:]
+ -[TPMIDStableTrustedDeviceID hash]
+ -[TPMIDStableTrustedDeviceID initWithCoder:]
+ -[TPMIDStableTrustedDeviceID initWithMachineID:stableID:]
+ -[TPMIDStableTrustedDeviceID isEqual:]
+ -[TPMIDStableTrustedDeviceID isEqualToMIDStableTrustedDeviceID:]
+ -[TPMIDStableTrustedDeviceID machineID]
+ -[TPMIDStableTrustedDeviceID stableID]
+ GCC_except_table2300
+ GCC_except_table4485
+ GCC_except_table4489
+ GCC_except_table4504
+ GCC_except_table4506
+ GCC_except_table4513
+ GCC_except_table4521
+ GCC_except_table4523
+ GCC_except_table4533
+ GCC_except_table4606
+ GCC_except_table4622
+ GCC_except_table4623
+ GCC_except_table4645
+ GCC_except_table4652
+ GCC_except_table4656
+ GCC_except_table4661
+ GCC_except_table4682
+ GCC_except_table4683
+ GCC_except_table4684
+ GCC_except_table4755
+ GCC_except_table4767
+ GCC_except_table4771
+ GCC_except_table4882
+ GCC_except_table5006
+ GCC_except_table5007
+ GCC_except_table5013
+ GCC_except_table5018
+ GCC_except_table5020
+ GCC_except_table5022
+ GCC_except_table5024
+ GCC_except_table5026
+ GCC_except_table5028
+ GCC_except_table5030
+ GCC_except_table5162
+ GCC_except_table5164
+ GCC_except_table5172
+ GCC_except_table5174
+ GCC_except_table5895
+ GCC_except_table5904
+ GCC_except_table5906
+ GCC_except_table5908
+ GCC_except_table5910
+ GCC_except_table6037
+ GCC_except_table6045
+ GCC_except_table6051
+ GCC_except_table6064
+ GCC_except_table6069
+ GCC_except_table6071
+ GCC_except_table6082
+ GCC_except_table6083
+ GCC_except_table6089
+ GCC_except_table6091
+ GCC_except_table6097
+ GCC_except_table6098
+ GCC_except_table6099
+ GCC_except_table6103
+ GCC_except_table6104
+ GCC_except_table6108
+ GCC_except_table6109
+ GCC_except_table6122
+ GCC_except_table6124
+ GCC_except_table6147
+ GCC_except_table6152
+ GCC_except_table6153
+ GCC_except_table6154
+ GCC_except_table6168
+ GCC_except_table6169
+ GCC_except_table6170
+ GCC_except_table6185
+ GCC_except_table6191
+ GCC_except_table6192
+ GCC_except_table6193
+ GCC_except_table6207
+ GCC_except_table6215
+ GCC_except_table6220
+ GCC_except_table6225
+ GCC_except_table6226
+ GCC_except_table6227
+ GCC_except_table6232
+ GCC_except_table6246
+ GCC_except_table6273
+ GCC_except_table6278
+ GCC_except_table6282
+ GCC_except_table6289
+ GCC_except_table6291
+ GCC_except_table6295
+ GCC_except_table6304
+ GCC_except_table6309
+ GCC_except_table6310
+ GCC_except_table6311
+ GCC_except_table6316
+ GCC_except_table6318
+ GCC_except_table6320
+ GCC_except_table6327
+ GCC_except_table6329
+ GCC_except_table6334
+ GCC_except_table6335
+ GCC_except_table6336
+ GCC_except_table6340
+ GCC_except_table6341
+ GCC_except_table6349
+ GCC_except_table6350
+ GCC_except_table6354
+ GCC_except_table6359
+ GCC_except_table6367
+ GCC_except_table6371
+ GCC_except_table6385
+ GCC_except_table6386
+ GCC_except_table6391
+ GCC_except_table6392
+ GCC_except_table6393
+ GCC_except_table6401
+ GCC_except_table6402
+ GCC_except_table6409
+ GCC_except_table6417
+ GCC_except_table6421
+ GCC_except_table6422
+ GCC_except_table6432
+ GCC_except_table6433
+ GCC_except_table6437
+ GCC_except_table6441
+ GCC_except_table6442
+ GCC_except_table6448
+ GCC_except_table6452
+ GCC_except_table6454
+ GCC_except_table6458
+ GCC_except_table6463
+ GCC_except_table6485
+ GCC_except_table6489
+ GCC_except_table6491
+ GCC_except_table6496
+ GCC_except_table6519
+ GCC_except_table6524
+ GCC_except_table6526
+ GCC_except_table6533
+ GCC_except_table6534
+ GCC_except_table6554
+ GCC_except_table6575
+ GCC_except_table6580
+ GCC_except_table6589
+ GCC_except_table6590
+ GCC_except_table6591
+ GCC_except_table6608
+ GCC_except_table6610
+ GCC_except_table6623
+ GCC_except_table6627
+ GCC_except_table6631
+ GCC_except_table6632
+ GCC_except_table6636
+ GCC_except_table6637
+ GCC_except_table6638
+ GCC_except_table6645
+ GCC_except_table6646
+ GCC_except_table6654
+ GCC_except_table6661
+ GCC_except_table6662
+ GCC_except_table6663
+ GCC_except_table6672
+ GCC_except_table6673
+ GCC_except_table6680
+ GCC_except_table6694
+ GCC_except_table6696
+ GCC_except_table6698
+ GCC_except_table6700
+ GCC_except_table6712
+ GCC_except_table6716
+ GCC_except_table6720
+ GCC_except_table6721
+ GCC_except_table6729
+ GCC_except_table6733
+ GCC_except_table6739
+ GCC_except_table6741
+ GCC_except_table6751
+ GCC_except_table6759
+ GCC_except_table6760
+ GCC_except_table6761
+ GCC_except_table6765
+ GCC_except_table6766
+ GCC_except_table6770
+ GCC_except_table6779
+ GCC_except_table6783
+ GCC_except_table6788
+ GCC_except_table6790
+ GCC_except_table6797
+ GCC_except_table6798
+ GCC_except_table6799
+ GCC_except_table6803
+ GCC_except_table6808
+ GCC_except_table6810
+ GCC_except_table6819
+ GCC_except_table6820
+ GCC_except_table6821
+ GCC_except_table6825
+ GCC_except_table6829
+ GCC_except_table6843
+ GCC_except_table6844
+ GCC_except_table6849
+ GCC_except_table6851
+ GCC_except_table6853
+ GCC_except_table6865
+ GCC_except_table6870
+ GCC_except_table6872
+ GCC_except_table6879
+ GCC_except_table6881
+ GCC_except_table6889
+ GCC_except_table6893
+ GCC_except_table6898
+ GCC_except_table6904
+ GCC_except_table6912
+ GCC_except_table6913
+ GCC_except_table6917
+ GCC_except_table6918
+ GCC_except_table6922
+ GCC_except_table6928
+ GCC_except_table6933
+ GCC_except_table6941
+ GCC_except_table6942
+ GCC_except_table6955
+ GCC_except_table6959
+ GCC_except_table6960
+ GCC_except_table6971
+ GCC_except_table6972
+ GCC_except_table6987
+ GCC_except_table6988
+ GCC_except_table6993
+ _OBJC_CLASS_$_TPMIDStableTrustedDeviceID
+ _OBJC_IVAR_$_TPMIDStableTrustedDeviceID._machineID
+ _OBJC_IVAR_$_TPMIDStableTrustedDeviceID._stableID
+ _OBJC_METACLASS_$_TPMIDStableTrustedDeviceID
+ _SecItemCountAllWithAccessGroups
+ __OBJC_$_CLASS_METHODS_TPMIDStableTrustedDeviceID
+ __OBJC_$_CLASS_PROP_LIST_TPMIDStableTrustedDeviceID
+ __OBJC_$_INSTANCE_METHODS_TPMIDStableTrustedDeviceID
+ __OBJC_$_INSTANCE_VARIABLES_TPMIDStableTrustedDeviceID
+ __OBJC_$_PROP_LIST_TPMIDStableTrustedDeviceID
+ __OBJC_CLASS_PROTOCOLS_$_TPMIDStableTrustedDeviceID
+ __OBJC_CLASS_RO_$_TPMIDStableTrustedDeviceID
+ __OBJC_METACLASS_RO_$_TPMIDStableTrustedDeviceID
+ ___count_all_with_access_groups_request_block_invoke
+ ___count_all_with_access_groups_request_block_invoke_2
+ ___getMetricSessionInfoClass_block_invoke
+ _getMetricSessionInfoClass
+ _getMetricSessionInfoClass.softClass
+ _kSecItemCountNonSyncableLive
+ _kSecItemCountNonSyncableTombstone
+ _kSecItemCountSyncableLive
+ _kSecItemCountSyncableTombstone
+ _objc_msgSend$initWithSession:eventName:
+ _objc_msgSend$isEqualToMIDStableTrustedDeviceID:
+ _objc_msgSend$sessionInfoWithAltDSID:flowID:deviceSessionID:
- +[TPMIDStableTrustedDeviceIDPair supportsSecureCoding]
- -[TPMIDStableTrustedDeviceIDPair .cxx_destruct]
- -[TPMIDStableTrustedDeviceIDPair compare:]
- -[TPMIDStableTrustedDeviceIDPair description]
- -[TPMIDStableTrustedDeviceIDPair encodeWithCoder:]
- -[TPMIDStableTrustedDeviceIDPair hash]
- -[TPMIDStableTrustedDeviceIDPair initWithCoder:]
- -[TPMIDStableTrustedDeviceIDPair initWithMachineID:stableID:]
- -[TPMIDStableTrustedDeviceIDPair isEqual:]
- -[TPMIDStableTrustedDeviceIDPair isEqualToMIDStableTrustedDeviceIDPair:]
- -[TPMIDStableTrustedDeviceIDPair machineID]
- -[TPMIDStableTrustedDeviceIDPair stableID]
- GCC_except_table2302
- GCC_except_table4486
- GCC_except_table4495
- GCC_except_table4503
- GCC_except_table4507
- GCC_except_table4515
- GCC_except_table4520
- GCC_except_table4524
- GCC_except_table4603
- GCC_except_table4616
- GCC_except_table4620
- GCC_except_table4642
- GCC_except_table4646
- GCC_except_table4653
- GCC_except_table4658
- GCC_except_table4674
- GCC_except_table4675
- GCC_except_table4676
- GCC_except_table4752
- GCC_except_table4764
- GCC_except_table4768
- GCC_except_table4879
- GCC_except_table5003
- GCC_except_table5004
- GCC_except_table5010
- GCC_except_table5015
- GCC_except_table5017
- GCC_except_table5019
- GCC_except_table5021
- GCC_except_table5023
- GCC_except_table5025
- GCC_except_table5027
- GCC_except_table5156
- GCC_except_table5161
- GCC_except_table5163
- GCC_except_table5171
- GCC_except_table5892
- GCC_except_table5901
- GCC_except_table5903
- GCC_except_table5905
- GCC_except_table5907
- GCC_except_table6034
- GCC_except_table6042
- GCC_except_table6048
- GCC_except_table6061
- GCC_except_table6063
- GCC_except_table6068
- GCC_except_table6077
- GCC_except_table6079
- GCC_except_table6086
- GCC_except_table6088
- GCC_except_table6092
- GCC_except_table6093
- GCC_except_table6094
- GCC_except_table6100
- GCC_except_table6101
- GCC_except_table6105
- GCC_except_table6106
- GCC_except_table6119
- GCC_except_table6121
- GCC_except_table6143
- GCC_except_table6144
- GCC_except_table6145
- GCC_except_table6150
- GCC_except_table6165
- GCC_except_table6166
- GCC_except_table6167
- GCC_except_table6179
- GCC_except_table6184
- GCC_except_table6186
- GCC_except_table6188
- GCC_except_table6204
- GCC_except_table6211
- GCC_except_table6212
- GCC_except_table6219
- GCC_except_table6223
- GCC_except_table6224
- GCC_except_table6229
- GCC_except_table6237
- GCC_except_table6270
- GCC_except_table6275
- GCC_except_table6279
- GCC_except_table6286
- GCC_except_table6288
- GCC_except_table6292
- GCC_except_table6299
- GCC_except_table6300
- GCC_except_table6301
- GCC_except_table6307
- GCC_except_table6312
- GCC_except_table6313
- GCC_except_table6314
- GCC_except_table6322
- GCC_except_table6323
- GCC_except_table6324
- GCC_except_table6332
- GCC_except_table6333
- GCC_except_table6337
- GCC_except_table6338
- GCC_except_table6344
- GCC_except_table6345
- GCC_except_table6346
- GCC_except_table6356
- GCC_except_table6364
- GCC_except_table6365
- GCC_except_table6379
- GCC_except_table6383
- GCC_except_table6388
- GCC_except_table6389
- GCC_except_table6390
- GCC_except_table6398
- GCC_except_table6399
- GCC_except_table6406
- GCC_except_table6413
- GCC_except_table6414
- GCC_except_table6415
- GCC_except_table6426
- GCC_except_table6430
- GCC_except_table6431
- GCC_except_table6438
- GCC_except_table6439
- GCC_except_table6440
- GCC_except_table6445
- GCC_except_table6451
- GCC_except_table6455
- GCC_except_table6460
- GCC_except_table6481
- GCC_except_table6482
- GCC_except_table6483
- GCC_except_table6488
- GCC_except_table6492
- GCC_except_table6494
- GCC_except_table6499
- GCC_except_table6530
- GCC_except_table6531
- GCC_except_table6551
- GCC_except_table6565
- GCC_except_table6566
- GCC_except_table6570
- GCC_except_table6578
- GCC_except_table6583
- GCC_except_table6602
- GCC_except_table6607
- GCC_except_table6611
- GCC_except_table6624
- GCC_except_table6625
- GCC_except_table6629
- GCC_except_table6633
- GCC_except_table6634
- GCC_except_table6635
- GCC_except_table6639
- GCC_except_table6643
- GCC_except_table6651
- GCC_except_table6658
- GCC_except_table6659
- GCC_except_table6660
- GCC_except_table6667
- GCC_except_table6669
- GCC_except_table6677
- GCC_except_table6682
- GCC_except_table6693
- GCC_except_table6695
- GCC_except_table6697
- GCC_except_table6703
- GCC_except_table6710
- GCC_except_table6714
- GCC_except_table6715
- GCC_except_table6726
- GCC_except_table6727
- GCC_except_table6732
- GCC_except_table6734
- GCC_except_table6736
- GCC_except_table6745
- GCC_except_table6754
- GCC_except_table6756
- GCC_except_table6762
- GCC_except_table6763
- GCC_except_table6767
- GCC_except_table6772
- GCC_except_table6776
- GCC_except_table6777
- GCC_except_table6785
- GCC_except_table6792
- GCC_except_table6794
- GCC_except_table6796
- GCC_except_table6800
- GCC_except_table6805
- GCC_except_table6807
- GCC_except_table6813
- GCC_except_table6815
- GCC_except_table6817
- GCC_except_table6822
- GCC_except_table6826
- GCC_except_table6840
- GCC_except_table6841
- GCC_except_table6842
- GCC_except_table6846
- GCC_except_table6847
- GCC_except_table6862
- GCC_except_table6867
- GCC_except_table6869
- GCC_except_table6873
- GCC_except_table6878
- GCC_except_table6880
- GCC_except_table6890
- GCC_except_table6891
- GCC_except_table6892
- GCC_except_table6896
- GCC_except_table6901
- GCC_except_table6907
- GCC_except_table6915
- GCC_except_table6919
- GCC_except_table6925
- GCC_except_table6930
- GCC_except_table6934
- GCC_except_table6935
- GCC_except_table6939
- GCC_except_table6944
- GCC_except_table6951
- GCC_except_table6962
- GCC_except_table6969
- GCC_except_table6984
- GCC_except_table6985
- GCC_except_table6990
- _OBJC_CLASS_$_TPMIDStableTrustedDeviceIDPair
- _OBJC_IVAR_$_TPMIDStableTrustedDeviceIDPair._machineID
- _OBJC_IVAR_$_TPMIDStableTrustedDeviceIDPair._stableID
- _OBJC_METACLASS_$_TPMIDStableTrustedDeviceIDPair
- __OBJC_$_CLASS_METHODS_TPMIDStableTrustedDeviceIDPair
- __OBJC_$_CLASS_PROP_LIST_TPMIDStableTrustedDeviceIDPair
- __OBJC_$_INSTANCE_METHODS_TPMIDStableTrustedDeviceIDPair
- __OBJC_$_INSTANCE_VARIABLES_TPMIDStableTrustedDeviceIDPair
- __OBJC_$_PROP_LIST_TPMIDStableTrustedDeviceIDPair
- __OBJC_CLASS_PROTOCOLS_$_TPMIDStableTrustedDeviceIDPair
- __OBJC_CLASS_RO_$_TPMIDStableTrustedDeviceIDPair
- __OBJC_METACLASS_RO_$_TPMIDStableTrustedDeviceIDPair
- ___getkSecurityRTCEventCategoryAccountDataAccessRecoverySymbolLoc_block_invoke
- _getkSecurityRTCEventCategoryAccountDataAccessRecovery
- _getkSecurityRTCEventCategoryAccountDataAccessRecoverySymbolLoc.ptr
- _objc_msgSend$initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:
- _objc_msgSend$isEqualToMIDStableTrustedDeviceIDPair:
- _objc_msgSend$testsEnabled
CStrings:
+ "1.2.840.113635.100.4.1.2"
+ "<MIDStableTrustedDeviceID: machineID=%@, stableID=%@>"
+ "Class getMetricSessionInfoClass(void)_block_invoke"
+ "MetricSessionInfo"
+ "SecItemCountAllWithAccessGroups"
+ "accessGroups must not be NULL"
+ "nonSyncableLive"
+ "nonSyncableTombstone"
+ "syncableLive"
+ "syncableTombstone"
- "<MIDStableIDPair: machineID=%@, stableID=%@>"
- "NSNumber *getkSecurityRTCEventCategoryAccountDataAccessRecovery(void)"
- "kSecurityRTCEventCategoryAccountDataAccessRecovery"
```
