## ScreenReader

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/ScreenReader`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_SCRMapEle`
- `__TEXT.__dof_SCRSpeech`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__DATA.__objc_ivar`

```diff

-1042.0.0.0.0
-  __TEXT.__text: 0x2d1a20
-  __TEXT.__objc_methlist: 0x257c8
+1045.0.0.0.0
+  __TEXT.__text: 0x2d4a4c
+  __TEXT.__objc_methlist: 0x25838
   __TEXT.__dlopen_cstrs: 0x6c9
-  __TEXT.__const: 0x13c0
-  __TEXT.__swift5_typeref: 0x5f4
-  __TEXT.__swift5_capture: 0x480
-  __TEXT.__constg_swiftt: 0x53c
-  __TEXT.__swift5_reflstr: 0x1a4
-  __TEXT.__swift5_fieldmd: 0x208
+  __TEXT.__const: 0x1450
+  __TEXT.__swift5_typeref: 0x650
+  __TEXT.__swift5_capture: 0x4c0
+  __TEXT.__constg_swiftt: 0x5d4
+  __TEXT.__swift5_reflstr: 0x1d4
+  __TEXT.__swift5_fieldmd: 0x258
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0x13e1
-  __TEXT.__cstring: 0x1dd07
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__swift_as_entry: 0x78
-  __TEXT.__swift_as_ret: 0x8c
-  __TEXT.__swift_as_cont: 0xc4
+  __TEXT.__cstring: 0x1dec5
+  __TEXT.__oslogstring: 0x1441
+  __TEXT.__swift5_types: 0x34
+  __TEXT.__swift_as_entry: 0x7c
+  __TEXT.__swift_as_ret: 0x90
+  __TEXT.__swift_as_cont: 0xd0
   __TEXT.__swift5_proto: 0x20
   __TEXT.__gcc_except_tab: 0x337c
   __TEXT.__ustring: 0x10a
   __TEXT.__dof_SCRMapEle: 0x47e
   __TEXT.__dof_SCRSpeech: 0x21a
-  __TEXT.__unwind_info: 0x8a30
-  __TEXT.__eh_frame: 0x1010
+  __TEXT.__unwind_info: 0x8a80
+  __TEXT.__eh_frame: 0x1098
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1fa0
+  __DATA_CONST.__const: 0x1f80
   __DATA_CONST.__objc_classlist: 0xd10
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13b60
+  __DATA_CONST.__objc_selrefs: 0x13bc0
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x9b0
+  __DATA_CONST.__objc_superrefs: 0x9a8
   __DATA_CONST.__objc_arraydata: 0x8b0
-  __DATA_CONST.__got: 0x20d8
-  __AUTH_CONST.__const: 0x4858
-  __AUTH_CONST.__cfstring: 0x23360
-  __AUTH_CONST.__objc_const: 0x25158
+  __DATA_CONST.__got: 0x2110
+  __AUTH_CONST.__const: 0x4948
+  __AUTH_CONST.__cfstring: 0x23480
+  __AUTH_CONST.__objc_const: 0x25130
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_intobj: 0x1590
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1f20
-  __AUTH.__objc_data: 0x8588
-  __AUTH.__data: 0x538
+  __AUTH_CONST.__auth_got: 0x1f48
+  __AUTH.__objc_data: 0x8600
+  __AUTH.__data: 0x560
   __DATA.__objc_ivar: 0x1a58
-  __DATA.__data: 0x2220
+  __DATA.__data: 0x2268
   __DATA.__bss: 0x12f8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13617
-  Symbols:   29052
-  CStrings:  5057
+  Functions: 13657
+  Symbols:   29073
+  CStrings:  5071
 
