## libsystemstats.dylib

> `/usr/lib/libsystemstats.dylib`

```diff

-498.0.0.0.0
-  __TEXT.__text: 0xb20c
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x334
-  __TEXT.__cstring: 0xa50
-  __TEXT.__oslogstring: 0x91c
-  __TEXT.__unwind_info: 0x310
+498.100.2.0.0
+  __TEXT.__text: 0xc55c
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_methlist: 0x158
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x44c
+  __TEXT.__cstring: 0xa4e
+  __TEXT.__oslogstring: 0x94c
+  __TEXT.__unwind_info: 0x3a0
   __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0x527
+  __TEXT.__objc_methname: 0x565
   __TEXT.__objc_methtype: 0x1de
-  __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x1c0
+  __TEXT.__objc_stubs: 0x560
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x138
+  __DATA_CONST.__objc_selrefs: 0x1f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x478
-  __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x3b8
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__const: 0x5d0
+  __AUTH_CONST.__cfstring: 0x4a0
+  __AUTH_CONST.__objc_const: 0x130
   __AUTH_CONST.__objc_dictobj: 0x28
   __DATA.__data: 0x608
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7EB27192-34E5-3546-A130-5811E95A1AA2
-  Functions: 244
-  Symbols:   243
-  CStrings:  305
+  UUID: 614A21DC-1FE9-3E25-8652-51C5F6D3D7D7
+  Functions: 265
+  Symbols:   249
+  CStrings:  315
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _objc_retainAutoreleaseReturnValue
+ _os_log_create
+ _strnstr
+ _systemstats_zipper_buffers_foreach_micro
+ _xpc_dictionary_get_value
CStrings:
+ "(unsigned)offsetToNextItem <= buffer_size"
+ "B24@?0r^v8Q16"
+ "B24@?0r^{systemstats_micro_chunk=IIb1b63}8Q16"
+ "B40@?0r^{micro_snapshot=IIQQCS}8r^{task_snapshot=IiQQQ[16C]QIiiiiiIQQ[17c]IIIQQQQ[4Q][4Q]QQQQQQQQI}16r^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24Q32"
+ "Returned %zu microstackshots, %zu chunks"
+ "Unexpected: a single microstackshot item was larger than TELEMETRY_DATA_HIGHERWATER_SIZE. Skipping this stream."
+ "__microstackshot for kernel returned error %{errno}d}"
+ "__microstackshot for kernel returned invalid buffer of size: %d"
+ "__microstackshot for user returned error %{errno}d}"
+ "__microstackshot for user returned invalid buffer of size: %d"
+ "bootinfo"
+ "com.apple.systemstats"
+ "containsObject:"
+ "containsString:"
+ "firstObject"
+ "micro"
+ "substringToIndex:"
+ "systemstats_foreach_micro_in_file"
- "32"
- "64"
- "B40@?0^{micro_snapshot=IIQQCS}8^{task_snapshot=IiQQQ[16C]QIiiiiiIQQ[17c]IIIQQQQ[4Q][4Q]QQQQQQQQI}16^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24Q32"
- "Fetched %d bytes of microstackshots from the kernel"
- "Returned %zu microstackshots"
- "Unable to copy bad size of %d bytes of microstackshots from kernel"
- "Unexpected: a single microstackshot was larger than TELEMETRY_DATA_HIGHERWATER_SIZE. Skipping this stream."
- "Unexpected: a single microstackshot was larger than TELEMETRY_DATA_HIGHWATER_SIZE"
- "v40@?0^{micro_snapshot=IIQQCS}8^{task_snapshot=IiQQQ[16C]QIiiiiiIQQ[17c]IIIQQQQ[4Q][4Q]QQQQQQQQI}16^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24Q32"

```
