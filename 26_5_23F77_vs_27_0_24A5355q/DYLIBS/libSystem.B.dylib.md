## libSystem.B.dylib

> `/usr/lib/libSystem.B.dylib`

```diff

-1356.0.0.0.0
-  __TEXT.__text: 0x648 sha256:94dbf05b6e7b79091800fd57e339de5709506c1f6f3ca62d25f7b807e77f853d
-  __TEXT.__auth_stubs: 0x410 sha256:178200d99ed9e7b5596844e5b4a29f70be708b722f1328f6f9a3d09a4a1c0d33
+1359.0.0.0.0
+  __TEXT.__text: 0x654 sha256:89b8cd827c15706593188024894459c38c9680f8e61d6b7fa347a7d4f74c336f
   __TEXT.__init_offsets: 0x4 sha256:235f15da1b8ed3637864f444e5e082cdc79f85f3a9658a05c71aa2c5a47bc81c
-  __TEXT.__const: 0x50 sha256:eaab8f8ff387be4232c12c8a2c4e549ff37659e58b2427ef79fc1cefe2a7cf4c
+  __TEXT.__const: 0x50 sha256:d3dc086cb974abcb03ab4305bcf0e2e241c38ef4251772c02cf80a3e7e784571
   __TEXT.__cstring: 0x6a sha256:ad87707c9d75c219716673486995d4645e6ac2591f255f4567a626534e4b0532
   __TEXT.__oslogstring: 0x35 sha256:53661421f9afb8b4042c4b17f09101e37dd0a26853a9ac56863cfdbbe7fe21dd
-  __TEXT.__unwind_info: 0x80 sha256:115b768db9a34d158d731d3d47129ff603b1afb0f835ffab2332b14d8b5eedc6
-  __DATA_CONST.__got: 0x10 sha256:08a45292deba2cb9fc714d0440262426b90cb75173d751d48ddfa6d2429ae513
-  __AUTH_CONST.__auth_got: 0x208 sha256:55c274c61850150da464f01dcdbe7325bb97e17364382b19000ae42a0788d07e
-  __AUTH_CONST.__const: 0xe0 sha256:1ad7f903e1b911555229a0a111bd06b10debbf52787001583d0d44e31c261380
+  __TEXT.__unwind_info: 0x80 sha256:46e8cd147c85ecdbc2c76a9309ecc0575a79bb7252108166e8c263e26220a639
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x10 sha256:de8f4daef4b84784c1696a3b47655616d8a7003282dd484ffdc789bfea718b78
+  __AUTH_CONST.__const: 0xe0 sha256:4e2cf338ee03b6e9ebd62bbd2b369d95e96dcde8918d15a68ae102def863e79d
+  __AUTH_CONST.__auth_got: 0x220 sha256:e5ed464051ec7f27f83007e9247da3bf4ef32f086bb89e0497cbd0febfa4b999
   __DATA.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_DIRTY.__data: 0x8 sha256:8722d9c27f7ee25655440235bfcbb0fd8de347acf8cc06a18e7407035264966f
+  __DATA_DIRTY.__data: 0x8 sha256:6d8dd8dbdfa3bfd933508c47a7474d6f2200dfaf14503f15574427208ea22097
   - /usr/lib/system/libcache.dylib
   - /usr/lib/system/libcommonCrypto.dylib
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_trial.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: ED582B70-F7EF-3222-8F75-30507F4E6E01
+  UUID: 28449900-A70F-3500-945C-1B49B9C05077
   Functions: 23
-  Symbols:   132
+  Symbols:   135
   CStrings:  7
 
Symbols:
+ __sanitizers_atfork_child
+ __sanitizers_atfork_parent
+ __sanitizers_atfork_prepare
Functions:
~ _libSystem_initializer : sha256 abce90897f0726c1b2717fc0b963819a5de4e5107c2785c52db16b515fd11723 -> 0bd33ba51d775458559627369aaa75df8f208835e4903942845926e5da64b62d
~ _OUTLINED_FUNCTION_0 : sha256 4365da0bfa6f68ddb16183f7c6ce8c08b8b99b9489ec2eb94b6604f7b4cd718a -> c6fd6d2a40adfabe9e0ade98d04c92a589d94041d7174c440f99ea37fbb5ba1b
~ _libSystem_initializer.cold.3 -> _libSystem_initializer.cold.5 : sha256 17c71aaec1cb83ebdb60181c788ca423fe51c746e3910d5ae41b0acde8714706 -> 12514bbe5eb4afacfdac42530390cafb1bab45ca09dacaa5a9f44298e68fa87f
~ _libSystem_initializer.cold.5 -> _libSystem_initializer.cold.3 : sha256 1b4e973ff4eac5bd1915ac455396b8828478999dbebfc6c69423403452627ba2 -> 39954ca1b626c11e30e82113d86d8c012c9b6b2fcb82a42fb62e52ce422f4377
~ _libSystem_initializer.cold.9 -> _libSystem_initializer.cold.7 : sha256 55d412a5ab24e487bbcef8060c682edbcff73c6296f1f1314d8f0d4ca3e3ac17 -> 82cb1232be2ad0e5446cd11a7c09f9d27aab80f4030ff3744566e53fd2f9720f
~ _libSystem_initializer.cold.10 -> _libSystem_initializer.cold.9 : sha256 cee1b09cc12ab796d0624f3395f7ffd1d0028a91977cd20e53158a47232861e5 -> e24a7b77194d601860b92f5291533f1a44064ccfb54ff9f6015ac25874419a6f
~ _libSystem_initializer.cold.11 -> _libSystem_initializer.cold.10 : sha256 881368a05c3eb969acca04401916db6dcce1b91987b6b077257b9164fbcea38d -> de11a38769e5e4cde3d6ef8e0df609011dc4f4ce40bf1ff4acc3a4e008897d93
~ _libSystem_initializer.cold.12 -> _libSystem_initializer.cold.11 : sha256 76662c6ebbc249d954addecb8686e6820ad3bba6d918a1543171a0437ed9a1b9 -> 2d6aac86173cc577d4251e4c155a4a7967393da45e9ac8bcbd4d2001ba37f616
~ _libSystem_initializer.cold.13 -> _libSystem_initializer.cold.12 : sha256 3d1ca0b27c4b40c4992c20c8d739ec991608c2b854c48505d957063c2d534cd8 -> 9b871269465d6d6466e95760f2f5cf8ca2cf69575d0b5f3c64f2299e92cd8ba2
~ _libSystem_initializer.cold.7 -> _libSystem_initializer.cold.13 : sha256 8aeff3db9899c7afc250b65bd0e1771ad8792a6080ee6180454c6e939d4b48fb -> afd1a016adff85e637bb0ef8e593595c2417520657284d8683f11f0d2dc49bd9
~ _libSystem_initializer.cold.16 : sha256 3be04e67d369c3ec533a2f056d67e550fa54f99cc39aa1530572104e7eef0605 -> 48d9750342cbbee815cb0abe2ab6f2b3e73715a62c2d21b73d270e43747150f0
~ _libSystem_atfork_prepare : 88 -> 92
~ _libSystem_atfork_parent : 100 -> 104
~ _libSystem_atfork_child : 120 -> 124
~ _libSystem_init_after_boot_tasks_4launchd : sha256 90d8df35f15a4a746d068194fa2e87efe3b02f085661ebe92c697810b310bb44 -> 9eaef4deb03ca2f5ae8c8f93f9bdba5ef2227be9064f04136662deb70e0ba1a0
~ _libSystem_initializer.cold.15 : sha256 d2280169173c10d37696eda0bc5237d6380e042ca7640b7ccf01027eab6ef8ac -> 01918da772260fbac673edea3dce4527003f7e5aceaa61e511724877dc2d802b

```
