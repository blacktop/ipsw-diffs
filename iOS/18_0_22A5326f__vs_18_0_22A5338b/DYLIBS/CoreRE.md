## CoreRE

> `/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE`

```diff

-366.0.20.0.2
-  __TEXT.__text: 0x1219ba4
-  __TEXT.__auth_stubs: 0x65c0
+366.0.22.0.4
+  __TEXT.__text: 0x1229cbc
+  __TEXT.__auth_stubs: 0x65e0
   __TEXT.__objc_methlist: 0x2ea4
-  __TEXT.__const: 0x122670
-  __TEXT.__gcc_except_tab: 0xc580
-  __TEXT.__cstring: 0x8cda3
-  __TEXT.__oslogstring: 0x3b02e
+  __TEXT.__const: 0x122f00
+  __TEXT.__gcc_except_tab: 0xc5a0
+  __TEXT.__cstring: 0x8d227
+  __TEXT.__oslogstring: 0x3b2d8
   __TEXT.__ustring: 0x1a
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x5920
+  __TEXT.__unwind_info: 0x5918
   __TEXT.__objc_classname: 0x753
   __TEXT.__objc_methname: 0xeacf
   __TEXT.__objc_methtype: 0x8d41
   __TEXT.__objc_stubs: 0xb800
   __DATA_CONST.__got: 0xd80
-  __DATA_CONST.__const: 0xac20
+  __DATA_CONST.__const: 0xacb0
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x32f8
+  __AUTH_CONST.__auth_got: 0x3308
   __AUTH_CONST.__auth_ptr: 0x250
-  __AUTH_CONST.__const: 0x78db0
+  __AUTH_CONST.__const: 0x79700
   __AUTH_CONST.__cfstring: 0x95c0
   __AUTH_CONST.__objc_const: 0x83a0
   __AUTH_CONST.__objc_intobj: 0x108

   __AUTH.__thread_vars: 0x90
   __AUTH.__thread_bss: 0x2d9
   __DATA.__objc_ivar: 0x380
-  __DATA.__data: 0x24710
+  __DATA.__data: 0x247a0
   __DATA.__bss: 0x7920
-  __DATA.__common: 0x85a8
+  __DATA.__common: 0x85d8
   __DATA_DIRTY.__objc_ivar: 0x10c
   __DATA_DIRTY.__data: 0x3a8
-  __DATA_DIRTY.__bss: 0x2f678
+  __DATA_DIRTY.__bss: 0x2f648
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 68528
-  Symbols:   78057
-  CStrings:  20241
+  Functions: 68700
+  Symbols:   78253
+  CStrings:  20293
 
Symbols:
+ _RECameraStreamManagerSetARKitPassthrough
+ _RECollisionWorldEnableContactsDetection
+ _RERemoteEffectsComponentGetVersion
+ _RERemoteEffectsComponentSetVersion
+ _RERenderManagerGetCameraStreamManager
+ _RERenderManagerUnsetBackdrop
+ __AXDarkenSystemColors
+ __AXSEnhanceBackgroundContrastEnabled
CStrings:
+ "BackdropPass"
+ "Blur: Caching WorldToView matrix: Left Camera data not available"
+ "Blur: Caching WorldToView matrix: Right Camera data not available"
+ "BlurPlanesRenderFrameData"
+ "BlurPlatterMeshDraw"
+ "BlurReprojectionState was not set."
+ "Camera projection frustums were not properly set. Unable to initialize encoder in SFBSystemShellReprojectAndFilterNode."
+ "CameraStreamContext"
+ "FilteredPassthroughBlurredColor"
+ "FilteredPassthroughBlurredColorSRGB"
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
+ "RenderGraphSFBSystemShellBlurProvider"
+ "SFBSystemShellBlurContext"
+ "SetVCAPassthroughAlias"
+ "SetVCAPassthroughSRGBAlias"
+ "StencilBlurMeshNode"
+ "StencilBlurSetStencil"
+ "SyntheticColor"
+ "SyntheticDepth"
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
+ "applyHitTestData() - component version: %!d(MISSING)"
+ "applyHitTestData() - found activeEntity %!l(MISSING)lu - position: %!f(MISSING), %!f(MISSING), %!f(MISSING)"
+ "bad_any_cast was thrown in -fno-exceptions mode"
+ "engine:BuiltinRenderGraphResources/SFBSystemShell/SFBPbrBlur.rematerial"
+ "engine:BuiltinRenderGraphResources/SFBSystemShell/SFBVCABlur.rematerial"
+ "kernelSFBARKitPassthroughDownsample"
+ "kernelSFBBilerpDownsample4x"
+ "kernelSFBBlurAndFilter"
+ "kernelSFBNoReprojectAndNoBlend"
+ "kernelSFBReprojectAndBlendPassthrough"
+ "kernelSFBReprojectAndSRGBCorrect"
+ "kernelSFBVCABlurAndFilterAndBlendPassthrough"
+ "kernelTiledVCADownsample4x"
+ "reprojectFilteredBlur"
+ "reprojectVCABlur"
- "CalculateBlendedDiffuseIBL"
- "CalculateBlendedSpecularIBL"
- "IBL Blending is not supported for multiple scenes, skip subsequent scenes."
- "Technique Sort - IsGroupedTechnique: %!d(MISSING) TechniqueGroupID: %!d(MISSING) IndexInTechniqueGroup: %!d(MISSING) TechniqueAndMaterialNameHash: %!z(MISSING)u HSRFlush: %!d(MISSING) DescriptorHash: %!z(MISSING)u MeshNameHash: %!l(MISSING)lu CreationOrder: %!d(MISSING)"
- "applyHitTestData() - found activeEntity %!l(MISSING)lu"
- "fsCalculateBlendedDiffuseIBL"
- "fsCalculateBlendedSpecularIBL"

```
