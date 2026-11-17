## profiled

> `/usr/libexec/profiled`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`

```diff

-2483.60.6.0.0
-  __TEXT.__text: 0xc69d8
-  __TEXT.__auth_stubs: 0x2a20
-  __TEXT.__objc_stubs: 0x134a0
-  __TEXT.__objc_methlist: 0x6214
-  __TEXT.__const: 0x138e
-  __TEXT.__gcc_except_tab: 0x1210
-  __TEXT.__oslogstring: 0x100b0
-  __TEXT.__cstring: 0xaa6a
-  __TEXT.__objc_methname: 0x16c37
-  __TEXT.__objc_classname: 0xbfe
-  __TEXT.__objc_methtype: 0x23b2
-  __TEXT.__constg_swiftt: 0xe94
-  __TEXT.__swift5_typeref: 0x804
+2483.60.9.0.0
+  __TEXT.__text: 0xca8b0
+  __TEXT.__auth_stubs: 0x2a40
+  __TEXT.__objc_stubs: 0x13880
+  __TEXT.__objc_methlist: 0x6314
+  __TEXT.__const: 0x13fe
+  __TEXT.__gcc_except_tab: 0x126c
+  __TEXT.__oslogstring: 0x105e0
+  __TEXT.__cstring: 0xab6a
+  __TEXT.__objc_methname: 0x16fcd
+  __TEXT.__objc_classname: 0xc2e
+  __TEXT.__objc_methtype: 0x23e2
+  __TEXT.__constg_swiftt: 0xee8
+  __TEXT.__swift5_typeref: 0x83a
   __TEXT.__swift5_reflstr: 0xee6
-  __TEXT.__swift5_fieldmd: 0xb64
+  __TEXT.__swift5_fieldmd: 0xb90
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x9c
-  __TEXT.__swift5_types: 0xb8
-  __TEXT.__swift5_protos: 0x74
+  __TEXT.__swift5_proto: 0xa0
+  __TEXT.__swift5_types: 0xbc
+  __TEXT.__swift5_protos: 0x78
   __TEXT.__swift5_capture: 0x80
-  __TEXT.__unwind_info: 0x26c0
+  __TEXT.__unwind_info: 0x2750
   __TEXT.__eh_frame: 0x190
-  __DATA_CONST.__const: 0x3050
-  __DATA_CONST.__cfstring: 0x8760
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__const: 0x3118
+  __DATA_CONST.__cfstring: 0x87c0
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x1e8
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x1520
-  __DATA_CONST.__got: 0x2150
-  __DATA_CONST.__auth_ptr: 0x300
-  __DATA.__objc_const: 0x7090
-  __DATA.__objc_selrefs: 0x54e0
+  __DATA_CONST.__auth_got: 0x1530
+  __DATA_CONST.__got: 0x2190
+  __DATA_CONST.__auth_ptr: 0x310
+  __DATA.__objc_const: 0x71a0
+  __DATA.__objc_selrefs: 0x55c8
   __DATA.__objc_ivar: 0x204
-  __DATA.__objc_data: 0x1ea8
-  __DATA.__data: 0x900
+  __DATA.__objc_data: 0x1ef8
+  __DATA.__data: 0x960
   __DATA.__common: 0x60
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2738
-  Symbols:   1819
-  CStrings:  5783
+  Functions: 2773
+  Symbols:   1828
+  CStrings:  5841
 
