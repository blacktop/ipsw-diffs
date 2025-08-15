## ManagedAppsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber`

```diff

-500.25.3.7.0
-  __TEXT.__text: 0xd5d0
-  __TEXT.__auth_stubs: 0xd00
+500.25.5.10.0
+  __TEXT.__text: 0xed98
+  __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_methlist: 0xe4
   __TEXT.__const: 0x192
-  __TEXT.__swift5_typeref: 0x296
-  __TEXT.__objc_methname: 0x700
+  __TEXT.__cstring: 0xe80
+  __TEXT.__swift5_typeref: 0x298
+  __TEXT.__objc_methname: 0x76e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xb0d
-  __TEXT.__constg_swiftt: 0x134
+  __TEXT.__constg_swiftt: 0x144
   __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_types: 0x10
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x306
-  __TEXT.__unwind_info: 0x2ac
-  __TEXT.__eh_frame: 0x640
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x208
+  __TEXT.__unwind_info: 0x304
+  __TEXT.__eh_frame: 0x728
+  __DATA_CONST.__auth_got: 0x6a0
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x690
-  __DATA.__objc_selrefs: 0x1a0
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__objc_data: 0x288
-  __DATA.__data: 0x3f8
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x58
+  __DATA.__objc_const: 0x670
+  __DATA.__objc_selrefs: 0x1c8
+  __DATA.__objc_data: 0x298
+  __DATA.__data: 0x458
   __DATA.__common: 0x30
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 080E400D-D36E-3C42-81E5-50AD94361832
-  Functions: 165
-  Symbols:   133
-  CStrings:  188
+  UUID: 14892F9E-2651-36BF-B08C-7299E1E09DD9
+  Functions: 180
+  Symbols:   138
+  CStrings:  214
 
Symbols:
+ _OBJC_CLASS_$_DMFApp
+ _OBJC_CLASS_$_DMFFetchAppsRequest
+ _OBJC_CLASS_$_DMFFetchAppsResultObject
+ _OBJC_CLASS_$_DMFStopManagingAppRequest
+ _objc_retain_x2
+ _objc_retain_x9
+ _swift_initStaticObject
+ _swift_release_n
- _OBJC_CLASS_$_DMFRemoveAppRequest
- _objc_retain_x24
- _objc_retain_x27
CStrings:
+ "Division by zero"
+ "Division results in an overflow"
+ "Failed to fetch DMF app data: %@"
+ "Failed to stop DMF managing app: %@"
+ "Fatal error"
+ "Fetched DMF app data for: %{public}s"
+ "Insufficient space allocated to copy string contents"
+ "Invalid status returned for: %@ - count: %ld"
+ "Stopped DMF managing app: %{public}s"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "appsByBundleIdentifier"
+ "bundleIdentifier"
+ "invalid Collection: less than 'count' elements in collection"
+ "setBundleIdentifiers:"
+ "setManagedAppsOnly:"
+ "setPropertyKeys:"
+ "setType:"
- "Apps cannot be used with enterprise persona"
- "Failed to remove DMF app data: %@"
- "Removed DMF app data for: %{public}s"
- "Wrong number of app status items for configuration UI: "

```
