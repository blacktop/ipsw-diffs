## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-702.120.3.0.0
-  __TEXT.__text: 0xdc6e0
+702.122.1.0.0
+  __TEXT.__text: 0xdc808
   __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_methlist: 0x1cce4
   __TEXT.__const: 0x670
   __TEXT.__cstring: 0xee92
-  __TEXT.__oslogstring: 0xd806
+  __TEXT.__oslogstring: 0xd8a2
   __TEXT.__gcc_except_tab: 0x12b8
   __TEXT.__unwind_info: 0x27a0
   __TEXT.__objc_classname: 0xd3a

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74F5FBEB-A1FC-3FB9-B202-3F627587E367
-  Functions: 10384
-  Symbols:   28620
-  CStrings:  9706
+  UUID: B570FF90-08EA-3F9B-AE5A-0AA2100977F8
+  Functions: 10386
+  Symbols:   28622
+  CStrings:  9708
 
Symbols:
+ -[PowerUICECGridDataManager forecastFromDefaults].cold.1
+ -[PowerUICECGridDataManager intervalStartTimesOverForecastHorizon:].cold.1
Functions:
~ -[PowerUICECGridDataManager forecastFromDefaults] : 628 -> 700
~ -[PowerUICECGridDataManager intervalStartTimesOverForecastHorizon:] : 344 -> 444
+ -[PowerUICECGridDataManager forecastFromDefaults].cold.1
+ -[PowerUICECGridDataManager intervalStartTimesOverForecastHorizon:].cold.1
CStrings:
+ "Failed to parse forecast date string '%@' from defaults. Discarding stored forecast."
+ "Forecast entry has nil date — discarding interval start times array."

```
