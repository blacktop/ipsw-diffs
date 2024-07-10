## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/Versions/A/NetworkExtension`

```diff

-2032.0.0.0.2
-  __TEXT.__text: 0x1eb37c
-  __TEXT.__auth_stubs: 0x3c40
+2026.0.0.0.2
+  __TEXT.__text: 0x1eb740
+  __TEXT.__auth_stubs: 0x3c30
   __TEXT.__objc_methlist: 0xd5dc
-  __TEXT.__cstring: 0x1763b
+  __TEXT.__cstring: 0x175ad
   __TEXT.__swift5_typeref: 0x332
-  __TEXT.__const: 0x2408
-  __TEXT.__constg_swiftt: 0x540
+  __TEXT.__const: 0x23f8
+  __TEXT.__constg_swiftt: 0x530
   __TEXT.__swift5_reflstr: 0xa4
   __TEXT.__swift5_fieldmd: 0x228
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x5384
-  __TEXT.__oslogstring: 0x213b2
-  __TEXT.__unwind_info: 0x4548
+  __TEXT.__gcc_except_tab: 0x5404
+  __TEXT.__oslogstring: 0x212e8
+  __TEXT.__unwind_info: 0x4538
   __TEXT.__eh_frame: 0x598
-  __TEXT.__objc_classname: 0x23be
-  __TEXT.__objc_methname: 0x1925d
-  __TEXT.__objc_methtype: 0x379a
-  __TEXT.__objc_stubs: 0xf6a0
-  __DATA_CONST.__got: 0x1568
+  __TEXT.__objc_classname: 0x2399
+  __TEXT.__objc_methname: 0x191c5
+  __TEXT.__objc_methtype: 0x3728
+  __TEXT.__objc_stubs: 0xf660
+  __DATA_CONST.__got: 0x1498
   __DATA_CONST.__const: 0x2ce8
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x200
+  __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c28
+  __DATA_CONST.__objc_selrefs: 0x4c18
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0x1e30
-  __AUTH_CONST.__auth_ptr: 0x170
-  __AUTH_CONST.__const: 0x43d8
-  __AUTH_CONST.__cfstring: 0x17080
-  __AUTH_CONST.__objc_const: 0x22088
+  __AUTH_CONST.__auth_got: 0x1e28
+  __AUTH_CONST.__auth_ptr: 0x278
+  __AUTH_CONST.__const: 0x4408
+  __AUTH_CONST.__cfstring: 0x17020
+  __AUTH_CONST.__objc_const: 0x21fc8
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x6e30
   __AUTH.__data: 0x1d8
-  __DATA.__objc_ivar: 0x1a58
-  __DATA.__data: 0x1a50
-  __DATA.__common: 0x198
+  __DATA.__objc_ivar: 0x1a4c
+  __DATA.__data: 0x1980
+  __DATA.__common: 0x208
   __DATA.__bss: 0xbd0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6675
-  Symbols:   15657
-  CStrings:  3733
+  Functions: 6677
+  Symbols:   15648
+  CStrings:  3731
 
Symbols:
+ -[NEIKEv2IKESA shouldReceiveWildcard]
+ -[NEIKEv2Listener delegate]
+ -[NEIKEv2Listener receivePacket:]
+ -[NEIKEv2Listener reportError:]
+ -[NEIKEv2Packet receiverSPI]
+ -[NEIKEv2Packet senderSPI]
+ -[NEIKEv2Transport addClient:wildcard:delegate:]
+ -[NEIKEv2Transport disableWildcardForClient:remoteSPI:]
+ GCC_except_table2795
+ GCC_except_table2797
+ GCC_except_table2808
+ GCC_except_table3051
+ GCC_except_table3056
+ GCC_except_table3062
+ GCC_except_table3065
+ GCC_except_table3083
+ GCC_except_table3084
+ GCC_except_table3085
+ GCC_except_table3099
+ GCC_except_table3109
+ GCC_except_table3110
+ GCC_except_table3193
+ GCC_except_table3241
+ GCC_except_table3291
+ GCC_except_table3305
+ GCC_except_table3314
+ GCC_except_table3316
+ GCC_except_table3333
+ GCC_except_table3334
+ GCC_except_table3335
+ GCC_except_table3351
+ GCC_except_table3392
+ GCC_except_table3400
+ GCC_except_table3434
+ GCC_except_table3435
+ GCC_except_table3524
+ GCC_except_table3548
+ GCC_except_table3784
+ GCC_except_table3811
+ GCC_except_table3814
+ GCC_except_table3897
+ GCC_except_table3945
+ GCC_except_table3952
+ GCC_except_table4053
+ GCC_except_table4068
+ GCC_except_table4074
+ GCC_except_table4096
+ GCC_except_table4097
+ GCC_except_table4101
+ GCC_except_table4106
+ GCC_except_table4107
+ GCC_except_table4113
+ GCC_except_table4120
+ GCC_except_table4121
+ GCC_except_table4193
+ GCC_except_table4194
+ GCC_except_table4202
+ GCC_except_table4300
+ GCC_except_table4303
+ GCC_except_table4384
+ GCC_except_table4554
+ GCC_except_table4564
+ GCC_except_table4568
+ GCC_except_table4581
+ GCC_except_table4603
+ GCC_except_table4611
+ GCC_except_table4701
+ GCC_except_table4770
+ GCC_except_table4790
+ GCC_except_table4804
+ GCC_except_table4902
+ GCC_except_table4907
+ GCC_except_table4951
+ GCC_except_table4999
+ GCC_except_table5061
+ GCC_except_table5064
+ GCC_except_table5102
+ GCC_except_table5126
+ GCC_except_table5137
+ GCC_except_table5176
+ GCC_except_table5181
+ GCC_except_table5184
+ GCC_except_table5226
+ GCC_except_table5247
+ GCC_except_table5250
+ GCC_except_table5322
+ GCC_except_table5646
+ GCC_except_table5658
+ GCC_except_table5659
+ GCC_except_table5662
+ GCC_except_table5715
+ GCC_except_table5721
+ GCC_except_table5722
+ GCC_except_table5731
+ GCC_except_table5734
+ GCC_except_table5740
+ GCC_except_table5761
+ GCC_except_table5762
+ GCC_except_table5765
+ GCC_except_table5766
+ GCC_except_table5769
+ GCC_except_table5775
+ GCC_except_table5784
+ GCC_except_table5787
+ GCC_except_table5791
+ GCC_except_table5869
+ GCC_except_table5870
+ GCC_except_table6005
+ GCC_except_table6006
+ GCC_except_table6015
+ GCC_except_table6021
+ GCC_except_table6022
+ GCC_except_table6027
+ GCC_except_table6053
+ GCC_except_table6134
+ GCC_except_table6135
+ OBJC_IVAR_$_NEIKEv2Listener._transport
+ OBJC_IVAR_$_NEIKEv2TransportClient._wildcard
+ __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.501
+ __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.505
+ __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.509
+ __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.513
+ __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.517
+ __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.521
+ __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.525
+ __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.529
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.536
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.540
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.544
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.548
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.552
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.556
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.563
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.567
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.571
+ __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.578
+ __46-[NEIKEv2Session(Exchange) receiveConnection:]_block_invoke.297
+ __46-[NEIKEv2Session(Exchange) receiveConnection:]_block_invoke.304
+ __46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.642
+ __46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.643
+ __47-[NEIKEv2Session(Exchange) initiateNewChildSA:]_block_invoke.347
+ __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.585
+ __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.589
+ __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.593
+ __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.597
+ __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.601
+ __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.605
+ __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.610
+ __48-[NEIKEv2Session(Exchange) initiateMOBIKEInner:]_block_invoke.675
+ __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.456
+ __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.457
+ __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.458
+ __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.459
+ __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.460
+ __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke_2.461
+ __51-[NEIKEv2Transport sendData:sendCompletionHandler:]_block_invoke.78
+ __51-[NEIKEv2Transport sendData:sendCompletionHandler:]_block_invoke.81
+ __53-[NEIKEv2Session(Exchange) receiveNewChildSA:packet:]_block_invoke.367
+ __53-[NEIKEv2Session(Exchange) receiveNewChildSA:packet:]_block_invoke.368
+ __55-[NEIKEv2Session(Exchange) receiveRekeyChildSA:packet:]_block_invoke.488
+ __56-[NEIKEv2Listener createListenerWithParameters:attempt:]_block_invoke.5
+ __56-[NEIKEv2Listener createListenerWithParameters:attempt:]_block_invoke.9
+ __Block_byref_object_copy_.12388
+ __Block_byref_object_copy_.14778
+ __Block_byref_object_copy_.17081
+ __Block_byref_object_copy_.21084
+ __Block_byref_object_copy_.22145
+ __Block_byref_object_copy_.23367
+ __Block_byref_object_copy_.24034
+ __Block_byref_object_copy_.26445
+ __Block_byref_object_copy_.27569
+ __Block_byref_object_copy_.9608
+ __Block_byref_object_dispose_.12389
+ __Block_byref_object_dispose_.14779
+ __Block_byref_object_dispose_.17082
+ __Block_byref_object_dispose_.21085
+ __Block_byref_object_dispose_.22146
+ __Block_byref_object_dispose_.23368
+ __Block_byref_object_dispose_.24035
+ __Block_byref_object_dispose_.26446
+ __Block_byref_object_dispose_.27570
+ __Block_byref_object_dispose_.9609
+ ___33-[NEIKEv2Listener receivePacket:]_block_invoke
+ ___39-[NEIKEv2Listener handleNewConnection:]_block_invoke
+ ___48-[NEIKEv2Listener startFailsafeTimerForSession:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48w56w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48w56w
+ ___destroy_helper_block_e8_32s40s48w56w
+ __block_descriptor_tmp.18.24936
+ __block_descriptor_tmp.19348
+ __block_descriptor_tmp.22849
+ __block_descriptor_tmp.24872
+ __block_descriptor_tmp.25480
+ __block_literal_global.10.15243
+ __block_literal_global.10.9261
+ __block_literal_global.12673
+ __block_literal_global.13048
+ __block_literal_global.13939
+ __block_literal_global.14.21611
+ __block_literal_global.14.25099
+ __block_literal_global.14113
+ __block_literal_global.14780
+ __block_literal_global.15245
+ __block_literal_global.15816
+ __block_literal_global.16052
+ __block_literal_global.16742
+ __block_literal_global.17090
+ __block_literal_global.17525
+ __block_literal_global.17661
+ __block_literal_global.17969
+ __block_literal_global.19.13952
+ __block_literal_global.19.17652
+ __block_literal_global.19274
+ __block_literal_global.19902
+ __block_literal_global.20170
+ __block_literal_global.21179
+ __block_literal_global.21616
+ __block_literal_global.22.13953
+ __block_literal_global.22.17658
+ __block_literal_global.22011
+ __block_literal_global.22760
+ __block_literal_global.22847
+ __block_literal_global.23312
+ __block_literal_global.23452
+ __block_literal_global.23562
+ __block_literal_global.23596
+ __block_literal_global.23778
+ __block_literal_global.24807
+ __block_literal_global.24870
+ __block_literal_global.25103
+ __block_literal_global.25203
+ __block_literal_global.25586
+ __block_literal_global.25982
+ __block_literal_global.26158
+ __block_literal_global.26412
+ __block_literal_global.26953
+ __block_literal_global.27590
+ __block_literal_global.28.26449
+ __block_literal_global.30.22767
+ __block_literal_global.4.13942
+ __block_literal_global.63.19897
+ __block_literal_global.7.24797
+ __block_literal_global.72.25198
+ __block_literal_global.9259
+ _associated conformance 16NetworkExtension26NEIKEv2CryptoKitSPAKE2PlusC4RoleOSHAASQ
+ _extensionAuxiliaryHostProtocol.protocol.19898
+ _extensionAuxiliaryHostProtocol.protocol.23597
+ _extensionAuxiliaryHostProtocol.protocol.25199
+ _extensionAuxiliaryHostProtocol.protocolInit.19896
+ _extensionAuxiliaryHostProtocol.protocolInit.23595
+ _extensionAuxiliaryHostProtocol.protocolInit.25197
+ _extensionAuxiliaryVendorProtocol.protocol.19903
+ _extensionAuxiliaryVendorProtocol.protocol.25204
+ _extensionAuxiliaryVendorProtocol.protocolInit.19901
+ _extensionAuxiliaryVendorProtocol.protocolInit.25202
+ _symbolic _____ 16NetworkExtension19NEIKEv2CryptoKitKeyO
+ _symbolic _____ 16NetworkExtension26NEIKEv2CryptoKitSPAKE2PlusC4RoleO
+ convert_error_to_string.24027
+ driverInterface.driverInterface.16743
+ driverInterface.driverInterface.20167
+ driverInterface.driverInterface.21612
+ driverInterface.onceToken.16741
+ driverInterface.onceToken.20166
+ driverInterface.onceToken.21610
+ g_noAppFilter.27543
+ globalConfigurationManager.gChangeQueue.17656
+ globalConfigurationManager.gConfigurationManager.17653
+ globalConfigurationManager.onceToken.17651
+ initGlobals.onceToken.16051
+ isA_CFArray.25298
+ loadedManagers.loadedManagers.26410
+ loadedManagers.loadedManagers.27546
+ loadedManagers.managers_init.26409
+ loadedManagers.managers_init.27545
+ managerInterface.managerInterface.20171
+ managerInterface.managerInterface.21617
+ managerInterface.onceToken.20169
+ managerInterface.onceToken.21615
+ sharedManager.onceToken.17660
+ sharedManager.onceToken.27589
- -[NEIKEv2Listener invalidatingTransport:]
- -[NEIKEv2Listener receivePacket:transport:]
- -[NEIKEv2Transport addClient:delegate:]
- -[NEIKEv2Transport cancelInvalidationTimer]
- -[NEIKEv2Transport invalidate]
- -[NEIKEv2Transport receivePacket:]
- -[NEIKEv2Transport setRemoteSPI:forClient:]
- -[NEIKEv2Transport setWildcardDelegate:preventsInvalidation:]
- -[NEIKEv2Transport startInvalidationTimer]
- GCC_except_table2794
- GCC_except_table2804
- GCC_except_table3043
- GCC_except_table3048
- GCC_except_table3054
- GCC_except_table3057
- GCC_except_table3075
- GCC_except_table3076
- GCC_except_table3077
- GCC_except_table3091
- GCC_except_table3101
- GCC_except_table3102
- GCC_except_table3185
- GCC_except_table3233
- GCC_except_table3283
- GCC_except_table3297
- GCC_except_table3306
- GCC_except_table3308
- GCC_except_table3325
- GCC_except_table3326
- GCC_except_table3327
- GCC_except_table3343
- GCC_except_table3385
- GCC_except_table3393
- GCC_except_table3395
- GCC_except_table3430
- GCC_except_table3433
- GCC_except_table3522
- GCC_except_table3546
- GCC_except_table3782
- GCC_except_table3807
- GCC_except_table3808
- GCC_except_table3895
- GCC_except_table3943
- GCC_except_table3950
- GCC_except_table4051
- GCC_except_table4066
- GCC_except_table4072
- GCC_except_table4087
- GCC_except_table4088
- GCC_except_table4099
- GCC_except_table4104
- GCC_except_table4105
- GCC_except_table4111
- GCC_except_table4118
- GCC_except_table4119
- GCC_except_table4191
- GCC_except_table4192
- GCC_except_table4200
- GCC_except_table4294
- GCC_except_table4295
- GCC_except_table4382
- GCC_except_table4552
- GCC_except_table4562
- GCC_except_table4566
- GCC_except_table4579
- GCC_except_table4599
- GCC_except_table4607
- GCC_except_table4699
- GCC_except_table4768
- GCC_except_table4788
- GCC_except_table4802
- GCC_except_table4900
- GCC_except_table4905
- GCC_except_table4949
- GCC_except_table4995
- GCC_except_table5059
- GCC_except_table5062
- GCC_except_table5100
- GCC_except_table5120
- GCC_except_table5135
- GCC_except_table5174
- GCC_except_table5175
- GCC_except_table5182
- GCC_except_table5224
- GCC_except_table5245
- GCC_except_table5248
- GCC_except_table5320
- GCC_except_table5644
- GCC_except_table5656
- GCC_except_table5657
- GCC_except_table5660
- GCC_except_table5713
- GCC_except_table5719
- GCC_except_table5720
- GCC_except_table5729
- GCC_except_table5732
- GCC_except_table5738
- GCC_except_table5753
- GCC_except_table5754
- GCC_except_table5763
- GCC_except_table5764
- GCC_except_table5767
- GCC_except_table5773
- GCC_except_table5782
- GCC_except_table5785
- GCC_except_table5789
- GCC_except_table5867
- GCC_except_table5868
- GCC_except_table5992
- GCC_except_table5993
- GCC_except_table6013
- GCC_except_table6018
- GCC_except_table6019
- GCC_except_table6025
- GCC_except_table6051
- GCC_except_table6130
- GCC_except_table6131
- OBJC_IVAR_$_NEIKEv2Listener._connectionTransports
- OBJC_IVAR_$_NEIKEv2Listener._packetDelegateTransport
- OBJC_IVAR_$_NEIKEv2Transport._invalidationTimer
- OBJC_IVAR_$_NEIKEv2Transport._wildcardDelegate
- OBJC_IVAR_$_NEIKEv2Transport._wildcardPreventsInvalidation
- __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.510
- __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.514
- __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.518
- __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.522
- __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.526
- __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.530
- __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.534
- __101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.538
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.545
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.549
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.553
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.557
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.561
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.565
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.572
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.576
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.580
- __120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.587
- __46-[NEIKEv2Session(Exchange) receiveConnection:]_block_invoke.306
- __46-[NEIKEv2Session(Exchange) receiveConnection:]_block_invoke.313
- __46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.651
- __46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.652
- __47-[NEIKEv2Session(Exchange) initiateNewChildSA:]_block_invoke.356
- __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.594
- __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.598
- __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.602
- __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.610
- __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.615
- __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.614
- __47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.619
- __48-[NEIKEv2Session(Exchange) initiateMOBIKEInner:]_block_invoke.684
- __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.465
- __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.466
- __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.467
- __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.468
- __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.469
- __49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke_2.470
- __51-[NEIKEv2Transport sendData:sendCompletionHandler:]_block_invoke.76
- __51-[NEIKEv2Transport sendData:sendCompletionHandler:]_block_invoke.79
- __53-[NEIKEv2Session(Exchange) receiveNewChildSA:packet:]_block_invoke.376
- __53-[NEIKEv2Session(Exchange) receiveNewChildSA:packet:]_block_invoke.377
- __55-[NEIKEv2Session(Exchange) receiveRekeyChildSA:packet:]_block_invoke.497
- __56-[NEIKEv2Listener createListenerWithParameters:attempt:]_block_invoke.2
- __56-[NEIKEv2Listener createListenerWithParameters:attempt:]_block_invoke.4
- __Block_byref_object_copy_.12384
- __Block_byref_object_copy_.14786
- __Block_byref_object_copy_.17087
- __Block_byref_object_copy_.21100
- __Block_byref_object_copy_.22161
- __Block_byref_object_copy_.23383
- __Block_byref_object_copy_.24050
- __Block_byref_object_copy_.26461
- __Block_byref_object_copy_.27591
- __Block_byref_object_copy_.9606
- __Block_byref_object_dispose_.12385
- __Block_byref_object_dispose_.14787
- __Block_byref_object_dispose_.17088
- __Block_byref_object_dispose_.21101
- __Block_byref_object_dispose_.22162
- __Block_byref_object_dispose_.23384
- __Block_byref_object_dispose_.24051
- __Block_byref_object_dispose_.26462
- __Block_byref_object_dispose_.27592
- __Block_byref_object_dispose_.9607
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NEIKEv2WildcardTransportDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NEIKEv2WildcardTransportDelegate
- __OBJC_$_PROTOCOL_REFS_NEIKEv2WildcardTransportDelegate
- __OBJC_LABEL_PROTOCOL_$_NEIKEv2WildcardTransportDelegate
- __OBJC_PROTOCOL_$_NEIKEv2WildcardTransportDelegate
- ___42-[NEIKEv2Transport startInvalidationTimer]_block_invoke
- ___43-[NEIKEv2Listener receivePacket:transport:]_block_invoke
- __block_descriptor_tmp.18.24952
- __block_descriptor_tmp.19352
- __block_descriptor_tmp.22865
- __block_descriptor_tmp.24888
- __block_descriptor_tmp.25496
- __block_literal_global.10.15248
- __block_literal_global.10.9259
- __block_literal_global.12669
- __block_literal_global.13044
- __block_literal_global.13941
- __block_literal_global.14.21627
- __block_literal_global.14.25115
- __block_literal_global.14121
- __block_literal_global.14788
- __block_literal_global.15250
- __block_literal_global.15821
- __block_literal_global.16058
- __block_literal_global.16748
- __block_literal_global.17096
- __block_literal_global.17531
- __block_literal_global.17667
- __block_literal_global.17973
- __block_literal_global.19.13954
- __block_literal_global.19.17658
- __block_literal_global.19278
- __block_literal_global.19915
- __block_literal_global.20183
- __block_literal_global.21195
- __block_literal_global.21632
- __block_literal_global.22.13955
- __block_literal_global.22.17664
- __block_literal_global.22027
- __block_literal_global.22776
- __block_literal_global.22863
- __block_literal_global.23328
- __block_literal_global.23468
- __block_literal_global.23578
- __block_literal_global.23612
- __block_literal_global.23794
- __block_literal_global.24823
- __block_literal_global.24886
- __block_literal_global.25119
- __block_literal_global.25219
- __block_literal_global.25602
- __block_literal_global.25998
- __block_literal_global.26174
- __block_literal_global.26428
- __block_literal_global.26969
- __block_literal_global.27612
- __block_literal_global.28.26465
- __block_literal_global.30.22783
- __block_literal_global.4.13944
- __block_literal_global.63.19910
- __block_literal_global.7.24813
- __block_literal_global.72.25214
- __block_literal_global.9257
- _associated conformance 16NetworkExtension26NEIKEv2CryptoKitSPAKE2PlusC4Role33_8A6EAEC7B0CD28E3C1D36D746A66647FLLOSHAASQ
- _extensionAuxiliaryHostProtocol.protocol.19911
- _extensionAuxiliaryHostProtocol.protocol.23613
- _extensionAuxiliaryHostProtocol.protocol.25215
- _extensionAuxiliaryHostProtocol.protocolInit.19909
- _extensionAuxiliaryHostProtocol.protocolInit.23611
- _extensionAuxiliaryHostProtocol.protocolInit.25213
- _extensionAuxiliaryVendorProtocol.protocol.19916
- _extensionAuxiliaryVendorProtocol.protocol.25220
- _extensionAuxiliaryVendorProtocol.protocolInit.19914
- _extensionAuxiliaryVendorProtocol.protocolInit.25218
- _nw_protocol_stack_includes_protocol
- _objc_msgSend$invalidatingTransport:
- _objc_msgSend$receivePacket:transport:
- _symbolic _____ 16NetworkExtension19NEIKEv2CryptoKitKey33_8A6EAEC7B0CD28E3C1D36D746A66647FLLO
- _symbolic _____ 16NetworkExtension26NEIKEv2CryptoKitSPAKE2PlusC4Role33_8A6EAEC7B0CD28E3C1D36D746A66647FLLO
- convert_error_to_string.24043
- createNATDetectionHashForInitiatorSPI:responderSPI:address:.hashBytes
- driverInterface.driverInterface.16749
- driverInterface.driverInterface.20180
- driverInterface.driverInterface.21628
- driverInterface.onceToken.16747
- driverInterface.onceToken.20179
- driverInterface.onceToken.21626
- g_noAppFilter.27565
- globalConfigurationManager.gChangeQueue.17662
- globalConfigurationManager.gConfigurationManager.17659
- globalConfigurationManager.onceToken.17657
- initGlobals.onceToken.16057
- isA_CFArray.25314
- loadedManagers.loadedManagers.26426
- loadedManagers.loadedManagers.27568
- loadedManagers.managers_init.26425
- loadedManagers.managers_init.27567
- managerInterface.managerInterface.20184
- managerInterface.managerInterface.21633
- managerInterface.onceToken.20182
- managerInterface.onceToken.21631
- sharedManager.onceToken.17666
- sharedManager.onceToken.27611
CStrings:
+ " wildcard"
+ "-[NEIKEv2Listener receivePacket:]"
+ "-[NEIKEv2Transport addClient:wildcard:delegate:]"
+ "[NEIKEv2TransportClient %!@(MISSING)%!s(MISSING) %!@(MISSING)]"
- "-[NEIKEv2Listener receivePacket:transport:]"
- "-[NEIKEv2Transport addClient:delegate:]"
- "Failed to create IKE SA Init Invalid KE packet"
- "KE method received in IKE SA Init packet (%!@(MISSING)) doesn't match selected (%!@(MISSING)) (receive)"
- "SA INIT INVALID KE"
- "[NEIKEv2TransportClient %!@(MISSING)-%!@(MISSING) %!@(MISSING)]"

```
