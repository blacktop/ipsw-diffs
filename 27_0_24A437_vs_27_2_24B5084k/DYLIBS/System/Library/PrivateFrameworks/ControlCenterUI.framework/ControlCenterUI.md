## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-704.0.2.0.0
-  __TEXT.__text: 0xb6ae0
-  __TEXT.__objc_methlist: 0xb538
-  __TEXT.__const: 0x2c3a
+704.2.2.0.0
+  __TEXT.__text: 0xb6bbc
+  __TEXT.__objc_methlist: 0xb560
+  __TEXT.__const: 0x2c7a
   __TEXT.__cstring: 0x4824
   __TEXT.__gcc_except_tab: 0x82c
-  __TEXT.__oslogstring: 0x445b
+  __TEXT.__oslogstring: 0x446b
   __TEXT.__dlopen_cstrs: 0x14e
   __TEXT.__constg_swiftt: 0x2a7c
-  __TEXT.__swift5_typeref: 0x2c40
+  __TEXT.__swift5_typeref: 0x2c2e
   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_reflstr: 0x1e02
   __TEXT.__swift5_fieldmd: 0x138c
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_proto: 0xcc
   __TEXT.__swift5_types: 0x12c
-  __TEXT.__swift5_capture: 0xf88
+  __TEXT.__swift5_capture: 0xfc8
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x38b0
+  __TEXT.__unwind_info: 0x38c0
   __TEXT.__eh_frame: 0x3e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x5b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6948
+  __DATA_CONST.__objc_selrefs: 0x6958
   __DATA_CONST.__objc_protorefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0xd30
-  __AUTH_CONST.__const: 0x4471
+  __DATA_CONST.__got: 0xd40
+  __AUTH_CONST.__const: 0x4511
   __AUTH_CONST.__cfstring: 0x2f80
-  __AUTH_CONST.__objc_const: 0x111d0
+  __AUTH_CONST.__objc_const: 0x111e0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x1368
+  __AUTH_CONST.__auth_got: 0x1358
   __AUTH.__objc_data: 0x17d0
   __AUTH.__data: 0x6f0
   __DATA.__objc_ivar: 0x744

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5048
-  Symbols:   7808
+  Functions: 5057
+  Symbols:   7810
   CStrings:  852
 
Symbols:
+ -[CCUICellularDataModuleViewController _rebuildContentMenuActions]
+ -[CCUISensorAttributionCompactControl updateContentIfDisplayedAttributionsAreStale]
+ ___113-[CCUICellularDataModuleViewController profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:]_block_invoke
+ _objc_msgSend$_controlCenterApplyPrimaryContentShadowWithOpacityScale:
+ _objc_msgSend$_rebuildContentMenuActions
+ _objc_msgSend$updateContentIfDisplayedAttributionsAreStale
- _objc_msgSend$_controlCenterApplyPrimaryContentShadow
- _objc_msgSend$setShadowOpacity:
- _objc_msgSend$shadowOpacity
- _symbolic So11NSHashTableC
CStrings:
+ "[Cellular Data Module] Cellular Data state updated to %{public}@ [ capable: %d enabled: %d airplaneMode: %d multipleSubscriptionsAvailable: %d showsMenu: %d subtitle: %{private}@ ]"
- "[Cellular Data Module] Cellular Data state updated to %{public}@ [ capable: %d enabled: %d airplaneMode: %d multipleSubscriptionsAvailable: %d subtitle: %{private}@ ]"
```
