## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1367.406.0.0.0
-  __TEXT.__text: 0x190700
+1378.12.0.0.0
+  __TEXT.__text: 0x1986b0
   __TEXT.__auth_stubs: 0x3210
-  __TEXT.__objc_methlist: 0xb2d0
-  __TEXT.__const: 0x900
-  __TEXT.__cstring: 0x1fcaf
-  __TEXT.__oslogstring: 0x12ac7
-  __TEXT.__gcc_except_tab: 0x233cc
+  __TEXT.__objc_methlist: 0xc3ec
+  __TEXT.__const: 0x920
+  __TEXT.__cstring: 0x207c9
+  __TEXT.__oslogstring: 0x12f56
+  __TEXT.__gcc_except_tab: 0x24200
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xa1f8
+  __TEXT.__unwind_info: 0xa6f0
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x1cd7
-  __TEXT.__objc_methname: 0x1b6e7
-  __TEXT.__objc_methtype: 0xaab5
-  __TEXT.__objc_stubs: 0xf260
-  __DATA_CONST.__got: 0x9f0
-  __DATA_CONST.__const: 0x6788
-  __DATA_CONST.__objc_classlist: 0x648
+  __TEXT.__objc_classname: 0x1d52
+  __TEXT.__objc_methname: 0x1be4b
+  __TEXT.__objc_methtype: 0xadf0
+  __TEXT.__objc_stubs: 0xf600
+  __DATA_CONST.__got: 0x9f8
+  __DATA_CONST.__const: 0x6a30
+  __DATA_CONST.__objc_classlist: 0x670
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58d8
+  __DATA_CONST.__objc_selrefs: 0x5a50
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x4f0
-  __DATA_CONST.__objc_arraydata: 0x188
+  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0x1920
-  __AUTH_CONST.__auth_ptr: 0x48
-  __AUTH_CONST.__const: 0x3380
-  __AUTH_CONST.__cfstring: 0x15c20
-  __AUTH_CONST.__objc_const: 0x139c8
+  __AUTH_CONST.__auth_ptr: 0x60
+  __AUTH_CONST.__const: 0x3408
+  __AUTH_CONST.__cfstring: 0x15f60
+  __AUTH_CONST.__objc_const: 0x12520
   __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH.__objc_data: 0x2850
-  __AUTH.__data: 0x320
-  __DATA.__objc_ivar: 0x9e8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH.__objc_data: 0x2940
+  __AUTH.__data: 0x328
+  __DATA.__objc_ivar: 0xa24
   __DATA.__data: 0x1350
-  __DATA.__bss: 0xef0
+  __DATA.__bss: 0xe58
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x1680
+  __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0x7c8
+  __DATA_DIRTY.__bss: 0x868
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7922
-  Symbols:   9630
-  CStrings:  10167
+  Functions: 8254
+  Symbols:   10037
+  CStrings:  10295
 
