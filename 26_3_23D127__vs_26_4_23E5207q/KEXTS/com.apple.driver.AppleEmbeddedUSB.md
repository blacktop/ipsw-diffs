## com.apple.driver.AppleEmbeddedUSB

> `com.apple.driver.AppleEmbeddedUSB`

```diff

-679.80.5.0.0
+682.100.15.0.0
   __TEXT.__cstring: 0x10bb
   __TEXT.__const: 0x1c
-  __TEXT_EXEC.__text: 0x8b68
+  __TEXT_EXEC.__text: 0x82c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x270
   __DATA.__common: 0x140

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1808
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: 5F498926-1589-3241-9DAC-9053EC952178
+  UUID: C4E2F57B-29B4-346C-8F47-2B444C67E7E3
   Functions: 210
   Symbols:   0
   CStrings:  127
Functions:
~ __ZN11AppleUSBPhy5startEP9IOService : 1324 -> 1180
~ sub_fffffe00091f1cb4 -> sub_fffffe00089d0bb4 : 272 -> 248
~ __ZN11AppleUSBPhy13setPropertiesEP8OSObject : 548 -> 516
~ sub_fffffe00091f1fe8 -> sub_fffffe00089d0eb0 : 256 -> 220
~ __ZN11AppleUSBPhy14enablePhyPowerEP8OSObjectj : 840 -> 744
~ sub_fffffe00091f249c -> sub_fffffe00089d12e0 : 372 -> 324
~ __ZN11AppleUSBPhy16applySDBTunablesEyPKNS_11tSDBTunableEm : 360 -> 344
~ sub_fffffe00091f29f4 -> __ZN24AppleUSBPhyServiceClient26AppleUSBPhyServiceNotifierC2Ev : 316 -> 284
~ sub_fffffe00091f2b54 -> sub_fffffe00089d1938 : 248 -> 224
~ sub_fffffe00091f2c4c -> sub_fffffe00089d1a18 : 248 -> 224
~ sub_fffffe00091f2d6c -> sub_fffffe00089d1b20 : 372 -> 316
~ sub_fffffe00091f2ee0 -> sub_fffffe00089d1c5c : 412 -> 380
~ __ZN24AppleUSBPhyServiceClient4freeEv : 320 -> 284
~ sub_fffffe00091f31bc -> sub_fffffe00089d1ef4 : 184 -> 148
~ __ZN24AppleUSBPhyServiceClient33initWithServicesPhyPortAndOptionsEP26AppleEmbeddedUSBArbitratorP11AppleUSBPhyNS2_8tPhyPortEj : 392 -> 352
~ sub_fffffe00091f33fc -> sub_fffffe00089d20e8 : 136 -> 120
~ __ZN24AppleUSBPhyServiceClient22requestPhyServiceLevelENS_16tPhyServiceLevelE : 1100 -> 1044
~ __ZN24AppleUSBPhyServiceClient21setOTGConnectionSpeedEN11AppleUSBPhy26tDeviceModeConnectionSpeedE : 192 -> 184
~ sub_fffffe00091f3d68 -> sub_fffffe00089d2a04 : 236 -> 200
~ __ZN26AppleEmbeddedUSBArbitrator5startEP9IOService : 2744 -> 2560
~ __ZN26AppleEmbeddedUSBArbitrator26powerStateChangeThreadCallEm : 440 -> 432
~ __ZN26AppleEmbeddedUSBArbitrator11registerPhyEP11AppleUSBPhy : 1696 -> 1540
~ __ZN26AppleEmbeddedUSBArbitrator27systemPowerChangeThreadCallEPNS_24tSystemPowerNotifyParamsE : 504 -> 496
~ __ZN26AppleEmbeddedUSBArbitrator32systemPowerChangeThreadCallGatedEj : 384 -> 360
~ __ZN26AppleEmbeddedUSBArbitrator22powerStateWillChangeToEmmP9IOService : 448 -> 440
~ sub_fffffe00091f5bac -> sub_fffffe00089d46a0 : 80 -> 72
~ __ZN26AppleEmbeddedUSBArbitrator18setPowerStateGatedEm : 264 -> 256
~ __ZN26AppleEmbeddedUSBArbitrator21powerStateDidChangeToEmmP9IOService : 448 -> 440
~ sub_fffffe00091f607c -> sub_fffffe00089d4b58 : 80 -> 72
~ sub_fffffe00091f60e4 -> sub_fffffe00089d4bb8 : 264 -> 236
~ sub_fffffe00091f61ec -> sub_fffffe00089d4ca4 : 524 -> 460
~ __ZN26AppleEmbeddedUSBArbitrator19updatePublishedNubsEj : 1880 -> 1668
~ __ZN26AppleEmbeddedUSBArbitrator22waitForTerminatingNubsEv : 708 -> 660
~ sub_fffffe00091f7044 -> sub_fffffe00089d59b8 : 148 -> 140
~ __ZN26AppleEmbeddedUSBArbitrator24handleUSBCableTypeChangeEmj : 604 -> 540
~ sub_fffffe00091f7334 -> sub_fffffe00089d5c60 : 236 -> 220
~ __ZN26AppleEmbeddedUSBArbitrator17enableDeviceClockEPK8OSObjectj : 832 -> 796
~ sub_fffffe00091f776c -> sub_fffffe00089d6064 : 372 -> 324
~ sub_fffffe00091f78e0 -> sub_fffffe00089d61a8 : 836 -> 800
~ sub_fffffe00091f7fe8 -> sub_fffffe00089d688c : 244 -> 208
~ sub_fffffe00091f80dc -> sub_fffffe00089d695c : 152 -> 148
~ sub_fffffe00091f8174 -> sub_fffffe00089d69f0 : 128 -> 112
~ sub_fffffe00091f81f4 -> sub_fffffe00089d6a60 : 124 -> 112
~ sub_fffffe00091f8270 -> sub_fffffe00089d6ad0 : 116 -> 104
~ sub_fffffe00091f82e4 -> sub_fffffe00089d6b38 : 248 -> 208
~ sub_fffffe00091f83dc -> sub_fffffe00089d6c08 : 128 -> 124
~ sub_fffffe00091f876c -> sub_fffffe00089d6f94 : 236 -> 228
~ __ZN19AppleEmbeddedUSBNub16initWithProviderEP9IOServiceP15IORegistryEntry : 1456 -> 1316
~ __ZN19AppleEmbeddedUSBNub17enableDevicePowerEPK8OSObjectj : 524 -> 500
~ __ZN19AppleEmbeddedUSBNub5startEP9IOService : 960 -> 912
~ sub_fffffe00091f9524 -> sub_fffffe00089d7c70 : 272 -> 240
~ sub_fffffe00091f964c -> sub_fffffe00089d7d78 : 276 -> 268
~ __ZN19AppleEmbeddedUSBNub26powerStateDidChangeToGatedEmmP9IOService : 268 -> 260
~ __ZN19AppleEmbeddedUSBNub15forcePowerGatedENS_11tPowerStateEb : 432 -> 424
~ sub_fffffe00091f9bbc -> sub_fffffe00089d82d0 : 268 -> 260
~ sub_fffffe00091f9cc8 -> sub_fffffe00089d83d4 : 168 -> 148
~ sub_fffffe00091f9e74 -> sub_fffffe00089d856c : 144 -> 136

```
