## EmergencyAlerts

> `/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts`

```diff

-195.0.0.0.0
-  __TEXT.__text: 0x3610
+197.0.0.0.0
+  __TEXT.__text: 0x37b0
   __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_methlist: 0x178
-  __TEXT.__const: 0x80
+  __TEXT.__const: 0x88
   __TEXT.__cstring: 0x474
-  __TEXT.__oslogstring: 0x618
+  __TEXT.__oslogstring: 0x687
   __TEXT.__unwind_info: 0x108
   __TEXT.__objc_classname: 0x4b
-  __TEXT.__objc_methname: 0xb72
+  __TEXT.__objc_methname: 0xb8c
   __TEXT.__objc_methtype: 0xf8
-  __TEXT.__objc_stubs: 0xde0
+  __TEXT.__objc_stubs: 0xe00
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x240
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a0
+  __DATA_CONST.__objc_selrefs: 0x3a8
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x60

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DAD9D0D-BC44-321B-981F-816027E5D26E
+  UUID: 03D6CB5D-68CE-344A-B0C4-E6C6625D0A41
   Functions: 66
-  Symbols:   401
-  CStrings:  307
+  Symbols:   402
+  CStrings:  311
 
Symbols:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
- _objc_msgSend$alphanumericCharacterSet
Functions:
~ -[UNMutableNotificationContent(EmergencyAlerts) ea_setPropertiesForCellBroadcastMessage:withActivePhoneCall:] : 2864 -> 3280
CStrings:
+ "Post trimming message: %@"
+ "Trimming leading whitespace to index %lu"
+ "Trimming trailing whitespace from index %lu"
+ "substringToIndex:"
+ "whitespaceAndNewlineCharacterSet"
- "alphanumericCharacterSet"

```
