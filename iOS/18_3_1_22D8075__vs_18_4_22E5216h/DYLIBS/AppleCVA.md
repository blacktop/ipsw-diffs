## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`

```diff

-1001.150.0.0.0
-  __TEXT.__text: 0xbb7a4
+1001.202.0.0.0
+  __TEXT.__text: 0xb8d28
   __TEXT.__auth_stubs: 0x1ab0
   __TEXT.__objc_methlist: 0xb4
-  __TEXT.__gcc_except_tab: 0x4bc8
-  __TEXT.__const: 0x871
-  __TEXT.__cstring: 0x5be5
-  __TEXT.__oslogstring: 0x83c5
-  __TEXT.__unwind_info: 0x1360
+  __TEXT.__const: 0x8e9
+  __TEXT.__gcc_except_tab: 0x4910
+  __TEXT.__cstring: 0x5c4f
+  __TEXT.__oslogstring: 0x838b
+  __TEXT.__unwind_info: 0x1368
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0xd8d
+  __TEXT.__objc_methname: 0xd99
   __TEXT.__objc_methtype: 0x1f5
-  __TEXT.__objc_stubs: 0x1280
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x1590
+  __TEXT.__objc_stubs: 0x1240
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x15a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0xd68
-  __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__const: 0x2068
-  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__auth_ptr: 0x40
+  __AUTH_CONST.__const: 0x1fc8
+  __AUTH_CONST.__cfstring: 0x39c0
   __AUTH_CONST.__objc_const: 0x368
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0xf0
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x40
-  __DATA.__bss: 0x458
+  __DATA.__bss: 0x3c0
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__data: 0xc8
+  __DATA_DIRTY.__bss: 0x178
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1208
-  Symbols:   964
-  CStrings:  1846
+  Functions: 1200
+  Symbols:   966
+  CStrings:  1865
 
Symbols:
+ _CVAFaceTrackingLiteGetCreateOptionsForFeatures
+ _CVAFaceTrackingLiteSetColorImageWithDistortion
+ _e5rt_get_last_error_message
+ _kCVAFaceTracking_ConfidenceLevel
+ _objc_retain_x9
- _CVAFaceTrackingTransformData
- __ZNK3cva11ItemHandler9getVectorIjEENS_6MatrixIT_Lj0ELj1EXclsr6detailE7IsSmallIS3_XLj0EEXLj1EEEEEEEv
- _objc_alloc_init
CStrings:
+ "Assertion failed: commandBuffer"
+ "Assertion failed: cropSurface"
+ "Assertion failed: dictionary.setItem(\"faceCrop\", cva::ItemHandler::createVector(faceCrop.bbox.toVector4f()))"
+ "Assertion failed: eye.warpParams.has_value()"
+ "Assertion failed: m_commandBuffer"
+ "Assertion failed: m_eyes"
+ "Assertion failed: m_prepareFlowResult.valid()"
+ "Assertion failed: noiseSurface"
+ "Assertion failed: prepareFlowResult.valid()"
+ "Assertion failed: surface"
+ "Assertion failed: surface.planeCount == 0"
+ "Assertion failed: warpfieldSurface"
+ "CVAViewpointCorrection created (%p)."
+ "Color camera extrinsics: (%.3f %.3f %.3f %.3f), (%.3f %.3f %.3f %.3f), (%.3f %.3f %.3f %.3f)"
+ "Color camera intrinsics: (%.3f %.3f %.3f), (%.3f %.3f %.3f), (%.3f %.3f %.3f)"
+ "Color camera resolution: %d x %d"
+ "Creating CVAViewpointCorrection with *default* options (user has given no options)."
+ "Creating CVAViewpointCorrection with options: %s."
+ "Currently only square crops are supported."
+ "Error running operation on the ANE"
+ "Failed to create Metal Helpers"
+ "Failed to create flow warper"
+ "Failed to encode the operation to the stream. %s"
+ "Failed to execute the stream. %s"
+ "Failed to initialize CbCr debug renderer"
+ "Failed to initialize Metal helpers"
+ "Failed to initialize Y debug renderer"
+ "Failed to initialize flow warper"
+ "Failed to initialize image augmenter"
+ "Failed to initialize processor"
+ "Failed to initialize the regressor"
+ "Failed to prepare flow."
+ "Failed to reset the stream. %s"
+ "Failed to setup eye crop texture wrapper"
+ "Failed to setup face crop noise texture wrapper"
+ "Failed to setup face crop texture wrapper"
+ "Failed to setup warpfield texture wrapper"
+ "Finalizing CVAViewpointCorrection (%p)."
+ "Precondition violated: commandBuffer && textureY && textureCbCr"
+ "Precondition violated: eyeCropData.crop->texture().width == eyeCropData.crop->texture().height"
+ "Precondition violated: m_crops.face.crop->surface()"
+ "Precondition violated: state"
+ "Running AsyncFlowWarper::applyFlow(std::move(preparedFlow), correctionStrength, imageModified) failed with %s, returning %s"
+ "Running MTLPixelFormatFromCVPixelFormat(m_surface.pixelFormat, pixelFormat) failed with %s, returning %s"
+ "Running addEyeCropDataToDictionary(m_crops.leftEye, true, *debugDictionary) failed with %s, returning %s"
+ "Running addEyeCropDataToDictionary(m_crops.rightEye, false, *debugDictionary) failed with %s, returning %s"
+ "Running addFaceCropDataToDictionary(m_crops.face, didRunNetwork, *debugDictionary) failed with %s, returning %s"
+ "Running addLandmarksToDictionary(normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), m_crops.face.bbox), *debugDictionary) failed with %s, returning %s"
+ "Running addSurface(kCVAViewpointCorrection_DebugFaceCrop, faceCrop.crop->surface(), dictionary) failed with %s, returning %s"
+ "Running addSurface(surfaceKey, eyeCrop.crop->surface(), dictionary) failed with %s, returning %s"
+ "Running augmentFace(commandBuffer, m_crops.face) failed with %s, returning %s"
+ "Running augmenter->setup(device, imageWidth, imageHeight) failed with %s, returning %s"
+ "Running cropEyes(commandBuffer, normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), m_crops.face.bbox), data.virtualCameraOffset(), m_crops, samplerMode) failed with %s, returning %s"
+ "Running cropFace(commandBuffer, m_crops.face, samplerMode) failed with %s, returning %s"
+ "Running draw(linePoints(boundingBoxCorners(m_crops.face.bbox)), PrimitiveTypeLineStrip) failed with %s, returning %s"
+ "Running draw(linePoints(m_crops.leftEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
+ "Running draw(linePoints(m_crops.rightEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
+ "Running draw(normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), m_crops.face.bbox), PrimitiveTypePoints) failed with %s, returning %s"
+ "Running drawDebugData() failed with %s, returning %s"
+ "Running encoder->setup(metalHelpers, warmupBuffer, warpfieldSurfaceProperties) failed with %s, returning %s"
+ "Running helpers->setup(device) failed with %s, returning %s"
+ "Running inputData->setup(params) failed with %s, returning %s"
+ "Running m_coarseHeadPoseCorrectionStrength.update(headPoseInValidRange, timestamp) failed with %s, returning %s"
+ "Running m_flowWarper->apply(textureY, textureCbCr, eye.warpfieldX->texture(), eye.warpfieldY->texture(), leftEye(eye) ? transformLeft : transformRight, *eye.warpParams, commandBuffer) failed with %s, returning %s"
+ "Running m_imageAugmenter->encodeToCommandBuffer(commandBuffer, m_faceCropNoise->texture(), jitterOffset, maxLumaChange, faceCrop.crop->texture()) failed with %s, returning %s"
+ "Running m_prepareFlowResult.get().value_or(ViewpointStatus::AssertionFailed) failed with %s, returning %s"
+ "Running m_trackedFace->updateLandmarks(transformedLandmarks, timestamp) failed with %s, returning %s"
+ "Running pipeline->setup(options) failed with %s, returning %s"
+ "Running processor->setup(options) failed with %s, returning %s"
+ "Running regressor->setup(resourceDir, loadLegacyModel) failed with %s, returning %s"
+ "Running scheduleCrops(data, mode) failed with %s, returning %s"
+ "Running setupCropData(@\"leftEye\", m_crops.leftEye) failed with %s, returning %s"
+ "Running setupCropData(@\"rightEye\", m_crops.rightEye) failed with %s, returning %s"
+ "Running setupWarpfield(eye.warpfieldX, @\"warpfieldX\") failed with %s, returning %s"
+ "Running setupWarpfield(eye.warpfieldY, @\"warpfieldY\") failed with %s, returning %s"
+ "Running updateJitterValue(landmarks, jitterOffset, timestamp) failed with %s, returning %s"
+ "Running updateTrackedFaceWithNetworkOutputs(data.timestamp()) failed with %s, returning %s"
+ "Running warper->setup(device) failed with %s, returning %s"
+ "Running wrapper->setup(device, surface, label, usage, clear) failed with %s, returning %s"
+ "Running writeDebugData(debugDictionary, false) failed with %s, returning %s"
+ "Running writeDebugData(debugDictionary, true) failed with %s, returning %s"
+ "ViewpointCorrectionProcessor::applyFlow"
+ "confidence_level"
+ "face_selection_offcenter_penalty"
+ "kCVAViewpointCorrection_UseFixedCorrection is deprecated and will be removed soon."
+ "off-center penalty for face selection"
+ "planeCount"
+ "stringByAppendingString:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "using strict error thresholds until tracking is stable (user %s)"
+ "~ViewpointCorrectionPipeline."
- "Assertion failed: commandBuffer = [m_queue commandBuffer]"
- "Assertion failed: data.cropSurface"
- "Assertion failed: dictionary.setItem(\"faceCrop\", cva::ItemHandler::createVector(bbox.toVector4f()))"
- "Assertion failed: isSuccess(e5rt_execution_stream_encode_operation(m_stream.get(), m_operation.get()))"
- "Assertion failed: isSuccess(e5rt_execution_stream_execute_sync(m_stream.get()))"
- "Assertion failed: isSuccess(e5rt_execution_stream_reset(m_stream.get()))"
- "Assertion failed: m_encodingResult.valid()"
- "Assertion failed: m_faceCropNoiseSurface"
- "Assertion failed: m_faceCropSurface"
- "Assertion failed: std::holds_alternative<Config>(configOrError)"
- "Assertion failed: std::holds_alternative<DebugRenderer>(rendererOrError)"
- "Assertion failed: warpfieldSurfaceX"
- "Assertion failed: warpfieldSurfaceY"
- "CVAViewpointCorrectionCreate"
- "CVAViewpointCorrectionCreate done"
- "Currently we only support square crops."
- "Decreasing max distance for tracking to %f mm; due to previous error detected (user %s)."
- "Increasing min distance for tracking to %f mm; due to previous error detected (user %s)."
- "Precondition violated: !m_encodingResult.valid()"
- "Precondition violated: eyeCropData.crop.texture().width == eyeCropData.crop.texture().height"
- "Precondition violated: m_encodingResult.valid()"
- "Precondition violated: m_faceCropSurface"
- "Precondition violated: texture.iosurface"
- "Running MTLPixelFormatFromCVPixelFormat(surface.pixelFormat, format) failed with %s, returning %s"
- "Running addEyeCropDataToDictionary(m_leftEye, true, *debugDictionary) failed with %s, returning %s"
- "Running addEyeCropDataToDictionary(m_rightEye, false, *debugDictionary) failed with %s, returning %s"
- "Running addFaceCropDataToDictionary(bbox, didRunNetwork ? m_faceCropSurface : nil, *debugDictionary) failed with %s, returning %s"
- "Running addLandmarksToDictionary(normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), bbox), *debugDictionary) failed with %s, returning %s"
- "Running addSurface(kCVAViewpointCorrection_DebugFaceCrop, surface, dictionary) failed with %s, returning %s"
- "Running addSurface(surfaceKey, eyeCrop.cropSurface, dictionary) failed with %s, returning %s"
- "Running augmentFace(commandBuffer) failed with %s, returning %s"
- "Running construct(m_flowWarper, *m_metalHelpers, warmupBuffer, leftWarpSurfacePropsX) failed with %s, returning %s"
- "Running construct(m_flowWarper, metalHelpers.device()) failed with %s, returning %s"
- "Running construct(m_imageAugmenter, device, uint32_t(m_faceCropNoiseSurface.width), uint32_t(m_faceCropNoiseSurface.height)) failed with %s, returning %s"
- "Running construct(m_metalHelpers, device) failed with %s, returning %s"
- "Running construct(m_processor, options) failed with %s, returning %s"
- "Running construct(m_regressor, resourceDir, loadLegacyModel) failed with %s, returning %s"
- "Running cropEyes(commandBuffer, normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), bbox), data.virtualCameraOffset(), faceCropToImage, faceCropCamera, samplerMode) failed with %s, returning %s"
- "Running cropFace(commandBuffer, faceCropToImage, samplerMode) failed with %s, returning %s"
- "Running draw(linePoints(boundingBoxCorners(bbox)), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(linePoints(m_leftEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(linePoints(m_rightEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), bbox), PrimitiveTypePoints) failed with %s, returning %s"
- "Running drawDebugData(bbox) failed with %s, returning %s"
- "Running m_encodingResult.get().value_or(ViewpointStatus::AssertionFailed) failed with %s, returning %s"
- "Running m_flowWarper->apply(textureY, textureCbCr, eye.warpfieldX.texture(), eye.warpfieldY.texture(), leftEye(eye) ? transformLeft : transformRight, *eye.warpParams, commandBuffer) failed with %s, returning %s"
- "Running m_flowWarper->endEncoding(fadeout) failed with %s, returning %s"
- "Running m_flowWarper->startEncoding(commandBuffer, m_textureY, m_textureCbCr, m_leftEye.imageToCropTransform, m_rightEye.imageToCropTransform, data.debugFlowEnabled()) failed with %s, returning %s"
- "Running m_imageAugmenter->encodeToCommandBuffer(commandBuffer, m_faceCropNoise.texture(), jitterOffset, maxLumaChange, m_faceCrop.texture()) failed with %s, returning %s"
- "Running m_metalHelpers->setupTextureBuffer(data.cropSurface, MTLTextureUsageRenderTarget, true, data.crop) failed with %s, returning %s"
- "Running m_metalHelpers->setupTextureBuffer(m_faceCropNoiseSurface, MTLTextureUsageShaderRead, false, m_faceCropNoise) failed with %s, returning %s"
- "Running m_metalHelpers->setupTextureBuffer(m_faceCropSurface, MTLTextureUsageShaderRead | MTLTextureUsageShaderWrite | MTLTextureUsageRenderTarget, false, m_faceCrop) failed with %s, returning %s"
- "Running m_trackedFace->updateLandmarks(transformedLandmarks, data.timestamp()) failed with %s, returning %s"
- "Running metalHelpers.setupTextureBuffer(warpfieldSurfaceX, MTLTextureUsageShaderRead, false, eye.warpfieldX) failed with %s, returning %s"
- "Running metalHelpers.setupTextureBuffer(warpfieldSurfaceY, MTLTextureUsageShaderRead, false, eye.warpfieldY) failed with %s, returning %s"
- "Running result->setup(std::forward<Params>(params)...) failed with %s, returning %s"
- "Running runEyeNetwork(data, bbox, faceCropToImage) failed with %s, returning %s"
- "Running scheduleCrops(data, bbox, faceCropToImage, faceCropCamera, mode) failed with %s, returning %s"
- "Running setupCropData(@\"leftEye\", m_leftEye) failed with %s, returning %s"
- "Running setupCropData(@\"rightEye\", m_rightEye) failed with %s, returning %s"
- "Running updateJitterValue(landmarks, jitterOffset, data.timestamp()) failed with %s, returning %s"
- "Running writeDebugData(debugDictionary, bbox, false) failed with %s, returning %s"
- "Running writeDebugData(debugDictionary, bbox, true) failed with %s, returning %s"
- "Set network failure threshold to %f; due to previous error detected (user %s)."
- "ViewpointCorrectionProcessor::executeMetalOperationsEyes"
- "allKeys"
- "copy"
- "data dictionary contains invalid data"
- "initWithCapacity:"
- "invalid number of faces: %d"
- "iosurface"
- "stringByAppendingPathExtension:"

```
