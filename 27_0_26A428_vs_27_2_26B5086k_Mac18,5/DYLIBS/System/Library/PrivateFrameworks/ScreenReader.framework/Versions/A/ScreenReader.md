## ScreenReader

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/ScreenReader`

```diff

-1048.3.0.0.0
-  __TEXT.__text: 0x2c9018
-  __TEXT.__objc_methlist: 0x25ac8
+1050.3.0.0.0
+  __TEXT.__text: 0x2cba2c
+  __TEXT.__objc_methlist: 0x25c58
   __TEXT.__dlopen_cstrs: 0x6c9
   __TEXT.__const: 0x1470
   __TEXT.__swift5_typeref: 0x664

   __TEXT.__swift5_reflstr: 0x1d4
   __TEXT.__swift5_fieldmd: 0x258
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__cstring: 0x1e15c
-  __TEXT.__oslogstring: 0x1441
+  __TEXT.__cstring: 0x1e391
+  __TEXT.__oslogstring: 0x1475
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift_as_cont: 0xd0
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__gcc_except_tab: 0x3564
+  __TEXT.__gcc_except_tab: 0x354c
   __TEXT.__ustring: 0x48
   __TEXT.__dof_SCRMapEle: 0x47e
   __TEXT.__dof_SCRSpeech: 0x21a
-  __TEXT.__unwind_info: 0xb3c0
-  __TEXT.__eh_frame: 0x10a8
+  __TEXT.__unwind_info: 0xb450
+  __TEXT.__eh_frame: 0x10f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f80
+  __DATA_CONST.__const: 0x1fa0
   __DATA_CONST.__objc_classlist: 0xd18
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d18
+  __DATA_CONST.__objc_selrefs: 0x13e10
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x9a8
-  __DATA_CONST.__objc_arraydata: 0x8b0
-  __DATA_CONST.__got: 0x2130
-  __AUTH_CONST.__const: 0x49b8
-  __AUTH_CONST.__cfstring: 0x23640
-  __AUTH_CONST.__objc_const: 0x25358
-  __AUTH_CONST.__objc_arrayobj: 0x1c8
-  __AUTH_CONST.__objc_intobj: 0x1590
+  __DATA_CONST.__objc_arraydata: 0x8c8
+  __DATA_CONST.__got: 0x2140
+  __AUTH_CONST.__const: 0x4a08
+  __AUTH_CONST.__cfstring: 0x23700
+  __AUTH_CONST.__objc_const: 0x253e8
+  __AUTH_CONST.__objc_arrayobj: 0x1e0
+  __AUTH_CONST.__objc_intobj: 0x15d8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1f60
+  __AUTH_CONST.__auth_got: 0x1fd0
   __AUTH.__objc_data: 0x8650
   __AUTH.__data: 0x560
-  __DATA.__objc_ivar: 0x1a80
-  __DATA.__data: 0x2270
+  __DATA.__objc_ivar: 0x1a90
+  __DATA.__data: 0x2290
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13721
-  Symbols:   29183
-  CStrings:  5088
+  Functions: 13757
+  Symbols:   29255
+  CStrings:  5102
 
