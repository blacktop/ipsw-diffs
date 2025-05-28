## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2448.3.0.0.0
-  __TEXT.__text: 0x2cf934
-  __TEXT.__auth_stubs: 0x40f0
-  __TEXT.__objc_methlist: 0x14538
+2463.0.0.0.0
+  __TEXT.__text: 0x2d16ec
+  __TEXT.__auth_stubs: 0x4130
+  __TEXT.__objc_methlist: 0x145f0
   __TEXT.__const: 0x8a78
-  __TEXT.__cstring: 0x181bf
-  __TEXT.__oslogstring: 0x16e05
-  __TEXT.__gcc_except_tab: 0xd428
+  __TEXT.__cstring: 0x1826f
+  __TEXT.__oslogstring: 0x170b3
+  __TEXT.__gcc_except_tab: 0xd484
   __TEXT.__dlopen_cstrs: 0x2fb
   __TEXT.__ustring: 0x39a
-  __TEXT.__swift5_typeref: 0x2cc5
+  __TEXT.__swift5_typeref: 0x2ccd
   __TEXT.__constg_swiftt: 0x216c
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_reflstr: 0x1118

   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_capture: 0xed8
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__unwind_info: 0xe0f4
-  __TEXT.__eh_frame: 0x5a50
+  __TEXT.__unwind_info: 0xe140
+  __TEXT.__eh_frame: 0x5a58
   __TEXT.__objc_classname: 0x1fa0
-  __TEXT.__objc_methname: 0x31361
+  __TEXT.__objc_methname: 0x31527
   __TEXT.__objc_methtype: 0x4665
-  __TEXT.__objc_stubs: 0x240a0
+  __TEXT.__objc_stubs: 0x24160
   __DATA_CONST.__got: 0xed8
-  __DATA_CONST.__const: 0x58b0
+  __DATA_CONST.__const: 0x58e0
   __DATA_CONST.__objc_classlist: 0x920
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18318
-  __DATA_CONST.__objc_selrefs: 0xb430
+  __DATA_CONST.__objc_const: 0x18378
+  __DATA_CONST.__objc_selrefs: 0xb480
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__cfstring: 0xe1a0
+  __AUTH_CONST.__cfstring: 0xe1c0
   __AUTH_CONST.__objc_const: 0x7880
-  __AUTH_CONST.__const: 0xb620
+  __AUTH_CONST.__const: 0xb608
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x278
-  __AUTH_CONST.__auth_got: 0x2090
+  __AUTH_CONST.__auth_got: 0x20b0
   __AUTH.__objc_data: 0x29f0
   __AUTH.__data: 0xca0
   __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0xde8
+  __DATA.__objc_classrefs: 0xdf0
   __DATA.__objc_superrefs: 0x680
-  __DATA.__objc_ivar: 0xc6c
+  __DATA.__objc_ivar: 0xc74
   __DATA.__objc_data: 0x120
-  __DATA.__data: 0x4608
+  __DATA.__data: 0x4618
   __DATA.__objc_stublist: 0x20
-  __DATA.__bss: 0xd880
+  __DATA.__bss: 0xd890
   __DATA.__common: 0x680
   __DATA_DIRTY.__objc_data: 0x3638
   __DATA_DIRTY.__data: 0xe90

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17245
-  Symbols:   35073
-  CStrings:  13238
+  Functions: 17263
+  Symbols:   35120
+  CStrings:  13262
 
