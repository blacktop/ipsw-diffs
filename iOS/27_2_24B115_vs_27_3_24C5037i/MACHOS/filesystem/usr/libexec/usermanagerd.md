## usermanagerd

> `/usr/libexec/usermanagerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`

```diff

-490.0.3.0.0
-  __TEXT.__text: 0xad160
-  __TEXT.__auth_stubs: 0x18d0
-  __TEXT.__objc_stubs: 0x22e0
-  __TEXT.__objc_methlist: 0x1a78
-  __TEXT.__const: 0x1554
-  __TEXT.__gcc_except_tab: 0x161c
-  __TEXT.__cstring: 0x76d7
-  __TEXT.__objc_classname: 0x37a
-  __TEXT.__objc_methname: 0x396d
-  __TEXT.__objc_methtype: 0x14ab
-  __TEXT.__oslogstring: 0x12070
-  __TEXT.__unwind_info: 0x1cb8
-  __DATA_CONST.__const: 0x27e8
-  __DATA_CONST.__cfstring: 0x1d60
-  __DATA_CONST.__objc_classlist: 0x100
+490.60.1.0.0
+  __TEXT.__text: 0xad59c
+  __TEXT.__auth_stubs: 0x18b0
+  __TEXT.__objc_stubs: 0x2440
+  __TEXT.__objc_methlist: 0x1b48
+  __TEXT.__const: 0x1564
+  __TEXT.__gcc_except_tab: 0x157c
+  __TEXT.__cstring: 0x7651
+  __TEXT.__objc_classname: 0x38b
+  __TEXT.__objc_methname: 0x3b23
+  __TEXT.__objc_methtype: 0x15be
+  __TEXT.__oslogstring: 0x124b7
+  __TEXT.__unwind_info: 0x1ce8
+  __DATA_CONST.__const: 0x27f8
+  __DATA_CONST.__cfstring: 0x1dc0
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0xc78
-  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__auth_got: 0xc68
+  __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA.__objc_const: 0x46c8
-  __DATA.__objc_selrefs: 0xd10
-  __DATA.__objc_ivar: 0x1e4
-  __DATA.__objc_data: 0xa00
-  __DATA.__data: 0x1340
-  __DATA.__common: 0xb0
+  __DATA.__objc_const: 0x47c0
+  __DATA.__objc_selrefs: 0xd60
+  __DATA.__objc_ivar: 0x1e8
+  __DATA.__objc_data: 0xa50
+  __DATA.__data: 0x1358
+  __DATA.__common: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 2404
+  Functions: 2496
   Symbols:   469
-  CStrings:  3392
+  CStrings:  3430
 
Symbols:
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
- _CFDateGetTypeID
- _perror
CStrings:
+ "-[UMDUserManager createUserWithOptions:passcode:passcodeSize:guestRefresh:error:]"
+ "-[UMDUserManager removeUser:]"
+ "-[UMDUserManager setUserAttributes:]"
+ "APFSIOC_GET_DIR_STATS failed for uid:%d"
+ "AUTHGUESTUSER"
+ "Adding disabled Clean User with uid:%d to the Array to be returned"
+ "Already in switch or refreshToUser, ignore current one: session type is:%d"
+ "Authenticated Guest User mode create User"
+ "Authenticated Guest mode, already another user.."
+ "Authenticted Guest User refresh with current user %d, Creating new one and switching to that"
+ "CALLING Deletion of Disabled Session after bubble"
+ "CHECKING DISABLED GUEST USERS TO DELETE"
+ "Cannot alter provision to authenticated guest as Users are present, remove them to change quota"
+ "Checking user cleanup from daemon start"
+ "Cleared kUMUserSessionHasSyncBagKey for uid %u"
+ "Clearing SyncBag if not needed for uid %u"
+ "Could not create a new user, switch to loginUser, i.e do a logout"
+ "Created SyncBag for uid %u"
+ "Created and Loaded User Session with ID %d"
+ "Created keybag for uid %u"
+ "Created new user awith uid %d and switching to that"
+ "Creating User with Name %@"
+ "Creating fully shared volume"
+ "Creating sized volume"
+ "Creating the  authenticated guest user to replace existing one"
+ "Creating the first authenticated guest user"
+ "Deleting Disabled  users..."
+ "Deleting disabled Guest User with uid:%d"
+ "Device Not provisioned for Authenticated Guest User, return ENOTSUP"
+ "Device Not sharedIPad or provisioned for Guest User, return ENOTSUP"
+ "Device already provisioned to be sharedIPad, verifying if we can change to Authenticated GuestMode"
+ "DeviceClass"
+ "Error: setAttributeOfClass: incorrect type for key %@: expected %@, got %@"
+ "FAILED as this User already exists,  cannot add another one"
+ "FOUND %d Disabled and Clean Users"
+ "Failed to allocate NSNUmber"
+ "Failed to delete User with uid:%d"
+ "Failed to load AKS identity for uid %u, bailing"
+ "Failed to remove SyncBag for uid %u: %d"
+ "Failed to unload AKS identity for uid %u"
+ "Failed to unload SyncBag for uid %u: %{mach.errno}d"
+ "File Layout Set"
+ "Finding disabled but clean Users"
+ "In Temporary user login, see if any disabled and clean users for deletion"
+ "In allUserIDs"
+ "In provisioningStatusWithReply:"
+ "Invalid configuration for reprovisioning"
+ "Legacy mode create User"
+ "Loaded AKS identity for uid %u"
+ "Loaded keybag for uid %u"
+ "MKBUserSessionAuthenticatedGuestUser"
+ "MKBUserSessionCreateKeybagForUser(%u) failed: %{darwin.errno}d"
+ "MKBUserSessionCreateSyncBagForUser(%u) failed: %d"
+ "MKBUserSessionLoadKeybagForUser(%u) failed: %{darwin.errno}d"
+ "MKBUserSessionSetVolumeToPersona(%{public}@, %{public}@) failed: %{darwin.errno}d"
+ "MKBUserSessionUnloadKeybagForUser(%u) failed: %{mach.errno}d"
+ "Moving Along with Refresh  Auntenticated GuestUser"
+ "No Disabled users found to delete, returning"
+ "No SyncBag to remove for loginwindow"
+ "No sync bubble content for Authenticated Guest User, removing if anything is set.."
+ "No users, changing to Authenticated GuestMode"
+ "Not in Shared iPad, Provisioning a Quotaless user Shared iPad device"
+ "Removed SyncBag for uid %u"
+ "Shared iPad Mode"
+ "Shared iPad Mode with userquota size"
+ "Skipping loginUI  uid:%d"
+ "Successfully deleted User with uid:%d"
+ "Successfully deleted the user:%d"
+ "SyncBag exists for uid %u, skipping creation"
+ "UMDDeviceManager"
+ "USRSwitchNow: Marking oldSession as DISABLED"
+ "USRSwitchNow: Removing disabled users if available"
+ "Unable to delete the user:%d"
+ "Unloaded AKS identity for uid %u"
+ "Unloaded SyncBag for uid %u"
+ "Unloaded keybag for uid %u"
+ "User Does not EXIST, Create the user first.."
+ "User with uid:%d is Disabled"
+ "User with uid:%d is NOT disabled so not added to the list"
+ "UserManagement early boot task failed assertion: _gPersonaManager == ((void*)0)"
+ "UserManagement loading foreground user failed assertion: [_gUserManager userWithUID:uid] != ((void*)0)"
+ "UserManagement user switch failed assertion: _gPersonaManager == ((void*)0)"
+ "UserQuota sized users mode: Creating user"
+ "UserSessionEducationAuthenticatedGuest"
+ "attemptSyncBagRemovalForSession:uid:splitUserVolumeEnabled:"
+ "createKeybagForSession:uid:passcode:gracePeriodInSecs:opaqueStuff:"
+ "createSyncBagForSession:uid:"
+ "i28@0:8@\"NSMutableDictionary\"16I24"
+ "i28@0:8@16I24"
+ "i32@0:8@\"NSMutableDictionary\"16I24B28"
+ "i32@0:8@16I24B28"
+ "i36@0:8@\"NSMutableDictionary\"16I24B28B32"
+ "i36@0:8@16I24B28B32"
+ "i48@0:8@\"NSMutableDictionary\"16I24@\"NSData\"28B36i40B44"
+ "i48@0:8@\"NSMutableDictionary\"16I24@\"NSData\"28i36@\"NSData\"40"
+ "i48@0:8@16I24@28B36i40B44"
+ "i48@0:8@16I24@28i36@40"
+ "iPhone"
+ "in No Quota User Mode with current user %d, Creating new one and switching to that"
+ "in refreshGuestUser"
+ "loadKeybagForSession:uid:passcode:setGracePeriod:gracePeriodInSecs:earlyStart:"
+ "loadSyncBagForSession:uid:splitUserVolumeEnabled:"
+ "numberWithLongLong:"
+ "provisioningStatusWithReply:"
+ "refreshGuestUserWithPID:completionHandler:"
+ "removeObjectAtIndex:"
+ "removeSyncBagForSession:uid:doUnload:splitUserVolumeEnabled:"
+ "setUserSessionAttributes pass for altDSID"
+ "status is Authenticated Guest Mode"
+ "unloadKeybagForSession:uid:"
+ "unloadSyncBagForSession:uid:splitUserVolumeEnabled:"
+ "user-%s"
+ "userSessionAttributesForOptions: could not find the requested session"
+ "v32@0:8@\"NSMutableDictionary\"16I24B28"
+ "v32@0:8@16I24B28"
+ "verifySyncBagForSession:uid:"
- "%s%s/%s.kb"
- "/private/var//keybags/usersyncbag.kb"
- "/private/var/keybags/LockoutState.plist"
- "APFSIOC_GET_DIR_STATS failed or uid:%d"
- "APFSUser Volume Unmount failed to mount"
- "APFSUser Volume Unmounted at home directory"
- "Adding Sandbox-kext path upload for uid %d, path:%s"
- "CHANGED DEVICE CONFIG from 0 --> 2!!"
- "Cannot support more users, Delete some to make room for new ones. Bailing..."
- "Clearing SyncBag if not needed for current FG ID:%d"
- "Could not provision due to error..."
- "Created path /var/Users"
- "Device already has 15 users, the maximum allowed with LocalUser Enrollment."
- "Error: _setAttributeOfType:Incorrect Type for the key %@"
- "FAILED Internal test Cleared"
- "FAILED Internal test setup"
- "Failed to Unload the AKS Identity for user:%d"
- "Failed to remove /var/Users hierarchy, please remove it"
- "Found problem with conversion at index:%d"
- "Improper session config to reset userquota"
- "In findAllUserSessionIDs"
- "LOCAL USER ENROLLMENT FEATURE ENABLED, WILL NOT BE ABLE TO PROVISION DEVICE; REMOVE FEATURE FLAG AND TRY AGAIN"
- "LOCAL USER ENROLLMENT FEATURE ENABLED, WILL NOT BE ABLE TO PROVISION DEVICE; REMOVE FEATURE FLAG AND TRY AGAIN - NOT SUPPORTED"
- "LOCAL USER ENROLLMENT FEATURE ENABLED, WILL NOT BE ABLE TO PROVISION THE DEVICE; REMOVE FEATURE FLAG AND TRY AGAIN"
- "LOGINWINDOW User EXISTS ALREADY, returning loginwindow setup"
- "Loaded AKS Identity"
- "Local User switching, switching to %d"
- "LocalUser Enrollment, creating new user adding %d user"
- "LocalUserEnrollment file Layout Set"
- "MKBUserSessionSetInternalTest:withReply:"
- "MKBUserSessionSetVolumeToPersona(%{public}@, %{public}@) failed: %d"
- "NO SYNCBAG TO REMOVE FOR LOGINWINDOW"
- "NOT MODIFIED THE LAST BOOTED USER, so 501 User will boot on reboot"
- "RESET kUMUserSessionHasSyncBagKey"
- "SUCCESSFUL Internal test Cleared"
- "SUCCESSFUL Internal test setup"
- "Setting UMLayout Handlers"
- "Skipping Sandbox Update for 501 user"
- "SyncBag Creation completed"
- "SyncBag exists, skipping..."
- "TRYING to Clear TestSetup for EDUMode"
- "TRYING to Setup Test for EDUMode"
- "Unload of SyncBag failed with error:%d"
- "Unload of SyncBag successful"
- "Unloaded the AKS Identity for user:%d"
- "UserManagement early boot task failed assertion: _gPersonaManager == ((void *)0)"
- "UserManagement loading foreground user failed assertion: [_gUserManager userWithUID:uid] != ((void *)0)"
- "UserManagement user switch failed assertion: _gPersonaManager == ((void *)0)"
- "UserSessionGuestUser"
- "configureLoginUIWithUserSessionCount:reply:"
- "dataMigrationSetup with NULL passcode"
- "dataMigrationSetup with SECRET passcode"
- "dataMigrationSetup: End"
- "dataMigrationSetup: Start"
- "dataMigrationSetup:withSecret:oldSize:reply:"
- "failed to Load AKS Identity, bailing"
- "failed to create:/var/Users (%s)\n"
- "failed to retrieve SyncBag content from keybag for uid %d: with error: 0x%x"
- "getUserSessionAttributes: could not find the requested session"
- "keybags"
- "loadUserSession"
- "removeUserSessionInternal"
- "removed /private/var/keybags/LockoutState.plist"
- "removed /var/Users path"
- "removed USER_SESSION_BAG_PATH"
- "removed USER_SYNC_BAG_PATH"
- "removed userBagPath"
- "setUserSessionAttributes"
- "switchToUserSessionNoUID with BLOB of size %ld"
- "switchToUserSessionNoUID, NO BLOB"
- "unlink of /private/var/keybags/LockoutState.plist failed with error"
- "unlink of USER_SESSION_BAG_PATH failed with error"
- "unlink of USER_SYNC_BAG_PATH failed with error"
- "unlink of userBagPath failed with error"
- "userbag"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v48@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32@?<v@?@\"NSError\">40"
```
