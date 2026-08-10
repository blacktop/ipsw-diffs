## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-753.0.15.0.0
-  __TEXT.__text: 0xd9c7c
-  __TEXT.__objc_methlist: 0x1d71c
+753.0.17.0.0
+  __TEXT.__text: 0xd9de4
+  __TEXT.__objc_methlist: 0x1d764
   __TEXT.__const: 0x6d0
-  __TEXT.__cstring: 0xf790
-  __TEXT.__oslogstring: 0xf0da
+  __TEXT.__cstring: 0xf7f9
+  __TEXT.__oslogstring: 0xf137
   __TEXT.__gcc_except_tab: 0x10c0
-  __TEXT.__unwind_info: 0x2208
+  __TEXT.__unwind_info: 0x2210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1720
+  __DATA_CONST.__const: 0x1728
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e78
+  __DATA_CONST.__objc_selrefs: 0x5ea8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x71c0
   __DATA_CONST.__got: 0x5e0
   __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0xdbc0
-  __AUTH_CONST.__objc_const: 0x39f98
+  __AUTH_CONST.__cfstring: 0xdc20
+  __AUTH_CONST.__objc_const: 0x39ff8
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_arrayobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__auth_got: 0x5f0
   __AUTH.__objc_data: 0x1b30
-  __DATA.__objc_ivar: 0x3ed0
+  __DATA.__objc_ivar: 0x3ed8
   __DATA.__data: 0x788
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0xb40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10650
-  Symbols:   17588
-  CStrings:  3204
+  Functions: 10656
+  Symbols:   17599
+  CStrings:  3209
 
Symbols:
+ -[PowerUIIBLMNotificationManager displayUnusualDrainNotification]
+ -[PowerUIIBLMNotificationManager postIBLMNotificationWithTitleKey:bodyKey:identifier:category:]
+ -[PowerUIRuntimeAwarenessNotifier mlCheckActive]
+ -[PowerUIRuntimeAwarenessNotifier mlCheckTimer]
+ -[PowerUIRuntimeAwarenessNotifier mlCheckTransaction]
+ -[PowerUIRuntimeAwarenessNotifier setMlCheckActive:]
+ -[PowerUIRuntimeAwarenessNotifier setMlCheckTimer:]
+ -[PowerUIRuntimeAwarenessNotifier setMlCheckTransaction:]
+ -[PowerUIRuntimeAwarenessNotifier startMLCheckTimer]
+ -[PowerUIRuntimeAwarenessNotifier stopMLCheckTimer]
+ GCC_except_table5
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._mlCheckActive
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._mlCheckTimer
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._mlCheckTransaction
+ ___52-[PowerUIRuntimeAwarenessNotifier startMLCheckTimer]_block_invoke
+ ___95-[PowerUIIBLMNotificationManager postIBLMNotificationWithTitleKey:bodyKey:identifier:category:]_block_invoke
+ _dispatch_resume
+ _kIBLMUnusualDrainNotification
+ _objc_msgSend$postIBLMNotificationWithTitleKey:bodyKey:identifier:category:
+ _objc_msgSend$startMLCheckTimer
+ _objc_msgSend$stopMLCheckTimer
- -[PowerUIRuntimeAwarenessNotifier cancelMLCheckAlarm]
- -[PowerUIRuntimeAwarenessNotifier mlAlarmScheduled]
- -[PowerUIRuntimeAwarenessNotifier scheduleMLCheckAlarm]
- -[PowerUIRuntimeAwarenessNotifier setMlAlarmScheduled:]
- GCC_except_table3
- _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._mlAlarmScheduled
- ___52-[PowerUIRuntimeAwarenessNotifier handleAlarmEvent:]_block_invoke_2
- ___64-[PowerUIIBLMNotificationManager displayIBLMEngagedNotification]_block_invoke
- _objc_msgSend$cancelMLCheckAlarm
- _objc_msgSend$scheduleMLCheckAlarm
CStrings:
+ "Conditions no longer met for ML check (battery: %ld%%, plugged: %d), stopping timer"
+ "Current battery level: %ld%% - invalid"
+ "IBLM-UnusualDrain"
+ "POWERUI_ADAPTIVE_POWER_FIRST_TIME_BODY"
+ "POWERUI_ADAPTIVE_POWER_FIRST_TIME_TITLE"
+ "POWERUI_ADAPTIVE_POWER_UNUSUAL_DRAIN_BODY"
+ "POWERUI_ADAPTIVE_POWER_UNUSUAL_DRAIN_TITLE"
+ "Posting onboarding Adaptive Power notification"
+ "Posting unusual-drain Adaptive Power notification"
+ "Starting ML check timer"
+ "Stopping ML check timer"
+ "com.apple.osi.iblm.unusualDrainNotification"
+ "com.apple.powerui.runtimeAwareness.mlCheck"
+ "unusualDrainIBLMCategory"
- "/System/Library/UserNotifications/Bundles/com.apple.osintelligence.notifications.bundle"
- "ADAPTIVE_POWER_FIRST_TIME_BODY"
- "ADAPTIVE_POWER_FIRST_TIME_TITLE"
- "Cancelling ML check alarm"
- "Conditions no longer met for ML check (battery: %ld%%, plugged: %d), cancelling alarm"
- "Localizable-IBLM"
- "Posting First time IBLM notification"
- "RuntimeAwarenessMLCheck"
- "Scheduling ML check alarm"
```
