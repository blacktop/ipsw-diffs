## SiriGestureBridge

> `/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge`

```diff

-3402.6.1.0.0
-  __TEXT.__text: 0x1ce28
-  __TEXT.__auth_stubs: 0x15c0
+3402.12.1.0.0
+  __TEXT.__text: 0x1d314
+  __TEXT.__auth_stubs: 0x1350
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x7f2
-  __TEXT.__cstring: 0xe54
-  __TEXT.__constg_swiftt: 0xb10
-  __TEXT.__swift5_typeref: 0x3cb
-  __TEXT.__swift5_reflstr: 0x648
-  __TEXT.__swift5_fieldmd: 0x444
-  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__const: 0x792
+  __TEXT.__cstring: 0xe24
+  __TEXT.__swift5_typeref: 0x39b
+  __TEXT.__oslogstring: 0x2697
+  __TEXT.__constg_swiftt: 0xa60
+  __TEXT.__swift5_reflstr: 0x608
+  __TEXT.__swift5_fieldmd: 0x3f4
+  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__oslogstring: 0x2437
-  __TEXT.__swift5_capture: 0x15c
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_capture: 0x148
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x650
-  __TEXT.__eh_frame: 0x1a0
+  __TEXT.__unwind_info: 0x640
+  __TEXT.__eh_frame: 0x1c0
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0xa91
-  __TEXT.__objc_methtype: 0x66d
-  __DATA_CONST.__got: 0x288
+  __TEXT.__objc_methname: 0xb1a
+  __TEXT.__objc_methtype: 0x6b0
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x168
+  __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0xae0
-  __AUTH_CONST.__auth_ptr: 0x360
-  __AUTH_CONST.__const: 0xee8
-  __AUTH_CONST.__objc_const: 0x10d8
+  __AUTH_CONST.__auth_got: 0x9a8
+  __AUTH_CONST.__auth_ptr: 0x338
+  __AUTH_CONST.__const: 0xd98
+  __AUTH_CONST.__objc_const: 0x10b0
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0xb8
-  __DATA.__data: 0x400
+  __AUTH.__data: 0xc0
+  __DATA.__data: 0x3a0
   __DATA.__bss: 0x800
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x648
-  __DATA_DIRTY.__data: 0x4b0
-  __DATA_DIRTY.__common: 0x190
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0x618
+  __DATA_DIRTY.__data: 0x4d0
+  __DATA_DIRTY.__common: 0x188
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 743
-  Symbols:   426
-  CStrings:  452
+  Functions: 734
+  Symbols:   419
+  CStrings:  462
 
Symbols:
+ _AVAudioSessionModeDefault
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _swift_allocateGenericClassMetadata
- _swift_checkMetadataState
- _swift_getGenericMetadata
CStrings:
+ "Handling StartChildLocalRequestMessage: %!s(MISSING)"
+ "No pending gesture response to create RC"
+ "Pending: Gesture requestId: %!s(MISSING), Gesture response: %!s(MISSING)"
+ "category"
+ "categoryOptions"
+ "currentLocationWithFetchRequest:completion:"
+ "deactivateAudioSessionIfNoActiveAssertions"
+ "isOtherAudioPlaying"
+ "mode"
+ "pendingGestureRequestId"
+ "pendingGestureResponse"
+ "v32@0:8@\"AFLocationFetchRequest\"16@?<v@?@\"CLLocation\"@\"NSError\">24"
+ "‼️ Gesture response is for IFGestureBasedCandidateMessage"
+ "‼️ Gesture response is not for IFGestureBasedCandidateMessage"
+ "‼️ Gesture response is pending, but this is not the request"
+ "✅ Gesture activation request has begun, posting gesture RC"
+ "🆔 Request started with requestId: %!s(MISSING), rootRequestId: %!s(MISSING), pendingGestureRequestId: %!s(MISSING)"
+ "🔊 Audio Session (%!u(MISSING)) is not configured"
+ "🔊 Audio Session Fallback (%!l(MISSING)d, %!s(MISSING), %!s(MISSING)) is active and ready for playback"
+ "🔊 Audio session (%!u(MISSING)) is active and ready for playback, no other audio is playing"
+ "🔊 Audio session (%!u(MISSING), %!s(MISSING), %!s(MISSING))) is ready for playback with categoryOptions: %!l(MISSING)u"
+ "🔊 Audio session (%!u(MISSING), %!s(MISSING), %!s(MISSING))) is ready for playback, no other audio is playing and the mode is configured"
+ "🔊 Audio session is still active, releasing it if no other client is using it"
+ "🔊 Will wait for audio session to be configured for announcement to prevent premature audio session actvation"
+ "🫨 HGManager has fully stopped"
- "Gesture activation request has begun, posting gesture RC"
- "Gesture activation request has begun, posting gesture candidate for planner"
- "Gesture requestId: %!s(MISSING)"
- "Incorrect requestId: %!s(MISSING) to post %!s(MISSING)"
- "No pending gesture response to post for planner"
- "Request started with requestId: %!s(MISSING)"
- "_requestContextData"
- "lock"
- "pendingGestureRC"
- "pendingIFGestureCandidate"
- "value"
- "🗣️ RequestContextData is nil"
- "🗣️ RequestContextData is unavailable, assuming the request is no or supplemental dialog"
- "🗣️ RequestMode is unavailable, assuming the request is no or supplemental dialog"
- "🗣️ Response mode: %!s(MISSING)"

```