Symbols:
+ +[SCRBrailleManager _relativeIndexBasedRangeFor:textProvider:]
+ +[SCRBrailleManager _textLineRangeForTextAreaStartLineIndex:endLineIndex:currentLineIndex:]
+ +[SCRBrailleUtilities refreshSelectionOnCurrentBrailleTextLine]
+ -[SCRBrailleManager refreshSelectionOnCurrentTextLine]
+ -[SCRCell _rowSpeaksExpandedStatus]
+ -[SCRCell mouseHotSpot]
+ -[SCRCell traitsSortingDescendantDescription]
+ -[SCRElement axDescriptionOrTitle]
+ -[SCRElement hasAXDescriptionOrTitle]
+ -[SCRElement(SCRElementDescription) _processDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:perEntry:]
+ -[SCRElement(SCRElementDescription) _spokenStringValueForRawStringValue:role:traits:]
+ -[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:defaultCategory:]
+ -[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:updatingMutableVariants:]
+ -[SCRElement(SCRElementEventHandling) _speakCurrentSearchDispatchHandler:]
+ -[SCRElement(SCRElementInteraction) _applicationsBrowsableByRotor]
+ -[SCRElement(SCRElementInteraction) handleApplicationsMovement:request:]
+ -[SCRElement(SCRElementInteraction) handleBoundaryReachedWithEvent:request:forward:discardEscapeSpeech:]
+ -[SCRElement(SCRElementInteraction) isAtBoundaryInDirection:]
+ -[SCRElement(SCRElementInteraction) shouldAutoDrillOutAtBoundary]
+ -[SCRElementRotorManager pendingApplicationSelection]
+ -[SCRElementRotorManager setPendingApplicationSelection:]
+ -[SCRIncrementor _echoValueChangeFrom:toRequest:]
+ -[SCRIncrementor _echoesValueThroughTextFieldParent]
+ -[SCRList setFocusedChild:]
+ -[SCRMailCell traitsSortingDescendantDescription]
+ -[SCRPDFGroup _isTransparentWrapper]
+ -[SCRSearchManager speakCurrentSearchWithRequest:]
+ -[SCRTextArea _refreshSelectionOnCurrentBrailleTextLine]
+ -[SCRXcodeTextElement _addCodingAnnouncementsToRequest:forEchoedRange:]
+ -[SCRXcodeTextElement _announceLineNumberForLine:moveType:request:]
+ -[SCRXcodeTextElement _beginLineGranularityReadAtPosition:]
+ -[SCRXcodeTextElement _currentLineNumberForVOCursor]
+ -[SCRXcodeTextElement _endLineGranularityRead]
+ -[SCRXcodeTextElement echoCharacterAttributedString:variants:request:]
+ -[SCRXcodeTextElement echoDataInRange:request:showOnScreen:braille:]
+ -[SCRXcodeTextElement readNextLine:]
+ -[SCRXcodeTextElement readPreviousLine:]
+ GCC_except_table10366
+ GCC_except_table10370
+ GCC_except_table10374
+ GCC_except_table10515
+ GCC_except_table10520
+ GCC_except_table11144
+ GCC_except_table11167
+ GCC_except_table11453
+ GCC_except_table11457
+ GCC_except_table11559
+ GCC_except_table11781
+ GCC_except_table12013
+ GCC_except_table12060
+ GCC_except_table12129
+ GCC_except_table12131
+ GCC_except_table12257
+ GCC_except_table12334
+ GCC_except_table12423
+ GCC_except_table12427
+ GCC_except_table12428
+ GCC_except_table12435
+ GCC_except_table12648
+ GCC_except_table12737
+ GCC_except_table1655
+ GCC_except_table1842
+ GCC_except_table1881
+ GCC_except_table1915
+ GCC_except_table1919
+ GCC_except_table2033
+ GCC_except_table2174
+ GCC_except_table2190
+ GCC_except_table2252
+ GCC_except_table2360
+ GCC_except_table2364
+ GCC_except_table2583
+ GCC_except_table2600
+ GCC_except_table2657
+ GCC_except_table2861
+ GCC_except_table3118
+ GCC_except_table3120
+ GCC_except_table3196
+ GCC_except_table3272
+ GCC_except_table3402
+ GCC_except_table3406
+ GCC_except_table3486
+ GCC_except_table3589
+ GCC_except_table3667
+ GCC_except_table3690
+ GCC_except_table3809
+ GCC_except_table3899
+ GCC_except_table3902
+ GCC_except_table3925
+ GCC_except_table3930
+ GCC_except_table3944
+ GCC_except_table4048
+ GCC_except_table4092
+ GCC_except_table4494
+ GCC_except_table4503
+ GCC_except_table4506
+ GCC_except_table4631
+ GCC_except_table4669
+ GCC_except_table4673
+ GCC_except_table4677
+ GCC_except_table4679
+ GCC_except_table4683
+ GCC_except_table4687
+ GCC_except_table4757
+ GCC_except_table4771
+ GCC_except_table4816
+ GCC_except_table4820
+ GCC_except_table4846
+ GCC_except_table4852
+ GCC_except_table5684
+ GCC_except_table5720
+ GCC_except_table5823
+ GCC_except_table6093
+ GCC_except_table6099
+ GCC_except_table6268
+ GCC_except_table6318
+ GCC_except_table6354
+ GCC_except_table6449
+ GCC_except_table6636
+ GCC_except_table6722
+ GCC_except_table6737
+ GCC_except_table6747
+ GCC_except_table6767
+ GCC_except_table6773
+ GCC_except_table6777
+ GCC_except_table6886
+ GCC_except_table6889
+ GCC_except_table6894
+ GCC_except_table6920
+ GCC_except_table6927
+ GCC_except_table6958
+ GCC_except_table6961
+ GCC_except_table6995
+ GCC_except_table6996
+ GCC_except_table7114
+ GCC_except_table7120
+ GCC_except_table7141
+ GCC_except_table7142
+ GCC_except_table7209
+ GCC_except_table7235
+ GCC_except_table7237
+ GCC_except_table7351
+ GCC_except_table7389
+ GCC_except_table7391
+ GCC_except_table7393
+ GCC_except_table7408
+ GCC_except_table7409
+ GCC_except_table7422
+ GCC_except_table7436
+ GCC_except_table7437
+ GCC_except_table7515
+ GCC_except_table7522
+ GCC_except_table7523
+ GCC_except_table7666
+ GCC_except_table7958
+ GCC_except_table7980
+ GCC_except_table8156
+ GCC_except_table8245
+ GCC_except_table8251
+ GCC_except_table8252
+ GCC_except_table8253
+ GCC_except_table8254
+ GCC_except_table8258
+ GCC_except_table8259
+ GCC_except_table8380
+ GCC_except_table8391
+ GCC_except_table8395
+ GCC_except_table8423
+ GCC_except_table8527
+ GCC_except_table8672
+ GCC_except_table8678
+ GCC_except_table8773
+ GCC_except_table8847
+ GCC_except_table8929
+ GCC_except_table9003
+ GCC_except_table9004
+ GCC_except_table9021
+ GCC_except_table9031
+ GCC_except_table9041
+ GCC_except_table9042
+ GCC_except_table9049
+ GCC_except_table9052
+ GCC_except_table9053
+ GCC_except_table9207
+ GCC_except_table9537
+ GCC_except_table9581
+ GCC_except_table9586
+ GCC_except_table9920
+ GCC_except_table9924
+ GCC_except_table9929
+ OBJC_IVAR_$_SCRElementRotorManager._pendingApplicationSelection
+ OBJC_IVAR_$_SCRXcodeTextElement._isLineGranularityRead
+ OBJC_IVAR_$_SCRXcodeTextElement._lineGranularityReadPosition
+ OBJC_IVAR_$_SCRXcodeTextElement._lineGranularityReadStartLine
+ ___131-[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:defaultCategory:]_block_invoke
+ ___139-[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:updatingMutableVariants:]_block_invoke
+ ___66-[SCRElement(SCRElementInteraction) _applicationsBrowsableByRotor]_block_invoke
+ ___block_descriptor_32_e43_q24?0"SCRApplication"8"SCRApplication"16l
+ ___block_descriptor_48_e8_32s40s_e69_v48?0"NSAttributedString"8"NSString"16Q24"NSString"32"NSArray"40l
+ ___block_descriptor_64_e8_32s40s48s56s_e69_v48?0"NSAttributedString"8"NSString"16Q24"NSString"32"NSArray"40l
+ __kLSAuditTokenKey
+ _objc_msgSend$_addCodingAnnouncementsToRequest:forEchoedRange:
+ _objc_msgSend$_announceLineNumberForLine:moveType:request:
+ _objc_msgSend$_applicationsBrowsableByRotor
+ _objc_msgSend$_beginLineGranularityReadAtPosition:
+ _objc_msgSend$_currentLineNumberForVOCursor
+ _objc_msgSend$_echoValueChangeFrom:toRequest:
+ _objc_msgSend$_echoesValueThroughTextFieldParent
+ _objc_msgSend$_endLineGranularityRead
+ _objc_msgSend$_isTransparentWrapper
+ _objc_msgSend$_processDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:perEntry:
+ _objc_msgSend$_refreshSelectionOnCurrentBrailleTextLine
+ _objc_msgSend$_relativeIndexBasedRangeFor:textProvider:
+ _objc_msgSend$_rowSpeaksExpandedStatus
+ _objc_msgSend$_spokenStringValueForRawStringValue:role:traits:
+ _objc_msgSend$_textLineRangeForTextAreaStartLineIndex:endLineIndex:currentLineIndex:
+ _objc_msgSend$accessibilityLabelOrTitle
+ _objc_msgSend$axDescriptionOrTitle
+ _objc_msgSend$descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:defaultCategory:
+ _objc_msgSend$descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:updatingMutableVariants:
+ _objc_msgSend$elementToken
+ _objc_msgSend$handleApplicationsMovement:request:
+ _objc_msgSend$handleBoundaryReachedWithEvent:request:forward:discardEscapeSpeech:
+ _objc_msgSend$hasAXDescriptionOrTitle
+ _objc_msgSend$hasAccessibilityLabelOrTitle
+ _objc_msgSend$isAtBoundaryInDirection:
+ _objc_msgSend$isTextLine
+ _objc_msgSend$pendingApplicationSelection
+ _objc_msgSend$refreshSelectionOnCurrentBrailleTextLine
+ _objc_msgSend$refreshSelectionOnCurrentTextLine
+ _objc_msgSend$setPendingApplicationSelection:
+ _objc_msgSend$shouldAutoDrillOutAtBoundary
+ _objc_msgSend$speakCurrentSearchWithRequest:
+ _objc_msgSend$traitsSortingDescendantDescription
- -[SCRCell _identifiersExcludedFromDescendantDescription]
- -[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingIdentifiers:updatingMutableVariants:]
- -[SCRPDFContentList shouldAutoFocusOnChildren]
- GCC_except_table10340
- GCC_except_table10344
- GCC_except_table10348
- GCC_except_table10490
- GCC_except_table10495
- GCC_except_table11119
- GCC_except_table11142
- GCC_except_table11428
- GCC_except_table11432
- GCC_except_table11534
- GCC_except_table11756
- GCC_except_table11988
- GCC_except_table12035
- GCC_except_table12104
- GCC_except_table12106
- GCC_except_table12232
- GCC_except_table12309
- GCC_except_table12398
- GCC_except_table12402
- GCC_except_table12403
- GCC_except_table12410
- GCC_except_table12623
- GCC_except_table12703
- GCC_except_table1653
- GCC_except_table1840
- GCC_except_table1879
- GCC_except_table1913
- GCC_except_table1917
- GCC_except_table2031
- GCC_except_table2172
- GCC_except_table2176
- GCC_except_table2250
- GCC_except_table2358
- GCC_except_table2362
- GCC_except_table2581
- GCC_except_table2598
- GCC_except_table2655
- GCC_except_table2859
- GCC_except_table3114
- GCC_except_table3116
- GCC_except_table3192
- GCC_except_table3268
- GCC_except_table3392
- GCC_except_table3396
- GCC_except_table3476
- GCC_except_table3579
- GCC_except_table3657
- GCC_except_table3679
- GCC_except_table3793
- GCC_except_table3883
- GCC_except_table3886
- GCC_except_table3909
- GCC_except_table3914
- GCC_except_table3928
- GCC_except_table4029
- GCC_except_table4073
- GCC_except_table4473
- GCC_except_table4482
- GCC_except_table4485
- GCC_except_table4610
- GCC_except_table4648
- GCC_except_table4652
- GCC_except_table4656
- GCC_except_table4658
- GCC_except_table4662
- GCC_except_table4666
- GCC_except_table4736
- GCC_except_table4750
- GCC_except_table4795
- GCC_except_table4799
- GCC_except_table4825
- GCC_except_table4831
- GCC_except_table5305
- GCC_except_table5662
- GCC_except_table5698
- GCC_except_table5801
- GCC_except_table6071
- GCC_except_table6077
- GCC_except_table6246
- GCC_except_table6296
- GCC_except_table6332
- GCC_except_table6426
- GCC_except_table6613
- GCC_except_table6699
- GCC_except_table6714
- GCC_except_table6724
- GCC_except_table6744
- GCC_except_table6750
- GCC_except_table6754
- GCC_except_table6863
- GCC_except_table6866
- GCC_except_table6871
- GCC_except_table6897
- GCC_except_table6904
- GCC_except_table6935
- GCC_except_table6938
- GCC_except_table6972
- GCC_except_table6973
- GCC_except_table7091
- GCC_except_table7097
- GCC_except_table7118
- GCC_except_table7119
- GCC_except_table7186
- GCC_except_table7212
- GCC_except_table7214
- GCC_except_table7328
- GCC_except_table7366
- GCC_except_table7368
- GCC_except_table7370
- GCC_except_table7385
- GCC_except_table7386
- GCC_except_table7399
- GCC_except_table7413
- GCC_except_table7414
- GCC_except_table7492
- GCC_except_table7499
- GCC_except_table7500
- GCC_except_table7643
- GCC_except_table7935
- GCC_except_table7957
- GCC_except_table8133
- GCC_except_table8222
- GCC_except_table8228
- GCC_except_table8229
- GCC_except_table8230
- GCC_except_table8231
- GCC_except_table8235
- GCC_except_table8236
- GCC_except_table8357
- GCC_except_table8368
- GCC_except_table8372
- GCC_except_table8399
- GCC_except_table8503
- GCC_except_table8648
- GCC_except_table8654
- GCC_except_table8749
- GCC_except_table8823
- GCC_except_table8905
- GCC_except_table8979
- GCC_except_table8980
- GCC_except_table8997
- GCC_except_table9007
- GCC_except_table9017
- GCC_except_table9018
- GCC_except_table9025
- GCC_except_table9028
- GCC_except_table9029
- GCC_except_table9183
- GCC_except_table9513
- GCC_except_table9556
- GCC_except_table9561
- GCC_except_table9894
- GCC_except_table9898
- GCC_except_table9903
- ___60-[SCRList _moveInDirection:event:request:allowFullWrapping:]_block_invoke
- ___block_descriptor_40_e8_32r_e22_B16?0"AXFUIElement"8l
- _objc_msgSend$_identifiersExcludedFromDescendantDescription
- _objc_msgSend$accessibilityIndexOfChild:
- _objc_msgSend$descriptionFromDescendantEntriesIncludingCaption:excludingIdentifiers:updatingMutableVariants:
CStrings:
+ "Braille: dropped description value \"%@\"; text-line element %lu already holds its line"
+ "Global.findTextSpeakCurrentSearch"
+ "IEAskAboutImage"
+ "IEFetchAndSpeakDescription"
+ "No valid PID for application %@"
+ "ReadLine"
+ "ReadWord"
+ "SCRElementRotorTypeApplications"
+ "SCRWorkspace.rotor.applications"
+ "Warning: braille element %lu got a second value (\"%@\" after \"%@\"); a producer is emitting more than one consolidated action for one element. Appending both."
+ "[Error] Interval already ended"
+ "granularity=line"
+ "granularity=word"
+ "q24@?0@\"SCRApplication\"8@\"SCRApplication\"16"
+ "role"
+ "v48@?0@\"NSAttributedString\"8@\"NSString\"16Q24@\"NSString\"32@\"NSArray\"40"
- "!q"
- "identifier"
```
