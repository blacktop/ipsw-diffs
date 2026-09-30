## CoreText

> `/System/Library/Frameworks/CoreText.framework/CoreText`

```diff

 904.0.0.0.0
-  __TEXT.__text: 0x15ed2c
+  __TEXT.__text: 0x15f0fc
   __TEXT.__delay_helper: 0x264
   __TEXT.__objc_methlist: 0xdd4
   __TEXT.__const: 0x51f94

   __TEXT.__ustring: 0x1954
   __TEXT.__gcc_except_tab: 0x248
   __TEXT.__dof_CoreText: 0x1629
-  __TEXT.__unwind_info: 0x54f8
+  __TEXT.__unwind_info: 0x54f0
   __TEXT.__eh_frame: 0x2b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 5463
+  Functions: 5462
   Symbols:   8025
   CStrings:  3347
 
Functions:
~ __ZN7TCFBaseI5TFontE9ClassHashEPKv : 76 -> 80
~ __ZNK8TRunGlue17DetermineCoverageEPh : 404 -> 400
~ __ZNK3OTL4GSUB23ApplySubstLookupRecordsEPKNS_14LookupSubtableEPKNS_17SubstLookupRecordEjR14TGlyphIteratorlPlmPtPNS_17SubstitutionStateEm : 968 -> 972
~ __ZNK3OTL4GSUB12ApplyLookupsER8TRunGlueiRNS_12GlyphLookupsER9SyncStatePFvPv7CFRangelES7_ : 1312 -> 1316
~ __ZNK5TFont28GetUnsummedAdvancesForGlyphsEPKtPd13AdvanceStridel17CTFontOrientationNSt3__18optionalIjEE : 680 -> 688
~ __ZNK8TRunGlue10GetAdvanceEl : 140 -> 144
~ __ZNK5TFont35GetAdvancesForGlyphsWithStyleFromCGEjPKtPd13AdvanceStridelRK17CGAffineTransformbdb : 720 -> 724
~ __ZN26TOpenTypePositioningEngine12PositionRunsER9SyncStateR13KerningStatus : 3996 -> 4000
~ __ZNK3OTL4GPOS23ApplyPairPosAcceleratedERKNS_6LookupEjR14TGlyphIterator : 3344 -> 3352
~ __ZNK3OTL8Coverage16SearchFmt1BinaryEt : 232 -> 236
~ __ZNK3OTL8Coverage16SearchFmt2BinaryEt : 280 -> 284
~ __ZNK3OTL4GPOS13ApplyLookupAtERKNS_6LookupEjR14TGlyphIteratorm : 344 -> 348
~ __ZNK3OTL4GSUB18ApplyLigatureSubstEPKNS_14LookupSubtableER14TGlyphIteratorjPtPNS_17SubstitutionStateE : 824 -> 840
~ __ZN7TCFBaseI11TDescriptorE9ClassHashEPKv : 108 -> 112
~ __Z20MakeSpliceDescriptorPK10__CFStringmS1_S1_PK10__CFNumberS4_j23CTFontTextStylePlatformjS4_S4_22CTFontLegibilityWeightPK11__CFBooleanPKvS1_ : 12712 -> 12720
~ __ZN13TGlyphEncoder11EncodeCharsE7CFRangeRK11TAttributesNS_9FallbacksE : 3244 -> 3256
~ __ZN13TASCIIEncoder6EncodeEb : 524 -> 528
~ __ZN21TTypesetterAttrString10InitializeEPK20__CFAttributedStringb : 3180 -> 3228
~ __Z52CreateCharacterSetWithCompressedBitmapRepresentationPK8__CFData : 480 -> 488
~ __ZNK3OTL4GSUB29ApplyChainContextSubstFormat3EPKNS_14LookupSubtableER14TGlyphIteratorPtPNS_17SubstitutionStateEm : 720 -> 732
~ __ZNK18ItemVariationStore16ValueForDeltaSetEttNSt3__17variantIJNS0_4spanIKsLm18446744073709551615EEENS2_IKdLm18446744073709551615EEEEEE : 1024 -> 1032
~ __ZN14TGlyphIterator25MatchCoverSequenceContextIL14MatchDirection0EEEbljPKN3OTL8OffsetToINS2_8Coverage5TableE15BigEndianScalarItEEEPKvSC_Pl : 280 -> 284
~ __ZNK4TRun39GetLeftPartialHangingGlyphCountAndWidthElmRK11TCharStream : 372 -> 368
~ __ZN8TRunGlueC2ER5TLine : 456 -> 464
~ __ZN7TCFBaseI12TRunDelegateE9ClassHashEPKv : 76 -> 80
~ __ZNK4TRun10DrawGlyphsEP9CGContext7CFRange : 1008 -> 992
~ __ZN15TUnicodeEncoder6EncodeEPK8__CTFontPK10__CFStringR19TCharStreamIterator7CFRangePtPdPjSA_b : 1628 -> 1612
~ __ZNK13TStorageRange25GetNextUnmappedGlyphRangeEl : 172 -> 168
~ __ZNK4TRun9FindBreakEldRK11TCharStream22TabMeasurementBehavior : 1448 -> 1456
~ __ZN11TCharStream33GetRangeOfCharacterClusterAtIndexEPK10__CFStringl28CFStringCharacterClusterType : 816 -> 820
~ __ZN15TUnicodeEncoder13EncodePortionElPKtlRK9TBaseFontbPtPd13AdvanceStridePjS6_b : 1708 -> 1712
~ __ZNK9TBaseFont19GetUnscaledAdvancesEPKtPd13AdvanceStridel : 388 -> 392
~ __ZL24GetGlyphAdvancesForStyleP6CGFontPK17CGAffineTransformjPKtlPd13AdvanceStride : 316 -> 320
~ __ZNK4TRun19CacheGlyphPositionsERdS0_ : 944 -> 940
~ __ZNK5TFont20GetAdvancesForGlyphsEPKtPd13AdvanceStridel17CTFontOrientationNSt3__18optionalIjEEPK17CGAffineTransform : 924 -> 940
~ __Z20CreateOTFeatureTableRK9TBaseFont : 2608 -> 2612
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPjEEEEvT1_S8_S8_OT0_NS_15iterator_traitsIS8_E15difference_typeESD_PNSC_10value_typeEl : 1224 -> 1228
~ __ZN8TRunGlue23UpdateForCurrentRealRunEb : 112 -> 120
~ __ZN14TAATKernEngine8KernRunsER9SyncStateR13KerningStatus : 3384 -> 3360
~ __ZN28TKerningEngineImplementation11MergeDeltasERKNSt3__16vectorINS0_4pairIl19TAATDeltaXListEntryEENS0_9allocatorIS4_EEEERKNS0_3mapIl19TAATDeltaYListEntryNS0_4lessIlEENS5_INS2_IKlSB_EEEEEER9SyncStateRb : 1004 -> 1008
~ __ZNK21TAATMorphSubtableMorx10FetchClassEt : 120 -> 128
~ __ZN21TAATMorphSubtableMorx8ProcessTIN8TRunGlue17TGlyphInSingleRunEEE21MorphActionResultCodeRS1_7CFRangej : 3152 -> 3204
~ __ZN18TAATMorphTableMorx11ShapeGlyphsER9SyncStatePK10__CFString : 2608 -> 2624
~ __ZN13TStorageRange13ResetAdvancesERK5TFontNSt3__18optionalIjEE : 252 -> 256
~ __ZN16TCombiningEngine21ResolveCombiningMarksENS_13CombiningFlagEPbS1_ : 8016 -> 8024
~ __ZNK4TRun26GetNextUncombinedCharRangeElRb : 552 -> 568
~ __ZN19UniversalClassTable25AddShapingGlyphsForScriptERK5TFontjNSt3__18functionIFvttEEE : 1112 -> 1164
~ __ZN14TGlyphIterator25MatchCoverSequenceContextIL14MatchDirection1EEEbljPKN3OTL8OffsetToINS2_8Coverage5TableE15BigEndianScalarItEEEPKvSC_Pl : 280 -> 284
~ __ZNK9TBaseFont19GetDefaultFallbacksE10UIFontFlagm : 252 -> 260
~ __ZNK5TFont25GetOpticalBoundsForGlyphsEPKtP6CGRectlm : 1396 -> 1400
~ __ZNSt3__110__function6__funcIZNK5TFont25GetBoundingBoxesForGlyphsEPKtP6CGRectl17CTFontOrientationE3$_1FvlEEclEOl : 136 -> 140
~ __ZN7TCFBaseI21TNativeParagraphStyleE9ClassHashEPKv : 76 -> 80
~ _CTLineGetRangeOfCharacterClusterAtIndex : 1068 -> 1076
~ __ZNK5TLine21EnumerateCaretOffsetsENSt3__18functionIFvdlbPbEEE : 4004 -> 4008
~ __ZNK5TLine15GetClusterRangeERK11TCharStreamlll28CFStringCharacterClusterTypeP7CFRangePdPi : 2664 -> 2620
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERNS_6__lessIvvEEPZZNK5TLine21EnumerateCaretOffsetsENS_8functionIFvdlbPbEEEENK3$_0clEmiE9CaretPairEEvT1_SD_SD_OT0_NS_15iterator_traitsISD_E15difference_typeESI_PNSH_10value_typeEl : 1224 -> 1220
~ __ZL31CGFontVariationFromDictCallbackPKvS0_Pv : 392 -> 384
~ __ZNK4TRun29DrawGlyphsAtPositionsInternalEP9CGContext7CFRangePK7CGPointbPK11TAttributesb : 888 -> 884
~ __ZNSt3__16vectorI6TCFRefIPK8__CFDataENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_ : 204 -> 208
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE6resizeEm : 284 -> 288
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE6insertENS_11__wrap_iterIPKjEERS5_ : 436 -> 432
~ __ZNK12TFramesetter11FrameInRectER6TFrame7CFRangeRdRNSt3__15tupleIJddddddEEE : 1960 -> 2040
~ _CTRunGetGlyphs : 464 -> 468
~ __ZN17TAATMorphSubtable15DoSwashSubtableEN8TRunGlue6TGlyphES1_PKv : 252 -> 256
~ __ZNK8TRunGlue15CoveredByBitmapENSt3__14spanIKhLm18446744073709551615EEE7CFRange : 312 -> 308
~ __ZN21TAATMorphSubtableMorx8ProcessTIN8TRunGlue14TGlyphInVectorEEE21MorphActionResultCodeRS1_7CFRangej : 3168 -> 3216
~ __ZNK15TAATLookupTable18LookupSegmentArrayEtPm : 176 -> 180
~ __ZN8TRunGlue6RotateElllP17TGlyphAuxDataList : 2376 -> 2388
~ __ZN18IndicShapingEngine11SetFeaturesEPj : 9108 -> 9132
~ __ZN14TAATKerxEngine8KernRunsER9SyncStateR13KerningStatus : 5264 -> 5300
~ __ZN14TAATKerxEngine15KerxOrderedList14ProcessGlyphsTIN8TRunGlue14TGlyphInVectorEEEvR9SyncState : 728 -> 740
~ __ZNK8TRunGlue9GetOriginEl : 152 -> 156
~ __ZNK3OTL4GPOS16ApplyMarkBasePosEPKNS_14LookupSubtableER14TGlyphIteratorj : 768 -> 776
~ __ZNK3OTL4GPOS16ApplyMarkMarkPosEPKNS_11LookupTableEPKNS_14LookupSubtableER14TGlyphIteratorj : 964 -> 972
~ __ZN14PostGSUBFixups5applyER8TRunGluetRK15IndicClassTablej : 1996 -> 2000
~ __ZN14TGlyphIterator25MatchCoverSequenceAndNoteEjPKN3OTL8OffsetToINS0_8Coverage5TableE15BigEndianScalarItEEEPlPKvSB_ : 344 -> 348
~ _CTRunGetStringIndices : 472 -> 476
~ __ZNK9TBaseFont9SetObjectE15TableAssocationmPKv : 184 -> 200
~ __ZNK15TAATLookupTable18LookupTrimmedArrayEtPm : 68 -> 72
~ __ZNK9TBaseFont19GetDefaultCompositeE10UIFontFlagm : 452 -> 468
~ __ZN21IndicReorderingOutput9noteMatraEPK15IndicClassTablejlPKj : 492 -> 496
~ __ZN15IndicClassTableC2ERKS_PK8__CTFontRN3OTL4GSUBEb : 1720 -> 1708
~ __ZNK13TAATPropTable21GetPropertiesForGlyphEt : 208 -> 212
~ __ZL7hasFormPK9TBaseFontRN3OTL4GSUBERA2_Ktjb : 540 -> 544
~ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE6resizeEm : 284 -> 288
~ __ZNK5TFont33GetLigatureCaretPositionsForGlyphEtPdl : 1224 -> 1228
~ _vImageCompressionDecode_BGRA8888 : 4156 -> 4184
~ __ZNSt3__16vectorI7CFRange22TInlineBufferAllocatorIS1_Lm64ELm8EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 228 -> 236
~ __ZN21TAATMorphSubtableMorx8ProcessTIN8TRunGlue6TGlyphEEE21MorphActionResultCodeRS1_7CFRangej : 3232 -> 3240
~ __ZN21TAATMorphSubtableMorx18DoContextualActionER8TRunGluetNS0_6TGlyphEPKc : 812 -> 816
~ __ZNSt3__16vectorIlNS_9allocatorIlEEE6insertENS_11__wrap_iterIPKlEEOl : 404 -> 400
~ __ZNSt3__114__split_bufferIlRNS_9allocatorIlEEE12emplace_backIJlEEEvDpOT_ : 256 -> 260
~ __ZN17TAATMorphSubtable21DoRearrangementActionER8TRunGluejll : 7188 -> 7192
~ __ZN17TAATMorphSubtable4pushER8TRunGlueRNSt3__15stackINS_16SimpleGlyphEntryENS2_5dequeIS4_NS2_9allocatorIS4_EEEEEEl : 1260 -> 1272
~ __ZNK13TStorageRange13GetGlyphEntryEl : 216 -> 220
~ __ZNSt3__114__split_bufferIPN17TAATMorphSubtable16SimpleGlyphEntryENS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_ : 248 -> 252
~ __ZN8TRunGlue25ActualCharRangeForStorageEPK13TStorageRange : 132 -> 136
~ __ZNK4TRun25CopyDescriptionDictionaryEj : 1320 -> 1324
~ __ZNK4TRun8CopyPathEv : 352 -> 348
~ __ZNK4TRun18FindInsertionGroupEl : 592 -> 588
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERNS_7greaterIlEEPlLb1EEEvT1_S6_T0_NS_15iterator_traitsIS6_E15difference_typeEb : 3036 -> 3032
~ __ZNSt3__16vectorIlNS_9allocatorIlEEE18__insert_with_sizeB9fqn220106INS_17_ClassicAlgPolicyEPKlS7_EENS_11__wrap_iterIPlEENS8_IS7_EET0_T1_l : 516 -> 532
~ __ZNSt3__16vectorIlNS_9allocatorIlEEE6resizeEm : 284 -> 288
~ __ZN14TAATKerxEngine37ProcessKerxIndexArrayWithTupleScalarsEPK20KerxIndexArrayHeaderRNS_14KerxIndexArrayEjPdR9SyncState : 1424 -> 1440
~ __ZN14TAATKerxEngine15KerxOrderedList14ProcessGlyphsTIN8TRunGlue17TGlyphInSingleRunEEEvR9SyncState : 732 -> 744
~ __ZN14TAATKerxEngine15KerxOrderedList14ProcessGlyphsTIN8TRunGlue6TGlyphEEEvR9SyncState : 632 -> 644
~ __ZL8ProviderlPlPPK14__CFDictionaryPv : 48 -> 52
~ __ZN7TCFBaseI4TRunE9ClassHashEPKv : 108 -> 112
~ __ZZN11TTypesetter19ApplyVerticalLayoutER5TLinePK11TCharStreamPaENK3$_0clElP7CFRange : 488 -> 492
~ __ZN7TCFBaseI5TLineE9ClassHashEPKv : 76 -> 80
~ __ZNK5TLine17CopyHighlightPathE7CFRange : 544 -> 540
~ __ZNSt3__16vectorIP4TRunNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 184 -> 176
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZNK5TLine21EnumerateCaretOffsetsENS_8functionIFvdlbPbEEEE3$_2PNS2_9CaretInfoEEEvT1_SB_SB_OT0_NS_15iterator_traitsISB_E15difference_typeESG_PNSF_10value_typeEl : 1236 -> 1232
~ __ZNSt3__1eqB9fqn220106IbNS_9allocatorIbEEEEbRKNS_6vectorIT_T0_EES8_ : 56 -> 60
~ __ZN7TCFBaseI6TFrameE9ClassHashEPKv : 76 -> 80
~ __ZN7TCFBaseI11TTypesetterE9ClassHashEPKv : 76 -> 80
~ __ZN7TCFBaseI12TFramesetterE9ClassHashEPKv : 108 -> 112
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE6resizeEmb : 240 -> 244
~ __ZNK12TFramesetter11FrameInPathER6TFrame7CFRange : 2416 -> 2436
~ __ZN12TFramesetter20TPathFrameLinesetter11LayoutLinesENSt3__18functionIFhlEEERhRdS6_S6_ : 1804 -> 1792
~ __ZNSt3__123__specialized_algorithmINS_10_Algorithm6__copyEJNS_15__iterator_pairINS_14__bit_iteratorINS_6vectorIbNS_9allocatorIbEEEELb1ELm0EEES9_EENS_17__single_iteratorINS4_IS8_Lb0ELm0EEEEEEEclB9fqn220106ES9_S9_SC_ : 768 -> 772
~ ____ZN21TTypesetterAttrString10InitializeEPK20__CFAttributedStringb_block_invoke : 1112 -> 1128
~ __ZNKSt3__116__deque_iteratorI7CFRangePS1_RS1_PS2_lLl256EEplB9fqn220106El : 76 -> 80
~ __ZNSt3__114__split_bufferIP7CFRangeNS_9allocatorIS2_EEE12emplace_backIJRS2_EEEvDpOT_ : 256 -> 260
~ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB9fqn220106IP7CFRangeNS_16__deque_iteratorIS4_S5_RS4_PS5_lLl256EEELi0EEENS_4pairIT_T0_EESB_SB_SC_ : 244 -> 248
~ __ZN14TAATMorphTable16AddCoveredGlyphsERK5TFontP16CTFeatureSettingNSt3__18functionIFvttEEENS6_IFvvEEE : 892 -> 884
~ __ZNK14TAATMorphChain25FlagsForOptionalLigaturesEv : 112 -> 100
~ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE6resizeEm : 284 -> 288
~ __ZNK14TEmojiImageRun21DrawGlyphsAtPositionsEP9CGContext7CFRangePK7CGPointRKN4TRun34DrawGlyphsAtPositionsConfigurationE : 1380 -> 1376
~ __ZL18ApplyFixedAdvancesPK14__CFDictionaryblPd13AdvanceStride : 168 -> 172
~ __ZNSt3__16vectorIPKN11COLRv1Table5PaintENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_ : 184 -> 176
~ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE18__insert_with_sizeB9fqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS2_EESA_EESA_NS8_IPKS2_EET0_T1_l : 552 -> 568
~ __ZNSt3__110__function6__funcIZNK5TFont25GetBoundingBoxesForGlyphsEPKtP6CGRectl17CTFontOrientationE3$_0FvlEEclEOl : 40 -> 44
~ __ZN7TCFBaseI11TCollectionE9ClassHashEPKv : 76 -> 80
~ __ZNSt3__16vectorItNS_9allocatorItEEE18__insert_with_sizeB9fqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPtEES8_EES8_NS6_IPKtEET0_T1_l : 484 -> 500
~ __ZNSt3__16vectorINS_5tupleIJttlEEENS_9allocatorIS2_EEE7emplaceIJS2_EEENS_11__wrap_iterIPS2_EENS7_IPKS2_EEDpOT_ : 484 -> 488
~ __ZN7TCFBaseI15TRubyAnnotationE9ClassHashEPKv : 76 -> 80
~ __ZN11TJustEngine19ApplyTrackingToRunsER8TRunGlueRK11TCharStream7CFRangeld : 2344 -> 2348
~ __ZN11TJustEngine18GenerateMaximaListERK5TLineRK11TCharStream7CFRanged12DistributionmRNSt3__16vectorI19JustLeftRightMaximaNS8_9allocatorISA_EEEERNS9_INS8_5tupleIJlNS8_10unique_ptrINS9_ItNSB_ItEEEENS8_14default_deleteISI_EEEE6TCFRefIPK8__CFDataEEEENSB_ISR_EEEE : 1928 -> 1940
~ __ZN11TJustEngine13DistributeGapENSt3__111__wrap_iterIPP5CTRunEES5_7CFRanged12DistributionmPNS0_6vectorI19JustLeftRightMaximaNS0_9allocatorIS9_EEEEPNS8_IdNSA_IdEEEEPNS0_4pairIddEE : 1292 -> 1312
~ __ZN18TGenericJustEngine15GenerateMaximasERK5TLineRK11TCharStream7CFRangeRNSt3__16vectorI19JustLeftRightMaximaNS7_9allocatorIS9_EEEElb12DistributionRb : 1604 -> 1688
~ __ZN15TPostcompEngine9DoActionsENSt3__111__wrap_iterIPP5CTRunEES5_7CFRangeRKNS0_6vectorINS0_5tupleIJlNS0_10unique_ptrINS7_ItNS0_9allocatorItEEEENS0_14default_deleteISC_EEEE6TCFRefIPK8__CFDataEEEENSA_ISL_EEEEPKdPlPNS7_I12KashidaEntryNSA_IST_EEEE : 732 -> 740
~ __ZN18TAATPostcompEngine9DoActionsERKNSt3__16vectorItNS0_9allocatorItEEEEPK17JustPostcompTablePKvPKdPlPNS1_I12KashidaEntryNS2_ISF_EEEE : 2648 -> 2652
~ __ZN18TAATPostcompEngine13ApplyKashidasENSt3__111__wrap_iterIPP5CTRunEES5_RKNS0_6vectorI12KashidaEntryNS0_9allocatorIS7_EEEEPKd : 1196 -> 1200
~ __ZNK9ZapfTable16VariantsForGlyphEt : 532 -> 536
~ __ZN7TCFBaseI14TNativeTextTabE9ClassHashEPKv : 76 -> 80
~ __ZNSt3__16vectorINS_8functionIFvR11TAttributesEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRKS5_EEEPS5_DpOT_ : 224 -> 232
~ __ZNK3OTL4GPOS32GetSinglePosAdjustmentsForLookupERKNS_6LookupEtPdS4_ : 600 -> 604
~ __ZNK3OTL4GPOS15ApplyCursivePosEPKNS_14LookupSubtableER14TGlyphIteratorRKNS_8CoverageEjb : 760 -> 764
~ __ZNK3OTL4GPOS15ApplyMarkLigPosEPKNS_14LookupSubtableER14TGlyphIteratorj : 956 -> 960
~ __ZNK3OTL4GPOS22ApplyContextPosFormat3EPKNS_14LookupSubtableER14TGlyphIteratorm : 452 -> 460
~ __ZN8TRubyRun11UpdateWidthEP5TLineld : 1616 -> 1636
~ __ZNK3OTL4GSUB28WouldSubstituteLookupRecordsEPKNS_14LookupSubtableEPKNS_17SubstLookupRecordEjPKtj : 456 -> 472
~ __ZNK3OTL4GSUB24ApplyContextSubstFormat3EPKNS_14LookupSubtableER14TGlyphIteratorPtPNS_17SubstitutionStateEm : 460 -> 468
~ __ZNK3OTL4GSUB23WouldSubstituteContext3EPKNS_14LookupSubtableEPKtj : 372 -> 376
~ __ZNK3OTL4GSUB28WouldSubstituteChainContext3EPKNS_14LookupSubtableEPKtj : 440 -> 444
~ __ZNSt3__110__function6__funcIZNK3OTL4GDEF25IterateMarkGlyphsNotInSetEtNS_8functionIFvtEEEEUltttE_FvtttEEclEOtSA_SA_ : 148 -> 152
~ __ZN8TRunGlue13ReorderGlyphsERK11TCharStream : 808 -> 804
~ __ZN8TRunGlue16FilterSurrogatesERK11TCharStreamPNSt3__16vectorIlNS3_9allocatorIlEEEE : 920 -> 908
~ __ZN8TRunGlue26ReplaceCharRangeWithGlyphsE7CFRangeRKNSt3__16vectorItNS1_9allocatorItEEEES7_PKl : 1464 -> 1468
~ __ZNSt3__110__function6__funcIZZN14TOpenTypeMorph18AddVariantsOfGlyphERK5TFonttNS_8functionIFvtPK14__CFDictionaryEEEENK3$_0clEjPKN3OTL12FeatureTableERbEUltSH_E_FbtSH_EEclEOtSH_ : 1164 -> 1168
~ __ZNK16TCharStreamUTF169CopyCharsE7CFRange : 76 -> 80
~ __ZNK16TCharStreamUTF169CopyCharsE7CFRangePt : 20 -> 24
~ __ZNK18TCharStreamUniChar9CopyCharsE7CFRangePt : 336 -> 348
~ __ZZNSt3__16vectorIN12_GLOBAL__N_112PathObserver12IntersectionENS_9allocatorIS3_EEE12emplace_backIJRdRNS2_16IntersectionTypeERNS2_8LineSideERjEEERS3_DpOT_ENKUlvE0_clEv : 296 -> 304
~ __ZNSt3__16vectorItNS_9allocatorItEEE6insertENS_11__wrap_iterIPKtEERS5_ : 432 -> 428
~ __ZNSt3__114__split_bufferItRNS_9allocatorItEEE12emplace_backIJRKtEEEvDpOT_ : 252 -> 256
~ __ZNK13TAATPropTable11MirrorGlyphERt : 116 -> 124
~ __ZN7TCFBaseI16TNativeGlyphInfoE9ClassHashEPKv : 76 -> 80
~ ___CTStringIsSuitableForVerticalLayout_block_invoke_2 : 204 -> 208
~ __ZNK10TLCARTable25GetLigatureCaretPositionsEtPslPt : 412 -> 416
~ __ZNK10TLCARTable21GetLigatureCaretCountEt : 320 -> 324
~ __ZNSt3__16vectorI6TCFRefIP7CGColorENS_9allocatorIS4_EEE6insertENS_11__wrap_iterIPKS4_EERS9_ : 492 -> 496
~ __ZNSt3__18__rotateB9fqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPPKvEES6_EENS_4pairIT0_S8_EES8_S8_T1_ : 340 -> 344
~ __ZNSt3__16vectorI6TCFRefIP8__CFDataENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS1_IPKS2_EEEEPS4_DpOT_ : 204 -> 208
~ __ZNSt3__110__function6__funcIZL31InsertionInputsForMultipleSubstlPKN3OTL14LookupSubtableEbPKvRNS_6vectorIN12_GLOBAL__N_114InsertionInputENS_9allocatorISA_EEEEE3$_0FbtttEEclEOtSI_SI_ : 820 -> 824
~ __ZZNSt3__16vectorIN12_GLOBAL__N_114InsertionInputENS_9allocatorIS2_EEE12emplace_backIJRKS2_EEERS2_DpOT_ENKUlvE0_clEv : 412 -> 400
~ __ZNSt3__110__function6__funcIZL25LigInputsForLigatureSubstlPKN3OTL14LookupSubtableEPKvRKNS_6vectorItNS_9allocatorItEEEERNS8_IN12_GLOBAL__N_18LigInputENS9_ISF_EEEEE3$_0FbtttEEclEOtSM_SM_ : 780 -> 784
~ __ZZNSt3__16vectorIN12_GLOBAL__N_115StateMemberInfoENS_9allocatorIS2_EEE12emplace_backIJRKS2_EEERS2_DpOT_ENKUlvE0_clEv : 396 -> 384
~ __ZNSt3__16vectorI16MortFeatureEntryNS_9allocatorIS1_EEE7emplaceIJS1_EEENS_11__wrap_iterIPS1_EENS6_IPKS1_EEDpOT_ : 656 -> 660
~ __ZN20MyanmarShapingEngine18ApplyScriptShapingERKN3OTL4GSUBEPNS0_12GlyphLookupsE : 4560 -> 4536
~ __ZNSt3__16vectorI22TGlyphAuxDataListEntryNS_9allocatorIS1_EEE6resizeEm : 284 -> 288
~ __ZL35GetUncompressedBitmapRepresentationPK42XTDataCompressedBitmapRepresentationHeadermhPv : 160 -> 196
~ __ZN17TArabicJustEngine15GenerateMaximasERK5TLineRK11TCharStream7CFRangeRNSt3__16vectorI19JustLeftRightMaximaNS7_9allocatorIS9_EEEElb12DistributionRb : 4556 -> 4532
~ __ZNSt3__16vectorItNS_9allocatorItEEE18__insert_with_sizeB9fqn220106INS_17_ClassicAlgPolicyEPjS6_EENS_11__wrap_iterIPtEENS7_IPKtEET0_T1_l : 540 -> 564
~ __ZNK22TAATControlPointAccess26GetControlPointCoordinatesEtt : 1688 -> 1700
- __ZNSt3__16vectorI19CTFramePathFillRuleNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
~ __ZN29TBaselineEngineImplementation11ApplyToRunsENSt3__18functionIFbR4TRunEEE : 548 -> 544
~ __ZN14TAATBslnEngine15GetBaselineInfoEPK9BslnTablePKvRK5TFontP13TBaselineInfo : 704 -> 716
~ __ZNSt3__110__function6__funcIZN14TAATBslnEngine25ProcessBSLNFormatsWithMapEPK15SFNTLookupTable13BaselineClassE3$_0FbR4TRunEEclES9_ : 596 -> 604
~ __ZN23TOpenTypeBaselineEngine15GetBaselineInfoERKN3OTL4BASEERK5TFontjP13TBaselineInfoP13BaselineClass : 3176 -> 3168
~ __ZN13TAATAnkrTable26GetControlPointCoordinatesEtt : 236 -> 252
~ __ZNK13TAATOpbdTable13GetSideValuesEt : 260 -> 264
~ __ZNSt3__16vectorI14TScriptRunInfoNS_9allocatorIS1_EEE6insertENS_11__wrap_iterIPKS1_EERS6_ : 608 -> 612
~ __ZN22UniversalShapingEngine18ApplyScriptShapingERKN3OTL4GSUBEPNS0_12GlyphLookupsE : 8752 -> 8760
```
