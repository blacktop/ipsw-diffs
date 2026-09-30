## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-809.0.0.0.1
-  __TEXT.__text: 0xb242c
+813.0.0.0.1
+  __TEXT.__text: 0xb27e8
   __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_stubs: 0xc540
   __TEXT.__objc_methlist: 0x3ddc
   __TEXT.__const: 0x308
   __TEXT.__objc_methname: 0xf392
-  __TEXT.__oslogstring: 0xefa2
+  __TEXT.__oslogstring: 0xefe2
   __TEXT.__objc_classname: 0xc61
   __TEXT.__objc_methtype: 0x2907
-  __TEXT.__gcc_except_tab: 0x4290
-  __TEXT.__cstring: 0xc0bb
+  __TEXT.__gcc_except_tab: 0x4288
+  __TEXT.__cstring: 0xc0d2
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__info_plist: 0x49b
-  __TEXT.__unwind_info: 0x18d0
+  __TEXT.__unwind_info: 0x18d8
   __DATA_CONST.__auth_got: 0xc40
   __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x1ef8
-  __DATA_CONST.__cfstring: 0x79e0
+  __DATA_CONST.__const: 0x1f18
+  __DATA_CONST.__cfstring: 0x7a00
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2069
+  Functions: 2070
   Symbols:   620
-  CStrings:  5884
+  CStrings:  5886
 
CStrings:
+ "+[NSPPrivateAccessTokenCache addOneTimeTokensToCacheForChallenge:tokens:salts:expirationTime:tokenKey:longLivedTokenChallenge:longLivedToken:]"
+ "Cached one-time token from keychain for \"%!@(MISSING)\" has non-matching key, but not expired. Returning token."
+ "Requesting clean exit after daily stats event"
+ "icloud.com.cn"
- "+[NSPPrivateAccessTokenCache addOneTimeTokensToCacheForChallenge:tokens:salts:expirationTime:longLivedTokenChallenge:longLivedToken:]"
- "Cached one-time token from keychain for \"%!@(MISSING)\" has non-matching key, flushing tokens"

```
