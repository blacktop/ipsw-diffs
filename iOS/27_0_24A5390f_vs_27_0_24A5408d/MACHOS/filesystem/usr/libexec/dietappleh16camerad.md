## dietappleh16camerad

> `/usr/libexec/dietappleh16camerad`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-6.14.1.0.0
-  __TEXT.__text: 0x1ab20
-  __TEXT.__auth_stubs: 0xe90
+6.18.0.0.0
+  __TEXT.__text: 0x1ae30
+  __TEXT.__auth_stubs: 0xed0
   __TEXT.__objc_stubs: 0x4e0
-  __TEXT.__const: 0x15b0
-  __TEXT.__cstring: 0x31d5
+  __TEXT.__const: 0x15c0
+  __TEXT.__cstring: 0x3287
   __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__oslogstring: 0x212f
+  __TEXT.__oslogstring: 0x21af
   __TEXT.__objc_methname: 0x343
-  __TEXT.__unwind_info: 0x530
-  __DATA_CONST.__const: 0x9b28
-  __DATA_CONST.__cfstring: 0x1420
+  __TEXT.__unwind_info: 0x540
+  __DATA_CONST.__const: 0x9b68
+  __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x758
-  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_got: 0x778
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x138
-  __DATA.__data: 0x371bc0
+  __DATA.__data: 0x380bc0
   __DATA.__common: 0x7
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 388
-  Symbols:   284
-  CStrings:  622
+  Functions: 393
+  Symbols:   289
+  CStrings:  629
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ __xpc_type_bool
+ _dispatch_once
+ _xpc_bool_get_value
+ _xpc_connection_copy_entitlement_value
CStrings:
+ "/usr/local/share/firmware/isp/2226_01XX.dat"
+ "/usr/local/share/firmware/isp/2226_02XX.dat"
+ "6.18"
+ "Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n"
+ "EnforceClientEntitlement"
+ "Rejecting XPC peer missing %{public}s (pid %{private}d)\n"
+ "com.apple.appleh16camerad"
+ "com.apple.private.appleh16camerad.client"
- "6.14.1"
```
