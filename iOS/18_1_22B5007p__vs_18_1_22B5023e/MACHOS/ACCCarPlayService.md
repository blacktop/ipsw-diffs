## ACCCarPlayService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCCarPlayService.xpc/ACCCarPlayService`

```diff

-1008.0.0.502.1
-  __TEXT.__text: 0x325c
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0xfc
-  __TEXT.__cstring: 0x623
-  __TEXT.__const: 0x58
-  __TEXT.__oslogstring: 0x63c
+1025.0.0.0.0
+  __TEXT.__text: 0x3c40
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x340
+  __TEXT.__objc_methlist: 0x11c
+  __TEXT.__cstring: 0x6ea
+  __TEXT.__const: 0x70
+  __TEXT.__oslogstring: 0x7ac
   __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x47c
-  __TEXT.__objc_methtype: 0x233
+  __TEXT.__objc_methname: 0x5b0
+  __TEXT.__objc_methtype: 0x286
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__cfstring: 0x160
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__const: 0x4b8
+  __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x7d8
-  __DATA.__objc_selrefs: 0xd0
+  __DATA.__objc_const: 0x838
+  __DATA.__objc_selrefs: 0x110
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1c8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 75
-  Symbols:   692
-  CStrings:  157
+  Functions: 82
+  Symbols:   764
+  CStrings:  184
 
Symbols:
+ -[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]
+ -[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]
+ -[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:].cold.1
+ -[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:]
+ -[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:]
+ -[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:].cold.1
+ -[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:].cold.1
+ -[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:].cold.2
+ -[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:].cold.3
+ -[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:].cold.4
+ _NSCocoaErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.22
+ __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.22
+ __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.22.cold.1
+ __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.22.cold.1
+ __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.22.cold.2
+ __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.25
+ __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.25
+ __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.25.cold.1
+ __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.25.cold.1
+ __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.25.cold.2
+ __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.29
+ __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.29
+ __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.29.cold.1
+ __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.29.cold.1
+ __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.29.cold.2
+ __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.24
+ __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.24
+ __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.24.cold.1
+ __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.24.cold.1
+ __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.24.cold.2
+ __70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.39
+ __70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.39
+ __70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.39.cold.1
+ __70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.39.cold.1
+ __70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.39.cold.2
+ __70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.cold.1
+ __70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.cold.2
+ __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.27
+ __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.27
+ __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.27.cold.1
+ __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.27.cold.1
+ __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.27.cold.2
+ __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.35
+ __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.35
+ __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.35.cold.1
+ __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.35.cold.1
+ __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.35.cold.2
+ __87-[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:]_block_invoke.cold.1
+ ___70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke
+ ___70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke
+ ___87-[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:]_block_invoke
+ ___87-[ACCCarPlayService carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ __block_literal_global.32
+ __block_literal_global.32
+ __block_literal_global.35
+ __block_literal_global.35
+ __block_literal_global.38
+ __block_literal_global.38
+ __block_literal_global.38
+ __block_literal_global.38
+ __block_literal_global.41
+ __block_literal_global.41
+ __block_literal_global.46
+ __block_literal_global.46
+ __block_literal_global.49
+ __block_literal_global.49
+ _iAPAuthComplete
+ _iAPAuthComplete
+ _iAPAuthStarted
+ _iAPAuthStarted
+ _iAPConnectionStart
+ _iAPConnectionStart
+ _iAPNCMStart
+ _iAPNCMStart
+ _objc_msgSend$carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$eventWithName:type:date:payload:
+ _objc_msgSend$initForSystemDaemon
+ _objc_msgSend$sendConnectionEvent:completion:
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x26
+ _objc_retain_x28
- __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.19
- __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.19
- __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.19.cold.1
- __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.19.cold.1
- __54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.19.cold.2
- __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.22
- __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.22
- __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.22.cold.1
- __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.22.cold.1
- __58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.22.cold.2
- __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.26
- __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.26
- __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.26.cold.1
- __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.26.cold.1
- __60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.26.cold.2
- __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.21
- __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.21
- __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.21.cold.1
- __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.21.cold.1
- __62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.21.cold.2
- __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.24
- __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.24
- __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.24.cold.1
- __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.24.cold.1
- __71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.24.cold.2
- __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.32
- __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.32
- __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.32.cold.1
- __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.32.cold.1
- __78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.32.cold.2
- __block_literal_global.23
- __block_literal_global.23
- __block_literal_global.26
- __block_literal_global.26
- __block_literal_global.29
- __block_literal_global.29
- __block_literal_global.31
- __block_literal_global.31
- __block_literal_global.37
- __block_literal_global.37
CStrings:
+ "CARConnection Time Store timed out!"
+ "CARConnectionEvent"
+ "CARConnectionTimeStore"
+ "CarPlay Connection Event: %!l(MISSING)d, %!l(MISSING)d, %!f(MISSING), %!@(MISSING)"
+ "Failed to link CARConnectionTimeStore"
+ "[#ACCCarPlayService] CARConnectionTimeStore soft link failed"
+ "[#ACCCarPlayService] CarPlay Connection Event: %!s(MISSING) -- %!@(MISSING) at %!@(MISSING), error: %!@(MISSING)"
+ "[#ACCCarPlayService] CarPlay Connection Event: preparing to send event: %!@(MISSING), %!l(MISSING)d, %!@(MISSING)"
+ "[#ACCCarPlayService] sendConnectionEvent() timed out after %!l(MISSING)ldms!"
+ "carPlaySendConnectionTimeEvent:connectionType:eventTime:"
+ "carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithDomain:code:userInfo:"
+ "eventWithName:type:date:payload:"
+ "failed"
+ "failed to send CarPlay Connect event %!@(MISSING)"
+ "iAP Auth Complete"
+ "iAP Auth Start"
+ "iAP Connection Start"
+ "iAP NCM Start"
+ "initForSystemDaemon"
+ "sendConnectionEvent:completion:"
+ "success"
+ "timeIntervalSinceReferenceDate"
+ "v40@0:8q16q24@32"
+ "v48@0:8Q16Q24@\"NSDate\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8Q16Q24@32@?40"

```
