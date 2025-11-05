## com.apple.driver.AppleSmartIO2

> `com.apple.driver.AppleSmartIO2`

```diff

 140.0.0.0.0
   __TEXT.__cstring: 0x474b
   __TEXT.__const: 0x60
-  __TEXT_EXEC.__text: 0xcc34
+  __TEXT_EXEC.__text: 0xced8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7f8
   __DATA.__common: 0x1a0

   __DATA_CONST.__const: 0x3950
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 592140C5-8DBF-3241-B1F9-8618A6154A14
+  UUID: 1D0222F1-563A-34C7-A5D2-43335D3CE884
   Functions: 471
   Symbols:   975
   CStrings:  379
Functions:
~ __ZN12AppleSmartIO5startEP9IOService : 1704 -> 1724
~ __ZN12AppleSmartIO15_messageHandlerEPvS0_ : 132 -> 136
~ __ZN12AppleSmartIO18_incomingMsgActionEy : 132 -> 136
~ __ZN12AppleSmartIO20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 428 -> 452
~ __ZN12AppleSmartIO17endpointForHandleEP8OSObjectPFvS1_PvS2_EjP16IODMAEventSource : 184 -> 188
~ __ZN22AppleSmartIOUserClient5startEP9IOService : 588 -> 592
~ __ZN22AppleSmartIOUserClient11clientCloseEv : 124 -> 128
~ __ZN22AppleSmartIOUserClient21_extQueryPerfDispatchEP8OSObjectPvP25IOExternalMethodArguments : 156 -> 164
~ __ZN22AppleSmartIOUserClient14externalMethodEjP31IOExternalMethodArgumentsOpaque : 140 -> 144
~ __ZN19AppleSmartIOCommand4freeEv : 28 -> 32
~ __ZN23AppleSmartIOCommandPool4freeEv : 112 -> 116
~ __ZN23AppleSmartIOCommandPool9_assignIDEP19AppleSmartIOCommand : 76 -> 80
~ __ZN23AppleSmartIOCommandPool18gatedReturnCommandEP9IOCommand : 164 -> 160
~ __ZN20AppleSmartIOEndpoint15initWithOptionsEP12AppleSmartIOP8OSObjectj : 196 -> 192
~ __ZN20AppleSmartIOEndpoint11sendMessageEPvS0_b : 188 -> 212
~ __ZN20AppleSmartIOEndpoint14deliverMessageEPv : 272 -> 296
~ __ZN20AppleSmartIOEndpoint19allocateCommandPoolEP10IOWorkLoopj : 356 -> 344
~ __ZN20AppleSmartIOEndpoint9ep_enableEv : 56 -> 60
~ __ZN20AppleSmartIOEndpoint10ep_disableEv : 48 -> 52
~ __ZN19AppleSmartIOControl11_initForSIOEP12AppleSmartIO : 176 -> 168
~ __ZN19AppleSmartIOControl14setupMapRangesEv : 836 -> 876
~ __ZN19AppleSmartIOControl12sendTunablesEv : 1016 -> 1048
~ __ZN19AppleSmartIOControl31populateShimPowerGatePropertiesEv : 556 -> 560
~ __ZN19AppleSmartIOControl12setupDevicesEv : 728 -> 732
~ __ZN19AppleSmartIOControl16sendSIORegistersEv : 912 -> 908
~ __ZN25AppleSmartIODMAController17_getConfigurationEP9IOServicej : 328 -> 348
~ __ZN25AppleSmartIODMAController20_initDMAChannelGatedEPK21AppleSmartIODMAConfigP16IODMAEventSourcePj : 408 -> 416
~ __ZN25AppleSmartIODMAController12setDMAConfigEjP9IOServicej : 212 -> 216
~ __ZN25AppleSmartIODMAController15startDMACommandEjP12IODMACommandjyy : 116 -> 120
~ __ZN15AppleSmartIODMA15startDMACommandEP12IODMACommandjyy : 468 -> 488
~ __ZN25AppleSmartIODMAController14stopDMACommandEjby : 112 -> 116
~ __ZN25AppleSmartIODMAController15queryDMACommandEjPP12IODMACommandPyb : 192 -> 196
~ __ZN25AppleSmartIODMAController12getFIFODepthEjj : 152 -> 156
~ __ZN25AppleSmartIODMAController12setFIFODepthEjy : 152 -> 156
~ __ZN25AppleSmartIODMAController14validFIFODepthEjyj : 156 -> 160
~ __ZN25AppleSmartIODMAController12setFrameSizeEjh : 152 -> 156
~ __ZN25AppleSmartIODMAController15bufferForHandleEj : 44 -> 64
~ __ZN25AppleSmartIODMAController16segmentForHandleEj : 48 -> 68
~ __ZN15AppleSmartIODMA16_initWithOptionsEP12AppleSmartIOP25AppleSmartIODMAControllerP16IODMAEventSourcej : 528 -> 560
~ __ZN15AppleSmartIODMA16_startDMACommandEP12IODMACommandPyS2_ : 1424 -> 1492
~ __ZN15AppleSmartIODMA9_queryDMAEPP12IODMACommandPyPb : 544 -> 584
~ __ZN15AppleSmartIODMA8_stopDMAEPbPv : 816 -> 836
~ __ZN15AppleSmartIODMA13_configureDMAEv : 572 -> 588
~ __ZN15AppleSmartIODMA16_segmentFunctionEP12IODMACommandNS0_9Segment64EPvj : 52 -> 76
~ __ZN15AppleSmartIODMA14_notifyCommandEP19AppleSmartIOCommand : 280 -> 320
~ __ZN15AppleSmartIODMA13_asyncMessageEPvS0_ : 372 -> 388
~ __ZN15AppleSmartIODMA16_completeCommandEP19AppleSmartIOCommand : 656 -> 752
~ __ZN15AppleSmartIODMA19handleShimFIFOPowerEb : 252 -> 264
~ _ZN12AppleSmartIO5startEP9IOService.cold.3 : 76 -> 44
~ _ZN12AppleSmartIO5startEP9IOService.cold.4 : 76 -> 56
~ _ZN12AppleSmartIO5startEP9IOService.cold.8 : 56 -> 76
~ _ZN12AppleSmartIO5startEP9IOService.cold.9 : 44 -> 76
~ _ZN12AppleSmartIO20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_.cold.1 : 76 -> 60
~ _ZN12AppleSmartIO20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_.cold.2 : 76 -> 60
~ _ZN12AppleSmartIO20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_.cold.3 : 60 -> 76
~ _ZN12AppleSmartIO20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_.cold.4 : 60 -> 76
~ _ZN15AppleSmartIODMA16_initWithOptionsEP12AppleSmartIOP25AppleSmartIODMAControllerP16IODMAEventSourcej.cold.1 : 84 -> 76
~ _ZN15AppleSmartIODMA16_initWithOptionsEP12AppleSmartIOP25AppleSmartIODMAControllerP16IODMAEventSourcej.cold.4 : 76 -> 84
~ _ZN15AppleSmartIODMA8_stopDMAEPbPv.cold.3 : 84 -> 76
~ _ZN15AppleSmartIODMA8_stopDMAEPbPv.cold.5 : 76 -> 84
~ _ZN15AppleSmartIODMA13_asyncMessageEPvS0_.cold.1 : 88 -> 84
~ _ZN15AppleSmartIODMA13_asyncMessageEPvS0_.cold.2 : 84 -> 76
~ _ZN15AppleSmartIODMA13_asyncMessageEPvS0_.cold.4 : 76 -> 84
~ _ZN15AppleSmartIODMA13_asyncMessageEPvS0_.cold.5 : 84 -> 88
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIO.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIO.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOControl.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIODMA.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOEndpoint.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOPerf.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOUserClient.cpp"
+ "21:12:29"
+ "Mar 19 2025"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIO.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIO.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOCommand.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOControl.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIODMA.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOEndpoint.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOPerf.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOUserClient.cpp"
- "20:13:48"
- "Jan  2 2025"

```
