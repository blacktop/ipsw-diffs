## AvatarKit

> `/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit`

```diff

-355.1.0.0.0
-  __TEXT.__text: 0x767b0
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_methlist: 0x5444
+356.0.0.0.0
+  __TEXT.__text: 0x769d4
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x5414
   __TEXT.__const: 0xa2c
-  __TEXT.__cstring: 0x1ddb2
-  __TEXT.__oslogstring: 0x2c38
-  __TEXT.__gcc_except_tab: 0x1030
-  __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x1bb8
+  __TEXT.__cstring: 0x1ddec
+  __TEXT.__oslogstring: 0x2c7c
+  __TEXT.__ustring: 0x66
+  __TEXT.__gcc_except_tab: 0xde8
+  __TEXT.__unwind_info: 0x1b90
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xa6d
-  __TEXT.__objc_methname: 0x10980
-  __TEXT.__objc_methtype: 0x273c
-  __TEXT.__objc_stubs: 0xc980
+  __TEXT.__objc_classname: 0xa6f
+  __TEXT.__objc_methname: 0x10904
+  __TEXT.__objc_methtype: 0x2885
+  __TEXT.__objc_stubs: 0xc940
   __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x26b8
+  __DATA_CONST.__const: 0x26e0
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cf0
+  __DATA_CONST.__objc_selrefs: 0x3cc8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x62590
-  __AUTH_CONST.__auth_got: 0x720
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x24880
-  __AUTH_CONST.__objc_const: 0xda60
+  __AUTH_CONST.__auth_got: 0x728
+  __AUTH_CONST.__const: 0xa40
+  __AUTH_CONST.__cfstring: 0x248e0
+  __AUTH_CONST.__objc_const: 0xdad0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x7bc0
   __AUTH_CONST.__objc_doubleobj: 0x2370
   __AUTH_CONST.__objc_dictobj: 0x4ede0
   __AUTH.__objc_data: 0x1810
-  __DATA.__objc_ivar: 0xa28
+  __DATA.__objc_ivar: 0xa3c
   __DATA.__data: 0x788
-  __DATA.__bss: 0xaa8
+  __DATA.__bss: 0xab8
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/ARKit.framework/ARKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7A5F943-78CE-3853-A1BB-CF18FD430AE8
+  UUID: 0B237E54-88E3-3003-901D-8C95648CA1AF
   Functions: 2478
-  Symbols:   9429
-  CStrings:  13024
+  Symbols:   9430
+  CStrings:  13027
 
Symbols:
+ -[AVTARMaskRenderer encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:cameraDepthDebug:]
+ -[AVTMemoji _invalidateSkinAO]
+ -[AVTMemoji _locked_invalidate]
+ -[AVTMemoji _updateSkinAO]
+ -[AVTMemoji createSkinCombinedAOImage]
+ -[AVTPhysicsController init]
+ -[AVTPreset newComponent]
+ -[AVTPresetStore debugDescription]
+ -[AVTPresetStore debugDescription].cold.1
+ -[AVTRendererViewTransitionTechnique rebuildRenderPipelineStateIfNeededForPixelFormat:]
+ -[AVTViewTransitionHelper coordinator_performCrossFadeTransitionOutOfStickerConfigurationWithDuration:avatar:avatarNode:oldReversionContext:].cold.2
+ -[AVTViewTransitionHelper coordinator_performCrossFadeTransitionToStickerConfiguration:duration:options:avatar:avatarNode:oldReversionContext:].cold.2
+ GCC_except_table103
+ GCC_except_table117
+ GCC_except_table130
+ GCC_except_table170
+ GCC_except_table34
+ _AVTGetPixelBufferTexture
+ _AVTPrecompiledStickerPackPlist.onceToken.1809
+ _AVTPrecompiledStickerPackPlist.onceToken.1812
+ _AVTPrecompiledStickerPackPlist.onceToken.2176
+ _AVTPrecompiledStickerPackPlist.onceToken.2179
+ _AVTPrecompiledStickerPackPlist.onceToken.2195
+ _AVTPrecompiledStickerPackPlist.onceToken.2198
+ _AVTPrecompiledStickerPackPlist.onceToken.2214
+ _AVTPrecompiledStickerPackPlist.onceToken.2217
+ _AVTPrecompiledStickerPackPlist.onceToken.2239
+ _CGColorSpaceGetModel
+ _CVPixelBufferGetPixelFormatType
+ _OBJC_IVAR_$_AVTARMaskRenderer._debugCameraColorTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._debugCameraDepthTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._debugConvertDepthPipelineState
+ _OBJC_IVAR_$_AVTMemoji._skinAOIsValid
+ _OBJC_IVAR_$_AVTPhysicsController._lock
+ _OBJC_IVAR_$_AVTRendererViewTransitionTechnique._helper
+ _OBJC_IVAR_$_AVTRendererViewTransitionTechnique._renderPipelineStateDescriptor
+ _OBJC_IVAR_$_AVTRendererViewTransitionTechnique._viewIsOpaque
+ _OBJC_IVAR_$_AVTStickerConfiguration._lock
+ ___26-[AVTMemoji _updateSkinAO]_block_invoke
+ ___34-[AVTPresetStore debugDescription]_block_invoke
+ ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.308
+ ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.308.cold.1
+ ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.333
+ _____AVTPresetLoadPresets_block_invoke.358
+ _____AVTPresetLoadPresets_block_invoke.374
+ _____AVTPresetLoadPresets_block_invoke.374.cold.1
+ _____AVTPresetLoadPresets_block_invoke.374.cold.2
+ _____AVTPresetLoadPresets_block_invoke_2.361
+ ___block_descriptor_72_e16_48s56s64s_e5_v8?0ls48l8s56l8s64l8
+ ___block_literal_global.1811
+ ___block_literal_global.1814
+ ___block_literal_global.2178
+ ___block_literal_global.2181
+ ___block_literal_global.2197
+ ___block_literal_global.2200
+ ___block_literal_global.2216
+ ___block_literal_global.2219
+ ___block_literal_global.2241
+ ___block_literal_global.252
+ ___block_literal_global.315
+ ___block_literal_global.318
+ ___block_literal_global.360
+ ___block_literal_global.537
+ ___copy_assignment_8_8_t0w72_s72_s80_t88w8
+ _debugDescription.maxCategoryToStringLength
+ _debugDescription.onceToken
+ _objc_msgSend$_invalidateSkinAO
+ _objc_msgSend$_locked_invalidate
+ _objc_msgSend$_updateSkinAO
+ _objc_msgSend$createSkinCombinedAOImage
+ _objc_msgSend$encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:cameraDepthDebug:
+ _objc_msgSend$newComponent
+ _objc_msgSend$rebuildRenderPipelineStateIfNeededForPixelFormat:
+ _objc_msgSend$stringWithString:
- -[AVTARMaskRenderer encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:camDepthDebug:]
- -[AVTMemoji _invalidateAOImage]
- -[AVTMemoji _updateAO]
- -[AVTMemoji componentForType:]
- -[AVTMemoji components]
- -[AVTMemoji createSkinAO]
- -[AVTMemoji invalidate]
- -[AVTPreset applyPresetByChangingComponentsOfMemoji:animated:]
- -[AVTStickerConfiguration assetsPath]
- -[AVTStickerConfiguration configurationDictionary]
- -[AVTStickerConfiguration hasLoadedFromConfiguration]
- -[AVTStickerConfiguration setAssetsPath:]
- -[AVTStickerConfiguration setConfigurationDictionary:]
- -[AVTStickerConfiguration setHasLoadedFromConfiguration:]
- GCC_except_table105
- GCC_except_table119
- GCC_except_table132
- GCC_except_table172
- GCC_except_table203
- GCC_except_table28
- GCC_except_table47
- GCC_except_table76
- GCC_except_table86
- GCC_except_table90
- _AVTGetCapturedDepthTexture
- _AVTPrecompiledStickerPackPlist.onceToken.1819
- _AVTPrecompiledStickerPackPlist.onceToken.1822
- _AVTPrecompiledStickerPackPlist.onceToken.2186
- _AVTPrecompiledStickerPackPlist.onceToken.2189
- _AVTPrecompiledStickerPackPlist.onceToken.2205
- _AVTPrecompiledStickerPackPlist.onceToken.2208
- _AVTPrecompiledStickerPackPlist.onceToken.2224
- _AVTPrecompiledStickerPackPlist.onceToken.2227
- _AVTPrecompiledStickerPackPlist.onceToken.2249
- _OBJC_IVAR_$_AVTARMaskRenderer._debugCamDepthPipelineState
- _OBJC_IVAR_$_AVTARMaskRenderer._debugCamDepthTexture
- _OBJC_IVAR_$_AVTMemoji._aoValid
- _OBJC_IVAR_$_AVTRendererViewTransitionTechnique._renderPassDescriptor
- ___22-[AVTMemoji _updateAO]_block_invoke
- ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.309
- ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.309.cold.1
- ___56-[AVTMemoji updateWrapDeformerIsActiveForComponentType:]_block_invoke.334
- _____AVTPresetLoadPresets_block_invoke.359
- _____AVTPresetLoadPresets_block_invoke.375
- _____AVTPresetLoadPresets_block_invoke.375.cold.1
- _____AVTPresetLoadPresets_block_invoke.375.cold.2
- _____AVTPresetLoadPresets_block_invoke_2.362
- ___block_literal_global.1821
- ___block_literal_global.1824
- ___block_literal_global.2188
- ___block_literal_global.2191
- ___block_literal_global.2207
- ___block_literal_global.2210
- ___block_literal_global.2226
- ___block_literal_global.2229
- ___block_literal_global.2251
- ___block_literal_global.253
- ___block_literal_global.316
- ___block_literal_global.319
- ___block_literal_global.361
- ___block_literal_global.541
- _objc_msgSend$_invalidateAOImage
- _objc_msgSend$_updateAO
- _objc_msgSend$applyPresetByChangingComponentsOfMemoji:animated:
- _objc_msgSend$assetsPath
- _objc_msgSend$componentForType:
- _objc_msgSend$configurationDictionary
- _objc_msgSend$createSkinAO
- _objc_msgSend$encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:camDepthDebug:
- _objc_msgSend$hasLoadedFromConfiguration
- _objc_msgSend$setHasLoadedFromConfiguration:
- _objc_retain_x6
CStrings:
+ "\n * %@"
+ "!2"
+ ":"
+ ": %@"
+ "Error: Coordinator can't perform animated transition without a view"
+ "[AvatarKit] Convert depth texture"
+ "_debugCameraColorTexture"
+ "_debugCameraDepthTexture"
+ "_debugConvertDepthPipelineState"
+ "_invalidateSkinAO"
+ "_locked_invalidate"
+ "_renderPipelineStateDescriptor"
+ "_skinAOIsValid"
+ "_updateSkinAO"
+ "_viewIsOpaque"
+ "avt_blurMaskX_high_fragment"
+ "avt_blurMaskY_high_fragment"
+ "avt_composite_debug_fragment"
+ "avt_composite_fragment_legacy"
+ "avt_composite_fragment_matte"
+ "avt_composite_fragment_matte_chroma_key"
+ "avt_convert_depth_to_debug_color_fragment"
+ "avt_fullscreen_quad_orientation_vertex"
+ "avt_fullscreen_quad_vertex"
+ "avt_generate_masks_fragment"
+ "avt_view_transition_generic_fragment"
+ "avt_view_transition_vertex"
+ "createSkinCombinedAOImage"
+ "encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:cameraDepthDebug:"
+ "newComponent"
+ "rebuildRenderPipelineStateIfNeededForPixelFormat:"
+ "stringWithString:"
+ "{?=\"color0PixelFormat\"Q\"depthPixelFormat\"Q\"colorBlendingEnabled\"B\"colorRGBBlendOperation\"Q\"colorSourceRGBBlendFactor\"Q\"colorDestinationRGBBlendFactor\"Q\"colorAlphaBlendOperation\"Q\"colorSourceAlphaBlendFactor\"Q\"colorDestinationAlphaBlendFactor\"Q\"vertexFunctionName\"@\"NSString\"\"fragmentFunctionName\"@\"NSString\"\"rasterSampleCount\"Q}"
- "AVT_blurMaskX_high_fragment"
- "AVT_blurMaskY_high_fragment"
- "AVT_composite_fragment_legacy"
- "AVT_composite_fragment_matte"
- "AVT_composite_fragment_matte_chroma_key"
- "AVT_dbg_camDepth"
- "AVT_dbg_fragment"
- "AVT_fullscreen_quad_orientation_vertex"
- "AVT_fullscreen_quad_vertex"
- "AVT_mask_fragment"
- "AVT_view_transition_generic_fragment"
- "AVT_view_transition_vertex"
- "T@\"NSDictionary\",&,N,V_configurationDictionary"
- "T@\"NSString\",&,N,V_assetsPath"
- "TB,N,V_hasLoadedFromConfiguration"
- "[AvatarKit] Generate depth texture"
- "_aoValid"
- "_debugCamDepthPipelineState"
- "_debugCamDepthTexture"
- "_invalidateAOImage"
- "_updateAO"
- "applyPresetByChangingComponentsOfMemoji:animated:"
- "assetsPath"
- "componentForType:"
- "components"
- "configurationDictionary"
- "createSkinAO"
- "encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:camDepthDebug:"
- "hasLoadedFromConfiguration"
- "setAssetsPath:"
- "setConfigurationDictionary:"
- "setHasLoadedFromConfiguration:"

```
