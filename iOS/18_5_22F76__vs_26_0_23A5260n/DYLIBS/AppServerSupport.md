## AppServerSupport

> `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport`

```diff

-2894.122.1.0.0
-  __TEXT.__text: 0x58d8
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x4bc
+3070.0.0.0.2
+  __TEXT.__text: 0x6e9c
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x96c
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x2d6
-  __TEXT.__oslogstring: 0xc8e
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__objc_classname: 0x8f
-  __TEXT.__objc_methname: 0xd87
-  __TEXT.__objc_methtype: 0x2b5
-  __TEXT.__objc_stubs: 0x600
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__cstring: 0x4e6
+  __TEXT.__oslogstring: 0xd82
+  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__objc_classname: 0xe7
+  __TEXT.__objc_methname: 0x18e1
+  __TEXT.__objc_methtype: 0x3b7
+  __TEXT.__objc_stubs: 0xa00
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x328
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__objc_selrefs: 0x608
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0xae0
-  __DATA.__objc_ivar: 0x94
-  __DATA.__crash_info: 0x40
-  __DATA_DIRTY.__objc_data: 0x230
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0x1568
+  __AUTH_CONST.__objc_intobj: 0x18
+  __DATA.__objc_ivar: 0xfc
+  __DATA.__data: 0xc0
+  __DATA.__crash_info: 0x148
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F41F583C-F36A-3F59-8A4D-7EAC96A363CC
-  Functions: 150
-  Symbols:   597
-  CStrings:  356
+  UUID: D3C9453A-EB64-32A4-9FBA-C2E6EEAC89A9
+  Functions: 223
+  Symbols:   854
+  CStrings:  578
 
Symbols:
+ +[OSLaunchdJob _handlesToJobs:]
+ +[OSLaunchdJob _handlesToJobs:].cold.1
+ +[OSLaunchdJob _handlesToJobs:].cold.2
+ +[OSLaunchdJob _submitExtension:overlay:domain:error:]
+ +[OSLaunchdJob _submitExtension:overlay:domain:error:].cold.1
+ +[OSLaunchdJob _submitExtension:overlay:domain:error:].cold.2
+ +[OSLaunchdJob copyJobsLoadedByCoalition:error:]
+ +[OSLaunchdJob submitExtensionAtURL:properties:domain:error:]
+ -[NSArray(AppServiceSupportAdditions) _OS_xpcObjectRepresentation]
+ -[NSData(AppServiceSupportAdditions) _OS_xpcObjectRepresentation]
+ -[NSDictionary(AppServiceSupportAdditions) _OS_xpcObjectRepresentation]
+ -[NSMutableDictionary(AppServiceSupportAdditions) _OS_overlayDictionary:]
+ -[NSNumber(AppServiceSupportAdditions) _OS_xpcObjectRepresentation]
+ -[NSString(AppServiceSupportAdditions) _OS_xpcObjectRepresentation]
+ -[NSUUID(AppServiceSupportAdditions) _OS_xpcObjectRepresentation]
+ -[OSLaunchdDomain description]
+ -[OSLaunchdJob copyJobsLoadedByJob:]
+ -[OSLaunchdJobProperties .cxx_destruct]
+ -[OSLaunchdJobProperties abandonCoalition]
+ -[OSLaunchdJobProperties additionalProperties]
+ -[OSLaunchdJobProperties additionalSubServices]
+ -[OSLaunchdJobProperties arguments]
+ -[OSLaunchdJobProperties debugDescription]
+ -[OSLaunchdJobProperties enterprisePersona]
+ -[OSLaunchdJobProperties environmentVariables]
+ -[OSLaunchdJobProperties init]
+ -[OSLaunchdJobProperties joinExistingSession]
+ -[OSLaunchdJobProperties lightweightCodeRequirement]
+ -[OSLaunchdJobProperties managedByServices]
+ -[OSLaunchdJobProperties managedEndpointLaunchIdentifiers]
+ -[OSLaunchdJobProperties omitSandboxParameters]
+ -[OSLaunchdJobProperties oneShotUUID]
+ -[OSLaunchdJobProperties overlay]
+ -[OSLaunchdJobProperties personaString]
+ -[OSLaunchdJobProperties platform]
+ -[OSLaunchdJobProperties processType]
+ -[OSLaunchdJobProperties programArguments]
+ -[OSLaunchdJobProperties roleAccount]
+ -[OSLaunchdJobProperties runLoopType]
+ -[OSLaunchdJobProperties sandboxContainer]
+ -[OSLaunchdJobProperties sandboxProfile]
+ -[OSLaunchdJobProperties serviceType]
+ -[OSLaunchdJobProperties setAbandonCoalition:]
+ -[OSLaunchdJobProperties setAdditionalProperties:]
+ -[OSLaunchdJobProperties setAdditionalSubServices:]
+ -[OSLaunchdJobProperties setArguments:]
+ -[OSLaunchdJobProperties setEnterprisePersona:]
+ -[OSLaunchdJobProperties setEnvironmentVariables:]
+ -[OSLaunchdJobProperties setJoinExistingSession:]
+ -[OSLaunchdJobProperties setLightweightCodeRequirement:]
+ -[OSLaunchdJobProperties setManagedByServices:]
+ -[OSLaunchdJobProperties setManagedEndpointLaunchIdentifiers:]
+ -[OSLaunchdJobProperties setOmitSandboxParameters:]
+ -[OSLaunchdJobProperties setOneShotUUID:]
+ -[OSLaunchdJobProperties setOverlay:]
+ -[OSLaunchdJobProperties setPersonaString:]
+ -[OSLaunchdJobProperties setPlatform:]
+ -[OSLaunchdJobProperties setProcessType:]
+ -[OSLaunchdJobProperties setProgramArguments:]
+ -[OSLaunchdJobProperties setRoleAccount:]
+ -[OSLaunchdJobProperties setRunLoopType:]
+ -[OSLaunchdJobProperties setSandboxContainer:]
+ -[OSLaunchdJobProperties setSandboxProfile:]
+ -[OSLaunchdJobProperties setServiceType:]
+ -[OSLaunchdJobProperties setSpawnConstraint:]
+ -[OSLaunchdJobProperties setUiApplicationClass:]
+ -[OSLaunchdJobProperties setUiApplicationDelegateClass:]
+ -[OSLaunchdJobProperties setWatchdogTimeout:]
+ -[OSLaunchdJobProperties spawnConstraint]
+ -[OSLaunchdJobProperties uiApplicationClass]
+ -[OSLaunchdJobProperties uiApplicationDelegateClass]
+ -[OSLaunchdJobProperties watchdogTimeout]
+ -[OSLaunchdJobProperties xpcOverlay]
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_OSLaunchdJobProperties
+ _OBJC_IVAR_$_OSLaunchdJobProperties._abandonCoalition
+ _OBJC_IVAR_$_OSLaunchdJobProperties._additionalProperties
+ _OBJC_IVAR_$_OSLaunchdJobProperties._additionalSubServices
+ _OBJC_IVAR_$_OSLaunchdJobProperties._arguments
+ _OBJC_IVAR_$_OSLaunchdJobProperties._enterprisePersona
+ _OBJC_IVAR_$_OSLaunchdJobProperties._environmentVariables
+ _OBJC_IVAR_$_OSLaunchdJobProperties._joinExistingSession
+ _OBJC_IVAR_$_OSLaunchdJobProperties._lightweightCodeRequirement
+ _OBJC_IVAR_$_OSLaunchdJobProperties._managedByServices
+ _OBJC_IVAR_$_OSLaunchdJobProperties._managedEndpointLaunchIdentifiers
+ _OBJC_IVAR_$_OSLaunchdJobProperties._omitSandboxParameters
+ _OBJC_IVAR_$_OSLaunchdJobProperties._oneShotUUID
+ _OBJC_IVAR_$_OSLaunchdJobProperties._overlay
+ _OBJC_IVAR_$_OSLaunchdJobProperties._personaString
+ _OBJC_IVAR_$_OSLaunchdJobProperties._platform
+ _OBJC_IVAR_$_OSLaunchdJobProperties._processType
+ _OBJC_IVAR_$_OSLaunchdJobProperties._programArguments
+ _OBJC_IVAR_$_OSLaunchdJobProperties._roleAccount
+ _OBJC_IVAR_$_OSLaunchdJobProperties._runLoopType
+ _OBJC_IVAR_$_OSLaunchdJobProperties._sandboxContainer
+ _OBJC_IVAR_$_OSLaunchdJobProperties._sandboxProfile
+ _OBJC_IVAR_$_OSLaunchdJobProperties._serviceType
+ _OBJC_IVAR_$_OSLaunchdJobProperties._spawnConstraint
+ _OBJC_IVAR_$_OSLaunchdJobProperties._uiApplicationClass
+ _OBJC_IVAR_$_OSLaunchdJobProperties._uiApplicationDelegateClass
+ _OBJC_IVAR_$_OSLaunchdJobProperties._watchdogTimeout
+ _OBJC_METACLASS_$_OSLaunchdJobProperties
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableDictionary_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSNumber_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_NSArray_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_NSData_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_NSDictionary_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_NSMutableDictionary_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_NSNumber_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_NSString_$_AppServiceSupportAdditions
+ __OBJC_$_CATEGORY_NSUUID_$_AppServiceSupportAdditions
+ __OBJC_$_INSTANCE_METHODS_OSLaunchdJobProperties
+ __OBJC_$_INSTANCE_VARIABLES_OSLaunchdJobProperties
+ __OBJC_$_PROP_LIST_NSArray_$_AppServiceSupportAdditions
+ __OBJC_$_PROP_LIST_NSData_$_AppServiceSupportAdditions
+ __OBJC_$_PROP_LIST_NSDictionary_$_AppServiceSupportAdditions
+ __OBJC_$_PROP_LIST_NSNumber_$_AppServiceSupportAdditions
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_NSString_$_AppServiceSupportAdditions
+ __OBJC_$_PROP_LIST_NSUUID_$_AppServiceSupportAdditions
+ __OBJC_$_PROP_LIST_OSLaunchdJobProperties
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__OSXPCObjectRepresentable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES__OSXPCObjectRepresentable
+ __OBJC_$_PROTOCOL_REFS__OSXPCObjectRepresentable
+ __OBJC_CATEGORY_PROTOCOLS_$_NSArray_$_AppServiceSupportAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_NSData_$_AppServiceSupportAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDictionary_$_AppServiceSupportAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_NSNumber_$_AppServiceSupportAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_NSString_$_AppServiceSupportAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_NSUUID_$_AppServiceSupportAdditions
+ __OBJC_CLASS_RO_$_OSLaunchdJobProperties
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$__OSXPCObjectRepresentable
+ __OBJC_METACLASS_RO_$_OSLaunchdJobProperties
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$__OSXPCObjectRepresentable
+ __OBJC_PROTOCOL_REFERENCE_$__OSXPCObjectRepresentable
+ ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.95
+ ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.95.cold.1
+ __xpc_mach_port_make_send_once
+ _mach_port_extract_right
+ _objc_msgSend$_OS_overlayDictionary:
+ _objc_msgSend$_OS_xpcObjectRepresentation
+ _objc_msgSend$_handlesToJobs:
+ _objc_msgSend$_submitExtension:overlay:domain:error:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bytes
+ _objc_msgSend$charValue
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$copy
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$intValue
+ _objc_msgSend$length
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objCType
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$oneShotUUID
+ _objc_msgSend$overlay
+ _objc_msgSend$path
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$shortValue
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$unsignedShortValue
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$watchdogTimeout
+ _objc_msgSend$xpcOverlay
+ _objc_setProperty_nonatomic_copy
+ _xpc_array_append_value
+ _xpc_bool_create
+ _xpc_data_create
+ _xpc_int64_create
+ _xpc_mach_send_once_create
+ _xpc_string_create
+ _xpc_uint64_create
+ _xpc_uuid_create
- +[OSLaunchdJob submitExtension:overlay:domain:error:].cold.1
- +[OSLaunchdJob submitExtension:overlay:domain:error:].cold.2
- ___64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.33
CStrings:
+ "#16@0:8"
+ "<%@: %p> XPC overlay:\n %@"
+ "<OSLaunchdDomain type %d, handle %qu>"
+ "@\"NSArray\""
+ "@\"NSData\""
+ "@\"NSObject<OS_xpc_object>\"16@0:8"
+ "@\"NSSet\""
+ "@\"NSString\"16@0:8"
+ "@\"NSURL\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8Q16^@24"
+ "@40@0:8:16@24@32"
+ "@48@0:8r*16@24@32^@40"
+ "AppServiceSupportAdditions"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "CFBundlePackageType"
+ "EnvironmentVariables"
+ "JoinExistingSession"
+ "NSObject"
+ "OSLaunchdJobProperties"
+ "PersonaEnterprise"
+ "Platform"
+ "ProgramArguments"
+ "RunLoopType"
+ "SandboxContainer"
+ "ServiceType"
+ "SpawnConstraint"
+ "T#,R"
+ "T@\"NSArray\",C,N,V_managedByServices"
+ "T@\"NSArray\",C,N,V_programArguments"
+ "T@\"NSData\",C,N,V_lightweightCodeRequirement"
+ "T@\"NSDictionary\",C,N,V_additionalProperties"
+ "T@\"NSDictionary\",C,N,V_additionalSubServices"
+ "T@\"NSDictionary\",C,N,V_arguments"
+ "T@\"NSDictionary\",C,N,V_environmentVariables"
+ "T@\"NSDictionary\",C,N,V_overlay"
+ "T@\"NSDictionary\",C,N,V_spawnConstraint"
+ "T@\"NSSet\",C,N,V_managedEndpointLaunchIdentifiers"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_personaString"
+ "T@\"NSString\",C,N,V_processType"
+ "T@\"NSString\",C,N,V_roleAccount"
+ "T@\"NSString\",C,N,V_runLoopType"
+ "T@\"NSString\",C,N,V_sandboxProfile"
+ "T@\"NSString\",C,N,V_serviceType"
+ "T@\"NSString\",C,N,V_uiApplicationClass"
+ "T@\"NSString\",C,N,V_uiApplicationDelegateClass"
+ "T@\"NSString\",R,C"
+ "T@\"NSURL\",&,N,V_sandboxContainer"
+ "T@\"NSUUID\",&,N,V_oneShotUUID"
+ "TB,N,V_abandonCoalition"
+ "TB,N,V_joinExistingSession"
+ "TB,N,V_omitSandboxParameters"
+ "TB,N,V_watchdogTimeout"
+ "TI,N,V_enterprisePersona"
+ "TI,N,V_platform"
+ "TQ,R"
+ "Vv16@0:8"
+ "XPC!"
+ "XPCService"
+ "^{_NSZone=}16@0:8"
+ "_AbandonCoalition"
+ "_AdditionalProperties"
+ "_AdditionalSubServices"
+ "_LaunchWatchdogTimeOut"
+ "_LightweightCodeRequirement"
+ "_ManagedBy_Services"
+ "_MultipleInstances"
+ "_OSXPCObjectRepresentable"
+ "_OS_overlayDictionary:"
+ "_OS_xpcObjectRepresentation"
+ "_OmitSandboxParameters"
+ "_RoleAccount"
+ "_SandboxProfile"
+ "_UIApplicationClass"
+ "_UIApplicationDelegateClass"
+ "_abandonCoalition"
+ "_additionalSubServices"
+ "_arguments"
+ "_enterprisePersona"
+ "_handlesToJobs:"
+ "_joinExistingSession"
+ "_lightweightCodeRequirement"
+ "_managedByServices"
+ "_managedEndpointLaunchIdentifiers"
+ "_omitSandboxParameters"
+ "_oneShotUUID"
+ "_overlay"
+ "_personaString"
+ "_platform"
+ "_programArguments"
+ "_roleAccount"
+ "_runLoopType"
+ "_sandboxContainer"
+ "_spawnConstraint"
+ "_submitExtension:overlay:domain:error:"
+ "_uiApplicationClass"
+ "_uiApplicationDelegateClass"
+ "_watchdogTimeout"
+ "abandonCoalition"
+ "additionalSubServices"
+ "arguments"
+ "assertion failure: \"(((reply_port) != 0) && ((reply_port) != ((mach_port_name_t) ~0)))\" -> %llu"
+ "assertion failure: \"handles != ((void *)0)\" -> %llu"
+ "autorelease"
+ "boolValue"
+ "bytes"
+ "charValue"
+ "class"
+ "client-reply-port"
+ "coalition-id"
+ "conformsToProtocol:"
+ "copy"
+ "copyJobsLoadedByCoalition failed with error %d: %s"
+ "copyJobsLoadedByCoalition:error:"
+ "copyJobsLoadedByJob failed with error %d: %s"
+ "copyJobsLoadedByJob:"
+ "debugDescription"
+ "enterprisePersona"
+ "fileSystemRepresentation"
+ "intValue"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "joinExistingSession"
+ "length"
+ "lightweightCodeRequirement"
+ "longLongValue"
+ "longValue"
+ "managedByServices"
+ "managedEndpointLaunchIdentifiers"
+ "numberWithBool:"
+ "numberWithUnsignedInt:"
+ "objCType"
+ "objectForKeyedSubscript:"
+ "omitSandboxParameters"
+ "oneShotUUID"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "personaString"
+ "platform"
+ "programArguments"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "roleAccount"
+ "runLoopType"
+ "sandboxContainer"
+ "self"
+ "setAbandonCoalition:"
+ "setAdditionalProperties:"
+ "setAdditionalSubServices:"
+ "setArguments:"
+ "setEnterprisePersona:"
+ "setJoinExistingSession:"
+ "setLightweightCodeRequirement:"
+ "setManagedByServices:"
+ "setManagedEndpointLaunchIdentifiers:"
+ "setObject:forKeyedSubscript:"
+ "setOmitSandboxParameters:"
+ "setOneShotUUID:"
+ "setOverlay:"
+ "setPersonaString:"
+ "setPlatform:"
+ "setProcessType:"
+ "setProgramArguments:"
+ "setRoleAccount:"
+ "setRunLoopType:"
+ "setSandboxContainer:"
+ "setServiceType:"
+ "setSpawnConstraint:"
+ "setUiApplicationClass:"
+ "setUiApplicationDelegateClass:"
+ "setValue:forKey:"
+ "setWatchdogTimeout:"
+ "shortValue"
+ "spawnConstraint"
+ "submitExtensionAtURL:properties:domain:error:"
+ "superclass"
+ "uiApplicationClass"
+ "uiApplicationDelegateClass"
+ "unsignedCharValue"
+ "unsignedIntValue"
+ "unsignedLongLongValue"
+ "unsignedLongValue"
+ "unsignedShortValue"
+ "v20@0:8I16"
+ "valueForKey:"
+ "watchdogTimeout"
+ "xpcOverlay"
+ "zone"
- "T@\"NSDictionary\",&,N,V_environmentVariables"
- "T@\"NSString\",&,N,V_sandboxProfile"

```
