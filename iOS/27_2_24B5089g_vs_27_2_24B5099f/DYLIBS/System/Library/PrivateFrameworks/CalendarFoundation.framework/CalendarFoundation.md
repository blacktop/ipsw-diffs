## CalendarFoundation

> `/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation`

```diff

-1636.1.2.0.0
-  __TEXT.__text: 0x5f7a8
-  __TEXT.__objc_methlist: 0x5d8c
-  __TEXT.__cstring: 0x65d2
-  __TEXT.__const: 0x594
-  __TEXT.__gcc_except_tab: 0xafc
-  __TEXT.__oslogstring: 0x38d5
+1636.2.2.0.0
+  __TEXT.__text: 0x61bf8
+  __TEXT.__objc_methlist: 0x5db4
+  __TEXT.__cstring: 0x6602
+  __TEXT.__const: 0x8f4
+  __TEXT.__gcc_except_tab: 0xaf8
+  __TEXT.__oslogstring: 0x39a5
   __TEXT.__ustring: 0x2e8
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x1f8
-  __TEXT.__constg_swiftt: 0x104
-  __TEXT.__swift5_reflstr: 0xf7
-  __TEXT.__swift5_fieldmd: 0xf8
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_typeref: 0x2cc
+  __TEXT.__constg_swiftt: 0x1b8
+  __TEXT.__swift5_reflstr: 0x140
+  __TEXT.__swift5_fieldmd: 0x170
+  __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_capture: 0xfc
-  __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x2688
+  __TEXT.__unwind_info: 0x2758
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1788
+  __DATA_CONST.__const: 0x1790
   __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41b0
+  __DATA_CONST.__objc_selrefs: 0x41d8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__got: 0x8f0
-  __AUTH_CONST.__const: 0x1058
-  __AUTH_CONST.__cfstring: 0x9540
+  __DATA_CONST.__got: 0x910
+  __AUTH_CONST.__const: 0x11a8
+  __AUTH_CONST.__cfstring: 0x9580
   __AUTH_CONST.__objc_const: 0x79b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xc28
-  __AUTH.__objc_data: 0x12c8
-  __AUTH.__data: 0x118
+  __AUTH_CONST.__auth_got: 0xcb8
+  __AUTH.__objc_data: 0xdf0
+  __AUTH.__data: 0x178
   __DATA.__objc_ivar: 0x354
-  __DATA.__data: 0xb48
-  __DATA_DIRTY.__objc_data: 0xf00
-  __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__bss: 0x278
+  __DATA.__data: 0xb98
+  __DATA_DIRTY.__objc_data: 0x13d8
+  __DATA_DIRTY.__data: 0xb0
+  __DATA_DIRTY.__bss: 0x288
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2680
-  Symbols:   4444
-  CStrings:  1561
+  Functions: 2753
+  Symbols:   4480
+  CStrings:  1567
 
Symbols:
+ +[CalPersonaUtils _isPersonalPersonaAvailable]
+ +[CalPersonaUtils _personaUtilErrorForUserManagementError:]
+ +[CalPersonaUtils _personaUtilErrorWithCode:underlyingError:]
+ +[CalPersonaUtils performBlockAsPersonaWithIdentifier:block:error:]
+ +[CalUMCalendarDataContainerInfo containerInfoWithAccount:error:]
+ +[CalUMCalendarDataContainerInfo containerInfoWithPersonaID:error:]
+ -[CalMockCalendarDataContainerProvider containerForAccountIdentifier:error:]
+ -[CalMockCalendarDataContainerProvider containerInfoForAccount:error:]
+ -[CalMockCalendarDataContainerProvider containerInfoForAccountIdentifier:error:]
+ -[CalMockCalendarDataContainerProvider containerInfoForPersonaIdentifier:error:]
+ -[CalMockCalendarDataContainerProvider personaForAccountIdentifier:error:]
+ -[CalUMCalendarDataContainerProvider containerForAccountIdentifier:error:]
+ -[CalUMCalendarDataContainerProvider containerInfoForAccount:error:]
+ -[CalUMCalendarDataContainerProvider containerInfoForAccountIdentifier:error:]
+ -[CalUMCalendarDataContainerProvider containerInfoForPersonaIdentifier:error:]
+ _CalPersonaUtilsErrorDomain
+ _NSPOSIXErrorDomain
+ _NSUnderlyingErrorKey
+ ___67+[CalUMCalendarDataContainerInfo containerInfoWithPersonaID:error:]_block_invoke
+ ___swift_memcpy17_8
+ ___swift_memcpy8_8
+ _associated conformance 18CalendarFoundation19CachedDateFormatterV11FormatStyleOSHAASQ
+ _associated conformance 18CalendarFoundation19CachedDateFormatterV3Key33_9D03EE37A6E1641E4F2D3701453009D0LLVSHAASQ
+ _associated conformance So19NSFormattingContextVSHSCSQ
+ _associated conformance So20NSDateFormatterStyleVSHSCSQ
+ _get_enum_tag_for_layout_string 18CalendarFoundation19CachedDateFormatterV11FormatStyleO
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $sSY
+ _symbolic SS
+ _symbolic Si
+ _symbolic So15NSDateFormatterC
+ _symbolic Su
+ _symbolic _____ 10Foundation8CalendarV
+ _symbolic _____ 18CalendarFoundation19CachedDateFormatterV
+ _symbolic _____ 18CalendarFoundation19CachedDateFormatterV11FormatStyleO
+ _symbolic _____ 18CalendarFoundation19CachedDateFormatterV3Key33_9D03EE37A6E1641E4F2D3701453009D0LLV
+ _symbolic _____ So19NSFormattingContextV
+ _symbolic _____ So20NSDateFormatterStyleV
+ _symbolic _____4date_AA4timet So20NSDateFormatterStyleV
+ _symbolic _____Sg 10Foundation6LocaleV
+ _symbolic _____ySDy_____So15NSDateFormatterCG_____G s13ManagedBufferCsRi__rlE 18CalendarFoundation19CachedDateFormatterV3Key33_9D03EE37A6E1641E4F2D3701453009D0LLV So16os_unfair_lock_sV
+ _symbolic _____y_____So15NSDateFormatterCG s18_DictionaryStorageC 18CalendarFoundation19CachedDateFormatterV3Key33_9D03EE37A6E1641E4F2D3701453009D0LLV
+ _type_layout_string 18CalendarFoundation19CachedDateFormatterV
+ _type_layout_string 18CalendarFoundation19CachedDateFormatterV11FormatStyleO
- +[CalPersonaUtils performBlockAsPersonaWithIdentifier:block:]
- -[CalMockCalendarDataContainerProvider containerForAccountIdentifier:]
- -[CalMockCalendarDataContainerProvider containerInfoForAccount:]
- -[CalMockCalendarDataContainerProvider containerInfoForAccountIdentifier:]
- -[CalMockCalendarDataContainerProvider containerInfoForPersonaIdentifier:]
- -[CalMockCalendarDataContainerProvider personaForAccountIdentifier:]
- -[CalUMCalendarDataContainerInfo initWithAccount:]
- -[CalUMCalendarDataContainerInfo initWithPersonaID:]
- -[CalUMCalendarDataContainerProvider containerForAccountIdentifier:]
- -[CalUMCalendarDataContainerProvider containerInfoForAccount:]
- -[CalUMCalendarDataContainerProvider containerInfoForAccountIdentifier:]
- -[CalUMCalendarDataContainerProvider containerInfoForPersonaIdentifier:]
- ___52-[CalUMCalendarDataContainerInfo initWithPersonaID:]_block_invoke
CStrings:
+ "CalPersonaUtilsErrorDomain"
+ "Error listing all persona attributes: %@"
+ "Personal persona is available. Assuming the requested persona was actually deleted."
+ "Personal persona is not available."
+ "Unexpected error from UserManagement: %@"
+ "value.stringValue"
```
