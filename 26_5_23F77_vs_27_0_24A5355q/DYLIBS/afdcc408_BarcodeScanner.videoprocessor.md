## BarcodeScanner.videoprocessor

> `/System/Library/VideoProcessors/BarcodeScanner.videoprocessor`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0x575c sha256:5430806990e83459d1966e7b3aa0c7ba158eba8152db715175691222b6e0e7c3
-  __TEXT.__auth_stubs: 0x7c0 sha256:e6f629360ecdb153c9a376e90497247b515631e93f7bd46a7d4afb98189571d1
-  __TEXT.__const: 0x10 sha256:517c98cee942bcfff0726d52c217839bf943643c199605647be569330e31a3aa
-  __TEXT.__cstring: 0x358 sha256:01fdefc237d1ae7a83c08ed40f855e1f6d1cc4af7a3dc4863b6ab7716e0b1639
-  __TEXT.__unwind_info: 0xe8 sha256:30c7cf3111259c68771eca596ec3d087da5230be396c387f6e12cdc0c69db727
-  __DATA_CONST.__got: 0x268 sha256:f9d54bbe3ccaf08564c2928c55218a3f696989a05dffc8edf057773751aae153
-  __AUTH_CONST.__auth_got: 0x3e0 sha256:5f51d9e57c051cc516388346d860976bff3531da9561f6570c19b2ca2da48eab
-  __AUTH_CONST.__const: 0xa0 sha256:6b7bdeb18a00c9ee34b3f74407fc7a94a39e2c89af926d82694a816cb86d6902
-  __AUTH_CONST.__cfstring: 0xe0 sha256:d34c386c918f10ad1c2e3df2b7719d982c26d0a52747c76c950217f6623401ea
+748.0.0.122.2
+  __TEXT.__text: 0x8e20 sha256:3c72274f3bbf650db3df42ae25c7a25725651b3ae7992a563327ed687aad2a2d
+  __TEXT.__const: 0x40 sha256:ce0fce8a4a029e873a76cf0580797c243752821cda93fa719fb92b68dc788155
+  __TEXT.__cstring: 0x895 sha256:aef52ad4e8f4fc3bc8a63b99781f68f940bde362d4320aabc0b29c6d9e7fcffa
+  __TEXT.__oslogstring: 0x1117 sha256:bbf3875292d4c860756929ff092e34a751188248175b2f6404f5822826720cef
+  __TEXT.__unwind_info: 0xf8 sha256:71b5c7e20480adccad34d5fb08aa7bcd9e8c7f3d2773776c89ebc0ae046363d8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xa0 sha256:0d46daa276ee47b5ea912ee80cd276033b4d58c7a80c931a247bfd49ddfa89bb
+  __AUTH_CONST.__cfstring: 0x120 sha256:ba6d9cf2a13562f4ddeb863b71301278a1724915bdbdeda0745bc1a730c4fbff
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA_DIRTY.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/Quagga.framework/Quagga
   - /usr/lib/libSystem.B.dylib
-  UUID: 748B2A71-0347-3544-AF58-62DB9C36FB2F
-  Functions: 54
-  Symbols:   312
-  CStrings:  41
+  UUID: A3ACC69C-51F3-346F-8DB4-8C1979B8594E
+  Functions: 65
+  Symbols:   342
+  CStrings:  150
 
