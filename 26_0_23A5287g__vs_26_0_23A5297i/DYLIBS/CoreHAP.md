## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1340.3.0.0.0
-  __TEXT.__text: 0x1a7e28
+1345.1.0.1.1
+  __TEXT.__text: 0x1a8a20
   __TEXT.__auth_stubs: 0x1570
-  __TEXT.__objc_methlist: 0x13840
-  __TEXT.__const: 0x700
+  __TEXT.__objc_methlist: 0x13860
+  __TEXT.__const: 0x710
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__gcc_except_tab: 0x63b4
-  __TEXT.__cstring: 0x10a3b
-  __TEXT.__oslogstring: 0x20050
-  __TEXT.__unwind_info: 0x5d78
+  __TEXT.__cstring: 0x11066
+  __TEXT.__oslogstring: 0x200d1
+  __TEXT.__unwind_info: 0x5d70
   __TEXT.__objc_classname: 0x2e07
-  __TEXT.__objc_methname: 0x26757
-  __TEXT.__objc_methtype: 0x8fc0
-  __TEXT.__objc_stubs: 0x186c0
+  __TEXT.__objc_methname: 0x267b1
+  __TEXT.__objc_methtype: 0x8fd0
+  __TEXT.__objc_stubs: 0x186a0
   __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__const: 0x5010
+  __DATA_CONST.__const: 0x50b8
   __DATA_CONST.__objc_classlist: 0x958
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ef8
+  __DATA_CONST.__objc_selrefs: 0x6ef0
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x7d8
   __DATA_CONST.__objc_arraydata: 0x208
   __AUTH_CONST.__auth_got: 0xac8
-  __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0xdb20
-  __AUTH_CONST.__objc_const: 0x22068
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0xdd20
+  __AUTH_CONST.__objc_const: 0x220b8
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x4e20
-  __DATA.__objc_ivar: 0x14e8
+  __DATA.__objc_ivar: 0x14f0
   __DATA.__data: 0x26c2
-  __DATA.__bss: 0x499
+  __DATA.__bss: 0x489
   __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xb8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: EB65A578-1281-3A9C-961A-66812086488D
-  Functions: 7483
-  Symbols:   24325
-  CStrings:  12870
+  UUID: 90D81602-EA0A-3152-97CF-27C13F76C888
+  Functions: 7484
+  Symbols:   24326
+  CStrings:  12937
 
