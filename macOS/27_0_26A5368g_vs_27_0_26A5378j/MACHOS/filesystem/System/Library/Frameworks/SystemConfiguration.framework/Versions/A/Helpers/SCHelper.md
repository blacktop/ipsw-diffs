## SCHelper

> `/System/Library/Frameworks/SystemConfiguration.framework/Versions/A/Helpers/SCHelper`

```diff

-  __TEXT.__text: 0x5570
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__const: 0xa8
-  __TEXT.__oslogstring: 0x593
-  __TEXT.__cstring: 0x4a8
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__const: 0x450
+  __TEXT.__text: 0x5fd8
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__const: 0xb8
+  __TEXT.__oslogstring: 0x7f3
+  __TEXT.__cstring: 0x498
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__cfstring: 0x480
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x40
   __DATA.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   Functions: 47
-  Symbols:   151
-  CStrings:  155
+  Symbols:   168
+  CStrings:  161
 
Sections:
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__auth_ptr : content changed
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
+ _kCFBooleanTrue
+ _kSecAttrService
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecGuestAttributeAudit
+ _kSecMatchSearchList
+ _kSecReturnRef
- __SCPreferencesSystemKeychainPasswordItemExists
Functions:
~ sub_1000019e8 : 1684 -> 1676
~ sub_100004d30 -> sub_100004d28 : 240 -> 260
~ sub_100004e20 -> sub_100004e2c : 216 -> 244
~ sub_100004ef8 -> sub_100004f20 : 216 -> 664
~ sub_100004fd0 -> sub_1000051b8 : 588 -> 84
~ sub_10000521c -> sub_10000520c : 84 -> 2764
CStrings:
+ "SCHelper keychain: caller pid=%d allowed access to \"%{private}@\""
+ "SCHelper keychain: caller pid=%d allowed — no existing item \"%{private}@\" (fresh create)"
+ "SCHelper keychain: caller pid=%d denied access to \"%{private}@\" — caller is not in the item's trusted applications list"
+ "SCHelper keychain: caller pid=%d denied — could not derive SecCodeRef from audit token"
+ "SCHelper keychain: caller pid=%d denied — could not open system keychain"
+ "SCHelper keychain: caller pid=%d denied — could not read ACL of \"%{private}@\""
+ "SCHelper keychain: caller pid=%d denied — lookup of \"%{private}@\" failed, status=%d"
- "KEYCHAIN exists"

```
