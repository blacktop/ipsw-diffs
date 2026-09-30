## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation`

```diff

-247.0.1.0.0
-  __TEXT.__text: 0x38df4
-  __TEXT.__objc_methlist: 0x2ae4
+250.0.0.3.0
+  __TEXT.__text: 0x38e70
+  __TEXT.__objc_methlist: 0x2aec
   __TEXT.__const: 0x23a
-  __TEXT.__cstring: 0x50dd
+  __TEXT.__cstring: 0x511d
   __TEXT.__oslogstring: 0x350d
-  __TEXT.__gcc_except_tab: 0xe44
+  __TEXT.__gcc_except_tab: 0xe6c
   __TEXT.__dlopen_cstrs: 0x2d4
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_typeref: 0x21
   __TEXT.__swift5_reflstr: 0x2f
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xe88
+  __TEXT.__unwind_info: 0xe90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18f8
+  __DATA_CONST.__objc_selrefs: 0x1900
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1408
   __DATA_CONST.__got: 0x388
   __AUTH_CONST.__const: 0xa80
   __AUTH_CONST.__cfstring: 0x5a00
-  __AUTH_CONST.__objc_const: 0x6d30
+  __AUTH_CONST.__objc_const: 0x6d50
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__auth_got: 0x650
   __AUTH.__objc_data: 0x520
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x290
+  __DATA.__objc_ivar: 0x294
   __DATA.__data: 0x618
   __DATA.__bss: 0x128
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__data: 0x198
+  __DATA_DIRTY.__data: 0x1b0
   __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1275
-  Symbols:   2887
-  CStrings:  1083
+  Functions: 1276
+  Symbols:   2890
+  CStrings:  1084
 
Symbols:
+ +[BMVanillaContainer biomeDirectoryURLForContainerPath:]
+ OBJC_IVAR_$_BMAccessClient._connectionLock
+ _objc_msgSend$biomeDirectoryURLForContainerPath:
Functions:
~ +[BMVanillaContainer containerForPersonaIdentifier:error:] : 720 -> 688
+ +[BMVanillaContainer biomeDirectoryURLForContainerPath:]
~ -[BMResourceContainerManager _standardDataVaultContainerForResource:] : 148 -> 152
~ -[BMAccessClient initWithUseCase:sandboxExtensionCache:accessTracker:] : 316 -> 320
~ -[BMAccessClient _synchronousRemoteObjectProxyForDomain:errorHandler:] : 808 -> 844
CStrings:
+ "BiomeSpaceAttribution"
+ "IOService:/IOResources/AppleKeyStore/AppleKeyStoreUserClient"
- "AppleKeyStoreUserClient"
```
