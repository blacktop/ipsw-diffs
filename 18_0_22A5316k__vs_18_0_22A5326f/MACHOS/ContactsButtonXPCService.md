## ContactsButtonXPCService

> `/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService`

```diff

-1264.0.0.0.0
-  __TEXT.__text: 0x1c6a0
-  __TEXT.__auth_stubs: 0x13b0
+1267.0.0.0.0
+  __TEXT.__text: 0x1b748
+  __TEXT.__auth_stubs: 0x1290
   __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0x752
-  __TEXT.__objc_methname: 0xb53
-  __TEXT.__oslogstring: 0x1627
+  __TEXT.__const: 0x722
+  __TEXT.__objc_methname: 0xbc6
+  __TEXT.__oslogstring: 0x1597
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x1434
-  __TEXT.__constg_swiftt: 0x880
-  __TEXT.__swift5_typeref: 0x1507
-  __TEXT.__swift5_reflstr: 0x523
-  __TEXT.__swift5_fieldmd: 0x4b4
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0x4c
+  __TEXT.__cstring: 0x13e4
+  __TEXT.__constg_swiftt: 0x860
+  __TEXT.__swift5_typeref: 0x15c4
+  __TEXT.__swift5_reflstr: 0x533
+  __TEXT.__swift5_fieldmd: 0x4d8
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift5_types: 0x48
   __TEXT.__objc_classname: 0x8a
   __TEXT.__objc_methtype: 0x286
-  __TEXT.__swift5_capture: 0x15c
-  __TEXT.__unwind_info: 0x4b8
-  __TEXT.__eh_frame: 0x400
-  __DATA_CONST.__auth_got: 0x9d8
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__auth_ptr: 0x308
-  __DATA_CONST.__const: 0x8d0
+  __TEXT.__swift5_capture: 0x134
+  __TEXT.__unwind_info: 0x498
+  __TEXT.__eh_frame: 0x3d0
+  __DATA_CONST.__auth_got: 0x948
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__auth_ptr: 0x2e8
+  __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA.__objc_const: 0x1000
-  __DATA.__objc_selrefs: 0x348
-  __DATA.__objc_data: 0xa20
-  __DATA.__data: 0xbc0
-  __DATA.__common: 0x98
-  __DATA.__bss: 0x4a8
+  __DATA.__objc_const: 0x1020
+  __DATA.__objc_selrefs: 0x370
+  __DATA.__objc_data: 0xa28
+  __DATA.__data: 0xbf0
+  __DATA.__common: 0xa8
+  __DATA.__bss: 0x428
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/EmailCore.framework/EmailCore
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/RenderBox.framework/RenderBox
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
-  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 354
-  Symbols:   216
-  CStrings:  409
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 344
+  Symbols:   209
+  CStrings:  412
 
Symbols:
+ _OBJC_CLASS_$_CNAuditToken
+ _OBJC_CLASS_$_CNAuthorizationContext
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x9
- _OBJC_CLASS_$_BSAuditToken
- _OBJC_CLASS_$_BSProcessHandle
- _dispatch_semaphore_create
- _kTCCServiceAddressBook
- _tcc_authorization_record_get_authorization_right
- _tcc_authorization_record_get_subject_identity
- _tcc_credential_create_data_from_process_with_audit_token
- _tcc_identity_create
- _tcc_identity_get_identifier
- _tcc_identity_get_type
- _tcc_message_options_create
- _tcc_message_options_set_nokill_policy
- _tcc_message_options_set_reply_handler_policy
- _tcc_message_options_set_request_prompt_policy
- _tcc_server_create
- _tcc_server_message_get_authorization_records_by_service
- _tcc_server_message_set_authorization_value
- _tcc_service_singleton_for_CF_name
CStrings:
+ "#ContactsButton avatarWidth: %!f(MISSING) buttonWidth: %!f(MISSING) buttonHeight: %!f(MISSING) trailingEdgeFromAvatar: %!f(MISSING)"
+ "#ContactsButton new context auth state is refreshed to  %!l(MISSING)d"
+ "#ContactsButton user allowed limited access, updated access to be %!l(MISSING)d"
+ "#ContactsButton user declined limited access, updated access to be %!l(MISSING)d"
+ "#ContactsButton will bring up library management UI? authorization right is %!l(MISSING)d"
+ "auditToken:"
+ "authContext"
+ "authorizationStatus"
+ "clientBundleIdentifier"
+ "cnAuditToken"
+ "initWithAuditToken:assumedIdentity:"
+ "isAccessDenied"
+ "isAccessUnknown"
+ "isLimitedAccessGranted"
+ "resetCachedStatus"
+ "setAuthorizationStatus:forBundleIdentifier:noKillApp:"
- "#ContactsButton avatarWidth: %!f(MISSING) avatarPadding: %!f(MISSING) buttonWidth: %!f(MISSING) buttonHeight: %!f(MISSING) trailingEdgeFromAvatar: %!f(MISSING)"
- "#ContactsButton got an authorization record of %!l(MISSING)lu for %!s(MISSING)"
- "#ContactsButton no ID for app at %!s(MISSING)?"
- "#ContactsButton unable to create LSApplicationRecord for %!s(MISSING): %!@(MISSING)"
- "#ContactsButton user allowed limited access, updated access to be %!l(MISSING)lu"
- "#ContactsButton user declined limited access, updated access to be %!l(MISSING)lu"
- "#ContactsButton will bring up library management UI? authorization right is %!l(MISSING)lu"
- "bundleIdentifier"
- "cachedAuthStatus"
- "initWithURL:allowPlaceholder:error:"
- "processHandleForAuditToken:"
- "tokenFromAuditToken:"
- "v24@?0@\"<OS_tcc_authorization_record>\"8^{__CFError=}16"

```
