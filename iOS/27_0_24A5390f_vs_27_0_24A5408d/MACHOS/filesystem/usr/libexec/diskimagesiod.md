## diskimagesiod

> `/usr/libexec/diskimagesiod`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-598.0.0.0.0
-  __TEXT.__text: 0x1ed170
+598.0.1.0.0
+  __TEXT.__text: 0x1ef5cc
   __TEXT.__auth_stubs: 0x2450
   __TEXT.__objc_stubs: 0x6860
   __TEXT.__objc_methlist: 0x3a1c
-  __TEXT.__gcc_except_tab: 0x1bc70
-  __TEXT.__const: 0x17457
-  __TEXT.__cstring: 0x172ec
+  __TEXT.__gcc_except_tab: 0x1bdbc
+  __TEXT.__const: 0x17597
+  __TEXT.__cstring: 0x173e5
   __TEXT.__oslogstring: 0x2dab
   __TEXT.__objc_methname: 0x78e1
   __TEXT.__objc_classname: 0x667

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0xe000
+  __TEXT.__unwind_info: 0xe120
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__const: 0x38988
+  __DATA_CONST.__const: 0x391f8
   __DATA_CONST.__cfstring: 0x4c40
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  Functions: 11457
+  Functions: 11520
   Symbols:   800
-  CStrings:  4035
+  CStrings:  4041
 
CStrings:
+ ", allocated: "
+ "Allocated after defrag: "
+ "Diskimageuio: Failed to create resizer: "
+ "Nothing to defrag"
+ "Starting ASIF defrag, used size: "
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2064:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2098:32)]"
+ "static expected<diskimage_resizer, diskimage_err> diskimage_uio::diskimage_resizer::create(diskimage_open_params &&)"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2035:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2069:32)]"
```
