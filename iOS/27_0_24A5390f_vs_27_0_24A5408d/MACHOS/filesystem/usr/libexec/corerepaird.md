## corerepaird

> `/usr/libexec/corerepaird`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1307.0.46.0.0
+1307.2.1.0.0
   __TEXT.__text: 0x127c
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_stubs: 0x380

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit
+  - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
```
