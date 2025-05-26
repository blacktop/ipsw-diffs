## OSLog

> `/System/Library/Frameworks/OSLog.framework/OSLog`

```diff

-1481.0.12.0.0
-  __TEXT.__text: 0xa73c
-  __TEXT.__auth_stubs: 0x6a0
+1481.40.16.0.0
+  __TEXT.__text: 0xac44
+  __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_methlist: 0x5a0
   __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x87a
+  __TEXT.__cstring: 0x92d
   __TEXT.__oslogstring: 0x59
-  __TEXT.__unwind_info: 0x2f4
+  __TEXT.__unwind_info: 0x308
   __TEXT.__objc_classname: 0x134
   __TEXT.__objc_methname: 0xedc
   __TEXT.__objc_methtype: 0x251
   __TEXT.__objc_stubs: 0xd20
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x348
+  __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xe60
   __DATA_CONST.__objc_selrefs: 0x3c8
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH.__os_assumes_log: 0x8
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0xb8
   __DATA.__objc_superrefs: 0x50
   __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0x1e8
+  __DATA.__data: 0x1f8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__const: 0x130
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__const: 0xd0
   __DATA_DIRTY.__objc_const: 0x4c8
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 228
-  Symbols:   856
-  CStrings:  380
+  Functions: 233
+  Symbols:   889
+  CStrings:  388
 
Symbols:
+ GCC_except_table202
+ GCC_except_table215
+ GCC_except_table219
+ GCC_except_table225
+ ____internal_log_block_invoke
+ ___block_descriptor_tmp.10.103
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.16.79
+ ___block_descriptor_tmp.2.89
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.34
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.50
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.72
+ ___block_descriptor_tmp.75
+ ___block_descriptor_tmp.8.81
+ ___block_descriptor_tmp.86
+ ___block_descriptor_tmp.98
+ ___block_literal_global.444
+ ___block_literal_global.84
+ ___block_literal_global.96
+ __internal_log_assumes
+ __internal_log_fd
+ __internal_log_file_0
+ __internal_log_file_1
+ __internal_log_once
+ __internal_log_open
+ __internal_log_q
+ __internal_log_q_key
+ __internal_log_queue_init
+ __internal_log_rotate_if_needed
+ __internal_queue_target
+ __os_redirect__internal_log_assumes
+ _asprintf
+ _dispatch_assert_queue$V2
+ _dispatch_get_specific
+ _dispatch_once_f
+ _dispatch_queue_create_with_target$V2
+ _dispatch_queue_set_specific
+ _dispatch_sync
+ _fchown
+ _fsync
+ _getprogname
+ _localtime_r
+ _rename
+ _strftime
+ _time
- GCC_except_table197
- GCC_except_table210
- GCC_except_table214
- GCC_except_table220
- ___block_descriptor_tmp.10.102
- ___block_descriptor_tmp.17.80
- ___block_descriptor_tmp.2.87
- ___block_descriptor_tmp.33
- ___block_descriptor_tmp.35
- ___block_descriptor_tmp.40
- ___block_descriptor_tmp.51
- ___block_descriptor_tmp.66
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.76
- ___block_descriptor_tmp.8
- ___block_descriptor_tmp.84
- ___block_descriptor_tmp.96
- ___block_literal_global.430
- ___block_literal_global.82
- ___block_literal_global.94
CStrings:
+ "%F %T%z"
+ "%s %s[%d]: %s\n"
+ "%s/%s.0.log"
+ "%s/%s.1.log"
+ "BUG IN LIBTRACE: failed to create log file path"
+ "BUG IN LIBTRACE: failed to create queue target from subsystem"
+ "com.apple.%s.log"
+ "logd"

```
