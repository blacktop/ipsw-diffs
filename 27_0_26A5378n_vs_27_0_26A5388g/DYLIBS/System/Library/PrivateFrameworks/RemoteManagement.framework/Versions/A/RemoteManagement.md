## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/Versions/A/RemoteManagement`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-624.0.8.0.0
-  __TEXT.__text: 0x52a0c
-  __TEXT.__objc_methlist: 0x1c28
+624.0.10.0.0
+  __TEXT.__text: 0x52a50
+  __TEXT.__objc_methlist: 0x1c38
   __TEXT.__const: 0x1a70
   __TEXT.__cstring: 0x2521
   __TEXT.__oslogstring: 0x4aeb

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xfd0
+  __TEXT.__unwind_info: 0xfd8
   __TEXT.__eh_frame: 0x1658
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d8
+  __DATA_CONST.__objc_selrefs: 0x13e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x5f8
   __AUTH_CONST.__const: 0x1120
   __AUTH_CONST.__cfstring: 0x1b40
-  __AUTH_CONST.__objc_const: 0x2f50
+  __AUTH_CONST.__objc_const: 0x2f60
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0xb60
-  __AUTH.__objc_data: 0x898
-  __AUTH.__data: 0xae0
+  __AUTH_CONST.__auth_got: 0xb68
+  __AUTH.__objc_data: 0x638
+  __AUTH.__data: 0x858
   __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x768
-  __DATA.__bss: 0x25d0
+  __DATA.__bss: 0x2610
   __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__objc_data: 0x670
+  __DATA_DIRTY.__data: 0x298
+  __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1468
-  Symbols:   2060
+  Functions: 1469
+  Symbols:   2062
   CStrings:  715
 
Symbols:
+ -[RMManagedDevice isConfiguredToBeSharediPad]
+ _CP_MDMUserPushToken
Functions:
+ -[RMManagedDevice isConfiguredToBeSharediPad]
~ -[RMManagedDevice pushTokenWithScope:] : 4 -> 64
```
