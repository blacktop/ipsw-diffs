## liblangid.dylib

> `/usr/lib/liblangid.dylib`

```diff

 140.0.0.0.0
-  __TEXT.__text: 0xa94 sha256:075d93d6462f93866469e2bf28c31577e2d3ba591f5e6602511187fbb378520d
-  __TEXT.__auth_stubs: 0x130 sha256:967d0182854bcb803b75101c31bd6cccceda927f23be0302788ab6dba6679077
+  __TEXT.__text: 0xab0 sha256:62e11c840f1ffa0145a314f57ca3c49802820506dcdefce6e313804b4d194c86
   __TEXT.__cstring: 0x173 sha256:d86d9ab8068aa10ed59dde0c0074f6ed50de79c3b164aaa1542376d6eb62080f
-  __TEXT.__unwind_info: 0x98 sha256:6b3eb834933527b60fc4d61191241cb093ce4d146fd56590a7a94145b9b6fc22
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __AUTH_CONST.__auth_got: 0x98 sha256:85ada57e1f601e962d705f389285adb4e74f450bc00672240dfef7399d82457f
+  __TEXT.__unwind_info: 0xa0 sha256:e681301c7e4597303f61893301c2d15513d38206dae60a641b602aa105b1b64f
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__data: 0x40 sha256:2ef4656d02cfb45347e2bb830799aab79d899ae45081de2a4906fe1290b69b93
   __DATA_DIRTY.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /usr/lib/libSystem.B.dylib
-  UUID: B6753BD8-3BEE-38C1-A50A-4A04F30E1648
+  UUID: 94E77892-424C-3F13-8BE4-2FF333D5DD20
   Functions: 26
   Symbols:   57
   CStrings:  17
Functions:
~ __langid_dispose_internal -> _langid_dispose : 148 -> 8
~ _langid_dispose -> __langid_dispose_internal : 8 -> 148
~ __langid_create_with_datapath_internal : sha256 6ebb49b743572818730a1bd1b397dc5a46bf906e04f62d4e0c3c569087401a7a -> cc649cecb32bc6f85eebdd0a128c4b14729e3080d41159fbc0acb3d3151e95fe
~ __langid_env_create : sha256 b5459b2df7ede1b1938444114c208948f49f28fdba3e58ad6e3b710e478428a5 -> 40edd18bd8ee63a4e69faf5ad4cee7a58de500b1e631f1819eaa651ba751408c
~ _textcat_Classify : 96 -> 92
~ _langid_languagecode : 76 -> 72
~ _langid_identify : 176 -> 180
~ _langid_consume_string : 364 -> 388
~ _langid_highest_score : 84 -> 88
~ _langid_identify_withbuf : 180 -> 184
~ _langid_numlanguages : sha256 314c07473c6d6b7098300393da1dff7baf36359c9e6f81236215993ae7128fc2 -> 41527e1698e4ea8dba86d654034e6bb3aaf99edd797fec452ae798622093905c
~ _langid_create_with_datapath : sha256 fef355435c4034036db0b080ecc04215c73680cdb138f129c3cf50457a87d65b -> f612c42b0c86800c60ad2ee49bfb3e6db1713c0e391c2a007700f77ed3669f3e
~ _langid_global_dispose : sha256 65b2934a1bfcc832aa322483af37126b34f0eb0ce93bf8af906ac45353380534 -> a8464dfcb3b7c8d4b8c0f1823ece6d0a879dce8306646958c44ca262109bdaf8
~ __langid_env_dispose : sha256 73e5f445115c07d61d79257f40540db08c89ee1a8ca0f136957e4937417d4219 -> 9833b93a0aceba76c9340d9754d55793020f5e6db3cf43bf40e44356f6d226b6
~ __langid_dispose_internal.cold.1 : sha256 7dc5c61e52ca84cdaf3667e78ff6ee30e77d0cae6304d6a23d293c3c4a13211b -> 2a6d180cdc74f2e52a912586cc8d865be93ac7193379986669e0081a98743b71
~ __langid_env_dispose.cold.1 : sha256 44ecf95c594d02c2a90007b32002e52b3974c2212dee0b2262fe347afe71fcbd -> 1e0ca70dfd8666d1a56ed3f407449ef1a3b889ab7fdc2b4b5946f3b526467c76
~ __langid_env_create.cold.1 : sha256 1803ef2160cde884d0abf497cfd67beaaba89d4b291cffa30488c94313861562 -> 0c196dcb1dbca72305fb1a2a905fde654f90e26d1e752002e0b8d16d4364357f
~ __langid_env_create.cold.2 : sha256 4368c3d9ea25fcd56a5ce93b5b79bc05cc1dfa2eaf9d4c001ec93cbb07378c13 -> 117e9cf98a53d0c01967503c7e43e1a0d1275f8c9bfbed14e3b2500dc299b6c8
~ __langid_env_create.cold.3 : sha256 bbb7b9772c2a4147c75b54e1f44caab2876d081b837c539358b752e28492dc31 -> bc90bac3fffe82141a3504eac05f0ccecfdbb638bfc51cf4169a5c1b1760f37f
~ __langid_env_create.cold.4 : sha256 f3a3f995b91c096a5fc9a42b72949e17e7ac52a54246556089d31a93e59f8eeb -> 43dcb5f23f5d3ddb136d1fa6eaa408f5c45ef6dc8e3997ee677b1a040d1790c8
~ __langid_env_create.cold.5 : sha256 4012aa509e03c84b08802af8aa3fae3205147c90a01f460296f12990ae776385 -> ee4dcc6ca2aa408532e71afe8673f7f21f92e32b95e497709f62a6b36ec1c303
~ __langid_env_create.cold.6 : sha256 e06f6e10923d2b4b562418a22128ebdc4f2a3d061b0915d1e91d10a399e4e899 -> 214b6ac1d860ec4492f875b1d263a8566870fdb71a68bd0231759f51214fd08c

```
