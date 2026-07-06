## mschapv2.so

> `/usr/lib/sasl2/mschapv2.so`

```diff

-  __TEXT.__text: 0x24c0
+  __TEXT.__text: 0x24fc
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x6b6
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _chap_server_mech_step : 1392 -> 1388
~ _chap_client_mech_step : 1356 -> 1408
~ _ChapMS2 : 532 -> 528
~ __plug_find_prompt : 64 -> 48
~ __plug_get_simple : 256 -> 264
~ __plug_get_password : 360 -> 368
~ __plug_challenge_prompt : 284 -> 292
~ __plug_get_realm : 256 -> 264
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.T9jXte/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.T9jXte/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.T9jXte/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.T9jXte/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
