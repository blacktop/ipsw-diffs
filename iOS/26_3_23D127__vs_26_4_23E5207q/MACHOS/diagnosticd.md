## diagnosticd

> `/usr/libexec/diagnosticd`

```diff

-1815.80.2.0.0
-  __TEXT.__text: 0x7f4c
-  __TEXT.__auth_stubs: 0xf50
+1861.100.16.0.0
+  __TEXT.__text: 0x8000
+  __TEXT.__auth_stubs: 0xf40
   __TEXT.__objc_stubs: 0x460
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x470
-  __TEXT.__cstring: 0x197c
+  __TEXT.__cstring: 0x1ad5
   __TEXT.__objc_methname: 0x33c
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methtype: 0x50
   __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x7b0
+  __DATA_CONST.__auth_got: 0x7a8
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x7d8
+  __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F7D63406-FD8B-3C44-9683-5FB40B98AF3F
-  Functions: 91
-  Symbols:   293
-  CStrings:  334
+  UUID: 5356E589-9DFA-32F8-82DB-C9AED22670D5
+  Functions: 90
+  Symbols:   292
+  CStrings:  338
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
CStrings:
+ "/Library/Caches/com.apple.xbs/985B05C5-5B1D-4136-A868-78BE8E4D2B74/TemporaryDirectory.psmime/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/diagnosticd.build/DerivedSources/OSLogDarwin_C.c"
+ "TB_FATAL: invalid result returned from setStreamPreferences"
+ "TB_FATAL: invalid result returned from setStreamPreferences (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[OSLogDarwin.StreamPrefsValue]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[OSLogDarwin.StreamPrefsValue]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: overflow detected when multiplying"
+ "TB_FATAL: overflow detected when multiplying (%s:%d)\n"
- "/Library/Caches/com.apple.xbs/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/diagnosticd.build/DerivedSources/OSLogDarwin_C.c"
- "TB_FATAL: invalid tag in array metadata: 0x%x"
- "TB_FATAL: invalid tag in array metadata: 0x%x (%s:%d)\n"

```
