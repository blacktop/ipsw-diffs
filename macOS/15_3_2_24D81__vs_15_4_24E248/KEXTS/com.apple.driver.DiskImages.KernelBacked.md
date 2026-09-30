## com.apple.driver.DiskImages.KernelBacked

> `com.apple.driver.DiskImages.KernelBacked`

```diff

-665.80.2.0.0
+671.100.2.0.0
   __TEXT.__cstring: 0x725
-  __TEXT_EXEC.__text: 0x8fcc
+  __TEXT_EXEC.__text: 0x921c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x178

   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x5da0
   __DATA_CONST.__kalloc_type: 0x240
-  UUID: 431BFBA6-B55D-306E-BFFE-DA91A5E2A9C5
-  Functions: 315
-  Symbols:   861
+  UUID: 08A19665-81F6-3100-A8A2-EC9F86024F12
+  Functions: 311
+  Symbols:   857
   CStrings:  73
 
Symbols:
- _ZN20KDIShadowedDiskImage13_addIndexNodeEb.cold.1
- _ZN20KDIShadowedDiskImage17_loadShadowBitmapEb.cold.1
- _ZN20KDIShadowedDiskImage20_generateShadowTableEv.cold.1
- _ZN20KDIShadowedDiskImage24_loadHeaderAndIndexNodesEb.cold.1
Functions:
~ __ZN21IOHDIXHDDriveInKernel10handleOpenEP9IOServicejPv : 208 -> 224
~ __ZN21IOHDIXHDDriveInKernel4freeEv : 104 -> 108
~ __ZN21IOHDIXHDDriveInKernel19processPropertyListEv : 1684 -> 1724
~ __ZN9KDIObject4freeEv : 28 -> 32
~ __ZN15KDIDiskImageNub4initEP12OSDictionary : 40 -> 48
~ __ZN15KDIDiskImageNub4freeEv : 120 -> 124
~ __ZN15KDIDiskImageNub5startEP9IOService : 908 -> 928
~ __ZN15KDIDiskImageNub10handleOpenEP9IOServicejPv : 208 -> 224
~ __ZN25KDIDiskImageNubUserClient11clientCloseEv : 272 -> 292
~ __ZN25KDIDiskImageNubUserClient4stopEP9IOService : 140 -> 136
~ __ZN25KDIDiskImageNubUserClient4freeEv : 88 -> 92
~ __ZN12KDIDiskImage4initEP12OSDictionary : 44 -> 48
~ __ZN12KDIDiskImage12_handleStartEP9IOService : 1740 -> 1816
~ __ZN12KDIDiskImage14checksumsMatchEP17HDIChecksumStructS1_ : 140 -> 148
~ __ZN20KDIShadowedDiskImage4initEP12OSDictionary : 76 -> 84
~ __ZN20KDIShadowedDiskImage4freeEv : 340 -> 384
~ __ZN20KDIShadowedDiskImage18_flushShadowBitmapEbxx : 156 -> 172
~ __ZN20KDIShadowedDiskImage5probeEP9IOServicePi : 176 -> 180
~ __ZN20KDIShadowedDiskImage11readSectorsExxPxPvb : 792 -> 856
~ __ZN20KDIShadowedDiskImage12writeSectorsExxPxPKvb : 308 -> 312
~ __ZN20KDIShadowedDiskImage17_writeSectorsCoreExxPxPKvbb : 376 -> 404
~ __ZN20KDIShadowedDiskImage20_markShadowBitmapRunExxbb : 552 -> 540
~ __ZN20KDIShadowedDiskImage44_optimizedNewBandWithSectorUsingShadowBitmapExxPxPKcb : 440 -> 452
~ __ZN20KDIShadowedDiskImage27_optimizedNewBandWithSectorExxPxPKvb : 408 -> 444
~ __ZN20KDIShadowedDiskImage5flushEv : 152 -> 144
~ __ZN20KDIShadowedDiskImage18_prepareShadowFileEb : 2292 -> 2352
~ __ZN20KDIShadowedDiskImage24_loadHeaderAndIndexNodesEb : 524 -> 540
~ __ZN20KDIShadowedDiskImage28_matchHeaderAgainstBaseImageEv : 260 -> 264
~ __ZN20KDIShadowedDiskImage20_generateShadowTableEv : 432 -> 460
~ __ZN20KDIShadowedDiskImage16_resetShadowFileEj : 508 -> 492
~ __ZN20KDIShadowedDiskImage8_addBandEjPKvxb : 508 -> 576
~ __ZN20KDIShadowedDiskImage13_getIndexNodeEj : 48 -> 68
~ __ZN20KDIShadowedDiskImage17_updateIndexNodesEb : 340 -> 360
~ __ZN20KDIShadowedDiskImage18_displayHeaderNodeEP20ShadowFileHeaderNode : 268 -> 272
~ __ZN20KDIShadowedDiskImage17_displayIndexNodeEP19ShadowFileIndexNode : 188 -> 192
~ _DI_ShadowFileHeaderNode_BigToHost : 96 -> 100
~ _DI_ShadowFileHeaderNode_HostToBig : 96 -> 100
~ _DI_ShadowFileIndexNode_BigToHost : 72 -> 76
~ _DI_ShadowFileIndexNode_HostToBig : 72 -> 76

```
