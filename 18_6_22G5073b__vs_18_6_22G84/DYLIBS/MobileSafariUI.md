## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-621.3.8.0.0
-  __TEXT.__text: 0x1d58e4
+621.3.11.10.3
+  __TEXT.__text: 0x1d5f98
   __TEXT.__auth_stubs: 0x1e40
-  __TEXT.__objc_methlist: 0x2003c
-  __TEXT.__const: 0x71a
+  __TEXT.__objc_methlist: 0x20044
+  __TEXT.__const: 0x72a
   __TEXT.__gcc_except_tab: 0x1a944
   __TEXT.__cstring: 0xc64b
   __TEXT.__dlopen_cstrs: 0x774
-  __TEXT.__oslogstring: 0x8cfe
+  __TEXT.__oslogstring: 0x8ece
   __TEXT.__ustring: 0x10f6
   __TEXT.__constg_swiftt: 0x128
   __TEXT.__swift5_typeref: 0x1d1

   __TEXT.__swift5_capture: 0x98
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0xbd80
+  __TEXT.__unwind_info: 0xbd90
   __TEXT.__eh_frame: 0x2d8
   __TEXT.__objc_classname: 0x3dd9
-  __TEXT.__objc_methname: 0x65ca3
+  __TEXT.__objc_methname: 0x65cfd
   __TEXT.__objc_methtype: 0x1453b
-  __TEXT.__objc_stubs: 0x438a0
-  __DATA_CONST.__got: 0x26c0
+  __TEXT.__objc_stubs: 0x438e0
+  __DATA_CONST.__got: 0x26d0
   __DATA_CONST.__const: 0x8110
   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x988
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15498
+  __DATA_CONST.__objc_selrefs: 0x154a8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x690
   __DATA_CONST.__objc_arraydata: 0x270

   __AUTH_CONST.__const: 0x2d18
   __AUTH_CONST.__cfstring: 0xb9e0
   __AUTH_CONST.__objc_const: 0x2cba8
-  __AUTH_CONST.__objc_intobj: 0x468
+  __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x70

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1E7309DC-087C-3624-913D-E399D74A6E1F
-  Functions: 11056
-  Symbols:   41648
-  CStrings:  20554
+  UUID: 7F35C506-B212-33C7-9BC1-AED6FCD8266C
+  Functions: 11061
+  Symbols:   41662
+  CStrings:  20563
 
Symbols:
+ -[CloudTabStore _forceFetchAllCloudTabDevicesWithCompletion:]
+ _WBSDateOfLastForcedFetchOfCloudTabsKey
+ _WBSDebugForceFetchCloudTabsOnceKey
+ ___61-[CloudTabStore _forceFetchAllCloudTabDevicesWithCompletion:]_block_invoke
+ ___61-[CloudTabStore _forceFetchAllCloudTabDevicesWithCompletion:]_block_invoke_2
+ ___61-[CloudTabStore _forceFetchAllCloudTabDevicesWithCompletion:]_block_invoke_3
+ ___70-[CloudTabStore _saveCurrentDeviceCloudTabsNow:syncCompletionHandler:]_block_invoke
+ ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.49
+ ___block_literal_global.59
+ _objc_msgSend$_forceFetchAllCloudTabDevicesWithCompletion:
+ _objc_msgSend$clearServerChangeTokenWithCompletionHandler:
- ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.48
CStrings:
+ "Force fetch complete with data available: %{public}d, current device is registered in CloudKit: %{public}d"
+ "Force fetching all cloud tabs"
+ "No devices saved, %{public}lu tabs to sync up, CK device registration state: %{public}d"
+ "No previous device or cloud tabs to sync up, CK device registration state: %{public}d"
+ "Skipping force fetch since attempted recently"
+ "Skipping force fetch since cloud tabs disabled"
+ "Synced cloud tab devices count when saving: %{public}lu"
+ "_forceFetchAllCloudTabDevicesWithCompletion:"
+ "clearServerChangeTokenWithCompletionHandler:"

```
