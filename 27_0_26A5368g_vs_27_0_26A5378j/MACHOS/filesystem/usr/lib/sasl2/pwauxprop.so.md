## pwauxprop.so

> `/usr/lib/sasl2/pwauxprop.so`

```diff

-  __TEXT.__text: 0x14f0
+  __TEXT.__text: 0x14fc
   __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_stubs: 0x20
   __TEXT.__cstring: 0x3f2
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA.__data : content changed
Functions:
~ __plug_find_prompt : 64 -> 48
~ __plug_get_simple : 256 -> 264
~ __plug_get_password : 360 -> 368
~ __plug_challenge_prompt : 284 -> 292
~ __plug_get_realm : 256 -> 264
~ _pwserver_auxprop_lookup : 724 -> 716
~ _authfile_getdata : 508 -> 512
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.19fG9U/Sources/passwordserver/plugin_common.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.19fG9U/Sources/passwordserver/pwauxprop.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.19fG9U/Sources/passwordserver/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.19fG9U/Sources/passwordserver/pwauxprop.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VffEvi/Sources/passwordserver/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VffEvi/Sources/passwordserver/pwauxprop.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VffEvi/Sources/passwordserver/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VffEvi/Sources/passwordserver/pwauxprop.c near line %d"

```
