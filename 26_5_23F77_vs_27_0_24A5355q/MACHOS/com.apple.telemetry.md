## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-510.120.2.0.0
-  __TEXT.__text: 0x8868
+514.0.0.0.0
+  __TEXT.__text: 0x80ec
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_stubs: 0x320
-  __TEXT.__const: 0x13b
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__cstring: 0x9a5
-  __TEXT.__oslogstring: 0x4782
-  __TEXT.__objc_classname: 0x3
+  __TEXT.__const: 0x144
+  __TEXT.__gcc_except_tab: 0x280
+  __TEXT.__cstring: 0x9a8
+  __TEXT.__oslogstring: 0x47e7
   __TEXT.__objc_methname: 0x202
-  __TEXT.__unwind_info: 0x158
-  __DATA.__auth_got: 0x3d0
-  __DATA.__got: 0xc0
-  __DATA.__auth_ptr: 0x8
+  __TEXT.__unwind_info: 0x140
   __DATA.__const: 0x268
   __DATA.__cfstring: 0x400
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_intobj: 0x18
   __DATA.__data: 0x8
+  __DATA.__auth_got: 0x3d0
+  __DATA.__got: 0xc0
+  __DATA.__auth_ptr: 0x8
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0146F00F-A429-38AE-8A9A-DEFBBFFF9C49
-  Functions: 159
+  UUID: E4DEFB09-6493-357D-BB3C-F931FE87A94A
+  Functions: 153
   Symbols:   153
   CStrings:  301
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x23
- _objc_retain_x24
CStrings:
+ "OB"
+ "Saved %zu microstackshots (%zu:%zu user:kernel, %d:%d bytes) (ignored %d:%d known duplicates and %d:%d likely duplicates). num_counted:%d num_noncounted:%d first_expected_samples_recorded:%llu largest_samples_recorded:%llu"
- "O"
- "Saved %zu microstackshots (%zu:%zu user:kernel, %d:%d bytes) (ignored %d:%d known duplicates and %d:%d likely duplicates)"

```
