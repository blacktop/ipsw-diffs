## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-541.5.2.0.1
-  __TEXT.__text: 0x4727e0
+541.10.0.0.0
+  __TEXT.__text: 0x472910
   __TEXT.__auth_stubs: 0x30f0
-  __TEXT.__objc_methlist: 0x39088
+  __TEXT.__objc_methlist: 0x390b8
   __TEXT.__const: 0x2654
   __TEXT.__cstring: 0x572f2
-  __TEXT.__oslogstring: 0x38e2b
+  __TEXT.__oslogstring: 0x38ec5
   __TEXT.__gcc_except_tab: 0xcf30
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x4

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xe998
+  __TEXT.__unwind_info: 0xe9a4
   __TEXT.__eh_frame: 0x1aa8
   __TEXT.__objc_classname: 0x8eb6
-  __TEXT.__objc_methname: 0xaf07f
-  __TEXT.__objc_methtype: 0x19a53
-  __TEXT.__objc_stubs: 0x4e180
+  __TEXT.__objc_methname: 0xaf14d
+  __TEXT.__objc_methtype: 0x19aa4
+  __TEXT.__objc_stubs: 0x4e1e0
   __DATA_CONST.__got: 0xaa8
   __DATA_CONST.__const: 0xbaa8
   __DATA_CONST.__objc_classlist: 0x1fb0
   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x72bc0
-  __DATA_CONST.__objc_selrefs: 0x1c6a0
+  __DATA_CONST.__objc_const: 0x72be0
+  __DATA_CONST.__objc_selrefs: 0x1c6c0
   __DATA_CONST.__objc_arraydata: 0x13c8
   __AUTH_CONST.__objc_const: 0x16de0
   __AUTH_CONST.__cfstring: 0x3b060

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 71F810C8-6EE0-37D3-B564-0BFD44E58CF7
-  Functions: 26233
-  Symbols:   78366
-  CStrings:  43463
+  UUID: C25FC20E-0030-3609-97C8-E3E4F7F9EB39
+  Functions: 26237
+  Symbols:   78377
+  CStrings:  43472
 
Symbols:
+ -[ATXModeEntityScorerServer rankedContactsForDenyListForMode:options:]
+ -[ATXModeEntityScorerServer rankedContactsForDenyListForMode:options:reply:]
+ -[ATXModeEntityScorerServer rankedContactsForDenyListForMode:options:reply:].cold.1
+ -[ATXModeEntityScorerServer rankedContactsForMode:options:]
+ -[ATXModeEntityScorerServer rankedContactsForNotificationsForMode:options:reply:]
+ -[ATXModeEntityScorerServer rankedContactsForNotificationsForMode:options:reply:].cold.1
+ -[ATXModeEntityScorerServer rankedEntitiesForDenyListForMode:entityTypeIdentifier:options:]
+ -[ATXModeEntityScorerServer rankedEntitiesForMode:entityTypeIdentifier:modeConfigurationType:options:]
+ -[ATXModeEntityScorerServer rankedEntitiesForMode:entityTypeIdentifier:options:]
+ ___64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.64
+ ___64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.64.cold.1
+ ___81-[ATXModeEntityScorerServer rankedContactsForNotificationsForMode:options:reply:]_block_invoke
+ ___81-[ATXModeEntityScorerServer rankedContactsForNotificationsForMode:options:reply:]_block_invoke_2
+ ___block_literal_global.82
+ _objc_msgSend$rankedContactsForDenyListForMode:options:
+ _objc_msgSend$rankedContactsForDenyListForMode:options:reply:
+ _objc_msgSend$rankedContactsForMode:options:
+ _objc_msgSend$rankedContactsForNotificationsForMode:options:reply:
+ _objc_msgSend$rankedEntitiesForDenyListForMode:entityTypeIdentifier:options:
+ _objc_msgSend$rankedEntitiesForMode:entityTypeIdentifier:modeConfigurationType:options:
+ _objc_msgSend$rankedEntitiesForMode:entityTypeIdentifier:options:
+ _objc_msgSend$recommendedDeniedContactsForMode:options:
- -[ATXModeEntityScorerServer rankedContactsForDenyListForMode:reply:].cold.1
- -[ATXModeEntityScorerServer rankedContactsForNotificationsForMode:reply:].cold.1
- -[ATXModeEntityScorerServer rankedEntitiesForDenyListForMode:entityTypeIdentifier:]
- -[ATXModeEntityScorerServer rankedEntitiesForMode:entityTypeIdentifier:]
- -[ATXModeEntityScorerServer rankedEntitiesForMode:entityTypeIdentifier:modeConfigurationType:]
- ___64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.61
- ___64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.61.cold.1
- ___73-[ATXModeEntityScorerServer rankedContactsForNotificationsForMode:reply:]_block_invoke
- ___73-[ATXModeEntityScorerServer rankedContactsForNotificationsForMode:reply:]_block_invoke_2
- _objc_msgSend$rankedContactsForDenyListForMode:
- _objc_msgSend$rankedEntitiesForDenyListForMode:entityTypeIdentifier:
- _objc_msgSend$rankedEntitiesForMode:entityTypeIdentifier:
- _objc_msgSend$rankedEntitiesForMode:entityTypeIdentifier:modeConfigurationType:
- _objc_msgSend$recommendedDeniedContactsForMode:
CStrings:
+ "%s: None of the notifications had associated contacts, so not returning any contact suggestions"
+ "@40@0:8Q16@24Q32"
+ "@48@0:8Q16@24q32Q40"
+ "Skipping contact id refresh because option was specified."
+ "rankedContactsForDenyListForMode:options:"
+ "rankedContactsForDenyListForMode:options:reply:"
+ "rankedContactsForMode:options:"
+ "rankedContactsForNotificationsForMode:options:reply:"
+ "rankedEntitiesForDenyListForMode:entityTypeIdentifier:options:"
+ "rankedEntitiesForMode:entityTypeIdentifier:modeConfigurationType:options:"
+ "rankedEntitiesForMode:entityTypeIdentifier:options:"
+ "recommendedDeniedContactsForMode:options:"
+ "v40@0:8Q16Q24@?32"
+ "v40@0:8Q16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
- "@40@0:8Q16@24q32"
- "rankedEntitiesForDenyListForMode:entityTypeIdentifier:"
- "rankedEntitiesForMode:entityTypeIdentifier:"
- "rankedEntitiesForMode:entityTypeIdentifier:modeConfigurationType:"
- "recommendedDeniedContactsForMode:"

```
