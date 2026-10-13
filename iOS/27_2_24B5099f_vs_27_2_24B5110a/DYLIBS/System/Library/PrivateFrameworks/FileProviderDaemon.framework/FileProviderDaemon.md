## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-4838.40.130.0.2
-  __TEXT.__text: 0xa62ff8
-  __TEXT.__objc_methlist: 0x9b54
+4838.42.2.0.0
+  __TEXT.__text: 0xa63194
+  __TEXT.__objc_methlist: 0x9b6c
   __TEXT.__const: 0x2e640
-  __TEXT.__cstring: 0x500b5
-  __TEXT.__oslogstring: 0x21972
+  __TEXT.__cstring: 0x500d5
+  __TEXT.__oslogstring: 0x21992
   __TEXT.__gcc_except_tab: 0xd9d8
   __TEXT.__ustring: 0x1880
   __TEXT.__dlopen_cstrs: 0x114

   __TEXT.__swift_as_ret: 0x188
   __TEXT.__swift_as_cont: 0x36c
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__unwind_info: 0x1c108
+  __TEXT.__unwind_info: 0x1c100
   __TEXT.__eh_frame: 0x2d098
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6438
+  __DATA_CONST.__objc_selrefs: 0x6450
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__got: 0x1940
-  __AUTH_CONST.__const: 0x4ccc8
-  __AUTH_CONST.__cfstring: 0x7860
-  __AUTH_CONST.__objc_const: 0x28320
+  __AUTH_CONST.__const: 0x4cce8
+  __AUTH_CONST.__cfstring: 0x7880
+  __AUTH_CONST.__objc_const: 0x28370
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x3180
   __AUTH.__objc_data: 0x1ca8
   __AUTH.__data: 0x28a8
-  __DATA.__objc_ivar: 0xbf8
+  __DATA.__objc_ivar: 0xc00
   __DATA.__data: 0x82b0
   __DATA.__common: 0x21b
   __DATA_DIRTY.__objc_data: 0x34b0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 31851
-  Symbols:   12742
+  Functions: 31853
+  Symbols:   12747
   CStrings:  8354
 
Symbols:
+ -[FPDProviderDescriptor owningApplicationIsInstallationHeld]
+ -[FPDProviderDescriptor setOwningApplicationIsInstallationHeld:]
+ _OBJC_IVAR_$_FPDExtensionManager._installationHeldProviderUUIDs
+ _OBJC_IVAR_$_FPDProviderDescriptor._owningApplicationIsInstallationHeld
+ ___49-[FPDExtensionManager synchronousProviderUpdate:]_block_invoke_2
Functions:
~ -[FPDProviderDescriptor initWithExtensionRecord:] : 6552 -> 6604
~ -[FPDDomain disconnectionState] : 448 -> 500
~ -[FPDProviderDescriptor initWithCoder:] : 2132 -> 2152
~ -[FPDProviderDescriptor encodeWithCoder:] : 896 -> 916
~ -[FPDProviderDescriptor isEqual:] : 320 -> 344
- -[FPDProviderDescriptor setPurposeIdentifier:]
+ -[FPDProviderDescriptor purposeIdentifier]
+ -[FPDProviderDescriptor setPersonaIdentifier:]
+ -[FPDProviderDescriptor setManagedPersona:]
~ -[FPDProvider providerDomainForDomain:] : 1452 -> 1472
~ ___49-[FPDExtensionManager synchronousProviderUpdate:]_block_invoke : 572 -> 724
+ ___49-[FPDExtensionManager synchronousProviderUpdate:]_block_invoke_2
~ -[FPDExtensionManager .cxx_destruct] : 196 -> 208
- ___49-[FPDExtensionManager synchronousProviderUpdate:]_block_invoke.cold.2
CStrings:
+ "[DEBUG] Updating extensions: %@ -> %@ (held: %@ -> %@)"
+ "_owningApplicationIsInstallationHeld"
+ "\xe1"
- "\r"
- "[DEBUG] Updating extensions: %@ -> %@"
- "\xd1"
```
