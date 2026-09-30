## MobileMailUI

> `/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI`

```diff

-3856.100.4.0.0
-  __TEXT.__text: 0x4909c
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x4c7c
-  __TEXT.__gcc_except_tab: 0x900c
-  __TEXT.__cstring: 0x363c
+3858.100.10.2.1
+  __TEXT.__text: 0x4d9f0
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x510c
+  __TEXT.__gcc_except_tab: 0x99d8
+  __TEXT.__cstring: 0x377c
   __TEXT.__ustring: 0x318
   __TEXT.__const: 0x81b4
-  __TEXT.__oslogstring: 0x1e57
+  __TEXT.__oslogstring: 0x1e77
   __TEXT.__dlopen_cstrs: 0x97
   __TEXT.__swift5_typeref: 0x2a2
-  __TEXT.__swift5_capture: 0x110
+  __TEXT.__swift5_capture: 0x128
   __TEXT.__swift5_fieldmd: 0x80
   __TEXT.__constg_swiftt: 0x1c4
   __TEXT.__swift5_reflstr: 0x3a

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x25f0
+  __TEXT.__unwind_info: 0x28b8
   __TEXT.__eh_frame: 0x1b0
-  __TEXT.__objc_classname: 0xb0f
-  __TEXT.__objc_methname: 0x112d8
-  __TEXT.__objc_methtype: 0x44ae
-  __TEXT.__objc_stubs: 0xb780
-  __DATA_CONST.__got: 0xa88
-  __DATA_CONST.__const: 0x12b8
-  __DATA_CONST.__objc_classlist: 0x1d8
-  __DATA_CONST.__objc_catlist: 0x20
+  __TEXT.__objc_classname: 0xb90
+  __TEXT.__objc_methname: 0x11df3
+  __TEXT.__objc_methtype: 0x454e
+  __TEXT.__objc_stubs: 0xbfc0
+  __DATA_CONST.__got: 0xb00
+  __DATA_CONST.__const: 0x12f0
+  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e78
+  __DATA_CONST.__objc_selrefs: 0x4158
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__const: 0x6c8
-  __AUTH_CONST.__cfstring: 0x2da0
-  __AUTH_CONST.__objc_const: 0x7780
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x888
+  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__cfstring: 0x2ec0
+  __AUTH_CONST.__objc_const: 0x7da0
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x8d0
+  __AUTH.__objc_data: 0xa10
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x468
+  __DATA.__objc_ivar: 0x4b0
   __DATA.__data: 0x1168
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x50
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0xb38
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6B3AF37A-9023-34DD-9AF8-6574318E3D8A
-  Functions: 1627
-  Symbols:   6714
-  CStrings:  4111
+  UUID: 77B3F2CA-6605-3CE6-99FE-8C4C099F29C6
+  Functions: 1725
+  Symbols:   7092
+  CStrings:  4270
 
Symbols:
+ +[MFMailboxUid(Utilities) iconForType:]
+ +[MFMailboxUid(Utilities) iconNameForType:]
+ +[MFMailboxUid(Utilities) shorcutIconNameForMailboxType:]
+ +[MFMessageSashHeaderBlock heightForCurrentFontMetrics]
+ +[MFMessageSashHeaderBlock titleFont]
+ +[MailAccount(Utilities) accountImageForAccount:]
+ -[MFMailboxUid(MobileMailEditing) mv_isEditable]
+ -[MFMailboxUid(MobileMailEditing) mv_isSelectable]
+ -[MFMailboxUid(Utilities) foundInDescriptionIncludingAccount:]
+ -[MFMailboxUid(Utilities) iconName]
+ -[MFMailboxUid(Utilities) icon]
+ -[MFMailboxUid(Utilities) level]
+ -[MFMailboxUid(Utilities) tinyDisplayIconWithColor:]
+ -[MFMessageSashHeaderBlock .cxx_destruct]
+ -[MFMessageSashHeaderBlock _fontMetricCacheDidInvalidate:]
+ -[MFMessageSashHeaderBlock _updateFonts]
+ -[MFMessageSashHeaderBlock _updateMailboxIcon]
+ -[MFMessageSashHeaderBlock accountsProvider]
+ -[MFMessageSashHeaderBlock backgroundView]
+ -[MFMessageSashHeaderBlock contentSizeCategoryDidChangeNotification:]
+ -[MFMessageSashHeaderBlock createPrimaryViews]
+ -[MFMessageSashHeaderBlock displayMessageUsingViewModel:]
+ -[MFMessageSashHeaderBlock iconImageView]
+ -[MFMessageSashHeaderBlock iconVerticalConstraint]
+ -[MFMessageSashHeaderBlock initWithCoder:]
+ -[MFMessageSashHeaderBlock initWithFrame:]
+ -[MFMessageSashHeaderBlock initWithFrame:accountsProvider:]
+ -[MFMessageSashHeaderBlock initializePrimaryLayoutConstraints]
+ -[MFMessageSashHeaderBlock setAccountsProvider:]
+ -[MFMessageSashHeaderBlock setBackgroundView:]
+ -[MFMessageSashHeaderBlock setDisplayMetrics:]
+ -[MFMessageSashHeaderBlock setIconImageView:]
+ -[MFMessageSashHeaderBlock setIconVerticalConstraint:]
+ -[MFMessageSashHeaderBlock setSeparatorDrawsFlushWithLeadingEdge:]
+ -[MFMessageSashHeaderBlock setSeparatorDrawsFlushWithTrailingEdge:]
+ -[MFMessageSashHeaderBlock setShouldShowMailbox:]
+ -[MFMessageSashHeaderBlock setTitleLabel:]
+ -[MFMessageSashHeaderBlock setTitleLabelBottom:]
+ -[MFMessageSashHeaderBlock setTitleLabelTop:]
+ -[MFMessageSashHeaderBlock shouldShowMailbox]
+ -[MFMessageSashHeaderBlock titleLabelBottom]
+ -[MFMessageSashHeaderBlock titleLabelTop]
+ -[MFMessageSashHeaderBlock titleLabel]
+ -[MFMessageSashHeaderBlock updateConstraints]
+ -[MailAccount(MailboxSorting) _addGenericChildrenToMailboxTree:forNode:hideNotes:]
+ -[MailAccount(MailboxSorting) _addSpecialMailbox:toTree:]
+ -[MailAccount(MailboxSorting) _allMailboxesIncludingLocals:withOutbox:hideInbox:hideNotes:]
+ -[MailAccount(MailboxSorting) _putMailboxesRootedAt:intoArray:hideNotes:]
+ -[MailAccount(MailboxSorting) _treeOfAllMailboxesIncludingLocals:withOutbox:hideInbox:hideNotes:]
+ -[MailAccount(MailboxSorting) addSpecialMailbox:toArray:]
+ -[MailAccount(MailboxSorting) allMailboxUidsSortedWithSpecialsAtTopIncludingLocals:]
+ -[MailAccount(MailboxSorting) treeOfAllGenericMailboxes]
+ -[MailAccount(MailboxSorting) treeOfAllMailboxUidsSortedWithSpecialsAtTopIncludingLocals:client:outbox:]
+ -[MailboxHierarchyNode .cxx_destruct]
+ -[MailboxHierarchyNode _findNodeForMailbox:removeNode:]
+ -[MailboxHierarchyNode addChild:]
+ -[MailboxHierarchyNode children]
+ -[MailboxHierarchyNode description]
+ -[MailboxHierarchyNode displayName]
+ -[MailboxHierarchyNode findNodeForMailbox:]
+ -[MailboxHierarchyNode initWithMailbox:]
+ -[MailboxHierarchyNode level]
+ -[MailboxHierarchyNode mailbox]
+ -[MailboxHierarchyNode parentMailbox]
+ -[MailboxHierarchyNode removeNodeForMailbox:]
+ -[MailboxHierarchyNode setDisplayName:]
+ -[MailboxHierarchyNode setLevel:]
+ -[MailboxHierarchyNode setParentMailbox:]
+ -[MailboxHierarchyTree .cxx_destruct]
+ -[MailboxHierarchyTree _addChildNode:toParentNode:]
+ -[MailboxHierarchyTree _insertMailboxUidsFlattenedFromMailboxNode:intoArray:currentLevel:]
+ -[MailboxHierarchyTree addChildMailbox:forMailboxNode:]
+ -[MailboxHierarchyTree displayNameForMailbox:]
+ -[MailboxHierarchyTree flattenedMailboxTreeRepresentation]
+ -[MailboxHierarchyTree initWithRootMailbox:]
+ -[MailboxHierarchyTree levelForMailbox:]
+ -[MailboxHierarchyTree mailboxHasSubMailboxes:]
+ -[MailboxHierarchyTree moveMailbox:toParent:]
+ -[MailboxHierarchyTree parentForMailbox:]
+ -[MailboxHierarchyTree removeNodeForMailbox:]
+ -[MailboxHierarchyTree rootMailboxNode]
+ -[MailboxHierarchyTree setDisplayName:forMailbox:]
+ -[_MFIconCacheItem .cxx_destruct]
+ -[_MFIconCacheItem cachedImage]
+ -[_MFIconCacheItem filename]
+ -[_MFIconCacheItem initWithFilename:]
+ -[_MFIconCacheItem setCachedImage:]
+ OBJC_IVAR_$_MailboxHierarchyNode._children
+ OBJC_IVAR_$_MailboxHierarchyNode._displayName
+ OBJC_IVAR_$_MailboxHierarchyNode._level
+ OBJC_IVAR_$_MailboxHierarchyNode._mailbox
+ OBJC_IVAR_$_MailboxHierarchyNode._parentMailbox
+ OBJC_IVAR_$_MailboxHierarchyTree._mailboxStructureHasBeenCached
+ OBJC_IVAR_$_MailboxHierarchyTree._nodesByMailbox
+ OBJC_IVAR_$_MailboxHierarchyTree._rootMailboxNode
+ _MFImageGlyphArchiveMailbox
+ _MFImageGlyphDraftMailbox
+ _MFImageGlyphGenericMailbox
+ _MFImageGlyphInboxMailbox
+ _MFImageGlyphJunkMailbox
+ _MFImageGlyphOutboxMailbox
+ _MFImageGlyphSentMailbox
+ _MFImageGlyphSentMailboxFilled
+ _MFImageGlyphTrashMailbox
+ _MSAccessibilityIdentifierMailConversationViewSashHeader
+ _OBJC_CLASS_$_LocalAccount
+ _OBJC_CLASS_$_MFMailboxUid
+ _OBJC_CLASS_$_MFMessageSashHeaderBlock
+ _OBJC_CLASS_$_MailboxHierarchyNode
+ _OBJC_CLASS_$_MailboxHierarchyTree
+ _OBJC_CLASS_$__MFIconCacheItem
+ _OBJC_IVAR_$_MFMessageSashHeaderBlock._accountsProvider
+ _OBJC_IVAR_$_MFMessageSashHeaderBlock._backgroundView
+ _OBJC_IVAR_$_MFMessageSashHeaderBlock._iconImageView
+ _OBJC_IVAR_$_MFMessageSashHeaderBlock._iconVerticalConstraint
+ _OBJC_IVAR_$_MFMessageSashHeaderBlock._shouldShowMailbox
+ _OBJC_IVAR_$_MFMessageSashHeaderBlock._titleLabel
+ _OBJC_IVAR_$_MFMessageSashHeaderBlock._titleLabelBottom
+ _OBJC_IVAR_$_MFMessageSashHeaderBlock._titleLabelTop
+ _OBJC_IVAR_$__MFIconCacheItem._cachedImage
+ _OBJC_IVAR_$__MFIconCacheItem._filename
+ _OBJC_METACLASS_$_MFMessageSashHeaderBlock
+ _OBJC_METACLASS_$_MailboxHierarchyNode
+ _OBJC_METACLASS_$_MailboxHierarchyTree
+ _OBJC_METACLASS_$__MFIconCacheItem
+ __CompareMailboxHierarchyNodes
+ __OBJC_$_CATEGORY_CLASS_METHODS_MFMailboxUid_$_Utilities
+ __OBJC_$_CATEGORY_CLASS_METHODS_MailAccount_$_Utilities
+ __OBJC_$_CATEGORY_MFMailboxUid_$_Utilities
+ __OBJC_$_CATEGORY_MailAccount_$_Utilities
+ __OBJC_$_CLASS_METHODS_MFMessageSashHeaderBlock
+ __OBJC_$_CLASS_PROP_LIST_MFMessageSashHeaderBlock
+ __OBJC_$_INSTANCE_METHODS_MFMailboxUid(Utilities|MobileMailEditing)
+ __OBJC_$_INSTANCE_METHODS_MFMessageSashHeaderBlock
+ __OBJC_$_INSTANCE_METHODS_MailAccount(Utilities|MailboxSorting)
+ __OBJC_$_INSTANCE_METHODS_MailboxHierarchyNode
+ __OBJC_$_INSTANCE_METHODS_MailboxHierarchyTree
+ __OBJC_$_INSTANCE_METHODS__MFIconCacheItem
+ __OBJC_$_INSTANCE_VARIABLES_MFMessageSashHeaderBlock
+ __OBJC_$_INSTANCE_VARIABLES_MailboxHierarchyNode
+ __OBJC_$_INSTANCE_VARIABLES_MailboxHierarchyTree
+ __OBJC_$_INSTANCE_VARIABLES__MFIconCacheItem
+ __OBJC_$_PROP_LIST_MFMessageSashHeaderBlock
+ __OBJC_$_PROP_LIST_MailboxHierarchyNode
+ __OBJC_$_PROP_LIST__MFIconCacheItem
+ __OBJC_CLASS_RO_$_MFMessageSashHeaderBlock
+ __OBJC_CLASS_RO_$_MailboxHierarchyNode
+ __OBJC_CLASS_RO_$_MailboxHierarchyTree
+ __OBJC_CLASS_RO_$__MFIconCacheItem
+ __OBJC_METACLASS_RO_$_MFMessageSashHeaderBlock
+ __OBJC_METACLASS_RO_$_MailboxHierarchyNode
+ __OBJC_METACLASS_RO_$_MailboxHierarchyTree
+ __OBJC_METACLASS_RO_$__MFIconCacheItem
+ ___37+[MFMessageSashHeaderBlock titleFont]_block_invoke
+ ___40-[MFMessageHeaderView _updateSeparators]_block_invoke_3
+ ___45-[MFMessageSashHeaderBlock updateConstraints]_block_invoke
+ ___45-[MFMessageSashHeaderBlock updateConstraints]_block_invoke_2
+ ___55+[MFMessageSashHeaderBlock heightForCurrentFontMetrics]_block_invoke
+ ___55+[MFMessageSashHeaderBlock heightForCurrentFontMetrics]_block_invoke_2
+ ___block_descriptor_40_e5_d8?0l
+ ___block_descriptor_40_ea8_32s_e13_"UIFont"8?0ls32l8
+ ___block_literal_global.1565
+ __folderNameFormatString
+ _accountImageForAccount:.__accountIcons
+ _accountImageForAccount:.bundle
+ _iconNameForType:.mailboxImages
+ _objc_msgSend$_addChildNode:toParentNode:
+ _objc_msgSend$_addGenericChildrenToMailboxTree:forNode:hideNotes:
+ _objc_msgSend$_addSpecialMailbox:toTree:
+ _objc_msgSend$_allMailboxesIncludingLocals:withOutbox:hideInbox:hideNotes:
+ _objc_msgSend$_applicationIconImageForFormat:precomposed:
+ _objc_msgSend$_findNodeForMailbox:removeNode:
+ _objc_msgSend$_flatImageWithColor:
+ _objc_msgSend$_insertMailboxUidsFlattenedFromMailboxNode:intoArray:currentLevel:
+ _objc_msgSend$_preferredFontDescriptorWithTextStyle:weight:
+ _objc_msgSend$_putMailboxesRootedAt:intoArray:hideNotes:
+ _objc_msgSend$_treeOfAllMailboxesIncludingLocals:withOutbox:hideInbox:hideNotes:
+ _objc_msgSend$_updateFonts
+ _objc_msgSend$_updateMailboxIcon
+ _objc_msgSend$accountsProvider
+ _objc_msgSend$addChild:
+ _objc_msgSend$addChildMailbox:forMailboxNode:
+ _objc_msgSend$addSpecialMailbox:toArray:
+ _objc_msgSend$capHeight
+ _objc_msgSend$childEnumerator
+ _objc_msgSend$children
+ _objc_msgSend$displayNameUsingSpecialNames
+ _objc_msgSend$ef_insertObject:usingSortFunction:context:allowDuplicates:
+ _objc_msgSend$font
+ _objc_msgSend$foundInDescriptionIncludingAccount:
+ _objc_msgSend$hasChildren
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$iconForType:
+ _objc_msgSend$iconImageView
+ _objc_msgSend$iconNameForType:
+ _objc_msgSend$iconString
+ _objc_msgSend$iconVerticalConstraint
+ _objc_msgSend$imageNamed:inBundle:compatibleWithTraitCollection:
+ _objc_msgSend$initWithMailbox:
+ _objc_msgSend$initWithRootMailbox:
+ _objc_msgSend$isDisplayingMultipleAccounts
+ _objc_msgSend$isStore
+ _objc_msgSend$isSyncingNotes
+ _objc_msgSend$level
+ _objc_msgSend$localAccount
+ _objc_msgSend$mailboxType
+ _objc_msgSend$mailboxUidOfType:createIfNeeded:
+ _objc_msgSend$moveMailbox:toParent:
+ _objc_msgSend$nextObject
+ _objc_msgSend$parent
+ _objc_msgSend$parentMailbox
+ _objc_msgSend$primaryMailboxUid
+ _objc_msgSend$removeNodeForMailbox:
+ _objc_msgSend$rootMailbox
+ _objc_msgSend$rootMailboxNode
+ _objc_msgSend$setAdjustsFontForContentSizeCategory:
+ _objc_msgSend$setAllowsGroupBlending:
+ _objc_msgSend$setIconImageView:
+ _objc_msgSend$setIconVerticalConstraint:
+ _objc_msgSend$setLevel:
+ _objc_msgSend$setParentMailbox:
+ _objc_msgSend$setTitleLabel:
+ _objc_msgSend$setTitleLabelBottom:
+ _objc_msgSend$setTitleLabelTop:
+ _objc_msgSend$shouldHideInbox
+ _objc_msgSend$shouldHideNotesForAccount:
+ _objc_msgSend$shouldShowMailbox
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$text
+ _objc_msgSend$tinyDisplayIconWithColor:
+ _objc_msgSend$titleLabelBottom
+ _objc_msgSend$titleLabelTop
+ _objc_setProperty_atomic
+ _shorcutIconNameForMailboxType:._mailboxAppShortcutIconNames
- _MailSceneSessionInfoActiveDraftIdentifier
- _MailSceneSessionInfoActiveDraftOriginalMessageIdentifier
- ___block_literal_global.1563
CStrings:
+ "%@, %@"
+ "-[MFMessageSashHeaderBlock initWithCoder:]"
+ "-[MFMessageSashHeaderBlock initWithFrame:]"
+ "<%{public}@> client:%{public}@"
+ "@\"<MFAccountsProvider>\""
+ "@\"MailboxHierarchyNode\""
+ "@\"UIImage\""
+ "@\"UIImageView\""
+ "@24@0:8q16"
+ "@36@0:8B16@20@28"
+ "@36@0:8B16@20B28B32"
+ "BOX_SUFFIX"
+ "FOLDER_SUFFIX"
+ "FOUND_IN_MAILBOX_FORMAT"
+ "MAILBOX_SUFFIX"
+ "MFMessageSashHeaderBlock"
+ "MFMessageSashHeaderBlock.m"
+ "MailboxHierarchyNode"
+ "MailboxHierarchyTree"
+ "MailboxSorting"
+ "MobileMailEditing"
+ "Notes"
+ "T@\"<MFAccountsProvider>\",&,N,V_accountsProvider"
+ "T@\"MFMailboxUid\",&,V_parentMailbox"
+ "T@\"NSLayoutConstraint\",&,N,V_iconVerticalConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_titleLabelBottom"
+ "T@\"NSLayoutConstraint\",&,N,V_titleLabelTop"
+ "T@\"NSString\",&,V_displayName"
+ "T@\"NSString\",R,C,N,V_filename"
+ "T@\"UIImage\",&,N,V_cachedImage"
+ "T@\"UIImageView\",&,N,V_iconImageView"
+ "T@\"UILabel\",&,N,V_titleLabel"
+ "T@\"UIView\",&,N,V_backgroundView"
+ "TB,N,V_shouldShowMailbox"
+ "Utilities"
+ "_Concurrency/arm64e-apple-ios.private.swiftinterface"
+ "_MFIconCacheItem"
+ "_SHORT"
+ "_WITH_ACCOUNT"
+ "_accountsProvider"
+ "_addChildNode:toParentNode:"
+ "_addGenericChildrenToMailboxTree:forNode:hideNotes:"
+ "_addSpecialMailbox:toTree:"
+ "_allMailboxesIncludingLocals:withOutbox:hideInbox:hideNotes:"
+ "_applicationIconImageForFormat:precomposed:"
+ "_cachedImage"
+ "_filename"
+ "_findNodeForMailbox:removeNode:"
+ "_flatImageWithColor:"
+ "_iconImageView"
+ "_iconVerticalConstraint"
+ "_insertMailboxUidsFlattenedFromMailboxNode:intoArray:currentLevel:"
+ "_level"
+ "_mailboxStructureHasBeenCached"
+ "_nodesByMailbox"
+ "_parentMailbox"
+ "_preferredFontDescriptorWithTextStyle:weight:"
+ "_putMailboxesRootedAt:intoArray:hideNotes:"
+ "_rootMailboxNode"
+ "_shouldShowMailbox"
+ "_titleLabel"
+ "_titleLabelBottom"
+ "_titleLabelTop"
+ "_treeOfAllMailboxesIncludingLocals:withOutbox:hideInbox:hideNotes:"
+ "_updateFonts"
+ "_updateMailboxIcon"
+ "_webViewDidEnterStandbyForTesting:"
+ "_webViewDidExitStandbyForTesting:"
+ "accountImageForAccount:"
+ "accountsProvider"
+ "addChild:"
+ "addChildMailbox:forMailboxNode:"
+ "addSpecialMailbox:toArray:"
+ "allMailboxUidsSortedWithSpecialsAtTopIncludingLocals:"
+ "cachedImage"
+ "capHeight"
+ "childEnumerator"
+ "displayNameForMailbox:"
+ "displayNameUsingSpecialNames"
+ "ef_insertObject:usingSortFunction:context:allowDuplicates:"
+ "filename"
+ "findNodeForMailbox:"
+ "flattenedMailboxTreeRepresentation"
+ "font"
+ "foundInDescriptionIncludingAccount:"
+ "hasChildren"
+ "hasSuffix:"
+ "heightForCurrentFontMetrics"
+ "i"
+ "i16@0:8"
+ "icon"
+ "iconForType:"
+ "iconImageView"
+ "iconName"
+ "iconNameForType:"
+ "iconString"
+ "iconVerticalConstraint"
+ "imageNamed:inBundle:compatibleWithTraitCollection:"
+ "initWithCoder:"
+ "initWithFilename:"
+ "initWithFrame:accountsProvider:"
+ "initWithMailbox:"
+ "initWithRootMailbox:"
+ "isDisplayingMultipleAccounts"
+ "isStore"
+ "isSyncingNotes"
+ "level"
+ "levelForMailbox:"
+ "localAccount"
+ "mailboxHasSubMailboxes:"
+ "mailboxType"
+ "mailboxUidOfType:createIfNeeded:"
+ "messageSashHeaderBlock.titleFont"
+ "messageSashHeaderBlock.titleLabel.bottom"
+ "messageSashHeaderBlock.titleLabel.top"
+ "moveMailbox:toParent:"
+ "mv_isEditable"
+ "mv_isSelectable"
+ "nextObject"
+ "parent"
+ "parentForMailbox:"
+ "parentMailbox"
+ "primaryMailboxUid"
+ "removeNodeForMailbox:"
+ "rootMailbox"
+ "rootMailboxNode"
+ "setAccountsProvider:"
+ "setAdjustsFontForContentSizeCategory:"
+ "setAllowsGroupBlending:"
+ "setCachedImage:"
+ "setDisplayName:forMailbox:"
+ "setIconImageView:"
+ "setIconVerticalConstraint:"
+ "setLevel:"
+ "setParentMailbox:"
+ "setShouldShowMailbox:"
+ "setTitleLabel:"
+ "setTitleLabelBottom:"
+ "setTitleLabelTop:"
+ "shorcutIconNameForMailboxType:"
+ "shouldHideInbox"
+ "shouldHideNotesForAccount:"
+ "shouldShowMailbox"
+ "stringWithString:"
+ "text"
+ "tinyDisplayIconWithColor:"
+ "titleLabelBottom"
+ "titleLabelTop"
+ "treeOfAllGenericMailboxes"
+ "treeOfAllMailboxUidsSortedWithSpecialsAtTopIncludingLocals:client:outbox:"
+ "v20@0:8i16"
+ "v36@0:8@16@24i32"
- "ActiveDraftIdentifier"
- "ActiveDraftOriginalMessageIdentifier"

```
