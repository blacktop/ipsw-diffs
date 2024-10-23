## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-80.200.41.0.0
-  __TEXT.__text: 0xb5c04
+80.300.121.0.0
+  __TEXT.__text: 0xb5d2c
   __TEXT.__auth_stubs: 0x17d0
-  __TEXT.__objc_methlist: 0x62f0
+  __TEXT.__objc_methlist: 0x62f8
   __TEXT.__const: 0x694
-  __TEXT.__cstring: 0x2eea
-  __TEXT.__oslogstring: 0x1011d
+  __TEXT.__cstring: 0x2f6a
+  __TEXT.__oslogstring: 0x1025d
   __TEXT.__gcc_except_tab: 0xd04
   __TEXT.__swift5_typeref: 0x8f4
   __TEXT.__swift5_capture: 0x1c0

   __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1ff8
+  __TEXT.__unwind_info: 0x2000
   __TEXT.__eh_frame: 0x1110
   __TEXT.__objc_classname: 0xe00
-  __TEXT.__objc_methname: 0xfaed
-  __TEXT.__objc_methtype: 0x43df
+  __TEXT.__objc_methname: 0xfb00
+  __TEXT.__objc_methtype: 0x43ea
   __TEXT.__objc_stubs: 0x8d40
   __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x1a08
+  __DATA_CONST.__const: 0x1a30
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x158

   __AUTH_CONST.__auth_got: 0xbf8
   __AUTH_CONST.__auth_ptr: 0x1c8
   __AUTH_CONST.__const: 0xe18
-  __AUTH_CONST.__cfstring: 0x22e0
+  __AUTH_CONST.__cfstring: 0x2340
   __AUTH_CONST.__objc_const: 0xfae0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3386
-  Symbols:   3602
-  CStrings:  4000
+  Functions: 3387
+  Symbols:   3603
+  CStrings:  4008
 
CStrings:
+ "%!@(MISSING) notification received: endDate = %!@(MISSING)"
+ "@24@0:8q16"
+ "Channel was rolled successfully."
+ "Client is currently rate-limited.  Enqueuing requests as pending publish."
+ "Create channel response contains non success status: %!l(MISSING)d - %!@(MISSING)"
+ "Decrypted payload: %!@(MISSING)"
+ "Error encountered during key roll for statusTypeIdentifier: %!@(MISSING) error: %!@(MISSING)"
+ "Invitation revocation for all handles completed successfully"
+ "Invitation revocation for handles %!@(MISSING) completed successfully"
+ "Invitation was not sent for handles %!@(MISSING) due to key roll error: %!@(MISSING)"
+ "NSPersistentCloudKitContainerEventTypeExport"
+ "NSPersistentCloudKitContainerEventTypeImport"
+ "NSPersistentCloudKitContainerEventTypeSetup"
+ "Our current checkpoint matches the update's checkpoint.  We're up to date -- dropping"
+ "Pending publish request has already been scheduled.  Not enqueuing again"
+ "Polling for current state as we've migrated channels"
+ "Status Publish Request has been rate-limited"
+ "Status payload decrypted to nil data"
+ "Status payload not decrypted from generatedKey: %!@(MISSING)"
+ "Status payload successfully decrypted from generatedKey: %!@(MISSING)"
+ "Status payload successfully decrypted from invitation: %!@(MISSING)"
+ "StatusKitAgent was previously subscribed to: %!@(MISSING)"
+ "Successfully added presence assertion to in memory model for presence identifier: %!@(MISSING) options: %!@(MISSING)"
+ "Successfully removed presence assertion for identifier: %!@(MISSING). Client had %!l(MISSING)d presence assertions, now has %!l(MISSING)d. Client: %!@(MISSING)"
+ "Successfully removed presence subscription assertion for identifier: %!@(MISSING). Client had %!l(MISSING)d transient subscription assertions, now has %!l(MISSING)d. Client: %!@(MISSING)"
+ "Successfully removed present devices for identifier: %!@(MISSING). Channel had %!l(MISSING)d presence assertions, now has %!l(MISSING)d"
+ "Successfully removed transient subscription assertion for identifier: %!@(MISSING). Client had %!l(MISSING)d transient subscription assertions, now has %!l(MISSING)d. Client: %!@(MISSING)"
+ "Successfully rolled personal channel with statusTypeIdentifier: %!@(MISSING)"
+ "Successfully rolled presence channel with presenceIdentifier: %!@(MISSING)"
+ "We found an existing invited user matching the requested user, but that invitation was sent with handle %!@(MISSING) instead of handle %!@(MISSING). Ignoring."
+ "_persistentCloudKitContainerEventTypeToString:"
- "Channel was rolled succesfully."
- "Client is currently rate-limited.  Enqueing requests as pending publish."
- "Create channle response contains non success status: %!l(MISSING)d - %!@(MISSING)"
- "Decrypteded payload: %!@(MISSING)"
- "Error encounted during key roll for statusTypeIdentifier: %!@(MISSING) error: %!@(MISSING)"
- "Inivtation was not sent for handles %!@(MISSING) due to key roll error: %!@(MISSING)"
- "Invitation revocation for all handles completed succesffully"
- "Invitation revocation for handles %!@(MISSING) completed succesffully"
- "Pending publish request has already been scheduled.  Not enqueing again"
- "Status Publish Request has been rate-limtited"
- "Status payload decypted to nil data"
- "Status payload not decrypteded from generatedKey: %!@(MISSING)"
- "Status payload successfully decrypteded from generatedKey: %!@(MISSING)"
- "Status payload successfully decrypteded from invitation: %!@(MISSING)"
- "StatusKitAgent was previously subscriped to: %!@(MISSING)"
- "Succesfully removed presence assertion for identifier: %!@(MISSING). Client had %!l(MISSING)d presence assertions, now has %!l(MISSING)d. Client: %!@(MISSING)"
- "Succesfully removed presence subscription assertion for identifier: %!@(MISSING). Client had %!l(MISSING)d transient subscription assertions, now has %!l(MISSING)d. Client: %!@(MISSING)"
- "Succesfully removed present devices for identifier: %!@(MISSING). Channel had %!l(MISSING)d presence assertions, now has %!l(MISSING)d"
- "Succesfully removed transient subscription assertion for identifier: %!@(MISSING). Client had %!l(MISSING)d transient subscription assertions, now has %!l(MISSING)d. Client: %!@(MISSING)"
- "Succesfully rolled personal channel with statusTypeIdentifier: %!@(MISSING)"
- "Succesfully rolled presence channel with presenceIdentifier: %!@(MISSING)"
- "Successfully added presence assertion to in memory model for presennce identifier: %!@(MISSING) options: %!@(MISSING)"
- "removeObserver:name:object:"

```
