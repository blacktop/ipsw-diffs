## SystemExtensions

> `/System/Library/Frameworks/SystemExtensions.framework/SystemExtensions`

```diff

 224.0.0.0.0
-  __TEXT.__text: 0xcb0
-  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__text: 0xc0c
   __TEXT.__objc_methlist: 0x160
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x18b
+  __TEXT.__cstring: 0x18d
   __TEXT.__oslogstring: 0x24
-  __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x4e9
-  __TEXT.__objc_methtype: 0x9b
-  __TEXT.__objc_stubs: 0x3c0
-  __DATA_CONST.__got: 0x60
+  __TEXT.__unwind_info: 0x90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x370
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F6CA6DC-0B26-3CE9-8B0B-7ED94C1093DA
+  UUID: 8243DDE3-762B-3AE4-9A58-36216D244DC9
   Functions: 27
-  Symbols:   187
-  CStrings:  106
+  Symbols:   190
+  CStrings:  27
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x25
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x24
Functions:
~ +[OSSystemExtensionsWorkspace sharedWorkspace] : 84 -> 68
~ -[OSSystemExtensionsWorkspace systemExtensionsForApplicationWithBundleID:error:] : 1464 -> 1392
~ _applicationDisplayNameForExecutable : 384 -> 368
~ -[OSSystemExtensionProperties initWithBundleIdentifier:isEnabled:displayName:usageDescription:] : 184 -> 192
~ -[OSSystemExtensionProperties encodeWithCoder:] : 236 -> 224
~ -[OSSystemExtensionProperties initWithCoder:] : 300 -> 288
~ -[OSSystemExtensionsWorkspace systemExtensionsForApplicationWithBundleID:error:].cold.1 : 116 -> 72
CStrings:
- ".cxx_destruct"
- "@\"NSString\""
- "@\"NSURL\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8@16^@24"
- "@44@0:8@16B24@28@36"
- "B"
- "B16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "OSSystemExtensionProperties"
- "OSSystemExtensionsWorkspace"
- "T@\"NSString\",&,V_bundleIdentifier"
- "T@\"NSString\",&,V_displayName"
- "T@\"NSString\",&,V_usageDescription"
- "T@\"NSString\",R,V_bundleShortVersion"
- "T@\"NSString\",R,V_bundleVersion"
- "T@\"NSURL\",R,V_URL"
- "T@\"OSSystemExtensionsWorkspace\",R"
- "TB,R"
- "TB,R,V_isAwaitingUserApproval"
- "TB,R,V_isUninstalling"
- "TB,V_isEnabled"
- "URL"
- "_URL"
- "_bundleIdentifier"
- "_bundleShortVersion"
- "_bundleVersion"
- "_displayName"
- "_isAwaitingUserApproval"
- "_isEnabled"
- "_isUninstalling"
- "_usageDescription"
- "addObject:"
- "bundleShortVersion"
- "bundleVersion"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultManager"
- "dictionaryWithObjects:forKeys:count:"
- "displayNameAtPath:"
- "driverApprovalStatesForThirdPartyApp:"
- "driverIsApproved"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "init"
- "initWithBundleIdentifier:isEnabled:displayName:usageDescription:"
- "initWithCoder:"
- "isAwaitingUserApproval"
- "isEqualToString:"
- "isUninstalling"
- "localizedDescription"
- "mainBundle"
- "path"
- "refreshForCurrentAppSync"
- "setBundleIdentifier:"
- "setDisplayName:"
- "setIsEnabled:"
- "setUsageDescription:"
- "sharedManager"
- "sharedWorkspace"
- "stringWithFormat:"
- "supportsSecureCoding"
- "systemExtensionsForApplicationWithBundleID:error:"
- "usageText"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"

```
