## SPLegacySoftwareReporter

> `/System/Library/SystemProfiler/SPLegacySoftwareReporter.spreporter/Contents/MacOS/SPLegacySoftwareReporter`

```diff

-22.0.0.0.0
-  __TEXT.__text: 0x348c
-  __TEXT.__auth_stubs: 0x140
-  __TEXT.__objc_stubs: 0x700
-  __TEXT.__objc_methlist: 0xdc
-  __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x3d6
-  __TEXT.__objc_methname: 0x3ea
-  __TEXT.__oslogstring: 0x979
-  __TEXT.__objc_classname: 0x23
-  __TEXT.__objc_methtype: 0x95
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__cfstring: 0x720
-  __DATA_CONST.__objc_classlist: 0x10
+23.0.0.0.0
+  __TEXT.__text: 0x109c
+  __TEXT.__auth_stubs: 0xd0
+  __TEXT.__objc_stubs: 0x180
+  __TEXT.__objc_methlist: 0x14
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x2b6
+  __TEXT.__oslogstring: 0x111
+  __TEXT.__ustring: 0x10
+  __TEXT.__objc_methname: 0xe1
+  __TEXT.__objc_classname: 0x19
+  __TEXT.__objc_methtype: 0xb
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__cfstring: 0x540
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0xa8
-  __DATA_CONST.__got: 0x80
-  __DATA.__objc_const: 0x228
-  __DATA.__objc_selrefs: 0x1e0
-  __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x40
+  __DATA.__objc_const: 0x90
+  __DATA.__objc_selrefs: 0x68
+  __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/Ecosystem.framework/Versions/A/Ecosystem
   - /System/Library/PrivateFrameworks/SPSupport.framework/Versions/A/SPSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 41
-  Symbols:   65
-  CStrings:  178
+  Functions: 15
+  Symbols:   64
+  CStrings:  61
 
Symbols:
+ _OBJC_CLASS_$_NSNull
+ _SPLSRDetail_build
+ _SPLSRDetail_reasonKey
+ _SPLegacySoftwareReporter_updateDictionaryWithItems
+ _kSPLSRKeyIdentityBundleID
+ _kSPLSRKeyIdentityPath
+ _kSPLSRKeyIdentityTeamID
+ _kSPLSRKeyIdentityVersion
+ _kSPLSRKeyNumberOfTimesLaunched
+ _kSPLSRKeyPreviouslyLaunchedDate
+ _kSPLSRKeyProcessBundleID
+ _kSPLSRKeyProcessBundleVersion
+ _kSPLSRKeyProcessDeveloperName
+ _kSPLSRKeyProcessName
+ _kSPLSRKeyProcessPath
+ _kSPLSRKeyProcessTeamID
+ _kSPLSRKeyProcessUID
+ _kSPLSRKeyReason
+ _kSPLSRKeyResponsibleBundleID
+ _kSPLSRKeyResponsibleBundleVersion
+ _kSPLSRKeyResponsibleDeveloperName
+ _kSPLSRKeyResponsibleName
+ _kSPLSRKeyResponsiblePath
+ _kSPLSRKeyResponsibleTeamID
+ _kSPLSRKeyTargetBundleID
+ _kSPLSRKeyTargetBundleVersion
+ _kSPLSRKeyTargetDeveloperName
+ _kSPLSRKeyTargetName
+ _kSPLSRKeyTargetPath
+ _kSPLSRKeyTargetTeamID
+ _kSPLSRNotAvailable
+ _kSPLSRSectionProcessIdentity
+ _kSPLSRSectionResponsibleIdentity
+ _kSPLSRSectionTargetIdentity
- OBJC_IVAR_$_SPLSRNode._children
- OBJC_IVAR_$_SPLSRNode._item
- OBJC_IVAR_$_SPLSRNode._most_recent_launch
- OBJC_IVAR_$_SPLSRNode._name
- OBJC_IVAR_$_SPLSRNode._num_times_launched
- OBJC_IVAR_$_SPLSRNode._processNames
- OBJC_IVAR_$_SPLSRNode._resp_dev
- OBJC_IVAR_$_SPLSRNode._resp_name
- _CFPreferencesAppSynchronize
- _CFPreferencesGetAppBooleanValue
- _CFPreferencesSetAppValue
- _OBJC_CLASS_$_NSCharacterSet
- _OBJC_CLASS_$_NSDateFormatter
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$_NSTimeZone
- _OBJC_CLASS_$_SPLSRNode
- _OBJC_METACLASS_$_SPLSRNode
- _SPLegacySoftwareReporter_arrangeProcessItems
- _SPLegacySoftwareReporter_getPresentableName
- _SPLegacySoftwareReporter_includeAppleProcessesOverride
- _SPLegacySoftwareReporter_removeDeveloperFields
- _SPLegacySoftwareReporter_renderBucket
- _SPLegacySoftwareReporter_renderLegacyBuckets
- _SPLegacySoftwareReporter_renderProductKeyGroupedBuckets
- _SPLegacySoftwareReporter_setIncludeAppleProcesses
- __os_log_disabled
- __os_log_impl
- _kCFBooleanFalse
- _kCFBooleanTrue
- _objc_storeStrong
- _objc_unsafeClaimAutoreleasedReturnValue
- _os_variant_has_internal_content
CStrings:
+ "%@ (Loading: %@)"
+ "%@ – %@"
+ "Due to Target"
+ "Not Available"
+ "SPLSRDetail_reasonKey: unrecognized reason %{public}@"
+ "SPLSRNode: previously_launched_date is %{public}@, expected NSDate"
+ "SPLegacySoftwareReporter: no items returned from Ecosystem.framework"
+ "SPLegacySoftwareReporter: skipping non-dictionary process item of class %{public}@"
+ "identity_bundle_id"
+ "identity_path"
+ "identity_team_id"
+ "identity_version"
+ "null"
+ "process_bundle_version"
+ "process_identity"
+ "process_path"
+ "process_uid"
+ "responsible_bundle_version"
+ "responsible_identity"
+ "responsible_team_id"
+ "target_bundle_id"
+ "target_bundle_version"
+ "target_developer_name"
+ "target_identity"
+ "target_name"
+ "target_path"
+ "target_team_id"
- ""
- "\n\nSPLSR_arrangeProcessItems: PROCESSING: %@"
- "    **Detected product_key support from ecosystemd"
- "   [%@] already has child [%@], what do do here..."
- "   [%@] does not have this child - adding [%@] to children"
- "   [%@] has no children - adding child dictionary with [%@]"
- "  **Finished processing responsibleDeveloperName: %@"
- "  **Processing responsibleDeveloperName: %@"
- "  [%@] Reason: %@"
- " Setting to True for Internal Build"
- "%@%@"
- "***************Processing Item*******************"
- "**responsibleDeveloperNames: %@"
- ".cxx_destruct"
- ":"
- "<name: %@> {\n  resp_dev: %@\n  resp_name: %@\n  num_times_launched: %@\n  most_recent_launch: %@\n  children: %@\n}"
- "<nil>"
- "<unknown>"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@16@0:8"
- "@32@0:8@16@24"
- "Apple"
- "B16@0:8"
- "ERROR RETRIEVING VALUE"
- "ERROR receiving ProcessItems from Ecosystem.Framework"
- "FALSE"
- "SPLSR: Unexpected empty processNameGroup for bucket: %@"
- "SPLSR: Using legacy rendering logic (no product_key)"
- "SPLSR: Using product_key grouping logic"
- "SPLSR: is_embedded_component field not provided by ecosystemd, using fallback (false)"
- "SPLSRIncludeAppleProcesses"
- "SPLSRNode"
- "SPLSR_BUCKETING DEBUG: Using processName bucket: %@"
- "SPLSR_BUCKETING DEBUG: Using responsibleName bucket: %@"
- "SPLSR_BUCKETING DEBUG: process=%@, responsible=%@, productKey=%@, responsiblePath=%@, isEmbedded=%d, detach=%d"
- "SPLSR_arrangeProcessItems: 'prevLaunchDate' is not a valid NSDate."
- "SPLSR_arrangeProcessItems: 'processBundleId' is not a valid NSString."
- "SPLSR_arrangeProcessItems: 'processDeveloperName' is not a valid NSString."
- "SPLSR_arrangeProcessItems: 'processName' is not a valid NSString."
- "SPLSR_arrangeProcessItems: 'processTeamId' is not a valid NSString."
- "SPLSR_arrangeProcessItems: 'productKey' is not a valid NSString."
- "SPLSR_arrangeProcessItems: 'responsibleBundleId' is not a valid NSString."
- "SPLSR_arrangeProcessItems: 'responsibleDeveloperName' is not a valid NSString."
- "SPLSR_arrangeProcessItems: 'responsibleName' is not a valid NSString."
- "SPLSR_arrangeProcessItems: 'responsiblePath' is not a valid NSString."
- "SPLSR_arrangeProcessItems: Found Apple-signed process: %@"
- "SPLSR_arrangeProcessItems: Found MAS process %@"
- "SPLSR_arrangeProcessItems: Including Apple processes as requested"
- "SPLSR_arrangeProcessItems: Sanitizing MAS process"
- "SPLSR_arrangeProcessItems: Sanitizing MAS responsible developer for Apple process: %@"
- "SPLSR_arrangeProcessItems: Sanitizing unknown responsible developer process: %@"
- "SPLSR_arrangeProcessItems: Sanitizing where process bundle != responsible bundle: %@"
- "SPLSR_arrangeProcessItems: Skipping Apple processes as requested"
- "SPLSR_includeAppleProcessesOverride: Unable to read value for SPLSRIncludeAppleProcesses. %@"
- "SPLSR_includeAppleProcessesOverride: defaults value: %@"
- "SPLSR_includeAppleProcessesOverride: detected an internal build"
- "SPLegacySoftwareReporter_MISSING_NAME_HOLDER"
- "Steam"
- "TRUE"
- "UTC"
- "_children"
- "_item"
- "_most_recent_launch"
- "_num_times_launched"
- "_processNames"
- "_resp_dev"
- "_resp_name"
- "addChildNode:"
- "addObjectsFromArray:"
- "addProcessNames:"
- "allKeys"
- "allObjects"
- "array"
- "arrayWithCapacity:"
- "boolValue"
- "capitalizedString"
- "com.apple."
- "com.apple.SPLegacySoftwareReporter"
- "com.apple.ecosystemd"
- "componentsSeparatedByString:"
- "containsString:"
- "count"
- "description"
- "dict"
- "dictionaryWithDictionary:"
- "en_US_POSIX"
- "exec"
- "firstObject"
- "has_native_version"
- "has_native_version_no"
- "has_native_version_yes"
- "init"
- "isEqualTo:"
- "isEqualToSet:"
- "isLeaf"
- "isNotEqualTo:"
- "isRoot"
- "is_embedded_component"
- "laterDate:"
- "localeWithLocaleIdentifier:"
- "main"
- "mutableCopy"
- "name"
- "node"
- "nodeWithName:"
- "nodeWithName:item:"
- "now"
- "objectAtIndexedSubscript:"
- "process"
- "processNames"
- "process_info"
- "process_names"
- "product_display_name"
- "product_key"
- "reason_source"
- "reason_x86_forced_explicit"
- "removeObject:"
- "removeObjectForKey:"
- "responsible"
- "responsible_info"
- "set"
- "setDateFormat:"
- "setItem:"
- "setLocale:"
- "setName:"
- "setObject:forKey:"
- "setTimeZone:"
- "steam_osx"
- "stringByTrimmingCharactersInSet:"
- "substringFromIndex:"
- "substringToIndex:"
- "target"
- "timeZoneWithAbbreviation:"
- "uid"
- "v16@0:8"
- "v24@0:8@16"
- "valueForKey:"
- "whitespaceCharacterSet"
- "yyyy-MM-dd HH:mm:ss"
```
