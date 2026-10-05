## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-2365.40.1.0.0
-  __TEXT.__text: 0x209268
-  __TEXT.__objc_methlist: 0xf508
+2365.40.3.0.1
+  __TEXT.__text: 0x20a618
+  __TEXT.__objc_methlist: 0xf578
   __TEXT.__const: 0x36b4
   __TEXT.__swift5_typeref: 0xdf0
   __TEXT.__swift5_capture: 0x1038

   __TEXT.__swift_as_cont: 0x1f4
   __TEXT.__swift5_fieldmd: 0x680
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__cstring: 0x1977f
-  __TEXT.__oslogstring: 0x24e22
+  __TEXT.__cstring: 0x197c9
+  __TEXT.__oslogstring: 0x24eff
   __TEXT.__gcc_except_tab: 0x5008
-  __TEXT.__unwind_info: 0x6ab0
+  __TEXT.__unwind_info: 0x6ae0
   __TEXT.__eh_frame: 0x2bd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x64e8
+  __DATA_CONST.__const: 0x6510
   __DATA_CONST.__objc_classlist: 0xb40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x53d8
+  __DATA_CONST.__objc_selrefs: 0x53e8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x728
   __DATA_CONST.__objc_arraydata: 0x138

   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x24b8
-  __AUTH.__objc_data: 0x3bc0
-  __AUTH.__data: 0x128
   __DATA.__objc_ivar: 0x1c50
-  __DATA.__data: 0x1e70
-  __DATA.__common: 0x188
-  __DATA_DIRTY.__objc_data: 0x3a98
-  __DATA_DIRTY.__data: 0xc20
-  __DATA_DIRTY.__bss: 0x78
-  __DATA_DIRTY.__common: 0x38
+  __DATA.__data: 0x640
+  __DATA.__common: 0x190
+  __DATA_DIRTY.__objc_data: 0x7658
+  __DATA_DIRTY.__data: 0x2580
+  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8323
-  Symbols:   14421
-  CStrings:  7239
+  Functions: 8335
+  Symbols:   14432
+  CStrings:  7247
 
