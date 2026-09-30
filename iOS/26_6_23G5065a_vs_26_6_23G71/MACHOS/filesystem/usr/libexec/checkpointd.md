## checkpointd

> `/usr/libexec/checkpointd`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0x511e0
+  __TEXT.__text: 0x51210
   __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_stubs: 0x320
   __TEXT.__cstring: 0x638
Functions:
~ sub_100000bdc : 5016 -> 5064
```
