## pwauxprop.so

> `/usr/lib/sasl2/pwauxprop.so`

```diff

 1890.0.0.0.0
-  __TEXT.__text: 0x14ac sha256:1fc1de18bf7b0336b9390b2998b3605f3e9ad67ccb3582b1c72707afe2fbc1a9
+  __TEXT.__text: 0x14f0 sha256:84334d84152a807180154e3b00cefbaffb39f86cd839278130652d5b6be92db8
   __TEXT.__auth_stubs: 0x130 sha256:d14013664e314f23c86183de3c5080cb5acd6cc4bac6f35688aa0c871150a9b2
   __TEXT.__objc_stubs: 0x20 sha256:d675dba63e495ff34bc536d4adb2c60466413a0318601db30f2930976796525a
-  __TEXT.__cstring: 0x3f2 sha256:adcd65414551fdfb819d5fc8f1fa287b6b35aa6c7861ea1312b16af559b19b9b
+  __TEXT.__cstring: 0x3f2 sha256:940ee8aff2b6541d6191283b6f364f0ec3c5c4a77d7e3c78b6e88b1011cf2b3b
   __TEXT.__objc_methname: 0x15 sha256:073de3fbd5e3ce3b103d97160018aa1d88005f51ba8b89a5f0612165bc1fa38e
-  __TEXT.__unwind_info: 0xb0 sha256:5a667d72fc8cc0816801cb8ebb162b2ef88e21f0bb5a3d67e73cf49071ae722f
+  __TEXT.__unwind_info: 0xb0 sha256:177f5d916d8f32726e09014109008d04aa6dde55177dac4bb315f291788b6b59
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
   __DATA_CONST.__auth_got: 0xa0 sha256:b58f6fa62296e56b1c350ff0cbc9f94f2116a125e1fb9d798e0d880312a583a5
   __DATA_CONST.__got: 0x18 sha256:298fbc3cdb85385ec842ddf97a19e3d1f1c9bf5d1911d70dc1a7bdcff5e39fa4
   __DATA_CONST.__auth_ptr: 0x10 sha256:558a93ff72b3dd6504846e4ccf16d6eaec1234577a7219654bcf2b87fc003663
-  __DATA.__objc_selrefs: 0x8 sha256:cf50a1b675a0177d8047a4f87b15b9771dd4aaa631843d2f7beae718b4ff7ba4
-  __DATA.__data: 0x30 sha256:05185e87e761c8a5b2bda27495c5d7df528e97bb1afb8c32c8d827e7a6a7345b
+  __DATA.__objc_selrefs: 0x8 sha256:e2e1711657edeb191c8ea1655895aa837a043c8b1f5f426e1aeba906c6d7491b
+  __DATA.__data: 0x30 sha256:341fe0accd2af4ddf0bbd871315b2b38dc94c897bd9bb856f9e99010011c60a2
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/LDAP.framework/Versions/A/LDAP

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 37BD3E33-9074-3445-84E0-2ACAA555F6E4
+  UUID: 5646FBE9-E618-3B1C-96C4-3CB80DF292D7
   Functions: 21
   Symbols:   47
   CStrings:  13
Functions:
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 d1eaac66fad73ee98ca4a3c8fbba3e283f87532bb35981b11fbfb68753afad3d -> dd40526bc574f0eb9ac133838ff4b0e3e19fa9b75f0a32d7df3b206e9e455a41
~ __plug_strdup : sha256 c40d77b6c93a80b96fe9c315402742fbecd4a9b5e440388b497834f048d465d2 -> aa27ec0c8358129afb757d19f7b1936e3936e6c1783d3c02ee2b65653fd173f1
~ __plug_free_string : sha256 7cf21a9cb831714a220a69910fb4b72a44eade62f7efff5303d7a56ef6acab76 -> 8e8f7ec92300874a22871cc431f4983292f51ac9ba261615430d3db37e8c2313
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 673d310ebf2bcf4ff5db3b475b74ee9c36c8f0247d69f50eb42d8080f1deed8b -> 28e0c3fc93696d2b739c54623d503ae887de0e0a0565924358935a38509dc9d1
~ __plug_get_password : 368 -> 360
~ __plug_challenge_prompt : sha256 b2cfaef1162f5d1bd5e91707375d59c947ce6de9dfcbfd6ecede8e4132697d04 -> a31af881f19f9522c787461264c3b21d0c755c223f7bd1e155214694f974968e
~ __plug_get_realm : sha256 c499b641681989f5a000d1405d15dfdae3571d8d1c6cb1d4485081c90e0acd3d -> 70c1beda3afbab5a2c4d774b42eafff6dfb928ec852e900754ccbe45e521822a
~ __plug_make_prompts : sha256 4d207a2c77e1c4a88f3034039f17f4b2a48deda6f4df26c35b792c791be1e846 -> 1ea025e8964cf2420061fd0e8e605fab6d00c4edecf0e06e264c2b1567e99386
~ __plug_decode : sha256 09d7955519e0db52e3e8939a07449883a38f36d544e4f2bc4a6018543ebf73c7 -> 9408ada62740c50beceaf797bfb655df400b9de78827388b3b8ce1087cce3f8f
~ __plug_parseuser : sha256 bfe4a5d75ff4889e59b2b7aa6312a2c205134fd08e22471bb868dafb7ba30b93 -> 10b15f7ff5398bf7d53ef807a77e6681711a9a48df9aa46b4a703108845dbceb
~ _pwserver_auxprop_plug_init : sha256 c7e96a142f8ffd0d1e46aeb13458089bf864162d9db9e1ae553ae8f2e86b894a -> 6f95e2f2c64188e270c04077ef068ed3a985a53793f2b5e8130320a894b783cd
~ _pwserver_auxprop_free : sha256 bc6a93be79207292ece50a107c8814570409f2886b1c882fcbaa1b148dba94b8 -> 6098f9d86da2736a7aae5b734960461f6142492712aef6b419a1cd8919dd78e2
~ _pwserver_auxprop_lookup : 716 -> 724
~ _authfile_init : sha256 08fccb50cd780f3f1549558ec9a468723b0152e95314b31c243b67155b93877b -> e3a31dae4c6ca3efaed9d830b53c62203ff7fa0624a6a36cf01b32993320aa21
~ _authfile_close : sha256 3572c3080697fd21dae87db4b47b3d3762a610f91ccc32761167061a57279f43 -> 6fb080d06b86d2a8d03c21d1e1b1fea48bf4beb8b85f0f84121b2b18b8998d13
~ _authfile_getdata : 476 -> 508
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCKJ77riP5OcSmYCcMcgjxbAnh72pJ0Lks/Library/Caches/com.apple.xbs/TemporaryDirectory.VffEvi/Sources/passwordserver/plugin_common.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCKJ77riP5OcSmYCcMcgjxbAnh72pJ0Lks/Library/Caches/com.apple.xbs/TemporaryDirectory.VffEvi/Sources/passwordserver/pwauxprop.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCKJ77riP5OcSmYCcMcgjxbAnh72pJ0Lks/Library/Caches/com.apple.xbs/TemporaryDirectory.VffEvi/Sources/passwordserver/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCKJ77riP5OcSmYCcMcgjxbAnh72pJ0Lks/Library/Caches/com.apple.xbs/TemporaryDirectory.VffEvi/Sources/passwordserver/pwauxprop.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugCE7klHs0oMuIU1_8DWm-u_IhPKGfwY1tE/Library/Caches/com.apple.xbs/TemporaryDirectory.IceGAI/Sources/passwordserver/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugCE7klHs0oMuIU1_8DWm-u_IhPKGfwY1tE/Library/Caches/com.apple.xbs/TemporaryDirectory.IceGAI/Sources/passwordserver/pwauxprop.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugCE7klHs0oMuIU1_8DWm-u_IhPKGfwY1tE/Library/Caches/com.apple.xbs/TemporaryDirectory.IceGAI/Sources/passwordserver/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugCE7klHs0oMuIU1_8DWm-u_IhPKGfwY1tE/Library/Caches/com.apple.xbs/TemporaryDirectory.IceGAI/Sources/passwordserver/pwauxprop.c near line %d"

```
