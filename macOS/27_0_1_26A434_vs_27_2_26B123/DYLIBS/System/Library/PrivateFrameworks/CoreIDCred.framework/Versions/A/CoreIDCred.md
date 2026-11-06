## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/Versions/A/CoreIDCred`

```diff

-9.41.1.0.0
-  __TEXT.__text: 0x323e4
-  __TEXT.__objc_methlist: 0x1f7c
+9.108.0.0.0
+  __TEXT.__text: 0x32358
+  __TEXT.__objc_methlist: 0x1f6c
   __TEXT.__const: 0x3520
   __TEXT.__cstring: 0x11ab
   __TEXT.__oslogstring: 0x2685

   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc40
+  __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__got: 0x2a8

   __AUTH_CONST.__objc_const: 0x35d8
   __AUTH_CONST.__auth_got: 0x580
   __AUTH_CONST.__auth_ptr: 0x340
-  __AUTH.__objc_data: 0x240
   __DATA.__objc_ivar: 0x204
-  __DATA.__data: 0xc30
+  __DATA.__data: 0x9f0
   __DATA.__bss: 0x5980
-  __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__data: 0x158
+  __DATA_DIRTY.__objc_data: 0xa10
+  __DATA_DIRTY.__data: 0x398
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

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
