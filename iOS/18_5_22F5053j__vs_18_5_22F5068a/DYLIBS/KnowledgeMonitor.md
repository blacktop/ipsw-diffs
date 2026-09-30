## KnowledgeMonitor

> `/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor`

```diff

-458.7.0.0.0
-  __TEXT.__text: 0x2d538
+458.8.0.0.0
+  __TEXT.__text: 0x2d920
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x2fac
-  __TEXT.__const: 0x230
-  __TEXT.__gcc_except_tab: 0x810
-  __TEXT.__cstring: 0x2c8e
-  __TEXT.__oslogstring: 0x2859
+  __TEXT.__objc_methlist: 0x2fc4
+  __TEXT.__const: 0x240
+  __TEXT.__gcc_except_tab: 0x824
+  __TEXT.__cstring: 0x2cae
+  __TEXT.__oslogstring: 0x2896
   __TEXT.__dlopen_cstrs: 0x49
-  __TEXT.__unwind_info: 0xc18
-  __TEXT.__objc_classname: 0x5dc
-  __TEXT.__objc_methname: 0x86e6
-  __TEXT.__objc_methtype: 0xcba
-  __TEXT.__objc_stubs: 0x6bc0
-  __DATA_CONST.__got: 0x600
-  __DATA_CONST.__const: 0x900
+  __TEXT.__unwind_info: 0xc28
+  __TEXT.__objc_classname: 0x5da
+  __TEXT.__objc_methname: 0x875a
+  __TEXT.__objc_methtype: 0xcc5
+  __TEXT.__objc_stubs: 0x6c40
+  __DATA_CONST.__got: 0x608
+  __DATA_CONST.__const: 0x928
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22e8
+  __DATA_CONST.__objc_selrefs: 0x2308
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__auth_got: 0x610
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1f40
-  __AUTH_CONST.__objc_const: 0x4aa0
+  __AUTH_CONST.__cfstring: 0x1f60
+  __AUTH_CONST.__objc_const: 0x4ac0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x168
-  __DATA.__objc_ivar: 0x338
+  __DATA.__objc_ivar: 0x33c
   __DATA.__data: 0x4e8
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0xe10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1183
-  Symbols:   4434
-  CStrings:  2220
+  Functions: 1186
+  Symbols:   4448
+  CStrings:  2229
 
Symbols:
+ -[_DKBacklightMonitor _lastAliveDate]
+ -[_DKBacklightMonitor _setLastAliveDate:]
+ GCC_except_table21
+ GCC_except_table23
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_IVAR_$__DKBacklightMonitor._lastAliveDateTimer
+ ___65-[_DKBacklightMonitor donateRetroactiveShutdownBacklightOffEvent]_block_invoke.29
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ _objc_msgSend$_lastAliveDate
+ _objc_msgSend$_setLastAliveDate:
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$sendEvent:date:
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:191"
+ "@\"NSTimer\""
+ "Last alive date is: %{public}@"
+ "LastAliveDate"
+ "Setting last alive date: %{public}@"
+ "Shutdown date from SpringBoard is: %{public}@"
+ "Shutdown date from kern.shutdowntime is: %{public}@"
+ "_lastAliveDate"
+ "_lastAliveDateTimer"
+ "_setLastAliveDate:"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "sendEvent:date:"
+ "v16@?0@\"NSTimer\"8"
- "\x12"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:175"
- "Using shutdown date from SpringBoard: %{public}@"
- "Using shutdown date from kern.shutdowntime: %{public}@"

```
