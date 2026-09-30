## liblog_mdns.dylib

> `/usr/lib/log/liblog_mdns.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`

```diff

-3089.0.0.0.1
-  __TEXT.__text: 0x58f4
+3109.0.0.0.0
+  __TEXT.__text: 0x5950
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__cstring: 0xdbb
+  __TEXT.__cstring: 0xdb4
   __TEXT.__const: 0x20
   __TEXT.__unwind_info: 0x150
   __TEXT.__objc_stubs: 0x0

   __AUTH_CONST.__cfstring: 0x5c0
   __AUTH_CONST.__objc_const: 0x2f8
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x38
+  __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libobjc.A.dylib
   Functions: 84
   Symbols:   191
-  CStrings:  381
+  CStrings:  380
 
Functions:
~ __DNSRecordDataToStringEx2 : 5016 -> 5064
~ __log_mdns_format_dns_message_ex : 4028 -> 4072
CStrings:
+ " ["
+ " key%u"
- " %s%s"
- " key%u=\""
- "["
```
