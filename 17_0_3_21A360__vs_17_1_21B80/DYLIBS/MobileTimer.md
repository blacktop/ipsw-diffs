## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2200.2.0.0.0
-  __TEXT.__text: 0xa9788
+2200.4.2.2.0
+  __TEXT.__text: 0xa98dc
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0xa5d0
+  __TEXT.__objc_methlist: 0xa5c8
   __TEXT.__const: 0x330
-  __TEXT.__oslogstring: 0xca18
+  __TEXT.__oslogstring: 0xca83
   __TEXT.__cstring: 0x7c55
   __TEXT.__gcc_except_tab: 0xac0
   __TEXT.__dlopen_cstrs: 0x671
   __TEXT.__ustring: 0x1a
-  __TEXT.__unwind_info: 0x2c7c
+  __TEXT.__unwind_info: 0x2c80
   __TEXT.__objc_classname: 0x17ef
-  __TEXT.__objc_methname: 0x157b7
+  __TEXT.__objc_methname: 0x157ab
   __TEXT.__objc_methtype: 0x3d27
   __TEXT.__objc_stubs: 0x102c0
   __DATA_CONST.__got: 0x1b8

   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x23518
-  __DATA_CONST.__objc_selrefs: 0x53e8
+  __DATA_CONST.__objc_selrefs: 0x53e0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3F2A82A-D336-371F-96EA-34A8A0747F8E
-  Functions: 4580
-  Symbols:   15694
+  UUID: E15C7C04-CE20-3B41-8649-CBD230F807D3
+  Functions: 4581
+  Symbols:   15696
   CStrings:  7397
 
Symbols:
+ -[MTSessionsCoordinator dismissTimerWithIdentifier:].cold.1
+ GCC_except_table60
+ GCC_except_table87
+ ___48-[MTSessionsCoordinator source:didRemoveAlarms:]_block_invoke.134
+ ___49-[MTSessionsCoordinator didRestoreAlarmSessions:]_block_invoke.139
+ ___49-[MTSessionsCoordinator didRestoreAlarmSessions:]_block_invoke_2.140
+ ___49-[MTSessionsCoordinator didRestoreTimerSessions:]_block_invoke.144
+ ___52-[MTSessionsCoordinator dismissTimerWithIdentifier:]_block_invoke.120
+ ___52-[MTSessionsCoordinator dismissTimerWithIdentifier:]_block_invoke.120.cold.1
+ ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.130
+ ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.130.cold.1
+ ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.130.cold.2
+ ___68-[MTSessionsCoordinator dismissTimerAndEndSessionWithId:completion:]_block_invoke.121.cold.1
+ ___68-[MTSessionsCoordinator dismissTimerAndEndSessionWithId:completion:]_block_invoke.122
+ ___block_literal_global.137
+ ___block_literal_global.142
+ ___block_literal_global.146
- +[MTUtilities logMessage:]
- GCC_except_table88
- ___48-[MTSessionsCoordinator source:didRemoveAlarms:]_block_invoke.133
- ___49-[MTSessionsCoordinator didRestoreAlarmSessions:]_block_invoke.138
- ___49-[MTSessionsCoordinator didRestoreAlarmSessions:]_block_invoke_2.139
- ___49-[MTSessionsCoordinator didRestoreTimerSessions:]_block_invoke.143
- ___52-[MTSessionsCoordinator dismissTimerWithIdentifier:]_block_invoke.cold.1
- ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.128
- ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.129.cold.1
- ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.129.cold.2
- ___68-[MTSessionsCoordinator dismissTimerAndEndSessionWithId:completion:]_block_invoke.120
- ___68-[MTSessionsCoordinator dismissTimerAndEndSessionWithId:completion:]_block_invoke.120.cold.1
- ___block_literal_global.132
- ___block_literal_global.136
- ___block_literal_global.141
- ___block_literal_global.145
CStrings:
+ "%{public}@ dismissing firing timer with identifier: %{public}@"
+ "%{public}@ hit a race, not dismissing non firing timer: %{public}@"
- "%{public}@: %{public}@"
- "logMessage:"

```
