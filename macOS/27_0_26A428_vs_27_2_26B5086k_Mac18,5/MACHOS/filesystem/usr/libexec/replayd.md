## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-740.62.1.0.0
-  __TEXT.__text: 0xc530c
+765.9.1.0.0
+  __TEXT.__text: 0xc6ca4
   __TEXT.__auth_stubs: 0x1b10
-  __TEXT.__objc_stubs: 0xed00
-  __TEXT.__objc_methlist: 0x75ac
+  __TEXT.__objc_stubs: 0xeee0
+  __TEXT.__objc_methlist: 0x768c
   __TEXT.__const: 0x430
-  __TEXT.__oslogstring: 0x15545
-  __TEXT.__cstring: 0x17324
+  __TEXT.__oslogstring: 0x158ef
+  __TEXT.__cstring: 0x17461
   __TEXT.__objc_classname: 0xacb
-  __TEXT.__objc_methname: 0x1618d
-  __TEXT.__objc_methtype: 0x40dd
+  __TEXT.__objc_methname: 0x1636a
+  __TEXT.__objc_methtype: 0x40d8
   __TEXT.__gcc_except_tab: 0xfe4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x33e0
-  __DATA_CONST.__const: 0x2900
-  __DATA_CONST.__cfstring: 0x6380
+  __TEXT.__unwind_info: 0x3460
+  __DATA_CONST.__const: 0x2950
+  __DATA_CONST.__cfstring: 0x63a0
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__auth_got: 0xd98
   __DATA_CONST.__got: 0xd08
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x11180
-  __DATA.__objc_selrefs: 0x4668
-  __DATA.__objc_ivar: 0xde8
+  __DATA.__objc_const: 0x111f8
+  __DATA.__objc_selrefs: 0x46e0
+  __DATA.__objc_ivar: 0xdf0
   __DATA.__objc_data: 0x1cc0
   __DATA.__data: 0xc98
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3752
+  Functions: 3787
   Symbols:   848
-  CStrings:  7410
+  CStrings:  7445
 
Symbols:
+ __exit
- _notify_register_check
CStrings:
+ " [ERROR] %{public}s:%d RPConnectionManager: SIGTERM cleanup window elapsed, exiting cleanly"
+ " [ERROR] %{public}s:%d failed to create SCPreviewSession for previewID=%@"
+ " [ERROR] %{public}s:%d failed to stop own session"
+ " [ERROR] %{public}s:%d maximum preview count (%lu) reached for previewContent=%d"
+ " [ERROR] %{public}s:%d missing or malformed previewID in previewConfig (got %@)"
+ " [ERROR] %{public}s:%d no client found for %{public}@, nothing to stop"
+ " [ERROR] %{public}s:%d no preview found for previewID=%@ content=%d"
+ " [ERROR] %{public}s:%d previewID=%@ already exists for previewContent=%d"
+ " [ERROR] %{public}s:%d stopAllActiveClients rejected: unentitled caller pid %d claims to be Control Center"
+ " [ERROR] %{public}s:%d stopAllActiveClients: caller pid %d lacks system recording entitlement, scoping stop to its own sessions"
+ " [ERROR] %{public}s:%d unsupported previewContent=%d"
+ " [INFO] %{public}s:%d Stopped recording due to display change, outputURL: %@ error: %@"
+ " [INFO] %{public}s:%d stop own session success"
+ "-[RPConnectionManager handleSIGTERMWithExitAfter:exitBlock:]"
+ "-[RPConnectionManager handleSIGTERMWithExitAfter:exitBlock:]_block_invoke"
+ "-[RPConnectionManager stopAllActiveClients]"
+ "-[RPRecordingManager stopActiveSessionForClientWithBundleID:]"
+ "-[RPRecordingManager stopActiveSessionForClientWithBundleID:]_block_invoke"
+ "RPConnectionManager: stopAllActiveClients completed for the calling client only"
+ "RPConnectionManager: stopAllActiveClientsInternal"
+ "RPConnectionManager: stopAllActiveClientsInternal completed"
+ "T@\"NSUUID\",R,N,V_previewID"
+ "T@\"SCClipSession\",&,V_clipSession"
+ "_cameraPreviewSessions"
+ "_displayFrameOnCameraPreviewSessions:"
+ "_displayFrameOnScreenPreviewSessions:"
+ "_screenPreviewSessions"
+ "_screenStreamsLock"
+ "_stopAndRemoveAllPreviewSessions"
+ "clipSession"
+ "com.screenCaptureKit.previewUpdateQueue.%@"
+ "elapsedClipBufferingSeconds"
+ "getStreamWithStreamID:"
+ "getStreamsSnapshot"
+ "handleSIGTERM"
+ "handleSIGTERMWithExitAfter:exitBlock:"
+ "initWithUUIDString:"
+ "previewID"
+ "removeStreamWithStreamID:"
+ "setClipSession:"
+ "setStream:withStreamID:"
+ "stopActiveSessionForClientWithBundleID:"
+ "stopAllActiveClientsInternal"
+ "v24@?0@\"NSError\"8Q16"
+ "v32@0:8d16@?24"
- " [ERROR] %{public}s:%d failed to start previewContent=%d alreadyStarted=%d"
- " [ERROR] %{public}s:%d failed to stop previewContent=%d alreadyStopped=%d"
- " [INFO] %{public}s:%d Stopped recording due to display change"
- "@\"SCPreviewSession\""
- "RPConnectionManager: stopAllActiveClients completed"
- "RPDaemonRun_block_invoke"
- "_cameraPreviewSession"
- "_screenPreviewSession"
- "com.screenCaptureKit.previewUpdateQueue"
- "valueForKey:"
```
