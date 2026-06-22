## AppleGPIOUser

> `/System/Library/PrivateFrameworks/AppleGPIOUser.framework/AppleGPIOUser`

```diff

 65.0.0.0.0
-  __TEXT.__text: 0x788 sha256:8bfb5b10eb6d2fc0dcdca648e7605ad731d24eb6739e123c1e402c74f087edd4
-  __TEXT.__objc_methlist: 0x38 sha256:ff6c243a59991f19fdbbddeb92685fe1ee2ca0dc7b27a84016ed5405923d2744
+  __TEXT.__text: 0x788 sha256:2fa6fdaf438aea86370c7bccc8ff52b6653198172694b7088a207c2b3f67f16a
+  __TEXT.__objc_methlist: 0x38 sha256:970c2052d92180cfc2d863f8d02337e72cfe97bcd1bdb8c38f2595e09f7ad350
   __TEXT.__const: 0x50 sha256:14942f87dbafda3e16f1e96cae69bf2841df3dcb975fc0fe33a4d591a3a672be
   __TEXT.__oslogstring: 0xf5 sha256:1a5a287e3254d7e6262274bf9873fb6a3f70b27b773227ed8ba3e6a8ded4978c
   __TEXT.__cstring: 0x36 sha256:4bd53b15f82b49d36e073acb896844b38cf2ef5fc3053f620b1551d09cfd337d

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__objc_classlist: 0x8 sha256:640c8ba28777164cafbd45ce3e2e12bec3e9746607a0aa2ac016787c60573587
+  __DATA_CONST.__objc_classlist: 0x8 sha256:583f9eb348985800827e2e2132384ce6f37902cc30eec7f3a2d8ea854b5b8a03
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x38 sha256:9062389f696ff8c337983139a85ff50dbfb764c460ff1eba0472c111c4323f52
-  __DATA_CONST.__objc_superrefs: 0x8 sha256:4a8d10f88e142760217809ebcb0ff775a71d26468aef0ad3d8f4e1581a949db0
-  __DATA_CONST.__got: 0x18 sha256:6c77560d15accab8d238ef049fce1990d513f9ba8a8de12015fe9494c196fdfa
-  __AUTH_CONST.__objc_const: 0xb8 sha256:c494109c0fe4db2e796de3f0b26ac689f972759b6b7fa3591b76243144344fef
+  __DATA_CONST.__objc_selrefs: 0x38 sha256:bb937da284527211ef2d1dfbc8aa753114be8b4a9ee10fce6035bbe95274d0dd
+  __DATA_CONST.__objc_superrefs: 0x8 sha256:960f91c77e481bf01b15cef5b66eb020c0a3320e666b812d5fbd81b3ccebb397
+  __DATA_CONST.__got: 0x18 sha256:232bfc4009167159297869b86851319cc1bf95370cb74f00c3b45a4825d94fe0
+  __AUTH_CONST.__objc_const: 0xb8 sha256:5560102da26875ba28fae6865aaed9cb0dfd02e94719b06e9efb9f233a13ec55
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50 sha256:441ae25f9da0a0e302df519e1d2e57fb87e303c1e786953af87cf3a28f6c5fae
+  __AUTH.__objc_data: 0x50 sha256:3b8a055d593a906669a82dc5035b12392a6276d9e46320fb10f7b5f7c9c2bf32
   __DATA.__objc_ivar: 0x4 sha256:dc765660b06ee03dd16fd7ca5b957e8c805161ac2c4af28c5a100ab2ab432ca1
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7DF7108-FAF0-344D-92BB-FEDBC16EC315
+  UUID: 20440DB9-9BF7-3C80-B1BB-5370C526BB93
   Functions: 18
   Symbols:   81
   CStrings:  12
Functions:
~ -[GPIOUser initWithName:result:] : sha256 4ecbfa2f7aeb9047842cb2bc00e7df527706c6e55bbd4991ccbca2136f36db5b -> 06d5d5c462e3f5e648b3b46bb922b2cda969c2aae598bde170bff5dbff84f01b
~ -[GPIOUser dealloc] : sha256 fb1364ca4fde78447c258eb5d531a9ea999411aecf1375363f0eb0f8bbac80dd -> 167086f75cbafe10775fa715cdcb6a5a075f14904d28ec122e024c365ee64c00
~ -[GPIOUser getGPIO:] : sha256 984358856034cc2b198b386688c9d3f2bf8bc2cea2d95fed9142eb5f9c32cb3f -> e1859e9aa2aae2161c223018563d5f1badd6400c2af7dde797d8e0eafb16da90
~ -[GPIOUser setGPIO:] : sha256 e364f726de1604e263791c839e05087bad8459e8bc4932e472c83faf70e56a6f -> c01e112b714bdba4228520f70a9f415bb95ae269f0f7be79d240fdf5c356245b
~ _GPIOUserCreate : sha256 94d0fa06509599b697ba562b12443c69a21a5e6b0a53dde7a62da71bee77d9a3 -> a666a901b53799ff4edb019fe49c2803aeb71b434a50701d7b0322a725e19859
~ _GPIOUserGetGPIOData : sha256 502c07379f1bd8a30e16200c366884b30cd04a59f55758d8c456dd5892a3e548 -> dc05f2bd83ea50394d842574ef9ec93829900edb66d301b651103ffc49d9202a
~ _GPIOUserSetGPIOData : sha256 f9437dc4439edd40f13298e38719c786daa693e7f37132470709e65b643b1f78 -> fd80ee89c5fe9abe919f6f233674013076422275bd70643394f2792fa0d1c1f5
~ _GPIOUserLog : sha256 b8e5cf8c6aa8391c9c3968788f026e1a9f09c6a1e1e51b510daccce3eaf684fb -> d2f0eadc51f027ec74fa0a424f362241a09f7a2804420a7cb4b9e2ad50c7bf6d
~ -[GPIOUser initWithName:result:].cold.1 : sha256 a1d4c67fcf4286441b81658d2044ea161f7fee34ec8db1619c83b9aa202cd6f7 -> 1ebfb99f94bfd45546aec69ebe9e9a4577dff9c475090d00a14c821af9a17b43
~ -[GPIOUser initWithName:result:].cold.2 : sha256 2c0560e06c162717ccc13e69479e457874fa3029dac7d7607c1e58bba39a8f09 -> 32cbdbd71614bf37640c0dce3c2bc3ed3b95a466dcd54e8b4562d851cad9887a
~ -[GPIOUser initWithName:result:].cold.3 : sha256 6712fda40061be88f67f7cae6a8b83ae86e091e5616f29dffbff0526cc942389 -> 813ff2009aa67c94319846086cf51cabd8484b5663a2b7cde0e74f05a8add945
~ -[GPIOUser initWithName:result:].cold.4 : sha256 cb91f1120b298740557769bc4f1c01f14aa13d473b32bd562621cde234dd57d6 -> e50c5dd5d07ca4a6ef628ba1f0d55f2da2c506ef0fab5126efcd3358c21ce9c7
~ -[GPIOUser initWithName:result:].cold.5 : sha256 ef5de5dc3edeaf41c84f6ca2a6f79f26683273c147ba4367bea4a1349ef164dc -> 41d79942e2bffd56e72dca1a39675380d9fa1449722b95b877f0caab0dcecbc9
~ -[GPIOUser getGPIO:].cold.1 : sha256 94ea26de3e51f5ef20a28adc34eccc8c8b3afe3d3ddc22bcef25e90533e03ecd -> 66364c836792fcb59b20225aff6067ad968b65458085bd4d309593abbeb26481
~ -[GPIOUser setGPIO:].cold.1 : sha256 1614cdfb6948645e6e8d3ec8aa266f61bb0d533e9b320f66771da690be494441 -> c7d4360a9d0c97653b83275e0817e2e947efac9649585ab76f7757af703aad69

```
