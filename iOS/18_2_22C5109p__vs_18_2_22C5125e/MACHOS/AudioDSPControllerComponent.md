## AudioDSPControllerComponent

> `/System/ExclaveKit/System/Library/PrivateFrameworks/AudioDSPControllerComponent.framework/AudioDSPControllerComponent`

```diff

-139.324.0.0.0
-  __TEXT.__text: 0x88f4
-  __TEXT.__auth_stubs: 0x310
+139.327.0.0.0
+  __TEXT.__text: 0xa1f8
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__const: 0x1a0
-  __TEXT.__oslogstring: 0x74b
-  __TEXT.__gcc_except_tab: 0x1e0
-  __TEXT.__cstring: 0x1fe9
-  __TEXT.__unwind_info: 0x2c0
-  __DATA.__auth_got: 0x190
+  __TEXT.__oslogstring: 0x863
+  __TEXT.__gcc_except_tab: 0x3bc
+  __TEXT.__cstring: 0x1c86
+  __TEXT.__unwind_info: 0x348
+  __DATA.__auth_got: 0x1a0
   __DATA.__got: 0x38
-  __DATA.__const: 0x838
+  __DATA.__const: 0x858
   __DATA.__data: 0xf8
   __DATA.__TIGHTBEAM: 0x10
   __DATA.__bss: 0x10

   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libc++.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
-  Functions: 248
-  Symbols:   425
-  CStrings:  116
+  Functions: 249
+  Symbols:   439
+  CStrings:  125
 
Symbols:
+ GCC_except_table10
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table7
+ GCC_except_table9
+ __ZN3adm35ScopedSignpostControllerEKIOStoppedD2Ev
+ __ZN3adm36ScopedSignpostControllerEKIOStartingD2Ev
+ __ZN3adm37ScopedSignpostControllerEKUnconfigureD2Ev
+ __ZN3adm38ScopedSignpostControllerEKPrepareForIOD2Ev
+ __ZN3adm41ScopedSignpostControllerEKTBCallIOStoppedD2Ev
+ __ZN3adm42ScopedSignpostControllerEKTBCallIOStartingD2Ev
+ __ZN3adm43ScopedSignpostControllerEKTBCallUnconfigureD2Ev
+ __ZN3adm44ScopedSignpostControllerEKTBCallPrepareForIOD2Ev
+ __block_descriptor_tmp.28
+ __block_descriptor_tmp.50
+ __block_descriptor_tmp.61
+ __block_descriptor_tmp.67
+ __block_descriptor_tmp.73
+ __block_descriptor_tmp.80
+ __block_descriptor_tmp.88
+ __block_descriptor_tmp.97
+ __decodeAudioDSPController2_block_invoke.57
+ __decodeAudioDSPController2_block_invoke.57.cold.1
+ __decodeAudioDSPController2_block_invoke.64
+ __decodeAudioDSPController2_block_invoke.70
+ __decodeAudioDSPController2_block_invoke.76
+ __decodeAudioDSPController2_block_invoke.76.cold.1
+ __decodeAudioDSPController2_block_invoke.84
+ __decodeAudioDSPController2_block_invoke.84.cold.1
+ __decodeAudioDSPController2_block_invoke.93
+ __decodeAudioDSPController2_block_invoke.93.cold.1
+ __os_signpost_emit_with_name_impl
+ _audiodsptypes_streamdescription__encode
+ _os_signpost_enabled
- GCC_except_table40
- GCC_except_table41
- __block_descriptor_tmp.45
- __block_descriptor_tmp.56
- __block_descriptor_tmp.62
- __block_descriptor_tmp.68
- __block_descriptor_tmp.75
- __block_descriptor_tmp.83
- __block_descriptor_tmp.91
- __decodeAudioDSPController2_block_invoke.52
- __decodeAudioDSPController2_block_invoke.52.cold.1
- __decodeAudioDSPController2_block_invoke.59
- __decodeAudioDSPController2_block_invoke.65
- __decodeAudioDSPController2_block_invoke.71
- __decodeAudioDSPController2_block_invoke.71.cold.1
- __decodeAudioDSPController2_block_invoke.79
- __decodeAudioDSPController2_block_invoke.79.cold.1
- __decodeAudioDSPController2_block_invoke.87
- __decodeAudioDSPController2_block_invoke.87.cold.1
- audiodspprocessor_audiodsp_getparameter.cold.1
- audiodspprocessor_audiodsp_getparameter.cold.2
- audiodspprocessor_audiodsp_performio.cold.1
- audiodspprocessor_audiodsp_prepareforio.cold.1
- audiodspprocessor_audiodsp_setparameter.cold.1
- audiodspprocessor_audiodsp_unconfigure.cold.1
- audiodsputility_parametervalue__decode.cold.1
- initAudioDSPControllerComponentAudioDSPControllerInit.cold.1
CStrings:
+ "%!s(MISSING)"
+ "ADM::ControllerEK::IOStarting"
+ "ADM::ControllerEK::IOStopped"
+ "ADM::ControllerEK::PrepareForIO"
+ "ADM::ControllerEK::TBCall::IOStarting"
+ "ADM::ControllerEK::TBCall::IOStopped"
+ "ADM::ControllerEK::TBCall::PrepareForIO"
+ "ADM::ControllerEK::TBCall::Unconfigure"
+ "ADM::ControllerEK::Unconfigure"
+ "AnomalyDetection"
+ "EchoCancellation"
+ "MicPreprocessing"
+ "RefSanitization"
+ "TB_FATAL: invalid error returned from getParameter (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from performIO (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from prepareForIO (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from setParameter (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from unconfigure (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "UnknownDSPStage"
- "(audiodsputility_orientationparametervalue__decode(message, &val->values.orientation.field0) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.OrientationParameterValue\""
- "(audiodsputility_parametererror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.ParameterError\""
- "(audiodsputility_parametervalue__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.ParameterValue\""
- "(audiodsputility_processerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.ProcessError\""
- "(audiodsputility_setuperror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.SetupError\""
- "(audiodsputility_usecase__decode(&tbMessage, &useCase) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.UseCase\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getParameter\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from performIO\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from prepareForIO\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from setParameter\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from unconfigure\""

```
