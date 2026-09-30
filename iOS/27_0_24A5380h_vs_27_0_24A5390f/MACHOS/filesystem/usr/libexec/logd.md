## logd

> `/usr/libexec/logd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__os_assumes_log`

```diff

-1965.0.0.0.0
-  __TEXT.__text: 0x2737c
-  __TEXT.__auth_stubs: 0x1b90
-  __TEXT.__objc_stubs: 0x5e0
+1966.0.6.0.0
+  __TEXT.__text: 0x27694
+  __TEXT.__auth_stubs: 0x1bc0
+  __TEXT.__objc_stubs: 0x640
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x4895
-  __TEXT.__objc_methname: 0x3e2
+  __TEXT.__cstring: 0x4a0a
+  __TEXT.__objc_methname: 0x428
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x690
-  __DATA_CONST.__const: 0x2378
+  __TEXT.__unwind_info: 0x698
+  __DATA_CONST.__const: 0x2398
   __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0xdd0
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__auth_got: 0xde8
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x120
-  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_selrefs: 0x1a8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1cf5
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xeb68
+  __DATA.__bss: 0xeb78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/SecureConfigDB.framework/SecureConfigDB
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 514
-  Symbols:   496
-  CStrings:  624
+  Functions: 515
+  Symbols:   500
+  CStrings:  633
 
Symbols:
+ _CFBooleanGetValue
+ _OBJC_CLASS_$_SecureConfigParameters
+ __os_trace_prefscachedir_path
+ _objc_opt_class
CStrings:
+ "Failed to check REM status. Enforcing logging privacy for this boot. (errno: %d)"
+ "Failed to create prefscachedir %s"
+ "Failed to load SecureConfigParameters; enforcing logging privacy for this boot. Error %ld - %s: %s"
+ "SecureConfig present but not in REM. No logging privacy enforcement for this boot."
+ "loadContentsAndReturnError:"
+ "localizedDescription"
+ "logFilteringEnforced"
+ "logFilteringEnforced: %d"
+ "security.mac.amfi.restricted_execution_mode_status"
```
