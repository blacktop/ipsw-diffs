## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-858.0.1.0.0
-  __TEXT.__text: 0x64328
+858.0.4.0.0
+  __TEXT.__text: 0x663f4
   __TEXT.__auth_stubs: 0x1500
-  __TEXT.__objc_stubs: 0x9120
-  __TEXT.__objc_methlist: 0x4434
-  __TEXT.__cstring: 0xc2fa
+  __TEXT.__objc_stubs: 0x9260
+  __TEXT.__objc_methlist: 0x44cc
+  __TEXT.__cstring: 0xc789
   __TEXT.__const: 0x6c8
-  __TEXT.__gcc_except_tab: 0x1b0c
-  __TEXT.__objc_methname: 0xf39a
-  __TEXT.__oslogstring: 0xb048
+  __TEXT.__gcc_except_tab: 0x1b70
+  __TEXT.__objc_methname: 0xf533
+  __TEXT.__oslogstring: 0xb288
   __TEXT.__objc_classname: 0x5df
-  __TEXT.__objc_methtype: 0x1dbf
+  __TEXT.__objc_methtype: 0x1dd7
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x13d0
+  __TEXT.__unwind_info: 0x1418
   __DATA_CONST.__auth_got: 0xa90
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1ee8
-  __DATA_CONST.__cfstring: 0x6e00
+  __DATA_CONST.__const: 0x1ed0
+  __DATA_CONST.__cfstring: 0x6ee0
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_intobj: 0x4e0
-  __DATA_CONST.__objc_arraydata: 0x1168
-  __DATA_CONST.__objc_dictobj: 0xcf8
+  __DATA_CONST.__objc_arraydata: 0x1178
+  __DATA_CONST.__objc_dictobj: 0xd20
   __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA.__objc_const: 0x8690
-  __DATA.__objc_selrefs: 0x2c60
-  __DATA.__objc_ivar: 0x5d8
+  __DATA.__objc_const: 0x8720
+  __DATA.__objc_selrefs: 0x2cb8
+  __DATA.__objc_ivar: 0x5e4
   __DATA.__objc_data: 0x1040
   __DATA.__data: 0x660
   __DATA.__bss: 0x389

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0C19C298-5A7F-3FB5-AE0A-48455F7223D9
-  Functions: 2298
+  UUID: 3347529A-365B-3565-9B4D-28025049A6F6
+  Functions: 2333
   Symbols:   469
-  CStrings:  5565
+  CStrings:  5619
 
CStrings:
+ "%s: Requestor: %@ is not entitled to read database"
+ "%s: Requestor: %@ is not entitled to reset permission for %s"
+ "%s: failed to allocate accessRecord dictionary array"
+ "-[TCCDDatabaseAccessory postMigrationHandle]"
+ "-[TCCDDatabaseAccessory setDeviceID:locked:]_block_invoke"
+ "-[TCCDServer postMigrationHandle]"
+ "6"
+ "@44@0:8@16@24@?32i40"
+ "Accessory database is deallocated. Failed to operate postMigrationHandle"
+ "CREATE TABLE IF NOT EXISTS accessory_access (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL,     auth_reason    INTEGER     NOT NULL,     flags          INTEGER,     PRIMARY KEY (service, client, client_type))"
+ "DELETE FROM accessory_access"
+ "Getting device unlock status failed"
+ "INSERT OR REPLACE INTO accessory_access (service, client, client_type, auth_value, auth_reason, flags) VALUES (?, ?, ?, ?, ?, ?)"
+ "Open accessory database failed as it's before device first unlock"
+ "SELECT service, client, client_type, auth_value, auth_reason, flags from accessory_access WHERE client=? AND client_type=?"
+ "Service does not support accessory"
+ "TB,N,V_accessorySupport"
+ "TB,N,V_unlockedSinceBoot"
+ "TCCAccessCopyInformationForAccessory"
+ "TCCD_MSG_ALLOW_STANDARD_USER_TO_SET_SYSTEM_SERVICE"
+ "Ti,N,V_encryptionClass"
+ "UniqueDeviceID"
+ "_accessorySupport"
+ "_encryptionClass"
+ "_unlockedSinceBoot"
+ "accessory feature not supported"
+ "accessoryDBOptimization"
+ "accessorySupport"
+ "accessory_access"
+ "client_type is defined in wrong class"
+ "configureAccessoryDatabase"
+ "encryptionClass"
+ "failed to get udid in %s"
+ "getDeviceIDWithLocked:"
+ "handle_TCCAccessCopyInformationForAccessory_with_attribution_chain"
+ "handle_TCCAccessCopyInformationForAccessory_with_attribution_chain_block_invoke_2"
+ "handle_TCCAccessResetInternal_with_attribution_chain_for_accessory"
+ "handle_TCCAccessSetInternalForAccessory"
+ "i28@0:8@16B24"
+ "initWithPathToDatabase:initialSetup:migration:encryptionClass:"
+ "kTCCServiceAccessoryWiFiNetworkSharing"
+ "migrating to have new accessory table"
+ "postMigrationHandle"
+ "previous device id is %@, curreng device id is %@"
+ "relaunching tccd on the different device, purging accessory records"
+ "relaunching tccd on the same device"
+ "setAccessorySupport:"
+ "setDeviceID:locked:"
+ "setEncryptionClass:"
+ "setUnlockedSinceBoot:"
+ "testSetDeviceID:"
+ "unlockedSinceBoot"
+ "updateWithAccessRecord:"
+ "\xf0\xf0\xf0\xb1\xf0B"
- "&"
- "-[TCCDDatabaseAccessory setDeviceID:]_block_invoke"
- "Database failed to open during TCCSQLDatabase init"
- "getDeviceID"
- "i24@0:8@16"
- "setDeviceID:"
- "\xf0\xf0\xf0\xa1\xf0B"

```
