## MessagesFlowDelegatePlugin

> `/System/Library/AccessibilityBundles/MessagesFlowDelegatePlugin.axbundle/MessagesFlowDelegatePlugin`

```diff

-3005.25.0.0.0
-  __TEXT.__text: 0x5c0
-  __TEXT.__auth_stubs: 0x150
+3005.27.0.0.0
+  __TEXT.__text: 0x778
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0xb9
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__const: 0x8
+  __TEXT.__oslogstring: 0x77
+  __TEXT.__unwind_info: 0x80
   __TEXT.__objc_classname: 0x78
-  __TEXT.__objc_methname: 0x26b
+  __TEXT.__objc_methname: 0x290
   __TEXT.__objc_methtype: 0x2e
-  __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x38
+  __TEXT.__objc_stubs: 0x320
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe0
+  __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb0
+  __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F90FB9E3-6F60-313C-87FF-AE17C8331896
-  Functions: 10
-  Symbols:   98
-  CStrings:  50
+  UUID: D7218AA0-7E71-38C0-A6D0-AD5A683D8D6B
+  Functions: 11
+  Symbols:   112
+  CStrings:  54
 
Symbols:
+ -[INSendMessageIntentAccessibility setRecipients:].cold.1
+ _CLFCommunicationLimitContacts
+ _CLFCommunicationLimitEveryone
+ _CLFCommunicationLimitSelectedContacts
+ _OBJC_CLASS_$_CLFLog
+ _OBJC_CLASS_$_CLFMessagesSettings
+ __os_log_fault_impl
+ __os_log_impl
+ _objc_msgSend$commonLog
+ _objc_msgSend$outgoingCommunicationLimit
+ _objc_release_x25
+ _objc_release_x27
+ _objc_retain_x27
+ _os_log_type_enabled
- _objc_retain_x23
Functions:
~ -[INSendMessageIntentAccessibility setRecipients:] : 584 -> 904
CStrings:
+ "Not sending message via Siri to unallowed recipient."
+ "Unhandled outgoing communication limit in INSendMessageIntent: %@"
+ "commonLog"
+ "outgoingCommunicationLimit"

```
