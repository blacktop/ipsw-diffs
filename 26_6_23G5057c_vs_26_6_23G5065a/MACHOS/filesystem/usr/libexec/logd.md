## logd

> `/usr/libexec/logd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__os_assumes_log`

```diff

-  __TEXT.__text: 0x270a4
-  __TEXT.__auth_stubs: 0x19c0
+  __TEXT.__text: 0x273c4
+  __TEXT.__auth_stubs: 0x19e0
   __TEXT.__delay_helper: 0x14c
-  __TEXT.__objc_stubs: 0x760
+  __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x488b
-  __TEXT.__objc_methname: 0x4ee
+  __TEXT.__cstring: 0x4a00
+  __TEXT.__objc_methname: 0x51f
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methtype: 0x10
   __TEXT.__unwind_info: 0x6c8
-  __DATA_CONST.__auth_got: 0xce8
-  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_got: 0xcf8
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2110
+  __DATA_CONST.__const: 0x2130
   __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x10

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x120
-  __DATA.__objc_selrefs: 0x1f0
+  __DATA.__objc_selrefs: 0x200
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1cf4
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xeaf8
+  __DATA.__bss: 0xeb08
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
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
-  Functions: 508
-  Symbols:   470
-  CStrings:  610
+  Functions: 509
+  Symbols:   473
+  CStrings:  618
 
Symbols:
+ _CFBooleanGetValue
+ _OBJC_CLASS_$_SecureConfigParameters
+ __os_trace_prefscachedir_path
CStrings:
+ "Failed to check REM status. Enforcing logging privacy for this boot. (errno: %d)"
+ "Failed to create prefscachedir %s"
+ "Failed to load SecureConfigParameters; enforcing logging privacy for this boot. Error %ld - %s: %s"
+ "SecureConfig present but not in REM. No logging privacy enforcement for this boot."
+ "loadContentsAndReturnError:"
+ "logFilteringEnforced"
+ "logFilteringEnforced: %d"
+ "security.mac.amfi.restricted_execution_mode_status"
```