Symbols:
+ _ACAccountPropertyDAAccountHost
+ _ACAccountPropertyHostname
+ _ACAccountPropertyIdentityEmailAddress
+ _MCBKDeviceClass
+ _MCBKDeviceManagerClass
+ _MCBKUserProtectedConfigurationClass
+ _MCFeatureVPNCreationAllowed
+ _MOSettingsGroupNameNetwork
+ _OBJC_CLASS_$_MONetworkSettingsGroup
+ _kDAAccountEmailAddress
- _MCBiometricKitClass
CStrings:
+ "-[MCProfileServiceServer releaseProfileReferencesToAccountWithIdentifier:completion:]_block_invoke"
+ "@48@0:8@16@24q32@40"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "AccountTakeover"
+ "Applying denyVPNCreation settings: %{bool,public}d"
+ "Applying effective Network settings"
+ "Biometric unlock is not disabled after it was disabled: %{public}@"
+ "Convenience biometric unlock was enabled while unlock is restricted. Reapplying the restriction."
+ "ConvenienceBioCreated"
+ "Could not detect biometric devices"
+ "Could not open biometric device type %ld: %{public}@"
+ "Could not read fingerprint options from device type %ld: %{public}@"
+ "Could not set fingerprint options on device type %ld: unlock %{public}@ payment %{public}@ error: %{public}@"
+ "Disabling biometric unlock for the unlock restriction: %{public}@"
+ "Failed to remove outgoing account %{public}@ with error: %{public}@"
+ "MCAccountPayloadProtocol"
+ "MCDDMManagedAccountUtilities"
+ "Not installing CalDAV payload %{public}@; account %{public}@ is owned by DDM."
+ "Not installing CardDAV payload %{public}@; account %{public}@ is owned by DDM."
+ "Not installing EAS payload %{public}@; account %{public}@ is owned by DDM."
+ "Not installing Google payload %{public}@; account %{public}@ is owned by DDM."
+ "Not installing LDAP payload %{public}@; account %{public}@ is owned by DDM."
+ "Not installing SubscribedCalendar payload %{public}@; account %{public}@ is owned by DDM."
+ "Not installing email payload %{public}@; account %{public}@ is owned by DDM."
+ "Not removing account %{public}@ with the profile; it is owned by DDM."
+ "Released account %{public}@ from profile %{public}@"
+ "RemoteManagementPrimaryAccountIdentifier"
+ "Set fingerprint options on device type %ld: unlock %{public}@ payment %{public}@"
+ "T@\"NSString\",?,&,N"
+ "_removeProfileOwnedOutgoingAccounts"
+ "acAccountIdentifier"
+ "accountMayBeRemovedWithProfile:"
+ "accountType"
+ "applePayEnabled"
+ "availableDevicesWithFailure:"
+ "caseInsensitiveCompare:"
+ "componentsWithString:"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "ddmManagedAccountOfType:emailAddress:"
+ "ddmManagedAccountOfType:hostname:port:username:"
+ "ddmManagedAccountOfType:subscriptionURL:username:"
+ "ddmManagedMailAccountOfType:emailAddress:incomingHostname:incomingPort:incomingUsername:outgoingHostname:outgoingPort:outgoingUsername:"
+ "denyVPNCreation"
+ "denyVPNCreationMetadata"
+ "descriptor"
+ "device detection failed"
+ "deviceWithDescriptor:error:"
+ "effectiveDenyVPNCreation should never be nil"
+ "isDDMManagedAccount:"
+ "network"
+ "notifyConvenienceBioCreated"
+ "profiled/MCAdapter+Network.swift"
+ "protectedConfigurationForUser:error:"
+ "query"
+ "releaseProfileReferencesToAccountWithIdentifier:"
+ "releaseProfileReferencesToAccountWithIdentifier:completion:"
+ "restrictedBoolForFeature:"
+ "setApplePayEnabled:"
+ "setProtectedConfiguration:forUser:credentialSet:error:"
+ "setUnlockEnabled:"
+ "subscriptionURL"
+ "type %ld: unlock %@"
+ "type %ld: unreadable (%@)"
+ "unlockEnabled"
+ "user"
+ "vpnCreationAllowed"
- "BKOptionAuthWithCredentialSet"
- "BKUserCfgTouchIDApplePayEnabled"
- "BKUserCfgTouchIDUnlockEnabled"
- "Could not set fingerprint options: %{public}@ Status: %d"
- "Set fingerprint options: %{public}@"
- "getProtectedConfiguration"
- "manager"
- "setProtectedConfiguration:withOptions:"
```
