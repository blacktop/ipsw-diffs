## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2126.10.4.0.0
-  __TEXT.__text: 0xc7544
-  __TEXT.__objc_methlist: 0x11314
+2131.10.1.2.7
+  __TEXT.__text: 0xc7c80
+  __TEXT.__objc_methlist: 0x11344
   __TEXT.__const: 0x620
-  __TEXT.__gcc_except_tab: 0x202c
-  __TEXT.__oslogstring: 0x7195
-  __TEXT.__cstring: 0x7128
-  __TEXT.__dlopen_cstrs: 0xaaf
-  __TEXT.__ustring: 0x104
-  __TEXT.__unwind_info: 0x3530
+  __TEXT.__gcc_except_tab: 0x207c
+  __TEXT.__oslogstring: 0x7217
+  __TEXT.__cstring: 0x720c
+  __TEXT.__dlopen_cstrs: 0xb4f
+  __TEXT.__ustring: 0x1f4
+  __TEXT.__unwind_info: 0x3570
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x28a8
+  __DATA_CONST.__const: 0x28d8
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c30
+  __DATA_CONST.__objc_selrefs: 0x8c48
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x678
   __DATA_CONST.__got: 0xfd0
   __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0x59e0
-  __AUTH_CONST.__objc_const: 0x2a350
+  __AUTH_CONST.__cfstring: 0x5a20
+  __AUTH_CONST.__objc_const: 0x2a388
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78

   __AUTH.__data: 0x198
   __DATA.__objc_ivar: 0x14a4
   __DATA.__data: 0x2bf0
-  __DATA.__bss: 0xab8
+  __DATA.__bss: 0xad8
   __DATA_DIRTY.__objc_data: 0xb40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5897
-  Symbols:   13907
-  CStrings:  1613
+  Functions: 5906
+  Symbols:   13917
+  CStrings:  1618
 
Symbols:
+ -[SFShareSheetSlotManager fetchExistingShareForFileOrFolderURL:completionHandler:]
+ -[SHSheetInteractor fetchExistingShareForFileOrFolderURL:completionHandler:]
+ -[SHSheetServiceManager fetchExistingShareForFileOrFolderURL:completionHandler:]
+ -[UICollaborationInviteWithLinkActivity _systemImageName]
+ GCC_except_table65
+ ___87-[UICollaborationInviteWithLinkActivity canPerformWithCollaborationItem:activityItems:]_block_invoke
+ ___getSFUIActivityViewControllerConfiguratorClass_block_invoke
+ _getSFUIActivityViewControllerConfiguratorClass.softClass
+ _objc_msgSend$adaptivePresentationStyleForTraitCollection:
+ _objc_msgSend$addItemAllowedForCollaborationItem:completionHandler:
+ _objc_msgSend$fetchExistingShareForFileOrFolderURL:completionHandler:
+ _objc_msgSend$popoverWidth
- -[UICollaborationInviteWithLinkActivity _activityImage]
- -[UICollaborationInviteWithLinkActivity _activitySettingsImage]
CStrings:
+ "Add Access"
+ "If you share this with a group, you have to approve access for each member. Or you can allow anyone with the link for instant access."
+ "SFUIActivityViewControllerConfigurator"
+ "SHARE_LINK_ACCESS_REQUESTS_ALREADY_ON_MESSAGE"
+ "SHARE_LINK_ACCESS_REQUESTS_UNSUPPORTED_MESSAGE"
+ "Sharing/SFShareSheetSlotManager/fetchExistingShareForFileOrFolderURL"
+ "Timed out waiting for addItemAllowed, returning default YES."
+ "To add access for people, enter their email addresses or choose from your Contacts list.\n\nAdding access doesn’t share a link. After adding, let these participants know they have access."
+ "person.badge.plus"
- "CopyLinkActivity"
- "Create Link"
- "Create a link by adding people who you‘d like to collaborate with"
- "SHARE_LINK_ACCESS_REQUESTS_ON_MESSAGE"
```
