## shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

-236.7.0.0.0
-  __TEXT.__text: 0x3d6a0
+236.12.0.0.0
+  __TEXT.__text: 0x3de44
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_stubs: 0xa780
-  __TEXT.__objc_methlist: 0x4424
+  __TEXT.__objc_stubs: 0xa8a0
+  __TEXT.__objc_methlist: 0x445c
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x790
-  __TEXT.__objc_methname: 0xd190
-  __TEXT.__cstring: 0x2100
-  __TEXT.__oslogstring: 0x2c46
-  __TEXT.__objc_classname: 0x10d7
-  __TEXT.__objc_methtype: 0x2545
+  __TEXT.__gcc_except_tab: 0x78c
+  __TEXT.__objc_methname: 0xd2ee
+  __TEXT.__cstring: 0x2153
+  __TEXT.__oslogstring: 0x2cfc
+  __TEXT.__objc_classname: 0x10e4
+  __TEXT.__objc_methtype: 0x2537
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x1084
+  __TEXT.__unwind_info: 0x1078
   __DATA_CONST.__auth_got: 0x3f0
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x1458
-  __DATA_CONST.__cfstring: 0x1d20
-  __DATA_CONST.__objc_classlist: 0x408
+  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__const: 0x1488
+  __DATA_CONST.__cfstring: 0x1da0
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0xc0f8
-  __DATA.__objc_selrefs: 0x2e08
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x850
+  __DATA.__objc_const: 0xc1a8
+  __DATA.__objc_selrefs: 0x2e58
+  __DATA.__objc_protorefs: 0x30
+  __DATA.__objc_classrefs: 0x870
   __DATA.__objc_superrefs: 0x310
-  __DATA.__objc_ivar: 0x4e8
-  __DATA.__objc_data: 0x2850
-  __DATA.__data: 0x1440
+  __DATA.__objc_ivar: 0x4f0
+  __DATA.__objc_data: 0x28a0
+  __DATA.__data: 0x13e0
   __DATA.__bss: 0xe0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1496
-  Symbols:   363
-  CStrings:  3146
+  Functions: 1499
+  Symbols:   368
+  CStrings:  3168
 
Symbols:
+ _OBJC_CLASS_$_SHLocalization
+ _OBJC_CLASS_$_UNNotificationAction
+ _OBJC_CLASS_$_UNNotificationActionIcon
+ _SHMediaLibraryAccountChangeNotification
+ _UNNotificationDefaultActionIdentifier
CStrings:
+ "%@.%@"
+ "@\"SHMediaLibraryInfoFetcher\""
+ "Calling shutdown on the service %@ of the handle %@"
+ "Error handling apple music action with error: %@"
+ "Failed to handle notification action"
+ "No apple music url provided for payload %@"
+ "SHAZAM_MODULE_NOTIFICATION_ACTION_TITLE"
+ "SHMediaLibraryInfoFetcher"
+ "SHShazamKitShazamService"
+ "Shazam service stopRecognition called"
+ "T@\"SHMediaLibraryInfoFetcher\",&,N,V_libraryInfoFetcher"
+ "T@\"SHMediaLibraryInfoFetcher\",R,N,V_libraryInfoFetcher"
+ "T@,&,N,V_notificationObserver"
+ "[%@] stopRecognition called for worker with task ID %@"
+ "_libraryInfoFetcher"
+ "_notificationObserver"
+ "actionIdentifier"
+ "actionWithIdentifier:title:options:icon:"
+ "apple-music-action"
+ "commonInitWithDataStore:remoteLibrary:libraryInfoFetcher:snapshotUpdater:"
+ "fetchAccountTokensWithAccountInfo:completion:"
+ "handleAppleMusicActionWithPayload:completionHandler:"
+ "handleDefaultActionWithPayload:completionHandler:"
+ "iconWithSystemImageName:"
+ "initWithDataStore:remoteLibrary:libraryInfoFetcher:snapshotUpdater:"
+ "libraryInfoFetcher"
+ "listenForChanges"
+ "localizedStringForKey:"
+ "music.square.fill"
+ "notificationActionForMatch"
+ "notificationObserver"
+ "sendAnalyticsEvent:forBundleIdentifier:actionName:"
+ "setLibraryInfoFetcher:"
+ "setNotificationObserver:"
+ "shutdownService"
+ "shutdownWorker"
+ "shutdownWorkerForRequestID:"
- "@\"<SHMediaLibraryAccountListenerDelegate>\""
- "Calling stop on the service %@ of the handle %@"
- "SHMediaLibraryAccountListenerDelegate"
- "T@\"<SHMediaLibraryAccountListenerDelegate>\",W,N,V_delegate"
- "T@\"SHMediaLibraryAccountListener\",&,N,V_accountListener"
- "[%@] stop called for worker with task ID %@"
- "commonInitWithDataStore:remoteLibrary:accountListener:snapshotUpdater:"
- "currentLibraryAccountHasChanged"
- "fetchAccountInfoWithCompletionHandler:"
- "fetchUserRecordIDWithCompletion:"
- "initWithDataStore:remoteLibrary:accountListener:snapshotUpdater:"
- "observeAccountChangedNotification"
- "setAccountListener:"
- "updateAccountInfo"
- "updateUserRecordWithAccountInfo:completion:"

```
