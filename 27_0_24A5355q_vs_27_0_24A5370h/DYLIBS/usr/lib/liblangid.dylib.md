## liblangid.dylib

> `/usr/lib/liblangid.dylib`

```diff

 140.0.0.0.0
-  __TEXT.__text: 0xab0 sha256:62e11c840f1ffa0145a314f57ca3c49802820506dcdefce6e313804b4d194c86
+  __TEXT.__text: 0xab0 sha256:1608e7bfbc3e7d303871c9d04a8322cef5b49a34918ac64fa06996b7b791e80b
   __TEXT.__cstring: 0x173 sha256:d86d9ab8068aa10ed59dde0c0074f6ed50de79c3b164aaa1542376d6eb62080f
-  __TEXT.__unwind_info: 0xa0 sha256:e681301c7e4597303f61893301c2d15513d38206dae60a641b602aa105b1b64f
+  __TEXT.__unwind_info: 0xa0 sha256:30e889680be5042282ebb96eb5fd50a8147b03e899628e3e4d39cf2150da03f3
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__data: 0x40 sha256:2ef4656d02cfb45347e2bb830799aab79d899ae45081de2a4906fe1290b69b93
   __DATA_DIRTY.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /usr/lib/libSystem.B.dylib
-  UUID: 94E77892-424C-3F13-8BE4-2FF333D5DD20
+  UUID: B4B24054-44F9-3CAB-A724-2AFBADD14386
   Functions: 26
   Symbols:   57
   CStrings:  17
Functions:
~ __langid_dispose_internal : sha256 ebf47ec3c3c895efbbcaeffca2a49342ea41bf6c627c6a7465240cc6513afa32 -> 117f63c2389de6a034803d74209d3cd2422b490019088b57ba62839d9d32f30e
~ __langid_create_with_datapath_internal : sha256 cc649cecb32bc6f85eebdd0a128c4b14729e3080d41159fbc0acb3d3151e95fe -> 8cdfd8f59a68c3b7f3a894f2c23ab167706c92b521e21cf7664e0a58450f789e
~ __langid_env_create : 568 -> 584
~ _textcat_Classify : sha256 3788027c75f7779ee9939763cb9a08f85aad35de61912d8bc811d21756af4129 -> 9f8e2905061c892b704724fc457e438c9a4a538c8d1fe7aea8e2b29604afad91
~ _langid_languagecode : sha256 ccc15455eab0b68135a0d4ed9b71bab339779cf9a8ddb5870148683610d9be63 -> 4222698e15d95f4e55cdcb508ec34851996bac899ac865fe89dfe41f8fd41099
~ _langid_identify : 180 -> 176
~ _langid_consume_string : 388 -> 384
~ _langid_highest_score : 88 -> 84
~ _langid_identify_withbuf : 184 -> 180
~ _langid_numlanguages : sha256 41527e1698e4ea8dba86d654034e6bb3aaf99edd797fec452ae798622093905c -> 7a9decee3ff4b7d9a85f2b2f77c0c9526b5baf0f9992c099c4db968b53bbdd85
~ _langid_global_dispose : sha256 a8464dfcb3b7c8d4b8c0f1823ece6d0a879dce8306646958c44ca262109bdaf8 -> e5ede9ee89a95932d7cd9fcc4e6b034a0644e284d2114abc0a999056b4f8f88e
~ __langid_env_dispose : sha256 9833b93a0aceba76c9340d9754d55793020f5e6db3cf43bf40e44356f6d226b6 -> 7bffdae9c4cbc5486b7494dcbaa6305d499086e44182995e9ac906affe27ee30
~ __langid_dispose_internal.cold.1 : sha256 2a6d180cdc74f2e52a912586cc8d865be93ac7193379986669e0081a98743b71 -> 166407f38f642f9eb38248f0f60360fc53bd458cff13084e3c6e9f1cfec6af3d
~ __langid_env_dispose.cold.1 : sha256 1e0ca70dfd8666d1a56ed3f407449ef1a3b889ab7fdc2b4b5946f3b526467c76 -> 4c3e3a9b2ceb96d7817985cdb49bd4fc5e1ee8a7bf262d9b038b451f92fe4d06
~ __langid_env_create.cold.1 : sha256 0c196dcb1dbca72305fb1a2a905fde654f90e26d1e752002e0b8d16d4364357f -> 88b5e96ea2d29c87d0ebc91e2fd992bda7c7b27f2599474761c05b6f053b2b26
~ __langid_env_create.cold.2 : sha256 117e9cf98a53d0c01967503c7e43e1a0d1275f8c9bfbed14e3b2500dc299b6c8 -> 2012cf9f7937801b139d55de1353ad91891f61648480535009eb40ff282fe817
~ __langid_env_create.cold.3 : sha256 bc90bac3fffe82141a3504eac05f0ccecfdbb638bfc51cf4169a5c1b1760f37f -> b89d977098aa057f068e6e41e7b379d1c57e57c8d05c0a1612b0d29ba6e9bde6
~ __langid_env_create.cold.4 : sha256 43dcb5f23f5d3ddb136d1fa6eaa408f5c45ef6dc8e3997ee677b1a040d1790c8 -> 044e1f26153491964e4727a7fe16e768adef11a3536de8aa81e16c9bfefa2437
~ __langid_env_create.cold.5 : sha256 ee4dcc6ca2aa408532e71afe8673f7f21f92e32b95e497709f62a6b36ec1c303 -> 94be5905f5cb80a20c9c1b9b2823ba60a054511ee8b02d9740bd7821698a7557
~ __langid_env_create.cold.6 : sha256 214b6ac1d860ec4492f875b1d263a8566870fdb71a68bd0231759f51214fd08c -> 487b270c094108aaad0d0d4a8fe9f69422a339dd394e5092338548d9192a51c4

```
