## SpotlightUIShared

> `/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared`

```diff

-250.1.4.1.0
-  __TEXT.__text: 0xd88ac
-  __TEXT.__objc_methlist: 0xf00
+250.1.9.0.0
+  __TEXT.__text: 0xd9ba8
+  __TEXT.__objc_methlist: 0xfd8
   __TEXT.__const: 0xa55c
-  __TEXT.__cstring: 0x3468
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__oslogstring: 0x13e2
+  __TEXT.__cstring: 0x34f8
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__oslogstring: 0x1602
   __TEXT.__ustring: 0x7de
   __TEXT.__swift5_typeref: 0x3476
   __TEXT.__swift5_reflstr: 0x1ce8

   __TEXT.__swift5_capture: 0x718
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0x4f20
-  __TEXT.__eh_frame: 0x934c
+  __TEXT.__unwind_info: 0x4f80
+  __TEXT.__eh_frame: 0x937c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x690
+  __DATA_CONST.__const: 0x6b8
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1620
+  __DATA_CONST.__objc_selrefs: 0x1710
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x1018
+  __DATA_CONST.__got: 0x1098
   __AUTH_CONST.__const: 0x6f91
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x3ab8
+  __AUTH_CONST.__cfstring: 0x8e0
+  __AUTH_CONST.__objc_const: 0x3ae8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1d38
+  __AUTH_CONST.__auth_got: 0x1d68
   __AUTH.__objc_data: 0x1580
   __AUTH.__data: 0x36e8
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x1c80
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x190

   - /System/Library/Frameworks/LinkPresentation.framework/LinkPresentation
   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5263
-  Symbols:   2278
-  CStrings:  438
+  Functions: 5292
+  Symbols:   2324
+  CStrings:  452
 
Symbols:
+ +[SUISPasteboardExtractor createIdentifierKey]
+ +[SUISPasteboardExtractor finalizeUniqueIdentifierForAttributeSet:]
+ +[SUISPasteboardExtractor hashStringFromData:]
+ +[SUISPasteboardExtractor hashStringFromRawHash:]
+ +[SUISPasteboardExtractor hashStringFromString:key:]
+ +[SUISPasteboardExtractor identifierKeyQuery]
+ +[SUISPasteboardExtractor identifierKey]
+ +[SUISPasteboardExtractor loadIdentifierKey]
+ +[SUISPasteboardExtractor readIdentifierKeyWithStatus:]
+ +[SUISPasteboardManager carryOverHistoryAttributesTo:from:]
+ +[SUISPasteboardManager indexActionForAttributeSet:generationCount:lastIndexedAttributeSet:lastIndexedGeneration:hasNewlyCachedFiles:]
+ +[SUISPasteboardManager pasteboardIndexingQueue]
+ -[SUISPasteboardManager clearPasteboardHistoryIfWipeRequested]
+ -[SUISPasteboardManager deleteCachedFiles:]
+ -[SUISPasteboardManager deleteStalePasteboardItem:]
+ -[SUISPasteboardManager forgetLastIndexedAttributeSet:]
+ -[SUISPasteboardManager historyItemCopiedGeneration]
+ -[SUISPasteboardManager indexCoreSpotlightItemWithAttributeSet:replacing:newlyCachedFiles:]
+ -[SUISPasteboardManager indexOrUpdateIfExistsCorespotlightItemAttributeSet:generationCount:newlyCachedFiles:]
+ -[SUISPasteboardManager lastIndexedAttributeSet]
+ -[SUISPasteboardManager lastIndexedGeneration]
+ -[SUISPasteboardManager setHistoryItemCopiedGeneration:]
+ -[SUISPasteboardManager setLastIndexedAttributeSet:]
+ -[SUISPasteboardManager setLastIndexedGeneration:]
+ GCC_except_table4
+ _CCHmac
+ _CC_SHA256
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_IVAR_$_SUISPasteboardManager._historyItemCopiedGeneration
+ _OBJC_IVAR_$_SUISPasteboardManager._lastIndexedAttributeSet
+ _OBJC_IVAR_$_SUISPasteboardManager._lastIndexedGeneration
+ _OUTLINED_FUNCTION_1
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecRandomCopyBytes
+ __OBJC_$_CLASS_METHODS_SUISPasteboardExtractor
+ ___109-[SUISPasteboardManager indexOrUpdateIfExistsCorespotlightItemAttributeSet:generationCount:newlyCachedFiles:]_block_invoke
+ ___48+[SUISPasteboardManager pasteboardIndexingQueue]_block_invoke
+ ___55-[SUISPasteboardManager forgetLastIndexedAttributeSet:]_block_invoke
+ ___91-[SUISPasteboardManager indexCoreSpotlightItemWithAttributeSet:replacing:newlyCachedFiles:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
+ _kSecAttrAccount
+ _kSecAttrService
+ _kSecAttrSynchronizable
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecRandomDefault
+ _kSecReturnData
+ _kSecUseDataProtectionKeychain
+ _kSecValueData
+ _objc_retain_x4
+ _pasteboardIndexingQueue.onceToken
+ _pasteboardIndexingQueue.queue
+ _sIdentifierKey
- +[SUISPasteboardManager pasteboardExpirationManagerQueue]
- -[SUISPasteboardManager changeCount]
- -[SUISPasteboardManager indexCoreSpotlightItemWithAttributeSet:]
- -[SUISPasteboardManager indexOrUpdateIfExistsCorespotlightItemAttributeSet:]
- -[SUISPasteboardManager pasteboardHistoryItemWasCopied]
- -[SUISPasteboardManager setChangeCount:]
- -[SUISPasteboardManager setPasteboardHistoryItemWasCopied:]
- _OBJC_IVAR_$_SUISPasteboardManager._changeCount
- _OBJC_IVAR_$_SUISPasteboardManager._pasteboardHistoryItemWasCopied
- ___57+[SUISPasteboardManager pasteboardExpirationManagerQueue]_block_invoke
- ___64-[SUISPasteboardManager indexCoreSpotlightItemWithAttributeSet:]_block_invoke
- ___76-[SUISPasteboardManager indexOrUpdateIfExistsCorespotlightItemAttributeSet:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8ls32l8s40l8s48l8
- _pasteboardExpirationManagerQueue.onceToken
- _pasteboardExpirationManagerQueue.queue
CStrings:
+ "%02x"
+ "already indexed this content for generation count %ld, skipping hash:%@"
+ "better extraction for generation count %ld, replacing hash:%@ with hash:%@"
+ "cached attachment for generation count %ld was gone, re-indexing hash:%@"
+ "com.apple.Spotlight.pasteboardHistory"
+ "com.apple.spotlight.delete.pasteboard.unindexed"
+ "com.apple.spotlight.pasteboardIndexingQueue"
+ "com.apple.spotlight.replace.pasteboard.superseded"
+ "deleting stale pasteboard item hash:%@ files:%lu"
+ "failed to generate pasteboard identifier key"
+ "failed to read pasteboard identifier key: %d"
+ "failed to store pasteboard identifier key: %d"
+ "generated a new pasteboard identifier key"
+ "identifierKey"
+ "no identifier key available, not indexing this pasteboard item"
+ "not indexing pasteboard item, identifier length:%lu lastUsedDate:%@"
+ "pasteboard identifier key already exists, re-reading"
+ "wiping pasteboard history for the new identifier scheme"
- "com.apple.spotlight.pasteboardExpirationManagerQueue"
- "identifier for CSSItem has no length"
- "updating changeCount from:%ld to %ld"
- "we're missing the lastuseddate when indexing. Skip indexing."
```
