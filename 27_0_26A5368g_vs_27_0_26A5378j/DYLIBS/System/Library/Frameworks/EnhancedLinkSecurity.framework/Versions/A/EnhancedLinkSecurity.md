## EnhancedLinkSecurity

> `/System/Library/Frameworks/EnhancedLinkSecurity.framework/Versions/A/EnhancedLinkSecurity`

```diff

-  __TEXT.__text: 0x4fe4
-  __TEXT.__objc_methlist: 0x19c
-  __TEXT.__const: 0x308
-  __TEXT.__swift5_typeref: 0x1bb
-  __TEXT.__swift5_fieldmd: 0x80
-  __TEXT.__constg_swiftt: 0x180
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_reflstr: 0x38
-  __TEXT.__cstring: 0xfc
-  __TEXT.__swift5_capture: 0x90
-  __TEXT.__oslogstring: 0x1c0
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__text: 0x1e50
+  __TEXT.__objc_methlist: 0x74
+  __TEXT.__const: 0xc2
+  __TEXT.__swift5_typeref: 0x93
+  __TEXT.__swift5_capture: 0x84
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__eh_frame: 0x230
+  __TEXT.__unwind_info: 0x138
+  __TEXT.__eh_frame: 0x1c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x140
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__got: 0x88
-  __AUTH_CONST.__const: 0x2d8
-  __AUTH_CONST.__objc_const: 0x9e8
-  __AUTH_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__objc_selrefs: 0x60
+  __DATA_CONST.__got: 0x20
+  __AUTH_CONST.__const: 0x168
+  __AUTH_CONST.__objc_const: 0x78
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH.__objc_data: 0x48
-  __AUTH.__data: 0x1d0
-  __DATA.__data: 0x1c0
-  __DATA.__common: 0x8
+  __DATA.__data: 0x10
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x28
-  __DATA_DIRTY.__data: 0x58
-  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/PrivateFrameworks/IMFoundation.framework/Versions/A/IMFoundation
+  - /System/Library/Frameworks/LinkSecurity.framework/Versions/A/LinkSecurity
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 143
-  Symbols:   81
-  CStrings:  16
+  Functions: 58
+  Symbols:   49
+  CStrings:  0
 
Sections:
~ __TEXT.__swift_as_cont : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _OBJC_CLASS_$_LSLinkSecurityManager
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
- _IMGetDomainBoolForKey
- _IMGetDomainValueForKey
- _IMSetDomainBoolForKey
- _IMSetDomainValueForKey
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_OS_dispatch_queue
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __os_log_impl
- __swiftEmptyArrayStorage
- __swiftEmptySetSingleton
- __swift_stdlib_bridgeErrorToNSError
- _malloc_size
- _os_log_type_enabled
- _swift_arrayInitWithCopy
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_deallocClassInstance
- _swift_deletedMethodError
- _swift_dynamicCast
- _swift_endAccess
- _swift_errorRelease
- _swift_errorRetain
- _swift_getTypeByMangledNameInContextInMetadataState2
- _swift_getWitnessTable
- _swift_isUniquelyReferenced_nonNull_native
- _swift_lookUpClassMethod
- _swift_slowAlloc
- _swift_slowDealloc
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
CStrings:
- "Adding %ld URL(s) to the store"
- "Adding URL to the store"
- "Checking if URL is in the store"
- "Checking sentinel value: %{bool}d"
- "Connection interrupted"
- "Connection invalidated"
- "Could not connect with error: %@"
- "EnhancedLinkSecurityManager"
- "EnhancedLinkSecuritySentinelKey"
- "No URLs were for a website, not adding any to the store"
- "Starting connection to EnhancedLinkSecurityStore"
- "URL was not for a website, not adding to the store"
- "com.apple.Messages"
- "com.apple.Messages.EnhancedLinkSecurityStoreConnection.queue"
- "com.apple.imagent.EnhancedLinkSecurityStore"
- "com.apple.messages.EnhancedLinkSecurity"

```
