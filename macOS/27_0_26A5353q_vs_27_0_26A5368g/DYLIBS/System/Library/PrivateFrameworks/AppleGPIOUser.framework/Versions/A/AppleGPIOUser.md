## AppleGPIOUser

> `/System/Library/PrivateFrameworks/AppleGPIOUser.framework/Versions/A/AppleGPIOUser`

```diff

 65.0.0.0.0
-  __TEXT.__text: 0x7b4 sha256:5afc1802b3641115ee8846d055b1b2bd1a178d8f8988aac771fc00dc0977bea6
-  __TEXT.__objc_methlist: 0x38 sha256:8e2896c56a0014f8b4f08826d60e85a3352b62646d19837895b3deca4b7c2c76
+  __TEXT.__text: 0x7b4 sha256:54e6b8cab5a046d6fafd888d34e0e0589ad319276e6a45fb60d0579d78d28b18
+  __TEXT.__objc_methlist: 0x38 sha256:3c3042819e82d9f585a74e7a985ffb8dc8a94323aeca29a619afa5faa27a6a1f
   __TEXT.__const: 0x50 sha256:14942f87dbafda3e16f1e96cae69bf2841df3dcb975fc0fe33a4d591a3a672be
   __TEXT.__oslogstring: 0xf5 sha256:1a5a287e3254d7e6262274bf9873fb6a3f70b27b773227ed8ba3e6a8ded4978c
   __TEXT.__cstring: 0x36 sha256:4bd53b15f82b49d36e073acb896844b38cf2ef5fc3053f620b1551d09cfd337d

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__objc_classlist: 0x8 sha256:286bb0d80e32e91d03812ceaa97df28c3c29ed887e263a080cc1c0a9a8d56dd3
+  __DATA_CONST.__objc_classlist: 0x8 sha256:c079588beaa637f777d794aecf9ca7723fafdeb1f992a02413b3807516068b93
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x38 sha256:9d8bfa23150e242f734249b436ed165a8eb9a1651a4319e189afbc706a2fbf31
-  __DATA_CONST.__objc_superrefs: 0x8 sha256:67dda054fcd16a1e1dd057c0f940cd2c15047d63db92087fdc84f44df55d96a9
-  __DATA_CONST.__got: 0x18 sha256:2e4d19fbc36ace24d52740838075a7b271f72c1edfd5d049653eb38942c71ad7
-  __AUTH_CONST.__objc_const: 0xb8 sha256:fa5fd5df9d0faff6b682aca525b816f8600016b270a4cafeb3a0a95b4c99cf61
+  __DATA_CONST.__objc_selrefs: 0x38 sha256:2411a46a9837e678fb91759d20285471adebf0de5bedce10a84a548a3d50f67a
+  __DATA_CONST.__objc_superrefs: 0x8 sha256:8166b7ced6f6be40bf4ecefa837f37488fa3ffe4549ef9ca94ac98ed40d6581b
+  __DATA_CONST.__got: 0x18 sha256:41fc7956012a04fa1e92189e34d62a13ce512c14d48a8b7864eefbbc3751951f
+  __AUTH_CONST.__objc_const: 0xb8 sha256:da870fcfd0504032da3b9a5cda01b6b4cae8f1e782bd78a31e2cf5827c1980a7
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50 sha256:8492bda5d516c3036f7c1f65c4d8dae5c73bbd23e53dd2c2ffb3fc37ce6a88db
+  __AUTH.__objc_data: 0x50 sha256:fcbf968b7e875afaa6ea3d572e906f51b20ee3e066126558afbe7eb420372d6f
   __DATA.__objc_ivar: 0x4 sha256:dc765660b06ee03dd16fd7ca5b957e8c805161ac2c4af28c5a100ab2ab432ca1
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F8FAA5E-AD90-3CDA-B613-F36F35E4FD66
+  UUID: 67671580-5422-34DD-ADA8-5AEF1998EC2F
   Functions: 18
   Symbols:   60
   CStrings:  12
Functions:
~ -[GPIOUser initWithName:result:] : sha256 3b0a18d45135959e5f9e0c59a91042b51a9c687efd1a0546bc1eb1a147c34f63 -> 03092cc2ca19c9c3caf701877daa12ef68669c8f2679f2f6facc93b5adfb1389
~ -[GPIOUser dealloc] : sha256 1680e151a02a62725a9b6c54e9b96350cc0509706b61a2bf0a52c5af942658bd -> c05e0d5bcbc9ae76fd200095879c0a388f2fc3e4c9ac42ffb387d465991849bb
~ -[GPIOUser getGPIO:] : sha256 f15704ab2dbe49dd81997b1792379945995449c0090928de43f8e8f98badbfb2 -> bc939afc6e54c17f62a5b832d26d85fd6defa1ade24b4aa02f748d3db0ab5c0d
~ -[GPIOUser setGPIO:] : sha256 d89c154cd6baa813e7656e53a29f00b29718fb9cab9498d1559c0ddbcd7e094c -> f8b2d96c0abb8ed0e574514b29865c1543eff2f759abe695d26d94ee0afca29d
~ _GPIOUserCreate : sha256 825cc6ecb7082b672ef497d70e22f3c0772be5b138d9afe3f5eb86bb5fafe27e -> 02f1e27d51d78a46a7eb6ff83866df9694209ff47d2920bd5ae10ea75718b924
~ _GPIOUserGetGPIOData : sha256 7ec1b60f28ad5631f77733f1455115f4631ea0833bb720999d3995a605199e79 -> 0ca4c9434f7b9875ecbc5cf7af6d7ab91f5bd311a7474c395a1c22d376e2f376
~ _GPIOUserSetGPIOData : sha256 ce611b50278bfd3e402d3c2ca243fe3f8da197b3ebea58862d472c30ce4f8062 -> 2acd4362b213796bc4823719c4103f146158ae701b995120d11ee21c34cbb6c3
~ _GPIOUserLog : sha256 73b09128db8632514946e6c4cbe9627528385e135572feb286b9e3a9e271255b -> 609ce7546a4b06f1e9b0522a99bd168bd06c6515ccf4e3c5946cf02797399b59
~ -[GPIOUser initWithName:result:].cold.1 : sha256 20ce7d021d05cfd0d1f612f91f3cb81296780ffcb203ff2409d83be66b7a1088 -> 3fca6a22e54fc418ae45135d2c30b7c3d8227bb2f5db87d939cafee33bba241b
~ -[GPIOUser initWithName:result:].cold.2 : sha256 4c4f63d406ebff469f9a80ed7673e7e3dc5f7bacc7d8399e86a827795e6222b1 -> 1947dccd914854c4aba1e1dbb01af95a582dabe758a7f9efe990d034d45b0b9a
~ -[GPIOUser initWithName:result:].cold.3 : sha256 bd05f7bae16bd3824ff4a02bc63aaee9b4a78244ef9b970e72d36e45d1fc6d46 -> b214c0172547c9803c6a38a27c080e3e94bddbcfd22d4c256247ed2ce9b45b57
~ -[GPIOUser initWithName:result:].cold.4 : sha256 68f932ec95c20212a9bbac66d8530b1dc6618337eeabf656ba0ba6608a78a045 -> 95bbbc9d0721d5220843efd9efafbf0e44bfb10d4ca14f57dd73fd3ffc58f69a
~ -[GPIOUser initWithName:result:].cold.5 : sha256 4af16795f9226c4e0d6b43aed851f88a63a630bd365f60c06a663df7f0f44b47 -> 493b459a71bd749e76602bd81b772b75a497d74cc5646b92be5e523ac2e809f6
~ -[GPIOUser getGPIO:].cold.1 : sha256 90644945e98c80578ea720a707303b6a5b53a2e431812f8250917f30ee94fb4e -> d603bb927818b9c2b3d48d91e10ea73fadea8704e7835b936f92f7c465c7d274
~ -[GPIOUser setGPIO:].cold.1 : sha256 d0b5aeb9d2d65e9dcba7993b7df7cf23e8e9121e52af2f424f5cb76366b7a381 -> 32ec6796b1de49839ee0d48a5f9265a982d8c75fe090d1b227f0f082d1148a49

```
