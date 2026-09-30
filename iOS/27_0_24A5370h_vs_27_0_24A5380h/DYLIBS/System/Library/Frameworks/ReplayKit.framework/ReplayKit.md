## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

```diff

-  __TEXT.__text: 0x361a8
-  __TEXT.__objc_methlist: 0x3600
+  __TEXT.__text: 0x36460
+  __TEXT.__objc_methlist: 0x3630
   __TEXT.__const: 0x158
-  __TEXT.__oslogstring: 0x569a
-  __TEXT.__cstring: 0x800a
+  __TEXT.__oslogstring: 0x5720
+  __TEXT.__cstring: 0x80eb
   __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__unwind_info: 0xbd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2118
+  __DATA_CONST.__objc_selrefs: 0x2130
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x4d0
   __AUTH_CONST.__const: 0xe18
-  __AUTH_CONST.__cfstring: 0x1e60
+  __AUTH_CONST.__cfstring: 0x1ec0
   __AUTH_CONST.__objc_const: 0x66e8
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x5c0
-  __AUTH.__objc_data: 0x8c0
   __DATA.__objc_ivar: 0x2e4
   __DATA.__data: 0xba8
   __DATA.__bss: 0xc8
-  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1404
-  Symbols:   4903
-  CStrings:  1328
+  Functions: 1409
+  Symbols:   4911
+  CStrings:  1337
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
Symbols:
+ -[RPBroadcastController finishSystemBroadcastWithSessionInfo:handler:]
+ -[RPControlCenterClient stopHQLRRecordingWithStopSource:handler:]
+ -[RPControlCenterClient stopSystemRecordingWithStopSource:handler:]
+ -[RPDaemonProxy stopHQLRWithSessionInfo:handler:]
+ -[RPDaemonProxy stopSystemBroadcastWithSessionInfo:handler:]
+ -[RPDaemonProxy stopSystemRecordingWithSessionInfo:handler:]
+ -[RPScreenRecorder stopHQLRWithSessionInfo:handler:]
+ -[RPScreenRecorder stopSystemBroadcastWithSessionInfo:handler:]
+ -[RPScreenRecorder stopSystemRecordingWithSessionInfo:handler:]
+ _OBJC_CLASS_$_NSConstantDictionary
+ ___49-[RPDaemonProxy stopHQLRWithSessionInfo:handler:]_block_invoke
+ ___52-[RPScreenRecorder stopHQLRWithSessionInfo:handler:]_block_invoke
+ ___60-[RPDaemonProxy stopSystemBroadcastWithSessionInfo:handler:]_block_invoke
+ ___60-[RPDaemonProxy stopSystemRecordingWithSessionInfo:handler:]_block_invoke
+ ___63-[RPScreenRecorder stopSystemBroadcastWithSessionInfo:handler:]_block_invoke
+ ___63-[RPScreenRecorder stopSystemRecordingWithSessionInfo:handler:]_block_invoke
+ ___65-[RPControlCenterClient stopHQLRRecordingWithStopSource:handler:]_block_invoke
+ ___65-[RPControlCenterClient stopHQLRRecordingWithStopSource:handler:]_block_invoke_2
+ ___67-[RPControlCenterClient stopSystemRecordingWithStopSource:handler:]_block_invoke
+ ___67-[RPControlCenterClient stopSystemRecordingWithStopSource:handler:]_block_invoke_2
+ ___70-[RPBroadcastController finishSystemBroadcastWithSessionInfo:handler:]_block_invoke
+ _objc_msgSend$finishSystemBroadcastWithSessionInfo:handler:
+ _objc_msgSend$stopHQLRRecordingWithStopSource:handler:
+ _objc_msgSend$stopHQLRWithSessionInfo:handler:
+ _objc_msgSend$stopSystemBroadcastWithSessionInfo:handler:
+ _objc_msgSend$stopSystemRecordingWithSessionInfo:handler:
+ _objc_msgSend$stopSystemRecordingWithStopSource:handler:
- -[RPControlCenterClient stopHQLRRecordingWithHandler:]
- -[RPControlCenterClient stopSystemRecordingWithHandler:]
- -[RPDaemonProxy stopHQLRWithHandler:]
- -[RPDaemonProxy stopSystemBroadcastWithHandler:]
- -[RPDaemonProxy stopSystemRecordingWithHandler:]
- ___29-[RPScreenRecorder stopHQLR:]_block_invoke
- ___37-[RPDaemonProxy stopHQLRWithHandler:]_block_invoke
- ___40-[RPScreenRecorder stopSystemRecording:]_block_invoke
- ___48-[RPDaemonProxy stopSystemBroadcastWithHandler:]_block_invoke
- ___48-[RPDaemonProxy stopSystemRecordingWithHandler:]_block_invoke
- ___51-[RPScreenRecorder stopSystemBroadcastWithHandler:]_block_invoke
- ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke
- ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke_2
- ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke
- ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke_2
- ___58-[RPBroadcastController finishSystemBroadcastWithHandler:]_block_invoke
- _objc_msgSend$finishSystemBroadcastWithHandler:
- _objc_msgSend$stopHQLR:
- _objc_msgSend$stopHQLRRecordingWithHandler:
- _objc_msgSend$stopHQLRWithHandler:
- _objc_msgSend$stopSystemBroadcastWithHandler:
- _objc_msgSend$stopSystemRecording:
- _objc_msgSend$stopSystemRecordingWithHandler:
CStrings:
+ " [INFO] %{public}s:%d %p stopSource=%ld"
+ "-[RPControlCenterClient stopHQLRRecordingWithStopSource:handler:]"
+ "-[RPControlCenterClient stopHQLRRecordingWithStopSource:handler:]_block_invoke"
+ "-[RPControlCenterClient stopHQLRRecordingWithStopSource:handler:]_block_invoke_2"
+ "-[RPControlCenterClient stopSystemRecordingWithStopSource:handler:]"
+ "-[RPControlCenterClient stopSystemRecordingWithStopSource:handler:]_block_invoke"
+ "-[RPControlCenterClient stopSystemRecordingWithStopSource:handler:]_block_invoke_2"
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
+ "stopSource"
- "-[RPControlCenterClient stopHQLRRecordingWithHandler:]"
- "-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke"
- "-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke_2"
- "-[RPControlCenterClient stopSystemRecordingWithHandler:]"
- "-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke"
- "-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke_2"
- "-[RPScreenRecorder stopHQLR:]"
- "-[RPScreenRecorder stopSystemBroadcastWithHandler:]"
- "-[RPScreenRecorder stopSystemRecording:]"
- "RPDaemonProxy: stopSystemBroadcastWithHandler: proxy error: %d"
- "RPDaemonProxy: stopSystemBroadcastWithHandler:withHandler:"
- "RPDaemonProxy: stopSystemRecordingWithHandler: proxy error: %d"
- "RPDaemonProxy: stopSystemRecordingWithHandler:withHandler:"

```
