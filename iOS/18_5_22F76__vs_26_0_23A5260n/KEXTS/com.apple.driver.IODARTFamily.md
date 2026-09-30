## com.apple.driver.IODARTFamily

> `com.apple.driver.IODARTFamily`

```diff

-354.100.4.0.0
-  __TEXT.__cstring: 0x208b
+365.0.0.0.0
+  __TEXT.__cstring: 0x1efb
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x13cd8
+  __TEXT_EXEC.__text: 0x14054
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__const: 0x26a0
   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x410
-  UUID: 1488573C-5751-3258-A316-5146A8C7AE07
+  UUID: 309982B6-78AE-3E8D-9B34-AEF8A8CCDAD3
   Functions: 375
   Symbols:   0
   CStrings:  227
Functions:
~ sub_fffffff00a0ed1ac -> sub_fffffff00a4a3c6c : 144 -> 192
~ sub_fffffff00a0ed23c -> sub_fffffff00a4a3d2c : 200 -> 252
~ sub_fffffff00a0ed7b0 -> sub_fffffff00a4a42d4 : 276 -> 300
~ sub_fffffff00a0eda04 -> sub_fffffff00a4a4540 : 172 -> 196
~ __ZN6IODART29_initPersistentMappingsForSIDEjPK6OSData : 2676 -> 2812
~ sub_fffffff00a0ee674 -> sub_fffffff00a4a5250 : 152 -> 176
~ __ZN12IODARTMapper5startEP9IOService : 4680 -> 4668
~ __ZN12IODARTMapper10_setActiveEb21StateTransitionReasonb : 712 -> 700
~ sub_fffffff00a0f292c -> sub_fffffff00a4a9508 : 136 -> 156
~ sub_fffffff00a0f2a1c -> sub_fffffff00a4a960c : 688 -> 684
~ sub_fffffff00a0f2ccc -> sub_fffffff00a4a98b8 : 256 -> 252
~ sub_fffffff00a0f32d4 -> sub_fffffff00a4a9ebc : 144 -> 148
~ sub_fffffff00a0f3364 -> sub_fffffff00a4a9f50 : 512 -> 508
~ sub_fffffff00a0f3788 -> sub_fffffff00a4aa370 : 60 -> 56
~ __ZN12IODARTMapper16_iomdCacheLookupEPK18IOMemoryDescriptorP16iomdHistoryEntryyP12IODMACommand : 1584 -> 1580
~ sub_fffffff00a0f41f0 -> sub_fffffff00a4aadd0 : 424 -> 428
~ sub_fffffff00a0f4398 -> sub_fffffff00a4aaf7c : 344 -> 340
~ sub_fffffff00a0f4dd8 -> sub_fffffff00a4ab9b8 : 124 -> 120
~ sub_fffffff00a0f534c -> sub_fffffff00a4abf28 : 460 -> 444
~ sub_fffffff00a0f556c -> sub_fffffff00a4ac138 : 156 -> 168
~ sub_fffffff00a0f56cc -> sub_fffffff00a4ac2a4 : 228 -> 224
~ sub_fffffff00a0f57b0 -> sub_fffffff00a4ac384 : 324 -> 320
~ __ZN12IODARTMapper13iovmMapMemoryEP18IOMemoryDescriptoryyjPK21IODMAMapSpecificationP12IODMACommandPK16IODMAMapPageListPySA_ : 1388 -> 1384
~ __ZN12IODARTMapper21_iovmInsertDMACommandEP13IODARTVMSpaceP12IODMACommandP18IOMemoryDescriptoryyjPy : 1772 -> 1776
~ __ZN12IODARTMapper16_addBatchSegmentEmymjj : 620 -> 756
~ __ZN12IODARTMapper15iovmUnmapMemoryEP18IOMemoryDescriptorP12IODMACommandyy : 584 -> 576
~ __ZN12IODARTMapper19_iovmFreeDMACommandEP12IODMACommandjj : 780 -> 776
~ __ZN12IODARTMapper14_destroyMapperEv : 1044 -> 1040
~ __ZN12IODARTMapper11_iovmInsertEP13IODARTVMSpacejjjj : 444 -> 440
~ sub_fffffff00a0f8aec -> sub_fffffff00a4af730 : 596 -> 592
~ sub_fffffff00a0f8d40 -> sub_fffffff00a4af980 : 600 -> 596
~ sub_fffffff00a0f8f98 -> sub_fffffff00a4afbd4 : 372 -> 368
~ sub_fffffff00a0f910c -> sub_fffffff00a4afd44 : 336 -> 352
~ sub_fffffff00a0f9344 -> sub_fffffff00a4aff8c : 344 -> 352
~ sub_fffffff00a0f949c -> sub_fffffff00a4b00ec : 224 -> 240
~ __ZN12IODARTMapper13_setParameterEP21IODARTMapperParameter : 612 -> 616
~ sub_fffffff00a0f9890 -> sub_fffffff00a4b04f4 : 388 -> 396
~ __ZN12IODARTMapper20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 1608 -> 1580
~ sub_fffffff00a0fb844 -> sub_fffffff00a4b2494 : 132 -> 152
~ sub_fffffff00a0fcaac -> sub_fffffff00a4b3710 : 516 -> 756
~ sub_fffffff00a0fd7ec -> sub_fffffff00a4b4540 : 516 -> 756
~ __ZN18IODARTMapperClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 1544 -> 1540
~ sub_fffffff00a1000d8 -> sub_fffffff00a4b6f18 : 104 -> 100
CStrings:
+ "/AllocGeneric.cpp"
+ "/IODART.cpp"
+ "/IODARTClient.cpp"
+ "/IODARTMapper.cpp"
+ "/IODARTMapperClient.cpp"
+ "/IODARTPrivate.h"
+ "/IODARTVMAllocator.cpp"
+ "/IODARTVMSpace.cpp"
- "/Library/Caches/com.apple.xbs/Sources/IODARTFamily/AllocGeneric.cpp"
- "/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODART.cpp"
- "/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTClient.cpp"
- "/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTMapper.cpp"
- "/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTMapperClient.cpp"
- "/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTPrivate.h"
- "/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTVMAllocator.cpp"
- "/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTVMSpace.cpp"

```
