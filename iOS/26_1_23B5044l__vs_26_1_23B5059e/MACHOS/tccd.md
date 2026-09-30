## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-857.0.7.0.0
-  __TEXT.__text: 0x63ce4
+858.0.1.0.0
+  __TEXT.__text: 0x64328
   __TEXT.__auth_stubs: 0x1500
   __TEXT.__objc_stubs: 0x9120
   __TEXT.__objc_methlist: 0x442c
-  __TEXT.__cstring: 0xc130
+  __TEXT.__cstring: 0xc2fa
   __TEXT.__const: 0x6c8
-  __TEXT.__gcc_except_tab: 0x1acc
+  __TEXT.__gcc_except_tab: 0x1b0c
   __TEXT.__objc_methname: 0xf35a
-  __TEXT.__oslogstring: 0xafad
+  __TEXT.__oslogstring: 0xb048
   __TEXT.__objc_classname: 0x5df
   __TEXT.__objc_methtype: 0x1d68
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x13a0
+  __TEXT.__unwind_info: 0x13d0
   __DATA_CONST.__auth_got: 0xa90
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1ee0
-  __DATA_CONST.__cfstring: 0x6de0
+  __DATA_CONST.__const: 0x1ee8
+  __DATA_CONST.__cfstring: 0x6e00
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 5E2C9D37-40C6-330F-91E7-F338AC990561
-  Functions: 2291
+  UUID: D18AB240-7E06-3AFD-B71F-EF3784564556
+  Functions: 2298
   Symbols:   469
-  CStrings:  5551
+  CStrings:  5563
 
CStrings:
+ "%{public}@ attempted to call %{public}s without %{public}@"
+ "CREATE TABLE IF NOT EXISTS admin (key TEXT PRIMARY KEY NOT NULL, value INTEGER NOT NULL);INSERT OR IGNORE INTO admin VALUES ('version', 32);CREATE TABLE IF NOT EXISTS policies (    id        INTEGER    NOT NULL PRIMARY KEY,     bundle_id    TEXT    NOT NULL,     uuid        TEXT    NOT NULL,     display        TEXT    NOT NULL,     UNIQUE (bundle_id, uuid));CREATE TABLE IF NOT EXISTS active_policy (    client        TEXT    NOT NULL,     client_type    INTEGER    NOT NULL,     policy_id    INTEGER NOT NULL,     PRIMARY KEY (client, client_type),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE INDEX IF NOT EXISTS active_policy_id ON active_policy(policy_id);CREATE TABLE IF NOT EXISTS access (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     pid            INTEGER,     pid_version    INTEGER,     boot_uuid      TEXT NOT NULL DEFAULT 'UNUSED',     last_reminded  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     PRIMARY KEY (service, client, client_type, indirect_object_identifier),    FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE TABLE IF NOT EXISTS access_overrides (    service        TEXT    NOT NULL PRIMARY KEY);CREATE TABLE IF NOT EXISTS expired (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     csreq          BLOB,     last_modified  INTEGER     NOT NULL ,     expired_at     INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     PRIMARY KEY (service, client, client_type));CREATE TABLE IF NOT EXISTS integrity_flag (    key TEXT PRIMARY KEY NOT NULL,    value INTEGER NOT NULL);INSERT OR IGNORE INTO integrity_flag VALUES ('integrity_flag', 0);"
+ "Failed to get database integrity flag, code %d"
+ "Failed to reset database integrity flag, code %d"
+ "INSERT OR REPLACE INTO integrity_flag (key, value) VALUES ('integrity_flag', 0)"
+ "SELECT value FROM integrity_flag WHERE key = 'integrity_flag'"
+ "TCCIntegrityFlagCheck"
+ "TCCIntegrityFlagReset"
+ "UPDATE admin SET value = 32 WHERE key = 'version'"
+ "com.apple.private.tcc.flag_manager"
+ "handle_TCCIntegrityFlagCheck"
+ "handle_TCCIntegrityFlagReset"
+ "success"
- "CREATE TABLE IF NOT EXISTS admin (key TEXT PRIMARY KEY NOT NULL, value INTEGER NOT NULL);INSERT OR IGNORE INTO admin VALUES ('version', 30);CREATE TABLE IF NOT EXISTS policies (    id        INTEGER    NOT NULL PRIMARY KEY,     bundle_id    TEXT    NOT NULL,     uuid        TEXT    NOT NULL,     display        TEXT    NOT NULL,     UNIQUE (bundle_id, uuid));CREATE TABLE IF NOT EXISTS active_policy (    client        TEXT    NOT NULL,     client_type    INTEGER    NOT NULL,     policy_id    INTEGER NOT NULL,     PRIMARY KEY (client, client_type),     FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE INDEX IF NOT EXISTS active_policy_id ON active_policy(policy_id);CREATE TABLE IF NOT EXISTS access (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL,     auth_reason    INTEGER     NOT NULL,     auth_version   INTEGER     NOT NULL,     csreq          BLOB,     policy_id      INTEGER,     indirect_object_identifier_type    INTEGER,     indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',     indirect_object_code_identity      BLOB,     flags          INTEGER,     last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     pid            INTEGER,     pid_version    INTEGER,     boot_uuid      TEXT NOT NULL DEFAULT 'UNUSED',     last_reminded  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     PRIMARY KEY (service, client, client_type, indirect_object_identifier),    FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);CREATE TABLE IF NOT EXISTS access_overrides (    service        TEXT    NOT NULL PRIMARY KEY);CREATE TABLE IF NOT EXISTS expired (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     csreq          BLOB,     last_modified  INTEGER     NOT NULL ,     expired_at     INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),     PRIMARY KEY (service, client, client_type));"
- "UPDATE admin SET value = 30 WHERE key = 'version'"

```
