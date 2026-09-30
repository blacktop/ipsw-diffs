## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeCore`

```diff

-527.400.0.0.0
-  __TEXT.__text: 0x8cb98
+529.2.0.0.0
+  __TEXT.__text: 0x8f508
   __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x6330
+  __TEXT.__objc_methlist: 0x6440
   __TEXT.__const: 0x308
-  __TEXT.__cstring: 0x6b02
+  __TEXT.__cstring: 0x7052
   __TEXT.__oslogstring: 0x769c
-  __TEXT.__gcc_except_tab: 0x1b98
+  __TEXT.__gcc_except_tab: 0x1ba4
   __TEXT.__swift5_typeref: 0x14c
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_fieldmd: 0xbc

   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_reflstr: 0xa2
-  __TEXT.__unwind_info: 0x1e10
+  __TEXT.__unwind_info: 0x1e50
   __TEXT.__eh_frame: 0x318
   __TEXT.__objc_classname: 0x1671
-  __TEXT.__objc_methname: 0x13316
+  __TEXT.__objc_methname: 0x1347e
   __TEXT.__objc_methtype: 0x1f6f
-  __TEXT.__objc_stubs: 0xbea0
+  __TEXT.__objc_stubs: 0xc080
   __DATA_CONST.__got: 0x9c8
   __DATA_CONST.__const: 0x710
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3df8
+  __DATA_CONST.__objc_selrefs: 0x3e70
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3e8
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x250
   __AUTH_CONST.__auth_got: 0x660
   __AUTH_CONST.__auth_ptr: 0xa8
   __AUTH_CONST.__const: 0x1a60
-  __AUTH_CONST.__cfstring: 0x7680
+  __AUTH_CONST.__cfstring: 0x79e0
   __AUTH_CONST.__objc_const: 0xf280
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x180

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2974
-  Symbols:   7187
-  CStrings:  1070
+  Functions: 2998
+  Symbols:   7226
+  CStrings:  1097
 
Symbols:
+ -[STCoreDevice _validateLocalDevice:]
+ -[STCoreDevice _validateNumberOfLocalDevices:]
+ -[STCoreDevice _validateRemoteDevice:]
+ -[STCoreDevice _validateUniqueIdentifier:]
+ -[STCoreDevice _validateUserDeviceStates:]
+ -[STCoreDevice validateForDelete:]
+ -[STCoreDevice validateForInsert:]
+ -[STCoreDevice validateForUpdate:]
+ -[STCoreUser(Identifiers) _validateAltDSID:]
+ -[STCoreUser(Identifiers) _validateAppleID:]
+ -[STCoreUser(Identifiers) _validateDSID:]
+ -[STCoreUser(Identifiers) _validateLocalUser:]
+ -[STCoreUser(Identifiers) _validateNumberOfLocalUsers:]
+ -[STCoreUser(Identifiers) _validateRemoteUser:]
+ -[STCoreUser(Identifiers) validateForDelete:]
+ -[STCoreUser(Identifiers) validateForInsert:]
+ -[STCoreUser(Identifiers) validateForUpdate:]
+ -[STUserDeviceState _validateCoreDuetIdentifier:]
+ -[STUserDeviceState _validateLocalUserDeviceState:]
+ -[STUserDeviceState _validateNumberOfLocalUserDeviceStates:]
+ -[STUserDeviceState validateForDelete:]
+ -[STUserDeviceState validateForInsert:]
+ -[STUserDeviceState validateForUpdate:]
+ __54-[STAdminPersistenceController performBackgroundTask:]_block_invoke.13
+ __62-[STAskServiceClient sendAskForTimeRequest:completionHandler:]_block_invoke.33
+ __76-[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]_block_invoke.34
+ __76-[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]_block_invoke.34.cold.1
+ _objc_msgSend$_validateAltDSID:
+ _objc_msgSend$_validateAppleID:
+ _objc_msgSend$_validateCoreDuetIdentifier:
+ _objc_msgSend$_validateDSID:
+ _objc_msgSend$_validateLocalDevice:
+ _objc_msgSend$_validateLocalUser:
+ _objc_msgSend$_validateLocalUserDeviceState:
+ _objc_msgSend$_validateNumberOfLocalDevices:
+ _objc_msgSend$_validateNumberOfLocalUserDeviceStates:
+ _objc_msgSend$_validateNumberOfLocalUsers:
+ _objc_msgSend$_validateRemoteDevice:
+ _objc_msgSend$_validateRemoteUser:
+ _objc_msgSend$_validateUniqueIdentifier:
+ _objc_msgSend$_validateUserDeviceStates:
+ _objc_msgSend$intValue
- __54-[STAdminPersistenceController performBackgroundTask:]_block_invoke.20
- __76-[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]_block_invoke.33
- __76-[STAskServiceClient respondToAskForTimeRequestWithIdentifier:answer:error:]_block_invoke.33.cold.1
CStrings:
+ "%!K(MISSING) != NULL OR %!K(MISSING) != NULL"
+ "A local device must have the UUID of the local device."
+ "A local device must match the platform of the current device."
+ "A local user must have Cloud Settings."
+ "A local user who is a child, teen, nor non-parent adult must have family settings."
+ "A remote device must have a valid platform."
+ "A remote user must be family member.."
+ "A remote user must have Family Settings."
+ "All devices must have at least 1 user device state."
+ "If the user has a DSID, they must have an altDSID."
+ "If the user has an Apple ID, they must have a DSID."
+ "The local device must match the device of the UserDeviceState."
+ "The local user must match the user of the UserDeviceState."
+ "The localUserDeviceState of a local device MUST be in the device's userDeviceState."
+ "There are multiple users with the same Apple ID."
+ "There are multiple users with the same DSID."
+ "There are multiple users with the same altDSID."
+ "There must be a CoreDuet identifier for UserDeviceStates."
+ "There must be a local user device state."
+ "There must be at least one local user object."
+ "There must be local device (with localUserDeviceState)."
+ "There must be one and only device with a given UUID."
+ "There must be one and only device with localUserDeviceState."
+ "There must be one and only local UserDeviceState."
+ "There must be one and only one local user object."
+ "There must be one and only one local user."
+ "There must be one local user."
+ "altDSID"
+ "cannot fetch or create Local User Device state with simplified agent"
+ "localDevice"
- "No local user found in the database"
- "Persistent Store not loaded"
- "The persistent store failed to load"

```
