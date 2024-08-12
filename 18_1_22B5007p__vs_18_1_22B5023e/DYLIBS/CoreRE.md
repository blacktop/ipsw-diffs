## CoreRE

> `/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE`

```diff

-366.0.16.0.3
-  __TEXT.__text: 0x12129b0
-  __TEXT.__auth_stubs: 0x65c0
-  __TEXT.__objc_methlist: 0x2e6c
-  __TEXT.__const: 0x1225e0
-  __TEXT.__gcc_except_tab: 0xc434
-  __TEXT.__cstring: 0x8c6d6
-  __TEXT.__oslogstring: 0x3aa07
+366.0.22.0.4
+  __TEXT.__text: 0x1229cbc
+  __TEXT.__auth_stubs: 0x65e0
+  __TEXT.__objc_methlist: 0x2ea4
+  __TEXT.__const: 0x122f00
+  __TEXT.__gcc_except_tab: 0xc5a0
+  __TEXT.__cstring: 0x8d227
+  __TEXT.__oslogstring: 0x3b2d8
   __TEXT.__ustring: 0x1a
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x5910
-  __TEXT.__objc_classname: 0x751
-  __TEXT.__objc_methname: 0xe7bc
-  __TEXT.__objc_methtype: 0x8ce8
-  __TEXT.__objc_stubs: 0xb700
+  __TEXT.__unwind_info: 0x5918
+  __TEXT.__objc_classname: 0x753
+  __TEXT.__objc_methname: 0xeacf
+  __TEXT.__objc_methtype: 0x8d41
+  __TEXT.__objc_stubs: 0xb800
   __DATA_CONST.__got: 0xd80
-  __DATA_CONST.__const: 0xab00
+  __DATA_CONST.__const: 0xacb0
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3be8
+  __DATA_CONST.__objc_selrefs: 0x3c28
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x32f8
-  __AUTH_CONST.__auth_ptr: 0x248
-  __AUTH_CONST.__const: 0x78cc8
-  __AUTH_CONST.__cfstring: 0x94e0
-  __AUTH_CONST.__objc_const: 0x82e0
+  __AUTH_CONST.__auth_got: 0x3308
+  __AUTH_CONST.__auth_ptr: 0x250
+  __AUTH_CONST.__const: 0x79700
+  __AUTH_CONST.__cfstring: 0x95c0
+  __AUTH_CONST.__objc_const: 0x83a0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__data: 0x1ad8
   __AUTH.__thread_vars: 0x90
   __AUTH.__thread_bss: 0x2d9
-  __DATA.__objc_ivar: 0x370
-  __DATA.__data: 0x24710
+  __DATA.__objc_ivar: 0x380
+  __DATA.__data: 0x247a0
   __DATA.__bss: 0x7920
-  __DATA.__common: 0x8598
+  __DATA.__common: 0x85d8
   __DATA_DIRTY.__objc_ivar: 0x10c
   __DATA_DIRTY.__data: 0x3a8
-  __DATA_DIRTY.__bss: 0x2f618
+  __DATA_DIRTY.__bss: 0x2f648
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 68467
-  Symbols:   77991
-  CStrings:  20177
+  Functions: 68700
+  Symbols:   78253
+  CStrings:  20293
 
Symbols:
+ _REAnchoringComponentGetTrackingImageHeight
+ _REAudioRegisterForPHASESoundEventMixerCreation
+ _RECameraStreamManagerSetARKitPassthrough
+ _RECollisionWorldEnableContactsDetection
+ _REIkParametersComponentEnsureSolversInit
+ _REMeshAssetGetBlendShapeDefinitionCountForPart
+ _REMeshAssetGetBlendShapeDefinitionNameForPart
+ _REMeshAssetGetBlendShapeOffsetsForPart
+ _REMeshAttributeDescriptorCopyBlendShapeOffsetsToBuffer
+ _REPhysicsJointDefinitionDistanceJointGetTolerance
+ _REPhysicsJointDefinitionGetAngularTolerance
+ _REPhysicsJointDefinitionGetLinearTolerance
+ _RERemoteEffectsComponentGetVersion
+ _RERemoteEffectsComponentSetVersion
+ _RERenderManagerGetCameraStreamManager
+ _RERenderManagerUnsetBackdrop
+ __AXDarkenSystemColors
+ __AXSEnhanceBackgroundContrastEnabled
+ _kREMeshAttributeDescriptorBlendShapeOffsetFloat3
CStrings:
+ "\x14"
+ "%!s(MISSING)/%!l(MISSING)u"
+ "%!s(MISSING)/%!s(MISSING)-%!l(MISSING)u"
+ "@64@0:8r^v16{Slice<re::MeshAssetPart>=^{MeshAssetPart}Q}24@40^v48^v56"
+ "@68@0:8I16B20B24C28C32@36@44@52@60"
+ "@96@0:8r^v16@24^v32^v40{DynamicArray<re::MeshResourceDefinition::Level>=^{Allocator}QQI^{Level}}48^v88"
+ "Attempting to load a shader graph with more than 16 textures, which is not supported on devices with tier 1 argument buffer support."
+ "Attempting to load a shader graph with non-2D textures, which is not supported on devices with tier 1 argument buffer support."
+ "B56@0:8r^v16Q24Q32Q40^@48"
+ "BackdropPass"
+ "Blur: Caching WorldToView matrix: Left Camera data not available"
+ "Blur: Caching WorldToView matrix: Right Camera data not available"
+ "BlurPlanesRenderFrameData"
+ "BlurPlatterMeshDraw"
+ "BlurReprojectionState was not set."
+ "Camera projection frustums were not properly set. Unable to initialize encoder in SFBSystemShellReprojectAndFilterNode."
+ "CameraStreamContext"
+ "EnableCustomTextureArray"
+ "Encountered an error communicating with the remote object proxy, which will cause a load failure for asset '%!s(MISSING)'. If the error domain is NSCocoaErrorDomain and the code is 4101 (NSXPCConnectionReplyInvalid), then the underlying issue might have been been logged from Foundation (see NSXPCConnection.m) with subsystem com.apple.Foundation and category xpc.exceptions. The error is: %!@(MISSING)"
+ "FilteredPassthroughBlurredColor"
+ "FilteredPassthroughBlurredColorSRGB"
+ "MeshShadow.PlaneProxy.DepthRatio"
+ "MeshShadow.PlaneProxy.EnablePlaneProxyTiltFade"
+ "MeshShadow.PlaneProxy.TiltFadeOpacityFalloffExp"
+ "MeshShadow.PlaneProxy.UseCylindricalProxy"
+ "MeshShadow.PlaneProxy.WidthRatio"
+ "Missing camera stream context."
+ "Missing data for Reprojection Constants in blur pipeline. Unable to setup encoder."
+ "No passthrough textures sent to blur CameraStreamManager for %!i(MISSING) frame(s)."
+ "PassthroughBlurAndFilter"
+ "PassthroughColor"
+ "PassthroughDownsample"
+ "PassthroughDownsampleCompute"
+ "PassthroughReprojectAndRectify"
+ "PersistentBlurredColorRead"
+ "PersistentBlurredColorWrite"
+ "PersistentVCABlurredColorRead"
+ "PersistentVCABlurredColorWrite"
+ "Provided material function (%!s(MISSING)) contains textures in its second argument. This feature requires support for tier 2 argument buffers, which the current device does not have."
+ "REMeshAssetGetBlendShapeDefinitionCountForPart called with unregistered mesh asset"
+ "REMeshAssetGetBlendShapeDefinitionCountForPart groupIndex %!z(MISSING)u exceeds group count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeDefinitionCountForPart modelIndex %!z(MISSING)u exceeds model count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeDefinitionCountForPart partIndex %!z(MISSING)u exceeds part count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeDefinitionNameForPart called with unregistered mesh asset"
+ "REMeshAssetGetBlendShapeDefinitionNameForPart defIndex %!z(MISSING)u exceeds definition count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeDefinitionNameForPart groupIndex %!z(MISSING)u exceeds group count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeDefinitionNameForPart modelIndex %!z(MISSING)u exceeds model count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeDefinitionNameForPart partIndex %!z(MISSING)u exceeds part count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeOffsetsForPart %!s(MISSING)"
+ "REMeshAssetGetBlendShapeOffsetsForPart called with unregistered mesh asset"
+ "REMeshAssetGetBlendShapeOffsetsForPart defIndex %!z(MISSING)u exceeds definition count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeOffsetsForPart groupIndex %!z(MISSING)u exceeds group count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeOffsetsForPart modelIndex %!z(MISSING)u exceeds model count %!z(MISSING)u"
+ "REMeshAssetGetBlendShapeOffsetsForPart partIndex %!z(MISSING)u exceeds part count %!z(MISSING)u"
+ "REMeshSkinningPartDescriptor: incorrect number of simplifiedInfluenceEndIndices"
+ "REMeshSkinningPartDescriptor: incorrect simplified influence count"
+ "REMeshSkinningPartDescriptor: is missing simplifiedInfluenceEndIndices"
+ "RenderGraphSFBSystemShellBlurProvider"
+ "SFBSystemShellBlurContext"
+ "SetVCAPassthroughAlias"
+ "SetVCAPassthroughSRGBAlias"
+ "StencilBlurMeshNode"
+ "StencilBlurSetStencil"
+ "SyntheticColor"
+ "SyntheticDepth"
+ "T@\"REAttributeDescriptor\",R,N,V_simplifiedInfluenceEndIndices"
+ "T@\"REAttributeDescriptor\",R,N,V_simplifiedSkinningInfluences"
+ "TB,R,N,V_simplifiedPackedInfluence"
+ "TC,R,N,V_simplifiedInfluencePerVertex"
+ "Technique Sort - IsGroupedTechnique: %!d(MISSING) TechniqueGroupID: %!d(MISSING) IndexInTechniqueGroup: %!d(MISSING) TechniqueAndMaterialNameHash: %!z(MISSING)u HSRFlush: %!d(MISSING) DescriptorHash: %!z(MISSING)u MeshNameHash: %!l(MISSING)lu "
+ "UnprojectedBlurredColor"
+ "VCABlur"
+ "VCABlurAndFilterAndBlendPassthrough"
+ "VCABlurRenderTarget"
+ "VCABlurredColorSRGB"
+ "VCADepth"
+ "VCADepthStencil"
+ "VCADownsampleCompute"
+ "VCADownsampledColor"
+ "VCAStencil"
+ "VCATiledDownsampleNode"
+ "ViewportPercentsData is missing in blur pipeline. Using default values."
+ "[SFBSystemShellComputeNode] (%!s(MISSING)) Mismatching protection options for input texture %!l(MISSING)lu and output texture %!l(MISSING)lu. Skipping compute for this frame."
+ "_simplifiedInfluenceEndIndices"
+ "_simplifiedInfluencePerVertex"
+ "_simplifiedPackedInfluence"
+ "_simplifiedSkinningInfluences"
+ "applyHitTestData() - component version: %!d(MISSING)"
+ "applyHitTestData() - found activeEntity %!l(MISSING)lu - position: %!f(MISSING), %!f(MISSING), %!f(MISSING)"
+ "argumentBuffersSupport"
+ "bad_any_cast was thrown in -fno-exceptions mode"
+ "engine:BuiltinRenderGraphResources/SFBSystemShell/SFBPbrBlur.rematerial"
+ "engine:BuiltinRenderGraphResources/SFBSystemShell/SFBVCABlur.rematerial"
+ "ikRigAssetHandle"
+ "imageHeight"
+ "initWithBlendShapeData:meshPartCount:payloadBuilder:deformationModelData:"
+ "initWithMeshSkinningData:meshParts:inverseBindPoseAttributes:deformerBuilders:payloadBuilder:"
+ "initWithResourceDefinitionModel:inverseBindPoseAttributes:deformerBuilders:payloadBuilder:levels:deformationModelData:"
+ "initWithSkeletonIndexAndInfluences:packedInfluence:simplifiedPackedInfluence:influencePerVertex:simplifiedInfluencePerVertex:skinningInfluences:influenceEndIndices:simplifiedSkinningInfluences:simplifiedInfluenceEndIndices:"
+ "kernelSFBARKitPassthroughDownsample"
+ "kernelSFBBilerpDownsample4x"
+ "kernelSFBBlurAndFilter"
+ "kernelSFBNoReprojectAndNoBlend"
+ "kernelSFBReprojectAndBlendPassthrough"
+ "kernelSFBReprojectAndSRGBCorrect"
+ "kernelSFBVCABlurAndFilterAndBlendPassthrough"
+ "kernelTiledVCADownsample4x"
+ "m_solverIDs"
+ "m_solverNames"
+ "needsArgumentBufferTextureEmulation"
+ "phaseEngine:didCreatePhaseSoundEventWithMixer:mixGroupName:"
+ "realitykit::texture_private::api::custom_at"
+ "realitykit::ui_geometry_modifier_private::api::model_position_offset"
+ "realitykit::ui_geometry_modifier_private::api::position"
+ "realitykit::ui_geometry_modifier_private::api::set_model_position_offset"
+ "realitykit::ui_geometry_modifier_private::api::set_uv0"
+ "realitykit::ui_geometry_modifier_private::api::uv0"
+ "realitykit::ui_geometry_modifier_private::api::uv0_offset"
+ "realitykit::ui_geometry_modifier_private::api::uv0_transform"
+ "realitykit::ui_geometry_modifier_private::api::vertex_id"
+ "remoteObjectProxyWithErrorHandler:"
+ "reprojectFilteredBlur"
+ "reprojectVCABlur"
+ "simplifiedInfluenceEndIndices"
+ "simplifiedInfluenceEndIndices"
+ "simplifiedInfluencePerVertex"
+ "simplifiedInfluencePerVertex"
+ "simplifiedPackedInfluence"
+ "simplifiedPackedInfluence"
+ "simplifiedSkinnedAnimationJointIndices"
+ "simplifiedSkinningInfluences"
+ "simplifiedSkinningInfluences"
+ "textureCustomArray[%!d(MISSING)]"
+ "v32@?0@\"PHASEEngine\"8@\"PHASEMixer\"16@\"NSString\"24"
+ "validateWithPayloadSize:skeletonCount:vertexCount:simplifiedVertexCount:error:"
- "@44@0:8I16B20C24@28@36"
- "@88@0:8r^v16@24^v32^v40{DynamicArray<re::MeshResourceDefinition::Level>=^{Allocator}QQI^{Level}}48"
- "B48@0:8r^v16Q24Q32^@40"
- "CalculateBlendedDiffuseIBL"
- "CalculateBlendedSpecularIBL"
- "IBL Blending is not supported for multiple scenes, skip subsequent scenes."
- "Technique Sort - IsGroupedTechnique: %!d(MISSING) TechniqueGroupID: %!d(MISSING) IndexInTechniqueGroup: %!d(MISSING) TechniqueAndMaterialNameHash: %!z(MISSING)u HSRFlush: %!d(MISSING) DescriptorHash: %!z(MISSING)u MeshNameHash: %!l(MISSING)lu CreationOrder: %!d(MISSING)"
- "applyHitTestData() - found activeEntity %!l(MISSING)lu"
- "forwardDirection"
- "fsCalculateBlendedDiffuseIBL"
- "fsCalculateBlendedSpecularIBL"
- "initWithMeshSkinningData:inverseBindPoseAttributes:deformerBuilders:payloadBuilder:"
- "initWithResourceDefinitionModel:inverseBindPoseAttributes:deformerBuilders:payloadBuilder:levels:"
- "initWithSkeletonIndexAndInfluences:packedInfluence:influencePerVertex:skinningInfluences:influenceEndIndices:"
- "rotationAxis"
- "upDirection"
- "useRotationAxis"
- "useUpDirection"
- "validateWithPayloadSize:skeletonCount:vertexCount:error:"

```
