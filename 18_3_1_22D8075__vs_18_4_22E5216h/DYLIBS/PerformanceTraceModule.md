## PerformanceTraceModule

> `/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule`

```diff

-600.3.3.100.1
-  __TEXT.__text: 0xfac
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0x13c
+600.4.21.100.0
+  __TEXT.__text: 0xc90
+  __TEXT.__auth_stubs: 0x1a0
+  __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xd2
-  __TEXT.__oslogstring: 0x16
-  __TEXT.__unwind_info: 0xc0
-  __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0x816
-  __TEXT.__objc_methtype: 0x383
-  __TEXT.__objc_stubs: 0x520
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x98
+  __TEXT.__cstring: 0x8e
+  __TEXT.__oslogstring: 0x36
+  __TEXT.__unwind_info: 0xb0
+  __TEXT.__objc_classname: 0x7a
+  __TEXT.__objc_methname: 0x788
+  __TEXT.__objc_methtype: 0x328
+  __TEXT.__objc_stubs: 0x420
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c8
+  __DATA_CONST.__objc_selrefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x120
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x878
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0xd8
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__objc_const: 0x4e8
+  __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x180
-  __DATA.__bss: 0x10
+  __DATA.__objc_ivar: 0x18
+  __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 33
-  Symbols:   69
-  CStrings:  153
+  Functions: 29
+  Symbols:   56
+  CStrings:  134
 
Symbols:
+ _CCUILogModuleInstance
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _PTTraceSessionInfoKey_EndingFGSceneIdentifiers
+ _PTTraceSessionInfoKey_StartingFGSceneIdentifiers
+ __os_log_error_impl
+ _objc_release_x23
+ _objc_retainBlock
+ _objc_retain_x1
- OBJC_IVAR_$_CCUIPerformanceTraceModuleViewController._traceSession
- _CCUILogUserInterface
- _NSClassFromString
- _OBJC_CLASS_$_FBSDisplayLayoutMonitor
- _OBJC_CLASS_$_FBSDisplayLayoutMonitorConfiguration
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSMutableArray
- __NSConcreteGlobalBlock
- __os_log_impl
- _dispatch_once
- _dispatch_sync
- _dlopen
- _objc_alloc
- _objc_enumerationMutation
- _objc_release_x1
- _objc_release_x24
- _objc_retainAutorelease
- _objc_retain_x19
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "\x13"
+ "configWithTracePlanName:"
+ "displayLayoutContextProvider"
+ "displayTraceCompletedAlertWithTraceFileURL failed: %@"
+ "displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:"
+ "foregroundApplicationSceneBundleIdentifiers"
+ "setObject:forKeyedSubscript:"
+ "setSymbolicate:"
+ "setTraceDurationSecs:"
+ "v16@?0@\"NSError\"8"
- "\x14"
- "-S"
- "/AppleInternal/Library/Frameworks/TraceCart.framework/TraceCart"
- "@\"TCArtraceSession\""
- "Performance Trace: %@"
- "TCArtraceSession"
- "TCArtraceSessionDelegate"
- "_traceSession"
- "addObject:"
- "array"
- "artraceSession:didReceiveOutput:"
- "artraceSessionDidComplete:"
- "bundleIdentifier"
- "configurationForDefaultMainDisplayMonitor"
- "countByEnumeratingWithState:objects:count:"
- "currentLayout"
- "displayTraceCompletedAlertWithSessionInfo:completion:"
- "elements"
- "getCurrentConfig"
- "initWithTraceOptions:"
- "invalidate"
- "isUIApplicationElement"
- "monitorWithConfiguration:"
- "q"
- "setObject:forKey:"
- "startTrace"
- "stopTrace"
- "v24@0:8@\"TCArtraceSession\"16"
- "v32@0:8@\"TCArtraceSession\"16@\"NSString\"24"

```
