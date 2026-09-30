## libmdns.dylib

> `/usr/lib/libmdns.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3089.0.0.0.1
-  __TEXT.__text: 0x310b4
+3109.0.0.0.0
+  __TEXT.__text: 0x31164
   __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__cstring: 0x21ce
+  __TEXT.__cstring: 0x21c9
   __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x154
   __TEXT.__oslogstring: 0x38e8
Functions:
~ _DNSMessageToString : 4844 -> 5012
~ __DNSRecordDataToStringEx2 : 5136 -> 5144
CStrings:
+ " ["
+ " key%u"
- " %s%s"
- " key%u=\""
```
