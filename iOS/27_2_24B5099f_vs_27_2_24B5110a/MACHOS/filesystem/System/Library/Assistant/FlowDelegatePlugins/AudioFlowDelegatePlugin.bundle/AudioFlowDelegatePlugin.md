## AudioFlowDelegatePlugin

> `System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-3605.23.1.0.0
-  __TEXT.__text: 0x2bb3bc
-  __TEXT.__auth_stubs: 0x6f10
-  __TEXT.__objc_stubs: 0x2ec0
+3605.24.1.0.0
+  __TEXT.__text: 0x2c2048
+  __TEXT.__auth_stubs: 0x6f70
+  __TEXT.__objc_stubs: 0x2ee0
   __TEXT.__objc_methlist: 0x6e8
-  __TEXT.__const: 0xc11a
-  __TEXT.__cstring: 0x4a9c
-  __TEXT.__swift5_typeref: 0x47a4
-  __TEXT.__oslogstring: 0x247bc
-  __TEXT.__constg_swiftt: 0x5b98
+  __TEXT.__const: 0xc1fa
+  __TEXT.__cstring: 0x4adc
+  __TEXT.__swift5_typeref: 0x47fc
+  __TEXT.__oslogstring: 0x24d2c
+  __TEXT.__constg_swiftt: 0x5c38
   __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_reflstr: 0x424b
+  __TEXT.__swift5_reflstr: 0x436b
   __TEXT.__swift5_assocty: 0xaa0
-  __TEXT.__swift5_proto: 0x708
+  __TEXT.__swift5_proto: 0x714
   __TEXT.__swift5_types: 0x3ac
   __TEXT.__objc_classname: 0x1db9
   __TEXT.__objc_methtype: 0x5ca
-  __TEXT.__objc_methname: 0x3f9d
-  __TEXT.__swift5_fieldmd: 0x3688
+  __TEXT.__objc_methname: 0x3fcd
+  __TEXT.__swift5_fieldmd: 0x377c
   __TEXT.__swift5_capture: 0x63a0
   __TEXT.__swift_as_entry: 0x198
   __TEXT.__swift_as_ret: 0x230
   __TEXT.__swift_as_cont: 0x1c8
-  __TEXT.__swift5_protos: 0x70
+  __TEXT.__swift5_protos: 0x74
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x4ef0
+  __TEXT.__unwind_info: 0x4f48
   __TEXT.__eh_frame: 0x36f8
-  __DATA_CONST.__const: 0xfe08
+  __DATA_CONST.__const: 0xfec8
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__auth_got: 0x3790
-  __DATA_CONST.__got: 0x1ea8
-  __DATA_CONST.__auth_ptr: 0x1ac0
-  __DATA.__objc_const: 0x9e10
-  __DATA.__objc_selrefs: 0xdb0
+  __DATA_CONST.__auth_got: 0x37c0
+  __DATA_CONST.__got: 0x1ee0
+  __DATA_CONST.__auth_ptr: 0x1ad0
+  __DATA.__objc_const: 0x9e30
+  __DATA.__objc_selrefs: 0xdb8
   __DATA.__objc_data: 0x1258
-  __DATA.__data: 0xc330
+  __DATA.__data: 0xc3c0
   __DATA.__common: 0x448
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
+  - /System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6047
+  Functions: 6072
   Symbols:   397
-  CStrings:  2977
+  CStrings:  2992
 
CStrings:
+ "ContinueInAppPunchOutStrategy#homeAccessoryContinuation cannot continue on the accessory, handling locally. hasAppIdentifier: %{bool,public}d, handledBySiriForAirPlay: %{bool,public}d, hasAssistantID: %{bool,public}d"
+ "ContinueInAppPunchOutStrategy#homeAccessoryContinuation originIsHomeAccessory: %{bool,public}d, isPumpkin: %{bool,public}d"
+ "ContinueInAppPunchOutStrategy#makeContinueInAppAutoPunchOutResponse launchAppCommand %@, appBundleId %s"
+ "ContinueInAppPunchOutStrategy#makeContinueInAppAutoPunchOutResponse remote assistantId %s, eor %@"
+ "ContinueInAppPunchOutStrategy#requireUnlock requireUnlock: %{bool}d"
+ "ExecuteMusicOnRemoteFlow#execute isFollowUpTurn: %{bool}d"
+ "ExecuteMusicOnRemoteFlow#execute remote request completed with topicSwitchDetected. Will return .unhandled(reason: .needsExecutionRerun)"
+ "ExecuteMusicOnRemoteFlow#execute remote request is waiting on user input. Will return .ongoing(requireInput: true)"
+ "FallbackSpeakerIDProviding#speakerIDInfo attaching sharedUserID: %{private}s, classification: %{public}s, speakerIDConfidence: %{public}ld %{public}s"
+ "FallbackSpeakerIDProviding#speakerIDInfo no sharedUserID to attach; SiriKit fallback intent will carry no speaker identity %{public}s"
+ "INAddMediaIntent#from(payload) reattaching forwarded SFA signals: %s"
+ "INPlayMediaIntent#from(payload) reattaching forwarded SFA signals: %s"
+ "UpdateMediaAffinityFlowStrategy#makeIntentFromParse reattaching forwarded SFA signals: %s"
+ "internalSignalsFromSiriAudio"
+ "originalPlayMediaIntent"
+ "topicSwitchDetected"
- "ExecuteMusicOnRemoteFlow#execute remote request is waiting on user input. But follow ups are not currently supported by this flow. Returning .complete()"
```
