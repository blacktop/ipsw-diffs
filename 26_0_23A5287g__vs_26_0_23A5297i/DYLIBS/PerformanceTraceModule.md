## PerformanceTraceModule

> `/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule`

```diff

-649.104.102.0.0
-  __TEXT.__text: 0x2c60
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x424
+652.102.0.0.0
+  __TEXT.__text: 0x2ef8
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_methlist: 0x454
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__cstring: 0x23a
-  __TEXT.__oslogstring: 0x4cd
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__cstring: 0x29e
+  __TEXT.__oslogstring: 0x53b
+  __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x7a
-  __TEXT.__objc_methname: 0xe39
-  __TEXT.__objc_methtype: 0x344
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0xf0
+  __TEXT.__objc_methname: 0xf65
+  __TEXT.__objc_methtype: 0x381
+  __TEXT.__objc_stubs: 0xa60
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d8
+  __DATA_CONST.__objc_selrefs: 0x408
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x150
+  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x240
-  __AUTH_CONST.__objc_const: 0x5a8
+  __AUTH_CONST.__objc_const: 0x608
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x120
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B51F8234-E976-3CDC-AD89-B87DDC079CDC
-  Functions: 76
-  Symbols:   75
-  CStrings:  258
+  UUID: E10E5006-77EF-3B87-80A3-1EF7F364739D
+  Functions: 84
+  Symbols:   80
+  CStrings:  274
 
Symbols:
+ _OBJC_CLASS_$_PTGlobalStateChangeMonitor
+ __NSConcreteGlobalBlock
+ _dispatch_once
+ _dispatch_queue_create
+ _objc_release_x1
+ _os_log_create
- _objc_retain_x22
CStrings:
+ "&"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"PTGlobalStateChangeMonitor\""
+ "Global locked state transitioned from locked to unlocked, so inferring that Power Profiler recording stopped."
+ "PerformanceTraceModule"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_stateChangeQueue"
+ "T@\"PTGlobalStateChangeMonitor\",R,N,V_stateChangeMonitor"
+ "_performanceTraceGlobalStateDidChange"
+ "_stateChangeMonitor"
+ "_stateChangeQueue"
+ "com.apple.ControlCenter"
+ "com.apple.MobileControlCenter.PerformanceTraceModule"
+ "globalSettingsAreLocked"
+ "initWithQueue:stateChangeBlock:"
+ "setStateChangeQueue:"
+ "stateChangeMonitor"
+ "stateChangeQueue"
- "$"

```
