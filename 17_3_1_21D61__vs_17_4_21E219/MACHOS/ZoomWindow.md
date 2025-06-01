## ZoomWindow

> `/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow`

```diff

-821.3.0.0.0
-  __TEXT.__text: 0x46994
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0xb980
-  __TEXT.__objc_methlist: 0x3ea4
+821.5.0.0.0
+  __TEXT.__text: 0x46b4c
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_stubs: 0xb9a0
+  __TEXT.__objc_methlist: 0x3ebc
   __TEXT.__const: 0x430
-  __TEXT.__objc_methname: 0x1137d
+  __TEXT.__objc_methname: 0x1147f
   __TEXT.__objc_classname: 0x7d8
-  __TEXT.__objc_methtype: 0x3789
-  __TEXT.__cstring: 0x1e85
+  __TEXT.__objc_methtype: 0x3845
+  __TEXT.__cstring: 0x1f66
   __TEXT.__gcc_except_tab: 0x790
-  __TEXT.__oslogstring: 0x319
-  __TEXT.__unwind_info: 0x1008
-  __DATA_CONST.__auth_got: 0x678
+  __TEXT.__oslogstring: 0x352
+  __TEXT.__unwind_info: 0x1014
+  __DATA_CONST.__auth_got: 0x680
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0xaf0
-  __DATA_CONST.__cfstring: 0x17a0
+  __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x3b8
+  __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_intobj: 0x108
-  __DATA_CONST.__objc_arraydata: 0x150
-  __DATA_CONST.__objc_arrayobj: 0xa8
+  __DATA_CONST.__objc_arraydata: 0x160
+  __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x8ef8
-  __DATA.__objc_selrefs: 0x3390
-  __DATA.__objc_classrefs: 0x3b8
-  __DATA.__objc_superrefs: 0x118
+  __DATA.__objc_const: 0x8f50
+  __DATA.__objc_selrefs: 0x33a8
   __DATA.__objc_ivar: 0x700
   __DATA.__objc_data: 0xc80
   __DATA.__data: 0xbd8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 61E9045D-A2EA-34F5-A93A-9A608BFF0840
-  Functions: 1645
-  Symbols:   4560
-  CStrings:  3397
+  UUID: F7DC75D8-178E-3001-B6C0-39B1A9D1670D
+  Functions: 1648
+  Symbols:   4564
+  CStrings:  3419
 
Symbols:
+ +[ZWUIServer isSafeToProcessMessageFromUnentitledProcessWithIdentifier:]
+ +[ZWUIServer requiredEntitlementForProcessingMessageWithIdentifier:]
+ _AXLogAssertions
+ __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke.244
+ __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_2.245
+ __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_3.246
+ __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_4.247
+ __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke.259
+ __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke.260
+ __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke_2.261
+ __67-[ZWRootViewController initWithAXUIService:onScreen:isMainDisplay:]_block_invoke.318
+ __67-[ZWRootViewController initWithAXUIService:onScreen:isMainDisplay:]_block_invoke_2.319
+ __75-[ZWUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.288
+ __block_literal_global.240
+ __block_literal_global.256
+ __block_literal_global.260
+ __block_literal_global.262
+ __block_literal_global.263
+ __block_literal_global.314
+ __block_literal_global.328
+ __block_literal_global.511
+ _objc_msgSend$securePayAssertionActive
+ _objc_msgSend$setWithArray:
+ _unnamed_array_storage.264
+ _unnamed_array_storage.269
+ _unnamed_array_storage.274
+ _unnamed_array_storage.277
+ _unnamed_array_storage.280
- __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke.220
- __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_2.221
- __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_3.222
- __42-[ZOTFullscreenEventHandler _handleEvent:]_block_invoke_4.223
- __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke.235
- __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke.236
- __49-[ZOTFullscreenEventHandler _scheduleTapTimeout:]_block_invoke_2.237
- __67-[ZWRootViewController initWithAXUIService:onScreen:isMainDisplay:]_block_invoke.294
- __67-[ZWRootViewController initWithAXUIService:onScreen:isMainDisplay:]_block_invoke_2.295
- __75-[ZWUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.246
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXUIService
- __block_literal_global.216
- __block_literal_global.232
- __block_literal_global.236
- __block_literal_global.238
- __block_literal_global.239
- __block_literal_global.290
- __block_literal_global.304
- __block_literal_global.487
- _objc_msgSend$setWithObject:
- _unnamed_array_storage.232
- _unnamed_array_storage.240
- _unnamed_array_storage.245
- _unnamed_array_storage.250
- _unnamed_array_storage.253
CStrings:
+ "@\"NSDictionary\"52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40^@44"
+ "@52@0:8@16Q24@32i40^@44"
+ "Not processing zoom alert because secure pay mode active"
+ "T@\"NSString\",?,R,C"
+ "com.apple.CoreRoutine.preferences"
+ "com.apple.accessibility.Carousel"
+ "com.apple.accessibility.voiceover"
+ "com.apple.private.allow-explicit-graphics-priority"
+ "com.apple.private.kernel.jetsam"
+ "com.apple.springboard.inCallPresentation"
+ "isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
+ "processMessage:withIdentifier:fromClientWithIdentifier:pid:error:"
+ "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:"
+ "securePayAssertionActive"
+ "setWithArray:"
+ "v52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8@16Q24@32i40@?44"
- "setWithObject:"

```
