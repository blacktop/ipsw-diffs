## com.apple.driver.IODARTFamily

> `com.apple.driver.IODARTFamily`

```diff

-365.100.7.0.0
+365.120.2.0.0
   __TEXT.__cstring: 0x1efb
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x1345c
+  __TEXT_EXEC.__text: 0x13af0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__const: 0x26d8
   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x410
-  UUID: 1456DA8D-71AA-3E3E-B164-68524EA0F4F6
+  UUID: 2061718B-4FE4-3EE3-B580-3F4E05F94EEF
   Functions: 385
   Symbols:   0
   CStrings:  227
Functions:
~ sub_fffffe0009c0cb40 -> sub_fffffe0009c11490 : 136 -> 196
~ sub_fffffe0009c0d424 -> __ZNK6IODART14_dumpPageTableEPKyjmj : 196 -> 468
~ __ZN6IODART29_initPersistentMappingsForSIDEjPK6OSData -> sub_fffffe0009c11f84 : 2596 -> 196
~ sub_fffffe0009c0df0c -> __ZN6IODART29_initPersistentMappingsForSIDEjPK6OSData : 56 -> 2596
~ __ZN12IODARTMapper21_iovmInsertDMACommandEP13IODARTVMSpaceP12IODMACommandP18IOMemoryDescriptoryyjPy -> sub_fffffe0009c12a6c : 224 -> 56
~ sub_fffffe0009c0e024 -> sub_fffffe0009c12aa4 : 56 -> 224
~ sub_fffffe0009c0e05c -> sub_fffffe0009c12b84 : 168 -> 56
~ __ZNK6IODART14_dumpPageTableEPKyjmj -> sub_fffffe0009c12bbc : 468 -> 168
~ sub_fffffe0009c0f1bc -> sub_fffffe0009c13b48 : 136 -> 196
~ __ZN12IODARTMapper5startEP9IOService : 4312 -> 4308
~ __ZN12IODARTMapper13iovmMapMemoryEP18IOMemoryDescriptoryyjPK21IODMAMapSpecificationP12IODMACommandPK16IODMAMapPageListPySA_ : 1324 -> 1508
~ __ZN12IODARTMapper15iovmUnmapMemoryEP18IOMemoryDescriptorP12IODMACommandyy : 560 -> 816
~ sub_fffffe0009c186b4 -> sub_fffffe0009c1d230 : 352 -> 360
~ __ZN12IODARTMapper13_setParameterEP21IODARTMapperParameter : 608 -> 604
~ __Z15NewIODARTMapperP9IOServiceS0_jPKcP12OSDictionary : 2808 -> 3544
~ sub_fffffe0009c1a79c -> sub_fffffe0009c1f5fc : 572 -> 600
~ sub_fffffe0009c1a9d8 -> sub_fffffe0009c1f854 : 288 -> 296
~ sub_fffffe0009c1aaf8 -> sub_fffffe0009c1f97c : 428 -> 436
~ sub_fffffe0009c1ad3c -> sub_fffffe0009c1fbc8 : 392 -> 400
~ __ZN24IODARTVMAllocatorGeneric4initEP8IOMapperj : 412 -> 420
~ sub_fffffe0009c1b5a8 -> sub_fffffe0009c20444 : 112 -> 120
~ __ZN24IODARTVMAllocatorGeneric4initEP8IOMapperj -> sub_fffffe0009c204bc : 660 -> 704
~ sub_fffffe0009c1b8ac -> __ZN24IODARTVMAllocatorGeneric4initEP8IOMapperj : 344 -> 396
~ __ZN24IODARTVMAllocatorGeneric6vmFreeEP13IODARTVMSpace -> __ZN24IODARTVMAllocatorGeneric6vmFreeEjj : 376 -> 388
~ sub_fffffe0009c1bb7c -> __ZN24IODARTVMAllocatorGeneric6vmFreeEP13IODARTVMSpace : 324 -> 332
~ sub_fffffe0009c1bcc0 -> sub_fffffe0009c20bd8 : 216 -> 224
~ sub_fffffe0009c1bd98 -> sub_fffffe0009c20cb8 : 708 -> 716
~ sub_fffffe0009c1c3d0 -> sub_fffffe0009c212f8 : 176 -> 184
~ __ZN25IODARTPIOAllocatorGeneric7vmAllocEjjjP12IODMACommandjjb : 1288 -> 1360
~ sub_fffffe0009c1c9f4 -> sub_fffffe0009c2196c : 152 -> 160
~ sub_fffffe0009c1ca8c -> sub_fffffe0009c21a0c : 116 -> 124
~ sub_fffffe0009c1cb00 -> sub_fffffe0009c21a88 : 708 -> 716
~ sub_fffffe0009c1d22c -> sub_fffffe0009c221bc : 364 -> 372
~ sub_fffffe0009c1d398 -> sub_fffffe0009c22330 : 152 -> 144
~ __ZN18IODARTMapperClient5startEP9IOService.cold.2 -> __ZN18IODARTMapperClient5startEP9IOService.cold.1 : 380 -> 388
~ __ZN18IODARTMapperClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 1484 -> 1528
~ sub_fffffe0009c1de44 -> sub_fffffe0009c22e08 : 264 -> 276
~ sub_fffffe0009c1eae4 -> sub_fffffe0009c23ab4 : 240 -> 256
~ sub_fffffe0009c1ebd4 -> sub_fffffe0009c23bb4 : 284 -> 288

```
