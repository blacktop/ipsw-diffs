## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

 696.0.1.0.0
-  __TEXT.__text: 0xc2244
+  __TEXT.__text: 0xc22c8
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_methlist: 0x1b6b4
-  __TEXT.__const: 0x528
-  __TEXT.__cstring: 0xe105
+  __TEXT.__const: 0x538
+  __TEXT.__cstring: 0xe111
   __TEXT.__oslogstring: 0xbf0a
   __TEXT.__gcc_except_tab: 0x125c
   __TEXT.__unwind_info: 0x1ce0

   __DATA_CONST.__objc_arraydata: 0x6fb8
   __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0xbd80
+  __AUTH_CONST.__cfstring: 0xbdc0
   __AUTH_CONST.__objc_const: 0x36420
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_arrayobj: 0x3a8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A453BBA2-139A-30DD-953F-569A69402034
+  UUID: 9E4A91AD-1428-348C-8D4F-CEE34D8B940F
   Functions: 9789
   Symbols:   26858
-  CStrings:  8891
+  CStrings:  8895
 
Symbols:
+ ___101+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:ignoringDisconnectsShorterThan:]_block_invoke.39
+ ___101+[PowerUISmartChargeUtilities timestampOfFirstEventReachingBatteryLevel:betweenStartTime:andEndTime:]_block_invoke.82
+ ___132+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:withMinimumPlugoutBatteryLevel:ignoringDisconnectsShorterThan:]_block_invoke.46
+ ___132+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:withMinimumPlugoutBatteryLevel:ignoringDisconnectsShorterThan:]_block_invoke.46.cold.1
+ ___48+[PowerUISmartChargeUtilities lastPluggedInDate]_block_invoke.192
+ ___50+[PowerUISmartChargeUtilities batteryLevelAtDate:]_block_invoke.186
+ ___56+[PowerUISmartChargeUtilities getBatteryLevelDurations:]_block_invoke.23
+ ___56+[PowerUISmartChargeUtilities getBatteryLevelDurations:]_block_invoke.23.cold.1
+ ___96+[PowerUISmartChargeUtilities historicalFullChargeDurationStartingAt:withMinimumPluginDuration:]_block_invoke.85
+ ___97+[PowerUISmartChargeUtilities drainSessionsInfoBetweenRelevantChargesBefore:withMinimumDuration:]_block_invoke.54
+ ___block_literal_global.137
+ ___block_literal_global.185
+ ___block_literal_global.191
+ ___block_literal_global.31
+ ___block_literal_global.38
+ ___block_literal_global.45
+ ___block_literal_global.53
+ ___block_literal_global.84
+ ___block_literal_global.87
- ___101+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:ignoringDisconnectsShorterThan:]_block_invoke.38
- ___101+[PowerUISmartChargeUtilities timestampOfFirstEventReachingBatteryLevel:betweenStartTime:andEndTime:]_block_invoke.81
- ___132+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:withMinimumPlugoutBatteryLevel:ignoringDisconnectsShorterThan:]_block_invoke.45
- ___132+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:withMinimumPlugoutBatteryLevel:ignoringDisconnectsShorterThan:]_block_invoke.45.cold.1
- ___48+[PowerUISmartChargeUtilities lastPluggedInDate]_block_invoke.191
- ___50+[PowerUISmartChargeUtilities batteryLevelAtDate:]_block_invoke.185
- ___56+[PowerUISmartChargeUtilities getBatteryLevelDurations:]_block_invoke.22
- ___56+[PowerUISmartChargeUtilities getBatteryLevelDurations:]_block_invoke.22.cold.1
- ___96+[PowerUISmartChargeUtilities historicalFullChargeDurationStartingAt:withMinimumPluginDuration:]_block_invoke.84
- ___97+[PowerUISmartChargeUtilities drainSessionsInfoBetweenRelevantChargesBefore:withMinimumDuration:]_block_invoke.53
- ___block_literal_global.136
- ___block_literal_global.148
- ___block_literal_global.184
- ___block_literal_global.190
- ___block_literal_global.37
- ___block_literal_global.44
- ___block_literal_global.52
- ___block_literal_global.83
- ___block_literal_global.86
Functions:
~ +[PowerUISmartChargeUtilities isUltraWatch] : 156 -> 196
~ -[PowerUIBluetoothHandler isAccessorySupported:] : 52 -> 64
~ -[PowerUIAudioAccessorySmartChargeManager nameForProductID:] : 348 -> 396
~ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2043 : 1044 -> 1076
CStrings:
+ "B788"
+ "B788CH"

```
