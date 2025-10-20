## storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

-815.1.14.0.0
-  __TEXT.__text: 0x2c9ad8
+815.1.15.0.0
+  __TEXT.__text: 0x2cf95c
   __TEXT.__auth_stubs: 0x38b0
-  __TEXT.__objc_stubs: 0xc460
-  __TEXT.__objc_methlist: 0x8294
-  __TEXT.__const: 0x221e0
+  __TEXT.__objc_stubs: 0xc540
+  __TEXT.__objc_methlist: 0x83e4
+  __TEXT.__const: 0x234f0
   __TEXT.__cstring: 0x14640
-  __TEXT.__oslogstring: 0xbb1a
-  __TEXT.__objc_classname: 0x1142
-  __TEXT.__objc_methname: 0x1244e
-  __TEXT.__objc_methtype: 0x3840
-  __TEXT.__gcc_except_tab: 0x2620
+  __TEXT.__oslogstring: 0xbb5a
+  __TEXT.__objc_classname: 0x116d
+  __TEXT.__objc_methname: 0x125c7
+  __TEXT.__objc_methtype: 0x3868
+  __TEXT.__gcc_except_tab: 0x2624
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x41b4

   __TEXT.__swift_as_entry: 0x5f4
   __TEXT.__swift_as_ret: 0x90c
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0xa278
-  __TEXT.__eh_frame: 0x12ccc
+  __TEXT.__unwind_info: 0xa2e0
+  __TEXT.__eh_frame: 0x12d34
   __DATA_CONST.__auth_got: 0x1c68
-  __DATA_CONST.__got: 0xda0
+  __DATA_CONST.__got: 0xd98
   __DATA_CONST.__auth_ptr: 0xc80
-  __DATA_CONST.__const: 0x1afd0
+  __DATA_CONST.__const: 0x1afc0
   __DATA_CONST.__cfstring: 0x5e00
-  __DATA_CONST.__objc_classlist: 0x5f0
+  __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x198
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1c380
-  __DATA.__objc_selrefs: 0x48a0
-  __DATA.__objc_ivar: 0x698
-  __DATA.__objc_data: 0x5218
-  __DATA.__data: 0x8ec0
-  __DATA.__bss: 0x1ec28
+  __DATA.__objc_const: 0x1c780
+  __DATA.__objc_selrefs: 0x48d8
+  __DATA.__objc_ivar: 0x6d4
+  __DATA.__objc_data: 0x52b8
+  __DATA.__data: 0x8ed0
+  __DATA.__bss: 0x1ecc8
   __DATA.__common: 0xde8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F8A41E3D-7D36-3ED2-AB86-82159F62B803
-  Functions: 14653
-  Symbols:   1569
-  CStrings:  7437
+  UUID: E9D0EF32-2343-350D-BDA9-6884DD707A78
+  Functions: 14690
+  Symbols:   1568
+  CStrings:  7460
 
Symbols:
- _OBJC_CLASS_$_NSBlockOperation
CStrings:
+ "11:08:35"
+ "@\"AppTransactionReadTask\""
+ "@44@0:8@16B24@28@36"
+ "AppTransactionReadTask"
+ "Oct 11 2025"
+ "T@\"AppTransactionReadTask\",&,N,V_appTransactionReadOperation"
+ "T@\"InAppReceiptDatabaseStore\",R,N,V_store"
+ "T@\"NSString\",R,N,V_appTransaction"
+ "TB,N,V_forceAuth"
+ "TB,R,N,V_ignoreCache"
+ "TB,R,N,V_needsSync"
+ "ValidateCacheTask"
+ "[%{public}@] Caching app transaction revision %ld for %{public}@"
+ "[%{public}@] No context available to force authentication"
+ "_appTransaction"
+ "_appTransactionReadOperation"
+ "_appTransactionSyncWithRevision:forceAuth:"
+ "_appTransactionsCompletionHandlers"
+ "_forceAuth"
+ "_ignoreCache"
+ "_needsSync"
+ "_store"
+ "appTransaction"
+ "appTransactionReadOperation"
+ "clearTransactionsForBundleID:"
+ "forceAuth"
+ "ignoreCache"
+ "initWithClient:ignoreCache:dbStore:syncQueue:"
+ "initWithClient:includeFinishedConsumables:dbStore:"
+ "needsSync"
+ "setAppTransactionReadOperation:"
+ "setForceAuth:"
+ "v28@0:8q16B24"
- "02:15:11"
- "@\"FetchReceiptTask\""
- "Oct  6 2025"
- "T@\"FetchReceiptTask\",&,N,V_appTransactionSyncTask"
- "[%{public}@] Caching app transaction for %{public}@"
- "_appTransactionSyncTask"
- "_appTransactionSyncWithRevision:dialogContext:logKey:completionHandler:"
- "addDependency:"
- "appTransactionSyncTask"
- "blockOperationWithBlock:"
- "setAppTransactionSyncTask:"

```
