## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-1672.100.48.0.0
-  __TEXT.__text: 0x1a7760
+1672.120.23.0.0
+  __TEXT.__text: 0x1aeddc
   __TEXT.__auth_stubs: 0x1500
-  __TEXT.__objc_methlist: 0x6edc
-  __TEXT.__cstring: 0x9e9b
-  __TEXT.__const: 0xefa8
-  __TEXT.__oslogstring: 0x1267f
-  __TEXT.__gcc_except_tab: 0x1c14
+  __TEXT.__objc_methlist: 0x70b4
+  __TEXT.__cstring: 0xa077
+  __TEXT.__const: 0xf558
+  __TEXT.__oslogstring: 0x12f6c
+  __TEXT.__gcc_except_tab: 0x1c60
   __TEXT.__dlopen_cstrs: 0x1d5
-  __TEXT.__unwind_info: 0x2ec4
+  __TEXT.__unwind_info: 0x2fb0
   __TEXT.__eh_frame: 0xb0
-  __TEXT.__objc_classname: 0xa03
-  __TEXT.__objc_methname: 0x104f6
-  __TEXT.__objc_methtype: 0x3db9
-  __TEXT.__objc_stubs: 0xc660
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x2028
-  __DATA_CONST.__objc_classlist: 0x3e0
+  __TEXT.__objc_classname: 0xa1f
+  __TEXT.__objc_methname: 0x109fa
+  __TEXT.__objc_methtype: 0x3e63
+  __TEXT.__objc_stubs: 0xc960
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x20b8
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x161f8
-  __DATA_CONST.__objc_selrefs: 0x3a48
+  __DATA_CONST.__objc_const: 0x16be8
+  __DATA_CONST.__objc_selrefs: 0x3b08
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_classrefs: 0x4e8
-  __DATA_CONST.__objc_superrefs: 0x3b8
+  __DATA_CONST.__objc_classrefs: 0x4f8
+  __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x468
-  __AUTH_CONST.__objc_const: 0x510
-  __AUTH_CONST.__cfstring: 0xb260
+  __AUTH_CONST.__objc_const: 0x318
+  __AUTH_CONST.__cfstring: 0xb460
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH_CONST.__const: 0x3c8
   __AUTH_CONST.__objc_floatobj: 0x30
+  __AUTH_CONST.__const: 0x3c8
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__auth_got: 0xa98
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x1030
-  __DATA.__data: 0x26d88
-  __DATA.__bss: 0x270
-  __DATA_DIRTY.__const: 0x458
-  __DATA_DIRTY.__objc_const: 0x2710
-  __DATA_DIRTY.__objc_data: 0x2440
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x10a0
+  __DATA.__data: 0x27048
+  __DATA.__bss: 0x1f0
+  __DATA_DIRTY.__const: 0x478
+  __DATA_DIRTY.__objc_const: 0x2950
+  __DATA_DIRTY.__objc_data: 0x24e0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x130
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4636
-  Symbols:   14456
-  CStrings:  7258
+  Functions: 4687
+  Symbols:   14638
+  CStrings:  7377
 
