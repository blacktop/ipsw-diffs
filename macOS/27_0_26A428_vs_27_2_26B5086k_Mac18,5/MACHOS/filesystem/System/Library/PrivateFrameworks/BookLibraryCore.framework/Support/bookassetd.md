## bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

### Sections with Same Size but Changed Content

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
-  __TEXT.__text: 0xcd740
+2353.0.0.0.0
+  __TEXT.__text: 0xceed4
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_stubs: 0xb380
-  __TEXT.__objc_methlist: 0x5670
-  __TEXT.__const: 0xa639
-  __TEXT.__objc_classname: 0xb95
-  __TEXT.__objc_methname: 0xf7ca
-  __TEXT.__cstring: 0x327b
-  __TEXT.__objc_methtype: 0x2ded
-  __TEXT.__oslogstring: 0xa108
-  __TEXT.__gcc_except_tab: 0x1ae4
-  __TEXT.__unwind_info: 0x1ae8
+  __TEXT.__objc_stubs: 0xb5c0
+  __TEXT.__objc_methlist: 0x57a8
+  __TEXT.__const: 0xa649
+  __TEXT.__objc_classname: 0xbb3
+  __TEXT.__objc_methname: 0xfae8
+  __TEXT.__cstring: 0x350f
+  __TEXT.__objc_methtype: 0x2dfe
+  __TEXT.__oslogstring: 0xa209
+  __TEXT.__gcc_except_tab: 0x1d08
+  __TEXT.__unwind_info: 0x1b70
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__const: 0xa320
-  __DATA_CONST.__cfstring: 0x3280
-  __DATA_CONST.__objc_classlist: 0x2c0
+  __DATA_CONST.__const: 0xa3c0
+  __DATA_CONST.__cfstring: 0x3520
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x618
   __DATA_CONST.__got: 0x8d8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x9e00
-  __DATA.__objc_selrefs: 0x38b0
-  __DATA.__objc_ivar: 0x6a0
-  __DATA.__objc_data: 0x1b80
+  __DATA.__objc_const: 0xa038
+  __DATA.__objc_selrefs: 0x3950
+  __DATA.__objc_ivar: 0x6c0
+  __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0x1298
   __DATA.__common: 0x9ec
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2149
+  Functions: 2183
   Symbols:   496
-  CStrings:  3984
+  CStrings:  4040
 
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
+ "timeIntervalSinceNow"
+ "unrecognised stage %ld"
+ "v24@?0q8@\"NSString\"16"
+ "v40@0:8q16@24@32"
+ "writeToURL:options:error:"
- "T@\"NSMutableSet\",R,N,V_ongoingPurchaseRequestsByStoreID"
- "[Purchase-Mgr]: Skipping because there is ongoing purchase request for storeIdentifier=%@, buyParameters=%@"
- "checkAndAddStoreIDForRequest:"
- "writeToURL:atomically:"
```
