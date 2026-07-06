## libsasl2.2.dylib

> `/usr/lib/libsasl2.2.dylib`

```diff

-  __TEXT.__text: 0xf420
+  __TEXT.__text: 0xf3e0
   __TEXT.__cstring: 0x24f5
   __TEXT.__const: 0xd8
-  __TEXT.__unwind_info: 0x300
+  __TEXT.__unwind_info: 0x308
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x198
   __DATA_CONST.__got: 0x0
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ __sasl_find_getpath_callback : 68 -> 52
~ __sasl_find_verifyfile_callback : 68 -> 52
~ __sasl_load_plugins : 796 -> 804
~ __sasl_getcallback : 552 -> 568
~ __sasl_conn_getopt : 212 -> 192
~ __sasl_global_getopt : 200 -> 192
~ _sasl_config_getstring : 144 -> 156
~ __plug_find_prompt : 64 -> 48
~ __plug_get_simple : 284 -> 292
~ __plug_get_password : 364 -> 372
~ __plug_challenge_prompt : 288 -> 296
~ __plug_get_realm : 260 -> 268
~ _parse_mechlist_file : 520 -> 528
~ __sasl_checkpass : 652 -> 660
~ _sasl_user_exists : 588 -> 600
~ _grab_field : 248 -> 268
~ _sasl_config_init : 828 -> 800
~ __sasl_find_getconfpath_callback : 68 -> 52
~ _authdaemon_verify_password : 980 -> 964
~ _prop_getnames : 188 -> 172
~ _prop_erase : 148 -> 156
~ _prop_format : 280 -> 272
~ _prop_set : 844 -> 840
~ __sasl_auxprop_lookup : 712 -> 708
~ _sasl_auxprop_store : 744 -> 728
~ __sasl_load_plugins_alt : 792 -> 788
CStrings:
+ "Internal Error %d in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/client.c near line %d"
+ "Internal Error %d in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/common.c near line %d"
+ "Internal Error %d in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/server.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/client.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/common.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/server.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/auxprop.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/checkpw.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/client.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/common.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VB4Q1y/Sources/passwordserver_sasl/cyrus_sasl/lib/server.c near line %d"
- "Internal Error %d in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/client.c near line %d"
- "Internal Error %d in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/common.c near line %d"
- "Internal Error %d in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/server.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/client.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/server.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/auxprop.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/checkpw.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/client.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/common.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/lib/server.c near line %d"

```
