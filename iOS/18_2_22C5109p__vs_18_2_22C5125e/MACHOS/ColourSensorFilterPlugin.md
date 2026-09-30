## ColourSensorFilterPlugin

> `/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin`

```diff

-1850.60.91.0.0
-  __TEXT.__text: 0x13a88
-  __TEXT.__auth_stubs: 0x8b0
+1850.60.94.0.0
+  __TEXT.__text: 0x1440c
+  __TEXT.__auth_stubs: 0x8d0
   __TEXT.__const: 0x550
-  __TEXT.__cstring: 0x11ef
-  __TEXT.__oslogstring: 0x1be9
-  __TEXT.__gcc_except_tab: 0x2b0
-  __TEXT.__unwind_info: 0x300
-  __DATA_CONST.__auth_got: 0x460
+  __TEXT.__cstring: 0x11f5
+  __TEXT.__oslogstring: 0x1c83
+  __TEXT.__gcc_except_tab: 0x2c8
+  __TEXT.__unwind_info: 0x320
+  __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x350
-  __DATA_CONST.__cfstring: 0x760
+  __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x80
   __DATA.__bss: 0x90

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 226
-  Symbols:   284
-  CStrings:  380
+  Functions: 236
+  Symbols:   287
+  CStrings:  384
 
Symbols:
+ _AMFDRSealingMapCopyLocalDict
+ _CFDictionaryGetValue
+ __ZN17ColorSensorPlugIn32copyDataFromCalibrationInstancesEPK10__CFStringPK9__CFArrayiRhS6_Ry
CStrings:
+ "AlsC"
+ "AlsC FDR calibration parsed = %!d(MISSING)"
+ "BIG: Failed to open big DB (result = %!d(MISSING))."
+ "Error creating calibration."
+ "Failed to send the calibration to the ALS driver."
+ "[0x%!l(MISSING)lx] %!{(MISSING)public}@ CFSN 0x%!l(MISSING)lx - placement match, orientation %!s(MISSING)match"
+ "[0x%!l(MISSING)lx] %!{(MISSING)public}@ CFSN 0x%!l(MISSING)lx does not match."
+ "[0x%!l(MISSING)lx] AMFDRSealingManifestCopyMultiInstanceForClass found %!d(MISSING) instances for key %!{(MISSING)public}@."
+ "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData (index = %!d(MISSING)) for key %!{(MISSING)public}@ failed with error %!@(MISSING)"
+ "[0x%!l(MISSING)lx] CFSN = 0x%!l(MISSING)lx"
+ "[0x%!l(MISSING)lx] Found matched %!{(MISSING)public}@ CFSN 0x%!l(MISSING)lx"
+ "[0x%!l(MISSING)lx] channel[%!z(MISSING)u]: luxCoeff = %!f(MISSING), darkCounts = %!d(MISSING), offsetCounts = %!f(MISSING), azOffsetCounts = %!d(MISSING), blHighCounts = %!d(MISSING)"
+ "doesn't "
- "Error creating calibration calibration"
- "[0x%!l(MISSING)lx] AMFDRSealingManifestCopyMultiInstanceForClass found %!d(MISSING) instances for key %!@(MISSING)."
- "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData (index = %!d(MISSING)) for key %!@(MISSING) failed with error %!@(MISSING)"
- "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData for key %!@(MISSING) failed with error %!@(MISSING)"
- "[0x%!l(MISSING)lx] AMFDRSealingMapCopyLocalData for key %!@(MISSING) succeeded."
- "[0x%!l(MISSING)lx] Found matched HmCA CFSN 0x%!l(MISSING)lx"
- "[0x%!l(MISSING)lx] HmCA CFSN 0x%!l(MISSING)lx - placement match, orientation %!s(MISSING)match"
- "[0x%!l(MISSING)lx] HmCA CFSN 0x%!l(MISSING)lx does not match."
- "doesn't"

```
