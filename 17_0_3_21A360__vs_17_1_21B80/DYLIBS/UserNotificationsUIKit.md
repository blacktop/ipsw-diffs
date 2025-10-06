## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-827.0.0.0.0
-  __TEXT.__text: 0xfb29c
+827.4.101.0.0
+  __TEXT.__text: 0xfb110
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0xce38
-  __TEXT.__const: 0x590
-  __TEXT.__gcc_except_tab: 0x2010
+  __TEXT.__objc_methlist: 0xce50
+  __TEXT.__const: 0x5a0
+  __TEXT.__gcc_except_tab: 0x202c
   __TEXT.__cstring: 0x711a
   __TEXT.__oslogstring: 0x7a18
   __TEXT.__ustring: 0x1e
   __TEXT.__objc_const_ax: 0x4ce8
-  __TEXT.__unwind_info: 0x4a70
+  __TEXT.__unwind_info: 0x4a68
   __TEXT.__objc_classname: 0x32ff
-  __TEXT.__objc_methname: 0x3b9db
-  __TEXT.__objc_methtype: 0xae77
-  __TEXT.__objc_stubs: 0x230e0
+  __TEXT.__objc_methname: 0x3ba25
+  __TEXT.__objc_methtype: 0xae87
+  __TEXT.__objc_stubs: 0x23100
   __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0x36d8
+  __DATA_CONST.__const: 0x3688
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3f5e8
-  __DATA_CONST.__objc_selrefs: 0xa278
+  __DATA_CONST.__objc_const: 0x3f608
+  __DATA_CONST.__objc_selrefs: 0xa288
   __DATA_CONST.__objc_arraydata: 0x158
   __AUTH_CONST.__cfstring: 0x65a0
   __AUTH_CONST.__const: 0xe20

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0xc98
   __DATA.__objc_superrefs: 0x4e0
-  __DATA.__objc_ivar: 0x12e0
+  __DATA.__objc_ivar: 0x12e4
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0x3b40
   __DATA.__bss: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E16A1449-1D22-319A-9157-37DC641FA8FB
-  Functions: 6868
-  Symbols:   24386
-  CStrings:  10920
+  UUID: 2CB209FE-F9CE-3649-AFBE-83DEC6E5B1CE
+  Functions: 6867
+  Symbols:   24384
+  CStrings:  10924
 
Symbols:
+ -[NCAvatarImageRenderer _queue_imageForContacts:compatibleWithTraitCollection:circular:]
+ -[NCFullScreenStagingBannerView _configureDetailScrollViewIfNecessary]
+ -[NCFullScreenStagingBannerView _detailLabelsNumberOfLines]
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table48
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table93
+ _OBJC_IVAR_$_NCFullScreenStagingBannerView._detailScrollView
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke.43
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_2.44
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_3.45
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_4.46
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_5.47
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_6.48
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_7.49
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_8.50
+ ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_9.51
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ _objc_msgSend$_configureDetailScrollViewIfNecessary
+ _objc_msgSend$_detailLabelsNumberOfLines
+ _objc_msgSend$_queue_imageForContacts:compatibleWithTraitCollection:circular:
+ _objc_msgSend$avatarImageForContacts:scope:
+ _objc_msgSend$offMainThreadSynchronousRenderingOnlySettingsWithCacheSize:
- -[NCAvatarImageRenderer _imageForContacts:compatibleWithTraitCollection:circular:completion:]
- GCC_except_table100
- GCC_except_table112
- GCC_except_table39
- GCC_except_table53
- GCC_except_table68
- GCC_except_table74
- GCC_except_table77
- GCC_except_table91
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke.42
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_2.43
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_3.44
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_4.45
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_5.46
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_6.47
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_7.48
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_8.49
- ___78-[NCFullScreenStagingBannerView _layoutForDetailStageWithSettings:completion:]_block_invoke_9.50
- ___89-[NCAvatarImageRenderer renderAvatarForRequest:compatibleWithTraitCollection:completion:]_block_invoke.14
- ___91-[NCBulletinNotificationSource observer:addBulletin:forFeed:playLightsAndSirens:withReply:]_block_invoke_2
- ___93-[NCAvatarImageRenderer _imageForContacts:compatibleWithTraitCollection:circular:completion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e17_v16?0"UIImage"8ls32l8
- ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e17_v16?0"UIImage"8lr64l8r72l8s32l8s40l8s48l8s56l8
- _objc_msgSend$_imageForContacts:compatibleWithTraitCollection:circular:completion:
- _objc_msgSend$defaultSettingsWithCacheSize:
- _objc_msgSend$dispatcher:requestsClearingNotificationRequests:
- _objc_msgSend$renderAvatarsForContacts:scope:imageHandler:
CStrings:
+ "\x0f\a"
+ "@\"UIScrollView\""
+ "_configureDetailScrollViewIfNecessary"
+ "_detailLabelsNumberOfLines"
+ "_detailScrollView"
+ "_queue_imageForContacts:compatibleWithTraitCollection:circular:"
+ "avatarImageForContacts:scope:"
+ "offMainThreadSynchronousRenderingOnlySettingsWithCacheSize:"
- "\x0f\x06"
- "_imageForContacts:compatibleWithTraitCollection:circular:completion:"
- "defaultSettingsWithCacheSize:"
- "renderAvatarsForContacts:scope:imageHandler:"

```
