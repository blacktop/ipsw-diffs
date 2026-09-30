## login.so

> `/usr/lib/sasl2/login.so`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x1a7c sha256:62d7fd47ab0c89f86a506b99e5fe02befecbbd0398588404e62c3235d4e3ebf0
-  __TEXT.__auth_stubs: 0xe0 sha256:8e745a4a2743ea2add42630a6df4c325e90ec9edea251cf6e8ec670aa6db425b
-  __TEXT.__cstring: 0x5b4 sha256:ba06aeb10ad1005ae71f95ebead63055d1957b9f45501914fb0e341c78b8acf1
-  __TEXT.__unwind_info: 0xc0 sha256:a34196c92dc7cbdf149925042e7a11bf0cc926a920a156eb5d3c5e00e46b9b40
+217.0.0.0.0
+  __TEXT.__text: 0x1a94 sha256:9aa7237f23b865e867c5d76940139d91779a8b76fb93ef8c2789c7fe11bc26e5
+  __TEXT.__auth_stubs: 0xe0 sha256:377f8cc61436417d7f0ac44c01bf9039933cc2f6353faeab16adcdf383ffcba6
+  __TEXT.__cstring: 0x5b4 sha256:a559e00c5d076d1c595e299bddd62bab8374cb7e3d1a61be5852dc024516b8e2
+  __TEXT.__unwind_info: 0xc0 sha256:d4d94a3fc189e5389969c29cd22beeb41eada56ff297b9f7dc91bac2f2bd744e
   __DATA_CONST.__auth_got: 0x70 sha256:801edba8c4504d4e3f4758d1823b8f8ea3bdb4f7c402aa8efb50c9bf465918f9
   __DATA_CONST.__got: 0x8 sha256:0db85176963353d81ec32c6394bc7ddf83dcba4a7c36eb294550853c254b96c0
-  __DATA.__data: 0xc8 sha256:f6cbbf1ac6b0b4b9ed1147700a1c171db431d7bc7c19488af636a38801d3efdf
+  __DATA.__data: 0xc8 sha256:30a292c6f0a46546cbeeea1ea257423967ecc489630a84fc7053bf3b52a371d5
   - /usr/lib/libSystem.B.dylib
-  UUID: BC64EAF7-4D81-33CC-A9D8-AB5EE5BD3B74
+  UUID: 73651F7C-57B1-3D00-9A0A-A34431019393
   Functions: 29
   Symbols:   46
   CStrings:  25
Functions:
~ _login_server_plug_init : sha256 7e6073b02846578cf257d1f6387d40f6f70f077025a4fd1787ad2ba459d1f96b -> 6a30ae12e2ffbd63c3f5740c0935dcccfed0827571aee5f4290d32fc3a84c4ae
~ _login_client_plug_init : sha256 d80ac26dbb90b54a3b681bb625f26daa57709f1b46fe6db85c1f8ae5fcad1288 -> 38c9d03285901cf51becc4322e8d90765a39e9f9a2b303142c84f3b4131f651e
~ _login_server_mech_new : sha256 686a917892f0534d3404312bba740f414f72a63a298a8e7d3cd93f42edf87658 -> 2f3989cb1c5d2f6bf0aa7a3de312c89381a21b6390eb74f69807bf50c7047d2a
~ _login_server_mech_step : 628 -> 624
~ _login_client_mech_new : sha256 99b74b15d52e1db936406f838e4aee9cfe05d106ebadc552cd4b070a86fe9e6c -> 2f49a1ca70ab5fed45dfd6050868daf6853120aefbf491a3a33c8b18905c4a8f
~ _login_client_mech_step : sha256 e411dcd21ffff9eca237d609cc3c947d45d1b75f6730ef12d83e556d40fbb917 -> 7df17efd25bf9a41ba1a0f378a36e02e8d3efbc984172e14ff1b964d409f54c4
~ _login_client_mech_dispose : sha256 35ff5e08c749aaba8cad802789539034261cfb87ca9552204f948d13696a5c62 -> 11bfb47f101ec3a85875f7ffdf4498f875f5b83a94e06a48789d11433ad41053
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 f8acf43996cac9003b6c512321ea9f5e0a2a3c20b00b0348e729a347957763df -> d8d5af188296dcd903a35fd03ba3983e6c9860feceb958cddd19f885e149f8cd
~ __plug_strdup : sha256 be61941010f6df850f956ca6f16810c23f6cc1581dad7824042b2db9bd196b1c -> 87c9b61c26d69ebccfd19070faf373d4043cdbca1f5514e9bcd24f9da9006d28
~ __plug_free_string : sha256 6ea852f26805aa6322a71e78190cbba3b5687ddff433662849a93d618f60da00 -> 94127a05224bae8105675b02614e7149377e4d50b3f8eb391ad91c9735eca4df
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 a7aaad87b1d582e7c97af6eda2df9644c42d47c26f93d9ca937e37f3a752e156 -> 243ad2c9d3e0f84cb8833320b4456c2a9a8da9f949a68f06c8363b747166c970
~ __plug_get_password : 372 -> 364
~ __plug_challenge_prompt : sha256 69edbc517d986559199982b4f2324628bb26fb77fb155b12d0a36c97a87b7445 -> f6282100c80e941cd8710f3775a42642b47962d69acde957c572c524afd40bfd
~ __plug_get_realm : sha256 dc1c526ba6f0d998a0436bc06c6443e366ba06db544004b5c23d6d29792ab280 -> 53386cc6723181d7ef00b2b987adc9968da76c7829594335969eae0a27fc4622
~ __plug_make_prompts : sha256 39b8ca970f265d2017d2464fe1a9c469e85bb65ffcea113b0725df483efcbf15 -> f34d96845e2826c344288ea49440296e0fc2d69edb92c23c2b39ae32bb618d62
~ __plug_decode : sha256 2f45e3fc455f8753272d66c8ce262b673248c20d4a933d46759d1f45dce2e0bd -> a5c5dbfccfbec76b7d51fd77966f0f5106ca2e5a70ca633deaf4c6dc04deb9b8
~ __plug_parseuser : sha256 0972465fc79ff1193b8507a7cced65e5b0367ca3e3169ff83e44445a36b8e83d -> 8a9a3c4248bc158909632db1b236c2669379250e1844456aadac4b1e872cb42b
~ __plug_make_fulluser : sha256 e0452004de5d3dfbe1530794f1e1f7de0195b1f9e75cad501a9b3ab9dfbb8175 -> 2cef934c59f51a083ed710e44a74ede7f567781a86017fcef23bbc867669adc4
~ __plug_get_error_message : sha256 022d53d6a9260609d84a5a07597a7b9a1218ad0cc6f250e93872f90bff1abea8 -> 07a797d7ea7e69aedba13293ef7c878394b81e0c4fe3f04311e35ce0d67a3cd2
~ __plug_snprintf_os_info : sha256 aa896a46deb423a3ddb6b309e2e37bfaed00003472b378181e8c74bc76711deb -> 4714d34ae2add6a450189798fd6569af9a4fe957c4759bc7115febcecd421ebe
~ _sasl_client_plug_init : sha256 5faa113d8aaf0ec2e0957790be3db8e55ec9ab561f66251ee1088d757a144f0e -> 6a0106a10acc445ff893e5e20132cb3e6d48017a5c8640463224e8f2add4a47c
~ _sasl_server_plug_init : sha256 58681cdf2a455059706983b5b71dc80db7360bc8ac9c7d4f68d1305cc46a6d2e -> 7119f3f214d223083717eb161c065a4b033490e928802aa494a8d4e4f1c5478a
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/login.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/login.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/login.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/login.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
