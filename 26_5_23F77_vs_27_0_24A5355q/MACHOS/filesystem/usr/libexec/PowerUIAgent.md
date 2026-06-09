## PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

-702.122.1.0.0
-  __TEXT.__text: 0x858 sha256:259074a600fd6efd49ba89941f04faf8291a5fff915c40626e909e8611b39195
-  __TEXT.__auth_stubs: 0x220 sha256:54ed2afb89a2e771e6ac53f7a4b6ed008e7ab4cdd56e345de1fc15441dd1c5d6
-  __TEXT.__objc_stubs: 0x240 sha256:76b02c77309b6b853e6ce62075b3da4450bae89e3024dda764a1cb9ee1c93902
+752.0.0.0.0
+  __TEXT.__text: 0x828 sha256:09d2f688b8aa3b6e36d789344563c737442225b690fabb4adc3819aec53cbfb9
+  __TEXT.__auth_stubs: 0x240 sha256:57564df015092a9cff6278c5e263ceff869f99766f39b246171b5e6ffc622efe
+  __TEXT.__objc_stubs: 0x260 sha256:4346a8cfa32a50dea914d78d1e33679573342cbfd1d1803a8fd3123db3fb2f87
   __TEXT.__const: 0x10 sha256:b1e4151e6fa08dad88b98c233f5b2d5df323afa294c4698f45bf7b4e4d59c9d5
-  __TEXT.__cstring: 0x21b sha256:a0b251694d79fb4732619741efc72cb0b36d2d189fa5d0a3147219770a6d2154
+  __TEXT.__cstring: 0x211 sha256:d6cb6659547beba4e12151f9e185be70bbe05d09b5f93ebd037216f0218aa137
   __TEXT.__oslogstring: 0x7c sha256:2d6a74837a45c9964f3a90a28e16b7a8283d0a9f4177ebdab5626ffb61e7cc71
-  __TEXT.__objc_methname: 0x16c sha256:c3ed50230ec4ed42e2f9e6ce1348a1fb0f85fe6d0340294640b6e839eb65a01c
-  __TEXT.__unwind_info: 0x70 sha256:f26302799d8a128efc72d2cb36922d1d904874897d4dca0e2607673744f8db9c
-  __DATA_CONST.__auth_got: 0x118 sha256:2abf045c781a76e5a16d8c60a597aed578a91b406a941b982e182f813e02c247
-  __DATA_CONST.__got: 0x98 sha256:175e557c809109e1e47b5165f37f548d3c37d3705c33086584af26767cc3bf39
-  __DATA_CONST.__const: 0xd0 sha256:60a610b2a3dc7f417ae18a0880f97204db39544d56f86d5d8a4008c341903f31
-  __DATA_CONST.__cfstring: 0x60 sha256:65af9ef21306503f1ccf664e622d3d5bf8bdb297e06af0622e4b3e8598969af4
+  __TEXT.__objc_methname: 0x173 sha256:b26b0f0dd7473f84314c5950860356eed7838be75583684aa5e0df28e682dc3a
+  __TEXT.__unwind_info: 0x78 sha256:7c5916b6dfba2cbce8749085deffc29ef08a3917dd101981c697175600daff68
+  __DATA_CONST.__const: 0xd0 sha256:c8e6f874192c66fa6a37732d5abf264fce025ff6e6db93bc9ec0337a3c1794ff
+  __DATA_CONST.__cfstring: 0x60 sha256:a8b0820bf20c77b6367ec5f45f3ebaf2f86be3aeea6dc0e9eb345a2f903d594d
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x90 sha256:47dac1d4f597e165bc071f17d267d19de442bbed74120d99d7dc65e1d7d80493
+  __DATA_CONST.__auth_got: 0x128 sha256:3f1903881d18c301aea215149f0e7abf41fff2d8910523d93cec399924f448c8
+  __DATA_CONST.__got: 0x90 sha256:b176367a918fec849dfac9484ac47eaa88f6520a24378e88b98c81581e2ef04b
+  __DATA.__objc_selrefs: 0x98 sha256:9491397d26df5f8ce1442c40109b93787c34933182592df1dfd0364badbfe548
   __DATA.__bss: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B57F2456-F624-35DA-9F19-F482C6BB4D98
+  UUID: FC14B10C-AF80-348E-B46A-F06EE014D260
   Functions: 6
-  Symbols:   58
+  Symbols:   59
   CStrings:  46
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release
+ _objc_retain_x1
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000b38 : 420 -> 380
~ sub_100000cdc -> sub_100000cb4 : 1176 -> 1096
~ sub_100001174 -> sub_1000010fc : 16 -> 92
~ sub_100001188 -> sub_10000115c : sha256 c5592b64619f39e55a927dcdc309242a92a4420e58ddffc8fbf700948311c734 -> 50f2293acbf0da76c8410a58722b6daa8bb95df6c7f2b9e846cd0cf664a10cbb
~ sub_100001224 -> sub_1000011f8 : 364 -> 360
CStrings:
+ "isiPad"
- "chargeRec"

```
