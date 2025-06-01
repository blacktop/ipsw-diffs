## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-136.0.0.0.0
-  __TEXT.__text: 0x13d48
+136.120.6.0.0
+  __TEXT.__text: 0x13bf0
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__init_offsets: 0x4
   __TEXT.__oslogstring: 0x193b
-  __TEXT.__cstring: 0x10a3
+  __TEXT.__cstring: 0x10b0
   __TEXT.__const: 0x4d8
-  __TEXT.__gcc_except_tab: 0x73c
-  __TEXT.__unwind_info: 0x6e0
+  __TEXT.__gcc_except_tab: 0x6f0
+  __TEXT.__unwind_info: 0x6dc
   __TEXT.__eh_frame: 0x88
   __DATA_CONST.__auth_got: 0x570
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0xae0
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0xa90
   __DATA_CONST.__cfstring: 0x60
-  __DATA.__data: 0x188
-  __DATA.__common: 0x8c
-  __DATA.__bss: 0x20
+  __DATA.__data: 0x198
+  __DATA.__common: 0x88
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 71457D1A-3DEF-303E-BF1C-CF49876076A9
-  Functions: 448
-  Symbols:   225
-  CStrings:  327
+  UUID: 29F70A00-4547-3898-A237-641096409489
+  Functions: 447
+  Symbols:   224
+  CStrings:  329
 
Symbols:
+ ___cxa_guard_acquire
+ ___cxa_guard_release
- __Block_object_dispose
- _vm_page_size
- _xpc_copy
CStrings:
+ "34"
+ "EXCLAVES"
+ "SELECT COUNT(*) FROM ecc_errors_v2 WHERE correctable = 0 AND (addr >> ?) = ?;"
- "SELECT COUNT(*) FROM ecc_errors_v2 WHERE correctable = 0 AND (addr / ?) = ?;"

```
