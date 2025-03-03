## libsystemstats.dylib

> `/usr/lib/libsystemstats.dylib`

```diff

-498.0.0.0.0
-  __TEXT.__text: 0x6158
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x5ff
-  __TEXT.__gcc_except_tab: 0x15c
-  __TEXT.__oslogstring: 0x8d0
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_methname: 0xf8
-  __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x290
+498.100.2.0.0
+  __TEXT.__text: 0x70a0
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x627
+  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__oslogstring: 0x900
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_methname: 0x185
+  __TEXT.__objc_stubs: 0x240
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__const: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x420
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xe0
-  __DATA.__data: 0x540
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_CONST.__objc_selrefs: 0x98
+  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x100
+  __DATA.__bss: 0x18
+  __DATA_DIRTY.__data: 0x540
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 144
-  Symbols:   187
-  CStrings:  128
+  Functions: 156
+  Symbols:   201
+  CStrings:  144
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _objc_release_x1
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x27
+ _objc_retain_x4
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
+ "count"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "firstObject"
+ "initWithUTF8String:"
+ "lastPathComponent"
+ "micro"
+ "substringToIndex:"
+ "systemstats_foreach_micro_in_file"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "B40@?0^{micro_snapshot=IIQQCS}8^{task_snapshot=IiQQQ[16C]QIiiiiiIQQ[17c]IIIQQQQ[4Q][4Q]QQQQQQQQI}16^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24Q32"
- "Fetched %d bytes of microstackshots from the kernel"
- "Returned %zu microstackshots"
- "Unable to copy bad size of %d bytes of microstackshots from kernel"
- "Unexpected: a single microstackshot was larger than TELEMETRY_DATA_HIGHERWATER_SIZE. Skipping this stream."
- "Unexpected: a single microstackshot was larger than TELEMETRY_DATA_HIGHWATER_SIZE"
- "v40@?0^{micro_snapshot=IIQQCS}8^{task_snapshot=IiQQQ[16C]QIiiiiiIQQ[17c]IIIQQQQ[4Q][4Q]QQQQQQQQI}16^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24Q32"

```
