## BarcodeScanner.videoprocessor

> `/System/Library/VideoProcessors/BarcodeScanner.videoprocessor`

```diff

-587.81.10.0.0
-  __TEXT.__text: 0x5464
+587.101.4.0.0
+  __TEXT.__text: 0x57d4
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x31e
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x31c
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__got: 0x260
   __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0xa0

   - /System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture
   - /System/Library/PrivateFrameworks/Quagga.framework/Versions/A/Quagga
   - /usr/lib/libSystem.B.dylib
-  UUID: 3C505DBD-DBAD-3F5D-8FC6-F7A359C85C0D
-  Functions: 19
-  Symbols:   222
+  UUID: 72C1E3C8-1BC7-370C-816A-D48EE2705652
+  Functions: 49
+  Symbols:   252
   CStrings:  38
 
Symbols:
+ FigDraw420Line.cold.1
+ FigDrawLumaRectangle.cold.1
+ FigSampleBufferProcessorCreateForBarcodeScanner.cold.1
+ FigSampleBufferProcessorCreateForBarcodeScanner.cold.2
+ FigSampleBufferProcessorCreateForBarcodeScanner.cold.3
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _sbp_bcs_updateBarcodeLocations
+ detectBarcodesInFrame.cold.1
+ ensurePyramidArray.cold.1
+ sbp_bcs_processSampleBuffer.cold.1
+ sbp_bcs_processSampleBuffer.cold.10
+ sbp_bcs_processSampleBuffer.cold.11
+ sbp_bcs_processSampleBuffer.cold.12
+ sbp_bcs_processSampleBuffer.cold.2
+ sbp_bcs_processSampleBuffer.cold.3
+ sbp_bcs_processSampleBuffer.cold.4
+ sbp_bcs_processSampleBuffer.cold.5
+ sbp_bcs_processSampleBuffer.cold.6
+ sbp_bcs_processSampleBuffer.cold.7
+ sbp_bcs_processSampleBuffer.cold.8
+ sbp_bcs_processSampleBuffer.cold.9
+ sbp_bcs_updateBarcodeLocations.cold.1
CStrings:
+ "!( ((void*)0) == pixelBuffer || x1 < 0 || y1 < 0 || x1 >= width || y1 >= height || x2 < 0 || y2 < 0 || x2 >= width || y2 >= height )"
+ "!( ((void*)0) == pixelBuffer || xStart < 0 || yStart < 0 || xStart >= width || yStart >= height || xSize < 1 || ySize < 1 )"
- "!( ((void *)0) == pixelBuffer || x1 < 0 || y1 < 0 || x1 >= width || y1 >= height || x2 < 0 || y2 < 0 || x2 >= width || y2 >= height )"
- "!( ((void *)0) == pixelBuffer || xStart < 0 || yStart < 0 || xStart >= width || yStart >= height || xSize < 1 || ySize < 1 )"

```
