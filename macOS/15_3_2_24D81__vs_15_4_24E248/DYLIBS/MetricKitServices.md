## MetricKitServices

> `/System/Library/PrivateFrameworks/MetricKitServices.framework/Versions/A/MetricKitServices`

```diff

-259.40.2.0.0
-  __TEXT.__text: 0x46e4
+261.0.0.0.0
+  __TEXT.__text: 0x4698
   __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_methlist: 0x4fc
   __TEXT.__const: 0x70

   - /System/Library/PrivateFrameworks/MetricKitSource.framework/Versions/A/MetricKitSource
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF3D67D1-58F2-3352-8DA0-2BAFF76F5121
-  Functions: 119
-  Symbols:   311
+  UUID: 9143BF3A-16B3-3EDF-9362-ED734CD92D16
+  Functions: 122
+  Symbols:   314
   CStrings:  232
 
Symbols:
+ +[MXUtilities containerPath].cold.1
+ +[MXUtilities modelIdentifier].cold.1
+ +[MXUtilities platformArchitecture].cold.1
Functions:
~ -[MXSpinTracerService init] : 264 -> 260
~ -[MXSpinTracerService unarchiveSpinTracerDataForDateString:] : 1500 -> 1492
~ -[MXService startService] : 28 -> 24
~ -[MXService pruneSourceData:] : 44 -> 8
~ -[MXHangTracerService init] : 264 -> 260
~ -[MXHangTracerService unarchiveHangTracerDataForDateString:] : 1500 -> 1492
~ -[MXPowerlogService init] : 264 -> 260
~ -[MXPowerlogService unarchivePowerlogData] : 1068 -> 1060
~ -[MXReportCrashService init] : 264 -> 260
~ -[MXReportCrashService unarchiveReportCrashDataForDateString:] : 1500 -> 1492
~ +[MXUtilities containerPath] : 84 -> 68
~ +[MXUtilities modelIdentifier] : 84 -> 68
~ +[MXUtilities platformArchitecture] : 84 -> 68
+ +[MXUtilities containerPath].cold.1

```
