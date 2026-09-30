## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-166.12.0.1.0
-  __TEXT.__text: 0x1b0f0
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x159c
+166.15.0.0.0
+  __TEXT.__text: 0x1b950
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x15ec
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x610
-  __TEXT.__cstring: 0xc47
-  __TEXT.__oslogstring: 0x3627
+  __TEXT.__gcc_except_tab: 0x5dc
+  __TEXT.__cstring: 0xc4e
+  __TEXT.__oslogstring: 0x344e
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x740
-  __TEXT.__objc_classname: 0x46b
-  __TEXT.__objc_methname: 0x48ec
-  __TEXT.__objc_methtype: 0x1098
-  __TEXT.__objc_stubs: 0x3d20
-  __DATA_CONST.__got: 0x270
+  __TEXT.__unwind_info: 0x730
+  __TEXT.__objc_classname: 0x46d
+  __TEXT.__objc_methname: 0x499c
+  __TEXT.__objc_methtype: 0x10a7
+  __TEXT.__objc_stubs: 0x3dc0
+  __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0x9c0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1190
+  __DATA_CONST.__objc_selrefs: 0x11c0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xa00
-  __AUTH_CONST.__objc_const: 0x3010
+  __AUTH_CONST.__cfstring: 0xa20
+  __AUTH_CONST.__objc_const: 0x3050
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x240
+  __DATA.__objc_ivar: 0x248
   __DATA.__data: 0x720
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 616
-  Symbols:   856
-  CStrings:  1316
+  Functions: 630
+  Symbols:   871
+  CStrings:  1330
 
