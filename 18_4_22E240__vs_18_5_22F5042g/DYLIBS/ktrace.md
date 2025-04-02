## ktrace

> `/System/Library/PrivateFrameworks/ktrace.framework/ktrace`

```diff

-649.100.6.0.0
-  __TEXT.__text: 0xba2dc
-  __TEXT.__auth_stubs: 0x3260
+649.120.3.0.0
+  __TEXT.__text: 0xba90c
+  __TEXT.__auth_stubs: 0x32e0
   __TEXT.__objc_methlist: 0x360
   __TEXT.__const: 0x4d78
-  __TEXT.__cstring: 0x6646
-  __TEXT.__oslogstring: 0x5235
+  __TEXT.__cstring: 0x6686
+  __TEXT.__oslogstring: 0x52c5
   __TEXT.__gcc_except_tab: 0x10e8
   __TEXT.__swift5_typeref: 0x135a
   __TEXT.__swift5_reflstr: 0x28a1

   __TEXT.__swift5_mpenum: 0x78
   __TEXT.__swift5_capture: 0x3b0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2888
+  __TEXT.__unwind_info: 0x28b8
   __TEXT.__eh_frame: 0x2748
   __TEXT.__objc_classname: 0x9b
   __TEXT.__objc_methname: 0xc46
   __TEXT.__objc_methtype: 0xfea
   __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x1bf0
+  __DATA_CONST.__got: 0x5a8
+  __DATA_CONST.__const: 0x1c30
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x1948
+  __AUTH_CONST.__auth_got: 0x1988
   __AUTH_CONST.__auth_ptr: 0x4e0
   __AUTH_CONST.__const: 0x4848
-  __AUTH_CONST.__cfstring: 0x1280
+  __AUTH_CONST.__cfstring: 0x12a0
   __AUTH_CONST.__objc_const: 0xf00
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x190

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3687
-  Symbols:   3558
-  CStrings:  1611
+  Functions: 3691
+  Symbols:   3569
+  CStrings:  1617
 
Symbols:
+ _dyld_image_copy_uuid
+ _dyld_image_for_each_segment_info
+ _dyld_image_get_file_path
+ _dyld_image_get_installname
+ _dyld_process_create_for_task
+ _dyld_process_dispose
+ _dyld_process_snapshot_create_for_process
+ _dyld_process_snapshot_dispose
+ _dyld_process_snapshot_for_each_image
+ _mach_task_self_
+ _task_read_for_pid
- _CSSymbolOwnerIsDyldSharedCache
- _CSSymbolicatorCreateWithPid
CStrings:
+ "!!!invalid-enc!!!"
+ "Failed to create dyld process for %u (%{errno}d)"
+ "Failed to create dyld snapshot for %u (%{errno}d)"
+ "task_read_for_pid failed for %u (%{errno}d)"
+ "v16@?0^{dyld_image_s=}8"
+ "v36@?0r*8Q16Q24i32"

```
