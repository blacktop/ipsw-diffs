## com.apple.appkit.xpc.VersionsUIHelper

> `/System/Library/Frameworks/AppKit.framework/Versions/Current/XPCServices/com.apple.appkit.xpc.VersionsUIHelper.xpc/Contents/MacOS/com.apple.appkit.xpc.VersionsUIHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2765.5.0.0.0
-  __TEXT.__text: 0x14cc
-  __TEXT.__auth_stubs: 0x140
+2768.2.1.0.0
+  __TEXT.__text: 0x152c
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x36c
+  __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x1d8
-  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x19e
+  __TEXT.__oslogstring: 0x5c
   __TEXT.__objc_methname: 0x8c7
   __TEXT.__objc_classname: 0xc2
   __TEXT.__objc_methtype: 0x2a0
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__const: 0x70
-  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__auth_got: 0xb8
+  __DATA_CONST.__got: 0xa0
   __DATA.__objc_const: 0x540
   __DATA.__objc_selrefs: 0x3e0
   __DATA.__objc_ivar: 0x1c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 38
-  Symbols:   66
+  Symbols:   68
   CStrings:  200
 
Symbols:
+ __os_log_default
+ __os_log_error_impl
+ _os_log_type_enabled
- _NSLog
Functions:
~ _main : 224 -> 320
CStrings:
+ "caught %{public}@: '%{private}@' with user dictionary %{private}@ and call stack %{public}@"
- "caught %@: '%@' with user dictionary %@ and call stack %@"
```
