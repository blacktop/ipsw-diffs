## com.apple.driver.AppleIISController

> `com.apple.driver.AppleIISController`

```diff

-420.1.0.0.0
+440.2.0.0.0
   __TEXT.__cstring: 0x985
-  __TEXT_EXEC.__text: 0x7264
+  __TEXT_EXEC.__text: 0x743c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x100

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x27e0
+  __DATA_CONST.__const: 0x27e8
   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 4475ED57-3D85-3FA1-9373-BE0F69C32BAF
-  Functions: 200
-  Symbols:   632
+  UUID: 89A93789-3AFB-3564-AC2F-F1427743EDFC
+  Functions: 201
+  Symbols:   633
   CStrings:  85
 
Symbols:
+ __ZN21AppleARMIISController32getDeactivateOnlyWhenStoppedFlagEv
Functions:
~ __ZN21AppleARMIISController5startEP9IOService : 1756 -> 1748
~ __ZN21AppleARMIISController18setPowerStateGatedEmP9IOService : 208 -> 224
~ __ZN21AppleARMIISController4freeEv : 216 -> 220
~ __ZN21AppleARMIISController23calculateStandardTimingEP17AppleARMIISConfigPjS2_S2_S2_ : 224 -> 232
~ __ZN21AppleARMIISController15updateIISConfigEP17AppleARMIISDevice : 132 -> 136
~ __ZN21AppleARMIISController22enqueueIISCommandGatedEP17AppleARMIISDevicejP18AppleARMIISCommand : 1788 -> 1784
~ __ZN21AppleARMIISController18completeIISCommandEP18AppleARMIISCommand : 1052 -> 1112
~ __ZN21AppleARMIISController20completeIISNoCommandEv : 168 -> 176
~ __ZN21AppleARMIISController19stopIISCommandGatedEP17AppleARMIISDevicej : 352 -> 360
~ __ZN21AppleARMIISController18getPhysicalChannelEP17AppleARMIISConfigjjPj : 52 -> 56
~ __ZN21AppleARMIISController25getSupportedChannelCountsEP17AppleARMIISConfigj : 128 -> 152
~ __ZNK17AppleARMIISDevice12getIISConfigEP17AppleARMIISConfig : 220 -> 224
~ __ZN17AppleARMIISDevice12setIISConfigEP17AppleARMIISConfig : 296 -> 300
~ __ZN17AppleARMIISDevice12setIISMasterEb : 112 -> 116
~ __ZN17AppleARMIISDevice16setMCLKFrequencyEy : 268 -> 272
~ __ZN17AppleARMIISDevice17setLRCLKFrequencyEy : 224 -> 228
~ __ZNK17AppleARMIISDevice15getChannelCountEj : 24 -> 28
~ __ZN17AppleARMIISDevice15setChannelCountEjj : 128 -> 136
~ __ZN17AppleARMIISDevice17setBitsPerChannelEjj : 112 -> 116
~ __ZN17AppleARMIISDevice14setBitsPerSlotEjj : 112 -> 116
~ __ZNK17AppleARMIISDevice14getBitsPerSlotEj : 96 -> 100
~ __ZN17AppleARMIISDevice14validIISConfigEjjjy : 248 -> 264
~ __ZN17AppleARMIISDevice21initWithRegistryEntryEP15IORegistryEntryP9IOService : 868 -> 932
~ __ZN18AppleARMIISCommand4freeEv : 28 -> 32
+ __ZN21AppleARMIISController32getDeactivateOnlyWhenStoppedFlagEv
~ __ZN17AppleARMIISSwitch15connectI2SPortsEjjjjjjjjbPj : 1416 -> 1444
~ __ZNK24AppleARMFunctionIISRoute14getClockDomainEj : 336 -> 296
~ __ZN25AppleARMFunctionIISActive4freeEv : 120 -> 124
~ __ZN17AppleARMIISSwitch5startEP9IOService : 1004 -> 996
~ __ZN17AppleARMIISSwitch4freeEv : 244 -> 252
~ __ZNK17AppleARMIISSwitch20copyRouteDescriptionEjjjjj : 280 -> 320
~ __ZNK17AppleARMIISSwitch15_connectObjectsEjjPKNS_9ChangeSetEPjS3_S3_P7OSArrayS5_b : 2736 -> 2940
~ __ZNK17AppleARMIISSwitch15_makeConnectionENS_14ConnectionTypeEjjPjS1_ : 568 -> 540
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleIISController/AppleARMIIS.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleIISController/AppleARMIIS.cpp"

```
