## libffi.dylib

> `/usr/lib/libffi.dylib`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0xd32c sha256:ead569b76b94b546e1d477cba5c37ee26b545bba8250f215c1194c91288a9b05
+  __TEXT.__text: 0xd38c sha256:d8cf299507335f59f063bbe52aadfcb37345c4deedff80f29a7c7279e8a4341e
   __TEXT.__const: 0x150 sha256:0467b040c1bcf39f61032dbee8973c2bdc705e7b7e7feb18cd5b2ae2302839f2
   __TEXT.__cstring: 0xa5 sha256:02f6b52a6a100f698eb6afc0d768f9248d03ee79cdb00ec5bff2407f1d45bbd5
-  __TEXT.__unwind_info: 0x120 sha256:4469d5e03260a710145c3dd5ba66f4484b8a0a8eda88dbb9e5587fe229c48bef
-  __TEXT.__eh_frame: 0x90 sha256:7d312e15f94b2880a1b5d37831f3ec927fa669ecf204e1d0406b019aac471771
+  __TEXT.__unwind_info: 0x120 sha256:5e934012c33bc426227d9bd253b3d41d9fde6b7b527d0e8d4c05f6f413b37c58
+  __TEXT.__eh_frame: 0x90 sha256:c57901b548f26eddefeba9919b201619ea11d8a49b837bc70a4e6aea52729505
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x50 sha256:259e4c27c096c3c1c0f2734e9329df47a88a19c3ab755f179432d56da5066032
+  __DATA_CONST.__const: 0x50 sha256:62ea1e30b5a6a3323a1e6617984bae697e3951ee0ba5c811c084b4746661093a
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x20 sha256:8f18b97ab926fa7c2415bf73554f5eb506bd4cd5a8139c5fec6d1ccc9c1bab17
+  __AUTH_CONST.__const: 0x20 sha256:a976dd80333dc94c3075168af2c76ac03cc1df536801cd37f2407cb1acdc9ae9
   __AUTH_CONST.__auth_got: 0x80 sha256:38723a2e5e8a17aa7950dc008209944e898f69a7bd10a23c839d341e935fd5ca
-  __DATA.__data: 0x60 sha256:7f4e3824b012f89e2915f62d6f1c73f97535c137881c8ad45be6d6cb61984dca
+  __DATA.__data: 0x60 sha256:ea4bf51929dbd87fbde0bc003baf421b2616a6188a523ae7c0a39e22bc750125
   __DATA.__bss: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
   - /usr/lib/libSystem.B.dylib
-  UUID: E67985C2-2FC3-39BB-AF10-CA0F57610A6E
+  UUID: 47394809-7F0F-326C-A701-BD61F7429EB5
   Functions: 48
   Symbols:   109
   CStrings:  7
