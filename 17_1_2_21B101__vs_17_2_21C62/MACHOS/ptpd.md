## ptpd

> `/usr/libexec/ptpd`

```diff

-1873.1.2.0.0
-  __TEXT.__text: 0x2a284
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x4260
-  __TEXT.__objc_methlist: 0x2628
-  __TEXT.__cstring: 0x6e8c
+1873.2.4.0.0
+  __TEXT.__text: 0x2ab20
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_stubs: 0x4300
+  __TEXT.__objc_methlist: 0x2658
+  __TEXT.__cstring: 0x6eec
   __TEXT.__oslogstring: 0x3f
   __TEXT.__objc_classname: 0x2a7
-  __TEXT.__objc_methname: 0x53c0
-  __TEXT.__objc_methtype: 0xb1f
+  __TEXT.__objc_methname: 0x545e
+  __TEXT.__objc_methtype: 0xb3b
   __TEXT.__const: 0x68
   __TEXT.__ustring: 0x9e4
-  __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__unwind_info: 0x820
-  __DATA_CONST.__auth_got: 0x4a0
+  __TEXT.__gcc_except_tab: 0x254
+  __TEXT.__unwind_info: 0x818
+  __DATA_CONST.__auth_got: 0x4e0
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x738
-  __DATA_CONST.__cfstring: 0x77e0
+  __DATA_CONST.__cfstring: 0x7940
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_arraydata: 0x28e0
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x21c0
-  __DATA.__objc_const: 0x3fd8
-  __DATA.__objc_selrefs: 0x1728
+  __DATA.__objc_const: 0x4010
+  __DATA.__objc_selrefs: 0x1738
   __DATA.__objc_classrefs: 0x158
   __DATA.__objc_superrefs: 0xf8
-  __DATA.__objc_ivar: 0x478
+  __DATA.__objc_ivar: 0x47c
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x1c4
   __DATA.__common: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2575E043-346E-393C-8C9A-ECA9F99224DD
-  Functions: 973
-  Symbols:   217
-  CStrings:  3259
+  UUID: 4A1F3C44-AE93-39C2-B817-63C1206BDDFE
+  Functions: 979
+  Symbols:   225
+  CStrings:  3285
 
Symbols:
+ _NSTemporaryDirectory
+ _lstat
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeak
+ _objc_release_x24
+ _unlink
CStrings:
+ "  !!! F_RDADVISE: Failed to set"
+ "  !!! Failed to read bytes from %s"
+ "  >>> Setting[%s]:[%10lu]"
+ "%@%@"
+ "0x%x"
+ "Boosted [%s]"
+ "Canceled [%s]"
+ "Created [%s]"
+ "Created temporary file at: %@ -- fd: %d"
+ "Destroyed [%s]"
+ "Fired [%s]"
+ "Output size: %llu"
+ "TB,N,V_unlinkWhenDone"
+ "USBDevice"
+ "Unlinking file on completion: %@"
+ "_unlinkWhenDone"
+ "objectInfos"
+ "pathObjectInfoForObjectsInStorage:forObjectFormatCode:inAssociation:withContentType:responseCode:"
+ "ptpDataPacket"
+ "ptpObjects"
+ "setUnlinkWhenDone:"
+ "strongSelf is not available, bailing."
+ "unlinkWhenDone"
+ "v40@0:8{_NSRange=QQ}16r^v32"
- "%s Issuing writeBulkPipeData: [%ld] \n"
- "%s Issuing writeInterruptData: [%ld] \n"
- "Data Source Changed - Closing[%s]:[%10lu]"
- "F_RDADVISE: Failed to set"
- "Failed to read bytes from %s"
- "Main Thread"
- "Worker Thread"
- "[%s] Boosted \n"
- "[%s] Path: %s \n"
- "[%s] Read Bytes: Length:[%lu] Offset:[%llu] \n"
- "isMainThread"

```
