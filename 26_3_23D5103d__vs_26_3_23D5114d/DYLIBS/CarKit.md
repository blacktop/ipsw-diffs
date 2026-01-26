## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-746.22.0.0.0
-  __TEXT.__text: 0x58d8c
+746.24.2.0.0
+  __TEXT.__text: 0x58ec8
   __TEXT.__auth_stubs: 0xe60
   __TEXT.__objc_methlist: 0x5dbc
   __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x56e1
-  __TEXT.__oslogstring: 0x647a
+  __TEXT.__cstring: 0x56f1
+  __TEXT.__oslogstring: 0x64aa
   __TEXT.__gcc_except_tab: 0xa50
   __TEXT.__ustring: 0x24
   __TEXT.__dlopen_cstrs: 0x15e

   __TEXT.__objc_methtype: 0x23bc
   __TEXT.__objc_stubs: 0x9580
   __DATA_CONST.__got: 0x788
-  __DATA_CONST.__const: 0x1ea8
+  __DATA_CONST.__const: 0x1ec0
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170

   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x740
   __AUTH_CONST.__const: 0x1b50
-  __AUTH_CONST.__cfstring: 0x5960
+  __AUTH_CONST.__cfstring: 0x5980
   __AUTH_CONST.__objc_const: 0xee98
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x10c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BDA7AC7A-CEF9-3D11-9ADF-A896BD40AA64
-  Functions: 2777
-  Symbols:   9112
-  CStrings:  5007
+  UUID: EEA9DA44-1E5B-30B7-B9DF-15522209B24D
+  Functions: 2778
+  Symbols:   9116
+  CStrings:  5010
 
Symbols:
+ _CARSessionInfoKeyStopSessionReasons
+ _CARSessionStopSessionCommand
+ _CARSessionStopSessionDisconnectReasonKey
+ _CRFetchStopSessionReasonsList
+ ___24-[CARSession suggestUI:]_block_invoke.427
+ ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.364
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.617
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.617.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.617.cold.2
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.622
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.626
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2.627
+ ___CARHandleSuggestUI_block_invoke.423
+ ___block_literal_global.422
+ ___block_literal_global.432
- ___24-[CARSession suggestUI:]_block_invoke.421
- ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.358
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.614
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.614.cold.1
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.614.cold.2
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.619
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.623
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2.624
- ___CARHandleSuggestUI_block_invoke.417
- ___block_literal_global.416
- ___block_literal_global.426
- ___block_literal_global.629
Functions:
~ -[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:] : 5576 -> 5648
+ _CRFetchStopSessionReasonsList
~ ___swift_instantiateConcreteTypeFromMangledNameV2 : 72 -> 84
CStrings:
+ "Send stop session reasons supported: %{public}@"
+ "stopSessionReasons"

```
