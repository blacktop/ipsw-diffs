## CDMFoundation

> `/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation`

```diff

-3600.31.14.0.0
-  __TEXT.__text: 0x25ccc0
-  __TEXT.__objc_methlist: 0x8684
-  __TEXT.__const: 0xd370
+3605.16.1.0.0
+  __TEXT.__text: 0x272d8c
+  __TEXT.__objc_methlist: 0x8cd8
+  __TEXT.__const: 0xd388
   __TEXT.__swift5_typeref: 0x423c
   __TEXT.__swift5_fieldmd: 0x3d80
   __TEXT.__constg_swiftt: 0x55d4
   __TEXT.__swift5_protos: 0x98
-  __TEXT.__cstring: 0x1ba53
+  __TEXT.__cstring: 0x1c783
   __TEXT.__swift5_types: 0x574
   __TEXT.__swift5_proto: 0x9ac
   __TEXT.__swift5_reflstr: 0x306a
-  __TEXT.__oslogstring: 0x1dd75
+  __TEXT.__oslogstring: 0x1f260
   __TEXT.__swift5_assocty: 0x438
   __TEXT.__swift5_capture: 0x196c
   __TEXT.__swift5_builtin: 0xf0

   __TEXT.__swift_as_entry: 0x23c
   __TEXT.__swift_as_ret: 0x270
   __TEXT.__swift_as_cont: 0x42c
-  __TEXT.__gcc_except_tab: 0xb52c
+  __TEXT.__gcc_except_tab: 0xc560
   __TEXT.__ustring: 0x17c
-  __TEXT.__unwind_info: 0x96f8
+  __TEXT.__unwind_info: 0x99d8
   __TEXT.__eh_frame: 0x7a20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e80
-  __DATA_CONST.__objc_classlist: 0x8d0
+  __DATA_CONST.__const: 0x1f08
+  __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5400
+  __DATA_CONST.__objc_selrefs: 0x5500
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x408
-  __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0x26c8
-  __AUTH_CONST.__const: 0xc880
-  __AUTH_CONST.__cfstring: 0x81a0
-  __AUTH_CONST.__objc_const: 0x128c8
+  __DATA_CONST.__objc_superrefs: 0x438
+  __DATA_CONST.__objc_arraydata: 0x260
+  __DATA_CONST.__got: 0x26f8
+  __AUTH_CONST.__const: 0xc8c0
+  __AUTH_CONST.__cfstring: 0x8660
+  __AUTH_CONST.__objc_const: 0x132b0
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__objc_intobj: 0x678
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x4e58
-  __AUTH.__objc_data: 0x1168
+  __AUTH_CONST.__auth_got: 0x4e60
+  __AUTH.__objc_data: 0x1438
   __AUTH.__data: 0x1090
-  __DATA.__objc_ivar: 0x7ac
+  __DATA.__objc_ivar: 0x7f0
   __DATA.__data: 0x1c68
   __DATA.__common: 0x378
   __DATA_DIRTY.__objc_data: 0x4a00

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12861
-  Symbols:   11211
-  CStrings:  4592
+  Functions: 13047
+  Symbols:   11491
+  CStrings:  4742
 
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
+ GCC_except_table1012
+ GCC_except_table1017
+ GCC_except_table1020
+ GCC_except_table1021
+ GCC_except_table1022
+ GCC_except_table1023
+ GCC_except_table1024
+ GCC_except_table1025
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1029
+ GCC_except_table1030
+ GCC_except_table1031
+ GCC_except_table1032
+ GCC_except_table1063
+ GCC_except_table1073
+ GCC_except_table1074
+ GCC_except_table1075
+ GCC_except_table1076
+ GCC_except_table1077
+ GCC_except_table1078
+ GCC_except_table1080
+ GCC_except_table1081
+ GCC_except_table1082
+ GCC_except_table1085
+ GCC_except_table1086
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table1130
+ GCC_except_table1131
+ GCC_except_table1133
+ GCC_except_table1134
+ GCC_except_table1135
+ GCC_except_table1136
+ GCC_except_table1137
+ GCC_except_table1138
+ GCC_except_table1139
+ GCC_except_table114
+ GCC_except_table1140
+ GCC_except_table1141
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table1210
+ GCC_except_table1213
+ GCC_except_table1214
+ GCC_except_table1215
+ GCC_except_table1216
+ GCC_except_table1219
+ GCC_except_table1220
+ GCC_except_table1223
+ GCC_except_table1242
+ GCC_except_table1243
+ GCC_except_table1256
+ GCC_except_table1261
+ GCC_except_table1272
+ GCC_except_table1279
+ GCC_except_table128
+ GCC_except_table1283
+ GCC_except_table1286
+ GCC_except_table1310
+ GCC_except_table1337
+ GCC_except_table1338
+ GCC_except_table1339
+ GCC_except_table1340
+ GCC_except_table1341
+ GCC_except_table1342
+ GCC_except_table1343
+ GCC_except_table1345
+ GCC_except_table1346
+ GCC_except_table1347
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table1363
+ GCC_except_table1364
+ GCC_except_table140
+ GCC_except_table1415
+ GCC_except_table1416
+ GCC_except_table1417
+ GCC_except_table145
+ GCC_except_table1453
+ GCC_except_table1454
+ GCC_except_table1455
+ GCC_except_table1456
+ GCC_except_table1457
+ GCC_except_table1458
+ GCC_except_table1459
+ GCC_except_table146
+ GCC_except_table1460
+ GCC_except_table1461
+ GCC_except_table1462
+ GCC_except_table1463
+ GCC_except_table1464
+ GCC_except_table1465
+ GCC_except_table1466
+ GCC_except_table1467
+ GCC_except_table1468
+ GCC_except_table1469
+ GCC_except_table1470
+ GCC_except_table1471
+ GCC_except_table1475
+ GCC_except_table1476
+ GCC_except_table1477
+ GCC_except_table1478
+ GCC_except_table1479
+ GCC_except_table1480
+ GCC_except_table1481
+ GCC_except_table1482
+ GCC_except_table1483
+ GCC_except_table1484
+ GCC_except_table1485
+ GCC_except_table1486
+ GCC_except_table1487
+ GCC_except_table1488
+ GCC_except_table1489
+ GCC_except_table1490
+ GCC_except_table150
+ GCC_except_table1508
+ GCC_except_table151
+ GCC_except_table1512
+ GCC_except_table1513
+ GCC_except_table1514
+ GCC_except_table1515
+ GCC_except_table1516
+ GCC_except_table1517
+ GCC_except_table1518
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table1558
+ GCC_except_table156
+ GCC_except_table1564
+ GCC_except_table1565
+ GCC_except_table1566
+ GCC_except_table1567
+ GCC_except_table157
+ GCC_except_table1588
+ GCC_except_table1604
+ GCC_except_table1605
+ GCC_except_table1606
+ GCC_except_table1607
+ GCC_except_table1608
+ GCC_except_table1609
+ GCC_except_table1610
+ GCC_except_table1611
+ GCC_except_table1612
+ GCC_except_table1613
+ GCC_except_table1615
+ GCC_except_table1616
+ GCC_except_table1820
+ GCC_except_table1848
+ GCC_except_table1852
+ GCC_except_table1868
+ GCC_except_table1870
+ GCC_except_table1897
+ GCC_except_table1898
+ GCC_except_table1899
+ GCC_except_table1900
+ GCC_except_table1901
+ GCC_except_table1903
+ GCC_except_table1904
+ GCC_except_table1905
+ GCC_except_table1906
+ GCC_except_table1907
+ GCC_except_table1908
+ GCC_except_table1909
+ GCC_except_table1910
+ GCC_except_table1911
+ GCC_except_table1912
+ GCC_except_table1913
+ GCC_except_table1914
+ GCC_except_table1915
+ GCC_except_table1916
+ GCC_except_table1917
+ GCC_except_table1918
+ GCC_except_table1919
+ GCC_except_table1920
+ GCC_except_table1921
+ GCC_except_table1922
+ GCC_except_table1923
+ GCC_except_table1924
+ GCC_except_table1928
+ GCC_except_table1929
+ GCC_except_table1945
+ GCC_except_table1950
+ GCC_except_table1956
+ GCC_except_table1970
+ GCC_except_table1971
+ GCC_except_table1972
+ GCC_except_table1973
+ GCC_except_table1974
+ GCC_except_table1975
+ GCC_except_table1977
+ GCC_except_table1978
+ GCC_except_table1979
+ GCC_except_table198
+ GCC_except_table1980
+ GCC_except_table1981
+ GCC_except_table1991
+ GCC_except_table1995
+ GCC_except_table2004
+ GCC_except_table203
+ GCC_except_table2044
+ GCC_except_table205
+ GCC_except_table2050
+ GCC_except_table207
+ GCC_except_table2071
+ GCC_except_table209
+ GCC_except_table210
+ GCC_except_table211
+ GCC_except_table2115
+ GCC_except_table2116
+ GCC_except_table212
+ GCC_except_table2120
+ GCC_except_table2121
+ GCC_except_table2122
+ GCC_except_table2123
+ GCC_except_table2127
+ GCC_except_table2134
+ GCC_except_table2135
+ GCC_except_table2136
+ GCC_except_table2138
+ GCC_except_table2139
+ GCC_except_table2140
+ GCC_except_table2141
+ GCC_except_table2142
+ GCC_except_table2143
+ GCC_except_table2144
+ GCC_except_table2145
+ GCC_except_table2163
+ GCC_except_table2165
+ GCC_except_table2166
+ GCC_except_table2167
+ GCC_except_table2187
+ GCC_except_table2188
+ GCC_except_table2189
+ GCC_except_table2210
+ GCC_except_table2218
+ GCC_except_table2229
+ GCC_except_table2330
+ GCC_except_table2331
+ GCC_except_table2333
+ GCC_except_table2338
+ GCC_except_table2359
+ GCC_except_table2360
+ GCC_except_table2361
+ GCC_except_table2362
+ GCC_except_table2363
+ GCC_except_table2365
+ GCC_except_table2366
+ GCC_except_table2367
+ GCC_except_table2370
+ GCC_except_table2374
+ GCC_except_table2376
+ GCC_except_table2387
+ GCC_except_table2388
+ GCC_except_table2389
+ GCC_except_table2390
+ GCC_except_table2391
+ GCC_except_table2392
+ GCC_except_table2395
+ GCC_except_table2397
+ GCC_except_table2398
+ GCC_except_table2470
+ GCC_except_table2471
+ GCC_except_table2472
+ GCC_except_table2473
+ GCC_except_table2474
+ GCC_except_table2475
+ GCC_except_table2476
+ GCC_except_table2477
+ GCC_except_table2478
+ GCC_except_table2479
+ GCC_except_table2480
+ GCC_except_table2481
+ GCC_except_table2516
+ GCC_except_table2518
+ GCC_except_table2519
+ GCC_except_table2520
+ GCC_except_table2521
+ GCC_except_table2523
+ GCC_except_table2524
+ GCC_except_table2525
+ GCC_except_table2526
+ GCC_except_table2527
+ GCC_except_table2528
+ GCC_except_table2529
+ GCC_except_table2530
+ GCC_except_table2531
+ GCC_except_table2532
+ GCC_except_table2533
+ GCC_except_table2534
+ GCC_except_table2536
+ GCC_except_table2538
+ GCC_except_table2539
+ GCC_except_table2541
+ GCC_except_table2617
+ GCC_except_table2618
+ GCC_except_table2619
+ GCC_except_table2620
+ GCC_except_table2621
+ GCC_except_table2622
+ GCC_except_table2623
+ GCC_except_table2624
+ GCC_except_table2625
+ GCC_except_table2626
+ GCC_except_table2627
+ GCC_except_table2628
+ GCC_except_table2629
+ GCC_except_table2630
+ GCC_except_table2631
+ GCC_except_table2632
+ GCC_except_table2634
+ GCC_except_table2654
+ GCC_except_table2677
+ GCC_except_table2678
+ GCC_except_table2679
+ GCC_except_table2685
+ GCC_except_table2686
+ GCC_except_table2687
+ GCC_except_table2688
+ GCC_except_table2689
+ GCC_except_table2690
+ GCC_except_table2691
+ GCC_except_table2721
+ GCC_except_table2723
+ GCC_except_table2726
+ GCC_except_table2753
+ GCC_except_table2754
+ GCC_except_table2781
+ GCC_except_table317
+ GCC_except_table321
+ GCC_except_table329
+ GCC_except_table334
+ GCC_except_table336
+ GCC_except_table338
+ GCC_except_table340
+ GCC_except_table343
+ GCC_except_table345
+ GCC_except_table348
+ GCC_except_table351
+ GCC_except_table353
+ GCC_except_table363
+ GCC_except_table376
+ GCC_except_table378
+ GCC_except_table398
+ GCC_except_table410
+ GCC_except_table420
+ GCC_except_table434
+ GCC_except_table435
+ GCC_except_table447
+ GCC_except_table459
+ GCC_except_table465
+ GCC_except_table471
+ GCC_except_table472
+ GCC_except_table473
+ GCC_except_table474
+ GCC_except_table476
+ GCC_except_table480
+ GCC_except_table486
+ GCC_except_table526
+ GCC_except_table531
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table537
+ GCC_except_table567
+ GCC_except_table570
+ GCC_except_table571
+ GCC_except_table585
+ GCC_except_table755
+ GCC_except_table756
+ GCC_except_table759
+ GCC_except_table760
+ GCC_except_table761
+ GCC_except_table762
+ GCC_except_table815
+ GCC_except_table818
+ GCC_except_table819
+ GCC_except_table820
+ GCC_except_table821
+ GCC_except_table822
+ GCC_except_table823
+ GCC_except_table838
+ GCC_except_table840
+ GCC_except_table841
+ GCC_except_table844
+ GCC_except_table845
+ GCC_except_table846
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table849
+ GCC_except_table851
+ GCC_except_table852
+ GCC_except_table853
+ GCC_except_table854
+ GCC_except_table855
+ GCC_except_table856
+ GCC_except_table861
+ GCC_except_table864
+ GCC_except_table865
+ GCC_except_table88
+ GCC_except_table881
+ GCC_except_table89
+ GCC_except_table917
+ GCC_except_table918
+ GCC_except_table99
+ _AFDeviceSupportsSAEByDeviceCapabilityAndFeatureFlags
+ _CDMConnectionIdRequiresUtteranceRedaction
+ _CDMRedactedUtteranceRequesters.onceToken
+ _CDMRedactedUtteranceRequesters.requesters
+ _OBJC_CLASS_$_CDMContactNLURequestCommand
+ _OBJC_CLASS_$_CDMContactNLUResponseCommand
+ _OBJC_CLASS_$_CDMContactNLUServiceGraph
+ _OBJC_CLASS_$_CDMMagicComposeRequestCommand
+ _OBJC_CLASS_$_CDMMagicComposeResponseCommand
+ _OBJC_CLASS_$_CDMMagicComposeServiceGraph
+ _OBJC_CLASS_$_CDMTrustedAgentRequestCommand
+ _OBJC_CLASS_$_CDMTrustedAgentResponseCommand
+ _OBJC_CLASS_$_CDMTrustedAgentServiceGraph
+ _OBJC_IVAR_$_CDMCATIProtoRequestCommand._connectionId
+ _OBJC_IVAR_$_CDMContactNLURequestCommand._clientId
+ _OBJC_IVAR_$_CDMContactNLURequestCommand._selfMetadata
+ _OBJC_IVAR_$_CDMContactNLURequestCommand._siriNLUTypeObj
+ _OBJC_IVAR_$_CDMContactNLUResponseCommand._requestId
+ _OBJC_IVAR_$_CDMContactNLUResponseCommand._siriNLUTypeObj
+ _OBJC_IVAR_$_CDMMagicComposeRequestCommand._clientId
+ _OBJC_IVAR_$_CDMMagicComposeRequestCommand._selfMetadata
+ _OBJC_IVAR_$_CDMMagicComposeRequestCommand._siriNLUTypeObj
+ _OBJC_IVAR_$_CDMMagicComposeResponseCommand._requestId
+ _OBJC_IVAR_$_CDMMagicComposeResponseCommand._siriNLUTypeObj
+ _OBJC_IVAR_$_CDMSpanMatcherRequestCommand._connectionId
+ _OBJC_IVAR_$_CDMTrustedAgentRequestCommand._clientId
+ _OBJC_IVAR_$_CDMTrustedAgentRequestCommand._selfMetadata
+ _OBJC_IVAR_$_CDMTrustedAgentRequestCommand._siriNLUTypeObj
+ _OBJC_IVAR_$_CDMTrustedAgentResponseCommand._requestId
+ _OBJC_IVAR_$_CDMTrustedAgentResponseCommand._siriNLUTypeObj
+ _OBJC_METACLASS_$_CDMContactNLURequestCommand
+ _OBJC_METACLASS_$_CDMContactNLUResponseCommand
+ _OBJC_METACLASS_$_CDMContactNLUServiceGraph
+ _OBJC_METACLASS_$_CDMMagicComposeRequestCommand
+ _OBJC_METACLASS_$_CDMMagicComposeResponseCommand
+ _OBJC_METACLASS_$_CDMMagicComposeServiceGraph
+ _OBJC_METACLASS_$_CDMTrustedAgentRequestCommand
+ _OBJC_METACLASS_$_CDMTrustedAgentResponseCommand
+ _OBJC_METACLASS_$_CDMTrustedAgentServiceGraph
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
+ ___39-[CDMContactNLUServiceGraph buildGraph]_block_invoke
+ ___39-[CDMContactNLUServiceGraph buildGraph]_block_invoke_2
+ ___41-[CDMMagicComposeServiceGraph buildGraph]_block_invoke
+ ___41-[CDMMagicComposeServiceGraph buildGraph]_block_invoke_2
+ ___41-[CDMMagicComposeServiceGraph buildGraph]_block_invoke_3
+ ___41-[CDMTrustedAgentServiceGraph buildGraph]_block_invoke
+ ___41-[CDMTrustedAgentServiceGraph buildGraph]_block_invoke_2
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
+ ___block_descriptor_104_e8_32s40s48s56r64r72r80r88r96r_e29_v16?0"CDMServiceGraphNode"8lr56l8s32l8r64l8r72l8s40l8r80l8s48l8r88l8r96l8
+ ___block_descriptor_216_e8_32s40s48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208w_e29_v16?0"CDMServiceGraphNode"8lr48l8s32l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8s40l8w208l8
+ ___block_descriptor_40_e8_32bs_e51_v24?0"SIRINLUEXTERNALCDMNluResponse"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_49_e8_B16?08l
+ ___block_descriptor_64_ea8_32s40bs48w_e34_v24?0"<CDMCommand>"8"NSError"16lw48l8s40l8s32l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8s40l8s48l8r64l8r72l8s56l8
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
+ _reminderName.onceToken
+ _reminderName.value
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
- GCC_except_table100
- GCC_except_table102
- GCC_except_table1056
- GCC_except_table1059
- GCC_except_table106
- GCC_except_table1060
- GCC_except_table1061
- GCC_except_table1062
- GCC_except_table1065
- GCC_except_table1066
- GCC_except_table1069
- GCC_except_table107
- GCC_except_table1088
- GCC_except_table1089
- GCC_except_table1102
- GCC_except_table1107
- GCC_except_table1118
- GCC_except_table1125
- GCC_except_table1129
- GCC_except_table1148
- GCC_except_table1149
- GCC_except_table1150
- GCC_except_table1151
- GCC_except_table1152
- GCC_except_table1156
- GCC_except_table1157
- GCC_except_table1161
- GCC_except_table1162
- GCC_except_table1165
- GCC_except_table1183
- GCC_except_table1184
- GCC_except_table1185
- GCC_except_table1186
- GCC_except_table1187
- GCC_except_table1188
- GCC_except_table1189
- GCC_except_table119
- GCC_except_table1190
- GCC_except_table1191
- GCC_except_table1192
- GCC_except_table1193
- GCC_except_table121
- GCC_except_table1251
- GCC_except_table1252
- GCC_except_table1253
- GCC_except_table126
- GCC_except_table127
- GCC_except_table1281
- GCC_except_table1289
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
- GCC_except_table1300
- GCC_except_table1301
- GCC_except_table1307
- GCC_except_table131
- GCC_except_table1312
- GCC_except_table1313
- GCC_except_table1314
- GCC_except_table1317
- GCC_except_table1318
- GCC_except_table132
- GCC_except_table1320
- GCC_except_table1321
- GCC_except_table1322
- GCC_except_table1323
- GCC_except_table1324
- GCC_except_table1325
- GCC_except_table1326
- GCC_except_table133
- GCC_except_table1348
- GCC_except_table1349
- GCC_except_table1350
- GCC_except_table1351
- GCC_except_table1352
- GCC_except_table1353
- GCC_except_table1354
- GCC_except_table1394
- GCC_except_table1400
- GCC_except_table1401
- GCC_except_table1402
- GCC_except_table1403
- GCC_except_table141
- GCC_except_table142
- GCC_except_table1424
- GCC_except_table1440
- GCC_except_table1441
- GCC_except_table1442
- GCC_except_table1443
- GCC_except_table1444
- GCC_except_table1446
- GCC_except_table1447
- GCC_except_table1448
- GCC_except_table1449
- GCC_except_table1451
- GCC_except_table1452
- GCC_except_table1646
- GCC_except_table1674
- GCC_except_table1678
- GCC_except_table1694
- GCC_except_table1696
- GCC_except_table1723
- GCC_except_table1724
- GCC_except_table1725
- GCC_except_table1726
- GCC_except_table1727
- GCC_except_table1729
- GCC_except_table1730
- GCC_except_table1731
- GCC_except_table1732
- GCC_except_table1733
- GCC_except_table1734
- GCC_except_table1735
- GCC_except_table1736
- GCC_except_table1737
- GCC_except_table1738
- GCC_except_table1739
- GCC_except_table1740
- GCC_except_table1741
- GCC_except_table1742
- GCC_except_table1743
- GCC_except_table1744
- GCC_except_table1748
- GCC_except_table1749
- GCC_except_table1765
- GCC_except_table1770
- GCC_except_table1773
- GCC_except_table1776
- GCC_except_table1777
- GCC_except_table1778
- GCC_except_table1779
- GCC_except_table1780
- GCC_except_table1781
- GCC_except_table1782
- GCC_except_table1783
- GCC_except_table1784
- GCC_except_table1785
- GCC_except_table1786
- GCC_except_table1787
- GCC_except_table1788
- GCC_except_table1789
- GCC_except_table1790
- GCC_except_table1791
- GCC_except_table1792
- GCC_except_table1793
- GCC_except_table1794
- GCC_except_table1795
- GCC_except_table1797
- GCC_except_table1798
- GCC_except_table1799
- GCC_except_table180
- GCC_except_table1800
- GCC_except_table1801
- GCC_except_table1802
- GCC_except_table1803
- GCC_except_table1804
- GCC_except_table1805
- GCC_except_table1806
- GCC_except_table1811
- GCC_except_table1815
- GCC_except_table1824
- GCC_except_table1825
- GCC_except_table1826
- GCC_except_table185
- GCC_except_table1863
- GCC_except_table1867
- GCC_except_table1869
- GCC_except_table187
- GCC_except_table189
- GCC_except_table1890
- GCC_except_table191
- GCC_except_table192
- GCC_except_table193
- GCC_except_table1934
- GCC_except_table1935
- GCC_except_table1939
- GCC_except_table194
- GCC_except_table1940
- GCC_except_table1941
- GCC_except_table1942
- GCC_except_table1946
- GCC_except_table1954
- GCC_except_table1955
- GCC_except_table1976
- GCC_except_table2000
- GCC_except_table2007
- GCC_except_table2008
- GCC_except_table2026
- GCC_except_table2029
- GCC_except_table2030
- GCC_except_table2037
- GCC_except_table2154
- GCC_except_table2156
- GCC_except_table2172
- GCC_except_table2173
- GCC_except_table2175
- GCC_except_table2176
- GCC_except_table2177
- GCC_except_table2178
- GCC_except_table2179
- GCC_except_table2182
- GCC_except_table2183
- GCC_except_table2190
- GCC_except_table2192
- GCC_except_table2203
- GCC_except_table2204
- GCC_except_table2205
- GCC_except_table2206
- GCC_except_table2208
- GCC_except_table2213
- GCC_except_table2214
- GCC_except_table2286
- GCC_except_table2287
- GCC_except_table2288
- GCC_except_table2289
- GCC_except_table2290
- GCC_except_table2291
- GCC_except_table2292
- GCC_except_table2293
- GCC_except_table2294
- GCC_except_table2295
- GCC_except_table2296
- GCC_except_table2297
- GCC_except_table2335
- GCC_except_table2336
- GCC_except_table2337
- GCC_except_table2339
- GCC_except_table2342
- GCC_except_table2343
- GCC_except_table2344
- GCC_except_table2345
- GCC_except_table2346
- GCC_except_table2347
- GCC_except_table2349
- GCC_except_table2350
- GCC_except_table2351
- GCC_except_table2352
- GCC_except_table2353
- GCC_except_table2354
- GCC_except_table2355
- GCC_except_table239
- GCC_except_table243
- GCC_except_table2431
- GCC_except_table2432
- GCC_except_table2433
- GCC_except_table2434
- GCC_except_table2435
- GCC_except_table2436
- GCC_except_table2437
- GCC_except_table2438
- GCC_except_table2439
- GCC_except_table2440
- GCC_except_table2441
- GCC_except_table2442
- GCC_except_table2443
- GCC_except_table2444
- GCC_except_table2445
- GCC_except_table2446
- GCC_except_table2448
- GCC_except_table245
- GCC_except_table2468
- GCC_except_table247
- GCC_except_table249
- GCC_except_table2491
- GCC_except_table2492
- GCC_except_table2493
- GCC_except_table2499
- GCC_except_table2500
- GCC_except_table2501
- GCC_except_table2502
- GCC_except_table2503
- GCC_except_table2504
- GCC_except_table2505
- GCC_except_table251
- GCC_except_table253
- GCC_except_table256
- GCC_except_table2567
- GCC_except_table2568
- GCC_except_table258
- GCC_except_table2595
- GCC_except_table260
- GCC_except_table262
- GCC_except_table265
- GCC_except_table267
- GCC_except_table270
- GCC_except_table273
- GCC_except_table275
- GCC_except_table285
- GCC_except_table298
- GCC_except_table300
- GCC_except_table303
- GCC_except_table304
- GCC_except_table316
- GCC_except_table322
- GCC_except_table324
- GCC_except_table337
- GCC_except_table372
- GCC_except_table377
- GCC_except_table383
- GCC_except_table413
- GCC_except_table416
- GCC_except_table417
- GCC_except_table431
- GCC_except_table558
- GCC_except_table601
- GCC_except_table602
- GCC_except_table605
- GCC_except_table606
- GCC_except_table607
- GCC_except_table608
- GCC_except_table661
- GCC_except_table664
- GCC_except_table665
- GCC_except_table666
- GCC_except_table667
- GCC_except_table668
- GCC_except_table669
- GCC_except_table684
- GCC_except_table686
- GCC_except_table687
- GCC_except_table690
- GCC_except_table691
- GCC_except_table692
- GCC_except_table693
- GCC_except_table694
- GCC_except_table695
- GCC_except_table697
- GCC_except_table698
- GCC_except_table699
- GCC_except_table700
- GCC_except_table701
- GCC_except_table702
- GCC_except_table704
- GCC_except_table707
- GCC_except_table709
- GCC_except_table710
- GCC_except_table711
- GCC_except_table714
- GCC_except_table715
- GCC_except_table719
- GCC_except_table727
- GCC_except_table763
- GCC_except_table764
- GCC_except_table765
- GCC_except_table79
- GCC_except_table80
- GCC_except_table81
- GCC_except_table867
- GCC_except_table870
- GCC_except_table871
- GCC_except_table874
- GCC_except_table875
- GCC_except_table876
- GCC_except_table877
- GCC_except_table878
- GCC_except_table909
- GCC_except_table920
- GCC_except_table921
- GCC_except_table922
- GCC_except_table923
- GCC_except_table924
- GCC_except_table926
- GCC_except_table927
- GCC_except_table928
- GCC_except_table931
- GCC_except_table932
- GCC_except_table96
- GCC_except_table976
- GCC_except_table977
- GCC_except_table978
- GCC_except_table979
- GCC_except_table980
- GCC_except_table981
- GCC_except_table982
- GCC_except_table983
- GCC_except_table984
- GCC_except_table985
- GCC_except_table986
- GCC_except_table987
- __OBJC_$_CLASS_METHODS_CDMClient(NLUPreprocess|ShortcutDetector|NLU|Embedding|SsuInference)
- __OBJC_$_INSTANCE_METHODS_CDMClient(NLUPreprocess|ShortcutDetector|NLU|Embedding|SsuInference)
- __OBJC_$_INSTANCE_METHODS_CDMFoundationClient(XPCEvent)
- __OBJC_CLASS_PROTOCOLS_$_CDMClient(NLUPreprocess|ShortcutDetector|NLU|Embedding|SsuInference)
- ___68-[CDMVocTrieProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56r64r72r80r88r96r_e29_v16?0"CDMServiceGraphNode"8lr56l8r64l8r72l8r80l8r88l8s32l8r96l8s40l8s48l8
- ___block_descriptor_40_e8_B16?08l
- ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32s40r48r_e29_v16?0"CDMServiceGraphNode"8lr40l8r48l8s32l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8s40l8r56l8r64l8s48l8
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
+ "-[CDMContactNLUServiceGraph buildGraph]_block_invoke_2"
+ "-[CDMFoundationClient processContactNluRequest:completionHandler:]"
+ "-[CDMFoundationClient processContactNluRequest:completionHandler:]_block_invoke"
+ "-[CDMFoundationClient processMagicComposeNluRequest:completionHandler:]"
+ "-[CDMFoundationClient processMagicComposeNluRequest:completionHandler:]_block_invoke"
+ "-[CDMFoundationClient(TrustedAgent) processTrustedAgentNluRequest:completionHandler:]"
+ "-[CDMFoundationClient(TrustedAgent) processTrustedAgentNluRequest:completionHandler:]_block_invoke"
+ "-[CDMMagicComposeServiceGraph buildGraph]_block_invoke"
+ "-[CDMMagicComposeServiceGraph buildGraph]_block_invoke_2"
+ "-[CDMMagicComposeServiceGraph buildGraph]_block_invoke_3"
+ "-[CDMRegexSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]"
+ "-[CDMSiriVocabularyProtoSpanMatcher matchSpansForTokenChain:asrHypothesis:connectionId:]"
+ "-[CDMTrustedAgentServiceGraph buildGraph]_block_invoke"
+ "-[CDMTrustedAgentServiceGraph buildGraph]_block_invoke_2"
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
