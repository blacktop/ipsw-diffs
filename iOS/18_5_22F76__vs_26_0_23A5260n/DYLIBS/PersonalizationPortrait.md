## PersonalizationPortrait

> `/System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait`

```diff

-1276.17.0.3.0
-  __TEXT.__text: 0x5c0d8
+1294.2.0.0.0
+  __TEXT.__text: 0x5d280
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x6e9c
+  __TEXT.__objc_methlist: 0x70cc
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x5932
-  __TEXT.__gcc_except_tab: 0x1080
+  __TEXT.__cstring: 0x5a12
+  __TEXT.__gcc_except_tab: 0x1098
   __TEXT.__oslogstring: 0x3021
   __TEXT.__dlopen_cstrs: 0xd5
-  __TEXT.__unwind_info: 0x1b10
-  __TEXT.__objc_classname: 0xd93
-  __TEXT.__objc_methname: 0xe1d0
-  __TEXT.__objc_methtype: 0x2104
-  __TEXT.__objc_stubs: 0x7640
+  __TEXT.__unwind_info: 0x1b48
+  __TEXT.__objc_classname: 0xe03
+  __TEXT.__objc_methname: 0xe51c
+  __TEXT.__objc_methtype: 0x2197
+  __TEXT.__objc_stubs: 0x76e0
   __DATA_CONST.__got: 0x7d8
-  __DATA_CONST.__const: 0x1f38
-  __DATA_CONST.__objc_classlist: 0x3d8
+  __DATA_CONST.__const: 0x1f60
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c00
-  __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_selrefs: 0x2c90
+  __DATA_CONST.__objc_protorefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x370
   __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0x7dc0
-  __AUTH_CONST.__objc_const: 0xc0c0
+  __AUTH_CONST.__const: 0xec0
+  __AUTH_CONST.__cfstring: 0x7ec0
+  __AUTH_CONST.__objc_const: 0xc470
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x850
-  __DATA.__data: 0xd20
-  __DATA.__bss: 0x438
-  __DATA_DIRTY.__objc_data: 0x2120
+  __AUTH.__objc_data: 0x6e0
+  __DATA.__objc_ivar: 0x870
+  __DATA.__data: 0xd80
+  __DATA.__bss: 0x420
+  __DATA_DIRTY.__objc_data: 0x2080
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ContactsDonation.framework/ContactsDonation
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions
   - /System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 843D49B9-3C5C-3603-8B95-A0FB7FBE1F47
-  Functions: 2518
-  Symbols:   8580
-  CStrings:  4996
+  UUID: 7D9A0932-6F6E-3F23-8670-F32A0C68B078
+  Functions: 2564
+  Symbols:   8723
+  CStrings:  5052
 
Symbols:
+ +[PPSpotlightAttributes supportsSecureCoding]
+ +[PPTextUnderstandingClient sharedInstance]
+ +[PPTextUnderstandingExtraction supportsSecureCoding]
+ -[PPSpotlightAttributes .cxx_destruct]
+ -[PPSpotlightAttributes copyWithZone:]
+ -[PPSpotlightAttributes description]
+ -[PPSpotlightAttributes encodeWithCoder:]
+ -[PPSpotlightAttributes featureVectorVersion]
+ -[PPSpotlightAttributes featureVector]
+ -[PPSpotlightAttributes hash]
+ -[PPSpotlightAttributes initWithCoder:]
+ -[PPSpotlightAttributes initWithStaticScore:featureVector:featureVectorVersion:namedEntityScores:]
+ -[PPSpotlightAttributes isEqual:]
+ -[PPSpotlightAttributes isEqualToSpotlightAttributes:]
+ -[PPSpotlightAttributes namedEntityScores]
+ -[PPSpotlightAttributes setFeatureVector:]
+ -[PPSpotlightAttributes setFeatureVectorVersion:]
+ -[PPSpotlightAttributes setNamedEntityScores:]
+ -[PPSpotlightAttributes setStaticScore:]
+ -[PPSpotlightAttributes staticScore]
+ -[PPTextUnderstandingClient .cxx_destruct]
+ -[PPTextUnderstandingClient _synchronousRemoteObjectProxyWithErrorHandler:]
+ -[PPTextUnderstandingClient init]
+ -[PPTextUnderstandingClient spotlightAttributesForBundleId:spotlightIdentifier:extractions:error:]
+ -[PPTextUnderstandingExtraction .cxx_destruct]
+ -[PPTextUnderstandingExtraction copyWithZone:]
+ -[PPTextUnderstandingExtraction description]
+ -[PPTextUnderstandingExtraction encodeWithCoder:]
+ -[PPTextUnderstandingExtraction hash]
+ -[PPTextUnderstandingExtraction initWithCoder:]
+ -[PPTextUnderstandingExtraction initWithNamedEntities:topics:topicAlgorithm:]
+ -[PPTextUnderstandingExtraction isEqual:]
+ -[PPTextUnderstandingExtraction isEqualToTextUnderstandingExtraction:]
+ -[PPTextUnderstandingExtraction namedEntities]
+ -[PPTextUnderstandingExtraction setNamedEntities:]
+ -[PPTextUnderstandingExtraction setTopicAlgorithm:]
+ -[PPTextUnderstandingExtraction setTopics:]
+ -[PPTextUnderstandingExtraction topicAlgorithm]
+ -[PPTextUnderstandingExtraction topics]
+ GCC_except_table1
+ GCC_except_table1012
+ GCC_except_table1013
+ GCC_except_table1018
+ GCC_except_table1094
+ GCC_except_table1099
+ GCC_except_table1102
+ GCC_except_table1149
+ GCC_except_table1153
+ GCC_except_table1244
+ GCC_except_table1264
+ GCC_except_table1269
+ GCC_except_table1274
+ GCC_except_table1296
+ GCC_except_table1318
+ GCC_except_table1319
+ GCC_except_table1328
+ GCC_except_table1373
+ GCC_except_table1387
+ GCC_except_table1390
+ GCC_except_table1392
+ GCC_except_table1481
+ GCC_except_table1497
+ GCC_except_table15
+ GCC_except_table1527
+ GCC_except_table1555
+ GCC_except_table1562
+ GCC_except_table1565
+ GCC_except_table1645
+ GCC_except_table1653
+ GCC_except_table1655
+ GCC_except_table1660
+ GCC_except_table1697
+ GCC_except_table1713
+ GCC_except_table1730
+ GCC_except_table1739
+ GCC_except_table1744
+ GCC_except_table1747
+ GCC_except_table1758
+ GCC_except_table1761
+ GCC_except_table1763
+ GCC_except_table1767
+ GCC_except_table1771
+ GCC_except_table1776
+ GCC_except_table1781
+ GCC_except_table1790
+ GCC_except_table1805
+ GCC_except_table1819
+ GCC_except_table1821
+ GCC_except_table1828
+ GCC_except_table1837
+ GCC_except_table1855
+ GCC_except_table1878
+ GCC_except_table1883
+ GCC_except_table1905
+ GCC_except_table1909
+ GCC_except_table209
+ GCC_except_table2120
+ GCC_except_table2125
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table228
+ GCC_except_table256
+ GCC_except_table297
+ GCC_except_table302
+ GCC_except_table312
+ GCC_except_table379
+ GCC_except_table383
+ GCC_except_table466
+ GCC_except_table470
+ GCC_except_table477
+ GCC_except_table483
+ GCC_except_table498
+ GCC_except_table502
+ GCC_except_table537
+ GCC_except_table624
+ GCC_except_table649
+ GCC_except_table653
+ GCC_except_table657
+ GCC_except_table686
+ GCC_except_table689
+ GCC_except_table902
+ GCC_except_table946
+ GCC_except_table961
+ GCC_except_table968
+ _EventKitLibraryCore.frameworkLibrary.1632
+ _EventKitLibraryCore.frameworkLibrary.6348
+ _OBJC_CLASS_$_PPSpotlightAttributes
+ _OBJC_CLASS_$_PPTextUnderstandingClient
+ _OBJC_CLASS_$_PPTextUnderstandingExtraction
+ _OBJC_IVAR_$_PPSpotlightAttributes._featureVector
+ _OBJC_IVAR_$_PPSpotlightAttributes._featureVectorVersion
+ _OBJC_IVAR_$_PPSpotlightAttributes._namedEntityScores
+ _OBJC_IVAR_$_PPSpotlightAttributes._staticScore
+ _OBJC_IVAR_$_PPTextUnderstandingClient._clientHelper
+ _OBJC_IVAR_$_PPTextUnderstandingExtraction._namedEntities
+ _OBJC_IVAR_$_PPTextUnderstandingExtraction._topicAlgorithm
+ _OBJC_IVAR_$_PPTextUnderstandingExtraction._topics
+ _OBJC_METACLASS_$_PPSpotlightAttributes
+ _OBJC_METACLASS_$_PPTextUnderstandingClient
+ _OBJC_METACLASS_$_PPTextUnderstandingExtraction
+ __OBJC_$_CLASS_METHODS_PPSpotlightAttributes
+ __OBJC_$_CLASS_METHODS_PPTextUnderstandingClient
+ __OBJC_$_CLASS_METHODS_PPTextUnderstandingExtraction
+ __OBJC_$_CLASS_PROP_LIST_PPSpotlightAttributes
+ __OBJC_$_CLASS_PROP_LIST_PPTextUnderstandingExtraction
+ __OBJC_$_INSTANCE_METHODS_PPSpotlightAttributes
+ __OBJC_$_INSTANCE_METHODS_PPTextUnderstandingClient
+ __OBJC_$_INSTANCE_METHODS_PPTextUnderstandingExtraction
+ __OBJC_$_INSTANCE_VARIABLES_PPSpotlightAttributes
+ __OBJC_$_INSTANCE_VARIABLES_PPTextUnderstandingClient
+ __OBJC_$_INSTANCE_VARIABLES_PPTextUnderstandingExtraction
+ __OBJC_$_PROP_LIST_PPSpotlightAttributes
+ __OBJC_$_PROP_LIST_PPTextUnderstandingExtraction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PPTextUnderstandingServerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PPTextUnderstandingServerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_PPSpotlightAttributes
+ __OBJC_CLASS_PROTOCOLS_$_PPTextUnderstandingExtraction
+ __OBJC_CLASS_RO_$_PPSpotlightAttributes
+ __OBJC_CLASS_RO_$_PPTextUnderstandingClient
+ __OBJC_CLASS_RO_$_PPTextUnderstandingExtraction
+ __OBJC_LABEL_PROTOCOL_$_PPTextUnderstandingServerProtocol
+ __OBJC_METACLASS_RO_$_PPSpotlightAttributes
+ __OBJC_METACLASS_RO_$_PPTextUnderstandingClient
+ __OBJC_METACLASS_RO_$_PPTextUnderstandingExtraction
+ __OBJC_PROTOCOL_$_PPTextUnderstandingServerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_PPTextUnderstandingServerProtocol
+ ___21-[PPEventClient init]_block_invoke.111
+ ___23-[PPContactClient init]_block_invoke.103
+ ___27-[PPConnectionsClient init]_block_invoke.82
+ ___29-[PPTopicReadOnlyClient init]_block_invoke.105
+ ___31-[PPSocialHighlightClient init]_block_invoke.90
+ ___31-[PPTemporalClusterClient init]_block_invoke.80
+ ___32-[PPLocationReadOnlyClient init]_block_invoke.83
+ ___33-[PPTextUnderstandingClient init]_block_invoke
+ ___33-[PPTextUnderstandingClient init]_block_invoke.67
+ ___35-[PPNamedEntityReadOnlyClient init]_block_invoke.85
+ ___43+[PPTextUnderstandingClient sharedInstance]_block_invoke
+ ___75+[PPCustomDonation donateLabeledStrings:bundleId:groupId:documentId:error:]_block_invoke.117
+ ___95+[PPCustomDonation donateParsecNamedEntitiesAndTopics:rawQuery:reformulatedQuery:source:error:]_block_invoke.105
+ ___98-[PPTextUnderstandingClient spotlightAttributesForBundleId:spotlightIdentifier:extractions:error:]_block_invoke
+ ___98-[PPTextUnderstandingClient spotlightAttributesForBundleId:spotlightIdentifier:extractions:error:]_block_invoke_2
+ ___Block_byref_object_copy_.1207
+ ___Block_byref_object_copy_.1852
+ ___Block_byref_object_copy_.2862
+ ___Block_byref_object_copy_.3147
+ ___Block_byref_object_copy_.3458
+ ___Block_byref_object_copy_.347
+ ___Block_byref_object_copy_.3706
+ ___Block_byref_object_copy_.407
+ ___Block_byref_object_copy_.4321
+ ___Block_byref_object_copy_.4492
+ ___Block_byref_object_copy_.4757
+ ___Block_byref_object_copy_.514
+ ___Block_byref_object_copy_.5367
+ ___Block_byref_object_copy_.5433
+ ___Block_byref_object_copy_.574
+ ___Block_byref_object_copy_.5759
+ ___Block_byref_object_copy_.6130
+ ___Block_byref_object_copy_.6340
+ ___Block_byref_object_copy_.6734
+ ___Block_byref_object_copy_.7677
+ ___Block_byref_object_dispose_.1208
+ ___Block_byref_object_dispose_.1853
+ ___Block_byref_object_dispose_.2863
+ ___Block_byref_object_dispose_.3148
+ ___Block_byref_object_dispose_.3459
+ ___Block_byref_object_dispose_.348
+ ___Block_byref_object_dispose_.3707
+ ___Block_byref_object_dispose_.408
+ ___Block_byref_object_dispose_.4322
+ ___Block_byref_object_dispose_.4493
+ ___Block_byref_object_dispose_.4758
+ ___Block_byref_object_dispose_.515
+ ___Block_byref_object_dispose_.5368
+ ___Block_byref_object_dispose_.5434
+ ___Block_byref_object_dispose_.575
+ ___Block_byref_object_dispose_.5760
+ ___Block_byref_object_dispose_.6131
+ ___Block_byref_object_dispose_.6341
+ ___Block_byref_object_dispose_.6735
+ ___Block_byref_object_dispose_.7678
+ ___EventKitLibraryCore_block_invoke.1633
+ ___EventKitLibraryCore_block_invoke.6349
+ ___block_descriptor_48_e8_32r40r_e43_v24?0"PPSpotlightAttributes"8"NSError"16lr32l8r40l8
+ ___block_literal_global.101.5435
+ ___block_literal_global.104
+ ___block_literal_global.106
+ ___block_literal_global.108
+ ___block_literal_global.121
+ ___block_literal_global.132
+ ___block_literal_global.1420
+ ___block_literal_global.145
+ ___block_literal_global.159
+ ___block_literal_global.1624
+ ___block_literal_global.1775
+ ___block_literal_global.18.7525
+ ___block_literal_global.1831
+ ___block_literal_global.201
+ ___block_literal_global.2062
+ ___block_literal_global.244
+ ___block_literal_global.27.7532
+ ___block_literal_global.2735
+ ___block_literal_global.2799
+ ___block_literal_global.2860
+ ___block_literal_global.3154
+ ___block_literal_global.3466
+ ___block_literal_global.367
+ ___block_literal_global.3783
+ ___block_literal_global.4147
+ ___block_literal_global.4490
+ ___block_literal_global.4632
+ ___block_literal_global.4759
+ ___block_literal_global.520
+ ___block_literal_global.5441
+ ___block_literal_global.5669
+ ___block_literal_global.629
+ ___block_literal_global.6430
+ ___block_literal_global.6656
+ ___block_literal_global.6780
+ ___block_literal_global.69.7559
+ ___block_literal_global.73.7563
+ ___block_literal_global.74
+ ___block_literal_global.7511
+ ___block_literal_global.7684
+ ___block_literal_global.7710
+ ___block_literal_global.84
+ ___block_literal_global.8481
+ ___block_literal_global.86
+ ___block_literal_global.88
+ ___block_literal_global.8838
+ ___block_literal_global.94
+ ___block_literal_global.94.5442
+ ___block_literal_global.99
+ _audit_stringEventKit.1645
+ _audit_stringEventKit.6352
+ _defaultStore._pasExprOnceResult.2448
+ _defaultStore._pasExprOnceResult.9344
+ _defaultStore._pasExprOnceResult.9711
+ _defaultStore._pasOnceToken12.9710
+ _featureNames._pasExprOnceResult.1776
+ _featureNames._pasExprOnceResult.245
+ _featureNames._pasExprOnceResult.3781
+ _featureNames._pasExprOnceResult.4146
+ _featureNames._pasExprOnceResult.6657
+ _featureNames._pasExprOnceResult.8482
+ _featureNames._pasOnceToken4.1774
+ _featureNames._pasOnceToken4.6655
+ _featureNames._pasOnceToken6.8480
+ _featureNames._pasOnceToken9.8552
+ _objc_msgSend$initWithNamedEntities:topics:topicAlgorithm:
+ _objc_msgSend$initWithStaticScore:featureVector:featureVectorVersion:namedEntityScores:
+ _objc_msgSend$isEqualToSpotlightAttributes:
+ _objc_msgSend$isEqualToTextUnderstandingExtraction:
+ _objc_msgSend$spotlightAttributesForBundleId:spotlightIdentifier:extractions:completion:
+ _sharedInstance._pasExprOnceResult.211
+ _sharedInstance._pasExprOnceResult.2922
+ _sharedInstance._pasExprOnceResult.3481
+ _sharedInstance._pasExprOnceResult.392
+ _sharedInstance._pasExprOnceResult.4400
+ _sharedInstance._pasExprOnceResult.442
+ _sharedInstance._pasExprOnceResult.5124
+ _sharedInstance._pasExprOnceResult.5194
+ _sharedInstance._pasExprOnceResult.543
+ _sharedInstance._pasExprOnceResult.5480
+ _sharedInstance._pasExprOnceResult.6176
+ _sharedInstance._pasExprOnceResult.6431
+ _sharedInstance._pasExprOnceResult.6509
+ _sharedInstance._pasExprOnceResult.6583
+ _sharedInstance._pasExprOnceResult.7700
+ _sharedInstance._pasOnceToken12.4399
+ _sharedInstance._pasOnceToken12.5123
+ _sharedInstance._pasOnceToken12.6429
+ _sharedInstance._pasOnceToken2.3480
+ _sharedInstance._pasOnceToken2.542
+ _sharedInstance._pasOnceToken2.5479
+ _sharedInstance._pasOnceToken2.7699
+ _sharedInstance._pasOnceToken4
+ _sharedInstance._pasOnceToken6.5193
+ _sharedInstance._pasOnceToken6.6508
+ _sharedInstance._pasOnceToken8.6175
+ _sharedInstance._pasOnceToken8.6582
- GCC_except_table1000
- GCC_except_table1001
- GCC_except_table1006
- GCC_except_table1082
- GCC_except_table1087
- GCC_except_table1090
- GCC_except_table1137
- GCC_except_table1141
- GCC_except_table1232
- GCC_except_table1252
- GCC_except_table1257
- GCC_except_table1262
- GCC_except_table1284
- GCC_except_table1306
- GCC_except_table1307
- GCC_except_table1316
- GCC_except_table1361
- GCC_except_table1375
- GCC_except_table1378
- GCC_except_table1380
- GCC_except_table1469
- GCC_except_table1485
- GCC_except_table1515
- GCC_except_table1543
- GCC_except_table1550
- GCC_except_table1553
- GCC_except_table1633
- GCC_except_table1641
- GCC_except_table1643
- GCC_except_table1648
- GCC_except_table1685
- GCC_except_table1701
- GCC_except_table1718
- GCC_except_table1727
- GCC_except_table1732
- GCC_except_table1735
- GCC_except_table1746
- GCC_except_table1749
- GCC_except_table1751
- GCC_except_table1755
- GCC_except_table1759
- GCC_except_table1764
- GCC_except_table1769
- GCC_except_table1778
- GCC_except_table1793
- GCC_except_table1807
- GCC_except_table1809
- GCC_except_table1816
- GCC_except_table1825
- GCC_except_table1843
- GCC_except_table1866
- GCC_except_table1871
- GCC_except_table1893
- GCC_except_table1897
- GCC_except_table197
- GCC_except_table202
- GCC_except_table205
- GCC_except_table2074
- GCC_except_table2079
- GCC_except_table216
- GCC_except_table244
- GCC_except_table285
- GCC_except_table290
- GCC_except_table3
- GCC_except_table300
- GCC_except_table367
- GCC_except_table371
- GCC_except_table453
- GCC_except_table454
- GCC_except_table458
- GCC_except_table471
- GCC_except_table486
- GCC_except_table490
- GCC_except_table525
- GCC_except_table612
- GCC_except_table637
- GCC_except_table641
- GCC_except_table645
- GCC_except_table674
- GCC_except_table677
- GCC_except_table890
- GCC_except_table934
- GCC_except_table949
- GCC_except_table956
- _EventKitLibraryCore.frameworkLibrary.1601
- _EventKitLibraryCore.frameworkLibrary.6318
- ___21-[PPEventClient init]_block_invoke.108
- ___23-[PPContactClient init]_block_invoke.100
- ___27-[PPConnectionsClient init]_block_invoke.79
- ___29-[PPTopicReadOnlyClient init]_block_invoke.102
- ___31-[PPSocialHighlightClient init]_block_invoke.87
- ___31-[PPTemporalClusterClient init]_block_invoke.77
- ___32-[PPLocationReadOnlyClient init]_block_invoke.80
- ___35-[PPNamedEntityReadOnlyClient init]_block_invoke.82
- ___75+[PPCustomDonation donateLabeledStrings:bundleId:groupId:documentId:error:]_block_invoke.114
- ___95+[PPCustomDonation donateParsecNamedEntitiesAndTopics:rawQuery:reformulatedQuery:source:error:]_block_invoke.102
- ___Block_byref_object_copy_.1178
- ___Block_byref_object_copy_.1821
- ___Block_byref_object_copy_.2829
- ___Block_byref_object_copy_.3114
- ___Block_byref_object_copy_.3425
- ___Block_byref_object_copy_.3673
- ___Block_byref_object_copy_.379
- ___Block_byref_object_copy_.4291
- ___Block_byref_object_copy_.4461
- ___Block_byref_object_copy_.4726
- ___Block_byref_object_copy_.489
- ___Block_byref_object_copy_.5335
- ___Block_byref_object_copy_.5404
- ___Block_byref_object_copy_.551
- ___Block_byref_object_copy_.5727
- ___Block_byref_object_copy_.6098
- ___Block_byref_object_copy_.6307
- ___Block_byref_object_copy_.6703
- ___Block_byref_object_copy_.7478
- ___Block_byref_object_dispose_.1179
- ___Block_byref_object_dispose_.1822
- ___Block_byref_object_dispose_.2830
- ___Block_byref_object_dispose_.3115
- ___Block_byref_object_dispose_.3426
- ___Block_byref_object_dispose_.3674
- ___Block_byref_object_dispose_.380
- ___Block_byref_object_dispose_.4292
- ___Block_byref_object_dispose_.4462
- ___Block_byref_object_dispose_.4727
- ___Block_byref_object_dispose_.490
- ___Block_byref_object_dispose_.5336
- ___Block_byref_object_dispose_.5405
- ___Block_byref_object_dispose_.552
- ___Block_byref_object_dispose_.5728
- ___Block_byref_object_dispose_.6099
- ___Block_byref_object_dispose_.6308
- ___Block_byref_object_dispose_.6704
- ___Block_byref_object_dispose_.7479
- ___EventKitLibraryCore_block_invoke.1602
- ___EventKitLibraryCore_block_invoke.6319
- ___block_literal_global.103
- ___block_literal_global.105
- ___block_literal_global.118
- ___block_literal_global.129
- ___block_literal_global.135
- ___block_literal_global.1389
- ___block_literal_global.139
- ___block_literal_global.1593
- ___block_literal_global.1744
- ___block_literal_global.178.6362
- ___block_literal_global.18.7417
- ___block_literal_global.1800
- ___block_literal_global.2030
- ___block_literal_global.218.6311
- ___block_literal_global.27.7424
- ___block_literal_global.2709
- ___block_literal_global.2770
- ___block_literal_global.2827
- ___block_literal_global.3121
- ___block_literal_global.340
- ___block_literal_global.3433
- ___block_literal_global.3751
- ___block_literal_global.4116
- ___block_literal_global.4459
- ___block_literal_global.4600
- ___block_literal_global.4728
- ___block_literal_global.495
- ___block_literal_global.5411
- ___block_literal_global.5638
- ___block_literal_global.605
- ___block_literal_global.6400
- ___block_literal_global.6625
- ___block_literal_global.6749
- ___block_literal_global.70
- ___block_literal_global.71.7486
- ___block_literal_global.7403
- ___block_literal_global.7485
- ___block_literal_global.7513
- ___block_literal_global.78
- ___block_literal_global.8283
- ___block_literal_global.83
- ___block_literal_global.85
- ___block_literal_global.8643
- ___block_literal_global.91
- ___block_literal_global.91.5412
- ___block_literal_global.93
- ___block_literal_global.95
- _audit_stringEventKit.1614
- _audit_stringEventKit.6322
- _defaultStore._pasExprOnceResult.2417
- _defaultStore._pasExprOnceResult.9149
- _defaultStore._pasExprOnceResult.9517
- _defaultStore._pasOnceToken12.9516
- _featureNames._pasExprOnceResult.1745
- _featureNames._pasExprOnceResult.219
- _featureNames._pasExprOnceResult.3749
- _featureNames._pasExprOnceResult.4115
- _featureNames._pasExprOnceResult.6626
- _featureNames._pasExprOnceResult.8284
- _featureNames._pasOnceToken4.1743
- _featureNames._pasOnceToken4.6624
- _featureNames._pasOnceToken6.8282
- _featureNames._pasOnceToken9.8354
- _sharedInstance._pasExprOnceResult.2888
- _sharedInstance._pasExprOnceResult.3448
- _sharedInstance._pasExprOnceResult.365
- _sharedInstance._pasExprOnceResult.411
- _sharedInstance._pasExprOnceResult.4369
- _sharedInstance._pasExprOnceResult.5090
- _sharedInstance._pasExprOnceResult.5160
- _sharedInstance._pasExprOnceResult.520
- _sharedInstance._pasExprOnceResult.5449
- _sharedInstance._pasExprOnceResult.6144
- _sharedInstance._pasExprOnceResult.6401
- _sharedInstance._pasExprOnceResult.6479
- _sharedInstance._pasExprOnceResult.6552
- _sharedInstance._pasExprOnceResult.7504
- _sharedInstance._pasOnceToken12.4368
- _sharedInstance._pasOnceToken12.5089
- _sharedInstance._pasOnceToken12.6399
- _sharedInstance._pasOnceToken2.3447
- _sharedInstance._pasOnceToken2.519
- _sharedInstance._pasOnceToken2.5448
- _sharedInstance._pasOnceToken2.7503
- _sharedInstance._pasOnceToken6.5159
- _sharedInstance._pasOnceToken6.6478
- _sharedInstance._pasOnceToken8.6143
- _sharedInstance._pasOnceToken8.6551
CStrings:
+ "<PPSpotlightAttributes s:%f f:%tu v:%f ne:%tu>"
+ "<PPTextUnderstandingExtraction n:%tu t:%tu ta:%tu>"
+ "@40@0:8@16@24Q32"
+ "@48@0:8@16@24@32^@40"
+ "@48@0:8d16@24@32@40"
+ "PPSpotlightAttributes"
+ "PPTextUnderstandingClient"
+ "PPTextUnderstandingExtraction"
+ "PPTextUnderstandingServerProtocol"
+ "T@\"NSArray\",&,N,V_namedEntities"
+ "T@\"NSArray\",&,N,V_topics"
+ "T@\"NSData\",&,N,V_featureVector"
+ "T@\"NSDictionary\",&,N,V_namedEntityScores"
+ "T@\"NSNumber\",&,N,V_featureVectorVersion"
+ "TQ,N,V_topicAlgorithm"
+ "Td,N,V_staticScore"
+ "_featureVector"
+ "_featureVectorVersion"
+ "_namedEntities"
+ "_namedEntityScores"
+ "_staticScore"
+ "_topicAlgorithm"
+ "com.apple.proactive.PersonalizationPortrait.TextUnderstanding"
+ "featureVector"
+ "fev"
+ "fvv"
+ "initWithNamedEntities:topics:topicAlgorithm:"
+ "initWithStaticScore:featureVector:featureVectorVersion:namedEntityScores:"
+ "isEqualToSpotlightAttributes:"
+ "isEqualToTextUnderstandingExtraction:"
+ "namedEntities"
+ "namedEntityScores"
+ "nes"
+ "setFeatureVector:"
+ "setFeatureVectorVersion:"
+ "setNamedEntities:"
+ "setNamedEntityScores:"
+ "setStaticScore:"
+ "setTopicAlgorithm:"
+ "setTopics:"
+ "spotlightAttributesForBundleId:spotlightIdentifier:extractions:completion:"
+ "spotlightAttributesForBundleId:spotlightIdentifier:extractions:error:"
+ "ssc"
+ "staticScore"
+ "tal"
+ "topicAlgorithm"
+ "v24@?0@\"PPSpotlightAttributes\"8@\"NSError\"16"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@?<v@?@\"PPSpotlightAttributes\"@\"NSError\">40"

```
