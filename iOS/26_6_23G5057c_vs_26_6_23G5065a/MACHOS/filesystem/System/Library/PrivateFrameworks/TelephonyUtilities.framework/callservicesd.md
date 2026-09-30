## callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-  __TEXT.__text: 0x4d4b58
+  __TEXT.__text: 0x4d56e8
   __TEXT.__auth_stubs: 0x4e20
-  __TEXT.__objc_stubs: 0x3ad20
-  __TEXT.__objc_methlist: 0x27638
-  __TEXT.__objc_classname: 0x5717
-  __TEXT.__objc_methname: 0x6a467
+  __TEXT.__objc_stubs: 0x3adc0
+  __TEXT.__objc_methlist: 0x27688
+  __TEXT.__objc_classname: 0x5747
+  __TEXT.__objc_methname: 0x6a537
   __TEXT.__cstring: 0x1af3d
   __TEXT.__objc_methtype: 0x1297f
-  __TEXT.__const: 0xec78
+  __TEXT.__const: 0xeca8
   __TEXT.__oslogstring: 0x4efc3
-  __TEXT.__gcc_except_tab: 0x296c
+  __TEXT.__gcc_except_tab: 0x2978
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x89f8
+  __TEXT.__swift5_typeref: 0x89fe
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x92d0
+  __TEXT.__constg_swiftt: 0x92fc
   __TEXT.__swift5_builtin: 0x6cc
   __TEXT.__swift5_reflstr: 0x7fe3
-  __TEXT.__swift5_fieldmd: 0x6798
+  __TEXT.__swift5_fieldmd: 0x67a8
   __TEXT.__swift5_assocty: 0x950
   __TEXT.__swift5_proto: 0x8e0
-  __TEXT.__swift5_types: 0x674
-  __TEXT.__swift5_capture: 0x3964
+  __TEXT.__swift5_types: 0x678
+  __TEXT.__swift5_capture: 0x398c
   __TEXT.__swift5_protos: 0x184
   __TEXT.__swift_as_entry: 0x228
   __TEXT.__swift_as_ret: 0x270
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xe998
+  __TEXT.__unwind_info: 0xe9b8
   __TEXT.__eh_frame: 0x92dc
   __DATA_CONST.__auth_got: 0x2720
-  __DATA_CONST.__got: 0x2490
+  __DATA_CONST.__got: 0x24a8
   __DATA_CONST.__auth_ptr: 0x13d8
-  __DATA_CONST.__const: 0x18868
+  __DATA_CONST.__const: 0x188e0
   __DATA_CONST.__cfstring: 0xb040
-  __DATA_CONST.__objc_classlist: 0xc58
+  __DATA_CONST.__objc_classlist: 0xc60
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0xad8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3cce0
-  __DATA.__objc_selrefs: 0x12978
-  __DATA.__objc_ivar: 0x1e48
-  __DATA.__objc_data: 0xdc30
-  __DATA.__data: 0xfbf8
+  __DATA.__objc_const: 0x3cd58
+  __DATA.__objc_selrefs: 0x129a0
+  __DATA.__objc_ivar: 0x1e4c
+  __DATA.__objc_data: 0xdce0
+  __DATA.__data: 0xfc68
   __DATA.__bss: 0xda90
   __DATA.__common: 0xa38
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
+  - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
   - /System/Library/PrivateFrameworks/FTClientServices.framework/FTClientServices

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25150
-  Symbols:   2660
-  CStrings:  23318
+  Functions: 25166
+  Symbols:   2663
+  CStrings:  23326
 
Symbols:
+ _OBJC_CLASS_$_DADaemonSession
+ _OBJC_CLASS_$_DADevice
+ _OBJC_CLASS_$_DADeviceAppAccessInfo
CStrings:
+ "CSDBluetoothAccessorySetupAuthorization"
+ "T@\"NSNotificationCenter\",R,N,V_notificationCenter"
+ "_notificationCenter"
+ "_startObservingNotifications"
+ "accessoryOptions"
+ "appAccessInfoMap"
+ "getDevicesWithFlags:session:error:"
+ "initWithQueue:assistantServicesObserver:chManager:notificationCenter:"
+ "initWithQueue:assistantServicesObserver:featureFlags:serverBag:chManager:notificationCenter:"
+ "isAuthorizedForBundleIdentifier:"
- "initWithQueue:assistantServicesObserver:chManager:"
- "initWithQueue:assistantServicesObserver:featureFlags:serverBag:chManager:"
```
