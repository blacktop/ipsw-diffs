## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-  __TEXT.__text: 0x30920
+  __TEXT.__text: 0x308ec
   __TEXT.__objc_methlist: 0x25c
   __TEXT.__cstring: 0x214e
   __TEXT.__const: 0x1e0

   __AUTH_CONST.__objc_const: 0x34f0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0xe20
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0xf78
   __DATA.__data: 0x14b4
   __DATA.__bss: 0x318
-  __DATA_DIRTY.__objc_data: 0xe60
+  __DATA_DIRTY.__objc_data: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Functions:
~ _DomainNameAppendString : 348 -> 352
~ __DNSRecordDataToStringEx2 : 5188 -> 5136
~ __mdns_siphash_with_key_ex : 980 -> 972
~ _mdns_string_builder_append_escaped_ascii_string : 304 -> 308

```
