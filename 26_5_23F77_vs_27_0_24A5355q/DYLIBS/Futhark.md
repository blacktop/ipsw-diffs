## Futhark

> `/System/Library/PrivateFrameworks/Futhark.framework/Futhark`

```diff

 121.0.0.0.0
-  __TEXT.__text: 0x12778
-  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__text: 0x12cc8
   __TEXT.__objc_methlist: 0x2fc
   __TEXT.__const: 0xcb0
-  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__gcc_except_tab: 0x78
   __TEXT.__cstring: 0x66d
-  __TEXT.__unwind_info: 0x2a8
-  __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methname: 0xbd8
-  __TEXT.__objc_methtype: 0x690
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x80
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0x80
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x800
+  __AUTH_CONST.__auth_got: 0x278
   __DATA.__objc_ivar: 0x94
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70AC8005-F32A-32E3-8943-973F6895F9E8
+  UUID: 25348FF6-0DE1-31DB-97E4-78581BE2AF43
   Functions: 184
   Symbols:   607
-  CStrings:  302
+  CStrings:  119
 
Functions:
~ -[FKTextFeature initWithType:boundingBox:corners:featureID:session:backingIndex:scale:] : 608 -> 612
~ +[FKTextFeature featureFromConcompIndex:session:scaling:type:createDiacriticFeatures:featureID:] : 576 -> 580
~ +[FKTextFeature featureFromSequenceIndex:session:scaling:createConcompFeatures:createDiacriticFeatures:featureID:] : 1232 -> 1248
~ -[FKTextFeature candidates] : 324 -> 340
~ -[FKTextDetector setRecognitionLanguages:] : 380 -> 384
~ _createOrResetSessions : 204 -> 208
~ -[FKTextDetector dealloc] : 132 -> 144
~ -[FKTextDetector translatePropertiesToOptionsWithNumSessions:] : 380 -> 384
~ -[FKTextDetector createFeaturesForSessionScale:roi:originalSize:startID:] : 440 -> 444
~ -[FKTextDetector mergeFeature:withArray:] : 804 -> 824
~ _getNumSharedConcomps : 316 -> 332
~ -[FKTextDetector createFeaturesForROI:originalSize:lastID:] : 468 -> 472
~ -[FKTextDetector runRecognizerOnFeatures:roi:size:lastID:] : 700 -> 712
~ _sortSequencesInSensibleOrder : 1024 -> 1044
~ -[FKTextDetector detectFeaturesInBuffer:withRegionOfInterest:error:] : 1912 -> 1944
~ _runDetectionOnSession : 1392 -> 1432
~ -[FKTextDetector getMemoryUsageOfLastOperation] : 52 -> 56
~ _extractCandidates : 780 -> 788
~ _FKRecognizeGetLangExtrachars : 140 -> 136
~ _FKRecognizeAddLanguage : 484 -> 488
~ _FKRecognizeSetLanguage : 104 -> 108
~ _FKRecognizeSequence : 3004 -> 3060
~ _rsSetUpDownNum : 1236 -> 1252
~ _rcFixSpecials : 232 -> 236
~ _rcFixSlanted_il : 140 -> 144
~ _rcAddDiacritics : 2452 -> 2480
~ _computeSpaceLimit : 464 -> 480
~ _rcSpace : 508 -> 516
~ _checkSpaceOne : 400 -> 408
~ _rcSelectCase : 816 -> 824
~ _rsRemoveBadWords : 716 -> 724
~ _FKSeqMatchGetConfidence : 328 -> 336
~ _FKRecognizeMultipleConcomps : 404 -> 420
~ _orderDiacriticToClusterCenters : 744 -> 764
~ _trySplit : 3348 -> 3428
~ _createAndRecognizeSubConcomp : 312 -> 320
~ _splitCCIfGood : 2288 -> 2416
~ _setDiacriticsOnSubCC : 316 -> 336
~ _calculatePenaltiesForBestPath : 472 -> 476
~ _getPathStats : 908 -> 920
~ _filterSplits : 1144 -> 1152
~ ___getPathStats_block_invoke : 980 -> 1000
~ _cutsCreateBadConcomp : 1404 -> 1412
~ _diacriticLooksLikeDot : 104 -> 108
~ _isFeasablePart : 164 -> 172
~ _isSaneSplit : 2204 -> 2248
~ _concatenatedCCsMatchCC : 188 -> 196
~ _combineSlash : 864 -> 916
~ _relativeYPosPercent : 324 -> 340
~ _diacriticIsResonablyCentered : 80 -> 84
~ _FKSessionDestroyRecognizer : 116 -> 128
~ _FKThresholdCalculateOtsuLimit : 456 -> 468
~ _FKThreshold : 116 -> 124
~ _FKThresholdBlockAverage : 692 -> 724
~ _FKThresholdMinMaxBlock : 2700 -> 2828
~ _FKConcompRelease : 200 -> 212
~ _FKConcompCreateSubConcomp : 1120 -> 1144
~ _FKComponentsFind : 996 -> 1028
~ _createConcompFromLineseg : 788 -> 804
~ _addScansegToScansegList : 940 -> 960
~ _sequenceUpdateBoxWithConcomp : 360 -> 368
~ _FKSequenceRemoveConcomp : 192 -> 196
~ _FKSequenceScoreAsPercent : 428 -> 448
~ _FKSequenceSortAndProcess : 308 -> 312
~ _sequenceSetSlope : 752 -> 764
~ _sequenceMarkup : 1416 -> 1448
~ _sequenceAddConcomp : 228 -> 236
~ _FKSequencesFind : 6088 -> 6080
~ _mergeNeighboringSequences : 824 -> 840
~ _sequenceRemove : 136 -> 148
~ _histogramIsOK : 572 -> 592
~ _FKSequenceOneBox : 588 -> 600
~ _sequenceCreate : 428 -> 432
~ _addDiacritic : 176 -> 188
~ _compareCCX : 40 -> 48
~ _computeBeta : 412 -> 416
~ _findNeighborAtY : 276 -> 280
~ _insertNeighbor : 592 -> 612
~ _sequenceMerge : 204 -> 224
CStrings:
- "(?=\"seqInd\"i\"ccInd\"i)"
- "@\"NSArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@16@0:8"
- "@28@0:8@16f24"
- "@32@0:8^{__CVBuffer=}16^@24"
- "@32@0:8{CGSize=dd}16"
- "@52@0:8i16^{FKSession=iiiiiiiiiI[128c]{vImage_Buffer=^vQQQ}{vImage_Buffer=^vQQQ}^{?}IIII^{?}^Sii^{concomp}iiiiii^{sequence}iiiiC^{recognizer}}20^{?={CGSize=dd}{CGPoint=dd}i}28B36B40^q44"
- "@56@0:8i16^{FKSession=iiiiiiiiiI[128c]{vImage_Buffer=^vQQQ}{vImage_Buffer=^vQQQ}^{?}IIII^{?}^Sii^{concomp}iiiiii^{sequence}iiiiC^{recognizer}}20^{?={CGSize=dd}{CGPoint=dd}i}28q36B44^q48"
- "@64@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24^@56"
- "@64@0:8q16^{CGRect={CGPoint=dd}{CGSize=dd}}24@32q40^{FKSession=iiiiiiiiiI[128c]{vImage_Buffer=^vQQQ}{vImage_Buffer=^vQQQ}^{?}IIII^{?}^Sii^{concomp}iiiiii^{sequence}iiiiC^{recognizer}}48(?=ii)56i60"
- "@72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48^q64"
- "@76@0:8i16{CGRect={CGPoint=dd}{CGSize=dd}}20{CGSize=dd}52^q68"
- "B"
- "B16@0:8"
- "C64@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24^@56"
- "FKTextCandidate"
- "FKTextFeature"
- "Q16@0:8"
- "T@\"NSArray\",&,N,V_subFeatures"
- "T@\"NSArray\",C,N,V_recognitionLanguages"
- "T@\"NSArray\",R,&,N,V_corners"
- "T@\"NSArray\",R,V_candidates"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_multiThreadingQueue"
- "T@\"NSString\",C,N,V_recognitionLanguage"
- "T@\"NSString\",C,N,V_text"
- "T@\"NSString\",R,C,N,V_text"
- "TB,N,V_colorSplits"
- "TB,N,V_createFeaturesForAllConcomps"
- "TB,N,V_detectDiacritics"
- "TB,N,V_enableBinarizerFiltering"
- "TB,N,V_minimizeFalseDetections"
- "TB,N,V_returnSubFeatures"
- "Tf,R,V_confidence"
- "Tf,V_confidence"
- "Ti,N,V_binarizerLimit"
- "Ti,N,V_contrastLimit"
- "Ti,N,V_minimumCharacterHeight"
- "Tq,N,V_thresholdingAlgorithm"
- "Tq,R,N,V_featureID"
- "Tq,R,N,V_type"
- "T{?=ii},N,V_mergeSettings"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_boundingBox"
- "UTF8String"
- "[8I]"
- "[8^{FKSession}]"
- "[8{?=\"scaleBuffer\"Q\"binarizer\"Q\"linesegs\"Q\"concomps\"Q\"sequences\"Q\"total\"Q}]"
- "^{FKSession=iiiiiiiiiI[128c]{vImage_Buffer=^vQQQ}{vImage_Buffer=^vQQQ}^{?}IIII^{?}^Sii^{concomp}iiiiii^{sequence}iiiiC^{recognizer}}"
- "^{recognizer=^vi[5{?=i^v{?=^v^v[4Q][4Q]QQQQQQQQQQi}{?=^v^v[4Q][4Q]QQQQQQQQQQi}{?=^v^v[4Q][4Q]QQQQQQQQQQi}}]^vi}"
- "_backingIndex"
- "_binarizerLimit"
- "_boundingBox"
- "_candidates"
- "_colorSplits"
- "_confidence"
- "_contrastLimit"
- "_corners"
- "_createFeaturesForAllConcomps"
- "_detectDiacritics"
- "_enableBinarizerFiltering"
- "_featureID"
- "_memoryUsage"
- "_mergeSettings"
- "_minimizeFalseDetections"
- "_minimumCharacterHeight"
- "_multiThreadingQueue"
- "_recognitionLanguage"
- "_recognitionLanguages"
- "_recognizer"
- "_returnSubFeatures"
- "_roi"
- "_scale"
- "_session"
- "_sessions"
- "_size"
- "_subFeatures"
- "_text"
- "_thresholdingAlgorithm"
- "_timeBinarizer"
- "_timeConcomps"
- "_timeDownscale"
- "_timeRecognizer"
- "_timeSequences"
- "_type"
- "addObject:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "binarizerLimit"
- "boolValue"
- "boundingBox"
- "candidates"
- "colorSplits"
- "confidence"
- "contrastLimit"
- "corners"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createFeaturesForAllConcomps"
- "createFeaturesForROI:originalSize:lastID:"
- "createFeaturesForSessionScale:roi:originalSize:startID:"
- "dealloc"
- "detectDiacritics"
- "detectFeaturesInBuffer:error:"
- "detectFeaturesInBuffer:withRegionOfInterest:error:"
- "dictionaryWithObjects:forKeys:count:"
- "disableMultithreading"
- "enableBinarizerFiltering"
- "errorWithDomain:code:userInfo:"
- "f"
- "f16@0:8"
- "featureFromConcompIndex:session:scaling:type:createDiacriticFeatures:featureID:"
- "featureFromSequenceIndex:session:scaling:createConcompFeatures:createDiacriticFeatures:featureID:"
- "featureID"
- "getMemoryUsageOfLastOperation"
- "i"
- "i16@0:8"
- "init"
- "initWithDimensions:"
- "initWithText:confidence:"
- "initWithType:boundingBox:corners:featureID:session:backingIndex:scale:"
- "isEqualToString:"
- "isValidPixelBuffer:regionOfInterest:error:"
- "length"
- "mergeFeature:withArray:"
- "mergeSettings"
- "minimizeFalseDetections"
- "minimumCharacterHeight"
- "multiThreadingQueue"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "q"
- "q16@0:8"
- "recognitionLanguage"
- "recognitionLanguages"
- "removeObjectAtIndex:"
- "resetOptions"
- "resetTimers"
- "returnSubFeatures"
- "runRecognizerOnFeatures:roi:size:lastID:"
- "setBinarizerLimit:"
- "setColorSplits:"
- "setConfidence:"
- "setContrastLimit:"
- "setCreateFeaturesForAllConcomps:"
- "setDetectDiacritics:"
- "setEnableBinarizerFiltering:"
- "setMergeSettings:"
- "setMinimizeFalseDetections:"
- "setMinimumCharacterHeight:"
- "setMultiThreadingQueue:"
- "setObject:atIndexedSubscript:"
- "setRecognitionLanguage:"
- "setRecognitionLanguages:"
- "setReturnSubFeatures:"
- "setSubFeatures:"
- "setText:"
- "setThresholdingAlgorithm:"
- "sortUsingComparator:"
- "standardUserDefaults"
- "stringWithUTF8String:"
- "subFeatures"
- "text"
- "thresholdingAlgorithm"
- "translatePropertiesToOptionsWithNumSessions:"
- "type"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v24@0:8{?=ii}16"
- "v32@0:8@16@24"
- "v80@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGSize=dd}56^q72"
- "{?=\"minScale\"i\"maxScale\"i}"
- "{?=ii}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"

```
