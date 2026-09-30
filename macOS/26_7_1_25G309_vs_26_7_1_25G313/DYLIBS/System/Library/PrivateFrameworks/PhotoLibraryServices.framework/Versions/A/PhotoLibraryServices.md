## PhotoLibraryServices

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/PhotoLibraryServices`

```diff

-860.0.170.0.0
-  __TEXT.__text: 0x7608fc
+860.0.173.0.0
+  __TEXT.__text: 0x760a40
   __TEXT.__auth_stubs: 0x48b0
   __TEXT.__objc_methlist: 0x40e54
   __TEXT.__const: 0x6a90
   __TEXT.__dlopen_cstrs: 0x671
-  __TEXT.__cstring: 0x62df2
+  __TEXT.__cstring: 0x62e30
   __TEXT.__swift5_typeref: 0xa66
   __TEXT.__swift5_capture: 0x7d8
   __TEXT.__constg_swiftt: 0x254
   __TEXT.__swift5_reflstr: 0x1a6
   __TEXT.__swift5_fieldmd: 0x20c
-  __TEXT.__oslogstring: 0x76075
+  __TEXT.__oslogstring: 0x760ac
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x20a80
+  __TEXT.__gcc_except_tab: 0x20aac
   __TEXT.__ustring: 0x588
   __TEXT.__unwind_info: 0x150b0
   __TEXT.__eh_frame: 0x6c8
   __TEXT.__objc_classname: 0xa516
-  __TEXT.__objc_methname: 0xb936d
+  __TEXT.__objc_methname: 0xb938d
   __TEXT.__objc_methtype: 0x1269f
-  __TEXT.__objc_stubs: 0x750a0
+  __TEXT.__objc_stubs: 0x750c0
   __DATA_CONST.__got: 0x4b60
   __DATA_CONST.__const: 0x5ce8
   __DATA_CONST.__objc_classlist: 0x2130
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x6e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22730
+  __DATA_CONST.__objc_selrefs: 0x22738
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x1458
   __DATA_CONST.__objc_arraydata: 0x1ae0
   __AUTH_CONST.__auth_got: 0x2470
   __AUTH_CONST.__const: 0x18368
-  __AUTH_CONST.__cfstring: 0x4cec0
+  __AUTH_CONST.__cfstring: 0x4cee0
   __AUTH_CONST.__objc_const: 0x674a8
   __AUTH_CONST.__objc_intobj: 0x4c80
   __AUTH_CONST.__objc_arrayobj: 0x12d8

   __DATA_DIRTY.__objc_data: 0x9d80
   __DATA_DIRTY.__data: 0x4c
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x670
+  __DATA_DIRTY.__bss: 0x680
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 26483
-  Symbols:   60246
-  CStrings:  45082
+  Symbols:   60247
+  CStrings:  45085
 
Symbols:
+ _objc_msgSend$isEntitledForPrivatePhotosTCCForToken:
Functions:
~ -[PLAssetsdService runDaemonJob:isSerial:withReply:] : 1532 -> 1856
CStrings:
+ "Rejecting runDaemonJob from unauthorized client %d: %@"
+ "isEntitledForPrivatePhotosTCCForToken:"
+ "runDaemonJob denied, client is missing a required entitlement"
```
