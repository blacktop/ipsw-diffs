## deviceaccessd

> `/usr/libexec/deviceaccessd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-2700.34.0.0.0
-  __TEXT.__text: 0x8f050
+2701.2.0.0.0
+  __TEXT.__text: 0x92e38
   __TEXT.__auth_stubs: 0x2280
-  __TEXT.__objc_stubs: 0x7f40
-  __TEXT.__objc_methlist: 0x2740
+  __TEXT.__objc_stubs: 0x8360
+  __TEXT.__objc_methlist: 0x2808
   __TEXT.__const: 0x1c88
-  __TEXT.__cstring: 0x15394
-  __TEXT.__objc_classname: 0x3e5
-  __TEXT.__gcc_except_tab: 0x40c0
-  __TEXT.__objc_methname: 0xa3e4
-  __TEXT.__objc_methtype: 0x1b2a
+  __TEXT.__cstring: 0x16094
+  __TEXT.__objc_classname: 0x3f5
+  __TEXT.__objc_methtype: 0x1b9a
+  __TEXT.__gcc_except_tab: 0x4300
+  __TEXT.__objc_methname: 0xa864
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__swift5_typeref: 0x9ee
   __TEXT.__swift5_fieldmd: 0x490

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x23f0
+  __TEXT.__unwind_info: 0x2440
   __TEXT.__eh_frame: 0x10a8
-  __DATA_CONST.__const: 0x2920
-  __DATA_CONST.__cfstring: 0x2200
+  __DATA_CONST.__const: 0x2998
+  __DATA_CONST.__cfstring: 0x2240
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__auth_got: 0x1150
-  __DATA_CONST.__got: 0x8c8
+  __DATA_CONST.__got: 0x8d0
   __DATA_CONST.__auth_ptr: 0x2b8
-  __DATA.__objc_const: 0x3668
-  __DATA.__objc_selrefs: 0x2750
-  __DATA.__objc_ivar: 0x2f4
+  __DATA.__objc_const: 0x3698
+  __DATA.__objc_selrefs: 0x2858
+  __DATA.__objc_ivar: 0x2f8
   __DATA.__objc_data: 0x8c0
-  __DATA.__data: 0x1378
+  __DATA.__data: 0x13e8
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2517
-  Symbols:   914
-  CStrings:  3973
+  Functions: 2551
+  Symbols:   915
+  CStrings:  4074
 
Symbols:
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSMutableOrderedSet
CStrings:
+ " %@"
+ " (%@)"
+ " (%@:%d)"
+ "### Activate failed, unknown type: %@"
+ "### Failed to start %@ extension for %@"
+ "### MigrateAppAccess %@ -> %@ finished, migrated %lu device(s)"
+ "### MigrateAppAccess %@ -> %@, %lu candidate device(s)"
+ "### MigrateAppAccess %@ already has access to %@, re-checking services"
+ "### MigrateAppAccess %@ declares no accessory support, reserving %lu device(s) for it"
+ "### MigrateAppAccess %@ still marked for migration: %@ has no access to %@, so removing %@ could unpair it"
+ "### MigrateAppAccess authorized %@ on %@ for %@, inherited %@, wifiAwarePairingID %llu"
+ "### MigrateAppAccess clearing the migration marker on %@ for %@ failed: %@"
+ "### MigrateAppAccess create reply failed"
+ "### MigrateAppAccess failed: %@ from %@"
+ "### MigrateAppAccess finished migrating %@ on %@%s"
+ "### MigrateAppAccess marked %@ on %@ for migration to %@"
+ "### MigrateAppAccess marking %@ on %@ for migration to %@ failed: %@"
+ "### MigrateAppAccess retagged service '%@' %@ -> %@ on %@"
+ "### MigrateAppAccess rollback of Wi-Fi Aware authorization failed: %@"
+ "### MigrateAppAccess skip %@, %@ holds no transport to migrate"
+ "### MigrateAppAccess skip %@, state %@ is still mid-setup, will retry later"
+ "### MigrateAppAccess skip service '%@' on %@, no authorization"
+ "### MigrateAppAccess skip, no access info for %@ on %@"
+ "### No %@ instance for CapFl %@ (%lu running)"
+ "### No extension point definition for %@ extension"
+ "### ResolvePendingAppMigrations %@"
+ "### ResolvePendingAppMigrations %@ -> %@ failed, will try again later: %@"
+ "### ResolvePendingAppMigrations %@ -> %@ migrated %lu device(s)"
+ "### ResolvePendingAppMigrations get devices failed: %@"
+ "### ResolvePendingAppMigrations unfinished, keeping the access of %@"
+ "### UpdateAppsAccess: %@ inherited access from %@ and declares %@, so keeping it on %@"
+ "### UpdateAppsAccess: %@ now declares %@, which it inherited on %@"
+ "### UpdateAppsAccess: %@ taking over access inherited from %@ on %@, %@ now, %@ later"
+ "### init failed with nil dispatch queue"
+ "### removeAppsAccess %@ is mid-migration, keeping its access to %@"
+ "%@ extension '%@' invalidated: %@"
+ ", source app gone so its record was dropped"
+ "-[DADaemonServer _saveDeviceAppAccessInfo:device:accessoryOptionsCap:error:]"
+ "-[DADaemonServer updateAppAccessInfo:accessoryDevice:removalType:accessoryOptionsCap:error:]"
+ "-[DADaemonServer updateAppAccessInfo:accessoryDevice:removalType:accessoryOptionsCap:error:]_block_invoke"
+ "-[DADaemonServer(AppMigration) _clearPendingMigrationForDevice:fromBundleID:]"
+ "-[DADaemonServer(AppMigration) _markPendingMigrationForDevices:fromBundleID:toBundleID:error:]"
+ "-[DADaemonServer(AppMigration) _migrateAccessoryServiceInfosForDevice:fromBundleID:toBundleID:error:]"
+ "-[DADaemonServer(AppMigration) _migrateAppAccessForDevice:fromBundleID:toBundleID:destinationOptions:outMigrated:error:]"
+ "-[DADaemonServer(AppMigration) _pendingAppMigrationPairs]"
+ "-[DADaemonServer(AppMigration) migrateAppAccessFromBundleID:toBundleID:migratedCount:error:]"
+ "-[DADaemonServer(AppMigration) resolvePendingAppMigrations]"
+ "-[DADaemonXPCConnection _xpcMigrateAppAccess:]"
+ "-[DADaemonXPCConnection _xpcMigrateAppAccess:]_block_invoke"
+ "-[DAExtensionCoordinator _activateExtension:capabilityFlags:]"
+ "-[DAExtensionCoordinator _executeCommandRuntimeAssertion:error:]"
+ "-[DAExtensionCoordinator _extensionEnsureStopped:]"
+ "-[DAExtensionCoordinator _extensionInvalidated:]"
+ "-[DAExtensionCoordinator _extensionWithType:capabilityFlags:]"
+ "-[DAExtensionCoordinator _handleEventLifecycle:]"
+ "-[DAExtensionCoordinator initWithDevice:bundleID:dispatchQueue:]"
+ "@32@0:8q16@24"
+ "@32@0:8q16Q24"
+ "@48@0:8@16@24Q32^@40"
+ "AppMigration"
+ "Authorize Wi-Fi Aware for %@ on %@ failed"
+ "B48@0:8@16@24^Q32^@40"
+ "B56@0:8@16@24q32Q40^@48"
+ "B64@0:8@16@24@32Q40^B48^@56"
+ "Capability %@ ended, %lu still running: %@"
+ "DAAppMigration"
+ "EnsureStopped: %@"
+ "FlushPending: transport %@ has not started its session, deferring message '%@'"
+ "Found extension point: %@"
+ "Marking %@ for migration failed"
+ "MgAA"
+ "MigrateAppAccess: %@ -> %@, from %@"
+ "No destination bundle ID"
+ "No source bundle ID"
+ "RuntimeAssertion: starting %@: CapFl %@"
+ "TB,N,V_mayHavePendingAppMigrations"
+ "_activateExtension:capabilityFlags:"
+ "_appAccessInfoFilenameForBundleID:"
+ "_clearPendingMigrationForDevice:fromBundleID:"
+ "_extensionArray"
+ "_extensionEnsureStopped:"
+ "_extensionInvalidated:"
+ "_extensionWithType:capabilityFlags:"
+ "_extensionWithType:sandboxName:"
+ "_extensionsWithType:"
+ "_markPendingMigrationForDevices:fromBundleID:toBundleID:error:"
+ "_mayHavePendingAppMigrations"
+ "_migrateAccessoryServiceInfosForDevice:fromBundleID:toBundleID:error:"
+ "_migrateAppAccessForDevice:fromBundleID:toBundleID:destinationOptions:outMigrated:error:"
+ "_pendingAppMigrationPairs"
+ "_removeExtension:"
+ "_saveDeviceAppAccessInfo:device:accessoryOptionsCap:error:"
+ "_xpcMigrateAppAccess:"
+ "appendFormat:"
+ "capability %@ is enrolled but not running, dropping event: %@"
+ "capability %@ is not enrolled, dropping event: %@"
+ "extensionFlags"
+ "extensionPointCapabilities"
+ "extensionPointForType:"
+ "extensionsWithType:"
+ "inheritedAccessoryOptions"
+ "initWithDevice:bundleID:dispatchQueue:"
+ "initWithName:authorizationLevel:bundleID:deviceID:"
+ "mayHavePendingAppMigrations"
+ "mgCnt"
+ "mgDst"
+ "mgSrc"
+ "migrateAppAccessFromBundleID:toBundleID:migratedCount:error:"
+ "missing extension with type %@, CapFl %@: %@"
+ "no capability declared for sessionID '%@': %@"
+ "pendingMigrationToBundleID"
+ "process not entitled for migration"
+ "resolvePendingAppMigrations"
+ "sandboxProfileName"
+ "sessionStarted"
+ "setExtensionFlags:"
+ "setExtensionPoint:"
+ "setInheritedAccessoryOptions:"
+ "setMayHavePendingAppMigrations:"
+ "setPendingMigrationTime:"
+ "setPendingMigrationToBundleID:"
+ "setSandboxProfileName:"
+ "setStateRestorationID:"
+ "setUnclaimedMigrationFromBundleID:"
+ "unclaimedMigrationFromBundleID"
+ "unsignedLongLongValue"
+ "updateAppAccessInfo:accessoryDevice:removalType:accessoryOptionsCap:error:"
+ "v32@?0@\"NSNumber\"8@\"NSMutableDictionary\"16^B24"
- "### Failed to start %@ extension, init returned nil"
- "%@ (%@:%d)"
- "%@ extension invalidated: %@"
- "-[DADaemonServer _saveDeviceAppAccessInfo:device:error:]"
- "-[DADaemonServer updateAppAccessInfo:accessoryDevice:removalType:error:]"
- "-[DADaemonServer updateAppAccessInfo:accessoryDevice:removalType:error:]_block_invoke"
- "-[DAExtensionCoordinator _executeCommandRuntimeAssertion:error:]_block_invoke_2"
- "-[DAExtensionCoordinator _extensionInvalidatedWithType:]"
- "-[DAExtensionCoordinator initWithDevice:bundleID:]"
- "FlushPending: transport %@ not yet running (state %d), deferring message '%@'"
- "Skip reporting to session, extension is not running: %@"
- "Skip reporting to session, no extension exists for %@"
- "_extensionEnsureStoppedWithType:"
- "_extensionInvalidatedWithType:"
- "_removeExtensionWithType:"
- "_saveDeviceAppAccessInfo:device:error:"
- "extensionInvalidatedWithType:"
- "extensionWithType:"
- "getExtensionPidByType:"
- "i24@0:8q16"
- "initWithDevice:bundleID:"
- "missing extension with type %@: %@"
- "no capability with sessionID for event: %@"
- "setCapabilityFlag:"
- "unable to get extension with type: %@, %@"
- "v16@?0q8"
- "v32@?0@\"NSString\"8@\"DAExtension\"16^B24"
```
