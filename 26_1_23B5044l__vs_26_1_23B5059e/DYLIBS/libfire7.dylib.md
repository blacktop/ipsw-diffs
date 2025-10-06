## libfire7.dylib

> `/usr/lib/libfire7.dylib`

```diff

-123.0.0.0.0
-  __TEXT.__text: 0x292698
+125.0.3.0.0
+  __TEXT.__text: 0x2931e4
   __TEXT.__auth_stubs: 0x540
   __TEXT.__init_offsets: 0x10
-  __TEXT.__const: 0x2cf9c
-  __TEXT.__cstring: 0x3ab1a
-  __TEXT.__gcc_except_tab: 0x5604
-  __TEXT.__unwind_info: 0x5718
+  __TEXT.__const: 0x2cfbc
+  __TEXT.__cstring: 0x3ab24
+  __TEXT.__gcc_except_tab: 0x5608
+  __TEXT.__unwind_info: 0x5720
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x8480
   __AUTH_CONST.__auth_got: 0x2a8

   __DATA_DIRTY.__bss: 0x9c
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 8A3943B6-F99C-3C8D-B02E-4014EDA3050E
-  Functions: 7325
-  Symbols:   18797
+  UUID: 8A4289DC-A40A-3115-8F8F-DC4FB3B88363
+  Functions: 7326
+  Symbols:   18799
   CStrings:  6194
 
Symbols:
+ __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_643487EPvs
+ __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_643487EPvs
+ __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_643487EPvs
+ __ZN7BlueFin13GlPeSubsetsKfC1Ev
+ __ZN7BlueFin14GlPeComputeZRH13CalcIonoDelayEdffRKNS_8LLA_TYPEERKNS_3XYZEbRNS_15GlPeAtmosDelaysE
+ __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_643487EPvs
+ __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_643487EPvs
+ __ZN7BlueFin8GlPeCand6SubmitERKNS_8stSubsetEb
+ __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_643487EPvs
+ ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_643487EPvs
- __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_636491EPvs
- __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_636491EPvs
- __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_636491EPvs
- __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_636491EPvs
- __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_636491EPvs
- __ZN7BlueFin8stSubsetaSERKS0_
- __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_636491EPvs
- __ZNK7BlueFin14GlPeComputeZRH13CalcIonoDelayEdffRKNS_8LLA_TYPEERKNS_3XYZEbRNS_15GlPeAtmosDelaysE
- ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_636491EPvs
Functions:
~ __ZN7BlueFin6GlPeKF7SetMsmtEb : 44456 -> 44460
~ __ZN7BlueFin12GlPeFirstFix11FirstFixMgrERKNS0_15stFirstFixInputERNS0_16stFirstFixReturnE : 16712 -> 17040
~ __ZNK7BlueFin14GlPeComputeZRH13GetAtmosDelayERKNS_10GlSignalIdEjRKNS_8LLA_TYPEERKNS_3XYZEffbbRNS_11GlPeIonoSrcE : 616 -> 868
- __ZNK7BlueFin14GlPeComputeZRH13CalcIonoDelayEdffRKNS_8LLA_TYPEERKNS_3XYZEbRNS_15GlPeAtmosDelaysE
~ __ZN7BlueFin13GlPeNavGnssKF19ComputePositionMainERKNS_15GlPeNavGnssKFIf8SettingsEbRKNS_16GlPeNavGnssStateEPNS_9stSKFMeasE : 23068 -> 23104
~ __ZN7BlueFin14GlPeLsqSubsets12RunLsqSubsetERKNS_13GlSignalIdSetEhbPNS_25stFirstFixIntegerAnalysisEb : 1060 -> 1164
~ __ZN7BlueFin7GlPeLsq11LsPosFinishERKNS0_10stLsPosInpERNS_13GlSignalIdSetERaPNS_9stSKFMeasEiRNS_12stLsPosStateERNS_8LLA_TYPEERNS_9SKFVectorERb : 936 -> 980
- __ZN7BlueFin8stSubsetaSERKS0_
~ __ZN7BlueFin13GlPeNavGnssKF15AddProcessNoiseEaaRKNS_16GlPeNavGnssStateEjbbbb : 2584 -> 2864
~ __ZN7BlueFin13GlPeNavGnssKF6UpdateEPNS_9stSKFMeasERKNS_15GlPeNavGnssKFIf8SettingsE : 15144 -> 15712
+ __ZN7BlueFin14GlPeComputeZRH13CalcIonoDelayEdffRKNS_8LLA_TYPEERKNS_3XYZEbRNS_15GlPeAtmosDelaysE
+ __ZN7BlueFin8GlPeCand6SubmitERKNS_8stSubsetEb
~ __ZN7BlueFin12GlPeFirstFix10ClassicFixERKNS_13GlSignalIdSetERNS_11GlPeSubsetsEh : 1128 -> 1308
~ __ZN7BlueFin12GlPeFirstFix24RunPreIsolationFixRangesERKNS_13GlSignalIdSetERNS_11GlPeSubsetsERKNS_8stSvAzElERNS_14GlPeLsqSubsetsE : 488 -> 588
~ __ZN7BlueFin12GlPeFirstFix12IsolationFixERKNS_13GlSignalIdSetERNS_11GlPeSubsetsE : 4156 -> 4604
~ __ZNK7BlueFin11GlPeSubsets20ComputeScatterWidthKEhRNS_8stSubsetE : 832 -> 1084
~ __ZNK7BlueFin11GlPeSubsets22ComputeWeightedMeanPosERKNS_13GlSignalIdSetE : 628 -> 632
+ __ZN7BlueFin13GlPeSubsetsKfC1Ev
~ __ZN7BlueFin14GlPeMeasStatus24ComputeReferencePositionEv : 1396 -> 1400
CStrings:
+ "@(#)Broadcom GLL ver. 162.20.25 643487, 2025/Sep/18, 11:13:58, build_job_id:2748, %s://depot/client/core/rel/Olympic/OSX_20.24.559185.v8.0/...\n"
+ "CalcLowCostIonoDelay"
+ "ChipData_GRABSNQ_643487"
+ "FIRE@125.0.3 GLL@643487"
+ "Sep 26 2025, 02:29:38"
- "@(#)Broadcom GLL ver. 162.20.25 636491, 2025/June/20, 12:15:57, build_job_id:2522, %s://depot/client/core/rel/Olympic/OSX_20.24.559185.v8.0/...\n"
- "CalcIonoDelay"
- "ChipData_GRABSNQ_636491"
- "FIRE@123 GLL@636491"
- "Sep  5 2025, 06:36:15"

```
