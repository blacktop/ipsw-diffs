## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-278.0.0.0.0
-  __TEXT.__text: 0x24270
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_stubs: 0x1be0
+285.100.1.0.0
+  __TEXT.__text: 0x24dcc
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_stubs: 0x1c20
   __TEXT.__objc_methlist: 0x538
   __TEXT.__const: 0x2ee
-  __TEXT.__cstring: 0x24ab
-  __TEXT.__gcc_except_tab: 0x764
-  __TEXT.__oslogstring: 0x3de5
+  __TEXT.__cstring: 0x255e
+  __TEXT.__gcc_except_tab: 0x7fc
+  __TEXT.__oslogstring: 0x3ee1
   __TEXT.__ustring: 0x1c6
   __TEXT.__objc_classname: 0xdd
-  __TEXT.__objc_methname: 0x15c9
+  __TEXT.__objc_methname: 0x15fb
   __TEXT.__objc_methtype: 0x465
-  __TEXT.__unwind_info: 0x5dc
-  __DATA_CONST.__auth_got: 0x660
+  __TEXT.__unwind_info: 0x5e0
+  __DATA_CONST.__auth_got: 0x668
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x800
-  __DATA_CONST.__cfstring: 0x2440
+  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__cfstring: 0x2520
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x178
-  __DATA_CONST.__objc_dictobj: 0xc8
+  __DATA_CONST.__objc_arraydata: 0x188
+  __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA.__objc_const: 0xc50
-  __DATA.__objc_selrefs: 0x750
-  __DATA.__objc_classrefs: 0x148
-  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_selrefs: 0x760
   __DATA.__objc_ivar: 0x9c
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0xe0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 473
-  Symbols:   278
-  CStrings:  1071
+  Functions: 477
+  Symbols:   279
+  CStrings:  1085
 
Symbols:
+ _malloc
CStrings:
+ "\n\n%@"
+ "\n%@"
+ "0 5"
+ "ExclaveCapability"
+ "Failed to get matching PMU ioservices: 0x%x"
+ "Failed to locate primary PMU service"
+ "Finished processing %@ core, available at %@"
+ "IOPMUBootFaultInfo"
+ "IOService match returned an empty iterator for PMU services"
+ "Skip handling kernel corefile which suggests 0 files present"
+ "Unexpected SPMI fault reset occurred"
+ "Unexpected uncategorized reset occurred"
+ "[Warning: The attachments may contain privacy-sensitive sensor data.]"
+ "detected interesting reset, promoting to panic"
+ "rangeOfString:options:"
+ "read out PMU fault data: resetCount: %d, bootFailCount: %d, boot stage: 0x%x, boot app hash: %d, boot faults: %@, universal boot faults: %@:"
+ "read out auxiliary PMU fault data: boot fault info: %@"
+ "secure"
+ "stringByAppendingFormat:"
+ "unable to read out auxiliary PMU properties"
+ "unable to read out primary PMU properties"
- "0 4"
- "Failed to locate PMU service"
- "Finished processing %@ core, avaiable at %@"
- "IOPMUBootErrorFaults"
- "detected unexpected SoC watchdog reset, writing panic log to disk"
- "read out PMU fault data: panic count: %d, unexpected reset count: %d, boot stage: 0x%x, boot app hash: %d, boot faults: %@, universal boot faults: %@:"
- "unable to read out PMU properties"

```
