## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-383.0.0.0.0
-  __TEXT.__text: 0x17250
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_methlist: 0x974
+384.0.0.0.0
+  __TEXT.__text: 0x1742c
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0x984
   __TEXT.__const: 0x160
   __TEXT.__cstring: 0x41b0
-  __TEXT.__oslogstring: 0x2b44
+  __TEXT.__oslogstring: 0x2b7e
   __TEXT.__gcc_except_tab: 0x21c
   __TEXT.__ustring: 0xe0
   __TEXT.__unwind_info: 0x558
   __TEXT.__objc_classname: 0x54
-  __TEXT.__objc_methname: 0x3b6d
-  __TEXT.__objc_methtype: 0x765
-  __TEXT.__objc_stubs: 0x16c0
+  __TEXT.__objc_methname: 0x3b83
+  __TEXT.__objc_methtype: 0x7fa
+  __TEXT.__objc_stubs: 0x1720
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x1688
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d8
+  __DATA_CONST.__objc_selrefs: 0x9e0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x4a0
   __AUTH_CONST.__cfstring: 0x56c0
   __AUTH_CONST.__objc_const: 0x1978

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x1dc
-  __DATA.__data: 0x208
+  __DATA.__data: 0x210
   __DATA.__bss: 0x90
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 26DCC710-D723-3204-8475-9C25E529D4EC
-  Functions: 550
-  Symbols:   2039
-  CStrings:  2242
+  UUID: 3C4D0E80-94FF-3E27-8A52-E886CA59C6D1
+  Functions: 553
+  Symbols:   2054
+  CStrings:  2245
 
Symbols:
+ +[HTMonitorPidHangEvent getSharedPageFromPid:]
+ +[HTMonitorPidHangEvent getSharedPageFromPid:].cold.1
+ GCC_except_table15
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table59
+ GCC_except_table65
+ GCC_except_table74
+ ___HTConnectToHTMonitor_block_invoke.45
+ ___HTInitializeHangTracerMonitor_block_invoke.53
+ ___HTInitializeHangTracerMonitor_block_invoke.53.cold.1
+ ___HTInitializeHangTracerMonitor_block_invoke.53.cold.2
+ ___HTInitializeHangTracerMonitor_block_invoke.53.cold.3
+ ___HTInitializeHangTracerMonitor_block_invoke.57
+ ___block_literal_global.13
+ ___block_literal_global.17
+ ___block_literal_global.48
+ ___block_literal_global.52
+ ___block_literal_global.59
+ _dispatch_assert_queue$V2
+ _dispatch_queue_get_label
+ _getEventFromPid
+ _getEventFromPid.cold.1
+ _htMonitorConnectionQueueLabel
+ _objc_msgSend$getSharedPageFromPid:
+ _objc_msgSend$shmem_region
+ _objc_msgSend$shmem_size
+ _strlen
+ _strncmp
- GCC_except_table14
- GCC_except_table40
- GCC_except_table42
- GCC_except_table44
- GCC_except_table47
- GCC_except_table52
- GCC_except_table58
- GCC_except_table63
- GCC_except_table73
- ___HTConnectToHTMonitor_block_invoke.42
- ___HTInitializeHangTracerMonitor_block_invoke.51
- ___HTInitializeHangTracerMonitor_block_invoke.51.cold.1
- ___HTInitializeHangTracerMonitor_block_invoke.51.cold.2
- ___HTInitializeHangTracerMonitor_block_invoke.51.cold.3
- ___HTInitializeHangTracerMonitor_block_invoke.55
- ___block_literal_global.12
- ___block_literal_global.16
- ___block_literal_global.45
- ___block_literal_global.50
- ___block_literal_global.57
Functions:
~ _updateHTForegroundTrackingState : 848 -> 876
+ _getEventFromPid
~ _HTEndNonResponsiveTaskAtTime : 1048 -> 1012
+ +[HTMonitorPidHangEvent getSharedPageFromPid:]
+ +[HTMonitorPidHangEvent getSharedPageFromPid:].cold.1
CStrings:
+ "HTMonitor shared page accessed on the incorrect queue: %s"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}20@0:8i16"
+ "getSharedPageFromPid:"

```
