## extensionkitservice

> `/System/Library/Frameworks/ExtensionFoundation.framework/XPCServices/extensionkitservice.xpc/extensionkitservice`

```diff

-264.4.9.0.0
-  __TEXT.__text: 0x2b8 sha256:9227efb9d34a25304ce7af27eff3c9f46fdb436d77cfc41adec7a1a75091ae29
-  __TEXT.__auth_stubs: 0x90 sha256:5d05accef62d24067afe932bd0082d7d47c74e44a1630580911f31b2833eae00
-  __TEXT.__objc_stubs: 0x20 sha256:e72bf4548db172f2b0f4f2a09570f11e362b86c70e77fa83e904292e022d25e0
+289.1.0.0.0
+  __TEXT.__text: 0x2b8 sha256:63073dd309a60236da83a5f90f375f7084f75378e6169cde6555088d90387114
+  __TEXT.__auth_stubs: 0x80 sha256:7deec0f45338057312e461862093a659d0dfc55823bd97e0e06f6748b812061c
+  __TEXT.__objc_stubs: 0x20 sha256:4001af4840893d9a8d21915bf57daae4a79c171fe958d4dd4796886a8bbdd1df
   __TEXT.__const: 0x10 sha256:9df24a78b58ce53130e0649f29d05bc81646d33a9408f3f7d0dc060855ba1262
   __TEXT.__gcc_except_tab: 0x10 sha256:2d10b6fba14b7017d152331400e3a9d6ae9a5aeaa701f20c968886ca1464f02f
-  __TEXT.__cstring: 0x2c sha256:0e20c5ab67059a8854aa216eb3204d71039742cbbcbb7c151d7b98ad4698c5c8
+  __TEXT.__cstring: 0x2d sha256:b92f5fd6a7e34237953a9da09eb7a38c86cb870e45cee27402c452ee993e1d89
   __TEXT.__dlopen_cstrs: 0x5d sha256:d66c771b6da8d91e00751fd46ab82a3a5612815cb789ba97dfc83d0ef8045851
-  __TEXT.__objc_classname: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
   __TEXT.__objc_methname: 0x10 sha256:e1b1e7bbfe7ee00a86376fc3803356b9a0c9deb9f797e4d39f82a976f68be732
-  __TEXT.__unwind_info: 0x70 sha256:91b3532bbad81e808cab4e2f23ec4967ae24e201cbe38cf2a32b3ebfdde7bd3c
-  __DATA_CONST.__auth_got: 0x58 sha256:09d8ca1089c3de543b061f9c2ff4562dca04a36989c7a2b4f51ae96a9ce55bb8
-  __DATA_CONST.__got: 0x10 sha256:146f8906c7b5b495929fd54e730c4380b7f2356ac6d49ce7d92dd902dab4ac12
-  __DATA_CONST.__const: 0x60 sha256:78141dc7c4d21face65d39beaf9eab8d0a71bc39cd7a295671b98b2cdc5035ca
+  __TEXT.__unwind_info: 0x70 sha256:ac7c659aadb4db01a97e4d10a6b4bda41c9196b3251bed27fc39b8f750c896b5
+  __DATA_CONST.__const: 0x60 sha256:0ecd18d86ae445a8be6f360d81d9c82899a141c6db21c73ca91a58eedfa10923
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x8 sha256:47575b276b0e531670971ff73452a14ffcd4694064ec1abe57c245eb194bfee1
+  __DATA_CONST.__auth_got: 0x50 sha256:d0afeb17ae3c6f2bbf48f7670673900580b84d4fea07168e4558474a49f85f46
+  __DATA_CONST.__got: 0x10 sha256:a51c3307502b79b2349e2ad7d9940cc8ef065ed94d2cb2c26f9cd72abef0b4e8
+  __DATA.__objc_selrefs: 0x8 sha256:69997f2de3099056bb4c08abd0b75d42991d10c0c833dc258dd45d6cbeefeb3e
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0E76A934-6F23-30DE-B798-24C8B7D83F2B
+  UUID: 1E53403B-270E-3F63-92DC-1A68E77A7229
   Functions: 4
-  Symbols:   16
+  Symbols:   15
   CStrings:  6
 
Symbols:
+ _objc_retainAutorelease
- _objc_autorelease
- _objc_retain_x19
Functions:
~ _main : sha256 2e4a4c0934154b1c0a1190ada651f8af392270ab4bbe4d4ed24ef0b9f79207cb -> 6e6e424a941a4b88f5c355bea569dc667de569839762955919788f6517f3b1c7
~ sub_100000a38 -> sub_1000009e8 : sha256 fe122ea160735864bd9d373df65a32583c15a5d9da35127e00ca7a8b5d5dd2b1 -> 7082ca6f51606b66d4dacec1d1659e1391ed0a4faf2c5f7cea8ea060a1646b04
~ sub_100000b7c -> sub_100000b2c : sha256 71ba3acde06b5b57ad6985931192fac0a7474dc724b89d31b6da07d3708b251a -> 00d4e99b91931851050a8757d07b9943b98d54c08e117bb10510aaf27b2e7458
~ sub_100000bf0 -> sub_100000ba0 : sha256 ca0cbcd695b28e1db4381188719e28a771ff33bff44540a3b4121af057617489 -> 2e222e8c5f589c65698e14200d1cb3352be4d03504fd5b9a15488b4040bcc95d

```
