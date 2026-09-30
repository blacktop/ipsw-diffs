## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2131.10.1.2.11
-  __TEXT.__text: 0xc3880
-  __TEXT.__objc_methlist: 0x11344
+2131.20.65.2.1
+  __TEXT.__text: 0xc4668
+  __TEXT.__objc_methlist: 0x1141c
   __TEXT.__const: 0x620
-  __TEXT.__gcc_except_tab: 0x207c
-  __TEXT.__oslogstring: 0x7217
-  __TEXT.__cstring: 0x720c
-  __TEXT.__dlopen_cstrs: 0xb4f
+  __TEXT.__gcc_except_tab: 0x20c4
+  __TEXT.__oslogstring: 0x726d
+  __TEXT.__cstring: 0x72be
+  __TEXT.__dlopen_cstrs: 0xb96
   __TEXT.__ustring: 0x1f4
-  __TEXT.__unwind_info: 0x4100
+  __TEXT.__unwind_info: 0x4148
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x28d8
+  __DATA_CONST.__const: 0x2918
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c48
+  __DATA_CONST.__objc_selrefs: 0x8cf0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x678
-  __DATA_CONST.__got: 0xfd0
+  __DATA_CONST.__got: 0xfe0
   __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0x5a20
-  __AUTH_CONST.__objc_const: 0x2a388
+  __AUTH_CONST.__cfstring: 0x5a80
+  __AUTH_CONST.__objc_const: 0x2a558
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x32f0
-  __AUTH.__data: 0x198
-  __DATA.__objc_ivar: 0x14a4
+  __AUTH.__data: 0x1a0
+  __DATA.__objc_ivar: 0x14b8
   __DATA.__data: 0x2bf0
   __DATA_DIRTY.__objc_data: 0xb40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5906
-  Symbols:   13917
-  CStrings:  1618
+  Functions: 5931
+  Symbols:   13980
+  CStrings:  1622
 
