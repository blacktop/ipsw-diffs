## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

```diff

-230.0.0.0.0
-  __TEXT.__text: 0xec0 sha256:adda91f557628e827cc480fe912f271b1d15d9df24da5341b88d3e7a3bfaeb63
+233.0.0.0.0
+  __TEXT.__text: 0xebc sha256:3ef63302b113767973f5310b64b644e2f481505cdb9204837f070f86bd2f2628
   __TEXT.__auth_stubs: 0x150 sha256:7092fc49c017a00507d0515f333fc89d2a081e25cb658baf67c19e093f80c491
-  __TEXT.__init_offsets: 0x4 sha256:18a81924dae099de83de4331bbd155b2105592df60a24e0bfd4ea3a9263544df
+  __TEXT.__init_offsets: 0x4 sha256:a972c2efa2d12e39e071289707c123e20011326d1de401d009a93ca32fa266f0
   __TEXT.__gcc_except_tab: 0x68 sha256:bc11842433f4688049b7228e999ec003280945f875ca59d1749da8354d1ae549
   __TEXT.__const: 0x98 sha256:0ebac02ed5ee2308dd982ed6d171d5b22b310ddbd6ff712e707a520ca11f3d99
-  __TEXT.__cstring: 0x339 sha256:a43414dea757b91419323c1ce5d1f803c63f9420eb94d264afa0753a87dc9829
-  __TEXT.__unwind_info: 0xb8 sha256:a827674bcd1e8cba041c3bfe0c234fb74835f763dcf89a5aab5c6f22c11e26fe
+  __TEXT.__cstring: 0x33a sha256:6dfed54bfc853d70a66848ef1b403a3d8b0b994fc69da3f3ff1eff3df82f4c6f
+  __TEXT.__unwind_info: 0xb8 sha256:0a832425b131d2bccc636b3c8e0b8eecd665715ae3dc25f05c4efa4a250afbba
   __DATA_CONST.__auth_got: 0xb0 sha256:f2b11f30ce0a46689898179d0edd91ee86f0772b1b9b7f5394981e90aad237ad
   __DATA_CONST.__got: 0x28 sha256:994b467850dde56b18d22a8d3ae4ab3692dda43b28e8c84f10ac56d73b43cd16
   __DATA.__bss: 0x48 sha256:d9c8ba4eef7f67f8d195d579dada471da4b26c5e4a73ab877ea0da3ee77d45aa

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 1C19F1AC-2F2E-385A-AD1E-B6EAC65AF2B8
+  UUID: 56CEE178-3CA3-37BA-9F44-D5E604C71478
   Functions: 15
   Symbols:   112
   CStrings:  20
Functions:
~ sub_100000720 : sha256 9cc4385264efe470f4ef7d7965a91440ee8160f1ec1ad90e80a43ff7991154c0 -> f8f85c09c1f39c9cca6065e350aff6f25ec3c9dca6d72f9a58b1a594a9be9aae
~ sub_100000b50 : sha256 2fdceff0d87e469e8d4f8dc0bb90da81b6fef6e25f230c9515ba9f42ab58f39c -> 9f61a6661b4d37efc563db545805fea5e37b801487b25c593db0fce7d14e3f3b
~ sub_100000b94 : 168 -> 164
~ sub_100000c40 -> sub_100000c3c : sha256 dd09bccc395c2b37e5afd179b5898b31b793f59ec041fcf4dadbf66078c768b7 -> 2c0c0a6e01d9606047d8a85152a986cac1b08f899367964ec81b84d1bfc36f46
~ sub_100000d94 -> sub_100000d90 : sha256 e3aa56338189d2a003c802b05c86cbf940577ea36237938453c000dfd5e00938 -> e288efbdb5d656bb891d2f357e8afbcd60487b664465eae518be8267602def82
~ sub_100000ec8 -> sub_100000ec4 : sha256 0bca90b41873f3b8782ba8121aa120409ceed04714a74b2bfe0eef92f40c1013 -> dcaff103c1398bc2c8e58ef7db3433a99ec45d02714f85bbfe10b643442dac58
~ sub_10000100c -> sub_100001008 : sha256 c01e16b742329a7911533d334d6c68918be720637b730c880f62de2b85475d5e -> 45eb4adb1c26fbf8612ae3c2ea760fb32b46cb126444ceda2fe034559188eebc
~ sub_1000011a4 -> sub_1000011a0 : sha256 cdb0ea4e2b80210ad0fab416b67b36bced127d8abdde1f8545ec0cc2a7084908 -> 51fef92883a422701db9eba495a78c10e0c2007b67dcd1921ddb60bc0be5f350
~ sub_1000012a8 -> sub_1000012a4 : sha256 17e3d507feb58e223dc4affe2cb43699fe2bb19814bf2b2d02f377a716b9cd83 -> 58b6ec9f8d2aea16394988b6a620fac5bfeb2c10e463868681e929552cd42781
~ sub_1000013a4 -> sub_1000013a0 : sha256 f140621971eb01bd48fc26b8492f14133aabbf683bad535a4d7e0d6b2a1266ff -> 9ceb8a53fd319367351fdcbb07041cd9480d58e40a0cf16babbd846692504df7
~ sub_100001538 -> sub_100001534 : sha256 8302d2e345811c4e99ff970625f6ebb78ce83d3d99c1fd63b27ca0364388b9d1 -> eb99eb0ba8936a2bd0d71eea174140ef547b00cf2044647e5dc78c28cdbdfc87
CStrings:
+ "Failed to update permissions to %04o and/or user/group ownership to %d/%d for '%s'.\n"
- "Failed to update permisions to %04o and/or user/group ownership to %d/%d for '%s'.\n"

```
