## AppleDeviceManagementHIDFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleDeviceManagementHIDFilter.plugin/Contents/MacOS/AppleDeviceManagementHIDFilter`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_selrefs`

```diff

-10400.22.0.0.0
-  __TEXT.__text: 0xc4e0
-  __TEXT.__auth_stubs: 0x830
+10410.2.0.0.0
+  __TEXT.__text: 0x1175c
+  __TEXT.__auth_stubs: 0xa90
   __TEXT.__objc_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x56c
-  __TEXT.__const: 0x71c
+  __TEXT.__objc_methlist: 0x57c
+  __TEXT.__const: 0xb0c
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x72a
-  __TEXT.__objc_methname: 0xf74
-  __TEXT.__oslogstring: 0xbb7
-  __TEXT.__objc_classname: 0x136
-  __TEXT.__objc_methtype: 0x53d
-  __TEXT.__swift5_typeref: 0x29f
-  __TEXT.__constg_swiftt: 0x3bc
-  __TEXT.__swift5_reflstr: 0x1f6
-  __TEXT.__swift5_fieldmd: 0x1ac
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_capture: 0x40
+  __TEXT.__cstring: 0x7ea
+  __TEXT.__objc_methname: 0xfe4
+  __TEXT.__oslogstring: 0xdc7
+  __TEXT.__objc_classname: 0x296
+  __TEXT.__objc_methtype: 0x54d
+  __TEXT.__swift5_typeref: 0x46b
+  __TEXT.__constg_swiftt: 0x5c4
+  __TEXT.__swift5_reflstr: 0x2a6
+  __TEXT.__swift5_fieldmd: 0x2c4
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_mpenum: 0x14
+  __TEXT.__swift5_capture: 0xec
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x28
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x3f0
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x3d8
+  __TEXT.__unwind_info: 0x598
+  __TEXT.__eh_frame: 0x208
+  __DATA_CONST.__const: 0x7c8
   __DATA_CONST.__cfstring: 0x460
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x428
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__auth_ptr: 0x138
-  __DATA.__objc_const: 0xb90
+  __DATA_CONST.__auth_got: 0x558
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__auth_ptr: 0x1b0
+  __DATA.__objc_const: 0xec8
   __DATA.__objc_selrefs: 0x3f0
   __DATA.__objc_ivar: 0x40
-  __DATA.__objc_data: 0x6d8
-  __DATA.__data: 0x428
-  __DATA.__bss: 0x570
+  __DATA.__objc_data: 0x770
+  __DATA.__data: 0x7f8
+  __DATA.__bss: 0x840
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 273
-  Symbols:   145
-  CStrings:  381
+  Functions: 391
+  Symbols:   170
+  CStrings:  407
 
Symbols:
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryGetRegistryEntryID
+ _IOServiceAddMatchingNotification
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _swift_allocError
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_getSingletonMetadata
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
CStrings:
+ "AppleMultitouchDevice"
+ "DeviceUsagePairs"
+ "Failed to fetch device usages from service %s"
+ "Failed to find matching MT service"
+ "Failed to read driver properties from service %s"
+ "Failed to register matching notifications"
+ "Failed to register termination notifications"
+ "Failed to start MT matching: Device does not publish a valid %s"
+ "Failed to start service matcher: %s"
+ "IOServiceFirstMatch"
+ "IOServiceTerminate"
+ "Matching callback fired without valid context"
+ "Skipping service %s as it is missing device usage pair (%s,%s)"
+ "Updating device with matched service properties"
+ "_TtC30AppleDeviceManagementHIDFilter12IOKitService"
+ "_TtC30AppleDeviceManagementHIDFilter14ServiceMatcher"
+ "_TtCC30AppleDeviceManagementHIDFilter14ServiceMatcherP33_59F123CA77F412DBA0C3FFA209B73FA612EventContext"
+ "_TtCC30AppleDeviceManagementHIDFilter14ServiceMatcherP33_59F123CA77F412DBA0C3FFA209B73FA612Subscription"
+ "backgroundTask"
+ "com.apple.hid.AppleTopCase.DeviceInfoManager.ServiceMatcher"
+ "com.apple.hid.AppleTopCase.ServiceMatcher"
+ "continuation"
+ "iterators"
+ "matchedContext"
+ "notificationPort"
+ "phase"
+ "terminatedContext"
- "com.apple.hid.AppleTopCase.DeviceInfoManager"
```
