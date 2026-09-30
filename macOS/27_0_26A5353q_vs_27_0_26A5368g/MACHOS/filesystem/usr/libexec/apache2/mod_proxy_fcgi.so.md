## mod_proxy_fcgi.so

> `/usr/libexec/apache2/mod_proxy_fcgi.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x6170 sha256:367827977eea23b331e159874c6633f0d5fadbc7769fbb0bd9c3a7b893467958
+888.0.0.0.0
+  __TEXT.__text: 0x61a0 sha256:fc294246895cedb4855f45cce1a7d741316ed197541867141750a2a476fc2f2a
   __TEXT.__auth_stubs: 0x4e0 sha256:6a0f69dad3067d2c7cfcd23be08a30f0a764b0733684f5b7f63291e65b7ca5af
-  __TEXT.__cstring: 0x81d sha256:5987dc092eda6348f89a0779ffe1708e8a852691dbcd86ab85199c8bd6c70bb3
-  __TEXT.__unwind_info: 0x78 sha256:a9ee76fb630fb8463eeb6170a1c4404afbf362acb5bfc404a1fca7a4d78198a2
-  __DATA_CONST.__const: 0x78 sha256:2650626fc12c46ff2f2ba6d752384ded1ebacd59eecdd7ec0848c368bd195f5f
+  __TEXT.__cstring: 0x81d sha256:01668ecdccbe8d230a4dba47f25df1306617416f9728760e386a902532e8f6ba
+  __TEXT.__unwind_info: 0x78 sha256:1c93da55d483c2ac07b5a55036bcec39f672e99ccb40888d722f286977206611
+  __DATA_CONST.__const: 0x78 sha256:d2c188d2bd598648cff7dfa9eac1bd23980de601a6f35a1351fef942f7110e02
   __DATA_CONST.__auth_got: 0x270 sha256:1f055b69234998e9a449e351cd7367fe74dacaf54a69a8757f71d04cde497bac
   __DATA_CONST.__got: 0x18 sha256:4ad7ceeb63ba4d11716309a80da11e037e8034cd7aca8a35966d72b10f352e35
   __DATA_CONST.__auth_ptr: 0x8 sha256:16509fb02ac553833cdea6757dc66a17d18d5246d6de30695588794d0743be82
-  __DATA.__data: 0x70 sha256:68ade8f319f3147ca49fbc7c9b3ee23da8d49e45c47c259844cb6fae28557c15
+  __DATA.__data: 0x70 sha256:38f084e256d8ad7ba255646d05a6e83d02346eaa9f33eb896295fdc101f543fb
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: DC662D31-C3E6-3670-B10E-B6EB13EFC136
+  UUID: D071F3BB-1F16-3BC5-9E1D-5B1F1AC34C42
   Functions: 16
   Symbols:   100
   CStrings:  73
Functions:
~ _fcgi_create_dconf : sha256 cd96fe0982e2141276403ff2457b3d622adf80fd4206e31b66919dab42b6119b -> 3aff071a99358528c63d00bd6fb401daeca14953cab66396affc5b425d2c9f9d
~ _fcgi_merge_dconf : sha256 3d5f63f3f8747a42168afa3a0e06db8d13c85977a5145bb1302e507aec5dc26b -> 8926bc835e9462cb4c5e01cc6bf59df26358aefbd9241f3b52c2029d4dda7346
~ _register_hooks : sha256 12208de6c6c8d5f4ca9da07c937c8eeea2127c723b51eee31edd8eac71000072 -> 13d3345a426055b04db858d6439dce68c9f4958c7f770a06ab939673b0bad3b3
~ _cmd_servertype : sha256 174c24497fea369202a070f707e3a5d5e3ea7f00bd7c474c1ebbcb921abae0da -> 152ebd5401d475e2984dd0d36a739291914102e73bd7ea4e57ba650d529e733c
~ _cmd_setenv : 600 -> 676
~ _proxy_fcgi_handler : sha256 f1499bc7e3160243e24d6d9b34e876e8ddd633cf1e5565d4275496bd007417e0 -> 499f3a9a87e666d870bd9a935e9633fda589762068d17f86bfec30ee6ca8f606
~ _proxy_fcgi_canon : sha256 c54e8ea56be1c6f7e7f5188d86c1b7fc1e62ae86643c647595f798528502b2c7 -> 82ac0cb800c331bbffd6279d11d4ba8fd34fe25021d9942b9f299654c2ff9663
~ _fcgi_do_request : sha256 8dc7ab738749985e2ecf51b5223bc31935031eb4341966cfce220b55bc0cb3e4 -> e9c2851a0b678a730b4cd3cb5a084c420c5935793f8515b05b13434182b1807c
~ _send_begin_request : sha256 f38a748a099fd922fb94a7b0539bffedadf204b6f2046bc03eecc520fe61dcc8 -> 1ecc2640520a42ebcd105abe5fd2419c2cfe7b3040393ab8c571ea5d0772ce2d
~ _send_environment : sha256 99fa4bcc4d62ca8b7881ef7e4b26d083f54deda855eda67b80e61ae42468c70f -> 8e22ecf1d0d0d60f6adcdd4e8729f1d194e8ea19b896be75b5f91e3da465d7a5
~ _dispatch : 5420 -> 5412
~ _send_data : 556 -> 536
~ _fix_cgivars : sha256 3ccbd1c7f0130d3902049069bfe88201268f0132be72b533c7abcd387797677c -> 88cf34e2853f47784940ce79b44b875cf627a8e14cb2d54149542816d49c130c
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/proxy/mod_proxy_fcgi.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/proxy/mod_proxy_fcgi.c"

```
