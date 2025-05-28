## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-1838.62.1.0.0
-  __TEXT.__text: 0x198b60
+1838.80.4.0.0
+  __TEXT.__text: 0x198b8c
   __TEXT.__auth_stubs: 0x3490
-  __TEXT.__objc_methlist: 0xca4c
+  __TEXT.__objc_methlist: 0xca14
   __TEXT.__const: 0x1c58
-  __TEXT.__cstring: 0x140eb
+  __TEXT.__cstring: 0x14105
   __TEXT.__constg_swiftt: 0x100
   __TEXT.__swift5_typeref: 0x49
   __TEXT.__swift5_reflstr: 0x35

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x14
   __TEXT.__gcc_except_tab: 0x399c
-  __TEXT.__oslogstring: 0x1cfc3
-  __TEXT.__unwind_info: 0x4014
+  __TEXT.__oslogstring: 0x1cfff
+  __TEXT.__unwind_info: 0x4024
   __TEXT.__eh_frame: 0x120
   __TEXT.__objc_classname: 0x21fc
-  __TEXT.__objc_methname: 0x17923
+  __TEXT.__objc_methname: 0x17903
   __TEXT.__objc_methtype: 0x3356
-  __TEXT.__objc_stubs: 0xe720
+  __TEXT.__objc_stubs: 0xe6a0
   __DATA_CONST.__got: 0xa00
-  __DATA_CONST.__const: 0x52d8
+  __DATA_CONST.__const: 0x52b8
   __DATA_CONST.__objc_classlist: 0x9a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17c18
-  __DATA_CONST.__objc_selrefs: 0x47b0
+  __DATA_CONST.__objc_const: 0x17bd0
+  __DATA_CONST.__objc_selrefs: 0x4790
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__const: 0xd18
   __AUTH_CONST.__auth_ptr: 0x58

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6026
-  Symbols:   20241
-  CStrings:  11240
+  Functions: 6024
+  Symbols:   20230
+  CStrings:  11236
 
