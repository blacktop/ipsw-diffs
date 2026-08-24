## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-910.0.0.0.0
-  __TEXT.__text: 0x86650
+913.3.3.0.0
+  __TEXT.__text: 0x8cf40
   __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_stubs: 0x9620
-  __TEXT.__objc_methlist: 0x409c
-  __TEXT.__cstring: 0x11c2c
-  __TEXT.__const: 0x638
-  __TEXT.__gcc_except_tab: 0x31a8
-  __TEXT.__objc_methname: 0xf866
-  __TEXT.__oslogstring: 0xe415
+  __TEXT.__lazy_helpers: 0x54
+  __TEXT.__objc_stubs: 0x9a80
+  __TEXT.__objc_methlist: 0x4214
+  __TEXT.__cstring: 0x125da
+  __TEXT.__const: 0x648
+  __TEXT.__gcc_except_tab: 0x34c4
+  __TEXT.__objc_methname: 0xfeca
+  __TEXT.__oslogstring: 0xf026
   __TEXT.__objc_classname: 0x4ae
-  __TEXT.__objc_methtype: 0x149f
-  __TEXT.__unwind_info: 0x1568
-  __DATA_CONST.__const: 0x25f8
-  __DATA_CONST.__cfstring: 0x8260
+  __TEXT.__objc_methtype: 0x14e3
+  __TEXT.__unwind_info: 0x1678
+  __DATA_CONST.__const: 0x2738
+  __DATA_CONST.__cfstring: 0x8480
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_intobj: 0x4f8
-  __DATA_CONST.__objc_arraydata: 0x17e8
+  __DATA_CONST.__objc_intobj: 0x528
+  __DATA_CONST.__objc_arraydata: 0x17d0
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0xf00
   __DATA_CONST.__auth_got: 0xb10
-  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA.__objc_const: 0x7c08
-  __DATA.__objc_selrefs: 0x2be8
-  __DATA.__objc_ivar: 0x640
+  __DATA.__objc_const: 0x7d80
+  __DATA.__objc_selrefs: 0x2d08
+  __DATA.__objc_ivar: 0x65c
   __DATA.__objc_data: 0xf50
-  __DATA.__data: 0x348
+  __DATA.__lazy_load_got: 0x8
+  __DATA.__data: 0x34c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x35c
+  __DATA.__bss: 0x360
   __DATA.__common: 0x30
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2522
-  Symbols:   502
-  CStrings:  5056
+  Functions: 2606
+  Symbols:   504
+  CStrings:  5184
 
