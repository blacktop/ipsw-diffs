## SCHelper

> `System/Library/Frameworks/SystemConfiguration.framework/Versions/A/Helpers/SCHelper`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__auth_ptr`

```diff

-1405.160.3.0.0
-  __TEXT.__text: 0x54f8
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x548
-  __TEXT.__cstring: 0x4ac
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x418
-  __DATA_CONST.__got: 0x60
+1405.160.3.701.3
+  __TEXT.__text: 0x5f9c
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__const: 0xc0
+  __TEXT.__oslogstring: 0x7f3
+  __TEXT.__cstring: 0x498
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x450
-  __DATA_CONST.__cfstring: 0x4a0
+  __DATA_CONST.__const: 0x428
+  __DATA_CONST.__cfstring: 0x480
   __DATA.__data: 0x40
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   Functions: 47
-  Symbols:   150
-  CStrings:  120
+  Symbols:   168
+  CStrings:  125
 
Symbols:
+ _CFArrayCreate
+ _CFDataCreate
+ _CFDictionaryCreateMutable
+ _SecACLCopyContents
+ _SecAccessCopyACLList
+ _SecCodeCheckValidity
+ _SecCodeCopyGuestWithAttributes
+ _SecItemCopyMatching
+ _SecKeychainItemCopyAccess
+ _SecTrustedApplicationCopyRequirement
+ __SCSecKeychainCopySystemKeychain
+ _audit_token_to_pid
+ _kCFBooleanTrue
+ _kSecAttrService
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecGuestAttributeAudit
+ _kSecMatchSearchList
+ _kSecReturnRef
- __SCPreferencesSystemKeychainPasswordItemExists
Functions:
~ sub_100002028 -> sub_100002060 : 1720 -> 1708
~ sub_100002dfc -> sub_100002e28 : 504 -> 532
~ sub_100003554 -> sub_10000359c : 588 -> 612
~ sub_100003aac -> sub_100003b0c : 1800 -> 1812
~ sub_100004c8c -> sub_100004cf8 : 232 -> 252
~ sub_100004d74 -> sub_100004df4 : 216 -> 244
~ sub_100004e4c -> sub_100004ee8 : 216 -> 656
~ sub_100004f24 -> sub_100005178 : 576 -> 84
~ sub_100005164 -> sub_1000051cc : 84 -> 2768
~ sub_1000051b8 -> sub_100005c9c : 464 -> 460
~ sub_100005388 -> sub_100005e68 : 764 -> 760
CStrings:
+ "  %p {port = %p, pid = %d, path = %{private}s%s}"
+ "%p : open, pid=%d"
+ "SCHelper keychain: caller pid=%d allowed access to \"%{private}@\""
+ "SCHelper keychain: caller pid=%d allowed — no existing item \"%{private}@\" (fresh create)"
+ "SCHelper keychain: caller pid=%d denied access to \"%{private}@\" — caller is not in the item's trusted applications list"
+ "SCHelper keychain: caller pid=%d denied — could not derive SecCodeRef from audit token"
+ "SCHelper keychain: caller pid=%d denied — could not open system keychain"
+ "SCHelper keychain: caller pid=%d denied — could not read ACL of \"%{private}@\""
+ "SCHelper keychain: caller pid=%d denied — lookup of \"%{private}@\" failed, status=%d"
+ "SCPreferences %s access to \"%{private}@\" denied, no authorization for pid=%d, status = %d"
+ "SCPreferences access to \"%{private}@\" denied, no [read] entitlement for pid=%d"
+ "SCPreferences access to \"%{private}@\" denied, no [write] entitlement for pid=%d"
+ "SecTaskCopyValueForEntitlement(,\"%@\",) failed, error = %@ : pid=%d"
+ "SecTaskCreateWithAuditToken() failed: pid=%d"
+ "data not valid, length = %ld"
+ "hasAuthorization() session pid=%d: entitlement=%@: not valid"
+ "interface \"%{private}@\" not refreshed: %s"
+ "prefsID (%{private}@) not valid"
- "  %p {port = %p, caller = %@, path = %s%s}"
- "%p : open, prefs = %@"
- "???"
- "KEYCHAIN exists"
- "SCPreferences %s access to \"%@\" denied, no authorization for \"%@\", status = %d"
- "SCPreferences access to \"%@\" denied, no [read] entitlement for \"%@\""
- "SCPreferences access to \"%@\" denied, no [write] entitlement for \"%@\""
- "SecTaskCopyValueForEntitlement(,\"%@\",) failed, error = %@ : %@"
- "SecTaskCreateWithAuditToken() failed: %@"
- "data not valid, %@"
- "hasAuthorization() session=%@: entitlement=%@: not valid"
- "interface \"%@\" not refreshed: %s"
- "prefsID (%@) not valid"
```