Symbols:
+ _BMUseCaseMaintenance
+ _BMUseCaseWriter
- _objc_retain_x9
CStrings:
+ "\x01\x13\x11\x12"
+ "\t"
+ "\x12"
+ "%@ Failed to delete file %@ from file\u00a0transfer directory with error %@"
+ "%@: Failed access database while handling fetch mergeable deltas request for set: %@ error: %@"
+ "%@: Failed to discover remote sets, cannot proceed to sync with device %@"
+ "%@: Failed to enumerate contents of file transfer directory %@"
+ "%@: Failed to fetch attributes of file at path: %@"
+ "%@: Failed to remove item at url %@ with error %@"
+ "%@: No database access - building fetch request with empty state vector for set: %@ (error: %@)"
+ "%@: Skipping pruning of temporary file with creation date: %@, not old enough"
+ "%@: activating file transfer session %@"
+ "%@: adding items %@ to file transfer session %@"
+ "%@: attempting to tear down sync engine but a request is still in progress %@"
+ "%@: barrier hit, all deltas fetched for device %@"
+ "%@: beginning to fetch deltas for set %@ from device %@"
+ "%@: cannot determine set or device from incoming file transfer metadata %@"
+ "%@: completeRequest:deliveredToDevices %@ withErrors:%@"
+ "%@: completing request, still inflight: %@"
+ "%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@"
+ "%@: could not find device to reciprocate with fallback identifier %@"
+ "%@: creating operations for syncing sets with device %@"
+ "%@: discovered %@ sets with device %@"
+ "%@: discovered devices: %@"
+ "%@: discovered local device %@"
+ "%@: discovered synable set %@ for platform %@"
+ "%@: done fetching all deltas from device, signalling remote device we are done fetching %@"
+ "%@: done fetching deltas for set %@ from device %@"
+ "%@: encountered rapport messaging error %@"
+ "%@: engaging with device: %@"
+ "%@: evaluating whether device is supported for messaging %@"
+ "%@: expecting reciprocal request from device %@"
+ "%@: failed to assume persona to handle incoming file with error %@"
+ "%@: failed to enumerate sets with error %@"
+ "%@: fetchMergeableDeltasWithReason persona is %@"
+ "%@: found syncable set %@"
+ "%@: initiated file transfer session with device %@ fileTransferSession %@"
+ "%@: initiating file transfer session with device %@"
+ "%@: item completion handler invoked for url %@ with error %@"
+ "%@: local device %@"
+ "%@: mismatched protocol version %lu, expected %d"
+ "%@: no syncable sets"
+ "%@: other device is already syncing so will not reciprocate with us, complete the request %@"
+ "%@: parent fetch all deltas operation cancelled, cancelling all operations on device operation queue"
+ "%@: protocol version mismatch %@, cannot initiate file transfer with device %@"
+ "%@: received done fetching mergeable deltas message %@ %@"
+ "%@: received fetch mergeable deltas request %@ %@"
+ "%@: received file transfer item with url %@ from device %@"
+ "%@: received item over file transfer session %@"
+ "%@: received response from initating file transfer %@ with error %@"
+ "%@: received response from set discovery %@ with error %@"
+ "%@: received response from signalling end of fetching %@ with error %@"
+ "%@: received set discovery request %@ %@"
+ "%@: reciprocal request completed with %@ %@"
+ "%@: registering to receive incoming files with peer key %@"
+ "%@: request %@ already finished running"
+ "%@: request timed out because no devices are nearby"
+ "%@: request timed out because no devices are nearby or messages in flight to devices failed to respond in time"
+ "%@: sending request for set: %@ to device %@"
+ "%@: set does not exist on device %@"
+ "%@: signalled remote device we are done fetching %@ with error %@"
+ "%@: syncing to platform %@ is not supported from this device"
+ "%@: unable to determine sender model info: %@"
+ "%@: unsupported file format version %@"
+ "%@[%@]"
+ "@32@0:8@16@?24"
+ "CCRapportFileTransferManager: access assertion does not contain a valid path to sync directory %@"
+ "Failed to assume persona %@ for didDiscoverDevice handler %@"
+ "Failed to assume persona %@ for didLoseDevice handler %@"
+ "Failed to assume persona %@ for localDeviceUpdated handler %@"
+ "Failed to assume persona with error %@, rejecting donate request %@"
+ "emptyStateVector"
+ "initWithPersonaIdentifier:asyncOperationBlock:"
+ "readOnlyInstanceForSet:mergeableDeltasFileURL:database:"
+ "reject"
+ "rejectConnection"
+ "requestAccess:forResource:withMode:useCase:error:"
+ "writeOnlyInstanceForSet:donateServiceProvider:"
- "\x01\x12\x11\x12"
- "\x06"
- "CCRapportSyncEngine%@: attempting to tear down sync engine but a request is still in progress %@"
- "CCRapportSyncEngine%@: barrier hit, all deltas fetched for device %@"
- "CCRapportSyncEngine%@: beginning to fetch deltas for set %@ from device %@"
- "CCRapportSyncEngine%@: completeRequest:deliveredToDevices %@ withErrors:%@"
- "CCRapportSyncEngine%@: completing request, still inflight: %@"
- "CCRapportSyncEngine%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@"
- "CCRapportSyncEngine%@: could not find device to reciprocate with fallback identifier %@"
- "CCRapportSyncEngine%@: creating operations for syncing sets with device %@"
- "CCRapportSyncEngine%@: discovered %@ sets with device %@"
- "CCRapportSyncEngine%@: discovered devices: %@"
- "CCRapportSyncEngine%@: discovered local device %@"
- "CCRapportSyncEngine%@: discovered synable set %@ for platform %@"
- "CCRapportSyncEngine%@: done fetching all deltas from device, signalling remote device we are done fetching %@"
- "CCRapportSyncEngine%@: done fetching deltas for set %@ from device %@"
- "CCRapportSyncEngine%@: engaging with device: %@"
- "CCRapportSyncEngine%@: evaluating whether device is supported for messaging %@"
- "CCRapportSyncEngine%@: expecting reciprocal request from device %@"
- "CCRapportSyncEngine%@: failed to enumerate sets with error %@"
- "CCRapportSyncEngine%@: found syncable set %@"
- "CCRapportSyncEngine%@: local device %@"
- "CCRapportSyncEngine%@: mismatched protocol version %lu, expected %d"
- "CCRapportSyncEngine%@: no syncable sets"
- "CCRapportSyncEngine%@: other device is already syncing so will not reciprocate with us, complete the request %@"
- "CCRapportSyncEngine%@: parent fetch all deltas operation cancelled, cancelling all operations on device operation queue"
- "CCRapportSyncEngine%@: received done fetching mergeable deltas message %@ %@"
- "CCRapportSyncEngine%@: received fetch mergeable deltas request %@ %@"
- "CCRapportSyncEngine%@: received set discovery request %@ %@"
- "CCRapportSyncEngine%@: reciprocal request completed with %@ %@"
- "CCRapportSyncEngine%@: request %@ already finished running"
- "CCRapportSyncEngine%@: request timed out because no devices are nearby"
- "CCRapportSyncEngine%@: request timed out because no devices are nearby or messages in flight to devices failed to respond in time"
- "CCRapportSyncEngine%@: sending request for set: %@ to device %@"
- "CCRapportSyncEngine%@: set does not exist on device %@"
- "CCRapportSyncEngine%@: signalled remote device we are done fetching %@ with error %@"
- "CCRapportSyncEngine%@: syncing to platform %@ is not supported from this device"
- "CCRapportSyncEngine%@: unable to determine sender model info: %@"
- "CCRapportSyncEngine: activating file transfer session %@"
- "CCRapportSyncEngine: adding items %@ to file transfer session %@"
- "CCRapportSyncEngine: cannot determine set or device from incoming file transfer metadata %@"
- "CCRapportSyncEngine: encountered rapport messaging error %@"
- "CCRapportSyncEngine: initiated file transfer session with device %@ fileTransferSession %@"
- "CCRapportSyncEngine: initiating file transfer session with device %@"
- "CCRapportSyncEngine: item completion handler invoked for url %@ with error %@"
- "CCRapportSyncEngine: protocol version mismatch %@, cannot initiate file transfer with device %@"
- "CCRapportSyncEngine: received file transfer item with url %@ from device %@"
- "CCRapportSyncEngine: received item over file transfer session %@"
- "CCRapportSyncEngine: received response from initating file transfer %@ with error %@"
- "CCRapportSyncEngine: received response from set discovery %@ with error %@"
- "CCRapportSyncEngine: received response from signalling end of fetching %@ with error %@"
- "CCRapportSyncEngine: registering to receive incoming files with peer key %@"
- "CCRapportSyncEngine: unsupported file format version %@"
- "Failed access database while handling fetch mergeable deltas request for set: %@ error: %@"
- "Failed access database while handling file transfer for set: %@ error: %@"
- "Failed to delete file %@ from file\u00a0transfer directory with error %@"
- "Failed to discover remote sets, cannot proceed to sync with device %@"
- "Failed to enumerate contents of file transfer directory %@"
- "Failed to fetch attributes of file at path: %@"
- "Failed to remove item at url %@ with error %@"
- "Skipping pruning of temporary file with creation date: %@, not old enough"
- "_encodedSetDescriptors"
- "a"
- "buildVersionedMergeableForSet:readAccess:"
- "fetchMergeableDeltasWithReason persona is %@"

```
