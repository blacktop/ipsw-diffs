## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1522.0.0.0.2
-  __TEXT.__text: 0x37f58
+1527.0.0.0.0
+  __TEXT.__text: 0x3845c
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x13e0
-  __TEXT.__objc_methlist: 0x55c
+  __TEXT.__objc_stubs: 0x1460
+  __TEXT.__objc_methlist: 0x564
   __TEXT.__const: 0x3f8
-  __TEXT.__gcc_except_tab: 0x7c4
-  __TEXT.__oslogstring: 0x20c2
-  __TEXT.__cstring: 0x2e667
+  __TEXT.__gcc_except_tab: 0x7fc
+  __TEXT.__oslogstring: 0x2207
+  __TEXT.__cstring: 0x2e6fc
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x1444
-  __TEXT.__unwind_info: 0x520
+  __TEXT.__objc_methname: 0x14af
+  __TEXT.__unwind_info: 0x530
   __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x98
   __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x1a40
+  __DATA_CONST.__cfstring: 0x1a80
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0x568
+  __DATA.__objc_selrefs: 0x588
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libdscsym.dylib
+  - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 833AF6CD-49F2-3453-A732-52B2C1EF45F2
-  Functions: 314
-  Symbols:   251
-  CStrings:  4238
+  UUID: 12CDF9FD-4FEF-3F85-8476-2137D87C88BF
+  Functions: 322
+  Symbols:   253
+  CStrings:  4259
 
Symbols:
+ _OBJC_CLASS_$_MISProfileDBClient
+ _OBJC_CLASS_$_NSJSONSerialization
CStrings:
+ "Profile Access SPI not available"
+ "Profile Access: Failed to allocate dest file path"
+ "Profile Access: error with JSON serialization: %{public}s"
+ "Profile Access: failed to create info dict"
+ "Profile Access: failed to fetch jsonData, but no error returned"
+ "Profile Access: task returned nil string data"
+ "Profile Access: task timed out"
+ "TASK_TYPE_PROFILE_ACCESS"
+ "dataWithJSONObject:options:error:"
+ "diagnostics"
+ "diagnostics.txt"
+ "initWithData:encoding:"
+ "profileAccessTaskWithDir:withTimeout:"
+ "wcacheOverWrLogSizeCnts"
+ "wcacheOverWrSizeByFlow"
+ "wcacheWr"
+ "wcache_Mbytes"
+ "wcache_Reads"
+ "wcache_segsSortedLogSize"

```
