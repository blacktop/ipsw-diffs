## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-623.0.0.0.0
-  __TEXT.__text: 0xb30bc
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x19d0c
-  __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0xd29c
-  __TEXT.__oslogstring: 0x95a3
-  __TEXT.__gcc_except_tab: 0x11e0
-  __TEXT.__unwind_info: 0x1a20
-  __TEXT.__objc_classname: 0xa7e
-  __TEXT.__objc_methname: 0x3cd68
-  __TEXT.__objc_methtype: 0x3fbb
-  __TEXT.__objc_stubs: 0xbd80
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x1388
-  __DATA_CONST.__objc_classlist: 0x2b0
+631.0.0.0.0
+  __TEXT.__text: 0xb5d5c
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x19fcc
+  __TEXT.__const: 0x4e0
+  __TEXT.__cstring: 0xd54d
+  __TEXT.__oslogstring: 0x97d2
+  __TEXT.__gcc_except_tab: 0x1230
+  __TEXT.__unwind_info: 0x1ab0
+  __TEXT.__objc_classname: 0xac1
+  __TEXT.__objc_methname: 0x3d240
+  __TEXT.__objc_methtype: 0x400b
+  __TEXT.__objc_stubs: 0xc000
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x1400
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4da0
+  __DATA_CONST.__objc_selrefs: 0x4eb8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x6e70
-  __AUTH_CONST.__auth_got: 0x578
-  __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0xae80
-  __AUTH_CONST.__objc_const: 0x361a0
-  __AUTH_CONST.__objc_intobj: 0x810
+  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__const: 0x640
+  __AUTH_CONST.__cfstring: 0xb100
+  __AUTH_CONST.__objc_const: 0x36a60
+  __AUTH_CONST.__objc_intobj: 0x858
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x3af8
+  __AUTH.__objc_data: 0x1270
+  __DATA.__objc_ivar: 0x3b34
   __DATA.__data: 0x6c0
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x148
+  __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/ContextSync.framework/ContextSync
   - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9393
-  Symbols:   9890
-  CStrings:  6876
+  Functions: 9467
+  Symbols:   9973
+  CStrings:  6976
 
Symbols:
+ _OBJC_CLASS_$_BrightnessSystemClient
+ _OBJC_CLASS_$_PowerUIBatteryData
+ _OBJC_CLASS_$_PowerUIBrightnessController
+ _OBJC_CLASS_$_PowerUIDrainMonitor
+ _OBJC_METACLASS_$_PowerUIBatteryData
+ _OBJC_METACLASS_$_PowerUIBrightnessController
+ _OBJC_METACLASS_$_PowerUIDrainMonitor
+ _notify_set_state
CStrings:
+ "\x13j"
+ "%!@(MISSING) Enable LPM!!"
+ "@\"BrightnessSystemClient\""
+ "@32@0:8Q16Q24"
+ "Added Slot %!l(MISSING)d, battery level %!l(MISSING)d"
+ "Brightness"
+ "Brightness string is null"
+ "Capping max brightness to %!l(MISSING)f"
+ "Confidence override exists: %!f(MISSING)"
+ "Current battery level %!l(MISSING)u"
+ "Current battery level %!l(MISSING)u, Reference level %!l(MISSING)u"
+ "DisplayBrightness"
+ "DisplayBrightnessMax"
+ "Duration override exists: %!f(MISSING)"
+ "E-T-Insights://"
+ "Internal method called on non-internal build"
+ "Not enough variation in the values. Min %!@(MISSING), Max %!@(MISSING)"
+ "Posted LPM notification "
+ "Posted LPM notification in last 12 hours; Skipping"
+ "Posting LPM notification %!@(MISSING)"
+ "PowerUIBatteryData"
+ "PowerUIBrightnessController"
+ "PowerUIDrainMonitor"
+ "PowerUIDrainMonitor initiating..."
+ "Q32@0:8@16Q24"
+ "Reducing brightness from %!l(MISSING)f to %!l(MISSING)f"
+ "Slot %!l(MISSING)d, battery level %!l(MISSING)d"
+ "SmartChargeClient setState timed out!"
+ "T@\"BrightnessSystemClient\",&,N,V_bClient"
+ "T@\"NSMutableDictionary\",&,N,V_dateToWeekdayMedian"
+ "T@\"NSMutableDictionary\",&,N,V_dateToWeekendMedian"
+ "T@\"NSMutableDictionary\",&,N,V_yesterdayReference"
+ "T@\"NSNumber\",&,N,V_confidenceOverride"
+ "T@\"NSNumber\",&,N,V_durationOverride"
+ "TB,N,V_mitigationEngaged"
+ "Ti,N,V_notifyToken"
+ "Your battery level is trending lower than typical!(Current:%!l(MISSING)d Typical:%!l(MISSING)d)"
+ "[Internal] Low Power Mode"
+ "_bClient"
+ "_confidenceOverride"
+ "_dateToWeekdayMedian"
+ "_dateToWeekendMedian"
+ "_durationOverride"
+ "_mitigationEngaged"
+ "_notifyToken"
+ "_yesterdayReference"
+ "bClient"
+ "battery.25percent"
+ "batteryData"
+ "batteryLevelByTimeSlot:dayType:"
+ "brightnessController"
+ "com.apple.PowerUIAgent.contextstore-registration"
+ "com.apple.powerui-internal-notification:%!l(MISSING)f"
+ "com.apple.powerui.brightnessController"
+ "com.apple.powerui.drainMonitor"
+ "com.apple.powerui.drainmonitor.notification"
+ "com.apple.powerui.nudge.LPM"
+ "com.apple.powerui.powerUIDrainMonitor"
+ "confidenceOverride"
+ "copyPropertyForKey:"
+ "currentLevel"
+ "dateBySettingUnit:value:ofDate:options:"
+ "dateToWeekdayMedian"
+ "dateToWeekendMedian"
+ "durationOverride"
+ "engageMitigation"
+ "evaluateNudgeForLPM"
+ "hasVariationForMedianLevels:"
+ "ignoreLastNudge"
+ "isDateInWeekend:"
+ "isTrendingLowerWithBatteryLevel:atDate:"
+ "isWeekend:"
+ "kLastALPMNotificationDate"
+ "keyPathForLowPowerModeStatus"
+ "medianBatteryLevelByTimeSlot:dayType:"
+ "midnightDateFrom:"
+ "mitigationEngaged"
+ "notifyToken"
+ "objectForContextualKeyPath:"
+ "postInternalNotificationAtDate:withTitle:withTextContent:icon:url:expirationDate:"
+ "postLPMNudgeNotificationWithInfo:"
+ "powerUIDrainMonitor"
+ "powerUIInternal"
+ "referenceLevel"
+ "removeAllObjects"
+ "resetMitigation"
+ "setBClient:"
+ "setConfidenceOverride:"
+ "setDateToWeekdayMedian:"
+ "setDateToWeekendMedian:"
+ "setDurationOverride:"
+ "setMitigationEngaged:"
+ "setNotifyToken:"
+ "setProperty:forKey:"
+ "setYesterdayReference:"
+ "shouldEngage"
+ "slotForDate:withTimeSlotWidth:"
+ "twoStageModelConfidenceOverride"
+ "twoStageModelDurationOverride"
+ "v64@0:8@16@24@32@40@48@56"
+ "yesterdayReference"
- "\x13h"
- "checkForSufficientBTConnectionEventsUpTo:forDevice:"

```
