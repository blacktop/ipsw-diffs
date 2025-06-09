## jetsam_priority

> `/usr/libexec/jetsam_priority`

```diff

-10733.120.3.0.0
-  __TEXT.__text: 0xa030
-  __TEXT.__auth_stubs: 0x570
+10765.0.0.0.0
+  __TEXT.__text: 0xa360
+  __TEXT.__auth_stubs: 0x5c0
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xa1
-  __TEXT.__gcc_except_tab: 0xb0c
-  __TEXT.__cstring: 0x1280
+  __TEXT.__gcc_except_tab: 0xb3c
+  __TEXT.__cstring: 0x12c1
+  __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x126
-  __TEXT.__unwind_info: 0x290
-  __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__unwind_info: 0x2b8
+  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x198
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x70
-  __DATA.__data: 0x48
-  __DATA.__bss: 0x98
+  __DATA.__data: 0x4c
+  __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65DD57A6-62AB-3BA7-9D1C-ED0A67217047
-  Functions: 93
-  Symbols:   120
+  UUID: E4380C6E-60C2-3A5B-9549-ECCA822A7394
+  Functions: 97
+  Symbols:   126
   CStrings:  192
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZnwmSt19__type_descriptor_t
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x2
+ _sigaction
+ _strtoul
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
- _objc_release_x21
- _objc_release_x25
CStrings:
+ "   -n NUM: Number of samples in the time series (0 for unlimited, SIGINT/SIGTERM to interrupt)\n"
+ "Warning: Spurious wakeup before %lums, retrying\n"
- "   -n NUM: Number of samples in the time series\n"
- "Fatal: Failed to wait for %dms"

```
