## Radius

> `/System/Library/SystemConfiguration/PPPController.bundle/Contents/PlugIns/Radius.ppp/Contents/MacOS/Radius`

```diff

-1027.0.0.0.0
-  __TEXT.__text: 0x3d9c sha256:8c682708fd323421f8bdeb38d1a6ee8b2a7b3d62211db11cba5d3a552078f0c2
+1029.0.0.0.0
+  __TEXT.__text: 0x3dc0 sha256:7445279a11acda2774f6bf33f5a59dee78d99d33fe978a57f753f208f99c944a
   __TEXT.__auth_stubs: 0x440 sha256:12296d5a086b5e46e23448604251496730f1189078f16316a325d3387c136ce1
   __TEXT.__const: 0x1b sha256:6865212b923c68975c5e6061dcb3fdee8f0e4456891a4e36f85be338ff7cb2e8
   __TEXT.__cstring: 0xf11 sha256:35e7a379c4a7dccc05134a6a44b93ff2e09fca22400c6fd5e63b41726a957956
-  __TEXT.__unwind_info: 0x110 sha256:339fd57c2034ac9a0ea6d37044e7f1b8d3ba49e75ff95baf36c304a39604dfec
-  __DATA_CONST.__cfstring: 0x200 sha256:cac0b581637e60606a8dd06ba33a32c46af05e8f3f2f0f1b2f7e755e34325a92
+  __TEXT.__unwind_info: 0x110 sha256:6c615fece528d90f16d2a9b6570824dd4ab2046305a6eacb9390de4550f4fd46
+  __DATA_CONST.__cfstring: 0x200 sha256:ff48ab6bae5abbdf8661daa0c89b58aca141c0433429b3f10ac31bf9de72ba9b
   __DATA_CONST.__auth_got: 0x220 sha256:18f2c9a07be397f6e6ba3caf460c3c37432b98b5a9cc9341edf940b776ec0920
   __DATA_CONST.__got: 0x80 sha256:2d088bc2e0b75a003df2d2dfc0cce730cda077c2c7258b07b895f82a81d5b017
   __DATA_CONST.__auth_ptr: 0x8 sha256:fb0fe06052cc40dba7350d92f645c960b0b554836bfefb2100ec108ea6f5a4f2
-  __DATA.__data: 0xa90 sha256:f78b052db55daf880191536527c6c80efb19eca032617b3c7c466633f7530015
+  __DATA.__data: 0xa90 sha256:a37f37e3f8d51309ea10fcf22337b1ee8c4ac7e28d90673aef196ff36ad32f2f
   __DATA.__common: 0x90 sha256:81c611f35bff79491538b2f7cf201c7597a661a5c549633541c62bdc8af1613f
   __DATA.__bss: 0x834 sha256:8dd6c05a3a7cd7642429f2a2d45dfa3ff0b97a4fb7c1dbc359cc82a829ea9d5f
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  UUID: 0678FAB1-603F-329D-9A28-0E591F0581BB
+  UUID: 3C3E7BAA-10F0-3B9D-886B-124FD385EE10
   Functions: 50
   Symbols:   144
   CStrings:  161
Functions:
~ _start : sha256 e2d814df7ee75eb97edc24b9503832b352cf3cbba1f5cebb82e46d6ca536458f -> b2ab4e3bddfc78c36c243f087470d49c481b341a619af3c246602ec195a56558
~ sub_81c : 2132 -> 2124
~ _makestr : sha256 965110fdeaf86529ff1a1cddb08393cc778ccbe1debbd17ff1f5a1ddab04499b -> 962ce26c96609e31063b04d30509ba338b1fcf480baa7a8cf67eb0eee4437706
~ _makeint : sha256 bab9625cdacd84e39cae45a470577555ecf66082a784229e6c757b1ecea69f7f -> bb5ceb7857f623d2eb77e053cea481e86967b81e9d4aaaf04d11fdb1bd45a7c7
~ _radius_decryptmppekey : sha256 47b01c8d886560b38f8011c9c03ea8249130cd7e29ebdd82c749b3afbb15a78d -> daa57de5d829b9f32219b5373311dae73a88ac36660339ec1a62eac38fd63809
~ sub_13c8 -> sub_13c0 : 2328 -> 2312
~ _rad_add_server : sha256 81e1d3f16f8364d5e67e3f0a90d92b98af56354dcbc2ab0a7ca91aadb0e4b602 -> 9f9614fc8a1a7f806f18e5914fb8440e0bd3b93b2cfe56635d6f9b2b190046b7
~ sub_1e40 -> sub_1e28 : sha256 cace4357565318c40d65d81587f371d007a9ebbab01fed4568286498b6042ac5 -> 073ae48de03c377da496b0189f9f948d6a5474bc8b1ca3ebbb0402dc2e6b4867
~ _rad_close : 164 -> 192
~ _rad_config : 1320 -> 1308
~ _rad_continue_send_request : 1892 -> 1868
~ _rad_create_request : 156 -> 184
~ _rad_cvt_string : sha256 be9864fbb37b6f4c05dd8c477356316857e768e40a9583b222ef539a1b82a53c -> 1e23535e6da9ea7e84123c4a92cc8ebc24405801bb3e155a39cc91a172b9fbe2
~ _rad_get_attr : sha256 41f114f99a302f72afe69d175efe663b4ffcbb41767b26fb94fff7068cd786d0 -> ad8e888afd23080e7630d3441af610a41f17738b9b2f6343e3a9fb43da7510d7
~ _rad_init_send_request : 460 -> 476
~ _rad_auth_open : sha256 946003a7f1fa2adbe843899f4ad24c232c4bc0b26840ca9e8bc6ee2826e727bd -> 2032a88e0ae7704a89ba0a7f8a92538979a69797051e8ba5adb6c052e1850568
~ _rad_put_attr : sha256 7ff6497fd766bba7ae3fdb0bc77745a43eaf41d77fe1c2c646033d02a2f49b4b -> 33ee626153db160abd475f7d02e937c4e4ed7c835c29b18e31767c705bd242d0
~ _rad_put_message_authentic : sha256 bf3733109c579e522f7720677e2640c93dc454932571e9f5547f28a4b2fa1b76 -> ffda1291d86eeb56c8e2556efcff6445417d2bfc8df29fc9d891c1ce2e776b79
~ sub_3254 -> sub_3260 : sha256 9f109f1b55910e4707ffcb7f7ed516efdbe1e06d8facaa255e236cd6ab8602c1 -> b3e11809e4b8a01919ec7594386522f132d0f727856aeadd1a3ed8029d518971
~ _rad_put_string : sha256 f5872691947994282ebf05d765cbdb803cfe7a980e1402ea0bc8cdc0c5996077 -> fcdd5a6b95afb73651e0a230db3f09eac2f6f5186a2d15f405c24461e7763b92
~ _rad_send_request : sha256 b07f4bf489ca8e124bba64b80a23cc1b6f07e2fd6e56163e702b424552d38695 -> 19bde582d89798755891b3aa345da54164b3088152503335b89611bc841a2846
~ _rad_put_vendor_attr : sha256 70e9681dfea5bce4ad6ce3933e86c7a611b034f3b0bc1975bba5474fdaa6ab8d -> aa461a9f59a2d20dc9cbc602e0d747a79e4a36678bbe665ed432f848d9cad0ad
~ _rad_put_vendor_string : sha256 7881f39f60d1f72633e8a6334d26e33f0a3348dc559e82ea9ab240271c778e40 -> 50c1c1951fccbaa3bbcb2a334ee7736aa2c2c86bde71da3b64821af546d4f788
~ _rad_demangle : 420 -> 428
~ _rad_server_secret : 20 -> 28
~ _rad_demangle_mppe_key : 608 -> 616
~ _radius_eap_install : sha256 2ad61eeff7231f747b9be41f72c25be12f9850af8b0d2e0ae7dba483448def3d -> 2dd564442062e833f8ccdaf13b1db72c14b0fdce978bbe9c5d28ea013282e957
~ sub_3cb0 -> sub_3cd4 : 412 -> 408
~ sub_3e4c -> sub_3e6c : sha256 ea1d504ad69b385e0edbdf0a0e28ba68e63727e7ca8b5260ba3a0e79d61df1cf -> 63d80713c7ec9b7bedb727a0a4a0ae3e5b05162051353c9bbab2300027e0afa5
~ sub_3e80 -> sub_3ea0 : 1624 -> 1628

```
