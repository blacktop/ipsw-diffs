## SetupAssistantFramework

> `/System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework`

```diff

-7217.1.0.0.0
-  __TEXT.__text: 0x66c4
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x53c
+7407.4.12.204.0
+  __TEXT.__text: 0x8b34
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_methlist: 0xcc8
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x930
+  __TEXT.__cstring: 0x1177
   __TEXT.__oslogstring: 0x57
   __TEXT.__gcc_except_tab: 0xa4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x348
-  __TEXT.__objc_classname: 0xcb
-  __TEXT.__objc_methname: 0x136b
-  __TEXT.__objc_methtype: 0x568
-  __TEXT.__objc_stubs: 0x1260
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__objc_classname: 0x148
+  __TEXT.__objc_methname: 0x1948
+  __TEXT.__objc_methtype: 0x786
+  __TEXT.__objc_stubs: 0x1740
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x500
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x190
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x1e98
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x188
+  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x8e0
+  __AUTH_CONST.__objc_const: 0x1ee8
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x2a8
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/IASUtilities.framework/Versions/A/IASUtilities
   - /System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0039AA81-DD90-3FCC-BC8C-F704B4315C63
-  Functions: 219
-  Symbols:   585
-  CStrings:  392
+  UUID: 688F6607-CFFB-36E7-926A-C82A5DE06B21
+  Functions: 279
+  Symbols:   733
+  CStrings:  539
 
Symbols:
+ +[MBSAConnection sharedConnection].cold.1
+ -[MBSAConnection activateProximityServerWithCompletion:]
+ -[MBSAConnection createTeslaUsersWithInfo:prepareFirstAdminForResume:completionBlock:]
+ -[MBSAConnection invalidateProximitySessionWithCompletion:]
+ -[MBSAConnection overrideSASInformation:]
+ -[MBSAConnection prepareForAppleAccountSignInWithCompletion:]
+ -[MBSAConnection preserveAnalyticsData:withCompletionBlock:]
+ -[MBSAConnection proximityDisplayCode:]
+ -[MBSAConnection proximityHandler]
+ -[MBSAConnection proximityPINCodeTypeChanged:]
+ -[MBSAConnection proximitySessionLost]
+ -[MBSAConnection proximitySessionReady:]
+ -[MBSAConnection removeTOSRequiredCookie:]
+ -[MBSAConnection retrieveAnalyticsDataWithCompletionBlock:]
+ -[MBSAConnection retrieveMessageSessionWithCompletion:]
+ -[MBSAConnection setProximityHandler:]
+ -[MBSAConnection setTOSRequiredCookie:]
+ -[MBSAConnection setTestingModeEnablement:]
+ -[MBSAConnection setupiCloudPasswordResetWithCompletion:]
+ -[SACookieHandling appleLaunchMigrationCookieIsSet]
+ -[SACookieHandling appleSetupResumeCookieIsSet]
+ -[SACookieHandling macBuddyCookieIsSet]
+ -[SACookieHandling repairMacBuddyCookieIfNeededWithSoftwareUpdateManager:]
+ -[SACookieHandling termsOfServiceCookieIsSet]
+ -[SALaunchController .cxx_destruct]
+ -[SALaunchController cookieHandler]
+ -[SALaunchController initWithCookieHandler:softwareUpdateManager:]
+ -[SALaunchController init]
+ -[SALaunchController launchReason]
+ -[SALaunchController repairMacBuddyCookieIfNeeded]
+ -[SALaunchController softwareUpdateManager]
+ -[SASetupOverrideClient .cxx_destruct]
+ -[SASetupOverrideClient changeProximityPasswordType:completionBlock:]
+ -[SASetupOverrideClient displayProxmimityPinCode:completionBlock:]
+ -[SASetupOverrideClient init]
+ -[SASetupOverrideClient mbsaConnection]
+ -[SASetupOverrideClient mbsaProxy]
+ -[SASetupOverrideClient overrideProximityHandlerWithCompletionHandler:]
+ -[SASetupOverrideClient proximityServerIsActiveWithCompletionBlock:]
+ -[SASetupOverrideClient proximitySessionLostWithCompletionBlock:]
+ -[SASetupOverrideClient proximitySessionReadyWithCompletionBlock:]
+ -[SASetupOverrideClient sendProximitySASInformation:completionBlock:]
+ -[SASetupOverrideClient setMbsaConnection:]
+ -[SASoftwareUpdateManager forceDeferredMandatoryUpdate].cold.1
+ -[SASoftwareUpdateManager forceNoMandatoryUpdateFound].cold.1
+ OBJC_IVAR_$_MBSAConnection._proximityHandler
+ OBJC_IVAR_$_SALaunchController._cookieHandler
+ OBJC_IVAR_$_SALaunchController._softwareUpdateManager
+ OBJC_IVAR_$_SASetupOverrideClient._mbsaConnection
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFPreferencesCopyValue
+ _CFRelease
+ _MBMigrationBuddyCookieIsSet
+ _MBRemoveTOSRequiredCookie
+ _MBSetTOSRequiredCookie
+ _MBTOSRequiredCookieExists
+ _OBJC_CLASS_$_ADMUser
+ _OBJC_CLASS_$_SACookieHandling
+ _OBJC_CLASS_$_SASetupOverrideClient
+ _OBJC_METACLASS_$_SACookieHandling
+ _OBJC_METACLASS_$_SASetupOverrideClient
+ __45-[MBSAConnection connectionWithErrorHandler:]_block_invoke.37
+ __OBJC_$_INSTANCE_METHODS_SACookieHandling
+ __OBJC_$_INSTANCE_METHODS_SASetupOverrideClient
+ __OBJC_$_INSTANCE_VARIABLES_SALaunchController
+ __OBJC_$_INSTANCE_VARIABLES_SASetupOverrideClient
+ __OBJC_$_PROP_LIST_SALaunchController
+ __OBJC_$_PROP_LIST_SASetupOverrideClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MBSAServerOverrideProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SACookieHandlingProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SASoftwareUpdateManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MBSAServerOverrideProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SACookieHandlingProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SASoftwareUpdateManagerProtocol
+ __OBJC_$_PROTOCOL_REFS_MBSAServerOverrideProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SACookieHandling
+ __OBJC_CLASS_PROTOCOLS_$_SASoftwareUpdateManager
+ __OBJC_CLASS_RO_$_SACookieHandling
+ __OBJC_CLASS_RO_$_SASetupOverrideClient
+ __OBJC_LABEL_PROTOCOL_$_MBSAServerOverrideProtocol
+ __OBJC_LABEL_PROTOCOL_$_SACookieHandlingProtocol
+ __OBJC_LABEL_PROTOCOL_$_SASoftwareUpdateManagerProtocol
+ __OBJC_METACLASS_RO_$_SACookieHandling
+ __OBJC_METACLASS_RO_$_SASetupOverrideClient
+ __OBJC_PROTOCOL_$_MBSAServerOverrideProtocol
+ __OBJC_PROTOCOL_$_SACookieHandlingProtocol
+ __OBJC_PROTOCOL_$_SASoftwareUpdateManagerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_MBSAServerOverrideProtocol
+ ___29-[SASetupOverrideClient init]_block_invoke
+ ___29-[SASetupOverrideClient init]_block_invoke_2
+ ___39-[MBSAConnection setTOSRequiredCookie:]_block_invoke
+ ___42-[MBSAConnection removeTOSRequiredCookie:]_block_invoke
+ ___43-[MBSAConnection setTestingModeEnablement:]_block_invoke
+ ___55-[MBSAConnection retrieveMessageSessionWithCompletion:]_block_invoke
+ ___56-[MBSAConnection activateProximityServerWithCompletion:]_block_invoke
+ ___57-[MBSAConnection setupiCloudPasswordResetWithCompletion:]_block_invoke
+ ___59-[MBSAConnection invalidateProximitySessionWithCompletion:]_block_invoke
+ ___59-[MBSAConnection retrieveAnalyticsDataWithCompletionBlock:]_block_invoke
+ ___60-[MBSAConnection preserveAnalyticsData:withCompletionBlock:]_block_invoke
+ ___61-[MBSAConnection prepareForAppleAccountSignInWithCompletion:]_block_invoke
+ ___86-[MBSAConnection createTeslaUsersWithInfo:prepareFirstAdminForResume:completionBlock:]_block_invoke
+ __block_literal_global.17
+ __block_literal_global.44
+ __block_literal_global.49
+ __block_literal_global.51
+ __block_literal_global.53
+ __block_literal_global.80
+ _kCFPreferencesAnyUser
+ _kCFPreferencesCurrentHost
+ _objc_msgSend$activateProximityServerWithCompletion:
+ _objc_msgSend$allLocalUsers
+ _objc_msgSend$appleLaunchMigrationCookieIsSet
+ _objc_msgSend$appleSetupResumeCookieIsSet
+ _objc_msgSend$changeProximityPasswordType:completionBlock:
+ _objc_msgSend$cookieHandler
+ _objc_msgSend$createTeslaUsersWithInfo:prepareFirstAdminForResume:completionBlock:
+ _objc_msgSend$displayProxmimityPinCode:completionBlock:
+ _objc_msgSend$initWithCookieHandler:softwareUpdateManager:
+ _objc_msgSend$invalidateProximitySessionWithCompletion:
+ _objc_msgSend$isSetupRunningForSetupUser
+ _objc_msgSend$launchReason
+ _objc_msgSend$macBuddyCookieIsSet
+ _objc_msgSend$mbsaConnection
+ _objc_msgSend$mbsaProxy
+ _objc_msgSend$overrideProximityHandlerWithCompletionHandler:
+ _objc_msgSend$overrideSASInformation:
+ _objc_msgSend$prepareForAppleAccountSignInWithCompletion:
+ _objc_msgSend$preserveAnalyticsData:withCompletionBlock:
+ _objc_msgSend$proximityDisplayCode:
+ _objc_msgSend$proximityHandler
+ _objc_msgSend$proximityPINCodeTypeChanged:
+ _objc_msgSend$proximityServerIsActiveWithCompletionBlock:
+ _objc_msgSend$proximitySessionLost
+ _objc_msgSend$proximitySessionLostWithCompletionBlock:
+ _objc_msgSend$proximitySessionReady:
+ _objc_msgSend$proximitySessionReadyWithCompletionBlock:
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$removeTOSRequiredCookie:
+ _objc_msgSend$repairMacBuddyCookieIfNeededWithSoftwareUpdateManager:
+ _objc_msgSend$retrieveAnalyticsDataWithCompletionBlock:
+ _objc_msgSend$retrieveMessageSessionWithCompletion:
+ _objc_msgSend$sendProximitySASInformation:completionBlock:
+ _objc_msgSend$setMbsaConnection:
+ _objc_msgSend$setTOSRequiredCookie:
+ _objc_msgSend$setTestingModeEnablement:
+ _objc_msgSend$setupiCloudPasswordResetWithCompletion:
+ _objc_msgSend$softwareUpdateManager
+ _objc_msgSend$termsOfServiceCookieIsSet
+ _objc_msgSend$userID
- -[MBSAConnection createTeslaUsersWithInfo:completionBlock:]
- __45-[MBSAConnection connectionWithErrorHandler:]_block_invoke.25
- ___59-[MBSAConnection createTeslaUsersWithInfo:completionBlock:]_block_invoke
- __block_literal_global.21
- __block_literal_global.29
- __block_literal_global.5
- __block_literal_global.7
- _objc_msgSend$createTeslaUsersWithInfo:completionBlock:
CStrings:
+ "!allowOriginalBehavior checking if the machine has additional accounts"
+ "\""
+ "-[MBSAConnection activateProximityServerWithCompletion:]_block_invoke"
+ "-[MBSAConnection connectionWithErrorHandler:]_block_invoke"
+ "-[MBSAConnection invalidateProximitySessionWithCompletion:]_block_invoke"
+ "-[MBSAConnection overrideSASInformation:]"
+ "-[MBSAConnection prepareForAppleAccountSignInWithCompletion:]_block_invoke"
+ "-[MBSAConnection proximityDisplayCode:]"
+ "-[MBSAConnection proximityPINCodeTypeChanged:]"
+ "-[MBSAConnection proximitySessionLost]"
+ "-[MBSAConnection proximitySessionReady:]"
+ "-[MBSAConnection retrieveMessageSessionWithCompletion:]_block_invoke"
+ "-[MBSAConnection setTestingModeEnablement:]_block_invoke"
+ "-[SACookieHandling repairMacBuddyCookieIfNeededWithSoftwareUpdateManager:]"
+ "-[SALaunchController launchReason]"
+ "-[SALaunchController needsToRun]"
+ "-[SASetupOverrideClient init]"
+ "-[SASetupOverrideClient init]_block_invoke"
+ "-[SASetupOverrideClient init]_block_invoke_2"
+ "/var/db/.AppleSetupTermsOfService"
+ "@\"<ProximitySetupConnectionHandler>\""
+ "@\"<SACookieHandlingProtocol>\""
+ "@\"<SASoftwareUpdateManagerProtocol>\""
+ "@32@0:8@16@24"
+ "AllowMacBuddyWithExistingAccounts"
+ "B24@0:8@\"<SASoftwareUpdateManagerProtocol>\"16"
+ "BOOL MBTOSRequiredCookieExists()"
+ "Creating MBSAServerOverride connection"
+ "Debug value for key %@ is %@"
+ "Deferred Mandatory Update: allowOriginalBehavior"
+ "Error activating proximity: %@"
+ "Error fetching proximity session: %@"
+ "Error invalidating proximity: %@"
+ "Error launching mbsystemadmininstration: %@"
+ "Error setting testing mode: %@"
+ "Found local users ignore missing setup done"
+ "Internal build, allowing macbuddy reset: %d"
+ "MBSAServerOverrideProtocol"
+ "No local users found"
+ "Removed TOS required cookie with success: %i, error: %@"
+ "SACookieHandling"
+ "SACookieHandlingProtocol"
+ "SASetupOverrideClient"
+ "SASoftwareUpdateManagerProtocol"
+ "Setting TOS cookie"
+ "Setup Resume allowOriginalBehavior"
+ "Setup is already currently running as the setup user, does not need to run"
+ "Setup launch reason: Migration"
+ "Setup launch reason: Migration Resume"
+ "Setup launch reason: deferred mandatory update"
+ "Setup launch reason: initial Setup"
+ "Setup launch reason: terms and conditions"
+ "Somehow attempting to call %s without a proximity manager"
+ "System requires license: %i"
+ "T@\"<ProximitySetupConnectionHandler>\",W,V_proximityHandler"
+ "T@\"<SACookieHandlingProtocol>\",R,V_cookieHandler"
+ "T@\"<SASoftwareUpdateManagerProtocol>\",R,V_softwareUpdateManager"
+ "T@\"NSXPCConnection\",&,V_mbsaConnection"
+ "_cookieHandler"
+ "_mbsaConnection"
+ "_proximityHandler"
+ "_softwareUpdateManager"
+ "activateProximityServerWithCompletion:"
+ "allLocalUsers"
+ "appleLaunchMigrationCookieIsSet"
+ "appleSetupResumeCookieIsSet"
+ "changeProximityPasswordType:completionBlock:"
+ "com.apple.loginwindow"
+ "com.apple.mbsystemadministration.override"
+ "cookieHandler"
+ "createTeslaUsersWithInfo:prepareFirstAdminForResume:completionBlock:"
+ "displayProxmimityPinCode:completionBlock:"
+ "id  _Nullable MBDebugInitializationDictValueForKey(NSString * _Nonnull __strong)"
+ "initWithCookieHandler:softwareUpdateManager:"
+ "invalidateProximitySessionWithCompletion:"
+ "launchReason"
+ "macBuddyCookieIsSet"
+ "mbsaConnection"
+ "mbsaProxy"
+ "overrideProximityHandlerWithCompletionHandler:"
+ "overrideSASInformation:"
+ "prepareForAppleAccountSignInWithCompletion:"
+ "preserveAnalyticsData:withCompletionBlock:"
+ "proximityDisplayCode:"
+ "proximityHandler"
+ "proximityPINCodeTypeChanged:"
+ "proximityServerIsActiveWithCompletionBlock:"
+ "proximitySessionLost"
+ "proximitySessionLostWithCompletionBlock:"
+ "proximitySessionReady:"
+ "proximitySessionReadyWithCompletionBlock:"
+ "remoteObjectProxy"
+ "removeTOSRequiredCookie:"
+ "repairMacBuddyCookieIfNeeded"
+ "repairMacBuddyCookieIfNeededWithSoftwareUpdateManager:"
+ "retrieveAnalyticsDataWithCompletionBlock:"
+ "retrieveMessageSessionWithCompletion:"
+ "sendProximitySASInformation:completionBlock:"
+ "setMbsaConnection:"
+ "setProximityHandler:"
+ "setTOSRequiredCookie:"
+ "setTestingModeEnablement:"
+ "setupiCloudPasswordResetWithCompletion:"
+ "softwareUpdateManager"
+ "termsOfServiceCookieIsSet"
+ "userID"
+ "v20@0:8i16"
+ "v24@0:8@\"CUMessageSession\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@\"SASProximityInformation\"16"
+ "v24@0:8@?<v@?@\"CUMessageSession\">16"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v28@0:8i16@?20"
+ "v28@0:8i16@?<v@?@\"NSError\">20"
+ "v32@0:8@\"NSArray\"16@?<v@?B>24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"SASProximityInformation\"16@?<v@?@\"NSError\">24"
+ "v36@0:8@\"NSArray\"16B24@?<v@?BB>28"
+ "v36@0:8@16B24@?28"
+ "void MBRemoveTOSRequiredCookie()"
+ "void MBSetTOSRequiredCookie()"
- "createTeslaUsersWithInfo:completionBlock:"
- "v32@0:8@\"NSArray\"16@?<v@?BB>24"

```
