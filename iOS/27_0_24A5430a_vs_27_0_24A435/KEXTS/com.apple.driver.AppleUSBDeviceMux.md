## com.apple.driver.AppleUSBDeviceMux

> `com.apple.driver.AppleUSBDeviceMux`

```diff

 571.0.0.0.1
   __TEXT.__const: 0x34
   __TEXT.__cstring: 0x1359
-  __TEXT_EXEC.__text: 0x58f8
+  __TEXT_EXEC.__text: 0x5a08
   __TEXT_EXEC.__auth_stubs: 0x4c0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68
Functions:
~ _panic : 128 -> 132
~ __ZN17AppleUSBDeviceMux9bmsRetainEP17BulkUSBMuxSessionPKc : 84 -> 88
~ __ZN17AppleUSBDeviceMux10bmsReleaseEP17BulkUSBMuxSessionPKc : 84 -> 88
~ sub_fffffe0009a4ded8 -> sub_fffffe0009adc4a4 : 72 -> 76
~ sub_fffffe0009a4df28 -> sub_fffffe0009adc4f8 : 68 -> 72
~ sub_fffffe0009a4df6c -> sub_fffffe0009adc540 : 68 -> 72
~ sub_fffffe0009a4dfc0 -> sub_fffffe0009adc598 : 68 -> 72
~ sub_fffffe0009a4e02c -> sub_fffffe0009adc608 : 72 -> 76
~ sub_fffffe0009a4e074 -> sub_fffffe0009adc654 : 120 -> 124
~ sub_fffffe0009a4e100 -> sub_fffffe0009adc6e4 : 104 -> 108
~ sub_fffffe0009a4e168 -> sub_fffffe0009adc750 : 104 -> 108
~ __ZN17AppleUSBDeviceMux5startEP9IOService : 984 -> 988
~ __ZN17AppleUSBDeviceMux17asyncReadCompleteEP6__mbufij : 1024 -> 1028
~ __ZN17AppleUSBDeviceMux18asyncWriteCompleteEP14USBWriteBufferij : 1108 -> 1112
~ __ZN17AppleUSBDeviceMux22asyncMbufWriteCompleteEP6__mbufij : 604 -> 608
~ __ZN17AppleUSBDeviceMux13sessionUpcallEP19IOSocketEventSourceP8__socketP17BulkUSBMuxSession : 460 -> 464
~ __ZN17AppleUSBDeviceMux12startUSBReadEv : 644 -> 648
~ __ZN17AppleUSBDeviceMux14resyncWithHostEv : 456 -> 460
~ __ZN17AppleUSBDeviceMux23allocateUSBWriteBuffersEv : 280 -> 284
~ sub_fffffe0009a4f788 -> sub_fffffe0009addd94 : 208 -> 212
~ __ZN17AppleUSBDeviceMux22allocateUSBReadBuffersEv : 204 -> 208
~ _IOLog : 136 -> 140
~ sub_fffffe0009a4f9f8 -> sub_fffffe0009ade010 : 352 -> 356
~ sub_fffffe0009a4fb58 -> sub_fffffe0009ade174 : 332 -> 336
~ sub_fffffe0009a4fca4 -> sub_fffffe0009ade2c4 : 288 -> 292
~ sub_fffffe0009a4fdc4 -> sub_fffffe0009ade3e8 : 64 -> 68
~ __ZN17AppleUSBDeviceMux18setPropertiesGatedEP8OSObject : 236 -> 240
~ __ZN17AppleUSBDeviceMux7messageEjP9IOServicePv : 892 -> 896
~ sub_fffffe0009a502c0 -> sub_fffffe0009ade8f0 : 164 -> 168
~ __ZN17AppleUSBDeviceMux11reportStatsEb : 184 -> 188
~ __ZN17AppleUSBDeviceMux14freeBufferListEP14USBWriteBuffer : 260 -> 264
~ __ZN17AppleUSBDeviceMux14sendMuxSegmentEP17BulkUSBMuxSession : 964 -> 968
~ __ZN17AppleUSBDeviceMux19handleConnectResultEP17BulkUSBMuxSessioni : 660 -> 664
~ sub_fffffe0009a50bdc -> sub_fffffe0009adf220 : 44 -> 48
~ sub_fffffe0009a50c08 -> sub_fffffe0009adf250 : 92 -> 96
~ __ZN17AppleUSBDeviceMux14writeMbufToUSBEP6__mbufj : 652 -> 656
~ __ZN17AppleUSBDeviceMux10newSessionEP6tcphdr : 960 -> 964
~ sub_fffffe0009a512b0 -> sub_fffffe0009adf904 : 44 -> 48
~ __ZN17AppleUSBDeviceMux17handleMuxTCPInputEP6__mbuf : 1608 -> 1612
~ __ZN17AppleUSBDeviceMux26handleMuxHostLogLevelInputEP6__mbuf : 188 -> 192
~ __ZN17AppleUSBDeviceMux21handleMuxVersionInputEP6__mbuf : 384 -> 388
~ __ZN17AppleUSBDeviceMux14writeMbufToUSBEP6__mbuf : 316 -> 320
~ __ZN17AppleUSBDeviceMux14handleMuxInputEP6__mbuf : 1908 -> 1912
~ __ZN17AppleUSBDeviceMux11dumpUSBLogsEv : 308 -> 312
~ sub_fffffe0009a52550 -> sub_fffffe0009ae0bc0 : 180 -> 184
~ sub_fffffe0009a5260c -> sub_fffffe0009ae0c80 : 72 -> 76
~ __ZN17AppleUSBDeviceMux14writeToUSBPipeEP14USBWriteBuffer : 576 -> 580
~ __ZN17AppleUSBDeviceMux13startUSBWriteEP14USBWriteBufferjb : 360 -> 364
~ sub_fffffe0009a529fc -> sub_fffffe0009ae107c : 360 -> 364
~ __ZN17AppleUSBDeviceMux11vsendMuxRSTEP6tcphdrbPKcPc : 440 -> 444
~ __ZN17AppleUSBDeviceMux14socketIsClosedEP8__socket : 196 -> 200
~ sub_fffffe0009a52f9c -> sub_fffffe0009ae1628 : 80 -> 84
~ sub_fffffe0009a5301c -> sub_fffffe0009ae16ac : 72 -> 76
~ sub_fffffe0009a5306c -> sub_fffffe0009ae1700 : 52 -> 56
~ sub_fffffe0009a530a0 -> sub_fffffe0009ae1738 : 52 -> 56
~ sub_fffffe0009a530e4 -> sub_fffffe0009ae1780 : 68 -> 72
~ sub_fffffe0009a53150 -> sub_fffffe0009ae17f0 : 72 -> 76
~ sub_fffffe0009a53198 -> sub_fffffe0009ae183c : 104 -> 108
~ sub_fffffe0009a53214 -> sub_fffffe0009ae18bc : 88 -> 92
~ sub_fffffe0009a5326c -> sub_fffffe0009ae1918 : 88 -> 92
~ sub_fffffe0009a532c4 -> sub_fffffe0009ae1974 : 196 -> 200
~ sub_fffffe0009a53394 -> sub_fffffe0009ae1a48 : 224 -> 228
~ sub_fffffe0009a53474 -> sub_fffffe0009ae1b2c : 116 -> 120
~ sub_fffffe0009a534e8 -> sub_fffffe0009ae1ba4 : 76 -> 80
~ sub_fffffe0009a5353c -> sub_fffffe0009ae1bfc : 80 -> 84
~ __ZN17AppleUSBDeviceMux10bmsReleaseEP17BulkUSBMuxSessionPKc.cold.1 : 40 -> 44
~ __ZN17AppleUSBDeviceMux9bmsRetainEP17BulkUSBMuxSessionPKc.cold.1 : 40 -> 44
~ __ZN17AppleUSBDeviceMux14freeBufferListEP14USBWriteBuffer.cold.1 : 56 -> 60
```
