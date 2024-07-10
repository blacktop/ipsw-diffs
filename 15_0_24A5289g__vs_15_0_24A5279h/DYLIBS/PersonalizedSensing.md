## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/Versions/A/PersonalizedSensing`

```diff

-186.0.0.0.0
-  __TEXT.__text: 0xa1a4
+183.0.0.0.0
+  __TEXT.__text: 0x969c
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0xf50
+  __TEXT.__objc_methlist: 0xd68
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0xc4f
-  __TEXT.__oslogstring: 0x4b9
+  __TEXT.__cstring: 0xb59
+  __TEXT.__oslogstring: 0x49f
   __TEXT.__gcc_except_tab: 0x1ac
-  __TEXT.__unwind_info: 0x3f0
-  __TEXT.__objc_classname: 0x21e
-  __TEXT.__objc_methname: 0x2136
-  __TEXT.__objc_methtype: 0x25e
-  __TEXT.__objc_stubs: 0x1d60
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__unwind_info: 0x3a0
+  __TEXT.__objc_classname: 0x1d4
+  __TEXT.__objc_methname: 0x1edb
+  __TEXT.__objc_methtype: 0x253
+  __TEXT.__objc_stubs: 0x1bc0
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x958
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_selrefs: 0x8d0
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x1c28
+  __AUTH_CONST.__cfstring: 0xde0
+  __AUTH_CONST.__objc_const: 0x18b0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x100
-  __DATA.__data: 0x1b0
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0xec
+  __DATA.__data: 0x198
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 355
-  Symbols:   1002
-  CStrings:  148
+  Functions: 320
+  Symbols:   913
+  CStrings:  132
 
Symbols:
+ +[NSDate(MOExtensions) dayNameFormatter]
+ ___40+[NSDate(MOExtensions) dayNameFormatter]_block_invoke
+ __block_literal_global.13
+ __block_literal_global.15
+ _objc_msgSend$dayNameFormatter
+ _objc_msgSend$setLocalizedDateFormatFromTemplate:
+ dayNameFormatter.dateFormatter
+ dayNameFormatter.onceToken
- +[MOContextMusicMetaData supportsSecureCoding]
- +[MOContextStringUpdateOptions supportsSecureCoding]
- +[MOContextTimeMetaData supportsSecureCoding]
- +[MOPersonalizedSensingServiceManager generatePromptSuggestionWithTemplate:context:options:]
- +[NSDate(MOExtensions) dayNameFormatterInEnglish]
- -[MOContext associatedMusic]
- -[MOContext associatedTime]
- -[MOContext setAssociatedMusic:]
- -[MOContext setAssociatedTime:]
- -[MOContextContactMetaData description]
- -[MOContextContactMetaData initWithContactName:]
- -[MOContextLocationMetaData description]
- -[MOContextLocationMetaData initWithPlace:city:]
- -[MOContextMusicMetaData .cxx_destruct]
- -[MOContextMusicMetaData copyWithZone:]
- -[MOContextMusicMetaData description]
- -[MOContextMusicMetaData encodeWithCoder:]
- -[MOContextMusicMetaData initWithCoder:]
- -[MOContextMusicMetaData initWithMusicString:]
- -[MOContextMusicMetaData init]
- -[MOContextMusicMetaData musicString]
- -[MOContextStringUpdateOptions appendMusicString]
- -[MOContextStringUpdateOptions copyWithZone:]
- -[MOContextStringUpdateOptions encodeWithCoder:]
- -[MOContextStringUpdateOptions initWithAppendMusicString:]
- -[MOContextStringUpdateOptions initWithCoder:]
- -[MOContextStringUpdateOptions init]
- -[MOContextStringUpdateOptions setAppendMusicString:]
- -[MOContextTimeMetaData .cxx_destruct]
- -[MOContextTimeMetaData copyWithZone:]
- -[MOContextTimeMetaData description]
- -[MOContextTimeMetaData encodeWithCoder:]
- -[MOContextTimeMetaData initWithCoder:]
- -[MOContextTimeMetaData initWithTimeReferenceString:]
- -[MOContextTimeMetaData init]
- -[MOContextTimeMetaData timeReferenceString]
- OBJC_IVAR_$_MOContext._associatedMusic
- OBJC_IVAR_$_MOContext._associatedTime
- OBJC_IVAR_$_MOContextMusicMetaData._musicString
- OBJC_IVAR_$_MOContextStringUpdateOptions._appendMusicString
- OBJC_IVAR_$_MOContextTimeMetaData._timeReferenceString
- _MOLogFacilityNotificationManager
- _OBJC_CLASS_$_MOContextMusicMetaData
- _OBJC_CLASS_$_MOContextStringUpdateOptions
- _OBJC_CLASS_$_MOContextTimeMetaData
- _OBJC_METACLASS_$_MOContextMusicMetaData
- _OBJC_METACLASS_$_MOContextStringUpdateOptions
- _OBJC_METACLASS_$_MOContextTimeMetaData
- __OBJC_$_CLASS_METHODS_MOContextMusicMetaData
- __OBJC_$_CLASS_METHODS_MOContextStringUpdateOptions
- __OBJC_$_CLASS_METHODS_MOContextTimeMetaData
- __OBJC_$_CLASS_PROP_LIST_MOContextMusicMetaData
- __OBJC_$_CLASS_PROP_LIST_MOContextStringUpdateOptions
- __OBJC_$_CLASS_PROP_LIST_MOContextTimeMetaData
- __OBJC_$_INSTANCE_METHODS_MOContextMusicMetaData
- __OBJC_$_INSTANCE_METHODS_MOContextStringUpdateOptions
- __OBJC_$_INSTANCE_METHODS_MOContextTimeMetaData
- __OBJC_$_INSTANCE_VARIABLES_MOContextMusicMetaData
- __OBJC_$_INSTANCE_VARIABLES_MOContextStringUpdateOptions
- __OBJC_$_INSTANCE_VARIABLES_MOContextTimeMetaData
- __OBJC_$_PROP_LIST_MOContextMusicMetaData
- __OBJC_$_PROP_LIST_MOContextStringUpdateOptions
- __OBJC_$_PROP_LIST_MOContextTimeMetaData
- __OBJC_CLASS_PROTOCOLS_$_MOContextMusicMetaData
- __OBJC_CLASS_PROTOCOLS_$_MOContextStringUpdateOptions
- __OBJC_CLASS_PROTOCOLS_$_MOContextTimeMetaData
- __OBJC_CLASS_RO_$_MOContextMusicMetaData
- __OBJC_CLASS_RO_$_MOContextStringUpdateOptions
- __OBJC_CLASS_RO_$_MOContextTimeMetaData
- __OBJC_METACLASS_RO_$_MOContextMusicMetaData
- __OBJC_METACLASS_RO_$_MOContextStringUpdateOptions
- __OBJC_METACLASS_RO_$_MOContextTimeMetaData
- ___49+[NSDate(MOExtensions) dayNameFormatterInEnglish]_block_invoke
- __block_literal_global.16
- __block_literal_global.18
- _kMOTemplateJSONCityNameDefaultValue
- _kMOTemplateJSONPersonNameDefaultValue1
- _kMOTemplateJSONPersonNameDefaultValue2
- _kMOTemplateJSONPlaceNameDefaultValue
- _kMOTemplateJSONTimeReferenceDefaultValue
- _objc_msgSend$appendMusicString
- _objc_msgSend$associatedMusic
- _objc_msgSend$associatedTime
- _objc_msgSend$dayNameFormatterInEnglish
- _objc_msgSend$decodeBoolForKey:
- _objc_msgSend$encodeBool:forKey:
- _objc_msgSend$initWithAppendMusicString:
- _objc_msgSend$initWithLocaleIdentifier:
- _objc_msgSend$initWithMusicString:
- _objc_msgSend$initWithTimeReferenceString:
- _objc_msgSend$mask
- _objc_msgSend$musicString
- _objc_msgSend$setAssociatedMusic:
- _objc_msgSend$setAssociatedTime:
- _objc_msgSend$timeReferenceString
- dayNameFormatterInEnglish.dateFormatter
- dayNameFormatterInEnglish.onceToken
CStrings:
- "Taylor"
- "Taylor's"
- "USERNOTIFICATIONS"
- "appendMusicString"
- "associatedMusic"
- "associatedTime"
- "cityName"
- "contact name, %!@(MISSING)"
- "en_US"
- "music string, %!@(MISSING)"
- "musicString"
- "place, %!@(MISSING), city, %!@(MISSING), visit time window %!@(MISSING)"
- "placeName"
- "time string, %!@(MISSING)"
- "timeReference"
- "timeReferenceString"

```
