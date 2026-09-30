## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

```diff

-  __TEXT.__text: 0x74520
-  __TEXT.__auth_stubs: 0x1340
-  __TEXT.__objc_stubs: 0x37c0
-  __TEXT.__objc_methlist: 0x2474
-  __TEXT.__cstring: 0x9ff3
-  __TEXT.__objc_methname: 0x6015
+  __TEXT.__text: 0x76d60
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_stubs: 0x3840
+  __TEXT.__objc_methlist: 0x2564
+  __TEXT.__cstring: 0xa663
+  __TEXT.__objc_methname: 0x6185
   __TEXT.__objc_classname: 0x357
-  __TEXT.__objc_methtype: 0x1875
+  __TEXT.__objc_methtype: 0x1905
   __TEXT.__const: 0x6f2
-  __TEXT.__gcc_except_tab: 0x1ab0
-  __TEXT.__oslogstring: 0xafca
+  __TEXT.__gcc_except_tab: 0x1bb4
+  __TEXT.__oslogstring: 0xb343
   __TEXT.__swift5_typeref: 0x47a
   __TEXT.__swift5_capture: 0x3c0
   __TEXT.__swift5_fieldmd: 0xac

   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift_as_cont: 0x128
-  __TEXT.__unwind_info: 0x1910
+  __TEXT.__unwind_info: 0x19c0
   __TEXT.__eh_frame: 0x13a0
-  __DATA_CONST.__const: 0x17f8
-  __DATA_CONST.__cfstring: 0x1a60
+  __DATA_CONST.__const: 0x18b8
+  __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__auth_got: 0x9b8
-  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__auth_got: 0x9c0
+  __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0x128
-  __DATA.__objc_const: 0x30f8
-  __DATA.__objc_selrefs: 0x1350
+  __DATA.__objc_const: 0x31a0
+  __DATA.__objc_selrefs: 0x1388
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x600
   __DATA.__data: 0x6d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1841
-  Symbols:   503
-  CStrings:  3005
+  Functions: 1872
+  Symbols:   508
+  CStrings:  3090
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _SecItemPersistKeychainWritesAtHighPerformanceCost
+ ___kCFBooleanFalse
+ _kSecAttrService
+ _kSecClassGenericPassword
+ _kSecReturnPersistentRef
CStrings:
+ "%@"
+ "%s : #MOS : %s Page is not Zero : %d"
+ "%s : #MOS : %s is not in the range : %d"
+ "%s is not in the range : %d"
+ "%s: #MOS : ==> Decoded %s Len : %d"
+ "%s: #MOS : ==> Decoded wakeup channel Line : %d"
+ "%s: #MOS : Wakeup channel : %d"
+ "%s: %@ dataset not found (already deleted)"
+ "%s: Add %@ DataSet with length: %lu"
+ "%s: Credential exists. Should have been deleted."
+ "%s: Delete completed (error ignored), now adding %@ dataset"
+ "%s: Empty data"
+ "%s: Failed adding %@ dataset: %@"
+ "%s: Failed to delete %@ dataset: %@"
+ "%s: Keychain item deleted for %@ dataset"
+ "%s: Keychain item not found for %@ dataset: %@"
+ "%s: Pending Dataset: Invoking SecItemPersistKeychainWritesAtHighPerformanceCost"
+ "%s: Reading %@ DataSet"
+ "%s: Remove %@ DataSet"
+ "%s: SecItemAdd SUCCESS for %@ dataset"
+ "%s: SecItemCopyMatching SUCCESS for %@ dataset, length: %lu"
+ "%s: SecItemPersistKeychainWritesAtHighPerformanceCost Error"
+ "%s: Server: Got response from Store, datasetData length: %lu, error: %@\n"
+ "%s: Server: Got response from Store, error: %@\n"
+ "%s: Server: adding %@ dataset...\n"
+ "%s: Server: deleting %@ dataset...\n"
+ "%s: Server: retrieving %@ dataset...\n"
+ "%s: dataset not found in keychain,CFData/Dictionary is NULL for %@ dataset"
+ "-[CTCSXPCService ctcsServerAddDataSetWithCompletion:datasetData:completion:]"
+ "-[CTCSXPCService ctcsServerAddDataSetWithCompletion:datasetData:completion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerDeleteDataSetWithCompletion:completion:]"
+ "-[CTCSXPCService ctcsServerDeleteDataSetWithCompletion:completion:]_block_invoke_2"
+ "-[CTCSXPCService ctcsServerFindAndGetDataSetWithCompletion:completion:]"
+ "-[CTCSXPCService ctcsServerFindAndGetDataSetWithCompletion:completion:]_block_invoke_2"
+ "-[THThreadNetworkCredentialsKeychainBackingStore addThreadDataSetWithCompletion:datasetData:completion:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore addThreadDataSetWithCompletion:datasetData:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore deleteThreadDataSetWithCompletion:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore findAndGetThreadDataSetWithCompletion:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore parsedChannelFromData:len:currentPos:debugDescription:error:]"
+ "-[THThreadNetworkCredentialsStoreLocalClient parsedChannelFromData:len:currentPos:debugDescription:error:]"
+ "==> Decoded %s Len : %d"
+ "==> Decoded wakeup channel  "
+ "Active"
+ "C48@0:8r*16C24I28r*32^@40"
+ "Channel"
+ "Duplicate item exists"
+ "Empty dataset data"
+ "Failed to add dataset"
+ "Failed to add dataset; Backing store is nil"
+ "Failed to delete dataset"
+ "Failed to delete dataset; Backing store is nil"
+ "Failed to retrieve dataset"
+ "Failed to retrieve dataset; Backing store is nil"
+ "Pending"
+ "Pending Dataset failed to persist keychain writes"
+ "ThreadActiveDataSet"
+ "ThreadPendingDataSet"
+ "Wakeup Channel"
+ "Wakeup Channel : %d"
+ "addThreadDataSetWithCompletion:datasetData:completion:"
+ "com.apple.thread.datasetmacos"
+ "ctcsServerAddDataSetWithCompletion:datasetData:completion:"
+ "ctcsServerDeleteDataSetWithCompletion:completion:"
+ "ctcsServerFindAndGetDataSetWithCompletion:completion:"
+ "deleteThreadDataSetWithCompletion:completion:"
+ "findAndGetThreadDataSetWithCompletion:completion:"
+ "parsedChannelFromData:len:currentPos:debugDescription:error:"
+ "thclient"
+ "thserver"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v28@0:8B16@?<v@?@\"NSData\"@\"NSError\">20"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "v36@0:8B16@\"NSData\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@20@?28"
- "%s : #MOS : Channel Page is not Zero : %d"
- "%s : #MOS : Channel is not in the range : %d"
- "%s: #MOS : ==> Decoded channel Len : %d"
- "-[THThreadNetworkCredentialsKeychainBackingStore areValidDataSetTLVs:creds:updateATS:isATSAppended:]"
- "==> Decoded channel Len : %d"
- "Channel is not in the range : %d"
- "THClient"
- "THServer"

```
