## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-1838.42.1.0.0
-  __TEXT.__text: 0x197ce4
+1838.62.1.0.0
+  __TEXT.__text: 0x198b60
   __TEXT.__auth_stubs: 0x3490
-  __TEXT.__objc_methlist: 0xca34
+  __TEXT.__objc_methlist: 0xca4c
   __TEXT.__const: 0x1c58
-  __TEXT.__cstring: 0x140e8
+  __TEXT.__cstring: 0x140eb
   __TEXT.__constg_swiftt: 0x100
   __TEXT.__swift5_typeref: 0x49
   __TEXT.__swift5_reflstr: 0x35

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x14
-  __TEXT.__gcc_except_tab: 0x395c
-  __TEXT.__oslogstring: 0x1cf56
-  __TEXT.__unwind_info: 0x3ff0
+  __TEXT.__gcc_except_tab: 0x399c
+  __TEXT.__oslogstring: 0x1cfc3
+  __TEXT.__unwind_info: 0x4014
   __TEXT.__eh_frame: 0x120
   __TEXT.__objc_classname: 0x21fc
-  __TEXT.__objc_methname: 0x17939
+  __TEXT.__objc_methname: 0x17923
   __TEXT.__objc_methtype: 0x3356
   __TEXT.__objc_stubs: 0xe720
   __DATA_CONST.__got: 0xa00
-  __DATA_CONST.__const: 0x52b0
+  __DATA_CONST.__const: 0x52d8
   __DATA_CONST.__objc_classlist: 0x9a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17c38
+  __DATA_CONST.__objc_const: 0x17c18
   __DATA_CONST.__objc_selrefs: 0x47b0
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__const: 0xd18

   __AUTH_CONST.__auth_got: 0x1a58
   __AUTH.__objc_data: 0x0
   __DATA.__objc_protorefs: 0xf0
-  __DATA.__objc_classrefs: 0x9d8
+  __DATA.__objc_classrefs: 0x9e0
   __DATA.__objc_superrefs: 0x6c0
-  __DATA.__objc_ivar: 0x1908
+  __DATA.__objc_ivar: 0x1904
   __DATA.__data: 0x16e8
   __DATA.__common: 0x158
   __DATA.__bss: 0x998

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6019
-  Symbols:   20224
-  CStrings:  11238
+  Functions: 6026
+  Symbols:   20241
+  CStrings:  11240
 
