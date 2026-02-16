## MicroLocationUtilities

> `/System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities`

```diff

-35.0.1.0.0
-  __TEXT.__text: 0x6988
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0xbd8
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__cstring: 0x358
+59.0.1.0.9
+  __TEXT.__text: 0x70d0
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0xc60
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x3a6
+  __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__oslogstring: 0x201
-  __TEXT.__unwind_info: 0x2f0
-  __TEXT.__objc_classname: 0x18c
-  __TEXT.__objc_methname: 0x1508
-  __TEXT.__objc_methtype: 0x61f
-  __TEXT.__objc_stubs: 0x1400
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__unwind_info: 0x338
+  __TEXT.__objc_classname: 0x1ae
+  __TEXT.__objc_methname: 0x156a
+  __TEXT.__objc_methtype: 0x97b
+  __TEXT.__objc_stubs: 0x1440
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0x5b8
-  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x718
+  __DATA_CONST.__objc_selrefs: 0x758
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x1488
-  __AUTH.__objc_data: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x58
+  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x300
+  __AUTH_CONST.__objc_const: 0x15f0
+  __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0x410
+  __DATA.__bss: 0x70
+  __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08426331-4A3B-3A9E-BD29-038A67AC7C8D
-  Functions: 239
-  Symbols:   1045
-  CStrings:  449
+  UUID: D81AFCD8-5134-3D9F-AB60-120FC045C013
+  Functions: 255
+  Symbols:   1101
+  CStrings:  474
 
Symbols:
+ +[ULFeatureFlags featureFlagsDescription]
+ +[ULFeatureFlags pil]
+ +[ULFeatureFlags pil].cold.1
+ +[ULMemoryLoadHelper formatBytes:]
+ +[ULPlatform supportsExclave]
+ +[ULPlatform supportsExclave].cold.1
+ -[ULMemoryLoadHelper init]
+ -[ULMemoryLoadHelper load]
+ -[ULMemoryLoadHelper measure]
+ -[ULMemoryLoadHelper peakLoad]
+ -[ULMemoryLoadHelper reset]
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_ULFeatureFlags
+ _OBJC_CLASS_$_ULMemoryLoadHelper
+ _OBJC_IVAR_$_ULMemoryLoadHelper._pid
+ _OBJC_IVAR_$_ULMemoryLoadHelper._rusage
+ _OBJC_METACLASS_$_ULFeatureFlags
+ _OBJC_METACLASS_$_ULMemoryLoadHelper
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_CLASS_METHODS_ULFeatureFlags
+ __OBJC_$_CLASS_METHODS_ULMemoryLoadHelper
+ __OBJC_$_INSTANCE_METHODS_ULMemoryLoadHelper
+ __OBJC_$_INSTANCE_VARIABLES_ULMemoryLoadHelper
+ __OBJC_CLASS_RO_$_ULFeatureFlags
+ __OBJC_CLASS_RO_$_ULMemoryLoadHelper
+ __OBJC_METACLASS_RO_$_ULFeatureFlags
+ __OBJC_METACLASS_RO_$_ULMemoryLoadHelper
+ ___21+[ULFeatureFlags pil]_block_invoke
+ ___29+[ULPlatform supportsExclave]_block_invoke
+ ___block_literal_global.47
+ ___block_literal_global.49
+ __os_feature_enabled_impl
+ _getpid
+ _objc_msgSend$pil
+ _objc_msgSend$supportsExclave
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _pil.cached_result
+ _pil.onceToken
+ _proc_pid_rusage
+ _proc_reset_footprint_interval
+ _supportsExclave.onceToken
+ _supportsExclave.supportsExclave
- ___block_literal_global.44
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "%.3fMB"
+ ", supportsExclave: %@"
+ "@24@0:8d16"
+ "ExclaveCapability"
+ "PIL"
+ "ULFeatureFlags"
+ "ULFeatureFlags:\n PIL: %@ \n"
+ "ULMemoryLoadHelper"
+ "_pid"
+ "_rusage"
+ "d16@0:8"
+ "featureFlagsDescription"
+ "formatBytes:"
+ "i"
+ "load"
+ "measure"
+ "peakLoad"
+ "pil"
+ "reset"
+ "supportsExclave"
+ "{rusage_info_v4=\"ri_uuid\"[16C]\"ri_user_time\"Q\"ri_system_time\"Q\"ri_pkg_idle_wkups\"Q\"ri_interrupt_wkups\"Q\"ri_pageins\"Q\"ri_wired_size\"Q\"ri_resident_size\"Q\"ri_phys_footprint\"Q\"ri_proc_start_abstime\"Q\"ri_proc_exit_abstime\"Q\"ri_child_user_time\"Q\"ri_child_system_time\"Q\"ri_child_pkg_idle_wkups\"Q\"ri_child_interrupt_wkups\"Q\"ri_child_pageins\"Q\"ri_child_elapsed_abstime\"Q\"ri_diskio_bytesread\"Q\"ri_diskio_byteswritten\"Q\"ri_cpu_time_qos_default\"Q\"ri_cpu_time_qos_maintenance\"Q\"ri_cpu_time_qos_background\"Q\"ri_cpu_time_qos_utility\"Q\"ri_cpu_time_qos_legacy\"Q\"ri_cpu_time_qos_user_initiated\"Q\"ri_cpu_time_qos_user_interactive\"Q\"ri_billed_system_time\"Q\"ri_serviced_system_time\"Q\"ri_logical_writes\"Q\"ri_lifetime_max_phys_footprint\"Q\"ri_instructions\"Q\"ri_cycles\"Q\"ri_billed_energy\"Q\"ri_serviced_energy\"Q\"ri_interval_max_phys_footprint\"Q\"ri_runnable_time\"Q}"

```
