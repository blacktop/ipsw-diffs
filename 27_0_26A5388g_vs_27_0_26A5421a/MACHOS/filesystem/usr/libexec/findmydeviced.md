## findmydeviced

> `/usr/libexec/findmydeviced`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-482.20.6.14.8
-  __TEXT.__text: 0x93c10
+482.20.6.14.14
+  __TEXT.__text: 0x93cf8
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0xdfe0
-  __TEXT.__objc_methlist: 0x8b34
+  __TEXT.__objc_stubs: 0xe080
+  __TEXT.__objc_methlist: 0x8ba4
   __TEXT.__const: 0x1d06
-  __TEXT.__gcc_except_tab: 0x1788
-  __TEXT.__objc_methname: 0x114db
-  __TEXT.__oslogstring: 0xb199
-  __TEXT.__cstring: 0x5ebe
-  __TEXT.__objc_classname: 0xfb6
-  __TEXT.__objc_methtype: 0x213c
+  __TEXT.__gcc_except_tab: 0x17cc
+  __TEXT.__objc_methname: 0x115bb
+  __TEXT.__oslogstring: 0xb139
+  __TEXT.__cstring: 0x5eae
+  __TEXT.__objc_classname: 0xff6
+  __TEXT.__objc_methtype: 0x219c
   __TEXT.__ustring: 0x56
   __TEXT.__swift5_typeref: 0x50a
   __TEXT.__swift5_capture: 0x240

   __TEXT.__swift5_protos: 0x8
   __TEXT.__unwind_info: 0x2478
   __TEXT.__eh_frame: 0xeac
-  __DATA_CONST.__const: 0x4238
+  __DATA_CONST.__const: 0x4208
   __DATA_CONST.__cfstring: 0x7160
-  __DATA_CONST.__objc_classlist: 0x458
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x68

   __DATA_CONST.__auth_got: 0xd80
   __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x718
-  __DATA.__objc_const: 0xe458
-  __DATA.__objc_selrefs: 0x4358
-  __DATA.__objc_ivar: 0x87c
-  __DATA.__objc_data: 0x2be8
-  __DATA.__data: 0x1500
+  __DATA.__objc_const: 0xe5b0
+  __DATA.__objc_selrefs: 0x4388
+  __DATA.__objc_ivar: 0x880
+  __DATA.__objc_data: 0x2c38
+  __DATA.__data: 0x1560
   __DATA.__bss: 0x2c10
   __DATA.__common: 0x58
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4013
+  Functions: 4017
   Symbols:   783
-  CStrings:  5427
+  CStrings:  5440
 
CStrings:
+ "#nvram - Skipping clear for key %@, already absent"
+ "%@ clearAllState: preserveLock=%d"
+ "@\"<FMDNVRAMWritePrimitives>\""
+ "@\"NSData\"24@0:8@\"NSString\"16"
+ "FMDNVRAMIOKitWritePrimitives"
+ "FMDNVRAMWritePrimitives"
+ "T@\"<FMDNVRAMWritePrimitives>\",&,N,V_writePrimitives"
+ "_writePrimitives"
+ "dataForKey:"
+ "i32@0:8@\"NSString\"16@\"NSData\"24"
+ "i32@0:8@16@24"
+ "initWithDevices:"
+ "initWithSerialNumbers:thisDeviceSerialNumber:"
+ "initWithWritePrimitives:"
+ "saveDataForKey:value:"
+ "setWritePrimitives:"
+ "writePrimitives"
- "#nvram - Error retrieving data value from nvrm. result code %d"
- "%@ clearAllState: Preserving PFLock activationLockInfo (maskedAppleID, activationLockStatus, fmLockType)"
- "addDevice:"
- "v24@?0@8^B16"
```
