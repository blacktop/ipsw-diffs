## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-1006.0.0.0.0
-  __TEXT.__text: 0x7d74c
-  __TEXT.__auth_stubs: 0x1470
+1007.0.0.0.1
+  __TEXT.__text: 0x7dab4
+  __TEXT.__auth_stubs: 0x14a0
   __TEXT.__objc_methlist: 0x61b4
-  __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x7bae
-  __TEXT.__oslogstring: 0xb4dd
+  __TEXT.__const: 0x1f8
+  __TEXT.__cstring: 0x7c0f
+  __TEXT.__oslogstring: 0xb539
   __TEXT.__gcc_except_tab: 0xcbc
-  __TEXT.__unwind_info: 0x1a98
-  __TEXT.__objc_classname: 0xf79
-  __TEXT.__objc_methname: 0xd4b5
-  __TEXT.__objc_methtype: 0x2cc4
-  __TEXT.__objc_stubs: 0xa220
+  __TEXT.__unwind_info: 0x1b48
+  __TEXT.__objc_classname: 0xf7c
+  __TEXT.__objc_methname: 0xd4d8
+  __TEXT.__objc_methtype: 0x2cd2
+  __TEXT.__objc_stubs: 0xa240
   __DATA_CONST.__got: 0x770
   __DATA_CONST.__const: 0x1770
   __DATA_CONST.__objc_classlist: 0x378

   __DATA_CONST.__objc_selrefs: 0x2e00
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x768
-  __AUTH_CONST.__auth_got: 0xa48
-  __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x6ac0
-  __AUTH_CONST.__objc_const: 0xd548
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH_CONST.__const: 0x640
+  __AUTH_CONST.__cfstring: 0x6b20
+  __AUTH_CONST.__objc_const: 0xd568
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0xa18
+  __DATA.__objc_ivar: 0xa1c
   __DATA.__data: 0x1320
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x20d0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x260

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 3A602039-B5EE-3ACC-9896-D4A173897528
-  Functions: 2713
-  Symbols:   9462
-  CStrings:  5416
+  UUID: 59859DAA-BB4B-3BA7-B3C5-4C0F3BC14341
+  Functions: 2719
+  Symbols:   9481
+  CStrings:  5426
 
Symbols:
+ +[RBThermalResponseManager _thermalConditionLevelForThermalLevel:notificationName:]
+ -[RBDaemon _EnterSandbox]
+ -[RBDaemon _EnterSandbox].cold.1
+ GCC_except_table23
+ GCC_except_table34
+ GCC_except_table43
+ GCC_except_table59
+ _MGCopyAnswer
+ _NSTemporaryDirectory
+ _OBJC_IVAR_$_RBThermalResponseManager._notificationName
+ ___block_literal_global.350
+ ___block_literal_global.47
+ ___block_literal_global.90
+ ___block_literal_global.95
+ ___currentDeviceClass_block_invoke
+ __errorWithRequestCode
+ __set_user_dir_suffix
+ _currentDeviceClass
+ _currentDeviceClass.__once
+ _currentDeviceClass.__value
+ _currentDeviceClass.cold.1
+ _objc_msgSend$_thermalConditionLevelForThermalLevel:notificationName:
+ _objc_msgSend$managerWithDaemonContext:notificationName:
- +[RBThermalResponseManager _thermalConditionLevelForThermalLevel:]
- GCC_except_table22
- GCC_except_table42
- GCC_except_table58
- ___block_literal_global.344
- ___block_literal_global.44
- ___block_literal_global.89
- _objc_msgSend$_thermalConditionLevelForThermalLevel:
CStrings:
+ "DeviceClassNumber"
+ "Diagnostic collection failed: [%@]"
+ "Thermal mitigation disabled, device is not an iPad"
+ "_notificationName"
+ "_thermalConditionLevelForThermalLevel:notificationName:"
+ "com.apple.system.thermalmitigation"
+ "com.apple.system.thermalpressurelevel"
+ "failed to initialize temporary directory"
+ "q32@0:8Q16@24"
- "Diagnostic collection failed"
- "_thermalConditionLevelForThermalLevel:"

```
