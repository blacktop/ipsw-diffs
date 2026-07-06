## srp.so

> `/usr/lib/sasl2/srp.so`

```diff

-  __TEXT.__text: 0x4a88
+  __TEXT.__text: 0x4a90
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__cstring: 0x12d8
   __TEXT.__const: 0x602
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ __plug_find_prompt : 64 -> 48
~ __plug_get_simple : 284 -> 292
~ __plug_get_password : 364 -> 372
~ __plug_challenge_prompt : 288 -> 296
~ __plug_get_realm : 260 -> 268
~ _srp_server_plug_init : 444 -> 424
~ _srp_generate_authdata_dict : 764 -> 756
~ _generate_N_and_g : 196 -> 192
~ _OptionsToString : 1052 -> 1028
~ _ParseOptions : 1128 -> 1152
~ _SetMDA : 132 -> 140
~ _LayerInit : 520 -> 528
~ _srp_client_mech_step : 2404 -> 2420
~ _CreateClientOpts : 444 -> 436
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/srp.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/srp.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/srp.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/srp.c near line %d"

```
