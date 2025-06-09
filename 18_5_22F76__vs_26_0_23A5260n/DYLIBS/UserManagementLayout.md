## UserManagementLayout

> `/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout`

```diff

-417.100.1.0.0
-  __TEXT.__text: 0xd774
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0xa64
-  __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0x1971
-  __TEXT.__cstring: 0x53d
-  __TEXT.__unwind_info: 0x1b8
+452.0.0.0.0
+  __TEXT.__text: 0x1446c
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0xb14
+  __TEXT.__const: 0xd0
+  __TEXT.__oslogstring: 0x2704
+  __TEXT.__cstring: 0x62f
+  __TEXT.__unwind_info: 0x1f8
   __TEXT.__objc_classname: 0xe1
-  __TEXT.__objc_methname: 0x1864
-  __TEXT.__objc_methtype: 0x5ec
-  __TEXT.__objc_stubs: 0x1400
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__objc_methname: 0x1b58
+  __TEXT.__objc_methtype: 0x6b3
+  __TEXT.__objc_stubs: 0x1620
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x698
+  __DATA_CONST.__objc_selrefs: 0x710
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x2f0
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0x1108
+  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__objc_const: 0x1110
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x128
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E2C3AB4F-D8C2-366E-9FC5-A945685C4321
-  Functions: 240
-  Symbols:   133
-  CStrings:  670
+  UUID: 2346A1EE-E0DD-3A90-BDE0-0AFF82A12E86
+  Functions: 273
+  Symbols:   176
+  CStrings:  797
 
Symbols:
+ _AKSIdentityChangePasscode
+ _AKSIdentityChangePasscodeWithACM
+ _AKSIdentityCreateWithACM
+ _AKSIdentityLoginWithACMCred
+ _AKSIdentitySetPrimary
+ _APFSContainerGetBootDevice
+ _CFBooleanGetTypeID
+ _CFDictionaryCreateMutable
+ _CFDictionaryGetValue
+ _CFDictionarySetValue
+ _CFGetTypeID
+ _CFNumberGetValue
+ _CFStringGetCString
+ _CFStringHasPrefix
+ _IOIteratorNext
+ _IOObjectConformsTo
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperties
+ _IORegistryEntryGetChildIterator
+ _IORegistryEntryGetName
+ _IORegistryEntryGetParentEntry
+ _IOServiceGetMatchingServices
+ _IOServiceMatching
+ _aks_lock_device
+ _aks_unlock_device_with_acm
+ _bzero
+ _exit
+ _getmntinfo
+ _kCFBooleanFalse
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kIOMainPortDefault
+ _malloc_type_malloc
+ _objc_retain_x26
+ _objc_retain_x28
+ _posix_spawn
+ _strcmp
+ _strerror
+ _strncmp
+ _sysctl
+ _sysctlbyname
+ _sysctlnametomib
+ _waitpid
CStrings:
+ " Skipping the diskNode:%@ as its not in the Boot Container"
+ "%@/mobile"
+ "-o"
+ "/sbin/mount_apfs"
+ "2457711A-523C-4604-B75A-F48A571D5036"
+ "501 AKS Identity already loaded, failure"
+ "501 AKS Identity already not loaded, failure"
+ "501 AKS Identity is not loaded, returning success"
+ "@36@0:8@16I24^@28"
+ "AKSIdentityChangePasscode(%@, %u) failed: %{public}@"
+ "AKSIdentityLoginWithACMCred(%@, %u) failed: %{public}@"
+ "APFSContainerGetBootDevice failed with %d, bailing.."
+ "AppleAPFSContainer"
+ "AppleAPFSVolume"
+ "B40@0:8I16@\"NSData\"20B28^@32"
+ "B40@0:8I16@20B28^@32"
+ "B48@0:8@\"NSUUID\"16I24@\"NSData\"28B36^@40"
+ "B48@0:8@16I24@28B36^@40"
+ "B52@0:8@16@24I32I36S40^@44"
+ "B56@0:8@\"NSUUID\"16@\"NSData\"24@\"NSData\"32I40B44^@48"
+ "B56@0:8@\"NSUUID\"16@\"NSData\"24I32@\"NSData\"36B44^@48"
+ "B56@0:8@16@24@32I40B44^@48"
+ "B56@0:8@16@24I32@36B44^@48"
+ "BSD Name"
+ "BootDevice is %@"
+ "Cannot wait for pid: %s"
+ "Changed passcode of AKS identity: %{public}@"
+ "Container: %@, volumeDiskNode:%@"
+ "Created AKS identity: %{public}@"
+ "Data"
+ "Deleted AKS identity %{public}@"
+ "Deleted persona %{public}@ from AKS session %u"
+ "Encrypted"
+ "FALSE"
+ "Failed to allocate buffer to read OSEnvironment value. Assuming running in normal mode"
+ "Failed to delete primary user Identity, bailing"
+ "Failed to determine size of buffer to read OSEnvironment value(%s). Assuming running in normal mode"
+ "Failed to find Primary USER volume"
+ "Failed to find SDV"
+ "Failed to load Primary UID after recreating, bailing"
+ "Failed to load bootstrap user with the token, bailing"
+ "Failed to load user AKSIdfentity with error, bailing"
+ "Failed to login with identity UDV with error, bailing"
+ "Failed to map the UDV with error, unload identity, bailing.."
+ "Failed to mount the UDV with error, unload identity, bailing.."
+ "Failed to mount the volume with error %d"
+ "Failed to set chown  on volume mounts directory %{public}@"
+ "Failed to set permissions on volume mounts directory %{public}@"
+ "Failed to unload AKS Identity with error %@"
+ "Failed to unload primary user Identity, bailing"
+ "Failing to delete 501 OTI after failure to set Primary"
+ "Failing to delete 501 after load failure"
+ "Failing to set Primary, return error"
+ "Failing to unload 501 OTI after failure to set Primary"
+ "Failing to unload 501 OTI after successful setting of Primary"
+ "Forced unmount of VARMOBILE failed with %s"
+ "Found DiskNode: %@ within the Boot Container"
+ "Found Existing User Uid:%d"
+ "Found Primary User Volume:%s  isEncrypted:%s"
+ "Found SystemData Volume:%s isEncrypted:%s"
+ "IOService"
+ "Invalid user uuid string on the user manifest on the given SDV Path"
+ "NOT in DRE with error:%@"
+ "No manifest on the SDV Path"
+ "No primary user in the manifest"
+ "No primary user manifest on the SDV Path"
+ "No user uuidstring on the user manifest on the given SDV Path"
+ "No uuid available for the Primary user"
+ "Out of Memory!!! could not allocate dict, exiting...."
+ "Primary user Identity DELETED"
+ "Primary user Identity Refreshed, load the identity to set Primary"
+ "Primary user Identity not Present, continue with the creation of the Identity"
+ "Primary user Identity unloaded"
+ "Primary user manifest exists on the SDV Path"
+ "RoleValue"
+ "Running in DeviceRecoveryEnvironment\n"
+ "Running in OS environment: %s"
+ "Set Primary on new 501 OTI, all parts successful"
+ "TRUE"
+ "UMD: Found keybag Blob"
+ "Unable to determine OS environment: %d:(%s)\n"
+ "Unable to force UnMount SDV at given location"
+ "Unable to force unmap UDV at given location"
+ "Unable to locate UDV on the booted container"
+ "Unable to mount SDV at given location"
+ "Unable to recreate Primary user Identity with bootstrap user"
+ "Unable to spawn %s"
+ "User"
+ "VALID primary user with UUID"
+ "Volume is Encrypted"
+ "Volume is UnEncrypted"
+ "aks_lock_device after check failed with Error:%d"
+ "bootstrap user LOADED"
+ "bootstrap user Unlaoded "
+ "changeSecretrForIdentityWithUUID:oldPasscode:newPasscode:existingSession:isACMCredential:error:"
+ "could not find user with error:%@"
+ "createIdentityWithUUID:passcode:existingSession:existingSessionPasscode:isACMCredential:error:"
+ "dataWithData:"
+ "device-recovery"
+ "failed to unload the AKS identity"
+ "failed to unload the Bootstrap idenitity in the end"
+ "failed to unmount UDV on error path"
+ "getmntfsid failed with error:%d"
+ "hw.osenvironment"
+ "inDeviceRecoveryEnvironment"
+ "keybagOpaqueDataOnSharedDataVolumePath:withError:"
+ "legacy"
+ "loginIdentity:intoSession:passcode:isACMCredential:error:"
+ "mountSystemDataVolumeAt:withError:"
+ "mountUserDataVolumeOnSystemDataAt:withACMCredential:withError:"
+ "mountUserDataVolumeOnSystemDataAt:withSecret:withError:"
+ "mountVolumeAtPath:fromDevice:forUserUID:userGID:withMode:withError:"
+ "no APFS containers found"
+ "nodev"
+ "nosuid"
+ "primaryUserOnSharedDataVolumePath:withError:"
+ "readUserFromManifest:forUserUid:withError:"
+ "refreshPrimaryUserOnSharedDataVolumePath:withBootstrapToken:withError:"
+ "stringWithCString:encoding:"
+ "sysctl_fsid failed with error:%d"
+ "unMountVolumeAt:withError:"
+ "unable to fetch IORegistry properties"
+ "unable to scan IORegistry"
+ "unloaded AKS identity on error path"
+ "unlockIdentityInSession:passcode:isACMCredential:error:"
+ "unmountSystemDataVolumeAt:withError:"
+ "unmountUserDataVolumeOnSystemDataAt:withError:"
+ "unmounted UDV on error path"
+ "user with no opaqueData"
+ "vfs.generic.ctlbyfsid"
- "B36@0:8I16@\"NSData\"20^@28"
- "B36@0:8I16@20^@28"
- "B52@0:8@\"NSUUID\"16@\"NSData\"24I32@\"NSData\"36^@44"
- "B52@0:8@16@24I32@36^@44"
- "Created AKS identity: %@"
- "Deleted AKS identity %@"
- "createIdentityWithUUID:passcode:existingSession:existingSessionPasscode:error:"
- "loginIdentity:intoSession:passcode:error:"
- "unlockIdentityInSession:passcode:error:"

```
