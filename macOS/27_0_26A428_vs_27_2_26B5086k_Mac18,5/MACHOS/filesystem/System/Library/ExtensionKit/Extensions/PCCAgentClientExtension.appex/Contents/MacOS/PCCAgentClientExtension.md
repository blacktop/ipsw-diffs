## PCCAgentClientExtension

> `/System/Library/ExtensionKit/Extensions/PCCAgentClientExtension.appex/Contents/MacOS/PCCAgentClientExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0x31404
-  __TEXT.__auth_stubs: 0x1300
+62.0.0.0.0
+  __TEXT.__text: 0x36414
+  __TEXT.__auth_stubs: 0x15a0
   __TEXT.__objc_stubs: 0x120
-  __TEXT.__const: 0xd30
-  __TEXT.__swift5_typeref: 0x45d
-  __TEXT.__cstring: 0x8fd
-  __TEXT.__oslogstring: 0x1cb3
-  __TEXT.__swift5_reflstr: 0x228
+  __TEXT.__const: 0xd90
+  __TEXT.__swift5_typeref: 0x4c7
+  __TEXT.__oslogstring: 0x2053
+  __TEXT.__cstring: 0x92d
+  __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__constg_swiftt: 0x3a0
-  __TEXT.__swift5_fieldmd: 0x280
+  __TEXT.__constg_swiftt: 0x428
+  __TEXT.__swift5_fieldmd: 0x2b0
   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__swift_as_entry: 0xb8
-  __TEXT.__swift_as_ret: 0xbc
-  __TEXT.__swift_as_cont: 0x210
+  __TEXT.__swift_as_entry: 0xc0
+  __TEXT.__swift_as_ret: 0xc4
+  __TEXT.__swift_as_cont: 0x240
   __TEXT.__objc_classname: 0x1dd
-  __TEXT.__objc_methname: 0x1bb
+  __TEXT.__objc_methname: 0x201
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__swift5_capture: 0x114
+  __TEXT.__swift5_capture: 0x150
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xa90
-  __TEXT.__eh_frame: 0x2390
-  __DATA_CONST.__const: 0x558
+  __TEXT.__unwind_info: 0xb30
+  __TEXT.__eh_frame: 0x2518
+  __DATA_CONST.__const: 0x5d0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x988
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__auth_ptr: 0x398
-  __DATA.__objc_const: 0x640
+  __DATA_CONST.__auth_got: 0xad8
+  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__auth_ptr: 0x3d0
+  __DATA.__objc_const: 0x6c0
   __DATA.__objc_selrefs: 0x48
   __DATA.__objc_data: 0x138
-  __DATA.__data: 0xa80
+  __DATA.__data: 0xbc8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 495
-  Symbols:   107
-  CStrings:  215
+  Functions: 529
+  Symbols:   110
+  CStrings:  230
 
Symbols:
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
CStrings:
+ "AIR inference report. requestID=%{public}s succeeded=%{bool,public}d latencySeconds=%{public}f"
+ "Cancelling the background connection task immediately; reason=%s."
+ "Closing LongLivedConnection; teardown=%s previousState=%s. elapsed=%s"
+ "Connection completed and streams finished"
+ "Emitted AIR inference event. requestID=%{public}s"
+ "Failed to emit AppleIntelligence inference event: %@"
+ "Failed to initialize AppleIntelligenceReporting.EventReporter: %@"
+ "Fresh connection went terminal before it could be claimed. session=%s"
+ "LongLivedConnection close() finished. elapsed=%s"
+ "PCC request already wound down before close(); nothing to cancel."
+ "PCC request already wound down before close(); nothing to watch."
+ "PCC request did not wind down within the grace period after close(); cancelling the background task as a last resort. This surfaces as cancellationReason=frameworkCancellation in PCC telemetry."
+ "PCC request wound down after close(). elapsed=%s"
+ "PCC request wound down on its own; no cancellation needed."
+ "backgroundWorkFinished"
+ "didSendRequest"
+ "isClaimed"
+ "teardownWatchdog"
- "Cancelling background connection task (if any)..."
- "Closing LongLivedConnection... currentState=%s"
- "LongLivedConnection closed successfully. elapsed=%s"
```
