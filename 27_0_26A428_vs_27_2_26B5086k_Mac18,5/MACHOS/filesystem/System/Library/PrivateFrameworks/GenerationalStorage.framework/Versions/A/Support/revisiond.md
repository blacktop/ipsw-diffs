## revisiond

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/Support/revisiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
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
-  __TEXT.__text: 0x3223c
+411.0.0.0.0
+  __TEXT.__text: 0x322f4
   __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_stubs: 0x3aa0
+  __TEXT.__objc_stubs: 0x3ac0
   __TEXT.__objc_methlist: 0x15b4
-  __TEXT.__const: 0x278
+  __TEXT.__const: 0x268
   __TEXT.__gcc_except_tab: 0x66c
-  __TEXT.__cstring: 0x64f4
-  __TEXT.__objc_methname: 0x40bb
+  __TEXT.__cstring: 0x64ea
+  __TEXT.__objc_methname: 0x4108
   __TEXT.__oslogstring: 0x363f
   __TEXT.__objc_classname: 0x1b7
   __TEXT.__objc_methtype: 0x15c6
-  __TEXT.__unwind_info: 0x1000
+  __TEXT.__unwind_info: 0x1008
   __DATA_CONST.__const: 0x12f8
   __DATA_CONST.__cfstring: 0x3120
   __DATA_CONST.__objc_classlist: 0x88

   __DATA_CONST.__auth_got: 0x800
   __DATA_CONST.__got: 0x2b0
   __DATA.__objc_const: 0x32b0
-  __DATA.__objc_selrefs: 0x11c0
+  __DATA.__objc_selrefs: 0x11c8
   __DATA.__objc_ivar: 0x1f4
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x498

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1025
+  Functions: 1026
   Symbols:   351
   CStrings:  1825
 
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
