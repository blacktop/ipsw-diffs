## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-622.1.14.10.4
-  __TEXT.__text: 0x27ad8
+622.1.16.10.3
+  __TEXT.__text: 0x27e48
   __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x1dc4
-  __TEXT.__cstring: 0x299c
-  __TEXT.__const: 0x238
-  __TEXT.__gcc_except_tab: 0x11d4
-  __TEXT.__oslogstring: 0xed8
+  __TEXT.__objc_methlist: 0x1dfc
+  __TEXT.__cstring: 0x29ac
+  __TEXT.__const: 0x248
+  __TEXT.__gcc_except_tab: 0x11e0
+  __TEXT.__oslogstring: 0x104c
   __TEXT.__dlopen_cstrs: 0x203
   __TEXT.__ustring: 0x1ee
   __TEXT.__swift5_typeref: 0x163

   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xf40
+  __TEXT.__unwind_info: 0xf48
   __TEXT.__eh_frame: 0x4f0
   __TEXT.__objc_classname: 0x4af
-  __TEXT.__objc_methname: 0x724b
-  __TEXT.__objc_methtype: 0xb30
-  __TEXT.__objc_stubs: 0x4700
+  __TEXT.__objc_methname: 0x735b
+  __TEXT.__objc_methtype: 0xb4d
+  __TEXT.__objc_stubs: 0x4760
   __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x1290
+  __DATA_CONST.__const: 0x1278
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16f8
+  __DATA_CONST.__objc_selrefs: 0x1720
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x528
-  __AUTH_CONST.__const: 0x768
-  __AUTH_CONST.__cfstring: 0x1bc0
-  __AUTH_CONST.__objc_const: 0x32d0
+  __AUTH_CONST.__const: 0x728
+  __AUTH_CONST.__cfstring: 0x1be0
+  __AUTH_CONST.__objc_const: 0x3310
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x150
   __AUTH.__data: 0x130
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x480
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0xa00
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A577F6B3-81E0-310E-B598-DB704D5BDD03
-  Functions: 1010
-  Symbols:   3448
-  CStrings:  1729
+  UUID: 5DC48F90-2C85-3D9A-973C-B5EF2C9B54CF
+  Functions: 1013
+  Symbols:   3446
+  CStrings:  1743
 
Symbols:
+ -[SFAppAutoFillOneTimeCodeProvider oneTimeCodeClient:detectedOneTimeCodes:].cold.1
+ -[SFAutoFillFeatureManager userIsEligibleForPasskeysWithICloudKeychain]
+ -[SFSafariCredential initWithUser:password:site:creationDate:customTitle:groupName:requestedHost:]
+ -[SFSafariCredential initWithUser:password:site:creationDate:customTitle:requestedHost:]
+ -[SFSafariCredential initWithUser:password:site:creationDate:requestedHost:]
+ -[SFSafariCredential requestedHost]
+ -[SFSafariCredential setRequestedHost:]
+ _OBJC_IVAR_$_SFSafariCredential._requestedHost
+ ___block_descriptor_40_e8_32s_e50_"SFSafariCredential"16?0"WBSSavedAccountMatch"8ls32l8
+ ___block_literal_global.149
+ ___block_literal_global.152
+ ___block_literal_global.158
+ ___block_literal_global.53
+ ___block_literal_global.76
+ ___block_literal_global.84
+ ___block_literal_global.87
+ _objc_msgSend$initWithUser:password:site:creationDate:customTitle:groupName:requestedHost:
+ _objc_msgSend$initWithUser:password:site:creationDate:customTitle:requestedHost:
+ _objc_msgSend$initWithUser:password:site:creationDate:requestedHost:
+ _objc_msgSend$requestedHost
+ _objc_msgSend$userIsEligibleForPasskeysWithICloudKeychain
- -[SFSafariCredential initWithUser:password:site:creationDate:groupName:]
- _WBS_LOG_CHANNEL_PREFIXPasswords
- _WBS_LOG_CHANNEL_PREFIXPasswords.cold.1
- _WBS_LOG_CHANNEL_PREFIXPasswords.log
- _WBS_LOG_CHANNEL_PREFIXPasswords.onceToken
- ___WBS_LOG_CHANNEL_PREFIXPasswords_block_invoke
- ___block_descriptor_32_e50_"SFSafariCredential"16?0"WBSSavedAccountMatch"8l
- ___block_literal_global.13
- ___block_literal_global.150
- ___block_literal_global.157
- ___block_literal_global.162
- ___block_literal_global.30
- ___block_literal_global.55
- ___block_literal_global.78
- ___block_literal_global.83
- ___block_literal_global.86
- ___block_literal_global.89
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SafariFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SafariFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SafariFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SafariFoundation
- _objc_msgSend$initWithUser:password:site:creationDate:
- _objc_msgSend$initWithUser:password:site:creationDate:customTitle:groupName:
CStrings:
+ "@72@0:8@16@24@32@40@48@56@64"
+ "Ignoring OTC from notification from %{private}@ because code string was nil or empty."
+ "Ignoring OTC from notification from %{private}@ because it's already covered by other support."
+ "Ignoring OTC from notification from %{private}@ because we failed to look up an LSBundleRecord for it, with error: %@"
+ "Ignoring OTC from notification from app with nil or empty appIdentifier."
+ "T@\"NSString\",&,N,V_requestedHost"
+ "_requestedHost"
+ "initWithUser:password:site:creationDate:customTitle:groupName:requestedHost:"
+ "initWithUser:password:site:creationDate:customTitle:requestedHost:"
+ "initWithUser:password:site:creationDate:requestedHost:"
+ "requestedHost"
+ "setRequestedHost:"
+ "userIsEligibleForPasskeysWithICloudKeychain"
- "initWithUser:password:site:creationDate:groupName:"

```
