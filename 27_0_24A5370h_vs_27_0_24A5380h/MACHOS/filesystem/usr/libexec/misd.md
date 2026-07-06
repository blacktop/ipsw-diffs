## misd

> `/usr/libexec/misd`

```diff

-  __TEXT.__text: 0x21c28
+  __TEXT.__text: 0x21d24
   __TEXT.__auth_stubs: 0x1250
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x39c
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0xb5f4
+  __TEXT.__cstring: 0xb6ba
   __TEXT.__oslogstring: 0x1e
   __TEXT.__objc_methname: 0x915
   __TEXT.__objc_classname: 0x74

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 455
+  Functions: 456
   Symbols:   393
-  CStrings:  1842
+  CStrings:  1846
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
CStrings:
+ "%s proxy prefixes (ND6_IFF_PROXY_PREFIXES) on %s"
+ "%s: %s is not prefix sharing; not enabling proxy prefixes"
+ "%s: mis_ext_if_set_proxy_prefixes, err %d"
+ "%s: mis_ext_if_set_proxy_prefixes, network %s, err %d"
+ "mis_ext_if_set_proxy_prefixes"
- "%s: mis_set_proxy_prefixes, err %d"

```
