## MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

-3826.600.15.2.1
-  __TEXT.__text: 0x458564
-  __TEXT.__auth_stubs: 0x5dd0
+3826.600.32.0.0
+  __TEXT.__text: 0x450bf8
+  __TEXT.__auth_stubs: 0x5d90
   __TEXT.__objc_stubs: 0x40c80
-  __TEXT.__objc_methlist: 0x24c2c
-  __TEXT.__gcc_except_tab: 0x52614
-  __TEXT.__objc_methname: 0x5fda8
-  __TEXT.__cstring: 0x1cc3d
+  __TEXT.__objc_methlist: 0x24c1c
+  __TEXT.__gcc_except_tab: 0x52644
+  __TEXT.__objc_methname: 0x5fedc
+  __TEXT.__cstring: 0x1cc2d
   __TEXT.__objc_classname: 0x4f94
   __TEXT.__objc_methtype: 0x11522
-  __TEXT.__const: 0xe510
-  __TEXT.__oslogstring: 0x12cc1
+  __TEXT.__const: 0xe410
+  __TEXT.__oslogstring: 0x12713
   __TEXT.__ustring: 0x896
   __TEXT.__swift5_typeref: 0x931e
-  __TEXT.__swift5_capture: 0x32c0
+  __TEXT.__swift5_capture: 0x3170
   __TEXT.__swift5_reflstr: 0x2cb4
   __TEXT.__swift5_assocty: 0x13f0
   __TEXT.__constg_swiftt: 0x33b8
   __TEXT.__swift5_fieldmd: 0x2588
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_proto: 0x928
+  __TEXT.__swift5_proto: 0x91c
   __TEXT.__swift5_types: 0x424
   __TEXT.__swift_as_entry: 0x390
   __TEXT.__swift_as_ret: 0x308
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x17610
+  __TEXT.__unwind_info: 0x175e8
   __TEXT.__eh_frame: 0x2918
-  __DATA_CONST.__auth_got: 0x2ef8
-  __DATA_CONST.__got: 0x3748
-  __DATA_CONST.__auth_ptr: 0x1ce8
-  __DATA_CONST.__const: 0x15430
+  __DATA_CONST.__auth_got: 0x2ed8
+  __DATA_CONST.__got: 0x3750
+  __DATA_CONST.__auth_ptr: 0x1e08
+  __DATA_CONST.__const: 0x15138
   __DATA_CONST.__cfstring: 0xe600
   __DATA_CONST.__objc_classlist: 0xde8
-  __DATA_CONST.__objc_catlist: 0xf8
+  __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0xb38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x218

   __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__objc_doubleobj: 0x220
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x34be8
-  __DATA.__objc_selrefs: 0x14640
-  __DATA.__objc_ivar: 0x1f54
+  __DATA.__objc_const: 0x34be0
+  __DATA.__objc_selrefs: 0x14648
+  __DATA.__objc_ivar: 0x1f58
   __DATA.__objc_data: 0xac30
-  __DATA.__data: 0xda68
-  __DATA.__bss: 0x120f8
+  __DATA.__data: 0xda18
+  __DATA.__bss: 0x11f78
   __DATA.__common: 0x6b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 20844
-  Symbols:   4009
-  CStrings:  21298
+  Functions: 20793
+  Symbols:   4004
+  CStrings:  21286
 
Symbols:
+ _kEMPayloadKeyCategorizationEnabled
- _$s10AppIntents16EntityIdentifierV3for10identifierACxm_2IDQztcAA0aC0RzlufC
- _$s17_AppIntents_UIKit016UICollectionViewaB10DataSourceMp
- _$s17_AppIntents_UIKit016UICollectionViewaB10DataSourceP010collectionE0_28appEntityIdentifierForItemAt0aB00jK0VSgSo0dE0C_10Foundation9IndexPathVtFTq
- _$sSo14NSUserActivityC10AppIntentsE19appEntityIdentifierAC0fG0VSgvs
- _$sSo16UICollectionViewC17_AppIntents_UIKitE03appD10DataSourceAC0abcdgH0_pSgvs
- _$sSo6UIViewC17_AppIntents_UIKitE19appEntityIdentifier0bC00fG0VSgvs
CStrings:
+ "Content requests differs %{BOOL}d, singleMessageConfigurationDiffers %{BOOL}d, messageListConfigurationDiffers %{BOOL}d for cell with itemID: %{public}@"
+ "TB,N,GisConfiguredForGroupedSenderMessageListDisplay,V_configuredForGroupedSenderMessageListDisplay"
+ "_configuredForGroupedSenderMessageListDisplay"
+ "configuredForGroupedSenderMessageListDisplay"
+ "ef_stringByTrimmingWhitespaceAndDuplicateSpaces"
+ "isCategorizationActionAllowed"
+ "isCategorizationActionAllowedForMessageViewController:"
+ "isConfiguredForGroupedSenderMessageListDisplay"
+ "setConfiguredForGroupedSenderMessageListDisplay:"
+ "shouldDisplayBannerIfIsShowingGroupedSenderMessageList:"
+ "viewingEndedForMessage:data:"
- "#ViewIntegration Associating DraftMessageEntity with MFMailComposeController via ComposeNavigationController"
- "#ViewIntegration Associating DraftMessageEntity with a new userActivity on MFMailComposeController via ComposeNavigationController"
- "#ViewIntegration Associating DraftMessageEntity with userActivity on MFMailComposeController via ComposeNavigationController"
- "#ViewIntegration ConversationViewController collectionView appEntityIdentifier %s"
- "#ViewIntegration ConversationViewController collectionView appEntityIdentifierForItemAt indexPath is nil!"
- "#ViewIntegration EMMessageListItem was not EMMessage and had no displayMessage result available. not annotating the view"
- "#ViewIntegration MailboxPickerCollectionHelper collectionView appEntityIdentifierForItemAt indexPath is nil!"
- "#ViewIntegration MailboxPickerCollectionHelper collectionView appEntityIdentifierForItemAt indexPath: %s"
- "#ViewIntegration MessageListViewController collectionView appEntityIdentifier %s"
- "#ViewIntegration MessageListViewController collectionView appEntityIdentifier nil!"
- "#ViewIntegration Updating userActivity on ConversationViewController with MailMessageEntity ID: %s"
- "#ViewIntegration Updating userActivity on ConversationViewController with nil MailMessageEntity ID"
- "#ViewIntegration found EMMessage, annotating the encoded ID"
- "#ViewIntegration found EMMessageObjectID on EMMessageListItem, annotating the globalMessageID only"
- "Composing Email"
- "Content requests differs %{BOOL}d, singleMessageConfigurationDiffers %{BOOL}d"
- "MobileMail4"
- "associateUserActivityWithEntityWithAutosaveId:"
- "associateViewWithEntityWithAutosaveId:"
- "setAllowNotAuthenticatedBanner:"
- "setAppIntentsDataSource"
- "updateEntityUserActivityState:"
- "viewingEndedForMessage:"

```
