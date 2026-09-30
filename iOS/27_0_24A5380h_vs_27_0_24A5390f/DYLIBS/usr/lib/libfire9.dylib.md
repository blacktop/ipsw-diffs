## libfire9.dylib

> `/usr/lib/libfire9.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__DATA.__data`

```diff

-28.0.0.0.0
-  __TEXT.__text: 0x301c60
-  __TEXT.__const: 0x9f698
-  __TEXT.__cstring: 0x1bd8d
+30.0.0.0.0
+  __TEXT.__text: 0x301f94
+  __TEXT.__const: 0x9f6e8
+  __TEXT.__cstring: 0x1bd44
   __TEXT.__oslogstring: 0x1938e
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xaa00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 7594
-  Symbols:   8826
-  CStrings:  5184
+  Symbols:   8823
+  CStrings:  5180
 
Symbols:
+ __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_669867EPvs
+ __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_669867EPvs
+ __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_669867EPvs
+ __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_669867EPvs
+ __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_669867EPvs
+ __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_669867EPvs
+ ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_669867EPvs
- __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_668981EPvs
- __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_668981EPvs
- __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_668981EPvs
- __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_668981EPvs
- __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_668981EPvs
- __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_668981EPvs
- ___func__._ZN7BlueFin15GlEngineImplStd10SetAsstPosEPNS_15GL_ASS_POS_QUALEjb
- ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_668981EPvs
- ___func__._ZN7BlueFin24GlMeSrdAsicUnitConverter23PpuToEswAidingFrequencyEfRKNS_10GlSignalIdE
- ___func__._ZN7BlueFin24GlMeSrdAsicUnitConverter30PpuToEswAidingFrequencyMinnow5EfRKNS_10GlSignalIdE
Functions:
~ __ZN7BlueFin15GlEngineImplStd13CommonAPIcodeEv : 4932 -> 4936
~ __ZNK7BlueFin16GlPeGloEphemeris6GetPvtERKNS_12GlPeGnssTimeEdRNS_12SAT_PVT_TYPEE : 3032 -> 2972
~ __ZN7BlueFin11GlPeGridMgr6UpdateEbbbbbRKNS_21GlPeExtendedFixStatusE : 4296 -> 4264
~ __ZN7BlueFin12GlPeFirstFix11FirstFixMgrERKNS0_15stFirstFixInputERNS0_16stFirstFixReturnE : 17748 -> 17760
~ __ZN7BlueFin7GlReqSm15SetSignalAidingERKNS_9GlSvIdSetE : 16876 -> 16888
~ __ZN7BlueFin7GlReqSm18sendMeSignalAidingERKNS_17GlMeSignalAidInfoE : 3592 -> 3748
~ __ZN7BlueFin16GlMeSrdAidingMgr17GetAidIdAndAidingERKNS_10GlSignalIdERhRNS_17aiding_param_typeEPNS_10GlMeClkModEPb : 620 -> 664
~ __ZN7BlueFin16GlMeSrdAidingMgr18FormatAidingForEswEPNS_17aiding_param_typeERKNS_10GlMeAcqWinEbdRKNS_10GlSignalIdE : 2852 -> 2900
~ __ZN7BlueFin24GlMeSrdAsicUnitConverter23PpuToEswAidingFrequencyEfRKNS_10GlSignalIdE : 128 -> 96
~ __ZN7BlueFin16GlMeSrdAidingMgr25FormatGpsTcxoAidingForEswEPNS_17aiding_param_typeE : 328 -> 380
~ __ZN7BlueFin16GlMeSrdAidingMgr26FormatGlnsTcxoAidingForEswEPNS_17aiding_param_typeE : 336 -> 388
~ __ZN7BlueFin16GlMeSrdAidingMgr28FormatBdsPosTcxoAidingForEswEPNS_17aiding_param_typeE : 336 -> 388
~ __ZN7BlueFin10GlDineCtrlC2EPNS_11GlEventPumpEPNS_6GlPeIfEPFPvjEPFvS5_Ebj : 1704 -> 1700
~ __ZN7BlueFin10GlDineCtrlD2Ev : 416 -> 412
~ __ZN7BlueFin25GlMeSrdSatRptSearchMsmtMIC2ERKNS_22GlMeSrdSatRptRpcBufferERKNS_10GlSignalIdERKNS_25GlMeReceiverParametersIfcERKNS_20GlMeSrdAsicConfigIfcEj : 5104 -> 4988
~ __ZN7BlueFin24GlMeSrdAsicUnitConverter30PpuToEswAidingFrequencyMinnow5EfRKNS_10GlSignalIdE : 128 -> 96
~ __ZN7BlueFin20GlMeSrdPacketManagerC2ERNS_30GlMeSrdPacketManagerCallbackIfERKNS_20GlMeSrdAsicConfigIfcEPNS_11GlEventPumpE : 604 -> 608
~ __ZN7BlueFin10GlPeOscMgr6updateEsstjb : 1244 -> 1116
~ __ZN7BlueFin15GlEngineImplStd10SetAsstPosEPNS_15GL_ASS_POS_QUALEjb : 444 -> 352
~ __ZN7BlueFin8GlPeHula15PosLocationData6UpdateERKNS_13GlExtSensDataE : 1044 -> 1076
~ __ZN7BlueFin13GlPeNavGnssKF15ComputePositionERKNS_15GlPeNavGnssKFIf8SettingsERKNS_16GlPeNavGnssStateE : 10192 -> 11036
~ __ZN7BlueFin15GlPeTimeManager17SetDataSubFrmMeasEPKNS_16GlDataSubFrmMeasE : 4184 -> 4192
CStrings:
+ "@(#)Broadcom GLL ver. 172.20.28 669867, 2026/Jul/01, 22:23:04, build_job_id:__BUILDJOBID__, %s://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/...\n"
+ "ChipData_GRABSNQ_669867"
+ "FIRE@30 GLL@669867"
+ "Jul 10 2026, 01:09:00"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_A8@$Change: 669866 $"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_B0@$Change: 669866 $"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_FE@$Change: 669866 $"
- "@(#)Broadcom GLL ver. 172.20.28 668981, 2026/Jun/22, 17:45:22, build_job_id:__BUILDJOBID__, %s://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/...\n"
- "ChipData_GRABSNQ_668981"
- "FIRE@28 GLL@668981"
- "GetPvt"
- "Jun 26 2026, 22:15:22"
- "PpuToEswAidingFrequency"
- "PpuToEswAidingFrequencyMinnow5"
- "SetAsstPos"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_A8@$Change: 668937 $"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_B0@$Change: 668937 $"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_FE@$Change: 668937 $"
```
