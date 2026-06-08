## UARPAssetManager

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/UARPAssetManager`

```diff

-1345.120.5.0.0
-  __TEXT.__text: 0x4514
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0x724
+1576.0.0.0.0
+  __TEXT.__text: 0x4420
+  __TEXT.__objc_methlist: 0x74c
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x5bb
-  __TEXT.__gcc_except_tab: 0x18c
+  __TEXT.__cstring: 0x5c9
+  __TEXT.__gcc_except_tab: 0x1d4
   __TEXT.__oslogstring: 0xc8
-  __TEXT.__unwind_info: 0x240
-  __TEXT.__objc_classname: 0x11b
-  __TEXT.__objc_methname: 0xe72
-  __TEXT.__objc_methtype: 0x35c
-  __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a0
+  __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__cfstring: 0x5c0
   __AUTH_CONST.__objc_const: 0xe40
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x1e0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F0806231-4A94-38E7-B29A-B50F617652B4
-  Functions: 135
-  Symbols:   586
-  CStrings:  351
+  UUID: E6589480-6858-3149-ACF4-7FABC85065E4
+  Functions: 137
+  Symbols:   597
+  CStrings:  112
 
Symbols:
+ -[UARPAssetManagerClient groupPersonality:peerPersonality:]
+ -[UARPEndpointPersonality addPersonality:]
+ -[UARPEndpointPersonalityMobileAsset addPersonality:]
+ GCC_except_table14
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table23
+ GCC_except_table25
+ GCC_except_table27
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addPersonality:
+ _objc_msgSend$mutableCopy
+ _objc_opt_new
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table15
- GCC_except_table19
- GCC_except_table22
- GCC_except_table24
- GCC_except_table26
- _OUTLINED_FUNCTION_3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x1
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSError\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"UARPAssetVersionBase\""
- "@\"UARPEndpointPersonality\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@44@0:8@16@24@32B40"
- "@48@0:8@16@24@32@40"
- "@72@0:8@16@24@32@40@48B56B60@64"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",R,V_partnerSerialNumbers"
- "T@\"NSArray\",R,V_serialNumbers"
- "T@\"NSDate\",R,V_creationDate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_appleModelNumber"
- "T@\"NSString\",R,C,V_assetVersion"
- "T@\"NSString\",R,C,V_domain"
- "T@\"NSString\",R,C,V_filePath"
- "T@\"NSString\",R,C,V_hwFusing"
- "T@\"NSString\",R,C,V_restoreVersion"
- "T@\"NSString\",R,V_activeVersion"
- "T@\"NSString\",R,V_assetVersion"
- "T@\"NSString\",R,V_buildVersion"
- "T@\"NSString\",R,V_domain"
- "T@\"NSString\",R,V_friendlyName"
- "T@\"NSString\",R,V_hwFusing"
- "T@\"NSString\",R,V_hwRevision"
- "T@\"NSString\",R,V_identifier"
- "T@\"NSString\",R,V_mobileAssetAppleModelNumber"
- "T@\"NSString\",R,V_osVersion"
- "T@\"NSString\",R,V_restoreVersion"
- "T@\"NSString\",R,V_serialNumber"
- "T@\"NSXPCConnection\",R"
- "T@\"UARPAssetVersionBase\",R,V_assetVersion"
- "T@\"UARPEndpointPersonality\",R,V_personality"
- "TB,R"
- "TB,R,V_internalAsset"
- "TB,R,V_internalVariant"
- "TB,R,V_internalVersion"
- "TB,R,V_softwareUpdateAsset"
- "TB,R,V_usePallas"
- "TQ,R"
- "Tq,R,V_status"
- "UARPAssetAvailableEvent"
- "UARPAssetManagerCacheConfiguration"
- "UARPAssetManagerClient"
- "UARPAssetVersionBase"
- "UARPAssetVersionSoftwareUpdate"
- "UARPAsyncAssetManagerXPCProvider"
- "UARPEndpointPersonality"
- "UARPEndpointPersonalityMobileAsset"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activeVersion"
- "_appleModelNumber"
- "_assetVersion"
- "_buildVersion"
- "_creationDate"
- "_domain"
- "_filePath"
- "_friendlyName"
- "_hwFusing"
- "_hwRevision"
- "_identifier"
- "_internalAsset"
- "_internalVariant"
- "_internalVersion"
- "_isEqualInternal:"
- "_lastProviderError"
- "_mobileAssetAppleModelNumber"
- "_osVersion"
- "_partnerSerialNumbers"
- "_personality"
- "_providerErrorReply"
- "_restoreVersion"
- "_serialNumber"
- "_serialNumbers"
- "_softwareUpdateAsset"
- "_status"
- "_usePallas"
- "_xpcConnection"
- "_xpcLog"
- "addObject:"
- "appendFormat:"
- "appendString:"
- "array"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "autorelease"
- "checkAssetAvailabilityForDomain:"
- "class"
- "clearAssetCacheForDomain:"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "creationDate"
- "dataWithBytes:length:"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "getAssetURLForPersonality:"
- "getAssetURLForPersonality:reply:"
- "getSandboxExtensionTokenForAssetURL:"
- "getSandboxExtensionTokenForAssetURL:reply:"
- "getSupplementalAssetURLForPersonality:supplementalAsset:"
- "getSupplementalAssetURLForPersonality:supplementalAsset:reply:"
- "hash"
- "includesPersonality:"
- "init"
- "initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:internalVersion:restoreVersion:"
- "initWithAppleModelNumber:serialNumber:hwFusing:domain:"
- "initWithAssetVersion:"
- "initWithCoder:"
- "initWithIdentifier:domain:"
- "initWithMachServiceName:options:"
- "initWithRestoreVersion:osVersion:buildVersion:internalAsset:"
- "initWithXPCObject:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPersonalityMatch:"
- "isProxy"
- "length"
- "lowercaseString"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "primeCache:"
- "q"
- "q16@0:8"
- "release"
- "releaseXPCConnection"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setActiveVersion:"
- "setFriendlyName:"
- "setHwFusingType:"
- "setHwRevision:"
- "setInternalVariant:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMobileAssetAppleModelNumber:"
- "setPartnerSerialNumbers:"
- "setRemoteObjectInterface:"
- "setSoftwareUpdateAsset:"
- "setWithArray:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subscribeForPersonality:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unarchivedObjectOfClass:fromData:error:"
- "updateReachabilityForPersonality:reachable:"
- "updateSettingsForPersonality:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"UARPAssetManagerCacheConfiguration\"16"
- "v24@0:8@\"UARPEndpointPersonality\"16"
- "v24@0:8@16"
- "v28@0:8@\"UARPEndpointPersonality\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"UARPEndpointPersonality\"16@?<v@?@\"NSURL\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"UARPEndpointPersonality\"16@\"NSString\"24@?<v@?@\"NSURL\">32"
- "v40@0:8@16@24@?32"
- "xpcConnection"
- "zone"

```
