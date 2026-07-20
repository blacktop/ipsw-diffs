## LocalAuthenticationUI

> `/System/Library/PrivateFrameworks/LocalAuthenticationUI.framework/Versions/A/LocalAuthenticationUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-2319.0.33.0.1
-  __TEXT.__text: 0x1cf88
-  __TEXT.__objc_methlist: 0x2188
+2319.0.46.0.0
+  __TEXT.__text: 0x1d1cc
+  __TEXT.__objc_methlist: 0x2190
   __TEXT.__const: 0xc10
   __TEXT.__gcc_except_tab: 0x8a4
   __TEXT.__cstring: 0xf76
-  __TEXT.__oslogstring: 0x1038
+  __TEXT.__oslogstring: 0x1069
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0x9d8
+  __TEXT.__unwind_info: 0x9e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a48
+  __DATA_CONST.__objc_selrefs: 0x1a50
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x428
   __AUTH_CONST.__const: 0xa10
   __AUTH_CONST.__cfstring: 0x7e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 746
-  Symbols:   2131
-  CStrings:  239
+  Functions: 748
+  Symbols:   2134
+  CStrings:  241
 
Symbols:
+ +[LAUIUserPasswordViewController requestViewController:connectionHandler:]
+ -[LAUIUserPasswordViewController viewDidAppear]
+ __74+[LAUIUserPasswordViewController requestViewController:connectionHandler:]_block_invoke
+ ___74+[LAUIUserPasswordViewController requestViewController:connectionHandler:]_block_invoke
+ _objc_msgSend$dispatchSyncOnMain:
- -[LAUIUserPasswordViewController viewWillLayout]
- ___77+[LAUIUserPasswordViewController requestViewControllerWithConnectionHandler:]_block_invoke_2
CStrings:
+ "%@ did appear with height %.1f"
+ "%@ view requested"
```
