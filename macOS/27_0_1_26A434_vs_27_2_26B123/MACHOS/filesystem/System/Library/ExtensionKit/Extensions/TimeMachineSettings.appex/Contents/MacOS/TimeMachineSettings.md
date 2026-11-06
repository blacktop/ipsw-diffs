## TimeMachineSettings

> `/System/Library/ExtensionKit/Extensions/TimeMachineSettings.appex/Contents/MacOS/TimeMachineSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-2612.1.0.0.0
-  __TEXT.__text: 0x65e90
-  __TEXT.__auth_stubs: 0x22d0
+2615.1.0.0.0
+  __TEXT.__text: 0x670c4
+  __TEXT.__auth_stubs: 0x22e0
   __TEXT.__objc_stubs: 0x2140
   __TEXT.__objc_methlist: 0x914
-  __TEXT.__objc_methname: 0x25ed
+  __TEXT.__objc_methname: 0x263d
   __TEXT.__objc_classname: 0x2e1
-  __TEXT.__objc_methtype: 0x8bd
-  __TEXT.__cstring: 0x367a
-  __TEXT.__ustring: 0x8f0
+  __TEXT.__objc_methtype: 0x8dd
   __TEXT.__const: 0x2a74
-  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__gcc_except_tab: 0x184
+  __TEXT.__cstring: 0x378a
+  __TEXT.__ustring: 0xa86
   __TEXT.__swift5_typeref: 0x5324
   __TEXT.__swift5_capture: 0xa54
   __TEXT.__constg_swiftt: 0xb7c

   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1b58
+  __TEXT.__unwind_info: 0x1bc8
   __TEXT.__eh_frame: 0x3954
-  __DATA_CONST.__const: 0x25c8
-  __DATA_CONST.__cfstring: 0x1260
+  __DATA_CONST.__const: 0x2658
+  __DATA_CONST.__cfstring: 0x12e0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x1178
-  __DATA_CONST.__got: 0x820
+  __DATA_CONST.__auth_got: 0x1180
+  __DATA_CONST.__got: 0x860
   __DATA_CONST.__auth_ptr: 0x850
   __DATA.__objc_const: 0xf88
-  __DATA.__objc_selrefs: 0xa58
+  __DATA.__objc_selrefs: 0xa60
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0x450
-  __DATA.__data: 0x21b8
+  __DATA.__data: 0x2200
   __DATA.__bss: 0x1c18
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1690
+  Functions: 1713
   Symbols:   283
-  CStrings:  828
+  CStrings:  836
 
Symbols:
+ _OBJC_CLASS_$_TMBackupdConnection
- _xpc_dictionary_get_uint64
CStrings:
+ ": no encryption UUID is known"
+ "Cannot update the disk image password for "
+ "Failed to store a disk image password in the System keychain for account '%@', error: %@"
+ "Failed to validate the password for '%@', result: %ld, error: %@"
+ "It may be damaged or may not be an encrypted backup."
+ "Stored a disk image password in the System keychain for account '%@'"
+ "The disk image “%@” couldn’t be opened."
+ "The password couldn’t be checked."
+ "The password couldn’t be saved to the system keychain."
+ "The password is correct, but it couldn’t be saved to the system keychain."
+ "Try again. If the problem persists, restart your Mac."
+ "Your existing backup is unaffected. Try again, and if the problem persists, restart your Mac."
+ "_handlePasswordValidationResult:underlyingError:forDiskImage:encryptionUUID:quota:password:"
+ "connectToBackupd:connectionBlock:"
+ "errorWithSettingsErrorCode:underlyingError:userInfo:"
+ "localizedKeychainItemDiskImagePasswordNameForLocation:"
+ "localizedStringWithFormat:"
+ "storeDiskImagePassword:forKeychainAccount:displayName:reply:"
+ "storeDiskImagePassword:keychainAccount:displayName:returningError:"
+ "v16@?0@\"NSError\"8"
+ "v24@?0@\"<TMPrivilegedXPCProtocol>\"8@?<v@?@\"NSError\">16"
+ "v24@?0q8@\"NSError\"16"
+ "v64@0:8q16@24@32@40@48@56"
+ "validatePassword:forDiskImageAtPath:reply:"
- "An unknown error occurred (%d)"
- "DiskImagePath"
- "Failed to store password in system keychain for account '%@', name '%@'"
- "Failed to validate password for '%@', error: %d"
- "Messaging backupd to validate keychain password for %@"
- "Stored password in system keychain for account '%@', name '%@'"
- "localizedKeychainItemDiskImageCreationPasswordNameFormat"
- "result"
- "sparsebundle"
- "storeDiskImageDecryptionPassword:encryptionUUID:returningError:"
- "storeSystemKeychainPassword:account:name:returningError:"
- "storeSystemKeychainPassword:account:service:"
- "stringByAppendingPathExtension:"
- "tm_posixErrorWithCode:"
- "v12@?0i8"
- "validateKeychainPasswordForDiskImageURL:replyHandler:"
```
