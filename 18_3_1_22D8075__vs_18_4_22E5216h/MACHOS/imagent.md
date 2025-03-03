## imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

-1402.400.131.2.6
-  __TEXT.__text: 0x4763c
-  __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_stubs: 0x5800
-  __TEXT.__objc_methlist: 0x1680
-  __TEXT.__const: 0x1024
-  __TEXT.__gcc_except_tab: 0x3c3c
-  __TEXT.__cstring: 0x1bbc
-  __TEXT.__oslogstring: 0x590b
-  __TEXT.__objc_methname: 0x9994
+1402.500.164.2.1
+  __TEXT.__text: 0x48914
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__objc_stubs: 0x5820
+  __TEXT.__objc_methlist: 0x2bc0
+  __TEXT.__const: 0x1064
+  __TEXT.__gcc_except_tab: 0x3c58
+  __TEXT.__cstring: 0x19ec
+  __TEXT.__oslogstring: 0x5b9b
+  __TEXT.__objc_methname: 0x9c4b
   __TEXT.__objc_classname: 0x598
-  __TEXT.__objc_methtype: 0x2228
-  __TEXT.__swift5_typeref: 0x42c
-  __TEXT.__swift5_fieldmd: 0x2b0
-  __TEXT.__constg_swiftt: 0x4c0
+  __TEXT.__objc_methtype: 0x2253
+  __TEXT.__swift5_typeref: 0x486
+  __TEXT.__swift5_fieldmd: 0x2c0
+  __TEXT.__constg_swiftt: 0x4fc
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0x130
+  __TEXT.__swift5_capture: 0x160
   __TEXT.__swift5_proto: 0xac
-  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_reflstr: 0x357
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x14f8
-  __TEXT.__eh_frame: 0x500
-  __DATA_CONST.__auth_got: 0xab8
-  __DATA_CONST.__got: 0x8d8
+  __TEXT.__unwind_info: 0x1538
+  __TEXT.__eh_frame: 0x4f8
+  __DATA_CONST.__auth_got: 0xab0
+  __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x2d8
-  __DATA_CONST.__const: 0x1308
+  __DATA_CONST.__const: 0x14d8
   __DATA_CONST.__cfstring: 0x7c0
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5348
-  __DATA.__objc_selrefs: 0x21a8
+  __DATA.__objc_const: 0x2b10
+  __DATA.__objc_selrefs: 0x24c0
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0xaf8
-  __DATA.__data: 0x1200
+  __DATA.__data: 0x12a8
   __DATA.__common: 0xe0
-  __DATA.__bss: 0xf70
+  __DATA.__bss: 0xf60
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 969
-  Symbols:   527
-  CStrings:  2158
+  Functions: 1006
+  Symbols:   535
+  CStrings:  2185
 
Symbols:
+ _IDSServiceNameiMessageForBusiness
+ _OBJC_CLASS_$_BGNonRepeatingSystemTask
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_IDSFeatureToggleRetrievalOptions
+ _OBJC_CLASS_$_IDSFeatureToggleUpdateOptions
+ _OBJC_CLASS_$_IDSFeatureToggler
+ _swift_dynamicCastObjCClassUnconditional
+ _swift_initStaticObject
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "%s BIA is enabled. No action required."
+ "%s No action required."
+ "%s called for task %s"
+ "%s called with lockdownModeEnabled %{bool}d"
+ "16:02:42"
+ "@\"IMDiMessageIDSDelegate\"16@0:8"
+ "BIADisabledInLDM"
+ "Error when updateFeatureToggleState:with: LDM is disabled. Error code: %lu"
+ "Error when updateFeatureToggleState:with: LDM is enabled. Error code: %lu"
+ "Failed to submit task %s with error: %@"
+ "Feb 28 2025"
+ "Got called to backup active aliases in check in state"
+ "Got called to backup active aliases with activity %@"
+ "LockdownMode is disabled. Sending a message to IDS Server to enable BIA"
+ "LockdownMode is enabled. Sending a message to IDS Server to disable BIA"
+ "Registering for backup of active aliases"
+ "Successfully submitted task %s"
+ "T@\"IMDiMessageIDSDelegate\",?,R,N"
+ "T@\"IMDiMessageIDSDelegate\",N,&,ViMessageIDSHandler"
+ "The BG system task %s expired."
+ "_TtC7imagent22BIALockdownModeHandler"
+ "_automation_receiveDictionary:options:fromHandle:"
+ "_automation_receiveDictionary:options:fromID:"
+ "_registerForAliasesBackup"
+ "calculateAndSaveAliasesToDefaults"
+ "com.apple.messages.LDM.BIA"
+ "com.apple.messages.backupOfAliases"
+ "deviceIsLockedDown"
+ "error"
+ "handleBIAToggleStateTask(_:)"
+ "initWithIdentifier:"
+ "initWithService:queue:"
+ "messagesAppDomain"
+ "movedMessageGUIDsToRecentlyDeleted:forChatWithGUID:queryID:deletionDate:"
+ "optionsWithFeatureID:"
+ "optionsWithFeatureID:state:"
+ "performLockdownModeActionsIfNeeded()"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "retrieveFeatureToggleState:for: returned result.success %{bool}d result.state %lu result.error %lu"
+ "retrieveFeatureToggleStateForOptions:completion:"
+ "sendBrandLogoUpdate:toChatID:identifier:style:account:"
+ "setExpirationHandler:"
+ "setIMessageIDSHandler:"
+ "setPriority:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setScheduleAfter:"
+ "setTaskCompleted"
+ "setTrySchedulingBefore:"
+ "sharedScheduler"
+ "state"
+ "submitTaskRequest:error:"
+ "success"
+ "updateBalloonPayload:attachments:bundleID:forMessage:"
+ "updateBalloonPayload:attachments:bundleID:forMessageGUID:"
+ "updateFeatureToggleState:with: LDM is enabled. returned result.success %{bool}d result.error %lu"
+ "updateFeatureToggleState:with: when LDM disabled returned result.success %{bool}d result.error %lu"
+ "updateFeatureToggleStateWithOptions:completion:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v16@?0@\"IDSFeatureToggleRetrievalResult\"8"
+ "v16@?0@\"IDSFeatureToggleUpdateResult\"8"
+ "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSString\"32"
- "21:40:00"
- "AutomationRequestHandler"
- "Fatal error"
- "Feb 10 2025"
- "Got called to sync chats in check in run state with non null activity %@"
- "Got called to sync chats in check in state"
- "Ignoring activity request to sync chats, as syncing is disabled"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Registering for chat syncing using identifier %s interval %lld"
- "Rejecting request to simulate messages as this is not an internal install"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "We did not set the state of xpc_activity from core duet to continue successfully for chat sync"
- "_automation_receiveDictionary:fromID:"
- "_registerForChatSyncing"
- "beginChatSyncPeriodic:activity:"
- "com.apple.messages.chatSyncing"
- "invalid Collection: less than 'count' elements in collection"
- "isCarrierPigeonEnabled"
- "movedMessagesToRecentlyDeletedWithQueryID:"
- "performInitialSyncOnFirstConnectionOfImagentIfNeeded"
- "syncChats"
- "updateBalloonPayload:attachments:forMessageGUID:"
- "v40@0:8@\"NSData\"16@\"NSArray\"24@\"NSString\"32"

```
