## PDS

> `/System/Library/PrivateFrameworks/PDS.framework/Versions/A/PDS`

```diff

-1926.400.131.1.1
-  __TEXT.__text: 0x8710
+1926.500.181.0.0
+  __TEXT.__text: 0x90d0
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0x620
+  __TEXT.__objc_methlist: 0x8b4
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x44d
-  __TEXT.__gcc_except_tab: 0x5c4
+  __TEXT.__gcc_except_tab: 0x584
   __TEXT.__oslogstring: 0xa1a
-  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__unwind_info: 0x2d8
   __TEXT.__objc_classname: 0x10d
   __TEXT.__objc_methname: 0x133c
   __TEXT.__objc_methtype: 0x70c

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_selrefs: 0x500
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x128
   __AUTH_CONST.__const: 0x270
   __AUTH_CONST.__cfstring: 0x560
-  __AUTH_CONST.__objc_const: 0x1560
+  __AUTH_CONST.__objc_const: 0x10d0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x58
   __DATA.__data: 0x3e8

   - /System/Library/PrivateFrameworks/IMFoundation.framework/Versions/A/IMFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25B85386-E453-3EDC-8B6D-A3F7A967BD62
-  Functions: 186
-  Symbols:   536
+  UUID: 5EF72364-4D4C-39B3-BFE0-746FB2F4D016
+  Functions: 228
+  Symbols:   580
   CStrings:  440
 
Symbols:
+ +[PDSRemoteRegistry remoteVendorForClientID:].cold.1
+ +[PDSUser userWithDSID:].cold.1
+ -[PDSEntry entryWithUpdatedState:].cold.1
+ -[PDSEntry initWithUser:registration:clientID:state:].cold.1
+ -[PDSEntry initWithUser:registration:clientID:state:].cold.2
+ -[PDSEntry initWithUser:registration:clientID:state:].cold.3
+ -[PDSEntry initWithUser:registration:clientID:state:].cold.4
+ -[PDSRegistrar activeUsersWithCompletion:].cold.1
+ -[PDSRegistrar addRegistration:toUser:error:].cold.1
+ -[PDSRegistrar addRegistration:toUser:error:].cold.2
+ -[PDSRegistrar allEntriesWithCompletion:].cold.1
+ -[PDSRegistrar allRegistrationsForUser:completion:].cold.1
+ -[PDSRegistrar allRegistrationsForUser:completion:].cold.2
+ -[PDSRegistrar allRegistrationsForUser:error:].cold.1
+ -[PDSRegistrar allRegistrationsWithCompletion:].cold.1
+ -[PDSRegistrar batchUpdateRegistrations:forUser:error:].cold.1
+ -[PDSRegistrar batchUpdateRegistrations:forUser:error:].cold.2
+ -[PDSRegistrar currentRegistrationsForUser:completion:].cold.1
+ -[PDSRegistrar currentRegistrationsForUser:completion:].cold.2
+ -[PDSRegistrar currentRegistrationsForUser:error:].cold.1
+ -[PDSRegistrar deleteRegistration:fromUser:error:].cold.1
+ -[PDSRegistrar deleteRegistration:fromUser:error:].cold.2
+ -[PDSRegistrar ensureRegistrationPresent:forUser:error:].cold.1
+ -[PDSRegistrar ensureRegistrationPresent:forUser:error:].cold.2
+ -[PDSRegistrar initWithClientID:error:].cold.1
+ -[PDSRegistrar removeAllRegistrationsFromUser:error:].cold.1
+ -[PDSRegistrar removeRegistration:fromUser:error:].cold.1
+ -[PDSRegistrar removeRegistration:fromUser:error:].cold.2
+ -[PDSRegistrar usersWithCompletion:].cold.1
+ -[PDSRegistration initWithTopic:qualifier:pushEnvironment:].cold.1
+ -[PDSRegistration initWithTopic:qualifier:pushEnvironment:].cold.2
+ -[PDSRegistration initWithTopic:qualifier:pushEnvironment:].cold.3
+ -[PDSUser initWithUserID:userType:].cold.1
+ -[PDSUser initWithUserID:userType:].cold.2
+ -[PDSXPCConnector initWithClientID:interfaceVendor:connectionVendor:].cold.1
+ -[PDSXPCConnector initWithClientID:interfaceVendor:connectionVendor:].cold.2
+ -[PDSXPCConnector initWithClientID:interfaceVendor:connectionVendor:].cold.3
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ pds_defaultLog.cold.1
+ pds_oversizedLog.cold.1
+ pds_serverBagLog.cold.1

```
