## libSystem.B_asan.dylib

> `/usr/lib/libSystem.B_asan.dylib`

```diff

-1356.0.0.0.0
-  __TEXT.__text: 0x6e4 sha256:6deca05f189f6ba30c9025731f1e405dac5d019eac875254be3141b0fbb9a41f
-  __TEXT.__auth_stubs: 0x450 sha256:7e883efe7ca6feaca3225181b45e5063c0409b2efb63dec6a17ed979963c6671
+1359.0.0.0.0
+  __TEXT.__text: 0x6f0 sha256:fb6dccb358121358f81a69a1db3d441e2b66c9a020bc2ef2db7ef4584725219c
+  __TEXT.__auth_stubs: 0x480 sha256:86fcda4c75729b86f9ed3fe3a7ed2ff54801423c84a40a709d188f8bd6b2a2ba
   __TEXT.__init_offsets: 0x4 sha256:60aa1a6530b508041779e0105d1c242a27156e9039c97069e1eec5125a21f3b7
-  __TEXT.__const: 0x50 sha256:eaab8f8ff387be4232c12c8a2c4e549ff37659e58b2427ef79fc1cefe2a7cf4c
+  __TEXT.__const: 0x50 sha256:d3dc086cb974abcb03ab4305bcf0e2e241c38ef4251772c02cf80a3e7e784571
   __TEXT.__cstring: 0x172 sha256:6f09caa7008c2672daed790c5926419b1cfe4d752d28d6cdb5fe98bb3959fbc0
   __TEXT.__oslogstring: 0x35 sha256:53661421f9afb8b4042c4b17f09101e37dd0a26853a9ac56863cfdbbe7fe21dd
-  __TEXT.__unwind_info: 0x80 sha256:e2a54235c77573d6dae0dd398034d0993f385e6bade95b1d8b0bfa8ea13da0b7
-  __DATA_CONST.__auth_got: 0x228 sha256:060cc05624f7b998cf65d70d6957c0db246fb2040078d9f855b4a2532e065153
-  __DATA_CONST.__got: 0x10 sha256:7d2b7440ada221153c786d41c647c47ef34f000b9f42cb830a08f9f192fa39be
-  __DATA_CONST.__const: 0xe0 sha256:de036ab306ca5eb457cd43694fe16ae2b6bd12360c5b407fbd9dfa3462c130ae
-  __DATA.__data: 0x8 sha256:074451173aab30347bd6fd9024851357388cba2474660cfe3762be614d3d6b2f
+  __TEXT.__unwind_info: 0x80 sha256:d2ad11a9706b13a2ed6338f82ec74eb6a90feaea72f7559905f4fefeab237aba
+  __DATA_CONST.__const: 0xe0 sha256:791ec57bf626bce638fa08299ae61e438e9eb3056fcd8852d1314c0f38394ecf
+  __DATA_CONST.__auth_got: 0x240 sha256:8302f5db57ce4d70e9afa0876b1f227eceb9b5d7dcda7275ec1798a5bb3069c6
+  __DATA_CONST.__got: 0x10 sha256:03c4790ef273903143dc42473453c7f87df957d7d043e8d3a25dfe6358df1c34
+  __DATA.__data: 0x8 sha256:b63e19353048e676dc92602f7c62c518a5db931c2aaa9fb8743f7d8fc1e56f67
   __DATA.__common: 0x408 sha256:934ee56ad6539fb9e5c276ecee2f3985f2d252d22acd690108bda80313c6bd58
   - /usr/lib/system/libcache.dylib
   - /usr/lib/system/libcommonCrypto.dylib

   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
   - @rpath/libclang_rt.asan_ios_dynamic.dylib
-  UUID: A71284E1-3798-33DC-AC72-74AF6A125B08
+  UUID: C790F534-D085-330B-9101-CC286D38DD2E
   Functions: 24
-  Symbols:   115
+  Symbols:   118
   CStrings:  11
 
Symbols:
+ __sanitizers_atfork_child
+ __sanitizers_atfork_parent
+ __sanitizers_atfork_prepare
Functions:
~ _libSystem_initializer : sha256 3fb292c937d9ceb47feefae28d836a8bb1678700870fa83ff38a96e9e64ea7dc -> bc04f5b39fce889f64a321aaa1ee4028554aae791d876d02d67d00c65e4ee7a9
~ _OUTLINED_FUNCTION_0 : sha256 ebb27e0721ff56a632a65d744e98a041229d02e158a64f8a17182799be4d4205 -> 2c9cd3b17f44a0d8e80160279d251cfc4036f2a242252545a57652aa951a4ee1
~ libSystem_initializer.cold.3 -> libSystem_initializer.cold.5 : sha256 17c71aaec1cb83ebdb60181c788ca423fe51c746e3910d5ae41b0acde8714706 -> 12514bbe5eb4afacfdac42530390cafb1bab45ca09dacaa5a9f44298e68fa87f
~ libSystem_initializer.cold.5 -> libSystem_initializer.cold.3 : sha256 1b4e973ff4eac5bd1915ac455396b8828478999dbebfc6c69423403452627ba2 -> 39954ca1b626c11e30e82113d86d8c012c9b6b2fcb82a42fb62e52ce422f4377
~ libSystem_initializer.cold.9 -> libSystem_initializer.cold.7 : sha256 55d412a5ab24e487bbcef8060c682edbcff73c6296f1f1314d8f0d4ca3e3ac17 -> 82cb1232be2ad0e5446cd11a7c09f9d27aab80f4030ff3744566e53fd2f9720f
~ libSystem_initializer.cold.10 -> libSystem_initializer.cold.9 : sha256 cee1b09cc12ab796d0624f3395f7ffd1d0028a91977cd20e53158a47232861e5 -> e24a7b77194d601860b92f5291533f1a44064ccfb54ff9f6015ac25874419a6f
~ libSystem_initializer.cold.11 -> libSystem_initializer.cold.10 : sha256 881368a05c3eb969acca04401916db6dcce1b91987b6b077257b9164fbcea38d -> de11a38769e5e4cde3d6ef8e0df609011dc4f4ce40bf1ff4acc3a4e008897d93
~ libSystem_initializer.cold.12 -> libSystem_initializer.cold.11 : sha256 76662c6ebbc249d954addecb8686e6820ad3bba6d918a1543171a0437ed9a1b9 -> 2d6aac86173cc577d4251e4c155a4a7967393da45e9ac8bcbd4d2001ba37f616
~ libSystem_initializer.cold.13 -> libSystem_initializer.cold.12 : sha256 3d1ca0b27c4b40c4992c20c8d739ec991608c2b854c48505d957063c2d534cd8 -> 9b871269465d6d6466e95760f2f5cf8ca2cf69575d0b5f3c64f2299e92cd8ba2
~ libSystem_initializer.cold.7 -> libSystem_initializer.cold.13 : sha256 8aeff3db9899c7afc250b65bd0e1771ad8792a6080ee6180454c6e939d4b48fb -> afd1a016adff85e637bb0ef8e593595c2417520657284d8683f11f0d2dc49bd9
~ libSystem_initializer.cold.16 : sha256 2b0c53e25512007d3c252c1a375e4556bb6bb15c1479c275297d580126fe31f9 -> cabca5173ace339764bee36057ee269b1566fe7cb2a05cef54303631aa5850c3
~ _libSystem_atfork_prepare : 88 -> 92
~ _libSystem_atfork_parent : 100 -> 104
~ _libSystem_atfork_child : 120 -> 124
~ _libSystem_init_after_boot_tasks_4launchd : sha256 ea65f7812463776732ae3bdfce6a9f6b5aaeab6587de49389ef009d17934abdc -> e29037b3342b25e768dcffde9afcdf799605f05aae435e3f44df91aa14a3956c
~ ___asan_default_options : sha256 2dbbf054b05d273b1f9f4bb6cfd4957c284eea562a47c88ed24c77287e81dc62 -> 7cd906ab96ae0bf9e5d69ac2b533d409d6321a477a225e3bfe65d4fba8f0f113
~ libSystem_initializer.cold.14 : sha256 2893c22c107d7a8abd086629918fda26c8d889bd82509e3c55af256a68520d7a -> e827d80c84b614983e1c5c3ab3e7addce2f5e08df77d938c825ff6f668e7b097

```
