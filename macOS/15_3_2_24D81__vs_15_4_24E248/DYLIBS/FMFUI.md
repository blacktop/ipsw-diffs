## FMFUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/FMFUI.framework/Versions/A/FMFUI`

```diff

-508.23.10.29.2
-  __TEXT.__text: 0xe5e0
+508.24.7.11.12
+  __TEXT.__text: 0xe59c
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x11d4
+  __TEXT.__objc_methlist: 0x171c
   __TEXT.__const: 0x100
   __TEXT.__cstring: 0x4e1
   __TEXT.__oslogstring: 0x9e3
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x438
+  __TEXT.__unwind_info: 0x440
   __TEXT.__objc_classname: 0x250
   __TEXT.__objc_methname: 0x4a8a
   __TEXT.__objc_methtype: 0xcd2

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12e8
+  __DATA_CONST.__objc_selrefs: 0x14e0
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x620
-  __AUTH_CONST.__objc_const: 0x2a40
+  __AUTH_CONST.__objc_const: 0x2040
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x130

   - /System/iOSSupport/System/Library/PrivateFrameworks/FMCoreUI.framework/Versions/A/FMCoreUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D92B9CC-FBC2-3673-BA7A-06F8490F4F27
-  Functions: 405
-  Symbols:   1361
+  UUID: D9C394C4-E31F-3B83-AF9A-82660A2AE9F5
+  Functions: 409
+  Symbols:   1366
   CStrings:  1151
 
Symbols:
+ +[FMFMapImageCache sharedInstance].cold.1
+ +[FMFMonogramUtility contactImageCache].cold.1
+ +[FMFMonogramUtility contactStatusCache].cold.1
+ LogCategory_Daemon.cold.1
+ LogCategory_FMFMapXPC.cold.1
Functions:
~ +[FMFMapImageCache sharedInstance] : 84 -> 68
~ +[FMFNoNetworkAlert alertInfoForInternetUnavailableReason:] : 692 -> 684
- sub_267de4668
~ +[FMFMonogramUtility contactImageCache] : 84 -> 68
~ +[FMFMonogramUtility contactStatusCache] : 84 -> 68
~ +[FMFMonogramUtility clearMonogramCache] : 72 -> 68
~ +[FMFMonogramUtility monogrammerWithDiameter:style:useTintColor:customFont:] : 352 -> 360
~ +[FMFMonogramUtility hexStringFromColor:] : 408 -> 404
~ -[FMFMapViewController updateNoLocationView:] : 948 -> 952
~ -[FMFMapViewController _setUserTrackingMode:animated:fromTrackingButton:] : 248 -> 200
~ -[FMFMapViewController _updateTitleViewLocation:] : 400 -> 384
~ -[FMFMapViewDelegateInternal initWithDelegate:mapView:] : 464 -> 456
~ -[FMFMapViewDelegateInternal slideAnnotation:intoViewIfNeededForMapView:] : 272 -> 276
~ _LogCategory_Daemon : 84 -> 68
~ _LogCategory_FMFMapXPC : 84 -> 68
+ +[FMFMapImageCache sharedInstance].cold.1

```