Symbols:
+ +[HAP2EncodedRequestThread stringFromHAP2EncodedRequestType:]
+ -[HAP2AccessoryServerControllerOperation initWithName:controller:encoding:transport:request:endpoint:mimeType:timeout:options:dscpPriority:]
+ -[HAP2AccessoryServerControllerReadOperation initWithName:controller:encoding:transport:readRequest:endpoint:mimeType:timeout:options:dscpPriority:]
+ -[HAP2AccessoryServerControllerTimedWriteOperation initWithName:controller:encoding:transport:prepareRequest:executeRequest:endpoint:mimeType:timeout:options:dscpPriority:]
+ -[HAP2AccessoryServerTransportRequest dscpPriority]
+ -[HAP2AccessoryServerTransportRequest initForReadingWithEndpoint:data:encrypted:mimeType:dscpPriority:]
+ -[HAP2AccessoryServerTransportRequest initForWritingWithEndpoint:data:encrypted:mimeType:dscpPriority:]
+ -[HAP2AccessoryServerTransportRequest initWithEndpoint:data:encrypted:mimeType:forReading:dscpPriority:]
+ -[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]
+ GCC_except_table1434
+ GCC_except_table1640
+ GCC_except_table1643
+ GCC_except_table1651
+ GCC_except_table1653
+ GCC_except_table1659
+ GCC_except_table1661
+ GCC_except_table1665
+ GCC_except_table1669
+ GCC_except_table1671
+ GCC_except_table1676
+ GCC_except_table1680
+ GCC_except_table1690
+ GCC_except_table1698
+ GCC_except_table1705
+ GCC_except_table1709
+ GCC_except_table1713
+ GCC_except_table1717
+ GCC_except_table1719
+ GCC_except_table1868
+ GCC_except_table1873
+ GCC_except_table1875
+ GCC_except_table1877
+ GCC_except_table1886
+ GCC_except_table1888
+ GCC_except_table1892
+ GCC_except_table1895
+ GCC_except_table1897
+ GCC_except_table1900
+ GCC_except_table1917
+ GCC_except_table1920
+ GCC_except_table1922
+ GCC_except_table1924
+ GCC_except_table1928
+ GCC_except_table1931
+ GCC_except_table1935
+ GCC_except_table1937
+ GCC_except_table1940
+ GCC_except_table1943
+ GCC_except_table1945
+ GCC_except_table1947
+ GCC_except_table1951
+ GCC_except_table1955
+ GCC_except_table1963
+ GCC_except_table1974
+ GCC_except_table2012
+ GCC_except_table2018
+ GCC_except_table2189
+ GCC_except_table2196
+ GCC_except_table2202
+ GCC_except_table2208
+ GCC_except_table2211
+ GCC_except_table2214
+ GCC_except_table2217
+ GCC_except_table2223
+ GCC_except_table2225
+ GCC_except_table2230
+ GCC_except_table2232
+ GCC_except_table2328
+ GCC_except_table2341
+ GCC_except_table2356
+ GCC_except_table2370
+ GCC_except_table2450
+ GCC_except_table2462
+ GCC_except_table2488
+ GCC_except_table2496
+ GCC_except_table2507
+ GCC_except_table2521
+ GCC_except_table2524
+ GCC_except_table2529
+ GCC_except_table2537
+ GCC_except_table2543
+ GCC_except_table2545
+ GCC_except_table2719
+ GCC_except_table2769
+ GCC_except_table2785
+ GCC_except_table2788
+ GCC_except_table2803
+ GCC_except_table2810
+ GCC_except_table2825
+ GCC_except_table2838
+ GCC_except_table2840
+ GCC_except_table2846
+ GCC_except_table2853
+ GCC_except_table2856
+ GCC_except_table2861
+ GCC_except_table2917
+ GCC_except_table2920
+ GCC_except_table2925
+ GCC_except_table2927
+ GCC_except_table2941
+ GCC_except_table2955
+ GCC_except_table2957
+ GCC_except_table2961
+ GCC_except_table2969
+ GCC_except_table2977
+ GCC_except_table3026
+ GCC_except_table3034
+ GCC_except_table3037
+ GCC_except_table3060
+ GCC_except_table3304
+ GCC_except_table3369
+ GCC_except_table3373
+ GCC_except_table3376
+ GCC_except_table3379
+ GCC_except_table3382
+ GCC_except_table3384
+ GCC_except_table3391
+ GCC_except_table3401
+ GCC_except_table3404
+ GCC_except_table3416
+ GCC_except_table3418
+ GCC_except_table3420
+ GCC_except_table3423
+ GCC_except_table3426
+ GCC_except_table3428
+ GCC_except_table3431
+ GCC_except_table3434
+ GCC_except_table3446
+ GCC_except_table3448
+ GCC_except_table3452
+ GCC_except_table3456
+ GCC_except_table3460
+ GCC_except_table3486
+ GCC_except_table3504
+ GCC_except_table3508
+ GCC_except_table3511
+ GCC_except_table3513
+ GCC_except_table3515
+ GCC_except_table3603
+ GCC_except_table3640
+ GCC_except_table3666
+ GCC_except_table3757
+ GCC_except_table3764
+ GCC_except_table3782
+ GCC_except_table3786
+ GCC_except_table3789
+ GCC_except_table3792
+ GCC_except_table3795
+ GCC_except_table3798
+ GCC_except_table3801
+ GCC_except_table3804
+ GCC_except_table3807
+ GCC_except_table3810
+ GCC_except_table3815
+ GCC_except_table3825
+ GCC_except_table3828
+ GCC_except_table3839
+ GCC_except_table3847
+ GCC_except_table3851
+ GCC_except_table3859
+ GCC_except_table3864
+ GCC_except_table3882
+ GCC_except_table3884
+ GCC_except_table3887
+ GCC_except_table3890
+ GCC_except_table3896
+ GCC_except_table3899
+ GCC_except_table3901
+ GCC_except_table3907
+ GCC_except_table3909
+ GCC_except_table3912
+ GCC_except_table3924
+ GCC_except_table3935
+ GCC_except_table3937
+ GCC_except_table3946
+ GCC_except_table3952
+ GCC_except_table4212
+ GCC_except_table4218
+ GCC_except_table4235
+ GCC_except_table4239
+ GCC_except_table4256
+ GCC_except_table4262
+ GCC_except_table4275
+ GCC_except_table4289
+ GCC_except_table4293
+ GCC_except_table4406
+ GCC_except_table4470
+ GCC_except_table4478
+ GCC_except_table4488
+ GCC_except_table4525
+ GCC_except_table4531
+ GCC_except_table4618
+ GCC_except_table4625
+ GCC_except_table4627
+ GCC_except_table4634
+ GCC_except_table4637
+ GCC_except_table4639
+ GCC_except_table4644
+ GCC_except_table4647
+ GCC_except_table4650
+ GCC_except_table4654
+ GCC_except_table4658
+ GCC_except_table4688
+ GCC_except_table4707
+ GCC_except_table4717
+ GCC_except_table4720
+ GCC_except_table4725
+ GCC_except_table4728
+ GCC_except_table4992
+ GCC_except_table4996
+ GCC_except_table5030
+ GCC_except_table5034
+ GCC_except_table5036
+ GCC_except_table5038
+ GCC_except_table5205
+ GCC_except_table5211
+ GCC_except_table5217
+ GCC_except_table5218
+ GCC_except_table5224
+ GCC_except_table5259
+ GCC_except_table5260
+ GCC_except_table5280
+ GCC_except_table5292
+ GCC_except_table5295
+ GCC_except_table5302
+ GCC_except_table5316
+ GCC_except_table5518
+ GCC_except_table5530
+ GCC_except_table5535
+ GCC_except_table5538
+ GCC_except_table5541
+ GCC_except_table5544
+ GCC_except_table5574
+ GCC_except_table5596
+ GCC_except_table5600
+ GCC_except_table5604
+ GCC_except_table5609
+ GCC_except_table5613
+ GCC_except_table5617
+ GCC_except_table5621
+ GCC_except_table5625
+ GCC_except_table5637
+ GCC_except_table5700
+ GCC_except_table5701
+ GCC_except_table5760
+ GCC_except_table5764
+ GCC_except_table5765
+ GCC_except_table5777
+ GCC_except_table5783
+ GCC_except_table5796
+ GCC_except_table5799
+ GCC_except_table5800
+ GCC_except_table5805
+ GCC_except_table5808
+ GCC_except_table5815
+ GCC_except_table5818
+ GCC_except_table5832
+ GCC_except_table5839
+ GCC_except_table5845
+ GCC_except_table5856
+ GCC_except_table5860
+ GCC_except_table5861
+ GCC_except_table5879
+ GCC_except_table5888
+ GCC_except_table5903
+ GCC_except_table5904
+ GCC_except_table5909
+ GCC_except_table5913
+ GCC_except_table5914
+ GCC_except_table5917
+ GCC_except_table5923
+ GCC_except_table5927
+ GCC_except_table5935
+ GCC_except_table5939
+ GCC_except_table6091
+ GCC_except_table6147
+ GCC_except_table6150
+ GCC_except_table6154
+ GCC_except_table6160
+ GCC_except_table6167
+ GCC_except_table6168
+ GCC_except_table6184
+ GCC_except_table6189
+ GCC_except_table6190
+ GCC_except_table6239
+ GCC_except_table6242
+ GCC_except_table6245
+ GCC_except_table6273
+ GCC_except_table6278
+ GCC_except_table6298
+ GCC_except_table6317
+ GCC_except_table6325
+ GCC_except_table6332
+ GCC_except_table6346
+ GCC_except_table6349
+ GCC_except_table6355
+ GCC_except_table6361
+ GCC_except_table6374
+ GCC_except_table6379
+ GCC_except_table6388
+ GCC_except_table6395
+ GCC_except_table6399
+ GCC_except_table6407
+ GCC_except_table6411
+ GCC_except_table6413
+ GCC_except_table6417
+ GCC_except_table6438
+ GCC_except_table6441
+ GCC_except_table6467
+ GCC_except_table6631
+ GCC_except_table6694
+ GCC_except_table6726
+ GCC_except_table6729
+ GCC_except_table6895
+ GCC_except_table6958
+ GCC_except_table7022
+ GCC_except_table7028
+ GCC_except_table7074
+ GCC_except_table7076
+ GCC_except_table7078
+ GCC_except_table7080
+ GCC_except_table7082
+ GCC_except_table7084
+ GCC_except_table7086
+ GCC_except_table7088
+ GCC_except_table7090
+ GCC_except_table7092
+ GCC_except_table7094
+ GCC_except_table7097
+ GCC_except_table7099
+ GCC_except_table7101
+ GCC_except_table7104
+ GCC_except_table7130
+ GCC_except_table7134
+ GCC_except_table7175
+ GCC_except_table7178
+ GCC_except_table7182
+ GCC_except_table7185
+ GCC_except_table7187
+ GCC_except_table7192
+ GCC_except_table7196
+ GCC_except_table7244
+ GCC_except_table7251
+ GCC_except_table7345
+ GCC_except_table7361
+ GCC_except_table7363
+ GCC_except_table7365
+ GCC_except_table7368
+ GCC_except_table7370
+ GCC_except_table7372
+ GCC_except_table7375
+ GCC_except_table7377
+ GCC_except_table7381
+ GCC_except_table7386
+ _OBJC_IVAR_$_HAP2AccessoryServerControllerOperation._dscpPriority
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportRequest._dscpPriority
+ __CopyPairingIdentityDelegateCallback_f.15028
+ __CopyPairingIdentityDelegateCallback_f.21810
+ __CopyPairingIdentityDelegateCallback_f.2828
+ __FindPairedPeerDelegateCallback_f.2827
+ __PairSetupPromptForSetupCodeDelegateCallback_f.21812
+ __SavePairedPeerDelegateCallback_f.15027
+ __SavePairedPeerDelegateCallback_f.21806
+ ___77-[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]_block_invoke
+ ___77-[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]_block_invoke_2
+ ___87-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:dscpPriority:completion:]_block_invoke
+ ___87-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:dscpPriority:completion:]_block_invoke_2
+ ___Block_byref_object_copy_.10631
+ ___Block_byref_object_copy_.10929
+ ___Block_byref_object_copy_.11749
+ ___Block_byref_object_copy_.11946
+ ___Block_byref_object_copy_.12947
+ ___Block_byref_object_copy_.13684
+ ___Block_byref_object_copy_.13912
+ ___Block_byref_object_copy_.14938
+ ___Block_byref_object_copy_.17108
+ ___Block_byref_object_copy_.17327
+ ___Block_byref_object_copy_.18314
+ ___Block_byref_object_copy_.18930
+ ___Block_byref_object_copy_.20032
+ ___Block_byref_object_copy_.20842
+ ___Block_byref_object_copy_.2116
+ ___Block_byref_object_copy_.24952
+ ___Block_byref_object_copy_.25118
+ ___Block_byref_object_copy_.2779
+ ___Block_byref_object_copy_.4352
+ ___Block_byref_object_copy_.5226
+ ___Block_byref_object_copy_.5492
+ ___Block_byref_object_copy_.5944
+ ___Block_byref_object_copy_.6571
+ ___Block_byref_object_copy_.6754
+ ___Block_byref_object_copy_.7547
+ ___Block_byref_object_copy_.9042
+ ___Block_byref_object_copy_.9364
+ ___Block_byref_object_copy_.9568
+ ___Block_byref_object_dispose_.10632
+ ___Block_byref_object_dispose_.10930
+ ___Block_byref_object_dispose_.11750
+ ___Block_byref_object_dispose_.11947
+ ___Block_byref_object_dispose_.12948
+ ___Block_byref_object_dispose_.13685
+ ___Block_byref_object_dispose_.13913
+ ___Block_byref_object_dispose_.14939
+ ___Block_byref_object_dispose_.17109
+ ___Block_byref_object_dispose_.17328
+ ___Block_byref_object_dispose_.18315
+ ___Block_byref_object_dispose_.18931
+ ___Block_byref_object_dispose_.20033
+ ___Block_byref_object_dispose_.20843
+ ___Block_byref_object_dispose_.2117
+ ___Block_byref_object_dispose_.24953
+ ___Block_byref_object_dispose_.25119
+ ___Block_byref_object_dispose_.2780
+ ___Block_byref_object_dispose_.4353
+ ___Block_byref_object_dispose_.5227
+ ___Block_byref_object_dispose_.5493
+ ___Block_byref_object_dispose_.5945
+ ___Block_byref_object_dispose_.6572
+ ___Block_byref_object_dispose_.6755
+ ___Block_byref_object_dispose_.7548
+ ___Block_byref_object_dispose_.9043
+ ___Block_byref_object_dispose_.9365
+ ___Block_byref_object_dispose_.9569
+ ___block_descriptor_69_e8_32s40s48s_e693_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.10300
+ ___block_literal_global.10985
+ ___block_literal_global.11745
+ ___block_literal_global.12118
+ ___block_literal_global.13217
+ ___block_literal_global.15052
+ ___block_literal_global.15481
+ ___block_literal_global.16843
+ ___block_literal_global.17118
+ ___block_literal_global.18503
+ ___block_literal_global.19775
+ ___block_literal_global.20054
+ ___block_literal_global.2021
+ ___block_literal_global.20509
+ ___block_literal_global.21467
+ ___block_literal_global.22802
+ ___block_literal_global.23137
+ ___block_literal_global.24725
+ ___block_literal_global.25338
+ ___block_literal_global.2846
+ ___block_literal_global.3799
+ ___block_literal_global.5313
+ ___block_literal_global.5488
+ ___block_literal_global.6041
+ ___block_literal_global.6583
+ ___block_literal_global.6729
+ ___block_literal_global.7807
+ ___block_literal_global.8710
+ ___block_literal_global.9133
+ ___block_literal_global.9682
+ _hkConfig.21451
+ _initWithEndpoint:data:encrypted:mimeType:forReading:dscpPriority:.nextIdentifier
+ _kCFAbsoluteTimeIntervalSince1970
+ _objc_msgSend$dscpPriority
+ _objc_msgSend$initForReadingWithEndpoint:data:encrypted:mimeType:dscpPriority:
+ _objc_msgSend$initForWritingWithEndpoint:data:encrypted:mimeType:dscpPriority:
+ _objc_msgSend$initWithName:controller:encoding:transport:prepareRequest:executeRequest:endpoint:mimeType:timeout:options:dscpPriority:
+ _objc_msgSend$initWithName:controller:encoding:transport:readRequest:endpoint:mimeType:timeout:options:dscpPriority:
+ _objc_msgSend$initWithName:controller:encoding:transport:request:endpoint:mimeType:timeout:options:dscpPriority:
+ _objc_msgSend$sendRequestWithMethod:path:payload:dscpPriority:completion:
+ _objc_msgSend$stringFromHAP2EncodedRequestType:
+ _sharedInstance.onceToken.15480
- -[HAP2AccessoryServerControllerOperation initWithName:controller:encoding:transport:request:endpoint:mimeType:timeout:options:]
- -[HAP2AccessoryServerControllerReadOperation initWithName:controller:encoding:transport:readRequest:endpoint:mimeType:timeout:options:]
- -[HAP2AccessoryServerControllerTimedWriteOperation initWithName:controller:encoding:transport:prepareRequest:executeRequest:endpoint:mimeType:timeout:options:]
- -[HAP2AccessoryServerTransportRequest initForReadingWithEndpoint:data:encrypted:mimeType:]
- -[HAP2AccessoryServerTransportRequest initForWritingWithEndpoint:data:encrypted:mimeType:]
- -[HAP2AccessoryServerTransportRequest initWithEndpoint:data:encrypted:mimeType:forReading:]
- -[HAP2CoAPClient sendRequestWithMethod:path:payload:completion:]
- GCC_except_table1433
- GCC_except_table1639
- GCC_except_table1642
- GCC_except_table1650
- GCC_except_table1652
- GCC_except_table1658
- GCC_except_table1660
- GCC_except_table1664
- GCC_except_table1668
- GCC_except_table1670
- GCC_except_table1675
- GCC_except_table1679
- GCC_except_table1689
- GCC_except_table1697
- GCC_except_table1704
- GCC_except_table1708
- GCC_except_table1712
- GCC_except_table1716
- GCC_except_table1718
- GCC_except_table1867
- GCC_except_table1871
- GCC_except_table1874
- GCC_except_table1876
- GCC_except_table1885
- GCC_except_table1887
- GCC_except_table1891
- GCC_except_table1894
- GCC_except_table1896
- GCC_except_table1899
- GCC_except_table1916
- GCC_except_table1919
- GCC_except_table1921
- GCC_except_table1923
- GCC_except_table1927
- GCC_except_table1930
- GCC_except_table1934
- GCC_except_table1936
- GCC_except_table1939
- GCC_except_table1942
- GCC_except_table1944
- GCC_except_table1946
- GCC_except_table1950
- GCC_except_table1954
- GCC_except_table1962
- GCC_except_table1973
- GCC_except_table2011
- GCC_except_table2017
- GCC_except_table2188
- GCC_except_table2195
- GCC_except_table2201
- GCC_except_table2207
- GCC_except_table2210
- GCC_except_table2213
- GCC_except_table2216
- GCC_except_table2222
- GCC_except_table2224
- GCC_except_table2228
- GCC_except_table2231
- GCC_except_table2327
- GCC_except_table2335
- GCC_except_table2355
- GCC_except_table2369
- GCC_except_table2449
- GCC_except_table2461
- GCC_except_table2487
- GCC_except_table2495
- GCC_except_table2506
- GCC_except_table2520
- GCC_except_table2523
- GCC_except_table2528
- GCC_except_table2536
- GCC_except_table2542
- GCC_except_table2544
- GCC_except_table2718
- GCC_except_table2768
- GCC_except_table2784
- GCC_except_table2787
- GCC_except_table2801
- GCC_except_table2809
- GCC_except_table2824
- GCC_except_table2836
- GCC_except_table2839
- GCC_except_table2845
- GCC_except_table2852
- GCC_except_table2855
- GCC_except_table2860
- GCC_except_table2916
- GCC_except_table2919
- GCC_except_table2924
- GCC_except_table2926
- GCC_except_table2940
- GCC_except_table2954
- GCC_except_table2956
- GCC_except_table2960
- GCC_except_table2968
- GCC_except_table2976
- GCC_except_table3025
- GCC_except_table3033
- GCC_except_table3035
- GCC_except_table3059
- GCC_except_table3303
- GCC_except_table3367
- GCC_except_table3372
- GCC_except_table3375
- GCC_except_table3377
- GCC_except_table3380
- GCC_except_table3383
- GCC_except_table3390
- GCC_except_table3400
- GCC_except_table3403
- GCC_except_table3414
- GCC_except_table3417
- GCC_except_table3419
- GCC_except_table3422
- GCC_except_table3425
- GCC_except_table3427
- GCC_except_table3430
- GCC_except_table3433
- GCC_except_table3445
- GCC_except_table3447
- GCC_except_table3451
- GCC_except_table3455
- GCC_except_table3459
- GCC_except_table3485
- GCC_except_table3503
- GCC_except_table3507
- GCC_except_table3510
- GCC_except_table3512
- GCC_except_table3514
- GCC_except_table3589
- GCC_except_table3639
- GCC_except_table3665
- GCC_except_table3756
- GCC_except_table3763
- GCC_except_table3781
- GCC_except_table3785
- GCC_except_table3788
- GCC_except_table3791
- GCC_except_table3794
- GCC_except_table3797
- GCC_except_table3800
- GCC_except_table3803
- GCC_except_table3806
- GCC_except_table3809
- GCC_except_table3814
- GCC_except_table3824
- GCC_except_table3827
- GCC_except_table3838
- GCC_except_table3846
- GCC_except_table3850
- GCC_except_table3857
- GCC_except_table3862
- GCC_except_table3881
- GCC_except_table3883
- GCC_except_table3885
- GCC_except_table3889
- GCC_except_table3895
- GCC_except_table3898
- GCC_except_table3900
- GCC_except_table3906
- GCC_except_table3908
- GCC_except_table3911
- GCC_except_table3923
- GCC_except_table3934
- GCC_except_table3936
- GCC_except_table3945
- GCC_except_table3951
- GCC_except_table4211
- GCC_except_table4217
- GCC_except_table4234
- GCC_except_table4238
- GCC_except_table4255
- GCC_except_table4261
- GCC_except_table4274
- GCC_except_table4288
- GCC_except_table4292
- GCC_except_table4405
- GCC_except_table4469
- GCC_except_table4477
- GCC_except_table4487
- GCC_except_table4524
- GCC_except_table4527
- GCC_except_table4612
- GCC_except_table4623
- GCC_except_table4626
- GCC_except_table4633
- GCC_except_table4636
- GCC_except_table4638
- GCC_except_table4643
- GCC_except_table4646
- GCC_except_table4649
- GCC_except_table4653
- GCC_except_table4657
- GCC_except_table4686
- GCC_except_table4706
- GCC_except_table4716
- GCC_except_table4719
- GCC_except_table4724
- GCC_except_table4727
- GCC_except_table4991
- GCC_except_table4995
- GCC_except_table5029
- GCC_except_table5033
- GCC_except_table5035
- GCC_except_table5037
- GCC_except_table5203
- GCC_except_table5209
- GCC_except_table5213
- GCC_except_table5214
- GCC_except_table5222
- GCC_except_table5256
- GCC_except_table5257
- GCC_except_table5278
- GCC_except_table5290
- GCC_except_table5293
- GCC_except_table5298
- GCC_except_table5314
- GCC_except_table5516
- GCC_except_table5528
- GCC_except_table5533
- GCC_except_table5536
- GCC_except_table5537
- GCC_except_table5540
- GCC_except_table5572
- GCC_except_table5594
- GCC_except_table5598
- GCC_except_table5602
- GCC_except_table5607
- GCC_except_table5611
- GCC_except_table5615
- GCC_except_table5619
- GCC_except_table5623
- GCC_except_table5631
- GCC_except_table5695
- GCC_except_table5696
- GCC_except_table5758
- GCC_except_table5762
- GCC_except_table5763
- GCC_except_table5775
- GCC_except_table5781
- GCC_except_table5794
- GCC_except_table5797
- GCC_except_table5798
- GCC_except_table5803
- GCC_except_table5806
- GCC_except_table5813
- GCC_except_table5816
- GCC_except_table5830
- GCC_except_table5837
- GCC_except_table5843
- GCC_except_table5852
- GCC_except_table5858
- GCC_except_table5859
- GCC_except_table5875
- GCC_except_table5886
- GCC_except_table5901
- GCC_except_table5902
- GCC_except_table5907
- GCC_except_table5911
- GCC_except_table5912
- GCC_except_table5915
- GCC_except_table5921
- GCC_except_table5925
- GCC_except_table5929
- GCC_except_table5937
- GCC_except_table6089
- GCC_except_table6145
- GCC_except_table6148
- GCC_except_table6152
- GCC_except_table6158
- GCC_except_table6165
- GCC_except_table6166
- GCC_except_table6182
- GCC_except_table6186
- GCC_except_table6187
- GCC_except_table6237
- GCC_except_table6238
- GCC_except_table6243
- GCC_except_table6271
- GCC_except_table6277
- GCC_except_table6297
- GCC_except_table6314
- GCC_except_table6324
- GCC_except_table6329
- GCC_except_table6345
- GCC_except_table6348
- GCC_except_table6354
- GCC_except_table6360
- GCC_except_table6372
- GCC_except_table6378
- GCC_except_table6387
- GCC_except_table6393
- GCC_except_table6398
- GCC_except_table6406
- GCC_except_table6410
- GCC_except_table6412
- GCC_except_table6416
- GCC_except_table6437
- GCC_except_table6439
- GCC_except_table6466
- GCC_except_table6630
- GCC_except_table6693
- GCC_except_table6725
- GCC_except_table6728
- GCC_except_table6894
- GCC_except_table6957
- GCC_except_table7021
- GCC_except_table7027
- GCC_except_table7073
- GCC_except_table7075
- GCC_except_table7077
- GCC_except_table7079
- GCC_except_table7081
- GCC_except_table7083
- GCC_except_table7085
- GCC_except_table7087
- GCC_except_table7089
- GCC_except_table7091
- GCC_except_table7093
- GCC_except_table7096
- GCC_except_table7098
- GCC_except_table7100
- GCC_except_table7103
- GCC_except_table7129
- GCC_except_table7132
- GCC_except_table7172
- GCC_except_table7176
- GCC_except_table7179
- GCC_except_table7183
- GCC_except_table7186
- GCC_except_table7190
- GCC_except_table7195
- GCC_except_table7243
- GCC_except_table7250
- GCC_except_table7344
- GCC_except_table7360
- GCC_except_table7362
- GCC_except_table7364
- GCC_except_table7367
- GCC_except_table7369
- GCC_except_table7371
- GCC_except_table7373
- GCC_except_table7376
- GCC_except_table7380
- GCC_except_table7385
- _HAPBLEDateStringForTime.formatter
- _HAPBLEDateStringForTime.onceToken
- _OBJC_CLASS_$_NSDateFormatter
- __CopyPairingIdentityDelegateCallback_f.15017
- __CopyPairingIdentityDelegateCallback_f.21740
- __CopyPairingIdentityDelegateCallback_f.2827
- __FindPairedPeerDelegateCallback_f.2826
- __PairSetupPromptForSetupCodeDelegateCallback_f.21742
- __SavePairedPeerDelegateCallback_f.15016
- __SavePairedPeerDelegateCallback_f.21736
- ___64-[HAP2CoAPClient sendRequestWithMethod:path:payload:completion:]_block_invoke
- ___64-[HAP2CoAPClient sendRequestWithMethod:path:payload:completion:]_block_invoke_2
- ___74-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:completion:]_block_invoke
- ___74-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:completion:]_block_invoke_2
- ___Block_byref_object_copy_.10621
- ___Block_byref_object_copy_.10919
- ___Block_byref_object_copy_.11739
- ___Block_byref_object_copy_.11936
- ___Block_byref_object_copy_.12936
- ___Block_byref_object_copy_.13672
- ___Block_byref_object_copy_.13900
- ___Block_byref_object_copy_.14927
- ___Block_byref_object_copy_.17042
- ___Block_byref_object_copy_.17260
- ___Block_byref_object_copy_.18247
- ___Block_byref_object_copy_.18863
- ___Block_byref_object_copy_.19965
- ___Block_byref_object_copy_.20772
- ___Block_byref_object_copy_.2112
- ___Block_byref_object_copy_.24881
- ___Block_byref_object_copy_.25047
- ___Block_byref_object_copy_.2775
- ___Block_byref_object_copy_.4344
- ___Block_byref_object_copy_.5217
- ___Block_byref_object_copy_.5482
- ___Block_byref_object_copy_.5934
- ___Block_byref_object_copy_.6561
- ___Block_byref_object_copy_.6744
- ___Block_byref_object_copy_.7537
- ___Block_byref_object_copy_.9032
- ___Block_byref_object_copy_.9354
- ___Block_byref_object_copy_.9558
- ___Block_byref_object_dispose_.10622
- ___Block_byref_object_dispose_.10920
- ___Block_byref_object_dispose_.11740
- ___Block_byref_object_dispose_.11937
- ___Block_byref_object_dispose_.12937
- ___Block_byref_object_dispose_.13673
- ___Block_byref_object_dispose_.13901
- ___Block_byref_object_dispose_.14928
- ___Block_byref_object_dispose_.17043
- ___Block_byref_object_dispose_.17261
- ___Block_byref_object_dispose_.18248
- ___Block_byref_object_dispose_.18864
- ___Block_byref_object_dispose_.19966
- ___Block_byref_object_dispose_.20773
- ___Block_byref_object_dispose_.2113
- ___Block_byref_object_dispose_.24882
- ___Block_byref_object_dispose_.25048
- ___Block_byref_object_dispose_.2776
- ___Block_byref_object_dispose_.4345
- ___Block_byref_object_dispose_.5218
- ___Block_byref_object_dispose_.5483
- ___Block_byref_object_dispose_.5935
- ___Block_byref_object_dispose_.6562
- ___Block_byref_object_dispose_.6745
- ___Block_byref_object_dispose_.7538
- ___Block_byref_object_dispose_.9033
- ___Block_byref_object_dispose_.9355
- ___Block_byref_object_dispose_.9559
- ___HAPBLEDateStringForTime_block_invoke
- ___block_descriptor_61_e8_32s40s48s_e693_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16ls32l8s40l8s48l8
- ___block_literal_global.10290
- ___block_literal_global.10975
- ___block_literal_global.11735
- ___block_literal_global.12108
- ___block_literal_global.13206
- ___block_literal_global.15041
- ___block_literal_global.15470
- ___block_literal_global.16777
- ___block_literal_global.17051
- ___block_literal_global.18436
- ___block_literal_global.19708
- ___block_literal_global.19987
- ___block_literal_global.2017
- ___block_literal_global.20439
- ___block_literal_global.21397
- ___block_literal_global.22732
- ___block_literal_global.23066
- ___block_literal_global.24654
- ___block_literal_global.25267
- ___block_literal_global.2845
- ___block_literal_global.3791
- ___block_literal_global.467
- ___block_literal_global.5304
- ___block_literal_global.5478
- ___block_literal_global.6031
- ___block_literal_global.6573
- ___block_literal_global.6719
- ___block_literal_global.7797
- ___block_literal_global.8700
- ___block_literal_global.9123
- ___block_literal_global.9673
- _hkConfig.21381
- _initWithEndpoint:data:encrypted:mimeType:forReading:.nextIdentifier
- _objc_msgSend$initForReadingWithEndpoint:data:encrypted:mimeType:
- _objc_msgSend$initForWritingWithEndpoint:data:encrypted:mimeType:
- _objc_msgSend$initWithName:controller:encoding:transport:prepareRequest:executeRequest:endpoint:mimeType:timeout:options:
- _objc_msgSend$initWithName:controller:encoding:transport:readRequest:endpoint:mimeType:timeout:options:
- _objc_msgSend$initWithName:controller:encoding:transport:request:endpoint:mimeType:timeout:options:
- _objc_msgSend$initWithTimeIntervalSinceReferenceDate:
- _objc_msgSend$sendRequestWithMethod:path:payload:completion:
- _objc_msgSend$setDateFormat:
- _objc_msgSend$stringFromDate:
- _sharedInstance.onceToken.15469
CStrings:
+ "%@ Sending request with priority %ld"
+ "%@ requestType: %@"
+ "%Y-%m-%d %H:%M:%S"
+ "%s     IPV6_PKTINFO: ifindex=%d, addr=%s\n"
+ "%s     IPV6_TCLASS: 0x%02x (DSCP 0x%02x)\n"
+ "%s     IP_PKTINFO: ifindex=%d, ipi_spec_dst=%s, ipi_addr=%s\n"
+ "%s     IP_TOS: 0x%02x (DSCP 0x%02x)\n"
+ "%s   No control messages.\n"
+ "%s   cmsg: level=%d, type=%d, len=%u\n"
+ "%s   iov[%d]: base=%p, len=%zu\n"
+ "%s --- End msghdr Info ---\n"
+ "%s --- msghdr Info ---\n"
+ "%s msg_controllen: %u\n"
+ "%s msg_flags: 0x%x ["
+ "%s msg_iovlen: %d\n"
+ "%s msg_name: AF_INET %s:%d (len %d)\n"
+ "%s msg_name: AF_INET6 %s:%d (len %d)\n"
+ "%s msg_name: NULL (len %d)\n"
+ "%s msg_name: Unknown Family %d (len %d)\n"
+ "%{public}@Unable to establish relationship between accessory and controller key: %@"
+ "@104@0:8@16@24@32@40@48@56@64@72d80Q88q96"
+ "@52@0:8@16@24B32@36q44"
+ "@96@0:8@16@24@32@40@48@56@64d72Q80q88"
+ "AF_INET: Setting IP_TOS to 0x%x (DSCP %d)\n"
+ "Chosen sock->fd = %d, flags = %d\n"
+ "Coap Network Read"
+ "HAP2EncodedRequestTypeAddPairing"
+ "HAP2EncodedRequestTypeAttributeDatabaseRead"
+ "HAP2EncodedRequestTypeCharacteristicConfiguration"
+ "HAP2EncodedRequestTypeListPairings"
+ "HAP2EncodedRequestTypeNotificationDeregister"
+ "HAP2EncodedRequestTypeNotificationRegister"
+ "HAP2EncodedRequestTypePreparedExecute"
+ "HAP2EncodedRequestTypePreparedWrite"
+ "HAP2EncodedRequestTypeProtocolConfiguration"
+ "HAP2EncodedRequestTypeRead"
+ "HAP2EncodedRequestTypeRemovePairing"
+ "HAP2EncodedRequestTypeSerializedRequest"
+ "HAP2EncodedRequestTypeServiceSignature"
+ "HAP2EncodedRequestTypeSignature"
+ "HAP2EncodedRequestTypeUnpairedIdentify"
+ "HAP2EncodedRequestTypeWrite"
+ "Invalid socket file descriptor (fd = -1).\n"
+ "MSG_CTRUNC "
+ "MSG_TRUNC "
+ "Registering consumer and creating new HAP2CoAPIOThread"
+ "TX: "
+ "Tq,R,N,V_dscpPriority"
+ "Unknown HAP2EncodedRequestType (%lu)"
+ "Unsupported address family for DSCP. Sending without it.\n"
+ "Using connected socket path (msg_name=NULL).\n"
+ "Using unconnected socket path (msg_name set).\n"
+ "]\n"
+ "_dscpPriority"
+ "coap_send_pdu_dscp"
+ "coap_send_pdu_dscp failed: %s (%d)\n"
+ "coap_send_pdu_dscp: Session state = %d\n"
+ "dscpPriority"
+ "initForReadingWithEndpoint:data:encrypted:mimeType:dscpPriority:"
+ "initForWritingWithEndpoint:data:encrypted:mimeType:dscpPriority:"
+ "initWithName:controller:encoding:transport:prepareRequest:executeRequest:endpoint:mimeType:timeout:options:dscpPriority:"
+ "initWithName:controller:encoding:transport:readRequest:endpoint:mimeType:timeout:options:dscpPriority:"
+ "initWithName:controller:encoding:transport:request:endpoint:mimeType:timeout:options:dscpPriority:"
+ "sendRequestWithMethod:path:payload:dscpPriority:completion:"
+ "stringFromHAP2EncodedRequestType:"
+ "v52@0:8C16@\"NSString\"20@\"NSData\"28q36@?<v@?@\"NSData\"@\"NSError\">44"
+ "v52@0:8C16@20@28q36@?44"
- "%{public}@Unable to establish relationsihp between accessory and controller key: %@"
- "@44@0:8@16@24B32@36"
- "@88@0:8@16@24@32@40@48@56@64d72Q80"
- "@96@0:8@16@24@32@40@48@56@64@72d80Q88"
- "initForReadingWithEndpoint:data:encrypted:mimeType:"
- "initForWritingWithEndpoint:data:encrypted:mimeType:"
- "initWithName:controller:encoding:transport:prepareRequest:executeRequest:endpoint:mimeType:timeout:options:"
- "initWithName:controller:encoding:transport:readRequest:endpoint:mimeType:timeout:options:"
- "initWithName:controller:encoding:transport:request:endpoint:mimeType:timeout:options:"
- "initWithTimeIntervalSinceReferenceDate:"
- "sendRequestWithMethod:path:payload:completion:"
- "setDateFormat:"
- "stringFromDate:"
- "v44@0:8C16@\"NSString\"20@\"NSData\"28@?<v@?@\"NSData\"@\"NSError\">36"
- "v44@0:8C16@20@28@?36"
- "yyyy-MM-dd HH:mm:ss"

```
