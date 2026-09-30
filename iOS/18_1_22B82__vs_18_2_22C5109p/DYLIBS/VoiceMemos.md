## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1238.3.0.0.0
-  __TEXT.__text: 0x4281c
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x3308
-  __TEXT.__gcc_except_tab: 0x1940
-  __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x5bba
-  __TEXT.__oslogstring: 0x2640
+1242.1.0.0.0
+  __TEXT.__text: 0x45558
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x3568
+  __TEXT.__gcc_except_tab: 0x1a00
+  __TEXT.__const: 0x1e8
+  __TEXT.__cstring: 0x5e5a
+  __TEXT.__oslogstring: 0x277c
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1728
-  __TEXT.__objc_classname: 0x79c
-  __TEXT.__objc_methname: 0xaa7e
-  __TEXT.__objc_methtype: 0x148b
-  __TEXT.__objc_stubs: 0x7f60
-  __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x1bb0
-  __DATA_CONST.__objc_classlist: 0x198
-  __DATA_CONST.__objc_catlist: 0x90
+  __TEXT.__unwind_info: 0x1810
+  __TEXT.__objc_classname: 0x801
+  __TEXT.__objc_methname: 0xb1ec
+  __TEXT.__objc_methtype: 0x1573
+  __TEXT.__objc_stubs: 0x85c0
+  __DATA_CONST.__got: 0x638
+  __DATA_CONST.__const: 0x1ce8
+  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2890
+  __DATA_CONST.__objc_selrefs: 0x2aa8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x130
-  __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x608
+  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_arraydata: 0xd8
+  __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x3020
-  __AUTH_CONST.__objc_const: 0x5b90
+  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__cfstring: 0x30a0
+  __AUTH_CONST.__objc_const: 0x60b0
+  __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x290
-  __DATA.__data: 0x7f8
-  __DATA.__bss: 0x168
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x2c0
+  __DATA.__data: 0x7f0
+  __DATA.__bss: 0x188
   __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1688
-  Symbols:   2227
-  CStrings:  2773
+  Functions: 1752
+  Symbols:   2323
+  CStrings:  2894
 
