## com.apple.iokit.IOBiometricFamily

> `com.apple.iokit.IOBiometricFamily`

```diff

-577.0.0.0.0
+578.40.6.0.0
   __TEXT.__os_log: 0x125b
-  __TEXT.__cstring: 0x1250
+  __TEXT.__cstring: 0x1253
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0xf778
+  __TEXT_EXEC.__text: 0xf524
   __TEXT_EXEC.__auth_stubs: 0x400
   __DATA.__data: 0xcc
-  __DATA.__common: 0x3c0
+  __DATA.__common: 0x330
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x5700

   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x70
   Functions: 507
-  Symbols:   1272
+  Symbols:   1256
   CStrings:  276
 
Symbols:
+ __ZL11OSLogHandle
+ __ZL16OSLogTraceHandle
+ __ZZN15MCDataMessaging11enqueueDataEP12MCDataStructmE20kalloc_type_view_235
+ __ZZN15MCDataMessaging11enqueueDataEP12MCDataStructmE20kalloc_type_view_240
+ __ZZN15MCDataMessaging15pullMessageDataEyP18IOMemoryDescriptorPjE20kalloc_type_view_195
+ __ZZN15MCDataMessagingD1EvE19kalloc_type_view_65
- __ZZN15MCDataMessaging11enqueueDataEP12MCDataStructmE20kalloc_type_view_236
- __ZZN15MCDataMessaging11enqueueDataEP12MCDataStructmE20kalloc_type_view_241
- __ZZN15MCDataMessaging15pullMessageDataEyP18IOMemoryDescriptorPjE20kalloc_type_view_196
- __ZZN15MCDataMessagingD1EvE19kalloc_type_view_66
- ___osLogTrace_IOBioArrayQueue
- ___osLogTrace_IOBioSEPSharedBufferFactory
- ___osLogTrace_IOBioSharedMemoryTransferQueue
- ___osLogTrace_IOBiometricService
- ___osLogTrace_IOBiometricUserClient
- ___osLogTrace_IOBiometricUtilities
- ___osLogTrace_IOSEPBiometricService
- ___osLogTrace_IOSEPSharedBuffer
- ___osLogTrace_MCDataMessaging
- ___osLog_IOBioArrayQueue
- ___osLog_IOBioSEPSharedBufferFactory
- ___osLog_IOBioSharedMemoryTransferQueue
- ___osLog_IOBiometricService
- ___osLog_IOBiometricUserClient
- ___osLog_IOBiometricUtilities
- ___osLog_IOSEPBiometricService
- ___osLog_IOSEPSharedBuffer
- ___osLog_MCDataMessaging
Functions:
~ __ZN15MCDataMessaging15initWithServiceEP9IOService : 236 -> 220
~ __ZN15MCDataMessagingD2Ev : 216 -> 200
~ __ZN15MCDataMessagingD1Ev : 216 -> 200
~ __ZN15MCDataMessaging14messageClientsEjjPvmS0_y : 804 -> 788
~ __ZN15MCDataMessaging11enqueueDataEP12MCDataStructm : 400 -> 376
~ __ZN15MCDataMessaging15pullMessageDataEyP18IOMemoryDescriptorPj : 672 -> 608
~ __ZN10IOBioUtils16writeBytesToIOMDEP18IOMemoryDescriptorPKvmPj : 608 -> 588
~ __ZN20IOBioSEPSharedBuffer4initE11OSSharedPtrI9IOBioPoolEP20kern_allocation_namemS0_I23AppleSEPGenericTransferE : 776 -> 760
~ __ZN20IOBioSEPSharedBuffer4freeEv : 400 -> 380
~ __ZN27IOBioSEPSharedBufferFactory4initEP20kern_allocation_namem11OSSharedPtrI23AppleSEPGenericTransferE : 360 -> 344
~ __ZN30IOBioSharedMemoryTransferQueue13enqueueObjectE11OSSharedPtrI26IOBioShareableMemoryObjectEb : 412 -> 416
~ __ZN30IOBioSharedMemoryTransferQueue28dequeueShareableMemoryObjectEb : 464 -> 420
~ __ZN30IOBioSharedMemoryTransferQueue14releaseObjectsEjj : 296 -> 280
~ ____ZN30IOBioSharedMemoryTransferQueue14releaseObjectsEjj_block_invoke : 392 -> 372
~ ____ZN30IOBioSharedMemoryTransferQueue17releaseAllObjectsEj_block_invoke : 328 -> 308
~ __ZN30IOBioSharedMemoryTransferQueue10osLogQueueEj : 396 -> 376
~ __ZN30IOBioSharedMemoryTransferQueue11osLogObjectEP26IOBioShareableMemoryObjectj : 112 -> 92
~ __ZN15IOBioArrayQueue4initEPKcjbb : 440 -> 424
~ __ZN15IOBioArrayQueue4freeEv : 224 -> 208
~ __ZN15IOBioArrayQueue13enqueueObjectE11OSSharedPtrI8OSObjectEb : 796 -> 776
~ __ZN15IOBioArrayQueue10osLogQueueEv : 396 -> 368
~ __ZN15IOBioArrayQueue14releaseObjectsEj : 244 -> 228
~ __ZN15IOBioArrayQueue19removeObjectAtIndexEjb : 460 -> 432
~ __ZN15IOBioArrayQueue17releaseAllObjectsEv : 232 -> 212
~ __ZN15IOBioArrayQueue22releaseMatchingObjectsEU13block_pointerFbP8OSObjectPbEb : 628 -> 608
~ __ZN15IOBioArrayQueue11osLogObjectEP8OSObject : 180 -> 160
~ __ZN21IOBiometricUserClient4freeEv : 336 -> 312
~ __ZN21IOBiometricUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 700 -> 672
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.40.6~52, %s file: %s, line: %d\n"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-577~9963, %s file: %s, line: %d\n"
```
