## PCCAgentClientExtension

> `/System/Library/ExtensionKit/Extensions/PCCAgentClientExtension.appex/PCCAgentClientExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-47.0.0.0.0
-  __TEXT.__text: 0x2c650
-  __TEXT.__auth_stubs: 0x12b0
+55.2.1.0.0
+  __TEXT.__text: 0x32d6c
+  __TEXT.__auth_stubs: 0x1500
   __TEXT.__objc_stubs: 0x120
-  __TEXT.__const: 0xcd2
-  __TEXT.__swift5_typeref: 0x443
-  __TEXT.__oslogstring: 0x18a2
-  __TEXT.__swift5_reflstr: 0x1e8
+  __TEXT.__const: 0xd60
+  __TEXT.__swift5_typeref: 0x461
+  __TEXT.__cstring: 0x85d
+  __TEXT.__oslogstring: 0x1c83
+  __TEXT.__swift5_reflstr: 0x238
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__constg_swiftt: 0x390
-  __TEXT.__swift5_fieldmd: 0x25c
+  __TEXT.__constg_swiftt: 0x3c0
+  __TEXT.__swift5_fieldmd: 0x28c
   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__swift_as_entry: 0xb0
-  __TEXT.__swift_as_ret: 0xb0
-  __TEXT.__swift_as_cont: 0x1a4
+  __TEXT.__swift_as_entry: 0xb8
+  __TEXT.__swift_as_ret: 0xbc
+  __TEXT.__swift_as_cont: 0x220
   __TEXT.__objc_classname: 0x1dd
-  __TEXT.__objc_methname: 0x11c
+  __TEXT.__objc_methname: 0x1cb
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__cstring: 0x78e
   __TEXT.__swift5_capture: 0x114
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x8a8
-  __TEXT.__eh_frame: 0x1f90
+  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__eh_frame: 0x2480
   __DATA_CONST.__const: 0x550
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x960
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__auth_ptr: 0x388
-  __DATA.__objc_const: 0x5e0
+  __DATA_CONST.__auth_got: 0xa88
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__auth_ptr: 0x398
+  __DATA.__objc_const: 0x660
   __DATA.__objc_selrefs: 0x48
   __DATA.__objc_data: 0x138
-  __DATA.__data: 0x9f8
+  __DATA.__data: 0xab0
   __DATA.__bss: 0xa80
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 440
-  Symbols:   135
-  CStrings:  181
+  Functions: 499
+  Symbols:   141
+  CStrings:  210
 
Symbols:
+ _objc_retain_x27
+ _swift_allocBox
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRetain_n
+ _swift_projectBox
+ _swift_release_x22
+ _swift_retain_x22
- _objc_retain_x26
CStrings:
+ "%s %s value %ld does not fit pid_t; using -1 sentinel"
+ "%s could not get handle for pid %d"
+ "%s could not get identifier for pid %d"
+ "%s could not get process bundle for pid=%d"
+ "%s daemon %s for pid=%d is not allowed"
+ "%s is bundle-id %s for pid %d"
+ "%{public}s"
+ "Background task cancelled during close(). elapsed=%s"
+ "Cancelling background connection task (if any)..."
+ "Emitted Request.MediaDecoderMetrics"
+ "Emitted RequestOutcome status=%{public}s reason=%{public}s"
+ "FinalResponse.Received"
+ "PCCAgent prewarmHint: already warm session=%s"
+ "PCCAgent prewarmHint: connection warm-up failed error=%@"
+ "PCCAgent prewarmHint: prefetch attestations for session=%s"
+ "PCCAgent prewarmHint: session=%s"
+ "PCCAgent prewarmHint: warmed connection for session=%s"
+ "Request.MediaDecoderMetrics"
+ "RequestOneShot"
+ "RequestOutcome"
+ "RequestStream"
+ "RequestStream.Finished"
+ "Reusing prewarmed connection for session=%s"
+ "Taskgroup for infinite read and write cancelled. elapsed=%s"
+ "Unexpected error in background task during close(). elapsed=%s error=%@"
+ "[Error] Interval already ended"
+ "auditToken"
+ "close() ignored; already %s."
+ "completionReason: %s"
+ "isClaimed"
+ "onBehalfOfPID"
+ "parentOfOnBehalfOfPID"
+ "part %ld/%ld\n%{public}s"
+ "responseCount: %ld"
+ "sessionUUID: %s"
+ "status=%{public, signpost.description=attribute,public}s, reason=%{public, signpost.description=attribute,public}s"
- "%s could not get handle for pid %ld"
- "%s could not get identifier for pid %ld"
- "%s could not get process bundle for pid=%ld"
- "%s daemon %s for pid=%ld is not allowed"
- "%s is bundle-id %s for pid %ld"
- "Index: %ld, %s"
- "PCCAgent start completePrewarm: with %s"
```
