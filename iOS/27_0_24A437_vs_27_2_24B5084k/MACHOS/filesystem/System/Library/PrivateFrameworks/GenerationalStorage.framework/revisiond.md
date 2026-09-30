## revisiond

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-405.0.0.0.1
-  __TEXT.__text: 0x28a98
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0x3420
+411.0.0.0.0
+  __TEXT.__text: 0x28af0
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_stubs: 0x3440
   __TEXT.__objc_methlist: 0x136c
   __TEXT.__const: 0x250
   __TEXT.__gcc_except_tab: 0x544
-  __TEXT.__cstring: 0x5268
-  __TEXT.__objc_methname: 0x3add
+  __TEXT.__cstring: 0x525e
+  __TEXT.__objc_methname: 0x3b2a
   __TEXT.__oslogstring: 0x2a8a
   __TEXT.__objc_classname: 0x188
   __TEXT.__objc_methtype: 0x1333
-  __TEXT.__unwind_info: 0xdb0
+  __TEXT.__unwind_info: 0xdb8
   __DATA_CONST.__const: 0x1030
   __DATA_CONST.__cfstring: 0x2720
   __DATA_CONST.__objc_classlist: 0x78

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x7b0
+  __DATA_CONST.__auth_got: 0x798
   __DATA_CONST.__got: 0x2a0
   __DATA.__objc_const: 0x2e80
-  __DATA.__objc_selrefs: 0x1030
+  __DATA.__objc_selrefs: 0x1038
   __DATA.__objc_ivar: 0x1ac
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x490

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 871
-  Symbols:   339
+  Functions: 872
+  Symbols:   336
   CStrings:  1571
 
Symbols:
- _objc_release_x3
- _snprintf
- _unlink
CStrings:
+ "\"%s\" is not owned by the caller"
+ "T@\"NSNumber\",&,N,V_doArchiveWithOwnerUID"
+ "_doArchiveWithOwnerUID"
+ "doArchiveWithOwnerUID"
+ "gsarchive-XXXXXXXX"
+ "setDoArchiveWithOwnerUID:"
+ "unsignedIntValue"
- "%s_XXXXXX"
- "TB,N,V_doArchive"
- "_doArchive"
- "doArchive"
- "setDoArchive:"
- "stat(%s) failed"
- "temporary path \"%s_XXXXXX\" too long"
```
