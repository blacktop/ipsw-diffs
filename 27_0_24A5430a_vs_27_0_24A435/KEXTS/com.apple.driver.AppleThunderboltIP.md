## com.apple.driver.AppleThunderboltIP

> `com.apple.driver.AppleThunderboltIP`

```diff

   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x1e267
   __TEXT.__os_log: 0xe017
-  __TEXT_EXEC.__text: 0x36cf4
+  __TEXT_EXEC.__text: 0x370c8
   __TEXT_EXEC.__auth_stubs: 0x630
   __DATA.__data: 0x360
   __DATA.__common: 0x158
Functions:
~ sub_fffffe0009858350 -> sub_fffffe00098e3940 : 72 -> 76
~ sub_fffffe00098583a0 -> sub_fffffe00098e3994 : 52 -> 56
~ sub_fffffe00098583d4 -> sub_fffffe00098e39cc : 52 -> 56
~ sub_fffffe0009858418 -> sub_fffffe00098e3a14 : 68 -> 72
~ sub_fffffe0009858484 -> sub_fffffe00098e3a84 : 72 -> 76
~ sub_fffffe00098584cc -> sub_fffffe00098e3ad0 : 104 -> 108
~ sub_fffffe0009858548 -> sub_fffffe00098e3b50 : 88 -> 92
~ sub_fffffe00098585a0 -> sub_fffffe00098e3bac : 88 -> 92
~ __ZN25AppleThunderboltIPService5startEP9IOService : 3152 -> 3156
~ __ZN25AppleThunderboltIPService11createPortsEv : 2400 -> 2404
~ __ZN25AppleThunderboltIPService24protocolListenerCallbackEPvP27IOThunderboltReceiveCommand : 2028 -> 2032
~ __ZN25AppleThunderboltIPService16publishIPServiceEb : 1396 -> 1400
~ __ZN25AppleThunderboltIPService8finalizeEj : 1884 -> 1888
~ __ZN25AppleThunderboltIPService19handleXDomainPacketEP28IOThunderboltDispatchContext : 2064 -> 2068
~ sub_fffffe000985b874 -> sub_fffffe00098e6e9c : 56 -> 60
~ __ZN25AppleThunderboltIPService27getIPPortForThunderboltPortEP17IOThunderboltPort : 3636 -> 3640
~ __ZN25AppleThunderboltIPService15reserveForLoginEbP29AppleThunderboltIPTransmitter : 2144 -> 2148
~ sub_fffffe000985d00c -> sub_fffffe00098e8640 : 80 -> 84
~ sub_fffffe000985d06c -> sub_fffffe00098e86a4 : 56 -> 60
~ sub_fffffe000985d0a4 -> sub_fffffe00098e86e0 : 56 -> 60
~ sub_fffffe000985d0dc -> sub_fffffe00098e871c : 52 -> 56
~ sub_fffffe000985d110 -> sub_fffffe00098e8754 : 52 -> 56
~ _kprintHexDump : 500 -> 504
~ sub_fffffe000985d338 -> sub_fffffe00098e8984 : 48 -> 52
~ sub_fffffe000985d380 -> sub_fffffe00098e89d0 : 72 -> 76
~ sub_fffffe000985d3d0 -> sub_fffffe00098e8a24 : 52 -> 56
~ sub_fffffe000985d404 -> sub_fffffe00098e8a5c : 52 -> 56
~ sub_fffffe000985d448 -> sub_fffffe00098e8aa4 : 68 -> 72
~ sub_fffffe000985d4b4 -> sub_fffffe00098e8b14 : 72 -> 76
~ sub_fffffe000985d4fc -> sub_fffffe00098e8b60 : 104 -> 108
~ sub_fffffe000985d578 -> sub_fffffe00098e8be0 : 88 -> 92
~ sub_fffffe000985d5d0 -> sub_fffffe00098e8c3c : 88 -> 92
~ __ZN30AppleThunderboltIPMSMInterface21attachToDataLinkLayerEjPv : 288 -> 292
~ __ZN30AppleThunderboltIPMSMInterface29configureIPv6LinkLayerAddressEb : 1412 -> 1416
~ __ZN30AppleThunderboltIPMSMInterface23detachFromDataLinkLayerEjPv : 284 -> 288
~ sub_fffffe000985ded8 -> sub_fffffe00098e9554 : 80 -> 84
~ sub_fffffe000985df40 -> sub_fffffe00098e95c0 : 76 -> 80
~ sub_fffffe000985df8c -> sub_fffffe00098e9610 : 180 -> 184
~ __ZN25AppleThunderboltIPGlobalsC2Ev : 232 -> 236
~ sub_fffffe000985e128 -> sub_fffffe00098e97b4 : 76 -> 80
~ sub_fffffe000985e174 -> sub_fffffe00098e9804 : 92 -> 96
~ sub_fffffe000985e214 -> sub_fffffe00098e98a8 : 72 -> 76
~ sub_fffffe000985e264 -> sub_fffffe00098e98fc : 52 -> 56
~ sub_fffffe000985e298 -> sub_fffffe00098e9934 : 52 -> 56
~ sub_fffffe000985e2dc -> sub_fffffe00098e997c : 68 -> 72
~ sub_fffffe000985e348 -> sub_fffffe00098e99ec : 72 -> 76
~ sub_fffffe000985e390 -> sub_fffffe00098e9a38 : 104 -> 108
~ sub_fffffe000985e40c -> sub_fffffe00098e9ab8 : 88 -> 92
~ sub_fffffe000985e464 -> sub_fffffe00098e9b14 : 88 -> 92
~ __ZN29AppleThunderboltIPTransmitter5startEP9IOService : 4404 -> 4408
~ __ZN29AppleThunderboltIPTransmitter8setStateEj : 572 -> 576
~ __ZN29AppleThunderboltIPTransmitter29ipServiceNotificationCallbackEPvP9IOService : 1212 -> 1216
~ __ZN29AppleThunderboltIPTransmitter20setupPowerManagementEP9IOService : 468 -> 472
~ __ZN29AppleThunderboltIPTransmitter8finalizeEj : 4920 -> 4924
~ sub_fffffe00098611f4 -> sub_fffffe00098ec8bc : 56 -> 60
~ __ZN29AppleThunderboltIPTransmitter21prepareForTerminationEv : 2032 -> 2036
~ __ZN29AppleThunderboltIPTransmitter8setTimerEj : 1780 -> 1784
~ __ZN29AppleThunderboltIPTransmitter4freeEv : 352 -> 356
~ __ZN29AppleThunderboltIPTransmitter13setPowerStateEmP9IOService : 3788 -> 3792
~ __ZN29AppleThunderboltIPTransmitter25dispatchLogoutWithRequestEb : 1736 -> 1740
~ __ZN29AppleThunderboltIPTransmitter24dispatchLoginWithRequestEb : 1808 -> 1812
~ __ZN29AppleThunderboltIPTransmitter18systemWillShutdownEj : 1344 -> 1348
~ __ZN29AppleThunderboltIPTransmitter17logoutWithRequestEv : 648 -> 652
~ __ZN29AppleThunderboltIPTransmitter28processIPServiceNotificationEP28IOThunderboltDispatchContext : 3756 -> 3760
~ sub_fffffe00098655ec -> sub_fffffe00098f0cdc : 88 -> 92
~ __ZN29AppleThunderboltIPTransmitter12createTxPathEv : 3136 -> 3140
~ __ZN29AppleThunderboltIPTransmitter12newTxCommandEb : 572 -> 576
~ __ZN29AppleThunderboltIPTransmitter15returnTxCommandEP33AppleThunderboltIPTransmitCommandb : 468 -> 472
~ __ZN29AppleThunderboltIPTransmitter13destroyTxPathEv : 2640 -> 2644
~ __ZN29AppleThunderboltIPTransmitter15configureTxPathEv : 2944 -> 2948
~ sub_fffffe0009867c74 -> sub_fffffe00098f337c : 140 -> 144
~ sub_fffffe0009867d00 -> sub_fffffe00098f340c : 244 -> 248
~ __ZN29AppleThunderboltIPTransmitter17txCommandCallbackEPviP28IOThunderboltTransmitCommand : 1272 -> 1276
~ __ZN29AppleThunderboltIPTransmitter20timerCommandCallbackEPviP25IOThunderboltTimerCommand : 2584 -> 2588
~ __ZN29AppleThunderboltIPTransmitter14processTimeoutEP28IOThunderboltDispatchContext : 6936 -> 6940
~ __ZN29AppleThunderboltIPTransmitter16sendLoginRequestEv : 2776 -> 2780
~ __ZN29AppleThunderboltIPTransmitter17sendLogoutRequestEv : 1732 -> 1736
~ __ZN29AppleThunderboltIPTransmitter34dispatchProcessLoginResponsePacketEP24IOBufferMemoryDescriptor : 1568 -> 1572
~ __ZN29AppleThunderboltIPTransmitter26processLoginResponsePacketEP28IOThunderboltDispatchContext : 4640 -> 4644
~ __ZN29AppleThunderboltIPTransmitter35dispatchProcessLogoutResponsePacketEP24IOBufferMemoryDescriptor : 1568 -> 1572
~ __ZN29AppleThunderboltIPTransmitter27processLogoutResponsePacketEP28IOThunderboltDispatchContext : 2292 -> 2296
~ __ZN29AppleThunderboltIPTransmitter16loginWithRequestEv : 1108 -> 1112
~ __ZN29AppleThunderboltIPTransmitter5loginEb : 3388 -> 3392
~ __ZN29AppleThunderboltIPTransmitter6logoutEb : 2776 -> 2780
~ __ZN29AppleThunderboltIPTransmitter12outputPacketEP6__mbufPv : 2820 -> 2824
~ __ZN29AppleThunderboltIPTransmitter13submitHeadersEP40AppleThunderboltIPPacketHeaderAggregatedj : 216 -> 220
~ sub_fffffe00098709c0 -> sub_fffffe00098fc108 : 276 -> 280
~ sub_fffffe0009870ad4 -> sub_fffffe00098fc220 : 88 -> 92
~ __ZN29AppleThunderboltIPTransmitter13getTxE2EHopIDEPt : 936 -> 940
~ sub_fffffe0009870ed4 -> sub_fffffe00098fc628 : 88 -> 92
~ sub_fffffe0009870f40 -> sub_fffffe00098fc698 : 80 -> 84
~ sub_fffffe0009870fa0 -> sub_fffffe00098fc6fc : 72 -> 76
~ sub_fffffe0009870ff0 -> sub_fffffe00098fc750 : 52 -> 56
~ sub_fffffe0009871024 -> sub_fffffe00098fc788 : 52 -> 56
~ sub_fffffe0009871068 -> sub_fffffe00098fc7d0 : 68 -> 72
~ sub_fffffe00098710d4 -> sub_fffffe00098fc840 : 72 -> 76
~ sub_fffffe000987111c -> sub_fffffe00098fc88c : 104 -> 108
~ sub_fffffe0009871198 -> sub_fffffe00098fc90c : 88 -> 92
~ sub_fffffe00098711f0 -> sub_fffffe00098fc968 : 88 -> 92
~ __ZN33AppleThunderboltIPTransmitCommand14withControllerEP23IOThunderboltControllery : 148 -> 152
~ __ZN33AppleThunderboltIPTransmitCommand18initWithControllerEP23IOThunderboltControllery : 360 -> 364
~ __ZN33AppleThunderboltIPTransmitCommand22withControllerAndQueueEP23IOThunderboltControllerP26IOThunderboltTransmitQueueby : 232 -> 236
~ __ZN33AppleThunderboltIPTransmitCommand38initWithControllerAndQueueAllocateDescEP23IOThunderboltControllerP26IOThunderboltTransmitQueuey : 560 -> 564
~ __ZN33AppleThunderboltIPTransmitCommand26initWithControllerAndQueueEP23IOThunderboltControllerP26IOThunderboltTransmitQueue : 356 -> 360
~ __ZN33AppleThunderboltIPTransmitCommand27addMemoryDescriptorMultipleEPP18IOMemoryDescriptorjy : 488 -> 492
~ sub_fffffe0009871aa8 -> sub_fffffe00098fd23c : 152 -> 156
~ __ZN33AppleThunderboltIPTransmitCommand11BuildPacketEjttjP6__mbufj : 560 -> 564
~ __ZN33AppleThunderboltIPTransmitCommand18BuildHeadersPacketEP40AppleThunderboltIPPacketHeaderAggregatedj : 512 -> 516
~ sub_fffffe0009871f70 -> sub_fffffe00098fd710 : 180 -> 184
~ sub_fffffe000987202c -> sub_fffffe00098fd7d0 : 80 -> 84
~ sub_fffffe000987208c -> sub_fffffe00098fd834 : 72 -> 76
~ sub_fffffe00098720dc -> sub_fffffe00098fd888 : 52 -> 56
~ sub_fffffe0009872110 -> sub_fffffe00098fd8c0 : 52 -> 56
~ sub_fffffe0009872154 -> sub_fffffe00098fd908 : 68 -> 72
~ sub_fffffe00098721c0 -> sub_fffffe00098fd978 : 72 -> 76
~ sub_fffffe0009872208 -> sub_fffffe00098fd9c4 : 104 -> 108
~ sub_fffffe0009872284 -> sub_fffffe00098fda44 : 88 -> 92
~ sub_fffffe00098722dc -> sub_fffffe00098fdaa0 : 88 -> 92
~ sub_fffffe0009872334 -> sub_fffffe00098fdafc : 156 -> 160
~ __ZN32AppleThunderboltIPReceiveCommand18initWithControllerEP23IOThunderboltController : 548 -> 552
~ __ZN32AppleThunderboltIPReceiveCommand22withControllerAndQueueEP23IOThunderboltControllerP25IOThunderboltReceiveQueueP18IOMemoryDescriptory : 156 -> 160
~ __ZN32AppleThunderboltIPReceiveCommand26initWithControllerAndQueueEP23IOThunderboltControllerP25IOThunderboltReceiveQueueP18IOMemoryDescriptory : 884 -> 888
~ sub_fffffe0009872a04 -> sub_fffffe00098fe1dc : 136 -> 140
~ __ZN32AppleThunderboltIPReceiveCommand17ExtractFromPacketEPjPtS1_S0_PPh : 648 -> 652
~ __ZN32AppleThunderboltIPReceiveCommand27ExtractFromPacketAggregatedEPPhbP40AppleThunderboltIPPacketHeaderAggregatedPj : 828 -> 832
~ sub_fffffe0009873058 -> sub_fffffe00098fe83c : 80 -> 84
~ sub_fffffe00098730b8 -> sub_fffffe00098fe8a0 : 72 -> 76
~ sub_fffffe0009873108 -> sub_fffffe00098fe8f4 : 52 -> 56
~ sub_fffffe000987313c -> sub_fffffe00098fe92c : 52 -> 56
~ sub_fffffe0009873180 -> sub_fffffe00098fe974 : 68 -> 72
~ sub_fffffe00098731ec -> sub_fffffe00098fe9e4 : 72 -> 76
~ sub_fffffe0009873234 -> sub_fffffe00098fea30 : 104 -> 108
~ sub_fffffe00098732b0 -> sub_fffffe00098feab0 : 88 -> 92
~ sub_fffffe0009873308 -> sub_fffffe00098feb0c : 88 -> 92
~ __ZN32AppleThunderboltIPControlCommand10withParamsEP23IOThunderboltController8EFI_GUIDS2_P24IOThunderboltXDomainLink : 196 -> 200
~ __ZN32AppleThunderboltIPControlCommand14initWithParamsEP23IOThunderboltController8EFI_GUIDS2_P24IOThunderboltXDomainLink : 760 -> 764
~ sub_fffffe0009873728 -> sub_fffffe00098fef38 : 160 -> 164
~ __ZN32AppleThunderboltIPControlCommand16BuildLoginPacketEjjb : 488 -> 492
~ __ZN32AppleThunderboltIPControlCommand29BuildThunderboltIPLoginPacketEP24IOBufferMemoryDescriptor8EFI_GUIDS2_jjb : 428 -> 432
~ __ZN32AppleThunderboltIPControlCommand24BuildLoginResponsePacketEjjPhj : 464 -> 468
~ __ZN32AppleThunderboltIPControlCommand37BuildThunderboltIPLoginResponsePacketEP24IOBufferMemoryDescriptor8EFI_GUIDS2_jjPhj : 456 -> 460
~ __ZN32AppleThunderboltIPControlCommand17BuildLogoutPacketEj : 464 -> 468
~ __ZN32AppleThunderboltIPControlCommand25BuildLogoutResponsePacketEjj : 468 -> 472
~ __ZN32AppleThunderboltIPControlCommand38BuildThunderboltIPLogoutResponsePacketEP24IOBufferMemoryDescriptor8EFI_GUIDS2_jj : 396 -> 400
~ __ZN32AppleThunderboltIPControlCommand9LogPacketEv : 272 -> 276
~ sub_fffffe0009874684 -> sub_fffffe00098ffeb8 : 80 -> 84
~ sub_fffffe00098746d4 -> sub_fffffe00098fff0c : 80 -> 84
~ __ZN32AppleThunderboltIPControlCommand32BuildThunderboltIPProtocolHeaderEP24IOBufferMemoryDescriptorj8EFI_GUIDS2_j : 636 -> 640
~ __ZN32AppleThunderboltIPControlCommand38ExtractFromThunderboltIPProtocolHeaderEP24IOBufferMemoryDescriptorPjP8EFI_GUIDS4_S2_ : 812 -> 816
~ __ZN32AppleThunderboltIPControlCommand35ExtractFromThunderboltIPLoginPacketEP24IOBufferMemoryDescriptorP8EFI_GUIDS3_PjS4_Pb : 672 -> 676
~ __ZN32AppleThunderboltIPControlCommand43ExtractFromThunderboltIPLoginResponsePacketEP24IOBufferMemoryDescriptorP8EFI_GUIDS3_PjS4_PhS4_ : 696 -> 700
~ __ZN32AppleThunderboltIPControlCommand36ExtractFromThunderboltIPLogoutPacketEP24IOBufferMemoryDescriptorP8EFI_GUIDS3_Pj : 556 -> 560
~ __ZN32AppleThunderboltIPControlCommand44ExtractFromThunderboltIPLogoutResponsePacketEP24IOBufferMemoryDescriptorP8EFI_GUIDS3_PjS4_ : 624 -> 628
~ sub_fffffe00098756c8 -> sub_fffffe0009900f1c : 80 -> 84
~ sub_fffffe0009875728 -> sub_fffffe0009900f80 : 72 -> 76
~ sub_fffffe0009875778 -> sub_fffffe0009900fd4 : 52 -> 56
~ sub_fffffe00098757ac -> sub_fffffe000990100c : 52 -> 56
~ sub_fffffe00098757f0 -> sub_fffffe0009901054 : 68 -> 72
~ sub_fffffe000987585c -> sub_fffffe00099010c4 : 72 -> 76
~ sub_fffffe00098758a4 -> sub_fffffe0009901110 : 104 -> 108
~ sub_fffffe0009875920 -> sub_fffffe0009901190 : 88 -> 92
~ sub_fffffe0009875978 -> sub_fffffe00099011ec : 88 -> 92
~ __ZN22AppleThunderboltIPPort18withPortAndServiceEP17IOThunderboltPortP25AppleThunderboltIPService : 680 -> 684
~ __ZN22AppleThunderboltIPPort18initPortAndServiceEP17IOThunderboltPortP25AppleThunderboltIPService : 1208 -> 1212
~ __ZN22AppleThunderboltIPPort5startEP9IOService : 1312 -> 1316
~ __ZN22AppleThunderboltIPPort16createMACAddressEv : 2072 -> 2076
~ __ZN22AppleThunderboltIPPort17createMediumStateEv : 940 -> 944
~ __ZN22AppleThunderboltIPPort16updateLinkStatusEv : 1112 -> 1116
~ __ZN22AppleThunderboltIPPort8finalizeEj : 1608 -> 1612
~ sub_fffffe0009877cb4 -> sub_fffffe0009903548 : 56 -> 60
~ __ZN22AppleThunderboltIPPort4freeEv : 352 -> 356
~ sub_fffffe0009877e70 -> sub_fffffe000990370c : 76 -> 80
~ __ZN22AppleThunderboltIPPort6enableEP18IONetworkInterface : 1752 -> 1756
~ __ZN22AppleThunderboltIPPort7disableEP18IONetworkInterface : 1076 -> 1080
~ __ZN22AppleThunderboltIPPort17outputStartLegacyEP18IONetworkInterfacej : 3828 -> 3832
~ __ZN22AppleThunderboltIPPort28outputStartAggregatedPacketsEP18IONetworkInterfacej : 2472 -> 2476
~ __ZN22AppleThunderboltIPPort8tickleTxEv : 328 -> 332
~ __ZN22AppleThunderboltIPPort15createInterfaceEv : 340 -> 344
~ sub_fffffe000987a638 -> sub_fffffe0009905ef0 : 184 -> 188
~ __ZN22AppleThunderboltIPPort15addIPConnectionEP28AppleThunderboltIPConnection : 1264 -> 1268
~ __ZN22AppleThunderboltIPPort18removeIPConnectionEP28AppleThunderboltIPConnection : 1796 -> 1800
~ __ZN22AppleThunderboltIPPort27createIPConnectionForXDLinkEP24IOThunderboltXDomainLinkP29AppleThunderboltIPTransmitter : 3416 -> 3420
~ __ZN22AppleThunderboltIPPort28getIPConnectionForRemoteUUIDE8EFI_GUID : 472 -> 476
~ __ZN22AppleThunderboltIPPort13receivePacketEP6__mbufm : 420 -> 424
~ sub_fffffe000987c3dc -> sub_fffffe0009907cac : 120 -> 124
~ sub_fffffe000987c454 -> sub_fffffe0009907d28 : 120 -> 124
~ sub_fffffe000987c4cc -> sub_fffffe0009907da4 : 56 -> 60
~ sub_fffffe000987c518 -> sub_fffffe0009907df4 : 80 -> 84
~ sub_fffffe000987c578 -> sub_fffffe0009907e58 : 72 -> 76
~ sub_fffffe000987c5c8 -> sub_fffffe0009907eac : 52 -> 56
~ sub_fffffe000987c5fc -> sub_fffffe0009907ee4 : 52 -> 56
~ sub_fffffe000987c640 -> sub_fffffe0009907f2c : 68 -> 72
~ sub_fffffe000987c6ac -> sub_fffffe0009907f9c : 72 -> 76
~ sub_fffffe000987c6f4 -> sub_fffffe0009907fe8 : 104 -> 108
~ sub_fffffe000987c770 -> sub_fffffe0009908068 : 88 -> 92
~ sub_fffffe000987c7c8 -> sub_fffffe00099080c4 : 88 -> 92
~ __ZN28AppleThunderboltIPConnection10withParamsE8EFI_GUIDP25AppleThunderboltIPServiceP24IOThunderboltXDomainLinkP22AppleThunderboltIPPort : 180 -> 184
~ __ZN28AppleThunderboltIPConnection14initWithParamsE8EFI_GUIDP25AppleThunderboltIPServiceP24IOThunderboltXDomainLinkP22AppleThunderboltIPPort : 1800 -> 1804
~ __ZN28AppleThunderboltIPConnection5startEP9IOService : 1832 -> 1836
~ __ZN28AppleThunderboltIPConnection8setStateEj : 848 -> 852
~ __ZN28AppleThunderboltIPConnection21createControlCommandsEv : 860 -> 864
~ __ZN28AppleThunderboltIPConnection20setupPowerManagementEP9IOService : 468 -> 472
~ __ZN28AppleThunderboltIPConnection8finalizeEj : 4844 -> 4848
~ sub_fffffe000987f57c -> sub_fffffe000990ae98 : 56 -> 60
~ __ZN28AppleThunderboltIPConnection21prepareForTerminationEv : 1628 -> 1632
~ __ZN28AppleThunderboltIPConnection4freeEv : 392 -> 396
~ __ZN28AppleThunderboltIPConnection13setPowerStateEmP9IOService : 3756 -> 3760
~ __ZN28AppleThunderboltIPConnection14dispatchLogoutEb : 1964 -> 1968
~ sub_fffffe0009881454 -> sub_fffffe000990cd84 : 84 -> 88
~ __ZN28AppleThunderboltIPConnection15returnRxCommandEP32AppleThunderboltIPReceiveCommand : 644 -> 648
~ __ZN28AppleThunderboltIPConnection18systemWillShutdownEj : 1256 -> 1260
~ __ZN28AppleThunderboltIPConnection6logoutEv : 3456 -> 3460
~ __ZN28AppleThunderboltIPConnection26xdLinkNotificationCallbackEPvP9IOService : 1260 -> 1264
~ __ZN28AppleThunderboltIPConnection25processXDLinkNotificationEP28IOThunderboltDispatchContext : 3200 -> 3204
~ __ZN28AppleThunderboltIPConnection13dispatchLoginEb : 1964 -> 1968
~ __ZN28AppleThunderboltIPConnection12createRxPathEv : 5040 -> 5044
~ __ZN28AppleThunderboltIPConnection12newRxCommandEP18IOMemoryDescriptory : 264 -> 268
~ __ZN28AppleThunderboltIPConnection13destroyRxPathEv : 3680 -> 3684
~ __ZN28AppleThunderboltIPConnection15configureRxPathEv : 2448 -> 2452
~ __ZN28AppleThunderboltIPConnection27rxCommandCallbackAggregatedEPviP27IOThunderboltReceiveCommand : 900 -> 904
~ __ZN28AppleThunderboltIPConnection17rxCommandCallbackEPviP27IOThunderboltReceiveCommand : 4236 -> 4240
~ __ZN28AppleThunderboltIPConnection17newControlCommandEv : 180 -> 184
~ __ZN28AppleThunderboltIPConnection20returnControlCommandEP32AppleThunderboltIPControlCommand : 644 -> 648
~ sub_fffffe000988869c -> sub_fffffe0009914008 : 84 -> 88
~ __ZN28AppleThunderboltIPConnection22controlCommandCallbackEPviP26IOThunderboltConfigCommand : 988 -> 992
~ __ZN28AppleThunderboltIPConnection17sendRequestPacketEjjb : 3076 -> 3080
~ __ZN28AppleThunderboltIPConnection18sendResponsePacketEjj : 3284 -> 3288
~ __ZN28AppleThunderboltIPConnection20processXDomainPacketEP24IOBufferMemoryDescriptor : 2176 -> 2180
~ __ZN28AppleThunderboltIPConnection18processLoginPacketEP24IOBufferMemoryDescriptor : 3916 -> 3920
~ __ZN28AppleThunderboltIPConnection19processLogoutPacketEP24IOBufferMemoryDescriptor : 2076 -> 2080
~ __ZN28AppleThunderboltIPConnection5loginEv : 6176 -> 6180
~ sub_fffffe000988dbac -> sub_fffffe0009919538 : 116 -> 120
~ __ZN28AppleThunderboltIPConnection18connectionIsActiveEv : 392 -> 396
~ __ZN28AppleThunderboltIPConnection14getTransmitterEv : 308 -> 312
~ __ZN28AppleThunderboltIPConnection14setTransmitterEP29AppleThunderboltIPTransmitter : 692 -> 696
~ __ZN28AppleThunderboltIPConnection19setRemoteMACAddressEPhj : 1456 -> 1460
~ __ZN28AppleThunderboltIPConnection17compareMacAddressEPhj : 668 -> 672
~ __ZN28AppleThunderboltIPConnection17compareRemoteUUIDE8EFI_GUID : 680 -> 684
~ sub_fffffe000988ecb0 -> sub_fffffe000991a658 : 88 -> 92
~ sub_fffffe000988ed20 -> sub_fffffe000991a6cc : 80 -> 84
~ __ZN33AppleThunderboltIPTransmitCommand18BuildHeadersPacketEP40AppleThunderboltIPPacketHeaderAggregatedj.cold.1 : 44 -> 48
~ sub_fffffe000988ee3c -> sub_fffffe000991a7f0 : 148 -> 152
~ sub_fffffe000988eed0 -> sub_fffffe000991a888 : 108 -> 112
~ sub_fffffe000988ef3c -> sub_fffffe000991a8f8 : 96 -> 100
~ sub_fffffe000988ef9c -> sub_fffffe000991a95c : 168 -> 172
```
