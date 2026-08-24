## studentd

> `/usr/libexec/studentd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`

```diff

-142.0.0.0.0
-  __TEXT.__text: 0xdfcfc
+143.1.1.0.0
+  __TEXT.__text: 0xe17ac
   __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_stubs: 0x12b00
-  __TEXT.__objc_methlist: 0xaf7c
-  __TEXT.__objc_methname: 0x19306
-  __TEXT.__objc_classname: 0x2b48
-  __TEXT.__objc_methtype: 0x3f4b
-  __TEXT.__cstring: 0x6382
-  __TEXT.__const: 0x19a0
-  __TEXT.__oslogstring: 0x74be
+  __TEXT.__objc_stubs: 0x12c00
+  __TEXT.__objc_methlist: 0xb09c
+  __TEXT.__objc_methname: 0x19456
+  __TEXT.__objc_classname: 0x2bda
+  __TEXT.__objc_methtype: 0x3f9b
+  __TEXT.__cstring: 0x6402
+  __TEXT.__const: 0x1a60
+  __TEXT.__oslogstring: 0x74de
   __TEXT.__gcc_except_tab: 0x7bc
   __TEXT.__ustring: 0x818
-  __TEXT.__swift5_typeref: 0xdc2
-  __TEXT.__constg_swiftt: 0x878
+  __TEXT.__swift5_typeref: 0xe26
+  __TEXT.__constg_swiftt: 0x8d0
   __TEXT.__swift5_reflstr: 0x7a3
-  __TEXT.__swift5_fieldmd: 0x550
+  __TEXT.__swift5_fieldmd: 0x570
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x84
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__swift5_capture: 0xa18
-  __TEXT.__swift_as_entry: 0x1b4
-  __TEXT.__swift_as_ret: 0x234
-  __TEXT.__swift_as_cont: 0x4cc
+  __TEXT.__swift5_types: 0x68
+  __TEXT.__swift5_capture: 0xa68
+  __TEXT.__swift_as_entry: 0x1bc
+  __TEXT.__swift_as_ret: 0x23c
+  __TEXT.__swift_as_cont: 0x4e4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4468
-  __TEXT.__eh_frame: 0x5a88
-  __DATA_CONST.__const: 0x4bb8
-  __DATA_CONST.__cfstring: 0x4840
-  __DATA_CONST.__objc_classlist: 0x918
+  __TEXT.__unwind_info: 0x44f8
+  __TEXT.__eh_frame: 0x5c58
+  __DATA_CONST.__const: 0x4cd0
+  __DATA_CONST.__cfstring: 0x48a0
+  __DATA_CONST.__objc_classlist: 0x930
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x898
+  __DATA_CONST.__objc_superrefs: 0x8a0
   __DATA_CONST.__objc_arraydata: 0x900
   __DATA_CONST.__objc_dictobj: 0x1680
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__auth_got: 0xda8
-  __DATA_CONST.__got: 0x13c8
-  __DATA_CONST.__auth_ptr: 0x298
-  __DATA.__objc_const: 0x15800
-  __DATA.__objc_selrefs: 0x53a0
+  __DATA_CONST.__got: 0x13e8
+  __DATA_CONST.__auth_ptr: 0x2a8
+  __DATA.__objc_const: 0x15980
+  __DATA.__objc_selrefs: 0x53e8
   __DATA.__objc_ivar: 0x9cc
-  __DATA.__objc_data: 0x6058
-  __DATA.__data: 0x2b18
-  __DATA.__bss: 0x1800
+  __DATA.__objc_data: 0x6208
+  __DATA.__data: 0x2b80
+  __DATA.__bss: 0x1810
   __DATA.__common: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5290
-  Symbols:   1166
-  CStrings:  5798
+  Functions: 5338
+  Symbols:   1170
+  CStrings:  5818
 
Symbols:
+ _CRKDeviceLastStudentErrorKey
+ _OBJC_CLASS_$_CRKKeychainMigrationServiceProxy
+ _OBJC_CLASS_$_CRKMigrateKeychainItemsToModernKeychainRequest
+ _OBJC_CLASS_$_CRKRemovePersistentIDsFromLoginKeychainRequest
CStrings:
+ "STUDidFailAppLockNotificationName"
+ "STULastStudentErrorProvider"
+ "STULastStudentErrorProvider.m"
+ "STUMigrateKeychainItemsToModernKeychainOperation"
+ "STURemovePersistentIDsFromLoginKeychainOperation"
+ "TB,N,VdidPostAppLockFailure"
+ "TB,N,VdidSuccessfullyApplyLock"
+ "didFailAppLock:"
+ "didPostAppLockFailure"
+ "didSuccessfullyApplyLock"
+ "kCRKStudentErrorTimestampKey"
+ "lastStudentError = %{public}@"
+ "performMigrationRequest:completion:"
+ "performRemovalRequest:completion:"
+ "postAppLockFailureIfNeeded"
+ "reportErrorWithCode:"
+ "request.persistentIDs"
+ "setDidPostAppLockFailure:"
+ "setDidSuccessfullyApplyLock:"
+ "v24@?0@\"CRKMigrateKeychainItemsToModernKeychainResultObject\"8@\"NSError\"16"
```
