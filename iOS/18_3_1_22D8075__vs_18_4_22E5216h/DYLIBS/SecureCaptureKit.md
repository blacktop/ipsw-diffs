## SecureCaptureKit

> `/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit`

```diff

-58.3.1.0.0
-  __TEXT.__text: 0x20750
-  __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x380
-  __TEXT.__const: 0xc84
-  __TEXT.__cstring: 0x15b5
+58.4.9.0.0
+  __TEXT.__text: 0x214c0
+  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__objc_methlist: 0x748
+  __TEXT.__const: 0xc94
+  __TEXT.__cstring: 0x1315
   __TEXT.__swift5_typeref: 0x9e4
-  __TEXT.__swift5_capture: 0x55c
+  __TEXT.__swift5_capture: 0x56c
   __TEXT.__swift5_reflstr: 0x310
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__constg_swiftt: 0x7d8

   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x50
-  __TEXT.__oslogstring: 0x9a7
-  __TEXT.__unwind_info: 0xa08
-  __TEXT.__eh_frame: 0x960
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__oslogstring: 0xbb4
+  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__eh_frame: 0xa48
   __TEXT.__objc_classname: 0xe5
-  __TEXT.__objc_methname: 0x155b
+  __TEXT.__objc_methname: 0x1572
   __TEXT.__objc_methtype: 0x626
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x618
+  __DATA_CONST.__objc_selrefs: 0x770
   __DATA_CONST.__objc_protorefs: 0x60
-  __AUTH_CONST.__auth_got: 0x888
+  __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__auth_ptr: 0x290
-  __AUTH_CONST.__const: 0x13b0
+  __AUTH_CONST.__const: 0x13d8
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x2088
-  __AUTH.__objc_data: 0x6c0
+  __AUTH_CONST.__objc_const: 0x1ce0
+  __AUTH.__objc_data: 0x688
   __AUTH.__data: 0x850
-  __DATA.__data: 0xa68
+  __DATA.__data: 0xa98
   __DATA.__common: 0x30
   __DATA.__bss: 0xc20
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 887
-  Symbols:   331
-  CStrings:  498
+  Functions: 875
+  Symbols:   339
+  CStrings:  487
 
Symbols:
+ _OBJC_CLASS_$_LCSExtension
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
CStrings:
+ "$__lazy_storage_$_logIdentifier"
+ "[%{public}s] Acquiring secure capture process assertion for bundle identifier: %s"
+ "[%{public}s] Adding unlocked attribute tag for the process assertion"
+ "[%{public}s] Can't create a capture extension scene"
+ "[%{public}s] Can't find the UI presentation manager"
+ "[%{public}s] Can't update Capture Extension mutable scene settings."
+ "[%{public}s] Capture Extension Scene Invalidated"
+ "[%{public}s] Capture Scene did activate."
+ "[%{public}s] Capture Scene did deactivate with error: %{public}s."
+ "[%{public}s] Capture Scene did deactivate."
+ "[%{public}s] Capture Scene did invalidate."
+ "[%{public}s] Capture Scene did receive actions: %{private}s"
+ "[%{public}s] Capture Scene did receive new client settings. clientSettings: %s, scene settings: %s"
+ "[%{public}s] Capture Scene sceneLayerManagerDidStartTrackingLayers"
+ "[%{public}s] Capture Scene sceneLayerManagerDidStopTrackingLayers"
+ "[%{public}s] Capture Scene sceneLayerManagerDidUpdateLayers"
+ "[%{public}s] Content state changed: %{public}s"
+ "[%{public}s] Creating capture scene to %{public}s."
+ "[%{public}s] Failed to acquire assertion: %{public}s"
+ "[%{public}s] Failed to acquire secure capture process assertion for bundle identifier: %s, no process identity found for the scene"
+ "[%{public}s] Failed to finalize current path %@"
+ "[%{public}s] Finalized path %@"
+ "[%{public}s] No Capture Scene found: %s"
+ "[%{public}s] No current path to finalize on scene deactivation..."
+ "[%{public}s] Reactivation: Setting transition context with launch actions: %s"
+ "[%{public}s] Runningboard assertion invalidated: %s"
+ "[%{public}s] Scene did deactivate but was foreground - reactivation needed."
+ "[%{public}s] Scene has not been initialized. Ignoring reactivation request."
+ "[%{public}s] Scene is already activated. Ignoring reactivation request."
+ "[%{public}s] Scene is not in foreground. Ignoring reactivation request."
+ "[%{public}s] Setting transition context with launch actions: %s"
+ "[%{public}s] Snapshot failed - %s"
+ "[%{public}s] Snapshot failed because there is no scene found"
+ "[%{public}s] Snapshot failed so backgrounding scene without updated snapshot: %{public}@"
+ "[%{public}s] Snapshot success - Updating layer."
+ "[%{public}s] Updating capture extension scene to %{public}s."
+ "[%{public}s] Updating presentationMode to: %{public}s - (forced? %{bool,public}d)."
+ "extensionWithIdentity:"
+ "init(info:responder:)"
+ "init(info:timeout:forResponseOn:withHandler:)"
+ "init(nibName:bundle:)"
- " Snapshot failed so backgrounding scene without updated snapshot: %{public}@"
- "Acquiring secure capture process assertion for bundle identifier: %s"
- "Adding unlocked attribute tag for the process assertion"
- "Can't find the UI presentation manager"
- "Can't update Capture Extension mutable scene settings."
- "Capture Extension Scene Invalidated"
- "Capture Scene did activate."
- "Capture Scene did deactivate with error: %{public}s."
- "Capture Scene did deactivate."
- "Capture Scene did invalidate."
- "Capture Scene did receive actions: %{private}s"
- "Capture Scene did receive new client settings. clientSettings: %s, scene settings: %s"
- "Capture Scene sceneLayerManagerDidStartTrackingLayers"
- "Capture Scene sceneLayerManagerDidStopTrackingLayers"
- "Capture Scene sceneLayerManagerDidUpdateLayers"
- "Content state changed: %{public}s"
- "Creating capture scene to %{public}s."
- "Division by zero"
- "Division results in an overflow"
- "Failed to acquire assertion: %{public}s"
- "Failed to acquire secure capture process assertion for bundle identifier: %s, no process identity found for the scene"
- "Failed to finalize current path %@"
- "Finalized path %@"
- "Insufficient space allocated to copy string contents"
- "No Capture Scene found: %s"
- "No current path to finalize on scene deactivation..."
- "Reactivation: Setting transition context with launch actions: %s"
- "Runningboard assertion invalidated: %s"
- "Scene did deactivate but was foreground - reactivation needed."
- "Scene has not been initialized. Ignoring reactivation request."
- "Scene is already activated. Ignoring reactivation request."
- "Scene is not in foreground. Ignoring reactivation request."
- "Setting transition context with launch actions: %s"
- "Snapshot failed - %s"
- "Snapshot failed because there is no scene found"
- "Snapshot success - Updating layer."
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
- "Updating capture extension scene to %{public}s."
- "Updating presentationMode to: %{public}s - (forced? %{bool,public}d)."
- "invalid Collection: less than 'count' elements in collection"

```
