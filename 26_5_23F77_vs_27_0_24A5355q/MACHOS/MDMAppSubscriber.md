## MDMAppSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/MDMAppSubscriber.xpc/MDMAppSubscriber`

```diff

-585.120.2.0.0
-  __TEXT.__text: 0x840
-  __TEXT.__auth_stubs: 0x1b0
+621.0.0.502.1
+  __TEXT.__text: 0x784
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x440
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x58

   __TEXT.__objc_methname: 0x483
   __TEXT.__objc_methtype: 0x141
   __TEXT.__oslogstring: 0x32
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x70
   __DATA.__objc_const: 0x260
   __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_data: 0x50

   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
+  - /System/Library/PrivateFrameworks/ManagedDevice.framework/ManagedDevice
   - /System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement
   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B686FCD9-64EF-3FB5-AEA5-D414DAE64760
+  UUID: BF6E3999-86A6-32A4-B284-CF40792C2EE3
   Functions: 12
-  Symbols:   72
+  Symbols:   74
   CStrings:  105
 
Symbols:
+ _OBJC_CLASS_$_MDFConnection
+ _OBJC_CLASS_$_MDFFetchAppsRequest
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
- _OBJC_CLASS_$_DMFConnection
- _OBJC_CLASS_$_DMFFetchAppsRequest
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x23
- _objc_retain_x24
CStrings:
+ "v24@?0@\"MDFFetchAppsResultObject\"8@\"NSError\"16"
- "v24@?0@\"DMFFetchAppsResultObject\"8@\"NSError\"16"

```
