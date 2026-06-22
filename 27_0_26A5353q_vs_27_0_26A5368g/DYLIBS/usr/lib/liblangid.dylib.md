## liblangid.dylib

> `/usr/lib/liblangid.dylib`

```diff

 140.0.0.0.0
-  __TEXT.__text: 0xb50 sha256:8e209e2d0690d4438501eb21cc5bdb1c710c3856b4fc4c34b8595953fb890cf1
+  __TEXT.__text: 0xb50 sha256:47e9b2cac74812d5624d0fbd93e1bb896f9fcf199809135b2b9c5990db86dff3
   __TEXT.__cstring: 0x195 sha256:9a0940673deb234aecda41dee15b91094c98716c30a7baaf7cd640ba7f3e1341
-  __TEXT.__unwind_info: 0x98 sha256:3c4b4531a12e54e6ab56d39d42fcddf0876e859ebd1dded4173f17fdbec830cb
+  __TEXT.__unwind_info: 0x90 sha256:4b778f7773ee8431c17325f3ab5f16ac6db5c576abdafdfd5bc152d5007bb923
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__data: 0x40 sha256:2ef4656d02cfb45347e2bb830799aab79d899ae45081de2a4906fe1290b69b93
   __DATA_DIRTY.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /usr/lib/libSystem.B.dylib
-  UUID: 67B3A18A-F4D3-325B-B644-C5C341ECE560
+  UUID: 52068756-619F-38B8-8E78-6311AB9B52F4
   Functions: 26
   Symbols:   48
   CStrings:  18
Functions:
~ __langid_create_with_datapath_internal : sha256 e2d1a31151adcec2abe04f8ae308ddd82aad406a709a9bfec218b1ffd2ad3a4b -> 23aab11a30459df966b12f442f458fc4054452210adef87a5a380878c7f6c770
~ __langid_env_create : 552 -> 568
~ _langid_identify_withbuf : 184 -> 180
~ _langid_consume_string : 388 -> 384
~ __langid_dispose_internal : sha256 200486856d35a819ae2de9087309d6496c5eb852ea9ffb54cecac91c7a16d0f7 -> c0e761049aefccfcf749dc4f629c110db314e3004762f2692955977e87b9927e
~ _langid_languagecode : sha256 14b03cea8882a92a3901d48c3b7044f4a42195aeb3c2cf9f7cc175483b67b4f4 -> 307073fb98113c9946b044f1a382ed45d016a2b5cefd45092cd641ffd10187df
~ _langid_numlanguages : sha256 a119ba339780a4da91177a36a39794e3064efb2425486c42cf9a0e3fe59cb83d -> 558d14021fb885eb5c8bb2df81c02374a069410b4181496c9edea3d09c812758
~ _textcat_Classify : sha256 71cf70f83dd095af6ab2438a8d5d099d4630a9604dc8e4de14eb70ae113eccd6 -> c867d3c04b219e65ffcc9b67d7067538dc5f6393cb38e5fd3a83d578567a3efa
~ _langid_identify : 180 -> 176
~ _langid_highest_score : 88 -> 84
~ _langid_global_dispose : sha256 437bafec40504f7e16e38b7aef71f1a87db1525d16f51753b22a4b6677f3e67d -> 534c1aa72d2d4ec6ccd8f51c20695263f963da4ac909d9cda56c1a43b58236a2
~ __langid_env_dispose : sha256 8f1c66067bb9b591408971533e01e3eba2ba3fd722137a7283b77711682088c2 -> d67100e51b30a5fdc82ef75c89665f4c6bb70ee3558cce48971535438c0077a5
~ _langid_dispose_internal.cold.1 : sha256 12875f386f24b8fbbbafe3c8a1575379d9b0e335d543c2818f000cbc3c8bab54 -> 978546aa7bc4c5f9200515b6e2e09fe4786d7f10f38edb5c28bd01fac64848b2
~ _langid_env_dispose.cold.1 : sha256 35c5e6d22a274cb012227316bd9f92899465d3ea9e0c6a7380e6097fe9e53bc0 -> 8a6c4bbc16ff0b2e35dd8af410546f0fde7d407472d3a6fa46e2ccc7c2bb8c38
~ _langid_env_create.cold.1 : sha256 0ea1567664b2d8fc58e5337118f7c939915f604e97fb7cecc547f90448fb7fb9 -> 51974ce1b41f1859dcc43e300d380f83cf33da35b84051fa41b727efdfa9a6c5
~ _langid_env_create.cold.2 : sha256 985d974f8313d9243c06bd6b7e7b349bea1456bab64b5b30b6f585595e6577c8 -> e37bba361419aed66bd82b7e40e8fb8eb0a2ec65522023c960c128b49614a46a
~ _langid_env_create.cold.3 : sha256 25767866ae336c534d95ca5e1c68dadf712166f05a63f44b47bb7d7af8ddb6b9 -> 34ff4b58e1de74d856b7fd51aac0838886ff80317fa586d9efff829a76f2297b
~ _langid_env_create.cold.4 : sha256 055d5a03110a58b13b01e7586fd170150490cd7ec49e901ae0b127582e345575 -> 065fa34cdcfcd2176526ce22daeb92a3ddbf0adc9e5b71a200c31b5200c119f0
~ _langid_env_create.cold.5 : sha256 8a026f255219e1052f90a7205a6cb34dea8d0af15da3329c1931001b229d3f29 -> 57cb83860afaaa434c1da6be7a914da243c6a914a2ba9582a03b74bc95a18a89
~ _langid_env_create.cold.6 : sha256 13a17408fa60a4ee5b7d9e0fb3edff36d39c98624a56d9ab6168b7f788d728b6 -> e67f265ee28bce412ca1941089f164c76aa82076bb7b0203ce8f29b4b750e985

```
