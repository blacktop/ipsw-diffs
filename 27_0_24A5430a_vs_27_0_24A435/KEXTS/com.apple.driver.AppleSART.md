## com.apple.driver.AppleSART

> `com.apple.driver.AppleSART`

```diff

 25.0.0.0.0
   __TEXT.__cstring: 0xd70
-  __TEXT_EXEC.__text: 0x273c
+  __TEXT_EXEC.__text: 0x2884
   __TEXT_EXEC.__auth_stubs: 0x190
   __DATA.__data: 0xc8
   __DATA.__common: 0x88
Functions:
~ sub_fffffe00094df320 -> sub_fffffe000955f900 : 72 -> 76
~ sub_fffffe00094df370 -> sub_fffffe000955f954 : 52 -> 56
~ sub_fffffe00094df3a4 -> sub_fffffe000955f98c : 52 -> 56
~ sub_fffffe00094df3e8 -> sub_fffffe000955f9d4 : 68 -> 72
~ sub_fffffe00094df454 -> sub_fffffe000955fa44 : 72 -> 76
~ sub_fffffe00094df49c -> sub_fffffe000955fa90 : 104 -> 108
~ sub_fffffe00094df518 -> sub_fffffe000955fb10 : 88 -> 92
~ sub_fffffe00094df570 -> sub_fffffe000955fb6c : 88 -> 92
~ _panic : 876 -> 880
~ _OUTLINED_FUNCTION_1 : 140 -> 144
~ __ZN22IOCoastGuardSARTMapper13iovmMapMemoryEP18IOMemoryDescriptoryyjPK21IODMAMapSpecificationP12IODMACommandPK16IODMAMapPageListPySA_ : 636 -> 640
~ __ZN22IOCoastGuardSARTMapper15iovmUnmapMemoryEP18IOMemoryDescriptorP12IODMACommandyy : 460 -> 472
~ sub_fffffe00094dfe4c -> sub_fffffe0009560464 : 80 -> 84
~ sub_fffffe00094dfed4 -> sub_fffffe00095604f0 : 72 -> 76
~ sub_fffffe00094dff24 -> sub_fffffe0009560544 : 52 -> 56
~ sub_fffffe00094dff58 -> sub_fffffe000956057c : 52 -> 56
~ sub_fffffe00094dff9c -> sub_fffffe00095605c4 : 68 -> 72
~ sub_fffffe00094e0008 -> sub_fffffe0009560634 : 72 -> 76
~ sub_fffffe00094e0050 -> sub_fffffe0009560680 : 104 -> 108
~ sub_fffffe00094e00cc -> sub_fffffe0009560700 : 88 -> 92
~ sub_fffffe00094e0124 -> sub_fffffe000956075c : 88 -> 92
~ __ZN16AppleSARTMarconi5startEP9IOService : 992 -> 996
~ _OUTLINED_FUNCTION_1_0 : 56 -> 60
~ sub_fffffe00094e0594 -> sub_fffffe0009560bd8 : 76 -> 80
~ sub_fffffe00094e05e8 -> sub_fffffe0009560c30 : 80 -> 84
~ sub_fffffe00094e06a4 -> sub_fffffe0009560cf0 : 72 -> 76
~ sub_fffffe00094e06f4 -> sub_fffffe0009560d44 : 60 -> 64
~ sub_fffffe00094e0730 -> sub_fffffe0009560d84 : 60 -> 64
~ sub_fffffe00094e077c -> sub_fffffe0009560dd4 : 68 -> 72
~ sub_fffffe00094e07e8 -> sub_fffffe0009560e44 : 72 -> 76
~ sub_fffffe00094e0830 -> sub_fffffe0009560e90 : 112 -> 116
~ sub_fffffe00094e08b4 -> sub_fffffe0009560f18 : 96 -> 100
~ sub_fffffe00094e0914 -> sub_fffffe0009560f7c : 96 -> 100
~ _OUTLINED_FUNCTION_0_1 : 308 -> 312
~ __ZN12IOSARTMapper10_setActiveEb : 352 -> 356
~ sub_fffffe00094e0c84 -> sub_fffffe00095612f8 : 120 -> 124
~ __ZN12IOSARTMapper10_addRegionEmjb : 332 -> 336
~ __ZN12IOSARTMapper13_removeRegionEi : 220 -> 224
~ sub_fffffe00094e0f44 -> sub_fffffe00095615c4 : 388 -> 392
~ __ZN12IOSARTMapper15iovmUnmapMemoryEP18IOMemoryDescriptorP12IODMACommandyy : 232 -> 236
~ sub_fffffe00094e11b0 -> sub_fffffe0009561838 : 132 -> 136
~ sub_fffffe00094e1248 -> sub_fffffe00095618d4 : 80 -> 84
~ _OUTLINED_FUNCTION_0 : 52 -> 56
~ __ZN22IOCoastGuardSARTMapper5startEP9IOService.cold.2 : 52 -> 56
~ __ZN12IOSARTMapper5startEP9IOService.cold.2 : 52 -> 56
~ __ZN12IOSARTMapper5startEP9IOService.cold.3 : 52 -> 56
~ __ZN22IOCoastGuardSARTMapper20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_.cold.1 : 52 -> 56
~ __ZN22IOCoastGuardSARTMapper13iovmMapMemoryEP18IOMemoryDescriptoryyjPK21IODMAMapSpecificationP12IODMACommandPK16IODMAMapPageListPySA_.cold.1 : 52 -> 56
~ __ZN22IOCoastGuardSARTMapper15iovmUnmapMemoryEP18IOMemoryDescriptorP12IODMACommandyy.cold.1 : 52 -> 56
~ __ZN16AppleSARTMarconi5startEP9IOService.cold.1 : 40 -> 44
~ __ZN16AppleSARTMarconi5startEP9IOService.cold.2 : 40 -> 44
~ __ZN16AppleSARTMarconi5startEP9IOService.cold.3 : 40 -> 44
~ __ZN16AppleSARTMarconi5startEP9IOService.cold.4 : 40 -> 44
~ __ZN16AppleSARTMarconi5startEP9IOService.cold.5 : 40 -> 44
~ __ZN16AppleSARTMarconi5startEP9IOService.cold.6 : 40 -> 44
~ __ZN16AppleSARTMarconi5startEP9IOService.cold.7 : 40 -> 44
~ sub_fffffe00094e1620 -> sub_fffffe0009561ce8 : 40 -> 44
~ __ZN16AppleSARTMarconi5startEP9IOService.cold.9 : 40 -> 44
~ __ZN16AppleSARTMarconi15_makeRegionBaseEy.cold.1 : 52 -> 56
~ __ZN16AppleSARTMarconi15_makeRegionBaseEy.cold.2 : 52 -> 56
~ __ZN16AppleSARTMarconi11_makeRegionEyb.cold.1 : 52 -> 56
~ __ZN16AppleSARTMarconi11_makeRegionEyb.cold.2 : 52 -> 56
~ __ZN9os_detail21panic_trapping_policy4trapEPKc : 48 -> 52
~ __ZN12IOSARTMapper5startEP9IOService.cold.1 : 52 -> 56
~ sub_fffffe00094e17a4 -> sub_fffffe0009561e8c : 52 -> 56
~ sub_fffffe00094e17d8 -> sub_fffffe0009561ec4 : 52 -> 56
~ __ZN12IOSARTMapper10_setActiveEb.cold.1 : 52 -> 56
~ __ZN12IOSARTMapper10_setActiveEb.cold.2 : 16 -> 20
~ __ZN9os_detail21panic_trapping_policy4trapEPKc : 16 -> 20
~ __ZN12IOSARTMapper10_addRegionEmjb.cold.1 : 52 -> 56
~ __ZN12IOSARTMapper10_addRegionEmjb.cold.2 : 52 -> 56
~ sub_fffffe00094e18c8 -> sub_fffffe0009561fcc : 52 -> 56
~ sub_fffffe00094e18fc -> sub_fffffe0009562004 : 52 -> 56
~ __ZN12IOSARTMapper10_addRegionEmjb.cold.6 : 16 -> 20
~ __ZN12IOSARTMapper13_removeRegionEi.cold.6 : 24 -> 28
~ _OUTLINED_FUNCTION_3 : 52 -> 56
~ sub_fffffe00094e198c -> sub_fffffe00095620a4 : 52 -> 56
~ __ZN12IOSARTMapper15iovmUnmapMemoryEP18IOMemoryDescriptorP12IODMACommandyy.cold.1 : 52 -> 56
~ __ZN12IOSARTMapper10iovmInsertEjyyyy.cold.2 : 52 -> 56
~ sub_fffffe00094e1a28 -> sub_fffffe000956214c : 52 -> 56
```
