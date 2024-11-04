## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-587.60.6.0.0
-  __TEXT.__text: 0x292514
-  __TEXT.__auth_stubs: 0xec0
+587.60.10.122.3
+  __TEXT.__text: 0x29306c
+  __TEXT.__auth_stubs: 0xee0
   __TEXT.__objc_methlist: 0xe748
   __TEXT.__const: 0x1026b8
-  __TEXT.__cstring: 0x5b8bf
-  __TEXT.__gcc_except_tab: 0x1f64
-  __TEXT.__oslogstring: 0x49040
+  __TEXT.__cstring: 0x5b9d3
+  __TEXT.__gcc_except_tab: 0x1f80
+  __TEXT.__oslogstring: 0x4913e
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x2d08
+  __TEXT.__unwind_info: 0x2c78
   __TEXT.__objc_classname: 0x2d5f
-  __TEXT.__objc_methname: 0x30126
-  __TEXT.__objc_methtype: 0x15492
+  __TEXT.__objc_methname: 0x30185
+  __TEXT.__objc_methtype: 0x155a9
   __TEXT.__objc_stubs: 0x14660
   __DATA_CONST.__got: 0xad8
   __DATA_CONST.__const: 0x1268

   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x988
   __DATA_CONST.__objc_arraydata: 0xd28
-  __AUTH_CONST.__auth_got: 0x770
+  __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x12000
+  __AUTH_CONST.__cfstring: 0x12080
   __AUTH_CONST.__objc_const: 0x33990
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x9d8
-  __AUTH_CONST.__objc_intobj: 0xa38
+  __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_dictobj: 0x528
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x910
+  __AUTH.__objc_data: 0x8c0
   __DATA.__objc_ivar: 0x32c8
   __DATA.__data: 0xb30
   __DATA.__common: 0x30
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x74e0
-  __DATA_DIRTY.__bss: 0x128
-  __DATA_DIRTY.__common: 0x134
+  __DATA.__bss: 0x4
+  __DATA_DIRTY.__objc_data: 0x7530
+  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__common: 0x130
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4961
-  Symbols:   5537
-  CStrings:  20953
+  Symbols:   5539
+  CStrings:  20963
 