Symbols:
+ -[AABRear started]
+ -[CBBrightnessProxyCA brightnessNotificationSecureIndicatorOff]
+ -[CBBrightnessProxyCA brightnessNotificationSecureIndicatorOn]
+ -[CBBrightnessProxyCA brightnessSecureIndicatorActiveCount]
+ -[CBBrightnessProxyCA brightnessSecureIndicatorType]
+ -[CBBrightnessProxyCA setIndicatorBrightness:]
+ -[CBIndicatorBrightnessModule addHIDServiceClient:]
+ -[CBIndicatorBrightnessModule copyPropertyForKey:]
+ -[CBIndicatorBrightnessModule copyPropertyForKey:withParameter:]
+ -[CBIndicatorBrightnessModule currentIndicatorBrightness]
+ -[CBIndicatorBrightnessModule currentSilState]
+ -[CBIndicatorBrightnessModule dealloc]
+ -[CBIndicatorBrightnessModule endRamp]
+ -[CBIndicatorBrightnessModule forceBrightnessTransaction]
+ -[CBIndicatorBrightnessModule handleHIDEvent:from:]
+ -[CBIndicatorBrightnessModule handleNotificationForKey:withProperty:]
+ -[CBIndicatorBrightnessModule initWithQueue:min:andMax:]
+ -[CBIndicatorBrightnessModule initWithQueue:min:max:andCurrentTimeFunction:]
+ -[CBIndicatorBrightnessModule isRampRunning]
+ -[CBIndicatorBrightnessModule isSecureIndicatorLightEnabled]
+ -[CBIndicatorBrightnessModule processTransaction]
+ -[CBIndicatorBrightnessModule rampTo:]
+ -[CBIndicatorBrightnessModule removeHIDServiceClient:]
+ -[CBIndicatorBrightnessModule setMinimumIndicatorBrightness:]
+ -[CBIndicatorBrightnessModule setProperty:forKey:]
+ -[CBIndicatorBrightnessModule setRampSpeed:]
+ -[CBIndicatorBrightnessModule setSdrBrightness:]
+ -[CBIndicatorBrightnessModule setSilEnabled:]
+ -[CBIndicatorBrightnessModule shouldPushIndicatorBrightness]
+ -[CBIndicatorBrightnessModule shouldRampToMib]
+ -[CBIndicatorBrightnessModule start]
+ -[CBIndicatorBrightnessModule stop]
+ -[CBIndicatorBrightnessModule updateRamp]
+ -[CBRearALSModule AABSensorOverridePropertyHandler:]
+ -[CBRearALSModule displayBrightnessFactorPropertyHandler:]
+ -[CBRearALSModule rLuxOverridePropertyHandler:]
+ -[KeyboardBacklight hysteresisOn]
+ -[KeyboardBacklight setHysteresisOn:]
+ GCC_except_table114
+ GCC_except_table123
+ GCC_except_table168
+ GCC_except_table175
+ GCC_except_table180
+ GCC_except_table184
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table308
+ GCC_except_table326
+ GCC_except_table68
+ _CBU_IsSecureIndicatorSupported
+ _CBU_IsSecureIndicatorSupported.onceToken
+ _CBU_IsSecureIndicatorSupported.supported
+ _DisplayGetCurrentRTPLCHeadroomCap
+ _DisplayStartRTPLCEDRCapRamp
+ _OBJC_CLASS_$_CBIndicatorBrightnessModule
+ _OBJC_IVAR_$_CBBrightnessProxyCA._brightnessNotificationSecureIndicatorOff
+ _OBJC_IVAR_$_CBBrightnessProxyCA._brightnessNotificationSecureIndicatorOn
+ _OBJC_IVAR_$_CBBrightnessProxyCA._brightnessSecureIndicatorActiveCount
+ _OBJC_IVAR_$_CBBrightnessProxyCA._brightnessSecureIndicatorType
+ _OBJC_IVAR_$_CBDisplayModuleiOS._brightnessIsUnderAutoDimThresholdCurrentValue
+ _OBJC_IVAR_$_CBDisplayModuleiOS._indicatorBrightnessModule
+ _OBJC_IVAR_$_CBDisplayModuleiOS._mibCurve
+ _OBJC_IVAR_$_CBDisplayRamps._minimumIndicatorRamp
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._currentIndicatorBrightness
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._currentTimeFunction
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._enforceMIB
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._forcedBrightnessUpdate
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._logHandle
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._maxSdr
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._mib
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._mibServices
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._minSdr
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._nextUpdate
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._notificationBlock
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._ramp
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._rampSpeed
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._sdrBrightness
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._silState
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._targetIndicatorBrightness
+ _OBJC_IVAR_$_CBRearALSModule._displayOn
+ _OBJC_IVAR_$_CBRearALSModule._enableIlluminanceOverride
+ _OBJC_IVAR_$_CBRearALSModule._illuminanceOverride
+ _OBJC_IVAR_$_CBRearALSModule._lastLux
+ _OBJC_IVAR_$_KeyboardBacklight._hysteresisOn
+ _OBJC_METACLASS_$_CBIndicatorBrightnessModule
+ __DisplaySetAdaptiveDimmingLimitWithFade
+ __OBJC_$_INSTANCE_METHODS_CBIndicatorBrightnessModule
+ __OBJC_$_INSTANCE_VARIABLES_CBIndicatorBrightnessModule
+ __OBJC_$_PROP_LIST_CBIndicatorBrightnessModule
+ __OBJC_CLASS_PROTOCOLS_$_CBIndicatorBrightnessModule
+ __OBJC_CLASS_RO_$_CBIndicatorBrightnessModule
+ __OBJC_METACLASS_RO_$_CBIndicatorBrightnessModule
+ __ZN14CoreBrightnessL11sbimLimits5E
+ ___25-[CBSBIM startMonitoring]_block_invoke.31
+ ___45-[CBIndicatorBrightnessModule setSilEnabled:]_block_invoke
+ ___52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.271
+ ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke_3
+ ___CBU_IsSecureIndicatorSupported_block_invoke
+ ___DisplayCPMSHDRCallbackDCPStage1
+ ___DisplayCPMSHDRCallbackDCPStage2
+ ___DisplayEvaluateCPMSHDRPowerConstraint
+ ___DisplayGetCurrentRTPLCHeadroomCap_block_invoke
+ ___DisplaySetProperty_block_invoke.452
+ ___DisplaySetProperty_block_invoke.583
+ ___DisplaySetState_block_invoke.370
+ ___DisplayStartRTPLCEDRCapRamp_block_invoke
+ ____DisplaySetBrightnessFactor_block_invoke.741
+ ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.770
+ ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.783
+ _____DisplayCPMSHDRCallbackDCPStage1_block_invoke
+ _____DisplayCPMSHDRCallbackDCPStage1_block_invoke_2
+ _____DisplayUpdateSlider_block_invoke.1113
+ _____DisplayUpdateSlider_block_invoke.1115
+ ___block_descriptor_33_e15_v32?08Q16^B24l
+ ___block_descriptor_56_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_64_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_descriptor_tmp.26
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.50
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.77
+ ___block_literal_global.1055
+ ___block_literal_global.205
+ ___block_literal_global.28
+ ___block_literal_global.33
+ ___block_literal_global.52
+ ___block_literal_global.59
+ ___block_literal_global.70
+ ___block_literal_global.72
+ ___block_literal_global.79
+ ___os_log_helper_16_2_21_8_0_8_0_8_0_8_32_8_0_8_0_8_0_8_0_8_0_8_0_8_32_8_0_8_32_8_0_8_32_8_0_8_0_8_0_8_0_8_0_8_0
+ ___os_log_helper_16_2_8_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_32
+ ___os_log_helper_16_2_8_8_0_8_0_8_0_8_0_8_0_8_0_8_32_8_0
+ _kCABrightnessNotificationSecureIndicatorActiveCount
+ _kCABrightnessNotificationSecureIndicatorOff
+ _kCABrightnessNotificationSecureIndicatorOn
+ _kCABrightnessNotificationSecureIndicatorType
+ _objc_msgSend$AABSensorOverridePropertyHandler:
+ _objc_msgSend$brightnessNotificationSecureIndicatorOff
+ _objc_msgSend$brightnessNotificationSecureIndicatorOn
+ _objc_msgSend$brightnessSecureIndicatorActiveCount
+ _objc_msgSend$currentBrightness
+ _objc_msgSend$currentIndicatorBrightness
+ _objc_msgSend$endRamp
+ _objc_msgSend$forceBrightnessTransaction
+ _objc_msgSend$hysteresisOn
+ _objc_msgSend$initWithQueue:min:andMax:
+ _objc_msgSend$initWithQueue:min:max:andCurrentTimeFunction:
+ _objc_msgSend$initWithStartingBrightness:targetBrightness:rampSpeed:andCurrentTime:
+ _objc_msgSend$isRampRunning
+ _objc_msgSend$isSecureIndicatorLightEnabled
+ _objc_msgSend$processTransaction
+ _objc_msgSend$rLuxOverridePropertyHandler:
+ _objc_msgSend$setHysteresisOn:
+ _objc_msgSend$setIndicatorBrightness:
+ _objc_msgSend$setMinimumIndicatorBrightness:
+ _objc_msgSend$setRampSpeed:
+ _objc_msgSend$setSilEnabled:
+ _objc_msgSend$shouldPushIndicatorBrightness
+ _objc_msgSend$started
+ _objc_msgSend$timeOfLastUpdate
+ _objc_msgSend$updateRampWithTimestamp:
- GCC_except_table122
- GCC_except_table167
- GCC_except_table174
- GCC_except_table179
- GCC_except_table183
- GCC_except_table185
- GCC_except_table188
- GCC_except_table193
- GCC_except_table321
- _DisplayGetCurrentRTPLCHeadroom
- _DisplayStartRTPLCEDRRamp
- _OBJC_IVAR_$_CBDisplayModuleiOS._nitsAtRTPLCRampStart
- __DisplaySetAdaptiveDimmingWithFade
- ___25-[CBSBIM startMonitoring]_block_invoke.23
- ___52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.251
- ___DisplayFadeUpdateAdaptiveFactorFade
- ___DisplayGetCurrentRTPLCHeadroom_block_invoke
- ___DisplaySetProperty_block_invoke.569
- ___DisplaySetState_block_invoke.357
- ___DisplayStartRTPLCEDRRamp_block_invoke
- ____DisplaySetBrightnessFactor_block_invoke.727
- ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.761
- ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.774
- _____DisplayUpdateSlider_block_invoke.1093
- _____DisplayUpdateSlider_block_invoke.1095
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.42
- ___block_descriptor_tmp.49
- ___block_descriptor_tmp.62
- ___block_literal_global.1046
- ___block_literal_global.206
- ___block_literal_global.24
- ___block_literal_global.29
- ___block_literal_global.44
- ___block_literal_global.51
- ___block_literal_global.61
- ___block_literal_global.64
- ___os_log_helper_16_2_20_8_0_8_0_8_0_8_32_8_0_8_0_8_0_8_0_8_0_8_32_8_0_8_32_8_0_8_32_8_0_8_0_8_0_8_0_8_0_8_0
- __unnamed_array_storage.40
- _objc_msgSend$brightnessCap
CStrings:
+ "@\"CBIndicatorBrightnessModule\""
+ "@\"CBStopsBasedBrightnessRamp\""
+ "@32@0:8@16f24f28"
+ "@40@0:8@16f24f28^?32"
+ "AABSensorOverridePropertyHandler:"
+ "ALS with orientation %d has been overriden to %f Lux."
+ "Already at correct brightness %f with ramp not running"
+ "Already running ramp with the same target %f"
+ "AutoDim begin ramp : %0.2f -> %0.2f t: %f"
+ "CBBrightnessIsUnderAutoDimThreshold"
+ "CBIndicatorBrightnessModule"
+ "Can't ramp MIB target %f when SIL is off"
+ "Copy overrided rear ALS Lux = %f"
+ "Copy rear ALS Lux = %f"
+ "Created ramp %f -> %f @ %f"
+ "Disable sensor override for ALS with orientation %d"
+ "Display powering off; reset AutoDim state"
+ "DisplayAsyncCPMS: %p"
+ "DisplayGetPowerAccumulatorDCP"
+ "EDMSupported"
+ "EXBrightSILEnabled"
+ "EmaxThreshold"
+ "Ending ramp"
+ "Enforce MIB: %d"
+ "Exit"
+ "Extended display mitigation supported: %d"
+ "Failed to create frequency NSNumber, display might not ramp"
+ "Failed to create ramp %f -> %f @ %f"
+ "Failed to load ALS fast integration time."
+ "Failed to load ALS orietnation."
+ "Failed to load ALS placement."
+ "Failed to load ALS sensor type."
+ "Failed to load ALS slow integration time."
+ "Failed to load ALS super fast integration time."
+ "Forced brightness transaction"
+ "HDR CAPS | RTPLC: [%s] %f, currentNitCap: %f, dynSliderCap: %f, Nits: %f"
+ "HDR RTPLC ACTION: hdrBrightness = %f, rtplcCap = %f, hdrHeadroom = %f, currentHeadroom = %f, _requestedHeadroom = %f"
+ "HDR RTPLC CAP: \n\tFADE: %f --------> %f, duration: %f, \n\tstart:%f, \n\thStart:%f, \n\ttarget:%f, \n\tdisplay->rtplcEDRFade.fade.Hcurrent: %f\n\trtplcFadeIsRunning: %s"
+ "HDR RTPLC EXIT: _rtplcCap = %f (_maxNitsEDR = %f)"
+ "HDR RTPLC RECOVERY COMPLETE -> EXITING RTPLC: ramp cap: %f --> %f"
+ "HDR RTPLC RECOVERY COMPLETE!!"
+ "HDR RTPLC RECOVERY: hdrBrightness = %f, hdrHeadroom = %f, currentHeadroom = %f, _requestedHeadroom = %f, rtplcCap = %f"
+ "HDR RTPLC RELEASED AND RECOVERY COMPLETE -> EXITING RTPLC: ramp cap: %f --> %f"
+ "Ignoring MIB target (%f) that is different than current sdr"
+ "IndicatorBrightness"
+ "IndicatorBrightness.Nits"
+ "MIB ramp speed can't be 0 seconds/stop, using default ramp speed"
+ "MIB ramp speed overriden to %f seconds/stop"
+ "MinimumIndicatorBrightness"
+ "MinimumIndicatorBrightnessEnforce"
+ "Mitigation is active -> copy last valid rear ALS Lux = %f"
+ "Negative MIB %f, ignoring"
+ "Negative sdr brightness %f, ignoring"
+ "Override rear ALS samples with value = %f %s."
+ "Pushing sdrBrightness: %f, capped _appliedHeadroom: %f, brightnessLimit: %f, potentialHeadroom: %f, Ambient: %f to CA, HDRBrightness: %f, [%s] rtplcCap: %f"
+ "RTPLC ACTION: StartRTPLCRamp, ramp Cap: %f--->%f"
+ "RTPLC EXIT COMPLETE!!"
+ "RTPLC RECOVERY RAMP! ramp Cap: %f ---> %f (currentCapToCA = %f)"
+ "RTPLC RECOVERY: target HDR Brightness= %f for APCE = %f, current RTPLC target: %f, scaleFactor: %f, peakAPCECap: %f"
+ "RTPLC RELEASED!"
+ "RTPLC TRIGGER!! RTPLCBrightness: %f, reducedHeadroom: %f, current(_applied): %f, _nitsSDR: %f, _currentCapToCA = %f"
+ "SDR brightness is higher than current MIB - something is probably off"
+ "SecureIndicatorActiveCount"
+ "SecureIndicatorBrightnessRampSpeed"
+ "SecureIndicatorLightEnabled"
+ "SyncDBV Transaction | ID=%llu SDR.Nits=%.0f HDR.Nits=%.0f HDR.State=%s BrightnessLimit=%f IndicatorBrightness.Nits=%.0f Headroom.Current=%f Headroom.Maximum=%f AppliedCompensations=%f Aurora.Factor=%f Aurora.RampInProgress=%s Lux=%.0f RTPLC.State=%s RTPLC.Cap=%.0f RTPLC.CapApplied=%s PeakAPCE.Cap=%f Nits.Cap=%f DynamicSlider.Cap=%f Twilight.Strength=%f Ammolite.Strength=%f ContrastEnhancer.Strength=%f"
+ "T@\"NSString\",R,V_brightnessSecureIndicatorActiveCount"
+ "T@\"NSString\",R,V_brightnessSecureIndicatorType"
+ "T@,R,V_brightnessNotificationSecureIndicatorOff"
+ "T@,R,V_brightnessNotificationSecureIndicatorOn"
+ "TB,R,V_started"
+ "TB,V_hysteresisOn"
+ "TrustedFrontLux"
+ "TrustedFrontLux from AABC = %f"
+ "Updated ramp %f -> %f @ %f"
+ "WARNING: Ramp was running while forced brightness transaction happened"
+ "[New Event] eventTimestamp=%llu (unknown payload)"
+ "[New Event] eventTimestamp=%llu MIBData.(ts=%fs mib=%f aggregatedLux=%f)\n"
+ "[New Event] unknown event type %u"
+ "[VID=%@] [PID=%@] Update frequency = %d"
+ "_brightnessIsUnderAutoDimThresholdCurrentValue"
+ "_brightnessNotificationSecureIndicatorOff"
+ "_brightnessNotificationSecureIndicatorOn"
+ "_brightnessSecureIndicatorActiveCount"
+ "_brightnessSecureIndicatorType"
+ "_currentIndicatorBrightness"
+ "_currentTimeFunction"
+ "_enableIlluminanceOverride"
+ "_enforceMIB"
+ "_forcedBrightnessUpdate"
+ "_hysteresisOn"
+ "_illuminanceOverride"
+ "_indicatorBrightnessModule"
+ "_maxSdr"
+ "_mib"
+ "_mibCurve"
+ "_mibServices"
+ "_minSdr"
+ "_minimumIndicatorRamp"
+ "_nextUpdate"
+ "_silState"
+ "_targetIndicatorBrightness"
+ "aab-constraint-emax-threshold"
+ "brightnessNotificationSecureIndicatorOff"
+ "brightnessNotificationSecureIndicatorOn"
+ "brightnessSecureIndicatorActiveCount"
+ "brightnessSecureIndicatorType"
+ "com.apple.CoreBrightness.CBIndicatorBrightnessModule"
+ "cpms-hdr-cap-multiplier"
+ "cpms-hdr-reset-duration"
+ "currentIndicatorBrightness"
+ "currentSilState"
+ "endRamp"
+ "enforce_mib"
+ "forceBrightnessTransaction"
+ "hysteresisOn"
+ "initWithQueue:min:andMax:"
+ "initWithQueue:min:max:andCurrentTimeFunction:"
+ "isRampRunning"
+ "isSecureIndicatorLightEnabled"
+ "power accumulator = %llu"
+ "processTransaction"
+ "rLuxOverridePropertyHandler:"
+ "setHysteresisOn:"
+ "setIndicatorBrightness:"
+ "setMinimumIndicatorBrightness:"
+ "setRampSpeed:"
+ "setSilEnabled:"
+ "shouldPushIndicatorBrightness"
+ "shouldRampToMib"
+ "started"
+ "supports-edm"
+ "trusted Lux: %f, trusted front Lux: %f, trusted capped Lux: %f"
+ "updateRamp called, isRampRunning: %s, silState: %lu, currentSDR: %f, currentMIB: %f, targetMIB: %f, MIB: %f"
+ "updateRamp finished, isRampRunning: %s, silState: %lu, currentSDR: %f, currentMIB: %f, targetMIB: %f, MIB: %f"
+ "{?=\"sdrBrightness\"f\"minimumIndicatorBrightness\"f\"silEnabled\"B\"dirty\"B}"
- "CBPLC : StartCBPLCRamp, startingHeadroom: %f--->%f"
- "CBPLC RECOVERY RAMP! targetHeadroom: %f"
- "CBPLC RECOVERY: target HDR Brightness= %f for APCE = %f, current CBPLC target: %f, scaleFactor: %f"
- "CBPLC RELEASED!"
- "CBPLC TRIGGER!! CBPLCBrightness: %f, reducedHeadroom: %f, current(_applied): %f, _nitsSDR: %f"
- "Copy rear ALS Lux = %@"
- "HDR CAPS | CBPLC: %f, PeakAPCE: %f, currentNitCap: %f, dynSliderCap: %f"
- "HDR CBPLC : \n\tstart:%f, \n\thStart:%f, \n\ttarget:%f, \n\tdisplay->rtplcEDRFade.fade.Hcurrent: %f\n\trtplcFadeIsRunning: %s"
- "HDR CBPLC FADE: %f --------> %f, duration: %f"
- "HDR CBPLC RECOVERY COMPLETE!!"
- "HDR CBPLC RELEASED AND RECOVERY COMPLETE!!"
- "HDR CBPLC | cbplcHeadroom: %f, _nitsAtCBPLCRampStart: %f"
- "Pushing sdrBrightness: %f, capped _appliedHeadroom: %f, brightnessLimit: %f, potentialHeadroom: %f, Ambient: %f to CA, HDRBrightness: %f"
- "SyncDBV Transaction | ID=%llu SDR.Nits=%.0f HDR.Nits=%.0f HDR.State=%s BrightnessLimit=%f Headroom.Current=%f Headroom.Maximum=%f AppliedCompensations=%f Aurora.Factor=%f Aurora.RampInProgress=%s Lux=%.0f RTPLC.State=%s RTPLC.Cap=%.0f RTPLC.CapApplied=%s PeakAPCE.Cap=%f Nits.Cap=%f DynamicSlider.Cap=%f Twilight.Strength=%f Ammolite.Strength=%f ContrastEnhancer.Strength=%f"
- "TrustedLux from AABC = %f"
- "[VID=%@] Update frequency = %d"
- "_nitsAtRTPLCRampStart"

```
