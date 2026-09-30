## AppServerSupport

> `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport`

```diff

-3089.82.3.0.0
-  __TEXT.__text: 0x6e9c
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x96c
+3102.100.97.502.1
+  __TEXT.__text: 0x6ef0
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x994
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x4e6
-  __TEXT.__oslogstring: 0xd82
-  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__cstring: 0x52a
+  __TEXT.__oslogstring: 0xdd6
+  __TEXT.__unwind_info: 0x218
   __TEXT.__objc_classname: 0xe7
-  __TEXT.__objc_methname: 0x18e1
+  __TEXT.__objc_methname: 0x18eb
   __TEXT.__objc_methtype: 0x3b7
-  __TEXT.__objc_stubs: 0xa00
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__objc_stubs: 0xa20
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x608
+  __DATA_CONST.__objc_selrefs: 0x610
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x1568
+  __AUTH_CONST.__objc_const: 0x1598
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0xfc
+  __DATA.__objc_ivar: 0x100
   __DATA.__data: 0xc0
   __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A9CCCA8-B791-3B9A-AE1B-1B7ED4733538
-  Functions: 223
-  Symbols:   854
-  CStrings:  578
+  UUID: D30E9B76-921A-34C4-A929-FED278FB6790
+  Functions: 231
+  Symbols:   873
+  CStrings:  585
 
Symbols:
+ +[LASSProperties4RB propertiesForJob:error:].cold.3
+ +[LASSProperties4RB propertiesForPid:error:].cold.1
+ -[OSLaunchdJob _getPlist]
+ -[OSLaunchdJobInstanceProperties sandboxContainer]
+ -[OSLaunchdJobInstanceProperties setSandboxContainer:]
+ _CFBooleanGetTypeID
+ _CFGetTypeID
+ _OBJC_IVAR_$_OSLaunchdJobInstanceProperties._sandboxContainer
+ ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.98
+ ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.98.cold.1
+ ____lass_log_block_invoke
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ __lass_log
+ __lass_log.cold.1
+ __lass_log.log
+ __lass_log.once
+ _objc_msgSend$_getPlist
+ _objc_msgSend$sandboxContainer
+ _objc_retainAutoreleasedReturnValue
- _OUTLINED_FUNCTION_8
- ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.95
- ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.95.cold.1
- __xpc_assert_dumping_ground
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$path
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
- _objc_retain_x28
- _objc_retain_x3
CStrings:
+ "<unknown>"
+ "Label"
+ "_getPlist"
+ "com.apple.libxpc.AppServerSupport"
+ "sandbox-container"
+ "submit (%@) with label %s failed with error %d: %s"
+ "unable to get attrs for job %@: %s"
+ "unable to get attrs for pid %d: %s"
- "submit (%@) failed with error %d: %s"

```
