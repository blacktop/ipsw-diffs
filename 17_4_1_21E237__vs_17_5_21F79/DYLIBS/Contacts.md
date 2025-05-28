## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3632.6.0.0.0
-  __TEXT.__text: 0x180724
+3632.8.0.0.0
+  __TEXT.__text: 0x181688
   __TEXT.__auth_stubs: 0x2eb0
-  __TEXT.__objc_methlist: 0x15b4c
+  __TEXT.__objc_methlist: 0x15b94
   __TEXT.__const: 0x11f0
-  __TEXT.__gcc_except_tab: 0x27fc
-  __TEXT.__cstring: 0xd4ca
-  __TEXT.__oslogstring: 0x67be
+  __TEXT.__gcc_except_tab: 0x2818
+  __TEXT.__cstring: 0xd56a
+  __TEXT.__oslogstring: 0x6ba1
   __TEXT.__dlopen_cstrs: 0x33e
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xcf4

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x344
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x7bdc
+  __TEXT.__unwind_info: 0x7974
   __TEXT.__eh_frame: 0x1d18
   __TEXT.__objc_classname: 0x3959
-  __TEXT.__objc_methname: 0x25561
+  __TEXT.__objc_methname: 0x25645
   __TEXT.__objc_methtype: 0x45f4
-  __TEXT.__objc_stubs: 0x1ad20
+  __TEXT.__objc_stubs: 0x1adc0
   __DATA_CONST.__got: 0xd70
   __DATA_CONST.__const: 0x5a20
   __DATA_CONST.__objc_classlist: 0xeb0

   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1c958
-  __DATA_CONST.__objc_selrefs: 0x82f0
+  __DATA_CONST.__objc_selrefs: 0x8318
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_classrefs: 0x1168
   __DATA_CONST.__objc_superrefs: 0x878
   __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__cfstring: 0xcb60
-  __AUTH_CONST.__const: 0x61e0
+  __AUTH_CONST.__cfstring: 0xcca0
+  __AUTH_CONST.__const: 0x6240
   __AUTH_CONST.__objc_const: 0xc100
-  __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__auth_ptr: 0x88
   __AUTH_CONST.__auth_got: 0x1768
-  __AUTH.__data: 0x5e8
-  __AUTH.__objc_data: 0x4c70
+  __AUTH.__data: 0x5f0
+  __AUTH.__objc_data: 0x4bd0
   __DATA.__objc_ivar: 0xfd0
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x2d50
-  __DATA.__bss: 0x1cb0
-  __DATA.__common: 0x50
-  __DATA_DIRTY.__objc_data: 0x5050
-  __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0xaa0
+  __DATA.__data: 0x2fd0
+  __DATA.__bss: 0x1a20
+  __DATA.__common: 0x38
+  __DATA_DIRTY.__objc_data: 0x50f0
+  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__bss: 0xae0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10820
-  Symbols:   31138
-  CStrings:  9690
+  Functions: 10831
+  Symbols:   31174
+  CStrings:  9712
 
