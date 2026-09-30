## DataFlow

> `/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow`

```diff

-1004.28.0.0.0
-  __TEXT.__text: 0x2c778
-  __TEXT.__auth_stubs: 0x1310
+1004.33.0.0.0
+  __TEXT.__text: 0x2bff0
+  __TEXT.__auth_stubs: 0x13c0
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x2494
-  __TEXT.__cstring: 0x588
-  __TEXT.__swift5_typeref: 0x1072
-  __TEXT.__constg_swiftt: 0x1278
-  __TEXT.__swift5_reflstr: 0x79a
-  __TEXT.__swift5_fieldmd: 0xb58
-  __TEXT.__swift5_proto: 0x190
-  __TEXT.__swift5_types: 0xcc
-  __TEXT.__swift5_assocty: 0x180
-  __TEXT.__oslogstring: 0x200
-  __TEXT.__swift_as_entry: 0x6c
+  __TEXT.__const: 0x2554
+  __TEXT.__cstring: 0x548
+  __TEXT.__swift5_typeref: 0x10a2
+  __TEXT.__constg_swiftt: 0x1288
+  __TEXT.__swift5_reflstr: 0x81a
+  __TEXT.__swift5_fieldmd: 0xc08
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_assocty: 0x1b0
+  __TEXT.__swift5_proto: 0x194
+  __TEXT.__swift5_types: 0xe0
+  __TEXT.__oslogstring: 0x340
+  __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__swift5_capture: 0x5c8
-  __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0xbd0
-  __TEXT.__eh_frame: 0x191c
+  __TEXT.__swift5_capture: 0x594
+  __TEXT.__swift_as_ret: 0x4c
+  __TEXT.__swift5_mpenum: 0x3c
+  __TEXT.__unwind_info: 0xb70
+  __TEXT.__eh_frame: 0x16d0
   __TEXT.__objc_classname: 0x9
-  __TEXT.__objc_methname: 0x26a
+  __TEXT.__objc_methname: 0x2cf
   __TEXT.__objc_methtype: 0xad
   __DATA_CONST.__got: 0x290
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x110
+  __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x988
-  __AUTH_CONST.__auth_ptr: 0x3f0
-  __AUTH_CONST.__const: 0x1f38
-  __AUTH_CONST.__objc_const: 0xa78
-  __AUTH.__data: 0x4b0
-  __DATA.__data: 0x840
-  __DATA.__bss: 0x1c80
-  __DATA_DIRTY.__data: 0xe48
-  __DATA_DIRTY.__bss: 0x1380
+  __AUTH_CONST.__auth_got: 0x9e0
+  __AUTH_CONST.__auth_ptr: 0x468
+  __AUTH_CONST.__const: 0x1eb8
+  __AUTH_CONST.__objc_const: 0x970
+  __AUTH.__data: 0x550
+  __DATA.__data: 0x898
+  __DATA.__bss: 0x1d80
+  __DATA_DIRTY.__data: 0xdc8
+  __DATA_DIRTY.__bss: 0x1300
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 948
-  Symbols:   227
-  CStrings:  125
+  Functions: 955
+  Symbols:   235
+  CStrings:  133
 
Symbols:
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_UIApplication
+ _UIApplicationDidEnterBackgroundNotification
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x24
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_dynamicCastClass
+ _swift_getForeignTypeMetadata
+ _swift_release_n
+ _swift_unknownObjectRetain_n
- _UIApplicationWillResignActiveNotification
- _objc_release
- _objc_retain
- _objc_retain_x23
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ " pending "
+ " voucher pending "
+ "Database closed while executing %s, closing connection"
+ "Database:: attempting close"
+ "Database:: preemptively closing database now that we are no longer active"
+ "Database::Completed executing %s transaction"
+ "Database::Executing %s transaction"
+ "Database::close (%ld)"
+ "Failed to open database connection to %{public}s: %{public}s"
+ "_TtC8DataFlow33ApplicationBackgroundTaskProvider"
+ "appState"
+ "application"
+ "applicationState"
+ "backgroundTaskProvider"
+ "beginBackgroundTaskWithExpirationHandler:"
+ "endBackgroundTask:"
+ "init"
+ "sharedApplication"
+ "withTransaction(_:)"
- "Database at %{mask.hash}s"
- "Database::close"
- "_TtC8DataFlow23ApplicationStateMonitor"
- "applicationStateMonitor"
- "applicationStateObserver"
- "continuations"
- "database"
- "encoder"
- "enterForegroundToken"
- "requireConnection()"
- "willResignActiveToken"

```
