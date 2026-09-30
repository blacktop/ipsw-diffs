## AirPlayUIAgent

> `/System/Library/CoreServices/AirPlayUIAgent.app/Contents/MacOS/AirPlayUIAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0x5e64
-  __TEXT.__auth_stubs: 0x660
+980.77.5.3.0
+  __TEXT.__text: 0x67fc
+  __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0xcc0
   __TEXT.__objc_methlist: 0x59c
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x1d0a
-  __TEXT.__objc_methname: 0x13b5
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__cstring: 0x1f84
+  __TEXT.__objc_methname: 0x13c4
   __TEXT.__ustring: 0xa
   __TEXT.__objc_classname: 0x86
   __TEXT.__objc_methtype: 0x81a
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__cfstring: 0x5a0
+  __TEXT.__unwind_info: 0x150
+  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x238
-  __DATA.__objc_const: 0x938
+  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0x268
+  __DATA.__objc_const: 0x958
   __DATA.__objc_selrefs: 0x600
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x320
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 81
-  Symbols:   180
-  CStrings:  521
+  Functions: 87
+  Symbols:   195
+  CStrings:  535
 
Symbols:
+ _CFArrayApplyBlock
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _FigCFEqual
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ _SecItemUpdate
+ __Unwind_Resume
+ ___objc_personality_v0
+ _dispatch_get_global_queue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kSecAttrService
+ _kSecMatchLimit
+ _kSecMatchLimitAll
+ _kSecReturnAttributes
+ _kSecUseDataProtectionKeychain
- _CFPropertyListCreateFormatted
- _KeychainAddFormatted
- _KeychainCopyMatchingFormatted
- _KeychainUpdateFormatted
- _kSecAttrSynchronizableAny
CStrings:
+ "AirPlayUIAgentCopyPasswordFromKeychain"
+ "AirPlayUIAgentMigrateKeychainItems"
+ "AirPlayUIAgentMigrateKeychainItems_block_invoke"
+ "AirPlayUIAgentSavePasswordForRoute"
+ "Boolean AirPlayUIAgentMigrateKeychainItems(CFArrayRef)"
+ "Boolean AirPlayUIAgentMigrateKeychainItems(CFArrayRef)_block_invoke"
+ "CFStringRef AirPlayUIAgentCopyPasswordFromKeychain(CFStringRef, const char *, CFStringRef, Boolean)"
+ "Failed to search stale keychain. (err: %d)\nquery: %@\n"
+ "Keychain migration failed for %@ (err %#m)\n"
+ "Keychain migration: %s\n"
+ "Keychain migration: failed searching for stale keychain items (err %#m)\n"
+ "Keychain migration: found %ld stale AirPlay item(s)\n"
+ "Keychain migration: migrating item for %@\n"
+ "Keychain migration: skipped, no stale keychain items found\n"
+ "OSStatus AirPlayUIAgentSavePasswordForRoute(CFStringRef, CFStringRef, CFStringRef, Boolean)"
+ "_AirPlayKeychainQueryCreate"
+ "_triedKeychain"
+ "com.apple.airplay.keychain-migration"
+ "com.apple.airplay.password"
+ "complete"
+ "complete with errors"
+ "v16@?0r^v8"
- "CFStringRef _CopyPasswordFromKeychain(CFStringRef, const char *, CFStringRef)"
- "OSStatus _SavePasswordForRoute(CFStringRef, CFStringRef, CFStringRef)"
- "_CopyPasswordFromKeychain"
- "_SavePasswordForRoute"
- "{%kO=%O%kO=%O%kO=%O%kO=%O%kO=%O%kO=%O%kO=%O}"
- "{%kO=%O%kO=%O%kO=%O%kO=%O%kO=%O}"
- "{%kO=%O%kO=%O%kO=%O%kO=%O}"
- "{%kO=%O%kO=%O%kO=%O}"
```
