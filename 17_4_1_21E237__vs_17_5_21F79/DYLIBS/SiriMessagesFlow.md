## SiriMessagesFlow

> `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow`

```diff

-3304.67.1.11.1
-  __TEXT.__text: 0x37a6b4
-  __TEXT.__auth_stubs: 0x6f00
+3305.8.1.0.0
+  __TEXT.__text: 0x37db24
+  __TEXT.__auth_stubs: 0x6f30
   __TEXT.__objc_methlist: 0x4c
-  __TEXT.__const: 0xdea4
-  __TEXT.__cstring: 0x2b547
-  __TEXT.__constg_swiftt: 0xbb44
-  __TEXT.__swift5_typeref: 0x61b8
-  __TEXT.__swift5_builtin: 0x2a8
-  __TEXT.__swift5_reflstr: 0x7153
+  __TEXT.__const: 0xdf04
+  __TEXT.__cstring: 0x2bbd7
+  __TEXT.__constg_swiftt: 0xbb34
+  __TEXT.__swift5_typeref: 0x61e2
+  __TEXT.__swift5_builtin: 0x2bc
+  __TEXT.__swift5_reflstr: 0x710b
   __TEXT.__swift5_fieldmd: 0x7dac
-  __TEXT.__swift5_assocty: 0x1070
-  __TEXT.__swift5_proto: 0xa18
-  __TEXT.__swift5_types: 0x5f0
-  __TEXT.__swift5_capture: 0x27f0
+  __TEXT.__swift5_assocty: 0x1088
+  __TEXT.__swift5_proto: 0xa1c
+  __TEXT.__swift5_types: 0x5f4
+  __TEXT.__swift5_capture: 0x2864
   __TEXT.__swift5_protos: 0x14c
   __TEXT.__swift5_mpenum: 0x7c
-  __TEXT.__unwind_info: 0xc6e4
-  __TEXT.__eh_frame: 0x1f48c
+  __TEXT.__unwind_info: 0xc7dc
+  __TEXT.__eh_frame: 0x1f53c
   __TEXT.__objc_classname: 0x126
-  __TEXT.__objc_methname: 0x3764
+  __TEXT.__objc_methname: 0x3784
   __TEXT.__objc_methtype: 0x32c
-  __DATA_CONST.__got: 0x1618
+  __DATA_CONST.__got: 0x1648
   __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb760
-  __DATA_CONST.__objc_selrefs: 0x1390
+  __DATA_CONST.__objc_const: 0xb768
+  __DATA_CONST.__objc_selrefs: 0x1398
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_classrefs: 0x628
-  __AUTH_CONST.__const: 0x10be0
+  __AUTH_CONST.__const: 0x10d38
   __AUTH_CONST.__auth_ptr: 0x6c0
-  __AUTH_CONST.__auth_got: 0x3780
-  __AUTH.__data: 0xf808
+  __AUTH_CONST.__auth_got: 0x3798
+  __AUTH.__data: 0xf7d8
   __AUTH.__objc_data: 0x1710
   __DATA.__objc_data: 0x5e8
-  __DATA.__data: 0x93d8
-  __DATA.__bss: 0x11300
+  __DATA.__data: 0x9418
+  __DATA.__bss: 0x11380
   __DATA.__common: 0x7d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19889
-  Symbols:   16267
-  CStrings:  3808
+  Functions: 19935
+  Symbols:   16301
+  CStrings:  3825
 
Symbols:
+ __IVARS__TtC16SiriMessagesFlow24ExperimentSignalGatherer
+ _objectdestroy.145Tm
+ _objectdestroy.344Tm
+ _symbolic _____ So22INResolutionResultCodeV
+ _symbolic _____Iegr_ 10Foundation4UUIDV
+ _symbolic _____y__________GIegn_ s6ResultO 11SiriSignals14SignalGathererC17ValuesWithTimingsV AC0dE5ErrorO
- _objectdestroy.202Tm
- _objectdestroy.341Tm
CStrings:
+ "#AppSelectionSignalCollection: SignalGatherer#gatherValuesAndTimings complete gatherAndSave success"
+ "#AppSelectionSignalCollection: SignalGatherer#gatherValuesAndTimings error: %s"
+ "#AppSelectionSignalCollection: crrCommsAppSelectionJointId:%s"
+ "#AppSelectionSignalCollection: starting SignalGatherer#gatherValuesAndTimings (%s) complete"
+ "#AppSelectionSignalCollection: starting SignalGatherer#gatherValuesAndTimings (%s)..."
+ "#SeasExperiment - CRR force prompted, but failed enhanced joint prompt rate check for forced disambiguation"
+ "#SendMessageAppResolutionBeforeNextResolveFlow - invoking app selection with carried crrCommsAppSelectionJointId: %s"
+ "#SendMessageFlow (makeAppResolutionFlowBeforeNextResolveFlowProducer)  skipping app resolution before next resolve flow"
+ "#SendMessageNLv4IntentConverter crrCommsAppSelectionJointId:%s"
+ "#SendMessageNLv4IntentConverter found at least one CRR recipient from 'random' force prompt - name:%s identifier:%s"
+ "#SendMessageNeedsValueFlowStrategy from slot:%s updated intent: %@"
+ "#SendMessageNeedsValueFlowStrategy recipient, replacing old-crrIsForcePrompt:%{bool}d old-crrCommsAppSelectionJointId:%s with crrIsForcePrompt:%{bool}d crrCommsAppSelectionJointId:%s"
+ "#SendMessageNeedsValueFlowStrategy updated intent app bundle id: %s"
+ "#SendMessasgeFlow (makeAppResolutionFlowBeforeNextResolveFlowProducer) parameterName:%s, resolutionResultCode:%s, hasRecipientsOrGroupName:%{bool}d, isAppSelectedByUser:%{bool}d"
+ "#SendMessasgeFlow (makeAppResolutionFlowBeforeNextResolveFlowProducer) recipient is present after prompt and app was not selected, trying to resolve app again"
+ "#SignalInstrumentation - No instrumentation for gathered signal %s"
+ "#SiriKitContactResolving CRR config creation with appIdentifier:%s, crrCommsAppSelectionJointId:%s"
+ "#SmartAppSelectionFeature - missing trial level for expected factor: %s in namespace: %s"
+ "X-Dev-ConfigOverride-assistant.service.seas.disambiguation.jointCrr.INSendMessageIntent.enabled"
+ "crrCommsAppSelectionJointId"
+ "forcedAppDisambiguationJointCrr"
+ "forcedAppDisambiguationJointCrrSampleRate"
+ "setCrrCommsAppSelectionJointId:"
+ "timeout"
- "#AppSelectionSignalCollection: signal gatherer error: %s"
- "#SendMessageFlow skipping app resolution before next resolve flow"
- "#SendMessageNeedsValueFlowStrategy updated intent: %@"
- "#SendMessasgeFlow recipient is present after prompt and app was not selected, trying to resolve app again"
- "#SignalInstrumentation - No instrumentation for gatherred signal %s"
- "$__lazy_storage_$_isForceAppDisambiguationEnabled"
- "$__lazy_storage_$_needsSignalsForMentionedAppName"

```
