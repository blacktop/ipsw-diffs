## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-638.100.48.0.0
-  __TEXT.__text: 0x4da14
-  __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_stubs: 0x6a40
-  __TEXT.__objc_methlist: 0x2e60
-  __TEXT.__const: 0x148
+694.0.1.0.0
+  __TEXT.__text: 0x4e1d8
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_stubs: 0x6be0
+  __TEXT.__objc_methlist: 0x2ea0
+  __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x1bfc
-  __TEXT.__cstring: 0x3ee4
-  __TEXT.__objc_methname: 0x7536
-  __TEXT.__oslogstring: 0x7d33
+  __TEXT.__cstring: 0x4001
+  __TEXT.__objc_methname: 0x7692
+  __TEXT.__oslogstring: 0x7dc5
   __TEXT.__objc_classname: 0x74c
   __TEXT.__objc_methtype: 0x10e2
-  __TEXT.__unwind_info: 0xc70
-  __DATA_CONST.__auth_got: 0x7f8
-  __DATA_CONST.__got: 0x6d8
+  __TEXT.__unwind_info: 0xc80
+  __DATA_CONST.__auth_got: 0x808
+  __DATA_CONST.__got: 0x6c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1488
-  __DATA_CONST.__cfstring: 0x3920
+  __DATA_CONST.__cfstring: 0x3ac0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x5138
-  __DATA.__objc_selrefs: 0x1e80
-  __DATA.__objc_ivar: 0x2ac
+  __DATA.__objc_const: 0x5180
+  __DATA.__objc_selrefs: 0x1ee8
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x130

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F213A252-EE02-3172-8CEA-9EC9948CA5B4
-  Functions: 1344
-  Symbols:   485
-  CStrings:  3293
+  UUID: 5D5CDCBE-16FB-3A21-A595-0D932F1B1C97
+  Functions: 1354
+  Symbols:   484
+  CStrings:  3340
 
Symbols:
+ _MGCopyAnswer
+ _OBJC_CLASS_$_AKAnisetteProvisioningController
+ _os_variant_has_internal_diagnostics
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "ClientMetadata mismatch: %@ %@"
+ "DeviceColor"
+ "DeviceEnclosureColor"
+ "DeviceName"
+ "Failed to get machine ID: %@"
+ "ProductType"
+ "Request must be a multiple-icsc request with a passphrase or a stash"
+ "T@\"NSData\",R,C,N"
+ "T@\"NSData\",R,C,N,V_passcodeStashSecret"
+ "UserAssignedDeviceName"
+ "_passcodeStashSecret"
+ "_setError"
+ "anisetteDataWithError:"
+ "com.apple.security"
+ "currentClientMetadata"
+ "currentMachineID"
+ "device_color"
+ "device_enclosure_color"
+ "device_mid"
+ "device_model"
+ "device_model_class"
+ "device_model_version"
+ "device_name"
+ "encodedEscrowRecordWithPublicKey:certificateData:error:"
+ "enrollment request received without ClientMetadata or GenerateClientMetadata"
+ "ensureClientMetadata:forRequest:"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "generateClientMetadata"
+ "getBytes:range:"
+ "hasError"
+ "initWithEventName:eventCategory:initData:altDSID:"
+ "initWithStoreIdentifier:type:"
+ "machineID"
+ "marketing-name"
+ "passcodeStashSecret"
+ "position"
+ "request: icdp:%d multipleICSC:%d passphrase:%@ stash:%@"
+ "setPosition:"
+ "unlockScreenTypeWithOutSimplePasscodeType:"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "Request must be a multiple-icsc request with a passphrase"
- "additionalStoreWithIdentifier:"
- "encodedEscrowRecordWithPublicKey:error:"
- "failed to open connection to %s\n"
- "initWithEventName:eventCategory:initData:"
- "request: icdp:%d multipleICSC:%d passphrase:%@"

```
