## BarcodeScanner.videoprocessor

> `/System/Library/VideoProcessors/BarcodeScanner.videoprocessor`

```diff

-587.101.4.0.0
-  __TEXT.__text: 0x57d4
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x31c
-  __TEXT.__unwind_info: 0xe8
+587.120.2.0.1
+  __TEXT.__text: 0x93a0
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0x898
+  __TEXT.__oslogstring: 0x1117
+  __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__got: 0x260
-  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__cfstring: 0x120
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture
   - /System/Library/PrivateFrameworks/Quagga.framework/Versions/A/Quagga
   - /usr/lib/libSystem.B.dylib
-  Functions: 49
-  Symbols:   252
-  CStrings:  31
+  Functions: 43
+  Symbols:   254
+  CStrings:  141
 
Symbols:
+ _CMTimeGetSeconds
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ _FigSignalErrorAt3
+ _MRCTrace
+ _OUTLINED_FUNCTION_6
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_type_enabled
- _FigSignalErrorAt
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _fig_log_get_emitter
- _sbp_bcs_updateBarcodeLocations
- sbp_bcs_processSampleBuffer.cold.12
- sbp_bcs_updateBarcodeLocations.cold.1
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
+ "<<<< BarcodeScanner >>>>"
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
+ "kFigBaseObjectError_Invalidated"
+ "kFigBaseObjectError_ParamErr"
+ "kFigBaseObjectError_PropertyNotFound"
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

```
