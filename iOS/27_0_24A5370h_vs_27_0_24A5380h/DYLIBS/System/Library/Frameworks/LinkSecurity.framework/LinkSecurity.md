## LinkSecurity

> `/System/Library/Frameworks/LinkSecurity.framework/LinkSecurity`

```diff

-  __TEXT.__text: 0x0
-  __TEXT.__const: 0x42
-  __DATA_CONST.__const: 0x30
+  __TEXT.__text: 0x491c
+  __TEXT.__objc_methlist: 0x18c
+  __TEXT.__const: 0x298
+  __TEXT.__swift5_typeref: 0x195
+  __TEXT.__swift5_fieldmd: 0x80
+  __TEXT.__constg_swiftt: 0x180
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__swift5_reflstr: 0x38
+  __TEXT.__cstring: 0x126
+  __TEXT.__swift5_capture: 0x80
+  __TEXT.__oslogstring: 0x1c0
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_cont: 0x8
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__eh_frame: 0x208
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x38
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x138
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__got: 0x88
+  __AUTH_CONST.__const: 0x288
+  __AUTH_CONST.__objc_const: 0x9e8
+  __AUTH_CONST.__auth_got: 0x340
+  __AUTH.__objc_data: 0x70
+  __AUTH.__data: 0x1f8
+  __DATA.__data: 0x1f0
+  __DATA.__common: 0x8
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 0
-  Symbols:   6
-  CStrings:  0
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 133
+  Symbols:   100
+  CStrings:  17
 
Symbols:
+ _IMGetDomainBoolForKey
+ _IMGetDomainValueForKey
+ _IMSetDomainBoolForKey
+ _IMSetDomainValueForKey
+ _OBJC_CLASS_$_LSLinkSecurityManager
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$_LSLinkSecurityManager
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ ___chkstk_darwin
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_stdlib_bridgeErrorToNSError
+ _malloc_size
+ _objc_allocWithZone
+ _objc_msgSend
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _os_log_type_enabled
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_resume
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
CStrings:
+ "Adding %ld URL(s) to the store"
+ "Adding URL to the store"
+ "Checking if URL is in the store"
+ "Checking sentinel value: %{bool}d"
+ "Connection interrupted"
+ "Connection invalidated"
+ "Could not connect with error: %@"
+ "EnhancedLinkSecuritySentinelKey"
+ "EnhancedLinkSecurityStoreConnection"
+ "LSLinkSecurityManager"
+ "No URLs were for a website, not adding any to the store"
+ "Starting connection to EnhancedLinkSecurityStore"
+ "URL was not for a website, not adding to the store"
+ "com.apple.Messages"
+ "com.apple.Messages.EnhancedLinkSecurityStoreConnection.queue"
+ "com.apple.imagent.EnhancedLinkSecurityStore"
+ "com.apple.messages.EnhancedLinkSecurity"

```
