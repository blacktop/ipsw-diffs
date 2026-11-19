## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__info_plist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-913.3.3.0.0
-  __TEXT.__text: 0x8b774
+921.0.1.0.0
+  __TEXT.__text: 0x8cb1c
   __TEXT.__auth_stubs: 0x1600
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x9a80
-  __TEXT.__objc_methlist: 0x4214
-  __TEXT.__cstring: 0x125da
+  __TEXT.__objc_stubs: 0x9e00
+  __TEXT.__objc_methlist: 0x43d4
+  __TEXT.__cstring: 0x1281d
   __TEXT.__const: 0x648
-  __TEXT.__gcc_except_tab: 0x34c4
-  __TEXT.__objc_methname: 0xfeca
-  __TEXT.__oslogstring: 0xf026
+  __TEXT.__gcc_except_tab: 0x35a4
+  __TEXT.__objc_methname: 0x107e4
+  __TEXT.__oslogstring: 0xf19d
   __TEXT.__objc_classname: 0x4ae
-  __TEXT.__objc_methtype: 0x14e3
+  __TEXT.__objc_methtype: 0x14f3
   __TEXT.__info_plist: 0x3af
-  __TEXT.__unwind_info: 0x2000
-  __DATA_CONST.__const: 0x2738
-  __DATA_CONST.__cfstring: 0x8480
+  __TEXT.__unwind_info: 0x2070
+  __DATA_CONST.__const: 0x2760
+  __DATA_CONST.__cfstring: 0x8660
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_intobj: 0x528
-  __DATA_CONST.__objc_arraydata: 0x17d0
+  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__objc_arraydata: 0x17f8
   __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA_CONST.__objc_dictobj: 0xf00
+  __DATA_CONST.__objc_intobj: 0x540
+  __DATA_CONST.__objc_dictobj: 0xf78
   __DATA_CONST.__auth_got: 0xb10
-  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA.__objc_const: 0x7d80
-  __DATA.__objc_selrefs: 0x2d08
-  __DATA.__objc_ivar: 0x65c
+  __DATA.__objc_const: 0x80f8
+  __DATA.__objc_selrefs: 0x2e30
+  __DATA.__objc_ivar: 0x6a8
   __DATA.__objc_data: 0xf50
   __DATA.__lazy_load_got: 0x8
   __DATA.__data: 0x34c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x360
