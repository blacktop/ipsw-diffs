## Automator

> `/System/Applications/Automator.app/Contents/MacOS/Automator`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__data`

```diff

-540.0.0.0.0
+541.0.0.0.0
   __TEXT.__text: 0x2365c
   __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_stubs: 0x8600
   __TEXT.__objc_methlist: 0x2d44
   __TEXT.__const: 0xb0
   __TEXT.__objc_methname: 0xa049
-  __TEXT.__cstring: 0x1f4c
-  __TEXT.__ustring: 0x36
+  __TEXT.__cstring: 0x1f15
+  __TEXT.__ustring: 0x9a
   __TEXT.__objc_classname: 0x460
   __TEXT.__objc_methtype: 0x1cc3
   __TEXT.__oslogstring: 0xba
CStrings:
+ "Your changes will be lost if you don’t save them."
- "Your changes will be lost if you don\\U2019t save them."
```
