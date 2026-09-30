## AccessibilityPlatformTranslation

> `/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation`

```diff

-502.7.8.0.0
-  __TEXT.__text: 0x14570
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x1134
-  __TEXT.__const: 0x578
-  __TEXT.__gcc_except_tab: 0x2e0
-  __TEXT.__cstring: 0x242c
-  __TEXT.__oslogstring: 0x56f
+534.1.0.0.0
+  __TEXT.__text: 0x156a0
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x11d4
+  __TEXT.__const: 0x5a0
+  __TEXT.__gcc_except_tab: 0x310
+  __TEXT.__cstring: 0x26d2
+  __TEXT.__oslogstring: 0x6ab
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__unwind_info: 0x548
   __TEXT.__objc_classname: 0x120
-  __TEXT.__objc_methname: 0x3cee
-  __TEXT.__objc_methtype: 0x69c
-  __TEXT.__objc_stubs: 0x3260
+  __TEXT.__objc_methname: 0x3eb7
+  __TEXT.__objc_methtype: 0x6b2
+  __TEXT.__objc_stubs: 0x33c0
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0xa60
+  __DATA_CONST.__const: 0xab8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe08
+  __DATA_CONST.__objc_selrefs: 0xe68
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x560
-  __AUTH_CONST.__auth_got: 0x3f0
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x2580
-  __AUTH_CONST.__objc_const: 0x13d0
-  __AUTH_CONST.__objc_intobj: 0xbe8
+  __AUTH_CONST.__auth_got: 0x400
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x2660
+  __AUTH_CONST.__objc_const: 0x1430
+  __AUTH_CONST.__objc_intobj: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x100
+  __DATA.__objc_ivar: 0x108
   __DATA.__data: 0x240
   __DATA.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D98A96BC-F02E-3976-BA44-240A92992358
-  Functions: 455
-  Symbols:   1831
-  CStrings:  1359
+  UUID: 1719518E-6333-3024-9733-28DAAAE9B8D5
+  Functions: 474
+  Symbols:   1888
+  CStrings:  1411
 
Symbols:
+ -[AXPRemoteCacheManager cachedTreeClientType]
+ -[AXPRemoteCacheManager initWithCachedTreeClientType:]
+ -[AXPRemoteCacheManager setCachedTreeClientType:]
+ -[AXPTranslator _treeDumpResponseIsApplicationOrientationData:]
+ -[AXPTranslator cachedTreeClientType]
+ -[AXPTranslator setCachedTreeClientType:]
+ -[AXPTranslator treeDumpApplicationOrientationForBridgeDelegateToken:]
+ -[AXPTranslator_iOS _attemptToResetSystemWideElement]
+ -[AXPTranslator_iOS _processApplicationOrientationForTreeDump:]
+ -[AXPTranslator_iOS _resetSystemWideElementAfterDelay]
+ -[AXPTranslator_iOS _resetSystemWideElement]
+ -[AXPTranslator_iOS _resetSystemWideElement].cold.1
+ -[AXPTranslator_iOS _usingCachedTreeForDevicesAppClient]
+ -[AXPTranslator_iOS _usingCachedTreeForOnenessClient]
+ -[AXPTranslator_iOS _usingCachedTree]
+ GCC_except_table123
+ GCC_except_table125
+ GCC_except_table14
+ GCC_except_table142
+ GCC_except_table159
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table2
+ GCC_except_table203
+ GCC_except_table22
+ GCC_except_table67
+ GCC_except_table78
+ _AXPTreeDumpTypeTreeDestroyed
+ _AXUIElementRegisterForApplicationDeath
+ _AXUIElementRegisterSystemWideServerDeathCallback
+ _OBJC_IVAR_$_AXPRemoteCacheManager._cachedTreeClientType
+ _OBJC_IVAR_$_AXPTranslator._cachedTreeClientType
+ ___30-[AXPRemoteCacheManager start]_block_invoke.283
+ ___30-[AXPRemoteCacheManager start]_block_invoke_2.284
+ ___30-[AXPRemoteCacheManager start]_block_invoke_2.cold.1
+ ___44-[AXPTranslator_iOS _resetSystemWideElement]_block_invoke
+ ___54-[AXPTranslator_iOS _resetSystemWideElementAfterDelay]_block_invoke
+ ___63-[AXPTranslator_iOS _processApplicationOrientationForTreeDump:]_block_invoke
+ ___72-[AXPTranslator_iOS axTreeDumpGenerateNextSetOfElementAttrsOnMainThread]_block_invoke.583
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8r48l8s40l8r56l8
+ ___block_literal_global.286
+ ___block_literal_global.303
+ ___block_literal_global.341
+ ___block_literal_global.344
+ ___block_literal_global.352
+ ___block_literal_global.384
+ ___block_literal_global.480
+ ___block_literal_global.574
+ ___block_literal_global.589
+ ___block_literal_global.591
+ ___block_literal_global.642
+ ___block_literal_global.651
+ ___block_literal_global.820
+ __systemWideServerDied
+ _objc_msgSend$_attemptToResetSystemWideElement
+ _objc_msgSend$_processApplicationOrientationForTreeDump:
+ _objc_msgSend$_resetSystemWideElement
+ _objc_msgSend$_resetSystemWideElementAfterDelay
+ _objc_msgSend$_treeDumpResponseIsApplicationOrientationData:
+ _objc_msgSend$_usingCachedTree
+ _objc_msgSend$_usingCachedTreeForDevicesAppClient
+ _objc_msgSend$_usingCachedTreeForOnenessClient
+ _objc_msgSend$cachedTreeClientType
+ _objc_msgSend$initWithCachedTreeClientType:
+ _objc_msgSend$setCachedTreeClientType:
+ _objc_msgSend$systemApplication
- -[AXPRemoteCacheManager dealloc]
- GCC_except_table1
- GCC_except_table11
- GCC_except_table117
- GCC_except_table13
- GCC_except_table131
- GCC_except_table148
- GCC_except_table15
- GCC_except_table17
- GCC_except_table192
- GCC_except_table21
- GCC_except_table61
- GCC_except_table72
- ___30-[AXPRemoteCacheManager start]_block_invoke.279
- ___30-[AXPRemoteCacheManager start]_block_invoke.cold.1
- ___72-[AXPTranslator_iOS axTreeDumpGenerateNextSetOfElementAttrsOnMainThread]_block_invoke_2
- ___block_literal_global.299
- ___block_literal_global.337
- ___block_literal_global.340
- ___block_literal_global.342
- ___block_literal_global.375
- ___block_literal_global.471
- ___block_literal_global.565
- ___block_literal_global.579
- ___block_literal_global.581
- ___block_literal_global.632
- ___block_literal_global.641
- ___block_literal_global.806
- _objc_msgSend$stop
CStrings:
+ "\"\""
+ "%s:"
+ "%s: %lu"
+ "%s: accessibilityEnabled: %@"
+ "%s: cachedTreeClientType: %lu"
+ "%s: error while attempting to process attrs: %lu"
+ "%s: failed to AXUIElementCreateSystemWide"
+ "%s: setting _systemAppElement"
+ "%s: successfully created systemApp with pid: %d"
+ "%s: system app died"
+ "%s: systemWideElement still nil, will retry after delay"
+ "-[AXPRemoteCacheManager initWithCachedTreeClientType:]"
+ "-[AXPRemoteCacheManager start]"
+ "-[AXPRemoteCacheManager stop]"
+ "-[AXPTranslator_iOS _attemptToResetSystemWideElement]"
+ "-[AXPTranslator_iOS _resetSystemWideElementAfterDelay]"
+ "-[AXPTranslator_iOS _resetSystemWideElement]"
+ "-[AXPTranslator_iOS _resetSystemWideElement]_block_invoke"
+ "-[AXPTranslator_iOS setAccessibilityEnabled:]"
+ "-[AXPTranslator_iOS setRequestResolvingBehavior:]"
+ "-[AXPTranslator_iOS systemAppElement]"
+ "@24@0:8Q16"
+ "AXPAttributeApplicationOrientation"
+ "AXPAttributeContentSize"
+ "AXPAttributeMapFeatureType"
+ "AXPAttributeMapSmartDescriptionData"
+ "AXPAttributeMemoryAddress"
+ "AXPTreeDumpTypeTreeDestroyed"
+ "TQ,N,V_cachedTreeClientType"
+ "YES"
+ "_attemptToResetSystemWideElement"
+ "_cachedTreeClientType"
+ "_processApplicationOrientationForTreeDump:"
+ "_resetSystemWideElement"
+ "_resetSystemWideElementAfterDelay"
+ "_treeDumpResponseIsApplicationOrientationData:"
+ "_usingCachedTree"
+ "_usingCachedTreeForDevicesAppClient"
+ "_usingCachedTreeForOnenessClient"
+ "cachedTreeClientType"
+ "initWithCachedTreeClientType:"
+ "q24@0:8@16"
+ "setCachedTreeClientType:"
+ "systemApplication"
+ "treeDumpApplicationOrientationForBridgeDelegateToken:"
+ "void _systemWideServerDied(void *)"
- "dealloc"

```
