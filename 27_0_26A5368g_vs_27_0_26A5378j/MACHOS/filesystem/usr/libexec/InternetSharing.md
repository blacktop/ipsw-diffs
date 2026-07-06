## InternetSharing

> `/usr/libexec/InternetSharing`

```diff

-  __TEXT.__text: 0x1bd4c
+  __TEXT.__text: 0x1be48
   __TEXT.__auth_stubs: 0x10c0
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x7f20
+  __TEXT.__cstring: 0x7fe6
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0x3f0
   __DATA_CONST.__const: 0x510

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
-  Functions: 340
+  Functions: 341
   Symbols:   364
-  CStrings:  1198
+  CStrings:  1202
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
CStrings:
+ "%s proxy prefixes (ND6_IFF_PROXY_PREFIXES) on %s"
+ "%s: %s is not prefix sharing; not enabling proxy prefixes"
+ "%s: mis_ext_if_set_proxy_prefixes, err %d"
+ "%s: mis_ext_if_set_proxy_prefixes, network %s, err %d"
+ "mis_ext_if_set_proxy_prefixes"
- "%s: mis_set_proxy_prefixes, err %d"

```
