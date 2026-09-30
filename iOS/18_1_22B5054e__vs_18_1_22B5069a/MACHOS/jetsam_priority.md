## jetsam_priority

> `/usr/libexec/jetsam_priority`

```diff

-10725.40.2.0.0
-  __TEXT.__text: 0x9104
-  __TEXT.__auth_stubs: 0x5b0
+10725.40.3.0.0
+  __TEXT.__text: 0x92e0
+  __TEXT.__auth_stubs: 0x5a0
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0xb68
-  __TEXT.__cstring: 0x116e
+  __TEXT.__gcc_except_tab: 0xba0
+  __TEXT.__cstring: 0x124e
   __TEXT.__objc_methname: 0x126
   __TEXT.__unwind_info: 0x2b8
-  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x70
-  __DATA.__data: 0x8
-  __DATA.__bss: 0xc8
+  __DATA.__data: 0xc
+  __DATA.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 91
-  Symbols:   124
-  CStrings:  179
+  Symbols:   123
+  CStrings:  184
 
Symbols:
+ _mach_wait_until
+ _objc_release_x21
- _objc_release_x25
- _objc_release_x26
- _objc_release_x28
CStrings:
+ "   -d MS: Delay between the time series samples in ms\n"
+ "   -n NUM: Number of samples in the time series\n"
+ ":kd:n:hcelifs:w:rxp:z::"
+ "Fatal: Failed to wait for %!d(MISSING)ms"
+ "Fatal: Specify the delay(ms) between the time series samples with option -d.\n"
+ "sample"
- ":khcelifs:w:rxp:z::"

```
