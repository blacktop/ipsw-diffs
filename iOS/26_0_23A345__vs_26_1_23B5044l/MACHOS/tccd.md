## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-854.0.1.0.0
-  __TEXT.__text: 0x5fffc
-  __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_stubs: 0x8bc0
-  __TEXT.__objc_methlist: 0x40a4
-  __TEXT.__cstring: 0xb90c
+857.0.7.0.0
+  __TEXT.__text: 0x63ce4
+  __TEXT.__auth_stubs: 0x1500
+  __TEXT.__objc_stubs: 0x9120
+  __TEXT.__objc_methlist: 0x442c
+  __TEXT.__cstring: 0xc130
   __TEXT.__const: 0x6c8
-  __TEXT.__gcc_except_tab: 0x1974
-  __TEXT.__objc_methname: 0xe9e2
-  __TEXT.__oslogstring: 0xac2b
-  __TEXT.__objc_classname: 0x58f
-  __TEXT.__objc_methtype: 0x1c60
+  __TEXT.__gcc_except_tab: 0x1acc
+  __TEXT.__objc_methname: 0xf35a
+  __TEXT.__oslogstring: 0xafad
+  __TEXT.__objc_classname: 0x5df
+  __TEXT.__objc_methtype: 0x1d68
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x12b8
-  __DATA_CONST.__auth_got: 0xa70
+  __TEXT.__unwind_info: 0x13a0
+  __DATA_CONST.__auth_got: 0xa90
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1db8
-  __DATA_CONST.__cfstring: 0x6bc0
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__const: 0x1ee0
+  __DATA_CONST.__cfstring: 0x6de0
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__objc_intobj: 0x4b0
-  __DATA_CONST.__objc_arraydata: 0x10d0
-  __DATA_CONST.__objc_dictobj: 0xcd0
+  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_intobj: 0x4e0
+  __DATA_CONST.__objc_arraydata: 0x1168
+  __DATA_CONST.__objc_dictobj: 0xcf8
   __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA.__objc_const: 0x7980
-  __DATA.__objc_selrefs: 0x2ab0
-  __DATA.__objc_ivar: 0x584
-  __DATA.__objc_data: 0xf50
-  __DATA.__data: 0x600
-  __DATA.__bss: 0x3a9
-  __DATA.__common: 0x10
+  __DATA.__objc_const: 0x8688
+  __DATA.__objc_selrefs: 0x2c58
+  __DATA.__objc_ivar: 0x5d8
+  __DATA.__objc_data: 0x1040
+  __DATA.__data: 0x660
+  __DATA.__bss: 0x389
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: BFCE821E-65EB-38DC-90A2-C139EE722C5E
-  Functions: 2173
-  Symbols:   465
-  CStrings:  5373
+  UUID: 5E2C9D37-40C6-330F-91E7-F338AC990561
+  Functions: 2291
+  Symbols:   469
+  CStrings:  5551
 
