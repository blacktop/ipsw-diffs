## BarcodeScanner.videoprocessor

> `/System/Library/VideoProcessors/BarcodeScanner.videoprocessor`

```diff

-570.4.21.0.0
-  __TEXT.__text: 0x919c
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x89a
-  __TEXT.__oslogstring: 0x1117
-  __TEXT.__unwind_info: 0xc0
+575.9.1.0.0
+  __TEXT.__text: 0x5564
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x31e
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x270
-  __AUTH_CONST.__auth_got: 0x420
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x120
-  __DATA_DIRTY.__common: 0x10
+  __AUTH_CONST.__cfstring: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/Quagga.framework/Quagga
   - /usr/lib/libSystem.B.dylib
   Functions: 20
-  Symbols:   231
-  CStrings:  141
+  Symbols:   224
+  CStrings:  31
 
Symbols:
+ _FigSignalErrorAt
+ _fig_log_get_emitter
- _CMTimeGetSeconds
- _FigGetUpTime
- _FigHostTimeToNanoseconds
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work_cf
- _os_log_type_enabled
CStrings:
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "(Fig)"
- "<<<< BarcodeScanner >>>>"
- "<<<< BarcodeScanner >>>> %!s(MISSING):  Found barcode:\n[barcode data at frame %!d(MISSING)] type: %!@(MISSING), contents: %!@(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): %!d(MISSING) barcodes found"
- "<<<< BarcodeScanner >>>> %!s(MISSING): %!s(MISSING) calling detector (frame %!d(MISSING))\n"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Aged out barcode %!f(MISSING)ms old"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Assigned new priority; %!f(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Barcode detector finished. Adding accumulated offset of %!f(MISSING), %!f(MISSING) (since detector started)\n"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Drawing debug debug info."
- "<<<< BarcodeScanner >>>> %!s(MISSING): FigSampleBufferGetSampleTimingInfoArray failed (%!d(MISSING))"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Found barcode, but could not decode"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Generating image pyramid took %!f(MISSING)ms"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Interest rect is empty, not sending buffer to detector"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Invalid parameter"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Invalid parameter: %!s(MISSING)\n"
- "<<<< BarcodeScanner >>>> %!s(MISSING): MRC confidence threshold: %!f(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): MRCDecoderDecodeSample returned error %!@(MISSING), not sending buffer to detector"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Missing barcode information, skipping"
- "<<<< BarcodeScanner >>>> %!s(MISSING): New code (pri=%!f(MISSING)) replaced old code %!d(MISSING) (pri=%!f(MISSING))."
- "<<<< BarcodeScanner >>>> %!s(MISSING): No metadata dictionary attached. Processing will not match real-time results."
- "<<<< BarcodeScanner >>>> %!s(MISSING): PixelSum offset: %!f(MISSING), %!f(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Preparing"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Priority of new code is too low to replace anything else."
- "<<<< BarcodeScanner >>>> %!s(MISSING): Quagga detector (MRCDecoderDecodeSample) took %!f(MISSING)ms"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Resetting"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Sample buffer missing kFigCaptureSampleBufferAttachmentKey_OriginalPresentationTimeStamp, using post-audio-CMSync timestamp instead"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Scanning for %!s(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Scanning for all symbologies"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Setting 1D scan lines to baseline"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Setting 1D scan lines to max"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Setting LowPowerModeEnabled to %!@(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Setting OutputSampleBufferWithoutImage to %!@(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Setting symbologies to search for: Symbology %!d(MISSING): %!@(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Using capture buffer!"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Using pixelFormat: %!s(MISSING)\n"
- "<<<< BarcodeScanner >>>> %!s(MISSING): Using preview buffer!"
- "<<<< BarcodeScanner >>>> %!s(MISSING): added image pyramid buffer (%!d(MISSING) x %!d(MISSING)) at index %!d(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): clearBarcodes() is called before running detector on any frames, not updating lastTimeBarcodesCleared. Current value: %!f(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): drawing barcode ID %!d(MISSING)\n"
- "<<<< BarcodeScanner >>>> %!s(MISSING): for [incoming mrc %!d(MISSING)], content match found (%!d(MISSING)). distance = %!f(MISSING), (%!f(MISSING) of width)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): for [incoming mrc %!d(MISSING)], distance match found (%!d(MISSING)). distance = %!f(MISSING), (%!f(MISSING) of width)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): for [incoming mrc %!d(MISSING)], no existing match found, looking for empty entry"
- "<<<< BarcodeScanner >>>> %!s(MISSING): for [incoming mrc %!d(MISSING)], total match found (%!d(MISSING)). distance = %!f(MISSING), (%!f(MISSING) of width)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): found next lowest priority (%!f(MISSING), at idx=%!d(MISSING))"
- "<<<< BarcodeScanner >>>> %!s(MISSING): frame %!d(MISSING) - Previous call to detector not done yet, not calling detector again."
- "<<<< BarcodeScanner >>>> %!s(MISSING): image pyramid allocation failed (%!d(MISSING))"
- "<<<< BarcodeScanner >>>> %!s(MISSING): image pyramid buffers are not re-usable"
- "<<<< BarcodeScanner >>>> %!s(MISSING): image pyramid buffers are re-usable"
- "<<<< BarcodeScanner >>>> %!s(MISSING): image pyramid computation failed (%!d(MISSING))"
- "<<<< BarcodeScanner >>>> %!s(MISSING): invalidated"
- "<<<< BarcodeScanner >>>> %!s(MISSING): looking for match in existing code %!d(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): looping over priorities to see if anything was not matched: %!f(MISSING) at idx=%!d(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): mrcDecodedResult is NULL (error %!@(MISSING)), not sending buffer to detector"
- "<<<< BarcodeScanner >>>> %!s(MISSING): mrcDecoder and/or mrcSample is NULL, not sending buffer to detector "
- "<<<< BarcodeScanner >>>> %!s(MISSING): new priority: %!f(MISSING), new ID: %!d(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): no key-value pair with a matching key of MRCDecoderOptionSymbologies exists in storage->mrcOptionValues"
- "<<<< BarcodeScanner >>>> %!s(MISSING): no pixelbuffer and/or err=%!d(MISSING)"
- "<<<< BarcodeScanner >>>> %!s(MISSING): priority already assigned"
- "<<<< BarcodeScanner >>>> %!s(MISSING): processing frame %!d(MISSING)\n"
- "<<<< BarcodeScanner >>>> %!s(MISSING): stability detector: stable"
- "<<<< BarcodeScanner >>>> %!s(MISSING): stability detector: unstable"
- "Buffer is 420v/420f and bytesPerRow does not meet requirement"
- "Buffer is not 420v/f or y420/f"
- "Buffer is y420/f420 and bytesPerRow does not meet requirement"
- "Buffer must be 420v/y420, a multiple of 16 pixels, and have no padding"
- "Buffer width not a multiple of 16"
- "Error with sbp_setupPixelBufferPool"
- "FigDraw420Line"
- "FigDrawLumaRectangle"
- "FigSampleBufferProcessorCreateForBarcodeScanner"
- "Invalid parameters"
- "NULL outProcessor"
- "NULL propertyValueOut"
- "No metadata dictionary found, cannot process"
- "asynchronously"
- "clearBarcodes"
- "com.apple.coremedia"
- "computeImagePyramidVT"
- "detectBarcodesInFrame"
- "ensurePyramidArray"
- "err"
- "invalidated"
- "kFigBaseObjectError_Invalidated"
- "kFigBaseObjectError_ParamErr"
- "kFigBaseObjectError_PropertyNotFound"
- "mrc_trace"
- "not a CFArray"
- "not a CFBoolean"
- "not a CFDictionary"
- "not a valid CGRect-based CFDictionary"
- "parseArgs"
- "sbp_bcs_copyDebugDescription"
- "sbp_bcs_copyOutputPixelBuffer"
- "sbp_bcs_copyProperty"
- "sbp_bcs_createMetadataDictWithBarcodeInfo"
- "sbp_bcs_dispatchBarcodeDetector"
- "sbp_bcs_drawBarcodeOutline"
- "sbp_bcs_finishPendingProcessing"
- "sbp_bcs_getInputPixelBuffer"
- "sbp_bcs_outputSampleBufferWithBarcodeMetadata"
- "sbp_bcs_processPixelSum"
- "sbp_bcs_processSampleBuffer"
- "sbp_bcs_purgeResources"
- "sbp_bcs_setOutputCallback"
- "sbp_bcs_setProperty"
- "sbp_bcs_updateBarcodeLocations"
- "sbp_bcs_updateStabilityStatistics"
- "sbp_bcs_verifyInputBuffer"
- "synchronously"

```
