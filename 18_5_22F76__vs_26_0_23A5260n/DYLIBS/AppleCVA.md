## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`

```diff

-1001.202.0.0.0
-  __TEXT.__text: 0xb8d28
+1002.4.0.0.0
+  __TEXT.__text: 0xbd788
   __TEXT.__auth_stubs: 0x1ab0
   __TEXT.__objc_methlist: 0xb4
-  __TEXT.__const: 0x8e9
-  __TEXT.__gcc_except_tab: 0x4910
-  __TEXT.__cstring: 0x5c4f
-  __TEXT.__oslogstring: 0x838b
-  __TEXT.__unwind_info: 0x1368
+  __TEXT.__const: 0x999
+  __TEXT.__gcc_except_tab: 0x4928
+  __TEXT.__cstring: 0x5bb8
+  __TEXT.__oslogstring: 0x8f87
+  __TEXT.__unwind_info: 0x1350
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0xd99
-  __TEXT.__objc_methtype: 0x1f5
-  __TEXT.__objc_stubs: 0x1240
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x15a0
+  __TEXT.__objc_methname: 0xd69
+  __TEXT.__objc_methtype: 0x1e6
+  __TEXT.__objc_stubs: 0x1220
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x1578
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a0
+  __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0xd68
-  __AUTH_CONST.__const: 0x1fc8
-  __AUTH_CONST.__cfstring: 0x39c0
-  __AUTH_CONST.__objc_const: 0x368
+  __AUTH_CONST.__const: 0x1f20
+  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__objc_const: 0x348
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0xf0
-  __DATA.__objc_ivar: 0x20
-  __DATA.__bss: 0x3c0
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x178
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x1c
+  __DATA.__bss: 0x300
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__data: 0x40
+  __DATA_DIRTY.__bss: 0x220
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E859F941-E4DD-3A3F-AC83-348F86510E45
-  Functions: 1200
-  Symbols:   966
-  CStrings:  2326
+  UUID: 994518A6-2C3A-371C-9C86-D8C5BD84BF2F
+  Functions: 1198
+  Symbols:   972
+  CStrings:  2339
 
Symbols:
+ _CVAViewpointCorrectionMaximumNumberOfCorrectedFaces
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ _kCVAViewpointCorrection_DebugFaceColor
+ _kCVAViewpointCorrection_DebugFaceUUID
+ _kCVAViewpointCorrection_DebugFaces
+ _kCVAViewpointCorrection_NumberOfCorrectedFaces
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferIOSurfacePropertiesKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferWidthKey
+ _os_unfair_lock_lock
+ _os_unfair_lock_trylock
+ _os_unfair_lock_unlock
- _MGGetStringAnswer
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
- _kCVAViewpointCorrection_DrawDebugMesh
- _kCVAViewpointCorrection_EnableDistanceThresholdsMultiplier
- _kCVAViewpointCorrection_EnablePerspectiveWarp
- _kCVAViewpointCorrection_UseFixedCorrection
CStrings:
+ "%@_%d"
+ "%d corrected faces in frame with timestamp %f"
+ "@24@0:8@16"
+ "Assertion failed: !inputFaceDetectionPerTrack[bestTrackIndex].has_value()"
+ "Assertion failed: (modificationStatus.imageModified && modificationStatus.numCorrectedFaces > 0) || (!modificationStatus.imageModified && modificationStatus.numCorrectedFaces == 0)"
+ "Assertion failed: CVMetalTextureCacheCreate(NULL, NULL, m_device, NULL, outputPointerTo(m_metalTextureCache)) == kCVReturnSuccess"
+ "Assertion failed: buffer"
+ "Assertion failed: dataIndex < m_regressorsWithData.size()"
+ "Assertion failed: faceDictionary.setItem(kCVAViewpointCorrection_DebugEstimatedFaceDistance, cva::ItemHandler::createValue(trackedFace.faceDistance()))"
+ "Assertion failed: faceDictionary.setItem(kCVAViewpointCorrection_DebugFadeoutFactor, cva::ItemHandler::createValue(fadeoutFactor))"
+ "Assertion failed: faceDictionary.setItem(kCVAViewpointCorrection_DebugRawLandmarksJitterValue, cva::ItemHandler::createValue(trackedFace.rawLandmarksJitter()))"
+ "Assertion failed: faceDictionary.setItem(key, cva::ItemHandler::createValue(averageWarpFieldIntensity))"
+ "Assertion failed: m_debugColorMap"
+ "Assertion failed: m_imageSampler"
+ "Assertion failed: m_imageSampler = [[CVABilinearSampler alloc] initWithDevice:device]"
+ "Assertion failed: m_trackedFaces.size() <= m_maxNumberOfTrackedFaces"
+ "Assertion failed: nextIndex < m_isColorAssigned.size()"
+ "Assertion failed: preparedFlows->size() == facesWithPreparedFlows.size()"
+ "Assertion failed: regressorWithData.landmarks"
+ "Assertion failed: regressorWithData.rigidPoseAngles"
+ "Assertion failed: result.size() == warpfields.size()"
+ "Assertion failed: state.m->m_commandBuffer"
+ "Assertion failed: state.m->m_eyesParameterBuffers"
+ "Assertion failed: state.m->m_prepareFlowResult.valid()"
+ "Assertion failed: trackedFace"
+ "Assertion failed: trackedFace->isValid()"
+ "Assertion failed: trackedFace.normalizedLandmarks()"
+ "Assertion failed: warpfield.warpfieldX"
+ "Assertion failed: warpfield.warpfieldY"
+ "Could not create crops command buffer"
+ "DebugFaceColor"
+ "DebugFaceUUID"
+ "DebugFaces"
+ "Discarding track (uuid=%s) due to high landmarks jitter."
+ "Error during the initialization of the faceprinter."
+ "FaceKitRecognitionProcessor initialization failed: could not create a recognition thread."
+ "FaceKitRecognitionProcessor initialization failed: null recognition object."
+ "Failed to create parameter buffer handle"
+ "Failed to initialize a regressor"
+ "Failed to initialize face tracker"
+ "Failed to initialize the warp field"
+ "Initializing RecognitionProcessor with\nrecognitionUpdatePeriod:%d ms\nsynchronization:%d\nclusterDetectionRange:%f\nclusterRadius:%f"
+ "NumberOfCorrectedFaces"
+ "PixelBufferCopier: failed to allocate pixel buffer"
+ "Precondition violated: !m_regressorsWithData.empty()"
+ "Precondition violated: CFGetTypeID(pixelBufferMetadata.get()) == CFDictionaryGetTypeID()"
+ "Precondition violated: commandQueue"
+ "Precondition violated: faceCrop->surface()"
+ "Precondition violated: textureY && textureCbCr"
+ "Precondition violated: trackedFaces.size() <= kAvailableColors.size()"
+ "Precondition violated: warpfields.size() <= supportedFlows()"
+ "Running AsyncFlowWarper::applyFlow(std::move(preparedFlow), correctionStrength, flowApplied) failed with %s, returning %s"
+ "Running addEyeCropDataToDictionary(crops.leftEye, true, faceDictionary) failed with %s, returning %s"
+ "Running addEyeCropDataToDictionary(crops.rightEye, false, faceDictionary) failed with %s, returning %s"
+ "Running addFaceCropDataToDictionary(crops.face, didRunNetwork, faceDictionary) failed with %s, returning %s"
+ "Running addLandmarksToDictionary(normalizedLandmarksToImage(**trackedFace.normalizedLandmarks(), crops.face.bbox), faceDictionary) failed with %s, returning %s"
+ "Running addWarpFieldIntensity(warpfields.leftWarpfieldX->surface(), warpfields.leftWarpfieldY->surface(), kCVAViewpointCorrection_DebugLeftWarpFieldAverageIntensity) failed with %s, returning %s"
+ "Running addWarpFieldIntensity(warpfields.rightWarpfieldX->surface(), warpfields.rightWarpfieldY->surface(), kCVAViewpointCorrection_DebugRightWarpFieldAverageIntensity) failed with %s, returning %s"
+ "Running augmentFace(commandBuffer, crops.face) failed with %s, returning %s"
+ "Running bindSurfaces(regressorWithData, m_correctionIntensitySurface) failed with %s, returning %s"
+ "Running checkFaceFeatures() failed with %s, returning %s"
+ "Running cropEyes(commandBuffer, normalizedLandmarksToImage(**trackedFace.normalizedLandmarks(), crops.face.bbox), data.virtualCameraOffset(), crops) failed with %s, returning %s"
+ "Running cropFace(commandBuffer, crops.face) failed with %s, returning %s"
+ "Running draw(linePoints(boundingBoxCorners(crops.face.bbox)), PrimitiveTypeLineStrip) failed with %s, returning %s"
+ "Running draw(linePoints(crops.leftEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
+ "Running draw(linePoints(crops.rightEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
+ "Running draw(normalizedLandmarksToImage(**trackedFace.normalizedLandmarks(), crops.face.bbox), PrimitiveTypePoints) failed with %s, returning %s"
+ "Running drawDebugData(*face, regressorData->crops, m_debugColorMap->yuv(*face)) failed with %s, returning %s"
+ "Running encoder->setup(commandQueue, metalHelpers, maxSupportedFlows) failed with %s, returning %s"
+ "Running initRegressor(resourceDir) failed with %s, returning %s"
+ "Running m_debugColorMap->update(m_tracker->trackedFaces()) failed with %s, returning %s"
+ "Running m_debugRendererCbCr->encode(cbCrVertices, type, m_textureCbCr, commandBuffer, simd::make_float4(yuv.y, yuv.z, 0.0f, 1.0f)) failed with %s, returning %s"
+ "Running m_debugRendererY->encode(vertices, type, m_textureY, commandBuffer, simd::make_float4(yuv.x, 0.0f, 0.0f, 1.0f)) failed with %s, returning %s"
+ "Running m_flowWarper->apply(textureY, textureCbCr, warpfield.warpfieldX, warpfield.warpfieldY, warpfield.transform, *eyeWarpParams, commandBuffer) failed with %s, returning %s"
+ "Running m_position.update(face->position, timestamp) failed with %s, returning %s"
+ "Running m_tracker->update(data.faces(), data.timestamp(), data.correctionEnabled(), uprightFaceRollAngle, distanceThresholdsMultiplier) failed with %s, returning %s"
+ "Running readAnglesFromIOSurface(anglesSurface, rigidPoseAngles) failed with %s, returning %s"
+ "Running readLandmarksFromIOSurface(landmarksSurface, landmarks) failed with %s, returning %s"
+ "Running regressor->setup(resourceDir) failed with %s, returning %s"
+ "Running regressorData->regressor->runNetwork() failed with %s, returning %s"
+ "Running regressorWithData.regressor->bindSurfaces(allSurfaces) failed with %s, returning %s"
+ "Running scheduleCrops(data, *face, regressorData->crops) failed with %s, returning %s"
+ "Running setupEyeCrop(@\"leftEye\", regressorWithData.crops.leftEye) failed with %s, returning %s"
+ "Running setupEyeCrop(@\"rightEye\", regressorWithData.crops.rightEye) failed with %s, returning %s"
+ "Running setupFaceCrop(@\"faceCrop.texture\", regressorWithData.crops.face) failed with %s, returning %s"
+ "Running setupParameterBuffers(buffers.leftWarpParams) failed with %s, returning %s"
+ "Running setupParameterBuffers(buffers.rightWarpParams) failed with %s, returning %s"
+ "Running setupRegressorInputs(m_regressorsWithData[i], m_metalHelpers->device(), i) failed with %s, returning %s"
+ "Running setupRegressorOutputs(m_regressorsWithData[i], m_metalHelpers->device(), i) failed with %s, returning %s"
+ "Running setupRegressors(maxNumCorrectedFaces) failed with %s, returning %s"
+ "Running setupTexturesAndDrawInputData() failed with %s, returning %s"
+ "Running setupWarpfield(regressorWithData.warpfields.leftWarpfieldX, leftWarpSurfacePropsX, @\"leftEyeWarpfieldX\") failed with %s, returning %s"
+ "Running setupWarpfield(regressorWithData.warpfields.leftWarpfieldY, leftWarpSurfacePropsY, @\"leftEyeWarpfieldY\") failed with %s, returning %s"
+ "Running setupWarpfield(regressorWithData.warpfields.rightWarpfieldX, rightWarpSurfacePropsX, @\"rightEyeWarpfieldX\") failed with %s, returning %s"
+ "Running setupWarpfield(regressorWithData.warpfields.rightWarpfieldY, rightWarpSurfacePropsY, @\"rightEyeWarpfieldY\") failed with %s, returning %s"
+ "Running state.m->m_prepareFlowResult.get().value_or(ViewpointStatus::AssertionFailed) failed with %s, returning %s"
+ "Running trackedFace->update(faceDetection, correctionEnabled, uprightFaceRollAngle, distanceThresholdsMultiplier, timestamp) failed with %s, returning %s"
+ "Running trackedFace->update(faces[i], correctionEnabled, uprightFaceRollAngle, distanceThresholdsMultiplier, timestamp) failed with %s, returning %s"
+ "Running trackedFace->update(std::nullopt, correctionEnabled, uprightFaceRollAngle, distanceThresholdsMultiplier, timestamp) failed with %s, returning %s"
+ "Running trackedFace.updateLandmarks(transformedLandmarks, timestamp) failed with %s, returning %s"
+ "Running trackedFace.updateLandmarksJitter(sum, timestamp) failed with %s, returning %s"
+ "Running updateJitterValue(trackedFace, crops, landmarks, jitterOffset, timestamp) failed with %s, returning %s"
+ "Running updateTrackedFaceWithNetworkOutputs(*face, regressorData->crops, regressorData->landmarks, regressorData->rigidPoseAngles, data.timestamp()) failed with %s, returning %s"
+ "Running updateTrackedFacesWithFaceDetections(m_trackedFaces, faces, timestamp, correctionEnabled, uprightFaceRollAngle, distanceThresholdsMultiplier) failed with %s, returning %s"
+ "Running writeDebugData(debugDictionary, *face, regressorData->crops, regressorData->warpfields, color, true) failed with %s, returning %s"
+ "Running writeDebugData(debugDictionary, *trackedFace, tmpCrops, {}, color, false) failed with %s, returning %s"
+ "Setup ViewpointCorrectionProcessor for %i faces"
+ "Tracked face (%p uuid=%s) has been invalidated and will be deleted."
+ "Tracking a new face (%p uuid=%s)."
+ "Unsupported number of corrected faces %i, valid range [1, %i]."
+ "ViewpointCorrection # corrected faces: 1 (%i (+%i), %.1f ms (%.1f ms)), 2 (%i (+%i), %.1f ms (%.1f ms)), 3 (%i (+%i), %.1f ms (%.1f ms)), 4 (%i (+%i), %.1f ms (%.1f ms))"
+ "ViewpointCorrectionProcessor::applyFlow_%d"
+ "[4{?=\"position\"}]"
+ "buffer copy for faceprinting was unnecessary, candidate(s) discarded (%d)"
+ "code"
+ "face_identity_cluster_detection_range_v4"
+ "face_identity_cluster_radius_v4"
+ "initWithDevice:"
+ "leftEyeWarpfieldX"
+ "leftEyeWarpfieldY"
+ "rightEyeWarpfieldX"
+ "rightEyeWarpfieldY"
+ "track is still in warmup"
- "%@: Unsupported sampling mode %d."
- "-[CVABilinearSampler initWithDevice:mode:]"
- "@28@0:8@16i24"
- "Assertion failed: CVMetalTextureCacheCreate(NULL, NULL, m_device, NULL, m_metalTextureCache.fill()) == kCVReturnSuccess"
- "Assertion failed: commandBuffer"
- "Assertion failed: debugDictionary->setItem(kCVAViewpointCorrection_DebugEstimatedFaceDistance, cva::ItemHandler::createValue(m_trackedFace->faceDistance()))"
- "Assertion failed: debugDictionary->setItem(kCVAViewpointCorrection_DebugFadeoutFactor, cva::ItemHandler::createValue(fadeoutFactor))"
- "Assertion failed: debugDictionary->setItem(kCVAViewpointCorrection_DebugRawLandmarksJitterValue, cva::ItemHandler::createValue(m_trackedFace->rawLandmarksJitter()))"
- "Assertion failed: debugDictionary->setItem(key, cva::ItemHandler::createValue(averageWarpFieldIntensity))"
- "Assertion failed: eye.warpParams = FlowWarper::ParameterBufferHandle::create(metalHelpers.device())"
- "Assertion failed: eye.warpParams.has_value()"
- "Assertion failed: m_anglesSurface"
- "Assertion failed: m_commandBuffer"
- "Assertion failed: m_eyes"
- "Assertion failed: m_imageSamplers[mode] = [[CVABilinearSampler alloc] initWithDevice:device mode:mode]"
- "Assertion failed: m_landmarksSurface"
- "Assertion failed: m_prepareFlowResult.valid()"
- "Assertion failed: m_trackedFace->isValid()"
- "Assertion failed: m_trackedFace->normalizedLandmarks()"
- "Assertion failed: sampler"
- "Assertion failed: warpfieldSurface"
- "BilinearSamplerPipeline"
- "Could not create command buffer"
- "Could not initialize rotator"
- "Deleting tracked face."
- "DeviceClass"
- "DrawDebugMesh"
- "Dropping faceprint task groups (too many %i)"
- "EnableDistanceThresholdsMultiplier"
- "EnablePerspectiveWarp"
- "Error during the Initialization of the recognition framework."
- "FaceKitRecognitionProcessor initialization error due to failure to create a recognition thread."
- "FaceKitRecognitionProcessor initialization error due to null recognition framework."
- "Failed to initialize the regressor"
- "Failed to setup warpfield texture wrapper"
- "Initializing RecognitionProcessor with recognitionUpdatePeriod:%d ms and synchronization:%d."
- "No face to track."
- "Precondition violated: CFGetTypeID(*pixelBufferMetadata) == CFDictionaryGetTypeID()"
- "Precondition violated: commandBuffer && textureY && textureCbCr"
- "Precondition violated: inputNames.size() == expectedInputNames.size()"
- "Precondition violated: m_crops.face.crop->surface()"
- "Precondition violated: m_regressor->supportsConfigurableCorrectionIntensity()"
- "Precondition violated: m_trackedFace"
- "Precondition violated: state"
- "Precondition violated: w == h"
- "Precondition violated: warpfieldSurfaceProperties"
- "Rotation helper type %i"
- "Running AsyncFlowWarper::applyFlow(std::move(preparedFlow), correctionStrength, imageModified) failed with %s, returning %s"
- "Running addEyeCropDataToDictionary(m_crops.leftEye, true, *debugDictionary) failed with %s, returning %s"
- "Running addEyeCropDataToDictionary(m_crops.rightEye, false, *debugDictionary) failed with %s, returning %s"
- "Running addFaceCropDataToDictionary(m_crops.face, didRunNetwork, *debugDictionary) failed with %s, returning %s"
- "Running addLandmarksToDictionary(normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), m_crops.face.bbox), *debugDictionary) failed with %s, returning %s"
- "Running addWarpFieldIntensity(m_flowWarper->leftWarpfieldSurfaceX(), m_flowWarper->leftWarpfieldSurfaceY(), kCVAViewpointCorrection_DebugLeftWarpFieldAverageIntensity) failed with %s, returning %s"
- "Running addWarpFieldIntensity(m_flowWarper->rightWarpfieldSurfaceX(), m_flowWarper->rightWarpfieldSurfaceY(), kCVAViewpointCorrection_DebugRightWarpFieldAverageIntensity) failed with %s, returning %s"
- "Running augmentFace(commandBuffer, m_crops.face) failed with %s, returning %s"
- "Running cropEyes(commandBuffer, normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), m_crops.face.bbox), data.virtualCameraOffset(), m_crops, samplerMode) failed with %s, returning %s"
- "Running cropFace(commandBuffer, m_crops.face, samplerMode) failed with %s, returning %s"
- "Running draw(linePoints(boundingBoxCorners(m_crops.face.bbox)), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(linePoints(m_crops.leftEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(linePoints(m_crops.rightEye.cropCorners()), PrimitiveTypeLineStrip) failed with %s, returning %s"
- "Running draw(normalizedLandmarksToImage(**m_trackedFace->normalizedLandmarks(), m_crops.face.bbox), PrimitiveTypePoints) failed with %s, returning %s"
- "Running drawDebugData() failed with %s, returning %s"
- "Running encoder->setup(metalHelpers, warmupBuffer, warpfieldSurfaceProperties) failed with %s, returning %s"
- "Running extractFaceFeatures() failed with %s, returning %s"
- "Running initRegressor(resourceDir, loadLegacyModel) failed with %s, returning %s"
- "Running m_flowWarper->apply(textureY, textureCbCr, eye.warpfieldX->texture(), eye.warpfieldY->texture(), leftEye(eye) ? transformLeft : transformRight, *eye.warpParams, commandBuffer) failed with %s, returning %s"
- "Running m_normalizedPosition.update(face->normalizedPosition, timestamp) failed with %s, returning %s"
- "Running m_prepareFlowResult.get().value_or(ViewpointStatus::AssertionFailed) failed with %s, returning %s"
- "Running m_regressor->bindSurfaces(allSurfaces) failed with %s, returning %s"
- "Running m_regressor->runNetwork() failed with %s, returning %s"
- "Running m_trackedFace->update(facePosition, data.correctionEnabled(), uprightFaceRollAngle, distanceThresholdsMultiplier, data.timestamp()) failed with %s, returning %s"
- "Running m_trackedFace->updateLandmarks(transformedLandmarks, timestamp) failed with %s, returning %s"
- "Running m_trackedFace->updateLandmarksJitter(sum, timestamp) failed with %s, returning %s"
- "Running readAnglesFromIOSurface(m_anglesSurface, rigidPoseAngles) failed with %s, returning %s"
- "Running readLandmarksFromIOSurface(m_landmarksSurface, landmarks) failed with %s, returning %s"
- "Running regressor->setup(resourceDir, loadLegacyModel) failed with %s, returning %s"
- "Running scheduleCrops(data, mode) failed with %s, returning %s"
- "Running setupCropData(@\"leftEye\", m_crops.leftEye) failed with %s, returning %s"
- "Running setupCropData(@\"rightEye\", m_crops.rightEye) failed with %s, returning %s"
- "Running setupRegressorInputs() failed with %s, returning %s"
- "Running setupRegressorOutputs() failed with %s, returning %s"
- "Running setupWarpfield(eye.warpfieldX, @\"warpfieldX\") failed with %s, returning %s"
- "Running setupWarpfield(eye.warpfieldY, @\"warpfieldY\") failed with %s, returning %s"
- "Running updateFacePositionAndFadeout(data) failed with %s, returning %s"
- "Running updateJitterValue(landmarks, jitterOffset, timestamp) failed with %s, returning %s"
- "Running updateTrackedFaceWithNetworkOutputs(data.timestamp()) failed with %s, returning %s"
- "Running writeDebugData(debugDictionary, false) failed with %s, returning %s"
- "Running writeDebugData(debugDictionary, true) failed with %s, returning %s"
- "Tracking a new face."
- "UseFixedCorrection"
- "ViewpointCorrectionProcessor::applyFlow"
- "[4{?=\"position\"\"texcoord\"}]"
- "_mode"
- "bilinearSamplerFragmentShader"
- "face_identity_cluster_detection_range"
- "face_identity_cluster_radius"
- "i"
- "iPhone"
- "initWithDevice:mode:"
- "isEqualToString:"
- "kCVAViewpointCorrection_UseFixedCorrection is deprecated and will be removed soon."
- "luma"
- "stringByAppendingString:"
- "viewpoint_correction_eyecrop_offset"
- "warpfieldX"
- "warpfieldY"

```
