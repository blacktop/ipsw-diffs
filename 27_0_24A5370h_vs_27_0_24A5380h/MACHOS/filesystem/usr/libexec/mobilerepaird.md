## mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

-  __TEXT.__text: 0xe2b8
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_stubs: 0x1be0
+  __TEXT.__text: 0xe088
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_stubs: 0x1c00
   __TEXT.__objc_methlist: 0xcfc
-  __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x3a8
-  __TEXT.__objc_methname: 0x211d
+  __TEXT.__const: 0xb2
+  __TEXT.__gcc_except_tab: 0x3d0
+  __TEXT.__objc_methname: 0x212c
   __TEXT.__cstring: 0x23b9
   __TEXT.__oslogstring: 0xb2c
   __TEXT.__objc_classname: 0x2e1
   __TEXT.__objc_methtype: 0x3da
-  __TEXT.__unwind_info: 0x330
-  __DATA_CONST.__const: 0x498
+  __TEXT.__unwind_info: 0x350
+  __DATA_CONST.__const: 0x478
   __DATA_CONST.__cfstring: 0x2300
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x350
+  __DATA_CONST.__got: 0x330
   __DATA.__objc_const: 0x1b08
-  __DATA.__objc_selrefs: 0x8d0
+  __DATA.__objc_selrefs: 0x8d8
   __DATA.__objc_ivar: 0xbc
   __DATA.__objc_data: 0x820
-  __DATA.__data: 0x198
+  __DATA.__data: 0x190
   __DATA.__bss: 0x160
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
+  - /System/Library/PrivateFrameworks/BatteryDischarge.framework/BatteryDischarge
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 295
-  Symbols:   200
-  CStrings:  1106
+  Functions: 292
+  Symbols:   201
+  CStrings:  1107
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__oslogstring : content changed
~ __TEXT.__objc_classname : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_imageinfo : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "numberWithInt:"

```
