## pkreporter

> `/usr/libexec/pkreporter`

```diff

-498.0.0.0.0
-  __TEXT.__text: 0x960 sha256:2ca7b44697118cb0d1b17d36ace8d4ffe4047b5c5d4d4ae178d5b17d6ffad98d
-  __TEXT.__auth_stubs: 0x1f0 sha256:faa06d3035ba168409889ba8b78106b2920d73b9588d6cbc79ff0990c61d94d6
-  __TEXT.__objc_stubs: 0x220 sha256:ced87d26de9d429d4211d99b6f2af876cbe0b24a1321fe0779d5392feb5cb6da
+510.0.0.0.0
+  __TEXT.__text: 0x938 sha256:4a2739a0872786cfd551d4ce02620f3a1e7d72e4d8f587ff762485ad2eb5c971
+  __TEXT.__auth_stubs: 0x1d0 sha256:a526d30299068d79b3697f4a3c708ffa82e5d68b60b582df3cee57033da21e91
+  __TEXT.__objc_stubs: 0x220 sha256:3d6741d2985f5c690a445259d7bb7033f4418ff8c09fd5aaaa8bb5eab9136ee6
   __TEXT.__cstring: 0x287 sha256:e9cc43c3977ae4ccbfe095c05f1429e820343313a056d749a608789f784b1e29
   __TEXT.__oslogstring: 0xf5 sha256:bb1e8b018ed754d0030ab3bdbb5641c54d99a43151b803529c2b7f9c733880bd
   __TEXT.__objc_methname: 0x126 sha256:d1286ff53298dc8eed092fb0127fe56aa0d030ad50f93d78b46e84255e5dc4b8
-  __TEXT.__unwind_info: 0x70 sha256:eb0e34bd658c65499bb0bbc1132b130db869b07443ea470bee1f20a6773622dc
-  __DATA_CONST.__auth_got: 0x100 sha256:bcb56104e98c44685043211cbaeb106a0a56a3745b5269224002a7a8487c3c4e
-  __DATA_CONST.__got: 0x48 sha256:b9ee8e28d23a2959f0df9cbff522c3ffee692114187a60d16b186d04e15fc4fc
-  __DATA_CONST.__const: 0xc0 sha256:640f12692621c83fb380a50db71fcc02337e0ebf36f40bae5d00356990c9cc18
-  __DATA_CONST.__cfstring: 0x2a0 sha256:4b1389cd534be7484eca4a4dd0fb1efa186c60fc031ad51156121884ce52b6a7
+  __TEXT.__unwind_info: 0x70 sha256:dada4e1daa9afcf5399029c40e870abdb6c8eb1e2703957995f87cd1a25e9b3f
+  __DATA_CONST.__const: 0xc0 sha256:0dcbffb1b4e5d0c0adf9f84ba5e0297d6d8baf7197f11db9efbc978bc4508003
+  __DATA_CONST.__cfstring: 0x2a0 sha256:63c905546488751c98ee684cb8963fc15eb36e251305425db42e2132319cd74b
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__objc_arraydata: 0x80 sha256:d3f481e654ad102e07417d322884a737ae35eb05257c62bad9c11b272e239d38
-  __DATA_CONST.__objc_dictobj: 0x28 sha256:24c6cdbf6b2a066a1e2832536cc431e2710b3c6d667798f330bff0636e6d7c55
-  __DATA.__objc_selrefs: 0x88 sha256:fa775a0f4d7c9ae0b2640ff02bc850290a87bdda5f65636b1b436537d0828929
+  __DATA_CONST.__objc_arraydata: 0x80 sha256:fecbe82a7ff06c87e20c6aa18328936d51a7e111dfc42b34de09dae343f84aae
+  __DATA_CONST.__objc_dictobj: 0x28 sha256:00e4db732890155ecbed3315e83b9dfca373ca3dfb8d2cdb8fcd11158686425b
+  __DATA_CONST.__auth_got: 0xf0 sha256:6d4971411db874ce0aec6ce953b362bc0bb7544476414035d27de0137cac9a6e
+  __DATA_CONST.__got: 0x48 sha256:718ef0874fec9dc838cf682852ea3f541dfe792d05f0441224725d3103cf944d
+  __DATA.__objc_selrefs: 0x88 sha256:2f6c6963c2a6a5566ca6d65a49f70035929fa1acd9fa9852b59d0c718db77237
   __DATA.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1FA37A6-0833-3A09-BF06-4F379826CB48
+  UUID: DF0D9C53-116E-328F-9294-A0282C045FFE
   Functions: 4
-  Symbols:   46
+  Symbols:   44
   CStrings:  71
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x8
- _objc_release_x23
- _objc_release_x26
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x28
Functions:
~ sub_100000a18 : 280 -> 272
~ sub_100000b30 -> sub_100000b28 : 2044 -> 2012
~ sub_10000132c -> sub_100001304 : sha256 85e0da22cebea17ca48745924174f29bb6ef0fbd8037f9c4f9be97aa423cc93e -> 3fed0c3cdfa1239f4df598d23053aebd46f9bb4a2061353458bcafa2d91c1b1f
~ sub_100001344 -> sub_10000131c : sha256 78bd2f8c21cc88e2eb7aafe9abe8979ab12b97b55a95b4c442609e601f33828b -> 9cbc27fd22b3c4d036a527a35426a5304b58fcdbf73ec3cf6c3d45a9f34d726f

```
