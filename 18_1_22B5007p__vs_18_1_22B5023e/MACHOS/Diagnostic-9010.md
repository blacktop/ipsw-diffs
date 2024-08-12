## Diagnostic-9010

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010`

```diff

-604.0.0.0.0
-  __TEXT.__text: 0x5cc
-  __TEXT.__auth_stubs: 0xf0
-  __TEXT.__objc_stubs: 0x120
-  __TEXT.__objc_methlist: 0xd4
-  __TEXT.__const: 0x18
-  __TEXT.__oslogstring: 0x22
-  __TEXT.__cstring: 0xa8
-  __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x3ef
-  __TEXT.__objc_methtype: 0x149
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x80
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__cfstring: 0x60
+645.0.0.0.0
+  __TEXT.__text: 0xd44
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_stubs: 0x1e0
+  __TEXT.__objc_methlist: 0xf4
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__oslogstring: 0x96
+  __TEXT.__cstring: 0xf4
+  __TEXT.__objc_methname: 0x514
+  __TEXT.__objc_classname: 0x4f
+  __TEXT.__objc_methtype: 0x169
+  __TEXT.__dlopen_cstrs: 0x62
+  __TEXT.__unwind_info: 0xa0
+  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__const: 0xb0
+  __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x5e0
-  __DATA.__objc_selrefs: 0xb0
-  __DATA.__objc_ivar: 0x14
+  __DATA_CONST.__objc_intobj: 0x78
+  __DATA.__objc_const: 0x640
+  __DATA.__objc_selrefs: 0xf0
+  __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 16
-  Symbols:   32
-  CStrings:  96
+  Functions: 27
+  Symbols:   48
+  CStrings:  118
 
Symbols:
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ __os_log_error_impl
+ __sl_dlopen
+ _abort_report_np
+ _free
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_getClass
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_new
+ _objc_release
+ _objc_retainAutorelease
+ _objc_retain_x20
- _objc_retain_x21
CStrings:
+ "\x02"
+ "\x05"
+ "@\"DSHardwareButtonEventMonitor\""
+ "ButtonEventMonitor not available"
+ "DSHardwareButtonEventMonitor"
+ "DiagnosticsSupport not available"
+ "Register physical button events"
+ "T@\"DSHardwareButtonEventMonitor\",&,N,V_buttonEventMonitor"
+ "T@\"NSNumber\",R,N,VtestIdentifer"
+ "Unable to find class %!s(MISSING)"
+ "_buttonEventMonitor"
+ "addTarget:action:forButtonEvents:propagate:"
+ "buttonEventMonitor"
+ "handleButtonEvent:"
+ "removeTarget:"
+ "setButtonEventMonitor:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport"
+ "startWithPriority:completion:"
+ "stopWithCompletion:"
+ "testIdentifer"
+ "testIdentifer"
+ "testIdentifer: %!@(MISSING)"
+ "v8@?0"
- "\x01"
- "\x04"

```
