## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3500.87.2.0.0
-  __TEXT.__text: 0x4c148
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x5f84
-  __TEXT.__const: 0x812
-  __TEXT.__cstring: 0x9cdd
-  __TEXT.__oslogstring: 0x6a5e
-  __TEXT.__gcc_except_tab: 0xa6c
-  __TEXT.__dlopen_cstrs: 0x168
+3500.91.1.1.1
+  __TEXT.__text: 0x4eb24
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x6014
+  __TEXT.__const: 0x822
+  __TEXT.__cstring: 0xa04d
+  __TEXT.__oslogstring: 0x6d03
+  __TEXT.__gcc_except_tab: 0xe40
+  __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x102
   __TEXT.__constg_swiftt: 0x160
   __TEXT.__swift5_reflstr: 0x2d

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1548
+  __TEXT.__unwind_info: 0x15f0
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x101d
-  __TEXT.__objc_methname: 0xdaae
-  __TEXT.__objc_methtype: 0x22af
-  __TEXT.__objc_stubs: 0x9280
-  __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x1628
+  __TEXT.__objc_methname: 0xdc5c
+  __TEXT.__objc_methtype: 0x23b0
+  __TEXT.__objc_stubs: 0x9480
+  __DATA_CONST.__got: 0x6a8
+  __DATA_CONST.__const: 0x1670
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d30
+  __DATA_CONST.__objc_selrefs: 0x2dd0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x530
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x5e8
-  __AUTH_CONST.__cfstring: 0x49a0
-  __AUTH_CONST.__objc_const: 0x9c60
-  __AUTH_CONST.__objc_intobj: 0x948
+  __AUTH_CONST.__cfstring: 0x49c0
+  __AUTH_CONST.__objc_const: 0x9ca0
+  __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x1c28
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x668
+  __DATA.__objc_ivar: 0x670
   __DATA.__data: 0xf98
-  __DATA.__bss: 0x4b0
+  __DATA.__bss: 0x510
   __DATA_DIRTY.__objc_data: 0x4b0
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 31D27213-3CD5-37FA-BE90-FBA2BE348D62
-  Functions: 2123
-  Symbols:   7273
-  CStrings:  4472
+  UUID: 56B80ED3-6CB4-38DB-841C-220EF4D3DCAE
+  Functions: 2164
+  Symbols:   7411
+  CStrings:  4530
 
