## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-753.0.17.0.0
-  __TEXT.__text: 0xd7498
+753.40.6.0.0
+  __TEXT.__text: 0xd7504
   __TEXT.__objc_methlist: 0x1d764
   __TEXT.__const: 0x6e0
   __TEXT.__cstring: 0xf815
-  __TEXT.__oslogstring: 0xf137
+  __TEXT.__oslogstring: 0xf16f
   __TEXT.__gcc_except_tab: 0x10c0
   __TEXT.__unwind_info: 0x2ce0
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 10656
   Symbols:   17599
-  CStrings:  3213
+  CStrings:  3214
 
Symbols:
+ -[PowerUISmartChargeManager loadDefaultsIsInitialLoad:]
+ _objc_msgSend$loadDefaultsIsInitialLoad:
- -[PowerUISmartChargeManager loadDefaults]
- _objc_msgSend$loadDefaults
Functions:
~ +[PowerUISmartChargeUtilities totalPluginDurationAfter:withMinimumDuration:withPluginEvents:] : 364 -> 360
~ -[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:] : 6668 -> 6672
~ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1120 -> ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.754 : 48 -> 132
~ -[PowerUISmartChargeManager loadDefaults] -> -[PowerUISmartChargeManager loadDefaultsIsInitialLoad:] : 2688 -> 2712
CStrings:
+ "Reloading defaults due to defaults-changed notification"
```
