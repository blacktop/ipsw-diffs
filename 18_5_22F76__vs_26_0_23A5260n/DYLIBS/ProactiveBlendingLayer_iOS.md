## ProactiveBlendingLayer_iOS

> `/System/Library/PrivateFrameworks/ProactiveBlendingLayer_iOS.framework/ProactiveBlendingLayer_iOS`

```diff

-588.12.0.0.0
-  __TEXT.__text: 0x2d8c
-  __TEXT.__auth_stubs: 0x230
+610.0.11.0.0
+  __TEXT.__text: 0x3228
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x35d
-  __TEXT.__oslogstring: 0x4a
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x3a3
+  __TEXT.__oslogstring: 0x151
+  __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_classname: 0x8c
   __TEXT.__objc_methname: 0x8f0
   __TEXT.__objc_methtype: 0x1a7

   __DATA_CONST.__objc_selrefs: 0x2a0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x120
-  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__auth_got: 0x128
+  __AUTH_CONST.__const: 0x600
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x318
   __AUTH_CONST.__objc_intobj: 0x168

   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x290
+  __DATA.__bss: 0x2d0
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient

   - /System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C23B2096-B6B5-3D34-A380-414F87AE2246
-  Functions: 159
-  Symbols:   582
-  CStrings:  186
+  UUID: BC56E7F5-FFCE-3C2E-8626-239AD6A7C323
+  Functions: 175
+  Symbols:   628
+  CStrings:  196
 
Symbols:
+ _____atxlog_handle_client_donations_block_invoke
+ _____atxlog_handle_document_predictor_block_invoke
+ _____atxlog_handle_menu_items_block_invoke
+ _____atxlog_handle_ml_inference_block_invoke
+ _____atxlog_handle_screen_entities_block_invoke
+ ___atxlog_handle_client_donations
+ ___atxlog_handle_client_donations.cold.1
+ ___atxlog_handle_client_donations.log
+ ___atxlog_handle_client_donations.onceToken
+ ___atxlog_handle_document_predictor
+ ___atxlog_handle_document_predictor.cold.1
+ ___atxlog_handle_document_predictor.log
+ ___atxlog_handle_document_predictor.onceToken
+ ___atxlog_handle_menu_items
+ ___atxlog_handle_menu_items.cold.1
+ ___atxlog_handle_menu_items.log
+ ___atxlog_handle_menu_items.onceToken
+ ___atxlog_handle_ml_inference
+ ___atxlog_handle_ml_inference.cold.1
+ ___atxlog_handle_ml_inference.log
+ ___atxlog_handle_ml_inference.onceToken
+ ___atxlog_handle_screen_entities
+ ___atxlog_handle_screen_entities.cold.1
+ ___atxlog_handle_screen_entities.log
+ ___atxlog_handle_screen_entities.onceToken
+ ___block_literal_global.128
+ ___block_literal_global.131
+ ___block_literal_global.134
+ ___block_literal_global.137
+ ___block_literal_global.140
+ __os_log_impl
CStrings:
+ "Filtering out %@ because UI isn't enabled"
+ "Filtering out %@ because UI isn't supported for it"
+ "Filtering out %@ because client model invalid for consumersubtype %d"
+ "Filtering out %@ because confidence score not met for %d"
+ "Filtering out %@ rendering not supported %d"
+ "client_donations"
+ "documentPredictor"
+ "inference"
+ "menuItems"
+ "screenEntities"

```
