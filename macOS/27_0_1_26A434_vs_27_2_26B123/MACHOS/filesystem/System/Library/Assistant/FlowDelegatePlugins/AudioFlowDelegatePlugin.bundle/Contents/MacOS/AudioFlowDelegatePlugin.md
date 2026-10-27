## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/MacOS/AudioFlowDelegatePlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-3600.33.17.0.0
-  __TEXT.__text: 0x262f44
-  __TEXT.__auth_stubs: 0x6520
-  __TEXT.__objc_stubs: 0x2680
+3605.24.1.0.0
+  __TEXT.__text: 0x268e7c
+  __TEXT.__auth_stubs: 0x6560
+  __TEXT.__objc_stubs: 0x26a0
   __TEXT.__objc_methlist: 0x580
-  __TEXT.__const: 0xbb2a
+  __TEXT.__const: 0xbbaa
   __TEXT.__cstring: 0x448c
-  __TEXT.__swift5_typeref: 0x4100
-  __TEXT.__oslogstring: 0x1dcf7
-  __TEXT.__constg_swiftt: 0x58a0
+  __TEXT.__swift5_typeref: 0x417a
+  __TEXT.__oslogstring: 0x1e237
+  __TEXT.__constg_swiftt: 0x58f0
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x3ecb
+  __TEXT.__swift5_reflstr: 0x3f0b
   __TEXT.__swift5_assocty: 0xa60
-  __TEXT.__swift5_proto: 0x6f0
+  __TEXT.__swift5_proto: 0x6fc
   __TEXT.__swift5_types: 0x398
   __TEXT.__objc_classname: 0x1c69
-  __TEXT.__objc_methname: 0x3a2d
+  __TEXT.__objc_methname: 0x3a6d
   __TEXT.__objc_methtype: 0x4ea
-  __TEXT.__swift5_fieldmd: 0x34a8
-  __TEXT.__swift5_capture: 0x5434
+  __TEXT.__swift5_fieldmd: 0x34dc
+  __TEXT.__swift5_capture: 0x54f8
   __TEXT.__swift_as_entry: 0x180
   __TEXT.__swift_as_ret: 0x21c
   __TEXT.__swift_as_cont: 0x1b0
-  __TEXT.__swift5_protos: 0x6c
+  __TEXT.__swift5_protos: 0x70
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4730
-  __TEXT.__eh_frame: 0x3268
-  __DATA_CONST.__const: 0xdec0
+  __TEXT.__unwind_info: 0x4768
+  __TEXT.__eh_frame: 0x32b8
+  __DATA_CONST.__const: 0xe040
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0x3298
-  __DATA_CONST.__got: 0x1c20
-  __DATA_CONST.__auth_ptr: 0x19b0
-  __DATA.__objc_const: 0x8020
-  __DATA.__objc_selrefs: 0xb38
+  __DATA_CONST.__auth_got: 0x32b8
+  __DATA_CONST.__got: 0x1c28
+  __DATA_CONST.__auth_ptr: 0x19b8
+  __DATA.__objc_const: 0x8080
+  __DATA.__objc_selrefs: 0xb40
   __DATA.__objc_data: 0x1258
-  __DATA.__data: 0xb8c8
+  __DATA.__data: 0xb8f0
   __DATA.__bss: 0xc610
   __DATA.__common: 0x440
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5441
+  Functions: 5462
   Symbols:   311
-  CStrings:  2562
+  CStrings:  2577
 
CStrings:
+ "AmbiguousPlayFlow#execute self deallocated prematurely during SiriForAirPlayFlow setup, completing"
+ "ContinueInAppPunchOutStrategy#homeAccessoryContinuation cannot continue on the accessory, handling locally. hasAppIdentifier: %{bool,public}d, handledBySiriForAirPlay: %{bool,public}d, hasAssistantID: %{bool,public}d"
+ "ContinueInAppPunchOutStrategy#homeAccessoryContinuation originIsHomeAccessory: %{bool,public}d, isPumpkin: %{bool,public}d"
+ "ContinueInAppPunchOutStrategy#makeContinueInAppAutoPunchOutResponse launchAppCommand %@, appBundleId %s"
+ "ContinueInAppPunchOutStrategy#makeContinueInAppAutoPunchOutResponse remote assistantId %s, eor %@"
+ "ContinueInAppPunchOutStrategy#requireUnlock requireUnlock: %{bool}d"
+ "ExecuteMusicOnRemoteFlow#execute isFollowUpTurn: %{bool}d"
+ "ExecuteMusicOnRemoteFlow#execute remote request completed with topicSwitchDetected. Will return .unhandled(reason: .needsExecutionRerun)"
+ "ExecuteMusicOnRemoteFlow#execute remote request is waiting on user input. Will return .ongoing(requireInput: true)"
+ "Parse#getSiriKitIntent Constructing INAddMediaIntent from addMediaSiriKitFallback"
+ "Parse#getSiriKitIntent Constructing INPlayMediaIntent from playMediaSiriKitFallback"
+ "Parse#getSiriKitIntent Constructing INUpdateMediaAffinityIntent from updateMediaAffinitySiriKitFallback"
+ "ResponseFactory+Utilities#effectiveResponseMode forcing .voiceOnly for SFA Now Playing (was %s)"
+ "deviceState"
+ "originalPlayMediaIntent"
+ "topicSwitchDetected"
- "ExecuteMusicOnRemoteFlow#execute remote request is waiting on user input. But follow ups are not currently supported by this flow. Returning .complete()"
```
