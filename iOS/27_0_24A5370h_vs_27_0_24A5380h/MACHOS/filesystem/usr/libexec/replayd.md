## replayd

> `/usr/libexec/replayd`

```diff

-  __TEXT.__text: 0xb717c
+  __TEXT.__text: 0xb790c
   __TEXT.__auth_stubs: 0x1900
-  __TEXT.__objc_stubs: 0xef20
-  __TEXT.__objc_methlist: 0x7308
+  __TEXT.__objc_stubs: 0xefa0
+  __TEXT.__objc_methlist: 0x7350
   __TEXT.__const: 0x3e4
-  __TEXT.__gcc_except_tab: 0xf18
-  __TEXT.__objc_methname: 0x15b0d
-  __TEXT.__oslogstring: 0x15c93
-  __TEXT.__cstring: 0x177bd
+  __TEXT.__gcc_except_tab: 0xf24
+  __TEXT.__objc_methname: 0x15be0
+  __TEXT.__oslogstring: 0x15e09
+  __TEXT.__cstring: 0x17846
   __TEXT.__objc_classname: 0xa44
-  __TEXT.__objc_methtype: 0x4357
-  __TEXT.__unwind_info: 0x2280
+  __TEXT.__objc_methtype: 0x439b
+  __TEXT.__unwind_info: 0x2298
   __DATA_CONST.__const: 0x29e0
-  __DATA_CONST.__cfstring: 0x5c20
+  __DATA_CONST.__cfstring: 0x5c80
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0xc90
-  __DATA_CONST.__got: 0xbe0
+  __DATA_CONST.__got: 0xc80
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x111f0
-  __DATA.__objc_selrefs: 0x4630
-  __DATA.__objc_ivar: 0xd60
+  __DATA.__objc_const: 0x11248
+  __DATA.__objc_selrefs: 0x4658
+  __DATA.__objc_ivar: 0xd68
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0xe54
   __DATA.__bss: 0x258

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3606
-  Symbols:   798
-  CStrings:  8044
+  Functions: 3613
+  Symbols:   799
+  CStrings:  8065
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _NSUnderlyingErrorKey
CStrings:
+ " [ERROR] %{public}s:%d Unexpected FVD start failure status %d, falling back to generic FailedToStart"
+ " [ERROR] %{public}s:%d getSystemBroadcastExtensionInfo rejected: caller lacks system recording entitlement"
+ " [ERROR] %{public}s:%d getSystemBroadcastPickerInfo rejected: caller lacks system recording entitlement"
+ " [ERROR] %{public}s:%d status: %d, error: %@"
+ " [INFO] %{public}s:%d Ignoring display change for HQLR recording"
+ " [INFO] %{public}s:%d sessionInfo=%@"
+ "-[RPClient stopHQLRWithSessionInfo:handler:]"
+ "-[RPClient stopHQLRWithSessionInfo:handler:]_block_invoke"
+ "-[RPClient stopSystemBroadcastWithSessionInfo:handler:]"
+ "-[RPClient stopSystemBroadcastWithSessionInfo:handler:]_block_invoke"
+ "-[RPClient stopSystemRecordingWithSessionInfo:handler:]"
+ "-[RPClient stopSystemRecordingWithSessionInfo:handler:]_block_invoke"
+ "-[RPConnectionManager getSystemBroadcastExtensionInfo:]"
+ "-[RPConnectionManager stopHQLRWithSessionInfo:handler:]"
+ "-[RPConnectionManager stopSystemRecordingWithSessionInfo:handler:]"
+ "-[RPScreenCaptureManagerIOS _handleFVDStartFailureWithErrorStatus:error:]"
+ "-[RPScreenCaptureManagerIOS screenCaptureController:didFailWithStatus:error:]"
+ "CTYP"
+ "RECORDING_ERROR_TIME_LIMIT_REACHED"
+ "RPConnectionManager: stopHQLRWithSessionInfo completed"
+ "RPConnectionManager: stopSystemBroadcastWithSessionInfo"
+ "RPConnectionManager: stopSystemBroadcastWithSessionInfo completed"
+ "RPConnectionManager: stopSystemRecordingWithSessionInfo completed"
+ "STPS"
+ "Tq,N,V_stopSource"
+ "_castingSessionIDs"
+ "_handleFVDStartFailureWithErrorStatus:error:"
+ "_stopSource"
+ "notifyScreenCaptureStateChanged:"
+ "screenCaptureController:didFailWithStatus:error:"
+ "serviceNameSupportsStopSource"
+ "setStopSource:"
+ "stopHQLRWithSessionInfo:handler:"
+ "stopSource"
+ "stopSourceForEndReason:"
+ "stopSystemBroadcastWithSessionInfo:handler:"
+ "stopSystemRecordingWithSessionInfo:handler:"
+ "v28@0:8i16@20"
+ "v36@0:8@\"FigScreenCaptureController\"16i24@\"NSError\"28"
- " [ERROR] %{public}s:%d status: %d"
- " [INFO] %{public}s:%d Stopped HQLR recording due to display change"
- "-[RPClient stopHQLRSessionWithHandler:]"
- "-[RPClient stopHQLRSessionWithHandler:]_block_invoke"
- "-[RPClient stopSystemBroadcastSessionWithHandler:]"
- "-[RPClient stopSystemBroadcastSessionWithHandler:]_block_invoke"
- "-[RPClient stopSystemRecordingSessionWithHandler:]"
- "-[RPClient stopSystemRecordingSessionWithHandler:]_block_invoke"
- "-[RPConnectionManager stopHQLRWithHandler:]"
- "-[RPConnectionManager stopSystemRecordingWithHandler:]"
- "-[RPScreenCaptureManagerIOS _handleFVDStartFailureWithErrorStatus:]"
- "-[RPScreenCaptureManagerIOS screenCaptureController:didFailWithStatus:]"
- "RECORDING_ERROR_FAILED_TO_START_LIGHTING"
- "RPConnectionManager: stopHQLRWithHandler completed"
- "RPConnectionManager: stopSystemBroadcastWithHandler"
- "RPConnectionManager: stopSystemBroadcastWithHandler completed"
- "RPConnectionManager: stopSystemRecordingWithHandler completed"
- "_handleFVDStartFailureWithErrorStatus:"
- "stopHQLRSessionWithHandler:"
- "stopHQLRWithHandler:"
- "stopSystemBroadcastSessionWithHandler:"
- "stopSystemRecordingSessionWithHandler:"

```
