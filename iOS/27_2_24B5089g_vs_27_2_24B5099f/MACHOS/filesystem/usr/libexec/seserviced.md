## seserviced

> `/usr/libexec/seserviced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__oslogstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-71.8.0.0.0
-  __TEXT.__text: 0x486408
+71.9.0.0.0
+  __TEXT.__text: 0x486b9c
   __TEXT.__auth_stubs: 0x53e0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x33c
   __TEXT.__objc_stubs: 0xe800
   __TEXT.__objc_methlist: 0x71b4
-  __TEXT.__const: 0x16310
+  __TEXT.__const: 0x16330
   __TEXT.__gcc_except_tab: 0x32e0
-  __TEXT.__objc_methname: 0x197fd
+  __TEXT.__objc_methname: 0x197dd
   __TEXT.__oslogstring: 0x32d68
-  __TEXT.__cstring: 0x23076
+  __TEXT.__cstring: 0x23096
   __TEXT.__objc_classname: 0x3198
   __TEXT.__objc_methtype: 0x7ffd
-  __TEXT.__swift5_typeref: 0x5d3c
+  __TEXT.__swift5_typeref: 0x5d52
   __TEXT.__constg_swiftt: 0x61ac
   __TEXT.__swift5_builtin: 0x410
   __TEXT.__swift5_reflstr: 0x668a

   __TEXT.__swift_as_ret: 0x62c
   __TEXT.__swift5_mpenum: 0xdc
   __TEXT.__swift5_protos: 0x6c
-  __TEXT.__unwind_info: 0xd2b0
-  __TEXT.__eh_frame: 0x16ad4
+  __TEXT.__unwind_info: 0xd2f8
+  __TEXT.__eh_frame: 0x16bec
   __DATA_CONST.__const: 0x16618
   __DATA_CONST.__cfstring: 0x8b80
   __DATA_CONST.__objc_classlist: 0x890

   __DATA.__objc_selrefs: 0x4b08
   __DATA.__objc_ivar: 0xcfc
   __DATA.__objc_data: 0x6c30
-  __DATA.__data: 0xe904
-  __DATA.__common: 0x840
+  __DATA.__data: 0xe8f4
+  __DATA.__common: 0x838
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13504
+  Functions: 13513
   Symbols:   2613
-  CStrings:  11722
+  CStrings:  11721
 
CStrings:
+ "Setting scanning to %{bool}d with low power mode %{bool}d, Uwb available %{bool}d, biolockout backoff %{bool}d, express reader group identifiers %s, adaptive connection rssi threshold %hhd, device stationary %{bool}d, biolock %{bool}d, and geofence entry state %{bool}d"
+ "iOS (27.2) - SecureElementService-71.9"
- "Setting scanning to %{bool}d with low power mode %{bool}d, Uwb suspended %{bool}d, biolockout backoff %{bool}d, express reader group identifiers %s, adaptive connection rssi threshold %hhd, device stationary %{bool}d, biolock %{bool}d, and geofence entry state %{bool}d"
- "iOS (27.2) - SecureElementService-71.8"
- "isAvailable"
```
