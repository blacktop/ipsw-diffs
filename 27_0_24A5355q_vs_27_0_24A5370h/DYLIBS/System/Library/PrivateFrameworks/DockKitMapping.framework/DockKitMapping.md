## DockKitMapping

> `/System/Library/PrivateFrameworks/DockKitMapping.framework/DockKitMapping`

```diff

-410.1.0.0.0
-  __TEXT.__text: 0x4124 sha256:1191620a49a0374a6a717bc666968f83ed76ed72b37a973f2a0bcea5faf1f338
+411.0.0.0.0
+  __TEXT.__text: 0x40a0 sha256:2194faa217d84b88c2fceacb882f88a002bc9f333e749fc02b620afb9628609e
   __TEXT.__const: 0x4d8 sha256:80d3acb5037c7206c5cd82f1721f5a1becea6579d2267e421ef9d315f1868cb0
-  __TEXT.__unwind_info: 0xd0 sha256:3fb1ba79ccfa41a335225a4e548d2d4ddd26be8859ad9efc123cf77e14374ebb
+  __TEXT.__unwind_info: 0xc8 sha256:f7898959d4698b87a6481ea714e029e7512ef72fc25b0c7b6285d090288f96a0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x68 sha256:39f37f8d1931b3bdf767e7510dd69509fbf23af1f7654933d0a4d291cbdd4418
   __DATA.__bss: 0x31f60 sha256:8f5eb0f890dc64d24658779cf34fdb3bbb5d56dfd94d4a43c366e29159b59120
-  - /System/Library/PrivateFrameworks/ObjectUnderstanding.framework/ObjectUnderstanding
-  - /System/Library/PrivateFrameworks/RoomScanCore.framework/RoomScanCore
   - /usr/lib/libSystem.B.dylib
-  UUID: 0D089E5C-16F7-3DE6-86E1-2BCDD0E69AF9
+  UUID: 1A6C395D-28E9-3F6B-ABC2-222C46F6DA6A
   Functions: 24
   Symbols:   73
   CStrings:  0
Functions:
~ _orb_init : 600 -> 604
~ _orb_configure_image_size : sha256 841ea5b5fbdf11a8a79e49a0e9dce95c9a9d54bd0caa1d1ce312e9d96de3425b -> d8f072ef9b80abec97460aaa951a2d8bc3071bd53b23f63d4dfb3ee0a3ac2041
~ _orb_cleanup : sha256 b4bd4f336b08e1df41408d1d4e2117eb9b1ff942b2b4a7acb6ea3cb085909b6d -> 6965f754bf5f6195296eb9daae807a556b6ecc1d026b686968f564091507e18d
~ _orb_extract_features : 3832 -> 3796
~ _get_time_us : sha256 7e9cca5125eb8a610e8ce3aaaeb82a7d71eb52d00f47db60703b8193cf855229 -> 308723f4d09a53ca8d21282b40125504db92d2e14a4b8a7a2e5557f6568886ea
~ _orb_hamming_distance : 68 -> 64
~ _orb_serialize_features : 200 -> 220
~ _orb_serialize_features_chunk : sha256 8891c5a36312e1f33ca42a17a17a9f494f6838d0b957bb6d64c243952007b11a -> 8373d9d5ea4c0e5fb10bbc23082abdc2716f8060511645a6d8afa498d4c92ed9
~ _orb_deserialize_features : 184 -> 236
~ _fm_match_features : 3504 -> 3488
~ _fm_get_time_us : sha256 4634803e03c354feba593f40cf8b476b9b1addaa6ea874e336ecfcc59e6eba53 -> cd8276527ec82c7184cc77e4bedef07be70aba86f80f60f861ae97b74a9fc935
~ _fm_get_match : 64 -> 68
~ _pnp_rotation_to_rodrigues : sha256 45aefaa17740b4b5e5df9f9fdc2bb8aac0f4cfdf5120f1159a1a2a60cd9b7280 -> 1e89bdb69be53ebf5f1a09f15673c804e3ce742019891fb7f8d21296cf8510de
~ _pnp_rodrigues_to_rotation : sha256 da9a0f3c7813059144937f0ef87490b88d8f0f622ad6c9819b0e8f68172e55bf -> 96fea6d7ef361dbfd13a582b1038d08706cc25fdbee0000589c7e38f4fb0d863
~ _pnp_rotation_to_euler : sha256 1d58e866714c26482d2b357004e12abdc3818a1c57266fc09d9a1da1ff0c4083 -> 0644e312f3bb41be568467071d72e748b726874d9337570aff395ac1f6ca882c
~ _pnp_compute_reprojection_errors : 164 -> 180
~ _project_point : sha256 05df3e40592450a8bea23b56024f11f9f8ddb8abcd191e100bba811d40bec436 -> b46ec6b63aa6b06a7bbdd2bfe3aaf68d2b0466984ebf96eefa65dcf8c4e3eb87
~ _pnp_solve_dlt : 2672 -> 2520
~ _solve_6x6 : 464 -> 456
~ _pnp_refine_iterative : 1356 -> 1380
~ _pnp_solve_ransac : 1472 -> 1436

```
