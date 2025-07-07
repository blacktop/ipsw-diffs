## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-140.12.4.0.0
-  __TEXT.__text: 0x49b1c
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x2ab4
+140.26.102.0.0
+  __TEXT.__text: 0x4a268
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_methlist: 0x2b14
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x4f3f
-  __TEXT.__oslogstring: 0x26de
+  __TEXT.__cstring: 0x4f95
+  __TEXT.__oslogstring: 0x2754
   __TEXT.__gcc_except_tab: 0x43c
   __TEXT.__dlopen_cstrs: 0x10b
-  __TEXT.__unwind_info: 0xe04
+  __TEXT.__unwind_info: 0xe24
   __TEXT.__objc_classname: 0x70f
-  __TEXT.__objc_methname: 0x82c1
-  __TEXT.__objc_methtype: 0x18a0
-  __TEXT.__objc_stubs: 0x50a0
-  __DATA_CONST.__got: 0x158
+  __TEXT.__objc_methname: 0x83dd
+  __TEXT.__objc_methtype: 0x18bf
+  __TEXT.__objc_stubs: 0x5200
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0xf70
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8f38
-  __DATA_CONST.__objc_selrefs: 0x19f8
+  __DATA_CONST.__objc_const: 0x8f48
+  __DATA_CONST.__objc_selrefs: 0x1a60
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__cfstring: 0x3c60
+  __AUTH_CONST.__cfstring: 0x3ce0
   __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__objc_const: 0x1898
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__auth_got: 0x6a8
   __AUTH.__objc_data: 0x640
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x300
+  __DATA.__objc_classrefs: 0x318
   __DATA.__objc_superrefs: 0x158
   __DATA.__objc_ivar: 0x340
   __DATA.__data: 0x5e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74AA9074-84A9-3B18-AEAC-171F01C93BC3
-  Functions: 1627
-  Symbols:   5334
-  CStrings:  2736
+  UUID: D4FE2CC5-7675-378D-B9A7-72758766D55F
+  Functions: 1636
+  Symbols:   5368
+  CStrings:  2762
 
Symbols:
+ +[PRSPosterArchiver markURLPurgableAfterOneHour:error:]
+ +[PRSPosterArchiver markURLPurgableAfterOneHour:error:].cold.1
+ -[NSURL(PRSAdditions) prs_URLExists:]
+ -[NSURL(PRSAdditions) prs_isDirectory]
+ -[NSURL(PRSAdditions) prs_isPurgable]
+ -[NSURL(PRSAdditions) prs_setPurgable:afterDate:error:]
+ -[NSURL(PRSAdditions) prs_unmarkAsPurgable]
+ -[NSURL(PRSAdditions) prs_unmarkAsPurgable].cold.1
+ -[PRSServerPosterIdentity stablePersistenceIdentifier]
+ -[PRSServerPosterPath stablePersistenceIdentifier]
+ _NSURLFileResourceTypeDirectory
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateComponents
+ _fsctl
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$date
+ _objc_msgSend$dateByAddingComponents:toDate:options:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$markURLPurgableAfterOneHour:error:
+ _objc_msgSend$prs_isDirectory
+ _objc_msgSend$prs_setPurgable:afterDate:error:
+ _objc_msgSend$prs_unmarkAsPurgable
+ _objc_msgSend$setHour:
+ _objc_msgSend$stablePersistenceIdentifier
+ _objc_msgSend$timeIntervalSince1970
- __Z18PRSArchiverZipDataP5NSURLP13NSFileManager.cold.24
CStrings:
+ "%@_%@_%@(%@)_%@_%llu-%llu"
+ "%@_%@_%@_%@_%llu-%llu"
+ "B24@0:8^B16"
+ "B36@0:8B16@20o^@28"
+ "Error marking '%@' as purgable %@ - %d"
+ "Error marking '%@' as purgable - %d"
+ "Failed to mark URL as purgable: %{public}@"
+ "NSURL_PRSAdditions.m"
+ "[self isFileURL]"
+ "currentCalendar"
+ "date"
+ "dateByAddingComponents:toDate:options:"
+ "fileExistsAtPath:isDirectory:"
+ "markURLPurgableAfterOneHour:error:"
+ "prs_URLExists:"
+ "prs_isDirectory"
+ "prs_isPurgable"
+ "prs_setPurgable:afterDate:error:"
+ "prs_unmarkAsPurgable"
+ "setHour:"
+ "stablePersistenceIdentifier"
+ "timeIntervalSince1970"

```
