## com.apple.driver.ApplePearlSEPDriver

> `com.apple.driver.ApplePearlSEPDriver`

```diff

-873.40.6.0.0
+873.40.8.0.0
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0xa733
-  __TEXT.__os_log: 0x48a5
-  __TEXT_EXEC.__text: 0x3fd40
+  __TEXT.__cstring: 0xa805
+  __TEXT.__os_log: 0x48b0
+  __TEXT_EXEC.__text: 0x402ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

   __DATA_CONST.__const: 0x2050
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 9DD37D35-379F-31C4-B3D1-90EE6936028E
+  UUID: 50E3F9D0-2E0D-3D64-A418-B252D4215D61
   Functions: 624
   Symbols:   0
-  CStrings:  1655
+  CStrings:  1663
 
Functions:
~ sub_fffffe00099a9470 -> sub_fffffe00099c6d30 : 256 -> 268
~ sub_fffffe00099a9578 -> sub_fffffe00099c6e44 : 2624 -> 2768
~ sub_fffffe00099a9fb8 -> sub_fffffe00099c7914 : 2624 -> 2768
~ sub_fffffe00099aaafc -> sub_fffffe00099c84e8 : 292 -> 304
~ sub_fffffe00099c1ddc -> sub_fffffe00099df7d4 : 332 -> 308
~ sub_fffffe00099c8f98 -> sub_fffffe00099e6978 : 2460 -> 3600
~ sub_fffffe00099c9fb4 -> sub_fffffe00099e7e08 : 1288 -> 1152
~ sub_fffffe00099cf8e8 -> sub_fffffe00099ed6b4 : 1976 -> 1952
~ sub_fffffe00099d2630 -> sub_fffffe00099f03e4 : 1728 -> 1812
~ sub_fffffe00099d9f18 -> sub_fffffe00099f7d20 : 16 -> 40
~ sub_fffffe00099d9f38 -> sub_fffffe00099f7d58 : 40 -> 16
~ sub_fffffe00099da038 -> sub_fffffe00099f7e40 : 12 -> 24
~ sub_fffffe00099da044 -> sub_fffffe00099f7e58 : 24 -> 12
~ sub_fffffe00099e1740 -> sub_fffffe00099ff548 : 352 -> 368
~ sub_fffffe00099e215c -> sub_fffffe00099fff74 : 648 -> 576
~ sub_fffffe00099e2fa8 -> sub_fffffe0009a00d78 : 224 -> 232
~ sub_fffffe00099e33e4 -> sub_fffffe0009a011bc : 228 -> 236
~ sub_fffffe00099e35ac -> sub_fffffe0009a0138c : 6956 -> 6948
~ sub_fffffe00099e5270 -> sub_fffffe0009a03048 : 320 -> 328
~ sub_fffffe00099e55ac -> sub_fffffe0009a0338c : 1196 -> 1264
~ sub_fffffe00099e5c44 -> sub_fffffe0009a03a68 : 196 -> 204
CStrings:
+ "%s -> err:0x%x (skipped:%d)\n"
+ "%s: %s (%d), cameraState:%s (%d)\n"
+ "12111112122212121121211111111111111111111121121122222222122211222222221211121111121222211121211122222222222221122222222221221112111211222111222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222221221222222221212222222222122212222222222222222121211222222221221222122111122222222112122223111222122122111111111112112221112"
+ "_ariesEphPublicKeySignature"
+ "_ariesEphPublicKeySignature->getLength() == sizeof(sessionPrepareResponse.ariesEphPublicKeySig)"
+ "_ariesEphPublicKeyX"
+ "_ariesEphPublicKeyX->getLength() == sizeof(ariesEphPublicKey->x)"
+ "_ariesEphPublicKeyY"
+ "_ariesEphPublicKeyY->getLength() == sizeof(ariesEphPublicKey->y)"
+ "data->getLength() == ((256 / 8) * 2)"
+ "data->getLength() == (256 / 8)"
+ "messageInfo"
- "12111112122212121121211111111111111111111121121122222222122211222222221211121111121222211121211122222222222221122222222221221112111211222111222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222221221222222221212222222222122212222222222222222121211222222221221222122111122222222112122223111222122122111111111112112222"
- "data->getLength() == sizeof(ariesEphPublicKey->x)"
- "data->getLength() == sizeof(ariesEphPublicKey->y)"
- "data->getLength() == sizeof(sessionPrepareResponse.ariesEphPublicKeySig)"

```
