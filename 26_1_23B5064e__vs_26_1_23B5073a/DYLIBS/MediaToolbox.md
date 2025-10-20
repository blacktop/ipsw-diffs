## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3285.9.1.0.0
-  __TEXT.__text: 0xb8b2d8
-  __TEXT.__auth_stubs: 0xb340
+3285.11.1.3.0
+  __TEXT.__text: 0xb8d974
+  __TEXT.__auth_stubs: 0xb350
   __TEXT.__objc_methlist: 0x2484
   __TEXT.__const: 0x4e4c0
-  __TEXT.__cstring: 0x6ace7
-  __TEXT.__oslogstring: 0x563d8
+  __TEXT.__cstring: 0x6ae4c
+  __TEXT.__oslogstring: 0x56b70
   __TEXT.__ustring: 0x23e
   __TEXT.__gcc_except_tab: 0x106c
   __TEXT.__dlopen_cstrs: 0x1c8

   __TEXT.__objc_methname: 0x6aba
   __TEXT.__objc_methtype: 0x2901
   __TEXT.__objc_stubs: 0x6100
-  __DATA_CONST.__got: 0x38f8
-  __DATA_CONST.__const: 0x23490
+  __DATA_CONST.__got: 0x3900
+  __DATA_CONST.__const: 0x234b0
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x59b8
+  __AUTH_CONST.__auth_got: 0x59c0
   __AUTH_CONST.__const: 0x414b8
-  __AUTH_CONST.__cfstring: 0x4fd40
+  __AUTH_CONST.__cfstring: 0x4fda0
   __AUTH_CONST.__objc_const: 0x4db8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9203E259-D4FB-38EB-A412-599FD28F0EA0
-  Functions: 38921
-  Symbols:   100285
-  CStrings:  31631
+  UUID: 9D059BDF-210D-3245-967B-2D81C5A410B9
+  Functions: 38933
+  Symbols:   100316
+  CStrings:  31659
 
