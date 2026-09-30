## com.apple.driver.AppleSEPHDCPManager

> `com.apple.driver.AppleSEPHDCPManager`

```diff

 108.0.0.0.0
   __TEXT.__cstring: 0x876
   __TEXT.__os_log: 0x587
-  __TEXT_EXEC.__text: 0x4870
+  __TEXT_EXEC.__text: 0x49e8
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0
Functions:
~ sub_fffffe00095359e0 -> sub_fffffe00095b6e00 : 72 -> 76
~ sub_fffffe0009535a30 -> sub_fffffe00095b6e54 : 52 -> 56
~ sub_fffffe0009535a64 -> sub_fffffe00095b6e8c : 52 -> 56
~ sub_fffffe0009535aa8 -> sub_fffffe00095b6ed4 : 68 -> 72
~ sub_fffffe0009535b14 -> sub_fffffe00095b6f44 : 72 -> 76
~ __ZN16AppleHDCPManager18serializeDebugInfoEPvP11OSSerialize : 552 -> 556
~ sub_fffffe0009535da4 -> sub_fffffe00095b71dc : 112 -> 116
~ sub_fffffe0009535e28 -> sub_fffffe00095b7264 : 80 -> 84
~ sub_fffffe0009536068 -> sub_fffffe00095b74a8 : 96 -> 100
~ sub_fffffe00095360c8 -> sub_fffffe00095b750c : 120 -> 124
~ sub_fffffe0009536140 -> sub_fffffe00095b7588 : 140 -> 144
~ sub_fffffe00095361cc -> sub_fffffe00095b7618 : 72 -> 76
~ sub_fffffe000953621c -> sub_fffffe00095b766c : 52 -> 56
~ sub_fffffe0009536250 -> sub_fffffe00095b76a4 : 52 -> 56
~ sub_fffffe0009536294 -> sub_fffffe00095b76ec : 68 -> 72
~ sub_fffffe0009536300 -> sub_fffffe00095b775c : 72 -> 76
~ sub_fffffe0009536348 -> sub_fffffe00095b77a8 : 104 -> 108
~ sub_fffffe00095363c4 -> sub_fffffe00095b7828 : 88 -> 92
~ sub_fffffe000953641c -> sub_fffffe00095b7884 : 88 -> 92
~ __ZN18AppleHDCPInterface11withOptionsEP9IOServiceP25AppleHDCPEndpointProtocolP20SEPHDCPInterfaceInfo : 356 -> 360
~ __ZN18AppleHDCPInterface11handleCloseEP9IOService : 240 -> 244
~ sub_fffffe000953672c -> sub_fffffe00095b7ba0 : 80 -> 84
~ sub_fffffe00095367e8 -> sub_fffffe00095b7c60 : 20 -> 28
~ sub_fffffe00095367fc -> sub_fffffe00095b7c7c : 28 -> 20
~ sub_fffffe00095368dc -> sub_fffffe00095b7d54 : 72 -> 76
~ sub_fffffe000953692c -> sub_fffffe00095b7da8 : 52 -> 56
~ sub_fffffe0009536960 -> sub_fffffe00095b7de0 : 52 -> 56
~ sub_fffffe00095369a4 -> sub_fffffe00095b7e28 : 68 -> 72
~ sub_fffffe0009536a10 -> sub_fffffe00095b7e98 : 72 -> 76
~ sub_fffffe0009536a58 -> sub_fffffe00095b7ee4 : 104 -> 108
~ sub_fffffe0009536ad4 -> sub_fffffe00095b7f64 : 88 -> 92
~ sub_fffffe0009536b2c -> sub_fffffe00095b7fc0 : 88 -> 92
~ __ZN19AppleSEPHDCPManager5startEP9IOService : 168 -> 172
~ sub_fffffe0009536c40 -> sub_fffffe00095b80dc : 80 -> 84
~ sub_fffffe0009536ca0 -> sub_fffffe00095b8140 : 72 -> 76
~ sub_fffffe0009536cf0 -> sub_fffffe00095b8194 : 84 -> 88
~ sub_fffffe0009536d44 -> sub_fffffe00095b81ec : 84 -> 88
~ sub_fffffe0009536db4 -> sub_fffffe00095b8260 : 68 -> 72
~ sub_fffffe0009536e10 -> sub_fffffe00095b82c0 : 72 -> 76
~ sub_fffffe0009536e68 -> sub_fffffe00095b831c : 72 -> 76
~ sub_fffffe0009536eb0 -> sub_fffffe00095b8368 : 136 -> 140
~ sub_fffffe0009536f4c -> sub_fffffe00095b8408 : 120 -> 124
~ sub_fffffe0009536fc4 -> sub_fffffe00095b8484 : 120 -> 124
~ _panic : 304 -> 308
~ __ZN20AppleSEPHDCPEndpoint6actionEPvS0_ : 380 -> 384
~ sub_fffffe00095372e8 -> sub_fffffe00095b87b4 : 152 -> 156
~ sub_fffffe0009537380 -> sub_fffffe00095b8850 : 144 -> 148
~ sub_fffffe0009537458 -> sub_fffffe00095b892c : 144 -> 148
~ sub_fffffe00095374e8 -> sub_fffffe00095b89c0 : 144 -> 148
~ __ZN20AppleSEPHDCPEndpoint12disableGatedEv : 76 -> 80
~ sub_fffffe00095375c4 -> sub_fffffe00095b8aa4 : 144 -> 148
~ sub_fffffe0009537654 -> sub_fffffe00095b8b38 : 156 -> 160
~ sub_fffffe00095376f0 -> sub_fffffe00095b8bd8 : 156 -> 160
~ __ZN20AppleSEPHDCPEndpoint27waitForEndpointAvailabilityEPKN25AppleHDCPEndpointProtocol11RequestArgsE : 568 -> 572
~ __ZN20AppleSEPHDCPEndpoint28signalForEndpointAvailabiltyEPKN25AppleHDCPEndpointProtocol11RequestArgsE : 240 -> 244
~ sub_fffffe0009537abc -> sub_fffffe00095b8fb0 : 80 -> 84
~ __ZN16AppleHDCPManager5startEP9IOServiceP25AppleHDCPEndpointProtocol : 584 -> 588
~ __ZN16AppleHDCPManager16launchInterfacesEv : 840 -> 844
~ sub_fffffe0009538324 -> sub_fffffe00095b9824 : 144 -> 148
~ __ZN18AppleHDCPInterface11handleStartEP9IOService : 320 -> 324
~ __ZN18AppleHDCPInterface19serializeDeviceRoleEPvP11OSSerialize : 136 -> 140
~ __ZN18AppleHDCPInterface18matchPropertyTableEP12OSDictionaryPi : 468 -> 472
~ sub_fffffe0009538954 -> sub_fffffe00095b9e64 : 88 -> 92
~ sub_fffffe00095389ac -> sub_fffffe00095b9ec0 : 88 -> 92
~ sub_fffffe0009538a04 -> sub_fffffe00095b9f1c : 104 -> 108
~ sub_fffffe0009538a6c -> sub_fffffe00095b9f88 : 104 -> 108
~ __ZN18AppleHDCPInterface8readCertEP11IOHDCP_Cert : 216 -> 220
~ sub_fffffe0009538c14 -> sub_fffffe00095ba138 : 96 -> 100
~ sub_fffffe0009538c74 -> sub_fffffe00095ba19c : 104 -> 108
~ sub_fffffe0009538d40 -> sub_fffffe00095ba26c : 96 -> 100
~ sub_fffffe0009538da0 -> sub_fffffe00095ba2d0 : 108 -> 112
~ sub_fffffe0009538e0c -> sub_fffffe00095ba340 : 96 -> 100
~ __ZN18AppleHDCPInterface12consumeNewKmE14IOHDCP_EKpubKm : 248 -> 252
~ sub_fffffe0009538f64 -> sub_fffffe00095ba4a0 : 128 -> 132
~ sub_fffffe0009538fe4 -> sub_fffffe00095ba524 : 96 -> 100
~ sub_fffffe00095390ac -> sub_fffffe00095ba5f0 : 96 -> 100
~ sub_fffffe000953910c -> sub_fffffe00095ba654 : 108 -> 112
~ sub_fffffe0009539178 -> sub_fffffe00095ba6c4 : 88 -> 92
~ sub_fffffe00095391d0 -> sub_fffffe00095ba720 : 104 -> 108
~ sub_fffffe000953928c -> sub_fffffe00095ba7e0 : 88 -> 92
~ sub_fffffe00095392e4 -> sub_fffffe00095ba83c : 104 -> 108
~ sub_fffffe00095393a0 -> sub_fffffe00095ba8fc : 88 -> 92
~ sub_fffffe00095394bc -> sub_fffffe00095baa1c : 116 -> 120
~ sub_fffffe0009539530 -> sub_fffffe00095baa94 : 88 -> 92
~ sub_fffffe0009539690 -> sub_fffffe00095babf8 : 144 -> 148
~ sub_fffffe0009539720 -> sub_fffffe00095bac8c : 88 -> 92
~ __ZN18AppleHDCPInterface11withOptionsEP9IOServiceP25AppleHDCPEndpointProtocolP20SEPHDCPInterfaceInfo.cold.1 : 64 -> 68
~ __ZN18AppleHDCPInterface11withOptionsEP9IOServiceP25AppleHDCPEndpointProtocolP20SEPHDCPInterfaceInfo.cold.2 : 64 -> 68
~ __ZN18AppleHDCPInterface11withOptionsEP9IOServiceP25AppleHDCPEndpointProtocolP20SEPHDCPInterfaceInfo.cold.3 : 196 -> 200
~ __ZN19AppleSEPHDCPManager5startEP9IOService.cold.1 : 84 -> 88
~ __ZN19AppleSEPHDCPManager5startEP9IOService.cold.2 : 84 -> 88
~ __ZN20AppleSEPHDCPEndpoint21initWithDeviceServiceEP21AppleSEPDeviceService : 128 -> 132
~ __ZN20AppleSEPHDCPEndpoint18handleRequestGatedEPKN25AppleHDCPEndpointProtocol11RequestArgsE : 1456 -> 1460
~ __ZN20AppleSEPHDCPEndpoint21initWithDeviceServiceEP21AppleSEPDeviceService.cold.1 : 44 -> 48
~ __ZN20AppleSEPHDCPEndpoint12disableGatedEv.cold.1 : 44 -> 48
~ __ZN20AppleSEPHDCPEndpoint28signalForEndpointAvailabiltyEPKN25AppleHDCPEndpointProtocol11RequestArgsE.cold.1 : 68 -> 72
```