Symbols:
+ _AVAudioSessionCategoryPlayAndRecord
+ _AVAudioSessionCategoryPlayback
+ _AVAudioSessionModeDefault
+ _AVFileTypeQuickTimeMovie
+ _AVLinearPCMBitDepthKey
+ _AVLinearPCMIsFloatKey
+ _AVMetadataKeySpaceQuickTimeMetadata
+ _AVSampleRateKey
+ _CMFormatDescriptionGetMediaSubType
+ _CMSampleBufferGetDuration
+ _CMSampleBufferGetNumSamples
+ _OBJC_CLASS_$_AVAssetReader
+ _OBJC_CLASS_$_AVAssetReaderAudioMixOutput
+ _OBJC_CLASS_$_AVAssetTrack
+ _OBJC_CLASS_$_AVAudioSession
+ _OBJC_CLASS_$_AVAudioTime
+ _OBJC_CLASS_$_AVMovie
+ _OBJC_CLASS_$_AVMutableAudioMix
+ _OBJC_CLASS_$_AVMutableAudioMixInputParameters
+ _OBJC_CLASS_$_NSEnumerator
+ _OBJC_CLASS_$_NSItemProvider
+ _OBJC_METACLASS_$_AVMutableMovie
+ _OBJC_METACLASS_$_NSEnumerator
+ _RCAudioFileExtensionForConvertingOnImport
+ _RCAudioFileExtensionForIntermediateCapture
+ _RCAudioFileExtensionM4A
+ _RCAudioFileExtensionQT
+ _RCAudioFileExtensionQTA
+ _RCCloudRecording_MtAudioFuture
+ _RCComputeAudioFileDigest
+ _RCGetAudioConfiguration
+ _RCOverdubRecordingFeatureFlagIsEnabled
+ _RCOverdubRecordingIsEnabled
+ _RCTranscribeAllAudioTracks
+ ___assert_rtn
+ _close
+ _fstat
+ _kCMTimePositiveInfinity
+ _lseek
+ _open
+ _read
- _AudioFileClose
- _AudioFileOpenURL
- _AudioFileReadBytes
- _RCTestAudioTrimmingProgressWithDuration
- _RCTestEditInTrimSheetAllowed
- _RCTestEditInTrimSheetAllowedGetDefaultOption
- _RCTestEditInTrimSheetAllowedSetDefaultOption
- _RCTestRunningAutomatedUITests
CStrings:
+ "\x01!\x11\x12"
+ "\x011"
+ "\x12%!\(MISSING)xf0!"
+ "%!@(MISSING) AVURL = %!@(MISSING) (waveformURL = %!@(MISSING)), contentDuration = %!@(MISSING), timeRangeInContentToUse = %!@(MISSING), timeRangeInComposition = %!@(MISSING), trackIndex = %!@(MISSING)"
+ "%!@(MISSING) savedRecordingUUID = %!@(MISSING), AVURL = %!@(MISSING) (waveformURLs = %!@(MISSING)), composedDuration = %!@(MISSING), _decomposedFragments = %!@(MISSING)"
+ "%!K(MISSING) == nil && %!K(MISSING) == nil"
+ "%!s(MISSING) -- AVAssetReader Error = %!@(MISSING)"
+ "%!s(MISSING) -- Audio Future was set to nil during synchronizeWithExistingAudioFuture"
+ "%!s(MISSING) -- Failed to load playable asset for URL: %!@(MISSING)"
+ "%!s(MISSING) -- Unknown atom type = 0x%!X(MISSING)"
+ "%!s(MISSING) -- Writing to %!s(MISSING) while %!s(MISSING) is non-nil!"
+ "%!s(MISSING) -- assetReader can not add readerOutput"
+ "%!s(MISSING) -- audioAsset = nil"
+ "%!s(MISSING) -- readerOutput = nil"
+ "%!s(MISSING) -- writeMovieHeaderToURL error = %!@(MISSING)"
+ "+[AVAsset(RCAdditions) rc_updateFile:withTranscriptionData:error:]"
+ "+[RCCaptureFormat _AVAssetExportDetermineSettingsForExportingAsset:outputExtensionWithFallbacks:preferredFormat:completionHandler:]"
+ "+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:]"
+ "+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:]_block_invoke"
+ "-[AVAudioPCMBuffer(RCAdditions) trimmedBuffer:]"
+ "-[NSFileManager(RCAdditions) rc_cleanUpAssetsInDirectory:]"
+ "-[NSFileManager(RCAdditions) rc_cleanUpAssetsInDirectory:]_block_invoke"
+ "-[RCCloudRecording _updateFlagsDerivedFromComposedAsset:]"
+ "-[RCCloudRecording(SyncedProperties) setSyncedAudioFuture:hasMultipleTracks:]"
+ "-[RCComposition _calculateComposedAVURLDerivedValues]"
+ "-[RCComposition newRandomFragmentWithInsertionTimeRangeInComposition:trackIndex:pathExtension:]"
+ "-[RCComposition rcs_composeToFinalDestinationWithCompletionBlock:]_block_invoke_2"
+ "-[RCComposition(RCAVFoundation) _compositionAsset:]"
+ "-overview"
+ "-track%!l(MISSING)u"
+ "@\"AVAssetReader\""
+ "@\"AVAssetReaderAudioMixOutput\""
+ "@\"AVMutableCompositionTrack\"16@?0Q8"
+ "@\"AVURLAsset\"16@?0@\"NSURL\"8"
+ "@16@?0@\"AVAssetTrack\"8"
+ "@16@?0@\"NSString\"8"
+ "@20@0:8I16"
+ "@32@0:8d16Q24"
+ "@40@0:8@16d24^@32"
+ "@44@0:8@16B24d28Q36"
+ "@48@0:8@16@24d32^@40"
+ "@48@0:8{?=dd}16Q32@40"
+ "@72@0:8@16d24{?=dd}32{?=dd}48Q64"
+ "AVAsset reader failed to read audio track samples."
+ "AVAssetExportDetermineSettingsForExportingAsset:preferredOutputExtension:preferredFormat:completionHandler:"
+ "AVAudioPCMBuffer+RCAdditions.m"
+ "AVFileTypeIdentifierForFileExtension:"
+ "B16@?0@\"NSString\"8"
+ "B16@?0@\"RCCompositionFragment\"8"
+ "B32@0:8Q16^@24"
+ "B56@0:8{_RCAudioSessionConfiguration=@@QQ}16^@48"
+ "B96@?0Q8@\"AVAssetTrack\"16{?={?=qiIq}{?=qiIq}}24{?=qiIq}72"
+ "FragmentFiltering"
+ "I"
+ "OverdubRecording"
+ "PrivateSyncedProperties"
+ "RCAudioBufferEnumerator"
+ "RCAudioSessionConfiguration"
+ "RCEnableOverdubForAllDevices"
+ "RCMutableMovie"
+ "RCTrackIndex"
+ "T@\"<_NSFileBackedFuture>\",R,N"
+ "T@\"NSURL\",&,N,V_composedAVURL"
+ "T@\"NSURL\",&,N,V_linkURL"
+ "TB,N,V_cachedComposedAVURLDerivedValuesAreValid"
+ "TB,N,V_cachedHasMultipleTracks"
+ "TB,N,V_hasMultipleTracks"
+ "TQ,N,V_trackIndex"
+ "TemporaryMovieLink"
+ "Tf,N"
+ "TranscribeAllAudioTracks"
+ "VoiceMemos13.mom"
+ "W\x11"
+ "[2{?=\"beginTime\"d\"endTime\"d}]"
+ "_AVAssetExportDetermineSettingsForExportingAsset:outputExtensionWithFallbacks:preferredFormat:completionHandler:"
+ "_activeAsset"
+ "_asset"
+ "_assetReader"
+ "_cachedComposedAVURLDerivedValuesAreValid"
+ "_cachedHasMultipleTracks"
+ "_cachedTrackRanges"
+ "_calculateComposedAVURLDerivedValues"
+ "_compositionAsset:"
+ "_determineImportabilityOfRecordingWithAudioAsset:preferredFormat:completionHandler:"
+ "_enumerateTracksForInsertion:"
+ "_hasMultipleTracks"
+ "_linkURL"
+ "_mdatAudioDigest"
+ "_mixerOutput"
+ "_trackIndex"
+ "_updateFlagsDerivedFromComposedAsset:"
+ "addOutput:"
+ "assetReaderAudioMixOutputWithAudioTracks:audioSettings:"
+ "audioMixInputParametersWithTrack:"
+ "bufferEnumerator:startTime:error:"
+ "cachedComposedAVURLDerivedValuesAreValid"
+ "cachedHasMultipleTracks"
+ "canAddOutput:"
+ "canUpdateWithMultiTrackAsset"
+ "cancelReading"
+ "com.apple.VoiceMemos.tsrp"
+ "composedAssetHasMultipleTracks"
+ "composedTimeRangeForTrackIndex:"
+ "composedWaveformURLForTrackIndex:"
+ "composedWaveformURLs"
+ "compositionWithURLAssetInitializationOptions:"
+ "copyNextSampleBuffer"
+ "destBuffer->mDataByteSize == (sourceBuffer->mDataByteSize - frameCountByteOffset)"
+ "enableOverdubForAllDevices"
+ "extrapolateTimeFromAnchor:"
+ "fileExtension"
+ "filePathForSyncingFromExistingAudioFuture"
+ "floatValue"
+ "fragmentsWithTrackIndex:"
+ "hasItemConformingToTypeIdentifier:"
+ "hasMultipleTracks"
+ "hostTime"
+ "initWithAVFileURL:savesGeneratedWaveform:segmentFlushInterval:trackIndex:"
+ "initWithAVFileURL:trackIndex:"
+ "initWithAVOutputURL:contentDuration:timeRangeInContentToUse:timeRangeInComposition:trackIndex:"
+ "initWithAsset:error:"
+ "initWithComposition:processingFormat:startTime:error:"
+ "initWithComposition:trackIndex:"
+ "initWithDestinationComposition:destinationFragment:trackIndex:"
+ "initWithPCMFormat:bufferListNoCopy:deallocator:"
+ "initWithSamplingParametersFromGenerator:trackIndex:"
+ "initWithSegmentFlushInterval:trackIndex:"
+ "initWithSourceComposition:destinationWaveformURL:trackIndex:"
+ "initWithWaveformGenerator:generatedWaveformOutputURL:trackIndex:"
+ "isEchoCancelledInputAvailable"
+ "isPlayable"
+ "keyForIdentifier:"
+ "keySpaceForIdentifier:"
+ "layerMix"
+ "linkItemAtURL:toURL:error:"
+ "linkURL"
+ "markConfigurationAsFinal"
+ "metadataItemsFromArray:filteredByIdentifier:"
+ "movieWithURL:error:"
+ "mtAudioFuture"
+ "mtLayerMix"
+ "newRandomFragmentWithInsertionTimeRangeInComposition:trackIndex:pathExtension:"
+ "numberWithFloat:"
+ "qt"
+ "qta"
+ "rc_URLByAppendingStringToLastComponentBasename:replacingPathExtension:"
+ "rc_adjustedBySamples:"
+ "rc_adjustedBySeconds:"
+ "rc_cleanUpAssetsInDirectory:"
+ "rc_configureSession:error:"
+ "rc_hostTimeInSeconds"
+ "rc_supportedFileTypesRepresented"
+ "rc_timeRange"
+ "rc_transcriptionDataForURL:"
+ "rc_v13ObjectModel"
+ "rc_writeMovieHeaderWithOptions:error:"
+ "recacheAVURLDerivedValues"
+ "sampleTime"
+ "secondsForHostTime:"
+ "setAlwaysCopiesSampleData:"
+ "setAudioMix:"
+ "setCachedComposedAVURLDerivedValuesAreValid:"
+ "setCachedHasMultipleTracks:"
+ "setCategory:mode:routeSharingPolicy:options:error:"
+ "setComposedAVURL:"
+ "setComposedAssetHasMultipleTracks:"
+ "setHasMultipleTracks:"
+ "setInputParameters:"
+ "setLayerMix:"
+ "setLinkURL:"
+ "setMtAudioFuture:"
+ "setMtLayerMix:"
+ "setSyncedAudioFuture:hasMultipleTracks:"
+ "setTimeRange:"
+ "setTrackIndex:"
+ "setVolume:atTime:"
+ "setWithObjects:count:"
+ "standardPathForRecordingWithCreationDate:uniqueID:fileExtension:"
+ "standardURLForRecordingWithCreationDate:fileExtension:"
+ "startReading"
+ "supportedFileTypeIdentifiers"
+ "supportsFileExtension:"
+ "supportsLiveInput"
+ "temporaryMovieLink:"
+ "timeWithSampleTime:atRate:"
+ "trackIndex"
+ "trimmedBuffer:"
+ "unsignedIntegerValue"
+ "v16@?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8"
+ "v44@0:8@16@24I32@?36"
+ "waveformURLForAVURL:trackIndex:"
+ "{?=dd}24@0:8Q16"
- "\x01!"
- "\x01!\x13"
- "\x12$\xf0!"
- "\x18\x11"
- "%!@(MISSING) AVURL = %!@(MISSING) (waveformURL = %!@(MISSING)), contentDuration = %!@(MISSING), timeRangeInContentToUse = %!@(MISSING), timeRangeInComposition = %!@(MISSING)"
- "%!@(MISSING) savedRecordingUUID = %!@(MISSING), AVURL = %!@(MISSING) (waveformURL = %!@(MISSING)), composedDuration = %!@(MISSING), _decomposedFragments = %!@(MISSING)"
- "%!s(MISSING) -- audioError = %!@(MISSING)"
- "%!s(MISSING) -- readError = %!@(MISSING)"
- "+[RCCaptureFormat _AVAssetExportDetermineSettingsForExportingAsset:inputFormat:outputExtensionWithFallbacks:preferredFormat:completionHandler:]"
- "+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioFile:preferredFormat:completionHandler:]"
- "+[RCSavedRecordingsModel _determineImportabilityOfRecordingWithAudioFile:preferredFormat:completionHandler:]_block_invoke"
- "+[RCSavedRecordingsModel _moveFileIntoRecordingsDirectory:]"
- "-[NSFileManager(RCAdditions) rc_cleanUpM4AsInDirectory:]"
- "-[NSFileManager(RCAdditions) rc_cleanUpM4AsInDirectory:]_block_invoke"
- "-[RCCloudRecording _updateTranscriptionAvailabilityFlags:]"
- "-[RCComposition _composedDuration]"
- "-[RCComposition newRandomFragmentWithInsertionTimeRangeInComposition:pathExtension:]"
- "-[RCComposition(RCAVFoundation) _compositionAsset:error:]"
- "@28@0:8B16^@20"
- "@36@0:8@16B24d28"
- "@64@0:8@16d24{?=dd}32{?=dd}48"
- "AVAssetExportDetermineSettingsForExportingAsset:inputFormat:preferredOutputExtension:preferredFormat:completionHandler:"
- "AVFileTypeUTIForFileExtension:"
- "B88@?0@\"AVURLAsset\"8{?={?=qiIq}{?=qiIq}}16{?=qiIq}64"
- "RCComposedWaveformURL"
- "RCCompositionComposedAssetWriter.m"
- "RCTestAudioTrimmingProgressWithDuration"
- "RCTestEditInTrimSheetAllowed"
- "RCTestRunningAutomatedUITests"
- "T@\"<_NSFileBackedFuture>\",&,N"
- "T@\"NSURL\",R,N,V_composedAVURL"
- "T@\"NSURL\",R,N,V_composedWaveformURL"
- "TB,N,V_cachedComposedAVURLDurationIsValid"
- "URLAssetWithURL:options:"
- "UnencryptedSyncedProperties"
- "_AVAssetExportDetermineSettingsForExportingAsset:inputFormat:outputExtensionWithFallbacks:preferredFormat:completionHandler:"
- "_cachedComposedAVURLDurationIsValid"
- "_composedWaveformURL"
- "_compositionAsset:error:"
- "_determineImportabilityOfRecordingWithAudioFile:preferredFormat:completionHandler:"
- "_enumerateFragmentsForInsertion:"
- "_moveFileIntoRecordingsDirectory:"
- "_updateTranscriptionAvailabilityFlags:"
- "cachedComposedAVURLDurationIsValid"
- "composedWaveformURL"
- "fileExtensionForAssetExport"
- "fileExtensionForIntermediateAssetCapture"
- "fileFormatsDirectlyImportable"
- "initForReading:commonFormat:interleaved:error:"
- "initForReading:error:"
- "initWithAVFileURL:"
- "initWithAVFileURL:savesGeneratedWaveform:segmentFlushInterval:"
- "initWithAVOutputURL:contentDuration:timeRangeInContentToUse:timeRangeInComposition:"
- "initWithDestinationComposition:destinationFragment:"
- "initWithSamplingParametersFromGenerator:"
- "initWithSegmentFlushInterval:"
- "initWithSourceComposition:destinationWaveformURL:"
- "initWithWaveformGenerator:generatedWaveformOutputURL:"
- "insertTimeRange:ofAsset:atTime:error:"
- "mov"
- "mp3"
- "newRandomFragmentWithInsertionTimeRangeInComposition:pathExtension:"
- "rc_cleanUpM4AsInDirectory:"
- "readIntoBuffer:error:"
- "recacheComposedDuration"
- "setCachedComposedAVURLDurationIsValid:"
- "setSyncedAudioFuture:"
- "standardPathForRecording:"
- "standardPathForRecordingWithCreationDate:uniqueID:"
- "standardURLForRecordingWithCreationDate:"
- "v48@0:8@16I24@28I36@?40"
- "waveformURLForAVURL:"

```