Symbols:
+ -[SFShareSheetSlotManager performShortcutActivityInHostWithBundleID:singleUseToken:sourceAppIsManaged:]
+ -[SHSheetContentLayoutSpec canAccommodateTopActionsRowForContentWidth:]
+ -[SHSheetInteractor collaborationOptionsDidChangeForSession:]
+ -[SHSheetServiceManager performShortcutActivityInHostWithBundleID:singleUseToken:sourceAppIsManaged:]
+ -[SHSheetSession isPublicCollaborationForActivities]
+ -[SHSheetSession setIsPublicCollaborationForActivities:]
+ -[UIActivityContentViewController _canShowTopActionsRow]
+ -[UIActivityContentViewController _updateAutoExpansionInteractionIfNeeded]
+ -[UIActivityContentViewController autoExpansionInteraction]
+ -[UIActivityContentViewController handleShouldAutoExpand:]
+ -[UIActivityContentViewController setAutoExpansionInteraction:]
+ -[UIActivityContentViewController setShouldAutoExpand:]
+ -[UIActivityContentViewController shouldAutoExpand]
+ -[UICopyToPasteboardActivity .cxx_destruct]
+ -[UICopyToPasteboardActivity _copyDataOwner]
+ -[UICopyToPasteboardActivity isContentManaged]
+ -[UICopyToPasteboardActivity setIsContentManaged:]
+ -[UICopyToPasteboardActivity setSourceApplicationBundleID:]
+ -[UICopyToPasteboardActivity sourceApplicationBundleID]
+ GCC_except_table102
+ GCC_except_table130
+ GCC_except_table84
+ _CloudKitLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_UTType
+ _OBJC_IVAR_$_SHSheetSession._isPublicCollaborationForActivities
+ _OBJC_IVAR_$_UIActivityContentViewController._autoExpansionInteraction
+ _OBJC_IVAR_$_UIActivityContentViewController._shouldAutoExpand
+ _OBJC_IVAR_$_UICopyToPasteboardActivity._isContentManaged
+ _OBJC_IVAR_$_UICopyToPasteboardActivity._sourceApplicationBundleID
+ _SFUIActivityViewControllerConfiguratorFunction
+ _UIFontWeightMedium
+ __OBJC_$_INSTANCE_VARIABLES_UICopyToPasteboardActivity
+ __OBJC_$_PROP_LIST_UICopyToPasteboardActivity
+ __OBJC_CLASS_PROTOCOLS_$_UICopyToPasteboardActivity
+ ___101-[SHSheetServiceManager performShortcutActivityInHostWithBundleID:singleUseToken:sourceAppIsManaged:]_block_invoke
+ ___55-[UICopyToPasteboardActivity prepareWithActivityItems:]_block_invoke_2
+ ___74-[UIActivityContentViewController _updateAutoExpansionInteractionIfNeeded]_block_invoke
+ ___CloudKitLibraryCore_block_invoke
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___getCKAllowedSharingOptionsClass_block_invoke
+ _audit_stringCloudKit
+ _classSFUIActivityViewControllerConfigurator
+ _getCKAllowedSharingOptionsClass.softClass
+ _getSFUIActivityViewControllerConfiguratorClass
+ _initSFUIActivityViewControllerConfigurator
+ _objc_msgSend$_canShowTopActionsRow
+ _objc_msgSend$_copyDataOwner
+ _objc_msgSend$_performAsDataOwner:block:
+ _objc_msgSend$_updateAutoExpansionInteractionIfNeeded
+ _objc_msgSend$addInteraction:
+ _objc_msgSend$autoExpansionInteraction
+ _objc_msgSend$autoExpansionInteractionForHandler:
+ _objc_msgSend$canAccommodateTopActionsRowForContentWidth:
+ _objc_msgSend$collaborationOptionsDidChangeForSession:
+ _objc_msgSend$handleShouldAutoExpand:
+ _objc_msgSend$isAnyoneWithLinkSharingAvailable
+ _objc_msgSend$isCollaborationItemPrivateShare:
+ _objc_msgSend$isDynamic
+ _objc_msgSend$isPublicCollaborationForActivities
+ _objc_msgSend$performShortcutActivityInHostWithBundleID:singleUseToken:sourceAppIsManaged:
+ _objc_msgSend$removeInteraction:
+ _objc_msgSend$requestForActivity:activityType:sourceAppIsManaged:
+ _objc_msgSend$setAutoExpansionInteraction:
+ _objc_msgSend$setIsPublicCollaborationForActivities:
+ _objc_msgSend$setShouldAutoExpand:
+ _objc_msgSend$setVibrantSubtitleView:
+ _objc_msgSend$shouldAutoExpand
+ _objc_msgSend$systemFontOfSize:weight:
+ _objc_msgSend$typeWithFilenameExtension:
+ _objc_msgSend$vibrantSubtitleView
- -[SFShareSheetSlotManager performShortcutActivityInHostWithBundleID:singleUseToken:]
- -[SHSheetServiceManager performShortcutActivityInHostWithBundleID:singleUseToken:]
- GCC_except_table113
- GCC_except_table123
- GCC_except_table126
- ___82-[SHSheetServiceManager performShortcutActivityInHostWithBundleID:singleUseToken:]_block_invoke
- _objc_msgSend$performShortcutActivityInHostWithBundleID:singleUseToken:
CStrings:
+ "CKAllowedSharingOptions"
+ "Not re-filtering activities for collaboration options change, session hasn't started."
+ "SHARE_LINK_ACCESS_REQUESTS_ALREADY_ON_MESSAGE_NO_PUBLIC_SHARING"
+ "SHARE_LINK_ACCESS_REQUESTS_OFF_MESSAGE_NO_PUBLIC_SHARING"
+ "SHARE_LINK_ACCESS_REQUESTS_UNSUPPORTED_MESSAGE_NO_PUBLIC_SHARING"
+ "softlink:r:path:/System/Library/Frameworks/CloudKit.framework/CloudKit"
- "TelephonyUtilities"
- "mochiEnabled"
```
