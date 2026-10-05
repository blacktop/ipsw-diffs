## FitnessMachineServices

> `/System/Library/PrivateFrameworks/FitnessMachineServices.framework/FitnessMachineServices`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-2027.1.51.0.0
-  __TEXT.__text: 0x51948
-  __TEXT.__objc_methlist: 0x1590
+2027.1.60.0.1
+  __TEXT.__text: 0x51d7c
+  __TEXT.__objc_methlist: 0x15a8
   __TEXT.__const: 0x3978
   __TEXT.__cstring: 0x210b
   __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__oslogstring: 0x1bb0
+  __TEXT.__oslogstring: 0x1cb0
   __TEXT.__swift5_typeref: 0x414a
   __TEXT.__swift5_capture: 0x994
   __TEXT.__constg_swiftt: 0x12ac

   __TEXT.__swift_as_cont: 0x28
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1d88
+  __TEXT.__unwind_info: 0x1d90
   __TEXT.__eh_frame: 0xac4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe18
+  __DATA_CONST.__objc_selrefs: 0xe28
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0x6b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2329
-  Symbols:   5594
-  CStrings:  337
+  Functions: 2331
+  Symbols:   5596
+  CStrings:  339
 
Symbols:
+ -[NLAPMachinePairingAlertUIController _hasOutstandingUserIntentRequest]
+ -[NLAPMachinePairingAlertViewController preferredVerticalBarBehavior]
+ GCC_except_table6
- GCC_except_table9
Functions:
+ -[NLAPMachinePairingAlertViewController preferredVerticalBarBehavior]
~ -[NLAPMachinePairingAlertUIController machinePairingAlertViewControllerDidDeactivate:] : 512 -> 1360
+ -[NLAPMachinePairingAlertUIController _hasOutstandingUserIntentRequest]
~ -[NLAPMachinePairingAlertController _resetAlerts] : 252 -> 276
CStrings:
+ "[FMAlerts] Reject machine connection because alert did deactivate before pairing completed, connectionState: %{public}@"
+ "[FMAlerts] Reject machine connection because alert did deactivate with an outstanding intent request, connectionState: %{public}@"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.Fitness/gymkit-detection"
- "settings-navigation://com.apple.Settings.Apps/com.apple.Fitness/gymkit"
```
