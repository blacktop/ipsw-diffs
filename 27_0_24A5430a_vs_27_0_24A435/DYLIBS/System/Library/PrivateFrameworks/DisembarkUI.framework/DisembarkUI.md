## DisembarkUI

> `/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`

```diff

 285.0.0.0.0
-  __TEXT.__text: 0x20790
+  __TEXT.__text: 0x20ac0
   __TEXT.__objc_methlist: 0x2a38
   __TEXT.__const: 0x194
-  __TEXT.__cstring: 0x1df4
+  __TEXT.__cstring: 0x1ea4
   __TEXT.__gcc_except_tab: 0x2a4
-  __TEXT.__oslogstring: 0x109b
+  __TEXT.__oslogstring: 0x1101
   __TEXT.__dlopen_cstrs: 0xc6
   __TEXT.__swift5_typeref: 0x1c0
   __TEXT.__swift5_capture: 0xf0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b10
+  __DATA_CONST.__objc_selrefs: 0x1b20
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0x4c8
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1640
+  __AUTH_CONST.__cfstring: 0x16c0
   __AUTH_CONST.__objc_const: 0x50a8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x5d8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 988
-  Symbols:   2632
-  CStrings:  378
+  Symbols:   2634
+  CStrings:  384
 
Symbols:
+ _objc_msgSend$isEuiccActiveWithError:
+ _objc_msgSend$supportsDynamicSIMConfigurationWithError:
Functions:
~ -[DKTelephonyProvider isPhysicalSIMModeActive] : 8 -> 628
~ +[DKEraseConfirmationAlertController alertControllerWithCellularPlans:physicalSIMModeActive:completion:] : 1580 -> 1776
CStrings:
+ "%@%@"
+ "ERASE_CONFIRMATION_ALERT_PHYSICAL_SIM_BACK_SIM_DEACTIVATION_MESSAGE_PLURAL"
+ "ERASE_CONFIRMATION_ALERT_PHYSICAL_SIM_BACK_SIM_DEACTIVATION_MESSAGE_SINGULAR"
+ "Failed to query isEuiccActive: %{public}@"
+ "Failed to query supportsDynamicSIMConfiguration: %{public}@"
+ "Localizable-V63"
```
