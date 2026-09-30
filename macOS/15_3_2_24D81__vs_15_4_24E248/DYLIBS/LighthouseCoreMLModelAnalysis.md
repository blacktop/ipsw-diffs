## LighthouseCoreMLModelAnalysis

> `/System/Library/PrivateFrameworks/LighthouseCoreMLModelAnalysis.framework/Versions/A/LighthouseCoreMLModelAnalysis`

```diff

 3.0.0.0.0
-  __TEXT.__text: 0x1938
+  __TEXT.__text: 0x1950
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0x88
   __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0x9c
   __TEXT.__cstring: 0x6b
   __TEXT.__oslogstring: 0x2a9
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methname: 0x447
   __TEXT.__objc_methtype: 0x82

   - /System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/Versions/A/LighthouseCoreMLModelStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49949D92-7236-371F-A337-3442431B84B6
+  UUID: 7792696C-1EE1-3A77-A8A1-A559734A39DC
   Functions: 30
   Symbols:   136
   CStrings:  82
Symbols:
+ +[LighthouseCoreMLModelTraining initialize].cold.1
- _OUTLINED_FUNCTION_3
Functions:
~ +[LighthouseCoreMLModelTraining initialize] : 40 -> 44
~ +[LighthouseCoreMLModelTraining trainModel:destModelUrl:modelConfiguration:dataBatch:labelFeatureName:] : 1728 -> 1720
~ __103+[LighthouseCoreMLModelTraining trainModel:destModelUrl:modelConfiguration:dataBatch:labelFeatureName:]_block_invoke.67 : 452 -> 456
~ _OUTLINED_FUNCTION_0 : 28 -> 12
~ _OUTLINED_FUNCTION_2 : 28 -> 32
~ _OUTLINED_FUNCTION_3 -> +[LighthouseCoreMLModelTraining initialize].cold.1 : 32 -> 20
~ +[LighthouseCoreMLModelTraining validateModelFeatureName:modelConfiguration:dataBatch:].cold.1 : 56 -> 244
~ +[LighthouseCoreMLModelTraining validateModelFeatureName:modelConfiguration:dataBatch:].cold.2 : 104 -> 112
~ +[LighthouseCoreMLModelTraining validateModelFeatureName:modelConfiguration:dataBatch:].cold.3 : 244 -> 64
~ __103+[LighthouseCoreMLModelTraining trainModel:destModelUrl:modelConfiguration:dataBatch:labelFeatureName:]_block_invoke.67.cold.1 : 120 -> 128
~ +[LighthouseCoreMLModelTraining evaluateModel:modelConfiguration:dataBatch:].cold.1 : 56 -> 160
~ +[LighthouseCoreMLModelTraining evaluateModel:modelConfiguration:dataBatch:].cold.2 : 56 -> 112
~ +[LighthouseCoreMLModelTraining evaluateModel:modelConfiguration:dataBatch:].cold.3 : 104 -> 64
~ +[LighthouseCoreMLModelTraining evaluateModel:modelConfiguration:dataBatch:].cold.4 : 160 -> 64

```
