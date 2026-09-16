## accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-1123.0.0.0.0
+1125.0.0.0.0
   __TEXT.__text: 0x468
   __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x300

   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__linkguard: 0x1d
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x58
   __DATA.__objc_selrefs: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
-  - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4
-  Symbols:   40
+  Symbols:   39
   CStrings:  34
 
Symbols:
- __linkguard_init
```
