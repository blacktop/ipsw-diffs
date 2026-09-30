## com.apple.driver.AppleHIDTransportFIFO

> `com.apple.driver.AppleHIDTransportFIFO`

```diff

-9140.6.0.0.0
+10100.34.0.0.0
   __TEXT.__const: 0x8 sha256:3e990d45c83fa01d9bf0c64b79ed7678df3c723614f0f7eccdc3d196fa3073e9
-  __TEXT.__cstring: 0x2b37 sha256:0c83c3b31dd034b87406c10d0d796925837ae217d27a42e52527e73886727a63
-  __TEXT_EXEC.__text: 0x135c0 sha256:27f6cafa69dcc343301eea0ed63eb3fc1ec64bd89c71a0388a575ebd1a4d6460
+  __TEXT.__cstring: 0x2be6 sha256:d1fe4915519b895a01499434463f7ffa57ad23c1fd7cda6a77e5ff0151a9a321
+  __TEXT_EXEC.__text: 0x13674 sha256:3aec2d457df8c60f04f3b9dc33f571a17671017a066d8e2ae9c45689a5118a26
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:e2a0ef90b2a8edd272e4fa0eba0cb91cfdcb5dc000ca2cd3ff02221b4fa3256c
+  __DATA.__data: 0xc8 sha256:94c7ca5940a305c6669c73b8ef11d5b7604207bccbb535d52fd8f06238fa269f
   __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
   __DATA.__bss: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
-  __DATA_CONST.__auth_got: 0x1e0 sha256:4bd81b0e1c74a709ce1be6106709197a7dc48ff11c88fe4c3398a2a3ce127438
-  __DATA_CONST.__got: 0xb8 sha256:99245dde428766e3b984576a481e1a341be7bbb580b4053f1d83e8d50100bd66
-  __DATA_CONST.__mod_init_func: 0x10 sha256:152e64d8386e0d1749602d3ab48c983be2b4c791ba37e8ae07ab3a514a3be022
-  __DATA_CONST.__mod_term_func: 0x10 sha256:c4ab03257eb225b23397aaf83e38a80baeb5270fd63220bdd4eb9b13b3c27a0b
-  __DATA_CONST.__const: 0x10a8 sha256:72dbe2114340c3ddb3f0a81445b31f6b842234e28835d187622f49160f76a63b
-  __DATA_CONST.__kalloc_type: 0x2c0 sha256:1d6c381c7bf82a36583364e89dc21395ac3743de9c7dc48b8459756bd9468225
-  UUID: 2EC831B3-013C-37E9-99AB-462A51159E9C
-  Functions: 324
+  __DATA_CONST.__mod_init_func: 0x10 sha256:d5de76ecb15f618f261c22d89c683fe0eb0b3f08b94c43d6d0a15314b1eaa9a5
+  __DATA_CONST.__mod_term_func: 0x10 sha256:46a5ceaaf16021042bffd09c113681f049851c4cb654b93f5ad8092fb6375dc1
+  __DATA_CONST.__const: 0x10f8 sha256:5f795d99e7d2c43882878008be3daf5d9a0b428c5a3e53058ba07e4df4ffbe51
+  __DATA_CONST.__kalloc_type: 0x2c0 sha256:dda6133ea36820d11cfff40d94d7760d89c4bddab3fc407938285431828beabb
+  __DATA_CONST.__auth_got: 0x1f0 sha256:6bc4102abb8e261a4b6dbaafb1e77b034744c0f6222dd5e554110acf2948cb2b
+  __DATA_CONST.__got: 0xb8 sha256:eeb9b43c176bdd5d19b86016aa2411665f901818acd31143887d4edb8ca60045
+  UUID: 8BDE21FE-C193-3B3F-A0E1-1258D32FC69A
+  Functions: 328
   Symbols:   0
-  CStrings:  288
+  CStrings:  289
 
CStrings:
+ "\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u, report ID 0x%02X, transfer ID 0x%02X: invalid checksum (read: 0x%08X, calculated: 0x%08X)\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: header size too large\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: message exceeds capacity %llu bytes\" @%s:%d"
+ "\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: read beyond message boundary\" @%s:%d"
+ "121111121222121211111211122112111112111121"
+ "Off Without Reset"
+ "ret == kIOReturnSuccess"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: header size too large\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: invalid checksum\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: message exceeds capacity %llu bytes\" @%s:%d"
- "\"[%s::%s] Invalid message read from the FIFO ID %d: read beyond message boundary\" @%s:%d"
- "12111112122212121111121112211211112111121"
- "ret == 0"

```
