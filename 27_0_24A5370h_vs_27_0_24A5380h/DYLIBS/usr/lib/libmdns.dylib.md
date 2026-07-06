## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-  __TEXT.__text: 0x310e8
+  __TEXT.__text: 0x310b4
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__cstring: 0x21ce
   __TEXT.__const: 0x1d0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x0
+  __DATA_CONST.__got: 0x2f0
   __AUTH_CONST.__const: 0x1380
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x3580
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0xf18
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0xfa0
   __DATA.__data: 0x14b4
   __DATA.__bss: 0x338
-  __DATA_DIRTY.__objc_data: 0xeb0
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
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
