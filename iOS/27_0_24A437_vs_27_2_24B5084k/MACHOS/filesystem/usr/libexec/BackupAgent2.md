## BackupAgent2

> `/usr/libexec/BackupAgent2`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3039.2.2.0.0
-  __TEXT.__text: 0x8ed68
+3039.40.8.0.0
+  __TEXT.__text: 0x8f4e4
   __TEXT.__auth_stubs: 0x1850
   __TEXT.__objc_stubs: 0xc9c0
   __TEXT.__objc_methlist: 0x5ffc
-  __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x1900c
-  __TEXT.__oslogstring: 0xdfd8
+  __TEXT.__const: 0x4b8
+  __TEXT.__cstring: 0x191dc
+  __TEXT.__oslogstring: 0xe1a8
   __TEXT.__objc_methname: 0xe80d
   __TEXT.__objc_classname: 0xa09
   __TEXT.__objc_methtype: 0x1e9d
-  __TEXT.__gcc_except_tab: 0x210c
-  __TEXT.__unwind_info: 0x22b0
-  __DATA_CONST.__const: 0x1438
+  __TEXT.__gcc_except_tab: 0x2478
+  __TEXT.__unwind_info: 0x22c0
+  __DATA_CONST.__const: 0x1460
   __DATA_CONST.__cfstring: 0x9500
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x68

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0xc38
   __DATA_CONST.__got: 0x588
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x99f0
   __DATA.__objc_selrefs: 0x3ca8
   __DATA.__objc_ivar: 0x558

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2458
+  Functions: 2459
   Symbols:   558
-  CStrings:  5765
+  CStrings:  5772
 
CStrings:
+ "=diag= Aborting directory node enumeration, too many dirents under %{public}s"
+ "=diag= Aborting readdir_r, too many dirents under %{public}s"
+ "=diag= Failed to enumerate directory nodes under %{public}s"
+ "=diag= Failed to find the file using getattrlistbulk (%u)"
+ "=diag= getattrlistbulk found file entry (%u) for %@: %@"
+ "=drive-domain-delegate= Not creating safe harbour for %@ with invalid container type (%@)"
+ "=pc= open_dprotected_np could not open file at %s: %{errno}d"
```
