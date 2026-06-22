## biometrickitd

> `/usr/libexec/biometrickitd`

```diff

-570.0.0.0.0
-  __TEXT.__text: 0xc84 sha256:9556a1646718a621f0ab22d39ed53d79701f4fdca187d1973c746d6b85ffdf00
-  __TEXT.__auth_stubs: 0x1e0 sha256:78e54932981ca7993a19546198cb1f9d5e482363f865990d2a75e4a8331a3626
+573.0.0.0.0
+  __TEXT.__text: 0xc60 sha256:629b62b2f1bedb0da9ad57ca38f693da01600924c1b8b3e476e580b27261f85b
+  __TEXT.__auth_stubs: 0x200 sha256:fd0cc94fb518b4119643a644418458b4e3261e6e952a37869ad99e41eea90a3a
   __TEXT.__objc_stubs: 0x240 sha256:e4edad2d97f6a8478c9c83ba74bf98b6813d5be8be225adb571e0e1cc27f263f
   __TEXT.__const: 0x18 sha256:98cea725c582ea1b4b846718cc32a34f7cc890afe177626e263c54c44ad00222
   __TEXT.__cstring: 0x15b sha256:9b2974664e35c36a2d44d1eee15c3da2e7a4752782b440e212f72500ec7785a3
-  __TEXT.__oslogstring: 0x1ba sha256:c7dd0ce7b1e99a7cea9faadacaef703d610a9ee05f538efb51d9ffb904bca306
+  __TEXT.__oslogstring: 0x1bb sha256:70ca8cbcf9b0ce2869398b71973f697bcf476eafa7249ed55c3b6273b6059808
   __TEXT.__objc_methname: 0x10a sha256:2da11d3861739742dacd37e54921a060629de7d3e115fd2ef988e42aeb124996
-  __TEXT.__unwind_info: 0x80 sha256:935c47b9be4bbf0e68fe8b31bfeae156e437206cf8bd376cf356067a37ccbb47
-  __DATA_CONST.__const: 0x60 sha256:cf8e8ee5474c17035e90f60f88eaca22d02c67a41f8cb29b26fe7e573fc28175
+  __TEXT.__unwind_info: 0x80 sha256:fa1163b47118165b13a97bb69f2c68ba6513f6c1f1ba081dd9a0b8da301550ab
+  __DATA_CONST.__const: 0x60 sha256:4a4265e5829db374d77fac433cfb6b7fb9c688178339a9ebe36be5c4e14444a9
   __DATA_CONST.__cfstring: 0x40 sha256:d5bfa7a4a4e6c765e73399e21d4b6af916032aa69b3594a9c03120faf57c31d1
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
   __DATA_CONST.__objc_intobj: 0x48 sha256:b9842e8151ba100755720779f9fc7706eb80702c7945323082dd85d7da49ffb3
   __DATA_CONST.__objc_arraydata: 0x30 sha256:f0e5414c010aef3505b2529a37b97ba95ccef198870291459684e4ea23643842
   __DATA_CONST.__objc_arrayobj: 0x30 sha256:9f1ef224d77ae393efafbcc01ff48e4b7b844e1887fb8e926e0d2fa484acfb68
-  __DATA_CONST.__auth_got: 0xf8 sha256:bf5844052bb805b3f79431d4ec1e729a0a0d9bcd7be602e5fb2c66fa3be9ef19
-  __DATA_CONST.__got: 0x40 sha256:371f5a38c4d866cc577c3d38f3556d8fe328d5f1f108e1880783c295cba807e8
-  __DATA.__objc_selrefs: 0x90 sha256:ac74484211fcb3c59dbd4063ccbe574385c61f78d86d061bbd4f56faca0cc082
+  __DATA_CONST.__auth_got: 0x108 sha256:d2a09e5983a8c0ce17d3c7439f32622579f4078f9197cce4099722aeb500152c
+  __DATA_CONST.__got: 0x40 sha256:232111d68c5247fba3cfee2548a06d202315e68de7b083130b8f15db7f718224
+  __DATA.__objc_selrefs: 0x90 sha256:612d431504770ad0fc037d0d1656085067b2e9e7f98ce13de527bce8334f0e6e
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74814B35-BB8C-39DC-8FD7-0ECF769BB811
+  UUID: 0FA68699-E173-341E-A6BB-998AC09EB0E0
   Functions: 12
-  Symbols:   45
+  Symbols:   47
   CStrings:  47
 
Symbols:
+ _objc_release_x25
+ _objc_release_x28
Functions:
~ sub_1000009e8 : 2432 -> 2404
~ sub_1000013b4 -> sub_100001398 : sha256 a1f5731158d53b0fa021aacdef8238e8d7c14307e36e988973edafd5d9b5cf6c -> 6d99f0c3ce74f13623f0a5aa0042fc00cfab2f9b83de48e1607269d3825c0502
~ sub_1000013e4 -> sub_1000013c8 : sha256 b47dd6bc235c82d64887079b4b8fb23988b6ba9220ee93cea362d9fd54635db8 -> 19d2b4580a3679d802d5789b0e8234e6f380083879a425940ed262ed7954625f
~ sub_100001404 -> sub_1000013e8 : sha256 bcc0bb839862bcaa5152883b3e9336b922033c537d28bb4ea542b70cb2cb9c20 -> a4f4ab2b7c7ced4899ebaaf6d4b12b3cfcb666dd8f1111968ace09d89326fdb8
~ sub_100001444 -> sub_100001428 : sha256 5b4fdad2d33cb4d5341b765d99b2a9e0bc5d856f374ef28b138018f22438f4d8 -> a392a09b23a040a08120d115da83061c460da842ce2f37bb1e932b12daef7731
~ sub_1000014b8 -> sub_10000149c : sha256 415d055001481077952ef972dcf60e38b26e26dd23aabec23e00fb7555a61dcd -> 87b245dc9eb25870a184e23f92c9db25229eeb89820bcdb4b9ad0f02af3fc778
~ sub_100001574 -> sub_100001558 : sha256 6b4851ef75db06b0069e40690fadcfae5cdb35824738719b7d4866782de80e5c -> 7481ab30dc72b7ba41ccd06e12ff788d21f923703e30b231f068ca57f7816e94
~ sub_1000015f0 -> sub_1000015d4 : 124 -> 116
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-573~1109, %s file: %s, line: %d\n\n"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-570~896, %s file: %s, line: %d\n\n"

```