Symbols:
+ +[ICAccount(Management) defaultAccountInContext:].cold.3
+ +[ICDefaultAccountUtilities _defaultAccountIdentifierForTests]
+ +[ICDefaultAccountUtilities _setDefaultAccountIdentifierForTests:]
+ +[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:].cold.9
+ -[ICAccount setUserRecordName:]
+ -[ICCloudSyncingObject unsafelyClearChangeCountWithReason:]
+ -[ICCloudSyncingObject unsafelyClearChangeCountWithReason:].cold.1
+ -[ICCloudSyncingObject unsafelyUpdateChangeCountWithReason:]
+ -[ICCloudSyncingObject unsafelyUpdateChangeCountWithReason:].cold.1
+ -[ICCloudSyncingObject unsafelyUpdateChangeCountWithReason:].cold.2
+ -[ICCompatibilityController clearCachedDevicesForAccount:]
+ -[ICInlineAttachment .cxx_destruct]
+ -[ICInlineAttachment attachmentDataChanged]
+ -[ICInlineAttachment awakeFromFetch]
+ -[ICInlineAttachment awakeFromInsert]
+ -[ICInlineAttachment cachedDisplayText]
+ -[ICInlineAttachment didAddAttachmentDataChangedObservers]
+ -[ICInlineAttachment setCachedDisplayText:]
+ -[ICInlineAttachment setDidAddAttachmentDataChangedObservers:]
+ -[ICInlineAttachment willTurnIntoFault]
+ GCC_except_table134
+ GCC_except_table259
+ GCC_except_table267
+ _ICDefaultAccountIdentifierLock
+ _ICDefaultAccountIdentifierLockForTests
+ _OBJC_IVAR_$_ICInlineAttachment._didAddAttachmentDataChangedObservers
+ _OBJC_IVAR_$_ICInlineAttachment.cachedDisplayText
+ ___29-[ICAuthenticationState init]_block_invoke_2
+ ___39-[ICTagSelection hashtagsForObjectIDs:]_block_invoke_4
+ ___52-[ICAuthenticationState endBlockingDeauthentication]_block_invoke
+ ___52-[ICCompatibilityController fetchDevicesForAccount:]_block_invoke.13
+ ___62+[ICCloudSyncingObject deleteTemporaryAssetFilesForOperation:]_block_invoke.226
+ ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.117
+ ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.118
+ ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.118.cold.1
+ ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.14
+ ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.14.cold.1
+ ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.15
+ ___block_descriptor_40_e8_32s_e33_q24?0"ICHashtag"8"ICHashtag"16ls32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ ___block_literal_global.12
+ ___block_literal_global.136
+ ___block_literal_global.141
+ ___block_literal_global.16
+ ___block_literal_global.188
+ ___block_literal_global.209
+ ___block_literal_global.213
+ ___block_literal_global.223
+ ___block_literal_global.229
+ ___block_literal_global.293
+ ___block_literal_global.428
+ ___block_literal_global.445
+ ___block_literal_global.448
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.457
+ ___block_literal_global.459
+ ___block_literal_global.55
+ ___block_literal_global.588
+ __unnamed_array_storage.165
+ _objc_msgSend$_defaultAccountIdentifierForTests
+ _objc_msgSend$cachedDisplayText
+ _objc_msgSend$didAddAttachmentDataChangedObservers
+ _objc_msgSend$setCachedDisplayText:
+ _objc_msgSend$setDidAddAttachmentDataChangedObservers:
+ _objc_msgSend$unsafelyClearChangeCountWithReason:
+ _objc_msgSend$unsafelyUpdateChangeCountWithReason:
+ _symbolic _____Sg 8PaperKit0A17RenderableOptionsV
- -[ICAuthenticationState setCachedMainKey:forObject:].cold.2
- -[ICCloudSyncingObject updateChangeCountWithReason:].cold.4
- -[ICCloudSyncingObject updateChangeCountWithReason:].cold.5
- -[ICCompatibilityController clearCachedDevices]
- GCC_except_table125
- GCC_except_table188
- ___52-[ICCompatibilityController fetchDevicesForAccount:]_block_invoke.12
- ___62+[ICCloudSyncingObject deleteTemporaryAssetFilesForOperation:]_block_invoke.223
- ___62-[ICCloudSyncingObject authenticationStateWillDeauthenticate:]_block_invoke
- ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.115
- ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.116
- ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.116.cold.1
- ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.12.cold.1
- ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.13
- ___63+[ICDefaultAccountUtilities defaultAccountWithHTMLNoteContext:]_block_invoke.8
- ___block_descriptor_32_e33_q24?0"ICHashtag"8"ICHashtag"16l
- ___block_literal_global.11
- ___block_literal_global.119
- ___block_literal_global.138
- ___block_literal_global.143
- ___block_literal_global.15
- ___block_literal_global.185
- ___block_literal_global.206
- ___block_literal_global.210
- ___block_literal_global.220
- ___block_literal_global.226
- ___block_literal_global.290
- ___block_literal_global.425
- ___block_literal_global.441
- ___block_literal_global.444
- ___block_literal_global.447
- ___block_literal_global.450
- ___block_literal_global.453
- ___block_literal_global.455
- ___block_literal_global.585
- __unnamed_array_storage.156
- _objc_msgSend$sharedProviderForAttachment:
CStrings:
+ "-[ICAccount setUserRecordName:]"
+ "-[ICAuthenticationState deauthenticate]"
+ "-[ICCloudSyncingObject deleteChangeTokensAndReSync]"
+ "AccountDevicesCache-"
+ "AccountDevicesCacheDate-"
+ "Caching compatibility devices for account… {account: %@}%s:%d"
+ "Cannot retrieve compatibility devices for account because it has no Apple Account"
+ "Cannot retrieve compatibility devices for account because the device is offline"
+ "Error caching compatibility devices {error: %@}"
+ "Error fetching compatibility devices for account {error: %@}"
+ "Error retrieving compatibility devices {error: %@}"
+ "Failed to create system paper attachment: %@"
+ "Failed to find existing cloud object for delete error in account ID %@: %@ %@: %@"
+ "Failed to find existing cloud object for fetch error in account ID %@: %@ %@: %@"
+ "Failed to find existing cloud object for modify error in account ID %@: %@ %@: %@"
+ "Fetched compatibility devices for account {#devices: %@}"
+ "Fetching compatibility devices for account… {account: %@}%s:%d"
+ "Overriding default account ID for testing {accountID: %@}"
+ "Refusing to clear change count for object with missing cloud state {object: %@, reason: %@}"
+ "Retrieving cached compatibility devices for account… {account: %@}%s:%d"
+ "Retrieving compatibility devices for account… {account: %@}%s:%d"
+ "Returning compatibility cached devices {#devices: %@}"
+ "Returning fake compatibility devices for debugging {#devices: %@}"
+ "Serious sync issue detected"
+ "Set cached main key for object {object: %@, oldMainKey: %@, newMainKey: %@}"
+ "Setting user record name… {account: %@, userRecordName: %@}%s:%d"
+ "T@\"NSString\",C,VcachedDisplayText"
+ "TB,N,V_didAddAttachmentDataChangedObservers"
+ "_defaultAccountIdentifierForTests"
+ "_didAddAttachmentDataChangedObservers"
+ "_setDefaultAccountIdentifierForTests:"
+ "attachmentDataChanged"
+ "cachedDisplayText"
+ "clearCachedDevicesForAccount:"
+ "createSystemPaperAttachmentWithPKDrawing:inNote:"
+ "didAddAttachmentDataChangedObservers"
+ "setCachedDisplayText:"
+ "setDidAddAttachmentDataChangedObservers:"
+ "unsafelyClearChangeCountWithReason:"
+ "unsafelyUpdateChangeCountWithReason:"
- "Authenticated object with passphrase {object: %@}"
- "Caching devices for account… {account: %@}%s:%d"
- "Cannot retrieve devices for account because it has no Apple Account"
- "Cannot retrieve devices for account because the device is offline"
- "Error caching devices {error: %@}"
- "Error fetching devices for account {error: %@}"
- "Error retrieving devices {error: %@}"
- "Fetched devices for account {#devices: %@}"
- "Fetching devices for account… {account: %@}%s:%d"
- "ICCompatibilityControllerDevices"
- "ICCompatibilityControllerDevicesDate"
- "Retrieving cached devices for account… {account: %@}%s:%d"
- "Retrieving devices for account… {account: %@}%s:%d"
- "Returning cached devices"
- "Returning fake devices for debugging"
- "clearCachedDevices"

```
