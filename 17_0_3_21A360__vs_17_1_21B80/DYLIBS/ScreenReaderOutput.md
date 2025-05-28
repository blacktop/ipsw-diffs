## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-344.0.0.0.0
-  __TEXT.__text: 0x399f0
-  __TEXT.__auth_stubs: 0xe90
+346.2.4.0.0
+  __TEXT.__text: 0x39d48
+  __TEXT.__auth_stubs: 0xeb0
   __TEXT.__objc_methlist: 0x3a7c
-  __TEXT.__cstring: 0x32cd
-  __TEXT.__gcc_except_tab: 0x147c
-  __TEXT.__oslogstring: 0xdcb
+  __TEXT.__cstring: 0x32f9
+  __TEXT.__gcc_except_tab: 0x149c
+  __TEXT.__oslogstring: 0xfed
   __TEXT.__const: 0x158
   __TEXT.__ustring: 0x9e
-  __TEXT.__unwind_info: 0x118c
-  __TEXT.__objc_classname: 0x6ba
-  __TEXT.__objc_methname: 0x9fd6
+  __TEXT.__unwind_info: 0x1184
+  __TEXT.__objc_classname: 0x6b9
+  __TEXT.__objc_methname: 0x9fce
   __TEXT.__objc_methtype: 0x1bc6
-  __TEXT.__objc_stubs: 0x81c0
+  __TEXT.__objc_stubs: 0x8160
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x7c0
   __DATA_CONST.__objc_classlist: 0x150

   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x8da8
-  __DATA_CONST.__objc_selrefs: 0x2638
+  __DATA_CONST.__objc_selrefs: 0x2620
   __DATA_CONST.__objc_arraydata: 0x200
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__cfstring: 0x3540
+  __AUTH_CONST.__cfstring: 0x3560
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x768
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x2a8
+  __DATA.__objc_classrefs: 0x298
   __DATA.__objc_superrefs: 0x120
   __DATA.__objc_ivar: 0x594
-  __DATA.__data: 0xb00
+  __DATA.__data: 0xb08
   __DATA.__common: 0x10
   __DATA.__bss: 0x280
   __DATA_DIRTY.__const: 0x388

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1484
-  Symbols:   5559
-  CStrings:  2584
+  Symbols:   5557
+  CStrings:  2590
 
Symbols:
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterPostNotification
+ _OBJC_CLASS_$_BRLTJBrailleStateManager
+ _OBJC_CLASS_$_BRLTJEditableString
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRLTJBrailleStateManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BRLTJBrailleStateManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_BRLTJBrailleStateManagerDelegate
+ __OBJC_PROTOCOL_$_BRLTJBrailleStateManagerDelegate
+ _kSCRODisplayConfigurationChangedNotification
+ _objc_msgSend$setTranslationDelegate:outputMode:inputMode:candidateSelectionLanguage:
- _OBJC_CLASS_$_BRLTJaBrailleStateManager
- _OBJC_CLASS_$_BRLTJaEditableString
- _OBJC_CLASS_$_BRLTJaJaForBrailleTranslationResult
- _OBJC_CLASS_$_BRLTJaTranslator
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRLTJaBrailleStateManagerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRLTJaBrailleStateManagerDelegate
- __OBJC_LABEL_PROTOCOL_$_BRLTJaBrailleStateManagerDelegate
- __OBJC_PROTOCOL_$_BRLTJaBrailleStateManagerDelegate
- _objc_msgSend$initWithTranslationDelegate:
- _objc_msgSend$initWithTranslator:source:
- _objc_msgSend$setTranslator:
- _objc_msgSend$target
CStrings:
+ "+[SCROClient sendCallback:]: client doesn't want callback."
+ "-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'"
+ "-[SCROBrailleClient handleCallback:] Call delegate's config change handler; Delegate wants == %d, isConfigured == %@"
+ "-[SCROBrailleHandler configurationDidChange]: _callbacks.configChanged == %d"
+ "BRLTJBrailleStateManagerDelegate"
+ "Posting SCRODisplayConfigurationChangedNotification"
+ "SCRO Queue is flooded: queue size (%ld) > max size (%d)"
+ "SCRODisplayConfigurationChangedNotification"
+ "[SCROBrailleClient handleCallback:] for key CallbackConnect"
+ "[SCROBrailleClient setDelegate:%@]"
+ "setTranslationDelegate:outputMode:inputMode:candidateSelectionLanguage:"
- "BRLTJaBrailleStateManagerDelegate"
- "initWithTranslationDelegate:"
- "initWithTranslator:source:"
- "setTranslator:"
- "target"

```
