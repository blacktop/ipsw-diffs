## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1274.0.0.0.0
-  __TEXT.__text: 0x46198
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x3ac4
-  __TEXT.__gcc_except_tab: 0x19fc
-  __TEXT.__const: 0x1f0
-  __TEXT.__cstring: 0x5ea7
-  __TEXT.__oslogstring: 0x2830
+1325.0.0.0.0
+  __TEXT.__text: 0x48b04
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_methlist: 0x3f0c
+  __TEXT.__gcc_except_tab: 0x1850
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0x6453
+  __TEXT.__oslogstring: 0x2a9d
   __TEXT.__ustring: 0x22
-  __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1920
-  __TEXT.__objc_classname: 0x80a
-  __TEXT.__objc_methname: 0xb2aa
-  __TEXT.__objc_methtype: 0x1562
-  __TEXT.__objc_stubs: 0x86e0
-  __DATA_CONST.__got: 0x638
-  __DATA_CONST.__const: 0x1d50
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__unwind_info: 0x1948
+  __TEXT.__objc_classname: 0x83f
+  __TEXT.__objc_methname: 0xc03e
+  __TEXT.__objc_methtype: 0x154f
+  __TEXT.__objc_stubs: 0x9280
+  __DATA_CONST.__got: 0x6a0
+  __DATA_CONST.__const: 0x1d28
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bc0
+  __DATA_CONST.__objc_selrefs: 0x2f00
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x638
-  __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0x30e0
-  __AUTH_CONST.__objc_const: 0x57c8
-  __AUTH_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_arraydata: 0xe0
+  __AUTH_CONST.__auth_got: 0x610
+  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__cfstring: 0x3360
+  __AUTH_CONST.__objc_const: 0x5e38
+  __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x2c0
-  __DATA.__data: 0x7f0
-  __DATA.__bss: 0x120
-  __DATA_DIRTY.__objc_data: 0xfa0
-  __DATA_DIRTY.__bss: 0x178
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x32c
+  __DATA.__data: 0x7a0
+  __DATA.__bss: 0x180
+  __DATA_DIRTY.__objc_data: 0xf00
+  __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaServices.framework/MediaServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
+  - /System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libCTGreenTeaLogger.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E448847D-5A91-3284-8C5B-31981EB43627
-  Functions: 1814
-  Symbols:   6337
-  CStrings:  3289
+  UUID: 6B66DDB4-F987-3668-894C-52A266F716F5
+  Functions: 1925
+  Symbols:   6705
+  CStrings:  3516
 
