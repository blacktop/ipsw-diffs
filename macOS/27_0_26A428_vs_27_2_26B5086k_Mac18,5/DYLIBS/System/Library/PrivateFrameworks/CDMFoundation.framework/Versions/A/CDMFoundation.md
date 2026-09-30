## CDMFoundation

> `/System/Library/PrivateFrameworks/CDMFoundation.framework/Versions/A/CDMFoundation`

```diff

-3600.31.14.0.0
-  __TEXT.__text: 0x271044
-  __TEXT.__objc_methlist: 0x8674
-  __TEXT.__const: 0xd3a8
+3605.16.1.0.0
+  __TEXT.__text: 0x288aac
+  __TEXT.__objc_methlist: 0x8cd0
+  __TEXT.__const: 0xd3b8
   __TEXT.__swift5_typeref: 0x4278
   __TEXT.__swift5_fieldmd: 0x3d80
   __TEXT.__constg_swiftt: 0x55d4
   __TEXT.__swift5_protos: 0x98
-  __TEXT.__cstring: 0x1b8a3
+  __TEXT.__cstring: 0x1c521
   __TEXT.__swift5_types: 0x574
   __TEXT.__swift5_proto: 0x9ac
   __TEXT.__swift5_reflstr: 0x306a
-  __TEXT.__oslogstring: 0x1ddb5
+  __TEXT.__oslogstring: 0x1f2a0
   __TEXT.__swift5_assocty: 0x438
   __TEXT.__swift5_capture: 0x196c
   __TEXT.__swift5_builtin: 0xf0

   __TEXT.__swift_as_entry: 0x23c
   __TEXT.__swift_as_ret: 0x270
   __TEXT.__swift_as_cont: 0x43c
-  __TEXT.__gcc_except_tab: 0xb5d0
+  __TEXT.__gcc_except_tab: 0xc604
   __TEXT.__ustring: 0x17c
-  __TEXT.__unwind_info: 0x97d8
+  __TEXT.__unwind_info: 0x9ad0
   __TEXT.__eh_frame: 0x7950
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__objc_classlist: 0x8d0
+  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x53f0
+  __DATA_CONST.__objc_selrefs: 0x54f0
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x408
-  __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0x26e0
-  __AUTH_CONST.__const: 0xddb0
-  __AUTH_CONST.__cfstring: 0x81e0
-  __AUTH_CONST.__objc_const: 0x128c0
+  __DATA_CONST.__objc_superrefs: 0x438
+  __DATA_CONST.__objc_arraydata: 0x260
+  __DATA_CONST.__got: 0x2710
+  __AUTH_CONST.__const: 0xdeb0
+  __AUTH_CONST.__cfstring: 0x86a0
+  __AUTH_CONST.__objc_const: 0x132a8
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__objc_intobj: 0x678
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x4ce0
-  __AUTH.__objc_data: 0x1168
+  __AUTH_CONST.__auth_got: 0x4ce8
+  __AUTH.__objc_data: 0x1438
   __AUTH.__data: 0x1090
-  __DATA.__objc_ivar: 0x7ac
+  __DATA.__objc_ivar: 0x7f0
   __DATA.__data: 0x1c88
   __DATA.__common: 0x350
   __DATA_DIRTY.__objc_data: 0x4a00

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12939
-  Symbols:   11326
-  CStrings:  4588
+  Functions: 13128
+  Symbols:   11610
+  CStrings:  4735
 
Symbols:
+ +[CDMBaseSpanMatchService convertToSpanMatchRequest:nlContext:connectionId:]
+ +[CDMBaseSpanMatchService convertToSpanMatchRequests:nlContext:connectionId:]
+ +[CDMClient(ContactNLU) graphNameForContactNLU]
+ +[CDMClient(MagicCompose) graphNameForMagicCompose]
+ +[CDMClient(NLU) buildNluRequestWithText:requestConnectionId:nlContext:previousUtterances:]
+ +[CDMClient(TrustedAgent) graphNameForTrustedAgent]
+ +[CDMComposerServiceUtils emitNluRequestInsights:]
+ +[CDMComposerServiceUtils requiresUtteranceRedactionForRequest:]
+ +[CDMContactNLURequestCommand serviceGraphName]
+ +[CDMContactNLURequestCommand supportsSecureCoding]
+ +[CDMContactNLUResponseCommand serviceGraphName]
+ +[CDMContactNLUResponseCommand supportsSecureCoding]
+ +[CDMContactNLUServiceGraph getNLXSchemaCDMServiceGraphName]
+ +[CDMContactNLUServiceGraph getUsageForAssetSetName:withLocale:]
+ +[CDMContactNLUServiceGraph requiredDAGServices]
+ +[CDMContactNLUServiceGraph requiresAssets]
+ +[CDMDateTimeAlignmentHelper entityHasExplicitDate:entityNodeIndex:forwardEdgeIndex:]
+ +[CDMDateTimeAlignmentHelper entityHasExplicitTime:entityNodeIndex:forwardEdgeIndex:]
+ +[CDMDateTimeAlignmentHelper extractInputTextForDateName:nameNodeIndex:spanInfo:alignmentsByNodeIndex:]
+ +[CDMDateTimeAlignmentHelper findDateNameSpansForNameNode:nameNodeIndex:]
+ +[CDMDateTimeAlignmentHelper findDefinedDateTimeRangeSpansForNameNode:nameNodeIndex:]
+ +[CDMDateTimeAlignmentHelper findEnclosingTaskVerbElementId:nodeIndex:invertedEdgeIndex:]
+ +[CDMDateTimeAlignmentHelper findNameNodeIndexForEntity:entityNodeIndex:forwardEdgeIndex:]
+ +[CDMDateTimeAlignmentHelper findNameParentNodeIndex:nameNodeIndex:parentElementId:invertedEdgeIndex:]
+ +[CDMDateTimeAlignmentHelper findOrCreateDateTimeNodeForReminder:reminderNodeIndex:forwardEdgeIndex:]
+ +[CDMDateTimeAlignmentHelper isCreateTaskTarget:entityNodeIndex:invertedEdgeIndex:]
+ +[CDMDateTimeAlignmentHelper processDateNameSpansForReminder:parseGraph:reminderNodeIndex:reminderNameNodeIndex:hasExplicitDate:hasNonDateTimeTrigger:forwardEdgeIndex:alignmentsByNodeIndex:]
+ +[CDMDateTimeAlignmentHelper processDateTimeAlignmentForReminder:reminderNodeIndex:reminderNameNodeIndex:forwardEdgeIndex:alignmentsByNodeIndex:]
+ +[CDMDateTimeAlignmentHelper processDefinedDateTimeRangeSpansForReminder:parseGraph:reminderNodeIndex:reminderNameNodeIndex:hasExplicitTime:hasNonDateTimeTrigger:forwardEdgeIndex:]
+ +[CDMDateTimeAlignmentHelper reminderHasNonDateTimeTrigger:reminderNodeIndex:forwardEdgeIndex:]
+ +[CDMMagicComposeRequestCommand serviceGraphName]
+ +[CDMMagicComposeRequestCommand supportsSecureCoding]
+ +[CDMMagicComposeResponseCommand serviceGraphName]
+ +[CDMMagicComposeResponseCommand supportsSecureCoding]
+ +[CDMMagicComposeServiceGraph getNLXSchemaCDMServiceGraphName]
+ +[CDMMagicComposeServiceGraph getUsageForAssetSetName:withLocale:]
+ +[CDMMagicComposeServiceGraph requiredDAGServices]
+ +[CDMMagicComposeServiceGraph requiresAssets]
+ +[CDMPostProcessUtils computeRecurrenceTrimmedRange:nodeIndex:matchingSpans:spanStart:spanEnd:outStart:outEnd:]
+ +[CDMPostProcessUtils isRecurrenceQualifierSpan:]
+ +[CDMServiceGraphUtil prepareCcqrTokens:currentTurn:previousTurns:utterance:locale:connectionId:]
+ +[CDMTokenizerProtoService createProtoTokenRequestWithAsrOutputs:locale:connectionId:]
+ +[CDMTrustedAgentRequestCommand serviceGraphName]
+ +[CDMTrustedAgentRequestCommand supportsSecureCoding]
+ +[CDMTrustedAgentResponseCommand serviceGraphName]
+ +[CDMTrustedAgentResponseCommand supportsSecureCoding]
+ +[CDMTrustedAgentServiceGraph getNLXSchemaCDMServiceGraphName]
+ +[CDMTrustedAgentServiceGraph getUsageForAssetSetName:withLocale:]
+ +[CDMTrustedAgentServiceGraph requiredDAGServices]
+ +[CDMTrustedAgentServiceGraph requiresAssets]
+ +[EntityKey reminderName]
+ -[CDMBaseSpanMatchService spanizeAsrs:asrSpansMap:topAsrSpans:topAsrSpansFiltered:asrHypotheses:connectionId:]
+ -[CDMBaseSpanMatchService spanizeTokenChain:spans:isTopAsr:topAsrSpansFiltered:asrHypothesis:connectionId:]
+ -[CDMCATIChildService checkExactMatchForUtterances:connectionId:]
+ -[CDMCATIProtoRequestCommand connectionId]
+ -[CDMCATIProtoRequestCommand setConnectionId:]
+ -[CDMClient processContactNluRequest:completionHandler:]
+ -[CDMClient processMagicComposeNluRequest:completionHandler:]
+ -[CDMClient processTrustedAgentNluRequest:completionHandler:]
+ -[CDMClient(MagicCompose) processMagicComposeText:requestConnectionId:nlContext:previousUtterances:completionHandler:]
+ -[CDMClient(NLURequestBuilder) buildNluRequestWithText:requestConnectionId:nlContext:previousUtterances:]
+ -[CDMClient(TrustedAgent) processTrustedAgentText:requestConnectionId:nlContext:completionHandler:]
+ -[CDMClient(TrustedAgent) setupTrustedAgentWithLocale:completionHandler:]
+ -[CDMClientInterface processContactNluRequest:completionHandler:]
+ -[CDMClientInterface processMagicComposeNluRequest:completionHandler:]
+ -[CDMClientInterface processTrustedAgentNluRequest:completionHandler:]
+ -[CDMComposerService _handleContactNLURequest:withCallback:]
+ -[CDMComposerService _handleMagicComposeRequest:withCallback:]
+ -[CDMComposerService _handleTrustedAgentRequest:withCallback:]
+ -[CDMContactNLURequestCommand .cxx_destruct]
+ -[CDMContactNLURequestCommand clientId]
+ -[CDMContactNLURequestCommand encodeWithCoder:]
+ -[CDMContactNLURequestCommand initWithCoder:]
+ -[CDMContactNLURequestCommand initWithNLURequest:clientId:]
+ -[CDMContactNLURequestCommand initWithNLURequest:clientId:dataDispatcherContext:]
+ -[CDMContactNLURequestCommand loggingRequestID]
+ -[CDMContactNLURequestCommand selfMetadata]
+ -[CDMContactNLURequestCommand setSelfMetadata:]
+ -[CDMContactNLURequestCommand siriNLUTypeObj]
+ -[CDMContactNLUResponseCommand .cxx_destruct]
+ -[CDMContactNLUResponseCommand encodeWithCoder:]
+ -[CDMContactNLUResponseCommand initWithCoder:]
+ -[CDMContactNLUResponseCommand initWithNLUResponse:requestId:]
+ -[CDMContactNLUResponseCommand requestId]
+ -[CDMContactNLUResponseCommand siriNLUTypeObj]
+ -[CDMContactNLUServiceGraph buildGraph]
+ -[CDMContactNLUServiceGraph supportedGraphInputType]
+ -[CDMDateTimeProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]
+ -[CDMFoundationClient processContactNluRequest:completionHandler:]
+ -[CDMFoundationClient processMagicComposeNluRequest:completionHandler:]
+ -[CDMFoundationClient(TrustedAgent) processTrustedAgentNluRequest:completionHandler:]
+ -[CDMMagicComposeRequestCommand .cxx_destruct]
+ -[CDMMagicComposeRequestCommand clientId]
+ -[CDMMagicComposeRequestCommand encodeWithCoder:]
+ -[CDMMagicComposeRequestCommand initWithCoder:]
+ -[CDMMagicComposeRequestCommand initWithNLURequest:clientId:]
+ -[CDMMagicComposeRequestCommand initWithNLURequest:clientId:dataDispatcherContext:]
+ -[CDMMagicComposeRequestCommand loggingRequestID]
+ -[CDMMagicComposeRequestCommand selfMetadata]
+ -[CDMMagicComposeRequestCommand setSelfMetadata:]
+ -[CDMMagicComposeRequestCommand siriNLUTypeObj]
+ -[CDMMagicComposeResponseCommand .cxx_destruct]
+ -[CDMMagicComposeResponseCommand encodeWithCoder:]
+ -[CDMMagicComposeResponseCommand initWithCoder:]
+ -[CDMMagicComposeResponseCommand initWithNLUResponse:requestId:]
+ -[CDMMagicComposeResponseCommand requestId]
+ -[CDMMagicComposeResponseCommand siriNLUTypeObj]
+ -[CDMMagicComposeServiceGraph buildGraph]
+ -[CDMMagicComposeServiceGraph supportedGraphInputType]
+ -[CDMRegexSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]
+ -[CDMSiriVocabularyProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]
+ -[CDMSpanMatcherRequestCommand connectionId]
+ -[CDMSpanMatcherRequestCommand setConnectionId:]
+ -[CDMTrustedAgentRequestCommand .cxx_destruct]
+ -[CDMTrustedAgentRequestCommand clientId]
+ -[CDMTrustedAgentRequestCommand encodeWithCoder:]
+ -[CDMTrustedAgentRequestCommand initWithCoder:]
+ -[CDMTrustedAgentRequestCommand initWithNLURequest:clientId:]
+ -[CDMTrustedAgentRequestCommand initWithNLURequest:clientId:dataDispatcherContext:]
+ -[CDMTrustedAgentRequestCommand loggingRequestID]
+ -[CDMTrustedAgentRequestCommand selfMetadata]
+ -[CDMTrustedAgentRequestCommand setSelfMetadata:]
+ -[CDMTrustedAgentRequestCommand siriNLUTypeObj]
+ -[CDMTrustedAgentResponseCommand .cxx_destruct]
+ -[CDMTrustedAgentResponseCommand encodeWithCoder:]
+ -[CDMTrustedAgentResponseCommand initWithCoder:]
+ -[CDMTrustedAgentResponseCommand initWithNLUResponse:requestId:]
+ -[CDMTrustedAgentResponseCommand requestId]
+ -[CDMTrustedAgentResponseCommand siriNLUTypeObj]
+ -[CDMTrustedAgentServiceGraph buildGraph]
+ -[CDMTrustedAgentServiceGraph supportedGraphInputType]
+ -[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]
+ -[CDMXPCClient processContactNluRequest:completionHandler:]
+ -[CDMXPCClient processMagicComposeNluRequest:completionHandler:]
+ -[CDMXPCClient processTrustedAgentNluRequest:completionHandler:]
+ CDMRedactedUtteranceRequesters.onceToken
+ CDMRedactedUtteranceRequesters.requesters
+ GCC_except_table1016
+ GCC_except_table1111
+ GCC_except_table1116
+ GCC_except_table1119
+ GCC_except_table1120
+ GCC_except_table1121
+ GCC_except_table1122
+ GCC_except_table1123
+ GCC_except_table1124
+ GCC_except_table1126
+ GCC_except_table1127
+ GCC_except_table1128
+ GCC_except_table1129
+ GCC_except_table1130
+ GCC_except_table1131
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table1172
+ GCC_except_table1173
+ GCC_except_table1174
+ GCC_except_table1175
+ GCC_except_table1176
+ GCC_except_table1177
+ GCC_except_table1179
+ GCC_except_table1182
+ GCC_except_table1183
+ GCC_except_table1186
+ GCC_except_table1189
+ GCC_except_table1233
+ GCC_except_table1234
+ GCC_except_table1236
+ GCC_except_table1237
+ GCC_except_table1238
+ GCC_except_table1239
+ GCC_except_table1240
+ GCC_except_table1241
+ GCC_except_table1242
+ GCC_except_table1243
+ GCC_except_table1244
+ GCC_except_table130
+ GCC_except_table1313
+ GCC_except_table1316
+ GCC_except_table1317
+ GCC_except_table1318
+ GCC_except_table1319
+ GCC_except_table1322
+ GCC_except_table1323
+ GCC_except_table1326
+ GCC_except_table1345
+ GCC_except_table1346
+ GCC_except_table1364
+ GCC_except_table1375
+ GCC_except_table1382
+ GCC_except_table1386
+ GCC_except_table1390
+ GCC_except_table1414
+ GCC_except_table1415
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table1444
+ GCC_except_table1445
+ GCC_except_table1446
+ GCC_except_table1447
+ GCC_except_table1448
+ GCC_except_table1449
+ GCC_except_table1451
+ GCC_except_table1452
+ GCC_except_table1453
+ GCC_except_table147
+ GCC_except_table1470
+ GCC_except_table1471
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table1522
+ GCC_except_table1523
+ GCC_except_table1524
+ GCC_except_table1562
+ GCC_except_table1565
+ GCC_except_table1566
+ GCC_except_table1567
+ GCC_except_table1568
+ GCC_except_table1569
+ GCC_except_table1570
+ GCC_except_table1571
+ GCC_except_table1572
+ GCC_except_table1573
+ GCC_except_table1574
+ GCC_except_table1575
+ GCC_except_table1576
+ GCC_except_table1577
+ GCC_except_table1578
+ GCC_except_table1582
+ GCC_except_table1583
+ GCC_except_table1584
+ GCC_except_table1585
+ GCC_except_table1586
+ GCC_except_table1587
+ GCC_except_table1588
+ GCC_except_table1589
+ GCC_except_table1590
+ GCC_except_table1591
+ GCC_except_table1592
+ GCC_except_table1593
+ GCC_except_table1594
+ GCC_except_table1595
+ GCC_except_table1596
+ GCC_except_table1597
+ GCC_except_table1615
+ GCC_except_table1619
+ GCC_except_table1620
+ GCC_except_table1621
+ GCC_except_table1622
+ GCC_except_table1623
+ GCC_except_table1624
+ GCC_except_table1625
+ GCC_except_table164
+ GCC_except_table1665
+ GCC_except_table1671
+ GCC_except_table1672
+ GCC_except_table1673
+ GCC_except_table1674
+ GCC_except_table1695
+ GCC_except_table171
+ GCC_except_table1717
+ GCC_except_table1718
+ GCC_except_table1719
+ GCC_except_table1720
+ GCC_except_table1721
+ GCC_except_table1722
+ GCC_except_table1723
+ GCC_except_table1724
+ GCC_except_table1725
+ GCC_except_table1726
+ GCC_except_table1728
+ GCC_except_table1729
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table1961
+ GCC_except_table1965
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table1981
+ GCC_except_table199
+ GCC_except_table2012
+ GCC_except_table2013
+ GCC_except_table2014
+ GCC_except_table2015
+ GCC_except_table2016
+ GCC_except_table2018
+ GCC_except_table2019
+ GCC_except_table2020
+ GCC_except_table2021
+ GCC_except_table2022
+ GCC_except_table2024
+ GCC_except_table2025
+ GCC_except_table2026
+ GCC_except_table2027
+ GCC_except_table2030
+ GCC_except_table2031
+ GCC_except_table2033
+ GCC_except_table2034
+ GCC_except_table2035
+ GCC_except_table2036
+ GCC_except_table2037
+ GCC_except_table2038
+ GCC_except_table2039
+ GCC_except_table2040
+ GCC_except_table2041
+ GCC_except_table2042
+ GCC_except_table2043
+ GCC_except_table2047
+ GCC_except_table2048
+ GCC_except_table2064
+ GCC_except_table2069
+ GCC_except_table2072
+ GCC_except_table2077
+ GCC_except_table2091
+ GCC_except_table2092
+ GCC_except_table2093
+ GCC_except_table2094
+ GCC_except_table2096
+ GCC_except_table2098
+ GCC_except_table2099
+ GCC_except_table2100
+ GCC_except_table2101
+ GCC_except_table2102
+ GCC_except_table2110
+ GCC_except_table2114
+ GCC_except_table2125
+ GCC_except_table2165
+ GCC_except_table2169
+ GCC_except_table2192
+ GCC_except_table2236
+ GCC_except_table2237
+ GCC_except_table2241
+ GCC_except_table2242
+ GCC_except_table2243
+ GCC_except_table2244
+ GCC_except_table2248
+ GCC_except_table2257
+ GCC_except_table2258
+ GCC_except_table2259
+ GCC_except_table2261
+ GCC_except_table2262
+ GCC_except_table2263
+ GCC_except_table2264
+ GCC_except_table2265
+ GCC_except_table2266
+ GCC_except_table2267
+ GCC_except_table2268
+ GCC_except_table2286
+ GCC_except_table2288
+ GCC_except_table2289
+ GCC_except_table2290
+ GCC_except_table2310
+ GCC_except_table2311
+ GCC_except_table2312
+ GCC_except_table2333
+ GCC_except_table2343
+ GCC_except_table2354
+ GCC_except_table240
+ GCC_except_table245
+ GCC_except_table2456
+ GCC_except_table247
+ GCC_except_table2481
+ GCC_except_table2482
+ GCC_except_table2484
+ GCC_except_table2485
+ GCC_except_table2486
+ GCC_except_table2487
+ GCC_except_table2488
+ GCC_except_table249
+ GCC_except_table2490
+ GCC_except_table2491
+ GCC_except_table2492
+ GCC_except_table2495
+ GCC_except_table2499
+ GCC_except_table2501
+ GCC_except_table251
+ GCC_except_table2512
+ GCC_except_table2513
+ GCC_except_table2514
+ GCC_except_table2515
+ GCC_except_table2516
+ GCC_except_table2517
+ GCC_except_table252
+ GCC_except_table2520
+ GCC_except_table2522
+ GCC_except_table2523
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table2595
+ GCC_except_table2596
+ GCC_except_table2597
+ GCC_except_table2598
+ GCC_except_table2599
+ GCC_except_table2600
+ GCC_except_table2601
+ GCC_except_table2602
+ GCC_except_table2603
+ GCC_except_table2604
+ GCC_except_table2605
+ GCC_except_table2606
+ GCC_except_table2641
+ GCC_except_table2643
+ GCC_except_table2644
+ GCC_except_table2645
+ GCC_except_table2646
+ GCC_except_table2648
+ GCC_except_table2649
+ GCC_except_table2650
+ GCC_except_table2651
+ GCC_except_table2652
+ GCC_except_table2653
+ GCC_except_table2654
+ GCC_except_table2655
+ GCC_except_table2656
+ GCC_except_table2657
+ GCC_except_table2659
+ GCC_except_table2661
+ GCC_except_table2662
+ GCC_except_table2664
+ GCC_except_table2665
+ GCC_except_table2666
+ GCC_except_table2742
+ GCC_except_table2743
+ GCC_except_table2744
+ GCC_except_table2745
+ GCC_except_table2746
+ GCC_except_table2747
+ GCC_except_table2748
+ GCC_except_table2749
+ GCC_except_table2750
+ GCC_except_table2751
+ GCC_except_table2752
+ GCC_except_table2753
+ GCC_except_table2754
+ GCC_except_table2755
+ GCC_except_table2756
+ GCC_except_table2757
+ GCC_except_table2759
+ GCC_except_table2779
+ GCC_except_table2803
+ GCC_except_table2804
+ GCC_except_table2805
+ GCC_except_table2811
+ GCC_except_table2812
+ GCC_except_table2813
+ GCC_except_table2814
+ GCC_except_table2815
+ GCC_except_table2816
+ GCC_except_table2817
+ GCC_except_table2847
+ GCC_except_table2849
+ GCC_except_table2852
+ GCC_except_table2879
+ GCC_except_table2880
+ GCC_except_table2907
+ GCC_except_table359
+ GCC_except_table365
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table371
+ GCC_except_table373
+ GCC_except_table375
+ GCC_except_table380
+ GCC_except_table382
+ GCC_except_table384
+ GCC_except_table386
+ GCC_except_table389
+ GCC_except_table391
+ GCC_except_table394
+ GCC_except_table399
+ GCC_except_table413
+ GCC_except_table426
+ GCC_except_table428
+ GCC_except_table431
+ GCC_except_table432
+ GCC_except_table477
+ GCC_except_table489
+ GCC_except_table516
+ GCC_except_table528
+ GCC_except_table540
+ GCC_except_table546
+ GCC_except_table552
+ GCC_except_table553
+ GCC_except_table554
+ GCC_except_table555
+ GCC_except_table557
+ GCC_except_table561
+ GCC_except_table567
+ GCC_except_table607
+ GCC_except_table612
+ GCC_except_table616
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table652
+ GCC_except_table655
+ GCC_except_table656
+ GCC_except_table670
+ GCC_except_table799
+ GCC_except_table842
+ GCC_except_table843
+ GCC_except_table846
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table849
+ GCC_except_table902
+ GCC_except_table905
+ GCC_except_table906
+ GCC_except_table907
+ GCC_except_table908
+ GCC_except_table909
+ GCC_except_table910
+ GCC_except_table925
+ GCC_except_table927
+ GCC_except_table928
+ GCC_except_table931
+ GCC_except_table932
+ GCC_except_table933
+ GCC_except_table934
+ GCC_except_table935
+ GCC_except_table936
+ GCC_except_table940
+ GCC_except_table941
+ GCC_except_table942
+ GCC_except_table943
+ GCC_except_table944
+ GCC_except_table945
+ GCC_except_table949
+ GCC_except_table952
+ GCC_except_table957
+ GCC_except_table958
+ GCC_except_table959
+ GCC_except_table963
+ OBJC_IVAR_$_CDMCATIProtoRequestCommand._connectionId
+ OBJC_IVAR_$_CDMContactNLURequestCommand._clientId
+ OBJC_IVAR_$_CDMContactNLURequestCommand._selfMetadata
+ OBJC_IVAR_$_CDMContactNLURequestCommand._siriNLUTypeObj
+ OBJC_IVAR_$_CDMContactNLUResponseCommand._requestId
+ OBJC_IVAR_$_CDMContactNLUResponseCommand._siriNLUTypeObj
+ OBJC_IVAR_$_CDMMagicComposeRequestCommand._clientId
+ OBJC_IVAR_$_CDMMagicComposeRequestCommand._selfMetadata
+ OBJC_IVAR_$_CDMMagicComposeRequestCommand._siriNLUTypeObj
+ OBJC_IVAR_$_CDMMagicComposeResponseCommand._requestId
+ OBJC_IVAR_$_CDMMagicComposeResponseCommand._siriNLUTypeObj
+ OBJC_IVAR_$_CDMSpanMatcherRequestCommand._connectionId
+ OBJC_IVAR_$_CDMTrustedAgentRequestCommand._clientId
+ OBJC_IVAR_$_CDMTrustedAgentRequestCommand._selfMetadata
+ OBJC_IVAR_$_CDMTrustedAgentRequestCommand._siriNLUTypeObj
+ OBJC_IVAR_$_CDMTrustedAgentResponseCommand._requestId
+ OBJC_IVAR_$_CDMTrustedAgentResponseCommand._siriNLUTypeObj
+ _AFDeviceSupportsSAEByDeviceCapabilityAndFeatureFlags
+ _CDMConnectionIdRequiresUtteranceRedaction
+ _OBJC_CLASS_$_CDMContactNLURequestCommand
+ _OBJC_CLASS_$_CDMContactNLUResponseCommand
+ _OBJC_CLASS_$_CDMContactNLUServiceGraph
+ _OBJC_CLASS_$_CDMMagicComposeRequestCommand
+ _OBJC_CLASS_$_CDMMagicComposeResponseCommand
+ _OBJC_CLASS_$_CDMMagicComposeServiceGraph
+ _OBJC_CLASS_$_CDMTrustedAgentRequestCommand
+ _OBJC_CLASS_$_CDMTrustedAgentResponseCommand
+ _OBJC_CLASS_$_CDMTrustedAgentServiceGraph
+ _OBJC_METACLASS_$_CDMContactNLURequestCommand
+ _OBJC_METACLASS_$_CDMContactNLUResponseCommand
+ _OBJC_METACLASS_$_CDMContactNLUServiceGraph
+ _OBJC_METACLASS_$_CDMMagicComposeRequestCommand
+ _OBJC_METACLASS_$_CDMMagicComposeResponseCommand
+ _OBJC_METACLASS_$_CDMMagicComposeServiceGraph
+ _OBJC_METACLASS_$_CDMTrustedAgentRequestCommand
+ _OBJC_METACLASS_$_CDMTrustedAgentResponseCommand
+ _OBJC_METACLASS_$_CDMTrustedAgentServiceGraph
+ __39-[CDMContactNLUServiceGraph buildGraph]_block_invoke
+ __41-[CDMMagicComposeServiceGraph buildGraph]_block_invoke
+ __41-[CDMTrustedAgentServiceGraph buildGraph]_block_invoke
+ __OBJC_$_CLASS_METHODS_CDMClient(NLUPreprocess|ShortcutDetector|ContactNLU|MagicCompose|TrustedAgent|NLU|NLURequestBuilder|Embedding|SsuInference)
+ __OBJC_$_CLASS_METHODS_CDMContactNLURequestCommand
+ __OBJC_$_CLASS_METHODS_CDMContactNLUResponseCommand
+ __OBJC_$_CLASS_METHODS_CDMContactNLUServiceGraph
+ __OBJC_$_CLASS_METHODS_CDMMagicComposeRequestCommand
+ __OBJC_$_CLASS_METHODS_CDMMagicComposeResponseCommand
+ __OBJC_$_CLASS_METHODS_CDMMagicComposeServiceGraph
+ __OBJC_$_CLASS_METHODS_CDMTrustedAgentRequestCommand
+ __OBJC_$_CLASS_METHODS_CDMTrustedAgentResponseCommand
+ __OBJC_$_CLASS_METHODS_CDMTrustedAgentServiceGraph
+ __OBJC_$_INSTANCE_METHODS_CDMClient(NLUPreprocess|ShortcutDetector|ContactNLU|MagicCompose|TrustedAgent|NLU|NLURequestBuilder|Embedding|SsuInference)
+ __OBJC_$_INSTANCE_METHODS_CDMContactNLURequestCommand
+ __OBJC_$_INSTANCE_METHODS_CDMContactNLUResponseCommand
+ __OBJC_$_INSTANCE_METHODS_CDMContactNLUServiceGraph
+ __OBJC_$_INSTANCE_METHODS_CDMFoundationClient(TrustedAgent|XPCEvent)
+ __OBJC_$_INSTANCE_METHODS_CDMMagicComposeRequestCommand
+ __OBJC_$_INSTANCE_METHODS_CDMMagicComposeResponseCommand
+ __OBJC_$_INSTANCE_METHODS_CDMMagicComposeServiceGraph
+ __OBJC_$_INSTANCE_METHODS_CDMTrustedAgentRequestCommand
+ __OBJC_$_INSTANCE_METHODS_CDMTrustedAgentResponseCommand
+ __OBJC_$_INSTANCE_METHODS_CDMTrustedAgentServiceGraph
+ __OBJC_$_INSTANCE_VARIABLES_CDMContactNLURequestCommand
+ __OBJC_$_INSTANCE_VARIABLES_CDMContactNLUResponseCommand
+ __OBJC_$_INSTANCE_VARIABLES_CDMMagicComposeRequestCommand
+ __OBJC_$_INSTANCE_VARIABLES_CDMMagicComposeResponseCommand
+ __OBJC_$_INSTANCE_VARIABLES_CDMTrustedAgentRequestCommand
+ __OBJC_$_INSTANCE_VARIABLES_CDMTrustedAgentResponseCommand
+ __OBJC_$_PROP_LIST_CDMContactNLURequestCommand
+ __OBJC_$_PROP_LIST_CDMContactNLUResponseCommand
+ __OBJC_$_PROP_LIST_CDMMagicComposeRequestCommand
+ __OBJC_$_PROP_LIST_CDMMagicComposeResponseCommand
+ __OBJC_$_PROP_LIST_CDMTrustedAgentRequestCommand
+ __OBJC_$_PROP_LIST_CDMTrustedAgentResponseCommand
+ __OBJC_CLASS_PROTOCOLS_$_CDMClient(NLUPreprocess|ShortcutDetector|ContactNLU|MagicCompose|TrustedAgent|NLU|NLURequestBuilder|Embedding|SsuInference)
+ __OBJC_CLASS_PROTOCOLS_$_CDMContactNLURequestCommand
+ __OBJC_CLASS_PROTOCOLS_$_CDMMagicComposeRequestCommand
+ __OBJC_CLASS_PROTOCOLS_$_CDMTrustedAgentRequestCommand
+ __OBJC_CLASS_RO_$_CDMContactNLURequestCommand
+ __OBJC_CLASS_RO_$_CDMContactNLUResponseCommand
+ __OBJC_CLASS_RO_$_CDMContactNLUServiceGraph
+ __OBJC_CLASS_RO_$_CDMMagicComposeRequestCommand
+ __OBJC_CLASS_RO_$_CDMMagicComposeResponseCommand
+ __OBJC_CLASS_RO_$_CDMMagicComposeServiceGraph
+ __OBJC_CLASS_RO_$_CDMTrustedAgentRequestCommand
+ __OBJC_CLASS_RO_$_CDMTrustedAgentResponseCommand
+ __OBJC_CLASS_RO_$_CDMTrustedAgentServiceGraph
+ __OBJC_METACLASS_RO_$_CDMContactNLURequestCommand
+ __OBJC_METACLASS_RO_$_CDMContactNLUResponseCommand
+ __OBJC_METACLASS_RO_$_CDMContactNLUServiceGraph
+ __OBJC_METACLASS_RO_$_CDMMagicComposeRequestCommand
+ __OBJC_METACLASS_RO_$_CDMMagicComposeResponseCommand
+ __OBJC_METACLASS_RO_$_CDMMagicComposeServiceGraph
+ __OBJC_METACLASS_RO_$_CDMTrustedAgentRequestCommand
+ __OBJC_METACLASS_RO_$_CDMTrustedAgentResponseCommand
+ __OBJC_METACLASS_RO_$_CDMTrustedAgentServiceGraph
+ ___25+[EntityKey reminderName]_block_invoke
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke_2
+ ___39-[CDMContactNLUServiceGraph buildGraph]_block_invoke
+ ___41-[CDMMagicComposeServiceGraph buildGraph]_block_invoke
+ ___41-[CDMTrustedAgentServiceGraph buildGraph]_block_invoke
+ ___52+[CDMComposerServiceUtils logNluRequestForInsights:]_block_invoke
+ ___59-[CDMXPCClient processContactNluRequest:completionHandler:]_block_invoke
+ ___59-[CDMXPCClient processContactNluRequest:completionHandler:]_block_invoke_2
+ ___60-[CDMComposerService _handleContactNLURequest:withCallback:]_block_invoke
+ ___62-[CDMComposerService _handleMagicComposeRequest:withCallback:]_block_invoke
+ ___62-[CDMComposerService _handleTrustedAgentRequest:withCallback:]_block_invoke
+ ___64-[CDMXPCClient processMagicComposeNluRequest:completionHandler:]_block_invoke
+ ___64-[CDMXPCClient processMagicComposeNluRequest:completionHandler:]_block_invoke_2
+ ___64-[CDMXPCClient processTrustedAgentNluRequest:completionHandler:]_block_invoke
+ ___64-[CDMXPCClient processTrustedAgentNluRequest:completionHandler:]_block_invoke_2
+ ___66-[CDMFoundationClient processContactNluRequest:completionHandler:]_block_invoke
+ ___71-[CDMFoundationClient processMagicComposeNluRequest:completionHandler:]_block_invoke
+ ___81-[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]_block_invoke
+ ___82+[CDMServiceGraphUtil mergeDateTimeSpans:regexSpans:siriVocabularySpans:vocSpans:]_block_invoke
+ ___85-[CDMFoundationClient(TrustedAgent) processTrustedAgentNluRequest:completionHandler:]_block_invoke
+ ___CDMRedactedUtteranceRequesters_block_invoke
+ ___block_descriptor_216_e8_32s40s48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208w_e29_v16?0"CDMServiceGraphNode"8l
+ ___block_descriptor_40_e8_32bs_e51_v24?0"SIRINLUEXTERNALCDMNluResponse"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e5_v8?0l
+ ___block_descriptor_48_e8_32s_e5_v8?0l
+ ___block_descriptor_49_e8_B16?08l
+ ___block_descriptor_64_ea8_32s40bs48w_e34_v24?0"<CDMCommand>"8"NSError"16l
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48l
+ ___copy_helper_block_e8_32s40s48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208w
+ ___copy_helper_block_e8_32s40s48s56s64r72r
+ ___destroy_helper_block_e8_32s40s48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208w
+ ___destroy_helper_block_e8_32s40s48s56s64r72r
+ _kIntelligenceFlowBundleId
+ _kSelfRequesterMagicCompose
+ _objc_msgSend$_handleContactNLURequest:withCallback:
+ _objc_msgSend$_handleMagicComposeRequest:withCallback:
+ _objc_msgSend$_handleTrustedAgentRequest:withCallback:
+ _objc_msgSend$buildNluRequestWithText:requestConnectionId:nlContext:previousUtterances:
+ _objc_msgSend$cdmRequestId
+ _objc_msgSend$checkExactMatchForUtterances:connectionId:
+ _objc_msgSend$computeRecurrenceTrimmedRange:nodeIndex:matchingSpans:spanStart:spanEnd:outStart:outEnd:
+ _objc_msgSend$convertToSpanMatchRequest:nlContext:connectionId:
+ _objc_msgSend$convertToSpanMatchRequests:nlContext:connectionId:
+ _objc_msgSend$createProtoTokenRequestWithAsrOutputs:locale:connectionId:
+ _objc_msgSend$emitNluRequestInsights:
+ _objc_msgSend$entityHasExplicitDate:entityNodeIndex:forwardEdgeIndex:
+ _objc_msgSend$entityHasExplicitTime:entityNodeIndex:forwardEdgeIndex:
+ _objc_msgSend$extractInputTextForDateName:nameNodeIndex:spanInfo:alignmentsByNodeIndex:
+ _objc_msgSend$findDateNameSpansForNameNode:nameNodeIndex:
+ _objc_msgSend$findDefinedDateTimeRangeSpansForNameNode:nameNodeIndex:
+ _objc_msgSend$findEnclosingTaskVerbElementId:nodeIndex:invertedEdgeIndex:
+ _objc_msgSend$findNameNodeIndexForEntity:entityNodeIndex:forwardEdgeIndex:
+ _objc_msgSend$findNameParentNodeIndex:nameNodeIndex:parentElementId:invertedEdgeIndex:
+ _objc_msgSend$findOrCreateDateTimeNodeForReminder:reminderNodeIndex:forwardEdgeIndex:
+ _objc_msgSend$graphNameForTrustedAgent
+ _objc_msgSend$hasUsoVerbElementId
+ _objc_msgSend$isCreateTaskTarget:entityNodeIndex:invertedEdgeIndex:
+ _objc_msgSend$isRecurrenceQualifierSpan:
+ _objc_msgSend$matchSpansForTokenChain:asrHypothesis:connectionId:
+ _objc_msgSend$prepareCcqrTokens:currentTurn:previousTurns:utterance:locale:connectionId:
+ _objc_msgSend$processContactNluRequest:completionHandler:
+ _objc_msgSend$processContactNluRequestWithCdmNluRequest:completionHandler:
+ _objc_msgSend$processDateNameSpansForReminder:parseGraph:reminderNodeIndex:reminderNameNodeIndex:hasExplicitDate:hasNonDateTimeTrigger:forwardEdgeIndex:alignmentsByNodeIndex:
+ _objc_msgSend$processDateTimeAlignmentForReminder:reminderNodeIndex:reminderNameNodeIndex:forwardEdgeIndex:alignmentsByNodeIndex:
+ _objc_msgSend$processDefinedDateTimeRangeSpansForReminder:parseGraph:reminderNodeIndex:reminderNameNodeIndex:hasExplicitTime:hasNonDateTimeTrigger:forwardEdgeIndex:
+ _objc_msgSend$processMagicComposeNluRequest:completionHandler:
+ _objc_msgSend$processMagicComposeNluRequestWithCdmNluRequest:completionHandler:
+ _objc_msgSend$processTrustedAgentNluRequest:completionHandler:
+ _objc_msgSend$processTrustedAgentNluRequestWithCdmNluRequest:completionHandler:
+ _objc_msgSend$reminderHasNonDateTimeTrigger:reminderNodeIndex:forwardEdgeIndex:
+ _objc_msgSend$reminderName
+ _objc_msgSend$requiresUtteranceRedactionForRequest:
+ _objc_msgSend$spanizeAsrs:asrSpansMap:topAsrSpans:topAsrSpansFiltered:asrHypotheses:connectionId:
+ _objc_msgSend$spanizeTokenChain:spans:isTopAsr:topAsrSpansFiltered:asrHypothesis:connectionId:
+ _objc_msgSend$usoVerbElementId
+ reminderName.onceToken
+ reminderName.value
- +[CDMBaseSpanMatchService convertToSpanMatchRequest:nlContext:]
- +[CDMBaseSpanMatchService convertToSpanMatchRequests:nlContext:]
- +[CDMDateTimeAlignmentHelper calendarEventHasExplicitDate:calendarEventNodeIndex:forwardEdgeIndex:]
- +[CDMDateTimeAlignmentHelper calendarEventHasExplicitTime:calendarEventNodeIndex:forwardEdgeIndex:]
- +[CDMDateTimeAlignmentHelper extractInputTextForDateName:calendarEventNameNodeIndex:spanInfo:alignmentsByNodeIndex:]
- +[CDMDateTimeAlignmentHelper findCalendarEventNameNodeIndex:calendarEventNodeIndex:forwardEdgeIndex:]
- +[CDMDateTimeAlignmentHelper findCalendarEventParentNodeIndex:calendarEventNameNodeIndex:invertedEdgeIndex:]
- +[CDMDateTimeAlignmentHelper findDateNameSpansForCalendarEventName:calendarEventNameNodeIndex:]
- +[CDMDateTimeAlignmentHelper findDefinedDateTimeRangeSpansForCalendarEventName:calendarEventNameNodeIndex:]
- +[CDMDateTimeAlignmentHelper isCalendarEventNameNode:nodeIndex:invertedEdgeIndex:]
- +[CDMServiceGraphUtil prepareCcqrTokens:currentTurn:previousTurns:utterance:locale:]
- +[CDMTokenizerProtoService createProtoTokenRequestWithAsrOutputs:locale:]
- -[CDMBaseSpanMatchService spanizeAsrs:asrSpansMap:topAsrSpans:topAsrSpansFiltered:asrHypotheses:]
- -[CDMBaseSpanMatchService spanizeTokenChain:spans:isTopAsr:topAsrSpansFiltered:asrHypothesis:]
- -[CDMCATIChildService checkExactMatchForUtterances:]
- -[CDMDateTimeProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:]
- -[CDMRegexSpanMatcher matchSpansForTokenChain:asrHypothesis:]
- -[CDMSiriVocabularyProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:]
- -[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:]
- GCC_except_table1007
- GCC_except_table1019
- GCC_except_table1020
- GCC_except_table1021
- GCC_except_table1022
- GCC_except_table1024
- GCC_except_table1027
- GCC_except_table1028
- GCC_except_table1031
- GCC_except_table1034
- GCC_except_table106
- GCC_except_table107
- GCC_except_table1078
- GCC_except_table1079
- GCC_except_table108
- GCC_except_table1080
- GCC_except_table1081
- GCC_except_table1082
- GCC_except_table1083
- GCC_except_table1084
- GCC_except_table1085
- GCC_except_table1086
- GCC_except_table1087
- GCC_except_table1088
- GCC_except_table1089
- GCC_except_table1158
- GCC_except_table1161
- GCC_except_table1163
- GCC_except_table1164
- GCC_except_table1167
- GCC_except_table1168
- GCC_except_table1171
- GCC_except_table1190
- GCC_except_table1191
- GCC_except_table1204
- GCC_except_table1209
- GCC_except_table121
- GCC_except_table1220
- GCC_except_table1227
- GCC_except_table1231
- GCC_except_table1251
- GCC_except_table1252
- GCC_except_table1253
- GCC_except_table1254
- GCC_except_table1255
- GCC_except_table1259
- GCC_except_table1260
- GCC_except_table1264
- GCC_except_table1265
- GCC_except_table1270
- GCC_except_table1289
- GCC_except_table129
- GCC_except_table1290
- GCC_except_table1291
- GCC_except_table1292
- GCC_except_table1293
- GCC_except_table1294
- GCC_except_table1295
- GCC_except_table1296
- GCC_except_table1297
- GCC_except_table1298
- GCC_except_table1299
- GCC_except_table133
- GCC_except_table135
- GCC_except_table1357
- GCC_except_table1358
- GCC_except_table1387
- GCC_except_table139
- GCC_except_table1395
- GCC_except_table1396
- GCC_except_table1397
- GCC_except_table1398
- GCC_except_table1399
- GCC_except_table140
- GCC_except_table1400
- GCC_except_table1401
- GCC_except_table1402
- GCC_except_table1403
- GCC_except_table1404
- GCC_except_table1405
- GCC_except_table1411
- GCC_except_table1412
- GCC_except_table1413
- GCC_except_table1417
- GCC_except_table1418
- GCC_except_table1421
- GCC_except_table1422
- GCC_except_table1423
- GCC_except_table1424
- GCC_except_table1426
- GCC_except_table1427
- GCC_except_table1428
- GCC_except_table1429
- GCC_except_table1430
- GCC_except_table1431
- GCC_except_table1432
- GCC_except_table1455
- GCC_except_table1456
- GCC_except_table1457
- GCC_except_table1458
- GCC_except_table1459
- GCC_except_table1460
- GCC_except_table1500
- GCC_except_table1506
- GCC_except_table1507
- GCC_except_table1508
- GCC_except_table1509
- GCC_except_table153
- GCC_except_table1530
- GCC_except_table155
- GCC_except_table1553
- GCC_except_table1554
- GCC_except_table1555
- GCC_except_table1556
- GCC_except_table1557
- GCC_except_table1558
- GCC_except_table1559
- GCC_except_table163
- GCC_except_table168
- GCC_except_table169
- GCC_except_table173
- GCC_except_table1758
- GCC_except_table1786
- GCC_except_table179
- GCC_except_table1790
- GCC_except_table180
- GCC_except_table1806
- GCC_except_table1808
- GCC_except_table181
- GCC_except_table1837
- GCC_except_table1838
- GCC_except_table1839
- GCC_except_table1840
- GCC_except_table1841
- GCC_except_table1843
- GCC_except_table1844
- GCC_except_table1845
- GCC_except_table1846
- GCC_except_table1847
- GCC_except_table1849
- GCC_except_table1850
- GCC_except_table1851
- GCC_except_table1852
- GCC_except_table1855
- GCC_except_table1856
- GCC_except_table1858
- GCC_except_table1859
- GCC_except_table1860
- GCC_except_table1861
- GCC_except_table1862
- GCC_except_table1866
- GCC_except_table1867
- GCC_except_table1883
- GCC_except_table1888
- GCC_except_table1891
- GCC_except_table1894
- GCC_except_table1895
- GCC_except_table1896
- GCC_except_table1897
- GCC_except_table1898
- GCC_except_table1899
- GCC_except_table1900
- GCC_except_table1901
- GCC_except_table1902
- GCC_except_table1903
- GCC_except_table1904
- GCC_except_table1905
- GCC_except_table1906
- GCC_except_table1907
- GCC_except_table1908
- GCC_except_table1909
- GCC_except_table1910
- GCC_except_table1911
- GCC_except_table1912
- GCC_except_table1913
- GCC_except_table1915
- GCC_except_table1916
- GCC_except_table1917
- GCC_except_table1918
- GCC_except_table1919
- GCC_except_table1920
- GCC_except_table1921
- GCC_except_table1922
- GCC_except_table1923
- GCC_except_table1924
- GCC_except_table1929
- GCC_except_table1944
- GCC_except_table1945
- GCC_except_table1946
- GCC_except_table1987
- GCC_except_table1989
- GCC_except_table2010
- GCC_except_table2054
- GCC_except_table2055
- GCC_except_table2059
- GCC_except_table2060
- GCC_except_table2061
- GCC_except_table2062
- GCC_except_table2066
- GCC_except_table2074
- GCC_except_table2106
- GCC_except_table2107
- GCC_except_table2121
- GCC_except_table2128
- GCC_except_table2129
- GCC_except_table2147
- GCC_except_table2150
- GCC_except_table2153
- GCC_except_table2160
- GCC_except_table222
- GCC_except_table227
- GCC_except_table2277
- GCC_except_table2279
- GCC_except_table229
- GCC_except_table2295
- GCC_except_table2296
- GCC_except_table2298
- GCC_except_table2299
- GCC_except_table2300
- GCC_except_table2301
- GCC_except_table2302
- GCC_except_table2305
- GCC_except_table2306
- GCC_except_table231
- GCC_except_table2313
- GCC_except_table2315
- GCC_except_table2326
- GCC_except_table2327
- GCC_except_table2328
- GCC_except_table2329
- GCC_except_table233
- GCC_except_table2331
- GCC_except_table2334
- GCC_except_table2337
- GCC_except_table234
- GCC_except_table235
- GCC_except_table236
- GCC_except_table2409
- GCC_except_table2410
- GCC_except_table2411
- GCC_except_table2412
- GCC_except_table2413
- GCC_except_table2414
- GCC_except_table2415
- GCC_except_table2416
- GCC_except_table2417
- GCC_except_table2418
- GCC_except_table2419
- GCC_except_table2420
- GCC_except_table2460
- GCC_except_table2462
- GCC_except_table2464
- GCC_except_table2467
- GCC_except_table2468
- GCC_except_table2469
- GCC_except_table2470
- GCC_except_table2471
- GCC_except_table2472
- GCC_except_table2474
- GCC_except_table2475
- GCC_except_table2476
- GCC_except_table2477
- GCC_except_table2478
- GCC_except_table2479
- GCC_except_table2480
- GCC_except_table2554
- GCC_except_table2555
- GCC_except_table2556
- GCC_except_table2557
- GCC_except_table2558
- GCC_except_table2559
- GCC_except_table2560
- GCC_except_table2561
- GCC_except_table2562
- GCC_except_table2563
- GCC_except_table2564
- GCC_except_table2565
- GCC_except_table2566
- GCC_except_table2567
- GCC_except_table2568
- GCC_except_table2569
- GCC_except_table2571
- GCC_except_table2591
- GCC_except_table2614
- GCC_except_table2615
- GCC_except_table2616
- GCC_except_table2622
- GCC_except_table2623
- GCC_except_table2624
- GCC_except_table2625
- GCC_except_table2626
- GCC_except_table2627
- GCC_except_table2628
- GCC_except_table2690
- GCC_except_table2691
- GCC_except_table2718
- GCC_except_table281
- GCC_except_table287
- GCC_except_table289
- GCC_except_table291
- GCC_except_table293
- GCC_except_table295
- GCC_except_table297
- GCC_except_table302
- GCC_except_table304
- GCC_except_table306
- GCC_except_table308
- GCC_except_table311
- GCC_except_table313
- GCC_except_table316
- GCC_except_table321
- GCC_except_table323
- GCC_except_table335
- GCC_except_table348
- GCC_except_table350
- GCC_except_table353
- GCC_except_table354
- GCC_except_table395
- GCC_except_table402
- GCC_except_table403
- GCC_except_table404
- GCC_except_table406
- GCC_except_table410
- GCC_except_table416
- GCC_except_table451
- GCC_except_table456
- GCC_except_table460
- GCC_except_table461
- GCC_except_table462
- GCC_except_table497
- GCC_except_table500
- GCC_except_table644
- GCC_except_table687
- GCC_except_table688
- GCC_except_table691
- GCC_except_table692
- GCC_except_table693
- GCC_except_table694
- GCC_except_table747
- GCC_except_table750
- GCC_except_table751
- GCC_except_table752
- GCC_except_table753
- GCC_except_table754
- GCC_except_table755
- GCC_except_table770
- GCC_except_table772
- GCC_except_table773
- GCC_except_table776
- GCC_except_table777
- GCC_except_table778
- GCC_except_table779
- GCC_except_table780
- GCC_except_table781
- GCC_except_table785
- GCC_except_table786
- GCC_except_table787
- GCC_except_table788
- GCC_except_table789
- GCC_except_table790
- GCC_except_table794
- GCC_except_table797
- GCC_except_table801
- GCC_except_table802
- GCC_except_table803
- GCC_except_table804
- GCC_except_table808
- GCC_except_table809
- GCC_except_table813
- GCC_except_table821
- GCC_except_table861
- GCC_except_table862
- GCC_except_table863
- GCC_except_table961
- GCC_except_table965
- GCC_except_table966
- GCC_except_table967
- GCC_except_table969
- GCC_except_table971
- GCC_except_table972
- GCC_except_table973
- GCC_except_table974
- GCC_except_table975
- __OBJC_$_CLASS_METHODS_CDMClient(NLUPreprocess|ShortcutDetector|NLU|Embedding|SsuInference)
- __OBJC_$_INSTANCE_METHODS_CDMClient(NLUPreprocess|ShortcutDetector|NLU|Embedding|SsuInference)
- __OBJC_$_INSTANCE_METHODS_CDMFoundationClient(XPCEvent)
- __OBJC_CLASS_PROTOCOLS_$_CDMClient(NLUPreprocess|ShortcutDetector|NLU|Embedding|SsuInference)
- ___68-[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:]_block_invoke
- ___block_descriptor_40_e8_B16?08l
- ___block_descriptor_56_e8_32s40r48r_e29_v16?0"CDMServiceGraphNode"8l
- ___block_descriptor_72_e8_32s40s48s56r64r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48l
- ___copy_helper_block_e8_32s40s48s56r64r
- _objc_msgSend$calendarEventHasExplicitDate:calendarEventNodeIndex:forwardEdgeIndex:
- _objc_msgSend$calendarEventHasExplicitTime:calendarEventNodeIndex:forwardEdgeIndex:
- _objc_msgSend$checkExactMatchForUtterances:
- _objc_msgSend$convertToSpanMatchRequest:nlContext:
- _objc_msgSend$convertToSpanMatchRequests:nlContext:
- _objc_msgSend$createProtoTokenRequestWithAsrOutputs:locale:
- _objc_msgSend$extractInputTextForDateName:calendarEventNameNodeIndex:spanInfo:alignmentsByNodeIndex:
- _objc_msgSend$findCalendarEventNameNodeIndex:calendarEventNodeIndex:forwardEdgeIndex:
- _objc_msgSend$findCalendarEventParentNodeIndex:calendarEventNameNodeIndex:invertedEdgeIndex:
- _objc_msgSend$findDateNameSpansForCalendarEventName:calendarEventNameNodeIndex:
- _objc_msgSend$findDefinedDateTimeRangeSpansForCalendarEventName:calendarEventNameNodeIndex:
- _objc_msgSend$isCalendarEventNameNode:nodeIndex:invertedEdgeIndex:
- _objc_msgSend$matchSpansForTokenChain:asrHypothesis:
- _objc_msgSend$prepareCcqrTokens:currentTurn:previousTurns:utterance:locale:
- _objc_msgSend$spanizeAsrs:asrSpansMap:topAsrSpans:topAsrSpansFiltered:asrHypotheses:
- _objc_msgSend$spanizeTokenChain:spans:isTopAsr:topAsrSpansFiltered:asrHypothesis:
CStrings:
+ "%s ASR #%d: Added asr.UUID=%@, trimmed=%{sensitive}@"
+ "%s ASR #%d: Processing asr.UUID=%@, asr.utterance=%{sensitive}@"
+ "%s ASR #%d: Skipping trimmed empty version of asr.UUID=%@, asr.utterance=%{sensitive}@"
+ "%s CATI normalized utterance: %{sensitive}@"
+ "%s CATI original utterance: %{sensitive}@"
+ "%s CDM Magic Compose graph finished processing, sending response back to caller: %@"
+ "%s CDM TrustedAgent client graph setup, locale=%@"
+ "%s CDM TrustedAgent graph finished processing, sending response back to caller: %@"
+ "%s CDM contact graph finished processing, sending response back to caller: %@"
+ "%s CDMFoundationClient processContactNluRequest... %@"
+ "%s CDMFoundationClient processMagicComposeNluRequest... %@"
+ "%s CDMFoundationClient processTrustedAgentNluRequest... %@"
+ "%s Completed Reminder Date.name double-alignment at node %u"
+ "%s Completed Reminder definedDateTimeRange double-alignment at node %u with definedValue '%@'"
+ "%s Converted TokenizerResponse -> SpanMatchRequest for utterance: %{sensitive}@"
+ "%s Date.name span [%u, %u] is outside entity .name span [%u, %u]"
+ "%s Entity .name node %u has no stringPayload"
+ "%s Entity .name node index %u out of bounds"
+ "%s Entity already has a .date edge from node %u (descendant of entity at node %u)"
+ "%s Entity has ambiguous time (common_Time) at node %u (descendant of entity at node %u) - allowing double-alignment"
+ "%s Entity has explicit time (element ID %u) at node %u (descendant of entity at node %u) - blocking double-alignment"
+ "%s Extracted from NluRequest.previousTurnInputs, previous asr hypo: %{sensitive}@"
+ "%s Extracted input text '%@' from entityNameText '%@' using indices [%u, %u] (relative [%u, %u])"
+ "%s Failed to extract input text for Reminder Date.name - falling back to valueString"
+ "%s For utterance <%{sensitive}@>, CDMRegexSpanMatcher matched text: <%{sensitive}@>, label: <%@>, start index: <%zu>, end index: <%zu>"
+ "%s Found 1 Date.name span for Reminder.name at node %u"
+ "%s Found 1 definedDateTimeRange span for Reminder.name at node %u"
+ "%s LVC Request for utterance: %{sensitive}s"
+ "%s No AER rewrite to apply; using original utterance tokens"
+ "%s No alignment found for entity .name node %u"
+ "%s Original text is '<%{sensitive}@>' with u16 size <%zu>. Text after filtering bidi characters is' <%{sensitive}@>' with u16 size <%zu>."
+ "%s PSC Request for utterance: %{sensitive}s"
+ "%s Relative end index %u exceeds entityNameText length %lu"
+ "%s Reminder EventTrigger at node %u has non-dateTimeTrigger attribute (edge element %u)"
+ "%s Reusing existing DateTime node %u reached via edge element %u"
+ "%s SNLC Request for utterance: %{sensitive}s"
+ "%s Sending CDMNluResponse to caller via callback in CDMClient"
+ "%s Sending XPC Magic Compose NLU request to service -> %@"
+ "%s Sending XPC TrustedAgent NLU request to service -> %@"
+ "%s Sending XPC contact NLU request to service -> %@"
+ "%s Skip node logic #1: Non-empty overridesProtoResponse.parsesForReplacement, will initiate skip of NLv4 inference node"
+ "%s Skipping Reminder Date.name double-alignment at node %u - EventTrigger already has a non-dateTimeTrigger condition"
+ "%s Skipping Reminder Date.name double-alignment at node %u - explicit date already exists"
+ "%s Skipping Reminder Date.name double-alignment at node %u - multiple Date.name spans found (%lu)"
+ "%s Skipping Reminder definedDateTimeRange double-alignment at node %u - DateTime node %u already has an .occurringIn edge"
+ "%s Skipping Reminder definedDateTimeRange double-alignment at node %u - EventTrigger already has a non-dateTimeTrigger condition"
+ "%s Skipping Reminder definedDateTimeRange double-alignment at node %u - explicit time already exists"
+ "%s Skipping Reminder definedDateTimeRange double-alignment at node %u - multiple definedDateTimeRange spans found (%lu), user should specify time"
+ "%s Skipping double-alignment for entity at node %u - enclosing task verb %u is not create"
+ "%s Spanized utterance: [%{sensitive}@]; Created %lu span(s) for span matcher: %@"
+ "%s Start spanizing utterance: [%{sensitive}@]; with span matcher: %@"
+ "%s Voc matcher Matching search chunk: %{sensitive}@"
+ "%s XPC response to Magic Compose NLU request <- %@"
+ "%s XPC response to TrustedAgent NLU request <- %@"
+ "%s XPC response to contact NLU request <- %@"
+ "%s [ERR]: CDM Magic Compose NLU processing failed: %s"
+ "%s [ERR]: CDM Magic Compose NLU request rejected: client setup has not succeeded"
+ "%s [ERR]: CDM TrustedAgent NLU processing failed: %s"
+ "%s [ERR]: CDM TrustedAgent NLU request rejected: client setup has not succeeded"
+ "%s [ERR]: CDM contact NLU processing failed: %s"
+ "%s [ERR]: CDM contact NLU request rejected: client setup has not succeeded"
+ "%s [ERR]: No CDMUAFClientManager for assetSetName: %@ (graph: %@, locale: %@). Reporting assets unavailable. Lookup error: %@"
+ "%s [ERR]: Sending Error to caller via callback in CDMClient, Error:%@"
+ "%s [ERR]: Using processContactNluRequest:completionHandler with delegate is not supported use [CDMClient init]"
+ "%s [ERR]: Using processMagicComposeNluRequest:completionHandler with delegate is not supported use [CDMClient init]"
+ "%s [ERR]: Using processTrustedAgentNluRequest:completionHandler with delegate is not supported use [CDMClient init]"
+ "%s [insights-cdm-%@]:\nCurrent Turn Utterance: %{sensitive}@"
+ "%s [insights-cdm-%@]:\nMENTIONRESOLVERRequest: %{sensitive}@"
+ "%s [insights-cdm-%@]:\nPrevious Turn %d Utterance: %{sensitive}@"
+ "%s [insights-cdm-%@]:\nQUERYREWRITEQRRequest: %{sensitive}@"
+ "%s [insights-cdm-%@]:\nServiceGraphNLUResponse: %{sensitive}@"
+ "%s doCorrectedUtteranceTokenize: re-tokenizing CCQR rewrite (%@): '%@'"
+ "%s doCorrectedUtteranceTokenize: re-tokenizing CCQR rewrite (%@): '%{sensitive}@'"
+ "+[CDMBaseSpanMatchService convertToSpanMatchRequest:nlContext:connectionId:]"
+ "+[CDMComposerServiceUtils emitNluRequestInsights:]"
+ "+[CDMContactNLUServiceGraph getUsageForAssetSetName:withLocale:]"
+ "+[CDMDateTimeAlignmentHelper entityHasExplicitDate:entityNodeIndex:forwardEdgeIndex:]"
+ "+[CDMDateTimeAlignmentHelper entityHasExplicitTime:entityNodeIndex:forwardEdgeIndex:]"
+ "+[CDMDateTimeAlignmentHelper extractInputTextForDateName:nameNodeIndex:spanInfo:alignmentsByNodeIndex:]"
+ "+[CDMDateTimeAlignmentHelper findDateNameSpansForNameNode:nameNodeIndex:]"
+ "+[CDMDateTimeAlignmentHelper findDefinedDateTimeRangeSpansForNameNode:nameNodeIndex:]"
+ "+[CDMDateTimeAlignmentHelper findOrCreateDateTimeNodeForCalendarEvent:calendarEventNodeIndex:forwardEdgeIndex:]"
+ "+[CDMDateTimeAlignmentHelper isCreateTaskTarget:entityNodeIndex:invertedEdgeIndex:]"
+ "+[CDMDateTimeAlignmentHelper processDateNameSpansForReminder:parseGraph:reminderNodeIndex:reminderNameNodeIndex:hasExplicitDate:hasNonDateTimeTrigger:forwardEdgeIndex:alignmentsByNodeIndex:]"
+ "+[CDMDateTimeAlignmentHelper processDefinedDateTimeRangeSpansForReminder:parseGraph:reminderNodeIndex:reminderNameNodeIndex:hasExplicitTime:hasNonDateTimeTrigger:forwardEdgeIndex:]"
+ "+[CDMDateTimeAlignmentHelper reminderHasNonDateTimeTrigger:reminderNodeIndex:forwardEdgeIndex:]"
+ "+[CDMMagicComposeServiceGraph getUsageForAssetSetName:withLocale:]"
+ "+[CDMServiceGraphUtil mergeDateTimeSpans:regexSpans:siriVocabularySpans:vocSpans:]_block_invoke"
+ "+[CDMServiceGraphUtil prepareCcqrTokens:currentTurn:previousTurns:utterance:locale:connectionId:]"
+ "+[CDMTokenizerProtoService createProtoTokenRequestWithAsrOutputs:locale:connectionId:]"
+ "+[CDMTrustedAgentServiceGraph getUsageForAssetSetName:withLocale:]"
+ "-[CDMBaseSpanMatchService spanizeAsrs:asrSpansMap:topAsrSpans:topAsrSpansFiltered:asrHypotheses:connectionId:]"
+ "-[CDMBaseSpanMatchService spanizeTokenChain:spans:isTopAsr:topAsrSpansFiltered:asrHypothesis:connectionId:]"
+ "-[CDMCATIChildService checkExactMatchForUtterances:connectionId:]"
+ "-[CDMClient(TrustedAgent) setupTrustedAgentWithLocale:completionHandler:]"
+ "-[CDMComposerService _handleContactNLURequest:withCallback:]_block_invoke"
+ "-[CDMComposerService _handleMagicComposeRequest:withCallback:]_block_invoke"
+ "-[CDMComposerService _handleTrustedAgentRequest:withCallback:]_block_invoke"
+ "-[CDMContactNLUServiceGraph buildGraph]_block_invoke"
+ "-[CDMFoundationClient processContactNluRequest:completionHandler:]"
+ "-[CDMFoundationClient processContactNluRequest:completionHandler:]_block_invoke"
+ "-[CDMFoundationClient processMagicComposeNluRequest:completionHandler:]"
+ "-[CDMFoundationClient processMagicComposeNluRequest:completionHandler:]_block_invoke"
+ "-[CDMFoundationClient(TrustedAgent) processTrustedAgentNluRequest:completionHandler:]"
+ "-[CDMFoundationClient(TrustedAgent) processTrustedAgentNluRequest:completionHandler:]_block_invoke"
+ "-[CDMMagicComposeServiceGraph buildGraph]_block_invoke"
+ "-[CDMNLUServiceGraph buildGraph]_block_invoke_2"
+ "-[CDMRegexSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]"
+ "-[CDMSiriVocabularyProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]"
+ "-[CDMTrustedAgentServiceGraph buildGraph]_block_invoke"
+ "-[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]"
+ "-[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]_block_invoke"
+ "-[CDMXPCClient processContactNluRequest:completionHandler:]"
+ "-[CDMXPCClient processContactNluRequest:completionHandler:]_block_invoke_2"
+ "-[CDMXPCClient processMagicComposeNluRequest:completionHandler:]"
+ "-[CDMXPCClient processMagicComposeNluRequest:completionHandler:]_block_invoke_2"
+ "-[CDMXPCClient processTrustedAgentNluRequest:completionHandler:]"
+ "-[CDMXPCClient processTrustedAgentNluRequest:completionHandler:]_block_invoke_2"
+ "1OCP"
+ "CDMContactNLUServiceGraph"
+ "CDMMagicComposeServiceGraph"
+ "CDMTrustedAgentServiceGraph"
+ "Caller calling CDM with a Magic Compose CDMNluRequest"
+ "Caller calling CDM with a TrustedAgent CDMNluRequest"
+ "Caller calling CDM with a contact CDMNluRequest"
+ "Caller received a Magic Compose CDMNluResponse (or error) from CDM"
+ "Caller received a TrustedAgent CDMNluResponse (or error) from CDM"
+ "Caller received a contact CDMNluResponse (or error) from CDM"
+ "Every"
+ "LOCALE_ACW_SA"
+ "LOCALE_AFB_AE"
+ "LOCALE_AJP_JO"
+ "LOCALE_AJP_PS"
+ "LOCALE_APC_LB"
+ "LOCALE_APC_SY"
+ "LOCALE_ARS_SA"
+ "LOCALE_ARZ_EG"
+ "LOCALE_AZ_AZ"
+ "LOCALE_BE_BY"
+ "LOCALE_BG_BG"
+ "LOCALE_BN_IN"
+ "LOCALE_ET_EE"
+ "LOCALE_GU_IN"
+ "LOCALE_HI_LATN"
+ "LOCALE_IS_IS"
+ "LOCALE_KN_IN"
+ "LOCALE_ML_IN"
+ "LOCALE_MR_IN"
+ "LOCALE_PA_IN"
+ "LOCALE_SL_SI"
+ "LOCALE_SR_RS"
+ "LOCALE_TA_IN"
+ "LOCALE_TE_IN"
+ "LOCALE_UR_IN"
+ "LOCALE_UZ_UZ"
+ "MAGIC_COMPOSE"
+ "On device TrustedAgent NL process time enableTelemetry=YES"
+ "On device contact NL process time enableTelemetry=YES"
+ "Using processContactNluRequest:completionHandler with delegate not supported"
+ "Using processMagicComposeNluRequest:completionHandler with delegate not supported"
+ "Using processTrustedAgentNluRequest:completionHandler with delegate not supported"
+ "com.apple.intelligenceflow.intelligenceflowd"
+ "contactRequestSent"
+ "contactResponseReceived"
+ "handleContactNLU"
+ "handleTrustedAgent"
+ "inference"
+ "nluRequest"
+ "ondevice_contact_nl_time"
+ "ondevice_trusted_agent_nl_time"
+ "override"
+ "responseReceived"
+ "trustedAgentRequestSent"
+ "trustedAgentResponseReceived"
- "%s CalendarEvent already has a .date edge from node %u (descendant of CalendarEvent at node %u)"
- "%s CalendarEvent has ambiguous time (common_Time) at node %u (descendant of CalendarEvent at node %u) - allowing double-alignment"
- "%s CalendarEvent has explicit time (element ID %u) at node %u (descendant of CalendarEvent at node %u) - blocking double-alignment"
- "%s CalendarEvent.name node %u has no stringPayload"
- "%s CalendarEvent.name node index %u out of bounds"
- "%s Current Turn is NOT a Correction for the previous turn"
- "%s Date.name span [%u, %u] is outside CalendarEvent.name span [%u, %u]"
- "%s Extracted input text '%@' from eventNameText '%@' using indices [%u, %u] (relative [%u, %u])"
- "%s No alignment found for CalendarEvent.name node %u"
- "%s Relative end index %u exceeds eventNameText length %lu"
- "%s doCorrectedUtteranceTokenize: re-tokenizing CCQR rewrite: '%@'"
- "+[CDMBaseSpanMatchService convertToSpanMatchRequest:nlContext:]"
- "+[CDMComposerServiceUtils logNluRequestForInsights:]"
- "+[CDMDateTimeAlignmentHelper calendarEventHasExplicitDate:calendarEventNodeIndex:forwardEdgeIndex:]"
- "+[CDMDateTimeAlignmentHelper calendarEventHasExplicitTime:calendarEventNodeIndex:forwardEdgeIndex:]"
- "+[CDMDateTimeAlignmentHelper extractInputTextForDateName:calendarEventNameNodeIndex:spanInfo:alignmentsByNodeIndex:]"
- "+[CDMDateTimeAlignmentHelper findDateNameSpansForCalendarEventName:calendarEventNameNodeIndex:]"
- "+[CDMDateTimeAlignmentHelper findDefinedDateTimeRangeSpansForCalendarEventName:calendarEventNameNodeIndex:]"
- "+[CDMServiceGraphUtil prepareCcqrTokens:currentTurn:previousTurns:utterance:locale:]"
- "+[CDMTokenizerProtoService createProtoTokenRequestWithAsrOutputs:locale:]"
- "-[CDMBaseSpanMatchService spanizeAsrs:asrSpansMap:topAsrSpans:topAsrSpansFiltered:asrHypotheses:]"
- "-[CDMBaseSpanMatchService spanizeTokenChain:spans:isTopAsr:topAsrSpansFiltered:asrHypothesis:]"
- "-[CDMCATIChildService checkExactMatchForUtterances:]"
- "-[CDMRegexSpanMatcher matchSpansForTokenChain:asrHypothesis:]"
- "-[CDMSiriVocabularyProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:]"
- "-[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:]"
- "-[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:]_block_invoke"
```
