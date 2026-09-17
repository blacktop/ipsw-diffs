## avbanalyse

> `/usr/bin/avbanalyse`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`

```diff

-1500.16.0.0.0
+1510.1.0.0.0
   __TEXT.__text: 0x18460
   __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_stubs: 0x2760
   __TEXT.__objc_methlist: 0x23f4
   __TEXT.__gcc_except_tab: 0x1094
   __TEXT.__objc_methname: 0x3f89
-  __TEXT.__cstring: 0x561e
+  __TEXT.__cstring: 0x561d
   __TEXT.__objc_classname: 0x6e4
   __TEXT.__objc_methtype: 0x320
   __TEXT.__const: 0x108
CStrings:
+ "1510.1"
- "1500.16"
```
