## libplain.2.so

> `/usr/lib/sasl2/libplain.2.so`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x1b04 sha256:9a9eed4907994b56f666389620761ba692f54e24745ac37ea7b653220b9fc2ba
-  __TEXT.__auth_stubs: 0xf0 sha256:74e95c0e767970d543da8951a92decaf80ae79e7ca8dbe32b076b31f6d138fbb
-  __TEXT.__cstring: 0x563 sha256:3eb95c608b25d694b374371d0c1c423669dac37db3aeee1e502b926725bd8f47
-  __TEXT.__unwind_info: 0xc0 sha256:5f7647140ed81f00fdf3d2a5a2d4469ca8383cafdcc6d02c4240c2ff8dd9b617
+217.0.0.0.0
+  __TEXT.__text: 0x1b34 sha256:f5917acea3b706663396290431461fc331d5d5c0564cba13cf7daadf77c1ee72
+  __TEXT.__auth_stubs: 0xf0 sha256:951a5c7b72d795900614153af7ef76cd993a4ec518eb3391b96ce476fcb3869a
+  __TEXT.__cstring: 0x563 sha256:709bfdb4a518be4425037be54871087c10b7f1397524a6d0aa8f3a5c125f454d
+  __TEXT.__unwind_info: 0xc0 sha256:04a8b79c14191e8345e95203cb643cc3b49851ec594071056868693e6f7ba4b8
   __DATA_CONST.__auth_got: 0x78 sha256:38c345cb9cf8745099627a43c391a1581c0c6e90e4af5679a2e9737df975dec9
   __DATA_CONST.__got: 0x8 sha256:342c14f50cc87ae753fbb43ed5599d9575578190e65d4f72909a50c20c019698
-  __DATA.__data: 0xc8 sha256:51b5d93910f7ad28cf441c70e7095e9ec6084c16651a2341668d60101cfe7d31
+  __DATA.__data: 0xc8 sha256:4bed3928fd12fcf054d38fa8b041f78c1af0cf0dd7bd7467ef3fd51b760eaf9f
   - /usr/lib/libSystem.B.dylib
-  UUID: 482171E2-1C2A-3AFA-B7BC-68951174B4D2
+  UUID: F0CA6DC9-BDC8-3A2A-9D2D-7FE95D101401
   Functions: 28
   Symbols:   46
   CStrings:  21
Functions:
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 64863e07c7ae303a33254a16bc377cee4c927aa2d5441e5ab99d9225894ed2a3 -> e5f604a975014e9c86e9f265b8fec81192ae5fc67732ebdabde0b4acf555bdeb
~ __plug_strdup : sha256 2c821c5409433e5013d78f8c81854cc522e0ba9068338b7f6f8a23135f54e166 -> d8984a0fd32daa69c8889d03a14cfb0868134dbef6694c41932a7db05be1418d
~ __plug_free_string : sha256 7d13499da2f67734e89eba0ccc790f9f7700299cd4b1d9fa610a784aeb38d259 -> 176227d62a6d28d1f284d82905a51c2643932d2aa757b3d77e91b0297840dfdf
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 7de32ed91c9095469d5a3dc788c291cb6ab293ba4fbbbb5288f3ecf3e4f6f9f5 -> d373231eb72e2a714a857f689d2660043af8d78698fe9e1adda97d2d8b72dbbc
~ __plug_get_password : 372 -> 364
~ __plug_challenge_prompt : sha256 aac3e30968937ae209fe5c26bf7903eae24c46d8e3440553658f774bbf3ba9d0 -> 6c1a791cfafb0e49226ec802d09d770c04d222ec0b1593c2d606f76ad3b133af
~ __plug_get_realm : sha256 2fcaa779c8d45eaac7160c5e84e9644a05193c8fc4c72ce11ac51464cca49014 -> c61823fe1f3bef2af99d1e6e22b573b9a5d42d8020bfa5b0075efde923d96f39
~ __plug_make_prompts : sha256 3c4f5f69db527add321432dd7d04a3dfab76c410b2c97ad0d41816d46df07215 -> d6564a665ff3f4b5040b25c9c25ded3fde3ca4e3237abe8c9b9f2176190fc87e
~ __plug_decode : sha256 f723db33f9b1e8c75e27753aa835d2c287acf0ebdf30f142cd6a366ff1bfca3d -> 9b2a2396747cf62c36d8f15dd6993715cf1352cd8314de0cd1e269087fb3776e
~ __plug_parseuser : sha256 41afbb894ed603a03d0913693e15874cb774b8464f06458971b0f79f49604736 -> ac4dd1114c8ad0adfdd5b8748432b46ccf3e7faf37b7baa776c11d21ffe6a423
~ __plug_make_fulluser : sha256 fcfd5b91666a173a810ab835bde60fc08b8aa165906f0e5f6a88849a13a251db -> a42f995ad4f990d045a09516ec078174c8876408ad644826738c75f47e7db13c
~ __plug_get_error_message : sha256 7b509d623791aa5e8d6d1ef61125173741f25bfd26d34ebc457e6f91f98ef1a7 -> 880cc495dfe006d3216cbd31a6d3d5c63171d1da2d60c9b2c4182456ffb3064a
~ __plug_snprintf_os_info : sha256 576f43476bd0d00a7dcd72ffbeb2a430b1a5bfb35563b4ffc16df0cf7fd2a421 -> c06e804652713dc3ec8a3f0792c282dabed9e3c37f0c8aa9196805a67532dd29
~ _plain_server_plug_init : sha256 fca880f437d9ddcea698646a63de185d9ee322635081ad00fd5fdfac00d8edb5 -> 9d76a8bdc6e80a67e17e6b4111ae0eeedd3d0b9d1f234d1dd71bd351a8f52ee8
~ _plain_client_plug_init : sha256 b3c6c801dbb0c35fa687b2aea180f27a9c3e47c60205b256360eaa8eb8c6ce1e -> d564b94ebd3703b89d729241cabc96afabc0156986f91ef52e5a45e39582df0e
~ _plain_server_mech_new : sha256 94933841be41a52172287fe64e782134d5db4d07166e9727f8c6011e62d2545f -> c29ff79746acc907b960ad5c3ab7b5a5969dedc1b417c4cf128f3e1d06fd927d
~ _plain_server_mech_step : 772 -> 792
~ _plain_client_mech_new : sha256 94b0c28b529caec5139e1325565f66026bf8e5ccae1f07260e46019acefbfa4a -> e624f45940ec55848af87398e74ca596f04bb7d7b9178ae3b1bdb76b1e339462
~ _plain_client_mech_step : sha256 94ae6e63d15e503529bdb43c03d256149360e2666fdb04ae5a6ef5345166f169 -> a5dd199f31df80afb2ba4dd2dbfa6be56a04e8a83e11a461926255e9b4f235da
~ _sasl_client_plug_init : sha256 350a8a4a35f64d4e42536292bc5d8f5aa5adfceb424697ee012822aae0088e35 -> b0619ca334a1057470d2e6481f53836cf9e9f7c705211d0da695e967e662564f
~ _sasl_server_plug_init : sha256 a3c69b958e11163b5e3b5129e051bd1daf5b78ea9fe9f28fa57a2ef260587ded -> 16145924105d626ea867b8b5013e7e15d22f7975a1875eb83874abba065d3ac3
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plain.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plain.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plain.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plain.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
