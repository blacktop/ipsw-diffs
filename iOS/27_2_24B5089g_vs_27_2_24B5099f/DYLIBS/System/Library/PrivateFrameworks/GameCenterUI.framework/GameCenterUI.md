## GameCenterUI

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI`

```diff

-821.1.8.0.0
-  __TEXT.__text: 0x4a1654
-  __TEXT.__objc_methlist: 0x1d1f4
+821.1.16.0.0
+  __TEXT.__text: 0x4a1a0c
+  __TEXT.__objc_methlist: 0x1d224
   __TEXT.__const: 0x28f34
   __TEXT.__cstring: 0x17b7f
-  __TEXT.__gcc_except_tab: 0x1a3c
-  __TEXT.__oslogstring: 0x93c7
+  __TEXT.__gcc_except_tab: 0x1a4c
+  __TEXT.__oslogstring: 0x9537
   __TEXT.__ustring: 0x16
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__swift5_typeref: 0x29a0e

   __TEXT.__swift5_protos: 0xac
   __TEXT.__swift5_mpenum: 0xf0
   __TEXT.__swift_as_cont: 0x768
-  __TEXT.__unwind_info: 0x18070
-  __TEXT.__eh_frame: 0x9c6c
+  __TEXT.__unwind_info: 0x18090
+  __TEXT.__eh_frame: 0x9c94
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x518
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf58
+  __DATA_CONST.__objc_selrefs: 0xdf88
   __DATA_CONST.__objc_protorefs: 0x220
   __DATA_CONST.__objc_classrefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x408
-  __DATA_CONST.__got: 0x2e38
+  __DATA_CONST.__got: 0x2e30
   __AUTH_CONST.__const: 0x1f0a8
   __AUTH_CONST.__cfstring: 0xa000
-  __AUTH_CONST.__objc_const: 0x553a0
+  __AUTH_CONST.__objc_const: 0x553b0
   __AUTH_CONST.__objc_intobj: 0xb28
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0x120

   __AUTH.__objc_data: 0x153c0
   __AUTH.__data: 0xfce0
   __DATA.__objc_ivar: 0x1744
-  __DATA.__data: 0xfb70
+  __DATA.__data: 0xfb60
   __DATA.__objc_stublist: 0xc0
   __DATA.__common: 0x1600
   __DATA_DIRTY.__objc_data: 0x2d80
   __DATA_DIRTY.__data: 0x1468
-  __DATA_DIRTY.__bss: 0x7d0
+  __DATA_DIRTY.__bss: 0x7e0
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 33748
-  Symbols:   20304
-  CStrings:  3252
+  Functions: 33752
+  Symbols:   20307
+  CStrings:  3255
 
Symbols:
+ -[GKDashboardMultiplayerPickerViewController updateAddRecipientButtonVisibility:]
+ -[GKLeaderboardScoreDataSource hasMoreEntriesToLoad]
+ -[GKMatchmakerViewController _finishWithMatchAfterPlayerResolution]
+ -[GKMatchmakerViewController setWaitingForPlayerResolution:]
+ -[GKMatchmakerViewController waitingForPlayerResolution]
+ GCC_except_table100
+ GCC_except_table55
+ GCC_except_table75
+ GCC_except_table97
+ _OBJC_IVAR_$_GKMatchmakerViewController._waitingForPlayerResolution
+ ___45-[GKMatchmakerViewController finishWithMatch]_block_invoke
- -[GKDashboardMultiplayerPickerViewController setExcludesContacts:]
- GCC_except_table47
- GCC_except_table48
- GCC_except_table60
- GCC_except_table74
- GCC_except_table95
- GCC_except_table98
- _OBJC_IVAR_$_GKDashboardMultiplayerPickerViewController._excludesContacts
CStrings:
+ "Not forming contact from picked contact, since contacts are excluded. GKPreferences.shared.multiplayerAllowedPlayerType is set to: %@, pickerOrigin: %@"
+ "Not presenting contact picker, since contacts are excluded. GKPreferences.shared.multiplayerAllowedPlayerType is set to: %@, pickerOrigin: %@"
+ "finishWithMatch: still waiting for player resolution, ignoring repeat call"
```
