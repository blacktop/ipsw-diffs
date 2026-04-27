## AppleMediaServicesUI

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI`

```diff

-7.5.8.0.0
-  __TEXT.__text: 0x1fc434
-  __TEXT.__auth_stubs: 0x4b20
-  __TEXT.__objc_methlist: 0x10c04
+7.5.10.2.1
+  __TEXT.__text: 0x1fcee0
+  __TEXT.__auth_stubs: 0x4b30
+  __TEXT.__objc_methlist: 0x10c34
   __TEXT.__const: 0xd8b4
   __TEXT.__gcc_except_tab: 0x1a20
-  __TEXT.__oslogstring: 0xa606
-  __TEXT.__cstring: 0xdb8d
+  __TEXT.__oslogstring: 0xa715
+  __TEXT.__cstring: 0xdc2d
   __TEXT.__dlopen_cstrs: 0xe35
   __TEXT.__ustring: 0x13a
   __TEXT.__swift5_typeref: 0xfe30
   __TEXT.__constg_swiftt: 0x54c0
-  __TEXT.__swift5_reflstr: 0x28e5
+  __TEXT.__swift5_reflstr: 0x28f5
   __TEXT.__swift5_assocty: 0x10f8
   __TEXT.__swift5_fieldmd: 0x2eb4
   __TEXT.__swift5_builtin: 0x1cc

   __TEXT.__swift_as_entry: 0x1b4
   __TEXT.__swift_as_ret: 0x1f8
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x90f0
+  __TEXT.__unwind_info: 0x90f8
   __TEXT.__eh_frame: 0x63f0
   __TEXT.__objc_classname: 0x3924
-  __TEXT.__objc_methname: 0x27b0f
+  __TEXT.__objc_methname: 0x27c7f
   __TEXT.__objc_methtype: 0x8551
-  __TEXT.__objc_stubs: 0x1c4a0
+  __TEXT.__objc_stubs: 0x1c560
   __DATA_CONST.__got: 0x1c40
   __DATA_CONST.__const: 0x3e28
   __DATA_CONST.__objc_classlist: 0xa58
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f08
+  __DATA_CONST.__objc_selrefs: 0x8f40
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x688
   __DATA_CONST.__objc_arraydata: 0x340
-  __AUTH_CONST.__auth_got: 0x25a0
+  __AUTH_CONST.__auth_got: 0x25a8
   __AUTH_CONST.__const: 0x87a0
-  __AUTH_CONST.__cfstring: 0xb1c0
-  __AUTH_CONST.__objc_const: 0x206e8
+  __AUTH_CONST.__cfstring: 0xb200
+  __AUTH_CONST.__objc_const: 0x20748
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x7a90
   __AUTH.__data: 0x5188
-  __DATA.__objc_ivar: 0x1104
-  __DATA.__data: 0x67f0
+  __DATA.__objc_ivar: 0x110c
+  __DATA.__data: 0x6800
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0xabf0
   __DATA.__common: 0x258

   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B66D6A6E-7496-390A-8D28-55E8F6E00085
-  Functions: 13994
-  Symbols:   26705
-  CStrings:  11665
+  UUID: ED02DBF8-D0D3-33A7-8B45-0B30B8D433F3
+  Functions: 14002
+  Symbols:   26734
+  CStrings:  11684
 
Symbols:
+ -[AMSUIWebCameraReaderPageModel invalidDocumentAction]
+ -[AMSUIWebCameraReaderPageModel setInvalidDocumentAction:]
+ -[AMSUIWebCameraReaderViewController detectedInvalidDocument]
+ -[AMSUIWebCameraReaderViewController setDetectedInvalidDocument:]
+ _AudioServicesPlaySystemSound
+ _OBJC_IVAR_$_AMSUIWebCameraReaderPageModel._invalidDocumentAction
+ _OBJC_IVAR_$_AMSUIWebCameraReaderViewController._detectedInvalidDocument
+ ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.102
+ ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.111
+ ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.115
+ ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.123
+ ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.125
+ _objc_msgSend$continuousMode
+ _objc_msgSend$detectedInvalidDocument
+ _objc_msgSend$invalidDocumentAction
+ _objc_msgSend$setContinuousMode:
+ _objc_msgSend$setDetectedInvalidDocument:
+ _objc_msgSend$setHideCardInfoOverlay:
- ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.108
- ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.112
- ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.120
- ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.122
- ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.99
CStrings:
+ "%{public}@: Controller created with AMSUIWebCameraReaderPageTypeManual. This type should use AMSUIWebManualCaptureView."
+ "%{public}@: [%{public}@] Recognized credit card during ID scanning"
+ "%{public}@: [%{public}@] Setting up Camera Reader for dual ID/Credit Card detection"
+ "Failed to encode password settings as UTF-8 string"
+ "Failed to format password settings: "
+ "T@\"<AMSUIWebActionRunnable>\",&,N,V_invalidDocumentAction"
+ "TB,N,V_detectedInvalidDocument"
+ "_detectedInvalidDocument"
+ "_invalidDocumentAction"
+ "continuousMode"
+ "detectedInvalidDocument"
+ "invalidDocumentAction"
+ "setContinuousMode:"
+ "setDetectedInvalidDocument:"
+ "setHideCardInfoOverlay:"
+ "setInvalidDocumentAction:"
+ "\xf0q"
- "\xf0a"

```
