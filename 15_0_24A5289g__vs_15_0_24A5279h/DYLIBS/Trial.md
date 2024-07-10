## Trial

> `/System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial`

```diff

-426.0.0.0.0
-  __TEXT.__text: 0x8428c
-  __TEXT.__auth_stubs: 0xa50
+424.0.0.0.0
+  __TEXT.__text: 0x823d0
+  __TEXT.__auth_stubs: 0x9f0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x64d4
-  __TEXT.__const: 0xf22
-  __TEXT.__gcc_except_tab: 0x545c
-  __TEXT.__cstring: 0x93ac
-  __TEXT.__oslogstring: 0x47dd
+  __TEXT.__objc_methlist: 0x636c
+  __TEXT.__const: 0xf1a
+  __TEXT.__gcc_except_tab: 0x53f4
+  __TEXT.__cstring: 0x8c74
+  __TEXT.__oslogstring: 0x47af
   __TEXT.__dlopen_cstrs: 0x101
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2660
-  __TEXT.__objc_classname: 0x13e5
-  __TEXT.__objc_methname: 0xe446
-  __TEXT.__objc_methtype: 0x2d96
-  __TEXT.__objc_stubs: 0x9c20
-  __DATA_CONST.__got: 0x848
-  __DATA_CONST.__const: 0x8c8
-  __DATA_CONST.__objc_classlist: 0x4f8
+  __TEXT.__unwind_info: 0x2600
+  __TEXT.__objc_classname: 0x13b0
+  __TEXT.__objc_methname: 0xdf5e
+  __TEXT.__objc_methtype: 0x2d12
+  __TEXT.__objc_stubs: 0x9740
+  __DATA_CONST.__got: 0x810
+  __DATA_CONST.__const: 0x870
+  __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3300
+  __DATA_CONST.__objc_selrefs: 0x3168
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x338
-  __DATA_CONST.__objc_arraydata: 0x1b8
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__const: 0x24e8
-  __AUTH_CONST.__cfstring: 0x7180
-  __AUTH_CONST.__objc_const: 0xdd88
-  __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2580
+  __DATA_CONST.__objc_arraydata: 0x68
+  __AUTH_CONST.__auth_got: 0x510
+  __AUTH_CONST.__const: 0x2438
+  __AUTH_CONST.__cfstring: 0x6720
+  __AUTH_CONST.__objc_const: 0xdbc0
+  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH.__objc_data: 0x2490
   __DATA.__objc_ivar: 0x6f0
   __DATA.__data: 0xdc0
-  __DATA.__bss: 0x348
+  __DATA.__bss: 0x340
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x1b0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2559
-  Symbols:   6624
-  CStrings:  1098
+  Functions: 2527
+  Symbols:   6520
+  CStrings:  1006
 
Symbols:
+ GCC_except_table120
+ __block_literal_global.164
+ __block_literal_global.178
- +[TRICCommandRunner _withLoggingRunCommand:arguments:output:]
- +[TRICCommandRunner _withoutLoggingRunCommand:withArgs:output:error:]
- +[TRICCommandRunner convertToTrialToolArgs:]
- +[TRICCommandRunner convertToTrialToolCommand:]
- +[TRICCommandRunner runCommand:withArgs:]
- +[TRICCommandRunner runCommand:withArgs:output:error:]
- +[TRICCommandRunner runCommandAsTrialDaemonUserName:withArgs:output:error:]
- +[TRICCommandRunner runCommandAsync:withArgs:taskOutputOut:error:]
- +[TRICCommandRunner runWithRootPrivilegesDroppedDescription:block:]
- +[TRICCommandRunner setUseTrialTool:]
- +[TRICCommandRunner useTrialTool]
- +[TRICEnvironmentManager checkDeviceUnlocked]
- +[TRICEnvironmentManager checkIfConnectedToVPN:]
- +[TRICEnvironmentManager currentEnv]
- +[TRICEnvironmentManager envToString:]
- +[TRICEnvironmentManager getLoginPasswd]
- +[TRICEnvironmentManager resetDaemonProcess]
- +[TRICEnvironmentManager trialDaemonUserName]
- +[TRICEnvironmentManager validateTrialPath:requireUserPath:]
- +[TRICPrinter _printAndLogString:error:]
- +[TRICPrinter _repeatString:length:]
- +[TRICPrinter printAndLogDefaultWithFormat:]
- +[TRICPrinter printAndLogErrorWithFormat:]
- +[TRICPrinter printNewlineAndLogDefaultWithFormat:]
- +[TRICPrinter printNewlineAndLogErrorWithFormat:]
- +[TRICPrinter printNewlineUsingStderr:format:]
- +[TRICPrinter printTabularWithLogDefaultForLines:]
- +[TRIClient printCurrentSettings]
- GCC_except_table121
- GCC_except_table24
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSPipe
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_CLASS_$_NSTask
- _OBJC_CLASS_$_TRICCommandRunner
- _OBJC_CLASS_$_TRICEnvironmentManager
- _OBJC_CLASS_$_TRICPrinter
- _OBJC_METACLASS_$_TRICCommandRunner
- _OBJC_METACLASS_$_TRICEnvironmentManager
- _OBJC_METACLASS_$_TRICPrinter
- __50+[TRICPrinter printTabularWithLogDefaultForLines:]_block_invoke.13
- __OBJC_$_CLASS_METHODS_TRICCommandRunner
- __OBJC_$_CLASS_METHODS_TRICEnvironmentManager
- __OBJC_$_CLASS_METHODS_TRICPrinter
- __OBJC_$_CLASS_PROP_LIST_TRICCommandRunner
- __OBJC_CLASS_RO_$_TRICCommandRunner
- __OBJC_CLASS_RO_$_TRICEnvironmentManager
- __OBJC_CLASS_RO_$_TRICPrinter
- __OBJC_METACLASS_RO_$_TRICCommandRunner
- __OBJC_METACLASS_RO_$_TRICEnvironmentManager
- __OBJC_METACLASS_RO_$_TRICPrinter
- ___50+[TRICPrinter printTabularWithLogDefaultForLines:]_block_invoke
- ___50+[TRICPrinter printTabularWithLogDefaultForLines:]_block_invoke_2
- ___61+[TRICCommandRunner _withLoggingRunCommand:arguments:output:]_block_invoke
- ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_56_e8_32s40s_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_56_e8_32s_e24_v32?0"NSArray"8Q16^B24l
- ___stderrp
- __block_literal_global.175
- __useTrialTool
- _fprintf
- _fwrite
- _geteuid
- _getlogin
- _getpwnam
- _objc_msgSend$_printAndLogString:error:
- _objc_msgSend$_repeatString:length:
- _objc_msgSend$_withLoggingRunCommand:arguments:output:
- _objc_msgSend$_withoutLoggingRunCommand:withArgs:output:error:
- _objc_msgSend$appendString:
- _objc_msgSend$currentEnv
- _objc_msgSend$envToString:
- _objc_msgSend$environment
- _objc_msgSend$fileHandleForReading
- _objc_msgSend$fileHandleWithStandardError
- _objc_msgSend$fileHandleWithStandardOutput
- _objc_msgSend$firstMatchInString:options:range:
- _objc_msgSend$getLoginPasswd
- _objc_msgSend$initWithUnsignedInteger:
- _objc_msgSend$isClassCLocked
- _objc_msgSend$launchAndReturnError:
- _objc_msgSend$pipe
- _objc_msgSend$populationType
- _objc_msgSend$printCurrentSettings
- _objc_msgSend$printNewlineAndLogDefaultWithFormat:
- _objc_msgSend$printNewlineAndLogErrorWithFormat:
- _objc_msgSend$printNewlineUsingStderr:format:
- _objc_msgSend$rangeOfString:
- _objc_msgSend$readDataToEndOfFile
- _objc_msgSend$regularExpressionWithPattern:options:error:
- _objc_msgSend$removeLastObject
- _objc_msgSend$runCommand:withArgs:
- _objc_msgSend$runCommand:withArgs:output:error:
- _objc_msgSend$runCommandAsync:withArgs:taskOutputOut:error:
- _objc_msgSend$setArguments:
- _objc_msgSend$setEnvironment:
- _objc_msgSend$setExecutableURL:
- _objc_msgSend$setObject:atIndexedSubscript:
- _objc_msgSend$setStandardError:
- _objc_msgSend$setStandardOutput:
- _objc_msgSend$terminationStatus
- _objc_msgSend$trialDaemonUserName
- _objc_msgSend$waitUntilExit
- _objc_msgSend$writeData:
- _seteuid
CStrings:
+ "TrialXP-424"
+ "[self initWithPaths:paths factorsState:factorsState activeFactorProvidersParser:nil]"
+ "factorPacksExperimentsDisableOld"
- " "
- " %!@(MISSING)%!@(MISSING) "
- " Unable to unload the daemon."
- "\"%!@(MISSING)\""
- "%!@(MISSING)\n"
- "(unknown: %!i(MISSING))"
- "+[TRICEnvironmentManager trialDaemonUserName]"
- "+[TRICPrinter printTabularWithLogDefaultForLines:]"
- "-f"
- "-q"
- "-v"
- ".*enabled.*"
- "/System/Library/LaunchAgents/com.apple.triald.plist"
- "/System/Library/LaunchDaemons/com.apple.triald.system.plist"
- "/bin/launchctl"
- "/sbin/ifconfig"
- "/usr/bin/csrutil"
- "/usr/bin/login"
- "/usr/local/bin/dvdo"
- "BETA_PROGRAM"
- "DEV"
- "Error running csrutil command: status = %!d(MISSING), error = %!@(MISSING)"
- "Error: Device has not been unlocked since reboot, please unlock to use trialcontroller\n"
- "GENERAL_PUBLIC"
- "INTERNAL"
- "LIMITED_CARRY"
- "ORGANIZATION"
- "OS_ACTIVITY_DT_MODE"
- "POPULATION_UNKNOWN"
- "PROD"
- "SQLITE"
- "Spawned subprocess: \"%!@(MISSING)\" [%!@(MISSING)]"
- "Subprocess \"%!@(MISSING)\" failed with status %!d(MISSING); error: %!@(MISSING)"
- "Subprocess \"%!@(MISSING)\" output: %!@(MISSING)"
- "TESTING"
- "TRICCommandRunner.m"
- "TRICEnvironmentManager.m"
- "TRICPrinter.m"
- "Tabular data has mismatched column counts"
- "TrialXP-426"
- "UAT"
- "UNKNOWN"
- "USER"
- "Unable to retrieve username"
- "VPN: Corporate"
- "Warning: Unable to get process environment variable \"USER\"\n"
- "Warning: failed to get pwInfo: %!s(MISSING) (%!d(MISSING))\n"
- "Warning: failed to seteuid() back to root: %!s(MISSING) (%!d(MISSING))\n"
- "Warning: failed to seteuid() to account \"%!s(MISSING)\": %!s(MISSING) (%!d(MISSING))\n"
- "Warning: got pwInfo for uid=0.\n"
- "XCTestConfigurationFilePath"
- "`csrutil` output indicates that SIP is enabled."
- "arguments"
- "check-new"
- "command"
- "deregister-namespace"
- "download-asset"
- "enroll-treatment"
- "exp fetch"
- "exp list-active"
- "exp list-notifications"
- "exp retarget"
- "exp rollback"
- "exp target"
- "flush-logs"
- "list-experiments"
- "list-logs"
- "list-namespace"
- "list-notification"
- "list-tasks"
- "make-default"
- "namespace deregister"
- "namespace list"
- "namespace register"
- "namespace update-on-demand"
- "register-namespace"
- "remove-asset"
- "retarget-experiments"
- "rollback-experiment"
- "rollout enroll"
- "run-fetch-activity"
- "run-on-demand-update"
- "stop"
- "target-experiment"
- "tasks list"
- "telemetry flush"
- "telemetry list"
- "trialcontroller was invoked as root; temporarily switched to account \"%!s(MISSING)\" to carry out operation \"%!s(MISSING)\".\n"
- "trialtool"
- "trt download-on-demand"
- "trt enroll"
- "trt remove-on-demand"
- "unload"
- "v32@?0@\"NSArray\"8Q16^B24"
- "|"

```
