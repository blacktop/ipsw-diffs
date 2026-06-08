## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

```diff

-498.0.0.0.0
-  __TEXT.__text: 0x18fec
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_stubs: 0x3080
-  __TEXT.__objc_methlist: 0xfb8
+510.0.0.0.0
+  __TEXT.__text: 0x17874
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_stubs: 0x3180
+  __TEXT.__objc_methlist: 0xfe8
   __TEXT.__const: 0x62
-  __TEXT.__objc_methname: 0x2f44
-  __TEXT.__oslogstring: 0x2ce7
-  __TEXT.__cstring: 0x11b6
-  __TEXT.__objc_classname: 0x192
-  __TEXT.__objc_methtype: 0x6fb
-  __TEXT.__gcc_except_tab: 0x53c
-  __TEXT.__unwind_info: 0x4d8
-  __DATA_CONST.__auth_got: 0x598
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__cfstring: 0x1160
+  __TEXT.__objc_methname: 0x3062
+  __TEXT.__oslogstring: 0x2c24
+  __TEXT.__cstring: 0x138c
+  __TEXT.__objc_classname: 0x171
+  __TEXT.__objc_methtype: 0x724
+  __TEXT.__gcc_except_tab: 0x478
+  __TEXT.__unwind_info: 0x4b0
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__cfstring: 0x1220
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x2768
-  __DATA.__objc_selrefs: 0xdf0
-  __DATA.__objc_ivar: 0x118
+  __DATA_CONST.__auth_got: 0x5d8
+  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x2798
+  __DATA.__objc_selrefs: 0xe28
+  __DATA.__objc_ivar: 0x11c
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A3F8CCBB-986E-34E1-89B9-AD4D0DDF7FD8
-  Functions: 447
-  Symbols:   1474
-  CStrings:  1229
+  UUID: 9EDC36CB-7A2D-39B0-BF6A-49654047BE9F
+  Functions: 436
+  Symbols:   1482
+  CStrings:  1251
 
Symbols:
+ -[PKDAnnotationStore containerURL].cold.2
+ -[PKDAnnotationStore containerURL].cold.3
+ -[PKDContainerProvider query_get_single_result:]
+ -[PKDPersona initWithPersonaID:dataSeparated:]
+ -[PKDPersona isDataSeparated]
+ -[PKDPersonaCache _lock_personaUniqueStringsToPersonas:]
+ -[PKDPersonaCache lock_personaUniqueStringToPersonaMap]
+ -[PKDPersonaCache personasForPersonaUniqueStrings:error:]
+ -[PKDPlugIn _personaIDForClient:requestedPersona:error:]
+ -[PKDPlugIn _personaIDForClient:requestedPersona:error:].cold.1
+ -[PKDPlugIn _personaIDForClient:requestedPersona:error:].cold.2
+ -[PKDPlugIn _personaIDForClient:requestedPersona:error:].cold.3
+ -[PKDPlugIn _personaIDForClient:requestedPersona:error:].cold.4
+ -[PKDPlugIn reportAnalyticsForPersonaLaunchWithClient:requestedPersona:]
+ -[PKDPlugIn reportAnalyticsForPersonaLaunchWithClient:requestedPersona:].cold.1
+ OBJC_IVAR_$_PKDPersona._dataSeparated
+ OBJC_IVAR_$_PKDPersonaCache._lock_personaUniqueStringToPersonaMap
+ _CONTAINER_PERSONA_PRIMARY
+ _OBJC_$_PROP_LIST_PKDExternalProviders.96
+ _PKUseLSPersonaAssociations
+ _SecTaskCopySigningIdentifier
+ ___72-[PKDPlugIn reportAnalyticsForPersonaLaunchWithClient:requestedPersona:]_block_invoke
+ ___72-[PKDPlugIn reportAnalyticsForPersonaLaunchWithClient:requestedPersona:]_block_invoke_2
+ ___72-[PKDPlugIn reportAnalyticsForPersonaLaunchWithClient:requestedPersona:]_block_invoke_3
+ ___72-[PKDPlugIn reportAnalyticsForPersonaLaunchWithClient:requestedPersona:]_block_invoke_4
+ ___block_descriptor_32_e33_Q16?0"UMUserPersonaAttributes"8l
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ __block_literal_global.256
+ _container_copy_sandbox_token
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_lock_personaUniqueStringsToPersonas:
+ _objc_msgSend$_personaIDForClient:requestedPersona:error:
+ _objc_msgSend$clientid
+ _objc_msgSend$initWithPersonaID:dataSeparated:
+ _objc_msgSend$isDataSeparated
+ _objc_msgSend$isDefaultPersona
+ _objc_msgSend$lock_personaUniqueStringToPersonaMap
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$personasForPersonaUniqueStrings:error:
+ _objc_msgSend$query_get_single_result:
+ _objc_msgSend$reportAnalyticsForPersonaLaunchWithClient:requestedPersona:
+ _objc_msgSend$sandbox
+ _objc_msgSend$sandbox_extension_consume:
+ _objc_msgSend$setWithCapacity:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x9
+ reportAnalyticsForPersonaLaunchWithClient:requestedPersona:.onceToken
+ reportAnalyticsForPersonaLaunchWithClient:requestedPersona:.queue
- -[PKDContainerProvider create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:]
- -[PKDPersona initWithPersonaID:enterprise:]
- -[PKDPersona isEnterprise]
- -[PKDPlugIn _personaIDForClient:requestedPersona:]
- -[PKDPlugIn _personaIDForClient:requestedPersona:].cold.1
- -[PKDPlugIn _personaIDForClient:requestedPersona:].cold.2
- -[PKDPlugIn _personaIDForClient:requestedPersona:].cold.3
- -[PKDPlugIn _personaIDForClient:requestedPersona:].cold.4
- -[PKDPlugIn _personaIDForClient:requestedPersona:].cold.5
- -[PKDPlugIn enableForClient:environment:languages:oneShotUUID:persona:sandbox:pid:error:].cold.4
- GCC_except_table37
- GCC_except_table38
- OBJC_IVAR_$_PKDPersona._enterprise
- _OBJC_$_PROP_LIST_PKDExternalProviders.97
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _PKPersonaEntitlementNoneValue
- _PKPersonaEntitlementPersonalValue
- _PKPersonaPropagateEntitlement
- _container_create_or_lookup_path_for_current_user
- _objc_msgSend$_personaIDForClient:requestedPersona:
- _objc_msgSend$create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:
- _objc_msgSend$dataContainerURLForPersona:
- _objc_msgSend$initWithPersonaID:enterprise:
- _objc_msgSend$isEnterprise
- _objc_msgSend$isEnterprisePersona
CStrings:
+ "%@: personaID: %@, isDataSeparated: %s"
+ "<unknown>"
+ "@40@0:8@16@24^@32"
+ "Containing bundle [%@] is associated with more than one persona. Caller must disambiguate by specifying desired persona; %@(%@)"
+ "InDiagnosticsMode"
+ "Q16@?0@\"UMUserPersonaAttributes\"8"
+ "Sent analytics event: %d; %@"
+ "T@\"NSDictionary\",R,N,V_lock_personaUniqueStringToPersonaMap"
+ "TB,R,GisDataSeparated,V_dataSeparated"
+ "Unrecognized persona string [%@]"
+ "^{container_object_s=}24@0:8^{container_query_s=}16"
+ "_dataSeparated"
+ "_lock_personaUniqueStringToPersonaMap"
+ "_lock_personaUniqueStringsToPersonas:"
+ "_personaIDForClient:requestedPersona:error:"
+ "client asked for unavailable persona for launch of plugin %@(%@); persona = %@"
+ "com.apple.PlugInKit.HostPersonaLaunch"
+ "com.apple.pkd.analytics"
+ "dataSeparated"
+ "error setting persona for launch of plugin %@(%@); personas = %@, error = %@"
+ "extensionEntitled"
+ "extensionIdentifier"
+ "extensionPersona"
+ "failed to consume storage container sandbox extension: error=%{darwin.errno}u"
+ "failed to get storage container: error=%s"
+ "hostEntitled"
+ "hostIdentifier"
+ "hostPersona"
+ "initWithPersonaID:dataSeparated:"
+ "isDataSeparated"
+ "isDefaultPersona"
+ "lock_personaUniqueStringToPersonaMap"
+ "numberWithUnsignedInteger:"
+ "personasForPersonaUniqueStrings:error:"
+ "query_get_single_result:"
+ "reportAnalyticsForPersonaLaunchWithClient:requestedPersona:"
+ "sandbox extension was not provided for container"
+ "sandbox_extension_consume:"
+ "setWithCapacity:"
+ "unable to locate user container: error %s"
+ "unknown error deciding persona for launch of plugin %@(%@)"
- "%@: personaID: %@, isEnterprise: %s"
- "*56@0:8Q16r*24B32B36^B40^Q48"
- "3kmXfug8VcxLI5yEmsqQKw"
- "CFFIXED_USER_HOME"
- "HOME"
- "TB,R,GisEnterprise,V_enterprise"
- "TMPDIR"
- "[u %{public}@] [%@(%@)] assigning to no specific persona"
- "[u %{public}@] [%@(%@)] assigning to personal persona ID %@ by entitlement"
- "[u %{public}@] [%@(%@)] failed for get personas for bundle identifier: %@"
- "[u %{public}@] [%@(%@)] no data container"
- "[u %{public}@] [%@(%@)] setting sandbox container to %@"
- "[u %{public}@] [%@(%@)] will launch with system-defined policy by entitlement"
- "_SandboxContainer"
- "_enterprise"
- "_personaIDForClient:requestedPersona:"
- "create_or_lookup_path_for_current_user:identifier:create_if_necessary:transient:out_existed:out_error:"
- "enterprise"
- "error setting persona for launch of plugin %@(%@)"
- "failed to get storage container: error=%llu"
- "initWithPersonaID:enterprise:"
- "isEnterprise"
- "isEnterprisePersona"
- "tmp"
- "unable to locate user container: error %llu"

```
