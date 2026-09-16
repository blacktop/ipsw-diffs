## bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-2310.0.0.0.0
-  __TEXT.__text: 0xdfae4
+2353.0.0.0.0
+  __TEXT.__text: 0xe1054
   __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_stubs: 0xd340
-  __TEXT.__objc_methlist: 0x6350
+  __TEXT.__objc_stubs: 0xd560
+  __TEXT.__objc_methlist: 0x6480
   __TEXT.__const: 0xdb00
-  __TEXT.__objc_classname: 0xd5d
-  __TEXT.__cstring: 0x3850
-  __TEXT.__objc_methname: 0x118ce
-  __TEXT.__oslogstring: 0xc53a
-  __TEXT.__objc_methtype: 0x3198
-  __TEXT.__gcc_except_tab: 0x1854
+  __TEXT.__objc_classname: 0xd7b
+  __TEXT.__cstring: 0x3ae1
+  __TEXT.__objc_methname: 0x11bd7
+  __TEXT.__oslogstring: 0xc63b
+  __TEXT.__objc_methtype: 0x31a9
+  __TEXT.__gcc_except_tab: 0x1a18
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x1e70
+  __TEXT.__unwind_info: 0x1ee8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x7e10
-  __DATA_CONST.__cfstring: 0x3820
-  __DATA_CONST.__objc_classlist: 0x328
+  __DATA_CONST.__const: 0x7ea0
+  __DATA_CONST.__cfstring: 0x3ac0
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x6f0
   __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0xb2a0
-  __DATA.__objc_selrefs: 0x40d8
-  __DATA.__objc_ivar: 0x778
-  __DATA.__objc_data: 0x1f90
+  __DATA.__objc_const: 0xb4d8
+  __DATA.__objc_selrefs: 0x4170
+  __DATA.__objc_ivar: 0x798
+  __DATA.__objc_data: 0x1fe0
   __DATA.__data: 0x1730
   __DATA.__common: 0xab8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2407
+  Functions: 2440
   Symbols:   589
-  CStrings:  4571
+  CStrings:  4626
 
CStrings:
+ "(dID=%{public}@) [Database]: No sinf.xml written; no epubRightsData supplied."
+ "(dID=%{public}@) [Purchase-Mgr]: No sinf.xml written; no epubRightsData supplied."
+ "AMS purchase finished, posting result"
+ "AMS purchase started, no result yet"
+ "BLPurchaseManager.ongoingPurchaseRequests"
+ "No FairPlay rights data (sinf) was supplied for the download; nothing to write."
+ "T@\"BUOSStateHandler\",&,N,V_ongoingPurchaseStateHandler"
+ "T@\"NSDate\",&,N,V_startDate"
+ "T@\"NSMutableDictionary\",R,N,V_ongoingPurchaseRequestsByStoreID"
+ "T@\"NSNumber\",&,N,V_stageAttributionStoreID"
+ "T@\"NSString\",C,N,V_lastStageLogKey"
+ "T@?,C,N,V_stageReporter"
+ "Tq,N,V_lastStage"
+ "[Purchase-Mgr]: Skipping because there is ongoing purchase request for storeIdentifier=%{mask.hash}@ (age %{public}.0fs, last stage: %{public}@, logKey %{public}@, downloadID %{public}@), buyParameters=%@"
+ "_BLOngoingPurchaseRequestInfo"
+ "_lastStage"
+ "_lastStageLogKey"
+ "_ongoingPurchaseStateHandler"
+ "_reportStage:logKey:"
+ "_stageAttributionStoreID"
+ "_stageReporter"
+ "_startDate"
+ "accepted, not yet enqueued to AMS"
+ "ageSeconds"
+ "auth answered, back inside AMS"
+ "auth forwarded, awaiting reply"
+ "checkAndAddStoreIDForRequest:existingSnapshot:"
+ "dialog answered, back inside AMS"
+ "dialog forwarded, awaiting reply"
+ "dq_noteStage:logKey:forStoreID:"
+ "engagement answered, back inside AMS"
+ "engagement forwarded, awaiting reply"
+ "inFlightPurchases"
+ "lastStage"
+ "lastStageLogKey"
+ "none"
+ "none recorded yet"
+ "noteAMSPurchaseFinishedForRequest:"
+ "noteAMSPurchaseStartedForRequest:downloadID:"
+ "noteStage:forRequest:"
+ "noteStageForAttributedRequest:logKey:"
+ "ongoingPurchaseStateHandler"
+ "payment sheet answered, back inside AMS"
+ "payment sheet forwarded, awaiting reply"
+ "post-AMS, triggering downloads"
+ "setLastStage:"
+ "setLastStageLogKey:"
+ "setOngoingPurchaseStateHandler:"
+ "setStageAttributionStoreID:"
+ "setStageReporter:"
+ "setStartDate:"
+ "stageAttributionStoreID"
+ "stageReporter"
+ "startDate"
+ "stateSnapshotForLog"
+ "unrecognised stage %ld"
+ "v24@?0q8@\"NSString\"16"
+ "v40@0:8q16@24@32"
+ "writeToURL:options:error:"
- "T@\"NSMutableSet\",R,N,V_ongoingPurchaseRequestsByStoreID"
- "[Purchase-Mgr]: Skipping because there is ongoing purchase request for storeIdentifier=%@, buyParameters=%@"
- "checkAndAddStoreIDForRequest:"
- "writeToURL:atomically:"
```
