## libplain.2.so

> `/usr/lib/sasl2/libplain.2.so`

```diff

-  __TEXT.__text: 0x1b34
+  __TEXT.__text: 0x1b48
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__cstring: 0x563
   __TEXT.__unwind_info: 0xc0
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA.__data : content changed
Functions:
~ __plug_find_prompt : 64 -> 48
~ __plug_get_simple : 284 -> 292
~ __plug_get_password : 364 -> 372
~ __plug_challenge_prompt : 288 -> 296
~ __plug_get_realm : 260 -> 268
~ _plain_server_mech_step : 792 -> 796
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plain.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plain.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plain.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plain.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
