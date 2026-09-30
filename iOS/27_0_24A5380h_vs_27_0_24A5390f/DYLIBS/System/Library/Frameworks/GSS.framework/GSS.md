## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-725.0.8.0.0
+725.0.10.0.0
   __TEXT.__text: 0x27fd0
   __TEXT.__const: 0x44a
   __TEXT.__cstring: 0x3b55
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x738
+  __TEXT.__unwind_info: 0x740
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1378
   __DATA_CONST.__got: 0x0
Symbols:
+ _asn1_KERB_ERROR_DATA_tag__456
- _asn1_KERB_ERROR_DATA_tag__455
Functions:
~ __gssapi_verify_pad : 76 -> 96
~ __gsskrb5_unwrap : 1372 -> 1352
```
