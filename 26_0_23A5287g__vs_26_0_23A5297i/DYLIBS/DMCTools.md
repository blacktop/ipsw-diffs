## DMCTools

> `/System/Library/PrivateFrameworks/DMCTools.framework/DMCTools`

```diff

-48.0.0.0.0
-  __TEXT.__text: 0x1b5a8
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x534
-  __TEXT.__const: 0xc60
-  __TEXT.__cstring: 0xb21
-  __TEXT.__swift5_typeref: 0x37a
-  __TEXT.__swift5_capture: 0x88
-  __TEXT.__oslogstring: 0xb38
-  __TEXT.__constg_swiftt: 0x1a4
-  __TEXT.__swift5_builtin: 0x64
+49.0.0.0.0
+  __TEXT.__text: 0x1f4d0
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_methlist: 0x6f8
+  __TEXT.__const: 0xcd8
+  __TEXT.__oslogstring: 0xd78
+  __TEXT.__swift5_typeref: 0x3e8
+  __TEXT.__cstring: 0xe71
+  __TEXT.__swift5_capture: 0x104
+  __TEXT.__constg_swiftt: 0x1f4
+  __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x150
   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_fieldmd: 0x1d4
   __TEXT.__swift5_proto: 0xa0
-  __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x618
-  __TEXT.__eh_frame: 0x6f8
-  __TEXT.__objc_methname: 0xc3b
-  __DATA_CONST.__got: 0x1d0
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__unwind_info: 0x6d0
+  __TEXT.__eh_frame: 0x740
+  __TEXT.__objc_methname: 0xe26
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
-  __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__objc_const: 0xc80
-  __AUTH.__objc_data: 0x2a0
-  __AUTH.__data: 0x2a8
-  __DATA.__data: 0x3f0
+  __DATA_CONST.__objc_selrefs: 0x538
+  __AUTH_CONST.__auth_got: 0x768
+  __AUTH_CONST.__const: 0x6d0
+  __AUTH_CONST.__objc_const: 0xf80
+  __AUTH.__objc_data: 0x380
+  __AUTH.__data: 0x2f8
+  __DATA.__data: 0x4d8
   __DATA.__bss: 0x1400
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F6E9B238-35DF-3128-88E6-EC7D706E9BDB
-  Functions: 524
-  Symbols:   334
-  CStrings:  291
+  UUID: FF546015-6DE7-3000-8936-A137DE00EC42
+  Functions: 621
+  Symbols:   402
+  CStrings:  359
 
Symbols:
+ _CFRunLoopAddSource
+ _CFRunLoopGetMain
+ _CFUserNotificationCancel
+ _CFUserNotificationCreate
+ _CFUserNotificationCreateRunLoopSource
+ _DMCSBUserNotificationDismissOnLock
+ _DMCSBUserNotificationDontDismissOnUnlock
+ _OBJC_CLASS_$_DMCSystemAlert
+ _OBJC_CLASS_$_DMCSystemAlertManager
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_METACLASS_$_DMCSystemAlert
+ _OBJC_METACLASS_$_DMCSystemAlertManager
+ __CLASS_METHODS_DMCBackgroundTask
+ __CLASS_METHODS_DMCSystemAlertManager
+ __DATA_DMCSystemAlert
+ __DATA_DMCSystemAlertManager
+ __INSTANCE_METHODS_DMCSystemAlert
+ __INSTANCE_METHODS_DMCSystemAlertManager
+ __IVARS_DMCSystemAlert
+ __METACLASS_DATA_DMCSystemAlert
+ __METACLASS_DATA_DMCSystemAlertManager
+ __PROPERTIES_DMCSystemAlert
+ _block_copy_helper.14
+ _block_copy_helper.23
+ _block_copy_helper.33
+ _block_descriptor.16
+ _block_descriptor.25
+ _block_descriptor.35
+ _block_destroy_helper.15
+ _block_destroy_helper.24
+ _block_destroy_helper.34
+ _dispatch_sync
+ _kCFAllocatorDefault
+ _kCFRunLoopCommonModes
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlertTopMostKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _kCFUserNotificationOtherButtonTitleKey
+ _swift_endAccess
+ _swift_isEscapingClosureAtFileLocation
+ _symbolic Ig_
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic So14DMCSystemAlertC
+ _symbolic So21DMCSystemAlertManagerCXMT
+ _symbolic _____ So21CFUserNotificationRefa
+ _symbolic _____ So22DMCSystemAlertResponseV
+ _symbolic _____Iegy_ So22DMCSystemAlertResponseV
+ _symbolic _____IeyBy_ So22DMCSystemAlertResponseV
CStrings:
+ "@24@0:8^Q16"
+ "B32@0:8d16^@24"
+ "DMCBackgroundTask failed to extend task with error: %{public}@"
+ "DMCSystemAlert"
+ "DMCSystemAlertManager"
+ "DMCSystemAlertManager alert queue is unexpectedly empty"
+ "DMCSystemAlertManager auto-dismissing alert (%@) in %f seconds"
+ "DMCSystemAlertManager auto-dismissing alert: %@"
+ "DMCSystemAlertManager dismissed alert with response: %s"
+ "DMCSystemAlertManager displaying alert: %@"
+ "DMCSystemAlertManager encountered unknown response flags: %lu"
+ "DMCSystemAlertManager failed to create alert (%@) with error: %d"
+ "DMCSystemAlertManager failed to create run loop source for alert: %@"
+ "SBUserNotificationAlternateButtonPresentationStyle"
+ "TB,N,R"
+ "TB,N,Vdestructive"
+ "TB,N,VdismissOnLock"
+ "TB,N,VdisplayOnLockScreen"
+ "TB,N,Vforce"
+ "T^{__CFUserNotification=},N,&,Vnotification"
+ "Td,N,VdismissAfterTimeInterval"
+ "^{__CFUserNotification=}16@0:8"
+ "alternate (secondary)"
+ "alternateButtonText"
+ "com.apple.devicemanagementclient.DMCSystemAlertManager.syncQueue"
+ "com.apple.devicemanagementclient.DMCTools"
+ "completionBlock"
+ "d16@0:8"
+ "default (primary)"
+ "defaultButtonText"
+ "destructive"
+ "dismissAfterTimeInterval"
+ "dismissOnLock"
+ "displayAlert:"
+ "displayOnLockScreen"
+ "extendForInterval:error:"
+ "force"
+ "handleDeadlineActionForNagItem:"
+ "isMigrationNag"
+ "localized:"
+ "localizedFormat::"
+ "localizedOptional:"
+ "mainBundle"
+ "minimumExtensionInterval"
+ "notification"
+ "notificationParametersOutFlags:"
+ "other (tertiary)"
+ "otherButtonText"
+ "setAlternateButtonText:"
+ "setCompletionBlock:"
+ "setDefaultButtonText:"
+ "setDestructive:"
+ "setDismissAfterTimeInterval:"
+ "setDismissOnLock:"
+ "setDisplayOnLockScreen:"
+ "setForce:"
+ "setOtherButtonText:"
+ "v16@?0Q8"
+ "v24@0:8^{__CFUserNotification=}16"
+ "v24@0:8d16"
- "com.apple.devicemanagementclient.dmctools"
- "migrationMessageWithDeadline:"
- "setNotificationMessage:"

```
