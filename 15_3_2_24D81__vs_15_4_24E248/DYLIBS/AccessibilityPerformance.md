## AccessibilityPerformance

> `/System/Library/PrivateFrameworks/AccessibilityPerformance.framework/Versions/A/AccessibilityPerformance`

```diff

-387.5.2.0.0
+387.7.3.0.0
   __TEXT.__text: 0x4b00
   __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_methlist: 0x600
+  __TEXT.__objc_methlist: 0x64c
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x3dc
   __TEXT.__oslogstring: 0x1d7

   __AUTH_CONST.__auth_got: 0x108
   __AUTH_CONST.__const: 0x70
   __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0xf58
+  __AUTH_CONST.__objc_const: 0xee0
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SignpostSupport.framework/Versions/A/SignpostSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC7BC018-CC6B-3A74-8EAA-16B1AAD0E8BB
-  Functions: 128
-  Symbols:   484
+  UUID: BA88DBDF-E1B1-3F04-8290-687678180435
+  Functions: 130
+  Symbols:   486
   CStrings:  405
 
Symbols:
+ +[AXPSignpostUtility convertMachTimeToSeconds:].cold.1
+ axp_log_performance.cold.1
Functions:
~ -[AXPSignpostParser _allSignpostObjectsFromTestArchiveWithSubsystemCategoryFilter:archivePath:] : 584 -> 580
~ +[AXPSignpostTestUtility _outputCSVForPerformanceTestResults:includeCSVDelimiters:includeTestInfo:saveToFile:] : 584 -> 580
~ +[AXPSignpostUtility convertMachTimeToSeconds:] : 88 -> 72
~ _axp_log_performance : 84 -> 68

```
