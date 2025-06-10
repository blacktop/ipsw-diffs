## com.apple.driver.AppleEmbeddedUSB

> `com.apple.driver.AppleEmbeddedUSB`

```diff

-651.100.4.0.0
+679.0.1.0.0
   __TEXT.__cstring: 0x10bb
   __TEXT.__const: 0x1c
-  __TEXT_EXEC.__text: 0x8b50
+  __TEXT_EXEC.__text: 0x8b68
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x270
   __DATA.__common: 0x140

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1808
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: 6F3DC88B-D565-302C-954E-926C72046988
+  UUID: 33DD39A6-DA05-3CAF-8F04-8441FEE2E3B0
   Functions: 210
   Symbols:   0
   CStrings:  127
Functions:
~ __ZN11AppleUSBPhy16applySDBTunablesEyPKNS_11tSDBTunableEm : 340 -> 360
~ sub_fffffff008f6a0cc -> sub_fffffff00919f0e0 : 388 -> 412
~ __ZN24AppleUSBPhyServiceClient33initWithServicesPhyPortAndOptionsEP26AppleEmbeddedUSBArbitratorP11AppleUSBPhyNS2_8tPhyPortEj : 368 -> 392
~ __ZN24AppleUSBPhyServiceClient22requestPhyServiceLevelENS_16tPhyServiceLevelE : 1108 -> 1100
~ __ZN26AppleEmbeddedUSBArbitrator5startEP9IOService : 2748 -> 2744
~ __ZN26AppleEmbeddedUSBArbitrator26powerStateChangeThreadCallEm : 444 -> 440
~ __ZN26AppleEmbeddedUSBArbitrator11registerPhyEP11AppleUSBPhy : 1700 -> 1696
~ __ZN26AppleEmbeddedUSBArbitrator27systemPowerChangeThreadCallEPNS_24tSystemPowerNotifyParamsE : 508 -> 504
~ __ZN26AppleEmbeddedUSBArbitrator22powerStateWillChangeToEmmP9IOService : 452 -> 448
~ __ZN26AppleEmbeddedUSBArbitrator21powerStateDidChangeToEmmP9IOService : 452 -> 448
~ sub_fffffff008f6e00c -> sub_fffffff0091a3030 : 296 -> 292
~ sub_fffffff008f7082c -> sub_fffffff0091a584c : 280 -> 276
~ sub_fffffff008f70a84 -> sub_fffffff0091a5aa0 : 316 -> 312

```
