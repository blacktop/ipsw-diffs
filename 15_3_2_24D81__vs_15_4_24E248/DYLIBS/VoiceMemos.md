## VoiceMemos

> `/System/iOSSupport/System/Library/PrivateFrameworks/VoiceMemos.framework/Versions/A/VoiceMemos`

```diff

-1252.0.0.0.0
-  __TEXT.__text: 0x45714
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x3590
-  __TEXT.__gcc_except_tab: 0x19bc
-  __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x5fc8
-  __TEXT.__oslogstring: 0x279e
+1272.0.0.0.0
+  __TEXT.__text: 0x45b4c
+  __TEXT.__auth_stubs: 0xc10
+  __TEXT.__objc_methlist: 0x3a44
+  __TEXT.__gcc_except_tab: 0x19fc
+  __TEXT.__const: 0x1f0
+  __TEXT.__cstring: 0x5ecd
+  __TEXT.__oslogstring: 0x27d4
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1840
+  __TEXT.__unwind_info: 0x1910
   __TEXT.__objc_classname: 0x7ee
-  __TEXT.__objc_methname: 0xb027
-  __TEXT.__objc_methtype: 0x151a
-  __TEXT.__objc_stubs: 0x8600
+  __TEXT.__objc_methname: 0xb023
+  __TEXT.__objc_methtype: 0x14f7
+  __TEXT.__objc_stubs: 0x8620
   __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x1d48
+  __DATA_CONST.__const: 0x1d50
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ab8
+  __DATA_CONST.__objc_selrefs: 0x2b58
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__cfstring: 0x3160
-  __AUTH_CONST.__objc_const: 0x5f40
+  __AUTH_CONST.__objc_const: 0x56e0
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0xc0

   - /System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AppAnalytics.framework/Versions/A/AppAnalytics
   - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D602338-A7BE-37C7-AAC9-D341925AD649
-  Functions: 1760
-  Symbols:   4512
-  CStrings:  3271
+  UUID: 83AF2E3B-9BD0-336F-A804-D526230A383F
+  Functions: 1810
+  Symbols:   4574
+  CStrings:  3272
 
Symbols:
+ +[RCAppGroupStorage sharedInstance].cold.1
+ +[RCBuiltinRecordingsFolder allBuiltInFolders].cold.1
+ +[RCCaptureFormat AVFileTypeForFileExtension:]
+ +[RCCaptureFormat supportedFileTypes]
+ +[RCDevice timeDisplayUpdateFrameInterval].cold.1
+ +[RCDurationFormatter sharedFormatter].cold.1
+ +[RCMutableMovie movieWithURL:error:].cold.1
+ +[RCQueryManager _defaultFolderFetchRequest].cold.1
+ +[RCQueryManager defaultFetchedProperties].cold.1
+ +[RCQueryManager defaultResidentRecordingsFetchedProperties].cold.1
+ +[RCQueryManager defaultSortDescriptors].cold.1
+ +[RCSSavedRecordingService sharedService].cold.1
+ +[RCSSavedRecordingServiceConnection clientInterface].cold.1
+ +[RCSSavedRecordingServiceConnection serviceInterface].cold.1
+ +[RCSavedRecordingsModel _copyFileIntoRecordingsDirectory:error:]
+ +[RCSavedRecordingsModel _copyFileIntoRecordingsDirectory:error:].cold.1
+ -[RCCaptureInputWaveformDataSource _updateCapturedComposition:].cold.1
+ -[RCCaptureInputWaveformDataSource undoCapture].cold.1
+ -[RCCloudRecording markRecordingAsExported:error:].cold.1
+ -[RCCloudRecording synchronizeRecordingMetadata].cold.1
+ -[RCCloudRecording userFolder]
+ -[RCComposition _loadMusicMemoMetadata].cold.1
+ -[RCCompositionFragment initWithAVOutputURL:contentDuration:timeRangeInContentToUse:timeRangeInComposition:trackIndex:].cold.1
+ -[RCCompositionFragment initWithAVOutputURL:contentDuration:timeRangeInContentToUse:timeRangeInComposition:trackIndex:].cold.2
+ -[RCDurationFormatter stringFromDuration:replacingDigitsWithDigit:style:].cold.1
+ -[RCFileInputWaveformDataSource initWithAVFileURL:savesGeneratedWaveform:segmentFlushInterval:trackIndex:].cold.1
+ -[RCSavedRecording willSave].cold.1
+ -[RCSavedRecording willSave].cold.2
+ -[RCSavedRecordingsModel deleteFolder:].cold.1
+ -[RCSavedRecordingsModel deleteFolder:].cold.2
+ -[RCSavedRecordingsModel deleteRecording:].cold.1
+ -[RCSavedRecordingsModel duplicateRecording:copyingResources:creationDate:error:].cold.1
+ -[RCSavedRecordingsModel eraseRecording:].cold.1
+ -[RCSavedRecordingsModel insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:error:]
+ -[RCSavedRecordingsModel playableRecordingsForFolder:]
+ -[RCSavedRecordingsModel restoreDeletedRecording:].cold.1
+ -[RCWaveformDataSource updateAccumulatorWaveformSegmentsWithBlock:].cold.1
+ GCC_except_table56
+ GCC_except_table70
+ GCC_except_table84
+ GCC_except_table89
+ GCC_except_table91
+ OSLogForCategory.cold.1
+ RCCloudRecordingsStoreURL.cold.1
+ RCDisplayStringForString.cold.1
+ RCIsInternalInstall.cold.1
+ RCLocalizedInteger.cold.1
+ RCLocalizedInteger.cold.2
+ RCOverdubRecordingFeatureFlagIsEnabled.cold.1
+ RCOverdubRecordingIsEnabled.cold.1
+ RCRecordingsDirectoryURL.cold.1
+ RCRunningInSavedRecordingDaemon.cold.1
+ RCSaveAsNewFeatureFlagIsEnabled.cold.1
+ RCStereoRecordingIsAvailable.cold.1
+ RCTestAlwaysShowLockScreenPlugin.cold.1
+ RCTestAutoSelectedRecordingIndex.cold.1
+ RCTestBeginPreviewDelay.cold.1
+ RCTestDebugAutolayout_Logging.cold.1
+ RCTestDebugAutolayout_Show.cold.1
+ RCTestResetNavigationStateThresholdSeconds.cold.1
+ RCTestResetSyncs.cold.1
+ RCTestResetSyncsAlwaysResetSync.cold.1
+ RCTestSlowMessageExportSeconds.cold.1
+ RCTestSlowMessageServiceSleepAmount.cold.1
+ RCTranscribeAllAudioTracks.cold.1
+ RCTranscriptionFeatureFlagIsEnabled.cold.1
+ RCUseDevelopmentContainer.cold.1
+ VMAudioWriteDelay.cold.1
+ __105-[RCWaveformGenerator async_finishLoadingByTerminating:loadingFinishedBlockTimeout:loadingFinishedBlock:]_block_invoke.21
+ __47-[RCCompositionWaveformDataSource startLoading]_block_invoke_3.cold.1
+ __80-[RCWaveformGenerator _appendPowerMeterValuesFromDataInAudioFile:progressBlock:]_block_invoke.40
+ __RCOverdubRecordingIsEnabled_block_invoke.cold.1
+ __ZL26_assertInvalidStateMessageP8NSString24RCWaveformGeneratorStateP13objc_selector
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___100-[RCSavedRecordingsModel insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:error:]_block_invoke
+ ___37+[RCCaptureFormat supportedFileTypes]_block_invoke
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r88r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8r88l8
+ __block_literal_global.115
+ __block_literal_global.118
+ __block_literal_global.121
+ __block_literal_global.126
+ __block_literal_global.169
+ __block_literal_global.183
+ __block_literal_global.188
+ __block_literal_global.192
+ __block_literal_global.195
+ __block_literal_global.198
+ __block_literal_global.207
+ __block_literal_global.210
+ __block_literal_global.221
+ __block_literal_global.295
+ __block_literal_global.87
+ __block_literal_global.95
+ _accessActiveCaptureCompositionAVURLs.cold.1
+ _kVMLogCategoryPointsOfInterest
+ _objc_msgSend$AVFileTypeForFileExtension:
+ _objc_msgSend$_copyFileIntoRecordingsDirectory:error:
+ _objc_msgSend$canContainFragments
+ _objc_msgSend$insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:error:
+ computeAudioDigest.cold.1
+ computeAudioDigest.cold.2
+ isAudioFilePurgeable.cold.1
- +[RCSavedRecordingsModel _copyFileIntoRecordingsDirectory:]
- +[RCSavedRecordingsModel _copyFileIntoRecordingsDirectory:].cold.1
- -[RCSavedRecordingsModel insertRecordingWithAudioFile:duration:date:]
- -[RCSavedRecordingsModel insertRecordingWithAudioFile:duration:date:customLabelBase:]
- -[RCSavedRecordingsModel insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:]
- -[RCSavedRecordingsModel nextRecordingDefaultLabelWithCustomLabelBase:]
- GCC_except_table63
- GCC_except_table71
- GCC_except_table90
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- __105-[RCWaveformGenerator async_finishLoadingByTerminating:loadingFinishedBlockTimeout:loadingFinishedBlock:]_block_invoke.23
- __80-[RCWaveformGenerator _appendPowerMeterValuesFromDataInAudioFile:progressBlock:]_block_invoke.42
- __ZL26_assertInvalidStateMessageP8NSStringlP13objc_selector
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___94-[RCSavedRecordingsModel insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:]_block_invoke
- ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
- __block_literal_global.111
- __block_literal_global.114
- __block_literal_global.117
- __block_literal_global.122
- __block_literal_global.171
- __block_literal_global.190
- __block_literal_global.194
- __block_literal_global.197
- __block_literal_global.200
- __block_literal_global.209
- __block_literal_global.214
- __block_literal_global.223
- __block_literal_global.296
- __block_literal_global.81
- __block_literal_global.91
- _fmod
- _objc_msgSend$_copyFileIntoRecordingsDirectory:
- _objc_msgSend$insertRecordingWithAudioFile:duration:date:customLabelBase:
- _objc_msgSend$insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:
CStrings:
+ "%s -- Attempted to write metadata before finalization"
+ "+[RCMutableMovie movieWithURL:error:]"
+ "+[RCSavedRecordingsModel _copyFileIntoRecordingsDirectory:error:]"
+ "@64@0:8@16d24@32@40@48^@56"
+ "AVFileTypeForFileExtension:"
+ "Attempted to write metadata before finalization"
+ "BOOL _checkCanAppend(RCWaveformGenerator * _Nonnull __strong, SEL _Nonnull)"
+ "PointsOfInterest"
+ "RCWaveformGenerator.mm"
+ "RCWaveformSegment.mm"
+ "T@\"RCRecordingsFolder\",R,N"
+ "_copyFileIntoRecordingsDirectory:error:"
+ "canContainFragments"
+ "insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:error:"
+ "playableRecordingsForFolder:"
+ "supportedFileTypes"
+ "userFolder"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}"
- "+[RCSavedRecordingsModel _copyFileIntoRecordingsDirectory:]"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/VoiceMemos_Framework/Framework/Waveform/RCWaveformGenerator.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/VoiceMemos_Framework/Framework/Waveform/RCWaveformSegment.mm"
- "<Unknown File>"
- "<Unknown Function>"
- "@40@0:8@16d24@32"
- "@48@0:8@16d24@32@40"
- "@56@0:8@16d24@32@40@48"
- "BOOL _checkCanAppend(RCWaveformGenerator *__strong, SEL)"
- "RCCaptureFormat.m"
- "_copyFileIntoRecordingsDirectory:"
- "insertRecordingWithAudioFile:duration:date:"
- "insertRecordingWithAudioFile:duration:date:customLabelBase:"
- "insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:"
- "nextRecordingDefaultLabelWithCustomLabelBase:"
- "unsupported file extension: %@"
- "{vector<float, std::allocator<float> >=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float> >=\"__value_\"^f}}"

```
