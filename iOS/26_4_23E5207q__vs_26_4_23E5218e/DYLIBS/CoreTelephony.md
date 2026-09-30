## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13169.2.1.2.0
-  __TEXT.__text: 0x1b6c90
-  __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0x1bcb4
-  __TEXT.__const: 0x1310
-  __TEXT.__gcc_except_tab: 0x20498
-  __TEXT.__cstring: 0x20108
+13171.6.0.0.0
+  __TEXT.__text: 0x1b6d04
+  __TEXT.__auth_stubs: 0x1c80
+  __TEXT.__objc_methlist: 0x1bd3c
+  __TEXT.__const: 0x1300
+  __TEXT.__gcc_except_tab: 0x204b4
+  __TEXT.__cstring: 0x20198
   __TEXT.__oslogstring: 0x4ca6
-  __TEXT.__swift5_typeref: 0x1a1
+  __TEXT.__swift5_typeref: 0x18d
   __TEXT.__swift5_reflstr: 0xc1
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0xa4

   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_ret: 0x10
   __TEXT.__unwind_info: 0xe980
-  __TEXT.__eh_frame: 0x2e0
-  __TEXT.__objc_classname: 0x5b96
-  __TEXT.__objc_methname: 0x238a7
+  __TEXT.__eh_frame: 0x2b8
+  __TEXT.__objc_classname: 0x5bc6
+  __TEXT.__objc_methname: 0x2395f
   __TEXT.__objc_methtype: 0x7442
-  __TEXT.__objc_stubs: 0x174e0
-  __DATA_CONST.__got: 0xba0
-  __DATA_CONST.__const: 0x73c0
-  __DATA_CONST.__objc_classlist: 0x15b0
+  __TEXT.__objc_stubs: 0x17580
+  __DATA_CONST.__got: 0xb80
+  __DATA_CONST.__const: 0x73c8
+  __DATA_CONST.__objc_classlist: 0x15b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a48
+  __DATA_CONST.__objc_selrefs: 0x7a70
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1870
+  __DATA_CONST.__objc_superrefs: 0x1880
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xe88
+  __AUTH_CONST.__auth_got: 0xe58
   __AUTH_CONST.__const: 0x2360
-  __AUTH_CONST.__cfstring: 0x1e060
-  __AUTH_CONST.__objc_const: 0x30730
+  __AUTH_CONST.__cfstring: 0x1e0e0
+  __AUTH_CONST.__objc_const: 0x30820
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xad70
+  __AUTH.__objc_data: 0xadc0
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x147c
-  __DATA.__data: 0x20b8
+  __DATA.__objc_ivar: 0x1484
+  __DATA.__data: 0x20a0
   __DATA.__bss: 0x600
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2b20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AF9FE49F-7D08-37B2-9417-8283F8A17B65
-  Functions: 11604
-  Symbols:   39109
-  CStrings:  17389
+  UUID: 5789C733-1A3A-3343-A887-DBF599066865
+  Functions: 11610
+  Symbols:   39145
+  CStrings:  17408
 