Symbols:
+ _CMTimeGetSeconds
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ _FigSignalErrorAt3
+ _MRCTrace
+ __os_log_send_and_compose_impl
+ _ensurePyramidArray.cold.2
+ _ensurePyramidArray.cold.3
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_type_enabled
+ _sbp_bcs_processSampleBuffer.cold.13
+ _sbp_bcs_processSampleBuffer.cold.14
+ _sbp_bcs_processSampleBuffer.cold.15
+ _sbp_bcs_setProperty.cold.1
+ _sbp_bcs_setProperty.cold.2
+ _sbp_bcs_setProperty.cold.3
+ _sbp_bcs_setProperty.cold.4
- _FigSignalErrorAtGM
- _fig_log_get_emitter
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "<<<< BarcodeScanner >>>> %s:  Found barcode:\n[barcode data at frame %d] type: %@, contents: %@"
+ "<<<< BarcodeScanner >>>> %s: %d barcodes found"
+ "<<<< BarcodeScanner >>>> %s: %s calling detector (frame %d)\n"
+ "<<<< BarcodeScanner >>>> %s: Aged out barcode %.0fms old"
+ "<<<< BarcodeScanner >>>> %s: Assigned new priority; %f"
+ "<<<< BarcodeScanner >>>> %s: Barcode detector finished. Adding accumulated offset of %f, %f (since detector started)\n"
+ "<<<< BarcodeScanner >>>> %s: Drawing debug debug info."
+ "<<<< BarcodeScanner >>>> %s: FigSampleBufferGetSampleTimingInfoArray failed (%d)"
+ "<<<< BarcodeScanner >>>> %s: Found barcode, but could not decode"
+ "<<<< BarcodeScanner >>>> %s: Generating image pyramid took %.1fms"
+ "<<<< BarcodeScanner >>>> %s: Interest rect is empty, not sending buffer to detector"
+ "<<<< BarcodeScanner >>>> %s: Invalid parameter"
+ "<<<< BarcodeScanner >>>> %s: Invalid parameter: %s\n"
+ "<<<< BarcodeScanner >>>> %s: MRC confidence threshold: %f"
+ "<<<< BarcodeScanner >>>> %s: MRCDecoderDecodeSample returned error %@, not sending buffer to detector"
+ "<<<< BarcodeScanner >>>> %s: Missing barcode information, skipping"
+ "<<<< BarcodeScanner >>>> %s: New code (pri=%f) replaced old code %d (pri=%f)."
+ "<<<< BarcodeScanner >>>> %s: No metadata dictionary attached. Processing will not match real-time results."
+ "<<<< BarcodeScanner >>>> %s: PixelSum offset: %f, %f"
+ "<<<< BarcodeScanner >>>> %s: Preparing"
+ "<<<< BarcodeScanner >>>> %s: Priority of new code is too low to replace anything else."
+ "<<<< BarcodeScanner >>>> %s: Quagga detector (MRCDecoderDecodeSample) took %.1fms"
+ "<<<< BarcodeScanner >>>> %s: Resetting"
+ "<<<< BarcodeScanner >>>> %s: Sample buffer missing kFigCaptureSampleBufferAttachmentKey_OriginalPresentationTimeStamp, using post-audio-CMSync timestamp instead"
+ "<<<< BarcodeScanner >>>> %s: Scanning for %s"
+ "<<<< BarcodeScanner >>>> %s: Scanning for all symbologies"
+ "<<<< BarcodeScanner >>>> %s: Setting 1D scan lines to baseline"
+ "<<<< BarcodeScanner >>>> %s: Setting 1D scan lines to max"
+ "<<<< BarcodeScanner >>>> %s: Setting LowPowerModeEnabled to %@"
+ "<<<< BarcodeScanner >>>> %s: Setting OutputSampleBufferWithoutImage to %@"
+ "<<<< BarcodeScanner >>>> %s: Setting symbologies to search for: Symbology %d: %@"
+ "<<<< BarcodeScanner >>>> %s: Using capture buffer!"
+ "<<<< BarcodeScanner >>>> %s: Using pixelFormat: %s\n"
+ "<<<< BarcodeScanner >>>> %s: Using preview buffer!"
+ "<<<< BarcodeScanner >>>> %s: added image pyramid buffer (%d x %d) at index %d"
+ "<<<< BarcodeScanner >>>> %s: clearBarcodes() is called before running detector on any frames, not updating lastTimeBarcodesCleared. Current value: %.3f"
+ "<<<< BarcodeScanner >>>> %s: drawing barcode ID %d\n"
+ "<<<< BarcodeScanner >>>> %s: for [incoming mrc %d], content match found (%d). distance = %f, (%f of width)"
+ "<<<< BarcodeScanner >>>> %s: for [incoming mrc %d], distance match found (%d). distance = %f, (%f of width)"
+ "<<<< BarcodeScanner >>>> %s: for [incoming mrc %d], no existing match found, looking for empty entry"
+ "<<<< BarcodeScanner >>>> %s: for [incoming mrc %d], total match found (%d). distance = %f, (%f of width)"
+ "<<<< BarcodeScanner >>>> %s: found next lowest priority (%f, at idx=%d)"
+ "<<<< BarcodeScanner >>>> %s: frame %d - Previous call to detector not done yet, not calling detector again."
+ "<<<< BarcodeScanner >>>> %s: image pyramid allocation failed (%d)"
+ "<<<< BarcodeScanner >>>> %s: image pyramid buffers are not re-usable"
+ "<<<< BarcodeScanner >>>> %s: image pyramid buffers are re-usable"
+ "<<<< BarcodeScanner >>>> %s: image pyramid computation failed (%d)"
+ "<<<< BarcodeScanner >>>> %s: invalidated"
+ "<<<< BarcodeScanner >>>> %s: looking for match in existing code %d"
+ "<<<< BarcodeScanner >>>> %s: looping over priorities to see if anything was not matched: %f at idx=%d"
+ "<<<< BarcodeScanner >>>> %s: mrcDecodedResult is NULL (error %@), not sending buffer to detector"
+ "<<<< BarcodeScanner >>>> %s: mrcDecoder and/or mrcSample is NULL, not sending buffer to detector "
+ "<<<< BarcodeScanner >>>> %s: new priority: %f, new ID: %d"
+ "<<<< BarcodeScanner >>>> %s: no key-value pair with a matching key of MRCDecoderOptionSymbologies exists in storage->mrcOptionValues"
+ "<<<< BarcodeScanner >>>> %s: no pixelbuffer and/or err=%d"
+ "<<<< BarcodeScanner >>>> %s: priority already assigned"
+ "<<<< BarcodeScanner >>>> %s: processing frame %d\n"
+ "<<<< BarcodeScanner >>>> %s: stability detector: stable"
+ "<<<< BarcodeScanner >>>> %s: stability detector: unstable"
+ "Buffer is 420v/420f and bytesPerRow does not meet requirement"
+ "Buffer is not 420v/f or y420/f"
+ "Buffer is y420/f420 and bytesPerRow does not meet requirement"
+ "Buffer must be 420v/y420, a multiple of 16 pixels, and have no padding"
+ "Buffer width not a multiple of 16"
+ "Error with sbp_setupPixelBufferPool"
+ "FigDraw420Line"
+ "FigDrawLumaRectangle"
+ "FigSampleBufferProcessorCreateForBarcodeScanner"
+ "Invalid parameters"
+ "NULL outProcessor"
+ "NULL propertyValueOut"
+ "No metadata dictionary found, cannot process"
+ "asynchronously"
+ "clearBarcodes"
+ "com.apple.coremedia"
+ "computeImagePyramidVT"
+ "detectBarcodesInFrame"
+ "ensurePyramidArray"
+ "err"
+ "invalidated"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_PropertyNotFound"
+ "mrc_trace"
+ "not a CFArray"
+ "not a CFBoolean"
+ "not a CFDictionary"
+ "not a valid CGRect-based CFDictionary"
+ "parseArgs"
+ "sbp_bcs_copyDebugDescription"
+ "sbp_bcs_copyOutputPixelBuffer"
+ "sbp_bcs_copyProperty"
+ "sbp_bcs_createMetadataDictWithBarcodeInfo"
+ "sbp_bcs_dispatchBarcodeDetector"
+ "sbp_bcs_drawBarcodeOutline"
+ "sbp_bcs_finishPendingProcessing"
+ "sbp_bcs_getInputPixelBuffer"
+ "sbp_bcs_outputSampleBufferWithBarcodeMetadata"
+ "sbp_bcs_processPixelSum"
+ "sbp_bcs_processSampleBuffer"
+ "sbp_bcs_purgeResources"
+ "sbp_bcs_setOutputCallback"
+ "sbp_bcs_setProperty"
+ "sbp_bcs_updateBarcodeLocations"
+ "sbp_bcs_updateStabilityStatistics"
+ "sbp_bcs_verifyInputBuffer"
+ "synchronously"
- "%s signalled err=%d at <>:%d"

```
