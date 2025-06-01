## libSESShared.dylib

> `/usr/lib/libSESShared.dylib`

```diff

-43.2.0.0.0
-  __TEXT.__text: 0xbcd4
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x7a4
-  __TEXT.__cstring: 0xa75
-  __TEXT.__oslogstring: 0x62d
+44.24.0.0.0
+  __TEXT.__text: 0xc998
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x80c
+  __TEXT.__cstring: 0xb65
+  __TEXT.__oslogstring: 0x6a3
   __TEXT.__const: 0xa10
   __TEXT.__gcc_except_tab: 0xd0
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x330
-  __TEXT.__objc_classname: 0x10a
-  __TEXT.__objc_methname: 0x1291
-  __TEXT.__objc_methtype: 0x4b8
-  __TEXT.__objc_stubs: 0xf60
+  __TEXT.__unwind_info: 0x354
+  __TEXT.__objc_classname: 0x11f
+  __TEXT.__objc_methname: 0x1393
+  __TEXT.__objc_methtype: 0x4cf
+  __TEXT.__objc_stubs: 0xfe0
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x2b8
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6a8
-  __DATA_CONST.__objc_selrefs: 0x670
+  __DATA_CONST.__objc_const: 0x6d0
+  __DATA_CONST.__objc_selrefs: 0x6c0
+  __DATA_CONST.__objc_classrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__cfstring: 0xf20
+  __AUTH_CONST.__cfstring: 0x1120
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x380
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0x8c
+  __AUTH_CONST.__auth_got: 0x388
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x90
   __DATA.__data: 0x8
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__const: 0xc0
+  __DATA_DIRTY.__const: 0xe0
   __DATA_DIRTY.__objc_const: 0x648
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 09ED98B8-153D-35B5-A9DB-EF80B93E6C60
-  Functions: 238
-  Symbols:   930
-  CStrings:  662
+  UUID: E011B087-1A87-390B-BDD6-E1EC24386BEF
+  Functions: 250
+  Symbols:   969
+  CStrings:  714
 
Symbols:
+ +[CertificationLogging bleLogMessageReceived:peerUUID:]
+ +[CertificationLogging bleLogMessageSent:peerUUID:]
+ +[CertificationLogging bleLogRSSI:peerUUID:]
+ +[CertificationLogging bleLogVehicleConnected:]
+ +[CertificationLogging bleLogVehicleDisconnected:]
+ +[CertificationLogging getInstance]
+ +[CertificationLogging logEncryptedAPDU:decrypted:]
+ +[NSUUID(Data) ses_withData:]
+ +[NSUUID(Data) ses_withUUIDString:]
+ -[CertificationLogging .cxx_destruct]
+ -[CertificationLogging logEvent:message:peerUUID:]
+ -[NSUUID(Data) ses_toData]
+ _OBJC_CLASS_$_CertificationLogging
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_IVAR_$_CertificationLogging._log
+ _OBJC_METACLASS_$_CertificationLogging
+ __OBJC_$_CLASS_METHODS_CertificationLogging
+ __OBJC_$_INSTANCE_METHODS_CertificationLogging
+ __OBJC_$_INSTANCE_VARIABLES_CertificationLogging
+ __OBJC_CLASS_RO_$_CertificationLogging
+ __OBJC_METACLASS_RO_$_CertificationLogging
+ ___35+[CertificationLogging getInstance]_block_invoke
+ ___50-[CertificationLogging logEvent:message:peerUUID:]_block_invoke
+ _objc_msgSend$UUIDString
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$isValidJSONObject:
+ _objc_opt_self
- +[NSUUID(Data) withData:]
- +[NSUUID(Data) withUUIDString:]
- -[NSUUID(Data) toData]
CStrings:
+ "%@"
+ ".GlobalPreferences"
+ "@\"NSObject<OS_os_log>\""
+ "CertificationLogging"
+ "Failed to serialize object %@ %@"
+ "Invalid JSON object %@"
+ "UUIDString"
+ "Unknown event type %lu"
+ "Wrong payload for event type %lu %@"
+ "_log"
+ "bleLogMessageReceived:peerUUID:"
+ "bleLogMessageSent:peerUUID:"
+ "bleLogRSSI:peerUUID:"
+ "bleLogVehicleConnected:"
+ "bleLogVehicleDisconnected:"
+ "boolForKey:"
+ "com.apple.CarKeysTests.enableCertificationLogging"
+ "com.apple.certification"
+ "connect"
+ "dataWithJSONObject:options:error:"
+ "dck_decrypted"
+ "dck_message"
+ "decrypted_payload"
+ "digitalCarKey"
+ "direction"
+ "disconnect"
+ "event"
+ "in"
+ "isValidJSONObject:"
+ "logEncryptedAPDU:decrypted:"
+ "log_type"
+ "out"
+ "payload"
+ "raw_payload"
+ "rssi"
+ "ses_toData"
+ "ses_withData:"
+ "ses_withUUIDString:"
+ "vehicle_uuid"
- "toData"
- "withData:"
- "withUUIDString:"

```
