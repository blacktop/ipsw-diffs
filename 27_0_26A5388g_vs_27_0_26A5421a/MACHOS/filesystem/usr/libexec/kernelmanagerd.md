## kernelmanagerd

> `/usr/libexec/kernelmanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-514.0.0.0.0
-  __TEXT.__text: 0x13af24
+514.0.2.0.0
+  __TEXT.__text: 0x13af40
   __TEXT.__auth_stubs: 0x3370
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0x8e8
   __TEXT.__swift5_typeref: 0x470a
   __TEXT.__swift5_capture: 0xc80
-  __TEXT.__const: 0x14698
+  __TEXT.__const: 0x146a8
   __TEXT.__constg_swiftt: 0x572c
-  __TEXT.__swift5_reflstr: 0x2ae8
-  __TEXT.__swift5_fieldmd: 0x4df8
+  __TEXT.__swift5_reflstr: 0x2b08
+  __TEXT.__swift5_fieldmd: 0x4e04
   __TEXT.__swift5_types: 0x6b8
-  __TEXT.__cstring: 0x15db0
+  __TEXT.__cstring: 0x15ddd
   __TEXT.__objc_classname: 0x11e1
   __TEXT.__swift5_builtin: 0x280
   __TEXT.__swift5_assocty: 0xa20
   __TEXT.__swift5_protos: 0xdc
   __TEXT.__swift5_proto: 0x10b0
-  __TEXT.__objc_methname: 0x28ad
+  __TEXT.__objc_methname: 0x28cd
   __TEXT.__objc_methtype: 0xac8
   __TEXT.__swift5_mpenum: 0x64
-  __TEXT.__oslogstring: 0xd2a
+  __TEXT.__oslogstring: 0xd40
   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x5530
-  __TEXT.__eh_frame: 0x9230
-  __DATA_CONST.__const: 0xd4b0
+  __TEXT.__eh_frame: 0x9210
+  __DATA_CONST.__const: 0xd4d8
   __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__auth_got: 0x19c0
   __DATA_CONST.__got: 0x7a0
   __DATA_CONST.__auth_ptr: 0x8f0
-  __DATA.__objc_const: 0x4e80
+  __DATA.__objc_const: 0x4ea0
   __DATA.__objc_selrefs: 0x708
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xcd8
-  __DATA.__data: 0x6372
+  __DATA.__data: 0x6362
   __DATA.__bss: 0x1dc90
   __DATA.__common: 0x6e0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   Functions: 9523
   Symbols:   1207
-  CStrings:  2431
+  CStrings:  2432
 
CStrings:
+ "KernelManagement_executables-514.0.2"
+ "Processing pending requests from the kernel, if any"
+ "disk is vitual ?: %d\n"
+ "processPendingRequestsOnActivation"
- "KernelManagement_executables-514"
- "PATH_KEY_POLICY_PATH"
- "PATH_KEY_PREBOOT_FD"
```
