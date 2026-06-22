## Twitter

> `/System/iOSSupport/System/Library/Frameworks/Twitter.framework/Versions/A/Twitter`

```diff

 230.0.0.0.0
-  __TEXT.__text: 0x2d4 sha256:e63b5fc44877086278826a49548efa08676c6283b70be4334437a05b70007f7e
-  __TEXT.__objc_methlist: 0x13c sha256:23c799ee7e5a075ef34b4f10a826ac3c05ee85237151208df6c07f33acc85686
+  __TEXT.__text: 0x2d4 sha256:d2d9526c3a2566fa80bdbb88e5359b34890d0f585ba308358a824c561c5bb901
+  __TEXT.__objc_methlist: 0x13c sha256:42c5938197a23148f0de24391da294b5febea1a334eae677b82ceebe0261729c
   __TEXT.__cstring: 0xc sha256:0603a8df27ac2211b7ccbb5d463a1552e62fba99e30dad2627fb61ad4f5d834c
   __TEXT.__unwind_info: 0x70 sha256:e7694a3b8bb6ff655c866f53a6641632bedd842aa1c25516686b40e4fb3b6c19
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__objc_classlist: 0x10 sha256:fae7cb5f69385bd3d972963efc6754d72d7f6063706c8a4e3052f011308bf8d7
-  __DATA_CONST.__objc_catlist: 0x8 sha256:dc110b8e2103270d65c8d68307e33f1ddfe6ea27581a7fb0978fd14a8bc13b47
+  __DATA_CONST.__objc_classlist: 0x10 sha256:f4b63c5e5bf4fd7e36d0c2657927452164d41c98167b8cd649a26f81802323a8
+  __DATA_CONST.__objc_catlist: 0x8 sha256:455822ba3dce9aa5b6aac3c625797dc50e9cc54cd7de73386912eb1aef6107f6
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x128 sha256:42a0ba53526a45ac36a0d263c0833e56b1defd3f2635b5c925f1f3f966e8c5eb
-  __DATA_CONST.__objc_superrefs: 0x8 sha256:31606bbbb2615a2cd22f66c0606ce6ab4b3c64b013143503f0e0c7e1978dd822
+  __DATA_CONST.__objc_selrefs: 0x128 sha256:64fc631e151c370e5bdaf3e4cd3e4c6e933cceca14f58cf10d11c0cc2d0b3b55
+  __DATA_CONST.__objc_superrefs: 0x8 sha256:c39060deee97b67b301b13343e210bfd510a7d3d1323481274b31e283cf62190
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x60 sha256:ac6a1fc0a5a50e64397f4fe729b21c923087566ad4e0f4fbd64f984b994b7f04
-  __AUTH_CONST.__objc_const: 0x1c0 sha256:1346846efa41e79e11bd52cd82e0900c82c5de81ce9809b6c0140dc2143ebfb4
+  __AUTH_CONST.__cfstring: 0x60 sha256:072a76b268566c13ff8955af9328b2a69af2905abb276d542dbcce5d04287da1
+  __AUTH_CONST.__objc_const: 0x1c0 sha256:8154878ae43f15ecdf0862b6742409d661bfa089106cba2db90f68d1f140b552
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0 sha256:96a818454414a453adbce96dbf49379aa7b6ea36cc86dd2bfe42a98da494479d
+  __AUTH.__objc_data: 0xa0 sha256:4b060c0ad5e01c0f0afb40d983c9d71e4366f489e076b19fe712ac1bb0e344e8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/iOSSupport/System/Library/Frameworks/Social.framework/Versions/A/Social
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA43415F-78EC-3DF0-8F45-D6063A837CD0
+  UUID: 862E9F82-688C-3FF2-84D4-3295502EC69A
   Functions: 23
   Symbols:   70
   CStrings:  5
Functions:
~ -[TWRequest initWithURL:parameters:requestMethod:] : sha256 2bc03fe7b470186de2f46c29eff602ab32aa435fd36dfc60b71de0b2723f3b80 -> 65f2fa2325cab8a4cf29223f3df277d939d30a17e933c888b6fbdc2dd1045ab3
~ -[TWRequest dealloc] : sha256 5927bc981508e48f8be213bdc0226f51990d69eb685ff8c540a453697d22ef35 -> e69813a346b630336283a41a7f64bcf99e8e4ba2c7f5a40e17504f66b2b22f7b
~ +[TWTweetComposeViewController canSendTweet] : sha256 98ec09ad30353cc8f44e4de46cfae4f47650d177aaf6bcb84ea8e3bd087ff7c0 -> 2793c5f92ad16b06363c6d82949402fa134741d139a3fffbe7f2c648dfca68d3
~ -[TWTweetComposeViewController init] : sha256 3b6a737574d1b42e0c6ef7e3aa445f13f6db07e3234bb699926569491fca382e -> 84c4298dec26baa9290c2f6c8124bac9fe383aec407e602c2079eac459cff329
~ -[NSString(TWStringAdditions) TWTwitterCharacterCountWithShortenedURLLength:] : sha256 5d479b1eb080d265380fea267b088d8a151e90cab22a73ffd51bf730cc755b61 -> 6ff5050fe1d2bf032011437d2eb6b2a520aeadf4df6e911f8043f9a62de2e891

```
