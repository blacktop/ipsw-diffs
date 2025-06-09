## AvatarKit

> `/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit`

```diff

-346.201.0.0.0
-  __TEXT.__text: 0x6f7ec
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x4e3c
-  __TEXT.__const: 0x9f8
-  __TEXT.__cstring: 0x1dc24
-  __TEXT.__oslogstring: 0x2b56
-  __TEXT.__gcc_except_tab: 0xf74
+355.1.0.0.0
+  __TEXT.__text: 0x767b0
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_methlist: 0x5444
+  __TEXT.__const: 0xa2c
+  __TEXT.__cstring: 0x1ddb2
+  __TEXT.__oslogstring: 0x2c38
+  __TEXT.__gcc_except_tab: 0x1030
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x1a50
+  __TEXT.__unwind_info: 0x1b80
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x9a1
-  __TEXT.__objc_methname: 0x101bc
-  __TEXT.__objc_methtype: 0x25f1
-  __TEXT.__objc_stubs: 0xc600
-  __DATA_CONST.__got: 0x890
-  __DATA_CONST.__const: 0x24f8
-  __DATA_CONST.__objc_classlist: 0x278
-  __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x88
+  __TEXT.__objc_classname: 0xa6d
+  __TEXT.__objc_methname: 0x10980
+  __TEXT.__objc_methtype: 0x273c
+  __TEXT.__objc_stubs: 0xc980
+  __DATA_CONST.__got: 0x920
+  __DATA_CONST.__const: 0x26b8
+  __DATA_CONST.__objc_classlist: 0x298
+  __DATA_CONST.__objc_catlist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b70
+  __DATA_CONST.__objc_selrefs: 0x3cf0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1b0
-  __DATA_CONST.__objc_arraydata: 0x625a0
-  __AUTH_CONST.__auth_got: 0x700
-  __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x249e0
-  __AUTH_CONST.__objc_const: 0xc1b0
-  __AUTH_CONST.__objc_intobj: 0x228
+  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_arraydata: 0x62590
+  __AUTH_CONST.__auth_got: 0x720
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x24880
+  __AUTH_CONST.__objc_const: 0xda60
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x7bc0
-  __AUTH_CONST.__objc_dictobj: 0x4ee08
   __AUTH_CONST.__objc_doubleobj: 0x2370
-  __AUTH.__objc_data: 0x16d0
-  __DATA.__objc_ivar: 0x9fc
-  __DATA.__data: 0x668
-  __DATA.__bss: 0xa80
+  __AUTH_CONST.__objc_dictobj: 0x4ede0
+  __AUTH.__objc_data: 0x1810
+  __DATA.__objc_ivar: 0xa28
+  __DATA.__data: 0x788
+  __DATA.__bss: 0xaa8
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/ARKit.framework/ARKit

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA
+  - /System/Library/PrivateFrameworks/VFX.framework/VFX
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67307BBC-619D-35C6-B39A-1845D9201A94
-  Functions: 2348
-  Symbols:   9005
-  CStrings:  12942
+  UUID: CDD78BC6-E451-33C0-A720-5B90445627DA
+  Functions: 2478
+  Symbols:   9429
+  CStrings:  13024
 
Symbols:
+ +[AVTAvatarPoseAnimation optimizeSceneKitAnimation:target:]
+ +[AVTMemoji skinTextureSize]
+ +[AVTMemoji skinTextureSize].cold.1
+ +[SCNTransaction(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded]
+ +[SCNTransaction(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded].cold.1
+ +[SCNTransaction(AvatarKit_CEKWorkaround) begin_CEKWorkaround]
+ +[SCNTransaction(AvatarKit_CEKWorkaround) commit_CEKWorkaround]
+ +[SCNTransaction(AvatarKit_CEKWorkaround) flush_CEKWorkaround]
+ +[SCNTransaction(AvatarKit_CEKWorkaround) setAnimationDuration_CEKWorkaround:]
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:]
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.1
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.10
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.11
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.2
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.3
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.4
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.5
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.6
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.7
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.8
+ +[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:].cold.9
+ +[VFXWorld(AVTExtensionMRR) avt_newWorldWithURL:options:error:]
+ +[VFXWorld(AVTExtensionMRR) avt_nodeNamed:forWorldAtURL:options:error:]
+ +[VFXWorld(AVTExtensionMRR) avt_rootNodeForWorldAtURL:options:error:]
+ +[VFXWorld(AVTExtensionMRR) avt_rootObjectForWorldAtURL:options:error:]
+ -[AVTARMaskRenderer encodeCompositePassWithEncoder:sceneColorTexture:sceneOnTopTexture:helper:]
+ -[AVTARMaskRenderer encodeTechniqueCommandsForRenderer:atTime:helper:]
+ -[AVTARMaskRenderer techniqueIsActive]
+ -[AVTARMaskRenderer techniqueUsesExtraRenderTargetForRenderer:pixelFormat:]
+ -[AVTARMaskRenderer techniqueUsesSpecificMainPassClearColorForRenderer:clearColor:]
+ -[AVTAnimoji updateWithOptions:]
+ -[AVTAvatar avatarSpecificTechniqueClass]
+ -[AVTAvatar newAvatarSpecificTechniqueWithRenderer:]
+ -[AVTAvatar updateWithOptions:]
+ -[AVTAvatar update].cold.1
+ -[AVTAvatar willRemoveFromWorld:]
+ -[AVTAvatarBodyPose initWithSceneKitHierarchy:]
+ -[AVTAvatarBodyPose initWithSceneKitRootJoints:]
+ -[AVTAvatarBodyPose initWithSceneKitSceneAtURL:]
+ -[AVTAvatarBodyPose initWithSceneKitSceneAtURL:].cold.1
+ -[AVTAvatarPhysicalizedPose initWithSceneKitSceneAtURL:]
+ -[AVTAvatarPhysicalizedPose initWithSceneKitSceneAtURL:].cold.1
+ -[AVTAvatarPoseAnimation _initWithSceneKitScene:usdaMetadata:identifier:]
+ -[AVTAvatarPoseAnimation initWithSceneKitScene:]
+ -[AVTAvatarPoseAnimation initWithSceneKitScene:usdaMetadata:]
+ -[AVTAvatarPoseAnimation initWithSceneKitSceneAtURL:]
+ -[AVTAvatarPoseAnimation initWithSceneKitSceneAtURL:usdaMetadata:]
+ -[AVTAvatarPoseAnimation initWithSceneKitSceneAtURL:usdaMetadata:].cold.1
+ -[AVTEyeSkinningDescriptor readMorpher]
+ -[AVTEyeSkinningDescriptor setReadMorpher:]
+ -[AVTMaterial applyToVFXMaterial:]
+ -[AVTMemoji _updateWithOptions:]
+ -[AVTMemoji updateWithOptions:]
+ -[AVTMetalHelper _locked_computePipelineStateWithFunctionName:].cold.2
+ -[AVTMorpherDrivenMaterialDescriptor readMorpher]
+ -[AVTMorpherDrivenMaterialDescriptor setReadMorpher:]
+ -[AVTPupilReflectionCorrectionDescriptor readMorpher]
+ -[AVTPupilReflectionCorrectionDescriptor setReadMorpher:]
+ -[AVTRenderer _avatarWantsSpecificTechniqueDidChange:]
+ -[AVTRenderer _customMainPassPostProcessUsesExtraRenderTargetForRenderer:pixelFormat:]
+ -[AVTRenderer _encodeCustomMainPassPostProcessForRenderer:atTime:helper:]
+ -[AVTRenderer _initWithDevice:options:isPrivateRenderer:privateRendererOwner:clearsOnDraw:]
+ -[AVTRenderer _usesSpecificMainPassClearColorForRenderer:clearColor:]
+ -[AVTRenderer _wantsCustomMainPassPostProcessForRenderer:]
+ -[AVTRenderer backgroundContentsBehindDrawable]
+ -[AVTRenderer scene]
+ -[AVTRenderer setBackgroundContentsBehindDrawable:]
+ -[AVTRenderer(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded]
+ -[AVTRenderer(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded].cold.1
+ -[AVTRendererViewTransitionTechnique encodeTechniqueCommandsForRenderer:atTime:helper:]
+ -[AVTRendererViewTransitionTechnique initWithWorldRenderer:]
+ -[AVTRendererViewTransitionTechnique initWithWorldRenderer:].cold.1
+ -[AVTRendererViewTransitionTechnique techniqueIsActive]
+ -[AVTRendererViewTransitionTechnique techniqueUsesExtraRenderTargetForRenderer:pixelFormat:]
+ -[AVTRendererViewTransitionTechnique techniqueUsesSpecificMainPassClearColorForRenderer:clearColor:]
+ -[AVTRenderer_CEKWorkaround pointOfView]
+ -[AVTRenderer_CEKWorkaround scene]
+ -[AVTStickerConfiguration loadIfNeeded].cold.1
+ -[AVTView _avatarWantsSpecificTechniqueDidChange:]
+ -[AVTView _customMainPassPostProcessUsesExtraRenderTargetForRenderer:pixelFormat:]
+ -[AVTView _defaultBackgroundColor]
+ -[AVTView _drawWithUpdate:]
+ -[AVTView _encodeCustomMainPassPostProcessForRenderer:atTime:helper:]
+ -[AVTView _renderer:willRenderWorld:atTime:]
+ -[AVTView _usesSpecificMainPassClearColorForRenderer:clearColor:]
+ -[AVTView _wantsCustomMainPassPostProcessForRenderer:]
+ -[AVTView backgroundContentsBehindDrawable]
+ -[AVTView scene]
+ -[AVTView setBackgroundContentsBehindDrawable:]
+ -[VFXCamera(AVTExtension) avt_setSimdPostProjectionTransform:]
+ -[VFXCamera(AVTExtension) avt_setSimdProjectionTransform:]
+ -[VFXCamera(AVTExtension) avt_simdPostProjectionTransform]
+ -[VFXCamera(AVTExtension) avt_simdProjectionTransform]
+ -[VFXCamera(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded]
+ -[VFXCamera(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded].cold.1
+ -[VFXCamera_CEKWorkaround focalLength]
+ -[VFXCamera_CEKWorkaround sensorHeight]
+ -[VFXCamera_CEKWorkaround setFocalLength:]
+ -[VFXCamera_CEKWorkaround setSensorHeight:]
+ -[VFXMaterialProperty(AVTExtension) avt_setSimdContentsTransform:]
+ -[VFXMaterialProperty(AVTExtension) avt_simdContentsTransform]
+ -[VFXMorpher(AVTExtension) avt_buildInternalSupportForCorrectivesWithBlock:]
+ -[VFXMorpher(AVTExtension) avt_buildInternalSupportForCorrectivesWithBlock:].cold.1
+ -[VFXMorpher(AVTExtension) avt_buildInternalSupportForCorrectivesWithBlock:].cold.2
+ -[VFXMorpher(AVTExtension) avt_buildInternalSupportForCorrectivesWithBlock:].cold.3
+ -[VFXMorpher(AVTExtension) avt_buildInternalSupportForCorrectivesWithBlock:].cold.4
+ -[VFXMorpher(AVTExtension) avt_buildInternalSupportForCorrectivesWithBlock:].cold.5
+ -[VFXMorpher(AVTExtension) avt_buildInternalSupportForCorrectivesWithBlock:].cold.6
+ -[VFXNode(AVTExtension) avt_enableSubdivisionOnHierarchyWithQuality:animoji:]
+ -[VFXNode(AVTExtension) avt_enableSubdivisionOnHierarchyWithQuality:animoji:].cold.1
+ -[VFXNode(AVTExtension) avt_enableSubdivisionOnHierarchyWithQuality:animoji:].cold.2
+ -[VFXNode(AVTExtension) avt_setGeometryPrimitiveRangesFromFaceIndexRanges:]
+ -[VFXNode(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded]
+ -[VFXNode(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded].cold.1
+ -[VFXNode_CEKWorkaround camera]
+ -[VFXRenderer(AVTWorldRenderer) avt_simdProjectPoint:]
+ -[VFXRenderer(AVTWorldRenderer) avt_simdUnprojectPoint:]
+ -[VFXSkinner(AVTExtension) avt_setSimdBaseMeshBindTransform:]
+ -[VFXSkinner(AVTExtension) avt_simdBaseGeometryBindTransform]
+ -[VFXView(AVTExtension) avt_simdViewport]
+ -[VFXView(AVTWorldRenderer) avt_simdProjectPoint:]
+ -[VFXView(AVTWorldRenderer) avt_simdUnprojectPoint:]
+ -[VFXWorld(AVTExtension) avt_fixQuirksOfNewUSDSchemaWithOptions:handler:]
+ -[VFXWorld(AVTExtension) avt_removeDuplicateSkeletonRootWithHandler:]
+ -[VFXWorld(AVTExtension) avt_removeDuplicateSkeletonRootWithHandler:].cold.1
+ -[VFXWorld(AVTExtension) avt_removeFaceSetsExportedAsDummyNodesWithHandler:]
+ -[VFXWorld(AVTExtension) avt_setInitialValuesExportedAsAnimationsWithWithOptions:handler:]
+ -[VFXWorld(AVTExtensionMRR) avt_init]
+ -[VFXWorld(AVTExtensionMRR) avt_writeByArchivingRootNodeInsteadOfScene:toURL:options:error:]
+ -[VFXWorld(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded]
+ -[VFXWorld(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded].cold.1
+ GCC_except_table105
+ GCC_except_table113
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table132
+ GCC_except_table147
+ GCC_except_table172
+ GCC_except_table187
+ GCC_except_table193
+ GCC_except_table203
+ GCC_except_table40
+ GCC_except_table50
+ GCC_except_table55
+ GCC_except_table65
+ GCC_except_table72
+ GCC_except_table85
+ GCC_except_table97
+ _AVTAvatarSpringSpecializationTarget
+ _AVTAvatarWantsSpecificTechniqueDidChangeNotificationName
+ _AVTCloneSceneKitNodesAndMaterials
+ _AVTFixMaterialsContainingSceneKitShaderModifiersInVFXNodeHierarchy
+ _AVTFixVFXShaderModifierFromSCNShaderModifier
+ _AVTFixVFXShaderModifiersFromSCNShaderModifiers
+ _AVTMergeSceneKitShaderModifiers
+ _AVTMergeSceneKitShaderModifiersForEntryPoint
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithCodeAndParts
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithCodeAndParts.cold.1
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithCodeAndParts.cold.2
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndCode
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndCode.cold.1
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndCode.cold.2
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndCode.cold.3
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndParts
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndParts.cold.1
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndParts.cold.2
+ _AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndParts.cold.3
+ _AVTPrecompiledStickerPackPlist.onceToken.1819
+ _AVTPrecompiledStickerPackPlist.onceToken.1822
+ _AVTPrecompiledStickerPackPlist.onceToken.2186
+ _AVTPrecompiledStickerPackPlist.onceToken.2189
+ _AVTPrecompiledStickerPackPlist.onceToken.2205
+ _AVTPrecompiledStickerPackPlist.onceToken.2208
+ _AVTPrecompiledStickerPackPlist.onceToken.2224
+ _AVTPrecompiledStickerPackPlist.onceToken.2227
+ _AVTPrecompiledStickerPackPlist.onceToken.2249
+ _MTLPixelFormatGetInfoForDevice
+ _NSClassFromString
+ _OBJC_CLASS_$_AVTRenderer_CEKWorkaround
+ _OBJC_CLASS_$_VFXAnimation
+ _OBJC_CLASS_$_VFXAnimationEvent
+ _OBJC_CLASS_$_VFXAnimationPlayer
+ _OBJC_CLASS_$_VFXCamera
+ _OBJC_CLASS_$_VFXCamera_CEKWorkaround
+ _OBJC_CLASS_$_VFXKeyedArchiver
+ _OBJC_CLASS_$_VFXKeyedUnarchiver
+ _OBJC_CLASS_$_VFXMaterialProperty
+ _OBJC_CLASS_$_VFXMesh
+ _OBJC_CLASS_$_VFXMeshSource
+ _OBJC_CLASS_$_VFXModelTessellator
+ _OBJC_CLASS_$_VFXModelWrapDeformer
+ _OBJC_CLASS_$_VFXModelWrapDeformerParameters
+ _OBJC_CLASS_$_VFXMorpher
+ _OBJC_CLASS_$_VFXNode
+ _OBJC_CLASS_$_VFXNode_CEKWorkaround
+ _OBJC_CLASS_$_VFXParametricModel
+ _OBJC_CLASS_$_VFXPhysicsBody
+ _OBJC_CLASS_$_VFXPhysicsConeTwistJoint
+ _OBJC_CLASS_$_VFXPhysicsShape
+ _OBJC_CLASS_$_VFXRenderer
+ _OBJC_CLASS_$_VFXSkinner
+ _OBJC_CLASS_$_VFXTransaction
+ _OBJC_CLASS_$_VFXView
+ _OBJC_CLASS_$_VFXWorld
+ _OBJC_CLASS_$_VFXWorld_CEKWorkaround
+ _OBJC_IVAR_$_AVTARMaskRenderer._compositeLegacyPipelineState
+ _OBJC_IVAR_$_AVTARMaskRenderer._compositeMattePipelineState
+ _OBJC_IVAR_$_AVTARMaskRenderer._compositeMatteWithChromaKeyPipelineState
+ _OBJC_IVAR_$_AVTARMaskRenderer._debugCamDepthTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._debugIntermediateTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._generatedMasksTexture
+ _OBJC_IVAR_$_AVTCompositorTextureProvider._lastRenderedTexture
+ _OBJC_IVAR_$_AVTEyeSkinningDescriptor._readMorpher
+ _OBJC_IVAR_$_AVTMorpherDrivenMaterialDescriptor._readMorpher
+ _OBJC_IVAR_$_AVTPupilReflectionCorrectionDescriptor._readMorpher
+ _OBJC_IVAR_$_AVTRenderer._avtRendererTechniquePresentationTree
+ _OBJC_IVAR_$_AVTRenderer._backgroundContentsBehindDrawable
+ _OBJC_IVAR_$_AVTRendererViewTransitionTechnique._renderPassDescriptor
+ _OBJC_IVAR_$_AVTRendererViewTransitionTechnique._renderPipelineState
+ _OBJC_IVAR_$_AVTSpringDynamic._targetPresentationNode
+ _OBJC_IVAR_$_AVTView._avtRendererTechniquePresentationTree
+ _OBJC_IVAR_$_AVTView._backgroundContentsBehindDrawable
+ _OBJC_METACLASS_$_AVTRenderer_CEKWorkaround
+ _OBJC_METACLASS_$_VFXCamera
+ _OBJC_METACLASS_$_VFXCamera_CEKWorkaround
+ _OBJC_METACLASS_$_VFXNode
+ _OBJC_METACLASS_$_VFXNode_CEKWorkaround
+ _OBJC_METACLASS_$_VFXRenderer
+ _OBJC_METACLASS_$_VFXView
+ _OBJC_METACLASS_$_VFXWorld
+ _OBJC_METACLASS_$_VFXWorld_CEKWorkaround
+ _OUTLINED_FUNCTION_9
+ _SCNSceneExportCompressGeometryElements
+ _SCNSceneExportCompressMorphTargets
+ _VFXGetPerformanceStatistics
+ _VFXGetShaderCollectionOutputURL
+ _VFXMeshSourceSemanticBoneIndices
+ _VFXMeshSourceSemanticBoneWeights
+ _VFXMeshSourceSemanticPosition
+ _VFXSetPerformanceStatisticsEnabled
+ _VFXSetShaderCollectionEnabled
+ _VFXShaderModifierEntryPointFragment
+ _VFXShaderModifierEntryPointLighting
+ _VFXShaderModifierEntryPointSurface
+ _VFXShaderModifierEntryPointVertex
+ _VFXWorldExportCompressMeshElements
+ _VFXWorldExportCompressMorphTargets
+ _VFXWorldLoaderDisableVFXCoreSupport
+ __AVTAvatarPoseImportSceneKitAnimation
+ __AVTAvatarPoseImportSceneKitAnimation.cold.1
+ __AVTAvatarPoseImportSceneKitAnimation.cold.2
+ __AVTAvatarPoseImportSceneKitAnimation.cold.3
+ __AVTAvatarPoseImportSceneKitAnimation.cold.4
+ __AVTUpgradeVFXWorldOptions
+ __OBJC_$_CATEGORY_CLASS_METHODS_SCNTransaction_$_AvatarKit_CEKWorkaround
+ __OBJC_$_CATEGORY_CLASS_METHODS_VFXSkinner_$_AVTExtension
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_VFXMaterialProperty_$_AVTExtension
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_VFXMorpher_$_AVTExtension
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_VFXRenderer_$_AVTWorldRenderer
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_VFXSkinner_$_AVTExtension
+ __OBJC_$_CATEGORY_SCNTransaction_$_AvatarKit_CEKWorkaround
+ __OBJC_$_CATEGORY_VFXCamera_$_AvatarKit_CEKWorkaround
+ __OBJC_$_CATEGORY_VFXMaterialProperty_$_AVTExtension
+ __OBJC_$_CATEGORY_VFXMorpher_$_AVTExtension
+ __OBJC_$_CATEGORY_VFXNode_$_AvatarKit_CEKWorkaround
+ __OBJC_$_CATEGORY_VFXRenderer_$_AVTWorldRenderer
+ __OBJC_$_CATEGORY_VFXSkinner_$_AVTExtension
+ __OBJC_$_CATEGORY_VFXView_$_AVTWorldRenderer
+ __OBJC_$_CATEGORY_VFXWorld_$_AvatarKit_CEKWorkaround
+ __OBJC_$_CLASS_METHODS_AVTRenderer(AvatarKit_CEKWorkaround|CameraEffectsKit)
+ __OBJC_$_CLASS_METHODS_VFXWorld(AvatarKit_CEKWorkaround|AVTExtensionMRR|AVTExtension)
+ __OBJC_$_INSTANCE_METHODS_AVTRenderer(AvatarKit_CEKWorkaround|CameraEffectsKit)
+ __OBJC_$_INSTANCE_METHODS_AVTRenderer_CEKWorkaround
+ __OBJC_$_INSTANCE_METHODS_VFXCamera(AvatarKit_CEKWorkaround|AVTExtension)
+ __OBJC_$_INSTANCE_METHODS_VFXCamera_CEKWorkaround
+ __OBJC_$_INSTANCE_METHODS_VFXNode(AvatarKit_CEKWorkaround|AVTExtension)
+ __OBJC_$_INSTANCE_METHODS_VFXNode_CEKWorkaround
+ __OBJC_$_INSTANCE_METHODS_VFXView(AVTWorldRenderer|AVTExtension)
+ __OBJC_$_INSTANCE_METHODS_VFXWorld(AvatarKit_CEKWorkaround|AVTExtensionMRR|AVTExtension)
+ __OBJC_$_PROP_LIST_VFXMaterialProperty_$_AVTExtension
+ __OBJC_$_PROP_LIST_VFXWorldRenderer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVTWorldRenderer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VFXWorldRendererDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__VFXWorldRendererDelegateSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VFXMaterialPropertyTextureProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VFXWorldRenderer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__VFXWorldCommandBufferStatusMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__VFXWorldRendererMainPassCustomPostProcessSupport
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__VFXWorldRendererResourceManagerMonitor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVTWorldRenderer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VFXMaterialPropertyTextureProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VFXWorldRenderer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VFXWorldRendererDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__VFXWorldCommandBufferStatusMonitor
+ __OBJC_$_PROTOCOL_METHOD_TYPES__VFXWorldRendererDelegateSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES__VFXWorldRendererMainPassCustomPostProcessSupport
+ __OBJC_$_PROTOCOL_METHOD_TYPES__VFXWorldRendererResourceManagerMonitor
+ __OBJC_$_PROTOCOL_REFS_AVTRendererTechnique
+ __OBJC_$_PROTOCOL_REFS_AVTWorldRenderer
+ __OBJC_$_PROTOCOL_REFS_VFXMaterialPropertyTextureProvider
+ __OBJC_$_PROTOCOL_REFS_VFXWorldRenderer
+ __OBJC_$_PROTOCOL_REFS_VFXWorldRendererDelegate
+ __OBJC_$_PROTOCOL_REFS__VFXWorldCommandBufferStatusMonitor
+ __OBJC_$_PROTOCOL_REFS__VFXWorldRendererDelegateSPI
+ __OBJC_$_PROTOCOL_REFS__VFXWorldRendererMainPassCustomPostProcessSupport
+ __OBJC_$_PROTOCOL_REFS__VFXWorldRendererResourceManagerMonitor
+ __OBJC_CLASS_RO_$_AVTRenderer_CEKWorkaround
+ __OBJC_CLASS_RO_$_VFXCamera_CEKWorkaround
+ __OBJC_CLASS_RO_$_VFXNode_CEKWorkaround
+ __OBJC_CLASS_RO_$_VFXWorld_CEKWorkaround
+ __OBJC_LABEL_PROTOCOL_$_AVTWorldRenderer
+ __OBJC_LABEL_PROTOCOL_$_VFXMaterialPropertyTextureProvider
+ __OBJC_LABEL_PROTOCOL_$_VFXWorldRenderer
+ __OBJC_LABEL_PROTOCOL_$_VFXWorldRendererDelegate
+ __OBJC_LABEL_PROTOCOL_$__VFXWorldCommandBufferStatusMonitor
+ __OBJC_LABEL_PROTOCOL_$__VFXWorldRendererDelegateSPI
+ __OBJC_LABEL_PROTOCOL_$__VFXWorldRendererMainPassCustomPostProcessSupport
+ __OBJC_LABEL_PROTOCOL_$__VFXWorldRendererResourceManagerMonitor
+ __OBJC_METACLASS_RO_$_AVTRenderer_CEKWorkaround
+ __OBJC_METACLASS_RO_$_VFXCamera_CEKWorkaround
+ __OBJC_METACLASS_RO_$_VFXNode_CEKWorkaround
+ __OBJC_METACLASS_RO_$_VFXWorld_CEKWorkaround
+ __OBJC_PROTOCOL_$_AVTWorldRenderer
+ __OBJC_PROTOCOL_$_VFXMaterialPropertyTextureProvider
+ __OBJC_PROTOCOL_$_VFXWorldRenderer
+ __OBJC_PROTOCOL_$_VFXWorldRendererDelegate
+ __OBJC_PROTOCOL_$__VFXWorldCommandBufferStatusMonitor
+ __OBJC_PROTOCOL_$__VFXWorldRendererDelegateSPI
+ __OBJC_PROTOCOL_$__VFXWorldRendererMainPassCustomPostProcessSupport
+ __OBJC_PROTOCOL_$__VFXWorldRendererResourceManagerMonitor
+ __VFXSetShaderCacheURL
+ ___130-[AVTAvatar _transitionFromPose:toPose:bakedAnimationBlendFactor:duration:delay:timingFunction:timingAnimation:completionHandler:]_block_invoke.266
+ ___145-[AVTAvatarPoseAnimation _addAnimationToAvatar:options:transitionInDuration:transitionOutDuration:isTransient:completionQueue:completionHandler:]_block_invoke.128
+ ___28+[AVTMemoji skinTextureSize]_block_invoke
+ ___32-[AVTMemoji _updateWithOptions:]_block_invoke
+ ___32-[AVTMemoji _updateWithOptions:]_block_invoke_2
+ ___34-[AVTMaterial applyToVFXMaterial:]_block_invoke
+ ___35-[AVTView setAvtRendererTechnique:]_block_invoke
+ ___39-[AVTRenderer setAvtRendererTechnique:]_block_invoke
+ ___44-[AVTView _renderer:willRenderWorld:atTime:]_block_invoke
+ ___47-[AVTAvatar updateEyeOrientationAndReflections]_block_invoke
+ ___47-[AVTAvatar updateEyeOrientationAndReflections]_block_invoke_2
+ ___47-[AVTAvatarBodyPose initWithSceneKitHierarchy:]_block_invoke
+ ___48-[AVTAvatarBodyPose initWithSceneKitRootJoints:]_block_invoke
+ ___48-[AVTAvatarBodyPose initWithSceneKitRootJoints:]_block_invoke_2
+ ___50-[AVTMemoji initWithDescriptor:usageIntent:error:]_block_invoke.242
+ ___55-[AVTAvatar updateMorpherDrivenMaterialsWithDeltaTime:]_block_invoke
+ ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.309
+ ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.309.cold.1
+ ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.334
+ ___67-[AVTMemoji addDerivedNodesMatchingStickerPattern:toArray:options:]_block_invoke.364
+ ___69-[VFXWorld(AVTExtension) avt_removeDuplicateSkeletonRootWithHandler:]_block_invoke
+ ___69-[VFXWorld(AVTExtension) avt_removeDuplicateSkeletonRootWithHandler:]_block_invoke.cold.1
+ ___73-[AVTAvatarPoseAnimation _initWithSceneKitScene:usdaMetadata:identifier:]_block_invoke
+ ___74+[SCNTransaction(AvatarKit_CEKWorkaround) _implementCEKWorkaroundIfNeeded]_block_invoke
+ ___75-[VFXNode(AVTExtension) avt_setGeometryPrimitiveRangesFromFaceIndexRanges:]_block_invoke
+ ___76-[VFXMorpher(AVTExtension) avt_buildInternalSupportForCorrectivesWithBlock:]_block_invoke
+ ___76-[VFXWorld(AVTExtension) avt_removeFaceSetsExportedAsDummyNodesWithHandler:]_block_invoke
+ ___77-[VFXNode(AVTExtension) avt_enableSubdivisionOnHierarchyWithQuality:animoji:]_block_invoke
+ ___77-[VFXNode(AVTExtension) avt_enableSubdivisionOnHierarchyWithQuality:animoji:]_block_invoke_2
+ ___77-[VFXNode(AVTExtension) avt_enableSubdivisionOnHierarchyWithQuality:animoji:]_block_invoke_3
+ ___90-[VFXWorld(AVTExtension) avt_setInitialValuesExportedAsAnimationsWithWithOptions:handler:]_block_invoke
+ ___92+[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:]_block_invoke
+ ___92+[VFXSkinner(AVTExtension) avt_skinnerByInterpolatingFromSkinner:toSkinner:factor:skeleton:]_block_invoke_2
+ ___92-[SCNScene(AVTExtensionMRR) avt_writeByArchivingRootNodeInsteadOfScene:toURL:options:error:]_block_invoke
+ ___92-[SCNScene(AVTExtensionMRR) avt_writeByArchivingRootNodeInsteadOfScene:toURL:options:error:]_block_invoke_2
+ ___AVTFixMaterialsContainingSceneKitShaderModifiersInVFXNodeHierarchy_block_invoke
+ ___AVTFixVFXShaderModifiersFromSCNShaderModifiers_block_invoke
+ ____AVTAvatarPoseImportSceneKitAnimation_block_invoke
+ ____AVTAvatarPoseImportSceneKitAnimation_block_invoke.249
+ ___block_descriptor_124_e8_32s40s48s56s64s72s80s88bs96r104w_e52_v48?0"AVTAvatar"8d16d24"<VFXWorldRenderer>"32^B40ls32l8s40l8r96l8s48l8s56l8s64l8s72l8s80l8w104l8s88l8
+ ___block_descriptor_32_e17_v16?0"VFXNode"8l
+ ___block_descriptor_32_e21_v24?0"VFXNode"8^B16l
+ ___block_descriptor_32_e40_B24?0"<AVTAvatarDynamic>"8"VFXNode"16l
+ ___block_descriptor_32_e51_v24?0"VFXAnimation"8?<v?"NSString""NSData">16l
+ ___block_descriptor_32_e56_B24?0"AVTMorpherDrivenMaterialDescriptor"8"VFXNode"16l
+ ___block_descriptor_32_e57_v24?0"VFXAnimation"8?<v?"NSString""NSDictionary">16l
+ ___block_descriptor_33_e21_v24?0"VFXNode"8^B16l
+ ___block_descriptor_34_e21_v24?0"VFXNode"8^B16l
+ ___block_descriptor_40_e63_v40?0"CABasicAnimation"8"NSString"16"<VFXAnimatable>"24^?32l
+ ___block_descriptor_40_e8_32bs_e21_v24?0"VFXNode"8^B16ls32l8
+ ___block_descriptor_40_e8_32r_e21_v24?0"VFXNode"8^B16lr32l8
+ ___block_descriptor_40_e8_32r_e39_v32?0"NSString"8"VFXAnimation"16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e10_v16?0r^v8ls32l8
+ ___block_descriptor_40_e8_32s_e114_v40?0"<MTLComputeCommandEncoder>"8"<VFXMaterialPropertyTextureProviderHelper>"16"AVTMemoji"24"NSMutableSet"32ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"VFXNode"8ls32l8
+ ___block_descriptor_40_e8_32s_e21_B24?0"VFXNode"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e21_v24?0"VFXNode"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e24_B32?0"VFXMesh"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e24_B32?0"VFXNode"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e24_v32?0"VFXMesh"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e28_B32?0"VFXMaterial"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e28_v32?0"VFXMaterial"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e31_v32?0"VFXMeshElement"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e34_v32?0"AVTMemoji"8"VFXNode"16Q24ls32l8
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"VFXNode"16^B24ls32l8
+ ___block_descriptor_41_e21_v24?0"VFXNode"8^B16l
+ ___block_descriptor_41_e8_32s_e17_v16?0"VFXNode"8ls32l8
+ ___block_descriptor_41_e8_32s_e21_v24?0"VFXNode"8^B16ls32l8
+ ___block_descriptor_44_e8_32s_e21_v24?0"VFXNode"8^B16ls32l8
+ ___block_descriptor_48_e8_32bs_e21_v24?0"VFXNode"8^B16ls32l8
+ ___block_descriptor_48_e8_32r_e17_v16?0"VFXNode"8lr32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v28?0"<VFXAnimation>"816B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e39_v32?0"NSString"8"VFXAnimation"16^B24ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e21_v24?0"VFXNode"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e37_v32?0"NSString"8"VFXSkinner"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e114_v40?0"<MTLComputeCommandEncoder>"8"<VFXMaterialPropertyTextureProviderHelper>"16"AVTMemoji"24"NSMutableSet"32ls32l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"VFXNode"8ls32l8
+ ___block_descriptor_48_e8_32s_e21_v24?0"VFXNode"8^B16ls32l8
+ ___block_descriptor_48_e8_32s_e30_v28?0"<VFXAnimation>"816B24ls32l8
+ ___block_descriptor_52_e8_32s40s_e21_v24?0"VFXNode"8^B16ls32l8s40l8
+ ___block_descriptor_56_e52_v48?0"AVTAvatar"8d16d24"<VFXWorldRenderer>"32^B40l
+ ___block_descriptor_56_e8_32s40bs48r_e21_v24?0"VFXNode"8^B16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e35_v32?0"NSString"8"NSString"16^B24lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v28?0"<VFXAnimation>"816B24ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e24_v32?0"VFXMesh"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e114_v40?0"<MTLComputeCommandEncoder>"8"<VFXMaterialPropertyTextureProviderHelper>"16"AVTMemoji"24"NSMutableSet"32ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e21_v24?0"VFXNode"8^B16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e34_v32?0"NSString"8"VFXNode"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e52_v48?0"AVTAvatar"8d16d24"<VFXWorldRenderer>"32^B40ls32l8s40l8
+ ___block_descriptor_56_e8_32s_e114_v40?0"<MTLComputeCommandEncoder>"8"<VFXMaterialPropertyTextureProviderHelper>"16"AVTMemoji"24"NSMutableSet"32ls32l8
+ ___block_descriptor_56_e8_32s_e21_v24?0"VFXNode"8^B16ls32l8
+ ___block_descriptor_56_e8_32s_e35_v32?0"VFXMesh"8f16"VFXMesh"20f28ls32l8
+ ___block_descriptor_60_e8_32s40s48bs_e21_v24?0"VFXNode"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40s48r_e35_v32?0"VFXMesh"8f16"VFXMesh"20f28lr48l8s32l8s40l8
+ ___block_descriptor_60_e8_32s40s48s_e21_v24?0"VFXNode"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40s48s_e24_v32?0"VFXMesh"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48o_e25_v32?0"NSString"816^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e24_v32?0"VFXMesh"8Q16^B24ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s_e24_v32?0"VFXMesh"8Q16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s_e67_v48?0"VFXNode"8"NSString"16"NSString"24"NSValue"32"NSValue"40ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56s_e21_v24?0"VFXNode"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s_e21_v24?0"VFXNode"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e52_v48?0"AVTAvatar"8d16d24"<VFXWorldRenderer>"32^B40ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s_e21_v24?0"VFXNode"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e21_v24?0"VFXNode"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e21_v24?0"VFXNode"8^B16ls32l8s40l8r72l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72w_e52_v48?0"AVTAvatar"8d16d24"<VFXWorldRenderer>"32^B40ls32l8s40l8w72l8s48l8s56l8s64l8
+ ___block_descriptor_92_e8_32s40s48s56s64bs72w_e52_v48?0"AVTAvatar"8d16d24"<VFXWorldRenderer>"32^B40ls32l8s40l8w72l8s48l8s56l8s64l8
+ ___block_literal_global.176
+ ___block_literal_global.1821
+ ___block_literal_global.1824
+ ___block_literal_global.209
+ ___block_literal_global.2188
+ ___block_literal_global.2191
+ ___block_literal_global.2207
+ ___block_literal_global.2210
+ ___block_literal_global.2226
+ ___block_literal_global.2229
+ ___block_literal_global.2251
+ ___block_literal_global.253
+ ___block_literal_global.358
+ ___block_literal_global.40
+ ___block_literal_global.42
+ ___block_literal_global.539
+ ___block_literal_global.541
+ ___block_literal_global.94
+ __implementCEKWorkaroundIfNeeded.onceToken
+ _class_getClassMethod
+ _method_exchangeImplementations
+ _objc_msgSend$VFXFloat3Value
+ _objc_msgSend$VFXFloat4Value
+ _objc_msgSend$_defaultBackgroundColor
+ _objc_msgSend$_implementCEKWorkaroundIfNeeded
+ _objc_msgSend$_initWithSceneKitScene:usdaMetadata:identifier:
+ _objc_msgSend$_presentationWeightForTargetAtIndex:token:
+ _objc_msgSend$_renderCommandEncoderWithCommandBuffer:renderTarget:shouldClear:clearColor:
+ _objc_msgSend$_updateWithOptions:
+ _objc_msgSend$addPhysicsJoint:
+ _objc_msgSend$allObjects
+ _objc_msgSend$animationPlayerWithAnimation:
+ _objc_msgSend$applyToVFXMaterial:
+ _objc_msgSend$avatarSpecificTechniqueClass
+ _objc_msgSend$avt_nodeNamed:forWorldAtURL:options:error:
+ _objc_msgSend$avt_rootNodeForWorldAtURL:options:error:
+ _objc_msgSend$avt_rootObjectForWorldAtURL:options:error:
+ _objc_msgSend$avt_setSimdBaseMeshBindTransform:
+ _objc_msgSend$avt_writeByArchivingRootNodeInsteadOfScene:toURL:options:error:
+ _objc_msgSend$baseMesh
+ _objc_msgSend$baseMeshBindTransform
+ _objc_msgSend$begin_CEKWorkaround
+ _objc_msgSend$blendMode
+ _objc_msgSend$clock
+ _objc_msgSend$commit_CEKWorkaround
+ _objc_msgSend$compact
+ _objc_msgSend$convertPosition:fromNode:
+ _objc_msgSend$convertPosition:toNode:
+ _objc_msgSend$convertTransform:fromNode:
+ _objc_msgSend$convertVector:fromNode:
+ _objc_msgSend$convertVector:toNode:
+ _objc_msgSend$deformers
+ _objc_msgSend$destinationTexture
+ _objc_msgSend$drawSceneBackgroundUsingEncoder:commandBuffer:renderPassDescriptor:
+ _objc_msgSend$encodeCompositePassWithEncoder:sceneColorTexture:sceneOnTopTexture:helper:
+ _objc_msgSend$encodeTechniqueCommandsForRenderer:atTime:helper:
+ _objc_msgSend$eulerAngles
+ _objc_msgSend$flush_CEKWorkaround
+ _objc_msgSend$grain
+ _objc_msgSend$initWithSceneKitHierarchy:
+ _objc_msgSend$initWithSceneKitRootJoints:
+ _objc_msgSend$initWithSceneKitSceneAtURL:
+ _objc_msgSend$initWithSceneKitSceneAtURL:usdaMetadata:
+ _objc_msgSend$initWithWorldRenderer:
+ _objc_msgSend$mainPassColorTextureAtIndex:
+ _objc_msgSend$mesh
+ _objc_msgSend$meshElements
+ _objc_msgSend$meshSourceChannels
+ _objc_msgSend$meshSourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:
+ _objc_msgSend$meshSources
+ _objc_msgSend$meshWithSources:elements:
+ _objc_msgSend$meshWithSources:elements:sourceChannels:
+ _objc_msgSend$model
+ _objc_msgSend$modelElements
+ _objc_msgSend$newAvatarSpecificTechniqueWithRenderer:
+ _objc_msgSend$nodeWithModel:
+ _objc_msgSend$optimizeSceneKitAnimation:target:
+ _objc_msgSend$orientation
+ _objc_msgSend$performPresentationObjectQueriesInWorld:usingBlock:
+ _objc_msgSend$removePhysicsJoint:
+ _objc_msgSend$renderCommandEncoder
+ _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
+ _objc_msgSend$setAnimationDuration_CEKWorkaround:
+ _objc_msgSend$setBaseMeshBindTransform:
+ _objc_msgSend$setBlendMode:
+ _objc_msgSend$setColored:
+ _objc_msgSend$setDeformers:
+ _objc_msgSend$setEulerAngles:
+ _objc_msgSend$setFilmOffset:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setMesh:
+ _objc_msgSend$setModel:
+ _objc_msgSend$setOrientation:
+ _objc_msgSend$setPhysicsShape:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setShadingModel:
+ _objc_msgSend$setSlice:
+ _objc_msgSend$setTime:
+ _objc_msgSend$setTimeOrigin:
+ _objc_msgSend$setTimeSource:
+ _objc_msgSend$setWorld:
+ _objc_msgSend$setWorldTransform:
+ _objc_msgSend$set_wantsWorldRendererDelegationMessages:
+ _objc_msgSend$shapeWithModel:
+ _objc_msgSend$skinnerWithBaseMesh:bones:boneInverseBindTransforms:boneWeights:boneIndices:
+ _objc_msgSend$snapshotWithSize:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$techniqueIsActive
+ _objc_msgSend$techniqueUsesExtraRenderTargetForRenderer:pixelFormat:
+ _objc_msgSend$techniqueUsesSpecificMainPassClearColorForRenderer:clearColor:
+ _objc_msgSend$time
+ _objc_msgSend$updateWithOptions:
+ _objc_msgSend$valueWithVFXFloat3:
+ _objc_msgSend$valueWithVFXFloat4:
+ _objc_msgSend$vfx_compressedDataUsingCompressionAlgorithm:
+ _objc_msgSend$vfx_uncompressedDataUsingCompressionAlgorithm:
+ _objc_msgSend$willRemoveFromWorld:
+ _objc_msgSend$world
+ _objc_msgSend$worldPosition
+ _objc_msgSend$worldTransform
+ _objc_msgSend$worldWithSceneKitScene:options:
+ _objc_msgSend$worldWithURL:options:error:
+ _objc_msgSend$writeToURL:options:progressHandler:
+ _object_setClass
- +[AVTAvatarPoseAnimation optimizeAnimation:target:]
- -[AVTARMaskRenderer technique]
- -[AVTAnimoji update]
- -[AVTAvatar setupEyeOrientationAndReflections].cold.3
- -[AVTAvatar updateEyeOrientationAndReflections].cold.1
- -[AVTAvatar updateEyeOrientationAndReflections].cold.2
- -[AVTAvatar updateMorpherDrivenMaterialsWithDeltaTime:].cold.1
- -[AVTAvatar willRemoveFromScene:]
- -[AVTAvatarBodyPose initWithHierarchy:]
- -[AVTAvatarBodyPose initWithRootJoints:]
- -[AVTAvatarBodyPose initWithSceneAtURL:]
- -[AVTAvatarBodyPose initWithSceneAtURL:].cold.1
- -[AVTAvatarPhysicalizedPose initWithSceneAtURL:]
- -[AVTAvatarPhysicalizedPose initWithSceneAtURL:].cold.1
- -[AVTAvatarPoseAnimation _initWithScene:usdaMetadata:identifier:]
- -[AVTAvatarPoseAnimation initWithScene:]
- -[AVTAvatarPoseAnimation initWithScene:usdaMetadata:]
- -[AVTAvatarPoseAnimation initWithSceneAtURL:]
- -[AVTAvatarPoseAnimation initWithSceneAtURL:usdaMetadata:]
- -[AVTAvatarPoseAnimation initWithSceneAtURL:usdaMetadata:].cold.1
- -[AVTEyeSkinningDescriptor readMorpherNode]
- -[AVTEyeSkinningDescriptor setReadMorpherNode:]
- -[AVTMaterial applyToSceneKitMaterial:]
- -[AVTMemoji _update]
- -[AVTMemoji morphTo:]
- -[AVTMemoji skinTextureSize]
- -[AVTMemoji skinTextureSize].cold.1
- -[AVTMemoji update]
- -[AVTPupilReflectionCorrectionDescriptor readMorpherNode]
- -[AVTPupilReflectionCorrectionDescriptor setReadMorpherNode:]
- -[AVTRenderer _initWithOptions:isPrivateRenderer:privateRendererOwner:clearsOnDraw:context:renderingAPI:]
- -[AVTRenderer setTechnique:]
- -[AVTRenderer setTechnique:].cold.1
- -[AVTRenderer technique]
- -[AVTRenderer technique].cold.1
- -[AVTRendererViewTransitionTechnique initWithSceneRenderer:]
- -[AVTRendererViewTransitionTechnique technique]
- -[AVTView _renderer:willRenderScene:atTime:]
- -[AVTView setTechnique:]
- -[AVTView setTechnique:].cold.1
- -[AVTView technique]
- -[AVTView technique].cold.1
- GCC_except_table106
- GCC_except_table109
- GCC_except_table120
- GCC_except_table133
- GCC_except_table140
- GCC_except_table173
- GCC_except_table180
- GCC_except_table186
- GCC_except_table204
- GCC_except_table23
- GCC_except_table39
- GCC_except_table49
- GCC_except_table70
- GCC_except_table92
- _AVTPrecompiledStickerPackPlist.onceToken.1813
- _AVTPrecompiledStickerPackPlist.onceToken.1816
- _AVTPrecompiledStickerPackPlist.onceToken.2180
- _AVTPrecompiledStickerPackPlist.onceToken.2183
- _AVTPrecompiledStickerPackPlist.onceToken.2199
- _AVTPrecompiledStickerPackPlist.onceToken.2202
- _AVTPrecompiledStickerPackPlist.onceToken.2218
- _AVTPrecompiledStickerPackPlist.onceToken.2221
- _AVTPrecompiledStickerPackPlist.onceToken.2243
- _NSStringFromSelector
- _OBJC_CLASS_$_SCNAnimation
- _OBJC_CLASS_$_SCNAnimationEvent
- _OBJC_CLASS_$_SCNGeometry
- _OBJC_CLASS_$_SCNGeometryWrapDeformer
- _OBJC_CLASS_$_SCNGeometryWrapDeformerParameters
- _OBJC_CLASS_$_SCNPhysicsBody
- _OBJC_CLASS_$_SCNPhysicsConeTwistJoint
- _OBJC_CLASS_$_SCNPlane
- _OBJC_CLASS_$_SCNSphere
- _OBJC_CLASS_$_SCNTechnique
- _OBJC_IVAR_$_AVTARMaskRenderer._technique
- _OBJC_IVAR_$_AVTEyeSkinningDescriptor._readMorpherNode
- _OBJC_IVAR_$_AVTPupilReflectionCorrectionDescriptor._readMorpherNode
- _OBJC_IVAR_$_AVTRendererViewTransitionTechnique._technique
- _OBJC_IVAR_$_AVTSpringDynamic._referencePresentationNode
- _OBJC_IVAR_$_AVTSpringDynamic._restPosition
- _OBJC_METACLASS_$_SCNRenderer
- _OBJC_METACLASS_$_SCNView
- _SCNGeometrySourceSemanticVertex
- _SCNGetPerformanceStatistics
- _SCNGetShaderCollectionOutputURL
- _SCNLightTypeDirectional
- _SCNLightingModelConstant
- _SCNMatrix4Identity
- _SCNSetPerformanceStatisticsEnabled
- _SCNSetShaderCollectionEnabled
- __OBJC_$_CLASS_METHODS_AVTRenderer(CameraEffectsKit)
- __OBJC_$_INSTANCE_METHODS_AVTRenderer(CameraEffectsKit)
- __OBJC_$_PROP_LIST_AVTRendererTechnique
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCNMaterialPropertyTextureProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCNSceneRendererDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__SCNSceneRendererDelegateSPI
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SCNSceneCommandBufferStatusMonitor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SCNSceneRendererResourceManagerMonitor
- __OBJC_$_PROTOCOL_METHOD_TYPES_SCNMaterialPropertyTextureProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_SCNSceneRendererDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__SCNSceneCommandBufferStatusMonitor
- __OBJC_$_PROTOCOL_METHOD_TYPES__SCNSceneRendererDelegateSPI
- __OBJC_$_PROTOCOL_METHOD_TYPES__SCNSceneRendererResourceManagerMonitor
- __OBJC_$_PROTOCOL_REFS_SCNMaterialPropertyTextureProvider
- __OBJC_$_PROTOCOL_REFS_SCNSceneRendererDelegate
- __OBJC_$_PROTOCOL_REFS__SCNSceneCommandBufferStatusMonitor
- __OBJC_$_PROTOCOL_REFS__SCNSceneRendererDelegateSPI
- __OBJC_$_PROTOCOL_REFS__SCNSceneRendererResourceManagerMonitor
- __OBJC_LABEL_PROTOCOL_$_SCNMaterialPropertyTextureProvider
- __OBJC_LABEL_PROTOCOL_$_SCNSceneRendererDelegate
- __OBJC_LABEL_PROTOCOL_$__SCNSceneCommandBufferStatusMonitor
- __OBJC_LABEL_PROTOCOL_$__SCNSceneRendererDelegateSPI
- __OBJC_LABEL_PROTOCOL_$__SCNSceneRendererResourceManagerMonitor
- __OBJC_PROTOCOL_$_SCNMaterialPropertyTextureProvider
- __OBJC_PROTOCOL_$_SCNSceneRendererDelegate
- __OBJC_PROTOCOL_$__SCNSceneCommandBufferStatusMonitor
- __OBJC_PROTOCOL_$__SCNSceneRendererDelegateSPI
- __OBJC_PROTOCOL_$__SCNSceneRendererResourceManagerMonitor
- __SCNSetShaderCacheURL
- ___130-[AVTAvatar _transitionFromPose:toPose:bakedAnimationBlendFactor:duration:delay:timingFunction:timingAnimation:completionHandler:]_block_invoke.258
- ___145-[AVTAvatarPoseAnimation _addAnimationToAvatar:options:transitionInDuration:transitionOutDuration:isTransient:completionQueue:completionHandler:]_block_invoke.127
- ___20-[AVTMemoji _update]_block_invoke
- ___20-[AVTMemoji _update]_block_invoke_2
- ___28-[AVTMemoji skinTextureSize]_block_invoke
- ___36-[AVTARMaskRenderer reloadTechnique]_block_invoke
- ___39-[AVTAvatarBodyPose initWithHierarchy:]_block_invoke
- ___39-[AVTMaterial applyToSceneKitMaterial:]_block_invoke
- ___40-[AVTAvatarBodyPose initWithRootJoints:]_block_invoke
- ___40-[AVTAvatarBodyPose initWithRootJoints:]_block_invoke_2
- ___44-[AVTView _renderer:willRenderScene:atTime:]_block_invoke
- ___50-[AVTMemoji initWithDescriptor:usageIntent:error:]_block_invoke.233
- ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.300
- ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.300.cold.1
- ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.325
- ___65-[AVTAvatarPoseAnimation _initWithScene:usdaMetadata:identifier:]_block_invoke
- ___67-[AVTMemoji addDerivedNodesMatchingStickerPattern:toArray:options:]_block_invoke.355
- ___addAnimation_block_invoke
- ___addAnimation_block_invoke.245
- ___block_descriptor_124_e8_32s40s48s56s64s72s80s88bs96r104w_e52_v48?0"AVTAvatar"8d16d24"<SCNSceneRenderer>"32^B40ls32l8s40l8r96l8s48l8s56l8s64l8s72l8s80l8w104l8s88l8
- ___block_descriptor_32_e17_v16?0"SCNNode"8l
- ___block_descriptor_32_e21_v24?0"SCNNode"8^B16l
- ___block_descriptor_32_e40_B24?0"<AVTAvatarDynamic>"8"SCNNode"16l
- ___block_descriptor_32_e51_v24?0"SCNAnimation"8?<v?"NSString""NSData">16l
- ___block_descriptor_32_e56_B24?0"AVTMorpherDrivenMaterialDescriptor"8"SCNNode"16l
- ___block_descriptor_32_e57_v24?0"SCNAnimation"8?<v?"NSString""NSDictionary">16l
- ___block_descriptor_33_e21_v24?0"SCNNode"8^B16l
- ___block_descriptor_34_e21_v24?0"SCNNode"8^B16l
- ___block_descriptor_40_e63_v40?0"CABasicAnimation"8"NSString"16"<SCNAnimatable>"24^?32l
- ___block_descriptor_40_e8_32bs_e21_v24?0"SCNNode"8^B16ls32l8
- ___block_descriptor_40_e8_32r_e21_v24?0"SCNNode"8^B16lr32l8
- ___block_descriptor_40_e8_32r_e39_v32?0"NSString"8"SCNAnimation"16^B24lr32l8
- ___block_descriptor_40_e8_32s_e114_v40?0"<MTLComputeCommandEncoder>"8"<SCNMaterialPropertyTextureProviderHelper>"16"AVTMemoji"24"NSMutableSet"32ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"SCNNode"8ls32l8
- ___block_descriptor_40_e8_32s_e21_B24?0"SCNNode"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e28_B32?0"SCNMaterial"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e28_v32?0"SCNGeometry"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e28_v32?0"SCNMaterial"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e34_v32?0"AVTMemoji"8"SCNNode"16Q24ls32l8
- ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"SCNNode"16^B24ls32l8
- ___block_descriptor_41_e8_32s_e17_v16?0"SCNNode"8ls32l8
- ___block_descriptor_41_e8_32s_e21_v24?0"SCNNode"8^B16ls32l8
- ___block_descriptor_44_e8_32s_e21_v24?0"SCNNode"8^B16ls32l8
- ___block_descriptor_48_e8_32r_e17_v16?0"SCNNode"8lr32l8
- ___block_descriptor_48_e8_32s40bs_e30_v28?0"<SCNAnimation>"816B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e39_v32?0"NSString"8"SCNAnimation"16^B24ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e37_v32?0"NSString"8"SCNSkinner"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e24_v16?0"SCNPassContext"8lw40l8s32l8
- ___block_descriptor_48_e8_32s_e114_v40?0"<MTLComputeCommandEncoder>"8"<SCNMaterialPropertyTextureProviderHelper>"16"AVTMemoji"24"NSMutableSet"32ls32l8
- ___block_descriptor_48_e8_32s_e17_v16?0"SCNNode"8ls32l8
- ___block_descriptor_48_e8_32s_e21_v24?0"SCNNode"8^B16ls32l8
- ___block_descriptor_48_e8_32s_e30_v28?0"<SCNAnimation>"816B24ls32l8
- ___block_descriptor_52_e8_32s40s_e21_v24?0"SCNNode"8^B16ls32l8s40l8
- ___block_descriptor_56_e52_v48?0"AVTAvatar"8d16d24"<SCNSceneRenderer>"32^B40l
- ___block_descriptor_56_e8_32s40bs48r_e21_v24?0"SCNNode"8^B16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e30_v28?0"<SCNAnimation>"816B24ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e28_v32?0"SCNGeometry"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e114_v40?0"<MTLComputeCommandEncoder>"8"<SCNMaterialPropertyTextureProviderHelper>"16"AVTMemoji"24"NSMutableSet"32ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e21_v24?0"SCNNode"8^B16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e34_v32?0"NSString"8"SCNNode"16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e52_v48?0"AVTAvatar"8d16d24"<SCNSceneRenderer>"32^B40ls32l8s40l8
- ___block_descriptor_56_e8_32s_e114_v40?0"<MTLComputeCommandEncoder>"8"<SCNMaterialPropertyTextureProviderHelper>"16"AVTMemoji"24"NSMutableSet"32ls32l8
- ___block_descriptor_56_e8_32s_e21_v24?0"SCNNode"8^B16ls32l8
- ___block_descriptor_56_e8_32s_e43_v32?0"SCNGeometry"8f16"SCNGeometry"20f28ls32l8
- ___block_descriptor_60_e8_32s40s48bs_e21_v24?0"SCNNode"8^B16ls32l8s40l8s48l8
- ___block_descriptor_60_e8_32s40s48r_e43_v32?0"SCNGeometry"8f16"SCNGeometry"20f28lr48l8s32l8s40l8
- ___block_descriptor_60_e8_32s40s48s_e21_v24?0"SCNNode"8^B16ls32l8s40l8s48l8
- ___block_descriptor_60_e8_32s40s48s_e28_v32?0"SCNGeometry"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e28_v32?0"SCNGeometry"8Q16^B24ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s_e28_v32?0"SCNGeometry"8Q16^B24ls32l8s40l8
- ___block_descriptor_64_e8_32s40s_e67_v48?0"SCNNode"8"NSString"16"NSString"24"NSValue"32"NSValue"40ls32l8s40l8
- ___block_descriptor_65_e8_32s40s48s56s_e21_v24?0"SCNNode"8^B16ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48s_e21_v24?0"SCNNode"8^B16ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r_e52_v48?0"AVTAvatar"8d16d24"<SCNSceneRenderer>"32^B40ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s_e21_v24?0"SCNNode"8^B16ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e21_v24?0"SCNNode"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e21_v24?0"SCNNode"8^B16ls32l8s40l8r72l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64bs72w_e52_v48?0"AVTAvatar"8d16d24"<SCNSceneRenderer>"32^B40ls32l8s40l8w72l8s48l8s56l8s64l8
- ___block_descriptor_92_e8_32s40s48s56s64bs72w_e52_v48?0"AVTAvatar"8d16d24"<SCNSceneRenderer>"32^B40ls32l8s40l8w72l8s48l8s56l8s64l8
- ___block_literal_global.162
- ___block_literal_global.1815
- ___block_literal_global.1818
- ___block_literal_global.200
- ___block_literal_global.2182
- ___block_literal_global.2185
- ___block_literal_global.2201
- ___block_literal_global.2204
- ___block_literal_global.2220
- ___block_literal_global.2223
- ___block_literal_global.2245
- ___block_literal_global.244
- ___block_literal_global.349
- ___block_literal_global.37
- ___block_literal_global.39
- ___block_literal_global.531
- ___block_literal_global.533
- ___block_literal_global.89
- _addAnimation
- _addAnimation.cold.1
- _addAnimation.cold.2
- _addAnimation.cold.3
- _addAnimation.cold.4
- _addAnimation.cold.5
- _objc_msgSend$_initWithScene:usdaMetadata:identifier:
- _objc_msgSend$_update
- _objc_msgSend$addBehavior:
- _objc_msgSend$animationForKey:
- _objc_msgSend$applyToSceneKitMaterial:
- _objc_msgSend$avt_nodeNamed:forSceneAtURL:options:error:
- _objc_msgSend$avt_rootNodeForSceneAtURL:options:error:
- _objc_msgSend$colorPixelFormat
- _objc_msgSend$dataWithContentsOfURL:
- _objc_msgSend$edgeCreasesElement
- _objc_msgSend$edgeCreasesSource
- _objc_msgSend$geometrySourceChannels
- _objc_msgSend$geometrySources
- _objc_msgSend$geometryWithSources:elements:
- _objc_msgSend$geometryWithSources:elements:sourceChannels:
- _objc_msgSend$initWithHierarchy:
- _objc_msgSend$initWithRootJoints:
- _objc_msgSend$initWithSceneAtURL:
- _objc_msgSend$initWithSceneAtURL:usdaMetadata:
- _objc_msgSend$initWithSceneRenderer:
- _objc_msgSend$inputTextureWithName:
- _objc_msgSend$morphTo:
- _objc_msgSend$movabilityHint
- _objc_msgSend$nodeWithGeometry:
- _objc_msgSend$optimizeAnimation:target:
- _objc_msgSend$outputTextureWithName:
- _objc_msgSend$passAtIndex:
- _objc_msgSend$postSkinningDeformers
- _objc_msgSend$removeBehavior:
- _objc_msgSend$renderingAPI
- _objc_msgSend$scene
- _objc_msgSend$sceneTime
- _objc_msgSend$setBlendInDuration:
- _objc_msgSend$setEdgeCreasesElement:
- _objc_msgSend$setEdgeCreasesSource:
- _objc_msgSend$setExecutionHandler:
- _objc_msgSend$setGrainIntensity:
- _objc_msgSend$setGrainIsColored:
- _objc_msgSend$setGrainScale:
- _objc_msgSend$setGrainSlice:
- _objc_msgSend$setGrainTexture:
- _objc_msgSend$setLensShift:
- _objc_msgSend$setLibrary:
- _objc_msgSend$setLightingModelName:
- _objc_msgSend$setMovabilityHint:
- _objc_msgSend$setPostSkinningDeformers:
- _objc_msgSend$setScene:
- _objc_msgSend$setSceneTime:
- _objc_msgSend$setSimdEulerAngles:
- _objc_msgSend$setSimdOrientation:
- _objc_msgSend$setSimdPosition:
- _objc_msgSend$setSimdScale:
- _objc_msgSend$setSimdWorldTransform:
- _objc_msgSend$setStartDelay:
- _objc_msgSend$setXFov:
- _objc_msgSend$set_wantsSceneRendererDelegationMessages:
- _objc_msgSend$simdConvertPosition:fromNode:
- _objc_msgSend$simdConvertPosition:toNode:
- _objc_msgSend$simdConvertTransform:toNode:
- _objc_msgSend$simdConvertVector:fromNode:
- _objc_msgSend$simdConvertVector:toNode:
- _objc_msgSend$simdEulerAngles
- _objc_msgSend$simdWorldPosition
- _objc_msgSend$simdWorldTransform
- _objc_msgSend$snapshotAtTime:withSize:antialiasingMode:
- _objc_msgSend$startDelay
- _objc_msgSend$subdivisionLevel
- _objc_msgSend$technique
- _objc_msgSend$techniqueWithDictionary:
- _objc_msgSend$update
- _objc_msgSend$usesReverseZ
- _objc_msgSend$valueWithBytes:objCType:
- _objc_msgSend$valueWithCGRect:
- _objc_msgSend$willRemoveFromScene:
CStrings:
+ " | empty pose"
+ "%@%@=%@"
+ "%@/%@.aa"
+ ", "
+ "-[AVTAvatar update]"
+ "-[AVTRendererViewTransitionTechnique initWithWorldRenderer:]"
+ "<%@ %p | \"%@\" %@>"
+ "<%@ %p | \"%@\">"
+ "<%@ %p | %@ %@>"
+ "<%@ %p | %@>"
+ "<%@ %p | %@[%@] = %f>"
+ "<%@ %p | Morpher %p driven by \"%@\">"
+ "<%@ %p | Skeleton %p driven by \"%@\">"
+ "<%@ %p | Spring \"%@\">"
+ "<%@ %p | base color: %@, additional properties: %@>"
+ "<%@ %p | category:%@ identifier:%@>"
+ "<%@ %p | name:%@ category:%@ variation:%f>"
+ "<%@ %p | type:%@"
+ "<%@ %p%@>"
+ "@\"<AVTRendererTechniqueSupport><AVTWorldRenderer>\""
+ "@\"<VFXCaptureDeviceOutputConsumer>\""
+ "@\"<VFXWorldRenderer>\""
+ "@\"<VFXWorldRendererDelegate>\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSArray\"24@0:8@\"VFXNode\"16"
+ "@\"NSData\"32@0:8@\"<VFXWorldRenderer>\"16@\"NSString\"24"
+ "@\"NSRecursiveLock\""
+ "@\"VFXAnimationPlayer\""
+ "@\"VFXMaterial\""
+ "@\"VFXMorpher\""
+ "@\"VFXNode\""
+ "@\"VFXNode\"16@0:8"
+ "@\"VFXNode\"24@0:8@\"AVTPhysicsController\"16"
+ "@\"VFXPhysicsBody\""
+ "@\"VFXPhysicsConeTwistJoint\""
+ "@\"VFXPhysicsWorld\""
+ "@\"VFXRenderGraph\"16@0:8"
+ "@\"VFXSkinner\""
+ "@\"VFXWorld\""
+ "@\"VFXWorld\"16@0:8"
+ "@48@0:8@16@24B32@36B44"
+ "AVTMergeSceneKitShaderModifiersForEntryPointWithCodeAndParts"
+ "AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndCode"
+ "AVTMergeSceneKitShaderModifiersForEntryPointWithPartsAndParts"
+ "AVTRendererViewTransitionTechnique.m"
+ "AVTRenderer_CEKWorkaround"
+ "AVTWorldRenderer"
+ "AVT_composite_fragment_legacy"
+ "AVT_dbg_fragment"
+ "AVT_view_transition_generic_fragment"
+ "AVT_view_transition_vertex"
+ "AvatarKit_CEKWorkaround"
+ "B24@0:8@\"<VFXWorldRenderer>\"16"
+ "B24@0:8@\"VFXNode\"16"
+ "B24@?0@\"<AVTAvatarDynamic>\"8@\"VFXNode\"16"
+ "B24@?0@\"AVTMorpherDrivenMaterialDescriptor\"8@\"VFXNode\"16"
+ "B24@?0@\"VFXNode\"8^B16"
+ "B32@0:8@\"<VFXWorldRenderer>\"16^24"
+ "B32@0:8@\"<VFXWorldRenderer>\"16^Q24"
+ "B32@0:8@\"VFXNode\"16@\"VFXNode\"24"
+ "B32@0:8@16^24"
+ "B32@0:8@16^Q24"
+ "B32@?0@\"VFXMaterial\"8Q16^B24"
+ "B32@?0@\"VFXMesh\"8Q16^B24"
+ "B32@?0@\"VFXNode\"8Q16^B24"
+ "Error: Condition '%s' failed. Did expect subclass %@"
+ "Error: Condition '%s' failed. Needs more work to support timeOffset + VFXAnimationEvent"
+ "Error: Failed to create compute pipeline state for \"%@\" with error %@"
+ "Error: Failed to create render pipeline state for \"%@\" + \"%@\" with error %@"
+ "Error: Unreachable code: %s should never be called"
+ "Error: Unreachable code: Unsupported file type for scene %@"
+ "Failed to find spring target named '%@'"
+ "JFXAnimojiEffectRenderer"
+ "T@\"<VFXWorldRendererDelegate>\",W,N"
+ "T@\"NSArray\",C,N"
+ "T@\"VFXNode\",&,N"
+ "T@\"VFXNode\",&,N,V_node"
+ "T@\"VFXNode\",R"
+ "T@\"VFXNode\",R,N"
+ "T@\"VFXNode\",R,N,V_rootNode"
+ "T@\"VFXNode\",R,V_assetNode"
+ "T@\"VFXRenderGraph\",&,N"
+ "T@\"VFXRenderer\",R,N"
+ "T@\"VFXWorld\",&,N"
+ "T@,&,N"
+ "VFX+AVTExtensions.m"
+ "VFXCamera_CEKWorkaround"
+ "VFXFloat3Value"
+ "VFXFloat4Value"
+ "VFXMaterialPropertyTextureProvider"
+ "VFXNode_CEKWorkaround"
+ "VFXWorldRenderer"
+ "VFXWorldRendererDelegate"
+ "VFXWorld_CEKWorkaround"
+ "[AvatarKit] Composite"
+ "[AvatarKit] Debug"
+ "[AvatarKit] View transition"
+ "[worldRenderer isKindOfClass:AVTView.class]"
+ "_VFXWorldCommandBufferStatusMonitor"
+ "_VFXWorldRendererDelegateSPI"
+ "_VFXWorldRendererMainPassCustomPostProcessSupport"
+ "_VFXWorldRendererResourceManagerMonitor"
+ "_avatarWantsSpecificTechniqueDidChange:"
+ "_avtRendererTechniquePresentationTree"
+ "_backgroundContentsBehindDrawable"
+ "_compositeLegacyPipelineState"
+ "_compositeMattePipelineState"
+ "_compositeMatteWithChromaKeyPipelineState"
+ "_customMainPassPostProcessUsesExtraRenderTargetForRenderer:pixelFormat:"
+ "_debugCamDepthTexture"
+ "_debugIntermediateTexture"
+ "_defaultBackgroundColor"
+ "_drawWithUpdate:"
+ "_encodeCustomMainPassPostProcessForRenderer:atTime:helper:"
+ "_generatedMasksTexture"
+ "_implementCEKWorkaroundIfNeeded"
+ "_initWithDevice:options:isPrivateRenderer:privateRendererOwner:clearsOnDraw:"
+ "_initWithSceneKitScene:usdaMetadata:identifier:"
+ "_lastRenderedTexture"
+ "_presentationWeightForTargetAtIndex:token:"
+ "_readMorpher"
+ "_renderPipelineState"
+ "_renderer:willRenderWorld:atTime:"
+ "_surface.$ambientOcclusion"
+ "_surface.ambient"
+ "_surface.ambientOcclusion"
+ "_targetPresentationNode"
+ "_updateWithOptions:"
+ "_usesSpecificMainPassClearColorForRenderer:clearColor:"
+ "_wantsCustomMainPassPostProcessForRenderer:"
+ "addPhysicsJoint:"
+ "additiveWritesToAlpha"
+ "allObjects"
+ "animationPlayerWithAnimation:"
+ "applyToVFXMaterial:"
+ "avatarSpecificTechniqueClass"
+ "avt_newWorldWithURL:options:error:"
+ "avt_nodeNamed:forWorldAtURL:options:error:"
+ "avt_rootNodeForWorldAtURL:options:error:"
+ "avt_rootObjectForWorldAtURL:options:error:"
+ "avt_setSimdBaseMeshBindTransform:"
+ "backgroundContentsBehindDrawable"
+ "baseMesh"
+ "baseMeshBindTransform"
+ "begin_CEKWorkaround"
+ "binaryArchives"
+ "blendMode"
+ "clock"
+ "commit_CEKWorkaround"
+ "compact"
+ "convertPosition:fromNode:"
+ "convertPosition:toNode:"
+ "convertTransform:fromNode:"
+ "convertVector:fromNode:"
+ "convertVector:toNode:"
+ "d32@0:8@\"<VFXWorldRenderer>\"16d24"
+ "deformers"
+ "destinationTexture"
+ "drawSceneBackgroundUsingEncoder:commandBuffer:renderPassDescriptor:"
+ "encodeCompositePassWithEncoder:sceneColorTexture:sceneOnTopTexture:helper:"
+ "encodeTechniqueCommandsForRenderer:atTime:helper:"
+ "float4 kAmbient"
+ "flush_CEKWorkaround"
+ "grain"
+ "initWithSceneKitHierarchy:"
+ "initWithSceneKitRootJoints:"
+ "initWithSceneKitScene:"
+ "initWithSceneKitScene:usdaMetadata:"
+ "initWithSceneKitSceneAtURL:"
+ "initWithSceneKitSceneAtURL:usdaMetadata:"
+ "initWithWorldRenderer:"
+ "kAVTAvatarWantsSpecificTechniqueDidChangeNotificationName"
+ "kAVTRecordViewLivePreview"
+ "kAmbient"
+ "main.vfxz-world"
+ "mainPassColorTextureAtIndex:"
+ "mesh"
+ "meshElements"
+ "meshSourceChannels"
+ "meshSourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:"
+ "meshSources"
+ "meshWithSources:elements:"
+ "meshWithSources:elements:sourceChannels:"
+ "modelElements"
+ "newAvatarSpecificTechniqueWithRenderer:"
+ "nodeWithModel:"
+ "optimizeSceneKitAnimation:target:"
+ "performPresentationObjectQueriesInWorld:usingBlock:"
+ "removePhysicsJoint:"
+ "renderCommandEncoder"
+ "renderGraph"
+ "renderer:didRenderWorld:atTime:"
+ "renderer:willRenderWorld:atTime:"
+ "replaceOccurrencesOfString:withString:options:range:"
+ "self.class == AVTRenderer.class"
+ "self.class == VFXCamera.class"
+ "self.class == VFXNode.class"
+ "self.class == VFXWorld.class"
+ "setAdditiveWritesToAlpha:"
+ "setAnimationDuration_CEKWorkaround:"
+ "setBackgroundContentsBehindDrawable:"
+ "setBaseMeshBindTransform:"
+ "setBinaryArchives:"
+ "setBlendMode:"
+ "setColored:"
+ "setDeformers:"
+ "setEulerAngles:"
+ "setFilmOffset:"
+ "setIdentifier:"
+ "setMesh:"
+ "setModel:"
+ "setOrientation:"
+ "setPhysicsShape:"
+ "setRenderGraph:"
+ "setShadingModel:"
+ "setSlice:"
+ "setTime:"
+ "setTimeOrigin:"
+ "setTimeSource:"
+ "setWorld:"
+ "setWorldTransform:"
+ "set_wantsWorldRendererDelegationMessages:"
+ "shapeWithModel:"
+ "simd_equal(rootJoint.transform, matrix_identity_float4x4)"
+ "skeleton.aa"
+ "skinnerWithBaseMesh:bones:boneInverseBindTransforms:boneWeights:boneIndices:"
+ "stringByAppendingPathExtension:"
+ "target"
+ "techniqueIsActive"
+ "techniqueUsesExtraRenderTargetForRenderer:pixelFormat:"
+ "techniqueUsesSpecificMainPassClearColorForRenderer:clearColor:"
+ "time"
+ "updateWithOptions:"
+ "v16@?0@\"VFXNode\"8"
+ "v16@?0r^v8"
+ "v24@0:8@\"<VFXWorldRendererDelegate>\"16"
+ "v24@0:8@\"NSArray\"16"
+ "v24@0:8@\"VFXNode\"16"
+ "v24@0:8@\"VFXRenderGraph\"16"
+ "v24@0:8@\"VFXWorld\"16"
+ "v24@?0@\"VFXAnimation\"8@?<v@?@\"NSString\"@\"NSData\">16"
+ "v24@?0@\"VFXAnimation\"8@?<v@?@\"NSString\"@\"NSDictionary\">16"
+ "v24@?0@\"VFXNode\"8^B16"
+ "v28@?0@\"<VFXAnimation>\"8@16B24"
+ "v32@0:8@\"<VFXWorldRenderer>\"16@\"<MTLCommandBuffer>\"24"
+ "v32@0:8@\"<VFXWorldRenderer>\"16d24"
+ "v32@?0@\"AVTMemoji\"8@\"VFXNode\"16Q24"
+ "v32@?0@\"NSString\"8@\"VFXAnimation\"16^B24"
+ "v32@?0@\"NSString\"8@\"VFXNode\"16^B24"
+ "v32@?0@\"NSString\"8@\"VFXSkinner\"16^B24"
+ "v32@?0@\"VFXMaterial\"8Q16^B24"
+ "v32@?0@\"VFXMesh\"8Q16^B24"
+ "v32@?0@\"VFXMesh\"8f16@\"VFXMesh\"20f28"
+ "v32@?0@\"VFXMeshElement\"8Q16^B24"
+ "v40@0:8@\"<VFXWorldRenderer>\"16@\"NSString\"24@?<@\"NSData\"@?>32"
+ "v40@0:8@\"<VFXWorldRenderer>\"16@\"VFXWorld\"24d32"
+ "v40@0:8@\"<VFXWorldRenderer>\"16@24@\"NSString\"32"
+ "v40@0:8@\"<VFXWorldRenderer>\"16d24@\"<_VFXWorldRendererMainPassCustomPostProcessHelper>\"32"
+ "v40@0:8@16d24@32"
+ "v40@?0@\"<MTLComputeCommandEncoder>\"8@\"<VFXMaterialPropertyTextureProviderHelper>\"16@\"AVTMemoji\"24@\"NSMutableSet\"32"
+ "v40@?0@\"CABasicAnimation\"8@\"NSString\"16@\"<VFXAnimatable>\"24^?32"
+ "v48@0:8@16q24d3240"
+ "v48@?0@\"AVTAvatar\"8d16d24@\"<VFXWorldRenderer>\"32^B40"
+ "v48@?0@\"VFXNode\"8@\"NSString\"16@\"NSString\"24@\"NSValue\"32@\"NSValue\"40"
+ "v56@0:8@\"<MTLTexture>\"16@?<v@?@?<v@?@\"<MTLComputeCommandEncoder>\">>24@?<v@?@?<v@?@\"<MTLBlitCommandEncoder>\">>32@?<v@?@?<v@?@\"<MTLCommandBuffer>\">>40@\"<VFXMaterialPropertyTextureProviderHelper>\"48"
+ "valueWithVFXFloat3:"
+ "valueWithVFXFloat4:"
+ "vfx-world"
+ "vfx_compressedDataUsingCompressionAlgorithm:"
+ "vfx_uncompressedDataUsingCompressionAlgorithm:"
+ "vfxz-world"
+ "willRemoveFromWorld:"
+ "world"
+ "worldPosition"
+ "worldTransform"
+ "worldWithSceneKitScene:options:"
+ "worldWithURL:options:error:"
+ "writeToURL:options:progressHandler:"
- " (empty pose)"
- "%@/%@.aa/main.scnz"
- ", %@=%@"
- "<%@ %p> \"%@\" %@"
- "<%@: %p \"%@\">"
- "<%@: %p category=%@ identifier=%@>"
- "<%@: %p | %@[%@] = %f>"
- "<%@: %p%@>"
- "<%@: %p, %@>"
- "<%@: %p, base color: %@, additional properties: %@>"
- "<%@: %p, type=%@"
- "<%@: %p> name:%@ category:%@ variation:%f "
- "<AVTPhysicalizedMorpherDynamic: %p> Morpher %p driven by \"%@\""
- "<AVTPhysicalizedMorpherDynamic: %p> Skeleton %p driven by \"%@\""
- "<AVTSpringDynamic: %p> Spring \"%@\""
- "<AVTStickerShaderModifier: %p>(%@ %@)"
- "@\"<AVTRendererTechniqueSupport><AVTSceneRenderer>\""
- "@\"<SCNCaptureDeviceOutputConsumer>\""
- "@\"<SCNSceneRenderer>\""
- "@\"NSData\"32@0:8@\"<SCNSceneRenderer>\"16@\"NSString\"24"
- "@\"SCNAnimationPlayer\""
- "@\"SCNMaterial\""
- "@\"SCNMorpher\""
- "@\"SCNNode\""
- "@\"SCNNode\"24@0:8@\"AVTPhysicsController\"16"
- "@\"SCNPhysicsBody\""
- "@\"SCNPhysicsConeTwistJoint\""
- "@\"SCNPhysicsWorld\""
- "@\"SCNScene\""
- "@\"SCNSkinner\""
- "@\"SCNTechnique\""
- "@\"SCNTechnique\"16@0:8"
- "@56@0:8@16B24@28B36^v40Q48"
- "ARMaskTechnique.json"
- "ARMaskTechniqueDbg.json"
- "B24@0:8@\"SCNNode\"16"
- "B24@?0@\"<AVTAvatarDynamic>\"8@\"SCNNode\"16"
- "B24@?0@\"AVTMorpherDrivenMaterialDescriptor\"8@\"SCNNode\"16"
- "B32@?0@\"SCNMaterial\"8Q16^B24"
- "CompositePass"
- "CustomPass"
- "Error: Condition '%s' failed. Needs more work to support timeOffset + SCNAnimationEvent"
- "Error: Condition '%s' failed. We did not expect a beginTime of %.3f"
- "Error: Unreachable code: %@ is not supported on AVTView"
- "SCNMaterialPropertyTextureProvider"
- "SCNSceneRendererDelegate"
- "ScenePass"
- "SimplePassTechnique.json"
- "T@\"SCNNode\",&,N,V_node"
- "T@\"SCNNode\",R"
- "T@\"SCNNode\",R,N"
- "T@\"SCNNode\",R,N,V_rootNode"
- "T@\"SCNNode\",R,V_assetNode"
- "T@\"SCNRenderer\",R,N"
- "T@\"SCNTechnique\",R,N"
- "ViewTransitionTechniqueGeneric.json"
- "_SCNSceneCommandBufferStatusMonitor"
- "_SCNSceneRendererDelegateSPI"
- "_SCNSceneRendererResourceManagerMonitor"
- "_initWithOptions:isPrivateRenderer:privateRendererOwner:clearsOnDraw:context:renderingAPI:"
- "_initWithScene:usdaMetadata:identifier:"
- "_referencePresentationNode"
- "_renderer:willRenderScene:atTime:"
- "_restPosition"
- "_technique"
- "_update"
- "addBehavior:"
- "animationForKey:"
- "applyToSceneKitMaterial:"
- "a\xe1"
- "camDepth_target"
- "chromaKeyColor"
- "chromaKeyColor_symbol"
- "colorStates"
- "d32@0:8@\"<SCNSceneRenderer>\"16d24"
- "dataWithContentsOfURL:"
- "edgeCreasesElement"
- "edgeCreasesSource"
- "fabs(delta - beginTime) < 1e-3"
- "float4"
- "geometrySourceChannels"
- "geometrySources"
- "geometryWithSources:elements:"
- "geometryWithSources:elements:sourceChannels:"
- "headZ_symbol"
- "initWithHierarchy:"
- "initWithRootJoints:"
- "initWithScene:usdaMetadata:"
- "initWithSceneAtURL:"
- "initWithSceneAtURL:usdaMetadata:"
- "initWithSceneRenderer:"
- "inputTextureWithName:"
- "inputs"
- "livePreview"
- "main.scnz"
- "mask_target"
- "metalFragmentShader"
- "morphTo:"
- "movabilityHint"
- "neckU_symbol"
- "neckV_symbol"
- "nodeWithGeometry:"
- "opacity_symbol"
- "optimizeAnimation:target:"
- "outputTextureWithName:"
- "passAtIndex:"
- "passes"
- "postSkinningDeformers"
- "removeBehavior:"
- "renderToTexture:computeCommandHandler:blitCommandHandler:helper:"
- "renderer:didRenderScene:atTime:"
- "renderer:willRenderScene:atTime:"
- "samples"
- "sceneColorTexture_target"
- "sceneOnTopTexture_target"
- "sequence"
- "setBlendInDuration:"
- "setEdgeCreasesElement:"
- "setEdgeCreasesSource:"
- "setExecutionHandler:"
- "setGrainIntensity:"
- "setGrainIsColored:"
- "setGrainScale:"
- "setGrainSlice:"
- "setGrainTexture:"
- "setLensShift:"
- "setLibrary:"
- "setLightingModelName:"
- "setMovabilityHint:"
- "setPostSkinningDeformers:"
- "setSimdEulerAngles:"
- "setSimdOrientation:"
- "setSimdPosition:"
- "setSimdScale:"
- "setSimdWorldTransform:"
- "setStartDelay:"
- "setTechnique:"
- "setXFov:"
- "set_wantsSceneRendererDelegationMessages:"
- "shadowMaskSizeU_symbol"
- "shadowMaskSizeV_symbol"
- "shadowUVOffset_symbol"
- "simdConvertPosition:fromNode:"
- "simdConvertPosition:toNode:"
- "simdConvertTransform:toNode:"
- "simdConvertVector:fromNode:"
- "simdConvertVector:toNode:"
- "simdEulerAngles"
- "simdWorldPosition"
- "simdWorldTransform"
- "skeleton.aa/main.scnz"
- "snapshotAtTime:withSize:antialiasingMode:"
- "snapshot_symbol"
- "startDelay"
- "subdivisionLevel"
- "symbols"
- "techniqueWithDictionary:"
- "v16@?0@\"SCNPassContext\"8"
- "v24@?0@\"SCNAnimation\"8@?<v@?@\"NSString\"@\"NSData\">16"
- "v24@?0@\"SCNAnimation\"8@?<v@?@\"NSString\"@\"NSDictionary\">16"
- "v28@?0@\"<SCNAnimation>\"8@16B24"
- "v32@0:8@\"<SCNSceneRenderer>\"16@\"<MTLCommandBuffer>\"24"
- "v32@0:8@\"<SCNSceneRenderer>\"16d24"
- "v32@?0@\"AVTMemoji\"8@\"SCNNode\"16Q24"
- "v32@?0@\"NSString\"8@\"SCNAnimation\"16^B24"
- "v32@?0@\"NSString\"8@\"SCNSkinner\"16^B24"
- "v32@?0@\"SCNGeometry\"8Q16^B24"
- "v32@?0@\"SCNGeometry\"8f16@\"SCNGeometry\"20f28"
- "v32@?0@\"SCNMaterial\"8Q16^B24"
- "v40@0:8@\"<SCNSceneRenderer>\"16@\"NSString\"24@?<@\"NSData\"@?>32"
- "v40@0:8@\"<SCNSceneRenderer>\"16@\"SCNScene\"24d32"
- "v40@0:8@\"<SCNSceneRenderer>\"16@24@\"NSString\"32"
- "v40@?0@\"<MTLComputeCommandEncoder>\"8@\"<SCNMaterialPropertyTextureProviderHelper>\"16@\"AVTMemoji\"24@\"NSMutableSet\"32"
- "v40@?0@\"CABasicAnimation\"8@\"NSString\"16@\"<SCNAnimatable>\"24^?32"
- "v48@0:8@\"<MTLTexture>\"16@?<v@?@?<v@?@\"<MTLComputeCommandEncoder>\">>24@?<v@?@?<v@?@\"<MTLBlitCommandEncoder>\">>32@\"<SCNMaterialPropertyTextureProviderHelper>\"40"
- "v48@0:8@16@?24@?32@40"
- "v48@0:8@16Q24d3240"
- "v48@?0@\"AVTAvatar\"8d16d24@\"<SCNSceneRenderer>\"32^B40"
- "v48@?0@\"SCNNode\"8@\"NSString\"16@\"NSString\"24@\"NSValue\"32@\"NSValue\"40"
- "v56@0:8@\"<MTLTexture>\"16@?<v@?@?<v@?@\"<MTLComputeCommandEncoder>\">>24@?<v@?@?<v@?@\"<MTLBlitCommandEncoder>\">>32@?<v@?@?<v@?@\"<MTLCommandBuffer>\">>40@\"<SCNMaterialPropertyTextureProviderHelper>\"48"
- "valueWithBytes:objCType:"
- "valueWithCGRect:"
- "willRemoveFromScene:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}"
- "{SCNMatrix4=ffffffffffffffff}"
- "{SCNVector3=fff}"
- "{SCNVector4=ffff}"

```
