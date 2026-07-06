## libmrc.dylib

> `/usr/lib/libmrc.dylib`

```diff

-  __TEXT.__text: 0x6428
+  __TEXT.__text: 0x6424
   __TEXT.__objc_methlist: 0x14c
   __TEXT.__cstring: 0x70f
   __TEXT.__const: 0x68

   __AUTH_CONST.__const: 0x788
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x320
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0x460
+  __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
Functions:
~ __mdns_siphash_with_key_ex : 980 -> 972
~ _DomainNameFromString : 296 -> 300

```
