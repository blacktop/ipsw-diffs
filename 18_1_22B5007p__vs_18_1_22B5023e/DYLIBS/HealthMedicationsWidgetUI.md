## HealthMedicationsWidgetUI

> `/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI`

```diff

-5132.0.0.0.0
-  __TEXT.__text: 0x2615c
-  __TEXT.__auth_stubs: 0x1390
-  __TEXT.__const: 0xaa4
+5200.1.3.0.0
+  __TEXT.__text: 0x26214
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__const: 0xab4
   __TEXT.__cstring: 0x5f9
   __TEXT.__constg_swiftt: 0x414
   __TEXT.__swift5_typeref: 0x52c

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_capture: 0xbc
   __TEXT.__oslogstring: 0x2d6
-  __TEXT.__unwind_info: 0x598
-  __TEXT.__eh_frame: 0x160
+  __TEXT.__unwind_info: 0x5a8
+  __TEXT.__eh_frame: 0x188
   __TEXT.__objc_methname: 0xc9
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x9c8
-  __AUTH_CONST.__auth_ptr: 0x3a8
+  __AUTH_CONST.__auth_got: 0x9d0
+  __AUTH_CONST.__auth_ptr: 0x3b0
   __AUTH_CONST.__const: 0x348
   __AUTH_CONST.__objc_const: 0x1a0
   __AUTH.__data: 0x98
-  __DATA.__data: 0x1f0
+  __DATA.__data: 0x1f8
   __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0xa90

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 481
-  Symbols:   123
-  CStrings:  0
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 483
+  Symbols:   131
+  CStrings:  32
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "_$s11SiriKitFlow011YesNoPromptC8StrategyPAAE04makeF15ForConfirmation13itemToConfirmAA6Output_pyt_tYaKF"
+ "_$s11SiriKitFlow011YesNoPromptC8StrategyPAAE24makeRepromptOnEmptyParse13itemToConfirmAA6Output_pyt_tYaKF"
+ "_$s11SiriKitFlow011YesNoPromptC8StrategyPAAE27makeRepromptOnLowConfidence13itemToConfirmAA6Output_pyt_tYaKF"
+ "_$s11SiriKitFlow029MultipleChoicePromptWindowingC8ProviderPAAE014makeConclusionC020paginationParametersAA03AnyC0CSgAA018WindowedPaginationL0V_tYaKF"
+ "_$s11SiriKitFlow0C10TraceEventO11encoreFoundyAcA06ActingC0_p_tcACmFWC"
+ "_$s11SiriKitFlow0C10TraceEventO9completedyAcA03AnyC0C_yptcACmFWC"
+ "_$s11SiriKitFlow15WindowingActionV12repeatWindowACyxGyFZ"
+ "_$s11SiriKitFlow15WindowingActionV21proceedWithNextWindowACyxGyFZ"
+ "_$s11SiriKitFlow15WindowingActionV5error_7handledACyxGs5Error_p_SbtFZ"
+ "_$s11SiriKitFlow15WindowingActionV8completeyACyxGxSgFZ"
+ "_$s11SiriKitFlow15WindowingActionV9cancelledACyxGyFZ"
+ "_$s11SiriKitFlow15WindowingActionVMa"
+ "_$s11SiriKitFlow18InterruptionPolicyO4stayyA2CmFWC"
+ "_$s11SiriKitFlow18InterruptionPolicyO5clearyA2CmFWC"
+ "_$s11SiriKitFlow18InterruptionPolicyO6notifyyA2CmFWC"
+ "_$s11SiriKitFlow18SubmitCommandErrorOs0F0AAMc"
+ "_$s11SiriKitFlow18SubmitCommandErrorOs23CustomStringConvertibleAAMc"
+ "_$s11SiriKitFlow20DisambiguationPromptC8ResponseO19chosenItemWithIndexyAEyxq_q0__Gx_SitcAGm0A8Ontology14USODynamicTaskR_r1_lFWC"
+ "_$s11SiriKitFlow20DisambiguationPromptC8ResponseO9cancelledyAEyxq_q0__GAGm0A8Ontology14USODynamicTaskR_r1_lFWC"
+ "_$s11SiriKitFlow20DisambiguationPromptC8ResponseO9rawEntityyAEyxq_q0__Gq0_cAGm0A8Ontology14USODynamicTaskR_r1_lFWC"
+ "_$s11SiriKitFlow20DisambiguationPromptCyxq_q0_GAA06ActingC0AAMc"
+ "_$s11SiriKitFlow22WindowingConfigurationV06promptC12ProviderType7padding18windowSizeOverrideACyxq_GAA06PromptcgH0Vyxq_G_S2iSgtcfC"
+ "_$s11SiriKitFlow25AceServiceContextProviderC0A9Utilities0a11EnvironmentG0AAMc"
+ "_$s11SiriKitFlow28WindowedPaginationParametersV016isNextWindowLastI0Sbvg"
+ "_$s11SiriKitFlow28WindowedPaginationParametersV12isConclusionSbvg"
+ "_$s11SiriKitFlow28WindowedPaginationParametersV14makeLastWindow10windowSize07isFirstI0ACSi_SbtFZ"
+ "_$s11SiriKitFlow28WindowedPaginationParametersV15asCATParametersSDySSypGyF"
+ "_$s11SiriKitFlow28WindowedPaginationParametersV19nextWindowItemCountSiSgvg"
+ "_$s11SiriKitFlow28WindowedPaginationParametersVMa"
+ "cA03AnyC0C_AA15PrepareResponseVtcACmFWC"
+ "rCyxGAA0eF10ContainingAAMc"
+ "stWindowSbvg"

```
