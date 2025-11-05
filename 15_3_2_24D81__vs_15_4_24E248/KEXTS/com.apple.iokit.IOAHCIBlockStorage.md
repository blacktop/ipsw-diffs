## com.apple.iokit.IOAHCIBlockStorage

> `com.apple.iokit.IOAHCIBlockStorage`

```diff

-362.0.0.0.0
-  __TEXT.__cstring: 0x5db7
+362.100.1.0.0
+  __TEXT.__cstring: 0x5e97
   __TEXT.__const: 0x28
-  __TEXT_EXEC.__text: 0x16350
+  __TEXT_EXEC.__text: 0x163e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x418
   __DATA.__common: 0x1c0
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__auth_got: 0x488
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x4fb0
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 32FF057F-7620-34B8-B676-009D896CAB38
-  Functions: 508
-  Symbols:   1183
-  CStrings:  426
+  UUID: F86B8818-BFA1-3FF8-AAFF-8F3D375B54F1
+  Functions: 562
+  Symbols:   1261
+  CStrings:  432
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ZN19AppleAHCIDiskDriver8PolledIOEhP18IOMemoryDescriptorjyy18IOPolledCompletion.cold.1
+ _ZN22AppleAHCIWatchdogTimer5RearmEv.cold.2
+ _ZN22IOAHCIDiskQueueManager20InitWithWorkLoopLockEP9IOServiceP21AppleAHCIWorkLoopLock.cold.1
+ _ZN22IOAHCIDiskQueueManager23GetRequestBlockInternalEh.cold.1
+ _ZN24IOAHCIBlockStorageDriver17AllocateResourcesEv.cold.1
+ _ZN24IOAHCIBlockStorageDriver17AllocateResourcesEv.cold.2
+ _ZN24IOAHCIBlockStorageDriver17AllocateResourcesEv.cold.3
+ _ZN24IOAHCIBlockStorageDriver17AllocateResourcesEv.cold.4
+ _ZN24IOAHCIBlockStorageDriver17AllocateResourcesEv.cold.5
+ _ZN24IOAHCIBlockStorageDriver17AllocateResourcesEv.cold.6
+ _ZN24IOAHCIBlockStorageDriver20EnableDeviceFeaturesEv.cold.2
+ _ZN24IOAHCIBlockStorageDriver5startEP9IOService.cold.1
+ _ZN24IOAHCIBlockStorageDriver5startEP9IOService.cold.2
+ __MergedGlobals
+ __ZN22IOAHCIDiskQueueManager18SetTerminateReasonEj
+ __ZN22IOAHCIDiskQueueManager23GetPowerStateStatisticsEv
+ __ZN7OSArray9withArrayEPKS_j
+ __ZZL25CompleteZeroBlockTransferP19IOStorageCompletionE21kalloc_type_view_5921
+ __ZZN22IOAHCIDiskQueueManager18CreateSATARequestsEiE20kalloc_type_view_461
+ __ZZN22IOAHCIDiskQueueManager4freeEvE20kalloc_type_view_354
+ __ZZN24IOAHCIBlockStorageDriver14AsyncReadWriteEP18IOMemoryDescriptoryyP19IOStorageAttributesP19IOStorageCompletionE21kalloc_type_view_3341
+ __ZZN24IOAHCIBlockStorageDriver19DeallocateResourcesEvE21kalloc_type_view_1448
+ __ZZN24IOAHCIBlockStorageDriver19DeallocateResourcesEvE21kalloc_type_view_1466
+ __ZZN24IOAHCIBlockStorageDriver19DeallocateResourcesEvE21kalloc_type_view_1484
+ __ZZN24IOAHCIBlockStorageDriver20AllocateSATARequestsEiE21kalloc_type_view_1629
+ __ZZN24IOAHCIBlockStorageDriver20AllocateSATARequestsEiE21kalloc_type_view_1641
+ __ZZN24IOAHCIBlockStorageDriver20AllocateSATARequestsEiE21kalloc_type_view_1653
+ __ZZN24IOAHCIBlockStorageDriver20AllocateSATARequestsEiE21kalloc_type_view_1675
+ __ZZN24IOAHCIBlockStorageDriver4freeEvE20kalloc_type_view_603
+ __ZZN24IOAHCIBlockStorageDriver5startEP9IOServiceE20kalloc_type_view_457
+ __ZZN24IOAHCIBlockStorageDriver5startEP9IOServiceE20kalloc_type_view_568
+ _get_bsdtask_info
+ _proc_name
+ _proc_pid
- __ZL12sPowerStates
- __ZL23sSATAExpressPowerStates
- __ZZL25CompleteZeroBlockTransferP19IOStorageCompletionE21kalloc_type_view_5892
- __ZZN22IOAHCIDiskQueueManager18CreateSATARequestsEiE20kalloc_type_view_440
- __ZZN22IOAHCIDiskQueueManager4freeEvE20kalloc_type_view_347
- __ZZN24IOAHCIBlockStorageDriver14AsyncReadWriteEP18IOMemoryDescriptoryyP19IOStorageAttributesP19IOStorageCompletionE21kalloc_type_view_3314
- __ZZN24IOAHCIBlockStorageDriver19DeallocateResourcesEvE21kalloc_type_view_1421
- __ZZN24IOAHCIBlockStorageDriver19DeallocateResourcesEvE21kalloc_type_view_1439
- __ZZN24IOAHCIBlockStorageDriver19DeallocateResourcesEvE21kalloc_type_view_1457
- __ZZN24IOAHCIBlockStorageDriver20AllocateSATARequestsEiE21kalloc_type_view_1602
- __ZZN24IOAHCIBlockStorageDriver20AllocateSATARequestsEiE21kalloc_type_view_1614
- __ZZN24IOAHCIBlockStorageDriver20AllocateSATARequestsEiE21kalloc_type_view_1626
- __ZZN24IOAHCIBlockStorageDriver20AllocateSATARequestsEiE21kalloc_type_view_1648
- __ZZN24IOAHCIBlockStorageDriver4freeEvE20kalloc_type_view_590
- __ZZN24IOAHCIBlockStorageDriver5startEP9IOServiceE20kalloc_type_view_444
- __ZZN24IOAHCIBlockStorageDriver5startEP9IOServiceE20kalloc_type_view_555
CStrings:
+ "12111112122212121111112111121111222222211222221212211112222121"
+ "1211111212221212111111211112111122222221122222121221111222212122222222222222222"
+ "Power State Transition Dark Wake"
+ "Power State Transition Duration Sleep"
+ "Power State Transition Duration Wake"
+ "Power State Transition Process"
+ "Power State Transition Stats"
+ "Power State Transition Terminate Reason"
- "121111121222121211111121111211112212222212122111122221"
- "12111112122212121111112111121111221222221212211112222122222222222222222"

```
