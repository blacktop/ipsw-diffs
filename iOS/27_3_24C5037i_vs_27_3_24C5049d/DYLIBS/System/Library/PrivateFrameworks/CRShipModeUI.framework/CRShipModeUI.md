## CRShipModeUI

> `/System/Library/PrivateFrameworks/CRShipModeUI.framework/CRShipModeUI`

```diff

-1307.60.20.0.0
-  __TEXT.__text: 0x35cbc
+1307.60.23.0.0
+  __TEXT.__text: 0x37004
   __TEXT.__objc_methlist: 0x644
-  __TEXT.__const: 0xf88
-  __TEXT.__constg_swiftt: 0xe14
-  __TEXT.__swift5_typeref: 0x7b0
+  __TEXT.__const: 0xfb8
+  __TEXT.__constg_swiftt: 0xe58
+  __TEXT.__swift5_typeref: 0x7ce
   __TEXT.__swift5_reflstr: 0x4f3
-  __TEXT.__swift5_fieldmd: 0x5f4
-  __TEXT.__cstring: 0x3cd9
-  __TEXT.__swift5_capture: 0xa90
+  __TEXT.__swift5_fieldmd: 0x604
+  __TEXT.__cstring: 0x3ea9
+  __TEXT.__swift5_capture: 0xb10
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0xa0
-  __TEXT.__oslogstring: 0x1475
+  __TEXT.__swift5_types: 0xa4
+  __TEXT.__oslogstring: 0x1613
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x80
   __TEXT.__swift_as_cont: 0xd0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0xfa0
+  __TEXT.__unwind_info: 0xfd8
   __TEXT.__eh_frame: 0x1308
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a8
+  __DATA_CONST.__objc_selrefs: 0x6c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1ff8
-  __AUTH_CONST.__objc_const: 0x15a0
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__const: 0x2138
+  __AUTH_CONST.__objc_const: 0x1630
+  __AUTH_CONST.__auth_got: 0x880
   __AUTH.__objc_data: 0xbc0
-  __AUTH.__data: 0x10b8
-  __DATA.__data: 0xdd0
+  __AUTH.__data: 0x1158
+  __DATA.__data: 0xe30
   __DATA.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI
   - /System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1112
-  Symbols:   242
-  CStrings:  324
+  Functions: 1135
+  Symbols:   243
+  CStrings:  333
 
Symbols:
+ _OBJC_CLASS_$_MCProfileConnection
CStrings:
+ "Body of the alert shown when Prepare to Ship is opened on a device managed by an organization (DEP-supervised); the organization, not the user, controls ship mode"
+ "CRShipMode.managedDeviceMessage"
+ "IneligibleForShipmentDEPManaged"
+ "This setting is currently managed by your organization. Contact your administrator for more information."
+ "Title of the alerts and review header shown when the device cannot be prepared to ship (e.g. an untrusted battery, unsupported hardware, or a device managed by an organization)"
+ "isDEPManaged: no MCProfileConnection; treating device as unmanaged"
+ "managedDeviceAlert"
+ "presentManagedDeviceAlert: host is already presenting %{public}s (isBeingDismissed=%{bool,public}d); presenting nothing"
+ "presentManagedDeviceAlert: presenting view controller is gone; presenting nothing"
+ "resolveStateAndPresent: DEP-managed device; blocking user-initiated ship mode, presenting managed-device alert"
- "Title of the alert shown when the device's battery is not trusted and ship mode cannot be started"
```
