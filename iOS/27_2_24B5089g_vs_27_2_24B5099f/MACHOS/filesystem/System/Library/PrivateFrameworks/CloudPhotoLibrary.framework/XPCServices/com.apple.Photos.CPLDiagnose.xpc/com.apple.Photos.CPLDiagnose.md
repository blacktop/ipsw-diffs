## com.apple.Photos.CPLDiagnose

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0x1d6ac
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_stubs: 0x4300
-  __TEXT.__objc_methlist: 0x1f40
+916.51.202.0.0
+  __TEXT.__text: 0x1d8cc
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_stubs: 0x4380
+  __TEXT.__objc_methlist: 0x1f50
   __TEXT.__const: 0xa0
   __TEXT.__objc_classname: 0x29b
-  __TEXT.__objc_methname: 0x4e85
+  __TEXT.__objc_methname: 0x4eed
   __TEXT.__objc_methtype: 0xaca
-  __TEXT.__oslogstring: 0x6e8
-  __TEXT.__cstring: 0x6fc7
-  __TEXT.__gcc_except_tab: 0x3b4
-  __TEXT.__unwind_info: 0x8f8
-  __DATA_CONST.__const: 0xc38
+  __TEXT.__oslogstring: 0x6f7
+  __TEXT.__cstring: 0x700e
+  __TEXT.__gcc_except_tab: 0x3f0
+  __TEXT.__unwind_info: 0x900
+  __DATA_CONST.__const: 0xc60
   __DATA_CONST.__cfstring: 0x6260
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA_CONST.__auth_got: 0x798
+  __DATA_CONST.__auth_got: 0x7c0
   __DATA_CONST.__got: 0x300
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x2b60
-  __DATA.__objc_selrefs: 0x1440
-  __DATA.__objc_ivar: 0x210
+  __DATA.__objc_const: 0x2b80
+  __DATA.__objc_selrefs: 0x1460
+  __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x558
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 703
-  Symbols:   391
-  CStrings:  2021
+  Functions: 705
+  Symbols:   396
+  CStrings:  2028
 
Symbols:
+ _objc_retain_x27
+ _objc_retain_x28
+ _sscanf
+ _tcgetattr
+ _tcsetattr
CStrings:
+ "%s options: %@"
+ "-[CPLDiagnoseService runDiagnoseWithOptions:replyHandler:]"
+ "_savedColumn"
+ "currentColumn"
+ "startAccessingSecurityScopedResource"
+ "stopAccessingSecurityScopedResource"
+ "url"
```
