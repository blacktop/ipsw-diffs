## libTelephonyUtilDynamic.dylib

> `/usr/lib/libTelephonyUtilDynamic.dylib`

```diff

 6575.0.0.0.0
-  __TEXT.__text: 0x84060
+  __TEXT.__text: 0x834f4
   __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x2a4
   __TEXT.__const: 0xa138
-  __TEXT.__cstring: 0x3725
-  __TEXT.__gcc_except_tab: 0x8b6c
-  __TEXT.__oslogstring: 0x21eb
-  __TEXT.__unwind_info: 0x4a38
+  __TEXT.__cstring: 0x369a
+  __TEXT.__gcc_except_tab: 0x8b20
+  __TEXT.__oslogstring: 0x1d5b
+  __TEXT.__unwind_info: 0x4a18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__weak_got: 0x20
   __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__got: 0x2f0
   __AUTH_CONST.__const: 0x6dc8
-  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__objc_const: 0x2e8
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0xc70
+  __AUTH_CONST.__auth_got: 0xc60
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x4

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3374
-  Symbols:   5249
-  CStrings:  732
+  Functions: 3371
+  Symbols:   5245
+  CStrings:  709
 
Symbols:
+ GCC_except_table109
+ GCC_except_table115
+ GCC_except_table134
+ _sTelephonyHardwareConfig
- _CFTypeToCString
- _CFUserNotificationCreate
- __ZN3ctu2cf6insertIPK10__CFStringS4_EEbP14__CFDictionaryT_T0_PK13__CFAllocator
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationDefaultButtonTitleKey
- _os_parse_boot_arg_string
- _performMGQueryReturnsString
CStrings:
- "/private/var/wireless/Library/Preferences/com.apple.telephony.overrides.plist"
- "BasebandChipset"
- "Did not find a hardware model override string"
- "Did not override hardware model string based on NVRAM boot args"
- "Failed to convert retrieved CFStringRef to UTF-8 C-string"
- "Failed to convert type returned by MobileGestalt to a C-string."
- "Failed to get baseband chipset from MobileGestalt and cache was empty; proceeding with unknown radio"
- "Failed to perform MobileGestalt query"
- "Failed to set Telephony hardware model info according to hardware model override string '%s'"
- "Failed while trying to query MobileGestalt"
- "HardwareModelString"
- "Invalid parameter"
- "OK"
- "Overrode and cached baseband chipset to enum value %d"
- "Passed buf of length %ld is not long enough for string of size %ld (incl. null terminator)"
- "Read baseband chipset %s from MobileGestalt"
- "Successfully overrode hardware model string to %s based on NVRAM boot args"
- "Successfully read %s to buffer from MobileGestalt"
- "Successfully set Telephony hardware model info according to hardware model override string '%s'"
- "Using cached baseband chipset enum value %d, originally from MobileGestalt"
- "Value %s from MobileGestalt does not match any supported baseband chipset; proceeding with unknown radio"
- "Value provided has type id %lu; it is not a CFString"
- "telephony-hw-override"
```
