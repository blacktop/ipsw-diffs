## TextInputCJK

> `/System/Library/PrivateFrameworks/TextInputCJK.framework/Versions/A/TextInputCJK`

```diff

-3479.227.0.0.0
-  __TEXT.__text: 0x1fd7c
+3479.319.0.0.0
+  __TEXT.__text: 0x1fd78
   __TEXT.__auth_stubs: 0x7e0
   __TEXT.__init_offsets: 0x2c
-  __TEXT.__objc_methlist: 0x1cf0
+  __TEXT.__objc_methlist: 0x1e48
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0xbe9
   __TEXT.__ustring: 0x3aa
   __TEXT.__oslogstring: 0x88
-  __TEXT.__unwind_info: 0x6c0
+  __TEXT.__unwind_info: 0x6b8
   __TEXT.__objc_classname: 0x3de
   __TEXT.__objc_methname: 0x6ccb
   __TEXT.__objc_methtype: 0x66a

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a88
+  __DATA_CONST.__objc_selrefs: 0x1b08
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0xa40
   __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0x890
   __AUTH_CONST.__cfstring: 0x1c60
-  __AUTH_CONST.__objc_const: 0x2a90
+  __AUTH_CONST.__objc_const: 0x2828
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4277683-051B-3690-B4B3-B2D1A49E357B
-  Functions: 707
+  UUID: 78EBF562-F27C-336E-BAEA-2BF70ED5CC7C
+  Functions: 706
   Symbols:   2142
   CStrings:  1586
 
Functions:
~ ___52-[TIKeyboardInputManagerChinese generateCompletions]_block_invoke_2 : 336 -> 332
~ __52-[TIKeyboardInputManagerChinese generateCompletions]_block_invoke.82 : 108 -> 104
~ -[TIKeyboardInputManagerChinese showingFacemarkCandidates] : 360 -> 372
~ -[TIKeyboardInputManagerChinese deleteFromInputWithContext:] : 144 -> 148
~ +[TIKeyboardInputManagerChinese unicodeCandidateFromString:] : 304 -> 296
~ +[TIKeyboardInputManagerChinese punctuationPredictionsForString:] : 284 -> 280
~ -[TIKeyboardInputManagerWubi notifyUpdateCandidates:forOperation:] : 836 -> 832
~ ___66-[TIKeyboardInputManagerWubi notifyUpdateCandidates:forOperation:]_block_invoke : 256 -> 252
~ -[TIWordSearchShapeBased autoconvertLongestValidPrefixes:option:candidateResultSet:autoconvertedCandidateArray:] : 604 -> 596
~ -[TIKeyboardInputManagerPinyin acceptAutocorrectionCommitsInline] : 80 -> 88
~ -[TIKeyboardInputManagerPinyin usesGeometryModelData] : 80 -> 84
~ -[TIWordSearchCangjie validateCode:withOption:] : 284 -> 280
~ -[CIMCandidateData candidatesSortedByMethod:omittingEmoji:] : 724 -> 756
- sub_2510f324c
~ -[NSString(CIMCandidateController) traditionalChineseZhuyinCompare:] : 424 -> 416
~ -[TIConvertedCandidate initWithCandidate:replacedAmbiguousPinyinSyllables:replacementUnambiguousPinyinSyllables:convertedInput:] : 284 -> 276
~ -[TIKeyboardInputManagerCangjie notifyUpdateCandidates:forOperation:] : 244 -> 240
~ ___69-[TIKeyboardInputManagerCangjie notifyUpdateCandidates:forOperation:]_block_invoke : 260 -> 256
~ -[TIKeyboardInputManagerChinesePhonetic composedTextForSelectedCandidate:remainingInput:] : 1332 -> 1340
~ -[TIKeyboardInputManagerChinesePhonetic shouldDelayUpdateComposedText] : 100 -> 96
~ -[TIKeyboardInputManagerChinesePhonetic updateComposedText] : 648 -> 652
~ -[TIKeyboardInputManagerChinesePhonetic wordSearchEngineDidFindCandidates:forOperation:] : 280 -> 276
~ __ZNK3WTF10RefCountedIN2TI8Favonius14KeyboardLayoutEE5derefEv : 344 -> 348
~ -[TIKeyboardInputManagerChinesePhonetic analysisStringRange] : 200 -> 204
~ -[TIKeyboardInputManagerChinesePhonetic didAcceptCandidate:] : 3860 -> 3856
~ -[TIKeyboardInputManagerChinesePhonetic setPhraseBoundary:] : 488 -> 492
~ -[TIKeyboardInputManagerChinesePhonetic deleteFromInput:] : 3276 -> 3280
~ -[TIKeyboardInputManagerChinesePhonetic setInput:] : 264 -> 268
~ -[TIKeyboardInputManagerChinesePhonetic addInput:withContext:] : 2404 -> 2408
~ -[TIKeyboardInputManagerChinesePhonetic _shouldCommitInputDirectly:] : 364 -> 368
~ -[TIKeyboardInputManagerChinesePhonetic keyboardConfigurationLayoutTag] : 216 -> 220
~ -[TIKeyboardInputManagerChinesePhonetic internalStringToExternal:] : 492 -> 496
~ -[TIKeyboardInputManagerChinesePhonetic searchStringForMarkedText] : 172 -> 176
~ -[TIKeyboardInputManagerChinesePhonetic revertLastDisambiguation] : 704 -> 700
~ -[TIKeyboardInputManagerChinesePhonetic syncToKeyboardState:from:afterContextChange:] : 180 -> 184
~ -[TIKeyboardInputManagerWubixing notifyUpdateCandidates:forOperation:] : 220 -> 216
~ ___70-[TIKeyboardInputManagerWubixing notifyUpdateCandidates:forOperation:]_block_invoke : 336 -> 332
~ -[RecognizeDrawingOperation main] : 832 -> 828
~ ___33-[RecognizeDrawingOperation main]_block_invoke : 368 -> 364
~ ___33-[RecognizeDrawingOperation main]_block_invoke_2 : 112 -> 108
~ -[GeneratePredictionsOperation main] : 1428 -> 1424
~ ___36-[GeneratePredictionsOperation main]_block_invoke : 368 -> 364
~ -[TIInputManagerHandwriting processCandidates:stickers:] : 3260 -> 3244
~ -[TIInputManagerHandwriting addInput:withContext:] : 724 -> 728
~ ___66-[TIInputManagerHandwriting keyboardCandidateResultSetFromResults]_block_invoke : 432 -> 436
~ -[TIInputManagerHandwriting recognizerProvider] : 336 -> 328
~ ___47-[TIInputManagerHandwriting recognizerProvider]_block_invoke : 356 -> 344
~ ___47-[TIInputManagerHandwriting recognizerProvider]_block_invoke_2 : 160 -> 156
~ -[CHRecognitionResult(TIAdditions) mecabraHandwritingCandidate] : 724 -> 728
~ -[TIWordSearchChinesePhonetic uncachedCandidatesForOperation:] : 4224 -> 4268

```
