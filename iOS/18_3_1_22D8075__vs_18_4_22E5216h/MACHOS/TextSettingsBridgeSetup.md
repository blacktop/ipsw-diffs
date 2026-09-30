## TextSettingsBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/TextSettingsBridgeSetup.bundle/TextSettingsBridgeSetup`

```diff

-965.5.4.0.0
-  __TEXT.__text: 0x3ae0
-  __TEXT.__auth_stubs: 0x330
+965.7.3.0.0
+  __TEXT.__text: 0x3e24
+  __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0x408
+  __TEXT.__objc_methlist: 0x988
   __TEXT.__objc_classname: 0x16c
   __TEXT.__cstring: 0x1f0
-  __TEXT.__const: 0xb0
+  __TEXT.__const: 0xb8
   __TEXT.__objc_methname: 0x22d1
+  __TEXT.__oslogstring: 0x295
   __TEXT.__objc_methtype: 0xc9c
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x1a8
+  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__auth_got: 0x1c8
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x188
   __DATA_CONST.__cfstring: 0x2a0

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1658
-  __DATA.__objc_selrefs: 0x600
+  __DATA.__objc_const: 0xbf0
+  __DATA.__objc_selrefs: 0x910
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 105
-  Symbols:   499
-  CStrings:  485
+  Functions: 107
+  Symbols:   505
+  CStrings:  496
 
Symbols:
+ -[TextSettingsViewController updateWatchScreenImageViewAndNotifyObserver:].cold.1
+ _AXLogCommon
+ __57-[TextSettingsMiniFlowController didReceiveIncomingData:]_block_invoke.cold.1
+ __os_log_error_impl
+ __os_log_impl
+ _os_log_type_enabled
CStrings:
+ "[TextSettingsMiniFlowController] already received snapshots, do not hold"
+ "[TextSettingsMiniFlowController] continue to hold"
+ "[TextSettingsMiniFlowController] data payload is invalid"
+ "[TextSettingsMiniFlowController] did receive incoming data"
+ "[TextSettingsMiniFlowController] do not skip for express mode"
+ "[TextSettingsMiniFlowController] publishing sendSnapshots request"
+ "[TextSettingsMiniFlowController] releasing hold on controller"
+ "[TextSettingsMiniFlowController] skip for express mode"
+ "[TextSettingsViewController] cached image is nil for size category: %@, bold text: %@"
+ "[TextSettingsViewController] view did load"
+ "[TextSettingsViewController] view is not loaded"

```
