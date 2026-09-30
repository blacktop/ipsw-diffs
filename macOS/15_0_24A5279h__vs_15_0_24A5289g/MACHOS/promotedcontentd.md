## promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

-541.0.0.0.0
-  __TEXT.__text: 0x23bb14
-  __TEXT.__auth_stubs: 0x2060
-  __TEXT.__objc_stubs: 0x16c40
-  __TEXT.__objc_methlist: 0x12b04
-  __TEXT.__const: 0x69dd0
-  __TEXT.__objc_methname: 0x228fb
-  __TEXT.__oslogstring: 0xbbfe
-  __TEXT.__cstring: 0xdb11
-  __TEXT.__objc_classname: 0x247f
-  __TEXT.__objc_methtype: 0x47a3
-  __TEXT.__gcc_except_tab: 0x1510
+545.0.0.0.0
+  __TEXT.__text: 0x23f518
+  __TEXT.__auth_stubs: 0x2080
+  __TEXT.__objc_stubs: 0x17080
+  __TEXT.__objc_methlist: 0x12d7c
+  __TEXT.__const: 0x69de0
+  __TEXT.__objc_methname: 0x22fec
+  __TEXT.__oslogstring: 0xbd6e
+  __TEXT.__cstring: 0xde5a
+  __TEXT.__objc_classname: 0x24b3
+  __TEXT.__objc_methtype: 0x4863
+  __TEXT.__gcc_except_tab: 0x15e0
   __TEXT.__constg_swiftt: 0x1cdc
-  __TEXT.__swift5_typeref: 0x138a
+  __TEXT.__swift5_typeref: 0x1386
   __TEXT.__swift5_fieldmd: 0x15a8
   __TEXT.__swift5_types: 0x1a8
   __TEXT.__swift5_reflstr: 0xc63

   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__info_plist: 0x550
-  __TEXT.__unwind_info: 0x4610
-  __TEXT.__eh_frame: 0xfa8
-  __DATA_CONST.__auth_got: 0x1040
-  __DATA_CONST.__got: 0xb10
-  __DATA_CONST.__auth_ptr: 0x660
-  __DATA_CONST.__const: 0x11870
-  __DATA_CONST.__cfstring: 0xdea0
-  __DATA_CONST.__objc_classlist: 0xb80
+  __TEXT.__info_plist: 0x55a
+  __TEXT.__unwind_info: 0x46f8
+  __TEXT.__eh_frame: 0x1018
+  __DATA_CONST.__auth_got: 0x1050
+  __DATA_CONST.__got: 0xb38
+  __DATA_CONST.__auth_ptr: 0x750
+  __DATA_CONST.__const: 0x11948
+  __DATA_CONST.__cfstring: 0xdf20
+  __DATA_CONST.__objc_classlist: 0xb98
   __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x258
+  __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x6f8
+  __DATA_CONST.__objc_protorefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x708
   __DATA_CONST.__linkguard: 0x15
-  __DATA_CONST.__objc_intobj: 0x16c8
+  __DATA_CONST.__objc_intobj: 0x16b0
   __DATA_CONST.__objc_arraydata: 0x6f8
   __DATA_CONST.__objc_dictobj: 0xa28
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x25a98
-  __DATA.__objc_selrefs: 0x85f0
-  __DATA.__objc_ivar: 0x142c
-  __DATA.__objc_data: 0x6d68
-  __DATA.__data: 0x5358
-  __DATA.__bss: 0x4a60
+  __DATA.__objc_const: 0x26010
+  __DATA.__objc_selrefs: 0x8738
+  __DATA.__objc_ivar: 0x1468
+  __DATA.__objc_data: 0x6e98
+  __DATA.__data: 0x5438
+  __DATA.__bss: 0x4a50
   __DATA.__common: 0xa80
   - /System/Library/Frameworks/AdServices.framework/Versions/A/AdServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/LimitAdTracking.framework/Versions/A/LimitAdTracking
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
+  - /System/Library/PrivateFrameworks/TestHookService.framework/Versions/A/TestHookService
+  - /System/Library/PrivateFrameworks/TestHookShared.framework/Versions/A/TestHookShared
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8140
-  Symbols:   1974
-  CStrings:  2253
+  Functions: 8210
+  Symbols:   1980
+  CStrings:  2272
 
Symbols:
+ _OBJC_CLASS_$_APTestHookID
+ _OBJC_CLASS_$_APTestHookMetadata
+ _OBJC_CLASS_$_APTestHookSender
+ _OBJC_CLASS_$_APTimeSpentEntry
+ _OBJC_CLASS_$_APTimeSpentLegacyInterface
+ _OBJC_CLASS_$_APTimeSpentStoreDatabase
+ _OBJC_METACLASS_$_APTimeSpentEntry
+ _OBJC_METACLASS_$_APTimeSpentLegacyInterface
+ _OBJC_METACLASS_$_APTimeSpentStoreDatabase
- _NSLog
- _OBJC_CLASS_$_APAdAccumulatorSettings
- _OBJC_METACLASS_$_APAdAccumulatorSettings
CStrings:
+ "@32@0:8@16@24"
+ "APTimeSpentEntry"
+ "APTimeSpentStoreDatabase"
+ "DELETE FROM TimeSpent WHERE contentId IN ("
+ "ExpiredAnonId"
+ "INSERT OR REPLACE INTO TimeSpent(contentId,timeStamp) VALUES (?,?)"
+ "ManagedContentNotFound"
+ "ManagedContextNotFound"
+ "SELECT * FROM TimeSpent WHERE timestamp <= ?"
+ "T@\"NSDate\",N,R"
+ "T@\"NSString\",N,R"
+ "TimeSpentDailyRequester"
+ "Trying to send time spent metric for promoted content with content id: %!@(MISSING), but couldn't find it or user account changed."
+ "[TimeSpentDatabase] Removing entry for contentId: %!{(MISSING)public}@"
+ "[TimeSpentDatabase] Retrieving entry for contentId: %!{(MISSING)public}@ and timeStamp: %!{(MISSING)public}@"
+ "[TimeSpentDatabase] Storing entry for contentId: %!{(MISSING)public}@ and timeStamp: %!{(MISSING)public}@"
+ "__ObjC.APTimeSpentEntry"
+ "__ObjC.APTimeSpentStoreDatabase"
+ "com.apple.ap.promotedcontentd.timespent"
+ "com.apple.ap.promotedcontentd.timespentactivity.queue"
+ "contentId"
+ "timeInterval"
+ "v20@?0B8@\"NSString\"12"
- "Can't construct Array with count < 0"
- "SELECT name FROM sqlite_master WHERE type='table' AND name='event_%!l(MISSING)d'"
- "SIGTERM, Bye bye."
- "Swift/Array.swift"

```
