## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

```diff

-1573.2.4.0.0
-  __TEXT.__text: 0x1ee350
+1573.3.3.0.0
+  __TEXT.__text: 0x1ee554
   __TEXT.__objc_methlist: 0x204bc
   __TEXT.__const: 0x2e94
   __TEXT.__cstring: 0xce64

   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0xac
-  __TEXT.__unwind_info: 0x9908
+  __TEXT.__unwind_info: 0x9910
   __TEXT.__eh_frame: 0xbec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x660
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfce8
+  __DATA_CONST.__objc_selrefs: 0xfcf0
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x8c8
   __DATA_CONST.__objc_arraydata: 0x1c0
Symbols:
+ +[EKUIAvailabilityParticipantList listWidthForCompact:aspectRatioType:safeAreaInsets:]
- +[EKUIAvailabilityParticipantList listWidthForCompact:orientation:]
Functions:
~ -[EKEventProposeNewTimeViewController viewAvailabilityTapped] : 280 -> 316
~ -[EKUIEventInviteesViewController availabilityTapped] : 292 -> 320
~ -[EKEventEditViewControllerModernImpl requestInviteeAvailabilityPresentationWithEvent:] : 280 -> 308
~ +[EKUIAvailabilityParticipantList listWidthForCompact:orientation:] -> +[EKUIAvailabilityParticipantList listWidthForCompact:aspectRatioType:safeAreaInsets:] : 48 -> 108
~ +[EKUIAvailabilityViewController presentAvailabilityViewControllerForEvent:fromViewController:] : 176 -> 204
~ -[EKUIAvailabilityViewController sizeWillBeCompact:] : 252 -> 284
~ -[EKUIAvailabilityViewController loadView] : 5252 -> 5276
~ -[EKUIAvailabilityViewController layout] : 1316 -> 1424
~ -[EKUIAvailabilityViewController viewPinched:] : 592 -> 628
~ sub_1dcce8d18 -> sub_1dd42de94 : 112 -> 124
~ sub_1dccfe288 -> sub_1dd443410 : 108 -> 96
~ sub_1dccfeb84 -> sub_1dd443d00 : 432 -> 460
~ sub_1dcd2c644 -> sub_1dd4717dc : 300 -> 324
~ sub_1dcd2d3d8 -> sub_1dd472588 : 4748 -> 4832
```
