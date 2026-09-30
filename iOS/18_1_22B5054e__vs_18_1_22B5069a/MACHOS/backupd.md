## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2349.40.54.0.1
-  __TEXT.__text: 0x28e360
+2349.40.65.0.0
+  __TEXT.__text: 0x28de14
   __TEXT.__auth_stubs: 0x3300
   __TEXT.__objc_stubs: 0x2bca0
-  __TEXT.__objc_methlist: 0x185a4
-  __TEXT.__cstring: 0x6f5d6
-  __TEXT.__objc_methname: 0x39b40
-  __TEXT.__const: 0x15a0
+  __TEXT.__objc_methlist: 0x185d4
+  __TEXT.__cstring: 0x6f69e
+  __TEXT.__objc_methname: 0x39c86
+  __TEXT.__const: 0x15b0
   __TEXT.__constg_swiftt: 0x910
   __TEXT.__swift5_typeref: 0xbc9
   __TEXT.__swift5_reflstr: 0x7bb

   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_types: 0x94
-  __TEXT.__objc_classname: 0x2157
-  __TEXT.__objc_methtype: 0x6a52
-  __TEXT.__oslogstring: 0x32b9e
+  __TEXT.__objc_classname: 0x2151
+  __TEXT.__objc_methtype: 0x6a55
+  __TEXT.__oslogstring: 0x32c16
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x384
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xceb8
+  __TEXT.__gcc_except_tab: 0xceb4
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x70b0
-  __TEXT.__eh_frame: 0x1c98
+  __TEXT.__unwind_info: 0x70a8
+  __TEXT.__eh_frame: 0x1cd0
   __DATA_CONST.__auth_got: 0x1990
   __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__auth_ptr: 0x348
+  __DATA_CONST.__auth_ptr: 0x368
   __DATA_CONST.__const: 0x88b8
-  __DATA_CONST.__cfstring: 0x1fa60
+  __DATA_CONST.__cfstring: 0x1fa80
   __DATA_CONST.__objc_classlist: 0xab0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x280

   __DATA_CONST.__objc_arraydata: 0xd28
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x4e0
-  __DATA.__objc_const: 0x29be0
-  __DATA.__objc_selrefs: 0xc7d0
-  __DATA.__objc_ivar: 0x1dc0
+  __DATA.__objc_const: 0x29c50
+  __DATA.__objc_selrefs: 0xc7f0
+  __DATA.__objc_ivar: 0x1dc8
   __DATA.__objc_data: 0x74f0
   __DATA.__data: 0x20e8
   __DATA.__common: 0x49

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10248
+  Functions: 10249
   Symbols:   1399
-  CStrings:  24767
+  CStrings:  24779
 
