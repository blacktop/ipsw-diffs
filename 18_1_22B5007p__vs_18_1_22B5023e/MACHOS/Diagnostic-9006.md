## Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

```diff

-604.0.0.0.0
-  __TEXT.__text: 0x8c0
-  __TEXT.__auth_stubs: 0xe0
-  __TEXT.__objc_stubs: 0x100
-  __TEXT.__objc_methlist: 0x284
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x9a
-  __TEXT.__oslogstring: 0xe
-  __TEXT.__objc_classname: 0xb1
-  __TEXT.__objc_methname: 0x170e
-  __TEXT.__objc_methtype: 0xaa0
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x78
-  __DATA_CONST.__got: 0x18
+645.0.0.0.0
+  __TEXT.__text: 0xf5c
+  __TEXT.__auth_stubs: 0x1c0
+  __TEXT.__objc_stubs: 0x1c0
+  __TEXT.__objc_methlist: 0x29c
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__cstring: 0xd8
+  __TEXT.__oslogstring: 0x70
+  __TEXT.__objc_methname: 0x1805
+  __TEXT.__objc_classname: 0xb2
+  __TEXT.__objc_methtype: 0xac0
+  __TEXT.__dlopen_cstrs: 0x62
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1410
-  __DATA.__objc_selrefs: 0x1d0
-  __DATA.__objc_ivar: 0x5c
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0x1440
+  __DATA.__objc_selrefs: 0x208
+  __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x240
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 52
-  Symbols:   31
-  CStrings:  316
+  Functions: 62
+  Symbols:   47
+  CStrings:  334
 
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
+ "\x1f\a"
+ "@\"DSHardwareButtonEventMonitor\""
+ "ButtonEventMonitor not available"
+ "DSHardwareButtonEventMonitor"
+ "DiagnosticsSupport not available"
+ "Register physical button events"
+ "T@\"DSHardwareButtonEventMonitor\",&,N,V_buttonEventMonitor"
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
+ "v8@?0"
- "\x1f\x06"

```
