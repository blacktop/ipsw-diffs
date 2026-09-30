## libfire7.dylib

> `/usr/lib/libfire7.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-135.0.4.0.0
-  __TEXT.__text: 0x2836f8
+135.0.5.0.0
+  __TEXT.__text: 0x284208
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x2cd1c
-  __TEXT.__cstring: 0x3ffaa
-  __TEXT.__gcc_except_tab: 0x54c8
+  __TEXT.__cstring: 0x3ffb7
+  __TEXT.__gcc_except_tab: 0x5514
   __TEXT.__unwind_info: 0x5718
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x84a0

   __DATA_DIRTY.__bss: 0x9c
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 7333
-  Symbols:   9839
-  CStrings:  6193
+  Functions: 7339
+  Symbols:   9848
+  CStrings:  6195
 
Symbols:
+ GCC_except_table53
+ GCC_except_table60
+ GCC_except_table63
+ __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_669847EPvs
+ __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_669847EPvs
+ __ZN7BlueFin11GlPeNavUtil25ComputeWeightedRangeResidERNS_13GlSignalIdSetERKNS_8LLA_TYPEEdibPfS6_bb
+ __ZN7BlueFin11GlPeNavUtil9ComputeBcERNS_13GlSignalIdSetERKNS_8LLA_TYPEEdibPfS6_b
+ __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_669847EPvs
+ __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_669847EPvs
+ __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_669847EPvs
+ __ZN7BlueFin19GlPeNavGnssResidMon23ComputePostfitResidualsERKNS_11GlPeNavUtilERKNS_13GlSignalIdSetEib
+ __ZN7BlueFin19GlPeNavGnssResidMon5ResetEv
+ __ZN7BlueFin21GlPeRqHdlrPosPeriodic17ApplyLocalUpdatesERNS_21GlPeExtendedFixStatusERKS1_
+ __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_669847EPvs
+ __ZNK7BlueFin11GlPeNavUtil18ComputeCphResidVecERNS_13GlSignalIdSetERKNS_8LLA_TYPEEdiRNS_12SKFVectorDimILi100EEEPS7_
+ __ZNK7BlueFin11GlPeNavUtil20ComputeRrateResidVecERNS_13GlSignalIdSetERKNS_8LLA_TYPEEdiRKNS_8NED_TYPEEd
+ __ZNK7BlueFin11GlPeNavUtil26computeRangeResidVecHelperERNS_13GlSignalIdSetERKNS_8LLA_TYPEEdiRKNS0_17stRangeResidParamERNS_12SKFVectorDimILi100EEEPSA_PfSD_
+ __ZNK7BlueFin11GlPeNavUtil26computeRrateResidVecHelperERNS_13GlSignalIdSetERKNS_8LLA_TYPEEdiRKNS_8NED_TYPEEdRNS_12SKFVectorDimILi100EEEPSA_
+ __ZNK7BlueFin11GlPeNavUtil28ComputeWeightedRrateResidVecERNS_13GlSignalIdSetERKNS_8LLA_TYPEEdiRKNS_8NED_TYPEEddb
+ __ZNK7BlueFin9GlSetBase4RankEs
+ ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_669847EPvs
+ ___func__._ZNK7BlueFin9GlSetBase4RankEs
- GCC_except_table64
- __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_653695EPvs
- __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_653695EPvs
- __ZN7BlueFin11GlPeNavUtil25ComputeWeightedRangeResidERNS_13GlSignalIdSetENS_8LLA_TYPEEdibPfS4_bb
- __ZN7BlueFin11GlPeNavUtil9ComputeBcERNS_13GlSignalIdSetENS_8LLA_TYPEEdibPfS4_b
- __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_653695EPvs
- __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_653695EPvs
- __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_653695EPvs
- __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_653695EPvs
- __ZNK7BlueFin11GlPeNavUtil20ComputeRangeResidVecERNS_13GlSignalIdSetENS_8LLA_TYPEEdibPfS4_bbddddb
- __ZNK7BlueFin11GlPeNavUtil20ComputeRrateResidVecERNS_13GlSignalIdSetENS_8LLA_TYPEEdiRKNS_8NED_TYPEEd
- __ZNK7BlueFin11GlPeNavUtil20ComputeRrateResidVecERNS_13GlSignalIdSetENS_8LLA_TYPEEdiRKNS_8NED_TYPEEddb
- ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_653695EPvs
CStrings:
+ "@(#)Broadcom GLL ver. 162.20.25 669847, 2026/Jul/01, 21:43:31, build_job_id:5189, %s://depot/client/core/rel/Olympic/OSX_20.24.559185.v8.0/...\n"
+ "ChipData_GRABSNQ_669847"
+ "FIRE@135.0.5 GLL@669847"
+ "Jul  9 2026, 00:49:51"
+ "Rank"
+ "SetMeasurements"
+ "computeRangeResidVecHelper"
+ "rotMeasData.otClock.sllFullBiasNs<=0"
+ "rotSignalIds.Cnt() <= GL_CHANNELS"
+ "ucWordNum < m_ucUlongSize"
- "@(#)Broadcom GLL ver. 162.20.25 653695, 2026/Jan/22, 20:35:22, build_job_id:3135, %s://depot/client/core/rel/Olympic/OSX_20.24.559185.v8.0/...\n"
- "Active Request: GL_REQ_GNSS_MEAS_DATA\n"
- "ChipData_GRABSNQ_653695"
- "ComputeRangeResidVec"
- "FIRE@135.0.4 GLL@653695"
- "Jun 23 2026, 02:00:11"
- "m_oMeasData.otClock.sllFullBiasNs<=0"
- "otThisSignals.Cnt() <= GL_CHANNELS"
```
