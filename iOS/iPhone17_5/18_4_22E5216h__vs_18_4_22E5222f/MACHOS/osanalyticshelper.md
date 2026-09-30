## osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

-758.100.41.0.0
-  __TEXT.__text: 0x11b5c
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_stubs: 0x2420
-  __TEXT.__objc_methlist: 0x7a8
+758.100.43.0.0
+  __TEXT.__text: 0x123f0
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_stubs: 0x2500
+  __TEXT.__objc_methlist: 0x7b0
   __TEXT.__const: 0x1ca
-  __TEXT.__oslogstring: 0x1b1c
-  __TEXT.__cstring: 0x1a01
+  __TEXT.__oslogstring: 0x1bbc
+  __TEXT.__cstring: 0x1b21
   __TEXT.__objc_classname: 0x14c
   __TEXT.__objc_methtype: 0x3d7
-  __TEXT.__gcc_except_tab: 0x790
-  __TEXT.__objc_methname: 0x1e10
+  __TEXT.__gcc_except_tab: 0x798
+  __TEXT.__objc_methname: 0x1ef2
   __TEXT.__constg_swiftt: 0x94
   __TEXT.__swift5_typeref: 0x78
   __TEXT.__swift5_reflstr: 0xd
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x438
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x480
+  __TEXT.__unwind_info: 0x440
+  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x8e0
-  __DATA_CONST.__cfstring: 0x1880
+  __DATA_CONST.__const: 0x908
+  __DATA_CONST.__cfstring: 0x1920
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x198
-  __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0xf28
-  __DATA.__objc_selrefs: 0xa18
+  __DATA.__objc_selrefs: 0xa50
   __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0x520
   __DATA.__data: 0x1a8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 280
-  Symbols:   376
-  CStrings:  891
+  Functions: 283
+  Symbols:   378
+  CStrings:  912
 
Symbols:
+ _OBJC_CLASS_$_OSASubmitter
+ _xpc_dictionary_get_double
CStrings:
+ "%@"
+ "313"
+ "999"
+ "Applying filter: only cleaning up logs created before %@"
+ "Applying filter: only cleaning up logs that contain header %@=%@"
+ "B16@?0@\"OSALog\"8"
+ "Cleaning up logs with bug type %@"
+ "Client (%d) is not entitled to clean up logs."
+ "Illegal log cleanup request (%d): bug type %@ is not supported"
+ "Illegal log cleanup request (%d): missing bug type"
+ "clear-logs-request"
+ "com.apple.private.osanalytics.cleanup-logs.allow"
+ "dateWithTimeIntervalSince1970:"
+ "fileCreationDate"
+ "filterByHeaders"
+ "filterByLogAge"
+ "handleLogCleanupRequest:fromConnection:forReply:"
+ "length"
+ "metaData"
+ "purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:"
+ "submissionPathsWithHomeDirectory:withProxies:"

```
