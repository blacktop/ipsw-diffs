## IntelligencePlatformComputeService

> `/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0xd9f0
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0xd0
+166.15.0.0.0
+  __TEXT.__text: 0xea2c
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_methlist: 0x234
   __TEXT.__const: 0x262
-  __TEXT.__cstring: 0x658
+  __TEXT.__cstring: 0x398
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x633
+  __TEXT.__oslogstring: 0x693
   __TEXT.__objc_methname: 0x33b
   __TEXT.__constg_swiftt: 0x178
   __TEXT.__swift5_typeref: 0x35f

   __TEXT.__swift5_types: 0x14
   __TEXT.__objc_classname: 0x4d
   __TEXT.__objc_methtype: 0x19f
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x498
-  __TEXT.__eh_frame: 0xe50
-  __DATA_CONST.__auth_got: 0x450
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x590
+  __TEXT.__unwind_info: 0x480
+  __TEXT.__eh_frame: 0xee8
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x658
-  __DATA.__objc_selrefs: 0xb0
+  __DATA.__objc_const: 0x3c8
+  __DATA.__objc_selrefs: 0x150
   __DATA.__objc_data: 0x2d8
   __DATA.__data: 0x4a8
-  __DATA.__common: 0x70
+  __DATA.__common: 0x60
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 233
-  Symbols:   240
-  CStrings:  127
+  Symbols:   234
+  CStrings:  113
 
Symbols:
+ _objc_retain_x27
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x24
- _swift_FORCE_LOAD_$_swiftFoundation.1
CStrings:
+ "IntelligencePlatformComputeService: cancelling task %{public}s"
+ "IntelligencePlatformComputeService: clearViewWithName called [name: %{public}s, fullRebuild: %{bool}d]"
+ "IntelligencePlatformComputeService: truncateViewWithName called [name: %{public}s, fullRebuild: %{bool}d]"
+ "IntelligencePlatformComputeService: update %{public}s returning responses"
+ "IntelligencePlatformComputeService: updateGroup: n:%{public}s failed: %s"
+ "IntelligencePlatformComputeService: updateGroupWithName %{public}s begining update"
+ "IntelligencePlatformComputeService: updateGroupWithName %{public}s called with %ld namesAndRequests"
+ "IntelligencePlatformComputeService: updateGroupWithName %{public}s returning responses"
+ "IntelligencePlatformComputeService: updateView: n:%{public}s failed: %s"
+ "IntelligencePlatformComputeService: updateViewWithName %{public}s begining update"
+ "IntelligencePlatformComputeService: updateViewWithName %{public}s called"
- "Insufficient space allocated to copy string contents"
- "IntelligencePlatformComputeService: cancelling task %s"
- "IntelligencePlatformComputeService: clearViewWithName called [name: %s, fullRebuild: %{bool}d]"
- "IntelligencePlatformComputeService: truncateViewWithName called [name: %s, fullRebuild: %{bool}d]"
- "IntelligencePlatformComputeService: update %s returning responses"
- "IntelligencePlatformComputeService: updateGroup: n:%s failed: %s"
- "IntelligencePlatformComputeService: updateGroupWithName %s begining update"
- "IntelligencePlatformComputeService: updateGroupWithName %s called with %ld namesAndRequests"
- "IntelligencePlatformComputeService: updateGroupWithName %s returning responses"
- "IntelligencePlatformComputeService: updateView: n:%s failed: %s"
- "IntelligencePlatformComputeService: updateViewWithName %s begining update"
- "IntelligencePlatformComputeService: updateViewWithName %s called"
- "Swift/ContiguousArrayBuffer.swift"
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
- "invalid Collection: less than 'count' elements in collection"

```
