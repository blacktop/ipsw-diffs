## com.apple.iokit.IOBiometricFamily

> `com.apple.iokit.IOBiometricFamily`

```diff

-577.0.0.0.0
+578.40.6.0.0
   __TEXT.__os_log: 0x125b
-  __TEXT.__cstring: 0x1297
+  __TEXT.__cstring: 0x129a
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0xf4d0
+  __TEXT_EXEC.__text: 0xf278
   __TEXT_EXEC.__auth_stubs: 0x400
   __DATA.__data: 0xcc
-  __DATA.__common: 0x3c0
+  __DATA.__common: 0x330
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x3200
Functions:
~ __ZN15MCDataMessaging15initWithServiceEP9IOService : 232 -> 216
~ __ZN15MCDataMessagingD2Ev : 216 -> 200
~ sub_fffffe000a029cb0 -> sub_fffffe000a1d0c10 : 216 -> 200
~ __ZN15MCDataMessaging14messageClientsEjjPvmS0_y : 804 -> 788
~ __ZN15MCDataMessaging11enqueueDataEP12MCDataStructm : 400 -> 376
~ __ZN15MCDataMessaging15pullMessageDataEyP18IOMemoryDescriptorPj : 656 -> 592
~ __ZN10IOBioUtils16writeBytesToIOMDEP18IOMemoryDescriptorPKvmPj : 588 -> 568
~ __ZN20IOBioSEPSharedBuffer4initE11OSSharedPtrI9IOBioPoolEP20kern_allocation_namemS0_I23AppleSEPGenericTransferE : 764 -> 748
~ __ZN20IOBioSEPSharedBuffer4freeEv : 400 -> 380
~ __ZN27IOBioSEPSharedBufferFactory4initEP20kern_allocation_namem11OSSharedPtrI23AppleSEPGenericTransferE : 356 -> 340
~ __ZN30IOBioSharedMemoryTransferQueue13enqueueObjectE11OSSharedPtrI26IOBioShareableMemoryObjectEb : 400 -> 404
~ __ZN30IOBioSharedMemoryTransferQueue28dequeueShareableMemoryObjectEb : 452 -> 408
~ __ZN30IOBioSharedMemoryTransferQueue14releaseObjectsEjj : 296 -> 280
~ ____ZN30IOBioSharedMemoryTransferQueue14releaseObjectsEjj_block_invoke : 376 -> 356
~ ____ZN30IOBioSharedMemoryTransferQueue17releaseAllObjectsEj_block_invoke : 312 -> 292
~ __ZN30IOBioSharedMemoryTransferQueue10osLogQueueEj : 384 -> 364
~ __ZN30IOBioSharedMemoryTransferQueue11osLogObjectEP26IOBioShareableMemoryObjectj : 112 -> 92
~ __ZN15IOBioArrayQueue4initEPKcjbb : 428 -> 412
~ __ZN15IOBioArrayQueue4freeEv : 224 -> 208
~ __ZN15IOBioArrayQueue13enqueueObjectE11OSSharedPtrI8OSObjectEb : 768 -> 748
~ __ZN15IOBioArrayQueue10osLogQueueEv : 364 -> 336
~ __ZN15IOBioArrayQueue14releaseObjectsEj : 236 -> 220
~ __ZN15IOBioArrayQueue19removeObjectAtIndexEjb : 452 -> 424
~ __ZN15IOBioArrayQueue17releaseAllObjectsEv : 216 -> 196
~ __ZN15IOBioArrayQueue22releaseMatchingObjectsEU13block_pointerFbP8OSObjectPbEb : 616 -> 592
~ __ZN15IOBioArrayQueue11osLogObjectEP8OSObject : 180 -> 160
~ __ZN21IOBiometricUserClient4freeEv : 336 -> 312
~ __ZN21IOBiometricUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 700 -> 672
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.40.6~55, %s file: %s, line: %d\n"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-577~9296, %s file: %s, line: %d\n"
```
