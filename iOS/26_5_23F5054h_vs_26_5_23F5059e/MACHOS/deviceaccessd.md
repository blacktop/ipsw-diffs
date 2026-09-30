## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-325.12.1.0.0
-  __TEXT.__text: 0x84bf4
-  __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_stubs: 0x7d40
-  __TEXT.__objc_methlist: 0x2650
-  __TEXT.__const: 0x1a88
-  __TEXT.__cstring: 0x14804
+325.14.0.0.0
+  __TEXT.__text: 0x86850
+  __TEXT.__auth_stubs: 0x1f50
+  __TEXT.__objc_stubs: 0x7dc0
+  __TEXT.__objc_methlist: 0x2660
+  __TEXT.__const: 0x1b40
+  __TEXT.__cstring: 0x14c04
   __TEXT.__objc_classname: 0x435
-  __TEXT.__gcc_except_tab: 0x3fe4
-  __TEXT.__objc_methname: 0x9ffa
+  __TEXT.__gcc_except_tab: 0x40b0
+  __TEXT.__objc_methname: 0xa09e
   __TEXT.__objc_methtype: 0x1aea
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__swift5_typeref: 0x90a
-  __TEXT.__swift5_fieldmd: 0x460
+  __TEXT.__swift5_typeref: 0x90e
+  __TEXT.__swift5_fieldmd: 0x478
   __TEXT.__constg_swiftt: 0x3e4
-  __TEXT.__swift5_reflstr: 0x4da
+  __TEXT.__swift5_reflstr: 0x4ea
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_capture: 0x494
-  __TEXT.__oslogstring: 0xa77
+  __TEXT.__swift5_capture: 0x4d0
+  __TEXT.__oslogstring: 0xb97
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_proto: 0x58
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x19b8
-  __TEXT.__eh_frame: 0xbe0
-  __DATA_CONST.__auth_got: 0xfa0
-  __DATA_CONST.__got: 0x858
+  __TEXT.__unwind_info: 0x1a18
+  __TEXT.__eh_frame: 0xd70
+  __DATA_CONST.__auth_got: 0xfb8
+  __DATA_CONST.__got: 0x880
   __DATA_CONST.__auth_ptr: 0x290
-  __DATA_CONST.__const: 0x25d8
+  __DATA_CONST.__const: 0x2690
   __DATA_CONST.__cfstring: 0x2200
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x3620
-  __DATA.__objc_selrefs: 0x26a8
+  __DATA.__objc_const: 0x3660
+  __DATA.__objc_selrefs: 0x26c8
   __DATA.__objc_ivar: 0x2f0
   __DATA.__objc_data: 0x8c0
-  __DATA.__data: 0x1340
-  __DATA.__bss: 0xd98
+  __DATA.__data: 0x1358
+  __DATA.__bss: 0xdb8
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88993635-96B0-39DB-8661-F880D80CC12D
-  Functions: 2371
-  Symbols:   847
-  CStrings:  4176
+  UUID: E07B56CB-7939-3F21-96A7-307F8B38F5E5
+  Functions: 2408
+  Symbols:   853
+  CStrings:  4203
 