+  __DATA.__bss: 0x368
   __DATA.__common: 0x30
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2604
-  Symbols:   504
-  CStrings:  5184
+  Functions: 2656
+  Symbols:   505
+  CStrings:  5277
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _time
- _os_eligibility_get_domain_answer
CStrings:
+ "#AuthorizationPromptServiceClient TCCDUserTrackingTransparencyMonitor 1-year reprompt triggered for service:%@ client: %@ last_modified:%ld"
+ "#AuthorizationPromptServiceClient TCCDUserTrackingTransparencyMonitor is %@ to reprompt to happen for service:%@ client: %@ serviceCooldown:%f"
+ "#ManagedTCCDefaults could not resolve a bundle identifier for the requesting process; not prompting"
+ "#ManagedTCCDefaults unable to build an access identity for the requesting process; managed rows bound to a csreq will not prompt"
+ "%@|%@"
+ "%s: %{public}@ does not support reminder prompts, ignoring report-use"
+ "%s: automaticTimeOverride=ForceDisabled, not surfacing reminder prompt"
+ "%s: last drain for %{public}@ is %.0fs in the future, ignoring the throttle"
+ "%s: missing client or service, refusing to enqueue"
+ "%s: service %{public}@ has no usageDescriptionKeyName; cannot resolve reminder purpose"
+ "+[TCCDReminderMonitor milestoneOverrideFromDefaultsForKey:]"
+ "-[TCCDReminderMonitor enqueueReminderWithContext:deferrals:]"
+ "-[TCCDReminderMonitor isServiceThrottled:atTime:]"
+ "-[TCCDReminderMonitor reminderPurposeForService:client:context:]"
+ "-[TCCDReminderMonitor showReminderPrompt:result:accessCount:]"
+ "@\"NSMutableSet\""
+ "@\"NSString\"16@?0@\"TCCDRequestContext\"8"
+ "A2"
+ "AUTHREQ_CTX: msgID=%{public}@, function=%@, service=%@, query=%llu, client_dict=%@, daemon_dict=%@, attributed_bundle_id=%{public}@"
+ "CREATE TABLE IF NOT EXISTS admin (key TEXT PRIMARY KEY NOT NULL, value INTEGER NOT NULL);INSERT OR IGNORE INTO admin VALUES ('version', 37);CREATE TABLE IF NOT EXISTS policies (    id        INTEGER    NOT NULL PRIMARY KEY,     bundle_id    TEXT    NOT NULL,     uuid        TEXT    NOT NULL,     display        TEXT    NOT NULL,     UNIQUE (bundle_id, uuid));CREATE TABLE IF NOT EXISTS active_policy (    client        TEXT    NOT NULL,     client_type    INTEGER    NOT NULL,     policy_id    INTEGER NOT NULL,     PRIMARY KEY (client, client_type),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE INDEX IF NOT EXISTS active_policy_id ON active_policy(policy_id);CREATE TABLE IF NOT EXISTS access (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     pid            INTEGER,     pid_version    INTEGER,     boot_uuid      TEXT NOT NULL DEFAULT 'UNUSED',     last_reminded  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     one_time_reprompt_eligible INTEGER,     reminder_count INTEGER NOT NULL DEFAULT 0,     PRIMARY KEY (service, client, client_type, indirect_object_identifier),    FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE TABLE IF NOT EXISTS access_overrides (    service        TEXT    NOT NULL PRIMARY KEY);CREATE TABLE IF NOT EXISTS expired (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     csreq          BLOB,     last_modified  INTEGER     NOT NULL ,     expired_at     INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     PRIMARY KEY (service, client, client_type));CREATE TABLE IF NOT EXISTS integrity_flag (    key TEXT PRIMARY KEY NOT NULL,    value INTEGER NOT NULL);INSERT OR IGNORE INTO integrity_flag VALUES ('integrity_flag', 0);CREATE TABLE IF NOT EXISTS managed_overrides (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL DEFAULT 1,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER     NOT NULL DEFAULT 0,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     one_time_reprompt_eligible INTEGER,     admin_auth_value    INTEGER NOT NULL,    PRIMARY KEY (service, client, client_type, indirect_object_identifier),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);"
+ "Invalid attributed bundle identifier: %@"
+ "ManagedSettings: existing access auth (%lld) differs from admin (%lld) for %{public}@:%{public}@, migrating with user's existing auth and pending disclosure"
+ "ManagedSettings: skipping %{public}@:%{public}@ - admin value %{public}@ resolved to None and there is no existing record"
+ "Override: enable notification already being posted for %{public}@:%{public}@; skipping duplicate post"
+ "REMINDER_ACCESS_INFO_COUNT"
+ "REMINDER_ACCESS_INFO_COUNT_ONE"
+ "SELECT auth_value, one_time_reprompt_eligible, last_modified FROM access WHERE client = ? AND service = ?"
+ "T@\"NSArray\",C,N,V_researchMilestoneOverride"
+ "T@\"NSString\",&,N,V_reminderAccessCountFormatLocalizationKey"
+ "T@\"NSString\",&,N,V_reminderAccessCountSingularLocalizationKey"
+ "T@\"NSString\",C,N,V_attributedBundleIdentifier"
+ "T@\"NSString\",C,N,V_attributedDisplayName"
+ "T@\"NSString\",C,N,V_reminderDisplayBundleIdentifier"
+ "TB,N,V_doesNotSupportCache"
+ "TB,N,V_supportsAttributedReportUse"
+ "TB,R,V_isEligibleForATTReprompt"
+ "TB,R,V_isEligibleForFullSheetATTAllowed"
+ "TB,R,V_isEligibleForFullSheetATTRequired"
+ "TB,R,V_isEligibleForMotionSensorDataRegulation"
+ "TCCD_MSG_MESSAGE_ELIGIBLE_FOR_REPROMPT"
+ "TCCD_MSG_MESSAGE_OPTION_ATTRIBUTED_BUNDLE_IDENTIFIER_KEY"
+ "Ti,N,V_eligibleForReprompt"
+ "Ti,N,V_reprompted"
+ "Ti,N,V_requestIsForOneTimeReprompt"
+ "Tq,V_automaticTimeOverride"
+ "UPDATE admin SET value = 37 WHERE key = 'version'"
+ "_attributedBundleIdentifier"
+ "_attributedDisplayName"
+ "_automaticTimeOverride"
+ "_doesNotSupportCache"
+ "_eligibleForReprompt"
+ "_inFlightEnableNotificationKeys"
+ "_inFlightEnableNotificationLock"
+ "_isEligibleForATTReprompt"
+ "_isEligibleForFullSheetATTAllowed"
+ "_isEligibleForFullSheetATTRequired"
+ "_isEligibleForMotionSensorDataRegulation"
+ "_reminderAccessCountFormatLocalizationKey"
+ "_reminderAccessCountSingularLocalizationKey"
+ "_reminderDisplayBundleIdentifier"
+ "_reprompted"
+ "_requestIsForOneTimeReprompt"
+ "_researchMilestoneOverride"
+ "_supportsAttributedReportUse"
+ "attributedBundleIdentifier"
+ "attributedDisplayName"
+ "automaticTimeOverride"
+ "characterAtIndex:"
+ "claimInFlightEnableNotificationKey:"
+ "com.apple.TCC.managed_overrides_audit"
+ "com.apple.developer.healthkit.research"
+ "deferrals"
+ "display_client"
+ "doesNotSupportCache"
+ "eligible"
+ "eligibleForReprompt"
+ "enqueueReminderWithContext:deferrals:"
+ "getUsageDescriptionKeyForAuthorization:"
+ "healthResearchReminderMilestoneOverride"
+ "identifier exceeds maximum length of %lu"
+ "identifier must be printable ASCII"
+ "identifier must be valid UTF-8"
+ "identifier must not be empty"
+ "isEligibleForATTReprompt"
+ "isEligibleForFullSheetATTAllowed"
+ "isEligibleForFullSheetATTRequired"
+ "isEligibleForMotionSensorDataRegulation"
+ "kTCCServiceAccessoryWorker"
+ "kTCCServiceAccessoryWorkerGPU"
+ "kTCCServiceMotionSensors"
+ "milestoneOverrideFromDefaultsForKey:"
+ "not eligible"
+ "releaseInFlightEnableNotificationKey:"
+ "reminderAccessCountFormatLocalizationKey"
+ "reminderAccessCountFormatLocalizationKeyNameForServiceName:"
+ "reminderAccessCountSingularLocalizationKey"
+ "reminderAccessCountSingularLocalizationKeyNameForServiceName:"
+ "reminderDisplayBundleIdentifier"
+ "reminderInfoTextForService:accessCount:"
+ "reminderPurposeForService:client:context:"
+ "removeObject:"
+ "reprompted"
+ "requestIsForOneTimeReprompt"
+ "researchMilestoneOverride"
+ "setAttributedBundleIdentifier:"
+ "setAttributedDisplayName:"
+ "setAutomaticTimeOverride:"
+ "setDoesNotSupportCache:"
+ "setEligibleForReprompt:"
+ "setReminderAccessCountFormatLocalizationKey:"
+ "setReminderAccessCountSingularLocalizationKey:"
+ "setReminderDisplayBundleIdentifier:"
+ "setReprompted:"
+ "setRequestIsForOneTimeReprompt:"
+ "setResearchMilestoneOverride:"
+ "setSupportsAttributedReportUse:"
+ "showReminderPrompt:result:accessCount:"
+ "supportsAttributedReportUse"
+ "\xf0\xf0\xf0\xf01\xf0c"
- "#AuthorizationPromptServiceClient TCCDUserTrackingTransparencyMonitor allowing reprompt to happen? canPrompt: %@ for service:%@ client: %@ calledWithNewAPI: %d serviceCooldown:%f"
- "#AuthorizationPromptServiceClient TCCDUserTrackingTransparencyMonitor eligibleToShowPrompt for service:%@ client: %@ authVal:%d one_time_reprompt_eligible:%d calledWithNewAPI: %d"
- "%s #AuthorizationPromptServiceClient %@ for service %@ is %@ eligible for the full sheet prompt"
- "%s #AuthorizationPromptServiceClient %@ for service %@ is not eligible to show a ATT - FF is not enabled"
- "%s #AuthorizationPromptServiceClient %@ for service %@ is not eligible to show a fullsheet prompt - FF is not enabled"
- "%s os eligibility status: %llu: called for %@ for service %@ #AuthorizationPromptServiceClient"
- "+[TCCDReminderMonitor milestoneOverrideFromDefaults]"
- "-[TCCDReminderMonitor enqueueReminderWithContext:]"
- "-[TCCDReminderMonitor showReminderPrompt:result:]"
- "-[TCCDRequestContext(SynchronousPrompt) serviceIsEligibleToPromptForFullSheet:]"
- "@\"NSString\"32@?0@\"TCCDService\"8Q16@\"TCCDAccessIdentity\"24"
- "A"
- "A!"
- "AUTHREQ_CTX: msgID=%{public}@, function=%@, service=%@, query=%llu, client_dict=%@, daemon_dict=%@"
- "CREATE TABLE IF NOT EXISTS admin (key TEXT PRIMARY KEY NOT NULL, value INTEGER NOT NULL);INSERT OR IGNORE INTO admin VALUES ('version', 36);CREATE TABLE IF NOT EXISTS policies (    id        INTEGER    NOT NULL PRIMARY KEY,     bundle_id    TEXT    NOT NULL,     uuid        TEXT    NOT NULL,     display        TEXT    NOT NULL,     UNIQUE (bundle_id, uuid));CREATE TABLE IF NOT EXISTS active_policy (    client        TEXT    NOT NULL,     client_type    INTEGER    NOT NULL,     policy_id    INTEGER NOT NULL,     PRIMARY KEY (client, client_type),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE INDEX IF NOT EXISTS active_policy_id ON active_policy(policy_id);CREATE TABLE IF NOT EXISTS access (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     pid            INTEGER,     pid_version    INTEGER,     boot_uuid      TEXT NOT NULL DEFAULT 'UNUSED',     last_reminded  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     one_time_reprompt_eligible INTEGER,     reminder_count INTEGER NOT NULL DEFAULT 0,     PRIMARY KEY (service, client, client_type, indirect_object_identifier),    FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE TABLE IF NOT EXISTS access_overrides (    service        TEXT    NOT NULL PRIMARY KEY);CREATE TABLE IF NOT EXISTS expired (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     csreq          BLOB,     last_modified  INTEGER     NOT NULL ,     expired_at     INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     PRIMARY KEY (service, client, client_type));CREATE TABLE IF NOT EXISTS integrity_flag (    key TEXT PRIMARY KEY NOT NULL,    value INTEGER NOT NULL);INSERT OR IGNORE INTO integrity_flag VALUES ('integrity_flag', 0);CREATE TABLE IF NOT EXISTS managed_overrides (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL DEFAULT 1,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER     NOT NULL DEFAULT 0,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     one_time_reprompt_eligible INTEGER,     admin_auth_value    INTEGER NOT NULL,    PRIMARY KEY (service, client, client_type, indirect_object_identifier),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);"
- "ManagedSettings: existing access auth (%lld) differs from admin (%lld) for %{public}@:%{public}@, migrating with user's existing auth"
- "SELECT auth_value, one_time_reprompt_eligible FROM access WHERE client = ? AND service = ?"
- "UPDATE admin SET value = 36 WHERE key = 'version'"
- "com.apple.TCC.managed_defaults_audit"
- "fullPromptSheet"
- "getUsageDescriptionKeyForAuthorization:forClient:"
- "is"
- "is not"
- "milestoneOverrideFromDefaults"
- "serviceIsEligibleToPromptForFullSheet:"
- "\xf0\xf0\xf0\xf1\xf0c"
```
