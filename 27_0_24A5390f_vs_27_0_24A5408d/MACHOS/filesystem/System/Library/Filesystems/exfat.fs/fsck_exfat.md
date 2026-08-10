## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/fsck_exfat`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-561.0.1.0.0
-  __TEXT.__text: 0xcc08
+561.0.3.0.0
+  __TEXT.__text: 0xcf14
   __TEXT.__auth_stubs: 0x610
   __TEXT.__const: 0x280
   __TEXT.__cstring: 0x35af
   __TEXT.__oslogstring: 0x18
-  __TEXT.__unwind_info: 0x228
-  __DATA_CONST.__const: 0x370
+  __TEXT.__unwind_info: 0x238
+  __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__auth_got: 0x308
   __DATA_CONST.__got: 0x60

   __DATA.__thread_vars: 0x60
   __DATA.__thread_bss: 0x40
   __DATA.__bss: 0xa4
-  __DATA.__common: 0x248
+  __DATA.__common: 0x250
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
-  Functions: 189
+  Functions: 193
   Symbols:   115
   CStrings:  375
 
```
