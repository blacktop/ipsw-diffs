## handwritingd

> `/usr/libexec/handwritingd`

```diff

-516.2.0.0.0
-  __TEXT.__text: 0x14520
+521.4.0.0.0
+  __TEXT.__text: 0x151d4
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0x3080
-  __TEXT.__objc_methlist: 0x984
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x1cd8
-  __TEXT.__cstring: 0x1339
-  __TEXT.__objc_methname: 0x37f3
-  __TEXT.__objc_classname: 0x271
-  __TEXT.__objc_methtype: 0x969
+  __TEXT.__objc_stubs: 0x3160
+  __TEXT.__objc_methlist: 0xc88
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__oslogstring: 0x1982
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x1ecc
+  __TEXT.__cstring: 0x134d
+  __TEXT.__objc_methname: 0x393c
+  __TEXT.__objc_classname: 0x274
+  __TEXT.__objc_methtype: 0x9e2
+  __TEXT.__oslogstring: 0x1b2c
+  __TEXT.__unwind_info: 0x7b0
   __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__got: 0x358
   __DATA_CONST.__const: 0x768
   __DATA_CONST.__cfstring: 0xf00
   __DATA_CONST.__objc_classlist: 0x70

   __DATA_CONST.__objc_doubleobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x1aa8
-  __DATA.__objc_selrefs: 0xd58
+  __DATA.__objc_const: 0x1570
+  __DATA.__objc_selrefs: 0xe38
   __DATA.__objc_ivar: 0xf0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x360

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 271
-  Symbols:   243
-  CStrings:  934
+  Functions: 275
+  Symbols:   246
+  CStrings:  952
 
Symbols:
+ _OBJC_CLASS_$_CHMultiScriptTextSynthesizer
+ _OBJC_CLASS_$_CHPersonalizedSynthesisModelStatus
+ _OBJC_CLASS_$_CHSynthesisModelHashes
CStrings:
+ "\x01\x11"
+ "@\"<CHSynthesizingText><CHSynthesizingTextInternal>\""
+ "BEGIN \"CHLoadDaemonResources\""
+ "CHLoadDaemonResources"
+ "CHRemoteSynthesisRequestTypeGeneration: style prediction from the textSynthesizer is nil for input style sample with content %{sensitive}@"
+ "Diffusion model (Latin) is not ready. The model hash could not be validated"
+ "END \"CHLoadDaemonResources\""
+ "Handling remote inventory containing sample request"
+ "Invalid tokenized result type provided: %@"
+ "Inventory data ingestion: (embedding prediction) sample with unsupported script. This sample will be removed: %{sensitive}@"
+ "Inventory data ingestion: Script prediction for tokenized text results is non-supported script for string: %{sensitive}@"
+ "The diffusion model hash for Latin should be non-nil"
+ "addSamplesIfNeededWithTokenizedTextResult:drawing:script:strokeIdentifiers:"
+ "containsSampleWithStrokeIdentifiers:"
+ "diffusionModelHashes"
+ "handleInventoryContainingSampleRequest:withReply:bundleIdentifier:"
+ "handleInventoryContentCheckRequest:withReply:"
+ "isPersonalizedSynthesisAvailableForLatin"
+ "latin"
+ "modelHashesWithLatinHash:"
+ "needsStylePredictionUpdateForScript:"
+ "q24@0:8q16"
+ "setStylePredictions:"
+ "stitchStyleSamples:"
+ "styleContents"
+ "styleDrawings"
+ "stylePredictionResultForTranscriptions:drawings:shouldCancel:"
+ "styleSampleOptionsForRequest:script:"
+ "styleSamplesForInputSample:prompt:script:samplingAlgorithm:"
+ "styleSamplesForInputSample:prompt:script:samplingAlgorithm:maxNumOfSamples:"
+ "styleScriptForSynthesizerSupportedStyle:"
+ "synthesisModelHashes"
+ "synthesis_expansion"
+ "updateStyleEmbedding:script:"
+ "updateSynthesisModelHashLatin:"
+ "v32@0:8@\"CHRemoteInventoryContentCheckRequest\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
- "@\"CHTextSynthesizer\""
- "CHRemoteSynthesisRequestTypeGeneration: style prediction from the textSynthesizer is nil for input style sample"
- "Diffusion model is not ready. The model hash could not be validated"
- "Invalid tokenized result type provided"
- "The diffusion model hash should be non-nil"
- "addSamplesIfNeededWithTokenizedTextResult:drawing:strokeIdentifiers:"
- "isPersonalizedSynthesisModelReady"
- "needsStylePredictionUpdate"
- "setStylePrediction:"
- "styleContent"
- "styleDrawing"
- "stylePredictionResultForTranscription:drawing:shouldCancel:"
- "styleSampleForInputSample:prompt:samplingAlgorithm:"
- "styleSampleOptionsForRequest:"
- "styleSamplesForInputSample:prompt:samplingAlgorithm:maxNumOfSamples:"
- "synthesisModelHash"
- "updateStyleEmbedding:"
- "updateSynthesisModelHash:"

```