Symbols:
+ _CFStringGetCString
+ _CFStringGetMaximumSizeForEncoding
+ _CFUUIDCreateString
+ _abort
CStrings:
+ "%s: Requestor: %@ is not entitled to reset all permission"
+ "%{public}s%s\n%@ for path to database:%@"
+ "&"
+ "-[TCCDDatabaseAccessory setDeviceID:]_block_invoke"
+ "-[TCCDPolicyOverride _locked_populateGeneralAuthorzationFieldsForService:info:entry:]"
+ "-[TCCDPolicyOverride _locked_populateIndirectAuthorzationFieldsForService:info:entry:]"
+ "-[TCCDPolicyOverride _locked_populatePolicyAuthorizationForSubjectWithInfoDict:message:]"
+ "-[TCCDSQLDatabase _doEval:bind:step:lock:line:]"
+ "/TCCAccessory.db"
+ "@\"<TCCDBaseDatabase>\""
+ "@\"TCCDDatabaseAccessory\""
+ "@40@0:8@16@24@?32"
+ "@64@0:8@16@24Q32Q40Q48Q56"
+ "@?<i@?*@?<v@?^{sqlite3_stmt=}>@?<v@?^{sqlite3_stmt=}>>16@0:8"
+ "Accessory UUID"
+ "Ask every time"
+ "B40@0:8@16@24@32"
+ "CFStringRef get C string error"
+ "CFUUID get CFStringRef error"
+ "CREATE TABLE IF NOT EXISTS admin (key TEXT PRIMARY KEY NOT NULL, value INTEGER NOT NULL);INSERT OR IGNORE INTO admin VALUES ('version', 2);CREATE TABLE IF NOT EXISTS accessory_access (    service        TEXT        NOT NULL,     client         TEXT        NOT NULL,     client_type    INTEGER     NOT NULL,     auth_value     INTEGER     NOT NULL,     auth_reason    INTEGER     NOT NULL,     flags          INTEGER,     PRIMARY KEY (service, client, client_type));CREATE TABLE IF NOT EXISTS tccd_attributes (    key          TEXT        NOT NULL,     value        TEXT        NOT NULL,     PRIMARY KEY (key));"
+ "CREATE TABLE IF NOT EXISTS tccd_attributes (    key          TEXT        NOT NULL,     value        TEXT        NOT NULL,     PRIMARY KEY (key))"
+ "Couldn't create the database for this path: %@"
+ "DELETE FROM %@ WHERE client = ? AND client_type = ?"
+ "Database failed to open during TCCSQLDatabase init"
+ "Database failed to open during _doEval"
+ "EnergyKitGuidance"
+ "Error in loading AEReceiver data in %s"
+ "Error in loading data in %s"
+ "Error in setting the title and info for the prompt for service: %@"
+ "Error: TCCDSQLDatabase has nil `self`"
+ "Failed to remove old database at %@"
+ "INSERT OR REPLACE INTO tccd_attributes (key, value) VALUES ('device_id', ?)"
+ "No coderequirementdata found in %s for %@"
+ "REQUEST_ACCESS_INFO_SERVICE_PRIMARY"
+ "REQUEST_ACCESS_INFO_SERVICE_SECONDARY"
+ "REQUEST_ACCESS_SERVICE_PRIMARY"
+ "REQUEST_ACCESS_SERVICE_SECONDARY"
+ "SELECT service FROM %@ WHERE client = ? AND client_type = ?"
+ "SELECT value FROM tccd_attributes WHERE key='device_id'"
+ "SimulatingDeviceIDChange"
+ "Successfully set prompt string type:%llu for the prompt for service: %@"
+ "T@\"<TCCDBaseDatabase>\",&,V_delegate"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_queue"
+ "T@\"NSString\",&,N,V_initialSetup"
+ "T@\"NSString\",&,N,V_pathToDatabase"
+ "T@\"NSString\",&,V_additionalForSecondaryPromptStringTypeSpecifiedPromptUsageTextLocationalKey"
+ "T@\"NSString\",&,V_requestForSecondaryPromptStringTypeSpecifiedPromptTitleTextLocationalKey"
+ "T@\"TCCDDatabaseAccessory\",R,V_accessoryDatabase"
+ "T@?,C,V_eval"
+ "T@?,C,V_evalLocked"
+ "T@?,C,V_migration"
+ "T@?,C,V_promptTitleAndInfoChoiceBlock"
+ "T@?,R,C"
+ "TB,N,V_unavailable"
+ "TCCAccessResetAll"
+ "TCCDAccessoryIdentity"
+ "TCCDBaseDatabase"
+ "TCCDDatabaseAccessory"
+ "TCCDSQLDatabase"
+ "TCCDSQLDatabase db close for path:%@"
+ "TQ,N,V_promptStringType"
+ "TQ,R,N,V_promptStringType"
+ "TQ,V_promptType"
+ "T^{sqlite3=},V_db"
+ "Thunderbolt"
+ "Ti,N,V_extendedErrorCode"
+ "UPDATE admin SET value = 2 WHERE key = 'version'"
+ "USB"
+ "Unable to load client id from infoDict in %s"
+ "Upgrading accessory database from version %d to %d"
+ "_accessoryDatabase"
+ "_additionalForSecondaryPromptStringTypeSpecifiedPromptUsageTextLocationalKey"
+ "_createDatabase"
+ "_db"
+ "_delegate"
+ "_doEval:bind:step:lock:line:"
+ "_eval"
+ "_evalLocked"
+ "_initialSetup"
+ "_makeTitleAndInfoStringChoiceBlock:"
+ "_migration"
+ "_pathToDatabase"
+ "_promptStringType"
+ "_promptTitleAndInfoChoiceBlock"
+ "_requestForSecondaryPromptStringTypeSpecifiedPromptTitleTextLocationalKey"
+ "_unavailable"
+ "accessoryDatabase"
+ "accessoryPermission"
+ "accessory_uuid"
+ "additionalForSecondaryPromptStringTypeSpecifiedPromptUsageTextLocationalKey"
+ "ask_every_time"
+ "choicesForCurrentPromptStringType:title:info:"
+ "closeDatabase"
+ "com.apple.tcc.db_queue_"
+ "commit"
+ "creating tccd_attributes table"
+ "db"
+ "db bind error for %s"
+ "delegate"
+ "eval"
+ "eval:bind:step:"
+ "evalLocked"
+ "evalLocked:bind:step:"
+ "full path to accessory db is nil"
+ "getAccessoryDBFullPath"
+ "getDeviceID"
+ "getInitialSetupQuery"
+ "graphic-icon.thunderbolt"
+ "graphic-icon.usb"
+ "handle_TCCAccessResetAll"
+ "handle_TCCAccessResetInternal_with_attribution_chain_for_process"
+ "handle_TCCAccessSetInternalForProcess"
+ "i16@?0@\"TCCDSQLDatabase\"8"
+ "i24@0:8@16"
+ "i32@?0Q8^@16^@24"
+ "i32@?0r*8@?<v@?^{sqlite3_stmt=}>16@?<v@?^{sqlite3_stmt=}>24"
+ "i40@0:8@16@?24@?32"
+ "i40@0:8Q16^@24^@32"
+ "i40@0:8r*16@?24@?32"
+ "i48@0:8r*16@?24@?32B40i44"
+ "initWithIdentifier:authority:"
+ "initWithPathToDatabase:initialSetup:migration:"
+ "initWithSubject:object:authorizationValue:authorizationReason:authorizationVersion:flags:"
+ "initialSetup"
+ "is_valid_authorization_for_service"
+ "kTCCServiceEnergyKitGuidance"
+ "lastPathComponent"
+ "migration"
+ "openDatabase"
+ "pathToDatabase"
+ "promptStringType"
+ "promptTitleAndInfoChoiceBlock"
+ "recordForAccessoryIdentityFromMessage:error:"
+ "recordForCodeIdentityFromMessage:accessIdentity:indirectObjectIdentity:error:"
+ "removeDatabase"
+ "requestAdditionalPrimaryTextNameForServiceName:"
+ "requestAdditionalSecondaryTextNameForServiceName:"
+ "requestForSecondaryPromptStringTypeSpecifiedPromptTitleTextLocationalKey"
+ "requestPrimaryTitleTextLocalizationKeyNameForServiceName:"
+ "requestSecondaryTitleTextLocalizationKeyNameForServiceName:"
+ "request_prompt_string_type"
+ "setAdditionalForSecondaryPromptStringTypeSpecifiedPromptUsageTextLocationalKey:"
+ "setDb:"
+ "setDeviceID:"
+ "setEval:"
+ "setEvalLocked:"
+ "setExtendedErrorCode:"
+ "setInitialSetup:"
+ "setMigration:"
+ "setPathToDatabase:"
+ "setPromptStringType:"
+ "setPromptTitleAndInfoChoiceBlock:"
+ "setRequestForSecondaryPromptStringTypeSpecifiedPromptTitleTextLocationalKey:"
+ "setUnavailable:"
+ "setUpMigration"
+ "set_device_id_block_invoke"
+ "stringByDeletingLastPathComponent"
+ "stringWithCString:encoding:"
+ "transaction:"
+ "unavailable"
+ "using accessory database version: %d"
+ "\xf0\xf0\xf0\xa1\xf0B"
- "handle_TCCAccessResetInternal_with_attribution_chain"
- "\xf0\xf0\xf0\xa1\xf02"

```
