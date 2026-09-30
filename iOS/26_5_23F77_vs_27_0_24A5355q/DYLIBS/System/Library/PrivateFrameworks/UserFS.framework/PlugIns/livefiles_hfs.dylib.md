## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

-715.120.4.0.0
-  __TEXT.__text: 0x3db14 sha256:f965d6e1ccd2d119823d71268fd5e4e13b9e4a9f0bb4d6d94bd4e3d096f97fe0
-  __TEXT.__auth_stubs: 0x470 sha256:ec13a2cd8bb822752166617c1269a91e4b4ae96aa24049c78d120fc1e67caed8
-  __TEXT.__const: 0x4e60 sha256:9fb8b8f380287f95dbcc96841fd956199f1130ffd662c5c3dbbf655f3416e697
-  __TEXT.__oslogstring: 0x5c74 sha256:946e6921a5e8dec81276d1f715bf73e290a93f82a52c236b26098f192a3e34c7
-  __TEXT.__cstring: 0x26fb sha256:f3477ee07742e38b3250107274fadf7f22cad2582e96f09d76bef484a051501e
-  __TEXT.__unwind_info: 0x6d8 sha256:ebc5f6220ee5b82345b1127e98236a0fdc4310ed9af66d42a1c0549a15555c16
-  __DATA_CONST.__got: 0x30 sha256:511b3f42c90dc2bd3ac3cbd22267810bbef39fdd0e007ae95a18cc16fe2ab6cb
-  __AUTH_CONST.__auth_got: 0x238 sha256:5203ba4e767d42f262e42eaca774fe88c052b116e47febe72e9dd6183d4bd22f
-  __AUTH.__data: 0x140 sha256:db2d987115ca6fd19f5385408a7f7c88aa42a2f236bfea227c34a4968ea2a45d
-  __DATA.__data: 0x1948 sha256:96abfc5d96108e3fee5bd24e82b5946dc01c7b05b1b1b05fcebf9bf4f08c56ae
+747.0.0.0.0
+  __TEXT.__text: 0x3d2a4 sha256:45200703689c73c3381d8c2224402bb8f2bdb9bf05baa7bf8a6e98e872e119d5
+  __TEXT.__const: 0x4e60 sha256:d27890f7e5beee9e263659d98dc38e8902268b0d3f763501106b293676325e5d
+  __TEXT.__oslogstring: 0x5e7a sha256:28cee38eab993f67fd376d0306288e7fcc1e7db9b093e52ec8b0b1389dc62b17
+  __TEXT.__cstring: 0x26fb sha256:033bdc6a41f002a7026109d930f0adf28487a498ec1523ebe2ffec214d49425a
+  __TEXT.__unwind_info: 0x6e0 sha256:7cdbc95876e4d4f34b3d3505fec404d20e9d7d2db1f38729c5e68f35fc496e14
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__weak_got: 0x8 sha256:34eded462da4d1d74b449b10142d01b2f87de33844b6cf2c9873c569ecae047a
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x148 sha256:f85cdb8aa48ec9824bda2351b5f0b4c351e4ca15424bf44fc847eb62820a04ce
+  __DATA.__data: 0x1948 sha256:e1f93fc1aeb079bc63ccba9357a422dce87ba8201554a8e4810e913abf497172
   __DATA.__bss: 0x34 sha256:7955cb2de90dd9efc6df9fdbf5f5d10c114f4135a9a6b52db1003be749e32f7a
   __DATA.__common: 0x100 sha256:5341e6b2646979a70e57653007a1f310169421ec9bdd9f1a5648f75ade005af1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 20780CCF-13C3-34DB-8A7E-241DD4632C3F
-  Functions: 677
-  Symbols:   1163
-  CStrings:  738
+  UUID: BEBAE024-98CD-3998-A07F-CF9A0B4DC854
+  Functions: 676
+  Symbols:   1141
+  CStrings:  746
 
Symbols:
+ _hfs_swap_HFSPlusBTInternalNode.cold.20
+ _hfs_swap_HFSPlusBTInternalNode.cold.21
+ _hfs_swap_HFSPlusBTInternalNode.cold.22
- _OUTLINED_FUNCTION_11
CStrings:
+ "hfs_ValidateHFSPlusVolumeHeader: invalid free block count (0x%X), greater than total block count (0x%X) \n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\n"
+ "jnl: open: blhdr size looks bogus! (%d) \n"
+ "jnl: open: blhdr_size (%d) >= journal size (%lld)\n"
+ "jnl: open: blhdr_size (%d) not a multiple of block_info size (%zu)\n"
+ "replay_journal: unable to allocate %d bytes for blhdr.\n"

```
