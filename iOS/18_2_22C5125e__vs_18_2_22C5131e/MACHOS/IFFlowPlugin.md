## IFFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin`

```diff

-3402.55.3.1.1
-  __TEXT.__text: 0x3a1f8
-  __TEXT.__auth_stubs: 0x2260
-  __TEXT.__const: 0x9f8
-  __TEXT.__constg_swiftt: 0x2f0
-  __TEXT.__swift5_typeref: 0x832
-  __TEXT.__swift5_reflstr: 0x482
-  __TEXT.__swift5_fieldmd: 0x398
-  __TEXT.__cstring: 0x1048
+3402.58.3.1.1
+  __TEXT.__text: 0x3c3c8
+  __TEXT.__auth_stubs: 0x22f0
+  __TEXT.__const: 0xab8
+  __TEXT.__constg_swiftt: 0x2f8
+  __TEXT.__swift5_typeref: 0x852
+  __TEXT.__swift5_reflstr: 0x4a2
+  __TEXT.__swift5_fieldmd: 0x3a4
+  __TEXT.__cstring: 0x1054
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x34
   __TEXT.__objc_classname: 0x24
-  __TEXT.__objc_methname: 0x57e
+  __TEXT.__objc_methname: 0x599
   __TEXT.__objc_methtype: 0x19e
-  __TEXT.__oslogstring: 0x1db7
+  __TEXT.__oslogstring: 0x1e77
   __TEXT.__swift5_assocty: 0x70
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_capture: 0xd8
-  __TEXT.__unwind_info: 0x760
-  __TEXT.__eh_frame: 0x1060
-  __DATA_CONST.__auth_got: 0x1130
-  __DATA_CONST.__got: 0x7e0
-  __DATA_CONST.__auth_ptr: 0x588
+  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__eh_frame: 0x11f0
+  __DATA_CONST.__auth_got: 0x1178
+  __DATA_CONST.__got: 0x870
+  __DATA_CONST.__auth_ptr: 0x5a8
   __DATA_CONST.__const: 0x540
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0xdb0
-  __DATA.__objc_selrefs: 0x138
-  __DATA.__data: 0xb80
-  __DATA.__bss: 0x820
+  __DATA.__objc_const: 0xdd0
+  __DATA.__objc_selrefs: 0x158
+  __DATA.__data: 0xbe8
+  __DATA.__bss: 0x840
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /System/Library/PrivateFrameworks/GenerativeAssistantEnablementFlow.framework/GenerativeAssistantEnablementFlow
   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
+  - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 475
-  Symbols:   160
-  CStrings:  310
+  Functions: 500
+  Symbols:   161
+  CStrings:  316
 
Symbols:
+ _objc_retain_x8
CStrings:
+ "Attempting to apply redaction tag for inferred toolId = %!s(MISSING) which is a Montara use-case"
+ "Attempting to apply redaction tag for inferred toolId = %!s(MISSING) which is a PQA use-case"
+ "Cannot attempt to apply redaction tag for empty rootRequestId"
+ "Exiting IFFlow, received .unaswered from PromptForDisambiguation"
+ "IFFlow not accepting input. No supported utterance found."
+ "IFFlow value prompt received direct SiriX input instead of NLRouterParse. Using observed utterance from environment (%!s(MISSING))"
+ "Not attempting to apply redaction tag for inferred toolId = %!s(MISSING)"
+ "Posting SDA: %!s(MISSING)"
+ "Unexpectedly found nil criticalInfoValueResponse in %!s(MISSING) (why didn't actionForInput ignore?)"
+ "_currentUtterance"
+ "dialog"
+ "id"
+ "setCatId:"
+ "setId:"
+ "systemResponseAction(_:systemResponse:responseFactory:executionRequestId:currentRequest:userUtterance:deviceState:)"
- "Couldn't create affirmative reference. Affirmative button label: %!s(MISSING)"
- "Couldn't create negative reference. Negative button label: %!s(MISSING)"
- "Posting sda using affirmative label: %!s(MISSING), negative label: %!s(MISSING)"
- "Unexpectedly found nil criticalInfoValueResponse in %!s(MISSING)"
- "redacting logs for parameterDisambiguation request - %!s(MISSING)"
- "redacting logs for parameterNeedsValue request - %!s(MISSING)"
- "redacting logs for parameterNotAllowed request - %!s(MISSING)"
- "redacting logs for success request - %!s(MISSING)"
- "systemResponseAction(_:systemResponse:responseFactory:executionRequestId:currentRequest:userUtterance:deviceState:instrumentationUtil:)"

```
