## replayd

> `/usr/libexec/replayd`

```diff

-  __TEXT.__text: 0xc5ab8
+  __TEXT.__text: 0xc5e44
   __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_stubs: 0xebe0
-  __TEXT.__objc_methlist: 0x751c
+  __TEXT.__objc_stubs: 0xec40
+  __TEXT.__objc_methlist: 0x754c
   __TEXT.__const: 0x430
-  __TEXT.__oslogstring: 0x151d8
-  __TEXT.__cstring: 0x171d0
+  __TEXT.__oslogstring: 0x15250
+  __TEXT.__cstring: 0x17255
   __TEXT.__objc_classname: 0xacb
-  __TEXT.__objc_methname: 0x1601b
+  __TEXT.__objc_methname: 0x16079
   __TEXT.__objc_methtype: 0x4064
   __TEXT.__gcc_except_tab: 0xf4c
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x22c8
+  __TEXT.__unwind_info: 0x22d0
   __DATA_CONST.__const: 0x2860
-  __DATA_CONST.__cfstring: 0x62a0
+  __DATA_CONST.__cfstring: 0x6340
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__auth_got: 0xd90
-  __DATA_CONST.__got: 0xc70
+  __DATA_CONST.__got: 0xd00
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x11088
-  __DATA.__objc_selrefs: 0x4620
-  __DATA.__objc_ivar: 0xdd0
+  __DATA.__objc_const: 0x110b8
+  __DATA.__objc_selrefs: 0x4638
+  __DATA.__objc_ivar: 0xdd4
   __DATA.__objc_data: 0x1cc0
   __DATA.__data: 0xc98
   __DATA.__bss: 0x288

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3732
+  Functions: 3736
   Symbols:   846
-  CStrings:  8194
+  CStrings:  8211
 
Sections:
~ __TEXT.__objc_methtype : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
CStrings:
+ " [ERROR] %{public}s:%d sample buffer missing color space for streamID=%{public}@"
+ " [INFO] %{public}s:%d Ignoring display change for HQLR recording"
+ " [INFO] %{public}s:%d sessionInfo=%@"
+ "-[RPClient stopHQLRWithSessionInfo:handler:]"
+ "-[RPClient stopHQLRWithSessionInfo:handler:]_block_invoke"
+ "-[RPConnectionManager stopHQLRWithSessionInfo:handler:]"
+ "CTYP"
+ "RECORDING_ERROR_FAILED_TO_START_HIGH_QUALITY_RECORDING"
+ "RECORDING_ERROR_TIME_LIMIT_REACHED"
+ "RPConnectionManager: stopHQLRWithSessionInfo completed"
+ "STPS"
+ "Tq,N,V_stopSource"
+ "_stopSource"
+ "serviceNameSupportsStopSource"
+ "setStopSource:"
+ "stopHQLRWithSessionInfo:handler:"
+ "stopSource"
+ "stopSourceForEndReason:"
- " [INFO] %{public}s:%d Stopped HQLR recording due to display change"
- "-[RPClient stopHQLRSessionWithHandler:]"
- "-[RPClient stopHQLRSessionWithHandler:]_block_invoke"
- "-[RPConnectionManager stopHQLRWithHandler:]"
- "RPConnectionManager: stopHQLRWithHandler completed"
- "stopHQLRSessionWithHandler:"
- "stopHQLRWithHandler:"

```
