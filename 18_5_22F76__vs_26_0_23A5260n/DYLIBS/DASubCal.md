## DASubCal

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DASubCal`

```diff

-2673.6.1.0.0
-  __TEXT.__text: 0x8890
+2690.0.0.0.0
+  __TEXT.__text: 0x879c
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0xcf0
+  __TEXT.__objc_methlist: 0xce8
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x52a
-  __TEXT.__oslogstring: 0x975
+  __TEXT.__oslogstring: 0x94b
   __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x17a
-  __TEXT.__objc_methname: 0x2b00
+  __TEXT.__objc_methname: 0x2b07
   __TEXT.__objc_methtype: 0xb30
-  __TEXT.__objc_stubs: 0x2700
+  __TEXT.__objc_stubs: 0x2720
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__const: 0x1f0
   __DATA_CONST.__objc_classlist: 0x28

   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x360
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1427277D-97C6-38C9-B6D6-6F3442111A34
-  Functions: 220
-  Symbols:   1045
-  CStrings:  812
+  UUID: 01AEF258-5C3C-32FF-A014-69FC27FDAC70
+  Functions: 219
+  Symbols:   1043
+  CStrings:  811
 
Symbols:
+ _objc_msgSend$setSkipModificationValidation:
- +[SubCalLocalDBHelper _setEventStoreProvider:]
- __eventStoreProvider
Functions:
~ -[SubCalAccount removeDataFromCalendar:forAccountChange:] : 1756 -> 1552
~ +[SubCalLocalDBHelper eventStoreWithClientId:] : 164 -> 140
- +[SubCalLocalDBHelper _setEventStoreProvider:]
CStrings:
+ "setSkipModificationValidation:"
- "Error restoring calendar as read only: %@"
- "_setEventStoreProvider:"

```
