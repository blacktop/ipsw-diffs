## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

-512.1.0.0.0
-  __TEXT.__text: 0x2f0d50
+515.0.0.0.0
+  __TEXT.__text: 0x2f14b0
   __TEXT.__auth_stubs: 0x2c90
-  __TEXT.__objc_methlist: 0x1e4c0
-  __TEXT.__cstring: 0xbf0e
-  __TEXT.__const: 0x5f04
+  __TEXT.__objc_methlist: 0x1e5a0
+  __TEXT.__cstring: 0xbf20
+  __TEXT.__const: 0x5f14
   __TEXT.__constg_swiftt: 0xa90
   __TEXT.__swift5_typeref: 0xca6
   __TEXT.__swift5_reflstr: 0x8f1

   __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x23bd8
-  __TEXT.__oslogstring: 0xc3b6
+  __TEXT.__gcc_except_tab: 0x23b44
+  __TEXT.__oslogstring: 0xc65a
   __TEXT.__dlopen_cstrs: 0x511
   __TEXT.__ustring: 0x10a
-  __TEXT.__unwind_info: 0xeed0
+  __TEXT.__unwind_info: 0xef10
   __TEXT.__eh_frame: 0x14f8
-  __TEXT.__objc_classname: 0x524c
-  __TEXT.__objc_methname: 0x608a9
-  __TEXT.__objc_methtype: 0x19af6
-  __TEXT.__objc_stubs: 0x38cc0
-  __DATA_CONST.__got: 0x1e40
-  __DATA_CONST.__const: 0x69c8
-  __DATA_CONST.__objc_classlist: 0x1010
+  __TEXT.__objc_classname: 0x528c
+  __TEXT.__objc_methname: 0x60b04
+  __TEXT.__objc_methtype: 0x19b66
+  __TEXT.__objc_stubs: 0x38e20
+  __DATA_CONST.__got: 0x1e58
+  __DATA_CONST.__const: 0x69f0
+  __DATA_CONST.__objc_classlist: 0x1018
   __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x758
+  __DATA_CONST.__objc_protolist: 0x760
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11088
+  __DATA_CONST.__objc_selrefs: 0x110f8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0xd00
+  __DATA_CONST.__objc_superrefs: 0xd08
   __DATA_CONST.__objc_arraydata: 0x820
   __AUTH_CONST.__auth_got: 0x1660
-  __AUTH_CONST.__auth_ptr: 0x530
-  __AUTH_CONST.__const: 0x5788
+  __AUTH_CONST.__auth_ptr: 0x540
+  __AUTH_CONST.__const: 0x5768
   __AUTH_CONST.__cfstring: 0xd600
-  __AUTH_CONST.__objc_const: 0x4cd80
+  __AUTH_CONST.__objc_const: 0x4cf38
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_arrayobj: 0x618
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x3c0
-  __AUTH.__objc_data: 0x9200
+  __AUTH.__objc_data: 0x9250
   __AUTH.__data: 0x280
-  __DATA.__objc_ivar: 0x2968
-  __DATA.__data: 0x5fb8
+  __DATA.__objc_ivar: 0x2978
+  __DATA.__data: 0x6018
   __DATA.__bss: 0x4f90
   __DATA.__common: 0x120
   __DATA_DIRTY.__objc_ivar: 0x1080

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting
   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16081
-  Symbols:   19397
-  CStrings:  20073
+  Functions: 16099
+  Symbols:   19419
+  CStrings:  20106
 
Symbols:
+ _MCEffectiveSettingsChangedNotification
+ _OBJC_CLASS_$_PKImageGenerationController
+ _OBJC_METACLASS_$_PKImageGenerationController
+ _OBJC_CLASS_$_MCProfileConnection
CStrings:
+ "Handle managed configuration effective settings did change notification, isImageGenerationAllowed: %!{(MISSING)BOOL}d"
+ "v24@0:8@\"PKImageGenerationController\"16"
+ "_lockHiddenNotify:"
+ "_unlockHiddenNotify:"
+ "_cachedShouldShowImageGenerationUI"
+ "_handleGenerationModelAvailabilityDidChangeNotification:"
+ "T@\"<PKImageGenerationControllerDelegate>\",W,N,V_delegate"
+ "_purgeResources"
+ "isImageGenerationAllowed"
+ "isGenerationToolEnabled: %!{(MISSING)BOOL}d"
+ "Observe managed configuration effective settings change notification"
+ "_reduceMemoryFootprint"
+ "Notify generation tool controller's state did change"
+ "\xe1"
+ "_generationModelAvailabilityStatus"
+ "@\"<PKImageGenerationControllerDelegate>\""
+ "_handleModelAvailabilityStatusDidChange:completion:"
+ "_notifyStateDidChangeIfNecessary"
+ "Remove generation tool, isGenerationToolEnabled: %!{(MISSING)BOOL}d, isImageGenerationAllowed: %!{(MISSING)BOOL}d, isGenerationModelAvailable: %!{(MISSING)BOOL}d"
+ "_cancelCurrentStrokeAndReduceMemoryFootprint"
+ "imageGenerationControllerShouldShowImageGenerationUIDidChange:"
+ "Observe generation model availability change notification"
+ "sharedConnection"
+ "_updateGenerationToolInstallation"
+ "Unexpected column index for available transcription path"
+ "PKImageGenerationController"
+ "_shouldNotifyDuringUpdate"
+ "\x01\x12\x15RDE"
+ "_imageGenerationController"
+ "!%!\(MISSING)x12%!"(MISSING)
+ "com.apple.Compose"
+ "_handleManagedConfigurationEffectiveSettingsDidChangeNotification:"
+ "\xf0\xa4"
+ "Handle model availability did change notification, isGenerationModelAvailable: %!{(MISSING)BOOL}d"
+ "shouldShowImageGenerationUI"
+ "Unexpected row index in available transcription path"
+ "@\"PKImageGenerationController\""
+ "Install generation tool"
+ "PKImageGenerationControllerDelegate"
+ "isGenerationToolEnabled"
- "updateAllToolPickersWithGenerationToolAvailability"
- "\x01\x12\x14RDE"
- "\xd1"
- "!%!\(MISSING)x11%!"(MISSING)
- "_graphableIsSet"
- "generationModelAvailabilityStatus"
- "\xf0\x94"

```
