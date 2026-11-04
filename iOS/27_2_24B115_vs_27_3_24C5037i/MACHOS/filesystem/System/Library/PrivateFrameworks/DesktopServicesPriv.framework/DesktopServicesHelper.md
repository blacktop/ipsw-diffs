## DesktopServicesHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`

```diff

-1857.1.8.0.0
-  __TEXT.__text: 0x830e0
-  __TEXT.__auth_stubs: 0x1910
-  __TEXT.__objc_stubs: 0x1f00
+1857.2.6.0.0
+  __TEXT.__text: 0x86464
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__objc_stubs: 0x1f40
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x924
-  __TEXT.__gcc_except_tab: 0xaa04
-  __TEXT.__const: 0x3460
-  __TEXT.__objc_methname: 0x1e46
-  __TEXT.__objc_classname: 0x14c
-  __TEXT.__cstring: 0x27bc
-  __TEXT.__objc_methtype: 0x1456
-  __TEXT.__oslogstring: 0x3a11
+  __TEXT.__gcc_except_tab: 0xadd4
+  __TEXT.__const: 0x34b0
+  __TEXT.__cstring: 0x2890
+  __TEXT.__oslogstring: 0x3a95
   __TEXT.__ustring: 0x1a
-  __TEXT.__unwind_info: 0x3e40
-  __DATA_CONST.__const: 0x2bd0
-  __DATA_CONST.__cfstring: 0x1440
+  __TEXT.__objc_methname: 0x1e63
+  __TEXT.__objc_classname: 0x14c
+  __TEXT.__objc_methtype: 0x1456
+  __TEXT.__unwind_info: 0x4080
+  __DATA_CONST.__const: 0x2c38
+  __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xc98
-  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__auth_got: 0xca0
+  __DATA_CONST.__got: 0x520
   __DATA.__objc_const: 0xfe0
-  __DATA.__objc_selrefs: 0x9b8
+  __DATA.__objc_selrefs: 0x9c8
   __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x320
-  __DATA.__data: 0x5a1
+  __DATA.__data: 0x5a8
+  __DATA.__thread_vars: 0x30
+  __DATA.__thread_bss: 0x10
   __DATA.__common: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2253
-  Symbols:   579
-  CStrings:  1237
+  Functions: 2309
+  Symbols:   582
+  CStrings:  1243
 
Symbols:
+ _NSURLNameKey
+ ___cxa_demangle
+ __tlv_bootstrap
CStrings:
+ "%{public}s failed to find key in message: %{public}s"
+ "%{public}s failed to unarchive any FPSandboxingURLWrappers from message: %{public}s"
+ "/Developer/Applications"
+ "AccessDeniedFull"
+ "Found two progress objects with the same UUID.\t\n Known: %{public}@\n\n\t new: %{public}@"
+ "MakeWrappedURLs"
+ "OperationFailed"
+ "TCFURLInfo::TranslateCFError -- status: %{public}s\n\t CFError: %{public}@\n\t URL: %{public}@\n\t Backtrace:\n%{public}s"
+ "TCFURLInfo::TranslateRawPOSIXError %{errno}d -> %{public}s, path: %{public}@\n%{public}s"
+ "[ \\t]*([0-9]+)[ \\t]+([0-9a-zA-Z._?+]+)[ \\t]+(0x[0-9a-f]+)[ \\t]+((.|\\n)*)"
+ "[ \\t]*([0-9]+)[ \\t]+([0-9a-zA-Z._?+]+)[ \\t]+(0x[0-9a-f]+)[ \\t]+([_$a-zA-Z][_$a-zA-Z0-9]*)((.|\\n)*)"
+ "hasSuffix:"
+ "substringToIndex:"
+ "writer about to write data for %{public}s"
- "0@0"
- "2!0"
- "AccessDenied"
- "CopyFailed"
- "Found two progress objects with the same UUID.\t\n Knonwn: %{public}@\n\n\t new: %{public}@"
- "TCFURLInfo::TranslateCFError -- status: %{public}s\n\t CFError: %{public}@\n\t URL: %{public}@\n\t Backtrace:\n%{public}@"
- "TCFURLInfo::TranslateRawPOSIXError %{errno}d -> %{public}s, path: %{public}@\n%{public}@"
- "writer about to write data for for %{public}s"
```
