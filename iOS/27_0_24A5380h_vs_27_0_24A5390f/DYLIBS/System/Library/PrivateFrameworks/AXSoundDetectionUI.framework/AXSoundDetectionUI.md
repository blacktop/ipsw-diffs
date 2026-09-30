## AXSoundDetectionUI

> `/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-534.0.0.0.0
-  __TEXT.__text: 0x56288
-  __TEXT.__objc_methlist: 0x22bc
+536.0.0.0.0
+  __TEXT.__text: 0x56f1c
+  __TEXT.__objc_methlist: 0x2344
   __TEXT.__const: 0xa18
-  __TEXT.__oslogstring: 0x623e
+  __TEXT.__oslogstring: 0x65b6
   __TEXT.__swift5_typeref: 0x79a
   __TEXT.__swift5_capture: 0x2ec
   __TEXT.__constg_swiftt: 0x844

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x38
-  __TEXT.__cstring: 0xff4
+  __TEXT.__cstring: 0x1029
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x70
-  __TEXT.__gcc_except_tab: 0x324
+  __TEXT.__gcc_except_tab: 0x344
   __TEXT.__dlopen_cstrs: 0x13e
-  __TEXT.__unwind_info: 0x1048
+  __TEXT.__unwind_info: 0x1078
   __TEXT.__eh_frame: 0x8b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x830
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1540
+  __DATA_CONST.__objc_selrefs: 0x15b8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__got: 0x690
   __AUTH_CONST.__const: 0x1118
-  __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__objc_const: 0x3500
+  __AUTH_CONST.__cfstring: 0xf60
+  __AUTH_CONST.__objc_const: 0x3678
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__auth_got: 0xa08
-  __AUTH.__objc_data: 0x1538
+  __AUTH_CONST.__auth_got: 0xa10
+  __AUTH.__objc_data: 0x1588
   __AUTH.__data: 0x300
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b8
   __DATA.__data: 0xa50
   __DATA.__bss: 0x950
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1447
-  Symbols:   2200
-  CStrings:  622
+  Functions: 1460
+  Symbols:   2242
+  CStrings:  636
 
Symbols:
+ -[AXSDCustomDetectionController _customPipedInFileUpdated]
+ -[AXSDCustomDetectionController _processCustomPipedFile]
+ -[AXSDKShotModelManager analyzeFileAtURL:forDetectors:]
+ -[_AXSDKShotFileObserver .cxx_destruct]
+ -[_AXSDKShotFileObserver detectorIdentifier]
+ -[_AXSDKShotFileObserver hasNotified]
+ -[_AXSDKShotFileObserver request:didFailWithError:]
+ -[_AXSDKShotFileObserver request:didProduceResult:]
+ -[_AXSDKShotFileObserver requestDidComplete:]
+ -[_AXSDKShotFileObserver setDetectorIdentifier:]
+ -[_AXSDKShotFileObserver setHasNotified:]
+ GCC_except_table563
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_SNClassificationResult
+ _OBJC_CLASS_$__AXSDKShotFileObserver
+ _OBJC_IVAR_$_AXSDCustomDetectionController._customPipeQueue
+ _OBJC_IVAR_$__AXSDKShotFileObserver._detectorIdentifier
+ _OBJC_IVAR_$__AXSDKShotFileObserver._hasNotified
+ _OBJC_METACLASS_$__AXSDKShotFileObserver
+ __OBJC_$_INSTANCE_METHODS__AXSDKShotFileObserver
+ __OBJC_$_INSTANCE_VARIABLES__AXSDKShotFileObserver
+ __OBJC_$_PROP_LIST__AXSDKShotFileObserver
+ __OBJC_CLASS_PROTOCOLS_$__AXSDKShotFileObserver
+ __OBJC_CLASS_RO_$__AXSDKShotFileObserver
+ __OBJC_METACLASS_RO_$__AXSDKShotFileObserver
+ ___37-[AXSDCustomDetectionController init]_block_invoke
+ ___58-[AXSDCustomDetectionController _customPipedInFileUpdated]_block_invoke
+ _objc_msgSend$_customPipedInFileUpdated
+ _objc_msgSend$_processCustomPipedFile
+ _objc_msgSend$analyzeFileAtURL:forDetectors:
+ _objc_msgSend$array
+ _objc_msgSend$detectorIdentifier
+ _objc_msgSend$firstObject
+ _objc_msgSend$globallyUniqueString
+ _objc_msgSend$hasNotified
+ _objc_msgSend$kShotCustomPipeFixedPath
+ _objc_msgSend$moveItemAtPath:toPath:error:
+ _objc_msgSend$processInfo
+ _objc_msgSend$setDetectorIdentifier:
+ _objc_msgSend$setHasNotified:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_setProperty_nonatomic_copy
CStrings:
+ ".claimed-%@"
+ "Custom Detection Controller (file): analyzing %@ against %lu detector(s)"
+ "Custom Detection Controller (file): doorbell rang but no enabled custom detectors; discarding %@"
+ "Custom Detection Controller (file): doorbell rang but no file at %@; ignoring"
+ "Custom Detection Controller (file): finished analyzing %@"
+ "Custom Detection Controller (file): no enabled custom detectors to analyze against %@"
+ "Custom Detection Controller (file): no requests added for %@; aborting analysis"
+ "Custom Detection Controller (file): request complete"
+ "Custom Detection Controller (file): request failed: %@"
+ "Custom Detection Controller (file): result — top class id=%@ confidence=%f (%lu classes)"
+ "Custom Detection Controller (file): unable to add request for %@: %@"
+ "Custom Detection Controller (file): unable to build request for %@ %@"
+ "Custom Detection Controller (file): unable to create file analyzer for %@: %@"
+ "com.apple.accessibility.kshot.custompipe"
```
