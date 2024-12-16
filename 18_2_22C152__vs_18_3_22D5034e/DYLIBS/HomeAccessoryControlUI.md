## HomeAccessoryControlUI

> `/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI`

```diff

-989.3.7.0.0
-  __TEXT.__text: 0x314f84
-  __TEXT.__auth_stubs: 0x52c0
+989.4.10.0.0
+  __TEXT.__text: 0x31891c
+  __TEXT.__auth_stubs: 0x5360
   __TEXT.__objc_methlist: 0x238
-  __TEXT.__const: 0xdd00
-  __TEXT.__cstring: 0x2d5e
-  __TEXT.__constg_swiftt: 0x4fec
-  __TEXT.__swift5_typeref: 0x24834
+  __TEXT.__const: 0xde40
+  __TEXT.__cstring: 0x2dee
+  __TEXT.__constg_swiftt: 0x5084
+  __TEXT.__swift5_typeref: 0x24a50
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x32d3
-  __TEXT.__swift5_fieldmd: 0x4288
+  __TEXT.__swift5_reflstr: 0x3323
+  __TEXT.__swift5_fieldmd: 0x42b8
   __TEXT.__swift5_assocty: 0x1438
-  __TEXT.__swift5_capture: 0x1340
+  __TEXT.__swift5_capture: 0x137c
   __TEXT.__swift5_proto: 0x7a0
   __TEXT.__swift5_types: 0x530
-  __TEXT.__oslogstring: 0x1697
+  __TEXT.__oslogstring: 0x17e7
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__unwind_info: 0x62b0
-  __TEXT.__eh_frame: 0x3920
+  __TEXT.__unwind_info: 0x62f0
+  __TEXT.__eh_frame: 0x3990
   __TEXT.__objc_classname: 0x7c
   __TEXT.__objc_methname: 0x1277
   __TEXT.__objc_methtype: 0x39c
   __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x1398
+  __DATA_CONST.__got: 0x13b0
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_selrefs: 0x5d0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2970
-  __AUTH_CONST.__auth_ptr: 0x1f68
-  __AUTH_CONST.__const: 0x8870
+  __AUTH_CONST.__auth_got: 0x29c0
+  __AUTH_CONST.__auth_ptr: 0x1fb8
+  __AUTH_CONST.__const: 0x8910
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x17f8
+  __AUTH_CONST.__objc_const: 0x1858
   __AUTH.__objc_data: 0x3d0
-  __AUTH.__data: 0x5100
+  __AUTH.__data: 0x51b0
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x7660
-  __DATA.__bss: 0xf298
+  __DATA.__data: 0x76d0
+  __DATA.__bss: 0xf2c8
   __DATA.__common: 0x218
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9046
+  Functions: 9093
   Symbols:   428
-  CStrings:  705
+  CStrings:  712
 
CStrings:
+ "%s Failed to find a DeviceTypeSolver for device type (%{public}s). Source: %s"
+ "Changing RVC cleaning mode to: %{public}s, current mode: %{public}s"
+ "Changing RVC secondary cleaning mode to: %{public}s, current mode: %{public}s"
+ "HFRVCHeaderGettingReady"
+ "HFRVCRoomSelectionFooter"
+ "HFSelectionViewCancel"
+ "Incorrect value found for selection state of type: %{public}s selection state: %{public}s"
+ "Incorrect values found for selection state of type: %{public}s selection state: %{public}s"
+ "Pause cleaning was pressed, pausing RVC. Current operational state: %{public}s. Current run mode: %{public}s"
+ "Robot vacuum does not support changing selected areas while running; supportsChangingSelectedAreasWhileRunning: %{public}s"
+ "Robot vacuum does not support skipping areas; supportsSkipAreaCommand: %{public}s"
+ "Start cleaning was pressed, current operational state: %{public}s, starting RVC."
+ "Start cleaning was pressed, resuming RVC. Current operational state: %{public}s. Current run mode: %{public}s"
+ "Start/Pause button was pressed, but current state is unsupported. Operational State: (%{public}s) Running Mode: (%{public}s)"
+ "Trying to set Pickker state got an unexpected control type: %{public}s"
+ "User attempted to start cleaning, but current state is unsupported. Operational State: (%{public}s) "
+ "User pressed %{public}s (Skip Area) button."
+ "User pressed %{public}s button."
+ "While trying to set Binary state, couldn't unwrap: %{public}s"
+ "While trying to set Picker state with controlId: %{public}s, failed to find a valid mode for selected ID: %{public}ld"
+ "While trying to set Picker state, failed to get selected option: %{public}s"
+ "While trying to set Picker statewith controlId: %{public}s, failed to find a valid mode for selected ID: %{public}ld"
+ "While trying to set button state, failed to get selection state: %{public}s"
+ "_hasOptionsSelected"
+ "_stateUpdated"
+ "_updateBlock"
- "%s Failed to find a DeviceTypeSolver for device type (%s). Source: %s"
- "Changing RVC cleaning mode to: %s, current mode: %s"
- "Changing RVC secondary cleaning mode to: %s, current mode: %s"
- "Incorrect value found for selection state of type: %s selection state: %s"
- "Incorrect values found for selection state of type: %s selection state: %s"
- "Pause cleaning was pressed, current operational state: %s, pausing RVC."
- "Robot vacuum does not support changing selected areas while running; supportsChangingSelectedAreasWhileRunning: %s"
- "Robot vacuum does not support skipping areas; supportsSkipAreaCommand: %s"
- "Start cleaning was pressed, current operational state: %s, resuming RVC."
- "Start cleaning was pressed, current operational state: %s, starting RVC."
- "Start/Pause button was pressed, but current state is unsupported. Operational State: (%s) Running Mode: (%s)"
- "Trying to set Pickker state got an unexpected control type: %s"
- "User pressed %s (Skip Area) button."
- "User pressed %s button."
- "While trying to set Binary state, couldn't unwrap: %s"
- "While trying to set Picker state with controlId: %s, failed to find a valid mode for selected ID: %ld"
- "While trying to set Picker state, failed to get selected option: %s"
- "While trying to set Picker statewith controlId: %s, failed to find a valid mode for selected ID: %ld"
- "While trying to set button state, failed to get selection state: %s"

```
