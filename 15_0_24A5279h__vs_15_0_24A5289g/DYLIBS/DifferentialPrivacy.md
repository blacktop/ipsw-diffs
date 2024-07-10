## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/Versions/A/DifferentialPrivacy`

```diff

-609.0.0.0.5
-  __TEXT.__text: 0x64594
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x532c
+614.0.0.0.1
+  __TEXT.__text: 0x650fc
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x5334
   __TEXT.__const: 0x850
-  __TEXT.__cstring: 0x44bd
-  __TEXT.__oslogstring: 0x3d50
-  __TEXT.__gcc_except_tab: 0xc0c
+  __TEXT.__cstring: 0x455d
+  __TEXT.__oslogstring: 0x3f81
+  __TEXT.__gcc_except_tab: 0xbf4
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x74
   __TEXT.__constg_swiftt: 0x218

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__unwind_info: 0x1878
+  __TEXT.__unwind_info: 0x1898
   __TEXT.__eh_frame: 0x3f8
   __TEXT.__objc_classname: 0xd49
-  __TEXT.__objc_methname: 0x972c
+  __TEXT.__objc_methname: 0x973e
   __TEXT.__objc_methtype: 0x1373
-  __TEXT.__objc_stubs: 0x7ae0
-  __DATA_CONST.__got: 0x768
-  __DATA_CONST.__const: 0x718
+  __TEXT.__objc_stubs: 0x7b00
+  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2378
+  __DATA_CONST.__objc_selrefs: 0x2380
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_arraydata: 0x738
-  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__auth_ptr: 0x180
-  __AUTH_CONST.__const: 0xf70
-  __AUTH_CONST.__cfstring: 0x48e0
+  __AUTH_CONST.__const: 0xfa0
+  __AUTH_CONST.__cfstring: 0x4920
   __AUTH_CONST.__objc_const: 0xb708
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_dictobj: 0x78

   __AUTH.__data: 0x1a0
   __DATA.__objc_ivar: 0x534
   __DATA.__data: 0x8d0
-  __DATA.__bss: 0x860
+  __DATA.__bss: 0x8a0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1e00
   __DATA_DIRTY.__bss: 0x28

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2349
-  Symbols:   5432
-  CStrings:  723
+  Functions: 2366
+  Symbols:   5468
+  CStrings:  729
 
Symbols:
+ +[_DPDeviceInfo isRunningAsLaunchDaemon]
+ +[_DPRandomizerUtils containValidDPParametersIn:maxCentralEpsilon:maxCentralDelta:].cold.20
+ +[_DPRandomizerUtils containValidDPParametersIn:maxCentralEpsilon:maxCentralDelta:].cold.21
+ +[_DPRandomizerUtils containValidDPParametersIn:maxCentralEpsilon:maxCentralDelta:].cold.22
+ +[_DPStrings tokensDirectoryPath]
+ +[_DPStrings transparencyLogDirectoryPath]
+ -[_DPDediscoReporter reportDediscoKeys:storage:].cold.1
+ -[_DPDediscoReporter reportDediscoRecords:].cold.4
+ -[_DPServer initWithDatabaseDirectoryPath:reportsDirectoryPath:enablePeriodicTasks:enterSandbox:].cold.2
+ -[_DPServer initWithDatabaseDirectoryPath:reportsDirectoryPath:enablePeriodicTasks:enterSandbox:].cold.3
+ -[_DPServer initWithDatabaseDirectoryPath:reportsDirectoryPath:enablePeriodicTasks:enterSandbox:].cold.4
+ -[_DPServer initWithDatabaseDirectoryPath:reportsDirectoryPath:enablePeriodicTasks:enterSandbox:].cold.5
+ -[_DPStorage saveRecords:andFlush:withCompletion:].cold.2
+ GCC_except_table30
+ _NSHomeDirectory
+ __40+[_DPDeviceInfo isRunningAsLaunchDaemon]_block_invoke.cold.1
+ __44-[_DPCoreDataStorage mocForProtectionClass:]_block_invoke.cold.1
+ __44-[_DPCoreDataStorage mocForProtectionClass:]_block_invoke.cold.2
+ ___33+[_DPStrings tokensDirectoryPath]_block_invoke
+ ___35+[_DPStrings databaseDirectoryPath]_block_invoke
+ ___40+[_DPDeviceInfo isRunningAsLaunchDaemon]_block_invoke
+ ___42+[_DPStrings transparencyLogDirectoryPath]_block_invoke
+ ___block_descriptor_40_e20_v20?0B8"NSError"12l
+ __block_literal_global.16
+ __block_literal_global.16
+ __block_literal_global.24
+ __block_literal_global.32
+ __block_literal_global.37
+ __block_literal_global.42
+ __block_literal_global.47
+ __block_literal_global.52
+ __block_literal_global.57
+ __one_time_setup_block_invoke.cold.7
+ __os_log_fault_impl
+ _getpwuid
+ _getuid
+ _objc_msgSend$isRunningAsLaunchDaemon
+ _objc_msgSend$tokensDirectoryPath
+ _objc_msgSend$transparencyLogDirectoryPath
+ _strcmp
+ _vproc_swap_string
+ databaseDirectoryPath._DPDatabaseDirectoryPath
+ databaseDirectoryPath.onceToken
+ isRunningAsLaunchDaemon.onceToken
+ isRunningAsLaunchDaemon.retval
+ tokensDirectoryPath._DPDediscoTokensDirectoryPath
+ tokensDirectoryPath.onceToken
+ transparencyLogDirectoryPath._DPTransparencyLogDirectoryPath
+ transparencyLogDirectoryPath.onceToken
- +[_DPStrings DediscoReportsDirectoryPath]
- +[_DPStrings DediscoTokensDirectoryPath]
- __87+[_DPPrivacyBudget createDatabaseRecordIfMissingIn:key:balance:cohortAggregateBalance:]_block_invoke.cold.2
- ___block_descriptor_56_e8_32s40r_e20_v20?0B8"NSError"12l
- __block_literal_global.21
- __block_literal_global.26
- __block_literal_global.31
- __block_literal_global.36
- __block_literal_global.41
- __block_literal_global.46
- _objc_msgSend$DediscoReportsDirectoryPath
- _objc_msgSend$DediscoTokensDirectoryPath
CStrings:
+ "%!@(MISSING)/Library/Application Support/DifferentialPrivacy/"
+ "%!@(MISSING)/Library/Logs/PrivacyPreservingMeasurement"
+ "%!@(MISSING)/Library/PPM/PAT/"
+ "HOME"
+ "LoginWindow"
+ "System"
+ "com.apple.dprivacyd.agent"
+ "com.apple.dprivacyd.daemon"
- "/var/lib/PPM/PAT/"
- "enter_custom_sandbox"

```
