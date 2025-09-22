## NotesSupport

> `/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport`

```diff

-2952.2.1.0.0
-  __TEXT.__text: 0x4cff0
-  __TEXT.__auth_stubs: 0x1bd0
-  __TEXT.__objc_methlist: 0x3cec
+2952.40.7.0.0
+  __TEXT.__text: 0x4c6d8
+  __TEXT.__auth_stubs: 0x1bc0
+  __TEXT.__delay_helper: 0x27c
+  __TEXT.__objc_methlist: 0x3d1c
   __TEXT.__const: 0x836
-  __TEXT.__cstring: 0x3f99
-  __TEXT.__oslogstring: 0x3805
-  __TEXT.__gcc_except_tab: 0x1014
-  __TEXT.__dlopen_cstrs: 0x19d
+  __TEXT.__cstring: 0x4022
+  __TEXT.__oslogstring: 0x3895
+  __TEXT.__gcc_except_tab: 0xfa4
+  __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__ustring: 0x18
   __TEXT.__constg_swiftt: 0x1bc
   __TEXT.__swift5_typeref: 0x188

   __TEXT.__swift5_capture: 0xd4
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x1a70
+  __TEXT.__unwind_info: 0x1a30
   __TEXT.__eh_frame: 0x6c8
   __TEXT.__objc_classname: 0x533
-  __TEXT.__objc_methname: 0xadd7
+  __TEXT.__objc_methname: 0xaebb
   __TEXT.__objc_methtype: 0x10c1
-  __TEXT.__objc_stubs: 0x7e80
-  __DATA_CONST.__got: 0x790
-  __DATA_CONST.__const: 0x12d8
+  __TEXT.__objc_stubs: 0x7f40
+  __DATA_CONST.__got: 0x7b8
+  __DATA_CONST.__const: 0x1280
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e30
+  __DATA_CONST.__objc_selrefs: 0x2e58
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0xe00
+  __AUTH_CONST.__auth_got: 0xdf8
   __AUTH_CONST.__const: 0xf98
-  __AUTH_CONST.__cfstring: 0x4180
-  __AUTH_CONST.__objc_const: 0x5728
+  __AUTH_CONST.__cfstring: 0x41a0
+  __AUTH_CONST.__objc_const: 0x5758
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x108
   __AUTH.__data: 0x210
-  __DATA.__objc_ivar: 0x1f8
-  __DATA.__data: 0x528
-  __DATA.__bss: 0x590
+  __DATA.__objc_ivar: 0x1fc
+  __DATA.__data: 0x534
+  __DATA.__bss: 0x560
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1158
   __DATA_DIRTY.__data: 0x148
-  __DATA_DIRTY.__bss: 0x390
+  __DATA_DIRTY.__bss: 0x370
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
+  - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/Speech.framework/Speech

   - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/Synapse.framework/Synapse
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D88A77B5-B19D-3227-97FB-1D967BCF687C
-  Functions: 2253
-  Symbols:   6781
-  CStrings:  3532
+  UUID: 79078A57-9635-3202-A04F-DA1EBE5BB34F
+  Functions: 2242
+  Symbols:   6765
+  CStrings:  3540
 
Symbols:
+ -[ICSearchIndexer dealloc]
+ -[ICSearchIndexer isActivelyReindexing]
+ -[ICSearchIndexer processReindexRequest:]
+ -[ICSearchIndexer setActivelyReindexing:]
+ GCC_except_table107
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table96
+ GCC_except_table97
+ _ICReindexRequestedNotification
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_PHPhotoLibrary
+ _OBJC_CLASS_$_SYItemIndexingManager
+ _OBJC_CLASS_$_UMUserManager
+ _OBJC_CLASS_$_UMUserPersonaAttributes
+ _OBJC_IVAR_$_ICSearchIndexer._activelyReindexing
+ ___33-[ICSearchIndexer processChanges]_block_invoke.25
+ ___41-[ICSearchIndexer processReindexRequest:]_block_invoke
+ ___41-[ICSearchIndexer processReindexRequest:]_block_invoke.cold.1
+ ___65-[ICSearchIndexer cancelIndexingOperationsWithCompletionHandler:]_block_invoke.32
+ ___65-[ICSearchIndexer cancelIndexingOperationsWithCompletionHandler:]_block_invoke.32.cold.1
+ ___66-[ICSearchIndexer finishRemainingOperationsWithCompletionHandler:]_block_invoke.33
+ ___66-[ICSearchIndexer finishRemainingOperationsWithCompletionHandler:]_block_invoke.33.cold.1
+ ___66-[ICSearchIndexer finishRemainingOperationsWithCompletionHandler:]_block_invoke.37
+ ___70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke.56
+ ___70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke.57
+ ___70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke.57.cold.1
+ ___84-[ICSearchIndexer reindexSearchableItemsWithObjectIDURIs:inIndex:completionHandler:]_block_invoke.61
+ ___84-[ICSearchIndexer reindexSearchableItemsWithObjectIDURIs:inIndex:completionHandler:]_block_invoke.61.cold.1
+ ___block_literal_global.36
+ ___block_literal_global.37
+ ___block_literal_global.39
+ ___block_literal_global.50
+ ___block_literal_global.57
+ ___block_literal_global.63
+ ___block_literal_global.68
+ _dlopenHelper$Photos
+ _dlopenHelper$Synapse
+ _dlopenHelper$UserManagement
+ _dlopenHelperFlag$Photos
+ _dlopenHelperFlag$Synapse
+ _dlopenHelperFlag$UserManagement
+ _gotLoadHelper_x8$_OBJC_CLASS_$_PHPhotoLibrary
+ _gotLoadHelper_x8$_OBJC_CLASS_$_SYItemIndexingManager
+ _gotLoadHelper_x8$_OBJC_CLASS_$_UMUserManager
+ _gotLoadHelper_x8$_OBJC_CLASS_$_UMUserPersonaAttributes
+ _objc_msgSend$addObserver:selector:name:object:suspensionBehavior:
+ _objc_msgSend$isActivelyReindexing
+ _objc_msgSend$isRunningInApp
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$reindexAllSearchableItemsWithCompletionHandler:
+ _objc_msgSend$setActivelyReindexing:
- GCC_except_table101
- GCC_except_table27
- GCC_except_table39
- GCC_except_table44
- GCC_except_table45
- GCC_except_table49
- GCC_except_table51
- GCC_except_table90
- GCC_except_table91
- _PhotosLibraryCore.frameworkLibrary
- _SynapseLibraryCore.frameworkLibrary
- _UserManagementLibrary
- _UserManagementLibraryCore.frameworkLibrary
- ___33-[ICSearchIndexer processChanges]_block_invoke.16
- ___65-[ICSearchIndexer cancelIndexingOperationsWithCompletionHandler:]_block_invoke.21
- ___65-[ICSearchIndexer cancelIndexingOperationsWithCompletionHandler:]_block_invoke.21.cold.1
- ___66-[ICSearchIndexer finishRemainingOperationsWithCompletionHandler:]_block_invoke.22
- ___66-[ICSearchIndexer finishRemainingOperationsWithCompletionHandler:]_block_invoke.22.cold.1
- ___66-[ICSearchIndexer finishRemainingOperationsWithCompletionHandler:]_block_invoke.26
- ___70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke.46
- ___70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke.47
- ___70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke.47.cold.1
- ___84-[ICSearchIndexer reindexSearchableItemsWithObjectIDURIs:inIndex:completionHandler:]_block_invoke.51
- ___84-[ICSearchIndexer reindexSearchableItemsWithObjectIDURIs:inIndex:completionHandler:]_block_invoke.51.cold.1
- ___PhotosLibraryCore_block_invoke
- ___SynapseLibraryCore_block_invoke
- ___UserManagementLibraryCore_block_invoke
- ___block_literal_global.35
- ___block_literal_global.55
- ___block_literal_global.66
- ___getPHPhotoLibraryClass_block_invoke
- ___getPHPhotoLibraryClass_block_invoke.cold.1
- ___getSYItemIndexingManagerClass_block_invoke
- ___getSYItemIndexingManagerClass_block_invoke.cold.1
- ___getUMUserManagerClass_block_invoke
- ___getUMUserManagerClass_block_invoke.cold.1
- ___getUMUserPersonaAttributesClass_block_invoke
- ___getUMUserPersonaAttributesClass_block_invoke.cold.1
- _audit_stringPhotos
- _audit_stringSynapse
- _audit_stringUserManagement
- _getPHPhotoLibraryClass
- _getPHPhotoLibraryClass.softClass
- _getSYItemIndexingManagerClass.softClass
- _getUMUserManagerClass.softClass
- _getUMUserPersonaAttributesClass.softClass
- _objc_retain_x9
CStrings:
+ "/System/Library/Frameworks/Photos.framework/Photos"
+ "/System/Library/PrivateFrameworks/Synapse.framework/Synapse"
+ "/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement"
+ "ICReindexRequestedNotification"
+ "Successfully reindexed all items. Resetting state."
+ "TB,N,GisActivelyReindexing,V_activelyReindexing"
+ "Unable to successfully reindex all items, keeping state for try next time. error: %@"
+ "_activelyReindexing"
+ "activelyReindexing"
+ "addObserver:selector:name:object:suspensionBehavior:"
+ "isActivelyReindexing"
+ "localizedDescription"
+ "processReindexRequest:"
+ "setActivelyReindexing:"
- "PHPhotoLibrary"
- "SYItemIndexingManager"
- "UMUserManager"
- "UMUserPersonaAttributes"
- "softlink:r:path:/System/Library/Frameworks/Photos.framework/Photos"
- "softlink:r:path:/System/Library/PrivateFrameworks/Synapse.framework/Synapse"
- "softlink:r:path:/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement"

```
