## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`
- `__DATA.__common`

```diff

-910.0.0.0.0
-  __TEXT.__text: 0x85964
-  __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_stubs: 0xb1c0
-  __TEXT.__objc_methlist: 0x52f4
-  __TEXT.__cstring: 0x120c4
+913.0.0.0.0
+  __TEXT.__text: 0x8bbb4
+  __TEXT.__auth_stubs: 0x1650
+  __TEXT.__objc_stubs: 0xb680
+  __TEXT.__objc_methlist: 0x5504
+  __TEXT.__cstring: 0x12a07
   __TEXT.__const: 0x6f8
-  __TEXT.__gcc_except_tab: 0x2d8c
-  __TEXT.__objc_methname: 0x12795
-  __TEXT.__oslogstring: 0xf4f1
-  __TEXT.__objc_classname: 0x6ce
-  __TEXT.__objc_methtype: 0x22f6
+  __TEXT.__gcc_except_tab: 0x2fe8
+  __TEXT.__objc_methname: 0x13084
+  __TEXT.__oslogstring: 0x10851
+  __TEXT.__objc_classname: 0x6da
+  __TEXT.__objc_methtype: 0x235f
   __TEXT.__dlopen_cstrs: 0x90
-  __TEXT.__unwind_info: 0x1958
-  __DATA_CONST.__const: 0x27c8
-  __DATA_CONST.__cfstring: 0x8940
+  __TEXT.__unwind_info: 0x1a58
+  __DATA_CONST.__const: 0x28c0
+  __DATA_CONST.__cfstring: 0x8b00
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_intobj: 0x660
-  __DATA_CONST.__objc_arraydata: 0x1620
+  __DATA_CONST.__objc_arraydata: 0x1608
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0xeb0
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__auth_got: 0xb38
+  __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0xa1b0
-  __DATA.__objc_selrefs: 0x35a8
-  __DATA.__objc_ivar: 0x708
+  __DATA.__objc_const: 0xa350
+  __DATA.__objc_selrefs: 0x3700
+  __DATA.__objc_ivar: 0x728
   __DATA.__objc_data: 0x1360
-  __DATA.__data: 0x730
-  __DATA.__bss: 0x431
+  __DATA.__data: 0x738
+  __DATA.__bss: 0x439
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2924
+  Functions: 3014
   Symbols:   506
-  CStrings:  5741
+  CStrings:  5901
 
Symbols:
+ _kTCCServiceAll
- _exit
CStrings:
+ "\n\n"
+ " (auth_value preserved; per-system service)"
+ "%@, %@"
+ "%@_WITH_ORG_NAME"
+ "%@|%@"
+ "%@|%@|%d"
+ "%s: all %lu queued reminder(s) within their drain-throttle window, nothing to drain"
+ "%s: failed to deserialize drain state plist: %{public}@"
+ "%s: failed to serialize drain state plist: %{public}@"
+ "%s: failed to write drain state plist to %{public}@: %{public}@"
+ "%s: no drain state plist found at %{public}@, nothing to restore"
+ "%s: prompt not shown for %{public}s/%{public}s, re-queuing without arming throttle"
+ "%s: restored drain state for %lu service(s)"
+ "%s: service %{public}s within drain-throttle window, skipping"
+ "%{public}s: failed to query managed_overrides for (service=%{public}@, client=%@): %d"
+ "%{public}s: failed to write back managed_overrides for (service=%{public}@, client=%{public}@): %d"
+ "%{public}s: ignoring inbound watch access change for admin-locked managed row (service=%{public}@, client=%{public}@, currentAuthValue=%lld)"
+ "%{public}s: managed row already at authValue=%lld, no-op"
+ "%{public}s: managed row is soft-deleted, falling through to access write (service=%{public}@, client=%{public}@)"
+ "%{public}s: no replica mapping for main client %{public}@, skipping"
+ "%{public}s: skipping non-translatable managed override for service=%{public}@ client=%{public}@"
+ "%{public}s: wrote watch-originated value %llu back to managed_overrides (service=%{public}@, client=%{public}@)"
+ "-[TCCDMainSyncController syncDegradedManagedOverrideForServiceIdentifier:mainClientIdentifier:clientType:authValue:flags:updateType:]"
+ "-[TCCDMainSyncController syncManagedOverrideForServiceIdentifier:mainClientIdentifier:clientType:adminAuthValue:userAuthValue:authReason:authorizationVersion:updateType:degradeWhenUnsupported:]"
+ "-[TCCDReminderMonitor persistDrainStateToDisk]"
+ "-[TCCDReminderMonitor restoreDrainState]"
+ "0"
+ "1"
+ "@\"NSMutableSet\""
+ "A!"
+ "All"
+ "Application Installed"
+ "B32@0:8@16d24"
+ "B32@0:8@16q24"
+ "ClientDisplayName"
+ "Could not resolve NanoRegistry capabilities-changed notification constant; peer-capability migration trigger disabled."
+ "DELETE FROM managed_overrides WHERE service = ?"
+ "DELETE FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
+ "Failed to construct localized enabled-notification string for service %{public}@ and subject %{public}@"
+ "Failed to delete managed_overrides for client %{public}@ type %d (%d)"
+ "Failed to mark managed_overrides row stale: serviceName=%{public}@, identifier=%{public}@"
+ "Failed to obtain localized button title for enabled-notification for service %{public}@"
+ "Failed to persist peer managed-overrides capability: %{public}@"
+ "Failed to upsert managed_overrides row for MDM policy: serviceName=%{public}@, identifier=%{public}@, identifier_type=%lld"
+ "Handling Application Installed event for %{public}@."
+ "Have %lu managed override actions to degrade for newly-installed apps."
+ "INSERT INTO managed_overrides (service, client, client_type, admin_auth_value, auth_reason, auth_version,  auth_value, csreq, policy_id, indirect_object_identifier_type, indirect_object_identifier,  indirect_object_code_identity, flags) VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, 'UNUSED', NULL, ?)"
+ "ManagedSettings: accessRightForManagedAuthValue: unexpected value %lld, mapping to UNKNOWN"
+ "ManagedSettings: applying %lu forwarded per-system clients on system tccd"
+ "ManagedSettings: canTranslate: service is nil, skipping"
+ "ManagedSettings: canTranslate: skipping non-translatable auth value %lld for service %{public}@"
+ "ManagedSettings: cleared %d legacy kTCCServiceAccessibility row(s) from user-agent managed_overrides (now owned by system tccd)"
+ "ManagedSettings: database is nil, cannot apply forwarded system permissions"
+ "ManagedSettings: database is nil, cannot clear legacy Accessibility records"
+ "ManagedSettings: deleted %{public}@ - %{public}@ (admin pushed None, prompt not presented)"
+ "ManagedSettings: failed to clear legacy kTCCServiceAccessibility rows: %d"
+ "ManagedSettings: failed to create XPC message for system tccd forward"
+ "ManagedSettings: failed to delete None record %{public}@:%{public}@: %d"
+ "ManagedSettings: failed to dispatch system tccd forward message"
+ "ManagedSettings: forwarding %lu per-system clients to system tccd"
+ "ManagedSettings: ignoring None for %{public}@:%{public}@ - disclosure already presented, record preserved"
+ "ManagedSettings: inserted managed_overrides for %{public}@:%{public}@ admin_auth_value=%lld auth_value=%lld (result=%d)"
+ "ManagedSettings: managedTCC feature disabled — NOT writing managed_overrides for %{public}@:%{public}@ (admin_auth_value=%lld). MDM grant will not take effect via managed path."
+ "ManagedSettings: marked %{public}@ - %{public}@ as stale (removed from policy)%{public}s"
+ "ManagedSettings: system tccd forward acknowledged"
+ "ManagedSettings: system tccd forward failed: %{public}s"
+ "ManagedSettings: updated managed_overrides for %{public}@:%{public}@ admin_auth_value=%lld (result=%d)"
+ "ManagedSettings: upsert managed_overrides from MDM policy for %{public}@:%{public}@ admin_auth_value=%lld"
+ "NRPairedDeviceRegistryPairedDeviceDidChangeCapabilitiesDarwinNotification"
+ "Override: Organization name is set to %@"
+ "Override: routing %{public}@ for %{public}@ to managed_overrides (admin_auth_value=%lld)"
+ "PayloadOrganization"
+ "Peer capabilities changed: peer now supports managed_overrides with no prior managed sync recorded; forcing a reset sync to migrate any degraded access state."
+ "Peer supports managed_overrides but no prior managed sync recorded; forcing a reset sync to migrate any degraded access state."
+ "PeerManagedOverridesCapability"
+ "REMINDER_ACCESS_INFO"
+ "REMINDER_ACCESS_PURPOSE"
+ "Registered for paired-device capability changes (managed_overrides upgrade trigger)."
+ "SELECT   service,   client,   client_type,   auth_value,   auth_reason,   auth_version,   admin_auth_value,   flags,   last_modified FROM managed_overrides WHERE client = ? AND client_type = ? AND (NOT (flags & ?) OR auth_value = ?)"
+ "SELECT COUNT(*) FROM managed_overrides WHERE service = ?"
+ "SELECT auth_value, auth_reason, auth_version, flags, csreq FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
+ "SELECT auth_value, flags FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
+ "SELECT client FROM managed_overrides WHERE service = ? AND client_type = ? AND admin_auth_value != 0 AND auth_value != ?"
+ "SELECT client FROM managed_overrides WHERE service = ? AND client_type = ? AND admin_auth_value = 0 AND auth_value != ?"
+ "SELECT client, client_type, auth_value, auth_reason, auth_version, admin_auth_value, last_modified, flags FROM managed_overrides WHERE service = ? AND auth_value != ?"
+ "SELECT service, auth_value, auth_reason, auth_version, admin_auth_value, flags FROM managed_overrides WHERE client = ? AND client_type = ? AND auth_value != ?"
+ "SELECT service, client, client_type FROM managed_overrides WHERE (flags & ?) AND NOT (flags & ?)"
+ "SELECT service, client, client_type, auth_value, auth_reason, admin_auth_value, flags, last_modified, csreq FROM managed_overrides WHERE 1=1"
+ "SELECT service, flags, csreq from managed_overrides WHERE client=? AND client_type=?"
+ "Site F (degrade): skipping non-translatable managed row service=%{public}@ client=%{public}@"
+ "Site F (degrade): syncing degraded access action for newly installed WatchKit app: %@"
+ "T@\"NSMutableDictionary\",&,N,V_lastDrainTimeByService"
+ "T@\"NSMutableSet\",&,N,V_notifiedEnableRecordKeys"
+ "T@\"NSString\",&,N,V_orgName"
+ "T@\"NSString\",&,N,V_reminderMessageTextLocalizationKey"
+ "T@\"NSString\",&,N,V_reminderPurposeFormatLocalizationKey"
+ "TB,N,V_mdm_migratingProfileToManagedSettings"
+ "TCCManagedSettingsApplyForSystemServices"
+ "Td,N,V_drainThrottleInterval"
+ "Ti,V_peerCapabilitiesNotifyToken"
+ "Translation"
+ "UPDATE managed_overrides SET   admin_auth_value = ?,   auth_value = CASE WHEN auth_reason IN (?, ?) THEN auth_value ELSE ? END,   auth_reason = ?,   flags = ((flags | ?) & ~?),   last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET   auth_value = ?,   flags = (flags | ?),   last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET auth_value = ?, auth_reason = ?, flags = (flags | ?), last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET auth_value = ?, auth_reason = ?, last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET flags = (flags | ?), last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "_beginResetSyncHook (degrade): skipping non-translatable managed row service=%{public}@ client=%{public}@"
+ "_beginResetSyncHook (degrade): skipping user-undecided managed row (no authoritative phone decision to push) service=%{public}@ client=%{public}@"
+ "_degradeOutgoingDeltaChanges:"
+ "_degradeOutgoingDeltaChanges: rewrote outbound Reset -> degraded access (managed row present) service=%{public}@ client=%{public}@"
+ "_drainThrottleInterval"
+ "_forwardSystemPermissionsToSystemTCCD:"
+ "_handlePeerManagedOverridesCapabilityDidChange"
+ "_lastDrainTimeByService"
+ "_lastKnownPeerManagedOverridesSupport"
+ "_mdm_migratingProfileToManagedSettings"
+ "_notifiedEnableRecordKeys"
+ "_orgName"
+ "_peerCapabilitiesNotifyToken"
+ "_peerManagedOverridesCapabilityFile"
+ "_persistPeerManagedOverridesSupport:"
+ "_registerForPeerCapabilityChanges"
+ "_reminderMessageTextLocalizationKey"
+ "_reminderPurposeFormatLocalizationKey"
+ "accessRightForManagedAuthValue:"
+ "applyForwardedSystemPermissions:"
+ "canTranslateManagedOverrideToAccessForService:authValue:"
+ "clearLegacyAccessibilityRecordsFromUserDatabase"
+ "decomposeManagedIdentifier:requirementString:"
+ "displayNameForIdentifier:identifierType:"
+ "do_not_forward_to_other_tccd"
+ "drainThrottleInterval"
+ "isServiceThrottled:atTime:"
+ "lastDrainTimeByService"
+ "localizedKeyNameWithOrganizationNameVariant:"
+ "managedAuthValueForAccessRight:"
+ "markRemovedManagedOverridesStale"
+ "mdm_isUserModifiableManagedGrant"
+ "mdm_migratingProfileToManagedSettings"
+ "nil"
+ "notifiedEnableRecordKeys"
+ "notify_register_dispatch for paired-device capabilities failed: %u"
+ "orgName"
+ "peerCapabilitiesNotifyToken"
+ "persistDrainStateToDisk"
+ "postEnableNotificationsForUserModifiableGrants"
+ "postNotificationForService"
+ "postNotificationForService_block_invoke"
+ "reminderDrainStatePlistPath"
+ "reminderDrainThrottle"
+ "reminderMessageTextLocalizationKey"
+ "reminderMessageTextLocalizationKeyNameForServiceName:"
+ "reminderPurposeFormatLocalizationKey"
+ "reminderPurposeFormatLocalizationKeyNameForServiceName:"
+ "reminder_drain_state.plist"
+ "restoreDrainState"
+ "setDrainThrottleInterval:"
+ "setLastDrainTimeByService:"
+ "setMdm_migratingProfileToManagedSettings:"
+ "setNotifiedEnableRecordKeys:"
+ "setOrgName:"
+ "setPeerCapabilitiesNotifyToken:"
+ "setReminderMessageTextLocalizationKey:"
+ "setReminderPurposeFormatLocalizationKey:"
+ "stringWithContentsOfFile:encoding:error:"
+ "syncDegradedManagedOverrideForServiceIdentifier:mainClientIdentifier:clientType:authValue:flags:updateType:"
+ "syncManagedOverrideForServiceIdentifier:mainClientIdentifier:clientType:adminAuthValue:userAuthValue:authReason:authorizationVersion:updateType:degradeWhenUnsupported:"
+ "system_permissions"
+ "v56@0:8@16@24i32q36i44Q48"
+ "v76@0:8@16@24i32q36q44i52Q56Q64B72"
+ "writeToFile:atomically:encoding:error:"
+ "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"
+ "\xf0\xf0\xf0\xf1\xf0c"
- "-[TCCDRequestContext(AsynchronousNotification) presentAsynchronousDenialNotificationWithMessage:buttonTitle:]"
- "-[TCCDRequestContext(AsynchronousNotification) presentAsynchronousDenialNotificationWithMessage:buttonTitle:]_block_invoke"
- "ManagedSettings: marked %{public}@ - %{public}@ as stale (removed from policy)"
- "SELECT   service,   client,   client_type,   auth_value,   auth_reason,   auth_version,   admin_auth_value,   flags,   last_modified FROM managed_overrides WHERE client = ? AND client_type = ? AND NOT (flags & ?)"
- "SELECT auth_value, auth_reason, auth_version, flags FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
- "SELECT client FROM managed_overrides WHERE service = ? AND client_type = ? AND admin_auth_value != 0 AND NOT (flags & ?)"
- "SELECT client FROM managed_overrides WHERE service = ? AND client_type = ? AND admin_auth_value = 0 AND NOT (flags & ?)"
- "SELECT client, client_type, auth_value, auth_reason, auth_version, admin_auth_value, last_modified, flags FROM managed_overrides WHERE service = ? AND NOT (flags & ?) AND auth_value != ?"
- "SELECT service, auth_value, auth_reason, auth_version, admin_auth_value, flags FROM managed_overrides WHERE client = ? AND client_type = ? AND NOT (flags & ?) AND auth_value != ?"
- "SELECT service, client, client_type, auth_value, auth_reason, admin_auth_value, flags, last_modified FROM managed_overrides WHERE 1=1"
- "SELECT service, flags from managed_overrides WHERE client=? AND client_type=? AND csreq=?"
- "setValue:forKey:"
- "\xf0\xf0\xf0\xd1\xf0c"
```
