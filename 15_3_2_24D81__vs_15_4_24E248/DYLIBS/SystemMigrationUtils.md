## SystemMigrationUtils

> `/System/Library/PrivateFrameworks/SystemMigrationUtils.framework/Versions/A/SystemMigrationUtils`

```diff

-5713.60.15.0.0
-  __TEXT.__text: 0xc678
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_methlist: 0xa4c
+5739.100.175.0.0
+  __TEXT.__text: 0xbba8
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0xa6c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1d55
-  __TEXT.__gcc_except_tab: 0x1f8
+  __TEXT.__cstring: 0x1c56
+  __TEXT.__gcc_except_tab: 0x204
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x310
-  __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x2264
-  __TEXT.__objc_methtype: 0x3e6
-  __TEXT.__objc_stubs: 0x1fa0
-  __DATA_CONST.__got: 0x270
+  __TEXT.__unwind_info: 0x308
+  __TEXT.__objc_classname: 0x167
+  __TEXT.__objc_methname: 0x1fef
+  __TEXT.__objc_methtype: 0x3c3
+  __TEXT.__objc_stubs: 0x1e00
+  __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f8
+  __DATA_CONST.__objc_selrefs: 0x970
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x4e8
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1b40
-  __AUTH_CONST.__objc_const: 0x1398
+  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x1ac0
+  __AUTH_CONST.__objc_const: 0x11c8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x68
   __DATA.__bss: 0x48
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libfakelink.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0251644-0F53-3CA1-9B40-1CDA7487D23A
-  Functions: 249
-  Symbols:   956
-  CStrings:  971
+  UUID: 4876A635-5270-3EFE-A0BA-0B62ECEC7BBC
+  Functions: 236
+  Symbols:   915
+  CStrings:  932
 
Symbols:
+ +[SMAnalyticsManager sharedManager].cold.1
+ +[SMLogging logType:inFunction:atLine:withString:].cold.4
+ +[SMLogging logType:inFunction:atLine:withString:].cold.5
+ +[SMUtilities commonBundleExtensions].cold.1
+ +[SMUtilities isMainQueue].cold.1
+ -[NSURL(SMUtilities) isPathPlatformBinary]
+ GCC_except_table4
+ _kCFURLFileIdentifierKey
- +[SMToolBox sendSignal:toProcess:]
- -[NSURL(SMUtilities) SM_bundleIsPlatformBinary]
- -[SMTask estimatedTimeToComplete]
- -[SMTask parentProgressPendingUnits]
- -[SMTask parentProgressQueue]
- -[SMTask parentProgress]
- -[SMTask setEstimatedTimeToComplete:]
- -[SMTask setParentProgress:]
- -[SMTask setParentProgressPendingUnits:]
- -[SMTask setParentProgressQueue:]
- OBJC_IVAR_$_SMTask._estimatedTimeToComplete
- OBJC_IVAR_$_SMTask._parentProgress
- OBJC_IVAR_$_SMTask._parentProgressPendingUnits
- OBJC_IVAR_$_SMTask._parentProgressQueue
- _OBJC_CLASS_$_NSProgress
- __13-[SMTask run]_block_invoke.23
- __13-[SMTask run]_block_invoke.33
- __13-[SMTask run]_block_invoke_2.37
- ___13-[SMTask run]_block_invoke
- ___13-[SMTask run]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e5_v8?0l
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0l
- ___copy_helper_block_e8_32s40s
- ___copy_helper_block_e8_32s40s48s
- ___destroy_helper_block_e8_32s40s
- ___destroy_helper_block_e8_32s40s48s
- __dispatch_source_type_timer
- __kCFURLInodeNumberKey
- _dispatch_get_global_queue
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _dispatch_time
- _objc_msgSend$addChild:withPendingUnitCount:
- _objc_msgSend$completedUnitCount
- _objc_msgSend$estimatedTimeToComplete
- _objc_msgSend$initWithParent:userInfo:
- _objc_msgSend$isRunning
- _objc_msgSend$lookupProcessIdentifierByName:
- _objc_msgSend$parentProgress
- _objc_msgSend$parentProgressPendingUnits
- _objc_msgSend$parentProgressQueue
- _objc_msgSend$setCompletedUnitCount:
- _objc_msgSend$setEstimatedTimeToComplete:
- _objc_msgSend$setTotalUnitCount:
- _objc_msgSend$totalUnitCount
CStrings:
+ "-[NSURL(SMUtilities) isPathPlatformBinary]"
+ "Platform binary check: could not load signature from %@ (OSStatus %d)"
+ "Platform binary check: could not retrieve code signature from %@ (OSStatus %d)"
+ "Platform binary check: platform binary found at %@"
+ "[SMSystem_FileManager_ROSV] %p Returning from init at (%@) with dv: (%@) and sv: (%@)"
+ "[SMSystem_FileManager_ROSV] %p Returning from init unexpectedly?"
+ "[SMSystem_FileManager_ROSV] Returning nil userContent root! %p dataVolumeMount: (%@)"
+ "isPathPlatformBinary"
- "-[NSURL(SMUtilities) SM_bundleIsPlatformBinary]"
- "-[SMTask run]_block_invoke"
- "-[SMTask run]_block_invoke_2"
- "@\"NSProgress\""
- "FileManager: Returning NIL userContent root! %p dataVolumeMount: (%@)"
- "Filemanager: %p Returning from init at (%@) with dv: (%@) and sv: (%@)"
- "Filemanager: %p Returning from init unexpectedly?"
- "Platform Binary: CodeCopySigningInformation failed (OSS %d): %@"
- "Platform Binary: Could not create code from path (OSS %d): %@"
- "Platform Binary: Found platform signature at path: %@"
- "Progress info: Task (%@) progress added [Expected: %f - (%f | 1 unit each)]: \n%@"
- "Progress info: Task (%@) progress finish confirmed: \n%@"
- "Progress info: Task (%@) progress not updated as it is already at max: \n%@"
- "Progress info: Task (%@) progress updated: \n%@"
- "SM_bundleIsPlatformBinary"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_parentProgressQueue"
- "T@\"NSProgress\",&,V_parentProgress"
- "Td,V_estimatedTimeToComplete"
- "Td,V_parentProgressPendingUnits"
- "_estimatedTimeToComplete"
- "_parentProgress"
- "_parentProgressPendingUnits"
- "_parentProgressQueue"
- "addChild:withPendingUnitCount:"
- "completedUnitCount"
- "d"
- "d16@0:8"
- "estimatedTimeToComplete"
- "initWithParent:userInfo:"
- "isRunning"
- "lookupProcessIdentifierByName:"
- "parentProgress"
- "parentProgressPendingUnits"
- "parentProgressQueue"
- "sendSignal:toProcess:"
- "setCompletedUnitCount:"
- "setEstimatedTimeToComplete:"
- "setParentProgress:"
- "setParentProgressPendingUnits:"
- "setParentProgressQueue:"
- "setTotalUnitCount:"
- "totalUnitCount"
- "v24@0:8d16"

```
