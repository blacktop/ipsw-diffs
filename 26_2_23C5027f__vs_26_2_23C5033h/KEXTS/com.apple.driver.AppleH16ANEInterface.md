## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.102.1.0.0
-  __TEXT.__const: 0xb38
-  __TEXT.__cstring: 0xee30
-  __TEXT.__os_log: 0x35d44
-  __TEXT_EXEC.__text: 0x106998
+9.200.2.0.0
+  __TEXT.__const: 0xbb8
+  __TEXT.__cstring: 0xee37
+  __TEXT.__os_log: 0x3607f
+  __TEXT_EXEC.__text: 0x106cf0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x434c
   __DATA.__common: 0x658

   __DATA_CONST.__const: 0xc2f8
   __DATA_CONST.__kalloc_type: 0x3ac0
   __DATA_CONST.__kalloc_var: 0x3160
-  UUID: 8EF8C3FD-0E46-3FE5-B25F-5DE237E72514
+  UUID: F938B465-6044-3164-8945-D5A079F97BD6
   Functions: 3296
   Symbols:   0
-  CStrings:  4329
+  CStrings:  4331
 
Functions:
~ __ZN9ANEDriver20ANE_MemoryMapRequestEPK18ANEMemoryMapParamsb : 312 -> 88
~ __ZN12ANEScheduler25moveResourceToUnwireQueueENSt3__110shared_ptrI11ANEResourceEE : 1092 -> 1100
~ __ZN12ANEScheduler25moveResourceToUnwireQueueEP21ANEResourceCollectiony : 1304 -> 1316
~ sub_fffffe0009319f58 -> sub_fffffe0009277d6c : 336 -> 312
~ sub_fffffe000931a28c -> sub_fffffe0009278088 : 356 -> 332
~ __ZN11ANEHWDevice32decProcedureCallCacheHandleCountEb : 476 -> 492
~ __ZN11ANEHWDevice40ANE_ProgramPrepareAndSubmitRequest_gatedEP21ANEProgramRequestArgsP15ANESharedEventsP37ANEProgramSendRequestAdditionalParams : 15512 -> 16036
~ __ZN11ANEHWDevice26ANE_MemoryMapRequest_gatedEPK18ANEMemoryMapParamsbbRNSt3__110unique_ptrI21ANEResourceCollectionNS3_14default_deleteIS5_EEEE : 12680 -> 12532
~ sub_fffffe0009340fbc -> __ZN9ANEDriver20ANE_MemoryMapRequestEPK18ANEMemoryMapParamsb : 140 -> 380
~ __ZN18ANEProgramResource13wireResourcesEb : 1504 -> 1544
~ __ZN20ANEProgramRTResource29programRTSendInferenceRequestEP21ANEProgramRequestArgsP15ANESharedEventsP37ANEProgramSendRequestAdditionalParams : 12344 -> 12952
~ __ZN11ANEHWDevice23EnableANEClocksAndPowerEbb : 2632 -> 2636
~ __ZN11ANEHWDevice36ANE_RegisterDebugWorkProcessor_gatedEP37ANEDebugWorkProcessorRegistrationArgsPyPv : 860 -> 880
~ __ZN11ANEHWDevice25ReleaseDebugWorkProcessorEP8ipc_port : 3152 -> 3120
~ __ZN11ANEHWDevice8ANE_InitEv : 13608 -> 13640
~ __ZN11ANEHWDevice15mapFwCTRRRegionEv : 3796 -> 3792
~ __ZN11ANEHWDevice5startEP9IOService : 18304 -> 18424
~ sub_fffffe00093be7cc -> sub_fffffe000931cb3c : 1268 -> 1300
~ __ZN11ANEHWDevice23initializeANEPropertiesEv : 1496 -> 1488
~ __ZN11ANEHWDevice22initializeANESoCConfigEv : 10684 -> 10424
~ __ZN11ANEHWDevice15aneExclaveCycleEbb : 2320 -> 2332
~ __ZN11ANEHWDevice24ANE_ProcessDestroy_gatedEP21ANEProcessDestroyArgsbbP18ANEProgramResourcePjS4_.cold.3 : 128 -> 116
~ __ZN11ANEHWDevice23handleRequestCompletionEP10ANERequesti.cold.1 : 124 -> 112
~ __ZN11ANEHWDevice23ANE_ProcessCreate_gatedEP20ANEProcessCreateArgsP26ANEProcessCreateArgsOutputP18ANEProgramResource.cold.2 : 136 -> 124
~ __ZN11ANEHWDevice23ANE_ProcessCreate_gatedEP20ANEProcessCreateArgsP26ANEProcessCreateArgsOutputP18ANEProgramResource.cold.3 : 128 -> 116
~ __ZN11ANEHWDevice12ProcessReMapEP10ANEProcess.cold.2 : 136 -> 132
~ sub_fffffe000940f44c -> sub_fffffe000936d6a8 : 124 -> 112
~ __ZN11ANEHWDevice38ANE_unwireAllAutoPrewiredBuffers_gatedEv.cold.1 : 196 -> 188
~ sub_fffffe000940f6dc -> sub_fffffe000936d924 : 144 -> 140
~ __ZNK11ANEResource19invokeActionUnGatedENSt3__18functionIFivEEE.cold.1 : 144 -> 140
~ __ZN11ANEHWDevice16ANE_RestoreStateEv.cold.1 : 144 -> 140
~ __ZN11ANEHWDevice32cleanupRCClientWithContext_gatedER16ANEClientContext.cold.1 : 152 -> 148
CStrings:
+ "11111111112221"
+ "SNEXL"
+ "[DEBUG] %s: %s: ProcessParams is not valid for programHandle: 0x%llx, programId: %u, processId: %u, transactionId: 0x%llx reqRetainCount: 1"
- "1111111111222"

```
