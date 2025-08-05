## AdID

> `/System/Library/PrivateFrameworks/AdID.framework/AdID`

```diff

-637.1.7.0.0
-  __TEXT.__text: 0x1946c
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x10ac
+637.1.11.0.0
+  __TEXT.__text: 0x196d0
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x10bc
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x6e8
-  __TEXT.__cstring: 0x6b3b
-  __TEXT.__unwind_info: 0x5b0
+  __TEXT.__cstring: 0x6c07
+  __TEXT.__unwind_info: 0x5b8
   __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x3f5f
+  __TEXT.__objc_methname: 0x401b
   __TEXT.__objc_methtype: 0x6f2
-  __TEXT.__objc_stubs: 0x4100
+  __TEXT.__objc_stubs: 0x4260
   __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__const: 0xaa0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1348
+  __DATA_CONST.__objc_selrefs: 0x13a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x4300
-  __AUTH_CONST.__objc_const: 0x25f0
+  __AUTH_CONST.__cfstring: 0x43a0
+  __AUTH_CONST.__objc_const: 0x2600
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 781C47D9-E058-32C3-BBFB-BC8F99BCA4B8
-  Functions: 417
-  Symbols:   1958
-  CStrings:  1936
+  UUID: 38754AEE-19DC-3205-81AE-F95AECF33C3C
+  Functions: 418
+  Symbols:   1974
+  CStrings:  1957
 
Symbols:
+ -[ADAdTrackingSchedulingManager setStateForProtoAccount]
+ GCC_except_table33
+ _NSSelectorFromString
+ _OBJC_CLASS_$_NSInvocation
+ ___block_literal_global.289
+ ___block_literal_global.86
+ _objc_msgSend$getReturnValue:
+ _objc_msgSend$invocationWithMethodSignature:
+ _objc_msgSend$invoke
+ _objc_msgSend$isProtoTeen
+ _objc_msgSend$isProtoTeenState
+ _objc_msgSend$methodSignatureForSelector:
+ _objc_msgSend$protoAccount
+ _objc_msgSend$setIsProtoTeen:
+ _objc_msgSend$setSelector:
+ _objc_msgSend$setStateForProtoAccount
+ _objc_msgSend$setTarget:
+ _objc_opt_respondsToSelector
- GCC_except_table32
- ___block_literal_global.276
- ___block_literal_global.84
CStrings:
+ "ProtoAccount"
+ "[%@ handleAccountChange]: Device is Proto Teen State."
+ "[%@]: Skipping sending segment data to AdPlatforms. Account %@ is a U13 or MAID or EDU or Proto U13/Teen account."
+ "[%@]: The current account is: EDU: %d. Managed: %d. U13: %d. T13: %d. U18: %d. Unknown Age: %d. Proto U13: %d. Proto Teen: %d"
+ "aa_isTeenProtoAccount"
+ "adprivacyd ignoring internal notification %@, it is no longer relevant."
+ "com.apple.AdPlatforms"
+ "getReturnValue:"
+ "invocationWithMethodSignature:"
+ "invoke"
+ "isProtoTeen"
+ "isProtoTeenState"
+ "methodSignatureForSelector:"
+ "protoAccount"
+ "setIsProtoTeen:"
+ "setSelector:"
+ "setStateForProtoAccount"
+ "setTarget:"
- "[%@]: Skipping sending segment data to AdPlatforms. Account %@ is a U13 or MAID or EDU or Proto U13 account."
- "[%@]: The current account is: EDU: %d. Managed: %d. U13: %d. T13: %d. U18: %d. Unknown Age: %d. Proto U13: %d"

```
