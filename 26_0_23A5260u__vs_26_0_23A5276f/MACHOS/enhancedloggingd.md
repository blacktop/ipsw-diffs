## enhancedloggingd

> `/usr/libexec/enhancedloggingd`

```diff

-69.0.0.0.0
-  __TEXT.__text: 0x2cc40
+73.0.0.0.0
+  __TEXT.__text: 0x2d7e8
   __TEXT.__auth_stubs: 0x10b0
   __TEXT.__objc_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x7fc
-  __TEXT.__const: 0xe6c
-  __TEXT.__cstring: 0x123c
-  __TEXT.__objc_methname: 0x1f1a
+  __TEXT.__objc_methlist: 0x814
+  __TEXT.__const: 0xe90
+  __TEXT.__cstring: 0x124c
+  __TEXT.__objc_methname: 0x1f64
   __TEXT.__objc_classname: 0x85
-  __TEXT.__objc_methtype: 0x34a
-  __TEXT.__oslogstring: 0xbfc
-  __TEXT.__constg_swiftt: 0x458
+  __TEXT.__objc_methtype: 0x370
+  __TEXT.__oslogstring: 0xc6c
+  __TEXT.__constg_swiftt: 0x448
   __TEXT.__swift5_typeref: 0x777
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0x364
+  __TEXT.__swift5_reflstr: 0x354
   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_fieldmd: 0x304
   __TEXT.__swift5_proto: 0xac

   __TEXT.__swift_as_ret: 0x8c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x918
-  __TEXT.__eh_frame: 0x1258
+  __TEXT.__unwind_info: 0x930
+  __TEXT.__eh_frame: 0x1250
   __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__got: 0x448
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__const: 0xe70
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0xce8
-  __DATA.__objc_selrefs: 0x910
+  __DATA.__objc_const: 0xce0
+  __DATA.__objc_selrefs: 0x928
   __DATA.__objc_ivar: 0x38
-  __DATA.__objc_data: 0x390
-  __DATA.__data: 0x8c0
+  __DATA.__objc_data: 0x380
+  __DATA.__data: 0x8d0
   __DATA.__bss: 0x1490
   __DATA.__common: 0xe0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
+  - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon
   - /System/Library/PrivateFrameworks/EnhancedLogging.framework/EnhancedLogging
   - /System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 79A98369-B2A7-3A7D-BE0C-436937F691D3
-  Functions: 715
-  Symbols:   475
-  CStrings:  598
+  UUID: 58052D14-3F8E-3D07-9D50-B5B5E0DD6C9E
+  Functions: 721
+  Symbols:   477
+  CStrings:  607
 
Symbols:
+ _$s15EnhancedLogging12TargetDeviceV2id12serialNumber11deviceClass4name5model11productType8platform7isLocalACSS_SSSgS4SAC8PlatformOSbtcfC
+ _$s15EnhancedLogging12TargetDeviceV2idSSvg
+ _DEDCapabilityClassic
+ _DEDCapabilityCloudKit
+ _DEDCapabilityEnhancedExecution
+ _DEDCapabilityEnhancedExecutionV2
+ _DEDCapabilityMutableBugSession
+ _DEDCapabilitySessionState
+ _DEDCapabilityUploadErrorHandling
- _$s15EnhancedLogging12TargetDeviceV10identifier12serialNumber11deviceClass4name5model11productType8platform7isLocalACSS_SSSgS4SAC8PlatformOSbtcfC
- _$s15EnhancedLogging12TargetDeviceV10identifierSSvg
- _OBJC_CLASS_$_DEDCapability
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "All devices completed uploading successfully!"
+ "DEExtensionHostAppKey"
+ "One or more devices failed to upload"
+ "Upload failed for bug session %s: %@"
+ "Upload succeeded for bug session %s: %@"
+ "Waiting for additional devices to finish uploading..."
+ "bugSession:didFinishUploadingWithError:"
+ "didCompleteCollection"
+ "finishWithFailure"
+ "hasCapabilities:"
+ "setParameters:"
+ "uploadStatus"
+ "v32@0:8@\"DEDBugSession\"16@\"NSError\"24"
- "All uploads are complete!"
- "Not all uploads are complete yet; Waiting until all sessions completed for completing the collection session"
- "allCapabilities"
- "collectionCompletionState"
- "isUploadCompleted"

```
