## ScreenTimeUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Versions/A/ScreenTimeUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`

```diff

-645.1.401.0.0
-  __TEXT.__text: 0x31508
-  __TEXT.__objc_methlist: 0x1c28
-  __TEXT.__const: 0xbb4
-  __TEXT.__cstring: 0x1936
-  __TEXT.__gcc_except_tab: 0x3fc
-  __TEXT.__oslogstring: 0x28fd
+649.0.0.0.0
+  __TEXT.__text: 0x33ff0
+  __TEXT.__objc_methlist: 0x1ca0
+  __TEXT.__const: 0xc34
+  __TEXT.__cstring: 0x1956
+  __TEXT.__gcc_except_tab: 0x4a0
+  __TEXT.__oslogstring: 0x29cd
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x17f2
-  __TEXT.__swift5_fieldmd: 0x1f4
-  __TEXT.__constg_swiftt: 0x5c0
+  __TEXT.__swift5_typeref: 0x189e
+  __TEXT.__swift5_fieldmd: 0x21c
+  __TEXT.__constg_swiftt: 0x5ec
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_reflstr: 0x12f
+  __TEXT.__swift5_reflstr: 0x15f
   __TEXT.__swift5_proto: 0x28
-  __TEXT.__swift5_types: 0x38
-  __TEXT.__swift5_capture: 0x80
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_capture: 0x128
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0xb28
-  __TEXT.__eh_frame: 0xa8
+  __TEXT.__unwind_info: 0xc08
+  __TEXT.__eh_frame: 0x168
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb68
-  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__const: 0xc80
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a00
+  __DATA_CONST.__objc_selrefs: 0x1a30
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__got: 0x6f0
-  __AUTH_CONST.__const: 0x5d8
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x2f08
-  __AUTH_CONST.__auth_got: 0xc00
-  __AUTH.__objc_data: 0x950
-  __AUTH.__data: 0x258
-  __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x7e8
+  __DATA_CONST.__got: 0x730
+  __AUTH_CONST.__const: 0x740
+  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__objc_const: 0x3048
+  __AUTH_CONST.__auth_got: 0xd38
+  __AUTH.__objc_data: 0xa10
+  __AUTH.__data: 0x280
+  __DATA.__objc_ivar: 0x1a4
+  __DATA.__data: 0x848
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x480
   __DATA.__common: 0x28

   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
+  - /System/Library/PrivateFrameworks/AskToCore.framework/Versions/A/AskToCore
   - /System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/Versions/A/DeviceManagement
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1052
-  Symbols:   2216
-  CStrings:  402
+  Functions: 1110
+  Symbols:   2286
+  CStrings:  403
 
Symbols:
+ -[STBlockingViewController _presentAskForMoreTimeOptions:]
+ -[STBlockingViewController _presentIgnoreLimitOptionsWithoutPasscode]
+ -[STBlockingViewController _refreshShouldAllowOneMoreMinuteWithCompletion:]
+ -[STBlockingViewController askToMessagesComposeCallbackReceiver]
+ -[STBlockingViewController resolvedShouldAllowOneMoreMinute]
+ -[STBlockingViewController resolvingPolicyOptions]
+ -[STBlockingViewController setAskToMessagesComposeCallbackReceiver:]
+ -[STBlockingViewController setResolvedShouldAllowOneMoreMinute:]
+ -[STBlockingViewController setResolvingPolicyOptions:]
+ -[STLockoutPolicyController shouldAllowOneMoreMinuteWithCompletionHandler:]
+ -[STLockoutViewController _presentIgnoreLimitActionSheetAllowingOneMoreMinute:]
+ -[STLockoutViewController _presentUnlockedAskOrApproveActionSheetAllowingOneMoreMinute:]
+ GCC_except_table116
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table34
+ GCC_except_table38
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table92
+ OBJC_IVAR_$_STBlockingViewController._askToMessagesComposeCallbackReceiver
+ OBJC_IVAR_$_STBlockingViewController._resolvedShouldAllowOneMoreMinute
+ OBJC_IVAR_$_STBlockingViewController._resolvingPolicyOptions
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_STAskToMessagesComposeCallbackReceiver
+ _OBJC_METACLASS_$_STAskToMessagesComposeCallbackReceiver
+ _OUTLINED_FUNCTION_11
+ __75-[STBlockingViewController _refreshShouldAllowOneMoreMinuteWithCompletion:]_block_invoke
+ __75-[STLockoutPolicyController shouldAllowOneMoreMinuteWithCompletionHandler:]_block_invoke
+ __79-[STLockoutViewController _presentIgnoreLimitActionSheetAllowingOneMoreMinute:]_block_invoke
+ __88-[STLockoutViewController _presentUnlockedAskOrApproveActionSheetAllowingOneMoreMinute:]_block_invoke
+ __DATA_STAskToMessagesComposeCallbackReceiver
+ __INSTANCE_METHODS_STAskToMessagesComposeCallbackReceiver
+ __IVARS_STAskToMessagesComposeCallbackReceiver
+ __METACLASS_DATA_STAskToMessagesComposeCallbackReceiver
+ ___58-[STBlockingViewController _presentAskForMoreTimeOptions:]_block_invoke
+ ___58-[STBlockingViewController _presentAskForMoreTimeOptions:]_block_invoke_2
+ ___58-[STBlockingViewController _presentAskForMoreTimeOptions:]_block_invoke_3
+ ___58-[STBlockingViewController _presentAskForMoreTimeOptions:]_block_invoke_4
+ ___58-[STBlockingViewController _presentAskForMoreTimeOptions:]_block_invoke_5
+ ___69-[STBlockingViewController _presentIgnoreLimitOptionsWithoutPasscode]_block_invoke
+ ___69-[STBlockingViewController _presentIgnoreLimitOptionsWithoutPasscode]_block_invoke_2
+ ___69-[STBlockingViewController _presentIgnoreLimitOptionsWithoutPasscode]_block_invoke_3
+ ___69-[STBlockingViewController _presentIgnoreLimitOptionsWithoutPasscode]_block_invoke_4
+ ___75-[STBlockingViewController _refreshShouldAllowOneMoreMinuteWithCompletion:]_block_invoke
+ ___75-[STLockoutPolicyController shouldAllowOneMoreMinuteWithCompletionHandler:]_block_invoke
+ ___79-[STLockoutViewController _presentIgnoreLimitActionSheetAllowingOneMoreMinute:]_block_invoke
+ ___88-[STLockoutViewController _presentUnlockedAskOrApproveActionSheetAllowingOneMoreMinute:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSNumber"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e28_v24?0"NSUUID"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32bs40w_e30_v24?0"NSNumber"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_49_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32bs40w_e28_v24?0"NSUUID"8"NSError"16lw40l8s32l8
+ ___swift__destructor
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __swiftEmptyDictionarySingleton
+ _dispatch_sync
+ _objc_alloc_init
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_presentAskForMoreTimeOptions:
+ _objc_msgSend$_presentIgnoreLimitActionSheetAllowingOneMoreMinute:
+ _objc_msgSend$_presentIgnoreLimitOptionsWithoutPasscode
+ _objc_msgSend$_presentUnlockedAskOrApproveActionSheetAllowingOneMoreMinute:
+ _objc_msgSend$_refreshShouldAllowOneMoreMinuteWithCompletion:
+ _objc_msgSend$askToMessagesComposeCallbackReceiver
+ _objc_msgSend$resolvedShouldAllowOneMoreMinute
+ _objc_msgSend$resolvingPolicyOptions
+ _objc_msgSend$setAskToMessagesComposeCallbackReceiver:
+ _objc_msgSend$setCallbackForQuestionIdentifier:callback:
+ _objc_msgSend$setResolvedShouldAllowOneMoreMinute:
+ _objc_msgSend$setResolvingPolicyOptions:
+ _objc_msgSend$shouldAllowOneMoreMinuteForBundleIdentifier:completionHandler:
+ _objc_msgSend$shouldAllowOneMoreMinuteForCategoryIdentifier:completionHandler:
+ _objc_msgSend$shouldAllowOneMoreMinuteForWebDomain:completionHandler:
+ _objc_msgSend$shouldAllowOneMoreMinuteWithCompletionHandler:
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_x1
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x27
+ _swift_retain_x8
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _symbolic Ieg_
+ _symbolic IeyB_
+ _symbolic Ig_
+ _symbolic SDy__________G 10Foundation4UUIDV 9AskToCore25ATDaemonConnectionManagerC
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic So17OS_dispatch_queueC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 12ScreenTimeUI36AskToMessagesComposeCallbackReceiverC
+ _symbolic _____ 9AskToCore25ATDaemonConnectionManagerC
+ _symbolic _____Sg 9AskToCore25ATDaemonConnectionManagerC
+ _symbolic _____SgXw 12ScreenTimeUI36AskToMessagesComposeCallbackReceiverC
+ _symbolic _____SgXwz_Xx 12ScreenTimeUI36AskToMessagesComposeCallbackReceiverC
+ _symbolic ___________t 10Foundation4UUIDV 9AskToCore25ATDaemonConnectionManagerC
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV 9AskToCore25ATDaemonConnectionManagerC
+ _symbolic ytIeAgHr_
- -[STBlockingViewController _askForMoreTimeMenuProvider]
- -[STBlockingViewController _enterScreenTimePasscodeAction]
- -[STBlockingViewController _ignoreForTodayAction]
- -[STBlockingViewController _ignoreLimitMenuProvider]
- -[STBlockingViewController _oneMoreMinuteAction]
- -[STBlockingViewController _remindMeIn15MinutesAction]
- -[STBlockingViewController _sendRequestAction]
- -[STLockoutPolicyController shouldAllowOneMoreMinute]
- GCC_except_table112
- GCC_except_table118
- GCC_except_table121
- GCC_except_table124
- GCC_except_table130
- GCC_except_table21
- GCC_except_table30
- GCC_except_table31
- GCC_except_table39
- GCC_except_table52
- GCC_except_table62
- GCC_except_table88
- _OBJC_CLASS_$_UIAction
- _OBJC_CLASS_$_UIMenu
- __57-[STLockoutViewController _actionIgnoreLimitActionSheet:]_block_invoke
- __65-[STLockoutViewController _actionUnlockedAskOrApproveActionSheet]_block_invoke
- ___46-[STBlockingViewController _sendRequestAction]_block_invoke
- ___48-[STBlockingViewController _oneMoreMinuteAction]_block_invoke
- ___49-[STBlockingViewController _ignoreForTodayAction]_block_invoke
- ___52-[STBlockingViewController _ignoreLimitMenuProvider]_block_invoke
- ___54-[STBlockingViewController _remindMeIn15MinutesAction]_block_invoke
- ___55-[STBlockingViewController _askForMoreTimeMenuProvider]_block_invoke
- ___55-[STBlockingViewController _showAskForMoreTimeOptions:]_block_invoke_2
- ___55-[STBlockingViewController _showAskForMoreTimeOptions:]_block_invoke_3
- ___55-[STBlockingViewController _showAskForMoreTimeOptions:]_block_invoke_4
- ___55-[STBlockingViewController _showAskForMoreTimeOptions:]_block_invoke_5
- ___58-[STBlockingViewController _enterScreenTimePasscodeAction]_block_invoke
- ___66-[STBlockingViewController _showIgnoreLimitOptionsWithoutPasscode]_block_invoke_2
- ___66-[STBlockingViewController _showIgnoreLimitOptionsWithoutPasscode]_block_invoke_3
- ___66-[STBlockingViewController _showIgnoreLimitOptionsWithoutPasscode]_block_invoke_4
- ___block_descriptor_40_e8_32s_e18_v16?0"UIAction"8ls32l8
- ___block_descriptor_40_e8_32s_e28_"UIMenu"24?08"NSArray"16ls32l8
- _objc_msgSend$_enterScreenTimePasscodeAction
- _objc_msgSend$_ignoreForTodayAction
- _objc_msgSend$_oneMoreMinuteAction
- _objc_msgSend$_remindMeIn15MinutesAction
- _objc_msgSend$_sendRequestAction
- _objc_msgSend$actionWithTitle:image:identifier:handler:
- _objc_msgSend$menuWithTitle:children:
- _objc_msgSend$shouldAllowOneMoreMinuteForBundleIdentifier:error:
- _objc_msgSend$shouldAllowOneMoreMinuteForCategoryIdentifier:error:
- _objc_msgSend$shouldAllowOneMoreMinuteForWebDomain:error:
- _objc_msgSend$systemImageNamed:
CStrings:
+ "Ask for time finished with no request identifier"
+ "Failed to fetch One More Minute policy: %{public}@"
+ "Request staged request with id %{public}@ successfully, waiting on user feedback to transition to pending state"
+ "User sent the request, updating UI for pending ask"
+ "com.apple.screentime.connectionMap"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
- "@\"UIMenu\"24@?0@8@\"NSArray\"16"
- "Failed to fetch One More Minute policy for %{public}@: %{public}@"
- "clock"
- "hourglass.badge.plus"
- "v16@?0@\"UIAction\"8"
- "xmark.circle"
```
