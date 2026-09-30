## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/Contents/Resources/fsck_exfat`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-561.0.1.0.0
-  __TEXT.__text: 0xcba0
+561.0.3.0.0
+  __TEXT.__text: 0xcf48
   __TEXT.__auth_stubs: 0x620
   __TEXT.__const: 0x288
   __TEXT.__cstring: 0x3532
   __TEXT.__oslogstring: 0x18
-  __TEXT.__unwind_info: 0x228
-  __DATA_CONST.__const: 0x390
+  __TEXT.__unwind_info: 0x238
+  __DATA_CONST.__const: 0x420
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x60

   __DATA.__thread_vars: 0x60
   __DATA.__thread_bss: 0x40
   __DATA.__bss: 0xa4
-  __DATA.__common: 0x248
+  __DATA.__common: 0x250
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
-  Functions: 195
+  Functions: 201
   Symbols:   116
   CStrings:  373
 
```
