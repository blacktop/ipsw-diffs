## iperf3-darwin

> `/usr/bin/iperf3-darwin`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

 135.0.0.0.0
-  __TEXT.__text: 0x1be2c
+  __TEXT.__text: 0x1be30
   __TEXT.__auth_stubs: 0x11e0
   __TEXT.__cstring: 0x4567
   __TEXT.__const: 0x4040

   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__data: 0xaa8
-  __DATA.__bss: 0xc30
+  __DATA.__bss: 0xc38
   __DATA.__common: 0x430
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
Functions:
~ sub_100011e28 : 332 -> 336
```
