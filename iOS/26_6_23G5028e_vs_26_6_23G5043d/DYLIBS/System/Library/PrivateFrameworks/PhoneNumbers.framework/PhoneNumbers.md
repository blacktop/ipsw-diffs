## PhoneNumbers

> `/System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers`

```diff

-106.700.11.0.0
-  __TEXT.__text: 0x1f4 sha256:8c6f226d0fe725081447d1b271eba17a97c92ca705c3165595ea38fd93f8e959
-  __TEXT.__auth_stubs: 0x80 sha256:453ed378c3cc3b4909f08c3a571512f7867d43e85dc38333e4dfa3acd37897ec
-  __TEXT.__objc_methlist: 0x6c sha256:f2394e70acbb1b86f540840ebf36cfe7df771050c07ab0d14516bd224ff2f465
+106.700.32.0.0
+  __TEXT.__text: 0x1f4 sha256:2574f854510778444bdf9b59005f71dcb581027aa2a8a2fd3925a46ff0e18566
+  __TEXT.__auth_stubs: 0x80 sha256:9a8002abf28de4830b0fddad71038d0e802a5313bb73df4441029056bf2a398d
+  __TEXT.__objc_methlist: 0x6c sha256:66efd5f5f89fe400fc9aeb6d7ea56b38565a58d7c125d8fd3724985afd31d141
   __TEXT.__const: 0x40 sha256:f7efefc4977b6a4442ab8f88feed244d6ca674cae368e42ef773606a9a7ff8ab
   __TEXT.__cstring: 0x2a sha256:5989c92f9a7ce39d676912b798e2dde2ad2e864eb9e56c79845df10cc56a4c09
   __TEXT.__unwind_info: 0x70 sha256:e3423dbdde592d38ddb06608bb2453008273335157e033d36286f9d8db55b120
   __TEXT.__objc_classname: 0xd sha256:f94663aa28ba754e8d61138789da8090868e171b560f02ca31063421d5be0d61
   __TEXT.__objc_methname: 0x13c sha256:d1f9d6c652ad371a8b0d3fc98bfb7e0412d3fd6704f94fa50659ed85902f9da9
   __TEXT.__objc_methtype: 0x2e sha256:6c2577c7fe08cf79d72c937c0431d81a88498f5ca5aa7fd6c615a21a1770f3ac
-  __TEXT.__objc_stubs: 0xc0 sha256:25bb1ef0a2dcea5bda94910291805cb577c18dd875c67309b1495d7becbb4a31
+  __TEXT.__objc_stubs: 0xc0 sha256:a2fdfecd28e159187a819025aec94f4af75df92f053ab1f038c81e3bdc46f58e
   __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x20 sha256:8083059ce96be6dba58453564aeb321b24e76b911539907394a9ed8a1f8a6630
-  __DATA_CONST.__objc_catlist: 0x18 sha256:1146bcf29b586ceb4144233b172382c2e7220ffc0f9e12f1c5fa4400f2ac9ee1
+  __DATA_CONST.__const: 0x20 sha256:e0ce4c77fa3bd1b895941f08b834f0a619687407d80d164cc0f228e32989ce67
+  __DATA_CONST.__objc_catlist: 0x18 sha256:05425df82e6806e7768e460c85f9d893297808b947bd063584c049923fea4e3c
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x50 sha256:a196bd94d3b7c68e1397d31853878a3af056a79b8ac73d7660fee2d69012cd0d
+  __DATA_CONST.__objc_selrefs: 0x50 sha256:9499fc27f4698ad6c58a0f276b053820ee628f892d41c74ca05a0bdf1fa00deb
   __AUTH_CONST.__auth_got: 0x48 sha256:834a709ba2534ebe3ee1397fd4f7bd288b2acc1d20a08d6c862dcd99b6f04400
-  __AUTH_CONST.__const: 0x20 sha256:3bfd71499ea886e46da2de16e8d19289223f1f169e9d0bccbfcc72d273fec08b
-  __AUTH_CONST.__cfstring: 0x40 sha256:dccc75ce17b307ae03459f7c1a210336ee70051ac351cb01a5526caf1d9b5700
-  __AUTH_CONST.__objc_const: 0x118 sha256:95d620ef4de6cdc2709b9a34e74a89fc14a5935702a1cf1176af1e30a7b1e69c
+  __AUTH_CONST.__const: 0x20 sha256:d17f6f41a2971a01ca31b4539bdb95c3583e05df865edbc4e56f1f58285d37b1
+  __AUTH_CONST.__cfstring: 0x40 sha256:6da31cbddda747d724efb82d0e643511a2058ce2394a39abfc13c3d21590e6e3
+  __AUTH_CONST.__objc_const: 0x118 sha256:7c16ab58b0529fef90e8b1929c793a5928d6717928038850b8a547afc50e79f2
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03850397-DC7D-38D1-9AD7-B20076F06999
+  UUID: 3CA6C9BA-FE8C-3E98-866A-543CF69D2F06
   Functions: 9
   Symbols:   54
   CStrings:  27
Functions:
~ -[NSString(PhoneNumbers) pn_hasInternationalDirectDialingPrefix] : sha256 fd894fbc39dbe53ae273c901daf9347db85702df2cf3eee53a9df008f9b86c29 -> d3495795196ec486208cfa40a7f1ecf95847146178b21f63c25b08257dbe9e42
~ +[NSLocale(PhoneNumbers) ITUCountryCodeForISOCountryCode:] : sha256 0776001e9f36393cf3b891dcda2fe9499e542e3380708182165c68df98967b4d -> cfd69c129c774d3fc6bb257f5f19f50b7e0ab2ed0dcc667a85f1e8f955c9edc5
~ +[NSLocale(PhoneNumbers) nationalDirectDialingPrefixForISOCountryCode:] : sha256 00b80f7aa75df0a5fc682ec89a36e1d22ec3c5c42205db40e8e391426172461b -> f78e1eb8c37433ef5bdd1d202a7ce578d61450fee50a85e924e45b6de8e5f267
~ -[NSLocale(PhoneNumbers) ITUCountryCode] : sha256 b17e2c5e0d7186b34cacefb5a398f5f4e7cc9334f48d4cc7b744bd348395ad8e -> 58b4e65d689720e037e8f372f85ebc2f2bef27362a0f45bd14b068315e5ecad5
~ -[NSLocale(PhoneNumbers) nationalDirectDialingPrefix] : sha256 7b569a1d100bd2a3ec71b8b4698e69666a50bff245344aa1be677dca5825fd06 -> b246de1fa7b59795dd263ddc69a782229f8d2ef2629a4f5d9c4cfe403ea96c4a
~ _pn_default_log : sha256 952374d34a7709f78efb6527881b733bebce4b56c567c963effc079f5a1ea591 -> 87e90872f051b7d8651e022ab89eadfd217d426b424282b89516bed281501669
~ ___pn_default_log_block_invoke : sha256 cc9aaaa1cbdf1bf4c422123ba7715039f4bc5b9200cbff02dfb78339809450c5 -> 73edf83d024d21334cc9881805faaa42c3e2a96be8fc63f52fb2d62a0780abaf
~ +[NSCharacterSet(PhoneNumbers) pn_verticalServiceCharacterSet] : sha256 35f466c796aac8d328524781ec66c49e5cecc1f1afac7718926f318cdb96c868 -> 822eeb3c5f7aa3015b0f36b1840aa2438c2a93a38925442e8303b37a0efb006c
~ _pn_default_log.cold.1 : sha256 d7ef720e72e77960e7e365b5420c4f4bb46f67412525d38e561ce64583fb6059 -> ea640737afadfa13f5543a1e29a7ced136932c697af33f7569beb989a29701aa

```
