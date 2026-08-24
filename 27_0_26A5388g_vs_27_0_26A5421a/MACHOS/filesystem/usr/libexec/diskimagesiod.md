## diskimagesiod

> `/usr/libexec/diskimagesiod`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-598.0.0.0.0
-  __TEXT.__text: 0x20deb0
+598.0.1.0.0
+  __TEXT.__text: 0x21032c
   __TEXT.__auth_stubs: 0x2580
   __TEXT.__objc_stubs: 0x6f00
   __TEXT.__objc_methlist: 0x3d5c
-  __TEXT.__const: 0x17d07
-  __TEXT.__gcc_except_tab: 0x1dfec
+  __TEXT.__const: 0x17e47
+  __TEXT.__gcc_except_tab: 0x1e134
   __TEXT.__objc_methname: 0x8121
   __TEXT.__oslogstring: 0x3c3d
-  __TEXT.__cstring: 0x158be
+  __TEXT.__cstring: 0x159b7
   __TEXT.__objc_classname: 0x6e0
   __TEXT.__objc_methtype: 0x2ca7
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0xeb20
+  __TEXT.__unwind_info: 0xec30
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__const: 0x3a3a0
+  __DATA_CONST.__const: 0x3ac10
   __DATA_CONST.__cfstring: 0x54a0
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 11977
+  Functions: 12040
   Symbols:   850
-  CStrings:  4348
+  CStrings:  4354
 
CStrings:
+ ", allocated: "
+ "Allocated after defrag: "
+ "Diskimageuio: Failed to create resizer: "
+ "Nothing to defrag"
+ "Starting ASIF defrag, used size: "
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2064:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2098:32)]"
+ "static expected<diskimage_resizer, diskimage_err> diskimage_uio::diskimage_resizer::create(diskimage_open_params &&)"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2035:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2069:32)]"
```
