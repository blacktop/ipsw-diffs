## accountsd

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Support/accountsd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-1123.0.0.0.0
+1125.0.0.0.0
   __TEXT.__text: 0x780
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_stubs: 0x380

   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__linkguard: 0x1d
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x80

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/Versions/A/AccountsDaemon
-  - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7
-  Symbols:   34
+  Symbols:   33
   CStrings:  41
 
Symbols:
- __linkguard_init
```
