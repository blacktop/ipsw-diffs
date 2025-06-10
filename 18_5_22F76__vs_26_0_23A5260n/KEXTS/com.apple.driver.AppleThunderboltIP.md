## com.apple.driver.AppleThunderboltIP

> `com.apple.driver.AppleThunderboltIP`

```diff

-1027.0.0.0.0
+1029.0.0.0.0
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x1e263
   __TEXT.__os_log: 0xe017
-  __TEXT_EXEC.__text: 0x37c0c
+  __TEXT_EXEC.__text: 0x3838c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x360
   __DATA.__common: 0x158

   __DATA_CONST.__const: 0x28e0
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 74A062AB-0360-3F0B-83DC-BA20A7E203B6
+  UUID: 5124B17C-53CC-3813-9D91-850623F94742
   Functions: 362
   Symbols:   0
   CStrings:  2019
Functions:
~ __ZN25AppleThunderboltIPService5startEP9IOService : 3360 -> 3368
~ __ZN25AppleThunderboltIPService24protocolListenerCallbackEPvP27IOThunderboltReceiveCommand : 2104 -> 2112
~ __ZN25AppleThunderboltIPService19handleXDomainPacketEP28IOThunderboltDispatchContext : 2020 -> 2092
~ sub_fffffff009a69598 -> sub_fffffff009da2130 : 40 -> 64
~ sub_fffffff009a6ad24 -> sub_fffffff009da38d4 : 12 -> 16
~ sub_fffffff009a6ad30 -> sub_fffffff009da38e4 : 12 -> 16
~ __ZN29AppleThunderboltIPTransmitter5startEP9IOService : 4580 -> 4628
~ __ZN29AppleThunderboltIPTransmitter29ipServiceNotificationCallbackEPvP9IOService : 1256 -> 1264
~ __ZN29AppleThunderboltIPTransmitter8finalizeEj : 5064 -> 5072
~ sub_fffffff009a6f128 -> sub_fffffff009da7d20 : 40 -> 64
~ __ZN29AppleThunderboltIPTransmitter13setPowerStateEmP9IOService : 3784 -> 3804
~ __ZN29AppleThunderboltIPTransmitter25dispatchLogoutWithRequestEb : 1764 -> 1768
~ __ZN29AppleThunderboltIPTransmitter24dispatchLoginWithRequestEb : 1836 -> 1840
~ __ZN29AppleThunderboltIPTransmitter18systemWillShutdownEj : 1348 -> 1344
~ __ZN29AppleThunderboltIPTransmitter17logoutWithRequestEv : 652 -> 648
~ __ZN29AppleThunderboltIPTransmitter28processIPServiceNotificationEP28IOThunderboltDispatchContext : 3864 -> 3860
~ __ZN29AppleThunderboltIPTransmitter12createTxPathEv : 3404 -> 3400
~ sub_fffffff009a75f14 -> sub_fffffff009daeb30 : 260 -> 252
~ __ZN29AppleThunderboltIPTransmitter17txCommandCallbackEPviP28IOThunderboltTransmitCommand : 1308 -> 1300
~ __ZN29AppleThunderboltIPTransmitter20timerCommandCallbackEPviP25IOThunderboltTimerCommand : 2632 -> 2636
~ __ZN29AppleThunderboltIPTransmitter14processTimeoutEP28IOThunderboltDispatchContext : 6992 -> 6988
~ __ZN29AppleThunderboltIPTransmitter34dispatchProcessLoginResponsePacketEP24IOBufferMemoryDescriptor : 1616 -> 1620
~ __ZN29AppleThunderboltIPTransmitter26processLoginResponsePacketEP28IOThunderboltDispatchContext : 4688 -> 4684
~ __ZN29AppleThunderboltIPTransmitter35dispatchProcessLogoutResponsePacketEP24IOBufferMemoryDescriptor : 1616 -> 1620
~ __ZN29AppleThunderboltIPTransmitter27processLogoutResponsePacketEP28IOThunderboltDispatchContext : 2340 -> 2332
~ __ZN29AppleThunderboltIPTransmitter16loginWithRequestEv : 1112 -> 1108
~ __ZN29AppleThunderboltIPTransmitter5loginEb : 3400 -> 3396
~ __ZN29AppleThunderboltIPTransmitter6logoutEb : 2780 -> 2776
~ __ZN29AppleThunderboltIPTransmitter12outputPacketEP6__mbufPv : 2864 -> 2856
~ __ZN22AppleThunderboltIPPort16updateLinkStatusEv : 1132 -> 1144
~ __ZN22AppleThunderboltIPPort17outputStartLegacyEP18IONetworkInterfacej : 3808 -> 3832
~ __ZN22AppleThunderboltIPPort11outputStartEP18IONetworkInterfacej : 24 -> 20
~ __ZN22AppleThunderboltIPPort28outputStartAggregatedPacketsEP18IONetworkInterfacej : 2520 -> 2516
~ __ZN28AppleThunderboltIPConnection8setStateEj : 748 -> 900
~ __ZN28AppleThunderboltIPConnection8finalizeEj : 4896 -> 4996
~ sub_fffffff009a8e100 -> sub_fffffff009dc6e0c : 40 -> 64
~ __ZN28AppleThunderboltIPConnection21prepareForTerminationEv : 1564 -> 1636
~ __ZN28AppleThunderboltIPConnection13setPowerStateEmP9IOService : 3708 -> 3788
~ __ZN28AppleThunderboltIPConnection14dispatchLogoutEb : 1920 -> 1996
~ __ZN28AppleThunderboltIPConnection18systemWillShutdownEj : 1188 -> 1256
~ __ZN28AppleThunderboltIPConnection6logoutEv : 3376 -> 3536
~ __ZN28AppleThunderboltIPConnection26xdLinkNotificationCallbackEPvP9IOService : 1332 -> 1340
~ __ZN28AppleThunderboltIPConnection25processXDLinkNotificationEP28IOThunderboltDispatchContext : 3156 -> 3224
~ __ZN28AppleThunderboltIPConnection13dispatchLoginEb : 1920 -> 1996
~ __ZN28AppleThunderboltIPConnection13destroyRxPathEv : 3668 -> 3808
~ sub_fffffff009a95b4c -> sub_fffffff009dceb5c : 776 -> 900
~ __ZN28AppleThunderboltIPConnection17rxCommandCallbackEPviP27IOThunderboltReceiveCommand : 4308 -> 4300
~ __ZN28AppleThunderboltIPConnection22controlCommandCallbackEPviP26IOThunderboltConfigCommand : 1016 -> 1008
~ __ZN28AppleThunderboltIPConnection17sendRequestPacketEjjb : 3060 -> 3056
~ __ZN28AppleThunderboltIPConnection18sendResponsePacketEjj : 3312 -> 3308
~ __ZN28AppleThunderboltIPConnection20processXDomainPacketEP24IOBufferMemoryDescriptor : 2180 -> 2176
~ __ZN28AppleThunderboltIPConnection18processLoginPacketEP24IOBufferMemoryDescriptor : 3740 -> 3928
~ __ZN28AppleThunderboltIPConnection19processLogoutPacketEP24IOBufferMemoryDescriptor : 2004 -> 2076
~ __ZN28AppleThunderboltIPConnection5loginEv : 5860 -> 6216
~ __ZN28AppleThunderboltIPConnection18connectionIsActiveEv : 396 -> 392
~ __ZN28AppleThunderboltIPConnection14getTransmitterEv : 312 -> 308
~ __ZN28AppleThunderboltIPConnection14setTransmitterEP29AppleThunderboltIPTransmitter : 712 -> 708
~ __ZN28AppleThunderboltIPConnection19setRemoteMACAddressEPhj : 1476 -> 1472
~ __ZN28AppleThunderboltIPConnection17compareMacAddressEPhj : 672 -> 668
~ __ZN28AppleThunderboltIPConnection17compareRemoteUUIDE8EFI_GUID : 684 -> 680

```
