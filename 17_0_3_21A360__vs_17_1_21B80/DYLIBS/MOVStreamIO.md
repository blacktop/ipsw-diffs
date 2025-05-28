## MOVStreamIO

> `/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO`

```diff

-3.19.9.0.0
-  __TEXT.__text: 0x39b48
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x2d74
-  __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x3d2d
-  __TEXT.__oslogstring: 0x19d9
-  __TEXT.__gcc_except_tab: 0x5ee4
+3.21.0.0.0
+  __TEXT.__text: 0x40f2c
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__objc_methlist: 0x31e4
+  __TEXT.__const: 0x250
+  __TEXT.__cstring: 0x44ea
+  __TEXT.__oslogstring: 0x23d9
+  __TEXT.__gcc_except_tab: 0x6a64
   __TEXT.__ustring: 0x74
-  __TEXT.__unwind_info: 0x17dc
+  __TEXT.__unwind_info: 0x19f8
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x782
-  __TEXT.__objc_methname: 0x7592
-  __TEXT.__objc_methtype: 0x3b97
-  __TEXT.__objc_stubs: 0x50a0
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0x370
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__objc_classname: 0x88e
+  __TEXT.__objc_methname: 0x8585
+  __TEXT.__objc_methtype: 0x3ed2
+  __TEXT.__objc_stubs: 0x5980
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9be8
-  __DATA_CONST.__objc_selrefs: 0x1a48
-  __DATA_CONST.__objc_arraydata: 0x210
-  __AUTH_CONST.__cfstring: 0x3020
-  __AUTH_CONST.__objc_const: 0x1168
-  __AUTH_CONST.__objc_intobj: 0x390
-  __AUTH_CONST.__const: 0x250
+  __DATA_CONST.__objc_const: 0x85d8
+  __DATA_CONST.__objc_selrefs: 0x1d60
+  __DATA_CONST.__objc_arraydata: 0x228
+  __AUTH_CONST.__cfstring: 0x3360
+  __AUTH_CONST.__objc_const: 0x11b0
+  __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__const: 0x270
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x660
-  __AUTH.__objc_data: 0xff0
+  __AUTH_CONST.__auth_got: 0x6e8
+  __AUTH.__objc_data: 0x1090
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x288
-  __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_classrefs: 0x298
+  __DATA.__objc_superrefs: 0xb8
+  __DATA.__objc_ivar: 0x288
   __DATA.__data: 0x7e0
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xf8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1075
-  Symbols:   4332
-  CStrings:  2065
+  Functions: 1170
+  Symbols:   4646
+  CStrings:  2312
 
Symbols:
+ +[MIOPixelBufferPool createMIOPixelBufferPoolWithWidth:height:pixelFormat:exactBytesPerRow:minBufferCount:bufferCacheMode:]
+ +[MIOPixelBufferPool createMIOPixelBufferPoolWithWidth:height:pixelFormat:exactBytesPerRows:minBufferCount:bufferCacheMode:]
+ +[MIOPixelBufferPool createMIOPixelBufferPoolWithWidth:height:pixelFormat:extendedPixelsPerRow:minBufferCount:bufferCacheMode:]
+ +[MIOPixelBufferPool createMIOPixelBufferPoolWithWidth:height:pixelFormat:minBufferCount:bufferCacheMode:]
+ +[MIOPixelBufferPool createNewL008MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:bufferCacheMode:]
+ +[MIOPixelBufferPool createNewL010MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:bufferCacheMode:]
+ +[MIOPixelBufferPool makeBufferConfigDict:height:pixelFormat:bufferCacheMode:]
+ +[MIOPixelBufferUtility bufferHasPadding:]
+ +[MIOPixelBufferUtility bytesPerWidthOfBuffer:]
+ +[MIOPixelBufferUtility concatPixelBuffer:withPixelBuffer:targetPixelBuffer:]
+ +[MIOPixelBufferUtility copyAlphaChannelOfBuffer:toMonochromeBuffer:]
+ +[MIOPixelBufferUtility copyAlphaChannelOfBuffer:touint16Data:]
+ +[MIOPixelBufferUtility copyData:toNonPlanarPixelBuffer:]
+ +[MIOPixelBufferUtility copyData:toPlanarPixelBuffer:toPlane:]
+ +[MIOPixelBufferUtility copyFromPixelBuffer:toPixelBuffer:andShiftBits:]
+ +[MIOPixelBufferUtility copyMonochromeBuffer:toAlphaChannelOfBuffer:]
+ +[MIOPixelBufferUtility copyNonPlanarPixelBufferData:]
+ +[MIOPixelBufferUtility copyPixelBuffer:toPixelBuffer:bytesPerPixel:]
+ +[MIOPixelBufferUtility copyPixelBufferData:ofPlane:]
+ +[MIOPixelBufferUtility copyuint16Data:toAlphaChannelOfBuffer:]
+ +[MIOPixelBufferUtility create4444AYpCbCr16PixelBufferFillAlphaWithData:width:height:]
+ +[MIOPixelBufferUtility createNewL008PixelBufferPoolWithReferencePixelBuffer:minimumBufferCount:]
+ +[MIOPixelBufferUtility createNewL010PixelBufferPoolWithReferencePixelBuffer:minimumBufferCount:]
+ +[MIOPixelBufferUtility createPixelBufferAttributesWithWidth:height:extendedPixelsPerRow:pixelFormat:bytesPerRowAlignment:planeAlignment:]
+ +[MIOPixelBufferUtility createPixelBufferAttributesWithWidth:height:extendedPixelsPerRow:pixelFormat:bytesPerRowAlignment:planeAlignment:bufferCacheMode:]
+ +[MIOPixelBufferUtility createPixelBufferAttributesWithWidth:height:pixelFormat:bytesPerRow:]
+ +[MIOPixelBufferUtility createPixelBufferAttributesWithWidth:height:pixelFormat:bytesPerRows:]
+ +[MIOPixelBufferUtility createPixelBufferPoolWithWidth:height:format:bytesPerRow:minBufferCount:]
+ +[MIOPixelBufferUtility createPixelBufferPoolWithWidth:height:format:bytesPerRows:minBufferCount:]
+ +[MIOPixelBufferUtility createPixelBufferPoolWithWidth:height:format:extendedPixelsPerRow:minBufferCount:]
+ +[MIOPixelBufferUtility createPixelBufferPoolWithWidth:height:format:extendedPixelsPerRow:minBufferCount:bufferCacheMode:]
+ +[MIOPixelBufferUtility createRawPixelBufferWithWidth:height:extendedRows:extendedPixelsPerRow:pixelFormat:bytesPerRowAlignment:planeAlignment:bufferCacheMode:]
+ +[MIOPixelBufferUtility createRawPixelBufferWithWidth:height:pixelFormat:bytesPerRow:]
+ +[MIOPixelBufferUtility extendedPixelsPerRowOfPixelBuffer:]
+ +[MIOPixelBufferUtility extendedPixelsRightForPlanarBufferWidth:height:bytesPerRow:format:]
+ +[MIOPixelBufferUtility fillPlaneOfPixelBuffer:planeIndex:withValue:]
+ +[MIOPixelBufferUtility histogramOf8BitBuffer:]
+ +[MIOPixelBufferUtility isPixelBufferCompandedRawBayer:]
+ +[MIOPixelBufferUtility isPixelBufferRawBayer:]
+ +[MIOPixelBufferUtility isPixelFormatCompandedRawBayer:]
+ +[MIOPixelBufferUtility isPixelFormatRawBayer:]
+ +[MIOPixelBufferUtility joinCompandedWarholBuffer:intoCompandedBayerBuffer:]
+ +[MIOPixelBufferUtility joinWarholBuffer:intoBayerBuffer:shiftBitsRightBy:msbReplication:]
+ +[MIOPixelBufferUtility joinYUVBuffer:intoRawBayerPixelBuffer:shiftBitsLeftBy:msbReplication:]
+ +[MIOPixelBufferUtility newPixelBufferRefCopy:]
+ +[MIOPixelBufferUtility newPixelBufferRefCopy:attachmentKeysToCopy:]
+ +[MIOPixelBufferUtility newRawBayerBufferFromYUVPixelBuffer:withPixelBufferPool:msbReplication:]
+ +[MIOPixelBufferUtility newWarholBufferFromCompandedRawBayerPixelBuffer:withPixelBufferPool:]
+ +[MIOPixelBufferUtility newWarholBufferFromRawBayerPixelBuffer:]
+ +[MIOPixelBufferUtility newWarholBufferFromRawBayerPixelBuffer:withPixelBufferPool:]
+ +[MIOPixelBufferUtility newYUVBufferFromRawBayerPixelBuffer:withPixelBufferPool:]
+ +[MIOPixelBufferUtility numberOfPlanesForPixelFormatType:]
+ +[MIOPixelBufferUtility pixelBufferFromPool:]
+ +[MIOPixelBufferUtility pixelBufferSizeWithPadding:]
+ +[MIOPixelBufferUtility rangesOf8BitBuffer:]
+ +[MIOPixelBufferUtility readFrameFromFile:width:height:pixelFormat:]
+ +[MIOPixelBufferUtility sharedBytesPerPixelLookUp]
+ +[MIOPixelBufferUtility splitBayerBuffer:intoWarholPixelBuffer:shiftBitsLeftBy:]
+ +[MIOPixelBufferUtility splitBayerBuffer:intoYUVPixelBuffer:shiftBitsLeftBy:]
+ +[MIOPixelBufferUtility splitCompandedBayerBuffer:intoCompandedWarholPixelBuffer:]
+ +[MIOPixelBufferUtility stripBufferPadding:]
+ +[MIOPixelBufferUtility verticallySplitPixelBuffer:intoTopPixelBuffer:bottomPixelBuffer:]
+ +[MIOPixelBufferUtility writeBuffer:ofSize:toFile:]
+ +[MIOPixelBufferUtility writeBuffer:toFile:]
+ +[MOVStreamIOUtility attachmentsContainTopLeftChromaLocations:]
+ +[MOVStreamIOUtility attachmentsContainsRec2020orRec2100ColorMatrices:]
+ +[MOVStreamIOUtility attachmentsContainsRec2020orRec2100ColorPrimaries:]
+ +[MOVStreamIOUtility attachmentsRepresentInterlacedFields:]
+ +[MOVStreamIOUtility chromaSubsamplingForDictionary:]
+ +[MOVStreamIOUtility chromaSubsamplingForFormatDescription:]
+ +[MOVStreamIOUtility colorimetricWarningsForColorPixelBufferAttachments:pixelFormat:]
+ +[MOVStreamIOUtility colorimetricWarningsForGrayscalePixelBufferAttachments:pixelFormat:]
+ +[MOVStreamIOUtility configWithEncoderType:]
+ +[MOVStreamIOUtility dictionary:booleanValueForKey:]
+ +[MOVStreamIOUtility dictionary:numberValueForKey:]
+ +[MOVStreamIOUtility dictionary:stringValueForKey:]
+ +[MOVStreamIOUtility formatDescriptionRepresentsBayer:]
+ +[MOVStreamIOUtility formatDescriptionRepresentsGrayscale:]
+ +[MOVStreamIOUtility formatDescriptionRepresentsRGB:]
+ +[MOVStreamIOUtility formatDescriptionRepresentsVideoRange:]
+ +[MOVStreamIOUtility formatDescriptionRepresentsYCbCr:]
+ +[MOVStreamIOUtility isSlimXEncodedTrack:]
+ +[MOVStreamIOUtility key:hasUnspecifiedValue:]
+ +[MOVStreamIOUtility pixelFormatIs420Sampled:]
+ +[MOVStreamIOUtility pixelFormatIs422Sampled:]
+ +[MOVStreamIOUtility(Private) reservedMIOTrackMetadataKeys]
+ +[MOVStreamMetalPixelBufferUtility sharedMetalPixelBufferUtility]
+ +[MOVStreamOutputSettings addAdditionalHEVCCompressionProperties:recordingConfig:]
+ +[MOVStreamOutputSettings proresRAWHQSettings:frameRate:]
+ +[MOVStreamOutputSettings proresRAWSettings:frameRate:]
+ +[MOVStreamPostProcessorFactory defaultFactory]
+ +[MOVStreamPreProcessorFactory defaultFactory]
+ +[MOVStreamVideoEncoderInterface createHEVCCompatiblePixelBuffer:]
+ +[NSError(MOVStreamIO) writerErrorWithMessage:code:]
+ -[MOVStreamCompandedRawBayerPostProcessor processedPixelBufferFrom:metadata:error:]
+ -[MOVStreamCompandedRawBayerPostProcessor processedPixelFormat]
+ -[MOVStreamCompandedRawBayerPreProcessor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamCompandedRawBayerPreProcessor encodedPixelFormatFromStreamData:]
+ -[MOVStreamCompandedRawBayerPreProcessor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamCompandedRawBayerPreProcessor inputPixelFormatFromStreamData:]
+ -[MOVStreamCompandedRawBayerPreProcessor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamDefaultPostProcessor .cxx_destruct]
+ -[MOVStreamDefaultPostProcessor bufferCacheMode]
+ -[MOVStreamDefaultPostProcessor dealloc]
+ -[MOVStreamDefaultPostProcessor exactBytesPerRow]
+ -[MOVStreamDefaultPostProcessor initWithOriginalPixelFormat:]
+ -[MOVStreamDefaultPostProcessor initWithOriginalPixelFormat:bufferCacheMode:]
+ -[MOVStreamDefaultPostProcessor minimumBytesPerRowForPixelBuffer:]
+ -[MOVStreamDefaultPostProcessor originalPixelFormat]
+ -[MOVStreamDefaultPostProcessor pixelBufferWithExactBytesPerRow:fromPixelBuffer:error:]
+ -[MOVStreamDefaultPostProcessor pixelBufferWithoutPaddingFromPixelBuffer:error:]
+ -[MOVStreamDefaultPostProcessor processedPixelBufferFrom:metadata:error:]
+ -[MOVStreamDefaultPostProcessor processedPixelFormat]
+ -[MOVStreamDefaultPostProcessor removePadding]
+ -[MOVStreamDefaultPostProcessor setBufferCacheMode:]
+ -[MOVStreamDefaultPostProcessor setExactBytesPerRow:]
+ -[MOVStreamDefaultPostProcessor setOriginalPixelFormat:]
+ -[MOVStreamDefaultPostProcessor setRemovePadding:]
+ -[MOVStreamDefaultPostProcessor shouldChangeBytesPerRowOfPixelBuffer:]
+ -[MOVStreamDefaultPostProcessor shouldRemovePaddingOfPixelBuffer:metadata:]
+ -[MOVStreamDefaultPreProcessor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamDefaultPreProcessor encodedPixelFormatFromStreamData:]
+ -[MOVStreamDefaultPreProcessor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamDefaultPreProcessor inputPixelFormatFromStreamData:]
+ -[MOVStreamDefaultPreProcessor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamFrameConverter initWithTargetWidth:height:format:bytesPerRow:bufferCacheMode:]
+ -[MOVStreamFrameConverter initWithTargetWidth:height:format:bytesPerRows:bufferCacheMode:]
+ -[MOVStreamFrameConverter initWithTargetWidth:height:format:extendedPixelsPerRow:bufferCacheMode:]
+ -[MOVStreamFrameTransform initWithRotation:flip:bufferCacheMode:]
+ -[MOVStreamFrameTransform initWithRotation:flip:bufferCacheMode:].cold.1
+ -[MOVStreamL008ToNonPlanarPostProcessor .cxx_destruct]
+ -[MOVStreamL008ToNonPlanarPostProcessor adjustedWidthForWidth:]
+ -[MOVStreamL008ToNonPlanarPostProcessor processedPixelBufferFrom:metadata:error:]
+ -[MOVStreamL008ToNonPlanarPostProcessor processedPixelFormat]
+ -[MOVStreamL016Raw14PostProcessor .cxx_destruct]
+ -[MOVStreamL016Raw14PostProcessor initWithOriginalPixelFormat:bufferCacheMode:l010OutputFormatRAW14L016:]
+ -[MOVStreamL016Raw14PostProcessor initWithOriginalPixelFormat:l010OutputFormatRAW14L016:]
+ -[MOVStreamL016Raw14PostProcessor l010OutputFormatRAW14L016]
+ -[MOVStreamL016Raw14PostProcessor processedPixelBufferFrom:metadata:error:]
+ -[MOVStreamL016Raw14PostProcessor processedPixelFormat]
+ -[MOVStreamL016Raw14PostProcessor setL010OutputFormatRAW14L016:]
+ -[MOVStreamL016Raw14PreProcessor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamL016Raw14PreProcessor encodedPixelFormatFromStreamData:]
+ -[MOVStreamL016Raw14PreProcessor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamL016Raw14PreProcessor inputPixelFormatFromStreamData:]
+ -[MOVStreamL016Raw14PreProcessor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamMetalPixelBufferUtility .cxx_destruct]
+ -[MOVStreamMetalPixelBufferUtility enabled]
+ -[MOVStreamMetalPixelBufferUtility init]
+ -[MOVStreamMetalPixelBufferUtility joinCompandedWarholBuffer:intoCompandedBayerBuffer:]
+ -[MOVStreamMetalPixelBufferUtility joinWarholBuffer:intoBayerBuffer:shiftBitsRightBy:msbReplication:]
+ -[MOVStreamMetalPixelBufferUtility joinYUVBuffer:intoRawBayerPixelBuffer:shiftBitsLeftBy:msbReplication:]
+ -[MOVStreamMetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:]
+ -[MOVStreamMetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:].cold.1
+ -[MOVStreamMetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:].cold.2
+ -[MOVStreamMetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:].cold.3
+ -[MOVStreamMetalPixelBufferUtility setEnabled:]
+ -[MOVStreamMetalPixelBufferUtility splitBayerBuffer:intoWarholPixelBuffer:shiftBitsLeftBy:]
+ -[MOVStreamMetalPixelBufferUtility splitBayerBuffer:intoYUVPixelBuffer:shiftBitsLeftBy:]
+ -[MOVStreamMetalPixelBufferUtility splitCompandedBayerBuffer:intoCompandedWarholPixelBuffer:]
+ -[MOVStreamNonPlanarToL008Processor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamNonPlanarToL008Processor encodedPixelFormatFromStreamData:]
+ -[MOVStreamNonPlanarToL008Processor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamNonPlanarToL008Processor inputPixelFormatFromStreamData:]
+ -[MOVStreamNonPlanarToL008Processor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamOutputSettings setConfig:]
+ -[MOVStreamOutputSettings setSettings:]
+ -[MOVStreamPostProcessorFactory postProcessorFromReader:originalPixelFormat:encodedFormat:encoderType:streamId:]
+ -[MOVStreamPostProcessorFactory postProcessorFromReader:originalPixelFormat:encodedFormat:encoderType:streamId:bufferCacheMode:]
+ -[MOVStreamPreProcessorFactory preProcessorForFormat:recordingConfiguration:]
+ -[MOVStreamRawBayerFromYUVPostProcessor initWithOriginalPixelFormat:bufferCacheMode:rawBayerMSBReplication:]
+ -[MOVStreamRawBayerFromYUVPostProcessor initWithOriginalPixelFormat:rawBayerMSBReplication:]
+ -[MOVStreamRawBayerFromYUVPostProcessor processedPixelBufferFrom:metadata:error:]
+ -[MOVStreamRawBayerFromYUVPostProcessor processedPixelFormat]
+ -[MOVStreamRawBayerFromYUVPostProcessor rawBayerMSBReplication]
+ -[MOVStreamRawBayerFromYUVPostProcessor setRawBayerMSBReplication:]
+ -[MOVStreamRawBayerPostProcessor initWithOriginalPixelFormat:bufferCacheMode:rawBayerMSBReplication:]
+ -[MOVStreamRawBayerPostProcessor initWithOriginalPixelFormat:rawBayerMSBReplication:]
+ -[MOVStreamRawBayerPostProcessor processedPixelBufferFrom:metadata:error:]
+ -[MOVStreamRawBayerPostProcessor processedPixelFormat]
+ -[MOVStreamRawBayerPostProcessor rawBayerMSBReplication]
+ -[MOVStreamRawBayerPostProcessor setRawBayerMSBReplication:]
+ -[MOVStreamRawBayerPreProcessor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamRawBayerPreProcessor encodedPixelFormatFromStreamData:]
+ -[MOVStreamRawBayerPreProcessor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamRawBayerPreProcessor inputPixelFormatFromStreamData:]
+ -[MOVStreamRawBayerPreProcessor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamRawBayerTo1stPlaneYUVPreProcessor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamRawBayerTo1stPlaneYUVPreProcessor encodedPixelFormatFromStreamData:]
+ -[MOVStreamRawBayerTo1stPlaneYUVPreProcessor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamRawBayerTo1stPlaneYUVPreProcessor inputPixelFormatFromStreamData:]
+ -[MOVStreamRawBayerTo1stPlaneYUVPreProcessor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamRawBayerToYUVPreProcessor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamRawBayerToYUVPreProcessor encodedPixelFormatFromStreamData:]
+ -[MOVStreamRawBayerToYUVPreProcessor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamRawBayerToYUVPreProcessor inputPixelFormatFromStreamData:]
+ -[MOVStreamRawBayerToYUVPreProcessor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamRawBayerToy416PreProcessor createTrackFormatDescriptionFromStreamData:]
+ -[MOVStreamRawBayerToy416PreProcessor encodedPixelFormatFromStreamData:]
+ -[MOVStreamRawBayerToy416PreProcessor formatDescriptionForPixelBuffer:streamData:]
+ -[MOVStreamRawBayerToy416PreProcessor inputPixelFormatFromStreamData:]
+ -[MOVStreamRawBayerToy416PreProcessor processedPixelBufferCopyOf:streamData:error:]
+ -[MOVStreamReader bufferCacheMode]
+ -[MOVStreamReader customTrackMetadataItemsForStream:]
+ -[MOVStreamReader getOutputPixelFormatWasGuessedForStream:]
+ -[MOVStreamReader setBufferCacheMode:]
+ -[MOVStreamReader setSkipEmptyEditVideoFrame:]
+ -[MOVStreamReader skipEmptyEditVideoFrame]
+ -[MOVStreamReaderStreamOutput customTrackMetadataItems]
+ -[MOVStreamReaderStreamOutput firstVideoFrameRead]
+ -[MOVStreamReaderStreamOutput getOutputPixelFormatWasGuessedForStream]
+ -[MOVStreamReaderStreamOutput initWithVideoTrack:assetReader:associatedMetadataTracks:version:bufferCacheMode:unknownStreamId:reader:delegate:error:]
+ -[MOVStreamReaderStreamOutput isEmptySample:]
+ -[MOVStreamReaderStreamOutput pixelFormatWasGuessed]
+ -[MOVStreamReaderStreamOutput setFirstVideoFrameRead:]
+ -[MOVStreamReaderStreamOutput setPixelFormatWasGuessed:]
+ -[MOVStreamSampleBufferAndMetadata .cxx_destruct]
+ -[MOVStreamSampleBufferAndMetadata metadata]
+ -[MOVStreamSampleBufferAndMetadata sampleBuffer]
+ -[MOVStreamSampleBufferAndMetadata setMetadata:]
+ -[MOVStreamSampleBufferAndMetadata setSampleBuffer:]
+ -[MOVStreamSampleTimeBuffer .cxx_construct]
+ -[MOVStreamSampleTimeBuffer .cxx_destruct]
+ -[MOVStreamSampleTimeBuffer appendTime:]
+ -[MOVStreamSampleTimeBuffer description]
+ -[MOVStreamSampleTimeBuffer initWithCapacity:]
+ -[MOVStreamSampleTimeBuffer init]
+ -[MOVStreamSampleTimeBuffer isEmpty]
+ -[MOVStreamSampleTimeBuffer name]
+ -[MOVStreamSampleTimeBuffer setName:]
+ -[MOVStreamSampleTimeBuffer timeline]
+ -[MOVStreamSampleTimeList .cxx_construct]
+ -[MOVStreamSampleTimeList .cxx_destruct]
+ -[MOVStreamSampleTimeList cached_cmtimes]
+ -[MOVStreamSampleTimeList cached_times]
+ -[MOVStreamSampleTimeList cmtimes]
+ -[MOVStreamSampleTimeList count]
+ -[MOVStreamSampleTimeList description]
+ -[MOVStreamSampleTimeList frameRangeFrom:to:]
+ -[MOVStreamSampleTimeList initWithTimes:]
+ -[MOVStreamSampleTimeList initWithTimestamps:]
+ -[MOVStreamSampleTimeList init]
+ -[MOVStreamSampleTimeList name]
+ -[MOVStreamSampleTimeList setName:]
+ -[MOVStreamSampleTimeList setTimestamps:]
+ -[MOVStreamSampleTimeList timeAtIndex:]
+ -[MOVStreamSampleTimeList timeRangeFrom:to:]
+ -[MOVStreamSampleTimeList times]
+ -[MOVStreamSampleTimeList timestamps]
+ -[MOVStreamSampleTimeRangeBuffer .cxx_construct]
+ -[MOVStreamSampleTimeRangeBuffer .cxx_destruct]
+ -[MOVStreamSampleTimeRangeBuffer appendTimeRange:]
+ -[MOVStreamSampleTimeRangeBuffer initWithCapacity:]
+ -[MOVStreamSampleTimeRangeBuffer init]
+ -[MOVStreamSampleTimeRangeBuffer timeRangeList]
+ -[MOVStreamSampleTimeRangeList .cxx_construct]
+ -[MOVStreamSampleTimeRangeList .cxx_destruct]
+ -[MOVStreamSampleTimeRangeList cached_ranges]
+ -[MOVStreamSampleTimeRangeList containsTimeRange:]
+ -[MOVStreamSampleTimeRangeList copyWithZone:]
+ -[MOVStreamSampleTimeRangeList indexOfTimeRangeAtTime:]
+ -[MOVStreamSampleTimeRangeList initWithTimeRange:]
+ -[MOVStreamSampleTimeRangeList initWithTimeRanges:]
+ -[MOVStreamSampleTimeRangeList init]
+ -[MOVStreamSampleTimeRangeList name]
+ -[MOVStreamSampleTimeRangeList setName:]
+ -[MOVStreamSampleTimeRangeList timeRangeAtIndex:]
+ -[MOVStreamSampleTimeRangeList timeRange]
+ -[MOVStreamVideoEncoderInterface .cxx_destruct]
+ -[MOVStreamVideoEncoderInterface closeEncoderInDispatchGroup:]
+ -[MOVStreamVideoEncoderInterface closeEncoder]
+ -[MOVStreamVideoEncoderInterface codecTypeOverride]
+ -[MOVStreamVideoEncoderInterface configureSessionOverride:]
+ -[MOVStreamVideoEncoderInterface customEncoderConfig]
+ -[MOVStreamVideoEncoderInterface dealloc]
+ -[MOVStreamVideoEncoderInterface encodeFrame:pts:frameProperties:metadata:]
+ -[MOVStreamVideoEncoderInterface frameReorderingEnabled]
+ -[MOVStreamVideoEncoderInterface initForStream:configuration:delegate:]
+ -[MOVStreamVideoEncoderInterface initWithExpectedFrameRate:forStream:delegate:enableAVEHighPerformanceProfile:]
+ -[MOVStreamVideoEncoderInterface init]
+ -[MOVStreamVideoEncoderInterface lastEncodingInfoFlags]
+ -[MOVStreamVideoEncoderInterface lastEncodingStatus]
+ -[MOVStreamVideoEncoderInterface overrideVideoEncoderSpecification]
+ -[MOVStreamVideoEncoderInterface pendingFrames]
+ -[MOVStreamVideoEncoderInterface processFrame:pts:frameProperties:metadata:]
+ -[MOVStreamVideoEncoderInterface setCustomEncoderConfig:]
+ -[MOVStreamVideoEncoderInterface setPendingFrames:]
+ -[MOVStreamVideoEncoderInterface setupEncoderWithWidth:andHeight:imageFormat:formatDescription:andFramerate:]
+ -[MOVStreamVideoEncoderInterface skipFrameWithStatus:andFlags:]
+ -[MOVStreamVideoEncoderInterface useQPEncoding:]
+ -[MOVStreamVideoEncoderInterface writeSampleBuffer:pts:metadata:withStatus:andFlags:]
+ -[MOVStreamWriter addMetadataTrack:copyData:]
+ -[MOVStreamWriter bufferCacheMode]
+ -[MOVStreamWriter canWriteData]
+ -[MOVStreamWriter finalConsume]
+ -[MOVStreamWriter finishingMode]
+ -[MOVStreamWriter getCountByPriorityForFifo:capacity:]
+ -[MOVStreamWriter logFifoUsage]
+ -[MOVStreamWriter multiplexWritingDisabled]
+ -[MOVStreamWriter setBufferCacheMode:]
+ -[MOVStreamWriter setCanWriteData:]
+ -[MOVStreamWriter setFinalConsume:]
+ -[MOVStreamWriter setFinishingMode:]
+ -[MOVStreamWriter setMediaTimeScale:forMetadataStream:error:]
+ -[MOVStreamWriter setMediaTimeScale:forStream:error:]
+ -[MOVStreamWriter setMultiplexWritingDisabled:]
+ -[MOVStreamWriter setShouldOptimizeForNetworkUse:]
+ -[MOVStreamWriter setTrackMetadataItems:forStream:error:]
+ -[MOVStreamWriter setWriteThreadCount:]
+ -[MOVStreamWriter shouldOptimizeForNetworkUse]
+ -[MOVStreamWriter startWritingThread]
+ -[MOVStreamWriter triggerWritingThread]
+ -[MOVStreamWriter writeThreadCount]
+ -[MOVStreamWriterStreamStats attemptCount]
+ -[MOVStreamWriterStreamStats fifoItemCount]
+ -[MOVStreamWriterStreamStats init]
+ -[MOVStreamWriterStreamStats setAttemptCount:]
+ -[MOVStreamWriterStreamStats setFifoItemCount:]
+ -[MOVStreamWriterStreamStats setVisitCount:]
+ -[MOVStreamWriterStreamStats setWriteCount:]
+ -[MOVStreamWriterStreamStats visitCount]
+ -[MOVStreamWriterStreamStats writeCount]
+ -[MOVStreamy416ToRawBayerPostProcessor .cxx_destruct]
+ -[MOVStreamy416ToRawBayerPostProcessor processedPixelBufferFrom:metadata:error:]
+ -[MOVStreamy416ToRawBayerPostProcessor processedPixelFormat]
+ GCC_except_table101
+ GCC_except_table102
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table115
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table206
+ GCC_except_table212
+ GCC_except_table217
+ GCC_except_table222
+ GCC_except_table40
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table91
+ GCC_except_table98
+ _AVFileTypeMPEG4
+ _CFAllocatorGetDefault
+ _CFDictionaryCreateMutableCopy
+ _CMFormatDescriptionGetExtension
+ _CVBufferPropagateAttachments
+ _CVColorPrimariesGetStringForIntegerCodePoint
+ _CVPixelFormatDescriptionCreateWithPixelFormatType
+ _CVTransferFunctionGetStringForIntegerCodePoint
+ _CVYCbCrMatrixGetStringForIntegerCodePoint
+ _OBJC_CLASS_$_MIOPixelBufferUtility
+ _OBJC_CLASS_$_MOVStreamCompandedRawBayerPostProcessor
+ _OBJC_CLASS_$_MOVStreamCompandedRawBayerPreProcessor
+ _OBJC_CLASS_$_MOVStreamDefaultPostProcessor
+ _OBJC_CLASS_$_MOVStreamDefaultPreProcessor
+ _OBJC_CLASS_$_MOVStreamL008ToNonPlanarPostProcessor
+ _OBJC_CLASS_$_MOVStreamL016Raw14PostProcessor
+ _OBJC_CLASS_$_MOVStreamL016Raw14PreProcessor
+ _OBJC_CLASS_$_MOVStreamMetalPixelBufferUtility
+ _OBJC_CLASS_$_MOVStreamNonPlanarToL008Processor
+ _OBJC_CLASS_$_MOVStreamPostProcessorFactory
+ _OBJC_CLASS_$_MOVStreamPreProcessorFactory
+ _OBJC_CLASS_$_MOVStreamRawBayerFromYUVPostProcessor
+ _OBJC_CLASS_$_MOVStreamRawBayerPostProcessor
+ _OBJC_CLASS_$_MOVStreamRawBayerPreProcessor
+ _OBJC_CLASS_$_MOVStreamRawBayerTo1stPlaneYUVPreProcessor
+ _OBJC_CLASS_$_MOVStreamRawBayerToYUVPreProcessor
+ _OBJC_CLASS_$_MOVStreamRawBayerToy416PreProcessor
+ _OBJC_CLASS_$_MOVStreamSampleBufferAndMetadata
+ _OBJC_CLASS_$_MOVStreamSampleTimeBuffer
+ _OBJC_CLASS_$_MOVStreamSampleTimeList
+ _OBJC_CLASS_$_MOVStreamSampleTimeRangeBuffer
+ _OBJC_CLASS_$_MOVStreamSampleTimeRangeList
+ _OBJC_CLASS_$_MOVStreamVideoEncoderInterface
+ _OBJC_CLASS_$_MOVStreamWriterStreamStats
+ _OBJC_CLASS_$_MOVStreamy416ToRawBayerPostProcessor
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_MOVStreamDefaultPostProcessor._converter
+ _OBJC_IVAR_$_MOVStreamDefaultPostProcessor.bufferCacheMode
+ _OBJC_IVAR_$_MOVStreamDefaultPostProcessor.exactBytesPerRow
+ _OBJC_IVAR_$_MOVStreamDefaultPostProcessor.originalPixelFormat
+ _OBJC_IVAR_$_MOVStreamDefaultPostProcessor.removePadding
+ _OBJC_IVAR_$_MOVStreamFrameTransform._bufferCacheMode
+ _OBJC_IVAR_$_MOVStreamL008ToNonPlanarPostProcessor._pool
+ _OBJC_IVAR_$_MOVStreamL016Raw14PostProcessor._l010OutputFormatRAW14L016
+ _OBJC_IVAR_$_MOVStreamL016Raw14PostProcessor._pool
+ _OBJC_IVAR_$_MOVStreamMetalPixelBufferUtility._enabled
+ _OBJC_IVAR_$_MOVStreamMetalPixelBufferUtility._metalCommandQueue
+ _OBJC_IVAR_$_MOVStreamMetalPixelBufferUtility._metalDevice
+ _OBJC_IVAR_$_MOVStreamMetalPixelBufferUtility._pipeLineStates
+ _OBJC_IVAR_$_MOVStreamRawBayerFromYUVPostProcessor._rawBayerMSBReplication
+ _OBJC_IVAR_$_MOVStreamRawBayerPostProcessor._rawBayerMSBReplication
+ _OBJC_IVAR_$_MOVStreamReader._bufferCacheMode
+ _OBJC_IVAR_$_MOVStreamReader._skipEmptyEditVideoFrame
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._firstVideoFrameRead
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._pixelFormatWasGuessed
+ _OBJC_IVAR_$_MOVStreamSampleBufferAndMetadata._metadata
+ _OBJC_IVAR_$_MOVStreamSampleBufferAndMetadata._sampleBuffer
+ _OBJC_IVAR_$_MOVStreamSampleTimeBuffer._name
+ _OBJC_IVAR_$_MOVStreamSampleTimeBuffer._times
+ _OBJC_IVAR_$_MOVStreamSampleTimeList._cached_cmtimes
+ _OBJC_IVAR_$_MOVStreamSampleTimeList._cached_times
+ _OBJC_IVAR_$_MOVStreamSampleTimeList._name
+ _OBJC_IVAR_$_MOVStreamSampleTimeList._times
+ _OBJC_IVAR_$_MOVStreamSampleTimeList._timestamps
+ _OBJC_IVAR_$_MOVStreamSampleTimeRangeBuffer._ranges
+ _OBJC_IVAR_$_MOVStreamSampleTimeRangeList._cached_ranges
+ _OBJC_IVAR_$_MOVStreamSampleTimeRangeList._name
+ _OBJC_IVAR_$_MOVStreamSampleTimeRangeList._ranges
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface._customEncoderConfig
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface._lastEncodingInfoFlags
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface._lastEncodingStatus
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface._pendingFrames
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_config
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_delegate
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_enableAVEHighPerformanceProfile
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_encoder
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_encoderInitialized
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_encodingQueue
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_expectedFrameRate
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_failedState
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_qpValue
+ _OBJC_IVAR_$_MOVStreamVideoEncoderInterface.m_stream
+ _OBJC_IVAR_$_MOVStreamWriter._avfAppendSignPostID
+ _OBJC_IVAR_$_MOVStreamWriter._bufferCacheMode
+ _OBJC_IVAR_$_MOVStreamWriter._canWriteData
+ _OBJC_IVAR_$_MOVStreamWriter._finalConsume
+ _OBJC_IVAR_$_MOVStreamWriter._finishingMode
+ _OBJC_IVAR_$_MOVStreamWriter._perfLogAVF
+ _OBJC_IVAR_$_MOVStreamWriter._writeThread
+ _OBJC_IVAR_$_MOVStreamWriter._writeThreadCount
+ _OBJC_IVAR_$_MOVStreamWriter._writingSema
+ _OBJC_IVAR_$_MOVStreamWriter.m_lastPtsForAttachmentsStream
+ _OBJC_IVAR_$_MOVStreamWriter.m_lastPtsForMetadataStream
+ _OBJC_IVAR_$_MOVStreamWriter.m_shouldOptimizeForNetworkUse
+ _OBJC_IVAR_$_MOVStreamWriterStreamStats._attemptCount
+ _OBJC_IVAR_$_MOVStreamWriterStreamStats._fifoItemCount
+ _OBJC_IVAR_$_MOVStreamWriterStreamStats._visitCount
+ _OBJC_IVAR_$_MOVStreamWriterStreamStats._writeCount
+ _OBJC_IVAR_$_MOVStreamy416ToRawBayerPostProcessor._pool
+ _OBJC_METACLASS_$_MIOPixelBufferUtility
+ _OBJC_METACLASS_$_MOVStreamCompandedRawBayerPostProcessor
+ _OBJC_METACLASS_$_MOVStreamCompandedRawBayerPreProcessor
+ _OBJC_METACLASS_$_MOVStreamDefaultPostProcessor
+ _OBJC_METACLASS_$_MOVStreamDefaultPreProcessor
+ _OBJC_METACLASS_$_MOVStreamL008ToNonPlanarPostProcessor
+ _OBJC_METACLASS_$_MOVStreamL016Raw14PostProcessor
+ _OBJC_METACLASS_$_MOVStreamL016Raw14PreProcessor
+ _OBJC_METACLASS_$_MOVStreamMetalPixelBufferUtility
+ _OBJC_METACLASS_$_MOVStreamNonPlanarToL008Processor
+ _OBJC_METACLASS_$_MOVStreamPostProcessorFactory
+ _OBJC_METACLASS_$_MOVStreamPreProcessorFactory
+ _OBJC_METACLASS_$_MOVStreamRawBayerFromYUVPostProcessor
+ _OBJC_METACLASS_$_MOVStreamRawBayerPostProcessor
+ _OBJC_METACLASS_$_MOVStreamRawBayerPreProcessor
+ _OBJC_METACLASS_$_MOVStreamRawBayerTo1stPlaneYUVPreProcessor
+ _OBJC_METACLASS_$_MOVStreamRawBayerToYUVPreProcessor
+ _OBJC_METACLASS_$_MOVStreamRawBayerToy416PreProcessor
+ _OBJC_METACLASS_$_MOVStreamSampleBufferAndMetadata
+ _OBJC_METACLASS_$_MOVStreamSampleTimeBuffer
+ _OBJC_METACLASS_$_MOVStreamSampleTimeList
+ _OBJC_METACLASS_$_MOVStreamSampleTimeRangeBuffer
+ _OBJC_METACLASS_$_MOVStreamSampleTimeRangeList
+ _OBJC_METACLASS_$_MOVStreamVideoEncoderInterface
+ _OBJC_METACLASS_$_MOVStreamWriterStreamStats
+ _OBJC_METACLASS_$_MOVStreamy416ToRawBayerPostProcessor
+ __OBJC_$_CLASS_METHODS_MIOPixelBufferUtility
+ __OBJC_$_CLASS_METHODS_MOVStreamMetalPixelBufferUtility
+ __OBJC_$_CLASS_METHODS_MOVStreamPostProcessorFactory
+ __OBJC_$_CLASS_METHODS_MOVStreamPreProcessorFactory
+ __OBJC_$_CLASS_METHODS_MOVStreamVideoEncoderInterface
+ __OBJC_$_INSTANCE_METHODS_MOVStreamCompandedRawBayerPostProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamCompandedRawBayerPreProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamDefaultPostProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamDefaultPreProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamL008ToNonPlanarPostProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamL016Raw14PostProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamL016Raw14PreProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamMetalPixelBufferUtility
+ __OBJC_$_INSTANCE_METHODS_MOVStreamNonPlanarToL008Processor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamPostProcessorFactory
+ __OBJC_$_INSTANCE_METHODS_MOVStreamPreProcessorFactory
+ __OBJC_$_INSTANCE_METHODS_MOVStreamRawBayerFromYUVPostProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamRawBayerPostProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamRawBayerPreProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamRawBayerTo1stPlaneYUVPreProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamRawBayerToYUVPreProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamRawBayerToy416PreProcessor
+ __OBJC_$_INSTANCE_METHODS_MOVStreamSampleBufferAndMetadata
+ __OBJC_$_INSTANCE_METHODS_MOVStreamSampleTimeBuffer
+ __OBJC_$_INSTANCE_METHODS_MOVStreamSampleTimeList
+ __OBJC_$_INSTANCE_METHODS_MOVStreamSampleTimeRangeBuffer
+ __OBJC_$_INSTANCE_METHODS_MOVStreamSampleTimeRangeList
+ __OBJC_$_INSTANCE_METHODS_MOVStreamVideoEncoderInterface
+ __OBJC_$_INSTANCE_METHODS_MOVStreamWriterStreamStats
+ __OBJC_$_INSTANCE_METHODS_MOVStreamy416ToRawBayerPostProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamDefaultPostProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamL008ToNonPlanarPostProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamL016Raw14PostProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamMetalPixelBufferUtility
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamRawBayerFromYUVPostProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamRawBayerPostProcessor
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamSampleBufferAndMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamSampleTimeBuffer
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamSampleTimeList
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamSampleTimeRangeBuffer
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamSampleTimeRangeList
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamVideoEncoderInterface
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamWriterStreamStats
+ __OBJC_$_INSTANCE_VARIABLES_MOVStreamy416ToRawBayerPostProcessor
+ __OBJC_$_PROP_LIST_MOVStreamDefaultPostProcessor
+ __OBJC_$_PROP_LIST_MOVStreamDefaultPreProcessor
+ __OBJC_$_PROP_LIST_MOVStreamL016Raw14PostProcessor
+ __OBJC_$_PROP_LIST_MOVStreamMetalPixelBufferUtility
+ __OBJC_$_PROP_LIST_MOVStreamRawBayerFromYUVPostProcessor
+ __OBJC_$_PROP_LIST_MOVStreamRawBayerPostProcessor
+ __OBJC_$_PROP_LIST_MOVStreamSampleBufferAndMetadata
+ __OBJC_$_PROP_LIST_MOVStreamSampleTimeBuffer
+ __OBJC_$_PROP_LIST_MOVStreamSampleTimeList
+ __OBJC_$_PROP_LIST_MOVStreamSampleTimeRangeList
+ __OBJC_$_PROP_LIST_MOVStreamVideoEncoderInterface
+ __OBJC_$_PROP_LIST_MOVStreamWriterStreamStats
+ __OBJC_CLASS_PROTOCOLS_$_MOVStreamDefaultPostProcessor
+ __OBJC_CLASS_PROTOCOLS_$_MOVStreamDefaultPreProcessor
+ __OBJC_CLASS_PROTOCOLS_$_MOVStreamL008ToNonPlanarPostProcessor
+ __OBJC_CLASS_PROTOCOLS_$_MOVStreamSampleTimeRangeList
+ __OBJC_CLASS_PROTOCOLS_$_MOVStreamVideoEncoderInterface
+ __OBJC_CLASS_RO_$_MIOPixelBufferUtility
+ __OBJC_CLASS_RO_$_MOVStreamCompandedRawBayerPostProcessor
+ __OBJC_CLASS_RO_$_MOVStreamCompandedRawBayerPreProcessor
+ __OBJC_CLASS_RO_$_MOVStreamDefaultPostProcessor
+ __OBJC_CLASS_RO_$_MOVStreamDefaultPreProcessor
+ __OBJC_CLASS_RO_$_MOVStreamL008ToNonPlanarPostProcessor
+ __OBJC_CLASS_RO_$_MOVStreamL016Raw14PostProcessor
+ __OBJC_CLASS_RO_$_MOVStreamL016Raw14PreProcessor
+ __OBJC_CLASS_RO_$_MOVStreamMetalPixelBufferUtility
+ __OBJC_CLASS_RO_$_MOVStreamNonPlanarToL008Processor
+ __OBJC_CLASS_RO_$_MOVStreamPostProcessorFactory
+ __OBJC_CLASS_RO_$_MOVStreamPreProcessorFactory
+ __OBJC_CLASS_RO_$_MOVStreamRawBayerFromYUVPostProcessor
+ __OBJC_CLASS_RO_$_MOVStreamRawBayerPostProcessor
+ __OBJC_CLASS_RO_$_MOVStreamRawBayerPreProcessor
+ __OBJC_CLASS_RO_$_MOVStreamRawBayerTo1stPlaneYUVPreProcessor
+ __OBJC_CLASS_RO_$_MOVStreamRawBayerToYUVPreProcessor
+ __OBJC_CLASS_RO_$_MOVStreamRawBayerToy416PreProcessor
+ __OBJC_CLASS_RO_$_MOVStreamSampleBufferAndMetadata
+ __OBJC_CLASS_RO_$_MOVStreamSampleTimeBuffer
+ __OBJC_CLASS_RO_$_MOVStreamSampleTimeList
+ __OBJC_CLASS_RO_$_MOVStreamSampleTimeRangeBuffer
+ __OBJC_CLASS_RO_$_MOVStreamSampleTimeRangeList
+ __OBJC_CLASS_RO_$_MOVStreamVideoEncoderInterface
+ __OBJC_CLASS_RO_$_MOVStreamWriterStreamStats
+ __OBJC_CLASS_RO_$_MOVStreamy416ToRawBayerPostProcessor
+ __OBJC_METACLASS_RO_$_MIOPixelBufferUtility
+ __OBJC_METACLASS_RO_$_MOVStreamCompandedRawBayerPostProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamCompandedRawBayerPreProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamDefaultPostProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamDefaultPreProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamL008ToNonPlanarPostProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamL016Raw14PostProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamL016Raw14PreProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamMetalPixelBufferUtility
+ __OBJC_METACLASS_RO_$_MOVStreamNonPlanarToL008Processor
+ __OBJC_METACLASS_RO_$_MOVStreamPostProcessorFactory
+ __OBJC_METACLASS_RO_$_MOVStreamPreProcessorFactory
+ __OBJC_METACLASS_RO_$_MOVStreamRawBayerFromYUVPostProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamRawBayerPostProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamRawBayerPreProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamRawBayerTo1stPlaneYUVPreProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamRawBayerToYUVPreProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamRawBayerToy416PreProcessor
+ __OBJC_METACLASS_RO_$_MOVStreamSampleBufferAndMetadata
+ __OBJC_METACLASS_RO_$_MOVStreamSampleTimeBuffer
+ __OBJC_METACLASS_RO_$_MOVStreamSampleTimeList
+ __OBJC_METACLASS_RO_$_MOVStreamSampleTimeRangeBuffer
+ __OBJC_METACLASS_RO_$_MOVStreamSampleTimeRangeList
+ __OBJC_METACLASS_RO_$_MOVStreamVideoEncoderInterface
+ __OBJC_METACLASS_RO_$_MOVStreamWriterStreamStats
+ __OBJC_METACLASS_RO_$_MOVStreamy416ToRawBayerPostProcessor
+ __ZGVZ76+[MOVStreamIOUtility(Private) detectPixelFormatForAsset:videoTrackId:error:]E18formatMappingTable
+ __ZN28MOVStreamHEVCLosslessEncoder11EncodeFrameEP10__CVBuffer6CMTimePK14__CFDictionaryPv
+ __ZN28MOVStreamHEVCLosslessEncoder15isSessionClosedEv
+ __ZN28MOVStreamHEVCLosslessEncoder16useQPCompressionEi
+ __ZN28MOVStreamHEVCLosslessEncoder17invalidateSessionEv
+ __ZN28MOVStreamHEVCLosslessEncoder22frameReorderingEnabledEv
+ __ZN28MOVStreamHEVCLosslessEncoder25propogateColorAttachmentsEPK25opaqueCMFormatDescriptionP26OpaqueVTCompressionSession
+ __ZN28MOVStreamHEVCLosslessEncoder4OpenEii10IMG_FORMATdPK25opaqueCMFormatDescriptionPFvPvS4_ijP20opaqueCMSampleBufferES4_
+ __ZN28MOVStreamHEVCLosslessEncoder5CloseEv
+ __ZN28MOVStreamHEVCLosslessEncoderC1Ev
+ __ZN28MOVStreamHEVCLosslessEncoderC2Ev
+ __ZN28MOVStreamHEVCLosslessEncoderD1Ev
+ __ZN28MOVStreamHEVCLosslessEncoderD2Ev
+ __ZZ46+[MOVStreamPreProcessorFactory defaultFactory]E7factory
+ __ZZ46+[MOVStreamPreProcessorFactory defaultFactory]E9onceToken
+ __ZZ47+[MOVStreamPostProcessorFactory defaultFactory]E7factory
+ __ZZ47+[MOVStreamPostProcessorFactory defaultFactory]E9onceToken
+ __ZZ50+[MIOPixelBufferUtility sharedBytesPerPixelLookUp]E6lookup
+ __ZZ50+[MIOPixelBufferUtility sharedBytesPerPixelLookUp]E9onceToken
+ __ZZ59+[MOVStreamIOUtility(Private) reservedMIOTrackMetadataKeys]E12reservedList
+ __ZZ59+[MOVStreamIOUtility(Private) reservedMIOTrackMetadataKeys]E9onceToken
+ __ZZ76+[MOVStreamIOUtility(Private) detectPixelFormatForAsset:videoTrackId:error:]E18formatMappingTable
+ ___37-[MOVStreamWriter startWritingThread]_block_invoke
+ ___41-[MOVStreamWriter processFinishRecording]_block_invoke.424
+ ___41-[MOVStreamWriter processFinishRecording]_block_invoke.425
+ ___46+[MOVStreamPreProcessorFactory defaultFactory]_block_invoke
+ ___47+[MOVStreamPostProcessorFactory defaultFactory]_block_invoke
+ ___50+[MIOPixelBufferUtility sharedBytesPerPixelLookUp]_block_invoke
+ ___59+[MOVStreamIOUtility(Private) reservedMIOTrackMetadataKeys]_block_invoke
+ ___62-[MOVStreamVideoEncoderInterface closeEncoderInDispatchGroup:]_block_invoke
+ ___65+[MOVStreamMetalPixelBufferUtility sharedMetalPixelBufferUtility]_block_invoke
+ ___75-[MOVStreamVideoEncoderInterface encodeFrame:pts:frameProperties:metadata:]_block_invoke
+ ___block_descriptor_88_ea8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.4
+ ___block_literal_global.446
+ __os_signpost_emit_with_name_impl
+ __unnamed_array_storage.245
+ _clock_gettime_nsec_np
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms
+ _kCVImageBufferChromaLocationBottomFieldKey
+ _kCVImageBufferChromaLocationTopFieldKey
+ _kCVImageBufferChromaLocation_TopLeft
+ _kCVImageBufferChromaSubsamplingKey
+ _kCVImageBufferColorPrimaries_ITU_R_2020
+ _kCVImageBufferFieldCountKey
+ _kCVPixelFormatComponentRange
+ _kCVPixelFormatComponentRange_VideoRange
+ _kCVPixelFormatContainsGrayscale
+ _kCVPixelFormatContainsRGB
+ _kCVPixelFormatContainsSenselArray
+ _kCVPixelFormatContainsYCbCr
+ _kCVPixelFormatHorizontalSubsampling
+ _kCVPixelFormatPlanes
+ _kCVPixelFormatVerticalSubsampling
+ _kMIOAdditionalCompressionProperties
+ _kMIOBufferCacheMode
+ _kMIODefaultBufferCacheMode
+ _kMIODefaultsDomainName
+ _kMOVStreamWriterErrorDomain
+ _objc_msgSend$addAdditionalHEVCCompressionProperties:recordingConfig:
+ _objc_msgSend$attachmentsContainTopLeftChromaLocations:
+ _objc_msgSend$attachmentsContainsRec2020orRec2100ColorMatrices:
+ _objc_msgSend$attachmentsContainsRec2020orRec2100ColorPrimaries:
+ _objc_msgSend$attachmentsRepresentInterlacedFields:
+ _objc_msgSend$attemptCount
+ _objc_msgSend$bufferCacheMode
+ _objc_msgSend$bufferHasPadding:
+ _objc_msgSend$bytesPerWidthOfBuffer:
+ _objc_msgSend$canWriteData
+ _objc_msgSend$chromaSubsamplingForDictionary:
+ _objc_msgSend$createMIOPixelBufferPoolWithWidth:height:pixelFormat:exactBytesPerRow:minBufferCount:bufferCacheMode:
+ _objc_msgSend$createMIOPixelBufferPoolWithWidth:height:pixelFormat:exactBytesPerRows:minBufferCount:bufferCacheMode:
+ _objc_msgSend$createMIOPixelBufferPoolWithWidth:height:pixelFormat:extendedPixelsPerRow:minBufferCount:bufferCacheMode:
+ _objc_msgSend$createNewL008MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:bufferCacheMode:
+ _objc_msgSend$createNewL010MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:bufferCacheMode:
+ _objc_msgSend$createPixelBufferAttributesWithWidth:height:extendedPixelsPerRow:pixelFormat:bytesPerRowAlignment:planeAlignment:bufferCacheMode:
+ _objc_msgSend$customTrackMetadataItems
+ _objc_msgSend$dictionary:booleanValueForKey:
+ _objc_msgSend$dictionary:numberValueForKey:
+ _objc_msgSend$dictionary:stringValueForKey:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$encodeFrame:pts:frameProperties:metadata:
+ _objc_msgSend$fifoItemCount
+ _objc_msgSend$finalConsume
+ _objc_msgSend$firstVideoFrameRead
+ _objc_msgSend$formatDescriptionRepresentsBayer:
+ _objc_msgSend$formatDescriptionRepresentsVideoRange:
+ _objc_msgSend$formatDescriptionRepresentsYCbCr:
+ _objc_msgSend$getCountByPriorityForFifo:capacity:
+ _objc_msgSend$getOutputPixelFormatWasGuessedForStream
+ _objc_msgSend$initWithBlock:
+ _objc_msgSend$initWithOriginalPixelFormat:bufferCacheMode:
+ _objc_msgSend$initWithOriginalPixelFormat:bufferCacheMode:l010OutputFormatRAW14L016:
+ _objc_msgSend$initWithOriginalPixelFormat:bufferCacheMode:rawBayerMSBReplication:
+ _objc_msgSend$initWithRotation:flip:bufferCacheMode:
+ _objc_msgSend$initWithTargetWidth:height:format:bytesPerRow:bufferCacheMode:
+ _objc_msgSend$initWithTargetWidth:height:format:bytesPerRows:bufferCacheMode:
+ _objc_msgSend$initWithTargetWidth:height:format:extendedPixelsPerRow:bufferCacheMode:
+ _objc_msgSend$initWithVideoTrack:assetReader:associatedMetadataTracks:version:bufferCacheMode:unknownStreamId:reader:delegate:error:
+ _objc_msgSend$isEmptySample:
+ _objc_msgSend$key:hasUnspecifiedValue:
+ _objc_msgSend$logFifoUsage
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$makeBufferConfigDict:height:pixelFormat:bufferCacheMode:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$pendingFrames
+ _objc_msgSend$pixelFormatForUnknownTrackOfReader:streamId:
+ _objc_msgSend$pixelFormatIs420Sampled:
+ _objc_msgSend$pixelFormatIs422Sampled:
+ _objc_msgSend$postProcessorFromReader:originalPixelFormat:encodedFormat:encoderType:streamId:bufferCacheMode:
+ _objc_msgSend$processFrame:pts:frameProperties:metadata:
+ _objc_msgSend$proresRAWHQSettings:frameRate:
+ _objc_msgSend$proresRAWSettings:frameRate:
+ _objc_msgSend$reason
+ _objc_msgSend$reservedMIOTrackMetadataKeys
+ _objc_msgSend$setAttemptCount:
+ _objc_msgSend$setBufferCacheMode:
+ _objc_msgSend$setCanWriteData:
+ _objc_msgSend$setFifoItemCount:
+ _objc_msgSend$setFinalConsume:
+ _objc_msgSend$setFirstVideoFrameRead:
+ _objc_msgSend$setName:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPendingFrames:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setSessionProperties:
+ _objc_msgSend$setSettings:
+ _objc_msgSend$setShouldOptimizeForNetworkUse:
+ _objc_msgSend$setSkipEmptyEditVideoFrame:
+ _objc_msgSend$setThreadPriority:
+ _objc_msgSend$setVisitCount:
+ _objc_msgSend$setWriteCount:
+ _objc_msgSend$setWriteThreadCount:
+ _objc_msgSend$skipEmptyEditVideoFrame
+ _objc_msgSend$start
+ _objc_msgSend$startWritingThread
+ _objc_msgSend$stringByRemovingPercentEncoding
+ _objc_msgSend$stripBufferPadding:
+ _objc_msgSend$triggerWritingThread
+ _objc_msgSend$visitCount
+ _objc_msgSend$writeCount
+ _objc_msgSend$writeThreadCount
+ _objc_msgSend$writerErrorWithMessage:code:
+ _objc_retain_x26
+ _os_signpost_enabled
+ _os_signpost_id_generate
- +[MIOPixelBufferPool createNewL008MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:]
- +[MIOPixelBufferPool createNewL010MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:]
- +[MetalPixelBufferUtility sharedMetalPixelBufferUtility]
- +[PixelBufferUtility concatPixelBuffer:withPixelBuffer:targetPixelBuffer:]
- +[PixelBufferUtility copyAlphaChannelOfBuffer:toMonochromeBuffer:]
- +[PixelBufferUtility copyAlphaChannelOfBuffer:touint16Data:]
- +[PixelBufferUtility copyData:toNonPlanarPixelBuffer:]
- +[PixelBufferUtility copyData:toPlanarPixelBuffer:toPlane:]
- +[PixelBufferUtility copyFromPixelBuffer:toPixelBuffer:andShiftBits:]
- +[PixelBufferUtility copyMonochromeBuffer:toAlphaChannelOfBuffer:]
- +[PixelBufferUtility copyNonPlanarPixelBufferData:]
- +[PixelBufferUtility copyPixelBuffer:toPixelBuffer:bytesPerPixel:]
- +[PixelBufferUtility copyPixelBufferData:ofPlane:]
- +[PixelBufferUtility copyuint16Data:toAlphaChannelOfBuffer:]
- +[PixelBufferUtility create4444AYpCbCr16PixelBufferFillAlphaWithData:width:height:]
- +[PixelBufferUtility createNewL008PixelBufferPoolWithReferencePixelBuffer:minimumBufferCount:]
- +[PixelBufferUtility createNewL010PixelBufferPoolWithReferencePixelBuffer:minimumBufferCount:]
- +[PixelBufferUtility createPixelBufferAttributesWithWidth:height:extendedPixelsPerRow:pixelFormat:bytesPerRowAlignment:planeAlignment:]
- +[PixelBufferUtility createPixelBufferAttributesWithWidth:height:pixelFormat:bytesPerRow:]
- +[PixelBufferUtility createPixelBufferAttributesWithWidth:height:pixelFormat:bytesPerRows:]
- +[PixelBufferUtility createPixelBufferPoolWithWidth:height:format:bytesPerRow:minBufferCount:]
- +[PixelBufferUtility createPixelBufferPoolWithWidth:height:format:bytesPerRows:minBufferCount:]
- +[PixelBufferUtility createPixelBufferPoolWithWidth:height:format:extendedPixelsPerRow:minBufferCount:]
- +[PixelBufferUtility createRawPixelBufferWithWidth:height:extendedRows:extendedPixelsPerRow:pixelFormat:bytesPerRowAlignment:planeAlignment:bufferCacheMode:]
- +[PixelBufferUtility createRawPixelBufferWithWidth:height:pixelFormat:bytesPerRow:]
- +[PixelBufferUtility extendedPixelsPerRowOfPixelBuffer:]
- +[PixelBufferUtility extendedPixelsRightForPlanarBufferWidth:height:bytesPerRow:format:]
- +[PixelBufferUtility fillPlaneOfPixelBuffer:planeIndex:withValue:]
- +[PixelBufferUtility histogramOf8BitBuffer:]
- +[PixelBufferUtility isPixelBufferCompandedRawBayer:]
- +[PixelBufferUtility isPixelBufferRawBayer:]
- +[PixelBufferUtility isPixelFormatCompandedRawBayer:]
- +[PixelBufferUtility isPixelFormatRawBayer:]
- +[PixelBufferUtility joinCompandedWarholBuffer:intoCompandedBayerBuffer:]
- +[PixelBufferUtility joinWarholBuffer:intoBayerBuffer:shiftBitsRightBy:msbReplication:]
- +[PixelBufferUtility joinYUVBuffer:intoRawBayerPixelBuffer:shiftBitsLeftBy:msbReplication:]
- +[PixelBufferUtility newPixelBufferRefCopy:]
- +[PixelBufferUtility newPixelBufferRefCopy:attachmentKeysToCopy:]
- +[PixelBufferUtility newRawBayerBufferFromYUVPixelBuffer:withPixelBufferPool:msbReplication:]
- +[PixelBufferUtility newWarholBufferFromCompandedRawBayerPixelBuffer:withPixelBufferPool:]
- +[PixelBufferUtility newWarholBufferFromRawBayerPixelBuffer:]
- +[PixelBufferUtility newWarholBufferFromRawBayerPixelBuffer:withPixelBufferPool:]
- +[PixelBufferUtility newYUVBufferFromRawBayerPixelBuffer:withPixelBufferPool:]
- +[PixelBufferUtility numberOfPlanesForPixelFormatType:]
- +[PixelBufferUtility pixelBufferFromPool:]
- +[PixelBufferUtility pixelBufferSizeWithPadding:]
- +[PixelBufferUtility rangesOf8BitBuffer:]
- +[PixelBufferUtility readFrameFromFile:width:height:pixelFormat:]
- +[PixelBufferUtility sharedBytesPerPixelLookUp]
- +[PixelBufferUtility splitBayerBuffer:intoWarholPixelBuffer:shiftBitsLeftBy:]
- +[PixelBufferUtility splitBayerBuffer:intoYUVPixelBuffer:shiftBitsLeftBy:]
- +[PixelBufferUtility splitCompandedBayerBuffer:intoCompandedWarholPixelBuffer:]
- +[PixelBufferUtility verticallySplitPixelBuffer:intoTopPixelBuffer:bottomPixelBuffer:]
- +[PixelBufferUtility writeBuffer:ofSize:toFile:]
- +[PixelBufferUtility writeBuffer:toFile:]
- +[PostProcessorFactory defaultFactory]
- +[PreProcessorFactory defaultFactory]
- +[VideoEncoderInterface createHEVCCompatiblePixelBuffer:]
- -[CompandedRawBayerPostProcessor processedPixelBufferFrom:metadata:error:]
- -[CompandedRawBayerPostProcessor processedPixelFormat]
- -[CompandedRawBayerPreProcessor createTrackFormatDescriptionFromStreamData:]
- -[CompandedRawBayerPreProcessor encodedPixelFormatFromStreamData:]
- -[CompandedRawBayerPreProcessor formatDescriptionForPixelBuffer:streamData:]
- -[CompandedRawBayerPreProcessor inputPixelFormatFromStreamData:]
- -[CompandedRawBayerPreProcessor processedPixelBufferCopyOf:streamData:error:]
- -[DefaultPostProcessor .cxx_destruct]
- -[DefaultPostProcessor dealloc]
- -[DefaultPostProcessor exactBytesPerRow]
- -[DefaultPostProcessor initWithOriginalPixelFormat:]
- -[DefaultPostProcessor minimumBytesPerRowForPixelBuffer:]
- -[DefaultPostProcessor originalPixelFormat]
- -[DefaultPostProcessor pixelBufferWithExactBytesPerRow:fromPixelBuffer:error:]
- -[DefaultPostProcessor pixelBufferWithoutPaddingFromPixelBuffer:error:]
- -[DefaultPostProcessor processedPixelBufferFrom:metadata:error:]
- -[DefaultPostProcessor processedPixelFormat]
- -[DefaultPostProcessor removePadding]
- -[DefaultPostProcessor setExactBytesPerRow:]
- -[DefaultPostProcessor setOriginalPixelFormat:]
- -[DefaultPostProcessor setRemovePadding:]
- -[DefaultPostProcessor shouldChangeBytesPerRowOfPixelBuffer:]
- -[DefaultPostProcessor shouldRemovePaddingOfPixelBuffer:metadata:]
- -[DefaultPreProcessor createTrackFormatDescriptionFromStreamData:]
- -[DefaultPreProcessor encodedPixelFormatFromStreamData:]
- -[DefaultPreProcessor formatDescriptionForPixelBuffer:streamData:]
- -[DefaultPreProcessor inputPixelFormatFromStreamData:]
- -[DefaultPreProcessor processedPixelBufferCopyOf:streamData:error:]
- -[L008ToNonPlanarPostProcessor .cxx_destruct]
- -[L008ToNonPlanarPostProcessor adjustedWidthForWidth:]
- -[L008ToNonPlanarPostProcessor processedPixelBufferFrom:metadata:error:]
- -[L008ToNonPlanarPostProcessor processedPixelFormat]
- -[L016Raw14PostProcessor initWithOriginalPixelFormat:l010OutputFormatRAW14L016:]
- -[L016Raw14PostProcessor l010OutputFormatRAW14L016]
- -[L016Raw14PostProcessor processedPixelBufferFrom:metadata:error:]
- -[L016Raw14PostProcessor processedPixelFormat]
- -[L016Raw14PostProcessor setL010OutputFormatRAW14L016:]
- -[L016Raw14PreProcessor createTrackFormatDescriptionFromStreamData:]
- -[L016Raw14PreProcessor encodedPixelFormatFromStreamData:]
- -[L016Raw14PreProcessor formatDescriptionForPixelBuffer:streamData:]
- -[L016Raw14PreProcessor inputPixelFormatFromStreamData:]
- -[L016Raw14PreProcessor processedPixelBufferCopyOf:streamData:error:]
- -[MOVStreamFrameTransform initWithRotation:flip:].cold.1
- -[MOVStreamReaderStreamOutput initWithVideoTrack:assetReader:associatedMetadataTracks:version:unknownStreamId:reader:delegate:error:]
- -[MetalPixelBufferUtility .cxx_destruct]
- -[MetalPixelBufferUtility enabled]
- -[MetalPixelBufferUtility init]
- -[MetalPixelBufferUtility joinCompandedWarholBuffer:intoCompandedBayerBuffer:]
- -[MetalPixelBufferUtility joinWarholBuffer:intoBayerBuffer:shiftBitsRightBy:msbReplication:]
- -[MetalPixelBufferUtility joinYUVBuffer:intoRawBayerPixelBuffer:shiftBitsLeftBy:msbReplication:]
- -[MetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:]
- -[MetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:].cold.1
- -[MetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:].cold.2
- -[MetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:].cold.3
- -[MetalPixelBufferUtility setEnabled:]
- -[MetalPixelBufferUtility splitBayerBuffer:intoWarholPixelBuffer:shiftBitsLeftBy:]
- -[MetalPixelBufferUtility splitBayerBuffer:intoYUVPixelBuffer:shiftBitsLeftBy:]
- -[MetalPixelBufferUtility splitCompandedBayerBuffer:intoCompandedWarholPixelBuffer:]
- -[NonPlanarToL008Processor createTrackFormatDescriptionFromStreamData:]
- -[NonPlanarToL008Processor encodedPixelFormatFromStreamData:]
- -[NonPlanarToL008Processor formatDescriptionForPixelBuffer:streamData:]
- -[NonPlanarToL008Processor inputPixelFormatFromStreamData:]
- -[NonPlanarToL008Processor processedPixelBufferCopyOf:streamData:error:]
- -[PostProcessorFactory postProcessorFromReader:originalPixelFormat:encodedFormat:encoderType:streamId:]
- -[PreProcessorFactory preProcessorForFormat:recordingConfiguration:]
- -[RawBayerFromYUVPostProcessor initWithOriginalPixelFormat:rawBayerMSBReplication:]
- -[RawBayerFromYUVPostProcessor processedPixelBufferFrom:metadata:error:]
- -[RawBayerFromYUVPostProcessor processedPixelFormat]
- -[RawBayerFromYUVPostProcessor rawBayerMSBReplication]
- -[RawBayerFromYUVPostProcessor setRawBayerMSBReplication:]
- -[RawBayerPostProcessor initWithOriginalPixelFormat:rawBayerMSBReplication:]
- -[RawBayerPostProcessor processedPixelBufferFrom:metadata:error:]
- -[RawBayerPostProcessor processedPixelFormat]
- -[RawBayerPostProcessor rawBayerMSBReplication]
- -[RawBayerPostProcessor setRawBayerMSBReplication:]
- -[RawBayerPreProcessor createTrackFormatDescriptionFromStreamData:]
- -[RawBayerPreProcessor encodedPixelFormatFromStreamData:]
- -[RawBayerPreProcessor formatDescriptionForPixelBuffer:streamData:]
- -[RawBayerPreProcessor inputPixelFormatFromStreamData:]
- -[RawBayerPreProcessor processedPixelBufferCopyOf:streamData:error:]
- -[RawBayerTo1stPlaneYUVPreProcessor createTrackFormatDescriptionFromStreamData:]
- -[RawBayerTo1stPlaneYUVPreProcessor encodedPixelFormatFromStreamData:]
- -[RawBayerTo1stPlaneYUVPreProcessor formatDescriptionForPixelBuffer:streamData:]
- -[RawBayerTo1stPlaneYUVPreProcessor inputPixelFormatFromStreamData:]
- -[RawBayerTo1stPlaneYUVPreProcessor processedPixelBufferCopyOf:streamData:error:]
- -[RawBayerToYUVPreProcessor createTrackFormatDescriptionFromStreamData:]
- -[RawBayerToYUVPreProcessor encodedPixelFormatFromStreamData:]
- -[RawBayerToYUVPreProcessor formatDescriptionForPixelBuffer:streamData:]
- -[RawBayerToYUVPreProcessor inputPixelFormatFromStreamData:]
- -[RawBayerToYUVPreProcessor processedPixelBufferCopyOf:streamData:error:]
- -[RawBayerToy416PreProcessor createTrackFormatDescriptionFromStreamData:]
- -[RawBayerToy416PreProcessor encodedPixelFormatFromStreamData:]
- -[RawBayerToy416PreProcessor formatDescriptionForPixelBuffer:streamData:]
- -[RawBayerToy416PreProcessor inputPixelFormatFromStreamData:]
- -[RawBayerToy416PreProcessor processedPixelBufferCopyOf:streamData:error:]
- -[SampleBufferAndMetadata .cxx_destruct]
- -[SampleBufferAndMetadata metadata]
- -[SampleBufferAndMetadata sampleBuffer]
- -[SampleBufferAndMetadata setMetadata:]
- -[SampleBufferAndMetadata setSampleBuffer:]
- -[SampleTimeBuffer .cxx_construct]
- -[SampleTimeBuffer .cxx_destruct]
- -[SampleTimeBuffer appendTime:]
- -[SampleTimeBuffer description]
- -[SampleTimeBuffer initWithCapacity:]
- -[SampleTimeBuffer init]
- -[SampleTimeBuffer isEmpty]
- -[SampleTimeBuffer name]
- -[SampleTimeBuffer setName:]
- -[SampleTimeBuffer timeline]
- -[SampleTimeList .cxx_construct]
- -[SampleTimeList .cxx_destruct]
- -[SampleTimeList cached_cmtimes]
- -[SampleTimeList cached_times]
- -[SampleTimeList cmtimes]
- -[SampleTimeList count]
- -[SampleTimeList description]
- -[SampleTimeList frameRangeFrom:to:]
- -[SampleTimeList initWithTimes:]
- -[SampleTimeList initWithTimestamps:]
- -[SampleTimeList init]
- -[SampleTimeList name]
- -[SampleTimeList setName:]
- -[SampleTimeList setTimestamps:]
- -[SampleTimeList timeAtIndex:]
- -[SampleTimeList timeRangeFrom:to:]
- -[SampleTimeList times]
- -[SampleTimeList timestamps]
- -[SampleTimeRangeBuffer .cxx_construct]
- -[SampleTimeRangeBuffer .cxx_destruct]
- -[SampleTimeRangeBuffer appendTimeRange:]
- -[SampleTimeRangeBuffer initWithCapacity:]
- -[SampleTimeRangeBuffer init]
- -[SampleTimeRangeBuffer timeRangeList]
- -[SampleTimeRangeList .cxx_construct]
- -[SampleTimeRangeList .cxx_destruct]
- -[SampleTimeRangeList cached_ranges]
- -[SampleTimeRangeList containsTimeRange:]
- -[SampleTimeRangeList copyWithZone:]
- -[SampleTimeRangeList indexOfTimeRangeAtTime:]
- -[SampleTimeRangeList initWithTimeRange:]
- -[SampleTimeRangeList initWithTimeRanges:]
- -[SampleTimeRangeList init]
- -[SampleTimeRangeList name]
- -[SampleTimeRangeList setName:]
- -[SampleTimeRangeList timeRangeAtIndex:]
- -[SampleTimeRangeList timeRange]
- -[VideoEncoderInterface .cxx_destruct]
- -[VideoEncoderInterface closeEncoderInDispatchGroup:]
- -[VideoEncoderInterface closeEncoder]
- -[VideoEncoderInterface codecTypeOverride]
- -[VideoEncoderInterface configureSessionOverride:]
- -[VideoEncoderInterface customEncoderConfig]
- -[VideoEncoderInterface dealloc]
- -[VideoEncoderInterface encodeFrame:pst:frameProperties:metadata:]
- -[VideoEncoderInterface frameReorderingEnabled]
- -[VideoEncoderInterface initForStream:configuration:delegate:]
- -[VideoEncoderInterface initWithExpectedFrameRate:forStream:delegate:enableAVEHighPerformanceProfile:]
- -[VideoEncoderInterface init]
- -[VideoEncoderInterface lastEncodingInfoFlags]
- -[VideoEncoderInterface lastEncodingStatus]
- -[VideoEncoderInterface overrideVideoEncoderSpecification]
- -[VideoEncoderInterface pendigFrames]
- -[VideoEncoderInterface processFrame:pst:frameProperties:metadata:]
- -[VideoEncoderInterface setCustomEncoderConfig:]
- -[VideoEncoderInterface setPendigFrames:]
- -[VideoEncoderInterface setupEncoderWithWidth:andHeight:imageFormat:formatDescription:andFramerate:]
- -[VideoEncoderInterface skipFrameWithStatus:andFlags:]
- -[VideoEncoderInterface useQPEncoding:]
- -[VideoEncoderInterface writeSampleBuffer:pts:metadata:withStatus:andFlags:]
- -[y416ToRawBayerPostProcessor .cxx_destruct]
- -[y416ToRawBayerPostProcessor processedPixelBufferFrom:metadata:error:]
- -[y416ToRawBayerPostProcessor processedPixelFormat]
- GCC_except_table100
- GCC_except_table108
- GCC_except_table109
- GCC_except_table113
- GCC_except_table117
- GCC_except_table121
- GCC_except_table122
- GCC_except_table123
- GCC_except_table126
- GCC_except_table131
- GCC_except_table132
- GCC_except_table185
- GCC_except_table193
- GCC_except_table196
- GCC_except_table201
- GCC_except_table44
- GCC_except_table45
- GCC_except_table50
- GCC_except_table62
- GCC_except_table70
- GCC_except_table77
- GCC_except_table78
- GCC_except_table81
- GCC_except_table82
- GCC_except_table83
- _OBJC_CLASS_$_CompandedRawBayerPostProcessor
- _OBJC_CLASS_$_CompandedRawBayerPreProcessor
- _OBJC_CLASS_$_DefaultPostProcessor
- _OBJC_CLASS_$_DefaultPreProcessor
- _OBJC_CLASS_$_L008ToNonPlanarPostProcessor
- _OBJC_CLASS_$_L016Raw14PostProcessor
- _OBJC_CLASS_$_L016Raw14PreProcessor
- _OBJC_CLASS_$_MetalPixelBufferUtility
- _OBJC_CLASS_$_NonPlanarToL008Processor
- _OBJC_CLASS_$_PostProcessorFactory
- _OBJC_CLASS_$_PreProcessorFactory
- _OBJC_CLASS_$_RawBayerFromYUVPostProcessor
- _OBJC_CLASS_$_RawBayerPostProcessor
- _OBJC_CLASS_$_RawBayerPreProcessor
- _OBJC_CLASS_$_RawBayerTo1stPlaneYUVPreProcessor
- _OBJC_CLASS_$_RawBayerToYUVPreProcessor
- _OBJC_CLASS_$_RawBayerToy416PreProcessor
- _OBJC_CLASS_$_SampleBufferAndMetadata
- _OBJC_CLASS_$_SampleTimeBuffer
- _OBJC_CLASS_$_SampleTimeList
- _OBJC_CLASS_$_SampleTimeRangeBuffer
- _OBJC_CLASS_$_SampleTimeRangeList
- _OBJC_CLASS_$_VideoEncoderInterface
- _OBJC_CLASS_$_y416ToRawBayerPostProcessor
- _OBJC_IVAR_$_DefaultPostProcessor._converter
- _OBJC_IVAR_$_DefaultPostProcessor.exactBytesPerRow
- _OBJC_IVAR_$_DefaultPostProcessor.originalPixelFormat
- _OBJC_IVAR_$_DefaultPostProcessor.removePadding
- _OBJC_IVAR_$_L008ToNonPlanarPostProcessor._pool
- _OBJC_IVAR_$_L016Raw14PostProcessor._l010OutputFormatRAW14L016
- _OBJC_IVAR_$_MetalPixelBufferUtility._enabled
- _OBJC_IVAR_$_MetalPixelBufferUtility._metalCommandQueue
- _OBJC_IVAR_$_MetalPixelBufferUtility._metalDevice
- _OBJC_IVAR_$_MetalPixelBufferUtility._pipeLineStates
- _OBJC_IVAR_$_RawBayerFromYUVPostProcessor._rawBayerMSBReplication
- _OBJC_IVAR_$_RawBayerPostProcessor._rawBayerMSBReplication
- _OBJC_IVAR_$_SampleBufferAndMetadata._metadata
- _OBJC_IVAR_$_SampleBufferAndMetadata._sampleBuffer
- _OBJC_IVAR_$_SampleTimeBuffer._name
- _OBJC_IVAR_$_SampleTimeBuffer._times
- _OBJC_IVAR_$_SampleTimeList._cached_cmtimes
- _OBJC_IVAR_$_SampleTimeList._cached_times
- _OBJC_IVAR_$_SampleTimeList._name
- _OBJC_IVAR_$_SampleTimeList._times
- _OBJC_IVAR_$_SampleTimeList._timestamps
- _OBJC_IVAR_$_SampleTimeRangeBuffer._ranges
- _OBJC_IVAR_$_SampleTimeRangeList._cached_ranges
- _OBJC_IVAR_$_SampleTimeRangeList._name
- _OBJC_IVAR_$_SampleTimeRangeList._ranges
- _OBJC_IVAR_$_VideoEncoderInterface._customEncoderConfig
- _OBJC_IVAR_$_VideoEncoderInterface._lastEncodingInfoFlags
- _OBJC_IVAR_$_VideoEncoderInterface._lastEncodingStatus
- _OBJC_IVAR_$_VideoEncoderInterface._pendigFrames
- _OBJC_IVAR_$_VideoEncoderInterface.m_config
- _OBJC_IVAR_$_VideoEncoderInterface.m_delegate
- _OBJC_IVAR_$_VideoEncoderInterface.m_enableAVEHighPerformanceProfile
- _OBJC_IVAR_$_VideoEncoderInterface.m_encoder
- _OBJC_IVAR_$_VideoEncoderInterface.m_encoderInitialized
- _OBJC_IVAR_$_VideoEncoderInterface.m_encodingQueue
- _OBJC_IVAR_$_VideoEncoderInterface.m_expectedFrameRate
- _OBJC_IVAR_$_VideoEncoderInterface.m_firstFrameReceived
- _OBJC_IVAR_$_VideoEncoderInterface.m_qpValue
- _OBJC_IVAR_$_VideoEncoderInterface.m_stream
- _OBJC_IVAR_$_y416ToRawBayerPostProcessor._pool
- _OBJC_METACLASS_$_CompandedRawBayerPostProcessor
- _OBJC_METACLASS_$_CompandedRawBayerPreProcessor
- _OBJC_METACLASS_$_DefaultPostProcessor
- _OBJC_METACLASS_$_DefaultPreProcessor
- _OBJC_METACLASS_$_L008ToNonPlanarPostProcessor
- _OBJC_METACLASS_$_L016Raw14PostProcessor
- _OBJC_METACLASS_$_L016Raw14PreProcessor
- _OBJC_METACLASS_$_MetalPixelBufferUtility
- _OBJC_METACLASS_$_NonPlanarToL008Processor
- _OBJC_METACLASS_$_PostProcessorFactory
- _OBJC_METACLASS_$_PreProcessorFactory
- _OBJC_METACLASS_$_RawBayerFromYUVPostProcessor
- _OBJC_METACLASS_$_RawBayerPostProcessor
- _OBJC_METACLASS_$_RawBayerPreProcessor
- _OBJC_METACLASS_$_RawBayerTo1stPlaneYUVPreProcessor
- _OBJC_METACLASS_$_RawBayerToYUVPreProcessor
- _OBJC_METACLASS_$_RawBayerToy416PreProcessor
- _OBJC_METACLASS_$_SampleBufferAndMetadata
- _OBJC_METACLASS_$_SampleTimeBuffer
- _OBJC_METACLASS_$_SampleTimeList
- _OBJC_METACLASS_$_SampleTimeRangeBuffer
- _OBJC_METACLASS_$_SampleTimeRangeList
- _OBJC_METACLASS_$_VideoEncoderInterface
- _OBJC_METACLASS_$_y416ToRawBayerPostProcessor
- __OBJC_$_CLASS_METHODS_MetalPixelBufferUtility
- __OBJC_$_CLASS_METHODS_PixelBufferUtility
- __OBJC_$_CLASS_METHODS_PostProcessorFactory
- __OBJC_$_CLASS_METHODS_PreProcessorFactory
- __OBJC_$_CLASS_METHODS_VideoEncoderInterface
- __OBJC_$_INSTANCE_METHODS_CompandedRawBayerPostProcessor
- __OBJC_$_INSTANCE_METHODS_CompandedRawBayerPreProcessor
- __OBJC_$_INSTANCE_METHODS_DefaultPostProcessor
- __OBJC_$_INSTANCE_METHODS_DefaultPreProcessor
- __OBJC_$_INSTANCE_METHODS_L008ToNonPlanarPostProcessor
- __OBJC_$_INSTANCE_METHODS_L016Raw14PostProcessor
- __OBJC_$_INSTANCE_METHODS_L016Raw14PreProcessor
- __OBJC_$_INSTANCE_METHODS_MetalPixelBufferUtility
- __OBJC_$_INSTANCE_METHODS_NonPlanarToL008Processor
- __OBJC_$_INSTANCE_METHODS_PostProcessorFactory
- __OBJC_$_INSTANCE_METHODS_PreProcessorFactory
- __OBJC_$_INSTANCE_METHODS_RawBayerFromYUVPostProcessor
- __OBJC_$_INSTANCE_METHODS_RawBayerPostProcessor
- __OBJC_$_INSTANCE_METHODS_RawBayerPreProcessor
- __OBJC_$_INSTANCE_METHODS_RawBayerTo1stPlaneYUVPreProcessor
- __OBJC_$_INSTANCE_METHODS_RawBayerToYUVPreProcessor
- __OBJC_$_INSTANCE_METHODS_RawBayerToy416PreProcessor
- __OBJC_$_INSTANCE_METHODS_SampleBufferAndMetadata
- __OBJC_$_INSTANCE_METHODS_SampleTimeBuffer
- __OBJC_$_INSTANCE_METHODS_SampleTimeList
- __OBJC_$_INSTANCE_METHODS_SampleTimeRangeBuffer
- __OBJC_$_INSTANCE_METHODS_SampleTimeRangeList
- __OBJC_$_INSTANCE_METHODS_VideoEncoderInterface
- __OBJC_$_INSTANCE_METHODS_y416ToRawBayerPostProcessor
- __OBJC_$_INSTANCE_VARIABLES_DefaultPostProcessor
- __OBJC_$_INSTANCE_VARIABLES_L008ToNonPlanarPostProcessor
- __OBJC_$_INSTANCE_VARIABLES_L016Raw14PostProcessor
- __OBJC_$_INSTANCE_VARIABLES_MetalPixelBufferUtility
- __OBJC_$_INSTANCE_VARIABLES_RawBayerFromYUVPostProcessor
- __OBJC_$_INSTANCE_VARIABLES_RawBayerPostProcessor
- __OBJC_$_INSTANCE_VARIABLES_SampleBufferAndMetadata
- __OBJC_$_INSTANCE_VARIABLES_SampleTimeBuffer
- __OBJC_$_INSTANCE_VARIABLES_SampleTimeList
- __OBJC_$_INSTANCE_VARIABLES_SampleTimeRangeBuffer
- __OBJC_$_INSTANCE_VARIABLES_SampleTimeRangeList
- __OBJC_$_INSTANCE_VARIABLES_VideoEncoderInterface
- __OBJC_$_INSTANCE_VARIABLES_y416ToRawBayerPostProcessor
- __OBJC_$_PROP_LIST_CompandedRawBayerPreProcessor
- __OBJC_$_PROP_LIST_DefaultPostProcessor
- __OBJC_$_PROP_LIST_DefaultPreProcessor
- __OBJC_$_PROP_LIST_L016Raw14PostProcessor
- __OBJC_$_PROP_LIST_L016Raw14PreProcessor
- __OBJC_$_PROP_LIST_MetalPixelBufferUtility
- __OBJC_$_PROP_LIST_NonPlanarToL008Processor
- __OBJC_$_PROP_LIST_RawBayerFromYUVPostProcessor
- __OBJC_$_PROP_LIST_RawBayerPostProcessor
- __OBJC_$_PROP_LIST_RawBayerPreProcessor
- __OBJC_$_PROP_LIST_RawBayerTo1stPlaneYUVPreProcessor
- __OBJC_$_PROP_LIST_RawBayerToYUVPreProcessor
- __OBJC_$_PROP_LIST_RawBayerToy416PreProcessor
- __OBJC_$_PROP_LIST_SampleBufferAndMetadata
- __OBJC_$_PROP_LIST_SampleTimeBuffer
- __OBJC_$_PROP_LIST_SampleTimeList
- __OBJC_$_PROP_LIST_SampleTimeRangeList
- __OBJC_$_PROP_LIST_VideoEncoderInterface
- __OBJC_CLASS_PROTOCOLS_$_CompandedRawBayerPreProcessor
- __OBJC_CLASS_PROTOCOLS_$_DefaultPostProcessor
- __OBJC_CLASS_PROTOCOLS_$_DefaultPreProcessor
- __OBJC_CLASS_PROTOCOLS_$_L008ToNonPlanarPostProcessor
- __OBJC_CLASS_PROTOCOLS_$_L016Raw14PreProcessor
- __OBJC_CLASS_PROTOCOLS_$_NonPlanarToL008Processor
- __OBJC_CLASS_PROTOCOLS_$_RawBayerPreProcessor
- __OBJC_CLASS_PROTOCOLS_$_RawBayerTo1stPlaneYUVPreProcessor
- __OBJC_CLASS_PROTOCOLS_$_RawBayerToYUVPreProcessor
- __OBJC_CLASS_PROTOCOLS_$_RawBayerToy416PreProcessor
- __OBJC_CLASS_PROTOCOLS_$_SampleTimeRangeList
- __OBJC_CLASS_PROTOCOLS_$_VideoEncoderInterface
- __OBJC_CLASS_RO_$_CompandedRawBayerPostProcessor
- __OBJC_CLASS_RO_$_CompandedRawBayerPreProcessor
- __OBJC_CLASS_RO_$_DefaultPostProcessor
- __OBJC_CLASS_RO_$_DefaultPreProcessor
- __OBJC_CLASS_RO_$_L008ToNonPlanarPostProcessor
- __OBJC_CLASS_RO_$_L016Raw14PostProcessor
- __OBJC_CLASS_RO_$_L016Raw14PreProcessor
- __OBJC_CLASS_RO_$_MetalPixelBufferUtility
- __OBJC_CLASS_RO_$_NonPlanarToL008Processor
- __OBJC_CLASS_RO_$_PostProcessorFactory
- __OBJC_CLASS_RO_$_PreProcessorFactory
- __OBJC_CLASS_RO_$_RawBayerFromYUVPostProcessor
- __OBJC_CLASS_RO_$_RawBayerPostProcessor
- __OBJC_CLASS_RO_$_RawBayerPreProcessor
- __OBJC_CLASS_RO_$_RawBayerTo1stPlaneYUVPreProcessor
- __OBJC_CLASS_RO_$_RawBayerToYUVPreProcessor
- __OBJC_CLASS_RO_$_RawBayerToy416PreProcessor
- __OBJC_CLASS_RO_$_SampleBufferAndMetadata
- __OBJC_CLASS_RO_$_SampleTimeBuffer
- __OBJC_CLASS_RO_$_SampleTimeList
- __OBJC_CLASS_RO_$_SampleTimeRangeBuffer
- __OBJC_CLASS_RO_$_SampleTimeRangeList
- __OBJC_CLASS_RO_$_VideoEncoderInterface
- __OBJC_CLASS_RO_$_y416ToRawBayerPostProcessor
- __OBJC_METACLASS_RO_$_CompandedRawBayerPostProcessor
- __OBJC_METACLASS_RO_$_CompandedRawBayerPreProcessor
- __OBJC_METACLASS_RO_$_DefaultPostProcessor
- __OBJC_METACLASS_RO_$_DefaultPreProcessor
- __OBJC_METACLASS_RO_$_L008ToNonPlanarPostProcessor
- __OBJC_METACLASS_RO_$_L016Raw14PostProcessor
- __OBJC_METACLASS_RO_$_L016Raw14PreProcessor
- __OBJC_METACLASS_RO_$_MetalPixelBufferUtility
- __OBJC_METACLASS_RO_$_NonPlanarToL008Processor
- __OBJC_METACLASS_RO_$_PostProcessorFactory
- __OBJC_METACLASS_RO_$_PreProcessorFactory
- __OBJC_METACLASS_RO_$_RawBayerFromYUVPostProcessor
- __OBJC_METACLASS_RO_$_RawBayerPostProcessor
- __OBJC_METACLASS_RO_$_RawBayerPreProcessor
- __OBJC_METACLASS_RO_$_RawBayerTo1stPlaneYUVPreProcessor
- __OBJC_METACLASS_RO_$_RawBayerToYUVPreProcessor
- __OBJC_METACLASS_RO_$_RawBayerToy416PreProcessor
- __OBJC_METACLASS_RO_$_SampleBufferAndMetadata
- __OBJC_METACLASS_RO_$_SampleTimeBuffer
- __OBJC_METACLASS_RO_$_SampleTimeList
- __OBJC_METACLASS_RO_$_SampleTimeRangeBuffer
- __OBJC_METACLASS_RO_$_SampleTimeRangeList
- __OBJC_METACLASS_RO_$_VideoEncoderInterface
- __OBJC_METACLASS_RO_$_y416ToRawBayerPostProcessor
- __ZN19HEVCLosslessEncoder11EncodeFrameEP10__CVBuffer6CMTimePK14__CFDictionaryPv
- __ZN19HEVCLosslessEncoder15isSessionClosedEv
- __ZN19HEVCLosslessEncoder16useQPCompressionEi
- __ZN19HEVCLosslessEncoder22frameReorderingEnabledEv
- __ZN19HEVCLosslessEncoder25propogateColorAttachmentsEPK25opaqueCMFormatDescriptionP26OpaqueVTCompressionSession
- __ZN19HEVCLosslessEncoder4OpenEii10IMG_FORMATdPK25opaqueCMFormatDescriptionPFvPvS4_ijP20opaqueCMSampleBufferES4_
- __ZN19HEVCLosslessEncoder5CloseEv
- __ZN19HEVCLosslessEncoderC1Ev
- __ZN19HEVCLosslessEncoderC2Ev
- __ZN19HEVCLosslessEncoderD1Ev
- __ZN19HEVCLosslessEncoderD2Ev
- __ZZ37+[PreProcessorFactory defaultFactory]E7factory
- __ZZ37+[PreProcessorFactory defaultFactory]E9onceToken
- __ZZ38+[PostProcessorFactory defaultFactory]E7factory
- __ZZ38+[PostProcessorFactory defaultFactory]E9onceToken
- __ZZ47+[PixelBufferUtility sharedBytesPerPixelLookUp]E6lookup
- __ZZ47+[PixelBufferUtility sharedBytesPerPixelLookUp]E9onceToken
- ___37+[PreProcessorFactory defaultFactory]_block_invoke
- ___38+[PostProcessorFactory defaultFactory]_block_invoke
- ___41-[MOVStreamWriter processFinishRecording]_block_invoke.390
- ___41-[MOVStreamWriter processFinishRecording]_block_invoke.391
- ___47+[PixelBufferUtility sharedBytesPerPixelLookUp]_block_invoke
- ___50-[MOVStreamWriter consumeMetadatOfMetadataStream:]_block_invoke
- ___52-[MOVStreamWriter consumeSamplesOfVideoAudioStream:]_block_invoke
- ___53-[VideoEncoderInterface closeEncoderInDispatchGroup:]_block_invoke
- ___56+[MetalPixelBufferUtility sharedMetalPixelBufferUtility]_block_invoke
- ___66-[VideoEncoderInterface encodeFrame:pst:frameProperties:metadata:]_block_invoke
- ___block_descriptor_65_ea8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
- ___block_descriptor_72_ea8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
- ___block_descriptor_88_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.407
- ___block_literal_global.7
- __unnamed_array_storage.242
- _objc_msgSend$createMIOPixelBufferPoolWithWidth:height:pixelFormat:exactBytesPerRow:minBufferCount:
- _objc_msgSend$createMIOPixelBufferPoolWithWidth:height:pixelFormat:exactBytesPerRows:minBufferCount:
- _objc_msgSend$createMIOPixelBufferPoolWithWidth:height:pixelFormat:extendedPixelsPerRow:minBufferCount:
- _objc_msgSend$createNewL008MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:
- _objc_msgSend$createNewL010MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:
- _objc_msgSend$encodeFrame:pst:frameProperties:metadata:
- _objc_msgSend$initWithTargetWidth:height:format:bytesPerRow:
- _objc_msgSend$initWithTargetWidth:height:format:bytesPerRows:
- _objc_msgSend$initWithVideoTrack:assetReader:associatedMetadataTracks:version:unknownStreamId:reader:delegate:error:
- _objc_msgSend$isReadyForMoreDataForStreamId:fromMap:
- _objc_msgSend$pendigFrames
- _objc_msgSend$postProcessorFromReader:originalPixelFormat:encodedFormat:encoderType:streamId:
- _objc_msgSend$processFrame:pst:frameProperties:metadata:
- _objc_msgSend$setPendigFrames:
CStrings:
+ "\x01!"
+ "\x06\x12\xf0\xf0A31"
+ "  [FIFO] %{public}@ = %lu (metadata)  ready: %d"
+ "  [FIFO] %{public}@ = %lu ready: %d %d"
+ "%@ attachment is required for all color pixel formats"
+ "%@ attachment is required for all grayscale pixel formats"
+ "%@ attachment is required for all pixel formats with 4:2:0 subsampling"
+ "%@ attachment is required for all pixel formats with YCbCr sampling"
+ "%@ attachment is unexpectedly missing for a pixel format using interlaced scanning"
+ "%@ attachment is unexpectedly present for a grayscale pixel format"
+ "%@ attachment is unexpectedly present for a pixel format without 4:2:0 subsampling"
+ "%@ attachment is unexpectedly present for a pixel format without 4:2:2 subsampling"
+ "%{public}@: Encoder frame reordering enabled: %d."
+ "+[MOVStreamIOUtility colorimetricWarningsForColorPixelBufferAttachments:pixelFormat:]"
+ "-[MOVStreamFrameTransform initWithRotation:flip:bufferCacheMode:]"
+ "-[MOVStreamMetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:]"
+ "-[MOVStreamWriter finishAVWriter]"
+ "/Library/Caches/com.apple.xbs/Sources/MOVStreamIO/MOVStreamIO/VTEncoder/MOVStreamHEVCLosslessEncoder.mm"
+ "3.21.0"
+ "@\"MOVStreamSampleTimeList\""
+ "@\"NSDictionary\"32@0:8@\"MOVStreamVideoEncoderInterface\"16@\"NSString\"24"
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSThread\""
+ "@20@0:8i16"
+ "@24@0:8I16i20"
+ "@24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
+ "@28@0:8@16I24"
+ "@28@0:8I16i20B24"
+ "@32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16d24"
+ "@36@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16d24B32"
+ "@36@0:8^{__CVBuffer=}16Q24i32"
+ "@36@0:8q16q24i32"
+ "@40@0:8Q16Q24I32i36"
+ "@48@0:8Q16Q24I32@36i44"
+ "@48@0:8Q16Q24I32Q36i44"
+ "@52@0:8@16I24I28@32@40i48"
+ "@56@0:8Q16Q24I32@36Q44i52"
+ "@56@0:8Q16Q24I32Q36Q44i52"
+ "@84@0:8@\"AVAssetTrack\"16@\"AVAssetReader\"24@\"NSArray\"32@\"MIOVersion\"40i48@\"NSString\"52@\"MOVStreamReader\"60@\"<MOVStreamReaderDelegate>\"68^@76"
+ "@84@0:8@16@24@32@40i48@52@60@68^@76"
+ "AVAssetWriter shouldOptimizeForNetworkUse = YES"
+ "AdditionalCompressionProperties"
+ "B24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
+ "B24@0:8^{opaqueCMSampleBuffer=}16"
+ "B36@0:8i16@20^@28"
+ "B40@0:8@\"MOVStreamVideoEncoderInterface\"16^{OpaqueVTCompressionSession=}24@\"NSString\"32"
+ "B64@0:8^{__CVBuffer=}16{?=qiIq}24^{__CFDictionary=}48@56"
+ "BufferCacheMode"
+ "Can't add metadata input to the asset writer to stream: %@"
+ "Cannot allocate reference buffer (Format: %d)."
+ "Cannot set baseMediaTimeScale for audio stream."
+ "Cannot set baseMediaTimeScale in current writer state."
+ "Empty Edit frame detected for stream '%{public}@'."
+ "Encoder Config >> kVTCompressionPropertyKey_Quality = %f"
+ "Exception during finishWritingWithCompletionHandler: %{public}@"
+ "FIFO buffer for metadata stream '%@' is full, dropping older buffer (%llu/%llu/%llu/%llu)."
+ "I24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
+ "I32@0:8@\"MOVStreamVideoEncoderInterface\"16@\"NSString\"24"
+ "Images with Rec 2020 or Rec 2100 color primaries and 4:2:0 subsampling are only defined for attachments containing topLeft chroma locations."
+ "Images with Rec 2020 or Rec 2100 color primaries are only defined for attachments containing Rec 2020 or Rec 2100 YCbCr matrices."
+ "Images with Rec 2020 or Rec 2100 color primaries are only defined for video range pixel formats."
+ "InternalCodecType"
+ "Invalid metadata streamId 'nil'."
+ "Last Trigger!"
+ "MIOPixelBufferUtility"
+ "MOVStreamCompandedRawBayerPostProcessor"
+ "MOVStreamCompandedRawBayerPreProcessor"
+ "MOVStreamDefaultPostProcessor"
+ "MOVStreamDefaultPreProcessor"
+ "MOVStreamL008ToNonPlanarPostProcessor"
+ "MOVStreamL016Raw14PostProcessor"
+ "MOVStreamL016Raw14PreProcessor"
+ "MOVStreamMetalPixelBufferUtility"
+ "MOVStreamMetalPixelBufferUtility.m"
+ "MOVStreamNonPlanarToL008Processor"
+ "MOVStreamPostProcessorFactory"
+ "MOVStreamPreProcessorFactory"
+ "MOVStreamRawBayerFromYUVPostProcessor"
+ "MOVStreamRawBayerPostProcessor"
+ "MOVStreamRawBayerPreProcessor"
+ "MOVStreamRawBayerTo1stPlaneYUVPreProcessor"
+ "MOVStreamRawBayerToYUVPreProcessor"
+ "MOVStreamRawBayerToy416PreProcessor"
+ "MOVStreamSampleBufferAndMetadata"
+ "MOVStreamSampleTimeBuffer"
+ "MOVStreamSampleTimeList"
+ "MOVStreamSampleTimeRangeBuffer"
+ "MOVStreamSampleTimeRangeList"
+ "MOVStreamVideoEncoderInterface"
+ "MOVStreamWriterStreamStats"
+ "MOVStreamy416ToRawBayerPostProcessor"
+ "Metadata was appended with presentation timestamp (%f) less than (or equal to) previous sample buffer (%f) for stream '%@'. Dropping sample."
+ "Mode for pixel buffer attachments for RawBayer pixel buffers is not set to PLIST! Default format is overridden by client (kMIOFrameAttachmentSerializationMode), this will be ignored for RawBayer."
+ "PointsOfInterest"
+ "Q32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16d24"
+ "Sample buffer encoding failed (encoder status: %i flags: %d) for stream '%@'."
+ "Sample buffers attachments appended with presentation timestamp (%f) less than (or equal to) previous sample buffer (%f) for stream '%@'. Inconsistency!"
+ "Setting multiplexWritingDisabled is not supported anymore."
+ "Setup associated metadata track for streamId \"%{public}@\" metadataId \"%{public}@\""
+ "Setup metadata track with streamId \"%{public}@\""
+ "Still frames in Fifo. Wait..."
+ "Surface cache mode (MIOBufferCacheMode) is not an NSNumber value, specified for stream '%@'."
+ "T@\"MOVStreamEncoderConfig\",&,V_config"
+ "T@\"MOVStreamSampleTimeList\",&,N,V_timeList"
+ "T@\"NSDictionary\",&,V_settings"
+ "TB,V_canWriteData"
+ "TB,V_finalConsume"
+ "TB,V_finishingMode"
+ "TB,V_firstVideoFrameRead"
+ "TB,V_pixelFormatWasGuessed"
+ "TB,V_skipEmptyEditVideoFrame"
+ "TQ,V_attemptCount"
+ "TQ,V_fifoItemCount"
+ "TQ,V_visitCount"
+ "TQ,V_writeCount"
+ "TQ,V_writeThreadCount"
+ "Td"
+ "Ti"
+ "Ti,V_bufferCacheMode"
+ "Ti,VbufferCacheMode"
+ "Tq,V_pendingFrames"
+ "Unknown metadata stream id."
+ "VTVideoEncoderSetProperty kVTCompressionPropertyKey_Quality failed"
+ "Will add AVAssetWriterInput for stream '%{public}@'"
+ "Writer is not in MIOWriterStatusInit state."
+ "Writing pending frame attachments for stream '%{public}@'."
+ "[FIFO] FIFO buffer for stream '%s' is full, dropping older buffer (%llu/%llu/%llu/%llu) ."
+ "[FIFO] Usage:"
+ "[FINISH] %{public}@: Encoder close..."
+ "[FINISH] %{public}@: Encoder closed."
+ "[FINISH] %{public}@: Encoder complete session..."
+ "[FINISH] finishAVWriter 01"
+ "[FINISH] finishAVWriter 02"
+ "[FINISH] finishRecording"
+ "[FINISH] processFinishRecording 01"
+ "[FINISH] processFinishRecording 02"
+ "[FINISH] processFinishRecording 03"
+ "[FINISH] processFinishRecording 04"
+ "[FINISH] processFinishRecording 05"
+ "[FINISH] processFinishRecording 06"
+ "[FINISH] processFinishRecording 07"
+ "[FINISH] processFinishRecording 08"
+ "[FINISH] processFinishRecording 09"
+ "[FINISH] processFinishRecording 10"
+ "[FINISH] processForceFinishRecording"
+ "[FINISH] processForceFinishRecording 01"
+ "[FINISH] processForceFinishRecording 02"
+ "[FINISH] processForceFinishRecording 03"
+ "[FINISH] processForceFinishRecording 04"
+ "[FINISH] processForceFinishRecording 05"
+ "[FINISH] processForceFinishRecording 06"
+ "[FINISH] processForceFinishRecording 07"
+ "[FINISH] startFinishingTimeoutTimer (items in fifos)"
+ "[KVO] Update metadata stream '%{public}@' input ready: %d"
+ "[KVO] Update stream '%{public}@' input ready: %d"
+ "[MIO PERF a] %{public}@ duration %llu"
+ "[MIO PERF] duration %{public}@ %llu"
+ "[VTEncoder] processing buffer for stream '%@' is full, dropping buffer (Pending:%lld Queue:%ld Fifo:%ld Capacity:%ld) (%llu/%llu/%llu/%llu)."
+ "[WritingThread] Cannot set priority to 1.0."
+ "[WritingThread] Exiting writing loop."
+ "[WritingThread] Input for %{public}@ not ready."
+ "[WritingThread] [FIFO] Consume (%{public}@) PTS: %f (%lu/%lu)"
+ "[WritingThread] [FIFO] Precheck All Fifo items written '%{public}@'"
+ "[WritingThread] finalConsume"
+ "[WritingThread] nothing written (attempts: %d)."
+ "^{MOVStreamHEVCLosslessEncoder=B@iid^{OpaqueVTCompressionSession}{EncoderConfig=iiiidBBBBBi}{?=qiIq}IIIBB}"
+ "^{__CFDictionary=}44@0:8I16I20I24i28I32I36i40"
+ "^{__CVBuffer=}40@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}24^@32"
+ "^{__CVPixelBufferPool=}56@0:8Q16Q24I32Q36Q44i52"
+ "^{opaqueCMFormatDescription=}24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
+ "^{opaqueCMFormatDescription=}32@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}24"
+ "_attemptCount"
+ "_avfAppendSignPostID"
+ "_bufferCacheMode"
+ "_canWriteData"
+ "_fifoItemCount"
+ "_finalConsume"
+ "_finishingMode"
+ "_firstVideoFrameRead"
+ "_pendingFrames"
+ "_perfLogAVF"
+ "_pixelFormatWasGuessed"
+ "_skipEmptyEditVideoFrame"
+ "_visitCount"
+ "_writeCount"
+ "_writeThread"
+ "_writeThreadCount"
+ "_writingSema"
+ "addAdditionalHEVCCompressionProperties:recordingConfig:"
+ "addMetadataTrack:copyData:"
+ "aprh"
+ "aprn"
+ "attachmentsContainTopLeftChromaLocations:"
+ "attachmentsContainsRec2020orRec2100ColorMatrices:"
+ "attachmentsContainsRec2020orRec2100ColorPrimaries:"
+ "attachmentsRepresentInterlacedFields:"
+ "attemptCount"
+ "bufferCacheMode"
+ "bufferHasPadding:"
+ "bytesPerWidthOfBuffer:"
+ "canWriteData"
+ "chromaSubsamplingForDictionary:"
+ "chromaSubsamplingForFormatDescription:"
+ "colorimetricWarningsForColorPixelBufferAttachments:pixelFormat:"
+ "colorimetricWarningsForGrayscalePixelBufferAttachments:pixelFormat:"
+ "com.apple.movstreamwriter.writeravf"
+ "com.apple.movstreamwriter.writingthread"
+ "com.apple.streamwriter.processing"
+ "com.apple.videoeng.streamwritererror"
+ "configWithEncoderType:"
+ "consumeMetadatOfMetadataStream: %@"
+ "consumeSamplesOfVideoAudioStream: %@"
+ "createMIOPixelBufferPoolWithWidth:height:pixelFormat:exactBytesPerRow:minBufferCount:bufferCacheMode:"
+ "createMIOPixelBufferPoolWithWidth:height:pixelFormat:exactBytesPerRows:minBufferCount:bufferCacheMode:"
+ "createMIOPixelBufferPoolWithWidth:height:pixelFormat:extendedPixelsPerRow:minBufferCount:bufferCacheMode:"
+ "createMIOPixelBufferPoolWithWidth:height:pixelFormat:minBufferCount:bufferCacheMode:"
+ "createNewL008MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:bufferCacheMode:"
+ "createNewL010MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:bufferCacheMode:"
+ "createPixelBufferAttributesWithWidth:height:extendedPixelsPerRow:pixelFormat:bytesPerRowAlignment:planeAlignment:bufferCacheMode:"
+ "createPixelBufferPoolWithWidth:height:format:extendedPixelsPerRow:minBufferCount:bufferCacheMode:"
+ "customTrackMetadataItems"
+ "customTrackMetadataItemsForStream:"
+ "d24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@i}16"
+ "dictionary:booleanValueForKey:"
+ "dictionary:numberValueForKey:"
+ "dictionary:stringValueForKey:"
+ "dictionaryWithDictionary:"
+ "dictionaryWithObject:forKey:"
+ "encodeFrame:pts:frameProperties:metadata:"
+ "encodingFailedForStream"
+ "false"
+ "fifoItemCount"
+ "finalConsume"
+ "finishingMode"
+ "firstVideoFrameRead"
+ "formatDescriptionRepresentsBayer:"
+ "formatDescriptionRepresentsGrayscale:"
+ "formatDescriptionRepresentsRGB:"
+ "formatDescriptionRepresentsVideoRange:"
+ "formatDescriptionRepresentsYCbCr:"
+ "getCountByPriorityForFifo:capacity:"
+ "getOutputPixelFormatWasGuessedForStream"
+ "getOutputPixelFormatWasGuessedForStream:"
+ "i32@0:8Q16Q24"
+ "initWithBlock:"
+ "initWithOriginalPixelFormat:bufferCacheMode:"
+ "initWithOriginalPixelFormat:bufferCacheMode:l010OutputFormatRAW14L016:"
+ "initWithOriginalPixelFormat:bufferCacheMode:rawBayerMSBReplication:"
+ "initWithRotation:flip:bufferCacheMode:"
+ "initWithTargetWidth:height:format:bytesPerRow:bufferCacheMode:"
+ "initWithTargetWidth:height:format:bytesPerRows:bufferCacheMode:"
+ "initWithTargetWidth:height:format:extendedPixelsPerRow:bufferCacheMode:"
+ "initWithVideoTrack:assetReader:associatedMetadataTracks:version:bufferCacheMode:unknownStreamId:reader:delegate:error:"
+ "isEmptySample:"
+ "isSlimXEncodedTrack:"
+ "key:hasUnspecifiedValue:"
+ "logFifoUsage"
+ "lowercaseString"
+ "m_failedState"
+ "m_lastPtsForAttachmentsStream"
+ "m_lastPtsForMetadataStream"
+ "m_shouldOptimizeForNetworkUse"
+ "makeBufferConfigDict:height:pixelFormat:bufferCacheMode:"
+ "mio.appendSampleBuffer"
+ "mio.appendTimedMetadataGroup"
+ "mio.att_appendTimedMetadataGroup"
+ "mp4"
+ "multiplexWritingDisabled"
+ "pathExtension"
+ "pendingFrames"
+ "pixelFormatForUnknownTrackOfReader:streamId:"
+ "pixelFormatIs420Sampled:"
+ "pixelFormatIs422Sampled:"
+ "pixelFormatWasGuessed"
+ "postProcessorFromReader:originalPixelFormat:encodedFormat:encoderType:streamId:bufferCacheMode:"
+ "processFrame:pts:frameProperties:metadata:"
+ "proresRAWHQSettings:frameRate:"
+ "proresRAWSettings:frameRate:"
+ "reason"
+ "reservedMIOTrackMetadataKeys"
+ "setAttemptCount:"
+ "setBufferCacheMode:"
+ "setCanWriteData:"
+ "setConfig:"
+ "setFifoItemCount:"
+ "setFinalConsume:"
+ "setFinishingMode:"
+ "setFirstVideoFrameRead:"
+ "setMediaTimeScale:forMetadataStream:error:"
+ "setMediaTimeScale:forStream:error:"
+ "setMultiplexWritingDisabled:"
+ "setObject:forKeyedSubscript:"
+ "setPendingFrames:"
+ "setPixelFormatWasGuessed:"
+ "setQualityOfService:"
+ "setSettings:"
+ "setShouldOptimizeForNetworkUse:"
+ "setSkipEmptyEditVideoFrame:"
+ "setThreadPriority:"
+ "setTrackMetadataItems:forStream:error:"
+ "setVisitCount:"
+ "setWriteCount:"
+ "setWriteThreadCount:"
+ "shouldOptimizeForNetworkUse"
+ "skipEmptyEditVideoFrame"
+ "slmC"
+ "start"
+ "startWritingThread"
+ "stringByRemovingPercentEncoding"
+ "stripBufferPadding:"
+ "triggerWritingThread"
+ "v28@0:8@16B24"
+ "v32@0:8@\"MOVStreamVideoEncoderInterface\"16@\"NSString\"24"
+ "v72@0:8@\"MOVStreamVideoEncoderInterface\"16^{opaqueCMSampleBuffer=}24@\"AVTimedMetadataGroup\"32{?=qiIq}40@\"NSString\"64"
+ "visitCount"
+ "write fifo samples"
+ "write thread"
+ "writeCount"
+ "writeMetadata: call 'metadataAdaptor appendTimedMetadataGroup' for stream: %@"
+ "writeMetadata: call 'metadataAdaptor appendTimedMetadataGroup' for stream: %@ Success: %d"
+ "writeThreadCount"
+ "writerErrorWithMessage:code:"
+ "\xb1"
+ "⚠️⚠️⚠️ WARNING [MOVStreamIO]: Selected file type is 'mp4'. Be aware that this can and will cause data loss. If you can please use 'mov'. ⚠️⚠️⚠️"
+ "⚠️⚠️⚠️ WARNING [MOVStreamIO]: setFinishingTimeout to %.1f sec below recommended minimum value %.1f sec."
+ "\xf0\xf0\xf0\x92"
- "\x01\x11"
- "\a\xf0\xd11\x11"
- "%{public}@: Encoder closed."
- "-[MOVStreamFrameTransform initWithRotation:flip:]"
- "-[MetalPixelBufferUtility processBayerBuffer:withWarholBuffer:shiftCount:msbReplication:operation:sampleSize:]"
- "/Library/Caches/com.apple.xbs/Sources/MOVStreamIO/MOVStreamIO/VTEncoder/HEVCLosslessEncoder.mm"
- "3.19.9"
- "@\"NSDictionary\"32@0:8@\"VideoEncoderInterface\"16@\"NSString\"24"
- "@\"SampleTimeList\""
- "@24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}16"
- "@32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}16d24"
- "@36@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}16d24B32"
- "B24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}16"
- "B40@0:8@\"VideoEncoderInterface\"16^{OpaqueVTCompressionSession=}24@\"NSString\"32"
- "Can't add smetadata input to the asset writer to stream: %@"
- "Cannot allocate reference buffer."
- "CompandedRawBayerPostProcessor"
- "CompandedRawBayerPreProcessor"
- "DefaultPostProcessor"
- "DefaultPreProcessor"
- "Encoder Config >> my_kVTCompressionPropertyKey_LossLess = %d"
- "FIFO buffer for metadata stream '%@' is full, dropping older buffer."
- "I24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}16"
- "I32@0:8@\"VideoEncoderInterface\"16@\"NSString\"24"
- "L008ToNonPlanarPostProcessor"
- "L016Raw14PostProcessor"
- "L016Raw14PreProcessor"
- "LossLess"
- "MetalPixelBufferUtility"
- "MetalPixelBufferUtility.m"
- "Mode for pixel buffer attachements for RawBayer pixel buffers is not set to PLIST! Default format is overriden by client (kMIOFrameAttachmentSerializationMode), this will be ignored for RawBayer."
- "NonPlanarToL008Processor"
- "PortTypeBack"
- "PostProcessorFactory"
- "PreProcessorFactory"
- "Q32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}16d24"
- "RawBayerFromYUVPostProcessor"
- "RawBayerPostProcessor"
- "RawBayerPreProcessor"
- "RawBayerTo1stPlaneYUVPreProcessor"
- "RawBayerToYUVPreProcessor"
- "RawBayerToy416PreProcessor"
- "Sample buffer encoding failed (encoder status: %i flags: %d) for stream '%@'. Dropping frame."
- "SampleBufferAndMetadata"
- "SampleTimeBuffer"
- "SampleTimeList"
- "SampleTimeRangeBuffer"
- "SampleTimeRangeList"
- "Setup metadata track with identifier \"%{public}@\""
- "SlimXFormat"
- "T@\"MOVStreamEncoderConfig\",R,V_config"
- "T@\"NSDictionary\",R,V_settings"
- "T@\"SampleTimeList\",&,N,V_timeList"
- "Td,V_finishingTimeout"
- "Tq,V_pendigFrames"
- "VTVideoEncoderSetProperty my_kVTCompressionPropertyKey_LossLess failed"
- "VideoEncoderInterface"
- "Writing pending frame attachements for stream '%{public}@'."
- "[FIFO] FIFO buffer for stream '%s' is full, dropping older buffer."
- "[FIFO] Precheck All Fifo items written '%{public}@'"
- "[VTEncoder] processing buffer for stream '%@' is full, dropping buffer (Pending:%lld Queue:%ld Fifo:%ld Capacity:%ld)."
- "^{HEVCLosslessEncoder=B@iid^{OpaqueVTCompressionSession}{EncoderConfig=iiiidBBBBBi}{?=qiIq}IIIBB}"
- "^{__CVBuffer=}40@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}24^@32"
- "^{opaqueCMFormatDescription=}24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}16"
- "^{opaqueCMFormatDescription=}32@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}24"
- "_pendigFrames"
- "com.apple.streamwriter.encoding"
- "createNewL008MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:"
- "createNewL010MIOPixelBufferPoolWithReferencePixelBuffer:minBufferCount:"
- "d24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@{?=qiIq}Q@q}16"
- "encodeFrame:pst:frameProperties:metadata:"
- "initWithVideoTrack:assetReader:associatedMetadataTracks:version:unknownStreamId:reader:delegate:error:"
- "m_firstFrameReceived"
- "pendigFrames"
- "processFrame:pst:frameProperties:metadata:"
- "setPendigFrames:"
- "v32@0:8@\"VideoEncoderInterface\"16@\"NSString\"24"
- "v72@0:8@\"VideoEncoderInterface\"16^{opaqueCMSampleBuffer=}24@\"AVTimedMetadataGroup\"32{?=qiIq}40@\"NSString\"64"
- "y416ToRawBayerPostProcessor"
- "\xa1"
- "\xf0\xf0\xd2"

```