Symbols:
+ +[CNContactImageUpdater descriptorForRequiredKeys]
+ +[CNContactImageUpdater updateMutableContact:withImageAndWallpaperPropertiesFromContact:]
+ +[CNContactImageUpdater updateMutableContact:withImagePropertiesFromContact:]
+ +[CNContactImageUpdater updateMutableContact:withWallpaperPropertiesFromContact:]
+ +[CNContactMatchSummarizer log]
+ +[CNSharedProfileStateOracle descriptionForActionType:]
+ +[CNSharedProfileStateOracle descriptionForUpdateState:]
+ -[CNContactMatchSummarizer summaryForContact:matchInfo:].cold.1
+ -[CNSharedProfileStateOracle didPendingNicknameChangePhotoOrWallpaper]
+ -[CNSharedProfileStateOracle didPhotoOrWallpaperChangeFrom:to:]
+ -[CNSharedProfileStateOracle targetProfileForActionType:].cold.2
+ ___31+[CNContactMatchSummarizer log]_block_invoke
+ ___55+[CNSharedProfileStateOracle descriptionForActionType:]_block_invoke
+ ___56+[CNSharedProfileStateOracle descriptionForUpdateState:]_block_invoke
+ _descriptionForActionType:.cn_once_object_62
+ _descriptionForActionType:.cn_once_token_62
+ _descriptionForUpdateState:.cn_once_object_63
+ _descriptionForUpdateState:.cn_once_token_63
+ _objc_msgSend$descriptionForActionType:
+ _objc_msgSend$descriptionForUpdateState:
+ _objc_msgSend$didPendingNicknameChangePhotoOrWallpaper
+ _objc_msgSend$didPhotoOrWallpaperChangeFrom:to:
+ _objc_msgSend$updateMutableContact:withImageAndWallpaperPropertiesFromContact:
+ _objc_msgSend$updateMutableContact:withImagePropertiesFromContact:
+ _objc_msgSend$updateMutableContact:withWallpaperPropertiesFromContact:
+ _summaryProperties.cn_once_object_2
+ _summaryProperties.cn_once_token_2
- -[CNContactImageUpdater updateContact:withImagePropertiesFromContact:]
- -[CNSharedProfileStateOracle didChangePhotoOrWallpaper]
- _objc_msgSend$didChangePhotoOrWallpaper
- _objc_msgSend$updateContact:withImagePropertiesFromContact:
- _summaryProperties.cn_once_object_1
- _summaryProperties.cn_once_token_1
CStrings:
+ "AlwaysAsk"
+ "Attempting to decline update for contact (%{public}@) and nicknames for actionType: %@"
+ "Attempting to update contact (%{public}@) and nicknames for actionType: %@"
+ "Attempting to update contact (%{public}@) and nicknames for auto-update"
+ "Cannot update an unsaved contact for actionType %@"
+ "Cannot update an unsaved contact for declined actionType %@"
+ "Contact (%{public}@) archived vs current: photoDiffers %d, wallpaperDiffers %d"
+ "Contact (%{public}@) archivedIsIgnored %d, archivedIsExpired %d"
+ "Contact (%{public}@) has a current nickname with no pending nickname ready, using currentNickname as target Latest Photo"
+ "Contact (%{public}@) has a pending nickname ready, using pendingNickname as target Latest Photo"
+ "Contact (%{public}@) has a recent avatar or poster, using recent as target Custom Photo"
+ "Contact (%{public}@) has an archived and current nickname containing the same photo and wallpaper, this will result in an action that shows no change"
+ "Contact (%{public}@) has an archived nickname, using archivedNickname as target Previous Photo"
+ "Contact (%{public}@) is in an undetermined update state, using the existing contact photo as target Custom Photo"
+ "Contact (%{public}@) using currentNickname as target Latest Photo"
+ "Defaulting to using current contact (%{public}@) photo as target photo for action type: %@ "
+ "Error updating contact for actionType %@"
+ "Error updating contact for declined actionType %@"
+ "ExplicitAutoUpdate"
+ "ImplicitAutoUpdate"
+ "Looking up banner action type for contact (%{public}@) with effective state: %@"
+ "Looking up banner action type: pendingIsIgnored %d for contact (%{public}@)"
+ "Looking up banner action type: pendingNickname is nil for contact (%{public}@)"
+ "Looking up banner action type: recentAvatarAvailableForRevert %d, recentPosterAvailableForRevert %d for contact (%{public}@)"
+ "No archived nickname found for contact (%{public}@), cannot show revert to previous banner"
+ "None"
+ "Pending nickname didPendingNicknameChangePhotoOrWallpaper: %d"
+ "Returning banner action type: %@ for contact (%{public}@)"
+ "Returning target shared profile %@ for action type %@"
+ "RevertToCustom"
+ "RevertToPrevious"
+ "Saved updated contact: %{public}@ for actionType %@"
+ "Saved updated contact: %{public}@ for declined actionType %@"
+ "Undetermined"
+ "UnknownAction"
+ "UnknownState"
+ "UpdateToLatest"
+ "Updated contact (%{public}@) and nicknames for actionType: %@"
+ "Updated contact (%{public}@) and nicknames for declined actionType: %@"
+ "contact %{public}@ does not have %{public}@ fetched, available keys %{public}@"
+ "contact %{public}@ does not have value for %{public}@"
+ "descriptionForActionType:"
+ "descriptionForUpdateState:"
+ "didPendingNicknameChangePhotoOrWallpaper"
+ "didPhotoOrWallpaperChangeFrom:to:"
+ "updateMutableContact:withImageAndWallpaperPropertiesFromContact:"
+ "updateMutableContact:withImagePropertiesFromContact:"
+ "updateMutableContact:withWallpaperPropertiesFromContact:"
- "Archived vs Current: photoDiffers %d, wallpaperDiffers %d"
- "Attempting to decline update for contact and nicknames for actionType: %lu"
- "Attempting to update contact and nicknames for actionType: %lu"
- "Attempting to update contact and nicknames for auto-update"
- "Cannot update an unsaved contact for actionType %lu"
- "Cannot update an unsaved contact for declined actionType %lu"
- "Error updating contact for actionType %lu"
- "Error updating contact for declined actionType %lu"
- "Looking up banner action type for effective state: %lu"
- "Looking up banner action type: pendingIsIgnored %d"
- "Looking up banner action type: pendingNickname is nil"
- "Looking up banner action type: recentAvatarAvailableForRevert %d, recentPosterAvailableForRevert %d"
- "No archived nickname found, cannot show revert to previous banner"
- "Pending nickname didChangePhotoOrWallpaper: %d"
- "Returning banner action type: %lu"
- "Returning target shared profile %@ for action type %lu"
- "Saved updated contact: %{public}@ for actionType %lu"
- "Saved updated contact: %{public}@ for declined actionType %lu"
- "Updated contact and nicknames for actionType: %lu"
- "Updated contact and nicknames for declined actionType: %lu"
- "archivedIsIgnored %d, archivedIsExpired %d"
- "didChangePhotoOrWallpaper"
- "targetProfileForActionType %lu, using archivedNickname"
- "targetProfileForActionType %lu, using contact recents"
- "targetProfileForActionType %lu, using current nickname"
- "targetProfileForActionType %lu, using pending nickname"
- "updateContact:withImagePropertiesFromContact:"

```
