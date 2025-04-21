## ProximityReaderDaemon

> `/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon`

```diff

-134.20.0.0.0
-  __TEXT.__text: 0x15d350
-  __TEXT.__auth_stubs: 0x48b0
+135.1.0.0.0
+  __TEXT.__text: 0x15c390
+  __TEXT.__auth_stubs: 0x48a0
   __TEXT.__objc_methlist: 0xda4
-  __TEXT.__const: 0x83d0
+  __TEXT.__const: 0x83e0
   __TEXT.__swift5_typeref: 0x26ac
-  __TEXT.__oslogstring: 0x79db
-  __TEXT.__cstring: 0x5d13
+  __TEXT.__oslogstring: 0x7bbb
+  __TEXT.__cstring: 0x5d03
   __TEXT.__swift5_reflstr: 0x33a3
   __TEXT.__swift5_assocty: 0x420
   __TEXT.__constg_swiftt: 0x379c

   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0xc
   __TEXT.__unwind_info: 0x4d30
-  __TEXT.__eh_frame: 0xbecc
+  __TEXT.__eh_frame: 0xbed4
   __TEXT.__objc_classname: 0x138
   __TEXT.__objc_methname: 0x22b7
   __TEXT.__objc_methtype: 0x345

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xbd0
   __DATA_CONST.__objc_protorefs: 0xf0
-  __AUTH_CONST.__auth_got: 0x2458
-  __AUTH_CONST.__auth_ptr: 0x9e8
+  __AUTH_CONST.__auth_got: 0x2450
+  __AUTH_CONST.__auth_ptr: 0x9f8
   __AUTH_CONST.__const: 0x89c0
   __AUTH_CONST.__objc_const: 0x50c8
   __AUTH.__objc_data: 0x11d0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5036
-  Symbols:   2162
+  Functions: 5034
+  Symbols:   2160
   CStrings:  1845
 
CStrings:
+ "\nENVIRONMENT: ------------------------------------\nsps: %{public}s %s\n-------------------------------------------------"
+ "%{public}s.%{public}s"
+ "Batch signature error: [ %s ]"
+ "Could not make Configurator module! Error: [ %s ]"
+ "Could not make Monitor module! Error: [ %s ]"
+ "Could not make PIN Controller module! Error: [ %s ]"
+ "Could not make Reader module! Error: [ %s ]"
+ "Could not register store: %s"
+ "Diagnostics mode = %{bool,public}d"
+ "Enable diagnostics error: [ %s ]"
+ "Error deleting all sessions: [ %s ]"
+ "Error deleting session: Error:[ %s ]"
+ "Error loading session: Error:[ %s ]"
+ "Error persisting session: Error:[ %s ]"
+ "Install error: [ %s ]"
+ "Kernel install failed with error: [ %@ ]"
+ "MerchantKit-135.1"
+ "Prepare error: [ %s ]"
+ "Primary account: %{sensitive}@)"
+ "Read Error: [ %@ ]"
+ "Secure reader blob error: [ %s ]"
+ "Status error: [ %s ]"
+ "Transaction signature error: [ %s ]"
+ "Unknown internal error"
+ "Unknown readCard error. Error: [ %s ]"
+ "[SessionTask] SAF is active, no refresh is needed"
+ "[SessionTask] boot id was updated"
+ "[SessionTask] could not parse session internal error: [ %s ]"
+ "[SessionTask] deleting previous SAF session"
+ "[SessionTask] error creating session, unexpected error: [ %s ]"
+ "[SessionTask] error creating session: [ %s ]"
+ "[SessionTask] error creating session: [ busy ]"
+ "[SessionTask] failed to build invalidSessionToken monitor event, merchantId was not found."
+ "[SessionTask] making sure no SAF session exists"
+ "[SessionTask] no online session was found, cannot create SAF session"
+ "[SessionTask] no previous SAF session to delete"
+ "[SessionTask] openSession API error: %s"
+ "[SessionTask] os version mismatch: %{public}s --> %{public}s"
+ "[SessionTask] preparing SAF session"
+ "[SessionTask] preparing online session"
+ "[SessionTask] reader is prepared"
+ "[SessionTask] readerValid: %{bool,public}d"
+ "[SessionTask] requesting reader to prepare, refresh: [ %{bool,public}d ] retry: [ %{bool,public}d ]"
+ "[SessionTask] sameProfile: %{bool,public}d"
+ "[SessionTask] session refresh failed, unexpected error: [ %s ]"
+ "[SessionTask] session refresh failed: [ %s ]"
+ "[SessionTask] session still valid"
+ "[SessionTask] session will be deleted, expired=%{bool,public}d, valid=%{bool,public}d, passcodeChanged=%{bool,public}d"
+ "[SessionTask] sessionStoreValid: %{bool,public}d"
+ "[SessionTask] skipping applet install"
+ "[SessionTask] stale: %{public}f"
+ "[SessionTask] unknown session type"
+ "[SessionTask] updating online session SAF active flag as [ false ]"
+ "[SessionTask] within24h: %{bool,public}d"
+ "[TransactionTask] PIN requested but not supported"
+ "[TransactionTask] PIN required but has error, returning"
+ "[TransactionTask] ReadEvent: [ %s ]"
+ "[TransactionTask] UI was dismissed and there is no active read, send readCancelled event"
+ "[TransactionTask] VAS only transaction, no data to be stored"
+ "[TransactionTask] already returned, skipping return data/error"
+ "[TransactionTask] building result"
+ "[TransactionTask] cardBlob encrypted"
+ "[TransactionTask] cardBlob failed"
+ "[TransactionTask] config needed, invalidating session"
+ "[TransactionTask] data returned with error: %@"
+ "[TransactionTask] existing session deleted: %s"
+ "[TransactionTask] failed to load session store after tapUIFinished"
+ "[TransactionTask] failed to prepare during retry: [ %@ ]"
+ "[TransactionTask] failed to refresh session: [ %@ ]"
+ "[TransactionTask] generating blob again, if needed"
+ "[TransactionTask] has error %@"
+ "[TransactionTask] has reader error %@"
+ "[TransactionTask] intercepting cancel request, read is not cancellable at current state"
+ "[TransactionTask] invalid reader mode"
+ "[TransactionTask] no session store"
+ "[TransactionTask] no transaction data"
+ "[TransactionTask] return data after tapUIFinished"
+ "[TransactionTask] returning SAF result with non-successful outcome"
+ "[TransactionTask] returning data early"
+ "[TransactionTask] returning data+PIN early"
+ "[TransactionTask] silent retry: %s"
+ "[TransactionTask] tapped via prox sensor"
+ "accountWasAdded"
+ "accountWasModified"
+ "accountWasRemoved"
+ "cancelRead error: [ %s ]"
+ "checking TaskManager busy: %{bool,public}d"
+ "context created for %{public}s"
+ "error preparing read session: [ %s ]"
+ "onUpdate: [ %s ]"
+ "onUpdate: failed to parse [ %s ]"
+ "pinDataReceived"
- "\nENVIRONMENT: ------------------------------------\nsps: %s %s\n-------------------------------------------------"
- "%{private}s.%{private}s"
- "Batch signature error: [ %{public}s ]"
- "Channel failure, nil api service"
- "Could not make Configurator module! Error: [ %{public}s ]"
- "Could not make Monitor module! Error: [ %{public}s ]"
- "Could not make PIN Controller module! Error: [ %{public}s ]"
- "Could not make Reader module! Error: [ %{public}s ]"
- "Could not parse session internal error: [ %@ ]"
- "Could not register store: %@"
- "Enable diagnostics error: [ %{public}s ]"
- "Error deleting all sessions: [ %{public}s ]"
- "Error deleting session: Error:[ %{public}s ]"
- "Error in result feature is enabled and an error is present in the result"
- "Error loading session: Error:[ %{public}s ]"
- "Error persisting session: Error:[ %{public}s ]"
- "Error trying to send invalidSessionToken monitor event, merchantId was not found."
- "Existing session invalidated (deleted) due to SPR fail - %s"
- "GeneralCardData: %{private}s"
- "Has PIN, returning data early"
- "Install error: [ %{public}s ]"
- "Intercepting cancel request, read is not cancellable at current state"
- "Invalid reader mode"
- "Kernel install failed with error: [ %{public}@ ]"
- "MerchantKit-134.20"
- "No PIN, returning data early"
- "PIN has been requested but PIN is not supported"
- "Prepare error: [ %{public}s ]"
- "Preparing SAF session"
- "Preparing online session"
- "Primary account: %{private}@)"
- "Read Error: [ %{public}@ ]"
- "ReadEvent: [ %{public}s ]"
- "Requires PIN, but has error, return data/error"
- "Secure reader blob error: [ %{public}s ]"
- "SessionTask | retry"
- "Status error: [ %{public}s ]"
- "The user performed a VAS transaction, no data to be stored"
- "Transaction signature error: [ %{public}s ]"
- "UI was dismissed and there is no active read, send readCancelled event"
- "Unknown readCard error. Error: [%{public}s]"
- "[SessionTask] Deleting previous SAF session"
- "[SessionTask] Making sure no SAF session exists"
- "[SessionTask] No online session was found, cannot create SAF session"
- "[SessionTask] No previous SAF session"
- "[SessionTask] Store and Forward is active, no refresh is needed"
- "[SessionTask] Updating online session SAF active flag as [ false ]"
- "[SessionTask] os version mismatch: %s --> %s"
- "[SessionTask] session refresh failed, unexpected error: [ %{public}s ]"
- "[SessionTask] session refresh failed: [ %{public}@ ]"
- "[TransactionTask] data returned with error: %s"
- "[TransactionTask] failed to prepare during retry: [ %{public}s ]"
- "[TransactionTask] failed to refresh session: [ %{public}@ ]"
- "accountWasAdded(%@)"
- "accountWasModified(%@)"
- "accountWasRemoved(%@)"
- "adapter isReaderValid threw %@"
- "adapter readerValid is %{bool}d"
- "boot id was updated in the TTP session"
- "building ReadResult"
- "cancelRead error: [ %{public}s ]"
- "checking TaskManager busy: %{bool}d"
- "configNeeded as reader error, invalidate session and continue normal error processing"
- "error creating session: [ %{public}@ ]"
- "error preparing read session: [ %{public}s ]"
- "failed to load session store after tapUIFinished"
- "generating blob again, if needed"
- "has reader error %s"
- "isReaderValid: %{bool}d"
- "no session store"
- "no transaction data"
- "onUpdate: [ %{public}s ]"
- "onUpdate: failed to parse [ %{public}s ]"
- "openSession API error: %{public}@"
- "os version: %s"
- "pinDataReceived:\n%{private}s"
- "preferredAIDList: %{private}s"
- "preserving, cc=%ld, stale=%f"
- "profile ok and not stale, skipping applet install"
- "reader is prepared"
- "requesting reader to prepare, refresh: [ %{bool}d ] retry: [ %{bool}d ]"
- "sameProfile: %{bool}d"
- "session still valid"
- "session will be deleted, expired=%{bool}d, valid=%{bool}d, passcodeChanged=%{bool}d"
- "sessionStoreValid: %{bool}d"
- "silent retry: %s"
- "staleInstallExpiry is nil, so consider stale"
- "status error: %@"
- "tapped via prox sensor"
- "terminalId = %s"
- "unknown session type"
- "within24h: %{bool}d"

```
