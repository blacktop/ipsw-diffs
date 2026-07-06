## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/Versions/A/ReplayKit`

```diff

-  __TEXT.__text: 0x313e4
-  __TEXT.__objc_methlist: 0x347c
-  __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x666f
+  __TEXT.__text: 0x31468
+  __TEXT.__objc_methlist: 0x348c
+  __TEXT.__const: 0x1a8
+  __TEXT.__cstring: 0x66e0
   __TEXT.__gcc_except_tab: 0x3a8
-  __TEXT.__oslogstring: 0x3c04
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__oslogstring: 0x3bec
+  __TEXT.__unwind_info: 0xbe8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x4c8
   __AUTH_CONST.__const: 0x1620
-  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__cfstring: 0x1ae0
   __AUTH_CONST.__objc_const: 0x7cc8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1318
-  Symbols:   3395
-  CStrings:  1052
+  Functions: 1319
+  Symbols:   3396
+  CStrings:  1056
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_classrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[RPDaemonProxy stopHQLRWithSessionInfo:handler:]
+ -[RPScreenRecorder stopHQLRWithSessionInfo:handler:]
+ GCC_except_table123
+ GCC_except_table126
+ __49-[RPDaemonProxy stopHQLRWithSessionInfo:handler:]_block_invoke
+ ___49-[RPDaemonProxy stopHQLRWithSessionInfo:handler:]_block_invoke
+ ___52-[RPScreenRecorder stopHQLRWithSessionInfo:handler:]_block_invoke
+ _objc_msgSend$stopHQLRWithSessionInfo:handler:
- -[RPDaemonProxy stopHQLRWithHandler:]
- GCC_except_table122
- GCC_except_table125
- __37-[RPDaemonProxy stopHQLRWithHandler:]_block_invoke
- ___29-[RPScreenRecorder stopHQLR:]_block_invoke
- ___37-[RPDaemonProxy stopHQLRWithHandler:]_block_invoke
- _objc_msgSend$stopHQLRWithHandler:
CStrings:
+ "-[RPScreenRecorder stopHQLRWithSessionInfo:handler:]"
+ "RECORDING_ERROR_FAILED_TO_START_HIGH_QUALITY_RECORDING"
+ "RECORDING_ERROR_TIME_LIMIT_REACHED"
+ "RPDaemonProxy: stopHQLRWithSessionInfo: proxy error: %d"
+ "RPDaemonProxy: stopHQLRWithSessionInfo:%@"
- "-[RPScreenRecorder stopHQLR:]"
- "RPDaemonProxy: stopSystemRecordingWithHandler: proxy error: %d"
- "RPDaemonProxy: stopSystemRecordingWithHandler:withHandler:"

```
