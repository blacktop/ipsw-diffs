## Futhark

> `/System/Library/PrivateFrameworks/Futhark.framework/Futhark`

```diff

-120.1.0.0.0
-  __TEXT.__text: 0x12bcc
+121.0.0.0.0
+  __TEXT.__text: 0x12778
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__objc_methlist: 0x2fc
-  __TEXT.__const: 0xc98
+  __TEXT.__const: 0xcb0
   __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__cstring: 0x66f
-  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__cstring: 0x66d
+  __TEXT.__unwind_info: 0x2a8
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x2d
   __TEXT.__objc_methname: 0xbd8

   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F6BE7DC-B9FD-39E4-8671-23176A2A6988
-  Functions: 183
+  UUID: 5E0A62CE-833E-3F53-B3C8-9D29CCBE384A
+  Functions: 184
   Symbols:   607
   CStrings:  302
 
Symbols:
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.37
- ___block_descriptor_tmp.33
- ___block_descriptor_tmp.34
Functions:
+ sub_20b951e00
~ -[FKTextFeature initWithType:boundingBox:corners:featureID:session:backingIndex:scale:] : 596 -> 608
~ +[FKTextFeature featureFromSequenceIndex:session:scaling:createConcompFeatures:createDiacriticFeatures:featureID:] : 1212 -> 1232
~ -[FKTextDetector initWithDimensions:] : 168 -> 160
~ _createOrResetSessions : 208 -> 204
~ _sortSequencesInSensibleOrder : 1168 -> 1024
~ -[FKTextDetector detectFeaturesInBuffer:withRegionOfInterest:error:] : 1920 -> 1912
~ _runDetectionOnSession : 1388 -> 1392
~ _FKPrintRender : 236 -> 232
~ _FKRecognizeSequence : 3020 -> 3004
~ _rsSetUpDownNum : 1232 -> 1236
~ _computeSpaceLimit : 468 -> 464
~ _rsRemoveBadWords : 720 -> 716
~ _candlistInsert : 252 -> 236
~ _FKRecognizeMultipleConcomps : 396 -> 404
~ _vUpdate : 664 -> 656
~ _vPredict : 416 -> 420
~ _trySplit : 3268 -> 3348
~ _splitCCIfGood : 2308 -> 2288
~ _setDiacriticsOnSubCC : 320 -> 316
~ _calculatePenaltiesForBestPath : 476 -> 472
~ _getPathStats : 928 -> 908
~ _filterSplits : 1140 -> 1144
~ _walkPathAndReturnFinalColumn : 196 -> 192
~ ___getPathStats_block_invoke : 1008 -> 980
~ _areCutsTooClose : 252 -> 232
~ _isCuttingSerif : 448 -> 440
~ _cutsCreateBadConcomp : 1700 -> 1404
~ _findEndBlackPixelRowInColumn : 132 -> 128
~ _isSaneSplit : 2324 -> 2204
~ _relativeYPosPercent : 320 -> 324
~ _FKThresholdCalculateOtsuLimit : 460 -> 456
~ _FKConcompRelease : 196 -> 200
~ _FKComponentsFind : 1136 -> 996
~ _createNewLineseg : 508 -> 512
~ _createConcompFromLineseg : 964 -> 788
~ _addScansegToScansegList : 944 -> 940
~ _FKSequenceAdjustSlantedLines : 228 -> 232
~ _FKSequenceScoreAsPercent : 432 -> 428
~ _FKSequenceSortAndProcess : 300 -> 308
~ _sequenceMarkup : 1444 -> 1416
~ _FKSequencesFind : 6312 -> 6088
~ _concompCanBeGlyph : 132 -> 128
~ _mergeNeighboringSequences : 832 -> 824
~ _histogramIsOK : 576 -> 572
~ _FKSequenceOneBox : 596 -> 588
~ _computeBeta : 428 -> 412
~ _pixelCount : 148 -> 152
CStrings:
+ "Futhark-121"
- "Futhark-120.1"

```
