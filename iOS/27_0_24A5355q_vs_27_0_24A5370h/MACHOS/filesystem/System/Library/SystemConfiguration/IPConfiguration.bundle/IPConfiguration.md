## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

```diff

-551.0.0.0.0
-  __TEXT.__text: 0x5c984 sha256:17d747d24da3af95ba831d48ad34f116196ae8723d8ffb86741c9a93ca571ab8
-  __TEXT.__auth_stubs: 0x1070 sha256:5f8a7e2d64058625fc7f91b6922603bc5daa704d1847d169cf9b8e1df21325a4
-  __TEXT.__const: 0x300 sha256:c36b8d1b5c13f74c5387beb879432f4b886bc6916a13e09d01a67aacbccce7df
-  __TEXT.__oslogstring: 0x61a9 sha256:872d8904fcfff3f36b006560eb8e2de71133c0960b2b3fb76ae88960ad9c3fc5
-  __TEXT.__cstring: 0x4226 sha256:c72abe7ca8cca5c03887c2dd11d27427354478d80d58612eac0eb937dd3004dd
-  __TEXT.__unwind_info: 0xc48 sha256:91ccb017b92e26de10ac06fd9cd2024b282d86ef701e554c50df93054034c0b0
-  __DATA_CONST.__const: 0x1dc8 sha256:76817e2a479eedfb8f1790ca1f61b001cd8a3309e00a8332e64786ebb9bc4312
-  __DATA_CONST.__cfstring: 0x2b20 sha256:0ee38f39d7b81cab995e9b26897b14b6e75f907afece6e7deef40e9a61bb9ad7
+553.0.0.0.0
+  __TEXT.__text: 0x5cad8 sha256:ca73c7bb4771c0ce15f3a0b68e3fed621f4f2d9f44378853730c2247fe450362
+  __TEXT.__auth_stubs: 0x10d0 sha256:26f04ed529886b3c214904eb04adae9a2c56bfaabff90fe15cd1a608b89c247c
+  __TEXT.__const: 0x300 sha256:657083f0b2ba216927c0cb3e4d4cb2ff1c817b400babb3a756b3fe4ed3707e63
+  __TEXT.__oslogstring: 0x61dc sha256:dc51419757b96370dd9b3ecc59fc543c854e1da0c3d40118afde22a21f1e6419
+  __TEXT.__cstring: 0x424b sha256:aaf20bba92fe2f90aa2c53c551f8000910e5137bd357a792189be3e40ae7cdcc
+  __TEXT.__unwind_info: 0xc40 sha256:1b487359b8775b6216d859123e531f3b0d6800aad60548a6703692b8c4c8e0b4
+  __DATA_CONST.__const: 0x1db0 sha256:df43bd51b60bcf697edf628f028dea1e9f9f63d56e8c76e0efc9287d4e61637e
+  __DATA_CONST.__cfstring: 0x2b40 sha256:dcab63a2f9b299ffa55b11fc8972e4009038531accf89fd39026a34d6ef96422
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__auth_got: 0x838 sha256:b62ffd89b50ed81fec569b8381c8e6da76f6ebe99e6eab8f10393d4e65564427
-  __DATA_CONST.__got: 0x3b8 sha256:5ce2b983239db8534ad935a35cf196e0a3b46720204c87c7f32db197e1a22de6
-  __DATA_CONST.__auth_ptr: 0xf8 sha256:5be36aecf7f90b6a39aae92a043a8a6362c5b6de439fe5764f3516e2dbb96481
-  __DATA.__data: 0x118 sha256:5bec124b590512e6238289668bdd5c1dc48a9350807cab806cc251f8401ee274
+  __DATA_CONST.__auth_got: 0x868 sha256:26cc75edd254a32da10fa6a318db78adfb88d1a0a0733f5fcdbf8f4c4e1cd890
+  __DATA_CONST.__got: 0x3b0 sha256:e80d925d83c058bf6b14e830564b9b129aeed7ce444d8109de76d44a5a31787d
+  __DATA_CONST.__auth_ptr: 0xf8 sha256:e822fcef97e45a15ccf8bb9b7b92c05d14778534dd21986f1cafeb8aa85b4ad2
+  __DATA.__data: 0x118 sha256:328a46aed513ea397f0b26490b5330ca30b6e6c1600233d691bc69962e07eb34
   __DATA.__bss: 0x210 sha256:8889eb3cdd3d0ac94711b47ce78b430d8e23a7b31ecc994c56d0c3310c87674a
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: A4591080-6F76-358A-8967-AA6D14AB6AC8
-  Functions: 1031
-  Symbols:   489
-  CStrings:  2088
+  UUID: C1B017B8-7C9B-338F-9B57-DD3707C35EBA
+  Functions: 1030
+  Symbols:   494
+  CStrings:  2092
 
Symbols:
+ _dispatch_mach_connect
+ _dispatch_mach_create_f
+ _dispatch_mach_mig_demux
+ _dispatch_mach_msg_get_msg
+ _dispatch_set_qos_class_fallback
+ _mach_msg_destroy
+ _mach_port_deallocate
- __dispatch_source_type_mach_recv
- _dispatch_mig_server
CStrings:
+ "%s: dispatch_mach_mig_demux failed"
+ "IPConfigurationAgent"
+ "dispatch_mach_create() failed"
+ "ipconfiguration_mach_handler"
+ "no domains "
- "%s: failed %d"
- "server_init_block_invoke"

```