Symbols:
+ _OBJC_CLASS_$_DMCComposedIdentifier
+ _OBJC_CLASS_$_LSApplicationProxy
+ __dyld_lazy_load
- _exit
CStrings:
+ "\n\n"
+ " (auth_value preserved; per-system service)"
+ "%@, %@"
+ "%@_WITH_ORG_NAME"
+ "%s: all %lu queued reminder(s) within their drain-throttle window, nothing to drain"
+ "%s: failed to clear pending flag for %{public}s:%{public}s"
+ "%s: failed to create records array"
+ "%s: failed to deserialize drain state plist: %{public}@"
+ "%s: failed to forward disclosure-prompt acknowledgement to system tccd: %{public}s"
+ "%s: failed to select pending enable-notification rows"
+ "%s: failed to serialize drain state plist: %{public}@"
+ "%s: failed to write drain state plist to %{public}@: %{public}@"
+ "%s: merging %zu system tccd records for service=%{public}s client=%{public}s"
+ "%s: no drain state plist found at %{public}@, nothing to restore"
+ "%s: no reply from system tccd for disclosure-prompt acknowledgement"
+ "%s: prompt not shown for %{public}s/%{public}s, re-queuing without arming throttle"
+ "%s: restored drain state for %lu service(s)"
+ "%s: returning %zu pending enable-notification record(s)"
+ "%s: service %{public}s within drain-throttle window, skipping"
+ "%{public}@: %s managed row csreq does not match running process; not prompting"
+ "-[TCCDReminderMonitor persistDrainStateToDisk]"
+ "-[TCCDReminderMonitor restoreDrainState]"
+ "@\"NSObject<OS_dispatch_queue>\"16@0:8"
+ "A!"
+ "All"
+ "B32@0:8@16d24"
+ "CFBundleDisplayName"
+ "CFBundleName"
+ "DELETE FROM managed_overrides WHERE client = ? AND client_type = ?"
+ "DELETE FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
+ "Failed to construct localized enabled-notification string for service %{public}@ and subject %{public}@"
+ "Failed to delete managed_overrides for client %{public}@ type %d (%d)"
+ "Failed to mark managed_overrides row stale: serviceName=%{public}@, identifier=%{public}@"
+ "Failed to obtain localized button title for enabled-notification for service %{public}@"
+ "Failed to upsert managed_overrides row for MDM policy: serviceName=%{public}@, identifier=%{public}@, identifier_type=%lld"
+ "INSERT INTO managed_overrides (service, client, client_type, admin_auth_value, auth_reason, auth_version,  auth_value, csreq, policy_id, indirect_object_identifier_type, indirect_object_identifier,  indirect_object_code_identity, flags) VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, 'UNUSED', NULL, ?)"
+ "Managed override csreq does not match requesting process: service=%{public}@, client=%{public}@; not honoring managed authorization"
+ "ManagedSettings: %{public}@ is not eligible for managed_overrides; skipping %{public}@:%{public}@"
+ "ManagedSettings: could not build csreq from requirement for %{public}@; storing without code-requirement binding"
+ "ManagedSettings: deleted %{public}@ - %{public}@ (admin pushed None, prompt not presented)"
+ "ManagedSettings: failed to delete None record %{public}@:%{public}@: %d"
+ "ManagedSettings: ignoring None for %{public}@:%{public}@ - disclosure already presented, record preserved"
+ "ManagedSettings: inserted managed_overrides for %{public}@:%{public}@ admin_auth_value=%lld auth_value=%lld (result=%d)"
+ "ManagedSettings: managedTCC feature disabled — NOT writing managed_overrides for %{public}@:%{public}@ (admin_auth_value=%lld). MDM grant will not take effect via managed path."
+ "ManagedSettings: marked %{public}@ - %{public}@ as stale (removed from policy)%{public}s"
+ "ManagedSettings: pruned ineligible managed_overrides rows for %{public}@ (result=%d)"
+ "ManagedSettings: updated managed_overrides for %{public}@:%{public}@ admin_auth_value=%lld (result=%d)"
+ "ManagedSettings: upsert managed_overrides from MDM policy for %{public}@:%{public}@ admin_auth_value=%lld"
+ "Override: Organization name is set to %@"
+ "Override: enable notification failed to post for %{public}@:%{public}@; leaving pending flag set for retry"
+ "Override: failed to acknowledge enable notification for %{public}@:%{public}@; will retry"
+ "Override: failed to fetch pending enable notifications from system tccd"
+ "Override: pruned ineligible managed_overrides rows for %{public}@ (result=%d)"
+ "Override: routing %{public}@ for %{public}@ to managed_overrides (admin_auth_value=%lld)"
+ "PayloadOrganization"
+ "REMINDER_ACCESS_INFO"
+ "REMINDER_ACCESS_PURPOSE"
+ "SELECT   service,   client,   client_type,   auth_value,   auth_reason,   auth_version,   admin_auth_value,   flags,   last_modified FROM managed_overrides WHERE client = ? AND client_type = ? AND (NOT (flags & ?) OR auth_value = ?)"
+ "SELECT DISTINCT service FROM managed_overrides"
+ "SELECT auth_value, auth_reason, auth_version, flags, csreq FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
+ "SELECT client FROM managed_overrides WHERE service = ? AND client_type = ? AND admin_auth_value != 0 AND auth_value != ?"
+ "SELECT client FROM managed_overrides WHERE service = ? AND client_type = ? AND admin_auth_value = 0 AND auth_value != ?"
+ "SELECT client, client_type, auth_value, auth_reason, auth_version, admin_auth_value, last_modified, flags FROM managed_overrides WHERE service = ? AND auth_value != ?"
+ "SELECT service, auth_value, auth_reason, auth_version, admin_auth_value, flags FROM managed_overrides WHERE client = ? AND client_type = ? AND auth_value != ?"
+ "SELECT service, client, client_type FROM managed_overrides WHERE (flags & ?)"
+ "SELECT service, client, client_type FROM managed_overrides WHERE (flags & ?) AND NOT (flags & ?)"
+ "SELECT service, client, client_type, auth_value, auth_reason, admin_auth_value, flags, last_modified, csreq FROM managed_overrides WHERE 1=1"
+ "SELECT service, flags, csreq from managed_overrides WHERE client=? AND client_type=?"
+ "T@\"NSData\",R,V_designatedRequirementData"
+ "T@\"NSMutableDictionary\",&,N,V_lastDrainTimeByService"
+ "T@\"NSString\",&,N,V_orgName"
+ "T@\"NSString\",&,N,V_reminderMessageTextLocalizationKey"
+ "T@\"NSString\",&,N,V_reminderPurposeFormatLocalizationKey"
+ "TB,N,V_mdm_eligibleForManagedOverrides"
+ "TB,N,V_mdm_migratingProfileToManagedSettings"
+ "TCCAccessAcknowledgeEnableNotifications"
+ "TCCAccessGetPendingEnableNotifications"
+ "Td,N,V_drainThrottleInterval"
+ "UPDATE managed_overrides SET   admin_auth_value = ?,   auth_value = CASE WHEN auth_reason IN (?, ?) THEN auth_value ELSE ? END,   auth_reason = ?,   flags = ((flags | ?) & ~?),   last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET   auth_value = ?,   flags = (flags | ?),   last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET admin_auth_value = ?, auth_reason = ?, csreq = ?, flags = (flags & ~?), last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET auth_value = ?, auth_reason = ?, flags = (flags | ?), last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET flags = (flags & ~?) WHERE service = ? AND client = ? AND client_type = ?"
+ "UPDATE managed_overrides SET flags = (flags | ?), last_modified = CAST(strftime('%s','now') AS INTEGER) WHERE service = ? AND client = ? AND client_type = ?"
+ "_drainThrottleInterval"
+ "_lastDrainTimeByService"
+ "_mdm_eligibleForManagedOverrides"
+ "_mdm_migratingProfileToManagedSettings"
+ "_orgName"
+ "_pruneIneligibleManagedOverrides"
+ "_reminderMessageTextLocalizationKey"
+ "_reminderPurposeFormatLocalizationKey"
+ "acknowledgeEnableNotificationForService:client:clientType:"
+ "applicationProxyForIdentifier:"
+ "com.apple.tcc.access-enabled-notification-pending"
+ "csreq"
+ "decomposeManagedIdentifier:requirementString:"
+ "designatedRequirement"
+ "displayNameForIdentifier:identifierType:"
+ "drainThrottleInterval"
+ "handle_TCCAccessAcknowledgeEnableNotifications"
+ "handle_TCCAccessAcknowledgeEnableNotifications_block_invoke"
+ "handle_TCCAccessGetPendingEnableNotifications"
+ "isServiceThrottled:atTime:"
+ "lastDrainTimeByService"
+ "localizedKeyNameWithOrganizationNameVariant:"
+ "markRemovedManagedOverridesStale"
+ "mdm_eligibleForManagedOverrides"
+ "mdm_isUserModifiableManagedGrant"
+ "mdm_migratingProfileToManagedSettings"
+ "newComposedIdentifier:"
+ "nil"
+ "orgName"
+ "persistDrainStateToDisk"
+ "postEnableNotificationsForUserModifiableGrants"
+ "postNotificationForService"
+ "postNotificationForService_block_invoke"
+ "pppc_eligibleForManagedOverrides"
+ "pruneIneligibleManagedOverrides"
+ "records"
+ "reminderDrainStatePlistPath"
+ "reminderDrainThrottle"
+ "reminderMessageTextLocalizationKey"
+ "reminderMessageTextLocalizationKeyNameForServiceName:"
+ "reminderPurposeFormatLocalizationKey"
+ "reminderPurposeFormatLocalizationKeyNameForServiceName:"
+ "reminder_drain_state.plist"
+ "requirement"
+ "restoreDrainState"
+ "setDrainThrottleInterval:"
+ "setLastDrainTimeByService:"
+ "setMdm_eligibleForManagedOverrides:"
+ "setMdm_migratingProfileToManagedSettings:"
+ "setOrgName:"
+ "setReminderMessageTextLocalizationKey:"
+ "setReminderPurposeFormatLocalizationKey:"
+ "stringByDeletingPathExtension"
+ "teamID"
+ "unknown"
+ "v12@?0B8"
+ "v36@0:8@16@24i32"
+ "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"
+ "\xf0\xf0\xf0\xf1\xf0c"
- " AND auth_value != ? AND auth_value != ?"
- "%s: merging %zu system tccd records (auth_value != unknown) for service=%{public}s client=%{public}s"
- "-[TCCDRequestContext(AsynchronousNotification) presentAsynchronousDenialNotificationWithMessage:buttonTitle:]"
- "-[TCCDRequestContext(AsynchronousNotification) presentAsynchronousDenialNotificationWithMessage:buttonTitle:]_block_invoke"
- "ManagedSettings: marked %{public}@ - %{public}@ as stale (removed from policy)"
- "SELECT   service,   client,   client_type,   auth_value,   auth_reason,   auth_version,   admin_auth_value,   flags,   last_modified FROM managed_overrides WHERE client = ? AND client_type = ? AND NOT (flags & ?)"
- "SELECT client FROM managed_overrides WHERE service = ? AND client_type = ? AND admin_auth_value != 0 AND NOT (flags & ?)"
- "SELECT client FROM managed_overrides WHERE service = ? AND client_type = ? AND admin_auth_value = 0 AND NOT (flags & ?)"
- "SELECT client, client_type, auth_value, auth_reason, auth_version, admin_auth_value, last_modified, flags FROM managed_overrides WHERE service = ? AND NOT (flags & ?) AND auth_value != ?"
- "SELECT service, auth_value, auth_reason, auth_version, admin_auth_value, flags FROM managed_overrides WHERE client = ? AND client_type = ? AND NOT (flags & ?) AND auth_value != ?"
- "SELECT service, client, client_type, auth_value, auth_reason, admin_auth_value, flags, last_modified FROM managed_overrides WHERE 1=1"
- "SELECT service, flags from managed_overrides WHERE client=? AND client_type=? AND csreq=?"
- "T@\"NSData\",&,V_designatedRequirementData"
- "setDesignatedRequirementData:"
- "\xf0\xf0\xf0\xd1\xf0c"
```
