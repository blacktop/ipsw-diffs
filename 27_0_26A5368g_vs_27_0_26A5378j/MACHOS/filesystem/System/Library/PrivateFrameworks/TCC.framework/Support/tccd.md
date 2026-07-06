## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-  __TEXT.__text: 0x82cc8
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_stubs: 0x9400
-  __TEXT.__objc_methlist: 0x3fac
-  __TEXT.__cstring: 0x115da
-  __TEXT.__const: 0x628
-  __TEXT.__gcc_except_tab: 0x2fe0
-  __TEXT.__objc_methname: 0xf4d7
-  __TEXT.__oslogstring: 0xdb83
+  __TEXT.__text: 0x865b8
+  __TEXT.__auth_stubs: 0x1600
+  __TEXT.__objc_stubs: 0x9620
+  __TEXT.__objc_methlist: 0x409c
+  __TEXT.__cstring: 0x11c2c
+  __TEXT.__const: 0x638
+  __TEXT.__gcc_except_tab: 0x31a8
+  __TEXT.__objc_methname: 0xf866
+  __TEXT.__oslogstring: 0xe38d
   __TEXT.__objc_classname: 0x4ae
-  __TEXT.__objc_methtype: 0x146f
-  __TEXT.__unwind_info: 0x14e0
-  __DATA_CONST.__const: 0x24d8
-  __DATA_CONST.__cfstring: 0x7f20
+  __TEXT.__objc_methtype: 0x149f
+  __TEXT.__unwind_info: 0x1568
+  __DATA_CONST.__const: 0x25f8
+  __DATA_CONST.__cfstring: 0x8260
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_intobj: 0x4f8
-  __DATA_CONST.__objc_arraydata: 0x1718
+  __DATA_CONST.__objc_arraydata: 0x17e8
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0xf00
-  __DATA_CONST.__auth_got: 0xb08
-  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__auth_got: 0xb10
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA.__objc_const: 0x7b68
-  __DATA.__objc_selrefs: 0x2b48
-  __DATA.__objc_ivar: 0x634
+  __DATA.__objc_const: 0x7c08
+  __DATA.__objc_selrefs: 0x2be8
+  __DATA.__objc_ivar: 0x640
   __DATA.__objc_data: 0xf50
   __DATA.__data: 0x348
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x354
+  __DATA.__bss: 0x364
   __DATA.__common: 0x20
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2452
-  Symbols:   501
-  CStrings:  6011
+  Functions: 2521
+  Symbols:   502
+  CStrings:  6141
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _xpc_array_get_value
CStrings:
+ " AND auth_value != ? AND auth_value != ?"
+ "%s Check for TCC registry records: %{private}@"
+ "%s Skipping. Failed to check TCC in legacy path"
+ "%s Skipping. TCC not registered: %{private}@"
+ "%s: caller missing %@ entitlement"
+ "%s: failed to create forwarded XPC message"
+ "%s: ignoring on user-agent tccd"
+ "%s: merging %zu records from system tccd for %{public}s"
+ "%s: merging %zu system tccd records (auth_value != unknown) for service=%{public}s client=%{public}s"
+ "%s: missing %s payload"
+ "%s: no reply from system tccd"
+ "%s: system tccd has no TCCDManagedSettings instance"
+ "%s: system tccd query failed: %{public}s"
+ "%s: system tccd reset failed: %{public}s"
+ "%s: system tccd reset result=%d for service=%{public}s client=%{public}s"
+ "%{public}s: %{private}@"
+ "-[TCCDDirectoryManager checkIsPathInRootVolume:]"
+ "-[TCCDDirectoryManager checkLegacyDatabaseRegisteredAtPath:]"
+ "2G98R5QYU5/com.kingsoft.wpsoffice.mac.global"
+ "3E9E9FN277/com.graphisoft.archicad29"
+ "4788TTJ39Y/com.wiheads.paste"
+ "4EJSV8E65Y/com.druide.AgentAntidote"
+ "4SNPZZ27XN/eziowave"
+ "79RR9LPM2N/com.macitbetter.betterzip"
+ "829ZY6G65P/com.seclore.SecloreLite.InstallHelper"
+ "8S7YS6Z5ZQ/com.ametiq.simed"
+ "97GAAZ6CPX/com.renewedvision.propresenter"
+ "<no reply>"
+ "<unknown>"
+ "@\"TCCDManagedSettings\""
+ "A43FW9RYK2/com.mendeley.desktop"
+ "AU2ALARPUP/com.fasttracksoftware.adminbyrequest"
+ "B32@0:8@16@?24"
+ "BJ4HAAB9B3/us.zoom.pluginagent"
+ "D6XDM4N99E/com.mcneel.rhinoceros.8"
+ "DE8Y96K9QP/com.cisco.webex.pluginservice"
+ "DE8Y96K9QP/com.cisco.webexmeetingsapp"
+ "DELETE FROM managed_overrides WHERE service = ?"
+ "EEUF3NPG73/com.exclaimer.csua"
+ "FORWARD-SYS: request: %{public}@"
+ "LFNG3Q6WX2/net.nemetschek.vectorworks"
+ "ManagedSettings: applying %lu forwarded per-system clients on system tccd"
+ "ManagedSettings: cleared %d legacy kTCCServiceAccessibility row(s) from user-agent managed_overrides (now owned by system tccd)"
+ "ManagedSettings: database is nil, cannot apply forwarded system permissions"
+ "ManagedSettings: database is nil, cannot clear legacy Accessibility records"
+ "ManagedSettings: failed to clear legacy kTCCServiceAccessibility rows: %d"
+ "ManagedSettings: failed to create XPC message for system tccd forward"
+ "ManagedSettings: failed to dispatch system tccd forward message"
+ "ManagedSettings: forwarding %lu per-system clients to system tccd"
+ "ManagedSettings: skipping MOEffectiveSettingsStore observer on system tccd; updates arrive via user-agent tccd forward"
+ "ManagedSettings: system tccd forward acknowledged"
+ "ManagedSettings: system tccd forward failed: %{public}s"
+ "NSSiriUsageDescription"
+ "QED4VVPZWA/com.logi.pluginservice"
+ "REPLY-SYS: reply: %{public}@"
+ "S5LKE7JNDX/com.roli.hub"
+ "S8EX82NJP6/com.macpaw.site.theunarchiver"
+ "SELECT 1 FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
+ "SELECT COUNT(*) FROM managed_overrides WHERE service = ?"
+ "SELECT admin_auth_value, auth_value, flags FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
+ "SELECT admin_auth_value, auth_version FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
+ "SetHealthKitAPIOverride"
+ "SetHealthKitAPIOverride: %{public}lld"
+ "T@\"TCCDManagedSettings\",&,N,V_managedSettings"
+ "TB,N,V_usageStringPolicyAuthorizedByForwarder"
+ "TCCD_MSG_MESSAGE_OPTION_USAGE_STRING_POLICY_AUTHORIZED_BY_FORWARDER_KEY"
+ "TCCManagedSettingsApplyForSystemServices"
+ "Tq,V_healthKitAPIOverride"
+ "XXKJ396S2Y/com.autodesk.AutoCAD2024"
+ "XXKJ396S2Y/com.autodesk.AutoCAD2027"
+ "XXKJ396S2Y/com.autodesk.AutoCADLT2026_StandAlone"
+ "_forwardSystemPermissionsToSystemTCCD:"
+ "_healthKitAPIOverride"
+ "_managedSettings"
+ "_resetRemovedManagedTCCDefaultsWithPermissionsMap:"
+ "_updateManagedTCCDefaultsWithPermissionsMap:"
+ "_usageStringPolicyAuthorizedByForwarder"
+ "applyForwardedSystemPermissions:"
+ "canOverridePromptPolicyForRequestor:withForwarderStamp:"
+ "checkIsPathInRootVolume:"
+ "checkLegacyDatabaseRegisteredAtPath:"
+ "clearLegacyAccessibilityRecordsFromUserDatabase"
+ "com.apple.private.tcc.system-tccd-forwarder"
+ "do_not_forward_to_other_tccd"
+ "handle_TCCManagedSettingsApplyForSystemServices"
+ "healthKitAPIOverride"
+ "isAuthSetViaDisclosurePrompt"
+ "launch_angel_full_sheet_prompt"
+ "managedSettings"
+ "permissionsMapFromTCCDefaults:"
+ "registerNewDatabaseAtPath:"
+ "sendMessageAsyncToSystemTCCD: failed to create connection"
+ "sendMessageAsyncToSystemTCCD: refused on system tccd (would send to ourself)"
+ "sendMessageAsyncToSystemTCCD:withReplyBlock:"
+ "sendMessageSyncToSystemTCCD reply: %{public}@"
+ "sendMessageSyncToSystemTCCD request: %{public}@"
+ "sendMessageSyncToSystemTCCD:"
+ "sendMessageSyncToSystemTCCD: failed to create connection"
+ "sendMessageSyncToSystemTCCD: refused on system tccd (would send to ourself)"
+ "setHealthKitAPIOverride:"
+ "setManagedSettings:"
+ "setUsageStringPolicyAuthorizedByForwarder:"
+ "splitPermissionsMap:intoUserPermissions:systemPermissions:"
+ "stampForwardedRequest:withRequestor:"
+ "string"
+ "system tccd handling cross-tccd %{public}s() locally"
+ "system_permissions"
+ "usageStringPolicyAuthorizedByForwarder"
+ "v40@0:8@16o^@24o^@32"
+ "validateExistingDatabaseAtPath:"
- "-[TCCDDirectoryManager isPathInRootVolume:]"
- "SELECT admin_auth_value FROM managed_overrides WHERE service = ? AND client = ? AND client_type = ?"
- "_resetRemovedManagedTCCDefaults:"
- "_updateManagedTCCDefaults:"
- "c24@0:8@16"
- "isPathInRootVolume:"

```
