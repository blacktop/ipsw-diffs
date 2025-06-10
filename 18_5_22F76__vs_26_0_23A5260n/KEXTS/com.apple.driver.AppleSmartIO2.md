## com.apple.driver.AppleSmartIO2

> `com.apple.driver.AppleSmartIO2`

```diff

-140.0.0.0.0
+141.0.0.0.0
   __TEXT.__cstring: 0x451b
   __TEXT.__const: 0x60
-  __TEXT_EXEC.__text: 0xc95c
+  __TEXT_EXEC.__text: 0xcdd4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7f8
   __DATA.__common: 0x1a0

   __DATA_CONST.__const: 0x21f0
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 58564ED0-65C5-37B0-8480-3D177A2B96FF
+  UUID: 03D56AC2-90A6-3D79-A30E-AA43E53F7D16
   Functions: 471
   Symbols:   0
   CStrings:  379
Functions:
~ sub_fffffff0098e23bc -> sub_fffffff009bfba7c : 40 -> 64
~ __ZN12AppleSmartIO17endpointForHandleEP8OSObjectPFvS1_PvS2_EjP16IODMAEventSource : 188 -> 240
~ __ZN20AppleSmartIOEndpoint11sendMessageEPvS0_b : 196 -> 212
~ __ZN20AppleSmartIOEndpoint18synchronousMessageEP19AppleSmartIOCommandPv : 1056 -> 1052
~ sub_fffffff0098e4598 -> sub_fffffff009bfdcb0 : 272 -> 288
~ sub_fffffff0098e4868 -> sub_fffffff009bfdf90 : 12 -> 16
~ __ZN19AppleSmartIOControl14setupMapRangesEv : 828 -> 844
~ __ZN19AppleSmartIOControl12sendTunablesEv : 984 -> 1016
~ __ZN25AppleSmartIODMAController17_getConfigurationEP9IOServicej : 304 -> 324
~ sub_fffffff0098e7d7c -> sub_fffffff009c014ec : 208 -> 232
~ __ZN25AppleSmartIODMAController15startDMACommandEjP12IODMACommandjyy : 120 -> 144
~ sub_fffffff0098e80cc -> sub_fffffff009c0186c : 116 -> 140
~ sub_fffffff0098e81c0 -> sub_fffffff009c01978 : 188 -> 212
~ sub_fffffff0098e82f4 -> sub_fffffff009c01ac4 : 148 -> 172
~ sub_fffffff0098e8388 -> sub_fffffff009c01b70 : 148 -> 172
~ sub_fffffff0098e841c -> sub_fffffff009c01c1c : 152 -> 176
~ sub_fffffff0098e84b4 -> sub_fffffff009c01ccc : 148 -> 172
~ __ZN25AppleSmartIODMAController15bufferForHandleEj : 48 -> 64
~ __ZN25AppleSmartIODMAController16segmentForHandleEj : 52 -> 68
~ __ZN25AppleSmartIODMAController25responseForEndpointAndTagEjj : 52 -> 72
~ __ZN15AppleSmartIODMA16_initWithOptionsEP12AppleSmartIOP25AppleSmartIODMAControllerP16IODMAEventSourcej : 512 -> 568
~ __ZN15AppleSmartIODMA16_startDMACommandEP12IODMACommandPyS2_ : 1296 -> 1568
~ sub_fffffff0098e924c -> sub_fffffff009c02bf8 : 516 -> 552
~ __ZN15AppleSmartIODMA8_stopDMAEPbPv : 788 -> 804
~ __ZN15AppleSmartIODMA13_configureDMAEv : 556 -> 572
~ sub_fffffff0098e9a28 -> sub_fffffff009c03418 : 60 -> 96
~ __ZN15AppleSmartIODMA14_notifyCommandEP19AppleSmartIOCommand : 284 -> 372
~ __ZN15AppleSmartIODMA13_asyncMessageEPvS0_ : 356 -> 372
~ __ZN15AppleSmartIODMA16_completeCommandEP19AppleSmartIOCommand : 684 -> 804
~ __ZN15AppleSmartIODMA19handleShimFIFOPowerEb : 264 -> 284
~ __ZN12AppleSmartIO20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_.cold.1 : 60 -> 84
~ __ZN12AppleSmartIO20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_.cold.2 : 60 -> 84
CStrings:
+ "18:51:19"
+ "May 30 2025"
- "20:15:54"
- "Apr 22 2025"

```