Symbols:
+ +[SCRXcodeTextElement _allDiagnosticAttributeKeys]
+ +[SCRXcodeTextElement diagnosticKeysToAnnounceForCurrentLine:currentDiagnostics:previousLine:previousDiagnostics:]
+ +[SCRXcodeTextElement shouldSpeakTextWhenAnnotationPresent:preference:]
+ -[SCRBrailleManager hasSharedSurfaceCanvasDisplay]
+ -[SCRBrailleManager setHasSharedSurfaceCanvasDisplay:]
+ -[SCRElement(SCRElementEventHandling) _handleImageExplorerSaveDescriptionDispatchHandler:]
+ -[SCRElementRotorManager advanceRotorInDirection:onlyVisible:includeActionsRotor:request:showVisuals:autoHideVisuals:onDisplay:]
+ -[SCRSystemUIServerApplication isScreenPeripheral]
+ -[SCRVisualsRotorWindow moveWindowCenter:]
+ -[SCRXcodeTextElement _consumePendingMoveType]
+ -[SCRXcodeTextElement _findLandingLineToAnnounce]
+ -[SCRXcodeTextElement _findMatchPresentOnLine:]
+ -[SCRXcodeTextElement _isFindNextEchoEvent:]
+ -[SCRXcodeTextElement _setPendingMoveType:]
+ -[SCRXcodeTextElement _shouldAnnounceLineNumberForLine:verbosity:moveType:]
+ -[SCRXcodeTextElement findMatchAnnouncement]
+ -[SCRXcodeTextElement keyboardHandler:request:]
+ -[_SCRTextLineNavigator currentLineRangeRelativeToProvider]
+ -[_SCRTextLineNavigator selectionRangeInCurrentLine]
+ GCC_except_table10293
+ GCC_except_table10297
+ GCC_except_table10301
+ GCC_except_table10442
+ GCC_except_table10447
+ GCC_except_table11070
+ GCC_except_table11093
+ GCC_except_table11378
+ GCC_except_table11382
+ GCC_except_table11484
+ GCC_except_table1156
+ GCC_except_table116
+ GCC_except_table1169
+ GCC_except_table11706
+ GCC_except_table11937
+ GCC_except_table11984
+ GCC_except_table1203
+ GCC_except_table12053
+ GCC_except_table12055
+ GCC_except_table1211
+ GCC_except_table12181
+ GCC_except_table12258
+ GCC_except_table12347
+ GCC_except_table12351
+ GCC_except_table12359
+ GCC_except_table1247
+ GCC_except_table1254
+ GCC_except_table12572
+ GCC_except_table1468
+ GCC_except_table1646
+ GCC_except_table1833
+ GCC_except_table1872
+ GCC_except_table1906
+ GCC_except_table1910
+ GCC_except_table2024
+ GCC_except_table2165
+ GCC_except_table2169
+ GCC_except_table2171
+ GCC_except_table2173
+ GCC_except_table2175
+ GCC_except_table2177
+ GCC_except_table2179
+ GCC_except_table2181
+ GCC_except_table2243
+ GCC_except_table2351
+ GCC_except_table2355
+ GCC_except_table2574
+ GCC_except_table2591
+ GCC_except_table2648
+ GCC_except_table2852
+ GCC_except_table3107
+ GCC_except_table3109
+ GCC_except_table3185
+ GCC_except_table3261
+ GCC_except_table3460
+ GCC_except_table3506
+ GCC_except_table3565
+ GCC_except_table3643
+ GCC_except_table3665
+ GCC_except_table3778
+ GCC_except_table3863
+ GCC_except_table3866
+ GCC_except_table3890
+ GCC_except_table3895
+ GCC_except_table3909
+ GCC_except_table4010
+ GCC_except_table4054
+ GCC_except_table4454
+ GCC_except_table4463
+ GCC_except_table4466
+ GCC_except_table4591
+ GCC_except_table4633
+ GCC_except_table4637
+ GCC_except_table4643
+ GCC_except_table4647
+ GCC_except_table4717
+ GCC_except_table4731
+ GCC_except_table4776
+ GCC_except_table4780
+ GCC_except_table4806
+ GCC_except_table4812
+ GCC_except_table5266
+ GCC_except_table5623
+ GCC_except_table5659
+ GCC_except_table5762
+ GCC_except_table6032
+ GCC_except_table6038
+ GCC_except_table6207
+ GCC_except_table6257
+ GCC_except_table6293
+ GCC_except_table6387
+ GCC_except_table6574
+ GCC_except_table6660
+ GCC_except_table6675
+ GCC_except_table6685
+ GCC_except_table6705
+ GCC_except_table6711
+ GCC_except_table6715
+ GCC_except_table6824
+ GCC_except_table6827
+ GCC_except_table6832
+ GCC_except_table6865
+ GCC_except_table6896
+ GCC_except_table6899
+ GCC_except_table6933
+ GCC_except_table6934
+ GCC_except_table7052
+ GCC_except_table7058
+ GCC_except_table7079
+ GCC_except_table7080
+ GCC_except_table7147
+ GCC_except_table7173
+ GCC_except_table7175
+ GCC_except_table725
+ GCC_except_table7289
+ GCC_except_table7327
+ GCC_except_table7329
+ GCC_except_table7331
+ GCC_except_table7346
+ GCC_except_table7347
+ GCC_except_table7360
+ GCC_except_table7374
+ GCC_except_table7375
+ GCC_except_table7460
+ GCC_except_table7461
+ GCC_except_table7604
+ GCC_except_table786
+ GCC_except_table7896
+ GCC_except_table7918
+ GCC_except_table8094
+ GCC_except_table8191
+ GCC_except_table8192
+ GCC_except_table8196
+ GCC_except_table8197
+ GCC_except_table8318
+ GCC_except_table8329
+ GCC_except_table8333
+ GCC_except_table8360
+ GCC_except_table8464
+ GCC_except_table8609
+ GCC_except_table8615
+ GCC_except_table8710
+ GCC_except_table8784
+ GCC_except_table8866
+ GCC_except_table8940
+ GCC_except_table8941
+ GCC_except_table8958
+ GCC_except_table8968
+ GCC_except_table8978
+ GCC_except_table8986
+ GCC_except_table8989
+ GCC_except_table8990
+ GCC_except_table9138
+ GCC_except_table9468
+ GCC_except_table9509
+ GCC_except_table9514
+ GCC_except_table9847
+ GCC_except_table9851
+ GCC_except_table9856
+ OBJC_IVAR_$_SCRBrailleManager._hasSharedSurfaceCanvasDisplay
+ OBJC_IVAR_$_SCRXcodeTextElement._lastDiagnosticKeys
+ OBJC_IVAR_$_SCRXcodeTextElement._lastDiagnosticLine
+ OBJC_IVAR_$_SCRXcodeTextElement._pendingMoveType
+ OBJC_IVAR_$_SCRXcodeTextElement._pendingMoveTypeCreationTime
+ _CGDisplayIsActive
+ _OBJC_CLASS_$_AXVScreenCaptureManager
+ _OBJC_CLASS_$_NSCache
+ _OBJC_METACLASS_$__TtCC12ScreenReader23SCRImageExplorerServiceP33_84FC609A0A0D832164FA0CD27967EA578CacheKey
+ _SCRDisplayIDForRotorGesture
+ __94-[SCRElement(SCRElementInteraction) _addActionsToGuide:forCategory:includeElementDescription:]_block_invoke
+ __DATA__TtCC12ScreenReader23SCRImageExplorerServiceP33_84FC609A0A0D832164FA0CD27967EA578CacheKey
+ __INSTANCE_METHODS__TtCC12ScreenReader23SCRImageExplorerServiceP33_84FC609A0A0D832164FA0CD27967EA578CacheKey
+ __IVARS__TtCC12ScreenReader23SCRImageExplorerServiceP33_84FC609A0A0D832164FA0CD27967EA578CacheKey
+ __METACLASS_DATA__TtCC12ScreenReader23SCRImageExplorerServiceP33_84FC609A0A0D832164FA0CD27967EA578CacheKey
+ __PROPERTIES__TtCC12ScreenReader23SCRImageExplorerServiceP33_84FC609A0A0D832164FA0CD27967EA578CacheKey
+ ___128-[SCRElementRotorManager advanceRotorInDirection:onlyVisible:includeActionsRotor:request:showVisuals:autoHideVisuals:onDisplay:]_block_invoke
+ ___50+[SCRXcodeTextElement _allDiagnosticAttributeKeys]_block_invoke
+ ___70-[SCRElement(SCRElementInteraction) _addAudiographGuideItemsForGuide:]_block_invoke_3
+ ___70-[SCRElement(SCRElementInteraction) _addAudiographGuideItemsForGuide:]_block_invoke_4
+ ___swift_memcpy9_8
+ __isAuthorizedToQuit
+ __sLastFindAnnouncedLine
+ __sLastFindAnnouncedTime
+ __swift_closure_destructor.17Tm
+ _allDiagnosticAttributeKeys.keys
+ _allDiagnosticAttributeKeys.onceToken
+ _kSCRCUserDefaultsCodingProgramCounterSound
+ _kSCROutputSoundLineProgramCounter
+ _objc_msgSend$_allDiagnosticAttributeKeys
+ _objc_msgSend$_consumePendingMoveType
+ _objc_msgSend$_findLandingLineToAnnounce
+ _objc_msgSend$_findMatchPresentOnLine:
+ _objc_msgSend$_isFindNextEchoEvent:
+ _objc_msgSend$_setPendingMoveType:
+ _objc_msgSend$_shouldAnnounceLineNumberForLine:verbosity:moveType:
+ _objc_msgSend$advanceRotorInDirection:onlyVisible:includeActionsRotor:request:showVisuals:autoHideVisuals:onDisplay:
+ _objc_msgSend$currentLineRangeRelativeToProvider
+ _objc_msgSend$diagnosticKeysToAnnounceForCurrentLine:currentDiagnostics:previousLine:previousDiagnostics:
+ _objc_msgSend$findMatchAnnouncement
+ _objc_msgSend$generativeModelsAvailable
+ _objc_msgSend$hasSharedSurfaceCanvasDisplay
+ _objc_msgSend$isIndexBased
+ _objc_msgSend$isPhotoLibraryAsset:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$moveWindowCenter:
+ _objc_msgSend$saveImageDescriptionWithElement:
+ _objc_msgSend$screenShotMainScreenWithRect:
+ _objc_msgSend$selectionRangeInCurrentLine
+ _objc_msgSend$setCountLimit:
+ _objc_msgSend$setFrameCenter:
+ _objc_msgSend$setHasSharedSurfaceCanvasDisplay:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$shouldSpeakTextWhenAnnotationPresent:preference:
+ _swift_deallocPartialClassInstance
+ _symbolic Sd
+ _symbolic So7NSCacheCy_____So8NSStringCG 12ScreenReader23SCRImageExplorerServiceC8CacheKey010_84FC609A0I21D832164FA0CD27967EA57LLC
+ _symbolic _____ 12ScreenReader23SCRImageExplorerServiceC28GenerativeModelsAvailability010_84FC609A0J21D832164FA0CD27967EA57LLV
+ _symbolic _____ 12ScreenReader23SCRImageExplorerServiceC8CacheKey010_84FC609A0I21D832164FA0CD27967EA57LLC
+ _symbolic _____ So14AXUIElementRefa
+ _symbolic _____Sg 12ScreenReader23SCRImageExplorerServiceC8CacheKey010_84FC609A0I21D832164FA0CD27967EA57LLC
+ _symbolic _____Sg_ABt 10Foundation3URLV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 12ScreenReader23SCRImageExplorerServiceC28GenerativeModelsAvailability010_84FC609A0L21D832164FA0CD27967EA57LLV So16os_unfair_lock_sV
+ _type_layout_string 12ScreenReader23SCRImageExplorerServiceC28GenerativeModelsAvailability010_84FC609A0J21D832164FA0CD27967EA57LLV
- +[SCRXcodeDiagnostic allAttributeKeys]
- +[SCRXcodeDiagnostic allDiagnostics]
- -[SCRMenuItem addItemDescriptionForBrailleToRequest:]
- -[SCRTextElement(Terminal) _terminalMoveToFirstWithEvent:request:visibleOnly:]
- -[SCRTextElement(Terminal) _terminalMoveToLastWithEvent:request:visibleOnly:]
- -[SCRXcodeDiagnostic .cxx_destruct]
- -[SCRXcodeDiagnostic attributeKey]
- -[SCRXcodeDiagnostic initWithAttributeKey:soundIdentifier:stateKey:preferenceProvider:]
- -[SCRXcodeDiagnostic preferenceProvider]
- -[SCRXcodeDiagnostic soundIdentifier]
- -[SCRXcodeDiagnostic stateKey]
- -[SCRXcodeTextElement _changedDiagnosticsForLine:]
- -[SCRXcodeTextElement _lastAnnouncedLineForDiagnostic:]
- -[SCRXcodeTextElement _resetAnnouncedDiagnosticLines]
- -[SCRXcodeTextElement _setLastAnnouncedLine:forDiagnostic:]
- -[SCRXcodeTextElement _shouldAnnounceLineNumberForLine:verbosity:]
- GCC_except_table10287
- GCC_except_table10291
- GCC_except_table10295
- GCC_except_table10436
- GCC_except_table10441
- GCC_except_table11064
- GCC_except_table11086
- GCC_except_table11371
- GCC_except_table11375
- GCC_except_table114
- GCC_except_table11477
- GCC_except_table1154
- GCC_except_table1167
- GCC_except_table11699
- GCC_except_table11930
- GCC_except_table11977
- GCC_except_table1200
- GCC_except_table12046
- GCC_except_table12048
- GCC_except_table1208
- GCC_except_table12174
- GCC_except_table12251
- GCC_except_table12340
- GCC_except_table12344
- GCC_except_table12345
- GCC_except_table1244
- GCC_except_table1248
- GCC_except_table12579
- GCC_except_table1465
- GCC_except_table1643
- GCC_except_table1830
- GCC_except_table1869
- GCC_except_table1903
- GCC_except_table1907
- GCC_except_table2021
- GCC_except_table2162
- GCC_except_table2166
- GCC_except_table2168
- GCC_except_table2170
- GCC_except_table2172
- GCC_except_table2174
- GCC_except_table2176
- GCC_except_table2178
- GCC_except_table2240
- GCC_except_table2348
- GCC_except_table2352
- GCC_except_table2571
- GCC_except_table2588
- GCC_except_table2645
- GCC_except_table2849
- GCC_except_table3104
- GCC_except_table3106
- GCC_except_table3182
- GCC_except_table3258
- GCC_except_table3457
- GCC_except_table3502
- GCC_except_table3561
- GCC_except_table3637
- GCC_except_table3659
- GCC_except_table3772
- GCC_except_table3857
- GCC_except_table3860
- GCC_except_table3883
- GCC_except_table3888
- GCC_except_table3902
- GCC_except_table4003
- GCC_except_table4047
- GCC_except_table4446
- GCC_except_table4455
- GCC_except_table4458
- GCC_except_table4583
- GCC_except_table4621
- GCC_except_table4625
- GCC_except_table4631
- GCC_except_table4635
- GCC_except_table4709
- GCC_except_table4723
- GCC_except_table4768
- GCC_except_table4772
- GCC_except_table4798
- GCC_except_table4804
- GCC_except_table5258
- GCC_except_table5615
- GCC_except_table5651
- GCC_except_table5754
- GCC_except_table6025
- GCC_except_table6031
- GCC_except_table6200
- GCC_except_table6250
- GCC_except_table6286
- GCC_except_table6380
- GCC_except_table6567
- GCC_except_table6653
- GCC_except_table6668
- GCC_except_table6678
- GCC_except_table6698
- GCC_except_table6704
- GCC_except_table6708
- GCC_except_table6817
- GCC_except_table6820
- GCC_except_table6825
- GCC_except_table6851
- GCC_except_table6889
- GCC_except_table6892
- GCC_except_table6926
- GCC_except_table6927
- GCC_except_table7045
- GCC_except_table7051
- GCC_except_table7072
- GCC_except_table7073
- GCC_except_table7140
- GCC_except_table7166
- GCC_except_table7168
- GCC_except_table723
- GCC_except_table7282
- GCC_except_table7320
- GCC_except_table7322
- GCC_except_table7324
- GCC_except_table7339
- GCC_except_table7340
- GCC_except_table7353
- GCC_except_table7367
- GCC_except_table7368
- GCC_except_table7446
- GCC_except_table7454
- GCC_except_table7597
- GCC_except_table784
- GCC_except_table7889
- GCC_except_table7911
- GCC_except_table8087
- GCC_except_table8176
- GCC_except_table8182
- GCC_except_table8184
- GCC_except_table8185
- GCC_except_table8311
- GCC_except_table8322
- GCC_except_table8326
- GCC_except_table8353
- GCC_except_table8457
- GCC_except_table8602
- GCC_except_table8608
- GCC_except_table8703
- GCC_except_table8777
- GCC_except_table8859
- GCC_except_table8933
- GCC_except_table8934
- GCC_except_table8951
- GCC_except_table8961
- GCC_except_table8971
- GCC_except_table8972
- GCC_except_table8982
- GCC_except_table8983
- GCC_except_table9130
- GCC_except_table9460
- GCC_except_table9501
- GCC_except_table9506
- GCC_except_table9839
- GCC_except_table9843
- GCC_except_table9848
- OBJC_IVAR_$_SCRXcodeDiagnostic._attributeKey
- OBJC_IVAR_$_SCRXcodeDiagnostic._preferenceProvider
- OBJC_IVAR_$_SCRXcodeDiagnostic._soundIdentifier
- OBJC_IVAR_$_SCRXcodeDiagnostic._stateKey
- OBJC_IVAR_$_SCRXcodeTextElement._lastAnnouncedLineByDiagnostic
- _CGSHWCaptureDesktop
- _OBJC_CLASS_$_SCRXcodeDiagnostic
- _OBJC_METACLASS_$_SCRXcodeDiagnostic
- __70-[SCRElement(SCRElementInteraction) _addAudiographGuideItemsForGuide:]_block_invoke
- __70-[SCRElement(SCRElementInteraction) _addAudiographGuideItemsForGuide:]_block_invoke_2
- __OBJC_$_CLASS_METHODS_SCRXcodeDiagnostic
- __OBJC_$_INSTANCE_METHODS_SCRXcodeDiagnostic
- __OBJC_$_INSTANCE_VARIABLES_SCRXcodeDiagnostic
- __OBJC_$_PROP_LIST_SCRXcodeDiagnostic
- __OBJC_CLASS_RO_$_SCRXcodeDiagnostic
- __OBJC_METACLASS_RO_$_SCRXcodeDiagnostic
- ___118-[SCRElementRotorManager advanceRotorInDirection:onlyVisible:includeActionsRotor:request:showVisuals:autoHideVisuals:]_block_invoke
- ___36+[SCRXcodeDiagnostic allDiagnostics]_block_invoke
- ___36+[SCRXcodeDiagnostic allDiagnostics]_block_invoke_2
- ___36+[SCRXcodeDiagnostic allDiagnostics]_block_invoke_3
- ___36+[SCRXcodeDiagnostic allDiagnostics]_block_invoke_4
- ___36+[SCRXcodeDiagnostic allDiagnostics]_block_invoke_5
- ___38+[SCRXcodeDiagnostic allAttributeKeys]_block_invoke
- ___block_descriptor_32_e26_q16?0"SCRCUserDefaults"8l
- __swift_closure_destructor.12Tm
- __swift_closure_destructor.23Tm
- _kSCRCUserDefaultsCodingDebugInstructionPointerSound
- _kSCROutputSoundLineDebugLine
- _objc_msgSend$_changedDiagnosticsForLine:
- _objc_msgSend$_lastAnnouncedLineForDiagnostic:
- _objc_msgSend$_resetAnnouncedDiagnosticLines
- _objc_msgSend$_setLastAnnouncedLine:forDiagnostic:
- _objc_msgSend$_shouldAnnounceLineNumberForLine:verbosity:
- _objc_msgSend$_terminalMoveToFirstWithEvent:request:visibleOnly:
- _objc_msgSend$_terminalMoveToLastWithEvent:request:visibleOnly:
- _objc_msgSend$allAttributeKeys
- _objc_msgSend$allDiagnostics
- _objc_msgSend$attributeKey
- _objc_msgSend$initWithAttributeKey:soundIdentifier:stateKey:preferenceProvider:
- _objc_msgSend$preferenceProvider
- _objc_msgSend$soundIdentifier
- _objc_msgSend$stateKey
- allAttributeKeys.keys
- allAttributeKeys.onceToken
- allDiagnostics.diagnostics
- allDiagnostics.onceToken
CStrings:
+ "AXMarkedFindMatch"
+ "Announced after the focused photo's cached description is written into its metadata"
+ "Global.askAboutImage"
+ "Global.askAboutScreen"
+ "Global.imageDescription"
+ "Global.imageDescription.intelligent.title"
+ "Global.screenExplorer"
+ "Image description saved"
+ "SCROutputSoundLineProgramCounter"
+ "Save Intelligent Image Description"
+ "ScreenReader.CacheKey"
+ "[SCR]: Empty image description."
+ "[SCR]: Empty saved image description."
+ "[SCR]: Failed to fetch image description. %@"
+ "[SCR]: Failed to save image description. %@"
+ "codingDiagnosticBreakpoint"
+ "codingDiagnosticError"
+ "codingDiagnosticProgramCounter"
+ "codingDiagnosticWarning"
+ "codingFindMatchLineAndText"
+ "kSCRImageExplorerSaveDescriptionGuideTag"
- "SCROutputSoundLineDebugLine"
- "[SCR]: %s image description."
- "[SCR]: Failed to request image description. %@"
- "breakpoint"
- "error"
- "programCounter"
- "q16@?0@\"SCRCUserDefaults\"8"
```
