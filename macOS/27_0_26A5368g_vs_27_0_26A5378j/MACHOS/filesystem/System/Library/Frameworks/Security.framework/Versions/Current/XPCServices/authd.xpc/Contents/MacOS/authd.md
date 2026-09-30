## authd

> `/System/Library/Frameworks/Security.framework/Versions/Current/XPCServices/authd.xpc/Contents/MacOS/authd`

```diff

-  __TEXT.__text: 0x27b70
-  __TEXT.__auth_stubs: 0x13d0
+  __TEXT.__text: 0x27e44
+  __TEXT.__auth_stubs: 0x13e0
   __TEXT.__lazy_helpers: 0x63c
   __TEXT.__objc_stubs: 0xda0
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0xb00
-  __TEXT.__cstring: 0x2f4b
-  __TEXT.__oslogstring: 0x4f95
+  __TEXT.__const: 0xb20
+  __TEXT.__cstring: 0x2f86
+  __TEXT.__oslogstring: 0x5056
   __TEXT.__dlopen_cstrs: 0x5d
   __TEXT.__gcc_except_tab: 0xe78
   __TEXT.__objc_methname: 0xace

   __TEXT.__objc_methtype: 0x140
   __TEXT.__unwind_info: 0x648
   __DATA_CONST.__const: 0x23a0
-  __DATA_CONST.__cfstring: 0x1180
+  __DATA_CONST.__cfstring: 0x11a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x9f8
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__auth_got: 0xa00
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x230
   __DATA.__objc_selrefs: 0x378
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x50
   __DATA.__lazy_load_got: 0x98
-  __DATA.__data: 0x98
+  __DATA.__data: 0xa0
   __DATA.__bss: 0x390
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 472
-  Symbols:   403
-  CStrings:  1231
+  Functions: 477
+  Symbols:   404
+  CStrings:  1238
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _CFPreferencesGetAppBooleanValue
CStrings:
+ "PluginFallbackEnabled"
+ "engine %llu: plist rule for system.login.console not found"
+ "engine %llu: plugin unavailable during login evaluation, retrying with plist"
+ "engine %llu: retrying %{public}s with default plist rule"
+ "loginwindow:login"
+ "plugin-unavailable"

```
