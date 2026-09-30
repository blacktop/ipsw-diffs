## DataDetectorsUI

> `/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI`

```diff

-590.0.0.0.0
-  __TEXT.__text: 0x52a04
+596.0.0.0.0
+  __TEXT.__text: 0x52abc
   __TEXT.__auth_stubs: 0xec0
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x1400
-  __TEXT.__objc_methlist: 0x4c40
+  __TEXT.__objc_methlist: 0x4c50
   __TEXT.__const: 0x270
   __TEXT.__oslogstring: 0x2198
   __TEXT.__gcc_except_tab: 0xd68

   __TEXT.__swift5_fieldmd: 0x54
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1438
+  __TEXT.__unwind_info: 0x1440
   __TEXT.__objc_classname: 0xc13
-  __TEXT.__objc_methname: 0xbb7b
+  __TEXT.__objc_methname: 0xbbba
   __TEXT.__objc_methtype: 0x36d5
-  __TEXT.__objc_stubs: 0xaba0
+  __TEXT.__objc_stubs: 0xabe0
   __DATA_CONST.__got: 0xa80
   __DATA_CONST.__const: 0xdf0
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32f8
+  __DATA_CONST.__objc_selrefs: 0x3308
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7B5D0207-3CC6-3AE2-97B7-674718047B9D
-  Functions: 1847
-  Symbols:   7103
-  CStrings:  4288
+  UUID: 64EF4E72-26E2-3FD5-A717-10554AAC4A1E
+  Functions: 1849
+  Symbols:   7109
+  CStrings:  4290
 
Symbols:
+ -[DDCallKitAudioAction _senderIdentityInitialForSymbolName]
+ -[DDFlightAction updateBarButtonItems:forViewController:]
+ ___59-[DDCallKitAudioAction _senderIdentityInitialForSymbolName]_block_invoke
+ _objc_msgSend$_senderIdentityInitialForSymbolName
+ _objc_msgSend$punctuationCharacterSet
+ _objc_msgSend$updateBarButtonItems:forViewController:
- -[DDCallKitAudioAction _senderIdentityInitialForSymbolName:]
- ___60-[DDCallKitAudioAction _senderIdentityInitialForSymbolName:]_block_invoke
- _objc_msgSend$_senderIdentityInitialForSymbolName:
Functions:
~ -[DDRemoteHeaderView showLoadingView] : 560 -> 548
~ -[DDFlightAction prepareViewControllerForActionController:] : 312 -> 296
~ -[DDFlightAction viewController] : 456 -> 444
+ -[DDFlightAction updateBarButtonItems:forViewController:]
~ -[DDActionController actionsForURL:result:enclosingResult:context:] : 6400 -> 6336
~ _OUTLINED_FUNCTION_0 : 20 -> 16
~ _OUTLINED_FUNCTION_3 : 32 -> 12
+ _OUTLINED_FUNCTION_4
~ +[DDRevealBridge updatedTextInteractionMenuElements:withRVItem:view:context:] : 4232 -> 4248
~ +[DDTextMessageAction isShowMessageURL:] : 536 -> 552
~ -[DDTextMessageAction notificationURL] : 1352 -> 1376
~ +[DDTextMessageAction actionsWithURL:result:context:] : 1040 -> 1052
~ -[DDTelephoneNumberAction initWithURL:result:context:] : 784 -> 804
~ -[DDCallKitAudioAction _nonSymbolBadgeForSenderIdentityCompact:] : 724 -> 720
~ -[DDPersonAction _menuActionsForBusinessWithNumber:] : 916 -> 936
~ -[NSURL dd_phoneNumberFromTelSchemeAndExtractBody:serviceID:suggestions:] : 2404 -> 2480
~ -[NSURL dd_rdarLinkFromTelScheme] : 304 -> 308
CStrings:
+ "_senderIdentityInitialForSymbolName"
+ "punctuationCharacterSet"
+ "updateBarButtonItems:forViewController:"
- "_senderIdentityInitialForSymbolName:"

```
