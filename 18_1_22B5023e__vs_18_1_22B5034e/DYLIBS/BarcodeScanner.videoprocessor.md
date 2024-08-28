## BarcodeScanner.videoprocessor

> `/System/Library/VideoProcessors/BarcodeScanner.videoprocessor`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0x5564
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x31e
-  __TEXT.__unwind_info: 0xb8
+580.2.0.0.0
+  __TEXT.__text: 0x919c
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x89a
+  __TEXT.__oslogstring: 0x1117
+  __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__got: 0x270
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__cfstring: 0x120
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/Quagga.framework/Quagga
   - /usr/lib/libSystem.B.dylib
   Functions: 20
-  Symbols:   224
-  CStrings:  31
+  Symbols:   231
+  CStrings:  141
 
Symbols:
+ _FigHostTimeToNanoseconds
+ _FigGetUpTime
+ _os_log_type_enabled
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ __os_log_send_and_compose_impl
+ _fig_note_initialize_category_with_default_work_cf
+ _CMTimeGetSeconds
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _FigSignalErrorAt3
- _fig_log_get_emitter
- _FigSignalErrorAt
CStrings:
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Aged out barcode %!f(MISSING)ms old"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): mrcDecoder and/or mrcSample is NULL, not sending buffer to detector "
+ "<<<< BarcodeScanner >>>> %!s(MISSING): no pixelbuffer and/or err=%!d(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING):  Found barcode:\n[barcode data at frame %!d(MISSING)] type: %!@(MISSING), contents: %!@(MISSING)"
+ "Buffer must be 420v/y420, a multiple of 16 pixels, and have no padding"
+ "sbp_bcs_setOutputCallback"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Scanning for all symbologies"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): priority already assigned"
+ "sbp_bcs_copyDebugDescription"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Priority of new code is too low to replace anything else."
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Preparing"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Sample buffer missing kFigCaptureSampleBufferAttachmentKey_OriginalPresentationTimeStamp, using post-audio-CMSync timestamp instead"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Setting LowPowerModeEnabled to %!@(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): found next lowest priority (%!f(MISSING), at idx=%!d(MISSING))"
+ "ensurePyramidArray"
+ "<<<< BarcodeScanner >>>>"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): PixelSum offset: %!f(MISSING), %!f(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): mrcDecodedResult is NULL (error %!@(MISSING)), not sending buffer to detector"
+ "NULL outProcessor"
+ "com.apple.coremedia"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Generating image pyramid took %!f(MISSING)ms"
+ "kFigBaseObjectError_ParamErr"
+ "sbp_bcs_purgeResources"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): %!s(MISSING) calling detector (frame %!d(MISSING))\n"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Scanning for %!s(MISSING)"
+ "FigDraw420Line"
+ "kFigBaseObjectError_Invalidated"
+ "parseArgs"
+ "sbp_bcs_processPixelSum"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Assigned new priority; %!f(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Setting 1D scan lines to baseline"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): for [incoming mrc %!d(MISSING)], distance match found (%!d(MISSING)). distance = %!f(MISSING), (%!f(MISSING) of width)"
+ "FigSampleBufferProcessorCreateForBarcodeScanner"
+ "sbp_bcs_dispatchBarcodeDetector"
+ "sbp_bcs_updateStabilityStatistics"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): %!d(MISSING) barcodes found"
+ "Buffer is y420/f420 and bytesPerRow does not meet requirement"
+ "Error with sbp_setupPixelBufferPool"
+ "NULL propertyValueOut"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): no key-value pair with a matching key of MRCDecoderOptionSymbologies exists in storage->mrcOptionValues"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Setting 1D scan lines to max"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Invalid parameter"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Found barcode, but could not decode"
+ "sbp_bcs_drawBarcodeOutline"
+ "sbp_bcs_finishPendingProcessing"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): looping over priorities to see if anything was not matched: %!f(MISSING) at idx=%!d(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Using pixelFormat: %!s(MISSING)\n"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): for [incoming mrc %!d(MISSING)], no existing match found, looking for empty entry"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): for [incoming mrc %!d(MISSING)], total match found (%!d(MISSING)). distance = %!f(MISSING), (%!f(MISSING) of width)"
+ "Buffer is not 420v/f or y420/f"
+ "err"
+ "invalidated"
+ "kFigBaseObjectError_PropertyNotFound"
+ "synchronously"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): image pyramid buffers are re-usable"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Using capture buffer!"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): stability detector: unstable"
+ "not a CFDictionary"
+ "not a valid CGRect-based CFDictionary"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Resetting"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Setting symbologies to search for: Symbology %!d(MISSING): %!@(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): image pyramid computation failed (%!d(MISSING))"
+ "sbp_bcs_getInputPixelBuffer"
+ "sbp_bcs_setProperty"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Barcode detector finished. Adding accumulated offset of %!f(MISSING), %!f(MISSING) (since detector started)\n"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): frame %!d(MISSING) - Previous call to detector not done yet, not calling detector again."
+ "<<<< BarcodeScanner >>>> %!s(MISSING): image pyramid buffers are not re-usable"
+ "sbp_bcs_copyProperty"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): No metadata dictionary attached. Processing will not match real-time results."
+ "<<<< BarcodeScanner >>>> %!s(MISSING): drawing barcode ID %!d(MISSING)\n"
+ "Buffer is 420v/420f and bytesPerRow does not meet requirement"
+ "sbp_bcs_outputSampleBufferWithBarcodeMetadata"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Drawing debug debug info."
+ "(Fig)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): invalidated"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): stability detector: stable"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "sbp_bcs_updateBarcodeLocations"
+ "Invalid parameters"
+ "No metadata dictionary found, cannot process"
+ "clearBarcodes"
+ "not a CFArray"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): New code (pri=%!f(MISSING)) replaced old code %!d(MISSING) (pri=%!f(MISSING))."
+ "<<<< BarcodeScanner >>>> %!s(MISSING): new priority: %!f(MISSING), new ID: %!d(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Quagga detector (MRCDecoderDecodeSample) took %!f(MISSING)ms"
+ "computeImagePyramidVT"
+ "sbp_bcs_verifyInputBuffer"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Interest rect is empty, not sending buffer to detector"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): added image pyramid buffer (%!d(MISSING) x %!d(MISSING)) at index %!d(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): image pyramid allocation failed (%!d(MISSING))"
+ "not a CFBoolean"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): FigSampleBufferGetSampleTimingInfoArray failed (%!d(MISSING))"
+ "detectBarcodesInFrame"
+ "sbp_bcs_createMetadataDictWithBarcodeInfo"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Setting OutputSampleBufferWithoutImage to %!@(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): for [incoming mrc %!d(MISSING)], content match found (%!d(MISSING)). distance = %!f(MISSING), (%!f(MISSING) of width)"
+ "asynchronously"
+ "sbp_bcs_processSampleBuffer"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Invalid parameter: %!s(MISSING)\n"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): looking for match in existing code %!d(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): processing frame %!d(MISSING)\n"
+ "Buffer width not a multiple of 16"
+ "FigDrawLumaRectangle"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): clearBarcodes() is called before running detector on any frames, not updating lastTimeBarcodesCleared. Current value: %!f(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Using preview buffer!"
+ "mrc_trace"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): MRC confidence threshold: %!f(MISSING)"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): MRCDecoderDecodeSample returned error %!@(MISSING), not sending buffer to detector"
+ "<<<< BarcodeScanner >>>> %!s(MISSING): Missing barcode information, skipping"
+ "sbp_bcs_copyOutputPixelBuffer"

```
