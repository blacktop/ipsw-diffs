## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-85.1.0.0.0
-  __TEXT.__text: 0x12a814
+85.3.0.0.0
+  __TEXT.__text: 0x12b310
   __TEXT.__auth_stubs: 0x2680
-  __TEXT.__objc_methlist: 0x947c
+  __TEXT.__objc_methlist: 0x9534
   __TEXT.__const: 0x1948
-  __TEXT.__cstring: 0xb2cc
-  __TEXT.__oslogstring: 0x8e53
+  __TEXT.__cstring: 0xb44c
+  __TEXT.__oslogstring: 0x8e46
   __TEXT.__gcc_except_tab: 0x13b4
   __TEXT.__ustring: 0xe6
   __TEXT.__swift5_typeref: 0x2f7a
-  __TEXT.__constg_swiftt: 0x13b8
-  __TEXT.__swift5_reflstr: 0x7ce
-  __TEXT.__swift5_fieldmd: 0x96c
+  __TEXT.__constg_swiftt: 0x13e8
+  __TEXT.__swift5_reflstr: 0x81e
+  __TEXT.__swift5_fieldmd: 0x984
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x108
   __TEXT.__swift5_proto: 0xc0
   __TEXT.__swift5_types: 0xcc
   __TEXT.__swift5_capture: 0xc70
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4a4c
+  __TEXT.__unwind_info: 0x4aa8
   __TEXT.__eh_frame: 0x14d0
-  __TEXT.__objc_classname: 0x1114
-  __TEXT.__objc_methname: 0x1b2b3
-  __TEXT.__objc_methtype: 0x3b1e
-  __TEXT.__objc_stubs: 0x13940
+  __TEXT.__objc_classname: 0x111c
+  __TEXT.__objc_methname: 0x1b3a5
+  __TEXT.__objc_methtype: 0x3b42
+  __TEXT.__objc_stubs: 0x13a00
   __DATA_CONST.__got: 0x708
-  __DATA_CONST.__const: 0x3c00
+  __DATA_CONST.__const: 0x3c30
   __DATA_CONST.__objc_classlist: 0x4a0
-  __DATA_CONST.__objc_catlist: 0xb8
+  __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x19630
-  __DATA_CONST.__objc_selrefs: 0x68b0
+  __DATA_CONST.__objc_const: 0x196c0
+  __DATA_CONST.__objc_selrefs: 0x68e8
   __DATA_CONST.__objc_arraydata: 0x4d0
-  __AUTH_CONST.__cfstring: 0x8a80
-  __AUTH_CONST.__objc_const: 0x3d70
-  __AUTH_CONST.__const: 0x48f0
+  __AUTH_CONST.__cfstring: 0x8ae0
+  __AUTH_CONST.__objc_const: 0x3db0
+  __AUTH_CONST.__const: 0x4900
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH_CONST.__auth_got: 0x1350
-  __AUTH.__objc_data: 0x42e0
+  __AUTH.__objc_data: 0x4320
   __AUTH.__data: 0x790
   __DATA.__objc_protorefs: 0xa0
   __DATA.__objc_classrefs: 0x840
   __DATA.__objc_superrefs: 0x278
   __DATA.__objc_ivar: 0x67c
   __DATA.__objc_data: 0x128
-  __DATA.__data: 0x25e0
-  __DATA.__bss: 0x1bf0
+  __DATA.__data: 0x25f0
+  __DATA.__bss: 0x1c00
   __DATA.__common: 0x128
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4B5E4CDC-4ED7-3E28-8E21-F80D80757F15
-  Functions: 6785
-  Symbols:   14458
-  CStrings:  8841
+  UUID: 2FC371A6-30AD-3E3D-A412-72C32A6BCD39
+  Functions: 6826
+  Symbols:   14492
+  CStrings:  8865
 