Symbols:
+ _FigEndpointStreamAudioFormatDescriptionGetTypeID
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.180
+ ___block_descriptor_tmp.182
+ ___block_descriptor_tmp.189
+ ___block_descriptor_tmp.191
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.217
+ ___block_descriptor_tmp.218
+ ___block_descriptor_tmp.219
+ ___block_descriptor_tmp.220
+ ___block_descriptor_tmp.221
+ ___block_descriptor_tmp.222
+ ___block_literal_global.159
+ ___block_literal_global.175
+ ___block_literal_global.178
+ ___block_literal_global.205
+ ___block_literal_global.218
+ ___block_literal_global.229
+ ___fbapspManager_flushFromTime_block_invoke.210
+ ___fbapspManager_flushFromTime_block_invoke.211
+ ___fbapspManager_flushFromTime_block_invoke.211.cold.1
+ ___fbapspManager_flushFromTime_block_invoke.211.cold.2
+ ___fbapspManager_flushFromTime_block_invoke.213
+ ___figHttpRequestSetupNSURLSessionTask_block_invoke_2
+ _fbapspManager_outputRequiresSubPipeChange
+ _figAudioQueueRenderPipelineStartAndUseTimebaseAtTransition.cold.2
+ _figSpeedRampRenderPipelineStartAndUseTimebaseAtTransition.cold.1
+ _figWarehouseRenderPipelineStartAndUseTimebaseAtTransition.cold.1
+ _itemoverlap_subItemNotificationWeakCallback.cold.2
+ _kFigBufferedAirPlaySubPipeManagerProperty_ContentStreamFormatDescription
+ _kFigBufferedAirPlaySubPipeManagerProperty_RecommendedTransportFormatDescription
+ _kFigBufferedAirPlaySubPipeManagerSbufAttachment_OriginalSbufOPTS
+ _kFigReportingEventKey_MusicItemReportingID
+ _kVTDecompressionPropertyKey_RequestedMVAV1SpatialIDs
- _OUTLINED_FUNCTION_861
- ___block_descriptor_tmp.174
- ___block_descriptor_tmp.177
- ___block_descriptor_tmp.210
- ___block_descriptor_tmp.211
- ___block_literal_global.172
- ___block_literal_global.202
- ___block_literal_global.215
- ___block_literal_global.226
- ___fbapspManager_flushFromTime_block_invoke.201
- ___fbapspManager_flushFromTime_block_invoke.202
- ___fbapspManager_flushFromTime_block_invoke.202.cold.1
- ___fbapspManager_flushFromTime_block_invoke.202.cold.2
- ___fbapspManager_flushFromTime_block_invoke.204
- _kFigBufferedAirPlaySubPipeManagerSbufAttachment_Retimed
CStrings:
+ "<<<< FAQ >>>> %s: [%p:%p:%p] %{public}s AudioQueue has started"
+ "<<<< FAQ >>>> %s: [%p:%p:%p] %{public}s AudioQueue has stopped"
+ "<<<< FAQ >>>> %s: [%p] AudioQueue signaled 'IsRunning' change."
+ "<<<< FAQRP >>>> %s: (%p %{public}s) cancelling transition %{public}@ callback because the refcon object was finalized"
+ "<<<< FigBufferedAirPlayOutput >>>> %s: [%p] %{public}s Resuming AudioEngine and EndpointStream result err = %d"
+ "<<<< FigBufferedAirPlayOutput >>>> %s: [%p] %{public}s inBufferedAirPlayOutput. isActive=%s, rate=%f, inMediaTime=%f, setConnectionActiveErr=%d"
+ "<<<< FigBufferedAirPlayOutput >>>> %s: [%p] %{public}s inBufferedAirPlayOutput. setConnectionActive failed."
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s Recommend SubPipeManager [%p] to use transport format %@"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s Using intro transport format for outro"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s Using outro transport format for intro "
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s failed retrieve contentStreamFormatDesc for SubPipeManager [%p] - err=%d"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s failed to handleDifferentMultiChannelLayoutForMixing SubPipeManager [%p] for MixEventID %@"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s failed to prepare SubPipeManager [%p] for MixEventID %@ err=%d"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s failed to start SubPipeManager [%p] for MixEventID %@ err=%d"
+ "<<<< FigBufferedAirPlayRP >>>> %s: [%p] %{public}s cancelling transition %{public}@ callback because the refcon object was finalized"
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Source format change detected! Clearing recommended Transport format to allow pipe rebuild!"
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s contentFormatASBD(transportFormatASBD). mSampleRate=%f(%f), mChannelsPerFrame=%u(%u), mBytesPerPacket=%u(%u), mFramesPerPacket=%u(%u), mBytesPerFrame=%u(%u), mBitsPerChannel=%u(%u), mFormatFlags=0x%x(0x%x) mFormatID=%c%c%c%c(%c%c%c%c) outputRequiresSubPipeChange=%d using recommendedTransportFormatDesc=%d\n"
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s decodeForPrerollRate:%1.3f, currentPipelineRate:%1.3f. currentState:%s  CANNOT set new rate since its not in Stopped state."
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s new decodeForPrerollRate=%1.3f "
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: No one is waiting for track %d, skipping playResourceReleased notification (nextTrackIsWaitingForResource=%s)"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s]: enableSpeedRamp"
+ "<<<< SpeedRamp RP >>>> %s: %{public}s (%p) cancelling transition %{public}@ callback because the refcon object was finalized"
+ "<<<< Warehouse RP >>>> %s: %{public}s (%p) cancelling transition %{public}@ callback because the refcon object was finalized"
+ "ContentStreamFormatDescription"
+ "OriginalSbufOPTS"
+ "RecommendedTransportFormatDescription"
+ "Stopped"
+ "TransitionCallbackRefconHolder"
+ "UseQoSUserInitiatedForNSURLSessionTaskResume"
+ "fbapop_handleDifferentMultiChannelLayoutForMixing"
+ "fbapspManager_findSubPipeTypeForSbuf"
+ "fbapspManager_setDecodeForPrerollRateRateIfNeeded"
+ "msc_ID"
+ "speedramp_timebaseTransitionCommitted"
+ "warehouse_timebaseTransitionCommitted"
- "<<<< FAQ >>>> %s: [%p:%p] %{public}s AudioQueue has started"
- "<<<< FAQ >>>> %s: [%p:%p] %{public}s AudioQueue has stopped"
- "<<<< FigBufferedAirPlayOutput >>>> %s: [%p] %{public}s Resuming AudioEngine and EndpointStream failed with err = %d"
- "<<<< FigBufferedAirPlayOutput >>>> %s: [%p] %{public}s inBufferedAirPlayOutput. isActive=%s, rate=%f, inMediaTime=%f"
- "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s failed to prepare SubPipeManager [%p] for MixEventID %@"
- "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s failed to start SubPipeManager [%p] for MixEventID %@"
- "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s contentFormatASBD(transportFormatASBD). mSampleRate=%f(%f), mChannelsPerFrame=%u(%u), mBytesPerPacket=%u(%u), mFramesPerPacket=%u(%u), mBytesPerFrame=%u(%u), mBitsPerChannel=%u(%u), mFormatFlags=0x%x(0x%x) mFormatID=%c%c%c%c(%c%c%c%c) outputRequiresSubPipeChange=%d\n"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: No one is waiting for track %d, skipping playResourceReleased notification"
- "Retimed"
- "TransitionCallbackRefcon"

```
