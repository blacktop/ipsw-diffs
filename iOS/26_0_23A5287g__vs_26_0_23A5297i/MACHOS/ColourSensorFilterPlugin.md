## ColourSensorFilterPlugin

> `/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin`

```diff

-2079.0.27.0.0
-  __TEXT.__text: 0x1478c
+2079.0.34.0.0
+  __TEXT.__text: 0x14a24
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__const: 0x4d0
-  __TEXT.__cstring: 0x12aa
-  __TEXT.__oslogstring: 0x1cd0
-  __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__const: 0x4c0
+  __TEXT.__cstring: 0x12bb
+  __TEXT.__oslogstring: 0x1d2f
+  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__unwind_info: 0x370
   __DATA_CONST.__auth_got: 0x488
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 537A50E9-0048-34F3-8F4A-95266525A7B3
-  Functions: 256
-  Symbols:   299
-  CStrings:  461
+  UUID: 4187450D-4FBB-32CE-B2F0-205C4EE99585
+  Functions: 259
+  Symbols:   300
+  CStrings:  465
 
Symbols:
+ __ZN17ColorSensorPlugIn16copyFDRInstancesEPK10__CFStringbb
CStrings:
+ "ID in FDR calibration (0x%x) doesn't match with chip ID (0x%x), will still try to process available calibration.\n"
+ "[%s] [%{public}@] [SealingManifest] Failed!"
+ "[%s] [%{public}@] [SealingManifest] Failed! Error: %@."
+ "[%s] [%{public}@] [SealingManifest] Succeeded! Instances: %@."
+ "[%s] [%{public}@] [SealingMap] Failed!"
+ "[%s] [%{public}@] [SealingMap] Failed! Error: %@."
+ "[%s] [%{public}@] [SealingMap] Succeeded! Instances: %@."
+ "copyFDRInstances"
- "AMFDRSealingMapCopyMultiInstanceForClass for key %@ failed with error %@"
- "AMFDRSealingMapCopyMultiInstanceForClass for key %@ succeeded."
- "ID in FDR calibration (0x%x) doesn't match with chip ID (0x%x) -> calibration will be skipped.\n"
- "[0x%llx] AMFDRSealingManifestCopyMultiInstanceForClass found %d instances for key %{public}@."

```
