## AppleEmbeddedDisplayServices

> `/System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices`

```diff

-165.0.0.0.0
-  __TEXT.__text: 0xc50
-  __TEXT.__auth_stubs: 0x260
+167.120.3.0.1
+  __TEXT.__text: 0x15d4
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xed
-  __TEXT.__oslogstring: 0x50
-  __TEXT.__unwind_info: 0x84
+  __TEXT.__cstring: 0x109
+  __TEXT.__oslogstring: 0x2a1
+  __TEXT.__unwind_info: 0x9c
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0xbf
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x30
+  __TEXT.__objc_methname: 0x12b
+  __TEXT.__objc_stubs: 0x180
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
-  __DATA_CONST.__objc_classrefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__auth_got: 0x148
   __DATA.__data: 0x8
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/AFKUser.framework/AFKUser
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 648955A6-CFDB-31D1-858C-51D6EC18002D
-  Functions: 23
-  Symbols:   109
-  CStrings:  28
+  UUID: 3A5F88CF-8ACB-36F3-AD99-1E856F2B3017
+  Functions: 30
+  Symbols:   130
+  CStrings:  45
 
Symbols:
+ _BIMUpdaterEndUpdate
+ _BIMUpdaterStartUpdate
+ _BIMUpdaterStartUpdate.cold.1
+ _BIMUpdaterStartUpdate.cold.2
+ _BIMUpdaterStartUpdate.cold.3
+ _OBJC_CLASS_$_CADisplay
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __os_crash_msg
+ __os_log_default
+ __os_log_send_and_compose_impl
+ _objc_msgSend$acquireAndWaitForPowerOn
+ _objc_msgSend$createPowerAssertionWithReason:identifier:
+ _objc_msgSend$invalidate
+ _objc_msgSend$mainDisplay
+ _objc_msgSend$stateControl
+ _objc_release_x22
+ _objc_retain_x8
- _BIMUpdaterCancel.cold.1
- _BIMUpdaterRead.cold.1
- _BIMUpdaterWrite.cold.1
- __os_assert_log
- __os_crash
CStrings:
+ "BIM Display Power Assertion"
+ "acquireAndWaitForPowerOn"
+ "assertion failure: \"!updater->_activated\" -> %lld"
+ "assertion failure: \"CFGetTypeID(cf) == BIMUpdaterGetTypeID()\" -> %lld"
+ "assertion failure: \"control\" -> %lld"
+ "assertion failure: \"display\" -> %lld"
+ "assertion failure: \"updater\" -> %lld"
+ "assertion failure: \"updater->_cancelled\" -> %lld"
+ "assertion failure: \"updater->_displayPowerAssertion\" -> %lld"
+ "assertion failure: \"updater->_queue && updater->_connectCB && updater->_cancelCB && updater->_eepromNotification && updater->_afkNotification\" -> %lld"
+ "assertion failure: activated:%d cancelled:%d"
+ "assertion failure: activated:%d cancelled:%d started:%d"
+ "createPowerAssertionWithReason:identifier:"
+ "invalidate"
+ "mainDisplay"
+ "stateControl"

```
