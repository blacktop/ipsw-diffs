## BridgeReporting

> `/System/Library/PrivateFrameworks/BridgeReporting.framework/BridgeReporting`

```diff

-1159.12.0.0.0
-  __TEXT.__text: 0x7130
+1159.14.0.0.0
+  __TEXT.__text: 0x7364
   __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x858
+  __TEXT.__objc_methlist: 0x8b0
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__cstring: 0xfda
-  __TEXT.__oslogstring: 0x625
+  __TEXT.__cstring: 0x105d
+  __TEXT.__oslogstring: 0x648
   __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x1fd9
+  __TEXT.__objc_methname: 0x20d1
   __TEXT.__objc_methtype: 0x2d0
-  __TEXT.__objc_stubs: 0x1540
+  __TEXT.__objc_stubs: 0x15a0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x698
+  __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1010
-  __DATA_CONST.__objc_selrefs: 0x6f0
+  __DATA_CONST.__objc_const: 0x1070
+  __DATA_CONST.__objc_selrefs: 0x718
   __DATA_CONST.__objc_classrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__objc_const: 0x2d0
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x13e0
+  __AUTH_CONST.__cfstring: 0x1420
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x1f0
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0xc0
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 211
-  Symbols:   958
-  CStrings:  633
+  Functions: 218
+  Symbols:   979
+  CStrings:  646
 
Symbols:
+ -[BRRTCMigrationMetric lastActiveDate]
+ -[BRRTCMigrationMetric migrationDeviceUnpairedByUserAction]
+ -[BRRTCMigrationMetric setLastActiveDate:]
+ -[BRRTCMigrationMetric setMigrationDeviceUnpairedByUserAction:]
+ -[BRRTCMigrationReportManager formatDate:]
+ -[BRRTCMigrationReportManager setLastActiveDate:]
+ -[BRRTCMigrationReportManager setMigrationDeviceUnpairedByUserAction:]
+ GCC_except_table16
+ _BRMigrationDeviceLastActiveDate
+ _BRMigrationDeviceUnpairedByUserActionKey
+ _OBJC_IVAR_$_BRRTCMigrationMetric._lastActiveDate
+ _OBJC_IVAR_$_BRRTCMigrationMetric._migrationDeviceUnpairedByUserAction
+ _objc_msgSend$formatDate:
+ _objc_msgSend$setLastActiveDate:
+ _objc_msgSend$setMigrationDeviceUnpairedByUserAction:
- GCC_except_table14
CStrings:
+ "\x19"
+ "%s device %@ unpair by user action"
+ "-[BRRTCMigrationReportManager setMigrationDeviceUnpairedByUserAction:]"
+ "MigrationDeviceUnpairedByUserAction"
+ "MigrationLastActiveDate"
+ "T@\"NSString\",&,N,V_lastActiveDate"
+ "TB,N,V_migrationDeviceUnpairedByUserAction"
+ "WatchMaxPairingVersion"
+ "_lastActiveDate"
+ "_migrationDeviceUnpairedByUserAction"
+ "formatDate:"
+ "lastActiveDate"
+ "migrationDeviceUnpairedByUserAction"
+ "setLastActiveDate:"
+ "setMigrationDeviceUnpairedByUserAction:"
- "\x18"
- "WatchMAxPairingVersion"

```