Symbols:
+ _$sSuN
+ _$sSuSEsWP
+ _$sSuSesWP
+ _DAExtensionTypeToTransportType
+ _DATransportTypeToExtensionType
+ _dispatch_group_wait
CStrings:
+ "### Failed to cleanup expired messages: %@"
+ "### Failed to create directory at "
+ "### Failed to delete all incoming messages: %@"
+ "### Failed to delete all outgoing messages: %@"
+ "### Failed to delete all transport priorities: %@"
+ "### Failed to delete incoming messages %s: %@"
+ "### Failed to delete outgoing messages %s: %@"
+ "### Failed to delete transport priority for %s: %@"
+ "### Failed to fetch all outgoing messages: %@"
+ "### Failed to fetch existing messages for queueOneIdentifier %s: %@"
+ "### Failed to fetch incoming message %s: %@"
+ "### Failed to fetch outgoing message withID %s: %@"
+ "### Failed to fetch outgoing message: %s with transport priority %ld: %@"
+ "### Failed to fetch pending incoming messages: %@"
+ "### Failed to fetch pending outgoing messages: %@"
+ "### Failed to fetch transport priority for %s: %@"
+ "### Failed to find capabilityID for %@: %@"
+ "### Failed to initialize ModelContainer: %@"
+ "### Failed to store incoming message %@: %@"
+ "### Failed to store outgoing message %@: %@"
+ "### Failed to store outgoing message: %@, %@"
+ "### Failed to store transport priority for %s: %@"
+ "### Failed to update outgoing message delivery status for %s: %@"
+ "### Failed to update outgoing message retry count for %s: %@"
+ "### Failed updateRetry on messageID %@: %@"
+ "### PersistDataEvent: timed out waiting for message store"
+ "### PushServiceManager: could not convert encrypted message string to data: %@#"
+ "### RetryEvent: transport type is unknown"
+ "-[DADaemonServer _activateFirstUnlockHandler]_block_invoke"
+ "-[DAExtensionCoordinator _flushPendingOutgoingMessages:]"
+ "-[DAExtensionCoordinator _flushPendingOutgoingMessages:]_block_invoke"
+ "-[DAExtensionCoordinator _flushPendingOutgoingMessages:]_block_invoke_2"
+ "-[DAExtensionCoordinator _flushPendingOutgoingMessages:]_block_invoke_3"
+ "-[DAExtensionCoordinator _handleEventDataDeliveryFailure:error:]"
+ "-[DAExtensionCoordinator _handleEventDataProvider:]"
+ "-[DAExtensionCoordinator _retryEvent:toExtensionType:withTransportType:error:]_block_invoke_2"
+ "Asserting extensions: %@"
+ "DataDeliveryFailure: No available transports for %@"
+ "DataProvider: No available transports for %@"
+ "Deleted message"
+ "Deleted message with missing featureID"
+ "Deleting expired message: %@"
+ "Deleting message with nil featureID: %@"
+ "FlushPending: %@"
+ "FlushPending: fetched %lu outgoing messages for '%@'"
+ "Found capabilityID: %@"
+ "Payload does not have an encrypted message: %@"
+ "Reporting event to %@: %@"
+ "Stored incoming message: %@"
+ "Transport extension is not ready to receive event: %@"
+ "Updated retry count for outgoing messageID: %@"
+ "Updated retry count to %ld for %ld outgoing message(s) with ID: %s"
+ "_flushPendingOutgoingMessages:"
+ "_transportType"
+ "_transportTypeBest"
+ "_transportTypeBest:"
+ "capabilityInfoMapForBundleID:capabilityFlags:"
+ "encryptedData"
+ "fetch failed with error: %@"
+ "message has surpassed retry count %lu: %@"
+ "no extensions found for %@"
+ "perAppToken"
+ "sessionIdentifier"
+ "setTransportType:"
+ "updateOutgoingMessageRetryCountWithMessageID:retryCount:completion:"
- "### Failed to store messages for %@: %@"
- "### RetryEvent: transportType is nil"
- "-[DADaemonServer _update]_block_invoke"
- "-[DAExtensionCoordinator _flushPendingOutgoingMessages]"
- "-[DAExtensionCoordinator _flushPendingOutgoingMessages]_block_invoke"
- "Asserting extension: %@"
- "Could not convert encryptedMessage string to data"
- "Failed to create directory at "
- "Failed to delete all transport priorities: %@"
- "Failed to delete incoming messages %s: %@"
- "Failed to delete outgoing messages %s: %@"
- "Failed to delete transport priority for %s: %@"
- "Failed to fetch all outgoing messages: %@"
- "Failed to fetch existing messages for queueOneIdentifier %s: %@"
- "Failed to fetch incoming message %s: %@"
- "Failed to fetch outgoing message %s with transport priority %ld: %@"
- "Failed to fetch outgoing message %s: %@"
- "Failed to fetch pending incoming messages: %@"
- "Failed to fetch transport priority for %s: %@"
- "Failed to initialize ModelContainer: %@"
- "Failed to store incoming message %s: %@"
- "Failed to store outgoing message %s: %@"
- "Failed to store transport priority for %s: %@"
- "Failed to update outgoing message delivery status for %s: %@"
- "Persisting message: %@"
- "Reporting event to configuration %@: %@"
- "RetryWithDelay: message %@ is still in store"
- "Stored incoming message: %s"
- "Stored outgoing message: %s"
- "_currentTransportExtensionType"
- "_currentTransportType"
- "_flushPendingOutgoingMessages"
- "encryptedMessage"
- "no extension found for %@"

```
