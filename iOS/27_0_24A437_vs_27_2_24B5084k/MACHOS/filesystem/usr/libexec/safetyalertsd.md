## safetyalertsd

> `/usr/libexec/safetyalertsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-70.0.20.0.0
-  __TEXT.__text: 0xfce28
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_stubs: 0x3760
+70.0.21.0.0
+  __TEXT.__text: 0xfd898
+  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__objc_stubs: 0x3780
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0x9870
-  __TEXT.__cstring: 0x7a5a
-  __TEXT.__gcc_except_tab: 0xef60
-  __TEXT.__oslogstring: 0x4359a
-  __TEXT.__objc_methname: 0x3e58
+  __TEXT.__cstring: 0x7a74
+  __TEXT.__gcc_except_tab: 0xf034
+  __TEXT.__oslogstring: 0x439b2
+  __TEXT.__objc_methname: 0x3e67
   __TEXT.__objc_classname: 0x1e9
   __TEXT.__objc_methtype: 0x1cdf
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x4a40
-  __DATA_CONST.__const: 0x89b8
-  __DATA_CONST.__cfstring: 0x72c0
+  __TEXT.__unwind_info: 0x4a88
+  __DATA_CONST.__const: 0x8988
+  __DATA_CONST.__cfstring: 0x7300
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__auth_got: 0x870
   __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x1248
-  __DATA.__objc_selrefs: 0x1260
+  __DATA.__objc_selrefs: 0x1268
   __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x448

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3605
-  Symbols:   469
-  CStrings:  5108
+  Functions: 3611
+  Symbols:   470
+  CStrings:  5119
 
Symbols:
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
CStrings:
+ ".."
+ "pathComponents"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,unsafe codebook file name rejected\", \"codebookFileName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#md,downloadManifest,unsafe manifest file name rejected\", \"id\":%{private, location:escape_only}s, \"fFileName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#rm,#warning,downloadManifest,unsafe manifest file name rejected\", \"efficacyStr\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#sa_util,safePath,rejected current-dir component\", \"path\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#sa_util,safePath,rejected embedded null byte\", \"path\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#sa_util,safePath,rejected invalid utf8\", \"path\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#sa_util,safePath,rejected parent traversal\", \"path\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#sa_util,safePath,rejected trailing slash\", \"path\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#sapref,customerBuildGating\", \"active\":%{private}hhd}"
```
