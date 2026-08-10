## SetupAssistantSoftwareUpdateUI

> `/System/Library/PrivateFrameworks/SetupAssistantSoftwareUpdateUI.framework/SetupAssistantSoftwareUpdateUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__data`
- `__DATA.__common`

```diff

-772.0.10.0.0
-  __TEXT.__text: 0x77604
+772.0.20.0.0
+  __TEXT.__text: 0x78b6c
   __TEXT.__objc_methlist: 0x748
-  __TEXT.__cstring: 0xf5b
-  __TEXT.__swift5_typeref: 0xfeb
-  __TEXT.__swift5_capture: 0x2018
+  __TEXT.__cstring: 0x104b
+  __TEXT.__swift5_typeref: 0x1005
+  __TEXT.__swift5_capture: 0x2078
   __TEXT.__const: 0xee8
-  __TEXT.__oslogstring: 0x1cb7
-  __TEXT.__constg_swiftt: 0x940
+  __TEXT.__oslogstring: 0x1c97
+  __TEXT.__constg_swiftt: 0x948
   __TEXT.__swift5_reflstr: 0x4dd
   __TEXT.__swift5_fieldmd: 0x320
   __TEXT.__swift5_builtin: 0x8c

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift_as_entry: 0x48
-  __TEXT.__swift_as_ret: 0x78
+  __TEXT.__swift_as_ret: 0x7c
   __TEXT.__swift_as_cont: 0xd4
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x17d8
+  __TEXT.__unwind_info: 0x1800
   __TEXT.__eh_frame: 0xff8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x5190
+  __AUTH_CONST.__const: 0x5258
   __AUTH_CONST.__objc_const: 0x37a8
-  __AUTH_CONST.__auth_got: 0x870
-  __AUTH.__objc_data: 0x1620
+  __AUTH_CONST.__auth_got: 0x888
+  __AUTH.__objc_data: 0x1640
   __AUTH.__data: 0x180
-  __DATA.__data: 0x9d0
+  __DATA.__data: 0x9b8
   __DATA.__bss: 0x750
   __DATA.__common: 0x60
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2110
-  Symbols:   566
-  CStrings:  190
+  Functions: 2125
+  Symbols:   569
+  CStrings:  195
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_wapiCapability
+ _symbolic So17SUUIStatefulErrorCSg
CStrings:
+ "%{public}s button pressed"
+ "%{public}s: environment is nil when instantiating progress view"
+ "%{public}s: reactivePlatformEnvironment is nil in handlePreUpdateError"
+ "A WLAN connection is needed to download this update."
+ "A Wi-Fi connection is needed to download this update."
+ "Choose WLAN Network"
+ "Choose Wi-Fi Network"
+ "Failed to check for updates: %{public}@"
+ "Requesting %{public}s status text for a presented descriptor that is unknown/availableToDownload. Returning \"Update requested\" as a fallback."
+ "SUUISetupAssistantController StatefulUI Observer: Refresh triggered via: %{public}s (state: %{public}s, descriptor state: %{public}s)"
+ "SUUISetupAssistantProgressController StatefulUI Observer: Refresh triggered via: %{public}s (state: %{public}s, descriptor state: %{public}s)"
+ "Transfer Data from \""
+ "Transfer Data from Device"
+ "Transferring directly from this "
+ "Update action \"%{public}s\" has been made by SUUISetupAssistantController but failed.\n    error: %{public}@\n    flowDone: %{bool,public}d"
+ "Update action \"%{public}s\" has been resolved by SUUISetupAssistantController.\n    success: %{bool,public}d\n    flowDone: %{bool,public}d"
+ "Update has maximum version %{public}s ..."
+ "Update has minimum version %{public}s ..."
+ "We got error: %{public}s"
+ "{nil}"
- "%s button pressed"
- "%s: environment is nil when instantiating progress view"
- "%s: reactivePlatformEnvironment is nil in handlePreUpdateError"
- "Failed to check for updates: %@"
- "Migrate from \""
- "Migrate from Device"
- "Migrating from this "
- "Requesting %s status text for a presented descriptor that is unknown/availableToDownload. Returning \"Update requested\" as a fallback."
- "SUUISetupAssistantController StatefulUI Observer: Refresh triggered via: %s (state: %s, descriptor state: %s)"
- "SUUISetupAssistantProgressController StatefulUI Observer: Refresh triggered via: %s (state: %{public}s, descriptor state: %{public}s)"
- "Update action \"%{public}s\" has been made by SUUISetupAssistantController but failed.\n    error: %{public}@\n    flowDone: %{bool}d"
- "Update action \"%{public}s\" has been resolved by SUUISetupAssistantController.\n    success: %{bool,public}d\n    flowDone: %{bool}d"
- "Update action \"%{public}s\" has been resolved by SUUISetupAssistantController.\n    success: %{bool}d\n    flowDone: %{bool}d"
- "Update has maximum version %s ..."
- "Update has minimum version %s ..."
```
