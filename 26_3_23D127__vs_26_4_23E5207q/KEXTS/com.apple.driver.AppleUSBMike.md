## com.apple.driver.AppleUSBMike

> `com.apple.driver.AppleUSBMike`

```diff

   __TEXT.__const: 0x28
   __TEXT.__cstring: 0xcda
   __TEXT.__os_log: 0x8de
-  __TEXT_EXEC.__text: 0x6c1c
+  __TEXT_EXEC.__text: 0x5fc8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xec
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x800
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 3B0A1FB7-FCEF-3DA4-81B3-B745DFE67AEC
+  UUID: 33DD3BB3-67CB-3ADF-9A7F-13BA8E6A0BFE
   Functions: 71
   Symbols:   0
   CStrings:  153
Functions:
~ __ZN12AppleUSBMike4initEP12OSDictionary : 380 -> 352
~ __ZN12AppleUSBMike5startEP9IOService : 5884 -> 4800
~ __ZNK12AppleUSBMike23isAudioControlInterfaceEP9IOService : 216 -> 192
~ sub_fffffe000a077838 -> sub_fffffe0009775988 : 244 -> 212
~ __ZN12AppleUSBMike19timestampWdtHandlerEP18IOTimerEventSource : 876 -> 776
~ sub_fffffe000a077f18 -> sub_fffffe0009775fe4 : 176 -> 168
~ __ZN12AppleUSBMike21serializeCurrentStateEPvP11OSSerialize : 1888 -> 1576
~ sub_fffffe000a078728 -> sub_fffffe00097766b4 : 368 -> 316
~ sub_fffffe000a078898 -> sub_fffffe00097767f0 : 448 -> 388
~ sub_fffffe000a078a58 -> sub_fffffe0009776974 : 384 -> 340
~ __ZN12AppleUSBMike12messageGatedEjP9IOServicePv : 1344 -> 1236
~ __ZN12AppleUSBMike10doTransferEv : 584 -> 552
~ __ZN12AppleUSBMike13startIOEngineEv : 1112 -> 1016
~ sub_fffffe000a07981c -> sub_fffffe0009777620 : 928 -> 820
~ __ZN12AppleUSBMike12stopIOEngineEv : 852 -> 740
~ sub_fffffe000a079f10 -> sub_fffffe0009777c38 : 128 -> 120
~ __ZN12AppleUSBMike24handleChangeStreamFormatEjP30IOAudio2StreamBasicDescriptiony : 732 -> 672
~ __ZN12AppleUSBMike22handleChangeSampleRateEPxy : 612 -> 556
~ __ZN12AppleUSBMike19performConfigChangeEP20IOAudio2Notification : 828 -> 756
~ __ZN12AppleUSBMike22helperChangeSampleRateEP20IOAudio2Notification : 1376 -> 1164
~ __ZN12AppleUSBMike23controlRequestCompletedEPviyP18IOMemoryDescriptor : 1008 -> 896
~ __ZN12AppleUSBMike20asyncWriteCompletionEP18IOMemoryDescriptoriP20IOUSBDeviceIsocFrame : 424 -> 400
~ __ZN12AppleUSBMike17completeAudioDataEP18IOMemoryDescriptoriP20IOUSBDeviceIsocFramej : 1240 -> 1116
~ __ZN12AppleUSBMike12getAudioDataEyPNS_12TransferDataE : 2248 -> 1996
~ sub_fffffe000a07c178 -> sub_fffffe0009779b08 : 452 -> 420
~ sub_fffffe000a07c6a4 -> sub_fffffe000977a014 : 96 -> 92

```
