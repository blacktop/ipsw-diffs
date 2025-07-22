## ExternalAccessory

> `/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`

```diff

-454.0.0.0.0
-  __TEXT.__text: 0xdf50
+456.0.0.0.0
+  __TEXT.__text: 0xe424
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x15ac
-  __TEXT.__cstring: 0x5368
+  __TEXT.__objc_methlist: 0x15ec
+  __TEXT.__cstring: 0x53b1
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x8c
   __TEXT.__dlopen_cstrs: 0x5c
   __TEXT.__unwind_info: 0x490
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x4095
+  __TEXT.__objc_methname: 0x4178
   __TEXT.__objc_methtype: 0x78e
-  __TEXT.__objc_stubs: 0x2a40
+  __TEXT.__objc_stubs: 0x2ae0
   __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x7d8
+  __DATA_CONST.__const: 0x7e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf80
+  __DATA_CONST.__objc_selrefs: 0xfb0
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x3520
+  __AUTH_CONST.__cfstring: 0x3560
   __AUTH_CONST.__objc_const: 0x1f50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_ivar: 0x1d4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2809E7BD-B1A6-3EFE-908A-E6F2C415822E
-  Functions: 463
-  Symbols:   1987
-  CStrings:  1687
+  UUID: DDAC7EC8-B919-37D9-9D99-31C586F84225
+  Functions: 468
+  Symbols:   2003
+  CStrings:  1697
 
Symbols:
+ -[EAAccessoryManager _ephemerisURLAvailableForAccessory:]
+ -[EAAccessoryManager _gpsTimeRequestedForAccessory:]
+ -[EAAccessoryManager _locationNmeaDataAvailableForAccessory:]
+ -[EAAccessoryManager _locationPointDataAvailableForAccessory:]
+ -[EAAccessoryManager _nmeaFilteringSupportChangedForAccessory:]
+ _EAAccessoryNMEASentenceFromAccessoryKey
+ _objc_msgSend$_ephemerisURLAvailableForAccessory:
+ _objc_msgSend$_gpsTimeRequestedForAccessory:
+ _objc_msgSend$_locationNmeaDataAvailableForAccessory:
+ _objc_msgSend$_locationPointDataAvailableForAccessory:
+ _objc_msgSend$_nmeaFilteringSupportChangedForAccessory:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$_locationNmeaDataAvailable:
CStrings:
+ "EAAccessoryNMEASentenceFromAccessoryKey"
+ "[#Location] send %@, userInfo %@"
+ "_ephemerisURLAvailableForAccessory:"
+ "_gpsTimeRequestedForAccessory:"
+ "_locationNmeaDataAvailableForAccessory:"
+ "_locationPointDataAvailableForAccessory:"
+ "_nmeaFilteringSupportChangedForAccessory:"
+ "dictionaryWithObjects:forKeys:count:"

```
