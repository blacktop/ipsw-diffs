## SetupAssistantSpringboard

> `/System/Library/CoreServices/Setup Assistant.app/Contents/SharedSupport/SetupAssistantSpringboard`

```diff

-7217.1.0.0.0
-  __TEXT.__text: 0x636c
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x448
-  __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__cstring: 0x9ab
-  __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methtype: 0x574
-  __TEXT.__objc_methname: 0x11a6
+7407.4.12.204.0
+  __TEXT.__text: 0x9048
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_stubs: 0x15e0
+  __TEXT.__objc_methlist: 0xb98
+  __TEXT.__const: 0x48
+  __TEXT.__gcc_except_tab: 0x1c0
+  __TEXT.__cstring: 0x1404
+  __TEXT.__objc_classname: 0x11f
+  __TEXT.__objc_methtype: 0x6db
+  __TEXT.__objc_methname: 0x1779
+  __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__oslogstring: 0x57
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x310
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x2e0
-  __DATA_CONST.__cfstring: 0x700
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__unwind_info: 0x400
+  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x3e0
+  __DATA_CONST.__cfstring: 0xb00
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x1c50
-  __DATA.__objc_selrefs: 0x468
-  __DATA.__objc_ivar: 0x18
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x188
-  __DATA.__bss: 0x33
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x1a18
+  __DATA.__objc_selrefs: 0x688
+  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_data: 0x280
+  __DATA.__data: 0x2a8
+  __DATA.__bss: 0x63
+  - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa
   - /System/Library/Frameworks/Collaboration.framework/Versions/A/Collaboration
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore
   - /System/Library/PrivateFrameworks/PreferencePanesSupport.framework/Versions/A/PreferencePanesSupport
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/StorageKit.framework/Versions/A/StorageKit
   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration
   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34222103-9299-365E-8674-BA8824607B9D
-  Functions: 202
-  Symbols:   77
-  CStrings:  391
+  UUID: 4C693609-6360-3282-B1BF-2B67EDB05F06
+  Functions: 270
+  Symbols:   98
+  CStrings:  554
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFPreferencesCopyValue
+ _CFRelease
+ _NSWorkspaceDidLaunchApplicationNotification
+ _NSWorkspaceDidTerminateApplicationNotification
+ _OBJC_CLASS_$_ADMUser
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_NSWorkspace
+ ___error
+ __sl_dlopen
+ _free
+ _kCFPreferencesAnyUser
+ _kCFPreferencesCurrentHost
+ _malloc_type_malloc
+ _objc_getClass
+ _objc_retainBlock
+ _strcmp
+ _sysctl
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
+ "-[SASoftwareUpdateManager forceDeferredMandatoryUpdate]_block_invoke"
+ "-[SASoftwareUpdateManager forceNoMandatoryUpdateFound]_block_invoke"
+ "-[SASoftwareUpdateManager requiresDeferredMandatoryUpdate]"
+ "/System/Library/PrivateFrameworks/OSUpdate.framework/Contents/MacOS/OSUpdate"
+ "/var/db/.AppleSetupTermsOfService"
+ "@\"<ProximitySetupConnectionHandler>\""
+ "@\"<SACookieHandlingProtocol>\""
+ "@\"<SASoftwareUpdateManagerProtocol>\""
+ "@32@0:8@16@24"
+ "AllowMacBuddyWithExistingAccounts"
+ "B24@0:8@\"<SASoftwareUpdateManagerProtocol>\"16"
+ "BOOL MBTOSRequiredCookieExists()"
+ "Class getSUOSUMacBuddyControllerClass(void)_block_invoke"
+ "Debug flag set. Checking for deferred mandatory update"
+ "Debug flag set. Forcing mandatory update not found"
+ "Debug value for key %@ is %@"
+ "Deferred Mandatory Update: allowOriginalBehavior"
+ "Dock"
+ "Error activating proximity: %@"
+ "Error checking for deferred mandatory update: %@"
+ "Error fetching proximity session: %@"
+ "Error invalidating proximity: %@"
+ "Error launching mbsystemadmininstration: %@"
+ "Error setting testing mode: %@"
+ "Found local users ignore missing setup done"
+ "Internal build, allowing macbuddy reset: %d"
+ "No local users found"
+ "Q20@0:8I16"
+ "Removed TOS required cookie with success: %i, error: %@"
+ "Requires deferred mandatory update: %i"
+ "SACookieHandling"
+ "SACookieHandlingProtocol"
+ "SALaunchController"
+ "SALaunchProtocol"
+ "SASoftwareUpdateManager"
+ "SASoftwareUpdateManager.m"
+ "SASoftwareUpdateManagerProtocol"
+ "SAUserSetupState"
+ "SUOSUMacBuddyController"
+ "Setting TOS cookie"
+ "Setup Assistant"
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
+ "Unable to find class %s"
+ "_cookieHandler"
+ "_proximityHandler"
+ "_softwareUpdateManager"
+ "activateProximityServerWithCompletion:"
+ "addObserverForName:object:queue:usingBlock:"
+ "allLocalUsers"
+ "appleLaunchMigrationCookieIsSet"
+ "appleSetupResumeCookieIsSet"
+ "com.apple.setupassistant.done"
+ "cookieHandler"
+ "createTeslaUsersWithInfo:prepareFirstAdminForResume:completionBlock:"
+ "currentHandler"
+ "defaultCenter"
+ "forceDeferredMandatoryUpdate"
+ "forceNoMandatoryUpdateFound"
+ "getSetupStateForUser:"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "id  _Nullable MBDebugInitializationDictValueForKey(NSString * _Nonnull __strong)"
+ "initWithCookieHandler:softwareUpdateManager:"
+ "invalidateProximitySessionWithCompletion:"
+ "isSetupRunningForSetupUser"
+ "launchReason"
+ "macBuddyCookieIsSet"
+ "mb_debug_deferredmandatoryupdate"
+ "mb_debug_forceupdatenotfound"
+ "needsToRun"
+ "notificationCenter"
+ "notifyWhenUserIsSetup:withCompletionBlock:"
+ "overrideSASInformation:"
+ "prepareForAppleAccountSignInWithCompletion:"
+ "preserveAnalyticsData:withCompletionBlock:"
+ "proximityDisplayCode:"
+ "proximityHandler"
+ "proximityPINCodeTypeChanged:"
+ "proximitySessionLost"
+ "proximitySessionReady:"
+ "removeObserver:"
+ "removeTOSRequiredCookie:"
+ "repairMacBuddyCookieIfNeeded"
+ "repairMacBuddyCookieIfNeededWithSoftwareUpdateManager:"
+ "requiresDeferredMandatoryUpdate"
+ "retrieveAnalyticsDataWithCompletionBlock:"
+ "retrieveMessageSessionWithCompletion:"
+ "setProximityHandler:"
+ "setTOSRequiredCookie:"
+ "setTestingModeEnablement:"
+ "setupiCloudPasswordResetWithCompletion:"
+ "sharedWorkspace"
+ "softlink:o:path:/System/Library/PrivateFrameworks/OSUpdate.framework/OSUpdate"
+ "softwareUpdateManager"
+ "termsOfServiceCookieIsSet"
+ "updateFromFactoryVersionRequired:withError:"
+ "userID"
+ "v16@?0@\"NSNotification\"8"
+ "v20@0:8i16"
+ "v24@0:8@\"CUMessageSession\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@\"SASProximityInformation\"16"
+ "v24@0:8@?<v@?@\"CUMessageSession\">16"
+ "v32@0:8@\"NSArray\"16@?<v@?B>24"
+ "v36@0:8@\"NSArray\"16B24@?<v@?BB>28"
+ "v36@0:8@16B24@?28"
+ "void *OSUpdateLibrary(void)"
+ "void GetBuddyType(MBPrimaryType *, MBSecondaryType *, NSDictionary *__autoreleasing *, __strong id<SALaunchProtocol>)"
+ "void MBRemoveTOSRequiredCookie()"
+ "void MBSetTOSRequiredCookie()"
- "-DeferredMandatoryUpdate"
- "-MigrationBuddyYes"
- "createTeslaUsersWithInfo:completionBlock:"
- "v32@0:8@\"NSArray\"16@?<v@?BB>24"
- "void GetBuddyType(MBPrimaryType *, MBSecondaryType *, NSDictionary *__autoreleasing *)"

```
