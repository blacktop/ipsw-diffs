## SiriAudioFlowTools

> `/System/Library/FlowTools/Tools/SiriAudioFlowTools.flowtool/SiriAudioFlowTools`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__common`

```diff

-3600.33.9.0.0
-  __TEXT.__text: 0x62f34
-  __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_stubs: 0x480
-  __TEXT.__const: 0x6d40
-  __TEXT.__oslogstring: 0x3a88
-  __TEXT.__constg_swiftt: 0x13f4
-  __TEXT.__swift5_typeref: 0x18cc
-  __TEXT.__swift5_reflstr: 0x14bf
-  __TEXT.__swift5_fieldmd: 0x17e0
+3600.33.17.0.0
+  __TEXT.__text: 0x65420
+  __TEXT.__auth_stubs: 0x1a70
+  __TEXT.__objc_stubs: 0x4a0
+  __TEXT.__const: 0x6ee0
+  __TEXT.__oslogstring: 0x3cd8
+  __TEXT.__constg_swiftt: 0x1478
+  __TEXT.__swift5_typeref: 0x1960
+  __TEXT.__swift5_reflstr: 0x14cf
+  __TEXT.__swift5_fieldmd: 0x180c
   __TEXT.__swift5_assocty: 0x400
-  __TEXT.__cstring: 0xa75
-  __TEXT.__swift5_proto: 0x5d0
-  __TEXT.__swift5_types: 0x19c
-  __TEXT.__swift5_capture: 0x194
+  __TEXT.__cstring: 0xab5
+  __TEXT.__swift5_proto: 0x5e0
+  __TEXT.__swift5_types: 0x1a4
+  __TEXT.__swift5_capture: 0x1b4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__swift_as_entry: 0xec
-  __TEXT.__swift_as_ret: 0x148
-  __TEXT.__swift_as_cont: 0x90
+  __TEXT.__swift_as_entry: 0xf4
+  __TEXT.__swift_as_ret: 0x154
+  __TEXT.__swift_as_cont: 0x94
   __TEXT.__objc_classname: 0x1ef
-  __TEXT.__objc_methname: 0x400
-  __TEXT.__objc_methtype: 0x1
-  __TEXT.__swift5_protos: 0x48
-  __TEXT.__unwind_info: 0x1470
-  __TEXT.__eh_frame: 0x26b0
-  __DATA_CONST.__const: 0x3368
+  __TEXT.__objc_methname: 0x410
+  __TEXT.__objc_methtype: 0x26
+  __TEXT.__swift5_protos: 0x4c
+  __TEXT.__unwind_info: 0x14e0
+  __TEXT.__eh_frame: 0x27c0
+  __DATA_CONST.__const: 0x34a0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xcb0
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__auth_ptr: 0x2120
+  __DATA_CONST.__auth_got: 0xd40
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__auth_ptr: 0x2170
   __DATA.__objc_const: 0xae0
-  __DATA.__objc_selrefs: 0x120
+  __DATA.__objc_selrefs: 0x128
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x24d0
-  __DATA.__bss: 0x9d40
+  __DATA.__data: 0x2538
+  __DATA.__bss: 0x9ec0
   __DATA.__common: 0x268
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/FlowToolsShared.framework/FlowToolsShared
   - /System/Library/PrivateFrameworks/FlowToolsSnippetService.framework/FlowToolsSnippetService
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
+  - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch
   - /System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation

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
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1655
-  Symbols:   192
-  CStrings:  313
+  Functions: 1692
+  Symbols:   205
+  CStrings:  322
 
Symbols:
+ _MRMediaRemoteSendCommandWithReply
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_OS_dispatch_queue
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ _kMRMediaRemoteOptionRemoteControlInterfaceIdentifier
+ _objc_retain_x26
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_dynamicCastObjCClass
+ _swift_getForeignTypeMetadata
+ _swift_retain_x2
CStrings:
+ "PlayAudioAppIntentExecutionStrategy.execute() - playbackRequestIdentifier=%{public}s applied to connect-to-speaker/warmup/play"
+ "PlayAudioAppIntentExecutionStrategy.playbackRequestIdentifier is 1P, try to use existing UUID"
+ "PlayAudioAppIntentExecutionStrategy.playbackRequestIdentifier not 1P ('%s'), mint new UUID"
+ "UpdateAudioAffinityAppIntentExecutionStrategy.skipToNextTrackIfNeeded() companion-paired request, not sending local next-track command (audio is on another device)"
+ "UpdateAudioAffinityAppIntentExecutionStrategy.skipToNextTrackIfNeeded() disliked a song, sending next-track command"
+ "UpdateAudioAffinityAppIntentExecutionStrategy.skipToNextTrackIfNeeded() next-track command did not succeed"
+ "com.apple.amp.agora"
+ "integerValue"
+ "sendNextTrackCommand()"
+ "v16@?0r^{__CFArray=}8"
- "PlayAudioAppIntentExecutionStrategy.execute() - minted playbackRequestIdentifier=%{public}s applied to connect-to-speaker/warmup/play"
```
