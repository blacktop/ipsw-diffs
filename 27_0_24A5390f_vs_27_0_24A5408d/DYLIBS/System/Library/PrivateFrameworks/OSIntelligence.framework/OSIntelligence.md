## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-284.0.0.0.0
-  __TEXT.__text: 0x1a5e8
-  __TEXT.__objc_methlist: 0x2290
-  __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x1a4a
-  __TEXT.__oslogstring: 0x2609
-  __TEXT.__gcc_except_tab: 0x6a8
-  __TEXT.__unwind_info: 0x9b8
+286.0.0.0.0
+  __TEXT.__text: 0x1b5dc
+  __TEXT.__objc_methlist: 0x2338
+  __TEXT.__const: 0x1b8
+  __TEXT.__cstring: 0x1b54
+  __TEXT.__oslogstring: 0x2820
+  __TEXT.__gcc_except_tab: 0x6c8
+  __TEXT.__unwind_info: 0x9e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1208
+  __DATA_CONST.__objc_selrefs: 0x1278
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x1f8
   __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x1580
-  __AUTH_CONST.__objc_const: 0x30e8
+  __AUTH_CONST.__cfstring: 0x1660
+  __AUTH_CONST.__objc_const: 0x3188
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1d8
+  __DATA.__objc_ivar: 0x1e4
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 921
-  Symbols:   1786
-  CStrings:  438
+  Functions: 938
+  Symbols:   1814
+  CStrings:  455
 
Symbols:
+ -[_OSBatteryPredictor currentBatteryDrainAggregatedOverTimeWidth:withError:]
+ -[_OSBatteryPredictor typicalBatteryDrainWithReferenceDays:aggregatedOverTimeWidth:withError:]
+ -[_OSIBLManager doubleValueForTrialFactor:withDefault:]
+ -[_OSIBLManager isCurrentDrainUnusual]
+ -[_OSIBLManager notificationDefaults]
+ -[_OSIBLManager recentUnusualDrainPostDatesWithinWindow]
+ -[_OSIBLManager recordUnusualDrainPostAtDate:]
+ -[_OSIBLManager setNotificationDefaults:]
+ -[_OSIBLManager setUnusualDrainRampUpFraction:]
+ -[_OSIBLManager setUnusualDrainStartingThreshold:]
+ -[_OSIBLManager unusualDrainRampUpFraction]
+ -[_OSIBLManager unusualDrainStartingThreshold]
+ _OBJC_IVAR_$__OSIBLManager._notificationDefaults
+ _OBJC_IVAR_$__OSIBLManager._unusualDrainRampUpFraction
+ _OBJC_IVAR_$__OSIBLManager._unusualDrainStartingThreshold
+ _OUTLINED_FUNCTION_9
+ ___76-[_OSBatteryPredictor currentBatteryDrainAggregatedOverTimeWidth:withError:]_block_invoke
+ ___94-[_OSBatteryPredictor typicalBatteryDrainWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke
+ ___NSArray0__struct
+ _objc_msgSend$array
+ _objc_msgSend$currentBatteryDrainAggregatedOverTimeWidth:withError:
+ _objc_msgSend$currentBatteryDrainAggregatedOverTimeWidth:withHandler:
+ _objc_msgSend$doubleValueForTrialFactor:withDefault:
+ _objc_msgSend$isCurrentDrainUnusual
+ _objc_msgSend$recentUnusualDrainPostDatesWithinWindow
+ _objc_msgSend$recordUnusualDrainPostAtDate:
+ _objc_msgSend$typicalBatteryDrainWithReferenceDays:aggregatedOverTimeWidth:withError:
+ _objc_msgSend$typicalBatteryDrainWithReferenceDays:aggregatedOverTimeWidth:withHandler:
+ _objc_retain_x26
- _objc_msgSend$distantPast
CStrings:
+ "Drain check slot %lu (hour %lu): current %f vs median %f + threshold %f -> %{public}s"
+ "Drain slot %lu out of range (typical=%lu, current=%lu); skipping"
+ "IBLM_UnusualDrainRampUpFraction"
+ "IBLM_UnusualDrainStartingThreshold"
+ "Local hour %lu before start hour %lu; skipping unusual-drain notification"
+ "Not enough drain data (typicalErr: %@, currentErr: %@); skipping"
+ "Notified for IBLM onboarding notification"
+ "Notified for IBLM unusual-drain notification"
+ "Onboarding IBLM notification already posted once; skipping"
+ "Unusual-drain notification posted %lu times in the last %.0f days; skipping"
+ "Unusual-drain notification within %.0f-day cooldown; skipping"
+ "com.apple.osi.iblm.unusualDrainNotification"
+ "com.apple.osintelligence.iblm.notifications"
+ "kDidPostOnboardingNotification"
+ "kDidRecordFirstUnusualDrainTrigger"
+ "normal"
+ "unusual"
+ "unusualDrainNotificationDates"
- "Notified for IBLM Engaged notification"
```
