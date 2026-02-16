## libIOReport.dylib

> `/usr/lib/libIOReport.dylib`

```diff

 107.0.0.0.0
-  __TEXT.__text: 0x6f04
+  __TEXT.__text: 0x6e38
   __TEXT.__auth_stubs: 0x550
   __TEXT.__cstring: 0x922
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0x174
-  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__unwind_info: 0x200
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x2b8
   __AUTH_CONST.__auth_got: 0x2a8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 159CA5AE-DE24-31EF-B829-8D51A2C7FC30
-  Functions: 136
-  Symbols:   342
+  UUID: F665581C-F912-3699-9A0C-1ABA882AF49C
+  Functions: 138
+  Symbols:   344
   CStrings:  204
 
Symbols:
+ _OUTLINED_FUNCTION_7
Functions:
~ __visitSample : 556 -> 564
~ __compareSamples : 1264 -> 1252
~ __iterSubDicts : 368 -> 380
~ _copyUnitLabel : 1112 -> 1036
+ sub_2a3a92308
~ _OUTLINED_FUNCTION_0 : 40 -> 56
~ _OUTLINED_FUNCTION_1 : 48 -> 20
~ _OUTLINED_FUNCTION_2 : 24 -> 20
~ _OUTLINED_FUNCTION_3 : 12 -> 16
~ _OUTLINED_FUNCTION_4 : 24 -> 12
+ _OUTLINED_FUNCTION_7
~ __iterateMatches : 228 -> 220
~ __IOReportCopyChannelsForDriver : 868 -> 844
~ ___IOReportCopyFilteredChannels_block_invoke : 172 -> 180
~ __findAddDict : 144 -> 140
~ _IOReportIterateSamplesRaw.cold.1 : 132 -> 116
~ __visitSample.cold.1 : 192 -> 200
~ ___IOReportUpdateSamplesRaw_block_invoke.cold.1 : 160 -> 124
~ ___IOReportUpdateSamplesRaw_block_invoke.cold.2 : 160 -> 124
~ ___IOReportUpdateSamplesRaw_block_invoke.cold.3 : 156 -> 120
~ ___IOReportUpdateSamplesRaw_block_invoke.cold.4 : 156 -> 120

```
