## FindMyDaemonSupport

> `/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport`

```diff

-62.33.10.29.3
-  __TEXT.__text: 0x3f0bc
-  __TEXT.__auth_stubs: 0x1150
-  __TEXT.__objc_methlist: 0xb0
-  __TEXT.__const: 0x14dc
-  __TEXT.__cstring: 0xeb4
-  __TEXT.__oslogstring: 0xbf3
-  __TEXT.__constg_swiftt: 0xd1c
-  __TEXT.__swift5_typeref: 0xc92
-  __TEXT.__swift5_reflstr: 0x7aa
-  __TEXT.__swift5_fieldmd: 0x690
+62.34.7.11.22
+  __TEXT.__text: 0x3f600
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x25c
+  __TEXT.__const: 0x166c
+  __TEXT.__cstring: 0xd74
+  __TEXT.__oslogstring: 0xc23
+  __TEXT.__constg_swiftt: 0xd64
+  __TEXT.__swift5_typeref: 0xd1e
+  __TEXT.__swift5_reflstr: 0x7da
+  __TEXT.__swift5_fieldmd: 0x6e4
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x118
-  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift5_proto: 0x120
+  __TEXT.__swift5_types: 0x78
+  __TEXT.__swift_as_entry: 0x234
+  __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_capture: 0x41c
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_capture: 0x430
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1428
-  __TEXT.__eh_frame: 0x3900
-  __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methname: 0x4a0
+  __TEXT.__unwind_info: 0x1450
+  __TEXT.__eh_frame: 0x3a48
+  __TEXT.__objc_classname: 0x5a
+  __TEXT.__objc_methname: 0x4b9
   __TEXT.__objc_methtype: 0x342
-  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf0
-  __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x8a8
-  __AUTH_CONST.__auth_ptr: 0x360
-  __AUTH_CONST.__const: 0x1328
-  __AUTH_CONST.__objc_const: 0x1178
+  __DATA_CONST.__objc_selrefs: 0x1a0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __AUTH_CONST.__auth_got: 0x8f0
+  __AUTH_CONST.__auth_ptr: 0x390
+  __AUTH_CONST.__const: 0x1380
+  __AUTH_CONST.__objc_const: 0xf60
   __AUTH.__objc_data: 0x48
   __AUTH.__data: 0xa0
-  __DATA.__data: 0xb10
-  __DATA.__bss: 0x1380
+  __DATA.__data: 0xc38
+  __DATA.__bss: 0x1480
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xe8
-  __DATA_DIRTY.__data: 0x12f8
-  __DATA_DIRTY.__common: 0xc8
-  __DATA_DIRTY.__bss: 0xe80
+  __DATA_DIRTY.__data: 0x1468
+  __DATA_DIRTY.__common: 0xc0
+  __DATA_DIRTY.__bss: 0xe00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1325
-  Symbols:   185
-  CStrings:  253
+  Functions: 1359
+  Symbols:   198
+  CStrings:  251
 
Symbols:
+ _OBJC_CLASS_$_OS_dispatch_source
+ _exit
+ _objc_retain_x25
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_initStructMetadataWithLayoutString
- _notify_cancel
- _notify_get_state
- _notify_register_check
- _objc_release_x28
- _objc_retain_x26
- _objc_retain_x28
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
+ "%s %{public}s"
+ "Daemon exiting after receiving signal %d"
+ "FindMyDaemonSupport.daemon called before a daemon was created!"
+ "FindMyDaemonSupport/Daemon.swift"
+ "Global daemon shared instance already set to "
+ "OS_dispatch_source"
+ "OS_dispatch_source_signal"
+ "Signal Handling activated for %s"
+ "_TtC19FindMyDaemonSupport11DaemonActor"
+ "_setOpportunisticTopics:"
+ "init(mockServices:) can only be called from unit tests!"
+ "init(placeholderIndentifier:) can only be called from unit tests!"
+ "placeholderIndentifier"
+ "resetMock() can only be called from unit tests!"
+ "set(enabledTopics:)"
+ "set(opportunisticTopics:)"
+ "signalSource"
- "Division by zero"
- "Division results in an overflow"
- "Failed notify_register_check."
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "enabledTopics: %{public}s"
- "invalid Collection: less than 'count' elements in collection"

```
