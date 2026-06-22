## pam_env.so.2

> `/usr/lib/pam/pam_env.so.2`

```diff

-230.0.0.0.0
-  __TEXT.__text: 0x148c sha256:2e1fbde6e9a5235cbc527bce969fe8e05e9c743866f5791409a9c6a25ac78bf5
+231.0.0.0.0
+  __TEXT.__text: 0x146c sha256:2032d528c3a6856fbb86233b12d9ab35a4428852324a6c22abb45919bd224322
   __TEXT.__auth_stubs: 0x1b0 sha256:a5d0495659c55585e9d33c218e5a096123b9f0ba4cef19e1a0830e0b501463ca
   __TEXT.__cstring: 0x691 sha256:26515f4b031eb188b433c57fae73da191a0d1a3da163231e8fa58a8f3c062de5
-  __TEXT.__unwind_info: 0x90 sha256:dad3f00938faee3cc4f9a4633b7d419097164777c82f965a27b1478b5c0547d9
+  __TEXT.__unwind_info: 0x90 sha256:847cb29ca408e308476af1f5012d46fb1c5e3ad91e1ad7263d8aab83e11adcdd
   __DATA_CONST.__auth_got: 0xd8 sha256:74b1f610eb69f548ed94373f82b0e1c9d4e406931bc0aa23fa2218cdad04e863
   __DATA_CONST.__got: 0x10 sha256:79467e098623fd07a634a9458d7debda46df3ec470ecfce1cfc1c3f023e0dd58
   __DATA_CONST.__auth_ptr: 0x8 sha256:471d27e0b2648519f10126c65bfd8a6130b73d89cf7d44bc120cc39ca9172f12
   __DATA.__data: 0x1 sha256:bbeebd879e1dff6918546dc0c179fdde505f2a21591c9a9c96e36b054ec5af83
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpam.2.dylib
-  UUID: 0F6F1312-7B6D-36BB-9292-6678C0459723
+  UUID: 3CD938E0-734C-3333-A13E-D69D2CC52580
   Functions: 12
   Symbols:   43
   CStrings:  81
Functions:
~ _pam_sm_setcred : sha256 4d778af714e1c14763fa60fb03f3e7b60b35b0b660863785ee8352f1915009fb -> b28c78c55c596fad9e3fb80064c97923795a7c06d5ac8b9f1caf744f42aaa719
~ __pam_parse : sha256 169d2c21da9d36d8fe45cdf427680a77ef5d2660bb52ce0c8862a97db302ad54 -> b58ffc6bcff1a507a4b62a6e631ed8bc96810a445f37ed67e80d15661728a4be
~ __parse_config_file : 1788 -> 1804
~ __parse_env_file : 764 -> 752
~ _pam_sm_acct_mgmt : sha256 a3c5ff27156f162137db992055dbd9844f790d8d618f68e413b0798374ffa20a -> 7c051c06d7112dcd50138eec7ed1afdc17871bbe830fb5c125b958985a753922
~ _pam_sm_open_session : sha256 44893f7056bc4874004037af2a961bd805c8a8990bd10c98850685c7cd8b263a -> 3ee4bd460767b99582fda2379575bc8650b33d684293cbbe5fbae6a21ae43685
~ _pam_sm_close_session : sha256 eb46167bb0d994cda2eaeda27ad843f2a20495c8b03667b633bc322eb0daf93c -> 3bbeaafc8a6de2ca34a830100cdd61bd6e184aaf299f5c9fd6b52a165344af28
~ _pam_sm_chauthtok : sha256 f29c9e7b089a6f4c8fa96dd43dc9ee50e65ea650903046ea6c95eedf9c153b82 -> 19fe525c8d83d022dbc062918ea708193af392c6373e693e8aa0e2b932552304
~ __assemble_line : 376 -> 352
~ __clean_var : sha256 638caf3d04e0ff7a24dcfea9e309e2af8a269459a83427f57489056e982784d3 -> c4ec9f56236b95d92e842193af1d8338d62a184520289ce1d7d69c5d7d6fb614
~ __expand_arg : 1364 -> 1352

```
