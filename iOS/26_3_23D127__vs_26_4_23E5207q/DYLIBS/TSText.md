## TSText

> `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText`

```diff

-485.0.0.0.0
-  __TEXT.__text: 0x247a34
-  __TEXT.__auth_stubs: 0x37b0
+486.0.0.0.0
+  __TEXT.__text: 0x258568
+  __TEXT.__auth_stubs: 0x37d0
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x10760
-  __TEXT.__gcc_except_tab: 0x2ae3c
-  __TEXT.__const: 0x14358
-  __TEXT.__cstring: 0x21afc
+  __TEXT.__objc_methlist: 0x108e8
+  __TEXT.__gcc_except_tab: 0x2b124
+  __TEXT.__const: 0x14558
+  __TEXT.__cstring: 0x2582f
   __TEXT.__ustring: 0x284
-  __TEXT.__swift5_typeref: 0x1a1
+  __TEXT.__swift5_typeref: 0x25a
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__swift5_reflstr: 0x154
-  __TEXT.__swift5_assocty: 0x80
+  __TEXT.__swift5_reflstr: 0x17f
+  __TEXT.__swift5_assocty: 0x108
   __TEXT.__constg_swiftt: 0x208
   __TEXT.__swift5_fieldmd: 0x1d4
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x38
-  __TEXT.__unwind_info: 0xf040
-  __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0x17f9
-  __TEXT.__objc_methname: 0x2349c
-  __TEXT.__objc_methtype: 0x9829
-  __TEXT.__objc_stubs: 0x17600
-  __DATA_CONST.__got: 0xb68
-  __DATA_CONST.__const: 0x3698
+  __TEXT.__unwind_info: 0xf5d8
+  __TEXT.__eh_frame: 0xe0
+  __TEXT.__objc_classname: 0x1858
+  __TEXT.__objc_methname: 0x23a4d
+  __TEXT.__objc_methtype: 0x9a6b
+  __TEXT.__objc_stubs: 0x179c0
+  __DATA_CONST.__got: 0xb98
+  __DATA_CONST.__const: 0x3760
   __DATA_CONST.__objc_classlist: 0x5e8
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8300
+  __DATA_CONST.__objc_selrefs: 0x83e8
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0xf10
-  __AUTH_CONST.__auth_got: 0x1bf0
+  __AUTH_CONST.__auth_got: 0x1c00
   __AUTH_CONST.__const: 0xc420
   __AUTH_CONST.__cfstring: 0x7980
-  __AUTH_CONST.__objc_const: 0x150f0
+  __AUTH_CONST.__objc_const: 0x15128
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x8e8
   __AUTH_CONST.__objc_doubleobj: 0x110

   __AUTH.__objc_data: 0x3be8
   __AUTH.__data: 0x80
   __DATA.__objc_ivar: 0xa9c
-  __DATA.__data: 0x24f0
+  __DATA.__data: 0x2558
   __DATA.__common: 0x60
-  __DATA.__bss: 0x1990
+  __DATA.__bss: 0x1b90
   __DATA_DIRTY.__data: 0x1d70
   __DATA_DIRTY.__common: 0x2c00
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 69EAE813-1F12-3E4A-B8F4-FF40FDE468F5
-  Functions: 13775
+  UUID: 86ECB0CB-5AFE-384E-92AF-003836037515
+  Functions: 13882
   Symbols:   7868
-  CStrings:  10710
+  CStrings:  10756
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __swift_FORCE_LOAD_$_swiftSpatial
+ _objc_initWeak
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_willThrowTypedImpl
- __swift_FORCE_LOAD_$_swiftAccelerate
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x6
- _swift_willThrow
CStrings:
+ "+[TSWPDateTimeSmartField dateStringFromTime:withFormat:localeIdentifier:dateStyle:timeStyle:yearOnlyDateString:]"
+ "+[TSWPShapeInfo autosizeOffsetForProperty:value:size:textIsVertical:]"
+ "-[TSWPListStyle geometryForLevel:]"
+ "-[TSWPShapeInfo autosizeGeometryForAlignment:]"
+ "-[TSWPStorage valueForProperty:atCharIndex:effectiveRange:styleEffectiveRange:]"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwwugDcVd3m2J1fX4qCtDLs-bXTAeSXLnFsvqE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Binaries/iWorkImport/install/Root/include/google/protobuf/repeated_field.h"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/messages/src/TSWPArchives.pb.cc"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/messages/src/TSWPArchives.sos.pb.cc"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/messages/src/TSWPCommandArchives.pb.cc"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/NSStringAdditions.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSSStyle+TSWPArchivingAdditions.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSSThemeAdditions.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPAdornmentLine.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPAdornmentRect.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPAdornments.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPArchivedDateTimeSelection.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPArchivedHyperlinkSelection.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPAttachmentAttributeArray.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPAttributeArray.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPAttributeEnumerator.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPBookmarkField.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPCTTypesetterCache.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPChange.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPChangeDetails.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPCharacterStyle.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPColumn.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPColumnStyle.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPColumns.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPCoreTextTypesetter.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDateTimeSmartField.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDocumentRoot.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDrawableAttachment.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDropCap.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDropCapAdornment+Geometry.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDropCapAdornment.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDropCapPersistenceAdditions.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDropCapStyle.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPDropCapStyle_Archiving.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPEquationBaseRep.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPEquationInfo.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPEquationInlineRep.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPEquationLayout.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPEquationLayoutContext.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFilteredStorage.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFilteredString.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFloatingCommentInfo.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFloatingCommentRep.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFlowInfo.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFlowInfoContainer.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFont.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFontList.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFontMetricsCache.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPFootnoteReferenceAttachment.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPHeaderFooterProvider.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPHighlight.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPHyperlinkField.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPImageBulletProvider.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPInteriorTextWrapController.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPItemNumbering.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPLayout.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPLayoutChore.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPLayoutManager.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPLayoutMetricsCache.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPLayoutState.h"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPLineFragment.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPLineSpacing.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPLinkedLayout.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPListLabel.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPListStyle.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPMergeFieldType.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPMergeProperty.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPNumberAttachment.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPObjectPlacement.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPOverlappingField.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPOverlappingFieldsAttributeArray.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPPadding.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPPageLayout.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPParagraphAttributeArray.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPParagraphEnumerator.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPParagraphIterator.swift"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPParagraphStyle.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPParagraphTypesetter.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPPencilAnnotation.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPPhonetics.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPRangeArray.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPRangeMap.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPRenderer.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPRendererUtilities.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPRendererUtilities_Internal.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPRep.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPSectionPlaceholder.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPSelection.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPShapeInfo.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPShapeInfoPersistenceAdditions.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPShapeLayout.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPShapeRep.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPShapeStyle.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPSmartField.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorage.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageAction.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageActionBuilder.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageActionBuilderCore.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageActionGroup.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageActionRunner.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageActionState.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageAnchorAttachmentMigrator.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageAttributeAction.h"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageAttributeAction.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageBroadcaster.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageIterator.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStoragePasteRules.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStoragePasteboardProxy.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageStyleProvider.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageStyler.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorageTransaction.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorage_action.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorage_annotation.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorage_attributeTables.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorage_copying.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStorage_private.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStyleAttributeArray.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStyleDiff.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPStylesheetAdditions.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTOCEntryData.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTOCInfo.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTOCLayout.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTOCLayoutHint.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTOCPartitioner.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTOCRep.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTOCSettings.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTableStorage.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTabs.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTargetHint.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPText.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTextHighlightRenderingDelegate.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTextReplacement.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTextualAttachment.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTrackedDeletion.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTrackedInsertion.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPTypesetterTextSource.mm"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPURLDataDetector.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPUserDefaults.m"
+ "/Library/Caches/com.apple.xbs/7993ECA3-AE30-40F3-84A4-74EFC800896C/TemporaryDirectory.kSuc8d/Sources/iWorkImport/shared/text/TSWPUtilities.mm"
+ "@44@0:8i16Q20^{_NSRange=QQ}28^{_NSRange=QQ}36"
+ "@60@0:8d16@24@32q40q48B56"
+ "I44@0:8{_NSRange=QQ}16@32B40"
+ "Illegal list level: %lu"
+ "Unexpected property"
+ "alignmentOffsetForProperty:oldAlignment:newAlignment:size:textIsVertical:"
+ "allowsImageGenerationForChild"
+ "autosizeGeometryForAlignment:"
+ "autosizeOffsetForProperty:value:size:textIsVertical:"
+ "bakeShrinkTextToFitIntoModelIfNeeded"
+ "boxedLabelIndentForLevel:"
+ "canPasteData:fromPhysicalKeyboard:"
+ "charCountOfGlyphStartingAtCharIndex:withColumns:"
+ "copyTextAttributeUUIDStringFrom:"
+ "d48@0:8i16q20{CGSize=dd}28B44"
+ "dateStringFromTime:withFormat:localeIdentifier:dateStyle:timeStyle:yearOnlyDateString:"
+ "fontTraitsForRange:withColumns:includingLabel:"
+ "geometryForLevel:"
+ "glyphCountForRubyFieldAtCharIndex:withColumns:"
+ "glyphRectForRange:withColumns:includingLabel:"
+ "glyphRectForRubyFieldAtCharIndex:withColumns:glyphRange:"
+ "initWithHomogeneousValue:"
+ "isAttachedToFootnoteText"
+ "isAttachedToHeaderText"
+ "listLabelTypeAtCharIndex:"
+ "maxInset"
+ "minInset"
+ "p_bakeShrinkTextToFitIntoModelIfNeeded"
+ "p_calcEffectiveRangeAtCharIndex:property:charStyleRange:parStyleRange:parStyle:value:"
+ "p_repHasHDRContent"
+ "p_repHasHDRStrokeContent"
+ "p_wantsHDRContentsRenderable"
+ "parStyle"
+ "prefersHDRRendering"
+ "rawTextIndentForLevel:"
+ "supportsHDR"
+ "v24@?0@\"TSWPColumn\"8^B16"
+ "v32@?0@\"TSUPair\"8Q16^B24"
+ "valueForProperty:atCharIndex:effectiveRange:styleEffectiveRange:"
+ "{CGPoint=dd}56@0:8i16q20q28{CGSize=dd}36B52"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}44@0:8{_NSRange=QQ}16@32B40"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8Q16@24{_NSRange=QQ}32"
+ "{_NSRange=QQ}76@0:8Q16i24{_NSRange=QQ}28{_NSRange=QQ}44@60@68"
+ "{map<unsigned long, TSWPFontMetricsCacheEntry, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, TSWPFontMetricsCacheEntry>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, std::__map_value_compare<unsigned long, std::pair<const unsigned long, TSWPFontMetricsCacheEntry>, std::less<unsigned long>>, std::allocator<std::pair<const unsigned long, TSWPFontMetricsCacheEntry>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::__map_value_compare<unsigned long, std::pair<const unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::less<unsigned long>>, std::allocator<std::pair<const unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "+[TSWPDateTimeSmartField dateStringFromTime:withFormat:localeIdentifier:dateStyle:timeStyle:]"
- "-[TSWPStorage valueForProperty:atCharIndex:effectiveRange:]"
- "/Library/Caches/com.apple.xbs/Binaries/iWorkImport/install/Root/include/google/protobuf/repeated_field.h"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/messages/src/TSWPArchives.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/messages/src/TSWPArchives.sos.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/messages/src/TSWPCommandArchives.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/NSStringAdditions.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSSStyle+TSWPArchivingAdditions.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSSThemeAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPAdornmentLine.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPAdornmentRect.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPAdornments.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPArchivedDateTimeSelection.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPArchivedHyperlinkSelection.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPAttachmentAttributeArray.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPAttributeArray.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPAttributeEnumerator.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPBookmarkField.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPCTTypesetterCache.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPChange.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPChangeDetails.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPCharacterStyle.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPColumn.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPColumnStyle.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPColumns.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPCoreTextTypesetter.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDateTimeSmartField.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDocumentRoot.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDrawableAttachment.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDropCap.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDropCapAdornment+Geometry.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDropCapAdornment.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDropCapPersistenceAdditions.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDropCapStyle.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPDropCapStyle_Archiving.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPEquationBaseRep.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPEquationInfo.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPEquationInlineRep.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPEquationLayout.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPEquationLayoutContext.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFilteredStorage.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFilteredString.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFloatingCommentInfo.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFloatingCommentRep.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFlowInfo.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFlowInfoContainer.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFont.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFontList.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFontMetricsCache.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPFootnoteReferenceAttachment.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPHeaderFooterProvider.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPHighlight.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPHyperlinkField.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPImageBulletProvider.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPInteriorTextWrapController.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPItemNumbering.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPLayout.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPLayoutChore.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPLayoutManager.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPLayoutMetricsCache.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPLayoutState.h"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPLineFragment.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPLineSpacing.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPLinkedLayout.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPListLabel.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPListStyle.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPMergeFieldType.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPMergeProperty.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPNumberAttachment.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPObjectPlacement.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPOverlappingField.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPOverlappingFieldsAttributeArray.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPPadding.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPPageLayout.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPParagraphAttributeArray.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPParagraphEnumerator.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPParagraphIterator.swift"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPParagraphStyle.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPParagraphTypesetter.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPPencilAnnotation.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPPhonetics.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPRangeArray.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPRangeMap.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPRenderer.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPRendererUtilities.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPRendererUtilities_Internal.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPRep.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPSectionPlaceholder.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPSelection.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPShapeInfo.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPShapeInfoPersistenceAdditions.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPShapeLayout.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPShapeRep.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPShapeStyle.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPSmartField.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorage.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageAction.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageActionBuilder.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageActionBuilderCore.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageActionGroup.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageActionRunner.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageActionState.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageAnchorAttachmentMigrator.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageAttributeAction.h"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageAttributeAction.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageBroadcaster.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageIterator.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStoragePasteRules.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStoragePasteboardProxy.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageStyleProvider.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageStyler.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorageTransaction.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorage_action.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorage_annotation.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorage_attributeTables.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorage_copying.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStorage_private.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStyleAttributeArray.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStyleDiff.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPStylesheetAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTOCEntryData.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTOCInfo.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTOCLayout.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTOCLayoutHint.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTOCPartitioner.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTOCRep.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTOCSettings.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTableStorage.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTabs.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTargetHint.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPText.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTextHighlightRenderingDelegate.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTextReplacement.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTextualAttachment.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTrackedDeletion.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTrackedInsertion.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPTypesetterTextSource.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPURLDataDetector.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPUserDefaults.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkImport/shared/text/TSWPUtilities.mm"
- "canPasteDataFromPhysicalKeyboard:"
- "string out of bounds"
- "string out of range"
- "uint (anonymous namespace)::toAbjadUnder1000(uint, unichar *)"
- "uint (anonymous namespace)::toHebrewUnder1000(uint, unichar *)"
- "{map<unsigned long, TSWPFontMetricsCacheEntry, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, TSWPFontMetricsCacheEntry>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"

```