CStrings:
+ "\n SELECT \n    SUM(IIF(restoreState == %!u(MISSING), 1, 0)),\n    SUM(IIF(restoreState == %!u(MISSING), 1, 0)),\n    COUNT(*)\n FROM Restorables"
+ "\x12'\xf07"
+ ", but found existing open plan at "
+ "-[MBBackgroundRestoreProgressMonitor initWithAccount:serviceManager:thermalPressureMonitor:snapshotUUID:]"
+ "=asset-fetch= Fetched asset record %!@(MISSING) for ino: %!l(MISSING)lu at %!@(MISSING)"
+ "=bg-estimate= Failed to open plan for sizing: %!@(MISSING)"
+ "=ckrestore-engine= =sync= Failed to open a restore plan to synchronize into: %!@(MISSING)"
+ "=ckrestore-engine= Failed to load restore plan for background restore: %!@(MISSING)"
+ "=ckrestore-engine= Failed to load restore plan: %!@(MISSING)"
+ "=snapshot-policy= Target snapshot %!@(MISSING) format (%!@(MISSING)) does not contain assets, falling back to Legacy"
+ "@60@0:8@16B24B28B32i36i40^@44@52"
+ "Clearing existing restore plan: "
+ "Deleting DB at %!@(MISSING)"
+ "Deposited asset (ino: "
+ "Expected plan at "
+ "Failed to get plan to set priority: %!@(MISSING)"
+ "Failed to remove the DB on attempt %!d(MISSING) opening at %!@(MISSING): %!@(MISSING)"
+ "Failed to remove the database while creating SQLite connection at %!@(MISSING): %!@(MISSING), remove error: %!@(MISSING)"
+ "Failed to set priority in plan for path %!@(MISSING): %!@(MISSING)"
+ "Failed to truncate the database at %!@(MISSING): %!d(MISSING): %!@(MISSING)"
+ "No existing plan to clear"
+ "No snapshot UUID to open restore plan"
+ "Not deleting DB on attempt %!d(MISSING) opening at %!@(MISSING): %!@(MISSING)"
+ "Not deleting DB while creating SQLite connection at %!@(MISSING): %!@(MISSING)"
+ "Not updating bundleID to personaID mapping because it was already set by MDM"
+ "RepairedDomains"
+ "SkippedFileListCloneDomains"
+ "T@\"NSMutableSet\",&,N,V_repairedDomains"
+ "T@\"NSMutableSet\",&,N,V_skippedFileListCloneDomains"
+ "T@\"NSString\",R,N,V_snapshotUUID"
+ "TB,R,N,V_shouldDeleteOnFailureToOpen"
+ "_TtC7backupd14MBPersonaState"
+ "_repairedDomains"
+ "_shouldDeleteOnFailureToOpen"
+ "_skippedFileListCloneDomains"
+ "hasSetPersonaMappingForRestore"
+ "initWithAccount:serviceManager:snapshotUUID:"
+ "initWithAccount:serviceManager:thermalPressureMonitor:snapshotUUID:"
+ "initWithPath:readOnly:"
+ "initWithPath:readOnly:shouldDeleteOnFailureToOpen:usePQLBatching:schemaCurrentVersion:schemaMinDatabaseVersionForUpgrade:error:schemaUpgrades:"
+ "openDatabaseIn:commitID:readOnly:error:"
+ "openOrUseExistingPlanWithPersona:snapshotUUID:error:"
+ "repairedDomains"
+ "restorePlanForAccount:snapshotUUID:error:"
+ "setRepairedDomains:"
+ "setSkippedFileListCloneDomains:"
+ "shouldDeleteOnFailureToOpen"
+ "skippedFileListCloneDomains"
+ "trackRepairedDomain:"
+ "trackSkippedFileListCloneDomain:"
- "\x02#"
- "\n SELECT \n    SUM(IIF(restoreState == %!u(MISSING), 1, 0)),\n    SUM(IIF(restoreState == %!u(MISSING), 1, 0)),\n    COUNT(*)\n FROM Restorables\n JOIN  Domains ON\n       Domains.domainID = Restorables.domainID\n WHERE Domains.rootPath IS NOT NULL"
- "\x11\x12"
- "\x12'\xf06"
- "-[MBBackgroundRestoreProgressMonitor initWithAccount:serviceManager:thermalPressureMonitor:]"
- "=asset-fetch= Fetched asset record %!@(MISSING) for asset %!@(MISSING) at %!@(MISSING)"
- "=ckdomain-engine= =domain-engine= Setting Legacy dir handled by restore plan: %!@(MISSING)"
- "=ckdomain-engine= Failed to verify background container restore for %!@(MISSING): %!@(MISSING)"
- "=ckdomain-engine= Finalized domain (%!@(MISSING)): %!@(MISSING)"
- "=ckdomain-engine= Fixed up Lightrail directory attributes: %!@(MISSING):%!@(MISSING)"
- "=ckdomain-engine= Placed Lightrail dir: %!@(MISSING):%!@(MISSING)"
- "=ckdomain-engine= Successfully verified background container restore for %!@(MISSING)"
- "=snapshot-policy= Target snapshot %!@(MISSING) format (%!@(MISSING)) is not supported, falling back to Legacy"
- "@56@0:8@16B24B28i32i36^@40@48"
- "Deposited asset "
- "Failed to set plan priority for path %!@(MISSING): %!@(MISSING)"
- "Fixed up directory attributes at "
- "Loading restore state opened plan: %!@(MISSING)"
- "Loading restore state used existing plan: %!@(MISSING)"
- "Placed directory at "
- "Removing the db at %!@(MISSING)"
- "RepairedDomainNames"
- "Setting restore session opened plan: %!@(MISSING)"
- "Setting restore session used existing plan: %!@(MISSING)"
- "T@\"NSMutableSet\",&,N,V_repairedDomainNames"
- "_TtC7backupd12PersonaState"
- "_domainRestorePlan"
- "_repairedDomainNames"
- "hasOpenRestorePlanWithPersona:snapshotUUID:"
- "initWithAccount:serviceManager:"
- "initWithAccount:serviceManager:thermalPressureMonitor:"
- "initWithPath:readOnly:usePQLBatching:schemaCurrentVersion:schemaMinDatabaseVersionForUpgrade:error:schemaUpgrades:"
- "initWithPath:readonly:"
- "openDatabaseIn:commitID:readonly:error:"
- "openRestorePlanWithPersona:snapshotUUID:error:"
- "repairedDomainNames"
- "restorePlanForAccount:"
- "setRepairedDomainNames:"
- "trackRepairedDomainName:"

```
