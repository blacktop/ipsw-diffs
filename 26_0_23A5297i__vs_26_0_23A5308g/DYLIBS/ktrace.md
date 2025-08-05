## ktrace

> `/System/Library/PrivateFrameworks/ktrace.framework/ktrace`

```diff

-675.0.0.0.0
-  __TEXT.__text: 0xbe5bc
-  __TEXT.__auth_stubs: 0x3480
+676.0.0.0.0
+  __TEXT.__text: 0xbee34
+  __TEXT.__auth_stubs: 0x3490
   __TEXT.__objc_methlist: 0x3e0
   __TEXT.__const: 0x556a
-  __TEXT.__cstring: 0x6b3a
+  __TEXT.__cstring: 0x6b6a
   __TEXT.__oslogstring: 0x5445
   __TEXT.__gcc_except_tab: 0x1088
   __TEXT.__swift5_typeref: 0x15b0

   __TEXT.__swift5_mpenum: 0x80
   __TEXT.__swift5_capture: 0x36c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2a20
+  __TEXT.__unwind_info: 0x2a30
   __TEXT.__eh_frame: 0x28bc
   __TEXT.__objc_classname: 0xc5
   __TEXT.__objc_methname: 0xd70
   __TEXT.__objc_methtype: 0x1423
   __TEXT.__objc_stubs: 0x7e0
   __DATA_CONST.__got: 0x5f0
-  __DATA_CONST.__const: 0x1c50
+  __DATA_CONST.__const: 0x1c78
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x1a58
+  __AUTH_CONST.__auth_got: 0x1a60
   __AUTH_CONST.__const: 0x4c78
   __AUTH_CONST.__cfstring: 0x12c0
   __AUTH_CONST.__objc_const: 0xf40

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 30D671DE-BD30-3DF3-B65D-A5F98E76EAF1
-  Functions: 3831
-  Symbols:   6902
-  CStrings:  1832
+  UUID: B230AABD-6441-39F0-AFF8-030651B3BF1B
+  Functions: 3834
+  Symbols:   6911
+  CStrings:  1833
 
Symbols:
+ ___block_descriptor_tmp.37
+ ___ktrace_file_passive_interval_block_invoke
+ _block_copy_helper.10
+ _block_copy_helper.22
+ _block_copy_helper.30
+ _block_copy_helper.37
+ _block_copy_helper.63
+ _block_copy_helper.69
+ _block_copy_helper.73
+ _block_copy_helper.76
+ _block_copy_helper.79
+ _block_copy_helper.82
+ _block_descriptor.12
+ _block_descriptor.24
+ _block_descriptor.32
+ _block_descriptor.39
+ _block_descriptor.65
+ _block_descriptor.71
+ _block_descriptor.75
+ _block_descriptor.78
+ _block_descriptor.81
+ _block_descriptor.84
+ _block_destroy_helper.11
+ _block_destroy_helper.23
+ _block_destroy_helper.31
+ _block_destroy_helper.38
+ _block_destroy_helper.64
+ _block_destroy_helper.70
+ _block_destroy_helper.74
+ _block_destroy_helper.77
+ _block_destroy_helper.80
+ _block_destroy_helper.83
+ _ktrace_file_passive_interval
+ _ktrace_file_passive_interval.cold.1
+ _ktrace_file_passive_interval.cold.2
+ _objectdestroy.20Tm
- _block_copy_helper.18
- _block_copy_helper.25
- _block_copy_helper.32
- _block_copy_helper.47
- _block_copy_helper.56
- _block_copy_helper.62
- _block_copy_helper.65
- _block_copy_helper.68
- _block_copy_helper.71
- _block_copy_helper.74
- _block_copy_helper.8
- _block_descriptor.10
- _block_descriptor.20
- _block_descriptor.27
- _block_descriptor.34
- _block_descriptor.49
- _block_descriptor.58
- _block_descriptor.64
- _block_descriptor.67
- _block_descriptor.70
- _block_descriptor.73
- _block_descriptor.76
- _block_destroy_helper.19
- _block_destroy_helper.26
- _block_destroy_helper.33
- _block_destroy_helper.48
- _block_destroy_helper.57
- _block_destroy_helper.63
- _block_destroy_helper.66
- _block_destroy_helper.69
- _block_destroy_helper.72
- _block_destroy_helper.75
- _block_destroy_helper.9
- _objectdestroy.16Tm
CStrings:
+ "Failed to append passive time range chunk"

```
