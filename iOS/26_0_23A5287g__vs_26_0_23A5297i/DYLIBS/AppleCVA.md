## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`

```diff

-1002.5.0.0.0
-  __TEXT.__text: 0xb3f7c
-  __TEXT.__auth_stubs: 0x1a60
+1002.6.0.0.0
+  __TEXT.__text: 0xb5674
+  __TEXT.__auth_stubs: 0x1a70
   __TEXT.__objc_methlist: 0xb4
-  __TEXT.__const: 0x929
-  __TEXT.__gcc_except_tab: 0x4938
-  __TEXT.__cstring: 0x5a75
-  __TEXT.__oslogstring: 0x8f2d
-  __TEXT.__unwind_info: 0x1310
+  __TEXT.__const: 0x959
+  __TEXT.__gcc_except_tab: 0x4994
+  __TEXT.__cstring: 0x5a3e
+  __TEXT.__oslogstring: 0x9362
+  __TEXT.__unwind_info: 0x1320
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methname: 0xd69
   __TEXT.__objc_methtype: 0x1e6

   __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xd40
-  __AUTH_CONST.__const: 0x1f20
-  __AUTH_CONST.__cfstring: 0x3980
+  __AUTH_CONST.__auth_got: 0xd48
+  __AUTH_CONST.__const: 0x1f58
+  __AUTH_CONST.__cfstring: 0x3960
   __AUTH_CONST.__objc_const: 0x348
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9F783C0-D89F-3E7F-ACDD-7544BC9624EE
-  Functions: 1174
-  Symbols:   968
-  CStrings:  2331
+  UUID: 09C93E1B-798D-3B9C-AB7F-199667071F64
+  Functions: 1181
+  Symbols:   967
+  CStrings:  2346
 
Symbols:
+ __os_log_fault_impl
- _CVAFaceTrackingLiteCopyDecodedOutput
- _CVAFaceTrackingLiteGetOutput
CStrings:
+ "Assertion failed: cbCrTexture"
+ "Assertion failed: debugDictionary"
+ "Assertion failed: device"
+ "Assertion failed: m_debugRenderer"
+ "Assertion failed: m_debugRendererCbCr"
+ "Assertion failed: m_debugRendererY"
+ "Assertion failed: queue"
+ "Assertion failed: state"
+ "Assertion failed: state->commandBuffer"
+ "Assertion failed: state.commandBuffer"
+ "Assertion failed: state.textureCbCr"
+ "Assertion failed: state.textureY"
+ "Assertion failed: yTexture"
+ "CVAFaceTrackingLiteProcessSecondary has not been called."
+ "FaceKitStatistics: ok %u; ML %u (%u); outside %u (%u); close %u; far %u; non-frontal %u; velocity %u/%u; acceleration %u/%u; fittable %u; faceprintable %u"
+ "FaceKitStatistics: total: %u; deltas: %u (color/depth: %u/%u); dropped: %u; face detections (0/1/2/3+): %u/%u/%u/%u; selected faces (0/1/2/3): %u/%u/%u/%u"
+ "Failed to prepare debug renderer."
+ "Failed to setup debug renderer"
+ "Running encode(lineStripFromPoints(boxCorners), debugrenderer::PrimitiveTypeLineStrip, kInputFaceYuv, state) failed with %s, returning %s"
+ "Running encode(lineStripFromPoints(leftEye.cropCorners()), debugrenderer::PrimitiveTypeLineStrip, yuv, state) failed with %s, returning %s"
+ "Running encode(lineStripFromPoints(rightEye.cropCorners()), debugrenderer::PrimitiveTypeLineStrip, yuv, state) failed with %s, returning %s"
+ "Running encode(rollAngleLine, debugrenderer::PrimitiveTypeLineStrip, kInputFaceYuv, state) failed with %s, returning %s"
+ "Running m_debugRenderer->commitAndWait(std::move(debugRendererState)) failed with %s, returning %s"
+ "Running m_debugRenderer->encode(data.inputFaceDetections(), *debugRendererState) failed with %s, returning %s"
+ "Running m_debugRenderer->encode(normalizedLandmarksToImage(**face->normalizedLandmarks(), regressorData->crops.face.bbox), yuv, *debugRendererState) failed with %s, returning %s"
+ "Running m_debugRenderer->encode(regressorData->crops.face, yuv, *debugRendererState) failed with %s, returning %s"
+ "Running m_debugRenderer->encode(regressorData->crops.leftEye, regressorData->crops.rightEye, yuv, *debugRendererState) failed with %s, returning %s"
+ "Running m_debugRenderer->encode(tmpCrops.face, m_debugColorMap->yuv(*trackedFace), *debugRendererState) failed with %s, returning %s"
+ "Running m_debugRendererCbCr->encode(vertices, type, state.textureCbCr, state.commandBuffer, simd::make_float4(yuv.y, yuv.z, 0.0f, 1.0f)) failed with %s, returning %s"
+ "Running m_debugRendererY->encode(vertices, type, state.textureY, state.commandBuffer, simd::make_float4(yuv.x, 0.0f, 0.0f, 1.0f)) failed with %s, returning %s"
+ "Running setupDebugRenderer() failed with %s, returning %s"
+ "Running writeDebugData(debugDictionary, *face, regressorData->crops, regressorData->warpfields, m_debugColorMap->rgb(*face), true) failed with %s, returning %s"
+ "Running writeDebugData(debugDictionary, *trackedFace, tmpCrops, {}, m_debugColorMap->rgb(*trackedFace), false) failed with %s, returning %s"
+ "ViewpointCorrectionDebugRenderer"
- "Precondition violated: destination.pixelFormat == MTLPixelFormatRG8Unorm"
- "Precondition violated: m_textureCbCr"
- "Running draw(linePoints(boundingBoxCorners(crops.face.bbox)), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(linePoints(crops.leftEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(linePoints(crops.rightEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(normalizedLandmarksToImage(**trackedFace.normalizedLandmarks(), crops.face.bbox), PrimitiveTypePoints) failed with %s, returning %s"
- "Running drawDebugData(*face, regressorData->crops, m_debugColorMap->yuv(*face)) failed with %s, returning %s"
- "Running drawInputData(data) failed with %s, returning %s"
- "Running drawInputFaceDetections(*m_debugRendererCbCr, commandBuffer, m_textureCbCr, data.inputFaceDetections()) failed with %s, returning %s"
- "Running m_debugRendererCbCr->encode(cbCrVertices, type, m_textureCbCr, commandBuffer, simd::make_float4(yuv.y, yuv.z, 0.0f, 1.0f)) failed with %s, returning %s"
- "Running m_debugRendererY->encode(vertices, type, m_textureY, commandBuffer, simd::make_float4(yuv.x, 0.0f, 0.0f, 1.0f)) failed with %s, returning %s"
- "Running renderer.encode(bboxVertices, PrimitiveTypeLineStrip, destination, commandBuffer, kRedColor) failed with %s, returning %s"
- "Running renderer.encode(segment, PrimitiveTypeLineStrip, destination, commandBuffer, kRedColor) failed with %s, returning %s"
- "Running setupTexturesAndDrawInputData() failed with %s, returning %s"
- "Running writeDebugData(debugDictionary, *face, regressorData->crops, regressorData->warpfields, color, true) failed with %s, returning %s"
- "Running writeDebugData(debugDictionary, *trackedFace, tmpCrops, {}, color, false) failed with %s, returning %s"
- "ViewpointCorrectionProcessor::drawDebugData"
- "ViewpointCorrectionProcessor::drawInputData"

```
