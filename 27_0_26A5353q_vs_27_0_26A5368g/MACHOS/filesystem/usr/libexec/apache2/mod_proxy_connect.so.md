## mod_proxy_connect.so

> `/usr/libexec/apache2/mod_proxy_connect.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x2ba8 sha256:289a0750bac4aaf4bbb0cdc47f4e3c4f73cd20445455693291644fc64c1be1c8
+888.0.0.0.0
+  __TEXT.__text: 0x2ba4 sha256:e08c11a7eda703c05f8e2c4efae913057b45e2150e2a8f70a2fd8e3473a0d0d0
   __TEXT.__auth_stubs: 0x240 sha256:173fba82273ad734ea4223a73648608b4f5be18667f7be3145c712100ecb6e5a
-  __TEXT.__cstring: 0x3c7 sha256:3a3dcb03172f5f1855b65a7f841b8d81c232f02d893fb0c223af679c380cb8e8
-  __TEXT.__unwind_info: 0x60 sha256:7f90456d28cc66623fdca1d36a879281ba371b7b448c6ffe762c6367c7d17bba
-  __DATA_CONST.__const: 0x50 sha256:542ace9c8535093ecf18b887e68660ca3fbc7a1935b7dc47d1ab8d30998b3a94
+  __TEXT.__cstring: 0x3c7 sha256:4fa3ca85ee271d8b44f8fdfd847ada615b259fad062c1072e996e40d3c1f117e
+  __TEXT.__unwind_info: 0x60 sha256:8bb2cd7211524e87c0b35364d4381bda3addee430ac7ab2544b914ce2059f96b
+  __DATA_CONST.__const: 0x50 sha256:62d9943b25335c05725d6afdd2a5987f343f94d947ddc0a4cba3f0fa90e33815
   __DATA_CONST.__auth_got: 0x120 sha256:414295a3f601797d69faeb2174672d2f3ad7c2b5d9c46acca93ba19343d08393
   __DATA_CONST.__got: 0x10 sha256:ff0b8ad4b66c6219c3b089d612c10b5fd12040d32b4d9842d0c81820121b7ac0
   __DATA_CONST.__auth_ptr: 0x8 sha256:f769a899f9f4987bccde1f03c735f522d58e0b60ea481aee5432004945b11a43
-  __DATA.__data: 0x70 sha256:8ac66556ae1e83c0ba30e04b1b44f22f7541a7ff6a8898797e53b9ce61786eb0
+  __DATA.__data: 0x70 sha256:c86166c3ce7de672f85f478dc95ed26938e8eec037785745213f7ad9844a4d72
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: E445519C-3E9F-3F3D-B75C-3E0EBBCD3F56
+  UUID: 0F9089D0-717A-317B-9E14-769D37FBF1D5
   Functions: 7
   Symbols:   48
   CStrings:  27
Functions:
~ _create_config : sha256 3f47940854a507901213d5103dd0878f98387e9371b43c5b97837429f1cfa842 -> 04b24b83981fde1f5e7726b87c0ccbb67b8908a69c8825179ba2b29fad0c9ba0
~ _merge_config : sha256 45908f1e9527282082ce8b856a787012a7da2b04963e3422bf6ae107600efbda -> 269860143307a7bb3a4c1a383dba75e69dcfa8398ef0c101a7ec9bac8bb02e33
~ _ap_proxy_connect_register_hook : sha256 f07051b6f06728b846fda99dc73435fdd8aa88c6663e54731bd5c233460e01df -> 20772f105ae3d766e77d9c1a27531b9bcc6e0c79f57fda23f9ee3b9b6f5116dd
~ _set_allowed_ports : sha256 9e5652adb2e80262405f93022fec2109f6d21b37e08f0ee03a8f2cf9a40c27d9 -> 11666d5d52daa8745b45158a4055797ed7319e6c0e40f35d57242c4cd5670c3c
~ _proxy_connect_handler : sha256 9f90b5313dc0b10f5b83a9243688f4f189c5ececfd3dc9fd2b5215fc7db3f14e -> 570f65060d0a9210994673783e19a2390ef9f7fdd6f677868c28e5d4a1eb9f7f
~ _proxy_connect_canon : sha256 fc55c2d34c56b1cce1bd99360fbf13cbe26b5c0604ceaa5427e3e38c02c3fee9 -> a4f8c839ec2d2ae5c91dcf1be91e5f327fc478819608beb8f7baafcf5d1bb2a1
~ _allowed_port : 284 -> 280
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/proxy/mod_proxy_connect.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/proxy/mod_proxy_connect.c"

```
