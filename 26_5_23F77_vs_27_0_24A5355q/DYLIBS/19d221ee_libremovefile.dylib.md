## libremovefile.dylib

> `/usr/lib/system/libremovefile.dylib`

```diff

-85.100.6.0.0
-  __TEXT.__text: 0x20ac sha256:decde4ae8bada0ed3402fc962ef377b5be0703f1331b4d93cc9e586acf631aa3
-  __TEXT.__auth_stubs: 0x300 sha256:2a1528646514f8796cab30cca9a28355e4073a6368c85888d1def1d0bb689ca4
-  __TEXT.__const: 0x40 sha256:9a72e56a08b11d4b1c67bfbe32aa94eb161f39866ca12d20f9caf6b0dca473fe
-  __TEXT.__cstring: 0x2d sha256:599ead73b71c8419d2843f72ed5efe1f11498882a7912c89344c5d95c4f98dfc
-  __TEXT.__unwind_info: 0xa8 sha256:6354cdf107432ed89bcc5d824649036befc2f6b489e5f9418422a03889585921
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __AUTH_CONST.__auth_got: 0x180 sha256:a1a4f5721c1c4610af7f71078f3a68c330536d679803b0e0507ee8dc10c5dfca
+94.0.0.0.0
+  __TEXT.__text: 0x1fc8 sha256:3ff5fe7f8d8292fc1f5973ca249743515c81c7a2187c7384aaa55368e1e25f15
+  __TEXT.__const: 0x48 sha256:fe37880300276b40d509866565b0e0726679f7760a4d2bf1f59459ad021695d4
+  __TEXT.__cstring: 0x5d sha256:0fac8eb5fdabfc29717a74e015081cc88c412d3890b3c9f865632163a3847dd5
+  __TEXT.__unwind_info: 0xa8 sha256:bbe5259a1859537c69edd93c05c199332ce49a8578665247a69da3175302e8f8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x50 sha256:7943525229e857dcc2e2db151dc2c0a6e5d2f2523ea3ca9cf1b00447d3b3d254
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x1a0 sha256:4cc7e6272db6b1ad7581f76c63c694e926e20698e9b02223d5041a55960463f2
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
+  - /usr/lib/system/libsystem_blocks.dylib
   - /usr/lib/system/libsystem_c.dylib
+  - /usr/lib/system/libsystem_containermanager.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: F15FF19D-C319-37D0-87A3-985A0F46C299
-  Functions: 21
-  Symbols:   81
-  CStrings:  5
+  UUID: BD6C2143-87F1-3839-B8DA-BBF362443BDB
+  Functions: 22
+  Symbols:   90
+  CStrings:  6
 
Symbols:
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ _____removefile_tree_walker_slim_block_invoke
+ _____removefile_tree_walker_slim_block_invoke_2
+ ___block_descriptor_tmp
+ ___block_descriptor_tmp.2
+ _container_traverse_directory
+ _container_traverse_node_get_depth_from_origin
+ _container_traverse_node_get_optional_flags
+ _container_traverse_node_get_path
+ _container_traverse_node_is_directory
- _dirfd
- _malloc_type_realloc
- _move_to_parent_dir
Functions:
+ ___removefile_tree_walker_slim
~ _removefile : sha256 0cbd91f3cda434efe26a34423ab1d36334c943433bccdd134ad9f229fa949aba -> 5bdcc06b90faa94db540fc0202c508ca56e3868aba75392cb8e72833f24d7714
- ___removefile_tree_walker_slim
~ ___removefile_tree_walker : sha256 9c5cee89875c367411e7dbc3f32a6a9ba41ab13cea38939d6cba84ae025252f8 -> c17527c9fc292e748e0c4c36e3269ddfa01f54039f49836c90c99c8f84f12b65
~ _removefile_state_free : sha256 da2c8561bf55ebda3142d82cde84e9f7d0eebad3ea4c2d8fc40907487ff11dbf -> 22e42ce5bae99f9caa786c19edb8a34d9197702e46f2256b2c2ee5102dfa4d00
- _move_to_parent_dir
~ ___removefile_init_random : sha256 ee9d0040f4e55cc8484f6bf5806b0a9e26788ced42aea2e88b6e78cd1b278146 -> 1f9f80180c472ab434da403a96b072dd714d16f17c1b9a6fcddec75599ccd5ec
~ ___removefile_random_char : sha256 3526270bccfe4d8c5fc36f2f0560729b230193c05d042c8d65fbba3de6ba2e97 -> c30588c154feec0bf8cb15c5e2e9f0cdf4357e5e7fefc1c0e6d3d8150b1d6722
~ ___removefile_randomize_buffer : sha256 1c99917532fcaf9c9a4cadfda9a0b62d9c2be9f2da835056fb5b4ce305a77f20 -> 230b3b4e2a00529a7db84c9801e2572025d24b2d3682857206f91f6f8b85045e
~ ___removefile_rename_unlink : sha256 41e644195b1282fae025f0da659b53469dbf7ff66e7c8c6f0c06a4f7437ff9b4 -> 22d97562bc00afcbd613930a303022566eede233b81b42d3888be31861e445de
~ ___removefile_sunlink : sha256 89636b097a9b31178da9c5757e7666c65dd330906007e7b4af0e1f478bc973a1 -> a45cd28a1721d89c7890ef9b1e7d90ad41d00543a2b4d772247a1d6ed46120ac
~ _init_write_buffer : sha256 35fbb73610c2e48a563b1092975d22cd5fd57cbf5a4d45c76ee96c740376fc68 -> 50a81e0e70718ba62a45045c27e62f0cbb8c1f94751bd8430d192dabe0f0ae14
~ _overwrite_file : sha256 400852ece05f79907b810584347ce6d5d8b774453a29288567be3e9e0f393328 -> 8f1fc6cae5f0726e51fa9dcdf2f78d491c6a947add0a4564d2e6329c55a6a21a
~ _overwrite_bytes : 296 -> 300
~ _overwrite : sha256 9815e5896adc9f1ba615674a840930087958cbc5a96ef5b927c1ad5c12e5a066 -> 40aad102d10d57d58d13344ca0081ca29c8788ba85357239c59725f4e07173cc
+ _____removefile_tree_walker_slim_block_invoke
~ _check_error_cb : sha256 6cd0c290d37fe8f3ddb4cffa70e83cfe163577773a8c1e94ebe68e1ed8597766 -> fc4f3a0666065c8bb73d9b7b06dff7a2cfce88abcf138e7e5f4f074ef6779370
+ _____removefile_tree_walker_slim_block_invoke_2
~ _iopolicy_materialization_on : sha256 9ca3ba67086f5b49ee178cca45c54e2900172f00dd90fb0cef307e78ab23ceab -> 3adc67f74c765ee585a5f65e223c62b13ed4d48365e1a95ecd5d6fa0f9d3d82e
~ _removefile_state_alloc : sha256 66d74a8ca16c1048bc0a716bee78c908689cb1b61c3a602ebfb30194ea19c3ac -> e170dfd01ac85de352982598ff45345390062d3382c386f5a6309d174a74a597
~ _removefile_state_get : sha256 4caffe5165714fa4cf124c22d3d2e575ebfc6140e9c30e91325db36e5f2a24d5 -> 917413403bc4f878295b7a198adfb6f9b812f2abb03d5318b3f93b755728c227
~ _removefile_state_set : sha256 b5e604f332488550413560fed9e08848a4a33173985277c9b853f223c6600fac -> 7c3453a11cfaccefc50e185ac5739d77345128f4a5c90b8578df52b299511bec
~ _removefile_cancel : sha256 c1cfa8a560e6c7f297299a1ae25947582b22dc8445b55c11150efdc1556b09a4 -> 63908387550a175f0251a7e3b9a5108b38fcad4a43709f258c559c385a14cdd0
~ _removefileat : sha256 c29ccf584b4259da518dc2e5f499433c35bb8cdbe617524ae32fb5d5fdbdebd6 -> 0aca9b78c36e589a9369231d6f0c5cc6ead7c013cf025710173f847d8d8108cd
CStrings:
+ "B16@?0r*8"
+ "B24@?0^{container_traverse_node_s=}8^B16"
- "%s"

```
