## ActivitySharingServices

> `/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices`

```diff

-813.0.0.0.0
-  __TEXT.__text: 0x11ca5c
-  __TEXT.__auth_stubs: 0x1e20
-  __TEXT.__objc_methlist: 0x344
-  __TEXT.__const: 0x4d18
-  __TEXT.__cstring: 0x41de
-  __TEXT.__swift5_typeref: 0x3014
-  __TEXT.__swift5_fieldmd: 0x2a64
-  __TEXT.__constg_swiftt: 0x273c
-  __TEXT.__oslogstring: 0x5178
+819.0.0.0.0
+  __TEXT.__text: 0x124ea0
+  __TEXT.__auth_stubs: 0x1e30
+  __TEXT.__objc_methlist: 0x354
+  __TEXT.__const: 0x4d28
+  __TEXT.__cstring: 0x434e
+  __TEXT.__swift5_typeref: 0x3020
+  __TEXT.__swift5_fieldmd: 0x2ab8
+  __TEXT.__constg_swiftt: 0x2764
+  __TEXT.__oslogstring: 0x53b8
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x3d74
+  __TEXT.__swift5_reflstr: 0x3e14
   __TEXT.__swift5_assocty: 0x210
   __TEXT.__swift5_protos: 0x130
   __TEXT.__swift5_proto: 0x318
   __TEXT.__swift5_types: 0x234
-  __TEXT.__swift5_capture: 0x1758
+  __TEXT.__swift5_capture: 0x1998
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x5ac0
-  __TEXT.__eh_frame: 0x125b8
+  __TEXT.__unwind_info: 0x5a50
+  __TEXT.__eh_frame: 0x12ed8
   __TEXT.__objc_classname: 0x1b9
-  __TEXT.__objc_methname: 0x38a5
-  __TEXT.__objc_methtype: 0x11aa
+  __TEXT.__objc_methname: 0x3923
+  __TEXT.__objc_methtype: 0x11fe
   __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__const: 0x9b8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba0
+  __DATA_CONST.__objc_selrefs: 0xbb0
   __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0xf10
-  __AUTH_CONST.__auth_ptr: 0x1138
-  __AUTH_CONST.__const: 0x7448
-  __AUTH_CONST.__objc_const: 0x59c8
+  __AUTH_CONST.__auth_got: 0xf18
+  __AUTH_CONST.__auth_ptr: 0x1160
+  __AUTH_CONST.__const: 0x78a8
+  __AUTH_CONST.__objc_const: 0x5a48
   __AUTH.__objc_data: 0x318
-  __AUTH.__data: 0x858
-  __DATA.__data: 0x29e0
-  __DATA.__bss: 0x3080
+  __AUTH.__data: 0x798
+  __DATA.__data: 0x2990
+  __DATA.__bss: 0x2e00
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x650
-  __DATA_DIRTY.__data: 0xee0
+  __DATA_DIRTY.__objc_data: 0x658
+  __DATA_DIRTY.__data: 0x1138
   __DATA_DIRTY.__common: 0x48
-  __DATA_DIRTY.__bss: 0x700
+  __DATA_DIRTY.__bss: 0x980
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
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
-  Functions: 4530
-  Symbols:   450
-  CStrings:  1287
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4706
+  Symbols:   462
+  CStrings:  1307
 
Symbols:
+ _IDSSendMessageOptionFromIDKey
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _ASSaveRelationshipRecordForContact
CStrings:
+ "Added item to map %!s(MISSING)"
+ "Added items to map %!s(MISSING)"
+ "Failed to fix up legacy relationships: %!@(MISSING)"
+ "Failed to fix up secure cloud relationships: %!@(MISSING)"
+ "Fixed up %!l(MISSING)d legacy relationships for migration"
+ "Fixed up secure cloud relationships for downgrade"
+ "Found contacts already waiting on downgrade: %!s(MISSING), new requests %!s(MISSING)"
+ "Found legacy relationship to fix up for migration: %!@(MISSING)"
+ "Found secure cloud relationship to fix up for downgrade: %!@(MISSING)"
+ "No contacts to downgrade"
+ "No contacts to fix up downgrade"
+ "No legacy relationships to fix up for migration"
+ "No secure cloud relationships to fix up for downgrade"
+ "Pushed legacy relationships after deleting zones: %!s(MISSING)"
+ "Remote relationship is marked upgraded, marking local as failed to reset state"
+ "Running migration service with devices: %!s(MISSING), ignore %!{(MISSING)bool}d, ids %!s(MISSING)"
+ "SecureCloudUpgradeSkipTieBreaker"
+ "Sent request to upgrade relationship: %!@(MISSING) from: %!s(MISSING)"
+ "Using migration available items: %!s(MISSING)"
+ "activity-sharing-invite"
+ "asyncLock"
+ "competitionManager(_:delete:group:)"
+ "competitionManager:deleteCompetitionLists:group:completion:"
+ "fixUpLegacyRelationships(contacts:)"
+ "fixUpSecureCloudRelationships()"
+ "handleSavedRecords:forContact:completion:"
+ "relationshipInviteAcceptService"
+ "relationshipManager:acceptedInviteForFriend:completion:"
+ "secureCloudReady"
+ "sendInvitationToDestination(_:payload:transportItem:fromAddress:)"
+ "sendInvitationToDestination:expirationDate:context:options:serverAcknowledgedBlock:"
+ "v48@0:8@\"ASCompetitionManager\"16@\"NSSet\"24@\"CKOperationGroup\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"ASCompetitionManager\"16@\"NSSet\"24@\"CKOperationGroup\"32@?<v@?B@\"NSError\">40"
- "Marked secure cloud relationship as failed: %!@(MISSING)"
- "Pushed relationship for repair %!@(MISSING)"
- "Pushed secure cloud relationship for repair %!@(MISSING)"
- "Repairing contact: %!@(MISSING)"
- "Repairing secure cloud relationship failed with error: %!@(MISSING), relationship: %!@(MISSING)"
- "Sent repair request to relationship %!@(MISSING)"
- "Sent request to upgrade relationship: %!@(MISSING)"
- "Unable to repair relationship, missing CloudKit address: %!@(MISSING)"
- "activity-sharing-temp"
- "additionalLegacyZoneIDs"
- "sendInvitationToDestination(_:payload:transportItem:)"
- "sendInvitationToDestination:expirationDate:context:serverAcknowledgedBlock:"
- "supportsMigrationAvailableRecord"

```
