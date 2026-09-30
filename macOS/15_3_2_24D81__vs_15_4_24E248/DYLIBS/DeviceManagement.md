## DeviceManagement

> `/System/Library/PrivateFrameworks/DeviceManagement.framework/Versions/A/DeviceManagement`

```diff

-221.2.7.0.0
-  __TEXT.__text: 0x3c0e4
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x6db0
+221.4.7.0.0
+  __TEXT.__text: 0x3dbcc
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x7314
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x5042
-  __TEXT.__oslogstring: 0xceb
+  __TEXT.__cstring: 0x5039
+  __TEXT.__oslogstring: 0xda1
   __TEXT.__ustring: 0xb64
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__unwind_info: 0xe70
-  __TEXT.__objc_classname: 0x173b
-  __TEXT.__objc_methname: 0x9a8d
-  __TEXT.__objc_methtype: 0xade
-  __TEXT.__objc_stubs: 0x4ba0
-  __DATA_CONST.__got: 0x358
+  __TEXT.__gcc_except_tab: 0x2f8
+  __TEXT.__unwind_info: 0xf30
+  __TEXT.__objc_classname: 0x178e
+  __TEXT.__objc_methname: 0x9c05
+  __TEXT.__objc_methtype: 0xb24
+  __TEXT.__objc_stubs: 0x4c40
+  __DATA_CONST.__got: 0x368
   __DATA_CONST.__const: 0xa08
-  __DATA_CONST.__objc_classlist: 0x600
+  __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c98
+  __DATA_CONST.__objc_selrefs: 0x1d68
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4b8
-  __DATA_CONST.__objc_arraydata: 0x680
-  __AUTH_CONST.__auth_got: 0x230
-  __AUTH_CONST.__const: 0x930
-  __AUTH_CONST.__cfstring: 0x7320
-  __AUTH_CONST.__objc_const: 0x10320
-  __AUTH_CONST.__objc_intobj: 0x14b8
-  __AUTH_CONST.__objc_arrayobj: 0x858
-  __AUTH.__objc_data: 0x1b8
-  __DATA.__objc_ivar: 0x89c
+  __DATA_CONST.__objc_superrefs: 0x4c8
+  __DATA_CONST.__objc_arraydata: 0x6a0
+  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__const: 0x9e0
+  __AUTH_CONST.__cfstring: 0x7360
+  __AUTH_CONST.__objc_const: 0x102c8
+  __AUTH_CONST.__objc_intobj: 0x1518
+  __AUTH_CONST.__objc_arrayobj: 0x888
+  __AUTH.__objc_data: 0x2a8
+  __DATA.__objc_ivar: 0x8d4
   __DATA.__data: 0x430
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0x188
   __DATA_DIRTY.__objc_data: 0x3a48
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/Versions/A/ManagedSettingsObjC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3FD51FD-2673-3A73-A396-AE744AD689A0
-  Functions: 2271
-  Symbols:   5572
-  CStrings:  3947
+  UUID: 0177BA15-495D-3D14-9E13-BAE2C3F5C22C
+  Functions: 2359
+  Symbols:   5732
+  CStrings:  3971
 
Symbols:
+ +[DMFApplicationPolicyMonitor policyTypes].cold.1
+ +[DMFCategoryPolicyMonitor policyTypes].cold.1
+ +[DMFCommunicationPolicyMonitor communicationBundleIdentifiers].cold.1
+ +[DMFCommunicationPolicyMonitor policyTypes].cold.1
+ +[DMFConnection connectionForAppleID:].cold.1
+ +[DMFConnection connectionForUID:].cold.1
+ +[DMFDevice propertyNameForKey:].cold.1
+ +[DMFEffectivePolicy systemCategoryIdentifiers].cold.1
+ +[DMFEffectivePolicy unblockableCategoryIdentifiers].cold.1
+ +[DMFEmergencyModeMonitor remoteInterface].cold.1
+ +[DMFEmergencyModeMonitor sharedMonitor].cold.1
+ +[DMFFetchAppInfoRequest allowlistedClassForResultObject]
+ +[DMFFetchAppInfoRequest isPermittedOnSystemConnection]
+ +[DMFFetchAppInfoRequest isPermittedOnUserConnection]
+ +[DMFFetchAppInfoRequest permittedPlatforms]
+ +[DMFFetchAppInfoRequest supportsSecureCoding]
+ +[DMFFetchAppInfoResultObject supportsSecureCoding]
+ +[DMFFetchDevicePropertiesRequest devicePropertyKeysForPlatform:].cold.1
+ +[DMFFetchSecurityInformationRequest allPlatformSecurityInfoKeys].cold.1
+ +[DMFFetchSecurityInformationRequest iOSSecurityInfoKeys].cold.1
+ +[DMFFetchSecurityInformationRequest macOSSecurityInfoKeys].cold.1
+ +[DMFFetchSecurityInformationRequest tvOSSecurityInfoKeys].cold.1
+ +[DMFFetchSecurityInformationRequest watchOSSecurityInfoKeys].cold.1
+ +[DMFPolicyMonitor allEffectivePolicyTypes]
+ +[DMFPolicyMonitor allEffectivePolicyTypes].cold.1
+ +[DMFPolicyMonitor policyMonitor].cold.1
+ +[DMFPolicyMonitor remoteInterface].cold.1
+ +[DMFUpdateAppAttributesRequest isPermittedOnSystemConnection]
+ +[DMFUpdateAppAttributesRequest isPermittedOnUserConnection]
+ +[DMFUpdateAppAttributesRequest permittedPlatforms]
+ +[DMFUpdateAppAttributesRequest supportsSecureCoding]
+ +[DMFWebsitePolicyMonitor policyTypes].cold.1
+ -[DMFBatchRequestOperation initWithActivityTransactionOperation:subOperations:].cold.1
+ -[DMFBook description].cold.1
+ -[DMFConfigurationSourceClient dealloc].cold.1
+ -[DMFConfigurationSourceClient initWithConnection:organizationIdentifier:displayName:localMachServiceName:].cold.1
+ -[DMFConfigurationSourceClient initWithConnection:organizationIdentifier:displayName:localMachServiceName:].cold.2
+ -[DMFConfigurationSourceClient initWithConnection:organizationIdentifier:displayName:localMachServiceName:].cold.3
+ -[DMFConfigurationSourceClient registerConfigurationSourceIfNeeded].cold.1
+ -[DMFConnection initWithTransportProvider:userInfo:].cold.1
+ -[DMFConnection performRequest:completion:].cold.1
+ -[DMFConnection prepareOperationForRequest:].cold.1
+ -[DMFControlGroupIdentifier initWithOrganizationUUID:groupID:].cold.1
+ -[DMFControlGroupIdentifier initWithString:].cold.1
+ -[DMFControlSessionIdentifier initWithString:].cold.1
+ -[DMFFetchAppInfoResultObject .cxx_destruct]
+ -[DMFFetchAppInfoResultObject addAttributes:forApp:]
+ -[DMFFetchAppInfoResultObject description]
+ -[DMFFetchAppInfoResultObject encodeWithCoder:]
+ -[DMFFetchAppInfoResultObject initWithCoder:]
+ -[DMFFetchAppInfoResultObject init]
+ -[DMFFetchAppInfoResultObject managedApps]
+ -[DMFMDMv1UpdateAppRequest ignoreNilConfiguration]
+ -[DMFMDMv1UpdateAppRequest setIgnoreNilConfiguration:]
+ -[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:completionHandler:]
+ -[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:withError:]
+ -[DMFPolicyRegistration initWithIdentifier:policyTypes:callback:].cold.1
+ -[DMFUpdateAppAttributesRequest .cxx_destruct]
+ -[DMFUpdateAppAttributesRequest DNSProxyUUIDString]
+ -[DMFUpdateAppAttributesRequest VPNUUIDString]
+ -[DMFUpdateAppAttributesRequest allowUserToHide]
+ -[DMFUpdateAppAttributesRequest allowUserToLock]
+ -[DMFUpdateAppAttributesRequest associatedDomainsEnableDirectDownloads]
+ -[DMFUpdateAppAttributesRequest associatedDomains]
+ -[DMFUpdateAppAttributesRequest cellularSliceUUIDString]
+ -[DMFUpdateAppAttributesRequest contentFilterUUIDString]
+ -[DMFUpdateAppAttributesRequest description]
+ -[DMFUpdateAppAttributesRequest encodeWithCoder:]
+ -[DMFUpdateAppAttributesRequest initWithCoder:]
+ -[DMFUpdateAppAttributesRequest managementOptions]
+ -[DMFUpdateAppAttributesRequest relayUUIDString]
+ -[DMFUpdateAppAttributesRequest removable]
+ -[DMFUpdateAppAttributesRequest setAllowUserToHide:]
+ -[DMFUpdateAppAttributesRequest setAllowUserToLock:]
+ -[DMFUpdateAppAttributesRequest setAssociatedDomains:]
+ -[DMFUpdateAppAttributesRequest setAssociatedDomainsEnableDirectDownloads:]
+ -[DMFUpdateAppAttributesRequest setCellularSliceUUIDString:]
+ -[DMFUpdateAppAttributesRequest setContentFilterUUIDString:]
+ -[DMFUpdateAppAttributesRequest setDNSProxyUUIDString:]
+ -[DMFUpdateAppAttributesRequest setManagementOptions:]
+ -[DMFUpdateAppAttributesRequest setRelayUUIDString:]
+ -[DMFUpdateAppAttributesRequest setRemovable:]
+ -[DMFUpdateAppAttributesRequest setTapToPayScreenLock:]
+ -[DMFUpdateAppAttributesRequest setVPNUUIDString:]
+ -[DMFUpdateAppAttributesRequest tapToPayScreenLock]
+ DMFAppLog.cold.1
+ DMFAtomicFileWritingLog.cold.1
+ DMFConfigurationEngineLog.cold.1
+ DMFConfigurationSourceClientXPCInterface.cold.1
+ DMFEmergencyModeLog.cold.1
+ DMFOSUpdateLog.cold.1
+ DMFPersonalHotspotLog.cold.1
+ DMFPolicyLog.cold.1
+ DMFServerLog.cold.1
+ GCC_except_table27
+ GCC_except_table32
+ GCC_except_table45
+ GCC_except_table54
+ GCC_except_table67
+ OBJC_IVAR_$_DMFFetchAppInfoResultObject._managedApps
+ OBJC_IVAR_$_DMFMDMv1UpdateAppRequest._ignoreNilConfiguration
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._DNSProxyUUIDString
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._VPNUUIDString
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._allowUserToHide
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._allowUserToLock
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._associatedDomains
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._associatedDomainsEnableDirectDownloads
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._cellularSliceUUIDString
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._contentFilterUUIDString
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._managementOptions
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._relayUUIDString
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._removable
+ OBJC_IVAR_$_DMFUpdateAppAttributesRequest._tapToPayScreenLock
+ _DMFErrorDescriptionsWithCodeAndUserInfo.cold.1
+ _OBJC_CLASS_$_DMFFetchAppInfoRequest
+ _OBJC_CLASS_$_DMFFetchAppInfoResultObject
+ _OBJC_CLASS_$_DMFUpdateAppAttributesRequest
+ _OBJC_METACLASS_$_DMFFetchAppInfoRequest
+ _OBJC_METACLASS_$_DMFFetchAppInfoResultObject
+ _OBJC_METACLASS_$_DMFUpdateAppAttributesRequest
+ __38-[DMFConfigurationSourceClient resume]_block_invoke.cold.1
+ __54-[DMFPolicyMonitor requestPoliciesForTypes:withError:]_block_invoke.130
+ __54-[DMFPolicyMonitor requestPoliciesForTypes:withError:]_block_invoke.130.cold.1
+ __62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.123
+ __62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.123.cold.1
+ __62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.129
+ __64-[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:withError:]_block_invoke.143
+ __64-[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:withError:]_block_invoke.143.cold.1
+ __64-[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:withError:]_block_invoke.cold.1
+ __66-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:withError:]_block_invoke.133
+ __66-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:withError:]_block_invoke.133.cold.1
+ __68-[DMFPolicyMonitor requestPoliciesForWebsiteURLs:completionHandler:]_block_invoke.139
+ __68-[DMFPolicyMonitor requestPoliciesForWebsiteURLs:completionHandler:]_block_invoke.139.cold.1
+ __68-[DMFPolicyMonitor requestPoliciesForWebsiteURLs:completionHandler:]_block_invoke.140
+ __72-[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:completionHandler:]_block_invoke.147
+ __72-[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:completionHandler:]_block_invoke.147.cold.1
+ __72-[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:completionHandler:]_block_invoke.cold.1
+ __74-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.131
+ __74-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.131.cold.1
+ __74-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.132
+ __76-[DMFPolicyMonitor requestPoliciesForCategoryIdentifiers:completionHandler:]_block_invoke.137
+ __76-[DMFPolicyMonitor requestPoliciesForCategoryIdentifiers:completionHandler:]_block_invoke.137.cold.1
+ __76-[DMFPolicyMonitor requestPoliciesForCategoryIdentifiers:completionHandler:]_block_invoke.138
+ __79-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:withError:]_block_invoke.136
+ __79-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:withError:]_block_invoke.136.cold.1
+ __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.118
+ __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.118.cold.1
+ __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.118.cold.2
+ __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.119
+ __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.122
+ __87-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.134
+ __87-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.134.cold.1
+ __87-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.135
+ __OBJC_$_CLASS_METHODS_DMFFetchAppInfoRequest
+ __OBJC_$_CLASS_METHODS_DMFFetchAppInfoResultObject
+ __OBJC_$_CLASS_METHODS_DMFUpdateAppAttributesRequest
+ __OBJC_$_CLASS_PROP_LIST_DMFPolicyMonitor
+ __OBJC_$_INSTANCE_METHODS_DMFFetchAppInfoResultObject
+ __OBJC_$_INSTANCE_METHODS_DMFUpdateAppAttributesRequest
+ __OBJC_$_INSTANCE_VARIABLES_DMFFetchAppInfoResultObject
+ __OBJC_$_INSTANCE_VARIABLES_DMFUpdateAppAttributesRequest
+ __OBJC_$_PROP_LIST_DMFFetchAppInfoResultObject
+ __OBJC_$_PROP_LIST_DMFUpdateAppAttributesRequest
+ __OBJC_CLASS_RO_$_DMFFetchAppInfoRequest
+ __OBJC_CLASS_RO_$_DMFFetchAppInfoResultObject
+ __OBJC_CLASS_RO_$_DMFUpdateAppAttributesRequest
+ __OBJC_METACLASS_RO_$_DMFFetchAppInfoRequest
+ __OBJC_METACLASS_RO_$_DMFFetchAppInfoResultObject
+ __OBJC_METACLASS_RO_$_DMFUpdateAppAttributesRequest
+ ___43+[DMFPolicyMonitor allEffectivePolicyTypes]_block_invoke
+ ___64-[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:withError:]_block_invoke
+ ___72-[DMFPolicyMonitor filterForExpiredBudgetIdentifiers:completionHandler:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_48_e8_32s40s_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16l
+ __block_literal_global.116
+ _objc_getProperty
+ _objc_msgSend$filterForExpiredBudgetIdentifiers:shouldBeSynchronous:replyHandler:
+ _objc_msgSend$ignoreNilConfiguration
+ _objc_msgSend$managedApps
+ _objc_msgSend$setPoliciesByBundleIdentifier:
+ _objc_msgSend$setValue:forKey:
+ _objc_setProperty_atomic_copy
+ allEffectivePolicyTypes.allTypes
+ allEffectivePolicyTypes.onceToken
- GCC_except_table25
- GCC_except_table30
- GCC_except_table43
- GCC_except_table52
- __54-[DMFPolicyMonitor requestPoliciesForTypes:withError:]_block_invoke.125
- __54-[DMFPolicyMonitor requestPoliciesForTypes:withError:]_block_invoke.125.cold.1
- __62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.118
- __62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.118.cold.1
- __62-[DMFPolicyMonitor requestPoliciesForTypes:completionHandler:]_block_invoke.124
- __66-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:withError:]_block_invoke.128
- __66-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:withError:]_block_invoke.128.cold.1
- __68-[DMFPolicyMonitor requestPoliciesForWebsiteURLs:completionHandler:]_block_invoke.134
- __68-[DMFPolicyMonitor requestPoliciesForWebsiteURLs:completionHandler:]_block_invoke.134.cold.1
- __68-[DMFPolicyMonitor requestPoliciesForWebsiteURLs:completionHandler:]_block_invoke.135
- __74-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.126
- __74-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.126.cold.1
- __74-[DMFPolicyMonitor requestPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.127
- __76-[DMFPolicyMonitor requestPoliciesForCategoryIdentifiers:completionHandler:]_block_invoke.132
- __76-[DMFPolicyMonitor requestPoliciesForCategoryIdentifiers:completionHandler:]_block_invoke.132.cold.1
- __76-[DMFPolicyMonitor requestPoliciesForCategoryIdentifiers:completionHandler:]_block_invoke.133
- __79-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:withError:]_block_invoke.131
- __79-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:withError:]_block_invoke.131.cold.1
- __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.113
- __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.113.cold.1
- __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.113.cold.2
- __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.114
- __81-[DMFPolicyMonitor addRegistration:forPolicyMonitorIdentifier:completionHandler:]_block_invoke.117
- __87-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.129
- __87-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.129.cold.1
- __87-[DMFPolicyMonitor requestCommunicationPoliciesForBundleIdentifiers:completionHandler:]_block_invoke.130
- _os_variant_has_factory_content
CStrings:
+ "Attributes"
+ "DMFFetchAppInfoRequest"
+ "DMFFetchAppInfoResultObject"
+ "DMFUpdateAppAttributesRequest"
+ "Failed to create an operation for request: \"%{public}@\": %{public}@"
+ "Failed to filter %lu identifiers with error: %{public}@"
+ "Successfully filtered %lu identifiers. Result: %@{public}"
+ "T@\"NSDictionary\",C,V_policiesByBundleIdentifier"
+ "T@\"NSDictionary\",R,C,N,V_managedApps"
+ "TB,N,V_ignoreNilConfiguration"
+ "_ignoreNilConfiguration"
+ "_managedApps"
+ "addAttributes:forApp:"
+ "allEffectivePolicyTypes"
+ "filterForExpiredBudgetIdentifiers:completionHandler:"
+ "filterForExpiredBudgetIdentifiers:shouldBeSynchronous:replyHandler:"
+ "filterForExpiredBudgetIdentifiers:withError:"
+ "ignoreNilConfiguration"
+ "managedApps"
+ "setIgnoreNilConfiguration:"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@16B24@?28"
- "T@\"NSDictionary\",C,N,V_policiesByBundleIdentifier"
- "com.apple.DeviceManagement"
- "connection %@ did not return an operation for request: %@"

```