Symbols:
+ +[AVAsset(RCAdditions) _scaledIntFromFloat:]
+ +[AVAsset(RCAdditions) rc_createSharingMetadataItemForKey:andValue:]
+ +[AVAsset(RCAdditions) rc_unscaleScaledMetadataValue:]
+ +[NSManagedObjectModel(NewObjectModel) rc_v14ObjectModel]
+ +[RCComposition mergeCaptureFragmentMetadataURLForComposedAVURL:]
+ +[RCMutableMovie movieWithURL:error:].cold.2
+ +[RCQueryManager playableRecordingsExcludingDeletedPredicate]
+ +[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:completionHandler:]
+ +[RCSavedRecordingsModel(ExportAdditions) fetchRecordingUUIDsForExport:]
+ +[RCSavedRecordingsModel(ExportAdditions) sizeOfRecordingsForExport:]
+ +[RCSavedRecordingsModel(ImportAdditions) _copyFileIntoImportFilesTemporaryDirectory:error:]
+ +[RCSavedRecordingsModel(ImportAdditions) importFileWithURL:shouldUseMetadataTitle:completionHandler:]
+ +[RCSavedRecordingsModel(ImportAdditions) importFileWithURL:withMetadata:completionHandler:]
+ +[RCVoiceMemoMetadata supportsSecureCoding]
+ +[TranscriptionMetadata supportsSecureCoding]
+ +[UtteranceMetaData supportsSecureCoding]
+ -[AVAsset(RCAdditions) _rc_all_audioTracks]
+ -[AVAsset(RCAdditions) createExportSettingsForSampleRate:channelCount:formatRanking:]
+ -[AVAsset(RCAdditions) createExportSettingsForSampleRate:channelCount:formatRanking:].cold.1
+ -[AVAsset(RCAdditions) rc_audioTracksPreferringSpatial]
+ -[AVAsset(RCAdditions) rc_exportFormat]
+ -[AVAsset(RCAdditions) rc_hasSpatialTracks]
+ -[AVAsset(RCAdditions) rc_sharingMetadata]
+ -[AVAsset(RCAdditions) rc_trackIsSpatial:]
+ -[NSFileManager(RCAdditions) rc_path:isChildOf:]
+ -[NSUserDefaults(VoiceMemosSettings) rc_channelConfiguration]
+ -[NSUserDefaults(VoiceMemosSettings) rc_setChannelConfiguration:]
+ -[RCAssetWriter finishWritingWithError:]
+ -[RCCloudRecording _copyResourceFromLocation:toDirectory:usingName:andExtension:]
+ -[RCCloudRecording _copyResourceFromLocation:toDirectory:usingName:andExtension:].cold.1
+ -[RCCloudRecording _copyResourceFromLocation:toDirectory:usingName:andExtension:].cold.2
+ -[RCCloudRecording composedAssetIsSpatialRecording]
+ -[RCCloudRecording fileNameForSharing]
+ -[RCCloudRecording fileNameForSharing].cold.1
+ -[RCCloudRecording setComposedAssetIsSpatialRecording:]
+ -[RCCloudRecording(SyncedProperties) audioFutureVersionIsCompatible]
+ -[RCCloudRecording(SyncedProperties) canUpdateWithSpatialAsset]
+ -[RCCloudRecording(SyncedProperties) isSkipSilenceEnabled]
+ -[RCCloudRecording(SyncedProperties) isSpeechIsolatorEnabled]
+ -[RCCloudRecording(SyncedProperties) migratePlaybackSettings]
+ -[RCCloudRecording(SyncedProperties) playRate]
+ -[RCCloudRecording(SyncedProperties) setIsSkipSilenceEnabled:]
+ -[RCCloudRecording(SyncedProperties) setIsSpeechIsolatorEnabled:]
+ -[RCCloudRecording(SyncedProperties) setPlayRate:]
+ -[RCCloudRecording(SyncedProperties) setSpeechIsolatorValue:]
+ -[RCCloudRecording(SyncedProperties) setSyncedAudioFuture:sourceFileURL:containsSpatialAudio:]
+ -[RCCloudRecording(SyncedProperties) setSyncedAudioFuture:sourceFileURL:containsSpatialAudio:].cold.1
+ -[RCCloudRecording(SyncedProperties) speechIsolatorValue]
+ -[RCComposition _updateCachedValueForHasSpatialAudio]
+ -[RCComposition cachedHasSpatialAudio]
+ -[RCComposition hasSpatialAudio]
+ -[RCComposition setCachedHasSpatialAudio:]
+ -[RCPersistentContainer performBlockAndWaitWithBackgroundModel:]
+ -[RCPersistentContainer performBlockWithBackgroundModel:]
+ -[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]
+ -[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:].cold.1
+ -[RCSSavedRecordingService fetchRecordingUUIDsForExport:]
+ -[RCSSavedRecordingService fetchRecordingUUIDsForExport:].cold.1
+ -[RCSSavedRecordingService sizeOfRecordingsForExport:]
+ -[RCSSavedRecordingService sizeOfRecordingsForExport:].cold.1
+ -[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:].cold.1
+ -[RCSavedRecordingsModel _postProcessCloudRecordingForRecordingWithId:named:userInfo:isMigrationImport:isMusicMemoImport:sharingMetadata:]
+ -[RCSavedRecordingsModel _postProcessCloudRecordingForRecordingWithId:named:userInfo:isMigrationImport:isMusicMemoImport:sharingMetadata:].cold.1
+ -[RCSavedRecordingsModel _postProcessCloudRecordingForRecordingWithId:named:userInfo:isMigrationImport:isMusicMemoImport:sharingMetadata:].cold.2
+ -[RCSavedRecordingsModel _postProcessCloudRecordingForRecordingWithId:named:userInfo:isMigrationImport:isMusicMemoImport:sharingMetadata:].cold.3
+ -[RCSavedRecordingsModel _postProcessCloudRecordingForRecordingWithId:named:userInfo:isMigrationImport:isMusicMemoImport:sharingMetadata:].cold.4
+ -[RCSpatialAsset .cxx_destruct]
+ -[RCSpatialAsset _associatedTrackOfType:forTrack:]
+ -[RCSpatialAsset _descriptionIsSpatial:]
+ -[RCSpatialAsset _findOverdubTrack]
+ -[RCSpatialAsset _findSpatialMetadataGroup]
+ -[RCSpatialAsset _findSpatialTrack]
+ -[RCSpatialAsset _isSpatialTrack:]
+ -[RCSpatialAsset _metadataGroupFor:]
+ -[RCSpatialAsset _metadataGroupFor:].cold.1
+ -[RCSpatialAsset asset]
+ -[RCSpatialAsset fallbackTrack]
+ -[RCSpatialAsset initWithAsset:]
+ -[RCSpatialAsset overdubTrack]
+ -[RCSpatialAsset spatialMetadataGroup]
+ -[RCSpatialAsset spatialTrack]
+ -[RCVoiceMemoMetadata .cxx_destruct]
+ -[RCVoiceMemoMetadata channelCount]
+ -[RCVoiceMemoMetadata codec]
+ -[RCVoiceMemoMetadata creationTimeMillis]
+ -[RCVoiceMemoMetadata deletionTimeMillis]
+ -[RCVoiceMemoMetadata durationMillis]
+ -[RCVoiceMemoMetadata encodeWithCoder:]
+ -[RCVoiceMemoMetadata enhanced]
+ -[RCVoiceMemoMetadata favorite]
+ -[RCVoiceMemoMetadata folder]
+ -[RCVoiceMemoMetadata initWithCoder:]
+ -[RCVoiceMemoMetadata multiLayerMix]
+ -[RCVoiceMemoMetadata multiLayer]
+ -[RCVoiceMemoMetadata path]
+ -[RCVoiceMemoMetadata recordedOnWatch]
+ -[RCVoiceMemoMetadata sampleRate]
+ -[RCVoiceMemoMetadata setChannelCount:]
+ -[RCVoiceMemoMetadata setCodec:]
+ -[RCVoiceMemoMetadata setCreationTimeMillis:]
+ -[RCVoiceMemoMetadata setDeletionTimeMillis:]
+ -[RCVoiceMemoMetadata setDurationMillis:]
+ -[RCVoiceMemoMetadata setEnhanced:]
+ -[RCVoiceMemoMetadata setFavorite:]
+ -[RCVoiceMemoMetadata setFolder:]
+ -[RCVoiceMemoMetadata setMultiLayer:]
+ -[RCVoiceMemoMetadata setMultiLayerMix:]
+ -[RCVoiceMemoMetadata setPath:]
+ -[RCVoiceMemoMetadata setRecordedOnWatch:]
+ -[RCVoiceMemoMetadata setSampleRate:]
+ -[RCVoiceMemoMetadata setTitle:]
+ -[RCVoiceMemoMetadata setTranscription:]
+ -[RCVoiceMemoMetadata setWrappedURL:]
+ -[RCVoiceMemoMetadata title]
+ -[RCVoiceMemoMetadata transcription]
+ -[RCVoiceMemoMetadata wrappedURL]
+ -[RCWaveform potentiallyCorrupted]
+ -[RCWaveform setPotentiallyCorrupted:]
+ -[RCWaveformDataSource markWaveformPotentiallyCorrupted]
+ -[RCWaveformDataSource saveGeneratedWaveformIfNecessary].cold.2
+ -[TranscriptionMetadata .cxx_destruct]
+ -[TranscriptionMetadata encodeWithCoder:]
+ -[TranscriptionMetadata initWithCoder:]
+ -[TranscriptionMetadata language]
+ -[TranscriptionMetadata setLanguage:]
+ -[TranscriptionMetadata setUtterances:]
+ -[TranscriptionMetadata utterances]
+ -[UtteranceMetaData .cxx_destruct]
+ -[UtteranceMetaData encodeWithCoder:]
+ -[UtteranceMetaData formattedString]
+ -[UtteranceMetaData initWithCoder:]
+ -[UtteranceMetaData offsetMillis]
+ -[UtteranceMetaData onsetMillis]
+ -[UtteranceMetaData rawString]
+ -[UtteranceMetaData setFormattedString:]
+ -[UtteranceMetaData setOffsetMillis:]
+ -[UtteranceMetaData setOnsetMillis:]
+ -[UtteranceMetaData setRawString:]
+ GCC_except_table100
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table136
+ GCC_except_table138
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table37
+ GCC_except_table51
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table79
+ GCC_except_table82
+ GCC_except_table86
+ GCC_except_table90
+ GCC_except_table93
+ _AVAudioSessionModeSpatialCapture
+ _AVGQX3DWIDHL6QYY3OCER3G5UEM2QU
+ _AVGestaltGetBoolAnswer
+ _AVMediaTypeMetadata
+ _AVNumberOfChannelsKey
+ _AVTrackAssociationTypeAudioFallback
+ _AVTrackAssociationTypeMetadataReferent
+ _CMAudioFormatDescriptionGetChannelLayout
+ _MGIsDeviceOneOfType
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_AVComposition
+ _OBJC_CLASS_$_AVSampleBufferGenerator
+ _OBJC_CLASS_$_AVSampleBufferRequest
+ _OBJC_CLASS_$_AVTimedMetadataGroup
+ _OBJC_CLASS_$_LNSpotlightAppEntityMapper
+ _OBJC_CLASS_$_NUPlatform
+ _OBJC_CLASS_$_RCSpatialAsset
+ _OBJC_CLASS_$_RCVoiceMemoMetadata
+ _OBJC_CLASS_$_TranscriptionMetadata
+ _OBJC_CLASS_$_UtteranceMetaData
+ _OBJC_IVAR_$_RCAssetWriter._markedAsFinished
+ _OBJC_IVAR_$_RCComposition._cachedHasSpatialAudio
+ _OBJC_IVAR_$_RCComposition._cachedValueForHasSpatialAudioIsValid
+ _OBJC_IVAR_$_RCSpatialAsset._asset
+ _OBJC_IVAR_$_RCSpatialAsset._fallbackTrack
+ _OBJC_IVAR_$_RCSpatialAsset._overdubTrack
+ _OBJC_IVAR_$_RCSpatialAsset._spatialMetadataGroup
+ _OBJC_IVAR_$_RCSpatialAsset._spatialTrack
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._channelCount
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._codec
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._creationTimeMillis
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._deletionTimeMillis
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._durationMillis
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._enhanced
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._favorite
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._folder
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._multiLayer
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._multiLayerMix
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._path
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._recordedOnWatch
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._sampleRate
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._title
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._transcription
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._wrappedURL
+ _OBJC_IVAR_$_RCWaveform._potentiallyCorrupted
+ _OBJC_IVAR_$_TranscriptionMetadata._language
+ _OBJC_IVAR_$_TranscriptionMetadata._utterances
+ _OBJC_IVAR_$_UtteranceMetaData._formattedString
+ _OBJC_IVAR_$_UtteranceMetaData._offsetMillis
+ _OBJC_IVAR_$_UtteranceMetaData._onsetMillis
+ _OBJC_IVAR_$_UtteranceMetaData._rawString
+ _OBJC_METACLASS_$_RCSpatialAsset
+ _OBJC_METACLASS_$_RCVoiceMemoMetadata
+ _OBJC_METACLASS_$_TranscriptionMetadata
+ _OBJC_METACLASS_$_UtteranceMetaData
+ _RCAudioExportFormatRankings
+ _RCAudioFuturePropertyNames
+ _RCAudioFuturePropertyNames.audioFuturePropertyNames
+ _RCAudioFuturePropertyNames.cold.1
+ _RCAudioFuturePropertyNames.onceToken
+ _RCCaptureDirectoryURL
+ _RCCaptureDirectoryURL.captureDirectoryURL
+ _RCCaptureDirectoryURL.cold.1
+ _RCCaptureDirectoryURL.onceToken
+ _RCCaptureRecoveryDirectoryURL
+ _RCCaptureRecoveryDirectoryURL.captureRecoveryDirectoryURL
+ _RCCaptureRecoveryDirectoryURL.cold.1
+ _RCCaptureRecoveryDirectoryURL.onceToken
+ _RCCloudRecording_AudioFutureFlags
+ _RCCloudRecording_LegacyPlaybackRate
+ _RCCloudRecording_LegacySilenceRemoverEnabled
+ _RCCloudRecording_VersionedAudioFuture
+ _RCHighQualityBluetoothRecordingEnabled
+ _RCHighQualityBluetoothRecordingEnabled.cold.1
+ _RCHighQualityBluetoothRecordingEnabled.enabled
+ _RCHighQualityBluetoothRecordingEnabled.onceToken
+ _RCRecordingShareMetadataKeyEnhanceEnabled
+ _RCRecordingShareMetadataKeyLayerMix
+ _RCRecordingShareMetadataKeyPlaybackRate
+ _RCRecordingShareMetadataKeySkipSilenceEnabled
+ _RCRecordingShareMetadataKeySpeechIsolatorValue
+ _RCSavedRecordingsImportErrorDomain
+ _RCSpatialAudioCaptureAvailable
+ _RCSpatialAudioCaptureAvailable.cold.1
+ _RCSpatialAudioCaptureAvailable.enabled
+ _RCSpatialAudioCaptureAvailable.onceToken
+ _RCSpatialEffectsAreAvailable
+ _RCSpatialEffectsAreAvailable.available
+ _RCSpatialEffectsAreAvailable.cold.1
+ _RCSpatialEffectsAreAvailable.onceToken
+ _RCSpatialFeatureFlagIsEnabled
+ _RCSpatialFeatureFlagIsEnabled.cold.1
+ _RCSpatialFeatureFlagIsEnabled.enabled
+ _RCSpatialFeatureFlagIsEnabled.onceToken
+ __OBJC_$_CLASS_METHODS_RCSavedRecordingsModel(ImportAdditions|ExportAdditions)
+ __OBJC_$_CLASS_METHODS_RCVoiceMemoMetadata
+ __OBJC_$_CLASS_METHODS_TranscriptionMetadata
+ __OBJC_$_CLASS_METHODS_UtteranceMetaData
+ __OBJC_$_CLASS_PROP_LIST_RCVoiceMemoMetadata
+ __OBJC_$_CLASS_PROP_LIST_TranscriptionMetadata
+ __OBJC_$_CLASS_PROP_LIST_UtteranceMetaData
+ __OBJC_$_INSTANCE_METHODS_RCSpatialAsset
+ __OBJC_$_INSTANCE_METHODS_RCVoiceMemoMetadata
+ __OBJC_$_INSTANCE_METHODS_TranscriptionMetadata
+ __OBJC_$_INSTANCE_METHODS_UtteranceMetaData
+ __OBJC_$_INSTANCE_VARIABLES_RCSpatialAsset
+ __OBJC_$_INSTANCE_VARIABLES_RCVoiceMemoMetadata
+ __OBJC_$_INSTANCE_VARIABLES_TranscriptionMetadata
+ __OBJC_$_INSTANCE_VARIABLES_UtteranceMetaData
+ __OBJC_$_PROP_LIST_RCSpatialAsset
+ __OBJC_$_PROP_LIST_RCVoiceMemoMetadata
+ __OBJC_$_PROP_LIST_TranscriptionMetadata
+ __OBJC_$_PROP_LIST_UtteranceMetaData
+ __OBJC_CLASS_PROTOCOLS_$_RCVoiceMemoMetadata
+ __OBJC_CLASS_PROTOCOLS_$_TranscriptionMetadata
+ __OBJC_CLASS_PROTOCOLS_$_UtteranceMetaData
+ __OBJC_CLASS_RO_$_RCSpatialAsset
+ __OBJC_CLASS_RO_$_RCVoiceMemoMetadata
+ __OBJC_CLASS_RO_$_TranscriptionMetadata
+ __OBJC_CLASS_RO_$_UtteranceMetaData
+ __OBJC_METACLASS_RO_$_RCSpatialAsset
+ __OBJC_METACLASS_RO_$_RCVoiceMemoMetadata
+ __OBJC_METACLASS_RO_$_TranscriptionMetadata
+ __OBJC_METACLASS_RO_$_UtteranceMetaData
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8ne200100ERKf
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke.117
+ ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke_2.118
+ ___102+[RCSavedRecordingsModel(ImportAdditions) importFileWithURL:shouldUseMetadataTitle:completionHandler:]_block_invoke
+ ___102+[RCSavedRecordingsModel(ImportAdditions) importFileWithURL:shouldUseMetadataTitle:completionHandler:]_block_invoke_2
+ ___102+[RCSavedRecordingsModel(ImportAdditions) importFileWithURL:shouldUseMetadataTitle:completionHandler:]_block_invoke_2.cold.1
+ ___114-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke.103
+ ___130-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke.108
+ ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke.113
+ ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke_2.114
+ ___40-[RCAssetWriter finishWritingWithError:]_block_invoke
+ ___40-[RCSSavedRecordingService serviceProxy]_block_invoke.108
+ ___43-[AVAsset(RCAdditions) rc_hasSpatialTracks]_block_invoke
+ ___43-[AVAsset(RCAdditions) rc_hasSpatialTracks]_block_invoke_2
+ ___49-[RCSSavedRecordingService openServiceConnection]_block_invoke.27
+ ___51-[RCSSavedRecordingService __fetchAllAccessTokens:]_block_invoke.85
+ ___53-[RCComposition _updateCachedValueForHasSpatialAudio]_block_invoke
+ ___53-[RCComposition _updateCachedValueForHasSpatialAudio]_block_invoke_2
+ ___54-[RCSSavedRecordingService sizeOfRecordingsForExport:]_block_invoke
+ ___54-[RCSSavedRecordingService sizeOfRecordingsForExport:]_block_invoke_2
+ ___54-[RCSSavedRecordingService sizeOfRecordingsForExport:]_block_invoke_2.cold.1
+ ___54-[RCSSavedRecordingService sizeOfRecordingsForExport:]_block_invoke_2.cold.2
+ ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke.99
+ ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke_2.101
+ ___57-[RCPersistentContainer performBlockWithBackgroundModel:]_block_invoke
+ ___57-[RCSSavedRecordingService fetchRecordingUUIDsForExport:]_block_invoke
+ ___57-[RCSSavedRecordingService fetchRecordingUUIDsForExport:]_block_invoke_2
+ ___57-[RCSSavedRecordingService fetchRecordingUUIDsForExport:]_block_invoke_2.cold.1
+ ___57-[RCSSavedRecordingService fetchRecordingUUIDsForExport:]_block_invoke_2.cold.2
+ ___64-[RCPersistentContainer performBlockAndWaitWithBackgroundModel:]_block_invoke
+ ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingExported:]_block_invoke.81
+ ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingModified:]_block_invoke.83
+ ___64-[RCSSavedRecordingService prepareToTrimCompositionAVURL:error:]_block_invoke.76
+ ___66-[RCSSavedRecordingService prepareToExportCompositionAVURL:error:]_block_invoke.71
+ ___67-[RCSSavedRecordingService prepareToPreviewCompositionAVURL:error:]_block_invoke.66
+ ___69-[RCSSavedRecordingService prepareToCaptureToCompositionAVURL:error:]_block_invoke.60
+ ___72+[RCSavedRecordingsModel(ExportAdditions) fetchRecordingUUIDsForExport:]_block_invoke
+ ___78-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke
+ ___78-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke_2
+ ___78-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke_2.cold.1
+ ___78-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke_2.cold.2
+ ___95+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:completionHandler:]_block_invoke
+ ___95+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:completionHandler:]_block_invoke.cold.1
+ ___RCAudioFuturePropertyNames_block_invoke
+ ___RCCaptureDirectoryURL_block_invoke
+ ___RCCaptureDirectoryURL_block_invoke.cold.1
+ ___RCCaptureRecoveryDirectoryURL_block_invoke
+ ___RCCaptureRecoveryDirectoryURL_block_invoke.cold.1
+ ___RCHighQualityBluetoothRecordingEnabled_block_invoke
+ ___RCSpatialAudioCaptureAvailable_block_invoke
+ ___RCSpatialAudioCaptureAvailable_block_invoke.cold.1
+ ___RCSpatialEffectsAreAvailable_block_invoke
+ ___RCSpatialEffectsAreAvailable_block_invoke.cold.1
+ ___RCSpatialFeatureFlagIsEnabled_block_invoke
+ ___block_descriptor_32_e35_16?0"AVCompositionTrackSegment"8l
+ ___block_descriptor_32_e37_"NSArray"16?0"AVCompositionTrack"8l
+ ___block_descriptor_32_e38_"NSURL"16?0"RCCompositionFragment"8l
+ ___block_descriptor_32_e73_v24?0"<RCSSavedRecordingServiceProtocol>"8?<v?"NSArray""NSError">16l
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e41_B24?0"AVMetadataItem"8"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32s_e85_v24?0"<RCSSavedRecordingServiceProtocol>"8?<v?"RCVoiceMemoMetadata""NSError">16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e41_v24?0"RCVoiceMemoMetadata"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e41_v24?0"RCVoiceMemoMetadata"8"NSError"16ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e39_v24?0"NSManagedObjectID"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e56_v32?0"NSManagedObjectID"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e8_v16?0q8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_90_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___block_literal_global.103
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.131
+ ___block_literal_global.141
+ ___block_literal_global.151
+ ___block_literal_global.154
+ ___block_literal_global.157
+ ___block_literal_global.160
+ ___block_literal_global.169
+ ___block_literal_global.177
+ ___block_literal_global.186
+ ___block_literal_global.191
+ ___block_literal_global.204
+ ___block_literal_global.207
+ ___block_literal_global.210
+ ___block_literal_global.215
+ ___block_literal_global.219
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.226
+ ___block_literal_global.231
+ ___block_literal_global.286
+ ___block_literal_global.297
+ ___block_literal_global.33
+ ___block_literal_global.35
+ ___block_literal_global.40
+ ___block_literal_global.44
+ ___block_literal_global.51
+ ___block_literal_global.54
+ ___block_literal_global.58
+ ___block_literal_global.71
+ ___block_literal_global.72
+ ___block_literal_global.80
+ ___block_literal_global.90
+ ___removeSharingKeysPredicate_block_invoke
+ _firstNumberValue
+ _kDefaultSpeechIsolatorValue
+ _objc_msgSend$_associatedTrackOfType:forTrack:
+ _objc_msgSend$_copyFileIntoImportFilesTemporaryDirectory:error:
+ _objc_msgSend$_copyResourceFromLocation:toDirectory:usingName:andExtension:
+ _objc_msgSend$_descriptionIsSpatial:
+ _objc_msgSend$_findOverdubTrack
+ _objc_msgSend$_findSpatialMetadataGroup
+ _objc_msgSend$_findSpatialTrack
+ _objc_msgSend$_isSpatialTrack:
+ _objc_msgSend$_metadataGroupFor:
+ _objc_msgSend$_postProcessCloudRecordingForRecordingWithId:named:userInfo:isMigrationImport:isMusicMemoImport:sharingMetadata:
+ _objc_msgSend$_rc_all_audioTracks
+ _objc_msgSend$_scaledIntFromFloat:
+ _objc_msgSend$_updateCachedValueForHasSpatialAudio
+ _objc_msgSend$asset
+ _objc_msgSend$associatedTracksOfType:
+ _objc_msgSend$audioFutureFlags
+ _objc_msgSend$codec
+ _objc_msgSend$composedAssetHasMultipleTracks
+ _objc_msgSend$composedAssetIsSpatialRecording
+ _objc_msgSend$createExportSettingsForSampleRate:channelCount:formatRanking:
+ _objc_msgSend$createSampleBufferForRequest:error:
+ _objc_msgSend$creationTimeMillis
+ _objc_msgSend$currentPlatform
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$deletionTimeMillis
+ _objc_msgSend$determineImportabilityOfRecordingWithAudioURL:completionHandler:
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$durationMillis
+ _objc_msgSend$enhanced
+ _objc_msgSend$family
+ _objc_msgSend$fetchMetadataForRecordingWithUUID:completionBlock:
+ _objc_msgSend$fetchRecordingUUIDsForExport:
+ _objc_msgSend$fileNameForSharing
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$finishWritingAudioFile:
+ _objc_msgSend$formattedString
+ _objc_msgSend$importRecordingWithSourceAudioURL:name:date:completionHandler:
+ _objc_msgSend$initWithAsset:
+ _objc_msgSend$initWithAsset:timebase:
+ _objc_msgSend$initWithSampleBuffer:
+ _objc_msgSend$initWithStartCursor:
+ _objc_msgSend$items
+ _objc_msgSend$key
+ _objc_msgSend$language
+ _objc_msgSend$mainDevice
+ _objc_msgSend$makeSampleCursorWithPresentationTimeStamp:
+ _objc_msgSend$mediaType
+ _objc_msgSend$multiLayer
+ _objc_msgSend$multiLayerMix
+ _objc_msgSend$na_any:
+ _objc_msgSend$na_flatMap:
+ _objc_msgSend$newBackgroundModel
+ _objc_msgSend$offsetMillis
+ _objc_msgSend$onsetMillis
+ _objc_msgSend$overdubTrack
+ _objc_msgSend$playableRecordingsExcludingDeletedPredicate
+ _objc_msgSend$playbackSpeed
+ _objc_msgSend$potentiallyCorrupted
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$rawString
+ _objc_msgSend$rc_andNot:
+ _objc_msgSend$rc_audioTracksPreferringSpatial
+ _objc_msgSend$rc_hasSpatialTracks
+ _objc_msgSend$rc_path:isChildOf:
+ _objc_msgSend$rc_sharingMetadata
+ _objc_msgSend$rc_unscaleScaledMetadataValue:
+ _objc_msgSend$rc_v14ObjectModel
+ _objc_msgSend$setAudioFutureFlags:
+ _objc_msgSend$setChannelCount:
+ _objc_msgSend$setCodec:
+ _objc_msgSend$setComposedAssetIsSpatialRecording:
+ _objc_msgSend$setCreationTimeMillis:
+ _objc_msgSend$setDeletionTimeMillis:
+ _objc_msgSend$setDirection:
+ _objc_msgSend$setDurationMillis:
+ _objc_msgSend$setFolder:
+ _objc_msgSend$setFormattedString:
+ _objc_msgSend$setIsSkipSilenceEnabled:
+ _objc_msgSend$setIsSpeechIsolatorEnabled:
+ _objc_msgSend$setLanguage:
+ _objc_msgSend$setMaxSampleCount:
+ _objc_msgSend$setMultiLayer:
+ _objc_msgSend$setMultiLayerMix:
+ _objc_msgSend$setOffsetMillis:
+ _objc_msgSend$setOnsetMillis:
+ _objc_msgSend$setPath:
+ _objc_msgSend$setPlayRate:
+ _objc_msgSend$setPlaybackSpeed:
+ _objc_msgSend$setPotentiallyCorrupted:
+ _objc_msgSend$setPreferredMinSampleCount:
+ _objc_msgSend$setRawString:
+ _objc_msgSend$setRecordedOnWatch:
+ _objc_msgSend$setSampleRate:
+ _objc_msgSend$setSkipSilenceEnabled:
+ _objc_msgSend$setSpeechIsolatorValue:
+ _objc_msgSend$setStudioMixEnabled:
+ _objc_msgSend$setStudioMixLevel:
+ _objc_msgSend$setSyncedAudioFuture:sourceFileURL:containsSpatialAudio:
+ _objc_msgSend$setTranscription:
+ _objc_msgSend$setUtterances:
+ _objc_msgSend$setVersionedAudioFuture:
+ _objc_msgSend$setWrappedURL:
+ _objc_msgSend$sizeOfRecordingsForExport:
+ _objc_msgSend$skipSilenceEnabled
+ _objc_msgSend$sourceURL
+ _objc_msgSend$spatialTrack
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$studioMixEnabled
+ _objc_msgSend$studioMixLevel
+ _objc_msgSend$supportsANE
+ _objc_msgSend$trackID
+ _objc_msgSend$tracks
+ _objc_msgSend$transcription
+ _objc_msgSend$transcriptionContentExists
+ _objc_msgSend$utterances
+ _objc_msgSend$versionedAudioFuture
+ _objc_msgSend$wrappedURL
- -[AVAsset(RCAdditions) rc_composedAVURL]
- -[AVAsset(RCAdditions) rc_setComposedAVURL:]
- -[NSFileManager(RCAdditions) rc_path:isSubpathOf:]
- -[RCCloudRecording _fileNameForSharing]
- -[RCCloudRecording _fileNameForSharing].cold.1
- -[RCCloudRecording copyResourcesForSharingIntoDirectory:].cold.2
- -[RCCloudRecording(SyncedProperties) setSyncedAudioFuture:sourceFileURL:]
- -[RCCloudRecording(SyncedProperties) setSyncedAudioFuture:sourceFileURL:].cold.1
- -[RCComposition _compositionByReplacingDecomposedFragments:]
- -[RCComposition _eaccess_repairDecomposedFragmentMetadataIfNecessary:]
- -[RCComposition composedAssetIsM4a]
- -[RCComposition rcs_composeToFinalDestinationWithCompletionBlock:]
- -[RCComposition rcs_repairDecomposedFragmentMetadataIfNecessary:]
- -[RCComposition willMigrateFromM4aToQta]
- -[RCCompositionComposedAssetWriter .cxx_destruct]
- -[RCCompositionComposedAssetWriter cancel]
- -[RCCompositionComposedAssetWriter composition]
- -[RCCompositionComposedAssetWriter initWithComposition:]
- -[RCCompositionComposedAssetWriter progress]
- -[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]
- -[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:].cold.1
- -[RCSSavedRecordingAccessToken setUserInfo:]
- -[RCSSavedRecordingAccessToken userInfo]
- -[RCSSavedRecordingService closeAudioFile:completionBlock:]
- -[RCSSavedRecordingService closeAudioFile:completionBlock:].cold.1
- -[RCSSavedRecordingService closeAudioFile:error:]
- -[RCSSavedRecordingService closeAudioFile:error:].cold.1
- -[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:]
- -[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:].cold.1
- -[RCSSavedRecordingService openAudioFile:settings:metadata:error:]
- -[RCSSavedRecordingService writeAudioFile:buffer:completionBlock:]
- -[_RCSAudioFile .cxx_destruct]
- -[_RCSAudioFile fileFormat]
- -[_RCSAudioFile fileToken]
- -[_RCSAudioFile processingFormat]
- -[_RCSAudioFile setFileToken:]
- -[_RCSAudioFile settings]
- -[_RCSAudioFile url]
- GCC_except_table104
- GCC_except_table125
- GCC_except_table132
- GCC_except_table134
- GCC_except_table140
- GCC_except_table147
- GCC_except_table150
- GCC_except_table152
- GCC_except_table155
- GCC_except_table158
- GCC_except_table161
- GCC_except_table164
- GCC_except_table167
- GCC_except_table170
- GCC_except_table174
- GCC_except_table177
- GCC_except_table49
- GCC_except_table67
- GCC_except_table70
- GCC_except_table74
- GCC_except_table77
- GCC_except_table80
- GCC_except_table83
- GCC_except_table89
- GCC_except_table91
- GCC_except_table94
- GCC_except_table97
- GCC_except_table99
- _LinkServicesLibraryCore.frameworkLibrary
- _MGGetStringAnswer
- _NSDefaultRunLoopMode
- _OBJC_CLASS_$_NSTimer
- _OBJC_CLASS_$_RCCompositionComposedAssetWriter
- _OBJC_CLASS_$__RCSAudioFile
- _OBJC_IVAR_$_RCCompositionComposedAssetWriter._composition
- _OBJC_IVAR_$_RCCompositionComposedAssetWriter._exportSession
- _OBJC_IVAR_$_RCSSavedRecordingAccessToken._userInfo
- _OBJC_IVAR_$__RCSAudioFile._fileToken
- _OBJC_METACLASS_$_RCCompositionComposedAssetWriter
- _OBJC_METACLASS_$__RCSAudioFile
- _RCOverdubRecordingFeatureFlagIsEnabled
- _RCOverdubRecordingFeatureFlagIsEnabled.cold.1
- _RCOverdubRecordingFeatureFlagIsEnabled.enabled
- _RCOverdubRecordingFeatureFlagIsEnabled.onceToken
- _RCSSavedRecordingAccessTokenUserInfoKey_FileFormat
- _RCSSavedRecordingAccessTokenUserInfoKey_Metadata
- _RCSSavedRecordingAccessTokenUserInfoKey_ProcessingFormat
- _RCSSavedRecordingAccessTokenUserInfoKey_Settings
- _RCSSavedRecordingServiceAudioFileMetadataKey_Composition
- _RCSSavedRecordingServiceAudioFileMetadataKey_OutputFragment
- _RCSSavedRecordingServiceAudioFileMetadataKey_UniqueID
- _RCSaveAsNewFeatureFlagIsEnabled
- _RCSaveAsNewFeatureFlagIsEnabled.cold.1
- _RCSaveAsNewFeatureFlagIsEnabled.onceToken
- _RCSaveAsNewFeatureFlagIsEnabled.saveAsNewEnabled
- _RCSupportsDebugAODOverlay
- _RCTestAlwaysShowLockScreenPlugin
- _RCTestAlwaysShowLockScreenPlugin.cold.1
- __OBJC_$_CLASS_METHODS_RCSavedRecordingsModel
- __OBJC_$_INSTANCE_METHODS_RCCompositionComposedAssetWriter
- __OBJC_$_INSTANCE_METHODS__RCSAudioFile
- __OBJC_$_INSTANCE_VARIABLES_RCCompositionComposedAssetWriter
- __OBJC_$_INSTANCE_VARIABLES__RCSAudioFile
- __OBJC_$_PROP_LIST_RCCompositionComposedAssetWriter
- __OBJC_$_PROP_LIST_RCSAudioFile
- __OBJC_$_PROP_LIST__RCSAudioFile
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_RCSAudioFile
- __OBJC_$_PROTOCOL_METHOD_TYPES_RCSAudioFile
- __OBJC_$_PROTOCOL_REFS_RCSAudioFile
- __OBJC_CLASS_PROTOCOLS_$__RCSAudioFile
- __OBJC_CLASS_RO_$_RCCompositionComposedAssetWriter
- __OBJC_CLASS_RO_$__RCSAudioFile
- __OBJC_LABEL_PROTOCOL_$_RCSAudioFile
- __OBJC_METACLASS_RO_$_RCCompositionComposedAssetWriter
- __OBJC_METACLASS_RO_$__RCSAudioFile
- __OBJC_PROTOCOL_$_RCSAudioFile
- __RCTestAlwaysShowLockScreenPlugin
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke.192
- ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke_2.193
- ___111-[RCSavedRecordingsModel importRecordingWithSourceAudioURL:name:date:xpcConnection:userInfo:completionHandler:]_block_invoke_2.cold.1
- ___114-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke.97
- ___130-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke.102
- ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke.188
- ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke_2.189
- ___32-[RCSSavedRecordingService init]_block_invoke_3
- ___40-[RCSSavedRecordingService serviceProxy]_block_invoke.183
- ___49-[RCSSavedRecordingService closeAudioFile:error:]_block_invoke
- ___49-[RCSSavedRecordingService closeAudioFile:error:]_block_invoke_2
- ___49-[RCSSavedRecordingService openServiceConnection]_block_invoke.107
- ___51-[RCSSavedRecordingService __fetchAllAccessTokens:]_block_invoke.160
- ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke.174
- ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke_2.176
- ___59-[RCSSavedRecordingService closeAudioFile:completionBlock:]_block_invoke
- ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingExported:]_block_invoke.156
- ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingModified:]_block_invoke.158
- ___64-[RCSSavedRecordingService prepareToTrimCompositionAVURL:error:]_block_invoke.152
- ___65-[RCComposition rcs_repairDecomposedFragmentMetadataIfNecessary:]_block_invoke
- ___66-[RCComposition rcs_composeToFinalDestinationWithCompletionBlock:]_block_invoke
- ___66-[RCComposition rcs_composeToFinalDestinationWithCompletionBlock:]_block_invoke_2
- ___66-[RCComposition rcs_composeToFinalDestinationWithCompletionBlock:]_block_invoke_2.cold.1
- ___66-[RCSSavedRecordingService openAudioFile:settings:metadata:error:]_block_invoke
- ___66-[RCSSavedRecordingService openAudioFile:settings:metadata:error:]_block_invoke.135
- ___66-[RCSSavedRecordingService openAudioFile:settings:metadata:error:]_block_invoke.cold.1
- ___66-[RCSSavedRecordingService openAudioFile:settings:metadata:error:]_block_invoke.cold.2
- ___66-[RCSSavedRecordingService prepareToExportCompositionAVURL:error:]_block_invoke.147
- ___66-[RCSSavedRecordingService writeAudioFile:buffer:completionBlock:]_block_invoke
- ___67-[RCSSavedRecordingService prepareToPreviewCompositionAVURL:error:]_block_invoke.142
- ___69-[RCSSavedRecordingService prepareToCaptureToCompositionAVURL:error:]_block_invoke.129
- ___70-[RCComposition _eaccess_repairDecomposedFragmentMetadataIfNecessary:]_block_invoke
- ___70-[RCComposition _eaccess_repairDecomposedFragmentMetadataIfNecessary:]_block_invoke.cold.1
- ___72-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]_block_invoke
- ___72-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]_block_invoke.7
- ___72-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]_block_invoke.7.cold.1
- ___72-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]_block_invoke.9
- ___72-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]_block_invoke.9.cold.1
- ___72-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]_block_invoke.9.cold.2
- ___72-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]_block_invoke_2
- ___81-[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:]_block_invoke
- ___81-[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:]_block_invoke_2
- ___81-[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:]_block_invoke_2.cold.1
- ___81-[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:]_block_invoke_2.cold.2
- ___LinkServicesLibraryCore_block_invoke
- ___RCOverdubRecordingFeatureFlagIsEnabled_block_invoke
- ___RCOverdubRecordingIsEnabled_block_invoke.cold.1
- ___RCSaveAsNewFeatureFlagIsEnabled_block_invoke
- ___block_descriptor_40_e8_32bs_e26_v20?0"RCComposition"8B16ls32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32bs40r_e27_v24?0"NSURL"8"NSError"16ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e63_v24?0"<RCSSavedRecordingServiceProtocol>"8?<v?"NSError">16ls32l8s40l8
- ___block_descriptor_52_e8_32s40s_e17_v16?0"NSTimer"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40r_e38_v32?0"RCCompositionFragment"8Q16^B24lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e39_v24?0"NSManagedObjectID"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e94_v24?0"<RCSSavedRecordingServiceProtocol>"8?<v?"RCSSavedRecordingAccessToken""NSError">16ls32l8s40l8s48l8
- ___block_descriptor_60_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e39_v24?0"NSManagedObjectID"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48bs56r64r72r_e5_v8?0ls32l8r56l8r64l8s40l8r72l8s48l8
- ___block_descriptor_80_e8_32s40s48bs56r64r72r_e8_v12?0B8ls32l8r56l8r64l8r72l8s40l8s48l8
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8
- ___block_literal_global.113
- ___block_literal_global.115
- ___block_literal_global.116
- ___block_literal_global.118
- ___block_literal_global.120
- ___block_literal_global.121
- ___block_literal_global.126
- ___block_literal_global.134
- ___block_literal_global.155
- ___block_literal_global.163
- ___block_literal_global.171
- ___block_literal_global.178
- ___block_literal_global.180
- ___block_literal_global.182
- ___block_literal_global.185
- ___block_literal_global.190
- ___block_literal_global.197
- ___block_literal_global.209
- ___block_literal_global.214
- ___block_literal_global.220
- ___block_literal_global.295
- ___block_literal_global.38
- ___block_literal_global.61
- ___block_literal_global.66
- ___block_literal_global.95
- ___getLNSpotlightAppEntityMapperClass_block_invoke
- ___getLNSpotlightAppEntityMapperClass_block_invoke.cold.1
- ___getLNSpotlightAppEntityMapperClass_block_invoke.cold.2
- __sl_dlopen
- _audit_stringLinkServices
- _getLNSpotlightAppEntityMapperClass.softClass
- _kVMLogCategoryLockScreen
- _notify_post
- _notify_register_check
- _notify_set_state
- _objc_getAssociatedObject
- _objc_getClass
- _objc_msgSend$AVAssetAuthoringMetadataWithComposition:
- _objc_msgSend$_compositionByReplacingDecomposedFragments:
- _objc_msgSend$_eaccess_repairDecomposedFragmentMetadataIfNecessary:
- _objc_msgSend$_fileNameForSharing
- _objc_msgSend$addTimer:forMode:
- _objc_msgSend$cancelExport
- _objc_msgSend$closeAudioFile:completionBlock:
- _objc_msgSend$composedAssetIsM4a
- _objc_msgSend$compositionAVURL
- _objc_msgSend$compositionAssetForExport:
- _objc_msgSend$fileToken
- _objc_msgSend$initWithComposition:
- _objc_msgSend$lowercaseString
- _objc_msgSend$mainRunLoop
- _objc_msgSend$openAudioFile:settings:metadata:accessRequestHandler:
- _objc_msgSend$progress
- _objc_msgSend$rc_path:isSubpathOf:
- _objc_msgSend$rc_setComposedAVURL:
- _objc_msgSend$setComposedAVURL:
- _objc_msgSend$setFileToken:
- _objc_msgSend$setSyncedAudioFuture:sourceFileURL:
- _objc_msgSend$timerWithTimeInterval:repeats:block:
- _objc_msgSend$writeAudioFile:buffer:completionBlock:
- _objc_msgSend$writeCompositionWithCompletionBlock:
- _objc_setAssociatedObject
CStrings:
+ "#"
+ "%K == nil && %K == nil && %K == nil"
+ "%s -- Attempted to call [RCMutableMovie movieWithURL:] with nil url"
+ "%s -- Attempting to save potentially corrupted waveform."
+ "%s -- Cannot update metadata for cloudrecording with nil url"
+ "%s -- ERROR: Attempt to load model into NSManagedObjectModel failed, possibly due to file handle exhaustion...."
+ "%s -- Exported from iCloud successfully, num ids = %d"
+ "%s -- Failed to access secure url for recording with UUID %@"
+ "%s -- Failed to create directory, error = %@"
+ "%s -- Failed to create sample buffer, error: %@"
+ "%s -- Failed to export recording UUIDs, error = %@"
+ "%s -- Failed to fetch metadata for recordin with UUID %@, error = %@"
+ "%s -- Failed to fetch metadata for recording with, error = %@"
+ "%s -- Failed to get recording with Id %@"
+ "%s -- Failed to remove sharing metadata for recording %@. Error: %@."
+ "%s -- Fetched Recording metadata successfully"
+ "%s -- Inconsistency detected - audioFuture: %{public}@, mtAudioFuture: %{public}@, versionedAudioFuture: %{public}@"
+ "%s -- Incorrect file extension for multi layer voice memo. Changing from %@ to %@."
+ "%s -- Invalid format ranking: %ld"
+ "%s -- Invalid format: %i"
+ "%s -- No metadata present in userinfo %@"
+ "%s -- Sending service request to fetchRecordingUUIDsForExport"
+ "%s -- Sending service request to sizeOfRecordingsForExport"
+ "+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:completionHandler:]_block_invoke"
+ "+[RCSavedRecordingsModel(ExportAdditions) fetchRecordingUUIDsForExport:]"
+ "+[RCSavedRecordingsModel(ImportAdditions) importFileWithURL:shouldUseMetadataTitle:completionHandler:]_block_invoke_2"
+ "-[AVAsset(RCAdditions) createExportSettingsForSampleRate:channelCount:formatRanking:]"
+ "-[AVAsset(RCAdditions) rc_exportFormat]"
+ "-[RCCloudRecording _copyResourceFromLocation:toDirectory:usingName:andExtension:]"
+ "-[RCCloudRecording fileNameForSharing]"
+ "-[RCCloudRecording(SyncedProperties) setSyncedAudioFuture:sourceFileURL:containsSpatialAudio:]"
+ "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]"
+ "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke"
+ "-[RCSSavedRecordingService fetchMetadataForRecordingWithUUID:completionBlock:]_block_invoke_2"
+ "-[RCSSavedRecordingService fetchRecordingUUIDsForExport:]"
+ "-[RCSSavedRecordingService fetchRecordingUUIDsForExport:]_block_invoke"
+ "-[RCSSavedRecordingService fetchRecordingUUIDsForExport:]_block_invoke_2"
+ "-[RCSSavedRecordingService sizeOfRecordingsForExport:]"
+ "-[RCSSavedRecordingService sizeOfRecordingsForExport:]_block_invoke"
+ "-[RCSSavedRecordingService sizeOfRecordingsForExport:]_block_invoke_2"
+ "-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]"
+ "-[RCSavedRecordingsModel _postProcessCloudRecordingForRecordingWithId:named:userInfo:isMigrationImport:isMusicMemoImport:sharingMetadata:]"
+ "-[RCSpatialAsset _metadataGroupFor:]"
+ ".ImportFilesTemporaryDirectory"
+ "@\"AVAssetTrack\""
+ "@\"AVTimedMetadataGroup\""
+ "@\"NSArray\"16@?0@\"AVCompositionTrack\"8"
+ "@\"NSNumber\""
+ "@\"NSSecurityScopedURLWrapper\""
+ "@\"NSURL\"16@?0@\"RCCompositionFragment\"8"
+ "@\"TranscriptionMetadata\""
+ "@16@?0@\"AVCompositionTrackSegment\"8"
+ "@20@0:8f16"
+ "@28@0:8@16f24"
+ "@36@0:8d16I24q28"
+ "AirPodsStudioVoiceMic"
+ "AudioAccessoryFeatures"
+ "B24@0:8^{opaqueCMFormatDescription=}16"
+ "B24@?0@\"AVMetadataItem\"8@\"NSDictionary\"16"
+ "Capture"
+ "CaptureRecovery"
+ "ExportAdditions"
+ "ImportAdditions"
+ "RCCaptureDirectoryURL_block_invoke"
+ "RCCaptureRecoveryDirectoryURL_block_invoke"
+ "RCSpatialAsset"
+ "RCVoiceMemoMetadata"
+ "RCVoiceMemoMetadataKey"
+ "RCVoiceMemosChannelConfigurationKey"
+ "SpatialAudioCapture"
+ "T@\"AVAsset\",R,N,V_asset"
+ "T@\"AVAssetTrack\",R,N,V_fallbackTrack"
+ "T@\"AVAssetTrack\",R,N,V_overdubTrack"
+ "T@\"AVAssetTrack\",R,N,V_spatialTrack"
+ "T@\"AVTimedMetadataGroup\",R,N,V_spatialMetadataGroup"
+ "T@\"NSArray\",&,N,V_utterances"
+ "T@\"NSNumber\",&,N,V_channelCount"
+ "T@\"NSNumber\",&,N,V_creationTimeMillis"
+ "T@\"NSNumber\",&,N,V_deletionTimeMillis"
+ "T@\"NSNumber\",&,N,V_durationMillis"
+ "T@\"NSNumber\",&,N,V_enhanced"
+ "T@\"NSNumber\",&,N,V_favorite"
+ "T@\"NSNumber\",&,N,V_multiLayer"
+ "T@\"NSNumber\",&,N,V_multiLayerMix"
+ "T@\"NSNumber\",&,N,V_offsetMillis"
+ "T@\"NSNumber\",&,N,V_onsetMillis"
+ "T@\"NSNumber\",&,N,V_recordedOnWatch"
+ "T@\"NSNumber\",&,N,V_sampleRate"
+ "T@\"NSSecurityScopedURLWrapper\",&,N,V_wrappedURL"
+ "T@\"NSString\",&,N,V_codec"
+ "T@\"NSString\",&,N,V_folder"
+ "T@\"NSString\",&,N,V_path"
+ "T@\"NSString\",C,N,V_formattedString"
+ "T@\"NSString\",C,N,V_language"
+ "T@\"NSString\",C,N,V_rawString"
+ "T@\"NSString\",C,N,V_title"
+ "T@\"TranscriptionMetadata\",&,N,V_transcription"
+ "TB,N,V_cachedHasSpatialAudio"
+ "TB,V_potentiallyCorrupted"
+ "TranscriptionMetadata"
+ "UtteranceMetaData"
+ "VoiceMemos14.mom"
+ "Vv24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"RCVoiceMemoMetadata\"@\"NSError\">24"
+ "_associatedTrackOfType:forTrack:"
+ "_cachedHasSpatialAudio"
+ "_cachedValueForHasSpatialAudioIsValid"
+ "_channelCount"
+ "_codec"
+ "_copyFileIntoImportFilesTemporaryDirectory:error:"
+ "_copyResourceFromLocation:toDirectory:usingName:andExtension:"
+ "_creationTimeMillis"
+ "_deletionTimeMillis"
+ "_descriptionIsSpatial:"
+ "_durationMillis"
+ "_enhanced"
+ "_fallbackTrack"
+ "_favorite"
+ "_findOverdubTrack"
+ "_findSpatialMetadataGroup"
+ "_findSpatialTrack"
+ "_folder"
+ "_formattedString"
+ "_isSpatialTrack:"
+ "_language"
+ "_markedAsFinished"
+ "_metadataGroupFor:"
+ "_multiLayer"
+ "_multiLayerMix"
+ "_offsetMillis"
+ "_onsetMillis"
+ "_overdubTrack"
+ "_path"
+ "_postProcessCloudRecordingForRecordingWithId:named:userInfo:isMigrationImport:isMusicMemoImport:sharingMetadata:"
+ "_potentiallyCorrupted"
+ "_rawString"
+ "_rc_all_audioTracks"
+ "_recordedOnWatch"
+ "_scaledIntFromFloat:"
+ "_spatialMetadataGroup"
+ "_spatialTrack"
+ "_transcription"
+ "_updateCachedValueForHasSpatialAudio"
+ "_utterances"
+ "_wrappedURL"
+ "asset"
+ "associatedTracksOfType:"
+ "audioFutureFlags"
+ "audioFutureVersionIsCompatible"
+ "cachedHasSpatialAudio"
+ "canUpdateWithSpatialAsset"
+ "codec"
+ "com.apple.iTunes.voice-memo-lrmx"
+ "com.apple.iTunes.voice-memo-nhnc"
+ "com.apple.iTunes.voice-memo-plrt"
+ "com.apple.iTunes.voice-memo-sivl"
+ "com.apple.iTunes.voice-memo-skps"
+ "composedAssetIsSpatialRecording"
+ "createExportSettingsForSampleRate:channelCount:formatRanking:"
+ "createSampleBufferForRequest:error:"
+ "creationTimeMillis"
+ "currentPlatform"
+ "dateWithTimeIntervalSince1970:"
+ "deletionTimeMillis"
+ "dictionaryWithObject:forKey:"
+ "durationMillis"
+ "f20@0:8i16"
+ "fallbackTrack"
+ "family"
+ "fetchMetadataForRecordingWithUUID:completionBlock:"
+ "fetchMetadataForRecordingWithUUID:completionHandler:"
+ "fetchRecordingUUIDsForExport:"
+ "fileNameForSharing"
+ "filterUsingPredicate:"
+ "finishWritingWithError:"
+ "formattedString"
+ "hasSpatialAudio"
+ "importFileWithURL:shouldUseMetadataTitle:completionHandler:"
+ "importFileWithURL:withMetadata:completionHandler:"
+ "initWithAsset:"
+ "initWithAsset:timebase:"
+ "initWithSampleBuffer:"
+ "initWithStartCursor:"
+ "isSkipSilenceEnabled"
+ "isSpeechIsolatorEnabled"
+ "items"
+ "key"
+ "language"
+ "mainDevice"
+ "makeSampleCursorWithPresentationTimeStamp:"
+ "markWaveformPotentiallyCorrupted"
+ "mdta/com.apple.quicktime.cinematic-audio"
+ "mediaType"
+ "mergeCaptureFragment.plist"
+ "mergeCaptureFragmentMetadataURLForComposedAVURL:"
+ "metadata cannot be nil"
+ "migratePlaybackSettings"
+ "multiLayer"
+ "multiLayerMix"
+ "na_any:"
+ "na_flatMap:"
+ "non-nil"
+ "offsetMillis"
+ "onsetMillis"
+ "overdubTrack"
+ "performBlockAndWaitWithBackgroundModel:"
+ "performBlockWithBackgroundModel:"
+ "playRate"
+ "playableRecordingsExcludingDeletedPredicate"
+ "playbackSpeed"
+ "potentiallyCorrupted"
+ "predicateWithBlock:"
+ "rawString"
+ "rc_audioTracksPreferringSpatial"
+ "rc_channelConfiguration"
+ "rc_createSharingMetadataItemForKey:andValue:"
+ "rc_exportFormat"
+ "rc_hasSpatialTracks"
+ "rc_path:isChildOf:"
+ "rc_setChannelConfiguration:"
+ "rc_sharingMetadata"
+ "rc_trackIsSpatial:"
+ "rc_unscaleScaledMetadataValue:"
+ "rc_v14ObjectModel"
+ "setAudioFutureFlags:"
+ "setCachedHasSpatialAudio:"
+ "setChannelCount:"
+ "setCodec:"
+ "setComposedAssetIsSpatialRecording:"
+ "setCreationTimeMillis:"
+ "setDeletionTimeMillis:"
+ "setDirection:"
+ "setDurationMillis:"
+ "setFolder:"
+ "setFormattedString:"
+ "setIsSkipSilenceEnabled:"
+ "setIsSpeechIsolatorEnabled:"
+ "setLanguage:"
+ "setMaxSampleCount:"
+ "setMultiLayer:"
+ "setMultiLayerMix:"
+ "setOffsetMillis:"
+ "setOnsetMillis:"
+ "setPlayRate:"
+ "setPlaybackSpeed:"
+ "setPotentiallyCorrupted:"
+ "setPreferredMinSampleCount:"
+ "setRawString:"
+ "setSampleRate:"
+ "setSkipSilenceEnabled:"
+ "setSpeechIsolatorValue:"
+ "setStudioMixEnabled:"
+ "setStudioMixLevel:"
+ "setSyncedAudioFuture:sourceFileURL:containsSpatialAudio:"
+ "setTranscription:"
+ "setUtterances:"
+ "setVersionedAudioFuture:"
+ "setWrappedURL:"
+ "sizeOfRecordingsForExport:"
+ "skipSilenceEnabled"
+ "sourceURL"
+ "spatialMetadataGroup"
+ "spatialTrack"
+ "speechIsolatorValue"
+ "stringByDeletingLastPathComponent"
+ "studioMixEnabled"
+ "studioMixLevel"
+ "supportsANE"
+ "trackID"
+ "tracks"
+ "transcription"
+ "utterances"
+ "v16@?0q8"
+ "v24@?0@\"<RCSSavedRecordingServiceProtocol>\"8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@?0@\"<RCSSavedRecordingServiceProtocol>\"8@?<v@?@\"RCVoiceMemoMetadata\"@\"NSError\">16"
+ "v24@?0@\"RCVoiceMemoMetadata\"8@\"NSError\"16"
+ "v32@?0@\"NSManagedObjectID\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v36@0:8@16@24B32"
+ "v56@0:8@16@24@32B40B44@48"
+ "versionedAudioFuture"
+ "wrappedURL"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"
- "$"
- "%K == nil"
- "%K == nil && %K == nil"
- "%s"
- "%s -- ERROR:  could not open fragment URL = %@"
- "%s -- ERROR: Attempt to load model into NSManagedObjectModel failed, possibly due to file handle exhaustion..."
- "%s -- ERROR: Unable to compose recording - _exportSession = %@, underlying error = %@"
- "%s -- ERROR: Unable to compose recording - there was a problem determining export settings"
- "%s -- ERROR: Unable to create temporary directory URLForDirectory error = %@"
- "%s -- ERROR: moveError = %@"
- "%s -- Export session produced file with no audio tracks"
- "%s -- Sending service request to close audio file: %@"
- "%s -- Sending service request to open audio file %@"
- "%s -- Writing to %s while %s is non-nil!"
- "-[RCCloudRecording _fileNameForSharing]"
- "-[RCCloudRecording(SyncedProperties) setSyncedAudioFuture:sourceFileURL:]"
- "-[RCComposition _eaccess_repairDecomposedFragmentMetadataIfNecessary:]_block_invoke"
- "-[RCComposition rcs_composeToFinalDestinationWithCompletionBlock:]_block_invoke_2"
- "-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]"
- "-[RCCompositionComposedAssetWriter writeCompositionWithCompletionBlock:]_block_invoke"
- "-[RCSSavedRecordingService closeAudioFile:completionBlock:]"
- "-[RCSSavedRecordingService closeAudioFile:error:]"
- "-[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:]"
- "-[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:]_block_invoke"
- "-[RCSSavedRecordingService openAudioFile:settings:metadata:accessRequestHandler:]_block_invoke_2"
- "-[RCSSavedRecordingService openAudioFile:settings:metadata:error:]_block_invoke"
- "@\"AVAssetExportSession\""
- "@\"AVAudioFormat\"16@0:8"
- "@\"NSURL\"16@0:8"
- "@\"RCSSavedRecordingAccessToken\""
- "@48@0:8@16@24@32^@40"
- "Class getLNSpotlightAppEntityMapperClass(void)_block_invoke"
- "D9"
- "HWModelStr"
- "LNSpotlightAppEntityMapper"
- "LockScreen"
- "No audio tracks after export"
- "OverdubRecording"
- "RCCompositionComposedAssetWriter"
- "RCSAudioFile"
- "RCSUserInfo"
- "RCSavedRecording+SpotlightAdditions.m"
- "RCSlowComposeDelay"
- "RCTestAlwaysShowLockScreenPlugin"
- "SaveAsNew"
- "T@\"AVAudioFormat\",R,N"
- "T@\"NSDictionary\",R,C,N,V_userInfo"
- "T@\"NSURL\",&,N,Src_setComposedAVURL:"
- "T@\"RCSSavedRecordingAccessToken\",&,N,V_fileToken"
- "UIApplicationWillTerminateNotification"
- "Unable to find class %s"
- "Vv40@0:8@\"NSURL\"16@\"AVAudioPCMBuffer\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@16@24@?32"
- "Vv48@0:8@\"NSURL\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"RCSSavedRecordingAccessToken\"@\"NSError\">40"
- "_AVAssetRCComposedAVURLKey"
- "_RCSAudioFile"
- "_compositionByReplacingDecomposedFragments:"
- "_eaccess_repairDecomposedFragmentMetadataIfNecessary:"
- "_exportSession"
- "_fileNameForSharing"
- "_fileToken"
- "_userInfo"
- "addTimer:forMode:"
- "audioFile"
- "cancel"
- "cancelExport"
- "closeAudioFile:completionBlock:"
- "closeAudioFile:error:"
- "composedAssetIsM4a"
- "fileToken"
- "initWithComposition:"
- "lowercaseString"
- "mainRunLoop"
- "openAudioFile:settings:metadata:accessRequestHandler:"
- "openAudioFile:settings:metadata:error:"
- "outputFragment"
- "progress"
- "rc_composedAVURL"
- "rc_path:isSubpathOf:"
- "rc_setComposedAVURL:"
- "rcs_composeToFinalDestinationWithCompletionBlock:"
- "rcs_repairDecomposedFragmentMetadataIfNecessary:"
- "setFileToken:"
- "setSyncedAudioFuture:sourceFileURL:"
- "setUserInfo:"
- "softlink:o:path:/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices"
- "timerWithTimeInterval:repeats:block:"
- "v16@?0@\"NSTimer\"8"
- "v20@?0@\"RCComposition\"8B16"
- "void *LinkServicesLibrary(void)"
- "willMigrateFromM4aToQta"
- "writeAudioFile:buffer:completionBlock:"
- "writeCompositionWithCompletionBlock:"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}"

```
