## com.apple.iokit.AppleARMIISAudio

> `com.apple.iokit.AppleARMIISAudio`

```diff

   __TEXT.__os_log: 0x29d7
   __TEXT.__cstring: 0x3218
   __TEXT.__const: 0xa8
-  __TEXT_EXEC.__text: 0x15c8c
-  __TEXT_EXEC.__auth_stubs: 0x610
+  __TEXT_EXEC.__text: 0x15fc0
+  __TEXT_EXEC.__auth_stubs: 0x630
   __DATA.__data: 0x1a8
   __DATA.__common: 0x60
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x1160
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0x280
-  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   Functions: 323
Functions:
~ sub_fffffe00085f0030 -> sub_fffffe000862b590 : 144 -> 148
~ sub_fffffe00085f00e8 -> sub_fffffe000862b64c : 300 -> 304
~ sub_fffffe00085f021c -> sub_fffffe000862b784 : 144 -> 148
~ sub_fffffe00085f02ac -> sub_fffffe000862b818 : 144 -> 148
~ sub_fffffe00085f033c -> sub_fffffe000862b8ac : 64 -> 68
~ sub_fffffe00085f037c -> sub_fffffe000862b8f0 : 100 -> 104
~ sub_fffffe00085f044c -> sub_fffffe000862b9c4 : 72 -> 76
~ sub_fffffe00085f049c -> sub_fffffe000862ba18 : 60 -> 64
~ sub_fffffe00085f04d8 -> sub_fffffe000862ba58 : 60 -> 64
~ sub_fffffe00085f0524 -> sub_fffffe000862baa8 : 68 -> 72
~ sub_fffffe00085f0590 -> sub_fffffe000862bb18 : 72 -> 76
~ sub_fffffe00085f05d8 -> sub_fffffe000862bb64 : 112 -> 116
~ sub_fffffe00085f065c -> sub_fffffe000862bbec : 96 -> 100
~ sub_fffffe00085f06bc -> sub_fffffe000862bc50 : 96 -> 100
~ __ZN22AppleARMIISAudioDevice4initEP12OSDictionaryj : 472 -> 476
~ sub_fffffe00085f0928 -> sub_fffffe000862bec4 : 540 -> 544
~ __ZN22AppleARMIISAudioDevice5startEP9IOServiceP17AppleARMIISDevicejjxPK7OSArray : 2332 -> 2336
~ __ZN22AppleARMIISAudioDevice28_initExternalPowerDependencyEP9IOService : 864 -> 868
~ sub_fffffe00085f1808 -> sub_fffffe000862cdb0 : 324 -> 328
~ sub_fffffe00085f194c -> sub_fffffe000862cef8 : 120 -> 124
~ __ZN22AppleARMIISAudioDevice22setTransportSampleRateEx : 172 -> 176
~ sub_fffffe00085f1d38 -> sub_fffffe000862d2ec : 212 -> 216
~ sub_fffffe00085f1e0c -> sub_fffffe000862d3c4 : 160 -> 164
~ __ZN22AppleARMIISAudioDevice18setTransportFormatEjjjj : 1128 -> 1132
~ __ZN22AppleARMIISAudioDevice22setTransportDataFormatEjN22AppleARMDMAAudioDevice14DataFormatTypeE : 844 -> 848
~ sub_fffffe00085f2694 -> sub_fffffe000862dc58 : 156 -> 160
~ sub_fffffe00085f2730 -> sub_fffffe000862dcf8 : 464 -> 468
~ sub_fffffe00085f2900 -> sub_fffffe000862decc : 84 -> 88
~ sub_fffffe00085f2954 -> sub_fffffe000862df24 : 124 -> 128
~ _panic : 144 -> 148
~ __ZN22AppleARMIISAudioDevice19getTransportLatencyEj : 140 -> 144
~ sub_fffffe00085f2aec -> sub_fffffe000862e0c8 : 124 -> 128
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_ : 1124 -> 1128
~ __ZN22AppleARMIISAudioDevice12transferDataEjP18IOMemoryDescriptorPvjyy : 716 -> 720
~ __ZN22AppleARMIISAudioDevice12stopTransferEjj : 412 -> 416
~ __ZN22AppleARMIISAudioDevice16getBytesPerFrameEjj : 276 -> 280
~ __ZN22AppleARMIISAudioDevice25stopAudioAndDataTransfersEv : 1260 -> 1264
~ __ZN22AppleARMIISAudioDevice18setAudioSampleRateExjj : 272 -> 276
~ __ZN22AppleARMIISAudioDevice21setAudioStreamFormatsExPK7OSArray : 1188 -> 1192
~ __ZN22AppleARMIISAudioDevice16gangAudioDevicesEPS_b : 780 -> 784
~ __ZN22AppleARMIISAudioDevice9waitAwakeEv : 1120 -> 1124
~ sub_fffffe00085f492c -> sub_fffffe000862ff30 : 336 -> 340
~ sub_fffffe00085f4a7c -> sub_fffffe0008630084 : 172 -> 176
~ sub_fffffe00085f4bd0 -> sub_fffffe00086301dc : 172 -> 176
~ sub_fffffe00085f4c7c -> sub_fffffe000863028c : 160 -> 164
~ sub_fffffe00085f4d1c -> sub_fffffe0008630330 : 188 -> 192
~ sub_fffffe00085f4dd8 -> sub_fffffe00086303f0 : 172 -> 176
~ sub_fffffe00085f4e84 -> sub_fffffe00086304a0 : 188 -> 192
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray : 1320 -> 1324
~ sub_fffffe00085f56f8 -> sub_fffffe0008630d1c : 196 -> 200
~ sub_fffffe00085f57bc -> sub_fffffe0008630de4 : 332 -> 336
~ sub_fffffe00085f5908 -> sub_fffffe0008630f34 : 128 -> 132
~ __ZN22AppleARMIISAudioDevice19createDebugControlsEP7OSArray : 428 -> 432
~ __ZN14IISAudioDevice6Helper8Delegate19createDebugControlsEP22AppleARMIISAudioDevice : 496 -> 500
~ sub_fffffe00085f5d30 -> sub_fffffe0008631368 : 152 -> 156
~ sub_fffffe00085f5ddc -> sub_fffffe0008631418 : 80 -> 84
~ __ZN14IISAudioDevice6Helper8Delegate19createDebugControlsEP22AppleARMIISAudioDevice : 440 -> 444
~ __ZN14IISAudioDevice6Helper22processConfigOverridesEP15IORegistryEntryS2_RN22AppleARMDMAAudioDevice15OverrideConfigsE : 428 -> 432
~ sub_fffffe00085f631c -> sub_fffffe0008631964 : 72 -> 76
~ sub_fffffe00085f636c -> sub_fffffe00086319b8 : 60 -> 64
~ sub_fffffe00085f63c0 -> sub_fffffe0008631a10 : 72 -> 76
~ sub_fffffe00085f6440 -> sub_fffffe0008631a94 : 104 -> 108
~ sub_fffffe00085f64a8 -> sub_fffffe0008631b00 : 144 -> 148
~ __ZN22AppleARMDMAAudioDevice27_setSafetyOffsetSeedDivisorEP9IOService : 236 -> 240
~ __ZN22AppleARMDMAAudioDevice14setAudioFormatEjjjj : 672 -> 676
~ __ZN22AppleARMDMAAudioDevice18checkDMACompletionEP18IOTimerEventSource : 424 -> 428
~ __ZN22AppleARMDMAAudioDevice5startEP9IOServicexjjPKjS3_S3_ : 440 -> 444
~ __ZN22AppleARMDMAAudioDevice18setAudioSampleRateEx : 884 -> 888
~ __ZN22AppleARMDMAAudioDevice21setAudioStreamFormatsEPK7OSArrayxPKS2_PKNS_14DataFormatTypeES4_PKjS4_S9_S4_S9_ : 4668 -> 4672
~ sub_fffffe00085f81e0 -> sub_fffffe0008633854 : 308 -> 312
~ sub_fffffe00085f8314 -> sub_fffffe000863398c : 612 -> 616
~ sub_fffffe00085f8578 -> sub_fffffe0008633bf4 : 116 -> 120
~ sub_fffffe00085f8618 -> sub_fffffe0008633c98 : 68 -> 72
~ sub_fffffe00085f865c -> sub_fffffe0008633ce0 : 132 -> 136
~ sub_fffffe00085f86e0 -> sub_fffffe0008633d68 : 168 -> 172
~ __ZN22AppleARMDMAAudioDevice18startIOEngineGatedEv : 500 -> 504
~ __ZN22AppleARMDMAAudioDevice21startIOEngineInternalEb : 544 -> 548
~ sub_fffffe00085f8b9c -> sub_fffffe0008634230 : 196 -> 200
~ __ZN22AppleARMDMAAudioDevice16startDMAInternalEb : 1328 -> 1332
~ __ZN22AppleARMDMAAudioDevice16restartTransportEv : 448 -> 452
~ __ZN22AppleARMDMAAudioDevice18startDataTransfersEjP18IOMemoryDescriptorjyy : 1436 -> 1440
~ __ZN22AppleARMDMAAudioDevice10sendBufferEjP18IOMemoryDescriptorjyy : 1940 -> 1944
~ __ZN22AppleARMDMAAudioDevice18startIOEngineGatedEv.cold.1 : 168 -> 172
~ __ZN22AppleARMDMAAudioDevice17stopIOEngineGatedEv : 860 -> 864
~ __ZN22AppleARMDMAAudioDevice20stopIOEngineInternalEv : 612 -> 616
~ sub_fffffe00085fa8e0 -> sub_fffffe0008635f94 : 292 -> 296
~ __ZN22AppleARMDMAAudioDevice15setStreamActiveEjj : 492 -> 496
~ __ZN22AppleARMDMAAudioDevice20setStreamActiveGatedEjj : 1512 -> 1516
~ __ZN22AppleARMDMAAudioDevice22handleChangeSampleRateEPxy : 564 -> 568
~ __ZN22AppleARMDMAAudioDevice24handleChangeStreamFormatEjP30IOAudio2StreamBasicDescriptiony : 852 -> 856
~ __ZN22AppleARMDMAAudioDevice19performConfigChangeEP20IOAudio2Notification : 560 -> 564
~ __ZN22AppleARMDMAAudioDevice24performConfigChangeGatedEP20IOAudio2Notification : 716 -> 720
~ sub_fffffe00085fbff0 -> sub_fffffe00086376c0 : 300 -> 304
~ __ZN22AppleARMDMAAudioDevice23performSampleRateChangeEPKx : 820 -> 824
~ __ZN22AppleARMDMAAudioDevice25performStreamFormatChangeEjjPKx : 1708 -> 1712
~ sub_fffffe00085fcafc -> sub_fffffe00086381d8 : 292 -> 296
~ sub_fffffe00085fcc20 -> sub_fffffe0008638300 : 376 -> 380
~ __ZN22AppleARMDMAAudioDevice20setAudioStreamFormatEjNS_14DataFormatTypeEjjj : 1724 -> 1728
~ sub_fffffe00085fd478 -> sub_fffffe0008638b60 : 124 -> 128
~ __ZNK22AppleARMDMAAudioDevice34getStreamFormatSupportedSampleRateExjj : 1028 -> 1032
~ sub_fffffe00085fd904 -> sub_fffffe0008638ff4 : 184 -> 188
~ __ZN22AppleARMDMAAudioDevice25getAudioStreamDescriptionEjxNS_14DataFormatTypeEjjj : 264 -> 268
~ sub_fffffe00085fdb0c -> sub_fffffe0008639204 : 112 -> 116
~ __ZN22AppleARMDMAAudioDevice14completeBufferEPviyy : 1556 -> 1560
~ sub_fffffe00085fe190 -> sub_fffffe0008639890 : 348 -> 352
~ __ZN22AppleARMDMAAudioDevice15updateTimestampEyy : 1072 -> 1076
~ __ZN22AppleARMDMAAudioDevice15allocateBuffersEv : 1732 -> 1736
~ __ZN22AppleARMDMAAudioDevice20_addUserSafetyOffsetERji : 460 -> 464
~ __ZN22AppleARMDMAAudioDevice22getTransportBufferSizeEx : 416 -> 420
~ sub_fffffe00085ff14c -> sub_fffffe000863a860 : 940 -> 944
~ __ZN22AppleARMDMAAudioDevice28setAudioStreamFormatInternalEjNS_14DataFormatTypeEjjjP12OSDictionaryS2_ : 936 -> 940
~ __ZN22AppleARMDMAAudioDevice16gangAudioDevicesEPS_b : 456 -> 460
~ sub_fffffe00085ffaf8 -> sub_fffffe000863b218 : 168 -> 172
~ __ZN22AppleARMDMAAudioDevice25zeroFillBufferForStreamIDEj : 396 -> 400
~ sub_fffffe00085ffd40 -> sub_fffffe000863b468 : 128 -> 132
~ sub_fffffe00085ffdc0 -> sub_fffffe000863b4ec : 128 -> 132
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray : 1984 -> 1988
~ sub_fffffe0008600600 -> sub_fffffe000863bd34 : 432 -> 436
~ __ZN22AppleARMDMAAudioDevice28_computeSafetyOffsetDivisorsEiRi : 320 -> 324
~ sub_fffffe0008600910 -> sub_fffffe000863c04c : 80 -> 84
~ __ZN32AppleAudioStreamFormatterFactory31createAppleAudioStreamFormatterEP9IOServiceP6OSData : 444 -> 448
~ __ZN22AppleARMIISAudioDevice18setupForIsolatedIOEjyj : 416 -> 420
~ sub_fffffe0008600f64 -> sub_fffffe000863c6ac : 68 -> 72
~ __ZN22AppleARMIISAudioDevice13stopTransportEv : 428 -> 432
~ __ZN22AppleARMIISAudioDevice28_initExternalPowerDependencyEP9IOService.cold.1 : 108 -> 112
~ __ZN22AppleARMIISAudioDevice22setTransportSampleRateEx.cold.1 : 320 -> 324
~ sub_fffffe0008601300 -> sub_fffffe000863ca58 : 300 -> 304
~ __ZN22AppleARMIISAudioDevice23getIISControllerLatencyEj.cold.1 : 112 -> 116
~ __ZN22AppleARMIISAudioDevice19getTransportLatencyEj.cold.1 : 104 -> 108
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.1 : 248 -> 252
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.2 : 248 -> 252
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.3 : 248 -> 252
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.4 : 248 -> 252
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.5 : 248 -> 252
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.6 : 184 -> 188
~ __ZN22AppleARMIISAudioDevice18setTransportFormatEjjjj.cold.1 : 248 -> 252
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.8 : 248 -> 252
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.9 : 340 -> 344
~ __ZN22AppleARMIISAudioDevice14startTransportEPKP18IOMemoryDescriptorPKjPKyS7_.cold.10 : 288 -> 292
~ __ZN22AppleARMIISAudioDevice16getBytesPerFrameEjj.cold.1 : 44 -> 48
~ __ZN22AppleARMIISAudioDevice18setAudioSampleRateExjj.cold.1 : 372 -> 376
~ __ZN22AppleARMIISAudioDevice9waitAwakeEv.cold.1 : 88 -> 92
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.1 : 300 -> 304
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.2 : 264 -> 268
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.3 : 264 -> 268
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.4 : 264 -> 268
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.5 : 264 -> 268
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.6 : 264 -> 268
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.7 : 264 -> 268
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.8 : 264 -> 268
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.9 : 264 -> 268
~ __ZN22AppleARMIISAudioDevice17createIOReportersEPK7OSArray.cold.10 : 272 -> 276
~ __ZN14IISAudioDevice6Helper8Delegate19createDebugControlsEP22AppleARMIISAudioDevice.cold.2 : 64 -> 68
~ __ZN14IISAudioDevice6Helper8Delegate19createDebugControlsEP22AppleARMIISAudioDevice.cold.3 : 64 -> 68
~ __ZN14IISAudioDevice6Helper22processConfigOverridesEP15IORegistryEntryS2_RN22AppleARMDMAAudioDevice15OverrideConfigsE.cold.1 : 64 -> 68
~ __ZN14IISAudioDevice6Helper22processConfigOverridesEP15IORegistryEntryS2_RN22AppleARMDMAAudioDevice15OverrideConfigsE.cold.2 : 64 -> 68
~ __ZN22AppleARMDMAAudioDevice4initEP12OSDictionary : 336 -> 340
~ __ZN22AppleARMDMAAudioDevice13startInternalEP9IOServicexjPKjS3_S3_S3_ : 1188 -> 1232
~ _snprintf : 528 -> 532
~ __ZN22AppleARMDMAAudioDevice5startEP9IOServicexjPKjS3_S3_S3_ : 620 -> 624
~ __ZN22AppleARMDMAAudioDevice5startEP9IOServicePK7OSArrayxjPKjPKS4_PKNS_14DataFormatTypeES8_S6_S8_S6_S8_S6_ : 940 -> 944
~ __ZN22AppleARMDMAAudioDevice12transferDataEjP18IOMemoryDescriptorPvjyy : 80 -> 84
~ __ZN22AppleARMDMAAudioDevice12stopTransferEjj : 80 -> 84
~ __ZN22AppleARMDMAAudioDevice27_setSafetyOffsetSeedDivisorEP9IOService.cold.1 : 172 -> 176
~ __ZN22AppleARMDMAAudioDevice27_setSafetyOffsetSeedDivisorEP9IOService.cold.2 : 180 -> 184
~ __ZN22AppleARMDMAAudioDevice14setAudioFormatEjjjj.cold.1 : 104 -> 108
~ __ZN22AppleARMDMAAudioDevice18startIOEngineGatedEv.cold.1 : 288 -> 292
~ __ZN22AppleARMDMAAudioDevice18startIOEngineGatedEv.cold.2 : 288 -> 292
~ __ZN22AppleARMDMAAudioDevice10sendBufferEjP18IOMemoryDescriptorjyy.cold.1 : 384 -> 388
~ __ZN22AppleARMDMAAudioDevice15allocateBuffersEv.cold.1 : 88 -> 92
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.1 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.2 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.3 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.4 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.5 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.6 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.7 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.8 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.9 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.10 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.11 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.12 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.13 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.14 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.15 : 272 -> 276
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.16 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.17 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.18 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.19 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.20 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.21 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.22 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.23 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.24 : 284 -> 288
~ __ZN22AppleARMDMAAudioDevice17createIOReportersEPK7OSArray.cold.25 : 284 -> 288
```
