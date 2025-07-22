## localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

-3500.97.2.0.0
-  __TEXT.__text: 0x43f98
+3500.101.2.0.0
+  __TEXT.__text: 0x445b8
   __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__objc_stubs: 0x2be0
-  __TEXT.__objc_methlist: 0x1664
-  __TEXT.__const: 0x1128
-  __TEXT.__cstring: 0x3d45
-  __TEXT.__objc_methname: 0x577a
-  __TEXT.__constg_swiftt: 0x184c
-  __TEXT.__swift5_typeref: 0xbe5
-  __TEXT.__swift5_reflstr: 0xf03
-  __TEXT.__swift5_fieldmd: 0xaa0
+  __TEXT.__objc_stubs: 0x2b80
+  __TEXT.__objc_methlist: 0x165c
+  __TEXT.__const: 0x11e8
+  __TEXT.__cstring: 0x3dab
+  __TEXT.__objc_methname: 0x5736
+  __TEXT.__constg_swiftt: 0x1870
+  __TEXT.__swift5_typeref: 0xc19
+  __TEXT.__swift5_reflstr: 0x1013
+  __TEXT.__swift5_fieldmd: 0xb70
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__oslogstring: 0x25ad
-  __TEXT.__swift5_proto: 0x68
-  __TEXT.__swift5_types: 0x98
+  __TEXT.__swift5_assocty: 0xd8
+  __TEXT.__oslogstring: 0x24f2
+  __TEXT.__swift5_proto: 0x74
+  __TEXT.__swift5_types: 0x9c
   __TEXT.__objc_classname: 0x290
-  __TEXT.__objc_methtype: 0x1b42
+  __TEXT.__objc_methtype: 0x1b48
   __TEXT.__swift5_capture: 0x1a4
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__gcc_except_tab: 0x558
-  __TEXT.__unwind_info: 0xf90
-  __TEXT.__eh_frame: 0xc90
+  __TEXT.__gcc_except_tab: 0x554
+  __TEXT.__unwind_info: 0xfc0
+  __TEXT.__eh_frame: 0xc80
   __DATA_CONST.__auth_got: 0xb68
-  __DATA_CONST.__got: 0x7d0
-  __DATA_CONST.__auth_ptr: 0x290
-  __DATA_CONST.__const: 0xf90
-  __DATA_CONST.__cfstring: 0x760
+  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__auth_ptr: 0x2b0
+  __DATA_CONST.__const: 0x1330
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x148

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x3160
-  __DATA.__objc_selrefs: 0x1680
+  __DATA.__objc_selrefs: 0x1660
   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x14d8
-  __DATA.__data: 0x2828
-  __DATA.__bss: 0xd88
-  __DATA.__common: 0x218
+  __DATA.__data: 0x2868
+  __DATA.__bss: 0xf08
+  __DATA.__common: 0x228
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Speech.framework/Speech

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
-  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriPowerInstrumentation.framework/SiriPowerInstrumentation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B2B02020-0A28-30E7-A81E-04F7ED2B6F46
-  Functions: 1365
+  UUID: 9655F0DD-5716-362B-8D57-FD44273DDEBD
+  Functions: 1377
   Symbols:   454
-  CStrings:  1670
+  CStrings:  1664
 
Symbols:
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_SFSpeechAssetManager
- _OBJC_CLASS_$_RBSProcessHandle
- _OBJC_CLASS_$_RBSProcessIdentifier
- _OBJC_CLASS_$_RBSProcessPredicate
CStrings:
+ "-[LSRConnection downloadAssetsForConfig:clientID:expiration:detailedProgress:]"
+ "-[LSRConnection downloadAssetsForConfig:clientID:expiration:detailedProgress:]_block_invoke_6"
+ "LiveTranscription"
+ "Maximum number of recognizers reached"
+ "OfflineTranscription"
+ "Vv44@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24@\"NSDate\"32B40"
+ "Vv44@0:8@16@24@32B40"
+ "currentCalendar"
+ "date"
+ "dateByAddingUnit:value:toDate:options:"
+ "downloadAssetsForConfig:clientID:expiration:detailedProgress:"
+ "systemClientId"
- "%s Connection (%{public}@) cannot use pre-recorded speech recognition; cannot start from the background"
- "%s Status of process identifier of connection (%{public}@) could not be determined"
- "-[LSRConnection downloadAssetsForConfig:clientID:detailedProgress:]"
- "-[LSRConnection downloadAssetsForConfig:clientID:detailedProgress:]_block_invoke_6"
- "Vv36@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24B32"
- "Vv36@0:8@16@24B32"
- "com.apple.frontboard.visibility"
- "countOfRecognizers"
- "currentState"
- "downloadAssetsForConfig:clientID:detailedProgress:"
- "endowmentNamespaces"
- "handleForPredicate:error:"
- "i16@0:8"
- "identifierWithPid:"
- "predicateMatchingIdentifier:"
- "processIdentifier"
- "taskState"

```
