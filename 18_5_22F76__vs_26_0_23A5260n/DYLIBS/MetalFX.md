## MetalFX

> `/System/Library/Frameworks/MetalFX.framework/MetalFX`

```diff

-29.7.6.0.0
-  __TEXT.__text: 0x17740
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x14bc
-  __TEXT.__gcc_except_tab: 0x260c
-  __TEXT.__cstring: 0x18a3
-  __TEXT.__const: 0x200
-  __TEXT.__unwind_info: 0x438
-  __TEXT.__objc_classname: 0x1ca
-  __TEXT.__objc_methname: 0x2c35
-  __TEXT.__objc_methtype: 0x9bc
-  __TEXT.__objc_stubs: 0x1ba0
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x158
-  __DATA_CONST.__objc_classlist: 0x60
+30.8.0.0.0
+  __TEXT.__text: 0x4db8c
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0x3d0c
+  __TEXT.__const: 0x268
+  __TEXT.__gcc_except_tab: 0x834c
+  __TEXT.__cstring: 0x304b
+  __TEXT.__unwind_info: 0xba8
+  __TEXT.__objc_classname: 0x5ba
+  __TEXT.__objc_methname: 0x5385
+  __TEXT.__objc_methtype: 0xf3e
+  __TEXT.__objc_stubs: 0x2da0
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e8
-  __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0xd58
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2060
-  __AUTH_CONST.__objc_const: 0x3438
-  __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0xe88
-  __DATA.__objc_ivar: 0x344
-  __DATA.__data: 0x240
-  __DATA.__bss: 0x48
-  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_CONST.__objc_selrefs: 0x1038
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_arraydata: 0x2d40
+  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x3d20
+  __AUTH_CONST.__objc_const: 0xa630
+  __AUTH_CONST.__objc_intobj: 0x300
+  __AUTH_CONST.__objc_arrayobj: 0x2b98
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0xb30
+  __DATA.__data: 0x840
+  __DATA.__bss: 0x1b0
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libAppleArchive.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9FC736D3-0E6A-385C-A5F7-D1A990AB48DF
-  Functions: 388
-  Symbols:   1517
-  CStrings:  1142
+  UUID: 17208DB9-50C1-384E-9C0F-0D5CD11E7E9F
+  Functions: 1168
+  Symbols:   4144
+  CStrings:  2067
 
Symbols:
+ +[MTLFXFrameInterpolatorDescriptor supportsDevice:]
+ +[MTLFXFrameInterpolatorDescriptor supportsMetal4FX:]
+ +[MTLFXSpatialScalerDescriptor supportsMetal4FX:]
+ +[MTLFXTemporalDenoisedScalerDescriptor supportedInputContentMaxScaleForDevice:]
+ +[MTLFXTemporalDenoisedScalerDescriptor supportedInputContentMinScaleForDevice:]
+ +[MTLFXTemporalDenoisedScalerDescriptor supportsDevice:]
+ +[MTLFXTemporalDenoisedScalerDescriptor supportsMetal4FX:]
+ +[MTLFXTemporalScalerDescriptor supportsMetal4FX:]
+ -[MFXTemporalDenoisingScalingEffectDescriptor newTemporalDenoisingScalingEffectWithDevice:]
+ -[MTLFXFrameInterpolatorDescriptor .cxx_destruct]
+ -[MTLFXFrameInterpolatorDescriptor colorTextureFormat]
+ -[MTLFXFrameInterpolatorDescriptor copyWithZone:]
+ -[MTLFXFrameInterpolatorDescriptor denoiserScaler4]
+ -[MTLFXFrameInterpolatorDescriptor denoiserScaler]
+ -[MTLFXFrameInterpolatorDescriptor depthInverted]
+ -[MTLFXFrameInterpolatorDescriptor depthTextureFormat]
+ -[MTLFXFrameInterpolatorDescriptor height]
+ -[MTLFXFrameInterpolatorDescriptor inputHeight]
+ -[MTLFXFrameInterpolatorDescriptor inputWidth]
+ -[MTLFXFrameInterpolatorDescriptor maskTextureFormat]
+ -[MTLFXFrameInterpolatorDescriptor motionTextureFormat]
+ -[MTLFXFrameInterpolatorDescriptor newFrameInterpolatorWithDevice:]
+ -[MTLFXFrameInterpolatorDescriptor newFrameInterpolatorWithDevice:compiler:]
+ -[MTLFXFrameInterpolatorDescriptor outputHeight]
+ -[MTLFXFrameInterpolatorDescriptor outputTextureFormat]
+ -[MTLFXFrameInterpolatorDescriptor outputWidth]
+ -[MTLFXFrameInterpolatorDescriptor scaler4]
+ -[MTLFXFrameInterpolatorDescriptor scaler]
+ -[MTLFXFrameInterpolatorDescriptor setColorTextureFormat:]
+ -[MTLFXFrameInterpolatorDescriptor setDenoiserScaler4:]
+ -[MTLFXFrameInterpolatorDescriptor setDenoiserScaler:]
+ -[MTLFXFrameInterpolatorDescriptor setDepthInverted:]
+ -[MTLFXFrameInterpolatorDescriptor setDepthTextureFormat:]
+ -[MTLFXFrameInterpolatorDescriptor setHeight:]
+ -[MTLFXFrameInterpolatorDescriptor setInputHeight:]
+ -[MTLFXFrameInterpolatorDescriptor setInputWidth:]
+ -[MTLFXFrameInterpolatorDescriptor setMaskTextureFormat:]
+ -[MTLFXFrameInterpolatorDescriptor setMotionTextureFormat:]
+ -[MTLFXFrameInterpolatorDescriptor setOutputHeight:]
+ -[MTLFXFrameInterpolatorDescriptor setOutputTextureFormat:]
+ -[MTLFXFrameInterpolatorDescriptor setOutputWidth:]
+ -[MTLFXFrameInterpolatorDescriptor setScaler4:]
+ -[MTLFXFrameInterpolatorDescriptor setScaler:]
+ -[MTLFXFrameInterpolatorDescriptor setUITextureFormat:]
+ -[MTLFXFrameInterpolatorDescriptor setVersion:]
+ -[MTLFXFrameInterpolatorDescriptor setWidth:]
+ -[MTLFXFrameInterpolatorDescriptor uiTextureFormat]
+ -[MTLFXFrameInterpolatorDescriptor version]
+ -[MTLFXFrameInterpolatorDescriptor width]
+ -[MTLFXSpatialScalerDescriptor newSpatialScalerWithDevice:compiler:]
+ -[MTLFXTemporalDenoisedScalerDescriptor colorTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor copyWithZone:]
+ -[MTLFXTemporalDenoisedScalerDescriptor denoiseStrengthMaskTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor depthTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor diffuseAlbedoTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor enableInputContentProperties]
+ -[MTLFXTemporalDenoisedScalerDescriptor inputContentMaxScale]
+ -[MTLFXTemporalDenoisedScalerDescriptor inputContentMinScale]
+ -[MTLFXTemporalDenoisedScalerDescriptor inputHeight]
+ -[MTLFXTemporalDenoisedScalerDescriptor inputWidth]
+ -[MTLFXTemporalDenoisedScalerDescriptor isAutoExposureEnabled]
+ -[MTLFXTemporalDenoisedScalerDescriptor isDenoiseStrengthMaskTextureEnabled]
+ -[MTLFXTemporalDenoisedScalerDescriptor isInputContentPropertiesEnabled]
+ -[MTLFXTemporalDenoisedScalerDescriptor isReactiveMaskTextureEnabled]
+ -[MTLFXTemporalDenoisedScalerDescriptor isSpecularHitDistanceTextureEnabled]
+ -[MTLFXTemporalDenoisedScalerDescriptor isTransparencyOverlayTextureEnabled]
+ -[MTLFXTemporalDenoisedScalerDescriptor motionTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor newTemporalDenoisedScalerWithDevice:]
+ -[MTLFXTemporalDenoisedScalerDescriptor newTemporalDenoisedScalerWithDevice:compiler:]
+ -[MTLFXTemporalDenoisedScalerDescriptor newTemporalDenoisedScalerWithHistoryTexture:]
+ -[MTLFXTemporalDenoisedScalerDescriptor normalTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor outputHeight]
+ -[MTLFXTemporalDenoisedScalerDescriptor outputTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor outputWidth]
+ -[MTLFXTemporalDenoisedScalerDescriptor reactiveMaskTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor requiresSynchronousInitialization]
+ -[MTLFXTemporalDenoisedScalerDescriptor roughnessTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor setAutoExposureEnabled:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setColorTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setDenoiseStrengthMaskTextureEnabled:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setDenoiseStrengthMaskTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setDepthTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setDiffuseAlbedoTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setEnableInputContentProperties:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setInputContentMaxScale:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setInputContentMinScale:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setInputContentPropertiesEnabled:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setInputHeight:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setInputWidth:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setMotionTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setNormalTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setOutputHeight:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setOutputTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setOutputWidth:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setReactiveMaskTextureEnabled:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setReactiveMaskTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setRequiresSynchronousInitialization:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setRoughnessTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setSpecularAlbedoTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setSpecularHitDistanceTextureEnabled:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setSpecularHitDistanceTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setTransparencyOverlayTextureEnabled:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setTransparencyOverlayTextureFormat:]
+ -[MTLFXTemporalDenoisedScalerDescriptor setVersion:]
+ -[MTLFXTemporalDenoisedScalerDescriptor specularAlbedoTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor specularHitDistanceTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor transparencyOverlayTextureFormat]
+ -[MTLFXTemporalDenoisedScalerDescriptor version]
+ -[MTLFXTemporalScalerDescriptor newTemporalScalerWithDevice:compiler:]
+ -[MTLFXTemporalScalerDescriptor newTemporalScalerWithHistoryTexture:compiler:]
+ -[_M4FXFrameInterpolatorEffect .cxx_destruct]
+ -[_M4FXFrameInterpolatorEffect aspectRatio]
+ -[_M4FXFrameInterpolatorEffect colorTextureBarrierStages]
+ -[_M4FXFrameInterpolatorEffect colorTextureFormat]
+ -[_M4FXFrameInterpolatorEffect colorTextureUsage]
+ -[_M4FXFrameInterpolatorEffect colorTexture]
+ -[_M4FXFrameInterpolatorEffect compositedUITexture]
+ -[_M4FXFrameInterpolatorEffect debugTexture]
+ -[_M4FXFrameInterpolatorEffect deltaTime]
+ -[_M4FXFrameInterpolatorEffect depthTextureFormat]
+ -[_M4FXFrameInterpolatorEffect depthTextureUsage]
+ -[_M4FXFrameInterpolatorEffect depthTexture]
+ -[_M4FXFrameInterpolatorEffect encodeToCommandBuffer:]
+ -[_M4FXFrameInterpolatorEffect farPlane]
+ -[_M4FXFrameInterpolatorEffect fence]
+ -[_M4FXFrameInterpolatorEffect fieldOfView]
+ -[_M4FXFrameInterpolatorEffect initWithDevice:compiler:descriptor:]
+ -[_M4FXFrameInterpolatorEffect inputHeight]
+ -[_M4FXFrameInterpolatorEffect inputWidth]
+ -[_M4FXFrameInterpolatorEffect isDepthReversed]
+ -[_M4FXFrameInterpolatorEffect isUITextureComposited]
+ -[_M4FXFrameInterpolatorEffect jitterOffsetX]
+ -[_M4FXFrameInterpolatorEffect jitterOffsetY]
+ -[_M4FXFrameInterpolatorEffect motionTextureFormat]
+ -[_M4FXFrameInterpolatorEffect motionTextureUsage]
+ -[_M4FXFrameInterpolatorEffect motionTexture]
+ -[_M4FXFrameInterpolatorEffect motionVectorScaleX]
+ -[_M4FXFrameInterpolatorEffect motionVectorScaleY]
+ -[_M4FXFrameInterpolatorEffect nearPlane]
+ -[_M4FXFrameInterpolatorEffect outputHeight]
+ -[_M4FXFrameInterpolatorEffect outputTextureBarrierStages]
+ -[_M4FXFrameInterpolatorEffect outputTextureFormat]
+ -[_M4FXFrameInterpolatorEffect outputTextureUsage]
+ -[_M4FXFrameInterpolatorEffect outputTexture]
+ -[_M4FXFrameInterpolatorEffect outputWidth]
+ -[_M4FXFrameInterpolatorEffect prevColorTexture]
+ -[_M4FXFrameInterpolatorEffect reset]
+ -[_M4FXFrameInterpolatorEffect setAspectRatio:]
+ -[_M4FXFrameInterpolatorEffect setColorTexture:]
+ -[_M4FXFrameInterpolatorEffect setColorTextureBarrierStages:]
+ -[_M4FXFrameInterpolatorEffect setCompositedUITexture:]
+ -[_M4FXFrameInterpolatorEffect setDebugTexture:]
+ -[_M4FXFrameInterpolatorEffect setDeltaTime:]
+ -[_M4FXFrameInterpolatorEffect setDepthReversed:]
+ -[_M4FXFrameInterpolatorEffect setDepthTexture:]
+ -[_M4FXFrameInterpolatorEffect setFarPlane:]
+ -[_M4FXFrameInterpolatorEffect setFence:]
+ -[_M4FXFrameInterpolatorEffect setFieldOfView:]
+ -[_M4FXFrameInterpolatorEffect setIsUITextureComposited:]
+ -[_M4FXFrameInterpolatorEffect setJitterOffsetX:]
+ -[_M4FXFrameInterpolatorEffect setJitterOffsetY:]
+ -[_M4FXFrameInterpolatorEffect setMotionTexture:]
+ -[_M4FXFrameInterpolatorEffect setMotionVectorScaleX:]
+ -[_M4FXFrameInterpolatorEffect setMotionVectorScaleY:]
+ -[_M4FXFrameInterpolatorEffect setNearPlane:]
+ -[_M4FXFrameInterpolatorEffect setOutputTexture:]
+ -[_M4FXFrameInterpolatorEffect setPrevColorTexture:]
+ -[_M4FXFrameInterpolatorEffect setReset:]
+ -[_M4FXFrameInterpolatorEffect setShouldResetHistory:]
+ -[_M4FXFrameInterpolatorEffect setUITexture:]
+ -[_M4FXFrameInterpolatorEffect shouldResetHistory]
+ -[_M4FXFrameInterpolatorEffect uiTextureFormat]
+ -[_M4FXFrameInterpolatorEffect uiTextureUsage]
+ -[_M4FXFrameInterpolatorEffect uiTexture]
+ -[_M4FXTemporalDenoisingScalingEffect .cxx_construct]
+ -[_M4FXTemporalDenoisingScalingEffect .cxx_destruct]
+ -[_M4FXTemporalDenoisingScalingEffect colorTextureBarrierStages]
+ -[_M4FXTemporalDenoisingScalingEffect colorTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect colorTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect colorTexture]
+ -[_M4FXTemporalDenoisingScalingEffect dealloc]
+ -[_M4FXTemporalDenoisingScalingEffect debugTexture]
+ -[_M4FXTemporalDenoisingScalingEffect denoiseStrengthMaskTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect denoiseStrengthMaskTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect denoiseStrengthMaskTexture]
+ -[_M4FXTemporalDenoisingScalingEffect depthTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect depthTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect depthTexture]
+ -[_M4FXTemporalDenoisingScalingEffect diffuseAlbedoTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect diffuseAlbedoTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect diffuseAlbedoTexture]
+ -[_M4FXTemporalDenoisingScalingEffect dilatedMotionVectors]
+ -[_M4FXTemporalDenoisingScalingEffect encodeToCommandBuffer:]
+ -[_M4FXTemporalDenoisingScalingEffect exposureTexture]
+ -[_M4FXTemporalDenoisingScalingEffect fence]
+ -[_M4FXTemporalDenoisingScalingEffect initWithDevice:compiler:descriptor:history:]
+ -[_M4FXTemporalDenoisingScalingEffect initWithDevice:compiler:descriptor:history:].cold.1
+ -[_M4FXTemporalDenoisingScalingEffect initWithDevice:compiler:descriptor:history:].cold.2
+ -[_M4FXTemporalDenoisingScalingEffect inputContentHeight]
+ -[_M4FXTemporalDenoisingScalingEffect inputContentMaxScale]
+ -[_M4FXTemporalDenoisingScalingEffect inputContentMinScale]
+ -[_M4FXTemporalDenoisingScalingEffect inputContentWidth]
+ -[_M4FXTemporalDenoisingScalingEffect inputHeight]
+ -[_M4FXTemporalDenoisingScalingEffect inputWidth]
+ -[_M4FXTemporalDenoisingScalingEffect isDepthReversed]
+ -[_M4FXTemporalDenoisingScalingEffect jitterOffsetX]
+ -[_M4FXTemporalDenoisingScalingEffect jitterOffsetY]
+ -[_M4FXTemporalDenoisingScalingEffect jitterOffset]
+ -[_M4FXTemporalDenoisingScalingEffect motionTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect motionTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect motionTexture]
+ -[_M4FXTemporalDenoisingScalingEffect motionVectorScaleX]
+ -[_M4FXTemporalDenoisingScalingEffect motionVectorScaleY]
+ -[_M4FXTemporalDenoisingScalingEffect motionVectorScale]
+ -[_M4FXTemporalDenoisingScalingEffect normalTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect normalTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect normalTexture]
+ -[_M4FXTemporalDenoisingScalingEffect outputHeight]
+ -[_M4FXTemporalDenoisingScalingEffect outputTextureBarrierStages]
+ -[_M4FXTemporalDenoisingScalingEffect outputTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect outputTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect outputTexture]
+ -[_M4FXTemporalDenoisingScalingEffect outputWidth]
+ -[_M4FXTemporalDenoisingScalingEffect preExposure]
+ -[_M4FXTemporalDenoisingScalingEffect reactiveMaskTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect reactiveMaskTexture]
+ -[_M4FXTemporalDenoisingScalingEffect reactiveTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect reset]
+ -[_M4FXTemporalDenoisingScalingEffect reversedDepth]
+ -[_M4FXTemporalDenoisingScalingEffect roughnessTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect roughnessTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect roughnessTexture]
+ -[_M4FXTemporalDenoisingScalingEffect setColorTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setColorTextureBarrierStages:]
+ -[_M4FXTemporalDenoisingScalingEffect setDebugTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setDenoiseStrengthMaskTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setDepthReversed:]
+ -[_M4FXTemporalDenoisingScalingEffect setDepthTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setDiffuseAlbedoTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setExposureTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setFence:]
+ -[_M4FXTemporalDenoisingScalingEffect setInputContentHeight:]
+ -[_M4FXTemporalDenoisingScalingEffect setInputContentWidth:]
+ -[_M4FXTemporalDenoisingScalingEffect setJitterOffset:]
+ -[_M4FXTemporalDenoisingScalingEffect setJitterOffsetX:]
+ -[_M4FXTemporalDenoisingScalingEffect setJitterOffsetY:]
+ -[_M4FXTemporalDenoisingScalingEffect setMotionTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setMotionVectorScale:]
+ -[_M4FXTemporalDenoisingScalingEffect setMotionVectorScaleX:]
+ -[_M4FXTemporalDenoisingScalingEffect setMotionVectorScaleY:]
+ -[_M4FXTemporalDenoisingScalingEffect setNormalTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setOutputTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setPreExposure:]
+ -[_M4FXTemporalDenoisingScalingEffect setReactiveMaskTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setReset:]
+ -[_M4FXTemporalDenoisingScalingEffect setReversedDepth:]
+ -[_M4FXTemporalDenoisingScalingEffect setRoughnessTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setShouldResetHistory:]
+ -[_M4FXTemporalDenoisingScalingEffect setSpecularAlbedoTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setSpecularHitDistanceTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setTransparencyOverlayTexture:]
+ -[_M4FXTemporalDenoisingScalingEffect setViewToClipMatrix:]
+ -[_M4FXTemporalDenoisingScalingEffect setWorldToViewMatrix:]
+ -[_M4FXTemporalDenoisingScalingEffect shouldResetHistory]
+ -[_M4FXTemporalDenoisingScalingEffect specularAlbedoTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect specularAlbedoTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect specularAlbedoTexture]
+ -[_M4FXTemporalDenoisingScalingEffect specularHitDistanceTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect specularHitDistanceTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect specularHitDistanceTexture]
+ -[_M4FXTemporalDenoisingScalingEffect transparencyOverlayTextureFormat]
+ -[_M4FXTemporalDenoisingScalingEffect transparencyOverlayTextureUsage]
+ -[_M4FXTemporalDenoisingScalingEffect transparencyOverlayTexture]
+ -[_M4FXTemporalDenoisingScalingEffect viewToClipMatrix]
+ -[_M4FXTemporalDenoisingScalingEffect worldToViewMatrix]
+ -[_M4FXTemporalScalingEffectV4 .cxx_construct]
+ -[_M4FXTemporalScalingEffectV4 .cxx_destruct]
+ -[_M4FXTemporalScalingEffectV4 colorTextureBarrierStages]
+ -[_M4FXTemporalScalingEffectV4 colorTextureFormat]
+ -[_M4FXTemporalScalingEffectV4 colorTextureUsage]
+ -[_M4FXTemporalScalingEffectV4 colorTexture]
+ -[_M4FXTemporalScalingEffectV4 currentViewToClipMatrix]
+ -[_M4FXTemporalScalingEffectV4 currentWorldToViewMatrix]
+ -[_M4FXTemporalScalingEffectV4 dealloc]
+ -[_M4FXTemporalScalingEffectV4 debugTexture]
+ -[_M4FXTemporalScalingEffectV4 depthTextureFormat]
+ -[_M4FXTemporalScalingEffectV4 depthTextureUsage]
+ -[_M4FXTemporalScalingEffectV4 depthTexture]
+ -[_M4FXTemporalScalingEffectV4 dilatedMotionVectors]
+ -[_M4FXTemporalScalingEffectV4 encodeToCommandBuffer:]
+ -[_M4FXTemporalScalingEffectV4 executionMode]
+ -[_M4FXTemporalScalingEffectV4 exposureTexture]
+ -[_M4FXTemporalScalingEffectV4 fence]
+ -[_M4FXTemporalScalingEffectV4 initWithDevice:descriptor:compiler:history:]
+ -[_M4FXTemporalScalingEffectV4 initWithDevice:descriptor:compiler:history:].cold.1
+ -[_M4FXTemporalScalingEffectV4 inputContentHeight]
+ -[_M4FXTemporalScalingEffectV4 inputContentMaxScale]
+ -[_M4FXTemporalScalingEffectV4 inputContentMinScale]
+ -[_M4FXTemporalScalingEffectV4 inputContentWidth]
+ -[_M4FXTemporalScalingEffectV4 inputHeight]
+ -[_M4FXTemporalScalingEffectV4 inputWidth]
+ -[_M4FXTemporalScalingEffectV4 isDepthReversed]
+ -[_M4FXTemporalScalingEffectV4 jitterOffsetX]
+ -[_M4FXTemporalScalingEffectV4 jitterOffsetY]
+ -[_M4FXTemporalScalingEffectV4 jitterOffset]
+ -[_M4FXTemporalScalingEffectV4 motionTextureFormat]
+ -[_M4FXTemporalScalingEffectV4 motionTextureUsage]
+ -[_M4FXTemporalScalingEffectV4 motionTexture]
+ -[_M4FXTemporalScalingEffectV4 motionVectorScaleX]
+ -[_M4FXTemporalScalingEffectV4 motionVectorScaleY]
+ -[_M4FXTemporalScalingEffectV4 motionVectorScale]
+ -[_M4FXTemporalScalingEffectV4 outputHeight]
+ -[_M4FXTemporalScalingEffectV4 outputTextureBarrierStages]
+ -[_M4FXTemporalScalingEffectV4 outputTextureFormat]
+ -[_M4FXTemporalScalingEffectV4 outputTextureUsage]
+ -[_M4FXTemporalScalingEffectV4 outputTexture]
+ -[_M4FXTemporalScalingEffectV4 outputWidth]
+ -[_M4FXTemporalScalingEffectV4 preExposure]
+ -[_M4FXTemporalScalingEffectV4 previousJitterOffset]
+ -[_M4FXTemporalScalingEffectV4 previousViewToClipMatrix]
+ -[_M4FXTemporalScalingEffectV4 previousWorldToViewMatrix]
+ -[_M4FXTemporalScalingEffectV4 reactiveMaskTextureFormat]
+ -[_M4FXTemporalScalingEffectV4 reactiveMaskTexture]
+ -[_M4FXTemporalScalingEffectV4 reactiveTextureUsage]
+ -[_M4FXTemporalScalingEffectV4 reset]
+ -[_M4FXTemporalScalingEffectV4 reversedDepth]
+ -[_M4FXTemporalScalingEffectV4 setColorTexture:]
+ -[_M4FXTemporalScalingEffectV4 setColorTextureBarrierStages:]
+ -[_M4FXTemporalScalingEffectV4 setCurrentViewToClipMatrix:]
+ -[_M4FXTemporalScalingEffectV4 setCurrentWorldToViewMatrix:]
+ -[_M4FXTemporalScalingEffectV4 setDebugTexture:]
+ -[_M4FXTemporalScalingEffectV4 setDepthReversed:]
+ -[_M4FXTemporalScalingEffectV4 setDepthTexture:]
+ -[_M4FXTemporalScalingEffectV4 setExposureTexture:]
+ -[_M4FXTemporalScalingEffectV4 setFence:]
+ -[_M4FXTemporalScalingEffectV4 setInputContentHeight:]
+ -[_M4FXTemporalScalingEffectV4 setInputContentWidth:]
+ -[_M4FXTemporalScalingEffectV4 setJitterOffset:]
+ -[_M4FXTemporalScalingEffectV4 setJitterOffsetX:]
+ -[_M4FXTemporalScalingEffectV4 setJitterOffsetY:]
+ -[_M4FXTemporalScalingEffectV4 setMotionTexture:]
+ -[_M4FXTemporalScalingEffectV4 setMotionVectorScale:]
+ -[_M4FXTemporalScalingEffectV4 setMotionVectorScaleX:]
+ -[_M4FXTemporalScalingEffectV4 setMotionVectorScaleY:]
+ -[_M4FXTemporalScalingEffectV4 setOutputTexture:]
+ -[_M4FXTemporalScalingEffectV4 setPreExposure:]
+ -[_M4FXTemporalScalingEffectV4 setPreviousJitterOffset:]
+ -[_M4FXTemporalScalingEffectV4 setPreviousViewToClipMatrix:]
+ -[_M4FXTemporalScalingEffectV4 setPreviousWorldToViewMatrix:]
+ -[_M4FXTemporalScalingEffectV4 setReactiveMaskTexture:]
+ -[_M4FXTemporalScalingEffectV4 setReset:]
+ -[_M4FXTemporalScalingEffectV4 setReversedDepth:]
+ -[_MFXFrameInterpolatorEffect .cxx_destruct]
+ -[_MFXFrameInterpolatorEffect aspectRatio]
+ -[_MFXFrameInterpolatorEffect colorTextureFormat]
+ -[_MFXFrameInterpolatorEffect colorTextureUsage]
+ -[_MFXFrameInterpolatorEffect colorTexture]
+ -[_MFXFrameInterpolatorEffect compositedUITexture]
+ -[_MFXFrameInterpolatorEffect debugTexture]
+ -[_MFXFrameInterpolatorEffect deltaTime]
+ -[_MFXFrameInterpolatorEffect depthTextureFormat]
+ -[_MFXFrameInterpolatorEffect depthTextureUsage]
+ -[_MFXFrameInterpolatorEffect depthTexture]
+ -[_MFXFrameInterpolatorEffect encodeToCommandBuffer:]
+ -[_MFXFrameInterpolatorEffect encodeToCommandQueue:]
+ -[_MFXFrameInterpolatorEffect farPlane]
+ -[_MFXFrameInterpolatorEffect fence]
+ -[_MFXFrameInterpolatorEffect fieldOfView]
+ -[_MFXFrameInterpolatorEffect height]
+ -[_MFXFrameInterpolatorEffect initWithDevice:descriptor:]
+ -[_MFXFrameInterpolatorEffect inputHeight]
+ -[_MFXFrameInterpolatorEffect inputWidth]
+ -[_MFXFrameInterpolatorEffect isDepthReversed]
+ -[_MFXFrameInterpolatorEffect isUITextureComposited]
+ -[_MFXFrameInterpolatorEffect jitterOffsetX]
+ -[_MFXFrameInterpolatorEffect jitterOffsetY]
+ -[_MFXFrameInterpolatorEffect motionTextureFormat]
+ -[_MFXFrameInterpolatorEffect motionTextureUsage]
+ -[_MFXFrameInterpolatorEffect motionTexture]
+ -[_MFXFrameInterpolatorEffect motionVectorScaleX]
+ -[_MFXFrameInterpolatorEffect motionVectorScaleY]
+ -[_MFXFrameInterpolatorEffect nearPlane]
+ -[_MFXFrameInterpolatorEffect outputHeight]
+ -[_MFXFrameInterpolatorEffect outputTextureFormat]
+ -[_MFXFrameInterpolatorEffect outputTextureUsage]
+ -[_MFXFrameInterpolatorEffect outputTexture]
+ -[_MFXFrameInterpolatorEffect outputWidth]
+ -[_MFXFrameInterpolatorEffect prevColorTexture]
+ -[_MFXFrameInterpolatorEffect reset]
+ -[_MFXFrameInterpolatorEffect setAspectRatio:]
+ -[_MFXFrameInterpolatorEffect setColorTexture:]
+ -[_MFXFrameInterpolatorEffect setCompositedUITexture:]
+ -[_MFXFrameInterpolatorEffect setDebugTexture:]
+ -[_MFXFrameInterpolatorEffect setDeltaTime:]
+ -[_MFXFrameInterpolatorEffect setDepthReversed:]
+ -[_MFXFrameInterpolatorEffect setDepthTexture:]
+ -[_MFXFrameInterpolatorEffect setFarPlane:]
+ -[_MFXFrameInterpolatorEffect setFence:]
+ -[_MFXFrameInterpolatorEffect setFieldOfView:]
+ -[_MFXFrameInterpolatorEffect setHeight:]
+ -[_MFXFrameInterpolatorEffect setIsUITextureComposited:]
+ -[_MFXFrameInterpolatorEffect setJitterOffsetX:]
+ -[_MFXFrameInterpolatorEffect setJitterOffsetY:]
+ -[_MFXFrameInterpolatorEffect setMotionTexture:]
+ -[_MFXFrameInterpolatorEffect setMotionVectorScaleX:]
+ -[_MFXFrameInterpolatorEffect setMotionVectorScaleY:]
+ -[_MFXFrameInterpolatorEffect setNearPlane:]
+ -[_MFXFrameInterpolatorEffect setOutputTexture:]
+ -[_MFXFrameInterpolatorEffect setPrevColorTexture:]
+ -[_MFXFrameInterpolatorEffect setReset:]
+ -[_MFXFrameInterpolatorEffect setShouldResetHistory:]
+ -[_MFXFrameInterpolatorEffect setUITexture:]
+ -[_MFXFrameInterpolatorEffect setWidth:]
+ -[_MFXFrameInterpolatorEffect shouldResetHistory]
+ -[_MFXFrameInterpolatorEffect uiTextureFormat]
+ -[_MFXFrameInterpolatorEffect uiTextureUsage]
+ -[_MFXFrameInterpolatorEffect uiTexture]
+ -[_MFXFrameInterpolatorEffect width]
+ -[_MFXSpatialScalingEffectEFFECT_NAME_V1 initWithDevice:descriptor:].cold.1
+ -[_MFXTemporalDenoisingScalingEffect .cxx_construct]
+ -[_MFXTemporalDenoisingScalingEffect .cxx_destruct]
+ -[_MFXTemporalDenoisingScalingEffect colorTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect colorTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect colorTexture]
+ -[_MFXTemporalDenoisingScalingEffect dealloc]
+ -[_MFXTemporalDenoisingScalingEffect debugTexture]
+ -[_MFXTemporalDenoisingScalingEffect denoiseStrengthMaskTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect denoiseStrengthMaskTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect denoiseStrengthMaskTexture]
+ -[_MFXTemporalDenoisingScalingEffect depthTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect depthTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect depthTexture]
+ -[_MFXTemporalDenoisingScalingEffect diffuseAlbedoTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect diffuseAlbedoTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect diffuseAlbedoTexture]
+ -[_MFXTemporalDenoisingScalingEffect dilatedMotionVectors]
+ -[_MFXTemporalDenoisingScalingEffect encodeToCommandBuffer:]
+ -[_MFXTemporalDenoisingScalingEffect encodeToCommandQueue:]
+ -[_MFXTemporalDenoisingScalingEffect exposureTexture]
+ -[_MFXTemporalDenoisingScalingEffect fence]
+ -[_MFXTemporalDenoisingScalingEffect initWithDevice:descriptor:history:]
+ -[_MFXTemporalDenoisingScalingEffect initWithDevice:descriptor:history:].cold.1
+ -[_MFXTemporalDenoisingScalingEffect initWithDevice:descriptor:history:].cold.2
+ -[_MFXTemporalDenoisingScalingEffect inputContentHeight]
+ -[_MFXTemporalDenoisingScalingEffect inputContentMaxScale]
+ -[_MFXTemporalDenoisingScalingEffect inputContentMinScale]
+ -[_MFXTemporalDenoisingScalingEffect inputContentWidth]
+ -[_MFXTemporalDenoisingScalingEffect inputHeight]
+ -[_MFXTemporalDenoisingScalingEffect inputWidth]
+ -[_MFXTemporalDenoisingScalingEffect isDepthReversed]
+ -[_MFXTemporalDenoisingScalingEffect jitterOffsetX]
+ -[_MFXTemporalDenoisingScalingEffect jitterOffsetY]
+ -[_MFXTemporalDenoisingScalingEffect jitterOffset]
+ -[_MFXTemporalDenoisingScalingEffect motionTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect motionTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect motionTexture]
+ -[_MFXTemporalDenoisingScalingEffect motionVectorScaleX]
+ -[_MFXTemporalDenoisingScalingEffect motionVectorScaleY]
+ -[_MFXTemporalDenoisingScalingEffect motionVectorScale]
+ -[_MFXTemporalDenoisingScalingEffect normalTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect normalTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect normalTexture]
+ -[_MFXTemporalDenoisingScalingEffect outputHeight]
+ -[_MFXTemporalDenoisingScalingEffect outputTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect outputTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect outputTexture]
+ -[_MFXTemporalDenoisingScalingEffect outputWidth]
+ -[_MFXTemporalDenoisingScalingEffect preExposure]
+ -[_MFXTemporalDenoisingScalingEffect reactiveMaskTexture]
+ -[_MFXTemporalDenoisingScalingEffect reactiveTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect reset]
+ -[_MFXTemporalDenoisingScalingEffect reversedDepth]
+ -[_MFXTemporalDenoisingScalingEffect roughnessTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect roughnessTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect roughnessTexture]
+ -[_MFXTemporalDenoisingScalingEffect setColorTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setDebugTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setDenoiseStrengthMaskTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setDepthReversed:]
+ -[_MFXTemporalDenoisingScalingEffect setDepthTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setDiffuseAlbedoTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setExposureTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setFence:]
+ -[_MFXTemporalDenoisingScalingEffect setInputContentHeight:]
+ -[_MFXTemporalDenoisingScalingEffect setInputContentWidth:]
+ -[_MFXTemporalDenoisingScalingEffect setJitterOffset:]
+ -[_MFXTemporalDenoisingScalingEffect setJitterOffsetX:]
+ -[_MFXTemporalDenoisingScalingEffect setJitterOffsetY:]
+ -[_MFXTemporalDenoisingScalingEffect setMotionTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setMotionVectorScale:]
+ -[_MFXTemporalDenoisingScalingEffect setMotionVectorScaleX:]
+ -[_MFXTemporalDenoisingScalingEffect setMotionVectorScaleY:]
+ -[_MFXTemporalDenoisingScalingEffect setNormalTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setOutputTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setPreExposure:]
+ -[_MFXTemporalDenoisingScalingEffect setReactiveMaskTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setReset:]
+ -[_MFXTemporalDenoisingScalingEffect setReversedDepth:]
+ -[_MFXTemporalDenoisingScalingEffect setRoughnessTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setShouldResetHistory:]
+ -[_MFXTemporalDenoisingScalingEffect setSpecularAlbedoTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setSpecularHitDistanceTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setTransparencyOverlayTexture:]
+ -[_MFXTemporalDenoisingScalingEffect setViewToClipMatrix:]
+ -[_MFXTemporalDenoisingScalingEffect setWorldToViewMatrix:]
+ -[_MFXTemporalDenoisingScalingEffect shouldResetHistory]
+ -[_MFXTemporalDenoisingScalingEffect specularAlbedoTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect specularAlbedoTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect specularAlbedoTexture]
+ -[_MFXTemporalDenoisingScalingEffect specularHitDistanceTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect specularHitDistanceTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect specularHitDistanceTexture]
+ -[_MFXTemporalDenoisingScalingEffect transparencyOverlayTextureFormat]
+ -[_MFXTemporalDenoisingScalingEffect transparencyOverlayTextureUsage]
+ -[_MFXTemporalDenoisingScalingEffect transparencyOverlayTexture]
+ -[_MFXTemporalDenoisingScalingEffect viewToClipMatrix]
+ -[_MFXTemporalDenoisingScalingEffect worldToViewMatrix]
+ -[_MFXTemporalScalingEffectV3 dilatedMotionVectors]
+ -[_MFXTemporalScalingEffectV3 initWithDevice:descriptor:history:].cold.2
+ -[_MFXTemporalScalingEffectV3 initWithDevice:descriptor:history:].cold.3
+ -[_MFXTemporalScalingEffectV3 reactiveMaskTextureFormat]
+ -[_MFXTemporalScalingEffectV4 .cxx_construct]
+ -[_MFXTemporalScalingEffectV4 .cxx_destruct]
+ -[_MFXTemporalScalingEffectV4 colorTextureFormat]
+ -[_MFXTemporalScalingEffectV4 colorTextureUsage]
+ -[_MFXTemporalScalingEffectV4 colorTexture]
+ -[_MFXTemporalScalingEffectV4 currentViewToClipMatrix]
+ -[_MFXTemporalScalingEffectV4 currentWorldToViewMatrix]
+ -[_MFXTemporalScalingEffectV4 dealloc]
+ -[_MFXTemporalScalingEffectV4 debugTexture]
+ -[_MFXTemporalScalingEffectV4 depthTextureFormat]
+ -[_MFXTemporalScalingEffectV4 depthTextureUsage]
+ -[_MFXTemporalScalingEffectV4 depthTexture]
+ -[_MFXTemporalScalingEffectV4 dilatedMotionVectors]
+ -[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]
+ -[_MFXTemporalScalingEffectV4 encodeToCommandQueue:]
+ -[_MFXTemporalScalingEffectV4 executionMode]
+ -[_MFXTemporalScalingEffectV4 exposureTexture]
+ -[_MFXTemporalScalingEffectV4 fence]
+ -[_MFXTemporalScalingEffectV4 initWithDevice:descriptor:history:]
+ -[_MFXTemporalScalingEffectV4 initWithDevice:descriptor:history:].cold.1
+ -[_MFXTemporalScalingEffectV4 initWithDevice:descriptor:history:].cold.2
+ -[_MFXTemporalScalingEffectV4 initWithDevice:descriptor:history:].cold.3
+ -[_MFXTemporalScalingEffectV4 inputContentHeight]
+ -[_MFXTemporalScalingEffectV4 inputContentMaxScale]
+ -[_MFXTemporalScalingEffectV4 inputContentMinScale]
+ -[_MFXTemporalScalingEffectV4 inputContentWidth]
+ -[_MFXTemporalScalingEffectV4 inputHeight]
+ -[_MFXTemporalScalingEffectV4 inputWidth]
+ -[_MFXTemporalScalingEffectV4 isDepthReversed]
+ -[_MFXTemporalScalingEffectV4 jitterOffsetX]
+ -[_MFXTemporalScalingEffectV4 jitterOffsetY]
+ -[_MFXTemporalScalingEffectV4 jitterOffset]
+ -[_MFXTemporalScalingEffectV4 motionTextureFormat]
+ -[_MFXTemporalScalingEffectV4 motionTextureUsage]
+ -[_MFXTemporalScalingEffectV4 motionTexture]
+ -[_MFXTemporalScalingEffectV4 motionVectorScaleX]
+ -[_MFXTemporalScalingEffectV4 motionVectorScaleY]
+ -[_MFXTemporalScalingEffectV4 motionVectorScale]
+ -[_MFXTemporalScalingEffectV4 outputHeight]
+ -[_MFXTemporalScalingEffectV4 outputTextureFormat]
+ -[_MFXTemporalScalingEffectV4 outputTextureUsage]
+ -[_MFXTemporalScalingEffectV4 outputTexture]
+ -[_MFXTemporalScalingEffectV4 outputWidth]
+ -[_MFXTemporalScalingEffectV4 preExposure]
+ -[_MFXTemporalScalingEffectV4 previousJitterOffset]
+ -[_MFXTemporalScalingEffectV4 previousViewToClipMatrix]
+ -[_MFXTemporalScalingEffectV4 previousWorldToViewMatrix]
+ -[_MFXTemporalScalingEffectV4 reactiveMaskTextureFormat]
+ -[_MFXTemporalScalingEffectV4 reactiveMaskTexture]
+ -[_MFXTemporalScalingEffectV4 reactiveTextureUsage]
+ -[_MFXTemporalScalingEffectV4 reset]
+ -[_MFXTemporalScalingEffectV4 reversedDepth]
+ -[_MFXTemporalScalingEffectV4 setColorTexture:]
+ -[_MFXTemporalScalingEffectV4 setCurrentViewToClipMatrix:]
+ -[_MFXTemporalScalingEffectV4 setCurrentWorldToViewMatrix:]
+ -[_MFXTemporalScalingEffectV4 setDebugTexture:]
+ -[_MFXTemporalScalingEffectV4 setDepthReversed:]
+ -[_MFXTemporalScalingEffectV4 setDepthTexture:]
+ -[_MFXTemporalScalingEffectV4 setExposureTexture:]
+ -[_MFXTemporalScalingEffectV4 setFence:]
+ -[_MFXTemporalScalingEffectV4 setInputContentHeight:]
+ -[_MFXTemporalScalingEffectV4 setInputContentWidth:]
+ -[_MFXTemporalScalingEffectV4 setJitterOffset:]
+ -[_MFXTemporalScalingEffectV4 setJitterOffsetX:]
+ -[_MFXTemporalScalingEffectV4 setJitterOffsetY:]
+ -[_MFXTemporalScalingEffectV4 setMotionTexture:]
+ -[_MFXTemporalScalingEffectV4 setMotionVectorScale:]
+ -[_MFXTemporalScalingEffectV4 setMotionVectorScaleX:]
+ -[_MFXTemporalScalingEffectV4 setMotionVectorScaleY:]
+ -[_MFXTemporalScalingEffectV4 setOutputTexture:]
+ -[_MFXTemporalScalingEffectV4 setPreExposure:]
+ -[_MFXTemporalScalingEffectV4 setPreviousJitterOffset:]
+ -[_MFXTemporalScalingEffectV4 setPreviousViewToClipMatrix:]
+ -[_MFXTemporalScalingEffectV4 setPreviousWorldToViewMatrix:]
+ -[_MFXTemporalScalingEffectV4 setReactiveMaskTexture:]
+ -[_MFXTemporalScalingEffectV4 setReset:]
+ -[_MFXTemporalScalingEffectV4 setReversedDepth:]
+ -[_MTL4FXEffect .cxx_destruct]
+ -[_MTL4FXEffect _beginEncodeWithCommandBuffer:]
+ -[_MTL4FXEffect _didCreateComputeCommandEncoder:forEncode:]
+ -[_MTL4FXEffect _didCreateRenderCommandEncoder:forEncode:]
+ -[_MTL4FXEffect init]
+ -[_MTL4FXEffect setTracingDelegate:]
+ -[_MTL4FXEffect tracingDelegate]
+ -[_MTL4FXFrameInterpolator _emitTelemetry:forDevice:]
+ -[_MTL4FXSpatialScaler _emitTelemetry:forDevice:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 .cxx_destruct]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorProcessingMode]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorTextureBarrierStages]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorTextureFormat]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorTextureUsage]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorTexture]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 debugTexture]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 encodeToCommandBuffer:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 fence]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 initWithDevice:compiler:descriptor:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 inputContentHeight]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 inputContentWidth]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 inputHeight]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 inputWidth]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputHeight]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputTextureBarrierStages]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputTextureFormat]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputTextureUsage]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputTexture]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputWidth]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setColorTexture:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setColorTextureBarrierStages:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setDebugTexture:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setFence:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setInputContentHeight:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setInputContentWidth:]
+ -[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setOutputTexture:]
+ -[_MTL4FXTemporalDenoisedScaler _emitTelemetry:forDevice:]
+ -[_MTL4FXTemporalScaler _emitTelemetry:forDevice:compiler:]
+ -[_MTLFXEffectBase .cxx_destruct]
+ -[_MTLFXEffectBase _beginEncode]
+ -[_MTLFXEffectBase effectID]
+ -[_MTLFXEffectBase init]
+ -[_MTLFXEffectBase init].cold.1
+ -[_MTLFXFrameInterpolator _emitTelemetry:forDevice:]
+ -[_MTLFXTemporalDenoisedScaler _emitTelemetry:forDevice:]
+ GCC_except_table10
+ GCC_except_table105
+ GCC_except_table11
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table12
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table13
+ GCC_except_table14
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table29
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table79
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table92
+ GCC_except_table94
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._asyncQueue
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._autoExposureEnabled
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._brnet_desc
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._colorTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._colorTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._colorTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._commandQueue
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfNetArg
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfNetPSO
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfnet_desc
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfnet_input_TensorData
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfnet_input_TensorData_Buffer
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfnet_net_wrapper
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfnet_output_TensorData
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfnet_output_TensorData_Buffer
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._denoiseFilter
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._denoiseStrengthMaskTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._denoiseStrengthMaskTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._denoiserColorTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._depthTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._depthTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._depthTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._device
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._diffuseAlbedoTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._diffuseAlbedoTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._diffuseAlbedoTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dummyFence
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._enableLateLatch
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._exposureTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._fence
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._filter
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._framePowerOnSharedEvent
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._frameSharedEvent
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._history
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._inputContentHeight
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._inputContentMaxScale
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._inputContentMinScale
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._inputContentWidth
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._inputEvent
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._inputEventValue
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._inputHeight
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._inputWidth
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._input_TensorData
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._input_TensorData_Buffer
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._jitterOffset
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._midBicubicWarp
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._midProcessingDoneEvent
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._midProcessingStartEvent
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._motionTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._motionTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._motionTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._motionVectorScale
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._netArg
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._netPSO
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._net_wrapper
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._normalTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._normalTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._normalTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._outputEvent
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._outputEventValue
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._outputHeight
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._outputTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._outputTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._outputWidth
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._output_TensorData
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._output_TensorData_Buffer
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._preExposure
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._preUpscaleComposeTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._preUpscaleComposeTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._prevReactiveTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._previousJitterOffset
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._reactiveMaskEnabled
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._reactiveMaskTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._reactiveTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._reactiveTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._reset
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._reversedDepth
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._roughnessTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._roughnessTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._roughnessTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._specularAlbedoTexture
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._specularAlbedoTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._specularAlbedoTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._specularHitDistance
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._specularHitDistanceTextureFormat
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._specularHitDistanceTextureUsage
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._useANE
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._viewToClipMatrix
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._worldToViewMatrix
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._asyncQueue
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._autoExposureEnabled
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._brnet_desc
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._colorTexture
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._colorTextureBarrierStages
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._colorTextureFormat
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._colorTextureUsage
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._commandQueue
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._currentViewToClipMatrix
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._currentWorldToViewMatrix
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._depthTexture
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._depthTextureFormat
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._depthTextureUsage
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._device
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._dummyFence
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._enableLateLatch
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._exposureTexture
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._fence
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._filter
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._framePowerOnSharedEvent
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._frameSharedEvent
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._history
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._inputContentHeight
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._inputContentMaxScale
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._inputContentMinScale
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._inputContentWidth
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._inputEvent
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._inputEventValue
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._inputHeight
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._inputWidth
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._input_TensorData
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._jitterOffset
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._midBicubicWarp
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._midProcessingDoneEvent
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._midProcessingStartEvent
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._mlHeap
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._mlProcessingArgs
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._mlProcessingPSO
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._motionTexture
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._motionTextureFormat
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._motionTextureUsage
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._motionVectorScale
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._net_wrapper
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._outputEvent
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._outputEventValue
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._outputHeight
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._outputTexture
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._outputTextureBarrierStages
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._outputTextureUsage
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._outputWidth
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._output_TensorData
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._preExposure
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._prevReactiveTexture
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._previousJitterOffset
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._previousViewToClipMatrix
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._previousWorldToViewMatrix
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._prewarmComplete
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._reactiveMaskEnabled
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._reactiveMaskTextureFormat
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._reactiveTexture
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._reactiveTextureUsage
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._reset
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._reversedDepth
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._useANE
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._waitForCompletion
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._asyncQueue
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._autoExposureEnabled
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._brnet_desc
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._colorTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._colorTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._colorTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._commandQueue
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._dbfnet_desc
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._dbfnet_input_TensorData
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._dbfnet_net_wrapper
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._dbfnet_output_TensorData
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._denoiseFilter
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._denoiseStrengthMaskTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._denoiseStrengthMaskTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._denoiserColorTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._depthTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._depthTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._depthTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._device
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._diffuseAlbedoTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._diffuseAlbedoTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._diffuseAlbedoTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._dummyFence
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._enableLateLatch
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._exposureTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._fence
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._filter
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._framePowerOnSharedEvent
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._frameSharedEvent
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._history
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._inputContentHeight
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._inputContentMaxScale
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._inputContentMinScale
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._inputContentWidth
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._inputEvent
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._inputEventValue
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._inputHeight
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._inputWidth
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._input_TensorData
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._jitterOffset
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._midBicubicWarp
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._midProcessingDoneEvent
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._midProcessingStartEvent
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._motionTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._motionTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._motionTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._motionVectorScale
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._net_wrapper
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._normalTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._normalTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._normalTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._outputEvent
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._outputEventValue
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._outputHeight
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._outputTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._outputTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._outputWidth
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._output_TensorData
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._preExposure
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._preUpscaleComposeTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._preUpscaleComposeTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._prevReactiveTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._previousJitterOffset
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._reactiveMaskEnabled
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._reactiveMaskTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._reactiveTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._reactiveTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._reset
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._reversedDepth
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._roughnessTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._roughnessTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._roughnessTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._specularAlbedoTexture
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._specularAlbedoTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._specularAlbedoTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._specularHitDistEnabled
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._specularHitDistance
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._specularHitDistanceTextureFormat
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._specularHitDistanceTextureUsage
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._useANE
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._viewToClipMatrix
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._worldToViewMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._brnet_desc
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._dummyFence
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._waitForPreviousEncode
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._asyncQueue
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._autoExposureEnabled
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._brnet_desc
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._colorTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._colorTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._colorTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._commandQueue
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._currentViewToClipMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._currentWorldToViewMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._depthTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._depthTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._depthTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._device
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._dummyFence
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._enableLateLatch
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._exposureTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._fence
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._filter
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._framePowerOnSharedEvent
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._frameSharedEvent
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._history
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._inputContentHeight
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._inputContentMaxScale
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._inputContentMinScale
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._inputContentWidth
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._inputEvent
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._inputEventValue
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._inputHeight
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._inputWidth
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._input_TensorData
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._jitterOffset
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._midBicubicWarp
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._midProcessingDoneEvent
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._midProcessingStartEvent
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._motionTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._motionTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._motionTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._motionVectorScale
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._net_wrapper
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._outputEvent
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._outputEventValue
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._outputHeight
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._outputTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._outputTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._outputWidth
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._output_TensorData
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._preExposure
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._prevReactiveTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._previousJitterOffset
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._previousViewToClipMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._previousWorldToViewMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._prewarmComplete
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._reactiveMaskEnabled
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._reactiveMaskTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._reactiveTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._reactiveTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._reset
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._reversedDepth
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._useANE
+ OBJC_IVAR_$__MFXTemporalScalingEffectV4._waitForCompletion
+ OBJC_IVAR_$__MTL4FXEffect._tracingDelegate
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._colorProcessingMode
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._colorTextureBarrierStages
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._colorTextureUsage
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._debugTexture
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._device
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._fence
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._inputContentHeight
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._inputContentWidth
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._inputFormat
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._inputSRGB
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._inputTexture
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._intermediatePixelFormat
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._mfxNormPerceptPSO
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._mfxNormPerceptTex
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._mfxPassDescriptor
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._mfxSharpenPSO
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._mfxUpscalePSO
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._mfxUpscaledTex
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._outputFormat
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._outputSRGB
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._outputTexture
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._outputTextureBarrierStages
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._outputTextureUsage
+ OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._texDesc
+ OBJC_IVAR_$__MTLFXEffectBase._dumpTensors
+ OBJC_IVAR_$__MTLFXEffectBase._dumpTensorsDir
+ OBJC_IVAR_$__MTLFXEffectBase._effectID
+ OBJC_IVAR_$__MTLFXEffectBase._encodeID
+ OBJC_IVAR_$__MTLFXEffectBase._useRefTensors
+ _MPSGetDataTypeName
+ _OBJC_CLASS_$_MFXTemporalDenoisingScalingEffectDescriptor
+ _OBJC_CLASS_$_MPSCommandBuffer
+ _OBJC_CLASS_$_MPSGraphPooling4DOpDescriptor
+ _OBJC_CLASS_$_MTL4ArgumentTableDescriptor
+ _OBJC_CLASS_$_MTL4ComputePipelineDescriptor
+ _OBJC_CLASS_$_MTL4LibraryFunctionDescriptor
+ _OBJC_CLASS_$_MTL4MachineLearningPipelineDescriptor
+ _OBJC_CLASS_$_MTL4RenderPassDescriptor
+ _OBJC_CLASS_$_MTL4RenderPipelineDescriptor
+ _OBJC_CLASS_$_MTL4SpecializedFunctionDescriptor
+ _OBJC_CLASS_$_MTL4TileRenderPipelineDescriptor
+ _OBJC_CLASS_$_MTLFXFrameInterpolatorDescriptor
+ _OBJC_CLASS_$_MTLFXTemporalDenoisedScalerDescriptor
+ _OBJC_CLASS_$_MTLHeapDescriptor
+ _OBJC_CLASS_$_MTLResidencySetDescriptor
+ _OBJC_CLASS_$_MTLTensorDescriptor
+ _OBJC_CLASS_$_MTLTensorExtents
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$__M4FXFrameInterpolatorEffect
+ _OBJC_CLASS_$__M4FXTemporalDenoisingScalingEffect
+ _OBJC_CLASS_$__M4FXTemporalScalingEffectV4
+ _OBJC_CLASS_$__MFXFrameInterpolatorEffect
+ _OBJC_CLASS_$__MFXTemporalDenoisingScalingEffect
+ _OBJC_CLASS_$__MFXTemporalScalingEffectV4
+ _OBJC_CLASS_$__MTL4FXEffect
+ _OBJC_CLASS_$__MTL4FXFrameInterpolator
+ _OBJC_CLASS_$__MTL4FXSpatialScaler
+ _OBJC_CLASS_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1
+ _OBJC_CLASS_$__MTL4FXTemporalDenoisedScaler
+ _OBJC_CLASS_$__MTL4FXTemporalScaler
+ _OBJC_CLASS_$__MTLFXEffectBase
+ _OBJC_CLASS_$__MTLFXFrameInterpolator
+ _OBJC_CLASS_$__MTLFXTemporalDenoisedScaler
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor._denoiserScaler
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor._denoiserScaler4
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor._scaler
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor._scaler4
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor._uiTextureFormat
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor._version
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.colorTextureFormat
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.depthInverted
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.depthTextureFormat
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.height
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.inputHeight
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.inputWidth
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.maskTextureFormat
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.motionTextureFormat
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.outputHeight
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.outputTextureFormat
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.outputWidth
+ _OBJC_IVAR_$_MTLFXFrameInterpolatorDescriptor.width
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._denoiseStrengthMaskTextureEnabled
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._denoiseStrengthMaskTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._diffuseAlbedoTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._normalTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._outputTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._reactiveMaskTextureEnabled
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._reactiveMaskTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._roughnessTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._specularAlbedoTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._specularHitDistanceTextureEnabled
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._specularHitDistanceTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._transparencyOverlayTextureEnabled
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor._transparencyOverlayTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.autoExposureEnabled
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.colorTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.depthTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.inputContentMaxScale
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.inputContentMinScale
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.inputContentPropertiesEnabled
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.inputHeight
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.inputWidth
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.motionTextureFormat
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.outputHeight
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.outputWidth
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.requiresSynchronousInitialization
+ _OBJC_IVAR_$_MTLFXTemporalDenoisedScalerDescriptor.version
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._aspectRatio
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._colorTexture
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._colorTextureBarrierStages
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._colorTextureFormat
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._colorTextureUsage
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._debugTexture
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._deltaTime
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._denoiserScaler
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._depthTexture
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._depthTextureFormat
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._depthTextureUsage
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._farPlane
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._fence
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._fieldOfView
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._impl
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._inputHeight
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._inputWidth
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._jitterOffsetX
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._jitterOffsetY
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._motionTexture
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._motionTextureFormat
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._motionTextureUsage
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._motionVectorScaleX
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._motionVectorScaleY
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._nearPlane
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._outputHeight
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._outputTexture
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._outputTextureBarrierStages
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._outputTextureFormat
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._outputTextureUsage
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._outputWidth
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._prevColorTexture
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._reset
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._reversedDepth
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._temporalScaler
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._uiTexture
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._uiTextureComposited
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._uiTextureFormat
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._uiTextureUsage
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect.m_pDevice
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._colorTextureBarrierStages
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfNetHeap
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._debugTexture
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._denoiseStrengthMaskTexture
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._hudProperties
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._internalFence
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._netHeap
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._outputTextureBarrierStages
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._outputTextureFormat
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._preUpscaleComposeTexture
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._reactiveMaskTexture
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._specularHitDistanceTexture
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._timingRecord
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect.frameIndex
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect.globalResidency
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4._debugTexture
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4._hudProperties
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4._input_TensorData_Buffer
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4._outputTextureFormat
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4._output_TensorData_Buffer
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4._reactiveMaskTexture
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4.frameIndex
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4.internalFence
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4.internalMLFence
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectV4.residencyGlobal
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._aspectRatio
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._colorTexture
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._colorTextureFormat
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._colorTextureUsage
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._debugTexture
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._deltaTime
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._depthTexture
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._depthTextureFormat
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._depthTextureUsage
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._farPlane
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._fence
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._fieldOfView
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._height
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._inputHeight
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._inputWidth
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._jitterOffsetX
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._jitterOffsetY
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._motionTexture
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._motionTextureFormat
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._motionTextureUsage
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._motionVectorScaleX
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._motionVectorScaleY
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._nearPlane
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._outputHeight
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._outputTexture
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._outputTextureFormat
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._outputTextureUsage
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._outputWidth
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._prevColorTexture
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._reset
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._reversedDepth
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._uiTexture
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._uiTextureComposited
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._uiTextureFormat
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._uiTextureUsage
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._width
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._debugTexture
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._denoiseStrengthMaskTexture
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._hudProperties
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._outputTextureFormat
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._preUpscaleComposeTexture
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._prevViewProjectionMatrix
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._reactiveMaskTexture
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._specularHitDistanceTexture
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._timingRecord
+ _OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect.frameIndex
+ _OBJC_IVAR_$__MFXTemporalScalingEffectV4._debugTexture
+ _OBJC_IVAR_$__MFXTemporalScalingEffectV4._outputTextureFormat
+ _OBJC_IVAR_$__MFXTemporalScalingEffectV4._reactiveMaskTexture
+ _OBJC_IVAR_$__MFXTemporalScalingEffectV4._timingRecord
+ _OBJC_IVAR_$__MFXTemporalScalingEffectV4.frameIndex
+ _OBJC_IVAR_$__MTL4FXEffect._maxFramesInFlightSemaphore
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._colorTextureFormat
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._frame
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._framesInFlight
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._fxrSharpenBuffer
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._fxrUpscaleBuffer
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._inputHeight
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._inputWidth
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._internalFence
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._needNormPercept
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._normPerceptFragInputs
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._normalizeBuffer
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._outputHeight
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._outputTextureFormat
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._outputWidth
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._residencySetGlobal
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._residencySetPercept
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._scaleBuffer
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._scaleFragInputs
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._sharpenBuffer
+ _OBJC_IVAR_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1._sharpenFragInputs
+ _OBJC_METACLASS_$_MFXTemporalDenoisingScalingEffectDescriptor
+ _OBJC_METACLASS_$_MTLFXFrameInterpolatorDescriptor
+ _OBJC_METACLASS_$_MTLFXTemporalDenoisedScalerDescriptor
+ _OBJC_METACLASS_$__M4FXFrameInterpolatorEffect
+ _OBJC_METACLASS_$__M4FXTemporalDenoisingScalingEffect
+ _OBJC_METACLASS_$__M4FXTemporalScalingEffectV4
+ _OBJC_METACLASS_$__MFXFrameInterpolatorEffect
+ _OBJC_METACLASS_$__MFXTemporalDenoisingScalingEffect
+ _OBJC_METACLASS_$__MFXTemporalScalingEffectV4
+ _OBJC_METACLASS_$__MTL4FXEffect
+ _OBJC_METACLASS_$__MTL4FXFrameInterpolator
+ _OBJC_METACLASS_$__MTL4FXSpatialScaler
+ _OBJC_METACLASS_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1
+ _OBJC_METACLASS_$__MTL4FXTemporalDenoisedScaler
+ _OBJC_METACLASS_$__MTL4FXTemporalScaler
+ _OBJC_METACLASS_$__MTLFXEffectBase
+ _OBJC_METACLASS_$__MTLFXFrameInterpolator
+ _OBJC_METACLASS_$__MTLFXTemporalDenoisedScaler
+ __OBJC_$_CLASS_METHODS_MTLFXFrameInterpolatorDescriptor
+ __OBJC_$_CLASS_METHODS_MTLFXTemporalDenoisedScalerDescriptor
+ __OBJC_$_INSTANCE_METHODS_MFXTemporalDenoisingScalingEffectDescriptor
+ __OBJC_$_INSTANCE_METHODS_MTLFXFrameInterpolatorDescriptor
+ __OBJC_$_INSTANCE_METHODS_MTLFXTemporalDenoisedScalerDescriptor
+ __OBJC_$_INSTANCE_METHODS__M4FXFrameInterpolatorEffect
+ __OBJC_$_INSTANCE_METHODS__M4FXTemporalDenoisingScalingEffect
+ __OBJC_$_INSTANCE_METHODS__M4FXTemporalScalingEffectV4
+ __OBJC_$_INSTANCE_METHODS__MFXFrameInterpolatorEffect
+ __OBJC_$_INSTANCE_METHODS__MFXTemporalDenoisingScalingEffect
+ __OBJC_$_INSTANCE_METHODS__MFXTemporalScalingEffectV4
+ __OBJC_$_INSTANCE_METHODS__MTL4FXEffect
+ __OBJC_$_INSTANCE_METHODS__MTL4FXFrameInterpolator
+ __OBJC_$_INSTANCE_METHODS__MTL4FXSpatialScaler
+ __OBJC_$_INSTANCE_METHODS__MTL4FXSpatialScalingEffectEFFECT_NAME_V1
+ __OBJC_$_INSTANCE_METHODS__MTL4FXTemporalDenoisedScaler
+ __OBJC_$_INSTANCE_METHODS__MTL4FXTemporalScaler
+ __OBJC_$_INSTANCE_METHODS__MTLFXEffectBase
+ __OBJC_$_INSTANCE_METHODS__MTLFXFrameInterpolator
+ __OBJC_$_INSTANCE_METHODS__MTLFXTemporalDenoisedScaler
+ __OBJC_$_INSTANCE_VARIABLES_MTLFXFrameInterpolatorDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MTLFXTemporalDenoisedScalerDescriptor
+ __OBJC_$_INSTANCE_VARIABLES__M4FXFrameInterpolatorEffect
+ __OBJC_$_INSTANCE_VARIABLES__M4FXTemporalDenoisingScalingEffect
+ __OBJC_$_INSTANCE_VARIABLES__M4FXTemporalScalingEffectV4
+ __OBJC_$_INSTANCE_VARIABLES__MFXFrameInterpolatorEffect
+ __OBJC_$_INSTANCE_VARIABLES__MFXTemporalDenoisingScalingEffect
+ __OBJC_$_INSTANCE_VARIABLES__MFXTemporalScalingEffectV4
+ __OBJC_$_INSTANCE_VARIABLES__MTL4FXEffect
+ __OBJC_$_INSTANCE_VARIABLES__MTL4FXSpatialScalingEffectEFFECT_NAME_V1
+ __OBJC_$_INSTANCE_VARIABLES__MTLFXEffectBase
+ __OBJC_$_PROP_LIST_MTL4FXFrameInterpolatorSPI
+ __OBJC_$_PROP_LIST_MTL4FXSpatialScalerSPI
+ __OBJC_$_PROP_LIST_MTL4FXTemporalDenoisedScalerSPI
+ __OBJC_$_PROP_LIST_MTL4FXTemporalScalerSPI
+ __OBJC_$_PROP_LIST_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROP_LIST_MTLFXFrameInterpolatorDescriptor
+ __OBJC_$_PROP_LIST_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROP_LIST_MTLFXSpatialScalerBase
+ __OBJC_$_PROP_LIST_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROP_LIST_MTLFXTemporalDenoisedScalerDescriptor
+ __OBJC_$_PROP_LIST_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROP_LIST_MTLFXTemporalScalerBase
+ __OBJC_$_PROP_LIST__M4FXFrameInterpolatorEffect
+ __OBJC_$_PROP_LIST__M4FXTemporalDenoisingScalingEffect
+ __OBJC_$_PROP_LIST__M4FXTemporalScalingEffectV4
+ __OBJC_$_PROP_LIST__MFXFrameInterpolatorEffect
+ __OBJC_$_PROP_LIST__MFXTemporalDenoisingScalingEffect
+ __OBJC_$_PROP_LIST__MFXTemporalScalingEffectV4
+ __OBJC_$_PROP_LIST__MTL4FXEffect
+ __OBJC_$_PROP_LIST__MTL4FXSpatialScalingEffectEFFECT_NAME_V1
+ __OBJC_$_PROP_LIST__MTLFXEffectBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXFrameInterpolator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXSpatialScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXSpatialScalerSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalScalerSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXSpatialScalerBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalScalerBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXFrameInterpolator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXSpatialScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXSpatialScalerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalScalerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXSpatialScalerBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalScalerBase
+ __OBJC_$_PROTOCOL_REFS_MTL4FXFrameInterpolator
+ __OBJC_$_PROTOCOL_REFS_MTL4FXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4FXSpatialScaler
+ __OBJC_$_PROTOCOL_REFS_MTL4FXSpatialScalerSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalScaler
+ __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalScalerSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFXSpatialScalerBase
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalScalerBase
+ __OBJC_CLASS_PROTOCOLS_$_MTLFXFrameInterpolatorDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_MTLFXTemporalDenoisedScalerDescriptor
+ __OBJC_CLASS_PROTOCOLS_$__M4FXFrameInterpolatorEffect
+ __OBJC_CLASS_PROTOCOLS_$__M4FXTemporalDenoisingScalingEffect
+ __OBJC_CLASS_PROTOCOLS_$__M4FXTemporalScalingEffectV4
+ __OBJC_CLASS_PROTOCOLS_$__MFXFrameInterpolatorEffect
+ __OBJC_CLASS_PROTOCOLS_$__MFXTemporalDenoisingScalingEffect
+ __OBJC_CLASS_PROTOCOLS_$__MFXTemporalScalingEffectV4
+ __OBJC_CLASS_PROTOCOLS_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1
+ __OBJC_CLASS_RO_$_MFXTemporalDenoisingScalingEffectDescriptor
+ __OBJC_CLASS_RO_$_MTLFXFrameInterpolatorDescriptor
+ __OBJC_CLASS_RO_$_MTLFXTemporalDenoisedScalerDescriptor
+ __OBJC_CLASS_RO_$__M4FXFrameInterpolatorEffect
+ __OBJC_CLASS_RO_$__M4FXTemporalDenoisingScalingEffect
+ __OBJC_CLASS_RO_$__M4FXTemporalScalingEffectV4
+ __OBJC_CLASS_RO_$__MFXFrameInterpolatorEffect
+ __OBJC_CLASS_RO_$__MFXTemporalDenoisingScalingEffect
+ __OBJC_CLASS_RO_$__MFXTemporalScalingEffectV4
+ __OBJC_CLASS_RO_$__MTL4FXEffect
+ __OBJC_CLASS_RO_$__MTL4FXFrameInterpolator
+ __OBJC_CLASS_RO_$__MTL4FXSpatialScaler
+ __OBJC_CLASS_RO_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1
+ __OBJC_CLASS_RO_$__MTL4FXTemporalDenoisedScaler
+ __OBJC_CLASS_RO_$__MTL4FXTemporalScaler
+ __OBJC_CLASS_RO_$__MTLFXEffectBase
+ __OBJC_CLASS_RO_$__MTLFXFrameInterpolator
+ __OBJC_CLASS_RO_$__MTLFXTemporalDenoisedScaler
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXFrameInterpolator
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXFrameInterpolatorSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXSpatialScaler
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXSpatialScalerSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalDenoisedScaler
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalDenoisedScalerSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalScaler
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalScalerSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolator
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolatorBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolatorSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLFXSpatialScalerBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScaler
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScalerBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalScalerBase
+ __OBJC_METACLASS_RO_$_MFXTemporalDenoisingScalingEffectDescriptor
+ __OBJC_METACLASS_RO_$_MTLFXFrameInterpolatorDescriptor
+ __OBJC_METACLASS_RO_$_MTLFXTemporalDenoisedScalerDescriptor
+ __OBJC_METACLASS_RO_$__M4FXFrameInterpolatorEffect
+ __OBJC_METACLASS_RO_$__M4FXTemporalDenoisingScalingEffect
+ __OBJC_METACLASS_RO_$__M4FXTemporalScalingEffectV4
+ __OBJC_METACLASS_RO_$__MFXFrameInterpolatorEffect
+ __OBJC_METACLASS_RO_$__MFXTemporalDenoisingScalingEffect
+ __OBJC_METACLASS_RO_$__MFXTemporalScalingEffectV4
+ __OBJC_METACLASS_RO_$__MTL4FXEffect
+ __OBJC_METACLASS_RO_$__MTL4FXFrameInterpolator
+ __OBJC_METACLASS_RO_$__MTL4FXSpatialScaler
+ __OBJC_METACLASS_RO_$__MTL4FXSpatialScalingEffectEFFECT_NAME_V1
+ __OBJC_METACLASS_RO_$__MTL4FXTemporalDenoisedScaler
+ __OBJC_METACLASS_RO_$__MTL4FXTemporalScaler
+ __OBJC_METACLASS_RO_$__MTLFXEffectBase
+ __OBJC_METACLASS_RO_$__MTLFXFrameInterpolator
+ __OBJC_METACLASS_RO_$__MTLFXTemporalDenoisedScaler
+ __OBJC_PROTOCOL_$_MTL4FXFrameInterpolator
+ __OBJC_PROTOCOL_$_MTL4FXFrameInterpolatorSPI
+ __OBJC_PROTOCOL_$_MTL4FXSpatialScaler
+ __OBJC_PROTOCOL_$_MTL4FXSpatialScalerSPI
+ __OBJC_PROTOCOL_$_MTL4FXTemporalDenoisedScaler
+ __OBJC_PROTOCOL_$_MTL4FXTemporalDenoisedScalerSPI
+ __OBJC_PROTOCOL_$_MTL4FXTemporalScaler
+ __OBJC_PROTOCOL_$_MTL4FXTemporalScalerSPI
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolator
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolatorBase
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolatorSPI
+ __OBJC_PROTOCOL_$_MTLFXSpatialScalerBase
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScaler
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScalerBase
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_PROTOCOL_$_MTLFXTemporalScalerBase
+ __OBJC_PROTOCOL_REFERENCE_$_MTL4FXTemporalDenoisedScaler
+ __OBJC_PROTOCOL_REFERENCE_$_MTL4FXTemporalScalerSPI
+ __OBJC_PROTOCOL_REFERENCE_$_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_PROTOCOL_REFERENCE_$_MTLFXTemporalScalerSPI
+ __Z12checkTexturePU21objcproto10MTLTexture11objc_objectmmP8NSStringbb14MTLPixelFormat
+ __Z14mlKernelMetal4PU19objcproto9MTLDevice11objc_objectP8NSStringP8NSBundlebPU23objcproto12MTL4Compiler11objc_objectP16MTLTensorExtents
+ __Z19computeKernelMetal4PU21objcproto10MTLLibrary11objc_objectPU23objcproto12MTL4Compiler11objc_objectP8NSStringPU15__autoreleasingP7NSErrorP25MTLFunctionConstantValuesmb
+ __Z20makeTensorFromBufferPU19objcproto9MTLDevice11objc_objectiiiPiPU26objcproto15MTLResidencySet11objc_objectb29MPSGraphTensorNamedDataLayout
+ __Z21createMetalBufferRandIDhEPU19objcproto9MTLBuffer11objc_objectPU19objcproto9MTLDevice11objc_objectP7NSArrayIP8NSNumberEmf
+ __Z21createMetalBufferRandIhEPU19objcproto9MTLBuffer11objc_objectPU19objcproto9MTLDevice11objc_objectP7NSArrayIP8NSNumberEmf
+ __Z21getMPSGraphExecutableR15BRNetDescriptorP29MPSGraphCompilationDescriptor
+ __Z22makeMTLBufferForTensorPU19objcproto9MTLDevice11objc_objectiiiRjPib29MPSGraphTensorNamedDataLayout
+ __Z23getEmitModelWeightsData13DBFNetVersion
+ __Z23getEmitModelWeightsData13UBFNetVersion
+ __Z23getEmitModelWeightsPath13DBFNetVersion
+ __Z23getEmitModelWeightsPath13UBFNetVersion
+ __Z25functionFromLibraryMetal4PU21objcproto10MTLLibrary11objc_objectP8NSStringP25MTLFunctionConstantValues
+ __Z25makeMPSTensorDataWithDataP14MPSGraphDeviceiiiP8NSStringPib29MPSGraphTensorNamedDataLayout
+ __Z34checkInputOutputTexturesForSpatialPU21objcproto10MTLTexture11objc_objectS0_mm14MTLPixelFormatmmmmS1_
+ __Z36EmitDBF_Net_V2_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor
+ __Z36EmitDBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor
+ __Z37getTemporalScalarBRNetVersionOverride12BRNetVersion
+ __Z37getTemporalScalarBRNetVersionOverride12BRNetVersion.cold.1
+ __Z7newHeapPU43objcproto32MTL4MachineLearningPipelineState11objc_objectPU26objcproto15MTLResidencySet11objc_object
+ __ZGVZL18MetalFXHUDInstancevE4inst
+ __ZGVZL20MetalFXHUDInstanceV3vE2v3
+ __ZL14loadTensorDataP8NSStringmP18MPSGraphTensorData
+ __ZL14saveTensorDataP8NSStringS0_mP18MPSGraphTensorData
+ __ZL17MetalFXHUDEnabledv
+ __ZL17WEAK_HUDServiceV3v
+ __ZL18MetalFXHUDInstancev
+ __ZL20MetalFXHUDInstanceV3v
+ __ZL25getDefaultBRNetDescriptor12BRNetVersioniii
+ __ZL25getDefaultBRNetDescriptor12BRNetVersioniii.cold.1
+ __ZL29WEAK_CADeveloperHUDPropertiesv
+ __ZL36EmitBR_Net_V35_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor
+ __ZL36EmitUBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16UBFNetDescriptor
+ __ZL37getMTLFXTemporalScalerVersionOverride26MTLFXTemporalScalerVersion
+ __ZL37getMTLFXTemporalScalerVersionOverride26MTLFXTemporalScalerVersion.cold.1
+ __ZL37getMTLFXTemporalScalerVersionOverride26MTLFXTemporalScalerVersion.cold.2
+ __ZL41EmitBR_Net_V40_nchw_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor
+ __ZL41EmitBR_Net_V40_nhwc_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor
+ __ZL41EmitBR_Net_V41_nchw_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor
+ __ZL41EmitBR_Net_V41_nhwc_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor
+ __ZN10MFXDevice316createTileShaderEPU21objcproto10MTLLibrary11objc_objectP8NSString14MTLPixelFormatP25MTLFunctionConstantValues
+ __ZN10MFXDevice321createComputePipelineEPU21objcproto10MTLLibrary11objc_objectP8NSStringP25MTLFunctionConstantValues
+ __ZN10MFXDevice3D1Ev
+ __ZN10MFXDevice412createBufferEm
+ __ZN10MFXDevice413createTextureEP20MTLTextureDescriptor
+ __ZN10MFXDevice416createTileShaderEPU21objcproto10MTLLibrary11objc_objectP8NSString14MTLPixelFormatP25MTLFunctionConstantValues
+ __ZN10MFXDevice421createComputePipelineEPU21objcproto10MTLLibrary11objc_objectP8NSStringP25MTLFunctionConstantValues
+ __ZN10MFXDevice4C2EPU19objcproto9MTLDevice11objc_objectPU23objcproto12MTL4Compiler11objc_object
+ __ZN12FrameGenImplI10MFXDevice3E8encodeToERS0_PU27objcproto16MTLCommandBuffer11objc_objectRK14FrameGenParams
+ __ZN12FrameGenImplI10MFXDevice3EC1ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_
+ __ZN12FrameGenImplI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_
+ __ZN12FrameGenImplI10MFXDevice3ED1Ev
+ __ZN12FrameGenImplI10MFXDevice3ED2Ev
+ __ZN12FrameGenImplI10MFXDevice4E8encodeToERS0_PU28objcproto17MTL4CommandBuffer11objc_objectRK14FrameGenParams
+ __ZN12FrameGenImplI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_
+ __ZN14FrameGenParamsD2Ev
+ __ZN15BFNet_v1_Filter10encodePostEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objecth
+ __ZN15BFNet_v1_Filter12encodeAtrousEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_S5_S5_S5_S5_S5_S5_Dv2_fS6_h
+ __ZN15BFNet_v1_Filter9encodeMidEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_S5_S5_Dv2_fS6_bRK13simd_float4x4S9_Dv4_fh
+ __ZN15BFNet_v1_Filter9encodePreEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_PU19objcproto9MTLBuffer11objc_objectDv2_fS8_bh
+ __ZN15BFNet_v1_FilterC1EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK16DBFNetDescriptorbbb
+ __ZN15BFNet_v1_FilterC2EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK16DBFNetDescriptorbbb
+ __ZN15BFNet_v1_FilterD2Ev
+ __ZN15BRNet_v3_Filter19encodeMidForDenoiseEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_Dv2_fS6_ffbDv2_tS6_h
+ __ZN15BRNet_v3_Filter19encodePreForDenoiseEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_S5_S5_S5_S5_PU19objcproto9MTLBuffer11objc_objectDv2_fS8_ffbbbfDv2_th
+ __ZN15BRNet_v3_Filter19getInternalExposureEv
+ __ZN15BRNet_v3_Filter9encodeMidEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_Dv2_fS6_bDv2_tS6_h
+ __ZN15BRNet_v3_FilterC1EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbb
+ __ZN15BRNet_v3_FilterC2EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbb
+ __ZN17MFXRenderEncoder313beginEncodingEPU27objcproto16MTLCommandBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectm
+ __ZN17MFXRenderEncoder411endEncodingEv
+ __ZN17MFXRenderEncoder413beginEncodingEPU28objcproto17MTL4CommandBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectmPU28objcproto17MTL4ArgumentTable11objc_object
+ __ZN17MFXRenderEncoder413setTileBufferEPU19objcproto9MTLBuffer11objc_objectmj
+ __ZN17MFXRenderEncoder414setTileTextureEPU21objcproto10MTLTexture11objc_objectj
+ __ZN17MFXRenderEncoder4D1Ev
+ __ZN18MFXComputeEncoder313beginEncodingEPU27objcproto16MTLCommandBuffer11objc_object
+ __ZN18MFXComputeEncoder410setTextureEPU21objcproto10MTLTexture11objc_objectj
+ __ZN18MFXComputeEncoder411endEncodingEv
+ __ZN18MFXComputeEncoder413beginEncodingEPU28objcproto17MTL4CommandBuffer11objc_objectPU28objcproto17MTL4ArgumentTable11objc_object
+ __ZN18MFXComputeEncoder48setBytesEPKvmj
+ __ZN18MFXComputeEncoder49setBufferEPU19objcproto9MTLBuffer11objc_objectmj
+ __ZN18MFXComputeEncoder4C2EPU19objcproto9MTLDevice11objc_object
+ __ZN18MFXComputeEncoder4D2Ev
+ __ZN22BFNet_v1_Metal4_Filter10encodePostEPU28objcproto17MTL4CommandBuffer11objc_objectPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objecth
+ __ZN22BFNet_v1_Metal4_Filter12encodeAtrousEPU28objcproto17MTL4CommandBuffer11objc_objectPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_S5_S5_S5_S5_Dv2_fS6_h
+ __ZN22BFNet_v1_Metal4_Filter9encodePreEPU28objcproto17MTL4CommandBuffer11objc_objectPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_PU19objcproto9MTLBuffer11objc_objecth
+ __ZN22BFNet_v1_Metal4_FilterC1EPU19objcproto9MTLDevice11objc_objectPU23objcproto12MTL4Compiler11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiPU26objcproto15MTLResidencySet11objc_objectRK16DBFNetDescriptor
+ __ZN22BFNet_v1_Metal4_FilterC2EPU19objcproto9MTLDevice11objc_objectPU23objcproto12MTL4Compiler11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiPU26objcproto15MTLResidencySet11objc_objectRK16DBFNetDescriptor
+ __ZN22BFNet_v1_Metal4_FilterD2Ev
+ __ZN22BRNet_v3_Metal4_Filter10encodePostEPU28objcproto17MTL4CommandBuffer11objc_objectPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS7_S7_S7_Dv2_fS8_fffbDv2_th
+ __ZN22BRNet_v3_Metal4_Filter12encodeLowResEPU36objcproto25MTL4ComputeCommandEncoder11objc_objectRKDv2_tPU21objcproto10MTLTexture11objc_objectS6_S6_PU19objcproto9MTLBuffer11objc_objectS8_S8_h
+ __ZN22BRNet_v3_Metal4_Filter17encodeWarpHistoryEPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectPU19objcproto9MTLBuffer11objc_objectS5_h
+ __ZN22BRNet_v3_Metal4_Filter18encodeAutoexposureEPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectPU19objcproto9MTLBuffer11objc_objectS5_S5_h
+ __ZN22BRNet_v3_Metal4_Filter18encodeLowResSignalEPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS3_S3_S3_S3_PU19objcproto9MTLBuffer11objc_objectS5_S5_h
+ __ZN22BRNet_v3_Metal4_Filter19encodeMidForDenoiseEPU28objcproto17MTL4CommandBuffer11objc_objectPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_Dv2_fS6_ffbDv2_tS6_h
+ __ZN22BRNet_v3_Metal4_Filter19encodePreForDenoiseEPU28objcproto17MTL4CommandBuffer11objc_objectPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_S5_S5_S5_S5_PU19objcproto9MTLBuffer11objc_objectDv2_fS8_ffbbbfDv2_th
+ __ZN22BRNet_v3_Metal4_Filter22encodeExposureToBufferEPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectPU19objcproto9MTLBuffer11objc_objecth
+ __ZN22BRNet_v3_Metal4_Filter9encodeMidEPU28objcproto17MTL4CommandBuffer11objc_objectPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_Dv2_fS6_bDv2_tS6_h
+ __ZN22BRNet_v3_Metal4_Filter9encodePreEPU28objcproto17MTL4CommandBuffer11objc_objectPU36objcproto25MTL4ComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_PU19objcproto9MTLBuffer11objc_objectDv2_fS8_ffbbbfDv2_th
+ __ZN22BRNet_v3_Metal4_FilterC1EPU19objcproto9MTLDevice11objc_objectPU23objcproto12MTL4Compiler11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbPU26objcproto15MTLResidencySet11objc_objectbbb
+ __ZN22BRNet_v3_Metal4_FilterC2EPU19objcproto9MTLDevice11objc_objectPU23objcproto12MTL4Compiler11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbPU26objcproto15MTLResidencySet11objc_objectbbb
+ __ZN22BRNet_v3_Metal4_FilterD2Ev
+ __ZN33MPSGraphMPSGraphExecutableWrapper3runEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_bbPU18objcproto8MTLEvent11objc_objectS5_yy
+ __ZN33MPSGraphMPSGraphExecutableWrapper3runEPU27objcproto16MTLCommandBuffer11objc_objectP18MPSGraphTensorDataS3_bb
+ __ZN33MPSGraphMPSGraphExecutableWrapper7prewarmEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_byPU18objcproto8MTLEvent11objc_objectS5_yy
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI13AppBundleInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI18AppFeatureOverrideEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocator_destroyB8ne200100INS_9allocatorI13AppBundleInfoEENS_16reverse_iteratorIPS2_EES6_EEvRT_T0_T1_
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI13AppBundleInfoEEPS3_EEED2B8ne200100Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorI13AppBundleInfoEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorI13AppBundleInfoNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI13AppBundleInfoNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI13AppBundleInfoNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPKS1_S7_EEvT_T0_m
+ __ZNSt3__16vectorI13AppBundleInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI13AppBundleInfoNS_9allocatorIS1_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorI18AppFeatureOverrideNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI18AppFeatureOverrideNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPKS1_S7_EEvT_T0_m
+ __ZNSt3__16vectorI18AppFeatureOverrideNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI18AppFeatureOverrideNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZZL18MetalFXHUDInstancevE4inst
+ __ZZL20MetalFXHUDInstanceV3vE2v3
+ __ZZL21metalfxForceNoPreWarmvE9noPrewarm
+ __ZZL21metalfxForceNoPreWarmvE9onceToken
+ __ZZL24MetalFXHUDAddTAAUMetricsvE9onceToken
+ ___47-[_MTL4FXEffect _beginEncodeWithCommandBuffer:]_block_invoke
+ ___49-[_MTL4FXSpatialScaler _emitTelemetry:forDevice:]_block_invoke
+ ___53-[_MFXTemporalScalingEffectV3 encodeToCommandBuffer:]_block_invoke_4.cold.1
+ ___53-[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]_block_invoke
+ ___53-[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]_block_invoke.cold.1
+ ___53-[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]_block_invoke_2
+ ___53-[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]_block_invoke_3
+ ___53-[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]_block_invoke_4
+ ___53-[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]_block_invoke_5
+ ___53-[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]_block_invoke_6
+ ___53-[_MFXTemporalScalingEffectV4 encodeToCommandBuffer:]_block_invoke_6.cold.1
+ ___57-[_MTLFXTemporalDenoisedScaler _emitTelemetry:forDevice:]_block_invoke
+ ___58-[_MTL4FXTemporalDenoisedScaler _emitTelemetry:forDevice:]_block_invoke
+ ___60-[_MFXTemporalDenoisingScalingEffect encodeToCommandBuffer:]_block_invoke
+ ___60-[_MFXTemporalDenoisingScalingEffect encodeToCommandBuffer:]_block_invoke_2
+ ___60-[_MFXTemporalDenoisingScalingEffect encodeToCommandBuffer:]_block_invoke_2.cold.1
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ____Z36EmitDBF_Net_V2_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor_block_invoke
+ ____Z36EmitDBF_Net_V2_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor_block_invoke_2
+ ____Z36EmitDBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor_block_invoke
+ ____Z36EmitDBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor_block_invoke_2
+ ____ZL21metalfxForceNoPreWarmv_block_invoke
+ ____ZL24MetalFXHUDAddTAAUMetricsv_block_invoke
+ ____ZL36EmitUBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16UBFNetDescriptor_block_invoke
+ ____ZL36EmitUBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16UBFNetDescriptor_block_invoke_2
+ ____ZN33MPSGraphMPSGraphExecutableWrapper7prewarmEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_byPU18objcproto8MTLEvent11objc_objectS5_yy_block_invoke
+ ____ZN33MPSGraphMPSGraphExecutableWrapper7prewarmEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_byPU18objcproto8MTLEvent11objc_objectS5_yy_block_invoke_2
+ ___block_descriptor_188_ea8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_188_ea8_32s40s48s56s64s72s80s_e76_B24?0"<MTLCommandBuffer>"8r^{_MTLCommandBufferSynchronizationInfo=iQ^Q}16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_40_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_ea8_32s_e31_v32?0"MPSGraphTensor"8Q16^B24ls32l8
+ ___block_descriptor_48_ea8_32s_e28_v16?0"<MTLCommandBuffer>"8ls32l8
+ ___block_literal_global.101
+ ___block_literal_global.1341
+ ___block_literal_global.517
+ ___block_literal_global.525
+ ___block_literal_global.531
+ ___block_literal_global.539
+ ___block_literal_global.609
+ ___invert_f4
+ __denoiserScaler
+ __denoiserScaler4
+ __impl
+ __temporalScaler
+ __temporalScaler4
+ _abort
+ _bzero
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _memcpy
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$_beginEncodeWithCommandBuffer:
+ _objc_msgSend$addAllocation:
+ _objc_msgSend$addMetric:name:unit:nameColor:valueColor:visualType:options:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addResetHandler:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:
+ _objc_msgSend$barrierAfterStages:beforeQueueStages:visibilityOptions:
+ _objc_msgSend$blitCommandEncoder
+ _objc_msgSend$castTensor:toType:name:
+ _objc_msgSend$commandAllocator
+ _objc_msgSend$commandBufferWithCommandBuffer:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$concatTensors:dimension:interleave:name:
+ _objc_msgSend$config
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$convolutionTranspose2DWithSourceTensor:weightsTensor:outputShapeTensor:descriptor:name:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$date
+ _objc_msgSend$denoiseStrengthMaskTextureFormat
+ _objc_msgSend$denoiserScaler
+ _objc_msgSend$denoiserScaler4
+ _objc_msgSend$description
+ _objc_msgSend$descriptorWithKernelSizes:strides:dilationRates:paddingValues:paddingStyle:
+ _objc_msgSend$diffuseAlbedoTextureFormat
+ _objc_msgSend$dilatedMotionVectors
+ _objc_msgSend$dimensions
+ _objc_msgSend$dispatchNetworkWithIntermediatesHeap:
+ _objc_msgSend$encodeToCommandBuffer:inputsArray:resultsArray:executionDescriptor:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$extentAtDimensionIndex:
+ _objc_msgSend$feedTensors
+ _objc_msgSend$gpuAddress
+ _objc_msgSend$gpuResourceID
+ _objc_msgSend$initWithDevice:compiler:descriptor:
+ _objc_msgSend$initWithDevice:compiler:descriptor:history:
+ _objc_msgSend$initWithDevice:descriptor:compiler:history:
+ _objc_msgSend$initWithRank:extents:
+ _objc_msgSend$intermediatesHeapSize
+ _objc_msgSend$isDenoiseStrengthMaskTextureEnabled
+ _objc_msgSend$isSpecularHitDistanceTextureEnabled
+ _objc_msgSend$isTransparencyOverlayTextureEnabled
+ _objc_msgSend$isUITextureComposited
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$machineLearningCommandEncoder
+ _objc_msgSend$markBlitEncoder:component:
+ _objc_msgSend$markCommandBuffer:component:
+ _objc_msgSend$markComputeEncoder:component:
+ _objc_msgSend$markRenderEncoder:component:
+ _objc_msgSend$maxPooling4DWithSourceTensor:descriptor:name:
+ _objc_msgSend$metalFXFrameInterpolatorEncodingEnd:
+ _objc_msgSend$multiplicationWithPrimaryTensor:secondaryTensor:name:
+ _objc_msgSend$newArgumentTableWithDescriptor:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newComputePipelineStateWithFunction:error:
+ _objc_msgSend$newFence
+ _objc_msgSend$newHeapWithDescriptor:
+ _objc_msgSend$newMachineLearningPipelineStateWithDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newRenderPipelineStateWithTileDescriptor:options:reflection:error:
+ _objc_msgSend$newResidencySetWithDescriptor:error:
+ _objc_msgSend$newTemporalDenoisedScalerWithDevice:
+ _objc_msgSend$newTensorWithDescriptor:offset:error:
+ _objc_msgSend$normalTextureFormat
+ _objc_msgSend$popDebugGroup
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$pushDebugGroup:
+ _objc_msgSend$rank
+ _objc_msgSend$readBytes:strideBytes:
+ _objc_msgSend$resizeBilinearWithTensor:sizeTensor:centerResult:alignCorners:name:
+ _objc_msgSend$roughnessTextureFormat
+ _objc_msgSend$scaler
+ _objc_msgSend$scaler4
+ _objc_msgSend$setAddress:atIndex:
+ _objc_msgSend$setAllowedComputeDevices:
+ _objc_msgSend$setArgumentTable:
+ _objc_msgSend$setArgumentTable:atStages:
+ _objc_msgSend$setCeilMode:
+ _objc_msgSend$setComputeFunctionDescriptor:
+ _objc_msgSend$setConstantValues:
+ _objc_msgSend$setDataType:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDenoiseStrengthMaskTextureEnabled:
+ _objc_msgSend$setDenoiseStrengthMaskTextureFormat:
+ _objc_msgSend$setDenoiserScaler4:
+ _objc_msgSend$setDenoiserScaler:
+ _objc_msgSend$setDeviceSelection:
+ _objc_msgSend$setDiffuseAlbedoTextureFormat:
+ _objc_msgSend$setDimensions:
+ _objc_msgSend$setEnableCommitAndContinue:
+ _objc_msgSend$setFragmentFunctionDescriptor:
+ _objc_msgSend$setFunctionDescriptor:
+ _objc_msgSend$setIncludeZeroPadToAverage:
+ _objc_msgSend$setInitializeBindings:
+ _objc_msgSend$setInputDimensions:atBufferIndex:
+ _objc_msgSend$setIsUITextureComposited:
+ _objc_msgSend$setLibrary:
+ _objc_msgSend$setMachineLearningFunctionDescriptor:
+ _objc_msgSend$setMaxBufferBindCount:
+ _objc_msgSend$setMaxTextureBindCount:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNormalTextureFormat:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setPipelineState:
+ _objc_msgSend$setPreferredDevice:
+ _objc_msgSend$setResource:atBufferIndex:
+ _objc_msgSend$setRoughnessTextureFormat:
+ _objc_msgSend$setScaler:
+ _objc_msgSend$setShouldResetHistory:
+ _objc_msgSend$setSize:
+ _objc_msgSend$setSpecializedName:
+ _objc_msgSend$setSpecularAlbedoTextureFormat:
+ _objc_msgSend$setSpecularHitDistanceTextureEnabled:
+ _objc_msgSend$setSpecularHitDistanceTextureFormat:
+ _objc_msgSend$setStrides:
+ _objc_msgSend$setThreadgroupSizeMatchesTileSize:
+ _objc_msgSend$setTileFunctionDescriptor:
+ _objc_msgSend$setTransparencyOverlayTextureEnabled:
+ _objc_msgSend$setTransparencyOverlayTextureFormat:
+ _objc_msgSend$setType:
+ _objc_msgSend$setVertexFunctionDescriptor:
+ _objc_msgSend$shapeOfTensor:name:
+ _objc_msgSend$shouldResetHistory
+ _objc_msgSend$showInternalMetrics
+ _objc_msgSend$sliceTensor:starts:ends:strides:startMask:endMask:squeezeMask:name:
+ _objc_msgSend$spaceToDepth2DTensor:widthAxisTensor:heightAxisTensor:depthAxisTensor:blockSize:usePixelShuffleOrder:name:
+ _objc_msgSend$specularAlbedoTextureFormat
+ _objc_msgSend$specularHitDistanceTextureFormat
+ _objc_msgSend$status
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$supportsMetal4FX:
+ _objc_msgSend$targetTensors
+ _objc_msgSend$transparencyOverlayTextureFormat
+ _objc_msgSend$transposeTensor:permute:name:
+ _objc_msgSend$uiTextureFormat
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$updateFence:afterEncoderStages:
+ _objc_msgSend$updateLabelMetric:label:
+ _objc_msgSend$useResidencySet:
+ _objc_msgSend$waitForFence:beforeEncoderStages:
+ _objc_msgSend$waitUntilCompleted
+ _objc_msgSend$writeBytes:strideBytes:
+ _objc_msgSend$writeToFile:options:error:
+ _objc_release_x10
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x26
+ _strcmp
- -[_MTLFXEffect _beginEncode]
- -[_MTLFXEffect effectID]
- -[_MTLFXEffect init]
- GCC_except_table22
- GCC_except_table40
- GCC_except_table41
- OBJC_IVAR_$__MTLFXEffect._effectID
- OBJC_IVAR_$__MTLFXEffect._encodeID
- _OBJC_IVAR_$__MFXTemporalScalingEffectV3._hudProperties
- __OBJC_$_PROP_LIST_MTLFXSpatialScaler
- __OBJC_$_PROP_LIST_MTLFXTemporalScaler
- __Z14isAtLeast2160pjj
- __Z21createMetalBufferRandIDhEPU19objcproto9MTLBuffer11objc_objectPU19objcproto9MTLDevice11objc_objectiiimf
- __Z21createMetalBufferRandIhEPU19objcproto9MTLBuffer11objc_objectPU19objcproto9MTLDevice11objc_objectiiimf
- __Z25makeMPSTensorDataWithDataP14MPSGraphDeviceiiiP8NSStringPib
- __Z36EmitBR_Net_V35_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor
- __Z39EmitBR_Net_V35_2x_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor
- __ZN15BRNet_v3_Filter9encodeMidEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_Dv2_fS6_ffbDv2_tS6_h
- __ZN15BRNet_v3_FilterC1EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbb
- __ZN15BRNet_v3_FilterC2EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbb
- __ZN33MPSGraphMPSGraphExecutableWrapper3runEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_bbPU25objcproto14MTLSharedEvent11objc_objectS5_yy
- __ZN33MPSGraphMPSGraphExecutableWrapper7prewarmEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_byPU25objcproto14MTLSharedEvent11objc_objectS5_yy
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI13AppBundleInfoEEPS2_EclB8ne190102Ev
- __ZNKSt3__16vectorI18AppFeatureOverrideNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI18AppFeatureOverrideEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI13AppBundleInfoEEPS3_EEED2B8ne190102Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorI13AppBundleInfoEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_
- __ZNSt3__16vectorI13AppBundleInfoNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI18AppFeatureOverrideNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI18AppFeatureOverrideNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
- __ZNSt3__19allocatorI13AppBundleInfoE7destroyB8ne190102EPS1_
- __ZNSt3__19allocatorI13AppBundleInfoE9constructB8ne190102IS1_JRKS1_EEEvPT_DpOT0_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ____ZN33MPSGraphMPSGraphExecutableWrapper7prewarmEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_byPU25objcproto14MTLSharedEvent11objc_objectS5_yy_block_invoke
- ____ZN33MPSGraphMPSGraphExecutableWrapper7prewarmEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_byPU25objcproto14MTLSharedEvent11objc_objectS5_yy_block_invoke_2
CStrings:
+ ""
+ "!useANE"
+ "\"\xe5S"
+ "%@"
+ "%@ and Color should have the same height for MetalFX use"
+ "%@ and Color should have the same width for MetalFX use"
+ "%@ pixel format mismatch from descriptor"
+ "%@ texture height mismatch from descriptor"
+ "%@ texture must not be nil"
+ "%@ texture type should be MTLTextureType2D, create MTLTextureType2D texture view for MetalFX use"
+ "%@ texture width mismatch from descriptor"
+ "%@/%@_%04d.dat"
+ "%@_%@_%04d_%@.dat"
+ "%@_%d_%@"
+ "%lux%lu"
+ "%s %f"
+ "-[MTLFXTemporalDenoisedScalerDescriptor newTemporalDenoisedScalerWithHistoryTexture:]"
+ "-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 initWithDevice:compiler:descriptor:]"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/Framework/MPSGraphMPSGraphExecutableWrapper.h"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/Framework/Metal4FXFrameInterpolatorEffect.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/Framework/Metal4FXSpatialScalingEffectV1.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/Framework/Metal4FXTemporalDenoisingScalingEffect.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/Framework/Metal4FXTemporalScalingEffectV4.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/Framework/MetalFXFrameInterpolatorEffect.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/Framework/MetalFXTemporalDenoisingScalingEffect.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectV4.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/MetalFX-Utilities/MetalFX-Utilities.h"
+ "/Library/Caches/com.apple.xbs/Sources/MetalFX/MetalFX-Utilities/MetalFX-Utilities.mm"
+ "/tmp/metalfx/dump"
+ "/tmp/metalfx/ref"
+ "1"
+ "@\"<MTL4ArgumentTable>\""
+ "@\"<MTL4CommandQueue>\""
+ "@\"<MTL4FXEffectTracingDelegate>\""
+ "@\"<MTL4FXTemporalDenoisedScaler>\""
+ "@\"<MTL4FXTemporalDenoisedScalerSPI>\""
+ "@\"<MTL4FXTemporalScaler>\""
+ "@\"<MTL4FXTemporalScalerSPI>\""
+ "@\"<MTL4MachineLearningPipelineState>\""
+ "@\"<MTLFXTemporalDenoisedScaler>\""
+ "@\"<MTLFXTemporalScaler>\""
+ "@\"<MTLHeap>\""
+ "@\"<MTLResidencySet>\""
+ "@\"<MTLTensor>\""
+ "@\"MTL4RenderPassDescriptor\""
+ "@\"NSMutableArray\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"NSString\""
+ "@48@0:8@16@24@32@40"
+ "Analyze histogram"
+ "Auto"
+ "BRNet version is overridden from %d to %d using Env MTLFX_TEMPORAL_SCALER_BRNET_VERSION"
+ "BRNet3"
+ "BRNet4"
+ "Color"
+ "Copy image"
+ "Creating directory %@ for dumping tensors"
+ "Debug output"
+ "Denoiser scaler object does not conform to MTLFXTemporalDenoisedScaler protocol"
+ "Denoising"
+ "Denoising | ANE"
+ "Denoising | GPU"
+ "Depth"
+ "Depth and Motion should have the same height for MetalFX use"
+ "Depth and Motion should have the same width for MetalFX use"
+ "Depth texture must not be nil"
+ "Directory %@ for dumping tensors already exits"
+ "Downsample"
+ "Dump tensors : Encode unblocked"
+ "Dump tensors : Unblock Encode"
+ "Env MTLFX_USE_REF_TENSORS is set. Tensors will be read from directory %@"
+ "Error compiling compute pipeline: %@"
+ "Error creating directory %@ : %@. Tensors will not be dumped to file"
+ "Error creating library %@"
+ "Error tensorData.mpsndarray returned NIL. Failed to write save tensor data for frame=%d"
+ "Error writing file %@ : %@\n"
+ "Error: %@"
+ "Exposure"
+ "Failed to load tensor from path %@ for frame %d. Error: Failed to create NSFileManager instance."
+ "Failed to load tensor from path %@ for frame %d. Error: File doesn't exist"
+ "Failed to load tensor from path %@ for frame %d. tensorData.mpsndarray returned NIL"
+ "Fill cracks game motion vectors"
+ "Inpaint optical motion vectors"
+ "Input/Output texture height mismatch"
+ "Input/Output texture width mismatch"
+ "MFXTemporalDenoisingScalingEffectDescriptor"
+ "MPSGraph TensorData failed. Layout=%lu. Shape=(%lu,%lu,%lu,%lu), Stride=%lu bytes"
+ "MPSGraphMPSGraphExecutableWrapper.h"
+ "MTL4FXFrameInterpolator"
+ "MTL4FXFrameInterpolatorSPI"
+ "MTL4FXSpatialScaler"
+ "MTL4FXSpatialScalerSPI"
+ "MTL4FXTemporalDenoisedScaler"
+ "MTL4FXTemporalDenoisedScalerSPI"
+ "MTL4FXTemporalScaler"
+ "MTL4FXTemporalScalerSPI"
+ "MTLFXFrameInterpolator"
+ "MTLFXFrameInterpolatorBase"
+ "MTLFXFrameInterpolatorDescriptor"
+ "MTLFXFrameInterpolatorSPI"
+ "MTLFXSpatialScalerBase"
+ "MTLFXTemporalDenoisedScaler"
+ "MTLFXTemporalDenoisedScalerBase"
+ "MTLFXTemporalDenoisedScalerDescriptor"
+ "MTLFXTemporalDenoisedScalerSPI"
+ "MTLFXTemporalScalerBase"
+ "MTLFXTemporalScalerVersion is being overridden using MTLFX_TEMPORAL_SCALER_VERSION to %s (%lu -> %lu)"
+ "MTLFX_DUMP_TENSORS"
+ "MTLFX_EXPOSURE_TOOL_ENABLED"
+ "MTLFX_Frame_Interpolation"
+ "MTLFX_NO_PREWARM"
+ "MTLFX_TEMPORAL_SCALER_BRNET_VERSION"
+ "MTLFX_TEMPORAL_SCALER_VERSION"
+ "MTLFX_TEMPORAL_SCALER_VERSION set to unknown value (%s)"
+ "MTLFX_USE_REF_TENSORS"
+ "Malloc failed. Buffer size=%lu bytes"
+ "Metal Buffer creation failed. Layout=%lu. Shape=(%lu,%lu,%lu,%lu). Stride=%lu bytes"
+ "Metal4FX_Normalize"
+ "Metal4FX_Scale"
+ "Metal4FX_Sharpen"
+ "MetalFXTemporalScalingDenoisingEffect.mm"
+ "MetalFX_Denoise_DPostProcessing_UPreProcessing"
+ "MetalFX_Denoise_DPreProcessing"
+ "MetalFX_Denoiser_DMidProcessing"
+ "MetalFX_Denoiser_UMidProcessing"
+ "MetalFX_Temporal_MidProcessing"
+ "MetalFX_Temporal_PostProcessing"
+ "MetalFX_Temporal_PreProcessing"
+ "Motion"
+ "Motion texture must not be nil"
+ "Optical Motion Vectors"
+ "Output"
+ "Reference tensors load for Network is not supported"
+ "Saved tensor for frame %04d to file %@ (Shape=%@ Type=%s Bytecount=%lu)\n"
+ "Scaling"
+ "Scaling Input Res"
+ "Scaling Target Res"
+ "Semaphore creation failed"
+ "Spatial"
+ "Splat game motion vectors"
+ "Splat optical motion vectors"
+ "T@\"<MTL4FXEffectTracingDelegate>\",W,V_tracingDelegate"
+ "T@\"<MTL4FXTemporalDenoisedScaler>\",&,N,V_denoiserScaler4"
+ "T@\"<MTL4FXTemporalScaler>\",&,N,V_scaler4"
+ "T@\"<MTLFXTemporalDenoisedScaler>\",&,N,V_denoiserScaler"
+ "T@\"<MTLFXTemporalScaler>\",&,N,V_scaler"
+ "T@\"<MTLTexture>\",&,N,SsetUITexture:"
+ "T@\"<MTLTexture>\",&,N,SsetUITexture:,V_uiTexture"
+ "T@\"<MTLTexture>\",&,N,V_denoiseStrengthMaskTexture"
+ "T@\"<MTLTexture>\",&,N,V_diffuseAlbedoTexture"
+ "T@\"<MTLTexture>\",&,N,V_normalTexture"
+ "T@\"<MTLTexture>\",&,N,V_preUpscaleComposeTexture"
+ "T@\"<MTLTexture>\",&,N,V_prevColorTexture"
+ "T@\"<MTLTexture>\",&,N,V_roughnessTexture"
+ "T@\"<MTLTexture>\",&,N,V_specularAlbedoTexture"
+ "T@\"<MTLTexture>\",&,N,V_specularHitDistanceTexture"
+ "T@\"<MTLTexture>\",R,N"
+ "TAAU"
+ "TAAUv3 | ANE"
+ "TAAUv3 | GPU"
+ "TAAUv4 | ANE"
+ "TAAUv4 | GPU"
+ "TB,N,GisDenoiseStrengthMaskTextureEnabled,V_denoiseStrengthMaskTextureEnabled"
+ "TB,N,GisReactiveMaskTextureEnabled,V_reactiveMaskTextureEnabled"
+ "TB,N,GisSpecularHitDistanceTextureEnabled,V_specularHitDistanceTextureEnabled"
+ "TB,N,GisTransparencyOverlayTextureEnabled,V_transparencyOverlayTextureEnabled"
+ "TB,N,GisUITextureComposited,SsetIsUITextureComposited:"
+ "TB,N,GisUITextureComposited,SsetIsUITextureComposited:,V_uiTextureComposited"
+ "TB,N,VdepthInverted"
+ "TQ,N,SsetUITextureFormat:,V_uiTextureFormat"
+ "TQ,N,V_colorTextureBarrierStages"
+ "TQ,N,V_denoiseStrengthMaskTextureFormat"
+ "TQ,N,V_diffuseAlbedoTextureFormat"
+ "TQ,N,V_height"
+ "TQ,N,V_normalTextureFormat"
+ "TQ,N,V_reactiveMaskTextureFormat"
+ "TQ,N,V_roughnessTextureFormat"
+ "TQ,N,V_specularAlbedoTextureFormat"
+ "TQ,N,V_specularHitDistanceTextureFormat"
+ "TQ,N,V_transparencyOverlayTextureFormat"
+ "TQ,N,V_width"
+ "TQ,N,Vheight"
+ "TQ,N,VmaskTextureFormat"
+ "TQ,N,Vwidth"
+ "TQ,R,N,V_denoiseStrengthMaskTextureFormat"
+ "TQ,R,N,V_denoiseStrengthMaskTextureUsage"
+ "TQ,R,N,V_diffuseAlbedoTextureFormat"
+ "TQ,R,N,V_diffuseAlbedoTextureUsage"
+ "TQ,R,N,V_normalTextureFormat"
+ "TQ,R,N,V_normalTextureUsage"
+ "TQ,R,N,V_outputTextureBarrierStages"
+ "TQ,R,N,V_preUpscaleComposeTextureFormat"
+ "TQ,R,N,V_preUpscaleComposeTextureUsage"
+ "TQ,R,N,V_reactiveMaskTextureFormat"
+ "TQ,R,N,V_roughnessTextureFormat"
+ "TQ,R,N,V_roughnessTextureUsage"
+ "TQ,R,N,V_specularAlbedoTextureFormat"
+ "TQ,R,N,V_specularAlbedoTextureUsage"
+ "TQ,R,N,V_specularHitDistanceTextureFormat"
+ "TQ,R,N,V_specularHitDistanceTextureUsage"
+ "TQ,R,N,V_uiTextureFormat"
+ "TQ,R,N,V_uiTextureUsage"
+ "TQ,V_version"
+ "Temporal"
+ "Temporal scaler object does not conform to MTLFXTemporalScaler protocol"
+ "Tensor loaded from path %@ for frame %d"
+ "Tf,N,V_aspectRatio"
+ "Tf,N,V_deltaTime"
+ "Tf,N,V_farPlane"
+ "Tf,N,V_fieldOfView"
+ "Tf,N,V_jitterOffsetX"
+ "Tf,N,V_jitterOffsetY"
+ "Tf,N,V_motionVectorScaleX"
+ "Tf,N,V_motionVectorScaleY"
+ "Tf,N,V_nearPlane"
+ "T{?=[4]},N,V_viewToClipMatrix"
+ "T{?=[4]},N,V_worldToViewMatrix"
+ "Unsupported BRNet version"
+ "Unsupported dimension count. Only support 4"
+ "Upsample game motion vectors"
+ "User command buffer was committed by MPSGraph. MetalFX code committing the user CB would result in incorrect results"
+ "Using reference tensor is currently are not supported"
+ "Warp image"
+ "^v"
+ "^{BFNet_v1_Filter=iiiiii@@@@@@@@[2@][2@]@[2@][2@]@@@[2@][2@][2@]@@@@BBBC}"
+ "^{BFNet_v1_Metal4_Filter=iiiiii@@[16@]@@[16@]@@[16@][16@][16@]@@@@[4@][4@]@@[2@][2@]@[2@][2@]@@@@@CQ}"
+ "^{BRNet_v3_Filter=iiiiiiiiiiiiiiSSBBBBBBBBi@@@[2@][2@]C@@@@@@[2@][2@][2@]@@[2@]@[2@]@@@@@@@@@@@@@@@@@@@@@@@@}"
+ "^{BRNet_v3_Metal4_Filter=iiiiiiiiiiiiiiSSBBBBBBi@@@[2@][2@]C@@@@@@[2@][2@][2@]@@[2@]@@@@[16@]@@[16@][16@]@@@@[16@][16@]@@@[16@]@@[16@][16@]@@[16@][16@][16@][16@][16@][16@]@@@@@@@@@@@@[16@][16@][16@][16@]@@@@@@@@@@@@Q}"
+ "^{MFXDevice4=@@@@{MFXComputeEncoder4=@@@I}{MFXRenderEncoder4=@@}}"
+ "_"
+ "_M4FXFrameInterpolatorEffect"
+ "_M4FXTemporalDenoisingScalingEffect"
+ "_M4FXTemporalScalingEffectV4"
+ "_MFXFrameInterpolatorEffect"
+ "_MFXTemporalDenoisingScalingEffect"
+ "_MFXTemporalScalingEffectV4"
+ "_MTL4FXEffect"
+ "_MTL4FXFrameInterpolator"
+ "_MTL4FXSpatialScaler"
+ "_MTL4FXSpatialScalingEffectEFFECT_NAME_V1"
+ "_MTL4FXTemporalDenoisedScaler"
+ "_MTL4FXTemporalScaler"
+ "_MTLFXEffectBase"
+ "_MTLFXFrameInterpolator"
+ "_MTLFXTemporalDenoisedScaler"
+ "_aspectRatio"
+ "_beginEncodeWithCommandBuffer:"
+ "_brnet_desc"
+ "_colorTextureBarrierStages"
+ "_dbfNetArg"
+ "_dbfNetHeap"
+ "_dbfNetPSO"
+ "_dbfnet_desc"
+ "_dbfnet_input_TensorData"
+ "_dbfnet_input_TensorData_Buffer"
+ "_dbfnet_net_wrapper"
+ "_dbfnet_output_TensorData"
+ "_dbfnet_output_TensorData_Buffer"
+ "_deltaTime"
+ "_denoiseFilter"
+ "_denoiseStrengthMaskTexture"
+ "_denoiseStrengthMaskTextureEnabled"
+ "_denoiseStrengthMaskTextureFormat"
+ "_denoiseStrengthMaskTextureUsage"
+ "_denoiserColorTexture"
+ "_denoiserScaler"
+ "_denoiserScaler4"
+ "_diffuseAlbedoTexture"
+ "_diffuseAlbedoTextureFormat"
+ "_diffuseAlbedoTextureUsage"
+ "_dummyFence"
+ "_dumpTensors"
+ "_dumpTensorsDir"
+ "_emitTelemetry:forDevice:compiler:"
+ "_farPlane"
+ "_fieldOfView"
+ "_frame"
+ "_framesInFlight"
+ "_fxrSharpenBuffer"
+ "_fxrUpscaleBuffer"
+ "_height"
+ "_impl"
+ "_input_TensorData_Buffer"
+ "_internalFence"
+ "_jitterOffsetX"
+ "_jitterOffsetY"
+ "_maxFramesInFlightSemaphore"
+ "_mlHeap"
+ "_mlProcessingArgs"
+ "_mlProcessingPSO"
+ "_motionVectorScaleX"
+ "_motionVectorScaleY"
+ "_nearPlane"
+ "_needNormPercept"
+ "_netArg"
+ "_netHeap"
+ "_netPSO"
+ "_normPerceptFragInputs"
+ "_normalTexture"
+ "_normalTextureFormat"
+ "_normalTextureUsage"
+ "_normalizeBuffer"
+ "_outputTextureBarrierStages"
+ "_outputTextureBarrierStages not set"
+ "_output_TensorData_Buffer"
+ "_preUpscaleComposeTexture"
+ "_preUpscaleComposeTextureFormat"
+ "_preUpscaleComposeTextureUsage"
+ "_prevColorTexture"
+ "_prevViewProjectionMatrix"
+ "_reactiveMaskTextureEnabled"
+ "_residencySetGlobal"
+ "_residencySetPercept"
+ "_roughnessTexture"
+ "_roughnessTextureFormat"
+ "_roughnessTextureUsage"
+ "_scaleBuffer"
+ "_scaleFragInputs"
+ "_scaler"
+ "_scaler4"
+ "_sharpenBuffer"
+ "_sharpenFragInputs"
+ "_specularAlbedoTexture"
+ "_specularAlbedoTextureFormat"
+ "_specularAlbedoTextureUsage"
+ "_specularHitDistEnabled"
+ "_specularHitDistance"
+ "_specularHitDistanceTexture"
+ "_specularHitDistanceTextureEnabled"
+ "_specularHitDistanceTextureFormat"
+ "_specularHitDistanceTextureUsage"
+ "_temporalScaler"
+ "_transparencyOverlayTextureEnabled"
+ "_transparencyOverlayTextureFormat"
+ "_uiTexture"
+ "_uiTextureComposited"
+ "_uiTextureFormat"
+ "_uiTextureUsage"
+ "_useRefTensors"
+ "_version"
+ "_viewToClipMatrix"
+ "_waitForCompletion"
+ "_waitForPreviousEncode"
+ "_width"
+ "_worldToViewMatrix"
+ "addAllocation:"
+ "addMetric:name:unit:nameColor:valueColor:visualType:options:"
+ "addObject:"
+ "addResetHandler:"
+ "analyzeHistogram"
+ "arrayWithCapacity:"
+ "aspectRatio"
+ "barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:"
+ "barrierAfterStages:beforeQueueStages:visibilityOptions:"
+ "bilateral"
+ "blitCommandEncoder"
+ "brnet"
+ "brnet_ane"
+ "brnet_in"
+ "c. %lux%lu->%lux%lu"
+ "castTensor:toType:name:"
+ "clear game motion vectors"
+ "clear temp motion vectors"
+ "clearAppMotionVectors"
+ "colorTextureBarrierStages"
+ "com.apple.hud-label.metalfx.v2.exposure"
+ "com.apple.hud-label.metalfx.v2.input_resolution"
+ "com.apple.hud-label.metalfx.v2.scaling"
+ "com.apple.hud-label.metalfx.v2.target_resolution"
+ "com.apple.metal4fx.api.encoder"
+ "commandAllocator"
+ "commandBufferWithCommandBuffer:"
+ "componentsJoinedByString:"
+ "compositedUITexture"
+ "computeLuminance"
+ "concatTensors:dimension:interleave:name:"
+ "config"
+ "convolutionTranspose2DWithSourceTensor:weightsTensor:outputShapeTensor:descriptor:name:"
+ "copyImage"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dataWithBytes:length:"
+ "date"
+ "dbf"
+ "dbf_ane"
+ "dbfnetv1_lowres_signals"
+ "dbfnetv1_output_channels"
+ "debugShader"
+ "deltaTime"
+ "denoiseStrengthMaskTexture"
+ "denoiseStrengthMaskTextureEnabled"
+ "denoiseStrengthMaskTextureFormat"
+ "denoiseStrengthMaskTextureUsage"
+ "denoise_brnet_ip"
+ "denoise_brnet_op"
+ "denoiserScaler"
+ "denoiserScaler4"
+ "denoiser_between_processing"
+ "depthInverted"
+ "descriptorWithKernelSizes:strides:dilationRates:paddingValues:paddingStyle:"
+ "diffuseAlbedoTexture"
+ "diffuseAlbedoTextureFormat"
+ "diffuseAlbedoTextureUsage"
+ "dilate depth"
+ "dilateDepth"
+ "dilatedMotionVectors"
+ "dimensions"
+ "dispatchNetworkWithIntermediatesHeap:"
+ "downSample"
+ "dst_shape_1"
+ "dst_shape_2"
+ "dst_shape_3"
+ "dst_shape_4"
+ "emit_dbfnet_v3_constants.dat"
+ "emit_ubfnet_v3_constants.dat"
+ "emit_v40_nchw_constants.dat"
+ "emit_v40_nhwc_constants.dat"
+ "emit_v41_nchw_constants.dat"
+ "emit_v41_nhwc_constants.dat"
+ "encodeToCommandBuffer:inputsArray:resultsArray:executionDescriptor:"
+ "enumerateObjectsUsingBlock:"
+ "error allocating tensor with buffer: %@"
+ "error: %@"
+ "extentAtDimensionIndex:"
+ "farPlane"
+ "feedTensors"
+ "fieldOfView"
+ "file://%@"
+ "fillCracksAppMotionVectors"
+ "findOpticalMotionVectorsV3"
+ "generateLuminancePyramid"
+ "globalResidency"
+ "gpuAddress"
+ "gpuResourceID"
+ "initMotionVectors"
+ "initWithDevice:compiler:descriptor:"
+ "initWithDevice:compiler:descriptor:history:"
+ "initWithDevice:descriptor:compiler:history:"
+ "initWithRank:extents:"
+ "inpaintMotionVectors"
+ "intermediatesHeapSize"
+ "internalFence"
+ "internalMLFence"
+ "isDenoiseStrengthMaskTextureEnabled"
+ "isSpecularHitDistanceTextureEnabled"
+ "isTransparencyOverlayTextureEnabled"
+ "isUITextureComposited"
+ "localizedDescription"
+ "m_pDevice"
+ "machineLearningCommandEncoder"
+ "main"
+ "markBlitEncoder:component:"
+ "markCommandBuffer:component:"
+ "markComputeEncoder:component:"
+ "markRenderEncoder:component:"
+ "maskTextureFormat"
+ "maxPooling4DWithSourceTensor:descriptor:name:"
+ "medianFilter"
+ "metalFXFrameInterpolatorEncodingEnd:"
+ "mtlpackage"
+ "multiplicationWithPrimaryTensor:secondaryTensor:name:"
+ "nearPlane"
+ "newArgumentTableWithDescriptor:error:"
+ "newComputePipelineStateWithDescriptor:compilerTaskOptions:error:"
+ "newComputePipelineStateWithFunction:error:"
+ "newFence"
+ "newFrameInterpolatorWithDevice:"
+ "newFrameInterpolatorWithDevice:compiler:"
+ "newHeapWithDescriptor:"
+ "newMachineLearningPipelineStateWithDescriptor:error:"
+ "newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:"
+ "newRenderPipelineStateWithTileDescriptor:options:reflection:error:"
+ "newResidencySetWithDescriptor:error:"
+ "newSpatialScalerWithDevice:compiler:"
+ "newTemporalDenoisedScalerWithDevice:"
+ "newTemporalDenoisedScalerWithDevice:compiler:"
+ "newTemporalDenoisedScalerWithHistoryTexture:"
+ "newTemporalDenoisingScalingEffectWithDevice:"
+ "newTemporalScalerWithDevice:compiler:"
+ "newTemporalScalerWithHistoryTexture:compiler:"
+ "newTensorWithDescriptor:offset:error:"
+ "normalTexture"
+ "normalTextureFormat"
+ "normalTextureUsage"
+ "outputTextureBarrierStages"
+ "popDebugGroup"
+ "prevColorTexture"
+ "processIdentifier"
+ "processSpecularHitDistance"
+ "pushDebugGroup:"
+ "rank"
+ "readBytes:strideBytes:"
+ "reproject"
+ "residencyGlobal"
+ "resizeBilinearWithTensor:sizeTensor:centerResult:alignCorners:name:"
+ "roughnessTexture"
+ "roughnessTextureFormat"
+ "roughnessTextureUsage"
+ "scaler"
+ "scaler4"
+ "scaling_brnet_ip"
+ "scaling_brnet_op"
+ "setAddress:atIndex:"
+ "setAllowedComputeDevices:"
+ "setArgumentTable:"
+ "setArgumentTable:atStages:"
+ "setAspectRatio:"
+ "setCeilMode:"
+ "setColorTextureBarrierStages:"
+ "setCompositedUITexture:"
+ "setComputeFunctionDescriptor:"
+ "setConstantValues:"
+ "setDataType:"
+ "setDateFormat:"
+ "setDeltaTime:"
+ "setDenoiseStrengthMaskTexture:"
+ "setDenoiseStrengthMaskTextureEnabled:"
+ "setDenoiseStrengthMaskTextureFormat:"
+ "setDenoiserScaler4:"
+ "setDenoiserScaler:"
+ "setDepthInverted:"
+ "setDeviceSelection:"
+ "setDiffuseAlbedoTexture:"
+ "setDiffuseAlbedoTextureFormat:"
+ "setDimensions:"
+ "setEnableCommitAndContinue:"
+ "setFarPlane:"
+ "setFieldOfView:"
+ "setFragmentFunctionDescriptor:"
+ "setFunctionDescriptor:"
+ "setIncludeZeroPadToAverage:"
+ "setInitializeBindings:"
+ "setInputDimensions:atBufferIndex:"
+ "setIsUITextureComposited:"
+ "setLibrary:"
+ "setMachineLearningFunctionDescriptor:"
+ "setMaskTextureFormat:"
+ "setMaxBufferBindCount:"
+ "setMaxTextureBindCount:"
+ "setName:"
+ "setNearPlane:"
+ "setNormalTexture:"
+ "setNormalTextureFormat:"
+ "setObject:atIndexedSubscript:"
+ "setPipelineState:"
+ "setPreferredDevice:"
+ "setPrevColorTexture:"
+ "setResource:atBufferIndex:"
+ "setRoughnessTexture:"
+ "setRoughnessTextureFormat:"
+ "setScaler4:"
+ "setScaler:"
+ "setShouldResetHistory:"
+ "setSize:"
+ "setSpecializedName:"
+ "setSpecularAlbedoTexture:"
+ "setSpecularAlbedoTextureFormat:"
+ "setSpecularHitDistanceTexture:"
+ "setSpecularHitDistanceTextureEnabled:"
+ "setSpecularHitDistanceTextureFormat:"
+ "setStrides:"
+ "setThreadgroupSizeMatchesTileSize:"
+ "setTileFunctionDescriptor:"
+ "setTransparencyOverlayTexture:"
+ "setTransparencyOverlayTextureEnabled:"
+ "setTransparencyOverlayTextureFormat:"
+ "setType:"
+ "setUITexture:"
+ "setUITextureFormat:"
+ "setVertexFunctionDescriptor:"
+ "setViewToClipMatrix:"
+ "setWorldToViewMatrix:"
+ "shapeOfTensor:name:"
+ "shouldResetHistory"
+ "showInternalMetrics"
+ "sigmoid_tensor_out"
+ "sliceTensor:starts:ends:strides:startMask:endMask:squeezeMask:name:"
+ "spaceToDepth2DTensor:widthAxisTensor:heightAxisTensor:depthAxisTensor:blockSize:usePixelShuffleOrder:name:"
+ "specularAlbedoTexture"
+ "specularAlbedoTextureFormat"
+ "specularAlbedoTextureUsage"
+ "specularHitDistanceTexture"
+ "specularHitDistanceTextureEnabled"
+ "specularHitDistanceTextureFormat"
+ "specularHitDistanceTextureUsage"
+ "splatAppMotionVectors"
+ "splatOpticalMotionVectors"
+ "src_shape_1"
+ "src_shape_2"
+ "src_shape_3"
+ "src_shape_4"
+ "status"
+ "stringFromDate:"
+ "supportsMetal4FX:"
+ "targetTensors"
+ "tensor102_hwio"
+ "tensor108_hwio"
+ "tensor114_hwio"
+ "tensor120_hwio"
+ "tensor129_hwio"
+ "tensor136_hwio"
+ "tensor142_hwio"
+ "tensor151_hwio"
+ "tensor158_hwio"
+ "tensor164_hwio"
+ "tensor173_hwio"
+ "tensor182_hwio"
+ "tensor188_hwio"
+ "tensor194_hwio"
+ "tensor200_hwio"
+ "tensor22"
+ "tensor23"
+ "tensor24"
+ "tensor25"
+ "tensor26"
+ "tensor27"
+ "tensor28"
+ "tensor29"
+ "tensor30"
+ "tensor31"
+ "tensor32"
+ "tensor33"
+ "tensor34"
+ "tensor35"
+ "tensor36"
+ "tensor37"
+ "tensor38"
+ "tensor39"
+ "tensor40"
+ "tensor41"
+ "tensor41_biasReshape"
+ "tensor42"
+ "tensor43"
+ "tensor44"
+ "tensor44_biasReshape"
+ "tensor45"
+ "tensor46"
+ "tensor47"
+ "tensor47_biasReshape"
+ "tensor48"
+ "tensor49"
+ "tensor50"
+ "tensor50_biasReshape"
+ "tensor51"
+ "tensor52"
+ "tensor53"
+ "tensor53_biasReshape"
+ "tensor54"
+ "tensor55"
+ "tensor56"
+ "tensor56_biasReshape"
+ "tensor57"
+ "tensor58"
+ "tensor59"
+ "tensor59_biasReshape"
+ "tensor60"
+ "tensor61"
+ "tensor62"
+ "tensor62_biasReshape"
+ "tensor63"
+ "tensor64"
+ "tensor64_biasReshape"
+ "tensor65"
+ "tensor66"
+ "tensor66_biasReshape"
+ "tensor67"
+ "tensor67_biasReshape"
+ "tensor68"
+ "tensor69"
+ "tensor70"
+ "tensor71"
+ "tensor72"
+ "tensor73"
+ "tensor73_biasReshape"
+ "tensor74"
+ "tensor75"
+ "tensor76"
+ "tensor76_biasReshape"
+ "tensor77"
+ "tensor78"
+ "tensor79"
+ "tensor80"
+ "tensor81"
+ "tensor81_biasReshape"
+ "tensor82"
+ "tensor83"
+ "tensor84"
+ "tensor84_biasReshape"
+ "tensor84_hwio"
+ "tensor87_biasReshape"
+ "tensor90_biasReshape"
+ "tensor90_hwio"
+ "tensor96_hwio"
+ "transparencyOverlayTexture"
+ "transparencyOverlayTextureEnabled"
+ "transparencyOverlayTextureFormat"
+ "transparencyOverlayTextureUsage"
+ "transposeTensor:permute:name:"
+ "ubf"
+ "ubf_ane"
+ "uiTexture"
+ "uiTextureComposited"
+ "uiTextureFormat"
+ "uiTextureUsage"
+ "unsignedIntegerValue"
+ "updateFence:afterEncoderStages:"
+ "updateLabelMetric:label:"
+ "update_vbbr"
+ "upsampleAppMotionVectors"
+ "useResidencySet:"
+ "v24@0:8@\"<MTL4CommandBuffer>\"16"
+ "v32@?0@\"MPSGraphTensor\"8Q16^B24"
+ "v40@0:8@16@24@32"
+ "variance_update"
+ "viewToClipMatrix"
+ "waitForFence:beforeEncoderStages:"
+ "waitUntilCompleted"
+ "warpImage"
+ "worldToViewMatrix"
+ "writeBytes:strideBytes:"
+ "writeToFile:options:error:"
+ "x"
+ "yyyy_MM_dd_HH_mm_ss_SSS"
+ "{BRNetDescriptor=\"version\"i\"image_width\"I\"image_height\"I\"input_width\"I\"input_height\"I\"input_channels\"I\"input_unshuffle_ratio\"I\"unshuffle_width\"I\"unshuffle_height\"I\"unshuffle_channels\"I\"output_shuffle_ratio\"I\"output_width\"I\"output_height\"I\"output_channels\"I\"tensorDataLayout\"Q\"weight_file\"@\"NSString\"}"
+ "{DBFNetDescriptor=\"version\"i\"image_width\"I\"image_height\"I\"input_width\"I\"input_height\"I\"input_channels\"I\"output_width\"I\"output_height\"I\"output_channels\"I}"
+ "{MPSGraphMPSGraphExecutableWrapper=\"_graph\"@\"MPSGraph\"\"_graphExecutableANE\"@\"MPSGraphExecutable\"\"_graphExecutableGPU\"@\"MPSGraphExecutable\"\"_input_Tensor\"@\"MPSGraphTensor\"\"_output_Tensor\"@\"MPSGraphTensor\"\"_prewarm_group\"@\"NSObject<OS_dispatch_group>\"\"_prewarmComplete\"B}"
+ "{UBFNetDescriptor=\"version\"i\"image_width\"I\"image_height\"I\"input_width\"I\"input_height\"I\"input_channels\"I\"input_unshuffle_ratio\"I\"unshuffle_width\"I\"unshuffle_height\"I\"unshuffle_channels\"I\"output_shuffle_ratio\"I\"output_width\"I\"output_height\"I\"output_channels\"I\"up_channels\"I\"layers_channels\"[4I]}"
+ "\xd4"
+ "\xe5s"
- "(content size) %lux%lu->%lux%lu"
- "@\"<MTLSharedEvent>\""
- "Depth and Color should have the same height for MetalFX use"
- "Depth and Color should have the same width for MetalFX use"
- "MetalFXTemporalScalingEffectV3.h"
- "MetalFX_TemporalV3_MidProcessing"
- "MetalFX_TemporalV3_PostProcessing"
- "MetalFX_TemporalV3_PreProcessing"
- "Motion and Color should have the same height for MetalFX use"
- "Motion and Color should have the same width for MetalFX use"
- "Motion texture type should be MTLTextureType2D, create MTLTextureType2D texture view for MetalFX use"
- "Motion, Depth and Color should have the same width for MetalFX use"
- "Output texture height mismatch from descriptor"
- "Output texture must not be nil"
- "Output texture width mismatch from descriptor"
- "^{BRNet_v3_Filter=iiiiiiiiiiiiiSSBBBBBBi@@@[2@][2@]C@@@@@@[2@][2@][2@]@@[2@][2@]@@@@@@@@@@@@@@@@@@@@@@@}"
- "tensor100_biasReshape"
- "tensor106_biasReshape"
- "tensor112_biasReshape"
- "tensor118_biasReshape"
- "tensor124_biasReshape"
- "tensor138_biasReshape"
- "tensor144_biasReshape"
- "tensor160_biasReshape"
- "tensor166_biasReshape"
- "tensor180_biasReshape"
- "tensor186_biasReshape"
- "tensor192_biasReshape"
- "tensor198_biasReshape"
- "tensor88_biasReshape"
- "tensor94_biasReshape"
- "{MPSGraphMPSGraphExecutableWrapper=\"_graph\"@\"MPSGraph\"\"_graphExecutableANE\"@\"MPSGraphExecutable\"\"_graphExecutableGPU\"@\"MPSGraphExecutable\"\"_input_Tensor\"@\"MPSGraphTensor\"\"_output_Tensor\"@\"MPSGraphTensor\"\"desc\"{BRNetDescriptor=\"version\"i\"image_width\"I\"image_height\"I\"input_width\"I\"input_height\"I\"input_channels\"I\"input_unshuffle_ratio\"I\"unshuffle_width\"I\"unshuffle_height\"I\"unshuffle_channels\"I\"output_shuffle_ratio\"I\"output_width\"I\"output_height\"I\"output_channels\"I\"up_channels\"I\"layers_channels\"[4I]}\"_prewarm_group\"@\"NSObject<OS_dispatch_group>\"\"_prewarmComplete\"B}"

```
