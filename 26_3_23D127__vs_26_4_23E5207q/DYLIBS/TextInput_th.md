## TextInput_th

> `/System/Library/TextInput/TextInput_th.bundle/TextInput_th`

```diff

-3532.3.2.3.0
-  __TEXT.__text: 0x3d5c
-  __TEXT.__auth_stubs: 0x4e0
+3532.4.3.0.0
+  __TEXT.__text: 0x3fac
+  __TEXT.__auth_stubs: 0x4b0
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x3fc
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x183
+  __TEXT.__cstring: 0x2d4
   __TEXT.__oslogstring: 0x3
   __TEXT.__ustring: 0x126
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_selrefs: 0x4e0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x3b8
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0xf8
   __AUTH_CONST.__cfstring: 0x9c0
   __AUTH_CONST.__objc_const: 0x328

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AD496E43-108E-3BDA-B6B3-E0B64E0DE5E9
+  UUID: 1041B4FA-7346-3B1C-8AE5-C59BC9EDF996
   Functions: 130
-  Symbols:   526
-  CStrings:  292
+  Symbols:   523
+  CStrings:  293
 
Symbols:
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fon210106Ev
+ __ZNSt3__127__tree_balance_after_insertB9fon210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE5clearB9fon210106Ev
+ __ZNSt3__19remove_ifB9fon210106INS_11__wrap_iterIPN2KB9CandidateEEEU13block_pointerFbRKS3_EEET_SA_SA_T0_
+ _objc_retainAutoreleasedReturnValue
- __ZNSt3__119__shared_weak_count16__release_sharedB8nn200100Ev
- __ZNSt3__127__tree_balance_after_insertB8nn200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE5clearB8nn200100Ev
- __ZNSt3__19remove_ifB8nn200100INS_11__wrap_iterIPN2KB9CandidateEEEU13block_pointerFbRKS3_EEET_SA_SA_T0_
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[TIKeyboardInputManager_th initImplementation] : 200 -> 208
~ -[TIKeyboardInputManager_th setAutoCorrects:] : 80 -> 84
~ -[TIKeyboardInputManager_th firstMecabraCandidateOccurranceFromLastAutocorrectionList] : 416 -> 436
~ -[TIKeyboardInputManager_th shouldAutocommitForInput:] : 488 -> 520
~ -[TIKeyboardInputManager_th trimmedInputStem] : 432 -> 468
~ -[TIKeyboardInputManager_th dropInputPrefix:commitToWordSearch:] : 324 -> 340
~ -[TIKeyboardInputManager_th setInput:] : 368 -> 384
~ -[TIKeyboardInputManager_th textAccepted:fromPredictiveInputBar:withInput:] : 532 -> 568
~ -[TIKeyboardInputManager_th addTouch:shouldHitTest:] : 308 -> 332
~ -[TIKeyboardInputManager_th addInput:withContext:] : 692 -> 736
~ -[TIKeyboardInputManager_th deleteFromInput:] : 392 -> 428
~ -[TIKeyboardInputManager_th usesComposingInput] : 144 -> 156
~ __ZNSt3__120__shared_ptr_emplaceIN2KB18CandidateFilter_thENS_9allocatorIS2_EEE16__on_zero_sharedEv : 36 -> 28
~ -[TIKeyboardInputManagerFavonius_th initImplementation] : 200 -> 208
~ -[TIKeyboardInputManagerFavonius_th trimmedInputStem] : 88 -> 96
~ -[TIKeyboardInputManagerFavonius_th trimmedInputStemForStem:] : 388 -> 400
~ -[TIKeyboardInputManagerFavonius_th addInput:withContext:] : 480 -> 520
~ -[TIWordSearchThai mecabraCreationOptionsDictionary] : 236 -> 252
~ -[TIKeyboardInputManager_th_24Key initialSelectedIndex] : 176 -> 188
~ -[TIKeyboardInputManager_th_24Key updateComposedText] : 316 -> 348
~ -[TIKeyboardInputManager_th_24Key candidateResultSet] : 528 -> 592
~ -[TIKeyboardInputManager_th_24Key processAcceptedCandidate:] : 196 -> 208
~ -[TIKeyboardInputManager_th_24Key keyLayoutMap] : 76 -> 88
~ -[TIKeyboardInputManager_th_24Key nearbyKeysForInput:isPopupVariant:] : 440 -> 452
~ -[TIKeyboardInputManager_th_24Key rawInputString] : 76 -> 84
~ -[TIKeyboardInputManager_th_24Key wordCharacters] : 276 -> 292
~ __ZNSt3__19remove_ifB8nn200100INS_11__wrap_iterIPN2KB9CandidateEEEU13block_pointerFbRKS3_EEET_SA_SA_T0_ -> __ZNSt3__19remove_ifB9fon210106INS_11__wrap_iterIPN2KB9CandidateEEEU13block_pointerFbRKS3_EEET_SA_SA_T0_ : 176 -> 188
~ __ZNSt3__16vectorIN2KB9CandidateENS_9allocatorIS2_EEE5eraseENS_11__wrap_iterIPKS2_EES9_ : 144 -> 172
~ __ZNK2KB18CandidateFilter_th31remove_low_word_score_candidateERNSt3__16vectorINS_9CandidateENS1_9allocatorIS3_EEEERKS3_P10__CFString : 172 -> 164
~ __ZNK2KB18CandidateFilter_th34remove_candidate_having_more_wordsERNSt3__16vectorINS_9CandidateENS1_9allocatorIS3_EEEERKS3_P10__CFString : 168 -> 160
~ __ZNSt3__119__shared_weak_count16__release_sharedB8nn200100Ev -> __ZNSt3__119__shared_weak_count16__release_sharedB9fon210106Ev : 108 -> 100
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE5clearB8nn200100Ev -> __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE5clearB9fon210106Ev : 80 -> 84
~ __ZNSt3__16__treeIN2KB6StringENS_4lessIS2_EENS_9allocatorIS2_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSC_SC_ : 88 -> 84
~ __ZNSt3__127__tree_balance_after_insertB8nn200100IPNS_16__tree_node_baseIPvEEEEvT_S5_ -> __ZNSt3__127__tree_balance_after_insertB9fon210106IPNS_16__tree_node_baseIPvEEEEvT_S5_ : 412 -> 456
~ -[TIKeyboardInputManager_th deleteFromInput:].cold.1 : 180 -> 184
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH5HugCZvc33nbL5eSOM4ar6I2psSKO0sKdTIsM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"

```
