## DurianUpdaterService

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/DurianUpdaterService.xpc/DurianUpdaterService`

```diff

-3056.0.20.0.2
-  __TEXT.__text: 0x36bc
+3056.0.25.0.5
+  __TEXT.__text: 0x386c
   __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0xfe0
+  __TEXT.__objc_stubs: 0x1000
   __TEXT.__objc_methlist: 0x54c
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x509
-  __TEXT.__oslogstring: 0x7aa
-  __TEXT.__objc_methname: 0x143f
+  __TEXT.__cstring: 0x537
+  __TEXT.__oslogstring: 0x907
+  __TEXT.__objc_methname: 0x1445
   __TEXT.__objc_classname: 0xa1
   __TEXT.__objc_methtype: 0x523
   __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__cfstring: 0x720
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x618
-  __DATA.__objc_selrefs: 0x580
+  __DATA.__objc_selrefs: 0x588
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x240

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7160FAE2-60C6-3DB7-ADF5-B9E4EFE3C36A
+  UUID: 121C3614-D125-307C-A07D-4D5875276691
   Functions: 77
-  Symbols:   90
-  CStrings:  422
+  Symbols:   92
+  CStrings:  431
 
Symbols:
+ _InvalidBeaconId
+ _InvalidFwVersion
Functions:
~ sub_100001050 : 680 -> 816
~ sub_100001b24 -> sub_100001bac : 556 -> 852
CStrings:
+ "#durian Bootstrapping with fake accessory; returning NO to stop aud statemachine and end this cycle"
+ "#durian Sending FUD the accessory list with a fake accessory"
+ "#durian candidateBeaconsToUpdate is empty sending FUD the accessory list with a fake accessory"
+ "#durian candidateBeaconsToUpdate is nil sending FUD the accessory list with a fake accessory"
+ "99.99.99"
+ "BADDE700-BADD-BADD-BADD-BADDBADDBADD"
+ "count"

```
