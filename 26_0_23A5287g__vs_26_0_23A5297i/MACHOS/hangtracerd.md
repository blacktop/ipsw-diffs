## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-380.0.0.0.0
-  __TEXT.__text: 0x33a28
+382.0.0.0.0
+  __TEXT.__text: 0x33be0
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_stubs: 0x5560
-  __TEXT.__objc_methlist: 0x209c
+  __TEXT.__objc_stubs: 0x5580
+  __TEXT.__objc_methlist: 0x20a4
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x4873
-  __TEXT.__oslogstring: 0x639b
+  __TEXT.__cstring: 0x4891
+  __TEXT.__oslogstring: 0x6428
   __TEXT.__objc_classname: 0x328
-  __TEXT.__objc_methname: 0x88c8
-  __TEXT.__objc_methtype: 0x1051
+  __TEXT.__objc_methname: 0x892c
+  __TEXT.__objc_methtype: 0x1055
   __TEXT.__gcc_except_tab: 0x3b8
-  __TEXT.__unwind_info: 0xa38
+  __TEXT.__unwind_info: 0xa40
   __DATA_CONST.__auth_got: 0x780
   __DATA_CONST.__got: 0x440
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1f08
-  __DATA_CONST.__cfstring: 0x5e00
+  __DATA_CONST.__const: 0x1f10
+  __DATA_CONST.__cfstring: 0x5e20
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x4a10
-  __DATA.__objc_selrefs: 0x1b00
-  __DATA.__objc_ivar: 0x42c
+  __DATA.__objc_const: 0x4a40
+  __DATA.__objc_selrefs: 0x1b10
+  __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x540
   __DATA.__bss: 0x538

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: CAB2B100-7584-3DE3-BB8F-CB6AFE4CC829
-  Functions: 1158
+  UUID: E7F5FC18-5654-39D1-A4D9-10E137D85D07
+  Functions: 1161
   Symbols:   389
-  CStrings:  3622
+  CStrings:  3631
 
CStrings:
+ "Collecting tailspin for a sequence of %lu hang(s): %{public}@\n"
+ "Compsed final stateInfo sorted Array: %{public}@"
+ "Passed in nil stateInfoPtr, returning nil."
+ "ShouldCollectCPURoleInfo"
+ "TB,R,V_shouldCollectCPURoleInfo"
+ "Will request tailspin at: %{public}@, fd: %i with reasonString:%{public}@"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}"
+ "_shouldCollectCPURoleInfo"
+ "cpuRoleEnum"
+ "isEqualToNumber:"
+ "shouldCollectCPURoleInfo"
- "Collecting tailspin for a sequence of %lu hang(s)\n"
- "Will request tailspin at: %@, fd: %i"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
- "taskEnum"

```
