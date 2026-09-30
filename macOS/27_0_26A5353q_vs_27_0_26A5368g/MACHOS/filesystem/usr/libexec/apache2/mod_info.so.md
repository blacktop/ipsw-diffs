## mod_info.so

> `/usr/libexec/apache2/mod_info.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x24bc sha256:88b6397d7f7f59f7027428d71e77688d7dc1c60fb8c6bdb20bf3a1905ceb45b5
+888.0.0.0.0
+  __TEXT.__text: 0x24a4 sha256:b30eedb1d18ca741b3d25641f0ce752e1b18a052d8e5ac2ab3614ae050f1bfb7
   __TEXT.__auth_stubs: 0x210 sha256:da53477ab1b3253d9c3b049dbbad352cbede33a5e314c3f737a2563707bdad97
-  __TEXT.__cstring: 0x1457 sha256:eb3b665339d8985704496dfc9b602a307a8165732726ab73d3f449c94bf7e5ae
-  __TEXT.__unwind_info: 0x68 sha256:d9f58e66102ed96a2d70c98d185e5c7f9a68283b8567d0a0a77b67631433364d
-  __DATA_CONST.__const: 0x340 sha256:a35ddbcb1443360cb5da13912f2eacb3f5fb01449775ea382d0b65bfd52ec63b
+  __TEXT.__cstring: 0x1457 sha256:12dfd54fe986ee0c14444e8b5dba1a7de556f8e8dbdaeb6630da3324c28dae7d
+  __TEXT.__unwind_info: 0x68 sha256:5b455199069b39c12cd451a94fa1eddfb74cbcd221fde33550451d84895f9fb5
+  __DATA_CONST.__const: 0x340 sha256:d222d68d58e0ff3717039a59c91ebd0818defeb33adcb30a22b1b3a0266675d0
   __DATA_CONST.__auth_got: 0x108 sha256:38d3690e8ea19d670ae4e8d017cb9ad2a39aef8a1bce6f90d081b5fcb575f967
   __DATA_CONST.__got: 0x20 sha256:2b680dfdec8095126090edff0c65fd2686bab01dc6bdd7cffbc151629b14d87b
-  __DATA.__data: 0x70 sha256:250eee276448d548b4c020b137fc20c739478e4d0fd17ddd78819b480273342e
+  __DATA.__data: 0x70 sha256:560b38b505200e02c93ae5c76b5807a226ceb53abcf506633c769477a0d9013e
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: D5BEB64D-AC22-3FD2-A46E-2E61E038A71A
+  UUID: 0E1C81E3-325F-380D-8D1F-CE70FF2D8010
   Functions: 29
   Symbols:   116
   CStrings:  160
Functions:
~ _create_info_config : sha256 de99bc79de1d6c21ec3c34ae028967dc96b2cd6de2b43a158a16f13150e01a34 -> 47072a54156444939cfbcb55e190c0b44e3cbc7e46b2bb12c5da1c1d23bf70c5
~ _merge_info_config : sha256 4df81214292f0d06c02e7fd3dbc691305ca03aaf290e40c07b82124bb2f0c5b9 -> ff07129a94880667bfd991bbd654d98e2132f0b2e407779b72b95ab1646d46e2
~ _register_hooks : sha256 b23c2854b0da985646e0b4c0fb6eb23b794eeadbf97b0f9893ad0aeba6e117d5 -> 426945ec4510f66fc0fc3ba3e228c1151a3fd1c1ff4666f53809484d672c5367
~ _add_module_info : sha256 c3f58f9b60247947f99f60d167ab9770f247b01b45c4201897a7c87f061c6033 -> ffd2e4cb45556595ef4ae77cb96846fa3eb241b91e37d0cd6b1322542ccfade4
~ _display_info : sha256 2795eb6f46f84da46a68fc719d030ee33ad843a340417621351a9f858018cc1d -> 82d887d7fdb61dd7c150847f6a452ca03163956adf05401f7c02f13d88cd6e06
~ _check_config : sha256 5b823dba14f0aed0ffadace540725acd808680791140cb0391e24a236779cc9c -> ba9cad91685035381ca6c1197e75578b1610b0f92ffd1e924845b50fb3328885
~ _ap_rputs : sha256 b0ac63363eb437b144ab190ca56db15bb1c693cc2f63cdb31a9a126d16edf36f -> 910f6da22b88c0a07d0ca58d581031148f267f4af75fb8211c52396599d6f773
~ _get_sorted_modules : sha256 86c9dc9b337eee96d8214802316e9d636653a604aa25871e802c52620a7a3802 -> aa80e289a2b0e15c438cdde98db1f2dfe09712967f979fa90e72347fddd36fb8
~ _show_server_settings : sha256 eee2bee646e60a9eff9f5741bc817c5357958a9f57dd90a70d6c856b92321b7e -> 54752d1272b9a19fc0558827a320af2df382dd047a57419590654d926a4500be
~ _show_active_hooks : 548 -> 536
~ _show_providers : 564 -> 556
~ _mod_info_module_cmds : sha256 1e05740d0516cbdf98b618280c2ba2c9758ccc0e9ff2ea68af9ce5f7fbe6afd3 -> 7cb4ef86fdf128dac6bb0ecd75fa998f502899eea3e7418727125934ad44894a
~ _module_find_hook : sha256 232efcdfb8c72b0903575649d7f14b9d5c9f48b104ca7a851a38bb0646a1e624 -> 8dae7bb9e4526d13550fcf83a93d3a0d930d05247055d5da58314a93718da9d2
~ _module_request_hook_participate : 200 -> 196
~ _dump_a_hook : sha256 6f22cd7d3599a190d47afbc75b1bda6798e52224e9a310020ccd15aa6435a095 -> 906f3a5bada8e957367b99c59888fbcb4cb18b991ef16f64d0687179a61b04ff
~ _mod_info_show_close : sha256 6e68bfebb5c900d221af141c48601c9bf1eaf3f8448b406c8d1b50ebdeb7242b -> 5e2d8c62c41f4bda8836d7adb5ee4026051f9fefb5092d56433e8fd1e1222222
~ _mod_info_show_cmd : sha256 17495b0239aecb43603ca02e446b78ad98c4019f4cfe69890af2a012e88160a7 -> 38d544c9202839d426edb256378414f8fbe5e10f05a621e709b98aab5fd3bf21
~ _mod_info_indent : sha256 033a8081eed7500f8ce5ae3212c8b22bc832af1b204ae9d33d3427a19a6eeece -> bffdd6742f7b1d06a5edf38191628d875cec983dcd6f99d52ab32dc426ef8112
~ _put_int_flush_right : sha256 11486de481a11301c836fb0505b145e7ff86c123ff259299d1121348f08e6f75 -> f24157215f3928f18e313c2584abb427378bc5adf6374cdb295297a43c442bcb
~ _mod_info_show_open : sha256 ffc765e76e4dc3fb1c356ffabffc69f8874a46c5359aeb87879f6dff52ab24e6 -> e4af34d13a3e926806c1d5fb7d019734295408272dae9d546a21568da351d903
~ _module_participate : sha256 6237d119c0ea7fcbd10b1bc52416c97f2806f64f413ca3e822abd64048bb41e7 -> b10cb83757a88595b0143301ad131510f45299f02545f3889831cdae3571792a
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/generators/mod_info.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/generators/mod_info.c"

```
