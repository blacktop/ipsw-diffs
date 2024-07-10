## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox`

```diff

-3145.65.1.0.0
-  __TEXT.__text: 0xcc7e30
+3145.61.2.0.0
+  __TEXT.__text: 0xcbf518
   __TEXT.__auth_stubs: 0xa8a0
   __TEXT.__objc_methlist: 0x1910
   __TEXT.__const: 0x1c400
   __TEXT.__gcc_except_tab: 0x133c
-  __TEXT.__cstring: 0xf5c96
-  __TEXT.__oslogstring: 0x10994c
+  __TEXT.__cstring: 0xf5590
+  __TEXT.__oslogstring: 0x108079
   __TEXT.__ustring: 0x1f8
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__unwind_info: 0xf980
+  __TEXT.__unwind_info: 0xf900
   __TEXT.__eh_frame: 0x1c1c
   __TEXT.__objc_classname: 0x73f
   __TEXT.__objc_methname: 0x46f9
   __TEXT.__objc_methtype: 0x1b79
   __TEXT.__objc_stubs: 0x4480
-  __DATA_CONST.__got: 0x2f18
-  __DATA_CONST.__const: 0x16058
+  __DATA_CONST.__got: 0x2f08
+  __DATA_CONST.__const: 0x16028
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x5468
   __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__const: 0x31ea0
-  __AUTH_CONST.__cfstring: 0x4d640
+  __AUTH_CONST.__const: 0x31b80
+  __AUTH_CONST.__cfstring: 0x4d560
   __AUTH_CONST.__objc_const: 0x42c0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__data: 0x15a8
   __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x8960
-  __DATA.__common: 0x2b78
-  __DATA.__bss: 0x5f20
+  __DATA.__common: 0x2b58
+  __DATA.__bss: 0x5f10
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21617
-  Symbols:   12699
-  CStrings:  32913
+  Functions: 21563
+  Symbols:   12692
+  CStrings:  32857
 
Symbols:
+ _FigCMCDHeaderVendorGetURLHostName
+ _FigCMCDHeaderVendorSetURLHostName
+ _kFigSampleAttachmentKey_PostDecodeProcessingMetadata
- _FigLoadAVFDylib
- _FigMetricItemVariantChangeStartEventCreate
- _kCMSampleAttachmentKey_PostDecodeProcessingMetadata
- _kFigContentKeyBossProperty_CMCDHeaderVendor
- _kFigMetadataReaderProperty_ContainerByteStream
- _kFigSampleBufferConduitNotificationParameter_CollectorCoherenceToken
- _kFigSampleBufferConduitNotification_CollectorCoherence
- _kFigVideoPerformanceKey_NumberOfFramesWithContiguousData
- _kFigVideoPerformanceKey_NumberOfFramesWithNonContiguousData
- _kVideoMentorKey_CollectorCoherenceToken
CStrings:
+ "Media Entry URL not match previous playlist for MEDIA-SEQUENCE %!l(MISSING)lu: %!s(MISSING) vs %!s(MISSING)"
+ "New EXT-X-PART segments cannot be added after parent segment %!s(MISSING) appears"
+ "No referencedDataRef."
+ "Rate must be >= 0"
+ "[FigMetricItremLikelyToKeepUpEvent %!p(MISSING)]"
+ "appendMemoryPoolBlockBuffer"
+ "bapspManager_setRateAndAnchorTime"
+ "flushDataBuffer"
+ "fpic_CheckIfPrimaryPlayheadHasReachedTimeToPausePlayback"
+ "fpic_InitiateSeekOutOfEvent"
+ "fpic_InitiateSeekOutOfEvent_block_invoke"
+ "referencedDataByteOffsetRef allocation failed."
+ "sbcbq_postOneSideNotification"
+ "segPumpEnsureCMCDHeaderVendor"
+ "segPumpLoadInformation"
- "/System/Library/Frameworks/AVFoundation.framework/AVFoundation"
- "CollectorCoherenceToken"
- "Failed to allocate payloadDictionary"
- "FigLoadAVFDylib_block_invoke"
- "FigMetricItemVariantChangeStartEvent.c"
- "FigMetricItemVariantChangeStartEventCreate"
- "Media Entry URL not match previous playlist for MEDIA-SEQUENCE %!l(MISSING)lu: %!@(MISSING) vs %!@(MISSING)"
- "MovieSampleDataWriterFlush"
- "Multivariant playlist can only be the top-level playlist"
- "New EXT-X-PART segments cannot be added after parent segment %!@(MISSING) appears"
- "No dataRef."
- "NumberOfFramesWithContiguousData"
- "NumberOfFramesWithNonContiguousData"
- "Pump is invalid"
- "[FigMetricItemLikelyToKeepUpEvent %!p(MISSING)]"
- "[FigMetricItemVariantChangeStartEvent %!p(MISSING)]"
- "appendAggregateBBufToByteStream"
- "appendDataBufferBBufReferenceToAggregateBBufAndBeginNewDataBuffer"
- "appendMemoryPoolBlockBufferToSampleDataDestination"
- "audioRenderer_shouldAllowAtmosDecode"
- "blockBufferCreateWithMemoryPoolBBufReferenceIncludingPadding"
- "checkIfShouldAppendSampleDataToDataBuffer"
- "containerByteStream"
- "dataByteOffsetRef allocation failed."
- "dataRef NULL"
- "event is not mutable"
- "figPlaybackCoordinator_playerPauseShouldBeIgnored"
- "fiit_createInterstitialSegment"
- "fiit_createPrimarySegment"
- "fiit_rebuildSegmentList"
- "fpic_CheckIfPlayheadHasReachedPrimaryPlaybackGate"
- "fpic_ObserveSeekOutOfEvent"
- "fpic_ObserveSeekOutOfEvent_block_invoke"
- "fpic_UpdateResolvedEventTimeIfNecessary"
- "fragManifold_SetTrackLatestFormatDescription"
- "itemfig_isAtmosSupported"
- "kCKBP_CMCDHeaderVendor"
- "kFigMetricEventError_InternalError"
- "kFigRemakerError_TempFileCreateFailed"
- "kMTPluginFormatReaderError_ExtensionDisabled"
- "kMediaDataChunkWriterError_InternalLogicFailed"
- "mee_setMediaTime"
- "mee_setSessionID"
- "meiltku_setMediaTime"
- "meiltku_setSessionID"
- "meirc_setMediaTime"
- "meirc_setSessionID"
- "meivc_setMediaTime"
- "meivc_setSessionID"
- "meivcs_setMediaTime"
- "meivcs_setSessionID"
- "memPool allocation failed."
- "memPoolBBuf is not contiguous"
- "mepe_setMediaTime"
- "mepe_setSessionID"
- "merr_setMediaTime"
- "merr_setSessionID"
- "mes_setMediaTime"
- "mes_setSessionID"
- "mutableProperties allocation failed."
- "owning player is null"
- "received bad temp directory URL"
- "sbcbq_postSideQueuePendingNotifications"
- "segPumpAPICheckStatus"
- "segPumpAPIUnlockAndSendNotificationThenCheckAPIStatus"
- "surrogatePlayer_respondToFailedLoadingOfItemAssetTypeInternal"
- "transferAIMEMetadataAndCopyUpdatedProperties"
- "transferMetadataItems"
- "transferMetadataItemsFromReader"
- "variant NULL"
- "videoMentorPostCollectorCoherenceConduitNotification"

```
