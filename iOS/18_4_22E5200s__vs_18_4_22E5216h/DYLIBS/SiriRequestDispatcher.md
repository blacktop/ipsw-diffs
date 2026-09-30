## SiriRequestDispatcher

> `/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher`

```diff

-3404.62.2.0.0
-  __TEXT.__text: 0x2752c
-  __TEXT.__auth_stubs: 0x12d0
+3404.69.1.0.0
+  __TEXT.__text: 0x2c00c
+  __TEXT.__auth_stubs: 0x1350
   __TEXT.__objc_methlist: 0x540
-  __TEXT.__const: 0x1500
-  __TEXT.__cstring: 0xdc8
-  __TEXT.__swift5_typeref: 0xbfb
-  __TEXT.__swift5_fieldmd: 0x684
-  __TEXT.__constg_swiftt: 0xf18
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x6d8
+  __TEXT.__const: 0x15a0
+  __TEXT.__cstring: 0xe08
+  __TEXT.__swift5_typeref: 0xc1d
+  __TEXT.__swift5_fieldmd: 0x6f0
+  __TEXT.__constg_swiftt: 0xfc8
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0x738
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_proto: 0x80
-  __TEXT.__swift5_types: 0x94
-  __TEXT.__oslogstring: 0x1f97
-  __TEXT.__swift5_capture: 0x380
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__swift5_types: 0xa0
+  __TEXT.__oslogstring: 0x2107
+  __TEXT.__swift5_capture: 0x384
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x9c8
-  __TEXT.__eh_frame: 0x960
+  __TEXT.__unwind_info: 0xaf0
+  __TEXT.__eh_frame: 0xd48
   __TEXT.__objc_classname: 0xb1
   __TEXT.__objc_methname: 0x1336
   __TEXT.__objc_methtype: 0x778
-  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_protorefs: 0x58
-  __AUTH_CONST.__auth_got: 0x968
-  __AUTH_CONST.__auth_ptr: 0x2d8
-  __AUTH_CONST.__const: 0x14b0
-  __AUTH_CONST.__objc_const: 0x3c38
+  __AUTH_CONST.__auth_got: 0x9a8
+  __AUTH_CONST.__auth_ptr: 0x318
+  __AUTH_CONST.__const: 0x15b8
+  __AUTH_CONST.__objc_const: 0x3c40
   __AUTH.__objc_data: 0xb0
   __AUTH.__data: 0x28
-  __DATA.__data: 0x6c8
-  __DATA.__bss: 0xb00
+  __DATA.__data: 0x898
+  __DATA.__bss: 0xb80
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xd98
+  __DATA_DIRTY.__data: 0xd08
   __DATA_DIRTY.__common: 0xb8
-  __DATA_DIRTY.__bss: 0x300
+  __DATA_DIRTY.__bss: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1153
-  Symbols:   534
-  CStrings:  469
+  Functions: 1248
+  Symbols:   593
+  CStrings:  479
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
CStrings:
+ "%s received %{public}s with messageId: %{public}s: %@"
+ "Beginning message event loop for session: %s"
+ "Dispatching message %s"
+ "Ending session %s"
+ "Ending the message event loop"
+ "Launching task for session: %s"
+ "Received SessionEndedMessage: %s for a non-existing session: %s, ignoring"
+ "Received SessionMessage: %s for a non-existing session: %s, ignoring"
+ "Received SessionStartedMessage for an existing session: %s, ignoring"
+ "Received non-Session message %s, ignoring"
+ "TaskAwaitTime"
+ "_currentTaskContainer"
+ "lock"
+ "messageHandlersContainer"
+ "tasksStorage"
- "Lifecycle of %{public}s has ended before message dispatch could start."
- "Lifecycle of %{public}s has ended before receiving next %{public}s."
- "container"
- "publisher"
- "stream"

```
