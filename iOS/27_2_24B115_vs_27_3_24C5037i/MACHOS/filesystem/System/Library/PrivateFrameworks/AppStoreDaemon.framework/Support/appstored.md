## appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_types2`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`

```diff

-13.1.17.0.0
-  __TEXT.__text: 0x552ab8
-  __TEXT.__auth_stubs: 0x48e0
-  __TEXT.__objc_stubs: 0x14cc0
-  __TEXT.__objc_methlist: 0xd6ec
+13.2.8.0.0
+  __TEXT.__text: 0x555a64
+  __TEXT.__auth_stubs: 0x4900
+  __TEXT.__objc_stubs: 0x14d00
+  __TEXT.__objc_methlist: 0xd6f4
   __TEXT.__dlopen_cstrs: 0x45e
-  __TEXT.__const: 0x26b80
-  __TEXT.__swift5_typeref: 0x35e0
+  __TEXT.__const: 0x26b88
+  __TEXT.__swift5_typeref: 0x35f4
   __TEXT.__objc_classname: 0x5283
-  __TEXT.__objc_methname: 0x1e38c
-  __TEXT.__objc_methtype: 0x8e59
+  __TEXT.__objc_methname: 0x1e4bc
+  __TEXT.__objc_methtype: 0x8e91
   __TEXT.__constg_swiftt: 0x2e94
-  __TEXT.__swift5_reflstr: 0x22d0
-  __TEXT.__swift5_fieldmd: 0x3040
+  __TEXT.__swift5_reflstr: 0x22e0
+  __TEXT.__swift5_fieldmd: 0x304c
   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_assocty: 0x498
-  __TEXT.__oslogstring: 0x3d804
-  __TEXT.__cstring: 0x21409
+  __TEXT.__oslogstring: 0x3dccd
+  __TEXT.__cstring: 0x21573
   __TEXT.__swift5_proto: 0x458
   __TEXT.__swift5_types: 0x34c
   __TEXT.__swift5_protos: 0x24

   __TEXT.__swift_as_cont: 0xa8c
   __TEXT.__swift5_mpenum: 0x54
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x8c5c
+  __TEXT.__gcc_except_tab: 0x8d48
   __TEXT.__ustring: 0x94
-  __TEXT.__unwind_info: 0xe3a0
+  __TEXT.__unwind_info: 0xe440
   __TEXT.__eh_frame: 0xea80
-  __DATA_CONST.__const: 0x298a0
-  __DATA_CONST.__cfstring: 0x1ad40
+  __DATA_CONST.__const: 0x299c8
+  __DATA_CONST.__cfstring: 0x1ae60
   __DATA_CONST.__objc_classlist: 0x15e0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x538

   __DATA_CONST.__objc_arraydata: 0x800
   __DATA_CONST.__objc_arrayobj: 0x420
   __DATA_CONST.__objc_dictobj: 0x168
-  __DATA_CONST.__auth_got: 0x2480
-  __DATA_CONST.__got: 0x1e80
+  __DATA_CONST.__auth_got: 0x2490
+  __DATA_CONST.__got: 0x1e88
   __DATA_CONST.__auth_ptr: 0xb28
-  __DATA.__objc_const: 0x33ca0
-  __DATA.__objc_selrefs: 0x6a58
-  __DATA.__objc_ivar: 0x22c4
-  __DATA.__objc_data: 0x108a8
-  __DATA.__data: 0x8640
+  __DATA.__objc_const: 0x33f50
+  __DATA.__objc_selrefs: 0x6a70
+  __DATA.__objc_ivar: 0x2314
+  __DATA.__objc_data: 0x108b0
+  __DATA.__data: 0x8650
   __DATA.__common: 0xcfc
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13814
-  Symbols:   2279
-  CStrings:  15110
+  Functions: 13848
+  Symbols:   2282
+  CStrings:  15154
 
Symbols:
+ _ASDUpdateItemMetricsBlockReason
+ _clock_gettime_nsec_np
+ _dispatch_walltime
CStrings:
+ "(PurchaseHistory) Failed reading removed apps' store item IDs: %{public}@"
+ "(PurchaseHistory) Failed to look up removed apps' store item IDs: %{public}@"
+ "(PurchaseHistory) Failed to read local revision for accountID: %{public}@ error: %{public}@"
+ ", ..."
+ "@\"DAAPURLRequest\""
+ "@\"PurchaseHistoryUpdateCommand\""
+ "@48@0:8q16B24@28@36B44"
+ "AB"
+ "AQ"
+ "B32@?0@\"ASDPurchaseHistoryApp\"8Q16^B24"
+ "Client did not reply to %@ request"
+ "Failed to create DAAP request"
+ "Failed to encode DAAP request body"
+ "Failed to encode DAAP request body: %{public}@"
+ "Internal auth finished for %{public}@"
+ "Items request authentication finished for %{public}@ error: %{public}@"
+ "Items request received 401 for %{public}@, presenting authentication"
+ "Purchase history update timed out"
+ "SELECT store_item_id FROM purchase_history_apps WHERE purchaser_dsid = ? AND locker_item_id IN (%@);"
+ "Unable to record update block reason without a bundle ID"
+ "Unable to record update block reason, no update exists for bundle ID: %{public}@"
+ "[%@] Allowing purchase history reload for accountID: %{public}@ clientID:%{public}@ last update: %{time_t}ld context: %{public}@"
+ "[%@] Blocking purchase history reload for accountID: %{public}@ clientID:%{public}@ last update: %{time_t}ld context: %{public}@ reason: %{public}@"
+ "[%@] Client %{public}@ did not reply to authentication request before timeout"
+ "[%@] Client %{public}@ did not reply to dialog request before timeout"
+ "[%@] Client %{public}@ did not reply to engagement request before timeout"
+ "[%@] Client com.apple.AppStore did not reply to authentication request before timeout"
+ "[%@] Client com.apple.AppStore did not reply to dialog request before timeout"
+ "[%@] Client com.apple.AppStore did not reply to engagement request before timeout"
+ "[%@] Ignoring %{public}@ reply from client %{public}@ that arrived after the timeout; timeout may be too short"
+ "[%@] Ignoring duplicate reply for accountID: %{public}@ error: %{public}@"
+ "[%@] Local revision %{public}@ behind server %{public}@, starting fetch items for accountID: %{public}@"
+ "[%@] Local revision %{public}@ not behind server %{public}@, setting last reload timestamp for accountID: %{public}@"
+ "[%@] No qualifying update requests remaining"
+ "[%@] No queued updates pending"
+ "[%@] Proceeding with purchase history reload, no previous reload time recorded for accountID: %{public}@ clientID:%{public}@ context: %{public}@"
+ "[%@] Query string for DAAP call is: %{public}@"
+ "[%@] Requesting server revision with local revision %{public}@"
+ "[%@] Server items request failed (%{public}@)"
+ "[%@] Server items request failed, no request context: %{public}@"
+ "[%@] Server items request started paginated: %{BOOL}d"
+ "[%@] Starting update command for accountID: %{public}@ context: %{public}@ queued: %lu"
+ "[%@] Update command completed, checking for next command"
+ "[%@] Update command failed: %{public}@, checking for next command"
+ "[%@] Update command stalled for %.0fs for accountID: %{public}@ context: %{public}@, abandoning it"
+ "[%@] Update is already running, waiting for it to finish"
+ "[%{public}@] Purchase History removed %lu itemIDs: [%{public}@]"
+ "[%{public}@] Purchase History updated from server (revision %@, %{public}s) with 0 changes"
+ "[%{public}@] Purchase History updated from server (revision %@, %{public}s): added or updated %lu itemIDs: [%{public}@]"
+ "_abandonReason"
+ "_abandoned"
+ "_activeRequestCanceller"
+ "_cancelled"
+ "_didReply"
+ "_lastActivityTime"
+ "_loggedLatestAddedApps"
+ "_loggedRemovedItemIDs"
+ "_numRemovedItemIDsFound"
+ "_runningCommand"
+ "_writeGroup"
+ "authentication"
+ "delta"
+ "dialog"
+ "engagement"
+ "evidForBundleID"
+ "full refresh"
+ "initWithAvailableUpdateCount:shouldNotifyOfChanges:bundleIDs:evidForBundleID:result:"
+ "seed"
+ "setBlockedBy:"
+ "setEvidForBundleID:"
+ "v24@?0@8@\"NSError\"16"
- "(PurchaseHistory) Local revision is %{public}@ for accountID: %{public}@ error: %{public}@"
- "@40@0:8q16B24@28B36"
- "Query string for DAAP call is: %{public}@"
- "[%@] Allowing purchase history reload for accountID: %{public}@ last update: %{time_t}ld context: %{public}@"
- "[%@] Blocking purchase history reload for accountID: %{public}@ last update: %{time_t}ld context: %{public}@ reason: %{public}@"
- "[%@] Decoded server revision: %@"
- "[%@] First query for purchase history items"
- "[%@] Proceeding with purchase history reload, no previous reload time recorded for accountID: %{public}@ context: %{public}@"
- "[%@] Push notification provided server revision: %@"
- "[%@] Sending notification for purchase history change"
- "[%@] Server items request failed (%@)"
- "[%@] Server items request failed, no request context: %@"
- "[%@] Server items request started"
- "[%@] Setting last reload timestamp for accountID: %{public}@"
- "[%@] Starting fetch items for accountID: %{public}@"
- "[%@] This is an update. Editing upon previous revision"
- "[%@] This is not an update. Clearing up purchase_history_apps first..."
- "[%{public}@] Purchase History updated from server (revision %@) with %ld changes"
- "[%{public}@] Purchase History updated from server (revision %@) with %ld changes: added {%@}; removed {%@}"
- "[%{public}@] Purchase History updated from server (revision %@) with 0 changes"
- "[PurchaseHistoryManager] No qualifying update requests remaining"
- "[PurchaseHistoryManager] No queued updates pending"
- "[PurchaseHistoryManager] Update command completed, checking for next command"
- "[PurchaseHistoryManager] Update command failed: %{public}@, checking for next command"
- "[PurchaseHistoryManager] Update is already running, waiting for it to finish"
- "gold"
- "initWithAvailableUpdateCount:shouldNotifyOfChanges:bundleIDs:result:"
```
