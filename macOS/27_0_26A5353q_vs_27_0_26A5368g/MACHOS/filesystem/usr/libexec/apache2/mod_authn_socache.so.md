## mod_authn_socache.so

> `/usr/libexec/apache2/mod_authn_socache.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x2714 sha256:19255f11fc980a35cdc1d1d0a8d2d178258859834914427416ebd385ec25fde6
+888.0.0.0.0
+  __TEXT.__text: 0x2720 sha256:ca7fc3eb0347858bb0320da41ca543f28ac74caa576369dfa7ebc7b1e16107ce
   __TEXT.__auth_stubs: 0x240 sha256:f0c44a3960512636038a93b9babb2a6d88f96f7d65436405eccf6814d1e60073
-  __TEXT.__cstring: 0x65f sha256:e7444a7ae25de457e94be11b2dcaaf8b353a866b807ed39003422f460fc2ca89
-  __TEXT.__unwind_info: 0x68 sha256:10df19dbcf4a7bedf3383e3511968db553ed5f5bf12aec3b21d6e6445d358445
-  __DATA_CONST.__const: 0x100 sha256:639f050be473f1dd42c6aeaaf9719ca766fe6bacba4811a8ce95ded7cca19f18
+  __TEXT.__cstring: 0x65f sha256:3d447b7436aef27b972089da7c8339cd8278870a5188b3572b1fdbe9044c6784
+  __TEXT.__unwind_info: 0x68 sha256:6244dc30f3d321f743f7b1f7922ffc7ee1e1a39ce1e44e6aac7ffb32253d10a4
+  __DATA_CONST.__const: 0x100 sha256:90419701f33455834307458933d6b94efe79c1c8d8057dd15d3f00e1c112abee
   __DATA_CONST.__auth_got: 0x120 sha256:f12e98bb24e56993a4a1ce6a13c1db97280e18491b5c8fab0cf6d79666495bcd
   __DATA_CONST.__got: 0x10 sha256:4fafbd02d1d8c5ab725c11be2ce635fb1b5c356712e6b546df124127b14fe482
-  __DATA.__data: 0x88 sha256:6ad2ae493f07c5f833ced3a25795788391ea6297a5bfb98afb9bd1ffe0608741
+  __DATA.__data: 0x88 sha256:4486691696d0410480d2f1583e8cfdcbcb045f9125bceae99466fa608442a686
   __DATA.__bss: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: BBECD5FF-DC38-36DD-BB3A-2EB448CAF02A
+  UUID: 9DCEE4BC-91C9-362B-BA43-3571585D52FC
   Functions: 16
   Symbols:   63
   CStrings:  39
Functions:
~ _authn_cache_dircfg_create : sha256 1322aee817fde1352de0bc6b6b0b967c5e460d09f6a17b2110b9e81370c2fd40 -> b23a843756e9d964e345d581d034e9045b47267b5dc433272a5a6271c4e654b6
~ _authn_cache_dircfg_merge : sha256 70e164ce4ae072c8c3c6041d8708467037bd7d191a17a7fba54d24887a47c3b3 -> c9afadf9d2b226f0d149bcbcfc2399ebf47fad4e5a5e3418fee967391b6da4ea
~ _register_hooks : sha256 94d71916f70e0e7d0050385a8e04eed2f31e218cb37d67667e380b5813344dba -> 7127bd2faf10e8ffd0561093522ef72dbf67995efac6e13e64b985f2be564703
~ _authn_cache_socache : sha256 f70dabc44f11346b6c5a9b4ecba14dff20c057f67d9401f824c46ffb9dae6822 -> dd3aa8343094283792f0a702fcef72b1154c42bf2d525f3378a4c35d618968d5
~ _authn_cache_enable : sha256 18475c4603d5c0cf83e64c1c7b3be1e924c07403f5c02873ba35ea32384b70d7 -> 621c0d65648488c6f26a59f9d3c0f66d35459be02a59e45c74434bc06cfe165a
~ _authn_cache_setprovider : sha256 d6779b149eb24c219652d34abf1fd8ec109c410222c43fbf023577380f7e0f66 -> ab048807127993058508cc4f3d8e5cd5653505eee5999d7bcd66abfc39ff5728
~ _authn_cache_timeout : sha256 57cd23333282e512b9036c97f35bfb9a232452ebc1f72e215dc087b1d69ff979 -> 7aacbd10dcf997e86dabbf5bcf7978b512b776ff9b01cad9b1783ec00ed5406c
~ _ap_authn_cache_store : sha256 f2a856f8f1ac57f998c38b7e9c8b6168a9468906cdcd4d5dbea27f26d727c0c9 -> 5a9de1907f0e05f78fd26498cff41417e68dedd1fd613033f82f8b829e52e01c
~ _authn_cache_precfg : sha256 520ca65fe1a4020ab4a9eb3f77f4f094ab5e1556d0fb8108066102deb1c5f31c -> 6597bfa65afa37dab5ad7f03404c7eb57bfbeb8d141e0181b901ad2797febebc
~ _authn_cache_post_config : sha256 b05404098b89fe17800f9db060499bc9fb5f0d5c334660b06b60338893fed878 -> cfad5da4ce54fa500bf73a5deba1cd9782242aadd8b7192b84f3f19babd0c9ad
~ _authn_cache_child_init : sha256 bbd33479c54736330acd16456d1e88707999f448d56e9a865ac15d30a7fddf95 -> 9a55d0a1d9f7380d7a2f2df31b8d3f558573aaa73d040839781e30a73f7d5cd4
~ _check_password : sha256 8c120969b46f3bac27499a04e634407c09529c9728531e2d5f5e2a50c78ff959 -> bb7b8946c888d815eb353c54108a41655129e878d14ff9c06712e22cc30ab3f7
~ _get_realm_hash : sha256 f202313e8b71187717426fbf82301570412c66438762c82489ac5323a3cb5306 -> 3a62301e5416a3ac9aa6ebf8b8d90f5cbba75fd4695223f95e321de403b52656
~ _construct_key : 436 -> 448
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/aaa/mod_authn_socache.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/aaa/mod_authn_socache.c"

```
