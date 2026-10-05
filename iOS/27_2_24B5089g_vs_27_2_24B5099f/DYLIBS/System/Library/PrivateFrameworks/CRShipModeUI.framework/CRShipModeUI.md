## CRShipModeUI

> `/System/Library/PrivateFrameworks/CRShipModeUI.framework/CRShipModeUI`

```diff

-1307.40.51.0.0
-  __TEXT.__text: 0x2d4cc
-  __TEXT.__objc_methlist: 0x624
-  __TEXT.__const: 0xd50
-  __TEXT.__constg_swiftt: 0xd5c
-  __TEXT.__swift5_typeref: 0x648
-  __TEXT.__swift5_reflstr: 0x4a5
-  __TEXT.__swift5_fieldmd: 0x56c
-  __TEXT.__cstring: 0x3b80
-  __TEXT.__swift5_capture: 0x6b4
+1307.40.64.0.0
+  __TEXT.__text: 0x35cbc
+  __TEXT.__objc_methlist: 0x644
+  __TEXT.__const: 0xf88
+  __TEXT.__constg_swiftt: 0xe14
+  __TEXT.__swift5_typeref: 0x7b0
+  __TEXT.__swift5_reflstr: 0x4f3
+  __TEXT.__swift5_fieldmd: 0x5f4
+  __TEXT.__cstring: 0x3cd9
+  __TEXT.__swift5_capture: 0xa90
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x98
-  __TEXT.__oslogstring: 0x1159
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x50
-  __TEXT.__swift_as_cont: 0xbc
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xcb8
-  __TEXT.__eh_frame: 0xea0
+  __TEXT.__swift5_proto: 0x4c
+  __TEXT.__swift5_types: 0xa0
+  __TEXT.__oslogstring: 0x1475
+  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_ret: 0x80
+  __TEXT.__swift_as_cont: 0xd0
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__unwind_info: 0xfa0
+  __TEXT.__eh_frame: 0x1308
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x680
+  __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1410
-  __AUTH_CONST.__objc_const: 0x15e8
-  __AUTH_CONST.__auth_got: 0x858
+  __AUTH_CONST.__const: 0x1ff8
+  __AUTH_CONST.__objc_const: 0x15a0
+  __AUTH_CONST.__auth_got: 0x878
   __AUTH.__objc_data: 0xbc0
-  __AUTH.__data: 0x10c0
-  __DATA.__data: 0xd70
-  __DATA.__common: 0x40
+  __AUTH.__data: 0x10b8
+  __DATA.__data: 0xdd0
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 859
-  Symbols:   237
-  CStrings:  307
+  Functions: 1112
+  Symbols:   242
+  CStrings:  324
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
+ _kCACornerCurveContinuous
+ _os_variant_has_internal_content
+ _swift_release_x10
+ _swift_release_x2
+ _swift_retain_x9
- _swift_release_x9
CStrings:
+ "%s: presenting prepare-for-shipping privacy disclosure (named recipient: %{bool,public}d)"
+ "-CRShipModeFakeDaemon"
+ "AKAuthenticationError"
+ "Body of the alert shown when the shipping preparation can't be cancelled because the recipient still holds a claim. %@ is the recipient name reported by the server. Translators may reposition %@ as grammar requires."
+ "Body of the double-confirmation alert shown when the user taps Don't Ship on the partner confirmation screen, including how long the charge limit stays locked. %@ is a localized duration such as \"30 minutes\" or \"3 days\". Translators may reposition %@ as grammar requires."
+ "Body of the informational alert shown when the shipping preparation can't be cancelled and no recipient was reported by the server — either the server's undo timer has not expired yet, or a claim is held by an unnamed recipient"
+ "CRShipMode.cancelShipMode"
+ "CRShipMode.contactPartnerMessageWithName"
+ "CRShipMode.unableToCancelPreparationTimerMessage"
+ "CRShipMode.unableToCancelPreparationTitle"
+ "CRShipModeDeviceErrorReport: report failed to enqueue: %{public}s"
+ "CRShipModeDeviceErrorReport: reporting ship-mode device error to server (%{public}s)"
+ "Cancel Shipping Preparation"
+ "Find My repair: authentication failed (%{public}s); AuthKit already reported it, ending repair/trade-in flow without a second alert"
+ "Find My repair: repair mode could not be enabled (%{public}s); no error UI from Find My, presenting retry and ending repair/trade-in flow"
+ "FlowEndedDeviceError"
+ "If someone else is going to use your iPhone, you should erase it to remove your personal data. For repairs, you do not need to erase your iPhone."
+ "Partner confirmation screen detail (no partner) including how long the charge limit stays locked. %@ is a localized duration such as \"30 minutes\" or \"3 days\". Translators may reposition %@ as grammar requires."
+ "Partner confirmation screen detail when no specific partner is reported and no charge-limit lock duration is available"
+ "Prepare iPhone to Ship"
+ "Shared title of the alerts shown when the shipping preparation could not be cancelled — the recipient still holds a claim, the server's undo timer has not expired, or the firmware disengage failed"
+ "Title of the confirmation alert shown when cancelling the shipping preparation (Other Shipping Purpose branch)"
+ "Tray button title on the discharge progress screen that opens the cancel-preparation confirmation"
+ "Unable to Cancel Shipping Preparation"
+ "You can try again after the timer expires."
+ "You will not be able to change the charge limit of your iPhone for %@."
+ "You will not be able to change the charge limit of your iPhone for %@. Apple will make the ship status of your iPhone available for any service provider who tries to look it up."
+ "You will not be able to change the charge limit of your iPhone."
+ "activateShipMode: ship-charge limit unsupported on this hardware; ending the peer-to-peer flow without a report"
+ "battery not trusted"
+ "battery not trusted, already in ship mode"
+ "checkmark.circle.fill"
+ "confirmPartner: %{public}s; reporting the device error and ending the flow instead of preparing"
+ "contactPartnerAlert"
+ "ineligible — ship-charge limit no longer engaged"
+ "performServerCheckedRemoval: server holds no ship-mode publication from this device (partner claim present: %{bool,public}d); disengaging locally without notifying the server"
+ "popToLastPresentedScreen: popping %{public}ld foreign view controller(s) off the ship mode nav stack"
+ "prepareForShippingAlert"
+ "prepareForShippingCancel"
+ "prepareForShippingContinue"
+ "present: no ship-charge-limit state reported for this device; presenting nothing"
+ "removePartnerAlert"
+ "removePartnerCancel"
+ "removePartnerContinue"
+ "reportAndPresentIneligible: not publishing the device error (%{public}s); ship mode was not entered via trade-in, so no disclosure was shown"
+ "retireCoveredLoadingPlaceholder: another screen covered the ship mode spinner; dropping it from the stack"
+ "ship-charge limit unsupported on this hardware"
+ "undoConfirmationAlert"
+ "undoFailureAlert"
+ "undoNoInternetAlert"
- "%s: presenting prepare-for-shipping confirmation (named recipient: %{bool,public}d)"
- "BatteryTrustFailedBlockedAtEntry"
- "Body of the alert shown when undoing ship mode is blocked by an active partner claim. Instructs the user to contact the shipment recipient; the partner name is shown in the title, not repeated here."
- "Body of the double-confirmation alert shown when the user taps Don't Ship on the partner confirmation screen, including how long ship mode lasts. %@ is a localized duration such as \"30 minutes\" or \"3 days\". Translators may reposition %@ as grammar requires."
- "Body of the informational alert shown when tapping Undo Shipping Preparation while the active session was enabled via the Repair, Trade-In & Returns flow"
- "CRShipMode.cancelRepairTradeInOrReturnsMessage"
- "CRShipMode.cancelRepairTradeInOrReturnsTitle"
- "CRShipMode.contactPartnerMessage"
- "CRShipMode.contactPartnerTitle"
- "CRShipMode.undoFailedTitle"
- "Find My repair: lookup failed (%{public}s) so repair mode could not be enabled; presenting retry and ending repair/trade-in flow"
- "If your iPhone is going to be used by someone else, you need to erase it. For repairs, you do not need to erase your iPhone."
- "IneligibleForShipmentShipChargeLimitUnsupported"
- "Partner confirmation screen detail (no partner) including how long ship mode lasts. %@ is a localized duration such as \"30 minutes\" or \"3 days\". Translators may reposition %@ as grammar requires."
- "Partner confirmation screen detail when no specific partner is reported and no ship-mode duration is available"
- "Reason for Shipping"
- "Title of the alert shown when the firmware disengage fails during the undo flow"
- "Title of the alert shown when undoing ship mode is blocked by an active partner claim. %@ is the partner name reported by the server. Translators may reposition %@ as grammar requires."
- "Title of the confirmation alert shown when undoing ship mode preparation (Other Shipping Purpose branch)"
- "Title of the informational alert shown when tapping Undo Shipping Preparation while the active session was enabled via the Repair, Trade-In & Returns flow"
- "To undo ship mode, you’ll need to contact the recipient."
- "Unable to Undo Ship Mode"
- "Your iPhone is ready to ship. Your battery was discharged and the charge limit was applied. You can undo shipping preparation at any time."
- "Your iPhone is temporarily locked for shipping. It will unlock when Ship Mode automatically expires."
- "Your iPhone will be locked in Ship Mode for %@. Apple will make the ship status of your iPhone available for any service provider who tries to look it up."
- "Your iPhone will be locked in ship mode for %@."
- "Your iPhone will be locked in ship mode."
- "iPhone Locked in Ship Mode"
- "largecircle.fill.circle"
- "resolveStateAndPresent: battery not trusted; reporting device error to server"
- "resolveStateAndPresent: ineligible device-error report failed to enqueue: %{public}s"
- "resolveStateAndPresent: ship-charge limit unsupported; showing unable-to-prepare alert"
- "resolveStateAndPresent: ship-mode device-error report failed to enqueue: %{public}s"
```
