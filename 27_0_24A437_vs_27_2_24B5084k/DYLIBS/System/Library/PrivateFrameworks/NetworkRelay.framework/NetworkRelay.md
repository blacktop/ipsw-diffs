## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-914.0.34.0.4
-  __TEXT.__text: 0x7a7dc
-  __TEXT.__objc_methlist: 0x1fc4
+914.40.22.0.0
+  __TEXT.__text: 0x7b6a4
+  __TEXT.__objc_methlist: 0x1ff4
   __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0xb60
-  __TEXT.__cstring: 0x104d4
+  __TEXT.__gcc_except_tab: 0xbbc
+  __TEXT.__cstring: 0x107bc
   __TEXT.__oslogstring: 0x13a9
-  __TEXT.__unwind_info: 0xe80
+  __TEXT.__unwind_info: 0xeb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd70
+  __DATA_CONST.__const: 0xda0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10e0
+  __DATA_CONST.__objc_selrefs: 0x1100
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x1f8
   __DATA_CONST.__got: 0x280
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x51e0
-  __AUTH_CONST.__objc_const: 0x5200
+  __AUTH_CONST.__cfstring: 0x5200
+  __AUTH_CONST.__objc_const: 0x5230
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x7a0
-  __DATA.__objc_ivar: 0x560
+  __DATA.__objc_ivar: 0x564
   __DATA.__data: 0x1f8
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_data: 0xbe0

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1064
-  Symbols:   2673
-  CStrings:  1997
+  Functions: 1074
+  Symbols:   2691
+  CStrings:  2008
 
Symbols:
+ -[NRDevicePairingManager checkAdditionalData:]
+ -[NRDevicePairingManager startPairingDevice:additionalData:withCompletion:resultBlock:]
+ -[NRDevicePairingManager updateAdditionalData:withCompletion:]
+ -[NRDevicePairingManagerMux startPairingForPairingManager:pairingTarget:additionalData:withCompletion:]
+ -[NRDevicePairingManagerMux updateAdditionalDataForPairingManager:additionalData:withCompletion:]
+ -[NRPairedDevice additionalData]
+ -[NRPairedDevice setAdditionalData:]
+ GCC_except_table705
+ GCC_except_table713
+ GCC_except_table718
+ GCC_except_table722
+ GCC_except_table727
+ GCC_except_table740
+ GCC_except_table744
+ GCC_except_table748
+ GCC_except_table752
+ GCC_except_table773
+ GCC_except_table776
+ GCC_except_table780
+ GCC_except_table787
+ GCC_except_table789
+ GCC_except_table791
+ GCC_except_table793
+ GCC_except_table796
+ GCC_except_table798
+ GCC_except_table800
+ GCC_except_table856
+ GCC_except_table858
+ GCC_except_table873
+ _OBJC_IVAR_$_NRPairedDevice._additionalData
+ ___103-[NRDevicePairingManagerMux startPairingForPairingManager:pairingTarget:additionalData:withCompletion:]_block_invoke
+ ___62-[NRDevicePairingManager updateAdditionalData:withCompletion:]_block_invoke
+ ___62-[NRDevicePairingManager updateAdditionalData:withCompletion:]_block_invoke_2
+ ___62-[NRDevicePairingManager updateAdditionalData:withCompletion:]_block_invoke_3
+ ___87-[NRDevicePairingManager startPairingDevice:additionalData:withCompletion:resultBlock:]_block_invoke
+ ___87-[NRDevicePairingManager startPairingDevice:additionalData:withCompletion:resultBlock:]_block_invoke_2
+ ___87-[NRDevicePairingManager startPairingDevice:additionalData:withCompletion:resultBlock:]_block_invoke_3
+ ___97-[NRDevicePairingManagerMux updateAdditionalDataForPairingManager:additionalData:withCompletion:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _nrXPCKeyAdditionalData
+ _objc_msgSend$additionalData
+ _objc_msgSend$setAdditionalData:
+ _objc_msgSend$startPairingDevice:additionalData:withCompletion:resultBlock:
- -[NRDevicePairingManagerMux startPairingForPairingManager:pairingTarget:withCompletion:]
- GCC_except_table703
- GCC_except_table711
- GCC_except_table716
- GCC_except_table720
- GCC_except_table724
- GCC_except_table730
- GCC_except_table738
- GCC_except_table742
- GCC_except_table765
- GCC_except_table768
- GCC_except_table772
- GCC_except_table777
- GCC_except_table779
- GCC_except_table781
- GCC_except_table783
- GCC_except_table788
- GCC_except_table790
- GCC_except_table846
- GCC_except_table848
- GCC_except_table863
- ___72-[NRDevicePairingManager startPairingDevice:withCompletion:resultBlock:]_block_invoke
- ___72-[NRDevicePairingManager startPairingDevice:withCompletion:resultBlock:]_block_invoke_2
- ___72-[NRDevicePairingManager startPairingDevice:withCompletion:resultBlock:]_block_invoke_3
- ___88-[NRDevicePairingManagerMux startPairingForPairingManager:pairingTarget:withCompletion:]_block_invoke
CStrings:
+ "%@: additionalData length %lu exceeds maximum of %lu bytes"
+ "%s%.30s:%-4d Update additional data could not deliver message %@, error %@"
+ "%s%.30s:%-4d Update additional data received unexpected XPC object: %@"
+ "%s%.30s:%-4d Update additional data request with no XPC connection"
+ "-[NRDevicePairingManager startPairingDevice:additionalData:withCompletion:resultBlock:]"
+ "-[NRDevicePairingManager startPairingDevice:additionalData:withCompletion:resultBlock:]_block_invoke_2"
+ "-[NRDevicePairingManager updateAdditionalData:withCompletion:]"
+ "-[NRDevicePairingManagerMux startPairingForPairingManager:pairingTarget:additionalData:withCompletion:]"
+ "-[NRDevicePairingManagerMux startPairingForPairingManager:pairingTarget:additionalData:withCompletion:]_block_invoke"
+ "-[NRDevicePairingManagerMux updateAdditionalDataForPairingManager:additionalData:withCompletion:]"
+ "-[NRDevicePairingManagerMux updateAdditionalDataForPairingManager:additionalData:withCompletion:]_block_invoke"
+ "AdditionalData"
+ "Update additional data received unexpected XPC object"
+ "Update additional data response missing or invalid result"
+ "additionalData"
- "-[NRDevicePairingManager startPairingDevice:withCompletion:resultBlock:]"
- "-[NRDevicePairingManager startPairingDevice:withCompletion:resultBlock:]_block_invoke_2"
- "-[NRDevicePairingManagerMux startPairingForPairingManager:pairingTarget:withCompletion:]"
- "-[NRDevicePairingManagerMux startPairingForPairingManager:pairingTarget:withCompletion:]_block_invoke"
```