Symbols:
+ -[SASMyriadController _resetMTAlarmObserver]
+ -[SASMyriadController _resetMTTimerObserver]
+ -[SASMyriadController _setFiringAlarmIfNeeded:]
+ -[SASMyriadController _setFiringTimerIfNeeded:]
+ -[SASMyriadController _startObservingMTAlarmNotifications]
+ -[SASMyriadController _startObservingMTTimerNotifications]
+ -[SASMyriadController _stopObservingMTAlarmNotifications]
+ -[SASMyriadController _stopObservingMTTimerNotifications]
+ -[SASMyriadController alarmsChanged:]
+ -[SASMyriadController alarmsReset:]
+ -[SASMyriadController timersChanged:]
+ -[SASMyriadController timersReset:]
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table70
+ _MobileTimerLibrary
+ _MobileTimerLibraryCore
+ _MobileTimerLibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_SASMyriadController._mobileClockObserver
+ _OBJC_IVAR_$_SASMyriadController._myriadWorkQueue
+ _SAInputOriginPresentedResponseInteractionValue
+ _SASRequestSourceFromSAInputOrigin
+ ___35-[SASMyriadController alarmsReset:]_block_invoke
+ ___35-[SASMyriadController timersReset:]_block_invoke
+ ___37-[SASMyriadController alarmsChanged:]_block_invoke
+ ___37-[SASMyriadController timersChanged:]_block_invoke
+ ___50-[SASMyriadController didChangeLockState:toState:]_block_invoke
+ ___54-[SASMyriadController _configureMotionActivityManager]_block_invoke.110
+ ___68-[SASMyriadController activateForRequest:withTimeout:visible:quiet:]_block_invoke.83
+ ___68-[SASMyriadController activateForRequest:withTimeout:visible:quiet:]_block_invoke.85
+ ___MobileTimerLibraryCore_block_invoke
+ ___block_descriptor_56_e8_32r40r48w_e5_v8?0lw48l8r32l8r40l8
+ ___destructor_8_s0_s8_s16_s24_s32_s40
+ ___getMTAlarmManagerAlarmsChangedSymbolLoc_block_invoke
+ ___getMTAlarmManagerAlarmsKeySymbolLoc_block_invoke
+ ___getMTAlarmManagerClass_block_invoke
+ ___getMTAlarmManagerClass_block_invoke.cold.1
+ ___getMTAlarmManagerStateResetSymbolLoc_block_invoke
+ ___getMTMutableAlarmClass_block_invoke
+ ___getMTMutableAlarmClass_block_invoke.cold.1
+ ___getMTMutableTimerClass_block_invoke
+ ___getMTMutableTimerClass_block_invoke.cold.1
+ ___getMTTimerManagerClass_block_invoke
+ ___getMTTimerManagerClass_block_invoke.cold.1
+ ___getMTTimerManagerStateResetSymbolLoc_block_invoke
+ ___getMTTimerManagerTimersChangedSymbolLoc_block_invoke
+ ___getMTTimerManagerTimersKeySymbolLoc_block_invoke
+ _audit_stringMobileTimer
+ _dispatch_activate
+ _dispatch_block_create_with_qos_class
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_set_qos_class_floor
+ _getMTAlarmManagerAlarmsChanged
+ _getMTAlarmManagerAlarmsChanged.cold.1
+ _getMTAlarmManagerAlarmsChangedSymbolLoc.ptr
+ _getMTAlarmManagerAlarmsKeySymbolLoc.ptr
+ _getMTAlarmManagerClass.softClass
+ _getMTAlarmManagerStateReset
+ _getMTAlarmManagerStateReset.cold.1
+ _getMTAlarmManagerStateResetSymbolLoc.ptr
+ _getMTMutableAlarmClass.softClass
+ _getMTMutableTimerClass.softClass
+ _getMTTimerManagerClass.softClass
+ _getMTTimerManagerStateReset
+ _getMTTimerManagerStateReset.cold.1
+ _getMTTimerManagerStateResetSymbolLoc.ptr
+ _getMTTimerManagerTimersChanged
+ _getMTTimerManagerTimersChanged.cold.1
+ _getMTTimerManagerTimersChangedSymbolLoc.ptr
+ _getMTTimerManagerTimersKeySymbolLoc.ptr
+ _objc_msgSend$_resetMTAlarmObserver
+ _objc_msgSend$_resetMTTimerObserver
+ _objc_msgSend$_setFiringAlarmIfNeeded:
+ _objc_msgSend$_setFiringTimerIfNeeded:
+ _objc_msgSend$_startObservingMTAlarmNotifications
+ _objc_msgSend$_startObservingMTTimerNotifications
+ _objc_msgSend$_stopObservingMTAlarmNotifications
+ _objc_msgSend$_stopObservingMTTimerNotifications
+ _objc_msgSend$alarmID
+ _objc_msgSend$dismissedDate
+ _objc_msgSend$firedDate
+ _objc_msgSend$isFiring
+ _objc_msgSend$isSleepAlarm
+ _objc_msgSend$isSnoozed
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$timerID
+ _qos_class_self
- GCC_except_table25
- ___54-[SASMyriadController _configureMotionActivityManager]_block_invoke.96
- ___68-[SASMyriadController activateForRequest:withTimeout:visible:quiet:]_block_invoke.81
CStrings:
+ "%s #myriad Firing alarms: %@, last firing dates: %@"
+ "%s #myriad Firing timers: %@, last firing dates: %@"
+ "%s #myriad alarm: %@, alarmID: %@, isSleepAlarm: %d, isFiring: %d, isSnoozed: %d fired date: %@, dismissed date: %@"
+ "%s #myriad getSCDAGoodnessScoreContext observed AFMediaPlaybackState %ld and interrupted time %f timer firing state %d and alarm firing state %d"
+ "%s #myriad ignoring alarm notifications %@, %@"
+ "%s #myriad ignoring timer notifications %@, %@"
+ "%s #myriad isTimerFiring = %d, firing timerID: %@, timer fired date: %@, isAlarmFiring = %d, firing alarmID: %@, alarm fired date: %@"
+ "%s #myriad observing alarm notifications: %@, %@"
+ "%s #myriad observing timer notifications: %@, %@"
+ "%s #myriad timer: %@, timerID: %@, isFiring: %d, fired date: %@ dismissed date: %@"
+ "-[SASMyriadController _resetMTAlarmObserver]"
+ "-[SASMyriadController _resetMTTimerObserver]"
+ "-[SASMyriadController _setFiringAlarmIfNeeded:]"
+ "-[SASMyriadController _setFiringTimerIfNeeded:]"
+ "-[SASMyriadController _startObservingMTAlarmNotifications]"
+ "-[SASMyriadController _startObservingMTTimerNotifications]"
+ "-[SASMyriadController _stopObservingMTAlarmNotifications]"
+ "-[SASMyriadController _stopObservingMTTimerNotifications]"
+ "-[SASMyriadController alarmsChanged:]"
+ "-[SASMyriadController alarmsReset:]_block_invoke"
+ "-[SASMyriadController timersChanged:]"
+ "-[SASMyriadController timersReset:]_block_invoke"
+ "MTAlarmManager"
+ "MTAlarmManagerAlarmsChanged"
+ "MTAlarmManagerAlarmsKey"
+ "MTAlarmManagerStateReset"
+ "MTMutableAlarm"
+ "MTMutableTimer"
+ "MTTimerManager"
+ "MTTimerManagerStateReset"
+ "MTTimerManagerTimersChanged"
+ "MTTimerManagerTimersKey"
+ "SASRequestSourcePresentedResponseInteraction"
+ "_mobileClockObserver"
+ "_myriadWorkQueue"
+ "_resetMTAlarmObserver"
+ "_resetMTTimerObserver"
+ "_setFiringAlarmIfNeeded:"
+ "_setFiringTimerIfNeeded:"
+ "_startObservingMTAlarmNotifications"
+ "_startObservingMTTimerNotifications"
+ "_stopObservingMTAlarmNotifications"
+ "_stopObservingMTTimerNotifications"
+ "alarmID"
+ "alarmsChanged:"
+ "alarmsReset:"
+ "com.siri-activation.myriad-work-queue"
+ "dismissedDate"
+ "firedDate"
+ "isFiring"
+ "isSleepAlarm"
+ "isSnoozed"
+ "removeObserver:name:object:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer"
+ "timerID"
+ "timersChanged:"
+ "timersReset:"
+ "{?=\"timerManager\"@\"MTTimerManager\"\"alarmManager\"@\"MTAlarmManager\"\"lastFiringTimerIDs\"@\"NSMutableSet\"\"lastFiringAlarmIDs\"@\"NSMutableSet\"\"lastTimerFiringDates\"@\"NSMutableDictionary\"\"lastAlarmFiringDates\"@\"NSMutableDictionary\"\"isTimerFiring\"B\"isAlarmFiring\"B}"
- "%s #myriad getSCDAGoodnessScoreContext observed AFMediaPlaybackState %ld and interrupted time %f"

```
