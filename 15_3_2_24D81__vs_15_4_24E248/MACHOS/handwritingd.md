## handwritingd

> `/usr/libexec/handwritingd`

```diff

-516.2.0.0.0
-  __TEXT.__text: 0x16800
+521.6.0.0.0
+  __TEXT.__text: 0x17654
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x2fe0
-  __TEXT.__objc_methlist: 0x96c
+  __TEXT.__objc_stubs: 0x30c0
+  __TEXT.__objc_methlist: 0xc58
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x1ce4
-  __TEXT.__cstring: 0x127d
-  __TEXT.__objc_methname: 0x3722
-  __TEXT.__objc_classname: 0x271
-  __TEXT.__objc_methtype: 0x957
-  __TEXT.__oslogstring: 0x1a9f
-  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__gcc_except_tab: 0x1ed4
+  __TEXT.__cstring: 0x1291
+  __TEXT.__objc_methname: 0x386b
+  __TEXT.__objc_classname: 0x274
+  __TEXT.__objc_methtype: 0x9d0
+  __TEXT.__oslogstring: 0x1c49
+  __TEXT.__unwind_info: 0x7d8
   __DATA_CONST.__auth_got: 0x320
-  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__got: 0x310
   __DATA_CONST.__const: 0x830
   __DATA_CONST.__cfstring: 0xe40
   __DATA_CONST.__objc_classlist: 0x70

   __DATA_CONST.__objc_doubleobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x1a68
-  __DATA.__objc_selrefs: 0xd20
+  __DATA.__objc_const: 0x1560
+  __DATA.__objc_selrefs: 0xe00
   __DATA.__objc_ivar: 0xf0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x360

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93F9A0C8-1120-3716-A1CE-7FDAE9A8A8D2
-  Functions: 313
-  Symbols:   207
-  CStrings:  1031
+  UUID: 5A0EDADF-8764-3A6D-BF44-F6D5673F7C36
+  Functions: 317
+  Symbols:   210
+  CStrings:  1048
 
Symbols:
+ _OBJC_CLASS_$_CHMultiScriptTextSynthesizer
+ _OBJC_CLASS_$_CHPersonalizedSynthesisModelStatus
+ _OBJC_CLASS_$_CHSynthesisModelHashes
CStrings:
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
