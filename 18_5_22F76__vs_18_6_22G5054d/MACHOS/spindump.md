## spindump

> `/usr/sbin/spindump`

```diff

-383.14.0.0.0
-  __TEXT.__text: 0x96a14
+383.17.0.0.0
+  __TEXT.__text: 0x980b8
   __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_stubs: 0x3f20
+  __TEXT.__objc_stubs: 0x3f00
   __TEXT.__objc_methlist: 0x9f4
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x129d5
-  __TEXT.__oslogstring: 0x21a77
+  __TEXT.__cstring: 0x12aac
+  __TEXT.__oslogstring: 0x21bb7
   __TEXT.__objc_classname: 0xe5
-  __TEXT.__gcc_except_tab: 0x1dd0
-  __TEXT.__objc_methname: 0x4105
+  __TEXT.__gcc_except_tab: 0x21a0
+  __TEXT.__objc_methname: 0x40d3
   __TEXT.__objc_methtype: 0x52d
-  __TEXT.__unwind_info: 0xc90
+  __TEXT.__unwind_info: 0xcb0
   __DATA_CONST.__auth_got: 0x900
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x13a8
-  __DATA_CONST.__cfstring: 0x8a00
+  __DATA_CONST.__const: 0x13f8
+  __DATA_CONST.__cfstring: 0x8ac0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x1120
+  __DATA.__objc_selrefs: 0x1118
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x20

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 195AC92B-1DBA-3873-8CA9-7B033ABD6497
-  Functions: 1602
+  UUID: 9E78778D-0683-3BE0-A5BB-464E6BA44A00
+  Functions: 1620
   Symbols:   364
-  CStrings:  5360
+  CStrings:  5379
 
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
