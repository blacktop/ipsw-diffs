## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-634.1.13.0.0
-  __TEXT.__text: 0xf02cc
+634.1.14.0.0
+  __TEXT.__text: 0xf02b8
   __TEXT.__auth_stubs: 0x2db0
   __TEXT.__objc_methlist: 0x12110
   __TEXT.__const: 0x36d4
-  __TEXT.__cstring: 0x4697
+  __TEXT.__cstring: 0x4757
   __TEXT.__oslogstring: 0x272f
   __TEXT.__gcc_except_tab: 0xa34
   __TEXT.__ustring: 0x9c

   __TEXT.__objc_methname: 0x2a3ab
   __TEXT.__objc_methtype: 0x7729
   __TEXT.__objc_stubs: 0x20540
-  __DATA_CONST.__got: 0x2490
+  __DATA_CONST.__got: 0x2468
   __DATA_CONST.__const: 0x27f0
   __DATA_CONST.__objc_classlist: 0xac8
   __DATA_CONST.__objc_catlist: 0x408

   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x16e8
   __AUTH_CONST.__const: 0x28d8
-  __AUTH_CONST.__cfstring: 0x31c0
+  __AUTH_CONST.__cfstring: 0x3260
   __AUTH_CONST.__objc_const: 0x1ddc8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SportsKit.framework/SportsKit
   - /System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices
+  - /System/Library/PrivateFrameworks/SpotlightUIServices.framework/SpotlightUIServices
   - /System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/StatusKit.framework/StatusKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88089C8F-A4A4-3C80-A5FF-6D3F71837376
+  UUID: 09F60655-1A33-30D4-A429-0FF21CB8E3D2
   Functions: 6821
-  Symbols:   21087
-  CStrings:  9136
+  Symbols:   21082
+  CStrings:  9146
 
Symbols:
+ _OBJC_CLASS_$_SPUISRecentResultsManager
+ _OBJC_CLASS_$_SPUISResultBuilder
+ _OBJC_CLASS_$_SPUISTopHitAppWithEntitiesSectionBuilder
- _OBJC_CLASS_$_SSRecentResultsManager
- _OBJC_CLASS_$_SSResultBuilder
- _OBJC_CLASS_$_SSTopHitAppWithEntitiesSectionBuilder
- _PRSRankingLocalFilesBundleString
- _SSResultBundleIdDocument
- _SSResultBundleIdFileProviderDocument
- _SSResultBundleIdFileProviderManagedDocument
- _SSShortcutsBundleIdentifier
Functions:
~ -[SearchUIShortcutsAppTopHitAsyncSectionLoader buildSearchQueryForBundleIdentifier:] : 752 -> 732
CStrings:
+ "com.apple.CloudDocs.MobileDocumentsFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
+ "com.apple.FileProvider.LocalStorage"
+ "com.apple.shortcuts"

```