Symbols:
+ -[NEAppPush replaceProviderBundleIdentifier:with:]
+ -[NEConfiguration replaceProviderBundleIdentifier:with:]
+ -[NEConfigurationManager handleAppReplacementFromBundleID:toBundleID:sourcePersona:destinationPersona:completionQueue:handler:]
+ -[NEContentFilter replaceProviderBundleIdentifier:with:]
+ -[NEDNSProxy replaceProviderBundleIdentifier:with:]
+ -[NEHotspot replaceProviderBundleIdentifier:with:]
+ -[NEPathController replaceProviderBundleIdentifier:with:]
+ -[NEVPN replaceProviderBundleIdentifier:with:]
+ -[NEVPNApp replaceProviderBundleIdentifier:with:]
+ GCC_except_table1000
+ GCC_except_table1001
+ GCC_except_table1003
+ GCC_except_table1004
+ GCC_except_table1005
+ GCC_except_table1006
+ GCC_except_table1055
+ GCC_except_table1144
+ GCC_except_table1204
+ GCC_except_table1209
+ GCC_except_table1210
+ GCC_except_table1211
+ GCC_except_table1384
+ GCC_except_table1385
+ GCC_except_table1386
+ GCC_except_table1387
+ GCC_except_table1388
+ GCC_except_table1390
+ GCC_except_table1391
+ GCC_except_table1397
+ GCC_except_table1402
+ GCC_except_table1403
+ GCC_except_table1416
+ GCC_except_table1427
+ GCC_except_table1428
+ GCC_except_table1554
+ GCC_except_table1679
+ GCC_except_table1685
+ GCC_except_table1688
+ GCC_except_table1742
+ GCC_except_table1743
+ GCC_except_table1744
+ GCC_except_table1745
+ GCC_except_table1747
+ GCC_except_table1748
+ GCC_except_table1749
+ GCC_except_table1754
+ GCC_except_table1758
+ GCC_except_table1761
+ GCC_except_table1768
+ GCC_except_table1775
+ GCC_except_table1800
+ GCC_except_table1826
+ GCC_except_table2040
+ GCC_except_table278
+ GCC_except_table2952
+ GCC_except_table3197
+ GCC_except_table3202
+ GCC_except_table3208
+ GCC_except_table3211
+ GCC_except_table3226
+ GCC_except_table3227
+ GCC_except_table3228
+ GCC_except_table3243
+ GCC_except_table3257
+ GCC_except_table3258
+ GCC_except_table3300
+ GCC_except_table3304
+ GCC_except_table3350
+ GCC_except_table3401
+ GCC_except_table3461
+ GCC_except_table3480
+ GCC_except_table3489
+ GCC_except_table3491
+ GCC_except_table3514
+ GCC_except_table3515
+ GCC_except_table3516
+ GCC_except_table3526
+ GCC_except_table3540
+ GCC_except_table3584
+ GCC_except_table3586
+ GCC_except_table3621
+ GCC_except_table3623
+ GCC_except_table3624
+ GCC_except_table3713
+ GCC_except_table3741
+ GCC_except_table3990
+ GCC_except_table3991
+ GCC_except_table3992
+ GCC_except_table3993
+ GCC_except_table3995
+ GCC_except_table408
+ GCC_except_table4087
+ GCC_except_table410
+ GCC_except_table4254
+ GCC_except_table4265
+ GCC_except_table4271
+ GCC_except_table4287
+ GCC_except_table4288
+ GCC_except_table4289
+ GCC_except_table4291
+ GCC_except_table4292
+ GCC_except_table4293
+ GCC_except_table4294
+ GCC_except_table4298
+ GCC_except_table4303
+ GCC_except_table4304
+ GCC_except_table4317
+ GCC_except_table4318
+ GCC_except_table4390
+ GCC_except_table4399
+ GCC_except_table4495
+ GCC_except_table4496
+ GCC_except_table4497
+ GCC_except_table4498
+ GCC_except_table4499
+ GCC_except_table4500
+ GCC_except_table4502
+ GCC_except_table4598
+ GCC_except_table476
+ GCC_except_table4780
+ GCC_except_table4785
+ GCC_except_table4792
+ GCC_except_table4823
+ GCC_except_table4833
+ GCC_except_table4837
+ GCC_except_table4849
+ GCC_except_table4869
+ GCC_except_table4871
+ GCC_except_table4877
+ GCC_except_table4879
+ GCC_except_table4971
+ GCC_except_table5041
+ GCC_except_table5061
+ GCC_except_table5065
+ GCC_except_table5078
+ GCC_except_table5177
+ GCC_except_table5182
+ GCC_except_table5223
+ GCC_except_table5269
+ GCC_except_table5271
+ GCC_except_table5337
+ GCC_except_table5340
+ GCC_except_table5376
+ GCC_except_table5396
+ GCC_except_table5398
+ GCC_except_table5400
+ GCC_except_table5408
+ GCC_except_table5448
+ GCC_except_table5449
+ GCC_except_table5451
+ GCC_except_table5453
+ GCC_except_table5456
+ GCC_except_table5500
+ GCC_except_table5522
+ GCC_except_table5525
+ GCC_except_table5620
+ GCC_except_table5951
+ GCC_except_table5990
+ GCC_except_table5991
+ GCC_except_table5994
+ GCC_except_table6059
+ GCC_except_table6066
+ GCC_except_table6074
+ GCC_except_table6077
+ GCC_except_table6087
+ GCC_except_table6103
+ GCC_except_table6104
+ GCC_except_table6105
+ GCC_except_table6106
+ GCC_except_table6107
+ GCC_except_table6108
+ GCC_except_table6112
+ GCC_except_table6113
+ GCC_except_table6114
+ GCC_except_table6130
+ GCC_except_table6133
+ GCC_except_table6137
+ GCC_except_table6215
+ GCC_except_table6216
+ GCC_except_table6357
+ GCC_except_table6358
+ GCC_except_table6359
+ GCC_except_table6360
+ GCC_except_table6361
+ GCC_except_table6362
+ GCC_except_table6363
+ GCC_except_table6364
+ GCC_except_table6366
+ GCC_except_table6367
+ GCC_except_table6368
+ GCC_except_table6382
+ GCC_except_table6383
+ GCC_except_table6384
+ GCC_except_table6389
+ GCC_except_table6415
+ GCC_except_table646
+ GCC_except_table647
+ GCC_except_table648
+ GCC_except_table649
+ GCC_except_table6494
+ GCC_except_table6495
+ GCC_except_table6496
+ GCC_except_table6497
+ GCC_except_table650
+ GCC_except_table652
+ GCC_except_table658
+ GCC_except_table663
+ GCC_except_table678
+ GCC_except_table679
+ GCC_except_table776
+ GCC_except_table843
+ GCC_except_table848
+ GCC_except_table897
+ GCC_except_table902
+ GCC_except_table926
+ GCC_except_table927
+ GCC_except_table928
+ GCC_except_table929
+ GCC_except_table957
+ ___127-[NEConfigurationManager handleAppReplacementFromBundleID:toBundleID:sourcePersona:destinationPersona:completionQueue:handler:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e39_v28?0B8q12"NSObject<OS_xpc_object>"20ls32l8s40l8s48l8s56l8s64l8
- GCC_except_table1047
- GCC_except_table1136
- GCC_except_table1195
- GCC_except_table1196
- GCC_except_table1201
- GCC_except_table1202
- GCC_except_table1371
- GCC_except_table1372
- GCC_except_table1375
- GCC_except_table1376
- GCC_except_table1377
- GCC_except_table1378
- GCC_except_table1381
- GCC_except_table1382
- GCC_except_table1394
- GCC_except_table1395
- GCC_except_table1408
- GCC_except_table1419
- GCC_except_table1420
- GCC_except_table1546
- GCC_except_table1671
- GCC_except_table1672
- GCC_except_table1677
- GCC_except_table1725
- GCC_except_table1726
- GCC_except_table1727
- GCC_except_table1728
- GCC_except_table1729
- GCC_except_table1730
- GCC_except_table1731
- GCC_except_table1732
- GCC_except_table1750
- GCC_except_table1753
- GCC_except_table1759
- GCC_except_table1760
- GCC_except_table1792
- GCC_except_table1818
- GCC_except_table2032
- GCC_except_table277
- GCC_except_table2944
- GCC_except_table3189
- GCC_except_table3194
- GCC_except_table3200
- GCC_except_table3203
- GCC_except_table3218
- GCC_except_table3219
- GCC_except_table3220
- GCC_except_table3235
- GCC_except_table3249
- GCC_except_table3250
- GCC_except_table3292
- GCC_except_table3296
- GCC_except_table3342
- GCC_except_table3393
- GCC_except_table3453
- GCC_except_table3472
- GCC_except_table3481
- GCC_except_table3483
- GCC_except_table3506
- GCC_except_table3507
- GCC_except_table3508
- GCC_except_table3518
- GCC_except_table3532
- GCC_except_table3570
- GCC_except_table3576
- GCC_except_table3613
- GCC_except_table3615
- GCC_except_table3616
- GCC_except_table3705
- GCC_except_table3733
- GCC_except_table3975
- GCC_except_table3982
- GCC_except_table3984
- GCC_except_table3985
- GCC_except_table3987
- GCC_except_table402
- GCC_except_table404
- GCC_except_table4079
- GCC_except_table4246
- GCC_except_table4257
- GCC_except_table4263
- GCC_except_table4278
- GCC_except_table4279
- GCC_except_table4280
- GCC_except_table4281
- GCC_except_table4282
- GCC_except_table4283
- GCC_except_table4284
- GCC_except_table4285
- GCC_except_table4295
- GCC_except_table4296
- GCC_except_table4302
- GCC_except_table4309
- GCC_except_table4382
- GCC_except_table4383
- GCC_except_table4487
- GCC_except_table4488
- GCC_except_table4489
- GCC_except_table4490
- GCC_except_table4491
- GCC_except_table4492
- GCC_except_table4494
- GCC_except_table4589
- GCC_except_table471
- GCC_except_table4771
- GCC_except_table4776
- GCC_except_table4783
- GCC_except_table4814
- GCC_except_table4824
- GCC_except_table4828
- GCC_except_table4840
- GCC_except_table4860
- GCC_except_table4862
- GCC_except_table4868
- GCC_except_table4870
- GCC_except_table4962
- GCC_except_table5032
- GCC_except_table5052
- GCC_except_table5056
- GCC_except_table5069
- GCC_except_table5168
- GCC_except_table5173
- GCC_except_table5214
- GCC_except_table5260
- GCC_except_table5262
- GCC_except_table5328
- GCC_except_table5331
- GCC_except_table5367
- GCC_except_table5387
- GCC_except_table5389
- GCC_except_table5391
- GCC_except_table5399
- GCC_except_table5439
- GCC_except_table5440
- GCC_except_table5442
- GCC_except_table5444
- GCC_except_table5447
- GCC_except_table5491
- GCC_except_table5513
- GCC_except_table5516
- GCC_except_table5611
- GCC_except_table5940
- GCC_except_table5978
- GCC_except_table5979
- GCC_except_table5982
- GCC_except_table6047
- GCC_except_table6053
- GCC_except_table6054
- GCC_except_table6062
- GCC_except_table6075
- GCC_except_table6090
- GCC_except_table6091
- GCC_except_table6092
- GCC_except_table6093
- GCC_except_table6094
- GCC_except_table6095
- GCC_except_table6096
- GCC_except_table6097
- GCC_except_table6100
- GCC_except_table6101
- GCC_except_table6118
- GCC_except_table6125
- GCC_except_table6203
- GCC_except_table6204
- GCC_except_table6336
- GCC_except_table6337
- GCC_except_table6338
- GCC_except_table6339
- GCC_except_table6340
- GCC_except_table6341
- GCC_except_table6342
- GCC_except_table6343
- GCC_except_table6344
- GCC_except_table6345
- GCC_except_table6346
- GCC_except_table6347
- GCC_except_table6370
- GCC_except_table6371
- GCC_except_table6372
- GCC_except_table639
- GCC_except_table640
- GCC_except_table6403
- GCC_except_table641
- GCC_except_table642
- GCC_except_table643
- GCC_except_table644
- GCC_except_table645
- GCC_except_table6482
- GCC_except_table6483
- GCC_except_table6484
- GCC_except_table6485
- GCC_except_table656
- GCC_except_table657
- GCC_except_table672
- GCC_except_table769
- GCC_except_table836
- GCC_except_table841
- GCC_except_table890
- GCC_except_table895
- GCC_except_table913
- GCC_except_table919
- GCC_except_table921
- GCC_except_table922
- GCC_except_table950
- GCC_except_table989
- GCC_except_table990
- GCC_except_table991
- GCC_except_table992
- GCC_except_table993
- GCC_except_table994
CStrings:
+ "%@: Cannot handle app replacement without both bundle identifiers"
+ "%@: Failed to handle app replacement from %@ to %@: %@"
+ "%@: Processing app replacement from %@ to %@"
+ "%@: Successfully handled app replacement from %@ to %@"
+ "destination-bundle-id"
+ "destination-persona"
+ "source-bundle-id"
+ "source-persona"
```
