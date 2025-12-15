## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

```diff

-333.0.3.0.0
-  __TEXT.__text: 0x553e8
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_stubs: 0x31a0
-  __TEXT.__objc_methlist: 0x2088
-  __TEXT.__cstring: 0x7d8a
-  __TEXT.__objc_methname: 0x5602
+333.0.5.0.0
+  __TEXT.__text: 0x572b8
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_stubs: 0x3220
+  __TEXT.__objc_methlist: 0x20a8
+  __TEXT.__cstring: 0x8016
+  __TEXT.__objc_methname: 0x56ab
   __TEXT.__objc_classname: 0x2ea
-  __TEXT.__objc_methtype: 0x1648
+  __TEXT.__objc_methtype: 0x165d
   __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x1a9c
-  __TEXT.__oslogstring: 0x8b9f
-  __TEXT.__unwind_info: 0x1008
-  __DATA_CONST.__auth_got: 0x560
+  __TEXT.__gcc_except_tab: 0x1cac
+  __TEXT.__oslogstring: 0x9215
+  __TEXT.__unwind_info: 0x1050
+  __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc68
-  __DATA_CONST.__cfstring: 0x1320
+  __DATA_CONST.__const: 0xce0
+  __DATA_CONST.__cfstring: 0x1300
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA.__objc_const: 0x2c10
-  __DATA.__objc_selrefs: 0x1198
+  __DATA.__objc_selrefs: 0x11b0
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x430

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 614A7D92-6F91-3BE2-B527-2B0913495B25
-  Functions: 1274
-  Symbols:   261
-  CStrings:  2557
+  UUID: 60E4CAAA-B072-380E-B9BB-E91C7937DDA7
+  Functions: 1286
+  Symbols:   263
+  CStrings:  2590
 
Symbols:
+ _dispatch_resume
+ _dispatch_source_cancel
CStrings:
+ "%s"
+ "%s: CKKS response for known is Not good, retrun with error: %@"
+ "%s: CKKS response for known state is Likely good"
+ "%s: Checking CKKS state before storing Thread credentials with sync"
+ "%s: Error, Sync failure %@"
+ "%s: Exiting early - keychain add operation failed, handled duplicate/error scenario (error = %d)"
+ "%s: Failed to create CKKS control object: %@"
+ "%s: Failed to create keychain add dictionary - bad parameter: %@"
+ "%s: Operation already completed by another thread/callback, ignoring duplicate completion"
+ "%s: Returning from sync timeout handler after notifying completion with timeout error: %@"
+ "%s: Sync operation completion handler finished (syncDone=%d)"
+ "%s: Timer Fired, CKKS response for known is Not good as it timedout, retrun with error: %@"
+ "%s:%d Adding Thread network credentials to keychain with sync notification"
+ "%s:%d Initiated keychain add operation for Thread network credentials (network='%@', xpanid=%@, baId=%@, status=%d)"
+ "%s:%d Timer Fired for sync !!! "
+ "%s:%d _SecItemAddAndNotifyOnSync returned success, waiting for async completion"
+ "%s:%d sync is done, syncDone : %d"
+ "%s:%d: Delete current network result: (err=%d)"
+ "%s:%d: Error, Preferred network exists (name : %@, xpanid : %@)  ! But newly created netowrk (name : %@, xpanid : %@) doesn't match with it, let's delete this new network credentials.."
+ "%s:%d: Failed deleting current network credentials: %@"
+ "%s:%d: Request to delete current network for border agent %@"
+ "%s:%d: Timeout waiting for storeActiveDataSetRecordAndSyncWithErrComletion"
+ "%s:%d:Failed to get Preferred network after sync"
+ "%s:%d:Preferred Network exist, use it to start Thread"
+ "-[THThreadNetworkCredentialsKeychainBackingStore deleteCurrentNetworkFromRetrieveOrGenerate:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore performSyncOperationWithRecord:queue:timeoutValInSec:completion:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore performSyncOperationWithRecord:queue:timeoutValInSec:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore retrieveOrGeneratePreferredNetworkInternallyWithCompletion:]_block_invoke_2"
+ "-[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:]_block_invoke"
+ "Error: failed to sync store record (%s)\n"
+ "deleteCurrentNetworkFromRetrieveOrGenerate:"
+ "performSyncOperationWithRecord:queue:timeoutValInSec:completion:"
+ "storeActiveDataSetRecordAndSyncWithErrComletion:completion:"
+ "v44@0:8@16@24S32@?36"
- "Error while adding preferred network entry"

```
