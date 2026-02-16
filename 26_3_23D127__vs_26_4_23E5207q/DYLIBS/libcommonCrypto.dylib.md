## libcommonCrypto.dylib

> `/usr/lib/system/libcommonCrypto.dylib`

```diff

 600035.0.0.0.0
-  __TEXT.__text: 0xb498
+  __TEXT.__text: 0xb304
   __TEXT.__auth_stubs: 0xd60
   __TEXT.__cstring: 0x2fc
-  __TEXT.__const: 0x28c
+  __TEXT.__const: 0x24c
   __TEXT.__oslogstring: 0x19
-  __TEXT.__unwind_info: 0x3f0
-  __TEXT.__eh_frame: 0x40
+  __TEXT.__unwind_info: 0x3e0
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x740
   __AUTH_CONST.__auth_got: 0x6b0

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 235BE85D-6C59-3D15-8F10-D0AA89ADB4EA
-  Functions: 355
-  Symbols:   821
+  UUID: 9FBDB16D-976B-3C60-9FD1-FC4E228D6E7E
+  Functions: 357
+  Symbols:   829
   CStrings:  52
 
Symbols:
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
Functions:
~ _CNEncode : 208 -> 220
~ _ccdigest_finalize : 240 -> 216
~ _ccdigest_process : 220 -> 212
+ _OUTLINED_FUNCTION_3
~ _enCode : 492 -> 496
~ _CNBufferRelease : 60 -> 64
~ _CCCryptorCreateWithMode : 1264 -> 1216
~ _ccClearCryptor : 256 -> 236
~ _CCCrypt : 276 -> 300
~ _dump_crc_table : 468 -> 464
~ _CCCKGConvertNativeToECCryptor : 192 -> 180
~ _OUTLINED_FUNCTION_2 : 28 -> 48
+ _OUTLINED_FUNCTION_4
~ _ccECpairwiseConsistencyCheck : 212 -> 216
~ _CCECCryptorExportKey : 260 -> 256
~ _CCCalibratePBKDF : 736 -> 416
~ _CCRSACryptorVerify : 352 -> 344
~ _cccbc_getiv : 76 -> 72
~ _deCode : 332 -> 340
~ _getDesc.cold.1 : 308 -> 208
~ _CCRSAGetCRTComponents : 580 -> 592
~ _CNEncoderBlocksize : 160 -> 164

```
