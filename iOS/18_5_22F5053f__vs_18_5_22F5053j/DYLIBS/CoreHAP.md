## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1278.6.26.0.0
-  __TEXT.__text: 0x1a46cc
+1278.6.30.0.0
+  __TEXT.__text: 0x1a50c8
   __TEXT.__auth_stubs: 0x1590
-  __TEXT.__objc_methlist: 0x13700
+  __TEXT.__objc_methlist: 0x13740
   __TEXT.__const: 0x6f0
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0x622c
-  __TEXT.__cstring: 0x108a9
-  __TEXT.__oslogstring: 0x1fb23
-  __TEXT.__unwind_info: 0x5c38
+  __TEXT.__gcc_except_tab: 0x6238
+  __TEXT.__cstring: 0x10937
+  __TEXT.__oslogstring: 0x1fc02
+  __TEXT.__unwind_info: 0x5c48
   __TEXT.__objc_classname: 0x2ddd
-  __TEXT.__objc_methname: 0x2644c
-  __TEXT.__objc_methtype: 0x8f36
-  __TEXT.__objc_stubs: 0x18480
+  __TEXT.__objc_methname: 0x2655f
+  __TEXT.__objc_methtype: 0x8f76
+  __TEXT.__objc_stubs: 0x18500
   __DATA_CONST.__got: 0xa68
   __DATA_CONST.__const: 0x4ff0
   __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e70
+  __DATA_CONST.__objc_selrefs: 0x6e90
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x7e0
   __DATA_CONST.__objc_arraydata: 0x208
   __AUTH_CONST.__auth_got: 0xad8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0xd9a0
-  __AUTH_CONST.__objc_const: 0x21e70
+  __AUTH_CONST.__cfstring: 0xda20
+  __AUTH_CONST.__objc_const: 0x21f20
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x4e70
-  __DATA.__objc_ivar: 0x14c8
+  __DATA.__objc_ivar: 0x14d8
   __DATA.__data: 0x266a
   __DATA.__bss: 0x4a9
   __DATA_DIRTY.__objc_data: 0xf50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7452
-  Symbols:   24212
-  CStrings:  11129
+  Functions: 7458
+  Symbols:   24232
+  CStrings:  11146
 
