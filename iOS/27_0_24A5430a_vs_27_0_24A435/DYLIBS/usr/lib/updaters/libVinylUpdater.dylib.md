## libVinylUpdater.dylib

> `/usr/lib/updaters/libVinylUpdater.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

 178.0.0.0.0
-  __TEXT.__text: 0x4d594
+  __TEXT.__text: 0x4d590
   __TEXT.__init_offsets: 0x48
   __TEXT.__const: 0x53f1
   __TEXT.__gcc_except_tab: 0x47b4

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1295
+  Functions: 1296
   Symbols:   2145
   CStrings:  1279
 
Functions:
~ _OUTLINED_FUNCTION_2 : 12 -> 20
+ _OUTLINED_FUNCTION_3
~ __ZN5eUICC15VinylPollResultINS_18VinylManagePairing8ResponseUt_EEEiR13HDLCFrame_tagRT_P26TelephonyUtilTransport_tagjbjNSt3__18functionIFbRKS6_EEE : 428 -> 424
~ __ZN5eUICC15VinylPollResultINS_18VinylValidatePerso8Response8contentsEEEiR13HDLCFrame_tagRT_P26TelephonyUtilTransport_tagjbjNSt3__18functionIFbRKS6_EEE : 428 -> 424
~ __ZN5eUICC15VinylPollResultINS_22VinylLPASigningRequest8Response8ContentsEEEiR13HDLCFrame_tagRT_P26TelephonyUtilTransport_tagjbjNSt3__18functionIFbRKS6_EEE : 428 -> 424
~ __ZNSt3__13mapIPK10__CFStringNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4lessIS3_EENS7_INS_4pairIKS3_S9_EEEEEC2B9nqe220106ESt16initializer_listISE_ERKSB_ : 84 -> 88
~ _OUTLINED_FUNCTION_9 : 12 -> 20
~ _OUTLINED_FUNCTION_10 : 20 -> 12
~ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE17VinylRefurbActionN15BBUpdaterCommon29case_insensitive_key_comparerENS4_INS_4pairIKS6_S7_EEEEEC2B9nqe220106ESt16initializer_listISC_ERKS9_ : 84 -> 88
~ __Z13_BBULogBinary9LogModuleiPKcS1_PKvmc : 600 -> 604
~ __ZN22VinylDaleCommunication15createTransportEP26TelephonyUtilTransport_tag.cold.4 : 112 -> 96
~ __ZN22VinylDaleCommunication11openChannelEP26TelephonyUtilTransport_tag.cold.1 : 124 -> 108
CStrings:
+ "VinylRestore-178~7453"
- "VinylRestore-178~7655"
```
