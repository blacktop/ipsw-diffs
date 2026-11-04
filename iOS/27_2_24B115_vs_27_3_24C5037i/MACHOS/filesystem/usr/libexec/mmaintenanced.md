## mmaintenanced

> `/usr/libexec/mmaintenanced`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-233.40.4.0.0
+233.52.2.0.0
   __TEXT.__text: 0x2696c
   __TEXT.__auth_stubs: 0x1580
   __TEXT.__objc_stubs: 0x540
CStrings:
+ "com.apple.driver.AppleH?[0-9]*Camera(:?Interface)?.NonPersistent.*"
- "com.apple.driver.AppleH[0-9]+CameraInterface.NonPersistent.*"
```
