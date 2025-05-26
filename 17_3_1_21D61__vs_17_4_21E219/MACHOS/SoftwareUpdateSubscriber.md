## SoftwareUpdateSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber`

```diff

-1856.80.3.0.1
-  __TEXT.__text: 0x2124
-  __TEXT.__auth_stubs: 0x230
+1856.100.79.0.3
+  __TEXT.__text: 0x2310
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x10c
-  __TEXT.__cstring: 0x2f4
+  __TEXT.__objc_methlist: 0xf4
   __TEXT.__objc_classname: 0xd4
-  __TEXT.__objc_methname: 0x826
-  __TEXT.__oslogstring: 0x3b7
-  __TEXT.__objc_methtype: 0x347
+  __TEXT.__cstring: 0x401
+  __TEXT.__objc_methname: 0x81c
+  __TEXT.__oslogstring: 0x443
+  __TEXT.__objc_methtype: 0x33a
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x120
+  __TEXT.__unwind_info: 0x84
+  __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x30
+  __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x968
-  __DATA.__objc_selrefs: 0x210
-  __DATA.__objc_classrefs: 0x90
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x10
+  __DATA_CONST.__objc_classrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x8f8
+  __DATA.__objc_selrefs: 0x208
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20
-  Symbols:   370
-  CStrings:  188
+  Functions: 18
+  Symbols:   357
+  CStrings:  189
 
Symbols:
+ _OBJC_CLASS_$_SUCoreDDMUtilities
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ __os_log_error_impl
+ __os_log_fault_impl
+ _objc_msgSend$setRemoveBeforeApply:
+ _objc_msgSend$sharedLogger
+ _objc_retain
+ _objc_retain_x24
- -[SoftwareUpdateAdapter logger]
- -[SoftwareUpdateAdapter setLogger:]
- OBJC_IVAR_$_SoftwareUpdateAdapter._logger
- OBJC_IVAR_$_SoftwareUpdateStatus._logger
- _OBJC_CLASS_$_SUCoreLog
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- _kDDMSoftwareUpdateCategory
- _objc_msgSend$initWithCategory:
- _objc_msgSend$logger
- _objc_retain_x22
CStrings:
+ "\x01"
+ "%s: ANOMALY: No date found for declaration? %@, date: %@, formattedDateString: %@"
+ "%s: Anomaly: No controller found to cancel declaration for key %{public}@"
+ "%s: Anomaly: No controller found to enforce declaration"
+ "%s: Anomaly: No controller found to get declaration keys"
+ "%s: Applying configuration with key: %{public}@"
+ "%s: Canceled update, result = %d; error = %{public}@"
+ "%s: Canceled update: %d"
+ "%s: Error, declarations required for non system scope: (long)%ld"
+ "%s: Get configuration UI for: %{public}@"
+ "%s: Querying for status"
+ "%s: Querying status for key paths: %{public}@"
+ "%s: Reporting status %{public}@ %{public}@"
+ "%s: Scheduled update, result = %d, error = %{public}@"
+ "%s: Scheduling update"
+ "-[SoftwareUpdateAdapter applyConfiguration:scope:returningReasons:error:]"
+ "-[SoftwareUpdateAdapter configurationUIForConfiguration:scope:completionHandler:]"
+ "-[SoftwareUpdateStatus queryForStatusWithKeyPaths:store:completionHandler:]_block_invoke"
+ "Invalid declaration payload"
+ "T@\"NSString\",?,R,C"
+ "setRemoveBeforeApply:"
+ "sharedLogger"
- "\x02"
- "@\"SUCoreLog\""
- "Anomaly: No controller found to cancel declaration for key %{public}@"
- "Anomaly: No controller found to enforce declaration"
- "Anomaly: No controller found to get declaration keys"
- "Applying configuration with key: %{public}@"
- "Canceled update, result = %d; error = %{public}@"
- "Canceled update: %d"
- "DDM"
- "Error, declarations required for non system scope: %ld"
- "Get configuration UI for: %{public}@"
- "Querying for status"
- "Querying status for key paths: %{public}@"
- "Reporting status %{public}@ %{public}@"
- "Scheduled update, result = %d, error = %{public}@"
- "Scheduling update"
- "T@\"SUCoreLog\",&,V_logger"
- "_logger"
- "initWithCategory:"
- "logger"
- "setLogger:"

```
