## BatteryAlgorithms

> `/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`

```diff

-90.0.0.0.0
-  __TEXT.__text: 0x2d590
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x7b4
-  __TEXT.__const: 0x3040
-  __TEXT.__gcc_except_tab: 0x3558
+93.0.0.0.0
+  __TEXT.__text: 0x2fb78
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x7cc
+  __TEXT.__const: 0x3560
+  __TEXT.__gcc_except_tab: 0x39a4
   __TEXT.__oslogstring: 0xa7
-  __TEXT.__cstring: 0x2278
-  __TEXT.__unwind_info: 0xc80
+  __TEXT.__cstring: 0x2298
+  __TEXT.__unwind_info: 0xd20
   __TEXT.__objc_classname: 0x65
-  __TEXT.__objc_methname: 0xfc7
-  __TEXT.__objc_methtype: 0xe3c
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0x138
+  __TEXT.__objc_methname: 0x1064
+  __TEXT.__objc_methtype: 0xfaa
+  __TEXT.__objc_stubs: 0xa40
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x410
+  __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x5d8
-  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x90
-  __AUTH_CONST.__cfstring: 0x2a20
-  __AUTH_CONST.__objc_const: 0x1188
+  __AUTH_CONST.__cfstring: 0x2b20
+  __AUTH_CONST.__objc_const: 0x11b8
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x4ff8
   __AUTH_CONST.__objc_arrayobj: 0x468
   __AUTH_CONST.__objc_doubleobj: 0x1a0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xe4
+  __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x3cd008
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 42758846-DCA6-34F7-A3E9-486B87271095
-  Functions: 592
-  Symbols:   1898
-  CStrings:  957
+  UUID: 6269045B-71C4-3210-9C7C-B2C791526BEE
+  Functions: 609
+  Symbols:   1959
+  CStrings:  977
 
Symbols:
+ -[AdaptiveOCV mlOcvModelCache]
+ -[AdaptiveOCV setMlOcvModelCache:]
+ GCC_except_table18
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table42
+ _OBJC_IVAR_$_AdaptiveOCV._mlOcvModelCache
+ __ZN15AdaptiveOcvAlgo10CoreEngine12getCapturedVEPA500_dRNSt3__16vectorIdNS3_9allocatorIdEEEE
+ __ZN15AdaptiveOcvAlgo10CoreEngine12getTelemetryENS_5StateENS_16CCSOCLinearModelENS_18CoverageScoreParamENS_12CCdriftModelEddPdRNSt3__16vectorIdNS6_9allocatorIdEEEESB_SB_SB_SB_RiSC_
+ __ZN15AdaptiveOcvAlgo10CoreEngine13getDriftStateERNS_12CCdriftModelE
+ __ZN15AdaptiveOcvAlgo10CoreEngine13setDriftStateENS_12CCdriftModelE
+ __ZN15AdaptiveOcvAlgo10CoreEngine14getSelectedOCVENS_16CCSOCLinearModelEddPdRNS_16ConfigurationOCVE
+ __ZN15AdaptiveOcvAlgo10CoreEngine16prepData4SympOCVEPKimii
+ __ZN15AdaptiveOcvAlgo10CoreEngine4initERKNS_16ConfigurationOCVES3_RKNS_10MLOCVModelE
+ __ZN15AdaptiveOcvAlgo10CoreEngine8getStateERNS_5StateE
+ __ZN15AdaptiveOcvAlgo10CoreEngine8setStateENS_5StateE
+ __ZN15AdaptiveOcvAlgo12CCdriftModelC2Ev
+ __ZN15AdaptiveOcvAlgo15Deserialization22setMlOcvFromDictionaryEPK12NSDictionaryRNS_18ConfigurationMLOCVE
+ __ZN15AdaptiveOcvAlgo15fitCCdriftModelEPKiS1_S1_S1_S1_mRNS_5StateERNS_12CCdriftModelE
+ __ZN15AdaptiveOcvAlgo16createSOCCCtableERKNS_5StateERKNSt3__16vectorIdNS3_9allocatorIdEEEERKNS_16ConfigurationOCVERKNS_16CCSOCLinearModelERNS_10CCSOCTableE
+ __ZN15AdaptiveOcvAlgo16selectUsefulDataEPKiS1_S1_S1_S1_S1_S1_mRKNSt3__16vectorIdNS2_9allocatorIdEEEENS_13ConfigurationERNS_5StateERNS_16CCSOCLinearModelE
+ __ZN15AdaptiveOcvAlgo18CoverageScoreParam22calculateCoverageScoreENS_5StateERKNS_16CCSOCLinearModelENS_13ConfigurationE
+ __ZN15AdaptiveOcvAlgo18CoverageScoreParam25calculateCoverageScoreDayENS_5StateERKNS_16CCSOCLinearModelENS_13ConfigurationE
+ __ZN15AdaptiveOcvAlgo18CoverageScoreParam25calculateCoverageScoreSOCENS_5StateERKNS_16CCSOCLinearModelENS_13ConfigurationE
+ __ZN15AdaptiveOcvAlgo18CoverageScoreParam26calculateCoverageScoreTempENS_5StateERKNS_16CCSOCLinearModelENS_13ConfigurationE
+ __ZN15AdaptiveOcvAlgo18CoverageScoreParam28calculateCoverageScoreNumberENS_5StateERKNS_16CCSOCLinearModelENS_13ConfigurationE
+ __ZN15AdaptiveOcvAlgo22fitSOCCCModelByOCVpoolERKNS_5StateERKNSt3__16vectorIdNS3_9allocatorIdEEEERKNS_16CCSOCLinearModelERdSD_Pd
+ __ZN25AugmentedBatteryHealthLib11SOCOCVParamD2Ev
+ __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_13ACAMDailyDataELi0EEENSt3__15tupleIJT_iEEERKNS2_6vectorIS4_NS2_9allocatorIS4_EEEEd
+ __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_14ACAMWeeklyDataELi0EEENSt3__15tupleIJT_iEEERKNS2_6vectorIS4_NS2_9allocatorIS4_EEEEd
+ __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_14ACAMWeeklyDataELi2EEENSt3__15tupleIJT_iEEERKNS2_6vectorIS4_NS2_9allocatorIS4_EEEEd
+ __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_9BDCWeeklyELi0EEENSt3__15tupleIJT_iEEERKNS2_6vectorIS4_NS2_9allocatorIS4_EEEEd
+ __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_9BDCWeeklyELi2EEENSt3__15tupleIJT_iEEERKNS2_6vectorIS4_NS2_9allocatorIS4_EEEEd
+ __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_9DailyDataELi0EEENSt3__15tupleIJT_iEEERKNS2_6vectorIS4_NS2_9allocatorIS4_EEEEd
+ __ZN25AugmentedBatteryHealthLib13findTimeStampINS_9DailyDataEEEdiNSt3__16vectorIT_NS2_9allocatorIS4_EEEE
+ __ZN25AugmentedBatteryHealthLib20initParametersV59ATLEv
+ __ZN25AugmentedBatteryHealthLib20initParametersV59LGCEv
+ __ZN25AugmentedBatteryHealthLib8RdcParamD2Ev
+ __ZN25AugmentedBatteryHealthLib9ABHWeeklyD2Ev
+ __ZN25AugmentedBatteryHealthLib9QmaxParamD2Ev
+ __ZN25AugmentedBatteryHealthLibL6NORMALE
+ __ZN25AugmentedBatteryHealthLibL7FAULTEDE
+ __ZN6BACore19CommonSerialization21assignNSArrayToCArrayIdLm5ELm500EEEvP7NSArrayRAT0__AT1__T_
+ __ZN6BACore19CommonSerialization21assignNSArrayToCArrayIdLm91EEEvP7NSArrayRAT0__T_
+ __ZN6BACore19CommonSerialization21assignNSArrayToCArrayIiLm100EEEvP7NSArrayRAT0__T_
+ __ZN6BACore19CommonSerialization21assignNSArrayToCArrayIiLm15EEEvP7NSArrayRAT0__T_
+ __ZN6BACore19CommonSerialization21assignNSArrayToCArrayIiLm50EEEvP7NSArrayRAT0__T_
+ __ZN6BACore19CommonSerialization22convertCArrayToNSArrayIKdLm5ELm500EEEP7NSArrayRAT0__AT1__T_
+ __ZN6BACore19CommonSerialization22convertCArrayToNSArrayIKiLm100EEEP7NSArrayIP8NSNumberERAT0__T_
+ __ZN6BACore19CommonSerialization22convertCArrayToNSArrayIKiLm15EEEP7NSArrayIP8NSNumberERAT0__T_
+ __ZN6BACore19CommonSerialization22convertCArrayToNSArrayIKiLm50EEEP7NSArrayIP8NSNumberERAT0__T_
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1EEEEJN25AugmentedBatteryHealthLib14ACAMWeeklyDataEiEEC1B8ne200100IJLm0ELm1EEJS4_iEJEJEJRKS4_RKiEEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSC_IJDpT2_EEEDpOT3_
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1EEEEJN25AugmentedBatteryHealthLib9BDCWeeklyEiEEC1B8ne200100IJLm0ELm1EEJS4_iEJEJEJRKS4_RKiEEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSC_IJDpT2_EEEDpOT3_
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4EEEEJN25AugmentedBatteryHealthLib9QmaxParamENS3_8RdcParamENS3_8NccParamENS3_11SOCOCVParamENS3_9ABHWeeklyEEEC2B8ne200100IJLm0ELm1ELm2ELm3ELm4EEJS4_S5_S6_S7_S8_EJEJEJRS4_RS5_RS6_RS7_RS8_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSH_IJDpT2_EEEDpOT3_
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4EEEEJN25AugmentedBatteryHealthLib9QmaxParamENS3_8RdcParamENS3_8NccParamENS3_11SOCOCVParamENS3_9ABHWeeklyEEED2Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE18__assign_with_sizeB8ne200100IPKdS6_EEvT_T0_l
+ _memset_pattern16
+ _objc_msgSend$lastObject
- GCC_except_table38
- GCC_except_table39
- GCC_except_table44
- GCC_except_table50
- __ZN15AdaptiveOcvAlgo10CCSOCTable5resetEv
- __ZN15AdaptiveOcvAlgo10CoreEngine12getCapturedVEPA101_dRNSt3__16vectorIdNS3_9allocatorIdEEEE
- __ZN15AdaptiveOcvAlgo10CoreEngine16prepData4SympOCVEPKim
- __ZN15AdaptiveOcvAlgo10CoreEngine4initERKNS_16ConfigurationOCVES3_RKNS_10MLOCVModelENS_5StateE
- __ZN15AdaptiveOcvAlgo10CoreEngine9getOutputENS_5StateENS_16CCSOCLinearModelENS_18CoverageScoreParamENS_12CCdriftModelEddPdRS1_RNS_16ConfigurationOCVERNSt3__16vectorIdNS9_9allocatorIdEEEESE_SE_SE_SE_RiSF_
- __ZN15AdaptiveOcvAlgo10MLOCVModel10learnMLOCVEv
- __ZN15AdaptiveOcvAlgo15fitCCdriftModelEPKiS1_S1_S1_PKfmRNS_5StateERNS_12CCdriftModelE
- __ZN15AdaptiveOcvAlgo16CCSOCLinearModel12getTableDataERKNS_5StateEPiPA101_dRS1_
- __ZN15AdaptiveOcvAlgo16CCSOCLinearModel13pushTableDataEPKd
- __ZN15AdaptiveOcvAlgo16CCSOCLinearModel5printEv
- __ZN15AdaptiveOcvAlgo16createSOCCCtableERKNSt3__16vectorINS1_IdNS0_9allocatorIdEEEENS2_IS4_EEEERKNS_16ConfigurationOCVERKNS_16CCSOCLinearModelERNS_10CCSOCTableE
- __ZN15AdaptiveOcvAlgo16selectUsefulDataEPKiS1_S1_S1_S1_S1_PKfmRKNSt3__16vectorINS5_IdNS4_9allocatorIdEEEENS6_IS8_EEEENS_13ConfigurationERNS_5StateERNS_16CCSOCLinearModelE
- __ZN15AdaptiveOcvAlgo18CoverageScoreParam22calculateCoverageScoreERKNS_16CCSOCLinearModelENS_13ConfigurationE
- __ZN15AdaptiveOcvAlgo18CoverageScoreParam25calculateCoverageScoreDayERKNS_16CCSOCLinearModelENS_13ConfigurationE
- __ZN15AdaptiveOcvAlgo18CoverageScoreParam25calculateCoverageScoreSOCERKNS_16CCSOCLinearModelENS_13ConfigurationE
- __ZN15AdaptiveOcvAlgo18CoverageScoreParam26calculateCoverageScoreTempERKNS_16CCSOCLinearModelENS_13ConfigurationE
- __ZN15AdaptiveOcvAlgo18CoverageScoreParam28calculateCoverageScoreNumberERKNS_16CCSOCLinearModelENS_13ConfigurationE
- __ZN15AdaptiveOcvAlgo21createSOCCCsmallTableERKNSt3__16vectorINS1_IdNS0_9allocatorIdEEEENS2_IS4_EEEERKNS_16ConfigurationOCVERKNS_16CCSOCLinearModelERNS_10CCSOCTableE
- __ZN15AdaptiveOcvAlgo22calculateCCSOCRsquaredEv
- __ZN15AdaptiveOcvAlgo22fitSOCCCModelByOCVpoolERKNSt3__16vectorINS1_IdNS0_9allocatorIdEEEENS2_IS4_EEEERKNS_16CCSOCLinearModelERdSC_Pd
- __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_13ACAMDailyDataELi0EEET_RKNSt3__16vectorIS2_NS3_9allocatorIS2_EEEEd
- __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_14ACAMWeeklyDataELi0EEET_RKNSt3__16vectorIS2_NS3_9allocatorIS2_EEEEd
- __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_9BDCWeeklyELi0EEET_RKNSt3__16vectorIS2_NS3_9allocatorIS2_EEEEd
- __ZN25AugmentedBatteryHealthLib12searchbyTimeINS_9DailyDataELi0EEET_RKNSt3__16vectorIS2_NS3_9allocatorIS2_EEEEd
- __ZNKSt3__111__copy_implclB8ne200100IPNS_6vectorIdNS_9allocatorIdEEEES6_S6_EENS_4pairIT_T1_EES8_T0_S9_
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l
CStrings:
+ "ChargeAccum_last"
+ "OCVcurvehysteresis_now"
+ "T{MLOCVModel=[1{ConfigurationMLOCV=[91d]}]},N,V_mlOcvModelCache"
+ "T{PersistentState={State=[100i][50i][15i][100i][5[500d]]dddid[6d][3d]iiii}{ConfigurationOCV=[103d][103d][103d][103d][103d]dB}},N,V_persistentStateCache"
+ "Vprev_mV"
+ "_mlOcvModelCache"
+ "lastObject"
+ "mlOcvModelCache"
+ "setMlOcvModelCache:"
+ "streamPaginate"
+ "table_data"
+ "table_dist"
+ "table_dist_day"
+ "table_dist_temp"
+ "table_pntr"
+ "v25344@0:8{PersistentState={State=[100i][50i][15i][100i][5[500d]]dddid[6d][3d]iiii}{ConfigurationOCV=[103d][103d][103d][103d][103d]dB}}16"
+ "v744@0:8{MLOCVModel=[1{ConfigurationMLOCV=[91d]}]}16"
+ "{MLOCVModel=\"configPool\"[1{ConfigurationMLOCV=\"OCV\"[91d]}]}"
+ "{MLOCVModel=[1{ConfigurationMLOCV=[91d]}]}16@0:8"
+ "{PersistentState=\"state\"{State=\"table_dist\"[100i]\"table_dist_temp\"[50i]\"table_dist_day\"[15i]\"table_pntr\"[100i]\"table_data\"[5[500d]]\"f_mid_h\"d\"OCVcurvehysteresis_now\"d\"Vprev_mV\"d\"data_number\"i\"i3\"d\"CtC3x3\"[6d]\"Cy3x1\"[3d]\"t_last\"i\"ChargeAccum_last\"i\"Thp_last\"i\"idx_selected_OCV\"i}\"config_selected\"{ConfigurationOCV=\"OCV\"[103d]\"OCV_temp_co\"[103d]\"ChgOCV\"[103d]\"ChgOCV_temp_co\"[103d]\"SOC\"[103d]\"RefTemp\"d\"ready\"B}}"
+ "{PersistentState={State=[100i][50i][15i][100i][5[500d]]dddid[6d][3d]iiii}{ConfigurationOCV=[103d][103d][103d][103d][103d]dB}}16@0:8"
- "Qmax[mAh]:%f\n"
- "Qoff[mAh]:%f\n"
- "T{PersistentState={State=[500d]dd[6d][3d]ddi}{ConfigurationOCV=[103d][103d][103d][103d][103d]dB}},N,V_persistentStateCache"
- "kt[mAh_per_month]:%f\n"
- "soc:%d number:%d pointer:%d\n"
- "table_short_data"
- "v8264@0:8{PersistentState={State=[500d]dd[6d][3d]ddi}{ConfigurationOCV=[103d][103d][103d][103d][103d]dB}}16"
- "{PersistentState=\"state\"{State=\"table_short_data\"[500d]\"f_mid_h\"d\"i3\"d\"CtC3x3\"[6d]\"Cy3x1\"[3d]\"t_last\"d\"Thp_last\"d\"idx_selected_OCV\"i}\"config_selected\"{ConfigurationOCV=\"OCV\"[103d]\"OCV_temp_co\"[103d]\"ChgOCV\"[103d]\"ChgOCV_temp_co\"[103d]\"SOC\"[103d]\"RefTemp\"d\"ready\"B}}"
- "{PersistentState={State=[500d]dd[6d][3d]ddi}{ConfigurationOCV=[103d][103d][103d][103d][103d]dB}}16@0:8"

```
