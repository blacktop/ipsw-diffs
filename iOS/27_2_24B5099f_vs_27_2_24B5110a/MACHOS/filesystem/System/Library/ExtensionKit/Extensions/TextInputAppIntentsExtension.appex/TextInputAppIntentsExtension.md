## TextInputAppIntentsExtension

> `System/Library/ExtensionKit/Extensions/TextInputAppIntentsExtension.appex/TextInputAppIntentsExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`

```diff

 3568.1.8.0.0
-  __TEXT.__text: 0x1b0
-  __TEXT.__auth_stubs: 0x70
-  __TEXT.__swift5_typeref: 0x46
-  __TEXT.__const: 0x90
-  __TEXT.__swift5_reflstr: 0xe
-  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__text: 0x3960
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_stubs: 0xa0
+  __TEXT.__swift5_typeref: 0x289
+  __TEXT.__const: 0x696
+  __TEXT.__swift5_reflstr: 0xb3
+  __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x28
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__const: 0x98
+  __TEXT.__constg_swiftt: 0xe0
+  __TEXT.__swift5_fieldmd: 0x70
+  __TEXT.__swift5_proto: 0x5c
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__cstring: 0x105
+  __TEXT.__oslogstring: 0x41
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0xc
+  __TEXT.__objc_methname: 0xa4
+  __TEXT.__unwind_info: 0x268
+  __TEXT.__eh_frame: 0x1f0
+  __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x38
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__auth_ptr: 0x48
-  __DATA.__data: 0x10
+  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__auth_ptr: 0x3a0
+  __DATA.__objc_selrefs: 0x28
+  __DATA.__data: 0x1a8
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/CoreTransferable.framework/CoreTransferable
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9
-  Symbols:   22
-  CStrings:  0
+  Functions: 137
+  Symbols:   80
+  CStrings:  13
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_TIPreferencesController
+ ___chkstk_darwin
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ _bzero
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_msgSend
+ _objc_opt_self
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x8
+ _os_log_type_enabled
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_errorRelease
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_x19
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
CStrings:
+ "Fetch Keyboard Preferences Intent"
+ "IDS identifier of remote device"
+ "Keyboard Preferences"
+ "Personal Unique Identifier of this device"
+ "Register remote device: %s as %s"
+ "TextInputAppIntentsExtension/FetchKeyboardPreferencesIntent.swift"
+ "Unregister remote device"
+ "_appIntentPreferencesKeys"
+ "com.apple.TextInput"
+ "dataWithPropertyList:format:options:error:"
+ "registerRemoteDeviceWithIDSIdentifier:user:"
+ "sharedPreferencesController"
+ "valueForPreferenceKey:"
```
