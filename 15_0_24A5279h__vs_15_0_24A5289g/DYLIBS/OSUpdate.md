## OSUpdate

> `/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate`

```diff

-2009.0.0.0.1
-  __TEXT.__text: 0x856ec
+2013.0.0.0.0
+  __TEXT.__text: 0x85818
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_methlist: 0x5558
   __TEXT.__const: 0x199
   __TEXT.__cstring: 0x5b5a
   __TEXT.__gcc_except_tab: 0x20c4
-  __TEXT.__oslogstring: 0xaf95
+  __TEXT.__oslogstring: 0xaff1
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x1ac0
   __TEXT.__objc_classname: 0x6a4
-  __TEXT.__objc_methname: 0x12d7a
+  __TEXT.__objc_methname: 0x12d99
   __TEXT.__objc_methtype: 0x1d97
-  __TEXT.__objc_stubs: 0xcba0
+  __TEXT.__objc_stubs: 0xcbc0
   __DATA_CONST.__got: 0x8e0
   __DATA_CONST.__const: 0xb70
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3df0
+  __DATA_CONST.__objc_selrefs: 0x3df8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x3f0

   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x2490
   __AUTH_CONST.__cfstring: 0x48e0
-  __AUTH_CONST.__objc_const: 0x89a8
+  __AUTH_CONST.__objc_const: 0x89c8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2604
-  Symbols:   6246
+  Symbols:   6247
   CStrings:  797
 
Symbols:
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.413
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.413.cold.1
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.417
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.417.cold.1
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.417.cold.2
+ __123-[SUOSUShimController _startInstallingUpdatesRequiringNoPostInstallAction:inForeground:nowIsLater:mdmInitiated:completion:]_block_invoke.482
+ __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.394
+ __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.394.cold.1
+ __51-[SUOSUShimController _handleForegroundSplatApply:]_block_invoke.318
+ __51-[SUOSUShimController _handleForegroundSplatApply:]_block_invoke.318.cold.1
+ __57-[SUOSUShimController observeForegroundInstallInProgress]_block_invoke.399
+ __59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke.344
+ __59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke_2.345
+ __63-[SUOSUShimController _installConfigDataUpdateWithProductKeys:]_block_invoke.491
+ __63-[SUOSUShimController _installConfigDataUpdateWithProductKeys:]_block_invoke.491.cold.1
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.458
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.459
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.470
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.471
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.474
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.405
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.408
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.408.cold.1
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.408.cold.2
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.408.cold.3
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.408.cold.4
+ __93-[SUOSUShimController _startShowingProgressForExternalUpdate:mdmInitiated:successCompletion:]_block_invoke.422
+ __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.507
+ __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.511
+ __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.512
+ __block_literal_global.407
+ __block_literal_global.461
+ __block_literal_global.476
+ _objc_msgSend$client:queuingUpdatesForLater:
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.411
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.411.cold.1
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.415
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.415.cold.1
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.415.cold.2
- __123-[SUOSUShimController _startInstallingUpdatesRequiringNoPostInstallAction:inForeground:nowIsLater:mdmInitiated:completion:]_block_invoke.480
- __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.390
- __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.392.cold.1
- __51-[SUOSUShimController _handleForegroundSplatApply:]_block_invoke.316
- __51-[SUOSUShimController _handleForegroundSplatApply:]_block_invoke.316.cold.1
- __57-[SUOSUShimController observeForegroundInstallInProgress]_block_invoke.397
- __59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke.342
- __59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke_2.343
- __63-[SUOSUShimController _installConfigDataUpdateWithProductKeys:]_block_invoke.489
- __63-[SUOSUShimController _installConfigDataUpdateWithProductKeys:]_block_invoke.489.cold.1
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.456
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.457
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.466
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.469
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.472
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.403
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.406
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.406.cold.1
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.406.cold.2
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.406.cold.3
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.406.cold.4
- __93-[SUOSUShimController _startShowingProgressForExternalUpdate:mdmInitiated:successCompletion:]_block_invoke.420
- __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.505
- __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.509
- __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.510
- __block_literal_global.405
- __block_literal_global.459
- __block_literal_global.474
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"

```
