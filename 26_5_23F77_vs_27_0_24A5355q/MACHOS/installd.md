## installd

> `/usr/libexec/installd`

```diff

-1513.120.7.0.0
-  __TEXT.__text: 0x60f9c
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_stubs: 0x8220
-  __TEXT.__objc_methlist: 0x335c
+1655.0.0.0.0
+  __TEXT.__text: 0x67154
+  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__objc_stubs: 0x8ac0
+  __TEXT.__objc_methlist: 0x35cc
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x169d2
-  __TEXT.__objc_classname: 0x613
-  __TEXT.__objc_methtype: 0x1fe2
-  __TEXT.__objc_methname: 0xbfd7
-  __TEXT.__gcc_except_tab: 0x33a0
-  __TEXT.__oslogstring: 0x11ac
+  __TEXT.__cstring: 0x17efd
+  __TEXT.__objc_classname: 0x5ee
+  __TEXT.__objc_methtype: 0x22ac
+  __TEXT.__objc_methname: 0xcd9b
+  __TEXT.__gcc_except_tab: 0x3b04
+  __TEXT.__oslogstring: 0x14ee
   __TEXT.__ustring: 0x84
-  __TEXT.__unwind_info: 0x1208
-  __DATA_CONST.__auth_got: 0x7d0
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1248
-  __DATA_CONST.__cfstring: 0x9ce0
-  __DATA_CONST.__objc_classlist: 0x148
+  __TEXT.__unwind_info: 0x1268
+  __DATA_CONST.__const: 0x1478
+  __DATA_CONST.__cfstring: 0xa4e0
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_intobj: 0x258
-  __DATA_CONST.__objc_arraydata: 0x5f0
-  __DATA_CONST.__objc_dictobj: 0xed8
-  __DATA.__objc_const: 0x5e10
-  __DATA.__objc_selrefs: 0x2530
-  __DATA.__objc_ivar: 0x2a8
-  __DATA.__objc_data: 0xcd0
-  __DATA.__data: 0xa18
-  __DATA.__bss: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_intobj: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x670
+  __DATA_CONST.__objc_dictobj: 0x1018
+  __DATA_CONST.__auth_got: 0x810
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__objc_const: 0x5e48
+  __DATA.__objc_selrefs: 0x2788
+  __DATA.__objc_ivar: 0x2a4
+  __DATA.__objc_data: 0xc80
+  __DATA.__data: 0xa78
+  __DATA.__bss: 0x1a0
   __DATA.__common: 0x10
   __RESTRICT.__restrict: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 026CFF5B-7F96-314B-8B16-0A418ED79395
-  Functions: 1291
-  Symbols:   371
-  CStrings:  4893
+  UUID: B4F960C0-AA1C-3051-895A-418BC0228551
+  Functions: 1374
+  Symbols:   384
+  CStrings:  5156
 
Symbols:
+ _MIIsValidPersonaLifecycleEventType
+ _MIStringForPersonaLifecycleEventType
+ _OBJC_CLASS_$_ICLBundleRecord
+ _OBJC_CLASS_$_LSBundlePersonaRecordMap
+ _OBJC_CLASS_$_MIPersonaAssociation
+ _OBJC_CLASS_$_MIPersonaContainerSet
+ _OBJC_CLASS_$_MIStagedUpdateMetadata
+ _OBJC_CLASS_$_NSJSONSerialization
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x10
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
- _OBJC_CLASS_$_MIContainerProtectionManager
CStrings:
+ "%s: App %@ has erroneous data container with persona %@. Deleting abandoned containers."
+ "%s: Did not find any data backed personas!"
+ "%s: Expected to find bundleURL on data container for SYSTEM/ANY persona extension %@; skipping"
+ "%s: Failed to deserialize built-in persona associations from %@ : %@"
+ "%s: Failed to enumerate all bundle containers: %@"
+ "%s: Failed to get data-backed personas list: %@"
+ "%s: Failed to get installed info for %@: %@"
+ "%s: Failed to get legacy persona to bundle ID mapping from UM! Existing personas will not be associated with apps. Error: %@"
+ "%s: Failed to get system persona unique string during migration: %@"
+ "%s: Failed to get system persona unique string: %@"
+ "%s: Failed to load %@ : %@"
+ "%s: Failed to serialize built-in persona association map content: %@"
+ "%s: Failed to set personas to %@ for app %@ : %@"
+ "%s: Failed to write serialized built-in persona association map to %@ : %@"
+ "%s: Found unexpected data format in %@: found %@ but expected dictionary"
+ "%s: Found unexpected data format in %@: unexpected class in keys or values"
+ "+[MIPersonaAssociationManager _removePersona:fromExistingPersonaSet:forApp:defaultPersona:addDefaultPersonaIfLastAssociation:personasChanged:error:]"
+ "-[MIClientConnection addPersona:toApp:inDomain:withCompletion:]"
+ "-[MIClientConnection appBundleIDsWithPersona:inDomain:withCompletion:]"
+ "-[MIClientConnection enrollPersona:forApps:inDomain:withCompletion:]"
+ "-[MIClientConnection personasForBuiltInBundleID:withCompletion:]"
+ "-[MIClientConnection personasForBundleID:inDomain:withCompletion:]"
+ "-[MIClientConnection removePersona:fromApp:inDomain:withCompletion:]"
+ "-[MIClientConnection reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:]"
+ "-[MIClientConnection reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:]_block_invoke"
+ "-[MIClientConnection setPersonas:forApp:inDomain:withCompletion:]"
+ "-[MIIPAPatcherFileManager dataFromJSONRepresentation:withError:]"
+ "-[MIIPAPatcherFileManager jsonRepresentationFromData:withError:]"
+ "-[MIIPAPatcherFileManager writeJSONRepresentation:toFileURL:mode:maxBytes:withError:]"
+ "-[MILaunchServicesOperationManager _discoverInfoForAppBundleID:inDomain:forPersonas:error:]"
+ "-[MILaunchServicesOperationManager _onQueue_setPersonaUniqueStrings:forAppBundleIDSet:inDomain:error:]"
+ "-[MILaunchServicesOperationManager setPersonaUniqueStrings:forAppBundleIDs:inDomain:error:]_block_invoke"
+ "-[MIPersonaAssociationManager _addPersona:toApp:inDomain:ignoreUninstalledApp:error:]"
+ "-[MIPersonaAssociationManager _enumerateAppContainersInDomain:usingBlock:]_block_invoke"
+ "-[MIPersonaAssociationManager _onQueue_loadBuiltInPersonaAssociationMap]"
+ "-[MIPersonaAssociationManager _onQueue_personasForBuiltInBundleID:defaultPersona:error:]"
+ "-[MIPersonaAssociationManager _onQueue_saveBuiltInPersonaAssociationMap]"
+ "-[MIPersonaAssociationManager _setPersonas:forApp:inDomain:saveMapping:tellLS:error:]"
+ "-[MIPersonaAssociationManager performMigrationFromUserManagement]"
+ "-[MIPersonaAssociationManager performMigrationFromUserManagement]_block_invoke"
+ "-[MIPersonaAssociationManager personasForBuiltInBundleID:error:]"
+ "-[MIPersonaAssociationManager personasForBundleID:inDomain:error:]"
+ "-[MIPersonaAssociationManager removePersona:fromApp:inDomain:error:]"
+ "-[MIReferenceAwareLSDatabaseGatherer scanExecutableBundle:inContainer:withError:]"
+ "<%@: %@:%lu [%@]/%@ personas:[%@]>"
+ "@\"MIPersonaContainerSet\""
+ "@\"NSData\"32@0:8@\"NSDictionary\"16^@24"
+ "@32@0:8Q16@?24"
+ "@32@0:8Q16^@24"
+ "@48@0:8@16@24^B32^@40"
+ "@48@0:8@16Q24@32^@40"
+ "@64@0:8@16@24@32@40^B48^@56"
+ "@68@0:8@16@24@32@40B48^B52^@60"
+ "App %@ has erroneous data container with persona %@. Deleting abandoned containers."
+ "App %@ queried by lsd was not in built-in content map; returning primary persona"
+ "App no longer needs data containers for appex with id %@; removing it"
+ "Attempt to remove persona %@ from %@ but that persona is not currently associated. Ignoring."
+ "B16@?0@\"MIBundleContainer\"8"
+ "B16@?0@\"MIPluginDataContainer\"8"
+ "B32@?0@\"MIBundleContainer\"8@\"MIBundleMetadata\"16@\"NSSet\"24"
+ "B48@0:8@16^@24^B32^@40"
+ "B52@0:8@\"NSDictionary\"16@\"NSURL\"24S32Q36^@44"
+ "B52@0:8@16@24Q32B40^@44"
+ "B52@0:8@16@24S32Q36^@44"
+ "B56@0:8@16@24Q32B40B44^@48"
+ "B56@0:8@16Q24@32Q40^@48"
+ "BuiltInPersonaAssociations.plist"
+ "Client %@ adding apps associated with persona %@: %@"
+ "Client %@ adding persona %@ to app %@"
+ "Client %@ adding persona %@ to apps %@"
+ "Client %@ attempted to set empty persona list for %@. This is not allowed."
+ "Client %@ queried apps for persona %@: %@"
+ "Client %@ queried personas on app %@: %@"
+ "Client %@ queried personas on built in app %@: %@"
+ "Client %@ removing apps associated with persona %@: %@"
+ "Client %@ removing persona %@ from app %@"
+ "Client %@ reported persona lifecycle event %@ for %@"
+ "Client %@ setting apps associated with persona %@ to %@"
+ "Client %@ setting personas on app %@: %@"
+ "Completed migration of persona to bundle ID mappings from UM"
+ "Could not find installed app with identifier %@ in domain %lu"
+ "Could not locate system/internal app for bundle ID %@"
+ "Could not remove persona %@ from %@ because this is the only persona currently associated with this app."
+ "Could not serialize JSON from given object [%@]"
+ "DataContainerTokens"
+ "Deleting orphaned container: %@"
+ "Did not find any data backed personas!"
+ "Exception thrown in dataWithJSONObject [%@]"
+ "Expected to find bundleURL on data container for SYSTEM/ANY persona extension %@; skipping"
+ "FF OFF: Bundle ID to Persona Mapping In UM"
+ "FF ON: Bundle ID to Persona Mapping In MI"
+ "Failed to clear existing UM bundle ID mapping: %@"
+ "Failed to create app extension data containers for  %@"
+ "Failed to create data containers for app extension %@ when registering placeholder for %@"
+ "Failed to create plugin data containers for plugin %@"
+ "Failed to deserialize built-in persona associations from %@ : %@"
+ "Failed to enumerate all bundle containers: %@"
+ "Failed to enumerate content with options %@: %@"
+ "Failed to fetch data containers for no longer present app extension with id %@ : %@"
+ "Failed to fetch primary persona"
+ "Failed to get data-backed personas list: %@"
+ "Failed to get installed info for %@: %@"
+ "Failed to get legacy persona to bundle ID mapping from UM! Existing personas will not be associated with apps. Error: %@"
+ "Failed to get persona for container %@"
+ "Failed to get personas associated with app %@ : %@"
+ "Failed to get system persona unique string during migration: %@"
+ "Failed to get system persona unique string: %@"
+ "Failed to load %@ : %@"
+ "Failed to load bundle metadata for container %@ : %@"
+ "Failed to locate data containers for stashed app %@"
+ "Failed to look up data containers for app extension %@"
+ "Failed to remove abandoned containers with incorrect persona for %@"
+ "Failed to resolve persona for %@: %@"
+ "Failed to serialize built-in persona association map content: %@"
+ "Failed to set personas to %@ for app %@ : %@"
+ "Failed to write serialized built-in persona association map to %@ : %@"
+ "Found %ld app extensions and %ld app extension data container sets; they should be equal."
+ "Found a container for a persona %@ not currently associated with the app: %@"
+ "Found a container for an unknown persona %@ : %@"
+ "Found unexpected data format in %@: found %@ but expected dictionary"
+ "Found unexpected data format in %@: unexpected class in keys or values"
+ "Found unknown personas in %@ associated with %@; overriding association to %@"
+ "JSON data is not a dictionary, got [%@]"
+ "JSONObjectWithData:options:error:"
+ "List safe harbor requested by client %@ for type %ld persona %@ with options %@"
+ "LocalManagerBridge"
+ "MIIPAPatcherSerializesJSON"
+ "MIPersonaAssociationManager"
+ "Max JSON representation length exceeded (%lu > %lu)"
+ "Migrating from UM: %@ -> %@"
+ "Migrating persona to bundle ID mappings from UM to MI"
+ "Missing bundleID(s) when deserializing registration"
+ "Process %@ tried to add persona %@ for %@ but this can only be done by InstallCoordination."
+ "Process %@ tried to enroll persona %@ for apps %@ but this can only be done by InstallCoordination."
+ "Process %@ tried to fetch personas from installd, but it was not either lsd or a process with the %@ entitlement."
+ "Process %@ tried to fetch personas from installd, but this can only be done by the test runner."
+ "Process %@ tried to remove persona %@ from %@ but this can only be done by InstallCoordination."
+ "Process %@ tried to report persona lifecycle event for %@ but this can only be done by InstallCoordination."
+ "Process %@ tried to set persona to %@ for app %@ but this can only be done by InstallCoordination."
+ "Registered info : %@/[%@]"
+ "T@\"MIPersonaAssociation\",R,N"
+ "T@\"MIPersonaAssociationManager\",R,N"
+ "T@\"MIPersonaContainerSet\",&,N,V_dataContainers"
+ "T@\"NSDictionary\",&,N,V_builtInPersonaAssociation"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSSet\",R,C,N,V_bundleIDs"
+ "The bundle ID %@ does not represent a known built-in app."
+ "_CleanUpErroneousDataContainers_block_invoke"
+ "_DoEnumerationOfInstalledAppsWithOptions_block_invoke"
+ "_DoEnumerationOfInstalledAppsWithOptions_block_invoke_4"
+ "_addPersona:toApp:inDomain:ignoreUninstalledApp:error:"
+ "_addPersona:toAppInBundleContainer:personasChanged:error:"
+ "_addPersona:toExistingPersonaSet:defaultPersona:"
+ "_builtInPersonaAssocationStorageURL"
+ "_builtInPersonaAssociation"
+ "_bundleIDIsOnDiskImage:"
+ "_bundleIDs"
+ "_dataContainers"
+ "_discoverInfoForAppBundleID:inDomain:forPersonas:error:"
+ "_enumerateAppContainersInDomain:usingBlock:"
+ "_filteredStorableSetForPersonaSet:filteredSet:changed:error:"
+ "_onQueue_addPersona:toBuiltInApp:defaultPersona:personasChanged:error:"
+ "_onQueue_loadBuiltInPersonaAssociationMap"
+ "_onQueue_personasForBuiltInBundleID:defaultPersona:error:"
+ "_onQueue_removeAppFromBuiltInPersonaMap:"
+ "_onQueue_removePersona:fromBuiltInApp:personasChanged:error:"
+ "_onQueue_saveBuiltInPersonaAssociationMap"
+ "_onQueue_setPersonaUniqueStrings:forAppBundleIDSet:inDomain:error:"
+ "_queue"
+ "_removePersona:fromAppInBundleContainer:personasChanged:error:"
+ "_removePersona:fromExistingPersonaSet:forApp:defaultPersona:addDefaultPersonaIfLastAssociation:personasChanged:error:"
+ "_removePersona:fromExistingPersonaSet:forApp:defaultPersona:personasChanged:error:"
+ "_setPersona:viaLaunchServicesForApps:inDomain:error:"
+ "_setPersonas:forApp:inDomain:saveMapping:tellLS:error:"
+ "_setPersonas:viaLaunchServicesForApp:inDomain:error:"
+ "_useBuiltInMapForBundleID:"
+ "addBundlePersonaRecordsForICLBundleRecords:"
+ "addPersona:toApp:inDomain:error:"
+ "addPersona:toApp:inDomain:withCompletion:"
+ "allBundleIDsForBuiltInMap"
+ "allContainers"
+ "allContainersForAllIdentifiers"
+ "allContainersInSafeHarbor"
+ "allContainersNotInSafeHarbor"
+ "allDataBackedPersonaUniqueStringsWithError:"
+ "appBundleIDsOnAllAttachedEntities"
+ "appBundleIDsWithPersona:inDomain:error:"
+ "appBundleIDsWithPersona:inDomain:withCompletion:"
+ "appBundleIDsWithSystemPersonaInDomain:error:"
+ "arrayWithObject:"
+ "associatedBuiltInBundleURL"
+ "associatedPersonas"
+ "associatedPersonasUsingParentPersona:error:"
+ "associatedPersonasWithError:"
+ "builtInPersonaAssociation"
+ "bundleIDIsOnAnyAttachedEntity:"
+ "bundleIDs"
+ "clearLegacyBundleIDMappingWithError:"
+ "com.apple.developer.usernotifications.critical-alerts"
+ "com.apple.developer.wrapper-bundle"
+ "com.apple.mobileinstallation.persona_association"
+ "com.apple.private.coreservices.lsd"
+ "com.apple.private.extensionkit.builtinanypersona"
+ "com.apple.private.extensionkit.builtinsystempersona"
+ "com.apple.private.pluginkit.persona"
+ "com.apple.usermanagerd.persona.fetch"
+ "dataContainers"
+ "dataContainersCreatingIfNeeded:forPersona:makeLive:created:error:"
+ "dataContainersCreatingIfNeeded:parentPersona:makeLive:created:didUseProvidedPersona:error:"
+ "dataFromJSONRepresentation:withError:"
+ "dataProtectionClass"
+ "dataWithJSONObject:options:error:"
+ "defaultPersonaWithError:"
+ "enrollPersona:forApps:inDomain:error:"
+ "enrollPersona:forApps:inDomain:withCompletion:"
+ "entryForBundle:inContainer:forPersonas:withError:"
+ "enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBlock:"
+ "enumerateAppBundleRecord:error:"
+ "enumerateAppExtensionsInBundle:forPersonas:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:"
+ "enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:"
+ "fetchInfoForBundle:forPersonas:inContainer:withError:"
+ "initWithAppExtensionBundle:inBundleIdentifier:dataContainers:associatedPersonaUniqueStrings:"
+ "initWithBundleContainer:dataContainers:associatedPersonaUniqueStrings:"
+ "initWithBundleIDs:domain:personas:registrationUUID:serialNumber:"
+ "initWithContainers:"
+ "isKnownPersonaUniqueString:error:"
+ "isSecondOrThirdPartyAppForDataProtection"
+ "isSystemOrAnyPersonaExtension"
+ "isValidJSONObject:"
+ "jsonRepresentationFromData:withError:"
+ "legacyBundleIDMappingWithError:"
+ "local_appBundleIDsWithPersona:inDomain:error:"
+ "local_personasForBuiltInBundleID:error:"
+ "local_personasForBundleID:inDomain:error:"
+ "minimalAppBundleContainerForMetadataForIdentifier:inDomain:withError:"
+ "performMigrationFromUserManagement"
+ "personaAssociationInstance"
+ "personaBundleIDPurgeCompleted"
+ "personaBundleIDRelayeringEnabled"
+ "personaMigrationFromUMComplete"
+ "personasAreKnownForUniqueStrings:error:"
+ "personasForBuiltInBundleID:error:"
+ "personasForBuiltInBundleID:withCompletion:"
+ "personasForBundleID:inDomain:error:"
+ "personasForBundleID:inDomain:withCompletion:"
+ "personasForBundleMetadata:error:"
+ "primaryPersonaUniqueStringWithError:"
+ "queue"
+ "reason"
+ "reconcileStateForPersona:eventType:parentAppBundleIDs:inDomain:error:"
+ "registerApplicationForRebuildWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:requestContext:registrationError:"
+ "registerUnbundledExtensionAtURL:error:"
+ "removePersona:fromApp:inDomain:error:"
+ "removePersona:fromApp:inDomain:withCompletion:"
+ "removeUnknownPersonasFromSet:error:"
+ "reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:"
+ "scanExecutableBundle:inContainer:withError:"
+ "setAssociatedPersonas:"
+ "setBuiltInPersonaAssociation:"
+ "setDataContainers:"
+ "setDataProtectionClass:forSecondOrThirdPartyApp:"
+ "setPersona:exclusivelyAssociatedWithApps:inDomain:error:"
+ "setPersonaBundleIDPurgeCompleted:"
+ "setPersonaMigrationFromUMComplete:"
+ "setPersonaUniqueString:forAppBundleIDs:inDomain:error:"
+ "setPersonaUniqueStrings:forAppBundleIDs:inDomain:error:"
+ "setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:bundlePersonaRecordMap:operationUUID:requestContext:saveObserver:error:"
+ "setPersonas:forApp:inDomain:error:"
+ "setPersonas:forApp:inDomain:withCompletion:"
+ "setPersonas:forBundleMetadata:error:"
+ "stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:completion:"
+ "stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:"
+ "stagingLocationForURL:withinStagingSubsystem:usingUniqueName:completion:"
+ "stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:"
+ "systemPersonaBundleIDs"
+ "systemPersonaUniqueStringWithError:"
+ "systemPersonaWithError:"
+ "v32@0:8@\"ICLBundleRecord\"16@\"NSError\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSError\">24"
+ "v32@?0@\"ICLBundleRecord\"8@\"NSArray\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"NSMutableSet\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSSet\"16^B24"
+ "v36@0:8@\"NSDictionary\"16B24@?<v@?@\"NSError\">28"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSSet\"@\"NSError\">32"
+ "v48@0:8@\"NSSet\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSSet\"24Q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24Q32@?40"
+ "writeJSONRepresentation:toFileURL:mode:maxBytes:withError:"
- "%s: App %@ already has a data container with persona %@ but this installation request came for a different persona, %@. Apps may not be installed for multiple personas simultaneously. Deleting abandoned containers."
- "+[MIAppReferenceTracker managerForInstallationDomain:]"
- "-[MIAppIdentity(MIDaemonUtilities) resolvePersonaUsingModuleSpecificLogicWithError:]"
- "-[MIAppReferenceTracker addReferenceForIdentity:error:]"
- "-[MIAppReferenceTracker addTemporaryReferenceForIdentity:error:]"
- "-[MIAppReferenceTracker enumerateAppReferencesWithBlock:]"
- "-[MIAppReferenceTracker finalizeTemporaryReference:error:]"
- "-[MIAppReferenceTracker referenceExists:forIdentity:error:]"
- "-[MIAppReferenceTracker removeReferenceForIdentity:waitingForSpaceReclaimation:error:]"
- "-[MIAppReferenceTracker revokeTemporaryReference:error:]"
- "-[MILaunchServicesOperationManager _onQueue_setPersonaUniqueStrings:forAppBundleID:inDomain:error:]"
- "-[MILaunchServicesOperationManager setPersonaUniqueStrings:forAppBundleID:inDomain:error:]_block_invoke"
- "-[MIReferenceAwareLSDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:]"
- "-[MIStagedUpdateMetadata isEqual:]"
- "@\"MIDataContainer\""
- "App %@ already has a data container with persona %@ but this installation request came for a different persona, %@. Apps may not be installed for multiple personas simultaneously. Deleting abandoned containers."
- "B40@0:8^B16@24^@32"
- "B48@0:8@16@24@32^@40"
- "Can't resolve the persona associated with the bundle %@ from the associated personas in app references: %@"
- "Container cleanup disabled"
- "Failed to associate %@ with persona string in LS %@ : %@"
- "Failed to create app extension data container for  %@"
- "Failed to create data container for app extension %@ when registering placeholder for %@"
- "Failed to create plugin data container for plugin %@"
- "Failed to fetch data container for no longer present app extension with id %@ : %@"
- "Failed to locate data container for stashed app %@"
- "Failed to look up data container for app extension %@"
- "Failed to query bundle containers: %@"
- "Failed to retrieve UM persona attributes: %@"
- "Found possibly abandoned container %@ %@ user data. Skipping deletion"
- "List safe harbor requested by client %@ for type %ld with options %@"
- "MIAppReferenceTracker"
- "MIDaemonUtilities"
- "MIStagedUpdateMetadata"
- "Registered info : %@"
- "Request for manager for unknown domain: %lu"
- "T@\"MIDataContainer\",&,N,V_dataContainer"
- "T@\"NSString\",C,N,V_stagedIdentifier"
- "TQ,N,V_stagedDiskUsage"
- "Unexpectedly found erroneous container %@"
- "[%@/%llu]"
- "_DoEnumerationOfInstalledAppsWithOptions_block_invoke_2"
- "_containerProtectionManager"
- "_dataContainer"
- "_onQueue_setPersonaUniqueStrings:forAppBundleID:inDomain:error:"
- "_stagedDiskUsage"
- "_stagedIdentifier"
- "addReferenceForIdentity:error:"
- "addTemporaryReferenceForIdentity:error:"
- "bundleIDsAssociatedWithPersonaUniqueString:error:"
- "containermanagerd"
- "dataContainer"
- "dataContainerCreatingIfNeeded:forPersona:makeLive:created:error:"
- "dataContainerForPersona:error:"
- "entryForBundle:inContainer:forPersona:withError:"
- "enumerateAppExtensionsInBundle:forPersona:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:"
- "enumerateInstalledAppsWithOptions:completion:"
- "fetchInfoForBundle:forPersona:inContainer:withError:"
- "finalizeTemporaryReference:error:"
- "initForInstallationDomain:"
- "initWithAppExtensionBundle:inBundleIdentifier:dataContainer:"
- "initWithBundleContainer:dataContainer:"
- "initWithBundleID:domain:personas:registrationUUID:serialNumber:"
- "isDataSeparatedPersona"
- "listAllPersonaAttributesWithError:"
- "managerForInstallationDomain:"
- "multiPersonaSADAppBundleIDsWithError:"
- "multipersona_reconciliation_on_delete"
- "primaryPersonaString"
- "primaryPersonaUniqueString"
- "referenceExists:forIdentity:error:"
- "registerApplicationForRebuildWithInfoDictionaries:requestContext:registrationError:"
- "removeReferenceForIdentity:waitingForSpaceReclaimation:error:"
- "resolvePersonaUsingModuleSpecificLogicWithError:"
- "revokeTemporaryReference:error:"
- "scanExecutableBundle:inContainer:forPersona:withError:"
- "setBundleIdentifiers:forPersonaUniqueString:error:"
- "setDataContainer:"
- "setDataProtectionOnDataContainer:forNewBundle:retryIfLocked:"
- "setPersonaUniqueStrings:forApplicationWithBundleIdentifier:operationUUID:requestContext:saveObserver:error:"
- "setStagedDiskUsage:"
- "setStagedIdentifier:"
- "stagedDiskUsage"
- "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:"
- "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
- "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:"
- "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:"
- "userPersonaBundleIDList"
- "userPersonaUniqueString"

```
