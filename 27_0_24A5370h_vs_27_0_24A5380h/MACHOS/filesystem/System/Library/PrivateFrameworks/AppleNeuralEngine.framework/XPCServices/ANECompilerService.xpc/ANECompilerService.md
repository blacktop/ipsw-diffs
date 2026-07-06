## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

```diff

-  __TEXT.__text: 0x167c8
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0x944
+  __TEXT.__text: 0x1819c
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_stubs: 0x2160
+  __TEXT.__objc_methlist: 0x954
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xe77
-  __TEXT.__oslogstring: 0x2025
+  __TEXT.__cstring: 0x1255
+  __TEXT.__oslogstring: 0x20e8
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x2332
+  __TEXT.__objc_methname: 0x246d
   __TEXT.__objc_methtype: 0x601
-  __TEXT.__gcc_except_tab: 0x1048
+  __TEXT.__gcc_except_tab: 0x1210
   __TEXT.__unwind_info: 0x428
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__cfstring: 0x12c0
+  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__cfstring: 0x1880
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__got: 0x1b8
   __DATA.__objc_const: 0xd20
-  __DATA.__objc_selrefs: 0x9d0
+  __DATA.__objc_selrefs: 0xa40
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x3c8
+  __DATA.__data: 0x3f0
   __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 286
-  Symbols:   2405
-  CStrings:  930
+  Functions: 291
+  Symbols:   2458
+  CStrings:  1039
 
Sections:
~ __TEXT.__objc_methtype : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ +[_ANESandboxingHelper issueSandboxExtensionForWeights:]
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSMutableArray
+ __ANECompilerServiceRUsageDict
+ __dispatch_main_q
+ _kANEFCompilerServiceBundleIdentifierKey
+ _kANEFCompilerServiceRUsageAfterKey
+ _kANEFCompilerServiceRUsageBeforeKey
+ _kANEFInMemoryModelFileHashesKey
+ _kANEFInMemoryModelFileNamesKey
+ _objc_msgSend$allValues
+ _objc_msgSend$array
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$containsObject:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$largeModelCompilerServiceAccessEntitlement
+ _objc_msgSend$largeModelCompilerServiceBundleID
+ _objc_msgSend$longLongValue
+ _objc_msgSend$mainBundle
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$setExternConstants:
+ _objc_msgSend$verifyBundleAtPath:expectedHashes:error:
+ _proc_pid_rusage
+ _proc_reset_footprint_interval
+ _xpc_transaction_exit_clean
CStrings:
+ "%@: failed to consume sandbox extension for %@: %@"
+ "%@: releaseSandboxExtension failed for token=%@ handle=%@ errno=%d"
+ "Exiting ANELargeModelCompilerService after compile to avoid VA fragmentation"
+ "Path"
+ "_SBExtension"
+ "allValues"
+ "array"
+ "bundleIdentifier"
+ "com.apple.ANELargeModelCompilerService"
+ "containsObject:"
+ "dictionaryWithCapacity:"
+ "handle"
+ "issueSandboxExtensionForWeights:"
+ "kANEFCompilerServiceBundleIdentifierKey"
+ "kANEFCompilerServiceRUsageAfterKey"
+ "kANEFCompilerServiceRUsageBeforeKey"
+ "kANEFInMemoryModelFileHashesKey"
+ "kANEFInMemoryModelFileNamesKey"
+ "largeModelCompilerServiceAccessEntitlement"
+ "largeModelCompilerServiceBundleID"
+ "longLongValue"
+ "mainBundle"
+ "numberWithLongLong:"
+ "objectAtIndexedSubscript:"
+ "ri_billed_energy"
+ "ri_billed_system_time"
+ "ri_child_elapsed_abstime"
+ "ri_child_interrupt_wkups"
+ "ri_child_pageins"
+ "ri_child_pkg_idle_wkups"
+ "ri_child_system_time"
+ "ri_child_user_time"
+ "ri_cpu_time_qos_background"
+ "ri_cpu_time_qos_default"
+ "ri_cpu_time_qos_legacy"
+ "ri_cpu_time_qos_maintenance"
+ "ri_cpu_time_qos_user_initiated"
+ "ri_cpu_time_qos_user_interactive"
+ "ri_cpu_time_qos_utility"
+ "ri_cycles"
+ "ri_diskio_bytesread"
+ "ri_diskio_byteswritten"
+ "ri_flags"
+ "ri_instructions"
+ "ri_interrupt_wkups"
+ "ri_interval_max_phys_footprint"
+ "ri_lifetime_max_phys_footprint"
+ "ri_logical_writes"
+ "ri_pageins"
+ "ri_phys_footprint"
+ "ri_pkg_idle_wkups"
+ "ri_proc_exit_abstime"
+ "ri_proc_start_abstime"
+ "ri_resident_size"
+ "ri_runnable_time"
+ "ri_serviced_energy"
+ "ri_serviced_system_time"
+ "ri_system_time"
+ "ri_user_time"
+ "ri_wired_size"
+ "setExternConstants:"
+ "token"
+ "verifyBundleAtPath:expectedHashes:error:"

```
