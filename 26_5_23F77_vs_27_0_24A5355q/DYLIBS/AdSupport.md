## AdSupport

> `/System/Library/Frameworks/AdSupport.framework/AdSupport`

```diff

 106.2.2.0.0
-  __TEXT.__text: 0x394
-  __TEXT.__auth_stubs: 0xd0
+  __TEXT.__text: 0x36c
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x6d
   __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_classname: 0x14
-  __TEXT.__objc_methname: 0x1fc
-  __TEXT.__objc_methtype: 0x18
-  __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x58
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0xb8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A082C6F-1C88-3660-A705-32DCB47E468E
+  UUID: 0C732E9D-A62A-3020-8AD3-FE6048CF9452
   Functions: 6
   Symbols:   66
-  CStrings:  37
+  CStrings:  9
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[ASIdentifierManager isUserOptedIn] : 140 -> 132
~ -[ASIdentifierManager isAdvertisingTrackingEnabled] : 420 -> 404
~ -[ASIdentifierManager advertisingIdentifier] : 216 -> 200
CStrings:
- "@16@0:8"
- "ASIdentifierManager"
- "B16@0:8"
- "T@\"NSUUID\",R,N"
- "TB,R,N,GisAdvertisingTrackingEnabled"
- "advertisingIdentifier"
- "advertisingTrackingEnabled"
- "boolForKey:"
- "clearAdvertisingIdentifier"
- "date"
- "defaultWorkspace"
- "deviceIdentifierForAdvertising"
- "effectiveBoolValueForSetting:"
- "initWithSuiteName:"
- "initWithUUIDString:"
- "isAdvertisingTrackingEnabled"
- "isBoolSettingLockedDownByRestrictions:"
- "isSharedIPad"
- "isUserOptedIn"
- "objectForKey:"
- "setBool:forKey:"
- "setObject:forKey:"
- "sharedConnection"
- "sharedManager"
- "shouldEnforceTrackingWithReasonCode:"
- "synchronize"
- "timeIntervalSinceDate:"
- "v16@0:8"

```
