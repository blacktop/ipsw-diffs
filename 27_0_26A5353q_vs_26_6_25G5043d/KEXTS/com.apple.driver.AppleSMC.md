## com.apple.driver.AppleSMC

> `com.apple.driver.AppleSMC`

```diff

-790.0.0.0.0
-  __TEXT.__cstring: 0x8564 sha256:bee61567b75e4244265dcb0ddd71ad66c46943e730c0dfaf0c1d1f2c56af7ffc
-  __TEXT.__const: 0x220 sha256:a2698cb33505f37880f3d3c57fa58fb5f98082f6c4ca8823ab21614015ed40ef
+752.160.2.0.0
+  __TEXT.__cstring: 0x83bb sha256:8a4835a96aede073b04804794379ccfc329470f8e39b804dc962fda7a56d6b4b
+  __TEXT.__const: 0x1d0 sha256:b428f09331fb474976f01b4ec3a4f7ca8e8c3cb0e5b2aa85a9cf320f962cfb67
   __TEXT.__os_log: 0xd97 sha256:eefc199526b18cb47c89ee1f05805b2ab26e3cde97f5b1374c4c38836ff25037
-  __TEXT_EXEC.__text: 0x27e50 sha256:057161473530668a293f6615656db0a311a36c5267207444ce03c40b44d9d4a3
+  __TEXT_EXEC.__text: 0x271c4 sha256:fa23f50b867757e30e746917d11e2308158a06f2fa9f28d2f5aaee5d4dd1263f
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xcc sha256:40fb0247d80ae763603e87ec4a91fd9bac12580d8ee2b888743a96dc4f654e83
+  __DATA.__data: 0xcc sha256:0d4ac2f45c580635d3912384fedac3f3a46c82a546c6d17540c93c67983f2b13
   __DATA.__common: 0x490 sha256:4717e5fb82c0ee85a7c97d022f410990a62efa2492070e42385cfeab67afd619
   __DATA.__bss: 0xd0 sha256:46f531b7ea0428fbf2c3ca2b60e8dc33d6bbfa000e0fd1b489c5e39140a47006
-  __DATA_CONST.__mod_init_func: 0xb8 sha256:ec628d7398d33405df04c11824b7d4a6af10781ca54f521110c3127ad9de8334
-  __DATA_CONST.__mod_term_func: 0xa8 sha256:91de0d1b4500b5c7b45aa2c4e9c7485c2ff4a4a4ceadff25ebd3c7423c356489
-  __DATA_CONST.__const: 0xd8d0 sha256:876485fb8753154bb97da60374552ae9a27d8e871c5459e02a2b727437e3d7be
-  __DATA_CONST.__kalloc_type: 0x700 sha256:802e13655a664c34a86881b44a5ba9cf95d534d3d8ce604d2b24df0fd8034631
-  __DATA_CONST.__kalloc_var: 0xa0 sha256:5f9ad020f545d835c6e06fd615eb12c4b60de5d8bedf3df16064a7056a2c8af6
-  __DATA_CONST.__auth_got: 0x4f0 sha256:48779d8c25f715628a20e48bd6aee72f19ca9e61935eee2daa03789156295306
-  __DATA_CONST.__got: 0x1d0 sha256:64a3497af0792e5ece4958982aa7930dafdbfc3c7b3a921ccccd4e651d6d26b7
-  __DATA_CONST.__auth_ptr: 0x8 sha256:375914cac8d644d21d11abffa5d06ef2754db87c98466d75541f07a113c94784
-  UUID: 52250049-131C-3975-9812-D97B6687AF73
-  Functions: 890
-  Symbols:   1829
-  CStrings:  1033
+  __DATA_CONST.__auth_got: 0x4f0 sha256:83cc718500aa62f8aebcb5dff087bb72428faaa722d59dbb9f006bcd04531865
+  __DATA_CONST.__got: 0x1c8 sha256:c3ae8a1adaaaaee592fe4a6cbe6b349e35debd07f0958aea89570ab92b99ed6e
+  __DATA_CONST.__auth_ptr: 0x8 sha256:aa15fecf180757029ca252ddb0adce474746370661afb2af34032c595a37b2b6
+  __DATA_CONST.__mod_init_func: 0xb8 sha256:d6c350daf5b4572536beee61bdb1c97197e2a9cc2bb1aed09323835f0afa7692
+  __DATA_CONST.__mod_term_func: 0xa8 sha256:e289eee1ec8ccef9b2b5d24cf7de8e4848d537290c95445f613d12d38b149823
+  __DATA_CONST.__const: 0xd8a8 sha256:047758d819167643b4dd2613f29829a4b074af60863a53fda98182cb8fa66a84
+  __DATA_CONST.__kalloc_type: 0x700 sha256:dd567ee0059aac0af87af8a21cb033af5df5cfe740d7e97ebc6e23d481a9c0cc
+  __DATA_CONST.__kalloc_var: 0xa0 sha256:9530e768094495b9bad286c218ca3326335fb01782cb1b092db7babae6a93250
+  UUID: F02C556B-E72B-3A89-82D0-89A2BDA17E8F
+  Functions: 883
+  Symbols:   1817
+  CStrings:  1020
 
Symbols:
- __ZN16AppleARMFunction8DispatchE5IORPC
- __ZN18IOAccessoryManager12_getPortTypeEv
- __ZN20AppleSMCKeysEndpoint17_getKeyInfoCachedEjP14SMCKeyInfoData
- __ZN20AppleSMCKeysEndpoint19_updateKeyInfoCacheEjP14SMCKeyInfoData
- __ZN20AppleSMCKeysEndpoint20_updateKeyIndexCacheEjPj
- __ZN20AppleSMCKeysEndpoint21_smcInitKeyTableCacheEv
- __ZN20AppleSMCKeysEndpoint22_getKeyFromIndexCachedEjPj
- __ZN20AppleSMCKeysEndpoint4stopEP9IOService
- __ZN28RTBuddyBinaryLogEntryHandler17processSourceInfoEP13logSourceInfoP8OSStringS3_
- __ZN8AppleSMC16smcSendPanicDataEP21PE_panic_save_context
- __ZZL24key_requires_entitlementjE13wildcard_keys
- _kOSBooleanFalse
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRehugAhPRKGL2sovwNHa0o_Ka2KN4erX_krqA4/Library/Caches/com.apple.xbs/TemporaryDirectory.PFJ6Jz/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCACAMDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugAhPRKGL2sovwNHa0o_Ka2KN4erX_krqA4/Library/Caches/com.apple.xbs/TemporaryDirectory.PFJ6Jz/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCBinaryLogDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugAhPRKGL2sovwNHa0o_Ka2KN4erX_krqA4/Library/Caches/com.apple.xbs/TemporaryDirectory.PFJ6Jz/Sources/AppleSMC/AppleSMCEmbedded.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugAhPRKGL2sovwNHa0o_Ka2KN4erX_krqA4/Library/Caches/com.apple.xbs/TemporaryDirectory.PFJ6Jz/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCCharger.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugAhPRKGL2sovwNHa0o_Ka2KN4erX_krqA4/Library/Caches/com.apple.xbs/TemporaryDirectory.PFJ6Jz/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCChargerUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugAhPRKGL2sovwNHa0o_Ka2KN4erX_krqA4/Library/Caches/com.apple.xbs/TemporaryDirectory.PFJ6Jz/Sources/AppleSMC/AppleSMCEmbeddedFunctions.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugAhPRKGL2sovwNHa0o_Ka2KN4erX_krqA4/Library/Caches/com.apple.xbs/TemporaryDirectory.PFJ6Jz/Sources/AppleSMC/AppleSMCEmbeddedPMU/AppleSMCPMU.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRehugAhPRKGL2sovwNHa0o_Ka2KN4erX_krqA4/Library/Caches/com.apple.xbs/TemporaryDirectory.PFJ6Jz/Sources/AppleSMC/AppleSMCKeysEndpoint.cpp"
+ "1211111212221212111212111111111121111222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222"
+ "1211111212221212111212111111111121111222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222111222"
+ "22:53:27"
+ "22:53:29"
+ "Jun  9 2026"
+ "performCommandV2"
- "%s: Error reading key count. Status: %s\n"
- "%s: Number of keys on this target: %d\n"
- "/AppleInternal/Library/BuildRoots/4~CQdZugB2gduEwNwocUxNRpyokMEweqWYRm2lpjc/Library/Caches/com.apple.xbs/TemporaryDirectory.gvLpud/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCACAMDriver.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugB2gduEwNwocUxNRpyokMEweqWYRm2lpjc/Library/Caches/com.apple.xbs/TemporaryDirectory.gvLpud/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCBinaryLogDriver.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugB2gduEwNwocUxNRpyokMEweqWYRm2lpjc/Library/Caches/com.apple.xbs/TemporaryDirectory.gvLpud/Sources/AppleSMC/AppleSMCEmbedded.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugB2gduEwNwocUxNRpyokMEweqWYRm2lpjc/Library/Caches/com.apple.xbs/TemporaryDirectory.gvLpud/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCCharger.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugB2gduEwNwocUxNRpyokMEweqWYRm2lpjc/Library/Caches/com.apple.xbs/TemporaryDirectory.gvLpud/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCChargerUtil.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugB2gduEwNwocUxNRpyokMEweqWYRm2lpjc/Library/Caches/com.apple.xbs/TemporaryDirectory.gvLpud/Sources/AppleSMC/AppleSMCEmbeddedFunctions.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugB2gduEwNwocUxNRpyokMEweqWYRm2lpjc/Library/Caches/com.apple.xbs/TemporaryDirectory.gvLpud/Sources/AppleSMC/AppleSMCEmbeddedPMU/AppleSMCPMU.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugB2gduEwNwocUxNRpyokMEweqWYRm2lpjc/Library/Caches/com.apple.xbs/TemporaryDirectory.gvLpud/Sources/AppleSMC/AppleSMCKeysEndpoint.cpp"
- "01:29:56"
- "01:29:58"
- "12111112122212121112121111111111211112222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222"
- "1211111212221212111212111111111121111222211111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222211122211112"
- "AppleSMC received kPEPanicDataSend\n"
- "ERROR: Key table cache not properly initialized (%s).\n\n"
- "Failed to get SMC key LGWT (%s)\n"
- "Failed to receive panic write done before timeout\n"
- "Failed to write SMC key LGSD (%s)\n"
- "FullWake PwrState Event\n"
- "Invalid LGWT value %llu\n"
- "LowPowerWake PwrState Event\n"
- "May 27 2026"
- "SLP_MEDIA"
- "_smcInitKeyTableCache"
- "bmc_remote_mgmt"
- "performCommandV3"

```
