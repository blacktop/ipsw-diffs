## com.apple.driver.EXDisplayPipeH18P

> `com.apple.driver.EXDisplayPipeH18P`

```diff

-7.7.22.0.0
+7.8.7.0.0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x21f2
-  __TEXT_EXEC.__text: 0x8b1c
+  __TEXT.__cstring: 0x2465
+  __TEXT_EXEC.__text: 0xa1a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf30
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 120911E3-9CB4-3492-A022-5C96A676C7E3
+  UUID: 9FEBECCD-72EC-3E8C-9DFD-A699027DE1C4
   Functions: 160
   Symbols:   0
-  CStrings:  178
+  CStrings:  210
 
Functions:
~ sub_fffffe000a065dd0 -> sub_fffffe000a12d740 : 5356 -> 10600
~ sub_fffffe000a068914 -> sub_fffffe000a131700 : 112 -> 300
~ sub_fffffe000a068984 -> sub_fffffe000a13182c : 312 -> 332
~ sub_fffffe000a068fbc -> sub_fffffe000a131e78 : 64 -> 20
~ sub_fffffe000a069004 -> sub_fffffe000a131e94 : 60 -> 24
~ sub_fffffe000a069c04 -> sub_fffffe000a132a70 : 236 -> 620
~ sub_fffffe000a06a5b0 -> sub_fffffe000a13359c : 424 -> 436
CStrings:
+ "EXDisplayPipe: error: args->structureOutputSize (0x%x) != sizeof(EXDisplayPipeHealthStats) (0x%lx)\n"
+ "average_crc_variance"
+ "average_sca_variance"
+ "brightness_cp"
+ "brightness_failure_time"
+ "crc_failures_beyond_thresh"
+ "dcptransporthealth_cp"
+ "dcptransporthealth_failure_time"
+ "globalhealth_cp"
+ "globalhealth_failure_time"
+ "hwlinkfailures_cp"
+ "hwlinkfailures_failure_time"
+ "link_cp"
+ "link_failure_time"
+ "nonauthenticpanel_cp"
+ "nonauthenticpanel_failure_time"
+ "pipe_cp"
+ "pipe_failure_time"
+ "sca_failures_beyond_thresh"
+ "scaalgorithm_cp"
+ "scaalgorithm_failure_time"
+ "scadriver_cp"
+ "scadriver_failure_time"
+ "scldriver_cp"
+ "scldriver_failure_time"
+ "silhealth_cp"
+ "silhealth_failure_time"
+ "tconcrc_cp"
+ "tconcrc_failure_time"
+ "tconhealth_cp"
+ "tconhealth_failure_time"
+ "tconhpd_cp"
+ "tconhpd_failure_time"
+ "v384@?0{exdisplaypipetightbeamcommon_exdisplaypipetelemetrycounters_s=QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ}8"
- "EXDisplayPipe: error: args->structureOutputSize (0x%x) != sizeof(exdisplaypipetightbeamcommon_exdisplaypipetelemetrycounters_s) (0x%lx)\n"
- "v128@?0{exdisplaypipetightbeamcommon_exdisplaypipetelemetrycounters_s=QQQQQQQQQQQQQQQ}8"

```
