## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-72.40.7.0.0
-  __TEXT.__text: 0x1f0a8
+72.80.2.0.0
+  __TEXT.__text: 0x1f338
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x2f44
+  __TEXT.__objc_methlist: 0x2f94
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x1a87
+  __TEXT.__cstring: 0x1a89
   __TEXT.__oslogstring: 0x1817
   __TEXT.__gcc_except_tab: 0xb14
-  __TEXT.__unwind_info: 0x938
+  __TEXT.__unwind_info: 0x940
   __TEXT.__objc_classname: 0x6c9
-  __TEXT.__objc_methname: 0x5a48
-  __TEXT.__objc_methtype: 0x10d5
-  __TEXT.__objc_stubs: 0x45e0
+  __TEXT.__objc_methname: 0x5b6b
+  __TEXT.__objc_methtype: 0x110f
+  __TEXT.__objc_stubs: 0x46a0
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1560
+  __DATA_CONST.__objc_selrefs: 0x1590
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0xe20
-  __AUTH_CONST.__objc_const: 0x51b0
+  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__objc_const: 0x5220
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0xdc0
-  __DATA.__objc_ivar: 0x2d0
+  __DATA.__objc_ivar: 0x2d8
   __DATA.__data: 0xe00
   __DATA.__bss: 0x108
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 21D2250A-0D8C-3AD4-81CB-4F33308E3196
-  Functions: 934
-  Symbols:   3514
-  CStrings:  1671
+  UUID: 7D14A0F1-F019-38D5-B367-09962C1B8E0C
+  Functions: 940
+  Symbols:   3534
+  CStrings:  1686
 
Symbols:
+ +[DKAnalytics sendAnalyticsWithEvent:error:extraInfo:]
+ -[DKComponentIdentity dictionaryRepresentation]
+ -[DKExtensionAdapter beginRequest:payload:concurrentContext:completion:]
+ -[DKExtensionAdapter beginRequest:payload:concurrentContext:completion:].cold.1
+ -[DKRequestContext executingConcurrently]
+ -[DKRequestContext payload]
+ -[DKRequestContext setExecutingConcurrently:]
+ -[DKRequestContext setPayload:]
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table25
+ GCC_except_table28
+ GCC_except_table43
+ _OBJC_IVAR_$_DKRequestContext._executingConcurrently
+ _OBJC_IVAR_$_DKRequestContext._payload
+ ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke.38
+ ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke.40
+ ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke.47
+ ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke_2.42
+ ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke_2.42.cold.1
+ ___72-[DKExtensionAdapter beginRequest:payload:concurrentContext:completion:]_block_invoke
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$beginRequest:payload:concurrentContext:completion:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$executingConcurrently
+ _objc_msgSend$sendAnalyticsWithEvent:error:extraInfo:
+ _objc_msgSend$setExecutingConcurrently:
- -[DKExtensionAdapter beginRequest:payload:completion:]
- -[DKExtensionAdapter beginRequest:payload:completion:].cold.1
- GCC_except_table14
- GCC_except_table21
- GCC_except_table24
- GCC_except_table39
- ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke.25
- ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke.27
- ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke.34
- ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke_2.29
- ___49-[DKExtensionAdapter _attachHandlersToExtension:]_block_invoke_2.29.cold.1
- ___54-[DKExtensionAdapter beginRequest:payload:completion:]_block_invoke
- _objc_msgSend$beginRequest:payload:completion:
CStrings:
+ ","
+ "@\"<NSSecureCoding>\""
+ "T@\"<NSSecureCoding>\",&,N,V_payload"
+ "T@\"NSDictionary\",R,N"
+ "TB,N,V_executingConcurrently"
+ "_executingConcurrently"
+ "addEntriesFromDictionary:"
+ "beginRequest:payload:concurrentContext:completion:"
+ "componentsJoinedByString:"
+ "dictionaryRepresentation"
+ "executingConcurrently"
+ "sendAnalyticsWithEvent:error:extraInfo:"
+ "setExecutingConcurrently:"
+ "v40@0:8Q16@24@32"
+ "v44@0:8@16@24B32@?36"
- "beginRequest:payload:completion:"

```
