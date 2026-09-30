## mount

> `/sbin/mount`

```diff

-757.0.0.0.0
-  __TEXT.__text: 0x4d9c sha256:2fcd95c02b1149df645a0a741880b5e6a69d8938b46db7c5d1968f8db87fab14
-  __TEXT.__auth_stubs: 0x840 sha256:61d15d0ae733bbe65f7629562769c397ee54110d891c87ada7d88fa174bd345a
-  __TEXT.__objc_stubs: 0x6a0 sha256:7afbc1073dfa0ac87a82a8b3d769624d2cd12c72a54623aac84d708c9bf81695
+766.0.0.0.0
+  __TEXT.__text: 0x4dcc sha256:9a077e828e863870fe1992ecf16cea9f8f8f10a32b7098ffc6d295a4ff091b8a
+  __TEXT.__auth_stubs: 0x890 sha256:f48d06305983581d224f9ad7a8329ccf4fa1de98db4660485ee2ec07a9c61bad
+  __TEXT.__objc_stubs: 0x6e0 sha256:89c6f86f33e12a1d104ffff4ade5d411da0f5ca336c6d39b7009703d12adb555
   __TEXT.__const: 0x3c sha256:2797d0a49c0ab15c71f0fd9b17a23f576489471d41805e0e1442d811942bed3e
-  __TEXT.__gcc_except_tab: 0x254 sha256:7f4976144cba1143c5c3424c54e3c816ea24cbcd31af8195d793bd024f549d6d
-  __TEXT.__cstring: 0x1216 sha256:b368b3f7d2f58a40855e5202395e997d89080bdb50605e7367bdc7fb4aec3335
+  __TEXT.__gcc_except_tab: 0x258 sha256:c039ee2a9c874ef6407202e81de24c368f30d981a8f066711eeee437d052e73a
+  __TEXT.__cstring: 0x123f sha256:acd8ae6f771433a8d50184f836c15a551eb321a7f939ca185a22c59cc33b6111
   __TEXT.__oslogstring: 0xc sha256:b2e406804d42a4339c6810cba6b4e19487566a50e1a25e50ad9b770e86d2ba7e
-  __TEXT.__objc_methname: 0x4ff sha256:b0794a8fc046aa0fb1490f23829575adca50eb895dabba65095dcc1c040c7ad7
-  __TEXT.__unwind_info: 0x110 sha256:c4e4f7cc58938c659c58df510e8020b59c8f2190554d60c77853ec89a8fdedec
-  __DATA_CONST.__auth_got: 0x430 sha256:f3a7b87b4bf84b758365f0a4358dbcda7b43989fb13ca3c93d7a6edcf3eae727
-  __DATA_CONST.__got: 0xe0 sha256:2feb16f8be697baba5fa92c632e225908512223773ddca3e4a1cc4a7ec95a384
-  __DATA_CONST.__auth_ptr: 0x8 sha256:38c1f70061a3cddf5066544f651189f15b45e36385ecdb620994dcc86209def1
-  __DATA_CONST.__const: 0x450 sha256:5d85c214a27986db141c25da3a83ee44024d5a7115278bd546cbffae58b6569c
-  __DATA_CONST.__cfstring: 0x2c0 sha256:405004827e1b9b4879af989afb20b409d2ec387bb11b66b6d44be6952c879ab6
+  __TEXT.__objc_methname: 0x52e sha256:04115e576e94afa3ea5e0f98ddef850196c78ce1dd03d6b701526164a69223fe
+  __TEXT.__unwind_info: 0x110 sha256:05bf522ab0beae92434b5db78060006deb5da193f4e96385d37df63d72ee42d7
+  __DATA_CONST.__const: 0x478 sha256:9a7b7b96c526384453eeb50e02cbfee27136cf40323323eaa3e0d5c7f12c68d1
+  __DATA_CONST.__cfstring: 0x2c0 sha256:b9b2082f24f0cee1f00d01e552ce32bec4958990d2728c2f00ad0e36c35a4ec7
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x1a8 sha256:5832d872ab0b47a7b191ae1f46b5d847dffdae645d2172e0d65c9b5f73152178
+  __DATA_CONST.__auth_got: 0x458 sha256:2df82281bba98660bd64f6d91bcb29304f19f9604ed7a9388362f7d336b507c4
+  __DATA_CONST.__got: 0xe8 sha256:b69d3619019311a6a76538f25ee3f789c5f98a6e45c084a646ce64531ea3ab2f
+  __DATA_CONST.__auth_ptr: 0x8 sha256:bbe596ae8cc9017eb0f3ae803239a760168a192f7e6098b8d12611f11b2c22f7
+  __DATA.__objc_selrefs: 0x1b8 sha256:1f4a58fd550b7ed3eed8ee5aa4ab97beef7cfc83e886bfac575d56722640ca35
   __DATA.__data: 0x4 sha256:67abdd721024f0ff4e0b3f4c2fc13bc5bad42d0b7851d456d88d203d15aaa450
   __DATA.__common: 0x54 sha256:4fea5e6a3ec5f5474a26d858bc77b6d7bd3ab864ea02d988683fdc648602b248
   __DATA.__bss: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d

   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6280DEB2-593E-377B-B191-30C099FE4E3D
-  Functions: 53
-  Symbols:   167
-  CStrings:  276
+  UUID: 6AF234C6-CD50-39DC-BC74-2416696CEB9A
+  Functions: 54
+  Symbols:   173
+  CStrings:  279
 
Symbols:
+ _OBJC_CLASS_$_NSMutableArray
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x8
+ _objc_storeStrong
+ _os_variant_is_darwinos
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
CStrings:
+ "addObjectsFromArray:"
+ "componentsJoinedByString:"
+ "failed to mount data volume on darwinOS."

```
