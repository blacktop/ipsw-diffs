## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`

```diff

-1.53.0.0.0
-  __TEXT.__text: 0x896c
+1.55.0.0.0
+  __TEXT.__text: 0x95fc
   __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x2dc
-  __TEXT.__const: 0x3084
-  __TEXT.__cstring: 0x380
-  __TEXT.__oslogstring: 0x27d
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__const: 0x2fb4
+  __TEXT.__cstring: 0x444
+  __TEXT.__oslogstring: 0x2bd
+  __TEXT.__unwind_info: 0x168
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x7ea
-  __TEXT.__objc_methtype: 0x23fe
+  __TEXT.__objc_methname: 0x801
+  __TEXT.__objc_methtype: 0x2422
   __TEXT.__objc_stubs: 0x4e0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x228

   __AUTH_CONST.__auth_got: 0x158
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x630
-  __DATA.__objc_ivar: 0x84
-  __DATA.__data: 0x1ca1c
+  __AUTH_CONST.__objc_const: 0x650
+  __DATA.__objc_ivar: 0x88
+  __DATA.__data: 0x1cb34
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FCE47F7F-10D0-3D90-B206-3B2E92901F1A
-  Functions: 118
-  Symbols:   773
-  CStrings:  184
+  UUID: 72683AEB-04B0-3FCF-8E61-65FB8887C42F
+  Functions: 122
+  Symbols:   782
+  CStrings:  199
 
Symbols:
+ OBJC_IVAR_$_ASEProcessingT0._prev_temporal_context
+ _disableOvershootFix
+ _dumpAllConfigs
+ _enableConfigDump
+ _enableTemporalControl
+ _getFGLevel
+ _getFGLevelLength
+ _initDefaultConfigs
+ _lumaBlend_SettingVideo_Heavy_FG_V2_PQ
+ _lumaBlend_SettingVideo_NFG_V2_PQ
+ _lumaBlend_SettingVideo_level1_FG_V2_PQ
+ _lumaBlend_SettingVideo_level2_FG_V2_PQ
+ _lumaBlend_SettingVideo_level3_FG_V2_PQ
+ _lumaBlend_SettingVideo_light_FG_V2_PQ
+ _minFGChangeStepsPerLevel
+ _minFramesPerLevel
- _disableSampleShift
- _hideHcu
- _overrideChipID
- _overrideEnhancement
- _overrideFGLevel
- _overrideInputTransferFunction
- _overrideInputType
CStrings:
+ " [1.55.0] \n"
+ " [1.55.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
+ " [1.55.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
+ " [1.55.0]  %30s: %-12d\n"
+ " [1.55.0] %s : bad argument, retVal=%ld, input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
+ " [1.55.0] %s : config=%p"
+ " [1.55.0] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
+ " [1.55.0] %s : instance=%p, productType=%u, destinationWidth=%d, destinationHeight=%d, inputType=%s"
+ " [1.55.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
+ " [1.55.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
+ " [1.55.0] %s: Frame #%llu:\n"
+ " [1.55.0] ++ %s: ASEApiVer=%d\n"
+ "_prev_temporal_context"
+ "disableHcuCache"
+ "disableOvershootFix"
+ "dumpOutputHcu"
+ "enableConfigDump"
+ "enableTemporalControl"
+ "logLevel"
+ "minFGChangeStepsPerLevel"
+ "minFramesPerLevel"
+ "readDefaultsWriteEnabled"
+ "void dumpAllConfigs(uint64_t)"
+ "{?=\"FG_value\"i\"FG_level_count\"[5i]}"
- " [1.53.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
- " [1.53.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
- " [1.53.0] %s : bad argument, retVal=%ld, input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
- " [1.53.0] %s : config=%p"
- " [1.53.0] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
- " [1.53.0] %s : instance=%p, productType=%u, destinationWidth=%d, destinationHeight=%d, inputType=%s"
- " [1.53.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
- " [1.53.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
- " [1.53.0] ++ %s: ASEApiVer=%d\n"

```
