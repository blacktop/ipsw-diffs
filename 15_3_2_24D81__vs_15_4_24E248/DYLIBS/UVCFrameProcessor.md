## UVCFrameProcessor

> `/System/Library/PrivateFrameworks/UVCFrameProcessor.framework/Versions/A/UVCFrameProcessor`

```diff

 466.80.2.0.0
-  __TEXT.__text: 0x8e18
+  __TEXT.__text: 0x8c4c
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_methlist: 0x3dc
   __TEXT.__const: 0xa0
   __TEXT.__oslogstring: 0xfa7
   __TEXT.__cstring: 0x4db
-  __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__gcc_except_tab: 0xa0
+  __TEXT.__unwind_info: 0x200
   __TEXT.__objc_classname: 0xda
   __TEXT.__objc_methname: 0xc97
   __TEXT.__objc_methtype: 0x632

   - /System/Library/PrivateFrameworks/UVCFamily.framework/Versions/A/UVCFamily
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBD33E8D-D8D1-3EC6-90F0-AA5190A8CF76
-  Functions: 147
-  Symbols:   461
+  UUID: 060AC254-D730-3EFC-8DBB-325C9B25574E
+  Functions: 152
+  Symbols:   464
   CStrings:  367
 
Symbols:
+ -[UVCFrameProcessorBase sendProcessedFrameToRender:handler:].cold.4
+ -[UVCFrameProcessorBase sendProcessedFrameToRender:handler:].cold.5
+ -[UVCFrameProcessorH264Decode _createSEIAttachmentPayloadFromBytePtr:dataSize:].cold.3
+ -[UVCNativeFrame appendDataToBlockBuffer:bytesPerRowAllignment:error:].cold.2
+ GCC_except_table22
+ UVCFrameProcessorLog.cold.1
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
- -[UVCFrameProcessorH264Decode setupDecompressionSession:error:handler:].cold.1
- -[UVCFrameProcessorH264Decode setupDecompressionSession:error:handler:].cold.2
- -[UVCFrameProcessorMJPEGDecode setupDecompressionSession:error:handler:].cold.1
- -[UVCFrameProcessorMJPEGDecode setupDecompressionSession:error:handler:].cold.2
- -[UVCFrameProcessorNative dispatchPreviousFrame].cold.1
- -[UVCFrameProcessorNative initWithStreamFormat:pixelFormat:colorAttributes:source:handler:].cold.1
- -[UVCFrameProcessorRotate handleStreamData:handler:].cold.1
- -[UVCFrameProcessorRotate setupRotationSession:].cold.1
- -[UVCFrameProcessorRotate setupRotationSession:].cold.2
- -[UVCNativeFrame initWithBuffer:presentationTimestamp:presentationDuration:discontinous:captureTimeInHostClock:].cold.1
- createPixelBufferPool.cold.1
- createRenderReadySampleBuffer.cold.1

```
