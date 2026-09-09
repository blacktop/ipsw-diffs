## Tungsten

> `/System/Library/PrivateFrameworks/Tungsten.framework/Tungsten`

```diff

-912.0.234.0.0
-  __TEXT.__text: 0xfcecc
+912.0.235.0.0
+  __TEXT.__text: 0xfcefc
   __TEXT.__objc_methlist: 0x11ca8
   __TEXT.__const: 0x39c0
   __TEXT.__constg_swiftt: 0x244

   __TEXT.__swift5_fieldmd: 0x7c8
   __TEXT.__swift5_protos: 0x8
   __TEXT.__cstring: 0xd784
-  __TEXT.__gcc_except_tab: 0x350c
+  __TEXT.__gcc_except_tab: 0x3510
   __TEXT.__oslogstring: 0x25bb
   __TEXT.__ustring: 0x3c
   __TEXT.__unwind_info: 0x4658
Functions:
~ ___101-[PXGMetalRenderer _populateEffectSprites:spriteRenderDataStore:presentationDataStore:metadataStore:]_block_invoke : 588 -> 592
~ -[PXGSublayoutDataStore enumerateSublayoutsInRange:options:usingBlock:] : 284 -> 288
~ -[PXGMetalRenderer _pipelinesLock_resizePipelinesStorageIfNeeded] : 180 -> 184
~ -[PXGTextureManager _lookupLock_requestTexturesForSpritesInRange:textureProvider:mediaKind:presentationType:isAppearing:layout:leafSpriteIndexRange:sprites:textureStreamInfos:loadingStatus:] : 1480 -> 1496
~ -[PXGSublayoutDataStore enumerateSublayoutGeometriesInRange:options:usingBlock:] : 352 -> 360
~ ___98-[PXGMetalTextureAtlas addSpriteWithTextureRequestID:thumbnailData:size:bytesPerRow:contentsRect:]_block_invoke_2 : 140 -> 144
~ -[PXGBurstStackEffect configureSiblingSprites:siblingsSpriteIndexRange:siblingsTexture:forMainRenderSpriteRef:mainPresentationSpriteRef:mainSpriteIndex:mainSpriteTexture:screenScale:] : 1040 -> 1036
~ -[PXGDisplayAssetTextureProvider requestTexturesForSpritesInRange:geometries:styles:infos:inLayout:] : 3164 -> 3156
~ -[PXGMetalRenderer _setupYCbCrMatrices] : 396 -> 388
~ ___87+[PXGDiagnosticsSpriteProbe shouldUseDoubleSidedAnimationForSprites:indexes:animation:]_block_invoke : 204 -> 208
~ -[PXGDecoratingLayout normalizedSizeForDecorationType:] : 72 -> 76
~ -[PXGMetalTextureAtlas addSpriteWithTextureRequestID:thumbnailData:size:bytesPerRow:contentsRect:] : 816 -> 812
~ -[PXGSpriteDataStore _mutableSpritesInRange:] : 244 -> 252
~ -[PXGSpriteDataStore spriteAtIndex:] : 136 -> 144
~ -[PXGViewRenderer renderSpritesWithTextures:dataStore:presentationDataStore:presentationMetadataStore:layout:] : 3888 -> 3892
~ ___110-[PXGViewRenderer renderSpritesWithTextures:dataStore:presentationDataStore:presentationMetadataStore:layout:]_block_invoke_5 : 1860 -> 1856
~ ___217-[PXGAnimator computeAnimationStateForTime:inputSpriteDataStore:inputChangeDetails:inputLayout:viewportShift:animationPresentationSpriteDataStore:animationTargetSpriteDataStore:animationChangeDetails:animationLayout:]_block_invoke_10 : 948 -> 952
~ ___217-[PXGAnimator computeAnimationStateForTime:inputSpriteDataStore:inputChangeDetails:inputLayout:viewportShift:animationPresentationSpriteDataStore:animationTargetSpriteDataStore:animationChangeDetails:animationLayout:]_block_invoke_11 : 216 -> 220
```
