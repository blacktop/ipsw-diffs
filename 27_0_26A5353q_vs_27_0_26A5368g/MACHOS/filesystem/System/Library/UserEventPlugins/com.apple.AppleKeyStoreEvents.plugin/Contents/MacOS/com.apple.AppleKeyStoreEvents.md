## com.apple.AppleKeyStoreEvents

> `/System/Library/UserEventPlugins/com.apple.AppleKeyStoreEvents.plugin/Contents/MacOS/com.apple.AppleKeyStoreEvents`

```diff

-2369.0.0.0.7
-  __TEXT.__text: 0x1688 sha256:e692a201e7c20f2adb5aee5478e3d5ce2f260d0c37e58607851f7db1ce6fe1e6
-  __TEXT.__auth_stubs: 0x250 sha256:d8cf725997850a715d7df648134ed138c627780ec825940bf450f668692045a5
-  __TEXT.__const: 0xd8 sha256:90bc5ac964755c2815ff10cbcbf61653cf68264208c955e4ad551f86478880f0
-  __TEXT.__cstring: 0x3ca sha256:a2ac56ba5c9719959230dd8379e8cecea880de2919bfc634a95f60d7eec26f24
+2383.0.6.0.1
+  __TEXT.__text: 0x1698 sha256:de1c0fd97c1b1c3c26363bfb6065bb41840e9200f26465a207e7b646e3362d69
+  __TEXT.__auth_stubs: 0x250 sha256:71d3493c337662775b4aaf16360bbb08756a6e9ee478b590b82ff1073bf12adf
+  __TEXT.__const: 0xd8 sha256:9957c55bf019d4c6de1d1ef55c79fc7972d2fd2f67ca58a74fd6e530af134fae
+  __TEXT.__cstring: 0x3ca sha256:a8d5c259f761e47ea059b24c6654c691577ec7a6ea9bc6cd8bf02cbe447c8cea
   __TEXT.__oslogstring: 0x17c sha256:0c144cb52db40f56548d5ace454a01d10f476b7faa8a25386553f9c35da4265b
-  __TEXT.__unwind_info: 0xe8 sha256:e666cd4f60f03fde3d54c6d9328aa898385ef9124a242d929360bcf839cc588b
-  __DATA.__const: 0xa8 sha256:1244775a3bab454d4b9d79be32cd3e3247bb42dd8ebef9dc1dcce0c2d998ec40
+  __TEXT.__unwind_info: 0xe8 sha256:10cf25bdee089b9ac93d8bf6a24d9bdcb68a0618ccf5b6cb30eb6d93a671f481
+  __DATA.__const: 0xa8 sha256:39ef427d09e6f37451fc6962839def3aab5b874afdeae46c38fd7825a2dcf1d4
   __DATA.__data: 0x4 sha256:ad95131bc0b799c0b1af477fb14fcf26a6a9f76079e48bf090acb7e8367bfd0e
   __DATA.__auth_got: 0x128 sha256:92b159f863c99d81135dedd2f73bbcc47ce3b354b3c12bf745f21160f657d794
   __DATA.__got: 0x28 sha256:d4e59ab65e31e49ede043585045ba9e443a29dfaf2bc6e5470adeb552a3ae2b8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
-  UUID: 318F0713-CD84-341F-B648-11CDEC4F2846
+  UUID: 465AA10F-3112-373E-8802-C50A014BFEAF
   Functions: 55
   Symbols:   92
   CStrings:  46
Functions:
~ _set_akslog_context : sha256 0f06cb94ceca628c6720a54bd008a363f38a92fcb211fa7e544275053200ce08 -> fc12de432f6e062a1a565caa70abc63ec96691e694ab7c3521d7e1bc440ed675
~ _uuid_to_string : sha256 838a76519160d42789271b58d983d61ac2a800fccb796f5cdb763706b6ae1e15 -> 3b743a4202d403119254f53db89e1f9646c443745dbd18a094f39d180fe566e4
~ _compress_uuid : sha256 65cdaab9d3a6727667a1b83d65f5476a93a939561f0b0242e74ae4194da66d00 -> b470b6fb7695c32a4e5969f0806ba3a7be5ce6400a9b549b8aa7db53b904ba6a
~ _time_seconds_to_abs_interval : sha256 b93cbea0c5288727e0213dd9572e3d88b1b926cb3f64ffa517f7b16dd40b4550 -> 32bddfb6f206376426a6a57643d44c1a2496332b52fc8bbb64d7ab53c61fc987
~ _time_absolute_to_nanoseconds : sha256 b93957663b07f1b8ef5a47dcdcc050a101a676e587d53a34e46807ed3700c07b -> 9eec52cefd2f63132693f23a98c6c7c20d8ce4e0df97cf2608d46a42dda202b9
~ _get_usec_time : sha256 f74ac70236b679107f4ce5fbe9f6e58bb245d6472ea6f272a2d45360f5081738 -> 8b7745489769332ba6200dbe5e8056aac974214322dfb8eca1afbaec22ef8a6b
~ _get_clock_time : sha256 70852616c012a22db4206db8f1604a2b29f0b7ada9eabd1752538b95b96817cb -> 1a474aa65342a77189de523a85c61f1d3d0feb92e8c836171f86ab43164fdcfd
~ _circular_queue_init : sha256 dbf3604440c82be3bdfcefc48eaed9b8d7910ddf636b2459e744245d7ae9e136 -> 3b3106c61f366263cc3dd280b6e3e784f7182e51ba0e9eb1527dc13f4558b248
~ _circular_queue_enqueue : sha256 c98c55581f22f9b8c6a6162ceb201129d6433b24781c142ef5d6e91655b9f3cd -> 5c44cc0b4d2dbdb3fdfbdfbb04e1048863c936a094c4b0b930a1361a430e62b7
~ _circular_queue_dequeue : sha256 97b207258b7abe7f797b517d9c2a4c3072b04428f772633e5b332515a06acb55 -> 8ac82f36990422cc0400828f10666faa10056abde56c03c757bf75e98c448537
~ _circular_queue_peek : sha256 5ea5d2b16cb14863e195dcad1d430c13df6fbca7cb231771fcca04a254258c87 -> 7f78503fa2f8209ec292b8140b786ef42f7ab8448bdf9ef1d78159ab856214e2
~ _circular_queue_dequeue_all : sha256 65ed5b098526f1fd2d09f943d96077c31b28712e5417eb51542239fd97c7cd14 -> f0e97bf0d974e58440dbfde44afde4bea6fbbd3acbf91cbdcea56ad0826c614f
~ _circular_queue_clear : sha256 74c37fa43d6174e783aa61d99afb83a0f766b0af130bb3f16c3416e875ac79db -> c37e9ef8d9e39acdc0c699ed591cf6a4abb431f2e2fbc942656687103f4f1d82
~ _circular_queue_free : sha256 f1be09f1aa8751e32538fa887bd0a5b013a035a7c0a38d67090db8682708d622 -> d4956d16e741c06a0fa60d9eeb30176e95caf79daa3f9a491a330db3784f0b46
~ _is_non_zero : 44 -> 52
~ _memcmp_c : sha256 3e9b334405fef2c89b20b910675daacfcefd58b180d455bbf68fdfeffbac2274 -> 78846f059a8aaed327a5875edfaa9fac38bf618b16981bc5523b8be0e9285335
~ _dump_bytes_internal : 488 -> 496
~ _bytes_to_str_hint : 148 -> 144
~ _byte_swap_val : 48 -> 56
~ _err_sks_to_aks : sha256 20f6521d2d35687fc31d50bafb4f3968b77eef80493d303d4623737e8e7fcb3a -> eed5ef54b6da2aab3b67776166111253a3a37d6e4685adca128942c21e610281
~ _REQUIRE_func : sha256 59ca985aecac59b10f1fde17370f32406053306747137ffea4f7a645264e6e85 -> ce9f54a4acd9772945020a5a96aec06ee750746ef2bba77cc5a1140235d2face
~ _dump_deltas : 256 -> 252
~ _lock_state_change_delta_id_to_string : sha256 0fb96600639c2e25f14f9ec28b56b5ddcc86ede39112d29e0873ccbcbefc0903 -> 1d11655cab1e1135537e982b9fe05908484af4aa48d10a26641ae243aa52c26f
~ _ticket_update : 216 -> 220
~ _analytics_send_perf_data : sha256 f4f33a9d5afe82c584b8e7c6bea9ba39a381ca604778f3a3263843d0de9cf015 -> 4ab62d6053822c96aca3827a40e6a53e3a3ab924f5fdcd39a337ae788b19fabe
~ sub_1488 -> sub_149c : 176 -> 172
~ _init_keystore_events : sha256 fc5bd22e875223688b4f3e5009c479bd4d68c50a462365d7b8edef942a3cd0a7 -> e1942b9493e7c952f6a43200f2c0320c3ee9f9cefcd5a23d839c3ee060222bdf
~ sub_1668 -> sub_1678 : 936 -> 932
~ _get_kcv : sha256 c8ada7fe2a9ecf0b4ed08234c89021f5aea14f839cd786fa5e1ed7a5e5df163a -> 9c5a69fc0016d9ca5d911e23af8432bb2dfb497e31ac47cdae3aaa62fddbb2f6
~ _print_kcv : sha256 7c5fbf13bf7231fa11bfe6cf4a5e2b5d70cd24b384d3de2e8488b8ab6ecb4ebe -> 0fed0eb6623ebb8caadaaa559e97750acfa90524f8c945f3dfb6b01c75f019f4
~ _ascii_hex_to_bytes : 268 -> 272
~ sub_1c40 -> sub_1c50 : sha256 23427885eeb4dfb24e94d1a50a9fe65eaef46912da6e75c31dd4c1e9541b43bb -> 5fea2fad4a349b305ba790fb64a18f5c3ad4dc5086b38950743613352b4fbb1d
~ sub_1cb4 -> sub_1cc4 : sha256 3d851e9d373542f1d05f31f55de199265eaa637afea913c4ad2d117afbbd7263 -> 431418dfe223150155bf55e22afed5868f281b36afb1ec18d6393e4670993ab0
~ sub_1d18 -> sub_1d28 : sha256 a18a306be648cca0300765daf9dac9b7393da7de9624874afe4da4830857c97b -> 3372f03969e964042ff85e6117b0dcbb220cad7a68c4a5a4231240e0c4f80b20
~ sub_1d60 -> sub_1d70 : sha256 ddd6915b3a6e4e8d957a1f87844e359abd9b09e12c689498db0c71c7126097c4 -> f8502c41406d488346023ab001a364dbf0639eea54958d2b7bb9c960dcf0ba6e
~ sub_1db4 -> sub_1dc4 : sha256 06eeeafb55bf6474d36ae4267ff1ea7a50bec365381a09577e73d9b4643612ba -> e35314baac1e45d563280d3e302ad2252d1fc3fe559a8e927f3edd768c07f3f8
~ sub_1dd8 -> sub_1de8 : sha256 c3c850f549b30a3b09a08927ffbb163969c9c23ee2f448418b7ad3977b226468 -> 13a3cecc4d9b5df4786f4053b971698c536203c9f999431301241442d4c2e487
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CR6nugBk3Mpq8rGbsNb9GzqfmzAai3b9n4ZGQes/Library/Caches/com.apple.xbs/TemporaryDirectory.AQaxIo/Sources/AppleKeyStore/timestamp_ticket.c"
- "/AppleInternal/Library/BuildRoots/4~CQdbugDFm33iSyxEe8Lmvnfx2xCpBnzrq-yxmWE/Library/Caches/com.apple.xbs/TemporaryDirectory.vfoSuA/Sources/AppleKeyStore/timestamp_ticket.c"

```
