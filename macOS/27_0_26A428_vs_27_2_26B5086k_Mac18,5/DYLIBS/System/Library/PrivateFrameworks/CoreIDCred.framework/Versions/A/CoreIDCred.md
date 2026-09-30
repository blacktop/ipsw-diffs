## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/Versions/A/CoreIDCred`

```diff

-9.41.1.0.0
-  __TEXT.__text: 0x30a28
-  __TEXT.__objc_methlist: 0x1f7c
+9.104.0.0.0
+  __TEXT.__text: 0x309a8
+  __TEXT.__objc_methlist: 0x1f6c
   __TEXT.__const: 0x3520
   __TEXT.__cstring: 0x11ab
   __TEXT.__oslogstring: 0x2685

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__unwind_info: 0x1710
+  __TEXT.__unwind_info: 0x1708
   __TEXT.__eh_frame: 0x9e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc40
+  __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__got: 0x2a8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1723
-  Symbols:   1738
+  Functions: 1722
+  Symbols:   1737
   CStrings:  310
 
Symbols:
- -[DCBiometricStore setModifiedGlobalAuthACL:externalizedLAContext:completion:]
Functions:
+ -[DCBiometricStore deleteGlobalAuthACLWithCompletion:]
- -[DCBiometricStore deleteGlobalAuthACLWithCompletion:]
+ -[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]
- -[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]
- -[DCBiometricStore boundAppletPresentmentACL:]
```