Functions:
~ _ffi_java_raw_size : sha256 c6e4608a88a2ef2321248b8238839f05bd97e913f75fef0b73d1d246c9a9de94 -> 327d04f9cddf17bdb81cc8c697ef9ec08231ee9970135115fcbe5b88ea3cc536
~ _ffi_java_raw_to_ptrarray : sha256 712d09a19de316be55cf363db968e9d69b0f6d670aafb2427103547d490b90b4 -> 1bca8453733087376c98a7cad819591123d82a86add15e6c9c3cde9d47c10914
~ _ffi_java_raw_call : sha256 38295da6df7d222289f63f7a9fa83ad66631b02f6b35550d094607c8b8f3ccfb -> eb233f06e4d3d7fd797502e7aba446f757164ea5db84da2655a17d56e844f341
~ _ffi_prep_java_raw_closure_loc : sha256 7017fd2bb6538fa49e2609af3057a18e7281f37f92b7d8a425fc7ebe7f181d27 -> c631e94f8178f362dfe2a97970ebb6fe2e07ac66d9c317bcdf93a8a5936a6bda
~ _ffi_java_translate_args : sha256 a2b79041ec4fdb874b7f0c4c47c87df27b29d4ef1277e14d2a4b4b20dd832fc0 -> 40d8e2c9871f4244abcbf69346a887f5e6040ca597ef72aced74a54f05969530
~ _ffi_prep_java_raw_closure : sha256 d50930c3fd10a0bf8923a5f78ba68a4d9003b051912e85b48f2204b6d39bf6b1 -> b89732309ea4a6aa2b95837f8e4dea0dac43cdd680591cfc6568554e387d2322
~ _ffi_raw_to_ptrarray : 96 -> 100
~ _ffi_ptrarray_to_raw : 316 -> 320
~ _ffi_raw_call : sha256 b38620f952bfdaa1a197f5e4df285d82d88f4214ac1e5b1928176a7e15916aa4 -> e7b7733c4da93d0fc83158c95af76b63a09961473bc4215e85ed7f536eab3dbc
~ _ffi_prep_raw_closure_loc : sha256 f7656d63183f17bf4c544dfd3ec9ca1309bdaa1253be53cdd86c7deae0236828 -> 90647aeb5bca523526a5af62672e9cea09c49a079629fa4518e808a1073016dc
~ _ffi_translate_args : sha256 201f90eb3bc2c252450fa9495b2905d03341d1abf454dfe5d5c64404b386a05f -> 9b6c66f1a0eee87c480ecd90cb81d68a0db3bcae6b32776af2f152bc41fe040d
~ _ffi_prep_raw_closure : sha256 c23b40599c6a9d336d17797ebca6b8854fbd3cd19221018784ac5ab27cc2708d -> cbf78d2806c59692f718c07bcf374763f81bebe9d1b33166380fdc47a4ab5d1c
~ _ffi_prep_cif_core : sha256 f2ac9fc558e434df8adcbd117344cba7a9a5d2630cfd3158185606d3752c804f -> 14d38edc8d44f7ddcd1d1f57ae818584c16ce009a639287d64de7989a9f5cb72
~ _ffi_prep_cif_var : 172 -> 176
~ _ffi_get_struct_offsets : 13632 -> 13620
~ _ffi_closure_SYSV : sha256 c5d7e70583a7f5f3f4689477c47a10b09e0612a1ad7049c831937c8df6198613 -> d0ec6459db65f79ff4196839df1222a7fdc23cc627d2aa348664cca6d842eb60
~ _ffi_closure_alloc : 560 -> 564
~ _ffi_closure_free : sha256 2332cdf2595d5a9b5f6c7b199f8de07d65fde56a34d13cc9f14bc843b73f3d81 -> aa38abfcb0a9d83004f911195fbd7971db9b4e90619fb60e86e917cd86c07052
~ ___ffi_trampoline_table_alloc_block_invoke : sha256 f2a0f36386267f88e62a531b4ed5b3dfed18363ece723353ad8c507c21eb7986 -> 4dcbab0b303aaeae98770c38c8e04983098b03cfaa60cf995dbfa500a8d0ed87
~ _ffi_prep_cif_machdep : 300 -> 308
~ _is_vfp_type : 312 -> 320
~ _ffi_prep_cif_machdep_var : sha256 78f8350242c302c8685fd06616c88a279e5660db4883d998f035b295b8efc904 -> 1f8dcd36ff11cb49d1326e7fb52537b5536fda0794b998cf204a1386117a1d77
~ _ffi_call_int : 1304 -> 1348
~ sub_2bd288b3c -> sub_2be799b7c : sha256 a575f278696ba23ce9731cc2642733a34c93ba7edf7ef727f91223f202b416b8 -> e01e9d6668df8efae10ececf8847449859bd16809c2e8fb9d3b3ffd9c9b28200
~ _ffi_closure_SYSV_inner : 952 -> 988
~ _compress_hfa_type : sha256 5d38314cf29ed64a721ae405f7efeb83f1587cfa9d238b73a5cb8292199421d2 -> 62c282f81c5feba23b4fc9e5075c9db417c8ed9f187b1e1e505a052628c3f9f0
~ _is_hfa0 : 100 -> 92
~ _is_hfa1 : sha256 90f7b2f1d1348ee2f4928d8e9a10ca8240409bfc738a5e9b85d51c6cb1e7f0e5 -> e6f8bd1e0c5549e289304d1870f536974cd372be1c909bb8ed4bb01c65125cf8
~ _initialize_aggregate : 244 -> 248
~ _ffi_closure_alloc.cold.1 : sha256 e13553d098397dbeaa32f50bfb1be4a5a3c1cad3591f87dc2142e2ba66dfaa11 -> 9330c921afbb2df599c51fc564efdfb6b328f20ebabc9707caad6183820a3a10
~ ___ffi_trampoline_table_alloc_block_invoke.cold.1 : sha256 7fd76690d99cdfb160c89f2d60735eac6af8e19f2b8b4c72eb8fe828adb282ff -> 60cabf71905b7acb0ca210a40dbcd72d3ff8c7b0fc1a6f11ef23ea1619549986
~ ___ffi_trampoline_table_alloc_block_invoke.cold.2 : sha256 9f8ee96196549ce2d3a405700f63410975c606216ec499a6f5826e869654d226 -> 645cf02d5e308b99cea4573d23cc8229f0c16c3929332551592b6e6db8c08160

```
