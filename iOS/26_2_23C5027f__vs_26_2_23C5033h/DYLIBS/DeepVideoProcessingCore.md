## DeepVideoProcessingCore

> `/System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore`

```diff

 2.9.0.0.0
-  __TEXT.__text: 0x711e0
+  __TEXT.__text: 0x711dc
   __TEXT.__auth_stubs: 0xf20
   __TEXT.__objc_methlist: 0x5094
   __TEXT.__const: 0x6b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00796D94-4D7E-3762-9363-C457CF164266
-  Functions: 2472
-  Symbols:   8415
+  UUID: EEC1B650-89EB-38CE-AF55-E86A2CC39799
+  Functions: 2473
+  Symbols:   8421
   CStrings:  4657
 
Functions:
~ _OUTLINED_FUNCTION_1 : 16 -> 40
~ _OUTLINED_FUNCTION_2 : 40 -> 12
+ _OUTLINED_FUNCTION_3
~ +[DVPLensFlareMitigationParameters getMotionShiftFromOpticalCenters:opticalCenterArrayLen:opticalCenterMotionShifts:] : 228 -> 268
~ -[ImageProcessor_Ext getPixelAttributesForBuffer:] : 368 -> 356
~ -[ImageProcessor_Ext allocateRGBABuffersForBuffer:] : 388 -> 376
~ -[Synthesis_Ext allocateSynthesisResources:Resolution:lowresRender:] : 788 -> 784
~ _adjustColorAndSpatialKey : 152 -> 148
~ -[SRNet getOutputPortNames] : 256 -> 276
~ -[VSRNet getInputPortNames] : 396 -> 416
~ -[ISRNet getInputPortNames] : 292 -> 312
~ -[VDGDetectionUtilsV2 generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:].cold.1 : 100 -> 92
~ -[VDGDetectionUtilsV2 generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:].cold.2 : 100 -> 92
~ -[VDGDetectionUtilsV2 updateDoGAndLumaFeaturesWithMetalBuffers:].cold.1 : 100 -> 92
~ -[VDGDetectionUtilsV2 updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:].cold.1 : 104 -> 100
~ -[VDGDetectionUtilsV2 updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:].cold.2 : 104 -> 100
~ -[GGMMetalToolBox initWithMetalContext:commandQueue:] : 820 -> 812
~ -[GGMMetalToolBox generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:] : 1132 -> 1128
~ -[GGMMetalToolBox initWithMetalContext:commandQueue:tuningParamDict:].cold.1 : 120 -> 112
~ _isMemoryAvailableForVSA : 88 -> 84
~ _isMemoryAvailableForFRC : 88 -> 84
~ _isMemoryAvailableForVSR : 200 -> 196
~ _isMemoryAvailableForISR : 180 -> 176
~ _writeBufferFlt32 : 292 -> 280

```