CStrings:
+ "%s: currently not eligible for %llu (answer %d)"
+ "-[LSApplicationWorkspace registerBuiltinApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]"
+ "-[LSApplicationWorkspace registerBuiltinStandaloneExtension:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]"
+ "-[LSApplicationWorkspace unregisterBuiltinApplicationAtURL:operationUUID:requestContext:saveObserver:error:]"
+ "-[LSApplicationWorkspace unregisterBuiltinStandaloneExtensionAtURL:operationUUID:requestContext:saveObserver:error:]"
+ "-[LSBuiltinApplicationRegistrant runWithCompletion:]"
+ "-[LSBuiltinApplicationRegistrant runWithCompletion:]_block_invoke"
+ "-[LSBuiltinApplicationRegistrant runWithCompletion:]_block_invoke_2"
+ "-[LSBuiltinPluginRegistrant runWithCompletion:]"
+ "-[LSBuiltinPluginRegistrant runWithCompletion:]_block_invoke"
+ "-[LSByURLBundleUnregistrant runWithCompletion:]_block_invoke"
+ "-[LSByURLPluginUnregistrant runWithCompletion:]_block_invoke"
+ "-[LSMIResultRegistrantTrueDatabaseContext findApplicationBundleAtNode:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext registerNonBundledExtensionPointWithIdentifier:platform:SDKDict:url:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext unregisterApplicationBundleByUnit:error:]"
+ "-[LSMIResultRegistrantTrueDatabaseContext unregisterPluginBundleByUnit:error:]"
+ "-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke"
+ "-[_LSDModifyClient refreshExtensionPointsWithOperationUUID:reply:]"
+ "-[_LSDModifyClient registerBuiltinAppex:operationUUID:reply:]"
+ "-[_LSDModifyClient registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:]"
+ "-[_LSDModifyClient registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:]_block_invoke"
+ "-[_LSDModifyClient unregisterApplicationAtURL:operationUUID:reply:]"
+ "-[_LSDModifyClient unregisterPluginAtURL:operationUUID:reply:]"
+ "@\"<LSRegistrantDatabaseContext>\"24@0:8^@16"
+ "@\"<LSRegistrantStrategy>\""
+ "@28@0:8I16@\"<LSRegistrantDatabaseContext>\"20"
+ "@28@0:8I16@20"
+ "@?28@0:8I16^@20"
+ "@?<v@?@>28@0:8I16^@20"
+ "B32@0:8@\"NSString\"16^@24"
+ "B44@0:8@\"FSNode\"16@\"NSDictionary\"24I32^@36"
+ "B44@0:8@16@24I32^@36"
+ "B52@0:8@\"NSString\"16I24@\"NSDictionary\"28@\"NSURL\"36^@44"
+ "B52@0:8@16I24@28@36^@44"
+ "B72@0:8@16@24@32@40@48@56^@64"
+ "Bad context provided"
+ "Cannot register parallel placeholders or standalone placeholders with this interface."
+ "Couldn't get answer for domain %llu: %@"
+ "Don't add weak binding (ineligible)"
+ "I32@0:8@\"FSNode\"16^@24"
+ "I52@0:8@\"FSNode\"16B24@\"NSDictionary\"28@\"NSSet\"36^@44"
+ "I52@0:8@16B24@28@36^@44"
+ "LSBuiltinApplicationRegistrant"
+ "LSBuiltinPluginRegistrant"
+ "LSByURLBundleUnregistrant"
+ "LSByURLPluginUnregistrant"
+ "LSDefaultAppCategoryInvalidPlaceholder"
+ "LSDefaultAppCategoryNavigation"
+ "LSDefaultAppCategoryTranslation"
+ "LSDefaultApplicationQueryBackend.mm"
+ "LSRegistrantDatabaseContext"
+ "LSRegistrantDatabaseContextProviding"
+ "LSRegistrantServerStrategy"
+ "LSRegistrantStrategy"
+ "LSRegistrants.mm"
+ "LSSystemExtensionPointRefreshRegistrant"
+ "LaunchServices database schema version: %{public}ld"
+ "Missing path"
+ "Registered %zu EPs, new: %@ obsolete: %@"
+ "Save after registration for refresh extension points, save attempted %d error %@"
+ "Save after registration for register builtin plugin url %@ (unit %llx) attempted: %d save error: %@"
+ "Save after unregistration for plugin url %@ (unit %llx) attempted: %d save error: %@"
+ "Save after unregistration for register builtin app url %@ (unit %llx) attempted: %d save error: %@"
+ "Save after unregistration for url %@ (unit %llx) attempted: %d save error: %@"
+ "T@\"NSArray\",R,N,V_windowOpenDates"
+ "TB,R,D,N,GisOpenWindowGroupFull"
+ "T^{LSContext=@},R"
+ "Unable to unregister obsolete EP %@: %@"
+ "Unregister bundle by URL start: %@"
+ "Unregister plugin by URL start: %@"
+ "Will unregister app by unit (0x%llx), removingPlaceholder: %d removingSystemPlaceholder: %d foundParallelBundle: %d"
+ "^{LSContext=@}16@0:8"
+ "_LSUnregisterAppByUnit"
+ "_prepareProxyForNotificationByBundleUnit:context:"
+ "_windowOpenDates"
+ "app in container"
+ "clientIsEntitledForEmbeddedRegistrationOperations"
+ "com.apple.LaunchServices.DefaultAppCategory.InactiveCategory"
+ "com.apple.LaunchServices.DefaultAppCategory.Navigation"
+ "com.apple.LaunchServices.DefaultAppCategory.Translation"
+ "com.apple.Maps"
+ "com.apple.Translate"
+ "com.apple.default-app.inactivecategory"
+ "com.apple.default-app.navigation"
+ "com.apple.default-app.translation"
+ "com.apple.developer.navigation-app"
+ "com.apple.developer.translation-app"
+ "com.apple.lsd.registerBuiltinAppex:operationUUID:reply"
+ "com.apple.lsd.registerBuiltinApplicationAtURL:operationUUID:reply"
+ "com.apple.lsd.unregisterApplicationAtURL:operationUUID:reply:"
+ "com.apple.lsd.unregisterPluginAtURL:operationUUID:reply"
+ "containerizedBundleExistsForIdentifier:"
+ "contextPointer"
+ "could not register EP %@ at %@: %@"
+ "couldn't find bundle for unit %llx, but we should have it in this flow!"
+ "doTokenizedRegistrationTaskWithName:xpcReply:work:"
+ "eligibleForDomainFailingClosed"
+ "enumerateExtensionPointRecords:"
+ "enumerateSystemEXExtensionPoints:"
+ "findApplicationBundleAtNode:error:"
+ "findPluginAtNode:error:"
+ "geo-navigation"
+ "have error even though we succeeded!? %@"
+ "initWithStrategy:operationUUID:"
+ "initWithStrategy:operationUUID:URL:"
+ "initWithStrategy:operationUUID:itemInfoDict:"
+ "initWithStrategy:operationUUID:itemInfoDict:personas:"
+ "initWithWindowOpenDates:refreshDate:defaultForCategory:"
+ "isOpenWindowGroupFull"
+ "must have at least one known window"
+ "newestWindowOpenDate"
+ "not a builtin application"
+ "not a builtin plugin"
+ "oldestWindowOpenDate"
+ "openWindowGroupFull"
+ "pid %d asks to directly register %@"
+ "pid %d asks to directly register plugin %@"
+ "pid %d asks to directly unregister url: %@"
+ "pid %d asks to refresh unbundled extension points"
+ "plugin is in an app"
+ "pluginDataForPlugin:"
+ "preUnregistrationContextForBundleUnit:context:"
+ "r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@0:8I16"
+ "refreshExtensionPointsWithOperationUUID:reply:"
+ "refreshUnbundledSystemExtensionPointsWithOperationUUID:requestContext:saveObserver:registrationError:"
+ "registerBuiltinAppex:operationUUID:reply:"
+ "registerBuiltinApplication:personaUniqueStrings:operationUUID:reply:"
+ "registerBuiltinApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
+ "registerBuiltinStandaloneExtension:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
+ "registerBundleNodeReinitializingContext:inBundleContainer:installDictionary:personasWithAttributes:error:"
+ "registerNonBundledExtensionPointWithIdentifier:platform:SDKDict:url:error:"
+ "registerPluginNodeReinitializingContext:installDictionary:existingPlugin:error:"
+ "stale windows, returning %@"
+ "unregisterApplicationAtURL:operationUUID:reply:"
+ "unregisterApplicationBundleByUnit:error:"
+ "unregisterBuiltinApplicationAtURL:operationUUID:requestContext:saveObserver:error:"
+ "unregisterBuiltinStandaloneExtensionAtURL:operationUUID:requestContext:saveObserver:error:"
+ "unregisterNonBundledExtensionPointWithIdentifier:error:"
+ "unregisterPluginAtURL:operationUUID:reply:"
+ "unregisterPluginBundleByUnit:error:"
+ "updatedEntryRotatingInWindowOpenDate:refreshDate:defaultForCategory:"
+ "updatedEntryWithRefreshDate:defaultForCategory:"
+ "v16@?0@\"<LSRegistrantDatabaseContextProviding>\"8"
+ "v16@?0@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">8"
+ "v24@0:8@?<v@?@\"<EXExtensionPoint>\"^B>16"
+ "v24@0:8@?<v@?@\"<LSRegistrantDatabaseContextProviding>\">16"
+ "v24@0:8@?<v@?@\"LSExtensionPointRecord\"^B>16"
+ "v24@0:8@?<v@?B@\"<LSRegistrantDatabaseContext>\"@\"NSError\">16"
+ "v24@?0@\"<EXExtensionPoint>\"8^B16"
+ "v24@?0@\"LSExtensionPointRecord\"8^B16"
+ "v24@?0r^{LSDefaultAppCategoryInfo=Q^{__CFString}^{__CFString}Q^?^{LSDefaultAppCategorySubordinateClaim}QB}8^B16"
+ "v28@?0B8@\"<LSRegistrantDatabaseContext>\"12@\"NSError\"20"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">24"
+ "v40@0:8@\"NSDictionary\"16@\"NSUUID\"24@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">32"
+ "v40@0:8@16@?24@?32"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSUUID\"32@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">40"
+ "window open dates %@"
+ "windowOpenDates"
- "-[LSMIResultRegistrantTrueDatabaseContext findOrRegisterContainerizedNodeReinitializingContext:installDictionary:personasWithAttributes:error:]"
- "-[_LSDModifyClient unregisterApplicationAtURL:reply:]_block_invoke"
- "@\"<LSMIResultRegistrantDatabaseContext>\"24@0:8^@16"
- "@\"<LSMIResultRegistrantStrategy>\""
- "I48@0:8@\"FSNode\"16@\"NSDictionary\"24@\"NSSet\"32^@40"
- "I48@0:8@16@24@32^@40"
- "LSDefaultAppCategoryContactlessPayment"
- "LSMIRegistrantServerStrategy"
- "LSMIResultRegistrantDatabaseContext"
- "LSMIResultRegistrantDatabaseContextProviding"
- "LSMIResultRegistrantStrategy"
- "T@\"NSDate\",R,N,V_windowOpenDate"
- "^I"
- "^Q"
- "^d"
- "_windowOpenDate"
- "clientIsEntitledForPostInstallationOperations"
- "com.apple.LaunchServices.DefaultAppCategory.ContactlessPayment"
- "com.apple.Passbook"
- "com.apple.default-app.contactless-payment"
- "com.apple.lsd.unregisterApplicationAtURL:reply:"
- "findOrRegisterContainerizedNodeReinitializingContext:installDictionary:personasWithAttributes:error:"
- "stale window, returning %@"
- "unregisterApplicationAtURL:reply:"
- "v16@?0@\"<LSMIResultRegistrantDatabaseContextProviding>\"8"
- "v24@0:8@?<v@?@\"<LSMIResultRegistrantDatabaseContextProviding>\">16"
- "v24@0:8@?<v@?B@\"<LSMIResultRegistrantDatabaseContext>\"@\"NSError\">16"
- "v24@?0r^{LSDefaultAppCategoryInfo=Q^{__CFString}^{__CFString}Q^?^{LSDefaultAppCategorySubordinateClaim}Q}8^B16"
- "v28@?0B8@\"<LSMIResultRegistrantDatabaseContext>\"12@\"NSError\"20"
- "window open date %@"
- "windowOpenDate"

```
