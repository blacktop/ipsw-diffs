## TSReading

> `/System/Library/PrivateFrameworks/TSReading.framework/TSReading`

```diff

 778.0.0.0.0
-  __TEXT.__text: 0x340a0c
+  __TEXT.__text: 0x340b48
   __TEXT.__objc_methlist: 0x34128
   __TEXT.__const: 0x4778
   __TEXT.__cstring: 0x48711
   __TEXT.__gcc_except_tab: 0xcb08
   __TEXT.__ustring: 0xf4
   __TEXT.__oslogstring: 0x120
-  __TEXT.__unwind_info: 0xf0e0
+  __TEXT.__unwind_info: 0xf0d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 20645
+  Functions: 20644
   Symbols:   41257
   CStrings:  7226
 
Functions:
~ __ZNSt3__16vectorIN9EQKitPath11PathElementENS_9allocatorIS2_EEE6insertENS_11__wrap_iterIPKS2_EERS7_ : 488 -> 484
~ __ZNSt3__114__split_bufferIN9EQKitPath11PathElementERNS_9allocatorIS2_EEE12emplace_backIJRKS2_EEEvDpOT_ : 264 -> 268
~ __ZNSt3__114__split_bufferIP28EQKitLayoutStretchedOperatorNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_ : 256 -> 260
~ __ZNSt3__114__split_bufferIP28EQKitLayoutStretchedOperatorRNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_ : 256 -> 260
~ __ZNSt3__114__split_bufferIPU13block_pointerFvPU26objcproto15EQKitLayoutNode11objc_objectRKN5EQKit6Layout8SchemataEENS_9allocatorISA_EEE12emplace_backIJSA_EEEvDpOT_ : 264 -> 268
~ __ZNSt3__114__split_bufferIPU13block_pointerFvPU26objcproto15EQKitLayoutNode11objc_objectRKN5EQKit6Layout8SchemataEERNS_9allocatorISA_EEE12emplace_backIJSA_EEEvDpOT_ : 264 -> 268
~ __ZNSt3__114__split_bufferIPmNS_9allocatorIS1_EEE12emplace_backIJS1_EEEvDpOT_ : 256 -> 260
~ __ZNSt3__114__split_bufferIPmRNS_9allocatorIS1_EEE12emplace_backIJS1_EEEvDpOT_ : 256 -> 260
~ __ZNSt3__114__split_bufferIP22EQKitMathMLParserStateNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_ : 264 -> 268
~ __ZNSt3__114__split_bufferIP22EQKitMathMLParserStateRNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_ : 264 -> 268
~ __ZNSt3__16vectorIN5EQKit11StemStretch12FeatureRange4SpanENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_ : 380 -> 376
~ __ZNSt3__16vectorIN5EQKit11StemStretch4StemENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 276 -> 272
~ ___46-[TSPCryptoReadChannel readWithQueue:handler:]_block_invoke_4 : 788 -> 792
~ -[TSKShuffleMapping remove:indicesAtIndex:] : 388 -> 392
~ _shrinkIntervalWithIntersectionsFromCurve : 196 -> 204
~ _GenerateBezier : 836 -> 844
~ -[TSDBezierPath flattenIntoPath:flatness:] : 228 -> 224
~ -[TSDBezierPath bezierPathByReversingPath] : 376 -> 380
~ -[TSDBezierPath elementAtIndex:associatedPoints:] : 220 -> 224
~ -[TSDBezierPath elementAtIndex:allPoints:] : 268 -> 272
~ -[TSDBezierPath setAssociatedPoints:atIndex:] : 236 -> 240
~ -[TSDBezierPath _appendToPath:] : 196 -> 192
~ __ZN10FloatLigne7BooleenEPS_S0_7bool_op : 1636 -> 1632
~ __ZN8IntLigne7BooleenEPS_S0_7bool_op : 1604 -> 1596
~ __ZN4Path4FillEP5Shapeibbb : 2484 -> 2492
~ __ZN4Path10DoSimplifyEf : 572 -> 592
~ __ZN4Path15AttemptSimplifyEfRNS_18path_descr_cubictoE : 2572 -> 2564
~ -[TSDMetalEdgeDistanceFieldMorphEffect p_actualPixelBoundsOfTexturedRectangle:] : 1536 -> 1552
~ -[TSDMetalEdgeDistanceFieldMorphEffect p_fillScanlineCenters:scanlineMinMaxZeroes:samples:fromTexture:textureSize:] : 1400 -> 1404
~ -[TSDMetalEdgeDistanceFieldTraceEffect p_generateTraceTextureInfoWithStrokeWidth:clockwise:context:randomGenerator:] : 3228 -> 3232
~ __ZN5Shape8SubPointEi : 220 -> 228
~ __ZN5Shape9SwapEdgesEii : 1528 -> 1560
~ __ZN5Shape9SortEdgesEv : 568 -> 592
~ __ZN5Shape14ConvertToFormeEP4Path : 1060 -> 1068
~ __ZN5Shape14ConvertToFormeEP4PathiPS1_ : 1160 -> 1164
~ __ZN5Shape10MakeOffsetEPS_f8join_typf : 1108 -> 1116
~ __ZN5Shape13ReFormeLineToEiiP4PathS1_ : 300 -> 304
~ __ZN5Shape12ReFormeArcToEiiP4PathS1_ : 604 -> 608
~ __ZN5Shape14ReFormeCubicToEiiP4PathS1_ : 516 -> 520
~ __ZN5Shape9ReorienteEPS_ : 1104 -> 1108
~ __ZN5Shape11GetWindingsEPS_S0_7bool_opb : 872 -> 884
~ __ZN5Shape14ConvertToShapeEPS_8fill_typb : 5048 -> 5068
~ __ZN5Shape14AssemblePointsEii : 464 -> 472
~ __ZN5Shape16CheckAdjacenciesEiiPS_i : 1740 -> 1744
~ __ZN5Shape7AddChgtEiiRPS_RiiS0_iS0_i : 744 -> 748
~ __ZN5Shape14AssembleAretesEv : 1060 -> 1064
~ __ZN5Shape7BooleenEPS_S0_7bool_op : 5880 -> 5904
~ __ZN5Shape17TesteIntersectionEP9SweepTreeS1_RfS2_S2_S2_b : 1204 -> 1252
~ __ZN5Shape15CreateIncidenceEPS_ii : 112 -> 116
~ __ZN5Shape7WindingEi : 76 -> 80
~ __ZN5Shape7WindingEff : 356 -> 352
~ __ZN5Shape14AssemblePointsEPS_ : 208 -> 216
~ __ZN5Shape17TesteIntersectionEPS_S0_iiRfS1_S1_S1_b : 592 -> 608
~ __ZN5Shape8DoEdgeToEPS_iibb : 460 -> 468
~ __ZN10SweepEvent14SupprFromQueueER15SweepEventQueue : 580 -> 588
~ __ZNSt3__16vectorIN5boost7polygon10point_dataIdEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_ : 288 -> 284
~ __ZNSt3__114__split_bufferIN5boost7polygon12segment_dataIdEERNS_9allocatorIS4_EEE12emplace_backIJRKS4_EEEvDpOT_ : 368 -> 372
~ ___64-[TSDGPUParticleSystem(Private) p_setupParticleDataWithTexture:]_block_invoke : 4420 -> 4424
~ __ZNSt3__16vectorIP18TSDOrthoGraphPointNS_9allocatorIS2_EEE6resizeEm : 284 -> 288
~ -[TSWPRubyTextSource initWithSource:subRange:] : 1116 -> 1112
~ -[TSWPRubyTextSource getCharacters:range:] : 308 -> 316
~ __ZNSt3__16vectorI20TSWPTopicNumberEntryNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 264 -> 260
~ -[TSWPLayoutManager inflateTarget:fromHints:childHint:anchoredAttachmentPositions:topicNumbers:] : 2536 -> 2532
~ __ZNK16TSWPLineFragment17rectsForLineRangeE8_NSRangebbbPP7NSArray : 2180 -> 2184
~ __ZNK16TSWPLineFragment19rectsForVisualRangeE8_NSRangemmbbbPP7NSArray : 1228 -> 1260
~ __ZNSt3__16vectorI19TSWPLFCharIndexDataNS_9allocatorIS1_EEE6insertENS_11__wrap_iterIPKS1_EERS6_ : 516 -> 512
~ __ZNSt3__114__split_bufferI19TSWPLFCharIndexDataRNS_9allocatorIS1_EEE12emplace_backIJRKS1_EEEvDpOT_ : 284 -> 288
~ +[TSWPTextWrapper p_wrappedSubrectsForRectOptimized:lineSegmentRects:polygon:type:skipHint:] : 2180 -> 2188
~ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE18__insert_with_sizeB9fqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS1_EES9_EES9_NS7_IPKS1_EET0_T1_l : 492 -> 508
~ -[TSWPRepTileGeometry tileGeometryRectWithLayer:atIndex:mask:] : 420 -> 424
~ __ZN15TSWPLayoutChore25pLayoutColumnWithOldLinesE15TSWPLayoutFlagsd6CGSizeS1_P14NSMutableArrayPtPbP21TSWPLineFragmentArray : 14804 -> 14808
~ -[TSWPStorage(TSWPStorage_private) p_fillMarkers:string:length:hasAttachments:hasFootnotes:hasBreaks:] : 740 -> 744
~ __ZN12_GLOBAL__N_131TSWPArabianAbjadLabelFromNumberEj : 476 -> 480
~ __ZN12_GLOBAL__N_133TSWPHebrewBiblicalLabelFromNumberEj : 476 -> 480
~ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE6insertENS_11__wrap_iterIPKS1_EERS6_ : 488 -> 484
~ __ZN15TSWPRangeVector22removeCharacterAtIndexEm : 276 -> 280
~ __ZN15TSWPRangeVector18deletedTextAtRangeERK8_NSRange : 304 -> 308
~ __ZN15TSWPRangeVector19replacedTextAtRangeERK8_NSRangem : 288 -> 292
~ __ZN15TSWPRangeVector12changedRangeE8_NSRangel : 312 -> 316
~ __ZNSt3__114__split_bufferI8_NSRangeRNS_9allocatorIS1_EEE12emplace_backIJRKS1_EEEvDpOT_ : 264 -> 268
~ __ZL26TSTTableRepDrawCellContentP11TSTTableRepP14TSTLayoutSpace12TSTGridRangeP14NSMutableArrayP9CGContext : 7708 -> 7692
- __ZNSt3__16vectorI16TSUColumnRowRectNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
~ __ZNSt3__16vectorIN27TSTWidthHeightCache_Private14WHCWidthBucketENS_9allocatorIS2_EEE6insertENS_11__wrap_iterIPKS2_EERS7_ : 512 -> 508
~ __ZNSt3__16vectorIN27TSTWidthHeightCache_Private15WHCHeightBucketENS_9allocatorIS2_EEE6insertENS_11__wrap_iterIPKS2_EEOS2_ : 476 -> 472
~ __ZNSt3__114__split_bufferIN27TSTWidthHeightCache_Private14WHCWidthBucketERNS_9allocatorIS2_EEE12emplace_backIJRKS2_EEEvDpOT_ : 268 -> 272
~ __ZNSt3__114__split_bufferIN27TSTWidthHeightCache_Private15WHCHeightBucketERNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_ : 268 -> 272
~ __ZL31p_TSTStrokeRunArrayInsertStrokeP17TSTStrokeRunArrayjjP9TSDStrokebb : 2096 -> 2152
~ -[TSTTablePartitioner measureCellRangeForNextPartitionOfSize:previousHint:horizontally:] : 1412 -> 1428
```
