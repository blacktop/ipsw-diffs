## AvatarKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/AvatarKit.framework/Versions/A/AvatarKit`

```diff

 346.201.0.0.0
-  __TEXT.__text: 0x5e6e0
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x3c2c
-  __TEXT.__const: 0x7b8
+  __TEXT.__text: 0x5e6b0
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x416c
+  __TEXT.__const: 0x7c8
   __TEXT.__cstring: 0x1d76c
   __TEXT.__oslogstring: 0x1c74
-  __TEXT.__gcc_except_tab: 0xd9c
+  __TEXT.__gcc_except_tab: 0xda0
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x1598
+  __TEXT.__unwind_info: 0x1608
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x8f9
   __TEXT.__objc_methname: 0xd0f4

   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e90
+  __DATA_CONST.__objc_selrefs: 0x3040
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x62590
-  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__const: 0x8c0
   __AUTH_CONST.__cfstring: 0x24700
-  __AUTH_CONST.__objc_const: 0xb000
+  __AUTH_CONST.__objc_const: 0xa660
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x7bc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A279A68D-323A-3797-B64B-7CACC45E8E3D
-  Functions: 1915
-  Symbols:   5448
+  UUID: FD04200E-4568-35B3-A86B-1B11CF0EBB0D
+  Functions: 1989
+  Symbols:   5526
   CStrings:  12264
 
Symbols:
+ +[AVTAnimoji animojiNames].cold.1
+ +[AVTAssetLibrary sharedAssetLibrary].cold.1
+ +[AVTAvatarBodyPose posesInPosePack:].cold.2
+ +[AVTAvatarPose friendlyPose].cold.1
+ +[AVTAvatarPose neutralPose].cold.1
+ +[AVTClassicPresentationConfiguration sharedConfiguration].cold.1
+ +[AVTMemoji neutralMemojiDataRepresentation].cold.1
+ +[AVTPreset availablePresetsForCategory:].cold.1
+ +[AVTSnapshotBuilder sharedInstance].cold.1
+ +[AVTStickerCamera stickerCameraCache].cold.1
+ +[AVTStickerProp stickerPropCache].cold.1
+ +[AVTStickerShaderModifier shaderModifierCache].cold.1
+ +[AVTStickerShaderModifierProperty shaderModifierPropertyCache].cold.1
+ -[AVTAvatar avatarCommonInit].cold.1
+ -[AVTAvatar setupEyeOrientationAndReflections].cold.2
+ -[AVTAvatar setupEyeOrientationAndReflections].cold.3
+ -[AVTAvatar updateEyeOrientationAndReflections].cold.1
+ -[AVTAvatar updateEyeOrientationAndReflections].cold.2
+ -[AVTAvatar updateMorpherDrivenMaterialsWithDeltaTime:].cold.1
+ -[AVTPhysicsController removeFromPhysicsWorld:].cold.2
+ -[AVTPhysicsController resetToPhysicsState:assumeRestStateIfNil:].cold.1
+ -[AVTPreset enumerateVariantDependenciesOfKind:block:].cold.1
+ -[AVTPreset enumerateVariantDependenciesOfKind:block:].cold.2
+ -[AVTPreset enumerateVariantDependenciesOfKind:block:].cold.3
+ -[AVTSnapshotHelper newCGImageWithRenderer:antialiasingMode:pixelWidth:pixelHeight:error:].cold.3
+ -[AVTStickerGenerator initWithAvatar:].cold.1
+ -[SCNNode(AVTExtension) avt_enableSubdivisionOnHierarchyWithQuality:animoji:].cold.1
+ AVTAvatarKitSnapshotVersionNumber.cold.1
+ AVTAvatarKitSnapshotVersionString.cold.1
+ AVTBlendShapeLocationFromARIndex.cold.1
+ AVTBlendShapeLocationToARIndex.cold.1
+ AVTColorCategoryFromString.cold.1
+ AVTComponentTypeFromString.cold.1
+ AVTEditorMetadata.cold.1
+ AVTGetNeutralZ.cold.1
+ AVTInitializeShaderCache.cold.1
+ AVTMorphTargetNameIsUsedForFaceAnimation.cold.1
+ AVTPlistDatabaseMemojiAssetWithIdentifier.cold.1
+ AVTPlistDatabaseMemojiAssetsForComponentType.cold.1
+ AVTPrecompiledAnimojiSpecializationSettings.cold.1
+ AVTPrecompiledMemojiAssetWithIdentifier.cold.1
+ AVTPrecompiledMemojiAssetsForComponentType.cold.1
+ AVTPrecompiledMemojiColorPalettes.cold.1
+ AVTPrecompiledMemojiCompositorPropertyNames.cold.1
+ AVTPrecompiledMemojiEditorMetadata.cold.1
+ AVTPrecompiledMemojiPrereleaseEditorMetadata.cold.1
+ AVTPrecompiledMemojiPresetPlist.cold.1
+ AVTPrecompiledStickerPackPlist.cold.10
+ AVTPrecompiledStickerPackPlist.cold.11
+ AVTPrecompiledStickerPackPlist.cold.2
+ AVTPrecompiledStickerPackPlist.cold.3
+ AVTPrecompiledStickerPackPlist.cold.4
+ AVTPrecompiledStickerPackPlist.cold.5
+ AVTPrecompiledStickerPackPlist.cold.6
+ AVTPrecompiledStickerPackPlist.cold.7
+ AVTPrecompiledStickerPackPlist.cold.8
+ AVTPrecompiledStickerPackPlist.cold.9
+ AVTPrecompiledToyboxAnimojiNames.cold.1
+ AVTPrereleaseEditorMetadata.cold.1
+ AVTPresetCategoryFromString.cold.1
+ AVTSceneKitSnapshotVersionString.cold.1
+ GCC_except_table203
+ GCC_except_table66
+ _AVTMemojiRandomize.cold.1
+ _AVTMemojiRandomize.cold.2
+ _AVTMemojiRandomize.cold.3
+ _AVTPoseRoundingBehaviour.cold.1
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __32+[AVTAvatarBodyPose neutralPose]_block_invoke.cold.1
+ _objc_retainAutoreleasedReturnValue
+ avt_default_log.cold.1
- -[AVTViewTransitionHelper transitionCoordinatorOutOfStickerConfigurationWithDuration:style:options:avatar:].cold.1
- -[AVTViewTransitionHelper transitionCoordinatorToStickerConfiguration:duration:style:options:avatar:].cold.1
- -[AVTViewTransitionHelper transitionCoordinatorToStickerConfiguration:duration:style:options:avatar:].cold.2
- -[AVTViewTransitionHelper transitionViewToStickerConfiguration:fallbackPose:duration:style:avatar:completionHandler:simultaneousAnimationsBlock:].cold.1
- -[AVTViewTransitionHelper transitionViewToStickerConfiguration:fallbackPose:duration:style:avatar:completionHandler:simultaneousAnimationsBlock:].cold.2
- GCC_except_table200
- GCC_except_table68
- __62-[AVTComponentInstance _initializeVariantSkinnerPairsIfNeeded]_block_invoke_2.cold.1
- __62-[AVTComponentInstance _initializeVariantSkinnerPairsIfNeeded]_block_invoke_2.cold.2

```