Symbols:
+ +[NEIKEv2Packet createPacketFromReceivedData:]
+ -[NEIKEv2Packet processDecryptedPacketForIKESA:]
+ -[NEIKEv2Packet processReceivedPacketForIKESA:]
+ -[NEIKEv2Session reportPrivateNotifies:]
+ -[NEIKEv2Session setPendingPrivateNotifies:]
+ GCC_except_table2782
+ GCC_except_table2793
+ GCC_except_table2796
+ GCC_except_table2812
+ GCC_except_table2813
+ GCC_except_table2814
+ GCC_except_table2829
+ GCC_except_table2843
+ GCC_except_table2844
+ GCC_except_table2886
+ GCC_except_table2890
+ GCC_except_table2935
+ GCC_except_table2983
+ GCC_except_table3034
+ GCC_except_table3048
+ GCC_except_table3059
+ GCC_except_table3072
+ GCC_except_table3073
+ GCC_except_table3074
+ GCC_except_table3091
+ GCC_except_table3132
+ GCC_except_table3138
+ GCC_except_table3170
+ GCC_except_table3172
+ GCC_except_table3258
+ GCC_except_table3280
+ GCC_except_table3515
+ GCC_except_table3521
+ GCC_except_table3522
+ GCC_except_table3609
+ GCC_except_table3753
+ GCC_except_table3764
+ GCC_except_table3770
+ GCC_except_table3785
+ GCC_except_table3786
+ GCC_except_table3787
+ GCC_except_table3797
+ GCC_except_table3802
+ GCC_except_table3803
+ GCC_except_table3809
+ GCC_except_table3816
+ GCC_except_table3817
+ GCC_except_table3889
+ GCC_except_table3890
+ GCC_except_table3898
+ GCC_except_table3991
+ GCC_except_table3992
+ GCC_except_table3993
+ GCC_except_table4078
+ GCC_except_table4245
+ GCC_except_table4255
+ GCC_except_table4259
+ GCC_except_table4271
+ GCC_except_table4291
+ GCC_except_table4293
+ GCC_except_table4299
+ GCC_except_table4301
+ GCC_except_table4389
+ GCC_except_table4456
+ GCC_except_table4477
+ GCC_except_table4490
+ GCC_except_table4587
+ GCC_except_table4592
+ GCC_except_table4633
+ GCC_except_table4679
+ GCC_except_table4681
+ GCC_except_table4777
+ GCC_except_table4797
+ GCC_except_table4799
+ GCC_except_table4801
+ GCC_except_table4808
+ GCC_except_table4847
+ GCC_except_table4848
+ GCC_except_table4852
+ GCC_except_table4897
+ GCC_except_table4918
+ GCC_except_table4991
+ GCC_except_table5310
+ GCC_except_table5322
+ GCC_except_table5323
+ GCC_except_table5378
+ GCC_except_table5384
+ GCC_except_table5385
+ GCC_except_table5394
+ GCC_except_table5403
+ GCC_except_table5418
+ GCC_except_table5419
+ GCC_except_table5420
+ GCC_except_table5429
+ GCC_except_table5430
+ GCC_except_table5437
+ GCC_except_table5446
+ GCC_except_table5453
+ GCC_except_table5526
+ GCC_except_table5527
+ GCC_except_table5633
+ GCC_except_table5634
+ GCC_except_table5635
+ GCC_except_table5654
+ GCC_except_table5659
+ GCC_except_table5660
+ GCC_except_table5661
+ GCC_except_table5687
+ GCC_except_table5764
+ GCC_except_table5765
+ GCC_except_table5766
+ _OBJC_IVAR_$_NEIKEv2EncryptedPayload._authenticatedHeaders
+ _OBJC_IVAR_$_NEIKEv2EncryptedPayload._nextPayload
+ _OBJC_IVAR_$_NEIKEv2Session._pendingPrivateNotifies
+ ___Block_byref_object_copy_.11491
+ ___Block_byref_object_copy_.13887
+ ___Block_byref_object_copy_.19874
+ ___Block_byref_object_copy_.20909
+ ___Block_byref_object_copy_.22041
+ ___Block_byref_object_copy_.22687
+ ___Block_byref_object_copy_.24980
+ ___Block_byref_object_dispose_.11492
+ ___Block_byref_object_dispose_.13888
+ ___Block_byref_object_dispose_.19875
+ ___Block_byref_object_dispose_.20910
+ ___Block_byref_object_dispose_.22042
+ ___Block_byref_object_dispose_.22688
+ ___Block_byref_object_dispose_.24981
+ ___block_descriptor_tmp.18.23504
+ ___block_descriptor_tmp.18110
+ ___block_descriptor_tmp.21602
+ ___block_descriptor_tmp.23440
+ ___block_descriptor_tmp.24029
+ ___block_literal_global.10.14282
+ ___block_literal_global.11782
+ ___block_literal_global.12.23662
+ ___block_literal_global.12152
+ ___block_literal_global.13040
+ ___block_literal_global.13203
+ ___block_literal_global.13889
+ ___block_literal_global.14.20384
+ ___block_literal_global.14284
+ ___block_literal_global.14850
+ ___block_literal_global.15089
+ ___block_literal_global.15572
+ ___block_literal_global.16323
+ ___block_literal_global.16458
+ ___block_literal_global.16761
+ ___block_literal_global.17.13052
+ ___block_literal_global.17.16449
+ ___block_literal_global.18036
+ ___block_literal_global.18673
+ ___block_literal_global.18936
+ ___block_literal_global.19971
+ ___block_literal_global.20.16455
+ ___block_literal_global.20389
+ ___block_literal_global.20784
+ ___block_literal_global.21529
+ ___block_literal_global.21600
+ ___block_literal_global.22142
+ ___block_literal_global.22253
+ ___block_literal_global.22287
+ ___block_literal_global.22467
+ ___block_literal_global.23385
+ ___block_literal_global.23438
+ ___block_literal_global.23666
+ ___block_literal_global.23754
+ ___block_literal_global.24135
+ ___block_literal_global.24526
+ ___block_literal_global.24698
+ ___block_literal_global.24948
+ ___block_literal_global.25469
+ ___block_literal_global.26034
+ ___block_literal_global.28.24984
+ ___block_literal_global.4.13043
+ ___block_literal_global.62.18668
+ ___block_literal_global.65.23922
+ ___block_literal_global.7.23376
+ ___block_literal_global.71.23749
+ __extensionAuxiliaryHostProtocol.protocol.18669
+ __extensionAuxiliaryHostProtocol.protocol.22288
+ __extensionAuxiliaryHostProtocol.protocol.23750
+ __extensionAuxiliaryHostProtocol.protocolInit.18667
+ __extensionAuxiliaryHostProtocol.protocolInit.22286
+ __extensionAuxiliaryHostProtocol.protocolInit.23748
+ __extensionAuxiliaryVendorProtocol.protocol.18674
+ __extensionAuxiliaryVendorProtocol.protocol.23755
+ __extensionAuxiliaryVendorProtocol.protocolInit.18672
+ __extensionAuxiliaryVendorProtocol.protocolInit.23753
+ __unnamed_array_storage.19975
+ __unnamed_array_storage.20923
+ __unnamed_array_storage.26742
+ _convert_error_to_string.22684
+ _driverInterface.driverInterface.15573
+ _driverInterface.driverInterface.18933
+ _driverInterface.driverInterface.20385
+ _driverInterface.onceToken.15571
+ _driverInterface.onceToken.18932
+ _driverInterface.onceToken.20383
+ _g_noAppFilter.25997
+ _globalConfigurationManager.gChangeQueue.16453
+ _globalConfigurationManager.gConfigurationManager.16450
+ _globalConfigurationManager.onceToken.16448
+ _initGlobals.onceToken.15088
+ _loadedManagers.loadedManagers.24946
+ _loadedManagers.loadedManagers.26000
+ _loadedManagers.managers_init.24945
+ _loadedManagers.managers_init.25999
+ _managerInterface.managerInterface.18937
+ _managerInterface.managerInterface.20390
+ _managerInterface.onceToken.18935
+ _managerInterface.onceToken.20388
+ _sharedManager.onceToken.16457
+ _sharedManager.onceToken.26033
- +[NEIKEv2Packet createPacketFromReceivedData:ikeSA:]
- -[NEIKEv2EncryptedFragmentPayload .cxx_destruct]
- -[NEIKEv2Packet copyReceivedPacketForIKESA:]
- -[NEIKEv2Packet decrypted]
- -[NEIKEv2Packet fragmentNumber]
- -[NEIKEv2Packet isFragmented]
- -[NEIKEv2Packet totalFragments]
- -[NEIKEv2ResponseConfigPayload initWithResponseConfigPayload:configRequest:]
- GCC_except_table2792
- GCC_except_table2798
- GCC_except_table2801
- GCC_except_table2817
- GCC_except_table2818
- GCC_except_table2819
- GCC_except_table2834
- GCC_except_table2848
- GCC_except_table2849
- GCC_except_table2891
- GCC_except_table2895
- GCC_except_table2940
- GCC_except_table2988
- GCC_except_table3039
- GCC_except_table3053
- GCC_except_table3064
- GCC_except_table3077
- GCC_except_table3078
- GCC_except_table3079
- GCC_except_table3096
- GCC_except_table3135
- GCC_except_table3141
- GCC_except_table3175
- GCC_except_table3176
- GCC_except_table3261
- GCC_except_table3283
- GCC_except_table3518
- GCC_except_table3525
- GCC_except_table3527
- GCC_except_table3612
- GCC_except_table3756
- GCC_except_table3767
- GCC_except_table3773
- GCC_except_table3794
- GCC_except_table3795
- GCC_except_table3796
- GCC_except_table3800
- GCC_except_table3805
- GCC_except_table3806
- GCC_except_table3812
- GCC_except_table3819
- GCC_except_table3820
- GCC_except_table3892
- GCC_except_table3893
- GCC_except_table3901
- GCC_except_table3997
- GCC_except_table3999
- GCC_except_table4001
- GCC_except_table4081
- GCC_except_table4248
- GCC_except_table4258
- GCC_except_table4262
- GCC_except_table4274
- GCC_except_table4294
- GCC_except_table4296
- GCC_except_table4302
- GCC_except_table4304
- GCC_except_table4392
- GCC_except_table4459
- GCC_except_table4480
- GCC_except_table4493
- GCC_except_table4590
- GCC_except_table4595
- GCC_except_table4636
- GCC_except_table4682
- GCC_except_table4684
- GCC_except_table4780
- GCC_except_table4800
- GCC_except_table4802
- GCC_except_table4804
- GCC_except_table4811
- GCC_except_table4851
- GCC_except_table4853
- GCC_except_table4858
- GCC_except_table4900
- GCC_except_table4924
- GCC_except_table4994
- GCC_except_table5313
- GCC_except_table5325
- GCC_except_table5329
- GCC_except_table5381
- GCC_except_table5387
- GCC_except_table5388
- GCC_except_table5400
- GCC_except_table5406
- GCC_except_table5426
- GCC_except_table5427
- GCC_except_table5431
- GCC_except_table5432
- GCC_except_table5433
- GCC_except_table5440
- GCC_except_table5452
- GCC_except_table5456
- GCC_except_table5529
- GCC_except_table5530
- GCC_except_table5646
- GCC_except_table5647
- GCC_except_table5648
- GCC_except_table5657
- GCC_except_table5662
- GCC_except_table5663
- GCC_except_table5664
- GCC_except_table5690
- GCC_except_table5768
- GCC_except_table5769
- GCC_except_table5770
- _OBJC_IVAR_$_NEIKEv2EncryptedFragmentPayload._fragmentData
- _OBJC_IVAR_$_NEIKEv2EncryptedFragmentPayload._nextPayload
- _OBJC_IVAR_$_NEIKEv2EncryptedPayload._encryptedData
- __OBJC_$_PROP_LIST_NEIKEv2Packet
- ___Block_byref_object_copy_.11593
- ___Block_byref_object_copy_.13983
- ___Block_byref_object_copy_.19909
- ___Block_byref_object_copy_.20942
- ___Block_byref_object_copy_.22073
- ___Block_byref_object_copy_.22719
- ___Block_byref_object_copy_.24966
- ___Block_byref_object_dispose_.11594
- ___Block_byref_object_dispose_.13984
- ___Block_byref_object_dispose_.19910
- ___Block_byref_object_dispose_.20943
- ___Block_byref_object_dispose_.22074
- ___Block_byref_object_dispose_.22720
- ___Block_byref_object_dispose_.24967
- ___block_descriptor_tmp.18.23490
- ___block_descriptor_tmp.18172
- ___block_descriptor_tmp.21634
- ___block_descriptor_tmp.23426
- ___block_descriptor_tmp.24015
- ___block_literal_global.10.14349
- ___block_literal_global.11885
- ___block_literal_global.12.23648
- ___block_literal_global.12252
- ___block_literal_global.13130
- ___block_literal_global.13293
- ___block_literal_global.13985
- ___block_literal_global.14.20418
- ___block_literal_global.14351
- ___block_literal_global.14914
- ___block_literal_global.15152
- ___block_literal_global.15636
- ___block_literal_global.16386
- ___block_literal_global.16521
- ___block_literal_global.16823
- ___block_literal_global.17.13142
- ___block_literal_global.17.16512
- ___block_literal_global.18098
- ___block_literal_global.18713
- ___block_literal_global.18977
- ___block_literal_global.20.16518
- ___block_literal_global.20006
- ___block_literal_global.20423
- ___block_literal_global.20818
- ___block_literal_global.21561
- ___block_literal_global.21632
- ___block_literal_global.22174
- ___block_literal_global.22285
- ___block_literal_global.22319
- ___block_literal_global.22499
- ___block_literal_global.23371
- ___block_literal_global.23424
- ___block_literal_global.23652
- ___block_literal_global.23740
- ___block_literal_global.24121
- ___block_literal_global.24512
- ___block_literal_global.24684
- ___block_literal_global.24934
- ___block_literal_global.25456
- ___block_literal_global.26019
- ___block_literal_global.28.24970
- ___block_literal_global.4.13133
- ___block_literal_global.62.18708
- ___block_literal_global.65.23908
- ___block_literal_global.7.23362
- ___block_literal_global.71.23735
- __extensionAuxiliaryHostProtocol.protocol.18709
- __extensionAuxiliaryHostProtocol.protocol.22320
- __extensionAuxiliaryHostProtocol.protocol.23736
- __extensionAuxiliaryHostProtocol.protocolInit.18707
- __extensionAuxiliaryHostProtocol.protocolInit.22318
- __extensionAuxiliaryHostProtocol.protocolInit.23734
- __extensionAuxiliaryVendorProtocol.protocol.18714
- __extensionAuxiliaryVendorProtocol.protocol.23741
- __extensionAuxiliaryVendorProtocol.protocolInit.18712
- __extensionAuxiliaryVendorProtocol.protocolInit.23739
- __unnamed_array_storage.20010
- __unnamed_array_storage.20956
- __unnamed_array_storage.26727
- _convert_error_to_string.22716
- _driverInterface.driverInterface.15637
- _driverInterface.driverInterface.18974
- _driverInterface.driverInterface.20419
- _driverInterface.onceToken.15635
- _driverInterface.onceToken.18973
- _driverInterface.onceToken.20417
- _g_noAppFilter.25982
- _globalConfigurationManager.gChangeQueue.16516
- _globalConfigurationManager.gConfigurationManager.16513
- _globalConfigurationManager.onceToken.16511
- _initGlobals.onceToken.15151
- _loadedManagers.loadedManagers.24932
- _loadedManagers.loadedManagers.25985
- _loadedManagers.managers_init.24931
- _loadedManagers.managers_init.25984
- _managerInterface.managerInterface.18978
- _managerInterface.managerInterface.20424
- _managerInterface.onceToken.18976
- _managerInterface.onceToken.20422
- _objc_msgSend$decrypted
- _objc_msgSend$fragmentNumber
- _objc_msgSend$isFragmented
- _objc_msgSend$totalFragments
- _sharedManager.onceToken.16520
- _sharedManager.onceToken.26018
CStrings:
+ "%s called with null self.decrypted"
+ "%s called with null self.encryptedPayload.payloadData"
+ "+[NEIKEv2Packet createPacketFromReceivedData:]"
+ "-[NEIKEv2EncryptedPayload decryptPayloadsForEncryption:integrity:encryptionKey:integrityKey:]"
+ "-[NEIKEv2Packet processDecryptedPacketForIKESA:]"
+ "1\x14/\f\x11\x11%"
+ "BACKTRACE Bad digest lengths %u != %u"
+ "BACKTRACE Padded len (%zu) > decrypted data len (%zu)"
+ "CC decrypt failed (status %d, bytes %zu)"
+ "Cannot decrypt, encrypted data length %u too short"
+ "Cannot decrypt, encrypted data length %zu too short"
+ "Cannot parse packet, no acceptable payloads found"
+ "Failed to decrypt packet"
+ "Failed to decrypt packet: Bad digest"
+ "Unencrypted critical payload type %u is not permitted for packet type %u"
+ "Unencrypted payload type %u is not permitted for packet type %u"
+ "_authenticatedHeaders"
+ "_pendingPrivateNotifies"
- "%s called with null receivedCreateChildSA"
- "%s called with null receivedDelete"
- "%s called with null receivedIKESAInit"
- "%s called with null receivedRekeyChildSA"
- "%s called with null receivedRekeyIKESA"
- "+[NEIKEv2Packet createPacketFromReceivedData:ikeSA:]"
- "-[NEIKEv2EncryptedPayload copyDecryptedPayloadsForEncryption:integrity:encryptionKey:integrityKey:packetData:]"
- "1\x14/\f\x11\x11$"
- "BACKTRACE Bad checksum lengths %u != %u"
- "BACKTRACE Padded len (%zu) > payload data len (%zu)"
- "CC decrypt failed (status %d, bytes %ld)"
- "Cannot decrypted, encrypted data length %u too short"
- "Decrypted fragment %u/%u"
- "Failed to decrypt packet\n"
- "Failed to decrypt packet: Bad checksum"
- "Failed to decrypt payload data, discarding"
- "_encryptedData"
- "_fragmentData"
- "decrypted"
- "fragmentNumber"
- "isFragmented"
- "totalFragments"

```
