## FMDCFUTheftAndLossReminderExtension

> `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/FMDCFUTheftAndLossReminderExtension`

```diff

-442.30.6.9.13
-  __TEXT.__text: 0x0
-  __TEXT.__auth_stubs: 0x10
-  __DATA_CONST.__auth_got: 0x8
+442.30.6.9.19
+  __TEXT.__text: 0x111c
+  __TEXT.__auth_stubs: 0x190
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0x38
+  __TEXT.__const: 0x30
+  __TEXT.__cstring: 0x101
+  __TEXT.__oslogstring: 0x2dd
+  __TEXT.__objc_classname: 0x24
+  __TEXT.__objc_methname: 0x2d9
+  __TEXT.__objc_methtype: 0x2d
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__objc_const: 0x90
+  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_data: 0x50
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI
+  - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC785910-A3D9-3CC3-91A0-E921391628A6
-  Functions: 0
-  Symbols:   3
-  CStrings:  0
+  UUID: FBF8209D-E8B2-3614-9882-8070AE29A381
+  Functions: 24
+  Symbols:   46
+  CStrings:  65
 
Symbols:
+ _FindMyTheftAndLossReminderUseCaseSettings
+ _MGCopyAnswerWithError
+ _OBJC_CLASS_$_FLExtensionViewController
+ _OBJC_CLASS_$_FMDSharedConfiguration
+ _OBJC_CLASS_$_FindMyRepairViewContext
+ _OBJC_CLASS_$_FindMyRepairViewFactory
+ _OBJC_CLASS_$_FindMyTheftAndLossReminderContext
+ _OBJC_CLASS_$_FindMyTheftAndLossReminderFactory
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UINavigationController
+ _OBJC_METACLASS_$_FLExtensionViewController
+ _OBJC_METACLASS_$_NSObject
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ ___CFConstantStringClassReference
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __dispatch_main_q
+ __objc_empty_cache
+ __os_log_default
+ __os_log_error_impl
+ __os_log_impl
+ _dispatch_async
+ _objc_alloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x8
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _os_log_type_enabled
CStrings:
+ "%s - %d"
+ "%s - %d - Failed to pull the serial number. Error (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/GreenTorch/FMDCFUTheftAndLossReminderExtension/FMDCFUTheftAndLossReminderExtension.m"
+ "Cancelling CFU reminder"
+ "Clear pending CFU failed with %@"
+ "Cleared pending CFU"
+ "Clearing repair CFU failed with %@"
+ "Configuring repair or trade-in"
+ "Enabled Find My, clearing pending CFU"
+ "FMDCFUTheftAndLossReminderExtension"
+ "Failed to create repair view controller"
+ "Failed to create view controller but also no error"
+ "Failed to create view controller. Error (%@)"
+ "Failed to enable Find My from CFU reminder"
+ "Missing device userInfo from repair CFU %@ (finishing)"
+ "Repair CFU cleared"
+ "Repair or trade-in cancelled by user"
+ "Repair or trade-in enabled"
+ "Repair or trade-in failed"
+ "SerialNumber"
+ "Unrecgonized action %lu"
+ "Unrecognized CFU identifier %@ (finishing)"
+ "_configureRepairWithFindMyID:completion:"
+ "_configureTheftAndLossReminderWithCompletion:"
+ "addChildViewController:"
+ "addSubview:"
+ "bounds"
+ "clearRepairCFUWithDeviceID:reply:"
+ "clearTheftAndLossCFUWithReply:"
+ "com.apple.findmy"
+ "com.apple.findmy.repair."
+ "device"
+ "didMoveToParentViewController:"
+ "finishProcessing"
+ "followUpPerformUpdateWithCompletionHandler"
+ "followUpPerformUpdateWithCompletionHandler:"
+ "hasPrefix:"
+ "initWithDeviceIdentifier:"
+ "initWithRootViewController:"
+ "initWithUseCase:serialNumber:"
+ "isEqualToString:"
+ "makeRepairViewControllerWithContext:completionHandler:"
+ "objectForKeyedSubscript:"
+ "presentViewController:animated:completion:"
+ "processFollowUpItem: %@, action: %@"
+ "processFollowUpItem:selectedAction:completion:"
+ "reminderViewControllerForContext:actionHandler:completion:"
+ "setAutoresizingMask:"
+ "setFrame:"
+ "setModalInPresentation:"
+ "sharedInstance"
+ "uniqueIdentifier"
+ "userInfo"
+ "v16@?0@\"NSError\"8"
+ "v16@?0Q8"
+ "v24@0:8@?16"
+ "v24@?0@\"UIViewController\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "v40@0:8@16@24@?32"
+ "v8@?0"
+ "view"

```
