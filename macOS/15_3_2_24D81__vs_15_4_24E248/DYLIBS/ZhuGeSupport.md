## ZhuGeSupport

> `/System/Library/PrivateFrameworks/ZhuGeSupport.framework/Versions/A/ZhuGeSupport`

```diff

-331.80.3.0.0
-  __TEXT.__text: 0xc020
+340.100.16.0.0
+  __TEXT.__text: 0xba30
   __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x39c
+  __TEXT.__objc_methlist: 0x458
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x474
-  __TEXT.__cstring: 0x47e0
+  __TEXT.__gcc_except_tab: 0x400
+  __TEXT.__cstring: 0x4783
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x228
+  __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0xbf
   __TEXT.__objc_methname: 0xf43
   __TEXT.__objc_methtype: 0x2df
-  __TEXT.__objc_stubs: 0x1220
+  __TEXT.__objc_stubs: 0x11e0
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x30

   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x3560
-  __AUTH_CONST.__objc_const: 0x858
+  __AUTH_CONST.__cfstring: 0x3500
+  __AUTH_CONST.__objc_const: 0x708
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4C42E3B-A96B-3C23-A3F5-FD2F339903F5
-  Functions: 161
-  Symbols:   591
-  CStrings:  1161
+  UUID: 3F6EE7F0-B9FF-385B-92D1-C91B68991D47
+  Functions: 181
+  Symbols:   617
+  CStrings:  1155
 
Symbols:
+ +[ZhuGeInternalSupportAssistant recursiveMutex].cold.1
+ +[ZhuGeSingleton sharedInstance].cold.1
+ +[ZhuGeSupportAssistant getDylibHandlerWithError:].cold.1
+ +[ZhuGeSupportAssistant getXpcProxyWithError:].cold.1
+ GCC_except_table21
+ ZhuGeBulkCopyPrivileges.cold.1
+ ZhuGeBulkCopyValues.cold.1
+ ZhuGeCopyPrivilege.cold.1
+ ZhuGeCopyValue.cold.1
+ ZhuGeIsKeyValid.cold.1
+ ZhuGeLog.cold.1
+ ZhuGeLog.cold.2
+ ZhuGeLog.cold.3
+ ZhuGeLog.cold.4
+ ZhuGeLog.cold.5
+ ZhuGePrintStderr.cold.1
+ ZhuGePrintStderr.cold.2
+ ZhuGeSetLogHandler.cold.1
+ __ZhuGeBulkCopyValues_block_invoke.210
+ __ZhuGeBulkCopyValues_block_invoke_2.211
+ __ZhuGeCopyValue_block_invoke.91
+ __block_literal_global.234
+ __block_literal_global.255
+ armoryInstanceForKey.cold.1
+ doesZhuGeDeemRestoreOSAsInternal.cold.1
+ doesZhuGeRecordMobileGestaltQuery.cold.1
+ domainForKey.cold.1
+ hasZhuGeLogConditionalPrint.cold.1
+ hasZhuGeLogPrefixFileFuncLine.cold.1
+ hasZhuGeLogPrefixPidTid.cold.1
+ isZhuGeInFactoryBuild.cold.1
+ isZhuGeInInternalBuild.cold.1
+ isZhuGeInRestoreOS.cold.1
+ isZhuGeStdoutRedirected.cold.1
+ islibtraceSimulatingCustomerBuild.cold.1
+ printCallerRestoreLog.cold.1
- GCC_except_table22
- __ZhuGeBulkCopyValues_block_invoke.215
- __ZhuGeBulkCopyValues_block_invoke_2.220
- __ZhuGeCopyValue_block_invoke.94
- ___ZhuGeBulkCopyValues_block_invoke_3
- ___ZhuGeCopyValue_block_invoke_4
- __block_literal_global.243
- __block_literal_global.264
- _objc_msgSend$setBulkMGKeys:getValuesAndError:
- _objc_msgSend$setMGKey:getValueAndError:
CStrings:
+ "\"%@\" is not a ZhuGe key nor a MobileGestalt key!"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/NSArray+ZhuGe.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/NSNumber+ZhuGe.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/ZhuGeCache.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/ZhuGeLog.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/ZhuGeUtils.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeInternalSupport/ZhuGeInternalSupportAssistant.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeSupport/ZhuGeSupport.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeSupport/ZhuGeSupportAssistant.m"
+ "In bulk query, \"%@\" is not a ZhuGe key nor a MobileGestalt key!"
+ "ZhuGe-340.100.16"
- "\"%@\" is not a ZhuGe key nor a MG key!"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/NSArray+ZhuGe.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/NSNumber+ZhuGe.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/ZhuGeCache.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/ZhuGeLog.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeCommon/ZhuGeUtils.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeInternalSupport/ZhuGeInternalSupportAssistant.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeSupport/ZhuGeSupport.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ZhuGe/ZhuGeSupport/ZhuGeSupportAssistant.m"
- "In bulk query, \"%@\" is not a ZhuGe key nor a MG key!"
- "In bulk query, failed to get the values from entrusted MG!"
- "Query key: \"%@\" from MG"
- "Query key: \"%@\" from entrusted MG"
- "ZhuGe-331.80.3"

```
