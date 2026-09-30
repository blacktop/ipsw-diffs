## spindump

> `/usr/sbin/spindump`

```diff

-  __TEXT.__text: 0xb76d0
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_stubs: 0x4180
+  __TEXT.__text: 0xb8e10
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__objc_stubs: 0x41a0
   __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x15117
-  __TEXT.__oslogstring: 0x2697f
-  __TEXT.__gcc_except_tab: 0x2f24
+  __TEXT.__const: 0x270
+  __TEXT.__cstring: 0x1532b
+  __TEXT.__oslogstring: 0x26ded
+  __TEXT.__gcc_except_tab: 0x3094
   __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methname: 0x4257
+  __TEXT.__objc_methname: 0x4265
   __TEXT.__objc_methtype: 0x530
-  __TEXT.__unwind_info: 0xcc8
-  __DATA_CONST.__const: 0x1520
-  __DATA_CONST.__cfstring: 0x9be0
+  __TEXT.__unwind_info: 0xcd0
+  __DATA_CONST.__const: 0x1540
+  __DATA_CONST.__cfstring: 0x9d60
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x980
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_got: 0x9c8
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x11b8
+  __DATA.__objc_selrefs: 0x11c0
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x20
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x808
+  __DATA.__bss: 0x818
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1808
-  Symbols:   380
-  CStrings:  5934
+  Functions: 1818
+  Symbols:   389
+  CStrings:  5977
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _SANanosecondsFromMachTimeUsingTimebase
+ _ktrace_file_close
+ _ktrace_file_earliest_continuous_time
+ _ktrace_file_latest_continuous_time
+ _ktrace_file_open
+ _ktrace_file_supports_continuous_time
+ _ktrace_file_timebase
+ _mach_timebase_info
+ _statfs
CStrings:
+ "No mach continuous time in WR tailspin %s"
+ "No overlap in WR tailspin %s"
+ "PowerExceptions"
+ "Unable to format: No mach continuous time in WR tailspin %s"
+ "Unable to format: No overlap in WR tailspin %s"
+ "Unable to format: Unable to get earliest ktrace machcont timestamp in WR tailspin %s: %d (%s)"
+ "Unable to format: Unable to get ktrace mach timebase, assuming native timebase in WR tailspin %s: %d (%s)"
+ "Unable to format: Unable to get latest ktrace machcont timestamp in WR tailspin %s: %d (%s)"
+ "Unable to format: Unable to open WR tailspin %s: %d (%s)"
+ "Unable to format: Unable to statfs %s: %d (%s)"
+ "Unable to format: ktrace mach timebase %d/%d, assuming native timebase in WR tailspin %s"
+ "Unable to format: ktrace unavailable for WR tailspin %s"
+ "Unable to get earliest ktrace machcont timestamp in WR tailspin %s: %d (%s)"
+ "Unable to get ktrace mach timebase, assuming native timebase in WR tailspin %s: %d (%s)"
+ "Unable to get latest ktrace machcont timestamp in WR tailspin %s: %d (%s)"
+ "Unable to open WR tailspin %s: %d (%s)"
+ "Unable to statfs %s: %d (%s)"
+ "bug_subtype"
+ "codesigningID"
+ "ktrace mach timebase %d/%d, assuming native timebase in WR tailspin %s"
+ "ktrace unavailable for WR tailspin %s"
+ "overlapdurationms"

```
