## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-913.3.3.0.0
-  __TEXT.__text: 0x8b774
+918.0.0.0.0
+  __TEXT.__text: 0x8bda8
   __TEXT.__auth_stubs: 0x1600
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x9a80
-  __TEXT.__objc_methlist: 0x4214
-  __TEXT.__cstring: 0x125da
+  __TEXT.__objc_stubs: 0x9c60
+  __TEXT.__objc_methlist: 0x42d4
+  __TEXT.__cstring: 0x12641
   __TEXT.__const: 0x648
-  __TEXT.__gcc_except_tab: 0x34c4
-  __TEXT.__objc_methname: 0xfeca
-  __TEXT.__oslogstring: 0xf026
+  __TEXT.__gcc_except_tab: 0x3528
+  __TEXT.__objc_methname: 0x10273
+  __TEXT.__oslogstring: 0xf070
   __TEXT.__objc_classname: 0x4ae
-  __TEXT.__objc_methtype: 0x14e3
-  __TEXT.__unwind_info: 0x2000
-  __DATA_CONST.__const: 0x2738
-  __DATA_CONST.__cfstring: 0x8480
+  __TEXT.__objc_methtype: 0x14f3
+  __TEXT.__unwind_info: 0x2040
+  __DATA_CONST.__const: 0x2758
+  __DATA_CONST.__cfstring: 0x8500
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_intobj: 0x528
-  __DATA_CONST.__objc_arraydata: 0x17d0
-  __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA_CONST.__objc_dictobj: 0xf00
+  __DATA_CONST.__objc_intobj: 0x540
+  __DATA_CONST.__objc_arraydata: 0x17f0
+  __DATA_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_dictobj: 0xf78
   __DATA_CONST.__auth_got: 0xb10
   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA.__objc_const: 0x7d80
-  __DATA.__objc_selrefs: 0x2d08
-  __DATA.__objc_ivar: 0x65c
+  __DATA.__objc_const: 0x7f78
+  __DATA.__objc_selrefs: 0x2d80
+  __DATA.__objc_ivar: 0x688
   __DATA.__objc_data: 0xf50
   __DATA.__lazy_load_got: 0x8
   __DATA.__data: 0x34c

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2604
+  Functions: 2628
   Symbols:   504
-  CStrings:  5184
+  CStrings:  5222
 
