## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-248.0.0.0.0
-  __TEXT.__text: 0x422d4
+251.0.0.0.1
+  __TEXT.__text: 0x42b04
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0x5340
-  __TEXT.__objc_methlist: 0x2aec
-  __TEXT.__cstring: 0x3b34
-  __TEXT.__objc_methname: 0x5ff6
-  __TEXT.__oslogstring: 0x4473
+  __TEXT.__objc_stubs: 0x53a0
+  __TEXT.__objc_methlist: 0x2b0c
+  __TEXT.__cstring: 0x3b5d
+  __TEXT.__objc_methname: 0x603e
+  __TEXT.__oslogstring: 0x4570
   __TEXT.__objc_classname: 0x77b
   __TEXT.__objc_methtype: 0x1255
-  __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0x638
+  __TEXT.__gcc_except_tab: 0x16c
+  __TEXT.__unwind_info: 0x640
   __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x5d18
-  __DATA_CONST.__cfstring: 0x3120
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x5df0
+  __DATA_CONST.__cfstring: 0x3160
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x180
   __DATA.__objc_const: 0x4988
-  __DATA.__objc_selrefs: 0x18e0
+  __DATA.__objc_selrefs: 0x18f8
   __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x7b0

   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
+  - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 558E101A-A488-34E3-8B28-4655BD303334
-  Functions: 983
-  Symbols:   310
-  CStrings:  2359
+  UUID: B932DF52-D7CE-32C4-ACEC-BD819FF69EB9
+  Functions: 987
+  Symbols:   311
+  CStrings:  2372
 
Symbols:
+ _OBJC_CLASS_$_MIBUClient
CStrings:
+ "%{public}@ was unexpectedly canceled"
+ "Alert was canceled"
+ "MIBUClient error: %@"
+ "Pallet mode timer elapsed.  Rebooting."
+ "Pallet mode timer started. MIBU: %d | defaults: %d"
+ "Should not show a post update alert; not showing alert item for reason: %@"
+ "[%{public}@] alertWasCanceled"
+ "_AllowUserInteraction"
+ "alertWasCanceled"
+ "isInPalletUpdateMode:"
+ "useMobileInboxUpdaterRebootDelay"

```