Symbols:
+ +[CTCellularPlanLifecycleProperties supportsSecureCoding]
+ +[CTXPCResumeCrossPlatformTransferSessionRequest allowedClassesForArguments]
+ -[CTCAConversationState endSessionOffered]
+ -[CTCAConversationState setEndSessionOffered:]
+ -[CTCellularPlanLifecycleProperties .cxx_destruct]
+ -[CTCellularPlanLifecycleProperties copyWithZone:]
+ -[CTCellularPlanLifecycleProperties description]
+ -[CTCellularPlanLifecycleProperties encodeWithCoder:]
+ -[CTCellularPlanLifecycleProperties expirationDate]
+ -[CTCellularPlanLifecycleProperties initWithCoder:]
+ -[CTCellularPlanLifecycleProperties init]
+ -[CTCellularPlanLifecycleProperties setExpirationDate:]
+ -[CTLazuliGroupChatInformation setSubjectState:]
+ -[CTLazuliGroupChatInformation subjectState]
+ -[CTXPCResumeCrossPlatformTransferSessionRequest init]
+ -[CTXPCResumeCrossPlatformTransferSessionRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCResumeCrossPlatformTransferSessionRequest requiredEntitlement]
+ -[CoreTelephonyClient(CrossPlatformTransfer) resumeCrossPlatformTransferSession:]
+ -[CoreTelephonyClient(CrossPlatformTransfer) resumeCrossPlatformTransferSession:].cold.1
+ _OBJC_CLASS_$_CTCellularPlanLifecycleProperties
+ _OBJC_CLASS_$_CTXPCResumeCrossPlatformTransferSessionRequest
+ _OBJC_IVAR_$_CTCAConversationState._endSessionOffered
+ _OBJC_IVAR_$_CTCellularPlanLifecycleProperties._expirationDate
+ _OBJC_IVAR_$_CTLazuliGroupChatInformation._subjectState
+ _OBJC_METACLASS_$_CTCellularPlanLifecycleProperties
+ _OBJC_METACLASS_$_CTXPCResumeCrossPlatformTransferSessionRequest
+ __OBJC_$_CLASS_METHODS_CTCellularPlanLifecycleProperties
+ __OBJC_$_CLASS_METHODS_CTXPCResumeCrossPlatformTransferSessionRequest
+ __OBJC_$_CLASS_PROP_LIST_CTCellularPlanLifecycleProperties
+ __OBJC_$_INSTANCE_METHODS_CTCellularPlanLifecycleProperties
+ __OBJC_$_INSTANCE_METHODS_CTXPCResumeCrossPlatformTransferSessionRequest
+ __OBJC_$_INSTANCE_VARIABLES_CTCellularPlanLifecycleProperties
+ __OBJC_$_PROP_LIST_CTCellularPlanLifecycleProperties
+ __OBJC_CLASS_PROTOCOLS_$_CTCellularPlanLifecycleProperties
+ __OBJC_CLASS_RO_$_CTCellularPlanLifecycleProperties
+ __OBJC_CLASS_RO_$_CTXPCResumeCrossPlatformTransferSessionRequest
+ __OBJC_METACLASS_RO_$_CTCellularPlanLifecycleProperties
+ __OBJC_METACLASS_RO_$_CTXPCResumeCrossPlatformTransferSessionRequest
+ ___81-[CoreTelephonyClient(CrossPlatformTransfer) resumeCrossPlatformTransferSession:]_block_invoke
+ ___81-[CoreTelephonyClient(CrossPlatformTransfer) resumeCrossPlatformTransferSession:]_block_invoke_2
+ ___94-[CTXPCResumeCrossPlatformTransferSessionRequest performRequestWithHandler:completionHandler:]_block_invoke
+ _block_copy_helper.11
+ _block_copy_helper.3
+ _block_copy_helper.7
+ _block_descriptor.13
+ _block_descriptor.5
+ _block_descriptor.9
+ _block_destroy_helper.12
+ _block_destroy_helper.4
+ _block_destroy_helper.8
+ _objc_msgSend$endSessionOffered
+ _objc_msgSend$resumeCrossPlatformTransferSession:
+ _objc_msgSend$setEndSessionOffered:
+ _objc_msgSend$setSubjectState:
+ _objc_msgSend$subjectState
- +[CTCellularPlanlifecycleProperties supportsSecureCoding]
- -[CTCellularPlanlifecycleProperties .cxx_destruct]
- -[CTCellularPlanlifecycleProperties copyWithZone:]
- -[CTCellularPlanlifecycleProperties description]
- -[CTCellularPlanlifecycleProperties encodeWithCoder:]
- -[CTCellularPlanlifecycleProperties expirationDate]
- -[CTCellularPlanlifecycleProperties initWithCoder:]
- -[CTCellularPlanlifecycleProperties init]
- -[CTCellularPlanlifecycleProperties setExpirationDate:]
- _OBJC_CLASS_$_CTCellularPlanlifecycleProperties
- _OBJC_IVAR_$_CTCellularPlanlifecycleProperties._expirationDate
- _OBJC_METACLASS_$_CTCellularPlanlifecycleProperties
- __OBJC_$_CLASS_METHODS_CTCellularPlanlifecycleProperties
- __OBJC_$_CLASS_PROP_LIST_CTCellularPlanlifecycleProperties
- __OBJC_$_INSTANCE_METHODS_CTCellularPlanlifecycleProperties
- __OBJC_$_INSTANCE_VARIABLES_CTCellularPlanlifecycleProperties
- __OBJC_$_PROP_LIST_CTCellularPlanlifecycleProperties
- __OBJC_CLASS_PROTOCOLS_$_CTCellularPlanlifecycleProperties
- __OBJC_CLASS_RO_$_CTCellularPlanlifecycleProperties
- __OBJC_METACLASS_RO_$_CTCellularPlanlifecycleProperties
- __swiftEmptyDictionarySingleton
- _block_copy_helper.12
- _block_copy_helper.4
- _block_copy_helper.8
- _block_descriptor.10
- _block_descriptor.14
- _block_descriptor.6
- _block_destroy_helper.13
- _block_destroy_helper.5
- _block_destroy_helper.9
- _nw_path_evaluator_start
- _symbolic SS_ypt
- _symbolic _____ySSypG s18_DictionaryStorageC
CStrings:
+ ", endSessionOffered=%s"
+ ", subjectState = %ld"
+ "/AppleInternal/Library/BuildRoots/4~CJMmugDo0WjUOke3tQDaQrUS0j89yOOAHlSYzSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJMmugDo0WjUOke3tQDaQrUS0j89yOOAHlSYzSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJMmugDo0WjUOke3tQDaQrUS0j89yOOAHlSYzSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJMmugDo0WjUOke3tQDaQrUS0j89yOOAHlSYzSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJMmugDo0WjUOke3tQDaQrUS0j89yOOAHlSYzSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CJMmugDo0WjUOke3tQDaQrUS0j89yOOAHlSYzSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "13171.6"
+ "13171.6~3"
+ "@\"CTCellularPlanLifecycleProperties\""
+ "CTCellularPlanLifecycleProperties"
+ "CTStewieConnectionAssistantEventTypeUnintendedEmergencySessionCheck"
+ "CTXPCResumeCrossPlatformTransferSessionRequest"
+ "T@\"CTCellularPlanLifecycleProperties\",&,N,V_lifecycleProperties"
+ "TB,N,V_endSessionOffered"
+ "Tq,N,V_subjectState"
+ "_endSessionOffered"
+ "_subjectState"
+ "endSessionOffered"
+ "kSubjectStateKey"
+ "resumeCrossPlatformTransferSession:"
+ "setEndSessionOffered:"
+ "setSubjectState:"
+ "subjectState"
- "/AppleInternal/Library/BuildRoots/4~CIdSugDsOHtEMrmV4CxyQywrAsBr0VC5t58aAls/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIdSugDsOHtEMrmV4CxyQywrAsBr0VC5t58aAls/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIdSugDsOHtEMrmV4CxyQywrAsBr0VC5t58aAls/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIdSugDsOHtEMrmV4CxyQywrAsBr0VC5t58aAls/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIdSugDsOHtEMrmV4CxyQywrAsBr0VC5t58aAls/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CIdSugDsOHtEMrmV4CxyQywrAsBr0VC5t58aAls/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "13169.2.1.2"
- "13169.2.1.2~2"
- "@\"CTCellularPlanlifecycleProperties\""
- "CTCellularPlanlifecycleProperties"
- "T@\"CTCellularPlanlifecycleProperties\",&,N,V_lifecycleProperties"

```
