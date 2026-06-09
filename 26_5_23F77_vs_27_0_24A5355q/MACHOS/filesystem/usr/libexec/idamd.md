## idamd

> `/usr/libexec/idamd`

```diff

 24.0.0.0.0
-  __TEXT.__text: 0xabc sha256:6cd80835c6837a1b03c647d047d4ac22c50356bc0708f16e8ab5890328d55d85
-  __TEXT.__auth_stubs: 0x1e0 sha256:cb78eb3d5640ff5cf166dcf56f5fa719e98958bf9ec695596cc1e83bd59cafd9
-  __TEXT.__init_offsets: 0x4 sha256:afc2cc3dcd366eae49326deaf3299dd09488ff6152ab785a9dc7e2f23acb1dbf
+  __TEXT.__text: 0xa04 sha256:f282ff846471e90403b3a7a8ed7f2ae28300a297243ae9c0cf6bfdbb8d74c212
+  __TEXT.__auth_stubs: 0x1d0 sha256:4c56b535109816bece209f1dcd2a7896698fbcc4fb55fa928eee844fa237d03b
+  __TEXT.__init_offsets: 0x4 sha256:50321de88bc8ae22ca0f47c5b5821be91a26c2a5c5cce34d09cbd097fd1de770
   __TEXT.__const: 0x10 sha256:7a0d0926a66a4542cc22896ddcc54f01cd063cb4a318342f01ec8b4436049015
-  __TEXT.__cstring: 0x169 sha256:85be88987472a4084cf6a86ff68ec0ab83a4a73752063f232fe8fe8ad6d2ee04
+  __TEXT.__cstring: 0x168 sha256:59182513753dcd91ab54ce1f6fedcf6932e406effcc7b7cf38f71bf0ff7a597f
   __TEXT.__oslogstring: 0x2c3 sha256:6975d68a6ad1a5ef92a8f217ec669cb334fdc97824ad618fc0493403b6c930d0
-  __TEXT.__unwind_info: 0x70 sha256:d23412d1ba34d428588af5c2f87a36d0859952b03cb327ab2d93eba0b4bbd569
-  __DATA_CONST.__auth_got: 0xf0 sha256:be5be13008debb60ae1178c78928d722a573b0c5236acf9fb83ca0b51c97f195
-  __DATA_CONST.__got: 0x38 sha256:49a07dc66356296e82fd66ed9d8b40615a75e1c78cf312f527d7537f797d0def
-  __DATA_CONST.__const: 0x40 sha256:5d721237face964a52c4be62329c4ae8f6e8c9a0bf4f1d29beeccf20cbab8f8b
-  __DATA_CONST.__cfstring: 0x120 sha256:d339d3eee4d4daa948ec8196715b122a28568683867e02e3184fd07876fb5cc0
+  __TEXT.__unwind_info: 0x70 sha256:3d44b5630fc664772c4087864cac7236eb4572cf702232ed5484d94ff0b0db10
+  __DATA_CONST.__const: 0x40 sha256:db9f3d86949c059e780a98c497011535b7b303d0bb66719492c735d8b4dacfbc
+  __DATA_CONST.__cfstring: 0x120 sha256:cff186bacbdd5c85f2e4b35c9ca4816ad29ab9145ce79107ba5ac711460aa13e
+  __DATA_CONST.__auth_got: 0xe8 sha256:5f636d1b01bff8439bf10e90ecbb881ad5b1f018baa16a5d8a5e71fed7504231
+  __DATA_CONST.__got: 0x30 sha256:e02bebaf65c61b24b6502c30bc9d7f21dd52ec3302d01e55a7c77bb22ccb1d17
   __DATA.__common: 0x8 sha256:6eca5cc86a53c80d74e777fffd48ee46b98f06a8b448d18106af49ac0862b875
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblockdown.dylib
-  UUID: E1A81E1A-6811-32DC-8593-2CA3E8398997
+  UUID: 38EB8CFF-0D7D-325A-BB54-7F3F41E812E2
   Functions: 7
-  Symbols:   41
+  Symbols:   39
   CStrings:  44
 
Symbols:
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ sub_100000888 : 948 -> 904
~ sub_100000c3c -> sub_100000c10 : 260 -> 216
~ sub_100000d40 -> sub_100000ce8 : 236 -> 192
~ sub_100000e2c -> sub_100000da8 : 1080 -> 1028
~ sub_100001264 -> sub_1000011ac : sha256 b15a375db567b5d390405de6f7957e2b737283c004a63d818735b7b6fdb09ac4 -> 75d3e5dd0688282f5d1527626571305aad1f95f7a382f04213d2e7e967a82844
~ sub_1000012d8 -> sub_100001220 : sha256 679dadaef5fcf45f39880c0f3f8177821e987d1ab67093f5a03c0a1f86cd985d -> 48f4e4650b05b243da7f8236e86c109f25c5ff1766896518cc308ae1291579fc
~ sub_100001314 -> sub_10000125c : sha256 968cf667095fc8f005f504d653f7eeae362425a21da7612da7fea7ef67a1b796 -> d61b38dec768b6e4e308cde095ee5cc40c9c2ff61f0d6610a5de5ae6eaaff804
CStrings:
+ "MonarchLowEndHardware"
- "s+gaKNe68Gs3PfqKrZhi1w"

```
