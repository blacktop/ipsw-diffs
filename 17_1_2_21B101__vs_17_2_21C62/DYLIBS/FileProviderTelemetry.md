## FileProviderTelemetry

> `/System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry`

```diff

-1703.42.2.0.0
-  __TEXT.__text: 0x1674
+1703.62.4.0.0
+  __TEXT.__text: 0x19d0
   __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x100
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__cstring: 0x1b8
-  __TEXT.__oslogstring: 0x8f
-  __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x38
-  __TEXT.__objc_methname: 0x561
-  __TEXT.__objc_methtype: 0x171
+  __TEXT.__objc_methlist: 0x108
+  __TEXT.__const: 0x10
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__cstring: 0x10c
+  __TEXT.__oslogstring: 0xc4
+  __TEXT.__unwind_info: 0xd4
+  __TEXT.__objc_classname: 0x37
+  __TEXT.__objc_methname: 0x5c1
+  __TEXT.__objc_methtype: 0x188
   __TEXT.__objc_stubs: 0x4a0
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x178
+  __DATA_CONST.__objc_const: 0x150
   __DATA_CONST.__objc_selrefs: 0x170
-  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__auth_got: 0x1f0
-  __DATA.__objc_classrefs: 0x48
+  __DATA.__objc_classrefs: 0x40
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_ivar: 0x1c
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 34
-  Symbols:   232
-  CStrings:  106
+  Functions: 36
+  Symbols:   231
+  CStrings:  99
 
Symbols:
+ +[FPRTCReportingSessionManager sessionInfo]
+ -[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]
+ GCC_except_table23
+ GCC_except_table9
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_CLASS_PROP_LIST_FPRTCReportingSessionManager
+ ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke
+ ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.10
+ ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.11
+ ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.11.cold.1
+ ___block_descriptor_80_e8_32s40s48s56s64r_e17_v16?0"NSArray"8ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.21
+ _objc_enumerationMutation
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$initWithSessionInfo:userInfo:frameworksToCheck:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$sendMessageWithCategory:type:payload:error:
+ _objc_msgSend$sessionInfo
+ _objc_msgSend$startConfigurationWithCompletionHandler:
+ _objc_msgSend$unsignedIntValue
+ _objc_retain_x1
+ _objc_retain_x9
- -[FPRTCReportingSessionManager sessionForProvider:version:]
- GCC_except_table14
- GCC_except_table17
- _FileProviderDaemonLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_NSAssertionHandler
- _OBJC_IVAR_$_FPRTCReportingSession._trialExperiment
- _OBJC_IVAR_$_FPRTCReportingSession._trialTreatment
- ___FileProviderDaemonLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_literal_global.17
- ___getFPDConfigurationStoreClass_block_invoke
- ___getFPDConfigurationStoreClass_block_invoke.cold.1
- ___getFPDConfigurationStoreClass_block_invoke.cold.2
- __sl_dlopen
- _audit_stringFileProviderDaemon
- _free
- _getFPDConfigurationStoreClass.softClass
- _objc_getClass
- _objc_msgSend$currentHandler
- _objc_msgSend$defaultStore
- _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
- _objc_msgSend$identifier
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$trialExperiment
- _objc_msgSend$trialTreatment
CStrings:
+ "\x05"
+ "T@\"NSDictionary\",R,N"
+ "[ERROR] FPRTCReporting: flushsing session failed: %@"
+ "countByEnumeratingWithState:objects:count:"
+ "initWithSessionInfo:userInfo:frameworksToCheck:"
+ "objectForKeyedSubscript:"
+ "postMultipleReports:type:userinfo:session:observer:"
+ "sendMessageWithCategory:type:payload:error:"
+ "sessionInfo"
+ "startConfigurationWithCompletionHandler:"
+ "unsignedIntValue"
+ "v16@?0@\"NSArray\"8"
+ "v56@0:8@16Q24@32@40@48"
- "\a"
- "%s"
- "Class getFPDConfigurationStoreClass(void)_block_invoke"
- "FPDConfigurationStore"
- "FPRTCReporting.m"
- "Unable to find class %s"
- "_trialExperiment"
- "_trialTreatment"
- "currentHandler"
- "defaultStore"
- "handleFailureInFunction:file:lineNumber:description:"
- "identifier"
- "sessionForProvider:version:"
- "softlink:r:path:/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon"
- "stringWithUTF8String:"
- "trialExperiment"
- "trialTreatment"
- "void *FileProviderDaemonLibrary(void)"

```
