## libntlm.so

> `/usr/lib/sasl2/libntlm.so`

```diff

-  __TEXT.__text: 0x3df0
+  __TEXT.__text: 0x3de8
   __TEXT.__auth_stubs: 0x200
   __TEXT.__cstring: 0xc11
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x10
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ __plug_find_prompt : 64 -> 48
~ __plug_get_simple : 284 -> 292
~ __plug_get_password : 364 -> 372
~ __plug_challenge_prompt : 288 -> 296
~ __plug_get_realm : 260 -> 268
~ _P16_nt : 212 -> 204
~ _P16_lm : 208 -> 192
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/ntlm.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/ntlm.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
