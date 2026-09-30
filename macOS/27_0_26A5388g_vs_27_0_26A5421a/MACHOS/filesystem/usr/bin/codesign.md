## codesign

> `/usr/bin/codesign`

### Sections with Same Size but Changed Content

- `__TEXT.__const`

```diff

-135.0.5.0.0
+135.0.6.0.0
   __TEXT.__text: 0x23c00
   __TEXT.__auth_stubs: 0x1680
   __TEXT.__objc_stubs: 0xcc0
```
