## visionhwserverd

> `/usr/libexec/visionhwserverd`

```diff

-4.4.9.0.0
-  __TEXT.__text: 0x450 sha256:fee73fdd6f11fdeb1cd0680f7f60c92b25b6dbf195174ed5c0da048bf7c42cb8
-  __TEXT.__auth_stubs: 0x190 sha256:71429a75c0ae9401cff6d7128be9f588829f79bad696c93fc4af65117d74fd26
-  __TEXT.__const: 0x28 sha256:40beeb9bb57d74a1522dd02af9e4ea36c8d994b8504c7b59c9be50eab343fdc7
-  __TEXT.__gcc_except_tab: 0x58 sha256:d98261c9d7a612924ea3fdbe3da40bfd40745e75da823831e256af77fd2a84ad
-  __TEXT.__oslogstring: 0xa2 sha256:f62fb4ef44935bce61542c4df84ed60c627516dcbda9e7bf31c80bb8f718a1da
-  __TEXT.__cstring: 0xbc sha256:ce06bb685ae8d9bf5421d03672b58fc1f8c4ed51465199bad00e81667032c323
-  __TEXT.__unwind_info: 0x78 sha256:9fda855687bb93d8cd79ca75c967f38255fa3ef770722416e7317086fbb5fde8
-  __DATA_CONST.__const: 0x28 sha256:dfe83fd5ab779a95b1b6c013f414957db40c33fcf1c0b093f5a90f36bf9a0b3a
+4.4.10.0.0
+  __TEXT.__text: 0x4d8 sha256:3d33e22f2cac3aa57506a93921ea967f13afd19417a77d9bc277182d6b7cef2e
+  __TEXT.__auth_stubs: 0x1b0 sha256:5cef1b1abe145f7f1a0b81ef00a8e2422e2226926b4c7622e5ecd926f9ee1ea7
+  __TEXT.__objc_stubs: 0x40 sha256:a509bdab1e069fee4f8d4875b10413bbe39deeb349fa796eb05cbc3729d05011
+  __TEXT.__const: 0x30 sha256:95919274aba4b2441fc599f0cf78f6dc9f6e3a60c9edac451b106e6952487a9a
+  __TEXT.__gcc_except_tab: 0x74 sha256:fa6b2ec7851fd4bbbed5005b727bd8fabe5de5fe386b250223dcab384862e203
+  __TEXT.__cstring: 0xd4 sha256:33070766f8dcf498d522c507565dff90cc454094b70a3cf8d5c012684c2e3f3c
+  __TEXT.__oslogstring: 0xb8 sha256:faeda4fd619a0a8411d04ae991f312663ff86c750c1b9ffb1b4e130f375f7395
+  __TEXT.__objc_methname: 0x27 sha256:e6e7495857d4c5dd37f5063e1869b06b7b764e4fd8e78b765d31147692fbade4
+  __TEXT.__unwind_info: 0x78 sha256:4be261ecdbe758c7d4ba9b6e1c2565a426a2750845c4185043eaa40400dc1d37
+  __DATA_CONST.__const: 0x28 sha256:83baec44f11b2eaa066aa7b96cf661c48b6c0aae2e800bb970c1233f1ec4d845
+  __DATA_CONST.__cfstring: 0x40 sha256:16e03209e670a65e2d7b4d0203c5b6d5e2ed68d26a0f8e1d5211e3eec6fed541
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__auth_got: 0xd0 sha256:38c7b846c0f0a17351ba902736c9eb358cb3d4095fb5a980f5afb0d6a0cd1367
-  __DATA_CONST.__got: 0x28 sha256:672ed465d232c00cb91d3bea90a4ea35f443ab030b1eadee3552ef088771b090
-  __DATA.__bss: 0x18 sha256:d0cb04e67cf7483723d2025141dbca663bbbd04b696b75aeae59acfcfc3b94e7
+  __DATA_CONST.__auth_got: 0xe8 sha256:6b4d544a3a7550c1f30da98e76c6023afccf3db4b0b1473672cff6d7244e916e
+  __DATA_CONST.__got: 0x30 sha256:c5e0320f5491289a06ffc8313aab6fa984eefd8bb5f8a60dd312e7829b7d4e57
+  __DATA.__objc_selrefs: 0x10 sha256:7668bd705d1a52b25cc87456cc0e402827571311c73a39b840ad9be99810d7bd
+  __DATA.__bss: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BF1DDF01-2B4F-3B68-A19F-C2B4DDE33A36
+  UUID: 2FB62B05-800B-3223-9A0F-CC2CE67D17E4
   Functions: 6
-  Symbols:   33
-  CStrings:  11
+  Symbols:   38
+  CStrings:  17
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ ___CFConstantStringClassReference
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend
+ _objc_release_x20
Functions:
~ sub_1000031b8 -> sub_1000032f8 : 880 -> 1016
~ sub_100003560 -> sub_100003728 : sha256 003f89f0aac1742fa1859928de573f1d3abff6836f10966360d8799e263541e8 -> 5b9dc54870f863b07ce53351a0a3787fcb79580f73bc834ccbc25ce943db18ea
~ sub_100003574 -> sub_10000373c : sha256 106296b3d227e0b134656316fed01969cf0c3fb736943b9e969fbe27e411674a -> cacb6845147c719d91a739d3be98220cb8e3b61d6bfbeb1546a89c54e8d55b02
~ sub_1000035c8 -> sub_100003790 : sha256 2a71b08aa3c4de9fda6ddff49df12eeb19e69dc969e7c13e8003de728b96b61f -> ef427a53d0144152b1bf019ecaf2c48d9094d5de1b2c479fce9473cad8bafb39
CStrings:
+ "CFBundleVersion"
+ "mainBundle"
+ "objectForInfoDictionaryKey:"
+ "unknown"
+ "visionhwserverd (version: %{public}@) is launching..."
- "visionhwserverd is launching..."

```
