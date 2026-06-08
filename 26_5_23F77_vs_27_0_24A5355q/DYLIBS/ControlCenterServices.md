## ControlCenterServices

> `/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices`

```diff

-655.10.5.3.0
-  __TEXT.__text: 0xea44
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0xd94
+696.0.1.0.0
+  __TEXT.__text: 0xf31c
+  __TEXT.__objc_methlist: 0xe04
   __TEXT.__const: 0x9a
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__cstring: 0x1949
-  __TEXT.__oslogstring: 0x11a4
-  __TEXT.__unwind_info: 0x4f0
-  __TEXT.__objc_classname: 0x1e0
-  __TEXT.__objc_methname: 0x293a
-  __TEXT.__objc_methtype: 0x60c
-  __TEXT.__objc_stubs: 0x1de0
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x878
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__cstring: 0x1a09
+  __TEXT.__oslogstring: 0x1404
+  __TEXT.__unwind_info: 0x520
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x890
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b0
+  __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x278
-  __AUTH_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0x198
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x1460
-  __AUTH_CONST.__objc_const: 0x1440
+  __AUTH_CONST.__cfstring: 0x14e0
+  __AUTH_CONST.__objc_const: 0x1460
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH.__objc_data: 0x48
   __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x2b8
   __DATA_DIRTY.__objc_data: 0x398
-  __DATA_DIRTY.__data: 0x30
+  __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__bss: 0xa8
-  __DATA_DIRTY.__common: 0x38
+  __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B8956B1D-FA0E-3D89-B623-E0BBE152255E
-  Functions: 396
-  Symbols:   1473
-  CStrings:  912
+  UUID: 52025277-6CA8-3BA5-A2CB-11D7628A4463
+  Functions: 420
+  Symbols:   1531
+  CStrings:  451
 
Symbols:
+ -[CCSControlCenterOperationService requestGridContentsWithCompletionHandler:]
+ -[CCSControlCenterService requestGridContentsWithCompletionHandler:]
+ -[CCSControlCenterService resizeIconElement:completionHandler:]
+ -[CCSRemoteServiceConnection requestGridContentsWithCompletionHandler:]
+ -[CCSRemoteServiceConnection requestGridContentsWithCompletionHandler:].cold.1
+ -[CCSRemoteServiceConnection resizeIconElement:completionHandler:]
+ -[CCSRemoteServiceProvider requestGridContentsWithCompletionHandler:]
+ -[CCSRemoteServiceProvider requestGridContentsWithCompletionHandler:].cold.1
+ -[CCSRemoteServiceProvider resizeIconElement:completionHandler:]
+ -[CCSRemoteServiceProvider resizeIconElement:completionHandler:].cold.1
+ -[NSXPCConnection(CCSEntitlements) ccs_hasEntitlementForResizingIconElements]
+ GCC_except_table28
+ _OBJC_CLASS_$_OS_os_log
+ ___64-[CCSRemoteServiceProvider resizeIconElement:completionHandler:]_block_invoke
+ ___66-[CCSRemoteServiceConnection resizeIconElement:completionHandler:]_block_invoke
+ ___66-[CCSRemoteServiceConnection resizeIconElement:completionHandler:]_block_invoke.47
+ ___66-[CCSRemoteServiceConnection resizeIconElement:completionHandler:]_block_invoke_2
+ ___66-[CCSRemoteServiceConnection resizeIconElement:completionHandler:]_block_invoke_2.48
+ ___66-[CCSRemoteServiceConnection resizeIconElement:completionHandler:]_block_invoke_3
+ ___66-[CCSRemoteServiceConnection resizeIconElement:completionHandler:]_block_invoke_3.cold.1
+ ___71-[CCSRemoteServiceConnection requestGridContentsWithCompletionHandler:]_block_invoke
+ ___71-[CCSRemoteServiceConnection requestGridContentsWithCompletionHandler:]_block_invoke.49
+ ___71-[CCSRemoteServiceConnection requestGridContentsWithCompletionHandler:]_block_invoke_2
+ ___71-[CCSRemoteServiceConnection requestGridContentsWithCompletionHandler:]_block_invoke_2.50
+ ___71-[CCSRemoteServiceConnection requestGridContentsWithCompletionHandler:]_block_invoke_3
+ ___71-[CCSRemoteServiceConnection requestGridContentsWithCompletionHandler:]_block_invoke_3.cold.1
+ ___72-[CCSRemoteServiceConnection resetToDefaultLayoutWithCompletionHandler:]_block_invoke.51
+ ___72-[CCSRemoteServiceConnection resetToDefaultLayoutWithCompletionHandler:]_block_invoke_2.52
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_ControlCenterServices
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_ControlCenterServices
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_ControlCenterServices
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_ControlCenterServices
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$ccs_hasEntitlementForResizingIconElements
+ _objc_msgSend$requestGridContentsWithCompletionHandler:
+ _objc_msgSend$requestGridContentsWithOperationService:completionHandler:
+ _objc_msgSend$resizeIconElement:completionHandler:
+ _objc_msgSend$restrictionReason
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _swift_bridgeObjectRetain
- GCC_except_table25
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___72-[CCSRemoteServiceConnection resetToDefaultLayoutWithCompletionHandler:]_block_invoke.47
- ___72-[CCSRemoteServiceConnection resetToDefaultLayoutWithCompletionHandler:]_block_invoke_2.48
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- _objc_retain_x25
CStrings:
+ "CCSIconElementRequestErrorCodeFailedToResizeIconElement"
+ "CCSIconElementRequestIntentResize"
+ "CCSModuleSizeLargeWide"
+ "Failed to request grid contents error=%@"
+ "Failed to resize icon element for CCSIconElementRequest error=%@"
+ "Handling Control Center operation type %ld"
+ "Handling icon element request %{public}@"
+ "Missing entitlement for listing grid contents"
+ "Request grid contents"
+ "Requesting icon element state for %{public}@"
+ "Resetting Control Center to default layout"
+ "Resizing icon element %{public}@"
+ "The application-identifier in your entitlements file is not allow-listed for resizing icon elements"
+ "com.apple.ControlCenter.RemoteServiceConnection.requestGridContents"
+ "com.apple.ControlCenter.RemoteServiceConnection.resizeIconElement"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<BSDefaultObserver>\""
- "@\"<CCSControlCenterOperationServiceDelegate>\""
- "@\"CCSControlCenterOperationService\""
- "@\"CCSModuleRepository\""
- "@\"CCSModuleSettingsProvider\""
- "@\"CCSRemoteServiceConnection\""
- "@\"INIntent\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSHashTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8o^Q16"
- "@28@0:8B16B20B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@48@0:8q16@24@32Q40"
- "@48@0:8q16@24@32q40"
- "@64@0:8q16@24Q32@40@48Q56"
- "@80@0:8@16@24@32@40@48@56Q64@72"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "CCSControlCenterDefaults"
- "CCSControlCenterOperationService"
- "CCSControlCenterService"
- "CCSControlCenterServicesManager"
- "CCSEntitlements"
- "CCSIconElementRequest"
- "CCSModuleMetadata"
- "CCSModulePresentationOptions"
- "CCSModuleRepository"
- "CCSModuleSettingsProvider"
- "CCSRemoteServiceConnection"
- "CCSRemoteServiceProvider"
- "CCSRemoteServiceServerProtocol"
- "CCSUsageMetrics"
- "LSApplicationWorkspaceObserverProtocol"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<CCSControlCenterOperationServiceDelegate>\",W,N,V_delegate"
- "T@\"INIntent\",&,N,V_intentConfiguration"
- "T@\"NSArray\",R,C,N"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,C,N,V_requiredDeviceCapabilities"
- "T@\"NSSet\",R,C,N,V_requiredDeviceIncapabilities"
- "T@\"NSSet\",R,C,N,V_supportedDeviceFamilies"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_associatedBundleIdentifier"
- "T@\"NSString\",R,C,N,V_associatedBundleMinimumVersion"
- "T@\"NSString\",R,C,N,V_containerBundleIdentifier"
- "T@\"NSString\",R,C,N,V_controlKind"
- "T@\"NSString\",R,C,N,V_extensionBundleIdentifier"
- "T@\"NSString\",R,C,N,V_moduleIdentifier"
- "T@\"NSURL\",R,C,N,V_moduleBundleURL"
- "TB,D,N"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_animateDismissal"
- "TB,R,N,V_animatePresentation"
- "TB,R,N,V_blurBackground"
- "TQ,D,N"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_controlType"
- "TQ,R,N,V_size"
- "TQ,R,N,V_visibilityPreference"
- "Tq,R,N,V_elementType"
- "Tq,R,N,V_intent"
- "Tq,R,N,V_moduleSize"
- "URLByAppendingPathComponent:"
- "URLForResource:withExtension:"
- "Vv16@0:8"
- "^{MGNotificationTokenStruct=}"
- "^{_NSZone=}16@0:8"
- "_allModuleMetadataByIdentifier"
- "_allowedModuleIdentifiers"
- "_animateDismissal"
- "_animatePresentation"
- "_applicationsDidChange:"
- "_associatedBundleIdentifier"
- "_associatedBundleMinimumVersion"
- "_availableModuleIdentifiers"
- "_bindAndRegisterDefaults"
- "_bindProperty:withDefaultKey:toDefaultValue:options:"
- "_blurBackground"
- "_callOutQueue"
- "_configurationChangedSource"
- "_configurationDirectoryURL"
- "_configurationFileURL"
- "_connection"
- "_containerBundleIdentifier"
- "_continuousExposeEnabled"
- "_controlCenterOperationService"
- "_controlKind"
- "_controlSizeString:"
- "_controlType"
- "_controlTypeString:"
- "_defaultEnabledModuleOrder"
- "_defaultFixedModuleIdentifiers"
- "_defaultModuleDirectories"
- "_defaultModuleIdentifierAllowedList"
- "_defaultPresentationGesture"
- "_defaultUserEnabledFixedModuleIdentifiers"
- "_defaultUserEnabledModuleIdentifiers"
- "_delegate"
- "_deviceFamily"
- "_directoryURLs"
- "_elementType"
- "_extensionBundleIdentifier"
- "_ignoreAllowedList"
- "_init"
- "_initWithDirectoryURLs:allowedModuleIdentifiers:"
- "_initWithDomain:"
- "_initWithModuleIdentifier:supportedDeviceFamilies:requiredDeviceCapabilities:requiredDeviceIncapabilities:associatedBundleIdentifier:associatedBundleMinimumVersion:visibilityPreference:moduleBundleURL:"
- "_intent"
- "_intentConfiguration"
- "_interestingBundleIdentifiers"
- "_internalDefaultsObserver"
- "_listener"
- "_loadableModuleIdentifiers"
- "_mobileGestaltNotificationToken"
- "_moduleBundleURL"
- "_moduleIdentifier"
- "_moduleRepository"
- "_moduleSize"
- "_observers"
- "_orderedFixedModuleIdentifiers"
- "_orderedUserEnabledFixedModuleIdentifiers"
- "_orderedUserEnabledModuleIdentifiers"
- "_presentationEndpoints"
- "_queue"
- "_queue_arrayContainsInterestingApplicationProxy:"
- "_queue_associatedBundleIdentifiersForModuleMetadata:"
- "_queue_filterModuleMetadataByAssociatedBundleAvailability:"
- "_queue_filterModuleMetadataByGestalt:"
- "_queue_filterModuleMetadataByVisibilityPreference:"
- "_queue_gestaltQuestionsForModuleMetadata:"
- "_queue_handleConfigurationFileUpdate"
- "_queue_loadAllModuleMetadata"
- "_queue_loadSettings"
- "_queue_moduleIdentifiersForMetadata:"
- "_queue_registerForInternalPreferenceChanges"
- "_queue_registerForVisiblityPreferenceChanges"
- "_queue_runBlockOnListeners:"
- "_queue_runBlockOnObservers:"
- "_queue_saveSettings"
- "_queue_sendConfigurationFileUpdateMessageToObservers"
- "_queue_setAndSaveOrderedUserEnabledModuleIdentifiers:previousOrderedUserEnabledModuleIdentifiers:"
- "_queue_setIgnoreAllowedList:"
- "_queue_startMonitoringConfigurationUpdates"
- "_queue_startObservingMobileGestaltQuestions:withChangeHandler:"
- "_queue_stopMonitoringConfigurationUpdates"
- "_queue_stopObservingGestaltQuestions"
- "_queue_unregisterForInternalPreferenceChanges"
- "_queue_unregisterForVisiblityPreferenceChanges"
- "_queue_updateAllModuleMetadata"
- "_queue_updateAllModuleMetadataForAllModuleMetadata:"
- "_queue_updateAvailableModuleMetadata"
- "_queue_updateAvailableModuleMetadataForAllModuleMetadata:"
- "_queue_updateGestaltQuestionsForModuleMetadata:"
- "_queue_updateInterestingBundleIdentifiersForModuleMetadata:"
- "_queue_updateLoadableModuleMetadata"
- "_queue_updateLoadableModuleMetadataForAvailableModuleMetadata:"
- "_readSettingsWithVersion:"
- "_requiredCapabilitiesForInfoDictionary:"
- "_requiredDeviceCapabilities"
- "_requiredDeviceIncapabilities"
- "_requiredIncapabilitiesForInfoDictionary:"
- "_settingsProvider"
- "_size"
- "_supportedDeviceFamilies"
- "_supportedDeviceFamiliesForBundleInfoDictionary:"
- "_updateAvailableModuleMetadata"
- "_userDisabledModuleIdentifiers"
- "_visibilityPreference"
- "_writeOrderedIdentifiers:userEnabledFixedIdentifiers:userDisabledIdentifiers:"
- "_xpcConnection"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "allKeys"
- "allObjects"
- "allValues"
- "appendBool:"
- "appendBool:withName:"
- "appendObject:"
- "appendObject:withName:"
- "appendString:withName:"
- "appendUnsignedInteger:"
- "applicationIconDidChange:"
- "applicationInstallsArePrioritized:arePaused:"
- "applicationInstallsDidCancel:"
- "applicationInstallsDidChange:"
- "applicationInstallsDidPause:"
- "applicationInstallsDidPrioritize:"
- "applicationInstallsDidResume:"
- "applicationInstallsDidStart:"
- "applicationInstallsDidUpdateIcon:"
- "applicationState"
- "applicationStateDidChange:"
- "applicationsDidChangePersonas:"
- "applicationsDidFailToInstall:"
- "applicationsDidFailToUninstall:"
- "applicationsDidInstall:"
- "applicationsDidUninstall:"
- "applicationsDidUpdateMetadata:"
- "applicationsWillInstall:"
- "applicationsWillUninstall:"
- "arrayByAddingObject:"
- "arrayWithContentsOfURL:"
- "arrayWithObjects:count:"
- "associatedBundleIdentifier"
- "associatedBundleMinimumVersion"
- "autorelease"
- "boolValue"
- "bs_containsObjectPassingTest:"
- "bs_each:"
- "bs_filter:"
- "bs_flatten"
- "bs_map:"
- "bs_mapNoNulls:"
- "bs_safeAddObject:"
- "bs_safeArrayForKey:"
- "bs_safeNumberForKey:"
- "bs_safeObjectForKey:ofType:"
- "bs_setSafeObject:forKey:"
- "build"
- "builder"
- "builderWithObject:"
- "bundleForClass:"
- "bundleIdentifier"
- "caseInsensitiveCompare:"
- "ccs_hasEntitlementForForciblyEnablingModules"
- "ccs_hasEntitlementForHandlingControlCenterOperation"
- "ccs_hasEntitlementForListingModuleIdentifiers"
- "ccs_hasEntitlementForModuleIdentifier:"
- "ccs_hasEntitlementToResetToDefaultLayout"
- "class"
- "close"
- "compare:options:"
- "conformsToProtocol:"
- "containerBundleIdentifier"
- "containsObject:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "controlKind"
- "controlType"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "currentConnection"
- "currentHandler"
- "dataWithPropertyList:format:options:error:"
- "databaseWasRebuilt"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultExpandedOptions"
- "defaultManager"
- "defaultOptions"
- "defaultWorkspace"
- "delegate"
- "description"
- "deviceClass"
- "deviceManagementPolicyDidChange:"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "elementType"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateEndpointsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "extensionBundleIdentifier"
- "fileExistsAtPath:"
- "fileSystemRepresentation"
- "fileURLWithPathComponents:"
- "filteredArrayUsingPredicate:"
- "getEnabledStateOfModuleWithIdentifier:completionHandler:"
- "handleControlCenterOperationType:completionHandler:"
- "handleControlCenterOperationTypeWithOperationService:operationType:completionHandler:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleIconElementRequest:completionHandler:"
- "handleIconElementRequestWithOperationService:iconElementRequest:completionHandler:"
- "hash"
- "hashTableWithOptions:"
- "helperPlaceholdersInstalled:"
- "helperPlaceholdersUninstalled:"
- "homeButtonType"
- "incrementUserInvocationCount"
- "infoDictionary"
- "init"
- "initWithBlurBackground:animatePresentation:animateDismissal:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithIntent:controlKind:controlType:extensionBundleIdentifier:containerBundleIdentifier:size:"
- "initWithIntent:moduleIdentifier:containerBundleIdentifier:moduleSize:"
- "initWithIntent:moduleIdentifier:containerBundleIdentifier:size:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initialize"
- "inputStreamWithURL:"
- "insertObject:atIndex:"
- "intent"
- "intentConfiguration"
- "intentDescription"
- "interfaceWithProtocol:"
- "intersectsSet:"
- "invalidate"
- "isCarrierInstall"
- "isEqual:"
- "isEqualToString:"
- "isInstalled"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRestricted"
- "isStageManagerAvailable"
- "isSubsetOfSet:"
- "legacyModuleMigration:versionNumber:"
- "length"
- "listener:shouldAcceptNewConnection:"
- "loadableModuleIdentifiers"
- "loadableModulesChangedForModuleRepository:"
- "metadataForBundleAtURL:"
- "minusSet:"
- "moduleBundleURL"
- "moduleIdentifier"
- "moduleMetadataForModuleIdentifier:"
- "moduleSize"
- "mutableCopy"
- "networkUsageChanged:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKey:ofClass:"
- "observeDefault:onQueue:withBlock:"
- "observeLaunchProhibitedApps"
- "open"
- "orderedEnabledModuleIdentifiersChangedForSettingsProvider:"
- "orderedFixedModuleIdentifiers"
- "orderedUserEnabledFixedModuleIdentifiers"
- "orderedUserEnabledModuleIdentifiers"
- "path"
- "pathExtension"
- "pathWithComponents:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginsDidInstall:"
- "pluginsDidUninstall:"
- "pluginsWillUninstall:"
- "predicateWithFormat:"
- "presentModuleWithIdentifier:options:completion:"
- "presentModuleWithIdentifier:options:completionHandler:"
- "propertyListWithStream:options:format:error:"
- "q"
- "q16@0:8"
- "registerEndpoint:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeObject:"
- "removeObjectsInArray:"
- "removeObserver:"
- "requestAvailableModuleIdentifiersWithCompletionHandler:"
- "requestDisableModuleWithIdentifier:completionHandler:"
- "requestEnableModuleWithIdentifier:completionHandler:"
- "requestEnableModuleWithIdentifier:force:completionHandler:"
- "requestIconElementState:completionHandler:"
- "requestIconElementStateWithOperationService:iconElementRequest:completionHandler:"
- "requiredDeviceCapabilities"
- "requiredDeviceIncapabilities"
- "resetToDefaultLayoutWithCompletionHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setAndSaveOrderedUserEnabledFixedModuleIdentifiers:"
- "setAndSaveOrderedUserEnabledModuleIdentifiers:"
- "setAndSaveOrderedUserEnabledModuleIdentifiers:previousOrderedUserEnabledModuleIdentifiers:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setIntentConfiguration:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setRemoteObjectInterface:"
- "setUserInvocationCount:"
- "setVisibility:forModuleIdentifier:"
- "setVisibility:forModuleWithIdentifier:completionHandler:"
- "setWithArray:"
- "sharedInstance"
- "sharedProvider"
- "sharedService"
- "shortVersionString"
- "size"
- "sortUsingSelector:"
- "standardDefaults"
- "startServices"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportedDeviceFamilies"
- "supportsSecureCoding"
- "tokenFromXPCConnection:"
- "unionSet:"
- "unsignedIntegerValue"
- "userDisabledModuleIdentifiers"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v28@0:8B16@20"
- "v32@0:8@\"CCSIconElementRequest\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"CCSIconElementRequest\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?Q>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8^B16Q24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?B@\"NSError\">24"
- "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v36@0:8B16@\"NSString\"20@?<v@?B@\"NSError\">28"
- "v36@0:8B16@20@?28"
- "v40@0:8@\"NSString\"16@\"CCSModulePresentationOptions\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "valueForEntitlement:"
- "visibilityForModuleIdentifier:"
- "visibilityPreference"
- "weakObjectsHashTable"
- "writeToURL:options:error:"
- "zone"

```
