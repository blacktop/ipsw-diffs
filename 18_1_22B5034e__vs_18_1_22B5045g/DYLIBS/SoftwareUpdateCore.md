## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2082.40.21.0.0
-  __TEXT.__text: 0x9c4b8
+2082.40.34.0.0
+  __TEXT.__text: 0x9d438
   __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x700c
+  __TEXT.__objc_methlist: 0x7054
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x13a07
-  __TEXT.__oslogstring: 0xb354
+  __TEXT.__cstring: 0x13e9a
+  __TEXT.__oslogstring: 0xb35b
   __TEXT.__gcc_except_tab: 0x6d4
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x1698
+  __TEXT.__unwind_info: 0x16b0
   __TEXT.__objc_classname: 0x6fe
-  __TEXT.__objc_methname: 0x140af
+  __TEXT.__objc_methname: 0x142d1
   __TEXT.__objc_methtype: 0xf04
-  __TEXT.__objc_stubs: 0xdee0
+  __TEXT.__objc_stubs: 0xe000
   __DATA_CONST.__got: 0x870
-  __DATA_CONST.__const: 0x2118
+  __DATA_CONST.__const: 0x2150
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4008
+  __DATA_CONST.__objc_selrefs: 0x4068
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x11b40
-  __AUTH_CONST.__objc_const: 0xa760
+  __AUTH_CONST.__cfstring: 0x11f20
+  __AUTH_CONST.__objc_const: 0xa7f0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x908
+  __DATA.__objc_ivar: 0x914
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2875
-  Symbols:   3821
-  CStrings:  6204
+  Functions: 2891
+  Symbols:   3842
+  CStrings:  6253
 
Symbols:
+ _kSU_ID_presustaging
+ _SUCorePolicyDDMStatusNotificationNameBetaEnrollment
+ _kSU_M_removeAsset
+ _SUCorePolicyDDMStatusKeyBetaEnrollment
+ _kSU_ID_splat
CStrings:
+ "setShouldReportDownloadFailureIfCanceled:"
+ "_numPendingOperations"
+ "Created by _SUCoreBorder_stagePurgeAllAtEnd"
+ "splat"
+ "[SCAN] DETERMINE_PSUS_SUCCESS"
+ "actionDeterminePSUSAssetsSuccess:error:"
+ "RemoveCompleted"
+ "PSUSAssetsSizes"
+ "[PreSUStaging] No need to remove PSUS assets (disabled)"
+ "numberWithDouble:"
+ "Duration"
+ "Created by _SUCoreBorder_stageCancelAtEnd"
+ "Created by _SUCoreBorder_stageDetermineResultAtBegin"
+ "Should have no pending operations: UpdateFailedToDownload"
+ "%!{(MISSING)public}@ [PreSUStaging] succeeded; %!{(MISSING)public}@\n[>>>\nbyGroupAvailableForStagingAttributes = DICT[%!l(MISSING)u]\nbyGroupTotalExpectedBytes = %!{(MISSING)public}@\n<<<]"
+ "Created by _SUCoreBorder_stageDownloadAtBegin"
+ "numPendingOperations"
+ "BetaEnrollment"
+ "Created by _SUCoreBorder_stagePurgeAllAtBegin"
+ "\n[>>>\n       majorPrimaryDescriptor: %!@(MISSING)\n     majorSecondaryDescriptor: %!@(MISSING)\n       minorPrimaryDescriptor: %!@(MISSING)\n     minorSecondaryDescriptor: %!@(MISSING)\n               additionalInfo: %!@(MISSING)\n<<<]"
+ "softwareupdate.beta-enrollment"
+ "setNumPendingOperations:"
+ "TB,N,V_shouldReportDownloadFailureIfCanceled"
+ "Ti,N,V_numPendingOperations"
+ "presustaging"
+ "REMOVE"
+ "Should have no pending operations: UpdateRemoved"
+ "%!@(MISSING) unexpected no assets sizes"
+ "additionalInfo"
+ "actionRemoveUpdate:error:"
+ "com.apple.SoftwareUpdateSubscriber.updateStatus.betaEnrollment"
+ "_shouldReportDownloadFailureIfCanceled"
+ "\n[>>>\n                   descriptor: %!@(MISSING)\n           fallbackDescriptor: %!@(MISSING)\n               additionalInfo: %!@(MISSING)\n<<<]"
+ "[Splombo] No need to remove Splat (no Splat)"
+ "_reportUpdateFailedToDownload:"
+ "Should have no pending operations: UpdateFailedToRemove"
+ "\n[>>>\n          note: %!@(MISSING)\nadditionalInfo: %!@(MISSING)\n<<<]"
+ "%!@(MISSING)(%!@(MISSING))]"
+ "decremented the number of pending operations (%!d(MISSING)): %!@(MISSING) (%!@(MISSING)) has ended"
+ "shouldReportDownloadFailureIfCanceled"
+ "actionCheckRemoveCompleted:error:"
+ "Created by _SUCoreBorder_stageCancelAtBegin"
+ "T@\"NSMutableDictionary\",&,N,V_additionalInfo"
+ "[TRACK_END]"
+ "_trackBegin:withIdentifier:"
+ "invalid numPendingOperations (%!d(MISSING)) when %!@(MISSING) (%!@(MISSING)) ends"
+ "Created by _SUCoreBorder_stageDownloadAtEnd"
+ "CheckRemoveCompleted"
+ "incremented the number of pending operations (%!d(MISSING)): %!@(MISSING) (%!@(MISSING)) has begun"
+ "PSUSDetermineError"
+ "_trackEnd:withIdentifier:withResult:withError:"
+ "_verifyNoPendingOperations:reason:"
+ "_additionalInfo"
+ "1.0.2"
+ "%!@(MISSING)[%!@(MISSING)]"
+ "Should have no pending operations: UpdateDownloaded"
+ "_versionedModuleName"
+ "Created by _SUCoreBorder_stageDetermineResultAtEnd"
+ "setAdditionalInfo:"
+ "\n[>>>\n                   resultCode: %!l(MISSING)d\n                        error: %!@(MISSING)\n               additionalInfo: %!@(MISSING)\n<<<]"
+ "RemovingUpdate"
+ "UNK_LOC"
- "[UPDATE_DOWNLOADER(%!@(MISSING))]"
- "RemovePSUSAssets"
- "RemovingPSUSAssets"
- "actionRemoveSplat:error:"
- "[Splombo] No need to remove Splat, skip removing Splat"
- "actionDeterminePSUSAssetsSuccess:"
- "actionRemovePSUSAssets:error:"
- "%!{(MISSING)public}@ [PreSUStaging] succeeded; %!{(MISSING)public}@\n[>>>\nbyGroupAvailableForStagingAttributes = %!@(MISSING)\nbyGroupTotalExpectedBytes = %!{(MISSING)public}@\n<<<]"
- "\n[>>>\n       majorPrimaryDescriptor: %!@(MISSING)\n     majorSecondaryDescriptor: %!@(MISSING)\n       minorPrimaryDescriptor: %!@(MISSING)\n     minorSecondaryDescriptor: %!@(MISSING)\n<<<]"
- "\n[>>>\n        note: %!@(MISSING)\n<<<]"
- "RemovingSplat"
- "[PreSUStaging] disabled; skip removing assets"
- "\n[>>>\n                   descriptor: %!@(MISSING)\n           fallbackDescriptor: %!@(MISSING)\n<<<]"
- "RemoveSplat"
- "\n[>>>\n                   resultCode: %!l(MISSING)d\n                        error: %!@(MISSING)\n<<<]"

```
