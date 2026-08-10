## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-725.0.10.0.0
-  __TEXT.__text: 0x27fd0
+725.0.12.0.0
+  __TEXT.__text: 0x27fdc
   __TEXT.__const: 0x44a
   __TEXT.__cstring: 0x3b55
   __TEXT.__oslogstring: 0xb
Functions:
~ __gssapi_unwrap_cfx_iov : 1420 -> 1432
```
