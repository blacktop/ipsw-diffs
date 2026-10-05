## mDNSResponder

> `/usr/sbin/mDNSResponder`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3111.40.42.0.0
-  __TEXT.__text: 0x10a200
+3111.40.45.0.0
+  __TEXT.__text: 0x10a1f8
   __TEXT.__auth_stubs: 0x2fc0
   __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x694
Functions:
~ _BuildQuestion : 680 -> 672
CStrings:
+ "mDNSResponder-3111.40.45"
- "mDNSResponder-3111.40.42"
```
