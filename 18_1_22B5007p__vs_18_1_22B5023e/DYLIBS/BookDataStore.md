## BookDataStore

> `/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore`

```diff

-2149.0.0.0.0
-  __TEXT.__text: 0x13f14c
-  __TEXT.__auth_stubs: 0x2f50
-  __TEXT.__objc_methlist: 0x6518
-  __TEXT.__cstring: 0x6db7
+2201.0.0.0.0
+  __TEXT.__text: 0x13e6b4
+  __TEXT.__auth_stubs: 0x2f70
+  __TEXT.__objc_methlist: 0x6580
+  __TEXT.__cstring: 0x6e17
   __TEXT.__const: 0x4bf8
-  __TEXT.__oslogstring: 0xeffa
+  __TEXT.__oslogstring: 0xf3ba
   __TEXT.__gcc_except_tab: 0x157c
   __TEXT.__swift5_typeref: 0x2750
   __TEXT.__swift5_reflstr: 0x1001

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x3c0
   __TEXT.__swift5_types: 0x184
-  __TEXT.__swift5_capture: 0xf9c
+  __TEXT.__swift5_capture: 0x100c
   __TEXT.__swift5_protos: 0x64
-  __TEXT.__unwind_info: 0x4198
-  __TEXT.__eh_frame: 0x2a90
+  __TEXT.__unwind_info: 0x41e0
+  __TEXT.__eh_frame: 0x2ab8
   __TEXT.__objc_classname: 0x11c9
-  __TEXT.__objc_methname: 0xe60c
-  __TEXT.__objc_methtype: 0x2486
-  __TEXT.__objc_stubs: 0x9520
-  __DATA_CONST.__got: 0xbb0
-  __DATA_CONST.__const: 0x22d0
+  __TEXT.__objc_methname: 0xe779
+  __TEXT.__objc_methtype: 0x24b7
+  __TEXT.__objc_stubs: 0x9600
+  __DATA_CONST.__got: 0xba0
+  __DATA_CONST.__const: 0x2310
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3030
+  __DATA_CONST.__objc_selrefs: 0x3080
   __DATA_CONST.__objc_protorefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x2a8
-  __AUTH_CONST.__auth_got: 0x17b8
+  __AUTH_CONST.__auth_got: 0x17c8
   __AUTH_CONST.__auth_ptr: 0x958
-  __AUTH_CONST.__const: 0x5648
-  __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0x10be8
+  __AUTH_CONST.__const: 0x5710
+  __AUTH_CONST.__cfstring: 0x3500
+  __AUTH_CONST.__objc_const: 0x10c18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1510
-  __AUTH.__data: 0x670
-  __DATA.__objc_ivar: 0x5d4
-  __DATA.__data: 0x3128
+  __AUTH.__data: 0x678
+  __DATA.__objc_ivar: 0x5d8
+  __DATA.__data: 0x3138
   __DATA.__bss: 0x5a50
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x17d0
-  __DATA_DIRTY.__data: 0x1f91
+  __DATA_DIRTY.__data: 0x1fa1
   __DATA_DIRTY.__bss: 0x15f8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6421
-  Symbols:   831
-  CStrings:  4507
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 6446
+  Symbols:   840
+  CStrings:  4534
 
Symbols:
+ _BDSIsInternalInstall
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _os_variant_has_internal_content
- _kTCCServiceUbiquity
CStrings:
+ "<nil>"
+ "@\"<BCCloudDataSourceDelegate>\""
+ "@40@0:8@16@24^@32"
+ "Attempting to remove files and start over"
+ "BCCloudDataManager #recordChange %!{(MISSING)public}@ setCloudData for id:%!{(MISSING)mask.hash}@ isNew:%!d(MISSING) data:%!@(MISSING)"
+ "BCCloudDataManager %!{(MISSING)public}@ getChangesSince -- fetchHistoryAfterToken encountered error: %!{(MISSING)public}@. About to reset historyToken, cloudSyncVersions:%!{(MISSING)public}@, currentSyncVersions:%!{(MISSING)public}@"
+ "BCCloudDataManager %!{(MISSING)public}@ getChangesSince _fetchHistoryAfterToken: %!{(MISSING)public}@"
+ "BCCloudKitDatabaseController - Detach occurred during fetch, container: %!@(MISSING)"
+ "BCSyncICloudDrive"
+ "BDSDevelopmentForceAddStoreFailureOnce"
+ "BDSLiverpoolStatusMonitor: dq_isCloudKitEnabled: signedIn = %!@(MISSING), cloudKit = %!@(MISSING), optedIn = %!@(MISSING)"
+ "BDSSyncEngine - resetChangeToken: resetting change token for %!{(MISSING)public}s"
+ "BDSSyncEngine - resetChangeToken: syncEngine not initialized"
+ "BDSSyncUserDefaults: isICloudDriveSyncOptedIn isPrimaryAccountManagedAppleID = %!@(MISSING) isBCSyncICloudDriveUserDefaults = %!@(MISSING) isBCSyncCloudKitUserDefaults = %!@(MISSING)"
+ "T@\"<BCCloudDataSourceDelegate>\",W,N,V_delegate"
+ "Trying to remove without IDs - GlobalMetadata"
+ "_booksAppBundleIdentifier"
+ "_fetchHistoryAfterToken:inMoc:error:"
+ "_isICloudDriveSyncOptedIn"
+ "_isServiceDisabled(%!{(MISSING)public}@): TCC returned a NULL array!"
+ "_isServiceEnabled(%!{(MISSING)public}@): TCC returned a NULL array!"
+ "_isTokenInvalidError:"
+ "_setupPersistentStoreWithRootDirectoryURL -- Forcing store failure once for %!{(MISSING)public}@, url: %!{(MISSING)mask.hash}@"
+ "_setupPersistentStoreWithRootDirectoryURL: %!@(MISSING), storeAdded: %!d(MISSING)"
+ "dataSource:storeDidReset:"
+ "initWithManagedObjectModel:nameOnDisk:delegate:"
+ "initWithManagedObjectModel:rootDirectoryURL:legacyRootDirectoryURL:nameOnDisk:delegate:"
+ "resetChangeToken:"
+ "stringForKey:"
+ "userDefaults"
- "BCCloudDataManager #recordChange %!{(MISSING)public}@ setCloudData for id:%!{(MISSING)mask.hash}@ data:%!@(MISSING)"
- "BDSSyncUserDefaults: isICloudDriveSyncOptedIn isPrimaryAccountManagedAppleID = %!@(MISSING) isBCSyncICloudDriveUserDefaults = %!@(MISSING)"
- "TCC returned a NULL array!"
- "Trying to remove without IDs"

```
