## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2891.0.0.0.0
-  __TEXT.__text: 0x2895d0
+2899.0.2.0.0
+  __TEXT.__text: 0x2899c8
   __TEXT.__auth_stubs: 0x3610
-  __TEXT.__objc_stubs: 0x29200
-  __TEXT.__objc_methlist: 0x1779c
+  __TEXT.__objc_stubs: 0x291e0
+  __TEXT.__objc_methlist: 0x17794
   __TEXT.__const: 0x2240
-  __TEXT.__cstring: 0x6fe4b
-  __TEXT.__objc_methname: 0x37dce
+  __TEXT.__cstring: 0x6ff2a
+  __TEXT.__objc_methname: 0x37d90
   __TEXT.__constg_swiftt: 0xa8c
   __TEXT.__swift5_typeref: 0x107d
   __TEXT.__swift5_reflstr: 0x1655

   __TEXT.__swift5_assocty: 0x108
   __TEXT.__swift5_proto: 0x160
   __TEXT.__swift5_types: 0xf0
-  __TEXT.__objc_classname: 0x1fad
-  __TEXT.__objc_methtype: 0x6517
+  __TEXT.__objc_classname: 0x1fab
+  __TEXT.__objc_methtype: 0x652e
   __TEXT.__swift5_capture: 0x444
-  __TEXT.__oslogstring: 0x328c7
+  __TEXT.__oslogstring: 0x3291e
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__gcc_except_tab: 0xc1b4
+  __TEXT.__gcc_except_tab: 0xc1d8
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x6cb0
+  __TEXT.__unwind_info: 0x6ce0
   __TEXT.__eh_frame: 0x2320
   __DATA_CONST.__auth_got: 0x1b18
-  __DATA_CONST.__got: 0xdd8
+  __DATA_CONST.__got: 0xde8
   __DATA_CONST.__auth_ptr: 0x348
   __DATA_CONST.__const: 0x8d68
-  __DATA_CONST.__cfstring: 0x1c9a0
+  __DATA_CONST.__cfstring: 0x1c9c0
   __DATA_CONST.__objc_classlist: 0xa28
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x290

   __DATA_CONST.__objc_arraydata: 0xd28
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x540
-  __DATA.__objc_const: 0x25528
-  __DATA.__objc_selrefs: 0xc028
-  __DATA.__objc_ivar: 0x1b38
+  __DATA.__objc_const: 0x25510
+  __DATA.__objc_selrefs: 0xc020
+  __DATA.__objc_ivar: 0x1b34
   __DATA.__objc_data: 0x7148
   __DATA.__data: 0x2978
   __DATA.__bss: 0x3268

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DF275999-EC6A-3CE8-BBC3-2A59781D5EF4
-  Functions: 9793
-  Symbols:   1396
-  CStrings:  27519
+  UUID: 81FED964-9036-34EC-9F1A-A527CDA791E2
+  Functions: 9792
+  Symbols:   1398
+  CStrings:  27523
 
Symbols:
+ _kMBTargetDeviceTransferMinutesRemainingNotification
+ _kMBTargetDeviceTransferProgressNotification
CStrings:
+ "-[MBPrebuddyFollowUpController updateFollowupWithBackupProgress:account:]"
+ "-[MBRemoteConfiguration loadConfigurationWithContainer:databaseManager:policy:operationGroup:completion:]"
+ "Associating cache tracker %@ with personaID %@"
+ "Fetching remote configuration id:%{public}@, gid:%{public}@ gn:%{public}@"
+ "MBRemoteConfiguration"
+ "MBRemoteConfiguration.m"
+ "Nil fileURL for resource asset (xattrs)"
+ "Nil fileURL for resource asset (xattrs) %@ for file %@"
+ "T@\"MBRemoteConfiguration\",R,N"
+ "T@\"NSMutableDictionary\",&,N,V_cacheTrackersByPersonaID"
+ "_cacheTrackersByPersonaID"
+ "_didUpdateBackupProgress:estimatedTimeRemaining:bytesRemaining:engineState:stateInfo:account:shouldUpdatePrebuddyFollowUp:"
+ "_postTransferProgressNotification:"
+ "_snapshotFormat != MBSnapshotFormatDomainsAssets || !domain.isLegacyPerAppPlaceholderDomain"
+ "addDomainsToBackUpToiCloudWithAppManager:manager:format:account:"
+ "cacheTrackersByPersonaID"
+ "isLegacyPerAppPlaceholderDomain"
+ "isLegacyPerAppPlaceholderName:"
+ "setCacheTrackersByPersonaID:"
+ "size:%lld (%@)/%lld/%lld, files:%llu, dirs:%llu, clones:%llu/%llu, hardlinks:%llu, symlinks:%llu"
+ "updateFollowupWithBackupProgress:account:"
+ "v48@0:8@16@24q32@40"
+ "v64@0:8f16Q20q28@36@44@52B60"
- "-[MBCKRemoteConfiguration loadConfigurationWithContainer:databaseManager:policy:operationGroup:completion:]"
- "-[MBPrebuddyFollowUpController updateFollowupWithBackupProgress:]"
- "=prebuddy-cfu= No account to get disabled domain infos: %@"
- "Fetching remote configuration"
- "MBCKRemoteConfiguration"
- "MBCKRemoteConfiguration.m"
- "T@\"NSMutableDictionary\",&,N,V_cacheTrackersByAccountIdentifier"
- "TB,N,V_isScanningPlaceholderAppDomain"
- "_cacheTrackersByAccountIdentifier"
- "_didUpdateBackupProgress:estimatedTimeRemaining:bytesRemaining:engineState:stateInfo:shouldUpdatePrebuddyFollowUp:"
- "_isScanningPlaceholderAppDomain"
- "addDomainsToBackUpToiCloudWithAppManager:manager:account:"
- "cacheTrackersByAccountIdentifier"
- "isAppPlaceholderName:"
- "isPlaceholderAppDomain"
- "isScanningPlaceholderAppDomain"
- "setCacheTrackersByAccountIdentifier:"
- "setIsScanningPlaceholderAppDomain:"
- "size:%lld (%@)/%lld/%lld, files:%llu, dirs:%llu, clones:%llu/%llu, hardLinks:%llu, symLinks:%llu"
- "updateFollowupWithBackupProgress:"
- "v56@0:8f16Q20q28@36@44B52"

```
