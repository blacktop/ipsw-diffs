## com.apple.driver.AppleThunderboltIP

> `com.apple.driver.AppleThunderboltIP`

```diff

-1030.0.0.0.0
+1032.0.0.0.0
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x1e263
   __TEXT.__os_log: 0xe017
-  __TEXT_EXEC.__text: 0x3839c
+  __TEXT_EXEC.__text: 0x36d10
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x360
   __DATA.__common: 0x158

   __DATA_CONST.__const: 0x28e0
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 62DD3D29-3A6F-3506-A357-26E481F4A1BE
+  UUID: 720487C6-3492-319D-9652-025068004170
   Functions: 362
   Symbols:   0
   CStrings:  2019
Functions:
~ __ZN25AppleThunderboltIPService5startEP9IOService : 3368 -> 3152
~ __ZN25AppleThunderboltIPService11createPortsEv : 2508 -> 2400
~ __ZN25AppleThunderboltIPService24protocolListenerCallbackEPvP27IOThunderboltReceiveCommand : 2112 -> 2028
~ __ZN25AppleThunderboltIPService16publishIPServiceEb : 1420 -> 1396
~ __ZN25AppleThunderboltIPService8finalizeEj : 1972 -> 1884
~ __ZN25AppleThunderboltIPService19handleXDomainPacketEP28IOThunderboltDispatchContext : 2096 -> 2064
~ __ZN25AppleThunderboltIPService27getIPPortForThunderboltPortEP17IOThunderboltPort : 3768 -> 3636
~ _kprintHexDump : 496 -> 492
~ __ZN29AppleThunderboltIPTransmitter5startEP9IOService : 4628 -> 4404
~ __ZN29AppleThunderboltIPTransmitter8setStateEj : 624 -> 572
~ __ZN29AppleThunderboltIPTransmitter29ipServiceNotificationCallbackEPvP9IOService : 1264 -> 1212
~ __ZN29AppleThunderboltIPTransmitter20setupPowerManagementEP9IOService : 484 -> 468
~ __ZN29AppleThunderboltIPTransmitter8finalizeEj : 5072 -> 4920
~ __ZN29AppleThunderboltIPTransmitter21prepareForTerminationEv : 2064 -> 2032
~ __ZN29AppleThunderboltIPTransmitter8setTimerEj : 1832 -> 1780
~ __ZN29AppleThunderboltIPTransmitter4freeEv : 364 -> 352
~ __ZN29AppleThunderboltIPTransmitter13setPowerStateEmP9IOService : 3804 -> 3788
~ __ZN29AppleThunderboltIPTransmitter25dispatchLogoutWithRequestEb : 1768 -> 1736
~ __ZN29AppleThunderboltIPTransmitter24dispatchLoginWithRequestEb : 1840 -> 1808
~ __ZN29AppleThunderboltIPTransmitter28processIPServiceNotificationEP28IOThunderboltDispatchContext : 3860 -> 3756
~ __ZN29AppleThunderboltIPTransmitter12createTxPathEv : 3400 -> 3136
~ __ZN29AppleThunderboltIPTransmitter12newTxCommandEb : 644 -> 572
~ __ZN29AppleThunderboltIPTransmitter15returnTxCommandEP33AppleThunderboltIPTransmitCommandb : 484 -> 468
~ __ZN29AppleThunderboltIPTransmitter13destroyTxPathEv : 2760 -> 2640
~ __ZN29AppleThunderboltIPTransmitter15configureTxPathEv : 3000 -> 2944
~ sub_fffffe0009e43ab4 -> sub_fffffe0009569d7c : 160 -> 144
~ sub_fffffe0009e43b54 -> sub_fffffe0009569e0c : 252 -> 244
~ __ZN29AppleThunderboltIPTransmitter17txCommandCallbackEPviP28IOThunderboltTransmitCommand : 1300 -> 1272
~ __ZN29AppleThunderboltIPTransmitter20timerCommandCallbackEPviP25IOThunderboltTimerCommand : 2636 -> 2584
~ __ZN29AppleThunderboltIPTransmitter14processTimeoutEP28IOThunderboltDispatchContext : 6988 -> 6936
~ __ZN29AppleThunderboltIPTransmitter34dispatchProcessLoginResponsePacketEP24IOBufferMemoryDescriptor : 1620 -> 1568
~ __ZN29AppleThunderboltIPTransmitter26processLoginResponsePacketEP28IOThunderboltDispatchContext : 4684 -> 4640
~ __ZN29AppleThunderboltIPTransmitter35dispatchProcessLogoutResponsePacketEP24IOBufferMemoryDescriptor : 1620 -> 1568
~ __ZN29AppleThunderboltIPTransmitter27processLogoutResponsePacketEP28IOThunderboltDispatchContext : 2332 -> 2292
~ __ZN29AppleThunderboltIPTransmitter5loginEb : 3396 -> 3388
~ __ZN29AppleThunderboltIPTransmitter12outputPacketEP6__mbufPv : 2856 -> 2820
~ sub_fffffe0009e4c840 -> sub_fffffe0009572984 : 240 -> 216
~ sub_fffffe0009e4c930 -> sub_fffffe0009572a5c : 112 -> 104
~ sub_fffffe0009e4c9a0 -> sub_fffffe0009572ac4 : 284 -> 276
~ __ZN29AppleThunderboltIPTransmitter13getTxE2EHopIDEPt : 944 -> 936
~ sub_fffffe0009e4d238 -> sub_fffffe000957334c : 164 -> 148
~ __ZN33AppleThunderboltIPTransmitCommand18initWithControllerEP23IOThunderboltControllery : 396 -> 360
~ sub_fffffe0009e4d468 -> sub_fffffe0009573548 : 256 -> 232
~ __ZN33AppleThunderboltIPTransmitCommand38initWithControllerAndQueueAllocateDescEP23IOThunderboltControllerP26IOThunderboltTransmitQueuey : 592 -> 560
~ __ZN33AppleThunderboltIPTransmitCommand27addMemoryDescriptorMultipleEPP18IOMemoryDescriptorjy : 540 -> 488
~ sub_fffffe0009e4db38 -> sub_fffffe0009573bac : 172 -> 152
~ __ZN33AppleThunderboltIPTransmitCommand11BuildPacketEjttjP6__mbufj : 612 -> 560
~ __ZN33AppleThunderboltIPTransmitCommand18BuildHeadersPacketEP40AppleThunderboltIPPacketHeaderAggregatedj : 556 -> 512
~ sub_fffffe0009e4e074 -> sub_fffffe0009574074 : 224 -> 180
~ sub_fffffe0009e4e464 -> sub_fffffe0009574438 : 180 -> 156
~ __ZN32AppleThunderboltIPReceiveCommand18initWithControllerEP23IOThunderboltController : 584 -> 548
~ sub_fffffe0009e4e760 -> sub_fffffe00095746f8 : 172 -> 156
~ __ZN32AppleThunderboltIPReceiveCommand26initWithControllerAndQueueEP23IOThunderboltControllerP25IOThunderboltReceiveQueueP18IOMemoryDescriptory : 924 -> 884
~ sub_fffffe0009e4eba8 -> sub_fffffe0009574b08 : 156 -> 136
~ __ZN32AppleThunderboltIPReceiveCommand17ExtractFromPacketEPjPtS1_S0_PPh : 660 -> 648
~ __ZN32AppleThunderboltIPReceiveCommand27ExtractFromPacketAggregatedEPPhbP40AppleThunderboltIPPacketHeaderAggregatedPj : 860 -> 828
~ sub_fffffe0009e4f544 -> sub_fffffe0009575464 : 212 -> 196
~ __ZN32AppleThunderboltIPControlCommand14initWithParamsEP23IOThunderboltController8EFI_GUIDS2_P24IOThunderboltXDomainLink : 808 -> 760
~ sub_fffffe0009e4f94c -> sub_fffffe000957582c : 180 -> 160
~ __ZN32AppleThunderboltIPControlCommand16BuildLoginPacketEjjb : 504 -> 488
~ __ZN32AppleThunderboltIPControlCommand29BuildThunderboltIPLoginPacketEP24IOBufferMemoryDescriptor8EFI_GUIDS2_jjb : 444 -> 428
~ __ZN32AppleThunderboltIPControlCommand24BuildLoginResponsePacketEjjPhj : 480 -> 464
~ __ZN32AppleThunderboltIPControlCommand37BuildThunderboltIPLoginResponsePacketEP24IOBufferMemoryDescriptor8EFI_GUIDS2_jjPhj : 464 -> 456
~ __ZN32AppleThunderboltIPControlCommand17BuildLogoutPacketEj : 476 -> 464
~ __ZN32AppleThunderboltIPControlCommand25BuildLogoutResponsePacketEjj : 484 -> 468
~ __ZN32AppleThunderboltIPControlCommand38BuildThunderboltIPLogoutResponsePacketEP24IOBufferMemoryDescriptor8EFI_GUIDS2_jj : 404 -> 396
~ __ZN32AppleThunderboltIPControlCommand9LogPacketEv : 316 -> 272
~ sub_fffffe0009e50944 -> sub_fffffe0009576788 : 88 -> 80
~ sub_fffffe0009e5099c -> sub_fffffe00095767d8 : 88 -> 80
~ __ZN32AppleThunderboltIPControlCommand32BuildThunderboltIPProtocolHeaderEP24IOBufferMemoryDescriptorj8EFI_GUIDS2_j : 656 -> 636
~ __ZN32AppleThunderboltIPControlCommand38ExtractFromThunderboltIPProtocolHeaderEP24IOBufferMemoryDescriptorPjP8EFI_GUIDS4_S2_ : 832 -> 812
~ __ZN32AppleThunderboltIPControlCommand35ExtractFromThunderboltIPLoginPacketEP24IOBufferMemoryDescriptorP8EFI_GUIDS3_PjS4_Pb : 684 -> 672
~ __ZN32AppleThunderboltIPControlCommand43ExtractFromThunderboltIPLoginResponsePacketEP24IOBufferMemoryDescriptorP8EFI_GUIDS3_PjS4_PhS4_ : 704 -> 696
~ __ZN32AppleThunderboltIPControlCommand44ExtractFromThunderboltIPLogoutResponsePacketEP24IOBufferMemoryDescriptorP8EFI_GUIDS3_PjS4_ : 632 -> 624
~ __ZN22AppleThunderboltIPPort18withPortAndServiceEP17IOThunderboltPortP25AppleThunderboltIPService : 696 -> 680
~ __ZN22AppleThunderboltIPPort18initPortAndServiceEP17IOThunderboltPortP25AppleThunderboltIPService : 1284 -> 1208
~ __ZN22AppleThunderboltIPPort5startEP9IOService : 1344 -> 1312
~ __ZN22AppleThunderboltIPPort16createMACAddressEv : 2348 -> 2072
~ __ZN22AppleThunderboltIPPort17createMediumStateEv : 988 -> 940
~ __ZN22AppleThunderboltIPPort16updateLinkStatusEv : 1144 -> 1112
~ __ZN22AppleThunderboltIPPort8finalizeEj : 1712 -> 1608
~ __ZN22AppleThunderboltIPPort4freeEv : 364 -> 352
~ sub_fffffe0009e543d8 -> sub_fffffe0009579f74 : 84 -> 76
~ sub_fffffe0009e5442c -> sub_fffffe0009579fc0 : 72 -> 68
~ __ZN22AppleThunderboltIPPort6enableEP18IONetworkInterface : 1768 -> 1752
~ __ZN22AppleThunderboltIPPort17outputStartLegacyEP18IONetworkInterfacej : 3832 -> 3828
~ __ZN22AppleThunderboltIPPort28outputStartAggregatedPacketsEP18IONetworkInterfacej : 2516 -> 2496
~ __ZN22AppleThunderboltIPPort15createInterfaceEv : 372 -> 340
~ sub_fffffe0009e56c0c -> sub_fffffe000957c754 : 192 -> 184
~ __ZN22AppleThunderboltIPPort15addIPConnectionEP28AppleThunderboltIPConnection : 1280 -> 1264
~ __ZN22AppleThunderboltIPPort18removeIPConnectionEP28AppleThunderboltIPConnection : 1820 -> 1796
~ __ZN22AppleThunderboltIPPort27createIPConnectionForXDLinkEP24IOThunderboltXDomainLinkP29AppleThunderboltIPTransmitter : 3556 -> 3416
~ __ZN22AppleThunderboltIPPort28getIPConnectionForRemoteUUIDE8EFI_GUID : 496 -> 472
~ __ZN22AppleThunderboltIPPort13receivePacketEP6__mbufm : 436 -> 420
~ sub_fffffe0009e58ed8 -> sub_fffffe000957e93c : 196 -> 180
~ __ZN28AppleThunderboltIPConnection14initWithParamsE8EFI_GUIDP25AppleThunderboltIPServiceP24IOThunderboltXDomainLinkP22AppleThunderboltIPPort : 1852 -> 1800
~ __ZN28AppleThunderboltIPConnection5startEP9IOService : 1976 -> 1832
~ __ZN28AppleThunderboltIPConnection8setStateEj : 900 -> 848
~ __ZN28AppleThunderboltIPConnection20setupPowerManagementEP9IOService : 484 -> 468
~ __ZN28AppleThunderboltIPConnection22destroyControlCommandsEv : 812 -> 780
~ __ZN28AppleThunderboltIPConnection8finalizeEj : 4996 -> 4844
~ __ZN28AppleThunderboltIPConnection21prepareForTerminationEv : 1636 -> 1628
~ __ZN28AppleThunderboltIPConnection4freeEv : 412 -> 392
~ __ZN28AppleThunderboltIPConnection13setPowerStateEmP9IOService : 3788 -> 3756
~ __ZN28AppleThunderboltIPConnection14dispatchLogoutEb : 1996 -> 1964
~ sub_fffffe0009e5dd38 -> sub_fffffe0009583570 : 92 -> 84
~ __ZN28AppleThunderboltIPConnection15returnRxCommandEP32AppleThunderboltIPReceiveCommand : 660 -> 644
~ __ZN28AppleThunderboltIPConnection6logoutEv : 3536 -> 3456
~ __ZN28AppleThunderboltIPConnection26xdLinkNotificationCallbackEPvP9IOService : 1340 -> 1260
~ __ZN28AppleThunderboltIPConnection25processXDLinkNotificationEP28IOThunderboltDispatchContext : 3224 -> 3200
~ __ZN28AppleThunderboltIPConnection13dispatchLoginEb : 1996 -> 1964
~ __ZN28AppleThunderboltIPConnection12createRxPathEv : 5456 -> 5040
~ __ZN28AppleThunderboltIPConnection12newRxCommandEP18IOMemoryDescriptory : 300 -> 264
~ __ZN28AppleThunderboltIPConnection13destroyRxPathEv : 3808 -> 3680
~ __ZN28AppleThunderboltIPConnection15configureRxPathEv : 2480 -> 2448
~ __ZN28AppleThunderboltIPConnection17rxCommandCallbackEPviP27IOThunderboltReceiveCommand : 4300 -> 4236
~ __ZN28AppleThunderboltIPConnection17newControlCommandEv : 188 -> 180
~ __ZN28AppleThunderboltIPConnection20returnControlCommandEP32AppleThunderboltIPControlCommand : 660 -> 644
~ sub_fffffe0009e6532c -> sub_fffffe000958a7b8 : 92 -> 84
~ __ZN28AppleThunderboltIPConnection22controlCommandCallbackEPviP26IOThunderboltConfigCommand : 1008 -> 988
~ __ZN28AppleThunderboltIPConnection17sendRequestPacketEjjb : 3056 -> 3076
~ __ZN28AppleThunderboltIPConnection18sendResponsePacketEjj : 3308 -> 3284
~ __ZN28AppleThunderboltIPConnection18processLoginPacketEP24IOBufferMemoryDescriptor : 3928 -> 3916
~ __ZN28AppleThunderboltIPConnection5loginEv : 6216 -> 6176
~ __ZN28AppleThunderboltIPConnection14setTransmitterEP29AppleThunderboltIPTransmitter : 708 -> 692
~ sub_fffffe0009e6bb40 -> sub_fffffe0009590f68 : 156 -> 148
~ sub_fffffe0009e6bbdc -> sub_fffffe0009590ffc : 116 -> 108
~ sub_fffffe0009e6bc50 -> sub_fffffe0009591068 : 104 -> 96
~ sub_fffffe0009e6bcb8 -> sub_fffffe00095910c8 : 180 -> 168

```
