## Messages

> `/System/Library/iCloudSettings/Messages.bundle/Contents/MacOS/Messages`

```diff

-  __TEXT.__text: 0xd12c
-  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__text: 0x100dc
+  __TEXT.__auth_stubs: 0xbd0
   __TEXT.__delay_helper: 0x114
-  __TEXT.__objc_stubs: 0x340
-  __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0x998
-  __TEXT.__swift5_typeref: 0x214b
-  __TEXT.__constg_swiftt: 0x2fc
-  __TEXT.__swift5_reflstr: 0x214
-  __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_fieldmd: 0x1b4
-  __TEXT.__cstring: 0x50b
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_capture: 0xac
-  __TEXT.__oslogstring: 0x2b3
-  __TEXT.__objc_classname: 0xae
-  __TEXT.__objc_methname: 0x4ea
-  __TEXT.__objc_methtype: 0xe7
-  __TEXT.__unwind_info: 0x300
-  __TEXT.__eh_frame: 0x7c
-  __DATA_CONST.__const: 0x51b
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__objc_stubs: 0x520
+  __TEXT.__objc_methlist: 0x244
+  __TEXT.__const: 0xc08
+  __TEXT.__swift5_typeref: 0x20cf
+  __TEXT.__constg_swiftt: 0x38c
+  __TEXT.__swift5_reflstr: 0x2a4
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__swift5_fieldmd: 0x200
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__cstring: 0x59b
+  __TEXT.__swift5_proto: 0x48
+  __TEXT.__swift5_types: 0x28
+  __TEXT.__objc_classname: 0x12e
+  __TEXT.__objc_methname: 0x8c5
+  __TEXT.__objc_methtype: 0x2cc
+  __TEXT.__swift5_capture: 0xf4
+  __TEXT.__oslogstring: 0x363
+  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__eh_frame: 0x14c
+  __DATA_CONST.__const: 0x623
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x568
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__auth_ptr: 0x388
-  __DATA.__objc_const: 0x338
-  __DATA.__objc_selrefs: 0x188
-  __DATA.__objc_data: 0x2a0
-  __DATA.__data: 0x74c
-  __DATA.__bss: 0x828
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__auth_got: 0x5f0
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__auth_ptr: 0x398
+  __DATA.__objc_const: 0x578
+  __DATA.__objc_selrefs: 0x238
+  __DATA.__objc_data: 0x3f0
+  __DATA.__data: 0x89c
+  __DATA.__bss: 0x9d8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
+  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer
   - /System/Library/Frameworks/Photos.framework/Versions/A/Photos

   - /System/Library/PrivateFrameworks/CoreParsec.framework/Versions/A/CoreParsec
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/CoreSuggestions
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/Versions/A/EmbeddedAcousticRecognition
+  - /System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/Versions/A/IMSharedUtilities
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/InputAnalytics.framework/Versions/A/InputAnalytics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 269
-  Symbols:   112
-  CStrings:  126
+  Functions: 360
+  Symbols:   128
+  CStrings:  178
 
Symbols:
+ _IMCloudKitDefinesDomain
+ _OBJC_CLASS_$_CKAttachmentAssetDownloadPresentableStatus
+ _OBJC_CLASS_$_IMCloudKitEventNotificationManager
+ _OBJC_CLASS_$_IMCloudKitHooks
+ _OBJC_CLASS_$_IMCloudKitSyncState
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_METACLASS_$_CKAttachmentAssetDownloadPresentableStatus
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ _swift_beginAccess
+ _swift_getForeignTypeMetadata
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
CStrings:
+ "@32@0:8@16q24"
+ "Attachment download status update — phase=%lu, remaining=%ld, finished=%{bool}d, timeFrame=%ld"
+ "Attachment download time frame changed: %ld -> %ld"
+ "CKAttachmentAssetDownloadPresentableStatus"
+ "IMCloudKitEventHandler"
+ "Q"
+ "SYNC_ALL_ATTACHMENTS_DOWNLOADED"
+ "SYNC_DOWNLOADING_N_ATTACHMENTS"
+ "SYNC_PENDING_ATTACHMENT_DOWNLOAD"
+ "TQ,N,R,Vphase"
+ "Tq,N,R,VremainingCount"
+ "Tq,N,R,VtimeFrame"
+ "User tapped Download All Attachments"
+ "_TtC8Messages27AttachmentDownloadViewModel"
+ "__ObjC.CKAttachmentAssetDownloadPresentableStatus"
+ "_currentTimeFrame"
+ "_downloadButtonLabel"
+ "_lastSyncState"
+ "_presentableStatus"
+ "addEventHandler:"
+ "attachmentDownloadTimeFrameWithReply:"
+ "attachmentDownloadViewModel"
+ "cloudKitEventNotificationManager:didChangeEnabled:error:"
+ "cloudKitEventNotificationManager:didDisableAllDevices:error:"
+ "cloudKitEventNotificationManager:didFetchSyncStatistics:error:"
+ "cloudKitEventNotificationManager:didPerformAdditionalStorageRequiredCheck:additionalStorageRequired:forAccountId:error:"
+ "cloudKitEventNotificationManager:syncProgressDidUpdate:"
+ "cloudKitEventNotificationManager:syncStateDidChange:"
+ "didFinishDownloadingAttachmentHistory"
+ "fetchSyncState"
+ "initWithSuiteName:"
+ "initWithSyncState:timeFrame:"
+ "integerForKey:"
+ "isSyncing"
+ "phase"
+ "q"
+ "q16@0:8"
+ "remainingCount"
+ "removeEventHandler:"
+ "serverAttachmentTotalCount"
+ "setAttachmentDownloadTimeFrame:"
+ "sharedInstance"
+ "statistics"
+ "syncState"
+ "syncType"
+ "timeFrame"
+ "v16@?0q8"
+ "v32@0:8@\"IMCloudKitEventNotificationManager\"16@\"IMCloudKitSyncProgress\"24"
+ "v32@0:8@\"IMCloudKitEventNotificationManager\"16@\"IMCloudKitSyncState\"24"
+ "v32@0:8@16@24"
+ "v36@0:8@\"IMCloudKitEventNotificationManager\"16B24@\"NSError\"28"
+ "v36@0:8@16B24@28"
+ "v40@0:8@\"IMCloudKitEventNotificationManager\"16@\"IMCloudKitSyncStatistics\"24@\"NSError\"32"
+ "v40@0:8@16@24@32"
+ "v52@0:8@\"IMCloudKitEventNotificationManager\"16B24Q28@\"NSString\"36@\"NSError\"44"
+ "v52@0:8@16B24Q28@36@44"
+ "v8@?0"
- "SYNC_BEFORE_SHORT_ALL"
- "Updating attachment download time frame to %ld"
- "attachmentDownloadSelection"
- "attachmentDownloadTimeFrame"
- "updateAttachmentDownloadTimeFrame:"

```
