## findmydeviced

> `/usr/libexec/findmydeviced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_acfuncs`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-482.31.6.16.11
-  __TEXT.__text: 0x4c9d70
-  __TEXT.__auth_stubs: 0x4e70
+482.31.6.16.16
+  __TEXT.__text: 0x4cca30
+  __TEXT.__auth_stubs: 0x4e60
   __TEXT.__objc_stubs: 0x18b20
   __TEXT.__objc_methlist: 0x10944
-  __TEXT.__const: 0x469e6
+  __TEXT.__const: 0x46a76
   __TEXT.__gcc_except_tab: 0x2880
-  __TEXT.__objc_methname: 0x20559
-  __TEXT.__oslogstring: 0x1d669
-  __TEXT.__cstring: 0xdfde
+  __TEXT.__objc_methname: 0x205e5
+  __TEXT.__oslogstring: 0x1d859
+  __TEXT.__cstring: 0xe02e
   __TEXT.__objc_classname: 0x2b46
   __TEXT.__objc_methtype: 0x3e2c
-  __TEXT.__swift5_typeref: 0x4df4
-  __TEXT.__constg_swiftt: 0x5c94
-  __TEXT.__swift5_reflstr: 0x57be
-  __TEXT.__swift5_fieldmd: 0x6ef4
+  __TEXT.__swift5_typeref: 0x4e1e
+  __TEXT.__constg_swiftt: 0x5ccc
+  __TEXT.__swift5_reflstr: 0x57fe
+  __TEXT.__swift5_fieldmd: 0x6f18
   __TEXT.__swift5_types: 0x838
-  __TEXT.__swift_as_entry: 0xd80
-  __TEXT.__swift_as_ret: 0x1478
-  __TEXT.__swift_as_cont: 0x20f0
-  __TEXT.__swift5_proto: 0x1414
+  __TEXT.__swift_as_entry: 0xd98
+  __TEXT.__swift_as_ret: 0x14a0
+  __TEXT.__swift_as_cont: 0x211c
+  __TEXT.__swift5_proto: 0x1418
   __TEXT.__swift5_assocty: 0xc40
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_capture: 0x1e60
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_mpenum: 0x138
   __TEXT.__swift5_acfuncs: 0xf0
-  __TEXT.__unwind_info: 0x12af0
-  __TEXT.__eh_frame: 0x2742c
-  __DATA_CONST.__const: 0x1dd50
+  __TEXT.__unwind_info: 0x12b60
+  __TEXT.__eh_frame: 0x27758
+  __DATA_CONST.__const: 0x1dd60
   __DATA_CONST.__cfstring: 0xb100
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0x60

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA_CONST.__auth_got: 0x2748
-  __DATA_CONST.__got: 0x1ba8
+  __DATA_CONST.__auth_got: 0x2740
+  __DATA_CONST.__got: 0x1b90
   __DATA_CONST.__auth_ptr: 0x1e38
-  __DATA.__objc_const: 0x1ece8
+  __DATA.__objc_const: 0x1ed48
   __DATA.__objc_selrefs: 0x7188
   __DATA.__objc_ivar: 0x1154
   __DATA.__objc_data: 0x55c0
-  __DATA.__data: 0xb2f0
-  __DATA.__common: 0x9f0
+  __DATA.__data: 0xb320
+  __DATA.__common: 0xa00
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16509
-  Symbols:   2719
-  CStrings:  10372
+  Functions: 16540
+  Symbols:   2717
+  CStrings:  10383
 
Symbols:
+ _$s10Foundation4DateV2leoiySbAC_ACtFZ
+ _$s11Distributed0A23TargetInvocationDecoderP18decodeNextArgumentqd__yKlFTj
- _$s10Foundation4DateVSLAAMc
- _$s14XPCDistributed9XPCSystemC17InvocationDecoderV18decodeNextArgumentxyKSeRzSERzlF
- _$sSL2leoiySbx_xtFZTj
- _swift_conformsToProtocol2
CStrings:
+ "%{public}s %{public}s %{public}s %{bool}d"
+ "%{public}s: Peripheral not connected."
+ "Accessory %{private,mask.hash}s does not support play sound"
+ "Accessory not connected, will not execute command."
+ "Detected non-matching findMy accessory: %{public}s"
+ "Disconnected from %{public}s, error: %{public}@"
+ "Failed to get play sound capability for accessory %{private,mask.hash}s, error: %@"
+ "Peripheral not connected, not executing command"
+ "Updated companionDeviceOnline: %{bool,public}d"
+ "_execute(command:peripheral:executeOnlyIfConnected:)"
+ "clientBundleIdentifier"
+ "com.apple.icloud.findmydeviced.btfinding"
+ "companionDeviceOnline"
- "Disconnected from %{public}s"
- "_execute(command:peripheral:)"
```
