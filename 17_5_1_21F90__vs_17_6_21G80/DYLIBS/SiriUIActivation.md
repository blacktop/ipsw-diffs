## SiriUIActivation

> `/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation`

```diff

-3305.4.1.1.2
-  __TEXT.__text: 0x16110
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x1140
+3306.9.1.0.0
+  __TEXT.__text: 0x16684
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x1168
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x544
-  __TEXT.__cstring: 0x2d72
-  __TEXT.__oslogstring: 0x2b9a
-  __TEXT.__unwind_info: 0x718
+  __TEXT.__cstring: 0x2e2f
+  __TEXT.__oslogstring: 0x2c25
+  __TEXT.__unwind_info: 0x728
   __TEXT.__objc_classname: 0x2ed
-  __TEXT.__objc_methname: 0x64fb
-  __TEXT.__objc_methtype: 0x10bc
-  __TEXT.__objc_stubs: 0x46e0
+  __TEXT.__objc_methname: 0x65cb
+  __TEXT.__objc_methtype: 0x10fa
+  __TEXT.__objc_stubs: 0x4820
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x20e8
-  __DATA_CONST.__objc_selrefs: 0x1578
+  __DATA_CONST.__objc_const: 0x2150
+  __DATA_CONST.__objc_selrefs: 0x15d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x270
+  __DATA_CONST.__objc_classrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__objc_const: 0x288
-  __AUTH_CONST.__cfstring: 0x620
+  __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x148
+  __DATA.__objc_ivar: 0x14c
   __DATA.__data: 0x4e0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 479
-  Symbols:   2077
-  CStrings:  1397
+  Functions: 487
+  Symbols:   2108
+  CStrings:  1420
 
Symbols:
+ -[SiriPresentationViewController _activeTCCHasContentAtPoint:]
+ -[SiriPresentationViewController _activeTCCHasContentAtPoint:].cold.1
+ -[SiriPresentationViewController didDismissLocationTCC:]
+ -[SiriPresentationViewController didDismissLocationTCC:].cold.1
+ -[SiriPresentationViewController didPresentLocationTCC:]
+ -[SiriPresentationViewController didPresentLocationTCC:].cold.1
+ GCC_except_table105
+ GCC_except_table120
+ GCC_except_table125
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table209
+ GCC_except_table210
+ GCC_except_table217
+ GCC_except_table222
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table29
+ GCC_except_table37
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table81
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table92
+ GCC_except_table94
+ GCC_except_table99
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_SiriPresentationViewController._activeTCCs
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SiriPresentation
+ ___73-[SiriPresentationViewController _clearSiriViewControllerWithCompletion:]_block_invoke.255
+ ___89-[SiriPresentationViewController handleButtonDownFromButtonIdentifier:timestamp:context:]_block_invoke.224
+ ___92-[SiriPresentationViewController _presentationDismissalRequestedWithOptions:withCompletion:]_block_invoke.218
+ ___92-[SiriPresentationViewController _presentationDismissalRequestedWithOptions:withCompletion:]_block_invoke.219
+ ___99-[SiriPresentationViewController _presentSiriViewControllerWithPresentationOptions:requestOptions:]_block_invoke.183
+ __os_log_debug_impl
+ __unnamed_array_storage.179
+ __unnamed_array_storage.180
+ __unnamed_array_storage.209
+ __unnamed_array_storage.210
+ __unnamed_array_storage.236
+ __unnamed_array_storage.237
+ __unnamed_array_storage.280
+ __unnamed_array_storage.281
+ __unnamed_array_storage.93
+ _objc_msgSend$_activeTCCHasContentAtPoint:
+ _objc_msgSend$alertController
+ _objc_msgSend$convertPoint:fromCoordinateSpace:
+ _objc_msgSend$coordinateSpace
+ _objc_msgSend$debugDescription
+ _objc_msgSend$hitTest:withEvent:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$screen
+ _objc_msgSend$set
+ _objc_msgSend$setWithSet:
- GCC_except_table102
- GCC_except_table117
- GCC_except_table122
- GCC_except_table140
- GCC_except_table142
- GCC_except_table156
- GCC_except_table158
- GCC_except_table168
- GCC_except_table169
- GCC_except_table206
- GCC_except_table207
- GCC_except_table214
- GCC_except_table219
- GCC_except_table23
- GCC_except_table230
- GCC_except_table232
- GCC_except_table234
- GCC_except_table34
- GCC_except_table35
- GCC_except_table44
- GCC_except_table53
- GCC_except_table55
- GCC_except_table60
- GCC_except_table62
- GCC_except_table72
- GCC_except_table73
- GCC_except_table74
- GCC_except_table78
- GCC_except_table82
- GCC_except_table83
- GCC_except_table87
- GCC_except_table89
- GCC_except_table91
- GCC_except_table96
- ___73-[SiriPresentationViewController _clearSiriViewControllerWithCompletion:]_block_invoke.247
- ___89-[SiriPresentationViewController handleButtonDownFromButtonIdentifier:timestamp:context:]_block_invoke.216
- ___92-[SiriPresentationViewController _presentationDismissalRequestedWithOptions:withCompletion:]_block_invoke.210
- ___92-[SiriPresentationViewController _presentationDismissalRequestedWithOptions:withCompletion:]_block_invoke.211
- ___99-[SiriPresentationViewController _presentSiriViewControllerWithPresentationOptions:requestOptions:]_block_invoke.175
- __unnamed_array_storage.171
- __unnamed_array_storage.172
- __unnamed_array_storage.201
- __unnamed_array_storage.202
- __unnamed_array_storage.228
- __unnamed_array_storage.229
- __unnamed_array_storage.272
- __unnamed_array_storage.273
- __unnamed_array_storage.85
CStrings:
+ "\x11\x13\x12\x12\x11E\x11\x12\x14\x18\x11"
+ "%s #location Location TCC dismissed: %@"
+ "%s #location Location TCC presented: %@"
+ "%s #location hit testing %lu alerts - touch %@ in content."
+ "-[SiriPresentationViewController _activeTCCHasContentAtPoint:]"
+ "-[SiriPresentationViewController didDismissLocationTCC:]"
+ "-[SiriPresentationViewController didPresentLocationTCC:]"
+ "@\"NSMutableSet\""
+ "B32@0:8{CGPoint=dd}16"
+ "_activeTCCHasContentAtPoint:"
+ "_activeTCCs"
+ "alertController"
+ "convertPoint:fromCoordinateSpace:"
+ "coordinateSpace"
+ "didDismissLocationTCC:"
+ "didPresentLocationTCC:"
+ "hitTest:withEvent:"
+ "removeObject:"
+ "screen"
+ "set"
+ "setWithSet:"
+ "v24@0:8@\"SBAlertItem\"16"
+ "was"
+ "was not"
+ "\xf0!"
- "\x11\x13\x11\x12\x11E\x11\x12\x14\x18\x11"
- "\xf0\x11"

```
