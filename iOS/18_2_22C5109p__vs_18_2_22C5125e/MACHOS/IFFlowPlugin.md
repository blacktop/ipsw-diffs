## IFFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin`

```diff

-3402.46.3.1.3
-  __TEXT.__text: 0x350c8
-  __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__const: 0x9d8
+3402.55.3.1.1
+  __TEXT.__text: 0x3a1f8
+  __TEXT.__auth_stubs: 0x2260
+  __TEXT.__const: 0x9f8
   __TEXT.__constg_swiftt: 0x2f0
-  __TEXT.__swift5_typeref: 0x7c8
-  __TEXT.__swift5_reflstr: 0x442
-  __TEXT.__swift5_fieldmd: 0x374
-  __TEXT.__cstring: 0xfe8
+  __TEXT.__swift5_typeref: 0x832
+  __TEXT.__swift5_reflstr: 0x482
+  __TEXT.__swift5_fieldmd: 0x398
+  __TEXT.__cstring: 0x1048
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x34
   __TEXT.__objc_classname: 0x24
-  __TEXT.__objc_methname: 0x542
+  __TEXT.__objc_methname: 0x57e
   __TEXT.__objc_methtype: 0x19e
-  __TEXT.__oslogstring: 0x1ac7
+  __TEXT.__oslogstring: 0x1db7
   __TEXT.__swift5_assocty: 0x70
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_capture: 0xd8
-  __TEXT.__unwind_info: 0x6f0
-  __TEXT.__eh_frame: 0xee8
-  __DATA_CONST.__auth_got: 0x1070
-  __DATA_CONST.__got: 0x740
-  __DATA_CONST.__auth_ptr: 0x568
+  __TEXT.__unwind_info: 0x760
+  __TEXT.__eh_frame: 0x1060
+  __DATA_CONST.__auth_got: 0x1130
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__auth_ptr: 0x588
   __DATA_CONST.__const: 0x540
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0xd70
-  __DATA.__objc_selrefs: 0x120
-  __DATA.__data: 0xb10
+  __DATA.__objc_const: 0xdb0
+  __DATA.__objc_selrefs: 0x138
+  __DATA.__data: 0xb80
   __DATA.__bss: 0x820
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 445
-  Symbols:   156
-  CStrings:  292
+  Functions: 475
+  Symbols:   160
+  CStrings:  310
 
Symbols:
+ _OBJC_CLASS_$_SAUIFeedbackForm
+ _SAUIFeedbackFormDomainSiriWithChatGPTValue
+ _swift_getObjCClassFromMetadata
+ _swift_projectBox
CStrings:
+ "Event received from IntelligenceFlow: %!{(MISSING)public}s"
+ "Exiting IFFlow, received .unaswered from PromptForValueFlow"
+ "Exiting IFFlow, received userCancelled"
+ "IF client stream ended unexpectedly"
+ "IFFlow Confirmation for GenAI Media QnA won't re-prompt on empty parse."
+ "IFFlow Confirmation re-prompting on empty parse."
+ "IFFlow creating feedback form for toolId: %!s(MISSING)"
+ "IFFlow pushing confirmation flow, isGenAIMediaQnA: %!{(MISSING)bool}d"
+ "IFFlow received parameterNotAllowed pushing needsValue flow for %!s(MISSING)"
+ "IFFlow retrieving string content for feedback form with length: %!l(MISSING)d"
+ "IFFlow setting subFeature as: %!s(MISSING)"
+ "IFFlow state transitioned to %!{(MISSING)public}s"
+ "IFFlowError.sessionTerminated"
+ "Setting minimumAutoDismissalTimeInMs to %!l(MISSING)d"
+ "com.apple.generativeassistanttools"
+ "initWithSessionID:requestID:inputOrigin:responseMode:isEyesFree:isMultiUser:isVoiceTriggerEnabled:isTextToSpeechEnabled:isTriggerlessFollowup:deviceRestrictions:bargeInModes:identifiedUser:encodedLocation:countryCode:siriLocale:contentRestrictions:uiScale:temperatureUnit:allowUserGeneratedContent:censorSpeech:meCard:deviceIdiom:didPSCFire:"
+ "isGenAIMediaQnA"
+ "redacting logs for parameterNotAllowed request - %!s(MISSING)"
+ "setDomain:"
+ "setOutput:"
+ "setSubFeature:"
- "IF client stream hung up unexpectedly"
- "IFFlow pushing confirmation flow"
- "initWithSessionID:requestID:inputOrigin:responseMode:isEyesFree:isMultiUser:isVoiceTriggerEnabled:isTextToSpeechEnabled:isTriggerlessFollowup:deviceRestrictions:bargeInModes:identifiedUser:encodedLocation:countryCode:siriLocale:contentRestrictions:uiScale:temperatureUnit:allowUserGeneratedContent:censorSpeech:meCard:"

```
