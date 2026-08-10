## CloudSharing

> `/System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-236.0.0.0.0
-  __TEXT.__text: 0x38d94
-  __TEXT.__objc_methlist: 0x4f8
-  __TEXT.__const: 0x37c
-  __TEXT.__cstring: 0xb7
+240.0.0.0.0
+  __TEXT.__text: 0x39bd8
+  __TEXT.__objc_methlist: 0x530
+  __TEXT.__const: 0x38c
+  __TEXT.__cstring: 0xf7
   __TEXT.__constg_swiftt: 0x1e8
-  __TEXT.__swift5_typeref: 0x443
+  __TEXT.__swift5_typeref: 0x453
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x23
   __TEXT.__swift5_fieldmd: 0x3c

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x137c
-  __TEXT.__oslogstring: 0xee4
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__oslogstring: 0x1054
+  __TEXT.__unwind_info: 0x430
   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b0
+  __DATA_CONST.__objc_selrefs: 0x438
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0x39d8
   __AUTH_CONST.__objc_const: 0x2d8
-  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__auth_got: 0x528
   __AUTH.__objc_data: 0x48
-  __DATA.__data: 0x178
+  __DATA.__data: 0x188
   __DATA.__bss: 0x310
   __DATA_DIRTY.__objc_data: 0x218
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__common: 0x8
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore
+  - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 865
-  Symbols:   354
-  CStrings:  81
+  Functions: 875
+  Symbols:   384
+  CStrings:  87
 
Symbols:
+ +[CSCloudSharing isManagedAppleAccountOwnerForFileOrFolderURL:]
+ +[CSCloudSharing isManagedAppleAccountOwnerForShare:containerSetupInfo:]
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_BRAccountDescriptor
+ __CLASS_METHODS__TtC12CloudSharing15InitiateSharing
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_CloudSharing
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_CloudSharing
+ _objc_msgSend$aa_appleAccountWithAltDSID:
+ _objc_msgSend$aa_appleAccountWithUsername:
+ _objc_msgSend$aa_isManagedAppleID
+ _objc_msgSend$accountDescriptorForURL:mustBeLoggedIn:
+ _objc_msgSend$accountID
+ _objc_msgSend$accountIdentifier
+ _objc_msgSend$accountOverrideInfo
+ _objc_msgSend$accountWithIdentifier:
+ _objc_msgSend$altDSID
+ _objc_msgSend$defaultStore
+ _objc_msgSend$emailAddress
+ _objc_msgSend$isManagedAppleAccountOwnerForFileOrFolderURL:
+ _objc_msgSend$isManagedAppleAccountOwnerForShare:containerSetupInfo:
+ _objc_msgSend$lookupInfo
+ _objc_msgSend$owner
+ _objc_msgSend$phoneNumber
+ _objc_msgSend$userIdentity
+ _objc_retain_x2
+ _swift_arrayInitWithCopy
+ _symbolic SSSg
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
CStrings:
+ "containerOverride.accountID"
+ "containerOverride.altDSID"
+ "isManagedAppleAccountOwner: %{bool}d (source: %s, accountResolved: %{bool}d)"
+ "isManagedAppleAccountOwner: false (source: containerOverride, no accountID or altDSID)"
+ "isManagedAppleAccountOwner: false (source: none, no owner handle or container override)"
+ "isManagedAppleAccountOwner: owner handle not resolvable on device; trying container override"
```