Symbols:
+ +[HAP2AccessoryServerTransportCoAP stringFromCoAPAddress:]
+ -[HAP2AccessorySessionInfo .cxx_destruct]
+ -[HAP2AccessorySessionInfo description]
+ -[HAP2AccessorySessionInfo initWithNumIPs:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:]
+ -[HAP2AccessorySessionInfo ipAddress]
+ -[HAP2AccessorySessionInfo resetWithNumIPs:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:]
+ -[HAP2AccessorySessionInfo resolveAttempted]
+ -[HAP2AccessorySessionInfo serviceName]
+ -[HAPAccessoryServerHAP2Adapter setSessionInfoWithNumIPsResolved:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:]
+ GCC_except_table4382
+ GCC_except_table4462
+ GCC_except_table4470
+ GCC_except_table4480
+ GCC_except_table4520
+ GCC_except_table4521
+ GCC_except_table4522
+ GCC_except_table4523
+ GCC_except_table4620
+ GCC_except_table4621
+ GCC_except_table4622
+ GCC_except_table4623
+ GCC_except_table4624
+ GCC_except_table4630
+ GCC_except_table4631
+ GCC_except_table4633
+ GCC_except_table4643
+ GCC_except_table4650
+ GCC_except_table4653
+ GCC_except_table4656
+ GCC_except_table4660
+ GCC_except_table4664
+ GCC_except_table4693
+ GCC_except_table4694
+ GCC_except_table4713
+ GCC_except_table4723
+ GCC_except_table4731
+ GCC_except_table4734
+ GCC_except_table4996
+ GCC_except_table5000
+ GCC_except_table5034
+ GCC_except_table5038
+ GCC_except_table5040
+ GCC_except_table5042
+ GCC_except_table5199
+ GCC_except_table5209
+ GCC_except_table5210
+ GCC_except_table5211
+ GCC_except_table5212
+ GCC_except_table5218
+ GCC_except_table5252
+ GCC_except_table5253
+ GCC_except_table5254
+ GCC_except_table5274
+ GCC_except_table5286
+ GCC_except_table5294
+ GCC_except_table5296
+ GCC_except_table5310
+ GCC_except_table5512
+ GCC_except_table5529
+ GCC_except_table5532
+ GCC_except_table5535
+ GCC_except_table5536
+ GCC_except_table5538
+ GCC_except_table5568
+ GCC_except_table5590
+ GCC_except_table5594
+ GCC_except_table5603
+ GCC_except_table5607
+ GCC_except_table5611
+ GCC_except_table5615
+ GCC_except_table5619
+ GCC_except_table5627
+ GCC_except_table5629
+ GCC_except_table5631
+ GCC_except_table5691
+ GCC_except_table5692
+ GCC_except_table5693
+ GCC_except_table5694
+ GCC_except_table5752
+ GCC_except_table5753
+ GCC_except_table5767
+ GCC_except_table5773
+ GCC_except_table5786
+ GCC_except_table5789
+ GCC_except_table5795
+ GCC_except_table5798
+ GCC_except_table5805
+ GCC_except_table5808
+ GCC_except_table5822
+ GCC_except_table5829
+ GCC_except_table5835
+ GCC_except_table5844
+ GCC_except_table5850
+ GCC_except_table5851
+ GCC_except_table5866
+ GCC_except_table5868
+ GCC_except_table5876
+ GCC_except_table5891
+ GCC_except_table5901
+ GCC_except_table5902
+ GCC_except_table5905
+ GCC_except_table5911
+ GCC_except_table5915
+ GCC_except_table5917
+ GCC_except_table5919
+ GCC_except_table5923
+ GCC_except_table6068
+ GCC_except_table6124
+ GCC_except_table6127
+ GCC_except_table6131
+ GCC_except_table6137
+ GCC_except_table6144
+ GCC_except_table6145
+ GCC_except_table6165
+ GCC_except_table6166
+ GCC_except_table6167
+ GCC_except_table6215
+ GCC_except_table6218
+ GCC_except_table6221
+ GCC_except_table6249
+ GCC_except_table6255
+ GCC_except_table6275
+ GCC_except_table6292
+ GCC_except_table6293
+ GCC_except_table6294
+ GCC_except_table6307
+ GCC_except_table6308
+ GCC_except_table6309
+ GCC_except_table6323
+ GCC_except_table6326
+ GCC_except_table6332
+ GCC_except_table6338
+ GCC_except_table6350
+ GCC_except_table6356
+ GCC_except_table6365
+ GCC_except_table6372
+ GCC_except_table6376
+ GCC_except_table6384
+ GCC_except_table6388
+ GCC_except_table6390
+ GCC_except_table6394
+ GCC_except_table6415
+ GCC_except_table6417
+ GCC_except_table6418
+ GCC_except_table6444
+ GCC_except_table6608
+ GCC_except_table6671
+ GCC_except_table6703
+ GCC_except_table6706
+ GCC_except_table6870
+ GCC_except_table6933
+ GCC_except_table7003
+ GCC_except_table7064
+ GCC_except_table7066
+ GCC_except_table7068
+ GCC_except_table7071
+ GCC_except_table7073
+ GCC_except_table7075
+ GCC_except_table7078
+ GCC_except_table7104
+ GCC_except_table7107
+ GCC_except_table7108
+ GCC_except_table7147
+ GCC_except_table7151
+ GCC_except_table7154
+ GCC_except_table7156
+ GCC_except_table7158
+ GCC_except_table7161
+ GCC_except_table7165
+ GCC_except_table7166
+ GCC_except_table7170
+ GCC_except_table7218
+ GCC_except_table7225
+ GCC_except_table7319
+ GCC_except_table7335
+ GCC_except_table7337
+ GCC_except_table7339
+ GCC_except_table7344
+ GCC_except_table7346
+ GCC_except_table7348
+ GCC_except_table7351
+ GCC_except_table7355
+ GCC_except_table7360
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._resolveAttempted
+ _OBJC_IVAR_$_HAP2AccessorySessionInfo._ipAddress
+ _OBJC_IVAR_$_HAP2AccessorySessionInfo._resolveAttempted
+ _OBJC_IVAR_$_HAP2AccessorySessionInfo._serviceName
+ __CopyPairingIdentityDelegateCallback_f.14973
+ __CopyPairingIdentityDelegateCallback_f.21540
+ __CopyPairingIdentityDelegateCallback_f.2710
+ __FindPairedPeerDelegateCallback_f.2709
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.406
+ __PairSetupPromptForSetupCodeDelegateCallback_f.21542
+ __SavePairedPeerDelegateCallback_f.14972
+ __SavePairedPeerDelegateCallback_f.21535
+ ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.78
+ ___54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.265
+ ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.83
+ ___59-[HAP2AccessoryServer(Paired) updateAccessoriesWithReason:]_block_invoke.93
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.281
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke_2.285
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.252
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.253
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.254
+ ___Block_byref_object_copy_.10487
+ ___Block_byref_object_copy_.10767
+ ___Block_byref_object_copy_.11590
+ ___Block_byref_object_copy_.11787
+ ___Block_byref_object_copy_.12851
+ ___Block_byref_object_copy_.13647
+ ___Block_byref_object_copy_.13875
+ ___Block_byref_object_copy_.14884
+ ___Block_byref_object_copy_.16874
+ ___Block_byref_object_copy_.17086
+ ___Block_byref_object_copy_.18073
+ ___Block_byref_object_copy_.18675
+ ___Block_byref_object_copy_.19762
+ ___Block_byref_object_copy_.1992
+ ___Block_byref_object_copy_.20568
+ ___Block_byref_object_copy_.24691
+ ___Block_byref_object_copy_.24856
+ ___Block_byref_object_copy_.2658
+ ___Block_byref_object_copy_.4214
+ ___Block_byref_object_copy_.5078
+ ___Block_byref_object_copy_.5338
+ ___Block_byref_object_copy_.5791
+ ___Block_byref_object_copy_.6435
+ ___Block_byref_object_copy_.6614
+ ___Block_byref_object_copy_.7409
+ ___Block_byref_object_copy_.8936
+ ___Block_byref_object_copy_.9251
+ ___Block_byref_object_copy_.9446
+ ___Block_byref_object_dispose_.10488
+ ___Block_byref_object_dispose_.10768
+ ___Block_byref_object_dispose_.11591
+ ___Block_byref_object_dispose_.11788
+ ___Block_byref_object_dispose_.12852
+ ___Block_byref_object_dispose_.13648
+ ___Block_byref_object_dispose_.13876
+ ___Block_byref_object_dispose_.14885
+ ___Block_byref_object_dispose_.16875
+ ___Block_byref_object_dispose_.17087
+ ___Block_byref_object_dispose_.18074
+ ___Block_byref_object_dispose_.18676
+ ___Block_byref_object_dispose_.19763
+ ___Block_byref_object_dispose_.1993
+ ___Block_byref_object_dispose_.20569
+ ___Block_byref_object_dispose_.24692
+ ___Block_byref_object_dispose_.24857
+ ___Block_byref_object_dispose_.2659
+ ___Block_byref_object_dispose_.4215
+ ___Block_byref_object_dispose_.5079
+ ___Block_byref_object_dispose_.5339
+ ___Block_byref_object_dispose_.5792
+ ___Block_byref_object_dispose_.6436
+ ___Block_byref_object_dispose_.6615
+ ___Block_byref_object_dispose_.7410
+ ___Block_byref_object_dispose_.8937
+ ___Block_byref_object_dispose_.9252
+ ___Block_byref_object_dispose_.9447
+ ___block_literal_global.10159
+ ___block_literal_global.10822
+ ___block_literal_global.11586
+ ___block_literal_global.11958
+ ___block_literal_global.13126
+ ___block_literal_global.14989
+ ___block_literal_global.15413
+ ___block_literal_global.16609
+ ___block_literal_global.16883
+ ___block_literal_global.18255
+ ___block_literal_global.1897
+ ___block_literal_global.19509
+ ___block_literal_global.19786
+ ___block_literal_global.20234
+ ___block_literal_global.21192
+ ___block_literal_global.22530
+ ___block_literal_global.22864
+ ___block_literal_global.24464
+ ___block_literal_global.25078
+ ___block_literal_global.2725
+ ___block_literal_global.3669
+ ___block_literal_global.5161
+ ___block_literal_global.5334
+ ___block_literal_global.5894
+ ___block_literal_global.6446
+ ___block_literal_global.6591
+ ___block_literal_global.7663
+ ___block_literal_global.769
+ ___block_literal_global.8563
+ ___block_literal_global.9020
+ ___block_literal_global.9555
+ _hkConfig.21176
+ _objc_msgSend$initWithNumIPs:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:
+ _objc_msgSend$ipAddress
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$resetWithNumIPs:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:
+ _objc_msgSend$resolveAttempted
+ _objc_msgSend$serviceName
+ _objc_msgSend$setSessionInfoWithNumIPsResolved:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:
+ _sharedInstance.onceToken.15412
- -[HAP2AccessorySessionInfo initWithNumIPs:numIPsTried:numBonjourNames:]
- -[HAP2AccessorySessionInfo resetWithNumIPs:numIPsTried:numBonjourNames:]
- -[HAPAccessoryServerHAP2Adapter setSessionInfoWithNumIPsResolved:numIPsTried:numBonjourNames:]
- GCC_except_table4377
- GCC_except_table4457
- GCC_except_table4465
- GCC_except_table4475
- GCC_except_table4512
- GCC_except_table4515
- GCC_except_table4516
- GCC_except_table4518
- GCC_except_table4614
- GCC_except_table4615
- GCC_except_table4616
- GCC_except_table4617
- GCC_except_table4618
- GCC_except_table4625
- GCC_except_table4626
- GCC_except_table4628
- GCC_except_table4635
- GCC_except_table4638
- GCC_except_table4648
- GCC_except_table4651
- GCC_except_table4655
- GCC_except_table4659
- GCC_except_table4688
- GCC_except_table4689
- GCC_except_table4708
- GCC_except_table4718
- GCC_except_table4721
- GCC_except_table4729
- GCC_except_table4991
- GCC_except_table4995
- GCC_except_table5029
- GCC_except_table5033
- GCC_except_table5035
- GCC_except_table5037
- GCC_except_table5194
- GCC_except_table5200
- GCC_except_table5204
- GCC_except_table5206
- GCC_except_table5207
- GCC_except_table5213
- GCC_except_table5247
- GCC_except_table5248
- GCC_except_table5249
- GCC_except_table5269
- GCC_except_table5281
- GCC_except_table5284
- GCC_except_table5291
- GCC_except_table5305
- GCC_except_table5507
- GCC_except_table5519
- GCC_except_table5527
- GCC_except_table5528
- GCC_except_table5530
- GCC_except_table5531
- GCC_except_table5563
- GCC_except_table5585
- GCC_except_table5589
- GCC_except_table5593
- GCC_except_table5602
- GCC_except_table5606
- GCC_except_table5610
- GCC_except_table5614
- GCC_except_table5622
- GCC_except_table5624
- GCC_except_table5626
- GCC_except_table5686
- GCC_except_table5687
- GCC_except_table5688
- GCC_except_table5689
- GCC_except_table5747
- GCC_except_table5748
- GCC_except_table5762
- GCC_except_table5768
- GCC_except_table5781
- GCC_except_table5784
- GCC_except_table5785
- GCC_except_table5793
- GCC_except_table5800
- GCC_except_table5803
- GCC_except_table5817
- GCC_except_table5824
- GCC_except_table5830
- GCC_except_table5839
- GCC_except_table5841
- GCC_except_table5845
- GCC_except_table5861
- GCC_except_table5863
- GCC_except_table5871
- GCC_except_table5886
- GCC_except_table5887
- GCC_except_table5896
- GCC_except_table5900
- GCC_except_table5906
- GCC_except_table5910
- GCC_except_table5912
- GCC_except_table5914
- GCC_except_table5918
- GCC_except_table6063
- GCC_except_table6119
- GCC_except_table6122
- GCC_except_table6126
- GCC_except_table6132
- GCC_except_table6139
- GCC_except_table6140
- GCC_except_table6156
- GCC_except_table6160
- GCC_except_table6162
- GCC_except_table6210
- GCC_except_table6211
- GCC_except_table6213
- GCC_except_table6244
- GCC_except_table6245
- GCC_except_table6270
- GCC_except_table6287
- GCC_except_table6288
- GCC_except_table6289
- GCC_except_table6297
- GCC_except_table6303
- GCC_except_table6304
- GCC_except_table6318
- GCC_except_table6321
- GCC_except_table6327
- GCC_except_table6333
- GCC_except_table6345
- GCC_except_table6346
- GCC_except_table6360
- GCC_except_table6366
- GCC_except_table6367
- GCC_except_table6379
- GCC_except_table6383
- GCC_except_table6385
- GCC_except_table6389
- GCC_except_table6410
- GCC_except_table6412
- GCC_except_table6413
- GCC_except_table6439
- GCC_except_table6603
- GCC_except_table6666
- GCC_except_table6698
- GCC_except_table6701
- GCC_except_table6865
- GCC_except_table6928
- GCC_except_table6991
- GCC_except_table7042
- GCC_except_table7044
- GCC_except_table7046
- GCC_except_table7065
- GCC_except_table7067
- GCC_except_table7069
- GCC_except_table7072
- GCC_except_table7098
- GCC_except_table7101
- GCC_except_table7102
- GCC_except_table7141
- GCC_except_table7142
- GCC_except_table7143
- GCC_except_table7145
- GCC_except_table7146
- GCC_except_table7150
- GCC_except_table7153
- GCC_except_table7160
- GCC_except_table7164
- GCC_except_table7212
- GCC_except_table7219
- GCC_except_table7313
- GCC_except_table7329
- GCC_except_table7331
- GCC_except_table7333
- GCC_except_table7336
- GCC_except_table7338
- GCC_except_table7340
- GCC_except_table7343
- GCC_except_table7345
- GCC_except_table7354
- __CopyPairingIdentityDelegateCallback_f.14939
- __CopyPairingIdentityDelegateCallback_f.21499
- __CopyPairingIdentityDelegateCallback_f.2713
- __FindPairedPeerDelegateCallback_f.2712
- __OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.405
- __PairSetupPromptForSetupCodeDelegateCallback_f.21501
- __SavePairedPeerDelegateCallback_f.14938
- __SavePairedPeerDelegateCallback_f.21494
- ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.76
- ___54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.264
- ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.81
- ___59-[HAP2AccessoryServer(Paired) updateAccessoriesWithReason:]_block_invoke.92
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.279
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke_2.284
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.251
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.252
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.253
- ___Block_byref_object_copy_.10486
- ___Block_byref_object_copy_.10768
- ___Block_byref_object_copy_.11588
- ___Block_byref_object_copy_.11785
- ___Block_byref_object_copy_.12818
- ___Block_byref_object_copy_.13614
- ___Block_byref_object_copy_.13842
- ___Block_byref_object_copy_.14850
- ___Block_byref_object_copy_.16829
- ___Block_byref_object_copy_.17041
- ___Block_byref_object_copy_.18029
- ___Block_byref_object_copy_.18634
- ___Block_byref_object_copy_.19721
- ___Block_byref_object_copy_.1995
- ___Block_byref_object_copy_.20527
- ___Block_byref_object_copy_.24636
- ___Block_byref_object_copy_.24802
- ___Block_byref_object_copy_.2661
- ___Block_byref_object_copy_.4217
- ___Block_byref_object_copy_.5081
- ___Block_byref_object_copy_.5341
- ___Block_byref_object_copy_.5794
- ___Block_byref_object_copy_.6438
- ___Block_byref_object_copy_.6617
- ___Block_byref_object_copy_.7410
- ___Block_byref_object_copy_.8937
- ___Block_byref_object_copy_.9250
- ___Block_byref_object_copy_.9445
- ___Block_byref_object_dispose_.10487
- ___Block_byref_object_dispose_.10769
- ___Block_byref_object_dispose_.11589
- ___Block_byref_object_dispose_.11786
- ___Block_byref_object_dispose_.12819
- ___Block_byref_object_dispose_.13615
- ___Block_byref_object_dispose_.13843
- ___Block_byref_object_dispose_.14851
- ___Block_byref_object_dispose_.16830
- ___Block_byref_object_dispose_.17042
- ___Block_byref_object_dispose_.18030
- ___Block_byref_object_dispose_.18635
- ___Block_byref_object_dispose_.19722
- ___Block_byref_object_dispose_.1996
- ___Block_byref_object_dispose_.20528
- ___Block_byref_object_dispose_.24637
- ___Block_byref_object_dispose_.24803
- ___Block_byref_object_dispose_.2662
- ___Block_byref_object_dispose_.4218
- ___Block_byref_object_dispose_.5082
- ___Block_byref_object_dispose_.5342
- ___Block_byref_object_dispose_.5795
- ___Block_byref_object_dispose_.6439
- ___Block_byref_object_dispose_.6618
- ___Block_byref_object_dispose_.7411
- ___Block_byref_object_dispose_.8938
- ___Block_byref_object_dispose_.9251
- ___Block_byref_object_dispose_.9446
- ___block_literal_global.10158
- ___block_literal_global.10821
- ___block_literal_global.11584
- ___block_literal_global.11956
- ___block_literal_global.13093
- ___block_literal_global.14955
- ___block_literal_global.15379
- ___block_literal_global.16564
- ___block_literal_global.16838
- ___block_literal_global.18211
- ___block_literal_global.1900
- ___block_literal_global.19468
- ___block_literal_global.19745
- ___block_literal_global.20194
- ___block_literal_global.21147
- ___block_literal_global.22490
- ___block_literal_global.22812
- ___block_literal_global.24409
- ___block_literal_global.25024
- ___block_literal_global.2728
- ___block_literal_global.3672
- ___block_literal_global.5164
- ___block_literal_global.5337
- ___block_literal_global.5897
- ___block_literal_global.6449
- ___block_literal_global.6594
- ___block_literal_global.764
- ___block_literal_global.7664
- ___block_literal_global.8564
- ___block_literal_global.9021
- ___block_literal_global.9554
- _hkConfig.21131
- _objc_msgSend$initWithNumIPs:numIPsTried:numBonjourNames:
- _objc_msgSend$resetWithNumIPs:numIPsTried:numBonjourNames:
- _objc_msgSend$setSessionInfoWithNumIPsResolved:numIPsTried:numBonjourNames:
- _sharedInstance.onceToken.15378
CStrings:
+ "\x14!#\x11\x12\x11"
+ "%@ '%@' - Close with error %@ and IP: %@"
+ "%@ '%@' - resolver failure with error %@ and IP: %@"
+ "%@ '%{private}@' - Opening finished with error %@ and IP: %@"
+ "(Unknown)"
+ "@60@0:8Q16Q24Q32@40@48B56"
+ "Coordinator: lost accessory: %@ with error: %@ and isDiscovering: %@"
+ "Num IP Addresses: %lu, Num IP Addresses Tried: %lu, Num Bonjour Names: %lu, IP Address: %@, Service Name: %@ Resolve Attmpt: %@"
+ "T@\"NSString\",R,N,V_ipAddress"
+ "T@\"NSString\",R,N,V_serviceName"
+ "TB,R,N,V_resolveAttempted"
+ "["
+ "]"
+ "_resolveAttempted"
+ "initWithNumIPs:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:"
+ "ipAddress"
+ "rangeOfString:"
+ "resetWithNumIPs:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:"
+ "resolveAttempted"
+ "serviceName"
+ "setSessionInfoWithNumIPsResolved:numIPsTried:numBonjourNames:ipAddress:serviceName:resolveAttempted:"
+ "v60@0:8Q16Q24Q32@\"NSString\"40@\"NSString\"48B56"
+ "v60@0:8Q16Q24Q32@40@48B56"
+ "\xd1"
- "\x04!#\x11\x12\x11"
- "@40@0:8Q16Q24Q32"
- "initWithNumIPs:numIPsTried:numBonjourNames:"
- "resetWithNumIPs:numIPsTried:numBonjourNames:"
- "setSessionInfoWithNumIPsResolved:numIPsTried:numBonjourNames:"
- "v40@0:8Q16Q24Q32"
- "\xc1"

```
