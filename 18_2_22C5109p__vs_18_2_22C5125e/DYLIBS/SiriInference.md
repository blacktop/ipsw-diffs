## SiriInference

> `/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference`

```diff

-3402.43.1.1.2
-  __TEXT.__text: 0x33515c
-  __TEXT.__auth_stubs: 0x55c0
+3402.51.1.1.1
+  __TEXT.__text: 0x336d14
+  __TEXT.__auth_stubs: 0x55f0
   __TEXT.__objc_methlist: 0x528
-  __TEXT.__const: 0x20780
-  __TEXT.__cstring: 0x122a4
-  __TEXT.__swift5_typeref: 0x8296
-  __TEXT.__swift5_fieldmd: 0xf8d0
-  __TEXT.__constg_swiftt: 0x9928
+  __TEXT.__const: 0x207d8
+  __TEXT.__cstring: 0x122d7
+  __TEXT.__swift5_typeref: 0x82c8
+  __TEXT.__swift5_fieldmd: 0xf920
+  __TEXT.__constg_swiftt: 0x99a4
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0xf544
+  __TEXT.__swift5_reflstr: 0xf564
   __TEXT.__swift5_assocty: 0x1330
-  __TEXT.__swift5_protos: 0x138
-  __TEXT.__swift5_proto: 0x1f30
-  __TEXT.__swift5_types: 0xb48
-  __TEXT.__oslogstring: 0x105f0
+  __TEXT.__swift5_protos: 0x13c
+  __TEXT.__swift5_proto: 0x1f34
+  __TEXT.__swift5_types: 0xb4c
+  __TEXT.__oslogstring: 0x10920
   __TEXT.__swift5_capture: 0x1248
   __TEXT.__swift5_mpenum: 0x80
-  __TEXT.__unwind_info: 0xb908
-  __TEXT.__eh_frame: 0x1452c
+  __TEXT.__unwind_info: 0xb930
+  __TEXT.__eh_frame: 0x14534
   __TEXT.__objc_classname: 0xc3
-  __TEXT.__objc_methname: 0x4e80
+  __TEXT.__objc_methname: 0x4ebe
   __TEXT.__objc_methtype: 0x186
-  __DATA_CONST.__got: 0x2110
+  __DATA_CONST.__got: 0x2118
   __DATA_CONST.__const: 0x280
-  __DATA_CONST.__objc_classlist: 0x358
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a48
+  __DATA_CONST.__objc_selrefs: 0x1a60
   __DATA_CONST.__objc_protorefs: 0x70
-  __AUTH_CONST.__auth_got: 0x2ae0
-  __AUTH_CONST.__auth_ptr: 0x2068
-  __AUTH_CONST.__const: 0x1bce8
-  __AUTH_CONST.__objc_const: 0x7798
+  __AUTH_CONST.__auth_got: 0x2af8
+  __AUTH_CONST.__auth_ptr: 0x20e0
+  __AUTH_CONST.__const: 0x1bd00
+  __AUTH_CONST.__objc_const: 0x7850
   __AUTH.__objc_data: 0x7d8
-  __AUTH.__data: 0x77e0
-  __DATA.__data: 0x6000
+  __AUTH.__data: 0x7850
+  __DATA.__data: 0x5ff0
   __DATA.__bss: 0x37110
   __DATA.__common: 0x1a0
   __DATA_DIRTY.__objc_data: 0xdb8
-  __DATA_DIRTY.__data: 0x2f20
+  __DATA_DIRTY.__data: 0x2fc0
   __DATA_DIRTY.__bss: 0xe00
   __DATA_DIRTY.__common: 0x240
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 18377
-  Symbols:   5672
-  CStrings:  4357
+  Functions: 18396
+  Symbols:   5690
+  CStrings:  4370
 
Symbols:
+ _OBJC_CLASS_$_INFERENCESchemaINFERENCESmartEnoughAppSelectionExecutionPathReported
CStrings:
+ "#AppResolver#resolveApp: Found more than 1 app to resolve: %!s(MISSING)"
+ "AppResolverLogEmitter#emitAppSelectionExecutionPath: Error generating log message Skipping Emission."
+ "AppResolverLogEmitter#emitAppSelectionExecutionPath: Execution path emitted."
+ "AppResolverLogEmitter#emitAppSelectionExecutionPath: No inferenceUUID, not emitting SELF."
+ "AppResolverLogEmitter#generateRequestLink: Failed to create RequestLink SELF message templates."
+ "AppResolverLogEmitter#generateSelfMessage: failed to generate top-level SELF message"
+ "AppResolverLogEmitter#generateSelfMessage: generated SELF message for SeAS execution path: %!s(MISSING)"
+ "MLAppPredictionOutput#getPrediction Direct execution on %!s(MISSING)"
+ "MLAppPredictionOutput#getPrediction confirmation on %!s(MISSING)"
+ "MLAppPredictionOutput#getPrediction disambigutaion on %!s(MISSING)"
+ "MLAppPredictionOutput#getPrediction: Unexpected output from model %!@(MISSING) & %!@(MISSING)"
+ "MLAppPredictionOutput#getPrediction: model defaults to default app"
+ "MLAppPredictionOutput#getPrediction: model output does not contain appsShowToUser value for all eligible candidate apps"
+ "MLAppPredictionOutput#getPrediction: model output does not contain the appConfidence value of size 1"
+ "Placemark has no memorable UUID"
+ "[UCG] There are relationship matches that appear to have high quality signals for '%!s(MISSING)'. Will discard other matches..."
+ "_TtC13SiriInference21AppResolverLogEmitter"
+ "executionPath"
+ "setExecutionPath:"
+ "setSeasExecutionPathReported:"
- "#AppResolver#resolveApp: Found more than 1 app to resolve"
- "PhoneAppPredictorOutput#getPrediction Direct execution on %!s(MISSING)"
- "PhoneAppPredictorOutput#getPrediction confirmation on %!s(MISSING)"
- "PhoneAppPredictorOutput#getPrediction disambigutaion on %!s(MISSING)"
- "PhoneAppPredictorOutput#getPrediction: Unexpected output from model %!@(MISSING) & %!@(MISSING)"
- "PhoneAppPredictorOutput#getPrediction: model output does not contain appsShowToUser value for all eligible candidate apps"
- "PhoneAppPredictorOutput#getPrediction: model output does not contain the appConfidence value of size 1"

```
