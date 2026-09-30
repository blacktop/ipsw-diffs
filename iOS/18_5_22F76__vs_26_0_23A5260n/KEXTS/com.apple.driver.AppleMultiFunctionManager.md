## com.apple.driver.AppleMultiFunctionManager

> `com.apple.driver.AppleMultiFunctionManager`

```diff

 71.0.0.0.0
   __TEXT.__const: 0x11
   __TEXT.__cstring: 0x2502
-  __TEXT_EXEC.__text: 0xb4c4
+  __TEXT_EXEC.__text: 0xb508
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1d8
   __DATA.__common: 0x108

   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0xed8
   __DATA_CONST.__kalloc_type: 0x300
-  UUID: 4BE6D084-5E18-3BB9-BBB5-9A1D5EBE9516
+  UUID: 5BD73F97-9998-3CF4-AC81-1CD097306458
   Functions: 261
   Symbols:   0
   CStrings:  344
Functions:
~ __ZN25AppleMultiFunctionManager16collectFaultDataEPvm : 948 -> 976
~ __ZN25AppleMultiFunctionManager5startEP9IOService : 3452 -> 3444
~ sub_fffffff0094cdbec -> sub_fffffff0097aca20 : 52 -> 76
~ __ZN25AppleMultiFunctionManager13setPowerStateEmP9IOService : 340 -> 336
~ __ZN25AppleMultiFunctionManager18setPowerStateGatedEmP9IOService : 2164 -> 2144
~ __ZN25AppleMultiFunctionManager22powerStateWillChangeToEmmP9IOService : 380 -> 376
~ __ZN25AppleMultiFunctionManager21powerStateDidChangeToEmmP9IOService : 380 -> 376
~ __ZN25AppleMultiFunctionManager20enqueueCommandLockedEjyy : 404 -> 428
~ __ZN25AppleMultiFunctionManager23flushCommandQueueLockedEj : 456 -> 480
~ __ZN25AppleMultiFunctionManager19executeCommandQueueEP22IOInterruptEventSourcei : 1684 -> 1708
~ __ZN25AppleMultiFunctionManager15pciErrorHandlerE25AMFMPCIEErrorHandlerEventP6OSData : 648 -> 644
~ __ZN25AppleMultiFunctionManager16registerInterestEPK8OSSymbolPFiPvS3_jP9IOServiceS3_mES3_S3_ : 604 -> 592

```
