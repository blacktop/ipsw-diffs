## com.apple.iokit.IOBufferCopyEngineFamily

> `com.apple.iokit.IOBufferCopyEngineFamily`

```diff

-98.0.0.0.0
+98.100.1.0.0
+  __TEXT.__const: 0xac
   __TEXT.__cstring: 0x761
-  __TEXT.__const: 0x3c
-  __TEXT_EXEC.__text: 0x8e18
+  __TEXT_EXEC.__text: 0x91b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x150

   __DATA_CONST.__const: 0x2880
   __DATA_CONST.__kalloc_type: 0x2c0
   __DATA_CONST.__kalloc_var: 0x5a0
-  UUID: 84DF7F5D-C47E-3E0C-95AC-2ECA8949B685
+  UUID: C843847D-43C3-3CFD-9335-0AE66C2CB05C
   Functions: 320
   Symbols:   849
   CStrings:  60
Functions:
~ __ZN18IOBufferCopyEngine5startEP9IOService : 952 -> 948
~ __ZN18IOBufferCopyEngine4freeEv : 304 -> 308
~ __ZN18IOBufferCopyEngine27createCompletionMemoryQueueEP23IOBufferCopyEventSourceti : 572 -> 560
~ __ZN18IOBufferCopyEngine27createSubmissionMemoryQueueEP27IOBufferCopySubmissionQueuePv : 668 -> 672
~ __ZN18IOBufferCopyEngine7prepareEPvP18IOMemoryDescriptorj : 1432 -> 1452
~ __ZN18IOBufferCopyEngine9configureEjitP8IOMapper : 728 -> 884
~ __ZN18IOBufferCopyEngine8shutdownEv : 440 -> 452
~ __ZN18IOBufferCopyEngine30handleCompletionQueueInterruptEi : 168 -> 192
~ __ZN18IOBufferCopyEngine18_createMemoryQueueEtj : 800 -> 820
~ __ZN18IOBufferCopyEngine18_requestDMACommandEPv : 232 -> 236
~ __ZN18IOBufferCopyEngine25_registerMemoryQueueGatedEPNS_24MemoryQueueConfigurationEPK8OSSymbolj : 384 -> 392
~ __ZN18IOBufferCopyEngine27_unregisterMemoryQueueGatedEPv : 360 -> 368
~ __ZN18IOBufferCopyEngine22_flushMemoryQueueGatedEPv : 360 -> 368
~ __ZN18IOBufferCopyEngine28_setMemoryQueuePropertyGatedEPvjy : 384 -> 392
~ __ZN24IOBufferCopyCommandQueue18initWithCompletionEPFvP8OSObjectP27IOBufferCopySubmissionQueueEt : 160 -> 180
~ __ZN34IOBufferCopyEngineUserClientBufferC2EPK11OSMetaClass : 60 -> 68
~ __ZN34IOBufferCopyEngineUserClientBufferC1EPK11OSMetaClass : 60 -> 68
~ __ZN34IOBufferCopyEngineUserClientBufferC2Ev : 96 -> 104
~ __ZN33IOBufferCopyEngineUserClientStateC2EPK11OSMetaClass : 60 -> 68
~ __ZN33IOBufferCopyEngineUserClientStateC1EPK11OSMetaClass : 60 -> 68
~ __ZNK33IOBufferCopyEngineUserClientState9MetaClass5allocEv : 112 -> 120
~ __ZN33IOBufferCopyEngineUserClientStateC1Ev : 96 -> 104
~ __ZN33IOBufferCopyEngineUserClientStateC2Ev : 96 -> 104
~ __ZN28IOBufferCopyEngineUserClient4freeEv : 216 -> 220
~ __ZN28IOBufferCopyEngineUserClient21createSubmissionQueueERNS_15MethodArgumentsE : 372 -> 364
~ __ZN28IOBufferCopyEngineUserClient19externalMethodGatedEPvS0_S0_S0_ : 80 -> 100
~ __ZN28IOBufferCopyEngineUserClient15MethodArgumentsC2EPS_P25IOExternalMethodArguments : 236 -> 232
~ __ZN33IOBufferCopyEngineUserClientState16initWithWorkloopEP10IOWorkLoop : 364 -> 368
~ __ZN33IOBufferCopyEngineUserClientState17asyncCleanupThunkEPvS0_ : 172 -> 188
~ __ZN33IOBufferCopyEngineUserClientState4freeEv : 336 -> 340
~ __ZN34IOBufferCopyEngineUserClientBuffer4freeEv : 176 -> 180
~ __ZN23IOBufferCopyEventSource21removeSubmissionQueueEP27IOBufferCopySubmissionQueue : 400 -> 420
~ __ZN23IOBufferCopyEventSource4freeEv : 280 -> 284
~ __ZN23IOBufferCopyEventSource22checkCompletionPendingEv : 88 -> 92
~ __ZN23IOBufferCopyEventSource23_processCompletionQueueEv : 404 -> 408
~ __ZN27IOBufferCopySubmissionQueue24getCompletionInformationEPPvPiPyS3_PP22IOBufferCopyDMACommand : 304 -> 320
~ __ZN27IOBufferCopySubmissionQueue18initWithCompletionEPFvP8OSObjectPS_EPK8OSSymboljt : 316 -> 320
~ __ZN27IOBufferCopySubmissionQueue4freeEv : 300 -> 304
~ __ZN27IOBufferCopySubmissionQueue24setCompletionInformationEtiyy : 136 -> 132
~ _IOBCCreateMemoryQueue : 176 -> 668
~ _IOBCSetBuffers : 52 -> 60
~ _IOBCSetNotificationToken : 84 -> 80
~ _IOBCCheckCompletionQueuePending : 88 -> 84
~ _IOBCGetCompletionQueueElement : 196 -> 192
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOBufferCopyEngine/Library/IOBufferCopyMemoryQueue.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOBufferCopyEngine/Library/IOBufferCopyMemoryQueue.c"

```
