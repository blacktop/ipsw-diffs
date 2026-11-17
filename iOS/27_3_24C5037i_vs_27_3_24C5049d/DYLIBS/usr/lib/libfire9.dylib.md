## libfire9.dylib

> `/usr/lib/libfire9.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-36.0.1.0.0
-  __TEXT.__text: 0x2fb1f8
+36.0.2.0.0
+  __TEXT.__text: 0x2fb0fc
   __TEXT.__const: 0x555a8
   __TEXT.__cstring: 0x1bbc1
-  __TEXT.__oslogstring: 0x1947b
+  __TEXT.__oslogstring: 0x194c2
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xa960
   __DATA_CONST.__got: 0x0

   - /usr/lib/libc++.1.dylib
   Functions: 7611
   Symbols:   8827
-  CStrings:  5179
+  CStrings:  5180
 
Symbols:
+ __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_678505EPvs
+ __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_678505EPvs
+ __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_678505EPvs
+ __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_678505EPvs
+ __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_678505EPvs
+ __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_678505EPvs
+ ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_678505EPvs
- __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_677832EPvs
- __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_677832EPvs
- __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_677832EPvs
- __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_677832EPvs
- __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_677832EPvs
- __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_677832EPvs
- ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_677832EPvs
Functions:
~ __ZN7BlueFin8GlPosEng16SetSIGMeasuementEPNS_6GlMeasE : 3324 -> 3456
~ __ZN7BlueFin20GlMeSrdSvIdReportMgr18ReportMeasurementsEj : 5708 -> 5684
~ __ZN7BlueFin20GlMeSrdSvIdReportMgrC2ERNS_22GlMeDspMeasListenerIfcERNS_27GlMeSrdSatStatusListenerIfcEPKNS_20GlMeSrdAsicConfigIfcE : 420 -> 412
~ __ZN7BlueFin20GlMeSrdSvIdReportMgr10SetDSPMeasERKNS_11GlMeDSPMeasERKNS_17GlMeSrdDspMeasAuxEPKNS_23GlMeSrdMultiPeakResultsE : 4116 -> 3764
CStrings:
+ "@(#)Broadcom GLL ver. 172.20.28 678505, 2026/Oct/25, 16:45:51, build_job_id:__BUILDJOBID__, %s://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/...\n"
+ "ChipData_GRABSNQ_678505"
+ "FIRE@36.0.2 GLL@678505"
+ "GlPosEng::SetSIGMeasuement dropping stale 5Hz LMS:%u < LastAsicLms:%u\n"
- "@(#)Broadcom GLL ver. 172.20.28 677832, 2026/Oct/14, 21:26:52, build_job_id:__BUILDJOBID__, %s://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/...\n"
- "ChipData_GRABSNQ_677832"
- "FIRE@36.0.1 GLL@677832"
```
