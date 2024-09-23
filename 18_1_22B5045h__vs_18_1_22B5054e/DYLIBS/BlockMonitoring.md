## BlockMonitoring

> `/System/Library/PrivateFrameworks/BlockMonitoring.framework/BlockMonitoring`

```diff

-379.0.0.0.0
-  __TEXT.__text: 0x3540
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x1d0
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0xd8
+380.0.0.0.0
+  __TEXT.__text: 0x39bc
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_methlist: 0x230
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0xdc
   __TEXT.__cstring: 0x511
-  __TEXT.__oslogstring: 0x51c
+  __TEXT.__oslogstring: 0x659
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__unwind_info: 0x150
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x737
-  __TEXT.__objc_methtype: 0x162
-  __TEXT.__objc_stubs: 0x680
+  __TEXT.__objc_methname: 0x85f
+  __TEXT.__objc_methtype: 0x185
+  __TEXT.__objc_stubs: 0x6c0
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x248
+  __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__objc_const: 0x2f8
-  __DATA.__objc_ivar: 0x4c
+  __AUTH_CONST.__objc_const: 0x398
+  __DATA.__objc_ivar: 0x60
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 80
-  Symbols:   233
-  CStrings:  200
+  Functions: 89
+  Symbols:   246
+  CStrings:  220
 
Symbols:
+ _objc_release_x26
+ _BMMonitorBlockExecutionWithSignatureAndOptions
+ _objc_retain_x24
+ _proc_pidinfo
+ _objc_retain_x5
+ __os_log_fault_impl
+ _objc_retain_x23
+ _objc_retain_x26
- _objc_retain_x4
- _BMMonitorBlockExecutionWithSignatureAndTimeout
- _objc_retain_x22
- _objc_retain_x28
- _objc_release_x28
CStrings:
+ "signature=%!{(MISSING)public,signpost.telemetry:string1,name=signature}@ reason=%!{(MISSING)public,signpost.telemetry:number1,name=reason}d demoted=%!{(MISSING)public,signpost.telemetry:number2,name=demoted}d enableTelemetry=YES "
+ "Disabling panics - coredumps not enabled: %!l(MISSING)lx"
+ "v52@0:8@16Q24Q32i40^AB44"
+ "BM state: %!d(MISSING) (%!d(MISSING)) - %!d(MISSING)"
+ "Panic not enabled - demoting the asked panic to a fault"
+ "_test_getWasFirstFault"
+ "_test_setDebuggerState:"
+ "_test_getResultType"
+ "logPanicDeny:reason:demoted:"
+ "logFault:reason:"
+ "_test_getCoreDumpsDisabled"
+ "isProcessBeingDebugged"
+ "executeBlockWithSignature:timeout:options:block:"
+ "v44@0:8r*16Q24i32@?36"
+ "_alreadyFaulted"
+ "takeActionIfRelevant:thread_id:timeout:options:recovered:"
+ "%!@(MISSING) (%!u(MISSING):%!l(MISSING)lu) recovered - skipping fault"
+ "v32@0:8@16r*24"
+ "_coreDumpsDisabled"
+ "fault_triggered"
+ "_test_getAlreadyFaulted"
+ "signature=%!{(MISSING)public,signpost.telemetry:string1,name=signature}@ first=%!{(MISSING)public,signpost.telemetry:number1,name=first}d enableTelemetry=YES "
+ "_test_resultType"
+ "v20@0:8C16"
+ "\x121!!\x11"
+ "_test_debuggerState"
+ "_test_getDebuggerState"
+ "_test_wasFirstFault"
+ "v32@0:8@16C24B28"
- "BM state: %!d(MISSING) - %!d(MISSING)"
- "Disabling feature - coredumps not enabled: %!l(MISSING)lx"
- "signature=%!{(MISSING)public,signpost.telemetry:string1,name=signature}@ reason=%!{(MISSING)public,signpost.telemetry:number1,name=reason}d enableTelemetry=YES "
- "v48@0:8@16Q24Q32^AB40"
- "logPanicDeny:reason:"
- "v40@0:8r*16Q24@?32"
- "v28@0:8@16C24"
- "panicDeviceIfRelevant:thread_id:timeout:recovered:"
- "\x121!\x11\x11"
- "executeBlockWithSignature:timeout:block:"

```
