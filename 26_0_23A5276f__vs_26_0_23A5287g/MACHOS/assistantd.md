## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3500.104.2.0.0
-  __TEXT.__text: 0x37075c
+3500.108.6.0.0
+  __TEXT.__text: 0x3710ac
   __TEXT.__auth_stubs: 0x34b0
-  __TEXT.__objc_stubs: 0x44600
-  __TEXT.__objc_methlist: 0x22220
+  __TEXT.__objc_stubs: 0x446e0
+  __TEXT.__objc_methlist: 0x22248
   __TEXT.__const: 0x109c8
   __TEXT.__dlopen_cstrs: 0xafa
   __TEXT.__gcc_except_tab: 0x49a0
-  __TEXT.__cstring: 0x51272
-  __TEXT.__oslogstring: 0x3fd1a
+  __TEXT.__cstring: 0x5128b
+  __TEXT.__oslogstring: 0x3fdb1
   __TEXT.__objc_classname: 0x517c
-  __TEXT.__objc_methname: 0x5c3b4
+  __TEXT.__objc_methname: 0x5c48b
   __TEXT.__objc_methtype: 0xf108
   __TEXT.__ustring: 0x2b0
-  __TEXT.__unwind_info: 0xa150
+  __TEXT.__unwind_info: 0xa310
   __TEXT.__eh_frame: 0x80
   __DATA_CONST.__auth_got: 0x1a68
-  __DATA_CONST.__got: 0x3a58
+  __DATA_CONST.__got: 0x3a70
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x14d38
+  __DATA_CONST.__const: 0x14d00
   __DATA_CONST.__cfstring: 0x127c0
   __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x620

   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x33550
-  __DATA.__objc_selrefs: 0x14520
+  __DATA.__objc_const: 0x33558
+  __DATA.__objc_selrefs: 0x14560
   __DATA.__objc_ivar: 0x2558
   __DATA.__objc_data: 0x8340
   __DATA.__data: 0x5630

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
+  - /System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 661C325D-054A-3DB5-B11A-A47EE7EE872B
-  Functions: 14255
-  Symbols:   2862
-  CStrings:  29299
+  UUID: 9D4C91E4-48E1-32AC-82FD-22F546CB06A8
+  Functions: 14260
+  Symbols:   2865
+  CStrings:  29311
 
Symbols:
+ _OBJC_CLASS_$_AFSpeechPackage
+ _OBJC_CLASS_$_FSFCurareInteractionAsJsonStr
+ _OBJC_CLASS_$_FSFCurareInteractionStream
CStrings:
+ "%s Enabling Assistant alongside voice trigger"
+ "%s Error: %@ inserting \"%@\" into FeatureStore for id: %@"
+ "%s RestrictedCommands: Adding EYES_FREE DeviceRestriction"
+ "%s setEndpointerThreshold: %f in CoreSpeech."
+ "25"
+ "ADVoiceTriggerSetEnabled"
+ "MobileAssistantDaemons-3500.108.6"
+ "fromSASRecognition:processedAudioDuration:"
+ "initWithJsonStr:interactionId:dataVersion:"
+ "initWithStreamId:"
+ "insert:error:"
+ "isEyesFreeDevice"
+ "isSiriEnabledOnCompanion"
+ "setAssistantIsEnabled:"
+ "setIsLongLivedIDUploadDisabled:"
- "%s setEndpointerThreshold: %f is unused in CoreSpeech."
- "45"
- "MobileAssistantDaemons-3500.104.2"

```
