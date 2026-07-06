## com.apple.driver.AppleHIDTransportSPI

> `com.apple.driver.AppleHIDTransportSPI`

```diff

   __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x7d46
-  __TEXT_EXEC.__text: 0x3d0e0
+  __TEXT.__cstring: 0x7d47
+  __TEXT_EXEC.__text: 0x3d04c
   __TEXT_EXEC.__auth_stubs: 0x620
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ sub_fffffe0008ee62ec -> sub_fffffe0008ee12bc : 260 -> 256
~ sub_fffffe0008ee6974 -> sub_fffffe0008ee1940 : 436 -> 432
~ __ZN31AppleHIDTransportProtocolHIDSPI9startTestEv : 2992 -> 2984
~ sub_fffffe0008ef216c -> sub_fffffe0008eed12c : 16 -> 12
~ sub_fffffe0008ef3420 -> sub_fffffe0008eee3dc : 352 -> 344
~ __ZN26AppleHIDTransportDeviceSPI11handleStartEP9IOService : 2024 -> 1956
~ __ZN26AppleHIDTransportDeviceSPI17cacheDeviceConfigEP12OSDictionary : 1224 -> 1212
~ __ZN27AppleHIDTransportProtocolZ213getDeviceInfoEv : 1056 -> 1048
~ __ZN27AppleHIDTransportProtocolZ219deviceGetReportInfoEhPNS_10ReportInfoE : 824 -> 820
~ __ZN27AppleHIDTransportProtocolZ215deviceGetReportEPNS_12ReportStructE : 1284 -> 1280
~ __ZN27AppleHIDTransportProtocolZ220deviceSetReportShortEPNS_12ReportStructE : 792 -> 788
~ __ZN27AppleHIDTransportProtocolZ219deviceSetReportLongEPNS_12ReportStructE : 1132 -> 1128
~ __ZN27AppleHIDTransportProtocolZ212getCMDStatusEPNS_13CommandStatusE : 600 -> 596
~ __ZN27AppleHIDTransportProtocolZ221deviceGetResultLengthEPt : 720 -> 716
~ __ZN27AppleHIDTransportProtocolZ220deviceReadResultDataEt : 1076 -> 1072
~ sub_fffffe0008f0b0e0 -> sub_fffffe0008f06020 : 16 -> 12
CStrings:
+ "121111121222121211111211122112111111121112212112111112222212122222222222222222221121"
- "12111112122212121111121112211211111121112212112111112222212122222222222222222221121"

```
