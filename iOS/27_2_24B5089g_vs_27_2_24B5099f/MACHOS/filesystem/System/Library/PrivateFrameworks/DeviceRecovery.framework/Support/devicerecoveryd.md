## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-150.40.7.0.0
-  __TEXT.__text: 0x27308
-  __TEXT.__auth_stubs: 0x1300
-  __TEXT.__objc_stubs: 0x2920
-  __TEXT.__objc_methlist: 0xe2c
-  __TEXT.__cstring: 0x8100
+150.40.9.0.0
+  __TEXT.__text: 0x28e24
+  __TEXT.__auth_stubs: 0x1340
+  __TEXT.__objc_stubs: 0x2b80
+  __TEXT.__objc_methlist: 0xf04
+  __TEXT.__cstring: 0x8510
   __TEXT.__const: 0x4e8
-  __TEXT.__gcc_except_tab: 0x684
-  __TEXT.__objc_methname: 0x2b50
-  __TEXT.__oslogstring: 0x3b75
+  __TEXT.__gcc_except_tab: 0x6b8
+  __TEXT.__objc_methname: 0x2e00
+  __TEXT.__oslogstring: 0x4059
   __TEXT.__objc_classname: 0x1ca
-  __TEXT.__objc_methtype: 0x697
+  __TEXT.__objc_methtype: 0x6be
   __TEXT.__constg_swiftt: 0x78
   __TEXT.__swift5_typeref: 0x38
   __TEXT.__swift5_reflstr: 0x20
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xbb8
+  __TEXT.__unwind_info: 0xc30
   __TEXT.__eh_frame: 0xd8
-  __DATA_CONST.__const: 0xd58
-  __DATA_CONST.__cfstring: 0x3180
+  __DATA_CONST.__const: 0xd88
+  __DATA_CONST.__cfstring: 0x3360
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x990
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__auth_got: 0x9b0
+  __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x1750
-  __DATA.__objc_selrefs: 0xc70
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_const: 0x17d0
+  __DATA.__objc_selrefs: 0xd20
+  __DATA.__objc_ivar: 0xf0
   __DATA.__objc_data: 0x330
   __DATA.__data: 0x330
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 891
-  Symbols:   402
-  CStrings:  1777
+  Functions: 927
+  Symbols:   410
+  CStrings:  1855
 
Symbols:
+ _MAECopyActivationRecordWithError
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSSet
+ _fsync
+ _kMADeviceConfigurationFlags
+ _objc_setProperty_nonatomic_copy
+ _write
CStrings:
+ "!self.eraseAndUpdateRestricted"
+ "%{public}s: %lu client(s) restricting EACS / Software Update"
+ "%{public}s: %{public}@ in %{public}@ is missing or is not an array - treating the device as unrestricted"
+ "%{public}s: %{public}@ is not a string - leaving the demo device state unchanged"
+ "%{public}s: %{public}s EACS / Software Update restriction for '%{public}@'"
+ "%{public}s: '%{public}@' is already %{public}s"
+ "%{public}s: could not flush %{public}@: %{darwin.errno}d"
+ "%{public}s: could not open %{public}@: %{darwin.errno}d"
+ "%{public}s: could not read %{public}@ - treating the device as unrestricted"
+ "%{public}s: could not read the activation record: %{public}@ - leaving the demo device state unchanged"
+ "%{public}s: could not serialise the restriction clients: %{public}@"
+ "%{public}s: could not stat %{public}@: %{darwin.errno}d"
+ "%{public}s: could not stat the parent of %{public}@: %{darwin.errno}d"
+ "%{public}s: could not write %{public}@: %{darwin.errno}d"
+ "%{public}s: demo device is %{BOOL}d (device configuration flags 0x%lx from %{public}@)"
+ "%{public}s: dropping an unusable client entry in %{public}@"
+ "%{public}s: no %{public}@ - no client has restricted EACS / Software Update"
+ "%{public}s: the update volume is not mounted at %{public}@ - refusing to record a restriction that DRE would not see"
+ ", "
+ "-[DeviceRecoveryService activationRecordWithError:]"
+ "-[DeviceRecoveryService readRestrictionClients]"
+ "-[DeviceRecoveryService restrictionsPathIsOnUpdateVolume]"
+ "-[DeviceRecoveryService setEraseAndUpdateRestriction:forClient:completion:]"
+ "-[DeviceRecoveryService setRestrictionClients:]"
+ "-[DeviceRecoveryService updateDemoDeviceRestriction]"
+ ".."
+ "/private/var/MobileSoftwareUpdate/DeviceRecoveryRestrictions.plist"
+ "; "
+ "@\"NSSet\""
+ "@24@0:8^@16"
+ "Booting to NeRD is restricted by: %@"
+ "ClientsRestrictingEraseAndUpdate"
+ "Denying client connection - client is missing 'com.apple.DeviceRecovery.Control' entitlement"
+ "EACS is restricted by: %@"
+ "EraseAndUpdateRestricted"
+ "T@\"NSSet\",C,N,V_cachedRestrictionClients"
+ "TB,N,V_isDemoDevice"
+ "TB,R,N"
+ "[self clientHasRestrictEraseAndUpdateEntitlement:client]"
+ "[self setRestrictionClients:updatedClients]"
+ "_cachedRestrictionClients"
+ "_isDemoDevice"
+ "activationRecordWithError:"
+ "addEraseAndUpdateRestrictionForClient:completion:"
+ "adding"
+ "allObjects"
+ "auto-boot-once"
+ "cachedRestrictionClients"
+ "client %@ missing '%@' entitlement required to restrict EACS / Software Update"
+ "clientHasRestrictEraseAndUpdateEntitlement:"
+ "clientIdentifier.length > 0"
+ "com.apple.DeviceRecovery.RestrictEraseAndUpdate"
+ "compare:"
+ "could not %s restriction for %@"
+ "dataWithPropertyList:format:options:error:"
+ "demo device"
+ "eraseAndUpdateRestricted"
+ "isDemoDevice"
+ "no client identifier provided"
+ "readRestrictionClients"
+ "record"
+ "registered"
+ "remove"
+ "removeEraseAndUpdateRestrictionForClient:completion:"
+ "removeObject:"
+ "removing"
+ "restrictionClients"
+ "restrictionReason"
+ "restrictionsPathIsOnUpdateVolume"
+ "set"
+ "setCachedRestrictionClients:"
+ "setEraseAndUpdateRestriction:forClient:completion:"
+ "setIsDemoDevice:"
+ "setRestrictionClients:"
+ "sortedArrayUsingSelector:"
+ "the system data volume is not mounted"
+ "timed out after %ds reading the activation record"
+ "unregistered"
+ "updateDemoDeviceRestriction"
+ "v36@0:8B16@20@?28"
- "Denying client connection - client does not have 'com.apple.DeviceRecovery.Control' entitlement"
- "auto-boot"
```
