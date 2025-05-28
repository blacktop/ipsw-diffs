## spindump

> `/usr/sbin/spindump`

```diff

-341.0.0.0.0
-  __TEXT.__text: 0x89e48
-  __TEXT.__auth_stubs: 0x1200
+341.1.0.0.0
+  __TEXT.__text: 0x8a274
+  __TEXT.__auth_stubs: 0x1210
   __TEXT.__objc_stubs: 0x2dc0
   __TEXT.__objc_methlist: 0x89c
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x117a8
-  __TEXT.__oslogstring: 0x1fc91
+  __TEXT.__cstring: 0x118aa
+  __TEXT.__oslogstring: 0x1fe6b
   __TEXT.__objc_classname: 0xc9
   __TEXT.__gcc_except_tab: 0x1510
   __TEXT.__objc_methname: 0x31c7
   __TEXT.__objc_methtype: 0x483
-  __TEXT.__unwind_info: 0xa50
-  __DATA_CONST.__auth_got: 0x910
+  __TEXT.__unwind_info: 0xa64
+  __DATA_CONST.__auth_got: 0x918
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x10c0
-  __DATA_CONST.__cfstring: 0x7da0
+  __DATA_CONST.__cfstring: 0x7e00
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1928

   __DATA.__data: 0x18
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x7d0
-  __DATA.__common: 0x68
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1678
-  Symbols:   376
-  CStrings:  3811
+  Functions: 1684
+  Symbols:   377
+  CStrings:  3818
 
Symbols:
+ _objc_release_x28
CStrings:
+ "%s [%d]: cpu resource: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "%{public}s [%d]: cpu resource: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "Unable to format: %s [%d]: cpu resource: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "Unable to format: cpu resource: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "cpu resource: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "cpu_resource_1st_party_sampling_percentage"

```
