## CoreRepairKit

> `/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0x1bdc
-  __TEXT.__auth_stubs: 0x280
+1291.0.0.502.1
+  __TEXT.__text: 0x1934
   __TEXT.__objc_methlist: 0x28c
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x186
   __TEXT.__oslogstring: 0x2df
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0xa8
-  __TEXT.__objc_methname: 0x7f6
-  __TEXT.__objc_methtype: 0x26b
-  __TEXT.__objc_stubs: 0x5e0
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x290
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x4f8
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH.__objc_data: 0x190
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 8710AA3E-4FA7-31D8-B4FA-102C54FA2C6C
-  Functions: 42
-  Symbols:   249
-  CStrings:  191
+  UUID: F1E0D464-EDA8-39D6-AF0C-8EF6C44D83A9
+  Functions: 40
+  Symbols:   83
+  CStrings:  62
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x8
- +[CRRepairStatus _wasRepairedWithSysCfg:]
- +[CRRepairStatus _wasRepairedWithSysCfg:].cold.1
- +[CRRepairStatus _wasRepairedWithSysCfg:].cold.2
- +[CRRepairStatus _wasRepairedWithSysCfg:].cold.3
- +[CRRepairStatus _wasRepairedWithSysCfg:].cold.4
- +[CRRepairStatus getVeridianFWVersionInfo]
- +[CRRepairStatus getVeridianFWVersionInfo].cold.1
- +[CRRepairStatus isCoverGlassRepaired]
- +[CRRepairStatus isDeviceStagedSealed]
- +[CRRepairStatus isServicePartWithError:]
- +[CRRepairStatus isVeridianFWUpdateRequiredLite]
- +[CRRepairStatus isVeridianFWUpdateRequired]
- +[CRRepairStatus isVolumeButtonRepaired]
- +[CRURLSessionDelegate trustIsValidWithProtectionSpace:]
- +[CRURLSessionDelegate trustIsValidWithProtectionSpace:].cold.1
- +[CRURLSessionDelegate trustIsValidWithProtectionSpace:].cold.2
- +[CRURLSessionDelegate trustIsValidWithProtectionSpace:].cold.3
- +[CRURLSessionDelegate trustIsValidWithProtectionSpace:].cold.4
- +[MRDataCollectionNotice didShowDataCollectionNoticeForComponent:]
- +[MRDataCollectionNotice shouldShowDataCollectionNoticeForComponent:]
- -[CRPluginsController isApplicationInstalledWithMaxRetries:bundleName:]
- -[CRPluginsController isApplicationInstalledWithMaxRetries:bundleName:].cold.1
- -[CRPluginsController rebuildApplicationDataBase]
- -[CRPluginsController rebuildApplicationDataBase].cold.1
- -[CRSystemHealthStatus getCurrentSystemHealthStatusForComponents:WithReply:]
- -[CRURLSessionDelegate URLSession:didReceiveChallenge:completionHandler:]
- -[CRURLSessionDelegate URLSession:didReceiveChallenge:completionHandler:].cold.1
- -[MRLocalization locKeyWithFormat:component:]
- -[MRLocalization locKeyWithFormat:component:].cold.1
- -[MRLocalization locKeyWithFormat:component:].cold.2
- -[MRLocalization localizedStringWithFormat:component:]
- -[MRLocalization localizedStringWithKey:defaultString:]
- <redacted>
- GCC_except_table0
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- __OBJC_$_CLASS_METHODS_CRRepairStatus
- __OBJC_$_CLASS_METHODS_CRURLSessionDelegate
- __OBJC_$_CLASS_METHODS_MRDataCollectionNotice
- __OBJC_$_INSTANCE_METHODS_CRPluginsController
- __OBJC_$_INSTANCE_METHODS_CRSystemHealthStatus
- __OBJC_$_INSTANCE_METHODS_CRURLSessionDelegate
- __OBJC_$_INSTANCE_METHODS_MRLocalization
- __OBJC_$_PROP_LIST_CRURLSessionDelegate
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSystemHealthProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CRSystemHealthProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDelegate
- __OBJC_$_PROTOCOL_REFS_NSURLSessionDelegate
- __OBJC_CLASS_PROTOCOLS_$_CRURLSessionDelegate
- __OBJC_CLASS_RO_$_CRPluginsController
- __OBJC_CLASS_RO_$_CRRepairStatus
- __OBJC_CLASS_RO_$_CRSystemHealthStatus
- __OBJC_CLASS_RO_$_CRURLSessionDelegate
- __OBJC_CLASS_RO_$_MRDataCollectionNotice
- __OBJC_CLASS_RO_$_MRLocalization
- __OBJC_LABEL_PROTOCOL_$_CRSystemHealthProtocol
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_LABEL_PROTOCOL_$_NSURLSessionDelegate
- __OBJC_METACLASS_RO_$_CRPluginsController
- __OBJC_METACLASS_RO_$_CRRepairStatus
- __OBJC_METACLASS_RO_$_CRSystemHealthStatus
- __OBJC_METACLASS_RO_$_CRURLSessionDelegate
- __OBJC_METACLASS_RO_$_MRDataCollectionNotice
- __OBJC_METACLASS_RO_$_MRLocalization
- __OBJC_PROTOCOL_$_CRSystemHealthProtocol
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_$_NSURLSessionDelegate
- __OBJC_PROTOCOL_REFERENCE_$_CRSystemHealthProtocol
- ___76-[CRSystemHealthStatus getCurrentSystemHealthStatusForComponents:WithReply:]_block_invoke
- ___76-[CRSystemHealthStatus getCurrentSystemHealthStatusForComponents:WithReply:]_block_invoke.11
- ___76-[CRSystemHealthStatus getCurrentSystemHealthStatusForComponents:WithReply:]_block_invoke.cold.1
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
- ___block_descriptor_64_e8_32r40r48r56r_e37_v28?0B8"NSDictionary"12"NSError"20lr32l8r40l8r48l8r56l8
- _objc_msgSend$JSONObjectWithData:options:error:
- _objc_msgSend$SHA256DigestString
- _objc_msgSend$_LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:
- _objc_msgSend$applicationIsInstalled:
- _objc_msgSend$boolForKey:
- _objc_msgSend$bundleWithPath:
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$count
- _objc_msgSend$credentialForTrust:
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$getCurrentSystemHealthStatusForComponentsInternal:WithReply:
- _objc_msgSend$getLocalizationKey:
- _objc_msgSend$groupUserDefaultsWithSuiteName:
- _objc_msgSend$host
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$invalidate
- _objc_msgSend$isDcSignedComponent:error:
- _objc_msgSend$isDeviceStagedSealed
- _objc_msgSend$isEqual:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$isServicePartWithError:
- _objc_msgSend$isVeridianFWUpdateRequired
- _objc_msgSend$isVeridianFWUpdateRequiredLite
- _objc_msgSend$length
- _objc_msgSend$locKeyWithFormat:component:
- _objc_msgSend$localizations
- _objc_msgSend$localizedStringForKey:value:table:localization:
- _objc_msgSend$localizedStringWithKey:defaultString:
- _objc_msgSend$numberWithBool:
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$preferredLanguages
- _objc_msgSend$preferredLocalizationsFromArray:forPreferences:
- _objc_msgSend$protectionSpace
- _objc_msgSend$resume
- _objc_msgSend$serverTrust
- _objc_msgSend$setBool:forKey:
- _objc_msgSend$setObject:forKeyedSubscript:
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$stringByStrippingPrefix:
- _objc_msgSend$stringWithFormat:
- _objc_msgSend$synchronize
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_msgSend$trustIsValidWithProtectionSpace:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
CStrings:
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B28@0:8i16@20"
- "B32@0:8Q16@?24"
- "CRPluginsController"
- "CRRepairStatus"
- "CRSystemHealthProtocol"
- "CRSystemHealthStatus"
- "CRURLSessionDelegate"
- "JSONObjectWithData:options:error:"
- "MRDataCollectionNotice"
- "MRLocalization"
- "NSObject"
- "NSURLSessionDelegate"
- "Q16@0:8"
- "SHA256DigestString"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:"
- "_wasRepairedWithSysCfg:"
- "applicationIsInstalled:"
- "autorelease"
- "boolForKey:"
- "bundleWithPath:"
- "class"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "count"
- "credentialForTrust:"
- "dataWithBytes:length:"
- "debugDescription"
- "defaultWorkspace"
- "description"
- "deviceHasReducedBootPolicyWithReply:"
- "didShowDataCollectionNoticeForComponent:"
- "getCurrentSystemHealthStatusForComponents:WithReply:"
- "getCurrentSystemHealthStatusForComponentsInternal:WithReply:"
- "getLocalizationKey:"
- "getVeridianFWVersionInfo"
- "groupUserDefaultsWithSuiteName:"
- "hash"
- "host"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isApplicationInstalledWithMaxRetries:bundleName:"
- "isBatteryInServiceState:"
- "isCoverGlassRepaired"
- "isDcSignedComponent:error:"
- "isDeviceStagedSealed"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isServicePartWithError:"
- "isVeridianFWUpdateRequired"
- "isVeridianFWUpdateRequiredLite"
- "isVolumeButtonRepaired"
- "length"
- "locKeyWithFormat:component:"
- "localizations"
- "localizedStringForKey:value:table:localization:"
- "localizedStringWithFormat:component:"
- "localizedStringWithKey:defaultString:"
- "numberWithBool:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postComponentStatusEventFor:status:withReply:"
- "preferredLanguages"
- "preferredLocalizationsFromArray:forPreferences:"
- "protectionSpace"
- "rebuildApplicationDataBase"
- "release"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverTrust"
- "setBool:forKey:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "shouldShowDataCollectionNoticeForComponent:"
- "stringByStrippingPrefix:"
- "stringWithFormat:"
- "superclass"
- "synchronize"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "trustIsValidWithProtectionSpace:"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?B@\"NSDictionary\"@\"NSError\">24"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8Q16Q24@?32"
- "v40@0:8Q16Q24@?<v@?B@\"NSError\">32"
- "zone"

```
