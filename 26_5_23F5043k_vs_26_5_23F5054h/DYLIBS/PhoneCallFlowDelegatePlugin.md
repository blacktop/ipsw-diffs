## PhoneCallFlowDelegatePlugin

> `/System/Library/AccessibilityBundles/PhoneCallFlowDelegatePlugin.axbundle/PhoneCallFlowDelegatePlugin`

```diff

-3005.25.0.0.0
-  __TEXT.__text: 0x604
-  __TEXT.__auth_stubs: 0x150
+3005.27.0.0.0
+  __TEXT.__text: 0x7bc
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0xc8
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__const: 0x8
+  __TEXT.__oslogstring: 0x71
+  __TEXT.__unwind_info: 0x88
   __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x29a
+  __TEXT.__objc_methname: 0x2bf
   __TEXT.__objc_methtype: 0x2e
-  __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x38
+  __TEXT.__objc_stubs: 0x340
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe8
+  __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb0
+  __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF156321-7B00-313B-803D-77645C697903
-  Functions: 10
-  Symbols:   99
-  CStrings:  55
+  UUID: 075BF860-A195-3122-B3D3-5706AA9899B1
+  Functions: 11
+  Symbols:   113
+  CStrings:  59
 
Symbols:
+ -[INStartCallIntentAccessibility setContacts:].cold.1
+ _CLFCommunicationLimitContacts
+ _CLFCommunicationLimitEveryone
+ _CLFCommunicationLimitSelectedContacts
+ _OBJC_CLASS_$_CLFLog
+ _OBJC_CLASS_$_CLFPhoneFaceTimeSettings
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
~ -[INStartCallIntentAccessibility setContacts:] : 584 -> 904
CStrings:
+ "Not starting call via Siri to unallowed contact."
+ "Unhandled outgoing communication limit in INStartCallIntent: %@"
+ "commonLog"
+ "outgoingCommunicationLimit"

```
