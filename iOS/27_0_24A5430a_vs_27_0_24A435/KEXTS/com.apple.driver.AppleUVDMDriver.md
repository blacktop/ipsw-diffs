## com.apple.driver.AppleUVDMDriver

> `com.apple.driver.AppleUVDMDriver`

```diff

 26.0.0.0.0
   __TEXT.__cstring: 0x13a6
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x6bd4
+  __TEXT_EXEC.__text: 0x6d0c
   __TEXT_EXEC.__auth_stubs: 0x2f0
   __DATA.__data: 0x188
   __DATA.__common: 0xb0
Functions:
~ sub_fffffe0009a996f0 -> sub_fffffe0009b28a70 : 72 -> 76
~ sub_fffffe0009a99740 -> sub_fffffe0009b28ac4 : 52 -> 56
~ sub_fffffe0009a99774 -> sub_fffffe0009b28afc : 52 -> 56
~ sub_fffffe0009a997b8 -> sub_fffffe0009b28b44 : 68 -> 72
~ sub_fffffe0009a99824 -> sub_fffffe0009b28bb4 : 72 -> 76
~ sub_fffffe0009a9986c -> sub_fffffe0009b28c00 : 104 -> 108
~ sub_fffffe0009a998e8 -> sub_fffffe0009b28c80 : 88 -> 92
~ sub_fffffe0009a99940 -> sub_fffffe0009b28cdc : 88 -> 92
~ __ZN17AppleUVDMEndpoint12initWithSelfEP9IOService : 436 -> 440
~ sub_fffffe0009a99b4c -> sub_fffffe0009b28ef0 : 596 -> 600
~ __ZN17AppleUVDMEndpoint16initWithEPNumberEP9IOServiceh : 196 -> 200
~ __ZN17AppleUVDMEndpoint5startEP9IOService : 256 -> 260
~ __ZN17AppleUVDMEndpoint4openEP9IOServicejPv : 232 -> 236
~ sub_fffffe0009a9a06c -> sub_fffffe0009b29420 : 192 -> 196
~ __ZN17AppleUVDMEndpoint13setPropertiesEP8OSObject : 1692 -> 1696
~ __ZN17AppleUVDMEndpoint11writeStreamEPhthS0_ : 332 -> 336
~ __ZN17AppleUVDMEndpoint10readStreamEPhtPtS0_S0_h : 356 -> 360
~ __ZN17AppleUVDMEndpoint10readAccessEPhhS0_tS0_ : 340 -> 344
~ __ZN17AppleUVDMEndpoint11writeAccessEPhhtS0_ : 332 -> 336
~ sub_fffffe0009a9adfc -> sub_fffffe0009b2a1c8 : 80 -> 84
~ sub_fffffe0009a9ae5c -> sub_fffffe0009b2a22c : 72 -> 76
~ sub_fffffe0009a9aeac -> sub_fffffe0009b2a280 : 52 -> 56
~ sub_fffffe0009a9aee0 -> sub_fffffe0009b2a2b8 : 52 -> 56
~ sub_fffffe0009a9af24 -> sub_fffffe0009b2a300 : 68 -> 72
~ sub_fffffe0009a9af90 -> sub_fffffe0009b2a370 : 72 -> 76
~ sub_fffffe0009a9afd8 -> sub_fffffe0009b2a3bc : 104 -> 108
~ sub_fffffe0009a9b054 -> sub_fffffe0009b2a43c : 88 -> 92
~ sub_fffffe0009a9b0ac -> sub_fffffe0009b2a498 : 88 -> 92
~ sub_fffffe0009a9b104 -> sub_fffffe0009b2a4f4 : 212 -> 216
~ sub_fffffe0009a9b1f4 -> sub_fffffe0009b2a5e8 : 112 -> 116
~ __ZN21AppleUVDMAceInterface16isUVDMModeActiveEv : 352 -> 356
~ __ZN21AppleUVDMAceInterface11writeAccessEhhPhhtS0_ : 764 -> 768
~ __ZN21AppleUVDMAceInterface10readAccessEhhPhhS0_tS0_ : 836 -> 840
~ __ZN21AppleUVDMAceInterface10readStreamEhhPhtPtS0_S0_h : 880 -> 884
~ __ZN21AppleUVDMAceInterface11writeStreamEhhPhthS0_ : 812 -> 816
~ __ZN21AppleUVDMAceInterface12getAppleVDOsEhP12OSDictionary : 1316 -> 1320
~ __ZN21AppleUVDMAceInterface11setUVDMModeEbPh : 304 -> 308
~ __ZN21AppleUVDMAceInterface11resetAccessEhhPh : 768 -> 772
~ sub_fffffe0009a9ca0c -> sub_fffffe0009b2be24 : 252 -> 256
~ sub_fffffe0009a9cb08 -> sub_fffffe0009b2bf24 : 168 -> 172
~ sub_fffffe0009a9cbb0 -> sub_fffffe0009b2bfd0 : 2232 -> 2236
~ sub_fffffe0009a9d470 -> sub_fffffe0009b2c894 : 80 -> 84
~ sub_fffffe0009a9d4d0 -> sub_fffffe0009b2c8f8 : 72 -> 76
~ sub_fffffe0009a9d520 -> sub_fffffe0009b2c94c : 64 -> 68
~ sub_fffffe0009a9d560 -> sub_fffffe0009b2c990 : 64 -> 68
~ sub_fffffe0009a9d5b0 -> sub_fffffe0009b2c9e4 : 68 -> 72
~ sub_fffffe0009a9d61c -> sub_fffffe0009b2ca54 : 72 -> 76
~ sub_fffffe0009a9d664 -> sub_fffffe0009b2caa0 : 52 -> 56
~ sub_fffffe0009a9d6b4 -> sub_fffffe0009b2caf4 : 100 -> 104
~ sub_fffffe0009a9d718 -> sub_fffffe0009b2cb5c : 136 -> 140
~ __ZN32IOPortTransportProtocolAppleUVDM5probeEP9IOServicePi : 228 -> 232
~ __ZN32IOPortTransportProtocolAppleUVDM5startEP9IOService : 912 -> 916
~ sub_fffffe0009a9dc14 -> sub_fffffe0009b2d064 : 60 -> 64
~ __ZN32IOPortTransportProtocolAppleUVDM20setupPowerManagementEv : 332 -> 336
~ sub_fffffe0009a9dd9c -> sub_fffffe0009b2d1f4 : 196 -> 200
~ sub_fffffe0009a9de60 -> sub_fffffe0009b2d2bc : 412 -> 416
~ sub_fffffe0009a9dffc -> sub_fffffe0009b2d45c : 192 -> 196
~ __ZN32IOPortTransportProtocolAppleUVDM9terminateEj : 156 -> 160
~ __ZN32IOPortTransportProtocolAppleUVDM12getAppleVDOsEhP12OSDictionary : 1724 -> 1728
~ __ZN32IOPortTransportProtocolAppleUVDM18readAccessForStartEhhPhhS0_tS0_iii : 1672 -> 1676
~ __ZN32IOPortTransportProtocolAppleUVDM11finishStartEP9IOService : 172 -> 176
~ __ZN32IOPortTransportProtocolAppleUVDM15setAvailableEPsEv : 624 -> 628
~ __ZN32IOPortTransportProtocolAppleUVDM13setPropertiesEP8OSObject : 400 -> 404
~ __ZN32IOPortTransportProtocolAppleUVDM15getAvailableEPsEPh : 256 -> 260
~ sub_fffffe0009a9f480 -> sub_fffffe0009b2e900 : 212 -> 216
~ sub_fffffe0009a9f554 -> sub_fffffe0009b2e9d8 : 252 -> 256
~ sub_fffffe0009a9f650 -> sub_fffffe0009b2ead8 : 204 -> 208
~ sub_fffffe0009a9f71c -> sub_fffffe0009b2eba8 : 180 -> 184
~ __ZN32IOPortTransportProtocolAppleUVDM12poweredStartEv : 868 -> 872
~ sub_fffffe0009a9fd04 -> sub_fffffe0009b2f198 : 80 -> 84
~ sub_fffffe0009a9fd64 -> sub_fffffe0009b2f1fc : 72 -> 76
~ sub_fffffe0009a9fdb4 -> sub_fffffe0009b2f250 : 52 -> 56
~ sub_fffffe0009a9fe00 -> sub_fffffe0009b2f2a0 : 72 -> 76
~ __ZN30AppleUVDMPDControllerInterface4initEv : 136 -> 140
~ sub_fffffe0009a9ff08 -> sub_fffffe0009b2f3b0 : 84 -> 88
~ __ZN30AppleUVDMPDControllerInterface7lockBusEy : 436 -> 440
~ sub_fffffe0009aa0110 -> sub_fffffe0009b2f5c0 : 96 -> 100
~ sub_fffffe0009aa01d0 -> sub_fffffe0009b2f684 : 80 -> 84
```
