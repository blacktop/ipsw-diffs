## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

```diff

-720.35.0.0.0
-  __TEXT.__text: 0x121034
-  __TEXT.__auth_stubs: 0x2e70
-  __TEXT.__objc_methlist: 0x90b0
-  __TEXT.__const: 0x2220
-  __TEXT.__gcc_except_tab: 0x18f4
-  __TEXT.__cstring: 0x25ce2
+730.4.0.0.0
+  __TEXT.__text: 0x122408
+  __TEXT.__auth_stubs: 0x2f10
+  __TEXT.__objc_methlist: 0x9110
+  __TEXT.__const: 0x2248
+  __TEXT.__gcc_except_tab: 0x1958
+  __TEXT.__cstring: 0x25ec8
   __TEXT.__oslogstring: 0x1ee
-  __TEXT.__unwind_info: 0x3cb0
+  __TEXT.__unwind_info: 0x3cec
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0xe36
-  __TEXT.__objc_methname: 0x15e39
-  __TEXT.__objc_methtype: 0x49b2
-  __TEXT.__objc_stubs: 0xa8a0
-  __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0x2f88
+  __TEXT.__objc_classname: 0xe37
+  __TEXT.__objc_methname: 0x15f57
+  __TEXT.__objc_methtype: 0x49e9
+  __TEXT.__objc_stubs: 0xa940
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x3000
   __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15890
-  __DATA_CONST.__objc_selrefs: 0x44d0
-  __AUTH_CONST.__cfstring: 0x46c0
+  __DATA_CONST.__objc_const: 0x15900
+  __DATA_CONST.__objc_selrefs: 0x4518
+  __AUTH_CONST.__cfstring: 0x4740
   __AUTH_CONST.__const: 0x1ff8
   __AUTH_CONST.__objc_const: 0x25f8
   __AUTH_CONST.__objc_intobj: 0x300
-  __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0x1748
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__auth_got: 0x1798
   __AUTH.__objc_data: 0x21c0
   __AUTH.__data: 0xbb0
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x330
   __DATA.__objc_superrefs: 0x260
-  __DATA.__objc_ivar: 0x1710
-  __DATA.__data: 0x3eb0
+  __DATA.__objc_ivar: 0x1718
+  __DATA.__data: 0x3ed0
   __DATA.__common: 0x22
-  __DATA.__bss: 0xdd0
+  __DATA.__bss: 0xdb0
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x178
   __DATA_DIRTY.__bss: 0x218
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreUtilsExtras.framework/CoreUtilsExtras

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6087
-  Symbols:   17381
-  CStrings:  10083
+  Functions: 6102
+  Symbols:   17434
+  CStrings:  10119
 
Symbols:
+ -[CUNetInterfaceMonitor _ensureStartedNW]
+ -[CUNetInterfaceMonitor _ensureStartedSC]
+ -[CUNetInterfaceMonitor _primaryIPChangedNW:]
+ -[CUPairedPeer groupInfo]
+ -[CUPairingManager getPairedPeersWithGroupID:options:completion:]
+ -[CUPairingManager updatePairedPeersWithGroupID:groupInfo:options:completion:]
+ -[CUPairingSession groupInfoPeer]
+ -[CUPairingSession groupInfoSelf]
+ -[CUPairingSession setGroupInfoSelf:]
+ GCC_except_table2773
+ GCC_except_table2777
+ GCC_except_table2954
+ GCC_except_table2956
+ GCC_except_table2973
+ GCC_except_table2980
+ GCC_except_table2982
+ GCC_except_table3049
+ GCC_except_table3384
+ GCC_except_table3385
+ GCC_except_table3473
+ GCC_except_table3495
+ GCC_except_table3567
+ GCC_except_table3570
+ GCC_except_table3571
+ GCC_except_table3573
+ GCC_except_table3854
+ GCC_except_table4262
+ GCC_except_table4508
+ GCC_except_table4516
+ GCC_except_table4666
+ GCC_except_table4670
+ GCC_except_table4672
+ GCC_except_table4674
+ GCC_except_table4697
+ GCC_except_table4774
+ GCC_except_table4776
+ GCC_except_table4778
+ GCC_except_table4780
+ GCC_except_table4782
+ GCC_except_table4784
+ GCC_except_table4788
+ GCC_except_table4790
+ GCC_except_table4802
+ GCC_except_table4809
+ GCC_except_table4811
+ GCC_except_table4812
+ GCC_except_table4814
+ GCC_except_table4818
+ GCC_except_table4840
+ GCC_except_table4844
+ GCC_except_table4846
+ GCC_except_table4847
+ GCC_except_table4848
+ GCC_except_table4849
+ GCC_except_table4850
+ GCC_except_table4851
+ GCC_except_table4852
+ GCC_except_table4853
+ GCC_except_table4854
+ GCC_except_table4856
+ GCC_except_table4857
+ GCC_except_table4858
+ GCC_except_table4860
+ GCC_except_table5503
+ GCC_except_table5511
+ GCC_except_table5520
+ GCC_except_table5528
+ GCC_except_table5867
+ GCC_except_table5868
+ GCC_except_table5881
+ _ACAccountStoreFunction.9876
+ _AKAccountManagerFunction.9865
+ _AccountsLibrary.sLib.9879
+ _AccountsLibrary.sOnce.9873
+ _AppleAccountLibrary.sLib.9882
+ _AppleAccountLibrary.sOnce.9869
+ _AuthKitLibrary.sLib.9868
+ _AuthKitLibrary.sOnce.9862
+ _CALayerFunction.14821
+ _CATransactionFunction.14838
+ _CoreAnalyticsLibrary.sLib.10288
+ _CoreAnalyticsLibrary.sOnce.10286
+ _CoreHAPLibrary.sLib.7295
+ _CoreHAPLibrary.sOnce.7289
+ _HAPSystemKeychainStoreFunction.7292
+ _MobileCoreServicesLibrary.sLib.15360
+ _MobileCoreServicesLibrary.sOnce.15359
+ _OBJC_IVAR_$_CUNetInterfaceMonitor._nwPathEvaluator
+ _OBJC_IVAR_$_CUPairingSession._groupInfoSelf
+ _QuartzCoreLibrary.sLib.14786
+ _QuartzCoreLibrary.sOnce.14784
+ _RapportLibrary.sLib.7308
+ _RapportLibrary.sOnce.7303
+ _VideoToolboxLibrary.sLib.14793
+ _VideoToolboxLibrary.sOnce.14792
+ __NetTransportFinalize.13645
+ __NetTransportFinalize.13653
+ __NetTransportInitialize.13646
+ __NetTransportInitialize.13656
+ __NetTransportRead.13642
+ __NetTransportRead.13655
+ __NetTransportWriteV.13641
+ __NetTransportWriteV.13654
+ ___41-[CUNetInterfaceMonitor _ensureStartedNW]_block_invoke
+ ___65-[CUPairingManager getPairedPeersWithGroupID:options:completion:]_block_invoke
+ ___78-[CUPairingManager updatePairedPeersWithGroupID:groupInfo:options:completion:]_block_invoke
+ ___78-[CUPairingManager updatePairedPeersWithGroupID:groupInfo:options:completion:]_block_invoke.73
+ ___78-[CUPairingManager updatePairedPeersWithGroupID:groupInfo:options:completion:]_block_invoke_2
+ ___AccountsLibrary_block_invoke.9878
+ ___AppleAccountLibrary_block_invoke.9881
+ ___AuthKitLibrary_block_invoke.9867
+ ___Block_byref_object_copy_.10638
+ ___Block_byref_object_copy_.12049
+ ___Block_byref_object_copy_.12639
+ ___Block_byref_object_copy_.14214
+ ___Block_byref_object_copy_.7251
+ ___Block_byref_object_copy_.7582
+ ___Block_byref_object_dispose_.10639
+ ___Block_byref_object_dispose_.12050
+ ___Block_byref_object_dispose_.12640
+ ___Block_byref_object_dispose_.14215
+ ___Block_byref_object_dispose_.7252
+ ___Block_byref_object_dispose_.7583
+ ___CoreAnalyticsLibrary_block_invoke.10326
+ ___CoreHAPLibrary_block_invoke.7294
+ ___MobileCoreServicesLibrary_block_invoke.15363
+ ___QuartzCoreLibrary_block_invoke.14790
+ ___RapportLibrary_block_invoke.7307
+ ___VideoToolboxLibrary_block_invoke.14796
+ ___block_descriptor_40_e8_32w_e30_v16?0"NSObject<OS_nw_path>"8lw32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_tmp.13348
+ ___block_descriptor_tmp.13394
+ ___block_descriptor_tmp.16323
+ ___block_descriptor_tmp.3.16333
+ ___block_descriptor_tmp.7.16328
+ ___block_literal_global.10287
+ ___block_literal_global.10883
+ ___block_literal_global.11131
+ ___block_literal_global.1128.9984
+ ___block_literal_global.11308
+ ___block_literal_global.11845
+ ___block_literal_global.12084
+ ___block_literal_global.13186
+ ___block_literal_global.13335
+ ___block_literal_global.13428
+ ___block_literal_global.14785
+ ___block_literal_global.15289
+ ___block_literal_global.16165
+ ___block_literal_global.16326
+ ___block_literal_global.224.9901
+ ___block_literal_global.237.9897
+ ___block_literal_global.256.12417
+ ___block_literal_global.256.12624
+ ___block_literal_global.29.9991
+ ___block_literal_global.320.9822
+ ___block_literal_global.329.9815
+ ___block_literal_global.33.9992
+ ___block_literal_global.41.9993
+ ___block_literal_global.47.9995
+ ___block_literal_global.52.9997
+ ___block_literal_global.58.9998
+ ___block_literal_global.6845
+ ___block_literal_global.7304
+ ___block_literal_global.8042
+ ___block_literal_global.8198
+ ___block_literal_global.8631
+ ___block_literal_global.8921
+ ___block_literal_global.9623
+ ___block_literal_global.9990
+ _classACAccountStore.9874
+ _classAKAccountManager.9863
+ _classCALayer.14819
+ _classCATransaction.14836
+ _classHAPSystemKeychainStore.7290
+ _gCFArrayType.14012
+ _gCFBooleanType.14010
+ _gCFDataType.14013
+ _gCFDateType.14014
+ _gCFDictionaryType.14011
+ _gCFNumberType.14009
+ _gCFStringType.14008
+ _getACAccountStoreClass.9870
+ _getAKAccountManagerClass.9855
+ _getCALayerClass.14800
+ _getCATransactionClass.14826
+ _getHAPSystemKeychainStoreClass.7286
+ _initACAccountStore.9872
+ _initAKAccountManager.9861
+ _initAnalyticsSendEvent.10304
+ _initCALayer.14817
+ _initCATransaction.14834
+ _initHAPSystemKeychainStore.7288
+ _kWiFiNetworkStandaloneKey
+ _nw_interface_get_name
+ _nw_parameters_create
+ _nw_parameters_prohibit_interface_type
+ _nw_parameters_set_avoided_netagent_classes
+ _nw_path_copy_interface
+ _nw_path_create_evaluator_for_endpoint
+ _nw_path_evaluator_cancel
+ _nw_path_evaluator_copy_path
+ _nw_path_evaluator_set_update_handler
+ _nw_path_get_status
+ _objc_msgSend$_ensureStartedNW
+ _objc_msgSend$_ensureStartedSC
+ _objc_msgSend$_primaryIPChangedNW:
+ _objc_msgSend$getPairedPeersWithGroupID:options:completion:
+ _objc_msgSend$groupInfo
+ _softLinkAnalyticsSendEvent.10302
- -[CUNetInterfaceMonitor _ensureStarted]
- GCC_except_table2772
- GCC_except_table2947
- GCC_except_table2948
- GCC_except_table2958
- GCC_except_table2977
- GCC_except_table2979
- GCC_except_table3369
- GCC_except_table3370
- GCC_except_table3458
- GCC_except_table3480
- GCC_except_table3552
- GCC_except_table3555
- GCC_except_table3556
- GCC_except_table3558
- GCC_except_table3839
- GCC_except_table4247
- GCC_except_table4493
- GCC_except_table4501
- GCC_except_table4651
- GCC_except_table4655
- GCC_except_table4657
- GCC_except_table4659
- GCC_except_table4682
- GCC_except_table4758
- GCC_except_table4759
- GCC_except_table4760
- GCC_except_table4761
- GCC_except_table4763
- GCC_except_table4765
- GCC_except_table4767
- GCC_except_table4769
- GCC_except_table4787
- GCC_except_table4794
- GCC_except_table4796
- GCC_except_table4797
- GCC_except_table4799
- GCC_except_table4800
- GCC_except_table4801
- GCC_except_table4803
- GCC_except_table4804
- GCC_except_table4805
- GCC_except_table4806
- GCC_except_table4807
- GCC_except_table4808
- GCC_except_table4824
- GCC_except_table4825
- GCC_except_table4827
- GCC_except_table4828
- GCC_except_table4829
- GCC_except_table4832
- GCC_except_table4833
- GCC_except_table4841
- GCC_except_table5488
- GCC_except_table5496
- GCC_except_table5505
- GCC_except_table5513
- GCC_except_table5852
- GCC_except_table5853
- GCC_except_table5866
- _ACAccountStoreFunction.9827
- _AKAccountManagerFunction.9816
- _AccountsLibrary.sLib.9830
- _AccountsLibrary.sOnce.9824
- _AppleAccountLibrary.sLib.9833
- _AppleAccountLibrary.sOnce.9820
- _AuthKitLibrary.sLib.9819
- _AuthKitLibrary.sOnce.9813
- _CALayerFunction.14773
- _CATransactionFunction.14790
- _CoreAnalyticsLibrary.sLib.10240
- _CoreAnalyticsLibrary.sOnce.10238
- _CoreHAPLibrary.sLib.7273
- _CoreHAPLibrary.sOnce.7267
- _HAPSystemKeychainStoreFunction.7270
- _MobileCoreServicesLibrary.sLib.15312
- _MobileCoreServicesLibrary.sOnce.15311
- _QuartzCoreLibrary.sLib.14738
- _QuartzCoreLibrary.sOnce.14736
- _RapportLibrary.sLib.7286
- _RapportLibrary.sOnce.7281
- _VideoToolboxLibrary.sLib.14745
- _VideoToolboxLibrary.sOnce.14744
- __NetTransportFinalize.13598
- __NetTransportFinalize.13606
- __NetTransportInitialize.13599
- __NetTransportInitialize.13609
- __NetTransportRead.13595
- __NetTransportRead.13608
- __NetTransportWriteV.13594
- __NetTransportWriteV.13607
- ___AccountsLibrary_block_invoke.9829
- ___AppleAccountLibrary_block_invoke.9832
- ___AuthKitLibrary_block_invoke.9818
- ___Block_byref_object_copy_.10591
- ___Block_byref_object_copy_.12004
- ___Block_byref_object_copy_.12594
- ___Block_byref_object_copy_.14164
- ___Block_byref_object_copy_.7229
- ___Block_byref_object_dispose_.10592
- ___Block_byref_object_dispose_.12005
- ___Block_byref_object_dispose_.12595
- ___Block_byref_object_dispose_.14165
- ___Block_byref_object_dispose_.7230
- ___CoreAnalyticsLibrary_block_invoke.10279
- ___CoreHAPLibrary_block_invoke.7272
- ___MobileCoreServicesLibrary_block_invoke.15315
- ___QuartzCoreLibrary_block_invoke.14742
- ___RapportLibrary_block_invoke.7285
- ___VideoToolboxLibrary_block_invoke.14748
- ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_tmp.13303
- ___block_descriptor_tmp.13349
- ___block_descriptor_tmp.16274
- ___block_descriptor_tmp.3.16284
- ___block_descriptor_tmp.7.16279
- ___block_literal_global.10239
- ___block_literal_global.10838
- ___block_literal_global.11087
- ___block_literal_global.11264
- ___block_literal_global.1128.9936
- ___block_literal_global.11799
- ___block_literal_global.12039
- ___block_literal_global.13141
- ___block_literal_global.13290
- ___block_literal_global.13383
- ___block_literal_global.14737
- ___block_literal_global.15241
- ___block_literal_global.16119
- ___block_literal_global.16277
- ___block_literal_global.224.9852
- ___block_literal_global.237.9848
- ___block_literal_global.256.12372
- ___block_literal_global.256.12579
- ___block_literal_global.29.9943
- ___block_literal_global.320.9774
- ___block_literal_global.329.9767
- ___block_literal_global.33.9944
- ___block_literal_global.41.9945
- ___block_literal_global.47.9947
- ___block_literal_global.52.9949
- ___block_literal_global.58.9950
- ___block_literal_global.6823
- ___block_literal_global.7282
- ___block_literal_global.8007
- ___block_literal_global.8164
- ___block_literal_global.8597
- ___block_literal_global.8878
- ___block_literal_global.9580
- ___block_literal_global.9942
- _classACAccountStore.9825
- _classAKAccountManager.9814
- _classCALayer.14771
- _classCATransaction.14788
- _classHAPSystemKeychainStore.7268
- _gCFArrayType.13963
- _gCFBooleanType.13961
- _gCFDataType.13964
- _gCFDateType.13965
- _gCFDictionaryType.13962
- _gCFNumberType.13960
- _gCFStringType.13959
- _getACAccountStoreClass.9821
- _getAKAccountManagerClass.9806
- _getCALayerClass.14752
- _getCATransactionClass.14778
- _getHAPSystemKeychainStoreClass.7264
- _initACAccountStore.9823
- _initAKAccountManager.9812
- _initAnalyticsSendEvent.10257
- _initCALayer.14769
- _initCATransaction.14786
- _initHAPSystemKeychainStore.7266
- _softLinkAnalyticsSendEvent.10255
CStrings:
+ "\x119"
+ "\x11E\x1f\t"
+ "### Get interface addresses failed: interface=%s, error=%@"
+ "### No NW path"
+ "### No interface name"
+ "### No primary interface"
+ "-[CUNetInterfaceMonitor _ensureStartedNW]"
+ "-[CUNetInterfaceMonitor _ensureStartedSC]"
+ "-[CUNetInterfaceMonitor _primaryIPChangedNW:]"
+ "@\"NSObject<OS_nw_path_evaluator>\""
+ "AppVPN"
+ "Monitoring start NW"
+ "Monitoring start SC"
+ "Monitoring stop NW"
+ "Monitoring stop SC"
+ "NetworkExtension"
+ "Path not satisfied"
+ "Primary IPs %s: interface=%s, IPv4=%@, IPv6=%@ %s"
+ "T@\"NSDictionary\",C,N,V_groupInfoSelf"
+ "VPN"
+ "_ensureStartedNW"
+ "_ensureStartedSC"
+ "_groupInfoSelf"
+ "_nwPathEvaluator"
+ "_primaryIPChangedNW:"
+ "changed"
+ "getPairedPeersWithGroupID:options:completion:"
+ "groupInfo"
+ "groupInfoPeer"
+ "groupInfoSelf"
+ "setGroupInfoSelf:"
+ "standalone6G"
+ "unchanged"
+ "updatePairedPeersWithGroupID:groupInfo:options:completion:"
+ "v16@?0@\"NSObject<OS_nw_path>\"8"
+ "v48@0:8@16@24Q32@?40"
- "\x11E\x1f\b"
- "-[CUNetInterfaceMonitor _ensureStarted]"

```
