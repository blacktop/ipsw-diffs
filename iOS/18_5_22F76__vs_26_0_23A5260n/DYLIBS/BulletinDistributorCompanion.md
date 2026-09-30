## BulletinDistributorCompanion

> `/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion`

```diff

-380.4.5.0.0
-  __TEXT.__text: 0x7ddac
+381.0.17.0.0
+  __TEXT.__text: 0x80c38
   __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x9d84
-  __TEXT.__cstring: 0x42a3
+  __TEXT.__objc_methlist: 0x9ddc
+  __TEXT.__cstring: 0x4221
   __TEXT.__const: 0x1d0
-  __TEXT.__gcc_except_tab: 0xa10
-  __TEXT.__oslogstring: 0x5128
+  __TEXT.__gcc_except_tab: 0xa28
+  __TEXT.__oslogstring: 0x5237
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1e48
+  __TEXT.__unwind_info: 0x1e50
   __TEXT.__objc_classname: 0x1610
-  __TEXT.__objc_methname: 0x13a3d
+  __TEXT.__objc_methname: 0x13a76
   __TEXT.__objc_methtype: 0x36a0
-  __TEXT.__objc_stubs: 0xcd80
-  __DATA_CONST.__got: 0x980
+  __TEXT.__objc_stubs: 0xce40
+  __DATA_CONST.__got: 0x960
   __DATA_CONST.__const: 0x1e20
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4580
+  __DATA_CONST.__objc_selrefs: 0x45a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x3e0
-  __DATA_CONST.__objc_arraydata: 0x1e8
+  __DATA_CONST.__objc_arraydata: 0x1c8
   __AUTH_CONST.__auth_got: 0x5a0
   __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__cfstring: 0x3ba0
+  __AUTH_CONST.__cfstring: 0x3b80
   __AUTH_CONST.__objc_const: 0x18598
-  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2df0
   __DATA.__objc_ivar: 0xa98
   __DATA.__data: 0x1050

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
-  - /System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit
+  - /System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices
   - /System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E1B2929D-6788-3600-A29D-DA8875BB46D1
-  Functions: 3670
-  Symbols:   12085
-  CStrings:  5358
+  UUID: CDBD5F00-C155-3516-9CD4-1C689F794FEC
+  Functions: 3671
+  Symbols:   12079
+  CStrings:  5362
 
Symbols:
+ -[BLTObjectStore descriptionBuilderWithMultilinePrefix:]
+ -[BLTObjectStore descriptionWithMultilinePrefix:]
+ -[BLTObjectStore description]
+ -[BLTObjectStore objectForKeyedSubscript:]
+ -[BLTObjectStore setObject:forKeyedSubscript:]
+ -[BLTObjectStore succinctDescriptionBuilder]
+ -[BLTObjectStore succinctDescription]
+ _OBJC_CLASS_$_UNSImageProvider
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _objc_msgSend$storeObject:withKey:
- -[BLTObjectStore objectForKey:].cold.1
- -[BLTObjectStore objectForKey:].cold.2
- -[BLTObjectStore objectForKey:].cold.3
- -[BLTObjectStore storeObject:withKey:].cold.2
- -[BLTObjectStore storeObject:withKey:].cold.3
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OBJC_CLASS_$__UNImageProvider
CStrings:
+ "%@ objectForKey: %@ error: %@ unarchiving %@"
+ "%@ objectForKey: %@ exception: %@ loading %@"
+ "%@ objectForKey: %@ not found at %@"
+ "%@ removeObjectForKey: %@ path: %@ error: %@"
+ "%@ storeObject:withKey: archiving/writing failed for: %@ path: %@ with exception: %@"
+ "%@ storeObject:withKey: createDirectoryAtPath failed for: %@ at path: %@ error: %@"
+ "%@ storeObject:withKey: failed to create archiver for: %@ path: %@"
+ "%@ storeObject:withKey: object nil for: %@"
+ "%@ storeObject:withKey: wrote for: %@ path: %@"
+ "_setError"
+ "getBytes:range:"
+ "hasError"
+ "position"
+ "setPosition:"
- "%s: %@ error writing data to %@"
- "%s: %@ exception archiving object"
- "%s: %@ exception loading object from %@"
- "-[BLTObjectStore objectForKey:]"
- "-[BLTObjectStore storeObject:withKey:]"
- "Error initializing unarchiver for object store: %@"
- "Error storing object in object store"
- "can't archive object"
- "com.apple.bulletindistributor.objectstore"
- "englishMessage"
- "object data not found in store"

```
