## com.apple.FontServices.FontProviderLoader

> `/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/com.apple.FontServices.FontProviderLoader.xpc/com.apple.FontServices.FontProviderLoader`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-169.0.0.0.0
-  __TEXT.__text: 0x2560
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0x9c0
+173.0.0.0.0
+  __TEXT.__text: 0x2eec
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0xa20
   __TEXT.__objc_methlist: 0x428
   __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x603
   __TEXT.__objc_classname: 0xc5
-  __TEXT.__objc_methname: 0xd6b
+  __TEXT.__objc_methname: 0xd8b
   __TEXT.__objc_methtype: 0x3e5
-  __TEXT.__cstring: 0x491
-  __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__unwind_info: 0x120
   __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x100
   __DATA.__objc_const: 0x578
-  __DATA.__objc_selrefs: 0x460
+  __DATA.__objc_selrefs: 0x470
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1e0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 37
-  Symbols:   129
-  CStrings:  244
+  Functions: 39
+  Symbols:   132
+  CStrings:  258
 
Symbols:
+ _FontProviderAppInfoIsWellFormed
+ _FontProviderFontsInfoIsWellFormed
+ _memchr
CStrings:
+ "FontProviderSubscriptionSupportInfo"
+ "actualPath"
+ "expire"
+ "length"
+ "objectForKeyedSubscript:"
+ "registerFonts received malformed appInfo."
+ "registerFonts received malformed fontsInfo."
+ "registeredFontsInfo received malformed appInfo; dropping the connection."
+ "scheme"
+ "test"
+ "unregisterFonts received malformed appInfo; dropping the connection."
+ "updateAppInfo received malformed appInfo; dropping the connection."
+ "url"
+ "warn"
```
