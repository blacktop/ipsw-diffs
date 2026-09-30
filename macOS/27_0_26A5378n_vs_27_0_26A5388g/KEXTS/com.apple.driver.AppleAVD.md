## com.apple.driver.AppleAVD

> `com.apple.driver.AppleAVD`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-989.1.0.0.0
-  __TEXT.__os_log: 0x18272
-  __TEXT.__cstring: 0x6721
+991.0.0.0.0
+  __TEXT.__os_log: 0x18350
+  __TEXT.__cstring: 0x6741
   __TEXT.__const: 0x9df99
-  __TEXT_EXEC.__text: 0x538a8
-  __TEXT_EXEC.__auth_stubs: 0x720
+  __TEXT_EXEC.__text: 0x538f0
+  __TEXT_EXEC.__auth_stubs: 0x710
   __DATA.__data: 0x1334
   __DATA.__common: 0x78
   __DATA.__bss: 0x14

   __DATA_CONST.__const: 0x3f38
   __DATA_CONST.__kalloc_type: 0x2b40
   __DATA_CONST.__kalloc_var: 0xbe0
-  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x10
-  Functions: 1721
+  Functions: 1720
   Symbols:   3906
-  CStrings:  1727
+  CStrings:  1728
 
Symbols:
+ __ZZN18AppleAVDUserClient14allocateMemoryEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutE21kalloc_type_view_3702
+ __ZZN18AppleAVDUserClient14allocateMemoryEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutE21kalloc_type_view_3724
+ __ZZN18AppleAVDUserClient16deallocateMemoryEP28_sAppleAVDDeallocateMemoryInP29_sAppleAVDDeallocateMemoryOutE21kalloc_type_view_3791
+ __ZZN18AppleAVDUserClient30getBoundaryCompliantAllocationEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutbE21kalloc_type_view_3839
+ __ZZN18AppleAVDUserClient30getBoundaryCompliantAllocationEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutbE21kalloc_type_view_3850
+ __ZZN18AppleAVDUserClient30getBoundaryCompliantAllocationEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutbE21kalloc_type_view_3887
+ __ZZN18AppleAVDUserClient32DeallocateUserClientKernelMemoryEvE21kalloc_type_view_4261
+ __ZZN8AppleAVD5startEP9IOServiceE11_os_log_fmt__73_
+ __ZZN8AppleAVD5startEP9IOServiceE11_os_log_fmt__74_
+ __ZZN8AppleAVD5startEP9IOServiceE11_os_log_fmt__75_
- __ZN17AppleAVDAnalytics18setEventEntryFloatEP12OSDictionaryPKcf
- __ZN8OSNumber9withFloatEf
- __ZZN17AppleAVDAnalytics18setEventEntryFloatEP12OSDictionaryPKcfE11_os_log_fmt
- __ZZN18AppleAVDUserClient14allocateMemoryEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutE21kalloc_type_view_3690
- __ZZN18AppleAVDUserClient14allocateMemoryEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutE21kalloc_type_view_3712
- __ZZN18AppleAVDUserClient16deallocateMemoryEP28_sAppleAVDDeallocateMemoryInP29_sAppleAVDDeallocateMemoryOutE21kalloc_type_view_3779
- __ZZN18AppleAVDUserClient30getBoundaryCompliantAllocationEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutbE21kalloc_type_view_3827
- __ZZN18AppleAVDUserClient30getBoundaryCompliantAllocationEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutbE21kalloc_type_view_3838
- __ZZN18AppleAVDUserClient30getBoundaryCompliantAllocationEP26_sAppleAVDAllocateMemoryInP27_sAppleAVDAllocateMemoryOutbE21kalloc_type_view_3875
- __ZZN18AppleAVDUserClient32DeallocateUserClientKernelMemoryEvE21kalloc_type_view_4249
Functions:
~ __ZN17AppleAVDAnalytics22sendCoreAnalyticsEventER19session_analytics_s : 1668 -> 1628
~ __ZN17AppleAVDAnalytics19calculatePercentageEyy : 60 -> 52
- __ZN17AppleAVDAnalytics18setEventEntryFloatEP12OSDictionaryPKcf
~ __ZN13AppleAVDPower16callHardResetAPIEv : 272 -> 308
~ __ZN8AppleAVD5startEP9IOService : 13672 -> 13948
~ __ZN18AppleAVDUserClient14externalMethodEjP31IOExternalMethodArgumentsOpaque : 188 -> 228
~ __ZN18AppleAVDUserClient13createDecoderEP25_sAppleAVDCreateDecoderInP26_sAppleAVDCreateDecoderOut : 2832 -> 2836
CStrings:
+ "AppleAVD: %s(): active_mcc_bit_vector_val is 0x%x\n"
+ "AppleAVD: ERROR: %s(): [Core %u] AVD Reset Function handle is NULL! Check the EDT\n"
+ "AppleAVD: INFO: %s(): Unexpected active-mcc-bit-vector value. Assume tunablesIdx is 1.\n"
+ "AppleAVD: INFO: %s(): [Core %u] AVD reset function returned %d\n"
+ "AppleAVD: INFO: %s(): [Core %u] resetPsdService(0, %u) returned %d\n"
- "AppleAVD: ERROR: %s(): AVD Reset Function handle is NULL! Check the EDT\n"
- "AppleAVD: INFO: %s(): AVD reset function returned %d\n"
- "AppleAVD: INFO: %s(): resetPsdService(0) returned %d\n"
- "setEventEntryFloat"
```
