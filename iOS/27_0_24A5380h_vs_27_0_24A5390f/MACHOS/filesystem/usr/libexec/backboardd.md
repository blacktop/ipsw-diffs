## backboardd

> `/usr/libexec/backboardd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-868.0.0.0.0
-  __TEXT.__text: 0x56f34
+873.100.0.0.0
+  __TEXT.__text: 0x58298
   __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_stubs: 0x9c80
-  __TEXT.__objc_methlist: 0x4924
+  __TEXT.__objc_stubs: 0x9e20
+  __TEXT.__objc_methlist: 0x49a4
   __TEXT.__const: 0x320
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__gcc_except_tab: 0x730
-  __TEXT.__objc_methname: 0xd8c9
+  __TEXT.__gcc_except_tab: 0x770
+  __TEXT.__objc_methname: 0xdb53
   __TEXT.__objc_classname: 0x1368
-  __TEXT.__cstring: 0x4b68
-  __TEXT.__objc_methtype: 0x2e2e
-  __TEXT.__oslogstring: 0x6f39
-  __TEXT.__unwind_info: 0x1578
-  __DATA_CONST.__const: 0x3278
-  __DATA_CONST.__cfstring: 0x4f60
+  __TEXT.__cstring: 0x4c7f
+  __TEXT.__objc_methtype: 0x2eb6
+  __TEXT.__oslogstring: 0x704c
+  __TEXT.__unwind_info: 0x15c8
+  __DATA_CONST.__const: 0x32f0
+  __DATA_CONST.__cfstring: 0x5020
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__objc_intobj: 0x228
+  __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xab8
-  __DATA_CONST.__got: 0x878
+  __DATA_CONST.__got: 0x890
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xaca0
-  __DATA.__objc_selrefs: 0x3058
-  __DATA.__objc_ivar: 0x7d4
+  __DATA.__objc_const: 0xad88
+  __DATA.__objc_selrefs: 0x30c8
+  __DATA.__objc_ivar: 0x7f0
   __DATA.__objc_data: 0x1fe0
   __DATA.__data: 0x1ac8
   __DATA.__bss: 0x328

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 1880
-  Symbols:   614
-  CStrings:  4039
+  Functions: 1897
+  Symbols:   617
+  CStrings:  4079
 
Symbols:
+ _OBJC_CLASS_$_BKSHardwareButtonLongPressDescriptor
+ _OBJC_CLASS_$_BSContinuousMachTimer
+ ___NSArray0__struct
CStrings:
+ " 0x%X/0x%X/%llX long press: emitting synthesized long press"
+ "%s: error unarchiving long press timeouts"
+ "@\"BSContinuousMachTimer\""
+ "CBUIBrightnessNotificationTakenOver"
+ "ConfigA"
+ "ConfigB"
+ "CoreBrightness owns UIBacklightLevelChangedNotification; backboardd will not post it"
+ "LockButton"
+ "SmartCover"
+ "_BKHIDXXSetButtonLongPressTimeouts"
+ "_BKHIDXXSetButtonLongPressTimeouts_block_invoke"
+ "_coreBrightnessOwnsUINotification"
+ "_didEmitLongPress"
+ "_lock_armLongPressTimerForRecord:senderID:page:usage:timeout:"
+ "_lock_cancelLongPressTimerForRecord:"
+ "_lock_effectiveLongPressTimeoutsByUsageKey"
+ "_lock_ensureDeathWatcherForPID:"
+ "_lock_longPressTimeoutsByPID"
+ "_lock_pidToDeathWatcher"
+ "_lock_recomputeEffectiveTimeouts"
+ "_lock_removeDeathWatcherForPID:"
+ "_longPressTimer"
+ "_longPressTimerFiredForSenderID:page:usage:record:"
+ "_longPressTimerQueue"
+ "_probeCoverSensorsFromContext:deviceUsagePage:deviceUsage:available:engaged:attached:unknownState:"
+ "addEntriesFromDictionary:"
+ "com.apple.backboard.button-long-press.0x%X/0x%X"
+ "com.apple.backboardd.button-long-press"
+ "hoistOnThread:forSessionID:"
+ "long press timeouts for pid %d removed"
+ "long press timeouts for pid %d set to %{public}@"
+ "removeLongPressTimeoutsForPID:"
+ "setLongPressTimeouts:forPID:"
+ "timeout"
+ "v16@?0@\"BSContinuousMachTimer\"8"
+ "v28@0:8@?16I24"
+ "v28@0:8@?<v@?>16I24"
+ "v40@0:8Q16S24S28@32"
+ "v48@0:8@16Q24S32S36d40"
+ "v64@0:8@16I24I28^Q32^Q40^B48^B56"
+ "\x81"
- "_eventRecords"
```
