## CrashReporterSupport

> `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport`

```diff

 15131.0.0.0.0
-  __TEXT.__text: 0xd4d8
+  __TEXT.__text: 0xd40c
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x94
+  __TEXT.__objc_methlist: 0xc4
   __TEXT.__const: 0xfe
-  __TEXT.__gcc_except_tab: 0x138
+  __TEXT.__gcc_except_tab: 0x144
   __TEXT.__cstring: 0x14d2
   __TEXT.__oslogstring: 0x1dcc
-  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__objc_classname: 0x29
   __TEXT.__objc_methname: 0x60a
   __TEXT.__objc_methtype: 0xdf

   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x290
   __AUTH_CONST.__cfstring: 0x1de0
-  __AUTH_CONST.__objc_const: 0x160
+  __AUTH_CONST.__objc_const: 0x110
   __AUTH.__objc_data: 0x50
   __DATA.__data: 0x118
   __DATA.__bss: 0x1e0

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 68712F82-E469-3B6A-A63B-CFF119BC8F2A
-  Functions: 238
-  Symbols:   762
+  UUID: 9EAC7CF0-328E-3CE3-A713-970832581040
+  Functions: 245
+  Symbols:   793
   CStrings:  761
 
Symbols:
+ +[OSALogWriter sharedObject].cold.1
+ CRCanSubmitLog.cold.1
+ CRGetUserUUID.cold.1
+ CRIsAutoSubmitEnabled.cold.1
+ CRIsThirdPartyApplicationDataSubmissionEnabled.cold.1
+ MTSanitizerCleanComponents.cold.1
+ MTSanitizerCleanComponents.cold.2
+ _CRAutoSubmitEnabledIsSet.cold.1
+ _CRGetAnonHostUUID.cold.1
+ _CRSetIsAutoSubmitEnabled.cold.1
+ _CRSetIsThirdPartyApplicationDataSubmissionEnabled.cold.1
+ _CRThirdPartyApplicationDataSubmissionEnabledIsSet.cold.1
+ _MTSanitizerGetLocalHomeDirectories.cold.1
+ _MTSanitizerGetLocalVolumes.cold.1
+ _MTSanitizerGetRulesForDomain.cold.1
+ __CRIsThirdPartyApplicationDataSubmissionEnabled_block_invoke.cold.1
+ ___CRAutoSubmitEnabledIsSet_block_invoke.cold.2
+ ___CRSetIsAutoSubmitEnabled_block_invoke.cold.10
+ ___CRSetIsAutoSubmitEnabled_block_invoke.cold.6
+ ___CRSetIsAutoSubmitEnabled_block_invoke.cold.7
+ ___CRSetIsAutoSubmitEnabled_block_invoke.cold.8
+ ___CRSetIsAutoSubmitEnabled_block_invoke.cold.9
+ ___CRSetIsThirdPartyApplicationDataSubmissionEnabled_block_invoke.cold.4
+ ___CRSetIsThirdPartyApplicationDataSubmissionEnabled_block_invoke.cold.5
+ ___CRSetIsThirdPartyApplicationDataSubmissionEnabled_block_invoke.cold.6
+ ___CRThirdPartyApplicationDataSubmissionEnabledIsSet_block_invoke.cold.2
+ ___createAutoSubmitSettingObject_block_invoke.cold.3
+ ___createAutoSubmitSettingObject_block_invoke.cold.4
+ _createAutoSubmitSettingObject.cold.1
+ _createAutoSubmitSettingObject.cold.2
+ _createAutoSubmitSettingObject.cold.3
+ _migrateLegacyAutoSubmitEnabledSetting.cold.2
+ _setPreference.cold.3
+ _setPreference.cold.4
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8

```
