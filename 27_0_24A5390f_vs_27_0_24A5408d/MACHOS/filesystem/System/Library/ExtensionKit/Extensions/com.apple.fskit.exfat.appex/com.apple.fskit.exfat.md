## com.apple.fskit.exfat

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-561.0.1.0.0
-  __TEXT.__text: 0x12434
+561.0.3.0.0
+  __TEXT.__text: 0x1287c
   __TEXT.__auth_stubs: 0x9c0
   __TEXT.__objc_stubs: 0x800
   __TEXT.__objc_methlist: 0x204
   __TEXT.__const: 0x4d03
-  __TEXT.__cstring: 0x3e5c
-  __TEXT.__oslogstring: 0x5bc
-  __TEXT.__gcc_except_tab: 0x374
+  __TEXT.__cstring: 0x3e6b
+  __TEXT.__oslogstring: 0x5f3
+  __TEXT.__gcc_except_tab: 0x39c
   __TEXT.__objc_methname: 0x741
   __TEXT.__objc_classname: 0x5f
   __TEXT.__objc_methtype: 0x233
-  __TEXT.__unwind_info: 0x2f8
-  __DATA_CONST.__const: 0x370
+  __TEXT.__unwind_info: 0x310
+  __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA.__thread_vars: 0x60
   __DATA.__thread_bss: 0x40
   __DATA.__bss: 0xa4
-  __DATA.__common: 0x2b0
+  __DATA.__common: 0x2b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 277
-  Symbols:   414
-  CStrings:  577
+  Functions: 284
+  Symbols:   416
+  CStrings:  579
 
Symbols:
+ _fsckRunGuarded
+ _fsck_set_run_guarded_func
CStrings:
+ "%s: caught exception on fsck worker thread, error = %d"
+ "fsckRunGuarded"
```
