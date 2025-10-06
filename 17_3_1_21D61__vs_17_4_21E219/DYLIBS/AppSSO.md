## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`

```diff

-384.60.2.0.0
-  __TEXT.__text: 0x23ea8
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x148c
+384.100.11.0.0
+  __TEXT.__text: 0x25158
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x14dc
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0xe50
-  __TEXT.__cstring: 0x29a5
+  __TEXT.__gcc_except_tab: 0xf6c
+  __TEXT.__cstring: 0x2a45
   __TEXT.__dlopen_cstrs: 0x5e4
-  __TEXT.__oslogstring: 0x395a
-  __TEXT.__unwind_info: 0xb54
+  __TEXT.__oslogstring: 0x3ab4
+  __TEXT.__unwind_info: 0xb8c
   __TEXT.__objc_classname: 0x3ba
-  __TEXT.__objc_methname: 0x4013
-  __TEXT.__objc_methtype: 0x93b
-  __TEXT.__objc_stubs: 0x3240
+  __TEXT.__objc_methname: 0x4249
+  __TEXT.__objc_methtype: 0x952
+  __TEXT.__objc_stubs: 0x3460
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0xae0
+  __DATA_CONST.__const: 0xae8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x37e0
-  __DATA_CONST.__objc_selrefs: 0xec8
+  __DATA_CONST.__objc_const: 0x3810
+  __DATA_CONST.__objc_selrefs: 0xf60
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__objc_const: 0x990
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__cfstring: 0xe20
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x358
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x178
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0x134
+  __DATA.__objc_ivar: 0x138
   __DATA.__data: 0x6f0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x550

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14D8A020-F934-3DD5-B438-98CBD6C2EEA3
-  Functions: 902
-  Symbols:   3092
-  CStrings:  1454
+  UUID: 68391B08-A2FD-3E17-8389-913B0C6BA075
+  Functions: 922
+  Symbols:   3156
+  CStrings:  1490
 
Symbols:
+ -[SOConfigurationHost _checkAssociatedDomainForProfiles:].cold.1
+ -[SOConfigurationHost _defaultCacheFile]
+ -[SOConfigurationHost _initCachePath:ifNeededWithError:]
+ -[SOConfigurationHost _initCachePath:ifNeededWithError:].cold.1
+ -[SOConfigurationHost _initCachePath:ifNeededWithError:].cold.2
+ -[SOConfigurationHost _initCachePath:ifNeededWithError:].cold.3
+ -[SOConfigurationHost _loadCacheFromDisk]
+ -[SOConfigurationHost _loadCacheFromDisk].cold.1
+ -[SOConfigurationHost _loadCacheFromDisk].cold.2
+ -[SOConfigurationHost _saveCacheToFile:error:]
+ -[SOConfigurationHost _saveCacheToFile:error:].cold.1
+ -[SOConfigurationHost _saveCacheToFile:error:].cold.2
+ -[SOConfigurationHost _saveCacheToFile:error:].cold.3
+ -[SOConfigurationHost associatedDomainCache]
+ -[SOConfigurationHost saveConfiguration:error:].cold.2
+ -[SOConfigurationHost setAssociatedDomainCache:]
+ -[SOExtension checkAssociatedDomainsWithCache:]
+ -[SOExtension checkAssociatedDomainsWithCache:].cold.1
+ -[SOExtension checkAssociatedDomainsWithCache:].cold.2
+ -[SOExtension checkAssociatedDomainsWithCache:].cold.3
+ -[SOExtension checkAssociatedDomainsWithCache:].cold.4
+ -[SOExtension hasURLApprovedAssociatedDomain:cache:]
+ -[SOExtension removeExpiredEntriesFromCache:]
+ GCC_except_table25
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table66
+ GCC_except_table70
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_IVAR_$_SOConfigurationHost._associatedDomainCache
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ ___104-[SOExtension beginUserRegistrationUsingUserName:authenticationMethod:options:extensionData:completion:]_block_invoke.74
+ ___41-[SOExtension protocolVersionCompletion:]_block_invoke.78
+ ___41-[SOExtension protocolVersionCompletion:]_block_invoke.78.cold.1
+ ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.77
+ ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.77.cold.1
+ ___46-[SOExtension cancelAuthorization:completion:]_block_invoke.12
+ ___48-[SOExtension canPerformRegistrationCompletion:]_block_invoke.79
+ ___49-[SOExtensionServiceConnection _connectToService]_block_invoke.46
+ ___49-[SOExtensionServiceConnection _connectToService]_block_invoke.46.cold.1
+ ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.76
+ ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.76.cold.1
+ ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.75
+ ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.75.cold.1
+ ___72-[SOExtension _connectContextToSessionWithRequestIdentifier:completion:]_block_invoke.22
+ ___76-[SOExtension beginDeviceRegistrationUsingOptions:extensionData:completion:]_block_invoke.72
+ ___block_literal_global.108
+ ___block_literal_global.165
+ ___block_literal_global.182
+ ___block_literal_global.55
+ _getuid
+ _kAssociatedDomainCacheTime
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$_defaultCacheFile
+ _objc_msgSend$_initCachePath:ifNeededWithError:
+ _objc_msgSend$_loadCacheFromDisk
+ _objc_msgSend$_saveCacheToFile:error:
+ _objc_msgSend$allKeys
+ _objc_msgSend$checkAssociatedDomainsWithCache:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$hasURLApprovedAssociatedDomain:cache:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$removeExpiredEntriesFromCache:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$writeToURL:options:error:
- -[SOExtension checkAssociatedDomains]
- -[SOExtension checkAssociatedDomains].cold.1
- -[SOExtension checkAssociatedDomains].cold.2
- -[SOExtension checkAssociatedDomains].cold.3
- -[SOExtension checkAssociatedDomains].cold.4
- -[SOExtension hasURLApprovedAssociatedDomain:]
- GCC_except_table28
- GCC_except_table31
- GCC_except_table65
- GCC_except_table69
- ___104-[SOExtension beginUserRegistrationUsingUserName:authenticationMethod:options:extensionData:completion:]_block_invoke.70
- ___41-[SOExtension protocolVersionCompletion:]_block_invoke.74
- ___41-[SOExtension protocolVersionCompletion:]_block_invoke.74.cold.1
- ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.73
- ___45-[SOExtension supportedGrantTypesCompletion:]_block_invoke.73.cold.1
- ___46-[SOExtension cancelAuthorization:completion:]_block_invoke.11
- ___48-[SOExtension canPerformRegistrationCompletion:]_block_invoke.75
- ___49-[SOExtensionServiceConnection _connectToService]_block_invoke.45
- ___49-[SOExtensionServiceConnection _connectToService]_block_invoke.45.cold.1
- ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.72
- ___51-[SOExtension registrationDidCancelWithCompletion:]_block_invoke.72.cold.1
- ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.71
- ___53-[SOExtension registrationDidCompleteWithCompletion:]_block_invoke.71.cold.1
- ___72-[SOExtension _connectContextToSessionWithRequestIdentifier:completion:]_block_invoke.21
- ___76-[SOExtension beginDeviceRegistrationUsingOptions:extensionData:completion:]_block_invoke.68
- ___block_literal_global.107
- ___block_literal_global.164
- ___block_literal_global.54
- _objc_msgSend$checkAssociatedDomains
- _objc_msgSend$hasURLApprovedAssociatedDomain:
CStrings:
+ "%@/Cache/%@"
+ "-[SOConfigurationHost _initCachePath:ifNeededWithError:]"
+ "-[SOConfigurationHost _saveCacheToFile:error:]"
+ "-[SOExtension checkAssociatedDomainsWithCache:]"
+ "-[SOExtension hasURLApprovedAssociatedDomain:cache:]"
+ "@\"NSMutableDictionary\""
+ "Associated domain: %{public}@ is cached"
+ "Associated domain: failed to save cache to file"
+ "JSONObjectWithData:options:error:"
+ "T@\"NSMutableDictionary\",&,V_associatedDomainCache"
+ "T@\"NSString\",?,R,C"
+ "_associatedDomainCache"
+ "_defaultCacheFile"
+ "_initCachePath:ifNeededWithError:"
+ "_loadCacheFromDisk"
+ "_saveCacheToFile:error:"
+ "allKeys"
+ "associatedDomainCache"
+ "cache written to file: %{public}@, %{public}@"
+ "checkAssociatedDomainsWithCache:"
+ "com.apple.AppSSO.cache.json"
+ "created cache directory at %{public}@"
+ "dataWithContentsOfURL:options:error:"
+ "dataWithJSONObject:options:error:"
+ "date"
+ "dateWithTimeIntervalSince1970:"
+ "doubleValue"
+ "failed to create cache directory at %{public}@: %{public}@"
+ "failed to load cache at %{private}@, error: %{public}@"
+ "failed to save cache to file: %{public}@, error: %{public}@"
+ "hasURLApprovedAssociatedDomain:cache:"
+ "numberWithDouble:"
+ "removeExpiredEntriesFromCache:"
+ "setAssociatedDomainCache:"
+ "stringByDeletingLastPathComponent"
+ "timeIntervalSince1970"
+ "timeIntervalSinceNow"
+ "writeToURL:options:error:"
- "-[SOExtension checkAssociatedDomains]"
- "-[SOExtension hasURLApprovedAssociatedDomain:]"
- "checkAssociatedDomains"
- "hasURLApprovedAssociatedDomain:"

```
