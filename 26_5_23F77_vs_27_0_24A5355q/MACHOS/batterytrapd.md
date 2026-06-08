## batterytrapd

> `/usr/libexec/batterytrapd`

```diff

-22.0.0.0.0
-  __TEXT.__text: 0x1d18
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0x620
-  __TEXT.__objc_methlist: 0x1cc
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x552
-  __TEXT.__cstring: 0x25d
-  __TEXT.__objc_methname: 0x417
-  __TEXT.__objc_classname: 0x24
-  __TEXT.__objc_methtype: 0xc7
+26.0.0.0.0
+  __TEXT.__text: 0x1ea8
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x720
+  __TEXT.__objc_methlist: 0x1d4
+  __TEXT.__const: 0x38
+  __TEXT.__oslogstring: 0x51c
+  __TEXT.__cstring: 0x38b
+  __TEXT.__objc_methname: 0x4bc
+  __TEXT.__objc_classname: 0x1e
+  __TEXT.__objc_methtype: 0xb0
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x88
-  __DATA_CONST.__cfstring: 0x2a0
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x2c8
-  __DATA.__objc_selrefs: 0x1d8
-  __DATA.__objc_ivar: 0x20
+  __DATA_CONST.__objc_arraydata: 0x518
+  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x90
+  __DATA.__objc_const: 0x260
+  __DATA.__objc_selrefs: 0x218
+  __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: EED9187D-C9E5-3348-BD2D-96092A615F06
-  Functions: 71
-  Symbols:   79
-  CStrings:  163
+  UUID: 1F6F55DB-A0A7-367A-A531-5036ABB5D54A
+  Functions: 70
+  Symbols:   84
+  CStrings:  288
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSConstantArray
+ _dispatch_once
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x1
+ _objc_release_x22
+ _objc_release_x23
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_alloc
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
CStrings:
+ "%lu"
+ "AppleLanguagePreferencesChangedNotification"
+ "Clearing all variables"
+ "Language %@ -> enum %lu"
+ "LanguageChangedNotification"
+ "No supported language matched preferences: %@, will default to en"
+ "Received XPC launch event com.apple.iokit.matching"
+ "Received XPC launch event com.apple.notifyd.matching: %s, paired: %d"
+ "Writing all variables"
+ "Writing non-ALPM variables"
+ "_handleLanguageChange"
+ "ar"
+ "bg"
+ "bn"
+ "ca"
+ "com.apple.notifyd.matching notification from AppleLanguagePreferencesChangedNotification"
+ "cs"
+ "da"
+ "de"
+ "el"
+ "en"
+ "en-AU"
+ "en-GB"
+ "en-IN"
+ "es"
+ "es-419"
+ "es-US"
+ "fi"
+ "firstObject"
+ "fr"
+ "fr-CA"
+ "gu"
+ "he"
+ "hi"
+ "hr"
+ "hu"
+ "id"
+ "indexOfObject:"
+ "isPaired"
+ "it"
+ "ja"
+ "kk"
+ "kn"
+ "ko"
+ "lt"
+ "ml"
+ "mr"
+ "ms"
+ "nl"
+ "no"
+ "or"
+ "pa"
+ "pl"
+ "preferredLanguages"
+ "preferredLocalizationsFromArray:forPreferences:"
+ "pt-BR"
+ "pt-PT"
+ "readCurrentLanguage"
+ "ro"
+ "ru"
+ "setUserLanguage"
+ "sk"
+ "sl"
+ "sv"
+ "ta"
+ "te"
+ "th"
+ "tr"
+ "uk"
+ "ur"
+ "user_language_enum"
+ "v8@?0"
+ "vi"
+ "writeNonALPMVariables"
+ "zh-CN"
+ "zh-HK"
+ "zh-TW"
- "@\"NSObject<OS_os_log>\""
- "Clearing all variables\n"
- "Received XPC launch event com.apple.iokit.matching for batterytrapd"
- "Received XPC launch event com.apple.notifyd.matching AppleTimePreferencesChangedNotification for batterytrapd"
- "Received XPC launch event com.apple.notifyd.matching SignificantTimeChangeNotification for batterytrapd"
- "Received XPC launch event com.apple.notifyd.matching com.apple.system.timezone for batterytrapd"
- "Writing all variables\n"
- "initWithLog:"
- "logs"

```
