## PerformanceTrace

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace`

```diff

-237.0.0.0.0
-  __TEXT.__text: 0x11d70
+238.0.0.0.0
+  __TEXT.__text: 0x11d8c
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_methlist: 0xc4c
   __TEXT.__const: 0x80

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB40AAB2-807A-31F4-B704-BFA67951508D
+  UUID: DF5516E5-DA64-3E94-9D89-F1BD04DB8CEB
   Functions: 334
-  Symbols:   1301
+  Symbols:   1303
   CStrings:  831
 
Symbols:
+ +[PTTraceConfig(ControlCenter) isControlCenterModuleAvailable].cold.1
Functions:
~ +[PTTraceConfig(ControlCenter) isControlCenterModuleAvailable] : 280 -> 308
~ __controlCenterHandle.cold.1 -> ___55+[PTTraceConfig(ControlCenter) availableTracePlanNames]_block_invoke.cold.1 : 20 -> 40
~ +[PTTraceConfig(ControlCenter) userSelectedTracePlanName].cold.1 -> __controlCenterHandle.cold.1 : 116 -> 20
~ +[PTTraceConfig(ControlCenter) availableTracePlanNames].cold.1 -> +[PTTraceConfig(ControlCenter) setUserSelectedTracePlanName:].cold.1 : 20 -> 116
~ ___55+[PTTraceConfig(ControlCenter) availableTracePlanNames]_block_invoke.cold.1 -> +[PTTraceConfig(ControlCenter) availableTracePlanNames].cold.1 : 40 -> 20

```
