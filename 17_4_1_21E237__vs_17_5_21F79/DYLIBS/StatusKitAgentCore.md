## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-25.500.131.0.0
-  __TEXT.__text: 0xa831c
+25.600.41.0.0
+  __TEXT.__text: 0xa84d8
   __TEXT.__auth_stubs: 0x15a0
-  __TEXT.__objc_methlist: 0x563c
+  __TEXT.__objc_methlist: 0x566c
   __TEXT.__const: 0x58c
   __TEXT.__cstring: 0x439a
-  __TEXT.__oslogstring: 0xe0fd
+  __TEXT.__oslogstring: 0xe122
   __TEXT.__gcc_except_tab: 0xac0
   __TEXT.__swift5_typeref: 0x78e
   __TEXT.__swift5_capture: 0x1d0

   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x20d8
+  __TEXT.__unwind_info: 0x20e0
   __TEXT.__eh_frame: 0x13a0
-  __TEXT.__objc_classname: 0xc81
-  __TEXT.__objc_methname: 0xec38
+  __TEXT.__objc_classname: 0xc84
+  __TEXT.__objc_methname: 0xecec
   __TEXT.__objc_methtype: 0x412a
   __TEXT.__objc_stubs: 0x8640
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x17d0
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x17f8
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc680
-  __DATA_CONST.__objc_selrefs: 0x2b70
+  __DATA_CONST.__objc_const: 0xc6e0
+  __DATA_CONST.__objc_selrefs: 0x2b90
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_classrefs: 0x4b8
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__cfstring: 0x20c0
-  __AUTH_CONST.__const: 0x1078
+  __AUTH_CONST.__const: 0xff8
   __AUTH_CONST.__objc_const: 0x1fa0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xae0
-  __AUTH.__objc_data: 0xae8
-  __DATA.__objc_ivar: 0x528
-  __DATA.__data: 0x1370
-  __DATA.__bss: 0x4c0
-  __DATA_DIRTY.__objc_data: 0xec8
-  __DATA_DIRTY.__data: 0x2f0
-  __DATA_DIRTY.__bss: 0x378
+  __AUTH.__objc_data: 0x908
+  __DATA.__objc_ivar: 0x530
+  __DATA.__data: 0x1300
+  __DATA.__bss: 0x3c0
+  __DATA_DIRTY.__const: 0x80
+  __DATA_DIRTY.__objc_data: 0x10a8
+  __DATA_DIRTY.__data: 0x390
+  __DATA_DIRTY.__bss: 0x480
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 94146A97-DCFE-34AB-80E5-CCF12682778A
-  Functions: 3338
-  Symbols:   8796
-  CStrings:  4057
+  UUID: 5788E7B2-F81E-3A9B-A162-E4D1BE6FA0E8
+  Functions: 3342
+  Symbols:   8808
+  CStrings:  4066
 
Symbols:
+ -[SKAAccountProvider cachedJwtTokenMap]
+ -[SKAAccountProvider cachedTimestamp]
+ -[SKAAccountProvider setCachedJwtTokenMap:]
+ -[SKAAccountProvider setCachedTimestamp:]
+ _AKAuthenticationIDMSTokenKey
+ _OBJC_IVAR_$_SKAAccountProvider._cachedJwtTokenMap
+ _OBJC_IVAR_$_SKAAccountProvider._cachedTimestamp
+ ___71-[SKAAccountProvider refreshCredentialForPrimaryAccountWithCompletion:]_block_invoke.38
+ ___71-[SKAAccountProvider refreshCredentialForPrimaryAccountWithCompletion:]_block_invoke.39
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$intersectSet:
- ___71-[SKAAccountProvider refreshCredentialForPrimaryAccountWithCompletion:]_block_invoke.35
- ___71-[SKAAccountProvider refreshCredentialForPrimaryAccountWithCompletion:]_block_invoke.36
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- _objc_msgSend$intersectsSet:
CStrings:
+ "\x01\x11"
+ "T@\"NSMutableDictionary\",&,N,V_cachedJwtTokenMap"
+ "Td,N,V_cachedTimestamp"
+ "Unable to fetch JWT token! Will use cached token if not expired"
+ "_cachedJwtTokenMap"
+ "_cachedTimestamp"
+ "cachedJwtTokenMap"
+ "cachedTimestamp"
+ "intersectSet:"
+ "setCachedJwtTokenMap:"
+ "setCachedTimestamp:"
- "Unable to fetch JWT token!"
- "intersectsSet:"

```
