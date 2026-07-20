## GSS

> `/System/Library/Frameworks/GSS.framework/Versions/A/GSS`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-725.0.8.0.0
-  __TEXT.__text: 0x4a914
+725.0.10.0.0
+  __TEXT.__text: 0x4a94c
   __TEXT.__const: 0x494
   __TEXT.__cstring: 0x3da0
   __TEXT.__oslogstring: 0xb
Symbols:
+ _asn1_KERB_ERROR_DATA_tag__456
- _asn1_KERB_ERROR_DATA_tag__455
Functions:
~ __gssapi_verify_pad : 256 -> 296
~ _unwrap_des3 : 1972 -> 1988
```
