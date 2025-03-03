## libhwtrace.dylib

> `/usr/lib/libhwtrace.dylib`

```diff

-114.1.0.0.0
-  __TEXT.__text: 0x1f7f68
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__const: 0x1ad430
-  __TEXT.__cstring: 0x18c5a
-  __TEXT.__oslogstring: 0x632
+117.0.0.0.0
+  __TEXT.__text: 0x1fd6c0
+  __TEXT.__auth_stubs: 0x1610
+  __TEXT.__const: 0x1ad480
+  __TEXT.__cstring: 0x18f4d
+  __TEXT.__oslogstring: 0x64c
   __TEXT.__gcc_except_tab: 0x1f8
-  __TEXT.__unwind_info: 0x2318
+  __TEXT.__unwind_info: 0x2350
   __TEXT.__eh_frame: 0xd8
   __TEXT.__objc_methname: 0x9b
   __TEXT.__objc_stubs: 0x100

   __DATA_CONST.__const: 0x489d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0xb08
+  __AUTH_CONST.__auth_got: 0xb18
   __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x6180
+  __AUTH_CONST.__const: 0x6288
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH.__data: 0x18
   __DATA.__data: 0x68

   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3535
-  Symbols:   550
-  CStrings:  5550
+  Functions: 3568
+  Symbols:   554
+  CStrings:  5581
 
Symbols:
+ _compression_encode_buffer
+ _compression_encode_scratch_buffer_size
+ _hwtrace_version_compatible_decode_format
+ _hwtrace_version_info
CStrings:
+ " without get-task-allow (csops: "
+ ", but consumer does not support it.\n"
+ ", but consumer has format "
+ "... Detected that amfi_unrestrict_task_for_pid=1 is not present in boot-args, so tracing policy is not relaxed."
+ "Chunks"
+ "CompressedOffset"
+ "CompressedSize"
+ "Compression"
+ "CompressionKey"
+ "CompressionType"
+ "ContextStarts"
+ "Counters"
+ "DataKey"
+ "Failed to parse version info from producer: "
+ "Incompatible compression metadata"
+ "LZ4"
+ "LZ4_RAW"
+ "LZFSE"
+ "Messages"
+ "Refusing to trace pid "
+ "Suggestion: Upgrade the OS installation on the target device where the trace was collected.\n"
+ "Suggestion: Upgrade the developer tools on this device.\n"
+ "Trace producer has format "
+ "Trace producer uses "
+ "UncompressedOffset"
+ "UncompressedSize"
+ "UnitMarks"
+ "Version incompatibility for decoded trace results:\n%{public}s\nIgnoring decoded results and attempting to re-decode..."
+ "Version information missing."
+ "VersionInfo"
+ "api_ver"
+ "compressed-decoding"
+ "compression_algs"
+ "default_compression_alg"
+ "format_maj_ver"
+ "format_min_ver"
+ "lib_ver"
+ "libhwtrace @ tag libhwtrace-117"
+ "libhwtrace @ tag libhwtrace-117\n"
+ "security.codesigning.config"
+ "sysctl security.codesigning.config failed"
- "ContextStartsKey"
- "CountersKey"
- "Major version incompatibility for decoded trace results: got %u, expected %u. Ignoring decoded results and attempting to re-decode..."
- "MajorVersion"
- "MessagesKey"
- "MinorVersion"
- "RangesKey"
- "Refusing to trace process without get-task-allow"
- "UnitMarksKey"
- "libhwtrace @ tag libhwtrace-114.1\n"

```
