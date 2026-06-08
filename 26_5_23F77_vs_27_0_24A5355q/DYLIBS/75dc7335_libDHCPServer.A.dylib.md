## libDHCPServer.A.dylib

> `/usr/lib/libDHCPServer.A.dylib`

```diff

-534.120.2.0.0
-  __TEXT.__text: 0xc84 sha256:3fc41b157654e2120240dfc51bde643c9246ea48ec4c26a1ca89bbf435154832
-  __TEXT.__auth_stubs: 0x210 sha256:e0fb2abc900ef0c196e6824db0a0a65fb01c9802f4d78433cd2d0b16c1ff6c7a
+551.0.0.0.0
+  __TEXT.__text: 0xc8c sha256:40eadc5f327befac82c04d2610e341be40f0c29a23f56f221bb563e8325b7561
   __TEXT.__cstring: 0x162 sha256:739a88ab7781e81199f4d7340750d754ca744052141b4ee8fe9e49a36667f4e9
-  __TEXT.__unwind_info: 0x98 sha256:58735cc4d752457f56c03d02b37ed73891b2d137f4966cd7b3bd870e6cbff062
-  __DATA_CONST.__got: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
-  __DATA_CONST.__const: 0x28 sha256:6862be660f55faa82470bbb8c17d4f204762adfa0b512fd1f1223ef3f94b8825
-  __AUTH_CONST.__auth_got: 0x108 sha256:44b8aa4d28701168922acf61435ea4bb442f97b0b14ad7a2510ed68874ee2a72
-  __AUTH_CONST.__cfstring: 0xe0 sha256:a9b9f7716de8598bf6b9e2bd4c49051f772d84ce46b9968af420611404baa545
-  __DATA.__data: 0x10 sha256:fbba62d20a64814a35b2079ba3ece976fd88d9eeb8f4b5097484b6cb2ce69878
+  __TEXT.__unwind_info: 0x98 sha256:11c86f59dc424308047d903e49eef3dec827703a38cb323500fefb9a17512001
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x28 sha256:01d716cf939f7e98a9fe6c980681817f7cf46d7925a1b17c76ec19475cb95087
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0xe0 sha256:73f8d6aa9ff271d987fcdb54efb06e2fd4ffff2758beded9a377ed965e49cb64
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x10 sha256:46444c95bcb664c03f1d18482d5198f2112de7dd3de88cc85aecf3241543ace9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  UUID: E740B16C-B7F0-35C9-BF69-AD38FA1693E8
+  UUID: C39BDA6D-520D-3406-B446-DAFF70DCD76D
   Functions: 15
   Symbols:   48
   CStrings:  24
Functions:
~ _DHCPSDHCPLeaseListCreate : 712 -> 716
~ _DHCPSCopyDisabledInterfaces : sha256 7e1d5dc027a9e9c4cc9efd9d60edb4d508dba0f2e09cec95c07dd83d5b4c6c2e -> bc0acdffac43efe5bc1436544dbd35176e2149bda9bede73d5474c800d9b087c
~ sub_2a1e129e4 -> sub_2bbb189e8 : sha256 590295b84d8b7e8aef8142a3642b7db3072c83eb738e8e5a39d249fbc98ab5b0 -> dd3a8939730afe0b408ee2abb60a8aa02fc41f8d9b5ca533bfe541414c52734b
~ sub_2a1e12a40 -> sub_2bbb18a44 : sha256 6a1ba73b21543d93f308e36fb22230c66f24a11063ce0eca7030eb54be94de07 -> 8e6b60eff6885d7265f75cae9b1982b5aed79c3d414ae2ce85ab454746503ea9
~ sub_2a1e12ab8 -> sub_2bbb18abc : sha256 2a846e5d32006d554d857fd764058e2717381a9ce6b48468f1454927afc9f73b -> 7825d211eb41660169478cdc842f7388606957a61818b1d6269c8a0d334485cd
~ sub_2a1e12b48 -> sub_2bbb18b4c : sha256 981f78b3ee212bff3a65cece0698e384810bfb5bf52fdeafc1448a744c9f9b65 -> b15d35a5dbba88bc97d5d35f515ee142577b29bdc6e9871665ac240b4850a491
~ sub_2a1e12ba8 -> sub_2bbb18bac : sha256 70673eae35b09bd1b1d34af7674cbf3e26cad297c1cb84b3e1a7170d19ad6999 -> 4616859a550ca0501fad22aacf89d4197613c8b9abd1c1eab28ab4672600c448
~ sub_2a1e12f5c -> sub_2bbb18f60 : sha256 065ec3f40b42e7e0f4087aa933fcd2d4ddb6c396684e73fe816a0b1c570dedbb -> 78184f5ee733fce7e04b1f1b967db9608d4b4b9f2e1e7af53d7a3732d1de9a90
~ sub_2a1e13054 -> sub_2bbb19058 : sha256 73aa5a5a0f94ff158070dc655ef28e4de72913887d39f9c90b10d6783b247f12 -> 9dd17e3811f3bd47a474c5b32cf4d4e3881fece18b4192b7279450486a0c1093
~ sub_2a1e13098 -> sub_2bbb1909c : sha256 bd423c01921076454e24013caf80820a94cdfed319ff480b4e706afc0dad68fb -> f8dc243eebd606c4f98f36d668d85daaaef192c82f87570ed90697ff24b5d031
~ sub_2a1e13104 -> sub_2bbb19108 : sha256 91943aa06829760974b06278f98711f22a18fcc6b40e88380ad9d8d6949d65e3 -> 37ec9d6feabd516c3afd14279497bcc887c9062c20400d16c8f2b843394426d6
~ sub_2a1e1319c -> sub_2bbb191a0 : sha256 7ad08c285f2f06ea9ddd25f8c6e8ff47c52e9d7301d5b89b1caf63189a699fcd -> 37fce13dcdfa85bfc70b1d08d36b651dedfbd84614c185bb5b9e96dc2fcd097e
~ sub_2a1e13214 -> sub_2bbb19218 : 108 -> 112
~ sub_2a1e13280 -> sub_2bbb19288 : sha256 544b9203a95d355bfefa8290cb16380585204ca1925f7da6e097a884a1bee579 -> cb2c94522e820a331c3da786b9a1465e139fde4143791f389d1c6938462059ec

```
