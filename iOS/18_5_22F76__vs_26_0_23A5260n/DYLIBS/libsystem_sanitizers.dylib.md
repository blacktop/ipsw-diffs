## libsystem_sanitizers.dylib

> `/usr/lib/system/libsystem_sanitizers.dylib`

```diff

-19.0.0.0.0
-  __TEXT.__text: 0x4158
+23.0.0.0.0
+  __TEXT.__text: 0x4984
   __TEXT.__auth_stubs: 0x190
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0xa36
+  __TEXT.__cstring: 0xa87
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x90
   __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0xb8
-  __DATA.__bss: 0x530
+  __DATA.__bss: 0x540
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x30
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 4F1DF60E-4E36-3139-BDBD-929A7647EB36
-  Functions: 186
-  Symbols:   388
-  CStrings:  130
+  UUID: 6E66DDB3-442B-3097-9C7F-5BEED2486725
+  Functions: 197
+  Symbols:   408
+  CStrings:  133
 
Symbols:
+ __ZL9collector
+ __ZN5trace19initTraceCollectionERKN6config6TracesE
+ __ZN5trace19initTraceCollectionERKN6config6TracesE.cold.1
+ __ZN5trace19initTraceCollectionERKN6config6TracesE.cold.2
+ __ZN5trace19initTraceCollectionERKN6config6TracesE.cold.3
+ __ZN5trace19initTraceCollectionERKN6config6TracesE.cold.4
+ __ZN5trace19initTraceCollectionERKN6config6TracesE.cold.5
+ __ZN6config3env6Parser11getTrialValILm18EEEPKcS4_RAT__S3_RA128_c
+ __ZN6config3env6Parser11getTrialValILm19EEEPKcS4_RAT__S3_RA128_c
+ __ZN6config3env6Parser11getTrialValILm27EEEPKcS4_RAT__S3_RA128_c
+ __ZN6config3env6Parser11getTrialValILm30EEEPKcS4_RAT__S3_RA128_c
+ __ZN6config3env6Parser11getTrialValILm34EEEPKcS4_RAT__S3_RA128_c
+ __ZNK5trace9CollectorINS_5DepotILm524288ELm64ELm8EN4hash7Murmur2EXadL_Z16thread_stack_pcsEEEENS_13AllocationMapILm1048576EXadL_ZNS3_11hashPointerEmEEEEXadL_Z11malloc_sizeEEE10shouldSkipINS7_8LazySizeEEEbmRT_
+ __ZNK6config3env6Parser10getSettingILm18ENS0_7AddressELm2EEET0_RAT__KcS4_RAT1__KNS1_7SettingIS4_EE
+ __ZNK6config3env6Parser10getSettingILm27ENS0_16AllocationTracesELm4EEET0_RAT__KcS4_RAT1__KNS1_7SettingIS4_EE
+ __ZNK6config3env6Parser10getSettingILm30EbLm3EEET0_RAT__KcS3_RAT1__KNS1_7SettingIS3_EE
+ __ZNK6config3env6Parser10getSettingILm34EbLm3EEET0_RAT__KcS3_RAT1__KNS1_7SettingIS3_EE
+ __ZNK6config3env6Parser6getValILm18EEEPKcRAT__S3_
+ __ZNK6config3env6Parser6getValILm19EEEPKcRAT__S3_
+ __ZNK6config3env6Parser6getValILm27EEEPKcRAT__S3_
+ __ZNK6config3env6Parser6getValILm30EEEPKcRAT__S3_
+ __ZNK6config3env6Parser6getValILm34EEEPKcRAT__S3_
+ __ZNK6config3env6Parser9getNumberILm19ElXadL_Z6strtolEEEET0_RAT__KcS3_
+ __ZNK6config3env6Parser9getNumberILm34EmXadL_Z7strtoulEEEET0_RAT__KcS3_
- __ZL9collector.0
- __ZL9collector.1
- __ZL9collector.2
- __ZN2vm6createIN5trace13AllocationMapILm1048576EXadL_ZN4hash7Murmur211hashPointerEmEEEEJEEEPT_DpOT0_
- __ZN2vm6createIN5trace13AllocationMapILm1048576EXadL_ZN4hash7Murmur211hashPointerEmEEEEJEEEPT_DpOT0_.cold.1
- __ZN2vm6createIN5trace13AllocationMapILm1048576EXadL_ZN4hash7Murmur211hashPointerEmEEEEJEEEPT_DpOT0_.cold.2
- __ZN2vm6createIN5trace5DepotILm524288ELm64ELm8EN4hash7Murmur2EXadL_Z16thread_stack_pcsEEEEJEEEPT_DpOT0_
- __ZN2vm6createIN5trace5DepotILm524288ELm64ELm8EN4hash7Murmur2EXadL_Z16thread_stack_pcsEEEEJEEEPT_DpOT0_.cold.1
- __ZN2vm6createIN5trace5DepotILm524288ELm64ELm8EN4hash7Murmur2EXadL_Z16thread_stack_pcsEEEEJEEEPT_DpOT0_.cold.2
- __ZN5trace19initTraceCollectionEb
- __ZN5trace19initTraceCollectionEb.cold.1
- __ZNK6config3env6Parser10getSettingINS0_16AllocationTracesELm4EEET_PKcS4_RAT0__KNS1_7SettingIS4_EE
- __ZNK6config3env6Parser10getSettingINS0_7AddressELm2EEET_PKcS4_RAT0__KNS1_7SettingIS4_EE
- __ZNK6config3env6Parser10getSettingIbLm3EEET_PKcS3_RAT0__KNS1_7SettingIS3_EE
- __ZNK6config3env6Parser9getNumberIlXadL_Z6strtolEEEET_PKcS3_
CStrings:
+ "SanitizersAllocationTracesMaxSize"
+ "SanitizersAllocationTracesMinSize"
+ "__TRIFactors"

```
