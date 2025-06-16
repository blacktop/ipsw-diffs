## spindump_fileparser

> `/usr/libexec/spindump_fileparser`

```diff

-383.14.0.0.0
-  __TEXT.__text: 0x9afe0
+383.17.0.0.0
+  __TEXT.__text: 0x9c684
   __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_stubs: 0x4120
+  __TEXT.__objc_stubs: 0x4100
   __TEXT.__objc_methlist: 0x9f4
   __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x13401
-  __TEXT.__oslogstring: 0x232b9
+  __TEXT.__cstring: 0x134d8
+  __TEXT.__oslogstring: 0x233f9
   __TEXT.__objc_classname: 0xe5
-  __TEXT.__gcc_except_tab: 0x1dd0
-  __TEXT.__objc_methname: 0x41b4
+  __TEXT.__gcc_except_tab: 0x21a0
+  __TEXT.__objc_methname: 0x4182
   __TEXT.__objc_methtype: 0x52d
-  __TEXT.__unwind_info: 0xc98
+  __TEXT.__unwind_info: 0xcb8
   __DATA_CONST.__auth_got: 0x900
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x13a8
-  __DATA_CONST.__cfstring: 0x8f60
+  __DATA_CONST.__const: 0x13f8
+  __DATA_CONST.__cfstring: 0x9020
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58

   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x1160
+  __DATA.__objc_selrefs: 0x1158
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x20

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E68B0BD0-F6C9-3564-8688-D22B7009C4C5
-  Functions: 1603
+  UUID: E3C78E02-2103-3E85-A4DF-FF27740D560F
+  Functions: 1621
   Symbols:   365
-  CStrings:  5526
+  CStrings:  5545
 
Symbols:
+ ___snprintf_chk
- _objc_release_x22
CStrings:
+ "\n%s [%d] output exceeded %llu bytes, truncating"
+ "\n%s [%d] timed out after %llus, truncating"
+ "%s [%d]: No ddt output for resource exhaustion report"
+ "%s [%d]: No lsof output for resource exhaustion report"
+ "%{public}s [%d]: No ddt output for resource exhaustion report"
+ "%{public}s [%d]: No lsof output for resource exhaustion report"
+ "Child %s [%d] output exceeded %llu bytes"
+ "Child %s [%d] timed out after %llus"
+ "Child [%d] exited"
+ "No ddt output for resource exhaustion report"
+ "No lsof output for resource exhaustion report"
+ "Unable to format: %s [%d]: No ddt output for resource exhaustion report"
+ "Unable to format: %s [%d]: No lsof output for resource exhaustion report"
+ "Unable to format: Child %s [%d] output exceeded %llu bytes"
+ "Unable to format: Child %s [%d] timed out after %llus"
+ "Unable to format: Child [%d] exited"
+ "Unable to format: No ddt output for resource exhaustion report"
+ "Unable to format: No lsof output for resource exhaustion report"
+ "Unable to format: Waiting for child %s [%d]..."
+ "Waiting for child %s [%d]..."
- "%s [%d]: Unable to convert ddt output to NSString: %s"
- "%s [%d]: Unable to convert lsof output to NSString: %s"
- "%{public}s [%d]: Unable to convert ddt output to NSString: %s"
- "%{public}s [%d]: Unable to convert lsof output to NSString: %s"
- "Unable to convert ddt output to NSString: %s"
- "Unable to convert lsof output to NSString: %s"
- "Unable to format: %s [%d]: Unable to convert ddt output to NSString: %s"
- "Unable to format: %s [%d]: Unable to convert lsof output to NSString: %s"
- "Unable to format: Unable to convert ddt output to NSString: %s"
- "Unable to format: Unable to convert lsof output to NSString: %s"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"

```