Symbols:
+ +[FBKSharedConstants isFormItemsDisabled]
+ +[UIAlertController(FBAIcon) fbaAlertControllerWithTitle:message:preferredStyle:]
+ +[iFBKUtils initialize]
+ +[iFBKUtils isFBAVisibleInHomeScreen]
+ +[iFBKUtils wasFBAVisibleAtFirstLaunch]
+ -[FBKHTTPClient _shouldSimulateInvalidSessionWithRequestAndHalt:successHandler:errorHandler:]
+ -[FBKLaunchAction isShowContentItemAction]
+ -[FBKLaunchAction launchesInbox]
+ _FBKDisableFormItems
+ _FBKImageNameAlertControllerIcon
+ __OBJC_$_CATEGORY_UIAlertController_$_FBAIcon
+ __OBJC_$_CLASS_METHODS_UIAlertController(FBAIcon)
+ __PROTOCOLS__TtC12FeedbackCore12FBKTopicCell.7
+ __PROTOCOLS__TtC12FeedbackCore21FBKAddAttachmentsCell.5
+ ___34-[FBKAnnouncement fullHTMLContent]_block_invoke.cold.1
+ ___39+[iFBKUtils wasFBAVisibleAtFirstLaunch]_block_invoke
+ ___61-[FBKSeedPortalAPI getFormResponseStubWithID:withCompletion:]_block_invoke.226
+ ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.188
+ ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.188.cold.1
+ ___67-[FBKSeedPortalAPI fetchAnnouncementForContentItem:withCompletion:]_block_invoke.238
+ ___68-[FBKSeedPortalAPI getFileDownloadURLForFilePromiseUUID:completion:]_block_invoke.256
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.163
+ ___79-[FBKSeedPortalAPI createFormResponseForBugForm:inTeam:appToken:success:error:]_block_invoke.209
+ ___87-[FBKSeedPortalAPI fetchBugFormWithID:forTeamID:requestPlugIns:appToken:success:error:]_block_invoke.201
+ ___block_literal_global.164
+ ___block_literal_global.255
+ ___block_literal_global.262
+ ___block_literal_global.67
+ __unnamed_array_storage.220
+ _objc_msgSend$fbaAlertControllerWithTitle:message:preferredStyle:
+ _objc_msgSend$getPreferencesValueforKey:domain:
+ _objc_msgSend$isFBAVisibleInHomeScreen
+ _objc_msgSend$isFormItemsDisabled
+ _objc_msgSend$isShowContentItemAction
+ _objc_msgSend$wasFBAVisibleAtFirstLaunch
+ _wasFBAVisibleAtFirstLaunch._wasVisible
+ _wasFBAVisibleAtFirstLaunch.onceToken
- -[FBKGroupedDevice shortDescription]
- __PROTOCOLS__TtC12FeedbackCore12FBKTopicCell.5
- __PROTOCOLS__TtC12FeedbackCore21FBKAddAttachmentsCell.3
- ___61-[FBKSeedPortalAPI getFormResponseStubWithID:withCompletion:]_block_invoke.225
- ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.187
- ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.187.cold.1
- ___67-[FBKSeedPortalAPI fetchAnnouncementForContentItem:withCompletion:]_block_invoke.237
- ___68-[FBKSeedPortalAPI getFileDownloadURLForFilePromiseUUID:completion:]_block_invoke.255
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.162
- ___79-[FBKSeedPortalAPI createFormResponseForBugForm:inTeam:appToken:success:error:]_block_invoke.208
- ___87-[FBKSeedPortalAPI fetchBugFormWithID:forTeamID:requestPlugIns:appToken:success:error:]_block_invoke.200
- ___block_literal_global.161
- ___block_literal_global.259
- ___block_literal_global.70
- __unnamed_array_storage.216
- __unnamed_array_storage.218
CStrings:
+ "%@://%@?item=%@"
+ "<head>"
+ "<head>\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
+ "@40@0:8@16@24q32"
+ "B40@0:8@16@?24@?32"
+ "Calling boxed request error handler"
+ "DisableFormItems"
+ "FBAIcon"
+ "Failed to load AnnouncementContent with error [%{public}@]"
+ "Td,N,VhorizontalFrameInset"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
+ "_shouldSimulateInvalidSessionWithRequestAndHalt:successHandler:errorHandler:"
+ "fbaAlertControllerWithTitle:message:preferredStyle:"
+ "feedback-assistant-icon-masked"
+ "isFBAVisibleInHomeScreen"
+ "isFormItemsDisabled"
+ "isShowContentItemAction"
+ "launchesInbox"
+ "wasFBAVisibleAtFirstLaunch"
- "%@://%@?feedback=%@"
- "Calling boxed request error handler on authentication request"
- "Session did become invalid while logging out."

```