Symbols:
+ _time
- _os_eligibility_get_domain_answer
CStrings:
+ "#AuthorizationPromptServiceClient TCCDUserTrackingTransparencyMonitor 1-year reprompt triggered for service:%@ client: %@ last_modified:%ld"
+ "#AuthorizationPromptServiceClient TCCDUserTrackingTransparencyMonitor is %@ to reprompt to happen for service:%@ client: %@ serviceCooldown:%f"
+ "#ManagedTCCDefaults could not resolve a bundle identifier for the requesting process; not prompting"
+ "#ManagedTCCDefaults unable to build an access identity for the requesting process; managed rows bound to a csreq will not prompt"
+ "%@|%@"
+ "%s: service %{public}@ has no usageDescriptionKeyName; cannot resolve reminder purpose"
+ "-[TCCDReminderMonitor reminderPurposeForService:client:context:]"
+ "@\"NSMutableSet\""
+ "@\"NSString\"16@?0@\"TCCDRequestContext\"8"
+ "CREATE TABLE IF NOT EXISTS admin (key TEXT PRIMARY KEY NOT NULL, value INTEGER NOT NULL);INSERT OR IGNORE INTO admin VALUES ('version', 37);CREATE TABLE IF NOT EXISTS policies (    id        INTEGER    NOT NULL PRIMARY KEY,     bundle_id    TEXT    NOT NULL,     uuid        TEXT    NOT NULL,     display        TEXT    NOT NULL,     UNIQUE (bundle_id, uuid));CREATE TABLE IF NOT EXISTS active_policy (    client        TEXT    NOT NULL,     client_type    INTEGER    NOT NULL,     policy_id    INTEGER NOT NULL,     PRIMARY KEY (client, client_type),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE INDEX IF NOT EXISTS active_policy_id ON active_policy(policy_id);CREATE TABLE IF NOT EXISTS access (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     pid            INTEGER,     pid_version    INTEGER,     boot_uuid      TEXT NOT NULL DEFAULT 'UNUSED',     last_reminded  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     one_time_reprompt_eligible INTEGER,     reminder_count INTEGER NOT NULL DEFAULT 0,     PRIMARY KEY (service, client, client_type, indirect_object_identifier),    FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE TABLE IF NOT EXISTS access_overrides (    service        TEXT    NOT NULL PRIMARY KEY);CREATE TABLE IF NOT EXISTS expired (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     csreq          BLOB,     last_modified  INTEGER     NOT NULL ,     expired_at     INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     PRIMARY KEY (service, client, client_type));CREATE TABLE IF NOT EXISTS integrity_flag (    key TEXT PRIMARY KEY NOT NULL,    value INTEGER NOT NULL);INSERT OR IGNORE INTO integrity_flag VALUES ('integrity_flag', 0);CREATE TABLE IF NOT EXISTS managed_overrides (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL DEFAULT 1,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER     NOT NULL DEFAULT 0,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     one_time_reprompt_eligible INTEGER,     admin_auth_value    INTEGER NOT NULL,    PRIMARY KEY (service, client, client_type, indirect_object_identifier),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);"
+ "ManagedSettings: existing access auth (%lld) differs from admin (%lld) for %{public}@:%{public}@, migrating with user's existing auth and pending disclosure"
+ "ManagedSettings: skipping %{public}@:%{public}@ - admin value %{public}@ resolved to None and there is no existing record"
+ "Override: enable notification already being posted for %{public}@:%{public}@; skipping duplicate post"
+ "SELECT auth_value, one_time_reprompt_eligible, last_modified FROM access WHERE client = ? AND service = ?"
+ "TB,N,V_doesNotSupportCache"
+ "TB,R,V_isEligibleForATTReprompt"
+ "TB,R,V_isEligibleForFullSheetATTAllowed"
+ "TB,R,V_isEligibleForFullSheetATTRequired"
+ "TB,R,V_isEligibleForMotionSensorDataRegulation"
+ "TCCD_MSG_MESSAGE_ELIGIBLE_FOR_REPROMPT"
+ "Ti,N,V_eligibleForReprompt"
+ "Ti,N,V_reprompted"
+ "Ti,N,V_requestIsForOneTimeReprompt"
+ "UPDATE admin SET value = 37 WHERE key = 'version'"
+ "_doesNotSupportCache"
+ "_eligibleForReprompt"
+ "_inFlightEnableNotificationKeys"
+ "_inFlightEnableNotificationLock"
+ "_isEligibleForATTReprompt"
+ "_isEligibleForFullSheetATTAllowed"
+ "_isEligibleForFullSheetATTRequired"
+ "_isEligibleForMotionSensorDataRegulation"
+ "_reprompted"
+ "_requestIsForOneTimeReprompt"
+ "claimInFlightEnableNotificationKey:"
+ "com.apple.TCC.managed_overrides_audit"
+ "doesNotSupportCache"
+ "eligible"
+ "eligibleForReprompt"
+ "getUsageDescriptionKeyForAuthorization:"
+ "isEligibleForATTReprompt"
+ "isEligibleForFullSheetATTAllowed"
+ "isEligibleForFullSheetATTRequired"
+ "isEligibleForMotionSensorDataRegulation"
+ "kTCCServiceAccessoryWorker"
+ "kTCCServiceAccessoryWorkerGPU"
+ "kTCCServiceMotionSensors"
+ "not eligible"
+ "releaseInFlightEnableNotificationKey:"
+ "reminderPurposeForService:client:context:"
+ "removeObject:"
+ "reprompted"
+ "requestIsForOneTimeReprompt"
+ "setDoesNotSupportCache:"
+ "setEligibleForReprompt:"
+ "setReprompted:"
+ "setRequestIsForOneTimeReprompt:"
- "#AuthorizationPromptServiceClient TCCDUserTrackingTransparencyMonitor allowing reprompt to happen? canPrompt: %@ for service:%@ client: %@ calledWithNewAPI: %d serviceCooldown:%f"
- "#AuthorizationPromptServiceClient TCCDUserTrackingTransparencyMonitor eligibleToShowPrompt for service:%@ client: %@ authVal:%d one_time_reprompt_eligible:%d calledWithNewAPI: %d"
- "%s #AuthorizationPromptServiceClient %@ for service %@ is %@ eligible for the full sheet prompt"
- "%s #AuthorizationPromptServiceClient %@ for service %@ is not eligible to show a ATT - FF is not enabled"
- "%s #AuthorizationPromptServiceClient %@ for service %@ is not eligible to show a fullsheet prompt - FF is not enabled"
- "%s os eligibility status: %llu: called for %@ for service %@ #AuthorizationPromptServiceClient"
- "-[TCCDRequestContext(SynchronousPrompt) serviceIsEligibleToPromptForFullSheet:]"
- "@\"NSString\"32@?0@\"TCCDService\"8Q16@\"TCCDAccessIdentity\"24"
- "A"
- "CREATE TABLE IF NOT EXISTS admin (key TEXT PRIMARY KEY NOT NULL, value INTEGER NOT NULL);INSERT OR IGNORE INTO admin VALUES ('version', 36);CREATE TABLE IF NOT EXISTS policies (    id        INTEGER    NOT NULL PRIMARY KEY,     bundle_id    TEXT    NOT NULL,     uuid        TEXT    NOT NULL,     display        TEXT    NOT NULL,     UNIQUE (bundle_id, uuid));CREATE TABLE IF NOT EXISTS active_policy (    client        TEXT    NOT NULL,     client_type    INTEGER    NOT NULL,     policy_id    INTEGER NOT NULL,     PRIMARY KEY (client, client_type),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE INDEX IF NOT EXISTS active_policy_id ON active_policy(policy_id);CREATE TABLE IF NOT EXISTS access (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     pid            INTEGER,     pid_version    INTEGER,     boot_uuid      TEXT NOT NULL DEFAULT 'UNUSED',     last_reminded  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     one_time_reprompt_eligible INTEGER,     reminder_count INTEGER NOT NULL DEFAULT 0,     PRIMARY KEY (service, client, client_type, indirect_object_identifier),    FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE TABLE IF NOT EXISTS access_overrides (    service        TEXT    NOT NULL PRIMARY KEY);CREATE TABLE IF NOT EXISTS expired (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     csreq          BLOB,     last_modified  INTEGER     NOT NULL ,     expired_at     INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     PRIMARY KEY (service, client, client_type));CREATE TABLE IF NOT EXISTS integrity_flag (    key TEXT PRIMARY KEY NOT NULL,    value INTEGER NOT NULL);INSERT OR IGNORE INTO integrity_flag VALUES ('integrity_flag', 0);CREATE TABLE IF NOT EXISTS managed_overrides (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL DEFAULT 1,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER     NOT NULL DEFAULT 0,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     one_time_reprompt_eligible INTEGER,     admin_auth_value    INTEGER NOT NULL,    PRIMARY KEY (service, client, client_type, indirect_object_identifier),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);"
- "ManagedSettings: existing access auth (%lld) differs from admin (%lld) for %{public}@:%{public}@, migrating with user's existing auth"
- "SELECT auth_value, one_time_reprompt_eligible FROM access WHERE client = ? AND service = ?"
- "UPDATE admin SET value = 36 WHERE key = 'version'"
- "com.apple.TCC.managed_defaults_audit"
- "fullPromptSheet"
- "getUsageDescriptionKeyForAuthorization:forClient:"
- "is"
- "is not"
- "serviceIsEligibleToPromptForFullSheet:"
```
