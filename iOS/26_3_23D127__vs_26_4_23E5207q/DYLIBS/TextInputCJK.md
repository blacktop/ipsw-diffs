## TextInputCJK

> `/System/Library/PrivateFrameworks/TextInputCJK.framework/TextInputCJK`

```diff

-3532.3.2.3.0
-  __TEXT.__text: 0x1ce34
-  __TEXT.__auth_stubs: 0xa20
+3532.4.3.0.0
+  __TEXT.__text: 0x1eb44
+  __TEXT.__auth_stubs: 0x9e0
   __TEXT.__init_offsets: 0x2c
   __TEXT.__objc_methlist: 0x1e48
   __TEXT.__const: 0xb8
   __TEXT.__cstring: 0xc23
   __TEXT.__ustring: 0x3aa
   __TEXT.__oslogstring: 0x134
-  __TEXT.__unwind_info: 0x678
+  __TEXT.__unwind_info: 0x738
   __TEXT.__objc_classname: 0x3de
   __TEXT.__objc_methname: 0x6e88
   __TEXT.__objc_methtype: 0x66a

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0xa40
-  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__auth_got: 0x4f8
   __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x1c60
   __AUTH_CONST.__objc_const: 0x2828

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 272A3F9C-4CE2-36FB-A724-A182F17C722D
+  UUID: 7BF8A812-1BAC-3507-95E8-1816F2C48526
   Functions: 672
-  Symbols:   2841
+  Symbols:   2837
   CStrings:  1605
 
Symbols:
+ __ZNSt3__16__treeINS_12__value_typeIfiEENS_19__map_value_compareIfNS_4pairIKfiEENS_4lessIfEELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
+ _objc_retainAutoreleasedReturnValue
- __ZNSt3__16__treeINS_12__value_typeIfiEENS_19__map_value_compareIfS2_NS_4lessIfEELb1EEENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
Functions:
~ -[TIKeyboardInputManagerChinese handlePairedPunctuationInput:context:] : 1060 -> 1156
~ -[TIKeyboardInputManagerChinese acceptFirstCandidateWithContext:] : 340 -> 368
~ -[TIKeyboardInputManagerChinese firstCandidate] : 120 -> 132
~ -[TIKeyboardInputManagerChinese setLearnsCorrection:] : 112 -> 116
~ -[TIKeyboardInputManagerChinese outputByConvertingDecimalPointForInput:] : 296 -> 332
~ -[TIKeyboardInputManagerChinese operationQueue] : 136 -> 144
~ -[TIKeyboardInputManagerChinese candidateData] : 168 -> 172
~ -[TIKeyboardInputManagerChinese groupedCandidatesFromCandidates:usingSortingMethod:completion:] : 260 -> 256
~ ___95-[TIKeyboardInputManagerChinese groupedCandidatesFromCandidates:usingSortingMethod:completion:]_block_invoke : 212 -> 216
~ -[TIKeyboardInputManagerChinese groupedCandidatesFromCandidates:usingSortingMethod:] : 172 -> 176
~ -[TIKeyboardInputManagerChinese sortMethodsGroupsForCandidates:] : 144 -> 152
~ -[TIKeyboardInputManagerChinese initialSelectedIndex] : 176 -> 188
~ -[TIKeyboardInputManagerChinese completionCandidateResultSetForKeyHint:] : 788 -> 812
~ -[TIKeyboardInputManagerChinese wordSearchEngineDidFindPredictionCandidates:] : 552 -> 588
~ -[TIKeyboardInputManagerChinese updateCompletionCandidatesIfAppropriate] : 280 -> 300
~ ___52-[TIKeyboardInputManagerChinese generateCompletions]_block_invoke : 684 -> 720
~ ___52-[TIKeyboardInputManagerChinese generateCompletions]_block_invoke.77 : 184 -> 208
~ ___52-[TIKeyboardInputManagerChinese generateCompletions]_block_invoke_2 : 324 -> 332
~ ___52-[TIKeyboardInputManagerChinese generateCompletions]_block_invoke_3 : 168 -> 180
~ -[TIKeyboardInputManagerChinese predictionOptions] : 156 -> 164
~ -[TIKeyboardInputManagerChinese mecabraCandidateRefFromPointerValue:] : 112 -> 124
~ -[TIKeyboardInputManagerChinese hasIdeographicCandidates] : 308 -> 320
~ -[TIKeyboardInputManagerChinese showingFacemarkCandidates] : 348 -> 356
~ -[TIKeyboardInputManagerChinese isFacemarkInput:] : 176 -> 184
~ -[TIKeyboardInputManagerChinese shouldEnableHalfWidthPunctuationForCurrentInputContext] : 164 -> 180
~ -[TIKeyboardInputManagerChinese wordCharacters] : 108 -> 120
~ -[TIKeyboardInputManagerChinese replacementForDoubleSpace] : 64 -> 80
~ -[TIKeyboardInputManagerChinese deleteFromInput:] : 104 -> 108
~ -[TIKeyboardInputManagerChinese didAcceptCandidate:] : 292 -> 312
~ -[TIKeyboardInputManagerChinese syncToKeyboardState:from:afterContextChange:] : 232 -> 240
~ -[TIKeyboardInputManagerChinese syncToLayoutState:] : 144 -> 148
~ -[TIKeyboardInputManagerChinese initImplementationWithMode:andLanguage:] : 320 -> 328
~ -[TIKeyboardInputManagerChinese resetCommitHistory] : 100 -> 108
~ -[TIKeyboardInputManagerChinese initWithConfig:keyboardState:] : 236 -> 248
~ +[TIKeyboardInputManagerChinese pairedPunctuationDictionary] : 84 -> 100
~ +[TIKeyboardInputManagerChinese unicodeCandidateFromString:] : 268 -> 284
~ +[TIKeyboardInputManagerChinese GB18030CandidateFromString:] : 324 -> 336
~ +[TIKeyboardInputManagerChinese punctuationPredictionsForString:] : 248 -> 264
~ -[TIKeyboardInputManagerWubi setAutoConfirmationCandidate:] : 20 -> 80
~ -[TIKeyboardInputManagerWubi supportsPairedPunctutationInput] : 184 -> 204
~ -[TIKeyboardInputManagerWubi isWubi:] : 140 -> 148
~ -[TIKeyboardInputManagerWubi inputsToReject] : 196 -> 204
~ -[TIKeyboardInputManagerWubi pushCandidateGenerationContextWithResults:] : 136 -> 140
~ -[TIKeyboardInputManagerWubi updateCandidatesWithTIWordSearch:predictionEnabled:] : 120 -> 124
~ -[TIKeyboardInputManagerWubi notifyUpdateCandidates:forOperation:] : 716 -> 768
~ ___66-[TIKeyboardInputManagerWubi notifyUpdateCandidates:forOperation:]_block_invoke : 220 -> 236
~ -[TIKeyboardInputManagerWubi formattedSearchString] : 96 -> 100
~ -[TIKeyboardInputManagerWubi deleteFromInput:] : 112 -> 116
~ -[TIKeyboardInputManagerWubi addInput:withContext:] : 812 -> 840
~ -[TIWordSearchWubihua uncachedCandidatesForOperation:] : 372 -> 384
~ -[TIWordSearchShapeBased validateCode:withOption:] : 124 -> 128
~ -[TIWordSearchShapeBased autoconvertLongestValidPrefixes:option:candidateResultSet:autoconvertedCandidateArray:] : 528 -> 552
~ -[TIKeyboardInputManagerPinyin remapInput:isFacemarkInput:] : 176 -> 184
~ -[TIKeyboardInputManagerPinyin isShuangpinSemicolon:] : 112 -> 116
~ -[TIKeyboardInputManagerPinyin currentShuangpinTypeUsesSemicolon] : 64 -> 68
~ -[TIKeyboardInputManagerPinyin adjustPhraseBoundaryInForwardDirection:granularity:] : 508 -> 524
~ -[TIKeyboardInputManagerPinyin validCharacterSetForAutocorrection] : 84 -> 100
~ ___66-[TIKeyboardInputManagerPinyin validCharacterSetForAutocorrection]_block_invoke : 112 -> 116
~ -[TIKeyboardInputManagerPinyin initialSelectedIndex] : 308 -> 328
~ -[TIWordSearchCangjie uncachedCandidatesForOperation:] : 928 -> 948
~ -[TIWordSearchCandidateResultSet(TIWordSearchCangjie) nthIndexIgnoringExtensionCandidates:] : 148 -> 156
~ -[TIKeyboardInputManagerShapeBased searchStringForMarkedText] : 76 -> 84
~ -[TIKeyboardInputManagerShapeBased markedTextWithAutoconvertedCandidates] : 544 -> 620
~ -[TIKeyboardInputManagerShapeBased didAcceptCandidate:] : 584 -> 616
~ -[TIKeyboardInputManagerShapeBased keyboardConfigurationLayoutTag] : 64 -> 80
~ -[TIKeyboardInputManagerShapeBased clearInput] : 216 -> 228
~ -[TIKeyboardInputManagerShapeBased deleteFromInput:] : 560 -> 604
~ -[TIKeyboardInputManagerShapeBased cancelCandidatesThread] : 64 -> 68
~ -[TIKeyboardInputManagerShapeBased candidateResultSet] : 256 -> 280
~ -[TIKeyboardInputManagerShapeBased updateCandidatesWithTIWordSearch:predictionEnabled:] : 304 -> 324
~ -[TIKeyboardInputManagerShapeBased hasCandidates] : 188 -> 208
~ -[TIKeyboardInputManagerShapeBased initialSelectedIndex] : 176 -> 188
~ -[TIKeyboardInputManagerShapeBased inputCount] : 116 -> 120
~ -[TIKeyboardInputManagerShapeBased inputIndex] : 56 -> 60
~ -[TIKeyboardInputManagerShapeBased rawInputString] : 112 -> 120
~ -[TIKeyboardInputManagerShapeBased searchString] : 92 -> 108
~ -[CIMCandidateData setCandidateInfoCache:] : 12 -> 64
~ -[CIMCandidateData setStoredCandidates:] : 12 -> 64
~ -[CIMCandidateData candidatesSortedByMethod:omittingEmoji:] : 668 -> 740
~ _SetLocaleFromInputMode : 100 -> 108
~ _GetCurrentLocale : 188 -> 196
~ -[CIMCandidateData candidatesSortedByWubi:omittingEmoji:] : 240 -> 252
~ -[CIMCandidateData candidatesSortedByPinyinOrZhuyin:simplified:zhuyin:] : 1120 -> 1172
~ ___71-[CIMCandidateData candidatesSortedByPinyinOrZhuyin:simplified:zhuyin:]_block_invoke_2 : 112 -> 120
~ ___71-[CIMCandidateData candidatesSortedByPinyinOrZhuyin:simplified:zhuyin:]_block_invoke : 112 -> 120
~ -[CIMCandidateData candidatesSortedByStrokes:simplified:] : 560 -> 600
~ -[CIMCandidateData candidatesSortedByRadical:simplified:collationLocale:] : 492 -> 520
~ -[CIMCandidateData candidatesSortedByEmoji:] : 268 -> 288
~ ___44-[CIMCandidateData candidatesSortedByEmoji:]_block_invoke : 72 -> 76
~ -[CIMCandidateData candidatesSortedByFrequency:omittingEmoji:] : 268 -> 284
~ -[CIMCandidateData candidateGroupsFromDictionary:sortedKeys:] : 640 -> 660
~ -[CIMCandidateData sortCharactersByStrokeCount:wordPropertiesDictionary:] : 552 -> 556
~ ___73-[CIMCandidateData sortCharactersByStrokeCount:wordPropertiesDictionary:]_block_invoke : 200 -> 216
~ -[CIMCandidateData wordPropertyDictionaryForCandidates:isSimplified:] : 364 -> 372
~ -[CIMCandidateData addCharacter:groupLabel:dictionary:isSecondary:] : 288 -> 300
~ -[CIMCandidateData clearCache] : 64 -> 68
~ -[CIMCandidateData initWithInputMode:] : 164 -> 168
~ +[CIMCandidateData shouldShowZhuyinSortingMethod] : 468 -> 492
~ -[NSString(CIMCandidateController) traditionalChineseZhuyinCompare:] : 368 -> 388
~ -[NSString(CIMCandidateController) chinesePinyinCompare:] : 116 -> 120
~ -[TIConversionHistory setMutableConvertedCandidateText:] : 12 -> 64
~ -[TIConversionHistory setMutableConvertedCandidateRefs:] : 12 -> 64
~ -[TIConversionHistory setConvertedCandidates:] : 12 -> 64
~ -[TIConversionHistory lastConvertedCandidate] : 76 -> 84
~ -[TIConversionHistory shouldRevertConvertedCandidateOnDeletionFromMarkedText:] : 188 -> 192
~ -[TIConversionHistory didRevertLastConvertedCandidate] : 308 -> 336
~ -[TIConversionHistory convertedCandidateText] : 72 -> 76
~ -[TIConversionHistory convertedLength] : 56 -> 60
~ -[TIConversionHistory clear] : 136 -> 148
~ -[TIConvertedCandidate setCandidate:] : 12 -> 64
~ -[TIConvertedCandidate revertedInput] : 76 -> 84
~ -[TIConvertedCandidate initWithCandidate:replacedAmbiguousPinyinSyllables:replacementUnambiguousPinyinSyllables:convertedInput:] : 232 -> 220
~ -[TIConvertedCandidate initWithCandidate:] : 152 -> 156
~ -[TIKeyboardInputManagerCangjie sortingMethods] : 132 -> 136
~ -[TIKeyboardInputManagerCangjie isPunctuationInput] : 136 -> 140
~ -[TIKeyboardInputManagerCangjie cangjieAlphabetSet] : 124 -> 136
~ -[TIKeyboardInputManagerCangjie cangjieSet] : 112 -> 128
~ -[TIKeyboardInputManagerCangjie cangjieInputType:fromPopupVariant:] : 256 -> 264
~ -[TIKeyboardInputManagerCangjie nonstopPunctuationCharacters] : 228 -> 252
~ ___69-[TIKeyboardInputManagerCangjie notifyUpdateCandidates:forOperation:]_block_invoke : 216 -> 232
~ -[TIKeyboardInputManagerCangjie selectedCandidateIsEnglish] : 160 -> 176
~ -[TIKeyboardInputManagerCangjie firstCandidateIsEnglish] : 176 -> 196
~ -[TIKeyboardInputManagerCangjie updateMarkedText] : 276 -> 304
~ -[TIKeyboardInputManagerCangjie formattedSearchString] : 80 -> 84
~ -[TIKeyboardInputManagerCangjie syncToKeyboardState:from:afterContextChange:] : 140 -> 148
~ -[TIKeyboardInputManagerCangjie addInput:withContext:] : 612 -> 640
~ -[TIKeyboardInputManagerCangjie syncWordSearch] : 112 -> 116
~ -[TIKeyboardInputManagerCangjie syncToLayoutState:] : 212 -> 224
~ -[TIKeyboardInputManagerCangjie supportsNumberKeySelection] : 60 -> 64
~ -[TIKeyboardHandwritingSpecialization nonstopPunctuationCharacters] : 116 -> 124
~ -[TIKeyboardHandwritingSpecialization replacementForDoubleSpace] : 96 -> 116
~ -[TIWordSearchChinesePhoneticOperationGetCandidates initWithWordSearch:inputString:keyboardInput:segmentBreakIndex:disambiguationCandidates:unambiguousSyllableCount:selectedDisambiguationCandidateIndex:regenerateDisambiguationCandidates:predictionEnabled:reanalysisMode:target:action:geometryModelData:hardwareKeyboardMode:logger:] : 304 -> 300
~ -[TIWordSearchHandwriting createMecabraContextFromCandidateContext:stringContext:] : 368 -> 364
~ -[TIWordSearchHandwriting generatePredictionsWithCandidateContext:stringContext:option:] : 516 -> 520
~ -[TIWordSearchHandwriting acceptCandidate:] : 304 -> 320
~ -[TIWordSearchHandwriting mecabraCreationOptionsDictionary] : 124 -> 128
~ -[TIWordSearchHandwriting_ja generateConversionsForCandidate:candidateContext:stringContext:] : 552 -> 548
~ ___93-[TIWordSearchHandwriting_ja generateConversionsForCandidate:candidateContext:stringContext:]_block_invoke : 204 -> 208
~ -[TIWordSearchHandwriting_ja generatePredictionsWithCandidateContext:stringContext:option:] : 536 -> 544
~ -[TIKeyboardInputManagerChinesePhonetic setSegments:] : 20 -> 80
~ -[TIKeyboardInputManagerChinesePhonetic setMostRecentCandidateResultSetPendingDisplay:] : 20 -> 80
~ -[TIKeyboardInputManagerChinesePhonetic setLogger:] : 20 -> 80
~ -[TIKeyboardInputManagerChinesePhonetic setPinyinSyllableCandidates:] : 20 -> 80
~ -[TIKeyboardInputManagerChinesePhonetic setReplacementUnambiguousPinyinSyllables:] : 20 -> 80
~ -[TIKeyboardInputManagerChinesePhonetic setReplacedAmbiguousPinyinSyllables:] : 20 -> 80
~ -[TIKeyboardInputManagerChinesePhonetic setConversionHistory:] : 20 -> 80
~ -[TIKeyboardInputManagerChinesePhonetic autocommitHeadSegmentWithContext:] : 260 -> 284
~ -[TIKeyboardInputManagerChinesePhonetic usesGeometryModelData] : 56 -> 60
~ -[TIKeyboardInputManagerChinesePhonetic generateReanalysisCandidatesIfAppropriate] : 492 -> 536
~ -[TIKeyboardInputManagerChinesePhonetic composedTextForSelectedCandidate:remainingInput:] : 1192 -> 1236
~ ___89-[TIKeyboardInputManagerChinesePhonetic composedTextForSelectedCandidate:remainingInput:]_block_invoke : 344 -> 348
~ -[TIKeyboardInputManagerChinesePhonetic hasLockedSyllable] : 60 -> 64
~ -[TIKeyboardInputManagerChinesePhonetic segmentedInputFromString:] : 524 -> 532
~ ___66-[TIKeyboardInputManagerChinesePhonetic segmentedInputFromString:]_block_invoke : 412 -> 432
~ -[TIKeyboardInputManagerChinesePhonetic SegmentedPinyin:inputMethodType:] : 480 -> 508
~ -[TIKeyboardInputManagerChinesePhonetic candidateForInlineTextSegmentation] : 284 -> 308
~ -[TIKeyboardInputManagerChinesePhonetic isPhraseBoundarySet] : 352 -> 392
~ -[TIKeyboardInputManagerChinesePhonetic updateComposedText] : 572 -> 636
~ -[TIKeyboardInputManagerChinesePhonetic wordSearchEngineDidFindCandidates:forOperation:] : 248 -> 244
~ ___88-[TIKeyboardInputManagerChinesePhonetic wordSearchEngineDidFindCandidates:forOperation:]_block_invoke : 2652 -> 2908
~ -[TIKeyboardInputManagerChinesePhonetic stringByPrependingConvertedCandidateTextToString:] : 160 -> 176
~ -[TIKeyboardInputManagerChinesePhonetic stringByStrippingConvertedCandidateTextFromString:] : 268 -> 288
~ -[TIKeyboardInputManagerChinesePhonetic convertedInput] : 76 -> 84
~ -[TIKeyboardInputManagerChinesePhonetic unconvertedInput] : 88 -> 96
~ -[TIKeyboardInputManagerChinesePhonetic inputStringForSearch] : 276 -> 296
~ -[TIKeyboardInputManagerChinesePhonetic analysisStringRange] : 180 -> 192
~ -[TIKeyboardInputManagerChinesePhonetic updateCandidatesByWaitingForResults:] : 668 -> 720
~ -[TIKeyboardInputManagerChinesePhonetic clearDynamicDictionary] : 64 -> 68
~ -[TIKeyboardInputManagerChinesePhonetic lastAcceptedCandidateCorrected] : 64 -> 68
~ -[TIKeyboardInputManagerChinesePhonetic didAcceptCandidate:] : 3240 -> 3568
~ -[TIKeyboardInputManagerChinesePhonetic canStartSentenceAfterString:] : 212 -> 220
~ -[TIKeyboardInputManagerChinesePhonetic handleAcceptedPinyinDisambiguationCandidate:keyboardState:] : 1424 -> 1504
~ -[TIKeyboardInputManagerChinesePhonetic defaultCandidate] : 476 -> 492
~ -[TIKeyboardInputManagerChinesePhonetic sortingMethods] : 284 -> 292
~ -[TIKeyboardInputManagerChinesePhonetic hasExtensionEmojiCandidates] : 204 -> 212
~ ___68-[TIKeyboardInputManagerChinesePhonetic hasExtensionEmojiCandidates]_block_invoke : 112 -> 120
~ -[TIKeyboardInputManagerChinesePhonetic candidateResultSetByWaitingForResults:] : 728 -> 800
~ -[TIKeyboardInputManagerChinesePhonetic predictionOptions] : 92 -> 84
~ -[TIKeyboardInputManagerChinesePhonetic setPhraseBoundary:] : 448 -> 480
~ -[TIKeyboardInputManagerChinesePhonetic setAutoCorrects:] : 80 -> 84
~ -[TIKeyboardInputManagerChinesePhonetic inputLocationChanged] : 144 -> 152
~ -[TIKeyboardInputManagerChinesePhonetic clearInput] : 188 -> 200
~ -[TIKeyboardInputManagerChinesePhonetic resume] : 132 -> 136
~ ___47-[TIKeyboardInputManagerChinesePhonetic resume]_block_invoke : 72 -> 76
~ -[TIKeyboardInputManagerChinesePhonetic deleteFromInput:] : 2732 -> 2996
~ -[TIKeyboardInputManagerChinesePhonetic convertInputsToSyntheticInputUptoCount:] : 192 -> 204
~ -[TIKeyboardInputManagerChinesePhonetic uncommittedText] : 204 -> 216
~ -[TIKeyboardInputManagerChinesePhonetic internalInputIndex] : 384 -> 392
~ -[TIKeyboardInputManagerChinesePhonetic internalInputCount] : 56 -> 60
~ -[TIKeyboardInputManagerChinesePhonetic inputString] : 184 -> 196
~ -[TIKeyboardInputManagerChinesePhonetic inputIndex] : 388 -> 412
~ -[TIKeyboardInputManagerChinesePhonetic inputCount] : 116 -> 120
~ -[TIKeyboardInputManagerChinesePhonetic setInput:] : 244 -> 252
~ -[TIKeyboardInputManagerChinesePhonetic addInputToInternal:] : 200 -> 204
~ -[TIKeyboardInputManagerChinesePhonetic handleDirectlyCommitForInput:withContext:] : 364 -> 376
~ -[TIKeyboardInputManagerChinesePhonetic remapInput:isFacemarkInput:] : 188 -> 192
~ -[TIKeyboardInputManagerChinesePhonetic addInput:withContext:] : 2128 -> 2240
~ ___62-[TIKeyboardInputManagerChinesePhonetic addInput:withContext:]_block_invoke : 336 -> 344
~ -[TIKeyboardInputManagerChinesePhonetic addInput:flags:point:firstDelete:] : 208 -> 212
~ -[TIKeyboardInputManagerChinesePhonetic _shouldCommitInputDirectly:] : 340 -> 348
~ ____ZL44GetDirectlyCommittedNumbersAndPunctuationSetv_block_invoke : 72 -> 76
~ -[TIKeyboardInputManagerChinesePhonetic isSpecialInput:] : 112 -> 116
~ -[TIKeyboardInputManagerChinesePhonetic inputContinuesGB18030OrUnicodeLookupKey:] : 440 -> 452
~ -[TIKeyboardInputManagerChinesePhonetic handleKeyboardInput:] : 172 -> 184
~ -[TIKeyboardInputManagerChinesePhonetic setInHardwareKeyboardMode:] : 120 -> 124
~ -[TIKeyboardInputManagerChinesePhonetic keyboardConfigurationLayoutTag] : 212 -> 224
~ -[TIKeyboardInputManagerChinesePhonetic syncToLayoutState:] : 176 -> 184
~ ___89-[TIKeyboardInputManagerChinesePhonetic externalIndexToInternal:shouldBoundToInputCount:]_block_invoke : 216 -> 220
~ -[TIKeyboardInputManagerChinesePhonetic internalIndexToExternal:] : 304 -> 308
~ ___65-[TIKeyboardInputManagerChinesePhonetic internalIndexToExternal:]_block_invoke : 296 -> 304
~ -[TIKeyboardInputManagerChinesePhonetic internalStringToExternal:] : 436 -> 476
~ -[TIKeyboardInputManagerChinesePhonetic externalStringToInternal:] : 144 -> 152
~ -[TIKeyboardInputManagerChinesePhonetic stringByRemovingSyllableSeparatorsFromString:] : 120 -> 128
~ -[TIKeyboardInputManagerChinesePhonetic searchStringForMarkedText] : 160 -> 172
~ -[TIKeyboardInputManagerChinesePhonetic internalInputString] : 340 -> 372
~ -[TIKeyboardInputManagerChinesePhonetic revertLastDisambiguation] : 604 -> 656
~ -[TIKeyboardInputManagerChinesePhonetic shiftPinyinSyllableSelection] : 176 -> 188
~ -[TIKeyboardInputManagerChinesePhonetic clearPinyinSyllableSelection] : 112 -> 120
~ -[TIKeyboardInputManagerChinesePhonetic storeLanguageModelDynamicDataIncludingCache] : 112 -> 116
~ -[TIKeyboardInputManagerChinesePhonetic syncToKeyboardState:from:afterContextChange:] : 172 -> 180
~ -[TIKeyboardInputManagerChinesePhonetic didDeleteCandidates:] : 100 -> 108
~ -[TIKeyboardInputManagerChinesePhonetic suspend] : 104 -> 108
~ -[TIKeyboardInputManagerChinesePhonetic dealloc] : 100 -> 104
~ -[TIKeyboardInputManagerChinesePhonetic supportsNumberKeySelection] : 60 -> 64
~ -[TIKeyboardInputManagerChinesePhonetic initWithConfig:keyboardState:] : 356 -> 368
~ +[TIKeyboardInputManagerChinesePhonetic stringFallBackForTenKeyInput:range:] : 232 -> 236
~ ___76+[TIKeyboardInputManagerChinesePhonetic stringFallBackForTenKeyInput:range:]_block_invoke : 140 -> 148
~ +[TIKeyboardInputManagerChinesePhonetic directlyCommittedCharacterSetForEmptyInline] : 160 -> 176
~ ___84+[TIKeyboardInputManagerChinesePhonetic directlyCommittedCharacterSetForEmptyInline]_block_invoke : 144 -> 156
~ +[TIKeyboardInputManagerChinesePhonetic ambiguousDefaults] : 256 -> 264
~ +[TIKeyboardInputManagerChinesePhonetic ambiguousAndPinyinCharacterSet] : 84 -> 100
~ ___71+[TIKeyboardInputManagerChinesePhonetic ambiguousAndPinyinCharacterSet]_block_invoke : 72 -> 76
~ +[TIKeyboardInputManagerChinesePhonetic ambiguousPinyinSet] : 96 -> 108
~ -[TIKeyboardInputManagerWubixing setAutoConfirmationCandidate:] : 20 -> 80
~ -[TIKeyboardInputManagerWubixing isValidWubiInput:] : 188 -> 192
~ ___51-[TIKeyboardInputManagerWubixing isValidWubiInput:]_block_invoke : 148 -> 160
~ -[TIKeyboardInputManagerWubixing notifyUpdateCandidates:forOperation:] : 204 -> 200
~ ___70-[TIKeyboardInputManagerWubixing notifyUpdateCandidates:forOperation:]_block_invoke : 284 -> 308
~ -[TIKeyboardInputManagerWubixing inputIndex] : 56 -> 60
~ -[TIKeyboardInputManagerWubixing updateMarkedText] : 92 -> 96
~ -[TIKeyboardInputManagerWubixing addInput:withContext:] : 500 -> 512
~ -[TIKeyboardInputManagerWubixing supportsNumberKeySelection] : 60 -> 64
~ -[TIKeyboardInputManagerWubixing initialSelectedIndex] : 132 -> 136
~ -[RecognizerProvider unloadRecognizer] : 84 -> 88
~ -[RecognizerProvider provideRecognizerToBlock:] : 128 -> 124
~ -[RecognizerProvider recognizer] : 356 -> 368
~ -[RecognizeDrawingOperation setRecognizer:] : 20 -> 80
~ -[RecognizeDrawingOperation setStickers:] : 20 -> 80
~ -[RecognizeDrawingOperation setHistory:] : 20 -> 80
~ -[RecognizeDrawingOperation setManager:] : 20 -> 80
~ -[RecognizeDrawingOperation setCandidates:] : 20 -> 80
~ -[RecognizeDrawingOperation main] : 712 -> 760
~ ___33-[RecognizeDrawingOperation main]_block_invoke : 316 -> 340
~ -[RecognizeDrawingOperation initWithInputManager:strokes:history:] : 256 -> 264
~ +[RecognizeDrawingOperation recognitionResultsForDrawing:withRecognizer:history:shouldCancel:] : 388 -> 392
~ ____ZL56TIGetHandwritingMultipleCharacterRecognitionEnabledValuev_block_invoke : 96 -> 100
~ +[RecognizeDrawingOperation textRecognitionResultsForDrawing:withRecognizer:keyboardState:history:shouldCancel:] : 728 -> 724
~ +[RecognizeDrawingOperation recognitionContentTypeForKeyboardState:] : 288 -> 300
~ -[GeneratePredictionsOperation main] : 1264 -> 1352
~ ___36-[GeneratePredictionsOperation main]_block_invoke : 316 -> 340
~ ___36-[GeneratePredictionsOperation main]_block_invoke_2 : 128 -> 124
~ -[GeneratePredictionsOperation initWithInputManager:predictionOptions:prefixContext:] : 260 -> 268
~ -[TIInputManagerHandwriting setProactiveTriggers:] : 20 -> 80
~ -[TIInputManagerHandwriting setCommittedCandidates:] : 20 -> 80
~ -[TIInputManagerHandwriting setCandidateRefsDictionary:] : 20 -> 80
~ -[TIInputManagerHandwriting setCandidates:] : 20 -> 80
~ -[TIInputManagerHandwriting setUserDrawing:] : 20 -> 80
~ -[TIInputManagerHandwriting candidateData] : 136 -> 148
~ -[TIInputManagerHandwriting processCandidates:stickers:] : 2880 -> 3012
~ -[TIInputManagerHandwriting mecabraLanguage] : 56 -> 60
~ -[TIInputManagerHandwriting keyboardConfigurationLayoutTag] : 64 -> 80
~ -[TIInputManagerHandwriting shouldEnableHalfWidthPunctuationForCurrentInputContext] : 164 -> 180
~ -[TIInputManagerHandwriting suppressPlaceholderCandidate] : 64 -> 68
~ -[TIInputManagerHandwriting deleteFromInputWithContext:] : 876 -> 956
~ -[TIInputManagerHandwriting updateCompletionCandidatesIfAppropriate] : 1356 -> 1384
~ ___68-[TIInputManagerHandwriting updateCompletionCandidatesIfAppropriate]_block_invoke : 664 -> 740
~ ___68-[TIInputManagerHandwriting updateCompletionCandidatesIfAppropriate]_block_invoke_2 : 696 -> 704
~ ___68-[TIInputManagerHandwriting updateCompletionCandidatesIfAppropriate]_block_invoke_7 : 184 -> 196
~ __Z37handwritingResponseKitBackgroundQueuev : 84 -> 100
~ ___68-[TIInputManagerHandwriting updateCompletionCandidatesIfAppropriate]_block_invoke_3 : 528 -> 520
~ ___68-[TIInputManagerHandwriting updateCompletionCandidatesIfAppropriate]_block_invoke_5 : 260 -> 240
~ ___68-[TIInputManagerHandwriting updateCompletionCandidatesIfAppropriate]_block_invoke_6 : 852 -> 916
~ ____Z37handwritingResponseKitBackgroundQueuev_block_invoke : 104 -> 108
~ -[TIInputManagerHandwriting shouldLookForCompletionCandidates] : 96 -> 100
~ -[TIInputManagerHandwriting predictionOptions:] : 108 -> 112
~ -[TIInputManagerHandwriting clearCandidateRefsDictionary] : 64 -> 68
~ -[TIInputManagerHandwriting didAcceptCandidate:] : 1760 -> 1980
~ -[TIInputManagerHandwriting mainThreadUpdateCandidates:] : 832 -> 904
~ -[TIInputManagerHandwriting updateCandidates] : 216 -> 232
~ -[TIInputManagerHandwriting addInputObject:] : 128 -> 132
~ -[TIInputManagerHandwriting cancelRecognition] : 168 -> 176
~ ___46-[TIInputManagerHandwriting cancelRecognition]_block_invoke : 236 -> 256
~ -[TIInputManagerHandwriting addInput:withContext:] : 636 -> 668
~ -[TIInputManagerHandwriting syncMarkedTextForKeyboardState:afterContextChange:] : 112 -> 116
~ -[TIInputManagerHandwriting facemarkCandidates] : 496 -> 524
~ -[TIInputManagerHandwriting markedTextForDefaultCandidate] : 96 -> 104
~ -[TIInputManagerHandwriting isDummyCandidate:] : 96 -> 100
~ -[TIInputManagerHandwriting defaultCandidate] : 436 -> 448
~ -[TIInputManagerHandwriting keyboardCandidateResultSetFromResults] : 832 -> 896
~ ___66-[TIInputManagerHandwriting keyboardCandidateResultSetFromResults]_block_invoke : 396 -> 412
~ -[TIInputManagerHandwriting candidateResultSet] : 156 -> 168
~ -[TIInputManagerHandwriting shouldCommitInputString] : 80 -> 84
~ -[TIInputManagerHandwriting updateDictionaryPaths] : 148 -> 152
~ ___50-[TIInputManagerHandwriting updateDictionaryPaths]_block_invoke : 272 -> 288
~ -[TIInputManagerHandwriting updateUserWordEntries] : 272 -> 280
~ ___50-[TIInputManagerHandwriting updateUserWordEntries]_block_invoke_2 : 108 -> 112
~ -[TIInputManagerHandwriting updateAddressBook] : 564 -> 592
~ ___46-[TIInputManagerHandwriting updateAddressBook]_block_invoke : 360 -> 372
~ ___46-[TIInputManagerHandwriting updateAddressBook]_block_invoke.207 : 108 -> 112
~ -[TIInputManagerHandwriting suspend] : 88 -> 92
~ -[TIInputManagerHandwriting keyboardActivityDidTransition:] : 272 -> 284
~ -[TIInputManagerHandwriting recognizerProvider] : 316 -> 328
~ ___47-[TIInputManagerHandwriting recognizerProvider]_block_invoke_2 : 156 -> 160
~ -[TIInputManagerHandwriting recognizer] : 76 -> 84
~ -[TIInputManagerHandwriting dealloc] : 432 -> 452
~ -[TIInputManagerHandwriting initImplementation] : 172 -> 180
~ -[TIInputManagerHandwriting initWithConfig:keyboardState:] : 348 -> 368
~ -[TIInputManagerHandwriting(TestingSupport) clearObservers] : 276 -> 288
~ -[CHRecognitionResult(TIAdditions) mecabraHandwritingCandidate] : 684 -> 708
~ -[TIWordSearchChinesePhonetic setFuzzyPinyinPairs:] : 20 -> 80
~ -[TIWordSearchChinesePhonetic uncachedCandidatesForOperation:] : 4100 -> 4252
~ -[TIWordSearchChinesePhonetic candidatesCacheKeyForOperation:] : 228 -> 244
~ __ZL11GetCacheKeyP8NSStringP15MCKeyboardInputbmbbm : 352 -> 368
~ -[TIWordSearchChinesePhonetic clearCacheForInputString:keyboardInput:unambiguousSyllableCount:selectedDisambiguationCandidateIndex:] : 192 -> 196
~ -[TIWordSearchChinesePhonetic nameReadingPairGenerationMode] : 96 -> 104
~ -[TIWordSearchChinesePhonetic mecabraInputMethodType] : 256 -> 264
~ -[TIWordSearchChinesePhonetic updateShuangpinTypeWithReanalysisMode:] : 312 -> 332
~ -[TIWordSearchChinesePhonetic setCustomDialectLanguageModel:] : 236 -> 248
~ -[TIWordSearchChinesePhonetic updateFuzzyPinyinSettings] : 684 -> 736
~ +[TIWordSearchChinesePhonetic pinyinCharacterSetWithTones] : 84 -> 100
~ ___58+[TIWordSearchChinesePhonetic pinyinCharacterSetWithTones]_block_invoke : 72 -> 76
~ -[TIWordSearchWubixing shouldAutoCommitCode:withOption:] : 144 -> 148
~ -[TIWordSearchWubixing autoconvertWubiXingPrefixes:option:candidateResultSet:autoconvertedCandidateArray:] : 436 -> 456
~ -[TIWordSearchWubixing uncachedCandidatesForOperation:] : 944 -> 1008
~ ___55-[TIWordSearchWubixing uncachedCandidatesForOperation:]_block_invoke : 72 -> 76
~ -[TIWordSearchWubixing wubiStandardPreference] : 136 -> 144
~ -[TIWordSearchWubixing mecabraCreationOptionsDictionary] : 200 -> 208

```
