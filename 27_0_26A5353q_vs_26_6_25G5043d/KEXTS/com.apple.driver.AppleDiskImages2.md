## com.apple.driver.AppleDiskImages2

> `com.apple.driver.AppleDiskImages2`

```diff

-588.0.0.0.2
-  __TEXT.__cstring: 0x3a04 sha256:bc802de4caff4f4e3f709573b31d45b4946cdad5a2842cfed8cbfe8536bb96e9
-  __TEXT.__os_log: 0x23d8 sha256:96c6f4cf351c965765764bf9b7cb2c339928338e051a96f0f78781e33f72b83d
-  __TEXT.__const: 0x18 sha256:feee68a7f503cf5e4bb6c0800fcf0690be0b9a0588ff523d4ffeeb2af17f8ad9
-  __TEXT_EXEC.__text: 0x11edc sha256:8872f0c23ded682f1f10e91f94d86f0884b1b61da6d863f4e8af2128a49e1bc2
+524.160.9.0.0
+  __TEXT.__cstring: 0x24b8 sha256:58a8e5412ac6c10cd04ae1cce95fadc3e91d2d5d902680565e7cb8c25c876162
+  __TEXT.__os_log: 0x1208 sha256:f4f9e0fc54ec6bc276218e0105602e7d04a9f21bc393fd7a2cab09be999e1055
+  __TEXT.__const: 0x10 sha256:98ac5716f57d2f0b626702c8de3b4fcecdca08e840a7d54cdf61b38c1ffccbde
+  __TEXT_EXEC.__text: 0xe048 sha256:1702c82649064dceb6b18c9a69352576575e4829df033a0d55097c8168253346
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x4e8 sha256:21cd4263767a5d033381a1e4f3ba452281d57876990ed4170cc28b4f1189f860
+  __DATA.__data: 0x4e8 sha256:147a216ea37f92375a82e5ed10af9326cf9f7d5d52d7c7211fc7d8637d70570c
   __DATA.__common: 0x148 sha256:7b4499c3cc6e82a9da3100028f52af7f8c1e9ee60e33010a108e401989782962
   __DATA.__bss: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
-  __DATA_CONST.__mod_init_func: 0x30 sha256:224261adabf69056820a8acbfeec5f974fbda228f40eb8c536a81b80a7b8829c
-  __DATA_CONST.__mod_term_func: 0x30 sha256:87ce1a44362f7e6530e0b0f9a96e5aef99ded154f1a7519b0e7ae0c23e67e8a2
-  __DATA_CONST.__const: 0x31c0 sha256:e33b1a00a66d87050e4859f8cc66d144c48c05bb1b0e0093e39330e1ef8b5647
-  __DATA_CONST.__kalloc_type: 0x280 sha256:a16b0da5453f649813b33e55905b2eddce8fa11625252843b83c43ff937d60b8
-  __DATA_CONST.__assert: 0x14 sha256:b3f0b462b8f051da1ef530f833ead9291d272571654f0add9f2eb04916b427d9
-  __DATA_CONST.__kalloc_var: 0xf0 sha256:7a0a7182c963d2cd07f503e8688b97bcd3bf5031e1d25714b5fd83f72d3952d0
-  __DATA_CONST.__auth_got: 0x2d8 sha256:fcb499ecf2acb224fb6a4492925e48baec72a1ffda43e4cf40690ae650cfc0fe
-  __DATA_CONST.__got: 0xa0 sha256:b2e35a7eecdfcc7598d8be506ea32665d73da777288729dcafc0782f2051e276
-  UUID: 2222C4C0-F13F-3622-A487-F00AB95AB168
-  Functions: 395
-  Symbols:   1210
-  CStrings:  394
+  __DATA_CONST.__auth_got: 0x270 sha256:2f87941e0c981dedd8a40930a1ae339754934a82fe5c70a9e9ecee69eaa3cae6
+  __DATA_CONST.__got: 0xa0 sha256:2f04d0b1308b59abf4154a010fa4fc4b3df1aebc6bdbb4e3c9d45f8e828b60c0
+  __DATA_CONST.__mod_init_func: 0x30 sha256:5e6f0d4f0f18460e5d9393909d4fc9b08e02485251825a5bbf14da3185034ad8
+  __DATA_CONST.__mod_term_func: 0x30 sha256:61a7d9849f73ef1f0a5d78ddca1b15227c480f2ba2f85089d6ee75ae1972a955
+  __DATA_CONST.__const: 0x3160 sha256:beb7a84adec3b372bbdbda65548ce17d79ea5bcfdadf9bf1ca79f6b04c5524d6
+  __DATA_CONST.__kalloc_type: 0x280 sha256:dd584db33d81424f529deec84b3246e0ef5b65adb4a29a2cc1d453d6a1217f96
+  __DATA_CONST.__kalloc_var: 0xf0 sha256:aec9f9bf0dd20ed4e6639d7f9dc1fe149df80c1f2b913b86b6c9ac2e1c699274
+  UUID: D6EC6715-6D79-3D05-A642-46F1B4A3E71C
+  Functions: 336
+  Symbols:   1042
+  CStrings:  293
 
Symbols:
+ _ZN19DIDeviceRequestPool14ReleaseBuffersEv.cold.1
+ _ZN19DIDeviceRequestPool16AllocateRequestsEmymj.cold.2
+ _ZN19DIDeviceRequestPool16AllocateRequestsEmymj.cold.3
+ _ZN19DIDeviceRequestPool16AllocateRequestsEmymj.cold.4
+ _ZN20AppleDiskImageDevice13doSynchronizeEyyj.cold.1
+ __ZN12IOLWPoolBase23releaseReservedElementsEm
+ __ZN20AppleDiskImageDevice14PrepareRequestEP15DIDeviceRequest5kDIIObP19IOStorageAttributes
+ __ZN20AppleDiskImageDevice16PrepareIORequestEP15DIDeviceRequestP18IOMemoryDescriptorymymP19IOStorageAttributesb
+ __ZN20AppleDiskImageDevice19prepareUnmapCommandEP15DIDeviceRequestP26IOBlockStorageDeviceExtentb
+ __ZN20AppleDiskImageDevice22CompleteRequestElementEP15DIDeviceRequestib
+ __ZN20AppleDiskImageDevice22sendSynchronousCommandEP15DIDeviceRequest5kDIIO
+ __ZN20AppleDiskImageDevice24HandIOCommandToExecutionEP15DIDeviceRequestb
+ __ZN20AppleDiskImageDevice38PrepareMappedBuffersMightFaultForUnmapEP15DIDeviceRequestP26IOBlockStorageDeviceExtent
+ __ZN8IOLWPoolI14DISharedBufferE14dequeueElementEbPbb
+ __ZN8IOLWPoolI15DIDeviceRequestE14dequeueElementEbPbb
+ __ZZN19DIDeviceRequestPool19ReleasePoolElementsI14DISharedBufferEEvRjR8IOLWPoolIT_EE11_os_log_fmt
+ __ZZN19DIDeviceRequestPool19ReleasePoolElementsI14DISharedBufferEEvRjR8IOLWPoolIT_EE11_os_log_fmt_0
+ __ZZN19DIDeviceRequestPool19ReleasePoolElementsI15DIDeviceRequestEEvRjR8IOLWPoolIT_EE11_os_log_fmt
+ __ZZN19DIDeviceRequestPool19ReleasePoolElementsI15DIDeviceRequestEEvRjR8IOLWPoolIT_EE11_os_log_fmt_0
+ __ZZN20AppleDiskImageDevice22CompleteRequestElementEP15DIDeviceRequestibE11_os_log_fmt
+ __ZZN20AppleDiskImageDevice5startEP9IOServiceE11_os_log_fmt
+ __ZZN20AppleDiskImageDevice9InitForIOEP20DIDeviceIOUserClientP16DIDeviceIOParamstE11_os_log_fmt_0
+ __ZZN8IOLWPoolI14DISharedBufferE15dequeueElementsEbmP11queue_entryPbmE11_os_log_fmt
- _IOLockSleepDeadline
- _ZN19DIDeviceRequestPool19ReleasePoolElementsI14DISharedBufferEEvRjR8IOLWPoolIT_E4Mode.cold.1
- _ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv.cold.1
- _ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv.cold.2
- _ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv.cold.3
- _ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv.cold.4
- _ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv.cold.5
- _ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv.cold.6
- _ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv.cold.7
- _ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv.cold.8
- _ZN19DIDeviceRequestPool4freeEv.cold.1
- _ZN19DIDeviceRequestPool4freeEv.cold.2
- _ZN19DIDeviceRequestPool4freeEv.cold.3
- _ZN19DIDeviceRequestPool4freeEv.cold.4
- _ZN20AppleDiskImageDevice14PrepareRequestEP15DIDeviceRequest5kDIIONS_19KernelInflightGuardEbP19IOStorageAttributesb.cold.1
- __ZN12IOLWPoolBase10deactivateEv
- __ZN12IOLWPoolBase10reactivateEv
- __ZN12IOLWPoolBase18waitForTargetCountEm
- __ZN12IOLWPoolBase20wakeupSleepersLockedEb
- __ZN12IOLWPoolBase23releaseReservedElementsEmm
- __ZN13DIIOMutexLock4LockEv
- __ZN13DIIOMutexLock5SleepEPvNS_20InterruptibilityTypeE
- __ZN13DIIOMutexLock6UnlockEv
- __ZN13DIIOMutexLock6WakeupEPvb
- __ZN13DIIOMutexLockC1EP7_IOLock
- __ZN13DIIOMutexLockC2EP7_IOLock
- __ZN13DIIOMutexLockD1Ev
- __ZN13DIIOMutexLockD2Ev
- __ZN14DIIOSimpleLock4LockEv
- __ZN14DIIOSimpleLock6UnlockEv
- __ZN14DIIOSimpleLockC1EP13_IOSimpleLock
- __ZN14DIIOSimpleLockC2EP13_IOSimpleLock
- __ZN14DIIOSimpleLockD1Ev
- __ZN14DIIOSimpleLockD2Ev
- __ZN14DIIOUniqueLockI13DIIOMutexLockE5SleepEPvNS0_20InterruptibilityTypeE
- __ZN14DIIOUniqueLockI13DIIOMutexLockE6WakeupEPvb
- __ZN14DIIOUniqueLockI13DIIOMutexLockEC1ERS0_
- __ZN14DIIOUniqueLockI13DIIOMutexLockEC1ERS0_N7details18DIIOUniqueLockBaseIS0_E11AcquireLockE
- __ZN14DIIOUniqueLockI13DIIOMutexLockEC1ERS0_N7details18DIIOUniqueLockBaseIS0_E9DeferLockE
- __ZN14DIIOUniqueLockI13DIIOMutexLockEC2ERS0_
- __ZN14DIIOUniqueLockI13DIIOMutexLockEC2ERS0_N7details18DIIOUniqueLockBaseIS0_E11AcquireLockE
- __ZN14DIIOUniqueLockI13DIIOMutexLockEC2ERS0_N7details18DIIOUniqueLockBaseIS0_E9DeferLockE
- __ZN14DIIOUniqueLockI14DIIOSimpleLockEC1ERS0_
- __ZN14DIIOUniqueLockI14DIIOSimpleLockEC2ERS0_
- __ZN14IntervalMapLRU10reactivateEv
- __ZN14IntervalMapLRU18deactivateAndClearEv
- __ZN15DIDeviceRequest14createReservedEj
- __ZN18IOTimerEventSource16timerEventSourceEP8OSObjectPFvS1_PS_E
- __ZN19DIDeviceRequestPool18GetReservedRequestEv
- __ZN19DIDeviceRequestPool19ReleasePoolElementsI14DISharedBufferEEvRjR8IOLWPoolIT_E4Mode
- __ZN19DIDeviceRequestPool21DeactivateBuffersPoolEv
- __ZN19DIDeviceRequestPool22ReleaseReservedRequestEv
- __ZN19DIDeviceRequestPool25AddBuffersForReconnectionEymj
- __ZN19DIDeviceRequestPool25AllocateBuffersForRequestEP15DIDeviceRequestmbPFbPvES2_
- __ZN19DIDeviceRequestPool25ReleaseBuffersNonBlockingEv
- __ZN20AppleDiskImageDevice13isDeviceCleanEv
- __ZN20AppleDiskImageDevice13submitRequestEP15DIDeviceRequest5kDIIObb
- __ZN20AppleDiskImageDevice14PrepareRequestEP15DIDeviceRequest5kDIIONS_19KernelInflightGuardEbP19IOStorageAttributesb
- __ZN20AppleDiskImageDevice14ReconnectForIOEP20DIDeviceIOUserClientP16DIDeviceIOParamst
- __ZN20AppleDiskImageDevice14enqueueRequestEP15DIDeviceRequestb
- __ZN20AppleDiskImageDevice16PrepareIORequestEP15DIDeviceRequestP18IOMemoryDescriptorymymP19IOStorageAttributesP19IOStorageCompletion
- __ZN20AppleDiskImageDevice16SetupQueueBufferEy
- __ZN20AppleDiskImageDevice18CreateQueueMappingEv
- __ZN20AppleDiskImageDevice18claimDormantDeviceEj
- __ZN20AppleDiskImageDevice19cleanupDormantStateEv
- __ZN20AppleDiskImageDevice19drainDormantIOQueueEv
- __ZN20AppleDiskImageDevice19prepareUnmapCommandEP15DIDeviceRequestb
- __ZN20AppleDiskImageDevice20PendingRequestHandle12AbortRequestERS_j
- __ZN20AppleDiskImageDevice20PendingRequestHandle17GetPendingRequestERS_j
- __ZN20AppleDiskImageDevice20PendingRequestHandle20MarkRequestAsPendingERS_P15DIDeviceRequest
- __ZN20AppleDiskImageDevice20PendingRequestHandleC1ERS_P15DIDeviceRequestb
- __ZN20AppleDiskImageDevice20PendingRequestHandleC2ERS_P15DIDeviceRequestb
- __ZN20AppleDiskImageDevice20PendingRequestHandleD1Ev
- __ZN20AppleDiskImageDevice20PendingRequestHandleD2Ev
- __ZN20AppleDiskImageDevice20triggerDaemonRespawnEv
- __ZN20AppleDiskImageDevice21incrementWriteCounterEv
- __ZN20AppleDiskImageDevice22flushDeviceWithTimeoutEj
- __ZN20AppleDiskImageDevice22sendSynchronousCommandEP15DIDeviceRequest5kDIIONS_19KernelInflightGuardE
- __ZN20AppleDiskImageDevice23cleanupForDaemonRespawnEv
- __ZN20AppleDiskImageDevice23requestGracefulShutdownEb
- __ZN20AppleDiskImageDevice24dormantIOTimeoutOccurredEP8OSObjectP18IOTimerEventSource
- __ZN20AppleDiskImageDevice24sendDaemonRespawnMessageEv
- __ZN20AppleDiskImageDevice24waitForRequestCompletionEP15DIDeviceRequestPy
- __ZN20AppleDiskImageDevice26SetupDormantRequestBuffersEP15DIDeviceRequest
- __ZN20AppleDiskImageDevice28ValidateAndSetupCommonParamsEP20DIDeviceIOUserClientP16DIDeviceIOParamst
- __ZN20AppleDiskImageDevice38PrepareMappedBuffersMightFaultForUnmapEP15DIDeviceRequest
- __ZN20DIDeviceIOUserClient17DrainDormantQueueEP8OSObjectPvP25IOExternalMethodArguments
- __ZN20DIDeviceIOUserClient20StashFileInformationEP8OSObjectPvP25IOExternalMethodArguments
- __ZN20DIDeviceIOUserClient23RequestGracefulShutdownEP8OSObjectPvP25IOExternalMethodArguments
- __ZN20DIDeviceIOUserClient24RetrieveFileAfterRespawnEP8OSObjectPvP25IOExternalMethodArguments
- __ZN7libkern20intrusive_shared_ptrI20DIDeviceIOUserClient27intrusive_osobject_retainerE5resetEPS1_NS_8retain_tE
- __ZN8IOLWPoolI14DISharedBufferE14dequeueElementE4ModePbb
- __ZN8IOLWPoolI15DIDeviceRequestE14dequeueElementE4ModePbb
- __ZNK13DIIOMutexLockcvbEv
- __ZNK14DIIOSimpleLockcvbEv
- __ZNK20AppleDiskImageDevice14isReconnectionEv
- __ZNK20AppleDiskImageDevice24supportsPersistentAttachEv
- __ZZN15DIDeviceRequest18CallPrepareBuffersEP20AppleDiskImageDevicebE6__desc
- __ZZN19DIDeviceRequestPool16AllocateRequestsEmymjE11_os_log_fmt_1
- __ZZN19DIDeviceRequestPool16AllocateRequestsEmymjE11_os_log_fmt_2
- __ZZN19DIDeviceRequestPool18GetReservedRequestEvE11_os_log_fmt
- __ZZN19DIDeviceRequestPool19ReleasePoolElementsI14DISharedBufferEEvRjR8IOLWPoolIT_E4ModeE11_os_log_fmt
- __ZZN19DIDeviceRequestPool19ReleasePoolElementsI14DISharedBufferEEvRjR8IOLWPoolIT_E4ModeE11_os_log_fmt_0
- __ZZN19DIDeviceRequestPool19ReleasePoolElementsI15DIDeviceRequestEEvRjR8IOLWPoolIT_E4ModeE11_os_log_fmt
- __ZZN19DIDeviceRequestPool19ReleasePoolElementsI15DIDeviceRequestEEvRjR8IOLWPoolIT_E4ModeE11_os_log_fmt_0
- __ZZN19DIDeviceRequestPool22ReleaseReservedRequestEvE11_os_log_fmt
- __ZZN19DIDeviceRequestPool25AddBuffersForReconnectionEymjE11_os_log_fmt
- __ZZN20AppleDiskImageDevice13setIOProviderEP20DIDeviceIOUserClientE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice13setIOProviderEP20DIDeviceIOUserClientE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice13setIOProviderEP20DIDeviceIOUserClientE11_os_log_fmt_2
- __ZZN20AppleDiskImageDevice14PrepareRequestEP15DIDeviceRequest5kDIIONS_19KernelInflightGuardEbP19IOStorageAttributesbE11_os_log_fmt
- __ZZN20AppleDiskImageDevice14ReconnectForIOEP20DIDeviceIOUserClientP16DIDeviceIOParamstE11_os_log_fmt
- __ZZN20AppleDiskImageDevice14ReconnectForIOEP20DIDeviceIOUserClientP16DIDeviceIOParamstE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice14ReconnectForIOEP20DIDeviceIOUserClientP16DIDeviceIOParamstE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice14enqueueRequestEP15DIDeviceRequestbE11_os_log_fmt
- __ZZN20AppleDiskImageDevice14enqueueRequestEP15DIDeviceRequestbE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice14enqueueRequestEP15DIDeviceRequestbE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice15CompleteCommandEjiE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice15CompleteRequestEP15DIDeviceRequestibE11_os_log_fmt
- __ZZN20AppleDiskImageDevice15onIOClientCloseEP20DIDeviceIOUserClientE11_os_log_fmt
- __ZZN20AppleDiskImageDevice15onIOClientCloseEP20DIDeviceIOUserClientE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice15onIOClientCloseEP20DIDeviceIOUserClientE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice15onIOClientCloseEP20DIDeviceIOUserClientE11_os_log_fmt_2
- __ZZN20AppleDiskImageDevice16AbortAllCommandsEvE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice18claimDormantDeviceEjE11_os_log_fmt
- __ZZN20AppleDiskImageDevice19cleanupDormantStateEvE11_os_log_fmt
- __ZZN20AppleDiskImageDevice19drainDormantIOQueueEvE11_os_log_fmt
- __ZZN20AppleDiskImageDevice19drainDormantIOQueueEvE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice19drainDormantIOQueueEvE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice19drainDormantIOQueueEvE11_os_log_fmt_2
- __ZZN20AppleDiskImageDevice19drainDormantIOQueueEvE11_os_log_fmt_3
- __ZZN20AppleDiskImageDevice19drainDormantIOQueueEvE11_os_log_fmt_4
- __ZZN20AppleDiskImageDevice19prepareUnmapCommandEP15DIDeviceRequestbE11_os_log_fmt
- __ZZN20AppleDiskImageDevice20triggerDaemonRespawnEvE11_os_log_fmt
- __ZZN20AppleDiskImageDevice20triggerDaemonRespawnEvE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice20triggerDaemonRespawnEvE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice20triggerDaemonRespawnEvE11_os_log_fmt_2
- __ZZN20AppleDiskImageDevice22flushDeviceWithTimeoutEjE11_os_log_fmt
- __ZZN20AppleDiskImageDevice22flushDeviceWithTimeoutEjE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice22flushDeviceWithTimeoutEjE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice22flushDeviceWithTimeoutEjE11_os_log_fmt_2
- __ZZN20AppleDiskImageDevice22flushDeviceWithTimeoutEjE11_os_log_fmt_3
- __ZZN20AppleDiskImageDevice23cleanupForDaemonRespawnEvE11_os_log_fmt
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_2
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_3
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_4
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_5
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_6
- __ZZN20AppleDiskImageDevice23requestGracefulShutdownEbE11_os_log_fmt_7
- __ZZN20AppleDiskImageDevice24dormantIOTimeoutOccurredEP8OSObjectP18IOTimerEventSourceE11_os_log_fmt
- __ZZN20AppleDiskImageDevice24dormantIOTimeoutOccurredEP8OSObjectP18IOTimerEventSourceE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice24sendDaemonRespawnMessageEvE11_os_log_fmt
- __ZZN20AppleDiskImageDevice24sendDaemonRespawnMessageEvE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice24sendDaemonRespawnMessageEvE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice24sendDaemonRespawnMessageEvE11_os_log_fmt_2
- __ZZN20AppleDiskImageDevice24sendDaemonRespawnMessageEvE11_os_log_fmt_3
- __ZZN20AppleDiskImageDevice25executeBarrierQueueLockedEvE11_os_log_fmt
- __ZZN20AppleDiskImageDevice26SetupDormantRequestBuffersEP15DIDeviceRequestE11_os_log_fmt
- __ZZN20AppleDiskImageDevice26SetupDormantRequestBuffersEP15DIDeviceRequestE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice26SetupDormantRequestBuffersEP15DIDeviceRequestE11_os_log_fmt_1
- __ZZN20AppleDiskImageDevice26executeBarrierQueueElementEP15DIDeviceRequestbE11_os_log_fmt
- __ZZN20AppleDiskImageDevice28ValidateAndSetupCommonParamsEP20DIDeviceIOUserClientP16DIDeviceIOParamstE11_os_log_fmt
- __ZZN20AppleDiskImageDevice28ValidateAndSetupCommonParamsEP20DIDeviceIOUserClientP16DIDeviceIOParamstE11_os_log_fmt_0
- __ZZN20AppleDiskImageDevice9terminateEjE11_os_log_fmt_0
- __ZZN20DIDeviceIOUserClient17DrainDormantQueueEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt
- __ZZN20DIDeviceIOUserClient17DrainDormantQueueEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt_0
- __ZZN20DIDeviceIOUserClient17DrainDormantQueueEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt_1
- __ZZN20DIDeviceIOUserClient20StashFileInformationEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt
- __ZZN20DIDeviceIOUserClient20StashFileInformationEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt_0
- __ZZN20DIDeviceIOUserClient20StashFileInformationEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt_1
- __ZZN20DIDeviceIOUserClient20StashFileInformationEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt_2
- __ZZN20DIDeviceIOUserClient20StashFileInformationEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt_3
- __ZZN20DIDeviceIOUserClient20StashFileInformationEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt_4
- __ZZN20DIDeviceIOUserClient23RequestGracefulShutdownEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt
- __ZZN20DIDeviceIOUserClient7ConnectEP8OSObjectPvP25IOExternalMethodArgumentsE11_os_log_fmt_5
- __ZZN8IOLWPoolI14DISharedBufferE15dequeueElementsE4ModemP11queue_entryPbmE11_os_log_fmt
- _clock_interval_to_deadline
- _host_get_special_port
- _host_priv_self
- _ipc_port_release_send
- _uuid_copy
- _vfs_context_current
- _vnode_getfromfd
- _vnode_put
- _vnode_ref
- _vnode_rele
- _vnode_vid
CStrings:
+ "( 0 != fParams.fQueue )"
+ "( 0 != fParams.fQueueBuffer )"
+ "/AppleInternal/Library/BuildRoots/4~CRehugDtqW4wlSx4mf18e4NxDjoe8QSMVFXFGI8/Library/Caches/com.apple.xbs/TemporaryDirectory.aZOBsH/Sources/DiskImages2/AppleDiskImages2/AppleDiskImageDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugDtqW4wlSx4mf18e4NxDjoe8QSMVFXFGI8/Library/Caches/com.apple.xbs/TemporaryDirectory.aZOBsH/Sources/DiskImages2/AppleDiskImages2/AppleDiskImagesController.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugDtqW4wlSx4mf18e4NxDjoe8QSMVFXFGI8/Library/Caches/com.apple.xbs/TemporaryDirectory.aZOBsH/Sources/DiskImages2/AppleDiskImages2/DIDeviceCreatorUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugDtqW4wlSx4mf18e4NxDjoe8QSMVFXFGI8/Library/Caches/com.apple.xbs/TemporaryDirectory.aZOBsH/Sources/DiskImages2/AppleDiskImages2/DIDeviceIOUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugDtqW4wlSx4mf18e4NxDjoe8QSMVFXFGI8/Library/Caches/com.apple.xbs/TemporaryDirectory.aZOBsH/Sources/DiskImages2/AppleDiskImages2/DIDeviceRequestPool.cpp"
+ "121111111112221211222222222"
+ "12111112122212121111112222222211111111222222111222121222221111121111212"
+ "1221211122111122111"
+ "524.160.9"
+ "IOReturn IOLWPool<DISharedBuffer>::dequeueElements(bool, size_t, queue_head_t *, bool *, size_t) [T = DISharedBuffer]"
+ "[%d] %s::%d: Device was already initialized.\n"
+ "index < fRequestsCount"
+ "res == 0 "
+ "static void DIDeviceRequestPool::ReleasePoolElements(uint32_t &, ::IOLWPool<TElem> &) [TElem = DIDeviceRequest]"
+ "static void DIDeviceRequestPool::ReleasePoolElements(uint32_t &, ::IOLWPool<TElem> &) [TElem = DISharedBuffer]"
+ "virtual bool AppleDiskImageDevice::start(IOService *)"
+ "void AppleDiskImageDevice::CompleteRequestElement(DIDeviceRequest *, int, bool)"
- "/AppleInternal/Library/BuildRoots/4~CQ9yugBNok6kiSW7XMlNG-1-p66wQ77c1EzdLs4/Library/Caches/com.apple.xbs/TemporaryDirectory.aXTYKV/Sources/DiskImages2/AppleDiskImages2/AppleDiskImageDevice.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQ9yugBNok6kiSW7XMlNG-1-p66wQ77c1EzdLs4/Library/Caches/com.apple.xbs/TemporaryDirectory.aXTYKV/Sources/DiskImages2/AppleDiskImages2/AppleDiskImagesController.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQ9yugBNok6kiSW7XMlNG-1-p66wQ77c1EzdLs4/Library/Caches/com.apple.xbs/TemporaryDirectory.aXTYKV/Sources/DiskImages2/AppleDiskImages2/DIDeviceCreatorUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQ9yugBNok6kiSW7XMlNG-1-p66wQ77c1EzdLs4/Library/Caches/com.apple.xbs/TemporaryDirectory.aXTYKV/Sources/DiskImages2/AppleDiskImages2/DIDeviceIOUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQ9yugBNok6kiSW7XMlNG-1-p66wQ77c1EzdLs4/Library/Caches/com.apple.xbs/TemporaryDirectory.aXTYKV/Sources/DiskImages2/AppleDiskImages2/DIDeviceRequestPool.cpp"
- "1211111111122212112222222222122"
- "1211111212221212112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212121212121212121211112222222221111111122222211111222212122222211111121111212"
- "12212111221211122121112"
- "588.0.0"
- "DIDeviceRequest *DIDeviceRequestPool::GetReservedRequest()"
- "DIDeviceRequestPool.h"
- "Daemon died during drain"
- "DaemonPID"
- "Device is not clean"
- "Graceful shutdown failed"
- "IOReturn AppleDiskImageDevice::PrepareRequest(DIDeviceRequest *, enum kDIIO, KernelInflightGuard, bool, IOStorageAttributes *, bool)"
- "IOReturn AppleDiskImageDevice::ReconnectForIO(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)"
- "IOReturn AppleDiskImageDevice::SetupDormantRequestBuffers(DIDeviceRequest *)"
- "IOReturn AppleDiskImageDevice::ValidateAndSetupCommonParams(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)"
- "IOReturn AppleDiskImageDevice::enqueueRequest(DIDeviceRequest *, bool)"
- "IOReturn AppleDiskImageDevice::executeBarrierQueueElement(DIDeviceRequest *, bool)"
- "IOReturn AppleDiskImageDevice::prepareUnmapCommand(DIDeviceRequest *, bool)"
- "IOReturn IOLWPool<DISharedBuffer>::dequeueElements(Mode, size_t, queue_head_t *, bool *, size_t) [T = DISharedBuffer]"
- "PersistentAttach"
- "[%d (ctx)] %s::%d: Allocated reserved flush request with index %u (not in pool)\n"
- "[%d (ctx)] %s::%d: Can't allocate reserved flush request\n"
- "[%d (ctx)] %s::%d: Failed to add any buffers for reconnection (requested %zu)\n"
- "[%d (ctx)] %s::%d: Reserved request already in use\n"
- "[%d (ctx)] %s::%d: Reserved request released\n"
- "[%d] %s::%d: %s, ejecting device\n"
- "[%d] %s::%d: Aborting barrier queue request %d\n"
- "[%d] %s::%d: All kernel requests completed\n"
- "[%d] %s::%d: Already triggered, returning early\n"
- "[%d] %s::%d: Bad argument: fileInfo is NULL\n"
- "[%d] %s::%d: Beginning drain\n"
- "[%d] %s::%d: Buffer allocation succeeded (fNumBuffers=%u)\n"
- "[%d] %s::%d: Cancelled dormant I/O timeout during drain\n"
- "[%d] %s::%d: Cancelled dormant I/O timeout during terminate\n"
- "[%d] %s::%d: Cancelled timeout during cleanup\n"
- "[%d] %s::%d: Completed successfully\n"
- "[%d] %s::%d: Device already clean - skipping flush\n"
- "[%d] %s::%d: Device does not support persistent attach - rejecting\n"
- "[%d] %s::%d: Device is active - not triggering respawn\n"
- "[%d] %s::%d: Device is clean - performing graceful shutdown\n"
- "[%d] %s::%d: Device is inactive/terminating - aborting respawn\n"
- "[%d] %s::%d: Device is not active - cannot perform graceful shutdown\n"
- "[%d] %s::%d: Device is not clean - attempting flush with timeout\n"
- "[%d] %s::%d: Device is not clean and flush not allowed - failing graceful shutdown\n"
- "[%d] %s::%d: Device is shutting down or dormant - terminating old user client %p\n"
- "[%d] %s::%d: Device reconnection - replacing old provider %p with new provider %p (PID=%u)\n"
- "[%d] %s::%d: Device reconnection - setting new IO provider %p (PID=%u)\n"
- "[%d] %s::%d: Dormant request (fIndex=%u) fully satisfied from cache\n"
- "[%d] %s::%d: Dormant request transitioning to active (cmd=%d, offset=%llu, size=%zu)\n"
- "[%d] %s::%d: Drain aborted: device no longer in dormant state\n"
- "[%d] %s::%d: Drain aborted: timeout was not active\n"
- "[%d] %s::%d: Drain already in progress - concurrent drain attempt detected\n"
- "[%d] %s::%d: Drain completed successfully\n"
- "[%d] %s::%d: Drain failed during reconnection (PID=%u)\n"
- "[%d] %s::%d: Enqueue failed during dormant mode\n"
- "[%d] %s::%d: Failed to claim dormant device during reconnection\n"
- "[%d] %s::%d: Failed to get instance ID from device registry\n"
- "[%d] %s::%d: Failed to parse instance ID UUID: %s\n"
- "[%d] %s::%d: Failed to prepare dormant request (fIndex=%u): %d\n"
- "[%d] %s::%d: First queued I/O - triggering daemon respawn and starting timeout\n"
- "[%d] %s::%d: Flush completed with status=%d\n"
- "[%d] %s::%d: Flush submit failed with status=%d\n"
- "[%d] %s::%d: Flush timed out after %ums\n"
- "[%d] %s::%d: Graceful shutdown completed successfully - device is now dormant\n"
- "[%d] %s::%d: Infrastructure destroyed during drain - failing request\n"
- "[%d] %s::%d: InitForIO called but device is not inactive\n"
- "[%d] %s::%d: Moved %zu pending requests to barrier queue\n"
- "[%d] %s::%d: No device initialized for drain\n"
- "[%d] %s::%d: No persistent attach support\n"
- "[%d] %s::%d: Persistent attach not supported - rejecting file stashing\n"
- "[%d] %s::%d: Pool deactivated - all buffers freed\n"
- "[%d] %s::%d: ReconnectForIO called but device is not dormant/draining\n"
- "[%d] %s::%d: Reconnection failed (status=%d) - terminating device\n"
- "[%d] %s::%d: Reconnection failed: could only allocate %zu of %u buffers\n"
- "[%d] %s::%d: Reconnection failed: newProvider->isInactive()=%d\n"
- "[%d] %s::%d: Reconnection: successfully allocated %zu new buffers\n"
- "[%d] %s::%d: Released %u vnode references during cleanup\n"
- "[%d] %s::%d: Reserved request is null or already in use - cannot perform flush\n"
- "[%d] %s::%d: STALE_COMPLETION: req[%u] - dropping completion from dying daemon (status=%d)\n"
- "[%d] %s::%d: Setting fClientPID to %u (was %u), fOldDaemonPID=%u\n"
- "[%d] %s::%d: Stopping barrier queue execution - device is dormant\n"
- "[%d] %s::%d: Successfully sent respawn message for instance ID %s with fOldDaemonPID=%u\n"
- "[%d] %s::%d: Successfully stashed file %u: ino=%llu fsid=%d:%d (total files: %u)\n"
- "[%d] %s::%d: Timeout callback fired but timeout was cancelled - ignoring\n"
- "[%d] %s::%d: Timeout expired - daemon failed to respawn within 30 seconds, ejecting device\n"
- "[%d] %s::%d: Timeout scheduled for %u ms from now\n"
- "[%d] %s::%d: Timeout scheduled for daemon reconnection (%u ms)\n"
- "[%d] %s::%d: Too many files stashed: %u (max=%u)\n"
- "[%d] %s::%d: host_get_diskimagesiod_port failed: 0x%x\n"
- "[%d] %s::%d: mach_msg_send_from_kernel_proper failed: 0x%x\n"
- "[%d] %s::%d: no extents available (fUnmapExtents=%p)\n"
- "[%d] %s::%d: vnode_getfromfd failed for file %u (fd=%lld): error=%d - disabling persistent attach\n"
- "[%d] %s::%d: vnode_ref failed for file %u: error=%d - disabling persistent attach\n"
- "bool AppleDiskImageDevice::claimDormantDevice(uint32_t)"
- "bool AppleDiskImageDevice::drainDormantIOQueue()"
- "bool AppleDiskImageDevice::flushDeviceWithTimeout(uint32_t)"
- "bool AppleDiskImageDevice::onIOClientClose(DIDeviceIOUserClient *)"
- "bool AppleDiskImageDevice::requestGracefulShutdown(bool)"
- "bool AppleDiskImageDevice::sendDaemonRespawnMessage()"
- "bool AppleDiskImageDevice::triggerDaemonRespawn()"
- "fPrepareBuffers != NULL"
- "index <= fRequestsCount"
- "size_t DIDeviceRequestPool::AddBuffersForReconnection(user_addr_t, size_t, unsigned int)"
- "static IOReturn DIDeviceIOUserClient::DrainDormantQueue(OSObject *, void *, IOExternalMethodArguments *)"
- "static IOReturn DIDeviceIOUserClient::RequestGracefulShutdown(OSObject *, void *, IOExternalMethodArguments *)"
- "static IOReturn DIDeviceIOUserClient::StashFileInformation(OSObject *, void *, IOExternalMethodArguments *)"
- "static void DIDeviceRequestPool::ReleasePoolElements(uint32_t &, ::IOLWPool<TElem> &, Mode) [TElem = DIDeviceRequest]"
- "static void DIDeviceRequestPool::ReleasePoolElements(uint32_t &, ::IOLWPool<TElem> &, Mode) [TElem = DISharedBuffer]"
- "timerSource"
- "void AppleDiskImageDevice::CompleteRequest(DIDeviceRequest *, int, bool)"
- "void AppleDiskImageDevice::cleanupDormantState()"
- "void AppleDiskImageDevice::cleanupForDaemonRespawn()"
- "void AppleDiskImageDevice::dormantIOTimeoutOccurred(OSObject *, IOTimerEventSource *)"
- "void AppleDiskImageDevice::executeBarrierQueueLocked()"
- "void DIDeviceRequestPool::ReleaseReservedRequest()"
- "workLoop"

```
