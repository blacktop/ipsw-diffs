## CalendarFoundation

> `/System/Library/PrivateFrameworks/CalendarFoundation.framework/Versions/A/CalendarFoundation`

```diff

-1636.0.400.0.0
-  __TEXT.__text: 0x6abdc
-  __TEXT.__objc_methlist: 0x5fd4
-  __TEXT.__cstring: 0x7082
-  __TEXT.__const: 0x564
-  __TEXT.__gcc_except_tab: 0xa7c
-  __TEXT.__oslogstring: 0x3705
+1636.2.2.0.0
+  __TEXT.__text: 0x6e878
+  __TEXT.__objc_methlist: 0x6024
+  __TEXT.__cstring: 0x7132
+  __TEXT.__const: 0x8c4
+  __TEXT.__gcc_except_tab: 0xb4c
+  __TEXT.__oslogstring: 0x3b85
   __TEXT.__ustring: 0x2e8
   __TEXT.__dlopen_cstrs: 0xe0
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
-  __TEXT.__unwind_info: 0x1cf8
+  __TEXT.__unwind_info: 0x1dd0
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xce0
+  __DATA_CONST.__const: 0xce8
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4388
+  __DATA_CONST.__objc_selrefs: 0x43d8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xf8
-  __DATA_CONST.__got: 0x918
-  __AUTH_CONST.__const: 0x1c18
-  __AUTH_CONST.__cfstring: 0x9760
+  __DATA_CONST.__got: 0x940
+  __AUTH_CONST.__const: 0x1d98
+  __AUTH_CONST.__cfstring: 0x9820
   __AUTH_CONST.__objc_const: 0x7c10
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xaf0
+  __AUTH_CONST.__auth_got: 0xbd0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x12a0
-  __AUTH.__data: 0xe8
+  __AUTH.__objc_data: 0xee0
+  __AUTH.__data: 0x178
   __DATA.__objc_ivar: 0x364
-  __DATA.__data: 0xb28
-  __DATA.__bss: 0x660
-  __DATA_DIRTY.__objc_data: 0x1018
+  __DATA.__data: 0xb68
+  __DATA.__bss: 0xb80
+  __DATA_DIRTY.__objc_data: 0x13d8
   __DATA_DIRTY.__data: 0xe8
-  __DATA_DIRTY.__bss: 0x370
+  __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2813
-  Symbols:   6050
-  CStrings:  1647
+  Functions: 2907
+  Symbols:   6122
+  CStrings:  1672
 
Symbols:
+ +[CalAttachmentUtils URL:isContainedInDirectory:]
+ +[CalAttachmentUtils isSymbolicLinkAtURL:]
+ +[CalEntitlementsVerifier currentProcessIsIntentsExtension]
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
+ UnzipArchiveWithLimits
+ _BOMCopierCancelCopy
+ _BOMCopierSetCopyFileFinishedHandler
+ _BOMCopierSetCopyFileStartedHandler
+ _BOMCopierSetCopyFileUpdateHandler
+ _BOMCopierUserData
+ _CalPersonaUtilsErrorDomain
+ _CalUnzipCopyFileFinished
+ _CalUnzipCopyFileStarted
+ _CalUnzipCopyFileUpdate
+ _NSPOSIXErrorDomain
+ _NSUnderlyingErrorKey
+ _UnzipArchiveWithLimits
+ __CalUnzipCopyFileFinished
+ __CalUnzipCopyFileStarted
+ __CalUnzipCopyFileUpdate
+ __CalUnzipEntryDestinationPath
+ __CalUnzipParentIsContained
+ __CalUnzipTrackTopLevelPath
+ ___67+[CalUMCalendarDataContainerInfo containerInfoWithPersonaID:error:]_block_invoke
+ ___CalUnzipRemoveEscapingSymlinks_block_invoke
+ ____CalUnzipRemoveEscapingSymlinks_block_invoke
+ ___block_descriptor_40_e8_32r_e27_B24?0"NSURL"8"NSError"16l
+ ___swift_memcpy17_8
+ ___swift_memcpy8_8
+ _associated conformance 18CalendarFoundation19CachedDateFormatterV11FormatStyleOSHAASQ
+ _associated conformance 18CalendarFoundation19CachedDateFormatterV3Key33_9D03EE37A6E1641E4F2D3701453009D0LLVSHAASQ
+ _associated conformance So19NSFormattingContextVSHSCSQ
+ _associated conformance So20NSDateFormatterStyleVSHSCSQ
+ _get_enum_tag_for_layout_string 18CalendarFoundation19CachedDateFormatterV11FormatStyleO
+ _lstat
+ _objc_msgSend$URL:isContainedInDirectory:
+ _objc_msgSend$_isPersonalPersonaAvailable
+ _objc_msgSend$_personaUtilErrorForUserManagementError:
+ _objc_msgSend$_personaUtilErrorWithCode:underlyingError:
+ _objc_msgSend$containerForAccountIdentifier:error:
+ _objc_msgSend$containerInfoForAccountIdentifier:error:
+ _objc_msgSend$containerInfoWithAccount:error:
+ _objc_msgSend$containerInfoWithPersonaID:error:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$isPersonalPersona
+ _objc_msgSend$isSymbolicLinkAtURL:
+ _objc_msgSend$listAllPersonaAttributesWithError:
+ _objc_msgSend$performBlockAsPersonaWithIdentifier:block:error:
+ _objc_msgSend$personaForAccountIdentifier:error:
+ _realpath$DARWIN_EXTSN
+ _strcmp
+ _strncmp
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
+ _unlink
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
- _objc_msgSend$containerForAccountIdentifier:
- _objc_msgSend$containerInfoForAccountIdentifier:
- _objc_msgSend$initWithAccount:
- _objc_msgSend$initWithPersonaID:
- _objc_msgSend$performBlockAsPersonaWithIdentifier:block:
- _objc_msgSend$personaForAccountIdentifier:
CStrings:
+ ".."
+ "Archive contains a symlink pointing outside destination; removing it. entry = %@"
+ "Archive entry exceeds total size limit (%llu bytes); canceling extraction."
+ "Archive entry resolves outside destination; canceling extraction. entry = %s"
+ "Archive entry's parent directory escapes destination (likely via an earlier symlink entry); canceling extraction. entry = %s"
+ "Archive exceeds item count limit (%lu); canceling extraction."
+ "Archive exceeds total size limit (%llu bytes) while writing an entry; canceling extraction."
+ "Archive exceeds total size limit (%llu bytes); canceling extraction."
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "CalPersonaUtilsErrorDomain"
+ "Could not lstat %@: %d"
+ "Could not resolve %@ or %@: %d"
+ "Could not resolve destination %@: %d; refusing to extract."
+ "Error listing all persona attributes: %@"
+ "Failed to enumerate extracted archive contents at %@: %@; treating as unsafe."
+ "Failed to remove debris left by a failed extraction at %@: %@"
+ "Failed to remove escaping symlink: %d"
+ "Personal persona is available. Assuming the requested persona was actually deleted."
+ "Personal persona is not available."
+ "Refusing to remove %@: its parent directory is not contained in destination."
+ "Unexpected error from UserManagement: %@"
+ "com.apple.calendar.CalendarIntentsExtension"
+ "enforceDestinationEncapsulation"
+ "enforceDestinationLocation"
+ "value.stringValue"
```