Symbols:
+ _CMILSCOISAdaptation_extrapAndCropCICWithOISOffset
+ _CMILSCOISAdaptation_extrapAndCropLSCLumaOnlyWithOISOffset
CStrings:
+ "-[H13FastBayerProcStage(FlareDetection) runFlareDetectionWithConfig:inputTex:flareDetectionConfig:lscMetadata:outputMetadata:]"
+ "-[H13FastBayerProcStage(Huemap) dispatchHuemapMotionCompensationWithSifr:ev0:outputTexture:config:args:lscMetadata:]"
+ "-[H13FastBayerProcStage(Huemap) dispatchHuemapWithInputTexture:outputTexture:config:args:lscMetadata:]"
+ "-[H13FastBayerProcStage(Huemap) runHuemapGenerationWithInputTexture:outputTexture:lscConfig:args:awbComputedGains:lscMetadata:applyLscToThumbnailsIfNecessary:]"
+ "-[H13FastBayerProcStage(Huemap) runHuemapMotionCompensationWithSifrTexture:ev0ThumbnailTexture:outputTexture:args:lscMetadata:]"
+ "-[H13FastRawScaleConfig(HOCL) getHOCLConfigForInputFrame:forInputFrame:metalCtx:softISPModuleConfig:lscMetadata:bounds:isQuadra:]"
+ "<<<< SoftISP >>>> %!s(MISSING): CIC table OIS Adaptation Version 2"
+ "<<<< SoftISP >>>> %!s(MISSING): LSC table OIS Adaptation Version 2"
+ "<<<< SoftISP >>>> %!s(MISSING): OIS shift = (%!f(MISSING), %!f(MISSING))"
+ "<<<< SoftISP >>>> %!s(MISSING): Warning: withoutChannelImbalanceCorrection is missing; using default value"
+ "ApplyLscInHuemap"
+ "Missing HR parameter"
+ "OISAdaptation"
+ "OISAdaptationMethod"
+ "SingleImageParametersForStereoPhotoLearnedNR"
+ "SingleImageParametersForStereoPhotoQuadraLearnedNR"
+ "Warning: Missing SoftISPTuning is missing; using default value"
+ "dispatchHuemapMotionCompensationWithSifr:ev0:outputTexture:config:args:lscMetadata:"
+ "dispatchHuemapWithInputTexture:outputTexture:config:args:lscMetadata:"
+ "getHOCLConfigForInputFrame:forInputFrame:metalCtx:softISPModuleConfig:lscMetadata:bounds:isQuadra:"
+ "i32@0:8@16^{HuemapMotionCompensationConfig=ffffBBBBSfSfffffS}24"
+ "i40@0:8@16^{HuemapConfig=ffffBBBBS}24^{GOCConfig=BIB}32"
+ "i56@0:8@16@24^@32@40^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}48"
+ "i56@0:8@16@24^{FlareDetectionConfig=SSffSfIBB}32^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}40@48"
+ "i56@0:8@16@24^{HuemapConfig=ffffBBBBS}32@40^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}48"
+ "i64@0:8@16@24@32^{HuemapMotionCompensationConfig=ffffBBBBSfSfffffS}40@48^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}56"
+ "i64@0:8@16^{FlareDetectionConfig=SSffSfIBB}24^{FlareCorrectionConfig={HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}{HOCLBinConfig=BSS}}32@40^{HOCLBinConfig=BSS}48@56"
+ "i76@0:8@16^@24^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}32@4048^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}64B72"
+ "runFlareDetectionWithConfig:inputTex:flareDetectionConfig:lscMetadata:outputMetadata:"
+ "runHuemapGenerationWithInputTexture:outputTexture:lscConfig:args:awbComputedGains:lscMetadata:applyLscToThumbnailsIfNecessary:"
+ "runHuemapMotionCompensationWithSifrTexture:ev0ThumbnailTexture:outputTexture:args:lscMetadata:"
+ "withoutChannelImbalanceCorrection"
- "-[H13FastBayerProcStage(FlareDetection) runFlareDetectionWithConfig:inputTex:flareDetectionConfig:outputMetadata:]"
- "-[H13FastBayerProcStage(Huemap) dispatchHuemapMotionCompensationWithSifr:ev0:outputTexture:config:args:]"
- "-[H13FastBayerProcStage(Huemap) dispatchHuemapWithInputTexture:outputTexture:config:args:]"
- "-[H13FastBayerProcStage(Huemap) runHuemapGenerationWithInputTexture:outputTexture:lscConfig:args:awbComputedGains:]"
- "-[H13FastBayerProcStage(Huemap) runHuemapMotionCompensationWithSifrTexture:ev0ThumbnailTexture:outputTexture:args:]"
- "-[H13FastRawScaleConfig(HOCL) getHOCLConfigForInputFrame:forInputFrame:metalCtx:hoclModuleConfig:lscMetadata:bounds:isQuadra:]"
- "SingleImageParametersForSambaLearnedNR"
- "SingleImageParametersForSambaQuadraLearnedNR"
- "dispatchHuemapMotionCompensationWithSifr:ev0:outputTexture:config:args:"
- "dispatchHuemapWithInputTexture:outputTexture:config:args:"
- "getHOCLConfigForInputFrame:forInputFrame:metalCtx:hoclModuleConfig:lscMetadata:bounds:isQuadra:"
- "i32@0:8@16^{HuemapMotionCompensationConfig=ffffBBBSfSfffffS}24"
- "i40@0:8@16^{HuemapConfig=ffffBBBS}24^{GOCConfig=BIB}32"
- "i48@0:8@16@24^@32@40"
- "i48@0:8@16@24^{FlareDetectionConfig=SSffSfIB}32@40"
- "i48@0:8@16@24^{HuemapConfig=ffffBBBS}32@40"
- "i56@0:8@16@24@32^{HuemapMotionCompensationConfig=ffffBBBSfSfffffS}40@48"
- "i64@0:8@16^@24^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}32@4048"
- "i64@0:8@16^{FlareDetectionConfig=SSffSfIB}24^{FlareCorrectionConfig={HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}{HOCLBinConfig=BSS}}32@40^{HOCLBinConfig=BSS}48@56"
- "runFlareDetectionWithConfig:inputTex:flareDetectionConfig:outputMetadata:"
- "runHuemapGenerationWithInputTexture:outputTexture:lscConfig:args:awbComputedGains:"
- "runHuemapMotionCompensationWithSifrTexture:ev0ThumbnailTexture:outputTexture:args:"

```
