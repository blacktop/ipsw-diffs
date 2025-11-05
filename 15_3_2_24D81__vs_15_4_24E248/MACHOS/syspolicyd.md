## syspolicyd

> `/usr/libexec/syspolicyd`

```diff

-620.81.1.0.0
-  __TEXT.__text: 0xae830
-  __TEXT.__auth_stubs: 0x29a0
-  __TEXT.__objc_stubs: 0x9500
+620.100.82.0.0
+  __TEXT.__text: 0xb5040
+  __TEXT.__auth_stubs: 0x29d0
+  __TEXT.__objc_stubs: 0x9b00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x4690
-  __TEXT.__const: 0x1d3f
-  __TEXT.__objc_methname: 0xba1d
-  __TEXT.__cstring: 0x10fb8
-  __TEXT.__objc_classname: 0x74b
-  __TEXT.__objc_methtype: 0x1fa4
-  __TEXT.__oslogstring: 0x9048
-  __TEXT.__gcc_except_tab: 0x1b4c
-  __TEXT.__swift5_typeref: 0x38a
+  __TEXT.__objc_methlist: 0x4fec
+  __TEXT.__const: 0x1d74
+  __TEXT.__objc_methname: 0xc3ca
+  __TEXT.__cstring: 0x11aa8
+  __TEXT.__objc_classname: 0x754
+  __TEXT.__objc_methtype: 0x236a
+  __TEXT.__oslogstring: 0x94c8
+  __TEXT.__gcc_except_tab: 0x1c78
+  __TEXT.__swift5_typeref: 0x390
   __TEXT.__swift5_capture: 0x134
+  __TEXT.__constg_swiftt: 0x3dc
+  __TEXT.__swift5_fieldmd: 0x278
+  __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_reflstr: 0x21d
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__constg_swiftt: 0x3a0
-  __TEXT.__swift5_fieldmd: 0x268
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x22a0
-  __TEXT.__eh_frame: 0x218
-  __DATA_CONST.__auth_got: 0x14e8
-  __DATA_CONST.__got: 0x818
-  __DATA_CONST.__auth_ptr: 0x1c8
-  __DATA_CONST.__const: 0x3d18
-  __DATA_CONST.__cfstring: 0x7a40
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __TEXT.__unwind_info: 0x23b0
+  __TEXT.__eh_frame: 0x248
+  __DATA_CONST.__auth_got: 0x1500
+  __DATA_CONST.__got: 0x830
+  __DATA_CONST.__auth_ptr: 0x1d8
+  __DATA_CONST.__const: 0x3d28
+  __DATA_CONST.__cfstring: 0x8820
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_intobj: 0x1e0
-  __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__objc_arrayobj: 0x228
+  __DATA_CONST.__objc_intobj: 0x270
+  __DATA_CONST.__objc_arraydata: 0x588
+  __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0xa4a0
-  __DATA.__objc_selrefs: 0x2ab8
-  __DATA.__objc_ivar: 0x7c4
-  __DATA.__objc_data: 0x2040
-  __DATA.__data: 0xc62
+  __DATA.__objc_const: 0x9af0
+  __DATA.__objc_selrefs: 0x2ce0
+  __DATA.__objc_ivar: 0x7e4
+  __DATA.__objc_data: 0x20f8
+  __DATA.__data: 0xc92
   __DATA.__bss: 0xabd
   __DATA.__common: 0x3c0
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/Bootability.framework/Versions/A/Bootability
+  - /System/Library/PrivateFrameworks/CloudTelemetry.framework/Versions/A/CloudTelemetry
   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate
   - /System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/Versions/A/WirelessDiagnostics

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4C616638-884F-3FBC-BAED-D716E2B7D93A
-  Functions: 3320
-  Symbols:   1005
-  CStrings:  6269
+  UUID: 2C0C98B4-F1C0-3C64-BDA2-CB5A07894F8B
+  Functions: 3419
+  Symbols:   1014
+  CStrings:  6579
 
Symbols:
+ _$s14CloudTelemetryAAC25setupXpcServiceActivitiesyyKFZ
+ _$s14CloudTelemetryAACMa
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _CP_ConfigurationProfilesAreInstalled
+ _OBJC_CLASS_$_CloudTelemetryReporter
+ _OBJC_CLASS_$_LPStaticAPFSVolume
+ _OBJC_CLASS_$_LPStaticMedia
+ _OBJC_CLASS_$_SPProvenanceTracking
+ _OBJC_CLASS_$_SUPreferenceManager
+ _TCCAccessCopyBundleIdentifiersForService
+ _XProtectUpdateServiceErrorNeedsDefer
+ __kCFURLDiskImageBackingURLKey
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _os_variant_allows_internal_security_policies
+ _responsibility_get_responsible_for_pid
+ _tcc_metrics_create
+ _tcc_metrics_set_service_name
+ _tcc_server_create
+ _tcc_server_send_analytics
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _OBJC_CLASS_$_LPAPFSVolume
- _OBJC_CLASS_$_LPMedia
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
CStrings:
+ "/.nofollow/private/var/db/gke.bundle/"
+ "/.nofollow/var/db/.LastGKReject"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/file/file/src/softmagic.c"
+ "/System/AppleInternal/Library/Frameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity"
+ "10"
+ "9"
+ "Alacritty.app"
+ "App wrapper check failed for %@, %@"
+ "B32@0:8@\"NSString\"16@\"NSDictionary\"24"
+ "B32@0:8Q16@\"NSDictionary\"24"
+ "CKTicketStore using CK settings: %@:%@"
+ "CREATE TABLE historic_gk_overrides (  pk INTEGER PRIMARY KEY AUTOINCREMENT,  timestamp INTEGER NOT NULL)"
+ "CREATE TABLE historic_malware_blocks (  pk INTEGER PRIMARY KEY AUTOINCREMENT,  timestamp INTEGER NOT NULL)"
+ "CREATE TABLE historic_malware_blocks (  pk INTEGER PRIMARY KEY AUTOINCREMENT,  timestamp INTEGER NOT NULL,  cdhash TEXT UNIQUE)"
+ "Canceling unrevoked cleanup"
+ "CloudTelemetry error while reporting %{public}@: %{public}@"
+ "DELETE FROM policy_scan_cache where cdhash = ?1"
+ "DELETE FROM policy_scan_cache_by_path where cdhash = ?1"
+ "DELETE FROM tickets WHERE hash = ?1 AND hash_type = ?2"
+ "DROP TABLE IF EXISTS historic_malware_blocks"
+ "Denying target with bad app wrapper: %@"
+ "Error querying revoked hashes: %d"
+ "Examining hash %@ and got %@ %@"
+ "Failed to derevoke %@"
+ "Failed to initialize Cloud Telemetry: %@"
+ "Failed to mark GK override: %{public}d"
+ "Failed to mark malware block: %{public}d"
+ "Failed to read last GK override: %{public}d"
+ "Failed to read last malware block: %{public}d"
+ "Finished Xprotect update in %{public}@ ms: %{public}@"
+ "GK Policy: Internal"
+ "GK protection status: %lld"
+ "GKTicket[%@ - %@ %@, %d]"
+ "GkProtectionStatus"
+ "Going to retry Xprotect update"
+ "History"
+ "INSERT INTO historic_gk_overrides (timestamp) VALUES (?1);"
+ "INSERT INTO historic_malware_blocks (timestamp, cdhash) VALUES (?1, ?2)"
+ "INSERT INTO historic_malware_blocks (timestamp, cdhash) VALUES (?1, ?2)  ON CONFLICT DO UPDATE SET timestamp = excluded.timestamp"
+ "MalwareDiscovered2"
+ "MalwareDiscoveredLite"
+ "Process path doesn't match Wrappedbundle symlink: %@, %@"
+ "Revoked hash %@ no longer has a revocation ticket, unrevoking"
+ "SELECT COUNT(*) FROM executable_measurements_v2 WHERE bundle_identifier = ?1 AND timestamp >= strftime('%s', 'now') - ?2"
+ "SELECT COUNT(*) FROM historic_gk_overrides WHERE timestamp >= strftime('%s', 'now') - ?1"
+ "SELECT COUNT(*) FROM historic_malware_blocks WHERE timestamp >= strftime('%s', 'now') - ?1"
+ "SELECT COUNT(*) FROM policy_scan_cache WHERE (flags & (?1)) != 0"
+ "SELECT COUNT(*) FROM policy_scan_cache WHERE signing_identifier = ?1"
+ "SELECT COUNT(*) FROM policy_scan_cache_by_path WHERE (flags & (?1)) != 0"
+ "SELECT COUNT(*) FROM policy_scan_cache_by_path WHERE signing_identifier = ?1"
+ "SELECT hash, hash_type from tickets WHERE (flags & ?1) != 0"
+ "SELECT timestamp FROM historic_gk_overrides ORDER BY pk DESC LIMIT 1"
+ "SELECT timestamp FROM historic_malware_blocks ORDER BY pk DESC LIMIT 1"
+ "Sent %@: %{boolean}d"
+ "Sent CloudTelemetry event: %{public}@"
+ "T@\"NSDate\",R,N,V_createdTime"
+ "TB,N,V_isBadAppWrapper"
+ "TB,N,V_newGatekeeperEnabled"
+ "TB,N,VfailedAppWrapperSymlinkPolicy"
+ "TB,N,VjobWantsDeferal"
+ "TB,R,N,V_isBackingDMGNotarized"
+ "Terminal.app"
+ "UX5GW259T3"
+ "Unable to create historic_gk_overrides"
+ "Unable to create historic_malware_blocks"
+ "Unable to create version 10 schema: %d"
+ "Unable to create version 9 schema: %d"
+ "Unable to delete historic_malware_blocks"
+ "Unable to re-create historic_malware_blocks"
+ "Unrevoked ticket: %@ %@"
+ "WrappedBundle symlink points outside of the bundle: %@, %@"
+ "XPBehavioralDetection"
+ "Xprotectupdateresult"
+ "_createdTime"
+ "_isBackingDMGNotarizationChecked"
+ "_isBackingDMGNotarized"
+ "_isBadAppWrapper"
+ "allRevokedHashes"
+ "anyConfigurationProfilesInstalled"
+ "automaticallyInstallConfigDataAndSecurityUpdates"
+ "bastionVersion"
+ "behavior"
+ "blockType"
+ "block_type"
+ "blocksSince:"
+ "checkAppWrapperWithURL:withProcessURL:"
+ "cleanupUnrevokedTickets:"
+ "com.apple.private.security.syspolicy.report-metrics"
+ "com.apple.syspolicyd"
+ "com.apple.syspolicyd: existing_deprecated_kext"
+ "com.bitTorrent.btweb"
+ "com.bitTorrent.utweb"
+ "com.bittorrent.BitTorrent"
+ "com.bittorrent.uTorrent"
+ "com.crowdstrike.falcon.App"
+ "com.kaspersky.kav"
+ "com.kaspersky.kav_agent"
+ "com.kaspersky.ksec"
+ "com.sentinelone.extensions-wrapper"
+ "com.sentinelone.sentinel-agent"
+ "createdTime"
+ "dailyBlocks"
+ "dailyGKOverrides"
+ "dailyMalwareBlocks"
+ "dailyOverrides"
+ "distantPast"
+ "doUpdate:"
+ "evaluation_path"
+ "exec_cdhash"
+ "exec_filename"
+ "exec_is_notarized"
+ "exec_sha256"
+ "exec_signingid"
+ "exec_teamid"
+ "executable_cdhash"
+ "executable_creation_time"
+ "executable_path"
+ "executable_sha256"
+ "executable_signingid"
+ "executable_teamid"
+ "failedAppWrapperSymlinkPolicy"
+ "failure"
+ "filename"
+ "findProvenanceEntryForURL:"
+ "getLastMalwareBlock"
+ "getLastTerminalLaunch"
+ "gkEnabled"
+ "gkPolicy"
+ "iTerm2.app"
+ "invalid"
+ "isAnyBundleIdentifierPresent:"
+ "isBackingDMGNotarized"
+ "isBadAppWrapper"
+ "isBundleIdentiferPresent:"
+ "isDeveloperOverridePresent"
+ "isGreaterThan:"
+ "isTerminalDotAppPresentWithin:"
+ "is_first_block"
+ "is_first_launch"
+ "jobWantsDeferal"
+ "lastTerminalLaunch"
+ "migrateToV10"
+ "migrateToV9"
+ "monthlyBlocks"
+ "monthlyGKOverrides"
+ "monthlyMalwareBlocks"
+ "monthlyOverrides"
+ "newGatekeeperEnabled"
+ "notifyBlockedSoftwareForUser:withPID:withProcessPath:withLibraryPath:withRuleName:withSamplingUUID:withMatchType:withBlockType:withRuleVersion:withEvaluationPath:isSilentlyBlocked:"
+ "org.m0k.transmission"
+ "org.qbittorrent.qBittorrent"
+ "originalVersion"
+ "overridesSince:"
+ "previousVersion"
+ "profile_hash"
+ "provenance_bundleid"
+ "provenance_filename"
+ "provenance_path"
+ "provenance_sha256"
+ "registerCloudTelemetryActivities"
+ "removePolicyScanCacheTargetForHash:"
+ "removeTicketByHash:"
+ "removeTicketByHash:withType:"
+ "reportEvent:withData:withReply:"
+ "reportWithTeamID:eventType:event:allowCellularAccess:allowExpensiveAccess:bundleID:error:"
+ "responsible_cdhash"
+ "responsible_creation_time"
+ "responsible_filename"
+ "responsible_is_notarized"
+ "responsible_path"
+ "responsible_provenance_bundleid"
+ "responsible_provenance_cdhash"
+ "responsible_provenance_path"
+ "responsible_provenance_signingid"
+ "responsible_provenance_teamid"
+ "responsible_sha256"
+ "responsible_signingid"
+ "responsible_teamid"
+ "rule_name"
+ "secEnabled"
+ "selectedSource"
+ "selectedVersion"
+ "sendEvaluationMetrics:withEvaluationType:withCurrentPolicy:withEvaluationArguments:forScanResults:forScanTarget:wasFirstBlock:"
+ "sendFastTelemetryEvent:andData:"
+ "sendMalwareDiscoveredFull:withCdhash:withCreationTime:withTeamID:withSigningID:withEvaluationPath:isFirstBlock:isFirstLaunch:withBlockType:withMatchedRule:isSilentRule:withResponsibleFile:withResponsibleCdhash:withResponsibleCreationTime:withResponsibleTeamID:withResponsibleSigningID:withCurrentGKPolicy:withXProtectVersion:withXProtectPayloadsVersion:withGKStatus:withDailyGKOverrides:withWeeklyGKOverrides:withMonthlyGKOverrides:withYearlyGKOverrides:withDailyMalwareInfections:withWeeklyMalwareInfections:withMonthlyMalwareInfections:withYearlyMalwareInfections:withUserClassification:"
+ "sendMalwareDiscoveredLite:withCdhash:withBlockType:withMatchedRule:withXProtectVersion:isSilent:"
+ "sendProtectionStatus:withGKStatus:withXProtectVersion:withXProtectPayloadsVersion:withSecurityUpdateStatus:withDailyGKOverrides:withWeeklyGKOverrides:withMonthlyGKOverrides:withYearlyGKOverrides:withDailyMalwareInfections:withWeeklyMalwareInfections:withMonthlyMalwareInfections:withYearlyMalwareInfections:withUserClassification:"
+ "sendXProtectEventLazyWithEventName:andData:"
+ "sendXProtectUpdateCompletion:withVersion:withSelectedSource:withOriginalVersion:withTotalTime:"
+ "setFailedAppWrapperSymlinkPolicy:"
+ "setIsBadAppWrapper:"
+ "setJobWantsDeferal:"
+ "setLastMalwareBlock:forCDHash:"
+ "setLastTerminalLaunch:"
+ "setNewGatekeeperEnabled:"
+ "sha256"
+ "silent"
+ "silent_rule"
+ "stringValue"
+ "totalTime"
+ "unable to allocate string"
+ "unable to get responsible path (%d) for pid %d"
+ "userBehaviors"
+ "userClassification"
+ "v120@0:8Q16B24@\"NSString\"28@\"NSString\"36B44@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72@\"NSNumber\"80@\"NSNumber\"88@\"NSNumber\"96@\"NSNumber\"104@\"NSNumber\"112"
+ "v120@0:8Q16B24@28@36B44@48@56@64@72@80@88@96@104@112"
+ "v232@0:8@\"NSURL\"16@\"NSString\"24@\"NSDate\"32@\"NSString\"40@\"NSString\"48Q56B64B68Q72@\"NSString\"80B88@\"NSURL\"92@\"NSString\"100@\"NSDate\"108@\"NSString\"116@\"NSString\"124Q132@\"NSString\"140@\"NSString\"148B156@\"NSNumber\"160@\"NSNumber\"168@\"NSNumber\"176@\"NSNumber\"184@\"NSNumber\"192@\"NSNumber\"200@\"NSNumber\"208@\"NSNumber\"216@\"NSNumber\"224"
+ "v232@0:8@16@24@32@40@48Q56B64B68Q72@80B88@92@100@108@116@124Q132@140@148B156@160@168@176@184@192@200@208@216@224"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
+ "v56@0:8@\"NSError\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48"
+ "v56@0:8@16@24@32@40@48"
+ "v60@0:8@\"NSURL\"16@\"NSString\"24Q32@\"NSString\"40@\"NSNumber\"48B56"
+ "v60@0:8@16@24Q32@40@48B56"
+ "v68@0:8@16Q24Q32@40@48@56B64"
+ "v88@0:8I16i20@24@32@40@48i56Q60@68Q76B84"
+ "valid"
+ "weeklyBlocks"
+ "weeklyGKOverrides"
+ "weeklyMalwareBlocks"
+ "weeklyOverrides"
+ "xpVersion"
+ "xprotectVersion"
+ "yearlyBlocks"
+ "yearlyGKOverrides"
+ "yearlyMalwareBlocks"
+ "yearlyOverrides"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/file/file/src/softmagic.c"
- "/private/var/db/gke.bundle/"
- "/var/db/.LastGKReject"
- "App wrapper has bad symlink: %@, %@"
- "Fatal error"
- "Finished Xprotect update: %@"
- "Go"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TB,R,N,V_hasBadAppWrapperSymlink"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_hasBadAppWrapperSymlink"
- "checkAppWrapperSymlink:"
- "doUpdate"
- "hasBadAppWrapperSymlink"
- "invalid Collection: less than 'count' elements in collection"
- "notifyBlockedSoftwareForUser:withProcessPath:withLibraryPath:withRuleName:withSamplingUUID:withMatchType:withBlockType:withRuleVersion:withEvaluationPath:isSilentlyBlocked:"
- "sendEvaluationMetrics:withEvaluationType:withCurrentPolicy:withEvaluationArguments:forScanResults:forScanTarget:"
- "v64@0:8@16Q24Q32@40@48@56"
- "v84@0:8I16@20@28@36@44i52Q56@64Q72B80"
- "x"

```
