## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-664.40.10.122.3
-  __TEXT.__text: 0x5bc34
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_stubs: 0x31e0
-  __TEXT.__objc_methlist: 0x1b34
+664.40.15.122.3
+  __TEXT.__text: 0x5c3d0
+  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__objc_stubs: 0x3220
+  __TEXT.__objc_methlist: 0x1b94
   __TEXT.__const: 0x6f0
-  __TEXT.__objc_methname: 0x5996
+  __TEXT.__objc_methname: 0x5b3e
   __TEXT.__objc_classname: 0x226
   __TEXT.__objc_methtype: 0x17ea
-  __TEXT.__cstring: 0x926e
-  __TEXT.__oslogstring: 0xdb2d
+  __TEXT.__cstring: 0x92e4
+  __TEXT.__oslogstring: 0xdf42
   __TEXT.__gcc_except_tab: 0x3cc
-  __TEXT.__unwind_info: 0x820
-  __DATA_CONST.__auth_got: 0x6a8
-  __DATA_CONST.__got: 0x868
+  __TEXT.__unwind_info: 0x828
+  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__got: 0x878
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__cfstring: 0x9e0

   __DATA_CONST.__objc_arraydata: 0x2760
   __DATA_CONST.__objc_dictobj: 0x988
   __DATA_CONST.__objc_arrayobj: 0x1680
-  __DATA.__objc_const: 0x43e0
-  __DATA.__objc_selrefs: 0xf98
-  __DATA.__objc_ivar: 0x498
+  __DATA.__objc_const: 0x4480
+  __DATA.__objc_selrefs: 0xfb8
+  __DATA.__objc_ivar: 0x4a0
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x300
   __DATA.__common: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE16F898-6FC4-3367-A963-8D20FE1794D0
-  Functions: 1253
-  Symbols:   2704
-  CStrings:  2845
+  UUID: A31F11BA-04BE-3079-9BFB-8649DB7474D9
+  Functions: 1258
+  Symbols:   2716
+  CStrings:  2861
 
Symbols:
+ -[VISConfigurationV2 faceStabilizationSigmaModulationExponent]
+ -[VISConfigurationV2 faceStabilizationSigmaModulationSmoothTransitionMultiplier]
+ -[VISConfigurationV2 setFaceStabilizationSigmaModulationExponent:]
+ -[VISConfigurationV2 setFaceStabilizationSigmaModulationSmoothTransitionMultiplier:]
+ OBJC_IVAR_$_VISConfigurationV2._faceStabilizationSigmaModulationExponent
+ OBJC_IVAR_$_VISConfigurationV2._faceStabilizationSigmaModulationSmoothTransitionMultiplier
+ _kFigVideoStabilizationSampleBufferProcessorOption_FaceStabilizationSigmaModulationExponent
+ _kFigVideoStabilizationSampleBufferProcessorOption_FaceStabilizationSigmaModulationSmoothTransitionMultiplier
+ _objc_msgSend$faceStabilizationSigmaModulationExponent
+ _objc_msgSend$faceStabilizationSigmaModulationSmoothTransitionMultiplier
+ _objc_retain_x28
+ sbp_gvs_work_cinematic.cold.14
CStrings:
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Configuration: face stabilization sigmaModulationExponent = %f. sigmaModulationSmoothTransitionMultiplier = %f"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Invalid/missing face stabilization tuning parameters: sigmaModulationExponent = %f, sigmaModulationSmoothTransitionMultiplier = %f, default tunings for video are used ( 1.75, 0.4 )"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Invalid/missing face stabilization tuning parameters: sigmaMultiplierForFaceFiltering = %f, sigmaMultiplierForBiasTracking = %f, default tunings for video are used ( 0.8, 1.0 )"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Options: Face stabilization enabled: %d. Sigma multiplier for face filtering read from plist = %f. Sigma multiplier for bias tracking read from plist = %f"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: [_smoothPowerMap] parameter exponent is %f, it cannot be less than 1.f, clamping it to 1.f\n"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: [_smoothPowerMap] parameter outputMin %f cannot be greater than outputMax %f, clamping it to outputMax\n"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: _initializeFaceFilteringAndBiasTrackingModulationParameters failed"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: sigmaMultiplierForFaceFiltering %f cannot be greater than sigmaMultiplierForBiasTracking %f: sigmaMultiplierForFaceFiltering will be clamped to sigmaMultiplierForBiasTracking"
+ "Tf,N,V_faceStabilizationSigmaModulationExponent"
+ "Tf,N,V_faceStabilizationSigmaModulationSmoothTransitionMultiplier"
+ "_faceStabilizationSigmaModulationExponent"
+ "_faceStabilizationSigmaModulationSmoothTransitionMultiplier"
+ "_smoothPowerMap"
+ "faceStabilizationContext->sigmaModulationInputMin < faceStabilizationContext->sigmaModulationInputMax"
+ "faceStabilizationSigmaModulationExponent"
+ "faceStabilizationSigmaModulationSmoothTransitionMultiplier"
+ "setFaceStabilizationSigmaModulationExponent:"
+ "setFaceStabilizationSigmaModulationSmoothTransitionMultiplier:"
- "<<<< GyroVideoStabilizationV2 >>>> %s: Invalid/missing face stabilization tuning parameters: sigmaMultiplierForFaceFiltering = %f, sigmaMultiplierForBiasTracking = %f"
- "<<<< GyroVideoStabilizationV2 >>>> %s: Options: Face stabilization enabled: %d. Sigma multiplier for face filtering = %f. Sigma multiplier for bias tracking = %f"

```
