## MOVStreamIO

> `/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO`

```diff

-3.21.0.0.0
-  __TEXT.__text: 0x40f2c
-  __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x31e4
-  __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x44ea
-  __TEXT.__oslogstring: 0x23d9
-  __TEXT.__gcc_except_tab: 0x6a64
-  __TEXT.__ustring: 0x74
-  __TEXT.__unwind_info: 0x19f8
-  __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x88e
-  __TEXT.__objc_methname: 0x8585
-  __TEXT.__objc_methtype: 0x3ed2
-  __TEXT.__objc_stubs: 0x5980
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x340
-  __DATA_CONST.__objc_classlist: 0x1a8
-  __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xa8
+3.24.0.0.0
+  __TEXT.__text: 0x5b7c4
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_methlist: 0x4b94
+  __TEXT.__const: 0x330
+  __TEXT.__cstring: 0x5e67
+  __TEXT.__oslogstring: 0x2ee3
+  __TEXT.__gcc_except_tab: 0x8e20
+  __TEXT.__ustring: 0x200
+  __TEXT.__unwind_info: 0x25e4
+  __TEXT.__eh_frame: 0x100
+  __TEXT.__objc_classname: 0xcd9
+  __TEXT.__objc_methname: 0xb88b
+  __TEXT.__objc_methtype: 0x4954
+  __TEXT.__objc_stubs: 0x7aa0
+  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__const: 0x5c0
+  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x85d8
-  __DATA_CONST.__objc_selrefs: 0x1d60
-  __DATA_CONST.__objc_arraydata: 0x228
-  __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x11b0
-  __AUTH_CONST.__objc_intobj: 0x528
+  __DATA_CONST.__objc_const: 0xb4d8
+  __DATA_CONST.__objc_selrefs: 0x2758
+  __DATA_CONST.__objc_arraydata: 0x248
+  __AUTH_CONST.__const: 0x350
+  __AUTH_CONST.__cfstring: 0x4200
+  __AUTH_CONST.__objc_const: 0x1e00
+  __AUTH_CONST.__objc_intobj: 0x720
+  __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__const: 0x270
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x6e8
-  __AUTH.__objc_data: 0x1090
+  __AUTH_CONST.__auth_got: 0x7a0
+  __AUTH.__objc_data: 0x1cc0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x298
-  __DATA.__objc_superrefs: 0xb8
-  __DATA.__objc_ivar: 0x288
-  __DATA.__data: 0x7e0
-  __DATA.__bss: 0xf8
+  __DATA.__objc_classrefs: 0x3b0
+  __DATA.__objc_superrefs: 0x178
+  __DATA.__objc_ivar: 0x498
+  __DATA.__data: 0x8a0
+  __DATA.__bss: 0x148
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1170
-  Symbols:   4646
-  CStrings:  2312
+  Functions: 1714
+  Symbols:   6628
+  CStrings:  3114
 
Symbols:
+ +[AVMetadataItem(MIOExtensions) attachmentsMIOMetadataItemForDictionary:pts:error:]
+ +[AVMetadataItem(MIOExtensions) attachmentsMIOMetadataItemForPixelBuffer:pts:error:]
+ +[AVMetadataItem(MIOExtensions) attachmentsMIOTimedMetadataItemForSampleBuffer:pts:error:]
+ +[AVMetadataItem(MIOExtensions) createMIOMetadataAttachmentsFormatDescription]
+ +[AVMetadataItem(MIOExtensions) createMIOMetadataStreamFormatDescription]
+ +[AVMetadataItem(MIOExtensions) customTrackMetadataItems:]
+ +[AVMetadataItem(MIOExtensions) metadataItemsForMetadataStreamFromData:copyData:]
+ +[AVMetadataItem(MIOExtensions) mioMovieMetadataItem]
+ +[AVMetadataItem(MIOExtensions) movMetadataItemWithSessionStartTime:error:]
+ +[AVMetadataItem(MIOExtensions) trackMetadataItemWithEncodedPixelFormat:]
+ +[AVMetadataItem(MIOExtensions) trackMetadataItemWithExactBytesPerRow:pixelFormat:]
+ +[AVMetadataItem(MIOExtensions) trackMetadataItemWithInputPixelFormat:]
+ +[AVMetadataItem(MIOExtensions) trackMetadataItemWithRawBayerRearrangeType:]
+ +[AVMetadataItem(MIOExtensions) trackMetadataItemWithSerializationMode:]
+ +[AVMetadataItem(MIOExtensions) trackMetadataItemWithStreamId:]
+ +[AVTimedMetadataGroup(MIOExtensions) attachmentsMIOTimedMetadataGroupForDictionary:pts:error:]
+ +[AVTimedMetadataGroup(MIOExtensions) attachmentsMIOTimedMetadataGroupForPixelBuffer:pts:error:]
+ +[AVTimedMetadataGroup(MIOExtensions) attachmentsMIOTimedMetadataGroupForSampleBuffer:pts:error:]
+ +[AVTimedMetadataGroup(MIOExtensions) metadataGroupForMetadataStreamFromData:timeStamp:copyData:]
+ +[MIOFrameProcessorFactory processorForConfig:formatDescription:]
+ +[MIOH264StreamOutputSettings outputSettingsMastery:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOH264StreamOutputSettings outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOH264StreamOutputSettings supportsEncoderType:]
+ +[MIOHEVCAlphaStreamOutputSettings outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOHEVCAlphaStreamOutputSettings supportsEncoderType:]
+ +[MIOHEVCStreamOutputSettings AVEEncoderTypeLosslessMasteringLookUp]
+ +[MIOHEVCStreamOutputSettings AVEEncoderTypeProfileLevelLookUp]
+ +[MIOHEVCStreamOutputSettings AVEEncoderTypeRequiresCustomEncodingLookUp]
+ +[MIOHEVCStreamOutputSettings adjustAVFCompressionProperties:encoderType:]
+ +[MIOHEVCStreamOutputSettings applyHighPerfSettings:]
+ +[MIOHEVCStreamOutputSettings avfEncoderSpecForEncoderType:]
+ +[MIOHEVCStreamOutputSettings encoderSpecification]
+ +[MIOHEVCStreamOutputSettings hevcAVFSettingsWithProfileLevel:encoderType:frameRate:dimensions:mastery:enableAVEHighPerformanceProfile:]
+ +[MIOHEVCStreamOutputSettings hevcSettingsWithProfileLevel:frameRate:mastery:enableAVEHighPerformanceProfile:]
+ +[MIOHEVCStreamOutputSettings masteryFromStreamData:withFrameRate:]
+ +[MIOHEVCStreamOutputSettings outputSettings:frameRate:dimensions:mastery:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOHEVCStreamOutputSettings outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOHEVCStreamOutputSettings requiresSWEncoder:]
+ +[MIOHEVCStreamOutputSettings supportsEncoderType:]
+ +[MIOJPEGStreamOutputSettings outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOJPEGStreamOutputSettings supportsEncoderType:]
+ +[MIOMastery masteryFromConfig:formatDescription:frameRate:]
+ +[MIOMastery masteryLossless]
+ +[MIOMastery masteryWithBitrate:]
+ +[MIOMastery masteryWithQuality:]
+ +[MIOMediaTypeUtility matchingAVMediaTypeFromCMType:]
+ +[MIOMediaTypeUtility matchingAVMediaTypeFromMIOMediaType:]
+ +[MIOMediaTypeUtility matchingMIOMediaTypeFromCMType:]
+ +[MIOMiscStreamOutputSettings audioSettingsFromConfig:]
+ +[MIOMiscStreamOutputSettings customEncoderSettingsFromConfig:frameRate:enableAVEHighPerformanceProfile:]
+ +[MIOMiscStreamOutputSettings outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOMiscStreamOutputSettings supportsEncoderType:]
+ +[MIOMovieMetadataUtility attachmentsTrackInAsset:forTrack:]
+ +[MIOMovieMetadataUtility findAllAssociatedMetadataTracksInAsset:forTrack:]
+ +[MIOMovieMetadataUtility isTrack:forStreamId:mediaType:]
+ +[MIOOutputSettingsFactory outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOPixelBufferPool createMIOPixelBufferPoolWithWidth:height:pixelFormat:minBufferCount:maxBufferCount:bufferCacheMode:]
+ +[MIOPixelBufferUtility combineLeftBuffer:rightBuffer:]
+ +[MIOPixelBufferUtility transferL010PixelBuffer:toq8q2PixelBuffer:]
+ +[MIOPixelBufferUtility transferq8q2PixelBuffer:toL010PixelBuffer:]
+ +[MIOProResStreamOutputSettings cmCodecTypeFromAVCodecType:]
+ +[MIOProResStreamOutputSettings outputSettingsProResEncoderType:quality:formatDescription:preferEncoderConfig:]
+ +[MIOProResStreamOutputSettings outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOProResStreamOutputSettings supportsEncoderType:]
+ +[MIOSlimStreamOutputSettings outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOSlimStreamOutputSettings supportsEncoderType:]
+ +[MIOTimePair alignedPTSTimeStamps:withSampleTimes:]
+ +[MIOTimePair timePairWithPts:originalTime:]
+ +[MIOTimePair timePairsForStream:mediaType:inAsset:error:]
+ +[MIOTimePair timePairsForStream:mediaType:inAssetURL:error:]
+ +[MIOYzipStreamOutputSettings outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:]
+ +[MIOYzipStreamOutputSettings supportsEncoderType:]
+ +[MOVStreamIOUtility colorimetricWarningsForPixelBufferAttachments:pixelFormat:]
+ +[MOVStreamIOUtility createTimeCode32FormatDescriptionWithFrameRate:dropFrame:error:]
+ +[MOVStreamIOUtility createTimeCode64FormatDescriptionWithFrameRate:dropFrame:error:]
+ +[MOVStreamIOUtility createTimecode32SampleBufferWithSMPTETime:formatDescription:pts:error:]
+ +[MOVStreamIOUtility createTimecode64SampleBufferWithSMPTETime:formatDescription:pts:error:]
+ +[MOVStreamIOUtility createTimecodeSampleBufferWithSMPTETime:formatDescription:pts:error:]
+ +[MOVStreamIOUtility customConfigWithOutputSettings:]
+ +[MOVStreamIOUtility jpegEncoderConfigWithQuality:]
+ +[MOVStreamIOUtility jpegEncoderConfig]
+ +[MOVStreamIOUtility monochrome10bitHEVCLosslessEncoderConfigAllowFrameReordering:]
+ +[MOVStreamIOUtility monochrome8bitHEVCLosslessEncoderConfigAllowFrameReordering:]
+ +[MOVStreamIOUtility stringFromTimeCode:dropFrame:]
+ +[MOVStreamIOUtility timeCodeFromString:isDropFrame:]
+ +[MOVStreamIOUtility timecode32ForSampleBuffer:dropFrame:]
+ +[MOVStreamIOUtility(Private) createTimeCode32FormatDescriptionWithFrameRate:tcDropFrame:error:]
+ +[MOVStreamIOUtility(Private) createTimeCodeFormatDescriptionWithFrameRate:error:]
+ +[MOVStreamIOUtility(Private) createxf20FormatDescriptionFromRawBayerFormatDescription:usingFirstPlaneOnly:]
+ +[MOVStreamIOUtility(Private) frameNumber32ForTimecode:usingFormatDescription:]
+ +[MOVStreamIOUtility(Private) frameNumber64ForTimecode:usingFormatDescription:]
+ +[MOVStreamIOUtility(Private) getCustomAssociatedMetadataStreamIdFromTrack:]
+ +[MOVStreamIOUtility(Private) isMOVStreamIOMovMetadataIdentifier:]
+ +[MOVStreamIOUtility(Private) nonMIOTrackMetadataItemsInMetadataItems:]
+ +[MOVStreamIOUtility(Private) saveSessionStartTime:toMovieAtURL:error:]
+ +[MOVStreamIOUtility(Private) timecodeForFrameNumber32:formatDescription:]
+ +[MOVStreamOutputSettings encoderTypeFromStreamData:]
+ +[MOVStreamOutputSettings jpegSettings:frameRate:]
+ +[MOVStreamOutputSettings supportsEncoderType:]
+ +[NSError(MOVStreamIO) populateWriterError:message:code:]
+ -[AVMetadataItem(MIOExtensions) valueAsMovSessionStartTime]
+ -[MIOCompandedRawBayerFrameProcessor .cxx_destruct]
+ -[MIOCompandedRawBayerFrameProcessor dealloc]
+ -[MIOCompandedRawBayerFrameProcessor encodedPixelFormat]
+ -[MIOCompandedRawBayerFrameProcessor formatDescriptionForEncoding]
+ -[MIOCompandedRawBayerFrameProcessor initWithInputFormatDescription:]
+ -[MIOCompandedRawBayerFrameProcessor processPixelBuffer:preserveAttachments:error:]
+ -[MIODefaultFrameProcessor encodedPixelFormat]
+ -[MIODefaultFrameProcessor formatDescriptionForEncoding]
+ -[MIODefaultFrameProcessor processPixelBuffer:preserveAttachments:error:]
+ -[MIOFifoBuffer .cxx_destruct]
+ -[MIOFifoBuffer capacity]
+ -[MIOFifoBuffer dealloc]
+ -[MIOFifoBuffer dequeue]
+ -[MIOFifoBuffer emptyFifoBuffer]
+ -[MIOFifoBuffer enqueue:]
+ -[MIOFifoBuffer initWithCapacity:]
+ -[MIOFifoBuffer prohibitDropping]
+ -[MIOFifoBuffer setProhibitDropping:]
+ -[MIOFifoBuffer usage]
+ -[MIOFifoBufferItem .cxx_destruct]
+ -[MIOFifoBufferItem dealloc]
+ -[MIOFifoBufferItem metadata]
+ -[MIOFifoBufferItem sampleBuffer]
+ -[MIOFifoBufferItem setMetadata:]
+ -[MIOFifoBufferItem setSampleBuffer:]
+ -[MIOFifoBufferItem setTimeCode:]
+ -[MIOFifoBufferItem timeCode]
+ -[MIOFrameProcessor bufferCacheMode]
+ -[MIOFrameProcessor dealloc]
+ -[MIOFrameProcessor encodedPixelFormat]
+ -[MIOFrameProcessor formatDesc]
+ -[MIOFrameProcessor formatDescriptionForEncoding]
+ -[MIOFrameProcessor initWithInputFormatDescription:]
+ -[MIOFrameProcessor processPixelBuffer:preserveAttachments:error:]
+ -[MIOFrameProcessor setBufferCacheMode:]
+ -[MIOL016Raw14FrameProcessor .cxx_destruct]
+ -[MIOL016Raw14FrameProcessor dealloc]
+ -[MIOL016Raw14FrameProcessor encodedPixelFormat]
+ -[MIOL016Raw14FrameProcessor formatDescriptionForEncoding]
+ -[MIOL016Raw14FrameProcessor initWithInputFormatDescription:]
+ -[MIOL016Raw14FrameProcessor processPixelBuffer:preserveAttachments:error:]
+ -[MIOMastery .cxx_destruct]
+ -[MIOMastery initWithKey:value:]
+ -[MIOMastery propertyKey]
+ -[MIOMastery propertyValue]
+ -[MIOMovieMetadataUtility .cxx_destruct]
+ -[MIOMovieMetadataUtility addMovieMetadataItem:]
+ -[MIOMovieMetadataUtility applyChangesError:]
+ -[MIOMovieMetadataUtility customTrackMetadataForStream:mediaType:error:]
+ -[MIOMovieMetadataUtility initWithURL:error:]
+ -[MIOMovieMetadataUtility metadataForMovie]
+ -[MIOMovieMetadataUtility movie]
+ -[MIOMovieMetadataUtility setCustomTrackMetadataForStream:mediaType:metadata:error:]
+ -[MIOMovieMetadataUtility setMovie:]
+ -[MIOMovieMetadataUtility setMovieMetadata:]
+ -[MIOMovieMetadataUtility trackForStreamId:mediaType:error:]
+ -[MIONonPlanarToL008FrameProcessor .cxx_destruct]
+ -[MIONonPlanarToL008FrameProcessor bufferCacheMode]
+ -[MIONonPlanarToL008FrameProcessor dealloc]
+ -[MIONonPlanarToL008FrameProcessor encodedPixelFormat]
+ -[MIONonPlanarToL008FrameProcessor formatDescriptionForEncoding]
+ -[MIONonPlanarToL008FrameProcessor initWithInputFormatDescription:]
+ -[MIONonPlanarToL008FrameProcessor processPixelBuffer:preserveAttachments:error:]
+ -[MIONonPlanarToL008FrameProcessor setBufferCacheMode:]
+ -[MIOOrderedKeysMutableMap .cxx_destruct]
+ -[MIOOrderedKeysMutableMap allOrderedKeys]
+ -[MIOOrderedKeysMutableMap allValues]
+ -[MIOOrderedKeysMutableMap init]
+ -[MIOOrderedKeysMutableMap objectForKey:]
+ -[MIOOrderedKeysMutableMap setObject:forKey:]
+ -[MIOPixelBufferPool flush]
+ -[MIORawBayerFrameProcessor .cxx_destruct]
+ -[MIORawBayerFrameProcessor dealloc]
+ -[MIORawBayerFrameProcessor encodedPixelFormat]
+ -[MIORawBayerFrameProcessor formatDescriptionForEncoding]
+ -[MIORawBayerFrameProcessor initWithInputFormatDescription:]
+ -[MIORawBayerFrameProcessor processPixelBuffer:preserveAttachments:error:]
+ -[MIORawBayerToy416FrameProcessor .cxx_destruct]
+ -[MIORawBayerToy416FrameProcessor bufferCacheMode]
+ -[MIORawBayerToy416FrameProcessor dealloc]
+ -[MIORawBayerToy416FrameProcessor encodedPixelFormat]
+ -[MIORawBayerToy416FrameProcessor formatDescriptionForEncoding]
+ -[MIORawBayerToy416FrameProcessor initWithInputFormatDescription:]
+ -[MIORawBayerToy416FrameProcessor processPixelBuffer:preserveAttachments:error:]
+ -[MIORawBayerToy416FrameProcessor setBufferCacheMode:]
+ -[MIOThread .cxx_destruct]
+ -[MIOThread initWithName:block:]
+ -[MIOThread init]
+ -[MIOThread perfLogHandle]
+ -[MIOThread proceed]
+ -[MIOThread setPerfLogHandle:]
+ -[MIOThread waitWithTimeout:]
+ -[MIOTimePair copyWithNewPts:]
+ -[MIOTimePair description]
+ -[MIOTimePair initWithPts:originalTime:]
+ -[MIOTimePair init]
+ -[MIOTimePair isPTSEqualOrCloseToTime:]
+ -[MIOTimePair isPTSEqualOrCloseToTime:tolerance:]
+ -[MIOTimePair originalTime]
+ -[MIOTimePair pts]
+ -[MIOTimePair setOriginalTime:]
+ -[MIOTimePair setPts:]
+ -[MIOVideoEncoderController .cxx_destruct]
+ -[MIOVideoEncoderController applyDefaultSessionProperties]
+ -[MIOVideoEncoderController closeEncoderError:]
+ -[MIOVideoEncoderController closed]
+ -[MIOVideoEncoderController codecType]
+ -[MIOVideoEncoderController dealloc]
+ -[MIOVideoEncoderController enableAVEHighPerformanceProfile]
+ -[MIOVideoEncoderController encodeFrame:pts:properties:context:error:]
+ -[MIOVideoEncoderController encoderSpecification]
+ -[MIOVideoEncoderController frameReorderingEnabled]
+ -[MIOVideoEncoderController initWithEncoderConfig:formtDescription:inProcessEncoding:frameRate:aveHighPerfMode:outputCallback:delegate:]
+ -[MIOVideoEncoderController openEncoderWithContext:error:]
+ -[MIOVideoEncoderController propagateColorAttachments]
+ -[MIOWriter .cxx_destruct]
+ -[MIOWriter addInput:]
+ -[MIOWriter addInput:error:]
+ -[MIOWriter avWriter]
+ -[MIOWriter baseMediaTimeScale]
+ -[MIOWriter bufferCacheMode]
+ -[MIOWriter canWrite]
+ -[MIOWriter cancelRecordingWithCompletionHandler:]
+ -[MIOWriter customMOVMetadata]
+ -[MIOWriter dealloc]
+ -[MIOWriter defaultFrameRate]
+ -[MIOWriter defaultNotificationQueue]
+ -[MIOWriter description]
+ -[MIOWriter drainWritingThreads]
+ -[MIOWriter enableAVEHighPerformanceProfile]
+ -[MIOWriter fail]
+ -[MIOWriter filePath]
+ -[MIOWriter finishWithCompletionHandler:]
+ -[MIOWriter finishWithEndTime:completionHandler:]
+ -[MIOWriter finishWithTimeout:completionHandler:]
+ -[MIOWriter finishWithTimeout:endTime:completionHandler:]
+ -[MIOWriter forceFinishWritingThreads]
+ -[MIOWriter getFailHandler]
+ -[MIOWriter getWarningHandler]
+ -[MIOWriter inProcessRecording]
+ -[MIOWriter initWithFilePath:error:]
+ -[MIOWriter inputs]
+ -[MIOWriter movieFragmentInterval]
+ -[MIOWriter movieMetadataUtility]
+ -[MIOWriter newWritingThreadWithName:]
+ -[MIOWriter preferCustomCompression]
+ -[MIOWriter prepareWriterWithCompletionHandler:]
+ -[MIOWriter preserveSessionStartTime]
+ -[MIOWriter proposeSessionStartTime:]
+ -[MIOWriter realTime]
+ -[MIOWriter reportError:]
+ -[MIOWriter reportWarning:]
+ -[MIOWriter sessionStartTime]
+ -[MIOWriter setAvWriter:]
+ -[MIOWriter setBaseMediaTimeScale:]
+ -[MIOWriter setBufferCacheMode:]
+ -[MIOWriter setCustomMOVMetadata:]
+ -[MIOWriter setDefaultFrameRate:]
+ -[MIOWriter setDefaultNotificationQueue:]
+ -[MIOWriter setDrainWritingThreads:]
+ -[MIOWriter setEnableAVEHighPerformanceProfile:]
+ -[MIOWriter setFailHandler:]
+ -[MIOWriter setForceFinishWritingThreads:]
+ -[MIOWriter setInProcessRecording:]
+ -[MIOWriter setMovieFragmentInterval:]
+ -[MIOWriter setPreferCustomCompression:]
+ -[MIOWriter setPreserveSessionStartTime:]
+ -[MIOWriter setRealTime:]
+ -[MIOWriter setSessionStartTime:]
+ -[MIOWriter setShouldOptimizeForNetworkUse:]
+ -[MIOWriter setStatus:]
+ -[MIOWriter setWarningHandler:]
+ -[MIOWriter shouldOptimizeForNetworkUse]
+ -[MIOWriter signalWritingThreadsProceed]
+ -[MIOWriter startSession]
+ -[MIOWriter startWriting]
+ -[MIOWriter status]
+ -[MIOWriter timeWithSeconds:]
+ -[MIOWriter writerInputsWithMediaType:]
+ -[MIOWriter writerInputsWithMediaType:streamId:]
+ -[MIOWriter writerInputs]
+ -[MIOWriter(MOVStreamWriter) addMetadataTrack:]
+ -[MIOWriter(MOVStreamWriter) addTrackForStreamWithIdentifier:formatDescription:recordingConfiguration:]
+ -[MIOWriter(MOVStreamWriter) appendMetadata:withTimeStamp:toStream:]
+ -[MIOWriter(MOVStreamWriter) appendPixelBuffer:presentationTime:toStreamId:]
+ -[MIOWriter(MOVStreamWriter) finishRecording]
+ -[MIOWriter(MOVStreamWriter) initWithURL:andExpectedFrameRate:]
+ -[MIOWriter(MOVStreamWriter) prepareToRecordWithMovieMetadata:]
+ -[MIOWriter(MOVStreamWriter) setFifoBufferCapacity:]
+ -[MIOWriter(MOVStreamWriter) setTrackMetadata:forMetadataStream:error:]
+ -[MIOWriter(MOVStreamWriter) setTrackMetadata:forStream:error:]
+ -[MIOWriter(MOVStreamWriter) setVideoTransform:forStream:]
+ -[MIOWriterAudioSampleBufferStreamInput .cxx_destruct]
+ -[MIOWriterAudioSampleBufferStreamInput appendAudioBuffer:error:]
+ -[MIOWriterAudioSampleBufferStreamInput applyWriterTimeScaleToSampleInput]
+ -[MIOWriterAudioSampleBufferStreamInput initWithStreamId:audioFormat:additionalSettings:]
+ -[MIOWriterAudioSampleBufferStreamInput init]
+ -[MIOWriterAudioSampleBufferStreamInput sampleInputOutputSettings]
+ -[MIOWriterBufferStreamInput .cxx_destruct]
+ -[MIOWriterBufferStreamInput allWriterInputs]
+ -[MIOWriterBufferStreamInput applyWriterTimeScaleToSampleInput]
+ -[MIOWriterBufferStreamInput areAllInputsReady]
+ -[MIOWriterBufferStreamInput associatedInputs]
+ -[MIOWriterBufferStreamInput avMediaType]
+ -[MIOWriterBufferStreamInput commonTrackMetadataItems]
+ -[MIOWriterBufferStreamInput customizeMetadataInput:]
+ -[MIOWriterBufferStreamInput customizeSampleInput:]
+ -[MIOWriterBufferStreamInput establishAssociationsWithError:]
+ -[MIOWriterBufferStreamInput formatDescription]
+ -[MIOWriterBufferStreamInput init]
+ -[MIOWriterBufferStreamInput inputSpecificTrackMetadataItems]
+ -[MIOWriterBufferStreamInput metadataAdaptor]
+ -[MIOWriterBufferStreamInput metadataInput]
+ -[MIOWriterBufferStreamInput pendingAttachments]
+ -[MIOWriterBufferStreamInput registerForAssociating:]
+ -[MIOWriterBufferStreamInput sampleInputOutputSettings]
+ -[MIOWriterBufferStreamInput sampleInput]
+ -[MIOWriterBufferStreamInput sampleReorderingEnabled]
+ -[MIOWriterBufferStreamInput setupInputsWithWriter:error:]
+ -[MIOWriterBufferStreamInput timeCodeAdaptor]
+ -[MIOWriterBufferStreamInput timeCodeFormatDescription]
+ -[MIOWriterBufferStreamInput timeCodeInput]
+ -[MIOWriterBufferStreamInput writeNextItemFromFifo]
+ -[MIOWriterDataStreamInput appendMetadata:withTimeStamp:error:]
+ -[MIOWriterDataStreamInput copyData]
+ -[MIOWriterDataStreamInput initWithStreamId:]
+ -[MIOWriterDataStreamInput initWithStreamId:copyData:]
+ -[MIOWriterDataStreamInput init]
+ -[MIOWriterDataStreamInput setCopyData:]
+ -[MIOWriterMetadataGroupStreamInput .cxx_destruct]
+ -[MIOWriterMetadataGroupStreamInput appendMetadata:error:]
+ -[MIOWriterMetadataGroupStreamInput associateToInput]
+ -[MIOWriterMetadataGroupStreamInput initWithStreamId:format:]
+ -[MIOWriterMetadataGroupStreamInput initWithStreamId:format:associateToInput:]
+ -[MIOWriterMetadataGroupStreamInput init]
+ -[MIOWriterMetadataGroupStreamInput uuid]
+ -[MIOWriterMetadataStreamInput .cxx_destruct]
+ -[MIOWriterMetadataStreamInput allWriterInputs]
+ -[MIOWriterMetadataStreamInput appendMetadata:]
+ -[MIOWriterMetadataStreamInput areAllInputsReady]
+ -[MIOWriterMetadataStreamInput customizeMetadataInput:]
+ -[MIOWriterMetadataStreamInput dealloc]
+ -[MIOWriterMetadataStreamInput finishProcessing]
+ -[MIOWriterMetadataStreamInput initWithStreamId:format:]
+ -[MIOWriterMetadataStreamInput metadataAdaptor]
+ -[MIOWriterMetadataStreamInput metadataInput]
+ -[MIOWriterMetadataStreamInput prepareInputFinished]
+ -[MIOWriterMetadataStreamInput setupInputsWithWriter:error:]
+ -[MIOWriterMetadataStreamInput writeNextItemFromFifo]
+ -[MIOWriterPixelBufferStreamInput .cxx_destruct]
+ -[MIOWriterPixelBufferStreamInput appendPixelBuffer:pts:error:]
+ -[MIOWriterPixelBufferStreamInput appendPixelBuffer:pts:timeCode:error:]
+ -[MIOWriterPixelBufferStreamInput attachmentsToEncode]
+ -[MIOWriterPixelBufferStreamInput avMediaType]
+ -[MIOWriterPixelBufferStreamInput config]
+ -[MIOWriterPixelBufferStreamInput customizeMetadataInput:]
+ -[MIOWriterPixelBufferStreamInput customizeSampleInput:]
+ -[MIOWriterPixelBufferStreamInput dealloc]
+ -[MIOWriterPixelBufferStreamInput encoder:codecTypeOverrideForstreamId:]
+ -[MIOWriterPixelBufferStreamInput encoder:configureSessionOverride:streamId:]
+ -[MIOWriterPixelBufferStreamInput encoder:encodedSampleBuffer:metadata:presentationTime:streamId:]
+ -[MIOWriterPixelBufferStreamInput encoder:encodingFailedForStream:]
+ -[MIOWriterPixelBufferStreamInput encoder:overrideVideoEncoderSpecificationForStreamId:]
+ -[MIOWriterPixelBufferStreamInput finishProcessing]
+ -[MIOWriterPixelBufferStreamInput formatDescription]
+ -[MIOWriterPixelBufferStreamInput initWithStreamId:format:recordingConfig:]
+ -[MIOWriterPixelBufferStreamInput initWithStreamId:format:recordingConfig:timeCodeFormat:]
+ -[MIOWriterPixelBufferStreamInput init]
+ -[MIOWriterPixelBufferStreamInput inputSpecificTrackMetadataItems]
+ -[MIOWriterPixelBufferStreamInput prepareInputFinished]
+ -[MIOWriterPixelBufferStreamInput processor]
+ -[MIOWriterPixelBufferStreamInput sampleInputOutputSettings]
+ -[MIOWriterPixelBufferStreamInput sampleReorderingEnabled]
+ -[MIOWriterPixelBufferStreamInput setTransform:]
+ -[MIOWriterPixelBufferStreamInput shouldEnableInProcessEncoding]
+ -[MIOWriterPixelBufferStreamInput stats]
+ -[MIOWriterPixelBufferStreamInput timeCodeFormatDescription]
+ -[MIOWriterPixelBufferStreamInput trackEnabled]
+ -[MIOWriterPixelBufferStreamInput transform]
+ -[MIOWriterPixelBufferStreamInput videoEncoderInterface]
+ -[MIOWriterSampleBufferStreamInput .cxx_destruct]
+ -[MIOWriterSampleBufferStreamInput appendSampleBuffer:attachments:error:]
+ -[MIOWriterSampleBufferStreamInput appendSampleBuffer:metadataGroup:error:]
+ -[MIOWriterSampleBufferStreamInput avMediaType]
+ -[MIOWriterSampleBufferStreamInput customizeMetadataInput:]
+ -[MIOWriterSampleBufferStreamInput customizeSampleInput:]
+ -[MIOWriterSampleBufferStreamInput dealloc]
+ -[MIOWriterSampleBufferStreamInput finishProcessing]
+ -[MIOWriterSampleBufferStreamInput formatDescription]
+ -[MIOWriterSampleBufferStreamInput initWithStreamId:format:]
+ -[MIOWriterSampleBufferStreamInput init]
+ -[MIOWriterSampleBufferStreamInput prepareInputFinished]
+ -[MIOWriterSampleBufferStreamInput sampleInputOutputSettings]
+ -[MIOWriterSampleBufferStreamInput sampleReorderingEnabled]
+ -[MIOWriterSampleBufferStreamInput timeCodeFormatDescription]
+ -[MIOWriterSceneSampleBufferStreamInput init]
+ -[MIOWriterStreamInput .cxx_destruct]
+ -[MIOWriterStreamInput allWriterInputs]
+ -[MIOWriterStreamInput areAllInputsReady]
+ -[MIOWriterStreamInput assignedWritingThread]
+ -[MIOWriterStreamInput avfAppendSignPostID]
+ -[MIOWriterStreamInput bufferingCapacity]
+ -[MIOWriterStreamInput canAppend]
+ -[MIOWriterStreamInput countingQueue]
+ -[MIOWriterStreamInput customMetadataItems]
+ -[MIOWriterStreamInput customMetadata]
+ -[MIOWriterStreamInput fifoBuffer]
+ -[MIOWriterStreamInput finishProcessingInDispatchGroup:]
+ -[MIOWriterStreamInput finishProcessing]
+ -[MIOWriterStreamInput init]
+ -[MIOWriterStreamInput invalidate]
+ -[MIOWriterStreamInput lastAppendTimeStamp]
+ -[MIOWriterStreamInput mediaTimeScale]
+ -[MIOWriterStreamInput mediaType]
+ -[MIOWriterStreamInput observeIsReadyStatus]
+ -[MIOWriterStreamInput observeValueForKeyPath:ofObject:change:context:]
+ -[MIOWriterStreamInput observingIsReadyStatus]
+ -[MIOWriterStreamInput onAVInputsAvailable:]
+ -[MIOWriterStreamInput pendSample]
+ -[MIOWriterStreamInput pendingSamples]
+ -[MIOWriterStreamInput perfLogHandle]
+ -[MIOWriterStreamInput prepareForAppendWithTimeStamp:error:]
+ -[MIOWriterStreamInput prepareInputFinished]
+ -[MIOWriterStreamInput prepareInputWithWriter:error:]
+ -[MIOWriterStreamInput processingQueue]
+ -[MIOWriterStreamInput processingSignPostID]
+ -[MIOWriterStreamInput resolveSample]
+ -[MIOWriterStreamInput setAssignedWritingThread:]
+ -[MIOWriterStreamInput setAvfAppendSignPostID:]
+ -[MIOWriterStreamInput setBufferingCapacity:]
+ -[MIOWriterStreamInput setCustomMetadata:]
+ -[MIOWriterStreamInput setCustomMetadataItems:]
+ -[MIOWriterStreamInput setLastAppendTimeStamp:]
+ -[MIOWriterStreamInput setMediaTimeScale:]
+ -[MIOWriterStreamInput setMediaType:]
+ -[MIOWriterStreamInput setObservingIsReadyStatus:]
+ -[MIOWriterStreamInput setPerfLogHandle:]
+ -[MIOWriterStreamInput setProcessingSignPostID:]
+ -[MIOWriterStreamInput setStreamId:]
+ -[MIOWriterStreamInput setUseOwnProcessingQueue:]
+ -[MIOWriterStreamInput setUseOwnWritingThread:]
+ -[MIOWriterStreamInput setWriter:]
+ -[MIOWriterStreamInput setupInputsWithWriter:error:]
+ -[MIOWriterStreamInput setupSignPost]
+ -[MIOWriterStreamInput shutDownOutError:]
+ -[MIOWriterStreamInput stats]
+ -[MIOWriterStreamInput stopObservingIsReadyStatus]
+ -[MIOWriterStreamInput streamId]
+ -[MIOWriterStreamInput useOwnProcessingQueue]
+ -[MIOWriterStreamInput useOwnWritingThread]
+ -[MIOWriterStreamInput uuid]
+ -[MIOWriterStreamInput verifyNewAppendTimeStamp:error:]
+ -[MIOWriterStreamInput writeNextItemFromFifo]
+ -[MIOWriterStreamInput writer]
+ -[MIOq8q2ToL010FrameProcessor .cxx_destruct]
+ -[MIOq8q2ToL010FrameProcessor bufferCacheMode]
+ -[MIOq8q2ToL010FrameProcessor dealloc]
+ -[MIOq8q2ToL010FrameProcessor encodedPixelFormat]
+ -[MIOq8q2ToL010FrameProcessor formatDescriptionForEncoding]
+ -[MIOq8q2ToL010FrameProcessor initWithInputFormatDescription:]
+ -[MIOq8q2ToL010FrameProcessor processPixelBuffer:preserveAttachments:error:]
+ -[MIOq8q2ToL010FrameProcessor setBufferCacheMode:]
+ -[MOVStreamConvertL010Toq8q2PostProcessor .cxx_destruct]
+ -[MOVStreamConvertL010Toq8q2PostProcessor processedPixelBufferFrom:metadata:error:]
+ -[MOVStreamConvertq8q2ToL010PreProcessor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamConvertq8q2ToL010PreProcessor encodedPixelFormatFromStreamData:]
+ -[MOVStreamConvertq8q2ToL010PreProcessor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamConvertq8q2ToL010PreProcessor inputPixelFormatFromStreamData:]
+ -[MOVStreamConvertq8q2ToL010PreProcessor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamOptions disableVTPreSetup]
+ -[MOVStreamOutputSettings applyAdditionalHEVCCompressionPropertiesFromRecordingConfig:]
+ -[MOVStreamReader copyNextFrameForStream:timestamp:timeCode:tcDropFrame:error:]
+ -[MOVStreamReader hasTimeCodeForStream:]
+ -[MOVStreamReader nextPixelBufferForStream:attachmentsData:timestamp:error:]
+ -[MOVStreamReader nextSampleBufferForStream:attachmentsData:timestamp:error:]
+ -[MOVStreamReader sessionStartTimeOfMovie]
+ -[MOVStreamReader timeCodeFormatDescriptionStream:]
+ -[MOVStreamReader trackMetadataForSceneStream:]
+ -[MOVStreamReader trackMetadataForStream:withMediaType:]
+ -[MOVStreamReader trackMetadataForVideoStream:]
+ -[MOVStreamReaderStreamOutput addAssociatedMetadataTracks:rawSampleAttachmentsIdentifier:trackKindIdentifier:error:]
+ -[MOVStreamReaderStreamOutput copyNextFrameForStreamTimestamp:timeCode:tcDropFrame:error:]
+ -[MOVStreamReaderStreamOutput findTimeCodeTrackAssociatedWithTrack:]
+ -[MOVStreamReaderStreamOutput formatDescriptionOfTrack:containsKey:]
+ -[MOVStreamReaderStreamOutput futureAttachmentsDuration]
+ -[MOVStreamReaderStreamOutput futureAttachmentsPts]
+ -[MOVStreamReaderStreamOutput futureTimeCodeBuffer]
+ -[MOVStreamReaderStreamOutput futureTimeCodePts]
+ -[MOVStreamReaderStreamOutput hasTimeCode]
+ -[MOVStreamReaderStreamOutput nextPixelBufferForStreamAttachmentsData:timestamp:error:]
+ -[MOVStreamReaderStreamOutput nextSampleBufferForStreamAttachmentsData:timecodeSampleBuffer:timestamp:error:]
+ -[MOVStreamReaderStreamOutput nextSampleBufferForStreamAttachmentsData:timestamp:error:]
+ -[MOVStreamReaderStreamOutput nextSampleBufferForStreamAttachmentsDataArray:timecodeSampleBuffer:timestamp:error:]
+ -[MOVStreamReaderStreamOutput setFutureAttachmentsDuration:]
+ -[MOVStreamReaderStreamOutput setFutureAttachmentsPts:]
+ -[MOVStreamReaderStreamOutput setFutureTimeCodeBuffer:]
+ -[MOVStreamReaderStreamOutput setFutureTimeCodePts:]
+ -[MOVStreamReaderStreamOutput setHasTimeCode:]
+ -[MOVStreamReaderStreamOutput setTimecodeOutput:]
+ -[MOVStreamReaderStreamOutput timeCodeBufferForStream:]
+ -[MOVStreamReaderStreamOutput timeCodeFormatDescription]
+ -[MOVStreamReaderStreamOutput timecodeOutput]
+ -[MOVStreamVideoEncoderInterface awaitEncoderClosed]
+ -[MOVStreamVideoEncoderInterface encodingQueueDepth]
+ -[MOVStreamVideoEncoderInterface formatDescriptionHasChanged:]
+ -[MOVStreamVideoEncoderInterface preSetupWithFormatDescription:]
+ -[MOVStreamVideoEncoderInterface setEncodingQueueDepth:]
+ -[MOVStreamVideoEncoderInterface setUseLegacyVTController:]
+ -[MOVStreamVideoEncoderInterface shouldEnableInProcessEncoding]
+ -[MOVStreamVideoEncoderInterface useLegacyVTController]
+ -[MOVStreamWriter encoder:overrideVideoEncoderSpecificationForStreamId:]
+ -[MOVStreamWriter inProcessRecording]
+ -[MOVStreamWriter movieMetadataUtility]
+ -[MOVStreamWriter preserveSessionStartTime]
+ -[MOVStreamWriter setInProcessRecording:]
+ -[MOVStreamWriter setPreserveSessionStartTime:]
+ -[MOVStreamWriter shouldEnableInProcessEncoding]
+ -[MOVStreamWriter startWritingThreadForMetadata]
+ -[MOVStreamWriter startWritingThreadForNonMetadataOnlyThreadId:]
+ -[MOVStreamWriter writeSampleBuffer:andMetadata:forStreamId:signpost:]
+ -[MOVStreamWriter writeVideoFrameStreamAttachmentsData:toMetadataAdaptor:ofStream:signpost:]
+ GCC_except_table100
+ GCC_except_table108
+ GCC_except_table112
+ GCC_except_table117
+ GCC_except_table121
+ GCC_except_table126
+ GCC_except_table131
+ GCC_except_table148
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table165
+ GCC_except_table223
+ GCC_except_table227
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table62
+ GCC_except_table70
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table81
+ _AVMediaTypeTimecode
+ _AVTrackAssociationTypeTimecode
+ _AVVideoCodecTypeJPEG
+ _CMBlockBufferCreateWithMemoryBlock
+ _CMBlockBufferGetDataPointer
+ _CMBlockBufferReplaceDataBytes
+ _CMFormatDescriptionEqual
+ _CMSampleBufferCreate
+ _CMSampleBufferGetDataBuffer
+ _CMSampleBufferGetFormatDescription
+ _CMSimpleQueueCreate
+ _CMSimpleQueueDequeue
+ _CMSimpleQueueEnqueue
+ _CMSimpleQueueGetCount
+ _CMTimeAbsoluteValue
+ _CMTimeCodeFormatDescriptionCreate
+ _CMTimeCodeFormatDescriptionGetFrameQuanta
+ _CMTimeCodeFormatDescriptionGetTimeCodeFlags
+ _CMTimeMakeFromDictionary
+ _CMTimeSubtract
+ _OBJC_CLASS_$_AVAsset
+ _OBJC_CLASS_$_AVMetadataItem
+ _OBJC_CLASS_$_MIOCompandedRawBayerFrameProcessor
+ _OBJC_CLASS_$_MIODefaultFrameProcessor
+ _OBJC_CLASS_$_MIOFifoBuffer
+ _OBJC_CLASS_$_MIOFifoBufferItem
+ _OBJC_CLASS_$_MIOFrameProcessor
+ _OBJC_CLASS_$_MIOFrameProcessorFactory
+ _OBJC_CLASS_$_MIOH264StreamOutputSettings
+ _OBJC_CLASS_$_MIOHEVCAlphaStreamOutputSettings
+ _OBJC_CLASS_$_MIOHEVCStreamOutputSettings
+ _OBJC_CLASS_$_MIOJPEGStreamOutputSettings
+ _OBJC_CLASS_$_MIOL016Raw14FrameProcessor
+ _OBJC_CLASS_$_MIOMastery
+ _OBJC_CLASS_$_MIOMediaTypeUtility
+ _OBJC_CLASS_$_MIOMiscStreamOutputSettings
+ _OBJC_CLASS_$_MIOMovieMetadataUtility
+ _OBJC_CLASS_$_MIONonPlanarToL008FrameProcessor
+ _OBJC_CLASS_$_MIOOrderedKeysMutableMap
+ _OBJC_CLASS_$_MIOOutputSettingsFactory
+ _OBJC_CLASS_$_MIOProResStreamOutputSettings
+ _OBJC_CLASS_$_MIORawBayerFrameProcessor
+ _OBJC_CLASS_$_MIORawBayerToy416FrameProcessor
+ _OBJC_CLASS_$_MIOSlimStreamOutputSettings
+ _OBJC_CLASS_$_MIOThread
+ _OBJC_CLASS_$_MIOTimePair
+ _OBJC_CLASS_$_MIOVideoEncoderController
+ _OBJC_CLASS_$_MIOWriter
+ _OBJC_CLASS_$_MIOWriterAudioSampleBufferStreamInput
+ _OBJC_CLASS_$_MIOWriterBufferStreamInput
+ _OBJC_CLASS_$_MIOWriterDataStreamInput
+ _OBJC_CLASS_$_MIOWriterMetadataGroupStreamInput
+ _OBJC_CLASS_$_MIOWriterMetadataStreamInput
+ _OBJC_CLASS_$_MIOWriterPixelBufferStreamInput
+ _OBJC_CLASS_$_MIOWriterSampleBufferStreamInput
+ _OBJC_CLASS_$_MIOWriterSceneSampleBufferStreamInput
+ _OBJC_CLASS_$_MIOWriterStreamInput
+ _OBJC_CLASS_$_MIOYzipStreamOutputSettings
+ _OBJC_CLASS_$_MIOq8q2ToL010FrameProcessor
+ _OBJC_CLASS_$_MOVStreamConvertL010Toq8q2PostProcessor
+ _OBJC_CLASS_$_MOVStreamConvertq8q2ToL010PreProcessor
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_IVAR_$_MIOCompandedRawBayerFrameProcessor._formatDescForEncoding
+ _OBJC_IVAR_$_MIOCompandedRawBayerFrameProcessor._pool
+ _OBJC_IVAR_$_MIOFifoBuffer._capacity
+ _OBJC_IVAR_$_MIOFifoBuffer._group
+ _OBJC_IVAR_$_MIOFifoBuffer._prohibitDropping
+ _OBJC_IVAR_$_MIOFifoBuffer._queue
+ _OBJC_IVAR_$_MIOFifoBufferItem._metadata
+ _OBJC_IVAR_$_MIOFifoBufferItem._sampleBuffer
+ _OBJC_IVAR_$_MIOFifoBufferItem._timeCode
+ _OBJC_IVAR_$_MIOFrameProcessor._formatDesc
+ _OBJC_IVAR_$_MIOFrameProcessor.bufferCacheMode
+ _OBJC_IVAR_$_MIOL016Raw14FrameProcessor._formatDescForEncoding
+ _OBJC_IVAR_$_MIOL016Raw14FrameProcessor._pool
+ _OBJC_IVAR_$_MIOMastery._propertyKey
+ _OBJC_IVAR_$_MIOMastery._propertyValue
+ _OBJC_IVAR_$_MIOMovieMetadataUtility._movie
+ _OBJC_IVAR_$_MIONonPlanarToL008FrameProcessor._bytesPerPixel
+ _OBJC_IVAR_$_MIONonPlanarToL008FrameProcessor._formatDescForEncoding
+ _OBJC_IVAR_$_MIONonPlanarToL008FrameProcessor._pool
+ _OBJC_IVAR_$_MIONonPlanarToL008FrameProcessor.bufferCacheMode
+ _OBJC_IVAR_$_MIOOrderedKeysMutableMap._keys
+ _OBJC_IVAR_$_MIOOrderedKeysMutableMap._map
+ _OBJC_IVAR_$_MIORawBayerFrameProcessor._formatDescForEncoding
+ _OBJC_IVAR_$_MIORawBayerFrameProcessor._pool
+ _OBJC_IVAR_$_MIORawBayerToy416FrameProcessor._formatDescForEncoding
+ _OBJC_IVAR_$_MIORawBayerToy416FrameProcessor._pool
+ _OBJC_IVAR_$_MIORawBayerToy416FrameProcessor.bufferCacheMode
+ _OBJC_IVAR_$_MIOThread._perfLogHandle
+ _OBJC_IVAR_$_MIOThread._waitSema
+ _OBJC_IVAR_$_MIOTimePair._originalTime
+ _OBJC_IVAR_$_MIOTimePair._pts
+ _OBJC_IVAR_$_MIOVideoEncoderController._aveHighPerfMode
+ _OBJC_IVAR_$_MIOVideoEncoderController._callbackFunc
+ _OBJC_IVAR_$_MIOVideoEncoderController._closed
+ _OBJC_IVAR_$_MIOVideoEncoderController._compressionSession
+ _OBJC_IVAR_$_MIOVideoEncoderController._config
+ _OBJC_IVAR_$_MIOVideoEncoderController._delegate
+ _OBJC_IVAR_$_MIOVideoEncoderController._enableInProcessEncoding
+ _OBJC_IVAR_$_MIOVideoEncoderController._formatDesc
+ _OBJC_IVAR_$_MIOVideoEncoderController._frameRate
+ _OBJC_IVAR_$_MIOVideoEncoderController._frameReorderingEnabled
+ _OBJC_IVAR_$_MIOWriter._avWriter
+ _OBJC_IVAR_$_MIOWriter._baseMediaTimeScale
+ _OBJC_IVAR_$_MIOWriter._bufferCacheMode
+ _OBJC_IVAR_$_MIOWriter._customMOVMetadata
+ _OBJC_IVAR_$_MIOWriter._defaultFrameRate
+ _OBJC_IVAR_$_MIOWriter._defaultNotificationQueue
+ _OBJC_IVAR_$_MIOWriter._drainWritingThreads
+ _OBJC_IVAR_$_MIOWriter._enableAVEHighPerformanceProfile
+ _OBJC_IVAR_$_MIOWriter._failHandler
+ _OBJC_IVAR_$_MIOWriter._filePath
+ _OBJC_IVAR_$_MIOWriter._finishStepDefaultTimeout
+ _OBJC_IVAR_$_MIOWriter._forceFinishWritingThreads
+ _OBJC_IVAR_$_MIOWriter._inProcessRecording
+ _OBJC_IVAR_$_MIOWriter._inputs
+ _OBJC_IVAR_$_MIOWriter._movieFragmentInterval
+ _OBJC_IVAR_$_MIOWriter._movieMetadataUtility
+ _OBJC_IVAR_$_MIOWriter._preferCustomCompression
+ _OBJC_IVAR_$_MIOWriter._preserveSessionStartTime
+ _OBJC_IVAR_$_MIOWriter._realTime
+ _OBJC_IVAR_$_MIOWriter._sessionStartTime
+ _OBJC_IVAR_$_MIOWriter._sessionStarted
+ _OBJC_IVAR_$_MIOWriter._shouldOptimizeForNetworkUse
+ _OBJC_IVAR_$_MIOWriter._status
+ _OBJC_IVAR_$_MIOWriter._warningHandler
+ _OBJC_IVAR_$_MIOWriter._writingThreads
+ _OBJC_IVAR_$_MIOWriter._writingThreadsGroup
+ _OBJC_IVAR_$_MIOWriterAudioSampleBufferStreamInput._config
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._associatedInputs
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._metadataAdaptor
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._metadataInput
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._pendingAttachments
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._sampleInput
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._timeCodeAdaptor
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._timeCodeInput
+ _OBJC_IVAR_$_MIOWriterDataStreamInput._copyData
+ _OBJC_IVAR_$_MIOWriterMetadataGroupStreamInput._associateToInput
+ _OBJC_IVAR_$_MIOWriterMetadataGroupStreamInput._associatedInput
+ _OBJC_IVAR_$_MIOWriterMetadataGroupStreamInput._uuid
+ _OBJC_IVAR_$_MIOWriterMetadataStreamInput._inputFormatDesc
+ _OBJC_IVAR_$_MIOWriterMetadataStreamInput._metadataAdaptor
+ _OBJC_IVAR_$_MIOWriterMetadataStreamInput._metadataInput
+ _OBJC_IVAR_$_MIOWriterPixelBufferStreamInput._attachmentsToEncode
+ _OBJC_IVAR_$_MIOWriterPixelBufferStreamInput._config
+ _OBJC_IVAR_$_MIOWriterPixelBufferStreamInput._inputFormatDesc
+ _OBJC_IVAR_$_MIOWriterPixelBufferStreamInput._processor
+ _OBJC_IVAR_$_MIOWriterPixelBufferStreamInput._timeCodeFormatDesc
+ _OBJC_IVAR_$_MIOWriterPixelBufferStreamInput._transform
+ _OBJC_IVAR_$_MIOWriterPixelBufferStreamInput._videoEncoderInterface
+ _OBJC_IVAR_$_MIOWriterSampleBufferStreamInput._avMediaType
+ _OBJC_IVAR_$_MIOWriterSampleBufferStreamInput._inputFormatDesc
+ _OBJC_IVAR_$_MIOWriterStreamInput._assignedWritingThread
+ _OBJC_IVAR_$_MIOWriterStreamInput._avfAppendSignPostID
+ _OBJC_IVAR_$_MIOWriterStreamInput._countingQueue
+ _OBJC_IVAR_$_MIOWriterStreamInput._customMetadata
+ _OBJC_IVAR_$_MIOWriterStreamInput._customMetadataItems
+ _OBJC_IVAR_$_MIOWriterStreamInput._fifoBuffer
+ _OBJC_IVAR_$_MIOWriterStreamInput._initFifoCapacity
+ _OBJC_IVAR_$_MIOWriterStreamInput._inputsAvailableHandler
+ _OBJC_IVAR_$_MIOWriterStreamInput._lastAppendTimeStamp
+ _OBJC_IVAR_$_MIOWriterStreamInput._mediaTimeScale
+ _OBJC_IVAR_$_MIOWriterStreamInput._mediaType
+ _OBJC_IVAR_$_MIOWriterStreamInput._observingIsReadyStatus
+ _OBJC_IVAR_$_MIOWriterStreamInput._pendingSamples
+ _OBJC_IVAR_$_MIOWriterStreamInput._perfLogHandle
+ _OBJC_IVAR_$_MIOWriterStreamInput._processingQueue
+ _OBJC_IVAR_$_MIOWriterStreamInput._processingSignPostID
+ _OBJC_IVAR_$_MIOWriterStreamInput._streamId
+ _OBJC_IVAR_$_MIOWriterStreamInput._useOwnProcessingQueue
+ _OBJC_IVAR_$_MIOWriterStreamInput._useOwnWritingThread
+ _OBJC_IVAR_$_MIOWriterStreamInput._uuid
+ _OBJC_IVAR_$_MIOWriterStreamInput._writer
+ _OBJC_IVAR_$_MIOq8q2ToL010FrameProcessor._formatDescForEncoding
+ _OBJC_IVAR_$_MIOq8q2ToL010FrameProcessor._pool
+ _OBJC_IVAR_$_MIOq8q2ToL010FrameProcessor.bufferCacheMode
+ _OBJC_IVAR_$_MOVStreamConvertL010Toq8q2PostProcessor._pool
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._futureAttachmentsDuration
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._futureAttachmentsPts
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._futureTimeCodeBuffer
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._futureTimeCodePts
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._hasTimeCode
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._timecodeOutput
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface._encoderCtrl
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface._encodingQueueDepth
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface._useLegacyVTController
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_convertL016toL010
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_preSetupFormatDescription
+ _OBJC_IVAR_$_MOVStreamWriter._avfAppendMetadataSignPost
+ _OBJC_IVAR_$_MOVStreamWriter._inProcessRecording
+ _OBJC_IVAR_$_MOVStreamWriter._movieMetadataUtility
+ _OBJC_IVAR_$_MOVStreamWriter._preserveSessionStartTime
+ _OBJC_IVAR_$_MOVStreamWriter._writeThreadAudio
+ _OBJC_IVAR_$_MOVStreamWriter._writeThreadMetadata
+ _OBJC_IVAR_$_MOVStreamWriter._writingMetadataSema
+ _OBJC_IVAR_$_MOVStreamWriter._writingThreads
+ _OBJC_METACLASS_$_MIOCompandedRawBayerFrameProcessor
+ _OBJC_METACLASS_$_MIODefaultFrameProcessor
+ _OBJC_METACLASS_$_MIOFifoBuffer
+ _OBJC_METACLASS_$_MIOFifoBufferItem
+ _OBJC_METACLASS_$_MIOFrameProcessor
+ _OBJC_METACLASS_$_MIOFrameProcessorFactory
+ _OBJC_METACLASS_$_MIOH264StreamOutputSettings
+ _OBJC_METACLASS_$_MIOHEVCAlphaStreamOutputSettings
+ _OBJC_METACLASS_$_MIOHEVCStreamOutputSettings
+ _OBJC_METACLASS_$_MIOJPEGStreamOutputSettings
+ _OBJC_METACLASS_$_MIOL016Raw14FrameProcessor
+ _OBJC_METACLASS_$_MIOMastery
+ _OBJC_METACLASS_$_MIOMediaTypeUtility
+ _OBJC_METACLASS_$_MIOMiscStreamOutputSettings
+ _OBJC_METACLASS_$_MIOMovieMetadataUtility
+ _OBJC_METACLASS_$_MIONonPlanarToL008FrameProcessor
+ _OBJC_METACLASS_$_MIOOrderedKeysMutableMap
+ _OBJC_METACLASS_$_MIOOutputSettingsFactory
+ _OBJC_METACLASS_$_MIOProResStreamOutputSettings
+ _OBJC_METACLASS_$_MIORawBayerFrameProcessor
+ _OBJC_METACLASS_$_MIORawBayerToy416FrameProcessor
+ _OBJC_METACLASS_$_MIOSlimStreamOutputSettings
+ _OBJC_METACLASS_$_MIOThread
+ _OBJC_METACLASS_$_MIOTimePair
+ _OBJC_METACLASS_$_MIOVideoEncoderController
+ _OBJC_METACLASS_$_MIOWriter
+ _OBJC_METACLASS_$_MIOWriterAudioSampleBufferStreamInput
+ _OBJC_METACLASS_$_MIOWriterBufferStreamInput
+ _OBJC_METACLASS_$_MIOWriterDataStreamInput
+ _OBJC_METACLASS_$_MIOWriterMetadataGroupStreamInput
+ _OBJC_METACLASS_$_MIOWriterMetadataStreamInput
+ _OBJC_METACLASS_$_MIOWriterPixelBufferStreamInput
+ _OBJC_METACLASS_$_MIOWriterSampleBufferStreamInput
+ _OBJC_METACLASS_$_MIOWriterSceneSampleBufferStreamInput
+ _OBJC_METACLASS_$_MIOWriterStreamInput
+ _OBJC_METACLASS_$_MIOYzipStreamOutputSettings
+ _OBJC_METACLASS_$_MIOq8q2ToL010FrameProcessor
+ _OBJC_METACLASS_$_MOVStreamConvertL010Toq8q2PostProcessor
+ _OBJC_METACLASS_$_MOVStreamConvertq8q2ToL010PreProcessor
+ _OBJC_METACLASS_$_NSThread
+ _VTCompressionSessionCreateWithOptions
+ __Block_object_dispose
+ __OBJC_$_CATEGORY_AVMetadataItem_$_MIOExtensions
+ __OBJC_$_CATEGORY_AVTimedMetadataGroup_$_MIOExtensions
+ __OBJC_$_CLASS_METHODS_AVMetadataItem(MIOExtensions)
+ __OBJC_$_CLASS_METHODS_AVTimedMetadataGroup(MIOExtensions)
+ __OBJC_$_CLASS_METHODS_MIOFrameProcessorFactory
+ __OBJC_$_CLASS_METHODS_MIOH264StreamOutputSettings
+ __OBJC_$_CLASS_METHODS_MIOHEVCAlphaStreamOutputSettings
+ __OBJC_$_CLASS_METHODS_MIOHEVCStreamOutputSettings
+ __OBJC_$_CLASS_METHODS_MIOJPEGStreamOutputSettings
+ __OBJC_$_CLASS_METHODS_MIOMastery
+ __OBJC_$_CLASS_METHODS_MIOMediaTypeUtility
+ __OBJC_$_CLASS_METHODS_MIOMiscStreamOutputSettings
+ __OBJC_$_CLASS_METHODS_MIOMovieMetadataUtility
+ __OBJC_$_CLASS_METHODS_MIOOutputSettingsFactory
+ __OBJC_$_CLASS_METHODS_MIOProResStreamOutputSettings
+ __OBJC_$_CLASS_METHODS_MIOSlimStreamOutputSettings
+ __OBJC_$_CLASS_METHODS_MIOTimePair
+ __OBJC_$_CLASS_METHODS_MIOYzipStreamOutputSettings
+ __OBJC_$_INSTANCE_METHODS_AVMetadataItem(MIOExtensions)
+ __OBJC_$_INSTANCE_METHODS_MIOCompandedRawBayerFrameProcessor
+ __OBJC_$_INSTANCE_METHODS_MIODefaultFrameProcessor
+ __OBJC_$_INSTANCE_METHODS_MIOFifoBuffer
+ __OBJC_$_INSTANCE_METHODS_MIOFifoBufferItem
+ __OBJC_$_INSTANCE_METHODS_MIOFrameProcessor
+ __OBJC_$_INSTANCE_METHODS_MIOL016Raw14FrameProcessor
+ __OBJC_$_INSTANCE_METHODS_MIOMastery
+ __OBJC_$_INSTANCE_METHODS_MIOMovieMetadataUtility
+ __OBJC_$_INSTANCE_METHODS_MIONonPlanarToL008FrameProcessor
+ __OBJC_$_INSTANCE_METHODS_MIOOrderedKeysMutableMap
+ __OBJC_$_INSTANCE_METHODS_MIORawBayerFrameProcessor
+ __OBJC_$_INSTANCE_METHODS_MIORawBayerToy416FrameProcessor
+ __OBJC_$_INSTANCE_METHODS_MIOThread
+ __OBJC_$_INSTANCE_METHODS_MIOTimePair
+ __OBJC_$_INSTANCE_METHODS_MIOVideoEncoderController
+ __OBJC_$_INSTANCE_METHODS_MIOWriter(MOVStreamWriter)
+ __OBJC_$_INSTANCE_METHODS_MIOWriterAudioSampleBufferStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterBufferStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterDataStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterMetadataGroupStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterMetadataStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterPixelBufferStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterSampleBufferStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterSceneSampleBufferStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOq8q2ToL010FrameProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamConvertL010Toq8q2PostProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamConvertq8q2ToL010PreProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MIOCompandedRawBayerFrameProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MIOFifoBuffer
+ __OBJC_$_INSTANCE_VARIABLES_MIOFifoBufferItem
+ __OBJC_$_INSTANCE_VARIABLES_MIOFrameProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MIOL016Raw14FrameProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MIOMastery
+ __OBJC_$_INSTANCE_VARIABLES_MIOMovieMetadataUtility
+ __OBJC_$_INSTANCE_VARIABLES_MIONonPlanarToL008FrameProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MIOOrderedKeysMutableMap
+ __OBJC_$_INSTANCE_VARIABLES_MIORawBayerFrameProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MIORawBayerToy416FrameProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MIOThread
+ __OBJC_$_INSTANCE_VARIABLES_MIOTimePair
+ __OBJC_$_INSTANCE_VARIABLES_MIOVideoEncoderController
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriter
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterAudioSampleBufferStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterBufferStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterDataStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterMetadataGroupStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterMetadataStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterPixelBufferStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterSampleBufferStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOq8q2ToL010FrameProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamConvertL010Toq8q2PostProcessor
+ __OBJC_$_PROP_LIST_MIOFifoBuffer
+ __OBJC_$_PROP_LIST_MIOFifoBufferItem
+ __OBJC_$_PROP_LIST_MIOFrameProcessor
+ __OBJC_$_PROP_LIST_MIOFrameProcessor.68
+ __OBJC_$_PROP_LIST_MIOMastery
+ __OBJC_$_PROP_LIST_MIOMovieMetadataUtility
+ __OBJC_$_PROP_LIST_MIOThread
+ __OBJC_$_PROP_LIST_MIOTimePair
+ __OBJC_$_PROP_LIST_MIOVideoEncoderController
+ __OBJC_$_PROP_LIST_MIOWriter
+ __OBJC_$_PROP_LIST_MIOWriterAudioSampleBufferStreamInput
+ __OBJC_$_PROP_LIST_MIOWriterBufferStreamInput
+ __OBJC_$_PROP_LIST_MIOWriterDataStreamInput
+ __OBJC_$_PROP_LIST_MIOWriterMetadataGroupStreamInput
+ __OBJC_$_PROP_LIST_MIOWriterMetadataStreamInput
+ __OBJC_$_PROP_LIST_MIOWriterPixelBufferStreamInput
+ __OBJC_$_PROP_LIST_MIOWriterStreamInput
+ __OBJC_$_PROP_LIST_MOVStreamConvertq8q2ToL010PreProcessor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MIOFrameProcessor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MIOVideoEncoderControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MIOFrameProcessor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MIOVideoEncoderControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_MIOFrameProcessor
+ __OBJC_$_PROTOCOL_REFS_MIOVideoEncoderControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MIOFrameProcessor
+ __OBJC_CLASS_PROTOCOLS_$_MIOWriterPixelBufferStreamInput
+ __OBJC_CLASS_PROTOCOLS_$_MOVStreamConvertq8q2ToL010PreProcessor
+ __OBJC_CLASS_RO_$_MIOCompandedRawBayerFrameProcessor
+ __OBJC_CLASS_RO_$_MIODefaultFrameProcessor
+ __OBJC_CLASS_RO_$_MIOFifoBuffer
+ __OBJC_CLASS_RO_$_MIOFifoBufferItem
+ __OBJC_CLASS_RO_$_MIOFrameProcessor
+ __OBJC_CLASS_RO_$_MIOFrameProcessorFactory
+ __OBJC_CLASS_RO_$_MIOH264StreamOutputSettings
+ __OBJC_CLASS_RO_$_MIOHEVCAlphaStreamOutputSettings
+ __OBJC_CLASS_RO_$_MIOHEVCStreamOutputSettings
+ __OBJC_CLASS_RO_$_MIOJPEGStreamOutputSettings
+ __OBJC_CLASS_RO_$_MIOL016Raw14FrameProcessor
+ __OBJC_CLASS_RO_$_MIOMastery
+ __OBJC_CLASS_RO_$_MIOMediaTypeUtility
+ __OBJC_CLASS_RO_$_MIOMiscStreamOutputSettings
+ __OBJC_CLASS_RO_$_MIOMovieMetadataUtility
+ __OBJC_CLASS_RO_$_MIONonPlanarToL008FrameProcessor
+ __OBJC_CLASS_RO_$_MIOOrderedKeysMutableMap
+ __OBJC_CLASS_RO_$_MIOOutputSettingsFactory
+ __OBJC_CLASS_RO_$_MIOProResStreamOutputSettings
+ __OBJC_CLASS_RO_$_MIORawBayerFrameProcessor
+ __OBJC_CLASS_RO_$_MIORawBayerToy416FrameProcessor
+ __OBJC_CLASS_RO_$_MIOSlimStreamOutputSettings
+ __OBJC_CLASS_RO_$_MIOThread
+ __OBJC_CLASS_RO_$_MIOTimePair
+ __OBJC_CLASS_RO_$_MIOVideoEncoderController
+ __OBJC_CLASS_RO_$_MIOWriter
+ __OBJC_CLASS_RO_$_MIOWriterAudioSampleBufferStreamInput
+ __OBJC_CLASS_RO_$_MIOWriterBufferStreamInput
+ __OBJC_CLASS_RO_$_MIOWriterDataStreamInput
+ __OBJC_CLASS_RO_$_MIOWriterMetadataGroupStreamInput
+ __OBJC_CLASS_RO_$_MIOWriterMetadataStreamInput
+ __OBJC_CLASS_RO_$_MIOWriterPixelBufferStreamInput
+ __OBJC_CLASS_RO_$_MIOWriterSampleBufferStreamInput
+ __OBJC_CLASS_RO_$_MIOWriterSceneSampleBufferStreamInput
+ __OBJC_CLASS_RO_$_MIOWriterStreamInput
+ __OBJC_CLASS_RO_$_MIOYzipStreamOutputSettings
+ __OBJC_CLASS_RO_$_MIOq8q2ToL010FrameProcessor
+ __OBJC_CLASS_RO_$_MOVStreamConvertL010Toq8q2PostProcessor
+ __OBJC_CLASS_RO_$_MOVStreamConvertq8q2ToL010PreProcessor
+ __OBJC_LABEL_PROTOCOL_$_MIOFrameProcessor
+ __OBJC_LABEL_PROTOCOL_$_MIOVideoEncoderControllerDelegate
+ __OBJC_METACLASS_RO_$_MIOCompandedRawBayerFrameProcessor
+ __OBJC_METACLASS_RO_$_MIODefaultFrameProcessor
+ __OBJC_METACLASS_RO_$_MIOFifoBuffer
+ __OBJC_METACLASS_RO_$_MIOFifoBufferItem
+ __OBJC_METACLASS_RO_$_MIOFrameProcessor
+ __OBJC_METACLASS_RO_$_MIOFrameProcessorFactory
+ __OBJC_METACLASS_RO_$_MIOH264StreamOutputSettings
+ __OBJC_METACLASS_RO_$_MIOHEVCAlphaStreamOutputSettings
+ __OBJC_METACLASS_RO_$_MIOHEVCStreamOutputSettings
+ __OBJC_METACLASS_RO_$_MIOJPEGStreamOutputSettings
+ __OBJC_METACLASS_RO_$_MIOL016Raw14FrameProcessor
+ __OBJC_METACLASS_RO_$_MIOMastery
+ __OBJC_METACLASS_RO_$_MIOMediaTypeUtility
+ __OBJC_METACLASS_RO_$_MIOMiscStreamOutputSettings
+ __OBJC_METACLASS_RO_$_MIOMovieMetadataUtility
+ __OBJC_METACLASS_RO_$_MIONonPlanarToL008FrameProcessor
+ __OBJC_METACLASS_RO_$_MIOOrderedKeysMutableMap
+ __OBJC_METACLASS_RO_$_MIOOutputSettingsFactory
+ __OBJC_METACLASS_RO_$_MIOProResStreamOutputSettings
+ __OBJC_METACLASS_RO_$_MIORawBayerFrameProcessor
+ __OBJC_METACLASS_RO_$_MIORawBayerToy416FrameProcessor
+ __OBJC_METACLASS_RO_$_MIOSlimStreamOutputSettings
+ __OBJC_METACLASS_RO_$_MIOThread
+ __OBJC_METACLASS_RO_$_MIOTimePair
+ __OBJC_METACLASS_RO_$_MIOVideoEncoderController
+ __OBJC_METACLASS_RO_$_MIOWriter
+ __OBJC_METACLASS_RO_$_MIOWriterAudioSampleBufferStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterBufferStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterDataStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterMetadataGroupStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterMetadataStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterPixelBufferStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterSampleBufferStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterSceneSampleBufferStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterStreamInput
+ __OBJC_METACLASS_RO_$_MIOYzipStreamOutputSettings
+ __OBJC_METACLASS_RO_$_MIOq8q2ToL010FrameProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamConvertL010Toq8q2PostProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamConvertq8q2ToL010PreProcessor
+ __OBJC_PROTOCOL_$_MIOFrameProcessor
+ __OBJC_PROTOCOL_$_MIOVideoEncoderControllerDelegate
+ __Z11pack_bufferPK11Raw16BuffermP12Raw10_packed
+ __Z13unpack_bufferPK12Raw10_packedmP11Raw14Bufferb
+ __Z13unpack_bufferPK12Raw10_packedmP11Raw16Bufferb
+ __ZN28MOVStreamHEVCLosslessEncoder17InvalidateEncoderEv
+ __ZN28MOVStreamHEVCLosslessEncoder25propagateColorAttachmentsEPK25opaqueCMFormatDescriptionP26OpaqueVTCompressionSession
+ __ZN28MOVStreamHEVCLosslessEncoder4OpenEii10IMG_FORMATdbPK25opaqueCMFormatDescriptionPFvPvS4_ijP20opaqueCMSampleBufferES4_
+ __ZZ63+[MIOHEVCStreamOutputSettings AVEEncoderTypeProfileLevelLookUp]E6lookUp
+ __ZZ63+[MIOHEVCStreamOutputSettings AVEEncoderTypeProfileLevelLookUp]E9onceToken
+ __ZZ68+[MIOHEVCStreamOutputSettings AVEEncoderTypeLosslessMasteringLookUp]E6lookUp
+ __ZZ68+[MIOHEVCStreamOutputSettings AVEEncoderTypeLosslessMasteringLookUp]E9onceToken
+ __ZZ73+[MIOHEVCStreamOutputSettings AVEEncoderTypeRequiresCustomEncodingLookUp]E6lookUp
+ __ZZ73+[MIOHEVCStreamOutputSettings AVEEncoderTypeRequiresCustomEncodingLookUp]E9onceToken
+ __ZZ80+[MOVStreamIOUtility colorimetricWarningsForPixelBufferAttachments:pixelFormat:]E27s_PixelFormatInfoDictionary
+ __ZZ80+[MOVStreamIOUtility colorimetricWarningsForPixelBufferAttachments:pixelFormat:]E4once
+ ___25-[MIOWriter reportError:]_block_invoke
+ ___27-[MIOWriter reportWarning:]_block_invoke
+ ___33-[MIOWriterStreamInput canAppend]_block_invoke
+ ___34-[MIOWriterStreamInput pendSample]_block_invoke
+ ___37-[MIOWriterStreamInput resolveSample]_block_invoke
+ ___38-[MIOWriter newWritingThreadWithName:]_block_invoke
+ ___38-[MIOWriterStreamInput pendingSamples]_block_invoke
+ ___39-[MIOWriterStreamInput processingQueue]_block_invoke
+ ___41-[MOVStreamWriter processFinishRecording]_block_invoke.441
+ ___41-[MOVStreamWriter processFinishRecording]_block_invoke.442
+ ___43-[MIOMovieMetadataUtility metadataForMovie]_block_invoke
+ ___44-[MIOMovieMetadataUtility setMovieMetadata:]_block_invoke
+ ___45-[MIOWriter(MOVStreamWriter) finishRecording]_block_invoke
+ ___48-[MIOWriter prepareWriterWithCompletionHandler:]_block_invoke
+ ___48-[MOVStreamWriter startWritingThreadForMetadata]_block_invoke
+ ___50-[MIOWriter cancelRecordingWithCompletionHandler:]_block_invoke
+ ___52-[MOVStreamVideoEncoderInterface awaitEncoderClosed]_block_invoke
+ ___56-[MIOWriterStreamInput finishProcessingInDispatchGroup:]_block_invoke
+ ___57-[MIOWriter finishWithTimeout:endTime:completionHandler:]_block_invoke
+ ___57-[MIOWriter finishWithTimeout:endTime:completionHandler:]_block_invoke.71
+ ___58-[MIOWriterMetadataGroupStreamInput appendMetadata:error:]_block_invoke
+ ___63+[MIOHEVCStreamOutputSettings AVEEncoderTypeProfileLevelLookUp]_block_invoke
+ ___63-[MIOWriter(MOVStreamWriter) prepareToRecordWithMovieMetadata:]_block_invoke
+ ___63-[MIOWriterDataStreamInput appendMetadata:withTimeStamp:error:]_block_invoke
+ ___64-[MOVStreamWriter startWritingThreadForNonMetadataOnlyThreadId:]_block_invoke
+ ___68+[MIOHEVCStreamOutputSettings AVEEncoderTypeLosslessMasteringLookUp]_block_invoke
+ ___70-[MOVStreamWriter writeSampleBuffer:andMetadata:forStreamId:signpost:]_block_invoke
+ ___72-[MIOWriterPixelBufferStreamInput appendPixelBuffer:pts:timeCode:error:]_block_invoke
+ ___73+[MIOHEVCStreamOutputSettings AVEEncoderTypeRequiresCustomEncodingLookUp]_block_invoke
+ ___73-[MIOWriterSampleBufferStreamInput appendSampleBuffer:attachments:error:]_block_invoke
+ ___75-[MIOWriterSampleBufferStreamInput appendSampleBuffer:metadataGroup:error:]_block_invoke
+ ___80+[MOVStreamIOUtility colorimetricWarningsForPixelBufferAttachments:pixelFormat:]_block_invoke
+ ___block_descriptor_104_ea8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_ea8_32r40w_e5_v8?0lw40l8r32l8
+ ___block_descriptor_56_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_80_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_88_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_literal_global.132
+ ___block_literal_global.147
+ ___block_literal_global.2
+ ___block_literal_global.463
+ __unnamed_array_storage.259
+ _dispatch_group_async
+ _dispatch_sync
+ _kMIOAllowFrameReordering
+ _kMIOCustomOutputSettings
+ _kVTCompressionSessionOption_AllowClientProcessEncode
+ _objc_msgSend$AVEEncoderTypeLosslessMasteringLookUp
+ _objc_msgSend$AVEEncoderTypeProfileLevelLookUp
+ _objc_msgSend$AVEEncoderTypeRequiresCustomEncodingLookUp
+ _objc_msgSend$addAssociatedMetadataTracks:rawSampleAttachmentsIdentifier:trackKindIdentifier:error:
+ _objc_msgSend$addInput:error:
+ _objc_msgSend$addMovieMetadataItem:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$adjustAVFCompressionProperties:encoderType:
+ _objc_msgSend$allObjects
+ _objc_msgSend$allOrderedKeys
+ _objc_msgSend$allWriterInputs
+ _objc_msgSend$appendMetadata:withTimeStamp:error:
+ _objc_msgSend$appendPixelBuffer:pts:error:
+ _objc_msgSend$appendPixelBuffer:pts:timeCode:error:
+ _objc_msgSend$appendSampleBuffer:metadataGroup:error:
+ _objc_msgSend$applyAdditionalHEVCCompressionPropertiesFromRecordingConfig:
+ _objc_msgSend$applyChangesError:
+ _objc_msgSend$applyDefaultSessionProperties
+ _objc_msgSend$applyHighPerfSettings:
+ _objc_msgSend$applyWriterTimeScaleToSampleInput
+ _objc_msgSend$areAllInputsReady
+ _objc_msgSend$assetWithURL:
+ _objc_msgSend$assetWriterInputWithMediaType:outputSettings:sourceFormatHint:
+ _objc_msgSend$assignedWritingThread
+ _objc_msgSend$associatedInputs
+ _objc_msgSend$attachmentsMIOMetadataItemForDictionary:pts:error:
+ _objc_msgSend$attachmentsMIOMetadataItemForPixelBuffer:pts:error:
+ _objc_msgSend$attachmentsMIOTimedMetadataGroupForDictionary:pts:error:
+ _objc_msgSend$attachmentsMIOTimedMetadataGroupForPixelBuffer:pts:error:
+ _objc_msgSend$attachmentsMIOTimedMetadataGroupForSampleBuffer:pts:error:
+ _objc_msgSend$attachmentsMIOTimedMetadataItemForSampleBuffer:pts:error:
+ _objc_msgSend$attachmentsToEncode
+ _objc_msgSend$attachmentsTrackInAsset:forTrack:
+ _objc_msgSend$audioSettingsFromConfig:
+ _objc_msgSend$avMediaType
+ _objc_msgSend$avWriter
+ _objc_msgSend$avfAppendSignPostID
+ _objc_msgSend$awaitEncoderClosed
+ _objc_msgSend$bufferingCapacity
+ _objc_msgSend$canAddTrackAssociationWithTrackOfInput:type:
+ _objc_msgSend$canWrite
+ _objc_msgSend$capacity
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$closeEncoderError:
+ _objc_msgSend$cmCodecTypeFromAVCodecType:
+ _objc_msgSend$colorimetricWarningsForColorPixelBufferAttachments:pixelFormat:
+ _objc_msgSend$colorimetricWarningsForGrayscalePixelBufferAttachments:pixelFormat:
+ _objc_msgSend$commonTrackMetadataItems
+ _objc_msgSend$compact
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$copyData
+ _objc_msgSend$copyNextFrameForStreamTimestamp:timeCode:tcDropFrame:error:
+ _objc_msgSend$copyWithNewPts:
+ _objc_msgSend$countingQueue
+ _objc_msgSend$createMIOMetadataAttachmentsFormatDescription
+ _objc_msgSend$createMIOMetadataStreamFormatDescription
+ _objc_msgSend$createMIOPixelBufferPoolWithWidth:height:pixelFormat:extendedPixelsPerRow:minBufferCount:
+ _objc_msgSend$createTimecode32SampleBufferWithSMPTETime:formatDescription:pts:error:
+ _objc_msgSend$createTimecode64SampleBufferWithSMPTETime:formatDescription:pts:error:
+ _objc_msgSend$createTimecodeSampleBufferWithSMPTETime:formatDescription:pts:error:
+ _objc_msgSend$createxf20FormatDescriptionFromRawBayerFormatDescription:usingFirstPlaneOnly:
+ _objc_msgSend$currentThread
+ _objc_msgSend$customEncoderSettingsFromConfig:frameRate:enableAVEHighPerformanceProfile:
+ _objc_msgSend$customMOVMetadata
+ _objc_msgSend$customMetadata
+ _objc_msgSend$customMetadataItems
+ _objc_msgSend$customTrackMetadataItems:
+ _objc_msgSend$customizeMetadataInput:
+ _objc_msgSend$customizeSampleInput:
+ _objc_msgSend$dataValue
+ _objc_msgSend$defaultFrameRate
+ _objc_msgSend$defaultNotificationQueue
+ _objc_msgSend$dequeue
+ _objc_msgSend$disableVTPreSetup
+ _objc_msgSend$drainWritingThreads
+ _objc_msgSend$emptyFifoBuffer
+ _objc_msgSend$encodeFrame:pts:properties:context:error:
+ _objc_msgSend$encodedPixelFormat
+ _objc_msgSend$encoder:overrideVideoEncoderSpecificationForStreamId:
+ _objc_msgSend$encoderTypeFromStreamData:
+ _objc_msgSend$encodingQueueDepth
+ _objc_msgSend$endSessionAtSourceTime:
+ _objc_msgSend$enqueue:
+ _objc_msgSend$establishAssociationsWithError:
+ _objc_msgSend$fail
+ _objc_msgSend$fifoBuffer
+ _objc_msgSend$filePath
+ _objc_msgSend$findAllAssociatedMetadataTracksInAsset:forTrack:
+ _objc_msgSend$findTimeCodeTrackAssociatedWithTrack:
+ _objc_msgSend$finishProcessing
+ _objc_msgSend$finishProcessingInDispatchGroup:
+ _objc_msgSend$finishWithCompletionHandler:
+ _objc_msgSend$finishWithTimeout:endTime:completionHandler:
+ _objc_msgSend$flush
+ _objc_msgSend$forceFinishWritingThreads
+ _objc_msgSend$formatDesc
+ _objc_msgSend$formatDescriptionForEncoding
+ _objc_msgSend$formatDescriptionHasChanged:
+ _objc_msgSend$formatDescriptionOfTrack:containsKey:
+ _objc_msgSend$frameNumber32ForTimecode:usingFormatDescription:
+ _objc_msgSend$frameNumber64ForTimecode:usingFormatDescription:
+ _objc_msgSend$futureAttachmentsDuration
+ _objc_msgSend$futureAttachmentsPts
+ _objc_msgSend$futureTimeCodeBuffer
+ _objc_msgSend$futureTimeCodePts
+ _objc_msgSend$getCustomAssociatedMetadataStreamIdFromTrack:
+ _objc_msgSend$getFailHandler
+ _objc_msgSend$getWarningHandler
+ _objc_msgSend$hasTimeCode
+ _objc_msgSend$hevcAVFSettingsWithProfileLevel:encoderType:frameRate:dimensions:mastery:enableAVEHighPerformanceProfile:
+ _objc_msgSend$hevcSettingsWithProfileLevel:frameRate:mastery:enableAVEHighPerformanceProfile:
+ _objc_msgSend$inProcessRecording
+ _objc_msgSend$initWithBytes:objCType:
+ _objc_msgSend$initWithEncoderConfig:formtDescription:inProcessEncoding:frameRate:aveHighPerfMode:outputCallback:delegate:
+ _objc_msgSend$initWithFilePath:error:
+ _objc_msgSend$initWithInputFormatDescription:
+ _objc_msgSend$initWithKey:value:
+ _objc_msgSend$initWithName:block:
+ _objc_msgSend$initWithPts:originalTime:
+ _objc_msgSend$initWithStreamId:
+ _objc_msgSend$initWithStreamId:copyData:
+ _objc_msgSend$initWithStreamId:format:
+ _objc_msgSend$initWithStreamId:format:recordingConfig:
+ _objc_msgSend$initWithURL:error:
+ _objc_msgSend$inputSpecificTrackMetadataItems
+ _objc_msgSend$inputs
+ _objc_msgSend$invalidate
+ _objc_msgSend$isMOVStreamIOMovMetadataIdentifier:
+ _objc_msgSend$isPTSEqualOrCloseToTime:
+ _objc_msgSend$isPTSEqualOrCloseToTime:tolerance:
+ _objc_msgSend$isTrack:forStreamId:mediaType:
+ _objc_msgSend$jpegSettings:frameRate:
+ _objc_msgSend$lastAppendTimeStamp
+ _objc_msgSend$masteryFromConfig:formatDescription:frameRate:
+ _objc_msgSend$masteryLossless
+ _objc_msgSend$masteryWithBitrate:
+ _objc_msgSend$masteryWithQuality:
+ _objc_msgSend$matchingAVMediaTypeFromCMType:
+ _objc_msgSend$matchingAVMediaTypeFromMIOMediaType:
+ _objc_msgSend$matchingMIOMediaTypeFromCMType:
+ _objc_msgSend$mediaTimeScale
+ _objc_msgSend$metadataAdaptor
+ _objc_msgSend$metadataGroupForMetadataStreamFromData:timeStamp:copyData:
+ _objc_msgSend$metadataInput
+ _objc_msgSend$metadataItemsForMetadataStreamFromData:copyData:
+ _objc_msgSend$mioMovieMetadataItem
+ _objc_msgSend$monochrome10bitHEVCLosslessEncoderConfig
+ _objc_msgSend$monochrome8bitHEVCLosslessEncoderConfig
+ _objc_msgSend$movMetadataItemWithSessionStartTime:error:
+ _objc_msgSend$movie
+ _objc_msgSend$newWritingThreadWithName:
+ _objc_msgSend$nextPixelBufferForStream:attachmentsData:timestamp:error:
+ _objc_msgSend$nextPixelBufferForStreamAttachmentsData:timestamp:error:
+ _objc_msgSend$nextSampleBufferForStream:attachmentsData:timestamp:error:
+ _objc_msgSend$nextSampleBufferForStreamAttachmentsData:timecodeSampleBuffer:timestamp:error:
+ _objc_msgSend$nextSampleBufferForStreamAttachmentsData:timestamp:error:
+ _objc_msgSend$nextSampleBufferForStreamAttachmentsDataArray:timecodeSampleBuffer:timestamp:error:
+ _objc_msgSend$nonMIOTrackMetadataItemsInMetadataItems:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$observeIsReadyStatus
+ _objc_msgSend$observingIsReadyStatus
+ _objc_msgSend$openEncoderWithContext:error:
+ _objc_msgSend$originalTime
+ _objc_msgSend$outputSettings:frameRate:dimensions:mastery:preferEncoderConfig:enableAVEHighPerformanceProfile:
+ _objc_msgSend$outputSettingsMastery:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:
+ _objc_msgSend$outputSettingsProResEncoderType:quality:formatDescription:preferEncoderConfig:
+ _objc_msgSend$outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:
+ _objc_msgSend$outputURL
+ _objc_msgSend$pendSample
+ _objc_msgSend$pendingAttachments
+ _objc_msgSend$pendingSamples
+ _objc_msgSend$perfLogHandle
+ _objc_msgSend$populateWriterError:message:code:
+ _objc_msgSend$preSetupWithFormatDescription:
+ _objc_msgSend$preferCustomCompression
+ _objc_msgSend$prepareForAppendWithTimeStamp:error:
+ _objc_msgSend$prepareInputFinished
+ _objc_msgSend$prepareInputWithWriter:error:
+ _objc_msgSend$prepareWriterWithCompletionHandler:
+ _objc_msgSend$preserveSessionStartTime
+ _objc_msgSend$proceed
+ _objc_msgSend$processPixelBuffer:preserveAttachments:error:
+ _objc_msgSend$processingQueue
+ _objc_msgSend$processingSignPostID
+ _objc_msgSend$processor
+ _objc_msgSend$processorForConfig:formatDescription:
+ _objc_msgSend$propagateColorAttachments
+ _objc_msgSend$propertyKey
+ _objc_msgSend$propertyValue
+ _objc_msgSend$proposeSessionStartTime:
+ _objc_msgSend$pts
+ _objc_msgSend$realTime
+ _objc_msgSend$registerForAssociating:
+ _objc_msgSend$reportError:
+ _objc_msgSend$reportWarning:
+ _objc_msgSend$requiresSWEncoder:
+ _objc_msgSend$resolveSample
+ _objc_msgSend$sampleInput
+ _objc_msgSend$sampleInputOutputSettings
+ _objc_msgSend$saveSessionStartTime:toMovieAtURL:error:
+ _objc_msgSend$setAssignedWritingThread:
+ _objc_msgSend$setAvWriter:
+ _objc_msgSend$setAvfAppendSignPostID:
+ _objc_msgSend$setBufferingCapacity:
+ _objc_msgSend$setCopyData:
+ _objc_msgSend$setCustomMOVMetadata:
+ _objc_msgSend$setCustomMetadata:
+ _objc_msgSend$setDrainWritingThreads:
+ _objc_msgSend$setEncodingQueueDepth:
+ _objc_msgSend$setForceFinishWritingThreads:
+ _objc_msgSend$setFutureAttachmentsDuration:
+ _objc_msgSend$setFutureAttachmentsPts:
+ _objc_msgSend$setFutureTimeCodeBuffer:
+ _objc_msgSend$setFutureTimeCodePts:
+ _objc_msgSend$setHasTimeCode:
+ _objc_msgSend$setInProcessRecording:
+ _objc_msgSend$setLastAppendTimeStamp:
+ _objc_msgSend$setMediaType:
+ _objc_msgSend$setMovie:
+ _objc_msgSend$setNaturalSize:
+ _objc_msgSend$setObservingIsReadyStatus:
+ _objc_msgSend$setOriginalTime:
+ _objc_msgSend$setPerfLogHandle:
+ _objc_msgSend$setProcessingSignPostID:
+ _objc_msgSend$setPts:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setTimeCode:
+ _objc_msgSend$setTimecodeOutput:
+ _objc_msgSend$setUseLegacyVTController:
+ _objc_msgSend$setWriter:
+ _objc_msgSend$setupInputsWithWriter:error:
+ _objc_msgSend$setupSignPost
+ _objc_msgSend$shouldEnableInProcessEncoding
+ _objc_msgSend$shouldOptimizeForNetworkUse
+ _objc_msgSend$shutDownOutError:
+ _objc_msgSend$signalWritingThreadsProceed
+ _objc_msgSend$startSession
+ _objc_msgSend$startWritingThreadForMetadata
+ _objc_msgSend$startWritingThreadForNonMetadataOnlyThreadId:
+ _objc_msgSend$stopObservingIsReadyStatus
+ _objc_msgSend$supportsEncoderType:
+ _objc_msgSend$timeCode
+ _objc_msgSend$timeCodeBufferForStream:
+ _objc_msgSend$timeCodeFormatDescription
+ _objc_msgSend$timeCodeInput
+ _objc_msgSend$timePairWithPts:originalTime:
+ _objc_msgSend$timePairsForStream:mediaType:inAsset:error:
+ _objc_msgSend$timecode32ForSampleBuffer:dropFrame:
+ _objc_msgSend$timecodeForFrameNumber32:formatDescription:
+ _objc_msgSend$timecodeOutput
+ _objc_msgSend$trackEnabled
+ _objc_msgSend$trackForStreamId:mediaType:error:
+ _objc_msgSend$trackMetadataForMetadataStream:
+ _objc_msgSend$trackMetadataItemWithEncodedPixelFormat:
+ _objc_msgSend$trackMetadataItemWithInputPixelFormat:
+ _objc_msgSend$trackMetadataItemWithRawBayerRearrangeType:
+ _objc_msgSend$trackMetadataItemWithSerializationMode:
+ _objc_msgSend$trackMetadataItemWithStreamId:
+ _objc_msgSend$transferL010PixelBuffer:toq8q2PixelBuffer:
+ _objc_msgSend$transferq8q2PixelBuffer:toL010PixelBuffer:
+ _objc_msgSend$usage
+ _objc_msgSend$useLegacyVTController
+ _objc_msgSend$useOwnProcessingQueue
+ _objc_msgSend$useOwnWritingThread
+ _objc_msgSend$uuid
+ _objc_msgSend$valueAsMovSessionStartTime
+ _objc_msgSend$verifyNewAppendTimeStamp:error:
+ _objc_msgSend$videoEncoderInterface
+ _objc_msgSend$waitWithTimeout:
+ _objc_msgSend$weakObjectsPointerArray
+ _objc_msgSend$writeMovieHeaderToURL:fileType:options:error:
+ _objc_msgSend$writeNextItemFromFifo
+ _objc_msgSend$writeSampleBuffer:andMetadata:forStreamId:signpost:
+ _objc_msgSend$writeVideoFrameStreamAttachmentsData:toMetadataAdaptor:ofStream:signpost:
+ _objc_msgSend$writer
+ _objc_msgSend$writerInputs
+ _objc_msgSend$writerInputsWithMediaType:
+ _objc_retainBlock
+ _objc_setProperty_atomic_copy
+ _processingQueue.onceToken
+ _processingQueue.proc
- +[MOVStreamIOUtility(Private) createxf20FormatDescriptionFromRawBayerFormatDescription:]
- -[MOVStreamReader findAllAssociatedMetadataTrackInAsset:forTrack:]
- -[MOVStreamReaderStreamOutput futureAttachementsDuration]
- -[MOVStreamReaderStreamOutput futureAttachementsPts]
- -[MOVStreamReaderStreamOutput getKeyFromMetadataTrack:]
- -[MOVStreamReaderStreamOutput setFutureAttachementsDuration:]
- -[MOVStreamReaderStreamOutput setFutureAttachementsPts:]
- -[MOVStreamWriter encoder:overrideVideoEncoderSpecificationForstreamId:]
- -[MOVStreamWriter marksOutputTracksAsEnabledForStream:]
- -[MOVStreamWriter writeSampleBuffer:andMetadata:forStreamId:]
- -[MOVStreamWriter writeVideoFrameStreamAttachmentsData:toMetadataAdaptor:ofStream:]
- GCC_except_table101
- GCC_except_table110
- GCC_except_table114
- GCC_except_table118
- GCC_except_table124
- GCC_except_table127
- GCC_except_table133
- GCC_except_table153
- GCC_except_table206
- GCC_except_table212
- GCC_except_table222
- GCC_except_table51
- GCC_except_table71
- GCC_except_table87
- _OBJC_IVAR_$_MOVStreamReaderStreamOutput._futureAttachementsDuration
- _OBJC_IVAR_$_MOVStreamReaderStreamOutput._futureAttachementsPts
- _OBJC_IVAR_$_MOVStreamWriter._avfAppendSignPostID
- __ZN28MOVStreamHEVCLosslessEncoder25propogateColorAttachmentsEPK25opaqueCMFormatDescriptionP26OpaqueVTCompressionSession
- __ZN28MOVStreamHEVCLosslessEncoder4OpenEii10IMG_FORMATdPK25opaqueCMFormatDescriptionPFvPvS4_ijP20opaqueCMSampleBufferES4_
- ___41-[MOVStreamWriter processFinishRecording]_block_invoke.424
- ___41-[MOVStreamWriter processFinishRecording]_block_invoke.425
- ___61-[MOVStreamWriter writeSampleBuffer:andMetadata:forStreamId:]_block_invoke
- ___block_literal_global.446
- __unnamed_array_storage.245
- _objc_msgSend$createxf20FormatDescriptionFromRawBayerFormatDescription:
- _objc_msgSend$encoder:overrideVideoEncoderSpecificationForstreamId:
- _objc_msgSend$findAllAssociatedMetadataTrackInAsset:forTrack:
- _objc_msgSend$futureAttachementsDuration
- _objc_msgSend$futureAttachementsPts
- _objc_msgSend$getKeyFromMetadataTrack:
- _objc_msgSend$nextPixelBufferForStreamAttachementsData:timestamp:error:
- _objc_msgSend$nextSampleBufferForStreamAttachementsData:timestamp:error:
- _objc_msgSend$setFutureAttachementsDuration:
- _objc_msgSend$setFutureAttachementsPts:
- _objc_msgSend$writeSampleBuffer:andMetadata:forStreamId:
- _objc_msgSend$writeVideoFrameStreamAttachmentsData:toMetadataAdaptor:ofStream:
CStrings:
+ "\x01B\x13D"
+ "\x02"
+ "\x021%!"
+ "\a\x12\xf0\xf0A6\x11!"
+ "!info.pixelFormatAlt || (info.pixelFormat == info.pixelFormatAlt)"
+ "$"
+ "%02d:%02d:%02d%c%02d"
+ "%@: PEND: %lld (FIFO: %zu ECDQ: %lld ENC: %lld) REDY: %d"
+ "%@: PEND: %lld (FIFO: %zu) REDY: %d"
+ "%@_%ld"
+ "%@_%ld_%@"
+ "%f [Orig: %f]"
+ "'JPEG' encoder does not support high performance profile."
+ "'Other' encoder does not support high performance profile."
+ "'ProRes' encoder does not support high performance profile."
+ "'Slim' encoder does not support high performance profile."
+ "'Yzip' encoder does not support high performance profile."
+ "+[MOVStreamIOUtility colorimetricWarningsForPixelBufferAttachments:pixelFormat:]_block_invoke"
+ "+[MOVStreamOutputSettings encoderTypeFromStreamData:]"
+ "-[MIOFrameProcessor encodedPixelFormat]"
+ "-[MIOFrameProcessor formatDescriptionForEncoding]"
+ "-[MIOFrameProcessor processPixelBuffer:preserveAttachments:error:]"
+ "-[MIORawBayerToy416FrameProcessor processPixelBuffer:preserveAttachments:error:]"
+ "-[MIOWriterBufferStreamInput avMediaType]"
+ "-[MIOWriterBufferStreamInput customizeMetadataInput:]"
+ "-[MIOWriterBufferStreamInput customizeSampleInput:]"
+ "-[MIOWriterBufferStreamInput formatDescription]"
+ "-[MIOWriterBufferStreamInput sampleInputOutputSettings]"
+ "-[MIOWriterBufferStreamInput sampleReorderingEnabled]"
+ "-[MIOWriterBufferStreamInput timeCodeFormatDescription]"
+ "-[MIOWriterPixelBufferStreamInput encoder:codecTypeOverrideForstreamId:]"
+ "-[MIOWriterPixelBufferStreamInput encoder:configureSessionOverride:streamId:]"
+ "-[MIOWriterPixelBufferStreamInput encoder:overrideVideoEncoderSpecificationForStreamId:]"
+ "-[MIOWriterStreamInput allWriterInputs]"
+ "-[MIOWriterStreamInput areAllInputsReady]"
+ "-[MIOWriterStreamInput finishProcessing]"
+ "-[MIOWriterStreamInput prepareInputFinished]"
+ "-[MIOWriterStreamInput setupInputsWithWriter:error:]"
+ "-[MIOWriterStreamInput writeNextItemFromFifo]"
+ "-[MIOq8q2ToL010FrameProcessor processPixelBuffer:preserveAttachments:error:]"
+ "-[MOVStreamReaderStreamOutput nextSampleBufferForStreamAttachmentsDataArray:timecodeSampleBuffer:timestamp:error:]"
+ "1650946098_0"
+ "1899524402_0"
+ "3.24.0"
+ ":"
+ ";"
+ ";,"
+ "@\"<MIOFrameProcessor>\""
+ "@\"<MIOVideoEncoderControllerDelegate>\""
+ "@\"AVAssetWriterInput\""
+ "@\"AVAssetWriterInputMetadataAdaptor\""
+ "@\"AVMutableMovie\""
+ "@\"MIOFifoBuffer\""
+ "@\"MIOMovieMetadataUtility\""
+ "@\"MIOOrderedKeysMutableMap\""
+ "@\"MIOThread\""
+ "@\"MIOVideoEncoderController\""
+ "@\"MIOWriter\""
+ "@\"MIOWriterBufferStreamInput\""
+ "@\"MOVStreamVideoEncoderInterface\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSPointerArray\""
+ "@20@0:8B16"
+ "@20@0:8C16"
+ "@24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
+ "@24@0:8^{opaqueCMFormatDescription=}16"
+ "@32@0:8@16@?24"
+ "@32@0:8@16^{opaqueCMFormatDescription=}24"
+ "@32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16d24"
+ "@32@0:8q16@24"
+ "@36@0:8@16d24B32"
+ "@36@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16d24B32"
+ "@40@0:8@16^{opaqueCMFormatDescription=}24@32"
+ "@40@0:8@16^{opaqueCMFormatDescription=}24d32"
+ "@40@0:8@16q24^@32"
+ "@40@0:8i16q20^{opaqueCMFormatDescription=}28B36"
+ "@40@0:8{?=qiIq}16"
+ "@44@0:8@16d24@32B40"
+ "@44@0:8{CVSMPTETime=ssIIIssss}16B40"
+ "@48@0:8@16^{opaqueCMFormatDescription=}24@32^{opaqueCMFormatDescription=}40"
+ "@48@0:8@16^{opaqueCMFormatDescription=}24d32B40B44"
+ "@48@0:8@16q24@32^@40"
+ "@48@0:8{?=qiIq}16^@40"
+ "@52@0:8@16{?=qiIq}24B48"
+ "@52@0:8i16d20{?=ii}28@36B44B48"
+ "@56@0:8@16i24d28{?=ii}36@44B52"
+ "@56@0:8@16{?=qiIq}24^@48"
+ "@56@0:8^{__CVBuffer=}16{?=qiIq}24^@48"
+ "@56@0:8^{opaqueCMSampleBuffer=}16{?=qiIq}24^@48"
+ "@64@0:8@16^{opaqueCMFormatDescription=}24B32d36B44^?48@56"
+ "@64@0:8{?=qiIq}16{?=qiIq}40"
+ "@?16@0:8"
+ "A\x12\x11"
+ "A processing queue is already assigned, cannot set usage of own processing queue."
+ "A writing thread is already assigned, cannot set usage of own writing thread."
+ "AVAssetWriter set requiresInProcessOperation = YES"
+ "AVAssetWriter.requiresInProcessOperation not supported."
+ "AVEEncoderTypeLosslessMasteringLookUp"
+ "AVEEncoderTypeProfileLevelLookUp"
+ "AVEEncoderTypeRequiresCustomEncodingLookUp"
+ "Attempted to enqueue sample in full Fifo for stream %@.  Indicates leak in overall pending sample tracking."
+ "B24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
+ "B24@0:8^{opaqueCMFormatDescription=}16"
+ "B40@0:8^{__CVBuffer=}16^{__CVBuffer=}24d32"
+ "B40@0:8^{opaqueCMSampleBuffer=}16@24^@32"
+ "B40@0:8{?=qiIq}16"
+ "B48@0:8@16@24@32Q40"
+ "B48@0:8@16q24@32^@40"
+ "B56@0:8@16{?=qiIq}24^@48"
+ "B56@0:8^{__CVBuffer=}16{?=qiIq}24^@48"
+ "B56@0:8{?=qiIq}16@40^@48"
+ "B64@0:8{?=qiIq}16{?=qiIq}40"
+ "B72@0:8^{__CVBuffer=}16{?=qiIq}24^{__CFDictionary=}48^v56^@64"
+ "B72@0:8{CGAffineTransform=dddddd}16@64"
+ "B80@0:8^{__CVBuffer=}16{?=qiIq}24{CVSMPTETime=ssIIIssss}48^@72"
+ "BytesPerPixelLookUp: Register %f for %@"
+ "CANCEL_0: processing queues"
+ "CANCEL_1: invalidate the input and empty the fifos"
+ "CANCEL_2: AVAssetWriter"
+ "Can't add timecode track output (%@) to the AVAssetReader."
+ "Cannot add AVAssetWriterInputs for stream '%@'."
+ "Cannot add output to associated metadata track for stream '%@'."
+ "Cannot add time code input for stream '%@'."
+ "Cannot append frame, CMSampleBufferCreateForImageBuffer failed (err:%d) for stream %@."
+ "Cannot append frame, invalid buffer attachments %@ for stream %@."
+ "Cannot append frame, invalid pixel buffer attachments %@ for stream %@."
+ "Cannot associate %@ with %@."
+ "Cannot associate attachment metadata input with %@."
+ "Cannot associate time code input with %@."
+ "Cannot convert L010 to q8q2 buffer."
+ "Cannot convert q8q2 to L010 buffer."
+ "Cannot create TimeCode32 FormatDescription with fps %f drop frame %@. Error: %d"
+ "Cannot create TimeCode32 FormatDescription with fps %f. Error: %d"
+ "Cannot create TimeCode64 FormatDescription with fps %f drop frame %@. Error: %d"
+ "Cannot create asset from URL '%@'."
+ "Cannot create metadata attachments format description (err: %d)."
+ "Cannot create metadata format description for stream '%@'."
+ "Cannot create metadata stream format description (err: %d)."
+ "Cannot create pixel buffer pool for q8q2 stream."
+ "Cannot create time code sample buffer for stream %@."
+ "Cannot find attachments track for stream '%@'."
+ "Cannot find track for stream '%@'."
+ "Cannot serialize MIO mov metadata: %@"
+ "Cannot set writing thread priority to 1.0. Continue with default priority..."
+ "Cannot start reading data for stream '%@'."
+ "Check AVAssetWriter.requiresInProcessOperation is %d"
+ "Could not close writing threads within timeout"
+ "Could not create block buffer"
+ "Could not drain the fifo buffers within timeout"
+ "Could not drain the processing queues within timeout"
+ "Could not get data from block buffer"
+ "Could not write into block buffer"
+ "CustomOutputSettings"
+ "Default thread writing mode enabled."
+ "Eror creating movieMetadataUtility: %{public}@."
+ "Error VTCompressionSession set properties failed."
+ "Error VTCompressionSessionCompleteFrames errNo: %d"
+ "Error VTCompressionSessionCreate errNo: %d"
+ "Error VTCompressionSessionEncodeFrame errNo: %d infoFlags: %d"
+ "Error applying default settings errNo: %d"
+ "Error closeEncoder: no VTCompressionSession"
+ "Error closing encoding session for stream '%@': %@"
+ "Error creating movieMetadataUtility: %{public}@."
+ "Error enabling AVE High Performance Mode errNo: %d"
+ "Error encoding frame for stream '%@': %d"
+ "Error occurred during AVWriter append %@ for stream '%@'."
+ "Error occurred during AVWriter timecode append %@ for stream '%@'."
+ "Error occurred during appendTimedMetadataGroup %@ for stream '%@'."
+ "Error on saving session start time: %{public}@"
+ "Error on shutdown %{public}@ : %{public}@"
+ "Error opening encoding session '%@': %@"
+ "Error saving sessionStartTime: %@"
+ "Exception (%@) creating AVAssetWriterInput for stream '%@'."
+ "Exception occurred during AVWriter append %@ for stream '%@'."
+ "Exception occurred during AVWriter timecode append %@ for stream '%@'."
+ "Exception occurred during appendTimedMetadataGroup %@ for stream '%@'."
+ "Exception occurred whiles setting session end time: %@"
+ "FIFOAlreadyCreated"
+ "FINISH_0: processing queues"
+ "FINISH_1: fifos"
+ "FINISH_2: shut down inputs queue"
+ "FINISH_3: AVAssetWriter"
+ "Fifo is already created, capacity cannot be changed anymore."
+ "File path '%@' is an existing directory"
+ "Format descriotionchanged for stream '%{public}@' failed (%{public}@)! Try re-initlialize encoder."
+ "HEVC config not available."
+ "HEVC_Monochrome_AutoLevel"
+ "I24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
+ "Invalid 'exact-bytes-per-row' value type (%@), allowed types: NSNUmber, NSArray<NSNumber*>."
+ "Invalid audioFormat, no format description found."
+ "Invalid time stamp (%f). Time stamp must be higher than %f."
+ "MIOCompandedRawBayerFrameProcessor"
+ "MIODefaultFrameProcessor"
+ "MIODisableVTPreSetup"
+ "MIOExtensions"
+ "MIOFifoBuffer"
+ "MIOFifoBufferItem"
+ "MIOFrameProcessor"
+ "MIOFrameProcessor.m"
+ "MIOFrameProcessorFactory"
+ "MIOH264StreamOutputSettings"
+ "MIOHEVCAlphaStreamOutputSettings"
+ "MIOHEVCStreamOutputSettings"
+ "MIOJPEGStreamOutputSettings"
+ "MIOL016Raw14FrameProcessor"
+ "MIOMastery"
+ "MIOMediaTypeUtility"
+ "MIOMiscStreamOutputSettings"
+ "MIOMovieMetadataUtility"
+ "MIONonPlanarToL008FrameProcessor"
+ "MIOOrderedKeysMutableMap"
+ "MIOOutputSettingsFactory"
+ "MIOProResStreamOutputSettings"
+ "MIORawBayerFrameProcessor"
+ "MIORawBayerToy416FrameProcessor"
+ "MIORawBayerToy416FrameProcessor.mm"
+ "MIOSlimStreamOutputSettings"
+ "MIOThread"
+ "MIOTimePair"
+ "MIOVideoEncoderController"
+ "MIOVideoEncoderControllerDelegate"
+ "MIOWriter"
+ "MIOWriter file path cannot be empty string."
+ "MIOWriter file path cannot be nil."
+ "MIOWriter status not MIOWriterInit, cannot add input."
+ "MIOWriter {\n Filepath: %@ \n}"
+ "MIOWriter.inProcessRecording requires custom or none encoder settings. Encoding for stream %@ will not performed in process!"
+ "MIOWriterAudioSampleBufferStreamInput"
+ "MIOWriterBufferStreamInput"
+ "MIOWriterBufferStreamInput.m"
+ "MIOWriterDataStreamInput"
+ "MIOWriterMetadataGroupStreamInput"
+ "MIOWriterMetadataStreamInput"
+ "MIOWriterPixelBufferStreamInput"
+ "MIOWriterPixelBufferStreamInput.mm"
+ "MIOWriterSampleBufferStreamInput"
+ "MIOWriterSceneSampleBufferStreamInput"
+ "MIOWriterStreamInput"
+ "MIOWriterStreamInput.m"
+ "MIOYzipStreamOutputSettings"
+ "MIOq8q2ToL010FrameProcessor"
+ "MIOq8q2ToL010FrameProcessor.mm"
+ "MOVStreamConvertL010Toq8q2PostProcessor"
+ "MOVStreamConvertq8q2ToL010PreProcessor"
+ "MOVStreamWriter.inProcessRecording requires custom or none encoder settings. Encoding for stream %{public}@ will not performed in process!"
+ "MOVStreamWriterMetadata"
+ "MOVStreamWriterSamples.%u"
+ "MULTI_THREAD_WRITING"
+ "Multi thread writing mode enabled."
+ "NO"
+ "Orig fd: %@  New fd: %@"
+ "Orig fd: %@  Used fd: %@"
+ "Pre-initialize VTCompressionSession for stream '%@' failed (%@)! Will try again after first pixel buffer is appended..."
+ "Pre-initialize VTCompressionSession for stream '%{public}@' disabled."
+ "Pre-initialize VTCompressionSession for stream '%{public}@' failed (%{public}@)! Will try again after first pixel buffer is appended..."
+ "Pre-initialize VTCompressionSession for stream '%{public}@'..."
+ "Process pixel buffer failed %@ for stream %@."
+ "ProcessingQueueAlreadyAssigned"
+ "Q32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16d24"
+ "Running out of buffers!"
+ "Sample buffer encoding failed (encoder status: %i flags: %d) for stream '%@'. Dropping frame."
+ "Setting kVTCompressionPropertyKey_AllowFrameReordering failed."
+ "Setting kVTCompressionPropertyKey_MaximizePowerEfficiency failed."
+ "Setting kVTCompressionPropertyKey_RealTime failed."
+ "Stream '%@' with same media type already exists."
+ "Stream: %@ buffering capacity reached (%zu), dropping sample"
+ "T@\"<MIOFrameProcessor>\",R,V_processor"
+ "T@\"AVAssetReaderTrackOutput\",&,V_timecodeOutput"
+ "T@\"AVAssetWriter\",&,V_avWriter"
+ "T@\"AVAssetWriterInput\",R"
+ "T@\"AVAssetWriterInput\",R,V_metadataInput"
+ "T@\"AVAssetWriterInput\",R,V_sampleInput"
+ "T@\"AVAssetWriterInput\",R,V_timeCodeInput"
+ "T@\"AVAssetWriterInputMetadataAdaptor\",R,V_metadataAdaptor"
+ "T@\"AVAssetWriterInputMetadataAdaptor\",R,V_timeCodeAdaptor"
+ "T@\"AVMutableMovie\",&,V_movie"
+ "T@\"MIOFifoBuffer\",R,V_fifoBuffer"
+ "T@\"MIOFifoBuffer\",R,V_pendingAttachments"
+ "T@\"MIOMovieMetadataUtility\",R"
+ "T@\"MIOOrderedKeysMutableMap\",R,V_inputs"
+ "T@\"MIOThread\",W,V_assignedWritingThread"
+ "T@\"MIOWriter\",W,V_writer"
+ "T@\"MIOWriterBufferStreamInput\",R,V_associateToInput"
+ "T@\"MOVStreamVideoEncoderInterface\",R,V_videoEncoderInterface"
+ "T@\"NSArray\",&,V_customMOVMetadata"
+ "T@\"NSArray\",&,V_customMetadataItems"
+ "T@\"NSArray\",&,V_futureAttachmentsData"
+ "T@\"NSArray\",R"
+ "T@\"NSArray\",R,V_attachmentsToEncode"
+ "T@\"NSDictionary\",&,V_customMetadata"
+ "T@\"NSDictionary\",R,V_config"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_defaultNotificationQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_countingQueue"
+ "T@\"NSObject<OS_os_log>\",&,V_perfLogHandle"
+ "T@\"NSString\",C,V_streamId"
+ "T@\"NSString\",R,V_filePath"
+ "T@\"NSString\",R,V_propertyKey"
+ "T@,R,V_propertyValue"
+ "TB,R,V_closed"
+ "TB,R,V_frameReorderingEnabled"
+ "TB,V_copyData"
+ "TB,V_drainWritingThreads"
+ "TB,V_enableAVEHighPerformanceProfile"
+ "TB,V_forceFinishWritingThreads"
+ "TB,V_hasTimeCode"
+ "TB,V_inProcessRecording"
+ "TB,V_observingIsReadyStatus"
+ "TB,V_preferCustomCompression"
+ "TB,V_preserveSessionStartTime"
+ "TB,V_prohibitDropping"
+ "TB,V_realTime"
+ "TB,V_shouldOptimizeForNetworkUse"
+ "TB,V_useLegacyVTController"
+ "TI,V_status"
+ "TQ,V_avfAppendSignPostID"
+ "TQ,V_processingSignPostID"
+ "T^{opaqueCMFormatDescription=},R"
+ "T^{opaqueCMSampleBuffer=},V_futureTimeCodeBuffer"
+ "T^{opaqueCMSampleBuffer=},V_timeCode"
+ "Td,V_defaultFrameRate"
+ "Ti,D"
+ "Ti,V_mediaTimeScale"
+ "TimeCode format (%d) not supported."
+ "Tq,V_encodingQueueDepth"
+ "T{?=qiIq},V_futureAttachmentsDuration"
+ "T{?=qiIq},V_futureAttachmentsPts"
+ "T{?=qiIq},V_futureTimeCodePts"
+ "T{?=qiIq},V_lastAppendTimeStamp"
+ "T{?=qiIq},V_originalTime"
+ "T{?=qiIq},V_pts"
+ "Unable to use output settings (%@) for stream '%@'."
+ "Unknown Prores Codec."
+ "Unknown metadata stream '%@'"
+ "Unknown stream %@."
+ "Unknown video stream '%@'"
+ "VTCompressionSession: Enabling kVTCompressionSessionOption_AllowClientProcessEncode"
+ "WARNING: %@"
+ "Writer not in MIOWriterInit state."
+ "Writer not in MIOWriterReady state."
+ "Writer not in state MIOWriterReady. Cannot append"
+ "WritingThreadAlreadyAssigned"
+ "YES"
+ "[MIOWriter dealloc]"
+ "[WritingThread Metadata] Exiting writing loop."
+ "[WritingThread.%u] Exiting writing loop."
+ "^?"
+ "^{MOVStreamHEVCLosslessEncoder=BB@iid^{OpaqueVTCompressionSession}{EncoderConfig=iiiidBBBBBi}{?=qiIq}IIIBB}"
+ "^{OpaqueVTCompressionSession=}"
+ "^{__CVBuffer=}32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
+ "^{__CVBuffer=}40@0:8^{__CVBuffer=}16@\"NSArray\"24^@32"
+ "^{__CVBuffer=}40@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}24^@32"
+ "^{__CVBuffer=}48@0:8o^{?=qiIq}16o^{CVSMPTETime=ssIIIssss}24o^B32o^@40"
+ "^{__CVBuffer=}56@0:8@16^{?=qiIq}24^{CVSMPTETime=ssIIIssss}32^B40^@48"
+ "^{opaqueCMFormatDescription=}"
+ "^{opaqueCMFormatDescription=}16@0:8"
+ "^{opaqueCMFormatDescription=}24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
+ "^{opaqueCMFormatDescription=}28@0:8^{opaqueCMFormatDescription=}16B24"
+ "^{opaqueCMFormatDescription=}32@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}24"
+ "^{opaqueCMFormatDescription=}32@0:8d16^@24"
+ "^{opaqueCMFormatDescription=}36@0:8d16B24^@28"
+ "^{opaqueCMSampleBuffer=}24@0:8^{?=qiIq}16"
+ "^{opaqueCMSampleBuffer=}48@0:8o^@16o^^{opaqueCMSampleBuffer}24o^{?=qiIq}32o^@40"
+ "^{opaqueCMSampleBuffer=}80@0:8{CVSMPTETime=ssIIIssss}16^{opaqueCMFormatDescription=}40{?=qiIq}48^@72"
+ "^{opaqueCMSimpleQueue=}"
+ "_assignedWritingThread"
+ "_associateToInput"
+ "_associatedInput"
+ "_associatedInputs"
+ "_attachmentsToEncode"
+ "_avMediaType"
+ "_avWriter"
+ "_aveHighPerfMode"
+ "_avfAppendMetadataSignPost"
+ "_bytesPerPixel"
+ "_callbackFunc"
+ "_capacity"
+ "_closed"
+ "_compressionSession"
+ "_copyData"
+ "_countingQueue"
+ "_customMOVMetadata"
+ "_customMetadata"
+ "_customMetadataItems"
+ "_defaultFrameRate"
+ "_defaultNotificationQueue"
+ "_drainWritingThreads"
+ "_enableAVEHighPerformanceProfile"
+ "_enableInProcessEncoding"
+ "_encoderCtrl"
+ "_encodingQueueDepth"
+ "_failHandler"
+ "_fifoBuffer"
+ "_filePath"
+ "_finishStepDefaultTimeout"
+ "_forceFinishWritingThreads"
+ "_formatDesc"
+ "_formatDescForEncoding"
+ "_frameRate"
+ "_frameReorderingEnabled"
+ "_futureAttachmentsDuration"
+ "_futureAttachmentsPts"
+ "_futureTimeCodeBuffer"
+ "_futureTimeCodePts"
+ "_group"
+ "_hasTimeCode"
+ "_inProcessRecording"
+ "_initFifoCapacity"
+ "_inputFormatDesc"
+ "_inputs"
+ "_inputsAvailableHandler"
+ "_keys"
+ "_lastAppendTimeStamp"
+ "_map"
+ "_mediaTimeScale"
+ "_metadataAdaptor"
+ "_metadataInput"
+ "_movie"
+ "_movieMetadataUtility"
+ "_observingIsReadyStatus"
+ "_originalTime"
+ "_pendingAttachments"
+ "_pendingSamples"
+ "_perfLogHandle"
+ "_preferCustomCompression"
+ "_preserveSessionStartTime"
+ "_processingQueue"
+ "_processingSignPostID"
+ "_processor"
+ "_prohibitDropping"
+ "_propertyKey"
+ "_propertyValue"
+ "_pts"
+ "_queue"
+ "_realTime"
+ "_sampleInput"
+ "_sessionStarted"
+ "_shouldOptimizeForNetworkUse"
+ "_status"
+ "_timeCode"
+ "_timeCodeAdaptor"
+ "_timeCodeFormatDesc"
+ "_timeCodeInput"
+ "_timecodeOutput"
+ "_useLegacyVTController"
+ "_useOwnProcessingQueue"
+ "_useOwnWritingThread"
+ "_uuid"
+ "_videoEncoderInterface"
+ "_waitSema"
+ "_warningHandler"
+ "_writeThreadAudio"
+ "_writeThreadMetadata"
+ "_writer"
+ "_writingMetadataSema"
+ "_writingThreads"
+ "_writingThreadsGroup"
+ "a"
+ "addAssociatedMetadataTracks:rawSampleAttachmentsIdentifier:trackKindIdentifier:error:"
+ "addInput:error:"
+ "addMovieMetadataItem:"
+ "addPointer:"
+ "adjustAVFCompressionProperties:encoderType:"
+ "alignedPTSTimeStamps:withSampleTimes:"
+ "allObjects"
+ "allOrderedKeys"
+ "allWriterInputs"
+ "appendAudioBuffer:error:"
+ "appendMetadata:"
+ "appendMetadata:error:"
+ "appendMetadata:withTimeStamp:error:"
+ "appendPixelBuffer:pts:error:"
+ "appendPixelBuffer:pts:timeCode:error:"
+ "appendSampleBuffer:attachments:error:"
+ "appendSampleBuffer:metadataGroup:error:"
+ "applyAdditionalHEVCCompressionPropertiesFromRecordingConfig:"
+ "applyChangesError:"
+ "applyDefaultSessionProperties"
+ "applyHighPerfSettings:"
+ "applyWriterTimeScaleToSampleInput"
+ "areAllInputsReady"
+ "assetWithURL:"
+ "assetWriterInputWithMediaType:outputSettings:sourceFormatHint:"
+ "assignedWritingThread"
+ "associateToInput"
+ "associatedInputs"
+ "attachmentsMIOMetadataItemForDictionary:pts:error:"
+ "attachmentsMIOMetadataItemForPixelBuffer:pts:error:"
+ "attachmentsMIOTimedMetadataGroupForDictionary:pts:error:"
+ "attachmentsMIOTimedMetadataGroupForPixelBuffer:pts:error:"
+ "attachmentsMIOTimedMetadataGroupForSampleBuffer:pts:error:"
+ "attachmentsMIOTimedMetadataItemForSampleBuffer:pts:error:"
+ "attachmentsToEncode"
+ "attachmentsTrackInAsset:forTrack:"
+ "audioSettingsFromConfig:"
+ "avMediaType"
+ "avWriter"
+ "avfAppendSignPostID"
+ "avfEncoderSpecForEncoderType:"
+ "awaitEncoderClosed"
+ "bufferHasPadding requires non-planar buffer."
+ "bufferingCapacity"
+ "bytesPerPixelForFormat requires non-planar buffer."
+ "bytesPerWidthOfBuffer requires non-planar buffer."
+ "canAddTrackAssociationWithTrackOfInput:type:"
+ "canAppend"
+ "canWrite"
+ "cancelRecordingWithCompletionHandler:"
+ "capacity"
+ "characterSetWithCharactersInString:"
+ "closeEncoderError:"
+ "closed"
+ "cmCodecTypeFromAVCodecType:"
+ "colorimetricWarningsForPixelBufferAttachments:pixelFormat:"
+ "com.apple.mio.processing.%@"
+ "com.apple.mio.processing.default"
+ "com.apple.mio.thread.%@"
+ "com.apple.movstreamwriter.writingthread.%u"
+ "com.apple.movstreamwriter.writingthread.metadata"
+ "combineLeftBuffer:rightBuffer:"
+ "commonTrackMetadataItems"
+ "compact"
+ "componentsSeparatedByCharactersInSet:"
+ "copyData"
+ "copyNextFrameForStream:timestamp:timeCode:tcDropFrame:error:"
+ "copyNextFrameForStreamTimestamp:timeCode:tcDropFrame:error:"
+ "copyWithNewPts:"
+ "countingQueue"
+ "createMIOMetadataAttachmentsFormatDescription"
+ "createMIOMetadataStreamFormatDescription"
+ "createMIOPixelBufferPoolWithWidth:height:pixelFormat:minBufferCount:maxBufferCount:bufferCacheMode:"
+ "createTimeCode32FormatDescriptionWithFrameRate:dropFrame:error:"
+ "createTimeCode32FormatDescriptionWithFrameRate:tcDropFrame:error:"
+ "createTimeCode64FormatDescriptionWithFrameRate:dropFrame:error:"
+ "createTimeCodeFormatDescriptionWithFrameRate:error:"
+ "createTimecode32SampleBufferWithSMPTETime:formatDescription:pts:error:"
+ "createTimecode64SampleBufferWithSMPTETime:formatDescription:pts:error:"
+ "createTimecodeSampleBufferWithSMPTETime:formatDescription:pts:error:"
+ "createxf20FormatDescriptionFromRawBayerFormatDescription:usingFirstPlaneOnly:"
+ "currentThread"
+ "customConfigWithOutputSettings:"
+ "customEncoderSettingsFromConfig:frameRate:enableAVEHighPerformanceProfile:"
+ "customMOVMetadata"
+ "customMetadata"
+ "customMetadataItems"
+ "customTrackMetadataForStream:mediaType:error:"
+ "customTrackMetadataItems:"
+ "customizeMetadataInput:"
+ "customizeSampleInput:"
+ "d20@0:8I16"
+ "d24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
+ "dataValue"
+ "defaultFrameRate"
+ "defaultNotificationQueue"
+ "dequeue"
+ "disableVTPreSetup"
+ "drainWritingThreads"
+ "emptyFifoBuffer"
+ "encodeFrame:pts:properties:context:error:"
+ "encodedPixelFormat"
+ "encoder:overrideVideoEncoderSpecificationForStreamId:"
+ "encoderTypeFromStreamData:"
+ "encodingQueueDepth"
+ "endSessionAtSourceTime:"
+ "enqueue:"
+ "establishAssociationsWithError:"
+ "fa\x12"
+ "fail"
+ "fifoBuffer"
+ "filePath"
+ "findAllAssociatedMetadataTracksInAsset:forTrack:"
+ "findTimeCodeTrackAssociatedWithTrack:"
+ "finishProcessing"
+ "finishProcessingInDispatchGroup:"
+ "finishWithCompletionHandler:"
+ "finishWithEndTime:completionHandler:"
+ "finishWithTimeout:completionHandler:"
+ "finishWithTimeout:endTime:completionHandler:"
+ "flush"
+ "forceFinishWritingThreads"
+ "formatDesc"
+ "formatDescriptionForEncoding"
+ "formatDescriptionHasChanged:"
+ "formatDescriptionOfTrack:containsKey:"
+ "frameNumber32ForTimecode:usingFormatDescription:"
+ "frameNumber64ForTimecode:usingFormatDescription:"
+ "futureAttachmentsDuration"
+ "futureAttachmentsPts"
+ "futureTimeCodeBuffer"
+ "futureTimeCodePts"
+ "getCustomAssociatedMetadataStreamIdFromTrack:"
+ "getFailHandler"
+ "getWarningHandler"
+ "hasTimeCode"
+ "hasTimeCodeForStream:"
+ "hevcAVFSettingsWithProfileLevel:encoderType:frameRate:dimensions:mastery:enableAVEHighPerformanceProfile:"
+ "hevcSettingsWithProfileLevel:frameRate:mastery:enableAVEHighPerformanceProfile:"
+ "i24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
+ "i48@0:8{CVSMPTETime=ssIIIssss}16^{opaqueCMFormatDescription=}40"
+ "inProcessRecording"
+ "initWithBytes:objCType:"
+ "initWithEncoderConfig:formtDescription:inProcessEncoding:frameRate:aveHighPerfMode:outputCallback:delegate:"
+ "initWithFilePath:error:"
+ "initWithInputFormatDescription:"
+ "initWithKey:value:"
+ "initWithName:block:"
+ "initWithPts:originalTime:"
+ "initWithStreamId:"
+ "initWithStreamId:audioFormat:additionalSettings:"
+ "initWithStreamId:copyData:"
+ "initWithStreamId:format:"
+ "initWithStreamId:format:associateToInput:"
+ "initWithStreamId:format:recordingConfig:"
+ "initWithStreamId:format:recordingConfig:timeCodeFormat:"
+ "inputSpecificTrackMetadataItems"
+ "inputs"
+ "invalidate"
+ "isMOVStreamIOMovMetadataIdentifier:"
+ "isPTSEqualOrCloseToTime:"
+ "isPTSEqualOrCloseToTime:tolerance:"
+ "isTrack:forStreamId:mediaType:"
+ "jpegEncoderConfig"
+ "jpegEncoderConfigWithQuality:"
+ "jpegSettings:frameRate:"
+ "lastAppendTimeStamp"
+ "m_convertL016toL010"
+ "m_preSetupFormatDescription"
+ "masteryFromConfig:formatDescription:frameRate:"
+ "masteryFromStreamData:withFrameRate:"
+ "masteryLossless"
+ "masteryWithBitrate:"
+ "masteryWithQuality:"
+ "matchingAVMediaTypeFromCMType:"
+ "matchingAVMediaTypeFromMIOMediaType:"
+ "matchingMIOMediaTypeFromCMType:"
+ "mdta/com.apple.framework.mio.session.starttime"
+ "mediaTimeScale"
+ "metadataAdaptor"
+ "metadataGroupForMetadataStreamFromData:timeStamp:copyData:"
+ "metadataInput"
+ "metadataItemsForMetadataStreamFromData:copyData:"
+ "mio.append.sample.buffer"
+ "mio.append.sample.buffer.attachments"
+ "mio.append.time.code.buffer"
+ "mio.append.timed.metadata.group"
+ "mio.counting.%@"
+ "mio.processing"
+ "mio.processing.%@"
+ "mio.processing.shared"
+ "mio.write.fifo.samples"
+ "mio.write.thread"
+ "mio.writer.cancel"
+ "mio.writer.finish"
+ "mio.writer.notifications"
+ "mio.writer.prepare"
+ "mio.writing.%@.%ld"
+ "mio.writing.default"
+ "mioMovieMetadataItem"
+ "monochrome10bitHEVCLosslessEncoderConfigAllowFrameReordering:"
+ "monochrome8bitHEVCLosslessEncoderConfigAllowFrameReordering:"
+ "movMetadataItemWithSessionStartTime:error:"
+ "movie"
+ "movieMetadataUtility"
+ "newWritingThreadWithName:"
+ "nextPixelBufferForStream:attachmentsData:timestamp:error:"
+ "nextPixelBufferForStreamAttachmentsData:timestamp:error:"
+ "nextSampleBufferForStream:attachmentsData:timestamp:error:"
+ "nextSampleBufferForStreamAttachmentsData:timecodeSampleBuffer:timestamp:error:"
+ "nextSampleBufferForStreamAttachmentsData:timestamp:error:"
+ "nextSampleBufferForStreamAttachmentsDataArray:timecodeSampleBuffer:timestamp:error:"
+ "nonMIOTrackMetadataItemsInMetadataItems:"
+ "numberWithBool:"
+ "observeIsReadyStatus"
+ "observingIsReadyStatus"
+ "onAVInputsAvailable:"
+ "openEncoderWithContext:error:"
+ "originalTime"
+ "outputSettings must not be nil."
+ "outputSettings:frameRate:dimensions:mastery:preferEncoderConfig:enableAVEHighPerformanceProfile:"
+ "outputSettingsMastery:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:"
+ "outputSettingsProResEncoderType:quality:formatDescription:preferEncoderConfig:"
+ "outputSettingsWithConfig:formatDescription:defaultFrameRate:preferEncoderConfig:enableAVEHighPerformanceProfile:"
+ "outputURL"
+ "overrideVideoEncoderSpecificationForStreamId"
+ "pendSample"
+ "pendingAttachments"
+ "pendingSamples"
+ "perfLogHandle"
+ "populateWriterError:message:code:"
+ "preSetupWithFormatDescription:"
+ "preferCustomCompression"
+ "prepareForAppendWithTimeStamp:error:"
+ "prepareInputFinished"
+ "prepareInputWithWriter:error:"
+ "prepareWriterWithCompletionHandler:"
+ "preserveSessionStartTime"
+ "proceed"
+ "processPixelBuffer:preserveAttachments:error:"
+ "processingQueue"
+ "processingSignPostID"
+ "processor"
+ "processorForConfig:formatDescription:"
+ "prohibitDropping"
+ "propagateColorAttachments"
+ "propertyKey"
+ "propertyValue"
+ "proposeSessionStartTime:"
+ "pts"
+ "q48@0:8{CVSMPTETime=ssIIIssss}16^{opaqueCMFormatDescription=}40"
+ "realTime"
+ "registerForAssociating:"
+ "reportError:"
+ "reportWarning:"
+ "requiresInProcessOperation"
+ "requiresSWEncoder:"
+ "resolveSample"
+ "sampleInput"
+ "sampleInputOutputSettings"
+ "sampleReorderingEnabled"
+ "saveSessionStartTime:toMovieAtURL:error:"
+ "sessionStartTimeOfMovie"
+ "setAssignedWritingThread:"
+ "setAvWriter:"
+ "setAvfAppendSignPostID:"
+ "setBufferingCapacity:"
+ "setCopyData:"
+ "setCustomMOVMetadata:"
+ "setCustomMetadata:"
+ "setCustomMetadataItems:"
+ "setCustomTrackMetadataForStream:mediaType:metadata:error:"
+ "setDefaultFrameRate:"
+ "setDefaultNotificationQueue:"
+ "setDrainWritingThreads:"
+ "setEnableAVEHighPerformanceProfile:"
+ "setEncodingQueueDepth:"
+ "setFailHandler:"
+ "setForceFinishWritingThreads:"
+ "setFutureAttachmentsDuration:"
+ "setFutureAttachmentsPts:"
+ "setFutureTimeCodeBuffer:"
+ "setFutureTimeCodePts:"
+ "setHasTimeCode:"
+ "setInProcessRecording:"
+ "setLastAppendTimeStamp:"
+ "setMovie:"
+ "setMovieMetadata:"
+ "setNaturalSize:"
+ "setObservingIsReadyStatus:"
+ "setOriginalTime:"
+ "setPerfLogHandle:"
+ "setPreferCustomCompression:"
+ "setPreserveSessionStartTime:"
+ "setProcessingSignPostID:"
+ "setProhibitDropping:"
+ "setPts:"
+ "setRealTime:"
+ "setStatus:"
+ "setTimeCode:"
+ "setTimecodeOutput:"
+ "setUseLegacyVTController:"
+ "setUseOwnProcessingQueue:"
+ "setUseOwnWritingThread:"
+ "setVideoTransform:forStream:"
+ "setWarningHandler:"
+ "setWriter:"
+ "setupInputsWithWriter:error:"
+ "setupSignPost"
+ "shouldEnableInProcessEncoding"
+ "shutDownOutError:"
+ "signalWritingThreadsProceed"
+ "startSession"
+ "startWriting canceled because writer is not in state that allows writing."
+ "startWritingThreadForMetadata"
+ "startWritingThreadForNonMetadataOnlyThreadId:"
+ "stats"
+ "stopObservingIsReadyStatus"
+ "stringFromTimeCode:dropFrame:"
+ "stripBufferPadding requires non-planar buffer."
+ "supportsEncoderType:"
+ "timeCode"
+ "timeCodeAdaptor"
+ "timeCodeBufferForStream:"
+ "timeCodeFormatDescription"
+ "timeCodeFormatDescriptionStream:"
+ "timeCodeFromString:isDropFrame:"
+ "timeCodeInput"
+ "timePairWithPts:originalTime:"
+ "timePairsForStream:mediaType:inAsset:error:"
+ "timePairsForStream:mediaType:inAssetURL:error:"
+ "timecode32ForSampleBuffer:dropFrame:"
+ "timecodeForFrameNumber32:formatDescription:"
+ "timecodeOutput"
+ "trackEnabled"
+ "trackForStreamId:mediaType:error:"
+ "trackMetadataForSceneStream:"
+ "trackMetadataForStream:withMediaType:"
+ "trackMetadataForVideoStream:"
+ "trackMetadataItemWithEncodedPixelFormat:"
+ "trackMetadataItemWithExactBytesPerRow:pixelFormat:"
+ "trackMetadataItemWithInputPixelFormat:"
+ "trackMetadataItemWithRawBayerRearrangeType:"
+ "trackMetadataItemWithSerializationMode:"
+ "trackMetadataItemWithStreamId:"
+ "transferL010PixelBuffer:toq8q2PixelBuffer:"
+ "transferq8q2PixelBuffer:toL010PixelBuffer:"
+ "usage"
+ "useLegacyVTController"
+ "useOwnProcessingQueue"
+ "useOwnWritingThread"
+ "uuid"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?16"
+ "v28@0:8@16i24"
+ "v32@0:8d16@?24"
+ "v48@0:8^{opaqueCMSampleBuffer=}16@24@32Q40"
+ "v48@0:8{?=qiIq}16@?40"
+ "v56@0:8d16{?=qiIq}24@?48"
+ "valueAsMovSessionStartTime"
+ "verifyNewAppendTimeStamp:error:"
+ "videoEncoderInterface"
+ "waitWithTimeout:"
+ "weakObjectsPointerArray"
+ "write fifo metadata"
+ "write thread metadata"
+ "writeMovieHeaderToURL:fileType:options:error:"
+ "writeNextItemFromFifo"
+ "writeNextItemFromFifo canceled because writer does not allow writing anymore."
+ "writeSampleBuffer:andMetadata:forStreamId:signpost:"
+ "writeVideoFrameStreamAttachmentsData:toMetadataAdaptor:ofStream:signpost:"
+ "writer"
+ "writerInputs"
+ "writerInputsWithMediaType:"
+ "writerInputsWithMediaType:streamId:"
+ "yzip"
+ "{?=IiI}"
+ "{CVSMPTETime=ssIIIssss}28@0:8i16^{opaqueCMFormatDescription=}20"
+ "{CVSMPTETime=ssIIIssss}32@0:8@16o^B24"
+ "{CVSMPTETime=ssIIIssss}32@0:8^{opaqueCMSampleBuffer=}16^B24"
+ "\xd2"
+ "\xd5\x11"
+ "⚠️⚠️⚠️ WARNING [MOVStreamIO]: Selected output file type is 'mp4'. Be aware that this can and will cause data loss. If you can please use QuickTime Movie('.mov'). ⚠️⚠️⚠️"
+ "\xf0\xf0\xf0\xe2"
- "\x06\x12\xf0\xf0A31"
- "-[MOVStreamReaderStreamOutput nextSampleBufferForStreamAttachementsData:timestamp:error:]"
- "3.21.0"
- "@\"NSData\""
- "@24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
- "@32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16d24"
- "@36@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16d24B32"
- "A\x12"
- "B24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
- "B40@0:8^{__CVBuffer=}16^{__CVBuffer=}24Q32"
- "B40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__long=*Qb63b1}{__short=[23c][0C]b7b1}{__raw=[3Q]})}}}16"
- "BytesPerPixelLookUp: Register %zu for %@"
- "I24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
- "Q20@0:8I16"
- "Q32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16d24"
- "T@\"NSData\",&,V_futureAttachmentsData"
- "T{?=qiIq},V_futureAttachementsDuration"
- "T{?=qiIq},V_futureAttachementsPts"
- "UQ\x12"
- "^{MOVStreamHEVCLosslessEncoder=B@iid^{OpaqueVTCompressionSession}{EncoderConfig=iiiidBBBBBi}{?=qiIq}IIIBB}"
- "^{__CVBuffer=}40@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}24^@32"
- "^{opaqueCMFormatDescription=}24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
- "^{opaqueCMFormatDescription=}32@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}24"
- "_futureAttachementsDuration"
- "_futureAttachementsPts"
- "createxf20FormatDescriptionFromRawBayerFormatDescription:"
- "d24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
- "encoder:overrideVideoEncoderSpecificationForstreamId:"
- "findAllAssociatedMetadataTrackInAsset:forTrack:"
- "futureAttachementsDuration"
- "futureAttachementsPts"
- "getKeyFromMetadataTrack:"
- "marksOutputTracksAsEnabledForStream:"
- "mio.appendTimedMetadataGroup"
- "overrideVideoEncoderSpecificationForstreamId"
- "setFutureAttachementsDuration:"
- "setFutureAttachementsPts:"
- "writeSampleBuffer:andMetadata:forStreamId:"
- "writeVideoFrameStreamAttachmentsData:toMetadataAdaptor:ofStream:"
- "\xa5\x11"
- "\xf0\xf0\xf0\x92"

```
