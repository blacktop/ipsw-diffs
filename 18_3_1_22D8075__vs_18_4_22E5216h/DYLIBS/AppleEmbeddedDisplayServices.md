## AppleEmbeddedDisplayServices

> `/System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices`

```diff

 179.0.0.0.0
-  __TEXT.__text: 0x1600
-  __TEXT.__auth_stubs: 0x280
+  __TEXT.__text: 0x1680
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0x109
   __TEXT.__oslogstring: 0x2a1

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_dictobj: 0x78

   - /System/Library/PrivateFrameworks/AFKUser.framework/AFKUser
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 30
-  Symbols:   83
+  Functions: 32
+  Symbols:   84
   CStrings:  38
 
Symbols:
- _objc_release_x22
- _objc_release_x25
- _objc_release_x27
CStrings:
+ "assertion failure: \"!updater->_activated\" -> %llu"
+ "assertion failure: \"CFGetTypeID(cf) == BIMUpdaterGetTypeID()\" -> %llu"
+ "assertion failure: \"control\" -> %llu"
+ "assertion failure: \"display\" -> %llu"
+ "assertion failure: \"updater\" -> %llu"
+ "assertion failure: \"updater->_cancelled\" -> %llu"
+ "assertion failure: \"updater->_displayPowerAssertion\" -> %llu"
+ "assertion failure: \"updater->_queue && updater->_connectCB && updater->_cancelCB && updater->_eepromNotification && updater->_afkNotification\" -> %llu"
- "assertion failure: \"!updater->_activated\" -> %lld"
- "assertion failure: \"CFGetTypeID(cf) == BIMUpdaterGetTypeID()\" -> %lld"
- "assertion failure: \"control\" -> %lld"
- "assertion failure: \"display\" -> %lld"
- "assertion failure: \"updater\" -> %lld"
- "assertion failure: \"updater->_cancelled\" -> %lld"
- "assertion failure: \"updater->_displayPowerAssertion\" -> %lld"
- "assertion failure: \"updater->_queue && updater->_connectCB && updater->_cancelCB && updater->_eepromNotification && updater->_afkNotification\" -> %lld"

```
