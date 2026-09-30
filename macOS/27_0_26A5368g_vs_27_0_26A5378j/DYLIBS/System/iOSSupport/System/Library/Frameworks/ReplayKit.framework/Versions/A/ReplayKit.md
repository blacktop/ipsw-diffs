## ReplayKit

> `/System/iOSSupport/System/Library/Frameworks/ReplayKit.framework/Versions/A/ReplayKit`

```diff

-  __TEXT.__text: 0x2a490
-  __TEXT.__objc_methlist: 0x2f58
-  __TEXT.__const: 0x138
-  __TEXT.__oslogstring: 0x3d78
-  __TEXT.__cstring: 0x6575
+  __TEXT.__text: 0x2a610
+  __TEXT.__objc_methlist: 0x2f80
+  __TEXT.__const: 0x140
+  __TEXT.__oslogstring: 0x3dd6
+  __TEXT.__cstring: 0x6609
   __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__unwind_info: 0x9e0
+  __TEXT.__unwind_info: 0xa08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bd8
+  __DATA_CONST.__objc_selrefs: 0x1be8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x3b8
   __AUTH_CONST.__const: 0xd58
-  __AUTH_CONST.__cfstring: 0x19c0
+  __AUTH_CONST.__cfstring: 0x1a00
   __AUTH_CONST.__objc_const: 0x5bd8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1198
-  Symbols:   2977
-  CStrings:  1047
+  Functions: 1203
+  Symbols:   2982
+  CStrings:  1053
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[RPBroadcastController finishSystemBroadcastWithSessionInfo:handler:]
+ -[RPDaemonProxy stopHQLRWithSessionInfo:handler:]
+ -[RPDaemonProxy stopSystemBroadcastWithSessionInfo:handler:]
+ -[RPDaemonProxy stopSystemRecordingWithSessionInfo:handler:]
+ -[RPScreenRecorder stopHQLRWithSessionInfo:handler:]
+ -[RPScreenRecorder stopSystemBroadcastWithSessionInfo:handler:]
+ -[RPScreenRecorder stopSystemRecordingWithSessionInfo:handler:]
+ GCC_except_table141
+ __49-[RPDaemonProxy stopHQLRWithSessionInfo:handler:]_block_invoke
+ __60-[RPDaemonProxy stopSystemBroadcastWithSessionInfo:handler:]_block_invoke
+ __60-[RPDaemonProxy stopSystemRecordingWithSessionInfo:handler:]_block_invoke
+ ___49-[RPDaemonProxy stopHQLRWithSessionInfo:handler:]_block_invoke
+ ___52-[RPScreenRecorder stopHQLRWithSessionInfo:handler:]_block_invoke
+ ___60-[RPDaemonProxy stopSystemBroadcastWithSessionInfo:handler:]_block_invoke
+ ___60-[RPDaemonProxy stopSystemRecordingWithSessionInfo:handler:]_block_invoke
+ ___63-[RPScreenRecorder stopSystemBroadcastWithSessionInfo:handler:]_block_invoke
+ ___63-[RPScreenRecorder stopSystemRecordingWithSessionInfo:handler:]_block_invoke
+ ___70-[RPBroadcastController finishSystemBroadcastWithSessionInfo:handler:]_block_invoke
+ _objc_msgSend$finishSystemBroadcastWithSessionInfo:handler:
+ _objc_msgSend$stopHQLRWithSessionInfo:handler:
+ _objc_msgSend$stopSystemBroadcastWithSessionInfo:handler:
+ _objc_msgSend$stopSystemRecordingWithSessionInfo:handler:
- -[RPDaemonProxy stopHQLRWithHandler:]
- -[RPDaemonProxy stopSystemBroadcastWithHandler:]
- -[RPDaemonProxy stopSystemRecordingWithHandler:]
- GCC_except_table135
- __37-[RPDaemonProxy stopHQLRWithHandler:]_block_invoke
- __48-[RPDaemonProxy stopSystemBroadcastWithHandler:]_block_invoke
- __48-[RPDaemonProxy stopSystemRecordingWithHandler:]_block_invoke
- ___29-[RPScreenRecorder stopHQLR:]_block_invoke
- ___37-[RPDaemonProxy stopHQLRWithHandler:]_block_invoke
- ___40-[RPScreenRecorder stopSystemRecording:]_block_invoke
- ___48-[RPDaemonProxy stopSystemBroadcastWithHandler:]_block_invoke
- ___48-[RPDaemonProxy stopSystemRecordingWithHandler:]_block_invoke
- ___51-[RPScreenRecorder stopSystemBroadcastWithHandler:]_block_invoke
- ___58-[RPBroadcastController finishSystemBroadcastWithHandler:]_block_invoke
- _objc_msgSend$stopHQLRWithHandler:
- _objc_msgSend$stopSystemBroadcastWithHandler:
- _objc_msgSend$stopSystemRecordingWithHandler:
CStrings:
+ "-[RPScreenRecorder stopHQLRWithSessionInfo:handler:]"
+ "-[RPScreenRecorder stopSystemBroadcastWithSessionInfo:handler:]"
+ "-[RPScreenRecorder stopSystemRecordingWithSessionInfo:handler:]"
+ "RECORDING_ERROR_FAILED_TO_START_HIGH_QUALITY_RECORDING"
+ "RECORDING_ERROR_TIME_LIMIT_REACHED"
+ "RPDaemonProxy: stopHQLRWithSessionInfo: proxy error: %d"
+ "RPDaemonProxy: stopHQLRWithSessionInfo:%@"
+ "RPDaemonProxy: stopSystemBroadcastWithSessionInfo: proxy error: %d"
+ "RPDaemonProxy: stopSystemBroadcastWithSessionInfo:%@"
+ "RPDaemonProxy: stopSystemRecordingWithSessionInfo: proxy error: %d"
+ "RPDaemonProxy: stopSystemRecordingWithSessionInfo:%@"
- "-[RPScreenRecorder stopHQLR:]"
- "-[RPScreenRecorder stopSystemBroadcastWithHandler:]"
- "-[RPScreenRecorder stopSystemRecording:]"
- "RPDaemonProxy: stopSystemBroadcastWithHandler: proxy error: %d"
- "RPDaemonProxy: stopSystemBroadcastWithHandler:withHandler:"
- "RPDaemonProxy: stopSystemRecordingWithHandler: proxy error: %d"
- "RPDaemonProxy: stopSystemRecordingWithHandler:withHandler:"

```
