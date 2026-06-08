## com.apple.Bridge.appremoval

> `/System/Library/AppRemovalServices/com.apple.Bridge.appremoval.xpc/com.apple.Bridge.appremoval`

```diff

-1310.13.0.0.0
-  __TEXT.__text: 0x8a0 sha256:55e5d63b58f4407ef8baf89054cf53ae4ca660045cf1d086c668c8a868940c75
-  __TEXT.__auth_stubs: 0x1c0 sha256:8efed58a12fcc7227af407059c3145baed7bfe7d04051141bfc06fcfddaed5c5
-  __TEXT.__objc_stubs: 0x360 sha256:83e8832e985285b6852249912c880855ff3685fefc2cd54cea5d35fcd5d1b366
-  __TEXT.__objc_methlist: 0x224 sha256:891ce061dc272ced4dc2f7ffec6150de9b4a2d693984fb11a48ea96e766ced31
+1350.1.0.0.0
+  __TEXT.__text: 0x894 sha256:fb23ca2d204014355155d5834fa600bd40706c959c2fd089e1e0ec34be8a4a0b
+  __TEXT.__auth_stubs: 0x1d0 sha256:f37850f86e0560da0bc924e420f06a496d7c23583baae7fbaafa100310849f21
+  __TEXT.__objc_stubs: 0x360 sha256:0ed3e2dd3f3ba541c9f7bc65fbc0f5416d76ccd03599b793bd72e36266eca15e
+  __TEXT.__objc_methlist: 0x224 sha256:1dc5e72411c54abfa953f894a64024dbe145658f3e1f29ee4d977c0d40a14674
   __TEXT.__objc_classname: 0x8b sha256:a0dc0fd9274036dc234dc350c6cb9de7dfd74974bd83a00c3e6279f59752a041
   __TEXT.__objc_methname: 0x3b1 sha256:4fb47dbd71530b2be3cdf4195997f91a21e8b44864a0852b756fd7663fda5b6b
   __TEXT.__objc_methtype: 0x13c sha256:24f29e45d351497ac4a5a46302122eddaa7164c7ab450931c17162edee6236ff
   __TEXT.__cstring: 0x37f sha256:3aa07866f2566229f9e0b6f07e1d38bf49a5f1b7b2456af0144834c506dca169
   __TEXT.__const: 0x10 sha256:805fcf7cbcb198f638bce88e313d0572233b5dbdfe33fe18b94aebaec3f09827
-  __TEXT.__unwind_info: 0xa0 sha256:ae870051c116d8f2813f993349469e0002ec5454ac5d93653af86b5fa9079414
-  __DATA_CONST.__auth_got: 0xe8 sha256:e7de95c408e140d992dfc04937f67503f0b1e5bb145f7ebdbb6d0fa7ed3fabde
-  __DATA_CONST.__got: 0x38 sha256:00e4e8afbeabb5aaeb0c0eaf829501529711e4a44394b2e522f2365246409fba
-  __DATA_CONST.__cfstring: 0x2a0 sha256:67ec8afe958ba9b0246a3f76aeed702b4e5b12f78a883e37d62b2ac1cdf7dc2b
+  __TEXT.__unwind_info: 0xa0 sha256:cd41b3034d312b6e5a3e6cb56375a2a60076471d4a65e5683e872d0be540d14f
+  __DATA_CONST.__cfstring: 0x2a0 sha256:7f24e829461444d793b7284175f758af7f9fcc0bd67808c835509bf3c47a8f96
   __DATA_CONST.__objc_classlist: 0x18 sha256:6ecb548d6836c38c3de9608929fad84e6de1af41037abfd2e526766cb7042034
-  __DATA_CONST.__objc_protolist: 0x18 sha256:3b08d603197ef6c23fca13c95482bae8fc43fd155b6722f64ccce1882efb1cef
+  __DATA_CONST.__objc_protolist: 0x18 sha256:24a8a971ded639cc4e94fd5c93cafbb5e0ae9c44e415f5e8b3026d4f6a44c0b0
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
+  __DATA_CONST.__auth_got: 0xf0 sha256:eabb868bfd6e2c2b1e23e9aed710adb72fd233314b61734b85a4d8a6c4844045
+  __DATA_CONST.__got: 0x38 sha256:3d37962ccfe3500c85b09eeb4f69f8d03456b9d43ce6ac577139c84008b4e690
   __DATA.__objc_const: 0x398 sha256:cdb3dc1e691f56f749012089c4e6d0e080de10e58f74c639c6cfb135fe4bc73e
   __DATA.__objc_selrefs: 0x188 sha256:af5a1a2479eac342e1bd4a6fa8d3fd02f5898122961c5e126c235b728c298d9f
-  __DATA.__objc_data: 0xf0 sha256:5e5e918a42c59c4da11aab7d4e8d536ffee73b6947bf91d18aaff68e6d0c9203
+  __DATA.__objc_data: 0xf0 sha256:8f59f98eb9a52057018e79ebde3a1f61779d581c3215ba8fe4952b97d3044ea5
   __DATA.__data: 0x120 sha256:c3835d07e649471900012693d7456ea37d2a5439b707adf250ef0e118c05193c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 631D6DDB-2C96-39D9-90CD-59F73BFEF5C7
+  UUID: AD098A0E-F6FF-3659-A095-4CEB6850C2AE
   Functions: 18
-  Symbols:   49
+  Symbols:   50
   CStrings:  123
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x21
+ _objc_release_x8
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x22
Functions:
~ sub_100000bd8 : 116 -> 112
~ _main : 96 -> 92
~ sub_100000cac -> sub_100000ca4 : sha256 2fb25cb085b2d65880786ad766785f2ef6d88644e8e1c7217c15f4608f6528bc -> 0e4c67970d36e4a4302f9ae9a591e37253621ce54355f53c4eb4f51c7e049214
~ sub_100000cbc -> sub_100000cb4 : sha256 b009df9920e47b9c456e0dc1c6f826c988754852038d64b7aa739cae053a2f0c -> 138da4dc58866f7898b08d363cc26512b99600fda2171736b6a060edc930e2e3
~ sub_100000ea4 -> sub_100000e9c : sha256 d1d0e50a47eca187379d08ced9bb2da9ec00e81fe196dca0bd1005deb5308a9a -> 7254db976d9624e8f94358acdf1bf21a51298ae91865d06297eba33897af1671
~ sub_100000ef4 -> sub_100000eec : sha256 059b4402a78a15677bd1d1633da6b3375c1af8b8ac7211c42910cec9335dbd17 -> 930060bbfbaf4fb679bc57340b5c2f01a7ffee30689bb41fe3e11e3797cb24bd
~ sub_100000f9c -> sub_100000f94 : 160 -> 156
~ sub_10000103c -> sub_100001030 : sha256 efa4b7cc61798649c45fbf16708638cacb40e6975dd1b8542e3b9460a5e56a67 -> b0312e5f342d143c0e2ff7e63c17d164bec6d67459e2664351d31a6274268fe5
~ sub_1000011a4 -> sub_100001198 : sha256 b7d99d59891c596e5f920b01d205b17088c92883efc99e222bec1188dbfe39b9 -> c152e4db0f16791f125f91d595139826fb9ce555c1b51384658cc42e8c070e38
~ sub_100001240 -> sub_100001234 : sha256 215711786a81b1b3ecf670b08cbfba355ae4f63582b198ac3fbf6d7deb8986a9 -> 2be3e6ba0093d1ff2c0ff31c04ff67f1ef3b2d5394b30c7029ee065ee35ccaf9
~ sub_1000012a0 -> sub_100001294 : sha256 0816a3c377e6762d0253f6ab91d38211419f36b6ae36c7fea56bb0a35cf32c20 -> 635184583a9058889af289e7f9900f3c333ed243b367b89093f0217a071bc1e3
~ sub_1000012d0 -> sub_1000012c4 : sha256 bfe9277c544b5e6f82632d6776f7f54943ac69a6871be684388b66563def187a -> 688cae121e56df3ec930252395e9d26b953d1a40d492ed8c8e581951be443cb7
~ sub_100001320 -> sub_100001314 : sha256 fd8e398f311dd7a9fc0061ae63eec32609736c07a90367e99d27b9535bbe3346 -> c2828d10a89c0e91f40d3b67e51b46bafb8e37137eee554401c3416472cd4093
~ sub_100001350 -> sub_100001344 : sha256 cd365d621f1a25b0481652c98b10ad4c07e8ca8c9ea9b597f0454ff698261c09 -> 1920b1c7bbddab39d03ac4d048b8bb847b0392a399d8cac335f0c714ced03a39
~ sub_1000013dc -> sub_1000013d0 : sha256 84c7624cf86808df556938aa465c05c812f10191174670e1cd5871c2ccfabe3c -> 2a44de7ea1715d72ce58dacbcc8245d44eb7c4c3401a68e2a4a0e8025a63d4a6
~ sub_1000013ec -> sub_1000013e0 : sha256 ac215eea8740b16942354003882d0ebf45c85364dbba771a681632f626419842 -> a394c4c81424f099b39f3f4d009a6ee688d61a036cac0a5f10880db7b2eec30c
~ sub_10000143c -> sub_100001430 : sha256 c157829e87b26c062583a2d3d500caf97b45503f553cc032556c41aafd6d3168 -> fec0b03ce7c7057995ab96c62e10953f916846b513d97c3a2dd8f7d469652a9a

```
