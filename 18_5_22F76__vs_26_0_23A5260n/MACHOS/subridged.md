## subridged

> `/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/Support/subridged`

```diff

-350.100.2.0.0
-  __TEXT.__text: 0x1976c
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0x2220
-  __TEXT.__objc_methlist: 0x11b4
-  __TEXT.__const: 0x510
-  __TEXT.__gcc_except_tab: 0x2e4
-  __TEXT.__cstring: 0x292c
-  __TEXT.__oslogstring: 0x2639
-  __TEXT.__objc_classname: 0x153
-  __TEXT.__objc_methtype: 0xe8d
-  __TEXT.__objc_methname: 0x3a84
-  __TEXT.__unwind_info: 0x4f0
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x10f0
-  __DATA_CONST.__cfstring: 0x1a60
+364.0.0.0.0
+  __TEXT.__text: 0x183e4
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_stubs: 0x2300
+  __TEXT.__objc_methlist: 0x1274
+  __TEXT.__const: 0x500
+  __TEXT.__gcc_except_tab: 0x314
+  __TEXT.__cstring: 0x24ca
+  __TEXT.__oslogstring: 0x28fe
+  __TEXT.__objc_classname: 0x156
+  __TEXT.__objc_methtype: 0xedc
+  __TEXT.__objc_methname: 0x3cf4
+  __TEXT.__unwind_info: 0x530
+  __DATA_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__const: 0x1178
+  __DATA_CONST.__cfstring: 0x1b40
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1fe0
-  __DATA.__objc_selrefs: 0xd88
-  __DATA.__objc_ivar: 0x124
+  __DATA.__objc_const: 0x2100
+  __DATA.__objc_selrefs: 0xdf8
+  __DATA.__objc_ivar: 0x13c
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x428
-  __DATA.__bss: 0xa0
-  __DATA.__common: 0x10
+  __DATA.__data: 0x438
+  __DATA.__bss: 0xc8
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9689A7BF-33A4-30C1-B64E-2F5B46E955A6
-  Functions: 490
-  Symbols:   231
-  CStrings:  1455
+  UUID: C008095B-30AE-3529-89BB-ECC337015DDB
+  Functions: 493
+  Symbols:   238
+  CStrings:  1491
 
Symbols:
+ _CFPreferencesCopyValue
+ _OBJC_CLASS_$_SUCoreDescriptor
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _kCFPreferencesAnyHost
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
CStrings:
+ "\n            terms: %s userInstallRequestType: %s installTonightScheduled: %s displayTermsRequested: %s\n            ProductVersion: %@\n            ProductBuildVersion: %@\n            ProductSystemName: %@\n            Publisher: %@\n            DownloadSize: %lld\n            PreparationSize: %lld\n            InstallationSize: %lld\n            TotalRequiredFreeSpace: %lld\n            DocumentationID: %@\n            MarketingVersion: %@\n            CurrentDenialReasons: %@\n            OSName: %@\n            Manifest Length: %lu\n             Terms Length: %lu\n            Release Note Length: %lu\n            Release Note Summary Length: %lu \n            SUIconPresent: %@\n             Power Policy: %@\n             CoreDescriptor: %@"
+ "%s"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"SUCoreDescriptor\""
+ "@32@0:8@16Q24"
+ "Found default for simulator file %@"
+ "InternalBuild"
+ "Not present"
+ "Present"
+ "Q"
+ "SUCoreDescriptor"
+ "SetSimulationFile"
+ "SimulationFileName"
+ "StandAloneGizmoMode"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_timerOperationsQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_timerSource"
+ "T@\"NSString\",&,N,V_transactionName"
+ "T@\"SUCoreDescriptor\",&,N,V_coreDescriptor"
+ "TB,N,V_isStalled"
+ "TQ,N,V_maxTransactionTimeout"
+ "[SUBTransaction]: Invalidating transaction %@ due to to timeout"
+ "[SUBtransaction]: TX ⬆: Total: %lu Current: %@"
+ "[SUBtransaction]: TX ⬇: Total: %lu Current: %@"
+ "[ScanResultHandler]: Forwarding ScanResult to bridge after documentation check"
+ "[ScanResultHandler]: Scan returned error %{public}@. Forwarding ScanResult to bridge without documentation checks"
+ "[ScanResultHandler]: Scan returned result as up to date. Clearing badge"
+ "[SendClouldMessageToCompanion]: Failed to determine IDS identifier for cloudService device. Not forwarding message of type %@"
+ "[SendClouldMessageToCompanion]: No IDS device was found via cloudService. Not forwarding message of type %@"
+ "[SendClouldMessageToCompanion]: Sending message %@ to ids device: %@"
+ "_coreDescriptor"
+ "_isStalled"
+ "_maxTransactionTimeout"
+ "_timerOperationsQueue"
+ "_timerSource"
+ "_transactionName"
+ "com.apple.nanosubridged.timerqueue"
+ "coreDescriptor"
+ "getPendingTransactions"
+ "getPendingTransactionsCount"
+ "initWithNameAndTimeout:timeOut:"
+ "maxTransactionTimeout"
+ "mobile"
+ "setCoreDescriptor:"
+ "setIsStalled:"
+ "setMaxTransactionTimeout:"
+ "setTimerOperationsQueue:"
+ "setTimerSource:"
+ "setTransactionName:"
+ "timerOperationsQueue"
+ "timerSource"
+ "transactionName"
+ "v24@0:8Q16"
- "\n            terms: %s userInstallRequestType: %s installTonightScheduled: %s displayTermsRequested: %s\n            ProductVersion: %@\n            ProductBuildVersion: %@\n            ProductSystemName: %@\n            Publisher: %@\n            DownloadSize: %lld\n            PreparationSize: %lld\n            InstallationSize: %lld\n            TotalRequiredFreeSpace: %lld\n            DocumentationID: %@\n            MarketingVersion: %@\n            CurrentDenialReasons: %@\n            OSName: %@\n            Manifest Length: %lu\n             Terms Length: %lu\n            Release Note Length: %lu\n            Release Note Summary Length: %lu \n            SUIconPresent: %@\n             Power Policy: %@"
- "-[SUBMessageEndpoint _checkConnectivityForQueuedDisconnectedBlocks]_block_invoke"
- "-[SUBMessageEndpoint _sendCloudMessage:isCritical:useTimeout:destinations:completion:]_block_invoke"
- "-[SUBMessageEndpoint _sendCloudMessage:isCritical:useTimeout:withReply:destinations:]_block_invoke"
- "-[SUBMessageEndpoint _sendMessage:isCritical:useTimeout:completion:]_block_invoke"
- "-[SUBMessageEndpoint _sendMessage:isCritical:useTimeout:withReply:]_block_invoke"
- "-[SUBMessageEndpoint executeBlockWhenDisconnected:]_block_invoke"
- "-[SUBMessageEndpoint handleMessage:withContext:]_block_invoke"
- "-[SUBMessageEndpoint resume]_block_invoke"
- "-[SUBMessageEndpoint sendCloudMessage:isCritical:useTimeout:destinations:completion:]_block_invoke"
- "-[SUBMessageEndpoint sendCloudMessage:isCritical:useTimeout:withReply:destinations:]_block_invoke"
- "-[SUBMessageEndpoint sendErrorReply:toMessage:isCritical:]_block_invoke"
- "-[SUBMessageEndpoint sendMessage:isCritical:useTimeout:completion:]_block_invoke"
- "-[SUBMessageEndpoint sendMessage:isCritical:useTimeout:withReply:]_block_invoke"
- "-[SUBMessageEndpoint sendReply:toMessage:isCritical:]_block_invoke"
- "-[SUBMessageEndpoint service:account:identifier:didSendWithSuccess:error:]_block_invoke"
- "-[SUBMessageEndpoint suspend]_block_invoke"
- "SUBMessageEndpoint.m"
- "SUBTransactionBegin"
- "TX ⬆: %ld %s %s %d"
- "TX ⬇: %ld SUBTransactionEnd %d %@"
- "UnknownObject"
- "tcount >= 0"

```
