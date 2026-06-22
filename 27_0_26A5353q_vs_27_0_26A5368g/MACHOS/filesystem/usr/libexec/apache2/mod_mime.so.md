## mod_mime.so

> `/usr/libexec/apache2/mod_mime.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x283c sha256:e9751be6831877c139eccd9fab00d1bc0205a54b2a6897fec12a6a30e106d663
-  __TEXT.__auth_stubs: 0x270 sha256:4edbd1c2e9542e2264145d65273b6ad3a4e4a9c1f017f4aba6eabb04550e293f
-  __TEXT.__cstring: 0x864 sha256:d81d98891f93e978aed7e6e232183d4beaba54f28aede06daf3360c86998c00a
-  __TEXT.__unwind_info: 0x78 sha256:e6743ab885a513ffeb1ac4f107be77caf04de30a0c9059eeadd25f8605cf92c1
-  __DATA_CONST.__const: 0x2f8 sha256:839e763918ff001f9697b3a2de119cfdd9d78c05c58a3028a5eaf376867b49f9
+888.0.0.0.0
+  __TEXT.__text: 0x2834 sha256:4ee0bfbf586d668314a29a4d8ab9eebe4544eaf09682704024c98015a8416f45
+  __TEXT.__auth_stubs: 0x270 sha256:1ffe939a4c1d5c3fec47792535d280480c6e98e5ba7b193ad1dd81950196de21
+  __TEXT.__cstring: 0x864 sha256:ce474b83e4a3bc0bc537a29f89f9c7b88b442cb9b2cf9d479ee694cdcc6ec209
+  __TEXT.__unwind_info: 0x78 sha256:fe5744bb745cbdccb175bb41c3a49f9490f631c5ce247e7c0d646b500fb91226
+  __DATA_CONST.__const: 0x2f8 sha256:a5ca5cde6d55943115f82be16ffca373f47f2916bc337fee2746eedbc31d8950
   __DATA_CONST.__auth_got: 0x138 sha256:b070d35edd416f3377cd6563b76486ec963d3c2696d1df3143d2675cac2bb930
   __DATA_CONST.__got: 0x8 sha256:7129bc16bdb1a29e6d5213fbc43dd52e3987c8ba6fe1da2367be517e270f2e85
   __DATA_CONST.__auth_ptr: 0x8 sha256:1e7b1d8d821a2120c73f102dbf0ba88c1c8482e2c958dbcd43f60cca5028f772
-  __DATA.__data: 0x80 sha256:f0c04648ed39ac573c86bdda38c92616f3905f2e590634c369530cfdcae99a2e
+  __DATA.__data: 0x80 sha256:616634d467f52aa9f6b2bda850d09acfcd3cf0ad0541f5ea580ac66eb8c26a6d
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 66D9EA6B-4FE9-3AF7-883F-B5A34D3E4391
+  UUID: 8A2116BC-9ABD-3E84-9824-34E26F025414
   Functions: 18
   Symbols:   65
   CStrings:  63
Functions:
~ _create_mime_dir_config : sha256 b65adf962cb8b869ccdd5790762e4d5e280b505da851046876a71ab5daec7ad1 -> 51c8e763bf45648b479aa72b44da54d841f1f0e53d8cc6ecab91a9b48add765c
~ _merge_mime_dir_configs : sha256 564cb7186589e6a0912206fd3bf22921b93115b93f6d849d73e7122ad7010d4c -> 036cb3f7f1d0266248971eda21c8bac1123042268c9b3afed8d8ac08a074a830
~ _register_hooks : sha256 89a008e38c22bb32d1cc47181dcf615ec96081355c7fb6427dd7e49223b863ce -> fae71f53d79e9de623bb8168194f642816d4d867dc4b46886a523a079f7b82a1
~ _overlay_extension_mappings : sha256 0ae2ebb1eaf0eb558d64235373050f05a5bb43147d4bee161838534bf43091b6 -> b00f964f217a2ac62a465b14a8822571f54dc0048808b9ab8fe9ed4ddf4ef52d
~ _remove_items : 284 -> 276
~ _multiviews_match : sha256 0835bc107fe1575ea8004ee55a82ba34c9c1c43ddd64cc14936b96f1370c63e2 -> bc8e6efaa363a86838131da80018cc050d324accae47e7f5625680a60bbf5b1b
~ _remove_extension_type : sha256 4e5d6cc4a20559e42251e01c5ba01ff6d2114e439566ab43a0a759b21f93f041 -> 727fd2c09eb8f7d8ab549e95bd627251959b778dd66b86c37986a73b97058f5b
~ _mime_post_config : sha256 f756e2d1b54cae102922f2e56b7fc06c50c8f46fbe4e06de6f71e7043f174d4a -> 656968edd9aeda8fdc8aa83d231245ec6bf6821aa7bec428ba263632c4ec8c8c
~ _find_ct : sha256 352e85288385d0bb26c7a2ca0412c12e0b013b7d4983587a716b8035783b17f7 -> f1a3b8ebede961b9132fabb1b115f0c4031e7acda4c6e2396b33cb441309cf6a
~ _analyze_ct : sha256 34d19715ae18aa16fa8f65f867af3ebe7d7d67a598391d7ca847a87f477ead34 -> 626f24d7004a58fda68821a39cea64ac184ae82b8bd3aa15335ca8f5835fc2b2
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/http/mod_mime.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/http/mod_mime.c"

```