Symbols:
+ +[NEIKEv2CreateChildPacket createRekeyRequestChildSA:]
+ -[NEIKEv2ChildSA configProposalsWithoutDH]
+ -[NEIKEv2ChildSA setConfigProposalsWithoutDH:]
+ -[NEIKEv2ChildSAConfiguration opportunisticPFS]
+ -[NEIKEv2ChildSAConfiguration setOpportunisticPFS:]
+ -[NEIKEv2ChildSAProposal copyWithoutDH]
+ -[NEIKEv2ChildSAProposal hash]
+ -[NEIKEv2ChildSAProposal isEqual:]
+ -[NEIKEv2CreateChildPacket validateRekeyResponseChildSA:]
+ GCC_except_table2336
+ GCC_except_table2548
+ GCC_except_table2550
+ GCC_except_table2787
+ GCC_except_table2798
+ GCC_except_table2801
+ GCC_except_table2817
+ GCC_except_table2818
+ GCC_except_table2819
+ GCC_except_table2834
+ GCC_except_table2848
+ GCC_except_table2849
+ GCC_except_table2891
+ GCC_except_table2895
+ GCC_except_table2940
+ GCC_except_table2988
+ GCC_except_table3039
+ GCC_except_table3053
+ GCC_except_table3064
+ GCC_except_table3077
+ GCC_except_table3078
+ GCC_except_table3079
+ GCC_except_table3096
+ GCC_except_table3135
+ GCC_except_table3141
+ GCC_except_table3173
+ GCC_except_table3175
+ GCC_except_table3176
+ GCC_except_table3261
+ GCC_except_table3283
+ GCC_except_table3524
+ GCC_except_table3525
+ GCC_except_table3527
+ GCC_except_table3612
+ GCC_except_table3756
+ GCC_except_table3767
+ GCC_except_table3773
+ GCC_except_table3790
+ GCC_except_table3791
+ GCC_except_table3792
+ GCC_except_table3794
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3800
+ GCC_except_table3806
+ GCC_except_table3819
+ GCC_except_table3820
+ GCC_except_table3892
+ GCC_except_table3893
+ GCC_except_table3901
+ GCC_except_table3995
+ GCC_except_table3996
+ GCC_except_table3997
+ GCC_except_table3998
+ GCC_except_table3999
+ GCC_except_table4001
+ GCC_except_table4081
+ GCC_except_table4248
+ GCC_except_table4258
+ GCC_except_table4262
+ GCC_except_table4274
+ GCC_except_table4294
+ GCC_except_table4296
+ GCC_except_table4302
+ GCC_except_table4304
+ GCC_except_table4392
+ GCC_except_table4459
+ GCC_except_table4480
+ GCC_except_table4493
+ GCC_except_table4590
+ GCC_except_table4595
+ GCC_except_table4636
+ GCC_except_table4682
+ GCC_except_table4684
+ GCC_except_table4780
+ GCC_except_table4800
+ GCC_except_table4802
+ GCC_except_table4811
+ GCC_except_table4850
+ GCC_except_table4853
+ GCC_except_table4855
+ GCC_except_table4858
+ GCC_except_table4900
+ GCC_except_table4921
+ GCC_except_table4924
+ GCC_except_table4994
+ GCC_except_table5313
+ GCC_except_table5325
+ GCC_except_table5326
+ GCC_except_table5329
+ GCC_except_table5387
+ GCC_except_table5388
+ GCC_except_table5397
+ GCC_except_table5400
+ GCC_except_table5406
+ GCC_except_table5422
+ GCC_except_table5423
+ GCC_except_table5427
+ GCC_except_table5428
+ GCC_except_table5431
+ GCC_except_table5432
+ GCC_except_table5440
+ GCC_except_table5452
+ GCC_except_table5456
+ GCC_except_table5529
+ GCC_except_table5530
+ GCC_except_table5642
+ GCC_except_table5643
+ GCC_except_table5644
+ GCC_except_table5645
+ GCC_except_table5646
+ GCC_except_table5647
+ GCC_except_table5648
+ GCC_except_table5662
+ GCC_except_table5663
+ GCC_except_table5664
+ GCC_except_table5690
+ GCC_except_table5767
+ GCC_except_table5768
+ GCC_except_table5769
+ GCC_except_table5770
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_IVAR_$_NEIKEv2ChildSA._internalProposalsWithoutDH
+ _OBJC_IVAR_$_NEIKEv2ChildSA._rekeyRequestProposals
+ _OBJC_IVAR_$_NEIKEv2ChildSA._rekeyResponseProposal
+ _OBJC_IVAR_$_NEIKEv2ChildSAConfiguration._opportunisticPFS
+ ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.72
+ ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.76
+ ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.80
+ ___37-[NEIKEv2Session sendCurrentRequest:]_block_invoke.70
+ ___46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.314
+ ___46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.324
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.275
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.279
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.283
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.287
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.291
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.295
+ ___48-[NEIKEv2Listener startFailsafeTimerForSession:]_block_invoke
+ ___48-[NEIKEv2Session(Exchange) initiateMOBIKEInner:]_block_invoke.343
+ ___55-[NEIKEv2Session(Exchange) receiveRekeyChildSA:packet:]_block_invoke.262
+ ___Block_byref_object_copy_.11593
+ ___Block_byref_object_copy_.13983
+ ___Block_byref_object_copy_.19909
+ ___Block_byref_object_copy_.20942
+ ___Block_byref_object_copy_.22073
+ ___Block_byref_object_copy_.22719
+ ___Block_byref_object_copy_.24966
+ ___Block_byref_object_dispose_.11594
+ ___Block_byref_object_dispose_.13984
+ ___Block_byref_object_dispose_.19910
+ ___Block_byref_object_dispose_.20943
+ ___Block_byref_object_dispose_.22074
+ ___Block_byref_object_dispose_.22720
+ ___Block_byref_object_dispose_.24967
+ ___block_descriptor_49_e8_32s40r_e39_B32?0"NEIKEv2ChildSAProposal"8Q16^B24lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48w56w_e5_v8?0lw48l8w56l8s32l8s40l8
+ ___block_descriptor_tmp.18.23490
+ ___block_descriptor_tmp.18172
+ ___block_descriptor_tmp.21634
+ ___block_descriptor_tmp.23426
+ ___block_descriptor_tmp.24015
+ ___block_literal_global.10.14349
+ ___block_literal_global.10.8989
+ ___block_literal_global.11885
+ ___block_literal_global.12.23648
+ ___block_literal_global.12252
+ ___block_literal_global.13130
+ ___block_literal_global.13293
+ ___block_literal_global.13985
+ ___block_literal_global.14.20418
+ ___block_literal_global.14351
+ ___block_literal_global.14914
+ ___block_literal_global.15152
+ ___block_literal_global.15636
+ ___block_literal_global.16386
+ ___block_literal_global.16521
+ ___block_literal_global.16823
+ ___block_literal_global.17.13142
+ ___block_literal_global.17.16512
+ ___block_literal_global.18098
+ ___block_literal_global.18713
+ ___block_literal_global.18977
+ ___block_literal_global.20.16518
+ ___block_literal_global.20006
+ ___block_literal_global.20423
+ ___block_literal_global.20818
+ ___block_literal_global.21561
+ ___block_literal_global.21632
+ ___block_literal_global.22174
+ ___block_literal_global.22285
+ ___block_literal_global.22319
+ ___block_literal_global.22499
+ ___block_literal_global.23371
+ ___block_literal_global.23424
+ ___block_literal_global.23652
+ ___block_literal_global.23740
+ ___block_literal_global.24121
+ ___block_literal_global.24512
+ ___block_literal_global.24684
+ ___block_literal_global.24934
+ ___block_literal_global.25456
+ ___block_literal_global.26019
+ ___block_literal_global.28.24970
+ ___block_literal_global.4.13133
+ ___block_literal_global.62.18708
+ ___block_literal_global.65.23908
+ ___block_literal_global.7.23362
+ ___block_literal_global.71.23735
+ ___block_literal_global.8987
+ __extensionAuxiliaryHostProtocol.protocol.18709
+ __extensionAuxiliaryHostProtocol.protocol.22320
+ __extensionAuxiliaryHostProtocol.protocol.23736
+ __extensionAuxiliaryHostProtocol.protocolInit.18707
+ __extensionAuxiliaryHostProtocol.protocolInit.22318
+ __extensionAuxiliaryHostProtocol.protocolInit.23734
+ __extensionAuxiliaryVendorProtocol.protocol.18714
+ __extensionAuxiliaryVendorProtocol.protocol.23741
+ __extensionAuxiliaryVendorProtocol.protocolInit.18712
+ __extensionAuxiliaryVendorProtocol.protocolInit.23739
+ __unnamed_array_storage.20010
+ __unnamed_array_storage.20956
+ __unnamed_array_storage.26727
+ _convert_error_to_string.22716
+ _driverInterface.driverInterface.15637
+ _driverInterface.driverInterface.18974
+ _driverInterface.driverInterface.20419
+ _driverInterface.onceToken.15635
+ _driverInterface.onceToken.18973
+ _driverInterface.onceToken.20417
+ _g_noAppFilter.25982
+ _globalConfigurationManager.gChangeQueue.16516
+ _globalConfigurationManager.gConfigurationManager.16513
+ _globalConfigurationManager.onceToken.16511
+ _initGlobals.onceToken.15151
+ _loadedManagers.loadedManagers.24932
+ _loadedManagers.loadedManagers.25985
+ _loadedManagers.managers_init.24931
+ _loadedManagers.managers_init.25984
+ _managerInterface.managerInterface.18978
+ _managerInterface.managerInterface.20424
+ _managerInterface.onceToken.18976
+ _managerInterface.onceToken.20422
+ _sharedManager.onceToken.16520
+ _sharedManager.onceToken.26018
- +[NEIKEv2CreateChildPacket createRekeyChildSAForInitiator:]
- -[NEIKEv2ChildSAProposal opportunisticPFS]
- -[NEIKEv2ChildSAProposal setOpportunisticPFS:]
- -[NEIKEv2CreateChildPacket validateRekeyChildSA:]
- GCC_except_table2543
- GCC_except_table2781
- GCC_except_table2786
- GCC_except_table2795
- GCC_except_table2811
- GCC_except_table2812
- GCC_except_table2813
- GCC_except_table2828
- GCC_except_table2842
- GCC_except_table2843
- GCC_except_table2885
- GCC_except_table2889
- GCC_except_table2934
- GCC_except_table2982
- GCC_except_table3033
- GCC_except_table3047
- GCC_except_table3058
- GCC_except_table3071
- GCC_except_table3072
- GCC_except_table3073
- GCC_except_table3089
- GCC_except_table3128
- GCC_except_table3134
- GCC_except_table3166
- GCC_except_table3168
- GCC_except_table3169
- GCC_except_table3254
- GCC_except_table3276
- GCC_except_table3511
- GCC_except_table3517
- GCC_except_table3520
- GCC_except_table3605
- GCC_except_table3749
- GCC_except_table3760
- GCC_except_table3766
- GCC_except_table3781
- GCC_except_table3782
- GCC_except_table3783
- GCC_except_table3784
- GCC_except_table3785
- GCC_except_table3786
- GCC_except_table3787
- GCC_except_table3798
- GCC_except_table3799
- GCC_except_table3813
- GCC_except_table3885
- GCC_except_table3886
- GCC_except_table3894
- GCC_except_table3987
- GCC_except_table3988
- GCC_except_table3989
- GCC_except_table3990
- GCC_except_table3991
- GCC_except_table3992
- GCC_except_table4074
- GCC_except_table4241
- GCC_except_table4251
- GCC_except_table4255
- GCC_except_table4267
- GCC_except_table4287
- GCC_except_table4289
- GCC_except_table4295
- GCC_except_table4297
- GCC_except_table4385
- GCC_except_table4452
- GCC_except_table4473
- GCC_except_table4486
- GCC_except_table4583
- GCC_except_table4588
- GCC_except_table4629
- GCC_except_table4675
- GCC_except_table4677
- GCC_except_table4773
- GCC_except_table4793
- GCC_except_table4795
- GCC_except_table4797
- GCC_except_table4843
- GCC_except_table4844
- GCC_except_table4846
- GCC_except_table4848
- GCC_except_table4893
- GCC_except_table4914
- GCC_except_table4917
- GCC_except_table4987
- GCC_except_table5306
- GCC_except_table5318
- GCC_except_table5319
- GCC_except_table5322
- GCC_except_table5374
- GCC_except_table5380
- GCC_except_table5390
- GCC_except_table5393
- GCC_except_table5399
- GCC_except_table5414
- GCC_except_table5415
- GCC_except_table5416
- GCC_except_table5417
- GCC_except_table5418
- GCC_except_table5419
- GCC_except_table5420
- GCC_except_table5442
- GCC_except_table5445
- GCC_except_table5522
- GCC_except_table5523
- GCC_except_table5629
- GCC_except_table5630
- GCC_except_table5631
- GCC_except_table5632
- GCC_except_table5633
- GCC_except_table5634
- GCC_except_table5635
- GCC_except_table5650
- GCC_except_table5655
- GCC_except_table5656
- GCC_except_table5683
- GCC_except_table5760
- GCC_except_table5761
- GCC_except_table5762
- GCC_except_table5763
- _OBJC_IVAR_$_NEIKEv2ChildSA._initiatorRekeyNonPFSProposal
- _OBJC_IVAR_$_NEIKEv2ChildSA._initiatorRekeyProposal
- _OBJC_IVAR_$_NEIKEv2ChildSA._responderRekeyProposal
- _OBJC_IVAR_$_NEIKEv2ChildSAPayload._includeDHGroup
- _OBJC_IVAR_$_NEIKEv2ChildSAProposal._opportunisticPFS
- ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.70
- ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.75
- ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.79
- ___46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.313
- ___46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.323
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.274
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.278
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.282
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.286
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.290
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.294
- ___48-[NEIKEv2Session(Exchange) initiateMOBIKEInner:]_block_invoke.342
- ___55-[NEIKEv2Session(Exchange) receiveRekeyChildSA:packet:]_block_invoke.261
- ___Block_byref_object_copy_.11451
- ___Block_byref_object_copy_.13833
- ___Block_byref_object_copy_.19847
- ___Block_byref_object_copy_.20884
- ___Block_byref_object_copy_.22015
- ___Block_byref_object_copy_.22661
- ___Block_byref_object_copy_.24954
- ___Block_byref_object_dispose_.11452
- ___Block_byref_object_dispose_.13834
- ___Block_byref_object_dispose_.19848
- ___Block_byref_object_dispose_.20885
- ___Block_byref_object_dispose_.22016
- ___Block_byref_object_dispose_.22662
- ___Block_byref_object_dispose_.24955
- ___block_descriptor_41_e8_32s_e39_B32?0"NEIKEv2ChildSAProposal"8Q16^B24ls32l8
- ___block_descriptor_tmp.18.23477
- ___block_descriptor_tmp.18097
- ___block_descriptor_tmp.21576
- ___block_descriptor_tmp.23413
- ___block_descriptor_tmp.24002
- ___block_literal_global.10.14268
- ___block_literal_global.10.8942
- ___block_literal_global.11748
- ___block_literal_global.12.23635
- ___block_literal_global.12114
- ___block_literal_global.12991
- ___block_literal_global.13154
- ___block_literal_global.13835
- ___block_literal_global.14.20356
- ___block_literal_global.14270
- ___block_literal_global.14836
- ___block_literal_global.15077
- ___block_literal_global.15560
- ___block_literal_global.16306
- ___block_literal_global.16441
- ___block_literal_global.16746
- ___block_literal_global.17.13003
- ___block_literal_global.17.16432
- ___block_literal_global.18023
- ___block_literal_global.18659
- ___block_literal_global.18923
- ___block_literal_global.19944
- ___block_literal_global.20.16438
- ___block_literal_global.20361
- ___block_literal_global.20756
- ___block_literal_global.21503
- ___block_literal_global.21574
- ___block_literal_global.22116
- ___block_literal_global.22227
- ___block_literal_global.22261
- ___block_literal_global.22441
- ___block_literal_global.23358
- ___block_literal_global.23411
- ___block_literal_global.23639
- ___block_literal_global.23727
- ___block_literal_global.24108
- ___block_literal_global.24499
- ___block_literal_global.24672
- ___block_literal_global.24922
- ___block_literal_global.25448
- ___block_literal_global.26012
- ___block_literal_global.28.24958
- ___block_literal_global.4.12994
- ___block_literal_global.62.18654
- ___block_literal_global.65.23895
- ___block_literal_global.7.23349
- ___block_literal_global.71.23722
- ___block_literal_global.8940
- __extensionAuxiliaryHostProtocol.protocol.18655
- __extensionAuxiliaryHostProtocol.protocol.22262
- __extensionAuxiliaryHostProtocol.protocol.23723
- __extensionAuxiliaryHostProtocol.protocolInit.18653
- __extensionAuxiliaryHostProtocol.protocolInit.22260
- __extensionAuxiliaryHostProtocol.protocolInit.23721
- __extensionAuxiliaryVendorProtocol.protocol.18660
- __extensionAuxiliaryVendorProtocol.protocol.23728
- __extensionAuxiliaryVendorProtocol.protocolInit.18658
- __extensionAuxiliaryVendorProtocol.protocolInit.23726
- __unnamed_array_storage.19948
- __unnamed_array_storage.20898
- __unnamed_array_storage.26720
- _convert_error_to_string.22658
- _driverInterface.driverInterface.15561
- _driverInterface.driverInterface.18920
- _driverInterface.driverInterface.20357
- _driverInterface.onceToken.15559
- _driverInterface.onceToken.18919
- _driverInterface.onceToken.20355
- _g_noAppFilter.25975
- _globalConfigurationManager.gChangeQueue.16436
- _globalConfigurationManager.gConfigurationManager.16433
- _globalConfigurationManager.onceToken.16431
- _initGlobals.onceToken.15076
- _loadedManagers.loadedManagers.24920
- _loadedManagers.loadedManagers.25978
- _loadedManagers.managers_init.24919
- _loadedManagers.managers_init.25977
- _managerInterface.managerInterface.18924
- _managerInterface.managerInterface.20362
- _managerInterface.onceToken.18922
- _managerInterface.onceToken.20360
- _sharedManager.onceToken.16440
- _sharedManager.onceToken.26011
CStrings:
+ "%@ %@ Generating SPI(s) for child"
+ "%@ Child SA proposal out of range"
+ "%s called with null ahLarvalSA"
+ "%s called with null childSA.configProposalsWithoutDH"
+ "%s called with null childSA.rekeyRequestProposals"
+ "%s called with null espLarvalSA"
+ "+[NEIKEv2CreateChildPacket(Exchange) createRekeyRequestChildSA:]"
+ "-[NEIKEv2CreateChildPacket(Exchange) validateRekeyResponseChildSA:]"
+ "Session %@ did not start after 5s, invalidating"
+ "_internalProposalsWithoutDH"
+ "_rekeyRequestProposals"
+ "_rekeyResponseProposal"
- "%@ %@ Generating SPI for child"
- "%@ Invalid child SA proposal number %u"
- "%s called with null childSA.configuration.proposals"
- "%s called with null childSA.initiatorRekeyProposal"
- "+[NEIKEv2CreateChildPacket(Exchange) createRekeyChildSAForInitiator:]"
- "-[NEIKEv2CreateChildPacket(Exchange) validateRekeyChildSA:]"
- "_includeDHGroup"
- "_initiatorRekeyNonPFSProposal"
- "_initiatorRekeyProposal"
- "_responderRekeyProposal"

```
