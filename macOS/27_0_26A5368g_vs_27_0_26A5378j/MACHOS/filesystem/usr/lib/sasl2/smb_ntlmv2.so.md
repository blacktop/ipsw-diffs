## smb_ntlmv2.so

> `/usr/lib/sasl2/smb_ntlmv2.so`

```diff

-  __TEXT.__text: 0x206c
+  __TEXT.__text: 0x20ac
   __TEXT.__auth_stubs: 0x190
   __TEXT.__cstring: 0x6fb
   __TEXT.__unwind_info: 0xc0
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _ntlmv2_server_mech_step : 1772 -> 1768
~ _ntlmv2_client_mech_step : 1332 -> 1384
~ __plug_find_prompt : 64 -> 48
~ __plug_get_simple : 256 -> 264
~ __plug_get_password : 360 -> 368
~ __plug_challenge_prompt : 284 -> 292
~ __plug_get_realm : 256 -> 264
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.T9jXte/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.T9jXte/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.T9jXte/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.T9jXte/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
