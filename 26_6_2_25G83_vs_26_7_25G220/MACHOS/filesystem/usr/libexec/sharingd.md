## sharingd

> `usr/libexec/sharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

 2094.70.81.0.0
-  __TEXT.__text: 0x69cac8
-  __TEXT.__auth_stubs: 0x9320
+  __TEXT.__text: 0x6a4ab4
+  __TEXT.__auth_stubs: 0x9330
   __TEXT.__objc_stubs: 0x29ee0
   __TEXT.__objc_methlist: 0x1aa0c
-  __TEXT.__cstring: 0x32386
-  __TEXT.__objc_methname: 0x3de85
+  __TEXT.__cstring: 0x32696
+  __TEXT.__objc_methname: 0x3deb5
   __TEXT.__objc_classname: 0x52d1
   __TEXT.__objc_methtype: 0x93c9
-  __TEXT.__const: 0x1bc89
-  __TEXT.__oslogstring: 0x32a31
+  __TEXT.__const: 0x1cc59
+  __TEXT.__oslogstring: 0x32ab1
   __TEXT.__gcc_except_tab: 0x2ed0
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x1c0
-  __TEXT.__swift5_typeref: 0x98ac
-  __TEXT.__constg_swiftt: 0xa9f4
-  __TEXT.__swift5_builtin: 0x2d0
-  __TEXT.__swift5_reflstr: 0x6f3d
-  __TEXT.__swift5_fieldmd: 0x8a88
-  __TEXT.__swift5_assocty: 0x16a8
-  __TEXT.__swift5_proto: 0x1644
-  __TEXT.__swift5_types: 0x904
-  __TEXT.__swift_as_entry: 0xe94
-  __TEXT.__swift_as_ret: 0xdf8
-  __TEXT.__swift5_capture: 0x45d4
-  __TEXT.__swift5_protos: 0x224
-  __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x139b0
-  __TEXT.__eh_frame: 0x249a8
-  __DATA_CONST.__auth_got: 0x49a0
-  __DATA_CONST.__got: 0x2cf0
-  __DATA_CONST.__auth_ptr: 0x1908
-  __DATA_CONST.__const: 0x1c0d0
-  __DATA_CONST.__cfstring: 0x147c0
+  __TEXT.__swift5_typeref: 0x99c2
+  __TEXT.__constg_swiftt: 0xad68
+  __TEXT.__swift5_builtin: 0x2e4
+  __TEXT.__swift5_reflstr: 0x717d
+  __TEXT.__swift5_fieldmd: 0x8f9c
+  __TEXT.__swift5_assocty: 0x1768
+  __TEXT.__swift5_capture: 0x4644
+  __TEXT.__swift5_proto: 0x1750
+  __TEXT.__swift5_types: 0x964
+  __TEXT.__swift_as_entry: 0xe9c
+  __TEXT.__swift_as_ret: 0xdfc
+  __TEXT.__swift5_protos: 0x228
+  __TEXT.__swift5_mpenum: 0x24
+  __TEXT.__unwind_info: 0x13760
+  __TEXT.__eh_frame: 0x24ec8
+  __DATA_CONST.__auth_got: 0x49a8
+  __DATA_CONST.__got: 0x2cf8
+  __DATA_CONST.__auth_ptr: 0x1938
+  __DATA_CONST.__const: 0x1d220
+  __DATA_CONST.__cfstring: 0x147e0
   __DATA_CONST.__objc_classlist: 0xdb8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x568

   __DATA_CONST.__objc_arrayobj: 0x348
   __DATA_CONST.__objc_dictobj: 0x15b8
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x34be0
+  __DATA.__objc_const: 0x34c40
   __DATA.__objc_selrefs: 0xdb28
-  __DATA.__objc_ivar: 0x24f8
+  __DATA.__objc_ivar: 0x24fc
   __DATA.__objc_data: 0x9df0
-  __DATA.__data: 0x183ca
-  __DATA.__bss: 0x16740
+  __DATA.__data: 0x188ba
+  __DATA.__bss: 0x169c0
   __DATA.__common: 0x810
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24816
-  Symbols:   4077
-  CStrings:  22619
+  Functions: 25023
+  Symbols:   4079
+  CStrings:  22642
 
Symbols:
+ _$s7Sharing10SFPlatformV6pebbleACvgZ
+ _SFIsDeviceHomeAccessory
CStrings:
+ " found for feature, remote device type is "
+ "AuthenticationUnlockVolumeEnabled"
+ "B525ish"
+ "Could not determine model of remote device"
+ "Forcing this device to identify as a B525\n"
+ "HomeAccessory"
+ "HomePod identifying as B525: %s -> %s\n"
+ "Invalid message object received for UnlockVolume"
+ "Invalid message object received for UnlockVolumePairing"
+ "Missing AKS token data"
+ "Need remoteDeviceID to get Local LTK for feature requiring it"
+ "No remote device matching "
+ "Process PairingResponse SessionID: %s"
+ "Wrong options type"
+ "_homePodIdentifiesAsB525"
+ "com.apple.sharing:/Authentications/UnlockVolume/Enabled"
+ "connectedHomeAccessories"
+ "device matching [%s] found for feature, remote device type is %s"
+ "homePodIdentifiesAsB525"
+ "missing aksToken"
+ "unlockVolume"
+ "unlockVolumeHeartbeat"
+ "unlockVolumePairing"
```
