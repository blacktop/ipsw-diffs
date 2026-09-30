## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

```diff

-550.48.0.0.0
-  __TEXT.__const: 0x21d8 sha256:ff37e270197c76d1014b804c58324e8d593e11645302f93ebf9c629683ea7995
-  __TEXT.__os_log: 0x9823 sha256:f089055cd6d50a38469fdbfcce8f7a15908d10f7ab19df44df7783662c3be2a9
-  __TEXT.__cstring: 0x10cf sha256:2553024edf3bd2750cf77d445d5b5d1629abef7dd3a6e96bcae166ebbeba40dc
-  __TEXT_EXEC.__text: 0x3dd44 sha256:ae2272afbbc765723dc6d383a1608ae455629eb3643f8631c540438d763b9d56
+600.24.1.0.0
+  __TEXT.__const: 0x2378 sha256:db78982f7b0778094fec911af258a58983ae839ac24898a6fbe94a95bfee69b8
+  __TEXT.__os_log: 0x9ab8 sha256:19c8d8183c2413e9c9d1544c772ae2ac6d7fbfe3668448b22b942a69ec1fd099
+  __TEXT.__cstring: 0x112a sha256:621bc0fbe506a6ad7d11c4e994f227f51dc4b64c51203f5d3a2b977ece65996c
+  __TEXT_EXEC.__text: 0x4e148 sha256:2d583aa86e451bbc6bf1a309094b6f175eefd2ea5f8f311cfc36aecc87cc09f4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x408 sha256:f58d19d12980af16c981cc2088e155780264278062a7037f6275d4db5a0ec1e9
-  __DATA.__common: 0x70 sha256:b5fdab78d8947eacc864bfeecb4d2100780e5afe1cd8efafb124887913ac49fa
-  __DATA.__bss: 0x6cc0 sha256:81e9b3c2b5f9651b76e804066bbbd2c661e98e238694134bf600bfa859259cd7
-  __DATA_CONST.__auth_got: 0x2d8 sha256:1ab1d5cf3712030559d262b4091a991273b3a5dfc0f9aebd32d8ab4bdcc70069
-  __DATA_CONST.__got: 0x60 sha256:897f033de17082daa66aa1e04b97c68bf1c4d4ca3d364b419177d6f6ca27769c
-  __DATA_CONST.__mod_init_func: 0x10 sha256:48c0384b2951f23da3ac8c2ccae5373b8c59d5911121b28a7655a39244d245d1
-  __DATA_CONST.__mod_term_func: 0x10 sha256:04a506064e7e3e4a2d79ce2bc2536c9817bb72de603c3dea608d955c1239bc68
-  __DATA_CONST.__const: 0xa140 sha256:7b294e3dafdfeb92ef4a95e61286e9ae53f88b0cdaa205c0e8ee5f4a45baf56c
-  __DATA_CONST.__kalloc_type: 0x480 sha256:91217e6b8fb18047b62b266c0292cf9fb7dab0f72a9e46b1c332db8ec825222b
-  __DATA_CONST.__kalloc_var: 0x140 sha256:f711a6ad760ea222cc4c5ebce5806e0432a4555f4f099b0ec081177f6653d854
-  UUID: 79BD27DE-66E8-386C-BEA6-210702229DC6
-  Functions: 2049
+  __DATA.__data: 0x448 sha256:48f4f3968f77cea35f2a233ce260e513cfa6321b2fb7428492faa6f9c25e1c7c
+  __DATA.__common: 0x78 sha256:6edd9f6f9cc92cded36e6c4a580933f9c9f1b90562b46903b806f21902a1a54f
+  __DATA.__bss: 0x9a20 sha256:00cfa53b849b1ee01cab49a7c68c2e486dafdd09b4bf832209b4734ca340eefc
+  __DATA_CONST.__mod_init_func: 0x10 sha256:483e0d1dd03a504929c3f6120800cec6505f3c51df0d7d77d8c762dc9ee28dcd
+  __DATA_CONST.__mod_term_func: 0x10 sha256:649cdb0bf402e578af78bfcae9676a3e8e5076075315e0cb5aff23a1cf0216b1
+  __DATA_CONST.__const: 0xb190 sha256:9662ba8024ad1a2ba6f57059b6b0913ebb28ef163e1763007a7891fd39a0be86
+  __DATA_CONST.__kalloc_type: 0x480 sha256:35fe33e9b68334e89a3ee610ad196f4a46e2e2d2bbb409450b69fe663acfb90b
+  __DATA_CONST.__kalloc_var: 0x140 sha256:7491d24331e0baea68f6b7e73a75e476626179903eb7fa6c1755e0997a20af45
+  __DATA_CONST.__auth_got: 0x2f0 sha256:1820b80fc19ba7a01c6b480a7713215b7d62c59c94f295b2644920acf6367df1
+  __DATA_CONST.__got: 0x60 sha256:b1c0b6aea77104b42c7520f499352774077b6d466815d9dea69ea604b857e3da
+  UUID: 6FD4E527-24B1-3D3C-B4A8-33190F4E22F4
+  Functions: 2758
   Symbols:   0
-  CStrings:  535
+  CStrings:  553
 
CStrings:
+ "/"
+ "AppleProResHW (0x%x): %s(): (AXI2AF) tunables are set at iBoot for DevID %d coreIndex %d"
+ "AppleProResHW (0x%x): %s(): aprDeviceEnabled boot-arg value %u is invalid (must be 0 or 1), ignoring"
+ "AppleProResHW (0x%x): %s(): isFastsim %d targetType:%.*s"
+ "AppleProResHW (0x%x): %s(): psd_die_id = %d on m_eDevID = %d corIdx = %d\n"
+ "ERROR AppleProResHW: %d: %s(): DevID %d not enabled; exiting without registering\n"
+ "ERROR AppleProResHW: %d: %s(): aprDeviceEnabled=0: driver disabled via boot-arg, exiting without registering\n"
+ "ap"
+ "aprDeviceEnabled"
+ "dev"
+ "getPsdServiceDieID"
+ "isFastsimPlatform"
+ "q0"
+ "r0"
+ "r1"
+ "r2"
+ "sim"
+ "target-type"

```
